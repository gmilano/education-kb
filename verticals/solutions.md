---
industry: education
region: Global
updated: 2026-10-11
---

# Education — vertical platforms you can customise

**Pass 130, 2026-10-11.** Full rewrite. This page answers one question: *the client runs X — where
does AI attach, and what does the licence let us ship?* Repo-level verification lives in
`repos/foundations.md`; this page is about the attachment, the integration standard and the
constraint.

## The attachment points, before the platforms

Four ways to put AI into an existing education platform, in increasing order of coupling:

1. **LTI 1.3 / LTI Advantage** — the external tool is launched from inside the LMS with signed
   identity and grade passback. Touches no platform source, so **no copyleft reciprocity at all**,
   and works across Moodle, Canvas, Open edX, Sakai, Blackboard, D2L and ILIAS. Library:
   [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (MIT). **This is the default
   recommendation** and the one most engagements under-use.
2. **MCP against the platform's REST API** — the agent gets tools, the platform stays untouched.
   Connectors on the shelf in `agents/top.md`.
3. **Plugin / XBlock inside the platform** — deepest UX integration, inherits the platform's
   licence obligations for the plugin.
4. **Fork the platform** — only defensible when the licence is permissive and the client wants to
   own the product.

## Platforms and where AI goes

| platform | licence | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **Moodle** — [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Moodle plugin types, or the AI subsystem introduced in the 4.5+ line; LTI for anything you want to keep out of GPL | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) (GPL-3.0, 222★ — tutoring, quiz generation, RAG over course materials); [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) (GPL-3.0, 16★ — Saylor Academy's "SOLA" learning coach, a real institutional deployment); [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) (17★, **unlicensed** — MCP as a web-service plugin, listed on marketplace.moodle.com). Build help: [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) (MIT). **Delivery note:** GitHub is a mirror; contribution goes to git.moodle.org. |
| **Open edX** — [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **XBlock** ([`openedx/XBlock`](https://github.com/openedx/XBlock), Apache-2.0) is the clean route — the component framework is permissive even though the platform is not. Operations go through **Tutor** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (AGPL-3.0, 2★, experimental) is the only MCP path. Sandboxing for generated/learner code: [`openedx/codejail`](https://github.com/openedx/codejail) (Apache-2.0). Analytics: `tutor-cairn`. |
| **Tutor** (Open edX distribution) — [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | Write a Tutor plugin (cookiecutter provided) to ship AI services as containers alongside the platform | Plugin family is first-party and broad: `tutor-mfe`, `tutor-cairn`, `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. A Tutor plugin is how an AI service gets deployed and upgraded with the platform rather than beside it. |
| **Canvas** — [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | Canvas's REST API is the richest of any LMS — hence MCP first, LTI second. Avoid forking | The deepest connector ecosystem in education AI: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 288★, canonical) and [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT, 9★). Avoid [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) (103★ but **no licence**). |
| **Kolibri** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Fork freely, or extend the Python app directly; content pipeline via [`learningequality/studio`](https://github.com/learningequality/studio) (MIT) | No AI agent found on top of Kolibri. **This is the most valuable unfilled slot in the whole KB:** MIT licence, offline-first design, and the deployment contexts (rural LATAM, Sub-Saharan Africa, South Asia) where a *small local model* is the only viable option. See pattern P4 in `compose/patterns.md`. |
| **Sakai** — [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** (permissive) | Java tool/provider model, or LTI | No notable AI-on-top found. Attractive because the licence is permissive and the installed base is institutional Java estate. |
| **Chamilo** — [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | Plugin API, or LTI | No notable AI-on-top found. Matters for engagement reach: real adoption in Francophone Europe and Spanish-speaking LATAM, where Moodle/Canvas assumptions do not hold. |
| **ILIAS** — [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | Plugin slots, or LTI | No notable AI-on-top found. Chosen in EMEA public-sector procurement for standards and accessibility compliance — the same reasons that make AI features there a documentation exercise as much as an engineering one. |
| **OpenOLAT** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** — verify | Java extension model, or LTI | No notable AI-on-top found. Swiss/German university base. |
| **OpenEduCat** — [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **NOASSERTION** — verify | Odoo module (it is an Odoo app), so the whole Odoo module ecosystem applies | No notable AI-on-top found. **The ERP slot** — admissions, records, timetabling, fees. This is where "80% of routine administration automated" claims would actually have to land, and nothing open source does it yet. |
| **BigBlueButton** — [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Use the API/webhooks and the recording pipeline; LGPL permits linking without reciprocity | No notable AI-on-top found. The live-classroom surface: transcription, session summarisation, participation analytics, post-session question generation. Install and front-end: `bbb-install`, `greenlight`. |
| **Oppia** — [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | Fork or extend directly — no reciprocity | No notable AI-on-top found. Its lesson model already encodes misconceptions explicitly, which is exactly the structure an LLM tutor needs and usually lacks. Permissive + pedagogically structured is a rare combination. |
| **Frappe LMS** — [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | Frappe app; inherits the Frappe/ERPNext data model | No notable AI-on-top found. Pick when the client already runs ERPNext and wants learning next to HR and finance data. |
| **H5P** — [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | Content type authored once, embedded into any host LMS (`moodle-mod_hvp` for Moodle) | The standard delivery vehicle for generated interactive content: have an agent produce H5P content types and they render in every platform above. |
| **Richie** — [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | Django/React CMS in front of Open edX | The catalogue/portal layer. MIT, so the public-facing surface can be customised freely even when the LMS behind it is AGPL. |
| **SCORM/xAPI** — [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | Runtime shim | How legacy courseware a client already paid for keeps working, and how learner interaction data gets out of it for analytics. |
| **Blackboard** (proprietary) | n/a | API only | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, 11★, Peru) is the only open connector found. Blackboard retains significant higher-ed share, especially in LATAM, and is almost entirely unserved by open source. |

## The licence decision, stated plainly

| client intent | platforms that permit it |
|---|---|
| Ship a **closed derivative** the client owns | Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Academico (MIT), Richie (MIT), H5P (MIT) |
| Run a **hosted service** for third parties | Anything, **via LTI or MCP only**. Forking an AGPL platform (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse, ClassroomIO) triggers network-copyleft source release |
| Deepest **in-platform UX**, client keeps the estate | Moodle plugin (GPL-3.0) or Open edX XBlock (Apache-2.0 component in an AGPL host) |
| Touch **no platform source** | LTI 1.3 everywhere — the safe default |

## Declared gaps

- **Eight of the fifteen platforms above have no AI-on-top project at all.** The AI work has
  concentrated almost entirely on Canvas (five-plus MCP servers) and Moodle (three plugins). Sakai,
  Chamilo, ILIAS, OpenOLAT, Oppia, Kolibri, Frappe LMS and OpenEduCat are open ground.
- **Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to an OSI identifier** and
  must be read before any client commitment.
- **No open-source proctoring or academic-integrity system** was found, in a year when assessment
  integrity is the top institutional concern and EU rules will treat such systems as high-risk.
