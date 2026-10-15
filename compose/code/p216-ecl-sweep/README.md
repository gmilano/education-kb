# p216 — `ACTION QI`: the ECL-2.0 classifier blind spot, and the QG gate's scope

## What this measures

Two things that share a reader:

1. **`ecl_sweep.py`** — every Apereo/Sakai/uPortal/Opencast/Unicon-family slug carried on the four
   client-facing shelves, read first-hand through `raw.githubusercontent.com/<slug>/HEAD/<path>`
   and classified **twice**: once with p215's classifier reproduced verbatim (`classify_p215`),
   once with the same classifier plus an ECL token (`classify_p216`). The **delta** between the two
   is the measurement.
2. **`qg_gate3.py`** — `ACTION QG`'s placement step. p215's gate declares an 8-file scope; this KB
   publishes current-state grant claims in ten. The script runs the same reader over both sets and
   reports the difference, then `adjudicate_scope.py` attaches each hit to its enclosing heading.

## Result

**`8` of `13`** family rows are `ECL-2.0`. **p215's classifier returns `UNCLASSIFIED` on `8` of
`8`** — it does not mis-name the family, it names nothing. `3` of `3` genuine `Apache-2.0` controls
(`uPortal-Project/uPortal`, `Unicon/tool13demo`, `Apereo-…/Larissa`) classify identically on both
instruments, so the new token does not over-fire.

On the cells: **`157` of `160`** grant-claim lines across all ten files already say `ECL-2.0`, so
the shelves were right and the instrument was not. `2` of the `3` exceptions are not grant cells
(a slug-resolution note; a table about per-file licence *headers* — `P215`'s documented comparator
exclusion).

On the scope: `intel/open-gaps.md` and `README.md` hold `50` grant-claim lines touching p215's `25`
recoveries, `19` of them contradicting. **All `19` are inside dated pass sections** — records, like
the `93` p215 left alone in the append-only shelves — so the 8-file scope is **sufficient** and the
gate can be wired into `make hooks` unchanged (`ACTION QO`).

## The ordering constraint (the whole trick)

`ECL-2.0` self-describes, in its own preamble (`sakaiproject/sakai` `LICENSE` l.9–13):

> "The Educational Community License version 2.0 ("ECL") consists of the Apache 2.0 license,
> modified to change the scope of the patent grant in section 3 to be specific to the needs of the
> education communities using this license."

So its **body is Apache-2.0's text**. A whole-body matcher returns `Apache-2.0`; a title-window
matcher that tests `apache license` before `educational community license` returns `Apache-2.0`
too. **The ECL token must be tested first.**

The operative difference is in the patent grant (l.95–100): a patent licence for contributions by
an institution-employed author reaches only claims where that author is also the inventor *and* the
institution has the right to grant under applicable grant and research-funding agreements. That is
a contract-review trigger, not a label.

## Byte counts are a drift control, never a classifier input

`ECL-2.0` ships in **five** byte-lengths across this family: `9 878`, `9 919` (×3), `11 087` (×2),
`11 120`, `11 340`. A length comparator would call them five licences. As a *drift* control the
same numbers are excellent — `3` of `3` byte-exact against readings taken 4 and 16 passes ago.

## Method note worth keeping

`adjudicate_scope.py` first used the **nearest** heading and reported `9` live claims. Testing the
enclosing **level-2** heading (the pass boundary) reports `0`. The heading *level* was the whole
measurement — the same instrument-versus-population lesson this KB keeps re-learning.

## Run

```sh
cd /home/user/education-kb
python3 -I compose/code/p216-ecl-sweep/ecl_sweep.py compose/code/p216-ecl-sweep/slugs.txt
python3 -I compose/code/p216-ecl-sweep/qg_gate3.py
python3 -I compose/code/p216-ecl-sweep/adjudicate_scope.py compose/code/p216-ecl-sweep/unswept-hits.tsv
```

Network: `raw.githubusercontent.com` only (`200` here; `api.github.com` is `403`). `qg_gate3.py`
and `adjudicate_scope.py` are entirely offline.

## Evidence

- [`evidence/ecl-classifier-blindspot.2026-10-15-p216.tsv`](../../../evidence/ecl-classifier-blindspot.2026-10-15-p216.tsv)
- [`evidence/qg-scope-adjudication.2026-10-15-p216.tsv`](../../../evidence/qg-scope-adjudication.2026-10-15-p216.tsv)

## What this does NOT establish

`ECL-2.0` was **not** discovered this pass. `repos/foundations.md` l.1373 is a full pass-200
section on it, p199 characterised it before that, and p212 published `OpenLRW` as `ECL-2.0`.
`ACTION QI` was registered on a claim of novelty that the shelves refute (`T216-2`), and this
instrument's real product is the repaired classifier, the `5` new grant cells on the Apereo
learning-analytics tier, and the drift controls — not the family.

## Reproducibility note — the figures are pre-write

The counts published in p216's shelf sections (`157` of `160` for JOB 1; `19` contradictions for
JOB 2) were measured against the shelf state **before** p216 wrote its own sections.

Re-running the gate **after** the write returns `166` of `169` and `21`, because p216's own
sections add correctly-stated `ECL-2.0` cells and quote `T215-2`'s superseded reading.

The `+2` outside the gate's scope are both at `intel/open-gaps.md` l.`28` — the `ACTION QH` verdict
row, which quotes the words *"recorded `ABSENT`"* in the act of stating that the reading was wrong.
That is `P215`'s documented comparator exclusion: **a line about a wrong reading prints the wrong
reading's tokens.** It is a record, not a cell, and it is not corrected.

Anyone re-deriving these numbers should either check out the parent commit or subtract this pass's
own sections. The *verdicts* are unaffected: JOB 1's exceptions remain `3`, of which `2` are not
grant cells, and JOB 2's live-claim count outside the gate's scope remains `0`.
