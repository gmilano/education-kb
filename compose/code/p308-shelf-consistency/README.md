# `p308-shelf-consistency` — the gate that reads this base against itself

`ACTION p307-R` item 1, built as ordered:

> 🔴 **Build the SHELF-CONSISTENCY gate** — for every slug carried on two or more shelves,
> compare the licence cells and fail on disagreement. 🟢 **The data is already tabular and the
> slug is the key.** 🔵 **This pass's headline defect lived in five places against three correct
> ones for two passes, and fifteen gates could not see it. It is the cheapest high-value
> instrument left in the base.**

Every gate standing at `p307` grades this base against something OUTSIDE it — a payload, a
registry, an enumeration, a date. **None of them compared two of this base's own cells.**

## What it does

```
make gate-shelf-consistency   # 52 offline controls, then the live shelves.  In `make hooks`.
make shelf-census             # where the DATED shelves disagree with the live answer.
```

* **LIVE shelves** — the seven catalogue files. A contradiction here **FAILS**.
* **DATED shelves** — the root index and the two append-only `trending.md` files. Every
  section there is dated by charter, so a stale cell is a *record*, not an error. **Censused,
  never failed.** 🔵 It is also where `p307`'s right answer was sitting.

The shelf list is **imported** from `p235-carried-index`, not restated. A second copy would be
a second thing to keep in step, which is the disease this instrument exists to detect.

## The verdict rule

Each location asserts a **set** of licences. The claims agree if some licence is in **every**
set. `{MIT}` against `{MIT, Apache-2.0}` intersects at MIT and is compatible; `{MIT}` against
`{Apache-2.0}` is empty and is the contradiction this gate is for.

🔴 The first draft flagged a slug whenever two licence names appeared against it anywhere, and
that is wrong twice over: a cell may assert a genuine **dual** licence, and a row may carry one
licence for code and another for content (`ankitects/anki` — AGPL-3.0 code, CC-BY-SA-4.0 decks).
Fifteen of the first run's flags were that one bug.

## What the first run measured

| run | flagged | what changed |
|---|---|---|
| 1 | **65** | first draft |
| 2 | 21 | the intersection rule; clause-family notes (`clause=MIT/ISC`) stopped being two claims |
| 3 | 8 | `"unlicensed"` stopped matching the Unlicense; prose got subject discipline; scoped absences and multi-grant rows suppressed |
| 4 | 5 | comparators (`more permissive than MIT`); declared manifest/payload splits |
| 5 | **1** | arrow-correction rows read over the whole row; paired rows; possessives; quoted third-party claims; prose takes the first licence only |

**1 real defect in 1 132 live claims over 344 slugs.** `intel/market.md:1834` carried
`DaRL-GenAI/instructional_agents` as `Apache-2.0`; the payload is **MIT** (`LICENSE`, 1 067 B,
`ae280df5a726`), and `intel/trends.md:2815` **already said so in writing** — *"`instructional_agents`
is MIT, not Apache-2.0"* — thirteen other cells agreed with the payload, and this one cell
survived the correction. Fixed at `p308`.

🔵 **Every one of the other 64 flags was the INSTRUMENT's**, in nine distinct false-positive
classes. Each class is now a named control, because a suppression nobody can see is a
suppression the next pass will re-discover:

| class | the row that taught it |
|---|---|
| dual / split-in-one-cell | `chamilo/chamilo-lms` GPL-2.0 · GPL-3.0 |
| code-and-content licences | `ankitects/anki` AGPL-3.0 code, CC-BY-SA-4.0 decks |
| clause-family note | `clause=MIT/ISC` read as two conflicting claims |
| `"unlicensed"` ≠ the Unlicense | `*(none — "unlicensed")*` beside a correct MIT, ×3 |
| sibling in prose | `moodle/moodle` collecting a recipe neighbour's Apache-2.0 |
| scoped absence | `meyerjp3/psychometrics` — *manifest-granted, not payload-pinned* |
| multi-grant row | `LearnPress/learnpress` — three manifests, declared on purpose |
| comparator | `gen-mentor` is CC0-1.0, *"more permissive than MIT"* |
| possessive / quoted | `` `MIT`'s `` verb list negated; `lms` published *as "MIT"* by a third party |
| arrow correction, no header | `| slug | 🔴 LGPL-3.0 | 🔴 …Version 2 → GPL-2.0 |` |
| paired row | `i-educar · i-diario` under one row, `GPL-2.0 · AGPL-3.0` |

## What this does NOT do

🔴 **It compares licence LABELS only.** `p308`'s second finding — that this vertical's standing
*"forced architecture"* conclusion was refuted by a row on its own shelf (`Selleo/mentingo`,
**MIT**, an AI-native LMS, carried for ~140 passes) — is the same disease in **prose
conclusions**, and no instrument here sees it. Registered as `ACTION p308-R` item 1 rather than
implied to be covered.

🔴 **It does not decide truth.** It finds disagreement; a payload decides who was right. Every
adjudication in `evidence/p308-shelf-consistency.2026-10-19-p308.tsv` names the payload that
settled it.

## Prior art in this base, which is the uncomfortable part

`intel/open-gaps.md:3807` carries **`ACTION QG`**: *"every pass that corrects a cell must sweep
that repository's every current-state cell in the same pass"* — **DISCHARGED**, with `263`
grant-claim lines adjudicated over `25` repos, `23` stale cells found, and **`4` comparator
false positives** recorded.

🔵 So this base ran this audit **by hand**, around `p214`, found the same false-positive class
this instrument re-derived from scratch, and **never turned it into a standing control.** The
rule existed as prose for roughly ninety passes. 🟢 That the hand-run found `23` stale cells
and this run found `1` is the measurement worth keeping: the hygiene is real, and now it holds
without a volunteer.
