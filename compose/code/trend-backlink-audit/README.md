---
industry: education
region: Global
updated: 2026-10-02
---

# El control de *backlink* aplicado a las TENDENCIAS — pase 49, acción 2

**Pase 48 dejó la acción escrita y el motivo medido:** ese pase buscó la *tendencia 210* con un
`grep` de encabezados, **no la encontró, y estuvo a punto de publicar un «backlink colgado» que no
existía.** El falso hallazgo lo atrapó el control positivo, no el instrumento. La cita es lo que un
cliente sigue, así que vale un instrumento.

```sh
python3 audit_trends.py          # el reporte
python3 audit_trends.py --tsv    # una fila por cita
python3 test_trends.py           # 22/22, sin red
```

## 🟢 El resultado: CERO citas colgadas, y las tendencias 1–219 sin un solo hueco

| Medición | Valor |
|---|---|
| Tendencias **definidas** en `intel/trends.md` | **219** (máximo 219) |
| Números **sin definición** por debajo del máximo | **0** |
| Citas de tendencia en los ocho archivos | **755** al correr la acción 2; **786** al cierre del pase |
| Citas **colgadas** | 🟢 **0** |

⚠️ **Dos cifras y las dos son correctas, que es el punto del gap 101:** **755** es la medición al
correr la acción 2, y **786** la del cierre, porque **el propio pase 49 escribió secciones que citan
tendencias**. 🔵 **Treinta y una citas de deriva en un pase es la demostración más corta de por qué una
cifra necesita decir CUÁNDO se midió además de CON QUÉ.** El reparto de abajo es el de la acción 2.

**Reparto de las citas por archivo:** `intel/trends.md` **375**, `agents/trending.md` **96**,
`agents/top.md` **88**, `intel/market.md` **63**, `compose/patterns.md` **47**,
`repos/foundations.md` **39**, `repos/trending.md` **34**, `verticals/solutions.md` **13**.

## 🔴 Lo primero que encontró el instrumento fue un error del instrumento (otra vez)

**La primera corrida reportó 700 citas. La real era 755: faltaban 55, el 7,3 %.**
El separador del patrón era `\s*(?:—|,|\sy\s|\se\s)?\s*`, y **`\sy\s` no puede disparar nunca**
porque el `\s*` anterior ya se comió el espacio. Así, `«las tendencias 213, 216 y 217»` devolvía
**`[213, 216]`** y se perdía la tercera.

🔵 **Es exactamente la misma forma del defecto que costó el 44 % del inventario de cifras en el pase
47** (`\b` después de un carácter que no es de palabra). **Un extractor con pérdida no falla
ruidosamente: devuelve un número más chico y más confiado.** Lo atrapó el control
`"una lista de citas parsea"`, escrito antes de mirar el resultado.

## 🔴 Y corrige el diagnóstico del pase 48: las formas son TRES, no dos

La acción decía *«resolverlo contra las dos formas en que esta base numera tendencias (encabezado y
fila)»*. **Son tres, y la tercera es la que sostiene las tendencias 1–196:**

| # | Forma | Ejemplo | Cuántas define |
|---|---|---|---|
| 1 | **encabezado numerado** | `## 57. La capa de analítica del LMS…` | **196** |
| 2 | **encabezado de RANGO** | `## Las tendencias 197–210, del pase 47` | **33** (157–166, 197–219) |
| 3 | **fila de tabla** | `\| **217** \| Una cifra condicional \| …` | **23** — *y ninguna que el rango no declare ya* |

🔴 **Por qué el `grep` del pase 48 falló, con más precisión que la que el pase 48 se dio a sí mismo:**
no es que *«la 210 vive en una fila y no en un `## `»* — **la 210 vive en las dos**, y además es el
**extremo** de `## Las tendencias 197–210`. El defecto real es que **un encabezado de rango nombra
sólo sus dos extremos**, así que las **doce** tendencias intermedias (198–209) no aparecen en
**ningún** texto de encabezado. El pase 48 sacó la acción correcta del motivo equivocado.

## ⚠️ La colisión de espacios de nombres, que es lo que obliga a leer el contexto

**Los gaps usan la MISMA forma `| **N** |` que las tendencias**, y comparten el espacio de los
enteros: `| **103** |` es un **gap**, no una tendencia. Una fila cuenta como definición de tendencia
**sólo si el encabezado anterior más cercano es de tendencias**. Acreditar filas de gap como
tendencias silenciaría citas colgadas reales, que es justo lo que el instrumento busca.
Hay un control para eso (`"una fila de GAP no se cuenta como definición de tendencia"`).

## El control positivo, que es lo que vuelve publicable un CERO

🔵 **Un cero es el único resultado que hay que ganarse:** un instrumento que no puede encontrar un
defecto reporta cero por el mismo motivo que una base correcta. Se inyectaron
`«la tendencia 777»` y `«las tendencias 801-803»` en `compose/patterns.md`:
**el instrumento marcó las cuatro** (755 → 759 citas, 4 colgadas), y el archivo se revirtió.

## ⚠️ Por qué este README no está en el conjunto auditado

Este archivo **nombra a propósito** `la tendencia 777` y `las tendencias 801-803` para documentar el
control positivo, y esas dos cadenas son **indistinguibles de una cita real** para el extractor.
`KB_FILES` cubre los **ocho** archivos de la base y **no** `compose/code/**`, así que la
documentación del control no contamina la medición.

🔴 **Y el caso se dio de verdad en este mismo pase:** la prosa de `intel/trends.md` que
describía el control nombraba los números inyectados, **el instrumento la leyó como cuatro citas
colgadas, y tenía razón** —la cadena publicada era exactamente la de una cita a algo que no existe.
Se reescribió la prosa (*«dos citas a números inexistentes, uno simple y un rango de tres»*) en vez
de ensordecer el instrumento. 🔵 **La regla que queda: si hay que elegir entre una prosa más
vistosa y un instrumento que no miente, gana el instrumento.**
