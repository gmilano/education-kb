---
industry: education
region: Global
updated: 2026-10-09
---

# `lib/` — los controles compartidos, no una referencia para copiar

## 🟢 Pase 74 del 2026-10-09 — `Gap 328` cierra, y el defecto estaba **en este directorio**

🔴 **`probe_payload.sh` cometía `P834`**, en el código del pase 15 sobre el que `P834` se
escribió después para advertir a otros pases: `body=$(_raw …)` saca la corrida de saltos de
línea final, así que `printf '%s' "$body" | wc -c` quedaba corto por esa corrida **en toda
medición de bytes que este probe haya emitido**. 🔵 **La regla apuntaba al instrumento
compartido y el instrumento compartido tenía el mismo defecto.**

🟢 **El seam real no es «librería sourceada vs script con argumentos» — es RED vs NO-RED.**
Medido: `. license_family.sh` 🟢 corre; `. probe_payload.sh` 🔴 **DENEGADO `[Code from
External]`** por el `curl` que contiene; `curl` directo 🔴 **DENEGADO `[Exfil Scouting]`**; y
un instrumento Python offline del mismo clon 🟢 **corre**. Ver la tabla en
`../p837-payload-measure/README.md`.

| Archivo | Qué da |
|---|---|
| `payload_measure.sh` | 🆕 **la mitad SIN RED**: `size_of_file` (byte-exacto, `P834`), `trailing_newlines`, `family_of_file`/`holder_of_file` (delegan en `license_family.sh`), `count_word_in_file`/`count_word_in_pathlist` (`P831`), `measure_payload_file` → la misma fila TSV de 6 campos |
| `measure` | 🆕 **front end invocable con argumentos**: `measure <file>`, `--size`, `--newlines`, `--family`, `--count <file> <word>`, `--self-test`. Sale **no-cero** si falta el payload — un pase no puede confundir un fallo con una medición de cero |
| `../p837-payload-measure/test_measure.sh` | 🆕 **27/27, OFFLINE**. Los casos que la cargan son **negativos**: el payload SIN salto final, donde el primitivo correcto y el defecto deben **COINCIDIR**, y el conteo por subcadena que encuentra **4** donde el acotado por palabra encuentra **1** |

🔴 **Regla para los pases que vienen, y es la que faltaba:** `size_of_capture_BROKEN` existe
sólo como control. **Ninguna cifra de bytes se publica desde `$(…)`.** Se usa
`. ../lib/payload_measure.sh` y `size_of_file`, o `lib/measure --size`. 🔵 Y `P834` queda
corregido en su enunciado: `$(…)` saca **la corrida completa** de saltos finales, no un byte
— medido 0/1/3 bytes sobre corridas de 0/1/3.

⚠️ **Lo que este pase NO verificó:** la rama de fetch de `probe_payload.sh` quedó **sin
ejecutar** (red denegada). Está `bash -n` limpia y sus primitivos están afirmados 27/27, pero
ningún repositorio vivo pasó por ella en este pase. **El primer pase con red debe correr
`test_probe_payload.sh` y esperar que cada cifra de bytes vuelva un byte más alta** que la
histórica del estante, para todo payload que termina en salto de línea. 🔵 Eso es la
corrección aterrizando, no un defecto nuevo.

---

**Pase 77 del 2026-10-03.**

`license_family.sh` existe porque una corrección de esta base **no viajó**.

El defecto GPL-3.0 / AGPL-3.0 está registrado como **P171** desde el pase 52: la sección 13 de
GPL-3.0 se titula *«Use with the GNU Affero General Public License»*, así que un clasificador que
busca `affero` en el **cuerpo** etiqueta **todo** payload GPL-3.0 como AGPL-3.0. Cinco instrumentos
(`p114`, `p170`, `p206`, `p211`, `p230`) clasifican por **bloque de título** y lo dicen en su
encabezado; `p206/test_family.py` incluso trae el *fixture* de la sección 13 como test de regresión.

