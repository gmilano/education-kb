#!/usr/bin/env python3
"""p129 ACTION AS binder: bind every published 'N tags' figure to an ADDRESS (p126 rules:
cell wall, then short-name-in-backticks, then single-address row)."""
import re, sys, os, collections

LIVE = ["README.md","agents/top.md","agents/trending.md","repos/foundations.md",
        "repos/trending.md","verticals/solutions.md","intel/market.md","intel/trends.md",
        "intel/open-gaps.md","compose/patterns.md"]
# p250 / `ACTION XJ`: the SECOND site of the same defect, and the first pass to name
# it.  Identical shape to `p228-shelf-gate/harvest_cells.py:17` — a lazy `+?` whose
# terminator lookahead holds `.` while the quantified class holds `.` too, so every
# dotted repository name bound here was truncated at its first dot.  `p230`'s lint
# has been reporting this line alongside the other one, non-blockingly, all along.
ADDR = re.compile(r'github\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]*[A-Za-z0-9_-])(?=[)\s`,.\]]|$)')
# figures: digits possibly with thin/nbsp/regular space separators, followed by optional markup then 'tags'
FIG  = re.compile(r'(\d[\d    ]*?)\s*(?:\*\*)?\s*(?:real\s+)?tags\b')
SHORT = re.compile(r'`([A-Za-z0-9._/-]+)`')
# the correction apparatus is a SCOPE: a figure inside it records a retracted claim (p129)
APPARATUS = re.compile(r'\u26a0\ufe0f \*\*was [^*]*\*\*<!--corrected-->')

root = sys.argv[1]
measured = {}
for ln in open(os.path.join(sys.argv[2])):
    p = ln.rstrip("\n").split("\t")
    if len(p) >= 4: measured[p[0].lower()] = p
# repo-name -> full address (for short-name binding); ambiguous names dropped
byname = collections.defaultdict(set)
for a in measured: byname[a.split("/")[1]].add(a)

def norm(s):
    return int(re.sub(r'[^\d]','', s))

rows=[]
unbound=[]
for page in LIVE:
    path=os.path.join(root,page)
    for i, line in enumerate(open(path), 1):
        prot=[(m.start(), m.end()) for m in APPARATUS.finditer(line)]
        figs=[(m.start(), norm(m.group(1))) for m in FIG.finditer(line)
              if not any(a <= m.start() < b for a,b in prot)]
        if not figs: continue
        cells=[]
        if '|' in line:
            pos=0
            for part in line.split('|'):
                cells.append((pos, pos+len(part), part)); pos += len(part)+1
        else:
            cells=[(0,len(line),line)]
        row_addrs=[(m.start(), m.group(1)) for m in ADDR.finditer(line)]
        for fpos, val in figs:
            cell=next((c for c in cells if c[0]<=fpos<=c[1]), cells[-1])
            cand=[a for a in row_addrs if cell[0]<=a[0]<=cell[1]]
            addr=None
            if cand:
                before=[a for a in cand if a[0]<fpos]
                addr=(before[-1] if before else cand[0])[1]
            else:
                shorts=[s for s in SHORT.findall(cell[2])]
                hit=[byname[s][0] if False else next(iter(byname[s])) for s in shorts
                     if s in byname and len(byname[s])==1]
                if len(set(hit))==1:
                    addr=hit[0]
                elif len({a[1] for a in row_addrs})==1 and row_addrs:
                    addr=row_addrs[0][1]
            if addr is None:
                unbound.append((page,i,val,line.strip()[:120])); continue
            rows.append((page,i,addr,val))

print("BOUND\t%d\tUNBOUND\t%d" % (len(rows), len(unbound)))
agree=0; disagree=[]; nomeas=[]
for page,i,addr,val in rows:
    m=measured.get(addr.lower())
    if not m: nomeas.append((page,i,addr,val)); continue
    real=int(m[3]); total=(int(m[1]) if m[1].isdigit() else -1); deref=(int(m[2]) if m[2].isdigit() else -1)
    if val==real: agree+=1
    else: disagree.append((page,i,addr,val,real,total,deref))
print("AGREE\t%d\tDISAGREE\t%d\tNOT-MEASURED\t%d" % (agree,len(disagree),len(nomeas)))
print("\n--- DISAGREEMENTS (page:line  address  published -> real  [lines/deref]) ---")
for d in sorted(disagree, key=lambda x:(x[2],x[0],x[1])):
    print("%s:%d\t%s\tpub=%d\treal=%d\t[lines=%d deref=%d]"%(d[0],d[1],d[2],d[3],d[4],d[5],d[6]))
print("\n--- distinct disagreeing addresses ---")
agg=collections.defaultdict(lambda: collections.Counter())
for d in disagree: agg[d[2]][ (d[3],d[4]) ]+=1
for a,c in sorted(agg.items()):
    print(a, dict(c))
print("\n--- UNBOUND (first 25) ---")
for u in unbound[:25]: print("%s:%d\tval=%d\t%s"%u)
