# p208 — `ACTION PT`: seed the errors on purpose, and find out what the audit can see

`ACTION PT` asked one question. Three passes had each audited this KB's licence column and each
reported mismatches that were all false — **24 reported, 0 true** (p205: 3/0, p206: 3/0,
p207: 18/0). Two readings of that are observationally identical from inside those passes:

* **(a)** the column is clean and the audit is merely noisy, or
* **(b)** the audit cannot detect a wrong cell **at all**, and three passes measured nothing.

PT's falsifier: *seed 5 deliberate errors and re-run; catching 4+ means the audit works
(limb 1); catching ≤2 means it is blind (limb 2).*

**It caught 3.** The falsifier lands between its own limbs — and the 3/2 split is not noise.
It is exactly what the instrument's shape predicts, which is the actual answer to PT.

## The shape: p205–p207 compared a UNION, so most of the column could not be audited

All three passes compared the true family against **every family token appearing on every line
that names the repository**. A repository whose true family is printed at two or more sites
therefore **cannot produce a mismatch no matter what any single cell says**: the right answer is
still in the union.

Measured over the 179 clean census rows — [`../../../evidence/comparator-reach.2026-10-14-p208.tsv`](../../../evidence/comparator-reach.2026-10-14-p208.tsv):

| the true family is printed at … | rows | a seeded error is |
|---|---|---|
| exactly **1** site | **27** (15%) | detectable |
| **2 or more** sites | **152** (85%) | 🔴 **undetectable by construction** |

So `Gap 467`'s "~100% false-positive rate" was never a property of this column. **85% of the
column was outside the instrument's reach**, and the three seeds that landed inside it were
caught 3 for 3 while the two outside it were missed 2 for 2.

## Three comparators, same seeds, same tree

* `audit.sh` — per **repo**, the union comparator p205–p207 used, rebuilt to take a directory so
  it can be aimed at a scratch copy. p207's audit was ad hoc and could not be aimed anywhere,
  which is why this question went three passes unasked.
* `audit_persite.sh` — per **line**. One verdict per line that names the repo and carries a
  token.
* `audit_percell.sh` — per **cell**: table rows only, and only rows naming **exactly one**
  repository, so the token belongs to that repository by construction. Rows naming two or more
  are skipped as ambiguous rather than reported.
* `seed.sh` — builds the scratch copy and writes the 5 wrong cells into it. Nothing in it
  touches the published tree.

| comparator | unit | seeds caught | candidates on the real tree | true | precision |
|---|---|---|---|---|---|
| per-repo *(p205–p207)* | union of all lines | **3 / 5** | 6 repos | **0** | `0`% |
| per-line *(p208)* | line | **5 / 5** | 61 sites | **7 sites, 2 repos** | `11`% |
| per-cell *(p208)* | single-repo table row | **5 / 5** | 12 cells | **6 cells, 1 repo** | 🟢 **`50`%** |

Seeding moved the per-line count 61 → 66 and the per-cell count 12 → 17: **+5 and −0 in both
cases**, the five seeded sites and nothing else.

## What this found, which is the point of asking

🔴 **Two true positives — the first in four passes of licence auditing.**

1. [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) was published **`MIT`
   in 6 cells across 4 files** while its own blob at `HEAD` is **`Apache-2.0`, `11 386` B**. The
   file was added **once**, in commit `b151505` on **28 June 2026**, and never replaced, and the
   repository sidebar reads `Apache-2.0` — so the cell was never right, and it is not a
   relicensing the KB failed to notice.
2. [`openfun/ralph`](https://github.com/openfun/ralph) was published **`Apache-2.0`** in a p193
   recipe step while its blob is **`MIT`, `LICENSE.md`, `1 094` B**.

🔵 **Both are UNPROPAGATED CORRECTIONS: in both cases this KB holds the right value elsewhere**
— `Apache-2.0` for `ai-tutor-app` on the agent shelf with its `md5`, `MIT` for `ralph` at some
fifteen other sites. The wrong value survived three dedicated audits because the right value was
in the union those audits compared against. **A correction here is published, not propagated.**

`ralph`'s site is a prose sentence inside a recipe, so **only the per-line comparator could see
it**; the six `ai-tutor-app` cells are table rows, where per-cell is five times more precise.
Neither comparator dominates: tables want per-cell, prose needs per-line.

## Honest limits

* Ground truth is p207's 185-row census, so this measures the **permissive-half population**,
  not the whole column.
* The per-line comparator's 54 false positives are the shape p206 and p207 already named: a line
  that names several repositories, or whose prose is *about* a licence divergence
  (`microsoft/autogen`'s `CC-BY` root over an `MIT` `LICENSE-CODE`;
  `cccareers/open-source-curriculum`'s manifest-vs-file split). `T207-3` holds: **when a flagged
  row's prose is about licensing, the row is usually the finding and the audit is the error.**
* The per-cell comparator cannot see prose at all, and skips multi-repo rows by design.
* `audit.sh` and `audit_percell.sh` are offline. `seed.sh` is offline. Verifying a true positive
  against `raw.githubusercontent.com` is not.

Run: `./audit.sh <kb-dir>`, `./audit_persite.sh <kb-dir>`, `./audit_percell.sh <kb-dir>`,
`./seed.sh <kb-dir> <scratch-dir>`.