🔴 **Y el pase 77 lo reintrodujo igual, en dos instrumentos nuevos**, porque escribió un clasificador
desde cero en vez de reusar uno endurecido. Leyó `LearningLocker/learninglocker` (GPL-3.0) como
AGPL-3.0 y estuvo a punto de publicar una corrección falsa contra su propia base.

🔵 **La lección, y es la razón de este directorio: una regla que hay que recordar no es un control.**
La corrección vivía en cinco instrumentos y en prosa, y un sexto instrumento no heredó nada. Un
barrido nuevo escrito de cero **vuelve a importar todos los defectos ya pagados.**

| Archivo | Qué da |
|---|---|
| `license_family.sh` | `family_of <payload>` — clasifica por **bloque de título** (P171). `affero_lines <payload>` — el discriminador cuantitativo |
| `test_license_family.sh` | **12/12**. El caso obligatorio es el *fixture* de la sección 13 de GPL-3.0 |
| `region.py` | la pregunta de región, que son **dos** preguntas con contratos opuestos (P265). Ver abajo |
| `test_region.py` | **79/79**. El caso obligatorio es que las dos funciones **DISIENTAN** |

**Regla para los pases que vienen: `. ../lib/license_family.sh`. No se inlinea un clasificador de
licencias.** Y, desde el pase 89: `from region import region_ok, regions_named`. **No se inlinea el
vocabulario de región.**

---

## `region.py` — pase 89 del 2026-10-04

**P263** (pase 88) dejó escrito que la pregunta de región tenía que mudarse acá, porque `p262` había
reintroducido **P248** —`"APAC "` con espacio aceptado— *a seis pases de distancia* del pase que lo
corrigió en `p243`. 🔴 **El pase 89 vino a cumplirlo y encontró que la regla, así escrita, no se
puede cumplir: no hay UNA pregunta de región.**

| Pregunta | Quién la hace | `"APAC "` | `🔴 **LATAM**` |
|---|---|---|---|
| **VALIDADOR** — ¿este valor está en vocabulario? | `p243` (frontmatter), `p262` (filas) | RECHAZA | RECHAZA |
| **DETECTOR** — ¿esta celda NOMBRA regiones? | `p239` (tablas publicadas) | acepta | acepta |

Una sola función compartida habría roto una de las dos: con la leniencia del detector **P248 se
reabre**; con el rigor del validador `p239` vuelve a reclamar como incompletas tablas que están
completas. 🔵 **Así que el contrato de este módulo es que las dos funciones DISIENTAN**, y eso está
afirmado valor por valor en la suite. La matriz que lo midió —**34 valores × 7 implementaciones**,
con **18** veredictos opuestos— está en
[`../p265-region-contract/`](../p265-region-contract/).

🔴 **Y hay una tercera función, porque ni los validadores coinciden.** `p243` acepta `" APAC"` y
`p262` lo rechaza, **y los dos tienen razón**: en YAML el blanco de la izquierda separa la clave del
valor y no es dato; en una celda TSV, sí lo es. De ahí `region_ok_frontmatter()`. A la derecha
ninguno perdona: eso sigue siendo P248.

| Función | Contrato |
|---|---|
| `region_ok(v)` | VALIDADOR, portador **dato**. Exacto byte a byte. `None` y `""` rechazados |
| `region_ok_frontmatter(v)` | VALIDADOR, portador **YAML**. Saca el separador de la izquierda, nada de la derecha |
| `regions_named(cell, strict=True)` | DETECTOR. `strict` es el **default**, y eso es contrato: ver P266 |
| `variants_in(cell)` | las grafías que el detector normalizó, clasificadas `MARKUP` / `CASO` / `SEPARADOR` |
| `actionable_variants(cell)` | las de arriba que **no** son sólo formato. Es la cifra que vale (P267) |
| `REGIONS`, `DIVERGENCE` | el vocabulario cerrado, y la clase donde las dos funciones deben oponerse |

