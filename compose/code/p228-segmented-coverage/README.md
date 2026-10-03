---
industry: education
region: Global
updated: 2026-10-03
---

# `p228-segmented-coverage` — el instrumento que al pase 74 le faltaba (pase 75 del 2026-10-03)

**Qué mide.** La cobertura de esta KB por plataforma, **contra la base instalada** y **dentro de una
sola cohorte** — donde una cohorte es el par `(segmento, unidad)`. Implementa el procedimiento que
**P224** escribió en el pase 74, y hace cumplir las dos reglas que ese pase enunció pero no pudo
hacer cumplir, porque **no existía instrumento**:

| Regla | Qué exige | Qué pasó sin ella (pase 74) |
|---|---|---|
| **P227** | un agregado sobre varios archivos tiene que **NOMBRAR el conjunto**, en **cada** archivo donde se publica | publicó «229 líneas / 389 ocurrencias en los 4 archivos de contenido» en **7** archivos; **1** dice cuáles y **6 no** |
| **P228** | una cifra de cuota no significa nada sin su **SEGMENTO** (K-12 / superior) y su **UNIDAD** (usuarios / instituciones / instalaciones) | comparó los ~150 M de **USUARIOS** de Classroom contra la cuota de Canvas en **INSTITUCIONES** de superior, y concluyó una «inversión» |

## Las invocaciones y sus cifras (regla de P107: la cifra se publica con su invocación)

| Invocación | Qué prueba | Hoy |
|---|---|---|
| `python3 test_coverage.py` | los controles, incluida la negativa que al pase 74 le habría bloqueado la conclusión | **15/15** |
| `python3 reproduce_p224.py` | el agregado de P224 contra el commit que citó: **182** subconjuntos de tamaño 3-5, **1** reproduce | **3/3** |
| `python3 measure.py --at 5dd2bcc` | la medición por cohorte **en un commit fijo** | **7** inversiones en K-12, **1** en superior |

## 🔵 Lo que `reproduce_p224.py` establece, y es a favor del pase 74

La cifra de P224 **es correcta y reproduce exactamente** — y `agents/top.md` **sí nombra** los cuatro
archivos (línea 250), así que el pase 74 hizo el trabajo. 🔴 **El defecto es de PROPAGACIÓN, no de
medición:** el mismo agregado se publica en **7** archivos y sólo **ese uno** nombra el conjunto; los
otros seis dicen «los 4 archivos de contenido» y nada más — **incluido `compose/patterns.md`, que es el
archivo que P224 escribió explícitamente «para que no haga falta un pase 74 en otra KB».** La copia
destinada a viajar es, justamente, la que no nombra su conjunto. Y sin el conjunto, de los **70** subconjuntos de 4 de los ocho archivos de contenido **exactamente
uno** da `229 / 389`: `agents/top.md` + `repos/foundations.md` + `verticals/solutions.md` +
`intel/market.md`, los cuatro de **INVENTARIO** (no los cuatro más grandes, y no los que la frase
«archivos de contenido» sugiere, que incluiría los de narrativa). Y la cifra de un solo archivo
(**111 líneas / 241 ocurrencias** en `agents/top.md`) reproduce **sin ambigüedad**, porque nombra su
archivo. 🔴 **La lección no es que la cifra estuviera mal: es que una cifra agregada sin su conjunto
le cuesta al siguiente pase una búsqueda de 70 subconjuntos para confirmarla — y este pase la hizo
antes de darse cuenta de que `agents/top.md` ya lo nombraba. Al lector externo, que llega por
`patterns.md` y no tiene el árbol, se la vuelve incomprobable.**

## 🔴 Lo que `measure.py` corrige del pase 74

