---
industry: education
region: Global
updated: 2026-10-10
---

# `p1026-archive-regression-census` — what the reset dropped, and the two defensible answers

**Pass 103, 2026-10-10.** Opens and measures **`Gap 394`**.

A reset that is followed by growth hides its own losses. This repository's live corpus is
**more than twice** the size of its `archive/2026-10-06-pre-reset/` snapshot, and it is still
missing a **sixth** of the snapshot's addresses. No count of the live pages can show that,
because the live pages got bigger.

## What it measures

Every `https://github.com/owner/repo` address in `archive/<snapshot>/` that appears in **no**
live file, case-folded and with trailing punctuation stripped. One direction only: an address
that is live-only is never reported, because the census asks what was *lost*, not what is new.

Each lost address is classed:

| class | meaning |
|---|---|
| `LOST` | in the archive, in no live file, and not a declared control |
| `CONTROL` | a deliberate ABSENT probe (`elgg/nosuchrepohere12345`) or a non-repo URL (`/topics/…`, a `.git` suffix) — these were never supply |

## The two numbers, and why they differ

🔴 **The definition of "live corpus" moves the answer by 21 addresses, so both numbers ship.**

| corpus definition | live addresses | `LOST` |
|---|---|---|
| **every non-archive text file** in the repo (this instrument's default: `.md` `.sh` `.py` `.tsv` `.txt`) | **1 419** | **82** |
| **pages and instrument READMEs only** — what a reader of this KB can actually find | 1 314 | **103** |

🔵 **The 21-address difference is not spread around. It is held in exactly ONE file:**
`compose/code/p725-readme-payload-sweep/shelf-repos.2026-10-08.txt` — an instrument's *input
worklist*. Measured, not assumed: `held-only-in-a-worklist.2026-10-10.txt` lists all 21, and a
`grep` for each returns that path and nothing else outside the archive.

🔴 **A worklist is not a shelf.** An address in a sweep's input file is held by the repository and
offered by no page. Among the 21: `mitodl/open-learning-ai-tutor` (MIT, 15 tags),
`project-sunbird/sunbird-devops` (MIT, 702 tags),
`european-commission-empl/european-digital-credentials`, both `fwu-de` ontologies,
`aiverify-foundation/llm-evals-catalogue` — and `ollama/ollama`, the local-inference runtime,
on no page of this KB.

🟢 **So `82` is "held nowhere outside the archive" and `103` is "absent from every page."**
Quote the one that matches the question.

## Self-reference, which is the trap this instrument had to be built around

🔴 **Committing the result into the corpus the result measures makes the next run return zero.**
`result.*.tsv` lists the lost addresses; leave it in the live corpus and every one of them is
"live" tomorrow. The guard excludes the instrument's outputs **by filename, not by directory**, so
a result copied elsewhere in the tree still cannot suppress the finding. Tests 6 and 7 are exactly
that case, and test 7 plants the file **outside** the instrument directory.

## Oracles

- `comm -23` over two sorted, case-folded address sets — no classifier was written (`P237`).
- The excluded controls are a committed list, not a regex: a control is a **declaration**, and
  a missing exclude file degrades to reporting it as `LOST` rather than silently dropping it
  (test 9).

## Run

```
bash census.sh [repo-root] [archive-dir]     # TSV on stdout, counts on stderr
bash test_census.sh                          # 9 tests, offline, fixture tree
```

## Execution record

🟢 **Executed pass 103, both limbs.** `test_census.sh`: **9 passed, 0 failed**.
`census.sh . ./archive`: `archive_addresses=681 live_addresses=1419 lost_total=88`
(**82 `LOST` + 6 `CONTROL`**), stable across a re-run **after** its own results were committed.

🔵 **And that execution is itself a measurement of `Gap 383`.** This pass, a **pre-existing**
instrument of this repository (`p383-region-heading-gate/check_headings.py`) was **refused**
(`[Code from External]`) while this instrument, **authored in the same pass**, ran. 🔴 **Pass 102
recorded the instrument state as "alternating between passes"; this pass shows the split is not
temporal.** See `P1028`.

## What this instrument does not do

🔴 **It does not check whether a lost address still resolves.** `concentricsky/badgr-server` is on
the `LOST` list and is also **ABSENT on GitHub** — two different facts. Recovery requires probing
each address (`P1005`), and pass 103 probed **14 of 82**. `Gap 394` carries the remaining 68.
