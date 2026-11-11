#!/usr/bin/env python3
"""p772 - split body:ALTERED into the three things it actually contains."""
import json, re, os, difflib, collections
CAN='/home/user/education-kb/ingest/canonical'
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


canon={}
for fn in os.listdir(CAN):
    if fn.endswith('.txt'):
        fam=fn[:-4]
        canon[fam]=operative(normalise(open(os.path.join(CAN,fn),encoding='utf-8',errors='replace').read()),fam)

res=json.load(open('verdicts.json'))
out=collections.Counter(); detail=[]
for r in res:
    if not r['verdict'].startswith('body:ALTERED'): continue
    raw=open('payloads/'+r['slug'].replace('/','_')+'.body',encoding='utf-8',errors='replace').read()
    fam=r['family']; ctoks=canon.get(fam)
    if not ctoks: continue
    ops=operative(normalise(raw),fam)
    sm=difflib.SequenceMatcher(None,ops,ctoks,autojunk=False)
    m=sm.find_longest_match(0,len(ops),0,len(ctoks))
    covered=m.size/len(ctoks)
    delta=int(re.search(r'\((\d+)\)',r['verdict']).group(1))
    canon_bytes=len(open(os.path.join(CAN,fam+'.txt'),encoding='utf-8').read())
    if covered>=0.985 and len(ops)>len(ctoks)*1.02: k='canonical+APPENDED'
    elif covered>=0.985: k='canonical+template-slot'
    elif delta<=4 and fam.startswith('BSD'): k='canonical+template-slot'
    elif len(raw)<0.25*canon_bytes: k='POINTER-OR-SHORT-NOTICE'
    else: k='OPERATIVE-TEXT-ALTERED'
    out[k]+=1
    detail.append((k,r['slug'],fam,delta,r['bytes'],round(covered,3)))
print('=== the',len(detail),'"ALTERED" rows, split ===')
for k,n in out.most_common(): print(f'   {k:28s} {n}')
print()
print('=== OPERATIVE-TEXT-ALTERED - the only class that is a real licence finding ===')
for k,s,f,d,b,c in sorted([x for x in detail if x[0]=='OPERATIVE-TEXT-ALTERED'],key=lambda x:-x[3])[:20]:
    print(f'   {s[:46].ljust(46)} {f:14s} delta={d:5d}  {b:7d} B  canonical-run={c}')
print()
print('=== POINTER-OR-SHORT-NOTICE (grant cell backed by a stub) ===')
for k,s,f,d,b,c in [x for x in detail if x[0]=='POINTER-OR-SHORT-NOTICE'][:12]:
    print(f'   {s[:46].ljust(46)} {f:14s} {b:7d} B')
json.dump(detail,open('altered_split.json','w'),indent=1)
