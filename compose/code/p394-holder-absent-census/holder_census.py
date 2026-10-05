#!/usr/bin/env python3
"""P394 — censo del estante: cuantas filas con huella de licencia tienen el titular AUSENTE.

Accion D pre-registrada por el pase 118. `P386` mostro que con titular ausente el par
(sha256, titular) vale 0 bits de procedencia y el deduplicador debe ABSTENERSE. La
accion pregunta si esa compuerta es para un caso raro o para una fraccion medible:

  Hipotesis: las filas con huella y titular ausente son >= 5.
  Refutada si son <= 2  =>  el racimo pristino es marginal y la compuerta es una nota.

Criterio, dicho antes de contar (regla de `P107`: la cifra se publica con su invocacion):
  - Universo = FILAS DE TABLA markdown que llevan una huella (>=12 hex) y hablan de
    una licencia. Una linea de prosa no es una fila.
  - Titular AUSENTE = la fila lleva un marcador explicito de ausencia
    (`NOT-APPLICABLE`, `sin titular`, `titular ausente`). Es la definicion que la
    accion pre-registro, y se cuenta por separado del caso MUDO (fila sin ninguna
    expresion de titular), que es un negativo DEBIL: la ausencia de la palabra no es
    la ausencia del titular (regla de la clase de `P160`).
"""
import re
import sys

HEX12 = re.compile(r"\b[0-9a-f]{12,64}\b")
ABSENT = re.compile(
    r"NOT-APPLICABLE|NOT_APPLICABLE|HOLDER-ABSENT|sin titular|titular\s+\*{0,2}ausente",
    re.I,
)
HOLDER = re.compile(r"titular|Copyright|holder|copyright\s*\(c\)", re.I)
# OJO con los acronimos cortos: sin frontera de palabra, `MIT` casa dentro de
# "com-MIT" y el universo del censo se infla con toda fila que nombre un commit.
# Lo encontro la propia suite de este instrumento (caso
# `sin-mencion-de-licencia-queda-fuera`), y es la razon de los \b de abajo.
LICENSEY = re.compile(
    r"LICENSE|COPYING|licencia|license|Apache|Unlicense|"
    r"\b(MIT|GPL|LGPL|AGPL|BSD|MPL|CC0|CC BY|EPL|Zlib)\b",
    re.I,
)
SEP_ROW = re.compile(r"^[\s:|-]+$")
PRISTINE_BYTES = re.compile(r"\b(11[.,]?357|35[.,]?187|18[.,]?092|7[.,]?651)\b")


def is_row(line):
    s = line.strip()
    if not s.startswith("|") or s.count("|") < 2:
        return False
    return not SEP_ROW.fullmatch(s.strip("|"))


def classify(line):
    """('absent'|'present'|'mute'|None, es_pristina_por_bytes)."""
    if not is_row(line) or not HEX12.search(line) or not LICENSEY.search(line):
        return None, False
    pristine = bool(PRISTINE_BYTES.search(line))
    if ABSENT.search(line):
        return "absent", pristine
    if HOLDER.search(line):
        return "present", pristine
    return "mute", pristine


def census(lines):
    counts = {"absent": 0, "present": 0, "mute": 0}
    pristine_absent = 0
    rows = []
    for path, no, line in lines:
        kind, pristine = classify(line)
        if kind is None:
            continue
        counts[kind] += 1
        if kind == "absent":
            rows.append((path, no, line.strip()[:160]))
            if pristine:
                pristine_absent += 1
    return counts, pristine_absent, rows


def main(argv):
    lines = []
    for p in argv:
        for i, line in enumerate(open(p, encoding="utf-8"), 1):
            lines.append((p, i, line.rstrip("\n")))
    counts, pristine_absent, rows = census(lines)
    total = sum(counts.values())
    print("clase\tfilas")
    for k in ("absent", "present", "mute"):
        print(f"titular-{k}\t{counts[k]}")
    print(f"universo-filas-con-huella-y-licencia\t{total}")
    print(f"titular-ausente-Y-bytes-de-boilerplate-pristino\t{pristine_absent}")
    if total:
        print(f"fraccion-ausente\t{counts['absent'] / total:.3f}")
    clause = "CONFIRMADA" if counts["absent"] >= 5 else (
        "REFUTADA" if counts["absent"] <= 2 else "INDETERMINADA (entre 3 y 4)"
    )
    print(f"#\tclausula-accion-D (>=5 confirma, <=2 refuta)\t{clause}")
    for path, no, text in rows:
        print(f"ausente\t{path}:{no}\t{text}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
