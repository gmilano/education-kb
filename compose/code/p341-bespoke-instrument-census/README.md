---
industry: education
region: Global
updated: 2026-10-20
---

# `p341-bespoke-instrument-census` — T29's open question, with a denominator

**Pass 341 · 2026-10-20 · `python3 -I test_bespoke_census.py` → 34/34, fully offline.**
Wired standing as `gate-bespoke-title`. Inherited gate state before a byte changed:
🟢 `make hooks` **23/23 green, exit 0**, `make gate-offline` green, `make recount`
MATCH on all five registered claims.

## What it closes

`p340` recorded, verbatim:

> 🟡 **Open question nobody has measured: how many `LICENSE*` payloads on these
> shelves are bespoke instruments rather than stock texts?** `p1054-mit-plus-clause`
> exists for the added-restriction case; **the fully-bespoke case has no census.**

**Answer, over 208 payloads read first-hand from the four live decision shelves
(`agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`,
`compose/patterns.md`):**

| title form | n | share |
|---|---|---|
| `SPDX-TITLED` | 183 | 88.0 % |
| `UNTITLED` | 15 | 7.2 % |
| `BESPOKE-TITLED` | 10 | 4.8 % |

**181 of 208 (87.0 %) are stock texts. 16 of 208 (7.7 %) carry an instrument a
human must read.** Evidence:
[`p341-bespoke-instrument-census`](../../../evidence/p341-bespoke-instrument-census.2026-10-20-p341.tsv)
(208 graded rows) ·
[`p341-payload-locate`](../../../evidence/p341-payload-locate.2026-10-20-p341.tsv)
(237 probe rows).

## 🟢 The result that matters most is a negative one

**Every one of the 16 is ALREADY LABELLED CORRECTLY on the live shelves.** Checked
cell by cell: `caviraoss/pagelm` already reads *"CaviraOSS Community Licence" — NOT
open source*; `canyongbs/advisingapp` already reads *Elastic Licence 2.0 —
source-available, not OSI*; `haolpku/k12-kgraph` already splits *MIT (code) /
CC BY-NC-SA 4.0 (data)* and quotes the README verbatim.

🔵 **So the bespoke class was never an unmeasured exposure — it was measured
row-by-row, in prose, by earlier passes, and never counted.** What this census
adds is the denominator, the named population and a standing gate; it corrects **no
published cell**. Stating that plainly is the point: a census that finds nothing
wrong is worth exactly its denominator, and reporting it as a save would be false.

## 🔴 What it found that nobody had measured

### 1. A carried "verify" row RESOLVED — and the reason it was never resolvable

`portabilis/i-diario` carried the shelf cell *"A LICENSE file exists but the page
does not name the licence — **read the file before any use**."* This pass read it:
branch `1.6`, `LICENSE`, **35 326 B**, opening
**`LICENÇA PÚBLICA GERAL AFFERO GNU · Versão 3, 19 de novembro de 2007`** — eight
lines naming Affero, FSF copyright on the licence text. **It is `AGPL-3.0`.**

🔴 **It was not neglected. It was unresolvable with this base's instruments.**
Both shared family classifiers return nothing on it:

| channel | verdict on `i-diario` |
|---|---|
| `pass257.family_of` | `None` → `UNCLASSIFIED:no-family-no-restriction` |
| `lib/license_family.sh` `family_of` | `UNCLASSIFIED` |

🔴 **And that verdict string fails UNSAFE.** `no-family-no-restriction` reads as
*nothing found* on the strongest copyleft in this corpus. AGPL restricts by
reciprocity, not by commercial field-of-use, so the restriction axis is silent by
construction — the quiet is a property of the instrument, not of the licence.
🔵 Opposite direction from `p314`'s abstention class, which fails safe.

🟢 **Consequential, not bookkeeping:** its sibling `portabilis/i-educar` is
`GPL-2.0` (18 092 B, English, read the same hour). A Brazilian municipal stack
therefore carries **network copyleft on the teacher-facing portal and ordinary
copyleft on the SIS core** — a deployment-shaping difference that was invisible
while the row said "verify".

