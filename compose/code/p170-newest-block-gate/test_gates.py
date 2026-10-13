#!/usr/bin/env python3
"""Tests de los dos gates de p170. Sin dependencias: `python3 -I test_gates.py`.

Cada test fija una propiedad que una version ANTERIOR del gate violaba, de modo
que un retroceso falla aqui y no en el arbol.
"""
import os
import sys

# `-I` quita el directorio del script de sys.path, asi que se reinserta a mano.
# Es la forma en que este KB ejecuta sus scripts (entrada no confiable: P355).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import check_action_labels as labels  # noqa: E402
import check_newest_block as nb  # noqa: E402


def t(name, got, want):
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"\n      got={got!r}\n      want={want!r}"))
    return ok


def main():
    r = []

    # --- check_newest_block ---------------------------------------------------
    # newest-FIRST: el bloque vigente es el PRIMERO. ACTION JF pidio el ULTIMO,
    # lo que habria juzgado el bloque mas VIEJO y lo habria llamado vigente.
    doc = [
        "## Opportunities by region",
        "### North America", "### EMEA", "### APAC", "### LATAM", "### Global",
        "## Pass 168",
        "## Opportunities by region",
        "### Latam",            # errata en un bloque HISTORICO: no debe juzgarse
    ]
    found, info = nb.check("f.md", doc)
    r.append(t("newest-first: bloque vigente limpio => 0 defectos", found, []))
    r.append(t("historicos reportados como informativo", [i[1] for i in info], ["P170-STALE-BLOCKS"]))

    # El bloque vigente al que le falta una region SI es defecto (el caso real
    # de p169 en intel/market.md: 4 de 5, sin `Global`).
    doc2 = ["## Opportunities by region",
            "### North America", "### EMEA", "### APAC", "### LATAM"]
    found, _ = nb.check("f.md", doc2)
    r.append(t("falta Global en el bloque vigente => MISSING-REGION",
               [(f[1], f[3]) for f in found], [("P170-MISSING-REGION", "Global")]))

    # Una errata real en el bloque VIGENTE sigue siendo OUT-OF-VOCAB: el corte
    # por encabezado-de-hallazgo no debe tragarse los errores de vocabulario.
    doc3 = ["## Opportunities by region",
            "### North America", "### EMEA", "### APAC", "### Latam", "### Global"]
    found, _ = nb.check("f.md", doc3)
    classes = sorted({f[1] for f in found})
    r.append(t("errata `Latam` en bloque vigente => OUT-OF-VOCAB + MISSING LATAM",
               classes, ["P170-MISSING-REGION", "P170-OUT-OF-VOCAB"]))

    # La extension del bloque TERMINA en el primer encabezado de hallazgo. Era
    # el defecto de P383: barria `### T203 — ...` y lo juzgaba como region.
    doc4 = ["## Opportunities by region",
            "### North America", "### EMEA", "### APAC", "### LATAM", "### Global",
            "### \U0001F534 `T203` — un hallazgo, no una region"]
    found, _ = nb.check("f.md", doc4)
    r.append(t("encabezado de hallazgo no se juzga como region", found, []))

    # --- check_action_labels -------------------------------------------------
    # Una FILA de tabla en una seccion de registro DEFINE.
    reg = "## \U0001F51C Registered for p171\n| `ACTION JJ` | falsificador |\n"
    r.append(t("fila de registro define", labels.definitions("a.md", reg), [("JJ", 2)]))

    # La PROSA en la misma seccion es resumen, no definicion. Era el tercer
    # intento fallido: marcaba las propias acciones de p170 como duplicadas.
    pros = "## \U0001F51C Registered for p171\nResumen: `ACTION JJ` y `ACTION JK`.\n"
    r.append(t("prosa en registro NO define", labels.definitions("b.md", pros), []))

    # Una referencia fuera de toda seccion de registro no define.
    ref = "## Pass 170\n| `ACTION JF` | DISCHARGED |\n"
    r.append(t("fila fuera del registro NO define", labels.definitions("c.md", ref), []))

    print(f"\n{sum(r)}/{len(r)} pasaron")
    return 0 if all(r) else 1


if __name__ == "__main__":
    sys.exit(main())
