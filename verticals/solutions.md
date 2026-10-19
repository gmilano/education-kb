---
industry: education
region: Global
updated: 2026-10-19
---

# Vertical platforms — education

**Pass 316 · 2026-10-19.** Fifteen platforms — the real systems a client is already running, or
would run, with AI built on top. **Checked** says whether the licence/star reading was taken in this
pass (p316) or earlier the same day (p315).

| Platform | Repo | Licence | ★ | Checked | What it is | AI-on-top angle |
|---|---|---|---|---|---|---|
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.2k | p315 | Web conferencing purpose-built for virtual classrooms | Post-session agents: transcription, participation analytics, summary-to-LMS |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | p315 | LMS + Studio behind large-scale MOOCs and corporate academies | Agents as XBlocks or LTI tools; AGPL makes the network boundary non-negotiable |
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.5k | p315 | The world's most deployed open source LMS | Build as a Moodle plugin or an external tool over LTI 1.3; never link AI code into the core |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | p316 | The open LMS by Instructure; 78,765 commits | **Verified this pass, closing a declared gap.** Same AGPL discipline as Open edX — and see the Project Athena note below |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | p315 | Learning, teaching, research and collaboration platform used in higher ed | ECL-2.0 is an Apache-2.0 derivative with an academic-attribution twist — the most permissive LMS core here |
| Kolibri | https://github.com/learningequality/kolibri | MIT | 1.2k | p316 | Offline-first learning platform for low-connectivity settings | The only MIT general platform — AI can embed directly, but must run on-device or batch-sync |
| Tutor | https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | p315 | Docker-based Open edX distribution | How you actually stand up Open edX in an engagement; plugin system is the clean AI insertion point |
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 889 | p315 | Education ERP on the Odoo framework — SIS, LMS, finance, HR, CRM | The Odoo-of-education: admin-side agents (enrolment, scheduling, fee chasing) rather than tutoring |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 669 | p316 | School management system on the Frappe/ERPNext framework; 1,095 commits | ERPNext-shop clients already run the framework; GPL-3.0 confirmed from `license.txt`, not assumed |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 647 | p316 | K-12 Student Information System (PHP + PostgreSQL/MySQL); 8,034 commits | A real, maintained open source SIS. **GPL-2.0** — the only v2 licence in this KB; it is not GPL-3.0-compatible in one direction, so keep agents external |
| Richie | https://github.com/openfun/richie | MIT | 316 | p315 | Education-portal CMS (France Université Numérique) | MIT front end over an AGPL Open edX back end — the licence-safe catalogue/portal layer |
| freelingo | https://github.com/artcc/freelingo | AGPL-3.0 | 188 | p316 | Self-hosted AI language-learning platform: CEFR study plans, AI tutor, voice, flashcards, spaced repetition; local or cloud LLMs; 1,168 commits | A complete AI-native vertical to study or fork — AGPL, so fork consciously |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 151 | p315 | Interactive content types embedded in Moodle/Open edX/Canvas | Generate H5P content JSON with an agent; the renderer stays untouched, so GPL stays contained |
| mentingo | https://github.com/Selleo/mentingo | MIT | 96 | p316 | Open-source AI-native LMS with an AI mentor and role-play, self-hostable; 1,348 commits | **The first MIT AI-native LMS in this KB** — see below |
| Sunbird | https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Portal of India's national digital-education stack | The base for an APAC public-sector engagement; see the caveat in `repos/foundations.md` |

## mentingo breaks the pattern this KB has been describing for three passes

Every pass of this KB has reported the same structure: **permissive agents, copyleft platforms, LTI
across the boundary.** `Selleo/mentingo` is an MIT-licensed, AI-native LMS with 1,348 commits — an
LMS you *can* link agent code into without a licence conversation.

Do not overstate it. 96 ★ against Moodle's 7.5k and Canvas's 6.9k is not a competitive position,
and no client is migrating off Canvas to it. Where it is genuinely useful:

- a greenfield corporate academy or bootcamp with no incumbent LMS;
- a reference implementation of what "AI-native LMS" means in code, rather than in a vendor deck;
- the one place in this sector where you can prototype deep agent/LMS coupling quickly, then port
  the lessons back across an LTI boundary for the Moodle or Canvas client.

## The licence fact that decides every engagement — unchanged, and now measured over 15

**The platform tier is copyleft; the agent tier is not.** Of the fifteen platforms above, four are
MIT (Kolibri, Richie, mentingo, Sunbird) and one is ECL-2.0 (Sakai, Apache-derived). The other ten
are GPL-2.0, GPL-3.0, LGPL-3.0 or AGPL-3.0. Against the agent tier's 13-of-15 permissive, the split
is as stark as it has been in every pass.

The consequence is concrete and identical in every region: **put Globant's agent code on the far
side of a network boundary** — LTI 1.3 tool, external service, MCP server, webhook consumer — not
inside the platform process. `pylti1.3` (MIT) is the repo that makes this practical. AGPL in
particular reaches network use of a *modified* platform, so leaving Canvas or Open edX unmodified
and talking to it over LTI keeps Globant's work separately licensed.

Two refinements from this pass:
- **RosarioSIS is GPL-2.0**, not GPL-3.0. The two are not freely interchangeable in a licence
  inventory, and GPL-2.0-only code cannot be combined with GPL-3.0 code. If a client runs
  RosarioSIS, the external-service posture is not a preference, it is the only clean option.
- **Frappe Education's licence is not shown in the GitHub sidebar.** It was read out of
  `license.txt`, which says "License: GNU GPL V3". Anyone scoping from the repo page alone will
  record it as unlicensed. It is not.

## Canvas, Project Athena, and the competitive read

Canvas LMS is verified and in the table for the first time. The strategic context matters more than
the row: **Instructure announced Project Athena on 2026-07-22** — an AI study coach grounded in the
student's own Canvas course context (assignments, deadlines, learning objectives), the first project
of its "Instructure Foundry" venture, positioned as coaching "toward mastery, not answers". It was
described as under development; one secondary report of a 7,000-student deployment at Hinds
Community College could not be confirmed against Instructure's own release and should not be
repeated to a client.

The read for a studio lead: **the incumbent LMS vendor is building exactly pattern P1 natively.**
Course-context grounding is no longer a differentiator against Canvas — it is table stakes that
Instructure will ship for free to its installed base. What Athena is not positioned to do is the
deterministic pedagogy layer (BKT, FSRS, prerequisite gating — see `tutor-mcp` in `agents/top.md`),
the governance and audit layer a US district now has to buy anyway (pattern P3), or anything
on-premise and offline (pattern P5). Sell those.

## Declared gaps

- **No LATAM-originated platform** at this tier, searched again. Public-sector LATAM deployments
  run on the platforms above (notably Kolibri). LATAM's 2026 education AI activity is venture-funded
  and closed-source — see `intel/market.md`.
- **No MENA- or Africa-originated open source platform** found, despite the region having the
  clearest named players of any this pass (Alef Education, Classera, Abwaab, EIDU). **All of them
  are proprietary.** That is a finding, not an absence: in MEA the open source story is deployment
  of global platforms, and the AI layer is commercial.
- **Blackboard/Anthology and D2L Brightspace are closed source** and so correctly absent, but they
  are LMS incumbents a client may be running. Integration is LTI 1.3 either way.
