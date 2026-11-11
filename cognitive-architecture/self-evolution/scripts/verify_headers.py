#!/usr/bin/env python3
"""
Verify frontmatter version matches latest changelog entry across all cognitive-architecture skills.
Also validates associative-network.md section counts match actual table rows.

Usage: python verify_headers.py [--skills-dir PATH] [--network PATH]
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict


def parse_frontmatter(content):
    """Extract frontmatter from SKILL.md content."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"\'')
    return fm


def parse_changelog_version(content):
    """Extract latest version from changelog table."""
    # Find changelog table
    changelog_match = re.search(r'##\s*(?:VI\.?\s*)?CHANGELOG.*?\| Date \| Version \| Change \|(.*?)(?:\n##|\n---|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not changelog_match:
        return None
    table = changelog_match.group(1)
    # First data row after header
    rows = [r.strip() for r in table.strip().split('\n') if r.strip() and not r.strip().startswith('|---')]
    if not rows:
        return None
    # Parse first row: | Date | Version | Change |
    parts = [p.strip() for p in rows[0].split('|') if p.strip()]
    if len(parts) >= 2:
        return parts[1]
    return None


def parse_associative_network(content):
    """Parse associative-network.md for section headers and row counts."""
    sections = {}
    # Match: ## Domain: NAME (N skills) OR ## Domain: NAME
    header_pattern = r'## Domain:\s*([^(\n]+)(?:\s*\(\d+\s*skills?\))?'
    for match in re.finditer(header_pattern, content):
        domain = match.group(1).strip()
        # Extract count if present
        count_match = re.search(r'\((\d+)\s*skills?\)', match.group(0))
        count = int(count_match.group(1)) if count_match else 0
        sections[domain] = {'header_count': count, 'actual_rows': 0}

    # Count actual rows per domain (lines with | **skill_name** |)
    current_domain = None
    for line in content.split('\n'):
        # Detect domain header - handle both with and without skill count
        header_match = re.match(r'## Domain:\s*([^(\n]+)(?:\s*\()?', line)
        if header_match and 'Summary' not in line:
            current_domain = header_match.group(1).strip()
            continue
        # Stop counting when we hit the Summary section
        if line.startswith('## Summary') or line.startswith('---'):
            current_domain = None
            continue
        # Count skill rows - handle |||| **skill** | or ||||| **skill** | format
        # Must have bold skill name and NOT be the header row ("Skill | Tags") or separator ("---")
        if (current_domain and re.match(r'^\|+\s*\*\*.+?\*\* \|', line)
                and 'Skill | Tags' not in line
                and '---' not in line):
            if current_domain in sections:
                sections[current_domain]['actual_rows'] += 1

    return sections


def main():
    parser = argparse.ArgumentParser(description='Verify skill headers and network counts')
    parser.add_argument('--skills-dir', default='.', help='Directory containing skill subdirectories')
    parser.add_argument('--network', default='../mind-map-cognition/references/associative-network.md', help='Path to associative-network.md')
    args = parser.parse_args()

    # Resolve relative paths relative to script's location
    base_dir = Path(__file__).parent
    skills_dir = (base_dir / args.skills_dir).resolve()
    # scripts/ is inside self-evolution/; mind-map-cognition/ is sibling of self-evolution/
    network_path = base_dir.parent.parent / "mind-map-cognition" / "references" / "associative-network.md"

    errors = []
    warnings = []

    # 1. Check each skill's frontmatter version vs changelog
    print("Checking skill version headers vs changelog...")
    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and (d / 'SKILL.md').exists()]

    for skill_dir in sorted(skill_dirs):
        skill_file = skill_dir / 'SKILL.md'
        content = skill_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)
        fm_version = fm.get('version', '').strip()
        changelog_version = parse_changelog_version(content)

        if fm_version and changelog_version and fm_version != changelog_version:
            errors.append(f"{skill_dir.name}: frontmatter version={fm_version} != changelog version={changelog_version}")
        elif not fm_version:
            warnings.append(f"{skill_dir.name}: missing version in frontmatter")
        elif not changelog_version:
            warnings.append(f"{skill_dir.name}: no changelog or changelog version not parseable")

    # 2. Check associative network section counts
    print("Checking associative network section counts...")
    if network_path.exists():
        network_content = network_path.read_text(encoding='utf-8')
        sections = parse_associative_network(network_content)

        for domain, counts in sections.items():
            if counts['header_count'] != counts['actual_rows']:
                errors.append(f"Network domain '{domain}': header says {counts['header_count']} skills, actual rows = {counts['actual_rows']}")

        # Verify total
        total_header = sum(c['header_count'] for c in sections.values())
        total_actual = sum(c['actual_rows'] for c in sections.values())
        if total_header != total_actual:
            errors.append(f"Network total mismatch: headers sum={total_header}, actual rows sum={total_actual}")

        # Check for double-pipe artifacts
        for i, line in enumerate(network_content.split('\n'), 1):
            if '||' in line and not line.strip().startswith('|---') and not line.strip().startswith('| Domain'):
                # Allow header separator lines
                if not re.match(r'\|[\s\-:|]+\|', line.strip()):
                    warnings.append(f"Network line {i}: possible double-pipe artifact: {line.strip()[:80]}")
    else:
        errors.append(f"Associative network not found at {network_path}")

    # Report
    if warnings:
        print("\n⚠️  WARNINGS:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("\n❌ ERRORS:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("\n✅ All checks passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())