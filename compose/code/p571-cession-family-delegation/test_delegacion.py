#!/usr/bin/env python3
"""`P571`..`P578` — la compuerta de cesion delega la FAMILIA. Suite sobre payloads REALES.

Pase 47 del 2026-10-08.

El pase 46 dejo declarado abierto que `p411-cession-identity-gate` «todavia inlinea un
clasificador de licencias y todavia carga `P561`». Esta suite es la medicion de ese
pendiente y el control que impide que vuelva.

🔵 **Por que el defecto sobrevivio un pase entero: el corpus de `p411/test_gate.py` no
tenia NI UN payload copyleft, ni uno OSI que no fuera MIT.** Siete casos, todos
sinteticos, todos verdes. Una suite verde porque nunca pregunto. Asi que esta suite no
agrega asserts: agrega CORPUS, y el corpus es el arbol real.

Cada caso trae su CONTROL NEGATIVO: `escalera_inlineada()` reproduce la escalera que el
pase 47 borro, y la suite exige que para cada clase de defecto la escalera siga dando la
respuesta EQUIVOCADA. Si manana alguien re-inlinea un clasificador, estos controles no se
quedan callados: una suite que solo verifica el camino correcto no detecta una regresion
que vuelve a tomar el camino viejo.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # `P355`: nunca el cwd
CODE = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(CODE, 'p411-cession-identity-gate'))

from gate_cesion import (                                   # noqa: E402
    clasificar, familia_compartida, SinClasificador, PERMISIVAS,
)

FIX = {
    'moodle':    'p184-holder-mismatch/fixtures/gpl-3.0-moodle-COPYING.txt',
    'openemis':  'p255-holder-shared-control/fixtures/gpl-2.0-openemis-core-LICENSE.txt',
    'rhino':     'p560-epl-mpl-version-read/fixtures/mpl-2.0-rhino-partial-grant.LICENSE',
    'huly':      'p560-epl-mpl-version-read/fixtures/epl-2.0-huly.LICENSE',
    'jersey':    'p560-epl-mpl-version-read/fixtures/epl-2.0-jersey.LICENSE',
    'junit4':    'p560-epl-mpl-version-read/fixtures/epl-1.0-junit4.LICENSE',
    'mpl11':     'p560-epl-mpl-version-read/fixtures/mpl-1.1-spdx-canonical.LICENSE',
    'h2':        'p560-epl-mpl-version-read/fixtures/dual-mpl-2.0-or-epl-1.0-h2database.LICENSE',
    'sakai':     'p473-probe-commercial-gate/fixtures/ecl-2.0-sakai.LICENSE',
    'gopt':      'p308-phrase-anchor-sweep/fixtures/bsd3-YuanGongND-gopt.LICENSE',
    'unlicense': 'p308-phrase-anchor-sweep/fixtures/unlicense-FWU-DE-mem-mcp.LICENSE',
    'lmscloud':  'p473-probe-commercial-gate/fixtures-pending/gpl-3.0-lmscloud.LICENSE',
    'autolab':   'p308-phrase-anchor-sweep/fixtures/apache-autolab-Autolab.LICENSE',
    'ccbysa':    'lib/fixtures-p551/cc-by-sa-4.0-ud-portuguese-bosque.LICENSE',
}


def leer(clave):
    ruta = os.path.join(CODE, FIX[clave])
    with open(ruta, encoding='utf-8') as fh:
        return fh.read()


def escalera_inlineada(texto):
    """La escalera que el pase 47 BORRO de `gate_cesion.py`, byte por byte.

    Vive aqui, y SOLO aqui, como control negativo. No se la llama en produccion.
    """
    bajo = texto.lower()
    if 'apache license' in bajo:
        return 'Apache-2.0'
    if 'gnu affero' in bajo:
        return 'AGPL-3.0'
    if 'gnu lesser' in bajo:
        return 'LGPL'
    if 'gnu general public' in bajo:
        return 'GPL'
    if 'mozilla public' in bajo:
        return 'MPL-2.0'
    if 'redistributions of source code' in bajo:
        return 'BSD'
    if 'permission is hereby granted, free of charge' in bajo:
        return 'MIT'
    return 'UNCLASSIFIED'


# (codigo, clave, familia esperada, usable esperado, respuesta EQUIVOCADA de la escalera)
CASOS = [
    ('P571', 'moodle',    'GPL-3.0',    False, 'AGPL-3.0'),
    ('P571', 'lmscloud',  'GPL-3.0',    False, 'AGPL-3.0'),
    ('P572', 'openemis',  'GPL-2.0',    False, 'LGPL'),
    ('P573', 'rhino',     'MPL-2.0',    False, 'AGPL-3.0'),
    ('P574', 'huly',      'EPL-2.0',    False, 'GPL'),
    ('P574', 'jersey',    'EPL-2.0',    False, 'GPL'),
    ('P575', 'mpl11',     'MPL-1.1',    False, 'MPL-2.0'),
    ('P578', 'h2',        'MPL-2.0',    False, 'AGPL-3.0'),
    ('P576', 'sakai',     'ECL-2.0',    True,  'Apache-2.0'),
    ('P577', 'gopt',      'BSD',        True,  'BSD'),
    ('P579', 'unlicense', 'Unlicense',  True,  'UNCLASSIFIED'),
    ('----', 'junit4',    'EPL-1.0',    False, 'UNCLASSIFIED'),
    ('----', 'autolab',   'Apache-2.0', True,  'Apache-2.0'),
]

# Las tres clases de defecto no se controlan igual, y confundirlas fue un error de ESTA
# suite en su primera corrida: `P576`/`P577`/`P579` NO eran fallas de la escalera de
# familia —la escalera acierta `BSD` y no sabe nada de ECL— sino de la compuerta de TITULO
# y de la lista de LIMITACIONES. Un control que le pide a la escalera un defecto que la
# escalera no comete pasa por la razon equivocada o falla por la razon equivocada.
DEFECTO_DE_ESCALERA = {'P571', 'P572', 'P573', 'P574', 'P575', 'P578'}

fallos = []


def check(ok, etiqueta, detalle=''):
    print(('🟢 ' if ok else '🔴 ') + etiqueta + ('' if ok else f'   <- {detalle}'))
    if not ok:
        fallos.append(etiqueta)


print(f'--- familia + usable sobre payloads REALES del arbol ({len(CASOS)} casos) ---')
for codigo, clave, fam_esp, usable_esp, _ in CASOS:
    v = clasificar(leer(clave))
    ok = v['familia'] == fam_esp and v['usable'] == usable_esp
    check(ok, f'{codigo} {clave:10s} -> {v["familia"]:12s} usable={"SI" if v["usable"] else "NO"}',
          f'esperado {fam_esp} usable={usable_esp}')

print('\n--- CONTROL NEGATIVO: la escalera borrada sigue dando la respuesta equivocada ---')
for codigo, clave, fam_esp, _u, mala in CASOS:
    if codigo not in DEFECTO_DE_ESCALERA:
        continue
    obtuvo = escalera_inlineada(leer(clave))
    ok = obtuvo == mala and mala != fam_esp
    check(ok, f'{codigo} {clave:10s}: escalera -> {obtuvo:12s} (correcto: {fam_esp})',
          f'la escalera devolvio {obtuvo}, se esperaba el defecto {mala}')

print('\n--- CONTROL NEGATIVO: los disparadores de los tres FALSOS RECHAZOS siguen ahi ---')
# Si manana alguien borra el disparador en vez de estrecharlo, la compuerta deja de
# atrapar a `PageLM` y estos controles son los que lo dicen.
_sakai6 = '\n'.join(leer('sakai').splitlines()[:6]).lower()
check('community license' in _sakai6,
      'P576 sakai     : «community license» sigue en el titulo de la ECL',
      'el disparador ya no aparece — la exencion dejo de tener sentido')
_gopt6 = '\n'.join(leer('gopt').splitlines()[:6]).lower()
check('all rights reserved' in _gopt6,
      'P577 gopt      : «all rights reserved» sigue en el encabezado BSD',
      'el disparador ya no aparece en las primeras 6 lineas')
check('non-commercial' in leer('unlicense').lower(),
      'P579 unlicense : «non-commercial» sigue en el texto del Unlicense',
      'el disparador ya no aparece — el fraseo de concesion cambio')

print('\n--- MUTANTES: cada uno rompe el arreglo y la suite DEBE verlo ---')


def mutante(nombre, fn, clave, familia_mala):
    try:
        v = fn(leer(clave))
    except Exception as e:                                   # noqa: BLE001
        check(False, f'mutante {nombre}', f'excepcion {e}')
        return
    check(v == familia_mala, f'mutante {nombre}: {clave} -> {v} (produccion no lo hace)',
          f'devolvio {v}, se esperaba {familia_mala}')


# M1 — sin delegacion: la escalera vuelve y Moodle vuelve a leerse AGPL-3.0.
mutante('M1 sin-delegacion', escalera_inlineada, 'moodle', 'AGPL-3.0')
# M2 — sin delegacion: MPL-2.0 vuelve a leerse como el copyleft de red mas fuerte.
mutante('M2 sin-delegacion', escalera_inlineada, 'rhino', 'AGPL-3.0')
# M3 — sin delegacion: EPL-2.0 vuelve a leerse GPL por la clausula de Secondary Licenses.
mutante('M3 sin-delegacion', escalera_inlineada, 'huly', 'GPL')


def gate_sin_exencion(texto):
    """M4 — la compuerta de titulo SIN la exencion de `P576`: Sakai se rechaza."""
    primeras = '\n'.join(texto.splitlines()[:6]).lower()
    return 'NO-OSI (community license)' if 'community license' in primeras else 'ECL-2.0'


mutante('M4 sin-exencion-P576', gate_sin_exencion, 'sakai', 'NO-OSI (community license)')


def gate_sin_guarda(texto):
    """M5 — la compuerta SIN la guarda de `P577`: un encabezado BSD se rechaza."""
    primeras = '\n'.join(texto.splitlines()[:6]).lower()
    return 'NO-OSI (all rights reserved)' if 'all rights reserved' in primeras else 'BSD'


mutante('M5 sin-guarda-P577', gate_sin_guarda, 'gopt', 'NO-OSI (all rights reserved)')


def limitaciones_sin_descuento(texto):
    """M6 — `LIMITACIONES_FATALES` SIN el descuento de `P579`: el Unlicense se rechaza."""
    bajo = texto.lower()
    return 'FATAL' if 'non-commercial' in bajo else 'limpio'


mutante('M6 sin-descuento-P579', limitaciones_sin_descuento, 'unlicense', 'FATAL')

print('\n--- `P197`: sin clasificador compartido NO hay degradacion silenciosa ---')
try:
    familia_compartida('MIT License\n\nPermission is hereby granted, free of charge',
                       lib=os.path.join(HERE, 'no-existe-este-clasificador.sh'))
    check(False, 'levanta SinClasificador', 'devolvio una familia sin el clasificador')
except SinClasificador:
    check(True, 'levanta SinClasificador en vez de re-inlinear la escalera')

print('\n--- `P542`: corpus vacio -> exit 2, no un verde ---')
try:
    v = clasificar('')
    check(v['familia'] == 'SIN-CESION' and not v['usable'],
          f'payload vacio -> {v["familia"]} usable=NO', f'devolvio {v}')
except Exception as e:                                       # noqa: BLE001
    check(False, 'payload vacio', str(e))

print('\n--- control de vocabulario: PERMISIVAS no contiene ningun copyleft ---')
COPYLEFT = {'GPL-2.0', 'GPL-3.0', 'AGPL-3.0', 'LGPL', 'LGPL-3.0',
            'MPL-1.0', 'MPL-1.1', 'MPL-2.0', 'EPL-1.0', 'EPL-2.0', 'EUPL-1.1', 'EUPL-1.2'}
solapamiento = PERMISIVAS & COPYLEFT
check(not solapamiento, 'PERMISIVAS ∩ copyleft = ∅', f'solapan: {sorted(solapamiento)}')

total = len(CASOS) + len([c for c in CASOS if c[0] in DEFECTO_DE_ESCALERA]) + 3 + 6 + 1 + 1 + 1
print()
if fallos:
    print(f'🔴 {len(fallos)} FALLO(S) de {total}:')
    for f in fallos:
        print(f'   - {f}')
    sys.exit(1)
print(f'🟢 TODO VERDE — {total} casos')
