import subprocess,hashlib,sys
slugs=[l.strip() for l in open('cands2.txt') if l.strip()]
print("slug\tbranch\tpath\thttp\tsha256_12\tbytes\tfirstline")
for s in slugs:
    done=False
    for br in ('main','master'):
        for path in ('LICENSE','LICENSE.md','LICENSE.txt','COPYING'):
            url=f"https://raw.githubusercontent.com/{s}/{br}/{path}"
            p=subprocess.run(['curl','-sL','-w','\n%{http_code}',url],capture_output=True,text=True)
            body,_,code=p.stdout.rpartition('\n'); code=code.strip()
            if code=='200' and body.strip():
                h=hashlib.sha256(body.encode()).hexdigest()[:12]
                fl=[x for x in body.splitlines() if x.strip()][0][:70]
                print(f"{s}\t{br}\t{path}\t200\t{h}\t{len(body)}\t{fl}")
                done=True; break
        if done: break
    if not done: print(f"{s}\t-\t-\tNOFILE\t-\t-\t-")
