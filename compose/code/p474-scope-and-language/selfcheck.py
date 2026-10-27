import re, os, subprocess, sys, csv

SHELVES = ["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
           "verticals/solutions.md","intel/market.md","intel/trends.md",
           "compose/patterns.md","intel/open-gaps.md"]
REGIONS = {"North America","EMEA","APAC","LATAM","Global"}
problems=[]

# 1 - frontmatter + closed vocabulary region
print("=== 1. frontmatter keys + closed-vocabulary region ===")
ok=0
for s in SHELVES:
    t=open(s,encoding="utf-8").read().split("\n")
    assert t[0].strip()=="---", s
    end=next(i for i,l in enumerate(t[1:],1) if l.strip()=="---")
    fm=dict()
    for l in t[1:end]:
        if ":" in l: k,v=l.split(":",1); fm[k.strip()]=v.strip()
    good = fm.get("industry")=="education" and fm.get("region") in REGIONS and "updated" in fm
    ok+=good
    if not good: problems.append(f"frontmatter {s}: {fm}")
    print(f"   {'OK ' if good else 'BAD'} {s:28} industry={fm.get('industry')} region={fm.get('region')} updated={fm.get('updated')}")
print(f"   -> {ok}/{len(SHELVES)} pass")

# 2 - p474 section tables: separator, pipe consistency, no header row as data
print("\n=== 2. p474 tables: separator present, pipe count consistent, no header published as data ===")
HEADER_WORDS={"nombre","repo","licencia","descripcion","descripción","name","license","stars",
              "nome","licenca","licença"}
tables=rows=0; tbl_problems=[]; hdr_findings=[]
for s in SHELVES:
    body=open(s,encoding="utf-8").read()
    m=re.search(r"\n## 🆕 `p474`.*?(?=\n## |\Z)", body, re.S)
    if not m: problems.append(f"{s}: no p474 section"); continue
    sec=m.group(0).split("\n")
    i=0
    while i < len(sec):
        if sec[i].strip().startswith("|"):
            blk=[]
            while i<len(sec) and sec[i].strip().startswith("|"):
                blk.append(sec[i].strip()); i+=1
            if len(blk)>=2 and re.fullmatch(r"\|[\s:|-]+\|", blk[1]):
                tables+=1
                n=blk[0].count("|")
                for j,l in enumerate(blk):
                    if l.count("|")!=n:
                        tbl_problems.append(f"{s} table@{tables} row{j}: {l.count('|')} pipes vs {n}")
                data=blk[2:]; rows+=len(data)
                for l in data:
                    cells=[c.strip().strip("*`").lower() for c in l.strip("|").split("|")]
                    if cells and all(c in HEADER_WORDS or c=="" for c in cells) and any(cells):
                        hdr_findings.append(f"{s}: {l}")
            else:
                if len(blk)>=2: tbl_problems.append(f"{s}: pipe block without separator: {blk[0][:60]}")
        else: i+=1
print(f"   tables={tables}  data rows={rows}")
print(f"   pipe/separator problems: {len(tbl_problems)}")
for p in tbl_problems[:10]: print("      "+p)
print(f"   header-row-as-data findings: {len(hdr_findings)}")
for p in hdr_findings[:10]: print("      "+p)
problems += tbl_problems + hdr_findings

# 3 - append-only containment on trending shelves vs HEAD
print("\n=== 3. append-only containment on trending shelves (vs git HEAD) ===")
for s in ["agents/trending.md","repos/trending.md"]:
    old=subprocess.run(["git","show",f"HEAD:{s}"],capture_output=True,text=True).stdout
    new=open(s,encoding="utf-8").read()
    oldbody=old.split("---",2)[2] if old.count("---")>=2 else old
    contained=oldbody.strip() in new
    print(f"   {'OK ' if contained else 'BAD'} {s}: prior body contained verbatim = {contained}")
    if not contained: problems.append(f"append-only broken: {s}")

# 4 - canonical block
print("\n=== 4. single canonical Opportunities-by-region block ===")
mk=open("intel/market.md",encoding="utf-8").read()
n=len(re.findall(r"\n## Opportunities by region\n", mk))
kids=re.search(r"\n## Opportunities by region\n(.*?)(?=\n## )", mk, re.S)
kid=re.findall(r"\n### (.+)", kids.group(1)) if kids else []
print(f"   live bare canonical blocks = {n}; children = {kid}")
if n!=1 or set(kid)!=REGIONS: problems.append(f"canonical block: n={n} kids={kid}")

# 5 - digest traceability
print("\n=== 5. digest traceability: every sha256-12 printed in a p474 section is in an evidence ledger ===")
led=set()
for f in os.listdir("evidence"):
    if "p474" in f:
        for tok in re.findall(r"\b[0-9a-f]{12}\b", open("evidence/"+f,encoding="utf-8").read()): led.add(tok)
# digests carried from earlier passes are traceable to their own pass ledgers
carried=set()
for f in os.listdir("evidence"):
    if f.endswith(".tsv") and "p474" not in f:
        for tok in re.findall(r"\b[0-9a-f]{12}\b", open("evidence/"+f,encoding="utf-8",errors="replace").read()): carried.add(tok)
printed=set(); missing=[]
for s in SHELVES:
    body=open(s,encoding="utf-8").read()
    m=re.search(r"\n## 🆕 `p474`.*?(?=\n## |\Z)", body, re.S)
    if not m: continue
    for tok in re.findall(r"`([0-9a-f]{12})`", m.group(0)):
        printed.add(tok)
        if tok not in led and tok not in carried: missing.append((s,tok))
print(f"   distinct digests printed in p474 sections: {len(printed)}")
print(f"   in this pass's ledgers: {len([t for t in printed if t in led])}; "
      f"traceable to an earlier pass ledger: {len([t for t in printed if t not in led and t in carried])}")
print(f"   UNTRACEABLE: {len(missing)}")
for s,t in missing[:12]: print(f"      {s}: {t}")
problems += [f"untraceable digest {t} in {s}" for s,t in missing]

print("\n" + "="*70)
print(f"TOTAL PROBLEMS: {len(problems)}")
print(f"MEASURED: {tables} tables / {rows} data rows in p474 sections")
