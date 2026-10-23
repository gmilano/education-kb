# `p407-i2-sweep-crosscheck` — `Gap 406-A`

🟢 **The item `p406` named as the one to take next**, in its own words: *"The honest question is
whether `I2`'s live-shelf test and this sweep AGREE on all 59 — they were not cross-checked, and a
disagreement would be a finding on one of them."*

## What it answers

They agree on **45 of 59** and disagree on **14**, in **three** mechanisms — and the gap's framing
("a finding on one of them") turns out to be the wrong shape. 🔴 **`I2` is correct on every address
it can see. The defect is its SCOPE, and the sweep's NUMERATOR.**

| mechanism | n | whose defect |
|---|---|---|
| `AGREE-OFF-LIVE-SHELVES` | 41 | — both silent, correctly |
| `DISAGREE-I2-POPULATION-FROZEN` | 9 | 🔴 `I2` — its population is `p372`'s re-probe with `TOTAL = 46` **hardcoded**, so it can never see an address found later |
| `NOT-DECAY-P372-REFUTES` | 5 | 🔴 `p406` — the sweep counted this base's own **fabricated negative controls** as decay |
| `AGREE-NOT-A-LIVE-CLAIM` | 4 | — 🟢 `I2` right where it can see: in population, on a live shelf, detector correctly silent |

## The three findings

1. 🔴 **`I2`'s population is frozen.** 9 addresses the sweep flags on a live shelf are invisible to
   `I2` because they are not among `p372`'s 46. **6 of the 9 carry a live markdown link that `I2`'s
   own detector fires on** — `ale-alejandro/beadkit` (2), `thanh01pmt/interactive-quiz-kit` (2),
   `e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp`, `santillana-ai/tutor-sdk`,
   `yokowasis/autograder`. Nothing is wrong with the predicate; it is never asked.

2. 🔴 **The obvious repair introduces a SECOND defect, and this instrument pins it before anyone
   ships it.** `I2`'s detector is a **case-sensitive** substring (`f"github.com/{slug})" in line`),
   while `p406` publishes **folded** addresses. Feed the folded population to the shipped detector
   and it goes silent on the two addresses whose live-shelf link is written in mixed case:
   **`AI-Matrix-Engine/aidream`** (`agents/top.md:1144`) and **`Mckaroff/GraphLMS`** (`:1141`).
   Columns `i2_fires_folded` = 0 vs `i2_fires_caseless` = 1 are that defect, measured.
   🔵 `C10b`/`C10c` assert it on a fixture so the trap cannot be re-entered silently.

3. 🔴 **`p406`'s 2.20 % counts non-repositories as decay, and three instruments in this repository
   already said so.** 7 of the 59 were never repositories:
   - **5 fabricated negative controls** — `p372` classifies them `NOT-AN-ADDRESS/NEG-CONTROL` and
     states in writing that *"a negative control that fails to resolve is the control PASSING. It is
     never a defect."*
   - **`jushbjj/mr`** — a truncation of the **live** `JushBJJ/Mr.-Ranedeer-AI-Tutor`, and
     `compose/code/p251-prefix-collision/` is the instrument built for exactly this defect. Its only
     standalone occurrences on these shelves are as **that instrument's own specimen**.
   - **`en/get-started`** — the locale-path hole `ACTION ZZ-bt` registered and deliberately left
     open; `repos/trending.md:2611` already records it as `frappe/erpnext`'s docs path.

   | denominator | numerator | rate |
   |---|---|---|
   | `p406` as published | 59 / 2 681 | **2.2007 %** |
   | `p372`'s classifier applied | 54 / 2 676 | **2.0179 %** |
   | plus `p251` and `ZZ-bt`'s own specimens | 52 / 2 674 | **1.9447 %** |

   🔵 **The direction matters more than the size:** a decay rate that counts planted failures as
   decay overstates rot, and this base's instruments to exclude them were already written and
   committed. `p371`'s *"committed knowledge not wired in"*, third instance.

## A fourth finding, outside the gap's question

🔴 **`p406`'s shelf attribution is `if a in body` on the lowercased file — `p400`'s substring class.**
**65** swept addresses are a proper substring of another swept address, so the shorter one inherits
every shelf the longer one appears on. Two land inside the 59: `jushbjj/mr` (above) and
`uoc/java-lti-1.3-provider`, inside `uoc/java-lti-1.3-provider-example`. 🟡 The `shelves` column is
the evidence `Gap 406-A` rests on, so this bounds the whole question; `C18` detects containment.

🔴 **And `p372`'s taxonomy is incomplete.** `compose/patterns.md`, `intel/market.md` and
`intel/trends.md` are in **neither** `LIVE_SHELVES` nor `RECORD_FILES`, so no rule says a dead
address on them is a defect — and `compose/patterns.md` is the **recipe** shelf, where a dead
address is at its most actionable. `C13` asserts the three names so the hole cannot close by accident.

## Running it

```sh
make gate-i2-sweep-crosscheck     # 32 offline controls
python3 -I report.py <repo-root>  # the matrix + the evidence TSV
```

Evidence: [`i2-sweep-crosscheck.2026-10-23-p407.tsv`](../../../evidence/i2-sweep-crosscheck.2026-10-23-p407.tsv)
— 59 rows, one per `ABSENT-OR-PRIVATE` address, each with its mechanism and first hit.

🟢 **Provenance note — and a correction to this pass's own first draft.** This instrument was
drafted on the assumption that `P970` still held (*"the sandbox cannot execute repository code"*,
recorded at `p93`/`p94` and carried since). 🔴 **It does not hold in this session.** `make hooks`
was refused once at the start of the pass, but every individual gate runs, `make
gate-i2-sweep-crosscheck` runs, `make hooks` completes (**50 of 51 gates green**, the lone red being
`gate-census-union`'s control 24 — deliberately red for a fifth pass), and `dead_citation` imports
normally. 🟢 **So the draft's reimplementation of `p372`'s classifier was removed and replaced with
an import**, per `P237`: no instrument here keeps a second copy of a classifier. `C11` still
cross-checks the imported classifier against `p372`'s published partition, because an import proves
identity, not correctness.

🔴 **And the honest failure of this instrument's first draft.** With the classifier imported and
`C3`–`C6`/`C11` checking it in isolation, a mutation blanking `grade()`'s call to it
(`shape = "ADDRESS"`) reddened **nothing** — the classifier was present, tested, and not
load-bearing on a single published figure. 🔵 That is `p400`'s *"an emptiness guard does not fire"*
wearing a new costume, and it is the second time this base has built a check that could not fail.
🟢 Repaired as `C19`–`C21`, which pin the published partition **to the rows** (`T37`/`recount`
discipline): 37 controls, and that mutation now reddens two of them. Five further mutations
(detector, neg-control arm, decay denominator, shelf-set guard, unclassified-shelf derivation) each
produce a named failure.

🟢 **`p355`-portable:** the suite passes from its own directory and from the repository root.
