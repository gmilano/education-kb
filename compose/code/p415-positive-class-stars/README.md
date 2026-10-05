---
industry: education
region: Global
updated: 2026-10-05
---

# `P415` — la clase POSITIVA no es «una fila de datos de una tabla»

Artefactos del **pase 123 (2026-10-05, lectura `20:45Z`)**. Corre la **acción O** pre-registrada por el pase 122.

## Lo que la acción O pedía

El pase 122 dejó su suite verde agregando **cuatro** clases de exclusión (meta, umbral, `P403` cita-de-canal, `P404` rechazo). La acción O declaró que eso es **afinar-hasta-verde** y pidió lo inverso: definir la clase **POSITIVA** —la ★ que es el *dato de una fila que el estante recomienda*— y medir la propiedad «lleva banda y fecha» **sólo** sobre ella.

| cláusula pre-registrada | pedía | medido (v2) | veredicto |
|---|---|---|---|
| la clase positiva es **menor** que el universo del barrido | sí | 🟢 **10 contra 282** | **confirmada** |
| la propiedad se sostiene **sin ninguna** exclusión | sí | 🔴 **10 de 10 sin banda**, 9 de 10 sin fecha | **REFUTADA** |

## El hallazgo: mi primera versión midió la clase equivocada

`clase_positiva.py` (v1) definió la clase positiva como *celda de una fila de datos de una tabla*. Devolvió **80** miembros, **0 de 80** con banda, y declaró la propiedad falsa en el 100%.

🔴 **Estaba mal.** Leyendo las filas en vez del conteo, las dos primeras eran una tabla de **RECHAZO** (`candidata / cifra que trajo el canal / por que NO entra`) y una de **DENOMINADOR** (`Lo que devolvio el barrido global / n`). Sus cifras son **citas con otra forma**: no se les debe banda ni fecha porque no son filas recomendadas.

🆕 **`P415`** — es **`P410` un nivel más arriba**. `P410` dijo que el contexto léxico de una cifra es la etiqueta de su bloque y no su renglón; acá la **tabla** se identifica por la etiqueta de su bloque y por su fila de encabezado, **no por su forma**.

## La definición corregida

`clase_positiva_v2.py`: la fila positiva vive en una tabla cuyo **encabezado declara una columna de cesión** (`licenc|cesión|SPDX`) y cuyo bloque **no** está rotulado como rechazo o denominador.

| medida | v1 (equivocada) | v2 (corregida) |
|---|---|---|
| universo del barrido | 282 | 282 |
| clase positiva | 80 | 🟢 **10** |
| sin banda | 80 | **10 de 10** |
| sin fecha | 78 | **9 de 10** |

## Y la refutación corrige a su propia cláusula

La acción O decía que si hacía falta ≥1 exclusión, entonces *«el universo del barrido era el correcto»*. **No lo era:** sobrecontaba **28×**. Y la propiedad no falla un poco: falla en **10 de 10**. Las 4 exclusiones del pase 122 no se acercaban a una propiedad verdadera — **tapaban que la propiedad es falsa en toda la clase que importa**. 🟢 La deuda real es **arreglable**: 10 filas, no 284. Queda pre-registrada como **acción S**.

## Correr

```
python3 clase_positiva.py        # v1, se conserva porque su FALLA es el hallazgo
python3 clase_positiva_v2.py     # v2, la medicion que vale
```

Salidas del pase: `resultado.2026-10-05.txt` (v1) y `resultado-v2.2026-10-05.txt` (v2).
