---
industry: education
region: Global
updated: 2026-10-13
---

# `agent-tool-receipts-port/` — the auditable assessment record, ported and RUNNING

**Pass 183, 2026-10-13, `ACTION LV`, limb `1` FIRED.** 🟢 **`18` checks, `0` failures,
`python3 test_receipts.py`, stdlib only.**

🔵 **Pattern `24` was written at p182 as a reading recommendation: borrow
[`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai)'s *(`MIT`)* audit tables even if
you do not deploy the app.** 🟢 **This folder is that recommendation turned into an artefact a
studio can lift into an engagement.**

🆕 🔵 **The channel finding that made it possible: `T303` bars building or testing a CLONED SUBJECT
tree. It does not bar running code this KB wrote.** 🟢 **This is the first pass to use that
distinction deliberately** — `civil-ai` itself was read, never built; the port is ours and runs.

## What was ported, and from where

🟢 **Source, read at `HEAD 37ba5e2` *(`795` tracked files, `MIT`, `1 067` B)*:**

| source file | what it contributed |
|---|---|
| `web/src/capabilities/database/migrations/032_agent_tool_receipts.sql` | the `agent_tool_receipts` table, verbatim — composite PK, the `5`-value status `CHECK`, `business_idempotency_key`, `lease_epoch`, `version`, both indexes |
| `web/src/capabilities/database/migrations/001_foundation.sql` | `assessment_policy_versions` *(status `CHECK`, `UNIQUE(subject, policy_type, version)`, `content_hash` length `CHECK`)* and `exam_cycle_policy_bindings` — **the `ON DELETE RESTRICT` policy FK** |
| `web/src/modules/agent/adapters/SqliteAgentToolReceiptRepository.ts` | `INSERT OR IGNORE` for an idempotent prepare; the `UPDATE … AND version = ?` guard; the `version !== expected + 1` refusal; the optional lease predicate |
| `web/src/modules/agent/adapters/IndexedDbAgentToolReceiptRepository.ts` | the parent-run guard — `run.status !== 'running'` is a refusal |

## What it enforces

| guard | where | the refusal |
|---|---|---|
| 🟢 **the state machine** | `LEGAL_TRANSITIONS` in `receipts.py` | `prepared → running → succeeded\|failed\|unknown`. **A terminal receipt cannot be re-opened** |
| 🟢 **optimistic concurrency** | `transition_receipt(expected_version=…)` | a stale version raises `StaleWrite`; the new version is written as exactly `expected + 1` |
| 🟢 **the parent-run gate** | same | a receipt cannot advance under a run that is not `running` |
| 🟢 **idempotent prepare** | `prepare_receipt()` | a retried prepare returns `False` and creates nothing |
| 🟢 **the non-erasable rule** | `ON DELETE RESTRICT` | **a policy version a cycle is BOUND to cannot be deleted**; an unbound one still can |

🔵 **One deliberate deviation from the source, flagged in the test output so nobody inherits it by
accident:** 🟡 **`prepared → succeeded` is REFUSED here.** 🔵 **`civil-ai`'s `CHECK` admits any of
the five values in any order; the transition table is this port's addition.** 🟢 **A tool that
succeeded without running is a receipt nobody can explain to an auditor.**

## 🆕 🔴 The two findings the port produced that reading could not

**1. `PRAGMA foreign_keys` is OFF by default in SQLite, and with it off the audit FK is
decorative.**

🔴 **The same schema, loaded on a connection that never opts in, lets a BOUND policy version
delete and leaves an orphan binding.** 🟢 **It is reproduced in a test rather than asserted**
*(`"with foreign_keys OFF the bound policy deletes and leaves an ORPHAN binding"`)*.
🔵 **Consequence for Pattern `24`: the verification step is not *"the migration has the FK"*. It
is *"a live connection refuses the delete."*** 🟢 **Check it in the deployment, not the
migration.**

**2. The policy side is `RESTRICT` and the receipt side is `CASCADE`.**

🔴 **`agent_tool_receipts.agent_run_id` references `tutor_agent_runs(id)` `ON DELETE CASCADE`, so
deleting the parent run deletes its receipts.** 🟢 **The rule a grade was given under survives any
delete attempt; the evidence that an agent applied it does not.** 🔵 **If the record must survive,
the receipt's parent FK cannot be `CASCADE` — a requirement the source does not carry and a
proposal should.**

## Run it

```
python3 test_receipts.py      # 18 checks, 0 failed
```

🟢 **No network. No registry install. No dependency beyond the standard library** — which is why
it runs here at all *(`T303`, `gap 140`)*.

## 🔴 What this is NOT

🔴 **Not a deployment.** It is a reference schema plus the guards that make it an audit record
rather than a table. 🔴 **Not a compliance claim** — EU Annex III documentation and North American
human-oversight expectations want this SHAPE of record, and meeting them is a programme, not a
file. 🔵 **And not a substitute for reading `civil-ai`**, which carries far more than these two
tables.
