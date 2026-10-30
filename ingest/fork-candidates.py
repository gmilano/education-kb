#!/usr/bin/env python3
"""p539 — Gap 538-A, and the correction that `Gap 538-A` itself needed.

🔴 READ THIS FIRST: `Gap 538-A` AS WRITTEN WAS A RESTATED ABSENCE.

  p538 registered: "No instrument here reads a 'forked from' line. 2 of 20
  observed, unbounded above. Gap 538-A."

  That sentence is literally true and substantively misleading, and this file
  was half-written before its author checked. THIS BASE ALREADY GRADES FORK
  LINEAGE, with two instruments, a Makefile gate each, and 23 passing controls:

    compose/code/p404-fork-direction/   grades ONE same-name PAIR from FULL
                                        git histories -- commit-SHA sets, tree
                                        sets, root commits, HEAD ancestry.
                                        11 controls. `make gate-fork-direction`
    compose/code/p405-group-lineage/    grades a WHOLE name-collision GROUP in
                                        O(N) clones instead of O(N^2), reusing
                                        p404's `verdict.grade` so the two cannot
                                        drift. 12 controls, transitive families
                                        via connected components.
                                        `make gate-group-lineage`

  AND IT HAS ALREADY USED THEM ON THE EXACT CLUSTER THIS FILE RANKS FIRST.
  p405's README reports `canvas-mcp` at 23 addresses, 20 clonable, 190 pairs
  graded, and the published finding "42 addresses are 27 projects -- a 1.56x
  overstatement", with 7 of canvas-mcp's 20 addresses genuinely sole projects.
  `Gap 446-C` is closed on the same channel: "Ten addresses, six projects"
  STANDS, with `vishalsachdev` root afe32c3e1721 and `r-huijts` root
  731aa116052b reproducing to the digit from independent clones.

  🔵 SO THE FULL-HISTORY CHANNEL IS STRICTLY STRONGER THAN THE ONE p538 ASKED
  FOR, and p404 exists because of exactly that: a squash-republish shares ZERO
  commits with its source and GitHub shows it no `forked from` line at all.
  A page read cannot see that case. A history read can.

  🔴 The meta-finding, which is worth more than this instrument: THE GAP LEDGER
  LOST TRACK OF THE BASE'S OWN CAPABILITY. `gate-capability-absence` (p392)
  was built for precisely this error -- "an absence keyed on CAPABILITY, not on
  string identity ... one whose refutation is in the base's own harvest log
  under different words" -- and it did not catch `Gap 538-A`, because it runs
  over SHELF absences and not over the gap ledger. Registered as `Gap 539-E`.

WHAT IS THEN ACTUALLY MISSING, AND WHAT THIS FILE IS

  p404 grades a pair. p405 grades a group ONCE YOU KNOW THE GROUP. Neither
  enumerates groups, and nothing in this base asks the prior question:

      ACROSS THE WHOLE CORPUS, WHICH REPOSITORY NAMES ARE HELD BY MORE THAN
      ONE OWNER, AND WHICH OF THOSE COLLISIONS TOUCH A FILED TABLE ROW?

  `canvas-mcp` was graded because somebody noticed it. This instrument finds
  every collision locally, at no network cost, and ranks them by the shape that
  actually costs a reader: FILED-vs-HISTORY, where a curated table row names
  one side and the other side sits only in history. A filed address is what a
  successor pastes.

  So this is a WORK-ORDER GENERATOR for p405, not a replacement for it. It says
  which groups to clone; p405 says what they are. The verdict column a shelf
  cites must come from p405's full-history grading, never from this file and
  never from a `forked from` line alone.

  ⚠️ COVERAGE, stated so silence is not read as coverage: a collision is found
  only when the corpus ALSO names a sibling. A fork of a repository this base
  has never mentioned, or one renamed after forking, is invisible here. The
  collision set is a FLOOR on the fork count, never a ceiling -- and unlike the
  gap as p538 wrote it, it is a bounded, checkable floor.

Usage:  python3 -I ingest/fork-candidates.py [--tsv OUT]
"""
import os
import re
import sys
import collections

ADDR = re.compile(r'github\.com/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9_.-]*[A-Za-z0-9])?)')

NOT_A_REPO = {
    'orgs', 'topics', 'features', 'about', 'pricing', 'marketplace', 'apps',
    'settings', 'sponsors', 'collections', 'trending', 'explore', 'login',
    'readme', 'site', 'blog', 'security', 'customer-stories',
    'search', 'repos', 'users', 'gists', 'enterprise', 'contact', 'join',
    'notifications', 'new', 'account', 'dashboard', 'stars', 'watching',
}

PLACEHOLDER = {'owner/repo', 'owner/name', 'org/repo', 'user/repo',
               'owner/repository', 'foo/bar', 'example/example'}

