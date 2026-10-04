#!/usr/bin/env python3
"""P267 — el vocabulario cerrado se aplica en UN portador y no en el otro: cuanto cuesta.

`p243` reclama una variante de region en el FRONTMATTER (`region: Latam` -> hallazgo). Pero
la misma variante en una CELDA de tabla la normaliza el detector de `p239` y **no se reporta
nunca**, porque el detector tiene que ser lenient para medir prosa publicada.

Este barrido mide el hueco sobre el arbol REAL: recorre los `.md` publicados, toma la primera
columna de cada fila de pipe —la misma celda que `p239` lee para decidir cobertura regional— y
reporta las grafias que el detector normalizo hasta hacerlas coincidir.

🔴 **Con una compuerta que la primera version no tenia:** solo se miran las celdas que `p239`
CUENTA como celdas de region (su veredicto `strict`). Sin esa compuerta el barrido devolvio 8
hallazgos y **los 8 eran falsos positivos** —celdas de cifras y de prosa— que es exactamente la
clase que el modo strict existe para descartar. El control negativo esta archivado en
`ungated.NEGATIVE-CONTROL-2026-10-04.tsv`.

Uso:
    python3 measure_variants.py            # tabla legible
    python3 measure_variants.py --tsv
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(CODE, "lib"))
sys.path.insert(0, os.path.join(CODE, "p239-table-integrity"))

import check_tables as p239      # noqa: E402
from region import variants_in   # noqa: E402


def repo_root():
    d = HERE
    while d != "/":
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        d = os.path.dirname(d)
    return HERE


def markdown_files(root):
    """Los `.md` del arbol, SIN los fixtures.

    `fixtures/` queda fuera porque ahi la variante esta PLANTADA: contarla haria que el
    instrumento reporte su propia entrada de prueba y el cero del arbol real dejaria de
    ser legible. El barrido sobre el fixture se corre aparte, y es el control positivo de
    `test_measure.py`.
    """
    out = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".git", "fixtures")]
        out += [os.path.join(base, f) for f in files if f.endswith(".md")]
    return sorted(out)


def sweep(root):
    """Rinde (rel, linea, grafia, region_normalizada, clase)."""
    rows = []
    for path in markdown_files(root):
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        rel = os.path.relpath(path, root)
        for i, text in p239.iter_rows(lines):
            if p239.is_sep(text):
                continue
            parts = text.split("|")
            if len(parts) < 2:
                continue
            # 🔴 LA COMPUERTA, y es la leccion del pase: sin ella este barrido devolvio
            # 8 hallazgos y los 8 eran FALSOS POSITIVOS de la clase exacta que el modo
            # strict de `p239` existe para descartar —celdas de CIFRAS (`92 % LATAM`,
            # `**APAC $591,6M`) y de PROSA donde `global` es adjetivo (`Uso de AI por
            # estudiantes, global`)—. Queda archivado en
            # `ungated.NEGATIVE-CONTROL-2026-10-04.tsv`.
            # La poblacion correcta no es «toda celda», es «las celdas que p239 CUENTA
            # como celdas de region», o sea su veredicto strict.
            counted = p239.regions_in_cell(parts[1])
            if not counted:
                continue
            for grafia, region, klass in sorted(variants_in(parts[1])):
                if region not in counted:
                    continue
                rows.append((rel, i + 1, grafia, region, klass))
    return rows


def main(argv):
    root = repo_root()
    rows = sweep(root)
    tsv = "--tsv" in argv
    act = [r for r in rows if r[4] != "MARKUP"]
    if tsv:
        print("archivo\tlinea\tgrafia\tregion\tclase")
    for rel, ln, grafia, region, klass in (rows if tsv else act):
        if tsv:
            print(f"{rel}\t{ln}\t{grafia}\t{region}\t{klass}")
        else:
            print(f"{rel}:{ln}  {grafia!r} -> {region}  [{klass}]")
    print()
    print(f"{len(markdown_files(root))} archivos .md recorridos")
    print(f"{len(rows)} celdas que el detector normaliza en silencio, de las cuales:")
    for k in ("MARKUP", "CASO", "SEPARADOR"):
        n = len([r for r in rows if r[4] == k])
        tag = "formato, NO accionable" if k == "MARKUP" else "variante real, ACCIONABLE"
        print(f"  {n:4} {k:10} ({tag})")
    print(f"{len(act)} hallazgos ACCIONABLES, en "
          f"{len({r[0] for r in act})} archivos y {len({r[2] for r in act})} grafias distintas")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
