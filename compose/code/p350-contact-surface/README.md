---
industry: education
region: Global
updated: 2026-10-05
---

# `P350` — la frontera de una accion hacia afuera es ANTES de «no mandar nada»

Artefactos y suite del **pase 111 (2026-10-05)**. Registra el veredicto de la **accion A**
pre-registrada por el pase 110.

## El veredicto: NO MEDIBLE, que es un tercer resultado

| clausula pre-registrada por el pase 110 | pedia | medido | veredicto |
|---|---|---|---|
| *«de los 6, **≥4** tienen canal de contacto resoluble desde el payload»* | ≥ 4 | ⚠️ **sin cifra** | **NO MEDIBLE** |
| rama de refutacion: *«que sean ≤2 ⇒ `P342` vuelve a descarte»* | ≤ 2 | ⚠️ **sin cifra** | no evaluable |
| la frontera que la pre-registracion declaro | *«se detiene en REDACTAR: no se manda nada»* | 🔴 **insuficiente** | la real esta **antes** |

🔴 **La frontera real de este entorno esta antes del envio: ENUMERAR un canal de contacto ya es
manejo de datos personales, y la extraccion fue DENEGADA por politica (`PII Data Handling`).**

La pre-registracion fue cuidadosa en el eje que anticipo —no mandar nada, la misma frontera que
el pase 61 respeto con el PR a `toshieji`— y se equivoco en CUAL era el eje. Recolectar correos y
perfiles de personas desde repos de terceros es la accion sensible, aunque el resultado no salga
del arbol.

⚠️ **No se intento por otra via, ni con otra herramienta, ni con un sub-agente, ni en otro turno.**
La denegacion se registra y se respeta.

## Lo que SI se midio: ESTRUCTURA, no contenido

Presencia y tamano de las superficies que podrian cargar un canal, por
`raw.githubusercontent.com`, en `main` y `master`. **120 sondas** (6 repos × 10 rutas × 2 ramas).
El contenido **no se leyo y no se publica**.

| ruta | repos | legible por maquina sin persona |
|---|---|---|
| `README.md` | 🟢 **6 / 6** | 🔴 no — es prosa libre |
| `package.json` | 1 / 6 (69 B) | 🔴 no — `author` es dato personal |
| `CODEOWNERS` | 🔴 **0 / 6** | si lo seria |
| `.github/CODEOWNERS` | 🔴 **0 / 6** | si lo seria |
| `CITATION.cff` | 🔴 **0 / 6** | si lo seria |
| `CONTRIBUTING.md` · `pyproject.toml` · `setup.py` · `README.rst` · `readme.md` | 🔴 **0 / 6** | — |

🟢 **Testigo de alcance: README 200 en 6 de 6.** El canal LLEGA, asi que los 404 de las otras
rutas son **ausencia** y no incapacidad de leer (`P294`). Las dos cifras hay que no confundirlas:
**0 superficies legibles CON 6 de 6 alcanzables** es un hallazgo; 0 y 0 seria un canal muerto.

## La consecuencia para `P342`, que decide si vale la pena

🔵 **El resultado estructural contesta la pregunta de todas formas, y en la direccion de la rama
de refutacion: ninguno de los 6 tiene una superficie de contacto LEGIBLE POR MAQUINA.** La unica
superficie presente en los 6 es prosa libre, que es exactamente lo que la politica protege. El
unico manifiesto que existe tiene **69 bytes**, que no alcanzan para declarar un canal ademas del
resto del objeto.

🔴 **Asi que `P342` es recuperable en teoria y, en este entorno, NI ENUMERABLE.** Es un enunciado
mas fuerte que el *«inalcanzable en la practica»* que la pre-registracion ofrecia — y es sobre el
ENTORNO y su politica, **no** sobre los 6 repos ni sobre sus titulares. Un entorno con una persona
que apruebe el paso puede volver a abrirlo; este no.

## Los 6, que son los falsos negativos `P342` del pase 110

`NLP2CT/LLM-generated-Text-Detection` · `RadiantCrystal/SafeTutors` ·
`SabioTechTeam/Teacher-Hub` · `eth-lre/mathtutorbench` · `kaushal0494/AITutor-EvalKit` ·
`kaushal0494/UnifyingAITutorEvaluation`

## Que hay aca

| archivo | que es |
|---|---|
| `superficie.py` | el veredicto versionado y la tabla estructural (bytes, nunca texto) |
| `test_p350.py` | **12** aserciones, 0 fallos (`Python 3.11.15`) |

🔵 **El control negativo que importa:** `test_NEGATIVE_ninguna_ruta_registra_contenido` exige que
cada entrada de la tabla sea un **entero**. Si alguna fuera `str`, se habria publicado payload —
el control no protege una cifra, protege la frontera.
