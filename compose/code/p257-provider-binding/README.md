---
industry: education
region: Global
updated: 2026-10-04
---

# P257 — la LIGADURA DE PROVEEDOR, medida del manifiesto (pase 86 del 2026-10-04)

La palabra `lock-in` estaba escrita en **los ocho** `.md` de este árbol —`agents/top.md`,
`agents/trending.md`, `repos/foundations.md`, `repos/trending.md`, `verticals/solutions.md`,
`intel/market.md`, `intel/trends.md` y `compose/patterns.md`— y **no existía un instrumento que la
contestara**. 🔵 **Cobertura total en prosa y cobertura cero en `compose/code/` es la firma de una
creencia heredada, no de un dato** (tendencia **667**).

## La regla

> **P257.** *Proveedores ligados* e *intercambiabilidad de la ligadura* son dos columnas, y se leen del
> **manifiesto de runtime** (`dependencies`, `peerDependencies`, `[project].dependencies`), nunca del
> README ni del nombre del repo. Una **capa de abstracción** hace intercambiable la ligadura **por
> definición** y no se somete a ningún token de proveedor: el detector de «un solo proveedor» corre
> **sólo** cuando la compuerta de abstracción dice que no hay capa. Y sin manifiesto **LEÍDO** la
> respuesta es `NO-CLAIM`, nunca «no liga nada» (`P251` en este eje).

## Invocación

| Qué | Comando | Hoy |
|---|---|---|
| la suite (imprime su total, regla 3 de `P126`) | `python3 test_binding.py` | 🟢 **37/37** |
| la calibración del canal, antes de creerle un negativo (`P249`) | `sh sweep_binding.sh --calibrate` | 🟢 `CALIBRATED good=200 bad=404` |
| el barrido real | `cat slugs.input.txt \| xargs -P 8 -I{} sh ./sweep_binding.sh {}` | → `result.2026-10-04.tsv` |
| el cruce con la capa MCP | `cat slugs.input.txt \| xargs -P 8 -I{} sh ./mcp_layer.sh {}` | → `mcp-layer.2026-10-04.tsv` |

## Lo medido sobre las 69 filas recomendables (el catálogo que fijó `p250`)

| Veredicto | n | Qué significa |
|---|---|---|
| 🟢 `UNBOUND` | **36** | manifiesto LEÍDO, cero SDK de proveedor y cero capa |
| ⚠️ `NO-CLAIM` | **21** | ningún manifiesto alcanzable por este canal |
| 🔴 `MULTI-DIRECT` | **6** | dos o más proveedores directos, sin capa |
| 🔴 `SINGLE-VENDOR` | **4** | un proveedor directo, sin capa |
| ⚠️ `MONOREPO-ROOT` | **2** | raíz de workspace: no es un manifiesto de runtime (`P258`) |
| 🔴 **`SWAPPABLE`** | **0** | **ninguna de las 69 rutea por `litellm`, `langchain` ni `@ai-sdk/*`** |

Manifiestos leídos: `package.json` **29** · `requirements.txt` **10** · `pyproject.toml` **9** = **48 de 69**.

### El cruce que da la cifra cotizable

| | `UNBOUND` | liga algo | raíz |
|---|---|---|---|
| **servidor MCP** (25) | 🟢 **21** | 🔴 4 | — |
| **no MCP** (23) | 16 | 🔴 6 | 1 |

🟢 **21 de 25 servidores MCP (84 %) no ligan ningún proveedor: la ligadura vive en el HOST.**
🔴 **Los 4 que ligan desde dentro del servidor son la excepción a cotizar**, porque ahí el mandato de
proveedor de un cliente se vuelve trabajo de código.

## 🔴 El instrumento falló DOS veces en su propio barrido, y los dos fallos están versionados

| Archivo | Publicó | 🟢 Correcto | Causa |
|---|---|---|---|
| `result-monoroot.NEGATIVE-CONTROL-2026-10-04.tsv` | `FWU-DE/ais-chat` → **UNBOUND** | **MONOREPO-ROOT** | leyó la raíz de un monorepo pnpm (`private`, 0 dependencias de runtime, `turbo` en dev). 🔴 **El producto SÍ liga: `apps/api/package.json` trae `openai`** |
| `result-overbroadgate.NEGATIVE-CONTROL-2026-10-04.tsv` | `algorithm0r/canvas-lms-mcp` y `bruchris/canvas-lms-mcp` → **MONOREPO-ROOT** | **UNBOUND** | el gate corrector salió **demasiado ancho**: esas raíces traen `pnpm-workspace.yaml` **y** 4 dependencias reales |

🔴 **La suite estaba en 34/34 cuando el gate ancho ya silenciaba dos filas de dato bueno.**
🔵 **Un gate nuevo no se valida con la suite verde: se valida con el barrido COMPLETO corrido otra vez y
diffeado contra el corte anterior** — `P126` regla 2 aplicada a un gate en vez de a un contador. Ver `P258`.

## Los falsos positivos que esta suite existe para rechazar

| Dependencia | Un lector ingenuo diría | 🟢 Correcto | Por qué |
|---|---|---|---|
| `@langchain/openai` | OpenAI directo | `SWAPPABLE` | es **capa**; el substring `openai` vive dentro del nombre de la abstracción |
| `tiktoken` | OpenAI | `UNBOUND` | es un tokenizador, no un cliente de inferencia |
| `boto3` | AWS Bedrock | `UNBOUND` | es el SDK entero de AWS; Bedrock es `@aws-sdk/client-bedrock-runtime` |
| `openai-whisper` | OpenAI | `UNBOUND` | pesos abiertos, corre local |
| `openai` en `devDependencies` | ligadura | `UNBOUND` | una herramienta de build no liga el producto |

🔵 **Es la falta de solidez que `P171` nombró para las licencias, en otro eje: el nombre de la abstracción
CONTIENE el token del proveedor que abstrae**, igual que el cuerpo de AGPL-3.0 contiene la palabra con la
que un detector ingenuo lo marca no-comercial.

## ⚠️ Cotas honestas

- **Los 21 `NO-CLAIM` no son 21 piezas sin ligadura.** Son 21 piezas cuyo manifiesto este canal no pudo
  leer; varias se distribuyen por Docker Hub o se instalan desde el código (lo midió el pase 33).
- **El eje se lee del manifiesto DECLARADO, no del código.** Una pieza que llame a una API por `httpx`
  con la URL en el código sale `UNBOUND` y estaría mal. 🔵 **Es la cota de este instrumento y se declara:
  mide la ligadura DECLARADA, que es la que un `audit` o un `SBOM` ven.**
- **La licencia no se re-litiga acá.** Es el eje de `p250` y son dos preguntas (`P257`).
