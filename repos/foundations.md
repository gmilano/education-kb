---
industry: education
region: Global
updated: 2026-11-13
---

# Foundational open-source repos for education

The platforms and libraries an education engagement actually builds on. **26
repos**, all verified on 2026-11-13 from the rendered repository page (license
field + star count). Grouped by the job they do, because "foundational" in
education means four different layers: the LMS, the student record, the content
format, and the learning-data/ML layer.

License matters more here than anywhere else in this KB: the big three LMSs are
**AGPL-3.0 or GPL-3.0**, which governs what a studio can hand a client as a
derived product. The MIT/Apache/BSD/ECL rows are the ones that compose freely.

## Learning platforms (LMS / MOOC)

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | Open edX LMS & Studio. **Formerly `openedx/edx-platform`** — that path now serves this repo; use this name. Stewarded by the nonprofit Harvard and MIT founded. |
| https://github.com/moodle/moodle | GPL-3.0 | 7.6k | The world's most deployed LMS. Plugin architecture is the integration surface. |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | The open LMS by Instructure; dominant in North American higher ed. Pair with `canvas-mcp` for agent access. |
| https://github.com/frappe/lms | AGPL-3.0 | 3.4k | Modern, lightweight LMS on the Frappe framework. Fastest to stand up of the group. |
| https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | Docker-based Open edX distribution. In practice this is *how* you deploy Open edX. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; strong LATAM and francophone footprint. |
| https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Higher-ed teaching/research/collaboration suite. **ECL-2.0 is Apache-2.0 with a patent clause tuned for universities** — permissive, and the friendliest license in this table. |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | Long-lived German LMS; heavy use in EMEA public sector and military/vocational training. |

## Student information systems and institutional ERP

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | SIS + LMS + finance modules as Odoo apps. The "Odoo for education" answer. |
| https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | RosarioSIS student information system for school management. Widely used in LATAM K-12. |
| https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible open-source school management platform. |
| https://github.com/OS4ED/openSIS-Classic | GPL (per README) | 351 | openSIS student information system. Sidebar shows no license badge; GPL claim comes from the README. |

## Content, authoring and delivery

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition engine. License read from the `LICENSE` file — GitHub's sidebar does not name it. The scheduling algorithm is the reusable asset. |
| https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Web conferencing built for virtual classes; LTI into Moodle/Canvas. |
| https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Free online learning platform with interactive explorations. **Apache-2.0 — permissive and substantial.** |
| https://github.com/Khan/perseus | MIT | 1.6k | Khan Academy's exercise question editor and renderer. **MIT** — the cleanest way to get real exercise rendering into a product. |
| https://github.com/learningequality/kolibri | MIT | 1.2k | Offline-first learning platform for low-connectivity settings. **MIT**, and the reference implementation for offline education. |
| https://github.com/opencast/opencast | ECL-2.0 | 511 | Automated lecture capture and video distribution at scale. |
| https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | Framework-agnostic H5P interactive content library. H5P is the de facto interactive-content format across Moodle/Canvas/Open edX. |
| https://github.com/learningequality/kolibri-design-system | No license shown | 53 | Kolibri's design system. Listed for completeness; **no license on the page**, so treat as unlicensed until confirmed. |

## Learning data, ML and assessment infrastructure

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user Jupyter server. The backbone of university CS/data-science teaching. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assigning and autograding notebooks. **The autograding layer to wrap an agent around.** |
| https://github.com/pykt-team/pykt-toolkit | MIT | 461 | pyKT: benchmark library for deep-learning knowledge-tracing models. **MIT** — the quantitative learner-modelling layer that LLM tutors usually lack. |
| https://github.com/getodk/collect | Apache-2.0 | 805 | Android app for offline form data collection; used for education field surveys and assessment at scale in low-connectivity regions. |
| https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | Open edX plugin housing AI tools and helpers. Early (17 stars) but it is the *official* AI extension point for Open edX. |
| https://github.com/1edtech/caliper-spec | IMS Global Specification Document License | 22 | Caliper Analytics spec — organizing and exchanging learning activity data. **Spec-document license, not a software license**: implement the spec, do not vendor the repo. |

## Interoperability standards worth knowing (not all are code repos)

- **LTI 1.3 / LTI Advantage** (1EdTech) — how any tool mounts inside Moodle,
  Canvas, Open edX, Sakai, ILIAS. The single highest-leverage integration to
  support: build the LTI tool once, reach every LMS above.
- **xAPI (Experience API)** and **Caliper Analytics** — the two learning-event
  telemetry standards. Emit one of them from any agent you build, or the
  institution cannot report on it.
- **QTI** — assessment item interchange. Matters the moment a client wants to
  move an item bank between systems.

## Declared gaps

- **No permissively licensed full LMS exists at scale.** Every LMS with real
  deployment is GPL/AGPL except Sakai (ECL-2.0). A client who needs a
  proprietary derived platform cannot start from Moodle, Canvas, or Open edX —
  that constraint should be surfaced in week one, not month three.
- **No open-source LTI 1.3 tool-provider library made the verified set.** The
  standard is the key integration path and the tooling for it is scattered
  across language-specific libraries; none surfaced as a clear foundational repo
  in this window. Worth a dedicated pass.
