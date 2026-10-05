---
industry: education
region: North America
updated: 2026-10-05
---

# `p326-titleholder-book-license` — el campo de licencia de un item es una AFIRMACION DEL REDISTRIBUIDOR, y se puede contrastar con el titular

> Nuevo en el **pase 105 del 2026-10-05**. Corre la **accion pre-registrada del pase 105** sobre
> `OATutor-Content` y la devuelve **CONFIRMADA en la letra y FALSIFICADA en la magnitud — en la
> direccion que nadie pre-registro**: no es que `Calculus Volume 1` sea la excepcion `NC-SA`
> entre libros `CC BY 4.0`; es que **ocho de las nueve ediciones medidas son `NC-SA`** y el libro
> `CC BY 4.0` que si existe es el unico que **ningun item etiqueta**.

## La accion pre-registrada, y por que se pudo correr con `openstax.org` caido

El pase 104 la dejo escrita asi, y con una prohibicion explicita:

> *«leer, **del titular** (`openstax.org`), la licencia de los **7** libros que `OATutor-Content`
> nombra. […] Lo que NO puede pasar es rellenar con el canal secundario: si el egress sigue
> cerrado, se dice no se pudo correr.»*

🔴 **`openstax.org` sigue en `000` por egress** (medido este pase, junto con `creativecommons.org`,
`arxiv.org`, `aclanthology.org`, `unu.edu`, `coe.int`, `publications.iadb.org`, `unesco.org`).

🟢 **Y la accion se corrio igual, sin violar la prohibicion, porque el titular publica por DOS
canales y solo uno estaba caido:** OpenStax mantiene el *payload* de cada libro en la organizacion
**`openstax` de GitHub** (`osbooks-*`), alcanzable por `raw.githubusercontent.com` (**200**). Se leyo
de ahi, **del titular y no de un agregador**, con dos lecturas independientes por libro:

1. el `<md:license>` del `collections/<slug>.collection.xml` del propio libro — **cesion por libro**;
2. el `LICENSE` de la raiz del repo del *bundle* — **cesion por repo**.

**`P326-A`**: *«egress cerrado al sitio del titular» NO es «la cesion del titular es inalcanzable».
Un titular puede publicar por varios canales, y el pase que hereda la declaracion de canal del
anterior se pierde el que esta vivo.* Es la direccion complementaria de `P314`: lo que descalifica a
un canal secundario no es que sea **otro canal**, es que sea **otro titular**.

## Eje A — la cesion, leida del payload del titular

| edicion (slug del titular) | `<md:license>` del libro | `LICENSE` de la raiz | bytes |
|---|---|---|---|
| `calculus-volume-1` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.443 |
| `precalculus-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.013 |
| `college-algebra-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.013 |
| `elementary-algebra-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| `intermediate-algebra-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| `introductory-statistics-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| `university-physics-volume-1` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.013 |
| `college-physics-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| 🟢 `physics` | **CC BY 4.0** (*«Creative Commons Attribution License»*) | CC BY 4.0 | 19.103 |
| 🟢 `statistics` | **CC BY 4.0** (*«Creative Commons Attribution License»*) | CC BY 4.0 | 18.706 |
| `college-success-2e` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| `college-success-concise` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| `preparing-for-college-success` | **CC BY-NC-SA 4.0** | CC BY-NC-SA 4.0 | 21.442 |
| 🔵 **control negativo**: `college-success` (slug inventado en repo real) | **NO-ALCANZABLE** (404) | CC BY-NC-SA 4.0 | 21.442 |

🟢 **`physics` y `statistics` son el control positivo que vuelve publicable todo lo demas.** Un
barrido que solo sabe devolver `NC-SA` no mide nada; este devuelve `CC BY 4.0` **en el mismo canal,
con el mismo extractor, para otros libros del mismo titular**. La licencia de OpenStax es **por
libro**, no por editorial — y por eso hay que leerla libro por libro en vez de citar «OpenStax es
CC BY».

🔵 **Y el control negativo esta en la misma tabla:** un `collection` **inventado** en un repo
**real** da **404 → `NO-ALCANZABLE`** mientras el `LICENSE` de la raiz del mismo repo **si** se lee.
Las dos lecturas son independientes y **un slug adivinado no hereda en silencio** la cesion del repo.

🔴 **Una correccion que este instrumento se hizo a si mismo antes de publicar.** La primera version
de esta tabla daba `osbooks-statistics` como `NC-SA` **por vecindad** —el resto del titular lo era—
y `osbooks-college-success` como *«no medida»*. **Medidas, la primera salio falsa**: `statistics` es
**`CC BY 4.0`**. Es el error exacto que este instrumento existe para no cometer, y lo unico que lo
evito fue medir las dos filas en vez de completarlas.

### 🔴 Y un defecto de metodo que indicta a esta base entera: los bytes no son identidad

