#!/usr/bin/env python3
"""p781 grant-read: resolve ref via git ls-remote --symref, then probe L56 and
grade the GRANT ON THE BYTES.

p780's lesson, obeyed: bytes are measured on the file ON DISK, never through
command substitution (which strips trailing newlines and under-counts by >=1).
T811 obeyed: a filename hit is a CANDIDATE. The title line is classified, and a
copyright-holder manifest or a grant NOTICE is reported as such, not as a grade.
An absence verdict always carries the count of names tried.
"""
import subprocess, hashlib, sys, os, re

STEMS = ['LICENSE','LICENCE','COPYING','COPYRIGHT','NOTICE','LICENSE-CODE','LICENSE-MIT']
EXTS  = ['', '.md', '.txt', '.rst']
def l56():
    names = []
    for s in STEMS:
        for e in EXTS:
            for n in (s+e, (s+e).lower()):
                if n not in names: names.append(n)
    return names
L56 = l56()
assert len(L56) == 56, f'L56 is {len(L56)}, must be 56'

def ref(slug):
    p = subprocess.run(['git','ls-remote','--symref',f'https://github.com/{slug}','HEAD'],
                       capture_output=True, text=True, timeout=60)
    if p.returncode != 0: return None, None
    br, head = None, None
    for ln in p.stdout.splitlines():
        if ln.startswith('ref:'):
            br = ln.split()[1].replace('refs/heads/','')
        elif '\tHEAD' in ln:
            head = ln.split('\t')[0][:12]
    return br, head

def fetch(slug, br, name, outdir):
    dst = os.path.join(outdir, name.replace('/','_'))
    p = subprocess.run(['curl','-sS','-o',dst,'-w','%{http_code}',
                        f'https://raw.githubusercontent.com/{slug}/{br}/{name}'],
                       capture_output=True, text=True, timeout=60)
    if p.stdout.strip() != '200': 
        if os.path.exists(dst): os.remove(dst)
        return None
    return dst

def classify(path):
    """T811: body vs holder-manifest vs notice vs composite."""
    b = open(path,'rb').read()
    n = len(b)
    sha = hashlib.sha256(b).hexdigest()[:12]
    txt = b.decode('utf-8', errors='replace')
    head = txt[:400]
    low  = txt.lower()
    # scope: -only vs -or-later
    later = bool(re.search(r'either version \d+.{0,40}or \(at your option\) any later version', low, re.S)) \
            or 'or (at your option) any later version' in low
    only  = ('version 3 of the license' in low or 'version 2 of the license' in low) and not later
    fam = 'UNKNOWN'
    if 'mit license' in low or ('permission is hereby granted, free of charge' in low): fam='MIT'
    elif 'apache license' in low and 'version 2.0' in low: fam='Apache-2.0'
    elif 'gnu affero general public license' in low: fam='AGPL-3.0'
    elif 'gnu lesser general public license' in low: fam='LGPL'
    elif 'gnu general public license' in low: fam='GPL'
    elif 'mozilla public license' in low: fam='MPL-2.0'
    elif 'bsd' in low and 'redistribution and use' in low: fam='BSD'
    elif 'educational community license' in low: fam='ECL-2.0'
    elif 'cecill' in low: fam='CECILL'
    elif 'attribution 4.0 international' in low: fam='CC-BY-4.0'
    # class
    deontic = sum(low.count(w) for w in ('permission is hereby','you may not','shall be','is granted','subject to the terms'))
    kls = 'BODY'
    if n < 1500 and fam=='UNKNOWN' and ('copyright' in low) and deontic==0: kls='HOLDER-MANIFEST'
    elif n < 1200 and ('see ' in low or 'licensed under' in low) and deontic<=1 and fam!='MIT': kls='NOTICE'
    return dict(bytes=n, sha=sha, fam=fam, kls=kls, only=only, later=later, head=head.replace('\n',' ')[:90])

def run(slug, outdir):
    os.makedirs(outdir, exist_ok=True)
    br, head = ref(slug)
    if not br:
        return dict(slug=slug, err='LS-REMOTE-FAILED (deleted/private)')
    hits = []
    for name in L56:
        d = fetch(slug, br, name, outdir)
        if d: hits.append((name, classify(d)))
    if not hits:
        return dict(slug=slug, branch=br, head=head, err=f'NO-GRANT-AT-ROOT-after-{len(L56)}-names')
    return dict(slug=slug, branch=br, head=head, hits=hits)

if __name__ == '__main__':
    for slug in sys.argv[1:]:
        r = run(slug, f'/tmp/p781/grants/{slug.replace("/","_")}')
        if 'err' in r:
            print(f'{slug}\t{r.get("branch","-")} · {r.get("head","-")}\t{r["err"]}')
        else:
            for name, c in r['hits']:
                scope = '-only' if c['only'] else ('-or-later' if c['later'] else '')
                print(f'{slug}\t{r["branch"]} · {r["head"]}\t{name}\t{c["bytes"]} B\t{c["sha"]}\t{c["fam"]}{scope}\t{c["kls"]}')
