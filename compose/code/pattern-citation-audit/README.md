---
industry: education
region: Global
updated: 2026-10-03
---

# `pattern-citation-audit` — el detector de citas de patrón COLGADAS (acción 2 del pase 61, CERRADA)

**El pase 60 encontró el defecto a mano y dejó la acción escrita así: «esta KB tiene 114 citas de
patrón colgadas sobre nueve números que nunca se definieron (P126–P130, P132–P135) … y no se cierra
inventando definiciones».** Este directorio cierra esa acción con las dos mitades que faltaban: una
cifra que reproduce y un instrumento que la vuelve a medir.

## Lo que la acción pedía, y cómo quedó

| Lo que pedía el pase 60 | Veredicto del pase 61 |
|---|---|
| **cuáles** son los números colgados | 🟢 **CONFIRMADO exacto: los nueve.** P126, P127, P128, P129, P130, P132, P133, P134, P135 |
| **cuántas** citas cuelgan: «114» | 🔴 **NO REPRODUCE.** Son **80** en forma `**Pn**` y **158** contando `Pn` suelto al cierre del pase 61. 114 no es ninguno de los dos |
| no inventar definiciones | 🟢 **ninguna definición escrita.** Se midió el origen en su lugar |

## El hallazgo que la acción no pedía: nacieron colgados

**Las nueve se buscaron en los 65 commits de la historia del repo, una por una.** Ninguna estuvo
nunca definida: **no es texto perdido en una reescritura, es texto que nunca existió.**

Y el mecanismo es regular, lo que lo vuelve prevenible:

| Pase | Promovió a sección | Acuñó al paso, sin sección |
|---|---|---|
| **55** (`52b1c68`) | **P131**, «el patrón nuevo es P131» | **P126, P127, P128, P129, P130** |
| **56** (`96635bb`) | **P136**, «el patrón nuevo es P136» | **P132, P133, P134, P135** |

**Los dos pases anunciaron UN patrón nuevo en singular y gastaron cuatro o cinco números más como
etiquetas de cita en el mismo párrafo.** Cada número colgado tiene, en el commit que lo acuñó, una
observación concreta de una sola oración — así que la intención es **recuperable del sitio de
acuñación** y un pase futuro puede promoverla sin inventar nada. Eso es **P157**.

## Correr el instrumento

```sh
python3 compose/code/pattern-citation-audit/audit_patterns.py .   # TSV; exit 1 si hay colgadas
python3 compose/code/pattern-citation-audit/test_audit.py         # 8 aserciones
```

## Por qué el detector conoce CUATRO convenciones y no una

🔴 **El primer detector de este pase reportó 13 números colgados, y cuatro eran falsos positivos.**
Conocía sólo `## Pn — …`, así que no vio que **P145–P148 están definidos bajo un encabezado de RANGO**
(`## 🧩 P145–P148, los patrones del pase 59`) con subsecciones `### P146 — …`, ni que **P149 es una
RECETA** (`## 🍳 Receta P149`), que es otro namespace. **La cifra de un instrumento ciego a una
convención es la cifra de la convención, no la del archivo** — y es la explicación más probable del
114 del pase 60.

| Convención | Forma real en `patterns.md` | Qué define |
|---|---|---|
| **A** | `## P142 — título` | sección propia |
| **B** | `### 🔴 P146 — título` | subsección dentro de un grupo |
| **C** | `## 🧩 P145–P148, los patrones del pase 59` | **los cuatro del rango** |
| **D** | `## 🍳 Receta P149 — …` | receta, **no** patrón |

`test_audit.py` **ancla y desancla** (P119): fija las cuatro convenciones, fija que una mención en
prosa NO define, fija el control negativo (`P999` → 0 citas) y fija que un rango absurdo (`P1–P900`)
no puede definir 900 números de un saque.

## La cifra, con su instrumento al lado (P107)

```
# definidos    149    convenciones  {'A/B-seccion': 147, 'D-receta': 2}
# COLGADAS     9 numeros    80 citas_bold    158 citas_any
# control_positivo_definidos   P142(A/B),P145(A/B),P148(A/B),P149(D-receta),P131(A/B),P136(A/B)
# control_negativo_P999_citas  0
```

⚠️ **`citas_bold` (80) es la cifra citable; `citas_any` se mueve cada pase, porque cada resumen que
discute el defecto suma menciones.** Al cerrar el pase 61 vale **158**: el propio pase agregó las
menciones al escribir **P157**. 🔵 **Por eso el número que se compara entre pases es el de forma
fuerte, y el suelto sólo sirve para el mismo pase que lo mide.**

⚠️ **Las dos más citadas siguen siendo las peores: `P135` (21 citas en forma fuerte, 31 en total) y
`P126` (12 y 31).** Las dos son reglas de **método** que esta base invoca como autoridad —`P135` en
`intel/market.md` siete veces— y **ninguna tiene texto.** Mientras no se promuevan, toda cifra que se
apoye en ellas se apoya en un paréntesis de un resumen de pase.
