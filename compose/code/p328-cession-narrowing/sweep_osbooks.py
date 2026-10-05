#!/usr/bin/env python3
"""Cesion POR COLECCION leida del payload del TITULAR (openstax en GitHub).
Canal: raw.githubusercontent.com. Se NIEGA a emitir veredicto si el canal no
discrimina (P249). Empareja slug<->collection-id por ATRIBUTO, no por orden."""
import re, subprocess, sys

RAW="https://raw.githubusercontent.com/openstax/{repo}/{ref}/{path}"

def get(url):
    r=subprocess.run(["curl","-s","-w","\n%{http_code}","--max-time","25",url],
                     capture_output=True,text=True)
    out=r.stdout.rsplit("\n",1)
    return (out[0], out[1].strip() if len(out)>1 else "000")

def calibrate():
    _,g=get("https://raw.githubusercontent.com/microsoft/vscode/main/README.md")
    _,b=get("https://raw.githubusercontent.com/microsoft/vscode/main/ZZZ-NO-EXISTE.md")
    return g=="200" and b=="404", g, b

def fam(url):
    u=(url or "").lower()
    if "by-nc-sa" in u: return "CC BY-NC-SA 4.0"
    if "by-nc"    in u: return "CC BY-NC"
    if "by-sa"    in u: return "CC BY-SA"
    if "/by/"     in u: return "CC BY 4.0"
    if not u:           return "NO-CLAIM(sin md:license)"
    return "otro:"+url

def refs(repo):
    r=subprocess.run(["git","ls-remote","--heads",
                      f"https://github.com/openstax/{repo}"],
                     capture_output=True,text=True)
    if r.returncode!=0: return []
    return [l.split("refs/heads/")[1] for l in r.stdout.splitlines() if "refs/heads/" in l]

ok,g,b=calibrate()
if not ok:
    print(f"CANAL NO CALIBRADO (good={g} bad={b}) -- NO-CLAIM", file=sys.stderr); sys.exit(2)
print(f"# canal CALIBRADO: buena={g} inventada={b}", file=sys.stderr)

print("repo\tref\tslug\tcol\tlicencia_url\tfamilia")
for repo in sys.argv[1:]:
    have=refs(repo)
    if not have:
        print(f"# {repo}: INALCANZABLE", file=sys.stderr); continue
    for ref in ("main","1e"):
        if ref not in have: continue
        books,code=get(RAW.format(repo=repo,ref=ref,path="META-INF/books.xml"))
        if code!="200":
            print(f"# {repo}@{ref}: books.xml HTTP {code}", file=sys.stderr); continue
        # cada <book .../> es una entrada; parsear por elemento
        for m in re.finditer(r"<book\b[^>]*/?>", books):
            el=m.group(0)
            slug=re.search(r'slug="([^"]*)"',el)
            col =re.search(r'collection-id="([^"]*)"',el)
            if not slug: continue
            slug=slug.group(1); col=col.group(1) if col else "-"
            xml,c2=get(RAW.format(repo=repo,ref=ref,path=f"collections/{slug}.collection.xml"))
            if c2!="200":
                print(f"{repo}\t{ref}\t{slug}\t{col}\t-\tNO-CLAIM(collection HTTP {c2})"); continue
            u=re.search(r'md:license\s+url="([^"]*)"',xml)
            u=u.group(1) if u else ""
            print(f"{repo}\t{ref}\t{slug}\t{col}\t{u or '-'}\t{fam(u)}")
