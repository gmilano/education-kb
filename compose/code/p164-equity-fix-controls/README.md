# `p164-equity-fix-controls` — does P163-A's equity fix cost the control?

**Pass 164, 2026-10-13.** Written and executed in-pass, discharging `ACTION IL`.

`test_fix_controls.py` — **9 passed, 0 failed**.
`run_fix.py` → `result.2026-10-13-p164.tsv`, 14 rows.

Builds directly on [`../p163-script-equity-gate/`](../p163-script-equity-gate/README.md),
importing its `script_equity.py` and `corpus.py` unchanged so that the two passes are
measuring the same bytes with the same instrument.

## The question

`ACTION IL` was pre-registered at the end of p163:

> port `P163-A` step 1 (the nine-script corpus as JUnit cases) and step 3 (counting
> `Mn`/`Mc` as letters) and measure whether the symbol-spam control still rejects at `0.000`.
> *Refuted if treating combining marks as letters lets ANY of the two negative controls
> through — which would mean the fix trades a real guard for the equity gain.*

p163 designed the fix and did not apply it. The open risk was the obvious one: a gate made
more permissive to admit Devanagari and vocalised Arabic might also admit the junk it exists
to reject.

## What is measured

Two changes, applied **separately** so each is attributable:

| variant | change |
|---|---|
| `step2` | the ratio's DENOMINATOR counted in code points, not UTF-16 code units |
| `step3` | `Mn`/`Mc` (combining marks) counted as letters — the registered one |
| `step2+3` | both |

Only the letter-ratio limb is swapped. The empty guard, the whitespace strip, the
min-length guard and the trigram-entropy limb are upstream's, untouched — so any verdict
change is attributable to the ratio change alone. A **fidelity gate** asserts that the
unpatched variant reproduces `p163`'s `gibberish_check` on all 14 rows before any result is
read; it reports `0` mismatches.

## Result

| tag | ratio upstream | ratio fixed | margin upstream | margin fixed |
|---|---|---|---|---|
| `en` / `de` / `es` | `0.976`–`0.977` | unchanged | `0.526`–`0.527` | unchanged |
| `zh` / `ja` / `ko` | `0.935`–`0.953` | unchanged | `0.485`–`0.503` | unchanged |
| `ar` (unvocalised) | `0.980` | unchanged | `0.530` | unchanged |
| **`ar-voc`** | `0.552` | **`0.990`** | **`0.102`** | **`0.540`** |
| **`hi`** | `0.591` | **`0.983`** | **`0.141`** | **`0.533`** |
| **`th`** | `0.815` | **`1.000`** | `0.365` | **`0.550`** |
| **`CTRL-extB`** (astral Han) | `0.500` | **`1.000`** *(step 2)* | `0.050` | **`0.550`** |
| `CTRL-mash` | `1.000` | `1.000` | — | **still REJECTED (entropy)** |
| `CTRL-symbols` | `0.000` | **`0.000`** | — | **still REJECTED (letter-ratio)** |

**Margin spread across the ten valid answers: `5.2×` → `1.1×`.**

## Verdict

**`ACTION IL` DISCHARGED, falsifier SILENT.** Both negative controls still reject under
`step3` and under `step2+3`, and the symbol-spam control rejects at exactly `0.000`, the
value the falsifier named.

The result is stronger than "measured and happened to pass", and the reason is worth
stating: **the fix cannot reach either control by construction.**

- `CTRL-symbols` is digits and ASCII punctuation. Those are neither `L*` nor `Mn`/`Mc`, so
  widening the predicate to include combining marks adds **zero** to its numerator. Asserted
  directly in `test_digits_and_punctuation_are_neither_letters_nor_marks`.
- `CTRL-mash` (`"a" × 49`) has a letter ratio of `1.000` **before** the fix. The ratio limb
  never rejected it; **entropy** did, at `0.000`. A ratio change cannot move a verdict the
  ratio was not making.

## What this confirms about p163 — and the one thing it corrects

p163 made three quantitative predictions about a fix it did not run. All three are confirmed:

| p163 predicted | p164 measured |
|---|---|
| vocalised Arabic `0.552` → `~0.99` | **`0.990`** |
| Hindi `0.591` → `~0.98` | **`0.983`** |
| astral Han `0.500` → `1.000` | **`1.000`** |

This is the first time this shelf has confirmed a numeric prediction made in an earlier pass.

**The correction, recorded rather than quietly fixed:** the first p164 draft of `fixed_gate.py`
omitted upstream's whitespace strip (`replaceAll("\\s+","")`) and produced ratios that
disagreed with p163's recorded TSV — English `0.823` against the recorded `0.976`. The
disagreement with the *previous pass's committed numbers* is what caught it, which is the
argument for committing the TSV rather than only the prose. The fidelity gate now in
`run_fix.py` and `test_fix_controls.py` makes that failure mode loud instead of silent.

## Honest limits

- This is a **Python replication**, not the JVM. It is proved faithful against p163's
  replication, which was itself proved against all `15` upstream JUnit oracle cases — but a
  chain of two replications is not a run of upstream's suite.
- `P163-A` steps 4 and 5 (extending `isCJK`, giving Thai a branch) are **not** measured here.
  `ACTION IL` registered steps 1 and 3 only.
- The ten valid answers were **already accepted** before the fix. The gain is margin — i.e.
  robustness against drift — not a verdict that changes today. That is exactly why the
  corpus is contributable upstream as tests now: it locks in current correct behaviour.

## Files

| file | what it is |
|---|---|
| `fixed_gate.py` | the patched ratio + the pipeline with only that limb swapped |
| `run_fix.py` | emits the margin table and the falsifier judgement |
| `test_fix_controls.py` | 9 cases: fidelity, both controls, p163's three predictions, margin spread |
| `result.2026-10-13-p164.tsv` | 14 rows, the table above |
| `script_equity.py`, `corpus.py` | copied unchanged from `p163-script-equity-gate` |
