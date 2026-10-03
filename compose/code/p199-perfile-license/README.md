---
industry: education
region: Global
updated: 2026-10-03
---

# `p199-perfile-license` — el instrumento POR ARCHIVO que P186 dejó pedido, y el alcance que NO se puede cerrar (acción 3 del pase 68, pase 69 del 2026-10-03)

Ejecuta la **acción 3 del pase 68**, con el recorte que la acción impuso: **no barrer árboles
completos** —el listado de directorio sólo está abierto por WebFetch y no es scripteable— sino tomar
las **piezas de alcance declarado** (hoy 2) y **leer los encabezados de sus archivos de entrada**,
publicando la licencia **más restrictiva** encontrada como la cotizable.

## Caso 1 — `UCL-INGI/INGInious`: la superficie de entrada está limpia y el alcance sigue abierto

| Capa | Qué dice |
|---|---|
| `LICENSE` (34.764 B) | *«Most of the files … are distributed under the GNU AGPL v3 licence … If it is not the case, this is clearly indicated in the files»* |
| superficie de entrada | 🟢 **7 de 7** archivos con el mismo encabezado, **0 excepciones**; `pyproject.toml` → `license = {text = "AGPL 3"}` + clasificador AGPL v3 |
| `COPYRIGHTS` (622 B) | 🔴 *«Some other files are entirely made by third parties, and distributed with other licences»* — **y no los enumera** |

🔴 **Dos resultados, y el segundo es el que manda.**

1. 🟢 **El titular, corregido.** Esta KB publicaba `FSF → NOT-APPLICABLE` en cuatro archivos. El
   `COPYRIGHTS` dice *«Copyright (c) 2014-2026 Anthony Gégo, Guillaume Derval and Pierre Reinbold»*.
   🔵 **Capa nueva para la escalera de **P197**: un archivo de TITULAR dedicado manda sobre el
   boilerplate del `LICENSE` para la pregunta del titular.**
2. 🔴 **El alcance NO se puede cerrar.** Las excepciones existen por declaración propia, están
   marcadas sólo dentro de los archivos y no hay manifiesto. 🟢 **Lo cotizable: *AGPL-3.0 en la
   superficie de entrada medida (7/7, 0 excepciones), con archivos de terceros de otras licencias
   existentes por declaración del proyecto y sin enumerar*** (**P201**).

⚠️ **`setup.py` da 404: el proyecto ya no lo tiene. Se declara en vez de contarlo como excepción.**

## Caso 2 — `1EdTech/openbadges-specification`: la licencia es por VERSIÓN, y una versión viva CALLA

| Ruta | Estado |
|---|---|
| `LICENSE` · `LICENSE.md` · `NOTICE` (raíz) | 🔴 **404** las tres |
| `ob_v3p0/license.md` | 🟢 **200** — *Specification Document License* de IMS Global: **niega derivados** |
| `ob_v2p0/index.md` | 🟢 **200** — **la versión EXISTE** |
| `ob_v2p0/license.md` | 🔴 **404** — **silencio, no ausencia de versión** |
| `ob_v2p1` · `ob_v1p1` · `ob_v1p0` · `ob_v3p1` · `clr_v2p0` | 404 en los dos nombres — **no se afirma que existan** |

🔵 **Por la regla de la acción, lo cotizable del repo es «niega derivados».** ⚠️ **Y «la licencia del
repo» queda escrita como frase mal formada para esta clase de repositorio.**

## Reservas declaradas

- 🔴 **Esto NO es un barrido de árbol.** Mide la superficie de entrada, que es lo que la acción
  acotó. ⚠️ **Un archivo de tercero en el interior del árbol no lo ve, y el `COPYRIGHTS` dice que
  hay. Es la acción 3 del pase 70.**
- ⚠️ **El detector de licencia en encabezado es por expresión regular sobre las primeras 40 líneas.**
  Un encabezado que nombre su licencia más abajo no se detecta. 🟢 **Mitigado en este caso porque los
  7 archivos traen el mismo encabezado corto y se leyó uno verbatim.**
- ⚠️ **No se probó `main`/`master` por archivo: se usó la ref `HEAD`**, que es la regla de **P170**.

## Correr

```sh
./perfile.sh <owner/repo> <archivo> [archivo ...]
./perfile.sh UCL-INGI/INGInious pyproject.toml inginious/__init__.py inginious/frontend/app.py
```

## Archivos

- `perfile.sh` — encabezado por archivo de entrada, una línea por archivo (**autoritativo**)
- `result.inginious.2026-10-03.tsv` — las 8 lecturas del caso 1
