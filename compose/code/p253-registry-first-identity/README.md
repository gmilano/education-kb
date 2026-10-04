---
industry: education
region: Global
updated: 2026-10-04
---

# `p253-registry-first-identity/` — la identidad de paquete no es un hecho a una sola profundidad

**Pase 84 del 2026-10-04.** Este instrumento existe por una frase del pase 83 (tendencia **646**):

> *«los 7 del racimo `Vishal Sachdev` **publican** el MISMO `name` —`canvas-mcp-code-api`— y los 7
> tienen el campo `repository` AUSENTE. Siete repositorios, un nombre de paquete, cero punteros:
> quien resuelva por paquete no aterriza en el padre equivocado, no aterriza en ninguno. La
> resolución por capa de paquete en esta familia es **indecidible**.»*

🔴 **Las dos mitades están mal, y el defecto es de CAPA.** Medido contra el registro por un canal
calibrado:

1. **`canvas-mcp-code-api` NO existe en npm — da 404.** Los 7 árboles **DECLARAN** ese nombre; ninguno
   lo publica. 🔵 **Un `package.json` en un árbol es una DECLARACIÓN; el registro es la PUBLICACIÓN**,
   y el pase 83 llamó «publican» a lo primero.
2. **La resolución no es indecidible: aterriza, y aterriza bien.** `canvas-mcp` **sí** está publicado
   —mantenedor **`vishalsachdev`**, `repository.url` → `vishalsachdev/canvas-mcp`— o sea **el mismo
   origen que el canal del titular del `LICENSE` había coronado en el pase 83**. 🟢 **Dos canales
   independientes convergen en el mismo padre**, que es la condición que esta base exige antes de
   promover una afirmación.

## La causa medida: dos manifiestos a dos profundidades

| Profundidad | Manifiesto | Publicado |
|---|---|---|
| `./package.json` | `canvas-mcp-code-api@1.0.6`, `repository` **ABSENT** | 🔴 **no** (404) |
| `./cli/package.json` | `canvas-mcp@1.1.0`, `repository.directory: "cli"` | 🟢 **sí** |

🔵 **Un instrumento que lee profundidad 0 y le pregunta al registro por ESE nombre no mide ninguna de
las dos cosas: mide la intersección de sus propias dos conjeturas.** De ahí **`P253`**.

⚠️ **Acreditación, porque la mitad de esta regla ya existía:** **`P188`** (pase 67) escribió que *«una
URL de `repository` DECLARADA es una afirmación, no un canal»* con la prueba ¿declara? / ¿resuelve? —
🔴 **pero sólo en la dirección registro → repo.** Este instrumento es **el espejo** (árbol → registro)
más el eje de **profundidad**, y existe porque `P188` nunca se volvió compuerta ejecutable en la
dirección que faltaba (`P237`/`P252`).

⚠️ **Y lo que aterriza no es lo que se busca:** el paquete publicado son **2.704 B y 5 archivos**
(`bin/cli.js`, `lib/clients.js`, `lib/config-writer.js`, `lib/wizard.js`, `package.json`) y se
describe como *«Setup wizard for Canvas MCP»*. **No trae servidor MCP ni una sola herramienta**, así
que la resolución acierta el REPOSITORIO y **sigue sin contestar la pregunta de superficie del
gap 647**.

## El hallazgo que no se buscaba: el artefacto publicado del origen sólo se reproduce desde un FORK

Los 5 archivos del *tarball*, sondeados en los dos árboles a `HEAD`:

| Archivo | `vishalsachdev/canvas-mcp` (origen) | `fdis111/canvas-mcp` (fork) | vs *tarball* |
|---|---|---|---|
| `cli/package.json` | 🔴 404 | 🟢 200 | **idéntico** |
| `cli/bin/cli.js` | 🔴 404 | 🟢 200 | **idéntico** |
| `cli/lib/clients.js` | 🔴 404 | 🟢 200 | **idéntico** |
| `cli/lib/wizard.js` | 🔴 404 | 🟢 200 | **idéntico** |
| `cli/lib/config-writer.js` | 🔴 404 | 🟢 200 | ⚠️ **DIFIERE** |

