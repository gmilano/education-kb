---
industry: education
region: Global
updated: 2026-10-05
---

# `P357` — la capa de HINT no hereda la cesion de su problema padre: la deja VACIA

Artefactos y suite del **pase 112 (2026-10-05)**. Corre la **accion C** pre-registrada por el
pase 111, que pedia medir la clasificacion de cesion de `P346`/`P348` sobre la capa de *hint* y
predijo que la tasa `RESOLUBLE` quedaria **dentro de ±3 pp** del 76,4 % de los problemas,
*«porque el hint hereda el `license` de su problema padre»*.

Corpus: `CAHLR/OATutor-Content` en **`1925decc91567faf6203bdb41b9d52b14891426f`**
(`P593`: el commit es parte de la invocacion).

## Invocacion

```sh
python3 hint_layer.py /ruta/a/OATutor-Content   # el barrido (requiere el corpus)
python3 test_p357.py                            # la suite: 24/24, SIN el corpus
```

La suite reproduce las cifras desde los artefactos versionados
(`reparto-capa`, `herencia`, `contrafactual`, `sha`), asi que **corre en un clon nuevo** — que es la
regla que `P352` dejo y `P355` convirtio en control.

## El reparto por capa

| capa | unidades | `RESOLUBLE` | tasa | `license` vacio |
|---|---|---|---|---|
| problema | 13.371 | 10.210 | 🟢 **76,4 %** | 2.545 |
| **hint** | **69.121** | **42.985** | 🔴 **62,2 %** | **26.136 (37,8 %)** |
| TOTAL | **82.492** | | | |

🟢 **El denominador de 82.492 del pase 106 queda REPRODUCIDO exactamente.** Y se replica la nota del
pase 107: `git ls-tree` enumera **49.473** rutas y el arbol materializado tiene **49.479** archivos
— la diferencia de **6** son los caminos con bytes de control en el nombre que `git` cita entre
comillas. **Dos canales, dos cifras, y la diferencia explicada.**

## La accion C, contra su prediccion

| | valor | contra la banda de ±3 pp |
|---|---|---|
| pedia | dentro de ±3 pp de 76,4 % | — |
| **medido** | **62,2 %** | 🔴 **−14,2 pp** ⇒ **REFUTADA** |

## El mecanismo, medido DIRECTO y no deducido del agregado

Cada objeto de hint trae sus **propios** campos `oer` y `license`, asi que la herencia es
**falsable por lectura**:

| relacion hint ↔ padre | unidades | % |
|---|---|---|
| igual al padre | 55.418 | **80,2 %** |
| **hijo VACIO con padre que cede** | **13.499** | **19,5 %** |
| hijo cede con padre vacio | 204 | 0,3 % |
| **se contradicen** | **0** | **0,0 %** |

🔵 **La herencia NO es la identidad** (80,2 %), la divergencia es **asimetrica 66 a 1** (el hijo
deja caer, no agrega), y la cubeta de **contradiccion esta vacia** ⇒ el defecto es **OMISION** y se
arregla **propagando**, no arbitrando.

## El contrafactual, que es el numero que decide

| medicion | valor |
|---|---|
| observado | **62,2 %** |
| **bajo la herencia ASUMIDA** (cada hint vacio toma la cesion del padre) | **72,6 %** (**+7.212** unidades, **+10,4 pp**) |
| residuo contra los problemas | 🔴 **−3,8 pp** ⇒ **la banda de ±3 pp SIGUE fallando** |

🔵 **La prediccion era inalcanzable sobre su propia premisa:** aun concedida la herencia entera, el
residuo cae fuera de la banda. Ese residuo tiene mecanismo propio — **los padres que tampoco
ceden**: un hint no puede heredar una cesion que arriba no existe. **Dos motivos independientes de
fallo, y el segundo solo aparece al medir el contrafactual** (ver `P679` en `intel/trends.md`).

## Un hecho de FORMA

La capa de hint tiene vocabulario **BINARIO** —solo `RESOLUBLE` y `AUSENTE`—. Las otras tres clases
(`VERSION-SIN-VARIANTE`, `NO-ES-CESION`, `NO-RECONOCIDO`) viven **solo** en la capa de problema.
**Las dos capas no son la misma pregunta con distinto `n`.**

## Controles negativos

- **Un dominio desnudo (`https://openstax.org/`) sale `NO-ES-CESION`.** Si saliera `RESOLUBLE`, la
  tasa de la capa de hint estaria inflada por URLs que no ceden nada.
- **El recorrido entra en LISTAS:** el JSON de `tutoring/` es una lista de hints. Si no entrara, la
  capa mediria **18.054** unidades (una por archivo) en vez de **69.121**.
- **Se reusa `clasificar` de `p345-oer-four-forms/entregabilidad.py`** (`P237`) — el mismo
  instrumento que produjo el 58,0 % y el 76,4 %. Un clasificador propio volveria la comparacion
  incomparable por una tercera via, que es el defecto que `P344` y `P348` ya documentaron.

## La consecuencia de negocio

🔴 **Si se ingiere este corpus y se asume la herencia, se sobre-declara la entregabilidad del
material de tutoria en +10,4 pp.** Las **42.985** `RESOLUBLE` son entregables sin gestion; las
**13.499** cuyo padre si cede son **recuperables por propagacion** (gestion documental, no
re-autoria); las **12.637** restantes estan **bloqueadas** hasta que el titular aclare.
⚠️ **La capa que un tutor AI usa mas —la de pistas— es la peor cedida del corpus.**
