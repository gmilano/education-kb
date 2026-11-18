#!/usr/bin/env python3
"""p888-candidate-verify: byte-read grants for p888 discovery candidates.
Honours 887-G1: scans ALL licence-ish paths and detects MULTIPLE family
titles inside a SINGLE payload (conjunctive grant), not first-title-wins.
Honours p887's control: a NOTICE is not a grant by default.
"""
import hashlib, json, re, subprocess, sys, os, time
OUT=os.path.dirname(os.path.abspath(__file__))

PATHS=["LICENSE","LICENSE.md","LICENSE.txt","LICENCE","LICENCE.md","COPYING",
       "LICENSE-MIT","LICENSE-APACHE","license","License","NOTICE","NOTICE.txt"]
# Family signatures: distinctive body text, not filenames.
SIG=[("Apache-2.0", r'Apache License\s*\n?\s*Version 2\.0'),
     ("MIT",        r'Permission is hereby granted, free of charge, to any person obtaining a copy'),
     ("BSD-3-Clause",r'Neither the name of .{0,120}? nor the names of its\s+contributors may be used to endorse'),
     ("BSD-3-Clause",r'3\.\s*Neither the name'),
     ("BSD-2-Clause",r'Redistributions in binary form must reproduce the above copyright'),
     ("GPL-3.0",    r'GNU GENERAL PUBLIC LICENSE\s*\n?\s*Version 3'),
     ("AGPL-3.0",   r'GNU AFFERO GENERAL PUBLIC LICENSE'),
     ("MPL-2.0",    r'Mozilla Public License Version 2\.0'),
     ("ISC",        r'Permission to use, copy, modify, and/or distribute this software'),
     ("Unlicense",  r'This is free and unencumbered software released into the public domain'),
     ("CC0-1.0",    r'CC0 1\.0 Universal'),]

def curl(url):
    r=subprocess.run(["curl","-sS","-m","25","-w","\n%{http_code}",url],capture_output=True,text=True)
    out=r.stdout
    if "\n" not in out: return None,0
    body,code=out.rsplit("\n",1)
    try: code=int(code)
    except: code=0
    return (body if code==200 else None), code

def families(text):
    """ALL families whose signature appears, with the byte span of the match."""
    found={}
    for fam,pat in SIG:
        m=re.search(pat,text,re.I|re.S)
        if m and fam not in found: found[fam]=m.start()
    return found

def commits12(slug):
    r=subprocess.run(["gh","api","-X","GET","search/commits","-f",
        f"q=repo:{slug} committer-date:>2025-11-18","-f","per_page=1"],
        capture_output=True,text=True,timeout=60)
    if r.returncode!=0: return None
    try: return json.loads(r.stdout).get("total_count")
    except: return None

CANDS=json.load(open(f"{OUT}/to-verify.json"))
res=[]
for c in CANDS:
    slug=c["slug"]; br=c["branch"]; rec={**c,"grants":[],"readme":None,"commits12":None,"arity":0}
    for p in PATHS:
        body,code=curl(f"https://raw.githubusercontent.com/{slug}/{br}/{p}")
        if not body: continue
        raw=body.encode("utf-8","replace")
        fams=families(body)
        rec["grants"].append({"path":p,"bytes":len(raw),
            "sha256_12":hashlib.sha256(raw).hexdigest()[:12],
            "families":sorted(fams.keys()),"n_families":len(fams)})
    # arity_own = distinct families across grant-bearing paths, NOTICE excluded unless sole
    grant_paths=[g for g in rec["grants"] if g["families"] and not g["path"].startswith("NOTICE")]
    notice_paths=[g for g in rec["grants"] if g["families"] and g["path"].startswith("NOTICE")]
    fams=set()
    for g in grant_paths: fams|=set(g["families"])
    rec["families_root"]=sorted(fams)
    rec["notice_families"]=sorted({f for g in notice_paths for f in g["families"]})
    rec["arity"]=len(fams)
    rb,rc=curl(f"https://raw.githubusercontent.com/{slug}/{br}/README.md")
    if rb: rec["readme"]=rb[:1800]; rec["readme_bytes"]=len(rb.encode())
    rec["readme_code"]=rc
    rec["commits12"]=commits12(slug)
    res.append(rec)
    fam=",".join(rec["families_root"]) or "NO-GRANT-FOUND"
    flag="  <== CONJUNCTIVE" if rec["arity"]>1 else ""
    mismatch=" <== SPDX-MISMATCH" if rec["families_root"] and c["spdx"] not in rec["families_root"] else ""
    print(f"{slug:<48} api={c['spdx']:<13} bytes={fam:<26} c12m={rec['commits12']}{flag}{mismatch}",flush=True)
    time.sleep(1.2)
json.dump(res,open(f"{OUT}/verified.json","w"),indent=1)
