#!/usr/bin/env python3
"""p537 — `Gap 536-A`'s remedy: a RATCHET on the prose ledger's filed count.

WHY THIS EXISTS
  p536 built ingest/prose-address-ledger.py and called its output a promotion
  queue.  `Gap 536-A` registered the unfinished half: "the instrument has no
  gate ... a future rewrite can silently drop every row it just gained."  That
  is the regression mechanism p528 identified and nobody closed.

WHAT IT GUARANTEES
  The number of addresses FILED IN A TABLE ROW on a curated page may not fall
  between passes.  The baseline lives in ingest/promotion-ratchet.json and is
  committed, so the check is reproducible from the tree alone.

  A pass that legitimately removes a row (a refuted find, a retraction, a fork
  replaced by its upstream) raises nothing and must instead LOWER the baseline
  explicitly, in the same commit, with a reason in `notes`.  That is the point:
  the drop becomes a visible, authored act rather than a silent rewrite.

USAGE
  python3 -I ingest/promotion-ratchet.py            # check against baseline
  python3 -I ingest/promotion-ratchet.py --update   # record current as baseline

EXIT  0 green; 1 the filed count fell below the committed baseline.
"""
import json
import os
import re
import sys
import collections

ADDR = re.compile(r'github\.com/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)')
NOT_A_REPO = {
    'orgs', 'topics', 'features', 'about', 'pricing', 'marketplace', 'apps',
    'settings', 'sponsors', 'collections', 'trending', 'explore', 'login',
    'readme', 'site', 'blog', 'security', 'customer-stories',
}
CURATED = [
    'agents/top.md', 'repos/foundations.md', 'verticals/solutions.md',
    'compose/patterns.md', 'intel/market.md', 'intel/trends.md',
]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, 'ingest', 'promotion-ratchet.json')


def norm(owner, repo):
    return '{}/{}'.format(owner.lower(), re.sub(r'\.git$', '', repo).lower())


def scan(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                row = line.lstrip().startswith('|')
                for owner, repo in ADDR.findall(line):
                    if owner.lower() in NOT_A_REPO:
                        continue
                    yield norm(owner, repo), row
    except (IsADirectoryError, PermissionError, FileNotFoundError):
        return


def measure():
    """Return (filed, prose, history, union) over the committed tree."""
    os.chdir(ROOT)
    filed, prose = set(), set()
    for rel in CURATED:
        if not os.path.exists(rel):
            print('MISSING CURATED PAGE: {}'.format(rel), file=sys.stderr)
            continue
        for addr, in_row in scan(rel):
            (filed if in_row else prose).add(addr)
    history = set()
    for dirpath, dirnames, filenames in os.walk('.'):
        if '.git' in dirpath.split(os.sep):
            continue
        for name in filenames:
            if not name.endswith(('.md', '.tsv', '.txt', '.json')):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), '.')
            if rel in CURATED:
                continue
            for addr, _ in scan(rel):
                history.add(addr)
    # p537: the UNION is printed explicitly.  p536's headline read the HISTORY
    # bucket as if it were the union; HISTORY excludes the curated pages by
    # construction, so it cannot be the denominator of a filing RATE.
    return filed, prose, history, (filed | prose | history)


def main():
    filed, prose, history, union = measure()
    queue = prose - filed
    print('FILED  (table rows on curated pages) : {}'.format(len(filed)))
    print('PROSE  (sentences only)              : {}'.format(len(prose)))
    print('HISTORY(outside the curated pages)   : {}'.format(len(history)))
    print('UNION  (distinct, all buckets)       : {}'.format(len(union)))
    print('filing rate                          : {:.1f}%'.format(
        100.0 * len(filed) / len(union) if union else 0.0))
    print('PROSE-minus-FILED (promotion queue)  : {}'.format(len(queue)))

    if '--update' in sys.argv:
        state = {
            'filed': len(filed),
            'union': len(union),
            'queue': len(queue),
            'pass': sys.argv[sys.argv.index('--pass') + 1] if '--pass' in sys.argv else 'unknown',
            'notes': 'baseline recorded by ingest/promotion-ratchet.py --update',
        }
        with open(STATE, 'w', encoding='utf-8') as fh:
            json.dump(state, fh, indent=2, sort_keys=True)
            fh.write('\n')
        print('🟢 baseline written: {}'.format(STATE))
        return 0

    if not os.path.exists(STATE):
        print('🔴 no baseline at {} — run with --update'.format(STATE))
        return 1
    with open(STATE, encoding='utf-8') as fh:
        base = json.load(fh)
    want = int(base['filed'])
    if len(filed) < want:
        print('🔴 RATCHET BROKEN — filed count FELL from {} ({}) to {}.'.format(
            want, base.get('pass', '?'), len(filed)))
        print('   A pass may lower this, but only explicitly: edit')
        print('   ingest/promotion-ratchet.json in the same commit and say why in `notes`.')
        return 1
    print('🟢 ratchet OK — filed {} >= baseline {} ({})'.format(
        len(filed), want, base.get('pass', '?')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
