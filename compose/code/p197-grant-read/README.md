---
industry: education
region: Global
updated: 2026-10-14
---

# `p197-grant-read` — las filas que p196 encontró y no leyó, leídas

**Pasada `197`, `2026-10-14`.** Corre tres acciones que p196 pre-registró, con un solo
instrumento y la cadena de reglas de esta base sin reescribir una:
`lib/licence_path.sh` *(qué ruta concede — promovido en esta pasada desde
`p196-none-tree-reach`, byte a byte)*, `lib/license_family.sh` *(qué familia es)*,
`lib/payload_measure.sh` *(los bytes se miden de un FICHERO, nunca de `$(…)` — `P834`)*.

## 1. Las `3` filas `OWN-GRANT-AT-ROOT` — 🟢 son concesiones REALES, las tres

| fila | ruta | bytes | familia |
|---|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | `License.txt` | `7 651` | 🟢 **`LGPL-3.0`** |
| [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | `License` | `1 079` | 🟢 **`MIT`** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | `LICENSE.TXT` | `11 358` | 🟢 **`Apache-2.0`** |

🟢 **Limbo `1` de p196 se cumple en el hecho: ninguna es plantilla ni stub.**
🔴 **Y su ARITMÉTICA estaba mal.** El limbo decía *«concesiones reales → la cuenta de
licenciadas sube `3` y el `16.2`% baja más»*. No baja: p196 **ya había restado las `12`
filas con concesión propia** cuando calculó `16.2`% *(`88` − `12` = `76`; `76`/`468` =
`16.2`%)*. Leerlas confirma el `16.2`%; no lo mueve. 🔵 **Un limbo puede estar bien escrito
como predicción y mal como cuenta, y el que lo corre tiene que rehacer la cuenta.**

🆕 🟢 **Lo que sí aporta la lectura: `kstateome/lti-launch` cae en `7 651` B, exactamente el
intervalo «`GPL` por referencia» que p196 derivó de `odoo/odoo`.** Y
[`unslothai/notebooks`](https://github.com/unslothai/notebooks) cae en `7 652` B. **Dos
observaciones independientes a un byte** — el banda-conjunto bimodal de `LGPL-3.0` tiene
ahora corpus fuera de la fila que lo originó.

## 2. Las filas del padrón que «ningún censo alcanzó» — 🔴 la premisa era falsa

p196 registró *«`26` de las `494` filas distintas nunca fueron sondeadas»*. Plegando por
caso son **`30`**, y se sondearon todas. 🔴 **Pero «ausente del TSV del censo» no es «no
medida»:** `16` de las `30` están publicadas en las páginas **con la misma cifra de bytes
que esta pasada midió, al byte** *(ver `../p197-census-vs-pages/`)*. 🔵 **El hueco estaba en
el artefacto del censo, no en el conocimiento** — la forma exacta de la reincidencia que p194
y p195 ya se habían anotado: *leer un TSV resumen como si fuera el estado del saber*.

| estado | filas |
|---|---|
| 🟢 concesión leída de los bytes | `18` |
| 🟡 payload corto *(`<400` B: declaración, no texto)* | `1` — `enkidevs/curriculum`, `189` B, `CC-BY-NC-SA-4.0` |
| 🔴 ninguna ruta de concesión en el árbol completo | `7` |
| 🔴 **ABSENT** *(git pide credenciales, `rc=128`)* | `2` — `apereo/opencast`, `yourusername/scholarmate` |
| 🆕 🔴 **EMPTY-REPO** *(existe y no tiene refs)* | `2` — `cdweaver1992/edfi-mcp-server`, `openfresno/edgenuity-aeries-grade-passback` |

🔴 **El limbo de p196 se cumple del lado malo: la cola no sondeada está SESGADA.** Sobre las
`26` filas vivas, `7` no tienen concesión en ninguna ruta = **`26.9`%**, contra el `16.2`% del
estante. 🔵 Cada pasada agrega lo que acaba de investigar, y lo que acaba de investigar está
peor licenciado que el estante que heredó.

🔴 **`yourusername/scholarmate` es un PLACEHOLDER publicado como dirección.** Un slug
sintácticamente válido cuyo dueño es un marcador de plantilla. Es la misma clase que una
fila de encabezado compilada como entidad; la regla que lo excluiría *(dueños de plantilla:
`yourusername`, `your-org`, `username`, `example`)* queda **pre-registrada**, no improvisada.

### 🆕 🔴 Tres estados de existencia, no dos — y los dos canales de esta base se contradecían

La v1 de `read_grants.sh` usaba `git ls-remote --exit-code -h` y leía su `2` *(«ninguna ref
coincide»)* como `ABSENT`. El canal de [`p107-git-lane-census`](../p107-git-lane-census/)
usa `--heads --tags` **sin** `--exit-code` y daba esas dos filas por alcanzables con `0`
heads y `0` tags. 🔵 **Los dos canales se contradecían sobre dos filas por una diferencia de
BANDERA, no de mundo.** Un repositorio ausente contesta `128` *(git pide usuario)*; uno vacío
contesta `0` sin refs. **Son estados distintos y se publican distintos.**

## 3. Las filas nuevas del canal MCP — ninguna se publica sin concesión leída

| fila | bytes | familia |
|---|---|---|
| [`human2human-ai/moodle-tool_human2human`](https://github.com/human2human-ai/moodle-tool_human2human) | `35 149` | `GPL-3.0` |
| [`cgrevisse/moodle-qbank_genai`](https://github.com/cgrevisse/moodle-qbank_genai) | `35 178` | `GPL-3.0` |
| [`ANFAIA/SkillNet`](https://github.com/ANFAIA/SkillNet) | `10 758` | 🟢 `Apache-2.0` |
| [`microsoft/moodle-ai-assistant`](https://github.com/microsoft/moodle-ai-assistant) | `1 084` | 🟢 `MIT` |
| [`langfuse/langfuse-workshop`](https://github.com/langfuse/langfuse-workshop) | `1 073` | 🟢 `MIT` |
| [`llwand1/xuelian-agent`](https://github.com/llwand1/xuelian-agent) | `1 062` | 🟢 `MIT` |
| 🔴 [`nakafaai/nakafa.com`](https://github.com/nakafaai/nakafa.com) | `7 705` | 🔴 **`NONCOMMERCIAL-NOT-OSI`** |
| 🟡 `marcusgreen/moodle-qtype_aitext` · `bycs-lp/moodle-local_ai_manager` · `bycs-lp/moodle-block_ai_chat` · `bigdata-ustc/Agent4Edu` | — | sin ruta de concesión → van al canal de cabecera |

🔴 **El canal MCP reportó `NOASSERTION` en `nakafaai/nakafa.com`; los bytes dicen una
licencia NO COMERCIAL.** Tercera vez que `NOASSERTION` esconde una barrera comercial en dos
pasadas *(`TrenTorch`, `frappe/education`, ésta)*.

## 4. El canal de CABECERA, con el instrumento de p139 — y aquí se cae una generalización

`ABSENCE-ENUMERATED` dice *«ninguna RUTA del árbol es un texto de concesión»*. No dice *«no
hay concesión»*: `P742` registra la concesión dentro del cuerpo de un fichero. `read_headers.sh`
corre [`p139-source-header-grant/headers.py`](../p139-source-header-grant/) *(24 tests)* sin
reescribirlo.

| fila | ficheros de texto | con concesión | veredicto |
|---|---|---|---|
| 🟢 `marcusgreen/moodle-qtype_aitext` | `50` | **`40`** | 🟢 **`HEADER-GRANT` — `GRANT_GPL`** |
| 🟢 `bycs-lp/moodle-local_ai_manager` | `278` | **`255`** | 🟢 **`HEADER-GRANT` — `GRANT_GPL`** |
| 🟢 `bycs-lp/moodle-block_ai_chat` | `91` | **`64`** | 🟢 **`HEADER-GRANT` — `GRANT_GPL`** |
| 🔴 las otras `8` | — | `0` | `NO-HEADER-GRANT` |

🆕 🔴 **p139 concluyó *«`0` de `9` llevan la concesión en una cabecera»* sobre paquetes npm, y
ESO NO GENERALIZA.** En el mundo de los plugins de Moodle la tasa es **`3` de `3`**, porque el
proyecto lo exige por convención: el aviso `GNU GPL v3` va en la cabecera de cada `.php`.
🟢 **Entonces `16.2`% «sin licencia en la raíz» SOBREESTIMA la ausencia en esa capa**, y la capa
es justo la que el filtro de lenguaje de p196 no veía.

🔴 **Y el veredicto se llama `NO-HEADER-GRANT`, no «sin concesión en ninguna parte», porque
esta pasada tiene la prueba del límite en su propio corpus**:
[`xiaolai/the-craft-of-selfteaching`](https://github.com/xiaolai/the-craft-of-selfteaching)
declara `CC-BY-NC-ND` en su `README.md` y **esta base lo sabe desde p854, con fixture**.
`headers.py` reconoce SPDX, línea de copyright y las frases operativas de MIT/Apache/(A)GPL —
**no reconoce una declaración CC**. Llamarlo *«sin concesión»* sería publicar el límite del
instrumento como un hecho del repositorio.

## 5. 🔴 El hallazgo que no estaba pre-registrado: `p854` nunca llegó a ningún llamador

Medido sobre los mismos bytes, con el clasificador endurecido de esta base:

| entrada | `family_of` |
|---|---|
| el `README.md` completo *(`5 869` B, byte-idéntico al fixture committeado)* | 🔴 **`UNCLASSIFIED`** |
| **la línea de declaración sola** *(`grep -m1 'CC-BY-NC-ND'`)* | 🟢 **`CC-BY-NC-ND-3.0`** |

🔵 **La capacidad de `p854` existe y está afirmada en una suite — pero la EXTRACCIÓN que la
hace funcionar vive en el test, no en la librería.** Ningún llamador real la tiene, así que
todo canal de esta base lee ese repositorio como no licenciado. 🔴 Es `Gap 440` *(«la
corrección estaba y no viajó»)* dentro de `lib/`.

🔴 **No se arregla aquí, y la razón es una medición de p195**, no prudencia: un extractor de
declaraciones que lea *«usa libfoo (MIT)»* como *«esto es MIT»* reintroduce la clase que p195
encontró en `PageLM`, `learner-verse` y `graspful` *(tres licencias restrictivas leídas como
`MIT`)*. **Un extractor que no distingue «esta obra se licencia bajo X» de «la dependencia Y
es MIT» es peor que no tenerlo.** Pre-registrado con falsificador para p198.

## Suites verdes

| suite | resultado |
|---|---|
| [`lib/test_licence_path.sh`](../lib/) | 🟢 **`33`/`33`** — los `24` casos de p196 sin cambiar uno, `4` casos nuevos de rutas que esta pasada leyó de verdad, y **el control de identidad byte a byte** contra el original de p196 |
| [`../p197-census-vs-pages/test_compare.py`](../p197-census-vs-pages/) | 🟢 **`10`/`10`** — `2` de sus casos son las `2` acusaciones falsas que el comparador v1 emitió en esta pasada |

## Lo que NO hizo

🔴 **No leyó las `7` filas `ABSENCE-ENUMERATED` del padrón por un canal de declaración** *(el
que no existe, §5)*. 🔴 **No tocó `is_licence_path`**, que cuenta `eula` como concesión —
medido en `Lumi`, pre-registrado, **no parchado**: `P237` y el control de identidad lo
prohíben en la misma pasada que lo promovió. 🔴 **`ACTION MN` sigue SIN CORRER**, duodécima
pasada: es una escritura hacia afuera, sobre repositorios de terceros, y esta corrida no
tiene a nadie mirando.
