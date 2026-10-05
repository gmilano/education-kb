#!/usr/bin/env python3
"""Suite del pase 107. Controles de los tres instrumentos de `p332-figure-layer`.

Cada aserto es un control; los NEGATIVOS son los que valen. Corre sin red y sin el
arbol del corpus: fabrica sus propios casos.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import intersect_media as IM  # noqa: E402
import measure as M  # noqa: E402
import sniff_format as SF  # noqa: E402

GIF = b"GIF89a" + b"\x00" * 16
PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
JPG = b"\xff\xd8\xff\xe0" + b"\x00" * 16
WEBP = b"RIFF\x24\x00\x00\x00WEBP" + b"\x00" * 16


class Formato(unittest.TestCase):
    """`P332` — la firma manda, la extension no."""

    def test_firmas_reconocidas(self):
        self.assertEqual(SF.formato(GIF), "GIF")
        self.assertEqual(SF.formato(PNG), "PNG")
        self.assertEqual(SF.formato(JPG), "JPEG")
        self.assertEqual(SF.formato(WEBP), "WEBP")

    def test_un_png_llamado_gif_sigue_siendo_png(self):
        # el control que define el hallazgo del pase
        self.assertEqual(SF.formato(PNG), "PNG")
        self.assertNotEqual(SF.formato(PNG), "GIF")

    def test_webp_exige_las_DOS_anclas(self):
        # `RIFF` solo no es WEBP: un WAV tambien empieza con RIFF
        wav = b"RIFF\x24\x00\x00\x00WAVE" + b"\x00" * 16
        self.assertNotEqual(SF.formato(wav), "WEBP")

    def test_desconocido_no_se_adivina(self):
        self.assertTrue(SF.formato(b"\x01\x02\x03\x04\x05\x06\x07\x08").startswith("OTRO:"))

    def test_ole_no_es_imagen(self):
        self.assertEqual(SF.formato(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"), "OLE/CFB")

    def test_censo_cuenta_por_firma_no_por_nombre(self):
        with tempfile.TemporaryDirectory() as d:
            for i, blob in enumerate((PNG, PNG, JPG, GIF)):
                with open(os.path.join(d, f"figure{i}.gif"), "wb") as fh:
                    fh.write(blob)
            total, sigs, _ = SF.censo(d, [".gif"])
            self.assertEqual(total, 4)
            self.assertEqual(sigs["PNG"], 2)
            self.assertEqual(sigs["JPEG"], 1)
            self.assertEqual(sigs["GIF"], 1)

    def test_arbol_vacio_sale_con_2_y_no_publica_censo(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(SF.main([d, "--ext", ".gif"]), 2)


class Familia(unittest.TestCase):
    """`P171`/`P299`/`P329` — la familia se decide por clausula, nunca por el sha."""

    def test_by_nc_sa_no_clasifica_como_by(self):
        self.assertEqual(
            M.familia("https://creativecommons.org/licenses/by-nc-sa/4.0/"), "CC BY-NC-SA 4.0"
        )

    def test_by_limpio(self):
        self.assertEqual(M.familia("https://creativecommons.org/licenses/by/4.0/ <CC BY 4.0>"), "CC BY 4.0")

    def test_vacio_es_AUSENCIA_no_permiso(self):
        self.assertEqual(M.familia(""), "SIN-DECLARAR")
        self.assertEqual(M.familia("   "), "SIN-DECLARAR")
        self.assertIsNone(None if M.familia("") == "SIN-DECLARAR" else 1)

    def test_cc4_sin_clausulas_no_resuelve(self):
        self.assertEqual(M.familia("CC4.0"), "NO-RESUELVE")

    def test_nd_y_nc_separados(self):
        self.assertEqual(M.familia("licenses/by-nd/4.0"), "CC BY-ND 4.0")
        self.assertEqual(M.familia("licenses/by-nc/4.0"), "CC BY-NC 4.0")
        self.assertEqual(M.familia("licenses/by-sa/4.0"), "CC BY-SA 4.0")

    def test_un_sha256_NO_es_una_familia(self):
        # `P329`: una huella no nombra la cesion
        self.assertEqual(M.familia("sha256:5385a26e2face987"), "NO-RESUELVE")


class ObraDeLaFigura(unittest.TestCase):
    """`P334` — la obra se extrae del `oer`, en sus DOS formas de URL."""

    def test_las_dos_formas_de_url_dan_la_misma_obra(self):
        a = IM.obra_de("https://openstax.org/details/books/introductory-statistics")
        b = IM.obra_de("https://openstax.org/books/introductory-statistics/pages/1-1")
        self.assertEqual(a, b)
        self.assertEqual(a, "introductory-statistics")

    def test_la_edicion_es_PARTE_del_slug(self):
        # `P328`: el slug cambia de nombre entre ediciones y no son la misma obra
        self.assertNotEqual(IM.obra_de("https://openstax.org/books/precalculus/pages/1-4"),
                            IM.obra_de("https://openstax.org/books/precalculus-2e/pages/1-4"))

    def test_oer_vacio_no_se_atribuye(self):
        self.assertEqual(IM.obra_de(""), "(oer VACIO)")
        self.assertEqual(IM.obra_de("   "), "(oer VACIO)")

    def test_oer_ajeno_no_se_lee_como_openstax(self):
        self.assertEqual(IM.obra_de("https://ck12.org/algebra"), "(no-openstax)")

    def test_un_dominio_parecido_no_cuenta(self):
        self.assertEqual(IM.obra_de("https://notopenstax.example/books/x"), "(no-openstax)")


class ShaClaims(unittest.TestCase):
    """Accion C — la regla de `P329` sobre el texto de esta base."""

    def setUp(self):
        import sweep_sha_claims as SC
        self.SC = SC

    def test_huella_con_familia_al_lado_es_la_forma_CORRECTA(self):
        linea = "LICENSE 1.071 B, `sha256:5385a26e2face987` identico, MIT"
        self.assertTrue(self.SC.HUELLA.search(linea))
        self.assertTrue(self.SC.IDENT.search(linea))
        self.assertTrue(self.SC.FAMILIA.search(linea))

    def test_huella_sin_familia_cae_en_la_clase(self):
        linea = "los dos dan el mismo `sha256` y son identicos byte a byte"
        self.assertTrue(self.SC.HUELLA.search(linea))
        self.assertTrue(self.SC.IDENT.search(linea))
        self.assertFalse(self.SC.FAMILIA.search(linea))

    def test_una_familia_sin_huella_no_entra(self):
        linea = "la pieza es Apache-2.0 y no hay nada mas que decir"
        self.assertFalse(self.SC.HUELLA.search(linea) and self.SC.IDENT.search(linea))

    def test_un_hex_corto_no_es_huella(self):
        self.assertFalse(self.SC.HUELLA.search("el commit abc123 no es una huella"))

    def test_barrido_sobre_arbol_sin_md_da_cero(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "x.txt"), "w", encoding="utf-8") as fh:
                fh.write("sha256 identico")
            out = subprocess.run(
                [sys.executable, os.path.join(HERE, "sweep_sha_claims.py"), d],
                capture_output=True, text=True, check=True)
            self.assertIn("archivos .md barridos                               : 0", out.stdout)


class Integridad(unittest.TestCase):
    """Controles de forma que el encargo exige de cualquier tabla derivada."""

    def test_measure_sale_con_2_si_no_hay_content_pool(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(M.main(d), 2)

    def test_intersect_sale_con_2_si_falta_media(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(IM.main([d, os.path.join(d, "no-existe")]), 2)

    def test_sha_de_contenido_discrimina(self):
        with tempfile.TemporaryDirectory() as d:
            a = os.path.join(d, "a.bin")
            b = os.path.join(d, "b.bin")
            c = os.path.join(d, "c.bin")
            for path, blob in ((a, PNG), (b, PNG), (c, JPG)):
                with open(path, "wb") as fh:
                    fh.write(blob)
            self.assertEqual(IM.sha(a), IM.sha(b))
            self.assertNotEqual(IM.sha(a), IM.sha(c))

    def test_el_salto_final_cambia_la_huella(self):
        """`P333` — el defecto exacto que este pase encontro en una cifra publicada."""
        import hashlib
        cuerpo = b"MIT License\n\nCopyright (c) 2026\n"
        con = hashlib.sha256(cuerpo).hexdigest()
        sin = hashlib.sha256(cuerpo.rstrip(b"\n")).hexdigest()
        self.assertNotEqual(con, sin)
        self.assertEqual(len(cuerpo) - len(cuerpo.rstrip(b"\n")), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