| Cohorte | Inversiones | Lectura |
|---|---|---|
| **K-12 / instituciones** | 🔴 **7** (hasta **653×**: Skyward 1 ocurrencia contra Moodle 653) | el hueco real, y es la capa de SIS/*rostering* |
| **Superior / instituciones** | 🟢 **1**, y es Moodle 1,6× sobre Canvas | el perfil de atención de esta KB es **casi correcto** acá |

🔵 **El diagnóstico de P224 era cierto en sustancia y equivocado en causa.** La atención de esta base
no es inversamente proporcional a la base instalada *en general*: **es una KB de educación SUPERIOR a
la que se le midió la cobertura contra un denominador de K-12.** En su propio segmento comete **una**
inversión; en el ajeno, **siete**. ⚠️ **Y lo que no cambia es que el hueco de K-12 existe** —
PowerSchool **6**, Infinite Campus **4**, Skyward **1** ocurrencia en los cuatro archivos de
inventario—, sólo que ahora está **localizado en una capa** en vez de atribuido a un sesgo general.

## 🔁 La contaminación que este instrumento se encontró A SÍ MISMO (tendencia 593)

🔴 **`measure.py` sobre el árbol de trabajo da 11 inversiones en K-12; sobre `5dd2bcc` (`HEAD` del
pase 74) da 7.** No cambió la cobertura de la KB: **cambió el archivo que la mide.** La prosa con la
que este pase documenta el hueco de K-12 nombra PowerSchool, Skyward e Infinite Campus, y esas
menciones caen en `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` e
`intel/market.md` — **los cuatro archivos que la métrica cuenta.**

🔵 **La regla que sale, y es la generalización de P227 un paso más:** una métrica de cobertura leída
del mismo árbol que documenta el hueco **se contamina sola**, así que el **COMMIT es parte de la
invocación**. `--at COMMIT` existe por eso, y la cifra publicada siempre lo nombra. ⚠️ **Escribir
sobre un hueco lo cierra en la métrica sin cerrarlo en la realidad** — es la trampa que haría que el
pase 76 leyera «el hueco de K-12 mejoró» cuando lo único que pasó es que el pase 75 habló de él.

## ⚠️ La cota del dato de cuota, que este pase NO pudo levantar

**Ninguna fila lleva `share=`.** Los cinco orígenes de cuota volvieron a dar `EGRESS_BLOCKED` por
WebFetch en este pase (`listedtech.com`, `cubite.io`, `axiomflow.app`, `en.wikipedia.org`), igual que
en el 74 — así que se publica el **ORDEN** y no el porcentaje. 🔵 **Y la restricción está en el
constructor, no en la prosa:** `Row(share=…, provenance='EGRESS_BLOCKED')` **levanta `Refusal`**. Es
P224 paso 4 convertido en código, para que un pase futuro no pueda publicar un porcentaje que no
alcanzó.

🔴 **Lo que el canal de búsqueda sí devolvió, y se registra COMO canal de búsqueda, no como fuente:**
K-12 2026 Classroom **31 %** / Canvas **24 %** / Moodle **7 %** (desde 19 % en 2017); superior de
EE. UU. Canvas **1.814 de 3.400** instituciones y Classroom **6** (**0,2 %**). ⚠️ **El par que el pase
74 publicó (~39 % Classroom / ~19 % Canvas) no coincide con ninguno de los dos segmentos para ese par
de plataformas**; el **39 %** aparece en este canal atado a **Canvas en superior por conteo de
instituciones**. **No se afirma que el pase 74 copió mal: se afirma que la cifra, sin segmento ni
unidad, no es comprobable — que es exactamente lo que P228 ahora impide.**

## El vocabulario, cerrado a propósito

```python
SEGMENTS   = ('K-12', 'HigherEd')
UNITS      = ('institutions', 'users', 'installations')
PROVENANCE = ('SOURCE-VERIFIED', 'SEARCH-CHANNEL', 'EGRESS_BLOCKED')
```

🔴 **`SOURCE-VERIFIED` es un valor que el dato de cuota de esta KB nunca llevó**, en 75 pases. Queda
en el vocabulario para que el día que una fuente sea alcanzable, la cifra se distinga de una que vino
de un *snippet*.

## El control que importa (regla 2 de P126)

`test_coverage.py` sostiene, **en el mismo archivo**, la negativa y su contraejemplo: un *ranker*
**ciego a la cohorte** que, con las **mismas** filas, **sí** reproduce la «inversión» del pase 74.
🔵 **Si ese control dejara de encontrarla, el control se quedó ciego y la negativa ya no prueba
nada** — por eso se versiona junto al positivo y no aparte. Y el anclaje de `\b` también se controla
con los dos casos donde un `grep -oi` del pase falla: **`D2LX` no es `D2L`** y **`Cleverly` no es
`Clever`**.
