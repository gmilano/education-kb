---
industry: education
region: Global
updated: 2026-10-08
---

# `p598-register-freshness-gate/` — `Gap 252` remedy 2, closed with code

**What it proves:** that **2 of 12** rows in `intel/open-gaps.md` carrying a freshness claim were
**stale** — contradicted by this KB's own live tree — and that the other 10 were not, each for a
*named* reason rather than by omission.

**Why it exists:** `Gap 252` (pass 48) named three remedies and left two open. The one it called
**"the honest next instrument"** was a freshness rule for the priority column *plus a check*. This
directory is that check.

## 🔴 Pass 49 is the evidence that this was not optional, because pass 49 paid for it

Pass 48 found the positional defect on `Gap 39` **by inspection**. Pass 49 found it on `Gap 246`
**by paying for it**: it read the register top-down, saw *"the spaCy `pt_core_news_*` model artefact
licences **are unmeasured**"*, judged that the cheapest open item, and spent its budget measuring
them. 🔴 **They were already measured** — `verticals/solutions.md` carries **CC-BY-SA-4.0** and says
in as many words *"was published as 'unmeasured', now measured."*

🟢 **Two instances, two rows, two independent discovery modes.** That is what pass 48 said it could
not yet claim, and it is why the defect is not confined to `Gap 39`.

## The rule this enforces

> No row may carry a **priority superlative** ("cheapest win", "smallest gap") if a later row closes
> that gap; and no row may assert a **measurement claim** ("unmeasured", "untested", "unjudged")
> whose subject is measured elsewhere in the live tree.

## The discrimination that makes it a gate and not a `grep`

🔴 The easy error is to flag every row that says *"unmeasured"*. **Most of them are right** —
`Gap 244` says 31 shell instruments are unjudged and they **still are**. Flagging it would be the
`P371` error and would bury the instrument in noise.

A row is `RANCIA` only when the live tree **contradicts** it, and the evidence is chosen by claim
class:

| Claim class | Refuted by | Why not the other one |
|---|---|---|
| `MEDICION` | a **measurement** of the row's own subject in the live tree | a status claim is falsified by a reading |
| `PRIORIDAD` | a later **closure** of that gap, in the register | 🔴 a licence measurement cannot tell you whether a gap is still open |

🔴 **Rows that carry their own correction are exempt** (`CITA`). Without that, the gate flags the
*"rows pass N changed"* tables — i.e. **the act of correcting** — and a staleness detector whose
naive form punishes the behaviour you want gets switched off in a week.

## 🔴 The run history, because three of the four defects were self-inflicted

| Version | Flagged | Adjudicated by hand | Defect found |
|---|---|---|---|
| **v1** | 6 | 🔴 **4 false positives**, 1 right-verdict-wrong-evidence, 1 correct | (1) quotation cells flagged ×2; (2) ALL-CAPS pseudo-subjects — `REFUSES`, `MEASURES` (verdict classes) and `PATH`, an env var colliding with the word *"path"* tree-wide; (3) a **priority** claim refuted by an unrelated **licence** measurement |
| **v2** | 2 | 🟢 **both true positives, right evidence** | (4) 🔴 after the forward pointers landed, `Gap 240` was flagged on the **`Gap 245` row** — two gap numbers on one line, closure attributed to the one merely *cited* |
| **v3** | 0 | 🟢 register clean, exit **0** | — |

🔵 **Why v1's precision is published rather than quietly fixed.** `P543` is this KB's own record that
`Gap 243`'s one-line remedy **over-accused** (49 → 23). 🔴 **The same thing happened here, to the
instrument built to prevent it**, and an instrument's first-run precision is the only honest
estimate of what its verdicts are worth.

## The mutant that matters

🔴 For defect (4) the obvious mutant — loosening `GAP_ROW` — **survives while telling you nothing**:
the looser regex still captures the declared number first. 🟢 **The faithful mutant makes
`declared_gap()` accept a line that merely *mentions* the gap**, which is what the defect was.
🔴 **A mutant that cannot fail reports coverage it does not have.**

## Suite

🟢 **58 assertions, 7/7 mutants killed.** The mandatory case is
`opposite_verdicts_on_real_rows`: two **real** rows of this tree must come out **opposite** —
`Gap 246` `RANCIA` (measured in `verticals/`), `Gap 244` `SOSTENIDA` (its 31 shell rows still
unjudged, and it names no measurable artefact).

🔴 **One assertion was removed rather than satisfied.** v2's suite required the **live** sweep to
return both `RANCIA` and `SOSTENIDA` rows — which tied the suite to the tree staying **broken**, so
fixing the three rows made it fail for the right reason. 🟢 **Discrimination is now asserted over
*constructed* rows**, where the input is controlled; over the live tree the only legitimate demand is
that every row be **classified**, not that any be **accused**.

🟢 **It refuses its own empty input** (`P541` / `Gap 245`), and the `p542` sweep classifies it
`REFUSES`: the instrument documenting that defect did not reproduce it.

## Use

```
python3 freshness_gate.py --self-test
python3 freshness_gate.py --sweep /path/to/education-kb    # exit 1 on any P598-RANCIA
```

🔴 **`Gap 255` is the limit, declared rather than hidden:** nothing *invokes* this gate. A convention
a pass has to remember is not a control (`P237`).
