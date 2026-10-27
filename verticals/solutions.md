---
industry: education
region: Global
updated: 2026-10-27
---

# Education platforms you can customise with AI on top

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it with two platform rows read from bytes and a resolved Fedena entry. Pre-p490
sections remain in
[`archive/2026-10-27-p490-pre-rewrite/solutions.md`](../archive/2026-10-27-p490-pre-rewrite/solutions.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

The "Odoo for education" question, answered by layer. Each row is a real, deployed system with a
license read from bytes at a pinned SHA — see
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## Pick by layer

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| **LMS — mass market** | [Moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | Largest installed base; 2,000+ plugins. A Moodle plugin is the lowest-friction way to ship AI into an existing institution. |
| **LMS — higher ed / MOOC** | [Open edX](https://github.com/openedx/edx-platform) | AGPL-3.0 | 8,200 | University and workforce standard. Deploy via [Tutor](https://github.com/overhangio/tutor) (AGPL-3.0), not by hand. |
| **LMS — North America HE** | [Canvas LMS](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | Dominant in US higher ed. Has a real MCP server already: [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 309★). |
| **LMS — permissive** | [OpenOlat](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 448 | **The only permissive full LMS found.** Pick this when the client needs a closed derivative. |
| **LMS — offline-first** | [Kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,200 | Runs without connectivity. Decisive for rural LATAM/Africa/APAC and for national programmes. |
| **LMS — ease of use** | [Chamilo](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | Francophone + LATAM public sector. |
| **LMS — DACH** | [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | German universities and public sector; SCORM-strong. |
| **LMS + AI mentoring** | [mentingo](https://github.com/Selleo/mentingo) | **MIT** | 100 | Small, modern, AI-native, multi-tenant via Postgres RLS. The best permissive *starting codebase* rather than a migration target. |
| **LMS — modern/greenfield** | [LearnHouse](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2,400 | **New `p491`.** "Next-gen" course and content platform, modern stack. Larger than Kolibri or Chamilo by stars and previously missing from this KB. 🔴 AGPL — not a closed-SaaS base. Default branch `dev`. |
| **SIS / school mgmt (Frappe)** | [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared)* | 682 | **New `p491`.** Admissions, students, programmes, fees on the Frappe stack. 🔴 Grant is a **19-byte stub** naming GPL v3 with no license text — family is GPL-3.0, paperwork is incomplete. **Not the same license as `frappe/lms` (AGPL-3.0).** |
| **Education ERP** | [OpenEduCat](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | Admissions, fees, library, hostel, timetable — on Odoo. This is the literal Odoo answer. |
| **SIS (K-12)** | [RosarioSIS](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | Enrolment, scheduling, grades, attendance, billing. |
| **School management** | [Gibbon](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | Teacher/student/parent/leadership workflows. |
| **Assessment / exams** | [TAO](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based testing. The only substantial open assessment engine. |
| **Interactive content** | [H5P](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | 50+ interactive content types; embeds into Moodle, Canvas, Open edX. |
| **Virtual classroom** | [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,300 | Live classes with whiteboard and breakouts. **LGPL — linking allowed**, the friendliest copyleft here. |
| **Structured lessons** | [Oppia](https://github.com/oppia/oppia) | **Apache-2.0** | 6,900 | Lesson "explorations" with built-in misconception handling. Permissive. |
| **Spaced repetition** | [Anki](https://github.com/ankitects/anki) | AGPL-3.0 | 32,300 | Reference SRS scheduler. Use as the algorithm reference even where the code can't ship. |

## The decision that actually matters on an engagement

**Does the client need to host a modified platform for third parties?**

- **No** (internal use, or they run it themselves) → any row above works. GPL/AGPL obligations
  are satisfied by their own deployment. Take Moodle or Open edX for installed base.
- **Yes, and it must stay closed** → **only three rows survive**: OpenOlat (Apache-2.0),
  Kolibri (MIT), Oppia (Apache-2.0), plus `mentingo` (MIT) as a greenfield base. Everything
  else forces source release to users over a network (AGPL) or to recipients (GPL).
  🔵 **`p491` added two platforms and this shortlist did not change** — both newcomers are
  copyleft. Three passes of platform discovery have not produced a fourth permissive LMS, which is
  itself the answer to "shouldn't we keep looking?".

**The AGPL trap specifically:** Open edX, Canvas, Frappe LMS, Tutor, Anki **and LearnHouse** are
AGPL-3.0.
A Globant-hosted SaaS built on any of them owes source to its users. This is routinely missed
because listicles print "open source" without the family — and in `frappe/lms`'s case print
"MIT" outright, which this pass refuted from bytes.

## AI-on-top integration surfaces that already exist

Don't build the connector — these are real:

| Surface | Repo | License | Reaches |
|---|---|---|---|
| Canvas tool API for agents | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | Canvas LMS; ~102 tools + 8 agent skills |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | MCQs, lesson plans, flashcards |
| Source → study package | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | PDF/video/web/audio → quizzes + SRS |
| Mastery modelling | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | Bayesian Knowledge Tracing |
| Moodle plugin API | — | GPL-3.0 (plugin inherits) | 2,000+ plugin ecosystem; note the plugin is a derivative |
| Eval runtime for tutors | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | MIT | 14,300★. Generic LLM eval; **the only permissive base for a tutoring-quality harness** — the education-specific benchmarks are unlicensed (see [`agents/top.md`](../agents/top.md)) |

## Declared gaps

- **No permissive SIS and no permissive assessment engine exist** (see
  [`repos/foundations.md`](../repos/foundations.md)). For a closed SIS or exam product, there is
  no open base — it is a build.
- **No MCP server for Moodle or Open edX reached a usable star floor.** Canvas is the only
  incumbent LMS with a real, maintained agent tool surface. For Moodle/Open edX, the connector
  is engagement work.
- ~~**`Fedena` (claimed Apache-2.0 SIS) could not be resolved.**~~ 🟢 **Resolved `p491`:** two real
  repos ([`projectfedena/fedena`](https://github.com/projectfedena/fedena) 547★,
  [`foradian/fedena`](https://github.com/foradian/fedena) 4★), **neither carrying a license file**.
  The Apache-2.0 claim comes from a README sentence, not a grant. Still not carried as a row — now
  for an evidenced reason rather than an unresolved one.
- **No maintenance signal is available for any row in this file.** Stars and license are readable;
  the latest-commit date is not, on any channel open to this session. A row's presence here means
  *it exists and its license is known*, **not** *it is actively maintained* — do not let a layer
  table imply currency it cannot support.
