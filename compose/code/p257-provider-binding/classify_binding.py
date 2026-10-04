#!/usr/bin/env python3
"""P257 — el eje de LIGADURA DE PROVEEDOR, leido del manifiesto.

Esta KB usa la palabra `lock-in` en PROSA en los ocho `.md` del arbol y NUNCA la midio.
Este instrumento la vuelve una pregunta con respuesta reproducible, y la parte en DOS
columnas, igual que `P250` partio familia de licencia y uso comercial:

  columna 1  QUE proveedores aparecen en el manifiesto de RUNTIME
  columna 2  si la ligadura es INTERCAMBIABLE (hay capa de abstraccion) o no

La compuerta, que es la que importa y es la leccion de `P250`:
el detector de «un solo proveedor» corre SOLO cuando la compuerta de abstraccion dice
que no hay capa. Una capa de abstraccion hace intercambiable la ligadura POR DEFINICION
y no se somete a ningun token de proveedor.

Y la regla de `P251` aplicada a este eje: la AUSENCIA de manifiesto no es la ausencia de
ligadura. Sin manifiesto leido la respuesta es `NO-CLAIM`, nunca `UNBOUND`.

La RAIZ DE UN MONOREPO no es un manifiesto de runtime, y por eso tiene su propio veredicto
(`MONOREPO-ROOT`, que es un `NO-CLAIM` con la causa nombrada). Es el defecto que este
instrumento COMETIO en su primer barrido real: leyo la raiz de `FWU-DE/ais-chat` —`private`,
cero dependencias de runtime, `turbo` en devDependencies— y publico `UNBOUND` sobre un
producto que SI liga Google, como lo declara el `allowBuilds: '@google/genai'` de su propio
`pnpm-workspace.yaml`. Ver `result-monoroot.NEGATIVE-CONTROL-2026-10-04.tsv`.
"""
import json
import re
import sys

# Capas de abstraccion: un SDK que habla con VARIOS proveedores detras de una interfaz.
# Si una de estas esta presente, la ligadura es intercambiable por construccion.
ABSTRACTION = {
    "litellm", "langchain", "langchain-core", "langchain-community", "langgraph",
    "llama-index", "llama_index", "llamaindex", "haystack-ai", "pydantic-ai",
    "ai", "openrouter", "aisuite", "any-llm", "portkey-ai", "instructor",
    "@langchain/core", "@langchain/community", "@langchain/openai",
    "@langchain/anthropic", "@langchain/google-genai", "@openrouter/ai-sdk-provider",
    "@ai-sdk/openai", "@ai-sdk/anthropic", "@ai-sdk/google", "@ai-sdk/provider",
    "llm", "simonw-llm", "agno", "crewai", "autogen-agentchat", "smolagents",
}
# Un prefijo de capa: todo `@langchain/*` y `@ai-sdk/*` es capa, no proveedor directo.
ABSTRACTION_PREFIX = ("@langchain/", "@ai-sdk/", "langchain-", "llama-index-")

# SDK de proveedor DIRECTO: habla con un solo proveedor y no media por nadie.
PROVIDER = {
    "openai": "OpenAI", "openai-python": "OpenAI", "tiktoken": None,
    "anthropic": "Anthropic", "@anthropic-ai/sdk": "Anthropic",
    "@anthropic-ai/claude-agent-sdk": "Anthropic",
    "google-generativeai": "Google", "google-genai": "Google",
    "@google/generative-ai": "Google", "@google/genai": "Google",
    "google-cloud-aiplatform": "Google", "vertexai": "Google",
    "cohere": "Cohere", "cohere-ai": "Cohere",
    "mistralai": "Mistral", "@mistralai/mistralai": "Mistral",
    "boto3": None, "@aws-sdk/client-bedrock-runtime": "AWS Bedrock",
    "azure-ai-inference": "Azure", "@azure/openai": "Azure",
    "ollama": "Ollama (local)", "llama-cpp-python": "local",
    "transformers": "local", "sentence-transformers": "local",
    "groq": "Groq", "together": "Together", "replicate": "Replicate",
    "dashscope": "Alibaba", "zhipuai": "Zhipu", "openai-whisper": None,
}
# `None` = aparece pero NO fija un proveedor de inferencia por si mismo.
# `tiktoken` es un tokenizador, `boto3` es el SDK entero de AWS, `openai-whisper`
# es un modelo de pesos abiertos que corre local. Marcarlos como ligadura es el
# falso positivo que este instrumento tiene que NO cometer.

RUNTIME_KEYS = ("dependencies", "peerDependencies")
# `devDependencies` queda FUERA a proposito: una herramienta de build que llama a un
# modelo no liga el producto. Es la distincion que el control (b) ejercita.

_REQ = re.compile(r"^\s*([A-Za-z0-9._-]+(?:\[[^\]]*\])?)\s*(?:[<>=!~;\[].*)?$")


def _norm(name):
    return name.split("[")[0].strip().lower()


