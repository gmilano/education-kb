---
industry: education
region: Global
updated: 2026-10-12
---

# `p142-schema-location-tiers` — `ACTION DD`: `T31` survives, and the instrument behind it does not generalise

## The action, as p141 wrote it

> Test `T31` on a **second** non-`.sql` component: run `p141-schema-location` over
> `nitsuah/bb-mcp` (TypeScript) and one Python education component as a control, and report the
> `.sql`-visible share for each. 🔴 *Refuted if the majority of tables in the second component
> are declared in `.sql` — which would make `T31` a property of `tutor-mcp` rather than of
> embedded-migration stacks, and it must then be withdrawn rather than narrowed.*

## 🟢 The control first: the generalised probe reproduces p141 to the digit

p141's probe globs `db/*.sql` and `db/*.go`. 🔴 **That is not a method, it is one project's
directory layout** — run unchanged elsewhere it returns zero tables, and the honest reading of
that zero is "the probe looked in the wrong place". So the population here is the whole tracked
tree, partitioned by extension, with vendored, generated and test trees excluded.

| subject | languages | tables | in `.sql` | share | verdict |
|---|---|---|---|---|---|
| 🟢 `ArnaudGuiovanna/tutor-mcp` *(p141's subject, as control)* | go+py | **118** | **22** | **19%** | `MINORITY_IN_SQL` |
| `nitsuah/bb-mcp` | py+ts | 🔴 **0** | 0 | — | 🔴 `NO_DDL_FOUND` |
| `zijinz456/OpenTutor` | py+ts | 1 | 🔴 **0** | 🔴 **0%** | `MINORITY_IN_SQL` |
| `fabrica-de-inovacao/expeditto` | py+ts | 🔴 **0** | 0 | — | 🔴 `NO_DDL_FOUND` |
| `SleepyPandas/UofT-MCP` | py | 🔴 **0** | 0 | — | 🔴 `NO_DDL_FOUND` |

🟢 **118 tables, 22 in `.sql`, 19% — identical to p141 on a differently-written instrument.**
That is what licenses the rest of the table.

## Verdict: 🔴 **DISCHARGED, NOT REFUTED — and `T31` must be RE-CUT rather than confirmed**

The falsifier required *"the majority of tables in the second component declared in `.sql`"*. It
cannot fire, because 🔴 **neither registered subject declares a table in `CREATE TABLE` form
anywhere at all.** The question "where is the DDL?" presupposed DDL.

🔴 **`zijinz456/OpenTutor` has a full schema and a `CREATE TABLE` census finds one table —
`alembic_version`, which Alembic writes for itself.** The real schema is SQLAlchemy:

| measure | value |
|---|---|
| 🔴 **`__tablename__` declarations** | 🔴 **34** |
| model classes (`class X(Base)`) | 148 |
| Alembic migration files | 27 |
| `.sql` files in the tree | 🔴 **0** |
| tables a `CREATE TABLE` reader sees | 🔴 **1 of 35, and it is bookkeeping** |

🔵 **So `T31`'s direction holds and its mechanism is wrong.** In `tutor-mcp` the DDL moved out of
`.sql` into Go string constants — still DDL, still greppable. Here there is no DDL: the schema is
Python classes, and the `.sql`-visible share is not 19% or 100% but undefined. **A `CREATE TABLE`
census is the wrong instrument for the ORM majority of this shelf**, and `T31` is restated as a
claim about *review method* rather than about file extensions.

## 🔴 And the tables OpenTutor declares are the ones a DPIA has to enumerate

`users`, `auth_sessions`, `integration_credentials` — and then
🔴 **`cognitive_baselines`, `concept_mastery`, `mastery_snapshots`, `preference_signals`,
`intervention_outcomes`, `conversation_memories`, `chat_message_logs`, `wrong_answers`.**

🔴 **That is the `PII_AND_AFFECT` class p140 assigned to `tutor-mcp`, on a second row** — and
p141 described this repository only as *"a real, MIT-licensed, active tutoring application"*
with no mention that it persists a per-learner cognitive profile. `agents/top.md` is corrected
this pass.

## 🟢 The one row that comes out of this well

`nitsuah/bb-mcp` has **no persistence of any kind**: 0 tables, 0 models, 0 `.sql`, 0 migrations.
🟢 **For the row this KB already calls "the only connector shipping an access-control layer",
holding no learner data at rest is the other half of the same virtue.**

## Reproduce

```sh
python3 -I schema_tiers.py "name=/path/to/clone" ...
python3 -I test_schema_tiers.py    # 13 tests, incl. p141's `CREATE TABLE … is not` fixture
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv),
[`detail.2026-10-12-p142.txt`](detail.2026-10-12-p142.txt).