### 2. The asymmetry that caused it, with a denominator

`pass257` carries a restriction vocabulary in **11 languages**
(`de en es fr id it ja ko pt vi zh`) and `language_of` types `i-diario` as `pt`
with `vocabulary_covers_language=True`. 🔴 **But `TITLE_ANCHORS` and
`BODY_ANCHORS` are English-only**, so the FAMILY question has no Portuguese rung
at all. The multilingual work `p240`/`p241` paid for reached the restriction axis
and never reached the family axis beside it.

**Measured population: 3 of 208 payloads (1.4 %) are non-English — all three
Portuguese, all three Brazilian.** `license_family.sh` recovers 2 of the 3
(`bncc-dev/bncc-benchmark`, `bncc-dev/bncc-pacotes` → `CC-BY-4.0`) and misses the
third. Evidence:
[`p341-nonenglish-payload-blindness`](../../../evidence/p341-nonenglish-payload-blindness.2026-10-20-p341.tsv).

🔵 **This is the LATAM finding this base has lacked for five passes, and it is not
a supply gap.** p340 concluded *"LATAM institutions run these platforms and
connectors to them are not being published."* That holds for connectors. For
platforms the constraint measured here is different: **the supply exists, is
large, and this base cannot read its licences.**

### 3. Two shared classifiers disagree on the most education-specific family there is

| payload | `license_family.sh` | `pass257.family_of` |
|---|---|---|
| `opencast/opencast` (11 340 B) | 🟢 `ECL-2.0` | 🔴 `None` |
| `sakaiproject/sakai` (11 120 B) | 🟢 `ECL-2.0` | 🔴 `None` |

`pass257.TITLE_ANCHORS` holds `eclipse public license → EPL` and **no rung for the
Educational Community License**, which is the Apache-2.0-derived grant Sakai and
Apereo ship under and the one licence family named for this industry. 🟢 **The
shelves are right** (17 `ECL-2.0` cells across `repos/foundations.md` and
`verticals/solutions.md`) **because `probe_repo` uses the classifier that gets it
right.** `p278`'s channel-conflict class, between two instruments in one `lib`.

## 🟡 The finding this pass withdrew, and why it is recorded anyway

The census flags **4 of 6 BSD-family payloads** `FAMILY-PLUS-RESTRICTION:needs-a-human`
whose **only** effective hit is `all rights reserved` — the canonical second line of
every stock `BSD-2-Clause` and `BSD-3-Clause` text. All four verbatim stock, one
(`open-tutorai/open-tutor-ai-ce`) foundation-tier. Evidence:
[`p341-bsd-boilerplate-cost`](../../../evidence/p341-bsd-boilerplate-cost.2026-10-20-p341.tsv).

🔴 **This pass drafted a one-line fix — `"BSD": frozenset({"all rights reserved"})`
in `BENIGN_FAMILY_HITS` — applied it, and `pass257`'s own suite went 127/129.** The
two failing controls are at `test_restriction_scan.py:179-181`, and their comment
reads:

> 🔴 …and that payload carries `all rights reserved`, which is in the vocabulary.
> **A real BSD grant says that phrase benignly, so the verdict must name a human
> rather than either publishing it as permissive or burying the hit.**

🟢 **`p257` knew. It chose.** The patch was **reverted**; `pass257` is byte-identical
to `HEAD` and back to 129/129. 🔵 **Sixth instance of the class `p333` named and
`p340` counted five of — except one degree worse: there a capability was present and
nearly re-derived as news, here a DECISION was present, documented in the suite that
guards it, and nearly overturned as a defect.** The guard that caught it was running
the suite, not reading it.

🟢 **What survives is the price tag, which `p257` could not have known and nobody has
measured since: the conservative choice costs 4 of 208 live rows (1.9 %), one of
them foundation-tier.**

