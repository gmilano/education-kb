---
industry: education
region: Global
updated: 2026-10-04
---

# P239 / P240 — integridad de tablas y cobertura regional

**Pase 78 del 2026-10-03.** Instrumento nacido de **dos defectos reales encontrados en el archivo
publicado**, no de una hipótesis.

## Qué mide

| Eje | Defecto | Por qué importa |
|---|---|---|
| **P239** | Fila de datos cuyo bloque de pipes **no tiene separadora (`\|---\|`) arriba** | El compilador lee la **primera fila de datos como encabezado**: una fila real se pierde y se crea una entidad con nombre de dato |
| **P240** | Tabla con **columna de región** a la que le **falta** una de las cinco del vocabulario cerrado | Un barrido que publica 3 de 4 regiones **no se distingue, leído desde afuera, de uno que midió 4 y encontró 3** |

## Los dos defectos que lo originaron

| Sitio | Qué pasaba | Reparación |
|---|---|---|
| `verticals/solutions.md:1501` | Un **comentario HTML** (`<!-- pase 39 ... -->`) entre la última fila y las siguientes **partía la tabla**: **14 filas** quedaban sin encabezado ni separadora | Re-emitir encabezado + separadora tras el comentario |
| `intel/market.md:582` | La tabla de cuatro regiones publicaba **tres**: la fila **LATAM** se había **partido en dos** y sus mitades vivían en `:894` (`` `) \| ``) y `:908`, 300 líneas más abajo, dentro de la sección de **APAC** | Reunir las mitades y restituir la fila a su tabla |

🔴 **El segundo es el más caro de los dos**, y no por el tamaño: la fila perdida era **la de LATAM**.
Una tabla regional a la que le falta una región **se lee como cobertura completa** — es exactamente
el daño que el encuadre de esta KB pide evitar.

## Uso

```sh
python3 check_tables.py intel/market.md verticals/solutions.md   # TSV a stdout
python3 check_tables.py */*.md > result.$(date +%F).tsv          # salida 1 si hay hallazgos
python3 -m unittest test_check_tables -v                         # 23 tests
```

### Tablas legítimamente parciales

Una tabla puede cubrir menos de cuatro regiones a propósito (p. ej. «las dos regiones que legislan
sobre la nota»). Eso **se declara**, no se deja implícito:

```markdown
<!-- p240-scope: North America, EMEA -->
| Región | Instrumento |
```

Sin marcador la tabla **se reclama**, que es el punto del eje.

## 🔴 Las tres versiones de este instrumento, porque el instrumento falló antes que el archivo

Este linter produjo **siete falsos positivos** sobre el archivo publicado antes de medir bien. Se
registran porque el patrón se repite y es transferible:

| Versión | Falsos positivos | Causa | Arreglo |
|---|---|---|---|
| v1 | 3 | `\| 🔴 **LATAM** \|` no matcheaba por el **emoji**; `APAC (Vietnam)` por el **paréntesis**; `**APAC / LATAM**` es **una celda con dos regiones** | Normalizar y permitir celda combinada |
| v2 | 4 | Leía como región cualquier celda que **contuviera** el nombre de una: `86 % NA / 92 % LATAM / 66 % APAC` es una celda de **cifras**; `Ministerio..., APAC / LATAM / África` es una de **perfil de cliente** | **Match estricto**: la celda cuenta sólo si **no queda nada más que regiones** |
| v3 | 0 | — | Baseline limpio (`result.2026-10-03.tsv`, salida 0) |

🔵 **La lección de método, que vale más que el linter:** el eje P240 **no se podía afirmar hasta que
el instrumento dejó de mentir**. Las siete tablas que la v1 y la v2 reclamaron estaban **bien**; si
se hubieran «arreglado» para callar al linter, el pase habría **dañado siete tablas correctas** para
tapar un defecto de medición. Cada falso positivo quedó como test de regresión.

## Resultado

`result.2026-10-03.tsv` — **0 hallazgos** sobre los 8 archivos de la KB, tras las cuatro
resoluciones del pase 78: 2 reparaciones estructurales, 1 deriva de vocabulario (`Asia Pacific` →
`APAC` en `repos/trending.md`, que es **variante y por lo tanto balde propio**), 3 alcances
declarados y 1 **fila de hueco** (APAC en `intel/trends.md`).
