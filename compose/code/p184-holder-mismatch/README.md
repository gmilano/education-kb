---
industry: education
region: Global
updated: 2026-10-03
---

# `p184-holder-mismatch` — un archivo de licencia COMPLETO puede decir la licencia EQUIVOCADA (pase 66 del 2026-10-03)

**No ejecuta una acción escrita: la encontró el barrido de altas de este pase**, y entra porque rompe
el supuesto sobre el que descansan **P170**, **P172** y **P179**.

## El caso que lo abre

🔴 **`MaybeItsAdam/tutors`** —una alta candidata de este pase, *«infinite canvas where students and AI
collaborate»*— trae **`LICENSE.md` de 1.075 B con el texto MIT completo, titular y año**:

```
MIT License

Copyright (c) 2024 tldraw Inc.
```

**Y su `README.md` dice otra cosa:** *«This project is built on the tldraw SDK, provided under the
tldraw SDK license. You can use the tldraw SDK in commercial or non-commercial projects **so long as
you preserve the "Made with tldraw" watermark on the canvas**.»*

⚠️ **Una condición de marca de agua NO es MIT.** MIT no obliga a conservar ningún elemento visual.

🔴 **Y lo que lo vuelve un patrón y no una anécdota: TODAS las capas que esta KB mide lo aprueban.**

| Capa | Pregunta | Veredicto sobre `MaybeItsAdam/tutors` |
|---|---|---|
| **P170** (pase 64) | ¿hay archivo de licencia en 14 nombres × ref `HEAD`? | 🟢 **sí**, `LICENSE.md` |
| **P171** (pase 64) | ¿qué familia dice el TÍTULO? | 🟢 **MIT**, leído del título |
| **P168** (pase anterior) | ¿tiene tamaño de texto y no de afirmación? | 🟢 **1.075 B**, texto completo |
| **P179** (pase 65) | ¿identificador o CESIÓN (titular + año + texto)? | 🟢 **cesión**: titular, año y texto |
| **P184** (hoy) | ¿el TITULAR pertenece al proyecto? | 🔴 **no**: `tldraw Inc.`, 2024, sobre un proyecto de 2026 de `MaybeItsAdam` |

🔵 **El titular es la señal más barata de que una licencia fue HEREDADA y no OTORGADA.** Un copyright
de `tldraw Inc.` de 2024 en un proyecto de tutoría de 2026 no pertenece al proyecto, y eso se detecta
sin leer el README.

## D7 — la FAMILIA es una entrada OBLIGATORIA, y eso es el hallazgo de método

La primera construcción corrió sobre los **160** archivos que **P170** ya había medido como presentes
y devolvió **87 `HOLDER-UNRELATED`**. 🔴 **87 sobre 99 no es una lista de lectura: es un instrumento
roto.** Leída la salida, dos causas, las dos del mismo tipo:

| | Familia | Qué publicó como titular | Qué era en realidad |
|---|---|---|---|
| **D6a** | **Apache-2.0** (29 de 30) | `notice that is included in or attached to the work` | una **frase del cuerpo**; el titular de Apache vive en un APÉNDICE que se publica **sin rellenar** |
| **D6b** | **GPL / AGPL** (21) | `Free Software Foundation, Inc. <https://fsf.org/>` | el copyright **DEL TEXTO DE LA LICENCIA**, que toda copia de la GPL lleva |
| **D6c** | **CC** | `Related Rights (defined below) upon the creator` | otra frase del cuerpo |

🔴 **Y parchear el filtro de frases fue el movimiento equivocado: los controles lo demostraron.**
Sobre el texto Apache **real y completo** (11.408 B) una construcción ciega a la familia seguía
publicando `patent, trademark, and`; sobre la GPL real (35.147 B), `permission, other than the making
of an`. **Ninguna lista de palabras cierra la clase, porque esos textos son decenas de kilobytes de
prosa SOBRE el copyright.**

🔵 **Así que el instrumento se NIEGA a contestar sin familia (`FAMILY-REQUIRED`) en vez de adivinar.
Y ésa es la asimetría que vale:** **P170** quitó la dimensión **rama** de la pregunta de licencia y
**P171** llevó la familia al **título** — las dos hicieron la pregunta *menos* dependiente del
contexto, y estuvo bien. **La dimensión del titular no va para ese lado: que un archivo de licencia
nombre al titular del proyecto es una propiedad DE LA FAMILIA.**

| Familia | ¿el texto estándar trae titular rellenado? | Dónde está el titular, entonces |
|---|---|---|
| **MIT · BSD · ISC** | 🟢 **sí, por construcción** | en el archivo |
| Apache-2.0 | 🔴 no (apéndice plantilla) | en `NOTICE`, o en los headers de fuente |
| GPL · AGPL · LGPL | 🔴 no (lleva el de la FSF) | **en los headers de fuente** — el canal de **P172**, el mismo que el pase 65 midió en `version.php` y `lib.php` |
| CC0 · CC-BY · Unlicense | 🔴 no | en la anotación del dato (**P172**) |

## El resultado, con la familia como entrada

