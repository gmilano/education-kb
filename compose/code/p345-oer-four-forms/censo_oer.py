#!/usr/bin/env python3
"""Accion C del pase 110 — el censo COMPLETO de formas de `oer`, en lotes.

`P337`: dos artefactos del pase 108, sobre el MISMO sha, se contradicen por 41
figuras en el corte openstax/no-openstax (1.611/832 contra 1.570/873, los dos
suman 2.443). `P338`: `oer` es TEXTO LIBRE y al ampliar la muestra aparecieron
CUATRO formas de URL, dos invisibles para el patron inicial.

Este modulo no afirma formas: las ENUMERA del corpus y deja el reparto medido.
"""
import json, os, re, sys, collections

DEFAULT_ROOT = '/tmp/oat-full'


def unidades(root=DEFAULT_ROOT):
    """Unidad = el JSON de problema de primer nivel: content-pool/<id>/<id>.json"""
    pool = os.path.join(root, 'content-pool')
    out = []
    for d in sorted(os.listdir(pool)):
        p = os.path.join(pool, d, d + '.json')
        if os.path.isfile(p):
            out.append((d, p))
    return out


# Las cuatro formas se NOMBRAN por su estructura, no por el libro.
FORMAS = [
    ('details-books', re.compile(r'openstax\.org/details/books/', re.I)),
    ('books-pages',   re.compile(r'openstax\.org/books/[^/]+/pages/', re.I)),
    ('books-sinpage', re.compile(r'openstax\.org/books/(?!.*?/pages/)', re.I)),
    ('openstax-otro', re.compile(r'openstax\.org', re.I)),
]


def forma_de(oer):
    o = (oer or '').strip()
    if not o:
        return 'VACIO'
    for nombre, rx in FORMAS:
        if rx.search(o):
            return nombre
    return 'NO-OPENSTAX'


def main(root, out_dir, lote):
    us = unidades(root)
    os.makedirs(out_dir, exist_ok=True)
    rows, bad = [], 0
    for i in range(0, len(us), lote):
        part = os.path.join(out_dir, 'lote-%03d.tsv' % (i // lote + 1))
        lote_rows = []
        for pid, path in us[i:i + lote]:
            try:
                with open(path, encoding='utf-8') as fh:
                    o = json.load(fh)
            except Exception as e:
                bad += 1
                lote_rows.append((pid, '', '', '', 'JSON-INVALIDO'))
                continue
            lote_rows.append((pid, o.get('oer', '') or '', o.get('license', '') or '',
                              o.get('courseName', '') or '', forma_de(o.get('oer'))))
        with open(part, 'w', encoding='utf-8') as fh:   # parcial GUARDADO: acumulable
            for r in lote_rows:
                fh.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for r2 in [r] for x in r2) + '\n')
        rows += lote_rows
        print('lote %d -> %d filas (acumulado %d/%d)' % (i // lote + 1, len(lote_rows), len(rows), len(us)),
              file=sys.stderr)

    with open(os.path.join(out_dir, 'unidades-oer.tsv'), 'w', encoding='utf-8') as fh:
        fh.write('problem_id\toer\tlicense\tcourseName\tforma\n')
        for r in rows:
            fh.write('\t'.join(r) + '\n')

    c = collections.Counter(r[4] for r in rows)
    print('\n=== CENSO DE FORMAS (unidades=%d, json invalidos=%d) ===' % (len(rows), bad))
    for k, v in c.most_common():
        print('%-16s %6d' % (k, v))
    return rows


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ROOT,
         sys.argv[2] if len(sys.argv) > 2 else '.',
         int(sys.argv[3]) if len(sys.argv) > 3 else 2000)
