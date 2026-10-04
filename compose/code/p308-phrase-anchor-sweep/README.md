---
industry: education
region: Global
updated: 2026-10-04
---

# `p308-phrase-anchor-sweep/` — la acción pre-registrada del pase 99, corrida

**Qué prueba:** que el veredicto de licencia de esta base **no depende de dónde caen los saltos
de línea** del payload. Antes de este pase sí dependía, en dos reglas distintas, y una de las dos
**invertía** la respuesta comercial sobre el texto más permisivo que existe.

## La predicción que se estaba contestando

El pase 99 pre-registró esto, y con la **unidad nombrada** a propósito (su lección del pase 98 fue
que una predicción cuya unidad es *«pieza licenciada»* la satisface cualquier barrido):

> **Afirmación a refutar:** *«el defecto de `P304` no es de la rama BSD solamente: hay más anclas
> escritas como FRASE CONTIGUA en `lib/license_family.sh`, y cada una pierde sus variantes con
> inserción»*. **La unidad que se cuenta es «ANCLAS DEL CLASIFICADOR mal escritas», no «piezas».**
> Candidatos declarados por nombre: **MIT**, **Unlicense**, **MPL-2.0**. **Si las tres aguantan,
> `P304` era específico de BSD y esa sección estaba equivocada.**

## Veredicto: CONFIRMADA — 3 de 18 anclas, y el daño es peor que el de `P304`

| Candidato nombrado | Forma del ancla | Veredicto |
|---|---|---|
| **Unlicense** | frase cruda de 9 palabras, **sin sombra** | 🔴 **FALLA** — pierde la familia y el veredicto comercial se **INVIERTE** |
| **MIT** | frase cruda de 7 palabras, **sombreada** por el ancla de título | ⚠️ **FRÁGIL** — la sombra lo salva, salvo en los payloads **sin título** |
| **MPL-2.0** | título sobre `$t`, **normalizado** | 🟢 **AGUANTA** — por forma; no medido por falta de payload |

🔴 **Y el control negativo de esta propia suite falló sobre un ancla que NO es una frase:** la
definición de la sección 0 de la AGPL que `P288` instaló es **normalizada** y se perdía igual,
porque **la VENTANA del bloque de título se contaba en LÍNEAS** (`head -40`). Re-envolver más
angosto empuja el mismo texto más allá de la línea 40. Es `P171` reabierto por **tercera** vez y
sobre el par exacto que `P171` existe para proteger.

### Por qué el Unlicense es el caso grave: tres capas, cada una sana por separado

1. el ancla frágil **pierde la familia**;
2. la compuerta de `P250` está condicionada a *«familia identificada»*, así que al perderse la
   familia **la compuerta se ABRE**;
3. corre entonces el token-match sobre el cuerpo **que la compuerta existe para suprimir** — y el
   Unlicense concede con las palabras *«for any purpose, commercial or **non-commercial**»*.

**Veredicto resultante: `NONCOMMERCIAL-NOT-OSI` sobre el texto más permisivo que existe.** El
comentario de `P250` en la propia librería nombra (3) como la falta de solidez que la compuerta
se escribió para evitar. Se evitó — y la precondición de la compuerta resultó depender del
reflujo. **La dirección es la de `P299` (inventa una restricción), no la de `P304` (pierde un
estante):** este defecto hace que la KB **descarte** una pieza usable.

### El número que hace la diferencia, y es medido

| Dato | Valor |
|---|---|
| Primera línea canónica del Unlicense | **71 columnas** |
| Columnas que ocupa el ancla dentro de ella | **9 a 70** |
| `fill-column` por omisión de Emacs | **70** |
| Ancho del ancla de MIT | **43 columnas** (necesita un envoltorio < 43: más raro) |

## El arreglo, y su límite declarado

1. **Se normaliza UNA vez, para todo el payload** (`$n`). El arreglo de `P304` normalizó sólo para
   BSD, en una variable **local**, y eso es exactamente lo que dejó a MIT y al Unlicense leyendo
   el payload crudo.
2. **La ventana del bloque de título se mide en BYTES** (`head -c 4000`), no en líneas. **El
   límite está medido, no elegido** — `window_probe.sh` imprime los offsets sobre los payloads
   reales de esta base:

| Ancla | Payload | Offset (texto normalizado) |
|---|---|---|
| definición de la sección 0 de la AGPL (ancla de `P288`) | `kuali/kfs` | **2.769 B** |
| `Version 3` en el mismo payload | `kuali/kfs` | 2.779 B |
| sección 13 de la GPL-3.0 (**la trampa de `P171`**) | `moodle/moodle` | **28.272 B** |

