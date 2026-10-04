#!/usr/bin/env python3
"""P265 — barrido DIFERENCIAL de la pregunta de region: una matriz, cuatro implementaciones.

Pase 89 del 2026-10-04. **P263** (pase 88) dejo escrito que la pregunta de region tenia que
mudarse a `compose/code/lib/`. Este instrumento mide, antes de mudarla, QUE responden hoy
las implementaciones que ya estan en el arbol — porque si no coinciden, mudar «la» pregunta
a una sola funcion rompe a alguna.

Las implementaciones se invocan por su SUPERFICIE PUBLICA, no reimplementadas:

| Columna | Implementacion | Pregunta que hace |
|---|---|---|
| `p243`  | `check_frontmatter.findings_for()`, codigo `REGION-NOT-IN-VOCABULARY` | VALIDADOR (portador frontmatter) |
| `p262`  | `mandate.region_ok({"region": v})`                                    | VALIDADOR (portador dato)        |
| `lib`   | `lib.region.region_ok(v)`                                             | VALIDADOR (portador dato)        |
| `libf`  | `lib.region.region_ok_frontmatter(v)`                                 | VALIDADOR (portador frontmatter) |
| `p239`  | `check_tables.regions_in_cell(v)` — su DEFAULT, que es `strict=True`  | DETECTOR                         |
| `p239l` | idem con `strict=False`                                               | DETECTOR lenient                 |
| `libd`  | `lib.region.regions_named(v)` — su default, `strict=True`             | DETECTOR                         |

`ACEPTA` = el valor pasa como region. Para los detectores, `ACEPTA` = el conjunto no es vacio.

Uso:
    python3 measure.py           # tabla legible
    python3 measure.py --tsv     # TSV para diffear entre pases
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
for sub in ("lib", "p243-frontmatter-coverage", "p262-mandate-level",
            "p239-table-integrity"):
    sys.path.insert(0, os.path.join(CODE, sub))

import region as libregion                       # noqa: E402
import check_frontmatter as p243                 # noqa: E402
import check_tables as p239                      # noqa: E402
import mandate as p262                           # noqa: E402

#: La matriz. Cada fila es (valor, clase). Las clases son del vocabulario de este eje:
#:   EXACTO    - uno de los cinco, byte a byte
#:   P248      - un exacto con blanco pegado: se renderiza igual, se bucketea aparte
#:   CASO      - un exacto con otra capitalizacion
#:   ADORNO    - un exacto dentro de markup publicado (negrita, backtick, emoji, parentesis)
#:   MULTIPLE  - la celda nombra dos o mas
#:   RESIDUO   - la celda nombra una region PERO trae algo mas (cifras, perfil)
#:   BALDE     - una variante que NO es del vocabulario y abre balde nuevo
#:   AUSENTE   - vacio
MATRIX = [
    ("North America", "EXACTO"), ("EMEA", "EXACTO"), ("APAC", "EXACTO"),
    ("LATAM", "EXACTO"), ("Global", "EXACTO"),
    ("APAC ", "P248"), (" APAC", "P248"), ("LATAM ", "P248"), ("Global ", "P248"),
    ("apac", "CASO"), ("latam", "CASO"), ("emea", "CASO"), ("GLOBAL", "CASO"),
    ("Latam", "CASO"),
    ("**LATAM**", "ADORNO"), ("🔴 **LATAM**", "ADORNO"), ("`EMEA`", "ADORNO"),
    ("APAC (Vietnam)", "ADORNO"), ("North  America", "ADORNO"),
    ("APAC / LATAM", "MULTIPLE"), ("EMEA, APAC, LATAM", "MULTIPLE"),
    ("EMEA y LATAM", "MULTIPLE"),
    ("86 % NA / 92 % LATAM", "RESIDUO"),
    ("Ministerio, APAC / LATAM / Africa", "RESIDUO"),
    ("Europe", "BALDE"), ("Asia Pacific", "BALDE"), ("Asia-Pacific", "BALDE"),
    ("Brazil", "BALDE"), ("Brasil", "BALDE"), ("North-America", "BALDE"),
    ("NA", "BALDE"), ("Africa", "BALDE"), ("MENA", "BALDE"),
    ("", "AUSENTE"),
]

COLS = ("p243", "p262", "lib", "libf", "p239", "p239l", "libd")
#: Los validadores del portador DATO. `p243`/`libf` quedan fuera a proposito: su portador
#: es YAML y ahi el blanco de la izquierda es sintaxis, no dato (P265).
VALIDATORS = ("p262", "lib")
DETECTORS = ("p239", "libd")
#: Los dos validadores que esta base tenia en el arbol ANTES de este pase, y que P265 fue
#: a comparar. Discrepan, y la medicion muestra en que clase.
LEGACY_VALIDATORS = ("p243", "p262")


def via_p243(value):
    """El validador de p243 tal como se usa: un frontmatter sintetico y su hallazgo."""
    text = (f"---\nindustry: education\nregion: {value}\nupdated: 2026-10-04\n---\n")
    codes = {c for c, _ in p243.findings_for("sintetico.md", text)}
    return "REGION-NOT-IN-VOCABULARY" not in codes and "MISSING-KEY" not in codes


def verdicts(value):
    return {
        "p243": via_p243(value),
        "p262": p262.region_ok({"region": value}),
        "lib": libregion.region_ok(value),
        "libf": libregion.region_ok_frontmatter(value),
        "p239": bool(p239.regions_in_cell(value)),
        "p239l": bool(p239.regions_in_cell(value, strict=False)),
        "libd": bool(libregion.regions_named(value)),
    }


def sweep():
    """Rinde (valor, clase, veredictos, legacy_discrepan, val_vs_det).

    `legacy_discrepan` = los dos validadores que ya estaban en el arbol dan veredictos
    distintos sobre el MISMO valor. `val_vs_det` = validador y detector dan veredictos
    opuestos, que es el contrato y no un defecto.
    """
    out = []
    for value, klass in MATRIX:
        v = verdicts(value)
        legacy = len({v[c] for c in LEGACY_VALIDATORS}) > 1
        val = {v[c] for c in VALIDATORS}
        det = {v[c] for c in DETECTORS}
        out.append((value, klass, v, legacy,
                    len(val) == 1 and len(det) == 1 and val != det))
    return out


def main(argv):
    rows = sweep()
    tsv = "--tsv" in argv
    head = ("valor", "clase") + COLS + ("legacy_discrepan", "val_vs_det")
    if tsv:
        print("\t".join(head))
    else:
        print(f"{'valor':36} {'clase':9} " + " ".join(f"{c:6}" for c in COLS)
              + "  LD V/D")
    n_vd = n_vdet = 0
    for value, klass, v, vd, vdet in rows:
        n_vd += vd
        n_vdet += vdet
        cells = ["ACEPTA" if v[c] else "RECHAZA" for c in COLS]
        if tsv:
            print("\t".join([repr(value), klass] + cells
                            + [str(vd), str(vdet)]))
        else:
            print(f"{value!r:36} {klass:9} "
                  + " ".join(f"{'SI' if v[c] else 'no':6}" for c in COLS)
                  + f"  {'SI' if vd else ' .'} {'SI' if vdet else ' .'}")
    print()
    print(f"{len(rows)} valores medidos")
    print(f"{n_vd} valores donde los DOS validadores preexistentes (p243, p262) discrepan")
    print(f"{n_vdet} valores donde VALIDADORES y DETECTORES dan veredicto opuesto")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
