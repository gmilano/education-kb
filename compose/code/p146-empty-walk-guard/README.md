---
industry: education
region: Global
updated: 2026-10-12
---

# p146-empty-walk-guard — a verdict over zero files is not a verdict

The four-line structural answer to `T42`. `p146-exclusion-reach` shows **0 of 35**
traversing instruments on this shelf can tell "I read no files" from "I read files and
found nothing" — and `P145-A` published seven rows where the first was presented as the
second.

    status, detail = walked_or_refuse(files, root, excluded=SKIP_DIRS)
    verdict, detail = guard_verdict(verdict, files, root, SKIP_DIRS)   # drop-in form

    python3 test_walk_guard.py        # 12 tests, offline, no external payload

## The distinction it preserves

| state | meaning | correct output |
|---|---|---|
| 🔴 **zero files walked** | the instrument saw no input | **no verdict is available** |
| 🟢 **files walked, none matched** | input seen, no surface found | `NOT_AN_MCP_SERVER` — a finding |

## What the tests pin

🆕 🔴 **`P146-B`** — `p141-agent-surface-gate/surface_gate.py` carries `P145-A`'s defect, in
an **inline literal set inside `walk()`**. On a fixture whose only code is under `dist/`:
`walk()` yields `[]` and `is_mcp_server` returns `(False, 0)`.

🟢 **`P146-C`** — the negative control. The **identical bytes at the repository root** read
as a server (`sdk=True`, hits>0). 🔵 **So the verdict was a function of the path, not the
payload.**

🔴 `P145-A` reproduced on `surface_gate2.py`, as a regression pin.

🟢 **`P146-G`** — p145's repair verified: `surface_gate3.payload_trees` re-admits a `dist/`
the `package.json` declares, on the same fixture that defeats the other two.

🟢 All fixtures are authored by the test. 🔴 **No external repository is fetched, cloned or
executed** — which is also why this probe could run in a pass where the clone channel was
refused.

## 🔴 What it deliberately does not do

It does not fix any exclusion list. Whether `dist/` *should* be read is artefact-relative,
and `P144-O`/`T39` settled how to decide: ask the artefact, not the name. 🔵 **This module
answers the prior question — did I read anything at all? — which has one right answer in
every artefact kind.**
