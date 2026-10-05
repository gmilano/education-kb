#!/usr/bin/env python3
"""`P351` — un barrido por una cifra PUBLICADA no distingue el dato de la CITA que lo refuta.

La accion B pre-registrada por el pase 110 pedia barrer los `.md` de este arbol buscando toda
cifra de estrellas con **4 o mas digitos exactos** y contarlas, con prediccion **>=20** y dos
ramas de refutacion: que sean **<20**, o que **alguna** sea posterior al pase 110.

Veredicto: **CONFIRMADA en el conteo** (254 ocurrencias, 40 valores distintos, 8 archivos) y
**ninguna posterior al pase 110**, asi que la regla que el pase 110 escribio no se violo.

🔴 **Pero el instrumento tiene un punto ciego propio, y lo destapa su propio resultado:** dos
de las ocurrencias caen DENTRO de la seccion del pase 110, y las dos son META-MENCIONES — el
pase 110 citando «385.407 ★» para refutarla, y el texto de la pre-registracion de la accion B
citandola como ejemplo de lo que hay que buscar. **Un `grep` por la cifra las cuenta igual que
un dato.**

Consecuencia de metodo: **254 SOBREESTIMA el defecto.** Lo que hay que arreglar no son 254
ocurrencias: son los **40 valores distintos** y, sobre todo, las **27 que viven en la region de
CATALOGO** (antes de cualquier encabezado de pase), que es la unica region que un lector lee
como dato vigente. Una cifra citada para refutarla es el registro FUNCIONANDO, no el defecto.

Es la forma inversa de `P344`: ahi el denominador excluia los casos que importaban; aca el
denominador INCLUYE casos que no son el defecto.
"""
import collections, os, re

# `385.407 ★`, `108.128 ★`, `1.074 ★` — separador de millar, 4+ digitos en total
RE_CIFRA = re.compile(r'[0-9]{1,3}[.,][0-9]{3}(?:\.[0-9]{3})* ?★')
RE_ENCABEZADO_PASE = re.compile(r'pase (\d+)')

ARCHIVOS = ('agents/top.md', 'agents/trending.md', 'repos/foundations.md', 'repos/trending.md',
            'verticals/solutions.md', 'intel/market.md', 'intel/trends.md',
            'compose/patterns.md')

# 🔴 La PRIMERA version de este clasificador era LEXICA: una lista de palabras que suelen
# aparecer cuando una linea cita una cifra en vez de publicarla. El pase 111 la rompio con su
# PROPIO texto -3 citas que la lista no cubria- y el arreglo no es alargar la lista: es `P354`
# otra vez (un ancla que reconoce una ORTOGRAFIA y no un OBJETO). La senal robusta es
# ESTRUCTURAL: en este arbol una cifra CITADA va entre comillas latinas o en codigo inline,
# y una cifra PUBLICADA va desnuda en prosa o en una celda de tabla.
DELIMITADORES_DE_CITA = (('\u00ab', '\u00bb'), ('`', '`'))

# La lista lexica se conserva como senal SECUNDARIA, para la cita que no lleva delimitador.
MARCAS_META = ('no son reproducibles', 'no reproducibles', 'del tipo', 'refuta', 'inflado',
               'cifra sin canal', 'NO MEDIBLE', 'pipeline-inflated', 'sobreestima')


def _limites_de_pase(lineas):
    """numero de linea -> pase al que pertenece. `None` = region de CATALOGO."""
    marcas = []
    for i, l in enumerate(lineas, 1):
        if l.startswith('#'):
            m = RE_ENCABEZADO_PASE.search(l)
            if m:
                marcas.append((i, int(m.group(1))))
    return marcas


def _pase_de(linea, marcas):
    p = None
    for ln, num in marcas:
        if ln <= linea:
            p = num
        else:
            break
    return p


def _tramos_de_cita(texto):
    """Rangos [inicio, fin) encerrados por un delimitador de cita."""
    tramos = []
    for ab, ce in DELIMITADORES_DE_CITA:
        i = 0
        while True:
            a = texto.find(ab, i)
            if a < 0:
                break
            c = texto.find(ce, a + len(ab))
            if c < 0:
                break
            tramos.append((a, c + len(ce)))
            i = c + len(ce)
    return tramos


def es_meta_mencion(texto, pos=None):
    """La linea CITA la cifra (para refutarla o ejemplificarla) en vez de publicarla.

    Senal PRIMARIA (estructural): la cifra cae dentro de un tramo entre comillas latinas
    o en codigo inline. Senal SECUNDARIA (lexica): la linea trae una marca de refutacion.
    """
    if pos is not None:
        for a, c in _tramos_de_cita(texto):
            if a <= pos < c:
                return True
    bajo = texto.lower()
    return any(m.lower() in bajo for m in MARCAS_META)


def barrer(raiz, archivos=ARCHIVOS):
    """-> lista de (archivo, linea, valor, pase, es_meta)."""
    out = []
    for rel in archivos:
        path = os.path.join(raiz, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as fh:
            lineas = fh.readlines()
        marcas = _limites_de_pase(lineas)
        for i, l in enumerate(lineas, 1):
            for m in RE_CIFRA.finditer(l):
                out.append((rel, i, m.group(0).strip(), _pase_de(i, marcas),
                            es_meta_mencion(l, m.start())))
    return out


def resumen(hits):
    return {
        'ocurrencias': len(hits),
        'valores_distintos': len({h[2] for h in hits}),
        'archivos': len({h[0] for h in hits}),
        'por_archivo': collections.Counter(h[0] for h in hits),
        'en_catalogo': sum(1 for h in hits if h[3] is None),
        'meta_menciones': sum(1 for h in hits if h[4]),
        'pase_maximo': max((h[3] for h in hits if h[3] is not None), default=None),
    }


def posteriores_a(hits, pase):
    """Las ramas de refutacion de la accion B: ocurrencias de un pase POSTERIOR,
    excluidas las meta-menciones (que no son el dato)."""
    return [h for h in hits if h[3] is not None and h[3] > pase and not h[4]]


if __name__ == '__main__':
    import sys
    raiz = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
    hits = barrer(raiz)
    r = resumen(hits)
    print('=== ACCION B: cifras de estrellas con 4+ digitos exactos ===')
    print('ocurrencias        %d   (la prediccion pedia >= 20)' % r['ocurrencias'])
    print('valores distintos  %d' % r['valores_distintos'])
    print('archivos           %d' % r['archivos'])
    print()
    print('=== por archivo ===')
    for a, n in r['por_archivo'].most_common():
        print('%-26s %4d' % (a, n))
    print()
    print('region de CATALOGO (dato vigente)  %d' % r['en_catalogo'])
    print('META-MENCIONES (cita, no dato)     %d' % r['meta_menciones'])
    print('pase mas alto con una ocurrencia   %s' % r['pase_maximo'])
    print()
    post = posteriores_a(hits, 110)
    print('posteriores al pase 110, sin contar meta-menciones: %d' % len(post))
    for h in post:
        print('   %s:%d  %s  (pase %s)' % (h[0], h[1], h[2], h[3]))
    print()
    print('=== valores mas repetidos ===')
    for v, n in collections.Counter(h[2] for h in hits).most_common(8):
        print('%-14s %4d' % (v, n))
