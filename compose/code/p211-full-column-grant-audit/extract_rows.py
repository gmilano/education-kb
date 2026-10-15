#!/usr/bin/env python3
"""Extract (repo, stated_licence) pairs from the KB's core shelf tables.

A row qualifies when it is a markdown table row containing exactly one
github.com/owner/repo reference and at least one cell that looks like an
SPDX-ish licence token. Rows naming several repos are recorded with
repo='MULTI' so they can be counted but not falsely adjudicated.
"""
import re
import sys
import os
import json

REPO_RE = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?=[)\s\]#,]|$)')
NON_REPO_OWNERS = {
    'topics', 'topic', 'trending', 'features', 'about', 'sponsors',
    'collections', 'orgs', 'settings', 'login', 'search', 'marketplace',
    'apps', 'site', 'readme',
}

# Licence tokens we expect to see in a stated cell.
LIC_TOKENS = [
    'AGPL-3.0', 'LGPL-3.0', 'LGPL-2.1', 'GPL-3.0', 'GPL-2.0', 'Apache-2.0',
    'MIT', 'BSD-3-Clause', 'BSD-2-Clause', 'MPL-2.0', 'ECL-2.0', 'EPL-2.0',
    'EPL-1.0', 'CDDL', 'Unlicense', 'CC0-1.0', 'CC-BY-4.0', 'CC-BY-SA-4.0',
    'CC-BY-NC-SA-4.0', 'CC-BY-NC-4.0', 'Elastic-2.0', 'BSL-1.1', 'ISC',
    'Zlib', 'Artistic-2.0', 'OSL-3.0', 'AFL-3.0',
]
LIC_RE = re.compile(
    r'(?<![A-Za-z0-9-])(' + '|'.join(re.escape(t) for t in LIC_TOKENS) + r')(?![A-Za-z0-9])',
    re.IGNORECASE,
)


def norm_lic(tok):
    for t in LIC_TOKENS:
        if t.lower() == tok.lower():
            return t
    return tok


def extract(paths):
    rows = []
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8', errors='replace') as fh:
            for lineno, line in enumerate(fh, 1):
                if not line.lstrip().startswith('|'):
                    continue
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) < 2:
                    continue
                # Skip separator rows
                if all(set(c) <= set('-: ') for c in cells):
                    continue
                repos = []
                for m in REPO_RE.finditer(line):
                    owner, name = m.group(1), m.group(2)
                    if owner.lower() in NON_REPO_OWNERS:
                        continue
                    name = name.rstrip('.')
                    repos.append(f'{owner}/{name}')
                repos = sorted(set(repos))
                if not repos:
                    continue
                lics = [norm_lic(m.group(1)) for m in LIC_RE.finditer(line)]
                lics = sorted(set(lics))
                rows.append({
                    'file': os.path.basename(path),
                    'line': lineno,
                    'repo': repos[0] if len(repos) == 1 else 'MULTI',
                    'n_repos': len(repos),
                    'repos': repos,
                    'stated': lics,
                })
    return rows


if __name__ == '__main__':
    rows = extract(sys.argv[1:])
    json.dump(rows, sys.stdout, indent=1)
