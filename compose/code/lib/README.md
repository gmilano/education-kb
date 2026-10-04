---
industry: education
region: Global
updated: 2026-10-04
---

# `lib/` — los controles compartidos, no una referencia para copiar

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
