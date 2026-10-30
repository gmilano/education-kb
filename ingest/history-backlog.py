#!/usr/bin/env python3
"""p539 — the HISTORY backlog, ranked.  The instrument the empty queue demanded.

p538 emptied the promotion queue.  Nine passes of supply had come out of
PROSE-minus-FILED, and when the last of it was read the base was left with no
queue at all, while the four mandated global legs and all four regional legs
returned nothing unfiled for the TENTH consecutive pass.  p538 wrote that
p539 "must either generate a new one (the HISTORY bucket holds 4 144 distinct
addresses against 240 filed -- a 5.8 % filing rate) or find supply in a channel
this base has not used."

This is the first half.  HISTORY-minus-FILED is the backlog: every address this
base has ever written down in trending history, evidence or archive and never
filed in a table row on a curated page.

TWO THINGS THIS INSTRUMENT DOES THAT THE PROSE LEDGER DOES NOT.

1. IT CARRIES AS-WRITTEN SPELLING THROUGH THE HISTORY BUCKET.
   ingest/prose-address-ledger.py (p536) records as-written spellings only for
   curated pages -- its history scan discards `_written` and keeps the key.
   That is p538's defect in a second place: a key is not an address, and the
   history bucket is where this pass's supply comes from.  Every spelling seen
   anywhere is kept here, and the emitted address is the most frequent one.

2. IT RANKS BY RECALL *AND* SAYS WHY THE RANK IS WEAK.
   p533 measured what a pure recall rank does: its queue head
   (DMontgomery40/mcp-canvas-lms, 16 distinct passes) had NO LICENCE FILE at 15
   probed paths, so the top of the queue was not promotable at all, while
   freeCodeCamp/freeCodeCamp sat at rank 18 with 458k stars.  Recall measures
   how often this base has TALKED about an address, which is a property of the
   base, not of the address.  So `mentions` is emitted as a tie-breaker and the
   gates (live, grant) are what a successor filters on -- not the rank.

Usage:  python3 -I ingest/history-backlog.py [--tsv OUT] [--min-mentions N]
"""
import os
import re
import sys
import collections

ADDR = re.compile(r'github\.com/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)')

# Identical to the prose ledger's list -- a path that matches the address shape
# and is not a repository.  Kept in sync by hand; divergence would silently
# change the denominator this pass reports.
NOT_A_REPO = {
    'orgs', 'topics', 'features', 'about', 'pricing', 'marketplace', 'apps',
    'settings', 'sponsors', 'collections', 'trending', 'explore', 'login',
    'readme', 'site', 'blog', 'security', 'customer-stories',
    # p539: API and search paths that match the address shape.  `search` reached
    # the backlog as `search/repositories` with 59 mentions across 27 files --
    # it is the REST endpoint this base queries, not a repository.
    'search', 'repos', 'users', 'gists', 'enterprise', 'contact', 'join',
    'notifications', 'new', 'account', 'dashboard', 'stars', 'watching',
}

# p539: DOCUMENTATION PLACEHOLDERS, which are the defect the task brief calls
# "never leave a header or example row as data" -- in the address channel.
# `OWNER/REPO` reached the backlog with 62 mentions across 31 files, ranking
# fifth, because this base's own instrument docstrings and usage lines write it
# as an example.  A placeholder is not a finding and must not occupy a queue
# slot that a real address could have.
PLACEHOLDER = {
    'owner/repo', 'owner/name', 'org/repo', 'user/repo', 'owner/repository',
    'owner/repo.git', 'o/r', 'owner/project', 'you/your-repo', 'org/name',
    'someone/something', 'foo/bar', 'example/example', 'user/project',
}

CURATED = [
    'agents/top.md',
    'repos/foundations.md',
    'verticals/solutions.md',
    'compose/patterns.md',
    'intel/market.md',
    'intel/trends.md',
]

PASS_TAG = re.compile(r'\bp(\d{2,4})\b')


def strip_git(repo):
    return re.sub(r'\.git$', '', repo)


def match_key(owner, repo):
    """Comparison key only.  p538: never emit this as an address."""
    return f'{owner.lower()}/{strip_git(repo).lower()}'


def as_written(owner, repo):
    return f'{owner}/{strip_git(repo)}'


def scan(path):
    """Yield (key, as_written, in_table_row) per occurrence."""
    try:
        with open(path, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                row = line.lstrip().startswith('|')
                for owner, repo in ADDR.findall(line):
                    if owner.lower() in NOT_A_REPO:
                        continue
                    if match_key(owner, repo) in PLACEHOLDER:
                        continue
                    yield match_key(owner, repo), as_written(owner, repo), row
    except (IsADirectoryError, PermissionError, FileNotFoundError):
        return


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    filed = set()
    spellings = collections.defaultdict(collections.Counter)

    for rel in CURATED:
        for key, written, in_row in scan(rel):
            spellings[key][written] += 1
            if in_row:
                filed.add(key)

    history = set()
    sites = collections.defaultdict(set)
    passes = collections.defaultdict(set)

    for dirpath, dirnames, filenames in os.walk('.'):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for name in filenames:
            if not name.endswith(('.md', '.tsv', '.txt', '.json')):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), '.')
            if rel in CURATED:
                continue
            # A pass tag in the FILENAME is evidence of which pass wrote it;
            # evidence files are named `<thing>.<date>-p<N>.tsv`.
            fname_passes = set(PASS_TAG.findall(name))
            for key, written, _row in scan(rel):
                history.add(key)
                spellings[key][written] += 1
                sites[key].add(rel)
                passes[key] |= fname_passes

    backlog = sorted(history - filed)

    floor = 0
    if '--min-mentions' in sys.argv:
        floor = int(sys.argv[sys.argv.index('--min-mentions') + 1])

    out = [('address', 'match_key', 'mentions', 'distinct_files',
            'distinct_passes', 'as_written_variants', 'spelling_conflict',
            'example_site')]
    conflicts = 0
    rows = []
    for key in backlog:
        seen = spellings[key]
        ranked = sorted(seen.items(), key=lambda kv: (-kv[1], kv[0]))
        best = ranked[0][0]
        variants = [w for w, _ in ranked]
        conflict = 'yes' if len(variants) > 1 else 'no'
        if conflict == 'yes':
            conflicts += 1
        n_files = len(sites[key])
        if n_files < floor:
            continue
        rows.append((best, key, str(sum(seen.values())), str(n_files),
                     str(len(passes[key])), ';'.join(variants[:4]), conflict,
                     sorted(sites[key])[0]))

    # Rank: distinct files desc, then mentions desc, then address.  p533's
    # warning applies -- this is a recall rank and recall is a property of this
    # base's prose, not of the repository.
    rows.sort(key=lambda r: (-int(r[3]), -int(r[2]), r[0].lower()))
    out.extend(rows)

    dest = None
    if '--tsv' in sys.argv:
        dest = sys.argv[sys.argv.index('--tsv') + 1]
        with open(dest, 'w', encoding='utf-8') as fh:
            for row in out:
                fh.write('\t'.join(row) + '\n')

    print(f'FILED   (table rows, curated) : {len(filed)}')
    print(f'HISTORY (anywhere else)       : {len(history)}')
    print(f'BACKLOG (HISTORY - FILED)     : {len(backlog)}')
    print(f'emitted at floor >={floor} files  : {len(rows)}')
    print(f'spelling conflicts in backlog : {conflicts}')
    if dest:
        print(f'written: {dest}')


if __name__ == '__main__':
    main()
