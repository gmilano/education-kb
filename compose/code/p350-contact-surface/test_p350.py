#!/usr/bin/env python3
"""Suite de `P350`. Versiona el veredicto NO-MEDIBLE y la superficie estructural,
para que un pase futuro no lo lea como una medicion que salio baja."""
import os, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from superficie import (ESTRUCTURADAS_CON_PERSONA, LEGIBLES_POR_MAQUINA, PRESENCIA,
                        REPOS, RUTAS, SONDAS_POR_REPO, cobertura, medible,
                        superficie_legible_por_maquina, testigo_de_alcance,
                        veredicto_accion_a)


class ElVeredictoEsNoMedible(unittest.TestCase):

    def test_no_es_confirmada_ni_refutada(self):
        """🔴 Las dos ramas de la pre-registracion (>=4 y <=2) admitian solo
        numeros. El resultado real es que el numero no se puede obtener aca."""
        self.assertEqual(veredicto_accion_a()[0], 'NO-MEDIBLE')
        self.assertFalse(medible())

    def test_el_motivo_queda_ESCRITO_no_implicito(self):
        """Un pase futuro tiene que poder distinguir «no se midio» de
        «se midio y salio 0» — es la misma leccion de `P343`."""
        self.assertIn('PII', veredicto_accion_a()[1])
        self.assertIn('denegado', veredicto_accion_a()[1])


class SuperficieEstructural(unittest.TestCase):
    """Presencia y tamano. El contenido no se leyo, asi que nada de lo que esta
    suite asegura depende de un dato personal."""

    def test_son_los_6_falsos_negativos_del_pase_110(self):
        self.assertEqual(len(REPOS), 6)
        self.assertEqual(len(set(REPOS)), 6)

    def test_testigo_de_alcance_6_de_6(self):
        """🟢 README 200 en 6 de 6: el canal LLEGA, asi que los 404 de las otras
        rutas son AUSENCIA y no incapacidad de leer (`P294`)."""
        self.assertEqual(len(testigo_de_alcance()), 6)
        self.assertEqual(cobertura('README.md'), (6, 6))

    def test_CERO_superficie_legible_por_maquina(self):
        """🔴 El hallazgo estructural: ninguno de los 6 declara mantenedor de
        forma estructurada y sin persona."""
        self.assertEqual(superficie_legible_por_maquina(), [])
        for ruta in LEGIBLES_POR_MAQUINA:
            self.assertEqual(cobertura(ruta), (0, 6), 'inesperado en %s' % ruta)

    def test_el_unico_manifiesto_es_de_69_bytes(self):
        """`SabioTechTeam/Teacher-Hub` es el unico con manifiesto, y 69 B no
        alcanzan para declarar un canal ademas del resto del objeto."""
        self.assertEqual(cobertura('package.json'), (1, 6))
        self.assertEqual(PRESENCIA['package.json']['SabioTechTeam/Teacher-Hub'], 69)

    def test_la_unica_superficie_es_PROSA(self):
        """Lo que cierra `P342` como no automatizable: la unica superficie
        presente en los 6 es prosa libre."""
        presentes = [r for r in RUTAS if cobertura(r)[0] > 0]
        self.assertEqual(presentes, ['README.md', 'package.json'])
        self.assertNotIn('README.md', LEGIBLES_POR_MAQUINA)

    def test_el_denominador_de_sondas_queda_escrito(self):
        self.assertEqual(len(RUTAS), 10)
        self.assertEqual(SONDAS_POR_REPO, 20)
        self.assertEqual(len(REPOS) * SONDAS_POR_REPO, 120)


class ControlesNegativos(unittest.TestCase):

    def test_NEGATIVE_ninguna_ruta_registra_contenido(self):
        """🔴 El control que importa: esta tabla guarda ENTEROS (bytes), nunca
        texto. Si alguna entrada fuera `str`, se habria publicado payload."""
        for ruta, repos in PRESENCIA.items():
            for repo, val in repos.items():
                self.assertIsInstance(val, int, 'contenido en %s/%s' % (ruta, repo))
                self.assertGreater(val, 0)

    def test_NEGATIVE_ruta_inventada_da_cero_sobre_el_mismo_denominador(self):
        self.assertEqual(cobertura('NO-EXISTE-p350.md'), (0, 6))

    def test_NEGATIVE_package_json_no_cuenta_como_legible_sin_persona(self):
        """`author`/`maintainers` SON datos personales: `package.json` no entra
        en la cubeta de superficie legible, aunque sea estructurado."""
        self.assertIn('package.json', ESTRUCTURADAS_CON_PERSONA)
        self.assertNotIn('package.json', LEGIBLES_POR_MAQUINA)

    def test_NEGATIVE_cero_legible_no_es_cero_alcanzable(self):
        """Las dos cifras son distintas y no hay que confundirlas: 0 superficies
        legibles CON 6 de 6 alcanzables es un hallazgo; 0 y 0 seria un canal muerto."""
        self.assertEqual(len(superficie_legible_por_maquina()), 0)
        self.assertEqual(len(testigo_de_alcance()), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
