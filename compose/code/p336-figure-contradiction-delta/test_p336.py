#!/usr/bin/env python3
"""
Pase 108 — Acciones A/B pre-registradas por el pase 107, y lo que salio al correrlas.

Esta suite NO sale a la red. Mide sobre:
  (1) los artefactos que el pase 107 dejo commiteados en este repo, y
  (2) `oer-shape.2026-10-05.tsv`, que este pase genero leyendo el arbol
      `CAHLR/OATutor-Content` en el MISMO sha que el pase 107 (`1925dec`).

Resultados que fija (todos falsables, todos con control negativo):

  P336 — la Accion B pre-registrada NO se puede correr contra el artefacto al que
         su propia pre-registracion la mando. `accion-a-b.2026-10-05.tsv` colapsa
         el campo `oer` a un clasificador de DOS valores (`openstax`/`otro`): el
         slug del libro —lo unico que distingue una edicion `2e` de una `1e`— no
         esta en el archivo. Las «825 figuras ya enumeradas» no estan enumeradas ahi.

  P337 — dos artefactos del MISMO pase, sobre el MISMO arbol, se contradicen por
         exactamente 41 figuras en el corte openstax / no-openstax
         (1.611/832 contra 1.570/873). Los dos suman 2.443. No es un error de
         conteo: es una reclasificacion.

  P338 — la causa: `oer` es TEXTO LIBRE con al menos DOS formas de URL, y en la
         muestra medida las dos formas PARTEN el espacio de slugs sin solaparse.
         Un extractor afirmado sobre `/details/books/<slug>` no pierde items
         sueltos: pierde OBRAS ENTERAS.
"""
import csv
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
FIGLAYER = os.path.join(ROOT, "compose", "code", "p332-figure-layer")
ACCION_AB = os.path.join(FIGLAYER, "accion-a-b.2026-10-05.tsv")
INTERSECCION = os.path.join(FIGLAYER, "interseccion-col30309.2026-10-05.tsv")
OER_SHAPE = os.path.join(HERE, "oer-shape.2026-10-05.tsv")

# Las 10 filas que el pase 107 publico en `interseccion-col30309.2026-10-05.tsv`.
CENSO_107 = {
    "(no-openstax)": 873,
    "introductory-statistics": 415,
    "elementary-algebra-2e": 348,
    "calculus-volume-1": 237,
    "intermediate-algebra-2e": 226,
    "college-algebra-2e": 173,
    "precalculus-2e": 134,
    "college-physics-2e": 26,
    "physics": 8,
    "university-physics-volume-1": 3,
}

DETALLE = re.compile(r"openstax\.org/details/books/([a-z0-9-]+)")
PAGINA = re.compile(r"openstax\.org/books/([a-z0-9-]+)/pages/")


def forma_de(oer):
    """Clasifica la forma de la URL. Devuelve (forma, slug)."""
    if not oer:
        return "no-openstax", ""
    m = DETALLE.search(oer)
    if m:
        return "details", m.group(1)
    m = PAGINA.search(oer)
    if m:
        return "pages", m.group(1)
    if "openstax.org" in oer:
        return "openstax-otra", ""
    return "no-openstax", ""


