---
industry: education
region: Global
updated: 2026-10-05
---

# `P429` — una cesión no se lee de quien RECOMIENDA la pieza

Artefactos del **pase 125 (2026-10-05, lectura `22:50Z`)**.

## El defecto, medido 4 de 4 contra una sola fuente

El canal de plataformas de este estante (`open source platform education ...`) devuelve *listicles* del tipo **«Best Open Source LMS 2026»**. Traen una **columna de licencia**, y esa columna es justo el dato que una propuesta copia. El pase 125 la midió entera contra el sidebar de GitHub:

| plataforma | lo que el listicle afirma | primera mano (`22:50Z`) | veredicto / riesgo |
|---|---|---|---|
| `sakaiproject/sakai` | ECL-2.0, «más permisiva para redistribución académica que GPL» | **ECL-2.0** · 1.2k ★ | 🟢 `ACIERTO` / `COSMETICA` |
| `chamilo/chamilo-lms` | «PHP, GPL v3» | **GPL-3.0** · 1.0k ★ | 🟢 `ACIERTO` / `COSMETICA` |
| `formalms/formalms` | **«Apache 2.0 — la licencia más permisiva de esta comparación»** | 🔴 **NINGUNA.** Sin campo de licencia; descripción = *«forma.lms mirror repository»* | 🔴 `REFUTADA` / **`BLOQUEANTE`** |
| `openedx/edx-platform` | «free, open-source», **sin nombrar la cesión**; recomendada para escala empresarial | **AGPL-3.0** · 8.2k ★ | 🔴 `OMITIDA` / **`HOSPEDAJE`** |

**2 aciertos de 4.** 🔴 **Pero el reparto NO es aleatorio, y eso es el hallazgo: las 2 que acierta son las 2 donde la licencia no cambia la entrega, y las 2 que falla son las 2 donde sí la cambia.**

- `formalms` se presenta como **la más permisiva de la comparación** y no cede **nada**: un repo sin archivo de licencia es *todos los derechos reservados*. No es «licencia desconocida», es **no usable**.
- `openedx/edx-platform` es la recomendación para **escala empresarial** y es **AGPL-3.0**, o sea la cláusula de **uso en red** — exactamente la que decide si un despliegue hospedado por Globant es legal.

🔵 **Hermano de `P419` por el otro lado.** `P419`: la identidad de un copyleft no se lee de las licencias que **cita**. `P429`: tampoco de quien lo **recomienda**. En los dos casos el eje corrompido es el mismo —el uso en red— y es el único que decide un despliegue hospedado.

🔵 **Y re-confirma un negativo a 12 pases de distancia:** el pase 113 midió `formalms/formalms` y lo descartó (`LICENSE` y `LICENSE.txt` ambos 404, sidebar sin licencia). El pase 125 vuelve a medirlo y da **lo mismo** ⇒ es un negativo **estable**, no una lectura transitoria.

## La regla

Una afirmación de cesión de segunda mano **no se publica como dato**. Entra como **candidata** y se clasifica por el **riesgo de entrega** de su discrepancia, que no es el tamaño del error sino **qué decisión cambia**:

| riesgo | qué cambia |
|---|---|
| `BLOQUEANTE` | si la pieza **se puede usar** (sin cesión, o no-OSI) |
| `HOSPEDAJE` | si el **despliegue hospedado** es legal (AGPL ↔ otra familia) |
| `COSMETICA` | ninguna de las dos |

## 🔴 `P430` — un verde no prueba el mecanismo, prueba que ningún caso lo discriminó

La **v1** de este instrumento escribía el chequeo de uso en red como `cp in RED` con `cp` **ya convertida a clase**: `'RED' in {'AGPL-3.0', …}` es **siempre `False`**, así que la rama **nunca disparaba por el lado medido**.

🔴 **Y su suite pasó `12/12` con el defecto adentro**, porque una rama posterior devolvía el **veredicto correcto por el motivo equivocado**. El defecto era invisible en `(veredicto, riesgo)` y visible **sólo en el motivo**.

🟢 **La suite endurecida** exige que toda discrepancia de riesgo `HOSPEDAJE` **nombre** el uso en red, y con eso **rechaza 2 de 2** de los casos de la v1 (`control` en `resultado.2026-10-05.txt`). La corrección es comparar **clase contra clase**.

🔵 Es `P417` aplicado un nivel más abajo: no basta que la referencia sea externa al instrumento, **la aserción tiene que tocar el mecanismo**. Una suite que sólo mira veredictos certifica la salida y no el camino.

## Suite y corrida

- `test_audit.py` — **12/12 🟢**. 4 fixtures **reales** (las 4 filas de arriba) + 3 casos del eje de uso en red + 3 discrepancias cosméticas + 2 de omisión.
- `resultado.2026-10-05.txt` — la corrida sobre las 4 afirmaciones reales, más el **control de `P430`** contra la v1.

## Uso

```bash
python3 audit_claim.py Apache-2.0 NINGUNA   # REFUTADA  BLOQUEANTE
python3 audit_claim.py - AGPL-3.0           # OMITIDA   HOSPEDAJE
python3 test_audit.py
```
