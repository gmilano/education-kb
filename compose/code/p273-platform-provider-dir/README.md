---
industry: education
region: Global
updated: 2026-10-04
---

# `p273-platform-provider-dir` — el manifiesto no es donde una plataforma liga su proveedor

> Nuevo en el **pase 92 del 2026-10-04**. Cierra la **ACCIÓN** que el pase 91 dejó abierta:
> *«las otras cinco filas siguen sin ref y quedan como ACCIÓN, no como veredicto»*.

## Lo que mide, y por qué

El pase 90 publicó **siete veredictos de plataforma** leyendo, en cada repo, **un manifiesto de
runtime** (`requirements/edx/base.txt`, `Gemfile`, `composer.json`, `pyproject.toml`,
`requirements.txt`). El pase 91 le puso ref a **dos** de los siete y encontró que **Open edX
contradice el suyo**.

🔴 **Este pase mide las cinco que quedaban y encuentra que el defecto tenía una segunda causa, más
grave que la ref: en una de las cinco el manifiesto es un instrumento CIEGO.** Chamilo liga **seis**
proveedores en el núcleo y su `composer.json` no nombra **ninguno**, porque los proveedores no son
dependencias: son **clases de un directorio del núcleo** — la misma forma que esta base ya había
medido en Moodle (`public/ai/provider/*`) y que, por eso, **midió con otro instrumento sin registrar
que eran instrumentos distintos**.

**P273**: *un veredicto «SIN-PROVEEDOR» leído en un manifiesto de runtime no es un veredicto
negativo si la plataforma puede ligar proveedores en un directorio del núcleo. Es una lectura de un
instrumento ciego a esa forma.*

## Resultado: 2 de 8 plataformas contradicen su veredicto, y por causas DISTINTAS

Datos crudos: [`platform-tally.2026-10-04.tsv`](platform-tally.2026-10-04.tsv).

| plataforma | instrumento | refs | veredicto por ref | vs. pase 90 |
|---|---|---|---|---|
| `moodle/moodle` | **DIR** (subplugins) | 6 | TIENE-PROVEEDOR, **2 → 7** según versión | línea base |
| `openedx/edx-platform` | MANIFIESTO | 4 | TIENE-PROVEEDOR en `quince`/`redwood`/`sumac` | 🔴 **CONTRADICHO** (causa: **ref**) |
| `chamilo/chamilo-lms` | **DIR** (`CoreBundle/AiProvider`) | 8 | TIENE-PROVEEDOR, **0 → 5 → 6** según versión | 🔴 **CONTRADICHO** (causa: **instrumento**) |
| `instructure/canvas-lms` | MANIFIESTO | 2 | SIN-PROVEEDOR | 🟢 sostenido |
| `ILIAS-eLearning/ILIAS` | MANIFIESTO + ÁRBOL (A–L) | 4 | SIN-PROVEEDOR en núcleo | 🟢 sostenido ⚠️ con límite |
| `frappe/education` | MANIFIESTO + ÁRBOL | 2 | SIN-PROVEEDOR | 🟢 sostenido |
| `frappe/erpnext` | MANIFIESTO + ÁRBOL | 3 | SIN-PROVEEDOR | 🟢 sostenido |
| `openeducat/openeducat_erp` | MANIFIESTO-REAL + ÁRBOL | 3 | SIN-PROVEEDOR | 🟢 **NO-CLAIM → MEDIDO** |

🔵 **Las dos contradicciones no son el mismo error.** La de Open edX es de **ref** (el veredicto era
verdadero en `master` y falso en las releases). La de Chamilo es de **instrumento**: es verdadera y
falsa **en la misma ref**, según dónde se mire. La segunda es peor, porque añadir refs no la
encuentra.

## La matriz de Chamilo, que es el dato de entrega

Datos crudos: [`chamilo-provider-by-ref.2026-10-04.tsv`](chamilo-provider-by-ref.2026-10-04.tsv).
Ruta medida: `src/CoreBundle/AiProvider/<Nombre>Provider.php`.

