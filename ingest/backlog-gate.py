#!/usr/bin/env python3
"""p539 — the two GATES p533 said promotion needs, run over the HISTORY backlog.

p533 established that promotion priority needs three inputs and that only one of
them is a rank: "does the grant let us build (gate), is the address alive
(gate), and how much does it matter (rank)".  It had the gates for a queue of
twenty.  This pass inherited a backlog of 3 873 and no queue at all, so the
gates have to run in BULK or they do not run.

WHY THIS IS NOT ingest/probe-grant.sh.

probe-grant.sh (p517, hardened p530) is the correct instrument for ONE address
and this pass keeps it as the authority on grant filenames.  It cannot be the
instrument for 3 873, for a measured reason: it probes all ~90 generated case
variants for every repository with NO EARLY EXIT and a 20-second per-probe
timeout.  That is up to 90 sequential round trips per address, and the backlog
would take days.  So this instrument:

  * resolves the default branch the same way -- `git ls-remote --symref`, never
    assumed, which is p509's defect and p517's fix;
  * probes the SAME name list, ordered by observed frequency, and stops at the
    first hit UNLESS the hit is a split-grant name (LICENSE-MIT, LICENSE-CODIGO,
    ...), where it keeps going because the second file is the point;
  * runs the addresses concurrently, which is the only reason the bulk gate is
    affordable at all;
  * prints UNRESOLVED-on-N-names, never "unlicensed".  p517's rule holds:
    absence on a name list is not absence of a grant.

CHANNEL NOTE, measured this pass.  `api.github.com` is HTTP 403 to this
session's egress, so p502's "the GitHub REST API answers" does NOT reproduce
here -- a successor should not plan on it.  `git ls-remote` over HTTPS and
`raw.githubusercontent.com` both answer, and they are what this runs on.

Usage:
    python3 -I ingest/backlog-gate.py BACKLOG.tsv --stage live  --out OUT.tsv [--limit N]
    python3 -I ingest/backlog-gate.py LIVE.tsv    --stage grant --out OUT.tsv [--limit N]
"""
import concurrent.futures as cf
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

# Ordered by how often this base has actually found each name, commonest first,
# so the early exit pays.  Same vocabulary as probe-grant.sh.
GRANT_NAMES = [
    'LICENSE', 'LICENSE.md', 'LICENSE.txt', 'LICENCE', 'LICENCE.md',
    'COPYING', 'license', 'License.md', 'LICENSE.TXT', 'license.md',
    'LICENSE.rst', 'COPYING.txt', 'COPYING.md', 'LICENCE.txt',
    'LICENSE-MIT', 'LICENSE-APACHE', 'LICENSE-CODE', 'LICENSE-CODE.md',
    'LICENSE-DATA', 'LICENSE-DATA.md', 'LICENSE-CODIGO.md', 'LICENSE-DADOS.md',
    'NOTICE', 'NOTICE.txt',
    'LICENCA', 'LICENCA.md', 'LICENCIA', 'LICENCIA.md', 'LIZENZ', 'LIZENZ.md',
    'LICENZA', 'LICENZA.md', 'LISENSI', 'LISENSI.md',
    'LICENSE-CN', 'LICENSE.zh', 'LICENSE_zh-CN.md', '许可证', '开源协议.md',
    'LICENSE.ja', 'ライセンス', 'LICENSE.ko', '라이선스',
    'ЛИЦЕНЗИЯ', 'LICENCE-FR.md', 'الترخيص',
]
# A hit on one of these does not end the probe: the whole point of the split is
# that a second file carries a different grant (bncc-dev, p516).
SPLIT = {'LICENSE-MIT', 'LICENSE-APACHE', 'LICENSE-CODE', 'LICENSE-CODE.md',
         'LICENSE-DATA', 'LICENSE-DATA.md', 'LICENSE-CODIGO.md',
         'LICENSE-DADOS.md', 'NOTICE', 'NOTICE.txt'}

PERMISSIVE = {'MIT', 'Apache-2.0', 'BSD-3-Clause', 'BSD-2-Clause', 'ISC',
              'Unlicense', 'MIT-like', 'ECL-2.0'}


