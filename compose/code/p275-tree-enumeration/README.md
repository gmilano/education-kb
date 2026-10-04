---
industry: education
region: Global
updated: 2026-10-04
---

# `p275-tree-enumeration` — para sostener una ausencia hay que ENUMERAR el árbol

> Nuevo en el **pase 93 del 2026-10-04**. Cierra el **límite** que el pase 92 declaró
> sobre su propio canal: *«ILIAS se mide en A–L, no completo […] el tramo M–Z no fue
> listado, así que el veredicto se publica como sostenido con límite y **no** como
> ausencia cerrada»*.

## El límite que cierra

El pase 92 abrió un canal nuevo (`WebFetch` sobre las páginas `tree/` de `github.com`)
y midió su cota en el mismo pase: **trunca los listados largos**. El listado de
`components/ILIAS` cortó en `LegalDocuments`, así que el veredicto de ILIAS quedó medido
en el tramo **A–L** y publicado como *sostenido con límite*.

🟢 **Un clon `--filter=blob:none --no-checkout --depth 1` baja el commit y los árboles sin
ningún blob, y `git ls-tree -d -r` enumera el árbol COMPLETO: sin truncar, sin paginar y
sin API.** Sobre ILIAS el clon tarda **< 1 s**.

**P275**: *para sostener una ausencia en un árbol hay que ENUMERARLO. Un canal que trunca
sirve para HALLAR; un negativo suyo sólo vale con el tramo declarado.*

🔵 Y vale leerlo contra **`P274`** del pase 92 (*un path de DIRECTORIO da 404 en el canal
`raw` SIEMPRE*): ese pase retiró una clase de negativo sin reemplazo, y éste le pone el
instrumento que faltaba. La ausencia dejó de ser incognoscible en este árbol.

## Resultado: el tramo M–Z de ILIAS, y la ausencia pasa a CERRADA

Datos crudos: [`result.2026-10-04.tsv`](result.2026-10-04.tsv).

| repo | ref | layout resuelto | componentes | árbol (dirs) | veredicto |
|---|---|---|---|---|---|
| `ILIAS-eLearning/ILIAS` | `release_9` | `Modules` + `Services` | **180** | 3.597 | 🟢 `SIN-AI-EN-NUCLEO` |
| `ILIAS-eLearning/ILIAS` | `release_10` | `components/ILIAS` | **193** | 4.112 | 🟢 `SIN-AI-EN-NUCLEO` |
| `ILIAS-eLearning/ILIAS` | `release_11` | `components/ILIAS` | **180** | 4.266 | 🟢 `SIN-AI-EN-NUCLEO` |
| `ILIAS-eLearning/ILIAS` | `trunk` | `components/ILIAS` | **176** | 4.369 | 🟢 `SIN-AI-EN-NUCLEO` |
| `frappe/erpnext` | `develop` | `erpnext` | 39 | 1.427 | 🟢 `SIN-AI-EN-NUCLEO` |
| `frappe/education` | `develop` | `education` | 11 | 159 | 🟢 `SIN-AI-EN-NUCLEO` |
| `openeducat/openeducat_erp` | `18.0` | **raíz del repo** | 15 | 173 | 🟢 `SIN-AI-EN-NUCLEO` |

🟢 **El tramo M–Z existe y está listado**: `Mail MainMenu Maps Math MediaCast
MediaObjects MediaPool Membership MetaData Migration Multilingualism MyStaff News Notes
Notification Notifications OnScreenChat OpenIdConnect OrgUnit Password PermanentLink
PersonalWorkspace Poll Portfolio PrivacySecurity RTE Rating Refinery Registration
Remote* Repository ResourceStorage RootFolder Saml Scorm2004 ScormAicc Search Session
Setup Skill StaticURL StudyProgramme Style Survey SystemCheck SystemFolder Table Tagging
Tasks Taxonomy TermsOfService Test TestQuestionPool Tracking Tree UI UIComponent UICore
User Utilities Verification VirusScanner WOPI WebAccessChecker WebDAV WebResource
WebServices Wiki WorkspaceFolder WorkspaceRootFolder Xml jQuery setup_ soap`.
**Ningún componente de AI, Chatbot, LLM ni Assistant en ninguna de las cuatro refs**, y
ahora sobre el árbol entero (`-r`), no sólo sobre el primer nivel.

