import json,sys
rows=json.load(open(sys.argv[1]))
n=len(rows); held=sum(1 for r in rows if r['held'])
print(f"TOTAL n={n}  held={held} ({100*held/n:.1f}%)  stale={n-held} ({100*(n-held)/n:.1f}%)")
print()
buckets=[(0,1,'<1 h'),(1,6,'1-6 h'),(6,24,'6-24 h'),(24,72,'1-3 d'),(72,168,'3-7 d'),(168,720,'7-30 d'),(720,10**9,'>30 d')]
print(f"{'age of commit at pin time':<26} {'n':>5} {'held':>6} {'P(held)':>9}")
print('-'*50)
for lo,hi,lab in buckets:
    sub=[r for r in rows if lo<=r['age_h']<hi]
    if not sub: continue
    h=sum(1 for r in sub if r['held'])
    print(f"{lab:<26} {len(sub):>5} {h:>6} {100*h/len(sub):>8.1f}%")
print()
# the p447 rule as a binary classifier: "age_at_pin < 24h => will go stale"
tp=sum(1 for r in rows if r['age_h']<24 and not r['held'])
fp=sum(1 for r in rows if r['age_h']<24 and r['held'])
fn=sum(1 for r in rows if r['age_h']>=24 and not r['held'])
tn=sum(1 for r in rows if r['age_h']>=24 and r['held'])
print("p447 RULE as classifier (predict STALE iff age_at_pin < 24 h):")
print(f"  predicted stale & stale (TP)={tp}   predicted stale & held (FP)={fp}")
print(f"  predicted hold  & stale (FN)={fn}   predicted hold  & held (TN)={tn}")
prec=tp/(tp+fp) if tp+fp else 0; rec=tp/(tp+fn) if tp+fn else 0
print(f"  precision={100*prec:.1f}%  recall={100*rec:.1f}%  accuracy={100*(tp+tn)/n:.1f}%")
print()
# strict form of p447's claim: pinned_commit_date == HEAD date  <=> pin held  (i.e. age<24h => stale ALWAYS)
viol=[r for r in rows if r['age_h']<24 and r['held']]
print(f"p447 claimed the biconditional held in every row (n=5). VIOLATIONS here: {len(viol)} of {tp+fp} rows with age<24h")
print()
# per-repo stale rate
from collections import defaultdict
d=defaultdict(lambda:[0,0])
for r in rows: d[r['slug']][0]+=1; d[r['slug']][1]+= (0 if r['held'] else 1)
print(f"{'repository':<46} {'n':>3} {'stale':>6} {'rate':>7}")
print('-'*66)
for s,(t,st) in sorted(d.items(), key=lambda x:-x[1][1]/x[1][0]):
    print(f"{s:<46} {t:>3} {st:>6} {100*st/t:>6.1f}%")
