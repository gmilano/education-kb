"""Suite de `P637`.  Corre OFFLINE y DESDE SU PROPIO DIRECTORIO (`P621`: nunca con
`python3 -I`, que saca el directorio del script de `sys.path`).

Lo que esta suite afirma no es «el clasificador anda»: es que la COMPUERTA DE ACUERDO
distingue las tres clases que importan — ACUERDO, DEFECTO (alguien leyo menos) y CONTRATO
(alguien es grueso a proposito) — y que el desempate es la lectura de primera mano y NO la
mayoria.  `P637`: sobre `openeducat` la mayoria estaba mal.
"""
import unittest

import agreement

# El payload REAL que cerro `Gap 256`: `openeducat/openeducat_erp`, master/LICENSE.
# Es la UNICA plataforma LGPL del estante de `verticals/solutions.md`.
OPENEDUCAT = (
    "\n For copyright information, please see the COPYRIGHT file.\n\n"
    "OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, "
    "Version 3 (LGPLv3), as included below. Since the LGPL is a set of "
    "additional permissions on top of the GPL, the text of t")

GPL3 = ("                    GNU GENERAL PUBLIC LICENSE\n"
        "                       Version 3, 29 June 2007\n\n"
        " Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>\n")

MIT = ("MIT License\n\nCopyright (c) 2014 Transcordia\n\n"
       "Permission is hereby granted, free of charge, to any person obtaining a copy")


class TestLectores(unittest.TestCase):
    def test_los_tres_lectores_cargan(self):
        """`P614`: si un lector no carga, la suite se NIEGA en vez de pasar en verde."""
        r = agreement.leer_todos(MIT)
        self.assertEqual(set(r), {'compartido', 'p419', 'grant_gate'})
        for nombre, v in r.items():
            self.assertFalse(v.startswith('ERROR:'),
                             'el lector %s no cargo: %s' % (nombre, v))

    def test_gap256_cerrado_el_compartido_lee_la_version(self):
        """El corazon de `Gap 256`: el compartido contestaba `LGPL` sobre este payload."""
        self.assertEqual(agreement.leer_todos(OPENEDUCAT)['compartido'], 'LGPL-3.0')

    def test_compartido_y_p419_ahora_coinciden_sobre_openeducat(self):
        r = agreement.leer_todos(OPENEDUCAT)
        self.assertEqual(r['compartido'], r['p419'])
        self.assertEqual(r['p419'], 'LGPL-3.0')


class TestAdjudicacion(unittest.TestCase):
    def test_openeducat_es_CONTRATO_no_DEFECTO(self):
        """Despues del arreglo solo `grant_gate` queda grueso, y eso es su contrato."""
        a = agreement.adjudicar(OPENEDUCAT)
        self.assertEqual(a['clase'], 'CONTRATO')
        self.assertEqual(a['veredicto'], 'LGPL-3.0')

    def test_acuerdo_limpio_sobre_familias_sin_version(self):
        self.assertEqual(agreement.adjudicar(MIT)['clase'], 'ACUERDO')

    def test_gpl3_no_se_confunde_con_lgpl(self):
        """Control negativo de `P171`/`P634`: ensanchar LGPL no se come la rama GPL."""
        r = agreement.leer_todos(GPL3)
        self.assertEqual(r['compartido'], 'GPL-3.0')

    def test_el_desempate_es_el_estante_y_no_la_mayoria(self):
        """`P637`, la propiedad entera.  Se simula el estado PREVIO al arreglo: dos lectores
        dicen `LGPL` y uno dice `LGPL-3.0`.  La mayoria dice `LGPL` y ESTA MAL."""
        orig = agreement.LECTORES
        try:
            agreement.LECTORES = (
                ('compartido', lambda t: 'LGPL'),
                ('p419', lambda t: 'LGPL-3.0'),
                ('grant_gate', lambda t: 'LGPL'),
            )
            sin = agreement.adjudicar(OPENEDUCAT)
            self.assertEqual(sin['clase'], 'DEFECTO',
                             'dos lectores que pretenden la misma granularidad y difieren')
            con = agreement.adjudicar(OPENEDUCAT, respuesta_del_estante='LGPL-3.0')
            self.assertEqual(con['veredicto'], 'LGPL-3.0')
            # Y la mayoria, que es lo que NO se usa:
            self.assertEqual(
                sorted(sin['respuestas'].values()).count('LGPL'), 2,
                'la mayoria decia LGPL; el estante decia LGPL-3.0 y el estante tenia razon')
        finally:
            agreement.LECTORES = orig

    def test_contradiccion_de_familia_es_INDECIDIBLE_sin_estante(self):
        """Familias distintas no es granularidad: no se elige la mas larga."""
        orig = agreement.LECTORES
        try:
            agreement.LECTORES = (('compartido', lambda t: 'GPL-3.0'),
                                  ('p419', lambda t: 'LGPL-3.0'))
            a = agreement.adjudicar(MIT)
            self.assertEqual(a['clase'], 'CONTRADICCION')
            self.assertEqual(a['veredicto'], 'INDECIDIBLE')
        finally:
            agreement.LECTORES = orig

    def test_lector_que_explota_no_se_silencia(self):
        orig = agreement.LECTORES
        try:
            def boom(t):
                raise ValueError('x')
            agreement.LECTORES = (('compartido', lambda t: 'MIT'), ('p419', boom))
            r = agreement.leer_todos(MIT)
            self.assertTrue(r['p419'].startswith('ERROR:'))
        finally:
            agreement.LECTORES = orig


if __name__ == '__main__':
    unittest.main(verbosity=2)
