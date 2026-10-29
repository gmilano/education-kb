---
industry: education
region: Global
updated: 2026-10-29
---

# Education Verticals — Real Platforms to Build AI On

**Pass `p534` · 2026-10-29.** Every platform below is a real, running system that
institutions already operate, with its licence read from **the licence file's own
title block** over `raw.githubusercontent.com`. 🟢 **The parenthesis this header
carried for two passes — "`github.com` returns HTTP 403 through the session
proxy" — is corrected: `github.com` HTML is 403 to `curl` and **200 through
WebFetch**, so archive state, star counts and org listings are readable after
all** ([`../evidence/channel-asymmetry.2026-10-29-p534.tsv`](../evidence/channel-asymmetry.2026-10-29-p534.tsv)).
🔴 **That correction immediately earned its keep on this page:** it is how
`p534` found that the AI agent layer of a platform filed here three times was
**archived seven days ago** — see §7. The question this file answers is not
"what exists" but **"where does the AI attach, and what does the licence let us
ship?"**

Odoo is to ERP what Moodle is to learning: the thing you customise rather than
replace. In education the equivalents are below, grouped by the institutional
function they own.

## 1. Learning delivery (LMS)

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ | The **plugin API** (local, block, mod, qtype plugins) plus the AI subsystem introduced in the 4.5 line. A GPL plugin living in-tree is the lowest-friction attachment anywhere in this sector, and the plugin directory gives distribution for free. Keep the model-serving side in a separate permissive service and call it over HTTP. 🔴 **The MCP route is not available off the shelf** — but ⚠️ **`p528` corrects why.** It is not that nobody built one: **eleven independent codebases exist, ten of them MIT**, the field tops out at **27★** and sums to **37★ in total**, and no two agree on a tool vocabulary. The most-visible option is still AGPL-3.0. 🟢 So for a client engagement there *is* permissive prior art to consolidate — see the census in [`../repos/foundations.md`](../repos/foundations.md) and **P553**. 🔴 For a deployment today, the plugin boundary is still the seam. |
| **Open edX** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 · 8.2k★ | **XBlocks** for new interactive component types, and **Tutor plugins** ([overhangio/tutor](https://github.com/overhangio/tutor), AGPL-3.0 · 1.1k★) for deployment-level changes. Never fork the platform; an XBlock plus a Tutor plugin covers almost every ask. |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 · 6.9k★ | **Do not fork.** Attach over **LTI 1.3 + the Canvas REST API**, or via MCP — [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT · 308★, v1.16.0 Oct 2026) already exposes Canvas to assistants and is **the fastest credible LMS-agent demo available in this sector, for any platform.** |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** · 7.0k★ | Fork it. Its explorations model — branching lesson states with feedback at each step — is the closest thing in open source to a structure an agent can author *into* rather than around. The permissive licence makes it the default when the client wants to own the product. |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · 1.0k★ | Plugin system. Chosen for ease of use and accessibility over feature depth — the right call for LATAM and francophone public deployments with thin IT staff. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 · 505★ | Plugin slots. Non-profit society governance is the selling point for EU public-sector procurement, where provenance of the code is itself a requirement. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · 449★ | Fork it. Swiss-origin, Apache-2.0, assessment built in — **the best EMEA base when the deliverable must include proprietary extensions.** |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** · 1.2k★ | Tool-level extension. Title block confirms ECL-2.0 — Apache-2.0 with an academic patent-grant tweak, so this behaves as permissive. Higher-ed and research collaboration focus. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 · 3.4k★ | Frappe apps and hooks. Pick it when the institution already runs Frappe/ERPNext, so learning and administration share one data model — but see the Frappe Education row below: **the two Frappe apps are not under the same licence.** |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** · 101★ | Fork it. An **AI-native LMS** — AI mentor and role-play are in the product, not bolted on. 101★ means early, but it is the only MIT full LMS-with-agent on this shelf and it skips the retrofit problem entirely. |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** · 1.2k★ | Fork it. **Offline-first** — the deciding platform wherever connectivity is intermittent. Pair it with a small local model; a cloud-only tutor is not deployable in the contexts Kolibri exists to serve. |
| ⚠️ **Lumen** | [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | 🆕 **GPL-3.0** · 91★ | **Read, do not ship.** A "learner-owned" platform: private courses built from a goal, course-scoped RAG with citations, BYOK model keys, moderated catalogue — a genuinely good product shape, and the author is in **Essen, Germany (EMEA)**. 🔴 But the **README badge says MIT and the licence file says GPL-3.0** (see the trap table in [`../agents/top.md`](../agents/top.md)). Strong copyleft. Borrow the two-role architecture; do not fork it into a proprietary deliverable. |

## 2. Administration (SIS / ERP)

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| 🆕 **GegoK12** | [Gego-K12/gegok12](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** · 54★ | Fork it. A Laravel school-management system, **API-first with mobile app support** by its own description — admissions, records, the administrative spine of a K-12 institution. 🟢 **The second permissive SIS/school-management system on this file**, after `p530` retracted this base's published "zero permissive SIS" non-finding with `academico-sis/academico` (MIT, 409★). 🔴 **And its grant is readable only at source:** the GitHub page links a `License` file *without naming the licence*, so a page-scraping probe records `unknown`; the title block reads `MIT License` with an `SPDX-License-Identifier: MIT` comment (1 150 B, `b8694396d7dc`). 🟡 54★ and a thin README — fork-and-own, not depend-on. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 · 900★ | Odoo modules (branch `19.0`): admissions, timetabling, attendance, fees, library. **This is the literal Odoo-for-education answer** — and the Odoo module boundary is a clean, well-documented place for an agent to act on records. |
| 🔵 **Frappe Education** | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** — *resolved this pass* · 685★ | "Open source education / school management system", the administration counterpart to Frappe LMS on the same stack and the same hooks. **`p526` could not grade it** — the page renders no licence type. Read directly this pass: `license.txt` says `License: GNU GPL V3`. 🔴 **Plan for the mismatch:** Frappe LMS is **AGPL-3.0**, Frappe Education is **GPL-3.0**. One stack, two copyleft regimes — a single deliverable touching both inherits both sets of obligations, and the AGPL §13 network clause is the one that bites a hosted engagement. |
| **i-educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 · 722★ | REST/DB integration. Brazil's largest free school-management system, born in **Itajaí (SC)** municipal government, on the federal Public Software Portal since 2008. For Brazilian public-sector work this is the incumbent, not an option. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 · 648★ | Module system + PostgreSQL. Strong ES/FR/PT localisation; common in small and mid-size schools. |
| ⚠️ **Advising App** | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | **Elastic-2.0** · 340★ | **Reference only — do not build on it.** AI advising and recruitment CRM for colleges; Elastic-2.0 prohibits offering it as a hosted service, which is the engagement shape. Read it for its data model (advising notes, engagement signals, outreach journeys), then build that model yourself. |
| 🔴 🆕 **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | ⛔ **NO GRANT** · 347★ · 288 forks | 🔴 **Do not build on it, and do not believe the table that says you can.** Marketed on its own page as a *"commercial grade, secure, scalable"* Student Information System, and a widely-cited third-party comparison lists it as **GPL-2.0**. `p529` probed it both ways: the GitHub API returns **no `license` key**, and ⛔ **no licence file exists at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE` or `COPYING` on `master`**. Default copyright applies. This is `tosuki/moodle-mcp`'s failure mode at **347 stars and 288 forks** — and the first time this base has caught a *secondary source asserting a grant the repository does not carry*. |

### 🆕 The SIS gap, measured rather than declared (`p529`)

This base has carried *"no SIS or advising agent under a permissive licence"* as
a declared gap for several passes. 🟢 **It is now a measurement.** Query:
`student information system school management in:name,description stars:>40`,
sorted by stars — **the global field at that threshold is four addresses**:

| Address | Grant | ★ | State |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** (API + title block) | 648 · 394 forks | 🟢 alive — pushed 28 Oct 2026 |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | ⛔ **no grant** | 347 · 288 forks | 🟢 alive — pushed 26 Oct 2026 |
| [`xrandx/Student-Information-Management-System`](https://github.com/xrandx/Student-Information-Management-System) | 🔴 AGPL-3.0 | 107 | ⛔ a university course project, last pushed **2021** |
| [`OPTIMUM-LINKUP/Latest-Optimum-School-System`](https://github.com/OPTIMUM-LINKUP/Latest-Optimum-School-System) | 🔴 GPL-3.0 | 83 | ⛔ dead — last pushed **2017** |

🔴 **Zero permissive in that sample** — and 🟢 **`p530` found the field's
permissive member, which that query could not see.** See
[§ `p530`: the permissive SIS exists](#-p530-the-permissive-sis-exists-and-this-base-has-owned-it-since-p108)
below before acting on the paragraph that follows. Of the four above: two are
dead, one is ungranted, and the one live grantable system is GPL-2.0. Adding the
ERP layer does not rescue it:
**OpenEduCat is LGPL-3.0**, **Frappe Education GPL-3.0**, **i-educar GPL-2.0**,
**Advising App Elastic-2.0**. A targeted check of the one permissive claim in
circulation — a vendor table listing **Fedena as Apache-2.0** — found that
`foradian/fedena` ⛔ **404s on `main` and `master`**; unverifiable at that address.

🔵 **What this means for an engagement, stated as a decision rather than a lament.**
The records layer of education is **structurally copyleft**, and unlike the LMS
layer it has no `Kolibri` and no `OpenOLAT` to escape to. So do not plan to fork
a SIS. **Plan to sit beside one**: the agent stays permissive and out-of-process,
reads and writes over REST/SQL, and the copyleft core is deployed unmodified.
That is the same architectural conclusion the LMS section reaches, arrived at
from a field with *no* permissive option at all — which makes it the stronger
version of the rule, not a weaker one.

## 3. Synchronous classroom

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **BigBlueButton** | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 · 9.3k★ | Recording and transcript pipeline, plus the LMS integrations it already ships. README names **BBB 4.0**. Post-session summarisation, participation analytics and follow-up generation all hang off the recording artefacts — no core changes needed. |
| **Apache OpenMeetings** | [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** · 688★ | Fork-friendly conferencing when the licence must be permissive end to end. Smaller community than BBB; take it only when LGPL is genuinely blocking. |

## 4. Content, assessment and records

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **H5P** | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ | **Generate H5P, not HTML.** It is the one interactive-content format that travels across Moodle, Canvas, Open edX and Drupal, so authoring agents that emit H5P produce portable output instead of platform lock-in. Grant lives at `LICENSE.txt`. |
| **Ralph (LRS)** | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ | **The analytics seam.** An **xAPI** Learning Record Store from France Université Numérique. Every agent interaction — hint given, mastery gate passed, misconception detected — becomes a standard statement here instead of a private log. This is what makes "did the AI help?" an answerable question later. |
| **Dolos** | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** · 355★ | Assessment integrity for programming work, from **Ghent University** (`dolos@ugent.be`, read from the licence file). Deliberately not an LLM: a similarity finding has to survive an academic appeal, and "the model thought so" does not. |
| **TAO** | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 · 64★ | QTI-standard computer-based assessment. The right base when items must interoperate with national testing infrastructure. |
| 🆕 **lineage-skill** | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** · 462★ | **The authoring seam, and it is permissive.** Turns course video, audio, PDF, transcripts and notes into a **source-backed** teaching Skill: short lessons, comprehension checks, feedback, review tracking. 70 forks. Apache-2.0 means the output pipeline can be shipped; "source-backed" means a generated lesson can be traced to the material it came from, which is what makes it defensible in the governance conversation. Pair with H5P for portability. |
| 🆕 **AI_AWE** | [wwrwbs/AI_AWE](https://github.com/wwrwbs/AI_AWE) | Apache-2.0 · 2★ | Automated essay scoring: Qwen classifier + LightGBM scorer + feedback generator, Gradio UI, vLLM-served. Two stars — a reference, not a dependency. ⚠️ A search result attributed the arXiv **ArguLens** paper to it; the repo mentions **neither ArguLens nor any arXiv paper**. Unverified, do not repeat. |

## 5. Retention layer

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **Anki + anki-mcp-server** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** · 538★ | The agent teaches; Anki makes it stick. An MCP server means any assistant can write cards into the learner's **own** deck, which survives the end of the engagement. README version **0.27.0**. |
| **FSRS** | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** · 4.1k★ | Modern spaced-repetition scheduler. Use it instead of inventing a review interval — the scheduling problem is solved and the solution is permissive. |

### 🆕 `p530`: the permissive SIS exists, and this base has owned it since `p108`

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** (title block, `main`) | **409★ · 150 forks · pushed 2026-10-28.** Laravel + Filament school-management platform for small and medium institutions; topics name it a `student-information-system`. 🟢 **The only permissive records system this base has verified.** Filament is an admin-panel framework, so an agent attaches as a Filament page or a Laravel command inside the app — **no out-of-process sidecar required**, because the grant permits modification and redistribution. |

🔴 **Why `p529`'s query could not return it.** Academico calls itself a *"school
management platform"*; the phrase *"student information system"* appears only in
its **topics**. `in:name,description` is structurally blind to that.
`topic:student-information-system stars:>40` returns it second, behind
RosarioSIS. 🔵 **Recorded as shelf rule 12** on
[`../agents/top.md`](../agents/top.md): a single query's `total_count` is a
sample size, not a field.

🟢 **What changes for an engagement.** The *"do not fork a SIS, sit beside one"*
rule above was derived from a field with **no** permissive option. That premise
is now false for one address. So there are two plays, not one:

| | When | Architecture |
|---|---|---|
| **Sit beside it** | The institution already runs RosarioSIS, openSIS, i-educar or a vendor SIS | Agent stays permissive and **out-of-process**, reads/writes over REST/SQL, copyleft core deployed unmodified. Unchanged, and still the common case. |
| 🆕 **Build inside it** | Greenfield, or a small/medium institution with no incumbent | Start from **Academico (MIT)** and add the agent **in-process** as Filament pages. 🟢 The whole stack stays permissive and shippable. |

🔴 **The gap that survives, restated precisely.** There is now a permissive SIS;
there is still **no agent that speaks to any SIS**. The Moodle and Canvas bridge
fields have dozens of entries, and crossing `topic:student-information-system`
with MCP returns nothing. 🔵 **That is this pass's cleanest greenfield** — and
with Academico it can be built permissively end to end. See **P559** in
[`../compose/patterns.md`](../compose/patterns.md).

### 🆕 `p530`: the permissive AI-native LMS, and four institutional platforms

All promoted off [`../evidence/address-ledger.tsv`](../evidence/address-ledger.tsv)
— owned by this base, never filed — and re-verified on two channels this pass.

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| 🆕 **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **101★ · 31 forks · pushed 2026-10-29 during this pass.** "Open-source AI-native LMS with AI Mentor & role-play", positioned as a self-hosted alternative to Moodle, Docebo and Open edX. Ships **SCORM** and **xAPI** topics, so it speaks the standards layer on [`../repos/foundations.md`](../repos/foundations.md). 🟢 **EMEA** (Selleo, Poland). 🔴 **The only permissive AI-native LMS this base has found** — every rival with more traction is AGPL-3.0 (`frappe/lms` 3 353★, `learnhouse` 2 430★, `courselit` 1 290★, `freelingo` 213★). The AI is already the product; what attaches is *your* domain content and model routing. |
| 🆕 **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** | **823★ · 395 forks · branch `develop` · pushed 2026-10-29.** "Interactive Learning with Automated Feedback", from TU München's `ls1intum` chair — exam mode, autograding, programming exercises. 🟢 **EMEA, stated institutional origin.** A permissive, production-grade assessment platform: the agent attaches as a feedback generator behind the existing autograder rather than replacing it. |
| 🆕 **Opencast** | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 **ECL-2.0** | **509★ · 260 forks · branch `develop`.** Automated lecture capture and video distribution at scale, run by a university consortium. ECL-2.0 is Apache-2.0 with a narrowed patent clause — **permissive, and not a trap**. 🟢 Where transcription, chaptering and lecture-derived material attach: it is the source of the content a tutoring agent should be grounded in. |
| 🆕 **UniTime** | [UniTime/unitime](https://github.com/UniTime/unitime) | 🟢 **Apache-2.0** | **356★ · 214 forks.** Comprehensive university course timetabling, exams and student scheduling (Apereo). 🔵 Scheduling is a **constraint-solving** problem, not a generative one — the honest AI attachment is natural-language intent capture and explanation on top of the existing solver, not a model asked to build a timetable. |
| 🆕 **Numbas** | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | **215★ · 129 forks.** Fully browser-based e-assessment for mathematics, with a computer-algebra system; from **Newcastle University** (🟢 EMEA, named in its own topics). Exports SCORM. 🔵 The CAS matters: it marks mathematical equivalence rather than string matches, so it is the component that makes an AI maths tutor *gradeable*. |
| 🆕 **Richie** | [openfun/richie](https://github.com/openfun/richie) | 🟢 **MIT** | **317★ · 94 forks · branch `master`.** Django + React CMS for education portals, from France Université Numérique (🟢 **EMEA**). The catalogue and marketing front end that sits in front of an LMS — where AI attaches is course discovery and recommendation, not delivery. |
| 🆕 **Sunbird Ed** | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🟢 **MIT** | **41★ and 317 forks — a 7.7:1 fork-to-star ratio.** The web portal of India's national education stack (🟢 **APAC**). 🔴 **This base ranks by stars and this row is the argument against that:** 317 forks on an MIT national platform is deployment, where 41 stars reads as obscurity. 🟡 Pushed **2026-02-21**, eight months quiet — verify liveness before proposing it. |

🟡 **One row deliberately not promoted.**
[`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) is **MIT**
(the API said `NOASSERTION`) at **980★** — and **pushed 2025-12-09**, eleven
months stale. 🔵 A dormant 980★ LMS is a **migration source**, not a platform to
build on.

### 🆕 `p531`: the platforms the rewrites dropped — assessment, polling, and the computational classroom

🔴 **Four real, running platforms were in an `archive/` snapshot of this file's
neighbours and nowhere in the live corpus.** They came back from `Gap 530-A`'s
triage of the **349** dropped addresses, grant read first-hand from the licence
file's title block.

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| 🆕 **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** · 823★ | **Fork it, or extend it.** TU München's interactive-learning platform: programming, modelling, text and quiz exercises with **automated assessment built in**, plus a proctored exam mode, in production across European universities. 🟢 **The best EMEA base when the deliverable is assessment and must include proprietary extensions** — MIT, 395 forks, pushed today. The AI attaches as a feedback generator *behind* the existing assessment pipeline, not as a new one. Deploy with [`artemis-ansible-collection`](https://github.com/ls1intum/artemis-ansible-collection) (MIT). 🔵 Compare OpenOLAT above: OpenOLAT is the broader LMS, Artemis is the deeper assessment engine. |
| 🆕 **JupyterHub + spawners** | [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | **BSD-3-Clause** · 611★ | **Configure it, never fork it.** The computational-course platform: one notebook server per student, spawned into Kubernetes, authenticated **out of the LMS over LTI** with [`ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (BSD-3-Clause). The AI attaches inside the student's own kernel, where it can see the code they actually wrote. 🔴 The official deployment tutorial is **archived** — budget your own runbook. Full family in [`../repos/foundations.md`](../repos/foundations.md). |
| 🆕 **abstimmbar** | [virtUOS/abstimmbar](https://github.com/virtUOS/abstimmbar) | **Apache-2.0** · 2★ | **Fork it.** An audience-response system for universities — live quizzes and polls, anonymous participation by QR or short code, **LTI 1.3 and OIDC**, and self-hostable AI helpers already in the design. From virtUOS (Universität Osnabrück), successor to Cliqr. 🟡 2★ means early; Apache-2.0 plus LTI 1.3 plus a named institutional owner means it is the cleanest *lecture-hall* attachment point in EMEA, and the in-room data it produces is the signal a tutor agent otherwise has to guess. |
| 🆕 **paper-lms** | [EduThemes/paper-lms](https://github.com/EduThemes/paper-lms) | **MIT** · 6★ | **Read it, then decide.** An LMS in Go that is *"fully backwards compatible with Canvas-LMS"*, built for low-cost hosting and easy modification, with LTI and IMSCC import. 🟢 **The only permissive escape route from an AGPL-3.0 Canvas deployment this base has found** — which is the architecture question Canvas forces. 🟡 6★ and 16 open issues: a migration *target* to evaluate, not a platform to promise. |

🟡 **One negative worth the row it is not getting.**
[`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) — Apache-2.0,
**582★**, a free open-source programming-education platform from **Brazil** — is
**archived by its owner**. 🔵 It is a migration source and a design reference
for a LATAM engagement, not a platform to build on, and the star count is
exactly why a reader would otherwise reach for it.

### 🆕 `p533`: the autograder layer, the student front door, and the AI layer Artemis ships separately

🔴 **The correction that matters most on this page.** `p530` and `p531` both
filed [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) and both wrote
that *"the agent attaches as a feedback generator behind the existing
autograder."* **TU München already built that agent and ships it as a separate
MIT repository**, and no row here pointed at it. Registered as `Gap 533-A`.

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| 🆕 **EduTelligence** (Artemis's own AI layer) | [ls1intum/edutelligence](https://github.com/ls1intum/edutelligence) | 🟢 **MIT** · 17★ | **Do not build this — mount it.** The three microservices TU München runs behind Artemis: **Iris** (tutor; reads submitted code, assessment feedback *and build logs*), **Athena** ((semi-)automated assessment for text and programming exercises at large-course scale), **Atlas** (competency-model generation and learning-activity recommendation, stated as *"adaptable to other LMSs"*). 🟢 **The version-compatibility matrix is the reason to trust it** — 21 rows, current through Artemis `10.2.x`. 🔵 **Atlas is the piece worth lifting on its own**: it is the only competency-modelling service on this page, and its own README says it is not Artemis-specific. |
| 🆕 **Autolab** | [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** · 808★ | **Fork it.** Carnegie Mellon's course-management service for **auto-graded programming assignments** — the North American counterpart to Artemis, permissive, Rails, with container-isolated grading. 🟢 **The autograding layer this page had no row for.** The agent attaches as the *explainer* of an autograder verdict the student already received, which is the highest-value and lowest-risk attachment in assessment: the grade stays deterministic, the explanation is generated. |
| 🆕 **Judge0** | [judge0/judge0](https://github.com/judge0/judge0) | 🔴 **GPL-3.0** · **4,498★** | **Deploy it beside the product, never inside it.** The field's default sandboxed code-execution service — 942 forks, and its own topics claim `ai-agents`/`ai-agent-tools`. 🟢 **The licence reasoning, stated because it decides the architecture:** GPL-3.0 has no §13, so a proprietary deliverable calling Judge0 over HTTP as a **separate self-hosted service** does not inherit the grant — where an AGPL-3.0 component in the same position would. Any agent that runs, tests or grades student code needs this layer; this is how to use it without contaminating the deliverable. |
| 🆕 **uPortal** | [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** · 287★ | **Configure it.** Apereo's higher-education portal — the authenticated **front door** that aggregates LMS, SIS, timetable and announcements into one student surface. 🔵 Nothing else on this page holds that position. When the engagement's ask is *"one place where the student sees everything, and an assistant inside it"*, the assistant belongs here as a portlet, with the LMS bridges on [`../agents/top.md`](../agents/top.md) behind it. |
| 🆕 **ClassroomIO** | [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** · **1,735★** | ⛔ **Do not fork, and this row exists as the contrast to Judge0 above.** *"Intelligent Customer Training Platform"* — SvelteKit + Supabase, 409 forks, pushed during this pass. 🔴 **AGPL-3.0 §13 reaches users who interact over a network**, which is exactly the hosted shape a studio engagement delivers, so the grant follows the deliverable. The capability — courses, assignments, a classroom — is real and well-starred; the architecture answer is to integrate over its API or to choose Mentingo (MIT) instead. |

## 🆕 6. Offline-first delivery — the deployment context most of this file assumes away (`p532`)

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| 🆕 **Project NOMAD** | [Crosstalk-Solutions/Project-NOMAD](https://github.com/Crosstalk-Solutions/Project-NOMAD) | 🟢 **Apache-2.0** · 🔴 **41.3k★** | Fork it, or deploy it as-is and attach. A **self-contained, offline-first knowledge and education server** — *"Knowledge That Never Goes Offline"* — that bundles content, tooling **and a local AI assistant** onto one Debian/Ubuntu box (≈5 GB disk, <1 GB RAM for the server itself; the offline corpus is what fills a drive). Terminal-based install, no cloud dependency at run time. |

> 🟢 **Why this row changes the shape of the file.** Every other platform here
> assumes connectivity; **Kolibri** (MIT, 1.2k★) was this base's only
> offline-first answer, and its own section says *"a cloud-only tutor is not
> deployable in the contexts Kolibri exists to serve."* NOMAD is the **server
> side of that same argument, with the model included and an Apache-2.0 grant**,
> at **41.3k★** — thirty-four times Kolibri's star count. 🔵 Pair them: Kolibri
> for the learner-facing curriculum and progress model, NOMAD for the box it all
> runs on plus the local assistant. That pairing is the deciding architecture for
> **LATAM** rural and **Africa** deployments, and it is also the honest answer
> whenever a client's connectivity assumption is weaker than a demo's.
>
> 🔴 **It was unfiled for 11 passes.** NOMAD came off `p532`'s ranked promotion
> queue, not off a search — this base had described it eleven separate times and
> filed it nowhere. 🟡 **No location stated** on the page or in the README, so it
> is unplaced; `Crosstalk-Solutions` as an org name is not evidence of a country.

## 🆕 `p534` — §7, liveness of the attachment point: the thing a licence cell cannot say

A platform row answers *"where does the AI attach?"*. 🔴 **It does not say
whether the attachment point is still maintained**, and this pass found two
cases where that is the whole answer.

| Attachment point | Platform it attaches to (filed here) | State read 2026-10-29 | What to do instead |
|---|---|---|---|
| 🔴 [`frappe/flow_client`](https://github.com/frappe/flow_client) — *"Frappe Flow: native AI agents, tools and triggers for Frappe"*, **AGPL-3.0**, **89★** | [`frappe/education`](https://github.com/frappe/education) (GPL-3.0), [`frappe/lms`](https://github.com/frappe/lms) (AGPL-3.0), [`frappe/frappe`](https://github.com/frappe/frappe) | 🔴 **`Public archive` as of 2026-10-22** — default branch `develop`, grant at `license.txt` | 🟢 **Build on the Frappe REST API**, not on Flow. The platform rows are unaffected; the agent layer has no upstream and must be treated as the studio's own code |
| 🔴 [`openedx/openedx-ai-extensions`](https://github.com/openedx/openedx-ai-extensions) — *"plugin for housing tools and helpers for working with AI"*, **AGPL-3.0**, 17★ | [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) (AGPL-3.0), [`openedx/XBlock`](https://github.com/openedx/XBlock) (**Apache-2.0**) | 🟢 Live, pushed 2026-10-05 — 🔴 **but copyleft** | 🟢 Attach behind an **XBlock** (Apache-2.0) or an **LTI** boundary. 🔴 Vendoring this plugin pulls AGPL §13 into a hosted deliverable — and the trap is that `XBlock` being Apache-2.0 makes "extend Open edX with AI" *read* permissive |

🔵 **The general rule for this file, which it did not previously state:** the
licence governs what you may ship, and the **archive flag governs whether
anyone will fix it**. A permissive-but-dead attachment point is worse for a
client than a copyleft-but-maintained one, because the second is an
architecture decision and the first is an unbudgeted maintenance transfer. 🟢
Both flags are now readable on the same channel, so every platform row on this
page should carry a liveness read — not yet done for the 30-plus rows above
→ `Gap 534-G`.

### 🟢 And one attachment point that *gained* an upstream: the US K-12 data plane

[`Ed-Fi-Alliance-OSS`](https://github.com/Ed-Fi-Alliance-OSS) — the alliance
governing the **Ed-Fi Data Standard** that US state education agencies move
student records on, already filed here through
[`Ed-Fi-Alliance-OSS/data-management-service`](https://github.com/Ed-Fi-Alliance-OSS/data-management-service)
and [`edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) —
ships **two Apache-2.0 AI repositories** that no page here held:
[`Fiona`](https://github.com/Ed-Fi-Alliance-OSS/Fiona) (an AI assistant for the
Ed-Fi community) and
[`AI-Tools-for-Ed-Fi-SDLC`](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC)
(prompts, skills, hooks and agents for the Alliance's own SDLC). 🔵 **Both are
0★ and both are Apache-2.0** — which makes the *data plane*, not the LMS, the
newest permissive attachment surface on this page, and the only one whose
upstream is a standards body rather than a vendor.

## The architecture this implies

1. **Never fork an AGPL core.** Attach over LTI 1.3, REST, xAPI or MCP.
2. **When a fork is genuinely needed, fork a permissive core:** Oppia,
   OpenOLAT, Sakai, Kolibri or Mentingo.
3. **Emit standard artefacts** — H5P for content, xAPI into Ralph for events,
   QTI for items. Standard output is what survives the next platform migration.
4. **Keep the model layer in a separate permissive service.** The licence of the
   platform then constrains the integration only, never the intelligence.
5. 🆕 **Check the licence per app, not per vendor.** Frappe LMS (AGPL-3.0) and
   Frappe Education (GPL-3.0) are the same stack under different regimes, and a
   README badge can disagree with the grant it links to (Lumen). Read the licence
   file's title block before the architecture depends on it.
   🆕 **And check it per *layer* too:** `frappe/frappe`, the framework under both,
   is **MIT**, so the copyleft lives in the apps and not in the platform.
6. 🆕 **GPL-3.0 and AGPL-3.0 are not the same architectural constraint.** A
   GPL-3.0 component (**Judge0**) can be deployed as a separate network service
   that a proprietary deliverable calls, because GPL-3.0 has no §13. An
   AGPL-3.0 component (**ClassroomIO**, Open edX, Canvas, Frappe LMS) in the
   same position pulls its grant onto the deliverable. 🔴 This base had been
   collapsing both into "copyleft — integrate, do not fork", which is right
   about AGPL and needlessly expensive about GPL.
7. 🆕 **Before building an AI layer for a platform, check whether the platform's
   own maintainers already ship one — in another repository.** Artemis and
   EduTelligence are one institution and two addresses; filing the platform said
   nothing about the agents. See `Gap 533-A`.
