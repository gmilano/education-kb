---
industry: education
region: Global
updated: 2026-10-05
---

# `P349` — la resolucion del canal de estrellas es una FUNCION ESCALON, no «3 cifras significativas»

Artefactos y suite del **pase 111 (2026-10-05)**. Refina la cota que el pase 110 publico junto a
su hallazgo de canal.

## El enunciado del pase 110, y por donde falla

El pase 110 escribio: *«la cota, que hay que publicar junto a cada cifra: la resolucion es de
**3 cifras significativas**. `github.com` renderiza «40,8k», no `40.823`»*.

Medido por `WebFetch` sobre cinco repos de este catalogo, en cuatro magnitudes:

| repo | lo que renderiza | cifras | cota | banda |
|---|---|---|---|---|
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | `264` | 3 | 🟢 **0 — EXACTO** | `EXACTO` |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `107` | 3 | 🟢 **0 — EXACTO** | `EXACTO` |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `7.5k` | 🔴 **2** | ±50 | `K-2CIFRAS` |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `40.8k` | 3 | ±50 | `K-3CIFRAS` |
| [`browser-use/browser-use`](https://github.com/browser-use/browser-use) | `117k` | 3 | ±500 | `K-ENTERO` |

🔴 **El enunciado es falso en LAS DOS direcciones:**

1. **Por debajo de 1.000 el canal entrega el ENTERO EXACTO** (`264`, `107`). Mejor que 3 cifras
   significativas, no peor. El pase 110 negaba el entero exacto en general, y en esa banda lo hay.
2. **En la banda 1.000–9.999 entrega solo DOS** (`7.5k`). `moodle/moodle` no distingue 7.450 de
   7.550, asi que ahi la cota es PEOR que 3 cifras.

## La cota, que es lo que importa para publicar

| banda | rango | se ve | cota absoluta | cota relativa |
|---|---|---|---|---|
| `EXACTO` | < 1.000 | `264` | 🟢 **0** | 🟢 **0 %** |
| `K-2CIFRAS` | 1.000–9.999 | `7.5k` | ±50 | 🔴 hasta **±5,0 %** (al pie) |
| `K-3CIFRAS` | 10.000–99.999 | `40.8k` | ±50 | ±0,5 % → ±0,05 % |
| `K-ENTERO` | ≥ 100.000 | `117k` | 🔴 **±500** | ±0,5 % → |
| `NO-MEDIDA` | ≥ 1.000.000 | — | ⚠️ **sin medir** | — |

🔵 **El peor error RELATIVO esta al pie de la banda `k`** (`1.0k` → ±5,0 %), y **el peor ABSOLUTO
arriba** (±500). Las dos cosas no ocurren en el mismo lugar, que es exactamente lo que una sola
cifra de «cifras significativas» no puede decir.

⚠️ **La banda de millones se declara `NO-MEDIDA` y no se infiere:** ningun repo de este catalogo
la alcanza, y extrapolarla es lo que `P286` prohibe.

## La regla operativa

> **Un entero exacto de estrellas solo es publicable por debajo de 1.000.** Arriba va como
> magnitud, con la banda nombrada y la cota al lado.

Las seis cifras del eje generalista que esta base publicaba quedan medidas contra la regla, y
🔴 **no estan todas en la misma banda** —tres pasan de 100.000 (cota ±500) y tres no (cota ±50)—,
asi que la cota se lee por fila y no por cohorte:

| cifra publicada | banda | cota |
|---|---|---|
| `385.407 ★` · `151.639 ★` · `108.128 ★` | `K-ENTERO` | ±500 |
| `62.735 ★` · `60.284 ★` · `55.226 ★` | `K-3CIFRAS` | ±50 |

## Que hay aca

| archivo | que es |
|---|---|
| `banda.py` | `leer_render` (lo que se ve → cota) y `precision_publicable` (valor → que se puede escribir) |
| `test_p349.py` | **21** aserciones, 0 fallos (`Python 3.11.15`) |

## El defecto que la suite encontro en su primera corrida

🔴 **El limite de banda no esta donde esta el limite aritmetico, porque el REDONDEO lo cruza.**
`precision_publicable(99950)` elegia la banda por el valor crudo (< 100.000 → `K-3CIFRAS`) y
emitia `100.0k`, una forma que `leer_render` **no reconoce**. Lo destapo el control de ida y
vuelta, no la lectura del codigo. Arreglado redondeando PRIMERO y eligiendo la banda despues;
quedan dos tests de regresion (`99950 → 100k`, `9950 → 10.0k`).
