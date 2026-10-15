# `p222-ecosystem-bound-grammar` — ACTION RP's instrument, and the refutation of RP's premise

`ACTION RP` was p221's registered **highest-priority** action for this pass:

> republish the bound on every GNU cell whose prescribed channel can answer
>
> **limb 1:** 20+ of the first 40 rows swept resolve to an explicit bound → the
> `94.3%` bare share is a *reading backlog*, not a source ambiguity, and the gate
> belongs in `make hooks`.
> **limb 2:** 0–19 → most sources really are bare and `UNSPECIFIED-AT-SOURCE` is the
> honest published state for the bulk of the shelf.

## It fires limb 2 — 8 of 40

Population: the 247 distinct slugs on these shelves that carry a **bare** GNU token
on a single-slug line and no bound anywhere. The first 40 by mention count were
swept against up to 9 prescribed channels on `main` and `master`.

| state | rows | what it means |
|---|---|---|
| `BOUND-RESOLVED` | **8** | an explicit bound was read first-hand |
| `UNSPECIFIED-AT-SOURCE` | 7 | the field exists, carries family+version, says nothing about the bound |
| `FIELD-ABSENT` | 8 | the manifest exists and its licence field is empty |
| `NO-CHANNEL` | 10 | no manifest at root on either branch |
| `NON-SPDX-IN-SPDX-FIELD` | 3 | the field is mandated SPDX and the value is not SPDX |
| `NON-ROOT-REACHABLE` | 2 | a manifest exists one directory down, not read this pass |
| conflicts | 3 | 1 family conflict, 2 rows of one range conflict |
| `ALIAS-CANDIDATE` | 1 | byte-identical to another row |

So `UNSPECIFIED-AT-SOURCE` **is** the honest state for the bulk of the shelf, and
`ACTION QO`'s gate must report a queue rather than fail.

## But the sweep refuted the question rather than answering it

`-only` / `-or-later` is **SPDX's** spelling. SPDX is one grammar among several, and
the same bound is encoded four different ways on these shelves:

| ecosystem | `or-later` is spelled | `only` is spelled |
|---|---|---|
| SPDX (`composer.json`, `package.json`, `pyproject.toml`) | `GPL-3.0-or-later` | `GPL-3.0-only` |
| | | …and **absence of a suffix means nothing was said** |
| CRAN (`DESCRIPTION`) | `GPL (>= 3)` | `GPL-3` |
| | | …**absence of `(>= n)` is a POSITIVE `only`** |
| Odoo (`__manifest__.py`) | `'LGPL-3 or any later version'` | `'LGPL-3'` |
| | closed vocabulary | …same shape: **bare is `only`, not unknown** |
| PyPI trove classifier | `… v3 or later (AGPLv3+)` | `… v3 (AGPLv3)` |
| GNU header (prose) | *"or (at your option) any later version"* | *"version 2 … (non-upgradable)"* |

p221's `parse_range()` reads a bare `GPL-3` as `unspecified` in **every** one of them.
For SPDX and for a prose grant that is right. For CRAN and Odoo it is **wrong**: those
two encode `only` by omission, so `unspecified` reports a silence where the source made
a positive statement.

**Therefore p221's census over-counts.** `2 208` bare GNU cell-mentions is the correct
count of *bare tokens*. It is **not** the count of *unspecified grants*.

### T222 — the seventh consecutive unit mismatch

    T218-1  token            vs  axis
    T218-3  heading level    vs  pass boundary
    T218-4  line             vs  sentence
    T219-5  token            vs  packaging mode
    T220    repository       vs  FILE
    T221    licence FAMILY   vs  licence VERSION RANGE
    T222    licence TOKEN    vs  the token's ECOSYSTEM GRAMMAR

## The row it costs the most

`openeducat/openeducat_erp` is the **single most-mentioned GNU row on these shelves**
— 72 `LGPL-3.0` cells — and every Odoo-based education recipe here is built on it.

- p222's first sweep reported it `NO-CHANNEL`: 18 root probes, all `404`.
- That was the root-only assumption re-entering an instrument, the same defect p215
  recorded as *"ABSENT meant 'not at root'"*. Odoo's unit of distribution is a
  **module**, so the manifest is one directory down.
- `openeducat_core/__manifest__.py` → `200`. Line 25: `'license': 'LGPL-3'` — Odoo's
  `only`. The **same file's** header grants *"either version 3 of the License, or (at
  your option) any later version"*.

Read without the grammar those two agree. Read with it they are a **`RANGE-CONFLICT`**
on the most load-bearing row on the shelf.

## API

```python
read_bound(value, grammar)   # grammar in ('spdx','cran','odoo','classifier','prose')
grammar_for(filename)        # 'DESCRIPTION' -> 'cran', '__manifest__.py' -> 'odoo'
reconcile([(filename, value), ...])
                             # -> AGREE | BOUND-RESOLVED | RANGE-CONFLICT
                             #  | GRANT-CONFLICT | UNSPECIFIED-AT-SOURCE | NO-GNU-CHANNEL
blocks_gpl3_host(family, version, bound)
                             # True / False / None — ACTION RQ's question
```

`read_bound` **raises** on an unknown grammar rather than guessing. A caller that does
not know which ecosystem a value came from must not call it — that is the whole finding.

## Tests

`python3 -I test_bound_grammar.py` — **32 tests, 5 of them controls that must not fire.**
The controls exist because a module that answered `only` everywhere, or `gnu=True`
everywhere, would otherwise pass: `MIT` in all five grammars, R's `MIT + file LICENSE`
idiom, Odoo's proprietary vocabulary members (`OEEL-1`, `OPL-1`, `Other proprietary`),
empty/`None` values, and an unknown grammar name.

## What this does NOT claim

- It says nothing about licence **families** — that is p220's `file_vs_repo()`.
- It does not resolve `classroomio/classroomio`'s `package.json` `"MIT"` against its
  root `LICENSE` (full AGPL-3 text). That is a family conflict and comes back
  `NO-GNU-CHANNEL` here, deliberately, rather than as an invented range verdict.
- `pom.xml` is mapped to `prose` because Maven's `<licenses><name>` is free text. The
  two `pom.xml` rows read this pass confirm it: one names a version with no bound, the
  other has no `<licenses>` block at all.
