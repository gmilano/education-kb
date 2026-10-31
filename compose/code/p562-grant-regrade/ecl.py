import sys,os,json,re,urllib.request,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import grade,ws,punct,sha12
SRC=[("spdx ECL-2.0","https://raw.githubusercontent.com/spdx/license-list-data/main/text/ECL-2.0.txt"),
     ("opensource.org ECL-2.0","https://opensource.org/licenses/ECL-2.0"),
     ("sakaiproject/sakai master/LICENSE","https://raw.githubusercontent.com/sakaiproject/sakai/master/LICENSE"),
     ("opencast/opencast develop/LICENSE","https://raw.githubusercontent.com/opencast/opencast/develop/LICENSE"),
     ("Apereo OpenLRW master/LICENSE","https://raw.githubusercontent.com/Apereo-Learning-Analytics-Initiative/OpenLRW/master/LICENSE")]
print("=== ECL-2.0 pin attempt ===")
pins=[]
for name,u in SRC:
    try: b=urllib.request.urlopen(u,timeout=60).read()
    except Exception as e: print(f"  FETCHFAIL {name}: {e}"); continue
    if b"Educational Community License" not in b:
        print(f"  NOT-ECL   {name} ({len(b)} B) — page is not the licence text"); continue
    g=grade(b); pins.append((name,g))
    print(f"  {name:38s} raw={g['raw_B']:6d} {g['sha_raw']}  ws={g['ws_B']:6d} {g['sha_ws']}  punct={g['sha_punct']}")
d=collections.Counter(g['sha_punct'] for _,g in pins)
print("  distinct punct digests:",dict(d))
if d: print("  CONVERGES" if len(d)==1 else f"  NO CONVERGENCE at punct across {len(pins)} sources")

print("\n=== shelf-wide ECL census: scanning all swept payloads ===")
res=json.load(open(sys.argv[1]))
hits=[]
for r in res:
    if not r.get("path"): continue
    u=f"https://raw.githubusercontent.com/{r['slug']}/{r['branch']}/{r['path']}"
    try: b=urllib.request.urlopen(u,timeout=60).read()
    except Exception: continue
    if b"Educational Community License" in b:
        g=grade(b); hits.append((r['slug'],r['shelf_families'],g))
        print(f"  ECL  shelf={','.join(r['shelf_families']):12s} {r['slug']:52s} raw={g['raw_B']:6d} punct={g['sha_punct']}")
print(f"\n{len(hits)} shelf rows carry ECL-2.0 while graded as something else")
json.dump([dict(slug=s,shelf=f,**g) for s,f,g in hits],open(sys.argv[2],"w"),indent=1)
