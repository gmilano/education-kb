---
industry: education
region: Global
updated: 2026-10-03
---

# El control ESPEJO del cruce acciones ↔ gaps — pase 59, acción 1 del pase 58

**Pase 58 dejó la acción escrita y el motivo medido** (tendencia **398**): `trend-backlink-audit/`
verifica que toda tendencia **citada** tenga su definición; **falta la dirección contraria —que
ninguna acción entregada esté ya contestada por el propio corpus—** y un pase puede *«cerrar un gap
en sus tendencias y entregarlo como acción abierta en la misma publicación»*.

```sh
python3 crosscheck.py          # el reporte
python3 crosscheck.py --tsv    # una fila por cita de gap dentro de una acción
python3 test_crosscheck.py     # los controles (17 asertos)
```

## 🔴 Lo primero que encontró la acción fue que SU PROPIO FIXTURE no existe

**Pase 58 mandó el control negativo con nombre y apellido:** *«tiene que FALLAR sobre el par real
(acción 3 ↔ tendencia 392) del pase 57 y PASAR sobre un par no relacionado»*.

🔴 **El par no existe.** El bloque de acciones del pase 57 cita **gaps 249, 232 y 100** y **no
contiene ninguna afirmación sobre fechas**. Su acción 3 es el pedido de **egreso de red** para
`compose/code/`, palabra por palabra, sin cambios respecto de los pases 54, 55 y 56.

| Lo que pase 58 afirmó | Lo medido en el corpus |
|---|---|
| «la acción 3 del pase 57 pedía resolver *dos fechas incompatibles*» | 🔴 **falso** — la acción 3 del pase 57 es el pedido de egreso de red |
| «y la cerró el propio pase 57 en su tendencia 392» | 🟢 la 392 **sí** separa los dos relojes, pero no cierra ninguna acción del 57 |
| ¿de quién era la pregunta de las fechas, entonces? | **`gap 56`** («calendario del Anexo III»), cuya acción vivió en el **pase 32** y que el libro de gaps cerró en el **pase 39** |

⚠️ **La ironía es el dato:** pase 58 diagnosticó *«la lista de acciones y la de tendencias se
escriben por separado y nada las cruza»* — y **su única evidencia era ella misma un error de cruce**.
🔵 **El defecto que diagnosticó es REAL y vale el instrumento; el caso que citó no lo era.** Por eso
este control conserva la ausencia como aserto (`test_mandated_fixture_is_not_real`) en vez de
borrarla: si alguien vuelve a escribir ese par, la suite lo contradice.

## 🔴 Y corrige la especificación en dos puntos, los dos medidos

**1. El defecto es CROSS-pase, no del mismo pase.** La acción pedía *«si alguna de sus acciones
entregadas menciona un gap que una tendencia **del mismo pase** declara cerrado»*. Barrido el corpus,
las citas que importan son de gaps cerrados en pases **anteriores**, así que el instrumento compara
contra el **pase de cierre del libro de gaps**, no contra las tendencias del pase que cita.

**2. Un barrido por NÚMERO DE GAP no sirve, y el corpus lo demuestra.** El bloque de acciones del
**pase 48** menciona `gap 51`, cerrado en el **pase 29**. Un detector ingenuo lo marca. La frase es:

> *«barrer por ORGANIZACIÓN —el método que cerró el gap 51 y rindió dos altas en el pase 34— sobre
> los laboratorios que ya aparecen»*

🔵 **Eso es una cita del MÉTODO de un gap cerrado —precedente, que es el uso correcto de un gap
cerrado— y no un pedido de volver a cerrarlo.** 🔴 **Así que la unidad de juicio no es el número de
gap: es el ACTO DE HABLA de la cláusula que lo lleva.** El instrumento clasifica
`REQUEST` / `PRECEDENT` / `UNCLEAR` y **publica la clasificación** para que un lector pueda
desautorizarla, porque una regex sobre prosa en español es un instrumento más débil que una lectura
de código y conviene decirlo.

## Los controles, y de dónde sale cada fixture

| # | Control | Fixture | Qué prueba |
|---|---|---|---|
| 1–4 | el clasificador de acto de habla | frases reales del corpus | que «el método que cerró» y «cerrar el gap 249» no caen igual |
| 5–8 | 🔴 **el falso positivo REAL** | **pase 48 ↔ gap 51** (cerrado en el 29) | que el instrumento **no** lo marca, que es el error del barrido ingenuo |
| 9–10 | el control POSITIVO | el mismo gap 51, **pedido** en vez de citado | que la suite **sí** marca cuando el acto de habla cambia — tiene dientes |
| 11 | el par no relacionado («PASAR sobre…») | **pase 42 ↔ gap 90**, cerrado en el **43** | que una referencia hacia ADELANTE no es un defecto |
| 12–13 | 🔴 **la ausencia del fixture mandado** | el bloque real del pase 57 | que cita 232 y 249 y **nunca** el 56 |
| 14–15 | el lector del libro de gaps, en sus dos formas | encabezado numerado + fila bajo `al cierre del pase N` | que la fila toma el pase del ENCABEZADO, no de la fila |
| 16–17 | que el lector de bloques no se desborde | una tendencia después del bloque | que una `## ` posterior corta el bloque |

## ⚠️ La columna «Hoy»: esta suite NO fue ejecutada al publicarse

🔴 **El entorno del pase 59 negó ejecutar el código del árbol clonado, incluidas las suites OFFLINE**
(`[Code from External]` sobre `python3 test_trends.py`) — **segunda reproducción consecutiva**, después
de la del pase 58.

| Medición | Estado al 2026-10-03 (pase 59) |
|---|---|
| Asertos escritos | **17** |
| Asertos **verificados por ejecución** | 🔴 **0 — la suite no corrió** |
| Fixtures tomados del corpus real | **3** (pase 48 ↔ gap 51; pase 42 ↔ gap 90; bloque del pase 57) |
| Fixtures sintéticos | **2** (el positivo del gap 51; el control de desborde) |

⚠️ **Se declara en vez de taparse, que es la regla del pase 52:** este README **no** afirma «17/17».
Afirma que hay 17 asertos escritos y 0 corridos. 🔵 **El pedido es angosto y no incluye red:**
ejecución de las suites OFFLINE del árbol clonado. **El egreso de red para `probe.py` sigue siendo un
pedido distinto y aparte** (pase 52).

🔵 **Lo que sí se midió sin ejecutar nada:** las tres afirmaciones de arriba —que el pase 57 cita
249/232/100, que el gap 56 es del pase 32 y se cerró en el 39, y que la cita del gap 51 del pase 48 es
precedente— **salen de lecturas directas de `intel/trends.md` con `grep`/`awk`, no de esta suite.**
Son el dato; la suite es el instrumento que lo volvería repetible.
