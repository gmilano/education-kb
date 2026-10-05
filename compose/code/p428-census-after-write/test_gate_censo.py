#!/usr/bin/env python3
"""Suite de la compuerta de censo. Cada caso es una cifra REAL de este arbol."""
import sys
from gate_censo import clasificar_censo

CASOS = [
    # (nombre, declarado, medido_post, momento, delta, veredicto_esperado)
    ('pase 124 — 645 etiquetada PRE con su delta publicado (lo que este pase hizo)',
     645, 655, 'PRE', 10, 'OK'),
    ('pase 124 — 645 etiquetada PRE SIN delta: correcta pero incompleta',
     645, 655, 'PRE', None, 'PRE-SIN-DELTA'),
    ('el defecto que la accion N predijo: 645 publicada como estado del arbol',
     645, 655, 'POST', None, 'DESFASADO'),
    ('cifra sin momento — la clase que los pases 122 y 123 publicaron sin verla',
     645, 655, None, None, 'SIN-MOMENTO'),
    ('censo POST correcto: se re-corrio despues de escribir',
     655, 655, 'POST', None, 'OK'),
    ('delta mal publicado (aritmetica propia, no del canal)',
     645, 655, 'PRE', 13, 'DELTA-ERRADO'),
    ('pase 122 — clase positiva: 10 pre-escritura, 13 post-escritura',
     10, 13, 'PRE', 3, 'OK'),
    ('pase 122 — la misma cifra presentada como estado final',
     10, 13, 'POST', None, 'DESFASADO'),
    ('arbol quieto: un pase sin altas no produce delta',
     655, 655, 'PRE', 0, 'OK'),
]

def main():
    fallos = 0
    for nombre, dec, post, mom, delta, esperado in CASOS:
        r = clasificar_censo(dec, post, mom, delta)
        ok = r['veredicto'] == esperado
        print(f"{'🟢' if ok else '🔴'} {r['veredicto']:14s} (esperado {esperado:14s}) {nombre}")
        if not ok:
            fallos += 1
            print(f"     motivo devuelto: {r['motivo']}")
    print(f"\n{len(CASOS) - fallos}/{len(CASOS)} casos en verde")
    return 1 if fallos else 0

if __name__ == '__main__':
    sys.exit(main())
