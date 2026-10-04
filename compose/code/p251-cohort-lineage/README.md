---
industry: education
region: Global
updated: 2026-10-04
---

# `p251-cohort-lineage/` — la topología de un cohorte, medida por tres canales

**Pase 83 del 2026-10-04.** Este instrumento existe por un defecto concreto: **el pase 82 coronó un
padre que las mediciones de los pases 59, 60 y 62 de esta misma base ya contradecían**, y lo coronó
razonando desde la **ausencia de menciones en el índice propio** (`r-huijts/canvas-mcp` tenía CERO
coincidencias en los 57 `.md`, y el archivo citaba 18 piezas Canvas-MCP → *«es el padre de la capa»*).

🔴 **Una ausencia en el índice propio es un hecho sobre el índice, no sobre el mundo.**

## Qué mide, y por qué tres canales

| Canal | Qué contesta | Fuerza |
|---|---|---|
| `sha256` del `LICENSE` | ¿comparten el archivo byte a byte? | 🔵 **MISMO TITULAR, no linaje** — ver la cota |
| **titular vs DUEÑO del repo** | ¿el titular es el dueño, o un tercero del cohorte? | 🟢 **el discriminador** (eje de `P184`) |
| `package.json` (`name`, `repository`) | ¿a dónde aterriza quien resuelve por paquete? | ⚠️ corrobora, y expone `P190` |

### La cota, declarada antes del resultado

⚠️ **Un `LICENSE` byte a byte idéntico prueba MISMO TITULAR, no linaje.** Dos repos del mismo autor
coinciden sin que ninguno sea fork del otro — y el control 4 de la suite es exactamente ese caso
(`acme/alpha` ↔ `acme/beta`: mismo hash, los dos `ORIGIN-CANDIDATE`, `NO-CLAIM` entre ellos). Por eso
el veredicto sale del **titular contra el dueño**, no del hash.

⚠️ **Y `match_strength()` es una heurística de NOMBRE**, con tres grados declarados
(`STRONG` / `WEAK` / `NONE`). `Christian Bru` ↔ `bruchris` sale **`WEAK`** y se acepta; un titular
colectivo (`Canvas LMS MCP Server Contributors` ↔ `ahnopologetic`) sale **`NONE`** y la fila queda
**`UNDETERMINED`** — *no* `INDEPENDENT`. **La ausencia de correspondencia no es evidencia de
independencia.**

## La compuerta

```
holder ~ owner                      -> ORIGIN-CANDIDATE
holder ~ owner de OTRO del cohorte  -> DERIVATIVE-OF <ese>
holder sin correspondencia          -> UNDETERMINED   (nunca INDEPENDENT)
sin archivo de licencia             -> UNDETERMINED   (nunca INDEPENDENT)
```

`paternity_claim(rows, candidato)` devuelve **`NO-CLAIM`** salvo que el candidato tenga **al menos un
derivado MEDIDO** en el cohorte. **No hay camino por el que una ausencia de menciones produzca
`PARENT`.**

## Invocación

```sh
sh sweep_lineage.sh > rows.tsv     # barrido real (exige canal CALIBRADO, P249: si no, exit 3)
python3 lineage.py rows.tsv        # la topología
python3 test_lineage.py            # la suite
```

🟢 **Hoy: `26/26`** (`Python 3.11.15`, código de salida 0).
🟢 **Barrido real: 17 slugs — 7 `DERIVATIVE-OF` · 6 `ORIGIN-CANDIDATE` · 4 `UNDETERMINED`.**

⚠️ **`sweep_lineage.sh` se niega a correr si el canal no discrimina** (200 a una URL buena **y** 404 a
una inexistente). Es `P249` como precondición y no como comentario: sale `exit 3` antes de emitir una
sola fila.

## El resultado que motivó el instrumento

| Candidato | Veredicto de la compuerta | Derivados MEDIDOS |
|---|---|---|
| `vishalsachdev/canvas-mcp` | 🟢 **`PARENT`** | **6** |
| `bruchris/canvas-lms-mcp` | 🟢 **`PARENT`** | **1** |
| **`r-huijts/canvas-mcp`** | 🔴 **`NO-CLAIM`** | **0** |

🔴 **`r-huijts/canvas-mcp` es un origen legítimo —titular propio, paquete propio, no es fork de nada—
y tiene CERO derivados en el cohorte que esta base cita.** Los 7 del racimo grande preservan
`Copyright (c) 2025 Vishal Sachdev`; **ninguno de los 16 menciona `r-huijts` en su `README`** (control
corrido aparte: 0 coincidencias × 16).

## Lo que este instrumento NO contesta, y el pase lo declara

🔴 **«¿Qué agrega cada fork?» sigue sin instrumento de cohorte.** El pase 82 la midió leyendo
`docs/TOOLS.md` del payload — y **ese archivo existe en 1 de los 17 repos** (sólo en
`r-huijts/canvas-mcp`, 19.578 B). **La medida que produjo «69 tools» y «delta +20» no generaliza al
cohorte**, así que la superficie por fork se sigue leyendo de la prosa de cada `README`, que es
precisamente lo que `P160` desaconseja. Queda como hueco declarado, con su causa medida.
