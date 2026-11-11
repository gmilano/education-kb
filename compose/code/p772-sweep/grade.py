#!/usr/bin/env python3
"""p772 — ACTION p771-C + p771-D, base-wide.

p771-C: adopt the BODY-DIFF as the standing licence verdict, normalising FIRST
        (its D1 reported 113 false deltas on a clean Apache grant because the
        payload was a Markdown rendering).
p771-D: grade ownership FAMILY-AWARE — MIT in the payload head, Apache-2.0 in the
        post-"END OF TERMS AND CONDITIONS" appendix, GPL/AGPL not probed at all.

Canonical texts are SPDX's own license-list-data, held in ingest/canonical/.
"""
import re, os, sys, json, hashlib, difflib, collections

CANON_DIR = sys.argv[1]
PAYLOADS  = sys.argv[2]
CLAIMS    = sys.argv[3]

def normalise(t):
    """p771-D1/D2: strip presentation before comparing anything."""
    t = t.replace('“', '"').replace('”', '"')
    t = t.replace('‘', "'").replace('’', "'")
    t = t.replace('–', '-').replace('—', '-').replace(' ', ' ')
    t = re.sub(r'<<?(https?://[^>\s]+)>?>', r'\1', t)   # markdown autolinks
    t = re.sub(r'^[=\-]{3,}$', ' ', t, flags=re.M)      # setext heading rules
    t = re.sub(r'[*_#>`]', ' ', t)                      # emphasis / headings
    t = t.lower()
    toks = [w.strip('.,:;!?()[]"\'') for w in t.split()]
    return [w for w in toks if w]

def operative(toks, family):
    """Apache's operative text ends at END OF TERMS AND CONDITIONS; the appendix
    after it is instructions, and p771 found a real alteration hiding there."""
    if family.startswith('Apache'):
        for i in range(len(toks) - 4):
            if toks[i:i+5] == ['end', 'of', 'terms', 'and', 'conditions']:
                return toks[:i]
    # for permissive short forms the copyright line is the variable part
    out, skip = [], False
    for w in toks:
        if w == 'copyright':
            skip = True
        elif skip and (w in ('permission', 'redistribution', 'licensed')):
            skip = False
        if not skip:
            out.append(w)
    return out

canon = {}
for fn in os.listdir(CANON_DIR):
    if not fn.endswith('.txt'): continue
    fam = fn[:-4]
    toks = normalise(open(os.path.join(CANON_DIR, fn), encoding='utf-8', errors='replace').read())
    canon[fam] = operative(toks, fam)

OWNER = re.compile(r'copyright\s*(?:\(c\)|©)?\s*((?:19|20)\d\d(?:\s*[-–,]\s*(?:19|20)?\d\d)?)?\s*,?\s*([^\n]{0,90})', re.I)
NOPROBE = ('GPL-3.0-only', 'AGPL-3.0-only', 'LGPL-3.0-only')

def ownership(raw, family):
    if family in NOPROBE:
        return 'UNOBTAINABLE-FROM-GRANT', None      # p771-D: do not probe
    if family.startswith('Apache'):
        i = raw.lower().find('end of terms and conditions')
        region = raw[i:] if i >= 0 else ''
    else:
        region = raw[:600]
    for m in OWNER.finditer(region):
        name = m.group(2).strip(' .,:;-')
        # reject Apache §1 boilerplate and the appendix placeholder (p771-D)
        if not name or re.search(r'owner|\[|\{|yyyy|<year>|name of|the copyright holders?$', name, re.I):
            continue
        if len(name) < 3:
            continue
        return 'ESTABLISHED', (m.group(1) or '').strip() + ' ' + name
    return 'ABSENT-FROM-GRANT', None

claims = json.load(open(CLAIMS))
res = []
for c in claims:
    safe = c['slug'].replace('/', '_')
    bp = os.path.join(PAYLOADS, safe + '.body')
    if not os.path.exists(bp):
        res.append(dict(c, verdict='NO-GRANT-PAYLOAD')); continue
    raw = open(bp, encoding='utf-8', errors='replace').read()
    nb = len(raw.encode('utf-8', 'replace'))
    sha = hashlib.sha256(raw.encode('utf-8', 'replace')).hexdigest()[:12]
    toks = normalise(raw)
    best, bestr = None, 9e9
    for fam, ctoks in canon.items():
        ops = operative(toks, fam)
        if not ops: continue
        sm = difflib.SequenceMatcher(None, ops, ctoks, autojunk=False)
        deltas = sum(max(i2-i1, j2-j1) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal')
        ratio = deltas / max(len(ctoks), 1)
        if ratio < bestr:
            best, bestr, bestd = fam, ratio, deltas
    own, owner = ownership(raw, c['family'])
    claimed_ops = operative(toks, c['family'])
    ctoks = canon.get(c['family'])
    if ctoks:
        sm = difflib.SequenceMatcher(None, claimed_ops, ctoks, autojunk=False)
        cd = sum(max(i2-i1, j2-j1) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal')
    else:
        cd = None
    if cd == 0:
        verdict = 'body:canonical'
    elif best != c['family'] and re.sub(r'-(only|or-later)$','',best) == re.sub(r'-(only|or-later)$','',c['family']):
        verdict = 'body:canonical'
    elif best != c['family'] and {re.sub(r'-(only|or-later)$','',best), re.sub(r'-(only|or-later)$','',c['family'])} <= {'GPL-3.0', 'LGPL-3.0', 'AGPL-3.0', 'LGPL-2.1', 'GPL-2.0'}:
        # D11: the GNU family ships one text inside another; body-diff cannot separate them.
        verdict = 'body:GNU-FAMILY-AMBIGUOUS'
    elif best != c['family'] and bestr < 0.08:
        verdict = f'grant:MISDECLARED(is {best})'
    elif cd is not None and cd / max(len(ctoks), 1) < 0.02:
        verdict = f'body:near-canonical({cd})'
    else:
        verdict = f'body:ALTERED({cd})'
    res.append(dict(c, bytes=nb, sha=sha, verdict=verdict,
                    ownership=own, owner=owner, best=best,
                    bestratio=round(bestr, 4)))
json.dump(res, open('verdicts.json', 'w'), indent=1)
v = collections.Counter(re.sub(r'\(.*\)', '', r['verdict']) for r in res)
print('=== BODY-DIFF VERDICTS over', len(res), 'published licence claims ===')
for k, n in v.most_common():
    print(f'   {k:28s} {n}')
print()
print('=== OWNERSHIP, family-aware (ACTION p771-D) ===')
o = collections.Counter((r['family'], r.get('ownership')) for r in res if r.get('ownership'))
fams = collections.defaultdict(lambda: collections.Counter())
for (f, s), n in o.items(): fams[f][s] = n
for f in sorted(fams):
    tot = sum(fams[f].values())
    est = fams[f].get('ESTABLISHED', 0)
    print(f'   {f:16s} established {est:4d}/{tot:4d}  ' +
          ' · '.join(f'{k}={v}' for k, v in fams[f].items() if k != 'ESTABLISHED'))
print()
print('=== MISDECLARED (the claim and the payload are different licences) ===')
mis = [r for r in res if r['verdict'].startswith('grant:MISDECLARED')]
for r in mis[:30]:
    print(f"   🔴 {r['slug']:48s} shelf says {r['family']:14s} payload is {r['best']:14s} ({r['file']}:{r['line']})")
print(f'   total MISDECLARED: {len(mis)}')
