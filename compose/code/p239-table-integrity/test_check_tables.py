#!/usr/bin/env python3
"""Tests de check_tables.py. Incluye los DOS defectos reales del pase 78 como
fixtures de regresión, reducidos a su forma mínima."""
# P115-AK. `python3 -I` (isolated mode) drops the SCRIPT'S OWN DIRECTORY from
# sys.path, so a sibling import fails -- and `-I` is the invocation several of
# this KB's own gate READMEs prescribe ("green under `python3 -I`"). Measured at
# pass 115: all five python gates passed under plain `python3` and ALL FIVE
# failed under `-I`, with a ModuleNotFoundError traceback. A gate that cannot be
# RUN is a gate that passes everything, which is `P471`'s failure wearing a
# different hat. Two lines make the documented invocation true.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))

import unittest
from check_tables import (find_orphans, find_region_gaps, is_sep,
                          regions_in_cell)


def L(s):
    return s.strip("\n").split("\n")


class TestSep(unittest.TestCase):
    def test_reconoce_separadoras(self):
        for s in ("|---|", "|---|---|", "| --- | :--- |", "|:-:|-|"):
            self.assertTrue(is_sep(s), s)

    def test_rechaza_no_separadoras(self):
        for s in ("| a | b |", "|  |  |", "texto", "| LATAM | x |"):
            self.assertFalse(is_sep(s), s)


class TestOrphans(unittest.TestCase):
    def test_tabla_sana_no_da_hallazgo(self):
        self.assertEqual(find_orphans(L("""
| A | B |
|---|---|
| 1 | 2 |
| 3 | 4 |
""")), [])

    def test_regresion_P239_comentario_html_parte_la_tabla(self):
        """El defecto real de verticals/solutions.md:1501.

        Un comentario HTML entre la ultima fila y las siguientes corta el
        bloque: las filas de abajo quedan sin encabezado ni separadora.
        """
        got = find_orphans(L("""
| LMS | Puerta |
|---|---|
| Canvas | a |
<!-- pase 39: las nueve filas siguientes salen del barrido -->
| Moodle | b |
| Sisu | c |
"""))
        self.assertEqual([g[0] for g in got], [5, 6])

    def test_el_fix_real_cierra_el_hallazgo(self):
        """Re-emitir encabezado + separadora tras el comentario lo resuelve:
        es exactamente la reparacion aplicada al archivo publicado."""
        self.assertEqual(find_orphans(L("""
| LMS | Puerta |
|---|---|
| Canvas | a |
<!-- pase 39 -->
| LMS | Puerta |
|---|---|
| Moodle | b |
""")), [])

    def test_no_cuenta_tuberias_de_shell_en_bloque_de_codigo(self):
        """El falso positivo que este instrumento tuvo que corregir: una
        tuberia de shell dentro de ``` empieza con '|' y no es una tabla."""
        self.assertEqual(find_orphans(L("""
```
curl -s x \\
| jq -r '.a'
```
""")), [])

    def test_fila_suelta_sin_tabla_alguna(self):
        got = find_orphans(L("""
texto

| LATAM | confirmacion |
"""))
        self.assertEqual([g[0] for g in got], [3])


class TestRegionGaps(unittest.TestCase):
    def test_regresion_P240_falta_LATAM(self):
        """El defecto real de intel/market.md:582 — la tabla de cuatro
        regiones publicaba tres porque la fila LATAM se habia caido."""
        got = find_region_gaps(L("""
| Region | Resultado |
|---|---|
| North America | x |
| EMEA | y |
| APAC | z |
"""))
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0][2], ["LATAM"])

    def test_cuatro_regiones_completas_no_dan_hallazgo(self):
        self.assertEqual(find_region_gaps(L("""
| Region | Resultado |
|---|---|
| North America | x |
| EMEA | y |
| APAC | z |
| LATAM | w |
""")), [])

    def test_global_no_se_exige(self):
        """Global es del vocabulario pero no es una region de barrido: una
        tabla con las cuatro no debe reclamar que falta Global."""
        got = find_region_gaps(L("""
| Region | R |
|---|---|
| North America | x |
| EMEA | y |
| APAC | z |
| LATAM | w |
"""))
        self.assertEqual(got, [])

    def test_una_sola_coincidencia_no_es_tabla_de_region(self):
        """Con una sola region la coincidencia es casual: no se reclama."""
        self.assertEqual(find_region_gaps(L("""
| Alcance | Valor |
|---|---|
| Global | 9,58 |
| Otro | 1 |
""")), [])

    def test_negrita_y_backticks_no_impiden_el_match(self):
        got = find_region_gaps(L("""
| Region | R |
|---|---|
| **North America** | x |
| **EMEA** | y |
| **APAC** | z |
"""))
        self.assertEqual(got[0][2], ["LATAM"])


