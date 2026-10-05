#!/usr/bin/env python3
"""P327 accion C: huella CRUDA vs NORMALIZADA de los archivos de licencia.

DEFECTO CORREGIDO EN ESTE PASE (P329): la v1 capturaba con
subprocess.run(text=True), que aplica universal-newlines y convierte CRLF->LF
ANTES de hashear. La columna "cruda" NO era cruda: para un LICENSE de 429
lineas con CRLF daba 21.013 B en vez de 21.442 B, o sea borraba exactamente el
fenomeno que P327 existe para medir. Se captura en BINARIO.
"""
import hashlib, subprocess, sys, collections, re

def get_bytes(url):
    """Devuelve (bytes crudos, codigo). SIN universal-newlines."""
    r=subprocess.run(["curl","-s","-w","\n%{http_code}","--max-time","20",url],
                     capture_output=True)   # <-- binario: sin text=True
    out=r.stdout
    i=out.rfind(b"\n")
    if i<0: return b"", "000"
    return out[:i], out[i+1:].decode("ascii","replace").strip()

def calib():
    _,g=get_bytes("https://raw.githubusercontent.com/microsoft/vscode/main/README.md")
    _,b=get_bytes("https://raw.githubusercontent.com/microsoft/vscode/main/ZZZ-NO.md")
    return g=="200" and b=="404", g, b

def norm_bytes(raw):
    b=raw.replace(b"\r\n",b"\n").replace(b"\r",b"\n")
    if b and not b.endswith(b"\n"): b+=b"\n"
    return b

def family(raw):
    head=" ".join(norm_bytes(raw).decode("utf-8","replace").split("\n")[:6]).lower()
    head=re.sub(r"\s+"," ",head)
    if "gnu affero" in head: return "AGPL-3.0"
    if "gnu lesser" in head: return "LGPL-3.0"
    if "gnu general public" in head: return "GPL"
    if "apache license" in head: return "Apache-2.0"
    if "mit license" in head or "permission is hereby granted, free of charge" in head: return "MIT"
    if "bsd" in head: return "BSD"
    if "mozilla public" in head: return "MPL-2.0"
    if "attribution-noncommercial-sharealike" in head: return "CC BY-NC-SA 4.0"
    if "attribution-sharealike" in head: return "CC BY-SA"
    if "attribution" in head and "4.0 international" in head: return "CC BY 4.0"
    if "unlicense" in head: return "Unlicense"
    return None

ok,g,b=calib()
if not ok:
    print(f"CANAL NO CALIBRADO (good={g} bad={b}) -- NO-CLAIM", file=sys.stderr); sys.exit(2)
print(f"# canal CALIBRADO buena={g} inventada={b}", file=sys.stderr)

NAMES=["LICENSE","LICENSE.md","LICENSE.txt","COPYING","LICENCE","license","License"]
src=sys.argv[1]
slugs=[l.strip() for l in open(src) if l.strip() and not l.startswith("#")]
print("slug\tarchivo\tbytes_crudos\tsha_crudo\tbytes_norm\tsha_norm\tcrlf\tfamilia")
groups=collections.defaultdict(list); diff=0; measured=0
for s in slugs:
    got=False
    for ref in ("HEAD","main","master"):
        if got: break
        for nm in NAMES:
            raw,c=get_bytes(f"https://raw.githubusercontent.com/{s}/{ref}/{nm}")
            if c=="200" and raw.strip():
                n=norm_bytes(raw)
                sr=hashlib.sha256(raw).hexdigest(); sn=hashlib.sha256(n).hexdigest()
                crlf = "SI" if b"\r\n" in raw else "no"
                fam=family(raw); measured+=1
                if sr!=sn: diff+=1
                print(f"{s}\t{nm}\t{len(raw)}\t{sr[:16]}\t{len(n)}\t{sn[:16]}\t{crlf}\t{fam or 'UNCLASSIFIED'}")
                groups[sn].append((s,len(raw),sr[:12],fam)); got=True; break
    if not got:
        print(f"{s}\t-\t-\t-\t-\t-\t-\tNO-CLAIM(sin archivo de licencia alcanzable)")
nc=0; members_in_collapse=0
print("# --- COLAPSOS: mismo texto normalizado, huella cruda DISTINTA ---", file=sys.stderr)
for sn,ms in groups.items():
    if len({m[2] for m in ms})>1:
        nc+=1; members_in_collapse+=len(ms)
        print(f"# norm={sn[:16]} familia={ms[0][3]} miembros={len(ms)}", file=sys.stderr)
        for s,bb,sr,fam in ms: print(f"#     {s:52s} crudo={sr} bytes={bb}", file=sys.stderr)
print(f"# medidas={measured}  huella cruda != normalizada: {diff}  colapsos={nc} ({members_in_collapse} miembros)", file=sys.stderr)
