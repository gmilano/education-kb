---
industry: education
region: Global
updated: 2026-10-05
---

# `p324-corpus-upstream-cession` — «NC hasta prueba en contrario» era la direccion segura y la CATEGORIA equivocada

> Nuevo en el **pase 104 del 2026-10-05**. Cierra la deuda que los pases **102** y **103** dejaron
> abierta: `amber` (45 archivos) y `ncte` (29), **74 de los 111** archivos de corpus que
> `rosewang2008/edu-convokit` redistribuye. El pase 103 no pudo correrla —canal denegado—; este
> pase **si**, y el resultado **no** es el que la receta asumia.

## Lo que la receta del pase 102 decia, y por que habia que medirlo

`R-102-PROCEDENCIA-DE-CORPUS` trata a `amber` y `ncte` como **`NC` hasta prueba en contrario**,
*«que es la direccion segura»*. 🟢 **La direccion era correcta.** 🔴 **La categoria no**, y la
diferencia decide un contrato.

Datos crudos: [`result.2026-10-05.tsv`](result.2026-10-05.tsv).

| corpus | n | upstream | cesion del titular | alcance | identidad | veredicto |
|---|---|---|---|---|---|---|
| `talkmoves` | 29 | `SumnerLab/TalkMoves` | `CC BY-NC-SA 4.0` (`LICENSE` **20.849 B** + `README`) | **corpus** | 29/29 nombres | **no comercial** |
| 🔴 `amber` | 45 | `laurenceholt/amber` | **NINGUNA** | — | **45/45 nombres** | 🔴 **no redistribuible** |
| 🔴 `ncte` | 29 | `ddemszky/classroom-transcript-analysis` | `MIT` (1.068 B) — **solo codigo** | **no alcanza al corpus** | no verificable por nombre | 🔴 **no redistribuible** |

🟢 **El pase 102 se reproduce EXACTO:** `SumnerLab/TalkMoves` da `Attribution-NonCommercial-ShareAlike
4.0`, `LICENSE` de **20.849 B**, al byte.

## `P324` — «sin cesion» es MAS restrictivo que `NC`, no menos

🔴 **`amber` no tiene licencia de ninguna clase.** Aserido por **dos canales independientes**:

1. **Arbol enumerado** (canal `P275`): **46** rutas, **0** archivos de licencia.
2. **Sonda de 7 nombres** en la raiz: `404` en los **7**.

Y el `README` del upstream —leido entero— **no contiene una sola linea de terminos**: describe la
grabacion (XQ Institute, 2022, sesiones de tutoria de ~1 h, un mismo tutor, *«students were
typically in 8th or 9th grade»*) y el esquema JSON. Nada mas.

**`P324`**: *tratar un corpus sin cesion como **`NC`** subestima la restriccion. `NC` **es** una
licencia: concede uso no comercial y se puede cumplir. **La ausencia de cesion no concede nada** y
no se puede cumplir — el titular conserva todos los derechos por defecto. Una receta que escribe
«NC hasta prueba en contrario» le da al lector un permiso que nadie otorgo.*

🔵 **Para un entregable la diferencia es operativa, no semantica:** con `NC` un estudio puede
construir una demo interna y negociar una licencia comercial con el titular. **Sin cesion no hay
demo interna**: la redistribucion que ya ocurrio es la que hay que deshacer, y el titular a quien
pedirle permiso es, en el caso de `amber`, el de **grabaciones de menores de 8º y 9º grado**.

## `P325` — una cesion puede ser correcta, legible y NO alcanzar al dato

🔴 **`ncte` es el caso mas facil de leer mal, porque aca SI hay un `LICENSE` y es impecable:**
`MIT (c) 2022 Dora Demszky`, 1.068 B, leido del payload. 🔴 **Y no cubre las transcripciones.**

El arbol enumerado del upstream tiene **10 archivos** y **ninguno** es una transcripcion:
`run_classifier.py`, `run_classifiers.sh`, `requirements.txt`, `transcript_issues.txt`,
`coding schemes/` (3 PDF) y el `README`. **El MIT cubre *«the Software»*, y el software esta todo
ahi: el corpus no.**

🔴 **Lo que el `README` del titular si declara es un ACCESO CONTROLADO, no una cesion abierta:**

