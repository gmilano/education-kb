#!/usr/bin/env python3
"""`899-G1` — rebuild the `logged-not-shelved` ledger with the hardened `p887` extractor.

The p860 ledger was built with an ad-hoc regex BEFORE `lib/slug_extract.py` existed.
p899 found its number-one row (`Li-Evan/Bloom`, logged 50x) is a slug-truncation phantom.
This rebuilds the same question with the extractor that has 64 controls behind it, and
emits the DELTA against p860 so the artefact rate is measured rather than asserted.

No network.  Run from the repo root:  python3 -I compose/code/p900-ledger-rebuild/build_ledger.py
"""
import os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'compose', 'code', 'lib'))
from slug_extract import extract_slugs  # noqa: E402

# The LIVE shelves: the pages an engagement actually reads.
SHELVES = ['agents/top.md', 'repos/foundations.md', 'verticals/solutions.md',
           'compose/patterns.md']
# Excluded from the "logged" corpus: archived pre-rewrite snapshots are not live logging.
SKIP_DIRS = {'.git', 'archive'}


def md_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(('.md', '.tsv')):
                yield os.path.join(dirpath, fn)


def read(p):
    with open(p, encoding='utf-8', errors='replace') as fh:
        return fh.read()


def main():
    # 1. shelved population
    shelved = set()
    for rel in SHELVES:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            for s in extract_slugs(read(p)):
                shelved.add(s.lower())

    # 2. logged population, counted by FILE (one file naming a repo 9 times is one log)
    logged = collections.Counter()
    where = collections.defaultdict(set)
    for p in md_files():
        rel = os.path.relpath(p, ROOT)
        for s in set(x.lower() for x in extract_slugs(read(p))):
            logged[s] += 1
            where[s].add(rel)

    rows = [(s, n) for s, n in logged.items() if s not in shelved]
    rows.sort(key=lambda r: (-r[1], r[0]))

    out = os.path.join(ROOT, 'evidence', 'logged-not-shelved.2026-11-18-p900.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('rank\taddress\tfiles_logging\tstatus\n')
        for i, (s, n) in enumerate(rows, 1):
            fh.write('%d\t%s\t%d\tLOGGED_NEVER_SHELVED\n' % (i, s, n))

    # 3. delta vs the stale p860 ledger
    old = os.path.join(ROOT, 'evidence', 'logged-not-shelved.2026-11-16-p860.tsv')
    old_rows = []
    if os.path.exists(old):
        for line in read(old).splitlines()[1:]:
            f = line.split('\t')
            if len(f) >= 2:
                old_rows.append(f[1].strip().lower())
    new_set = set(s for s, _ in rows)
    all_new_logged = set(logged)
    print('shelved slugs (4 live shelves) : %d' % len(shelved))
    print('logged slugs (whole live repo) : %d' % len(logged))
    print('logged-not-shelved (p900)      : %d' % len(rows))
    print('p860 ledger rows               : %d' % len(old_rows))
    gone = [s for s in old_rows if s not in all_new_logged]
    promoted = [s for s in old_rows if s in shelved]
    print('p860 rows NOT extractable now  : %d  (regex artefacts / archive-only)' % len(gone))
    print('p860 rows now SHELVED          : %d' % len(promoted))
    print('p900 rows absent from p860     : %d' % len([s for s in new_set if s not in old_rows]))
    print('\n-- top 25 of the rebuilt ledger --')
    for i, (s, n) in enumerate(rows[:25], 1):
        print('%3d  %-52s %3d' % (i, s, n))
    print('\n-- a sample of p860 rows the p887 extractor does NOT reproduce --')
    for s in gone[:25]:
        print('    %s' % s)
    print('\nwrote %s' % os.path.relpath(out, ROOT))


if __name__ == '__main__':
    main()
