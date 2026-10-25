"""p428 — the population arm: every ref-asserting citation on the live shelves.

A MEASUREMENT, never a failure.  It grades each published path against a ref set
captured in `fixtures/`, and reports `UNRESOLVED-REFSET` for every address whose ref
set this pass did not capture — rather than assuming the branch is fine.

    make branch-alias-census
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from branch_alias import classify, is_defect, parse_refset  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, 'fixtures')

# 🔴 SCOPE, and p428 got this wrong on its first measurement.  A recursive sweep of
# `compose/` pulls in `compose/code/**/evidence/*__README.md` — VENDORED COPIES OF OTHER
# PROJECTS' READMEs.  A `master` path in one of those is the upstream project's citation,
# not this base's, and counting them inflated p428's first figure by a factor of ten.
# These nine files are what this base PUBLISHES; `--vendored` grades the other population
# separately and never mixes the two.
SHELVES = ('agents/top.md', 'agents/trending.md', 'repos/foundations.md',
           'repos/trending.md', 'verticals/solutions.md', 'intel/market.md',
           'intel/trends.md', 'compose/patterns.md', 'README.md')

# 🔴 The `(?:/(?:blob|tree|raw))?` form this census first shipped with was WRONG and the
# bug is worth keeping named: with the segment optional, `github.com/o/r/blob/main/x`
# matched with ref=`blob`, and the caller's `'/blob/' in raw` filter then DISCARDED it.
# The arm reported 17 citations where the corpus holds hundreds.  Both shapes are now
# required explicitly, so a path either names a ref or does not match at all.
CITE_RE = re.compile(
    r'(?:https?://)?(?:'
    r'raw\.githubusercontent\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+'
    r'|github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/(?:blob|tree|raw)'
    r')/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_./~-]*)?')


def load_refsets():
    out = {}
    if not os.path.isdir(FIX):
        return out
    for fn in os.listdir(FIX):
        if not fn.endswith('.heads'):
            continue
        key = fn[:-len('.heads')].replace('_', '/', 1).lower()
        with open(os.path.join(FIX, fn), encoding='utf-8') as fh:
            text = fh.read()
        out[key] = parse_refset(text) if text.strip() else None
    return out


def vendored_files(root):
    """Every vendored upstream README under `compose/code/`.

    These are OTHER projects' citations, carried here as evidence.  They are graded so
    the population the mechanism actually bites can be SIZED — never so a defect in one
    of them can be charged to this base.
    """
    out = []
    base = os.path.join(root, 'compose', 'code')
    for dirpath, _dirs, files in os.walk(base):
        for fn in files:
            # 🔴 `.md` alone was WRONG: `p371-backlog-grade/trees/` carries 92 vendored
            # upstream READMEs under a `.readme` extension, and they hold the bulk of
            # this population.  Both extensions, or the arm under-reports tenfold.
            if fn.endswith('.md') or fn.endswith('.readme'):
                out.append(os.path.relpath(os.path.join(dirpath, fn), root))
    return sorted(out)


def main(root, scope='shelves'):
    refsets = load_refsets()
    tally, defects, seen = {}, [], set()
    targets = SHELVES if scope == 'shelves' else vendored_files(root)
    for rel in targets:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8', errors='replace') as fh:
            body = fh.read()
        for raw in CITE_RE.findall(body):
            key = (rel, raw)
            if key in seen:
                continue
            seen.add(key)
            from branch_alias import parse_path
            p = parse_path(raw)
            rs = refsets.get('%s/%s' % (p['owner'], p['repo']), 'MISSING') if p else 'MISSING'
            if rs == 'MISSING':
                rs = None
            r = classify(raw, rs)
            tally[r['verdict']] = tally.get(r['verdict'], 0) + 1
            if is_defect(r['verdict']):
                defects.append((rel, raw, r['verdict'], r['served_by']))

    label = ('the live shelves — what THIS BASE publishes' if scope == 'shelves'
             else 'VENDORED upstream READMEs — what OTHER projects publish')
    print('p428 branch-alias census — ref-asserting citations on %s' % label)
    for v in sorted(tally):
        print('  %-20s %5d' % (v, tally[v]))
    print('  %-20s %5d' % ('TOTAL', sum(tally.values())))
    print()
    if defects:
        print('defects graded against a CAPTURED ref set (%d):' % len(defects))
        for rel, raw, v, served in defects[:60]:
            print('  %-14s %-12s served_by=%-8s %s' % (v, rel, served, raw[:92]))
    else:
        print('no defect gradeable from the captured ref sets')
    print()
    print('🔵 Every UNRESOLVED-REFSET line is an address whose ref set this pass did '
          'not capture.  It is exposure, not a clean bill.')
    print('🔴 Known limitation, declared rather than hidden: this census grades PATHS, '
          'not the prose around them.  A shelf that publishes a path in order to REPORT '
          'that it 404s is graded ABSENT-REF, which is the right verdict about the path '
          'and the wrong one about the sentence.  Read every defect line before acting.')
    return 0


if __name__ == '__main__':
    argv = [a for a in sys.argv[1:] if a != '--vendored']
    sys.exit(main(argv[0] if argv else '../../..',
                  'vendored' if '--vendored' in sys.argv else 'shelves'))