def spdx_of(body):
    """Name the grant from its own title block.  Order matters: AGPL before
    GPL, and the version lines before the generic GNU line."""
    b = body
    if 'GNU AFFERO GENERAL PUBLIC LICENSE' in b or 'AFFERO' in b:
        return 'AGPL-3.0'
    if 'GNU LESSER GENERAL PUBLIC' in b:
        return 'LGPL'
    if 'Version 2, June 1991' in b:
        return 'GPL-2.0'
    if 'Version 3, 29 June 2007' in b:
        return 'GPL-3.0'
    if 'GNU GENERAL PUBLIC LICENSE' in b or 'LICENÇA PÚBLICA GERAL' in b:
        return 'GPL-?'
    if 'Apache License' in b:
        return 'Apache-2.0'
    if 'MIT License' in b or 'Permission is hereby granted, free of charge' in b:
        return 'MIT'
    if 'Educational Community License' in b:
        return 'ECL-2.0'
    if 'Mozilla Public License' in b:
        return 'MPL-2.0'
    if 'Creative Commons Attribution-ShareAlike' in b:
        return 'CC-BY-SA-4.0'
    if 'Creative Commons' in b:
        return 'CC-BY-4.0'
    if 'Redistribution and use in source and binary forms' in b:
        return 'BSD-3-Clause' if 'Neither the name' in b else 'BSD-2-Clause'
    if 'ISC License' in b or 'ISC LICENSE' in b:
        return 'ISC'
    if 'This is free and unencumbered software' in b:
        return 'Unlicense'
    if 'THE SOFTWARE IS PROVIDED "AS IS"' in b:
        return 'MIT-like'
    return 'unknown-text'


def resolve(slug):
    """Liveness + default branch + head sha, resolved not assumed (p509/p517)."""
    try:
        r = subprocess.run(
            ['git', 'ls-remote', '--symref',
             f'https://github.com/{slug}', 'HEAD'],
            capture_output=True, text=True, timeout=60,
            env={**os.environ, 'GIT_TERMINAL_PROMPT': '0',
                 'GIT_ASKPASS': '/bin/true'})
    except subprocess.TimeoutExpired:
        return slug, 'TIMEOUT', '-', '-'
    if r.returncode != 0 or not r.stdout.strip():
        return slug, 'DEAD/PRIVATE', '-', '-'
    branch, sha = '(detached)', '-'
    for line in r.stdout.splitlines():
        if line.startswith('ref:'):
            branch = line.split()[1].replace('refs/heads/', '')
        elif line.split('\t')[-1].strip() == 'HEAD':
            sha = line.split()[0][:12]
    return slug, 'LIVE', branch, sha


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'education-kb-p539'})
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.read(4096).decode('utf-8', 'replace')
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return None


def grant(slug, branch):
    found, spdx = [], []
    for name in GRANT_NAMES:
        url = (f'https://raw.githubusercontent.com/{slug}/'
               f'{urllib.parse.quote(branch)}/{urllib.parse.quote(name)}')
        body = fetch(url)
        if body is None:
            continue
        found.append(name)
        g = spdx_of(body)
        if g not in spdx:
            spdx.append(g)
        if name not in SPLIT:
            break
    if not found:
        return f'UNRESOLVED-on-{len(GRANT_NAMES)}-names', 'UNRESOLVED'
    return ','.join(found), ','.join(spdx)


def read_tsv(path, limit):
    with open(path, encoding='utf-8') as fh:
        header = fh.readline().rstrip('\n').split('\t')
        rows = [l.rstrip('\n').split('\t') for l in fh if l.strip()]
    return header, rows[:limit] if limit else rows


def main():
    src = sys.argv[1]
    stage = sys.argv[sys.argv.index('--stage') + 1]
    out = sys.argv[sys.argv.index('--out') + 1]
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else 0
    header, rows = read_tsv(src, limit)

    if stage == 'live':
        with cf.ThreadPoolExecutor(max_workers=24) as ex:
            res = dict((r[0], r[1:]) for r in
                       ex.map(lambda r: resolve(r[0]), rows))
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write('\t'.join(header + ['live', 'default_branch', 'head_sha']) + '\n')
            for r in rows:
                v = res.get(r[0], ('ERROR', '-', '-'))
                fh.write('\t'.join(r + list(v)) + '\n')
        counts = {}
        for v in res.values():
            counts[v[0]] = counts.get(v[0], 0) + 1
        for k in sorted(counts, key=lambda k: -counts[k]):
            print(f'{k:>14} : {counts[k]}')
        print(f'written: {out}  ({len(rows)} addresses)')
        return

    # grant stage: only LIVE rows are probed; the rest are carried through.
    li = header.index('live')
    bi = header.index('default_branch')
    live = [r for r in rows if len(r) > li and r[li] == 'LIVE']
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        res = dict(zip((r[0] for r in live),
                       ex.map(lambda r: grant(r[0], r[bi]), live)))
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\t'.join(header + ['grant_files', 'spdx_guess', 'buildable']) + '\n')
        for r in rows:
            gf, sp = res.get(r[0], ('-', '-'))
            ok = 'yes' if any(x in PERMISSIVE for x in sp.split(',')) else 'no'
            fh.write('\t'.join(r + [gf, sp, ok]) + '\n')
    counts = {}
    for _gf, sp in res.values():
        counts[sp] = counts.get(sp, 0) + 1
    for k in sorted(counts, key=lambda k: -counts[k]):
        print(f'{k:>24} : {counts[k]}')
    print(f'probed {len(live)} live of {len(rows)}; written: {out}')


if __name__ == '__main__':
    main()
