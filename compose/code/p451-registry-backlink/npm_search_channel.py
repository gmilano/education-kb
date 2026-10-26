import json,urllib.request,urllib.parse,sys
def search(text,size=100):
    u="https://registry.npmjs.org/-/v1/search?"+urllib.parse.urlencode({"text":text,"size":size})
    with urllib.request.urlopen(u,timeout=40) as r: return json.load(r)
seen={}
for q in sys.argv[1:]:
    try: d=search(q)
    except Exception as e:
        print(f"# QUERY {q!r} -> ERROR {e}"); continue
    print(f"# QUERY {q!r} -> total={d.get('total')}")
    for o in d.get("objects",[]):
        p=o["package"]; links=p.get("links",{}) or {}
        repo=links.get("repository") or "-"
        key=p["name"]
        if key in seen: continue
        seen[key]=1
        print("\t".join([p["name"],p.get("version","-"),(p.get("date") or "-")[:10],repo,(p.get("description") or "")[:90].replace("\t"," ").replace("\n"," ")]))
