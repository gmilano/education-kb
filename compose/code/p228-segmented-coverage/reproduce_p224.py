#!/usr/bin/env python3
"""Proof of P227, run against real git history.

P224 published "229 lines / 389 occurrences in the 4 content files" without naming them.
This searches every 3-, 4- and 5-subset of the eight content files at the commit P224 cited
(pase 73 HEAD) and reports which ones reproduce the figure.  Exactly one 4-subset does.

Usage:  python3 reproduce_p224.py [commit]      (default 81e3e9a = pase 73 HEAD)
Needs the repo's git history; with a --depth 1 clone, fetch --depth=6 first.
"""
import itertools
import subprocess
import sys

FILES = ['agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
         'verticals/solutions.md', 'intel/market.md', 'intel/trends.md', 'compose/patterns.md']
TARGET = (229, 389)
PLATFORM = 'canvas'


def main():
    commit = sys.argv[1] if len(sys.argv) > 1 else '81e3e9a'
    per = {}
    for f in FILES:
        r = subprocess.run(['git', 'show', f'{commit}:{f}'], capture_output=True, text=True)
        if r.returncode != 0:
            print(f'FAIL cannot read {commit}:{f} -- fetch history first '
                  f'(git fetch --depth=6 origin main)')
            return 1
        t = r.stdout
        per[f] = (sum(1 for ln in t.splitlines() if PLATFORM in ln.lower()),
                  t.lower().count(PLATFORM))

    print(f'per-file Canvas at {commit}:')
    for f in FILES:
        print(f'  {f:<26} lines={per[f][0]:<4} occ={per[f][1]}')

    matches, considered = [], 0
    for size in (3, 4, 5):
        for combo in itertools.combinations(FILES, size):
            considered += 1
            agg = (sum(per[f][0] for f in combo), sum(per[f][1] for f in combo))
            if agg == TARGET:
                matches.append(combo)

    four = sum(1 for _ in itertools.combinations(FILES, 4))
    print(f'\nsubsets considered (sizes 3-5): {considered}   (of which 4-subsets: {four})')
    print(f'subsets reproducing {TARGET[0]} lines / {TARGET[1]} occurrences: {len(matches)}')
    for m in matches:
        print('  MATCH: ' + ', '.join(m))

    ok = n = 0
    n += 1
    if len(matches) == 1:
        ok += 1
        print('\nPASS exactly one subset reproduces the published aggregate')
    else:
        print(f'\nFAIL {len(matches)} subsets reproduce it')
    n += 1
    if matches and set(matches[0]) == {'agents/top.md', 'repos/foundations.md',
                                       'verticals/solutions.md', 'intel/market.md'}:
        ok += 1
        print('PASS the reproducing set is the four INVENTORY files, not the four '
              'largest and not the four named "content"')
    else:
        print('FAIL the reproducing set is not the inventory four')
    n += 1
    if per['agents/top.md'] == (111, 241):
        ok += 1
        print('PASS P224\'s single-file figure (111 lines / 241 occ) reproduces exactly')
    else:
        print(f'FAIL agents/top.md is {per["agents/top.md"]}, not (111, 241)')

    print(f'\n{ok}/{n} checks passed')
    return 0 if ok == n else 1


if __name__ == '__main__':
    sys.exit(main())
