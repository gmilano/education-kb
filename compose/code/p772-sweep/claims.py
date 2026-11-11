#!/usr/bin/env python3
"""p772 — extract (address, CLAIMED licence family) pairs from the shelves that
publish licence cells. This is ACTION p771-C's population: a grant cell can only
be wrong where a grant is claimed."""
import re, sys, json, collections

LINK = re.compile(r'\[([^\]\n]{0,300}?)\]\(\s*https?://github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*?)(?:\.git)?(?:[/#?][^\s)]*)?\s*\)')
FAM = [
    ('Apache-2.0',    r'apache[\s-]*(?:licen[cs]e[\s,]*)?(?:v)?2(?:\.0)?|apache2'),
    ('MIT',           r'\bMIT\b'),
    ('BSD-3-Clause',  r'BSD[\s-]*3'),
    ('BSD-2-Clause',  r'BSD[\s-]*2'),
    ('CC-BY-4.0',     r'CC[\s-]*BY[\s-]*4'),
    ('CC-BY-SA-4.0',   r'CC[\s-]*BY[\s-]*SA'),
    ('CC0-1.0',        r'CC0'),
    ('EPL-2.0',        r'EPL[\s-]*2'),
    ('AGPL-3.0-only', r'AGPL[\s-]*(?:v)?3'),
    ('LGPL-2.1-only', r'LGPL[\s-]*(?:v)?2'),
    ('GPL-2.0-only',  r'(?<!A)(?<!L)GPL[\s-]*(?:v)?2'),
    ('LGPL-3.0-only', r'LGPL[\s-]*(?:v)?3'),
    ('GPL-3.0-only',  r'(?<!A)(?<!L)GPL[\s-]*(?:v)?3'),
    ('MPL-2.0',       r'MPL[\s-]*2'),
    ('ISC',           r'\bISC\b'),
    ('Zlib',          r'\bzlib\b'),
    ('Unlicense',     r'\bunlicense\b'),
]
rows = []
for path in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    for ln, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.lstrip().startswith('|'):
            continue                      # licence cells live in TABLE ROWS
        links = LINK.findall(line)
        if not links:
            continue
        fams = [f for f, pat in FAM if re.search(pat, line, re.I)]
        if len(fams) != 1:
            continue                      # ambiguous or none -> not a clean claim
        # D10: ONLY the row's subject (first link) is described by the licence cell.
        _text, owner, repo = links[0]
        rows.append({'slug': f'{owner}/{repo}', 'family': fams[0],
                     'file': path, 'line': ln, 'links_on_row': len(links)})
# one claim per (slug, family)
seen, out = set(), []
for r in rows:
    k = (r['slug'], r['family'])
    if k in seen: continue
    seen.add(k); out.append(r)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
c = collections.Counter(r['family'] for r in out)
print(f'clean licence claims: {len(out)}  (distinct addresses: {len({r["slug"] for r in out})})')
for f, n in c.most_common():
    print(f'   {f:16s} {n}')
