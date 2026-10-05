#!/usr/bin/env python3
"""Suite de `P351`. Controles de respuesta conocida sobre el arbol real, y
controles negativos sobre texto sintetico."""
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import barrido as B
from barrido import (RE_CIFRA, _limites_de_pase, _pase_de, barrer, es_meta_mencion,
                     posteriores_a, resumen)

HITS = barrer(RAIZ)
R = resumen(HITS)


class AccionBConfirmadaEnElConteo(unittest.TestCase):

    def test_la_prediccion_pedia_20_y_hay_muchas_mas(self):
        """🔵 La cota se asevera, no el conteo exacto: el arbol CRECE cada pase y
        congelar `== 254` haria fallar esta suite por una edicion de prosa, que es
        justo el modo de falla de `P352`. Medido en el pase 111: 262."""
        self.assertGreaterEqual(R['ocurrencias'], 20)
        self.assertGreaterEqual(R['ocurrencias'], 254)

    def test_hay_decenas_de_valores_distintos(self):
        """La cifra que importa para arreglarlo: no son 262 ediciones.
        Medido en el pase 111: 42 valores distintos."""
        self.assertGreaterEqual(R['valores_distintos'], 40)
        self.assertLess(R['valores_distintos'], R['ocurrencias'])

    def test_los_ocho_archivos_estan_tocados(self):
        self.assertEqual(R['archivos'], 8)

    def test_ninguna_es_POSTERIOR_al_pase_110(self):
        """🟢 La segunda rama de refutacion NO dispara: la regla que el pase 110
        escribio no se violo en el 111."""
        self.assertEqual(posteriores_a(HITS, 110), [])

    def test_las_seis_del_eje_generalista_dominan(self):
        import collections
        top = dict(collections.Counter(h[2] for h in HITS).most_common(6))
        for v in ('385.407 ★', '151.639 ★', '108.128 ★', '62.735 ★', '60.284 ★', '55.226 ★'):
            self.assertIn(v, top, 'falta %s entre las 6 mas repetidas' % v)


