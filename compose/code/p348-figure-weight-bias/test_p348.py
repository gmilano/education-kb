#!/usr/bin/env python3
"""Suite de `P348`. El control que la vuelve medible es de RESPUESTA CONOCIDA:
el mismo instrumento tiene que reproducir el 1.418/2.443 del pase 110 AL ENTERO.
Si eso falla, la comparacion no es con el pase 110 y el hallazgo no existe."""
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sesgo
from sesgo import (cargar_censo, cargar_figuras, clasificar, factor_de_sesgo,
                   figuras_por_unidad, informe, tasa, tasa_por_figura)

CENSO = cargar_censo()
FIGURAS = cargar_figuras()


class ControlDeRespuestaConocida(unittest.TestCase):
    """Sin estas, el resto de la suite mide otra cosa."""

    def test_el_censo_tiene_las_13371(self):
        self.assertEqual(len(CENSO), 13371)

    def test_el_corte_tiene_las_2443_figuras(self):
        self.assertEqual(len(FIGURAS), 2443)

    def test_las_figuras_viven_en_1586_unidades(self):
        self.assertEqual(len(set(FIGURAS)), 1586)

    def test_REPLICA_el_58_por_ciento_del_pase_110_AL_ENTERO(self):
        """🟢 El control que ata este pase al 110: 1.418 de 2.443."""
        res, tot, pc = tasa_por_figura(FIGURAS, CENSO)
        self.assertEqual(res, 1418)
        self.assertEqual(tot, 2443)
        self.assertAlmostEqual(pc, 58.0, places=1)

    def test_toda_figura_tiene_su_unidad_en_el_censo(self):
        """Si una figura no resuelve a una unidad, su clase saldria `AUSENTE`
        por un hueco de JOIN y no por una ausencia de cesion."""
        self.assertEqual([p for p in set(FIGURAS) if p not in CENSO], [])


class AccionCRefutada(unittest.TestCase):

    def test_la_tasa_del_corpus_SUBE_no_baja(self):
        """La prediccion pedia «por debajo de 58,0 %». Medido: 76,4 %."""
        res, tot, pc = tasa(list(CENSO), CENSO)
        self.assertEqual(res, 10210)
        self.assertEqual(tot, 13371)
        self.assertAlmostEqual(pc, 76.4, places=1)
        self.assertGreater(pc, 58.0 + 2.0, 'la rama de refutacion pedia subir mas de 2 pp')

    def test_tener_figura_es_predictor_NEGATIVO(self):
        """El razonamiento de la pre-registracion estaba al reves."""
        _, _, con = tasa([u for u in CENSO if u in set(FIGURAS)], CENSO)
        _, _, sin = tasa([u for u in CENSO if u not in set(FIGURAS)], CENSO)
        self.assertLess(con, sin)
        self.assertAlmostEqual(con, 63.4, places=1)
        self.assertAlmostEqual(sin, 78.1, places=1)

    def test_la_capa_con_figura_en_su_propia_unidad_es_63_4_no_58_0(self):
        """Los 5,3 pp que separan 58,0 de 63,4 son FORMA DEL DENOMINADOR."""
        _, _, por_unidad = tasa([u for u in CENSO if u in set(FIGURAS)], CENSO)
        _, _, por_figura = tasa_por_figura(FIGURAS, CENSO)
        self.assertAlmostEqual(por_unidad - por_figura, 5.3, places=1)

    def test_la_comparacion_commensurable_es_13_pp_no_18_4(self):
        """Lo que se puede llevar a una reunion: la capa con figura esta
        13,0 pp peor que el corpus, no 18,4."""
        _, _, corpus = tasa(list(CENSO), CENSO)
        _, _, con = tasa([u for u in CENSO if u in set(FIGURAS)], CENSO)
        self.assertAlmostEqual(corpus - con, 13.0, places=1)


class ElMecanismoMedido(unittest.TestCase):

    def test_las_mal_cedidas_cargan_mas_figuras(self):
        fpu = figuras_por_unidad(FIGURAS, CENSO)
        self.assertAlmostEqual(fpu['RESOLUBLE'][2], 1.411, places=3)
        self.assertGreater(fpu['AUSENTE'][2], fpu['RESOLUBLE'][2])
        self.assertGreater(fpu['VERSION-SIN-VARIANTE'][2], fpu['RESOLUBLE'][2])

    def test_la_PEOR_cubeta_es_la_MAS_pesada(self):
        """`NO-ES-CESION` -una URL de fuente, que no concede nada- carga mas del
        DOBLE de figuras por unidad. Es el nucleo del sesgo."""
        fpu = figuras_por_unidad(FIGURAS, CENSO)
        self.assertAlmostEqual(fpu['NO-ES-CESION'][2], 3.021, places=3)
        self.assertGreater(fpu['NO-ES-CESION'][2], 2 * fpu['RESOLUBLE'][2])

    def test_factor_de_sesgo_25_por_ciento(self):
        self.assertAlmostEqual(factor_de_sesgo(FIGURAS, CENSO), 1.250, places=3)

    def test_el_sesgo_EXPLICA_el_signo_de_la_brecha(self):
        """Factor > 1 y tasa por figura < tasa por unidad tienen que ir juntos:
        si el factor fuera < 1 la brecha cambiaria de signo."""
        f = factor_de_sesgo(FIGURAS, CENSO)
        _, _, por_unidad = tasa([u for u in CENSO if u in set(FIGURAS)], CENSO)
        _, _, por_figura = tasa_por_figura(FIGURAS, CENSO)
        self.assertGreater(f, 1.0)
        self.assertLess(por_figura, por_unidad)


