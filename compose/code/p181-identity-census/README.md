---
industry: education
region: Global
updated: 2026-10-13
---

# `ACTION LK` — the identity census that tests `T290`

**Pass `181` of `2026-10-13`.** `ACTION LK` was pre-registered at p180 with these limbs:

> **limb `1`:** the top-★ rows keep showing OWN identity less often than mid-★ rows → `T290`
> becomes a usable triage rule: sort candidates by tables, not by stars.
> **limb `2`:** identity tracks ★ after all → `T290` was a `3`-row coincidence and must be
> withdrawn like `T286`.

🟢 **LIMB `1` FIRED, on `14` rows rather than the `10` pre-registered.**

| ★ band | rows | own persistence | identity a cohort can use |
|---|---|---|---|
| `≥ 500`★ | `3` | `1` of `3` *(users in a JSON file)* | **`0` of `3`** |
| `< 500`★ | `11` | `8` of `11` | **`7` of `11`** |

The sharpest pair: [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) at `41 000`★ has **no
`users` table**; [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) at
`44`★ has tenants, cohorts, billing events and an audit trail.

## What was measured, and how

* Candidate pool: this KB's own
  [`p865-tag-exhaustion/candidates.input.2026-10-09-p79.tsv`](../p865-tag-exhaustion/candidates.input.2026-10-09-p79.tsv)
  — `16` rows from `topics/ai-tutor`, `topics/intelligent-tutoring-system` and two web searches.
  `14` cloned successfully and were measured.
* Every figure comes from a `--depth 1` clone, word-bounded `git grep -Ilw` over **tracked files
  only**.
* ★ counts are the p79 census and remain **SECONDARY** (`gap 140`: `api.github.com`, `github.com`
  and `codeload.github.com` all `403` through this environment's proxy). They are used only to
  BAND the rows, never as evidence of quality.
* Licence grants are identified by **reading the text**, not by matching a byte size —
  `feedbacksystem`'s `Apache-2.0` is `10 785` B against the canonical `11 358`.

## Files

| file | what it holds |
|---|---|
| `identity_probe.sh` | the probe, with its own defects documented in its header |
| `result.2026-10-13-p181.tsv` | raw per-row measurements, `20` columns |
| `verdicts.2026-10-13-p181.tsv` | the classification, one row per candidate |

## Four defects this pass found in its OWN probe

The probe was run, then the rows were **read**, and the reading contradicted the counting four
times. All four are fixed in `identity_probe.sh`'s header notes; two required re-measurement.

| # | defect | evidence | status |
|---|---|---|---|
| **`1`** | **false ABSENCE — file-extension scope.** `CREATE TABLE` counted only in `*.sql` | `DeepTutor` has `69` in `.py` and scored `0`; `InterviewMentor` has `20` and scored `0` | 🟢 **CONFIRMED, re-measured** |
| **`2`** | **false PRESENCE — unread table names.** Widening the scope then counts teaching fixtures as schema | `InterviewMentor`'s `20` tables are `dim_customer`/`dim_date`/`fact_orders` warehouse exercises; `feedbacksystem`'s German tables are a student SQL playground *(recipes, auctions)* | 🟢 **CONFIRMED.** `T300`: in an EDUCATION corpus, teaching SQL is a product feature, so a table count over-reports by design |
| **`3`** | **false ABSENCE — English-only entity vocabulary** | 🔴 **REFUTED.** `用户` `82` files in `DeepTutor`, `benutzer` `13` in `feedbacksystem`, `utilisateur` `10` in `tutor-mcp`, `usuario` `5` in `mentingo` — every one an i18n catalogue, design doc or fixture. **Every real entity declaration in all `14` rows is English** | 🔴 **FALSIFIED — recorded so it is not re-proposed** |
| **`4`** | **false PRESENCE — binary files.** `git grep -ilw` without `-I` matches binaries | `mentingo` scored `4` files for `lti`: one HTML comment, plus `review.webp`, `ai-mentor-avatar.png` and `content-video.mp4` | 🟢 **CONFIRMED.** `T301`: every capability probe in this repository must pass `-I` |

## The identity axis, now five-valued

p180 published three values. `14` rows needed five.

| shape | rows |
|---|---|
| **OWN, in the schema** | `OpenTutor`, `mentingo`, `tutor-mcp`, `feedbacksystem`, `lumen`, `LTLTutor` |
| **OWN, but FILE-BACKED** | `DeepTutor` — `USERS_FILE` JSON, roles by insertion order, env bootstrap admin |
| **DELEGATED to a service** | `DeepTutor` *(optional PocketBase)*, `feedbacksystem` *(`Keycloak`, `auth0`)* |
| **BORROWED from the host** | `anki-mcp-server` *(p180)* |
| **NONE** | `fsrs4anki`, `education-agent-skills`, `gen-mentor`, `InterviewMentor`, `ai-tutor-app`, `Tutorbot-Spock` |

One row needed a sixth description: [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai)
owns its identity as **`candidate_profiles`**, not `users` — so a `users` probe grades it `0`.
`T309`: the identity probe is a VOCABULARY, and assessment systems say *candidate* where an LMS
says *user*.

## What this census does NOT establish

* 🔴 **No ★ figure here is primary.** The banding is this KB's own earlier census.
* 🔴 **`T290` is about the ROUTE slot only.** `fsrs4anki` at `4 100`★ has `0` tables and that is
  CORRECT — it is a scheduling algorithm. Ranking it low on engagement-readiness says nothing
  against it as a COMPONENT (`T299`).
* 🔴 **No row was executed.** This harness refuses to build or test a cloned subject tree
  (`T303`), so every verdict is static.
* 🔴 **Regional placement comes from trees** — i18n catalogues, design-doc language, institutional
  holders — never from search (`gap 141`, `0` region-originated repositories named by four
  regional prose searches for a second consecutive pass).

## Usage

```
bash identity_probe.sh <clone-root> <slug> <stars>
```

Writes one TSV row to stdout and an evidence block to stderr, so the classification can be read
rather than trusted.
