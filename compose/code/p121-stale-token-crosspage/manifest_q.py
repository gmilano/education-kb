#!/usr/bin/env python3
"""P121 ACTION Q. Does a repository's own package manifest agree with the
licence file it commits?

Clause: "read the licence of every address whose package.json, composer.json or
pyproject.toml declares one, and count the contradictions. REFUTED if fewer than
15 % of manifest-declared licences differ from the committed licence file."

p120 measured this on 4 addresses and said so: 2 of 4 contradicted, both
permissive-over-restrictive. 4 is not a denominator. This reads all 249 census
addresses on their measured default branch.

Why it matters commercially: a dependency scanner reads the MANIFEST. If the
manifest says MIT and the committed file says AGPL-3.0, every automated licence
gate in a client's pipeline returns the permissive answer and the copyleft
obligation ships undetected.
"""
import json, os, re, csv, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MAN  = os.path.join(HERE, 'manifests')
P118 = os.path.join(HERE, '..', 'p118-licence-column-sweep')

def norm(t):
    if not t: return ''
    t = str(t).strip().upper().replace('_','-')
    t = re.sub(r'\s+', ' ', t)
    aliases = {
      'APACHE 2.0':'APACHE-2.0','APACHE-2':'APACHE-2.0','APACHE LICENSE 2.0':'APACHE-2.0',
      'APACHE-2.0-ONLY':'APACHE-2.0','THE MIT LICENSE':'MIT','MIT LICENSE':'MIT',
      'GPL-3.0+':'GPL-3.0','GPL-3.0-ONLY':'GPL-3.0','GPL-3.0-OR-LATER':'GPL-3.0','GPLV3':'GPL-3.0',
      'GPL-2.0+':'GPL-2.0','GPL-2.0-ONLY':'GPL-2.0','GPL-2.0-OR-LATER':'GPL-2.0','GPLV2':'GPL-2.0',
      'AGPL-3.0-ONLY':'AGPL-3.0','AGPL-3.0-OR-LATER':'AGPL-3.0','AGPLV3':'AGPL-3.0','AGPL-3.0+':'AGPL-3.0',
      'LGPL-3.0-ONLY':'LGPL-3.0','LGPL-3.0-OR-LATER':'LGPL-3.0','LGPLV3':'LGPL-3.0',
      'BSD-3-CLAUSE':'BSD-3','BSD-2-CLAUSE':'BSD-2','CC0-1.0':'CC0','ECL-2.0':'ECL-2.0',
      'MPL-2.0':'MPL-2.0','BSD':'BSD','ISC':'ISC',
    }
    t = aliases.get(t, t)
    # P121 own-instrument fix, found by reading all 20 flagged rows before
    # believing them. Three classes were NOT contradictions:
    #  (a) spelling   -- "GPL v3", "AGPL 3", "GPL-3.0-or-later"
    #  (b) vendor form -- "Elastic-2.0" vs "ElasticLicense-2.0-NOT-OSS"
    #  (c) COARSE TRUTH -- p118 recorded some committed licences as the bare
    #      family ("BSD", "CC-BY"); a manifest refining that to "BSD-3-Clause"
    #      is MORE precise, not contradictory. Handled in cmp() below.
    t = re.sub(r'^MANIFEST:', '', t)      # must precede the family rules
    t = re.sub(r'^(A?GPL|LGPL)\s*V?\s*([0-9])(\.0)?(-OR-LATER|-ONLY|\+)?$', r'\1-\2.0', t)
    t = re.sub(r'^ELASTIC(?:LICENSE)?-?2(\.0)?.*$', 'ELASTIC-2.0', t)
    return t

FAMS = ('AGPL-3.0','LGPL-3.0','GPL-3.0','GPL-2.0','APACHE-2.0','MIT','0BSD','BSD-3','BSD-2',
        'ECL-2.0','MPL-2.0','EPL-2.0','CC0','CC-BY-SA','CC-BY-NC','CC-BY','ISC','UNLICENSE','BSD')
def fam(t):
    t = norm(t)
    for f in FAMS:
        if f in t: return f
    return t

def from_package(txt):
    try: d = json.loads(txt)
    except Exception: return None
    L = d.get('license') or d.get('licence')
    if isinstance(L, dict): L = L.get('type')
    if not L and isinstance(d.get('licenses'), list) and d['licenses']:
        e = d['licenses'][0]; L = e.get('type') if isinstance(e, dict) else e
    return L if isinstance(L, str) else None

