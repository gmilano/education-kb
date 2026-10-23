# `p395-grant-ladder-fallthrough` — 394-A and 394-B, discharged as control flow

`p394` pre-registered two defects in `licence-grant-gate` and called both cheap and bounded. They
were. Both are discharged here against real addresses, and the result is **8 rows that the shipped
gate reports as absences and that do in fact carry a grant**.

## What was wrong

**`394-A` — the ladder is first-hit-wins.** `probe_repo` returns on the *first* path that answers 200
with a non-empty body. R's convention for templated licences puts a **year/holder stub** at `LICENSE`
and the licence **text** at `LICENSE.md`. So on `rstudio/gradethis` the gate grades a **49-byte**
stub and returns `NON-GRANT — payload present but no known licence family in title region`, and never
reads the clean MIT one position later. The path is present, and it is *first* — which is why
`393-F`'s remedy (enumerate the whole tree) cannot catch this: widening the path space does not help
when the problem is that the ladder stops too early.

**`394-B` — the R grant lives in `DESCRIPTION`.** Five rows `p394` published have no licence-shaped
file at any tree path; their grant is the `License:` field in `DESCRIPTION`, which CRAN itself
enforces. `licence-grant-gate` has `DESCRIPTION` in neither `LICENCE_PATHS` nor `EXISTENCE_PATHS`, so
each falls through to `EXISTS-NOLICENCE — all rights reserved until shown otherwise`.

## The fix

Two changes, both to **control flow and arm order**, neither to a vocabulary:

1. When a licence payload yields **no family**, remember it and **keep reading** instead of returning.
   Fall back to it only if no later arm does better. A payload that yields a family, or that is an
   explicit refusal, still returns immediately — so the change **can only turn absences into grants**,
   never the reverse.
2. Add a **manifest arm** after the licence ladder that reads `DESCRIPTION` verbatim, returning the
   `MANIFEST-ONLY` class `p383` already defined, and a **README arm** after that, returning the
   `README-ONLY` class `p394` defined in `394-F`.

## What it measured, 2026-10-23

`p395_probe.py` is written fresh for this and run first-hand; `run-*.tsv` are its unedited output.

| Control | Result |
|---|---|
| `rstudio/gradethis` | 🟢 `LICENSED MIT` at `main/LICENSE.md` (1,078 B) — was a 49 B stub verdict |
| `ucbds-infra/ottr` | 🟢 `LICENSED BSD` at `master/LICENSE.md` (1,555 B) — was a stub verdict |
| `cran/exams`, `philchalmers/mirt`, `patriciamar/ShinyItemAnalysis`, `cran/catR`, `cran/TAM`, `cran/learnr` | 🟢 `MANIFEST-ONLY` with the `License:` field read verbatim — all six were `EXISTS-NOLICENCE` |
| `pykt-team/pykt-toolkit` | 🟢 **positive control holds**: grant at position 0 still returns at position 0 |
| `gmilano/definitely-not-a-real-repo-p395` | 🟢 **negative control holds**: still `ABSENT` |

🔴 **One correction to `394-A` itself.** It records the `ottr` stub and BSD text without a branch.
Both paths **404 on `main`**; the ref is **`master`**. The defect is real and reproduces — but on the
second branch, not the first, which is also why its 108 B figure differs from the 1,555 B text read
here.

## 🔴 Why the shipped gate is NOT patched in this pass

`grant_gate.py` is **unchanged**, and [`PROPOSED-lib-patch.md`](./PROPOSED-lib-patch.md) carries the
diff instead. The reason is a limit of this pass's environment, not a judgement about the fix:
**running the repository's own Python could not be done here**, so `test_grant_gate.py` and its
existing controls for `P453`–`P459` **were never executed**. Editing an instrument while unable to
run the suite that guards it would be exactly the move this base's gates exist to prevent. A
successor with the suite runnable should apply the diff and confirm the prior controls still pass;
the evidence that the fix is correct on real addresses is already in `run-*.tsv`.
