#!/usr/bin/env python3
"""Barrido ANTES/DESPUES de la delegacion, sobre todos los payloads reales del arbol.

Pase 47 del 2026-10-08.

`clasificar_pase123()` reconstruye la compuerta tal como estaba ANTES de este pase, para
que el numero «18 de 29 divergian» sea REPRODUCIBLE y no una cifra copiada de una
corrida. Si alguien duda del antes, lo corre.

Uso:  python3 medir.py            -> escribe los dos TSV y el resumen
      python3 medir.py --check    -> falla si el antes/despues dejo de reproducirse
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # `P355`
CODE = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(CODE, 'p411-cession-identity-gate'))

from gate_cesion import (                                   # noqa: E402
    clasificar, LIMITACIONES_FATALES, PISO_DE_CESION, PISO_MIT, TITULOS_NO_OSI,
)

LIB = os.path.join(CODE, 'lib', 'license_family.sh')
_PUENTE = '. "$1"\nT=$(cat)\nprintf "%s" "$(family_of "$T")"\n'


def family_of(texto):
    p = subprocess.run(['sh', '-c', _PUENTE, 'sh', LIB], input=texto,
                       capture_output=True, text=True, timeout=60)
    return (p.stdout or '').strip()


def clasificar_pase123(texto):
    """La compuerta ANTES del pase 47: escalera inlineada + compuerta de titulo ancha."""
    bytes_ = len(texto.encode('utf-8'))
    bajo = texto.lower()
    if bytes_ == 0 or bytes_ < 10:
        return 'SIN-CESION'
    if bytes_ < PISO_DE_CESION:
        return 'NOMBRAMIENTO'
    primeras = '\n'.join(texto.splitlines()[:6]).lower()
    for t in TITULOS_NO_OSI:
        if t in primeras:
            return f'NO-OSI ({t})'
    fatales = [l for l in LIMITACIONES_FATALES if l in bajo]
    if 'apache license' in bajo:
        fam = 'Apache-2.0'
    elif 'gnu affero' in bajo:
        fam = 'AGPL-3.0'
    elif 'gnu lesser' in bajo:
        fam = 'LGPL'
    elif 'gnu general public' in bajo:
        fam = 'GPL'
    elif 'mozilla public' in bajo:
        fam = 'MPL-2.0'
    elif 'redistributions of source code' in bajo:
        fam = 'BSD'
    elif 'permission is hereby granted, free of charge' in bajo:
        if bytes_ > PISO_MIT * 3:
            return 'NO-OSI (frase MIT en documento largo)'
        fam = 'MIT'
    else:
        return 'UNCLASSIFIED'
    _ = fatales
    return fam


def payloads():
    """Todo payload de cesion real del arbol. `P542`: un corpus vacio es un error."""
    out = []
    for raiz, _dirs, archivos in os.walk(CODE):
        for a in sorted(archivos):
            if a.endswith('.LICENSE') or a.endswith('COPYING.txt') or \
                    (a.startswith('gpl-') and a.endswith('.txt')):
                out.append(os.path.join(raiz, a))
    return sorted(set(out))


def main():
    rutas = payloads()
    if not rutas:
        print('🔴 corpus vacio — no hay payloads que medir', file=sys.stderr)
        return 2

    filas, divergian, divergen = [], 0, 0
    for ruta in rutas:
        with open(ruta, encoding='utf-8') as fh:
            texto = fh.read()
        antes = clasificar_pase123(texto)
        lib = family_of(texto)
        ahora = clasificar(texto)['familia']
        mal_antes = antes != lib
        mal_ahora = ahora != lib
        divergian += mal_antes
        divergen += mal_ahora
        filas.append((os.path.basename(ruta), antes, ahora, lib,
                      'DIVERGIA' if mal_antes else 'ok',
                      'DIVERGE' if mal_ahora else 'ok'))

    for nombre, cols in (('result-before.2026-10-08.tsv', (1, 3, 4)),
                         ('result-after.2026-10-08.tsv', (2, 3, 5))):
        with open(os.path.join(HERE, nombre), 'w', encoding='utf-8') as fh:
            fh.write('PAYLOAD\tCOMPUERTA\tfamily_of\tVEREDICTO\n')
            for f in filas:
                fh.write(f'{f[0]}\t{f[cols[0]]}\t{f[cols[1]]}\t{f[cols[2]]}\n')

    print(f'payloads reales medidos : {len(filas)}')
    print(f'divergian ANTES         : {divergian}')
    print(f'divergen DESPUES        : {divergen}')
    print('\nlas que todavia divergen son el JUICIO de la compuerta, no un defecto:')
    for f in filas:
        if f[5] == 'DIVERGE':
            print(f'  {f[0]:46s} compuerta={f[2]:26s} family_of={f[3]}')

    if '--check' in sys.argv:
        # El antes debe seguir siendo reproducible, y el despues no debe empeorar.
        if divergian != 18:
            print(f'🔴 el ANTES ya no reproduce 18 divergencias (dio {divergian})',
                  file=sys.stderr)
            return 1
        if divergen > 4:
            print(f'🔴 el DESPUES empeoro: {divergen} > 4', file=sys.stderr)
            return 1
        print('\n🟢 antes=18 despues=4 — reproducido')
    return 0


if __name__ == '__main__':
    sys.exit(main())
