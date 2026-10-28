# `p499` — retained canonical licence set + operative-span grader

Closes **`Gap 498-B`** (*"no retained canonical licence set exists on this base"*) and answers
**`Gap 488-T`** (*"the sector-wide operative-body edit rate is still unmeasured"*).

## Why bytes and blob SHAs do not work

`Gap 498-B` proposed storing canonical payloads **by blob SHA**. The set itself disproves the key:

| canonical form | bytes | git blob SHA-1 | operative words |
|---|---|---|---|
| `Apache-2.0.apache-org` (apache.org's own) | 11 358 | `d645695673349e3947e8e5ae42332d0ac3164cd7` | 1 426 |
| `Apache-2.0` (SPDX's) | 10 280 | `137069b823873b8bcf42979bcf8e9371052d26a2` | 1 426 |

Two *legitimate* canonical forms of the same licence. Different bytes, different blob SHA, **not one
different word** — the delta is entirely apache.org's centering whitespace. A blob-SHA allowlist
would reject correctly-licensed repositories, and byte size (which `p498` reasoned from) has no
discriminating power at all.

So the grader normalises whitespace and compares the **word sequence of the operative span**.

## What the operative span excludes, and why

Two regions of a payload are **fill-in-the-blank by instruction** and must not be graded:

1. **The appendix** — Apache-2.0's *"APPENDIX: How to apply the Apache License"* and the GNU
   family's *"How to Apply These Terms to Your New Programs"*. Replacing `yyyy`/`name of copyright
   owner` there is what the licence tells the licensor to do.
2. **Copyright notice lines** — MIT/BSD/ISC carry no appendix; their placeholder is the notice line
   itself, inside the body.

Grading these conflates an instructed fill with an alteration. **41 of 64** rows swept are in
exactly that position, so a whole-payload gate raises 41 false alarms and buries the real finding.

## The notice-line rule, and two wrong versions of it

A notice line must carry **either** an explicit `(c)`/`©` marker **or** a year/placeholder. Both
looser forms were tried first and both silently deleted operative text:

| form | what it deleted | how it was caught |
|---|---|---|
| any line beginning `copyright` | GPL-3.0 §2's *"…for the term of copyright on the Program, and are irrevocable…"* | a uniform **−22-word "deletion" across 14 independent GPL/AGPL projects**. Fourteen projects do not make the same edit. |
| also accept a bare word after `copyright` (to catch `Copyright (c) Microsoft Corporation.`, which has no year) | GPL-2.0 §1's wrapped *"copyright notice and disclaimer of warranty; keep intact all the"* | `formalms` §1 read **word-for-word canonical** when fetched and diffed by hand |

**Neither error was visible in the instrument's own output.** A plausible number is the expected
output of a broken instrument — which is why `Gap 498-M` requires a known-good *and* a known-bad
control before any gate is trusted.

## Controls (re-run these before trusting a change)

```sh
CANON_DIR=evidence/canonical python3 -I compose/code/p499-canonical-set/grade_licence.py <payloads...>
```

| input | expected |
|---|---|
| `beltromatti/get-it` `LICENSE` | 🔴 **DEVIANT, −5 words**: `reasonable and customary use in` (an Apache §6 trademark-clause deletion) |
| `huggingface/smolagents` `LICENSE` | 🟢 **IDENTICAL** |
| `menthorlabs/menthor` `LICENSE` | 🟢 operative **IDENTICAL**, whole payload deviant (placeholder filled) |
| `formalms` `html/license.txt` | 🟡 **DEVIANT, −2/+6** — 1991-vintage FSF transcription only |

`get-it` is the known-bad: `p498` found its deletion only by comparing two Apache payloads that
happened to land in the same pass. This instrument recovers it **from the payload alone**.

## Usage

```sh
# list the retained set with bytes, blob SHA and word counts
CANON_DIR=evidence/canonical python3 -I grade_licence.py

# grade payloads
CANON_DIR=evidence/canonical python3 -I grade_licence.py path/to/LICENSE ...

# sweep a grant-path census; asserts output rows == input rows (Gap 498-L)
CANON_DIR=evidence/canonical python3 -I sweep_operative.py \
    evidence/grant-paths.2026-10-28-p498.tsv out.tsv
```

## Known limits

- **`Gap 499-B`** — 12 payloads, and **no "unknown licence" verdict**. A licence outside the set
  (e.g. `CERN-OHL-S-2.0`) gets a meaningless nearest-neighbour label instead of an abstention.
- **`Gap 499-C`** — GNU canonicals are **single-sourced from SPDX**; `www.gnu.org` does not resolve
  through this session's network policy. Only Apache-2.0 is two-sourced.
- **`Gap 499-D`** — SPDX payloads are pinned at commit `f715b366` and **nothing re-resolves them**.
- **`Gap 499-E`** — the appendix cut uses three literal markers; a renamed appendix heading is not cut.
- **`Gap 499-F`** — `closest canonical` is a **nearest-neighbour by edit distance, not a licence
  identification**. On a short pointer file it picks `MIT` spuriously. The four-class
  interpretation of a deviation is **not implemented** and was done by hand.
- **`T21`** — a pointer grant (19–121 bytes, no licence text) is graded rather than refused.
