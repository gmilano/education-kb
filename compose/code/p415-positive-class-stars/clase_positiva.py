#!/usr/bin/env python3
"""Accion O del pase 122, corrida en el pase 123.

La accion O dice que vaciar el conjunto AGREGANDO clases de exclusion es afinar-hasta-verde:
la suite del pase 122 quedo verde con CUATRO exclusiones (meta, umbral, `P403` cita-de-canal,
`P404` rechazo). En vez de eso se define la clase POSITIVA —la ★ que es el DATO de una fila
que el estante recomienda— y se mide la propiedad «lleva banda y fecha» SOLO sobre ella.

Hipotesis pre-registrada: la clase positiva tiene MENOS miembros que el universo del barrido
y la propiedad se sostiene sin ninguna clase de exclusion.
Refutada si hace falta >=1 exclusion igual.

🔵 Y pesa mas por `P409`: el atribuidor de pases era sensible a mayusculas y la rama de
refutacion de la accion B venia pasando por accidente. Aca se re-prueba sobre el atribuidor
CORREGIDO (ambos portadores, ambos insensibles a mayusculas).
"""
import os, re, sys

RE_CIFRA = re.compile(r'[0-9]{1,3}[.,][0-9]{3}(?:\.[0-9]{3})* ?★')
RE_ENCABEZADO_PASE = re.compile(r'pase (\d+)', re.IGNORECASE)
RE_LINEA_DE_PASE = re.compile(r'^>\s*\*\*Pase (\d+) del ', re.IGNORECASE)
RE_FECHA = re.compile(r'20[0-9]{2}-[0-9]{2}-[0-9]{2}')
RE_BANDA = re.compile(r'EXACTO|K-3CIFRAS|±\s*500|P349', re.IGNORECASE)

ARCHIVOS = ('agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
            'verticals/solutions.md', 'intel/market.md', 'intel/trends.md',
            'compose/patterns.md')
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')


def es_fila_de_datos(linea):
    """Una fila de TABLA que no es encabezado ni separador. Es donde vive el dato que el
    estante RECOMIENDA: el resto del archivo es prosa, y la prosa cita."""
    l = linea.strip()
    if not (l.startswith('|') and l.endswith('|')):
        return False
    if re.fullmatch(r'[\s:|\-]+', l):          # separador `|---|---|`
        return False
    return True


def es_cita(fragmento_de_celda):
    """`P351`: en este arbol una cifra CITADA va entre comillas latinas o en codigo inline."""
    return ('«' in fragmento_de_celda and '»' in fragmento_de_celda) or \
           fragmento_de_celda.count('`') >= 2


def main():
    universo = 0            # toda ocurrencia, como la contaba la accion B
    positivos = []          # la clase POSITIVA
    for rel in ARCHIVOS:
        ruta = os.path.join(RAIZ, rel)
        if not os.path.exists(ruta):
            continue
        lineas = open(ruta, encoding='utf-8').read().splitlines()
        for i, linea in enumerate(lineas, 1):
            hits = RE_CIFRA.findall(linea)
            if not hits:
                continue
            universo += len(hits)
            if not es_fila_de_datos(linea):
                continue
            celdas = [c for c in linea.strip().strip('|').split('|')]
            for celda in celdas:
                for cifra in RE_CIFRA.findall(celda):
                    if es_cita(celda):
                        continue
                    positivos.append({
                        'archivo': rel, 'linea': i, 'cifra': cifra.strip(),
                        'banda': bool(RE_BANDA.search(linea)),
                        'fecha': bool(RE_FECHA.search(linea)),
                    })

    con_ambas = [p for p in positivos if p['banda'] and p['fecha']]
    sin_banda = [p for p in positivos if not p['banda']]
    sin_fecha = [p for p in positivos if not p['fecha']]

    print('=== ACCION O: la clase POSITIVA (★ que es el dato de una fila recomendada) ===')
    print(f'universo del barrido (accion B, toda ocurrencia)   {universo}')
    print(f'clase POSITIVA (celda de fila de datos, no cita)   {len(positivos)}')
    print(f'  de ellas con BANDA y FECHA                       {len(con_ambas)}')
    print(f'  sin banda                                        {len(sin_banda)}')
    print(f'  sin fecha                                        {len(sin_fecha)}')
    print()
    print('clausula 1 — la clase positiva es MENOR que el universo: '
          f'{"🟢 SI" if len(positivos) < universo else "🔴 NO"}')
    sostiene = len(sin_banda) == 0 and len(sin_fecha) == 0
    print('clausula 2 — la propiedad se sostiene SIN exclusiones: '
          f'{"🟢 SI" if sostiene else "🔴 NO"}')
    print()
    print(f'VEREDICTO: {"CONFIRMADA" if (len(positivos) < universo and sostiene) else "REFUTADA"}')
    print()
    print('=== reparto de la clase positiva por archivo ===')
    por_archivo = {}
    for p in positivos:
        por_archivo[p['archivo']] = por_archivo.get(p['archivo'], 0) + 1
    for a, n in sorted(por_archivo.items(), key=lambda x: -x[1]):
        print(f'{a:28} {n}')
    print()
    print('=== primeras 12 de la clase positiva SIN banda ===')
    for p in sin_banda[:12]:
        print(f"{p['archivo']}:{p['linea']}  {p['cifra']}  banda={p['banda']} fecha={p['fecha']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
