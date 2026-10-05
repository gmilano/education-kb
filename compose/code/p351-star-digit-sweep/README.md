---
industry: education
region: Global
updated: 2026-10-05
---

# `P351` — un barrido por una cifra PUBLICADA no distingue el dato de la CITA que lo refuta

Artefactos y suite del **pase 111 (2026-10-05)**. Corre la **accion B** pre-registrada por el
pase 110.

## El veredicto: CONFIRMADA en el conteo, y la segunda rama NO dispara

| clausula pre-registrada por el pase 110 | pedia | medido | veredicto |
|---|---|---|---|
| *«hay **≥20** cifras de estrellas con digitos exactos que ningun canal reproduce»* | ≥ 20 | 🟢 **262 ocurrencias · 42 valores** | **CONFIRMADA** |
| rama de refutacion: *«que sean <20»* | — | no dispara | — |
| rama de refutacion: *«que **alguna** sea posterior al pase 110»* | — | 🟢 **0** | no dispara |

🟢 **La regla que el pase 110 escribio no se violo en el 111:** 0 ocurrencias de un pase posterior
al 110, descontando meta-menciones.

## El reparto, que es lo que se puede arreglar

| archivo | ocurrencias |
|---|---|
| `agents/trending.md` | 94 |
| `agents/top.md` | 57 |
| `repos/trending.md` | 57 |
| `intel/trends.md` | 36 |
| `repos/foundations.md` | 6 |
| `verticals/solutions.md` · `intel/market.md` | 4 cada uno |
| `compose/patterns.md` | 4 |

⚠️ **Medido sobre el arbol TAL COMO ESTE PASE LO DEJA.** De las 262, **8 son de este pase** y las 8
son **citas** (el texto de `P351` citando «385.407 ★» para explicar el defecto). Es el instrumento
midiendose a si mismo, y es por eso que el clasificador de abajo tuvo que cambiar.

| valor | ocurrencias | banda (`P349`) |
|---|---|---|
| `385.407 ★` | 44 | `K-ENTERO` ±500 |
| `108.128 ★` | 26 | `K-ENTERO` ±500 |
| `151.639 ★` | 23 | `K-ENTERO` ±500 |
| `62.735 ★` | 22 | `K-3CIFRAS` ±50 |
| `60.284 ★` | 22 | `K-3CIFRAS` ±50 |
| `55.226 ★` | 20 | `K-3CIFRAS` ±50 |

## El punto ciego del instrumento, que lo destapa su propio resultado

🔴 **Varias ocurrencias son META-MENCIONES:** el pase 110 citando «385.407 ★» precisamente para
decir que no es reproducible, y el texto de la pre-registracion de esta accion citandola como
ejemplo de lo que hay que buscar. **Un `grep` por la cifra las cuenta igual que un dato publicado.**
Medido en este pase: **20 de 262**.

🔵 **Consecuencia de metodo: el conteo crudo SOBREESTIMA el defecto.** Lo que hay que arreglar no
son 262 ediciones. Son los **42 valores distintos** y, sobre todo, las **31 que viven en la region
de CATALOGO** —antes de cualquier encabezado de pase—, que es la unica region que un lector lee
como dato vigente. **Una cifra citada para refutarla es el registro FUNCIONANDO, no el defecto.**

## 🔴 El defecto que este pase se hizo A SI MISMO, y el arreglo que NO fue alargar una lista

La primera version de `es_meta_mencion` era **lexica**: una lista de palabras que suelen aparecer
cuando una linea cita una cifra (`no son reproducibles`, `del tipo`, `refuta`, …). 🔴 **El texto de
este mismo pase la rompio:** tres citas claras quedaron contadas como DATO porque no traian ninguna
de esas palabras, y la rama de refutacion de la accion B —*«que alguna sea posterior al pase 110»*—
**disparo sobre el pase 111**.

| las tres que la version lexica no vio | donde |
|---|---|
| *pase 110 citando «385.407 ★» precisamente para decir que no es reproducible* | `agents/top.md` |
| *(«385.407 ★») que ningun canal de este entorno reproduce* | `compose/patterns.md` |
| *«DeepTutor, 40.823 ★» no lo es, y es la forma que…* | `compose/patterns.md` |

🔵 **Las tres van entre comillas latinas, y el arreglo correcto es ESTRUCTURAL, no lexico:** en este
arbol una cifra **citada** va entre `«»` o en codigo inline, y una cifra **publicada** va desnuda en
prosa o en una celda de tabla. Alargar la lista de palabras habria sido `P354` otra vez — un ancla
que reconoce una **ortografia** y no el **objeto**.

🟢 **La senal lexica se conserva como SECUNDARIA**, para la cita sin delimitador. Y el control mas
fino de la suite es el que exige la **posicion**: si una linea tiene un tramo citado pero la cifra
cae **fuera** de el, la cifra es dato — sin la posicion, el clasificador contagiaria toda la linea.

🔵 **Es la forma INVERSA de `P344`:** ahi el denominador EXCLUIA los casos que importaban; aca
INCLUYE casos que no son el defecto. Las dos veces el numero salia bien y significaba otra cosa.

## Dos nuances del atribuidor, las dos con test

1. 🔵 **Una pre-registracion atribuye a un pase que todavia NO corrio.** El encabezado *«Acciones
   pre-registradas para el pase 111»* hace que las lineas siguientes caigan en el pase 111 por
   atribucion de linea. Por eso la rama de refutacion se evalua **excluyendo meta-menciones**, y
   no por el maximo del pase.
2. 🔴 **El regex no ve tres digitos, y por eso este barrido NUNCA iba a encontrar el `265 ★` de
   `OATutor`.** Ese defecto de propagacion (`P353`) se encontro por otra via. El denominador de
   una accion decide que defectos son encontrables por ella — tercera vez en dos pases.

## Que hay aca

| archivo | que es |
|---|---|
| `barrido.py` | el barrido, la atribucion por pase y el clasificador de meta-mencion |
| `resultado.2026-10-05.txt` | la corrida |
| `test_p351.py` | **26** aserciones, 0 fallos (`Python 3.11.15`) |
