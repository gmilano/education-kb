---
industry: education
region: Global
updated: 2026-10-27
---

# Foundational education repos

**Pass `p490` — reads of 2026-10-27.** Rewritten this pass; 62 prior pass-sections preserved in
[`archive/2026-10-27-p490-pre-rewrite/foundations.md`](../archive/2026-10-27-p490-pre-rewrite/foundations.md).

These are the systems an education engagement starts *from* — the ones that already hold the
students, the courses, the enrolments and the grades. The AI goes on top; see
[`compose/patterns.md`](../compose/patterns.md).

Every license below was read from `raw.githubusercontent.com` at the pinned SHA. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## The licence picture is the headline

**The education platform layer is overwhelmingly copyleft.** Of 16 foundational platforms read
this pass, **3 are permissive**. Every incumbent LMS — Moodle, Open edX, Canvas — is GPL or
AGPL. This is the single most commercially important fact in this file: a hosted, closed
derivative of the market-leading education platforms is not available on any of them.

| | count | repos |
|---|---|---|
| Permissive (MIT / Apache-2.0) | **3** | `oppia`, `kolibri`, `OpenOLAT` |
| GPL / LGPL (hostable, derivative must share) | 8 | `moodle`, `chamilo`, `ILIAS`, `h5p`, `GibbonEdu`, `tao-core`, `rosariosis`, `bigbluebutton`, `openeducat_erp` |
| AGPL (network copyleft — reaches hosted SaaS) | 5 | `edx-platform`, `canvas-lms`, `frappe/lms`, `tutor`, `anki` |

## Permissive — the three you can build a closed derivative on

| Repo | License | ★ | SHA read | Role |
|---|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 6,900 | `bc73ecf9cf71` | Interactive lesson platform with built-in structured "explorations". Byte-identical to canonical Apache-2.0. Default branch is `develop`, not `main`. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | `dbe14ef6c499` | **Offline-first** learning platform. The one row here designed for no-connectivity deployment — the decisive property for rural LATAM, Africa and APAC programmes. Default branch `develop`. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 448 | `3736d48fa685` | Full Java LMS, Apache-2.0 (10,982 B). The only permissively-licensed *full* LMS found. Swiss-origin, strong EMEA higher-ed footprint. |

## Copyleft — real systems, with the obligation named

| Repo | License | ★ | SHA read | Role / constraint |
|---|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,300 | `ac97a8bfdc20` | Virtual classroom / web conferencing. LGPL — linking is permitted, so this is the most integration-friendly copyleft row. Default branch `v4.0.x-develop`. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 8,200 | `d9aaee456069` | The Open edX LMS + Studio. Dominant in higher ed and workforce. AGPL: hosting a modified copy for a client triggers source release. Default branch `master`. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | `46c042e7da65` | Largest installed base and the largest plugin ecosystem (2,000+). Grant is at `COPYING.txt`, **not** `LICENSE` — a root-`LICENSE` probe reports "no grant" here. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | 6,900 | `1c9f0bb8013e` | The open LMS by Instructure; heavy North America higher-ed share. AGPL. Default branch `master`. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | 3,400 | `6054772c0426` | Frappe-framework LMS. **Widely published as MIT — it is not.** Grant at `license.txt` (lowercase), 33,893 B, AGPL-3.0; the GitHub sidebar agrees. |
| [ankitects/anki](https://github.com/ankitects/anki) | **AGPL-3.0** | 32,300 | `d87cb22bf337` | Spaced-repetition engine; the reference implementation of SRS scheduling. AGPL. Useful as an algorithm reference even where the code can't be taken. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **AGPL-3.0** | 1,100 | `aa5d1a764b6c` | Docker-based Open edX distribution — the realistic way anyone actually deploys Open edX. Default branch `release`. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | `2d1e97ee4244` | LMS focused on ease of use and accessibility. Notable francophone + LATAM public-sector footprint. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | `fa5f4b66caf4` | Student Information System for school management. **Correct path — `RosarioSIS/RosarioSIS` is a 404** and was cited on this KB. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | `65f86bf061fa` | K-12 school management platform (teachers, students, parents, leadership). Default branch `v31.0.00`. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | `db9582e3cd3e` | German-origin LMS, strong DACH public-sector and university use. Default branch `release_11`. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | `1e21b7a2da4a` | Interactive content types (the H5P core). Embeds into Moodle/Canvas/Open edX; the standard way interactive exercises get authored. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | `46a5d7d40082` | Education **ERP** on Odoo — admissions, fees, hostel, library, timetable. The Odoo-for-education answer. Default branch `19.0`. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | `d9b3da5e6b0a` | Computer-based **assessment** platform core (QTI). The serious open assessment/exam engine. |

## Branch-name trap, worth its own note

Six of these repos do **not** default to `main`: `oppia` and `kolibri` (`develop`),
`edx-platform` and `canvas-lms` (`master`), `tutor` (`release`), `openeducat_erp` (`19.0`),
`GibbonEdu/core` (`v31.0.00`), `ILIAS` (`release_11`), `bigbluebutton` (`v4.0.x-develop`),
`tao-core` (`develop`). Any raw-content fetch that hardcodes `/main/` returns 404 on all of
them — which reads as "file absent" rather than "wrong branch". Resolve the ref with
`git ls-remote --symref` first.

## Declared gaps

- **No permissive SIS exists.** Every student-information system found (`rosariosis` GPL-2.0,
  `GibbonEdu` GPL-3.0, `openeducat_erp` LGPL-3.0, `openSIS` GPL-2.0) is copyleft. A client
  needing a closed-source SIS derivative has no open starting point — that is a build, not a fork.
- **No permissive assessment/QTI engine exists.** `tao-core` is GPL-2.0 and is the only
  substantial one.
- **`Fedena` could not be confirmed.** Listed as Apache-2.0 by one source; no maintained
  canonical GitHub repo resolved via `ls-remote`. Not carried as a row.
