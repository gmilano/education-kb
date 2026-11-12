import json,urllib.request,sys,re,os
PROX=os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
def get(u):
    try:
        req=urllib.request.Request(u,headers={"User-Agent":"kb-dep-audit"})
        return urllib.request.urlopen(req,timeout=25).read().decode("utf-8","replace")
    except Exception as e: return None
def npm(p):
    d=get("https://registry.npmjs.org/%s/latest"%urllib.parse.quote(p,safe='@'))
    if not d: return "REGISTRY-UNREACHABLE"
    try:
        j=json.loads(d); l=j.get("license") or j.get("licenses")
        if isinstance(l,list): l=",".join(x.get("type","?") for x in l)
        return l or "NONE-DECLARED"
    except Exception: return "UNPARSEABLE"
def pypi(p):
    d=get("https://pypi.org/pypi/%s/json"%p)
    if not d: return "REGISTRY-UNREACHABLE"
    try:
        j=json.loads(d)["info"]
        # PEP 639: modern packages use license_expression, NOT the legacy license field.
        # Reading only `license` reports MIT/BSD/Apache packages as NONE-DECLARED.
        le=(j.get("license_expression") or "").strip()
        if le: return le
        cls=[c for c in (j.get("classifiers") or []) if c.startswith("License ::")]
        if cls: return cls[-1].split("::")[-1].strip()
        l=(j.get("license") or "").strip()
        return (l[:40].replace("\n"," ") if l else "NONE-DECLARED-IN-METADATA")
    except Exception: return "UNPARSEABLE"
import urllib.parse
kind,path=sys.argv[1],sys.argv[2]
txt=open(path).read()
deps=[]
if kind=="npm":
    j=json.loads(txt)
    for sec in ("dependencies","devDependencies"):
        deps += list((j.get(sec) or {}).keys())
else:
    for line in txt.splitlines():
        line=line.split("#")[0].strip()
        m=re.match(r'^["\']?([A-Za-z0-9_.\-]+)',line)
        if m and line and not line.startswith("-"): deps.append(m.group(1))
seen=set(); out=[]
for d in deps:
    if d in seen: continue
    seen.add(d)
    lic = npm(d) if kind=="npm" else pypi(d)
    out.append((d,lic))
COPYLEFT=re.compile(r'GPL|AGPL|LGPL|SSPL|OSL|EUPL|CeCILL|CDDL|EPL|MPL|CC-BY-NC|NonCommercial|Proprietary',re.I)
for d,l in out:
    flag="FLAG" if COPYLEFT.search(l or "") else ("?" if "UNREACH" in (l or "") or "NONE" in (l or "") else "ok")
    print("%-5s %-34s %s"%(flag,d,l))
print("---- %d direct deps, %d flagged"%(len(out),sum(1 for d,l in out if COPYLEFT.search(l or ""))))
