---
industry: education
region: Global
updated: 2026-10-19
---

# `p311-template-identity` — `ACTION p310-R` item 1

**Pass 311 — 2026-10-19.** `python3 test_template_identity.py` — **80 passed / 0 failed**,
fully offline, no network and no clock. Wired standing as `gate-template-identity`;
**20/20 gates green** at publication.

## The one-line version

🔴 **MIT and Apache-2.0 are the two most-published licence families on this base — `5 558` and
`2 335` cells, `7 893` between them — and no dynamic arm had ever run a single classifier
against either one's real legalcode.** 🟢 **Run here on eleven first-hand payloads against all
nine declared classifiers: `36` CORRECT, `6` COARSE, `6` ABSTAIN, `6` OUT-OF-DOMAIN,
**`0` DEFECT**.** 🔵 **The exposure `p310` called *"the single highest-value hour available"* is
retired with a measured negative result — and the hour paid for something better than a verdict.**

## The finding: a byte band cannot identify MIT, and no correction can fix that

`intel/open-gaps.md` carries MIT `1 062`–`1 074` as a **discharged** falsifier. `T184` corrected
three such bands and recorded that *"every correction makes the test WORSE."* 🟢 **`T184` was
right and did not say why. The reason is structural:**

> **MIT's payload length is `constant(template) + len(copyright line)`.**

The copyright line carries a **free variable** — the holder's name — so a band measures *whose*
repositories were sampled, not the licence. Measured over **eight** payloads from eight unrelated
repositories, five countries, 2020–2026:

| | |
|---|---|
| observed lengths | **`1 061` – `1 086`** — breaks the published band at **both** ends |
| normalise the declaration, then hash | 🟢 **seven of eight collapse to ONE digest** `16d6b7b5799875f6` |
| `bytes - len(declaration)` on those seven | 🟢 **`1 038`, exactly, all seven** |
| the eighth | 🟢 **a SECOND TEMPLATE, not a defect** — titled `The MIT License (MIT)`, own constant **`1 047`**, digest `d936246a542832f3` |

🔵 **Two templates cover 8 of 8.** So the family's honest shape is a small discrete set of
templates, each with an exact constant — and the instrument that matches it returns
`UNKNOWN-TEMPLATE` for anything unseen. **A band always answers, and at the edges it answers
wrongly and silently.** That is the whole behavioural difference, and it is `P250`'s
reported-vs-realised distinction applied to identity instead of to commercial use.

## Fixed-document families are a different problem and must not share the rung

Apache-2.0 has no holder slot, so normalisation is the identity function and its two observed
lengths are not holder variation at all. Measured first-hand:

| | |
|---|---|
| `10 173` B vs `11 357` B | 🟢 **the short payload is a STRICT BYTE PREFIX of the long one** |
| the delta | 🟢 **exactly `1 184` B** — the `APPENDIX: How to apply the Apache License to your work.` block |
| `11 358` B | 🟢 **byte-exactly `b"\n"` + `11 357`** → **`p310`'s fork-signal note, CLOSED** |
| why both modes are holder-BLIND | 🔴 **two DIFFERENT reasons**: `10 173` has **`NO-DECLARATION`**; `11 357`/`11 358` have one and it is **`PLACEHOLDER-DECLARATION`** — `Copyright [yyyy] [name of copyright owner]`, never filled |

🟢 **And the structure is not Apache-specific.** `simjanos-dev/LinguaCafe` serves a
`GPL-3.0`-titled payload at **`32 423` B** against the canonical **`35 149` B**, and it too is a
**strict byte prefix**, delta **`2 726` B** — the `END OF TERMS AND CONDITIONS` +
*"How to Apply These Terms"* block. The operative text through §17 is intact. 🔵 **So
appendix-bimodality is a property of fixed-document licences that ship an instructional
appendix, measured now on two families by prefix rather than by interval — which is exactly why
`T184`'s bands kept getting worse: an interval was being fitted to a discrete bimodal set.**
🔵 **Operational consequence: a `32 423` B GPL-3.0 or a `10 173` B Apache-2.0 is NOT a defective
grant and must not be flagged as one.**

