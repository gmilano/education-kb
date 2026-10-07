---
industry: education
region: Global
updated: 2026-10-07
---

# `p449` — the gate this corpus needed for two passes: prose against data, both directions

**Pass 28 of 2026-10-07.** Not pre-registered: built because pass 28's three unrelated actions
landed in the same place pass 26 did, for the third time.

Pass 26's closing diagnosis, which proposed no fix:

> *"A corpus that versions both prose and instruments has to reconcile them, and nothing in this
> repository did — `p342` explicitly chose the other direction, asserting 'against the TSVs, not
> against the prose'."*

## What it proves

Over 6 published `.md` files, **431 slugs with a bound licence claim** in prose, and **510 lines
where a slug and a licence co-occur and the binding rules REFUSED** (published as a denominator, not
hidden):

| Verdict | n | |
|---|---|---|
| `AGREE` | **299** | prose and today's measurement agree |
| `PROSE-ONLY` | 83 | prose names a family for a slug the data has no row for |
| `PROSE-MIXED-INCLUDES-TODAY` | 29 | the corpus says two things; the gate **abstains** |
| 🟡 `STALE-DATA` | **14** | **prose right, published data behind** |
| `DATA-ABSTAINS` | 5 | classifier returned `UNKNOWN` — a refusal, not a contradiction |
| 🔴 `CONTRADICT` | **1** | prose wrong |

🔴 **Prose and data disagree on 15 of 431, and the prose is right in 14 of 15.** With pass 26's
four-for-four, this corpus's record is **18 of 19** in favour of the sentence a human wrote.

🔴 **The nineteenth is the mechanism, not a counterexample.** The single `CONTRADICT` is
`oat-sa/lib-lti1p3-core` (prose LGPL-2.1, payload **GPL-2.0**) — and the pre-reset archive carries
GPL-2.0 for it in **nine** places, once as a deliberate finding. The prose **regressed**: a correct
human reading was overwritten by the classifier's wrong answer (`P452`), and `intel/market.md` then
published EMEA architecture advice concluding *"neither is a blocker."*

## The five defects it had to find in itself first

Its first build produced **16 `CONTRADICT` rows and eleven were its own**. Each is now a control.

| # | Defect | Caught by |
|---|---|---|
| **`P451`** | unanchored acronyms — `MPL` matches inside "exa**mpl**e", `ECL` inside "edgam**ecl**aw". **This is pass 26's `UNLICENSE`-inside-`UNLICENSED` defect, re-imported one pass later** (`p432`, third occurrence) | the sweep's own output being implausible |
| `P385` at cell level | one cell naming three slugs and one licence bound the licence to all three (`repos/foundations.md:607`). Now: **one slug per cell, or refuse** | inspection of the reported lines |
| abstention as contradiction | six rows were `CONTRADICT` against `today=UNKNOWN`. An instrument that declined to answer has contradicted nothing (`P160`, `P184`) | inspection |
| path-shaped slugs | `main/LICENSE` has slug shape, so the licence of every row bound to the **path** instead of the repository | 🟢 **the control, not the sweep** |
| URLs invisible | the slug regex cannot start inside `github.com/owner/repo`, the commonest form in this corpus, so those mentions matched **nothing** | 🟢 **the control, not the sweep** |

## Reproduce

```sh
python3 test_reconcile.py        # 59/59, offline, fixtures only
python3 reconcile.py ../../../agents/top.md ../../../repos/foundations.md \
    ../../../verticals/solutions.md ../../../intel/market.md \
    ../../../intel/trends.md ../../../compose/patterns.md \
    ../p447-deep-grant-divergence/divergence.tsv \
    ../p436-fork-hypothesis/payloads.2026-10-07.tsv
```

Offline in both cases: it reads this repository and two TSVs, nothing else.

## Declared limits

- **Binding is conservative and refuses rather than guessing.** 510 co-occurrences went unbound.
  A refusal is a measurement (`P160`); the denominator is published beside it.
- **It abstains on the 29 rows where this corpus contradicts itself**, and at least one of those
  carries a live error (`Citolab/qti-components`, described as both GPL and LGPL across nine
  mentions, is GPL-3.0). Resolving them by **pass date** is pass 28's pre-registered action A.
- `PROSE-ONLY` (83) is published as a **count, not a finding**: it mixes repositories the data layer
  genuinely lacks with slug-shaped strings that are not repositories.
- It compares **families**, not qualifiers. A row agreeing on `CC-BY` may still disagree on
  `NonCommercial`, which is the distinction that decides commercial use (`P449`). Qualifier
  reconciliation is pass 29's action C.
