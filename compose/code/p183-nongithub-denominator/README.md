---
industry: education
region: Global
updated: 2026-10-03
---

# `p183-nongithub-denominator` — la capa de PAQUETE, y el denominador que nadie había medido (pase 66 del 2026-10-03)

Ejecuta la **acción 1 del pase 65**: *«barrer el PAYLOAD de las 249 filas de `agents/top.md` SIN URL
de GitHub, que llevan 14 pases fuera de todo denominador de licencia»*, con la condición que la propia
acción impuso — **declarar el denominador exacto antes de empezar.**

## La cifra 249 no se puede reproducir, y por eso lo primero es el instrumento

🔴 **El **249** nunca salió de un instrumento versionado** (regla 1 de **P126**). Medido hoy, la
pregunta *«filas sin URL de GitHub»* no tiene UNA respuesta: tiene dos capas, y la diferencia no es
cosmética.

| | Qué se cuenta | n |
|---|---|---|
| **Capa 1** | filas de dato de **todas** las tablas (98 bloques: encabezado + separador + filas) | **578** |
| ídem, sin `github.com` | | **292** |
| **Capa 2** | filas en tablas de **ENTIDAD** — las que declaran pieza, repo, paquete, licencia o ★ | **452** |
| ídem, sin `github.com` | 🔵 **el denominador real** | **174** |
| de esas, con paquete **declarado por su registro** | alcanzables por npm/PyPI | **21 filas → 18 paquetes** |
| de esas, sin paquete y sin repo | 🔴 **no medibles por NINGÚN canal de esta KB** | **153** |

🟢 **Las otras 118 filas sin `github.com` son filas de tablas de MÉTODO** (`Magnitud · Valor`,
`Estado · n · %`, `Clase · Qué es`). Preguntarle la licencia a una fila de `Magnitud · Valor` es un
error de categoría, y contarla infla el denominador con algo que no puede estar licenciado nunca.
⚠️ **La capa accionable es el 10 % de lo que la cifra sugería.**

## D4 — la pregunta de la FORMA no es la pregunta de la DECLARACIÓN

La primera construcción cosechó todo *token* entre comillas invertidas con **forma** de paquete
npm/PyPI. Devolvió **46** filas, y leídas a mano la mayoría **no eran paquetes**: nombres de *tool*
MCP (`server_status`, `search_data`, `record_evidence`, `sisu_plan`), ajustes de Moodle
(`posting_policy`, `use_rubric_for_grading`), nombres de rama (`upgrade-mcp-v2`, `new-version`) y
nombres cortos de repo (`lindsay-cheng`, `mcp-usc`). **Todos tienen la forma. A ninguno se le puede
preguntar un registro.**

🔵 **Es **P171** en la capa de paquete: se clasifica sobre una DECLARACIÓN, nunca sobre una forma.**
Una fila nombra un paquete cuando **cita el registro que lo sirve** (`registry.npmjs.org`,
`npmjs.com/package`, `pypi.org/project`) o marca el canal explícitamente como `` `nombre` (npm) ``.
Con esa regla: **46 → 21**. La construcción por forma se conserva como control negativo fechado en
`shape-only.NEGATIVE-CONTROL-2026-10-03.py`.

## El resultado: la hipótesis de la acción se resuelve en su SEGUNDA rama, y con holgura

La acción escribió la hipótesis falsable así: *«si el reparto de clases de **P179** en esa capa se
parece al de ésta (5 identificador / 2 cesión de 7), entonces "identificador sin texto" es la forma
NORMAL de declarar licencia en la capa de paquete y hay que cambiar lo que esta KB publica en la
columna Licencia para TODA esa capa; si predomina la cesión con texto, el problema es específico de
los repos de GitHub sin archivo y la capa de paquete está sana.»*

🟢 **Medido: predomina la cesión con texto. La capa de paquete está SANA.**

| Capa | Pregunta | Identificador sin texto | Texto de licencia presente |
|---|---|---|---|
| repos de GitHub **sin archivo** de licencia (pase 65) | `package.json`, `setup.cfg`, header | **5 de 7 — 71 %** | 2 de 7 |
| **paquetes de registro** (este pase) | registro + *tarball*/sdist bajado | **6 de 23 — 26 %** | 🟢 **17 de 23 — 74 %** |

🔵 **Conclusión operativa: NO hay que reescribir la columna Licencia de la capa de paquete.** El
problema de **P179** es **específico de los repos de GitHub cuyo árbol no tiene archivo de licencia**,
y el artefacto publicado no hereda esa enfermedad: **la hereda al revés.** `npm pack` y los
constructores de sdist **incluyen el archivo de licencia cuando existe en el árbol**, así que el
*tarball* responde la pregunta de **P179** (¿hay texto?) con **una** llamada al registro y **una**
descarga, contra **14** sondas a `raw` por nombre de archivo.

