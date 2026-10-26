import json,urllib.request,sys
def get(pkg):
    url="https://registry.npmjs.org/"+pkg.replace("/","%2f")
    try:
        with urllib.request.urlopen(url,timeout=30) as r:
            return r.status,json.load(r)
    except Exception as e:
        return getattr(e,'code','ERR'),None
names=sys.argv[1:]
print("pkg\tstatus\trepository\tlicense\tlatest\tmodified\tmaintainers")
for n in names:
    st,d=get(n)
    if d is None:
        print(f"{n}\t{st}\t-\t-\t-\t-\t-"); continue
    latest=d.get("dist-tags",{}).get("latest","-")
    vmeta=d.get("versions",{}).get(latest,{})
    repo=vmeta.get("repository") or d.get("repository") or "-"
    if isinstance(repo,dict): repo=repo.get("url","-")
    lic=vmeta.get("license") or d.get("license") or "-"
    mod=d.get("time",{}).get("modified","-")
    created=d.get("time",{}).get("created","-")
    maint=",".join(sorted(m.get("name","?") for m in (d.get("maintainers") or [])))
    nver=len(d.get("versions",{}))
    print(f"{n}\t{st}\t{repo}\t{lic}\t{latest} ({nver}v)\t{created[:10]}..{mod[:10]}\t{maint}")
