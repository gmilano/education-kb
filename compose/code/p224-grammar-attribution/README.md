# `p224-grammar-attribution` — `ACTION RU`'s instrument, and two defects it found in itself

`ACTION RU` was p222's registered **highest-priority** action for p223, carried unrun into
p224 with the note *"p224 has no excuse"*. It asks whether p221's headline survives p222's
correction:

> re-run p221's census **under the ecosystem grammar**
>
> **limb 1:** `50`+ of the `2 208` bare GNU mentions attach to a row whose grant was read
> from a CRAN `DESCRIPTION` or an Odoo `__manifest__.py` → the headline `94.3%` must be
> restated and p221's census republished with a grammar column.
> **limb 2:** `0`–`49` → the grammar finding is real but numerically small, and `94.3%`
> stands as a token count with a footnote.

## It fires limb 1 — `81`

| population | bare GNU mentions | limb |
|---|---|---|
| **STRICT** — grant actually read from a CRAN `DESCRIPTION` or an Odoo `__manifest__.py` | **`81`** *(`80` Odoo + `1` CRAN)* | **1** |
| WIDE — row sits in one of those ecosystems, manifest not yet read | `101` | 1 |

`80` of the `81` are one row: [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp),
whose bound p222 read from `openeducat_core/__manifest__.py` l.`25` as `'license': 'LGPL-3'`
— Odoo's **`only`** form. `1` is `dexter-psychometrics/dexter`, CRAN's `LGPL-3`.

**So the restatement is specific:** those `81` mentions are not silences awaiting a read.
They are **positive `only` grants**, already stated, in a grammar p221's `parse_range()`
could not see. `94.3%` remains a true count of bare *tokens* and is not a count of
unspecified *grants*.

### The verdict is robust to the unit, which matters because the unit is what moved

| unit of enumeration | numerator | limb |
|---|---|---|
| table **cell** *(line begins `\|`)* | `71` | 1 |
| **token occurrence** anywhere, before the dependency guard | `83` | 1 |
| token occurrence, after the dependency guard | `81` | 1 |

The cell count independently corroborates p222's separately-derived *"`72` bare `LGPL-3.0`
cells"* on the same row, from a different instrument, to within one cell.

## 🔴 The denominator does NOT reproduce, and that is a finding

This module **imports p221's `parse_range()` by path** so that "bare" means exactly what it
meant when `2 208` was published. It still does not reproduce p221's population:

| | p221 | p224 | corpus |
|---|---|---|---|
| GNU mentions | `2 342` | `4 152` | `120 296` → `121 085` lines *(+`789`)* |
| bare | `2 208` | `3 582` | |

`789` more lines cannot produce `1 374` more mentions. **Importing a prior instrument's
*predicate* does not reproduce its *population*, because the unit of enumeration lives in
the runner, not in the predicate** — p221 counted cell-mentions, this counts token
occurrences anywhere including prose. So the `94.3%` **ratio** is not reproducible from the
published artefacts; only `ACTION RU`'s **numerator** question is, and it is the numerator
the limbs are stated in. A census that publishes a ratio should publish its enumerator.

## Two defects this instrument found in itself

### `T224-2` — the phantom host slug, which would have produced a false limb `2`

The first run attributed nothing where it should have attributed most. A URL
`https://github.com/openeducat/openeducat_erp` yielded the **phantom row**
`github.com/openeducat` *beside* the real one, so a line naming **one** row looked like a
line naming **two**, went to `bare_ambiguous_line`, and dropped out of attribution. The
phantom is already visible in the shelves' own grep counts: `112` × `github.com/openeducat`,
`15` × `github.com/odoo`.

🟢 **The fix is a rule, not a blocklist: a GitHub account name is alphanumeric-and-hyphen,
so a dotted "owner" is always a hostname.**

### `T224-3` — the dependency-scoped token: the unit is the grant's SUBJECT

`repos/trending.md` l.`12548` names exactly **one** row —
`CambridgeAssessmentResearch/KernEqWPS`, an **`MIT`** package — and the tokens `GPL-2` and
`GPL-3` on that line belong to its R dependency **`MASS`**. The single-slug guard cannot
see it: the line names one row, and the token's real subject is not a GitHub slug at all.
Counting them put the numerator at `85` against a true `83`.

🔵 **This is p222's false-`GRANT-CONFLICT` defect in a second shape**, and the rule
generalises: **the unit is the grant's SUBJECT, not the row sharing its line.** Ninth
consecutive unit mismatch in this KB's headline series — and the first found in this KB's
own live output *before* publishing it rather than a pass later.

## States it publishes rather than hides

| state | count | why it is not zero |
|---|---|---|
| `bare_attributed` | `1 773` | a bare token on a line naming exactly one row |
| `bare_no_slug_on_line` | `1 442` | prose mentions — real, unattributable, and not a defect |
| `bare_ambiguous_line` | `367` | line names 2+ rows; p222's defect guard, deliberately not guessed |
| `dependency_scoped` | — | `T224-3`; the row's own grant is not in question |

## Files

| file | what it is |
|---|---|
| `grammar_attribution.py` | the predicate + attribution; imports p221's `parse_range()` |
| `run_census.py` | the runner; builds the grammar map **from evidence TSVs on disk**, not hardcoded |
| `selfclaim_table_gate.py` | `ACTION SA`'s deliverable — p223's gate generalised to a table |
| `test_grammar_attribution.py` | `24` tests, `14` of them controls that must **not** fire |

Evidence: [`ru-grammar-census`](../../../evidence/ru-grammar-census.2026-10-15-p224.tsv) ·
[`sa-refuted-claims`](../../../evidence/sa-refuted-claims.2026-10-15-p224.tsv)

## `ACTION SA` — limb `2`, with the harness built anyway

`SA` asked whether p223's single-purpose date gate should become general: limb `1` was
`2`+ **other** refuted claims re-asserted in live prose.

🔴 **It fires limb `2` at `0`.** The generalised gate, driven by a three-subject table
(`sa-refuted-claims`), reports **`0` `ASSERTED`, `5` `ATTRIBUTED`** across the `8` shelf
files — every live hit is this KB **quoting** a claim it elsewhere refutes, which is
permitted and is what a conflict cell looks like. p223's own gate also now reports `0`/`0`,
so **p223's fix held**.

🟢 **The table is kept regardless, with its purpose restated:** not a general defect
detector, but a **regression harness** on three subjects (the AI Act date, p221's `94.3%`,
openeducat's bound) that will fire if a later pass re-asserts one. `9` controls, `6` of
which must not fire.
