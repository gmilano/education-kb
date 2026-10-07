---
industry: education
region: Global
updated: 2026-10-07
---

# `p550` — duplicate-definition sweep, and the inversion oracle that prices it

**Pass 45, 2026-10-07.** Closes nothing on its own; it reports a failure class this KB had not
looked for, and the first run found an instance in the one file every other instrument is told to
reuse.

## What it found

`lib/license_family.sh` — the shared hardened licence classifier, whose own header says *"source
this, do not rewrite it"* — defined **`commercial_use_ok()` twice**:

* line 429: the **pass-82 first cut**, a pure token-match over the payload body with **no family gate**;
* line 455: the hardened `P299`/`P312` body.

Bash keeps the **last** definition, so the hardened body is the one that ran and **no verdict this
KB has published was ever wrong**. But it was correct *by source order*, and source order is not a
control. The detail worth keeping: the comment block explaining why the first cut was wrong sits
**between the two definitions**. The fix had been **appended, not substituted**.

The duplicate is also present in the frozen `../p308-phrase-anchor-sweep/license_family.PRE-P308-CONTROL-2026-10-04.sh`
snapshot, so it predates **2026-10-04** and survived every `132/132` run since.

## What it would have cost — `oracle_inversion.sh`

The sweep proves a divergent shadow exists. The oracle measures what it would cost, which is the
difference between "dead code, tidy it up" and "the shelf's verdicts depend on source order". It
binds the shadowed body under a second name and runs **both** over this KB's own licence payloads —
no synthetic fixtures, because the question is what happens to *this* shelf.

| | Result (pre-fix) |
|---|---|
| Payloads judged | **27** |
| Verdicts that invert | **7** |
| Direction | **uniform** `ALLOWED` → `PROHIBITED` |
| `CC-BY-NC-4.0` control | `PROHIBITED` under both — the NC case does not move |

The seven: `openemis-core` (GPL-2.0), `kuali/kfs` (AGPL-3.0), `Ovsyanka83/autograder` (GPL-3.0),
`INGInious` (AGPL-3.0), `FWU-DE/mem-mcp` (**Unlicense**), `classroomio` (AGPL-3.0), `lmscloud`
(GPL-3.0).

All seven **over**-restrict. That is `P308`'s direction (lose shelf, cost an opportunity), not
`P312`'s (invent permission, cost the deliverable) — which is why the remedy is a cleanup and not a
recall of published rows. `result-inversion.2026-10-07.tsv` is the **pre-fix** measurement and is
kept as the record; against the repaired library the oracle now answers `SHADOW-ABSENT`.

## Files

| File | What it is |
|---|---|
| `sweep_dupdefs.sh` | the sweep. `<root>...`, scans `*.sh` and `*.py`. Exit `0` clean, `1` findings, **`2` refused** |
| `strip_quoted.awk` | blanks heredoc bodies and triple-quoted strings before scanning (`P550c`) |
| `oracle_inversion.sh` | `<license_family.sh> <corpus-root>` — measures the divergence over real payloads |
| `test_sweep.sh` | the suite: **26/26**, 4 mutants, offline, no network, no clone |
| `result.2026-10-07.tsv` | the sweep over `compose/code/` **after** the repair: 0 divergent |
| `result-inversion.2026-10-07.tsv` | the oracle's **pre-fix** measurement — the evidence, kept deliberately |

## Classes it reports, and the two it refuses to inflate

| Class | Meaning |
|---|---|
| `P550-SHADOWED-DIVERGENT` | **the finding** — two definitions, bodies differ, one is dead and the live one wins only by order |
| `P550-REDUNDANT-IDENTICAL` | byte-identical re-declaration: redundant, **not dangerous**, and not counted as a finding |
| `P550-FROZEN-CONTROL` | a declared snapshot (`*PRE-P*-CONTROL-*`, `*.frozen.*`) that inherited a duplicate from the file it snapshots — **declared, not accused**: reproducing old behaviour is its job |

## Two defects this instrument found in itself, both before publishing

**`P550b` — a private counter beside the published table.** The first cut kept `findings` as a
variable incremented during the scan. Two mutants walked through the suite (drop the increment;
force the final test `true`) because both leave the **rows correct** and only the **exit status**
lies — `P541`'s shape inside the instrument written to find `P541`'s cousin. Fixed by construction:
the status is now recomputed **from the emitted rows**, so there is no second number to drift, and
the suite asserts on the **table**.

Declared asymmetry, because it is the honest statement of what this instrument guarantees: **the
exit code is a convenience, the table is the evidence.**

**`P550c` — three definitions reported that do not exist.** `f`, `g` and `k`: fixture source quoted
inside heredocs in this sweep's **own suite**. A scanner that cannot tell a definition from a string
containing one **over-accuses**, which is `P543`'s error class. Fixed with `strip_quoted.awk` and
tested in **both** directions — a quoted definition must not be reported, and a real duplicate
*after* a heredoc must still be.

## Running it

```sh
./sweep_dupdefs.sh /path/to/tree                  # 0 clean · 1 findings · 2 refused
./oracle_inversion.sh ../lib/license_family.sh .. # SHADOW-ABSENT once repaired
./test_sweep.sh                                   # 26/26
```

`P542`'s lesson is applied to both instruments rather than described: invoked with no arguments, or
pointed at a root holding no source file / no licence payload, each exits **`2`** and judges nothing,
so "0 findings" can never be a reading of an empty run. The suite asserts all four refusals.

## The lesson meant to travel

When a pass fixes an instrument, **delete** the old implementation. Keeping the explanation as a
comment is right; keeping the **code** is the defect. A suite calls a *name*; the name resolves to
*one* body; a green tally says nothing whatsoever about the body that did not resolve.
