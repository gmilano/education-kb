#!/usr/bin/env python3
"""P121 repair -- the 5 cells ACTION P confirmed against the live tree.

Anchoring, per P120-E's lesson. p120's repair v1 anchored on a LINE NUMBER and
broke when the same pass prepended its sections; v2 anchored on a bare token and
over-matched rows that were ABOUT a repair. So this one anchors on the full
(slug-bearing row prefix + exact old cell) and additionally refuses any row that
already carries a correction marker. Idempotent by construction: the old cell is
gone after the first run, so a second run matches nothing.

Every repair below was verified against raw.githubusercontent.com this pass
(verify.2026-10-11.tsv), not taken from a carried verdict.
"""
import os, sys, re

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'

# (page, anchor-substring-identifying-the-row, old-cell, new-cell)
REPAIRS = [
 ('agents/top.md',
  '[`artcc/freelingo`](https://github.com/artcc/freelingo) | **165** | 164 |',
  '| 🟢 MIT | 🟢 live |',
  '| 🔴 **AGPL-3.0** ⚠️ **was 🟢 MIT** | 🟢 live |'),
 ('verticals/solutions.md',
  '[`portabilis/i-educar`](https://github.com/portabilis/i-educar) | SIS (LATAM, BR) | **718** |',
  '| 🔴 AGPL-3.0 | 🔴 no |',
  '| 🔴 **GPL-2.0** ⚠️ **was 🔴 AGPL-3.0** | 🔴 no |'),
 ('verticals/solutions.md',
  '[`frappe/education`](https://github.com/frappe/education) | 🟡 AGPL-3 | 🟡 `partial-pin`',
  '| 🟡 AGPL-3 |',
  '| 🟡 **GPL-3.0** ⚠️ **was 🟡 AGPL-3** |'),
 ('verticals/solutions.md',
  '[`frappe/education`](https://github.com/frappe/education) | 🟢 MIT | — | npm,py |',
  '| 🟢 MIT | — | npm,py |',
  '| 🔴 **GPL-3.0** ⚠️ **was 🟢 MIT** | — | npm,py |'),
 ('intel/market.md',
  '[`portabilis/i-educar`](https://github.com/portabilis/i-educar) (AGPL-3.0, **718★**, branch',
  '(AGPL-3.0, **718★**, branch',
  '(GPL-2.0 — `P121-A`, **718★**, branch'),
]

CORRECTION_MARK = re.compile(r'⚠️\s*\*\*was\b|\bpublished\s*\|', re.I)

applied, skipped = 0, []
for page, anchor, old, new in REPAIRS:
    fp = os.path.join(ROOT, page)
    lines = open(fp, encoding='utf-8').read().splitlines(keepends=True)
    hits = [i for i, l in enumerate(lines) if anchor in l and old in l]
    if not hits:
        skipped.append((page, anchor[:60], 'no row matches (already repaired?)')); continue
    if len(hits) > 1:
        skipped.append((page, anchor[:60], f'AMBIGUOUS: {len(hits)} rows')); continue
    i = hits[0]
    if CORRECTION_MARK.search(lines[i]):
        skipped.append((page, anchor[:60], 'row already carries a correction marker')); continue
    lines[i] = lines[i].replace(old, new, 1)
    open(fp, 'w', encoding='utf-8').write(''.join(lines))
    print(f'REPAIRED {page}:{i+1}  {old.strip()}  ->  {new.strip()}')
    applied += 1

for p, a, why in skipped:
    print(f'SKIP     {p}  [{a}]  {why}')
print(f'\napplied={applied} skipped={len(skipped)}')
