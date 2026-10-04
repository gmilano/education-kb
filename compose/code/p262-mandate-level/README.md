---
industry: education
region: Global
updated: 2026-10-04
---

# `p262-mandate-level/` — un mandato curricular tiene NIVEL, y el nivel no sale del titular

**Pase 88 del 2026-10-04.** Este instrumento existe por una frase que la búsqueda de este pase
devolvió repetida por varias fuentes secundarias:

> *«China and the UAE are the only nations running compulsory, national AI curricula since the
> 2025-26 school year.»*

🔴 **La mitad de esa frase es falsa, y es falsa en el eje que decide el tamaño del mercado.** Medido
contra la autoridad que firma cada instrumento:

| Jurisdicción | Autoridad que obliga | Alcance medido | Nivel |
|---|---|---|---|
| **UAE** | Ministry of Education (federal) | nacional | 🟢 **`NATIONAL`** |
| **China** | **Beijing** Municipal Education Commission | **municipio de rango provincial** | 🔴 **`SUBNATIONAL-PROVINCE`** |
| China (nacional) | Ministry of Education (PRC) | nacional, pero sólo emitió **guías** | 🔴 **`NO-MANDATE`** |

🔵 **O sea: la UAE sostiene la frase y China no.** Lo que Pekín hizo —*«the first provincial-level
region in China to launch compulsory comprehensive AI education»*, mínimo **8 horas de clase por
ciclo** desde **2025-26**— es un mandato real y vigente, pero **municipal**. Lo que el Ministerio
chino emitió en diciembre de 2024 y mayo de 2025 son **guías** (*General AI Education Guide for
Primary and Secondary Schools, 2025 Edition*), y una guía no es un mandato.

⚠️ **Por qué esto importa comercialmente y no es una nota al pie:** un producto K-12 que se cotiza
«para el mandato nacional de China» tiene, medido, un mercado direccionable **municipal**. El error
no es de magnitud, es de **unidad** — y es el mismo error que `P228` ya había encontrado en otro eje
(ordenar una cuota en USUARIOS contra una en INSTITUCIONES).

## 🆕 P262 — tres preguntas, tres columnas

> **P262.** Un mandato curricular se declara en **tres** columnas y ninguna se infiere de otra:
> **NIVEL** (¿quién obliga?), que sale del **alcance de la autoridad que firma** y nunca del titular
> de la nota; **VIGENCIA** (¿obliga ya, está anunciado para un ciclo futuro, o es sólo una guía?),
> que exige el **ciclo** de entrada en vigor; y **ENTREGA** (¿asignatura propia o contenido integrado
> en materias que ya existen?), que se lee del **texto del instrumento**.
> Sin autoridad leída, sin ciclo, o sin instrumento, la respuesta es **`NO-CLAIM`**, nunca el valor
> optimista.

Y la regla de `P251` en este eje: **una búsqueda propia que no encontró mandato es silencio, no
ausencia.** Por eso la ausencia se parte en dos veredictos distintos:

| Caso | Instrumento que midió la ausencia | Veredicto |
|---|---|---|
| **EEUU federal** | la competencia curricular es **estatal**; 134 proyectos en 31 estados en 2026, **ninguno federal** | 🟢 **`NO-MANDATE`** (ausencia **medida**) |
| **Brasil**, **Chile** | — *(buscado en este pase, no encontrado)* | ⚠️ **`NO-CLAIM`** (hueco **declarado**) |

🔵 **La diferencia no es cosmética:** `NO-MANDATE` se puede cotizar, `NO-CLAIM` manda a medir.

## 🆕 P263 — una regla corregida dentro de UN instrumento no es todavía una regla de la base

🔴 **El aporte más incómodo de este pase es contra sí mismo.** La primera versión de `region_ok()`
hacía `strip()` del valor **antes** de preguntar por el vocabulario cerrado, así que `"APAC "` con
espacio salía **aceptado**. 🔵 **Eso es exactamente `P248`** — el defecto que el pase 82 encontró y
corrigió en `p243-frontmatter-coverage/`.

> **P263.** Una regla que se corrigió **dentro** de un instrumento sigue disponible para que el
> próximo instrumento la reintroduzca. Mientras la pregunta no viva en la **librería compartida**
> (`compose/code/lib/`), cada instrumento nuevo la vuelve a implementar y vuelve a elegir el bug.
> La prueba de que la regla es de la base no es que un archivo la cumpla: es que **un archivo nuevo
> no pueda incumplirla**.

⚠️ **Acreditación honesta:** esto es `P237`/`P252` otra vez (un clasificador compartido en vez de uno
por instrumento; una corrección viaja a todos los archivos), pero ninguna de las dos lo había dicho
sobre una regla **ya corregida**. `P263` es ese caso.

## La asimetría que deja la medición, y es la oportunidad

| Pregunta | Medido en las 12 filas |
|---|---|
| ¿Cuántos tramos **obligan hoy**? | **4** (UAE, Pekín, India Clases 3-8, CABA) |
| ¿Cuántos de esos son de alcance **nacional**? | **2** (UAE, India Clases 3-8) |
| ¿Cuántos obligan hoy una **asignatura propia** de IA? | 🔴 **0** |
| ¿Cuántos entregan **integrado** en materias que ya existen? | **4 de 4** |

🔵 **La lectura que esto habilita:** el producto que el mandato vigente pide **no** es un curso de IA.
Es material de IA **dentro** de lengua, matemática, ciencias y de la asignatura de informática que ya
está en el horario —el instrumento de la UAE lo dice literalmente: integrado en *Computing, Design and
Innovation*, **«without extending instructional hours»**; el de India, *«interwoven into existing
subjects, not taught as a separate discipline»*; el de Pekín permite **las dos** formas—. 🔴 **La
asignatura propia existe, pero está en el futuro: India la anuncia para Clases 9-10 en 2027-28, y
Georgia y Mississippi para fines de la década.**

## Reproducir

```sh
cd compose/code/p262-mandate-level
python3 test_classify.py          # 47/47  (Python 3.11.15, pase 88)
```

El barrido no tiene canal de red: las 12 filas de `rows.tsv` se escribieron a mano desde la fuente
citada en la columna `instrument`, y el módulo sólo las **clasifica**. 🔵 **Es a propósito: el eje de
este instrumento es documental, y un `curl` no contesta «¿quién firma?».**

⚠️ **Cota declarada:** `rows.tsv` **no es un censo**. Son las jurisdicciones que la búsqueda de este
pase alcanzó; que una no esté no dice nada sobre ella (`P251`). Las dos que se buscaron y no
aparecieron están escritas como `NO-CLAIM` en vez de omitidas, que es la diferencia entre un hueco
informado y un silencio que se lee como cobertura.
