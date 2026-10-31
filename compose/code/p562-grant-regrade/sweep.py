import sys,os,json,re,subprocess,urllib.request,urllib.error
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from norm import grade

PATHS=["LICENSE","LICENSE.md","LICENSE.txt","LICENCE","LICENCE.md","LICENCE.txt",
       "COPYING","COPYING.txt","COPYING.LESSER","license","license.txt","License.txt",
       "LICENSE-2.0.txt","LICENSE.LGPL-3.0","docs/License.txt","LICENSE.APACHE2"]
# canonical pins from p561 (calibrated 14/14 this pass)
PIN={
 "0ffddef9e48f":("Apache-2.0","ws"), "cd83b5f465e5":("GPL-3.0","punct"),
 "2cd0fb7883a3":("AGPL-3.0","punct"), "de41de5bdd96":("AGPL-3.0-edX-rider","punct"),
 "690578875bea":("LGPL-3.0-rider-only","punct"), "05e49932344e":("LGPL-3.0-rider+GPL","punct"),
}
PIN_RAW={"cfc7749b96f6":"Apache-2.0","074e6e32c86a":"Apache-2.0","8ceb4b9ee5ad":"GPL-3.0",
 "fb981668c18a":"GPL-3.0","c53a65c2fd56":"GPL-3.0","d8a6cc31abc1":"AGPL-3.0",
 "57c8ff33c9c0":"AGPL-3.0","e12d78569742":"AGPL-3.0-edX-rider","996af0513df2":"LGPL-3.0-rider+GPL",
 "e3a994d82e64":"LGPL-3.0-rider-only"}

def branch(slug):
    try:
        o=subprocess.run(["git","ls-remote","--symref",f"https://github.com/{slug}","HEAD"],
                         capture_output=True,text=True,timeout=90).stdout
        m=re.search(r"ref:\s+refs/heads/(\S+)\s+HEAD",o)
        if m: return m.group(1)
        return "UNRESOLVED" if not o.strip() else "NO-SYMREF"
    except Exception: return "UNRESOLVED"

def fetch(slug,br,p):
    u=f"https://raw.githubusercontent.com/{slug}/{br}/{p}"
    try:
        r=urllib.request.urlopen(u,timeout=60)
        return r.read() if r.status==200 else None
    except Exception: return None

def one(item):
    slug,fams=item
    br=branch(slug)
    rec=dict(slug=slug,shelf_families=sorted(fams),branch=br,path=None,verdict="",**{})
    if br in ("UNRESOLVED","NO-SYMREF"):
        rec["verdict"]="ADDRESS-UNRESOLVED"; return rec
    for p in PATHS:
        b=fetch(slug,br,p)
        if b is None or len(b)<40: continue
        g=grade(b); rec.update(g); rec["path"]=p
        if g["sha_raw"] in PIN_RAW:
            rec["verdict"]="CANONICAL-BYTE-IDENTICAL"; rec["matched"]=PIN_RAW[g["sha_raw"]]
        elif g["sha_punct"] in PIN:
            fam,st=PIN[g["sha_punct"]]
            rec["verdict"]="CANONICAL-VERBATIM"; rec["matched"]=fam; rec["converged_at"]=st
        elif g["sha_ws"] in PIN:
            fam,st=PIN[g["sha_ws"]]
            rec["verdict"]="CANONICAL-VERBATIM"; rec["matched"]=fam; rec["converged_at"]="ws"
        else:
            rec["verdict"]="RESIDUAL"
        return rec
    rec["verdict"]="NO-GRANT-AT-16-PATHS"; return rec

pop=json.load(open(sys.argv[1]))
agg={}
for k in pop:
    slug,fam=k.rsplit("|",1); agg.setdefault(slug,set()).add(fam)
items=sorted(agg.items())
print(f"sweeping {len(items)} distinct repositories",flush=True)
res=[]
with ThreadPoolExecutor(max_workers=8) as ex:
    for i,r in enumerate(ex.map(one,items),1):
        res.append(r); print(f"{i:3d} {r['verdict']:26s} {r['slug']}",flush=True)
json.dump(res,open(sys.argv[2],"w"),indent=1)
