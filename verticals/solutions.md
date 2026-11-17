---
industry: education
region: Global
updated: 2026-11-17
---

# Vertical platforms — education

**Pass `p871`, 2026-11-17.** Real, deployed systems that can be customised with AI on top —
the education equivalents of Odoo for ERP or OpenMRS for healthcare. Existence and licence
bytes verified this run via `git ls-remote` + `raw.githubusercontent.com` on the resolved
default branch.

> **The single most important strategic fact in this file:** the education platform layer is
> **overwhelmingly copyleft**. Of the 20 verified platforms below, only **5** are permissive
> (Apache-2.0 / MIT / BSD). The brief asks for MIT / Apache / BSD because those are what
> Globant can build on — in this vertical that constraint eliminates Moodle, Canvas, Open edX,
> ILIAS, Chamilo and both SIS options. The workable pattern is therefore **not** forking a
> platform: it is building permissive AI services that attach over **LTI 1.3** and **xAPI**.
> That integration seam is the actual product surface in education.

## Learning management systems

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| **Moodle** | https://github.com/moodle/moodle | GPL-3.0 (`COPYING.txt`) | `main` | The most widely deployed LMS worldwide and dominant in EMEA and LATAM public education. Has a first-party AI subsystem with pluggable providers, so **AI can be added as a plugin without forking** — the cleanest copyleft-safe integration path in this file. |
| **Open edX** | https://github.com/openedx/edx-platform | AGPL-3.0 | `master` | Originated at MIT and Harvard, now stewarded by the non-profit Axim Collaborative. The standard choice for large-scale MOOC and national-platform deployments. Note: the *platform* is AGPL-3.0 — the Apache-2.0 figure that circulates in listicles refers to satellite repos such as `openedx-aspects`, not to `edx-platform`. Verified this run. |
| **Canvas LMS** | https://github.com/instructure/canvas-lms | AGPL-3.0 | `master` | Dominant in North American higher education. The open-source edition carries core LMS function; some commercial features are withheld. AGPL. |
| **ILIAS** | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | `release_11` | Strong in German-speaking EMEA, including public-sector and military training. Note the default branch is `release_11`, not `main`. |
| **Chamilo** | https://github.com/chamilo/chamilo-lms | GPL-3.0 | `master` | Significant installed base in **LATAM** and francophone Africa; lighter to operate than Moodle, which is why ministries with thin IT capacity pick it. |
| **Sakai** | https://github.com/sakaiproject/sakai | **ECL-2.0** | `master` | Apereo Foundation, research-university focus. Educational Community License 2.0 is an Apache-2.0 derivative — **more permissive than the rest of this table**, a genuinely under-used fact. |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | `master` | Swiss-origin, used across EMEA higher education. **The only major full LMS here under a clean permissive licence** — the obvious base if a client needs a customised LMS that Globant can extend without copyleft obligations. |
| **Frappe LMS** | https://github.com/frappe/lms | **AGPL-3.0** | `develop` | Modern, lightweight LMS on the Frappe framework. **Correction recorded this pass:** multiple 2026 listicles state MIT; the licence bytes at `license.txt` are **AGPL-3.0**. |
| **Kolibri** | https://github.com/learningequality/kolibri | **MIT** | `develop` | Learning Equality. Purpose-built for **offline-first, low-connectivity and low-resource deployments** — the platform of record for rural LATAM, Sub-Saharan Africa and South Asia programmes. MIT-licensed. For any equity-of-access or ministry-of-education mandate, this is the starting point, not Moodle. |

## Courseware, content & assessment

| Platform | Repo | Licence | Branch | Position & AI surface |
|---|---|---|---|---|
| **Oppia** | https://github.com/oppia/oppia | **Apache-2.0** | `develop` | Interactive lesson platform built around structured "explorations" with misconception-specific feedback. Apache-2.0, and its explicit misconception model is unusually well matched to LLM-generated remediation. |
| **Perseus (Khan Academy)** | https://github.com/Khan/perseus | **MIT** | `main` | Khan Academy's exercise and question rendering framework. MIT — directly embeddable, and the fastest route to a credible practice-item UI. |
| **H5P** | https://github.com/h5p/h5p-php-library | GPL-3.0 | `master` | The interactive-content standard embedded inside Moodle, Canvas and Open edX. Content-type authoring for interactive video, branching scenarios, quizzes. |
| **Anki** | https://github.com/ankitects/anki | AGPL-3.0 | `main` | The dominant spaced-repetition application. Relevant as an **export target**: DeepTutor already exports to it, so a Globant build can meet learners in the tool they use. Pair with MIT-licensed `fsrs4anki` for the scheduler. |

