import re,sys,os
KB="/home/user/education-kb/"
SHELVES=["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
         "verticals/solutions.md","intel/market.md","intel/trends.md","compose/patterns.md",
         "intel/open-gaps.md"]
VOCAB={"North America","EMEA","APAC","LATAM","Global"}
fail=[]
# C1 frontmatter
for s in SHELVES:
    t=open(KB+s,encoding="utf-8").read().splitlines()
    if t[0].strip()!="---": fail.append(f"C1 {s}: no frontmatter"); continue
    end=next(i for i in range(1,len(t)) if t[i].strip()=="---")
    fm=dict(l.split(":",1) for l in t[1:end] if ":" in l)
    fm={k.strip():v.strip() for k,v in fm.items()}
    for key in ("industry","region","updated"):
        if key not in fm: fail.append(f"C1 {s}: missing {key}")
    if fm.get("region") not in VOCAB: fail.append(f"C1 {s}: region {fm.get('region')!r} out of vocab")
    if fm.get("updated")!="2026-10-26": fail.append(f"C1 {s}: updated={fm.get('updated')}")
print("C1 frontmatter+vocab: 9 shelves checked")
# C2 region heading contract
CANON=re.compile(r"^## +Opportunities by region\s*$")
lines=open(KB+"intel/market.md",encoding="utf-8").read().splitlines()
st=[i for i,l in enumerate(lines) if CANON.match(l)]
if len(st)!=1: fail.append(f"C2 canonical blocks={len(st)}")
else:
    s0=st[0]; e0=len(lines)
    for i in range(s0+1,len(lines)):
        if lines[i].startswith("## ") and not lines[i].startswith("###"): e0=i; break
    subs=[l[4:].strip() for l in lines[s0:e0] if l.startswith("### ") and not l.startswith("#### ")]
    if set(subs)!=VOCAB: fail.append(f"C2 subheads={subs}")
    print(f"C2 region contract: 1 canonical block, subheads={subs}")
# C3 template/header row as data in the NEW p451 sections only
DELIM=re.compile(r"^\|[\s:|-]+\|?\s*$")
PLACE=re.compile(r"^\|\s*(nombre|name|repo|repository|licencia|license|descripci[oó]n|description|url|stars?)\s*\|",re.I)
for s in SHELVES:
    txt=open(KB+s,encoding="utf-8").read()
    seg=txt.split("`p451`")
    if len(seg)<2: continue
    # inspect the first p451 block only (up to the first horizontal rule after it)
    blk=seg[1].split("\n---\n")[0]
    L=blk.splitlines()
    for i,ln in enumerate(L):
        if PLACE.match(ln.strip()):
            nxt=L[i+1].strip() if i+1<len(L) else ""
            if not DELIM.match(nxt):
                fail.append(f"C3 {s}: placeholder-shaped row renders as DATA: {ln.strip()[:60]}")
print("C3 placeholder-row scan: p451 blocks checked")
# C4 append-only: p450 section still present and p451 precedes it
for s in ["agents/trending.md","repos/trending.md"]:
    txt=open(KB+s,encoding="utf-8").read()
    i451=txt.find("`p451`"); i450=txt.find("`p450`")
    if i451<0 or i450<0: fail.append(f"C4 {s}: missing marker")
    elif not (i451<i450): fail.append(f"C4 {s}: p451 not above p450")
    else: print(f"C4 {s}: append-only OK (p451 @{i451} < p450 @{i450})")
print()
if fail:
    print("🔴 FAIL"); [print("  ",f) for f in fail]; sys.exit(1)
print("🟢 all 4 re-implemented contracts GREEN")
