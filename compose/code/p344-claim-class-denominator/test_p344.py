#!/usr/bin/env python3
"""Suite de `P344`. Corre contra el MODULO y contra los TSV, no contra la prosa
de los .md. Cada eje positivo lleva su control negativo."""
import csv, os, re, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import detect_claim as D

HERE = os.path.dirname(os.path.abspath(__file__))


class BadgeHTML(unittest.TestCase):
    """El defecto que abrio `P344`: badge en HTML, no en Markdown."""

    def test_html_badge_shields_detected(self):
        t = '<img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License-MIT">'
        self.assertEqual(len(D.detect(t)['badge_html']), 1)

    def test_html_badge_anchor_wrapped_detected(self):
        t = ('<a href="https://github.com/u/r/blob/main/LICENSE">\n'
             '<img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License">\n'
             '</a>')
        self.assertEqual(len(D.detect(t)['badge_html']), 1)

    def test_html_badge_attr_order_irrelevant(self):
        t = '<img alt="License" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg">'
        self.assertEqual(len(D.detect(t)['badge_html']), 1)

    def test_NEGATIVE_html_img_unrelated_not_a_claim(self):
        """Control negativo: una imagen que no habla de licencia no es afirmacion."""
        t = '<img src="https://img.shields.io/badge/build-passing-green.svg" alt="build">'
        self.assertEqual(D.detect(t)['badge_html'], [])

    def test_NEGATIVE_plain_logo_not_a_claim(self):
        t = '<img src="docs/logo.png" alt="logo">'
        self.assertEqual(D.detect(t)['badge_html'], [])


class BadgeMarkdown(unittest.TestCase):
    def test_md_linked_badge_detected(self):
        t = '[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)'
        c = D.detect(t)
        self.assertEqual(len(c['badge_md']), 1)
        self.assertTrue(c['badge_md'][0]['dest_is_path'])

    def test_md_badge_dest_http_is_claim_but_not_path(self):
        """`SafeTutors`: el destino es una URL de plantilla sin editar, no una ruta."""
        t = ('[![License](https://img.shields.io/badge/License-MIT-blue.svg)]'
             '(https://github.com/your-username/SafeTutors/blob/main/LICENSE)')
        c = D.detect(t)
        self.assertEqual(len(c['badge_md']), 1)

    def test_NEGATIVE_md_badge_unrelated(self):
        t = '[![CI](https://img.shields.io/badge/ci-green.svg)](https://ci.example.org)'
        self.assertEqual(D.detect(t)['badge_md'], [])


class TreeEntry(unittest.TestCase):
    def test_unicode_tee_detected(self):
        t = '├── LICENSE                  # Licencia del proyecto'
        self.assertEqual(len(D.detect(t)['tree']), 1)

    def test_unicode_elbow_detected(self):
        t = '└── LICENSE.md'
        self.assertEqual(len(D.detect(t)['tree']), 1)

    def test_ascii_tree_detected(self):
        self.assertEqual(len(D.detect('|-- LICENSE')['tree']), 1)
        self.assertEqual(len(D.detect('`-- LICENCE')['tree']), 1)

    def test_british_spelling_detected(self):
        """`P340`: la cesion puede vivir en `LICENCE`."""
        t = '├── LICENCE'
        self.assertEqual(len(D.detect(t)['tree']), 1)

    def test_NEGATIVE_prose_mentioning_licence_is_not_a_tree(self):
        t = 'See the LICENSE file for details.'
        self.assertEqual(D.detect(t)['tree'], [])

    def test_NEGATIVE_tree_without_license_entry(self):
        t = '├── README.md\n└── src/'
        self.assertEqual(D.detect(t)['tree'], [])


class Prose(unittest.TestCase):
    def test_bold_wrapped_name_detected(self):
        """El segundo defecto del pase 110: `**MIT License**` se perdia porque la
        clase de caracteres excluia el asterisco."""
        t = 'This project is licensed under the **MIT License** — see the LICENSE file.'
        c = D.detect(t)
        self.assertEqual(len(c['prose']), 1)
        self.assertIn('MIT', c['families'])

    def test_plain_name_detected(self):
        t = 'This code is licensed under the Apache 2.0 License.'
        self.assertEqual(len(D.detect(t)['prose']), 1)

    def test_backtick_wrapped_detected(self):
        t = 'Released under the `BSD-3-Clause` license.'
        self.assertGreaterEqual(len(D.detect(t)['prose']), 1)

    def test_british_spelling_detected(self):
        t = 'This project is licenced under the MIT licence.'
        self.assertEqual(len(D.detect(t)['prose']), 1)

    def test_NEGATIVE_narrow_custom_permission_is_not_a_license(self):
        """`carrera-lectora`: permiso a medida, NO nombra licencia. `NOT-A-LICENSE`."""
        t = 'Creado con fines educativos. Libre para usar en contextos educativos.'
        self.assertEqual(D.detect(t)['prose'], [])

    def test_NEGATIVE_word_license_alone_is_not_a_claim(self):
        t = 'Please read the license before use.'
        self.assertEqual(D.detect(t)['prose'], [])


