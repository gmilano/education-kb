# `p515-class-claim` — the probe for a claim no licence gate can see

## Why it exists

`p514` published, as the stated justification for its flagship recipe `P518`:

> *"Every LMS on these shelves is copyleft — Moodle **GPL-3.0**, Chamilo **GPL-3.0**, Open edX
> **AGPL-3.0**."*

It was false when written. Two Apache-2.0 **full LMS** rows were live on the shelves:
`OpenOLAT/OpenOLAT` (shelved since `p508`, sold as *"pick this when the client needs a closed
derivative"*) and `pacewisdomhq/TutorLoom` (added at `p513`, **the pass immediately before**).

🔴 **No existing gate could have caught it.** `gate-shelf-consistency` (`p308`) compares licence
**cells for one slug** across shelves — it is blind to a sentence that quantifies over a *class*.
A universal claim is a different object from a disagreeing cell, and it had no instrument.

## What it does

1. Collects universal licence claims from the eight live shelves — `every|all|each|no` + a class
   noun (`LMS`, `platform`, `repo`, `row`, …) + a grant word (`copyleft`, `GPL`, `MIT`, …).
2. Collects the **permissive rows that such a claim quantifies over**: a table row carrying a
   `owner/repo` GitHub address, a bolded `MIT` / `Apache-2.0` / `BSD` grant, and an LMS-ish term.
3. Prints the claims next to their counterexamples, so a universal claim can never be read without
   the rows that would refute it in view.

Exit **1** when an unqualified universal copyleft claim is live while permissive rows exist.

## What it found on its first run

| run | result |
|---|---|
| permissive LMS/platform rows on the shelves | **57** |
| universal licence claims | **30** |
| unqualified `every/all … copyleft` over an LMS class | **4 flagged**, of which **1 is a live uncorrected claim**: `verticals/solutions.md` L112 |
| 🟢 the finding a manual read missed | `p514` published the claim **TWICE** — `compose/patterns.md` *and* `verticals/solutions.md` L112, the latter in the very file that sells `OpenOlat` as Apache-2.0, and there it also miscasts the permissive rows as *"small — `gegok12` (SIS) and a handful of components"* |

## Stated limits — an unstated limit is how `p514` happened

- 🔴 **Phrase-based.** A claim worded a new way is missed. This is a floor on recall, not a ceiling.
- 🔴 **It does not decide truth.** It places a claim beside the rows it generalises over and leaves
  the verdict to a reader. A correctly-scoped claim can still be flagged.
- 🟡 **Precision is 1 genuine in 4 flagged** on this run. Two flags are quotations of the claim
  inside corrections of it; one is a search-results data row. The exclusion filter excuses lines
  that quote, correct, or scope a claim (`this window`, `they front`, `first-hand`), which cut the
  flags from 15 to 4 — but it cannot excuse everything, and it should not.
- 🔴 **It reads the shelves as text and fetches nothing.** Grant cells are trusted as written; this
  probe tests *agreement*, not *licences*. Byte verification is a separate channel.

## Run

```
python3 -I compose/code/p515-class-claim/class_claim.py .
```

Reads only; writes nothing; no network.