🟡 **Prescription, measured not proposed — and it is NOT the reverted patch.** The
phrase in all 4 rows sits in the *canonical BSD position*: on the line directly
after a copyright declaration and before `Redistribution and use in source and
binary forms`. A **positional** rung preserves `p257`'s safety property exactly —
it buries nothing and exempts nothing — and over this corpus it clears all 4 with
**0 false clears**: the only other payloads carrying the phrase are
`asthetech/mewcp-google-classroom` (6 other hits) and `mikeargento/sealed-exam`
(MIT + `commercial use`, a vendored bundle), and both keep failing. 🔴 **Its
falsifier, named so the next pass can refuse it cheaply: find one payload whose
canonical-position `all rights reserved` is NOT boilerplate.** Until that is run,
this is a prescription and the 4 rows stay flagged.

## Why the title form, and not `p312.identify`

🔴 Reading `p312`'s `UNKNOWN-TEMPLATE` as "bespoke" would report most of this
corpus bespoke: its registry is **derived from its own fixtures**, so verbatim
`Apache-2.0` (11 356 B) and verbatim `GPL-3.0` (35 146 B) both return
`UNKNOWN-TEMPLATE` while being unimpeachably stock. That is `p310`'s byte-band
error in a new costume. Pinned in `TestP312IsNotABespokeDetector`, whose own first
draft asked `p312` about `p312`'s fixtures, measured the tautology, and failed on
the first run — which is the only reason the control is right now.

## Vocabulary

    SPDX-TITLED      a title-shaped leading line names a family in `pass257.TITLE_ANCHORS`
    BESPOKE-TITLED   a title-shaped leading line calls itself a licence and names no family
    UNTITLED         no instrument-naming title line at all (`p314`'s class)

🔴 `UNTITLED` is deliberately NOT merged into `BESPOKE-TITLED`. `p314` measured
complete stock `MIT` grants whose title line is simply absent
(`Priyamakeshwari/TeachGPT`, 1 057 B, cited in `pass257`'s own `BODY_ANCHORS`
comment). An untitled stock grant and a bespoke instrument are opposite findings
and a census that fuses them answers nothing — asserted in
`TestTheUntitledClassIsNotTheBespokeClass`.

**A title is short.** `TITLE_MAX_BYTES = 60`. The first draft tested bare
`agreement` over `pass257`'s 4-line window and typed `usc-academic-1812`
`BESPOKE-TITLED` off its body prose *"without a written agreement is hereby
granted"*. Both halves of the repair — dropping bare `agreement`, and requiring a
title-shaped line — are pinned in `TestTheTitleShapeRepair`, including that the
row is **still** sent to a human through its restriction hits. 🔵 Only the REASON
changed, which is what keeping the limbs separate buys.

## Running it

    python3 -I test_bespoke_census.py                     # 34/34, offline, no clock
    make gate-bespoke-title                               # the same suite, wired
    python3 -I bespoke_census.py PAYLOAD [PAYLOAD ...]    # grade files, offline
    JOBS=10 bash probe.sh SLUGFILE OUTDIR                 # the ONLINE limb

🔵 `probe.sh` sources `lib/probe_payload.sh` and contains **no probe loop**. That
file's header records two passes that rewrote the loop by hand and published wrong
families from it; `p341` is not the third. Grading is offline over the cache, so a
re-grade never re-spends the network.

🟢 **The case-varied ladder `p336`/`p337` bought paid out again, unprompted:** of
208 located payloads, **6** sit at spellings an all-uppercase ladder would have
missed — `license.txt` ×3, `license.md`, `LICENCE.md`, and `docs/License.txt`.

## Scope — what this instrument does NOT answer

A payload answers the **copyright** question only. Whether a component may be
**called** is `P26`'s access-rights question, lives in a third party's Terms of
Use, and is invisible here — `lib/probe_payload.sh` states the same limit and it is
restated rather than assumed. 🔴 A 404 body served with `200` is `p1058`'s class,
not this one; the census takes its population from `probe_repo`, which never
returns a non-200 body as a payload.
