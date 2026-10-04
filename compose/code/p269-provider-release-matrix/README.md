---
industry: education
region: Global
updated: 2026-10-04
---

# `p269-provider-release-matrix` — el eje de proveedor, medido por REF y en la capa de PLATAFORMA

> Nuevo en el **pase 90 del 2026-10-04**.

Este instrumento mide dos cosas que esta base afirmaba sin tenerlas medidas:

1. **Qué proveedores de modelo trae el NÚCLEO de Moodle, rama por rama** — y por lo tanto en qué
   versión entró cada uno. Un conjunto de proveedores es propiedad del par **(repo, ref)**, no del
   repo.
2. **La capa de PLATAFORMA en el eje de ligadura de proveedor** — el denominador que `P257` nunca
   tuvo: `P257` midió **69 filas de agente** y **cero plataformas**.

## ⚠️ Lo que este pase NO puede afirmar

🔴 **No hay suite y no hay total de aserciones, a propósito.** La ejecución de código del árbol está
**NEGADA** en este pase (`[Code from External]`), igual que en los pases 58, 67, 79, 80, 81, 84 y 86.
Publicar un `N/N` sin haber corrido nada sería inventar la cifra, que es exactamente lo que la regla
de `P107` prohíbe.

🔵 **Lo que sí se puede afirmar, y es lo que esta carpeta publica:** los datos de los cuatro `.tsv`
salieron de bucles `curl` corridos **a mano en este pase**, no de un archivo del árbol.
`sweep_matrix.sh` **registra** ese bucle para que un pase futuro lo reproduzca desde el archivo;
**no se ejecutó desde el archivo acá**, y por eso no lleva columna «Hoy» en el README de la raíz.

## Canal, y su calibración (`P249`)

| control | código | lectura |
|---|---|---|
| `raw/moodle/moodle/HEAD/README.md` | 🟢 **200** | el canal responde |
| `raw/moodle/moodle/HEAD/NO-SUCH-FILE-zzz9.md` | 🟢 **404** | **DISCRIMINA → `CALIBRATED`** |
| `curl -sI github.com/openedx/edx-platform` | 🔴 **403** | — |
| `curl -sI github.com/nonexistent-org-zzz/nonexistent-repo-xyz9` | 🔴 **403** | **403 a la buena Y a la inexistente → NO DISCRIMINA** |
| `api.github.com/repos/openedx/edx-platform` | 🔴 **403** | — |
| `api.github.com/repos/nonexistent-org-zzz/…` | 🔴 **403** | **NO DISCRIMINA** |

🔴 **El `curl -sI` que el encargo ordena es, medido, el canal que no puede opinar** — tercer pase
consecutivo que lo reconfirma (85, 86, 90). Todo lo de abajo se leyó por `raw.githubusercontent.com`.

## 1. La matriz: proveedores en el núcleo de Moodle, por ref

Ruta leída: `<prefix>/provider/<name>/version.php`, con `prefix` = `ai` (layout root) o `public/ai`
(layout `public/`). Datos crudos: [`matrix.2026-10-04.tsv`](matrix.2026-10-04.tsv).

| ref | layout | `$release` | anthropic | awsbedrock | azureai | deepseek | gemini | ollama | openai | **total** |
|---|---|---|---|---|---|---|---|---|---|---|
| `MOODLE_405_STABLE` | root | 4.5.15 | 404 | 404 | **200** | 404 | 404 | 404 | **200** | **2** |
| `MOODLE_500_STABLE` | root | 5.0.11 | 404 | 404 | **200** | 404 | 404 | **200** | **200** | **3** |
| `MOODLE_501_STABLE` | `public/` | 5.1.8 | 404 | 404 | **200** | **200** | 404 | **200** | **200** | **4** |
| `MOODLE_502_STABLE` | `public/` | 5.2.4 | 404 | **200** | **200** | **200** | **200** | **200** | **200** | **6** |
| `MOODLE_503_STABLE` | `public/` | **5.3** | **200** | **200** | **200** | **200** | **200** | **200** | **200** | **7** |
| `main` | `public/` | **6.0dev** | **200** | **200** | **200** | **200** | **200** | **200** | **200** | **7** |

**El dato que esta base no tenía: la versión de ENTRADA de cada proveedor.**

| entra en | proveedor |
|---|---|
| ≤ 4.5 | `openai`, `azureai` |
| **5.0** | `ollama` |
| **5.1** | `deepseek` |
| **5.2** | `awsbedrock`, `gemini` |
| **5.3** | `anthropic` |

🟢 **Reproduce la cifra del pase 19 sin copiarla:** aquel pase auditó el árbol de `main` y contó
**siete** proveedores; este barrido, por otro canal y otra ruta, da **7** en `main` y en
`MOODLE_503_STABLE`. Dos lecturas independientes, misma cifra.

