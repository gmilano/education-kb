#!/usr/bin/env python3
"""
Controles de `description-drift-audit` (pase 63).

Regla de esta KB (P126): un instrumento se publica con un control que FALLA si el
instrumento no discrimina. Aca hay tres cosas que discriminar, y la tercera es la que
justifica el archivo entero:

  1. que lea la cifra de la `description` y la del README POR SEPARADO;
  2. que la deriva sea None -- y NO 0 -- cuando falta cualquiera de las dos cifras;
  3. que distinga un repo SIN descripcion (invisible para un barrido por busqueda) de uno
     con descripcion que simplemente no nombra una cifra.

Todas las fixtures son capturas reales del pase 63, salvo donde se declara lo contrario.
"""
import io, os, sys
from audit_drift import audit, drift, split_capture

HERE = os.path.dirname(os.path.abspath(__file__))
fails = []


def check(label, got, want):
    ok = got == want
    print('  %-4s %-58s %s' % ('ok' if ok else 'FALLA', label, got))
    if not ok:
        fails.append('%s: esperaba %r, dio %r' % (label, want, got))


def load(name):
    with io.open(os.path.join(HERE, 'fixtures', name), encoding='utf-8') as f:
        return audit(name, f.read())


print('== Los dos ejes se leen POR SEPARADO (P165) ==')
a = load('amirf194-canvas-mcp.txt')
check('AmirF194: la description dice 80', a['description_tools'], 80)
check('AmirF194: el README dice 101', a['readme_tools'], 101)
check('AmirF194: deriva = +21', a['drift'], 21)

print('== La deriva aparece tambien SIN fork, y es el hallazgo del pase ==')
x = load('xmike04-canvas-student-mcp.txt')
check('xmike04 NO es fork y deriva igual: 19 -> 29', x['drift'], 10)

print('== Un fork puede tener la description AL DIA y derivar poco ==')
l = load('lindsay-cheng-canvas-mcp.txt')
check('lindsay-cheng: 102 -> 103', l['drift'], 1)

print('== CONTROL 1: sin descripcion, el repo es INVISIBLE a un barrido por busqueda ==')
p = load('peancor-moodle-mcp-server.txt')
check('peancor: description_tools es None', p['description_tools'], None)
check('peancor: NO es buscable', p['searchable'], False)
check('peancor: deriva None, no 0', p['drift'], None)

print('== CONTROL 2: con descripcion pero SIN cifra, tampoco es 0 ==')
m = load('mtgibbs-canvas-lms-mcp.txt')
check('mtgibbs: SI tiene descripcion', m['searchable'], True)
check('mtgibbs: pero sin cifra -> None', m['description_tools'], None)
check('mtgibbs: deriva None, no 0', m['drift'], None)

print('== CONTROL 3: el 0 se reserva para una coincidencia REAL (caso sintetico) ==')
# No se encontro NINGUN repo con las dos cifras iguales en el barrido del pase 63
# (0 de 5). El control es sintetico y se declara como tal: sirve para probar que el
# instrumento SI puede devolver 0, y que el 0 no es su valor por defecto.
check('coincidencia real -> 0', drift(42, 42), 0)
check('falta la del README -> None', drift(42, None), None)
check('falta la de la description -> None', drift(None, 42), None)

print('== La captura se parte bien: `forked from` no se confunde con la description ==')
desc, _ = split_capture(open(os.path.join(HERE, 'fixtures', 'amirf194-canvas-mcp.txt'),
                             encoding='utf-8').read())
check('la description NO empieza con "forked from"',
      desc.lower().startswith('forked from'), False)

print()
if fails:
    print('FALLARON %d ASERCIONES:' % len(fails))
    for f in fails:
        print('  - ' + f)
    sys.exit(1)
print('TODAS LAS ASERCIONES PASAN (14)')