| Veredicto | n (de 160) | Qué significa |
|---|---|---|
| `NOT-APPLICABLE` | **61** | Apache-2.0 (30), GPL (12), AGPL-3.0 (9), LGPL (2), CC0-1.0 (2), CC-BY (1), Unlicense (1), UNKNOWN (4): **el titular no está en el archivo por construcción** |
| `HOLDER-MATCH` | **68** | el titular comparte un *token* con el dueño o el nombre del repo |
| `HOLDER-UNRELATED` | **31** | 🔵 **la lista de lectura** — 31 filas se leen a mano; 87 no se leían |

⚠️ **`HOLDER-UNRELATED` NO es un veredicto de incorrección.** El nombre propio de una persona casi
nunca coincide con su *handle* de GitHub, así que la clase es una **lista de lectura**. Lo que la
vuelve útil es que **31 se leen y 87 no**, y que el caso de `tldraw` cae dentro.

### Leída la lista: 17 son el nombre propio del autor. Las que importan son 6

| Fila | Titular | Clase |
|---|---|---|
| **`AmirF194/canvas-mcp`** | `Vishal Sachdev` | 🟢 **linaje** |
| **`BartMassey-upstream/canvas-mcp`** | `Vishal Sachdev` | 🟢 **linaje** |
| **`abr-Projects/canvas-mcp`** | `Vishal Sachdev` | 🟢 **linaje** |
| **`lindsay-cheng/canvas-mcp`** | `Vishal Sachdev` | 🟢 **linaje** |
| **`GEMLab-HKU/Unlearn_and_Relearn`** | `UCSB ML&NLP Group` | 🔴 **titular heredado del *upstream*** — repo de un laboratorio de **HKU** con copyright de un grupo de **UCSB** |
| **`jupyterlab/jupyter-ai`** | `author_a` | 🔴 **marcador de plantilla** — el *default* del *cookiecutter* de extensiones de Jupyter, publicado en un BSD real de un proyecto de JupyterLab |

🟢 **El resultado que más vale: las CUATRO filas con `Vishal Sachdev` son los forks de `canvas-mcp`
que el pase 63 estableció leyendo DERIVA DE `description`, y el titular los recupera solo.** **El
copyright de un archivo MIT es una señal de linaje, y sobrevive a un renombre, a una reescritura de
`description` y a un fork desprendido** — tres cosas que la deriva de descripción no sobrevive. Es
una confirmación de un pase anterior **por un canal sin relación con el que lo produjo**.

⚠️ **Dos titulares preservan el nombre ANTERIOR del proyecto**, que es la misma señal en otra
dirección: `SirhanMacx/Claw-ED` → `EDUagent Contributors`, y `UKGovernmentBEIS/inspect_ai` → `UK AI
Security Institute` (el *handle* lleva el nombre viejo del departamento, el copyright el nuevo del
organismo).

## Reservas declaradas

- ⚠️ **El corpus son los 160 que P170 midió como `LICENSED`.** `MaybeItsAdam/tutors` **no está en
  esos 160**: es un alta de hoy, y se midió a mano. **El barrido se rehace cuando `slugs.input.txt`
  de P170 incorpore las altas de este pase** — está escrito como acción para el pase 67.
- ⚠️ **El titular responde «¿esto fue heredado?», no «¿la licencia es la correcta?»** En
  `MaybeItsAdam/tutors` el titular detecta la herencia y **el README** es lo único que dice los
  términos reales. **El instrumento acorta la lista de lectura; no la elimina.**
- ⚠️ **Un *match* de *token* puede ser casual.** El piso son 4 caracteres y la clase se lee a mano,
  pero `Miaotofu01` → `Cattofu` salió `UNRELATED` siendo la misma persona, y `GibbonEdu` → `Gibbon
  Foundation` exigió comparación por contención de *token* (está fijado como control).

## Correr

```sh
python3 test_holder.py                 # los 15 controles
printf '%s' "$texto" | python3 extract_holder.py <org/repo> <familia>
./sweep_holder.sh                      # los 160 de P170, leyendo su archivo y su familia
```

**15/15 controles pasan**, y el par que importa son dos vocabularios distintos (regla 2 de **P126**):
`THU-MAIC/OpenMAIC` con titular `THU-MAIC` tiene que dar `HOLDER-MATCH`, y `MaybeItsAdam/tutors` con
titular `tldraw Inc.` tiene que dar `HOLDER-UNRELATED`. 🔵 **Un control hecho sólo de pares que
coinciden pasa sin ejercitar nunca la detección** — es el error que el pase 55 cometió y el 56 dejó
escrito como regla.

## Archivos

- `extract_holder.py` — extracción del titular y clasificación, con la familia **obligatoria**
- `test_holder.py` — **15 controles**, incluidos los 4 sobre los textos Apache y GPL **reales**
- `fixtures/apache-2.0-deeptutor.txt` (11.408 B) · `fixtures/gpl-3.0-moodle-COPYING.txt` (35.147 B)
  — **los textos completos, no recortes**: el primer *build* pasó un Apache recortado y aun así
  publicaba una frase como titular
- `unscoped.NEGATIVE-CONTROL-2026-10-03.py` — **control negativo fechado de D6/D7** (devuelve 87)
- `sweep_holder.sh` — delega el denominador en `../p170-headref-license-sweep/result.2026-10-03.tsv`
  (regla 1 de **P126**: no se re-adivinan nombres de archivo que P170 ya pagó)
- `result.2026-10-03.tsv` — las 160 filas (**autoritativo**)
