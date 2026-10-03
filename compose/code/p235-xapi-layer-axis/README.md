# P235 — el eje CAPA de P230 se reproduce, y su SIGNO se INVIERTE entre estándares

**Pase 77 del 2026-10-03.** Instrumentos: `measure.sh`, `classify_title.sh`,
`negative-control.2026-10-03.sh`. Salidas: `result.2026-10-03.tsv`,
`result-agpl-audit.2026-10-03.tsv`, `result-negcontrol.2026-10-03.tsv`.

## La pregunta que el pase 76 dejó abierta

**P230** midió la capa OneRoster por **CAPA** (servidor / cliente / puente) y concluyó: *«CONSUMIR
OneRoster con licencia permisiva se puede hoy; EXPONERLO no.»* Lo que no se sabía es si eso es una
propiedad **del SECTOR** o **del ESTÁNDAR**. Este instrumento le hace la misma pregunta de tres capas
a **otro** estándar del mismo sector —**xAPI**— para poder comparar celda contra celda.

## Resultado: el eje se reproduce y el signo se da vuelta

| CAPA | OneRoster (**P230**, pase 76) | xAPI (**P235**, este pase) |
|---|---|---|
| **servidor** | 🔴 ningún permisivo en spec vigente | 🟢 **dos permisivos VIVOS**: `yetanalytics/lrsql` (Apache-2.0, `HEAD` **2 d**) · `openfun/ralph` (MIT, **26 d**) |
| **cliente** | 🟢 cuatro permisivos, uno en spec vigente | ⚠️ **permisivos pero TODOS congelados**: `php-xapi/model` (MIT, **1,7 a**) · `TinCanPHP` (Apache-2.0, **3,9 a**) · `TinCanPython` (Apache-2.0, **6,1 a**) |
| **puente** | 🔴 los dos existentes **sin archivo de licencia** | 🟡 **MIT**, pero el *upstream* congelado **1,1 a** y el único «vivo» no es sucesión (ver **P238**) |

🔵 **Por lo tanto: «CONSUMIR se puede, EXPONER no» es una propiedad de OneRoster, NO de educación.**
Para xAPI la frase correcta es **la inversa**: 🟢 **EXPONER xAPI —ser el LRS— se puede hoy, con
licencia permisiva y mantenimiento de esta semana; el cuello de botella está en el CLIENTE y en el
PUENTE.** Generalizar el signo de P230 al sector habría invertido exactamente la recomendación.

**Reparto de licencia de la capa: 8 de 9 piezas son permisivas.** La única copyleft es
`LearningLocker/learninglocker` (**GPL-3.0**, `HEAD` **2021-11-16** → 4,9 años).

## El control negativo, y es lo que salva el resultado

`classify_title.sh` auditó **los cinco veredictos AGPL que esta base sostiene** y **los cinco son
correctos** (bloque de título, y tres además concordantes con su manifiesto):
`csmediapro/moodle-mcp-server`, `usechalk/chalk`, `helixnow/deep-student`, `schroedinger-hat/certo`,
`instructure/canvas-lms`.

🔴 **Y ahí está el problema de método: un clasificador validado sólo sobre repos AGPL saca 5/5 y
sigue roto**, porque AGPL → AGPL acierta por casualidad. El defecto se ve **únicamente** sobre
payloads GPL-3.0, y `negative-control.2026-10-03.sh` lo muestra en la capa que más duele:

| Pieza | `grep` del cuerpo | bloque de título | líneas con `affero` | Veredicto |
|---|---|---|---|---|
| **`moodle/moodle`** | 🔴 AGPL-3.0 | 🟢 **GPL-3.0** | **3** | **FALSO POSITIVO** |
| `LearningLocker/learninglocker` | 🔴 AGPL-3.0 | 🟢 **GPL-3.0** | **3** | **FALSO POSITIVO** |
| `oat-sa/qti-sdk` | GPL | GPL-2.0 | **0** | OK |
| `oat-sa/extension-tao-testqti` | GPL | GPL-2.0 | **0** | OK |
| `csmediapro/moodle-mcp-server` | AGPL-3.0 | AGPL-3.0 | **15** | OK |
| `instructure/canvas-lms` | AGPL-3.0 | AGPL-3.0 | **15** | OK |

🔴 **Un `grep` de cuerpo etiqueta a Moodle como AGPL-3.0** — el LMS más instalado del planeta y el
argumento de *«el cliente ya lo tiene»* más grande de esta KB. Y **AGPL §13 contra GPL-3.0 es
exactamente la distinción que decide si se puede construir un producto alojado encima**: es el error
más caro que esta base podría cometer.

🟢 **Dos cotas nuevas que el registro de P171 no tenía:**

1. **Discriminador cuantitativo:** GPL-3.0 nombra la AGPL en **3** líneas (su §13); una AGPL-3.0 real,
   en **15**.
2. **El defecto es específico de versión:** GPL-2.0 da **0** — predata a la AGPL. 🔵 **Así que sólo las
   filas GPL-3.0 estuvieron en riesgo, y la capa QTI de esta base (GPL-2.0) nunca lo estuvo.**

## Cotas del instrumento, declaradas

- La columna `spec_en_codigo` sólo rinde cuando la versión está **en el árbol** (nombre de archivo o
  constante). Siete de nueve piezas dan `(sin version en el arbol)`: **ausencia de instrumento, no
  ausencia de conformidad.** La única que rindió es `Transcordia/jupiter` → **xAPI 0.9.5**.
- `caliper-en-codigo` cuenta archivos no-Markdown que nombran Caliper. **Da 0 en las nueve**, incluida
  la pieza cuya fila en esta KB decía «LRS xAPI + **Caliper**».

## Cómo correrlo

```sh
./measure.sh yetanalytics/lrsql:servidor openfun/ralph:servidor Transcordia/jupiter:servidor \
             LearningLocker/learninglocker:servidor RusticiSoftware/TinCanPHP:cliente \
             RusticiSoftware/TinCanPython:cliente php-xapi/model:cliente \
             DavidLMS/learnmcp-xapi:puente ashleycribb/learnmcp-xapi:puente
./negative-control.2026-10-03.sh moodle/moodle LearningLocker/learninglocker oat-sa/qti-sdk
```
