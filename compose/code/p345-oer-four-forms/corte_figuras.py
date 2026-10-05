#!/usr/bin/env python3
"""El corte openstax / no-openstax sobre las 2.443 FIGURAS (`P337`).

Cada figura vive en `content-pool/<problemId>/figures/*.gif`, asi que la
atribucion es por RUTA y no por nombre: la unidad de cesion de una figura es
el problema que la contiene.
"""
import collections, csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from censo_oer import forma_de

ROOT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/oat-full'
CENSO = sys.argv[2] if len(sys.argv) > 2 else '/tmp/oat-censo/unidades-oer.tsv'
OUT = sys.argv[3] if len(sys.argv) > 3 else 'corte-figuras.2026-10-05.tsv'
POOL = os.path.join(ROOT, 'content-pool')

oer_de, forma_pub = {}, {}
with open(CENSO, encoding='utf-8') as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        oer_de[r['problem_id']] = r['oer']
        forma_pub[r['problem_id']] = r['forma']

figuras = []
for d in sorted(os.listdir(POOL)):
    fd = os.path.join(POOL, d, 'figures')
    if not os.path.isdir(fd):
        continue
    for f in sorted(os.listdir(fd)):
        if f.lower().endswith('.gif'):
            figuras.append((d, f))

filas, sin_unidad = [], 0
for pid, fn in figuras:
    if pid not in oer_de:
        sin_unidad += 1
        filas.append((pid, fn, '', 'SIN-UNIDAD-JSON', 'NO-RESOLUBLE'))
        continue
    oer = oer_de[pid]
    forma = forma_pub[pid]
    lado = 'OPENSTAX' if forma not in ('NO-OPENSTAX', 'VACIO') else 'NO-OPENSTAX'
    if forma == 'VACIO':
        lado = 'OER-VACIO'
    filas.append((pid, fn, oer, forma, lado))

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('problem_id\tfigura\toer\tforma\tlado\n')
    for r in filas:
        fh.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')

print('figuras totales: %d' % len(filas))
print('problemas con figuras: %d' % len({r[0] for r in filas}))
print('figuras sin JSON de unidad: %d' % sin_unidad)
print()
print('=== por FORMA de oer ===')
for k, v in collections.Counter(r[3] for r in filas).most_common():
    print('%-18s %5d' % (k, v))
print()
print('=== EL CORTE que P337 disputa ===')
c = collections.Counter(r[4] for r in filas)
for k, v in c.most_common():
    print('%-14s %5d' % (k, v))
print()
print('openstax=%d  no-openstax(+vacio)=%d  suma=%d'
      % (c['OPENSTAX'], c['NO-OPENSTAX'] + c['OER-VACIO'] + c['NO-RESOLUBLE'],
         sum(c.values())))