> *«**EACH user** who would like to access the dataset should fill out this form: […] Once you fill
> it out, the Google Drive folder will be shared with you automatically.»*

Y los metadatos asociados estan en **ICPSR** (archivo de investigacion de acceso restringido).

**`P325`**: *un repo puede traer una cesion valida, permisiva y correctamente redactada que **no
alcanza al dato**, porque el dato no esta en ese repo. Y cuando el titular distribuye el corpus
por **formulario por usuario**, redistribuirlo publicamente no es un desajuste de licencia: **quita
una compuerta de acceso que el titular instalo a proposito**.*

🟢 **Esto corrige, ademas, la pista del pase 103 en la direccion que `P314` exige.** El pase 103
habia encontrado `CC BY 4.0` para NCTE por **canal secundario** y, correctamente, **no lo publico**.
Medido de primera mano: **el titular no declara `CC BY 4.0` en ninguna parte de su repo.** La pista
era falsa y la cautela del pase 103 estaba justificada.

## Identidad: medida donde se puede, y declarada donde no

🟢 **`amber`: 45 de 45.** Los nombres de `data/amber/` de `edu-convokit` y los de
`raw-transcripts/` del upstream son **identicos**, interseccion exacta **45**, diferencia simetrica
**0** (`4244.json`, `4245.json`, …). No hay inferencia: son los mismos archivos.

🔴 **`ncte`: NO verificable por nombre, y se dice.** El upstream **no publica** las transcripciones
(estan tras el formulario), asi que no hay lista contra la cual comparar. Los 29 archivos de
`edu-convokit` son `10.csv`, `11.csv`, … — numeracion compatible con los `OBSID` que el `README`
del titular describe, **pero compatible no es identico**. La identidad de `ncte` descansa en que
**el propio redistribuidor lo enlaza de primera mano** (`docs/source/tutorial_ncte.ipynb` apunta a
`github.com/ddemszky/classroom-transcript-analysis`), no en una huella de archivos.

🟢 **Y el upstream NO se adivino del nombre del directorio.** Se leyo de los notebooks del
redistribuidor, que enlazan cada dataset. Adivinar `amber` → *«algun repo llamado amber»* habria
sido el error de identidad que `P306` y `P253` ya le costaron a esta base.

## Consecuencia sobre lo publicado

🟢 **La fila de `edu-convokit` en `agents/top.md` y `repos/foundations.md` sigue siendo CORRECTA:
`MIT`, y el MIT es la licencia del codigo.** Lo que cambia es el veredicto de la receta:

🔴 **Los 111 archivos de `data/` quedan AHORA resueltos de punta a punta, y ninguno es
redistribuible en una entrega comercial:** 29 son `NC` (`talkmoves`), **74 no tienen cesion
alguna** (`amber` 45 + `ncte` 29). La instruccion operativa del pase 102 —*«usar la libreria (MIT)
y NO embarcar `data/`»*— **se confirma, y ahora se apoya en los tres corpus y no en uno**.

## Invocacion

```sh
WORK=/tmp/p324 bash resolve_upstream.sh    # enumera, resuelve upstream, lee cesion del payload
```

## Limites declarados

- 🔴 **`ncte` no tiene identidad por huella de archivo** (arriba). Es el limite mas fuerte de este
  modulo y no se tapa: el veredicto `NO-REDISTRIBUIBLE` **no depende** de la identidad —se sostiene
  solo con que el titular no cede el corpus por ningun canal publico—, pero la afirmacion *«son
  LAS transcripciones NCTE»* descansa en el enlace del redistribuidor.
- 🔴 **`amber`: ausencia de cesion, no ausencia de derechos.** Que no haya archivo de licencia no
  dice que nadie sea titular: dice lo contrario. Y este modulo **no** resuelve si hubo
  consentimiento informado de los participantes —menores— para redistribucion: eso no esta en el
  repo y no se infiere.
- 🔴 **Los 3 `.zip` y `annotated_data.csv`** (4 de los 111) no se abren: un `.zip` exige descargar
  el blob y este modulo trabaja con el arbol y el payload de texto. Se asume que replican los
  mismos tres corpus **y se declara como supuesto**, no como medicion.