🟢 **Los tres instrumentos del árbol ya delegan acá, y cada uno reprodujo su total exacto** —`p262`
47/47, `p243` 23/23, `p239` 23 tests `OK`—, que es la prueba de que la migración no cambió
comportamiento. Las copias locales (`REGIONS`, `NORM_DROP`, `PAREN`) se **borraron**: una copia muerta
es la invitación concreta a incumplir P263.

### 🔵 P266, que este módulo aprendió de sí mismo

**La primera versión de `regions_named()` puso `strict=False` por default.** `p239`, el instrumento
del que salió, tiene `strict=True`. O sea que el módulo escrito para no volver a elegir un defecto
eligió uno nuevo en su primera línea, y lo encontró la matriz de P265 al ver que su columna no
coincidía con la de `p239`.

⚠️ **El contraejemplo ya estaba en el árbol:** `p243.parse_frontmatter(text, raw=False)` tiene la
lectura endurecida —la que cierra P248— **detrás de un argumento NO default.** Hoy el único llamador
interno pasa `raw=True`; el próximo que importe la función hereda la floja sin pedirla.

🟢 **La regla: cuando una función tiene una versión segura y una lenient, la segura es el DEFAULT y
la lenient se PIDE.** Una regla que vive en `lib/` pero detrás de un flag no viajó: viajó a medias.

---

## `probe_payload.sh` — el bucle, no sólo el clasificador

**Pase 15 del 2026-10-06 (capa SIS/MIS).**

Este directorio existía ya, con la regla escrita arriba, y **se rompió otra vez**. El pase 15
escribió su propio bucle de sondeo (`curl` + `grep`) sin hacer `source` de
`license_family.sh`, y reportó **cuatro** payloads **GPL-3.0/AGPL-3.0** como Creative
Commons/NonCommercial (`SapuSeven/BetterUntis` 300★, `TEAMSchools/powerschool`,
`sikkepitje/TeamSync`, `sas-fossdev/saspes`).

🔴 **La causa ya estaba medida en esta base**: el cuerpo de GPL-3.0 dice *«noncommercially»*
en su sección 6, **línea 259 del payload**, y `license_family.sh` ya lo resolvía con una
compuerta — la rama Creative Commons se entra sólo con un marcador CC, y `NonCommercial` se
lee después como **atributo** de una familia CC, nunca como familia propia. 🟢 **Probado este
pase, la librería acierta los tres payloads difíciles a la primera: `GPL-3.0`, `AGPL-3.0`,
`CC-BY-NC-SA-4.0`.**

🔵 **El diagnóstico, y es la razón de este archivo nuevo.** La pregunta de **familia** tenía
control; el **bucle que la rodea** no. Así que cada pase seguía escribiendo el `curl` y el
`grep` a mano y, mientras lo escribía, **volvía a elegir el clasificador también.** La regla
«hacé `source` de la librería» no se cumple porque escribir seis líneas de `grep` es más
barato que encontrar la librería.

🟢 **`probe_payload.sh` es ese bucle.** `probe_repo <owner/repo>` devuelve TSV
`repo · rama · archivo · bytes · familia · titular`, clasificando con `family_of()` y
`holder_of()` de `license_family.sh`. **Un control que nadie tiene que ensamblar es el único
que se usa.**

Cierra además **tres trampas medidas en repositorios reales del pase 15**, no en fixtures:

| # | Trampa | Especímenes reales |
|---|---|---|
| 1 | 🔴 **La rama por defecto no es `main` ni `master`** | `GibbonEdu/core` → **`v31.0.00`** · `portabilis/i-educar` → **`2.12`** · `francoisjacquet/rosariosis` → **`mobile`** — **3 de las 5 plataformas SIS abiertas más estrelladas que existen.** Una rama hardcodeada las anota a las tres como *sin cesión*, y son **GPL**, que es una entrega muy distinta. |
| 2 | 🔴 **La licencia vive en un subdirectorio, con mayúsculas mixtas** | `OS4ED/openSIS-Classic` guarda GPL-2.0 en **`docs/License.txt`** (con BOM). **Ninguna escalera de nombres de esta base la encontraba**; el *enlace del propio README* sí, en una petición. Por eso el enlace del README se intenta **antes** de la escalera larga. |
| 3 | 🟢 **Ortografía británica** | `AkizumiFox/NTU-COOL-Assignment-Status-Viewer` trae `LICENCE`. El pase 14 midió la escalera completa de 20 nombres en **0 pagos sobre 98 repos** y dijo no volver a comprarla; `LICENCE` es **una** petición y pagó **1 de 44**. La lista corta de `PROBE_NAMES` es ese hallazgo, no una conjetura. |

