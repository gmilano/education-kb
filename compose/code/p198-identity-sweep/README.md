---
industry: education
region: Global
updated: 2026-10-03
---

# `p198-identity-sweep` — la IDENTIDAD de los nombres de registro ÚNICO, y la cota real del hash del `LICENSE` (acción 1 del pase 68, pase 69 del 2026-10-03)

Ejecuta la **acción 1 del pase 68**: *«IDENTIDAD sobre las 16 filas `PKG-NAMED` de registro ÚNICO»*,
con las dos condiciones que la acción impuso — **declarar los nombres antes de empezar** y **pedir el
repositorio declarado, no leerlo del manifiesto**.

## Lo primero es el denominador, y el de la acción estaba mal

🔴 **La acción dice «16 nombres». Son 13.** Reproducido desde el archivo que el propio repositorio
versiona (`../p183-nongithub-denominator/pkgs.input.txt`, 18 nombres) menos los 5 de doble registro
que el pase 68 barrió:

| Magnitud | Valor |
|---|---|
| filas `PKG-NAMED` | **21** |
| nombres distintos | **18** |
| de doble registro (pase 68) | **5** |
| 🔵 **de registro único — el denominador de esta acción** | **13** |

🔵 **El «16» era `21 − 5`: un conteo de FILAS leído como conteo de NOMBRES** — el mismo error de
categoría que **P183** cometió y que esta acción venía a arreglar. ⚠️ **Por eso el reparto de abajo
NO se compara con el «4 de 5» del pase 68, como la acción misma prohibía.**

## Las cuatro clases, y la que sobraba

La acción pidió tres valores y agregó un cuarto (`IDENTITY-DECLARED-BUT-DEAD`) al ver dos repos
declarados con 404. 🔴 **La clase `IDENTITY-PROVEN` por hash, que la acción daba por buena, resultó
inservible y se re-definió por manifiesto** (**P199**, **P200**).

| Veredicto | n de 13 |
|---|---|
| 🟢 `IDENTITY-DECLARED` — trae `repository` y RESUELVE | **3** |
| 🔴 `IDENTITY-DECLARED-BUT-DEAD` — trae `repository` y da 404 en las 33 celdas | **2** |
| 🟢 `IDENTITY-PROVEN` — el manifiesto del ÁRBOL nombra el paquete | **3** |
| 🔴 `IDENTITY-UNKNOWN` | **5** |

🔵 **5 ≥ 3 → la hipótesis de la acción cae en su rama CARA: la columna *Identidad* es CONDICIÓN para
publicar una fila de paquete, con el valor `desconocida` escrito y no omitido.**

## D1 — un sondeo de un nombre de archivo FABRICA lápidas

🔴 **La primera construcción probaba `HEAD/README.md` y leía el 404 como «no resuelve». Sobre
`UCL-INGI/INGInious` —una pieza RECOMENDADA de esta base— eso da DEAD, y el repo está vivo: no tiene
`README.md`, embarca `README.rst`.** 🟢 **Corregido: `resolve_repo.sh` es una matriz de 33 celdas
(3 refs × 11 nombres) y sólo las 33 en 404 autorizan la palabra** (**P198**).

## D2 — el hash del `LICENSE` prueba la CLASE, no el ÁRBOL

🔴 **Dos colisiones medidas en esta misma tanda:** `openedx-mcp` y `tutor-contrib-openedxmcp`, dos
paquetes distintos, comparten `sha256:8d56b405468a` (34.524 B de AGPL-3.0 prístina); y borrándole
**sólo el nombre del titular** al `LICENSE` de `@yunmiao/studymate` y al de `@schoolexl/mentor`, los
dos quedan **byte a byte** iguales al de `opencode-sit` (1.056 B, `1126322e2cc8`).

🔵 **`holder_of.sh` es el instrumento que mide la cota: extrae la línea de copyright y separa
`HOLDER-BEARING` de boilerplate.** 🟢 **La medición del pase 68 se reprodujo exacta —1.056 B,
`1126322e2cc8`, byte a byte entre tarball y árbol—, así que lo que se corrige no es el número sino lo
que se concluyó de él.**

## Reservas declaradas

- 🔴 **Los 3 `IDENTITY-UNKNOWN` sin candidato se buscaron por UN canal: adivinar `owner/repo` desde el
  nombre y el *scope*.** ⚠️ **`api.github.com` da `403` por el proxy de esta corrida, así que la
  búsqueda de código de GitHub —el canal que los encontraría— no estuvo disponible. **No se afirma
  que no existan**: se afirma que no se declararon y que el nombre no los encuentra.**
- ⚠️ **La colisión se midió sobre 13 paquetes, no sobre las 200 filas de la base.** No se afirma
  cuántas celdas de licencia son boilerplate sin titular (acción 2 del pase 70).
- 🟢 **Hallazgo lateral que CONFIRMA al pase 65:** con el árbol de `@ink-waffle/*` por fin
  identificado, el `LICENSE` **tampoco existe en el árbol** (404 en 12 celdas cada uno) y el
  `package.json` declara `"license": "MIT"` con `"repository": null`. **El otorgamiento no existe en
  ninguna capa** (**P179**).
- ⚠️ `api.github.com` **403** y `codeload.github.com` **403** por el proxy (medido).
  `registry.npmjs.org`, `pypi.org` y `raw.githubusercontent.com` dan **200**.

## Correr

```sh
./resolve_repo.sh <owner/repo>                 # la matriz de 33 celdas (autoritativo)
./sweep_identity.sh <paquete> <npm|pypi>       # una fila de veredicto
while IFS=$'\t' read -r p c; do ./sweep_identity.sh "$p" "$c"; done < names.input.tsv
./holder_of.sh <paquete> <npm|pypi>            # bytes · sha256 · línea de titular
```

## Archivos

- `resolve_repo.sh` — la matriz de reachability (**autoritativo**, **P198**)
- `sweep_identity.sh` — registro + repositorio pedido + tarball, un veredicto por línea (**autoritativo**)
- `holder_of.sh` — la cota de identidad del hash: titular vs. boilerplate (**autoritativo**, **P199**)
- `names.input.tsv` — **los 13 nombres declarados antes de medir**
- `result.2026-10-03.tsv` — los 13 veredictos de la etapa de manifiesto
