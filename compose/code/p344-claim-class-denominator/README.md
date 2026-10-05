---
industry: education
region: Global
updated: 2026-10-05
---

# `P344` — el denominador de una pregunta puede estar construido CONTRA su propia hipotesis

Artefactos y suite del **pase 110 (2026-10-05)**. Las aserciones corren contra los TSV y contra el
modulo, no contra la prosa de los `.md`.

## Que hay aca

| archivo | que es |
|---|---|
| `detect_claim.py` | el detector de AFIRMACIONES de cesion: 4 ejes (`badge_md`, `badge_html`, `tree`, `prose`) + `verdict()` de 3 cubetas |
| `sweep_claim.py` | el barrido: 10 nombres × 2 ramas + README en 4 ortografias × 3 refs, por `raw.githubusercontent.com` |
| `enumerate_trees.sh` | el canal de `P275`: clon `--filter=blob:none` + `git ls-tree -r`, que ve el arbol COMPLETO y no solo la raiz |
| `targets13.txt` | **el denominador pre-registrado**: los 13 «sin licencia» vivos |
| `targets-resto9.txt` | **las 9 filas que la pre-registracion EXCLUYO**, y donde esta el hallazgo |
| `accionA-v2.2026-10-05.tsv` | los 13 + control, con el detector corregido |
| `accionA-resto9-v2.2026-10-05.tsv` | las 9 excluidas |
| `arbol13.2026-10-05.tsv` | arbol enumerado de los 13 (**9.886 rutas**, 0 archivos de cesion) |
| `arbol-controles.2026-10-05.tsv` | el instrumento de arbol contra 2 respuestas CONOCIDAS + repo inventado |
| `control-codes.2026-10-05.txt` | **20/20 · 404** del repo inventado, en el mismo lote |
| `candidatas.2026-10-05.tsv` | las 2 candidatas nuevas del barrido de este pase |
| `test_p344.py` | **31 aserciones**, 0 fallos (`Python 3.11.15`) |

## El hallazgo

La accion A pre-registrada por el pase 109 pedia: *de los 13 «sin licencia», ¿cuantos afirman una
cesion por badge o por arbol de README sin archivo que la respalde?* Prediccion: **≥2**.

**Medido: 0 de 13.** Eso cae en la rama de refutacion que la propia pre-registracion escribio
(*«que sea 0 o 1, y entonces `P342` es un espécimen y el catalogo esta sano»*).

🔴 **Pero esa conclusion es FALSA, y el motivo es de construccion del denominador.** Los 13 son las
filas `SILENT-3-LAYERS` del pase 66 — y el pase 66 ya habia separado, con otras etiquetas, a los
repos que SI afirman: `README-BADGE`, `README-PROMISE-BROKEN`, `README-IDENTIFIER`,
`README-CONTRADICTION`. **Los 13 se formaron quitando exactamente la clase que la prediccion
buscaba.**

Medido sobre las **9 filas que la pre-registracion excluyo**: **6 de 9** son
`P342-AFIRMA-SIN-ARCHIVO`. Eso cruza la OTRA rama de refutacion de la misma pre-registracion
(*«que lo hagan ≥6 de 13, y entonces el defecto no es del catalogo sino del ecosistema»*).

🔵 **Las dos ramas de refutacion disparan a la vez, sobre denominadores distintos.** La leccion de
metodo: *una prediccion falsable tiene que decir como se CONSTRUYO su denominador, no solo su
tamaño — un denominador se puede haber formado restando la clase que la hipotesis predice.*

## El defecto de instrumento, que es la mitad del aporte

La primera version de la accion A estaba escrita en `grep -E` y era **ciega a dos formas**:

1. **badge en HTML.** `NLP2CT/LLM-generated-Text-Detection` y `RadiantCrystal/SafeTutors` afirman
   MIT con `<img src="https://img.shields.io/badge/License-MIT-…" alt="License">`, no con el
   `[![…]](…)` de Markdown. Un detector de sintaxis Markdown publica «silencio» sobre los dos.
2. **el nombre envuelto en enfasis.** `licensed under the **MIT License**` se perdia porque la
   clase de caracteres del patron excluia el asterisco.