class ElPuntoCiegoDelInstrumento(unittest.TestCase):

    def test_hay_META_MENCIONES_contadas_como_dato(self):
        """🔴 El hallazgo de `P351`: el barrido cuenta la cita igual que el dato."""
        self.assertGreater(R['meta_menciones'], 0)

    def test_la_region_de_CATALOGO_es_la_que_importa(self):
        """Las que viven donde un lector las lee como vigentes.
        Medido en el pase 111: 31 de 262."""
        self.assertGreater(R['en_catalogo'], 0)
        self.assertLess(R['en_catalogo'], R['ocurrencias'] // 2)

    def test_el_conteo_crudo_SOBREESTIMA_el_defecto(self):
        """El defecto real esta acotado por catalogo + distintos, no por ocurrencias."""
        self.assertLess(R['en_catalogo'], R['ocurrencias'])
        self.assertLess(R['valores_distintos'], R['ocurrencias'])

    def test_una_pre_registracion_atribuye_a_un_pase_FUTURO(self):
        """🔵 Nuance del atribuidor: un encabezado «Acciones pre-registradas para
        el pase N» hace que una linea caiga en un pase que todavia NO corrio.
        Por eso la rama de refutacion se evalua EXCLUYENDO meta-menciones.

        🔴 `P359` (pase 112): la version del pase 111 afirmaba `pase_maximo == 111`,
        o sea CLAVABA el numero del pase que la escribio, y por construccion fallaba en
        el pase siguiente. Es la familia de `P352`/`P355` en un tercer eje: una suite
        que solo pasa en el PASE que la escribio. El invariante no es el valor del
        maximo —ese crece— sino que TODO lo atribuido al maximo sea meta-mencion o
        umbral, que es lo que el docstring siempre quiso decir."""
        self.assertIsNotNone(R['pase_maximo'])
        self.assertGreaterEqual(R['pase_maximo'], 111)
        futuras = B.atribucion_es_ambigua(HITS, R['pase_maximo'])
        self.assertTrue(futuras)
        for h in futuras:
            self.assertTrue(h[4] or (len(h) > 5 and h[5]),
                            'ocurrencia atribuida al pase %s que no es meta ni umbral: %r'
                            % (R['pase_maximo'], h))


class UmbralNoEsMedicion(unittest.TestCase):
    """`P359` — el borde de una banda no es el dato de ningun repo."""

    def test_por_debajo_de_mil_es_umbral(self):
        self.assertTrue(B.es_umbral('vive por debajo de 1.000 ★', 20))

    def test_celda_de_rango_es_umbral(self):
        self.assertTrue(B.es_umbral('| `K-2CIFRAS` | 1.000–9.999 | `7.5k` |', 16))

    def test_NEGATIVE_una_cifra_de_repo_NO_es_umbral(self):
        """El control que impide que la clase nueva se coma el defecto que el
        instrumento existe para encontrar: `385.407 ★` desnudo en una celda de
        catalogo sigue siendo una cifra PUBLICADA."""
        self.assertFalse(B.es_umbral('| OpenClaw | MIT | 385.407 ★ |', 20))

    def test_NEGATIVE_una_cita_no_se_reclasifica_como_umbral(self):
        self.assertFalse(B.es_umbral('el pase 110 citando «385.407 ★»', 22))

    def test_el_umbral_queda_fuera_de_la_rama_de_refutacion(self):
        """La consecuencia medida: con la clase nueva, `posteriores_a(110)` vuelve a 0.
        Sin ella, la tabla de bandas de `P349` que escribio el pase 111 salia como
        defecto del pase 112 por haber quedado debajo de una seccion nueva."""
        self.assertEqual(B.posteriores_a(HITS, 110), [])
        self.assertGreater(R['umbrales'], 0)


class ClasificadorDeMetaMencion(unittest.TestCase):

    def test_reconoce_la_cita_que_refuta(self):
        self.assertTrue(es_meta_mencion(
            'los enteros exactos («385.407 ★») no son reproducibles por este canal'))

    def test_reconoce_el_ejemplo_de_la_pre_registracion(self):
        self.assertTrue(es_meta_mencion(
            'cifra de estrellas publicada con 4 o mas digitos exactos (del tipo `385.407 ★`)'))

    def test_NEGATIVE_una_fila_de_tabla_NO_es_meta_mencion(self):
        """Una fila que publica la cifra como dato tiene que contar como defecto."""
        self.assertFalse(es_meta_mencion('| openclaw | MIT | 385.407 ★ | TypeScript |'))

    def test_NEGATIVE_prosa_que_la_publica_NO_es_meta_mencion(self):
        self.assertFalse(es_meta_mencion(
            'el barrido devolvio el eje generalista: openclaw 385.407 ★, dify 151.639 ★'))


class ElRegexYLaAtribucion(unittest.TestCase):

    def test_atrapa_cuatro_digitos_con_separador(self):
        self.assertTrue(RE_CIFRA.search('1.074 ★'))
        self.assertTrue(RE_CIFRA.search('385.407 ★'))

    def test_NEGATIVE_no_atrapa_tres_digitos(self):
        """🔴 Por esto el 265 de `OATutor` NUNCA entro en el denominador de la
        accion B: tiene 3 digitos. El defecto de propagacion se encontro por
        otra via, no por este barrido."""
        self.assertIsNone(RE_CIFRA.search('265 ★'))
        self.assertIsNone(RE_CIFRA.search('264 ★'))

    def test_NEGATIVE_no_atrapa_cifra_sin_estrella(self):
        self.assertIsNone(RE_CIFRA.search('13.371 unidades'))

    def test_atribucion_region_de_catalogo_es_None(self):
        lineas = ['# titulo\n', '| x | 1.234 ★ |\n', '## pase 9 del hoy\n', '1.234 ★\n']
        marcas = _limites_de_pase(lineas)
        self.assertIsNone(_pase_de(2, marcas))
        self.assertEqual(_pase_de(4, marcas), 9)

    def test_NEGATIVE_encabezado_sin_pase_no_abre_seccion(self):
        lineas = ['## Otra cosa\n', '1.234 ★\n']
        self.assertEqual(_limites_de_pase(lineas), [])
        self.assertIsNone(_pase_de(2, []))

    def test_NEGATIVE_arbol_vacio_no_inventa_hits(self):
        self.assertEqual(barrer(RAIZ, archivos=('NO-EXISTE-p351.md',)), [])

class ClasificadorESTRUCTURAL(unittest.TestCase):
    """🔴 Regresion del defecto que el pase 111 se hizo A SI MISMO.

    La primera version de `es_meta_mencion` era LEXICA (una lista de palabras) y el
    texto de este mismo pase la rompio: tres citas claras quedaron contadas como
    dato porque no traian ninguna de las palabras de la lista. El arreglo no fue
    alargar la lista -eso es `P354`, un ancla que reconoce una ORTOGRAFIA- sino usar
    la senal ESTRUCTURAL: en este arbol una cifra citada va entre comillas latinas
    o en codigo inline."""

    def test_comillas_latinas_marcan_cita(self):
        linea = 'pase 110 citando \u00ab385.407 \u2605\u00bb precisamente para decir que no'
        self.assertTrue(es_meta_mencion(linea, linea.index('385')))

    def test_codigo_inline_marca_cita(self):
        linea = 'con 4 o mas digitos exactos (del tipo `385.407 \u2605`) y contarlas'
        self.assertTrue(es_meta_mencion(linea, linea.index('385')))

    def test_las_TRES_lineas_que_rompieron_la_version_lexica(self):
        """Las tres del pase 111, verbatim en su forma relevante."""
        casos = [
            'pase 110 citando \u00ab385.407 \u2605\u00bb precisamente para decir que no es reproducible, y el texto de la',
            '(\u00ab385.407 \u2605\u00bb) que **ningun canal de este entorno reproduce**, y el pase 110 los reemplazo',
            'Apache-2.0 leida del payload\u00bb es defendible. \U0001f534 \u00abDeepTutor, 40.823 \u2605\u00bb no lo es, y es la forma',
        ]
        for linea in casos:
            pos = RE_CIFRA.search(linea).start()
            self.assertTrue(es_meta_mencion(linea, pos), 'no clasificada: %r' % linea[:50])

    def test_NEGATIVE_cifra_DESNUDA_en_prosa_no_es_cita(self):
        linea = 'el barrido devolvio el eje generalista: openclaw 385.407 \u2605, dify 151.639 \u2605'
        self.assertFalse(es_meta_mencion(linea, linea.index('385')))

    def test_NEGATIVE_cifra_en_CELDA_de_tabla_no_es_cita(self):
        linea = '| openclaw | MIT | 385.407 \u2605 | TypeScript |'
        self.assertFalse(es_meta_mencion(linea, linea.index('385')))

    def test_NEGATIVE_una_cita_en_OTRA_parte_de_la_linea_no_contagia(self):
        """\U0001f534 El control mas fino: si la linea tiene un tramo citado pero la
        cifra esta FUERA de el, la cifra es dato. Sin la posicion, el clasificador
        contagiaria toda la linea."""
        linea = 'la regla de \u00abmagnitud con canal\u00bb no se aplico y quedo 385.407 \u2605 en la fila'
        self.assertFalse(es_meta_mencion(linea, linea.index('385')))

    def test_compatibilidad_sin_posicion_usa_la_senal_lexica(self):
        """Llamada sin `pos`, sigue valiendo la lista de marcas."""
        self.assertTrue(es_meta_mencion('la cifra no son reproducibles por este canal'))
        self.assertFalse(es_meta_mencion('| openclaw | 385.407 \u2605 |'))



class P376DosPortadoresDeAtribucion(unittest.TestCase):
    """🆕 `P376` (pase 115) - este arbol atribuye un pase con DOS portadores.

    🔴 El modulo reconocia solo el encabezado `#`, y por eso `P359` se repitio TRES
    pases seguidos: una seccion nueva arriba ANEXABA la prosa de los pases viejos de mas
    abajo. En el pase 115 eso puso las «385.407 ★» del pase **56** a nombre del
    115 - sobre una linea que dice «Pase 56 del 2026-10-03» en su propio texto.

    🔵 El arreglo respeta la estructura del archivo y no el instrumento: la linea
    se atribuye a lo que ELLA MISMA declara.
    """

    def test_la_linea_de_resumen_se_atribuye_A_SI_MISMA(self):
        linea = ('> **Pase 56 del 2026-10-03:** cero repos nuevos y el barrido volvio con '
                 'las cifras identicas (openclaw **385.407 ★**)')
        self.assertEqual(_pase_de(99, [(1, 115)], linea), 56)

    def test_sin_portador_de_linea_vale_el_encabezado(self):
        self.assertEqual(_pase_de(99, [(1, 115)], 'prosa comun con 385.407 ★'), 115)

    def test_NEGATIVE_un_bloque_de_lineas_NO_abre_seccion(self):
        """🔴 El caso que prohibe el arreglo obvio.

        Los bloques de lineas de resumen van en orden DESCENDENTE (115, 114, 113 ...), asi
        que tratarlas como APERTURAS de seccion atribuiria todo lo de abajo al pase MAS
        VIEJO del bloque. La linea se auto-atribuye y no abre nada.
        """
        vieja = '> **Pase 99 del 2026-10-04:** 7 altas fundacionales'
        self.assertEqual(_pase_de(26, [(1, 115)], vieja), 99)
        self.assertEqual(_pase_de(27, [(1, 115)], 'prosa de la seccion del 115'), 115)

    def test_NEGATIVE_una_cita_del_titulo_en_prosa_no_atribuye(self):
        self.assertIsNone(
            _pase_de(5, [], 'el pase dejo escrito **Pase 56 del** adentro de la prosa'))

    def test_el_arbol_real_ya_no_atribuye_al_115_lo_que_es_del_56(self):
        malas = [h for h in HITS
                 if h[3] == 115 and not (h[4] or (len(h) > 5 and h[5]))]
        self.assertEqual(malas, [], 'ocurrencias publicadas a nombre del pase 115')


if __name__ == '__main__':
    unittest.main(verbosity=2)
