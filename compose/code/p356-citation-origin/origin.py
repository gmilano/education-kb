#!/usr/bin/env python3
"""`P356` — las 21 citas colgadas de `P354`, repartidas por ORIGEN.

La accion D pre-registrada por el pase 111 pedia, para cada una de las 21 colgadas,
buscar la PRIMERA aparicion y decidir si el numero fue **anunciado y nunca escrito**
(la clase de `P295`/`P297`) o si es un **error de numeracion**. Predijo que >=14 serian
de la primera clase.

El reparto no cabe en esas dos clases, y el motivo es del INSTRUMENTO que produjo las 21:
`audit_patterns.definitions()` lee **un solo archivo** (`compose/patterns.md`), mientras
`audit_patterns.citations()` barre **todos** los `**/*.md` del arbol. La asimetria FABRICA
colgadas: un numero definido con la misma convencion de encabezado, pero en otro archivo,
sale colgado sin que nada lo marque.

Este modulo no afloja el ancla: reusa las MISMAS regex del auditor (`P237` — consumir la
libreria compartida en vez de traer un clasificador propio) y solo cambia el DENOMINADOR
de archivos sobre el que las aplica.

Uso:  python3 origin.py [raiz-del-kb]
"""
import importlib.util, os, re, sys, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
AUD = os.path.join(HERE, '..', 'pattern-citation-audit', 'audit_patterns.py')


def _auditor():
    spec = importlib.util.spec_from_file_location('audit_patterns', AUD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A = _auditor()
SELF_DIRS = (os.path.join('compose', 'code', 'pattern-citation-audit'),
             os.path.join('compose', 'code', 'p356-citation-origin'))


def defs_in(text):
    """Los numeros que ESTE texto define, por las tres convenciones del auditor."""
    out = {}
    for m in A.DEF_A_B.finditer(text):
        out.setdefault(int(m.group(1)), 'A/B-seccion')
    for m in A.DEF_RANGE.finditer(text):
        lo, hi = int(m.group(1)), int(m.group(2))
        if 0 < hi - lo < 50:
            for n in range(lo, hi + 1):
                out.setdefault(n, 'C-rango')
    for m in A.DEF_RECIPE.finditer(text):
        out.setdefault(int(m.group(1)), 'D-receta')
    return out


def scan(root):
    """(definiciones por numero -> [(archivo, convencion)], texto por archivo)."""
    where = collections.defaultdict(list)
    texts = {}
    for f in sorted(glob.glob(os.path.join(root, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(f, root)
        if any(rel.startswith(d) for d in SELF_DIRS):
            continue
        with open(f, encoding='utf-8') as fh:
            text = fh.read()
        texts[rel] = text
        for n, conv in defs_in(text).items():
            where[n].append((rel, conv))
    return where, texts


def classify(n, where, root):
    """Clase de ORIGEN de una cita colgada.

    DEFINIDA-FUERA  el numero SI tiene seccion con la convencion del auditor, en otro
                    archivo del arbol: no es deuda doctrinal, es alcance del instrumento.
    INSTRUMENTO     existe `compose/code/p<n>-*/` — el numero tiene codigo y README propios.
    ANUNCIADA       ninguna de las dos: candidata a `P295`/`P297`.
    """
    out = []
    if n in where:
        out.append('DEFINIDA-FUERA')
    if glob.glob(os.path.join(root, 'compose', 'code', 'p%d-*' % n)):
        out.append('INSTRUMENTO')
    return out or ['ANUNCIADA']


COLGADAS = [127, 128, 129, 130, 132, 133, 134, 135, 173, 174, 175,
            239, 240, 245, 252, 279, 280, 281, 282, 283, 293]


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', '..')
    root = os.path.abspath(root)
    where, _ = scan(root)
    pat = os.path.join(root, 'compose', 'patterns.md')
    in_patterns = set(A.definitions(pat))

    tally = collections.Counter()
    print('numero\tclases\tdonde_definido')
    for n in COLGADAS:
        assert n not in in_patterns, 'P%d NO es colgada: patterns.md la define' % n
        cls = classify(n, where, root)
        tally['+'.join(cls)] += 1
        loc = ';'.join('%s(%s)' % (f, c) for f, c in where.get(n, [])) or '-'
        print('P%d\t%s\t%s' % (n, '+'.join(cls), loc))

    print()
    print('# 21 colgadas de P354, por ORIGEN')
    for k, v in sorted(tally.items(), key=lambda kv: -kv[1]):
        print('#   %-28s %d' % (k, v))
    anunciadas = tally['ANUNCIADA']
    print('# ANUNCIADA (la clase que la accion D predijo >=14): %d' % anunciadas)
    veredicto = ('CONFIRMADA' if anunciadas >= 14 else
                 'REFUTADA' if anunciadas <= 7 else 'NI-UNA-NI-OTRA')
    print('# veredicto accion D: %s' % veredicto)

    # El defecto de ALCANCE, medido: numeros definidos fuera de patterns.md.
    fuera = {n for n in where if n not in in_patterns}
    print('# numeros con seccion FUERA de patterns.md (invisibles al auditor): %d' % len(fuera))
    print('# de ellos, dentro de las 21 colgadas: %d' % len(fuera & set(COLGADAS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
