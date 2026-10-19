---
industry: education
region: Global
updated: 2026-10-19
---

# Vertical platforms — education

**Pass 315 · 2026-10-19.** The real systems a client is already running, or would run, with AI
built on top. All ten verified first-hand this pass.

| Platform | Repo | Licence | ★ (2026-10-19) | What it is | AI-on-top angle |
|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.5k | The world's most deployed open source LMS | Build as a Moodle plugin or an external tool over LTI 1.3; never link AI code into the core |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | LMS + Studio behind large-scale MOOCs and corporate academies | Agents as XBlocks or LTI tools; AGPL makes the network boundary non-negotiable |
| Tutor | https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | Docker-based Open edX distribution | How you actually stand up Open edX in an engagement; plugin system is the clean AI insertion point |
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 889 | Education ERP on the Odoo framework — SIS, LMS, finance, HR, CRM | The Odoo-of-education: admin-side agents (enrolment, scheduling, fee chasing) rather than tutoring |
| Kolibri | https://github.com/learningequality/kolibri | MIT | 1.2k | Offline-first learning platform for low-connectivity settings | The only MIT platform here — AI can be embedded directly, but must run on-device or batch-sync |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.2k | Web conferencing purpose-built for virtual classrooms | Post-session agents: transcription, participation analytics, summary-to-LMS |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Learning, teaching, research and collaboration platform used in higher ed | ECL-2.0 is an Apache-2.0 derivative with an academic-attribution twist — the most permissive LMS core here |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 151 | Interactive content types (quizzes, branching scenarios) embedded in Moodle/Open edX/Canvas | Generate H5P content JSON with an agent; the renderer stays untouched, so GPL stays contained |
| Richie | https://github.com/openfun/richie | MIT | 316 | Education-portal CMS (France Université Numérique) | MIT front end over an AGPL Open edX back end — the licence-safe catalogue/portal layer |
| Sunbird | https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | Portal of India's national digital-education stack | The base for an APAC public-sector engagement; see the caveat in `repos/foundations.md` |

## The licence fact that decides every engagement

**The platform tier is copyleft; the agent tier is not.** Of the ten platforms above, only three
(Kolibri, Richie, Sunbird — all MIT) and arguably Sakai (ECL-2.0) can take AI code linked directly
in. Moodle is GPL-3.0; Open edX and Tutor are AGPL-3.0; OpenEduCat is LGPL-3.0; BigBlueButton is
LGPL-3.0; H5P is GPL-3.0.

The consequence is concrete and it is the same in every region: **put Globant's agent code on the
far side of a network boundary** (LTI 1.3 tool, external service, MCP server, webhook consumer),
not inside the platform process. `pylti1.3` (MIT) is the repo that makes this practical. AGPL in
particular reaches network use of a *modified* platform — leaving Open edX unmodified and talking to
it over LTI keeps Globant's work separately licensed.

For LGPL (OpenEduCat, BigBlueButton) dynamic linking is permitted with conditions, which is a
materially weaker constraint than AGPL — but "weaker" is not "absent", and the client's counsel
should see it in writing either way.

## Declared gaps

- **Canvas LMS was not verified this pass** and so is deliberately absent from the table rather
  than carried forward from an earlier pass on trust. It is a major platform (Instructure, AGPL-3.0
  for the open source edition) and belongs here once read first-hand.
- **No LATAM-originated platform** found at this tier. Public-sector LATAM deployments in this
  sector run on the platforms above (notably Kolibri) rather than on locally authored stacks.