class ControlesNegativos(unittest.TestCase):

    def test_NEGATIVE_censo_vacio_no_inventa_tasa(self):
        self.assertEqual(tasa([], {}), (0, 0, 0.0))
        self.assertEqual(tasa_por_figura([], {}), (0, 0, 0.0))

    def test_NEGATIVE_unidad_fuera_del_censo_no_cuenta_como_resoluble(self):
        """Un `problem_id` que no existe no puede salir `RESOLUBLE`: si saliera,
        un hueco de JOIN se publicaria como cesion."""
        res, tot, _ = tasa(['no-existe-p111'], CENSO)
        self.assertEqual(res, 0)
        self.assertEqual(tot, 1)

    def test_NEGATIVE_sin_figuras_el_factor_es_None_no_1(self):
        """Sin la capa de figura el factor no esta definido. Devolver 1,0
        diria «no hay sesgo», que es una afirmacion, no una ausencia."""
        self.assertIsNone(factor_de_sesgo([], CENSO))

    def test_NEGATIVE_todas_resolubles_no_define_factor(self):
        """Si no hay unidades no-resolubles no hay con que comparar."""
        falso = {'a': ('https://creativecommons.org/licenses/by/4.0/', '')}
        self.assertIsNone(factor_de_sesgo(['a', 'a'], falso))

    def test_NEGATIVE_reusa_el_clasificador_de_p345_no_una_copia(self):
        """🔴 Si este modulo reescribiera `clasificar`, la comparacion con el
        58,0 % seria por una tercera via y no mediria lo que dice medir."""
        import importlib.util
        ruta = os.path.join(HERE, '..', 'p345-oer-four-forms', 'entregabilidad.py')
        self.assertTrue(os.path.exists(ruta))
        spec = importlib.util.spec_from_file_location('p345_check', ruta)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        # 🔵 Dos cargas del mismo fuente dan objetos de codigo DISTINTOS, asi que
        # `assertIs` sobre `__code__` es falso aunque no haya copia. Lo que afirma
        # «no es una copia» es la PROCEDENCIA: mismo archivo, misma linea.
        self.assertEqual(os.path.realpath(clasificar.__code__.co_filename),
                         os.path.realpath(mod.clasificar.__code__.co_filename))
        self.assertEqual(clasificar.__code__.co_firstlineno,
                         mod.clasificar.__code__.co_firstlineno)
        self.assertEqual(os.path.realpath(clasificar.__code__.co_filename),
                         os.path.realpath(ruta))
        for caso in ('https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>',
                     'CC4.0', 'https://ds100.org/su26/past-exams/', '', 'openstax'):
            self.assertEqual(clasificar(caso), mod.clasificar(caso), 'divergen en %r' % caso)

    def test_el_modulo_de_p345_es_importable_SIN_tmp(self):
        """🟢 Control de `P352`: importarlo no puede depender de una ruta efimera."""
        import importlib.util
        ruta = os.path.join(HERE, '..', 'p345-oer-four-forms', 'entregabilidad.py')
        spec = importlib.util.spec_from_file_location('p345_import_check', ruta)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)   # no debe levantar FileNotFoundError
        self.assertTrue(callable(mod.clasificar))


class InformeCompleto(unittest.TestCase):

    def test_informe_trae_las_cinco_cifras(self):
        r = informe(CENSO, FIGURAS)
        self.assertAlmostEqual(r['corpus'][2], 76.4, places=1)
        self.assertAlmostEqual(r['con_figura'][2], 63.4, places=1)
        self.assertAlmostEqual(r['sin_figura'][2], 78.1, places=1)
        self.assertAlmostEqual(r['por_figura'][2], 58.0, places=1)
        self.assertAlmostEqual(r['factor_de_sesgo'], 1.250, places=3)

    def test_las_unidades_parten_en_dos_sin_solape(self):
        r = informe(CENSO, FIGURAS)
        self.assertEqual(r['con_figura'][1] + r['sin_figura'][1], r['corpus'][1])
        self.assertEqual(r['con_figura'][0] + r['sin_figura'][0], r['corpus'][0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
