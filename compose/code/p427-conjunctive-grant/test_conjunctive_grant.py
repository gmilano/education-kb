"""p427 — controls for the conjunctive-grant classifier.

Every fixture but one is a payload this pass read FIRST-HAND at a SHA on 2026-10-25.
The single synthetic fixture is the DISJUNCTIVE control and is named
`disjunctive-SYNTHETIC-elgg-shape.LICENSE` so it can never be mistaken for a read.

Runs from this directory (`p355-cwd-portability`: the Makefile recipe cd's in).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conjunctive_grant import (  # noqa: E402
    classify,
    holders,
    notice_obligation,
    title_hits,
)

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')

UNIMCP = 'mit+isc-unimcp-1980.LICENSE'
UTN = 'isc-utn-mcp-748.LICENSE'
SPBSTU = 'mit-spbstu-mcp-1064.LICENSE'
GPL = 'gpl-3.0-moodle-local-mcp-35149.LICENSE'
APACHE = 'apache-2.0-mcp-builder-11345.LICENSE'
DISJ = 'disjunctive-SYNTHETIC-elgg-shape.LICENSE'

FAILURES = []


def read(name):
    with open(os.path.join(FIX, name), encoding='utf-8') as fh:
        return fh.read()


def check(label, got, want):
    if got == want:
        print('   ok   %-58s %r' % (label, got))
    else:
        print('   FAIL %-58s got=%r want=%r' % (label, got, want))
        FAILURES.append(label)


# ─────────────────────────── C1-C5: the positive, read first-hand
body = read(UNIMCP)
r = classify(body)
check('C1  UniMCP mode', r['mode'], 'CONJUNCTIVE')
check('C2  UniMCP families', r['families'], ['MIT', 'ISC'])
check('C3  UniMCP scope marker', r['scope'], 'portions of')
check('C4  UniMCP declares its upstream', r['derived_from'], 'utn-mcp')
check('C5  UniMCP holders, accent preserved', holders(body),
      ['MaxiFG', 'Joaquín Peñalva'])

# 🔴 C6 is the whole point: the published cell said MIT, and MIT owes ONE notice.
check('C6  UniMCP notice obligation is TWO, not one', notice_obligation(body), 2)

# ─────────────────────────── C7-C10: stock GPL-3.0, the load-bearing negative
# It names `GNU Affero General Public License` in its own section 13 and contains
# `at your option` twice.  Both naive detectors fire on it; neither guard lets it.
gpl = read(GPL)
check('C7  stock GPL-3.0 is SINGLE', classify(gpl)['mode'], 'SINGLE')
check('C8  stock GPL-3.0 families', classify(gpl)['families'], ['GPL'])
check('C9  stock GPL-3.0 notice obligation', notice_obligation(gpl), 1)
# 🔵 Three distinct contaminants live in this one payload and all three are excluded by
# the year requirement alone: the FSF steward notice (named), the wrapped clause text at
# lines 157 and 426, and the `<year>  <name of author>` appendix placeholder at line 635.
check('C10 stock GPL-3.0 FSF boilerplate is not a holder', holders(gpl), [])

# ─────────────────────────── C11-C14: single-family positives
isc = read(UTN)
check('C11 utn-mcp ISC is SINGLE', classify(isc)['mode'], 'SINGLE')
check('C12 utn-mcp families', classify(isc)['families'], ['ISC'])
mit = read(SPBSTU)
check('C13 stock MIT is SINGLE', classify(mit)['mode'], 'SINGLE')
check('C14 stock MIT families', classify(mit)['families'], ['MIT'])

# ─────────────────────────── C15-C16: Apache-2.0 stock text
ap = read(APACHE)
check('C15 stock Apache-2.0 is SINGLE', classify(ap)['mode'], 'SINGLE')
# 🔵 NOT an empty expectation: this Apache-2.0 text has its appendix FILLED IN, so the
# payload does name a real holder, while its two wrapped `copyright ...` prose lines (38,
# 70) are excluded.  The vendored skill is Anthropic's, carried inside `HyNuwa/UniMCP`.
check('C16 stock Apache-2.0 with a filled appendix names its holder',
      holders(ap), ['Anthropic, PBC'])

# ─────────────────────────── C17-C19: the disjunctive shape stays p228's
dj = read(DISJ)
check('C17 disjunctive is not reported CONJUNCTIVE', classify(dj)['mode'], 'DISJUNCTIVE')
check('C18 disjunctive notice obligation is ONE (a choice)', notice_obligation(dj), 1)
check('C19 disjunctive names both options', classify(dj)['families'], ['MIT'])

# ─────────────────────────── C20-C22: guard 1 in isolation
# A family named in PROSE is not a title.  This is the exact line from stock GPL-3.0.
prose = 'MIT License\n\n  13. Use with the GNU Affero General Public License.\n'
check('C20 prose family mention is not a title',
      [f for _, f in title_hits(prose)], ['MIT'])
check('C21 prose mention does not make it conjunctive',
      classify(prose)['mode'], 'SINGLE')

# ─────────────────────────── C23: guard 2 in isolation
# Two real standalone titles, NO scope sentence -> a restatement, not a second grant.
unscoped = 'MIT License\n\nCopyright (c) 2026 A\n\nISC License\n\nCopyright (c) 2026 B\n'
check('C22 two titles without a scope sentence stay SINGLE',
      classify(unscoped)['mode'], 'SINGLE')
# ... and the same payload WITH one becomes conjunctive.
scoped = ('MIT License\n\nCopyright (c) 2026 A\n\n'
          'Portions of this software are derived from upstream and remain under its\n'
          'original license:\n\nISC License\n\nCopyright (c) 2026 B\n')
check('C23 the scope sentence alone flips the verdict',
      classify(scoped)['mode'], 'CONJUNCTIVE')
check('C24 and it carries both holders',
      notice_obligation(scoped), 2)

print('')
if FAILURES:
    print('🔴 %d control(s) FAILED: %s' % (len(FAILURES), ', '.join(FAILURES)))
    sys.exit(1)
print('🟢 24 controls PASS — conjunctive vs disjunctive vs single, with stock GPL-3.0')
print('   and stock Apache-2.0 as the negatives both guards exist for.')
