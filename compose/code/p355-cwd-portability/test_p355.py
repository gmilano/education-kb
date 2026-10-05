#!/usr/bin/env python3
"""Suite de `P355` — la accion A del pase 111.

Corre SIN rehacer el tablero: reproduce el reparto desde el artefacto versionado, y prueba
los dos clasificadores (`shape`, `ephemeral_refs`) con los controles negativos que sostienen
el hallazgo de SEVERIDAD. Rutas resueltas contra `__file__` (`P352`/`P355` sobre si misma).
"""
import csv, importlib.util, os, unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def _mod():
    spec = importlib.util.spec_from_file_location(
        'p355_portability', os.path.join(HERE, 'portability.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


P = _mod()
ART = os.path.join(HERE, 'resultado.2026-10-05.tsv')


def filas():
    with open(ART, encoding='utf-8') as fh:
        lines = [l for l in fh if not l.startswith('#')]
    return [r for r in csv.DictReader(lines, delimiter='\t') if r.get('suite')]


FILAS = filas()
ROTAS = [r for r in FILAS if r['exit_propio'] == '0' and r['exit_ajeno'] != '0']


class Tablero(unittest.TestCase):
    def test_todas_pasan_desde_su_propio_cwd(self):
        """La linea base del pase 111: 66 suites, 0 fallos — remedida desde el clon."""
        self.assertEqual([r['suite'] for r in FILAS if r['exit_propio'] != '0'], [])

    def test_el_tablero_tiene_las_66_del_pase_111_mas_las_nuevas(self):
        self.assertGreaterEqual(len(FILAS), 66)


class AccionA(unittest.TestCase):
    def test_CONFIRMADA_con_4(self):
        self.assertEqual(len(ROTAS), 4)
        self.assertGreaterEqual(len(ROTAS), 3, 'la prediccion pedia >=3')

    def test_NINGUNA_de_las_4_es_por_ruta_efimera(self):
        """El reparto que la prediccion sumo en una cifra: la clase de `P352` aporta 0."""
        for r in ROTAS:
            self.assertEqual(r['refs_efimeras'], '0', r['suite'])

    def test_la_unica_suite_con_ruta_efimera_PASA(self):
        """`p345`, el espécimen de `P352`, ya esta arreglado: nombra `/tmp` y no falla."""
        p345 = [r for r in FILAS if 'p345' in r['suite']]
        self.assertEqual(len(p345), 1)
        self.assertNotEqual(p345[0]['refs_efimeras'], '0')
        self.assertEqual(p345[0]['exit_ajeno'], '0')

    def test_la_forma_del_fallo_se_reparte_2_y_2(self):
        formas = sorted(r['forma_ajeno'] for r in ROTAS)
        self.assertEqual(formas, ['CRASH', 'CRASH',
                                  'TOTAL-DEGRADADO', 'TOTAL-DEGRADADO'])


class FormaDelFallo(unittest.TestCase):
    """`shape()` — el clasificador del que depende el hallazgo de severidad."""

    def test_traceback_es_CRASH(self):
        self.assertEqual(P.shape(
            'Traceback (most recent call last):\nFileNotFoundError: rows.tsv'), 'CRASH')

    def test_total_bien_formado_y_menor_es_TOTAL_DEGRADADO(self):
        self.assertEqual(P.shape('FAIL negative control\n\n14/15 checks passed'),
                         'TOTAL-DEGRADADO')

    def test_CONTROL_NEGATIVO_un_crash_no_se_lee_como_total(self):
        """El control que sostiene el hallazgo: si `shape` mirara primero el `N/M`, el
        traceback de `p251` -que imprime `26/26` en su cabecera cuando corre bien- caeria
        en `TOTAL-DEGRADADO` y el reparto 2-2 se volveria 0-4. El orden importa."""
        mixto = '26/26 esperado\nTraceback (most recent call last):\nFileNotFoundError'
        self.assertEqual(P.shape(mixto), 'CRASH')

    def test_CONTROL_NEGATIVO_salida_sin_nada_es_SILENCIOSO(self):
        """La forma PEOR y la que `P352` tenia: ni total ni traceback. Que exista como
        etiqueta propia es lo que permite decir que este pase no encontro ninguna."""
        self.assertEqual(P.shape(''), 'SILENCIOSO')
        self.assertNotIn('SILENCIOSO', [r['forma_ajeno'] for r in ROTAS])


class RutaEfimera(unittest.TestCase):
    """`ephemeral_refs()` — y sobre todo lo que NO tiene que marcar."""

    def setUp(self):
        self.tmp = os.path.join(HERE, '_fixture_tmp.py')

    def tearDown(self):
        if os.path.exists(self.tmp):
            os.remove(self.tmp)

    def escribir(self, texto):
        with open(self.tmp, 'w', encoding='utf-8') as fh:
            fh.write(texto)
        return P.ephemeral_refs(HERE, os.path.basename(self.tmp))

    def test_marca_tmp_absoluto(self):
        self.assertEqual(len(self.escribir("p = '/tmp/oat-censo/x.tsv'\n")), 1)

    def test_marca_TMPDIR(self):
        self.assertEqual(len(self.escribir('out="${TMPDIR:-/tmp}/build"\n')), 1)

    def test_CONTROL_NEGATIVO_mkdtemp_NO_se_marca(self):
        """`tempfile.mkdtemp()` es el ARREGLO de `P352`, no el defecto. Un detector que lo
        marcara reportaria como rota justo la suite que se corrigio."""
        self.assertEqual(self.escribir('d = tempfile.mkdtemp()\n'), [])

    def test_CONTROL_NEGATIVO_palabra_que_contiene_tmp_NO_se_marca(self):
        self.assertEqual(self.escribir("x = 'attempt/tmpl/plantilla'\n"), [])


class Inventario(unittest.TestCase):
    def test_no_cuenta_una_suite_dos_veces(self):
        """`P126`: el conteo del pase 111 se equivoco por recorrer `lib/` dos veces."""
        nombres = [r['suite'] for r in FILAS]
        self.assertEqual(len(nombres), len(set(nombres)))

    def test_suites_encuentra_py_y_sh(self):
        root = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
        ss = P.suites(root)
        self.assertTrue(any(s.endswith('.py') for s in ss))
        self.assertTrue(any(s.endswith('.sh') for s in ss))


if __name__ == '__main__':
    unittest.main(verbosity=2)
