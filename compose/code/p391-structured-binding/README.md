---
industry: education
region: Global
updated: 2026-10-05
---

# `p391-structured-binding` — el binding `huella → repo` leído de la CELDA, no de la LÍNEA

**Pase 120 del 2026-10-05.** Corre la **acción B** que el pase 118 pre-registró: cerrar el
intervalo `[3, 22]` de `P385` leyendo el binding de un **campo estructurado**.

## Qué mide

| Lectura | Filas | Fingerprints | Racimos | Sesgo que le queda |
|---|---|---|---|---|
| prosa anclada a URL *(piso de `P385`)* | — | 54 | **3** | 🔴 no ve handles pelados |
| prosa permisiva *(techo de `P385`)* | — | 54 | **22** | 🔴 liga por co-ocurrencia de línea |
| 🆕 **celda anclada al token `sha256`** | 155 | 44 | **5** | 🔴 no ve la columna tipada por encabezado |
| 🆕 **columna tipada por su ENCABEZADO** | 144 | 61 | **13** | 🔴 cuenta de más por `P392`/`P393` |
| 🆕 **unión estructurada** | 299 | 79 | **14** | — |
| 🟢 **canónico por CONJUNTO de repos** | — | — | 🟢 **10** | — |

🟢 **Cláusula de la acción B (pedía caer dentro de `[3, 22]` y ser ≥4): CONFIRMADA por las cuatro
lecturas estructuradas.** La refutación (≤3) no se dispara con ninguna.

## El hallazgo (`P391`)

🔵 **La lectura estructurada ANGOSTA el intervalo —de ancho 19 a ancho 9— pero NO lo cierra, y lo
que queda ya no es de la misma clase.** El ancho de `P385` era **convención de escritura**. El
ancho residual se descompone en dos causas medidas:

- 🟢 **8 racimos** que el lector anclado al token no veía porque el digest vive en una **columna
  cuyo encabezado dice `sha256`** y cuya celda trae el hex pelado. **Es el lector, y está arreglado.**
- 🔴 **2 conjuntos de repos con MÁS DE UN digest publicado**, que no se arreglan con un parser:
  - **`P392`** — el trío `OpenTutor` tiene columna de huella del `README.md` **y** del `LICENSE`, y
    el lector tipa las dos igual ⇒ **una huella se identifica por el par `(archivo, digest)`**, no
    por el digest. Importa porque la compuerta de `P386` razona sobre el `LICENSE`: alimentada con
    la del `README`, dictaminaría procedencia leyendo prosa de presentación.
  - **`P393`** — el par `blackboard-mcp` colisiona bajo `fa4e32e5e622`, una huella que **`P333`
    retractó** en el pase 107. El corpus es **append-only por encargo**, así que conserva lo
    retractado y **el censo lo re-anima**. ⇒ Hace falta una **lista de retractaciones**, no un lector
    mejor; sin ella la calidad del censo se degrada monótonamente con cada pase.

## Punto ciego propio, declarado

🔴 **El racimo que publica es un PISO en su MEMBRESÍA, no sólo en su conteo.** El repo canónico de
la familia `canvas-mcp` vive en una celda **compuesta**
(`` `DERIVATIVE-OF vishalsachdev/canvas-mcp` ``), que no es un slug entre backticks: el lector lo usa
como **ancla** para calificar los handles pelados (`sirdanielm` → `sirdanielm/canvas-mcp`) pero **no
lo liga como miembro**. El caso está en la suite, con ese nombre.

## Uso

```
python3 structured_binding.py agents/top.md agents/trending.md repos/foundations.md \
        repos/trending.md verticals/solutions.md intel/market.md intel/trends.md \
        compose/patterns.md            # TSV: las 3 lecturas + los racimos
python3 test_structured_binding.py     # 17/17
```

## Estado

🟢 **Implementado, corrido sobre los 8 archivos este pase, y con suite de 17 casos** — cada uno
nombra el sesgo que demuestra, incluidos el control de convergencia (los lectores coinciden cuando
la convención es uniforme), el control de co-ocurrencia (una celda de prosa **no** liga) y el punto
ciego de arriba.
