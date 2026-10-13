#!/usr/bin/env python3
"""P170-A — gate de region, corregido en DOS puntos por su propio fallo.

`ACTION JF` (registrada por p169 en `intel/open-gaps.md`) pidio enmendar `P383`
para que en un archivo APPEND-ONLY solo se juzgue UN bloque canonico. Al
implementarlo aparecieron dos defectos del instrumento, no de la convencion:

1. **"LAST" es la direccion equivocada.** La convencion de este KB es
   newest-FIRST: cada pase antepone su bloque. El bloque vigente es el PRIMERO
   del archivo, no el ultimo. `ACTION JF` pidio juzgar el ultimo; eso habria
   juzgado el bloque MAS VIEJO y llamado a eso "vigente".

2. **La extension del bloque de `P383` no termina donde termina la lista de
   regiones.** `P383` recoge TODO `###` hasta el siguiente `##`, asi que las
   secciones de hallazgo (`### 🆕 🔴 T203 — ...`) se juzgaban como si fueran
   etiquetas de region. De ahi la mayor parte de `OUT-OF-VOCAB 13`.

Regla de extension que usa este gate: la lista de regiones es la corrida de
`###` que arranca tras el `##` canonico. Un `###` que empieza por marcador de
hallazgo (emoji) o que contiene un backtick TERMINA la corrida y no se juzga.
Cualquier otro `###` de la corrida SI se juzga contra el vocabulario, de modo
que una errata real (`Latam`, `Brazil`, `Europe`) sigue siendo `OUT-OF-VOCAB`.

Hallazgos:
  P170-OUT-OF-VOCAB      un `###` de la lista que no es una de las 5 regiones
  P170-MISSING-REGION    una region del vocabulario ausente del bloque vigente
  P170-LATAM-ONLY        LATAM presente y >=1 de las otras tres ausente
  P170-NO-CANON-BLOCK    el archivo no tiene bloque canonico (solo si --require)
  P170-STALE-BLOCKS      informativo: cuantos bloques historicos hay detras

`P170-STALE-BLOCKS` es INFORMATIVO y no suma al total de defectos: es la
propiedad que `gap 112` confundio con un defecto. Salida TSV. Codigo 1 si hay
defectos reales.
"""
import re
import sys

VOCAB = ["North America", "EMEA", "APAC", "LATAM", "Global"]
CANON = re.compile(r"^## +Opportunities by region\s*$")
H2 = re.compile(r"^## (?!#)")
H3 = re.compile(r"^### (?!#)")
# Un encabezado de HALLAZGO, no de region: marcador emoji al inicio o backtick.
FINDING = re.compile(r"^(?:[\U0001F300-\U0001FAFF←-⇿☀-➿️‍\s]+|.*`)")


def is_finding_heading(text):
    t = text.strip()
    if "`" in t:
        return True
    return bool(re.match(r"^[\U0001F300-\U0001FAFF☀-➿⬀-⯿️]", t))


def canonical_blocks(lines):
    """Todos los indices (0-based) de encabezados canonicos, en orden de archivo."""
    return [i for i, l in enumerate(lines) if CANON.match(l)]


def region_children(lines, start):
    """La corrida de `###` que sigue a `start`, cortada en el primer hallazgo.

    Devuelve (hijos_juzgables, linea_de_corte_o_None).
    """
    kids = []
    j = start + 1
    while j < len(lines) and not H2.match(lines[j]):
        if H3.match(lines[j]):
            text = lines[j][4:].strip()
            if is_finding_heading(text):
                return kids, j + 1
            kids.append((j + 1, text))
        j += 1
    return kids, None


def check(path, lines, require=False):
    found = []
    info = []
    bs = canonical_blocks(lines)
    if not bs:
        if require:
            found.append((path, "P170-NO-CANON-BLOCK", 0, "sin bloque canonico"))
        return found, info
    # newest-FIRST: el bloque vigente es el PRIMERO.
    newest = bs[0]
    if len(bs) > 1:
        info.append((path, "P170-STALE-BLOCKS", bs[1] + 1,
                     f"historicos={len(bs) - 1} (informativo, no es defecto)"))
    kids, cut = region_children(lines, newest)
    names = [t for _, t in kids]
    for kln, t in kids:
        if t not in VOCAB:
            found.append((path, "P170-OUT-OF-VOCAB", kln, t[:80]))
    for r in VOCAB:
        if r not in names:
            found.append((path, "P170-MISSING-REGION", newest + 1, r))
    if "LATAM" in names and any(r not in names for r in ("North America", "EMEA", "APAC")):
        found.append((path, "P170-LATAM-ONLY", newest + 1, "LATAM sin las otras tres"))
    return found, info


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    require = "--require" in argv
    # P541: un gate sin entradas que imprime `total 0` es indistinguible de un
    # arbol limpio habiendo medido CERO archivos. Se rechaza.
    if not args:
        print(
            "P541-NO-INPUT\tREFUSED: este gate mide los archivos que recibe por "
            "argumento y no recibio ninguno. Uso: check_newest_block.py "
            "intel/market.md [...] [--require]",
            file=sys.stderr,
        )
        return 2
    print("archivo\thallazgo\tlinea\tdetalle")
    total = 0
    for p in args:
        rows, info = check(p, open(p, encoding="utf-8").read().split("\n"), require)
        total += len(rows)
        for r in rows + info:
            print("\t".join(str(x) for x in r))
    print(f"#\tdefectos\t{total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
