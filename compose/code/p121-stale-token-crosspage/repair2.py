#!/usr/bin/env python3
"""P121 repair batch 2 -- the 5 cells the WIDENED sweep confirmed live.

Trending pages are APPEND-ONLY, so a stale token inside a dated historical
section is NOT edited here; it is recorded instead. Only live recommendation
cells are repaired.

Two of these five are a defect class no prior pass of this KB named: the page is
MORE restrictive than the tree. `UniTime/unitime` is Apache-2.0 and was published
GPL-3.0; `pupilfirst/pupilfirst` is MIT and was published AGPL-3.0. Both rows
told a studio "do not build on this". That error never shows up in a sweep that
looks only for permissive-over-restrictive.
"""
import os, re, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
REPAIRS = [
 ('verticals/solutions.md',
  '[`unitime/unitime`](https://github.com/UniTime/unitime) | timetabling | **350** |',
  '| 🔴 GPL-3.0 | 🔴 no |',
  '| 🟢 **Apache-2.0** ⚠️ **was 🔴 GPL-3.0** | 🟢 **yes** |'),
 ('verticals/solutions.md',
  '[`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | LMS | **979** |',
  '| 🔴 AGPL-3.0 | 🔴 no |',
  '| 🟢 **MIT** (split: `docs/` CC-BY-SA-4.0) ⚠️ **was 🔴 AGPL-3.0** | 🟢 **yes, via the MIT arm** |'),
 ('verticals/solutions.md',
  '[`course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud) | MOOC (APAC, CN) | **1 173** |',
  '| 🟢 MIT | 🟢 **yes** |',
  '| 🔴 **GPL-2.0** ⚠️ **was 🟢 MIT** | 🔴 no |'),
 ('repos/foundations.md',
  '[`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **153** |',
  '| 🟢 MIT |',
  '| 🟢 **BSD-3-Clause** ⚠️ **was 🟢 MIT** |'),
 ('agents/top.md',
  '[`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **453** | — |',
  '| 🟢 MIT | 🟢 live |',
  '| 🟢 **Apache-2.0** ⚠️ **was 🟢 MIT** | 🟢 live |'),
]
CORRECTION_MARK = re.compile(r'⚠️\s*\*\*was\b', re.I)
applied, skipped = 0, []
for page, anchor, old, new in REPAIRS:
    fp = os.path.join(ROOT, page)
    lines = open(fp, encoding='utf-8').read().splitlines(keepends=True)
    hits = [i for i, l in enumerate(lines) if anchor in l and old in l]
    if len(hits) != 1:
        skipped.append((page, anchor[:55], f'{len(hits)} matches')); continue
    i = hits[0]
    if CORRECTION_MARK.search(lines[i]):
        skipped.append((page, anchor[:55], 'already corrected')); continue
    lines[i] = lines[i].replace(old, new, 1)
    open(fp, 'w', encoding='utf-8').write(''.join(lines))
    print(f'REPAIRED {page}:{i+1}  {old.strip()} -> {new.strip()}')
    applied += 1
for p, a, w in skipped: print(f'SKIP     {p} [{a}] {w}')
print(f'\napplied={applied} skipped={len(skipped)}')
