---
industry: education
region: Global
updated: 2026-10-04
---

# P250 — familia de licencia y USO COMERCIAL son dos preguntas (pase 82 del 2026-10-04)

`dssg/student-early-warning` estuvo en `agents/top.md` —tabla cuyo propósito declarado es
*«MIT / Apache 2.0 / BSD, las que Globant puede usar de base»*— con una licencia académica de la
**Universidad de Chicago** que excluye explícitamente *«any service or part of selling a service that
uses the Program»*. La base lo tenía marcado **en prosa desde el pase 51**. 🔴 **Sus instrumentos
devolvían `UNKNOWN`, y `UNKNOWN` es indistinguible de «el uso comercial está PROHIBIDO» — que son
respuestas opuestas a la única pregunta para la que existe esta KB.**

## La regla

> **P250.** *Familia de licencia* y *uso comercial* son dos preguntas y se contestan en dos columnas.
> Una familia OSI identificada permite uso comercial **por definición** y no se somete a ningún
> token. El detector de restricciones corre **sólo** cuando no hay familia que lo proteja.

## Lo medido sobre las 69 filas recomendables

| Uso comercial | n |
|---|---|
| 🟢 `OK` | **42** |
| 🔴 `PROHIBIDO` | **1** — `dssg/student-early-warning` |
| ⚠️ `SIN-DETERMINAR` | **26** (23 sin archivo de licencia + 3 inalcanzables) |

Familias sobre las 43 licenciadas: **MIT 30 · Apache-2.0 3 · AGPL-3.0 3 · CC0-1.0 2 · Unlicense 1 ·
0BSD 1 · BSD 1 · CC-BY-SA-4.0 1 · NONCOMMERCIAL-NOT-OSI 1** → 🟢 **38 de 43 (88,4 %) permisivas.**

## 🔴 El instrumento falló su primera prueba real, y el fallo está versionado

`result-falsepositive.NEGATIVE-CONTROL-2026-10-04.tsv` es la salida del **primer corte**, que marcó
`PROHIBIDO` a **cuatro** filas que no lo son:

| Fila | Primer corte | 🟢 Correcto | Causa |
|---|---|---|---|
| `FWU-DE/ais-chat` | 🔴 PROHIBIDO | 🟢 **AGPL-3.0 / OK** | El cuerpo de AGPL-3.0 dice *«allowed only occasionally and **noncommercially**»* — **sección 6, línea 259** del payload |
| `csmediapro/moodle-mcp-server` | 🔴 PROHIBIDO | 🟢 **AGPL-3.0 / OK** | ídem |
| `helixnow/deep-student` | 🔴 PROHIBIDO | 🟢 **AGPL-3.0 / OK** | ídem |
| `FWU-DE/mem-mcp` | 🔴 `NONCOMMERCIAL-NOT-OSI` | 🟢 **Unlicense / OK** | The Unlicense **concede** con *«for any purpose, **commercial or non-commercial**»* — la licencia más permisiva que existe, marcada por el token con el que otorga el permiso |

🔴 **Es la falta de solidez exacta que `P171` nombra: el cuerpo de una licencia contiene el
vocabulario de otras condiciones, así que un token sobre el cuerpo no se puede creer.**
⚠️ **Y los controles negativos del primer corte no lo atraparon porque usaban *fixtures* truncados —
bloques de título sin sección 6 y sin la frase de concesión. Un *fixture* lo bastante corto para ser
cómodo es lo bastante corto para no ver el defecto.** 🟢 **La suite de `lib/` ahora trae las dos
entradas completas que producían el falso positivo, y pasa de 18/18 a 41/41.**

## Correr

```sh
# una fila
sh sweep_commercial.sh r-huijts/canvas-mcp
# el catálogo, en paralelo
cat slugs.input.txt | xargs -P 8 -I{} sh ./sweep_commercial.sh {}
# la librería compartida que hace la clasificación
sh ../lib/test_license_family.sh     # 50/50 (41/41 cuando se escribio este README; P299 sumo 9)
```

| Archivo | Qué es |
|---|---|
| `sweep_commercial.sh` | Barrido de 6 columnas. 🟢 **Primer barrido del catálogo que consume `lib/license_family.sh`** en vez de traer su propio clasificador — la deuda que `P237` nombró |
| `slugs.input.txt` | Los **69** `org/repo` distintos de la tabla principal de `agents/top.md` |
| `result.2026-10-04.tsv` | El resultado corregido |
| `result-falsepositive.NEGATIVE-CONTROL-2026-10-04.tsv` | 🔴 El primer corte, **conservado como control negativo** |

## Cota honesta

⚠️ **26 de 69 salen `SIN-DETERMINAR`, y no es un fallo del instrumento:** 23 no tienen archivo de
licencia en 14 nombres probados (**ausencia medida**) y 3 no son alcanzables. 🔵 **«Sin licencia» no
es «permisivo por omisión»: es una pregunta abierta para el cliente.**

⚠️ **Y las cuatro familias que este pase agregó al clasificador no son descubrimientos:** las cuatro
estaban resueltas **en prosa** desde los pases 51 y 64. 🔵 **Es `P237` otra vez — la corrección vivía
en el texto y nunca llegó al código.**
