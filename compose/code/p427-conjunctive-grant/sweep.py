"""p427 — the population arm: how many payloads on this base are conjunctive grants?

A finding without a denominator is an anecdote.  `p427` found ONE conjunctive grant in
the ten addresses it read first-hand, which says nothing about how many the base already
carries unlabelled.  This sweep answers that over every licence payload committed to this
repository — the only corpus available offline.

A measurement, never a failure: it exits 0 whatever it finds, because the population is
not a contract.  The CONTRACT is `test_conjunctive_grant.py`.

    python3 -I sweep.py --root ../../..

No network.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from conjunctive_grant import classify  # noqa: E402

LICENCE_HINTS = ('license', 'licence', 'copying', 'unlicense')


def is_payload(name):
    low = name.lower()
    return any(h in low for h in LICENCE_HINTS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    args = ap.parse_args()

    rows = []
    skipped = 0
    for dirpath, dirnames, filenames in os.walk(args.root):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '__pycache__')]
        for fn in filenames:
            if not is_payload(fn):
                continue
            # A .md is prose ABOUT licences, not a payload.
            if fn.lower().endswith(('.md', '.py', '.tsv', '.json')):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding='utf-8') as fh:
                    body = fh.read()
            except (OSError, UnicodeDecodeError):
                skipped += 1
                continue
            r = classify(body)
            rows.append((os.path.relpath(path, args.root), r))

    conj = [(p, r) for p, r in rows if r['mode'] == 'CONJUNCTIVE']
    disj = [(p, r) for p, r in rows if r['mode'] == 'DISJUNCTIVE']

    print('# p427 conjunctive-grant sweep')
    print('# payloads read: %d   unreadable: %d' % (len(rows), skipped))
    print('# CONJUNCTIVE: %d   DISJUNCTIVE: %d   SINGLE: %d'
          % (len(conj), len(disj), len(rows) - len(conj) - len(disj)))
    print('')
    if conj:
        print('## conjunctive grants — a distributor owes EVERY notice listed')
        for p, r in sorted(conj):
            print('  %-66s %-14s notices=%d  derived_from=%s'
                  % (p, '+'.join(r['families']), len(r['holders']),
                     r['derived_from'] or '-'))
            for h in r['holders']:
                print('      holder: %s' % h)
    else:
        print('## no conjunctive grant in this corpus')
    print('')
    if disj:
        print('## disjunctive grants — p228.dual_grant is the authority on these')
        for p, r in sorted(disj):
            print('  %-66s %s' % (p, '+'.join(r['families'])))
    # A measurement, never a failure (p279's rule).
    return 0


if __name__ == '__main__':
    sys.exit(main())
