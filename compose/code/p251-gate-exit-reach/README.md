---
industry: education
region: Global
updated: 2026-10-16
---

# `P251-A` — `ACTION XM`: can the standing gate actually fail?

Artefacts and suite of the **two-hundred-and-fifty-first pass (2026-10-16)**.
🟢 **`27`/`27` green under `python3 test_gate_exit_reach.py`.**

## Why the pass needed the instrument

`p250` found [`lazy_lint.py`](../p230-prose-path-ladder/lazy_lint.py) reporting
two real findings on **every** run of `make hooks` and returning `0`
unconditionally, so the gate printed `ALL OFFLINE LICENCE CONTROLS PASS`
directly underneath its own failure. `ACTION XM` asked the general question:
**of the gate's controls, how many can actually fail?**

A control is failure-capable only if **two** layers agree:

| layer | what can break it | measured here |
|---|---|---|
| **1 — the recipe line** | `\|\| true`, `\|\| :`, a trailing `; exit 0`, a leading `-`, or a pipeline whose last stage is a reader (`\| tail`) — this gate does **not** set `pipefail` | 🟢 **`24` of `24` commands are failure-capable.** `set -e` plus `&&` is the whole reason |
| **2 — the suite** | a suite that prints `FAIL` and exits `0` | 🟡 **`19` of `24` exit explicitly; `5` run through `unittest.main()`** |

## 🔴 The finding: `unittest.main()` has a silent-zero mode, and the gate hides it

Measured in this suite, as subprocesses, not read off the documentation:

| suite shape | exit code |
|---|---|
| `unittest.main()` with **zero** collected tests | 🔴 **`0`** |
| `unittest.main()` with every test **skipped** | 🔴 **`0`** |
| `unittest.main()` with one real failure | 🟢 `1` |

So a rename off the `test_` prefix, a dropped class or a mass `@skip` leaves a
gate control **passing while asserting nothing** — `lazy_lint`'s defect reached
by a different road.

> 🔴 **And the correlation is exact: the `5` suites with a silent-zero mode are
> the `5` recipe lines — the only `5` — whose `stderr` the gate discards with
> `2>&1`.** `unittest` writes `Ran 0 tests` to `stderr`. The gate suppresses
> the one channel on which the mode would be visible, on exactly the controls
> where it matters.

## The fix: a floor per unittest suite

`FLOORS` pins the collected-test count of each of the five, measured by running
every suite individually at `p251`:

| suite | floor |
|---|---|
| `p222-ecosystem-bound-grammar/test_bound_grammar.py` | `32` |
| `p228-shelf-gate/test_shelf_gate.py` | `36` |
| `p1054-mit-plus-clause/test_mit_plus.py` | `14` |
| `p242-grant-delta/test_grant_delta.py` | `23` |
| `p1058-empty-payload-gate/test_empty_payload_gate.py` | `29` |

🔵 The static count (`def test_*`) and the count `unittest` reported at
run time agree on all five — `14`, `23`, `29`, `32`, `36` — which is what makes
a static floor a usable control.

## Runner

```
python3 audit.py <repo-root>      # one TSV row per gate command
```

🔴 **A caveat this instrument states rather than hides:** the audit reads the
`Makefile` and the suites' source. It does **not** execute `make hooks`, and
`p251` could not: this session's sandbox refuses to run the repository's own
`make` recipe. Every suite was therefore invoked **individually** and its exit
code recorded ([`p251-gate-measured`](../../../evidence/p251-gate-measured.2026-10-16-p251.tsv)).
