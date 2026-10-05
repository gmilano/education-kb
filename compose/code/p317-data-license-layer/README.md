---
industry: education
region: Global
updated: 2026-10-05
---

# `p317-data-license-layer` — la pregunta de datos son DOS preguntas, y la prediccion colapsó las dos

> Nuevo en el **pase 102 del 2026-10-04**. Corre la acción pre-registrada del pase 101 y la
> **falsifica**, y el instrumento que la falsifica encuentra un caso **peor** que el que la
> predicción buscaba.

## Qué se pre-registró, y qué salió

El pase 101 dejó escrito:

> *«`P315` no es un espécimen aislado: la licencia por CAPA es la norma en la capa de observación de
> aula, porque toda pieza útil ahí necesita un corpus de aula y los corpus de aula se publican no
> comerciales»*. **Predicción: un barrido de los `data/`, `datasets/`, `corpus/` y `README` de datos
> de las 6 altas del pase 101 y de las 3 piezas de habla del pase 14 encontrará al menos DOS piezas
> más con licencia de datos distinta de la del código, y la mayoría de las que declaren datos serán
> `NC`.** Denominador: **9 repos**.

Medido sobre los 9, con el árbol **enumerado** y la licencia leída del **payload**:

| | pre-registrado | medido | veredicto |
|---|---|---|---|
| piezas con licencia de datos **distinta** de la del código, además de `classroom_discourse_intelligence` | **≥ 2** | 🔴 **0** | **FALSIFICADA** |
| de las que **declaran** datos, mayoría `NC` | mayoría | 🔴 **1 de 2** (la otra concede uso comercial **explícito**) | **FALSIFICADA** |

🟢 **`P315` era específico de `classroom_discourse_intelligence`.** La sección del pase 101 que lo
generalizó estaba equivocada, y queda corregida acá en vez de quedar en pie.

## Lo que el barrido encontró en cambio, y es peor

🔴 **La pregunta estaba mal planteada.** Comparar *«licencia de datos declarada»* contra *«licencia
de código»* sólo alcanza a los repos que **declaran** algo. El caso peor para un entregable **no
declara nada**: es el repo que **redistribuye un corpus ajeno sin ponerle cesión**, de modo que el
único archivo de licencia del árbol —el del **código**— queda cubriendo material que **no es del
titular que lo firma**.

Son **dos ejes ortogonales**, y la predicción los colapsó en uno:

| | **B: declara términos de datos** | **B: no declara** |
|---|---|---|
| **A: redistribuye corpus** | `CORPUS-CON-TERMINOS` | 🔴 **`CORPUS-SIN-CESION`** ← el caso peor |
| **A: no redistribuye** | `DATOS-DECLARADOS-DISTINTOS` ← acá vive `P315` | `SIN-CORPUS` |

**`P317`**: *la pregunta de datos de un repo son dos preguntas ortogonales —¿redistribuye corpus? y
¿cede algo sobre él?— y un barrido que sólo compara licencias **declaradas** da PERMITIDO sobre la
celda peor, porque esa celda es silenciosa.*

## El hallazgo: `edu-convokit` redistribuye bajo MIT el corpus que el otro repo declara `NC`

Datos crudos: [`result.2026-10-04.tsv`](result.2026-10-04.tsv).

**Los dos repos de la misma cohorte toman posiciones opuestas sobre el MISMO corpus:**

| | qué hace con TalkMoves | medido en |
|---|---|---|
| `devissaputra/classroom_discourse_intelligence` | declara `CC BY-NC-SA 4.0` y dice *«This repository does **not** redistribute the source corpus»* — y su `data/` tiene **0** archivos de payload: cumple lo que dice | `data/README.md` + árbol enumerado |
| 🔴 `rosewang2008/edu-convokit` | **redistribuye 29 transcripciones** (`data/talkmoves/*.xlsx`) **+ `data/talkmoves.zip`**, bajo un repo cuya **única** cesión es `MIT © 2023 Rose E. Wang`, y **sin una sola línea** sobre términos de datos | árbol enumerado + `LICENSE` + `README.md` |

🟢 **La identidad del corpus no se infiere, se mide.** El upstream `SumnerLab/TalkMoves` declara
`CC BY-NC-SA 4.0` por **dos** canales que concuerdan (`LICENSE`, **20.849 B**, texto íntegro de la
CC BY-NC-SA 4.0; y el `README`, que la nombra). Y los nombres de archivo de `data/talkmoves/` de
`edu-convokit` coinciden **exactamente** con `data/Subset 1/` del upstream, incluida la huella
`Boats and Fish 4_Grade 4 .xlsx` — **con el espacio antes de la extensión**, que es una huella casi
única y está aserida en la suite.

