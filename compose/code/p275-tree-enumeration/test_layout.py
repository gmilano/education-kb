#!/usr/bin/env python3
"""Suite de `layout.py` (P275 / P278)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import NO_CLAIM, count_ai, is_ai_dir, pick_layout, verdict  # noqa: E402


class TestFalsoPositivoDeSubcadena(unittest.TestCase):
    """🔴 El defecto que mas barato era cometer en este pase.

    Buscar `ai` como SUBCADENA en los 180 componentes de ILIAS devuelve `Mail`,
    `MainMenu`, `Container`, `ContainerReference` y `ScormAicc`. Publicar eso como
    «cinco componentes de AI en ILIAS» seria exactamente el tipo de entidad inventada
    que el encargo prohibe. El barrido real los encontro y la comparacion por segmento
    completo los descarta.
    """

    FALSOS = ["Mail", "MainMenu", "Maps", "Container", "ContainerReference",
              "ScormAicc", "Chatroom", "OnScreenChat", "Math", "Membership"]

    def test_ninguno_de_los_falsos_positivos_cuenta(self):
        for nombre in self.FALSOS:
            self.assertFalse(is_ai_dir(nombre), f"{nombre} no es componente de AI")
        self.assertEqual(count_ai(self.FALSOS), 0)

    def test_subcadena_ingenua_habria_fallado(self):
        """Fija el contraste: el metodo que NO se uso daria CINCO componentes de AI.

        Y fija tambien el limite exacto del falso positivo, porque el barrido de este
        pase uso primero un patron mas amplio (`ai|chat|llm|assist|bot`) que sumaba
        `Chatroom` y `OnScreenChat` por el token `chat`, no por `ai`. Los dos efectos
        son distintos y se miden por separado.
        """
        por_ai = sorted(n for n in self.FALSOS if "ai" in n.lower())
        self.assertEqual(
            por_ai,
            ["Container", "ContainerReference", "Mail", "MainMenu", "ScormAicc"],
        )
        por_chat = sorted(n for n in self.FALSOS if "chat" in n.lower())
        self.assertEqual(por_chat, ["Chatroom", "OnScreenChat"])
        # Y el metodo que si se uso descarta las siete.
        self.assertEqual(count_ai(self.FALSOS), 0)

    def test_los_verdaderos_si_cuentan(self):
        for nombre in ["ai", "AI", "aiprovider", "AiProvider", "chatbot", "llm",
                       "assistant", "openai", "copilot"]:
            self.assertTrue(is_ai_dir(nombre), nombre)

    def test_compara_el_ultimo_segmento(self):
        self.assertTrue(is_ai_dir("public/ai"))
        self.assertTrue(is_ai_dir("src/CoreBundle/AiProvider/"))
        self.assertFalse(is_ai_dir("components/ILIAS/Mail"))


class TestLayoutGate(unittest.TestCase):
    def test_elige_el_layout_poblado(self):
        grupos = [(["components/ILIAS"], 180), (["Modules", "Services"], 0)]
        self.assertEqual(pick_layout(grupos), (["components/ILIAS"], 180))

    def test_cae_al_layout_viejo(self):
        """🔴 P278 medido: `release_9` da CERO en `components/ILIAS`.

        El mismo arbol tiene 180 en `Modules`+`Services`. Sin esta compuerta el pase
        publicaria «ILIAS 9: 0 componentes», que mide la ruta y no el arbol.
        """
        grupos = [(["components/ILIAS"], 0), (["Modules", "Services"], 180)]
        rutas, total = pick_layout(grupos)
        self.assertEqual(rutas, ["Modules", "Services"])
        self.assertEqual(total, 180)

    def test_ningun_layout_poblado_es_no_claim(self):
        self.assertEqual(pick_layout([(["a"], 0), (["b"], 0)]), (None, 0))

    def test_la_raiz_del_repo_es_un_layout_valido(self):
        """🔴 Regresion de un defecto REAL que este pase cometio y corrigio.

        `sweep_tree.sh` usaba la cadena `layout` como bandera de "encontrado". La ruta
        del RAIZ del repo es la cadena VACIA, asi que `openeducat_erp` --cuyos 15
        modulos viven en el nivel superior-- se publicaba como LAYOUT-NO-ENCONTRADO /
        NO-CLAIM con n=15 ya contado. Centinela que colisiona con un valor real de
        dato: la misma clase que `P250` (`UNCLASSIFIED`).

        El veredicto no se deduce de la VERDAD del nombre de la ruta sino de su conteo.
        """
        rutas, total = pick_layout([([""], 15)])
        self.assertEqual(total, 15)
        self.assertIsNotNone(rutas, "la raiz no es 'no encontrado'")
        self.assertEqual(verdict(total, 0, bool(rutas)), "SIN-AI-EN-NUCLEO")
        # Y el contraste: una ruta vacia SIN poblar si es NO-CLAIM.
        self.assertEqual(pick_layout([([""], 0)]), (None, 0))


class TestVerdict(unittest.TestCase):
    def test_ausencia_cerrada(self):
        """Arbol enumerado completo y cero AI -> ausencia CERRADA, no «con limite»."""
        self.assertEqual(verdict(180, 0, True), "SIN-AI-EN-NUCLEO")

    def test_presencia_con_conteo(self):
        self.assertEqual(verdict(10923, 154, True), "TIENE-AI:154")

    def test_sin_layout_no_afirma(self):
        """Lo que separa este instrumento del del pase 92: el cero no se publica."""
        self.assertEqual(verdict(0, 0, False), NO_CLAIM)
        self.assertEqual(verdict(0, 0, True), NO_CLAIM)

    def test_ilias_las_cuatro_refs(self):
        """Las cuatro refs medidas en el pase 93, con su layout resuelto."""
        medido = {
            "release_9": (180, 0, True),    # Modules+Services
            "release_10": (193, 0, True),   # components/ILIAS
            "release_11": (180, 0, True),
            "trunk": (176, 0, True),
        }
        for ref, args in medido.items():
            self.assertEqual(verdict(*args), "SIN-AI-EN-NUCLEO", ref)


if __name__ == "__main__":
    unittest.main(verbosity=2)
