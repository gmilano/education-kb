---
industry: education
region: Global
updated: 2026-10-04
---

# `p265-region-contract/` — la pregunta de región son DOS preguntas, y ni los validadores coinciden

**Pase 89 del 2026-10-04.** Este directorio existe porque el pase 88 escribió **P263** —«mientras
la pregunta no viva en `compose/code/lib/`, cada instrumento nuevo la reimplementa y vuelve a elegir
el bug»— y el pase 89 fue a cumplirlo. 🔴 **Y la regla, tal como estaba escrita, no se puede
cumplir: no hay UNA pregunta de región.**

## Lo medido

Una matriz de **34 valores** contra **7 implementaciones**, todas invocadas por su superficie
pública y ninguna reimplementada:

| Columna | Implementación | Pregunta |
|---|---|---|
| `p243` | `check_frontmatter.findings_for()` | VALIDADOR, portador frontmatter |
| `p262` | `mandate.region_ok()` | VALIDADOR, portador dato |
| `lib` | `lib.region.region_ok()` | VALIDADOR, portador dato |
| `libf` | `lib.region.region_ok_frontmatter()` | VALIDADOR, portador frontmatter |
| `p239` | `check_tables.regions_in_cell()`, su default | DETECTOR |
| `p239l` | ídem con `strict=False` | DETECTOR lenient |
| `libd` | `lib.region.regions_named()`, su default | DETECTOR |

```
python3 measure.py          # la tabla legible
python3 measure.py --tsv    # result.2026-10-04.tsv
python3 test_measure.py     # 30/30
```

**Las tres cifras del pase:**

| Cifra | Qué dice |
|---|---|
| **34** valores medidos | la matriz, en 8 clases: `EXACTO`, `P248`, `CASO`, `ADORNO`, `MULTIPLE`, `RESIDUO`, `BALDE`, `AUSENTE` |
| **1** valor donde los dos validadores preexistentes DISCREPAN | `" APAC"`: `p243` lo **acepta**, `p262` lo **rechaza** |
| **18** valores donde VALIDADOR y DETECTOR dan veredicto OPUESTO | y eso es el contrato, no un defecto |

## 🔴 El hallazgo: los dos validadores discrepan y **los dos tienen razón**

`p243` acepta `" APAC"` porque su portador es YAML, donde `region:   APAC` separa la clave del valor
con blanco arbitrario: **a la izquierda el blanco es SINTAXIS, no dato.** `p262` lo rechaza porque su
portador es una celda TSV, donde **sí es dato**.

🔵 **Así que «¿está en vocabulario?» no tiene una sola respuesta ni siquiera entre validadores:
depende de la SINTAXIS DEL PORTADOR.** Por eso `lib/region.py` expone `region_ok()` y
`region_ok_frontmatter()` y no un parámetro: un parámetro invita a pasar el default.

⚠️ **A la derecha ninguno de los cuatro perdona**, y eso sigue siendo **P248** —el defecto que el
pase 82 corrigió en `p243` y el pase 88 reintrodujo en `p262`, a seis pases de distancia.

## 🔴 Y por qué una sola función compartida habría roto algo

Con la leniencia del detector, `p243` y `p262` vuelven a aceptar `"APAC "` y **P248 se reabre**. Con
el rigor del validador, `p239` deja de reconocer sus propias celdas publicadas —`| 🔴 **LATAM** |`,
`| APAC (Vietnam) |`, `| **APAC / LATAM** |`— y **vuelve a reclamar como incompletas tablas que están
completas**: los tres falsos positivos que su v1 ya pagó.

🟢 **De modo que la divergencia de 18 valores no es algo a conciliar: es el contrato**, y
`lib/test_region.py` lo afirma valor por valor como caso obligatorio. Una suite que sólo dijera «el
validador rechaza las variantes» pasaría igual con una única función lenient compartida — que es
exactamente el control insensible que la regla de **P126** prohíbe.

## P263, cumplido en los tres instrumentos

Las tres implementaciones del árbol pasan a delegar en `lib/region.py`, **y cada una reprodujo su
total exacto de antes**, que es la prueba de que la migración no cambió comportamiento:

| Instrumento | Antes | Después |
|---|---|---|
| `p262-mandate-level/test_classify.py` | 47/47 | **47/47** |
| `p243-frontmatter-coverage/test_check_frontmatter.py` | 23/23 | **23/23** |
| `p239-table-integrity/test_check_tables.py` | 23 tests `OK` | **23 tests `OK`** |

