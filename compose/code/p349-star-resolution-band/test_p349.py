#!/usr/bin/env python3
"""Suite de `P349`. Cada banda lleva su TESTIGO MEDIDO del pase 111, y cada
clase lleva su control negativo."""
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from banda import leer_render, precision_publicable, entero_publicable


class TestigosMedidos(unittest.TestCase):
    """Los cinco repos medidos por `WebFetch` el 2026-10-05, pase 111.
    Si una de estas falla, el canal CAMBIO de formato y el enunciado de
    `P349` hay que re-medirlo, no parchearlo."""

    def test_oatutor_264_es_exacto(self):
        """`CAHLR/OATutor` -> `264`. Debajo de 1.000 el canal NO redondea."""
        self.assertEqual(leer_render('264'), ('EXACTO', 264, 264))

    def test_open_tutor_ai_ce_107_es_exacto(self):
        """`Open-TutorAi/open-tutor-ai-CE` -> `107`."""
        self.assertEqual(leer_render('107'), ('EXACTO', 107, 107))

    def test_moodle_7_5k_son_DOS_cifras(self):
        """`moodle/moodle` -> `7.5k`. ESTE es el testigo que refuta al pase 110:
        dos cifras significativas, no tres."""
        self.assertEqual(leer_render('7.5k'), ('K-2CIFRAS', 7450, 7550))

    def test_deeptutor_40_8k_son_TRES_cifras(self):
        """`HKUDS/DeepTutor` -> `40.8k`. La unica banda donde el pase 110 acertaba."""
        self.assertEqual(leer_render('40.8k'), ('K-3CIFRAS', 40750, 40850))

    def test_browser_use_117k_es_millar(self):
        """`browser-use/browser-use` -> `117k`. Peor cota ABSOLUTA: +/-500."""
        self.assertEqual(leer_render('117k'), ('K-ENTERO', 116500, 117500))


class LaCotaEsUnEscalon(unittest.TestCase):

    def test_el_pase_110_erraba_por_DEBAJO(self):
        """3 cifras significativas sobre 264 daria `264` — pero el enunciado
        del pase 110 negaba el entero exacto. Debajo de 1.000 la cota es CERO."""
        banda, lo, hi = leer_render('264')
        self.assertEqual(lo, hi)
        self.assertEqual(hi - lo, 0)

    def test_el_pase_110_erraba_por_ARRIBA(self):
        """En la banda 1.000-9.999 el canal da DOS cifras, no tres:
        `7.5k` no distingue 7.450 de 7.550."""
        _, lo, hi = leer_render('7.5k')
        self.assertEqual(hi - lo, 100)

    def test_peor_error_RELATIVO_al_pie_de_la_banda_k(self):
        """La cota relativa es maxima donde el canal cambia de forma."""
        _, lo, hi = leer_render('1.0k')
        rel_pie = (hi - lo) / 2.0 / 1000.0
        _, lo2, hi2 = leer_render('9.9k')
        rel_techo = (hi2 - lo2) / 2.0 / 9900.0
        self.assertGreater(rel_pie, rel_techo)
        self.assertAlmostEqual(rel_pie, 0.05, places=3)

    def test_peor_error_ABSOLUTO_arriba(self):
        """+/-500 en la banda de millares contra +/-50 en las de centenas."""
        self.assertEqual((leer_render('117k')[2] - leer_render('117k')[1]) / 2, 500)
        self.assertEqual((leer_render('40.8k')[2] - leer_render('40.8k')[1]) / 2, 50)


