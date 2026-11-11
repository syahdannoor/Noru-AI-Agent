#!/usr/bin/env python3
"""
Cross-reference associative-network.md against actual skills on disk.
Detects missing nodes (skills not in network) and dead refs (network entries for deleted skills).

Usage: python cross_ref_network.py [--skills-dir PATH] [--network PATH]
"""

import re
import sys
import json
import argparse
import subprocess
import os
import yaml
from pathlib import Path


# Directories/files to skip - not Noru skills
SKIP_ENTRIES = {
    # Hermes-bundled macOS skills (irrelevant on Windows)
    'apple-notes', 'apple-reminders', 'findmy', 'imessage', 'macos-computer-use',
    'apple',  # directory
    # Hermes social media skill
    'xurl',
    'social-media',  # directory
    # Platform-unsupported / orphaned stubs
    'minecraft-modpack-server', 'python-debugpy', 'research-paper-writing',
    'backtesting-harness', 'ensemble', 'process-watchdog', 'smart_money',
    # Archived/legacy skills
    'hermes-gateway-api-server', 'legacy-data-ingestion', 'nor5-execution-script',
    'nor5-phase-two-plan', 'pine-script', 'portable-dev-tools-windows',
    'telegram-media-send', 'windows-system-diagnostics', 'process-watchdog',
    'smart_money', 'backtesting-harness', 'ensemble',
    # Non-skill directories
    'references', 'templates', 'scripts', 'assets', '__pycache__',
    'evaluation', 'inference', 'models', 'research', 'training', 'vector-databases',
    # Sub-skills that aren't top-level
    'segment-anything', 'audiocraft', 'lm-evaluation-harness', 'vllm',
    'creative-ideation', 'obliteratus', 'trace', 'skill', 'nor5-execution-script',
    'nor5-phase-two-plan', 'pine-script', 'legacy-data-ingestion',
    'hermes-gateway-api-server', 'portable-dev-tools-windows',
    'windows-system-diagnostics', 'telegram-media-send',
    # Additional Hermes-bundled skills that appear on disk but aren't Noru skills
    'audiocraft-audio-generation', 'evaluating-llms-harness', 'findmy',
    'serving-llms-vllm', 'obliteratus',
    # Low-quality skills created by knowledge-harvester (filter catches but doesn't prevent creation)
    'wikipedia-main-page',
    # Archived skills in .archive directory
    '4d-prediction', 'airtable', 'android-apk-modification', 'api-model-probe',
    'apple-notes', 'apple-reminders', 'architecture-diagram', 'arxiv',
    'ascii-video', 'backtesting-harness', 'baoyu-infographic', 'claude-code',
    'claude-design', 'codebase-inspection', 'codex', 'computer-use',
    'dashboard-launch', 'design-md', 'dogfood', 'ensemble',
    'findmy', 'fishing-tally-processing', 'gif-search',
    'hermes-agent-skill-authoring', 'hermes-gateway-api-server',
    'himalaya', 'humanizer', 'imessage', 'indonesian-education-system',
    'indonesian-marine-data', 'legacy-data-ingestion', 'llm-wiki',
    'nextjs-rsc-payload-regex', 'node-inspect-debugger', 'nor5-execution-script',
    'nor5-phase-two-plan', 'notion', 'obsidian', 'opencode',
    'p5js', 'pine-script', 'popular-web-designs', 'portable-dev-tools-windows',
    'powerpoint', 'process-watchdog', 'project_roadmap', 'python-debugpy',
    'requesting-code-review', 'sawo-pdf-extraction', 'school-communication',
    'simplify-code', 'sketchfab-model-sourcing', 'smart_money',
    'songsee', 'songwriting-and-ai-music', 'spike',
    'sports-scores', 'streaming-site-scraper', 'systematic-debugging',
    'teams-meeting-pipeline', 'telegram-media-send',
    'test-driven-development', 'tor-proxy', 'windows-system-diagnostics',
    'wsl-proxy-routing', 'xurl', 'youtube-content',
}


def get_skill_name_from_skill_md(skill_md_path):
    """Extract skill name from SKILL.md frontmatter."""
    try:
        content = skill_md_path.read_text(encoding='utf-8')
        # First try YAML parsing
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    if frontmatter and 'name' in frontmatter:
                        return frontmatter['name']
                except Exception:
                    pass
        # Fallback: regex extract name field from frontmatter (only at start of line)
        import re
        match = re.search(r'^name:\s*([^\n]+)', content, re.MULTILINE)
        if match:
            return match.group(1).strip().strip('"\'')
    except Exception:
        pass
    # Fallback to directory name
    return skill_md_path.parent.name


