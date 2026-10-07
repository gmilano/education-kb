---
industry: education
region: Global
updated: 2026-10-07
---

# `p471-gap-gate-language/` — the gate was fine. It could not read the corpus any more.

**What it measures.** The *coverage* of `p370-gap-gate/` over a corpus: for every declared-gap
sentence that names exactly one region, whether the gate can assign it a **scope** as shipped, and
whether it can once English markers are present. The boolean that matters is `language_blind` —
the gate cannot scope the sentence as shipped but **can** with English markers. That class is the
set of claims the gate silently declines to judge.

## Why it exists

`p370-gap-gate/` is correct and its suite is **27/27**. The pass that introduced it reported
**29 gap sentences with a region → 2 CONTRADICHOS**.

Swept against the live tree on **2026-10-07** it reports **5 gap sentences → 0 CONTRADICHOS, all
5 `NO-CLAIM` / `SIN-ALCANCE`**.

🔴 **The KB did not stop declaring gaps.** `repos/foundations.md` declared an EMEA gap for **three
consecutive passes** (`P467`), and the claim was **false**: `OpenOLAT/OpenOLAT` (Apache-2.0, OLAT
from the University of Zurich, maintained by frentix GmbH) and `OpenOLAT/qtiworks` (BSD-3-Clause,
University of Edinburgh) were already on these shelves — one of them already tagged `🟢 EMEA`
(`P469`).

**What changed is the language the KB writes its gaps in.** Two *independent* filters in
`gap_gate.py` are Spanish-only, and either one alone is enough to lose the claim:

| Filter | Role | Behaviour on the real `P467` sentence |
|---|---|---|
| `GAP_SENTENCE` | the extractor `--sweep` uses; matches `hueco`, `cero repositorios`, `sigue abierta` | 🔴 **extracts nothing** — a sweep never presents the sentence for judgement at all |
| `INDEX_MARKERS` / `CHANNEL_MARKERS` | the **scope** classifier | 🔴 falls through to `SIN-ALCANCE` → verdict `NO-CLAIM` |

Measured, verbatim sentence:

```
verdict=NO-CLAIM  scope=SIN-ALCANCE  region=EMEA  contradicting_rows=0
```

🔵 **Note `region=EMEA` resolved correctly.** `region_in_prose` is language-independent, because the
five region names are identical in both languages. **So the gate knew which region the claim was
about and still declined to judge it.** Meanwhile the tree carries **94 repo rows naming EMEA beside
a GitHub URL**, **77** of them *placed* (region heads the cell). The contradiction material was
abundant; the gate never reached the comparison step.

With `MARKERS_EN` installed, the same sentence returns:

```
verdict=CONTRADICHO  scope=INDICE  region=EMEA  contradicting_rows=94  (77 placed)
```

## The discrimination that keeps this a gate and not a word counter

🔵 **The mandatory case in the suite is that the two wordings of the *same* gap get OPPOSITE
verdicts**, in English, exactly as `p370-gap-gate/` requires for Spanish:

| Wording | Scope | Verdict |
|---|---|---|
| *"…it can find **no EMEA-origin** permissive education foundation."* | `INDICE` | 🔴 **CONTRADICHO** (94 rows) |
| *"No EMEA-origin permissive education foundation was found **through the forges this environment can reach**…"* | `CANAL` | 🟢 **SOSTENIDO** |

The second is `P467`'s own "defensible sentence" — and it is genuinely not refutable by index rows.
A channel gap is a claim about the **query**; an index gap is a claim about the **corpus**. If both
fired, this would be counting the word "gap".

A sentence that merely *contains* "gap" (*"LATAM's governance gap is now measured by a UN-system
instrument"*) stays `SIN-ALCANCE` in both languages. That is also a test.

## The transferable failure — `P471`

🔴 **`NO-CLAIM` is not a safe default.** A gate that cannot *parse* its input returned the same
verdict it returns for prose that is **not a claim at all**. A reader of the sweep sees *"nothing to
judge"* where the truth was *"I cannot read this."*

🔵 **The general rule: an instrument whose coverage depends on the prose language of the corpus
decays the moment the corpus changes language, and reports full health while doing it.** `27/27` and
`0 CONTRADICHOS` were both true and together they were misleading. **A passing suite measures the
cases you wrote, never the class you stopped writing.**

🔵 **The cheap guard, and it is the reusable part:** a gate that classifies should distinguish
*"not a claim"* from *"unparseable"*, and a sweep should report its **denominator** — how many
candidate sentences it examined — so a collapse from 29 to 5 is visible as a collapse rather than as
quiet good news.

## This does not replace the gate

`p370-gap-gate/` stays the instrument of record for `P370`/`P371`. This module **imports** it
(`P237`: the gate is measured, not reimplemented) and only reports coverage. `MARKERS_EN` is the
patch to fold back into it, kept separate here so the finding is reproducible against the gate
exactly as it was when the finding was made.

⚠️ `with_english()` **mutates a module other instruments import.** `scope_both()` and `coverage()`
save and restore that state, and two tests assert they do.

## Run

```
python3 gap_language.py --self-test            # 16/16, and nests the gate's own 27/27
python3 gap_language.py --coverage /path/to/kb
```

Measured on the live tree, 2026-10-07: **50 gap sentences with a region, 8 language-blind.** Among
the 8, a second false index-scoped claim in English that nothing had flagged:
*"…rested on **no LATAM-origin permissive education project**."*

## 🔴 `P472` — the retraction trips the gate, and that is not a bug in the retraction

Measured on this tree **after** `P467` was withdrawn, with `MARKERS_EN` installed:

| Index-scoped claims the gate marks `CONTRADICHO` | **11** |
|---|---|
| carrying **quotation or table-citation** markers | **9** |
| narrowed by a **maturity qualifier** the gate cannot measure | **2** |
| **bare live assertions** | 🟢 **0** |

🔴 **A gate that failed the build on `CONTRADICHO` alone would have produced 11 false failures and
0 true ones.** And the cause is structural, not sloppiness: **the correct way to retract a false gap
is to quote it in the retraction** — `repos/foundations.md` now carries
`> **Superseded text:** *"no EMEA-origin permissive education foundation."*` — so **a correct fix
makes the gate fire forever.** An instrument that punishes the fix trains people to fix things
quietly.

🔵 **The second class is subtler and matters more for honesty.** *"No LATAM-origin permissive
education product **at production maturity**"* is a claim about **maturity**, not existence. Placed
rows prove assets exist; they say nothing about whether any is production-grade. **The gate compares
on existence, so it must not be allowed to refute a claim quantified on a dimension it never
measured.**

**The fix, implemented here:** `assertion_class()` returns `QUOTED` / `QUALIFIED` / `ASSERTED`, and
`build_verdict()` fails **only** on an `INDICE` + `CONTRADICHO` + `ASSERTED` claim. Quotation wins
over qualifier, because a retraction that quotes a qualified claim is still a retraction.

```
would FAIL build under P45: 0
Counter({'CONTRADICHO-but-QUOTED': 9, 'CONTRADICHO-but-QUALIFIED': 2})
```

🔵 **Generalised: a contradiction detector needs a speech-act classifier in front of it.** *Asserting*
X, *quoting* X, and *asserting X under a qualifier* are three different acts, and only the first is
refutable by the corpus. This is the same lesson as `P471` one level up — `P471` is "the gate could
not **read** the claim", `P472` is "the gate could not tell **what the sentence was doing**."

Suite: **25/25**, nesting `p370-gap-gate`'s **27/27**.
