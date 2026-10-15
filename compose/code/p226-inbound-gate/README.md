# `p226-inbound-gate` — the refuted-claims gate, moved from OUTBOUND prose to INBOUND results

**`ACTION SH`, p226's registered highest priority.** Stdlib only. No requests. Runs on text the
pass already has.

## Why it exists

`ACTION SA` (p223/p224) built a `(subject, refuted-claim, correction)` table and ran it over this
KB's own published prose. It reported `0 ASSERTED / 5 ATTRIBUTED` at p224 and again at p225 — and
a `0/0` report reads like a solved problem.

p225 showed it is not. Both refuted claims came back **inbound**, through the mandated regional
query itself, carried by sources that had never been cited here. The outbound gate stops this KB
re-asserting a refuted claim. It does nothing about the claim still being in circulation and being
handed back by every search.

This instrument runs the **same table and the same regexes one step earlier**: against a pass's
raw search results, before anything is written to a shelf.

## Usage

```sh
python3 -I inbound_gate.py ../../../evidence/sh-refuted-claims.2026-10-15-p226.tsv p226-raw-results.txt
python3 -I test_inbound_gate.py        # 13 controls
```

Capture raw results into a file whose query blocks are delimited by `=====QUERY: <verbatim query>`.
That delimiter also satisfies `ACTION RE` — the verbatim query travels with the text it returned.

## The firing rule, and why the unit is the LINE

A row fires when, **within one record**, `subject_pattern` matches **and** `refuted_pattern`
matches **and** `exempt_pattern` does not.

The conjunction is load-bearing. `subject_pattern` alone is far too broad — every AI Act paragraph
says "high-risk". `refuted_pattern` alone would fire on unrelated August-2026 prose.

**One record is one line.** A whole-block unit would let a subject in paragraph 1 pair with an
unrelated date in paragraph 9 — the exact `ENTITY-grep → AXIS-claim` inference `ACTION QY` tracks.
There is a control for it (`test_subject_and_date_in_DIFFERENT_records_do_not_pair`).

## What p226 measured with it

| | |
|---|---|
| inbound records scanned | `76` |
| **inbound hits** | **`0`** |
| near misses reported | `1` |
| p225's 2 inbound strings vs the **3**-row p224 table | **`1` of `2`** caught |
| p225's 2 inbound strings vs the **4**-row p226 table | **`2` of `2`** caught |

The binding constraint was never sensitivity — the EU regex fired correctly both times. It was
**coverage**: there was no Boston subject in the table for the gate to fire on. p225 caught that
claim by a human read and wrote it down; nobody extended the table. p226 added the row.

## The near miss, and why widening the regex would be a mistake

```
EU AI Act: Sources agree it treats education AI as high-risk ... One source says it entered
into force in August 2024, and its general application date was 2 August 2026.
```

Subject matched; `refuted_pattern` did not; the gate correctly stayed silent. **"General
application date 2 August 2026" is true of the AI Act as a whole.** The refuted claim —
*education high-risk obligations take effect August 2026* — carries the **same date** and differs
only in the **obligation**.

So widening `refuted_pattern` to catch "general application" would make the gate fire on a true
statement. The unit of this refuted claim is the `(OBLIGATION, DATE)` pair, never the date alone.

A gate that reports only its own firings cannot tell a clean pass from a blind spot, which is why
`scan()` returns near misses as a second channel and the runner prints them.

## Controls

`13` tests, `13` passing.

- **MUST FIRE** — p225's EU string; p225's Boston string under the extended table.
- **MUST NOT FIRE** — this pass's EMEA near miss; the Vietnam high-risk / March-2026 line; the KB's
  own published correct form for both subjects; a bare date with no subject; a bare subject with
  no date; a subject and a date in two different records.

## Wiring it into `make hooks`

This is the inbound half of `ACTION QO`'s gate. See [`compose/patterns.md`](../../patterns.md)
`P226-R1` for the full recipe alongside `P222-R3` (bounds) and `P225-R1` (aliases).
