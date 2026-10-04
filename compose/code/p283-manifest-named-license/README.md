---
industry: education
region: Global
updated: 2026-10-04
---

# `p283-manifest-named-license` — la acción PRE-REGISTRADA del pase 94, corrida, y su predicción FALSIFICADA

> Nuevo en el **pase 95 del 2026-10-04**. El pase 94 dejó escrita una acción *«para que no se
> pueda eludir»*: re-correr el barrido de licencia sobre las **200 filas `org/repo`** que los
> pases 62/64 midieron con el instrumento viejo, y predijo que **~28 filas** tendrían por
> veredicto un hueco de nombre. **Se corrió sobre las 200. La predicción es FALSA: fueron 0.**

| Qué prueba | Invocación | Hoy |
|---|---|---|
| la parte pura (lectura de manifiesto + propiedad), sobre payloads REALES | `python3 test_manifest_license.py` | 🟢 **34/34** |
| el barrido en vivo, 200 filas | `sh sweep_named.sh slugs.input.txt` | 🟢 **200/200 filas** → `result.2026-10-04.tsv` |
| los dos controles del pase 94, en vivo | `sh sweep_named.sh --repos openedx/XBlock alfredang/ai-mms` | 🟢 reproducidos |

## 🔬 El canal, declarado antes de cualquier veredicto (`P247`)

Medido hoy de nuevo: **`github.com/` → `403`** y **`api.github.com` → `403`**; `raw.githubusercontent.com`
discrimina `200`/`404` **y entrega el payload**, así que la licencia se LEE. Todo lo de abajo sale de ahí.

## 🔴 El resultado: la predicción del pase 94 no se sostiene

El pase 94 razonó que si `P279` (el hueco de CAJA en el nombre del archivo) se repartía como en su
control positivo —1 de 7— entonces **~28 de 200** filas tendrían un `SIN LICENCIA` que es un hueco
del instrumento y no un dato. Medido:

| Lo medido sobre las 200 | n |
|---|---|
| filas re-medidas | **200** |
| 🔴 **huecos de NOMBRE de archivo (`P279`) hallados** | 🔴 **0** |
| payload hallado por el nombre que NOMBRA el manifiesto | **12** — *y las 12 resolvieron a `LICENSE`*, que la lista fija ya tenía |
| veredicto que cambia de CLASE | **5** (`SIN_LICENCIA` → `SOLO_MANIFIESTO`) |
| familia de licencia más PRECISA | **17** |
| filas donde la **tabla publicada** ya era correcta | 🟢 **200 de 200** |

🔵 **Por qué la predicción falló, y es informativo:** `P279` es **real pero RARO**. El único caso
medido en esta base sigue siendo `openedx/XBlock` (`master/LICENSE.TXT`), y **XBlock no está en
estas 200 filas** — vive en `repos/foundations.md`. La tasa no es 1 de 7: es **1 de 201** sobre todo
lo que esta base ha barrido. 🔴 **Extrapolar un reparto desde UN control positivo fue el error**, y
queda escrito: `P286`.

## 🟢 Lo que sí rinde: la corrección a mano del pase 65 se vuelve CONTROL

Las **5** filas que cambian de clase son **exactamente** las que el pase 65 corrigió **a mano**, una
por una, leyendo manifiestos:

| Fila | Manifiesto | `name` declarado | Propiedad | Licencia |
|---|---|---|---|---|
| `HKUDS/AI-Researcher` | `setup.cfg` | `ai-researcher` | 🟢 `OWN` | MIT |
| `Timadey/proctor` | `package.json` | `@timadey/proctor` | 🟢 `OWN` | MIT |
| `ink-waffle/moodle-mcp` | `package.json` | `@ink-waffle/moodle-mcp` | 🟢 `OWN` | MIT |
| `tejpalvirk/student` | `package.json` | `contextmanager-student` | 🟢 `OWN` | MIT |
| `DMontgomery40/mcp-canvas-lms` | `package.json` | `canvas-mcp-server` | ⚠️ `WEAK` | MIT |

🟢 **Eso es el aporte durable: lo que era memoria de un pase pasa a ser un instrumento que lo
deriva solo.** La clase `SOLO_MANIFIESTO` nombra lo que esas 5 filas son y el barrido viejo no podía
decir: **no hay archivo de licencia, pero el manifiesto del PROPIO proyecto declara una expresión.**
Para Globant no es lo mismo que «sin licencia»: es una cesión **defectuosa pero intencional**
(`P179` ya separaba *identificador* de *cesión*; esta clase lo hace medible).

