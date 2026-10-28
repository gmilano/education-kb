---
industry: education
region: Global
updated: 2026-10-28
---

# Foundational education repos

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it: **two new platform rows** read from bytes, **Fedena finally resolved**, and an
**arithmetic correction to p490's own census**. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/foundations.md`](../archive/2026-10-27-p490-pre-rewrite/foundations.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

These are the systems an education engagement starts *from* — the ones that already hold the
students, the courses, the enrolments and the grades. The AI goes on top; see
[`compose/patterns.md`](../compose/patterns.md).

Every license below was read from `raw.githubusercontent.com` at the pinned SHA. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## The licence picture is the headline

**The education platform layer is overwhelmingly copyleft.** Of **19** foundational platforms now
read from bytes, **3 are permissive** — and both platforms added this pass are copyleft, so the
permissive numerator has not moved in two passes while the denominator keeps growing. Every
incumbent LMS — Moodle, Open edX, Canvas — is GPL or AGPL. This is the single most commercially
important fact in this file: a hosted, closed derivative of the market-leading education platforms
is not available on any of them.

| | count | repos |
|---|---|---|
| Permissive (MIT / Apache-2.0) | **3** | `oppia`, `kolibri`, `OpenOLAT` |
| GPL / LGPL (hostable, derivative must share) | 10 | `moodle`, `chamilo`, `ILIAS`, `h5p`, `GibbonEdu`, `tao-core`, `rosariosis`, `bigbluebutton`, `openeducat_erp`, **`frappe/education`** |
| AGPL (network copyleft — reaches hosted SaaS) | 6 | `edx-platform`, `canvas-lms`, `frappe/lms`, `tutor`, `anki`, **`learnhouse`** |

🔴 **Arithmetic correction to `p490`.** `p490` published "16 foundational platforms … 3 are
permissive" with a census reading 3 + **8** + 5 = 16. Its own GPL/LGPL cell already *named nine
repos*, and its two tables already *listed seventeen rows* (3 permissive + 14 copyleft). The
count was off by one and the stated total was an undercount: p490's real figure was **17**, not
16. With this pass's two rows it is **19**. The permissive count of 3 was correct throughout and
is unaffected — but any downstream deck quoting "16 platforms" is quoting a miscount.

## Permissive — the ones you can build a closed derivative on

🔴 **Heading corrected `p493`** — it read *"the three"* while the table below it already held four
rows after `p492` added `openmeetings`, and `p493` restores a fifth. **A hard-coded count in a
heading goes stale silently; the table is the census, not the heading.**

| Repo | License | ★ | SHA read | Role |
|---|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 6,900 | `bc73ecf9cf71` | Interactive lesson platform with built-in structured "explorations". Byte-identical to canonical Apache-2.0. Default branch is `develop`, not `main`. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | `dbe14ef6c499` | **Offline-first** learning platform. The one row here designed for no-connectivity deployment — the decisive property for rural LATAM, Africa and APAC programmes. Default branch `develop`. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | **355** | `74b101785bad` | **Source-code plagiarism / academic-integrity engine** — 1 084 B, `sha1 8f6f3815d28d`; **3,865 commits**, the most-maintained repo in this file. Ghent University (`dolos@ugent.be`). 🟢 **Restored `p493`: `p296` recorded this as *already a foundation row* and this KB's identity gate refused a duplicate promotion on that basis — then a later full-file rewrite deleted the row the gate had defended.** The gate worked; the rewrite did not. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 448 | `3736d48fa685` | Full Java LMS, Apache-2.0 (10,982 B). The only permissively-licensed *full* LMS found. Swiss-origin, strong EMEA higher-ed footprint. |

## Copyleft — real systems, with the obligation named

