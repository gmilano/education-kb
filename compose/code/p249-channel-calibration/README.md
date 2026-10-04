---
industry: education
region: Global
updated: 2026-10-04
---

# P249 — calibrar un canal antes de creerle un negativo (pase 82 del 2026-10-04)

El **pase 81** pidió `curl -sI` contra `github.com` para las URLs de `agents/top.md`, recibió
**`403` en 81 de 81** y escribió que *«el canal que el encargo ordena usar marca MUERTO el 100 % del
catálogo»*. El diagnóstico de canal era correcto y ya tenía nombre (**P247**). 🔴 **Lo que faltaba no
era el diagnóstico: era la compuerta, y el canal que la pasa estaba en este mismo repositorio desde
el pase 64.**

`p170-headref-license-sweep` lee `raw.githubusercontent.com/<slug>/HEAD/<archivo>` y documenta en su
encabezado que la ref literal `HEAD` resuelve la rama por omisión cualquiera sea su nombre.
🔵 **El pase 81 declaró el catálogo inverificable teniendo el instrumento a 17 pases de distancia.**

## La regla

> **P249.** Antes de creerle un **negativo** a un canal de verificación, el canal se calibra contra
> una URL que se sabe **buena** y una que se sabe **inexistente**. Un canal que contesta lo mismo a
> las dos **no discrimina**, y de un canal que no discrimina no se lee una ausencia — ni una ni
> ochenta y una. Y antes de **escribir** un defecto de canal, se busca en `compose/code/` si esta
> base ya tiene uno calibrado.

## El ledger medido el 2026-10-04

| Canal | URL buena | URL inexistente | Veredicto | ¿Creer un negativo? |
|---|---|---|---|---|
| 🔴 `curl -sI` a `github.com` | **403** | **403** | `UNCALIBRATED-NO-DISCRIMINATION` | 🔴 **NO** |
| 🔴 `curl` GET a `github.com` | **403** | **403** | `UNCALIBRATED-NO-DISCRIMINATION` | 🔴 **NO** |
| 🔴 `curl` a `api.github.com` | **403** | **403** | `UNCALIBRATED-NO-DISCRIMINATION` | 🔴 **NO** |
| 🟢 `raw.githubusercontent.com` + `HEAD` | 🟢 **200** | 🟢 **404** | 🟢 **`CALIBRATED`** | 🟢 **SÍ** |

🔵 **Varianza cero sobre 81 muestras no es el estado de 81 repos: es el estado del canal.** Y el
mismo `curl` que da `403` a `github.com` da `200` a `pypi.org`, así que tampoco es «no hay egreso».

## Lo que el canal calibrado dice del catálogo

| Estado de los 69 `org/repo` de `agents/top.md` | n | % |
|---|---|---|
| 🟢 `LICENSED` | **43** | 62,3 % |
| ⚠️ `UNLICENSED` (ausencia **medida**) | **23** | 33,3 % |
| 🔴 `UNREACHABLE` | **3** | 4,3 % |
| 🟢 **Alcanzables** | **66 de 69** | 🟢 **95,7 %** |

🟢 **El control que cierra el caso es de reproducibilidad, no de conteo: de los 58 slugs compartidos
con el resultado del pase 64, los 58 dan el mismo estado y la misma familia. Cero deriva.**

## Correr

```sh
python3 test_calibrate.py        # 20/20 — la lógica, sin red
sh sweep_channels.sh             # el ledger vivo, 4 canales × 2 controles
```

| Archivo | Qué es |
|---|---|
| `calibrate.py` | Las funciones **puras**: `classify_channel`, `may_believe_negative`, `channel_defect_from_uniformity`, `verdict_for_sweep`. No tocan la red, así que la suite es reproducible sin egreso |
| `channels.tsv` | Los 4 canales con su URL buena y su URL inexistente |
| `sweep_channels.sh` | Mide los dos controles de cada canal y publica el veredicto |
| `result.2026-10-04.tsv` | El ledger de arriba, medido |
| `test_calibrate.py` | **20/20** |

## El control que importa es el NEGATIVO

La suite incluye la **medición literal del pase 81** (`403` × 81) y exige que el instrumento conteste
**`NO-CLAIM`**: no se puede afirmar nada del catálogo por un canal que no discrimina. También exige
que *(a)* un barrido uniforme en `200` **no** se lea como defecto —un uniforme positivo no es un
negativo—, *(b)* dos muestras no alcancen para declarar defecto, y *(c)* un barrido con varianza real
**no** se declare defecto de canal.