⚠️ **Y `DMontgomery40/mcp-canvas-lms` sale `WEAK`, no `OWN`**: su `package.json` se llama
`canvas-mcp-server` y el repo `mcp-canvas-lms`. Se atribuye **con reserva**, y la reserva está en
la columna, no en la prosa.

## 🟢 Los 17 que ganan PRECISIÓN, por reusar el classificador compartido (`P237`)

El instrumento no trae classificador propio: **sourcea `lib/license_family.sh`**, que classifica por
**bloque de título** (`P171`). Eso convierte 12 `GPL` genéricos en su versión y classifica 4 `UNKNOWN`:

| Fila | Viejo | Medido hoy | Payload |
|---|---|---|---|
| `oat-sa/tao-core` | `GPL` | 🔴 **`GPL-2.0`** | `LICENSE` |
| `moodle/moodle` | `GPL` | **`GPL-3.0`** | `COPYING.txt` |
| `kaldi-asr/kaldi` | `UNKNOWN` | **`Apache-2.0`** | `COPYING` |
| `trilogy-group/oneroster-ts` | `UNKNOWN` | 🟢 **`0BSD`** | `LICENSE` |
| `nmarafo/OpenDidactia` | `UNKNOWN` | ⚠️ **`CC-BY-SA-4.0`** | `LICENSE.md` |
| `dssg/student-early-warning` | `UNKNOWN` | **`UNCLASSIFIED`** | `LICENSE` |
| + 11 filas `GPL` → `GPL-3.0` | | | |

🔴 **`oat-sa/tao-core` es la consecuente: `GPL-2.0`, no `GPL-3.0`.** Son incompatibles en un sentido,
y TAO es la plataforma de evaluación QTI más madura del inventario. La tabla publicada **ya lo dice
bien** (pase 9) — el que estaba grueso era el archivo de resultado.

🟢 **`dssg/student-early-warning` → `UNCLASSIFIED` es el classificador portándose BIEN:** su `LICENSE`
es una licencia académica **no comercial** de la Universidad de Chicago. Negarse a ponerle familia OSI
es el comportamiento correcto; la tabla ya la marca como **no open source**.

## ⚠️ Límite declarado de este barrido

`kaldi-asr/kaldi` sale `Apache-2.0` y **el veredicto es correcto** (el `COPYING` concede Apache 2.0
en su línea 51 y repite el *grant* estándar en la 145), 🔴 **pero la evidencia que lo disparó es
PROSA del bloque de título, no una línea de título canónica** — el `COPYING` de Kaldi es un *legal
notice* de 364 líneas, no el texto de la licencia. Es un acierto por una vía débil, y queda escrito:
el mismo patrón sobre un repo que sólo *mencione* «Apache» daría un falso positivo. La tabla ya
marcaba esta fila como **texto anómalo** (pase 36).

## 📄 Formato de `result.2026-10-04.tsv`

```
slug  ref  testigo  veredicto  payload  familia  manifiesto  manifest_name  propiedad  nombrado  sondas
```

- `veredicto` ∈ `CON_LICENCIA` · `SOLO_MANIFIESTO` · `SIN_LICENCIA` · `INDETERMINADO`
- `INDETERMINADO` **no es ausencia**: es que el testigo de alcance no dio `200` en ninguna ref, así
  que no se puede afirmar nada. Son **8**, e incluyen los 2 slugs de plantilla (`owner/repo`,
  `your-username/SafeTutors`) que el pase 72 ya había diagnosticado como artefactos de prosa.
- `propiedad` ∈ `OWN` · `WEAK` · `FOREIGN` · `NONAME` — es el control de **`P280`**: con `FOREIGN`
  la licencia del manifiesto **no se publica** (es el caso `alfredang/ai-mms` → `openmage/magento-lts`).

## 🔴 Acción pre-registrada para el pase 96

Correr este mismo instrumento sobre las filas `org/repo` de `repos/foundations.md` y
`verticals/solutions.md` que **no** están en estas 200 — es donde vive `openedx/XBlock`, el único
`P279` conocido, así que es el único sitio donde la tasa de 1 de 201 puede subir.
