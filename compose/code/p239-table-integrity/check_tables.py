#!/usr/bin/env python3
"""P239/P240 — linter de integridad de tablas Markdown para esta KB.

Mide dos defectos que el pase 78 encontró en el archivo publicado y que ningún
pase anterior medía:

  P239  Una fila de datos cuyo bloque de pipes NO tiene fila separadora
        (`|---|`) arriba. Causa típica: un comentario HTML o un párrafo
        intercalado PARTE la tabla en dos; el segundo trozo queda sin encabezado
        y el compilador lee su PRIMERA FILA DE DATOS como encabezado — es decir,
        entidades con nombre de dato y una fila real perdida.

  P240  Una tabla con columna de región a la que le FALTA una de las cinco
        regiones del vocabulario cerrado. Un barrido regional que publica tres
        de cuatro regiones no se distingue, leído desde afuera, de uno que midió
        cuatro y encontró tres.

Salida: TSV por hallazgo. Código de salida 1 si hay hallazgos, 0 si está limpio.
Uso:  python3 check_tables.py ARCHIVO.md [ARCHIVO.md ...]
"""
import re
import sys

REGIONS = ("North America", "EMEA", "APAC", "LATAM", "Global")
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def is_sep(line):
    """Fila separadora de tabla Markdown: sólo pipes, guiones, dos puntos."""
    s = line.strip()
    return bool(SEP_RE.match(s)) and "-" in s


def iter_rows(lines):
    """Rinde (indice, texto) de las filas de pipe FUERA de bloques de código.

    Las tuberías de shell dentro de ``` ``` empiezan con '|' y no son tablas;
    contarlas fue el falso positivo que este instrumento tuvo que corregir
    antes de publicarse.
    """
    fence = False
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if l.strip().startswith("|"):
            yield i, l


def find_orphans(lines):
    """P239 — filas cuyo bloque de pipes no tiene separadora."""
        
    rows = dict(iter_rows(lines))
    out = []
    for i, l in rows.items():
        if is_sep(l):
            continue
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if is_sep(nxt):          # es encabezado legítimo
            continue
        j, ok = i - 1, False
        while j in rows:         # subir sólo dentro del bloque contiguo
            if is_sep(rows[j]):
                ok = True
                break
            j -= 1
        if not ok:
            out.append((i + 1, l.strip()))
    return out


NORM_DROP = re.compile(r"[^A-Za-z ]")          # emoji, **, backticks, numeros
PAREN = re.compile(r"\s*\([^)]*\)")             # "APAC (Vietnam)" -> "APAC"
SCOPE = re.compile(r"<!--\s*p240-scope:\s*([^>]*?)\s*-->", re.I)


def regions_in_cell(cell, strict=True):
    """Regiones nombradas en UNA celda, normalizando lo que v1 no normalizaba.

    Los tres falsos positivos de la v1 de este instrumento, medidos sobre el
    archivo publicado y corregidos antes de publicarlo:
      - `| 🔴 **LATAM** |`      el emoji impedia el match exacto
      - `| APAC (Vietnam) |`    el calificativo entre parentesis lo impedia
      - `| **APAC / LATAM** |`  una celda puede nombrar DOS regiones
    """
    c = PAREN.sub("", cell)
    out, residue = set(), False
    for part in re.split(r"[/,]| y ", c):
        t = NORM_DROP.sub(" ", part)
        t = re.sub(r"\s+", " ", t).strip()
        if not t:
            continue
        hit = next((r for r in REGIONS if t.casefold() == r.casefold()), None)
        if hit:
            out.add(hit)
        else:
            residue = True
    # En modo estricto la celda cuenta como celda de REGION solo si no queda
    # nada mas que regiones. Es el arreglo de la v3: la v2 leia como region
    # cualquier celda que CONTUVIERA el nombre de una, y reclamaba tablas cuya
    # primera columna no es regional —`86 % NA / 92 % LATAM / 66 % APAC` es una
    # celda de CIFRAS, y `Ministerio..., APAC / LATAM / Africa` es una de
    # PERFIL DE CLIENTE—. Cuatro falsos positivos, todos de esta causa.
    if strict and residue:
        return set()
    return out


def find_region_gaps(lines):
    """P240 — tablas cuya primera columna es de region y le falta alguna.

    Una tabla puede ser legitimamente parcial (p. ej. «las dos regiones que
    legislan sobre la nota»). Para esos casos se declara el alcance con un
    marcador en la linea de arriba:  <!-- p240-scope: North America, EMEA -->
    Sin marcador, la tabla se reclama: el objetivo del eje es que una tabla
    regional incompleta NO pase por completa.
    """
    rows = sorted(dict(iter_rows(lines)))
    out, block = [], []
    for i in rows + [-1]:
        if block and (i == -1 or i != block[-1] + 1):
            present = set()
            for k in block:
                if is_sep(lines[k]):
                    continue
                parts = lines[k].split("|")
                if len(parts) > 1:
                    present |= regions_in_cell(parts[1])
            if len(present) >= 2:
                # alcance declarado en las 3 lineas previas al bloque
                declared = None
                for k in range(max(0, block[0] - 3), block[0] + 1):
                    m = SCOPE.search(lines[k])
                    if m:
                        declared = regions_in_cell(m.group(1))
                expected = declared if declared else {
                    r for r in REGIONS if r != "Global"}
                missing = [r for r in REGIONS if r in expected and r not in present]
                if missing:
                    out.append((block[0] + 1, sorted(present), missing))
            block = []
        if i != -1:
            block.append(i)
    return out


def main(paths):
    n = 0
    print("archivo\thallazgo\tlinea\tdetalle")
    for p in paths:
        lines = open(p, encoding="utf-8").read().split("\n")
        for ln, txt in find_orphans(lines):
            n += 1
            print(f"{p}\tP239-ORPHAN-ROW\t{ln}\t{txt[:90]}")
        for ln, present, missing in find_region_gaps(lines):
            n += 1
            print(f"{p}\tP240-REGION-GAP\t{ln}\tpresentes={'+'.join(present)} FALTA={'+'.join(missing)}")
    print(f"#\ttotal\t{n}", file=sys.stderr)
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["-"]))
