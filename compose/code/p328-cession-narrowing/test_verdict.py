#!/usr/bin/env python3
"""Suite de P328. Publica su total propio (P126: cuenta el total, no imprime 'ALL PASSED')."""
import verdict as V
import os, sys

OK=0; FAIL=[]
def eq(got, want, name):
    global OK
    if got==want: OK+=1
    else: FAIL.append(f"{name}: got {got!r} want {want!r}")

# --- eje 1: familia desde la URL del titular ---
eq(V.fam_from_url("http://creativecommons.org/licenses/by/4.0/"), V.BY, "url by")
eq(V.fam_from_url("http://creativecommons.org/licenses/by-nc-sa/4.0/"), V.NC, "url by-nc-sa")
eq(V.fam_from_url("https://creativecommons.org/licenses/by-sa/4.0/"), "CC BY-SA", "url by-sa")
eq(V.fam_from_url(""), None, "url vacia -> None")
eq(V.fam_from_url(None), None, "url None -> None")
# CONTROL NEGATIVO (P299): by-nc-sa contiene la subcadena 'by' y NO debe salir CC BY 4.0
eq(V.fam_from_url("http://creativecommons.org/licenses/by-nc-sa/4.0/") != V.BY, True, "by-nc-sa no es by")

# --- eje 2: familia que declara el item; ausencia != permiso ---
eq(V.fam_from_item(""), "(sin declarar)", "item vacio")
eq(V.fam_from_item(None), "(sin declarar)", "item None")
eq(V.fam_from_item("   "), "(sin declarar)", "item blancos")
eq(V.fam_from_item("https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>"), V.BY, "item by 4.0")
eq(V.fam_from_item("CC4.0"), "CC4.0 (sin clausulas)", "CC4.0 no resuelve")
eq(V.fam_from_item("https://ds100.org/su26/past-exams/"), "otro", "url de tercero")

# --- obra citada: las DOS formas de URL (el extractor del pase 105 perdia una) ---
eq(V.work_from_oer("https://openstax.org/details/books/precalculus-2e <OpenStax>"), "precalculus-2e", "forma details")
eq(V.work_from_oer("https://openstax.org/books/precalculus-2e"), "precalculus-2e", "forma corta")
eq(V.work_from_oer("https://openstax.org/"), None, "sin obra")
eq(V.work_from_oer("openai"), None, "oer openai no es obra")
eq(V.work_from_oer(""), None, "oer vacio")

# --- el veredicto ---
eq(V.verdict("https://creativecommons.org/licenses/by/4.0/", V.NC), "CONTRADICE", "item amplia")
eq(V.verdict("https://creativecommons.org/licenses/by/4.0/", V.BY), "CORRECTO", "item concuerda")
eq(V.verdict("https://creativecommons.org/licenses/by-nc-sa/4.0/", V.NC), "CORRECTO", "item concuerda NC")
eq(V.verdict("https://creativecommons.org/licenses/by-nc-sa/4.0/", V.BY), "CORRECTO", "ceder MENOS se puede")
eq(V.verdict("", V.NC), "SIN-DECLARAR", "ausencia no es contradiccion")
eq(V.verdict("", V.BY), "SIN-DECLARAR", "ausencia tampoco con titular permisivo")
# CONTROL NEGATIVO: sin cesion del titular NO hay veredicto, ni a favor ni en contra
eq(V.verdict("https://creativecommons.org/licenses/by/4.0/", None), "NO-CLAIM", "sin titular -> NO-CLAIM")
eq(V.verdict("", None), "NO-CLAIM", "sin titular y sin item -> NO-CLAIM")
eq(V.verdict("CC4.0", V.NC), "NO-CLAIM", "CC4.0 no resuelve -> NO-CLAIM")

# --- estrechamiento: la identidad es el collection-id, no el slug ---
rows=[
 {"col":"col11667","ref":"1e","familia":V.BY,"slug":"precalculus"},
 {"col":"col11667","ref":"main","familia":V.NC,"slug":"precalculus-2e"},
 {"col":"col12081","ref":"main","familia":V.BY,"slug":"physics"},
]
n=V.narrowed(rows)
eq(len(n),1,"un estrechamiento")
eq(n[0],("col11667",V.BY,V.NC),"el par correcto")
# CONTROL NEGATIVO: una coleccion que vive en UN solo ref no estrecha nada
eq(V.narrowed([{"col":"col12081","ref":"main","familia":V.BY,"slug":"physics"}]),[],"un ref solo no estrecha")
# CONTROL NEGATIVO: si no cambia, no es estrechamiento
eq(V.narrowed([{"col":"cX","ref":"1e","familia":V.BY,"slug":"a"},
               {"col":"cX","ref":"main","familia":V.BY,"slug":"a"}]),[],"igual no estrecha")
# CONTROL NEGATIVO de DIRECCION: de NC a BY es AMPLIACION, no estrechamiento
eq(V.narrowed([{"col":"cY","ref":"1e","familia":V.NC,"slug":"a"},
               {"col":"cY","ref":"main","familia":V.BY,"slug":"a"}]),[],"ampliacion no es estrechamiento")

# --- el barrido real versionado, si esta al lado ---
here=os.path.dirname(os.path.abspath(__file__))
tsv=os.path.join(here,"osbooks-cesion.tsv")
if os.path.exists(tsv):
    rows=V.load_tsv(tsv)
    eq(len(rows),36,"36 filas medidas")
    nar=V.narrowed(rows)
    eq(len(nar),10,"10 colecciones estrechan")
    eq(all(a==V.BY and b==V.NC for _,a,b in nar),True,"las 10 van de BY a NC-SA")
    main_by=[r["slug"] for r in rows if r["ref"]=="main" and r["familia"]==V.BY]
    eq(sorted(main_by),["physics","statistics"],"solo physics y statistics son CC BY en main")
    eq(len([r for r in rows if r["ref"]=="main"]),22,"22 colecciones en main")

print(f"{OK}/{OK+len(FAIL)}")
for f in FAIL: print("  FAIL:",f)
sys.exit(1 if FAIL else 0)