✅ **Control positivo en la misma corrida:** `package.json`, `README.md` y `LICENSE` de la raíz del
origen dan **200**, así que `HEAD` resuelve y los 404 de `cli/` son **reales**, no un artefacto del
*ref*.

🔵 **El puntero del registro apunta a un camino que ya no existe en el árbol al que apunta**
(`repository.directory: "cli"` sobre un `cli/` que hoy da 404 en el origen), **mientras un fork sí lo
conserva.** ⚠️ **Y el quinto archivo no es una copia: es una REFACTORIZACIÓN** — el fork colapsa
`configureJsonClient` + `configureCodexClient` en un solo `updateConfigFile(client, mutate)` con
interruptor de formato, **86 → 78 líneas (2.170 B → 2.128 B)**. De ahí **`P254`**.

## La COMPUERTA, declarada antes del resultado

🔴 **Ninguna lectura de árbol puede, por sí sola, producir «no tiene paquete», y ningún 404 sobre un
nombre CONJETURADO puede producir «no publicado».** Las dos salen `UNDETERMINED`.

**El caso del mundo que lo obliga:** `owentaylor/canvas-mcp` publica como **`@owen-x-tech/canvas-mcp`**
— 🔴 **el *scope* de npm NO es el dueño de GitHub**, así que construir `@<dueño>/<repo>` y leer su 404
como ausencia es exactamente el error que esta compuerta rechaza. **Los 8 nombres conjeturados de este
pase dieron 404 y ninguno se publica como hallazgo.**

## Y la lectura de árbol falla en LOS DOS sentidos

| Dirección | Caso | Cuántos |
|---|---|---|
| **sobre-reporta** | el árbol declara un nombre que no existe en el registro | 🔴 **5** |
| **sub-reporta** | el registro publica algo que la lectura de árbol anotó como `-` | 🔴 **3** |

Los 3 sub-reportados: `@imazhar101/mcp-canvas-server` **2.1.3**, `@mtgibbs/canvas-lms-mcp` **0.2.18**,
`@owen-x-tech/canvas-mcp` **1.1.0**. 🔵 **Son instalables hoy y el inventario los tenía como «sin
paquete».**

## La trampa de colisión entre capas

`collision.2026-10-04.tsv`: el nombre de npm **`mcp-canvas-lms`** lo mantiene **`mistercommand`** y
**no trae puntero de repositorio**, mientras el repo `DMontgomery40/mcp-canvas-lms` publica bajo
**`canvas-mcp-server`**. 🔴 **Casar «nombre de npm == nombre de repo» aterriza en OTRO actor.**

## Invocación

| Qué | Comando | Hoy |
|---|---|---|
| la compuerta y los controles negativos | `python3 test_identity.py` | 🟢 **27/27** |
| el barrido real, registry-first (se niega a correr si el canal no discrimina) | `sh sweep_identity.sh canvas-mcp canvas-mcp-code-api canvas-lms-mcp` | 🟢 `CALIBRATED` |

⚠️ **Cota de procedencia de este pase, declarada porque cambia cuánto pesa la cifra:** las **27/27**
son de código **escrito en este pase**. 🔴 **La ejecución de las 35 suites PREEXISTENTES de este árbol
clonado quedó NEGADA (`[Code from External]`)**, como en los pases 58, 67, 79, 80 y 81, **así que la
columna «Hoy» del `README.md` de la raíz NO se re-verificó en el pase 84.** 🔵 **La frontera medida fue
exactamente ésa —código de este pase sí, suites preexistentes no— y no se eleva a regla del entorno:
varía entre pases, y generalizarla es el error que los pases 50, 51 y 58 cometieron en una dirección y
el 52, el 66 y el 75 en la otra.**
