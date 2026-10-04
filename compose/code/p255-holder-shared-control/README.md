---
industry: education
region: Global
updated: 2026-10-04
---

# `p255-holder-shared-control` — la pregunta del TITULAR no tenía control compartido, y el payload que lo prueba es GPL-2.0 (pase 85 del 2026-10-04)

## El hallazgo en una línea

🔴 **Esta base pregunta «¿quién es el titular?» en TRES instrumentos, y hasta este pase los tres
daban TRES respuestas distintas sobre el mismo payload GPL.**

| Instrumento | Pase | Qué hace con el titular de un payload GPL | Veredicto |
|---|---|---|---|
| `p184/extract_holder.py` | 66 | `NOT-APPLICABLE (GPL: holder not in the license text by construction)` — **con compuerta de familia** | 🟢 **CORRECTO** |
| `p198/holder_of.sh` | 69 | filtra **UNA** cadena fija: `Copyright \(C\) [0-9]{4} Free Software Foundation` | ⚠️ **correcto sólo en GPL-3.0** |
| `p204/sweep_payload_license.sh` | 70 | `grep -m1 -i copyright`, **sin compuerta alguna** | 🔴 **INCORRECTO siempre** |

## La medición que lo abre, sobre payloads REALES y no sobre fixtures

🟢 **El alta de este pase es `OpenEMIS/core`, y su licencia es GPL-2.0 — la primera GPL-2.0 real
que esta base mide.** Ahí se ve lo que ninguna GPL-3.0 podía mostrar:

```
GPL-2.0 (OpenEMIS/core, 15.518 B, sha256:b6f03c6715ee7b0f)
  Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.o...
            ^^^^^^^^^^^^ DOS años separados por coma
```

🔴 **El filtro de `p198` pide `[0-9]{4}` seguido de espacio y `Free`. En GPL-2.0 hay `1989, 1991`,
así que el patrón NO coincide y la línea PASA.** `p198` reporta a la **Free Software Foundation**
como titular de OpenEMIS. Verificado ejecutando su regex verbatim contra el payload:

```
gpl2.txt -> Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
```

🔴 **Y en GPL-3.0, donde el filtro SÍ atrapa la línea de la FSF, el ancla
`^[[:space:]]*(Copyright|\(c\))` cae en PROSA DEL CUERPO ya plegada:**

```
gpl3.txt -> copyright on the Program, and are irrevocable provided the stated
```

**Una oración de la sección 8 reportada como titular.** Los dos resultados están mal, en
direcciones opuestas, y la causa es la misma.

## La causa, y es la que `P237` ya había resuelto para la FAMILIA

🔵 **Un titular está presente en el texto de la cesión POR CONSTRUCCIÓN en MIT / BSD / ISC / 0BSD,
y AUSENTE POR CONSTRUCCIÓN en toda la familia GPL, en Apache-2.0, MPL-2.0, ECL-2.0, Unlicense y
CC0.** En esos textos la única línea de copyright pertenece al autor **de la licencia** —la FSF,
la ASF—, nunca al proyecto. Así que la pregunta sólo es sana **si se compuerta por la FAMILIA
ANTES de leer una línea**, que es exactamente lo que `p184` hace desde el pase 66.

🔴 **`P197` es por qué esto es un ARCHIVO y no una nota al pie: una corrección sobrevive sólo si
el instrumento que re-mide la conoce.** `p184` lo sabía. Los dos instrumentos escritos DESPUÉS
—`p198` en el pase 69, `p204` en el pase 70— no heredaron nada, porque no había nada que heredar:
`lib/license_family.sh` es el control compartido de la **familia** (`P237`, pase 77) y **nunca
tuvo un `holder_of`**.

🟢 **Ahora lo tiene**, y `p204` lo consume en vez de reescribirlo.

## Un tercer trampa que el payload real tiene y ninguna fixture pequeña tendría

En el `gpl-3.0-moodle-COPYING.txt` que esta base YA guardaba desde el pase 66, la línea **635**
dice literalmente:

```
    Copyright (C) <year>  <name of author>
```

🔴 **Es el apéndice «How to Apply These Terms».** Un ancla sin cota puede devolver un
**placeholder** como titular. El `head -40` lo deja afuera, y la suite lo pinea.

## 🔴 Y el instrumento nuevo falló su primera prueba de verdad — en el BARRIDO, no en la suite

**Tercera vez que esto le pasa a esta base, y se registra igual que las anteriores.**

El primer corte de la compuerta exigía un **dígito** justo después de `Copyright (c)`. Con eso:

