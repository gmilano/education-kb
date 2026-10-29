---
industry: education
region: Global
updated: 2026-10-29
---

# Education Verticals — Real Platforms to Build AI On

**Pass `p527` · 2026-10-29.** Every platform below is a real, running system that
institutions already operate, with its licence read this pass from **the licence
file's own title block** (`raw.githubusercontent.com` is reachable while
`github.com` returns HTTP 403 through the session proxy). The question this file
answers is not "what exists" but **"where does the AI attach, and what does the
licence let us ship?"**

Odoo is to ERP what Moodle is to learning: the thing you customise rather than
replace. In education the equivalents are below, grouped by the institutional
function they own.

## 1. Learning delivery (LMS)

| Platform | Repo | Licence | Where AI attaches |
|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ | The **plugin API** (local, block, mod, qtype plugins) plus the AI subsystem introduced in the 4.5 line. A GPL plugin living in-tree is the lowest-friction attachment anywhere in this sector, and the plugin directory gives distribution for free. Keep the model-serving side in a separate permissive service and call it over HTTP. 🔴 **The MCP route is not available off the shelf:** the whole Moodle-MCP field tops out at **27★** and the most-visible option is AGPL-3.0 — see the lineage table in [`../repos/foundations.md`](../repos/foundations.md). For Moodle, the plugin boundary *is* the seam today. |
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
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 · 900★ | Odoo modules (branch `19.0`): admissions, timetabling, attendance, fees, library. **This is the literal Odoo-for-education answer** — and the Odoo module boundary is a clean, well-documented place for an agent to act on records. |
| 🔵 **Frappe Education** | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** — *resolved this pass* · 685★ | "Open source education / school management system", the administration counterpart to Frappe LMS on the same stack and the same hooks. **`p526` could not grade it** — the page renders no licence type. Read directly this pass: `license.txt` says `License: GNU GPL V3`. 🔴 **Plan for the mismatch:** Frappe LMS is **AGPL-3.0**, Frappe Education is **GPL-3.0**. One stack, two copyleft regimes — a single deliverable touching both inherits both sets of obligations, and the AGPL §13 network clause is the one that bites a hosted engagement. |
| **i-educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 · 722★ | REST/DB integration. Brazil's largest free school-management system, born in **Itajaí (SC)** municipal government, on the federal Public Software Portal since 2008. For Brazilian public-sector work this is the incumbent, not an option. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 · 648★ | Module system + PostgreSQL. Strong ES/FR/PT localisation; common in small and mid-size schools. |
| ⚠️ **Advising App** | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | **Elastic-2.0** · 340★ | **Reference only — do not build on it.** AI advising and recruitment CRM for colleges; Elastic-2.0 prohibits offering it as a hosted service, which is the engagement shape. Read it for its data model (advising notes, engagement signals, outreach journeys), then build that model yourself. |

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
