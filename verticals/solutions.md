---
industry: education
region: Global
updated: 2026-10-11
---

# Education — vertical platforms you can customise

**Pass 132, 2026-10-11.** p131's structure and rows retained; 🔴 **a whole category of platform is
ADDED below — the national K-12 school platforms, which carry more AI connectors than Moodle and
which no previous pass of this KB had listed at all** (see `README.md` → Pass 132, `P132-A`). The
Kolibri row is also corrected. This page answers one question: *the client runs X — where does AI
attach, and what does the licence let us ship?* Repo-level verification lives in
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
| **Moodle** — [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Moodle plugin types, or the AI subsystem introduced in the 4.5+ line; LTI for anything you want to keep out of GPL | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) (GPL-3.0, 222★ — tutoring, quiz generation, RAG over course materials); [`saylordotorg/moodle-local_ai_course_assistant`](https://github.com/saylordotorg/moodle-local_ai_course_assistant) (GPL-3.0, 16★ — Saylor Academy's "SOLA" learning coach, a real institutional deployment); [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) (17★, **unlicensed** — MCP as a web-service plugin, listed on marketplace.moodle.com). 🟢 **CORRECTED BY p131 — the permissive route exists and p130 denied it:** a *standalone* MCP server against Moodle's web-service API needs **no in-tree plugin and inherits no GPL obligation**. [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) is **MIT** (43★, verified at pass 30 of this KB as the licence-boundary exemplar), with [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) (**MIT**, assessment + gradebooks, writes gated), [`1alexandrer/moodle-mcp`](https://github.com/1alexandrer/moodle-mcp) (**MIT**, template) and [`Deeptanshuu/mydy-lms-helper`](https://github.com/Deeptanshuu/mydy-lms-helper) (**MIT**, single-institution worked example). Avoid [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) (40★, **no licence**). Build help: [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) (MIT). **Delivery note:** GitHub is a mirror; contribution goes to git.moodle.org. |
| **Open edX** — [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **XBlock** ([`openedx/XBlock`](https://github.com/openedx/XBlock), Apache-2.0) is the clean route — the component framework is permissive even though the platform is not. Operations go through **Tutor** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (AGPL-3.0, 2★, experimental) is the only MCP path. Sandboxing for generated/learner code: [`openedx/codejail`](https://github.com/openedx/codejail) (Apache-2.0). Analytics: `tutor-cairn`. |
| **Tutor** (Open edX distribution) — [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | Write a Tutor plugin (cookiecutter provided) to ship AI services as containers alongside the platform | Plugin family is first-party and broad: `tutor-mfe`, `tutor-cairn`, `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. A Tutor plugin is how an AI service gets deployed and upgraded with the platform rather than beside it. |
| **Canvas** — [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | Canvas's REST API is the richest of any LMS — hence MCP first, LTI second. Avoid forking | The deepest connector ecosystem in education AI: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 288★, canonical) and [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT, 9★). Avoid [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) (103★ but **no licence**). |
| **Kolibri** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Fork freely, or extend the Python app directly; content pipeline via [`learningequality/studio`](https://github.com/learningequality/studio) (MIT). 🟢 **Or do not integrate at all — orchestrate it** | 🔴 **CORRECTED BY p132. The claim that this was "the most valuable unfilled slot in the whole KB" is false.** [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) (**Apache-2.0, 39 444★**) already runs **Kolibri as its education container** beside **Kiwix** (library) and **Ollama** (AI assistant), as a Docker orchestration layer. It is the second-largest repo in this KB. Also [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) (20★, macOS port) and [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) (2★, Indian Class-10 curriculum, claims Kolibri integration). 🟢 **The surviving slots are narrower: nothing builds AI *inside* Kolibri** (NOMAD attaches from outside), **and nothing offline targets LATAM.** See pattern P2 in `compose/patterns.md`. |
| **Sakai** — [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** (permissive) | Java tool/provider model, or LTI | No notable AI-on-top found. Attractive because the licence is permissive and the installed base is institutional Java estate. |
| **Chamilo** — [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | Plugin API, or LTI | No notable AI-on-top found. Matters for engagement reach: real adoption in Francophone Europe and Spanish-speaking LATAM, where Moodle/Canvas assumptions do not hold. |
| **ILIAS** — [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | Plugin slots, or LTI | No notable AI-on-top found. Chosen in EMEA public-sector procurement for standards and accessibility compliance — the same reasons that make AI features there a documentation exercise as much as an engineering one. |
| **OpenOLAT** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** — verify | Java extension model, or LTI | No notable AI-on-top found. Swiss/German university base. |
| **OpenEduCat** — [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read; the API's `NOASSERTION` is a matcher artefact) | Odoo module (it is an Odoo app), so the whole Odoo module ecosystem applies. **LGPL permits linking without reciprocity** — so an AI service calling it from outside is clean | No notable AI-on-top found. **The ERP slot** — admissions, records, timetabling, fees. This is where "80% of routine administration automated" claims would have to land. 🟢 **And the tier is wider than p130 said:** `frappe/education` (662★), `academico` (MIT, 404★), RosarioSIS, Gibbon, openSIS, Fedena — see `repos/foundations.md`. |
| **BigBlueButton** — [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Use the API/webhooks and the recording pipeline; LGPL permits linking without reciprocity | No notable AI-on-top found. The live-classroom surface: transcription, session summarisation, participation analytics, post-session question generation. Install and front-end: `bbb-install`, `greenlight`. |
| **Oppia** — [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | Fork or extend directly — no reciprocity | No notable AI-on-top found. Its lesson model already encodes misconceptions explicitly, which is exactly the structure an LLM tutor needs and usually lacks. Permissive + pedagogically structured is a rare combination. |
| **Frappe LMS** — [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | Frappe app; inherits the Frappe/ERPNext data model | No notable AI-on-top found. Pick when the client already runs ERPNext and wants learning next to HR and finance data. |
| **H5P** — [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | Content type authored once, embedded into any host LMS (`moodle-mod_hvp` for Moodle) | The standard delivery vehicle for generated interactive content: have an agent produce H5P content types and they render in every platform above. |
| **Richie** — [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | Django/React CMS in front of Open edX | The catalogue/portal layer. MIT, so the public-facing surface can be customised freely even when the LMS behind it is AGPL. |
| **SCORM/xAPI** — [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | Runtime shim | How legacy courseware a client already paid for keeps working, and how learner interaction data gets out of it for analytics. |
| **Blackboard** (proprietary) | n/a | API only | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (ISC, 11★, Peru) is the only open connector found. Blackboard retains significant higher-ed share, especially in LATAM, and is almost entirely unserved by open source. |

## The category this page was missing: national K-12 school platforms

🔴 **Every platform above is an LMS or an ERP, and in most of EMEA and APAC that is not what a
school actually runs.** A Polish school runs **Librus**. A Slovak or Czech school runs **EduPage**.
A French school runs **Pronote**. A German one runs **IServ**. These are the systems of record for
grades, attendance, homework and parent communication for millions of pupils — and this KB had
never listed one.

🟢 **They are also, by connector count, better served by open-source AI than Moodle is.** The
connectors are tiny and unofficial, but they exist and they map the API surface.

| platform | country | proprietary? | the attachment point | open connectors that exist |
|---|---|---|---|---|
| **Librus Synergia** | Poland | yes | portal login; no public partner API found | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) — 🟡 **MIT (2.x)**, `legacy_reference/` **GPL-3.0-only**, 10★. The largest connector of the tier. 🔴 Unofficial, *"not affiliated with Librus"*, and **no 2FA support** |
| **EduPage** | Slovakia / Czechia | yes | portal login | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) (**MIT**, 3★ — timetables, grades, homework, **meal ordering**, multi-school discovery, 2FA) and an independent second implementation [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) (**MIT**, 1★). 🟢 **Two independent implementations is the strongest demand signal in the tier** |
| **Pronote** | France | yes | portal login | [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) (**MIT**, 1★) — grades, timetables, homework, absences |
| **IServ** | Germany | yes | portal login | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) (**MIT**, 0★) — parent letters, timetables, **sick notes**. 🔵 The only connector in this KB whose user is a **parent** |
| **Sisu (Funidata)** | Finland (higher ed) | yes | institutional SIS API | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) (🔴 **no licence**, 1★) — written for **any** Sisu deployment, so the broadest reach of the tier, and unusable as published |
| **uSaint** | South Korea (higher ed) | yes | via `rusaint` | [`yourssu/soongpt-plugin`](https://github.com/yourssu/soongpt-plugin) (**MIT**, 3★) — course search, timetable planning, **graduation requirements**. Org-owned |
| **VTOP** | India (VIT) | yes | portal login | [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) (**Apache-2.0**, 4★) — attendance, marks, timetable, exams |
| **QLDT** | Vietnam (Hanoi Univ.) | yes | portal login | [`qxbao/qldt-hanu-mcp`](https://github.com/qxbao/qldt-hanu-mcp) (**GPL-2.0**, 1★). 🔴 **Jurisdiction warning:** Vietnam's Decision 33/2026/QD-TTg names education, including automated assessment and behavioural monitoring, as high-risk |
| **Visual Schedule Builder (VSB)** | Canada | yes | institutional API | [`luca-dupont2/mcgill-vsb-mcp`](https://github.com/luca-dupont2/mcgill-vsb-mcp) (**MIT**, 2★ — conflict checks and schedule generation **without browser automation**) and [`SleepyPandas/UofT-MCP`](https://github.com/SleepyPandas/UofT-MCP) (**MIT**, 1★) |

🔴 **The attachment point for this whole category is the problem, not the opportunity.** There is no
LTI here, no MCP-friendly partner API, and no vendor programme — the connectors log in **as the
pupil or the parent, with their password**, against a platform that has not sanctioned it. For the
four K-12 platforms that is children's attendance and grade data under GDPR with no processing
agreement, and `librus-mcp` only works where **two-factor authentication is switched off**.

🟢 **How to use this category in an engagement anyway, which is the genuinely valuable part:**

1. **As integration intelligence.** The expensive, slow work — mapping each platform's undocumented
   API surface — is done and published under MIT. Read it, keep the surface map, rebuild the auth.
2. **As the opening for a sanctioned integration.** None of these vendors has an agent story. A
   studio that brings one a properly authenticated, logged, DPA-backed connector is not competing
   with open source; it is replacing a password-scraper the vendor would rather did not exist.
3. **Never deploy one as-is.** See the credential-model blocker in `agents/top.md`.

## The licence decision, stated plainly

| client intent | platforms that permit it |
|---|---|
| Ship a **closed derivative** the client owns | Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Academico (MIT), Richie (MIT), H5P (MIT) |
| Run a **hosted service** for third parties | Anything, **via LTI or MCP only**. Forking an AGPL platform (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse, ClassroomIO) triggers network-copyleft source release |
| Deepest **in-platform UX**, client keeps the estate | Moodle plugin (GPL-3.0) or Open edX XBlock (Apache-2.0 component in an AGPL host) |
| Touch **no platform source** | LTI 1.3 everywhere — the safe default |

## Declared gaps

- **Eight of the fifteen platforms above have no AI-on-top project at all.** 🟢 **SURVIVES.** The AI
  work has concentrated almost entirely on Canvas (five-plus MCP servers) and Moodle (three plugins
  **plus eight standalone MCP servers, five of them MIT** — p131). Sakai, Chamilo, ILIAS, OpenOLAT,
  Oppia, Kolibri, Frappe LMS and OpenEduCat are open ground.
- ~~**Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to an OSI identifier.**~~
  🔴 **HALF-REFUTED.** `openeducat_erp` **does** resolve: **LGPL-3.0**, read from an 8 241-byte
  `master/LICENSE` by an earlier pass of this KB. 🟢 **`OpenOLAT` survives as unresolved** — its own
  documentation describes an Apache-2.0 basis that GitHub's matcher does not recognise, and no
  payload read is on record here. **Rule:** `NOASSERTION` means "GitHub's matcher did not recognise
  the file", never "no grant".
- ~~**No open-source proctoring or academic-integrity system** was found.~~ 🔴 **REFUTED.** Four
  **MIT** proctoring projects are now on the shelf (`agents/top.md` → academic-integrity tier), one
  of which this KB already held. 🟢 **The surviving gap is grade, not existence:** the largest is
  18★, all four are individually owned, and three do affect-adjacent inference — which is
  **prohibited** in EU education settings under AI Act Art. 5, not merely high-risk. Assessment
  integrity remains the top institutional concern and the shelf still cannot answer it at
  production grade.
- **No AI-on-top for any *open-source* system of record.** 🟢 **NARROWED, and the distinction is
  now the whole point.** p132 found **21 SIS/student-portal agents** (`agents/top.md`), so the
  blanket claim *"no AI-on-top for any system of record"* is **refuted** — but every one of the 21
  connects to a **proprietary or institution-hosted** portal (Librus, EduPage, Pronote, IServ,
  Sisu, uSaint, VTOP, QLDT, VSB, Quercus). 🔴 **The open-source systems of record —
  `openeducat_erp`, `frappe/education`, `academico`, RosarioSIS, Gibbon, openSIS, Fedena — still
  have exactly zero agent coverage between them.** That is the sharper and more useful gap: the
  connector effort has gone to the platforms a studio *cannot* fork, and avoided the ones it can.
- 🆕 **The national K-12 platforms have no sanctioned integration path at all.** Nine proprietary
  platforms (above) with real open connectors and **no LTI, no partner API and no vendor agent
  programme** between them. Every existing connector is an unofficial password-scraper. This is
  simultaneously the clearest unmet need and the clearest compliance hazard on this page.
