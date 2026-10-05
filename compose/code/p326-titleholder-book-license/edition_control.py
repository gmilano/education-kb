#!/usr/bin/env python3
"""p326 control C6 — la escapatoria de EDICION.

Hipotesis alternativa que hay que matar antes de publicar el hallazgo:
«los items dicen CC BY 4.0 porque salieron de una edicion ANTERIOR que SI era
CC BY 4.0, y OpenStax relicencio despues». Si fuera cierta, el item seria
correcto y el error estaria en comparar contra la edicion de hoy.

Se mata leyendo el SLUG DE LIBRO que el propio item cita en su `oer`: si el item
cita la MISMA edicion cuyo collection.xml declara NC-SA, no hay escapatoria.
"""
import json, os, re, sys
from collections import Counter
ROOT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/oatc"
POOL = os.path.join(ROOT, "content-pool")
pat = re.compile(r"openstax\.org/(?:details/)?books/([^/\s<>]+)")
cnt = Counter()
for d in sorted(os.listdir(POOL)):
    f = os.path.join(POOL, d, d + ".json")
    if not os.path.isfile(f): continue
    try:
        j = json.load(open(f, encoding="utf-8"))
    except Exception: continue
    m = pat.search(str(j.get("oer") or ""))
    if not m: continue
    lic = str(j.get("license") or "").strip()
    cl = "CC-BY-4.0" if "licenses/by/4.0" in lic.lower() else ("VACIA" if lic == "" else "OTRO")
    cnt[(m.group(1), cl)] += 1
libros = sorted({k[0] for k in cnt})
print(f"{'slug citado por el ITEM':38s} {'CC-BY-4.0':>10s} {'VACIA':>7s} {'OTRO':>6s} {'total':>7s}")
tot_by = tot = 0
for b in libros:
    a, v, o = cnt[(b,"CC-BY-4.0")], cnt[(b,"VACIA")], cnt[(b,"OTRO")]
    n = a+v+o; tot_by += a; tot += n
    print(f"{b:38s} {a:10d} {v:7d} {o:6d} {n:7d}")
print(f"{'TOTAL':38s} {tot_by:10d} {'':7s} {'':6s} {tot:7d}")
print(f"\nediciones distintas citadas por los items: {len(libros)}")
