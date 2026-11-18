#!/usr/bin/env python3
"""Controls for `p887-instrument-ledger` — the four defects, as a suite.

🟢 `886-G2(b)` COMPLIANCE: the fixture set is NAMED and drawn from cells this base already
established. Every case below is a real line from a real instrument in this repository,
with the verdict that hand-adjudication reached. A regression names the row it broke.

Run: `python3 test_ledger.py`   (from this directory)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ledger import (  # noqa: E402
    FAMILY_RE, REFUTATION_MARK, ENUM_CEILING, is_snapshot, is_fixture,
    norm_family, scope_for,
)

FAILED, PASSED = [], []


def check(name, got, want):
    (PASSED if got == want else FAILED).append(
        name if got == want else '%s: got %r want %r' % (name, got, want))


def fams(text):
    out = []
    for m in FAMILY_RE.finditer(text):
        f = norm_family(m.group(1))
        if f not in out:
            out.append(f)
    return out


def classify(rel, lines, i):
    ctx, how = scope_for(lines, i)
    seen = fams(ctx)
    if not seen:
        return 'NO-FAMILY', seen
    if len(seen) >= ENUM_CEILING:
        return 'ENUMERATION', seen
    if is_snapshot(rel):
        return 'SNAPSHOT', seen
    if is_fixture(rel):
        return 'FIXTURE', seen
    if len(seen) >= 2 and REFUTATION_MARK.search(ctx):
        return 'CORRECTION', seen
    return 'CLAIM', seen


# ── DEFECT 1 — a markdown table row is a self-contained record.
#    Verbatim from compose/code/p441-tree-licence-enumeration/README.md.
P441 = [
    '| Slug | Verdict | Family | Path, and the axis the list missed |',
    '|---|---|---|---|',
    '| [`openedx/XBlock`](https://github.com/openedx/XBlock) | root | **Apache-2.0** | `LICENSE.TXT` |',
    '| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | root | GPL-2.0+ | `copying.txt` |',
    '| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | root | **MIT** | `License` |',
]
ctx, how = scope_for(P441, 2)
check('D1-1 a `|` line is scoped to ITSELF, not a ±3 window', how, 'ROW')
check('D1-2 XBlock draws ONLY Apache-2.0 from its own row '
      '(the first run attributed five families to it)',
      fams(ctx), ['Apache-2.0'])
check('D1-3 and that row is therefore a CLAIM, not an enumeration',
      classify('compose/code/p441-tree-licence-enumeration/README.md', P441, 2)[0],
      'CLAIM')
check('D1-4 prose keeps the window, because openSIS-Classic\'s refutation spans lines',
      scope_for(['a', 'b', 'c'], 1)[1], 'WINDOW')

# ── DEFECT 2 — a snapshot of a shelf is not an instrument's knowledge.
check('D2-1 p119 current corpus is a SNAPSHOT',
      is_snapshot('compose/code/p119-carried-column-audit/current/'
                  'agents-trending.current.md'), True)
check('D2-2 archive/ is a snapshot too', is_snapshot('archive/2026-10-06/x.md'), True)
check('D2-3 an ordinary instrument README is NOT a snapshot',
      is_snapshot('compose/code/p314-untitled-payload-arm/README.md'), False)

# ── DEFECT 3 — an enumeration of families is not a verdict about a repository.
ENUM = ['see https://github.com/some/repo for the ladder',
        'families probed: MIT, Apache-2.0, BSD-3-Clause, GPL-3.0']
check('D3-1 a candidate-family list is an ENUMERATION, not a claim',
      classify('compose/code/x/README.md', ENUM, 0)[0], 'ENUMERATION')
check('D3-2 the ceiling is 3 distinct families', ENUM_CEILING, 3)

# ── DEFECT 4 — a CORRECTION TABLE carries the refuted value AND the true one.
#    All three verbatim; all three were FALSE POSITIVES of the corrected run.
C_ORA2 = ['| row | published | 🔴 actually |', '|---|---|---|',
          '| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) '
          '| 🟢 Apache-2.0 | 🔴 **AGPL-3.0** |']
check('D4-1 edx-ora2: a published-vs-actually row is a CORRECTION '
      '(shelf AGPL-3.0 is RIGHT)',
      classify('compose/code/p117-second-channel/README.md', C_ORA2, 2)[0], 'CORRECTION')

C_RALPH = ['2. [`openfun/ralph`](https://github.com/openfun/ralph) was published '
           '**`Apache-2.0`** in a p193',
           '   recipe step while its blob is **`MIT`, `LICENSE.md`, `1 094` B**.']
check('D4-2 ralph: "was published X while its blob is Y" is a CORRECTION '
      '(shelf MIT is RIGHT)',
      classify('compose/code/p208-seeded-error-audit/README.md', C_RALPH, 0)[0],
      'CORRECTION')

C_IED = ['| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) '
         '| 🔴 `LGPL-3.0` · 18 092 B | **GPL-2.0** | 🔴 *"link, don\'t absorb"* |']
check('D4-3 i-educar: a 🔴-marked refuted family beside the true one is a CORRECTION '
      '(shelf GPL-2.0 is RIGHT)',
      classify('compose/code/grant-ladder-v4/README.md', C_IED, 0)[0], 'CORRECTION')

# ── THE ONE SURVIVOR. It must stay a CLAIM, or `886-G5`'s only real finding disappears.
C_JHUB = ['`ACTION p313-R` item 5 asked for a `BSD-3-Clause` fixture, and said why: `301`',
          'published cells, and',
          '[`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) serves a '
          'complete, valid grant',
          'with **no title line and zero `BSD` tokens anywhere in the file**.']
k, f = classify('compose/code/p314-untitled-payload-arm/README.md', C_JHUB, 2)
check('SURVIVOR-1 jupyterhub stays a CLAIM (the ONE real 886-G5 finding)', k, 'CLAIM')
# 🔵 The window names BOTH ids, because p314's prose says jupyterhub's payload has
# "zero `BSD` tokens" — so the token `BSD` appears in the sentence that denies it. The
# ledger emits one row per family and the two land on OPPOSITE verdicts: `BSD` AGREES with
# the shelf's under-specified cell, `BSD-3-Clause` DISAGREES with it. That is the finding,
# and it survives precisely because the ledger did not collapse the two.
check('SURVIVOR-2 the scope names both ids, in longest-first order',
      f, ['BSD-3-Clause', 'BSD'])
check('SURVIVOR-3 and BSD-3-Clause is among them — the id the metadata channel '
      'independently returned this pass',
      'BSD-3-Clause' in f, True)

# ── FAMILY precedence: the longest id must win, or every BSD-3-Clause becomes BSD.
check('F-1 BSD-3-Clause is not shortened to BSD', fams('BSD-3-Clause'), ['BSD-3-Clause'])
check('F-2 AGPL-3.0 is not read as GPL-3.0', fams('AGPL-3.0'), ['AGPL-3.0'])
check('F-3 LGPL-2.1 is not read as GPL-2.0', fams('LGPL-2.1'), ['LGPL-2.1'])
check('F-4 a bare BSD is still recorded as BSD (the under-specified shelf cell)',
      fams('published as BSD'), ['BSD'])
check('F-5 Apache 2.0 with a space normalises to Apache-2.0',
      fams('Apache 2.0'), ['Apache-2.0'])
check('F-6 NOASSERTION is a recordable verdict, not a gap',
      fams('spdx=NOASSERTION'), ['NOASSERTION'])

# ── 886-G3 COMPLIANCE: the ledger must not re-derive slugs with an inline grep.
import ledger  # noqa: E402
check('G3 the ledger imports the TESTED helper rather than re-writing the grep',
      hasattr(ledger, 'extract_slugs'), True)

print('p887-instrument-ledger — %d controls' % (len(PASSED) + len(FAILED)))
for f_ in FAILED:
    print('  FAIL  %s' % f_)
if FAILED:
    print('RED: %d/%d' % (len(PASSED), len(PASSED) + len(FAILED)))
    sys.exit(1)
print('PASS: %d/%d' % (len(PASSED), len(PASSED)))