def from_pyproject(txt):
    # license = "MIT" | license = {text = "MIT"} | license-expression = "MIT"
    m = re.search(r'^\s*license(?:-expression)?\s*=\s*["\']([^"\']+)["\']', txt, re.M)
    if m: return m.group(1)
    m = re.search(r'^\s*license\s*=\s*\{[^}]*text\s*=\s*["\']([^"\']+)["\']', txt, re.M|re.S)
    if m: return m.group(1)
    m = re.search(r'License :: OSI Approved :: ([^"\']+?)(?:"|\')', txt)
    if m:
        s = m.group(1)
        for k, v in (('MIT','MIT'),('Apache Software','APACHE-2.0'),('GNU Affero','AGPL-3.0'),
                     ('GNU Lesser','LGPL-3.0'),('GNU General Public License v3','GPL-3.0'),
                     ('GNU General Public License v2','GPL-2.0'),('BSD','BSD')):
            if k in s: return v
    return None

rows, declared = [], 0
for fn in sorted(os.listdir(MAN)):
    slug = fn.rsplit('__', 1)[0].replace('__', '/')
    kind = fn.rsplit('__', 1)[1]
    txt = open(os.path.join(MAN, fn), encoding='utf-8', errors='replace').read()
    L = from_package(txt) if kind.endswith('.json') else from_pyproject(txt)
    if not L or not str(L).strip(): continue
    declared += 1
    rows.append((slug, kind, str(L).strip()))

# measured committed licence, p118 sweep + p120 refinements
truth = {}
for r in csv.reader(open(os.path.join(P118,'measured2.2026-10-11.tsv')), delimiter='\t'):
    if len(r) >= 4: truth[r[0].lower()] = r[3]
for r in csv.reader(open(os.path.join(P118,'ledger.2026-10-11.tsv')), delimiter='\t')  :
    if len(r) >= 3 and r[0] != 'slug': truth[r[0].lower()] = r[2]
p120 = os.path.join(HERE,'..','p120-unread-grant-resolution','verdict.2026-10-11.tsv')
for r in csv.reader(open(p120), delimiter='\t'):
    if len(r) >= 3: truth[r[0].lower()] = r[2]

PERM = ('MIT','APACHE-2.0','BSD-3','BSD-2','0BSD','ISC','UNLICENSE','CC0','BSD')
out, counts = [], Counter()
for slug, kind, L in rows:
    T = truth.get(slug.lower())
    if not T:
        counts['no-measured-licence'] += 1
        out.append(('NO-TRUTH', slug, kind, L, '-', '')); continue
    d, t = fam(L), fam(T)
    # coarse truth: p118 recorded a bare family; a manifest naming a member of
    # that family refines it rather than contradicting it.
    COARSE = {'BSD': ('BSD-2','BSD-3','0BSD','BSD'), 'CC-BY': ('CC-BY','CC-BY-SA','CC-BY-NC')}
    if t in COARSE and d in COARSE[t]:
        counts['AGREE-COARSE'] += 1
        out.append(('AGREE-COARSE', slug, kind, L, T, 'truth recorded as bare family')); continue
    if d == t:
        counts['AGREE'] += 1; out.append(('AGREE', slug, kind, L, T, '')); continue
    # direction matters: permissive manifest over a restrictive file is the dangerous one
    direction = 'PERMISSIVE-OVER-RESTRICTIVE' if (d in PERM and t not in PERM) else \
                'RESTRICTIVE-OVER-PERMISSIVE' if (t in PERM and d not in PERM) else 'OTHER'
    counts['CONTRADICT'] += 1; counts[direction] += 1
    out.append(('CONTRADICT', slug, kind, L, T, direction))

w = csv.writer(open(os.path.join(HERE,'action-q.tsv'),'w'), delimiter='\t', lineterminator='\n')
for r in out: w.writerow(r)

comparable = counts['AGREE'] + counts['AGREE-COARSE'] + counts['CONTRADICT']
print(f"AGREE-COARSE (truth bare family)    : {counts['AGREE-COARSE']}")
print(f"manifests fetched (HTTP 200)        : {len(os.listdir(MAN))}")
print(f"manifests DECLARING a licence       : {declared}")
print(f"  of those, measured file available : {comparable}")
print(f"  no measured licence to compare    : {counts['no-measured-licence']}")
print()
print(f"AGREE                               : {counts['AGREE']}")
print(f"CONTRADICT                          : {counts['CONTRADICT']}")
if comparable:
    print(f"contradiction rate                  : {100*counts['CONTRADICT']/comparable:.1f} %  (clause threshold 15 %)")
print(f"  PERMISSIVE-OVER-RESTRICTIVE       : {counts['PERMISSIVE-OVER-RESTRICTIVE']}   <- the dangerous direction")
print(f"  RESTRICTIVE-OVER-PERMISSIVE       : {counts['RESTRICTIVE-OVER-PERMISSIVE']}")
print(f"  OTHER                             : {counts['OTHER']}")
