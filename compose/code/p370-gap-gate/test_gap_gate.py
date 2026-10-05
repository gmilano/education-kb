#!/usr/bin/env python3
"""Suite de `p370-gap-gate/`. Corre SIN el corpus: las fixtures son lineas REALES del arbol.

El caso OBLIGATORIO es la divergencia: las dos oraciones de hueco que esta base publico
—la del pase 113, con el alcance puesto, y el titular del pase 114, que lo solto— tienen
que salir con veredicto OPUESTO. Si salieran iguales, el gate seria un contador de la
palabra «CERO».
"""
import unittest

from gap_gate import (SCOPE_CHANNEL, SCOPE_INDEX, SCOPE_UNDETERMINED, V_CONTRADICHO,
                      V_NO_CLAIM, V_SOSTENIDO, region_claimed, repo_rows, scope_of,
                      verdict)

# ---------------------------------------------------------------- fixtures reales
# `intel/market.md:339`, pase 113: el hueco CON su alcance, que ademas nombra una pieza propia.
P113 = ("El hueco, declarado por TERCER pase consecutivo (`P343`): LATAM devuelve mercado, "
        "adopcion y regulacion y **CERO repositorios**. No se publica como «LATAM no produce "
        "codigo» - se publica como lo que es: **este canal no encuentra codigo de LATAM**, y "
        "las piezas LATAM que esta base si tiene aparecieron por otras vias.")

# `intel/market.md:11`, pase 114: el TITULAR, que conservo el numero y solto el alcance.
P114_TITULAR = ("Hueco declarado por CUARTO pase consecutivo: LATAM devuelve mercado, "
                "adopcion, regulacion y ahora dos instrumentos nuevos - y **CERO "
                "repositorios**. La capa de CODIGO de LATAM sigue abierta.")

# `intel/market.md:179`, MISMO pase 114: el LEDGER, que si mantuvo el alcance.
P114_LEDGER = ("Hueco declarado (4o pase consecutivo): CERO repositorios de origen LATAM. "
               "Lo buscado este pase: `AI educacion LATAM 2026 adopcion regulacion`, edtech "
               "regional. Devuelve politica y adopcion; no devuelve codigo. Un informado "
               "hueco, no cobertura.")

# `agents/top.md:7125`, la fila que contradice: MIT, LATAM, y esta base la marca ACTIVO.
FILA_TUTORIA = ("| TutorIA | https://github.com/LabSirius/TutorIA | MIT | 0 | Python | Tutor "
                "conversacional autonomo para educacion superior rural, integrado dentro de "
                "Open edX y con la API de Claude como motor | **LATAM (Pereira, Colombia)** - "
                "Grupo Sirius, Universidad Tecnologica de Pereira |")

FILA_EMEA = ("| OpenDidactia | https://github.com/nmarafo/OpenDidactia | MIT | 12 | Esquemas "
             "curriculares LOMLOE | **EMEA** (España, 17 comunidades) |")

ARBOL = [("agents/top.md", FILA_TUTORIA + "\n" + FILA_EMEA)]
ARBOL_SIN_LATAM = [("agents/top.md", FILA_EMEA)]


class TestAlcance(unittest.TestCase):
    """El alcance es lo que decide si una fila del indice puede refutar el hueco."""

    def test_p113_es_de_canal(self):
        self.assertEqual(scope_of(P113), SCOPE_CHANNEL)

    def test_p114_titular_es_de_indice(self):
        self.assertEqual(scope_of(P114_TITULAR), SCOPE_INDEX)

    def test_p114_ledger_es_de_canal_aunque_diga_cero_repositorios(self):
        # El marcador estrecho gana: la oracion dice «CERO repositorios de origen LATAM»
        # (marcador de INDICE) y tambien «lo buscado este pase» (marcador de CANAL).
        self.assertEqual(scope_of(P114_LEDGER), SCOPE_CHANNEL)

    def test_sin_marcadores_no_hay_alcance(self):
        self.assertEqual(scope_of("LATAM esta complicado este trimestre."),
                         SCOPE_UNDETERMINED)

    def test_la_palabra_cero_sola_no_alcanza(self):
        # Un hueco no se declara por decir «cero»: sin marcador, no hay afirmacion gateable.
        self.assertEqual(scope_of("LATAM: cero sorpresas."), SCOPE_UNDETERMINED)


