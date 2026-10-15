#!/usr/bin/env python3
"""ACTION PZ — reconcile every repository printing MORE THAN ONE distinct grant
across the four client-facing shelves.

p211's P211-1 found that 6 of 7 wrong cells named a repository whose correct
grant this KB had already published somewhere else: the dominant failure mode
is propagation, not discovery. PZ prices that backlog.

Method, and the one thing that makes it honest:

  A row that prints two licence tokens is NOT a contradiction. It is either a
  legitimate dual grant (autogen's two-FILE shape) or -- far more often on
  these shelves -- a CORRECTION TRAIL row, which prints the wrong value and the
  right value side by side on purpose. Counting those would manufacture
  findings out of this KB's own integrity work.

  So PZ considers only UNAMBIGUOUS CELLS: a row naming exactly one repository
  and exactly one distinct licence token. A repository contradicts itself when
  two or more such cells disagree on the grant FAMILY.

Adjudication is a lookup, not a judgement: the p211 census holds one first-hand
grant per repository, read from the licence blob at HEAD.
"""
import json
import os
import sys
import collections

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'p211-full-column-grant-audit'))
from extract_rows import extract  # noqa: E402

KB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SHELVES = ['agents/top.md', 'repos/foundations.md',
           'verticals/solutions.md', 'compose/patterns.md']
CENSUS = 'evidence/full-column-grant-census.2026-10-15-p211.tsv'

# Spellings of the SAME grant. Collapsing these is what keeps PZ from counting
# "GPL" against "GPL-3.0" as a contradiction.
CANON = {
    'GPL': 'GPL-3.0', 'GPL-3.0': 'GPL-3.0', 'GPL-2.0': 'GPL-2.0',
    'LGPL': 'LGPL-3.0', 'LGPL-3.0': 'LGPL-3.0', 'LGPL-2.1': 'LGPL-2.1',
    'AGPL-3.0': 'AGPL-3.0',
    'MIT': 'MIT', 'MIT-BODYONLY': 'MIT',
    'Apache-2.0': 'Apache-2.0',
    'BSD-3-Clause': 'BSD-3-Clause', 'BSD-2-Clause': 'BSD-2-Clause',
    'BSD-family': 'BSD-family',
    'MPL-2.0': 'MPL-2.0', 'ECL-2.0': 'ECL-2.0',
    'EPL-2.0': 'EPL-2.0', 'EPL': 'EPL-2.0', 'EPL-1.0': 'EPL-1.0',
    'CC0-1.0': 'CC0-1.0',
    'CC-BY-4.0': 'CC-BY-4.0', 'CC-BY': 'CC-BY-4.0', 'CC-BY-BODYONLY': 'CC-BY-4.0',
    'CC-BY-SA-4.0': 'CC-BY-SA-4.0', 'CC-BY-SA': 'CC-BY-SA-4.0',
    'CC-BY-NC-4.0': 'CC-BY-NC-4.0', 'CC-BY-NC': 'CC-BY-NC-4.0',
    'CC-BY-NC-SA-4.0': 'CC-BY-NC-SA-4.0', 'CC-BY-NC-SA': 'CC-BY-NC-SA-4.0',
    'Elastic-2.0': 'Elastic-2.0', 'BSL-1.1': 'BSL-1.1', 'ISC': 'ISC',
    'Unlicense': 'Unlicense', 'Zlib': 'Zlib', 'Artistic-2.0': 'Artistic-2.0',
    'OSL-3.0': 'OSL-3.0', 'AFL-3.0': 'AFL-3.0', 'CDDL': 'CDDL',
}
# The GNU family: P211-3's standing hazard. Flagged separately because this is
# the one axis that decides whether a hosted education deployment owes source.
GNU = {'GPL-3.0', 'GPL-2.0', 'LGPL-3.0', 'LGPL-2.1', 'AGPL-3.0'}


def canon(tok):
    return CANON.get(tok, CANON.get(tok.upper(), tok))


def load_census(path):
    out = {}
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            if line.startswith('#') or line.startswith('repo\t'):
                continue
            p = line.rstrip('\n').split('\t')
            if len(p) < 4:
                continue
            out[p[0]] = {'family': p[2], 'bytes': p[3], 'form': p[1]}
    return out


def main():
    os.chdir(KB)
    rows = extract(SHELVES)
    census = load_census(CENSUS)

    # Unambiguous cells only: one repo, one distinct licence token.
    cells = collections.defaultdict(list)
    multi_token_rows = 0
    for r in rows:
        if r['n_repos'] != 1 or not r['stated']:
            continue
        fams = {canon(t) for t in r['stated']}
        if len(fams) != 1:
            multi_token_rows += 1
            continue
        cells[r['repo']].append({'file': r['file'], 'line': r['line'],
                                 'fam': next(iter(fams)),
                                 'raw': r['stated'][0]})

    contradictions = {}
    for repo, cl in cells.items():
        fams = {c['fam'] for c in cl}
        if len(fams) > 1:
            contradictions[repo] = cl

    print('shelves              :', ', '.join(SHELVES))
    print('table rows extracted :', len(rows))
    print('unambiguous cells    :', sum(len(v) for v in cells.values()))
    print('repos w/ >=1 cell    :', len(cells))
    print('multi-token rows     :', multi_token_rows,
          '(dual grants + correction trails -- deliberately excluded)')
    print()
    print('=== ACTION PZ RESULT ===')
    print('repos printing >1 distinct grant family :', len(contradictions))
    print('FALSIFIER: limb 1 (>=10) fires' if len(contradictions) >= 10
          else 'FALSIFIER: limb 2 (<10) fires')
    print()

    rec = []
    for repo in sorted(contradictions):
        cl = contradictions[repo]
        g = census.get(repo)
        blob = g['family'] if g else 'NOT-IN-CENSUS'
        fams = sorted({c['fam'] for c in cl})
        gnu_axis = len([f for f in fams if f in GNU]) > 0 and len(set(fams)) > 1
        print('%-52s shelves=%-28s blob=%-14s %s'
              % (repo, '/'.join(fams), blob, 'GNU-AXIS' if gnu_axis else ''))
        for c in cl:
            verdict = ('agrees' if c['fam'] == blob
                       else ('STALE' if blob not in ('NOT-IN-CENSUS', 'ABSENT',
                                                     'NOBLOB', 'UNRECOGNISED')
                             else 'unadjudicable'))
            print('      %-26s:%-6s %-16s -> %s'
                  % (c['file'], c['line'], c['fam'], verdict))
            rec.append({'repo': repo, 'file': c['file'], 'line': c['line'],
                        'shelf_fam': c['fam'], 'blob_fam': blob,
                        'blob_bytes': g['bytes'] if g else '',
                        'blob_form': g['form'] if g else '',
                        'verdict': verdict, 'gnu_axis': gnu_axis})
    json.dump(rec, open(sys.argv[1], 'w'), indent=1)

    print()
    stale = [r for r in rec if r['verdict'] == 'STALE']
    print('cells to correct (STALE) :', len(stale))
    print('cells already right      :',
          len([r for r in rec if r['verdict'] == 'agrees']))
    print('unadjudicable (no blob)  :',
          len([r for r in rec if r['verdict'] == 'unadjudicable']))
    print('contradictions on the GNU axis :',
          len({r['repo'] for r in rec if r['gnu_axis']}))


if __name__ == '__main__':
    main()
