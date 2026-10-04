---
industry: education
region: Global
updated: 2026-10-04
---

# P170 — Barrido de licencia por ref `HEAD` (pase 64 del 2026-10-03)

Ejecuta la **acción 1 del pase 64**: medir la licencia de **las 200 filas `org/repo` distintas** que
cita `agents/top.md`, leyendo el archivo de licencia en vez de inferirlo.

## El cambio de instrumento, que es el hallazgo

La acción venía escrita como *«`LICENSE`, `LICENSE.md`, `LICENSE.txt` y `COPYING` en `main` y
`master`»*. **Esa especificación tiene una ceguera, y el pase anterior ya había publicado el
contraejemplo sin notarlo:** `frappe/education` declara su licencia en
`develop/license.txt` — rama que no es `main` ni `master`, y nombre en minúsculas, que
`raw.githubusercontent.com` **distingue**.

`raw.githubusercontent.com` resuelve la ref literal **`HEAD`** a la rama por omisión del repo,
**cualquiera sea su nombre**. Con eso la dimensión «rama» DESAPARECE del instrumento: 14 nombres de
archivo × **1 ref** cubren `main`, `master`, `develop`, `trunk` y cualquier otra, mientras la
especificación original —4 nombres × 2 ramas— deja `develop` afuera por construcción (**P170**).

## El control de alcanzabilidad, que separa tres cosas y no dos

Un 404 en los 14 nombres significa dos cosas distintas que no se pueden mezclar: *«el repo existe y
no cede licencia»* y *«no llego al repo»*. El script resuelve la ambigüedad pidiendo
`HEAD/README.md` y 7 rutas más: si alguna da 200, el repo es alcanzable y la **ausencia está
medida**; si todas dan 404, el estado es `UNREACHABLE` y **no se afirma nada sobre su licencia**.

| Estado | Significado | n (de 200) |
|---|---|---|
| `LICENSED` | archivo de licencia leído, con tamaño y familia | **160** |
| `UNLICENSED` | repo alcanzable, **ausencia medida** en 14 nombres | **32** |
| `UNREACHABLE` | 404 por este canal; sin afirmación de licencia | **8** |

## Correr

```sh
./sweep_headref.sh <org/repo>                       # una fila
xargs -P 6 -n 1 ./sweep_headref.sh < slugs.input.txt  # el barrido completo
```

Salida TSV: `slug · estado · archivo · bytes · familia`.

## El defecto de clasificación que este pase corrigió

Un classificador que hace `grep` sobre **todo el cuerpo** etiqueta **GPL-3.0 como AGPL-3.0**, porque
el §13 del texto de GPL-3.0 se TITULA *«Use with the GNU Affero General Public License»*. Se detectó
contra `frappe/erpnext`, que el pase 63 había leído —bien— como GPL-3.0. **La clasificación se hace
sobre el TÍTULO (primeras 12 líneas), no sobre el cuerpo** (**P171**).

## Archivos

- `sweep_headref.sh` — el instrumento (ref `HEAD`, 14 nombres, control de alcanzabilidad)
- `result.2026-10-03.tsv` — las 200 filas medidas con `HEAD` (**autoritativo**)
- `result-branchlimited.2026-10-03.tsv` — las mismas 200 con el instrumento acotado a `main`/`master`,
  que se conserva como **control negativo**: 7 de 160 licenciados quedan mal etiquetados ahí
- `slugs.input.txt` — el denominador, extraído de `agents/top.md`

## Reserva de denominador, declarada

De los 200 slugs, **2 no son filas de datos**: `owner/repo` sale del texto de un comando `grep`
citado en una tabla de método, y `your-username/SafeTutors` sale de la PROSA que describe el badge
sin editar de `SafeTutors` (defecto que el pase 51 ya había caracterizado bien). **No son datos
sucios de la KB: son un artefacto de MI extractor de slugs.** El denominador real es **198**.
