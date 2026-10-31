import sys,os,json,re,collections,urllib.request
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import grade,ws,punct,sha12
res=json.load(open(sys.argv[1]))
tal=collections.Counter(r["verdict"] for r in res)
print("=== VERDICT TALLY (100 repositories) ===")
for k,v in tal.most_common(): print(f"  {v:3d}  {k}")
# canonical ws byte lengths for residual sizing
CANON_WS={"Apache-2.0":10221,"GPL-3.0":34281,"AGPL-3.0":33687,"LGPL-3.0-rider-only":7317,
          "LGPL-3.0-rider+GPL":41761,"BSD-3-Clause":1453}
MARK=[("AGPL-3.0",r"GNU AFFERO GENERAL PUBLIC LICENSE"),
      ("LGPL",r"GNU LESSER GENERAL PUBLIC LICENSE"),
      ("GPL-2.0",r"GNU GENERAL PUBLIC LICENSE.{0,400}Version 2"),
      ("GPL-3.0",r"GNU GENERAL PUBLIC LICENSE.{0,400}Version 3"),
      ("Apache-2.0",r"Apache License.{0,200}Version 2\.0"),
      ("MIT",r"MIT License|Permission is hereby granted, free of charge"),
      ("BSD",r"Redistribution and use in source and binary forms"),
      ("MPL-2.0",r"Mozilla Public License"),
      ("EPL",r"Eclipse Public License"),
      ("CC0",r"CC0 1\.0|Creative Commons Zero"),
      ("CC-BY",r"Creative Commons Attribution"),
      ("ISC",r"ISC License"),
      ("Unlicense",r"This is free and unencumbered software released into the public domain"),
      ("PolyForm",r"PolyForm"),("BUSL",r"Business Source License"),
      ("SSPL",r"Server Side Public License"),("Proprietary",r"All rights reserved")]
def detect(t):
    for name,pat in MARK:
        if re.search(pat,t,re.I|re.S): return name
    return "UNIDENTIFIED"
print("\n=== RESIDUALS, family detected from payload ===")
rows=[]
for r in res:
    if r["verdict"]!="RESIDUAL": continue
    u=f"https://raw.githubusercontent.com/{r['slug']}/{r['branch']}/{r['path']}"
    try: b=urllib.request.urlopen(u,timeout=60).read()
    except Exception as e: print("  FETCHFAIL",r["slug"],e); continue
    t=ws(b).decode()
    fam=detect(t)
    shelf=",".join(r["shelf_families"])
    agree = fam in shelf or (fam=="LGPL" and "LGPL" in shelf)
    delta=""
    if fam in CANON_WS: delta=f"{len(t.encode())-CANON_WS[fam]:+d} ws B"
    elif fam=="LGPL": delta=f"{len(t.encode())} ws B"
    rows.append(dict(slug=r["slug"],path=r["path"],raw_B=r.get("raw_B"),detected=fam,
                     shelf=shelf,agree=agree,delta=delta,sha_punct=r.get("sha_punct")))
    print(f"  {'OK ' if agree else 'XX '} {fam:12s} shelf={shelf:22s} {delta:12s} {r['slug']} ({r['path']}, {r.get('raw_B')} B)")
json.dump(rows,open(sys.argv[2],"w"),indent=1)
dis=[x for x in rows if not x["agree"]]
print(f"\n=== {len(dis)} of {len(rows)} residuals: payload family DISAGREES with shelf row ===")
c=collections.Counter(x["detected"] for x in rows)
print("detected-family distribution:",dict(c))
