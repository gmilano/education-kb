#!/usr/bin/env python3
"""Suite de `adjacency.py`. Reproduce: `python3 test_adjacency.py`"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from adjacency import scan

ok = fail = 0


def check(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print("  FAIL %-62s got=%r want=%r" % (label, got, want))


def orphans(lines, window=6):
    """`lines` es una LISTA de lineas (igual contrato que `scan`), no un bloque de texto."""
    if isinstance(lines, str):
        lines = lines.splitlines()
    return [n for n, _ in scan(lines, window)[2]]


# --- la huerfana, en su forma REAL (intel/market.md:239 del pase 94)
t, c, o = scan(["entra en vigor pleno en **agosto de 2026** y clasifica la AI educativa como **alto riesgo**."])
check("huerfana real: se cuenta", t, 1)
check("huerfana real: no acompanada", c, 0)
check("huerfana real: se reporta", len(o), 1)

# --- acompanada: el diferimiento a la vista
t, c, o = scan([
    "El EU AI Act entra en vigor pleno en agosto de 2026 y clasifica la educacion como alto riesgo",
    "(Anexo III; el reloj autonomo que esta base fijo en 2027-12-02 por el Reglamento (UE) 2026/1744).",
])
check("acompanada: cuenta 1", t, 1)
check("acompanada: acompanada", c, 1)
check("acompanada: sin huerfanas", o, [])

# --- la ventana IMPORTA: el mismo par, lejos, es huerfana
far = ["agosto de 2026 ... alto riesgo"] + ["relleno"] * 20 + ["2027-12-02"]
check("ventana: a 21 lineas NO acompana", orphans(far), [1])
check("ventana: ampliada a 25 SI acompana", orphans(far, 25), [])

# --- EXIMENTE: el articulo 50 no fue tocado, su fecha vieja es la CORRECTA
check("art.50: 'articulo 50' exime",
      orphans(["El articulo 50 rige desde agosto de 2026 y la educacion es alto riesgo"]), [])
check("art.50: '50(2)' exime",
      orphans(["El marcado del 50(2) vence en agosto de 2026 para sistemas de alto riesgo"]), [])
check("art.50: 'transparencia' exime",
      orphans(["Las obligaciones de transparencia rigen desde 2026-08-02 para Anexo III"]), [])

# --- NO es afirmacion: la fecha SOLA es correcta (aplicacion general del Reglamento)
check("fecha sola no se cuenta", scan(["El Reglamento se aplica desde agosto de 2026."])[0], 0)
check("deber solo no se cuenta", scan(["La educacion es de alto riesgo en el Anexo III."])[0], 0)

# --- formas de la fecha y del diferimiento que esta base usa de verdad
for form in ["agosto de 2026", "2026-08-02", "2 de agosto de 2026", "August 2, 2026"]:
    check("fecha reconocida: %s" % form,
          scan(["%s ... alto riesgo" % form])[0], 1)
for fix in ["2027-12-02", "2 de diciembre de 2027", "December 2, 2027", "Omnibus", "2026/1744"]:
    check("diferimiento reconocido: %s" % fix,
          orphans(["agosto de 2026 ... alto riesgo", fix]), [])

# --- en ingles, como aparece en trending
check("en: high-risk + August 2, 2026",
      scan(["EMEA: AI Act general application August 2, 2026, high-risk access and assessment"])[0], 1)

# --- el diferimiento ANTES de la linea tambien acompana (la ventana es simetrica)
check("ventana simetrica: el fix arriba acompana",
      orphans(["Reglamento (UE) 2026/1744 corrio el Anexo III", "agosto de 2026 ... alto riesgo"]), [])

print("%d/%d" % (ok, ok + fail))
sys.exit(1 if fail else 0)