## Student information, library & repository systems

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Gibbon** | https://github.com/GibbonEdu/core | GPL-3.0 | `v31.0.00` | School management / SIS for K-12. Note: default branch is a version tag, not `main`. |
| **openSIS Classic** | https://github.com/OS4ED/openSIS-Classic | **GPL per README; no licence file** | `master` | Student information system. **Licence flag:** there is no `LICENSE`, `COPYING` or `license.txt` on the default branch — the GPL claim exists only in prose in the README. Treat the grant as unconfirmed until clarified with OS4ED. |
| **Koha** | https://github.com/Koha-Community/Koha | GPL-3.0 | `main` | The mature open-source integrated library system; very large installed base in school and university libraries worldwide. |
| **DSpace** | https://github.com/DSpace/DSpace | **BSD** | `main` | Institutional repository for theses, datasets and scholarly output. **Permissive** — a strong base for AI-assisted discovery and metadata enrichment over a university's own corpus. |
| **Open Journal Systems** | https://github.com/pkp/ojs | GPL-3.0 | `main` | PKP's scholarly publishing platform; heavily used by LATAM and Global South universities for their own journals. |

## Classroom delivery & lecture capture

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **BigBlueButton** | https://github.com/bigbluebutton/bigbluebutton | LGPL | `v4.0.x-develop` | Virtual classroom built for teaching rather than for meetings (whiteboard, breakout rooms, polling); integrates with Moodle and Canvas. LGPL — linking is permitted, which makes it friendlier than GPL for an attached service. |
| **Opencast** | https://github.com/opencast/opencast | **ECL-2.0** | `develop` | University lecture capture and video management. ECL-2.0 (Apache-derived, permissive). The natural source of the lecture-video corpus a tutoring agent should be grounded in. |

## Offline & low-connectivity delivery

Treated as a first-class category rather than a footnote, because it decides whether a
ministry programme reaches rural schools at all.

| Platform | Repo | Licence | Branch | Position |
|---|---|---|---|---|
| **Kiwix** | https://github.com/kiwix/kiwix-tools | GPL-3.0 | `main` | Offline Wikipedia and educational-archive reader (ZIM format). Already an ingest source for DeepTutor, so an offline corpus can feed an offline tutor. |
| **Internet-in-a-Box** | https://github.com/iiab/iiab | LGPL | `master` | Turnkey offline learning server — bundles Kiwix, Moodle and content libraries onto low-cost hardware for schools without reliable connectivity. |

**22 verified platforms.**

## Permissive-licence shortlist

For a Globant engagement that must avoid copyleft obligations, the verified permissive set is:

| Platform | Licence | Use it for |
|---|---|---|
| **OpenOLAT** | Apache-2.0 | A full LMS you can extend and commercialise |
| **Kolibri** | MIT | Offline-first / low-connectivity delivery |
| **Oppia** | Apache-2.0 | Interactive courseware with misconception handling |
| **Perseus** | MIT | Exercise and assessment item UI |
| **Sakai** | ECL-2.0 | Research-university LMS |
| **Opencast** | ECL-2.0 | Lecture capture and video corpus |
| **DSpace** | BSD | Institutional repository / scholarly corpus |

## Declared gaps

- **No permissive open-source SIS exists.** Both verified options are copyleft and one has no
  licence file. A permissive, AI-native SIS is an unmet need — and an opportunity.
- **No open-source exam-proctoring platform was found** that is both maintained and
  permissively licensed. Given that the EU has moved AI proctoring into the high-risk tier
  (see `intel/market.md`), this is a conspicuous hole in the OSS landscape.
- **No LATAM-origin education *platform*** surfaced in this run's searches. LATAM appears in
  this file as a large **deployer** of Moodle, Chamilo, Kolibri and OJS, not as an originator
  of platforms. That asymmetry is itself the regional finding.
