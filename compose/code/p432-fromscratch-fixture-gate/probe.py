#!/usr/bin/env python3
"""Pass-16 payload probe. Authored here because executing the repo's own
lib/probe_payload.sh was denied in this environment (external code).
Architecture copied deliberately from lib/license_family.sh's documented design:
  - classify on the TITLE BLOCK (first 40 lines), never the body  -> closes P171
    (GPL-3.0 section 13 is TITLED "Use with the GNU Affero GPL")
  - Creative Commons is gated FIRST; NonCommercial is read as an ATTRIBUTE of a CC
    family, never as a family of its own -> closes the GPL-3.0 section-6
    "noncommercially" defect that pass 15 re-imported
  - licence tokens matched on WORD boundaries -> closes P299 ("mit" in permit/submit)
Verification pair is pass 15 Finding 7's: raw.githubusercontent for the payload,
git ls-remote for existence/default branch.  curl -sI on github.com is NOT used.
"""
import re, subprocess, sys, urllib.request

NAMES = ["LICENSE", "LICENSE.txt", "LICENSE.md", "LICENCE", "LICENCE.txt", "LICENCE.md",
         "license", "license.txt", "license.md", "licence", "COPYING", "COPYING.txt",
         "LICENSE-MIT", "LICENSE-APACHE", "MIT-LICENSE", "MIT-LICENSE.txt",
         "LICENSE.rst", "COPYRIGHT", "NOTICE"]

def _decl(text, token):
    return re.search(r'(^|[^a-z0-9])(' + token + r')([^a-z0-9]|$)', text) is not None

def family_of(payload):
    lines = [l.strip() for l in payload.splitlines() if l.strip()]
    # NAME LINE: the licence announces itself in its first few lines.  Anything further
    # down is preamble, and a preamble MENTIONS other licences (P171).
    name  = " ".join(lines[:3]).lower()
    title = "\n".join(payload.splitlines()[:40]).lower()
    body  = payload.lower()
    # --- CC0 is its OWN branch and must come FIRST: the string "CC0 1.0 Universal"
    # contains none of "creative commons"/"cc by", so nesting it inside the CC-BY gate
    # makes it unreachable.  This is lib/license_family.sh:120, and pass 16 re-broke it.
    if re.search(r'cc0|public domain dedication', name):
        return 'CC0-1.0'
    # --- Creative Commons gate (NonCommercial is an attribute, not a family)
    if re.search(r'creative commons|creativecommons\.org|cc by|cc-by', name):
        nc = 'noncommercial' in title
        sa = 'sharealike' in title or 'share alike' in title
        nd = 'noderiv' in title
        ver = '4.0' if '4.0' in title else ('3.0' if '3.0' in title else '')
        if 'cc0' in title or 'public domain dedication' in title:
            return 'CC0-1.0'
        fam = 'CC-BY' + ('-NC' if nc else '') + ('-SA' if sa else '') + ('-ND' if nd else '')
        return fam + ('-' + ver if ver else '')
    # --- copyleft families, decided on the title block
    if _decl(name, 'affero') or _decl(name, 'agpl'):
        return 'AGPL-3.0'
    if 'lesser general public license' in name or 'library general public license' in name or _decl(name, 'lgpl'):
        return 'LGPL-2.1' if '2.1' in title else 'LGPL-3.0'
    if 'general public license' in name or _decl(name, 'gpl'):
        if 'version 3' in title or _decl(title, 'gpl-3') or _decl(title, 'gplv3'):
            return 'GPL-3.0'
        if 'version 2' in title or _decl(title, 'gpl-2') or _decl(title, 'gplv2'):
            return 'GPL-2.0'
        return 'GPL'
    if 'mozilla public license' in name or _decl(name, 'mpl'):
        return 'MPL-2.0'
    if 'eclipse public license' in name:
        return 'EPL-2.0'
    if 'educational community license' in name:
        return 'ECL-2.0'
    if 'apache license' in name:
        return 'Apache-2.0' if 'version 2' in title else 'Apache'
    if 'unlicense' in name or 'this is free and unencumbered' in body[:600]:
        return 'Unlicense'
    if 'isc license' in name or (_decl(name, 'isc') and 'permission to use' in body):
        return 'ISC'
    if _decl(name, 'bsd') or 'redistribution and use in source and binary' in body:
        if '3-clause' in title or 'neither the name' in body: return 'BSD-3-Clause'
        if '2-clause' in title: return 'BSD-2-Clause'
        return 'BSD'
    # MIT: the grant line IS its identity (documented fallback to body)
    if _decl(name, 'mit') or 'permission is hereby granted, free of charge' in body:
        return 'MIT'
    if 'microsoft public license' in name or _decl(name, 'ms-pl'):
        return 'MS-PL'
    return 'UNCLASSIFIED'

FLOOR = {'MPL-2.0': 10000, 'GPL-3.0': 25000, 'GPL-2.0': 15000, 'AGPL-3.0': 25000,
         'LGPL-3.0': 5000, 'LGPL-2.1': 20000, 'Apache-2.0': 9000, 'CC0-1.0': 4000}

def size_check(fam, nbytes):
    """A long-text family in a short file is a POINTER or a MISREAD, never the grant."""
    f = FLOOR.get(fam)
    return '' if (f is None or nbytes >= f) else f'SHORT({nbytes}B<{f})'

def holder_of(payload):
    m = re.search(r'copyright\s*(?:\(c\)|©)?\s*,?\s*((?:19|20)\d{2}[^\n]{0,90})', payload, re.I)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''

def ls_remote(repo):
    try:
        out = subprocess.run(["git", "ls-remote", "--symref",
                              f"https://github.com/{repo}", "HEAD"],
                             capture_output=True, text=True, timeout=60).stdout
        m = re.search(r'ref:\s+refs/heads/(\S+)\s+HEAD', out)
        return m.group(1) if m else ('DEAD' if not out.strip() else 'NO-SYMREF')
    except Exception:
        return 'ERROR'

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'kb-probe'})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode('utf-8', 'replace')
    except Exception:
        return None

def probe(repo, branch=None):
    br = branch or ls_remote(repo)
    if br in ('DEAD', 'ERROR'):
        return (repo, br, 'NO-REMOTE', 0, 'NO-PAYLOAD', '')
    for n in NAMES:
        p = fetch(f"https://raw.githubusercontent.com/{repo}/{br}/{n}")
        if p and p.strip():
            fam = family_of(p)
            if fam == 'UNCLASSIFIED':
                # R/CRAN convention: LICENSE is a YEAR/HOLDER template fill-in and the
                # real grant is DESCRIPTION's `License:` field.  Measured on educabR.
                d = fetch(f"https://raw.githubusercontent.com/{repo}/{br}/DESCRIPTION")
                if d:
                    m = re.search(r'^License:\s*(.+)$', d, re.M)
                    if m:
                        return (repo, br, n + '+DESCRIPTION', len(p.encode()),
                                m.group(1).strip() + ' (via DESCRIPTION)', holder_of(p))
            nb = len(p.encode())
            flag = size_check(fam, nb)
            return (repo, br, n, nb, fam + ('  ⚠' + flag if flag else ''), holder_of(p))
    return (repo, br, 'NO-PAYLOAD', 0, 'NO-PAYLOAD', '')

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        r = probe(parts[0], parts[1] if len(parts) > 1 else None)
        print("\t".join(str(x) for x in r), flush=True)
