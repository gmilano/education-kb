#!/usr/bin/env python3
"""Suite de `measure.py`. Reproduce: `python3 test_measure.py`"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from measure import measure, load_facts

HERE = os.path.dirname(os.path.abspath(__file__))
ok = fail = 0


def check(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print("  FAIL %-56s got=%r want=%r" % (label, got, want))


F = [("LATAM", "IESALC 200 inst", "IESALC"),
     ("EMEA", "diferimiento", "2027-12-02"),
     ("APAC", "LearnUpon", "LearnUpon")]

# saturacion TOTAL: todo esta en el corpus
t, a, n = measure(F, "... IESALC ... 2027-12-02 ... LearnUpon ...")
check("saturado: total", t, 3)
check("saturado: ya", a, 3)
check("saturado: nuevos", n, [])

# nada esta: los tres son nuevos, y se REPORTAN con su region
t, a, n = measure(F, "corpus sin nada de eso")
check("vacio: ya", a, 0)
check("vacio: nuevos enumerados", n, [("LATAM", "IESALC 200 inst"),
                                      ("EMEA", "diferimiento"),
                                      ("APAC", "LearnUpon")])

# parcial: la fraccion es la que importa
t, a, n = measure(F, "solo IESALC aparece")
check("parcial: ya", a, 1)
check("parcial: nuevos", [r for r, _ in n], ["EMEA", "APAC"])

# el patron es insensible a la CAJA (el corpus mezcla 'IESALC' y 'Iesalc')
check("caja: insensible", measure([("LATAM", "x", "iesalc")], "UNESCO IESALC")[1], 1)

# el patron es una REGEX, no un literal: las variantes de una cifra se declaran en una fila
check("regex: alternancia", measure([("NA", "x", r"2\.303|2303")], "llego a 2303,2 M")[1], 1)
# y un punto literal no matchea cualquier caracter si se escapa
check("regex: punto escapado", measure([("NA", "x", r"2\.303")], "2X303")[1], 0)

# un hecho que NO esta no se puede contar como saturacion: es el error que este modulo evita
check("no inventa saturacion", measure([("APAC", "x", "NIIT")], "nada")[1], 0)

# el TSV real de este pase carga y trae las 4 regiones
rows = load_facts(os.path.join(HERE, "facts.2026-10-04.tsv"))
check("tsv: filas", len(rows), 27)
check("tsv: las 4 regiones", sorted({r for r, _, _ in rows}),
      ["APAC", "EMEA", "LATAM", "North America"])
check("tsv: vocabulario CERRADO (sin 'Latam', 'Europe', paises)",
      all(r in ("North America", "EMEA", "APAC", "LATAM", "Global") for r, _, _ in rows), True)
# la cabecera no es un hecho (P239: una fila de cabecera compilada como dato ya paso en esta base)
check("tsv: la cabecera no entra como fila",
      any(f == "fact" for _, f, _ in rows), False)

print("%d/%d" % (ok, ok + fail))
sys.exit(1 if fail else 0)