CURATED = ['agents/top.md', 'repos/foundations.md', 'verticals/solutions.md',
           'compose/patterns.md', 'intel/market.md', 'intel/trends.md']

# Repository names so generic that two owners sharing one is not evidence of a
# fork. Measured from the collision set itself rather than guessed: each of
# these is a name many unrelated education projects pick independently.
GENERIC = {
    'docs', 'demo', 'test', 'tests', 'example', 'examples', 'template',
    'templates', 'website', 'web', 'app', 'api', 'core', 'cli', 'server',
    'client', 'sdk', 'skills', 'agent', 'agents', 'tutor', 'lms', 'moodle',
    'education', 'school', 'learn', 'learning', 'course', 'courses',
    'homepage', 'blog', 'config', 'utils', 'common', 'main', 'starter',
    'awesome', 'notes', 'research', 'data', 'dataset', 'benchmark',
}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    # repo-name -> owner -> set of files naming it; plus whether FILED.
    byname = collections.defaultdict(lambda: collections.defaultdict(set))
    written = {}
    filed = set()

    for dirpath, dirnames, filenames in os.walk('.'):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for name in filenames:
            if not name.endswith(('.md', '.tsv', '.txt', '.json')):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), '.')
            try:
                with open(rel, encoding='utf-8', errors='replace') as fh:
                    lines = fh.readlines()
            except (IsADirectoryError, PermissionError, FileNotFoundError):
                continue
            for line in lines:
                in_row = line.lstrip().startswith('|')
                for owner, repo in ADDR.findall(line):
                    if owner.lower() in NOT_A_REPO:
                        continue
                    repo = re.sub(r'\.git$', '', repo)
                    key = f'{owner.lower()}/{repo.lower()}'
                    if key in PLACEHOLDER:
                        continue
                    byname[repo.lower()][owner.lower()].add(rel)
                    written.setdefault(key, f'{owner}/{repo}')
                    if in_row and rel in CURATED:
                        filed.add(key)

    rows = []
    for repo, owners in byname.items():
        if len(owners) < 2 or repo in GENERIC:
            continue
        filed_owners = [o for o in owners if f'{o}/{repo}' in filed]
        # The dangerous shape: a curated table row names one side of a
        # collision and the other side is only in history.
        shape = ('FILED-vs-HISTORY' if len(filed_owners) == 1
                 else 'BOTH-FILED' if len(filed_owners) > 1
                 else 'NEITHER-FILED')
        rank = {'FILED-vs-HISTORY': 0, 'BOTH-FILED': 1, 'NEITHER-FILED': 2}[shape]
        rows.append((
            rank, repo, shape, len(owners),
            ';'.join(written.get(f'{o}/{repo}', f'{o}/{repo}')
                     for o in sorted(owners,
                                     key=lambda o: (f'{o}/{repo}' not in filed, o))),
            ';'.join(sorted(f'{o}(filed)' if f'{o}/{repo}' in filed else o
                            for o in owners)),
        ))

    rows.sort(key=lambda r: (r[0], -r[3], r[1]))

    out = [('repo_name', 'shape', 'owner_count', 'addresses_filed_first',
            'owners')]
    out += [(r[1], r[2], str(r[3]), r[4], r[5]) for r in rows]

    if '--tsv' in sys.argv:
        dest = sys.argv[sys.argv.index('--tsv') + 1]
        with open(dest, 'w', encoding='utf-8') as fh:
            for row in out:
                fh.write('\t'.join(row) + '\n')
        print(f'written: {dest}')

    shapes = collections.Counter(r[2] for r in rows)
    print(f'distinct repository names        : {len(byname)}')
    print(f'names held by >1 owner (non-generic): {len(rows)}'
          '   <- the Gap 538-A work order')
    for sh in ('FILED-vs-HISTORY', 'BOTH-FILED', 'NEITHER-FILED'):
        print(f'  {sh:<18} : {shapes.get(sh, 0)}')
    print()
    print('A COLLISION IS A CANDIDATE, NOT A FORK, AND THIS FILE NEVER GRADES')
    print('ONE. Feed a group to compose/code/p405-group-lineage (`make')
    print('gate-group-lineage`), which grades it from FULL git histories and')
    print('catches the squash-republish a `forked from` line cannot see. Work')
    print('the FILED-vs-HISTORY rows first -- a filed address is what a')
    print('successor pastes. p405 has already graded `canvas-mcp`: 20')
    print('addresses, 190 pairs, 11+2 families, 7 sole projects.')
    print()
    for r in rows[:25]:
        print(f'  {r[2]:<18} {r[1]:<34} {r[4]}')


if __name__ == '__main__':
    main()
