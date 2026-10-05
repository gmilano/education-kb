#!/usr/bin/env python3
"""Controles OFFLINE de P322.  `python3 test_classify.py`"""
import sys
from classify_item import classify

CASES = [
    # (nombre, item, clase esperada, por que existe el control)
    ("C1 CC BY 4.0 canonica",
     {"license": "https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>",
      "oer": "https://openstax.org/books/precalculus/pages/1-4"},
     "CC-BY-4.0",
     "el positivo conocido: si no lo reproduce, ningun negativo suyo vale"),

    ("C2 license VACIA",
     {"license": "", "oer": "https://openstax.org/x"},
     "VACIA",
     "D1 — vacio NO hereda el README; es ausencia de cesion por item"),

    ("C3 URL que no es licencia",
     {"license": "https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf",
      "oer": "https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf"},
     "URL-NO-LICENCIA",
     "D2+D3 — el caso peor: parece lleno y no cede nada; y delata que se copio `oer`"),

    ("C4 sin campo license",
     {"oer": "https://openstax.org/x"},
     "AUSENTE",
     "ausencia de campo != campo vacio: son dos estados distintos y se cuentan aparte"),

    ("C5 CC BY-NC-SA no se lee como CC BY",
     {"license": "https://creativecommons.org/licenses/by-nc-sa/4.0/"},
     "OTRA-CC",
     "P312 — la compuerta se abria sobre las familias que existe para atrapar"),

    ("C6 CC BY 3.0 no es CC BY 4.0",
     {"license": "https://creativecommons.org/licenses/by/3.0/"},
     "OTRA-CC",
     "la VERSION es parte de la cesion; colapsarlas borra una diferencia real"),

    ("C7 nombre sin URL",
     {"license": "CC BY 4.0"},
     "NOMBRADA-SIN-URL",
     "una cesion nombrada y no enlazada es valida y mas debil: no se mezcla con C1"),

    ("C8 license=null",
     {"license": None},
     "AUSENTE",
     "null es ausencia, no el string 'None'"),

    ("C9 el nombre de archivo NO es el dato",
     {"license": "", "oer": "", "id": "a95836f13.1driverslicense"},
     "VACIA",
     "D4 — 'driverslicense' en el id contiene 'license' y no cede nada. "
     "El barrido de RUTAS de este pase devolvio 8 falsos positivos por esto"),

    ("C10 URL de licencia no-CC se reconoce",
     {"license": "https://opensource.org/licenses/MIT"},
     "URL-NO-LICENCIA",
     "declarado: este modulo clasifica CC por URL; una URL OSI cae en revision manual "
     "y NO se promueve a cesion CC en silencio"),
]

def main():
    ok = fail = 0
    for name, item, want, why in CASES:
        got, detail = classify(item)
        if got == want:
            ok += 1
            print(f"  ok   {name}: {got} ({detail})" if detail else f"  ok   {name}: {got}")
        else:
            fail += 1
            print(f"  FAIL {name}: esperado {want}, dio {got} ({detail})")
            print(f"       razon del control: {why}")
    print(f"\n{ok}/{ok+fail}")
    return 1 if fail else 0

if __name__ == '__main__':
    sys.exit(main())