🔵 **Y la consecuencia de canal es contraintuitiva:** el pase 66 los habia visto **porque leyo la
pagina RENDERIZADA**; el canal de PAYLOAD que este arbol prefiere —y con razon, para leer
cesiones— tiene **menor recall para AFIRMACIONES**. Son dos preguntas distintas y quieren canales
distintos.

## Los dos controles de respuesta conocida, que el sondeo de raiz FALLA

Este arbol ya sabe dos respuestas, y sirven para medir el instrumento en vez de confiar en el:

| repo | lo que este arbol ya sabe | sondeo de RAIZ (10 nombres × 2 ramas) | arbol enumerado |
|---|---|---|---|
| `1EdTech/openbadges-specification` | cede en `ob_v3p0/license.md`, **12.324 B** (`P187`) | 🔴 `SILENCIO-CONFIRMADO` | 🟢 **5** superficies de cesion |
| `dini-ag-kim/school-curriculum-pg` | cede **CC BY-SA 4.0** en `lp-base.ttl:24` (`P172`-semantic) | 🔴 `SILENCIO-CONFIRMADO` | 🟢 **2** rutas |

🔴 **2 de 2 fallan, y en la misma direccion: el sondeo de raiz SUBREPORTA cesion.** Asi que
«`SILENCIO-CONFIRMADO`» de este instrumento no significa *«no cede»*: significa *«no cede en la
raiz, con 10 nombres y 2 ramas»*. La replica de `P187` es **al byte** (12.324 B,
`sha256 c443abf513b1`), y de paso corrige su denominador: no es UNA superficie de cesion, son
**CINCO** (`ob_v2p1/LICENSE-INPROGRESS.md`, `ob_v3p0/cert/terms.md`, `ob_v3p0/license.md`,
`proposals/OBv3p0/license.md`, `proposals/a-template/license.md`) — *«la pregunta de licencia es
POR VERSION»* con cifra.

## Y el error que el instrumento de ARBOL introduce, medido

🔴 **Un archivo de licencia hallado en profundidad puede no ser la cesion del repo.** En
`dini-ag-kim/school-curriculum-pg` el arbol devuelve
`src/ontology/utils/owl2shacl/LICENSE` = **LGPL-3.0**, 7.652 B, `sha256 e3a994d82e64`, con titular
**Free Software Foundation** — es el texto de una herramienta EMPOTRADA, no la cesion del
repositorio, que es **CC BY-SA 4.0 sobre los datos**.

🔵 **Tres canales, tres respuestas distintas para UN repo:**

| canal | devuelve | ¿correcto? |
|---|---|---|
| sondeo de raiz | *sin cesion* | 🔴 no |
| arbol, primer archivo hallado | **LGPL-3.0** | 🔴 no — es de una dependencia empotrada |
| payload RDF (`lp-base.ttl:24`) | **CC BY-SA 4.0** | 🟢 si, y es la cesion de los DATOS |

⚠️ **La direccion del error importa:** un barrido de arbol que tome el primer archivo que
encuentra le pega una licencia COPYLEFT DE CODIGO a un repo cuyo entregable es DATO con
atribucion. Es `P283`/`OpenMAIC` («la licencia de la raiz no es la licencia del arbol») en la
direccion contraria: **la licencia del arbol tampoco es la licencia de la raiz.**

## Lo que queda cerrado sobre los 13

🟢 **Con el arbol enumerado, los 13 dejan de ser «sin cesion EN LA RAIZ» y pasan a ser medidos:**
**0 archivos de cesion en 9.886 rutas**, en ninguna profundidad y en ninguna caja. El instrumento
que lo afirma **pasa** los dos controles de respuesta conocida y **falla** con el repo inventado
(`CLON-FALLO`), asi que el cero discrimina.

## Los artefactos SUPERADOS, que se conservan a proposito

`sweep_claim.MARKDOWN-ONLY-SUPERSEDED-2026-10-05.sh` y sus dos TSV son la **primera** version de la
accion A — la de `grep -E`, ciega a los badges en HTML y al nombre en `**enfasis**`. 🔵 **Se
conservan porque son la EVIDENCIA de `P344`:** sus dos filas `SILENCIO-CONFIRMADO` sobre
`NLP2CT/LLM-generated-Text-Detection` y `RadiantCrystal/SafeTutors` son el falso negativo medido,
y compararlos con `accionA-resto9-v2` muestra el defecto en vez de contarlo. **No usar para medir.**
