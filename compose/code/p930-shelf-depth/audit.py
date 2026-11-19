# p930 — SUPERSEDED BY audit2.py, kept as the record of a blocked channel.
# GET /repos/{owner}/{repo} returns 403 for every address in this base:
#   'GitHub access to this repository is not enabled for this session.'
# The per-repo REST endpoint is scoped to repositories attached to the session, so it
# cannot be used for third-party audit here. search/repositories is NOT so scoped —
# which is why this base has always measured stars and licences through the search
# channel plus raw.githubusercontent.com byte-reads. See audit2.py.

import json,os,sys,csv,time
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.error
TOK=os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
H={"Accept":"application/vnd.github+json","User-Agent":"kb-audit"}
if TOK: H["Authorization"]="Bearer "+TOK
def get(url,raw=False):
    req=urllib.request.Request(url,headers=H)
    try:
        with urllib.request.urlopen(req,timeout=30) as r:
            b=r.read()
            return r.status, (b if raw else json.loads(b))
    except urllib.error.HTTPError as e: return e.code,None
    except Exception as e: return -1,str(e)
rows=json.load(open(sys.argv[1]))
def work(r):
    st,d=get("https://api.github.com/repos/"+r["slug"])
    o=dict(r); o["http"]=st
    if st==200 and isinstance(d,dict):
        o["api_stars"]=d.get("stargazers_count")
        o["api_lic"]=(d.get("license") or {}).get("spdx_id")
        o["pushed_at"]=(d.get("pushed_at") or "")[:10]
        o["archived"]=d.get("archived")
        o["full_name"]=d.get("full_name")
        o["default_branch"]=d.get("default_branch")
    return o
with ThreadPoolExecutor(max_workers=8) as ex:
    out=list(ex.map(work,rows))
json.dump(out,open(sys.argv[2],'w'),indent=0)
from collections import Counter
print("HTTP:",Counter(o["http"] for o in out))
print("archived:",sum(1 for o in out if o.get("archived")))
