import sys,os,re,json,collections,urllib.request,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import ws,punct,sha12
# the p378 fold: neutralise the filled template's variable span (year + holder)
def fold(b):
    t=punct(ws(b)).decode()
    t=re.sub(r'Copyright\s*(?:\(c\)|\(C\))?\s*[0-9]{4}(?:\s*[-,]\s*(?:[0-9]{4}|present))?\s*[^.]{0,120}?(?=\s+Permission is hereby granted)',
             'Copyright (c) <YEAR> <HOLDER>',t,flags=re.I)
    return t
MIT=["EduThemes/paper-lms","Selleo/mentingo","frappe/frappe","mitodl/learn-ai","opensalt/opensalt",
     "sonstellar969/open-moodle","theopenem/OneRoster.NET","ucfopen/canvasapi","vishalsachdev/canvas-mcp",
     "huggingface/smolagents"]
def br(s):
    o=subprocess.run(["git","ls-remote","--symref",f"https://github.com/{s}","HEAD"],capture_output=True,text=True,timeout=90).stdout
    m=re.search(r"ref:\s+refs/heads/(\S+)\s+HEAD",o); return m.group(1) if m else None
rows=[]
for s in MIT:
    b0=br(s)
    if not b0: print("unresolved",s); continue
    got=None
    for p in ("LICENSE","LICENSE.md","LICENSE.txt","license.txt"):
        try:
            r=urllib.request.urlopen(f"https://raw.githubusercontent.com/{s}/{b0}/{p}",timeout=60)
            if r.status==200: got=r.read(); break
        except Exception: pass
    if not got: continue
    t=punct(ws(got)).decode()
    if 'Permission is hereby granted, free of charge' not in t:
        print(f"  NOT-MIT  {s} (skipped)"); continue
    f=fold(got)
    rows.append(dict(slug=s,raw_B=len(got),punct_B=len(t.encode()),punct_sha=sha12(t),
                     fold_B=len(f.encode()),fold_sha=sha12(f)))
print(f"\n=== {len(rows)} MIT payloads, p378 fold applied ===")
print(f"{'repo':44s} {'raw':>6s} {'punct':>6s} {'punctsha':>13s} {'fold':>6s} {'foldsha':>13s}")
for r in rows:
    print(f"{r['slug']:44s} {r['raw_B']:6d} {r['punct_B']:6d} {r['punct_sha']:>13s} {r['fold_B']:6d} {r['fold_sha']:>13s}")
dl=collections.Counter(r['fold_B'] for r in rows); dd=collections.Counter(r['fold_sha'] for r in rows)
pp=collections.Counter(r['punct_sha'] for r in rows)
print(f"\ndistinct punct digests : {len(pp)} of {len(rows)}  (pre-fold — 561-D's 'no canonical digest')")
print(f"distinct folded LENGTHS: {len(dl)} of {len(rows)}  {dict(dl)}")
print(f"distinct folded DIGESTS: {len(dd)} of {len(rows)}")
mode=dl.most_common(1)[0]
print(f"\nmodal folded length    : {mode[0]} B on {mode[1]}/{len(rows)} payloads")
# FALSE-MATCH probe: does the fold LENGTH survive an added clause?
base=[r for r in rows if r['fold_B']==mode[0]]
if base:
    s=base[0]['slug']
    print(f"\n=== false-match probe on {s} ===")
    b0=br(s)
    for p in ("LICENSE","LICENSE.md","LICENSE.txt"):
        try:
            r=urllib.request.urlopen(f"https://raw.githubusercontent.com/{s}/{b0}/{p}",timeout=60)
            if r.status==200: orig=r.read(); break
        except Exception: pass
    t=punct(ws(orig)).decode()
    # substitution of EQUAL length in an operative word
    sub=t.replace("without restriction","without limitation",1)
    # Commons Clause style addition
    add=t+" The Software is provided for non-commercial use only."
    for name,v in (("stock",t),("equal-length substitution",sub),("added restriction",add)):
        fv=fold(v.encode())
        print(f"  {name:26s} fold_B={len(fv.encode()):5d}  fold_sha={sha12(fv)}  length-gate={'PASSES (false match)' if len(fv.encode())==mode[0] else 'catches it'}")
json.dump(rows,open(sys.argv[1],"w"),indent=1)