class TestRegionNormalization(unittest.TestCase):
    """Los TRES falsos positivos que la v1 de este instrumento produjo sobre el
    archivo publicado, cada uno como test. Se midieron antes de publicar."""

    def test_FP1_emoji_en_la_celda_no_impide_el_match(self):
        """intel/market.md:8730 — la tabla tiene las CUATRO regiones; la v1
        reclamaba APAC y LATAM por el emoji y el parentesis."""
        self.assertEqual(find_region_gaps(L("""
| Region | Que obliga | Fecha |
|---|---|---|
| EMEA | AI Act, Anexo III punto 3 | 2027-12-02 |
| APAC (Vietnam) | lista de 6 sectores | 2027-03-01 |
| North America | leyes estatales | vigentes |
| LATAM | ningun instrumento | - |
""")), [])

    def test_FP2_celda_combinada_nombra_dos_regiones(self):
        """compose/patterns.md:9503 — `**APAC / LATAM**` es UNA celda con DOS
        regiones; la v1 no la leia y reclamaba las dos."""
        self.assertEqual(find_region_gaps(L("""
| Region | Que es |
|---|---|
| **North America** | casi reuso |
| **EMEA** | adopcion del armazon |
| **APAC / LATAM** | adopcion del armazon |
""")), [])

    def test_FP3_alcance_declarado_suprime_el_reclamo(self):
        """compose/patterns.md:9765 — tabla legitimamente parcial («las dos
        regiones que legislan sobre la nota»). Con marcador, no se reclama."""
        self.assertEqual(find_region_gaps(L("""
<!-- p240-scope: North America, EMEA -->
| Region | Instrumento |
|---|---|
| **North America** | Oklahoma SB 1734 |
| **EMEA** | AI Act Anexo III |
""")), [])

    def test_sin_marcador_la_misma_tabla_SI_se_reclama(self):
        """El marcador debe ser explicito: sin el, la tabla parcial se reclama.
        Es el punto del eje — una tabla incompleta no debe pasar por completa."""
        got = find_region_gaps(L("""
| Region | Instrumento |
|---|---|
| **North America** | Oklahoma SB 1734 |
| **EMEA** | AI Act Anexo III |
"""))
        self.assertEqual(got[0][2], ["APAC", "LATAM"])

    def test_variante_de_vocabulario_NO_cuenta_como_region(self):
        """`Asia Pacific` no es `APAC`. El vocabulario es cerrado: la variante
        debe seguir contando como FALTA, que es el defecto real de
        repos/trending.md:1574."""
        got = find_region_gaps(L("""
| Terna | Veredicto |
|---|---|
| **North America** | inconsistente |
| **Asia Pacific** | inconsistente |
| **Global** | consistente |
"""))
        self.assertIn("APAC", got[0][2])

    def test_regions_in_cell_directo(self):
        self.assertEqual(regions_in_cell("| 🔴 **LATAM**"), {"LATAM"})
        self.assertEqual(regions_in_cell("APAC (Vietnam)"), {"APAC"})
        self.assertEqual(regions_in_cell("**APAC / LATAM**"), {"APAC", "LATAM"})
        self.assertEqual(regions_in_cell("Asia Pacific"), set())
        self.assertEqual(regions_in_cell("North America y EMEA"),
                         {"North America", "EMEA"})


class TestStrictRegionCell(unittest.TestCase):
    """Los CUATRO falsos positivos de la v2, todos de la misma causa: leer como
    celda de region cualquiera que CONTUVIERA el nombre de una."""

    def test_FP4_columna_de_perfil_de_cliente_no_es_de_region(self):
        """verticals/solutions.md:2127 — la primera columna es «Si el cliente
        es...», no una region."""
        self.assertEqual(find_region_gaps(L("""
| Si el cliente es | Plataforma |
|---|---|
| Ministerio o sistema publico, APAC / LATAM / Africa | Sunbird |
| Distrito o estado de EE UU, K-12 | Ed-Fi |
""")), [])

    def test_FP5_columna_de_cifras_no_es_de_region(self):
        """intel/market.md:139 — `86 % NA / 92 % LATAM / 66 % APAC` es una
        celda de CIFRAS de adopcion."""
        self.assertEqual(find_region_gaps(L("""
| Serie | Que mide |
|---|---|
| 86 % NA / 92 % LATAM / 66 % APAC | adopcion |
| 10,6 MM US$ CAGR 40,9 % | gasto |
""")), [])

    def test_FP6_columna_de_consulta_no_es_de_region(self):
        """intel/market.md:8908 — la celda es la CONSULTA corrida."""
        self.assertEqual(find_region_gaps(L("""
| Consulta | Que devolvio |
|---|---|
| AI education {NA, EMEA, APAC, LATAM} 2026 adoption | regulacion |
| top open source AI agents education 2026 | listicles |
""")), [])

    def test_la_celda_estricta_sigue_contando(self):
        """El arreglo no debe apagar el eje: una columna de region de verdad,
        con decoracion y celda combinada, se sigue leyendo."""
        got = find_region_gaps(L("""
| Region | R |
|---|---|
| 🔴 **North America** | x |
| **APAC / LATAM** | y |
"""))
        self.assertEqual(got[0][2], ["EMEA"])

    def test_regions_in_cell_estricto(self):
        self.assertEqual(regions_in_cell("86 % NA / 92 % LATAM"), set())
        self.assertEqual(regions_in_cell("APAC / LATAM / Africa"), set())
        self.assertEqual(regions_in_cell("**APAC / LATAM**"), {"APAC", "LATAM"})
        self.assertEqual(regions_in_cell("APAC (Vietnam)"), {"APAC"})
        # sin strict, el comportamiento permisivo de la v2 queda disponible
        self.assertEqual(regions_in_cell("86 % NA / 92 % LATAM", strict=False),
                         {"LATAM"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
