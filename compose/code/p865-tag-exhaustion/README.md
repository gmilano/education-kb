# `P865` — a channel is exhausted only at the SURFACE that was actually mined

Pass 79 of 2026-10-09.  This directory holds the evidence for the pass's main finding, and it
exists because four consecutive passes recorded "the discovery channel is measured exhausted"
when what was actually exhausted was **one tag**.

## The measurement

Tags this shelf had already bought, counted from `repos/trending.md` + `agents/trending.md`:

    topics/ai-tutor                      9 mentions
    topics/education-ai                  8
    topics/ai-education                  3   (pass 78 — 492 repos)
    topics/edtech|mooc|lti|lms            3 each
    topics/ferpa|ferpa-compliance         3 each
    topics/student-information-system     2
    topics/moodle|e-learning              2 each
    topics/claude-skill|agent-skills      2 each
    topics/intelligent-tutoring-system    0   <-- never mined, in 79 passes

Both were then bought in the same hour, with `WebFetch` (`P855`: `curl` 403s, `WebFetch` 200s):

| surface                                   | rows | shelved | UNSHELVED |
|-------------------------------------------|------|---------|-----------|
| `topics/ai-tutor` (mined 9x)              | 20/660 | 17    | 1         |
| `topics/intelligent-tutoring-system`      | 20/39  | 2     | **5**     |
| `search?q=AI+tutor+agent+education`       | 10/157 | 8     | 2         |

**Tag SIZE did not predict yield; prior-sweep status did.**  The 39-repo tag beat the
660-repo tag by 5 to 1.

## `P428` — the census moment is labelled, because this pass changes its own corpus

* `PRE`-write (the denominator the discovery decision was made on): **7 unshelved candidates**
  across the three surfaces, 0 of them named anywhere in the tree at `4a2853f`.
* `POST`-write (the state the tree is left in): **7 shelved or refused**, all 7 now named — by
  this file among others.

A later pass re-running the same tags will read these 7 as SHELVED.  That is correct and is not
contamination; what would be wrong is publishing a single unlabelled number.

## Files

* `payloads.2026-10-09-p79.tsv` — every grant read this pass, with branch, SHA, bytes, family
  and verdict.  Family is a **human read of the payload head**, not a classifier result: `P866`
  blocked execution and `P126` forbids re-implementing `license_family.sh`.
* `candidates.input.2026-10-09-p79.tsv` — the candidate set as discovered, before probing.

## What this directory does NOT contain

No runnable instrument.  `P866`: this pass could not execute code from the clone **or a script
of its own** — only inline commands.  Writing an instrument here that was never run would
violate `P126`.  The next pass with execution restored should fold this TSV into
`shelf_gate.sh`'s inputs and add the lowercase `PROBE_NAMES` fix that `P862` already names.
