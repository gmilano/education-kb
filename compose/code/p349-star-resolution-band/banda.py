#!/usr/bin/env python3
"""`P349` — la resolucion del canal de estrellas es una FUNCION ESCALON, no «3 cifras significativas».

El pase 110 publico: *«la resolucion es de 3 cifras significativas ("40,8k")»*. Medido sobre
cinco repos de este catalogo en cuatro magnitudes distintas, ese enunciado es falso en LAS DOS
direcciones:

  - por DEBAJO de 1.000 el canal entrega el ENTERO EXACTO (`264`, `107`) — mejor que 3 cifras
  - en la banda 1.000-9.999 entrega solo DOS (`7.5k`) — peor que 3 cifras

Lo que importa para publicar una cifra no es cuantas cifras se ven: es la COTA. Y la cota es un
escalon, con el peor error RELATIVO al pie de la banda `k` y el peor error ABSOLUTO arriba.

Bandas MEDIDAS (cada una con su testigo en `test_p349.py`):

  EXACTO       n < 1.000        se ve `264`     cota 0        exacto
  K-2CIFRAS    1.000-9.999      se ve `7.5k`    +/-50         2 cifras significativas
  K-3CIFRAS    10.000-99.999    se ve `40.8k`   +/-50         3 cifras significativas
  K-ENTERO     >= 100.000       se ve `117k`    +/-500        3 cifras significativas

⚠️ La banda de MILLONES no esta medida: ningun repo de este catalogo la alcanza. Se declara
`NO-MEDIDA` y no se infiere, que es lo que `P286` prohibe.
"""
import re

RE_ENTERO = re.compile(r'^\s*(\d{1,3})\s*$')
RE_K_DEC = re.compile(r'^\s*(\d{1,2})[.,](\d)\s*k\s*$', re.I)
RE_K_INT = re.compile(r'^\s*(\d{1,3})\s*k\s*$', re.I)
RE_M = re.compile(r'^\s*(\d+)(?:[.,](\d))?\s*m\s*$', re.I)


def leer_render(s):
    """Lo que el canal MUESTRA -> (banda, cota_baja, cota_alta).

    Las cotas son inclusivas y son el intervalo de valores verdaderos COMPATIBLES con
    lo renderizado. `exacto` es `cota_baja == cota_alta`.
    """
    if s is None or not str(s).strip():
        return ('AUSENTE', None, None)
    t = str(s).strip()

    m = RE_ENTERO.match(t)
    if m:
        n = int(m.group(1))
        return ('EXACTO', n, n)

    m = RE_K_DEC.match(t)
    if m:
        # `7.5k` -> 7.500 redondeado al centenar: verdadero en [7.450, 7.550]
        centro = int(m.group(1)) * 1000 + int(m.group(2)) * 100
        banda = 'K-2CIFRAS' if centro < 10000 else 'K-3CIFRAS'
        return (banda, centro - 50, centro + 50)

    m = RE_K_INT.match(t)
    if m:
        # `117k` -> redondeado al millar: verdadero en [116.500, 117.500]
        centro = int(m.group(1)) * 1000
        if centro < 10000:
            # `7k` sin decimal no es la forma que el canal usa en esta banda
            return ('NO-RECONOCIDO', None, None)
        return ('K-ENTERO', centro - 500, centro + 500)

    if RE_M.match(t):
        return ('NO-MEDIDA', None, None)

    return ('NO-RECONOCIDO', None, None)


def precision_publicable(n):
    """Dado un valor verdadero, QUE se puede publicar de el por este canal.

    Devuelve (banda, texto_publicable, cota_absoluta). Es la direccion que decide si una
    fila de esta base puede llevar un entero o tiene que llevar una magnitud.

    🔴 La banda se elige por el valor REDONDEADO, no por el crudo. Un valor al pie de un
    limite se redondea CRUZANDOLO (99.950 -> 100.000), y elegir la banda antes de redondear
    emitia `100.0k`, una forma que el propio lector no reconoce. El defecto lo encontro el
    control de ida y vuelta de `test_p349.py`, no la lectura del codigo.
    """
    if n is None:
        return ('AUSENTE', None, None)
    n = int(n)
    if n < 0:
        raise ValueError('un conteo de estrellas no es negativo: %r' % n)
    if n < 1000:
        return ('EXACTO', str(n), 0)
    if n >= 1000000:
        return ('NO-MEDIDA', None, None)

    # redondear PRIMERO, elegir banda despues
    if n < 100000:
        centro = int(round(n / 100.0)) * 100
        if centro < 100000:
            banda = 'K-2CIFRAS' if centro < 10000 else 'K-3CIFRAS'
            return (banda, '%.1fk' % (centro / 1000.0), 50)
        # el redondeo cruzo a la banda de millares
    centro = int(round(n / 1000.0)) * 1000
    if centro >= 1000000:
        return ('NO-MEDIDA', None, None)
    return ('K-ENTERO', '%dk' % (centro // 1000), 500)


def entero_publicable(n):
    """La regla operativa en una linea: un ENTERO EXACTO de estrellas solo es
    publicable por debajo de 1.000. Arriba es magnitud con banda nombrada."""
    return precision_publicable(n)[0] == 'EXACTO'
