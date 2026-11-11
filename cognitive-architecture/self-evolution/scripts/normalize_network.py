#!/usr/bin/env python3
"""Normalize associative-network.md: repair mangled table rows, recompute
domain/summary counts, optionally add skills.

Root cause it fixes: repeated fuzzy patches strip leading pipes from data rows
(``    **x** | t | e |``) and stack pipes on summary rows (``||||| DOMAIN | 3 ||``).
verify_headers.py then reports every domain as 0 rows.

Usage:
  python normalize_network.py            # dry-run report
  python normalize_network.py --write
  python normalize_network.py --write --add TRADING:name:tags:edges
"""

import argparse
import re
from pathlib import Path

NETWORK = Path(__file__).resolve().parent.parent.parent / \
    "mind-map-cognition" / "references" / "associative-network.md"

DOMAIN_RE = re.compile(r'^##\s*Domain:\s*(.+?)\s*(?:\((\d+)\s*skills?\))?\s*$')
ROW_RE = re.compile(r'^\s*\|*\s*\*\*(.+?)\*\*\s*\|(.*)$')


def parse(path):
    """-> (header_lines, [(domain, [(name, tags, edges)])])"""
    header, domains = [], []
    current = None
    for line in path.read_text(encoding='utf-8').splitlines():
        m = DOMAIN_RE.match(line)
        if m:
            current = {'name': m.group(1).strip(), 'rows': []}
            domains.append(current)
            continue
        if line.startswith('## Summary'):
            current = None
            continue
        if current is None:
            header.append(line) if not domains else None
            continue
        r = ROW_RE.match(line)
        if r:
            name = r.group(1).strip()
            if name in ('Skill', 'Total rows', 'Domain'):
                continue
            cells = [c.strip() for c in r.group(2).split('|')]
            tags = cells[0] if cells else ''
            edges = cells[1] if len(cells) > 1 else ''
            current['rows'].append((name, tags, edges))
    return header, domains


def add_skills(domains, specs):
    by_name = {d['name'].upper(): d for d in domains}
    for spec in specs:
        domain, name, tags, edges = spec.split(':', 3)
        dom = by_name.get(domain.upper())
        if dom is None:
            dom = {'name': domain, 'rows': []}
            domains.append(dom)
            by_name[domain.upper()] = dom
        if any(r[0] == name for r in dom['rows']):
            continue
        dom['rows'].append((name, tags, edges))


def render(header, domains):
    body_domains = [d for d in domains if d['rows']]
    rows_total = sum(len(d['rows']) for d in body_domains)
    unique = {r[0] for d in body_domains for r in d['rows']}

    out = list(header)
    # rewrite header block counts
    for i, line in enumerate(out):
        if line.startswith('Last updated:'):
            import datetime
            out[i] = f"Last updated: {datetime.date.today().isoformat()}"
        elif line.startswith('Total skills:'):
            out[i] = f"Total skills: {len(unique)}"
        elif line.startswith('Total rows:'):
            out[i] = f"Total rows: {rows_total}"
    out.append('')
    for d in body_domains:
        n = len(d['rows'])
        out.append(f"## Domain: {d['name']} ({n} skill{'s' if n != 1 else ''})")
        out.append('| Skill | Tags | Edges |')
        out.append('|-------|------|-------|')
        for name, tags, edges in d['rows']:
            out.append(f"| **{name}** | {tags} | {edges} |")
        out.append('')
    out.append('---')
    out.append('')
    out.append('## Summary')
    out.append('| Domain | Count |')
    out.append('|--------|-------|')
    for d in sorted(body_domains, key=lambda x: x['name'].upper()):
        out.append(f"| {d['name']} | {len(d['rows'])} |")
    out.append(f"| **Total rows** | **{rows_total}** |")
    out.append('')
    out.append(f"**Note**: {rows_total} rows = {len(unique)} unique skills "
               f"+ {rows_total - len(unique)} cross-domain duplicates, "
               f"{len(body_domains)} domains. Cross-domain dups are intentional.")
    out.append('')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--add', action='append', default=[],
                    help='DOMAIN:name:tags:edges')
    args = ap.parse_args()

    header, domains = parse(NETWORK)
    # dedupe rows within a domain, preserve order
    cleaned = []
    for d in domains:
        seen, rows = set(), []
        for r in d['rows']:
            if r[0] in seen:
                continue
            seen.add(r[0])
            rows.append(r)
        cleaned.append({'name': d['name'], 'rows': rows})
    if args.add:
        add_skills(cleaned, args.add)

    text = render(header, cleaned)
    total = sum(len(d['rows']) for d in cleaned if d['rows'])
    print(f"parsed domains={len(domains)} nonempty={len([d for d in cleaned if d['rows']])} rows={total}")
    for d in cleaned:
        if not d['rows']:
            print(f"  dropped empty domain: {d['name']}")
    if args.write:
        NETWORK.write_text(text, encoding='utf-8')
        print(f"written: {NETWORK}")
    else:
        print("dry-run (use --write)")


if __name__ == '__main__':
    main()
