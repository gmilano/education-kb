#!/usr/bin/env python3
"""P275 — un arbol se ENUMERA, y la RUTA que lo contiene depende de la ref.

El pase 92 abrio un canal nuevo (`WebFetch` sobre las paginas `tree/` de github.com) y
declaro su limite en el mismo pase: **trunca los listados largos**. Por eso ILIAS quedo
medido en el tramo **A-L** (el listado corto en `LegalDocuments`) y su veredicto se
publico como *sostenido con limite*, no como ausencia cerrada.

Este instrumento retira ese limite. Un clon `--filter=blob:none --no-checkout --depth 1`
baja commit y arboles SIN blobs --sobre ILIAS tarda menos de un segundo-- y `git ls-tree`
enumera el arbol COMPLETO, sin truncar y sin paginar.

**P275**: *para sostener una ausencia en un arbol hay que ENUMERARLO. Un canal que trunca
sirve para HALLAR; un negativo suyo solo vale con el tramo declarado. Un clon sin blobs
convierte la ausencia en medible.*

Y trae su propia trampa, que es `P270` en la capa de RUTA:

**P278**: *la ruta que contiene los componentes es propiedad de la (repo, ref), no del
repo. Un conteo de CERO sobre una ruta que no existe en esa ref mide la RUTA, no el
contenido.* Medido: `components/ILIAS/` da 180 directorios en `release_11` y **CERO** en
`release_9`, donde el mismo arbol los tiene en `Modules/` (54) + `Services/` (126) = 180.
Publicar ese cero como «ILIAS 9 no tiene componentes» seria dato incorrecto.

De ahi que este modulo no sea un contador sino una COMPUERTA: dada la lista de rutas
candidatas de una plataforma, elige la que esta poblada en esa ref y, si ninguna lo esta,
devuelve `NO-CLAIM` en vez de cero.

Uso (como libreria):  from layout import pick_layout, verdict
"""

# Rutas candidatas por plataforma. Mas de una porque el layout CAMBIA entre versiones:
# ILIAS movio sus componentes de `Modules/`+`Services/` a `components/ILIAS/` en la 10.
LAYOUTS = {
    "ILIAS-eLearning/ILIAS": [
        ["components/ILIAS"],          # release_10, release_11, trunk
        ["Modules", "Services"],       # release_9 y anteriores
    ],
}

NO_CLAIM = "NO-CLAIM"


def pick_layout(counts_by_path):
    """Elige el layout poblado.

    `counts_by_path` es {ruta: n_directorios}. Devuelve (rutas_elegidas, total) del
    primer grupo con total > 0, o (None, 0) si ninguno esta poblado -> NO-CLAIM.
    """
    best = None
    for group, total in counts_by_path:
        if total > 0 and best is None:
            best = (group, total)
    return best if best else (None, 0)


def verdict(total_dirs, ai_dirs, layout_found):
    """Veredicto de ausencia, y NO afirma nada si el layout no se encontro.

    - layout no encontrado -> `NO-CLAIM` (es `P278`: el cero mide la ruta)
    - layout encontrado y 0 componentes de AI -> `SIN-AI-EN-NUCLEO` (ausencia CERRADA,
      porque el arbol se enumero completo)
    - layout encontrado y n > 0 -> `TIENE-AI` con el conteo
    """
    if not layout_found:
        return NO_CLAIM
    if total_dirs <= 0:
        return NO_CLAIM
    return "SIN-AI-EN-NUCLEO" if ai_dirs == 0 else f"TIENE-AI:{ai_dirs}"


# Tokens que marcan un componente de AI. Se comparan contra el NOMBRE COMPLETO del
# directorio, no como subcadena: `ai` como subcadena casa con `Mail`, `MainMenu`,
# `Container` y `ScormAicc`, que no son componentes de AI. Ese falso positivo esta
# medido en la suite.
AI_TOKENS = {
    "ai", "aiprovider", "chatbot", "llm", "assistant", "openai", "genai", "copilot",
}


def is_ai_dir(name):
    """¿El nombre de este directorio es un componente de AI?

    Compara el segmento COMPLETO en minusculas contra `AI_TOKENS`. Un `in` sobre la
    cadena daria `Mail` -> True, y esta base publicaria componentes de AI inventados.
    """
    return name.strip("/").split("/")[-1].lower() in AI_TOKENS


def count_ai(dir_names):
    return sum(1 for d in dir_names if is_ai_dir(d))
