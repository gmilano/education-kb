---
industry: education
region: Global
updated: 2026-10-20
---

# `p342-family-axis-readability` — T31's falsifier, run, and the axis it repairs

**Pass 342 · 2026-10-20.** The repair itself lives in
[`pass257-restriction-scan`](../pass257-restriction-scan/restriction_scan.py) and is
gated there — `python3 -I test_restriction_scan.py` → **185/185** (was 129/129),
fully offline, already in `make hooks`. 🔵 **This directory holds no new classifier
and no new probe loop on purpose.** `p340` named "capability present, nearly
re-derived as news" five times and `p341` spent its opening reading
`compose/code/` to avoid it; this pass reuses four instruments and writes none.

Inherited gate state, measured on p341's HEAD before a byte changed:
🟢 `make hooks` **24/24 green, exit 0** · 🟢 `make gate-offline` green ·
🟢 `make recount` MATCH on all five registered claims, `STALE=0 NO-ANCHOR=0`.
**Third consecutive clean inheritance.**

## What T31 asked, and what the falsifier answered

`p341` opened T31 and named its falsifier as cheap: *"probe the Spanish- and
Chinese-language platform tiers. If their payloads resolve, the defect is
specifically Portuguese and not 'non-English.'"*

**Run over 25 addresses, 21 payloads read first-hand** through
[`p341`'s probe](../p341-bespoke-instrument-census/probe.sh) (sourced, not rewritten)
and graded through four channels:
[`p342-nonenglish-title-falsifier`](../../../evidence/p342-nonenglish-title-falsifier.2026-10-20-p342.tsv).

🟢 **The falsifier's prediction HELD. All 15 Spanish- and Chinese-tier payloads type
`en` and resolve a family on the first channel** — `chamilo/chamilo-lms` ships the
stock English GPL-3.0 (35 147 B), `francoisjacquet/rosariosis` the English GPL-2.0,
`OS4ED/openSIS-Classic` the English GPL-2.0 with a BOM, and nine CJK-owned
repositories ship the stock English MIT text. **A translated licence payload is not
a general non-English phenomenon in this vertical. It is a Brazilian one.**

🔴 **And T31's own population is wrong: it is 1, not 3.** `bncc-dev/bncc-benchmark`
and `bncc-dev/bncc-pacotes` return no family for a reason that has nothing to do
with Portuguese — they are **dual-licence index documents** naming MIT for code and
CC BY 4.0 for data, each text in a sibling file, with no operative clause of their
own. An English translation of either would also return no family. **Only
`portabilis/i-diario` is blind because its title is Portuguese.**

🔴 **The fact that kills the obvious shortcut.** `portabilis` ships **both**:
`i-educar`'s grant is the **English** GPL-2.0 (18 092 B) and `i-diario`'s is the
**Portuguese** AGPL-3.0 (35 326 B) — same owner, same country, same stack, same
pass. So the payload's language is a **per-repository** fact, not a regional or
owner-level one, and "flag the LATAM rows for a human read" cannot work. Every
payload has to be typed.

## The repair, and the regression it was one line away from

Two changes in `pass257`, both narrow:

1. **`TITLE_ANCHORS_BY_LANGUAGE`** — the `en` arm moved verbatim, plus a `pt` arm
   carrying the one title form a payload establishes
   (`licença pública geral affero gnu`, both accented and unaccented).
   `i-diario` now resolves **`AGPL` / `COPYLEFT`** instead of
   `UNCLASSIFIED:no-family-no-restriction`.
2. **`VERDICT_UNREADABLE_TITLE`** — `p287`'s own reasoning applied to the axis
   beside the one it fixed. `p287` keyed the *restriction* vocabulary by language
   and gave it `UNREADABLE-BODY`; the *family* vocabulary stayed English-only with
   no admission of its own, so a Portuguese payload came out as *nothing found*
   because `pt` **is** a covered restriction language and the body axis's
   admission could never fire. The two admissions are now distinct.

🔴 **`pt` is deliberately NOT in `FAMILY_TITLE_VOCABULARY_COMPLETE`, and that is
the whole safety argument.** The `pt` arm knows one family. Declaring `pt`
"covered" because it now has anchors would mean a Portuguese **GPL-2.0** payload
came out `UNCLASSIFIED` — reintroducing, for GPL, exactly the defect this pass
removed for AGPL. Having one family's title in a language is not coverage of that
language. Pinned by `test_restriction_scan.py` controls **11b**.

🟢 **"No English verdict moved" is asserted, not claimed.** `family_of` and `scan`
take an optional `title_languages`, so `scan(x, {"en"})` reproduces the p341
vocabulary and control **11c** compares **every field** of both results across all
eight pre-existing fixtures. Control **11f** re-runs `P171`'s collision
measurement: no `pt` anchor appears anywhere in any other fixture, including the
35 146 B English GPL-3.0 whose own §13 names the Affero GPL.

## Measured this pass and NOT patched — three instruments, each named

Each is real, each has a direction, none is a vocabulary tweak that belongs in this
pass. Evidence:
[`p342-channel-disagreement`](../../../evidence/p342-channel-disagreement.2026-10-20-p342.tsv).

- 🔴 **`lib/license_family.sh::family_of` answers `MIT` on `haolpku/k12-kgraph`** —
  a payload whose title line reads
  `Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)`. The
  only occurrence of "MIT" in it is the sentence *"The source code … is released
  separately under the MIT License; see LICENSE-CODE"* — a **cross-reference to a
  different file's grant**, read as this payload's own. **Permissive reported for a
  NonCommercial instrument, in English, on a fully covered language: the highest-
  severity finding of this pass.** 🟢 Mitigated, not open: `pass257` returns
  `RESTRICTED:added-restriction` and `pass258` returns not-usable with both axes
  named, so a two-channel read is safe and the shelf cell is already correct.
  🔵 Not patched because the right change is **scoped-grant detection** — "a row's
  state is not what it QUOTES", which `p262` already names — with its own controls,
  in a shell classifier that four standing gates consume. That is its own piece of
  work, the same judgement `p341` recorded about the ECL rung.
- 🔴 **`p307.classify_payload` types `i-diario`'s 35 KB operative AGPL grant as
  `POINTER url=https://fsf.org/`** — the FSF address inside the licence text's own
  boilerplate. Its `GRANT_CLAUSES` are English-only, so the URL fallback fires on a
  complete grant. **The same language blindness, in a third instrument**, which
  `p341` could not see because it measured two channels. It also types
  `bncc-benchmark` as `RESERVED` — **a dual-permissive repository as
  rights-reserved** — because its POINTER class requires an `http(s)` URL and these
  pointers are **relative sibling paths**; and on `bncc-pacotes` it latches a link
  to a sibling *project* as its "pointer".
- 🟡 **`pass258.CC_ANCHOR` is the literal `"creative commons"`**, so
  `bncc-benchmark` (which writes `CC BY 4.0`) returns `NOT-A-CONTENT-LICENCE` while
  `bncc-pacotes` (which spells out `Creative Commons Attribution 4.0
  International`) returns `CONTENT-POINTER:not-a-grant`. **Two sibling repositories
  under one licensing model, two verdicts, on spelling alone.**

## Reproducing it

    # the online limb (needs raw.githubusercontent.com + github.com)
    bash compose/code/p341-bespoke-instrument-census/probe.sh SLUGS OUTDIR

    # the graded suite, offline
    cd compose/code/pass257-restriction-scan && python3 -I test_restriction_scan.py
