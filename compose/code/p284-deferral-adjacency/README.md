---
industry: education
region: Global
updated: 2026-10-04
---

# `p284-deferral-adjacency` — una corrección verificada que vive en PROSA no es un control: no viaja

> Nuevo en el **pase 95 del 2026-10-04**. Sale de un defecto **medido en esta base**, no de una
> hipótesis: el pase 58 verificó por **tres canales concordantes** que el *Digital Omnibus* corrió
> el **Anexo III autónomo** del AI Act de **2026-08-02 a 2027-12-02**, lo escribió en
> `agents/top.md` — 🔴 **y la corrección no viajó a 13 afirmaciones publicadas.**

| Qué prueba | Invocación | Hoy |
|---|---|---|
| la lógica del detector, con su eximente y su ventana | `python3 test_adjacency.py` | 🟢 **24/24** |
| el estado de los archivos publicados | `python3 adjacency.py ../../../agents/*.md ../../../intel/*.md …` | 🟢 **88 afirmaciones, 0 huérfanas** |

Desde la raíz de la KB:

```sh
python3 compose/code/p284-deferral-adjacency/adjacency.py \
  agents/top.md agents/trending.md repos/foundations.md repos/trending.md \
  verticals/solutions.md intel/market.md intel/trends.md compose/patterns.md README.md
```

Sale `1` si hay huérfanas, `0` si no: sirve de compuerta.

## 🔴 Lo que estaba roto, con su denominador

| Medido sobre los 9 archivos publicados | n |
|---|---|
| afirmaciones que atan **un deber de ALTO RIESGO** a **agosto de 2026** | **87** |
| 🟢 acompañadas por el diferimiento a ≤6 líneas | **74** |
| 🔴 **huérfanas** | 🔴 **13** |

Las 13, enumeradas (el pase 93 dejó la regla: *un conteo sólo es un conteo si ENUMERA*):

`agents/trending.md:1108, 4497, 4601` · `verticals/solutions.md:256` ·
`intel/market.md:239, 3795, 5272, 5393, 5739` · `intel/trends.md:69, 4993, 13315, 13636`

🔴 **La más grave es `intel/trends.md:4993`, que es la tendencia #75**, y no es un dato de paso: su
**tesis** es *«el Annex III dejó de ser una fecha: rige desde el 2026-08-02, y la demanda de
conformidad en EMEA está **vencida**, no anticipada»*. Con el diferimiento, **la tesis se invierte** —
para el Anexo III autónomo la demanda vuelve a ser anticipada, y vence el **2027-12-02**.

## 🟢 Cómo se arregló, y por qué NO se reescribió nada

Las 13 quedaron **anotadas**, no editadas: cada una conserva su texto palabra por palabra y gana una
marca con la fecha nueva. 🔵 **Es deliberado**: `agents/trending.md` es **append-only** por encargo
—reescribirla destruye la tendencia que existe para registrar— y las tendencias numeradas son
registro histórico. **Anotar hace viajar la corrección sin borrar el registro**, que es justo lo que
`P284` pide. Tras la anotación: **88 afirmaciones, 0 huérfanas.**

## ⚖️ El eximente, que es la mitad del control

🔴 **El error simétrico sería exigir el diferimiento en todas partes.** El *Omnibus* **no tocó el
artículo 50**: para la transparencia —el marcado de contenido generado, que es exactamente lo que
`compose/code/aiact-50-2-*` implementa— **agosto de 2026 sigue siendo la fecha CORRECTA**. Así que
una línea que se declara del art. 50 (`artículo 50`, `50(2)`, `transparencia`, `aiact-50-2`) **está
eximida**, y eso está afirmado en la suite como caso obligatorio.

🟢 **La consecuencia comercial es la que importa y no cambia:** el reloj que vence **antes** es el del
art. 50(2), en **2026-08-02**, y esta base ya tiene ese instrumento construido y con suite. Lo que se
corrió 16 meses es el expediente de alto riesgo, que **no desapareció**.

## 🔬 Contrato del módulo

Es un **detector laxo**, no un validador: decide si una afirmación está **acompañada**, nunca si es
correcta. Mismo contrato que `p239` y el lado detector de `lib/region.py` (`P263`).

- **afirmación** = en UNA línea, la fecha vieja **y** el deber corrido. La fecha **sola** no se cuenta
  (la aplicación *general* del Reglamento sí rige desde 2026-08-02); el deber **solo** tampoco.
- **ventana** = ±6 líneas, simétrica: el diferimiento vale arriba o abajo. Es parámetro, y la suite
  afirma que la ventana **importa** (el mismo par a 21 líneas es huérfano; con ventana 25 no).

**P284**: *cuando una fecha regulatoria se corrige, la corrección hay que MEDIRLA en todas las
afirmaciones que dependen de ella, no escribirla una vez. Si vive en un archivo y las demás
afirmaciones no la ven, la base publica dos relojes y el cliente planifica con el viejo.*
