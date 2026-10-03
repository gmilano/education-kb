#!/usr/bin/env python3
"""Ancla Y desancla el detector (P119): un instrumento recien escrito es el menos probado.

Los dos falsos positivos que este test fija son REALES: el primer detector del
pase 61 reporto P145-P148 y la receta P149 como colgados, porque solo conocia la
convencion "## Pn -". Si alguien simplifica el detector, estos casos lo atrapan.
"""
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_patterns import definitions, citations


def kb(patterns_text, extra=None):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'compose'))
    with open(os.path.join(d, 'compose', 'patterns.md'), 'w', encoding='utf-8') as fh:
        fh.write(patterns_text)
    for name, body in (extra or {}).items():
        p = os.path.join(d, name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(body)
    return d


class AnclaDetector(unittest.TestCase):
    def test_convencion_A_seccion_nivel_2(self):
        self.assertIn(142, definitions(os.path.join(
            kb('## P142 — separar la puerta que afirma\n'), 'compose/patterns.md')))

    def test_convencion_B_subseccion_nivel_3(self):
        # el caso que el primer detector perdio
        d = definitions(os.path.join(kb('### \U0001f534 P146 — la unicidad se cuenta sobre codigo\n'),
                                     'compose/patterns.md'))
        self.assertIn(146, d)

    def test_convencion_C_encabezado_de_rango_define_los_cuatro(self):
        d = definitions(os.path.join(kb('## \U0001f9e9 P145–P148, los patrones del pase 59\n'),
                                     'compose/patterns.md'))
        for n in (145, 146, 147, 148):
            self.assertIn(n, d, 'P%d debe quedar definido por el rango' % n)

    def test_convencion_D_receta_es_otro_namespace_pero_resuelve(self):
        d = definitions(os.path.join(kb('## \U0001f373 Receta P149 — capa que no puede publicar\n'),
                                     'compose/patterns.md'))
        self.assertEqual(d.get(149), 'D-receta')

    def test_rango_absurdo_no_define_medio_mundo(self):
        # "P1-P900" no puede definir 900 numeros de un saque
        d = definitions(os.path.join(kb('## P1–P900, todo\n'), 'compose/patterns.md'))
        self.assertNotIn(500, d)


class DesanclaDetector(unittest.TestCase):
    def test_numero_citado_y_no_definido_SI_cuelga(self):
        root = kb('## P1 — algo\n', {'intel/trends.md': 'ver (**P126**) y P126 otra vez\n'})
        defs = definitions(os.path.join(root, 'compose', 'patterns.md'))
        bold, any_, _ = citations(root)
        self.assertNotIn(126, defs)
        self.assertEqual(bold[126], 1)
        self.assertEqual(any_[126], 2)

    def test_control_negativo_numero_inexistente_no_aparece(self):
        root = kb('## P1 — algo\n', {'intel/trends.md': 'sin citas\n'})
        _, any_, _ = citations(root)
        self.assertEqual(any_[999], 0)

    def test_mencion_en_prosa_no_es_definicion(self):
        # citar P135 en un parrafo no lo define, aunque sea en patterns.md
        d = definitions(os.path.join(kb('texto que menciona **P135** sin encabezado\n'),
                                     'compose/patterns.md'))
        self.assertNotIn(135, d)


if __name__ == '__main__':
    unittest.main(verbosity=2)
