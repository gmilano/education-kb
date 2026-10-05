---
industry: education
region: Global
updated: 2026-10-05
---

# `P345` / `P346` — `P337` cierra, y lo que cierra es que la pregunta no decidia nada

Artefactos y suite del **pase 110 (2026-10-05)**. Medido sobre
`CAHLR/OATutor-Content`, **sha `1925decc91567faf6203bdb41b9d52b14891426f`** — el **MISMO** sha
sobre el que los dos artefactos del pase 108 se contradecian, asi que la comparacion es exacta y
no por aproximacion.

## Que hay aca

| archivo | que es |
|---|---|
| `censo_oer.py` | el censo de formas de `oer`, en **lotes de 2.000** con el parcial de cada lote guardado (la cota que los pases 108 y 109 perdieron) |
| `corte_figuras.py` | atribuye cada figura a su problema **por RUTA** y aplica el corte |
| `entregabilidad.py` | clasifica el campo `license` en **cuatro** clases de cesion |
| `censo-unidades.2026-10-05.tsv.gz` | **13.371** unidades con `oer`, `license`, `courseName`, forma |
| `corte-figuras.2026-10-05.tsv` | **2.443** figuras con su forma y su lado |
| `entregabilidad.2026-10-05.tsv` | las 2.443 con su clase de cesion |
| `materialize.sh` | la version por `git cat-file`, **que NO sirve** — ver la nota de canal |
| `test_p345.py` | **21 aserciones**, 0 fallos (`Python 3.11.15`) |

## Nota de canal, antes de cualquier cifra

🔴 **`git cat-file --batch` sobre un clon `--filter=blob:none` NO sirve para materializar**: los
blobs no estan, y `cat-file` los pide **de a uno** al remoto. La corrida se cuelga sin producir una
fila, que es exactamente como se perdieron los pases 108 y 109 sobre esta misma tarea.

🟢 **Lo que si sirve:** `git clone --depth 1` **con** blobs — **711 MB, 20 segundos, 49.483 JSON**.
La deuda de tres pases no era de tiempo: era de **eleccion de canal**. Un filtro que abarata
enumerar el arbol encarece leerlo, y la tarea de este pase era leerlo.

## La prediccion pre-registrada: CONFIRMADA en la letra

> *«al clasificar por las cuatro formas de URL juntas, el corte converge a **1.611** y no a 1.570»*

🟢 **Medido: `OPENSTAX 1611` / `NO-OPENSTAX 832`.** Converge a 1.611.

## `P337` cerrado — y el mecanismo es un numero, no una conjetura

| forma de `oer` | figuras |
|---|---|
| `details-books` (`openstax.org/details/books/…`) | **1.392** |
| `books-pages` (`openstax.org/books/…/pages/…`) | **178** |
| **subtotal** | **1.570** ← el artefacto «menor» |
| `openstax-otro` | 🆕 **41** |
| **total openstax** | **1.611** ← el artefacto «mayor» |
| `NO-OPENSTAX` | **832** |

🔴 **Las 41 son un DOMINIO DESNUDO:** `https://openstax.org/` (39) y `https://openstax.org` (2).
**1.611 − 1.570 = 41**, al uno.

🔵 **Asi que `P337` nunca fue una contradiccion: era un PREDICADO NO DICHO.** Los dos artefactos
estaban aritmeticamente bien y contestaban preguntas distintas — *«¿cuantas figuras invocan a
OpenStax?»* (1.611) y *«¿cuantas tienen una procedencia OpenStax RESOLUBLE?»* (1.570). Las 41
nombran al **EDITOR y no a la OBRA**, que es `P341` medido a nivel de figura y con cifra: sin obra
no hay edicion, y sin edicion no hay cesion resoluble.

⚠️ **Y el denominador que la pre-registracion traia estaba mal:** las unidades son **13.371**, no
12.999 — 372 de diferencia, enumeradas.

## `P346` — el numero que decide un presupuesto no es ninguno de los dos

Tres pases discutieron 1.611 contra 1.570. 🔴 **Medido el campo `license` de las mismas 2.443
figuras, el corte openstax/no-openstax no responde la pregunta de entrega:**

| clase de cesion | figuras | % | que es |
|---|---|---|---|
| 🟢 `RESOLUBLE` | **1.418** | 58,0 % | `CC BY 4.0`, las 1.418 — identificador con variante y version |
| 🔴 `AUSENTE` | **586** | 24,0 % | el campo esta vacio |
| 🔴 `NO-ES-CESION` | **293** | 12,0 % | 🆕 una **URL a un PDF de EXAMEN** de `ds100.org` en el campo `license` |
| 🔸 `VERSION-SIN-VARIANTE` | **146** | 6,0 % | `«CC4.0»` — la version 4.0 son **SEIS** licencias, **TRES** NonCommercial |

🔴 **ENTREGABLE SIN GESTION: 1.418 de 2.443 (58,0 %). Requiere gestion: 1.025 (42,0 %).**

### El cruce, que es lo que mata al corte como proxy de licencia

| lado | clase | figuras |
|---|---|---|
| `OPENSTAX` | 🟢 `RESOLUBLE` | 1.243 |
| `OPENSTAX` | 🔴 **`AUSENTE`** | **368** |
| `NO-OPENSTAX` | 🟢 **`RESOLUBLE`** | **175** |
| `NO-OPENSTAX` | 🔴 `NO-ES-CESION` | 293 |
| `NO-OPENSTAX` | 🔸 `VERSION-SIN-VARIANTE` | 146 |
| `NO-OPENSTAX` | 🔴 `AUSENTE` | 218 |

🔴 **368 figuras estan del lado OPENSTAX y no ceden NADA.** Y **175** del lado NO-OPENSTAX ceden
`CC BY 4.0` impecable. 🔵 **Procedencia y cesion son ejes INDEPENDIENTES, y esta medido en las dos
direcciones** — el 1.611 incluye 368 figuras que no conceden nada, y el «lado malo» incluye 175
que se entregan hoy.

⚠️ **La leccion de metodo, que es la mas caro de este expediente:** tres pases se gastaron
afinando un numero que no decide una entrega. **Antes de medir con precision, hay que preguntar
que decision cambia con el resultado** — y si la respuesta es «ninguna», la precision es gasto.

## Las 293 que no son una cesion, por si se intentan usar

El campo `license` de 293 figuras apunta a `ds100.org/…/past-exams/` y a PDF de examen
(`fa25_mt1_sol.pdf`, `fa25_final_sol.pdf`, `sp25_mt.pdf`, `fa25_mt2.pdf`, `sp25_final.pdf`,
`su25_final.pdf`). 🔴 **Eso es una FUENTE, no una licencia: no concede nada**, y el material
apuntado son examenes de curso. La direccion segura es tratarlas como `AUSENTE` y pedir la cesion,
nunca como «licencia desconocida pero probablemente abierta».

## Colapso de identidad: 6 rutas con caracteres de control

🔴 **`content-pool/a89b247ds100-su19-final-Q6/steps/` tiene TRES directorios distintos** cuyos
nombres se diferencian solo por un caracter de control empotrado — `\177` (U+007F),
`\302\200` (U+0080) y `\302\201` (U+0081). `git ls-tree` los cita; con `-z` salen crudos y los
tres se vuelven **indistinguibles**.

🔵 **Es la misma clase de mecanismo que `P337`, un piso mas abajo: tres unidades colapsan a un
identificador en cuanto el canal normaliza.** Cualquier tubería que indexe por nombre de
directorio pierde dos de las tres sin que nada avise.
