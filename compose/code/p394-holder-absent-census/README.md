---
industry: education
region: Global
updated: 2026-10-05
---

# `p394-holder-absent-census` — cuántas filas con huella de licencia tienen el titular AUSENTE

**Pase 120 del 2026-10-05.** Corre la **acción D** que el pase 118 pre-registró, para saber si la
compuerta de `P386` («con titular ausente el fingerprint vale 0 bits de procedencia ⇒ abstenerse»)
cubre un caso raro o una fracción medible del estante.

## Criterio, dicho ANTES de contar

- **Universo** = **filas de tabla** markdown con una huella (≥12 hex) **y** mención de licencia. Una
  línea de prosa **no** es una fila.
- **AUSENTE** = la fila lleva marcador explícito (`NOT-APPLICABLE`, «sin titular», «titular
  ausente») — la definición que la acción pre-registró.
- **MUDO** = la fila no dice nada del titular. Se cuenta **aparte**, porque es un negativo **DÉBIL**:
  la ausencia de la PALABRA no es la ausencia del TITULAR (clase de `P160`).

## Lo medido

| Clase de titular | Filas | Fracción |
|---|---|---|
| 🔴 **AUSENTE explícito** | **15** | 8,1 % |
| 🟢 **PRESENTE** | 46 | 24,7 % |
| ⚠️ **MUDO** | 🔴 **125** | 🔴 **67,2 %** |
| **Universo** | **186** | 100 % |

🟢 **Cláusula de la acción D (≥5 confirma, ≤2 refuta): CONFIRMADA con 15.** Y **8 de las 15** llevan
además bytes de boilerplate prístino conocido ⇒ en poco más de la mitad el titular falta **por
construcción de la licencia**, no por omisión de quien escribió la fila.

## El hallazgo (`P394`): la pregunta de la acción cubre un tercio del estante

🔴 **«Ausente vs. presente» tiene respuesta para 61 de 186 filas (32,8 %). Las otras 125 son MUDAS y
la compuerta de `P386` no tiene rama para ellas.** Las dos salidas disponibles son malas:

- MUDO como **ausente** ⇒ la compuerta se abstiene en **140/186** (75,3 %) y deja de ser compuerta:
  pasa a ser el comportamiento por defecto.
- MUDO como **presente** ⇒ funde proyectos ajenos exactamente como `P386` advirtió.

🟢 **La corrección es una tercera rama:** `ausente ⇒ abstenerse` · `presente ⇒ linaje` ·
**`mudo ⇒ MEDIR el archivo por ruta, no inferir`**. 🔵 **Y es el único lugar donde la tabla
`PRISTINE_SIZES` de `p386-pristine-dedup-gate/` recupera trabajo real** (ver `P396`: hoy su
disyunto está muerto): en la rama muda el titular no decide, y un tamaño de boilerplate conocido es
evidencia **a favor** de que el titular no vive en el texto.

## Defecto propio, encontrado por la suite y medido antes de publicar

🔴 **La primera versión buscaba los nombres de licencia sin frontera de palabra, así que `MIT`
casaba dentro de «com-MIT»** y toda fila que nombrara un *commit* entraba al universo. 🟢 **Arreglado
con `\b`, y el radio del daño se midió en vez de suponerse: universo de 188 → **186** (2 filas de
más), **las 2 en la clase MUDA**, y AUSENTE (15) y PRESENTE (46) sin moverse ⇒ la cláusula da el
mismo veredicto con el instrumento roto y con el arreglado.** Se escribe porque es lo que vuelve la
cifra defendible, no porque el defecto fuera inofensivo.

## Uso

```
python3 holder_census.py agents/top.md agents/trending.md repos/foundations.md \
        repos/trending.md verticals/solutions.md intel/market.md intel/trends.md \
        compose/patterns.md            # TSV: las 3 clases + cada fila ausente con su ubicacion
python3 test_holder_census.py          # 19/19
```

⚠️ **Invocación de las cifras publicadas arriba (regla de `P107`): el censo arreglado sobre los 8
archivos tal como estaban en `HEAD`, o sea SIN las filas que este pase agrega.** Corrido después de
escribirlas da **23 / 46 / 139** sobre **208**, porque el pase agrega 8 filas de titular ausente
explícito (las 2 altas prístinas y las tablas de corrección).

## Estado

🟢 **Implementado, corrido sobre los 8 archivos, suite de 19 casos** — incluidos los controles de la
cláusula pre-registrada en sus dos extremos (2 ausentes ⇒ refutaría; 5 ⇒ confirmaría) y el caso que
destapó el defecto de `MIT`/«commit».
