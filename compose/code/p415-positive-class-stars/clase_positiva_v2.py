#!/usr/bin/env python3
"""Accion O, segunda version — y la primera version se deja publicada porque FALLO y el
motivo es el hallazgo.

🔴 `P415` — la clase positiva NO es «una fila de datos de una tabla». Las tablas de este arbol
incluyen tablas de RECHAZO (`| candidata | cifra que trajo el canal | por que NO entra |`) y
tablas de DENOMINADOR (`| Lo que devolvio el barrido global | n |`). Sus cifras son citas con
OTRA FORMA: no se les debe banda ni fecha, porque no son filas que el estante recomiende.
Medir «0 de 80 lleva banda» sobre ellas no mide una deuda: mide el instrumento equivocado.

La v1 contaba 80 y declaraba la propiedad falsa en el 100%. Leyendo las filas —y no el
conteo— las dos primeras resultaron ser «por que NO entra» y «lo que devolvio el barrido».
Es `P410` un nivel mas arriba: la tabla se identifica por la ETIQUETA DE SU BLOQUE y por su
FILA DE ENCABEZADO, no por su forma.

Definicion corregida: la fila positiva es la que vive en una tabla cuyo ENCABEZADO declara una
columna de CESION (licencia/cesion/repo+licencia) — que es la forma que tiene una fila
recomendada en este arbol — y cuyo bloque no esta rotulado como rechazo/denominador.
"""
import os, re, sys

RE_CIFRA = re.compile(r'[0-9]{1,3}[.,][0-9]{3}(?:\.[0-9]{3})* ?★')
RE_FECHA = re.compile(r'20[0-9]{2}-[0-9]{2}-[0-9]{2}')
RE_BANDA = re.compile(r'EXACTO|K-3CIFRAS|±\s*500|P349', re.IGNORECASE)
# el encabezado de una tabla que RECOMIENDA nombra la cesion
RE_ENCABEZADO_RECOMIENDA = re.compile(r'licenc|cesi(o|ó)n|SPDX', re.IGNORECASE)
# rotulos que marcan rechazo o denominador
RE_RECHAZO = re.compile(r'NO entra|rechaz|no cede|descart|denominador|lo que devolvi|'
                        r'por que NO|candidata|hueco|falla|sin licencia', re.IGNORECASE)

ARCHIVOS = ('agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
            'verticals/solutions.md', 'intel/market.md', 'intel/trends.md',
            'compose/patterns.md')
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')


def es_fila(l):
    l = l.strip()
    return l.startswith('|') and l.endswith('|') and not re.fullmatch(r'[\s:|\-]+', l)


def main():
    universo = 0
    v1 = 0            # la clase de la v1: toda fila de datos
    positivos = []
    for rel in ARCHIVOS:
        ruta = os.path.join(RAIZ, rel)
        if not os.path.exists(ruta):
            continue
        lineas = open(ruta, encoding='utf-8').read().splitlines()
        encabezado_actual, etiqueta_actual = None, ''
        for i, linea in enumerate(lineas, 1):
            if linea.startswith('#'):
                etiqueta_actual = linea
                encabezado_actual = None
                continue
            if es_fila(linea):
                if encabezado_actual is None:
                    encabezado_actual = linea      # primera fila del bloque = su encabezado
                    continue
            else:
                if not linea.strip().startswith('|'):
                    encabezado_actual = None
            hits = RE_CIFRA.findall(linea)
            if not hits:
                continue
            universo += len(hits)
            if not es_fila(linea):
                continue
            v1 += len(hits)
            if encabezado_actual is None:
                continue
            if not RE_ENCABEZADO_RECOMIENDA.search(encabezado_actual):
                continue
            if RE_RECHAZO.search(encabezado_actual) or RE_RECHAZO.search(etiqueta_actual):
                continue
            for cifra in hits:
                positivos.append({'archivo': rel, 'linea': i, 'cifra': cifra.strip(),
                                  'banda': bool(RE_BANDA.search(linea)),
                                  'fecha': bool(RE_FECHA.search(linea)),
                                  'etiqueta': etiqueta_actual[:70]})

    sin_banda = [p for p in positivos if not p['banda']]
    sin_fecha = [p for p in positivos if not p['fecha']]
    print('=== ACCION O v2: la clase POSITIVA por ETIQUETA DE BLOQUE y ENCABEZADO (`P415`) ===')
    print(f'universo del barrido (toda ocurrencia)             {universo}')
    print(f'clase de la v1 (toda fila de datos) — EQUIVOCADA   {v1}')
    print(f'clase POSITIVA corregida                           {len(positivos)}')
    print(f'  sin banda                                        {len(sin_banda)}')
    print(f'  sin fecha                                        {len(sin_fecha)}')
    print()
    print(f'clausula 1 — positiva < universo: {"🟢 SI" if len(positivos) < universo else "🔴 NO"}')
    sostiene = not sin_banda and not sin_fecha
    print(f'clausula 2 — se sostiene sin exclusiones: {"🟢 SI" if sostiene else "🔴 NO"}')
    print(f'\nVEREDICTO v2: {"CONFIRMADA" if (len(positivos) < universo and sostiene) else "REFUTADA"}')
    print('\n=== la clase positiva, fila por fila (enumerada, no resumida) ===')
    for p in positivos:
        print(f"{p['archivo']}:{p['linea']}  {p['cifra']:12} banda={'SI' if p['banda'] else 'NO'} "
              f"fecha={'SI' if p['fecha'] else 'NO'}  « {p['etiqueta']} »")
    return 0


if __name__ == '__main__':
    sys.exit(main())
