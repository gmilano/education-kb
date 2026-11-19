import re,json,hashlib,sys,urllib.request,urllib.error
from concurrent.futures import ThreadPoolExecutor
CLEAN=[]
for f in ["agents/top.md","repos/foundations.md","verticals/solutions.md"]:
    for ln,line in enumerate(open(f,encoding='utf-8'),1):
        if not line.startswith('|'): continue
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(c)<5: continue
        m=re.fullmatch(r'\[?`?(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?))`?\]?(\(.*\))?',c[1])
        if not m: continue
        if not re.fullmatch(r'\*{0,2}[\d,]+\*{0,2}',c[3]): continue
        CLEAN.append({"file":f,"line":ln,"slug":f"{m.group(2)}/{m.group(3)}","pub_lic":c[2],
                      "pub_stars":int(c[3].replace('**','').replace(',',''))})
print("clean cohort:",len(CLEAN),file=sys.stderr)
NAMES=["LICENSE","LICENSE.md","LICENSE.txt","LICENCE","COPYING","LICENSE-MIT","license"]
def fetch(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"kb"}),timeout=25) as r:
            return r.read()
    except Exception: return None
def classify(t):
    h=t[:3000].decode('utf-8','replace')
    hl=' '.join(h.split()).lower()
    if 'gnu affero general public license' in hl: return 'AGPL-3.0'
    if 'gnu lesser general public license' in hl: return 'LGPL'
    if 'gnu general public license' in hl: return 'GPL-2.0' if 'version 2' in hl[:400] else 'GPL-3.0'
    if 'apache license' in hl: return 'Apache-2.0'
    if 'mozilla public license' in hl: return 'MPL-2.0'
    if 'educational community license' in hl: return 'ECL-2.0'
    if 'boost software license' in hl: return 'BSL-1.0'
    if 'mulan' in hl: return 'MulanPSL-2.0'
    if 'creative commons' in hl or 'creativecommons.org' in hl:
        if 'sharealike' in hl or '-sa' in hl: return 'CC-BY-SA'
        if 'noncommercial' in hl or '-nc' in hl: return 'CC-BY-NC'
        if 'cc0' in hl or 'public domain dedication' in hl: return 'CC0-1.0'
        return 'CC-BY'
    if 'redistribution and use in source and binary' in hl:
        return 'BSD-3-Clause' if 'neither the name' in hl else 'BSD-2-Clause'
    if 'permission to use, copy, modify, and/or distribute' in hl: return 'ISC'
    if 'permission is hereby granted, free of charge' in hl: return 'MIT'
    if 'unlicense' in hl or 'this is free and unencumbered' in hl: return 'Unlicense'
    return 'UNKNOWN'
def work(r):
    for n in NAMES:
        b=fetch(f"https://raw.githubusercontent.com/{r['slug']}/HEAD/{n}")
        if b and len(b)>40:
            o=dict(r); o["path"]=n; o["bytes"]=len(b)
            o["sha12"]=hashlib.sha256(b).hexdigest()[:12]; o["byte_lic"]=classify(b)
            return o
    o=dict(r); o["path"]=None; o["byte_lic"]="NO-PAYLOAD"; o["bytes"]=0; o["sha12"]=""
    return o
with ThreadPoolExecutor(max_workers=12) as ex: out=list(ex.map(work,CLEAN))
json.dump(out,open("compose/code/p929-shelf-depth/grants.json","w"),indent=0)
import collections
print("byte-read result:",collections.Counter(o["byte_lic"] for o in out))