4.000 B deja la primera **dentro** con margen y la segunda **fuera por un factor de 7** — y de
paso **estrecha** la ventana para los payloads de líneas largas, donde `head -40` llegaba a leer
el cuerpo entero.

🔴 **`P309`, residual y declarado en vez de tapado.** La ventana en bytes volvió a hacer
alcanzable la *línea* del titular, pero `holder_of` devuelve **una línea**, y una línea depende
del reflujo **por construcción**: `Copyright (c) 2015 Tyler Mulligan` mide 33 columnas, así que a
`w=30` vuelve cortado en *«…Tyler»*. **El arreglo no es quitar el ancla `^Copyright`** — ése es el
que `P255` instaló para que no se reporte prosa del cuerpo como titular. Necesita leer un **tramo**
sobre el texto normalizado, que es más de lo que este pase debe cambiar solo, y queda
pre-registrado.

## ¿Está el defecto DISPARANDO en el campo?

**Probar un ancla frágil y probar que los repos la pisan son dos afirmaciones distintas,** y esta
base ya pagó por deslizarse de una a la otra (`P286`, pase 95: un reparto poblacional extrapolado
desde un único control positivo falló por un factor de ~28). Así que:

| | |
|---|---|
| Payloads reales medidos **tal como se publican** | **18** |
| En los que el defecto **estaba disparando** | 🟢 **0** |
| Extrapolación al inventario de 215 slugs | 🔴 **NO SE HACE** |

⚠️ **Y el denominador es chico por un límite del ENTORNO, no del método.** El barrido honesto es
el inventario completo; **el entorno niega enumerar destinos en lote** (`[Exfil Scouting]`, el
mismo bloqueo que el pase 96 declaró). El denominador son los payloads que este pase trajo **uno
por uno, cada uno nombrado**. El arreglo es por lo tanto **preventivo** — y el caso AGPL estaba a
**un solo re-envoltorio** de disparar.

🟢 **La mitad MIT no descansa en un payload que esta base editó:** el eje rotado de este pase
devolvió `Priyamakeshwari/TeachGPT`, cuyo `LICENSE.md` (1.057 B) abre directo en
*«Copyright (c) 2023 Priyadharshini»* **sin línea de título**. La población sin sombra existe, y
para ella el ancla frágil era la única vía a la familia MIT en todo el clasificador.

## Invocación

```sh
sh test_anchors.sh     # la suite:  hoy 100/100
sh anchor_form.sh      # auditoría estatica: forma de cada ancla, antes y despues de P308
sh window_probe.sh     # los offsets con los que se eligio la ventana de 4.000 B
sh field_check.sh      # 18 payloads reales tal como se publican -> result.2026-10-04.tsv
```

`lib/test_license_family.sh` pasa de **62/62 a 79/79** con los controles negativos de `P308`
(familia invariante, **veredicto comercial** invariante, y la contracara obligatoria: que la
ventana en bytes **no afloje `P171`**). **51 suites pasan, 0 fallan.**

## Archivos

| Archivo | Qué es |
|---|---|
| `test_anchors.sh` | la suite — incluye la **réplica pre-arreglo** que reproduce los dos defectos |
| `license_family.PRE-P308-CONTROL-2026-10-04.sh` | la función **superada, verbatim**, como control |
| `anchor_form.sh` | auditoría estática de las 18 anclas + la ventana |
| `window_probe.sh` | los offsets en bytes que eligieron el límite |
| `field_check.sh` | ¿dispara en el campo? repair vs pre-fix sobre 18 payloads |
| `reflow.sh` | el envoltorio duro (`fold -s`), con su límite declarado |
| `fetch_payload.sh` | el canal, un slug por invocación |
| `fixtures/*.LICENSE*` | payloads **reales**, traídos de primera mano y commiteados |

### Una nota de método que costó una corrida

La primera versión de `field_check.sh` **escribió a mano una réplica** de la cascada pre-arreglo,
y la réplica produjo un **falso positivo** en su primera corrida: le faltaba la rama de
declaración, así que `frappe/education` (19 B) volvía como *desacuerdo* sin tener nada que ver con
el reflujo. **Un control que difiere de su sujeto en algo más que la variable bajo prueba no puede
atribuir lo que encuentra** — que es `P126` punto 2 con otro sombrero. Por eso el control es
ahora **la función superada verbatim**, sourceada en un subshell.
