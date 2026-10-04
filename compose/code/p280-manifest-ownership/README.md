---
industry: education
region: Global
updated: 2026-10-04
---

# `p280-manifest-ownership` — un manifiesto en la raíz de un repo no necesariamente DESCRIBE a ese repo

> Nuevo en el **pase 94 del 2026-10-04**. Pone a prueba la columna más consecuente de esta
> base —la de licencia— con un instrumento más duro que el que la produjo, y el resultado
> tiene las dos mitades: **los 8 veredictos `SIN LICENCIA` se sostienen (8/8)**, y
> **el instrumento que los produjo tenía dos huecos**, uno de los cuales casi hace publicar
> una licencia FALSA en este mismo pase.

| Qué prueba | Invocación | Hoy |
|---|---|---|
| la lógica de los dos controles, sobre payloads capturados | `python3 test_license_probe.py` | **37/37** |
| el barrido en vivo, por repo | `sh sweep.sh openedx/XBlock alfredang/ai-mms` | — (red) |

## 🔬 El canal, declarado antes de cualquier veredicto (`P247`)

El encargo de esta base ordena verificar cada URL con `curl -sI`. **Medido hoy: contra
`github.com/` devuelve `403` en 3 de 3**, y los repos están vivos. Reproduce exacto lo que
el pase 81 midió en 81 de 81 URLs: **ese canal no sirve aquí, y seguir citándolo como
verificación es citar un 403.**

🟢 **El canal que rinde es `raw.githubusercontent.com`**, que discrimina `200` de `404` y
—a diferencia de la página del repo— **entrega el payload**, así que la licencia se LEE en
vez de inferirse. Todo lo de abajo está medido por ahí.

## 🔴 Hueco 1 (`P279`): el canal es sensible a MAYÚSCULAS, también en la extensión

`openedx/XBlock` está publicado en `repos/foundations.md` como **Apache-2.0**, y la fila es
**correcta**. Pero el barrido no la pudo confirmar:

| Sonda | Resultado |
|---|---|
| 11 variantes de nombre × 3 ramas = **33 sondas** | 🔴 **0 hits** |
| testigo de alcance (`README.rst`, rama `master`) | 🟢 `200` — el repo SÍ se alcanzaba |
| `master/LICENSE.TXT` | 🟢 `200`, y abre con `Apache License` |

**La diferencia entre la variante probada y la real es la CAJA de la extensión:**
se probó `LICENSE.txt`, el archivo es `LICENSE.TXT`.

🔵 **Y el nombre no hay que adivinarlo: el manifiesto lo NOMBRA.**
`master/pyproject.toml` de XBlock dice, en dos líneas contiguas:

```toml
license = "Apache-2.0"
license-files = ["LICENSE.TXT"]
```

**P279**: *una lista fija de nombres de archivo de licencia siempre tiene un hueco, porque
el espacio de nombres es libre y el canal distingue mayúsculas. El nombre autoritativo está
en el manifiesto del paquete (`license-files`), no en la lista de variantes del barrido: hay
que LEERLO de ahí y sondear ESE nombre.* Caso de `P278` en su eje de nombre: la ruta del
payload es propiedad de la **(repo, ref)** —aquí la ref es `master`, no `main`.

⚠️ **Lo que esto implica para esta base:** un `🔴 SIN LICENCIA` cuya única evidencia sea
`/blob/main/LICENSE → 404` **no es un veredicto, es un hueco del instrumento**. Por eso las
8 filas se re-midieron con el barrido ancho Y con el testigo de alcance.

## 🔴 Hueco 2 (`P280`): el manifiesto hallado puede describir a OTRO proyecto

Sondeados 6 manifiestos sobre las 8 filas marcadas `SIN LICENCIA`, **exactamente 1** devolvió
una licencia: `alfredang/ai-mms` → `main/composer.json` → **`["OSL-3.0", "AFL-3.0"]`**.

🔴 **Tomar esa cifra habría publicado una licencia falsa en un LMS de Singapur.** El campo de
al lado la refuta:

```json
"name": "openmage/magento-lts",
"license": ["OSL-3.0", "AFL-3.0"],
"type": "magento-source",
"description": "A fork of Magento-1 that is accepting bug fixes ..."
```

Es el `composer.json` de **OpenMage**, sin modificar, en la raíz de otro repo.

**P280**: *una licencia leída de un manifiesto sólo es la licencia de la fila si el
manifiesto se NOMBRA como ese proyecto. El discriminador es el campo `name`; sin esa
comprobación, el probe atribuye al repo anfitrión la cesión de un upstream vendorizado.*
Es la misma familia de error que `P276` (pase 93): **dos señales que no pueden discrepar no
se validan entre sí** — aquí, un campo `license` y el repo que lo aloja no se validan,
porque el archivo nunca habló del repo.

