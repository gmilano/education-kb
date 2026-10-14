---
industry: education
region: Global
updated: 2026-10-14
---

# `p1049-bare-token-grant` — la licencia de una fila puede ser UNA PALABRA, y dos instrumentos de esta KB la declaran ausente (pase 185 del 2026-10-14)

**Ejecuta `ACTION MD`**, registrada en p184 después de que `tianshuo/trainingllm` apareciera con su
licencia completa escrita así:

```markdown
## License

MIT
```

🔴 **Sin archivo de licencia y sin texto de cesión, los dos instrumentos de esta KB informan *«no
grant»* y los dos se equivocan.** El probe por rutas (**P170**) busca `LICENSE`/`COPYING`; el
comparador de cuerpo (**P179**) busca marcadores de cesión *(«Permission is hereby granted»,
«Grant of Copyright License»)*. **Una palabra bajo un encabezado no tiene ninguno de los dos.**

## Las dos extremidades

| limbo | script | qué lee | por qué existe |
|---|---|---|---|
| **1** | `bare_token_grant.py` | sólo lo que cuelga de un encabezado tipo *licen[cs]e / licencia / 版权 / ライセンス* | precisión: el encabezado es el lugar donde un autor pone SU concesión |
| **2** | `whole_readme_scan.py` | **toda** línea del README con un identificador de licencia | su propio control positivo venció al limbo 1 |

🔵 **El limbo 2 no se diseñó por completitud: se diseñó porque el control positivo falló.**
`xiaolai/the-craft-of-selfteaching` declara su licencia en una frase en chino sin ningún encabezado
—*«本书的版权协议为 CC-BY-NC-ND license»*— y el limbo 1 devolvió `NO_HEADING`.

## Canal

`raw.githubusercontent.com`. **Es el único canal de lectura de GitHub que responde `200` en este
entorno**, re-medido este pase: `api.github.com` → `403`, `codeload.github.com` → `403`.
🔵 Y una lección barata: el canal **distingue mayúsculas**. `pipwerks/scorm-api-wrapper` no tiene
`README.md` pero sí `readme.md`, y su concesión vive allí.

## Lo que midió (n = 61 filas + 3 controles)

| resultado | n |
|---|---|
| 🔴 la ausencia SE SOSTIENE *(sin encabezado y sin identificador en todo el README)* | **43** |
| 🟢 **concesión real que esta KB registraba como ausente** | **9** |
| 🟡 identificador presente que **no es** una concesión *(reclamo, insignia, restricción, referencia colgante)* | **5** |
| 🔴 **falso positivo de la pantalla** *(tras la corrección de abajo)* | **3** |

🟢 **De las `9`, seis son permisivas** *(`MIT` ×3, `Apache-2.0` ×3)*, una es una cesión **bespoke en
prosa española** y dos son copyleft.

## Los tres modos de falla, porque valen más que el resultado

1. 🔴 **El inventario de dependencias DENTRO de la sección de licencia.**
   `jadrianlg16/learning-tutor` lista `AGPL-3.0` *(PyMuPDF)*, `Apache-2.0` *(FastMCP)* y
   `BSD-3-Clause` *(httpx)* bajo `## License` — y esa misma sección dice *«All rights reserved …
   no license is granted to reuse or redistribute it»*. **El token no era de este proyecto.**
   🔵 El mismo patrón aparece en `sohan1611/BloodCoded_Agentic` *(tabla de dependencias con tres
   `Apache-2.0`, licencia propia `MIT`)* y en `IC-Redacoes-UTFPR/CorrecaoRedacao` *(el `MIT` es del
   corpus `lplnufpi/essay-br`)*. **Tres instancias en un solo pase: no es anécdota, es la forma.**
2. 🔴 **El encabezado que PREGUNTA en vez de conceder.** `rachelproject/module-template` trae
   `## What licenses are appropriate?` — una política de contribución, no una cesión.
3. 🟢 **Dos bugs de LÍMITE DE PALABRA, encontrados por la suite de este mismo instrumento y
   corregidos en el pase:** `MIT\b` —sin límite por delante— coincidía dentro de **`sub|mit `**, y
   `CC0` coincidía dentro del id hexadecimal **`…bcc0-66af…`**.
   🔵 **Re-correr los dos limbos con `\bMIT\b` y `\bCC0\b` cambió exactamente `2` veredictos y
   ningún otro**, así que las `9` recuperaciones no dependen del bug.
   🟢 **Y deja la pantalla con una propiedad útil: los `3` falsos positivos que quedan tienen UNA
   sola forma — el identificador es de una DEPENDENCIA o de un corpus de terceros.**

🔵 **La regla que sale de los tres: esta pantalla es una PANTALLA.** El token es la señal para
**leer**, nunca el veredicto. Y la supresión por palabra clave es peor que el ruido: el filtro
`NOISE` del limbo 2 descartó la línea de `haolpku/Omni-Edu` —*«The code is licensed under
Apache-2.0. Model weights and third-party datasets and benchmarks retain their respective
licenses»*— **porque contenía `third-party`. Un falso negativo construido a mano.**

## Uso

```sh
python3 -I bare_token_grant.py  population.p185.txt > limb1.tsv
python3 -I whole_readme_scan.py population.p185.txt > limb2.tsv
```

Evidencia publicada: [`evidence/bare-token-grant.2026-10-14-p185.tsv`](../../../evidence/bare-token-grant.2026-10-14-p185.tsv)
*(lectura a mano, fila por fila)* y los dos crudos `-limb1-raw` / `-limb2-raw`.
