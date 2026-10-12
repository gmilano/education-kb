---
industry: education
region: EMEA
updated: 2026-10-12
---

# `p141-schema-location` — `ACTION CX`: the decision log is real, learner-linked, and immutable in the database

**Subject:** [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp), MIT,
HEAD `368d637` **2026-10-10**, 459 commits.
**Region:** 🟢 **EMEA** — 76 commits at `+0200`, zero at any non-`+0000` offset outside it
([`p141-repo-origin-layer`](../p141-repo-origin-layer/README.md)).

## The action, as p140 wrote it

> Resolve where `tutor-mcp` defines `pedagogical_decisions`. The table is absent from
> `db/schema.sql` while `db/pedagogical_decisions.go` and `get_decision_replay_summary` both
> exist, so the *"auditable pedagogical decisions"* half of `ACTION CT` is only half answered.
> 🔴 *Refuted if the decision log turns out to persist no learner-linked row at all — which
> would make `P19`'s audit-trail claim rest on the affect tables alone.*

## Verdict: 🔴 **DISCHARGED, NOT REFUTED** — and the answer is stronger than p140 expected

`pedagogical_decisions` is declared in **`db/pedagogical_contract_schema.go`**, as a Go string
constant holding DDL that is applied as a migration body. Not in any `.sql` file.

It is learner-linked in the strongest available sense, so the falsifier does not fire:

```sql
CREATE TABLE pedagogical_decisions (
    id TEXT PRIMARY KEY,
    tenant_id TEXT NOT NULL REFERENCES tenants(id),
    learner_id TEXT NOT NULL REFERENCES learners(id),
    domain_id TEXT NOT NULL REFERENCES domains(id),
    session_id TEXT NOT NULL REFERENCES learning_sessions(id),
    curriculum_version INTEGER NOT NULL CHECK (curriculum_version >= 1),
    snapshot_json TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (tenant_id, learner_id) REFERENCES learners(tenant_id, id),
    FOREIGN KEY (domain_id, curriculum_version) REFERENCES curriculum_versions(domain_id, version)
);
```

🟢 **And three guarantees sit on top of it, in the database rather than in application code:**

| guarantee | mechanism | engine |
|---|---|---|
| 🟢 **append-only** | `CREATE TRIGGER pedagogical_decisions_no_update BEFORE UPDATE … RAISE(ABORT, 'pedagogical decisions are immutable')` | SQLite |
| 🟢 same | `CREATE FUNCTION tutor_immutable_pedagogical_decision() … RAISE EXCEPTION` + `BEFORE UPDATE … FOR EACH ROW` | Postgres |
| 🟢 **tenant isolation that the owner cannot bypass** | `ENABLE ROW LEVEL SECURITY` **and** `FORCE ROW LEVEL SECURITY`, policy on `current_setting('app.current_tenant')` | Postgres |
| 🟢 **one decision per graded attempt, immutably bound** | `assessment_attempts.decision_id REFERENCES pedagogical_decisions(id)`, `CREATE UNIQUE INDEX idx_assessment_decision_once … WHERE decision_id IS NOT NULL`, plus `assessment_decision_immutable` and `assessment_decision_identity_immutable` triggers | both |

🔵 **The last row is the one worth stealing.** `assessment_decision_scope` refuses an insert
unless the attempt's concept and activity type match the decision's own snapshot:

```sql
AND json_extract(p.snapshot_json, '$.contract.target_concept') = NEW.concept_id
AND json_extract(p.snapshot_json, '$.contract.recommended_activity_type') = NEW.activity_type
```

🟢 **So the recommendation a learner was given and the assessment they were graded against are
bound to each other at write time, at the pinned curriculum version, and neither side can be
edited afterwards.** That is what "auditable pedagogical decision" has to mean to survive an
EU AI Act **Article 14** / **Annex III** review, and it is enforced by the engine, not promised
by a maintainer. `P19` does **not** rest on the affect tables.

## 🔴 The larger finding: 96 of 118 tables are invisible to a `.sql` reader

p140 said the table is *"absent from `db/schema.sql`"*. That is true of the file and misleading
about the project. `db/schema.sql` and `db/schema_pg.sql` both exist — and between them hold a
**minority** of the schema.

| population | tables |
|---|---|
| `db/*.sql` | **22** |
| `db/*.go` (non-test, 60 files) | **111** |
| 🔴 **`GO_ONLY` — declared only in Go source** | 🔴 **96** |
| `SQL_ONLY` | 7 |
| `BOTH` | 15 |
| distinct total | **118** |

🔴 **A reviewer who reads `db/*.sql` — the conventional place, and the only place a
schema-diff tool looks — sees 22 of 118 tables (19%).**

🔵 **And the split falls across a DPIA, not along it.** The identity half is in `.sql`; the
audit half is not:

| table | `.sql` | Go | where |
|---|---|---|---|
| `learners` *(holds `email TEXT UNIQUE NOT NULL`)* | 🟢 yes | no | `SQL_ONLY` |
| `interactions` | 🟢 yes | no | `SQL_ONLY` |
| `affect_states` *(the psychological profile of `ACTION CT`)* | yes | yes | `BOTH` |
| 🔴 `pedagogical_decisions` | **no** | yes | `pedagogical_contract_schema.go` |
| 🔴 `assessment_attempts` | **no** | yes | `postgres.go` |
| 🔴 `audit_events` | **no** | yes | `postgres.go` |

🔴 **So the whole audit layer is `GO_ONLY`.** An records-of-processing exercise that enumerates
`db/*.sql` finds the learner's email and misses every table that records what was decided about
them — the opposite of the omission one would guess. Nothing in the repository layout signals
this, and the project is not at fault for it: Go-embedded migrations are ordinary practice. The
defect is in the *review method* this KB has been assuming, and it generalises to every Go, Rust
or TypeScript component on these shelves.

## 🔴 A correction this probe made to itself

The first draft reported **112** tables in Go and **97** `GO_ONLY`. Both were one too high. The
regex matched a line of `db/postgres.go` that quotes DDL in prose:

```go
// Serialize migration across the fleet. CREATE TABLE IF NOT EXISTS is not
```

...producing a table named **`is`**. 🔵 **A comment that quotes DDL is not DDL.** Comments are
now stripped before matching — while Go backtick raw strings are deliberately **kept**, since
that is exactly where the DDL lives — and `test_schema_location.py` pins that line verbatim as
a fixture. The figures published above and in `result.2026-10-12-p141.tsv` are the corrected
ones; the uncorrected ones appear nowhere else in this KB.

🔵 This is the second consecutive pass in which an instrument's first draft was wrong in the
inflating direction and the published number is the smaller one. p140's was `SERVER_CTOR`;
this one is `CREATE TABLE … is not`.

## Reproduce

```sh
git clone https://github.com/ArnaudGuiovanna/tutor-mcp /tmp/tutor-mcp
python3 -I schema_location.py /tmp/tutor-mcp    # TSV on stdout, totals on stderr
python3 -I test_schema_location.py              # 11 tests, including the `is` regression
```

Committed: [`result.2026-10-12-p141.tsv`](result.2026-10-12-p141.tsv) (118 rows),
[`detail.2026-10-12-p141.txt`](detail.2026-10-12-p141.txt) (the totals as run).
