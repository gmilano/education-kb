---
industry: education
region: Global
updated: 2026-10-05
---

# `p399-census-order-gate` — un auto-censo publicado en el mismo pase que escribe mide el corpus PRE-ESCRITURA

**Pase 121 del 2026-10-05 (lectura `18:45Z`).** Nace de una contradicción interna, no de una
hipótesis: el README de `p394-holder-absent-census` publica **15 / 46 / 125 / 186**, y re-correr su
**propia invocación publicada** sobre el corpus commiteado da **23 / 46 / 139 / 208**.

## El criterio, dicho ANTES de medir

- **El criterio de clasificación no se cambió.** `is_row`, `classify` y el universo son los de
  `P394`, con los `\b` de los acrónimos cortos incluidos (sin ellos `MIT` casa dentro de
  «com-**MIT**» y el universo se infla con toda fila que nombre un *commit*).
- **El árbol se lee de `git show`, no se infiere.** Un censo sobre el *working tree* no prueba nada
  sobre lo que un pase publicó; la revisión sí.
- **Un archivo que no existe en la revisión NO es un cero.** Se omite y se publica cuántos archivos
  se leyeron, para no confundir «no estaba» con «no tenía filas» (clase de `P160`).
- **`DESFASADO` sólo se puede afirmar si los dos árboles DIFIEREN.** Si son iguales la cifra
  describe los dos y el veredicto correcto es `OK`. Es el control negativo de esta compuerta y está
  en la suite.

## Lo medido

| Árbol | `ausente` | `presente` | `MUDO` | universo | archivos leídos |
|---|---|---|---|---|---|
| `8110153` — commit del **pase 119** | **15** | **46** | **125** | **186** | 8 |
| `195fe59` — commit del **pase 120**, donde `P394` se publicó | **23** | **46** | **139** | **208** | 8 |
| **publicado por `P394`** | **15** | **46** | **125** | **186** | — |

🔴 **Veredicto: `DESFASADO`.** La cifra publicada es, exactamente, el censo del árbol **anterior**.

## El hallazgo (`P399`): es un error de ORDEN, no de aritmética

Medir el estante → escribir las filas del pase → commitear con la cifra de antes. El pase 120
agregó **22** filas con huella y licencia a su propio corpus mientras publicaba un censo que no las
veía.

🔴 **Y el motivo por el que ningún control lo agarraba, que la compuerta ahora imprime solo:** la
clase **`presente` no se mueve** (46 → 46). Es la única columna que un lector verifica a mano,
porque es la que tiene nombres propios; el error vive entero en `ausente` (**+53 %**) y en `MUDO`
(**+11 %**). Por eso `blind_spot()` es parte de la salida y no un detalle: nombra qué columnas
**no** sirven para detectar el desfase en cada caso concreto.

## Las dos salidas, y las dos sirven

1. **Medir después de escribir** las filas del pase.
2. **Publicar contra qué commit se midió.**

Lo que no sirve es lo que había: medir antes y publicar como si fuera el estado final.

## Invocación (regla de `P107`: la cifra se publica con su invocación)

```bash
cd compose/code/p399-census-order-gate

# la suite
python3 test_census_order.py                      # 🟢 21/21

# el caso que destapó P399, desde la raíz del repo
cd ../../.. && python3 compose/code/p399-census-order-gate/census_order.py \
    8110153 195fe59 15 46 125 186
# => veredicto DESFASADO · clases-que-NO-se-mueven: present · exit 3
```

**Códigos de salida:** `0` la cifra describe el árbol propio · `3` **DESFASADO** (describe el
anterior) · `4` **DESCONOCIDO** (no describe ninguno de los dos, que es peor: no se sabe qué midió)
· `2` invocación mal formada.

## Hoy

| Qué prueba | Invocación | Resultado |
|---|---|---|
| la suite, con el control negativo de árboles iguales y el punto ciego | `python3 test_census_order.py` | 🟢 **21/21** |
| el censo de `P394` contra sus dos árboles | `census_order.py 8110153 195fe59 15 46 125 186` | 🔴 **DESFASADO** (`exit 3`), punto ciego `present` |

## Su punto ciego propio, declarado

🔴 **Esta compuerta no sabe si una cifra publicada corresponde a la invocación que se le pasa.**
Compara cuatro números contra dos árboles; si un pase publicara un censo con **otro criterio** de
universo, los cuatro números no coincidirían con ninguno de los dos árboles y el veredicto saldría
`DESCONOCIDO` — que es honesto, pero no distingue «se midió el árbol equivocado» de «se midió con
otro criterio». Separar esos dos casos pide que el pase publique también el **criterio**, y eso es
convención de escritura, no algo que este instrumento pueda medir.
