# p216 — `ACTION QK`: person-level inferences resting on an absence reading

## Why this action existed

`T215-7`: this KB published *"this author ships unlicensed education connectors as a pattern"*
about a **named individual**, derived from two root-only `ABSENT` readings. Both repositories
declare `MIT` in their manifests. p215 withdrew the claim in place.

p215 called `QK` *"the highest-priority action in this table: it is the only class whose errors are
about people rather than artefacts."* `QK` asks whether it was the only one.

## Method

For every line on **ten** files (the four client-facing shelves, `intel/market.md`,
`intel/trends.md`, `compose/patterns.md`, both trending shelves, `intel/open-gaps.md`, `README.md`),
two independent questions, reported as a conjunction:

- **(a)** does the line attribute a **practice, habit or character** to an actor — `this author`,
  `the maintainer's`, `el autor`, `as a pattern`, `ships unlicensed`, `habitually`,
  `systematically`, …?
- **(b)** does that line or either neighbour carry an **absence marker** — `ABSENT`,
  `NOASSERTION`, `no licence`, `sin licencia`, `ungranted`, `404`, `unlicensed`?

Deliberately **high-recall**, with every hit printed verbatim: a sweep for claims about people must
not be the one that quietly drops candidates. Adjudication is by hand, in the pass notes.

Two controls are printed so the conjunction's size is interpretable: how often each side fires
alone.

## Result — limb 2 fires

| measure | value |
|---|---|
| candidate lines (both conditions) | **43** |
| further **person-level** practice claims | **0** |
| the withdrawn `ink-waffle` claim and its withdrawal records | 4 |
| artefact- or shelf-scoped claims, correctly bounded | **39** |
| control: actor-claim lines with no absence marker | 75 |
| control: absence lines with no actor claim | 3 365 |

The **39** are the shape such a claim *should* have — *"9 of 21 published connector packages ship
no licence file"*, *"1 of 21 practise per-file notice"*, *"3 of three published jars ship no licence
text"*. Each names a **measured population of payloads** and stops there. The withdrawn claim
generalised from two root-only readings to what a person habitually does.

So `P215-6`'s rule holds, now with a measurement behind it: **a row may record what a channel
returned; a claim about a PERSON needs a channel that can support it** — and on 43 candidates this
KB broke that rule exactly once.

## Run

```sh
cd /home/user/education-kb
python3 -I compose/code/p216-person-claims-sweep/sweep.py
```

Entirely offline.

## Evidence

[`evidence/person-claims-sweep.2026-10-15-p216.tsv`](../../../evidence/person-claims-sweep.2026-10-15-p216.tsv)

## Limits, stated

The sweep is lexical and English/Spanish only. It would not catch a person-level inference phrased
without any of the trigger forms, nor one separated from its absence marker by more than one line.
A limb-2 result here means *no such claim was found by this instrument*, not that none can exist —
which is why the rule, and not the sweep, is the deliverable.
