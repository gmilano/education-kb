---
industry: education
region: Global
updated: 2026-10-13
---

# `P175-A` — the dated-evidence gate, and the exit code that was missing

Artefacts and suite of the **one-hundred-and-seventy-fifth pass (2026-10-13)**.
🟢 **`13`/`13` green under `python3 -I`.**

## Why the pass needed the instrument

p174 observed, as a side finding it recorded rather than acted on, that running
`p120`'s and `p121`'s suites **overwrites their own dated result files** with
today's measurement. It restored three files to `HEAD` and registered
`ACTION KF`: *"settle whether instruments destroy their own evidence."*

The action asked two questions in one sentence — **how many instruments WRITE a
hardcoded dated file**, and **how many dated results DIFFER after a re-run** —
and set its falsifier at *"`≤1` instrument"*. 🔴 **The answers are `6` and `1`.**
At `6` the limb is silent; at `1` it fires. `T268` is that a falsifier naming a
threshold must also name the denominator it counts.

## What the gate measures, and where its rule stops

`dated_write.py` classifies a script as an **offender** when it WRITES to a path
whose basename carries a literal ISO date. The full rule, with its boundary, is
in the module docstring — it is stated in prose before it is coded, so it can be
argued with.

Three classifications, and the middle one is the honest one:

| shape | verdict | why |
|---|---|---|
| `> verdict.2026-10-11.tsv` | 🔴 **`hardcoded`** | every later run overwrites the file a published claim cites |
| `out = D / "x.2026-10-05.tsv"` in a script that also calls `date.today()` | 🟡 **`clock`** | the clock call may not reach that path; the gate resolves ambiguity in the script's favour |
| `> result.$(date +%F).tsv` | 🟢 **out of scope** | no literal date, so every run names a different file and nothing can be overwritten |

🔵 **Reading or naming a dated path is NOT a write.** An instrument that cites
yesterday's evidence is doing the right thing, and a gate that could not tell a
mention from a write would flag every honest instrument here.

## Controls — the suite must show it CATCHES, not merely that it passes

`T262` taught that a control which only ever runs in one configuration cannot
test configuration-dependence. So the fixtures run both ways:

| fixture | role | must |
|---|---|---|
| `offender_shell.sh` | 🔴 **positive**, frozen from a real shape | be CAUGHT as `hardcoded` |
| `offender_python.py` | 🔴 **positive** — a variable bound to a dated literal, then written, which is the commonest real shape | be CAUGHT, both paths |
| `mixed_clock_and_literal.py` | 🟡 **ambiguous** | be seen, and classified `clock` — never `hardcoded` |
| `clean_clock.sh` | 🟢 **negative** | be out of scope entirely |
| `clean_mention.py` | 🟢 **FABRICATED negative** — names a dated path three times, in a docstring, a comment and a READ, and writes to an UNDATED path | stay SILENT |

🔴 **The fabricated negative is the one that matters.** It was written to be the
most plausible false positive available — a script whose whole job is to cite
pass `120`'s evidence — and the gate stays silent on it.

🟡 **And the gate excludes its OWN directory from a repository sweep**, because
its rule prose, its tests and its controls all quote dated filenames
deliberately. The first run of it over `compose/code/` reported `19` hardcoded
writes in `7` instruments; `5` of those writes and the seventh instrument were
this gate describing itself. 🔵 **The exclusion is an explicit path, not a
`fixtures/` heuristic — a blanket rule would hide real offenders in other
instruments' fixture trees — and `exclude_self=False` is what the suite passes
so the controls can still be measured.**

## What it found in this repository

🟢 **`14` hardcoded dated writes across `6` instruments** —
`p120-unread-grant-resolution` (`3` files, where p174 had named `2`),
`p1040-ecl-corpus-census`, `p1026-archive-regression-census`,
`p164-equity-fix-controls`, `p326-titleholder-book-license`,
`p345-oer-four-forms`. Full rows in `result.2026-10-13-p175.tsv`.

## The second instrument, and the column whose absence confounded the answer

`rerun_dated.py` re-runs each instrument's scripts from inside their own
directory, hashes every dated file before and after, reports
`CHANGED`/`CREATED`/`DELETED`, and **restores the instrument to `HEAD`
unconditionally** — so the measurement cannot destroy the evidence it measures.

🔴 **It also prints a `RAN` row carrying the EXIT CODE for every script, and
that column is the finding.** Across `5` instruments and `28` executions:

| measurement | value |
|---|---|
| 🟢 instruments re-run | `5` |
| 🟢 script executions | `28` |
| 🔴 **dated files CHANGED** | 🔴 **`2`, in `1` instrument** — `p120`'s `score.` and `phantom-claims.2026-10-11.tsv`, by both `score.py` and `score_after.py` |
| 🔴 **executions exiting NON-ZERO** | 🔴 **`9` of `28`** |

🔴 **And `p326/census_items.py` and `p345/corte_figuras.py` — two of the four
instruments whose dated files did NOT change — are among the failures.**
🔵 **They did not hold their evidence steady; they could not run.** An instrument
that fails reports identically to one that is deterministic, in any sweep that
does not record the exit code. That is `gap 131`, and `ACTION KL` measures the
full-suite rate against this `5`-instrument sample.

## Files

| file | what |
|---|---|
| `dated_write.py` | the classifier; rule in the docstring, boundary included |
| `rerun_dated.py` | the re-run harness, with the `rc` column and an unconditional restore |
| `test_dated_write.py` | `13` offline tests — `4` positive, `3` negative, `1` ambiguous, `5` rule-shape *(one of which asserts the self-exclusion)* |
| `fixtures/` | the controls above |
| `result.2026-10-13-p175.tsv` | the static sweep over `compose/code/` |

🟢 **Reproduce:**

```bash
python3 -I test_dated_write.py                       # 12/12
python3 -I dated_write.py ../                        # the static sweep
python3 -I dated_write.py ../ --summary              # counts only
python3 -I rerun_dated.py <repo-root> <instrument>…  # the dynamic sweep
```

🔴 **One limit, declared:** `rerun_dated.py` executes repository code. It
restores to `HEAD` afterwards, but it should not be run against a tree with
uncommitted work in `compose/code/`, because the restore is a `git checkout`
and a `git clean` scoped to the instrument directory.
