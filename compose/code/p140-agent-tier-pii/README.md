---
industry: education
region: Global
updated: 2026-10-12
---

# `p140-agent-tier-pii` — `ACTION CT`: the agent tier holds an email AND a per-session psychological profile, and it ships its own high-risk gate

**Executes p139's pre-registered `ACTION CT`**, written as:

> Read **`ArnaudGuiovanna/tutor-mcp`** in source: what its "durable learner state" and
> "auditable pedagogical decisions" actually persist, and whether any of it is a write surface
> of the `P18` class. 🔴 *Refuted if the agent tier turns out to hold no learner PII at all,
> which would put it outside the Annex III/Decision 33 frame this KB has been applying.*

## Verdict: **DISCHARGED, NOT REFUTED — `PII_AND_AFFECT`**

| measure | value |
|---|---|
| tree paths | 687 |
| Go source / test files | 279 / 🟢 **286** — *more test files than source files* |
| registered tools (non-test) | **55** |
| 🔴 write tools | **27 (49%)** |
| documented in `docs/mcp-tools.md` | 46 |
| 🟡 undocumented | **9** — *all of one tier; see below* |
| 🔴 undocumented **writes** | **3** |
| schema tables | 36 |
| 🔴 tables with a direct identifier | **1** — `learners.email` (`TEXT UNIQUE NOT NULL`) |
| 🔴 tables with affective state | **2** |
| human-oversight tool | 🟢 `mark_domain_high_stakes` |
| 🟢 inverse tool to clear it | **NONE** |

Licence **MIT**, `Copyright (c) 2026 Arnaud Guiovanna`, status **alpha**, Go 1.26.9, built on
the official `github.com/modelcontextprotocol/go-sdk v1.8.0`.

## 🔴 `P140-E1` — the falsifier fails twice, and the second way is the one that matters

**PII is present:** `learners.email` is `TEXT UNIQUE NOT NULL` — a direct identifier, not a
pseudonym.

🔴 **And `affect_states` persists a per-session psychological profile**, keyed
`UNIQUE(learner_id, session_id)`:

```sql
CREATE TABLE IF NOT EXISTS affect_states (
    learner_id           TEXT NOT NULL REFERENCES learners(id),
    session_id           TEXT NOT NULL,
    energy               INTEGER DEFAULT 0,
    subject_confidence   INTEGER DEFAULT 0,
    satisfaction         INTEGER DEFAULT 0,
    perceived_difficulty INTEGER DEFAULT 0,
    next_session_intent  INTEGER DEFAULT 0,
    autonomy_score       REAL DEFAULT 0,
    ...
    UNIQUE(learner_id, session_id)
);
```

plus `interactions.confidence`. 🔵 **This is not adjacent to the regime this KB tracks — it is
the exact element of it.** p138 added to `T16` that **Vietnam's Decision 33/2026/QĐ-TTg names
psychological assessment in its education high-risk list**, and `EU AI Act Annex III` names
grading or ranking learners. This row persists both: affective state *and*
`submit_assessment_attempt` / `check_mastery` / `get_cohort_statistics`. 🔴 **A deployment of
this row is inside both regimes on the strength of its schema alone.**

## 🟢 `P140-E2` — the first row on this shelf that SHIPS a high-risk control instead of needing one

`mark_domain_high_stakes` is a one-way safety classification, and its own description states
the evidence policy:

> *"Apply the one-way high-stakes safety classification to an owned active domain. Demonstrated
> claims and intrusive suggestions then require a trusted human-reviewed evaluation; no
> external evaluator is created or assumed."*

Once set, the tool returns `demonstrated_claims_allowed: false`,
`intrusive_notifications_allowed: false`, and:

> `"policy": "trusted human_review evidence is required; host_llm and external_service`
> `evaluations do not satisfy this gate"`

🟢 **The one-way claim is real, and it is implemented by the ABSENCE of an inverse tool.**
This probe searched for one — `unmark_*`, `clear_*`, `unset_*`, `reset_*` — and found **none**.
`db/store.go` says why, above `MarkDomainHighStakes`:

> `// Downgrading safety classification requires an operator-controlled process that is`
> `// outside the learner-facing MCP trust boundary.`

🔵 **That is human oversight expressed as a tool contract**, which is what EU AI Act Article 14
requires and what Oklahoma's and Maryland's statutes mean by "human oversight and no AI
high-stakes decisions about students". 🔴 **Every other row this KB has measured needed a gate
wrapped around it. This one ships the gate** — which makes it a pattern donor rather than
merely a shelf row, and it is why `P19` exists.

## 🟡 `P140-E3` — the 9 "undocumented" tools are a TIER, not drift, and the distinction cuts both ways

The 9 are `draft_formation`, `publish_formation`, `add_formation_concepts`,
`get_formation_version`, `get_learner_formation`, `get_learner_progress`,
`get_cohort_insights`, `get_cohort_statistics`, `list_trainer_cohorts`. 🔵 **They are not a
random residue — they are exactly the institution/trainer tier**, and `RegisterTools` gates
all of them behind one flag:

```go
if deps != nil && deps.Institution {
    registerFormationTools(server, deps)
    registerProgressTools(server, deps)
    registerLearnerFormationTools(server, deps)
    registerBadgeTools(server, deps)
}
```

🟢 **So this is NOT the `p139-tool-count-drift` finding repeated.** On the npm shelf, 62
undocumented tools were *registered and served* while the README stayed silent — undisclosed
capability. Here the undocumented tools are **not registered at all** in the default
deployment, and `docs/mcp-tools.md`'s 46 matches the default surface. 🔵 **Tiering is the
better-engineered shape, and calling it drift would have been the easy wrong answer.**

🔴 **It still leaves a real gap.** Turn `Institution` on and three undocumented **writes**
become live — `draft_formation`, `publish_formation`, `add_formation_concepts`, which author
and publish the curriculum a cohort is taught against. 🔵 **An institutional buyer enables
precisely the tier its documentation does not cover.** That is the finding to put in front of
one, and it is narrower and more useful than a count.

## Cross-reference: this row answers `ACTION CP` where the npm shelf could not

The gating above, plus `REGULATION_GOAL` and `deps.OAuthGranularScopes`, is why a live
`tools/list` on this row returns **46** by its own CI-enforced test assertion
(`tools/tools_register_test.go:221`) against **55** names in the build. See
[`p140-live-surface-bound`](../p140-live-surface-bound/README.md).

## 🟡 Naming collision worth recording

🔴 **`ArnaudGuiovanna/tutor-mcp` has nothing to do with `overhangio/tutor`.** The latter is the
Open edX deployment tool (AGPL-3.0, now Edly's); this is an independent MIT adaptive-learning
MCP engine. Both appear in this pass for unrelated reasons, and the shared word "tutor" is the
only thing they have in common.

## Limits

- 🔴 **Nothing was executed.** The clone is read as text; the 46 figure is the subject's own
  test assertion, not a `tools/list` this pass called.
- The affect/PII patterns are column-name heuristics over `CREATE TABLE` bodies. They find
  what they name and would miss an identifier stored under an unexpected column name, so the
  PII count is a floor.
- `db/pedagogical_decisions.go` exists and `get_decision_replay_summary` is registered, but
  the `pedagogical_decisions` table is not in `db/schema.sql`; the "auditable pedagogical
  decisions" half of `ACTION CT` is therefore **only partly answered**, and that is stated
  rather than rounded up. Where the decision log is defined is open for the next pass.

## Reproduce

```sh
git clone --depth 1 https://github.com/ArnaudGuiovanna/tutor-mcp
python3 -I agent_tier.py tutor-mcp
```
