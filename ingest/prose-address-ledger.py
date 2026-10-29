#!/usr/bin/env python3
"""p536 — Gap 535-E: extract GitHub-shaped addresses from PROSE, not just tables.

The base's existing address ledger (ingest/address-ledger.py, p530) indexes
addresses by how many passes MENTION them.  Gap 535-E registered the residue it
cannot see: an address named inside a *sentence* on a curated page — a stack
description, a dependency list, a "built with" clause — is already "mentioned",
so the recall instrument scores it as known while no table row files it.
`comet-ml/opik` (Apache-2.0, 23.0k stars) sat in that residue for one pass;
`Crosstalk-Solutions/Project-NOMAD` for eleven.

This instrument splits the corpus on RENDERED ROLE rather than on file:

  FILED     the address occurs inside a table row (a line whose first
            non-space character is `|`) on a curated page
  PROSE     the address occurs on a curated page, but never in a table row
  HISTORY   the address occurs only in trending history / evidence / archive

PROSE-minus-FILED is the promotion queue this pass works.  It is a strictly
smaller and strictly more actionable set than the pass-count queue, because the
base has already judged these addresses worth writing a sentence about.

Usage:  python3 -I ingest/prose-address-ledger.py [--tsv OUT]
"""
import os
import re
import sys
import collections

ADDR = re.compile(r'github\.com/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)')

# Paths that are NOT repositories even though they match the address shape.
NOT_A_REPO = {
    'orgs', 'topics', 'features', 'about', 'pricing', 'marketplace', 'apps',
    'settings', 'sponsors', 'collections', 'trending', 'explore', 'login',
    'readme', 'site', 'blog', 'security', 'customer-stories',
}

CURATED = [
    'agents/top.md',
    'repos/foundations.md',
    'verticals/solutions.md',
    'compose/patterns.md',
    'intel/market.md',
    'intel/trends.md',
]

def norm(owner, repo):
    repo = re.sub(r'\.git$', '', repo)
    return f'{owner.lower()}/{repo.lower()}'

def scan(path):
    """Yield (address, in_table_row) for every address occurrence in a file."""
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                row = line.lstrip().startswith('|')
                for owner, repo in ADDR.findall(line):
                    if owner.lower() in NOT_A_REPO:
                        continue
                    yield norm(owner, repo), row
    except (IsADirectoryError, PermissionError):
        return

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    filed, prose = set(), set()
    prose_sites = collections.defaultdict(set)

    for rel in CURATED:
        if not os.path.exists(rel):
            print(f'MISSING CURATED PAGE: {rel}', file=sys.stderr)
            continue
        for addr, in_row in scan(rel):
            if in_row:
                filed.add(addr)
            else:
                prose.add(addr)
                prose_sites[addr].add(rel)

    history = set()
    for dirpath, dirnames, filenames in os.walk('.'):
        if any(part in ('.git',) for part in dirpath.split(os.sep)):
            continue
        for name in filenames:
            if not name.endswith(('.md', '.tsv', '.txt', '.json')):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), '.')
            if rel in CURATED:
                continue
            for addr, _ in scan(rel):
                history.add(addr)

    queue = sorted(prose - filed)

    out = [('address', 'prose_pages', 'also_in_history', 'curated_sites')]
    for addr in queue:
        sites = sorted(prose_sites[addr])
        out.append((addr, str(len(sites)), 'yes' if addr in history else 'no',
                    ';'.join(sites)))

    dest = None
    if '--tsv' in sys.argv:
        dest = sys.argv[sys.argv.index('--tsv') + 1]
        with open(dest, 'w', encoding='utf-8') as fh:
            for row in out:
                fh.write('\t'.join(row) + '\n')

    print(f'curated pages scanned : {len(CURATED)}')
    print(f'FILED  (in table rows): {len(filed)}')
    print(f'PROSE  (sentences only): {len(prose)}')
    print(f'HISTORY (elsewhere)   : {len(history)}')
    print(f'PROSE-minus-FILED     : {len(queue)}   <- the p536 promotion queue')
    if dest:
        print(f'written: {dest}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
