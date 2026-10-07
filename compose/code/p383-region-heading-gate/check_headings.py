#!/usr/bin/env python3
"""P383 — gate de ENCABEZADOS: el nivel de encabezado es un contrato de TIPO.

El encargo fija: las oportunidades van bajo UN SOLO `## Opportunities by region`
con UN `###` por region, y `region` es vocabulario CERRADO.

Falla:
  P383-MULTIPLE-BLOCKS   mas de un bloque canonico `## Opportunities by region`
  P383-OUT-OF-VOCAB      un `###` hijo del bloque que no es una de las 5 regiones
  P383-MISSING-REGION    una region del vocabulario ausente del bloque
  P383-LATAM-ONLY        LATAM presente y >=1 de las otras tres ausente
Salida TSV. Codigo 1 si hay hallazgos.
"""
import re
import sys

VOCAB = ["North America", "EMEA", "APAC", "LATAM", "Global"]
CANON = re.compile(r"^## +Opportunities by region\s*$")
H2 = re.compile(r"^## (?!#)")
H3 = re.compile(r"^### (?!#)")


def blocks(lines):
    """Devuelve [(linea_del_encabezado, [(linea, texto_h3), ...]), ...]."""
    out = []
    for i, l in enumerate(lines):
        if not CANON.match(l):
            continue
        kids, j = [], i + 1
        while j < len(lines) and not H2.match(lines[j]):
            if H3.match(lines[j]):
                kids.append((j + 1, lines[j][4:].strip()))
            j += 1
        out.append((i + 1, kids))
    return out


def check(path, lines):
    found = []
    bs = blocks(lines)
    if len(bs) > 1:
        for ln, _ in bs[1:]:
            found.append((path, "P383-MULTIPLE-BLOCKS", ln, f"bloques={len(bs)} (el encargo pide 1)"))
    for ln, kids in bs:
        names = [t for _, t in kids]
        for kln, t in kids:
            if t not in VOCAB:
                found.append((path, "P383-OUT-OF-VOCAB", kln, t[:80]))
        for r in VOCAB:
            if r not in names:
                found.append((path, "P383-MISSING-REGION", ln, r))
        if "LATAM" in names and any(r not in names for r in ("North America", "EMEA", "APAC")):
            found.append((path, "P383-LATAM-ONLY", ln, "LATAM sin las otras tres"))
    return found


def main(argv):
    # P541 (pase 43 del 2026-10-07).  Sin argumentos este gate imprimia
    # `#\ttotal\t0` y salia 0: indistinguible de un arbol limpio, habiendo medido
    # CERO archivos.  Es la forma exacta de P471 -- una compuerta que pasa todas
    # sus comprobaciones sin juzgar nada -- y el pase 43 la cobro en vivo: leyo
    # `total 0` como aprobacion antes de notar que el gate toma rutas por
    # argumento.  Un contrato de uso que hay que recordar no es un control (P237).
    if not argv:
        print(
            "P541-NO-INPUT\tREFUSED: este gate mide los archivos que recibe por "
            "argumento y no recibio ninguno.  `total 0` sin archivos NO es un "
            "arbol limpio.  Uso: check_headings.py intel/market.md [...]",
            file=sys.stderr,
        )
        return 2
    print("archivo\thallazgo\tlinea\tdetalle")
    total = 0
    for p in argv:
        rows = check(p, open(p, encoding="utf-8").read().split("\n"))
        total += len(rows)
        for r in rows:
            print("\t".join(str(x) for x in r))
    print(f"#\ttotal\t{total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