⚠️ **Y para 2 de los 18 el registro es el ÚNICO canal que existe:** `opencode-sit` y
`aicourse-mcp-server` **no declaran repositorio**, así que la pregunta del archivo no se puede ni
formular — y el *tarball* la contesta igual (el primero **con** texto de 1.056 B, el segundo **sin**).

### Las 6 sin texto, que son la lista corta que queda

`@ink-waffle/moodle-mcp` · `@ink-waffle/sisu-mcp` · `aicourse-mcp-server` · `clawed` (npm) ·
`educhain` (npm) · `frappe-mcp-server` (npm).

🟢 **Las dos de `@ink-waffle` REPRODUCEN la medición del pase 65** —identificador MIT en el registro,
cero bytes de otorgamiento en el artefacto— **por un instrumento escrito de cero y sin ver el
anterior.** Es la reproducción independiente que **P126** pide.

## D5 — un NOMBRE no es un PAQUETE: la primera construcción salía en el primer canal que contestaba

🔴 **La primera versión consultaba npm y `exit 0` en cuanto obtenía respuesta.** Dos filas de esta KB
citan un paquete de **PyPI** cuyo nombre **también existe en npm como una subida sin relación**, así
que el *build* npm-first publicó la licencia del artefacto equivocado bajo el nombre de la fila.
Corregido, el instrumento consulta **los dos** registros y emite **una línea por canal**: 18 nombres →
**23 mediciones**, y **5 nombres viven en los dos registros**.

| Nombre | npm | PyPI | Lectura |
|---|---|---|---|
| **`educhain`** | **ISC** 1.0.0, 🔴 sin texto | **MIT** 0.4.0, texto 1.092 B | 🔴 **licencias DISTINTAS bajo un nombre.** La fila de esta KB es el proyecto Python (`satvik314/educhain`): quien corra `npm i educhain` se lleva ISC y ningún texto |
| **`frappe-mcp-server`** | **ISC** 0.6.0, 🔴 sin texto | **MIT** 1.2.0, texto 1.065 B | 🔴 **ídem, y aquí la fila cita npm** — o sea la fila cita el canal peor licenciado de los dos |
| **`clawed`** | MIT 0.0.1, 🔴 sin texto | MIT **9.18.2026.1**, texto 1.078 B | ⚠️ misma licencia, **brecha de versión que delata una reserva de nombre** en npm. La fila cita `(PyPI)`: correcto |
| `canvas-lms-mcp` | MIT 1.30.0, texto | MIT 0.1.2, texto | 🟢 benigno |
| `moodle-cli` | MIT 0.10.0, texto | MIT 0.4.2, texto | 🟢 benigno |

⚠️ **Lo que esto obliga a la KB: una fila que nombra un paquete tiene que nombrar su CANAL.** Sin
canal, el nombre es ambiguo entre dos artefactos con dos licencias, y en 2 de 5 casos medidos lo es
de verdad. El *build* npm-first se conserva en `npm-first.NEGATIVE-CONTROL-2026-10-03.sh`.

## Reservas declaradas

- ⚠️ **Una fila que nombra el paquete entre comillas invertidas y describe el registro en PROSA sin su
  URL no se cosecha.** Hay **un** caso conocido, `@timeback/caliper` (línea 3450), cuya licencia ya
  estaba medida en el pase 64 (*no declara licencia*). La regla se prefiere así: un falso negativo
  declarado es más barato que los 25 falsos positivos de **D4**.
- ⚠️ **Las 153 filas `NO-CHANNEL` siguen sin medir, y ahora se sabe POR QUÉ:** no tienen repo ni
  paquete. Son especificaciones, estándares, marcas, despliegues institucionales y lápidas. **No es
  un pendiente de barrido: es una propiedad de la fila.** Lo accionable es decidir qué columna
  Licencia corresponde a una fila que no es software.
- ⚠️ `codeload.github.com` **403** y `api.github.com` **403** por el proxy de esta corrida (medido),
  igual que en el pase 65. `registry.npmjs.org`, `pypi.org` y `raw.githubusercontent.com` dan **200**.

## Correr

```sh
python3 denominator.py agents/top.md           # el reporte de las dos capas
python3 denominator.py agents/top.md --tsv     # las 174 filas de capa 2, clasificadas
./sweep_registry.sh <paquete>                  # un paquete, los dos registros
xargs -P 4 -n 1 ./sweep_registry.sh < pkgs.input.txt   # los 18
```

## Archivos

- `denominator.py` — el denominador de dos capas y la detección por DECLARACIÓN (**autoritativo**)
- `shape-only.NEGATIVE-CONTROL-2026-10-03.py` — **control negativo fechado de D4** (devuelve 46)
- `sweep_registry.sh` — registro + *tarball*/sdist, un canal por línea (**autoritativo**)
- `npm-first.NEGATIVE-CONTROL-2026-10-03.sh` — **control negativo fechado de D5** (18 líneas, pierde
  los 5 nombres que viven en los dos registros)
- `pkgs.input.txt` — los 18 paquetes, extraídos por `denominator.py --tsv`
- `result.2026-10-03.tsv` — las 23 mediciones (**autoritativo**)