🟢 Y las copias locales del vocabulario se **borraron**, no se dejaron de adorno: `NORM_DROP` y
`PAREN` quedaban muertas en `p239` y una copia muerta es la invitación concreta a incumplir P263.

## 🔵 P266 — el comportamiento endurecido va en el DEFAULT, no detrás de un flag

La primera versión de `lib/region.py` puso `strict=False` por default en el detector. **`p239`, el
instrumento del que salió, tiene `strict=True`.** O sea que el módulo compartido, escrito para no
volver a elegir un defecto, eligió uno nuevo en su primera línea.

⚠️ **El contraejemplo ya estaba en el árbol:** `p243.parse_frontmatter(text, raw=False)` tiene la
lectura endurecida —la que no limpia la derecha, la que cierra P248— **detrás de un argumento NO
default**. Hoy el único llamador interno pasa `raw=True`; el próximo que importe la función hereda la
versión floja sin pedirla.

🟢 **La regla: cuando una función tiene una versión segura y una lenient, la segura es el default y
la lenient se PIDE.** `regions_named(cell, strict=True)` y `regions_named(cell, strict=False)`.

## 🔵 P267 — el vocabulario cerrado se aplica en un portador y no en el otro

`measure_variants.py` mide el hueco sobre el árbol real: `p243` reclama `region: Latam` en el
frontmatter, pero la misma grafía en una **celda** la normaliza el detector de `p239` y **no se
reporta nunca**.

```
python3 measure_variants.py          # variants.2026-10-04.tsv
```

| Cifra | |
|---|---|
| **66** archivos `.md` recorridos | los 67 del árbol menos el fixture, porque ahí la variante está **plantada** y contarla haría que el instrumento reporte su propia entrada de prueba |
| **160** celdas que el detector normaliza en silencio | |
| **160** de clase `MARKUP` | `**LATAM**`, `` `EMEA` ``, `🔴 **LATAM**` — es FORMATO, no una variante |
| **0** de clase `CASO` o `SEPARADOR` | las accionables |

🟢 **Así que el árbol está limpio en este eje hoy y el hueco es LATENTE**: el instrumento es una
guarda para los pases que vienen, no una limpieza para este.

🔴 **Dos correcciones que este pase tuvo que hacerse a sí mismo, y son la parte reproducible:**

1. **La primera corrida devolvió 172 hallazgos, de los cuales 164 eran `**LATAM**`.** Negrita no es
   una variante de grafía: es formato. Confundirlas es el mismo falso positivo que la v1 de `p239`
   pagó tres veces, cometido sobre el instrumento que vino a auditarla. De ahí la clasificación en
   `MARKUP` / `CASO` / `SEPARADOR`, y la cifra que vale es la de las dos últimas.
2. **Sin compuerta, el barrido devolvió 8 hallazgos y los 8 eran falsos positivos** — celdas de
   CIFRAS (`92 % LATAM`, `**APAC $591,6M`) y de PROSA donde `global` es adjetivo (`Uso de AI por
   estudiantes, global`). Es la clase exacta que el modo `strict` de `p239` existe para descartar.
   La población correcta no es «toda celda»: es **las celdas que `p239` cuenta como celdas de
   región**, o sea su veredicto strict. Archivado en
   [`ungated.NEGATIVE-CONTROL-2026-10-04.tsv`](ungated.NEGATIVE-CONTROL-2026-10-04.tsv).

🟢 **Y el cero tiene control positivo**, porque un cero sin él no vale nada:
[`fixtures/tabla-con-variante.md`](fixtures/tabla-con-variante.md) es una tabla regional legítima con
dos grafías plantadas —`**latam**` (`CASO`) y `**North-America**` (`SEPARADOR`)— más dos de
vocabulario con negrita y una exacta. El barrido tiene que encontrar **exactamente las dos**, y eso
es lo que `test_measure.py` afirma.

## Archivos

| Archivo | Qué es |
|---|---|
| `measure.py` | la matriz diferencial de 34 × 7 |
| `measure_variants.py` | el barrido de grafías sobre el árbol real, con la compuerta strict |
| `test_measure.py` | **30/30**, con el control positivo del fixture y la discrepancia medida |
| `result.2026-10-04.tsv` | la matriz, para diffear entre pases |
| `variants.2026-10-04.tsv` | el barrido de grafías |
| `ungated.NEGATIVE-CONTROL-2026-10-04.tsv` | el barrido SIN compuerta: 8 hallazgos, 8 falsos positivos |
| `fixtures/tabla-con-variante.md` | el control positivo |

**Entorno:** `Python 3.11.15`.