Tres `LICENSE` del mismo titular dan **21.443 / 21.013 / 21.442 B** y **429 lineas cada uno**. No son
tres licencias: son **el mismo texto con CRLF, con LF, y con CRLF sin salto final**. Normalizando el
fin de linea, los tres dan **un unico `sha256` `78442b480475e7ae…`**.

**`P327`**: *el conteo de bytes y el `sha256` **crudo** de un archivo de licencia **no son una
identidad**: el mismo texto varia hasta **430 B** segun el fin de linea. La identidad es el `sha256`
del texto **normalizado**.* Esta base viene citando *«`LICENSE` 20.849 B»* y `sha256` crudos como
huella desde el pase 66 — **los datos siguen siendo correctos, la huella no era una huella.**

## Eje B — el CENSO: 13.371 problemas, no una muestra

`compose/code/p322-content-item-license/` midio **1.216 de 13.371** por muestreo sistematico. Este
pase **enumera el arbol** (`P275`: **51.929** rutas, reproduce el pase 104 al archivo) y **materializa
los 13.371** problemas por `sparse-checkout`, asi que el reparto deja de ser una estimacion.

🟢 **El muestreo del pase 104 queda VALIDADO** — censo **76,4 / 19,0 / 3,4 / 1,2 %** frente a
**75,7 / 19,3 / 3,6 / 1,4 %** con `STEP=11`. El instrumento anterior era sano; lo que le faltaba no
era precision, era **el segundo campo**.

**El segundo campo es `oer`, y es el que dice QUIEN ES EL TITULAR.** El pase 104 lo tenia a la vista
y lo leyo como procedencia; cruzado contra el eje A, decide la entrega:

| | n | % | veredicto |
|---|---|---|---|
| 🔴 **declara `CC BY 4.0`; el titular de la edicion citada cede `NC-SA`** | **8.312** | **62,2 %** | **contradice al titular** |
| 🔴 no declara nada; el titular cede `NC-SA` | 2.104 | 15,7 % | no embarcable |
| ⚠️ declara `CC BY 4.0` contra una edicion que **el titular ya no publica** | 1.748 | 13,1 % | **sin resolver — escape de edicion ABIERTO** |
| ⚠️ titular no resuelto (`docs.google.com`, `drive.google.com`, `oer` ilegible) | 455 | 3,4 % | sin resolver |
| 🔴 el campo de cesion lleva una **URL de procedencia** (`ds100.org`) | 160 | 1,2 % | sin cesion |
| 🟢 **autoria propia de OATutor** (`oer: OATutor.io`) | 552 | 4,1 % | **embarcable** |
| 🟢 el titular **SI** cede `CC BY 4.0` (`physics`) | 40 | 0,3 % | **embarcable** |

**Embarcable en una entrega comercial: 592 items = 4,4 %.** No embarcable y **medido**: **77,9 %**.
Sin resolver y **declarado**: **17,7 %**.

### 🔵 La ironia esta medida, y es la prueba de que la tasa de llenado no mide permiso

**`physics` es el unico libro cuyo titular SI cede `CC BY 4.0`, y sus 40 items son los unicos que
dejan el campo VACIO.** `elementary-algebra-2e`, cuyo titular cede `NC-SA`, lo llena en **2.650 de
2.840**. El campo no esta siguiendo la cesion: esta siguiendo la plantilla de autoria del curso.

## El control que casi no se corrio, y que era obligatorio: la EDICION

La hipotesis alternativa que habia que matar antes de publicar: *«los items dicen `CC BY 4.0`
porque salieron de una edicion anterior que **si** era `CC BY 4.0`, y OpenStax relicencio despues»*.
Si fuera cierta, el item seria correcto y el error estaria en comparar contra la edicion de hoy.

Se mata **leyendo el slug de libro que el propio item cita**:

| edicion citada por el item | cede el titular | n | dice `CC BY 4.0` | vacia |
|---|---|---|---|---|
| `elementary-algebra-2e` | CC BY-NC-SA 4.0 | 2.840 | 2.650 | 190 |
| `intermediate-algebra-2e` | CC BY-NC-SA 4.0 | 2.063 | 2.034 | 29 |
| `college-algebra-2e` | CC BY-NC-SA 4.0 | 1.939 | 1.875 | 64 |
| `precalculus-2e` | CC BY-NC-SA 4.0 | 1.903 | 1.306 | 543 |
| ⚠️ `introductory-statistics` (**1e**) | **no publicada por el titular** | 1.700 | 1.684 | 16 |
| `calculus-volume-1` | CC BY-NC-SA 4.0 | 1.012 | 2 | 1.010 |
| `university-physics-volume-1` | CC BY-NC-SA 4.0 | 394 | 181 | 213 |
| `college-physics-2e` | CC BY-NC-SA 4.0 | 265 | 264 | 1 |
| ⚠️ `precalculus` (**1e**) | **no publicada por el titular** | 48 | 48 | 0 |
| 🟢 `physics` | **CC BY 4.0** | 40 | 0 | 40 |