| Repo | License | ★ | SHA read | Role / constraint |
|---|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,300 | `ac97a8bfdc20` | Virtual classroom / web conferencing. LGPL — linking is permitted, so this is the most integration-friendly copyleft row. Default branch `v4.0.x-develop`. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 8,200 | `d9aaee456069` | The Open edX LMS + Studio. Dominant in higher ed and workforce. AGPL: hosting a modified copy for a client triggers source release. Default branch `master`. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | `46c042e7da65` | Largest installed base and the largest plugin ecosystem (2,000+). Grant is at `COPYING.txt`, **not** `LICENSE` — a root-`LICENSE` probe reports "no grant" here. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | 6,900 | `1c9f0bb8013e` | The open LMS by Instructure; heavy North America higher-ed share. AGPL. Default branch `master`. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | 3,400 | `6054772c0426` | Frappe-framework LMS. **Widely published as MIT — it is not.** Grant at `license.txt` (lowercase), 33,893 B, AGPL-3.0; the GitHub sidebar agrees. |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0** | 2,400 | `2d75337273ac` | **New row `p491`.** "Next-gen open source learning platform" — modern course/content platform. At 2,400★ it outranks Kolibri and Chamilo, and was absent from this KB entirely. AGPL confirmed on both channels (`LICENSE`, 34,522 B; sidebar `AGPL-3.0 license`). Default branch **`dev`**. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared only)* | 682 | `73ce33ef2719` | **New row `p491`.** Frappe school-management / SIS app — **a different product from `frappe/lms`, under a different license family.** Its grant is a **19-byte** `license.txt` reading `License: GNU GPL V3` with **no license text at all**; GitHub's classifier cannot resolve it and shows a bare "License" link. See the note below. Default branch `develop`. |
| [ankitects/anki](https://github.com/ankitects/anki) | **AGPL-3.0** | 32,300 | `d87cb22bf337` | Spaced-repetition engine; the reference implementation of SRS scheduling. AGPL. Useful as an algorithm reference even where the code can't be taken. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **AGPL-3.0** | 1,100 | `aa5d1a764b6c` | Docker-based Open edX distribution — the realistic way anyone actually deploys Open edX. Default branch `release`. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | `2d1e97ee4244` | LMS focused on ease of use and accessibility. Notable francophone + LATAM public-sector footprint. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | `fa5f4b66caf4` | Student Information System for school management. **Correct path — `RosarioSIS/RosarioSIS` is a 404** and was cited on this KB. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | `65f86bf061fa` | K-12 school management platform (teachers, students, parents, leadership). Default branch `v31.0.00`. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | `db9582e3cd3e` | German-origin LMS, strong DACH public-sector and university use. Default branch `release_11`. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | `1e21b7a2da4a` | Interactive content types (the H5P core). Embeds into Moodle/Canvas/Open edX; the standard way interactive exercises get authored. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | `46a5d7d40082` | Education **ERP** on Odoo — admissions, fees, hostel, library, timetable. The Odoo-for-education answer. Default branch `19.0`. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | `d9b3da5e6b0a` | Computer-based **assessment** platform core (QTI). The serious open assessment/exam engine. |

## The 19-byte license, and why it matters more than it looks

`frappe/education`'s entire grant is the string `License: GNU GPL V3` — 19 bytes, no license body.
Three consequences, none of them academic:

1. **GitHub cannot classify it.** The sidebar shows a bare "License" link with no SPDX identifier,
   so every tool that trusts the GitHub license field — including this KB's page-fetch channel —
   reports *unknown*, not *GPL-3.0*.
2. **It is a declaration, not a text.** GPL-3.0 is enforced through its own terms; a repository
   that names the license without shipping it still signals GPL-3.0 intent, but a client's counsel
   will ask for the text. Treat the family as **GPL-3.0 and the paperwork as incomplete**.
3. **Two Frappe education products, two license families.** `frappe/lms` is **AGPL-3.0** (p490,
   read at `license.txt`, 33,893 B) and `frappe/education` is **GPL-3.0** (19 B). Anyone who
   generalises "Frappe education apps are X" is wrong whichever X they pick.

## Fedena: resolved, and the Apache-2.0 claim does not survive contact with the repository

`p490` recorded Fedena as "could not be confirmed … not carried as a row." It resolves — to **two**
repositories, both of which `git ls-remote` reaches:

| repo | ★ | grant at SHA | sidebar |
|---|---|---|---|
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 547 | 🔴 **none** (`68a84ac445bf`) | no license shown |
| [foradian/fedena](https://github.com/foradian/fedena) | 4 | 🔴 **none** (`333477b06f1d`) | no license shown |

Both are "Fedena SIS"; the 4★ one is a **fork** of the 547★ one. Neither ships a license file under
any of the nine names probed. The **Apache-2.0** that comparison tables and vendor blogs print for
Fedena traces to a single sentence in the README — *"Fedena is released under the Apache License
2.0"* — and a README sentence is not a grant.

🔴 **Not carried as a permissive row, and the reason is now evidential rather than "unresolved."**
This *strengthens* the finding below: the one candidate that would have broken "no permissive SIS
exists" turns out to have no license at all. Also note the 40,000-schools / 100-countries figures
attached to Fedena in listicles describe the **commercial hosted product**, not these repositories.

## Branch-name trap, worth its own note

**Twelve** of these repos do **not** default to `main` (p491 adds `learnhouse` → `dev` and
`frappe/education` → `develop`; p490's prose said "six" while its own list named ten):
`oppia`, `kolibri` and `frappe/education` (`develop`), `learnhouse` (`dev`),
`edx-platform` and `canvas-lms` (`master`), `tutor` (`release`), `openeducat_erp` (`19.0`),
`GibbonEdu/core` (`v31.0.00`), `ILIAS` (`release_11`), `bigbluebutton` (`v4.0.x-develop`),
`tao-core` (`develop`), and `projectfedena`/`foradian` `fedena` (`master`). Any raw-content fetch
that hardcodes `/main/` returns 404 on all of them — which reads as "file absent" rather than "wrong branch". Resolve the ref with
`git ls-remote --symref` first.

## Declared gaps

- **No permissive SIS exists — confirmed harder this pass.** Every student-information system
  found (`rosariosis` GPL-2.0, `GibbonEdu` GPL-3.0, `openeducat_erp` LGPL-3.0, `openSIS` GPL-2.0,
  `frappe/education` GPL-3.0-declared) is copyleft, and **Fedena — the only candidate published as
  Apache-2.0 — ships no license grant at all**. A client needing a closed-source SIS derivative has
  no open starting point. That is a build, not a fork.
- **No permissive assessment/QTI engine exists.** `tao-core` is GPL-2.0 and is the only
  substantial one.
- ~~**`Fedena` could not be confirmed.**~~ 🟢 **Closed this pass** — it resolves to two repos, both
  unlicensed. See the section above. The claim was not wrong about the repos existing; it was wrong
  about them being licensed.
- **Commit recency is still absent from this file.** The page-fetch channel does not expose the
  latest-commit date (every fetch this pass returned a commit *count* and no date), and
  `api.github.com` is 403 for unattached repos. So **no row here can be shown to be maintained** —
  `fedena` at 547★ may well be abandoned and this file cannot tell. Rows carry a pinned SHA, which
  proves existence and content but not liveness.


## 🆕 `p492` — `2026-10-28` — the permissive numerator moves 3 → 4

Evidence: [`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv).
Narrative: [`repos/trending.md`](trending.md).

`p491` recorded that "the permissive numerator has not moved in two passes while the denominator
keeps growing." 🟢 **It moved this pass**, and in the layer where this file's only option was
copyleft.

| repo | licence | ★ | SHA read | note |
|---|---|---|---|---|
| [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** | 688 | `79b71bcb39f8` | Virtual classroom / web conferencing: video, IM, **whiteboard**, collaborative document editing; media via **Kurento Media Server**. Apache-2.0 read from **51 425 B** (`sha1 d30124557187`); the sidebar shows only an unnamed "License" link, the bytes are unambiguous. Latest release **`v9.1.0`, a security release**. Default branch `master`. **ASF governance** rather than a single maintainer. |

### The census, corrected

| | `p491` published | `p492` |
|---|---|---|
| platforms read from bytes | 19 | **20** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | **4** |
| GPL / LGPL / AGPL and other copyleft | 16 | **16** |
| permissive *full LMS* | 1 (`OpenOLAT`) | **1** — unchanged; **OpenMeetings is not an LMS** |

🔵 **The standing finding survives the correction.** The education platform layer is still
**16 of 20 copyleft**, and every hard gap this file established **still holds**: **no permissive
SIS exists** (both `fedena` repos ship no grant at all) and **no permissive assessment/QTI engine
exists** (`tao-core` remains GPL-2.0). OpenMeetings closes a **conferencing** gap and nothing else.

### How to read this row against BigBlueButton — honestly, in both directions

| | [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | [`apache/openmeetings`](https://github.com/apache/openmeetings) |
|---|---|---|
| ★ | **9,300** | 688 |
| licence | LGPL-3.0 — **linking permitted** | **Apache-2.0** |
| verdict | **still the default** for a live-classroom deployment | a **considered fallback**, not a recommendation |

**BigBlueButton is 13× larger and remains the right default.** LGPL already permits linking, which
is why this file calls it the friendliest copyleft here. The case OpenMeetings uniquely serves is
narrow and real: a deliverable that must ship **modified platform source inside a proprietary
product**, where LGPL's linking allowance does not help. **That case is rare — but this file
previously had no answer for it.** Verify the Kurento dependency and the `v9.1.0` security notes
before proposing it.

### 🔵 Recorded as a teaching resource, deliberately not a foundations row

[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
— **MIT**, 1 082 B, `sha1 b3428e1f52c0` (`2be1800d141e`), **67,600★**. At 67.6k it is the
largest-starred MIT repo this KB has read and would top any table it entered. It holds **no
students, no courses, no enrolments, no grades** — it is 60+ annotated PyTorch paper
implementations, i.e. CS-education *content*. **A foundation here is a system that already holds
the records.** This is not one.

🔵 **Probe-list fix worth more than the row:** its licence file is lowercase **`license`**. A probe
trying only `LICENSE`/`LICENSE.md` reports "no licence" on an MIT repo — the `fedena`
false-negative mechanism in reverse. **Add lowercase `license` to the nine probed names.**

### 🟢 The maintenance gap is partly closed

This file has declared, for several passes, that "no row here can be shown to be maintained."
**That was too strong.** The page-fetch channel **does** expose tagged releases with dates —
`openmeetings v9.1.0`, `canvas-mcp v1.16.0` (Oct 2026), `DeepTutor v1.6.15` (`2026-10-19`),
`education-agent-skills v3.1.0` (`2026-10-22`). For any repo that tags releases, **liveness is
readable**. The remaining limit is real but narrower: repos that never tag have no signal, and
`api.github.com` stays 403 for unattached repos. **Next pass should read a release date for every
row in this file** — it is available and this file was not using it.


## 🆕 `p493` — `2026-10-28` — the census was measuring this KB's bookkeeping, not the ecosystem

Reads: [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).
Narrative and the full list of dropped rows: [`agents/trending.md`](../agents/trending.md) `p493`.

🔴 **`p490` rewrote `agents/top.md` in full and `p383`/`p391`/`p392` rewrote this file in full.
A full-file rewrite re-derives its tables from the rewriting pass's own reads, so any row an
earlier pass promoted but that pass did not re-read is deleted without a marker.** Eight addresses
this KB had recorded as promoted are absent from both shelf files at HEAD `cb6a4be`; `dolos` is the
one that belongs here and it is restored above.

### The census, corrected again — and the correction is about the denominator's authority

| | `p491` | `p492` | `p493` |
|---|---|---|---|
| platforms read from bytes | 19 | 20 | **21** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | 4 | **5** |
| copyleft | 16 | 16 | **16** |
| permissive *full LMS* | 1 | 1 | **1** — `OpenOLAT`, unchanged |

🔴 **Do not read the `4 → 5` as ecosystem movement.** `p492`'s `3 → 4` was a real find
(`apache/openmeetings`). **`p493`'s is a repair**: `dolos` was always in the ecosystem and was
previously in this file. Two passes in a row have now moved the permissive numerator for
**different reasons**, and conflating them would turn a bookkeeping fix into a false trend.

### What still holds, and what does not

🟢 **Holds, and `p493` re-confirms it:** the **full-LMS** layer is copyleft-bound —
`OpenOLAT` (Apache-2.0, 448★) is the only permissive full LMS, against Moodle (GPL-3.0),
Open edX (AGPL-3.0), Canvas (AGPL-3.0), `frappe/lms` (AGPL-3.0, widely mispublished as MIT) and
`learnhouse` (AGPL-3.0). **No permissive SIS exists** (both `fedena` repos ship no grant).
**No permissive assessment/QTI engine exists** (`tao-core`, GPL-2.0). These are the gaps that
actually constrain an engagement and none of them moved this pass.

🔴 **Does not hold:** the generalisation that *the education stack* is copyleft-bound. With the
restored rows (see [`repos/trending.md`](trending.md) `p493`), the courseware, tutoring-platform,
teacher-workflow, academic-integrity and evaluation layers each have a permissive option, and an
end-to-end all-permissive stack is assemblable for the first time — wired up as
[`compose/patterns.md`](../compose/patterns.md) `P493-1`. **The constraint is specific to the
LMS/SIS/assessment core, and saying so is both more accurate and more useful than the blanket
claim.**

### 🔵 Declared gap, unchanged and restated

**No permissive SIS and no permissive QTI assessment engine** — searched again this pass across the
brief's platform query (`open source platform education ERP SIS student information system MIT
Apache 2026`). 🔴 **The query returned no permissive candidate at all**: OpenEduCat (LGPL-3.0),
RosarioSIS (GPL-2.0), `frappe/education` (GPL-3.0), Unifiedtransform (GPL-3.0), openSIS and Gibbon
(GPL-3.0). **Every education ERP/SIS this KB can find is copyleft.** That is now a four-pass
consistent result and should be treated as a property of the sector, not of the search.