| ref | proveedores en núcleo | cuáles | `plugin/ai_helper` | `composer.json` |
|---|---|---|---|---|
| `v1.11.40`, `1.11.x` | **0** | — | **200** (OpenAI + DeepSeek) | 0 tokens |
| `v2.0.0`, `2.0` | **5** | OpenAI, DeepSeek, Gemini, Mistral, Grok | **404** (desapareció) | 0 tokens |
| `v3.0.0`, `v3.0.1`, `3.0`, `master` | **6** | **+ Anthropic** | **404** | 0 tokens |

🔴 **El `composer.json` da CERO tokens de proveedor en las OCHO refs, incluida `v3.0.1`, donde hay
seis proveedores en el núcleo.** La contradicción es en la misma ref: no es un problema de versión,
es de dónde se lee.

🟢 **Y la regla comercial, que es lo que viaja a una propuesta** — la misma forma que `P269` sacó
para Moodle, ahora para la segunda plataforma de la vertical:

| proveedor sin código de terceros | Moodle | Chamilo |
|---|---|---|
| **Anthropic** | ≥ **5.3** | ≥ **3.0** |
| Gemini | ≥ 5.2 | ≥ 2.0 |
| DeepSeek | ≥ 5.1 | ≥ 2.0 (o 1.11 **vía plugin**) |
| Mistral / Grok | **no están en el núcleo** | ≥ 2.0 |
| OpenAI | ≥ 4.5 | ≥ 2.0 (o 1.11 **vía plugin**) |

🔴 **Y el riesgo de migración que sale de la fila de 1.11, que ninguna columna de licencia muestra:**
en `1.11.x` los dos proveedores viven en `plugin/ai_helper/` (un **plugin embarcado**, con
`AiHelperPlugin.php` y sus constantes `OPENAI_API` / `DEEPSEEK_API`), y ese directorio **da 404 desde
`v2.0.0`**. Un cliente que migre 1.11 → 2.x/3.x **no actualiza una integración: cambia su punto de
integración**, de un plugin a un servicio del núcleo (`AiProviderFactory`).

🟢 **Capacidades en el núcleo desde `v2.0.0`** (las tres refs medidas, 200 en todas):
`AiTaskGraderService.php` (**autograding**), `AiTutorChatService.php` (**tutor**),
`AiMediaFailoverService.php`, `AiProviderFactory.php`, más interfaces de **imagen** y **video**.
Es decir: la capa de autograding que esta base inventaría desde el pase 67 **ya está en el núcleo de
Chamilo 2.0+**, y no estaba registrada.

⚠️ **Licencia: `GPL-3.0`** (`LICENSE` + `license.txt` leídos en `2.0`). Novena lectura de payload de
la capa de plataforma y **novena copyleft** — la tendencia **701** se sostiene, cero permisivas.

## El límite de este pase, declarado

⚠️ **ILIAS se mide en A–L, no completo.** El listado del árbol de `components/ILIAS` **se trunca** en
`LegalDocuments`. No hay componente `AI`, `Chatbot`, `LLM` ni `Assistant` en el tramo **A–L**; el
tramo **M–Z no fue listado**, así que el veredicto se publica como *sostenido con límite* y **no**
como ausencia cerrada. La capacidad de ILIAS que las fuentes describen (*AI Chat plugin*,
*ILIAS Assistant* en modo de prueba, operación general prevista para la primavera de 2026) vive en
**plugins de terceros**, fuera de este repo — que es justo por qué el veredicto del núcleo se
sostiene.

⚠️ **`frappe/erpnext` y `frappe/education`**: árbol completo listado, cero módulos de AI. La
capacidad del ecosistema es de **apps de marketplace de terceros** (`noviz_ai`, `nextai`,
`ChatNext`), no del núcleo.

