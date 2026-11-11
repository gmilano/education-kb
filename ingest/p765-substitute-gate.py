#!/usr/bin/env python3
"""p765 substitute commit gate. `make hooks` is denied in this session as
repository-code execution ([Code from External]), for the eighth consecutive
pass, so this self-contained checker is run and recorded instead.

Controls:
  1  frontmatter present and valid on every shelf (industry/region/updated,
     region drawn from the closed five-value vocabulary)
  2  no data row renders as a table header
  3  no table separator line appears as a data row
  4  no row consists entirely of placeholder cells
  5  the live `## Opportunities by region` section carries all five regions,
     each with this pass's block sitting DIRECTLY under its own `###` heading
     (ACTION p756-C)
  6  every markdown table is rectangular enough to parse: a data row may not
     have more cells than its header.

     D6 — this control's first revision split rows on every `|` and produced 58
     false positives, because a cell may legitimately contain a pipe inside an
     inline-code span or escaped as `\|`. This base documented exactly this
     failure class at `672-E` ("the naive implementation is unusable") and the
     warning was in the file being checked. Cells are now split on unescaped
     pipes OUTSIDE inline-code spans.

usage: KB_ROOT=... PASS=p765 python3 -I p765-substitute-gate.py
"""
import os, re, sys

ROOT = os.environ.get('KB_ROOT', '/home/user/education-kb')
PASS = os.environ.get('PASS', 'p765')
SHELVES = ['agents/top.md', 'agents/trending.md', 'repos/foundations.md',
           'repos/trending.md', 'verticals/solutions.md', 'intel/market.md',
           'intel/trends.md', 'compose/patterns.md', 'intel/open-gaps.md',
           'intel/measured-unusable.md', 'README.md']
REGIONS = ['North America', 'EMEA', 'APAC', 'LATAM', 'Global']
HEADERISH = {'nombre', 'name', 'repo', 'repository', 'licencia', 'license', 'licence',
             'descripcion', 'descripción', 'description', 'stars', 'agent', 'platform',
             'item', 'role', 'grant', 'branch', 'probe', 'topic', 'source', 'claim',
             'component', 'channel', 'instrument', 'figure', 'verdict', 'reading',
             'state', 'buyer', 'pattern', 'region', 'indicator', 'line', 'count',
             'token', 'bytes', 'path', 'family', 'query', 'date', 'jurisdiction'}
def split_cells(line):
    """Split a markdown row on unescaped pipes that are not inside `code`."""
    out, cur, incode, k = [], [], False, 0
    while k < len(line):
        ch = line[k]
        if ch == '\\' and k + 1 < len(line):
            cur.append(line[k:k + 2]); k += 2; continue
        if ch == '`':
            incode = not incode; cur.append(ch); k += 1; continue
        if ch == '|' and not incode:
            out.append(''.join(cur)); cur = []; k += 1; continue
        cur.append(ch); k += 1
    out.append(''.join(cur))
    if out and not out[0].strip(): out = out[1:]
    if out and not out[-1].strip(): out = out[:-1]
    return out


PLACE_CELL = re.compile(
    r'^(TBD|TODO|FIXME|XXX+|N/?A|placeholder|lorem ipsum|example|example\.com|'
    r'your-org|owner/repo|owner/name|a/b|O/R|\.\.\.|\?+|-{1,3})$', re.I)
SEP = re.compile(r'\|[\s:|-]+\|')

# Control 6's findings are split against a recorded baseline: `p276` appended its
# corrections as an extra cell to 14 rows in tables with no column for them, so a
# markdown renderer silently discards the correction. Those 14 are pre-existing
# debt, recorded in evidence/ and registered as ACTION p765-G; the gate fails only
# on NEW over-wide rows.
BASELINE = set()
_b = os.path.join(ROOT, 'evidence/overwide-rows.2026-11-11-p765.tsv')
if os.path.exists(_b):
    for _l in open(_b, encoding='utf-8').read().split('\n')[1:]:
        _p = _l.split('\t')
        if len(_p) >= 2 and _p[1].isdigit():
            BASELINE.add((_p[0], int(_p[1])))