def _leer_tsv(path, comentario="#"):
    filas, campos = [], None
    with open(path, newline="", encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.rstrip("\n")
            if not linea or linea.startswith(comentario):
                continue
            partes = linea.split("\t")
            if campos is None:
                campos = partes
                continue
            if len(partes) == len(campos):
                filas.append(dict(zip(campos, partes)))
    return campos, filas


def leer_accion_ab():
    return _leer_tsv(ACCION_AB)


def leer_oer_shape():
    return _leer_tsv(OER_SHAPE)


class TestP336ArtefactoNoRespondeLaPregunta(unittest.TestCase):
    """La Accion B no es falsable contra el archivo al que la mandaron."""

    @classmethod
    def setUpClass(cls):
        cls.campos, cls.filas = leer_accion_ab()

    def test_artefacto_del_pase_107_existe(self):
        self.assertTrue(os.path.isfile(ACCION_AB))

    def test_cubre_las_2443_figuras(self):
        self.assertEqual(len(self.filas), 2443)

    def test_la_columna_oer_es_BINARIA_no_un_slug(self):
        vals = {f["oer_del_problema"] for f in self.filas}
        self.assertEqual(vals, {"openstax", "otro"})

    def test_ningun_slug_de_libro_sobrevive_en_el_artefacto(self):
        """Si hubiera slugs, la Accion B seria corrible. No los hay."""
        vals = {f["oer_del_problema"] for f in self.filas}
        for slug in CENSO_107:
            if slug == "(no-openstax)":
                continue
            self.assertNotIn(slug, vals)

    def test_por_lo_tanto_las_825_de_edicion_2e_NO_estan_enumeradas(self):
        n = sum(1 for f in self.filas if f["oer_del_problema"].endswith("-2e"))
        self.assertEqual(n, 0)

    def test_control_negativo_la_columna_familia_SI_discrimina(self):
        """El artefacto no es basura: otra de sus columnas si trae 3 valores."""
        vals = {f["familia_del_problema"] for f in self.filas}
        self.assertEqual(vals, {"CC BY 4.0", "SIN-DECLARAR", "NO-RESUELVE"})


class TestP337DosArtefactosDelMismoPaseSeContradicen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.campos, cls.filas = leer_accion_ab()

    def test_el_censo_107_suma_2443(self):
        self.assertEqual(sum(CENSO_107.values()), 2443)

    def test_el_artefacto_binario_tambien_suma_2443(self):
        self.assertEqual(len(self.filas), 2443)

    def test_el_corte_openstax_difiere_en_41(self):
        binario_os = sum(1 for f in self.filas if f["oer_del_problema"] == "openstax")
        censo_os = 2443 - CENSO_107["(no-openstax)"]
        self.assertEqual(binario_os, 1611)
        self.assertEqual(censo_os, 1570)
        self.assertEqual(binario_os - censo_os, 41)

    def test_el_corte_no_openstax_difiere_en_41_al_reves(self):
        binario_otro = sum(1 for f in self.filas if f["oer_del_problema"] == "otro")
        self.assertEqual(binario_otro, 832)
        self.assertEqual(CENSO_107["(no-openstax)"] - binario_otro, 41)

    def test_la_cifra_que_llego_a_la_PROSA_es_la_menor(self):
        """El pase 107 razono con 1.570, no con 1.611. Queda anotado."""
        self.assertEqual(2443 - CENSO_107["(no-openstax)"], 1570)


class TestP338LaCausaEsElTextoLibre(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.campos, cls.filas = leer_oer_shape()

    def test_artefacto_de_este_pase_existe(self):
        self.assertTrue(os.path.isfile(OER_SHAPE))

    def test_la_muestra_esta_declarada_como_parcial(self):
        with open(OER_SHAPE, encoding="utf-8") as _fh:
            cab = _fh.read(400)
        self.assertIn("NO aleatoria", cab)

    # --- controles del clasificador de forma ---

    def test_control_positivo_forma_details(self):
        f, s = forma_de(
            "https://openstax.org/details/books/elementary-algebra-2e "
            "<OpenStax: Elementary Algebra>"
        )
        self.assertEqual((f, s), ("details", "elementary-algebra-2e"))

    def test_control_positivo_forma_pages(self):
        f, s = forma_de(
            "https://openstax.org/books/precalculus-2e/pages/2-4-fitting-linear-models-to-data"
        )
        self.assertEqual((f, s), ("pages", "precalculus-2e"))

    def test_control_negativo_google_docs_no_es_cesion(self):
        f, s = forma_de("https://docs.google.com/document/d/1YmKp18kCsijuc05nVrIkmjHd3rYeFAt2/edit")
        self.assertEqual((f, s), ("no-openstax", ""))

    def test_control_negativo_host_inventado(self):
        self.assertEqual(
            forma_de("https://openstax.example.invalid/details/books/no-existe-p108"),
            ("no-openstax", ""),
        )

    def test_control_negativo_vacio(self):
        self.assertEqual(forma_de(""), ("no-openstax", ""))

    # --- el hallazgo ---

    def test_la_forma_deep_link_es_una_fraccion_que_no_se_puede_ignorar(self):
        n_pages = sum(1 for f in self.filas if f["forma_url"] == "pages")
        self.assertGreater(n_pages, 100)

    def test_las_dos_formas_PARTEN_el_espacio_de_slugs(self):
        """Ningun slug aparece en las dos formas: perder una forma pierde OBRAS."""
        det = {f["slug"] for f in self.filas if f["forma_url"] == "details" and f["slug"]}
        pag = {f["slug"] for f in self.filas if f["forma_url"] == "pages" and f["slug"]}
        self.assertTrue(det)
        self.assertTrue(pag)
        self.assertEqual(det & pag, set())

    def test_precalculus_a_secas_existe_y_NO_esta_en_ninguna_fila_del_censo_107(self):
        """Una obra entera del corpus que el censo publicado no tiene."""
        slugs = {f["slug"] for f in self.filas if f["slug"]}
        self.assertIn("precalculus", slugs)
        self.assertNotIn("precalculus", CENSO_107)

    def test_precalculus_y_precalculus_2e_son_obras_DISTINTAS(self):
        """P328: la edicion cambia la cesion. Colapsarlas cambia el veredicto."""
        slugs = {f["slug"] for f in self.filas if f["slug"]}
        self.assertIn("precalculus", slugs)
        self.assertIn("precalculus-2e", slugs)

    def test_no_se_filtra_por_extension_en_ningun_punto(self):
        """P332: la extension de un archivo de imagen no es su formato.

        El guardia inspecciona el codigo OPERATIVO (el clasificador y sus dos
        expresiones regulares), no el texto de este archivo: un guardia que se
        lee a si mismo se dispara con su propio literal.
        """
        import inspect

        operativo = inspect.getsource(forma_de) + DETALLE.pattern + PAGINA.pattern
        for prohibido in ("gif", "png", "jpeg", "webp", "endswith"):
            self.assertNotIn(prohibido, operativo.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