🔵 **Y `edu-convokit` vendorea tres corpus, no uno:** `amber` (45), `ncte` (29), `talkmoves` (29),
más los tres `.zip` y `annotated_data.csv` → **111 archivos** bajo `data/`.

🔴 **Por qué cuesta el entregable.** La fila de `edu-convokit` en `agents/top.md` dice **MIT** y
**es correcta para el código**. Un equipo que la lee, instala el paquete y usa los datos que vienen
adentro **embarca material `NonCommercial ShareAlike` en una entrega comercial**. La fila no está
mal: **lo que faltaba era el eje que distingue el código del corpus.**

**`P318`**: *dos repos de la misma capa pueden contradecirse sobre el mismo corpus, y el que lo
maneja MAL es el que tiene más estrellas y está en la tabla. La cesión de un repo no alcanza a los
datos que ese repo no creó.*

## `P319` — la ausencia de `data/README.md` NO es ausencia de datos

🔴 `rosewang2008/edu-convokit` da **404 en `data/README.md`** y redistribuye **111 archivos** de
corpus. **El barrido de paths adivinados que este pase corrió primero lo publicó como «sin datos»**
— un falso negativo que esconde exactamente la celda peor de la matriz.

🟢 **El arreglo es de canal, no de umbral:** el árbol se **enumera** con un clon
`--filter=blob:none --no-checkout --depth 1` (el canal de **`P275`**), que es el único que sostiene
una **ausencia** mientras `github.com` y `api.github.com` siguen en **403**. El fracaso del
instrumento viejo está **aserido**, no narrado: ver `C3` en la suite.

## Invocación

```sh
python3 test_corpus_axis.py          # OFFLINE, sobre los arboles congelados en fixtures/
WORK=/tmp/t317 sh sweep_corpus.sh    # con red: enumera, lee payload, emite el TSV
```

**Hoy: 37/37.** Los controles, y por qué cada uno existe:

| Control | Qué afirma | Por qué |
|---|---|---|
| **C3** | `pathguess` **NO** ve el corpus de `edu-convokit` y enumerar **sí** | es `P319` como aserto. Sin él, el defecto es prosa |
| **C2** | `classroom_discourse_intelligence` vuelve `DATOS-DECLARADOS-DISTINTOS` | un instrumento que no reproduce el positivo conocido de `P315` no sostiene los 8 negativos |
| **C5** | *«for both commercial and non-commercial purposes»* **no** se lee como `NC` | es el defecto de **`P308`** sobre el Unlicense, que este módulo podía reintroducir: invertir el veredicto sobre el texto **más** permisivo |
| **C4** | el `.wav` de `src/feat/test_data/` de kaldi **no** es corpus | un eje que cuente payload en cualquier parte del árbol llama corpus a todo fixture y no discrimina nada |
| **C6** | un `data/README.md` **no** es payload | una tarjeta de dataset es eje **B**, no eje **A**. Si contara, `CDI` saldría «redistribuye» y contradiría su propio README |
| **C7** | un badge de `shields.io` **no** concede nada | `P314`: el canal secundario del pase 101 leyó una licencia de un badge, y un badge es una imagen |
| **C8** | el censo **sin compuerta de ubicación** da **115**, y la compuerta descuenta los **4** prompts `.txt` | el primer censo de este pase contó código como dato. Un conteo de datos que no gatea por **ubicación** infla |
| **C1** | un slug inventado hace **fallar** el clon | si el canal no discrimina, ningún negativo suyo vale |

## Límites declarados

- 🔴 **`amber` y `ncte` quedan sin procedencia resuelta.** Son 74 de los 111 archivos de
  `edu-convokit`. El hallazgo publicado se sostiene sobre `talkmoves`, que **sí** está medido de
  punta a punta. Para los otros dos, lo que falta es el upstream con su cesión, y este pase **no**
  lo resolvió: se dice en vez de callarse.
- 🔴 **El umbral `CORPUS_MIN_FILES = 20` es una decisión, no una medición.** Se publica con el
  conteo de cada repo al lado (`archivos_corpus`) para que el lector re-derive el veredicto. Ningún
  repo de la cohorte cae cerca del borde: los dos positivos dan **111** y **5.245**, y los siete
  negativos dan **0**.
- 🔴 **`speechocean762` concede por README y no por archivo.** El árbol **enumerado** no tiene
  archivo de licencia en ninguna parte (aserido), y el `README` declara disponibilidad *«for both
  commercial and non-commercial purposes»*. Es cesión válida y débil: **corrige** el límite que los
  pases 14 y 100 dejaron como *«no verificable»* —el texto **sí** se lee de primera mano— y **no**
  la eleva a familia OSI, porque no hay archivo que la nombre.
