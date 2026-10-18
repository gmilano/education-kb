# `p279-absence-claims` — the absence gate, because `make claims` was an instruction

## Why this exists

`p278`'s headline was **a gate that exists and was not run.**

`p277` ranked *"build the payload-vs-metadata CONFLICT class"* **first, at zero searches**, on the
stated ground that *"this base has a grade for payload and a grade for metadata and **no class at all
for CONFLICT**"*. `p121` had built that class on 2026-10-11 — 249 addresses, 161 manifests, 10
contradictions — and the instance `p277` reported as NEW was **row 8 of `p121`'s own published
table**.

`make claims TOKEN=conflict` answers `ALREADY CLAIMED … STOP` over **26 cells** and exits 1. The
Makefile documents that recipe as *"THE GATE: run before publishing any 'there is no X'"*. Nobody ran
it. So `p278` registered the remedy as: **"the next pass should not be able to publish an absence
without it having run."**

And *"read more carefully"* is not that remedy. `p121`'s class lives in `repos/trending.md` while
`p277` was working in `agents/top.md` and `intel/open-gaps.md`. **On ten shelves and 28,000+ lines,
care does not substitute for running the index.**

## The predicate

> an ABSENCE PHRASE from the vocabulary, followed by a DISTINCTIVE SUBJECT TOKEN (backticked,
> ALL-CAPS, or slug-shaped) that `carried_index.claims()` already finds on the shelves

Subjects are **distinctive** rather than every noun, because the subjects this base writes absences
about are written as `CONFLICT`, `MCP`, `AGPL`, `` `gegok12` ``. Testing every word would report
`education` and `licence` as "already claimed" on every line of the corpus, and the gate would be
noise within one pass. A narrow gate that fires beats a broad one that gets ignored.

## Polarity, copied from `gate-enumeration`

| verdict | meaning | fatal? |
|---|---|---|
| `REFUTED` | an absence this text **asserts**, whose subject the shelves already claim | 🔴 **yes** |
| `QUEUE` | absence prose with no resolvable subject — the backlog | no |
| `QUOTED` | an absence this text **reports** (quoting another pass or a source) | no, but always **printed** |

## Scope — the one judgement call, stated plainly

The fatal arm reads the **newest `## Pass` section of `README.md`**: the pass being written now. The
shelves carry hundreds of historical absence sentences, each already adjudicated by the pass that
wrote it, and failing on those would make `make hooks` red on arrival — so the gate would be disabled
within a pass. `--census` reads everything and never fails (**124 refuted / 239 queued** at p279).

## Two predicates that were wrong before it was wired in

Both measured on the real `README.md` rather than reasoned about:

1. 🔴 It reported `p278`'s forensic **quotation** of `p277` as a fresh assertion. A gate that cannot
   tell an assertion from a report would punish the write-up this base is built on. The distinction
   already existed one subject over, in `p223`'s date gate (`QUOTED` *"because the KB reporting what a
   source said is evidence, not a defect"*) — cited, not reinvented.
2. 🔴 The first fix computed quote parity **per line**, and still failed, because the real sentence
   **wraps**: the opening `*"` sits on the line above the absence phrase. That is `p278`'s own
   reflow-brittleness class one layer out. Quote state is tracked across the **paragraph** now, and
   the real wrapped text is a control.

## Running it

```bash
make gate-absence        # in `make hooks`: the live pass section, fatal
make absence-census      # whole corpus, a measurement, never fatal
```

## Controls

`test_absence_claims.py`. **Control Zero is `p277`'s verbatim sentence**, over a fixture carrying
`p121`'s real claim, asserting the real verdict — a gate built from a historical defect that cannot
reproduce that defect is a gate built from a story. Every shape that broke a draft is a control, so a
later pass widening the predicate detonates on these instead of on the shelves.
