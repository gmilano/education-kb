#!/usr/bin/env python3
"""Suite de `P345`/`P346`. Corre contra los modulos y contra los TSV del pase 110."""
import collections, csv, os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from censo_oer import forma_de
from entregabilidad import clasificar


class FormasDeOer(unittest.TestCase):
    """Las CUATRO formas de `P338`, cada una con su control negativo."""

    def test_details_books(self):
        self.assertEqual(forma_de('https://openstax.org/details/books/precalculus'),
                         'details-books')

    def test_books_pages(self):
        self.assertEqual(
            forma_de('https://openstax.org/books/precalculus/pages/1-4-composition-of-functions'),
            'books-pages')

    def test_books_sin_pages(self):
        self.assertEqual(forma_de('https://openstax.org/books/precalculus'), 'books-sinpage')

    def test_dominio_desnudo_es_cuarta_forma(self):
        """Las 41 figuras que explican `P337`: nombran al EDITOR, no a la OBRA."""
        self.assertEqual(forma_de('https://openstax.org/'), 'openstax-otro')
        self.assertEqual(forma_de('https://openstax.org'), 'openstax-otro')

    def test_NEGATIVE_otro_dominio_no_es_openstax(self):
        self.assertEqual(forma_de('https://ds100.org/su26/past-exams/'), 'NO-OPENSTAX')

    def test_NEGATIVE_vacio_no_es_no_openstax(self):
        """Un campo vacio no es «de otro editor»: es una ausencia, y la cubeta
        propia es lo que impide contarlo como si fuera un dato."""
        self.assertEqual(forma_de(''), 'VACIO')
        self.assertEqual(forma_de(None), 'VACIO')

    def test_books_sinpage_no_se_come_a_books_pages(self):
        """El orden de las formas importa: `books-sinpage` lleva un lookahead
        negativo para no tragarse la forma con `/pages/`."""
        self.assertNotEqual(forma_de('https://openstax.org/books/x/pages/1-1'), 'books-sinpage')


class ClaseDeCesion(unittest.TestCase):
    def test_cc_by_4_resoluble(self):
        c, i = clasificar('https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>')
        self.assertEqual(c, 'RESOLUBLE')
        self.assertEqual(i, 'CC-BY-4.0')

    def test_cc_by_nc_sa_resoluble_y_distinguible(self):
        c, i = clasificar('https://creativecommons.org/licenses/by-nc-sa/4.0/')
        self.assertEqual(c, 'RESOLUBLE')
        self.assertEqual(i, 'CC-BY-NC-SA-4.0')

    def test_cc0_resoluble(self):
        c, i = clasificar('https://creativecommons.org/publicdomain/zero/1.0/')
        self.assertEqual(c, 'RESOLUBLE')
        self.assertEqual(i, 'CC0-1.0')

    def test_version_sin_variante_no_es_resoluble(self):
        """«CC4.0» nombra una version, no una licencia: la 4.0 son seis, tres NC."""
        c, _ = clasificar('CC4.0')
        self.assertEqual(c, 'VERSION-SIN-VARIANTE')

    def test_url_de_fuente_no_es_cesion(self):
        """El hallazgo de `P346`: un PDF de examen en el campo `license`."""
        c, _ = clasificar('https://ds100.org/sp26/assets/exams/fa25/fa25_final_sol.pdf')
        self.assertEqual(c, 'NO-ES-CESION')

    def test_vacio_es_ausente(self):
        self.assertEqual(clasificar('')[0], 'AUSENTE')
        self.assertEqual(clasificar(None)[0], 'AUSENTE')

    def test_NEGATIVE_una_url_de_creativecommons_sin_variante_no_pasa(self):
        """Control negativo del propio detector: el dominio correcto no alcanza."""
        c, _ = clasificar('https://creativecommons.org/')
        self.assertNotEqual(c, 'RESOLUBLE')


class Artefactos(unittest.TestCase):
    def _rows(self, name):
        p = os.path.join(HERE, name)
        if not os.path.exists(p):
            self.skipTest(name + ' no generado')
        with open(p, encoding='utf-8') as fh:
            return list(csv.DictReader(fh, delimiter='\t'))

    def test_figuras_son_2443(self):
        self.assertEqual(len(self._rows('corte-figuras.2026-10-05.tsv')), 2443)

    def test_corte_converge_a_1611_832(self):
        """La prediccion pre-registrada por el pase 109, medida."""
        rows = self._rows('corte-figuras.2026-10-05.tsv')
        c = collections.Counter(r['lado'] for r in rows)
        self.assertEqual(c['OPENSTAX'], 1611)
        self.assertEqual(c['NO-OPENSTAX'], 832)

    def test_la_cuarta_forma_son_exactamente_41(self):
        """`P337` cerrado: 1.611 - 1.570 = 41 = las de dominio desnudo."""
        rows = self._rows('corte-figuras.2026-10-05.tsv')
        c = collections.Counter(r['forma'] for r in rows)
        self.assertEqual(c['openstax-otro'], 41)
        self.assertEqual(c['details-books'] + c['books-pages'], 1570)
        self.assertEqual(c['details-books'] + c['books-pages'] + c['openstax-otro'], 1611)

    def test_entregable_es_1418_no_1611_ni_1570(self):
        """`P346`: el corte openstax no responde la pregunta de entrega."""
        rows = self._rows('entregabilidad.2026-10-05.tsv')
        c = collections.Counter(r['clase_cesion'] for r in rows)
        self.assertEqual(c['RESOLUBLE'], 1418)
        self.assertEqual(sum(c.values()), 2443)

    def test_hay_figuras_openstax_SIN_cesion(self):
        """Lo que refuta usar el corte como proxy de licencia."""
        rows = self._rows('entregabilidad.2026-10-05.tsv')
        n = len([r for r in rows
                 if r['lado'] == 'OPENSTAX' and r['clase_cesion'] == 'AUSENTE'])
        self.assertEqual(n, 368)
        self.assertGreater(n, 0)

    def test_hay_figuras_NO_openstax_CON_cesion(self):
        """Y la direccion contraria: el otro lado tampoco es uniforme."""
        rows = self._rows('entregabilidad.2026-10-05.tsv')
        n = len([r for r in rows
                 if r['lado'] == 'NO-OPENSTAX' and r['clase_cesion'] == 'RESOLUBLE'])
        self.assertEqual(n, 175)

    def test_unidades_son_13371_no_12999(self):
        """El denominador que la pre-registracion traia estaba mal."""
        p = '/tmp/oat-censo/unidades-oer.tsv'
        if not os.path.exists(p):
            self.skipTest('censo no generado')
        with open(p, encoding='utf-8') as fh:
            self.assertEqual(len(list(csv.DictReader(fh, delimiter='\t'))), 13371)


if __name__ == '__main__':
    unittest.main(verbosity=1)
