import json,os,sys,time,urllib.request,urllib.error,urllib.parse
TOK=os.environ.get("GITHUB_TOKEN")
H={"Accept":"application/vnd.github+json","User-Agent":"kb-audit"}
if TOK: H["Authorization"]="Bearer "+TOK
def get(url):
    for attempt in range(5):
        try:
            req=urllib.request.Request(url,headers=H)
            with urllib.request.urlopen(req,timeout=40) as r: return r.status,json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (403,429): time.sleep(20); continue
            return e.code,None
        except Exception: time.sleep(5); continue
    return -1,None
rows=json.load(open(sys.argv[1]))
slugs=sorted({r["slug"] for r in rows})
print("unique slugs:",len(slugs))
found={}
B=20
for i in range(0,len(slugs),B):
    batch=slugs[i:i+B]
    q=" ".join("repo:"+s for s in batch)
    st,d=get("https://api.github.com/search/repositories?per_page=100&q="+urllib.parse.quote(q))
    if st==200 and d:
        for it in d.get("items",[]):
            found[it["full_name"].lower()]={"full_name":it["full_name"],"stars":it["stargazers_count"],
              "lic":(it.get("license") or {}).get("spdx_id"),"pushed":it["pushed_at"][:10],
              "archived":it["archived"],"fork":it.get("fork")}
    print(f"batch {i//B+1}/{(len(slugs)+B-1)//B} status={st} cum_found={len(found)}",flush=True)
    time.sleep(2.5)
json.dump(found,open(sys.argv[2],'w'),indent=0)
miss=[s for s in slugs if s.lower() not in found]
json.dump(miss,open(sys.argv[3],'w'),indent=0)
print("FOUND",len(found),"ABSENT",len(miss))