🔴 **`katoj65/emis` —el EMIS del *ministry of education in Uganda (MOU)*— devolvió
`NO-HOLDER-LINE`**, y su texto MIT de **1.090 B** dice:

```
Copyright (c) Jonathan Reinink <jonathan@reinink.ca>
```

**SIN AÑO.** La compuerta ocultó el titular — **y el titular era justamente el hallazgo**, porque
`Jonathan Reinink` es el autor de **Inertia.js / Ping CRM**, no de un EMIS ministerial ugandés:
un `HOLDER-UNRELATED` de libro, licencia **HEREDADA** y no otorgada (`P184`).

🔵 **Una compuerta que suprime la señal que `P184` existe para levantar es peor que no tener
compuerta.** Corregida: la prueba es por **NOMBRE**, no por año — se quitan la palabra clave, el
`(c)`, los años y la puntuación, y se pregunta si sobrevive un token alfabético. **11/11 → 13/13.**

## La cota de este hallazgo, medida y no estimada

🟢 **En datos ya persistidos el daño son DOS filas**, las dos en `p204/result.2026-10-03.tsv`:

| Fila | Lo que decía la columna `holder` | Lo que dice ahora |
|---|---|---|
| `classroomio/classroomio` | 🔴 `Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>` | 🟢 `NOT-APPLICABLE (AGPL-3.0: …)` |
| `gibbonedu/core` | 🔴 `Copyright (C) 2007 Free Software Foundation, Inc. {http://fsf.org/}` | 🟢 `NOT-APPLICABLE (GPL-3.0: …)` |

⚠️ **Y la parte que importa más que el conteo: la PROSA del `README.md` de `p204` ya decía
«boilerplate FSF» en las dos filas.** El defecto estaba en el **DATO**, no en la lectura — y el
dato es lo que el compilador ingiere. Es el mismo signo que `P239` (una tabla que renderiza
perfecto y dejó de ser dato).

🟢 **Cero deriva en la re-medición:** los bytes y el `sha256` de las dos filas reproducen
exactamente los del pase 70 (`34.523` / `8486a10c4393` y `35.121` / `93178a43d6d3`), y el control
MIT `oliverhruby/edupage-mcp` sigue devolviendo su titular real (`Copyright (c) 2026 Oliver
Hrubý`, 1.070 B). **La compuerta no se volvió una negativa general**, que es el modo en que un
arreglo así destruiría `P184` entero.

## Dos defectos más de `p204`, cerrados de paso

1. 🔴 **La lista de nombres era de 5 y producía un FALSO «sin cesión».** `frappe/education` **sí**
   cede, en `license.txt` **minúscula**, y `p204` devolvía `404`. `p170` barre **14** nombres
   desde el pase 64; `p204` barría 5. Adoptadas las variantes en minúscula → `frappe/education`
   resuelve: **19 B**, `GPL-3.0 (declaracion)`.
2. 🔴 **El script salía con código `1` cuando todo había ido BIEN**, porque la última sentencia
   era un test que fallaba al haber encontrado licencia. Un barrido que miente en su código de
   salida no se puede encadenar ni poner en una compuerta. `exit 0` explícito.

## ⚠️ Lo que este instrumento NO compra, declarado

- 🔴 **No dice de quién ES el proyecto.** Dice si el ARCHIVO DE LICENCIA puede responderlo. Para
  un payload GPL la respuesta correcta es `NOT-APPLICABLE`, y eso deja la pregunta de titularidad
  **abierta**, no resuelta: hay que ir a los encabezados del código o al `composer.json`.
- 🔴 **No sustituye a `P184`.** `P184` pregunta si el titular PERTENECE al proyecto; `holder_of`
  sólo entrega la línea cuando la familia garantiza que la hay. Son dos capas, y la de `P184` va
  después.
- 🔴 **Sobre `UNCLASSIFIED` sigue preguntando**, acotado al bloque de título. Si un texto
  desconocido pone su titular en la línea 50, este instrumento no lo ve, y eso es deliberado:
  `P171` dice que un cuerpo que no se puede clasificar tampoco se puede anclar.

## Cómo se corre

```bash
cd compose/code/p255-holder-shared-control && ./test_holder_of.sh     # 13/13
cd compose/code/p204-writesurface-axis && ./sweep_payload_license.sh owner/repo ...
```

Las fixtures son payloads **reales**, traídos de los árboles que sus nombres indican, no escritos
a mano. `gpl-2.0-openemis-core-LICENSE.txt` es el que prueba el caso que ninguna GPL-3.0 muestra.
