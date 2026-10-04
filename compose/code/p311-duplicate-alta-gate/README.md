---
industry: education
region: Global
updated: 2026-10-04
---

# `p311-duplicate-alta-gate/` — la pregunta que ningún control de esta base hacía

**Qué prueba:** que un slug que esta base **ya publicó** se detecte **antes** de redactarlo como
alta, y que un slug legítimamente nuevo **no** se frene.

## Por qué existe, y es un defecto de ESTE pase

El pase 100 rotó su eje de búsqueda a pronunciación y práctica oral —eje que eligió con su **propio**
barrido de mercado—, midió **14 candidatas de primera mano** y tenía redactada una nota de cabecera
que anunciaba que *«esta base no tenía NINGUNA pieza de habla»*.

🔴 **Era falso.** `repos/foundations.md` tiene una sección titulada **«Capa de habla y lectura
oral»** desde el **pase 14 (2026-10-01)**, con `Halleck45/OpenPronounce`, `kaldi-asr/kaldi` y
`jimbozhang/speechocean762` — **incluido el hallazgo de que el corpus no trae archivo de licencia**,
que el pase 100 estaba por publicar como nuevo. Lo mismo con `eecs-autograder/autograder.io`,
inventariado en `verticals/solutions.md` desde el **pase 5** con su licencia ya marcada como no
declarada.

🔵 **El defecto no es una licencia mal leída ni un número mal: es que un ALTA estaba por publicarse
sobre piezas que la base YA TENÍA, y nada en el repositorio habría objetado.**

## Y la razón es ESTRUCTURAL, que es lo que lo hace un patrón y no un descuido

Esta base tiene controles para casi todo:

| Control | Qué audita |
|---|---|
| `p243-frontmatter-coverage` | que cada `.md` traiga frontmatter y región del vocabulario cerrado |
| `p239-table-integrity` | que ninguna fila de encabezado o de ejemplo quede como dato |
| `p265-region-contract` | el vocabulario de región |
| `trend-backlink-audit` | que cada tendencia citada exista como sección |
| `pattern-citation-audit` | que cada patrón citado exista |
| `lib/license_family.sh` | la familia de licencia |
| `p184` / `p255` | el titular |
| `p250` | el uso comercial |
| `p280` / `p283` / `p289` | la propiedad y la licencia declaradas en el manifiesto |

🔴 **Ninguno pregunta *«¿esto ya está acá?»*.** Y el motivo es que **todos auditan una afirmación que
el pase HACE** —*esta licencia es X*, *este titular es Y*, *esta región es Z*, *esta cita existe*—
mientras **la afirmación de que un alta es NUEVA no se escribe en ninguna parte: está implícita en
llamarla alta.** 🔵 **Lo implícito no tiene superficie que auditar, así que nada lo auditaba** — y
un pase 100 pases y ~250 slugs adentro puede republicar su propia capa sin fricción.

## Lo que reporta, y por qué la SECCIÓN es la columna que importa

```
ALREADY PUBLISHED  Halleck45/OpenPronounce
    agents/top.md:5214            [Capa de lectura oral y pronunciación — agregada en el pase 14…]
    repos/foundations.md:3922     [Capa de habla y lectura oral — agregada en el pase 14 del 2026-10-01]
    verticals/solutions.md:3230   [Capa de lectura oral — agregada en el pase 14 del 2026-10-01]
```

🔵 **Archivo, línea y sección.** Sin la sección la respuesta es *«ya está»*, que obliga a ir a
buscar; con la sección es *«ya está, en la capa de habla agregada en el pase 14»*, que es
**accionable**: dice si corresponde **no publicar**, o **publicar como corrección de alcance** sobre
la sección que ya existe. El pase 100 hizo lo segundo con `speechocean762`.

## Los tres veredictos, y el del medio es el que evita que el gate estorbe

| Veredicto | Qué significa | Qué hacer |
|---|---|---|
| 🟢 `NEW` | el slug no aparece en ningún archivo publicado | publicar como alta |
| ⚠️ `NAME COLLISION` | el **slug** no está; el **nombre** del repo sí, bajo otro propietario | **publicar**, y revisar que no sea un *fork* no declarado (`fork-lineage-audit`) |
| 🔴 `ALREADY PUBLISHED` | el slug exacto está publicado | no es alta |

🔵 **`NAME COLLISION` existe porque el falso `ALREADY` sería peor que el defecto que este gate
arregla: suprimiría trabajo real.** Esta base inventaría `AmirF194/canvas-mcp` **y**
`BartMassey-upstream/canvas-mcp` como filas distintas y legítimas, y el pase 99 midió
`examplary/qti` **e** `instructure/qti` como piezas distintas con licencias distintas. **Un gate que
las confundiera se desactivaría en dos pases.**

⚠️ **Y la sonda de nombre desnudo está acotada por LONGITUD (≥ 5 caracteres) y por frontera de
palabra**, que es `P299` en la clave de este instrumento: `qti` son 3 caracteres y el inventario
tiene **cuatro** propietarios distintos de ese nombre, así que sin la cota **toda** alta de QTI
llegaría pre-marcada y el gate se volvería ruido.

## El denominador: `compose/code/` queda FUERA a propósito

Las *fixtures* y los `.tsv` de los instrumentos **nombran** slugs para medirlos, y medir no es
publicar. Contarlos haría que **toda candidata medida pareciera una fila existente** — el falso
`ALREADY` otra vez, por la puerta de atrás. El control negativo que lo afirma está en la suite.

## Invocación

```sh
python3 check_duplicate.py --self-test                        # fixtures, OFFLINE — hoy 11/11
python3 check_duplicate.py mikhailvs/loqui YuanGongND/gopt    # slugs explícitos
python3 check_duplicate.py --stdin < candidates.input.txt     # el barrido de un pase
```

**Sale con estado 1 cuando alguno ya está publicado**, así que puede usarse como compuerta antes de
redactar o antes de un *commit*.

## Resultado del pase 100 (`result.2026-10-04.txt`)

| Veredicto | N | Slugs |
|---|---|---|
| 🟢 `NEW` | **8** | `mikhailvs/loqui` · `Priyamakeshwari/TeachGPT` · `YuanGongND/gopt` · `Submitty/Submitty` · `autolab/Autolab` · `speechsuper/SpeechSuper-API-Samples` · `speechace/speechace-api-samples` · `ABCoder1/mentorAI` |
| ⚠️ `NAME COLLISION` | **1** | `Ovsyanka83/autograder` — el nombre `autograder` ya aparece en dos secciones de `agents/top.md`, bajo otros propietarios |
| 🔴 `ALREADY PUBLISHED` | **5** | `Halleck45/OpenPronounce`, `kaldi-asr/kaldi`, `jimbozhang/speechocean762` (**pase 14**) · `INGInious/INGInious`, `eecs-autograder/autograder.io` (**pases 5** / **67**) |

🔴 **Las cinco se habrían publicado como alta sin este gate**, y tres de ellas arrastrando un
hallazgo —el corpus sin licencia— que la base ya tenía escrito desde el pase 14.