def deps_from_package_json(text):
    """Dependencias de RUNTIME de un package.json. devDependencies excluidas."""
    try:
        doc = json.loads(text)
    except (ValueError, TypeError):
        return None
    if not isinstance(doc, dict):
        return None
    out = []
    for key in RUNTIME_KEYS:
        block = doc.get(key)
        if isinstance(block, dict):
            out.extend(_norm(k) for k in block)
    return out


def deps_from_requirements(text):
    """Dependencias de un requirements.txt. Comentarios y flags excluidos."""
    out = []
    for raw in text.splitlines():
        line = raw.split("#")[0].strip()
        if not line or line.startswith("-"):
            continue
        m = _REQ.match(line)
        if m:
            out.append(_norm(m.group(1)))
    return out


def deps_from_pyproject(text):
    """Dependencias de un pyproject.toml, sin exigir un parser de TOML.

    Lee el bloque `dependencies = [...]` de `[project]`. Los `[dependency-groups]`
    y `[tool.*.dev-dependencies]` quedan fuera por la misma razon que devDependencies.
    """
    out = []
    m = re.search(r"^\s*dependencies\s*=\s*\[(.*?)\]", text, re.S | re.M)
    if m:
        for piece in re.findall(r'["\']([^"\']+)["\']', m.group(1)):
            mm = _REQ.match(piece.strip())
            if mm:
                out.append(_norm(mm.group(1)))
    return out


PARSERS = {
    "package.json": deps_from_package_json,
    "requirements.txt": deps_from_requirements,
    "pyproject.toml": deps_from_pyproject,
}


def parse_manifest(kind, text):
    """Devuelve la lista de dependencias de runtime, o None si no se pudo leer."""
    fn = PARSERS.get(kind)
    if fn is None:
        return None
    return fn(text)


def is_abstraction(dep):
    return dep in ABSTRACTION or dep.startswith(ABSTRACTION_PREFIX)


def is_monorepo_root(kind, text, workspace_marker=False):
    """La raiz de un workspace no es un manifiesto de runtime.

    `workspace_marker` lo pone el barrido cuando encuentra un archivo de workspace
    FUERA del manifiesto (`pnpm-workspace.yaml`, `lerna.json`): pnpm no escribe los
    workspaces en el `package.json`, asi que desde el manifiesto solo no se ve.
    """
    if workspace_marker:
        return True
    if kind != "package.json" or not text:
        return False
    try:
        doc = json.loads(text)
    except (ValueError, TypeError):
        return False
    if not isinstance(doc, dict):
        return False
    # npm y yarn SI declaran los workspaces en el manifiesto.
    return bool(doc.get("workspaces"))


def classify(kind, text, workspace_marker=False):
    """Clasifica la ligadura de proveedor de un manifiesto.

    Devuelve (verdict, providers, layers). `providers` son los proveedores DIRECTOS
    nombrados; `layers` las capas de abstraccion presentes.
    """
    deps = parse_manifest(kind, text) if text is not None else None
    if deps is None:
        # Sin manifiesto LEIDO no hay nada que afirmar: regla de P251 en este eje.
        return "NO-CLAIM", [], []

    # Una raiz es INCONTESTABLE solo si NO declara NINGUNA dependencia de runtime.
    # Un marcador de workspace por si solo NO alcanza: `algorithm0r/canvas-lms-mcp` y
    # `bruchris/canvas-lms-mcp` traen `pnpm-workspace.yaml` Y un root con cuatro
    # dependencias reales (`@modelcontextprotocol/sdk`, `zod`...), asi que su raiz SI es
    # un paquete y la respuesta correcta es `UNBOUND`. El primer corte de este gate los
    # silencio: ver `result-overbroadgate.NEGATIVE-CONTROL-2026-10-04.tsv`.
    if not deps and is_monorepo_root(kind, text, workspace_marker):
        return "MONOREPO-ROOT", [], []

    layers = sorted({d for d in deps if is_abstraction(d)})
    # La compuerta de P250 aplicada aca: el detector de proveedor directo corre
    # SOLO sobre lo que no es capa. `@langchain/openai` es capa, no OpenAI directo.
    providers = sorted({
        PROVIDER[d] for d in deps
        if d in PROVIDER and PROVIDER[d] is not None and not is_abstraction(d)
    })

    if layers:
        return "SWAPPABLE", providers, layers
    if not providers:
        return "UNBOUND", [], []
    if len(providers) == 1:
        return "SINGLE-VENDOR", providers, []
    return "MULTI-DIRECT", providers, []


def main():
    kind = sys.argv[1] if len(sys.argv) > 1 else "package.json"
    marker = len(sys.argv) > 2 and sys.argv[2] == "--workspace-marker"
    text = sys.stdin.read()
    verdict, providers, layers = classify(kind, text, marker)
    print("%s\t%s\t%s" % (verdict, ",".join(providers) or "-", ",".join(layers) or "-"))


if __name__ == "__main__":
    main()
