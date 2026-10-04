---
industry: education
region: Global
updated: 2026-10-04
---

# `p287-regional-saturation` — «saturación» dicha en prosa no tiene denominador

> Nuevo en el **pase 95 del 2026-10-04**. Los pases 91, 92, 93 y 94 registraron que las cuatro
> búsquedas regionales obligatorias devuelven lo mismo. 🔴 **Pero «las cuatro regiones vuelven a dar
> saturación» es un adjetivo, y el pase 93 dejó la regla: un conteo sólo es un conteo si ENUMERA.**
> Este instrumento la aplica al barrido regional.

| Qué prueba | Invocación | Hoy |
|---|---|---|
| la lógica de la medición | `python3 test_measure.py` | 🟢 **15/15** |
| el barrido regional del 2026-10-04 | ver abajo | 🔴 **27 hechos, 0 nuevos** |

```sh
python3 compose/code/p287-regional-saturation/measure.py \
    compose/code/p287-regional-saturation/facts.2026-10-04.tsv \
    intel/market.md intel/trends.md agents/top.md agents/trending.md \
    verticals/solutions.md repos/foundations.md repos/trending.md compose/patterns.md
```

## 🔴 El resultado del pase 95: saturación TOTAL, y por fin con denominador

Las cuatro búsquedas obligatorias se corrieron con el **año CALCULADO** (`date -u +%Y` → **2026**):
`AI education {North America|EMEA|APAC|LATAM} 2026 adoption regulation players`. Cada hecho que
devolvieron está enumerado en `facts.2026-10-04.tsv` con el patrón que lo identifica:

| Región | Hechos devueltos | 🔴 Nuevos para esta base |
|---|---|---|
| North America | 7 | **0** |
| EMEA | 6 | **0** |
| APAC | 7 | **0** |
| LATAM | 7 | **0** |
| **TOTAL** | **27** | 🔴 **0** |

🔴 **27 de 27 ya estaban publicados.** No es que las regiones no rindieran: **rindieron, y rindieron
exactamente lo mismo que el pase 94 y el 93**. Esa es la diferencia entre *«no encontré nada»* (que
no se puede auditar) y *«encontré 27 hechos y los 27 ya estaban»* (que sí).

## 🔵 Lo que la medición hace decidible, y es de MÉTODO

🔴 **El valor marginal de estas cuatro consultas, tal como están redactadas, es CERO medido** —cuatro
pases consecutivos, y éste con denominador. Repetirlas literalmente un pase más no es rigor, es
gasto. 🟢 **Lo que rompería la saturación no es más esfuerzo en el mismo eje, es cambiar el EJE de la
consulta**, y queda pre-registrado para el pase 96:

- el eje de **proveedor/soberanía** (quién procesa datos de alumnos, bajo qué contrato) en vez del de
  adopción/regulación — es donde la capa de plataforma (`P269`–`P273`) ya mostró hallazgos;
- el eje de **licitación pública** (ministerios, compras de LMS) en vez del de prensa de mercado;
- y la fuente **primaria fechada** (boletín oficial, repositorio institucional) en vez del agregador.

**P287**: *una saturación sin denominador no se distingue de no haber buscado. Si un barrido obligatorio
devuelve sólo cosas conocidas, hay que ENUMERAR lo que devolvió y medir la intersección con lo
publicado — y entonces «cero nuevos» es un dato con el que se puede decidir si cambiar el canal.*

## 🔬 Contrato

- `facts.<fecha>.tsv` es **inmutable por fecha**: un pase no reescribe el de otro, agrega el suyo. Así
  la serie muestra si la saturación se mantiene o se rompe.
- `region` usa el **vocabulario CERRADO de cinco valores** (`North America`, `EMEA`, `APAC`, `LATAM`,
  `Global`), y la suite lo **afirma** como caso obligatorio — no `Latam`, no `Europe`, no un país.
- `pattern` es una **regex**, no un literal, para que las variantes de una cifra (`2.303` / `2303`)
  vivan en UNA fila y no infleun el denominador.
- La suite afirma que la **cabecera del TSV no entra como fila**: una fila de cabecera compilada como
  dato ya le pasó a esta base más de una vez (`P239`).
