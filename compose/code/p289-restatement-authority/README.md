# `ACTION p289` — is the payload the **licence**, or the licensee's **restatement** of one?

Built pass 289 (`2026-10-18`). Suite: **40 controls**, in `make hooks`.
Online arm: `probe.sh <slugs-file> <out-dir>`.

## The gap it fills

`p742-grant-body-vs-reference` asks whether a licence file carries a **grant body** or only
a **pointer**. That is the right question and it does not separate two populations that
behave differently for a studio:

| population | what it is | can the repository be checked? |
|---|---|---|
| **self-contained** | the payload **is** the licence — MIT, Apache-2.0, AGPL-3.0. The body travels with the clone | 🟢 yes, from the clone alone |
| **restated** | the payload **paraphrases**, in the licensee's own words, a licence whose authoritative text lives on a **third-party host** | 🔴 no — not without reaching that host |

**Both grade `GRANTED` under `p742`.** Only the first can be verified from the repository.

The second population is exactly where public-sector **curriculum** data lives: OGL v3.0,
the Creative Commons suite, national ministry terms. This is the layer a studio ships when
it sells anything "curriculum-aligned", and it is the layer this base had no verdict for.

## What it found on its first run

`oaknational/oak-curriculum-ontology` publishes the **National Curriculum for England
(2014)** as a machine-readable ontology. Seven payloads over five Oak repositories, every
one read first-hand on an `ls-remote`-resolved ref:

| payload | bytes | classification | attribution | body vs summary |
|---|---|---|---|---|
| `oak-curriculum-ontology` `LICENSE.md` | 1 867 | 🔴 **RESTATEMENT** | 🔴 `DISAGREEMENT` | 🔴 `SUMMARY-REPLACES-PRESCRIBED` |
| `oak-curriculum-ontology` `DATA-LICENSE.md` | 2 408 | 🔴 **RESTATEMENT** | 🔴 `DISAGREEMENT` | 🔴 `SUMMARY-REPLACES-PRESCRIBED` |
| `oak-curriculum-ontology` `CODE-LICENSE.md` | 1 491 | 🟢 AUTHORITATIVE-BODY (MIT) | `SINGLE` | 🟡 `SUMMARY-ADDS-OBLIGATION` |
| `oak-open-curriculum-ecosystem` `LICENCE` | 1 086 | 🟢 AUTHORITATIVE-BODY (MIT) | `NONE` | `NO-SUMMARY` |
| `oak-curriculum-api` `LICENSE` | 1 077 | 🟢 AUTHORITATIVE-BODY (MIT) | `NONE` | `NO-SUMMARY` |
| `oak-ai-plugins` `LICENSE` | 1 085 | 🟢 AUTHORITATIVE-BODY (MIT) | `NONE` | `NO-SUMMARY` |
| `oak-ai-lesson-assistant` `LICENSE` | 1 077 | 🟢 AUTHORITATIVE-BODY (MIT) | `NONE` | `NO-SUMMARY` |

🔵 **The split is the finding: the CODE is verifiable and the DATA is not.** The asset a
studio actually wants — 50 948 key learning points, 11 207 misconceptions, a national
curriculum — sits under the two restated payloads.

## The three defects, each reproducible

**1. `RESTATEMENT` of an authority this environment cannot reach.** Both OGL payloads name
`nationalarchives.gov.uk` as the official text. That host, and **eleven other** national
curriculum hosts, answer `403` to `CONNECT` at the gateway and `NXDOMAIN` to local
resolution — **12/12, zero reachable**, across two independent egress paths, measured in
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../../../evidence/curriculum-authority-egress.2026-10-18-p289.tsv).
So the grant can be **quoted and not checked**. `posture()` returns
`USE-WITH-RECORDED-BOUND` — and returns `VERIFY` for the *same payload* when the authority
is reachable, because the bound is a property of the environment, not of the repository.

**2. `DISAGREEMENT`: one payload, two different required attributions.**
`DATA-LICENSE.md` line 19 prescribes the OGL statement verbatim —

> Contains public sector information licensed under the Open Government Licence v3.0.

— and line 54, in its own summary block, asks instead for

> ⚠️ Must provide attribution: "Oak National Academy"

`LICENSE.md` does the same thing 40 lines apart (L27 prescribed, L67 bare credit).
🔴 **A studio that credits "Oak National Academy" and stops has not met the condition the
same file states above.** These are different obligations and nothing in either payload says
which one discharges it.

**3. `SUMMARY-ADDS-OBLIGATION`, and a self-description that overstates.** `CODE-LICENSE.md`
carries a **verbatim MIT body** whose condition is the copyright-and-permission notice, then
appends a summary asking for a credit string **MIT does not require**. And `LICENSE.md`
advertises `DATA-LICENSE.md` as the *"Full OGL 3.0 License"* when it is a restatement —
`self_description_verdict()` returns `OVERSTATED`.

🔵 All three Oak licence files pair terms with a friendly summary, and **in all three the
summary states the obligation differently from the terms above it.** 3 of 3. A reader who
stops at the summary — which is what a summary is for — discharges the wrong obligation.

## Why the classifier is not OGL-shaped

`p283`'s ratchet rejects an instrument that only works on the axis it was built for, and
this one was built on an OGL fixture. Controls 20-23 therefore run the **same** classifier
over a **Creative Commons** restatement containing no OGL vocabulary, and require that the
two defect shapes stay distinguishable there: `SUMMARY-ADDS-OBLIGATION` when the body
prescribes nothing, `SUMMARY-REPLACES-PRESCRIBED` when it does.

## Failure capability (`p208`)

The suite passed on its first run, which is exactly when a suite must be shown able to fail.
Two seeded mutations of `restatement.py`:

| seed | mutation | result |
|---|---|---|
| 1 | operative-term threshold `>= 2` → `>= 99` | 🔴 **8 controls fail** — every `RESTATEMENT` collapses to `BARE-REFERENCE` |
| 2 | drop the `BARE-CREDIT` detector | 🔴 **9 controls fail** — `DISAGREEMENT` becomes `SINGLE`, `SUMMARY-REPLACES-PRESCRIBED` becomes `ALIGNED` |

Restored, the suite passes again. It also passes under `python3 -I` **from the repository
root** as well as from its own directory — `p355-cwd-portability`'s rule, which is the
reason a working gate used to stay a one-off.

## The bug `set -u` caught in this instrument's own probe

`probe.sh` first wrote its payload captures to `"$OUT/$safe__..."`. Bash parses `$safe__` as
the variable **`safe__`**, not `safe` followed by `__`. Under `set -u` it aborted on the
first repository; without it, **every payload would have been written to the same path and
the last one graded five times** — and the dual-licence split this instrument exists to find
is precisely what that would have erased.

## Reading order for a later pass

`probe.sh` records **every** rung that answers 200, never stopping at the first. A repository
that splits its grant by directory serves more than one payload, and grading it on the first
hit is how a dual-licensed curriculum repo gets filed under its **code** licence while the
**data** it exists to publish sits under another one.
