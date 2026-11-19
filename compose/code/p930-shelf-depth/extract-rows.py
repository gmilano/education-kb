import re,sys,json
files=["agents/top.md","repos/foundations.md","verticals/solutions.md"]
rows=[]
seen=set()
for f in files:
    for ln,line in enumerate(open(f,encoding='utf-8'),1):
        if not line.startswith('|'): continue
        m=re.search(r'https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)',line)
        if not m: continue
        slug=f"{m.group(1)}/{m.group(2)}".rstrip('.')
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        # published stars = first cell that is a pure integer (with optional commas)
        stars=None
        for c in cells:
            cc=c.replace('**','').replace(',','').strip()
            if re.fullmatch(r'\d{1,7}',cc):
                stars=int(cc); break
        # published licence = cell containing a known SPDX-ish token
        lic=None
        for c in cells:
            if re.search(r'MIT|Apache-2\.0|BSD|ISC|MPL-2\.0|Unlicense|0BSD|GPL|AGPL|LGPL|CC[ -]BY|CC0|EPL|MulanPSL|NOASSERTION|NONE|ODbL|EUPL',c):
                lic=c; break
        key=(f,slug,ln)
        if (f,slug) in seen: continue
        seen.add((f,slug))
        rows.append({"file":f,"line":ln,"slug":slug,"pub_stars":stars,"pub_lic":lic})
json.dump(rows,open(sys.argv[1],'w'),indent=0)
print(f"{len(rows)} rows from {len(files)} files")
from collections import Counter
print(Counter(r['file'] for r in rows))
