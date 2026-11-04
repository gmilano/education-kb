import re,sys,glob
FILES=["agents/top.md","agents/trending.md","repos/foundations.md","repos/trending.md",
       "verticals/solutions.md","intel/market.md","intel/trends.md","compose/patterns.md"]
R="/home/user/education-kb/"
verified=set()
for p in ["existence.tsv","existence-recipe.tsv"]:
    for l in open(p):
        f=l.split('\t')
        if len(f)>1 and f[1]=="LIVE": verified.add(f[0].lower())
# carried addresses verified in earlier passes (named in prose, re-cited not re-read)
CARRIED={"hkuds/deeptutor","thu-maic/openmaic","patchy631/ai-engineering-hub",
         "christian-bick/edugraph-dataset","umass-ml4ed/kcgen-kt",
         "jiuwang123/quiet-reader-english-learning","ai-infra-curriculum/ai-infra-engineer-learning",
         "ai-infra-curriculum","ml-engineering-curriculum","ai-engineering-curriculum",
         "ai-governance-curriculum","ai-startup-curriculum","ai-workforce-curriculum"}
PLACE=re.compile(r'\b(nombre|licencia|descripci|tbd|todo|xxx|lorem|example\.com|your-?repo|placeholder)\b',re.I)
CLOSED={"North America","EMEA","APAC","LATAM","Global"}
errs=[];warns=[];stats={"tables":0,"rows":0,"urls":0}
for rel in FILES:
    txt=open(R+rel,encoding='utf-8').read()
    # the p649 section only: from its heading to the next top-level pass heading
    m=re.search(r'^## 🆕 `p649`.*?(?=^## 🆕 `p648`)',txt,re.S|re.M)
    if not m: errs.append(f"{rel}: p649 section not found"); continue
    sec=m.group(0)
    # 648-Q: strip fenced code blocks before any line-oriented table test
    nofence=re.sub(r'```.*?```','',sec,flags=re.S)
    lines=nofence.split('\n')
    # table structure
    i=0
    while i<len(lines):
        if lines[i].strip().startswith('|'):
            tbl=[]
            while i<len(lines) and lines[i].strip().startswith('|'): tbl.append(lines[i]); i+=1
            if len(tbl)>=2:
                stats["tables"]+=1
                def ncells(l):
                    # mask escaped pipes and pipes inside code spans
                    s=l.replace('\\|','\x00')
                    s=re.sub(r'`[^`]*`',lambda x:x.group(0).replace('|','\x00'),s)
                    return len(s.strip().strip('|').split('|'))
                w=ncells(tbl[0])
                for k,row in enumerate(tbl):
                    stats["rows"]+=1
                    if ncells(row)!=w:
                        errs.append(f"{rel}: RAGGED table row (want {w} got {ncells(row)}): {row.strip()[:90]}")
                    if k>=2 and PLACE.search(row):
                        errs.append(f"{rel}: PLACEHOLDER-AS-DATA row: {row.strip()[:90]}")
                if not re.match(r'^\|[\s:|-]+\|$',tbl[1].strip()):
                    errs.append(f"{rel}: table has no delimiter row: {tbl[1].strip()[:80]}")
        else: i+=1
    # unescaped pipe inside a code span
    for n,l in enumerate(lines,1):
        if not l.strip().startswith('|'): continue
        for cs in re.findall(r'`[^`]*`',l):
            if '|' in cs and '\\|' not in cs:
                errs.append(f"{rel}:{n}: unescaped | inside code span in a table row: {cs[:50]}")
    # every github.com slug must be verified this pass or carried
    for slug in re.findall(r'github\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)',sec):
        stats["urls"]+=1
        s=slug.lower().rstrip('.,)')
        if s not in verified and s not in CARRIED:
            errs.append(f"{rel}: UNVERIFIED github address cited: {slug}")
    for slug in re.findall(r'github\.com/([A-Za-z0-9._-]+)\)',sec):
        s=slug.lower()
        if '/' not in s and s not in CARRIED: warns.append(f"{rel}: org-only link {slug}")
    # region headings closed vocabulary
    for h in re.findall(r'^### ([A-Za-z ]+) — `p649`',sec,re.M):
        if h.strip() not in CLOSED: errs.append(f"{rel}: region heading not in closed vocabulary: {h}")
# market.md structural contract
mk=open(R+"intel/market.md",encoding='utf-8').read()
sec=re.search(r'^## 🆕 `p649`.*?(?=^## 🆕 `p648`)',mk,re.S|re.M).group(0)
if sec.count('## Opportunities by region')!=1: errs.append("market: need exactly one '## Opportunities by region' in the p649 section")
got=re.findall(r'^### ([A-Za-z ]+) — `p649`',sec,re.M)
if [g.strip() for g in got]!=["North America","EMEA","APAC","LATAM"]:
    errs.append(f"market: region subsections wrong/incomplete: {got}")
print(f"tables={stats['tables']} rows={stats['rows']} github_addresses_cited={stats['urls']}")
print(f"ERRORS: {len(errs)}")
for e in errs[:40]: print("  🔴",e)
print(f"warnings: {len(warns)}")
for w in warns[:10]: print("  🟡",w)
sys.exit(1 if errs else 0)
