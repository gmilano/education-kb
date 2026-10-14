---
industry: education
region: Global
updated: 2026-10-14
---

# `p1052-stale-absence` — una ausencia registrada puede estar CADUCA, y la pista suele estar ya en la página (pase 186 del 2026-10-14)

**Ejecuta `ACTION MK` ampliada.** La acción registrada en p185 preguntaba sólo una cosa: *¿qué
costó el filtro `NOISE` del limbo 2 de `P1049`?* 🟢 **La respuesta es `0` concesiones reales más**
*(`compose/code/p1049-bare-token-grant/noise_cost.py`,
[evidencia](../../../evidence/noise-cost.2026-10-14-p186.tsv))*. De `61` filas, sólo `3` tenían
alguna línea suprimida y las `3` ya estaban bien clasificadas.

🔴 **Pero ejecutarla produjo un hallazgo que las líneas suprimidas no contenían.** p185 cerró
[`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) como
`NO-badge-only`, con una regla que es **jurídicamente correcta**: *una insignia es una afirmación
sobre una licencia, no una licencia.* 🟢 **La regla se mantiene. Lo que cambia es su USO: el
repositorio sirve `LICENSE`, `1 068` B, texto `MIT` completo.** 🔵 **Una insignia no es un veredicto,
es una PISTA PARA RE-SONDEAR.**

## Las dos extremidades

| limbo | qué lee | por qué existe |
|---|---|---|
| **1** `FILE` | `14` rutas de archivo de licencia, incluidas **las tres grafías** `LICENSE` / `License` / `license` | 🔴 **El canal distingue mayúsculas.** `open-spaced-repetition/fsrs4anki-helper` sirve `License` —sin extensión— y por eso esta KB la registraba sin concesión |
| **2** `MANIFEST` | el manifiesto del ecosistema: `11` formatos *(`package.json`, `DESCRIPTION`, `pyproject.toml`, `pom.xml`, `Cargo.toml`, …)* | 🟢 **En varios ecosistemas la concesión vive en el manifiesto y el archivo de licencia es un muñón.** La forma ya estaba registrada **dos veces** en este estante *(`shmercer/writeAlizer`, `47` B con `License: MIT + file LICENSE` en `DESCRIPTION`; y `sonsoleslp/tna`, `46` B, pase `83`)* 🔴 **pero nunca se había ejecutado como pase de POBLACIÓN** |

## Lo que midió (n = `41`)

Población = la población `P1049` de p185 **menos** las `23` filas con veredicto publicado.
*(p185 informó `43` sostenidas; la diferencia de `2` es su propia contabilidad de controles, así que
`41` es un SUELO.)*

| resultado | n |
|---|---|
| 🔴 la ausencia SE SOSTIENE *(sin archivo en `14` rutas, sin campo en `11` manifiestos)* | **`37`** |
| 🟢 **concesión real registrada como ausente — las `3` permisivas** | **`3`** |
| 🟡 artefacto de POBLACIÓN *(fila que esta KB ya registra bien)* | **`1`** |

🟢 **Las tres recuperaciones:**

| fila | limbo | la concesión, tal como está escrita |
|---|---|---|
| 🟢 [`Simon-Initiative/lti-example-tool`](https://github.com/Simon-Initiative/lti-example-tool) | `MANIFEST` | `"license": "MIT"` en `package.json` — **sin archivo de licencia en el árbol** |
| 🟢 [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | `MANIFEST` | `"license": "MIT"` en `package.json` — **sin archivo de licencia en el árbol** |
| 🟢 [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | `FILE` | `MIT License / Copyright (c) 2022 Open Spaced Repetition`, en un archivo llamado **`License`** |

🟡 **El artefacto:** `ai-shifu/ai-shifu` sirve `LICENSE.txt`, `11 342` B, `Apache-2.0`,
*«Copyright 2024 ai-shifu.com»*. 🔴 **No es una recuperación: esta KB lo registra como `Apache-2.0`
desde p184.** 🔵 **Es un defecto del extractor de población de `P1049`** —el filtro de una-slug-por-
línea metió en la población *«sin concesión»* una fila correctamente licenciada. **La población de
`61` no eran `61` ausencias.**

## Límites declarados, medidos en este pase

🔴 **`1`. `GRANT_TEXT` genera falsos positivos sobre licencias propietarias.** La lista de marcadores
incluye `THE SOFTWARE IS PROVIDED`, la cláusula de garantía de `MIT`.
[`ShuyunYuan/talentcoach`](https://github.com/ShuyunYuan/talentcoach) sirve `842` B de
*«All rights reserved … no other rights are granted»* **copiando esa cláusula**. 🟢 El test
reproduce el falso positivo a propósito: **el marcador es una pista, nunca un veredicto.**

🔴 **`2`. Un archivo de `46` B puede llevar el TÍTULO de una licencia y ninguna cesión.**
`MoKangMedical/digital-sage` sirve exactamente `MIT License\n\nCopyright (c) 2026 MoKangMedical`.
🔵 **Es una concesión INCOMPLETA, y es una forma distinta del muñón `CRAN`** *(`writeAlizer`: año y
titular en el archivo, cesión en `DESCRIPTION`)*. 🟢 Por eso se imprime la columna de bytes y la
columna `grant_text`.

🔴 **`3`. El limbo `2` no lee cabeceras de archivo de plugins `Moodle` / `WordPress`**, donde una
cesión `GPL` vive por convención. Las filas de esa forma están dentro de las `37` y **su ausencia no
queda establecida para este instrumento**. 🔵 `ACTION MO`.

## Canal

`raw.githubusercontent.com`, re-medido este pase como el único canal de lectura de GitHub que
responde `200` aquí: `api.github.com` → `403` *(«GitHub access to this repository is not enabled for
this session»)*, `codeload.github.com` → `403`, `github.com` por `curl` → `403`.
🔵 **Y una consecuencia que esta KB debe asumir: sin listado de árbol, un archivo cuya ruta no
aparezca en la documentación del repositorio es ILEGIBLE.** Por eso el censo de esquema de
`ACTION MJ` quedó a medias este pase.

## Cómo se ejecuta

```sh
python3 -I stale_absence.py population.p186.txt > out.tsv   # el pase de población
python3 -I test_stale_absence.py                            # 13 comprobaciones, 0 red
```