🔵 **El control compara por PROYECTO, no por owner**, para no romper el caso legítimo: un
fork que renombra el owner sigue siendo el mismo paquete (`fork-owner/XBlock` vs
`openedx/XBlock` → propio).

## 🔴 Y la consecuencia comercial va al revés de lo que el hallazgo sugiere: el riesgo SUBE

Medido el árbol de `alfredang/ai-mms`:

| Sonda | Resultado |
|---|---|
| `main/app/Mage.php` | 🟢 `200` — árbol de Magento-1 |
| `main/index.php`, `main/composer.lock` | 🟢 `200` |
| `README.md`, auto-descripción | **«Tertiary Courses LMS (ai-mms)»** sobre **OpenMage LTS v20.12.0** |
| upstream `openmage/magento-lts` → `main/LICENSE.txt` | 🟢 `200` (**OSL-3.0**) |
| ídem → `main/LICENSE_AFL.txt` | 🟢 `200` (**AFL-3.0**) |

🔴 **Así que `SIN LICENCIA` no sobra-castiga esta fila: la SUBESTIMA.** La pieza no tiene
cesión propia **y** su código heredado viene bajo **OSL-3.0**, copyleft fuerte con disparo
por **despliegue externo** —exactamente la forma de cesión más hostil para un encargo de
cliente, porque el gatillo lo aprieta poner el sistema frente a usuarios, que es lo único
que un LMS hace.

🔵 **Para el estudio:** `ai-mms` deja de ser «la candidata más dolorosa, a revisar si
aparece una licencia». Para que fuera usable habría que relicenciar el **upstream**, no el
repo — y eso no está al alcance de su autor. **Es un descarte definitivo, no diferido.**

## 🟢 El resultado sobre esta base: los 8 veredictos se sostienen, 8/8

`relicense.2026-10-04.tsv`. Por fila: **33 sondas de payload + 6 manifiestos + 1 testigo**.
El testigo va **antes** del veredicto, porque sin alcance la «ausencia» mide el canal y no
el repo:

| Fila | Región | Testigo | Veredicto |
|---|---|---|---|
| `Vashishtha05/An-Adaptive-LLM-Based-AI-Tutor-for-Multi-Level-Learning` | 🔴 sin región declarable | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `alfredang/ai-mms` | **APAC** — Singapur | `main/README.md` | **AUSENCIA CONFIRMADA** + `P280` + derivado OSL-3.0 |
| `alfredang/ai4kids` | **APAC** — Singapur | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `attoyibi/lms-with-ai` | 🔴 sin región declarable | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `bigdata-ustc/EduX` | **APAC** — China (USTC) | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `dddanielliu/NCCU-Moodle-MCP` | **APAC** — Taiwán (NCCU) | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `loyaniu/moodle-mcp` | 🔴 sin región declarable | `main/README.md` | **AUSENCIA CONFIRMADA** |
| `vilcaaguilerandrea-oss/carrera-lectora` | **LATAM** | `main/README.md` | **AUSENCIA CONFIRMADA** |

🟢 **8/8 alcanzadas, 8/8 ausencia confirmada.** La columna de licencia de esta base aguanta
un instrumento ~33× más ancho que el que la produjo. **Lo que no aguanta es la
PROCEDENCIA de una de las ocho**, y queda corregida arriba.

🟢 **Control positivo, que es lo que destapó `P279`:** 7 repos de licencia conocida sondeados
con la lista fija → **6 hallados en la primera pasada, 1 (`XBlock`) sólo por manifiesto**.
Un control positivo que hubiera dado 7/7 habría dejado el hueco invisible.

## Pre-registro para el próximo pase

1. Re-correr `sweep.sh` sobre las **~200 filas `org/repo`** que los pases 62/64 barrieron con
   el instrumento viejo: **si `P279` se reparte como en el control (1 de 7), hay ~28 filas de
   esta base cuyo veredicto de licencia es un hueco de nombre, no un dato.** Es la acción de
   mayor valor pendiente y se declara aquí para que el próximo pase no la pueda eludir.
2. Extender el detector de derivación más allá de `app/Mage.php`: marcadores de Moodle
   (`version.php` + `lib/moodlelib.php`), Open edX (`manage.py` + `cms/envs/`) y WordPress
   (`wp-load.php`), para saber **cuántas filas de esta base heredan un árbol copyleft** sin
   decirlo.
3. `P280` en el eje de `package.json`: medir cuántas filas npm de esta base alojan un
   manifiesto cuyo `name` no coincide con el repo.