def get_skills_on_disk(skills_dir):
    """Scan skills directory (and subdirectories) for actual skill directories."""
    skills = set()
    skills_dir = Path(skills_dir)
    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return skills
    
    for root, dirs, files in os.walk(skills_dir):
        # Skip archived, hidden directories, and virtual environments
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'archive' and d != '.venv' and d != 'venv']
        
        # Check for SKILL.md in subdirectories (standard skill structure)
        if 'SKILL.md' in files:
            skill_md_path = Path(root) / 'SKILL.md'
            # Skip archived skills and skills inside virtual environments
            parts = skill_md_path.parts
            if '.archive' in parts or '.venv' in parts or 'venv' in parts:
                continue
            name = get_skill_name_from_skill_md(skill_md_path)
            if name not in SKIP_ENTRIES and name:
                skills.add(name)
        
        # Also check for loose .md files with skill frontmatter in cognitive-architecture/ directory only
        # These are skills created by knowledge-harvester directly as .md files (not in subdirectories)
        if 'cognitive-architecture' in Path(root).parts:
            for file in files:
                if file.endswith('.md') and file != 'SKILL.md':
                    md_path = Path(root) / file
                    # Skip if in .archive
                    if '.archive' in md_path.parts:
                        continue
                    name = get_skill_name_from_skill_md(md_path)
                    if name not in SKIP_ENTRIES and name:
                        skills.add(name)
    return skills


def get_skills_from_network(network_path):
    """Extract skill names from associative-network.md tables."""
    content = network_path.read_text(encoding='utf-8')
    skills = set()
    # Match table rows: | **skill_name** | tags | edges |
    for match in re.finditer(r'\|\s*\*\*(.+?)\*\*\s*\|', content):
        skill_name = match.group(1).strip()
        # Skip header/footer rows
        if skill_name not in ('Skill', 'Total rows', 'Domain'):
            # Skip archived skills
            if skill_name not in SKIP_ENTRIES:
                skills.add(skill_name)
    return skills


def main():
    parser = argparse.ArgumentParser(description='Cross-reference associative-network.md against actual skills on disk.')
    parser.add_argument('--skills-dir', default='../../..', help='Directory containing skill subdirectories. Default: hermes/skills/ root.')
    parser.add_argument('--network', default='../mind-map-cognition/references/associative-network.md', help='Path to associative-network.md')
    args = parser.parse_args()

    # Resolve relative paths relative to script's location
    base_dir = Path(__file__).parent
    skills_dir = (base_dir / args.skills_dir).resolve()
    # scripts/ is inside self-evolution/; mind-map-cognition/ is sibling of self-evolution/
    network_path = base_dir.parent.parent / "mind-map-cognition" / "references" / "associative-network.md"

    if not network_path.exists():
        print(f"❌ Network file not found: {network_path}")
        return 1

    disk_skills = get_skills_on_disk(skills_dir)
    network_skills = get_skills_from_network(network_path)

    print(f"Skills on disk: {len(disk_skills)}")
    print(f"Skills in network: {len(network_skills)}")

    # Missing from network (on disk but not in network)
    missing = disk_skills - network_skills
    # Dead refs (in network but not on disk)
    dead = network_skills - disk_skills

    has_issues = False

    if missing:
        has_issues = True
        print(f"\n❌ SKILLS MISSING FROM NETWORK ({len(missing)}):")
        for skill in sorted(missing):
            print(f"  - {skill}")

    if dead:
        has_issues = True
        print(f"\n💀 DEAD REFS IN NETWORK ({len(dead)}):")
        for skill in sorted(dead):
            print(f"  - {skill}")

    if not has_issues:
        print("\n✅ Network matches disk skills perfectly.")
        return 0
    # Summary for programmatic use
    result = {
        'disk_skills': sorted(disk_skills),
        'network_skills': sorted(network_skills),
        'missing_from_network': sorted(missing),
        'dead_refs': sorted(dead),
    }

    # Optionally output JSON for consumption
    if '--json' in sys.argv:
        print(json.dumps(result, indent=2))

    return 1 if has_issues else 0
    return 1 if has_issues else 0


if __name__ == '__main__':
    sys.exit(main())