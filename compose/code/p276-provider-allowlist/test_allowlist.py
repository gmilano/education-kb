#!/usr/bin/env python3
"""Suite de `extract_allowlist.py` y `capability.py` (P276 / P277)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from capability import closure, parse, resolve, types_of  # noqa: E402
from extract_allowlist import extract  # noqa: E402

# Fragmento con la forma REAL del factory de Chamilo `v3.0.1`, incluidos los mapas
# VECINOS que tienen la misma forma sintactica y no son proveedores.
FACTORY = """
        $this->defaultProvider = array_key_first($config) ?? 'openai';

        $possibleProviders = [
            'openai' => 'OpenAi',
            'deepseek' => 'DeepSeek',
            'grok' => 'Grok',
            'mistral' => 'Mistral',
            'gemini' => 'Gemini',
            'claude' => 'Claude',
            'anthropic' => 'Anthropic',
        ];

        $typeSuffix = [
            'text' => '',
            'image' => 'Image',
            'video' => 'Video',
        ];
"""


class TestAllowlist(unittest.TestCase):
    def test_lee_las_siete_claves(self):
        self.assertEqual(
            [k for k, _ in extract(FACTORY)],
            ["openai", "deepseek", "grok", "mistral", "gemini", "claude", "anthropic"],
        )

    def test_no_arrastra_el_mapa_vecino(self):
        """🔴 El defecto que este test existe para impedir.

        `$typeSuffix` tiene la MISMA forma `'clave' => 'Valor'`. Un regex sin corte en
        el primer `];` devolveria `text`/`image`/`video` como si fueran proveedores:
        tres entidades inventadas, que es el defecto que el encargo prohibe.
        """
        keys = [k for k, _ in extract(FACTORY)]
        for intruso in ("text", "image", "video"):
            self.assertNotIn(intruso, keys)

    def test_prefijo_de_clase(self):
        self.assertEqual(dict(extract(FACTORY))["claude"], "Claude")
        self.assertEqual(dict(extract(FACTORY))["openai"], "OpenAi")

    def test_sin_mapa_no_afirma_cero(self):
        """Un archivo sin allowlist devuelve lista vacia -> el CLI emite NO-CLAIM."""
        self.assertEqual(extract("<?php class X {}"), [])

    def test_el_punto_ciego_del_pase_92(self):
        """P276 — la lista sondeada por el pase 92 no contenia `claude`.

        Este test fija la causa de la correccion 6 -> 7 para que no se repita: el
        conteo venia de sondear estos siete nombres, y `Claude` no esta entre ellos
        mientras `Ollama` --que no existe en Chamilo-- si estaba.
        """
        sondeados_pase_92 = [
            "OpenAi", "DeepSeek", "Gemini", "Mistral", "Grok", "Anthropic", "Ollama",
        ]
        reales = [p for _, p in extract(FACTORY)]
        self.assertIn("Claude", reales)
        self.assertNotIn("Claude", sondeados_pase_92)
        self.assertNotIn("Ollama", reales)
        # El conteo sondeado da 6 y el enumerado da 7: la diferencia es exactamente
        # `Claude`, y el sondeo ademas gasto una consulta en un nombre inexistente.
        self.assertEqual(len([p for p in reales if p in sondeados_pase_92]), 6)
        self.assertEqual(len(reales), 7)


class TestCapability(unittest.TestCase):
    def test_parse_implements(self):
        src = ("<?php\nclass DeepSeekProvider implements AiProviderInterface, "
               "AiDocumentProviderInterface\n{\n}\n")
        name, ext, ifaces = parse(src)
        self.assertEqual(name, "DeepSeekProvider")
        self.assertIsNone(ext)
        self.assertEqual(ifaces, ["AiProviderInterface", "AiDocumentProviderInterface"])

    def test_parse_final_con_extends_y_sin_implements(self):
        src = "<?php\nfinal class AnthropicProvider extends ClaudeProvider\n{\n}\n"
        name, ext, ifaces = parse(src)
        self.assertEqual((name, ext, ifaces), ("AnthropicProvider", "ClaudeProvider", []))

    def test_herencia_de_clase_no_publica_cero(self):
        """🔴 `AnthropicProvider` no declara `implements`: su superficie es la HEREDADA.

        Sin resolver `extends`, la fila de `anthropic` saldria con cero capacidades
        teniendo las dos de `ClaudeProvider`.
        """
        parsed = {
            "ClaudeProvider": (None, ["AiProviderInterface", "AiDocumentProviderInterface"]),
            "AnthropicProvider": ("ClaudeProvider", []),
        }
        surfaces = resolve(parsed)
        self.assertEqual(types_of(surfaces["AnthropicProvider"]), ["text", "document"])
        self.assertEqual(
            types_of(surfaces["AnthropicProvider"]), types_of(surfaces["ClaudeProvider"])
        )

    def test_herencia_de_interfaz_habilita_video(self):
        """🔴 NINGUN proveedor declara `AiVideoProviderInterface` literalmente.

        Los tres que hacen video declaran la Job, que la EXTIENDE. Comparando nombres
        literales el veredicto seria «cero video» teniendo tres.
        """
        ifaces = ["AiProviderInterface", "AiVideoJobProviderInterface"]
        self.assertIn("AiVideoProviderInterface", closure(ifaces))
        self.assertIn("video", types_of(ifaces))

    def test_interfaz_que_no_es_tipo_del_factory(self):
        """⚠️ Seis interfaces declaradas no son seis tipos registrables.

        `AiSearchMediaTextProviderInterface` no esta en el mapa `$typeInterface`, asi
        que no habilita ningun (proveedor, tipo). OpenAI declara SEIS interfaces y
        llega a CINCO tipos.
        """
        openai = [
            "AiProviderInterface", "AiImageProviderInterface",
            "AiVideoJobProviderInterface", "AiDocumentProviderInterface",
            "AiDocumentProcessProviderInterface", "AiSearchMediaTextProviderInterface",
        ]
        self.assertEqual(len(openai), 6)
        self.assertEqual(len(types_of(openai)), 5)
        self.assertEqual(
            types_of(openai), ["text", "image", "video", "document", "document_process"]
        )

    def test_la_superficie_no_es_uniforme(self):
        """P277 — el swap es gratis solo donde las dos clases coinciden."""
        openai = types_of([
            "AiProviderInterface", "AiImageProviderInterface",
            "AiVideoJobProviderInterface", "AiDocumentProviderInterface",
            "AiDocumentProcessProviderInterface",
        ])
        claude = types_of(["AiProviderInterface", "AiDocumentProviderInterface"])
        self.assertEqual(sorted(set(openai) & set(claude)), ["document", "text"])
        # `document_process` lo tiene OpenAI y no Claude: ese swap es desarrollo.
        self.assertIn("document_process", openai)
        self.assertNotIn("document_process", claude)

    def test_ciclo_de_herencia_no_cuelga(self):
        parsed = {"A": ("B", []), "B": ("A", ["AiProviderInterface"])}
        self.assertEqual(types_of(resolve(parsed)["A"]), ["text"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
