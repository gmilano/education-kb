---
industry: education
region: Global
updated: 2026-10-04
---

# `p272-platform-ref-verdict` — un veredicto de plataforma sin REF no es un veredicto

> Nuevo en el **pase 91 del 2026-10-04**.

## Lo que mide, y por qué

El pase 90 demostró (**P269**) que un conjunto de proveedores es propiedad del par **(repo, ref)**:
en el núcleo de Moodle los proveedores van de **2** (4.5.15) a **7** (5.3), así que «la plataforma
soporta X» es verdadero o falso **según la versión**.

🔴 **Y en el mismo pase, en el mismo instrumento, publicó siete veredictos de plataforma SIN REF**
([`platform-layer.2026-10-04.tsv`](../p269-provider-release-matrix/platform-layer.2026-10-04.tsv)):
`openedx/edx-platform → SIN-PROVEEDOR-DE-MODELO`, `canvas-lms → SIN-PROVEEDOR-DE-MODELO`, etc. Cada
fila leyó **un** manifiesto en **una** ref implícita (la rama por defecto). Es el defecto exacto que
P269 acababa de nombrar, una capa más abajo, y no quedó marcado.

**P272** le pone ref a esas filas. No es una regla nueva de la nada: es **P269 aplicado al
denominador de su propia tabla vecina**.

## Resultado: 1 de 2 plataformas CONTRADICE su veredicto sin ref

Datos crudos: [`platform-by-ref.2026-10-04.tsv`](platform-by-ref.2026-10-04.tsv).

| plataforma | ref | token de proveedor | veredicto por ref | vs. pase 90 |
|---|---|---|---|---|
| `openedx/edx-platform` | `open-release/quince.master` | **`openai==0.28.1`** (l. 767, `via kernel.in`) | **TIENE-PROVEEDOR** | 🔴 **CONTRADICHO** |
| `openedx/edx-platform` | `open-release/redwood.master` | **`openai==0.28.1`** (l. 767, `via kernel.in`) | **TIENE-PROVEEDOR** | 🔴 **CONTRADICHO** |
| `openedx/edx-platform` | `open-release/sumac.master` | **`openai==0.28.1`** (l. 809, `via kernel.in`) | **TIENE-PROVEEDOR** | 🔴 **CONTRADICHO** |
| `openedx/edx-platform` | `master` | — | SIN-PROVEEDOR | 🟢 coincide |
| `instructure/canvas-lms` | `master` | — | SIN-PROVEEDOR | 🟢 coincide |
| `instructure/canvas-lms` | `prod` | — | SIN-PROVEEDOR | 🟢 coincide |

🔴 **El veredicto del pase 90 para Open edX es verdadero exactamente en la rama que ningún cliente
corre, y falso en las TRES releases nombradas que sí corre.** `openai` no es transitiva: la propia
línea del manifiesto dice `via -r requirements/edx/kernel.in`, o sea **declarada a mano**.

🟢 **Canvas sobrevive**: en las 2 refs que resuelven, el veredicto sin ref se sostiene. Así que el
defecto es **real pero no universal** — **1 de 2** medidas. No se generaliza a las otras cinco filas:
no fueron medidas por ref en este pase.

## El dato de entrega que sale de acá

🔴 **`openai==0.28.1` es la última release **pre-1.0** del SDK de Python de OpenAI.** Las tres
releases nombradas de Open edX la traen clavada, y la API de ese major **no** es la de `openai>=1.0`
(`openai.OpenAI()`). Un engagement que llegue a un Open edX Quince/Redwood/Sumac y asuma el SDK
moderno **se choca con un major antiguo en el core**, no en su propio código.

🔵 **Y `master` ya no la trae**: la dependencia se cayó entre `sumac` y `master`. Así que la
pregunta «¿con qué SDK hablo?» tiene **tres respuestas distintas** según dónde caiga el cliente.

## Canal y su calibración (`P249`)

Controles completos: [`controls.2026-10-04.tsv`](controls.2026-10-04.tsv).

- 🟢 `raw.githubusercontent.com` → **200 a la buena, 404 a la inventada: DISCRIMINA**, en los tres
  repos medidos. Además **DETERMINISTA**: 5 repeticiones × 6 pares `(ref, ruta)` = **30/30** iguales,
  así que ningún 404 de acá es *flake*.
- 🔴 `curl -sI github.com/...` → **403 a la buena Y a la inexistente**. **Cuarto pase consecutivo**
  (85, 86, 90, 91) midiendo que el canal que el encargo ordena **no puede opinar**. `api.github.com`,
  igual: **403**.

## La regla de control que este pase agrega

Un control de ref (`README.md` resuelve 200) prueba que **la ref existe**; **no** prueba que la ruta
medida siga siendo la dirección correcta en esa ref. Son dos preguntas:

| si… | entonces el 404 mide… |
|---|---|
| el control de ref **falla** | la **REF** (o el nombre conjeturado — `P270`) |
| el control de ref **pasa** y la ruta medida 404 | la **RUTA**: ausencia real **o** layout movido |

🔵 **Contraejemplo medido en este mismo pase, y es la razón de la regla:** sobre
`MOODLE_501_STABLE`, `README.md`/`composer.json`/`index.php` dan **200** y `version.php` da **404** —
no porque falte, sino porque en 5.1 el webroot se mudó a `public/`. Un control invariante al layout
**pasa** justo cuando la ruta medida se rompió. Por eso el barrido de P269 compara `root` **y**
`public/` y exige que **exactamente uno** resuelva; `sweep_platform_ref.sh` hereda esa compuerta.

## ⚠️ Lo que este pase NO afirma

🔴 **No hay suite ni total de aserciones, a propósito.** La ejecución de código del árbol está
**NEGADA** en este pase (`[Code from External]`), como en los pases 58, 67, 79, 80, 81, 84, 86, 89
y 90. Publicar un `N/N` sin correr nada sería inventar la cifra (`P107`).

🔵 Los datos de los `.tsv` salieron de bucles `curl` corridos **a mano** en este pase.
[`sweep_platform_ref.sh`](sweep_platform_ref.sh) **registra** ese bucle para reproducirlo;
**no se ejecutó desde el archivo acá**, y por eso esta carpeta **no** lleva columna «Hoy».

⚠️ Las cinco filas restantes del pase 90 (`chamilo`, `ILIAS`, `frappe/education`, `frappe/erpnext`,
`openeducat`) **siguen sin ref**. Quedan como ACCIÓN, no como veredicto.