🟢 **Para 10.416 items el escape esta CERRADO:** el item cita la **misma edicion** (`-2e`, o
`calculus-volume-1`) cuyo `collection.xml` declara `NC-SA`. No hay edicion intermedia que invocar.

⚠️ **Para 1.748 items el escape queda ABIERTO y se dice en vez de callarse:** citan
`introductory-statistics` y `precalculus` **1e**, y la enumeracion de `collections/` de los dos
*bundles* vivos muestra que el titular **ya no publica esas ediciones** (`osbooks-introductory-statistics-bundle`
trae solo `-2e` y `introductory-business-statistics-2e`; `osbooks-college-algebra-bundle` solo `-2e`).
**Ausencia aserida por enumeracion, no por 404 de un nombre adivinado.** Queda **pre-registrado para
el pase 106**.

## Un defecto de ESTE instrumento, encontrado por ESTE instrumento antes de publicar

🔴 La primera version del extractor buscaba solo `openstax.org/books/<slug>` y resolvia **2.878** de
**12.332** items con `oer` en `openstax.org`. Los otros **9.326** usan
`openstax.org/details/books/<slug>` — **tres cuartos del universo**, perdidos en silencio. Si el
veredicto se hubiera publicado con esa version, el hallazgo habria salido con **un cuarto** de su
denominador y la familia `P171`/`P319` se habria cobrado otro pase. **La senal que lo delato fue una
aritmetica que no cerraba** (12.332 por host frente a 2.878 por slug), no una excepcion.
El test `test_verdict.py` fija la forma `/details/books/` con el numero a la vista.

## Hallazgo lateral: 6 rutas del `content-pool` llevan caracteres de control C1

```
content-pool/a89b247ds100-su19-final-Q6/steps/a89b247ds100-su19-final-Q6\177/…
content-pool/a89b247ds100-su19-final-Q6/steps/a89b247ds100-su19-final-Q6\302\200/…
content-pool/a89b247ds100-su19-final-Q6/steps/a89b247ds100-su19-final-Q6\302\201/…
```

`\177` (DEL), `U+0080` y `U+0081` **dentro de nombres de directorio**, en el mismo curso de Data100
que ya aportaba los 160 `URL-NO-LICENCIA`. 🔴 **Consecuencia operativa concreta:** esas rutas rompen
en Windows, en `zip` y en cualquier *pipeline* que normalice nombres — **un cliente que empaquete el
`content-pool` tal cual se lleva seis rutas que su CI no puede reproducir.** Es la segunda cosa que
el curso de Data100 aporta a esta base, y las dos son de higiene de datos.

## Como correrlo

```bash
# 1. canal + control negativo (obligatorio ANTES de cualquier veredicto)
bash controls.sh | tee controls.$(date -u +%F).txt

# 2. eje A — cesion del titular, leida de su payload en GitHub
bash sweep_titleholder.sh books.tsv > result.$(date -u +%F).tsv

# 3. materializar los 13.371 problemas (enumeracion P275 + sparse-checkout)
git clone --depth 1 --filter=blob:none --no-checkout \
    https://github.com/CAHLR/OATutor-Content /tmp/oatc
git -C /tmp/oatc sparse-checkout set --no-cone '/content-pool/*/*.json'
git -C /tmp/oatc checkout

# 4. eje B — censo y cruce
python3 census_items.py   /tmp/oatc
python3 edition_control.py /tmp/oatc | tee edicion.$(date -u +%F).txt
python3 verdict.py        /tmp/oatc | tee veredicto.$(date -u +%F).txt

# 5. controles del instrumento (22 aserciones, sin red)
python3 test_verdict.py
```

## Lo que este instrumento NO mide, dicho en vez de callado

- 🔴 **No mide los 18.054 JSON de `tutoring/`** — pistas y andamios, **dos tercios** del arbol.
  El pase 104 publico **18.051**; el conteo correcto por enumeracion es **18.054**.
- 🔴 **No abre archivos comprimidos** ni los **2.443 `.gif`** del arbol: una imagen de tercero
  dentro de un item permisivo es un eje que esta base todavia no toco.
- 🔴 **No resuelve los 455 items de titular no resuelto** (`docs.google.com`, `drive.google.com`,
  `oer` ilegible): hace falta abrir cada documento, y el egress a Google Docs no se midio este pase.
- ⚠️ **No establece que `introductory-statistics` 1e fuera `CC BY 4.0`.** Que el titular ya no la
  publique **no concede ni niega** nada: es exactamente el estado que `P324` obliga a no convertir
  en permiso.
