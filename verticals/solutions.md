---
industry: education
region: Global
updated: 2026-10-19
---

# Vertical platforms — education

**Pass 317 · 2026-10-19.** Sixteen platforms — the real systems a client is already running, or
would run, with AI built on top. **Checked** says which pass took the licence/star reading.

**New this pass: OpenOLAT, Apache-2.0, 31,877 commits** — and it materially weakens the
"every LMS is copyleft" rule this KB has stated in every pass. Moodle, Open edX and Sakai were all
re-verified first-hand. Detail below the table.

| Platform | Repo | Licence | ★ | Checked | What it is | AI-on-top angle |
|---|---|---|---|---|---|---|
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.2k | p315 | Web conferencing purpose-built for virtual classrooms | Post-session agents: transcription, participation analytics, summary-to-LMS |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | p317 | LMS + Studio behind large-scale MOOCs and corporate academies; 68,824 commits. The older `openedx/edx-platform` URL redirects here | Agents as XBlocks or LTI tools; AGPL makes the network boundary non-negotiable |
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.5k | p317 | The world's most deployed open source LMS; 123,234 commits | Build as a Moodle plugin or an external tool over LTI 1.3; never link AI code into the core |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | p316 | The open LMS by Instructure; 78,765 commits | **Verified this pass, closing a declared gap.** Same AGPL discipline as Open edX — and see the Project Athena note below |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | p317 | Learning, teaching, research and collaboration platform used in higher ed; 55,483 commits | ECL-2.0 is an Apache-2.0 derivative with an academic-attribution twist — the most permissive LMS core here |
| OpenOLAT | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | 448 | p317 | Web-based LMS for teaching, learning, assessment and communication; a modular course-authoring toolkit. 31,877 commits; built by frentix GmbH from the University of Zurich's OLAT 7.1 | **The most permissively licensed mature LMS in this KB.** Agent code can link directly — no LTI boundary required. See below |
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

## OpenOLAT is the real crack in the copyleft-platform rule — and it was missed for a measurable reason

`Selleo/mentingo` (MIT, 96 ★) was recorded last pass as the first counter-example to this KB's
permissive-agents / copyleft-platforms thesis, with the honest caveat that 96 ★ changes no
engagement. **`OpenOLAT/OpenOLAT` is a much stronger counter-example: Apache-2.0 with 31,877
commits** — a mature, institution-grade LMS, not a promising young project.

It is a web-based LMS for teaching, learning, assessment and communication, developed by
**frentix GmbH (Switzerland) since 2011**, based on the **OLAT 7.1** release from the
**University of Zurich**. That provenance makes it the only **EMEA-authored, EMEA-maintained,
permissively licensed LMS** in this KB — which lands directly on the standing EMEA requirement for
sovereign, in-region education infrastructure (see `intel/market.md`).

**Read the licence file, not the sidebar.** The GitHub sidebar shows a bare "License" link with no
name; the README badge reads Apache 2.0. The `LICENSE` file is the full Apache License 2.0 text
followed by two provenance statements — one crediting "the Multimedia & E-Learning Services … 
originally created by the OLAT Zentrum at the University of Zurich", one crediting the OpenOLAT
community and frentix GmbH. **These are attribution/provenance notices in the NOTICE tradition, not
additional licence terms**, so the grant is Apache-2.0. Record it that way in a licence inventory,
and cite the file rather than the page — this is the third repo in this KB (with Frappe Education
and `education-agent-skills`) whose real licence is invisible from the repository page.

**Why 316 passes missed it: 448 stars.** This is the same lesson pass 316 drew from Ed-Fi (12 ★)
and Sunbird (41 ★), and it now has three independent confirmations. A 31,877-commit LMS used across
European universities carries fewer stars than a 76-commit tutor demo, because institutional
software is adopted through procurement, not GitHub. **A star-ranked search cannot see this
sector's real infrastructure.** Pass 318 should assume the remaining gaps are search-method
artefacts until proven otherwise.

**What it changes commercially.** For a greenfield or EMEA-sovereign engagement, OpenOLAT is the
one real LMS where the architectural tax this KB charges in every pattern — agent code on the far
side of an LTI boundary — is **optional**. You can link agent code into the platform, ship one
deployable, and skip the bridge. For a client already on Moodle or Canvas it changes nothing: the
LTI posture still applies. See **P8** in `compose/patterns.md`, new this pass.

Do not oversell it. 448 ★ against Moodle's 7.5k is not market share, the project is
Swiss-German-speaking in its documentation centre of gravity, and no client is migrating off Canvas
to it. It is a *starting point*, and the first one in this sector that is both mature and
licence-clean.

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

**The platform tier is copyleft; the agent tier is not — but the margin narrowed this pass.** Of the
sixteen platforms above, four are MIT (Kolibri, Richie, mentingo, Sunbird), **one is Apache-2.0
(OpenOLAT)** and one is ECL-2.0 (Sakai, Apache-derived). The other ten are GPL-2.0, GPL-3.0,
LGPL-3.0 or AGPL-3.0. So **6 of 16 platforms are now permissive**, against the agent tier's
13 of 16. The split is still real and still dictates architecture, but "the platforms are all
copyleft" is no longer an accurate sentence, and with OpenOLAT it is no longer accurate at
*institutional scale* either.

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