class PrecisionPublicable(unittest.TestCase):

    def test_entero_exacto_solo_debajo_de_mil(self):
        self.assertTrue(entero_publicable(264))
        self.assertTrue(entero_publicable(999))
        self.assertFalse(entero_publicable(1000))

    def test_las_cifras_que_esta_base_publicaba_NO_son_publicables(self):
        """Las seis cifras exactas del eje generalista: ninguna es publicable como
        entero. 🔴 Y las seis NO estan en la misma banda — este test lo asumia y
        estaba MAL: tres pasan de 100.000 (cota +/-500) y tres no (cota +/-50).
        La cota hay que leerla por fila, no por cohorte."""
        esperado = {385407: ('K-ENTERO', 500), 151639: ('K-ENTERO', 500),
                    108128: ('K-ENTERO', 500), 62735: ('K-3CIFRAS', 50),
                    60284: ('K-3CIFRAS', 50), 55226: ('K-3CIFRAS', 50)}
        for n, (banda_esp, cota_esp) in esperado.items():
            banda, texto, cota = precision_publicable(n)
            self.assertFalse(entero_publicable(n), 'entero en %d' % n)
            self.assertEqual(banda, banda_esp, 'banda en %d' % n)
            self.assertEqual(cota, cota_esp, 'cota en %d' % n)

    def test_ida_y_vuelta_es_consistente(self):
        """Lo que `precision_publicable` deja escribir, `leer_render` lo
        tiene que poder leer, y el valor verdadero tiene que caer en la cota."""
        for n in (264, 107, 7500, 40800, 117000, 1050, 99950):
            banda, texto, _ = precision_publicable(n)
            b2, lo, hi = leer_render(texto)
            self.assertEqual(banda, b2, 'banda ida/vuelta en %d (%r)' % (n, texto))
            self.assertLessEqual(lo, n, 'cota baja en %d' % n)
            self.assertGreaterEqual(hi, n, 'cota alta en %d' % n)


class LimiteDeBandaPorRedondeo(unittest.TestCase):
    """Regresion del defecto que esta suite encontro en su primera corrida:
    el redondeo CRUZA el limite de banda y la banda hay que elegirla despues."""

    def test_99950_cruza_a_millares(self):
        """99.950 redondeado al centenar es 100.000, que ya es banda de millares.
        Antes del arreglo emitia `100.0k`, forma que el lector no reconoce."""
        banda, texto, cota = precision_publicable(99950)
        self.assertEqual(banda, 'K-ENTERO')
        self.assertEqual(texto, '100k')
        self.assertEqual(leer_render(texto)[0], 'K-ENTERO')

    def test_9950_cruza_a_tres_cifras(self):
        """9.950 -> 10.000: sale de la banda de DOS cifras a la de TRES."""
        banda, texto, _ = precision_publicable(9950)
        self.assertEqual(banda, 'K-3CIFRAS')
        self.assertEqual(texto, '10.0k')

    def test_999_no_cruza(self):
        """El limite de abajo no se cruza por redondeo: 999 es exacto."""
        self.assertEqual(precision_publicable(999), ('EXACTO', '999', 0))
        self.assertEqual(precision_publicable(1000)[0], 'K-2CIFRAS')


class ControlesNegativos(unittest.TestCase):

    def test_NEGATIVE_millones_es_NO_MEDIDA_y_no_se_infiere(self):
        """Ningun repo de este catalogo llega al millon. `P286` prohibe
        extrapolar la banda: se declara, no se adivina."""
        self.assertEqual(leer_render('1.2M')[0], 'NO-MEDIDA')
        self.assertEqual(precision_publicable(1200000)[0], 'NO-MEDIDA')
        self.assertIsNone(precision_publicable(1200000)[1])

    def test_NEGATIVE_vacio_es_AUSENTE_no_cero(self):
        """Una ausencia no es un cero: la cubeta propia es lo que impide
        contarla como dato (misma regla que `P345`)."""
        self.assertEqual(leer_render('')[0], 'AUSENTE')
        self.assertEqual(leer_render(None)[0], 'AUSENTE')
        self.assertEqual(leer_render('   ')[0], 'AUSENTE')

    def test_NEGATIVE_basura_no_se_lee_como_cifra(self):
        self.assertEqual(leer_render('abc')[0], 'NO-RECONOCIDO')
        self.assertEqual(leer_render('264 estrellas')[0], 'NO-RECONOCIDO')

    def test_NEGATIVE_forma_k_sin_decimal_abajo_no_es_del_canal(self):
        """`7k` no es una forma que el canal emita en esa banda; leerla como
        K-ENTERO inventaria una cota de +/-500 donde el canal da +/-50."""
        self.assertEqual(leer_render('7k')[0], 'NO-RECONOCIDO')

    def test_NEGATIVE_conteo_negativo_es_error(self):
        with self.assertRaises(ValueError):
            precision_publicable(-5)

    def test_NEGATIVE_coma_decimal_se_lee_igual(self):
        """El canal renderiza `40.8k` y esta base escribe `40,8k`: la misma banda."""
        self.assertEqual(leer_render('40,8k'), leer_render('40.8k'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
