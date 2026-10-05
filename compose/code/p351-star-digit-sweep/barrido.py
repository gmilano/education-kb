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

# 🆕 `P376` (pase 115): este arbol atribuye un pase con DOS portadores, y este modulo
# reconocia UNO. El otro es la linea de resumen `> **Pase N del FECHA:** ...`, que es como
# los ocho `.md` atribuyen la mayor parte de su prosa — y que se AUTO-atribuye: cada linea
# dice su propio pase y no abre una seccion, porque los bloques de esas lineas van en orden
# DESCENDENTE (115, 114, 113 …) y tratarlos como aperturas invertiria todo lo de abajo.
#
# 🔴 El costo de la omision es exactamente la recurrencia de `P359`, tres pases seguidos:
# al ser el encabezado `#` el unico marcador reconocido, una seccion nueva arriba ANEXABA
# la prosa de todos los pases viejos que vinieran despues. En el pase 115 eso puso las
# «385.407 ★» del pase **56** —una linea que dice «Pase 56 del 2026-10-03» en su propio
# texto— a nombre del pase 115.
#
# 🔵 El arreglo respeta la estructura del archivo y no el instrumento (que es lo que `P359`
# pedia): la linea se atribuye a lo que ELLA MISMA declara.
RE_LINEA_DE_PASE = re.compile(r'^>\s*\*\*Pase (\d+) del ', re.IGNORECASE)

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


def _pase_de(linea, marcas, texto=None):
    """El pase al que pertenece una linea.

    Precedencia: si la linea ES una linea de resumen de pase, se atribuye a SI MISMA
    (`P376`); si no, al ultimo encabezado `#` con numero de pase que la precede.
    """
    if texto is not None:
        m = RE_LINEA_DE_PASE.match(texto)
        if m:
            return int(m.group(1))
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


# 🆕 `P359` (pase 112): una TERCERA clase que ni el clasificador lexico ni el estructural
# tenian. Una cifra puede aparecer como el BORDE DE UNA BANDA -«por debajo de 1.000 ★»,
# «1.000-9.999»- y entonces no es el dato de ningun repo ni la cita de un dato: es una
# UNIDAD. El barrido la contaba como cifra publicada y la atribuia a un repo inexistente.
# Lo encontro la publicacion del pase 112: la tabla de bandas de `P349` que el pase 111
# escribio quedo debajo de una seccion nueva y salio como «defecto del pase 112».
MARCAS_UMBRAL = ('por debajo de', 'por encima de', 'banda', 'menos de', 'mas de',
                 'arriba de', 'abajo de', 'umbral', 'cota')


def es_umbral(texto, pos=None):
    """La cifra es el BORDE de una banda, no la medicion de un repo.

    Senal estructural: cae en una celda que declara un RANGO (`1.000-9.999`, `< 1.000`,
    `>= 100.000`). Senal lexica: la linea habla de la banda y no de un repo.
    """
    bajo = texto.lower()
    if any(m in bajo for m in MARCAS_UMBRAL):
        return True
    if pos is not None:
        ventana = texto[max(0, pos - 12):pos + 24]
        if re.search(r'[<>≥≤]\s*\d|\d[\.\d]*\s*[-–—]\s*\d', ventana):
            return True
    return False


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
                out.append((rel, i, m.group(0).strip(), _pase_de(i, marcas, lineas[i - 1]),
                            es_meta_mencion(l, m.start()), es_umbral(l, m.start())))
    return out


def resumen(hits):
    return {
        'ocurrencias': len(hits),
        'valores_distintos': len({h[2] for h in hits}),
        'archivos': len({h[0] for h in hits}),
        'por_archivo': collections.Counter(h[0] for h in hits),
        'en_catalogo': sum(1 for h in hits if h[3] is None),
        'meta_menciones': sum(1 for h in hits if h[4]),
        'umbrales': sum(1 for h in hits if len(h) > 5 and h[5]),
        'pase_maximo': max((h[3] for h in hits if h[3] is not None), default=None),
    }


def posteriores_a(hits, pase):
    """Las ramas de refutacion de la accion B: ocurrencias de un pase POSTERIOR,
    excluidas las meta-menciones y los UMBRALES (que no son el dato de ningun repo).

    ⚠️ LIMITE DECLARADO del atribuidor (`P359`, pase 112): `_pase_de` asigna por POSICION
    -el encabezado de pase mas cercano hacia arriba-. En un archivo *newest-first* la
    posicion NO codifica la autoria: insertar la seccion de un pase nuevo ARRIBA
    re-atribuye a ese pase todas las lineas que queden debajo hasta el proximo
    encabezado. Por eso esta funcion NO puede sostener sola un enunciado sobre QUE PASE
    publico una cifra, y la suite prueba el limite en vez de taparlo.
    """
    return [h for h in hits if h[3] is not None and h[3] > pase
            and not h[4] and not (len(h) > 5 and h[5])]


def atribucion_es_ambigua(hits, pase):
    """Las ocurrencias cuya atribucion a `pase` viene de la POSICION y no del texto.

    Son las que caen en la ventana entre el encabezado mas nuevo y el siguiente: un
    archivo *newest-first* las re-atribuye con cada publicacion.
    """
    return [h for h in hits if h[3] == pase]


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