🔵 **Y la regla comercial que sale de la tabla, que es lo que viaja a una propuesta:** la pregunta
«¿puedo usar Anthropic / Gemini / Bedrock / DeepSeek en Moodle sin plugin de terceros?» **no se
contesta con «sí, Moodle tiene subsistema de AI»: se contesta con una versión mínima.** Anthropic
exige **5.3**; Gemini y Bedrock, **5.2**; DeepSeek, **5.1**. Un cliente en 4.5 LTS tiene **dos**.

### Controles de la matriz

Datos: [`controls.2026-10-04.tsv`](controls.2026-10-04.tsv).

| control | código | por qué importa |
|---|---|---|
| `MOODLE_503_STABLE/ai/provider/openai/version.php` (prefijo root sobre ref `public/`) | 🔴 404 | el layout es **medido**, no supuesto |
| `MOODLE_500_STABLE/public/ai/provider/openai/version.php` (prefijo `public/` sobre ref root) | 🔴 404 | ídem, en el sentido contrario |
| `main/public/ai/provider/nosuchprov9/version.php` | 🔴 404 | un nombre inventado da 404 → **una celda 200 significa algo** |

## 2. La capa de plataforma en el eje de proveedor

Datos: [`platform-layer.2026-10-04.tsv`](platform-layer.2026-10-04.tsv).

| plataforma | manifiesto leído | tokens | veredicto |
|---|---|---|---|
| `moodle/moodle` | subplugins `aiprovider` del núcleo | **7 proveedores** | 🟢 **`ABSTRACCION-EN-NUCLEO`** |
| `openedx/edx-platform` | `requirements/edx/base.txt` | `boto3` | `SIN-PROVEEDOR-DE-MODELO` |
| `instructure/canvas-lms` | `Gemfile` | — | `SIN-PROVEEDOR-DE-MODELO` |
| `chamilo/chamilo-lms` | `composer.json` | — | `SIN-PROVEEDOR-DE-MODELO` |
| `ILIAS-eLearning/ILIAS` | `composer.json` | — | `SIN-PROVEEDOR-DE-MODELO` |
| `frappe/education` | `pyproject.toml` | — | `SIN-PROVEEDOR-DE-MODELO` |
| `frappe/erpnext` | `pyproject.toml` | — | `SIN-PROVEEDOR-DE-MODELO` |
| `openeducat/openeducat_erp` | `requirements.txt` → **404** | — | ⚠️ **`NO-CLAIM`** (el manifiesto no está en esa ruta; **no se afirma ausencia**) |

⚠️ **El falso positivo queda versionado, porque es de una clase que se repite:** el barrido marcó
`boto3` en `edx-platform`. **`boto3` es el SDK de AWS, no un proveedor de modelo.** Un token de
proveedor y un SDK de nube se parecen en la cadena y no en lo que ligan.

## 3. La licencia de la capa de plataforma, leída del payload

Datos: [`licenses.2026-10-04.tsv`](licenses.2026-10-04.tsv). **8 de 8 leídas de primera mano**, no
de política de proyecto ni de la página del repo.

| plataforma | familia |
|---|---|
| `moodle/moodle` | **GPL-3.0-or-later** |
| `openedx/edx-platform` | **AGPL-3.0** |
| `instructure/canvas-lms` | **AGPL-3.0** |
| `chamilo/chamilo-lms` | **GPL-3.0** |
| `ILIAS-eLearning/ILIAS` | **GPL-3.0** |
| `frappe/erpnext` | **GPL-3.0** |
| `frappe/education` | **GPL-3.0** |
| `openeducat/openeducat_erp` | 🔵 **LGPL-3.0** |

🔴 **8 de 8 son COPYLEFT. CERO permisivas.** El encargo pide foco en MIT / Apache 2.0 / BSD, y eso
se cumple en la capa de AGENTE; **en la capa de PLATAFORMA no hay ninguna opción permisiva que
elegir**, así que la restricción no es de selección sino de entrega.

🔵 **La única distinción que cambia una cotización es LGPL vs GPL/AGPL**, y la tiene una sola fila:
`openeducat_erp`. Y **AGPL** en las dos plataformas más grandes (`edx-platform`, `canvas-lms`)
alcanza el uso **en red**, que es exactamente la forma en que se entrega un LMS.

## Reglas que este instrumento deja escritas

- **`P269`** — Un conjunto de proveedores (o de subplugins, o de capacidades) es propiedad del par
  **(repo, ref)**. Citarlo sin la ref tiene el defecto que `P268` encontró en los conteos de
  capacidades: **le falta la superficie**. `HEAD` no es una ref útil para Moodle.
- **`P270`** — Un negativo sobre una ruta que codifica un **NOMBRE** no se publica como ausencia a
  menos que la lista de nombres venga de una fuente **enumerable**. Contraejemplo permanente:
  `ai/provider/bedrock` → 404, `ai/provider/awsbedrock` → **200**.
- **`P271`** — Una afirmación sobre la **capa A** no puede citar una medición cuyo denominador es la
  **capa B**. Es la versión por capa de `P228`. Contraejemplo permanente: el pase 86 escribió *«las
  plataformas no ligan proveedor de modelo»* citando `P257`, **cuyo denominador son 69 filas de
  agente y cero plataformas**.
