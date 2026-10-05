#!/usr/bin/env python3
"""p326 veredicto — cruza la cesion MEDIDA del titular (eje A) contra la EDICION
que cada item cita en su `oer` (eje B). Unidad: el item. Denominador: 13.371.
"""
import json, os, re, sys
from collections import Counter
POOL = os.path.join(sys.argv[1] if len(sys.argv) > 1 else "/tmp/oatc", "content-pool")
# cesion leida del PAYLOAD del titular (openstax/osbooks-*), eje A de este instrumento
TITULAR = {
    "calculus-volume-1": "CC BY-NC-SA 4.0", "college-algebra-2e": "CC BY-NC-SA 4.0",
    "college-physics-2e": "CC BY-NC-SA 4.0", "elementary-algebra-2e": "CC BY-NC-SA 4.0",
    "intermediate-algebra-2e": "CC BY-NC-SA 4.0", "precalculus-2e": "CC BY-NC-SA 4.0",
    "university-physics-volume-1": "CC BY-NC-SA 4.0", "introductory-statistics-2e": "CC BY-NC-SA 4.0",
    "physics": "CC BY 4.0",
    # el titular NO publica estas ediciones: ausencia ASERIDA por enumeracion de collections/
    "introductory-statistics": "NO-PUBLICADA-POR-EL-TITULAR",
    "precalculus": "NO-PUBLICADA-POR-EL-TITULAR",
}
pat = re.compile(r"openstax\.org/(?:details/)?books/([^/\s<>]+)")
v = Counter(); por_slug = {}
for d in sorted(os.listdir(POOL)):
    f = os.path.join(POOL, d, d + ".json")
    if not os.path.isfile(f): continue
    try: j = json.load(open(f, encoding="utf-8"))
    except Exception: v["ILEGIBLE"] += 1; continue
    oer, lic = str(j.get("oer") or ""), str(j.get("license") or "").strip()
    dice_by = "licenses/by/4.0" in lic.lower() or lic.lower() in ("cc by 4.0", "cc-by-4.0")
    m = pat.search(oer)
    if m:
        slug = m.group(1); ced = TITULAR.get(slug, "SLUG-NO-MEDIDO")
        a = por_slug.setdefault(slug, Counter()); a["_n"] += 1; a["dice_by"] += int(dice_by)
        a["vacia"] += int(lic == ""); a["ced"] = ced
        if ced == "CC BY-NC-SA 4.0":
            v["A_contradice_al_titular" if dice_by else "B_no_declara_titular_NC"] += 1
        elif ced == "CC BY 4.0":
            v["C_titular_SI_cede_BY"] += 1
        else:
            v["D_edicion_no_publicada_escape_ABIERTA"] += 1
    elif "oatutor.io" in oer.lower():
        v["E_autoria_propia_de_OATutor"] += 1
    elif "ds100.org" in oer.lower():
        v["F_campo_de_cesion_con_URL_de_procedencia"] += 1
    else:
        v["G_titular_no_resuelto"] += 1
tot = sum(v.values())
print(f"denominador (problemas): {tot}\n")
ORD = ["A_contradice_al_titular","B_no_declara_titular_NC","C_titular_SI_cede_BY",
       "D_edicion_no_publicada_escape_ABIERTA","E_autoria_propia_de_OATutor",
       "F_campo_de_cesion_con_URL_de_procedencia","G_titular_no_resuelto","ILEGIBLE"]
for k in ORD:
    if v[k]: print(f"  {k:44s} {v[k]:6d}  {100*v[k]/tot:5.1f} %")
ship = v["C_titular_SI_cede_BY"] + v["E_autoria_propia_de_OATutor"]
print(f"\n  EMBARCABLE en entrega comercial (titular cede BY o es OATutor): {ship} = {100*ship/tot:.1f} %")
print(f"  NO embarcable, MEDIDO:                                          {v['A_contradice_al_titular']+v['B_no_declara_titular_NC']} = {100*(v['A_contradice_al_titular']+v['B_no_declara_titular_NC'])/tot:.1f} %")
print(f"  SIN RESOLVER (declarado, no inferido):                          {v['D_edicion_no_publicada_escape_ABIERTA']+v['F_campo_de_cesion_con_URL_de_procedencia']+v['G_titular_no_resuelto']} = {100*(v['D_edicion_no_publicada_escape_ABIERTA']+v['F_campo_de_cesion_con_URL_de_procedencia']+v['G_titular_no_resuelto'])/tot:.1f} %")
print(f"\n{'edicion citada por el item':32s} {'cede el titular':22s} {'n':>6s} {'dice BY':>8s} {'vacia':>7s}")
for s, a in sorted(por_slug.items(), key=lambda x: -x[1]["_n"]):
    print(f"{s:32s} {a['ced']:22s} {a['_n']:6d} {a['dice_by']:8d} {a['vacia']:7d}")
