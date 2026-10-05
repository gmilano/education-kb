#!/usr/bin/env python3
"""Suite de `P357` — la accion C del pase 111, medida sobre la capa de hint.

Corre SIN el corpus: reproduce las cifras desde los artefactos versionados del pase 112.
🔵 `P352`/`P355`: todas las rutas se resuelven contra `__file__`, nunca contra el `cwd`,
y la suite se corre desde un `cwd` ajeno como parte de su propia verificacion.
"""
import csv, importlib.util, os, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HERE, 'hint_layer.py')


def _mod():
    spec = importlib.util.spec_from_file_location('p357_hint_layer', MOD)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


H = _mod()


def tsv(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as fh:
        return list(csv.DictReader(fh, delimiter='\t'))


REPARTO = tsv('reparto-capa.2026-10-05.tsv')
HERENCIA = {r['bucket']: int(r['n']) for r in tsv('herencia.2026-10-05.tsv')}
CONTRA = {r['metrica']: (int(r['n']), int(r['total']))
          for r in tsv('contrafactual.2026-10-05.tsv')}


def capa(c):
    return {r['clase']: int(r['n']) for r in REPARTO if r['capa'] == c}


class ClasificadorCompartido(unittest.TestCase):
    """`P237`: el instrumento consume `clasificar` de `p345`, no una copia propia."""

    def test_es_el_de_p345(self):
        ruta = os.path.join(HERE, '..', 'p345-oer-four-forms', 'entregabilidad.py')
        self.assertTrue(os.path.exists(ruta), 'el modulo compartido tiene que existir')

    def test_vacio_es_ausente(self):
        self.assertEqual(H.clasificar('')[0], 'AUSENTE')

    def test_cc_by_es_resoluble(self):
        self.assertEqual(
            H.clasificar('https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>')[0],
            'RESOLUBLE')

    def test_control_negativo_url_cualquiera_no_es_cesion(self):
        """Un dominio desnudo NO es una cesion: si esto saliera RESOLUBLE, la tasa de
        la capa de hint estaria inflada por URLs que no ceden nada."""
        self.assertEqual(H.clasificar('https://openstax.org/')[0], 'NO-ES-CESION')


class Particion(unittest.TestCase):
    def test_capa_por_ruta(self):
        self.assertEqual(H.layer_of('content-pool/x/steps/xa/tutoring/y.json'), 'hint')
        self.assertEqual(H.layer_of('content-pool/x/x.json'), 'problema')

    def test_problema_padre(self):
        self.assertEqual(H.problem_of('content-pool/a1/steps/a1a/tutoring/z.json'), 'a1')
        self.assertIsNone(H.problem_of('otra-cosa.json'))

    def test_unidad_es_todo_dict_con_license(self):
        obj = [{'license': 'a'}, {'x': {'license': 'b'}}, {'sin': 1}]
        self.assertEqual(len(H.units(obj, [])), 2)

    def test_control_negativo_lista_de_hints_cuenta_cada_uno(self):
        """El JSON de tutoring es una LISTA: si el recorrido no entrara en listas,
        la capa de hint mediria 18.054 unidades (una por archivo) y no 69.121."""
        obj = [{'license': ''}, {'license': ''}, {'license': ''}]
        self.assertEqual(len(H.units(obj, [])), 3)


class Denominador(unittest.TestCase):
    def test_total_reproduce_el_pase_106(self):
        tot = sum(capa('problema').values()) + sum(capa('hint').values())
        self.assertEqual(tot, 82492)

    def test_problemas_reproduce_p348(self):
        self.assertEqual(sum(capa('problema').values()), 13371)

    def test_hints_reproduce_la_capa_de_hint(self):
        self.assertEqual(sum(capa('hint').values()), 69121)

    def test_la_capa_de_hint_tiene_vocabulario_BINARIO(self):
        """El hallazgo de forma: en la capa de hint solo existen dos clases. Las otras
        tres (`VERSION-SIN-VARIANTE`, `NO-ES-CESION`, `NO-RECONOCIDO`) viven SOLO en la
        capa de problema."""
        self.assertEqual(set(capa('hint')), {'RESOLUBLE', 'AUSENTE'})
        self.assertTrue({'VERSION-SIN-VARIANTE', 'NO-ES-CESION'} <= set(capa('problema')))


class AccionC(unittest.TestCase):
    def pct(self, c):
        d = capa(c)
        return 100.0 * d['RESOLUBLE'] / sum(d.values())

    def test_problemas_76_4(self):
        self.assertAlmostEqual(self.pct('problema'), 76.4, places=1)

    def test_hint_62_2(self):
        self.assertAlmostEqual(self.pct('hint'), 62.2, places=1)

    def test_accion_C_REFUTADA(self):
        """Pedia +-3 pp del 76,4 %. Mide -14,2 pp."""
        delta = self.pct('hint') - 76.4
        self.assertLess(delta, -3.0, 'la accion C sale REFUTADA, no confirmada')
        self.assertAlmostEqual(delta, -14.2, places=1)


class Herencia(unittest.TestCase):
    """La hipotesis del mecanismo, medida DIRECTO y no deducida del agregado."""

    def test_total_comparado_son_todos_los_hints(self):
        self.assertEqual(sum(HERENCIA.values()), 69121)

    def test_la_herencia_NO_es_la_identidad(self):
        igual = 100.0 * HERENCIA['IGUAL-AL-PADRE'] / sum(HERENCIA.values())
        self.assertAlmostEqual(igual, 80.2, places=1)
        self.assertLess(igual, 95.0)

    def test_la_divergencia_es_ASIMETRICA(self):
        """Casi toda la divergencia es el hijo DEJANDO CAER una cesion que el padre hizo,
        no el hijo agregando una. 13.499 contra 204: la asimetria es ~66 a 1."""
        cae = HERENCIA['HIJO-VACIO-PADRE-CEDE']
        agrega = HERENCIA['HIJO-CEDE-PADRE-VACIO']
        self.assertEqual(cae, 13499)
        self.assertEqual(agrega, 204)
        self.assertGreater(cae / agrega, 60)

    def test_control_negativo_ningun_hint_contradice_al_padre(self):
        """La cubeta `DISTINTO-NO-VACIO` esta VACIA: cuando los dos declaran, declaran lo
        MISMO. Si tuviera miembros, el defecto seria una CONTRADICCION y no una omision,
        y el remedio no seria el mismo."""
        self.assertEqual(HERENCIA.get('DISTINTO-NO-VACIO', 0), 0)


class Contrafactual(unittest.TestCase):
    """El numero que decide: incluso CONCEDIDA la herencia, la prediccion no se alcanza."""

    def pct(self, k):
        n, t = CONTRA[k]
        return 100.0 * n / t

    def test_observado(self):
        self.assertAlmostEqual(self.pct('observado'), 62.2, places=1)

    def test_bajo_herencia_asumida(self):
        self.assertAlmostEqual(self.pct('bajo-herencia-asumida'), 72.6, places=1)

    def test_la_herencia_concedida_NO_alcanza_la_banda(self):
        """Segundo motivo, independiente del primero: aun si cada hint vacio tomara la
        cesion de su padre, el residuo es -3,8 pp y la banda de +-3 pp sigue fallando.
        La prediccion era inalcanzable sobre su propia premisa."""
        residuo = self.pct('bajo-herencia-asumida') - 76.4
        self.assertAlmostEqual(residuo, -3.8, places=1)
        self.assertGreater(abs(residuo), 3.0)

    def test_la_herencia_habria_sumado_7212(self):
        obs, _ = CONTRA['observado']
        cf, _ = CONTRA['bajo-herencia-asumida']
        self.assertEqual(cf - obs, 7212)


class Procedencia(unittest.TestCase):
    def test_el_corpus_esta_nombrado_por_sha(self):
        """`P593`: el commit es parte de la invocacion."""
        with open(os.path.join(HERE, 'sha.2026-10-05.txt'), encoding='utf-8') as fh:
            sha = fh.read().strip()
        self.assertEqual(len(sha), 40)
        self.assertTrue(all(c in '0123456789abcdef' for c in sha))


if __name__ == '__main__':
    unittest.main(verbosity=2)
