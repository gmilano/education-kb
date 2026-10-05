#!/usr/bin/env python3
"""La pregunta que decide un presupuesto, y no es el corte openstax/no-openstax.

`P337` se discutio tres pases como «1.611 o 1.570». Este modulo mide el campo
`license` de las 2.443 figuras y clasifica por lo que una entrega COMERCIAL
necesita: una cesion RESOLUBLE. Cuatro cubetas, y la diferencia entre ellas es
dinero:

  RESOLUBLE        un identificador de licencia que nombra variante y version
  VERSION-SIN-VARIANTE  «CC4.0»: la version 4.0 son SEIS licencias distintas
                   (BY, BY-SA, BY-NC, BY-NC-SA, BY-ND, BY-NC-ND), TRES de ellas
                   NonCommercial. Nombrar la version no nombra la cesion.
  NO-ES-CESION     el campo trae una URL de FUENTE (un PDF de examen), no una
                   licencia: no concede nada
  AUSENTE          el campo esta vacio
"""
import collections, csv, gzip, os, re, sys

CORTE = sys.argv[1] if len(sys.argv) > 1 else 'corte-figuras.2026-10-05.tsv'
# 🔴 `P352`: el default era `/tmp/oat-censo/unidades-oer.tsv`, una ruta EFIMERA del
# contenedor del pase 110. Importar este modulo fuera de ese contenedor fallaba, asi que
# `test_p345.py` pasaba SOLO donde se escribio. El default pasa al artefacto VERSIONADO.
CENSO = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'censo-unidades.2026-10-05.tsv.gz')
OUT = sys.argv[3] if len(sys.argv) > 3 else 'entregabilidad.2026-10-05.tsv'

# un identificador RESOLUBLE nombra la variante (BY / BY-SA / BY-NC...) y la version
RESOLUBLE = re.compile(
    r'creativecommons\.org/(?:licenses/(by(?:-nc)?(?:-sa)?(?:-nd)?)/(\d\.\d)|publicdomain/zero/(\d\.\d))',
    re.I)
# «CC4.0», «CC 4.0», «CC BY» sin version: nombra MENOS que una licencia
VERSION_SIN_VARIANTE = re.compile(r'^\s*cc\s*-?\s*\d\.\d\s*$', re.I)
URL_CUALQUIERA = re.compile(r'^\s*https?://', re.I)


def clasificar(lic):
    l = (lic or '').strip()
    if not l:
        return 'AUSENTE', '-'
    m = RESOLUBLE.search(l)
    if m:
        if m.group(3):
            return 'RESOLUBLE', 'CC0-%s' % m.group(3)
        return 'RESOLUBLE', 'CC-%s-%s' % (m.group(1).upper(), m.group(2))
    if VERSION_SIN_VARIANTE.match(l):
        return 'VERSION-SIN-VARIANTE', l
    if URL_CUALQUIERA.match(l):
        return 'NO-ES-CESION', l
    return 'NO-RECONOCIDO', l




def _abrir(path):
    """Lee el censo versionado (`.gz`) o uno plano pasado por argumento."""
    return gzip.open(path, 'rt', encoding='utf-8') if path.endswith('.gz') else open(
        path, encoding='utf-8')


def main(corte=CORTE, censo=CENSO, out=OUT):
    lic = {}
    with _abrir(censo) as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            lic[r['problem_id']] = r['license']

    rows = []
    with open(corte, encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            cls, ident = clasificar(lic.get(r['problem_id'], ''))
            rows.append((r['problem_id'], r['figura'], r['forma'], r['lado'], cls, ident))

    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('problem_id\tfigura\tforma_oer\tlado\tclase_cesion\tidentificador\n')
        for r in rows:
            fh.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')

    print('=== LAS 2.443 FIGURAS POR CLASE DE CESION ===')
    c = collections.Counter(r[4] for r in rows)
    tot = len(rows)
    for k, v in c.most_common():
        print('%-22s %5d  %5.1f %%' % (k, v, 100.0 * v / tot))
    print('%-22s %5d' % ('TOTAL', tot))
    print()
    print('=== identificadores resolubles ===')
    for k, v in collections.Counter(r[5] for r in rows if r[4] == 'RESOLUBLE').most_common():
        print('%-16s %5d' % (k, v))
    print()
    print('=== cruce: lado openstax x clase de cesion ===')
    x = collections.Counter((r[3], r[4]) for r in rows)
    for k, v in sorted(x.items()):
        print('%-13s %-22s %5d' % (k[0], k[1], v))
    print()
    ent = c['RESOLUBLE']
    print('ENTREGABLE SIN GESTION: %d de %d  (%.1f %%)' % (ent, tot, 100.0 * ent / tot))
    print('REQUIERE GESTION:       %d de %d  (%.1f %%)' % (tot - ent, tot, 100.0 * (tot - ent) / tot))


if __name__ == '__main__':
    main()
