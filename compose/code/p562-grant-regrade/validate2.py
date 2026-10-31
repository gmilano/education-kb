import re,os
KB="/tmp/education-kb/"
PAGES=["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
       "verticals/solutions.md","intel/trends.md","intel/market.md","compose/patterns.md",
       "intel/open-gaps.md","README.md"]
PLACE=re.compile(r'^\|\s*(nombre|name|repo|licencia|license|descripci[oó]n|description|tbd|xxx|\.\.\.|example|ejemplo|stars?)\s*\|',re.I)
def sec_of(p,t):
    if p=="README.md":
        m=re.search(r'^(## Pass 562\b.*?)(?=^## Pass \d|\Z)',t,re.M|re.S)
    else:
        m=re.search(r'^(## 🆕 `p562`.*?)(?=^## 🆕 `p5|\Z)',t,re.M|re.S)
    return m.group(1) if m else None
tables=ragged=ph=0; rows=0
for p in PAGES:
    t=open(KB+p,encoding='utf-8').read(); sec=sec_of(p,t)
    if sec is None: print("  !! no section",p); continue
    cur=[]
    def flush(cur):
        global tables,ragged
        if len(cur)>=2:
            tables+=1
            w=[len(re.findall(r'(?<!\\)\|',r)) for r in cur]
            if len(set(w))>1:
                ragged+=1
                print(f"  RAGGED {p}: widths {w}")
                for r in cur[:3]: print("     ",r[:120])
    for ln in sec.split('\n'):
        s=ln.strip()
        if s.startswith('|'):
            cur.append(s); rows+=1
            if PLACE.match(s): ph+=1; print("  PLACEHOLDER-AS-DATA",p,s[:90])
        else:
            flush(cur); cur=[]
    flush(cur)
print(f"\n  tables checked: {tables}   ragged: {ragged}   table rows: {rows}   placeholder-as-data: {ph}")
# measured matrix
ids=[f"562-{c}" for c in "ABCDEFGH"]
MP=PAGES[:8]
hit={p:{i:(i in (sec_of(p,open(KB+p,encoding='utf-8').read()) or "")) for i in ids} for p in MP}
print("\n=== MEASURED matrix ===")
LAB={"agents/top.md":"../agents/top.md","agents/trending.md":"../agents/trending.md",
     "repos/foundations.md":"../repos/foundations.md","repos/trending.md":"../repos/trending.md",
     "verticals/solutions.md":"../verticals/solutions.md","intel/trends.md":"../intel/trends.md",
     "intel/market.md":"../intel/market.md","compose/patterns.md":"../compose/patterns.md"}
lines=[]
for p in MP:
    cells=" | ".join("✔" if hit[p][i] else "·" for i in ids)
    lines.append(f"| [`{LAB[p]}`]({LAB[p]}#-p562--2026-10-31) | {cells} |")
    print(lines[-1])
open(os.environ.get("MATRIX_OUT","matrix.txt"),"w").write("\n".join(lines)+"\n")
orph=[i for i in ids if not any(hit[p][i] for p in MP)]
print(f"\n  ids cited: {8-len(orph)}/8   orphans: {orph or 'none'}")
