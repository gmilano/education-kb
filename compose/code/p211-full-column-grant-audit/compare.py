#!/usr/bin/env python3
"""Compare each shelf row's STATED licence against the grant read from the blob.

Per-cell (p208's lesson): a row is adjudicated against its own cell, not
against the union of every value printed for that repository anywhere.
"""
import json
import sys
import collections

rows = json.load(open(sys.argv[1]))
cls = json.load(open(sys.argv[2]))

# Families that are the same grant under different spellings.
EQUIV = {
    'GPL-3.0': {'GPL-3.0', 'GPL'},
    'GPL-2.0': {'GPL-2.0', 'GPL'},
    'LGPL-3.0': {'LGPL-3.0', 'LGPL'},
    'LGPL-2.1': {'LGPL-2.1', 'LGPL'},
    'AGPL-3.0': {'AGPL-3.0'},
    'Apache-2.0': {'Apache-2.0'},
    'MIT': {'MIT', 'MIT-BODYONLY'},
    'BSD-3-Clause': {'BSD-3-Clause', 'BSD-family'},
    'BSD-2-Clause': {'BSD-2-Clause', 'BSD-family'},
    'ECL-2.0': {'ECL-2.0'},
    'MPL-2.0': {'MPL-2.0'},
    'EPL-2.0': {'EPL-2.0', 'EPL'},
    'CC0-1.0': {'CC0-1.0'},
    'CC-BY-4.0': {'CC-BY-4.0', 'CC-BY', 'CC-BY-BODYONLY'},
    'CC-BY-SA-4.0': {'CC-BY-SA-4.0', 'CC-BY-SA'},
    'CC-BY-NC-4.0': {'CC-BY-NC-4.0', 'CC-BY-NC'},
    'CC-BY-NC-SA-4.0': {'CC-BY-NC-SA-4.0', 'CC-BY-NC-SA', 'CC-BY-NC'},
    'Elastic-2.0': {'Elastic-2.0'},
    'BSL-1.1': {'BSL-1.1'},
    'ISC': {'ISC'},
    'Unlicense': {'Unlicense'},
}

mismatch, agree, unreadable, nostate = [], 0, 0, 0
for r in rows:
    repo = r['repo']
    if repo == 'MULTI' or not r['stated']:
        nostate += 1
        continue
    g = cls.get(repo)
    if not g:
        continue
    fam = g['family']
    if fam in ('ABSENT', 'NOBLOB', 'UNRECOGNISED'):
        unreadable += 1
        continue
    # A row may legitimately print a dual grant; agreement with ANY stated
    # token on that row counts as agreement for that cell.
    hit = False
    for st in r['stated']:
        if fam in EQUIV.get(st, {st}):
            hit = True
            break
    if hit:
        agree += 1
    else:
        mismatch.append({'file': r['file'], 'line': r['line'], 'repo': repo,
                         'stated': r['stated'], 'blob': fam,
                         'bytes': g['bytes'], 'form': g.get('path_form')})

print('rows adjudicated      :', agree + len(mismatch))
print('  agree               :', agree)
print('  MISMATCH            :', len(mismatch))
print('rows unreadable grant :', unreadable)
print('rows w/o stated/MULTI :', nostate)
print()
by_repo = collections.Counter((m['repo'], tuple(m['stated']), m['blob'])
                              for m in mismatch)
print('=== distinct mismatching (repo, stated, blob) ===')
for (repo, stated, blob), n in by_repo.most_common():
    print('%4d rows  %-48s shelf=%-22s blob=%s' %
          (n, repo, '/'.join(stated), blob))
json.dump(mismatch, open(sys.argv[3], 'w'), indent=1)
