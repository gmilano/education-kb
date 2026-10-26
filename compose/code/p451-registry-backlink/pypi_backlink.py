import json,urllib.request,sys
print("pkg\tstatus\tlicense\tversion\thome/repo")
for n in sys.argv[1:]:
    try:
        with urllib.request.urlopen("https://pypi.org/pypi/%s/json"%n,timeout=30) as r:
            d=json.load(r); i=d.get("info",{})
            urls=i.get("project_urls") or {}
            print(f"{n}\t200\t{i.get('license') or i.get('license_expression') or '-'}\t{i.get('version','-')}\t{urls or i.get('home_page') or '-'}")
    except Exception as e:
        print(f"{n}\t{getattr(e,'code','ERR')}\t-\t-\t-")