class TestDivergenciaObligatoria(unittest.TestCase):
    """El caso que hace al instrumento un GATE y no un contador de «CERO»."""

    def test_las_dos_oraciones_reales_divergen(self):
        v113 = verdict(P113, ARBOL)[0]
        v114 = verdict(P114_TITULAR, ARBOL)[0]
        self.assertNotEqual(v113, v114)
        self.assertEqual(v113, V_SOSTENIDO)
        self.assertEqual(v114, V_CONTRADICHO)

    def test_divergencia_dentro_del_mismo_pase(self):
        # El titular y el ledger del pase 114 no dicen lo mismo, y el gate lo ve.
        self.assertEqual(verdict(P114_TITULAR, ARBOL)[0], V_CONTRADICHO)
        self.assertEqual(verdict(P114_LEDGER, ARBOL)[0], V_SOSTENIDO)

    def test_las_tres_citan_el_mismo_numero(self):
        # Lo que cambia entre veredictos es el ALCANCE, no la cifra: las tres dicen «CERO».
        for s in (P113, P114_TITULAR, P114_LEDGER):
            self.assertIn("CERO", s.upper())


class TestContradiccion(unittest.TestCase):
    """Un CONTRADICHO tiene que nombrar archivo, linea y slug, no publicar un conteo."""

    def test_nombra_la_fila(self):
        v, scope, reg, rows = verdict(P114_TITULAR, ARBOL)
        self.assertEqual(v, V_CONTRADICHO)
        self.assertEqual(reg, "LATAM")
        self.assertEqual(len(rows), 1)
        path, line, slug, r, placed = rows[0]
        self.assertTrue(placed)
        self.assertEqual(path, "agents/top.md")
        self.assertEqual(slug, "LabSirius/TutorIA")
        self.assertEqual(r, "LATAM")
        self.assertIsInstance(line, int)

    def test_sin_filas_el_hueco_se_sostiene(self):
        v, _, _, rows = verdict(P114_TITULAR, ARBOL_SIN_LATAM)
        self.assertEqual(v, V_SOSTENIDO)
        self.assertEqual(rows, [])

    def test_una_fila_de_otra_region_no_contradice(self):
        # Control negativo: la fila EMEA no refuta un hueco de LATAM.
        _, _, _, rows = verdict(P114_TITULAR, ARBOL_SIN_LATAM)
        self.assertNotIn("nmarafo/OpenDidactia", [r[2] for r in rows])

    def test_hueco_sin_region_no_se_gatea(self):
        v, _, reg, _ = verdict("Esta base no tiene nada de eso.", ARBOL)
        self.assertIsNone(reg)
        self.assertEqual(v, V_SOSTENIDO)


class TestLecturaDeFilas(unittest.TestCase):
    """`repo_rows` lee del indice publicado, y reusa el detector compartido (`P237`)."""

    def test_encuentra_slug_y_region(self):
        rows = repo_rows(FILA_TUTORIA)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "LabSirius/TutorIA")
        self.assertIn("LATAM", rows[0][2])

    def test_no_confunde_dos_filas(self):
        rows = repo_rows(FILA_TUTORIA + "\n" + FILA_EMEA)
        self.assertEqual([r[1] for r in rows],
                         ["LabSirius/TutorIA", "nmarafo/OpenDidactia"])
        self.assertEqual(rows[1][2], {"EMEA"})

    def test_ignora_prosa_con_url(self):
        # Una mencion en prosa no es una fila publicada.
        self.assertEqual(repo_rows("ver https://github.com/LabSirius/TutorIA para el detalle"), [])

    def test_ignora_fila_sin_repo(self):
        self.assertEqual(repo_rows("| LATAM | mercado | 2026 |"), [])

    def test_region_reclamada_sale_del_vocabulario_cerrado(self):
        self.assertEqual(region_claimed(P114_TITULAR), "LATAM")
        self.assertIsNone(region_claimed("Brasil tiene cero repositorios."))


