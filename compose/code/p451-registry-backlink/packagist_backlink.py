import json,urllib.request,sys
for n in sys.argv[1:]:
    try:
        with urllib.request.urlopen("https://repo.packagist.org/packages/%s.json"%n,timeout=30) as r:
            d=json.load(r).get("package",{})
            vs=d.get("versions",{})
            lic=set()
            for v in vs.values():
                for l in (v.get("license") or []): lic.add(l)
            print(f"{n}\t200\trepo={d.get('repository','-')}\tabandoned={d.get('abandoned','NO')}\tlicenses={sorted(lic) or '-'}\tversions={len(vs)}\ttime={d.get('time','-')[:10]}")
    except Exception as e:
        print(f"{n}\t{getattr(e,'code','ERR')}\t-\t-\t-\t-\t-")