🟢 **El veredicto de ILIAS del pase 90 queda SOSTENIDO y sin límite**: la capacidad de AI
que las fuentes le atribuyen (*AI Chat plugin*, *ILIAS Assistant*) vive en **plugins de
terceros**, fuera de este repo — que es justo por qué el núcleo da cero.

🟢 **Y las tres filas de `frappe` / `openeducat` pasan de *sostenidas por manifiesto +
árbol truncable* a *sostenidas por árbol COMPLETO*.**

## `P278` — la ruta que contiene los componentes es propiedad de la (repo, ref)

🔴 **`components/ILIAS/` da 180 directorios en `release_11` y CERO en `release_9`.** No
porque ILIAS 9 no tenga componentes, sino porque los tiene en `Modules/` (54) +
`Services/` (126) = **180**: el layout se movió en la 10.

**P278**: *un conteo de CERO sobre una ruta que no existe en esa ref mide la RUTA, no el
contenido.* Es `P270` subido una capa: ese patrón decía que un negativo sobre una ruta que
codifica un **nombre** mide el nombre; éste dice lo mismo del **layout**.

Por eso `scan` no es un contador sino una **compuerta**: recibe las rutas candidatas de la
plataforma, elige la poblada en esa ref, y si ninguna lo está devuelve `NO-CLAIM` en lugar
de cero. La compuerta está en [`layout.py`](layout.py) y su suite la fija ref por ref.

## Los tres controles, y ninguno es decorativo

| control | qué prueba | resultado |
|---|---|---|
| **C1** — ref inventada | el canal DISCRIMINA: `zzz-fake-ref-93` debe fallar el clon | 🟢 **rechazada** |
| **C2** — compuerta de layout | `release_9` no publica el cero de `components/ILIAS` | 🟢 **cae a `Modules`+`Services`, 180** |
| **C3** — control POSITIVO | el instrumento reproduce un positivo conocido: los 7 proveedores de Moodle | 🟢 **7/7** (`anthropic awsbedrock azureai deepseek gemini ollama openai`) |

🔵 **C3 es el que habilita publicar los negativos.** Un instrumento que no reproduce un
positivo conocido no sostiene una ausencia; sobre Moodle este canal enumera **10.923**
directorios sin truncar y devuelve exactamente los 7 proveedores que los pases 90 y 92
habían medido por otros dos canales.

## 🔴 Dos defectos que este pase cometió en su propio instrumento, y corrigió antes de publicar

**1. El falso positivo de subcadena, que valía cinco entidades inventadas.** Buscar `ai`
como **subcadena** en los 180 componentes de ILIAS devuelve `Mail`, `MainMenu`,
`Container`, `ContainerReference` y `ScormAicc`. Publicar eso habría sido *«cinco
componentes de AI en el núcleo de ILIAS»* — exactamente la clase de dato inventado que el
encargo prohíbe. El contador compara el **último segmento completo** contra un conjunto
cerrado de tokens, y la suite fija los diez nombres reales que lo habrían disparado.
⚠️ Con su distinción medida: `Chatroom` y `OnScreenChat` **no** entran por `ai` sino por
`chat`, que es un patrón más amplio que el barrido usó primero; son dos efectos distintos
y la suite los separa.

**2. Un centinela que colisiona con un valor real de dato.** La primera versión de
`sweep_tree.sh` usaba la cadena `layout` como bandera de *encontrado*, y la ruta de la
**raíz** del repo es la cadena **vacía**: `openeducat_erp` salía `LAYOUT-NO-ENCONTRADO` /
`NO-CLAIM` **con sus 15 módulos ya contados**. Es la misma clase que `P250`
(`UNCLASSIFIED` y *«uso comercial prohibido»* eran la misma cadena). Corregido con una
bandera aparte, y con regresión en la suite.

🔵 **Los dos defectos tienen la misma forma:** el veredicto se estaba deduciendo de la
**forma de un nombre** en vez de de una **medición**. En el primer caso el nombre del
directorio, en el segundo el nombre de la ruta.

## Suites

```
python3 test_layout.py      # 12/12 verdes
sh sweep_tree.sh            # el barrido; WORK=<dir> para reusar los clones
```

⚠️ **Cota declarada:** `--depth 1` mide **una ref por clon**, así que el costo crece
lineal con las refs, no con el tamaño del repo. Y mide el árbol **publicado en esa ref**:
nada dice de plugins de terceros, que es donde vive la capacidad de AI de ILIAS.