class TestUbicacionVsMencion(unittest.TestCase):
    """Tres formas de NOMBRAR una region en una fila, y solo una es una UBICACION."""

    def test_ubica_cuando_la_region_encabeza_la_celda(self):
        from gap_gate import placed_in
        self.assertTrue(placed_in(FILA_TUTORIA, "LATAM"))
        self.assertTrue(placed_in(FILA_EMEA, "EMEA"))

    def test_mercado_no_es_ubicacion(self):
        # `chamilo/chamilo-lms`, tal como esta publicado: habla de donde se USA (`P368`).
        from gap_gate import placed_in
        fila = ("| Chamilo | https://github.com/chamilo/chamilo-lms | GPL | 800 | LMS "
                "liviano; fuerte en LATAM y EMEA hispano/francofona |")
        self.assertFalse(placed_in(fila, "LATAM"))

    def test_prosa_del_pase_no_es_ubicacion(self):
        from gap_gate import placed_in
        fila = ("| x | https://github.com/a/b | MIT | 3 | el primer alta LATAM de esta KB "
                "en ocho pases, y entra por el eslabon que faltaba |")
        self.assertFalse(placed_in(fila, "LATAM"))

    def test_una_region_no_ubica_en_otra(self):
        from gap_gate import placed_in
        self.assertFalse(placed_in(FILA_EMEA, "LATAM"))


class TestNoClaim(unittest.TestCase):
    def test_alcance_indeterminado_es_no_claim(self):
        v, scope, _, _ = verdict("LATAM anda flojo de repos, me parece.", ARBOL)
        self.assertEqual(scope, SCOPE_UNDETERMINED)
        self.assertEqual(v, V_NO_CLAIM)

    def test_no_claim_no_cuenta_como_sostenido(self):
        self.assertNotEqual(V_NO_CLAIM, V_SOSTENIDO)


class TestFalsoNegativoDelDetectorDeCelda(unittest.TestCase):
    """El control que explica por que la fila se lee como PROSA y no como CELDA.

    🔴 Si el gate usara el detector de CELDA en su contrato (`strict=True`, su default), la
    fila real de `TutorIA` saldria SIN region —la celda mezcla region con atribucion y
    `strict` la rechaza por residuo— y el hueco falso quedaria SOSTENIDO. El gate habria
    coincidido con el pase 114 por el motivo OPUESTO: falso negativo del instrumento.
    """

    def test_el_detector_de_celda_no_ve_la_fila_real(self):
        from gap_gate import regions_named
        celdas = [c for c in FILA_TUTORIA.split("|") if "LATAM" in c]
        self.assertEqual(len(celdas), 1)
        self.assertEqual(regions_named(celdas[0]), set())

    def test_y_la_pregunta_de_prosa_si(self):
        from gap_gate import region_in_prose
        self.assertEqual(region_in_prose(FILA_TUTORIA), {"LATAM"})

    def test_prosa_no_inventa_region_desde_un_pais(self):
        from gap_gate import region_in_prose
        self.assertEqual(region_in_prose("Brasil, Mexico y Colombia"), set())

    def test_prosa_no_matchea_subcadena(self):
        from gap_gate import region_in_prose
        self.assertEqual(region_in_prose("LATAMBER no es una region"), set())


def run():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromTestCase(c) for c in
        (TestAlcance, TestDivergenciaObligatoria, TestContradiccion,
         TestLecturaDeFilas, TestUbicacionVsMencion, TestNoClaim,
         TestFalsoNegativoDelDetectorDeCelda))
    total = suite.countTestCases()
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    ok = total - len(res.failures) - len(res.errors)
    print(f"\n{ok}/{total}")
    return 0 if res.wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    sys.exit(run())


