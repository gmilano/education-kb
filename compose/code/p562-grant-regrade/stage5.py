import sys,os,re,urllib.request,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import ws,punct,sha12
def body(t):
    """stage 5: operative-body isolation.
       (a) drop the APPENDIX boilerplate, (b) drop pointer URLs, (c) fold list enumerators."""
    t=re.split(r'END OF TERMS AND CONDITIONS',t)[0]
    t=re.sub(r'https?://\S+','<URL>',t)
    t=re.sub(r'(?<![A-Za-z0-9])(?:[0-9]{1,2}|[a-z])[.)]\s+',' ',t)
    return re.sub(r'\s+',' ',t).strip()
FAM={
 "ECL-2.0":{"spdx":"https://raw.githubusercontent.com/spdx/license-list-data/main/text/ECL-2.0.txt",
   "sakai":"https://raw.githubusercontent.com/sakaiproject/sakai/master/LICENSE",
   "opencast":"https://raw.githubusercontent.com/opencast/opencast/develop/LICENSE",
   "openlrw":"https://raw.githubusercontent.com/Apereo-Learning-Analytics-Initiative/OpenLRW/master/LICENSE"},
 "Apache-2.0":{"apache.org":"https://www.apache.org/licenses/LICENSE-2.0.txt",
   "spdx":"https://raw.githubusercontent.com/spdx/license-list-data/main/text/Apache-2.0.txt",
   "oppia":"https://raw.githubusercontent.com/oppia/oppia/develop/LICENSE"},
}
for fam,srcs in FAM.items():
    print(f"=== {fam} at stage 5 (operative body) ===")
    d=collections.Counter()
    for k,u in srcs.items():
        b=urllib.request.urlopen(u,timeout=60).read()
        t=body(punct(ws(b)).decode())
        h=sha12(t); d[h]+=1
        print(f"  {k:12s} {len(t.encode()):6d} B  {h}")
    print(f"  distinct: {len(d)} -> {'CONVERGES' if len(d)==1 else 'NO CONVERGENCE'}\n")
# cross-family: is ECL distinguishable from Apache at stage 5?
def get(u): return body(punct(ws(urllib.request.urlopen(u,timeout=60).read())).decode())
ecl=get(FAM["ECL-2.0"]["sakai"]); ap=get(FAM["Apache-2.0"]["apache.org"])
print("=== ECL-2.0 vs Apache-2.0 at stage 5 ===")
print(f"  ECL    {len(ecl.encode())} B {sha12(ecl)}")
print(f"  Apache {len(ap.encode())} B {sha12(ap)}")
print(f"  distinct: {sha12(ecl)!=sha12(ap)}  (must be True — the patent grant differs)")
print(f"  ECL carries education patent-scope clause: {'specific to the needs of the education' in ecl}")
print(f"  Apache carries it: {'specific to the needs of the education' in ap}")
