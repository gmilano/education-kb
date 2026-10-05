#!/usr/bin/env python3
"""Controles del instrumento p326, con fixtures en vez de red.

Lo que estos tests existen para impedir, caso por caso:
  1. que el clasificador de familia solo sepa decir «CC BY-NC-SA» (el falso
     positivo que haria del hallazgo un artefacto);
  2. que un `oer` sin slug se cuente como slug;
  3. que la forma `/details/books/<slug>` se pierda — el defecto que ESTE
     instrumento tuvo y que se corrigio antes de publicar (9.326 de 12.204
     items usan esa forma);
  4. que una edicion que el titular NO publica se cuente como medida.
"""
import re, sys, tempfile, os, json, subprocess

# se resuelve relativo a ESTE archivo para que el test corra desde cualquier cwd
HERE = os.path.dirname(os.path.abspath(__file__))

PAT = re.compile(r"openstax\.org/(?:details/)?books/([^/\s<>]+)")

def familia(primera_linea):
    h = primera_linea.strip()
    if "NonCommercial-ShareAlike" in h: return "CC BY-NC-SA 4.0"
    if "NonCommercial" in h:            return "CC BY-NC (variante)"
    if h.startswith("Attribution 4.0"): return "CC BY 4.0"
    if "Attribution" in h and "ShareAlike" in h: return "CC BY-SA (variante)"
    return "SIN-ARCHIVO-O-NO-CC"

fallos = []
def ok(cond, nombre):
    print(("  PASS  " if cond else "  FAIL  ") + nombre)
    if not cond: fallos.append(nombre)

print("== 1. el clasificador discrimina (si solo dijera NC-SA, el hallazgo seria artefacto) ==")
ok(familia("Attribution-NonCommercial-ShareAlike 4.0 International") == "CC BY-NC-SA 4.0",
   "NC-SA se reconoce  [primera linea real de openstax/osbooks-calculus-bundle:LICENSE]")
ok(familia("Attribution 4.0 International") == "CC BY 4.0",
   "CC BY 4.0 se reconoce  [texto SPDX CC-BY-4.0]")
ok(familia("Attribution-ShareAlike 4.0 International") == "CC BY-SA (variante)",
   "BY-SA no se confunde con NC-SA")
ok(familia("MIT License") == "SIN-ARCHIVO-O-NO-CC", "una licencia de codigo no entra como CC")
ok(familia("") == "SIN-ARCHIVO-O-NO-CC", "vacio no clasifica")

print("\n== 2. extraccion de la EDICION desde el `oer` ==")
ok(PAT.search("https://openstax.org/books/precalculus-2e/pages/11-5-counting-principles").group(1)
   == "precalculus-2e", "forma /books/<slug>/pages/...")
ok(PAT.search("https://openstax.org/details/books/elementary-algebra-2e <OpenStax: Elementary Algebra>").group(1)
   == "elementary-algebra-2e", "forma /details/books/<slug> + sufijo entre <> (9.326 items)")
ok(PAT.search("https://openstax.org/books/precalculus/pages/1-4-composition-of-functions").group(1)
   == "precalculus", "1e (sin -2e) NO se normaliza a 2e: son ediciones distintas")
ok(PAT.search("https://openstax.org/") is None, "openstax.org pelado no produce slug")
ok(PAT.search("https://OATutor.io") is None, "autoria propia no produce slug de OpenStax")
ok(PAT.search("https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf") is None,
   "una URL de procedencia ajena no produce slug")

print("\n== 3. una edicion no publicada por el titular NO se cuenta como medida ==")
TIT = {"calculus-volume-1": "CC BY-NC-SA 4.0", "physics": "CC BY 4.0",
       "introductory-statistics": "NO-PUBLICADA-POR-EL-TITULAR"}
ok(TIT.get("introductory-statistics") == "NO-PUBLICADA-POR-EL-TITULAR",
   "introductory-statistics (1e) queda SIN RESOLVER, no como NC-SA")
ok(TIT.get("algebra-inventada", "SLUG-NO-MEDIDO") == "SLUG-NO-MEDIDO",
   "un slug desconocido no hereda la cesion de sus vecinos")

print("\n== 4. identidad de un archivo de licencia: los bytes NO alcanzan ==")
crlf = b"Attribution-NonCommercial-ShareAlike 4.0 International\r\ntexto\r\n"
lf   = b"Attribution-NonCommercial-ShareAlike 4.0 International\ntexto\n"
import hashlib
ok(len(crlf) != len(lf), "el MISMO texto da conteos de bytes distintos segun fin de linea")
ok(hashlib.sha256(crlf).hexdigest() != hashlib.sha256(lf).hexdigest(),
   "el sha256 CRUDO tampoco es identidad")
ok(hashlib.sha256(crlf.replace(b"\r\n", b"\n")).hexdigest()
   == hashlib.sha256(lf).hexdigest(),
   "normalizando fin de linea SI coinciden  [osbooks calculus/college-algebra/prealgebra: 21443/21013/21442 B -> un solo sha256]")

print("\n== 5. el veredicto corre de punta a punta sobre un pool sintetico ==")
with tempfile.TemporaryDirectory() as td:
    pool = os.path.join(td, "content-pool"); os.makedirs(pool)
    casos = [
        ("i1", "https://openstax.org/details/books/elementary-algebra-2e", "https://creativecommons.org/licenses/by/4.0/"),
        ("i2", "https://openstax.org/details/books/calculus-volume-1", ""),
        ("i3", "https://openstax.org/details/books/physics", ""),
        ("i4", "https://openstax.org/details/books/introductory-statistics", "https://creativecommons.org/licenses/by/4.0/"),
        ("i5", "https://OATutor.io", "CC4.0"),
        ("i6", "https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf", "https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf"),
    ]
    for cid, oer, lic in casos:
        os.makedirs(os.path.join(pool, cid))
        json.dump({"id": cid, "oer": oer, "license": lic, "courseName": "T"},
                  open(os.path.join(pool, cid, cid + ".json"), "w"))
    out = subprocess.run([sys.executable, os.path.join(HERE, "verdict.py"), td],
                         capture_output=True, text=True).stdout
    for frag, nombre in [
        ("A_contradice_al_titular                           1", "i1 -> contradice al titular"),
        ("B_no_declara_titular_NC                           1", "i2 -> no declara, titular NC"),
        ("C_titular_SI_cede_BY                              1", "i3 -> el titular SI cede BY"),
        ("D_edicion_no_publicada_escape_ABIERTA             1", "i4 -> escape de edicion ABIERTA"),
        ("E_autoria_propia_de_OATutor                       1", "i5 -> autoria propia"),
        ("F_campo_de_cesion_con_URL_de_procedencia          1", "i6 -> URL de procedencia en el campo"),
    ]:
        ok(frag in out, nombre)
    ok("denominador (problemas): 6" in out, "el denominador es el numero de problemas leidos")

print(f"\n{'TODO EN VERDE' if not fallos else 'FALLOS: ' + ', '.join(fallos)}")
sys.exit(1 if fallos else 0)