class Verdict(unittest.TestCase):
    EMPTY = {'badge_md': [], 'badge_html': [], 'tree': [], 'prose': [], 'families': []}

    def test_file_present_beats_every_claim(self):
        c = dict(self.EMPTY, badge_html=[{'alt': 'License', 'src': 'x'}])
        self.assertEqual(D.verdict(c, 1, True), 'CEDE')

    def test_unreachable_readme_is_not_silence(self):
        """Un 404 de README no es «no cede»: es canal sin testigo de alcance."""
        self.assertEqual(D.verdict(self.EMPTY, 0, False), 'INALCANZABLE')

    def test_badge_without_file_is_P342(self):
        c = dict(self.EMPTY, badge_html=[{'alt': 'License', 'src': 'x'}])
        self.assertEqual(D.verdict(c, 0, True), 'P342-AFIRMA-SIN-ARCHIVO')

    def test_tree_without_file_is_P342(self):
        c = dict(self.EMPTY, tree=['├── LICENSE'])
        self.assertEqual(D.verdict(c, 0, True), 'P342-AFIRMA-SIN-ARCHIVO')

    def test_prose_only_is_P314_not_P342(self):
        """La distincion que `P342` instalo: badge/arbol apuntan a una RUTA, la
        prosa solo nombra una familia. La gestion que las arregla es distinta."""
        c = dict(self.EMPTY, prose=['licensed under the MIT License'])
        self.assertEqual(D.verdict(c, 0, True), 'P314-PROSA-SIN-ARCHIVO')

    def test_nothing_is_confirmed_silence(self):
        self.assertEqual(D.verdict(self.EMPTY, 0, True), 'SILENCIO-CONFIRMADO')


class Artefactos(unittest.TestCase):
    """Aserciones contra los TSV de este pase."""

    def _rows(self, name):
        p = os.path.join(HERE, name)
        if not os.path.exists(p):
            self.skipTest(name + ' no generado todavia')
        with open(p, encoding='utf-8') as fh:
            return list(csv.DictReader(fh, delimiter='\t'))

    def test_control_negativo_404_en_20_de_20(self):
        p = os.path.join(HERE, 'control-codes.2026-10-05.txt')
        codes = open(p, encoding='utf-8').read().split()
        self.assertEqual(len(codes), 20)
        self.assertEqual(codes.count('404'), 20,
                         'el canal no discrimina: un 404 no se distingue de un canal caido')

    def test_denominador_es_13_no_32(self):
        n = len([l for l in open(os.path.join(HERE, 'targets13.txt'),
                                 encoding='utf-8').read().split() if l.strip()])
        self.assertEqual(n, 13, 'la cadena 32 -> 22 -> 13 ya fue corregida (P172)')

    def test_los_13_tienen_readme_alcanzable(self):
        """Sin testigo de alcance, `hits=0` no es una ausencia."""
        rows = self._rows('accionA-v2.2026-10-05.tsv')
        trece = [r for r in rows if r['slug'] != 'gmilano/repo-inventado-p110-control']
        self.assertEqual(len(trece), 13)
        for r in trece:
            self.assertNotEqual(r['readme_ref'], '-', r['slug'])

    def test_ninguno_de_los_13_tiene_archivo(self):
        rows = self._rows('accionA-v2.2026-10-05.tsv')
        for r in rows:
            self.assertEqual(r['license_file_hits'], '0', r['slug'])

    def test_resto9_tiene_al_menos_dos_P342(self):
        """El denominador que la pregunta deberia haber tenido."""
        rows = self._rows('accionA-resto9-v2.2026-10-05.tsv')
        n = len([r for r in rows if r['veredicto'] == 'P342-AFIRMA-SIN-ARCHIVO'])
        self.assertGreaterEqual(n, 2)


if __name__ == '__main__':
    unittest.main(verbosity=1)
