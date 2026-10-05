# `p379-cession-dedup` — deduplicar CESIONES por (sha256, titular), no por repo

**Pase 117 del 2026-10-05.** Instrumento que `P377` pidió y `P379` hizo necesario.

## Qué mide

`P377` (pase 116) midió un linaje de 2 nodos **sin** archivo de licencia: forkear copia el `README`
y con él la afirmación, pero no copia el `LICENSE` porque no existe ⇒ el fork **manufactura una
segunda afirmación del mismo permiso inexistente**.

`P379` (este pase) midió el caso **espejo** y el resultado no es el simétrico:
`krishna16-origin/ai-tutor` → `maxew6/ai-tutor-project` tienen `LICENSE` de **1.073 B** con el
**mismo `sha256:de8107bf9312862c`**. El fork copió la cesión al byte y con ella el **titular**: el
`LICENSE` del fork otorga en nombre de `krishna16-origin`.

**Consecuencia, y el signo del riesgo está invertido respecto de `P377`:** ahí el doble conteo
inflaba *afirmaciones* y era detectable porque el denominador de cesiones estaba en cero. Acá infla
**cesiones verificadas** — los dos nodos **pasan** el control «¿hay archivo de licencia permisiva
leído del payload?» con 200 y texto canónico. El doble conteo que *parece* seguro es más peligroso
que el que parece roto.

## La clave

> La unidad de deduplicación de una cesión es el par (`sha256` del texto de licencia, **titular
> nombrado**). No el repo, no el `full_name`, no la etiqueta SPDX.

Dos filas con el mismo par son **una** cesión, con **un** titular a quien reclamar.

## Cómo correrlo

El dato ya está en el estante: esta base viene anotando `sha256` de licencia por fila. El barrido es
sobre los `.md`, no sobre la red.

1. Extraer de `agents/top.md`, `repos/foundations.md` y `verticals/solutions.md` las ternas
   *(repo, `sha256`, titular)* de las filas que las traigan.
2. Agrupar por `sha256`. Todo grupo de tamaño > 1 es un **candidato a colisión**.
3. Para cada grupo, comparar el titular. Dos casos distintos:
   - **mismo `sha256` + mismo titular** ⇒ **una** cesión duplicada (caso `P379`): colapsar a 1.
   - **mismo `sha256` + titular distinto** ⇒ **no** es colisión: es el mismo texto canónico con
     holders distintos, que son cesiones independientes. Precedente medido: `i-educar` y `enem-api`
     (pase 115) comparten el `sha256` de GPL-2.0 y son dos cesiones reales.
4. Reportar: nº de filas, nº de `sha256` distintos, nº de pares (`sha256`, titular) distintos.
   **El tercero es el conteo honesto de cesiones.**

## Por qué el paso 3 no es opcional

Un deduplicador que agrupe **sólo** por `sha256` colapsa `i-educar` + `enem-api` —dos cesiones
GPL-2.0 reales de titulares distintos— y **sub**-cuenta. Agrupar sólo por titular colapsa repos
distintos del mismo dueño y también sub-cuenta. **Es el par o nada.**

## Estado

⚠️ **No corrido sobre el estante completo todavía.** Pre-registrado como acción **B** del pase 117:
hipótesis ≥1 par en colisión además de `krishna16-origin`/`maxew6`; **refutada si** sobre ≥30 filas
con `sha256` legible las colisiones son 0 ⇒ `P379` sería un caso aislado y no un sesgo del conteo.
