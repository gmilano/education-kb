# `p252-ungated-floors` — `ACTION XR`

**What it answers.** `p251` floored the five `unittest.main()` suites *inside* `make
hooks` and registered `ACTION XR` for everything outside it, sized as *"`344`
instruments on disk, `23` referenced by the `Makefile`, so `321` are ungated and
unfloored"*, with an explicit falsifier: *"falsified if a pass reports the count without
naming which of the `321` carry a `unittest.main()` suite"*.

**The size was wrong, and the correction is the point.** A directory is not a suite. The
artefact that can pass while asserting nothing is a **test file**:

| measure | `p251` | `p252` |
|---|---|---|
| instrument directories | `344` | `347` |
| referenced by the `Makefile` | `23` | `27` |
| python test files | — | **`201`** |
| gated | — | `20` |
| ungated | `321` *(directories)* | **`181`** *(suites)* |
| ungated **and** `unittest.main()` | — | 🔴 **`71`** |
| ungated **and** explicit-exit | — | 🟢 `110` — immune by construction |
| of the `71`, collecting **zero** tests | — | 🟢 **`0`** |

🟢 **So the exposure is `71`, not `321`, and it is LATENT rather than active:** nothing on
these shelves currently rests on a suite that asserts nothing. What the `71` are exposed
to is a *future* edit — a method rename, a dropped class, a mass `@skip` — landing with
no signal, which is how `p250`'s `lazy_lint.py` and `p251`'s five controls got there.

## Why the pins live in a TSV

`p251` pinned five floors as literals in `gate_reach.py`, which is right for five.
Hand-writing `71` would itself become the drift surface: a floor nobody can regenerate is
a floor that gets edited to match a broken suite. So `--pin` writes [`floors.tsv`](floors.tsv)
and `--verify` checks it, and `--verify` is what the gate runs.

## The classifier is imported, never re-implemented

`suite_signal`, `silent_zero` and `collected_tests` come from
[`p251-gate-exit-reach`](../p251-gate-exit-reach/) by import, and two controls assert
function **identity** — so `suite_signal`'s measured python/shell asymmetry cannot
diverge between the two instruments. The only thing this module adds is the enumeration.

## Usage

```
python3 -I ungated_floors.py --census    # the population, as a TSV
python3 -I ungated_floors.py --table     # every member with its floor and verdict
python3 -I ungated_floors.py --pin       # (re)write floors.tsv
python3 -I ungated_floors.py             # --verify: exit 1 if any floor is breached
python3 -I test_ungated_floors.py        # 31 controls
```

## Proven able to fail, not assumed to

🟢 Both falsifiers were RUN, which is `ACTION XS`'s lesson from `p251`:

| falsifier | result |
|---|---|
| raise one pinned floor beyond reach | `exit=1`, `BELOW-FLOOR git-recency-channel/test_git_recency.py` — **and it names the suite** |
| delete `floors.tsv` entirely | `exit=1`, `71 UNPINNED` — 🔴 **a missing pin file must not read as clean**, and it does not |

🔴 **One measurement error worth keeping:** the second falsifier first reported `exit=0`,
because it was run as `python3 … | head -3; echo $?` — the status was `head`'s. That is
exactly the *pipeline-to-reader with no `pipefail`* pattern `p251`'s `audit.py`
enumerates as a layer-1 swallower, reproduced by accident while testing for it. Re-run
without the pipe, the instrument exits `1` correctly.

🔵 The suite signals failure with an **explicit non-zero exit, not `unittest.main()`** —
a silent-zero runner guarding the silent-zero census would be `lazy_lint.py` again.
