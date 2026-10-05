#!/usr/bin/env python3
"""p326 eje B — CENSO (no muestra) de los 13.371 problemas de OATutor-Content.

Cruza DOS campos que el pase 104 midio por separado:
  `license` -> lo que el item DICE que cede
  `oer`     -> de donde SALIO el item, es decir QUIEN es el titular

La pregunta que decide la receta no es «que dice el campo» sino
«coincide lo que dice con lo que el TITULAR cede». Un item cuyo `oer`
apunta a openstax.org y cuyo `license` dice `CC BY 4.0` esta
DECLARANDO UNA CESION QUE SU TITULAR NO OTORGA (p326 eje A: los 8
libros de OpenStax son CC BY-NC-SA 4.0).
"""
import json, os, sys
from urllib.parse import urlparse
from collections import Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/oatc"
POOL = os.path.join(ROOT, "content-pool")

def clase_licencia(v):
    if v is None:          return "AUSENTE"
    s = str(v).strip()
    if s == "":            return "VACIA"
    low = s.lower()
    if "by-nc" in low or "by_nc" in low:            return "CC-BY-NC"
    if "licenses/by/4.0" in low or low in ("cc by 4.0", "cc-by-4.0"):
        return "CC-BY-4.0"
    if low.startswith("http"):
        return "CC-BY-4.0" if "creativecommons.org/licenses/by/4.0" in low else "URL-NO-LICENCIA"
    return "OTRO"

def host(v):
    if not v: return "SIN-OER"
    try:
        h = (urlparse(str(v)).hostname or "").lower()
    except Exception:
        return "OER-ILEGIBLE"
    return h.removeprefix("www.") or "OER-ILEGIBLE"

TITULAR = {
    # host del `oer` -> quien es el titular, y que cede (medido en el eje A)
    "openstax.org":  ("OpenStax", "CC BY-NC-SA 4.0"),
    "oatutor.io":    ("OATutor (autoria propia)", "README: CC BY 4.0"),
}

rows, cnt_lic, cnt_host, cross, por_curso = [], Counter(), Counter(), Counter(), {}
total = bad = 0
for d in sorted(os.listdir(POOL)):
    f = os.path.join(POOL, d, d + ".json")
    if not os.path.isfile(f):
        continue
    total += 1
    try:
        with open(f, encoding="utf-8") as fh:
            j = json.load(fh)
    except Exception:
        bad += 1
        rows.append((d, "PARSE-FAIL", "PARSE-FAIL", "", ""))
        continue
    cl, h = clase_licencia(j.get("license")), host(j.get("oer"))
    curso = (j.get("courseName") or "SIN-CURSO").strip()
    cnt_lic[cl] += 1; cnt_host[h] += 1; cross[(h, cl)] += 1
    a = por_curso.setdefault(curso, Counter()); a[cl] += 1; a["_n"] += 1; a["host:" + h] += 1
    rows.append((d, cl, h, curso, str(j.get("license"))[:120]))

with open("census-items.2026-10-05.tsv", "w", encoding="utf-8") as o:
    o.write("problema\tclase_licencia\thost_oer\tcurso\tvalor_license\n")
    for r in rows: o.write("\t".join(r) + "\n")

print(f"problemas leidos: {total}   ilegibles: {bad}")
print("\n== clase de licencia (CENSO) ==")
for k, v in cnt_lic.most_common(): print(f"  {k:16s} {v:6d}  {100*v/total:5.1f} %")
print("\n== host del campo `oer` (quien es el titular) ==")
for k, v in cnt_host.most_common(12): print(f"  {k:28s} {v:6d}  {100*v/total:5.1f} %")
print("\n== CRUCE titular x lo que el item declara ==")
print(f"  {'host oer':26s} {'clase declarada':16s} {'n':>6s}   veredicto")
for (h, cl), v in sorted(cross.items(), key=lambda x: -x[1]):
    if v < 5: continue
    tit = TITULAR.get(h)
    if tit and tit[1].startswith("CC BY-NC-SA") and cl == "CC-BY-4.0":
        ver = "CONTRADICE AL TITULAR (dice BY, el titular cede NC-SA)"
    elif tit and tit[1].startswith("CC BY-NC-SA") and cl in ("VACIA", "OTRO"):
        ver = "no declara; el titular cede NC-SA"
    elif h == "oatutor.io":
        ver = "autoria propia: el README SI es cesion del titular"
    elif cl == "URL-NO-LICENCIA":
        ver = "el campo de cesion lleva una URL de PROCEDENCIA"
    else:
        ver = "titular no resuelto"
    print(f"  {h:26s} {cl:16s} {v:6d}   {ver}")

with open("por-curso.2026-10-05.tsv", "w", encoding="utf-8") as o:
    o.write("curso\tn\tCC-BY-4.0\tVACIA\tOTRO\tURL-NO-LICENCIA\tCC-BY-NC\tAUSENTE\thost_oer_dominante\n")
    for c, a in sorted(por_curso.items(), key=lambda x: -x[1]["_n"]):
        hosts = [(k[5:], v) for k, v in a.items() if k.startswith("host:")]
        dom = max(hosts, key=lambda x: x[1])[0] if hosts else "-"
        o.write("\t".join([c, str(a["_n"])] + [str(a[k]) for k in
                ("CC-BY-4.0","VACIA","OTRO","URL-NO-LICENCIA","CC-BY-NC","AUSENTE")] + [dom]) + "\n")
print("\nTSV: census-items.2026-10-05.tsv  ·  por-curso.2026-10-05.tsv")