🟢 **`openeducat/openeducat_erp` pasa de NO-CLAIM a MEDIDO, y es P270 otra vez.** El pase 90 probó
`requirements.txt` → **404** y, correctamente, **no afirmó ausencia**. El manifiesto real es
**`openeducat_core/__manifest__.py`** (**200** en `16.0`, `17.0` y `18.0`): `'depends': ['board',
'hr', 'web', 'website']`, cero proveedores. Árbol completo: 15 módulos, ninguno de AI.
Licencia **LGPL-3.0**.

## Canal y su calibración (`P249`, y la regla nueva `P274`)

Controles completos: [`controls.2026-10-04.tsv`](controls.2026-10-04.tsv).

🟢 `raw.githubusercontent.com` **DISCRIMINA** en los cinco repos (200 a la buena / 404 a la ref
inventada) y es **DETERMINISTA**: **20/20** en 5 repeticiones de 4 pares `(ref, archivo)`.

🔴 **`P274`, y retira una clase entera de negativo de esta base: en este canal un path de DIRECTORIO
da 404 SIEMPRE, exista o no.** Control: `public/ai` de Moodle **404** y `public/ai/provider`
**404** —los dos **existen**— mientras `public/ai/provider/openai/version.php` da **200**. Así que
*«probé el directorio y dio 404»* **no es evidencia de ausencia**: es una propiedad del canal. Este
pase cometió exactamente ese error en su primer intento sobre Chamilo e ILIAS y lo retiró antes de
publicar.

🔴 **`P270` reconfirmado por tercera vez, y en este mismo árbol:** `OpenAi.php` → **404**,
`OpenAiProvider.php` → **200**. El nombre real salió del **listado del árbol**, no de una conjetura.

🟢 **Canal nuevo para esta base: `WebFetch` sobre `github.com/<org>/<repo>/tree/<ref>/<path>`
LISTA directorios.** Los cuatro pases anteriores registran `curl -sI github.com` y `api.github.com`
en **403**, y de ahí venía la imposibilidad de enumerar un árbol. `WebFetch` sobre la página de árbol
**sí responde**, y es el canal que encontró `src/CoreBundle/AiProvider` y los nombres reales de las
clases. ⚠️ **Con su límite medido en el mismo pase: trunca los listados largos** (ILIAS cortó en
`LegalDocuments`), así que sirve para **hallar**, y un negativo suyo necesita el tramo declarado.

## 🟢 La ejecución VOLVIÓ, después de once pases, y el pase la gastó en replicarse

🟢 **Los pases 58, 67, 79, 80, 81, 84, 86, 89, 90 y 91 registran `ejecución NEGADA
([Code from External])`. En este pase la ejecución FUNCIONA, y es la primera vez en once pases que
este árbol puede publicar `N/N`.**

| suite | resultado |
|---|---|
| suites Python (`test_*.py`) | **39 / 39 verdes** |
| suites shell (`test_*.sh`) | **2 / 2 verdes** |
| **total del árbol** | **41 / 41, cero fallos** |

🟢 **Y el linter de integridad de tablas (`P239`/`P240`) corrido sobre los OCHO archivos de contenido
da `total 0`**: cero filas huérfanas —o sea **cero encabezados compilados como dato**, que es el
defecto que esta base arrastró por varias industrias— y cero tablas de región incompletas.

🟢 **Lo primero que se gastó la ejecución recuperada fue en replicar la medición de este pase, que es
lo que el pase 91 estableció como estándar:** [`sweep_provider_dir.sh`](sweep_provider_dir.sh)
—escrito para registrar el bucle corrido a mano— **se corrió**, y sus **8 refs coinciden EXACTO** con
la tabla de arriba (`0,0,5,5,6,6,6,6`), incluida la demostración de `P274` en la misma corrida
(`dir-que-existe 404` / `archivo-en-ese-dir 200`). **Segunda cifra de esta base confirmada por segunda
mano**, después de la matriz de Moodle del pase 91.
