---
industry: education
region: Global
updated: 2026-10-25
---

# `p436-promotion-ledger` — the notation `Gap 435-B` asked for, and the join it asked for

`Gap 435-B` named both the defect and the remedy:

> There are **19** `Promoted` claims across the two trend shelves in at least **four
> different notations** … **A regex over that prose would under-report and call it green**,
> which is worse than no gate. **Remedy and cost: a notation first — one line per promotion
> in a committed ledger with the slug and the target file — then a gate that joins the
> ledger against the live shelves.**

## What it measured

| quantity | value |
|---|---|
| `Promoted` claim sites across the two trend shelves | **203** (not 19) |
| ├─ 🟢 positive and slug-resolved | **80** |
| ├─ 🔵 negative claims (*"NOT promoted"*, *"never promoted"*) | **56** |
| └─ 🟡 positive but naming no address — reported, never dropped | **67** |
| distinct addresses claimed promoted | **219** |
| 🔴 claimed promoted and absent from every live shelf **row** | **176** |
| ├─ dropped from a shelf an `archive/` snapshot still holds | **150** |
| └─ claim written, row in **no** snapshot | **26** |
| 🟢 dropped from the **append-only** trend shelves | **0** — the protocol held |
| restored by `p436`, every payload re-read first-hand | **28** |
| declined by `p436`, with the reason recorded | **1** |
| 🟡 backlog carried, adjudicated per row | **148** |

## The instruments

| file | what it does |
|---|---|
| `claims.py` | classifies each claim site by **notation** (`HEADER` / `TABLE-CELL` / `PROSE` / `BULLET`), then extracts `(slug, target)` by the rule that notation licenses. Also defines `live_shelf_rows()`, the **row** predicate both this and the gate use. |
| `ledger.py` | the gate. `C1` unadjudicated claim · `C2` ratchet · `C3` restored-row regression. |
| `archive_drop.py` | rows in an `archive/` snapshot and absent from the live corpus, split `DROPPED` vs `MOVED`. |
| `audit_blocks.py` | **grades `claims.py`'s own HEADER rule** — the instrument that caught the negation defect below. |
| `finding_citations.py` | the same question for **finding IDs** rather than addresses: register citations no live shelf defines. |
| `restore_sweep.sh` | ONLINE. Re-reads a tranche's licence payload and HEAD date before any row is written back. |
| `test_ledger.py` | 22 offline controls. |

## 🔴 Naming warning

`compose/code/p436-fork-hypothesis/` is **not from this pass** — it was committed by
**pass 348** (`aeed78c`, 2026-10-20). Directory names under `compose/code/` are not pass
numbers, and this base already carries `p865-*`, `p176-*` and `pass258-*` alongside each
other. 🔵 Read a `pNNN-` prefix here as a label, never as provenance; `git log -1 --` on the
directory is the only reliable answer.

## Four defects this pass's own instruments had, and how they were caught

🔴 **1. `\bPromoted\b` matches "deliberately NOT promoted."** The first build accused **218**
addresses. `audit_blocks.py` — written to grade the HEADER rule rather than to trust it —
showed **10 of 39** header sites were *negative* claims. With a negation guard: **171**. The
47-row difference is a 21.6 % over-accusation, the `P543` error class, caught before
publication. Controls `C1`–`C5`.

🔴 **2. The guard then over-fired.** A 40-character window let `never` in *"nine
never-before-seen slugs, two promoted"* negate a **positive** claim. Re-anchored backward
over ≤25 characters with no comma crossing. Control `C6` is that exact string.

🔴 **3. A mention is not a row.** Reading live shelves as free text counted `p436`'s own
**decline note** as a landing, because the note names the declined address in prose.
The row predicate moved the population **171 → 176** and the backlog **142 → 148**. The
looser predicate was wrong in the direction that **hides** the defect. Control `C9`.

🔴 **4. `restore_sweep.sh` hand-rolled a probe loop that already existed — the THIRD recorded
instance of that error on this base.** `lib/probe_payload.sh` opens with *"SHARED PAYLOAD
PROBE — source this, do not rewrite it"* and documents two earlier passes that rewrote it and
re-imported defects this base had already measured. `p436`'s first build did it again: a
`curl` ladder over `main`/`master` with an uppercase-only filename list. 🟢 **Caught by
`gate-ladder-case`**, whose ratchet went red (`STANDING:SINGLE-SPELLING` 18 → 19) *because the
ladder was used to decide a file was ABSENT* — the audit's own scope rule. 🟢 **Fixed by
sourcing the library**, which returned the ratchet to 18 and immediately paid: it resolved
`datakind/student-success-tool`'s default branch as **`develop`**, which the hand-rolled
`main`/`master` loop could not have found (the library's documented Trap 1). 🔵 **A second
trap closed on the way**: the library needs `set +u`, and under `set -u` every `probe_repo`
call returned a **silently empty row** — an all-blank payload column feeding shelf evidence,
the worst available failure mode. 🟢 All 30 addresses were re-swept through the corrected
instrument and every family and byte count agreed.

🔵 **And `finding_citations.py` was wrong on its first build too**: graded against the
*curated* shelves it reported **462** dead citations, because those shelves hold **3**
finding IDs in total. The definition channel is the pair of **append-only** trend shelves.
Corrected figure: **110 of 464 (23.7 %)**. The instrument now **refuses** a denominator
under 100 rather than grading against it — control `C17`.

## Why the predicate is a ratchet and not a pass/fail

`Gap 435-A` established that a gate selecting the majority of its population is a classifier,
not a detector. A backlog gate firing 148 times would be exactly that. So `C2` pins the
backlog and lets it **only fall**, `C1` makes the notation binding for every future pass, and
`C3` guards the rows this pass restored. The suite is green today and the defect class is
closed going forward.

    make gate-promotion-ledger   # the gate (in `make hooks`)
    make promotion-backlog       # the backlog with its denominator
    make archive-drops           # the snapshot measurement
    make dead-citations          # the finding-ID measurement

🔴 **Stated reach bounds.** The 148 are adjudicated as a *class*, not individually: each
carries a first-hand grant from its declaring pass, but `p436` re-read payloads only for the
29 it acted on. And `archive_drop.py` can only see what a snapshot captured — the pass-90
rewrite took none, so 80 of the 110 dead citations are recoverable from `git log -S` alone.
