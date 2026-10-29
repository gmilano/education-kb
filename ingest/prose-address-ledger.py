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

p538 — THE DEFECT THIS INSTRUMENT INTRODUCED, AND THE FIX.

p537 promoted eight agents off the p536 queue and found that 13 of 29 queued
addresses (45 %) carried an owner or repository spelling that was not canonical.
It attributed this to the ledger: "the ledger lower-cases every address it
emits (norm())".  p538 tested that attribution against the corpus and it is
correct, and worse than stated: for every one of the six addresses re-measured
(upstream1119/Traceable-Ideological-Education-RAG, oas114/EduShield,
dougpenny/SwiftyPSCore, shishiv/EDUCA, guruduan/SIMG, h9-tec/Awesome_Arabic_NLP)
the CURATED PROSE ALREADY CARRIED THE CANONICAL SPELLING.  The 45 % was not
inherited from the corpus and was not a research gap.  This instrument
manufactured it, by emitting its own comparison key as if it were data.

So the queue is now TWO columns.  `address` carries the spelling as the corpus
wrote it — which is what a successor pastes into a table row or a probe — and
`match_key` carries the lower-cased form, which is what the set arithmetic
needs and which must never leave this file as an address.  Where one normalised
key has more than one as-written spelling in the corpus, every spelling is
emitted in `as_written_variants` and the row is flagged, because that is a real
inconsistency on the pages rather than an artefact of this script.

GitHub redirects on case, so a mis-cased address still resolves — which is
exactly why nine passes could carry one in prose without noticing.  A table row
must not: it is the thing successors copy.

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

def strip_git(repo):
    return re.sub(r'\.git$', '', repo)


def match_key(owner, repo):
    """The COMPARISON key. Lower-cased because GitHub is case-insensitive on
    both owner and repository. p538: this value is for set arithmetic only and
    must never be emitted as an address -- that is the defect p537 measured."""
    return f'{owner.lower()}/{strip_git(repo).lower()}'


def as_written(owner, repo):
    """The address AS THE CORPUS WROTE IT. This is what a successor pastes."""
    return f'{owner}/{strip_git(repo)}'

def scan(path):
    """Yield (match_key, as_written, in_table_row) for every occurrence."""
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                row = line.lstrip().startswith('|')
                for owner, repo in ADDR.findall(line):
                    if owner.lower() in NOT_A_REPO:
                        continue
                    yield match_key(owner, repo), as_written(owner, repo), row
    except (IsADirectoryError, PermissionError):
        return

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    filed, prose = set(), set()
    prose_sites = collections.defaultdict(set)
    # p538: every as-written spelling seen for a key, on curated pages only.
    spellings = collections.defaultdict(collections.Counter)

    for rel in CURATED:
        if not os.path.exists(rel):
            print(f'MISSING CURATED PAGE: {rel}', file=sys.stderr)
            continue
        for key, written, in_row in scan(rel):
            spellings[key][written] += 1
            if in_row:
                filed.add(key)
            else:
                prose.add(key)
                prose_sites[key].add(rel)

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
            for key, _written, _row in scan(rel):
                history.add(key)

    queue = sorted(prose - filed)

    out = [('address', 'match_key', 'as_written_variants', 'spelling_conflict',
            'prose_pages', 'also_in_history', 'curated_sites')]
    conflicts = 0
    for key in queue:
        sites = sorted(prose_sites[key])
        seen = spellings[key]
        # Most frequent as-written spelling wins; ties break on sort order so
        # the output is deterministic across runs.
        ranked = sorted(seen.items(), key=lambda kv: (-kv[1], kv[0]))
        best = ranked[0][0]
        variants = [w for w, _ in ranked]
        conflict = 'yes' if len(variants) > 1 else 'no'
        if conflict == 'yes':
            conflicts += 1
        out.append((best, key, ';'.join(variants), conflict,
                    str(len(sites)), 'yes' if key in history else 'no',
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
    print(f'PROSE-minus-FILED     : {len(queue)}   <- the promotion queue')
    print(f'spelling conflicts    : {conflicts}   '
          f'<- keys with >1 as-written spelling on curated pages')
    print('addresses are emitted AS WRITTEN (p538); match_key is the '
          'lower-cased comparison key and is not an address')
    if dest:
        print(f'written: {dest}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
