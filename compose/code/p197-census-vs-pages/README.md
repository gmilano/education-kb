---
industry: education
region: Global
updated: 2026-10-14
---

# `p197-census-vs-pages` — ¿«nunca sondeada» o sólo «ausente del TSV»?

**Pasada `197`, `2026-10-14`.** p196 pre-registró *«sondear las `26` filas del padrón que
ningún censo alcanzó»*. [`../p197-grant-read/`](../p197-grant-read/) las sondeó. Este
directorio contesta la pregunta que es **anterior** a esa acción: **¿estaban medidas en las
páginas?** Porque una fila publicada con su cifra de bytes está medida, esté o no en el
artefacto del censo.

## Veredicto: 🔴 **la premisa de la acción era falsa, y el hueco estaba en el artefacto**

| veredicto | filas | qué significa |
|---|---|---|
| 🟢 **`AGREE-PUBLISHED`** | **`16`** de `30` | la página trae **la misma cifra de bytes, al byte**, que el canal de árbol midió hoy |
| 🟡 `SLUG-NO-FIGURE` | `13` | el slug está publicado, sin cifra de concesión |
| 🟡 `MULTI-SLUG-LINE` | `1` | la única cifra discrepante vive en una celda que nombra **otro** slug |
| 🔴 `DISAGREE` | 🟢 **`0`** | ninguna contradicción real |

🟢 **`16` acuerdos entre dos canales independientes y `0` divergencias** *(árbol + `cat-file`
hoy, contra lo que pasadas anteriores publicaron por el canal de payload)*. 🔵 Eso no es una
nota al pie: es la primera validación cruzada del canal de árbol contra el estante publicado.

🔴 **Y la lección es la reincidencia que esta base ya tiene anotada dos veces:** p196 leyó
*«ausente del TSV de p195»* como *«nunca medida»*. `16` de esas filas llevaban su cifra
publicada. **Leer un resumen como si fuera el estado del saber** — p194 lo registró contra
p193, p195 lo repitió, y p196 lo cometió sobre la lista de huecos de p195.

## 🔴 Las dos acusaciones que el comparador v1 emitió, y las dos eran suyas

`Gap 441` dice: *un instrumento se mide contra las filas que ACUSA.* Se midió. Las dos:

| fila acusada | la cifra que «contradecía» | lo que es de verdad |
|---|---|---|
| `midudev/libros-programacion-gratis` | `50 266` B | 🔴 **el tamaño del README**, y la página lo dice: *«README (`50 266` B) mentions no licence»*. La página **COINCIDE** con la lectura |
| `O0000-code/awesome-academic-skills` | `1 230` B | 🔴 **es de `GarethManning/education-agent-skills`**, nombrado en la MISMA celda de `intel/trends.md` |

🔵 **La segunda es `Gap 441` literal:** *«la fila que se lee mal es la MEJOR documentada,
porque una celda que explica su licencia contra otra más conocida contiene dos
identificadores»*. 🔴 **La regla estaba escrita, con número, y este instrumento la volvió a
importar.** Registrado como reincidencia contra mí mismo.

Las dos reglas que la v2 lleva, por eso:

1. **una cifra en bytes no es una cifra de CONCESIÓN** si los `24` caracteres previos la
   declaran de otra cosa *(`README`, `paths`/`rutas`, `★`, `LOC`, `commits`)*;
2. **una línea que nombra otro slug no acusa**: su cifra puede ser de la otra fila, y el
   veredicto es `MULTI-SLUG-LINE`, que es *«no atribuible»*, no *«de acuerdo»*.

## Suite — `test_compare.py`, `10`/`10`, offline

🔴 **Un comparador que nunca acusa pasaría cualquier suite construida con sus aciertos.** Así
que las dos primeras cajas son **las dos acusaciones falsas de hoy, con el texto real de las
páginas**, y la tercera es una contradicción **verdadera y sintética** que tiene que seguir
disparando:

| caso | entrada | debe contestar |
|---|---|---|
| `C1` | la celda real de `midudev` con su `50 266` B de README | `SLUG-NO-FIGURE` |
| `C2` | la celda real `T5` de `intel/trends.md`, con dos slugs | `MULTI-SLUG-LINE` |
| 🟢 `C3` | un slug solo, con **otra** cifra de concesión | 🟢 **`DISAGREE`** *(el positivo verdadero)* |
| `C4`,`C4b`,`C4c` | `11 348` con espacio, coma y espacio duro | `AGREE-PUBLISHED` ×3 |
| `C5` | un slug que no está en ninguna página | `SLUG-ABSENT` |
| `C6` | una fila sin bytes | ni `AGREE` ni `DISAGREE` |
| `C7`,`C8` | `833`★ y `5 345` paths | `SLUG-NO-FIGURE` ×2 |

## Lo que NO hace

🔴 No compara **familias**, sólo cifras de bytes: una página que publicara `MIT` donde los
bytes dicen `GPL-3.0` con el mismo tamaño pasaría como `AGREE`. 🔵 Improbable y no imposible;
el eje de familia queda **pre-registrado** para p198 junto con el barrido de las `494` filas,
porque este corpus de `30` no es el estante.
