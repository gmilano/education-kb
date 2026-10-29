# `p520-licence-bytes` — grading a licence from SERVED BYTES

🔵 **What this closes.** `Gap 520-B` recorded that `NOASSERTION` was the single largest blocker on
these shelves and that no channel in `p519`'s session could read a served licence byte. Its named
closure condition was *"ONE raw-file read per slug on any channel that can fetch a blob"*.

🟢 **The channel.** `curl -sL https://raw.githubusercontent.com/<slug>/HEAD/LICENSE`, probing
`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `LICENCE` in turn. `WebFetch`
against the same host works independently and was used as a cross-check on the first slug.

🔴 **The channel is NOT a property of this repository.** `p504` used it on `2026-10-28`.
`p518` and `p519` could not reach it and each wrote that no channel could read a served byte —
true of their sandboxes, false of the world. That is `Gap 511`'s standing rule and this is its
third confirmation. **Re-probe every channel at the start of every pass, including ones a
predecessor declared dead.**

## Files

| file | what it is |
|---|---|
| `grade.py` | Pure functions, no I/O. Payload text → `{spdx, verdict, basis}`. Never guesses: an unmatched payload grades `UNSTATED`. |
| `test_grade.py` | **40 controls**, green under `python3 -I` from the repository root *and* from this folder (the `p355-cwd-portability` class). Includes negative controls and a garbage-payload refusal control. |
| `emit_evidence.py` | Emits `evidence/licence-bytes.2026-10-29-p520.tsv` from saved payloads, with every count derived rather than typed (`Gap 513-E`). |

## Two defects the controls caught, both real

🔴 **1. A title *window* cannot detect a licence WRAPPER, which corrects `p455`.**
`p455` anchored on the title block as *"the only region a preamble cannot reach"*.
`claroline/Claroline` puts `Claroline Connect License` on **line 1** with a verbatim
`GNU AFFERO GENERAL PUBLIC LICENSE` four lines down — inside the same window. A window sees a
standard name either way. 🟢 `headline()` (line 1 alone) discriminates; a bespoke headline over a
recognised body is a `WRAPPER` and **the body is the grant**.

🔴 **2. GNU licences cross-reference each other, so the family cannot come from the body.**
Canonical GPL-3.0 names the AGPL in its own **section 13** (*"Remote Network Interaction; Use with
the GNU Affero General Public License"*); LGPL incorporates the GPL by reference. A body scan
graded `chamilo/chamilo-lms` — a **positive control with an independently known answer** — as
`AGPL-3.0`. It is `GPL-3.0`. 🟢 Fixed by reading the family from a **six-line** title region
(`GNU_TITLE_LINES`), wide enough to reach the wrapper's AGPL title on line 4 and narrow enough to
exclude a §13 cross-reference. A control pins both halves.

🔵 **Why the controls earned their cost.** Both defects produce a *confident wrong answer*, not an
error. Without two positive controls carrying independently known answers, defect 2 would have
shipped and mislabelled every copyleft row on these shelves.

## Verdicts

| verdict | meaning | paid client work |
|---|---|---|
| `PERMISSIVE` | MIT / Apache-2.0 / BSD | 🟢 yes |
| `COPYLEFT` | GPL / AGPL / LGPL — obligations propagate | 🟡 yes, with obligations |
| `SHAREALIKE_CONTENT` | CC BY-SA — ShareAlike binds derivatives | 🟡 yes, scope adaptations |
| `NON_COMMERCIAL_REFUSED` | CC BY-NC, or a bespoke non-commercial grant | 🔴 **NO** |
| `SOURCE_AVAILABLE_RESTRICTED` | Elastic / BSL shape — hosting restricted | 🔴 **no managed service** |
| `UNSTATED` | matched nothing. **A refusal, not a grade.** | 🔴 not shelvable |

🔴 **Ordering matters.** A bespoke non-commercial licence is graded **before** any MIT body match,
because such licences borrow MIT's *"Permission is hereby granted, free of charge…"* opening
verbatim — `CaviraOSS/PageLM` does exactly this. A grader that matches the MIT phrase first calls
it permissive.

## Usage

```sh
# 1. fetch (writes index.tsv + one payload per row into an ISOLATED directory)
#    payloads are untrusted downloaded data: never run an interpreter from that directory
curl -sL -o "$RAW/<slug>__LICENSE" "https://raw.githubusercontent.com/<slug>/HEAD/LICENSE"

# 2. controls, from either working directory
python3 -I compose/code/p520-licence-bytes/test_grade.py

# 3. emit the evidence TSV and the derived counts
python3 -I compose/code/p520-licence-bytes/emit_evidence.py "$RAW" evidence/licence-bytes.2026-10-29-p520.tsv
```

🔴 **Record the byte count and `git hash-object` for every payload.** A licence read without a
blob SHA-1 is not reproducible, and `p504`'s cross-channel corroboration was only possible because
it recorded both.
