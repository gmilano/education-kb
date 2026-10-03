# P234 — cerrar la tabla de «repo muerto ⇒ licencia no verificada»

**Pase 77 del 2026-10-03.** Instrumento: `sweep_dead.sh`. Salida ejecutada: `result.2026-10-03.tsv`.

## Qué se midió y por qué

`repos/trending.md:3450` publica cinco filas con la licencia en `— (no verificada: repo muerto)` y,
debajo, una **nota de honestidad** que explica la decisión:

> «en los cinco repos muertos **no se verificó el archivo**. No hacía falta y habría sido gasto: una
> licencia permisiva sobre un repo sin commits en una década no cambia la decisión.»

El pase 76 (**P231**) refutó esa nota en **una** de las cinco filas: `jdolny/OneRoster.NET`, archivada
como no verificada, es **MIT** y trae `v1p2` — el único permisivo con el spec vigente de toda su capa.
Este instrumento mide **las cinco**, para saber si el pase 76 encontró una excepción o un patrón.

## Resultado

**5 de 5 son permisivas. Cero copyleft, cero sin archivo.**

| Pieza | Licencia (payload) | Estado antes de este pase |
|---|---|---|
| `EASOL/edfi-to-oneroster` | **Apache-2.0** | 🆕 medida acá |
| `Transcordia/jupiter` | **MIT** (titular `Transcordia`, 2014) | 🆕 medida acá |
| `jdolny/OneRoster.NET` | **MIT** (titular `theopenem`) | pase 76, reconfirmada |
| `bgwdotdev/go-oneroster` | **MIT** (titular `fffnite`) | pase 76, reconfirmada |
| `gotranseo/oneroster` | **Apache-2.0** | pase 76, reconfirmada |

**La nota de honestidad está refutada en las cinco filas, no en una.** Y su razonamiento está dado
vuelta: la columna de muertos de esta KB **no es un cementerio, es una reserva de código
bifurcable** — es la clase donde *más* paga medir la licencia, porque es lo único que queda cuando no
hay quien atienda un *issue*. **Costo total del cierre: cinco peticiones HTTP.**

## Correcciones que este instrumento pagó en su propia construcción

1. 🔴 **Clasificador propio en vez del compartido (→ `P237`).** La primera versión definía su propio
   `classify()` con un `grep` de `affero` sobre el **cuerpo**, que es exactamente el defecto **P171**
   que esta base arregló hace cinco instrumentos. Reportó `LearningLocker/learninglocker` (**GPL-3.0**)
   como **AGPL-3.0**. Ahora **importa** `../lib/license_family.sh`, que está testeado.
2. 🔴 **Titular de boilerplate (→ `P184`).** La primera versión tomaba cualquier línea que empezara
   con `copyright` y así imprimía texto de la **licencia Apache** —*«copyright notice that is included
   in or attached to the work»*— como si fuera un titular. El archivo de licencia responde el titular
   **sólo** para MIT/BSD/ISC. Medido acá: de las dos filas Apache-2.0, `EASOL` **no trae ninguna línea
   de copyright** y `gotranseo` trae **la plantilla sin llenar** (`Copyright [yyyy] [name of copyright
   owner]`).

## Cómo correrlo

```sh
./sweep_dead.sh EASOL/edfi-to-oneroster Transcordia/jupiter jdolny/OneRoster.NET \
                bgwdotdev/go-oneroster gotranseo/oneroster
```
