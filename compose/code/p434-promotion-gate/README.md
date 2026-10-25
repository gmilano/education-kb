# `p434-promotion-gate` — `Gap 433-A`, and the refutation of its own remedy

**Pass 434, 2026-10-25.** Closes `Gap 433-A` with a tested, wired, blocking gate — and
refutes the predicate the gap prescribed, with the refutation kept runnable as controls
`C8`–`C11` rather than asserted in prose.

## What `Gap 433-A` got right

🟢 **The diagnosis is confirmed and now quantified.** `p433` declared the trending shelves
write-only: append-only by contract, with no promotion path, so traction accumulates unread.
The census measures the shape of that:

| cifra | valor |
|---|---|
| addresses on the curated shelves | **276** |
| addresses on the trending shelves | **2 708** |
| **unpromoted** (trending, in no curated shelf) | **2 457** |
| graded first-hand this pass | 7 |
| ungraded — a **REACH bound, not a defect count** | 2 450 |

## What `Gap 433-A` got wrong, measured

The prescribed remedy was *"reads its current star count, and fails when an address above a
threshold (say 150 ★) carries a permissive grade and appears in no curated shelf."*

🔴 **Reason 1 — the star channel does not exist from inside a run.** `api.github.com`,
`github.com` HTML and `codeload.github.com` were each re-measured at **HTTP 403** through
this environment's proxy on 2026-10-25. What answers is `raw.githubusercontent.com` (200)
and the git smart-HTTP transport. `p228-shelf-gate/fetch_grants.sh` has carried that same
finding in a comment for over two hundred passes. **So the gap keyed its gate on the one
quantity no reachable channel serves**, and no `make` target can obtain it. The star figures
in `grades.2026-10-25.tsv` came from the agent session's GitHub tool and are labelled
`stars_channel=mcp-github-search` for exactly that reason: 🔵 **they are not reproducible
from `make`, and the gate therefore does not depend on them.**

🔴 **Reason 2 — the threshold filters out precisely the rows a build-on shelf wants.** All
seven unpromoted high-traction addresses were graded on payloads read first-hand:

| address | ★ | family | bytes · sha256(12) | permissive? |
|---|---|---|---|---|
| `brycewang-stanford/Auto-Empirical-Research-Skills` | 4 771 | CC-BY-SA-4.0 | 620 · `22401c14e67f` | 🔴 no |
| `sitor-ai/frametell` | 400 | AGPL-3.0 | 34 523 · `0d96a4ff68ad` | 🔴 no |
| `minicoohei/ai-agent-camp` | 346 | **NO-GRANT** | 404 on every path | 🔴 no |
| `helixnow/deep-student` | 290 | AGPL-3.0 | 34 532 · `894342980454` | 🔴 no |
| `ystemsrx/sql-to-ER` | 192 | AGPL-3.0 | 34 523 · `8486a10c4393` | 🔴 no |
| `wenflow-org/wenflow` | 59 | **MIT** | 1 067 · `b6fac57d4710` | 🟢 yes |
| `zhangl1001/civil-ai` | 41 | **MIT** | 1 067 · `5731a2d3ccea` | 🟢 yes |

🔴 **Every address above the prescribed 150 ★ threshold is non-permissive, and both
permissive ones are below it.** The prescribed predicate fires **0** times; the star-free
predicate fires **2**. In this domain's new supply traction and permissiveness are
*anti-correlated*, so a star threshold is a filter against the findings.

🔵 **The honest reading of `p433`'s own promotion decision:** it promoted three permissive
rows and left five larger ones behind, and that was **substantively correct** — there was
nothing permissive above the threshold to promote. What was wrong was the *denominator*.
`p433` reported its sweep as *"26 of 30 already named on a shelf; 4 absent, all ≤ 8 ★"*;
re-running `p433`'s own query returns `Auto-Empirical-Research-Skills` at **4 771 ★** as the
top hit. Both statements are true at once, because "named on a shelf" counted the **trending**
shelves — the very shelves the same pass declared write-only. 🔴 **Saturation was measured
against a denominator that includes the backlog, so the backlog could not show up in it.**

## The gate

🟢 **Corrected predicate: PERMISSIVE and absent from every curated shelf.** No star count,
therefore fully offline, therefore admissible in `make hooks` — which the prescribed version
could never have been.

```
make gate-promotion                                  # controls + live arm (blocking)
promotion_gate.py census   <repo-root>               # the population, offline
promotion_gate.py findings <repo-root>               # the blocking arm alone
promotion_gate.py findings <repo-root> --predicate p433   # the refuted form, still runnable
```

**28 / 28 offline controls.** `C6` is the load-bearing negative (the 4 771 ★ CC-BY-SA-4.0
specimen — the error direction that would put unusable supply into a client deliverable).
`C8`–`C11` are the refutation. `C11a` constructs the starless population and shows the
prescribed predicate judging **nothing**. `C12`–`C13` assert an ungraded address is a reach
bound and never a finding. `C19`–`C21` are the `P541` / `Gap 243` empty-input refusals.

## Reuse, not reimplementation

Per `T108` — *run this base's instruments, do not re-improvise them*:

- the address population and its rejection classes are `p351-address-shape`'s `harvest` /
  `partition`, so a nav namespace or a truncation residue never becomes a finding;
- `PERMISSIVE` is **imported** from `p444-root-vs-tree-family`, never restated, so a family
  cannot drift between the two (control `C16`, and `C17a` pins `CC-BY`'s deliberate absence);
- the grades were produced by `p228-shelf-gate`'s own `fetch_grants.sh` ladder and
  `classify_grant.py`, not by a new classifier;
- addresses are compared case-folded, because `p439-case-collision-gate` measured that this
  corpus cites repositories under more than one spelling (control `C14`).

## What this does not claim

🟡 `UNPROMOTED-PERMISSIVE` says a permissive address this base already recorded is absent
from every build-on shelf. **It is not an instruction to shelve it** — that is
`p400-candidate-membership`'s question. 🟡 The 2 450 ungraded addresses are a reach bound;
grading them is an online sweep and a later pass's work, registered as `Gap 434-A`.
