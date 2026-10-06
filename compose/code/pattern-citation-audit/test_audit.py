#!/usr/bin/env python3
"""Ancla Y desancla el detector (P119): un instrumento recien escrito es el menos probado.

Los dos falsos positivos que este test fija son REALES: el primer detector del
pase 61 reporto P145-P148 y la receta P149 como colgados, porque solo conocia la
convencion "## Pn -". Si alguien simplifica el detector, estos casos lo atrapan.
"""
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_patterns import definitions, citations, duplicate_definitions


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


class TestDuplicateDefinitions(unittest.TestCase):
    """La asercion que el pase 20 del 2026-10-06 dejo escrita y no implementada:
    que cada numero resuelva a EXACTAMENTE una definicion, no a AL MENOS una."""

    def _dups(self, text):
        import tempfile, os
        fd, path = tempfile.mkstemp(suffix='.md')
        with os.fdopen(fd, 'w', encoding='utf-8') as fh:
            fh.write(text)
        try:
            return duplicate_definitions(path)
        finally:
            os.unlink(path)

    def test_un_numero_una_definicion_no_es_duplicado(self):
        self.assertEqual(self._dups('## P5 \u2014 uno\n## P6 \u2014 otro\n'), {})

    def test_dos_definiciones_del_mismo_numero_SI_es_duplicado(self):
        """El caso real: dos patrones DISTINTOS peleando por un numero."""
        d = self._dups('## P28 \u2014 gestion escolar brasilena\n'
                       '## P28 \u2014 integracion administrativa K-12\n')
        self.assertEqual(d, {28: 2})

    def test_tres_definiciones_se_cuentan_tres(self):
        d = self._dups('## P28 \u2014 a\n## P28 \u2014 b\n## P28 \u2014 c\n')
        self.assertEqual(d, {28: 3})

    def test_COLGADA_no_es_DUPLICADA(self):
        """\U0001f535 Las dos fallas son del mismo namespace y NO son la misma:
        un numero citado y nunca definido no es un numero definido dos veces.
        El detector de la primera es ciego a la segunda por construccion."""
        self.assertEqual(self._dups('Ver **P126**, que nadie definio.\n'), {})

    def test_seccion_de_ACTUALIZACION_no_es_una_segunda_definicion(self):
        """\U0001f534 El falso positivo que corrige la cifra del pase 20.

        `## P1 update, fourteenth pass ...` es una nota sobre P1, no un segundo
        patron llamado P1. El pase 20 conto `^## P1` -- la ORTOGRAFIA -- y
        reporto 7 numeros duplicados; contando el OBJETO son 6. Es exactamente
        la familia de defectos que el docstring de este mismo instrumento
        advierte: el ancla reconoce una ortografia y no un objeto."""
        d = self._dups('## P1 \u2014 LTI + MCP side-car tutor\n'
                       '## P1 update, fourteenth pass \u2014 cuatro puertas\n')
        self.assertEqual(d, {})

    def test_encabezado_de_RANGO_no_colisiona_con_su_numero_bajo(self):
        """`## P145-P148` define cuatro numeros a proposito."""
        d = self._dups('## P145\u2014P148, los patrones del pase 55\n')
        self.assertEqual(d, {})


if __name__ == '__main__':
    unittest.main(verbosity=2)

class ConvencionEBackticks(unittest.TestCase):
    """`P354` — regresion: el numero en CODIGO INLINE es la forma que
    patterns.md usa desde el pase ~95, y el detector era ciego a ella."""

    def _defs(self, text):
        import tempfile, os
        fd, p = tempfile.mkstemp(suffix='.md')
        with os.fdopen(fd, 'w', encoding='utf-8') as fh:
            fh.write(text)
        try:
            return definitions(p)
        finally:
            os.unlink(p)

    def test_backticks_con_emoji_se_definen(self):
        """La forma exacta del pase 111."""
        d = self._defs('### \U0001f534 `P348` \u2014 contar por el ARCHIVO\n')
        self.assertIn(348, d)

    def test_backticks_sin_emoji_se_definen(self):
        d = self._defs('## `P284` \u2014 titulo\n')
        self.assertIn(284, d)

    def test_rango_con_backticks_se_expande(self):
        """La convencion C con backticks. \U0001f535 Sin prosa antes del numero:
        un encabezado de GRUPO con titulo ('Patrones del pase 111 \u2014 `P348`...')
        NO define por rango, y esta bien que no lo haga — cada patron lleva su
        propia subseccion. Lo verifica `test_NEGATIVE_encabezado_con_prosa_antes`."""
        d = self._defs('## `P360`\u2013`P362` \u2014 los tres patrones del pase\n')
        for n in (360, 361, 362):
            self.assertIn(n, d)

    def test_la_forma_VIEJA_sigue_funcionando(self):
        """El arreglo no puede romper las convenciones A/B/C/D que ya andaban."""
        d = self._defs('## P142 \u2014 titulo\n### **P146** \u2014 otro\n'
                       '## Receta P149 \u2014 x\n')
        for n in (142, 146, 149):
            self.assertIn(n, d)

    def test_NEGATIVE_una_CITA_en_backticks_no_es_definicion(self):
        """\U0001f534 El control que importa: `P999` citado en prosa o en una FILA
        de tabla no define nada. Si lo hiciera, el detector no detectaria."""
        d = self._defs('Ver `P999`, que es la causa.\n\n| `P998` | x |\n')
        self.assertNotIn(999, d)
        self.assertNotIn(998, d)

    def test_NEGATIVE_encabezado_sin_guion_no_define(self):
        """La convencion pide separador (guion o coma) despues del numero."""
        d = self._defs('### `P997` es interesante\n')
        self.assertNotIn(997, d)

    def test_NEGATIVE_encabezado_con_prosa_antes_no_define(self):
        """Un encabezado de GRUPO que lista numeros no los define por si solo;
        cada patron lleva su propia subseccion."""
        d = self._defs('## Patrones del pase 110 (2026-10-05) \u2014 `P996`, `P995`\n')
        self.assertNotIn(996, d)


if __name__ == '__main__':
    unittest.main(verbosity=2)
