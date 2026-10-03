#!/usr/bin/env python3
"""This pass's measurement: KB coverage per platform, ranked inside each cohort separately.

The file set is NAMED (P227) and is the one that `reproduce_p224.py` proves P224 actually
used: the four INVENTORY files.  Trending/trends/patterns are excluded on purpose -- they are
narrative and history, so a platform discussed at length in them can still have zero rows.

A COMMIT is part of the invocation here, not an option -- and pass 75 learned that the hard
way, on itself.  Measured on the working tree AFTER pass 75 wrote up the K-12 gap, K-12 shows
11 inversions; measured at pass 74's HEAD, it shows 7.  Nothing about the KB's coverage
changed: the prose documenting the gap mentions the stub platforms, and those mentions land in
the same files the metric counts.  A coverage metric read off the tree that documents the
coverage gap is SELF-CONTAMINATING, so the published figure names its commit.

Usage:  python3 measure.py [--at COMMIT] [repo_root]
        --at COMMIT   read the four files from git at COMMIT (reproducible)
        no --at       read the working tree (drifts as the pass writes)
"""
import os
import subprocess
import sys
from coverage import Row, aggregate, inversions, Refusal

INVENTORY = ['agents/top.md', 'repos/foundations.md', 'verticals/solutions.md',
             'intel/market.md']

# Installed-base ORDER only.  Passes 74 and 75 both measured EGRESS_BLOCKED on every
# market-share source (listedtech.com, cubite.io, axiomflow.app, en.wikipedia.org), so no
# `share=` is set on any row: P224 step 4, enforced by Row() itself.
COHORTS = {
    'K-12 / institutions': [
        Row('Google Classroom', 'K-12', 'institutions', rank=1),
        Row('Canvas', 'K-12', 'institutions', rank=2, aliases=('Instructure',)),
        Row('Schoology', 'K-12', 'institutions', rank=3),
        Row('PowerSchool', 'K-12', 'institutions', rank=4),
        Row('Infinite Campus', 'K-12', 'institutions', rank=5),
        Row('Skyward', 'K-12', 'institutions', rank=6),
        Row('Moodle', 'K-12', 'institutions', rank=7, self_hostable=True),
    ],
    'HigherEd / institutions': [
        Row('Canvas', 'HigherEd', 'institutions', rank=1, aliases=('Instructure',)),
        Row('Moodle', 'HigherEd', 'institutions', rank=2, self_hostable=True),
        Row('Blackboard', 'HigherEd', 'institutions', rank=3, aliases=('Anthology',)),
        Row('Brightspace', 'HigherEd', 'institutions', rank=4, aliases=('D2L',)),
        Row('Google Classroom', 'HigherEd', 'institutions', rank=5),
    ],
}


def main():
    argv = sys.argv[1:]
    commit = None
    if argv and argv[0] == '--at':
        if len(argv) < 2:
            print('FAIL --at needs a commit')
            return 1
        commit, argv = argv[1], argv[2:]
    root = argv[0] if argv else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')

    if commit:
        def read(p):
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            r = subprocess.run(['git', '-C', root, 'show', f'{commit}:{rel}'],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise SystemExit(f'FAIL cannot read {commit}:{rel} '
                                 f'(fetch history: git fetch --depth=6 origin main)')
            return r.stdout
        source = f'git {commit}'
    else:
        read = None
        source = 'working tree (NOT reproducible -- see the module docstring)'

    paths = [os.path.join(root, p) for p in INVENTORY]
    if not commit:
        missing = [p for p in paths if not os.path.exists(p)]
        if missing:
            print('FAIL missing inventory files: ' + ', '.join(missing))
            return 1

    print(f'source: {source}')
    print('file set (NAMED, per P227):')
    for p in INVENTORY:
        print(f'  {p}')

    print('\nplatform\tsegment\tunit\trank\tlines\toccurrences\tverdict')
    for label, rows in COHORTS.items():
        agg = aggregate(paths, rows, read=read)
        cov = {k: v for k, v in agg['coverage'].items()}
        for r in sorted(rows, key=lambda r: r.rank):
            c = cov[r.platform]
            verdict = 'ABSENT' if c['absent'] else ('STUB' if c['occurrences'] < 10 else 'covered')
            print(f'{r.platform}\t{r.segment}\t{r.unit}\t{r.rank}\t'
                  f'{c["lines"]}\t{c["occurrences"]}\t{verdict}')
        inv = inversions(rows, cov)
        print(f'# {label}: {len(inv)} inversion(s)')
        for i in inv:
            f = '' if i['factor'] is None else f', {i["factor"]}x'
            print(f'#   {i["expected_higher"]}(rank-higher, {i["occ_higher"]} occ) '
                  f'< {i["expected_lower"]}({i["occ_lower"]} occ){f}')

    # The refusal, exercised against the real tree rather than fixtures.
    try:
        inversions(COHORTS['K-12 / institutions'] + COHORTS['HigherEd / institutions'],
                   aggregate(paths, COHORTS['K-12 / institutions'], read=read)['coverage'])
        print('\nFAIL the cross-cohort rank was computed')
        return 1
    except Refusal as e:
        print(f'\nPASS cross-cohort rank refused on the real tree: {e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
