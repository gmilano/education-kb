---
industry: education
region: Global
updated: 2026-10-05
---

# `P428` — una cifra de censo tiene que declarar su MOMENTO de medición

Artefactos del **pase 124 (2026-10-05, lectura `21:46Z`)**. Cierra la **acción N**, pre-registrada por los pases **122**, **123** y **124** y no construida en ninguno de los tres.

## El defecto, medido en tres pases consecutivos

Un censo del corpus se corre **antes** de escribir, porque es el denominador que decide qué entra. Pero la cifra se **publica dentro del mismo pase que agrega filas**, así que queda vieja en el instante en que se escribe.

| pase | censo pre-escritura | censo post-escritura | delta |
|---|---|---|---|
| 122 | 10 (clase positiva) | 13 | +3 |
| 123 | mismo defecto, acción N sin construir | — | — |
| **124** | **645** slugs del corpus | **655** | **+10** |

🔴 **Ninguna de esas cifras está mal MEDIDA: están mal ETIQUETADAS.** El lector no puede saber si `645` es el corpus contra el que se decidió o el corpus que quedó. Las dos lecturas son útiles y son distintas, y la diferencia entre ellas es exactamente el aporte del pase.

## La regla

Toda cifra de censo se publica con su momento:

- **`PRE`** — el denominador con el que se decidió qué entra. Correcta para esa función, **y debe publicar el delta** para que el lector pueda derivar el estado final.
- **`POST`** — el estado en que queda el árbol. Debe reproducir el censo re-corrido después de escribir.
- **sin momento** → `SIN-MOMENTO`: es el defecto mismo, y es la clase que los pases 122 y 123 publicaron sin verla.

🔵 **La asimetría que importa:** una cifra `PRE` **no** se invalida por el delta. Lo que la invalida es no publicarlo.

## Lo que este pase hizo con su propia cifra

Publicó **645** etiquetada como denominador **pre-escritura** (`P311`/`P287`), midió **655** después de escribir y declaró el delta de **+10**. Corrido por la compuerta: **`OK`**.

```
$ python3 gate_censo.py 645 655 PRE 10
OK             declarado=645 post=655 delta_real=10 | cifra PRE con su delta publicado y verificado

$ python3 gate_censo.py 645 655 POST
DESFASADO      declarado=645 post=655 delta_real=10 | P428: declara POST=645 y el censo posterior da 655
```

## Suite

`test_gate_censo.py` — **9/9 🟢**, y los 9 casos son cifras reales de este árbol (las del pase 122 y las del 124), no inventos. Incluye el control negativo: un árbol quieto (delta 0) pasa como `PRE` válida.

## Veredicto de la acción N

🟢 **CONFIRMADA en su premisa y CERRADA en su instrumento.** La hipótesis decía *«con la compuerta puesta, re-correr los censos da 0 `DESFASADO`»*. Medido: con la compuerta puesta y la cifra etiquetada `PRE` + delta, el veredicto es `OK` y los `DESFASADO` son **0**. 🔵 Pero el modo en que se consigue el cero **no** es el que la acción imaginaba: no se consigue midiendo después, se consigue **etiquetando el momento**. Medir después y re-escribir produciría una cifra que vuelve a quedar vieja con la próxima edición — el defecto es de **etiqueta**, no de **orden**.
