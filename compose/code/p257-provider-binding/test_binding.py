#!/usr/bin/env python3
"""Suite de P257. Imprime su propio total (regla 3 de P126).

Los controles que importan son los NEGATIVOS, y son cuatro familias:

 (a) la AUSENCIA de manifiesto no es la ausencia de ligadura  -> `NO-CLAIM`, nunca `UNBOUND`
 (b) una dependencia de BUILD no liga el producto             -> devDependencies fuera
 (c) `@langchain/openai` es CAPA, no OpenAI directo           -> el trampa de substring
 (d) un tokenizador o un SDK de nube no fijan un proveedor    -> el falso positivo a no cometer
 (e) la RAIZ DE UN MONOREPO no es un manifiesto de runtime    -> el defecto que ESTE instrumento cometio
"""
import classify_binding as cb

checks = []


def check(label, got, want):
    ok = got == want
    checks.append(ok)
    print("%s %s\n    esperado=%r\n    obtenido=%r" % ("PASS" if ok else "FAIL", label, want, got))


def verdict(kind, text, marker=False):
    return cb.classify(kind, text, marker)[0]


def full(kind, text):
    v, p, l = cb.classify(kind, text)
    return (v, tuple(p), tuple(l))


# ---------------------------------------------------------------- (a) NO-CLAIM
print("--- (a) la ausencia de manifiesto NO es ausencia de ligadura (P251 en este eje) ---")
check("manifiesto no leido (None) -> NO-CLAIM",
      verdict("package.json", None), "NO-CLAIM")
check("tipo de manifiesto desconocido -> NO-CLAIM",
      verdict("Makefile", "openai\nanthropic\n"), "NO-CLAIM")
check("package.json ILEGIBLE (JSON roto) -> NO-CLAIM, no UNBOUND",
      verdict("package.json", '{"dependencies": {"openai"'), "NO-CLAIM")
check("package.json que es una LISTA, no un objeto -> NO-CLAIM",
      verdict("package.json", '["openai"]'), "NO-CLAIM")
check("README que NOMBRA OpenAI no es un manifiesto -> NO-CLAIM",
      verdict("README.md", "This project uses the OpenAI API with gpt-4o."), "NO-CLAIM")
# El positivo que da sentido al negativo: un manifiesto LEIDO y vacio si puede decir UNBOUND.
check("package.json leido y SIN proveedor -> UNBOUND (y no NO-CLAIM)",
      verdict("package.json", '{"dependencies": {"express": "^4.0.0"}}'), "UNBOUND")
check("requirements.txt leido y vacio -> UNBOUND",
      verdict("requirements.txt", "# nada\n"), "UNBOUND")

# ------------------------------------------------------- (b) devDependencies
print("\n--- (b) una dependencia de BUILD no liga el producto ---")
check("openai SOLO en devDependencies -> UNBOUND",
      verdict("package.json",
              '{"dependencies": {"express": "^4"}, "devDependencies": {"openai": "^4"}}'),
      "UNBOUND")
check("openai en dependencies -> SINGLE-VENDOR",
      full("package.json", '{"dependencies": {"openai": "^4"}}'),
      ("SINGLE-VENDOR", ("OpenAI",), ()))
check("peerDependencies CUENTA como runtime",
      full("package.json", '{"peerDependencies": {"@anthropic-ai/sdk": "^0.30"}}'),
      ("SINGLE-VENDOR", ("Anthropic",), ()))
check("pyproject: [project].dependencies cuenta",
      full("pyproject.toml",
           '[project]\nname = "x"\ndependencies = [\n  "anthropic>=0.30",\n  "httpx",\n]\n'),
      ("SINGLE-VENDOR", ("Anthropic",), ()))
check("pyproject: dependency-groups de dev NO cuenta",
      verdict("pyproject.toml",
              '[project]\nname = "x"\ndependencies = ["httpx"]\n'
              '[dependency-groups]\ndev = ["openai"]\n'),
      "UNBOUND")

# ------------------------------------------------- (c) el trampa de substring
print("\n--- (c) `@langchain/openai` es CAPA, no OpenAI directo (la compuerta de P250) ---")
check("@langchain/openai -> SWAPPABLE, no SINGLE-VENDOR",
      full("package.json", '{"dependencies": {"@langchain/openai": "^0.3"}}'),
      ("SWAPPABLE", (), ("@langchain/openai",)))
check("langchain-openai (python) -> SWAPPABLE",
      verdict("requirements.txt", "langchain-openai==0.2.0\n"), "SWAPPABLE")
check("litellm SOLO -> SWAPPABLE sin proveedor directo",
      full("requirements.txt", "litellm>=1.40\n"),
      ("SWAPPABLE", (), ("litellm",)))
check("litellm + openai directo -> SWAPPABLE (la capa protege POR DEFINICION)",
      full("requirements.txt", "litellm>=1.40\nopenai>=1.0\n"),
      ("SWAPPABLE", ("OpenAI",), ("litellm",)))
check("@ai-sdk/anthropic -> SWAPPABLE por prefijo",
      verdict("package.json", '{"dependencies": {"@ai-sdk/anthropic": "^1"}}'), "SWAPPABLE")

# ------------------------------------------------- (d) falsos positivos a NO cometer
print("\n--- (d) un tokenizador o un SDK de nube no fijan proveedor ---")
check("tiktoken solo -> UNBOUND (es un tokenizador)",
      verdict("requirements.txt", "tiktoken==0.7.0\n"), "UNBOUND")
check("boto3 solo -> UNBOUND (es el SDK entero de AWS, no Bedrock)",
      verdict("requirements.txt", "boto3>=1.34\n"), "UNBOUND")
