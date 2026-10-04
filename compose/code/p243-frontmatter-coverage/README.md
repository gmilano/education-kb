---
industry: education
region: Global
updated: 2026-10-04
---

# P243 — la cobertura de *frontmatter* se hacía cumplir en 8 archivos y nunca se midió en los otros 48

## El eje que faltaba

`P239`/`P240` (pase 78) **declaran su alcance en los 8 archivos de contenido** —
`agents/`, `repos/`, `verticals/`, `intel/`, `compose/patterns.md` —. 🔴 **Esa declaración de alcance
es correcta y tuvo un costo invisible: los `README.md` de `compose/code/` quedaron fuera de TODA
medición de *frontmatter*, en 79 pases.**

Medido en el pase 79, con el loop de `sh` de abajo y **verificación de primera mano de los 15
hallazgos** (se imprimió la primera línea real de cada archivo reclamado, no sólo el veredicto del
contador):

| Medición | Antes del pase 79 | Después |
|---|---|---|
| Archivos `.md` en el árbol | **56** | **57** *(este pase agregó el README de este instrumento)* |
| Con *frontmatter* | **41** | 🟢 **57** |
| **Sin *frontmatter*** | 🔴 **15** | 🟢 **0** |

🔴 **Los 15 eran todos `README.md` de `compose/code/`**, así que el compilador los leía **sin
`industry` y sin `region`** — y la consecuencia es justo la que el encuadre de esta KB nombra: *la
región hay que inferirla de la prosa, y las inferencias se vuelven datos equivocados.*

🔵 **Decisión de región declarada, no escondida:** a los 15 se les puso **`region: Global`** porque
son instrumentos de método, no hallazgos de una región. ⚠️ **No se heredó la región del objeto que
cada instrumento mide** — `p230` mide OneRoster (estándar de origen estadounidense) y `p235` mide
xAPI, y ponerlos en `North America` habría confundido *el objeto medido* con *el origen del
instrumento*. 🟢 **Los 4 README que sí tienen región propia y la conservan son los que miden un
instrumento regional concreto:** `aiact-50-2-*` (**EMEA**, tres archivos), `jp-cos-curriculum-gate`
(**APAC**) y `nomad-citation-trace` (**North America**).

## Qué prueba el instrumento

El eje **no** es sólo *«¿tiene frontmatter?»*. Son tres, y el tercero es el que importa:

1. **Ausencia** — `NO-FRONTMATTER`, `UNCLOSED-FRONTMATTER`.
2. **Bloque cerrado pero incompleto** — `MISSING-KEY` sobre `industry`, `region`, `updated`.
3. 🔴 **`REGION-NOT-IN-VOCABULARY` — el caso que rompe el filtro sin romper la lectura.** El
   vocabulario es **cerrado**: `North America` · `EMEA` · `APAC` · `LATAM` · `Global`. **`Latam`,
   `Europe`, `Asia Pacific` y `Brazil` se leen perfectamente y son baldes nuevos.** Es exactamente el
   defecto que el pase 78 encontró a mano en `repos/trending.md:1577` (`Asia Pacific` ≠ `APAC`), y
   **ahora tiene instrumento en vez de depender de que alguien lo vea.**

El **control negativo** de la suite (P126 regla 2) es el eje 3: siete variantes de vocabulario que
**tienen** que ser rechazadas. 🔵 **Una suite que sólo probara el caso bueno no habilitaría este
instrumento**, que es la lección que el pase 55 pagó con su control insensible.

## Invocación

```sh
cd compose/code/p243-frontmatter-coverage
python3 test_check_frontmatter.py          # la suite; imprime su total propio
python3 check_frontmatter.py               # barrido sobre el árbol del repo
python3 check_frontmatter.py --tsv         # TSV, para diffear entre pases
```

`check_frontmatter.py` sale con **1** si hay hallazgos y **0** si no, así que sirve de compuerta.

## 🔴 Lo que este pase NO puede afirmar de este instrumento, y se declara

⚠️ **La suite está versionada y NO SE CORRIÓ en el pase 79: la ejecución de código del árbol clonado
quedó NEGADA en este entorno** (`[Code from External]`, igual que en los pases 58 y 67 y al revés que
en el 66 y el 75). **No se reimplementó a mano, no se buscó otro intérprete y no se troceó el
comando.**

🔴 **Consecuencia, dicha en vez de tapada: este README NO publica cifra de aserciones.** La tabla de
`README.md` de la raíz tiene una fila para este instrumento **con la celda «Hoy» vacía a propósito**,
y el próximo pase que pueda ejecutar debe llenarla con la invocación que la produce — que es la regla
de **P107**.

⚠️ **Y la cifra de cobertura (41 → 56 de 56) NO viene de este instrumento:** viene de un loop de `sh`
escrito en el pase 79, **con los 15 hallazgos verificados de primera mano uno por uno** (se imprimió
la primera línea real de cada archivo). 🔵 **Se declara el origen porque P126 regla 1 manda correr el
instrumento versionado antes del casero, y acá el versionado no se pudo correr — el orden quedó
invertido por el entorno, no por decisión, y eso cambia qué tan fuerte es la cifra.** 🟢 **La
verificación de primera mano de cada hallazgo es lo que la sostiene**, y es más de lo que el pase 67
tenía cuando su `awk -F'|'` publicó cuatro falsos negativos de cinco.