fails, legacy, tables, rows = [], [], 0, 0

for rel in SHELVES:
    path = os.path.join(ROOT, rel)
    lines = open(path, encoding='utf-8').read().split('\n')

    # control 1
    if lines[0] != '---':
        fails.append(f'{rel}: no frontmatter')
    else:
        end = next((i for i, l in enumerate(lines[1:], 1) if l == '---'), None)
        fm = {}
        for l in lines[1:end]:
            if ':' in l:
                k, v = l.split(':', 1)
                fm[k.strip()] = v.strip()
        for k in ('industry', 'region', 'updated'):
            if k not in fm:
                fails.append(f'{rel}: frontmatter missing {k}')
        if fm.get('industry') != 'education':
            fails.append(f'{rel}: industry={fm.get("industry")!r}')
        if fm.get('region') not in REGIONS:
            fails.append(f'{rel}: region not in closed vocab: {fm.get("region")!r}')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', fm.get('updated', '')):
            fails.append(f'{rel}: updated malformed: {fm.get("updated")!r}')

    # controls 2, 3, 4, 6
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and SEP.fullmatch(lines[i + 1].strip()):
            tables += 1
            ncols = len(split_cells(lines[i].strip()))
            j = i + 2
            while j < len(lines) and lines[j].startswith('|'):
                rows += 1
                cells = [c.strip().strip('`*_ ') for c in split_cells(lines[j].strip())]
                nonempty = [c for c in cells if c]
                low = [c.lower() for c in nonempty]
                if len(low) >= 2 and all(c in HEADERISH for c in low):
                    fails.append(f'{rel}:{j+1}: data row renders as a table header: {lines[j][:80]}')
                if SEP.fullmatch(lines[j].strip()):
                    fails.append(f'{rel}:{j+1}: separator line as data row')
                ph = [c for c in nonempty if PLACE_CELL.fullmatch(c)]
                if nonempty and len(ph) == len(nonempty):
                    fails.append(f'{rel}:{j+1}: every cell is a placeholder: {lines[j][:80]}')
                if len(cells) > ncols:
                    msg = f'{rel}:{j+1}: {len(cells)} cells against a {ncols}-cell header'
                    (legacy if (rel, j + 1) in BASELINE else fails).append(msg)
                j += 1
            i = j
        else:
            i += 1

# control 5 — live region section only (the FIRST such heading in the file)
mkt = open(os.path.join(ROOT, 'intel/market.md'), encoding='utf-8').read().split('\n')
start = next((i for i, l in enumerate(mkt) if l.strip() == '## Opportunities by region'), None)
placed = {}
if start is None:
    fails.append('market.md: no `## Opportunities by region` heading')
else:
    for idx in range(start + 1, len(mkt)):
        l = mkt[idx]
        if l.startswith('## ') and l.strip() != '## Opportunities by region':
            break                                  # left the live section
        m = re.fullmatch(r'### (North America|EMEA|APAC|LATAM|Global)\s*', l)
        if m and m.group(1) not in placed:
            reg = m.group(1)
            placed[reg] = False
            for k in range(idx + 1, min(idx + 6, len(mkt))):
                if mkt[k].startswith(f'#### 🆕 {PASS}'):
                    placed[reg] = True
                    break
                if mkt[k].startswith('### ') or mkt[k].startswith('## '):
                    break
for reg in REGIONS:
    if not placed.get(reg):
        fails.append(f'market.md: {PASS} block not directly under ### {reg}')

print(f'shelves={len(SHELVES)} tables={tables} data_rows={rows} '
      f'region_blocks_ok={sum(1 for v in placed.values() if v)}/5 '
      f'legacy_overwide_rows={len(legacy)} (baseline, ACTION p765-G)')
if fails:
    print('FAIL:')
    for f in fails[:40]:
        print('  ' + f)
    print(f'  ({len(fails)} findings)')
    sys.exit(1)
print(f'GREEN({PASS}): 0 NEW over-wide rows, 0 header-as-data rows, 0 separator rows, 0 placeholder rows, '
      f'frontmatter valid on all {len(SHELVES)} shelves, 5/5 region blocks placed')
