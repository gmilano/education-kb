#!/usr/bin/env python3
"""Suite de p383: cada caso nombra el defecto que atrapa."""
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

print(f"\n{ok}/{ok+fail} checks passed")
raise SystemExit(1 if fail else 0)