## 🔴 Three wrong rungs, kept as live negative controls

This module's declaration test took three builds, and every failure is one of this base's own
registered classes. They run in the suite rather than sitting in prose, because a defect
described is a claim and a defect that still executes is a test.

| # | the wrong rung | what it did | class |
|---|---|---|---|
| 1 | `copyright` matched **anywhere** in the line | MIT names copyright on **three** lines and only the first is a slot, so an exactly-one guard built on it registered **all twelve** payloads as fixed documents | a MARKER test standing in for a POSITION test — `p124` |
| 2 | a bare `\(c\)` admitted as a declaration opener | Apache-2.0 enumerates conditions `(a)`, `(b)`, `(c)`, so **both** Apache modes read `MULTIPLE-DECLARATIONS` and the two real reasons they are blind were hidden | over-wide alternation |
| 3 | 🔴 **`re.I` on the position test** | Apache **wraps** its prose, so continuation lines begin with a lowercase `copyright notice that is included …`. **Case-insensitivity re-created defect 1 after it had been fixed** — the anchor was right and the alphabet was wrong | `p283-ladder-case-audit`'s subject, met from the other direction |

## 🔴 And the gate caught this module breaking the convention it quotes

`gate-ladder-case` went **red on the first run**: `STANDING:SINGLE-SPELLING` rose **17 → 18** and
named `template_identity.py`. The cause was `GRANT_SUFFIX = "." + "LICENSE"` — a literal grant
path, which `p283` reads as a one-rung licence-path ladder. 🔵
**`p310-family-coverage/fixtures.py` documents this exact hazard and the exact remedy, and this
module restated the hazard in a comment while committing it in code three lines later.** The
ratchet's own note says bumping the ceiling is what eight passes were trained to do, so **the
rung was removed** — `fixture_names()` + `splitext` — and the ceiling was left at 17.
🔵 **`p309`'s *"import the canonical list, never restate it"*, paid for one more time.**

## The rule this pass adds

> **`P311-T`.** A licence family is identified by its **TEMPLATE**, never by its byte length.
> Before a length may be compared at all, the family's FORM must be decided: a **fill-in** form
> has a free variable in it and no interval can bound it; a **fixed-document** form may still be
> **bimodal by section**, so its lengths are a small enumerated set and the relation between
> them is stated as a **prefix**, not as a range.

## Files

| file | what it is |
|---|---|
| `template_identity.py` | the classifier: `normalise` · `template_digest` · `slot_constant` · `form_of` · `identify` · `appendix_prefix_of` |
| `test_template_identity.py` | 80 offline controls, including the refuted MIT band and the three rungs above as live negative controls |
| `fixtures/` | **12 pinned payloads**, each with its byte length in its own filename, every one read first-hand at `p311` over `raw.githubusercontent.com` |

## 🔵 Registered, not claimed

- **`BSD-2-Clause`'s constant is `1 290` on ONE sample.** It is recorded and **not** claimed to
  generalise; one payload is not an invariant.
- 🔴 **`BSD-2-Clause` is where the classifiers are weakest**, not MIT or Apache-2.0: of nine
  instruments, **2 CORRECT · 2 COARSE · 4 ABSTAIN · 1 out-of-domain**. `p419` returns
  *"el encabezado no nombra una familia — tratar como no-osi"* for a payload whose own title line
  reads `BSD 2-Clause License` — an abstention whose attached safe advice points the **wrong way**
  for an OSI-approved permissive licence. Reported, not graded a defect: it is an abstention.
- 🟡 **The two Apache fixtures from `reference-audit` and `time-series-analysis-for-education`
  are byte-identical** (`11 357` · `c71d239df917`); only one is pinned, since a second copy of
  the same bytes adds no coverage.
- 🔴 **No commercial-use column is asserted here.** This module answers identity. `P250`'s
  second column still has no importable oracle — `ACTION p310-R` item 2, **not performed**.
