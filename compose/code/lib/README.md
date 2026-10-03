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

**Regla para los pases que vienen: `. ../lib/license_family.sh`. No se inlinea un clasificador de
licencias.**
