#!/usr/bin/env python3
"""Suite de p383: cada caso nombra el defecto que atrapa."""
# P115-AK. `python3 -I` (isolated mode) drops the SCRIPT'S OWN DIRECTORY from
# sys.path, so a sibling import fails -- and `-I` is the invocation several of
# this KB's own gate READMEs prescribe ("green under `python3 -I`"). Measured at
# pass 115: all five python gates passed under plain `python3` and ALL FIVE
# failed under `-I`, with a ModuleNotFoundError traceback. A gate that cannot be
# RUN is a gate that passes everything, which is `P471`'s failure wearing a
# different hat. Two lines make the documented invocation true.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import check_headings as m

ok, fail = 0, 0


def t(name, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS {name}")
    else:
        fail += 1
        print(f"FAIL {name}")


GOOD = """## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
""".split("\n")

codes = lambda ls: {r[1] for r in m.check("x.md", ls)}

t("el caso bueno no reporta nada", codes(GOOD) == set())

OUT = """## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
### Brechas declaradas de este pase, por region
""".split("\n")
t("atrapa un ### fuera de vocabulario", "P383-OUT-OF-VOCAB" in codes(OUT))

MISS = """## Opportunities by region

### North America
### EMEA
### Global
""".split("\n")
t("atrapa regiones ausentes", "P383-MISSING-REGION" in codes(MISS))

LAT = """## Opportunities by region

### LATAM
### Global
""".split("\n")
t("atrapa una seccion solo-LATAM", "P383-LATAM-ONLY" in codes(LAT))

TWO = (GOOD + GOOD)
t("atrapa mas de un bloque canonico", "P383-MULTIPLE-BLOCKS" in codes(TWO))

# el defecto real del pase 117: el acento partia el cubo
t("`por region` sin tilde tambien cae fuera de vocabulario",
  "P383-OUT-OF-VOCAB" in codes("""## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
### Oportunidades por region
""".split("\n")))

# un #### NO es hijo sintactico: el remedio del README debe pasar el gate
DEMOTED = """## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
#### Brechas declaradas, por region
""".split("\n")
t("un #### no se cuenta como region (remedio del README)", codes(DEMOTED) == set())

# un bloque archivado con otro nombre no es el canonico
ARCH = """## Oportunidades archivadas — bloque historico

#### North America
""".split("\n")
t("un bloque archivado no se mide como canonico", codes(ARCH) == set())

# ---------------------------------------------------------------------------
# P541 — el control que el pase 43 pago en vivo.
# Sin argumentos el gate imprimia `total 0` y salia 0: indistinguible de un
# arbol limpio habiendo medido CERO archivos (la forma de P471).  Debe RECHAZAR.
t("sin argumentos el gate RECHAZA en vez de aprobar", m.main([]) == 2)

# Control negativo del control: con un archivo real el gate sigue midiendo,
# porque un gate que rechaza SIEMPRE tampoco juzga nada.
import tempfile, os
with tempfile.TemporaryDirectory() as d:
    good = os.path.join(d, "good.md")
    open(good, "w").write("""## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
""")
    t("con un archivo limpio el gate aprueba (exit 0)", m.main([good]) == 0)
    bad = os.path.join(d, "bad.md")
    open(bad, "w").write("""## Opportunities by region

### North America
### EMEA
### APAC
### LATAM
### Global
### Latam
""")
    t("con un archivo sucio el gate falla (exit 1)", m.main([bad]) == 1)

print(f"\n{ok}/{ok+fail} checks passed")
raise SystemExit(1 if fail else 0)
