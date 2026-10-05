#!/usr/bin/env python3
"""Suite de `P356` — la accion D del pase 111.

El control que importa es NEGATIVO: un encabezado que MENCIONA un numero no lo DEFINE.
La primera version de esta medicion uso un `grep` con `[^0-9]*` antes del numero, y por eso
leyo *«## Capa de escritura del lado DOCENTE — el agujero de P129, cerrado»* como una
definicion de `P129`. Habria convertido 2 de las 21 colgadas en falsos `DEFINIDA-FUERA`.
Rutas contra `__file__` (`P355`).
"""
import os, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

import importlib.util
spec = importlib.util.spec_from_file_location('p356_origin', os.path.join(HERE, 'origin.py'))
O = importlib.util.module_from_spec(spec)
spec.loader.exec_module(O)

WHERE, _TEXTS = O.scan(ROOT)
IN_PATTERNS = set(O.A.definitions(os.path.join(ROOT, 'compose', 'patterns.md')))
CLASES = {n: O.classify(n, WHERE, ROOT) for n in O.COLGADAS}


def clase(n):
    return '+'.join(CLASES[n])


class Denominador(unittest.TestCase):
    def test_son_21(self):
        self.assertEqual(len(O.COLGADAS), 21)

    def test_ninguna_la_define_patterns_md(self):
        """Si patterns.md definiera una, no seria colgada y el denominador estaria mal."""
        for n in O.COLGADAS:
            self.assertNotIn(n, IN_PATTERNS, 'P%d' % n)


class AccionD(unittest.TestCase):
    def test_ANUNCIADA_son_15(self):
        self.assertEqual(sum(1 for n in O.COLGADAS if clase(n) == 'ANUNCIADA'), 15)

    def test_CONFIRMADA(self):
        """Pedia >=14 de la clase «anunciado y nunca escrito». Refutada con <=7."""
        a = sum(1 for n in O.COLGADAS if clase(n) == 'ANUNCIADA')
        self.assertGreaterEqual(a, 14)

    def test_las_otras_6_NO_son_deuda_documental(self):
        """El tercer resultado que la pre-registracion no admitia: 6 de las 21 SI estan
        definidas, y lo que fallo es el ALCANCE del instrumento que las conto."""
        self.assertEqual(sum(1 for n in O.COLGADAS if clase(n) == 'DEFINIDA-FUERA'), 3)
        self.assertEqual(sum(1 for n in O.COLGADAS if clase(n) == 'INSTRUMENTO'), 3)

    def test_quienes_son(self):
        self.assertEqual(sorted(n for n in O.COLGADAS if clase(n) == 'DEFINIDA-FUERA'),
                         [245, 279, 281])
        self.assertEqual(sorted(n for n in O.COLGADAS if clase(n) == 'INSTRUMENTO'),
                         [239, 280, 283])

    def test_las_clases_son_exhaustivas(self):
        self.assertEqual(len(O.COLGADAS),
                         sum(1 for n in O.COLGADAS
                             if clase(n) in ('ANUNCIADA', 'DEFINIDA-FUERA', 'INSTRUMENTO')))


class AsimetriaDelAuditor(unittest.TestCase):
    """El defecto de ALCANCE, medido: definiciones de 1 archivo, citas de todos."""

    def test_el_auditor_lee_definiciones_de_un_solo_archivo(self):
        import inspect
        src = inspect.getsource(O.A.definitions)
        self.assertIn('patterns_md', src)

    def test_hay_numeros_definidos_fuera_de_patterns_md(self):
        fuera = {n for n in WHERE if n not in IN_PATTERNS}
        self.assertEqual(len(fuera), 3)
        self.assertEqual(sorted(fuera), [245, 279, 281])


class ControlesNegativos(unittest.TestCase):
    def test_CONTROL_NEGATIVO_mencion_en_encabezado_NO_es_definicion(self):
        """El caso que rompio la primera medicion de este pase."""
        texto = ('## Capa de escritura del lado DOCENTE — el agujero de P129, cerrado\n'
                 '### Y el hueco de APAC queda ABIERTO, por la regla de P135\n')
        self.assertEqual(O.defs_in(texto), {})

    def test_CONTROL_POSITIVO_las_convenciones_reales_si_definen(self):
        self.assertEqual(O.defs_in('## P142 — titulo\n'), {142: 'A/B-seccion'})
        self.assertEqual(O.defs_in('### `P348` — titulo\n'), {348: 'A/B-seccion'})
        self.assertEqual(O.defs_in('## Receta P149 — x\n'), {149: 'D-receta'})
        self.assertIn(146, O.defs_in('## P145—P148, los patrones\n'))

    def test_CONTROL_NEGATIVO_cita_en_prosa_NO_es_definicion(self):
        self.assertEqual(O.defs_in('ver **P135** y `P279` en la tabla\n'), {})

    def test_CONTROL_NEGATIVO_P129_y_P135_siguen_ANUNCIADAS(self):
        """La consecuencia de los dos controles de arriba, sobre el arbol real."""
        self.assertEqual(clase(129), 'ANUNCIADA')
        self.assertEqual(clase(135), 'ANUNCIADA')

    def test_CONTROL_NEGATIVO_el_propio_directorio_queda_fuera(self):
        """Este archivo cita P129/P135/P142 como ejemplos y `origin.py` los escribe en
        encabezados de su docstring. Si el barrido se leyera a si mismo, contaria sus
        propias fixtures como definiciones del arbol.

        La primera version de este control afirmaba `142 not in WHERE` y estaba MAL:
        `P142` SI esta definida, en `compose/patterns.md`, y legitimamente — es el
        control positivo del propio auditor. El control correcto no mira el NUMERO sino
        la PROCEDENCIA: ninguno de los dos directorios de instrumento puede aportar
        una definicion al barrido."""
        propios = [f for defs in WHERE.values() for f, _c in defs
                   if any(f.startswith(d) for d in O.SELF_DIRS)]
        self.assertEqual(propios, [])


class DeudaReal(unittest.TestCase):
    def test_P135_es_la_peor(self):
        """84 citas en negrita y 0 definiciones: la mas urgente de las 15 anunciadas."""
        _b, any_, _w = O.A.citations(ROOT)
        self.assertEqual(clase(135), 'ANUNCIADA')
        self.assertGreater(any_[135], 100)

    def test_la_accion_D_se_detiene_en_CLASIFICAR(self):
        """`P286`: inventar la definicion de un patron ajeno es fabricar doctrina. Esta
        suite verifica que el pase NO escribio ninguna de las 15 secciones faltantes."""
        for n in (127, 128, 129, 130, 132, 133, 134, 135):
            self.assertNotIn(n, IN_PATTERNS, 'P%d no debe haberse inventado' % n)


if __name__ == '__main__':
    unittest.main(verbosity=2)
