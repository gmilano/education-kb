#!/usr/bin/env python3
"""Detector de citas de patron COLGADAS (accion 2 del pase 61).

Una cita colgada es un **Pn** (o Pn suelto) que ninguna seccion de
compose/patterns.md define. El instrumento existe porque el pase 60 encontro el
defecto a mano y su cifra no reprodujo: hay que poder volver a correrlo.

Convenciones de DEFINICION que patterns.md usa de verdad -- las tres, porque dos
pases distintos escribieron encabezados distintos y un detector que solo conoce
una produce falsos positivos (fue lo que paso: P145-P148 y la receta P149):

  A  "## P142 - titulo"              seccion propia de nivel 2
  B  "### P146 - titulo"             subseccion dentro de un encabezado de grupo
  C  "## P145-P148, los patrones..." encabezado de RANGO (define los cuatro)
  D  "## Receta P149 - ..."          receta: otro namespace, NO es patron
  E  "### `P348` - titulo"           el numero en CODIGO INLINE (backticks)

`P354`: la convencion E es la que patterns.md usa desde el pase ~95 y este detector
era CIEGO a ella -- 42 numeros (284-287, 308-319, 328-353) estaban definidos con
backticks y salian COLGADOS. Es el mismo defecto que su propio docstring documenta
haber tenido con P145-P148: apareció una tercera forma de escribir el encabezado y
el detector solo conocia dos. La familia es la de P171/P288/P299/P304: el ancla
reconoce una ORTOGRAFIA y no el OBJETO.

Uso:  python3 audit_patterns.py [raiz-del-kb]
Salida: TSV por numero + resumen. Codigo 1 si hay colgadas.
"""
import re, sys, glob, os, collections

DEF_A_B = re.compile(r'^#{2,4}\s*(?:[^\w\n]*\s)?[`*]{0,3}P(\d+)[`*]{0,3}\s*(?:[—–-]|,)', re.M)
DEF_RANGE = re.compile(r'^#{2,4}\s*(?:[^\w\n]*\s)?[`*]{0,3}P(\d+)[`*]{0,3}\s*[—–-]\s*[`*]{0,3}P(\d+)', re.M)
DEF_RECIPE = re.compile(r'^#{2,4}\s*(?:[^\w\n]*\s)?Receta\s+P(\d+)', re.M | re.I)
CITE_BOLD = re.compile(r'\*\*P(\d+)\*\*')
CITE_ANY = re.compile(r'\bP(\d+)\b')


def definitions(patterns_md):
    """Numeros definidos, por convencion, para poder nombrar cual los cubre."""
    with open(patterns_md, encoding='utf-8') as fh:
        text = fh.read()
    by = {}
    for m in DEF_A_B.finditer(text):
        by.setdefault(int(m.group(1)), 'A/B-seccion')
    for m in DEF_RANGE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        if 0 < hi - lo < 50:
            for n in range(lo, hi + 1):
                by.setdefault(n, 'C-rango')
    for m in DEF_RECIPE.finditer(text):
        by.setdefault(int(m.group(1)), 'D-receta')
    return by


# El propio directorio del detector queda FUERA del barrido: documenta sus casos
# de prueba con numeros de ejemplo (P900, P999) que no son citas de la KB. Un
# detector que se lee a si mismo se cuenta sus propios ejemplos como defectos.
SELF_DIR = os.path.join('compose', 'code', 'pattern-citation-audit')


def citations(root):
    bold, any_, where = collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    for f in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(f, root)
        if rel.startswith(SELF_DIR):
            continue
        with open(f, encoding='utf-8') as fh:
            text = fh.read()
        for m in CITE_BOLD.finditer(text):
            bold[int(m.group(1))] += 1
        for m in CITE_ANY.finditer(text):
            n = int(m.group(1))
            any_[n] += 1
            where[n][rel] += 1
    return bold, any_, where


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    patterns_md = os.path.join(root, 'compose', 'patterns.md')
    if not os.path.exists(patterns_md):
        print('no existe %s' % patterns_md, file=sys.stderr)
        return 2
    defs = definitions(patterns_md)
    bold, any_, where = citations(root)
    dangling = sorted(n for n in any_ if n not in defs)

    print('# definidos\t%d\tconvenciones\t%s' % (
        len(defs), dict(collections.Counter(defs.values()))))
    print('numero\tcitas_bold\tcitas_any\tarchivos')
    tb = ta = 0
    for n in dangling:
        tb += bold[n]; ta += any_[n]
        print('P%d\t%d\t%d\t%s' % (n, bold[n], any_[n],
                                   ','.join('%s:%d' % (f, c) for f, c in sorted(where[n].items()))))
    print('# COLGADAS\t%d numeros\t%d citas_bold\t%d citas_any' % (len(dangling), tb, ta))

    # controles: sin ellos la cifra no es citable (P107/P119)
    ok = [n for n in (142, 145, 148, 149, 131, 136) if n in defs]
    print('# control_positivo_definidos\t%s' % ','.join('P%d(%s)' % (n, defs[n]) for n in ok))
    print('# control_negativo_P999_citas\t%d' % any_[999])
    return 1 if dangling else 0


if __name__ == '__main__':
    sys.exit(main())