🟢 **Y un veredicto nuevo que no es una ausencia: `DECLARED-NOT-GRANTED`.** Un README que
**apunta** a un archivo de licencia que no existe no es silencio — es un mantenedor que
**cree** que cedió. Espécimen: [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms)
(**103★**, el segundo servidor MCP de Canvas más estrellado) dice *«MIT License - see
[LICENSE] file for details»* y **no trae ese archivo**. Eso es un **pedido upstream de un
commit**, y reportarlo como «sin cesión» pierde esa distinción.

⚠️ **Lo que este archivo NO contesta, y es el límite que el pase 15 encontró:** un payload
contesta la pregunta de **copyright**. La pregunta de **acceso** —¿podemos *llamar* a este
sistema?— vive en los Términos de Uso de un tercero, es invisible para todo sondeo de este
directorio, y tiene su propia compuerta: **P26** en `compose/patterns.md`. El pase 15 encontró
un componente **MIT** que es **inentregable** exactamente por eso.

**Suite:** `bash lib/test_probe_payload.sh` → **12/12**. Los doce casos son repositorios
reales y pegan a la red a propósito, por la lección de este mismo README: *un fixture lo
bastante corto para ser cómodo es lo bastante corto para no ver el defecto.*

---

## 🆕 `package_repo.sh` + `pkgrepo` — package name → repository (pass 75, `Gap 329`)

🔵 *Written in English, consistent with every pass since the 2026-10-06 reset; the Spanish
above is pass 15's and is left as it stands.*

🟢 **`package_repo.sh`** is the **network-free** half: `normalise_repo_url`,
`repo_from_pypi_json`, `repo_from_npm_json`, `repo_from_packagist_json`, and the three
`core_deps_of_*` manifest readers that `P15` named and no pass had written. 🟢 **`pkgrepo`** is
the argument-invocable front end (`--pypi --npm --packagist --parse --deps --closure
--self-test`) and holds the only `curl`, per `P838`'s seam.

🟢 **Suite:** `bash ../p840-package-repo/test_package_repo.sh` → **37/37**, offline.

🔴 **The verdicts are loud on purpose**, following `measure`'s `NO-PAYLOAD` precedent:
`NO-REPO` (metadata exists, no source declared — **`Gap 327`'s category**),
`UNRESOLVABLE-HOST` (an SSH-config alias, e.g. `git@ibl_connection:…` — an address only the
publisher can resolve), `NON-GITHUB`, `NO-METADATA`. 🔴 **Never collapse `NO-REPO` into
`NO-METADATA`**: one is a package that publishes no source, the other a name that does not
exist.

⚠️ **The limit this file inherits, and it is the same shape as the one above:** a resolved
path answers **where the source is**, not whether the **grant** is in it. 🟢 **Both reads are
available in this session:** the shipped tarball (npm) *and* the repository —
`raw.githubusercontent.com` answers **200** here, and `lib/test_probe_payload.sh` runs
**12/12** against live repositories. 🔴 **The shelf had recorded that channel as refused and
the record was stale**, which is `P844`. 🟡 What remains of **`Gap 330`** is the PyPI/Packagist
payload read and the `NON-GITHUB` case — not a defect of this library.

🔴 **And the lesson the suite encodes:** it was **32/32 green while the instrument was wrong**,
on the first real address it met. 🟢 **`P841` — re-assert every verdict class against a live
payload before citing the instrument.** 🔵 Pass 74 predicted this about its own unexecuted
fetch branch and was right.