check("openai-whisper -> UNBOUND (pesos abiertos, corre local)",
      verdict("requirements.txt", "openai-whisper\n"), "UNBOUND")
check("@aws-sdk/client-bedrock-runtime SI es ligadura",
      full("package.json", '{"dependencies": {"@aws-sdk/client-bedrock-runtime": "^3"}}'),
      ("SINGLE-VENDOR", ("AWS Bedrock",), ()))
check("extras de pip no rompen el nombre: anthropic[vertex]",
      verdict("requirements.txt", "anthropic[vertex]>=0.30\n"), "SINGLE-VENDOR")
check("comentario de requirements NO cuenta",
      verdict("requirements.txt", "httpx\n# openai is optional\n"), "UNBOUND")
check("flag -r de requirements NO se lee como paquete",
      verdict("requirements.txt", "-r base.txt\nhttpx\n"), "UNBOUND")

# ------------------------------------------------- (e) la raiz de un monorepo
# El control NEGATIVO que importa es el literal: el manifiesto REAL de la raiz de
# `FWU-DE/ais-chat`, que el primer barrido de este pase clasifico `UNBOUND` sobre un
# producto que liga Google. Tiene que salir `MONOREPO-ROOT`, nunca `UNBOUND`.
print("\n--- (e) la raiz de un monorepo no es un manifiesto de runtime ---")

AIS_CHAT_ROOT = """{
  "name": "ais-chat",
  "version": "0.1.0",
  "description": "AIS.chat monorepo",
  "private": true,
  "scripts": {"build": "turbo run build", "dev": "turbo run dev"},
  "packageManager": "pnpm@11.11.0",
  "engines": {"node": ">=24.21.0"},
  "devDependencies": {
    "@ais-chat/typescript-config": "workspace:*",
    "madge": "8.0.0", "prettier": "3.9.9", "turbo": "2.11.4"
  }
}"""

check("CONTROL NEGATIVO LITERAL: la raiz de FWU-DE/ais-chat (pnpm, marker del barrido)"
      " -> MONOREPO-ROOT, no UNBOUND",
      verdict("package.json", AIS_CHAT_ROOT, True), "MONOREPO-ROOT")
check("la MISMA raiz SIN el marker: el manifiesto solo no delata a pnpm -> UNBOUND"
      " (y por eso el marker lo pone el BARRIDO, no el clasificador)",
      verdict("package.json", AIS_CHAT_ROOT), "UNBOUND")
check("workspaces de npm/yarn SI se ven en el manifiesto -> MONOREPO-ROOT sin marker",
      verdict("package.json",
              '{"private": true, "workspaces": ["apps/*"], "devDependencies": {"turbo": "2"}}'),
      "MONOREPO-ROOT")
check("workspaces en forma de OBJETO (yarn) tambien",
      verdict("package.json",
              '{"workspaces": {"packages": ["apps/*"]}, "devDependencies": {"turbo": "2"}}'),
      "MONOREPO-ROOT")
check("una raiz que SI liga algo propio NO se silencia: eso es dato",
      full("package.json",
           '{"workspaces": ["apps/*"], "dependencies": {"openai": "^4"}}'),
      ("SINGLE-VENDOR", ("OpenAI",), ()))
check("una raiz con CAPA propia tampoco se silencia",
      verdict("package.json",
              '{"workspaces": ["apps/*"], "dependencies": {"litellm": "^1"}}'),
      "SWAPPABLE")
check("el marker NO convierte un paquete con ligadura en MONOREPO-ROOT",
      verdict("package.json", '{"dependencies": {"anthropic": "^1"}}', True), "SINGLE-VENDOR")
# SEGUNDO control negativo literal del pase: el gate de arriba, en su PRIMER corte,
# silencio a los dos `canvas-lms-mcp` que traen `pnpm-workspace.yaml` Y una raiz con
# cuatro dependencias de runtime reales. Una raiz CON dependencias es un paquete.
CANVAS_LMS_MCP_ROOT = """{
  "name": "canvas-lms-mcp",
  "dependencies": {
    "@iarna/toml": "^3.0.0", "@modelcontextprotocol/sdk": "^1.0.0",
    "prompts": "^2.4.2", "zod": "^3.23.8"
  }
}"""
check("CONTROL NEGATIVO LITERAL: raiz CON dependencias + marker de workspace"
      " -> UNBOUND, no MONOREPO-ROOT",
      verdict("package.json", CANVAS_LMS_MCP_ROOT, True), "UNBOUND")
check("una raiz con workspaces de npm PERO con dependencias de runtime sigue siendo paquete",
      verdict("package.json",
              '{"workspaces": ["apps/*"], "dependencies": {"express": "^4"}}'), "UNBOUND")
check("solo devDependencies + marker -> MONOREPO-ROOT (no hay runtime que medir)",
      verdict("package.json", '{"devDependencies": {"turbo": "2"}}', True), "MONOREPO-ROOT")
check("requirements.txt NUNCA es raiz de workspace de npm",
      verdict("requirements.txt", "httpx\n"), "UNBOUND")

# ------------------------------------------------------------- multi-proveedor
print("\n--- multi-proveedor directo: intercambiable A MANO, no por construccion ---")
check("openai + anthropic sin capa -> MULTI-DIRECT",
      full("requirements.txt", "openai>=1.0\nanthropic>=0.30\n"),
      ("MULTI-DIRECT", ("Anthropic", "OpenAI"), ()))
check("ollama solo -> SINGLE-VENDOR pero el proveedor es LOCAL",
      full("requirements.txt", "ollama>=0.3\n"),
      ("SINGLE-VENDOR", ("Ollama (local)",), ()))

total = len(checks)
passed = sum(checks)
print("\n%d/%d controles pasados" % (passed, total))
raise SystemExit(0 if passed == total else 1)
