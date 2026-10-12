---
industry: education
region: Global
updated: 2026-10-12
---

# `p145-licence-census` — `ACTION DX`: the falsifier is silent, and the npm tier ships declarations rather than grants

🟢 **`ACTION DX` DISCHARGED, falsifier silent.** 🔴 **9 of 52 rows carry no licence at
all** — more than double the threshold that would have made `P144-Q`'s two a coincidence.
🔴 **And 18 of 52 ship no grant a client can rely on.**

## What was registered

> 🟢 **`ACTION DX`** — count how many of the 44 connector rows are UNLICENSED. `P144-Q`
> found two by accident while verifying something else, and one of them is the largest
> tool surface on its tier. Read the licence file at HEAD for all 44 rows and all 8 npm
> packages.
> 🔴 *Refuted if fewer than 4 rows are unlicensed* — which would make `DAU-buddy` and
> `aula-virtual-mcp` a coincidence rather than a property of this population.

## 🔴 Result: it is a property of the population

| grant | rows | what a client gets |
|---|---|---|
| 🟢 `FILE` — a licence file at HEAD | **34** | a grant |
| 🔴 `PKG_ONLY` — declared in `package.json`, no file | **7** | 🔴 **an identifier, not a grant** |
| 🔴 `README_ONLY` — prose in a README | **2** | weaker still |
| 🔴 `NONE` — no file, no declaration, no prose | **9** | 🔴 **nothing. No grant, no build** |

🔵 **Two readings of "unlicensed" are reported separately, because the registered question
has two defensible answers and this probe should not quietly pick one:**

- 🔴 **strict — 9 of 52 (17%)**: no file, no declaration, nothing.
- 🔴 **no shipped grant — 18 of 52 (35%)**: the above plus declaration-only and
  README-only.

**Either number clears the threshold of 4.** `P144-Q`'s `Piyushtanwani/DAU-buddy` and
`ruud0/aula-virtual-mcp` are two of eight such rows on the 44-row tier.

## 🔴 The eight connector rows that carry no licence at all

| row | note |
|---|---|
| `Piyushtanwani/DAU-buddy` | 🔴 **40 literal tools** — the largest tool surface on the github-only tier, found by `P144-Q` |
| `ruud0/aula-virtual-mcp` | 🔴 placed to **EMEA (Universidad de Navarra)** by `P144-K`, and unbuildable |
| `karkarkins/BlackboardAssistantMCP` | 🔴 the row `ACTION DK` **placed** in p143 — placed, and unlicensed |
| `MatheusMach/QuantoFalta` | — |
| `P1ckle3/blackboard-mcp` | — |
| `SIU-Toba/docker-guarani` | 🔴 the **SIU-Guaraní** containerisation, on the LATAM platform tier |
| `eugeborzone/Auto_Grade_Guarani` | 🔴 an **auto-grading** row: the EU high-risk use case, no grant |
| `frjunioalves/suap-mcp` | 🔴 **SUAP**, on the Brazilian platform tier |

🔵 **Three of the eight are on the LATAM system-of-record tier** (`docker-guarani`,
`Auto_Grade_Guarani`, `suap-mcp`), which is the tier this KB most often recommends as an
entry point. 🔴 **That is a delivery finding, not a bookkeeping one.**

## 🔴 The tier property: npm ships a declaration and calls it a licence

| npm package | grant | licence |
|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 `README_ONLY` | MIT |
| `@ink-waffle/moodle-mcp` | 🔴 `PKG_ONLY` | MIT |
| `@n35da/brightspace-mcp` | 🔴 **`NONE`** | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `PKG_ONLY` | MIT |
| `canvas-mcp-server` | 🔴 `PKG_ONLY` | MIT |
| `eth-moodle-mcp` | 🔴 `PKG_ONLY` | MIT |
| `mcp-canvas-lms` | 🔴 `PKG_ONLY` | MIT |
| `moodle-mcp-server-aql` | 🔴 `PKG_ONLY` | 🔴 **AGPL-3.0** |

🔴 **Zero of eight ship a licence file.** 🔵 **`T21` said the npm tier's licence *payload*
rate was 33%; this probe says the npm tier's licence *file* rate at HEAD is 0%** — and the
two are consistent, because `npm pack` includes a `LICENSE` only if one exists to include.

🔴 **`moodle-mcp-server-aql` is the row that stops a build**: it declares **AGPL-3.0** in
`package.json` with no licence text behind it, and it is also the one row on this shelf
whose tool surface is **extended by plugins at run time** (`P145`'s
`JS_LIST_HANDLER_MUTATED`). 🔵 **A copyleft declaration with no text is the worst of both
worlds** — it deters use without granting anything.

## Copyleft rows, named so nobody builds on them by accident

🔴 **7 of 52**: `Agso-o/sigaa-calendar`, `despedite/siu-guarani`, `edwyj/ddl-killer`,
`fabrica-de-inovacao/expeditto`, `mhlavac/edupage-mcp`, `qxbao/qldt-hanu-mcp`, and
`moodle-mcp-server-aql` (declared only).

🔵 **Four of the six repository rows are LATAM or APAC system-of-record connectors**, which
is where this KB sends engagements. 🟢 **Globant can read them; it cannot fold them into a
client deliverable without accepting the obligation.**

## Why the test is not `ls LICENSE`

🔴 **A licence identifier is not a licence** — `P138` established that, and this probe keeps
the distinction in the output rather than collapsing it. The body is identified from its
own text (`BODY_HINTS`) *before* any SPDX string in it is trusted, because a file saying
"MIT" in a comment above the Apache text is Apache.

## Limits

- 🔴 **Root-level only.** A per-module grant three levels down (`ACTION DF`'s veraPDF
  shape) is not sought here; this probe answers "is there a grant at HEAD", which is the
  question `ACTION DX` asked.
- 🟡 **`UNIDENTIFIED`** is reported rather than guessed when a file exists whose body
  matches no known licence.

## Run it

```
python3 licence_census.py "<subject>=<path>=<tier>" …
```

Results: [`result.2026-10-12-p145.tsv`](result.2026-10-12-p145.tsv),
summary: [`summary.2026-10-12-p145.txt`](summary.2026-10-12-p145.txt).
