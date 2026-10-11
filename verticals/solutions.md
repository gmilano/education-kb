---
industry: education
region: Global
updated: 2026-10-11
---

# Education — vertical platforms you can customise

**Pass 135, 2026-10-11.** 🟢 **This page's longest-standing unresolved licence cell is resolved by
payload read, and the answer promotes a platform the page had written off.** `OpenOLAT` has sat in
*Declared gaps* as *"survives as unresolved — its own documentation describes an Apache-2.0 basis
that GitHub's matcher does not recognise, and no payload read is on record here."* 🔴 **A payload
read is now on record, and the matcher was defeated by something neither side guessed.**

🟢 **Two platforms are added**, both permissive, both pushed the day before this pass:
**OpenOlat** (a full LMS with QTI and SCORM built in) and **Mentingo** (an AI-native LMS under MIT).
🟢 **One authoring platform is added** — **Adapt Framework**, the largest repository in the entire
standards stack at 630★.

🔵 **Licence cells added or corrected this pass were established by sha256 identity against
canonical SPDX texts**, not by GitHub's badge — `compose/code/p135-licence-sha-identity`, which
discharges `ACTION BP`.

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
   🟢 **Corrected by p134 — the library to reach for is not the one this page has been naming.**
   `ims-lti` (MIT, 203★) is Instructure's library. The platform-independent reference implementation
   is [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — **Apache-2.0, 373★, pushed 2026-10-06**,
   with OIDC launch, Deep Linking, **AGS grade passback** and NRPS rosters, plus first-party database
   plugins. In Python, [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT,
   138★) — 🔴 **but dormant since 2024-08-18, which is the weak link for an agent build.** For a PoC,
   [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter)
   (MIT) is a template over `ltijs`. 🟢 **And for the first time this page can name a conformance
   test:** [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests)
   (Apache-2.0) for the rostering side.
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

🟢 **Extended by p133 to LATAM and ANZ, and the same rule holds with different nouns.** A Brazilian
federal university runs **SIGAA**; a Brazilian federal institute runs **SUAP**; an Argentine
university runs **SIU-Guaraní**; an Australian school runs **SEQTA**; a New Zealand school runs
**KAMAR**. 🔴 **None of these five was on this page before p133, and together they carry 12 of the
category's connectors — including every teacher-facing one this KB has found.**

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
| **SIGAA** | Brazil (federal universities) | yes (SIG/UFRN-derived) | portal login | 🟢 **The deepest connector shelf of any platform on this page — 5 rows.** [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0, 20★ — deadlines → Google Tasks), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**, 19★), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**, 16★ — UI modernisation), [`MatheusMach/QuantoFalta`](https://github.com/MatheusMach/QuantoFalta) (🔴 no licence, 9★ — absence counter), and 🔴 **the teacher-facing one:** [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) (**MIT**, 9★ — grade entry from a spreadsheet) |
| **SUAP** | Brazil (federal institutes / IFs) | yes | portal login + institutional API | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**, 0★) and [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 no licence, 0★) — 🟢 two independent MCP implementations. Plus [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) (🟡 **AGPL-3.0**, 1★), **org-owned**, which drafts a lecturer's **RIT** workload report |
| **SIU-Guaraní** | Argentina (university consortium) | yes | portal login | [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) (**MIT**, 17★), [`despedite/siu-guarani`](https://github.com/despedite/siu-guarani) (🟡 GPL-3.0, 8★ — seat watcher), [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) (🔴 no licence — **teacher** grade upload). 🟢 **Uniquely, the vendor consortium is itself on GitHub:** [`SIU-Toba/docker-guarani`](https://github.com/SIU-Toba/docker-guarani) (🔴 no licence, 4★, dormant since 2017) |
| **SEQTA** | Australia | yes (TheSchoolBox) | portal login | 🟢 **The best-licensed and only product-shaped corner of this category.** [`BetterSEQTA/BetterSEQTA-Plus`](https://github.com/BetterSEQTA/BetterSEQTA-Plus) (**MIT**, **40★**, org-owned, 25 forks, Chrome Web Store, pushed 2026-10-06) and [`BetterSEQTA/DesQTA`](https://github.com/BetterSEQTA/DesQTA) (**MIT**, 16★ — native desktop port) |
| **KAMAR** | New Zealand | yes | portal login | 🔴 **One row, archived.** [`st22209/Parent-Portal`](https://github.com/st22209/Parent-Portal) (**MIT**, 2★) — README: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. 🔵 **Keep this row on the page precisely because it is dead: it is this category's only measured example of what a vendor API change does to an unsanctioned connector.** |
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

### 🆕 Four more national academic systems, and one national dataset *(p134)*

p133 added SIGAA, SUAP, SIU-Guaraní, SEQTA and KAMAR. 🟢 **p134's `ACTION BJ` sweep adds four more
and records two hard zeros with their probes named** — because an unprobed platform and an empty one
are different findings, and only one of them is information.

| platform | country | what it is | open-source AI/connector supply found | probe |
|---|---|---|---|---|
| **Q-Acadêmico** | 🟢 **Brazil** | The academic system of Brazil's **federal institutes** (IFs) — a fourth Brazilian national system alongside SIGAA, SUAP and the SAE family | 🟡 **~7 real rows out of 85 hits, topping out at 6★.** Best-licensed: [`adiel-calixto/IFAcademico`](https://github.com/adiel-calixto/IFAcademico) (**Apache-2.0**, 6★, 2026-04-26, Android). Also [`WKolodziejski/QMobile`](https://github.com/WKolodziejski/QMobile) (no licence, 6★, IFSul), [`MuriloCalegari/Ifes-Academico`](https://github.com/MuriloCalegari/Ifes-Academico) (GPL-3.0, 4★ — syncs grades, so **staff-adjacent**), [`kkauaon/qaluno`](https://github.com/kkauaon/qaluno) (no licence, 4★, IFCE), [`AlexandreL0pes/q-scraper`](https://github.com/AlexandreL0pes/q-scraper) (no licence — self-declared scraping) | `q-academico` |
| **SAES** (*Sistema de Administración Escolar*) | 🟢 **Mexico** | The academic portal of the **Instituto Politécnico Nacional** and other Mexican institutions | 🔴 **19 hits and effectively nothing usable.** Only 3 carry a permissive licence; the rest are unlicensed student scrapers. 🟢 **Two are conversational agents** — [`DanieelRC/SAES-R`](https://github.com/DanieelRC/SAES-R) (*"incluye un agente conversacional"*) and [`DanieelRC/AgenteConversacional-SAES-R`](https://github.com/DanieelRC/AgenteConversacional-SAES-R) (answers questions on the IPN academic regulations, *"para profesores"*) — 🔴 **both unlicensed, both 0★.** The one MIT row is a utility library, [`roncuevas/ipn_saes_utils`](https://github.com/roncuevas/ipn_saes_utils). [`pekochu/SAES2GO`](https://github.com/pekochu/SAES2GO) (GPL-3.0, 4★) **declares itself obsolete** | `saes escolar` |
| **SIMAT** (*Sistema Integrado de Matrícula*) | 🟢 **Colombia** | The national school-enrolment system run by the Ministry of National Education | 🟢 **One row, and it is a different species from everything else on this page:** [`juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia`](https://github.com/juanfelipemalaver00-arch/Predictive-model-for-primary-school-dropout-in-Colombia) (🔴 **no licence field**, 1★, pushed **2026-10-10**) — a CRISP-DM pipeline joining **C-600, SIMAT and IPM** with territorial variables to raise **explainable dropout-risk alerts for a Secretaría de Educación**. 🔵 **Not a portal connector and not a chatbot: a government-facing early-warning model.** The only row in this KB aimed at a ministry rather than a student | `simat colombia` |
| **SIAGIE** | **Peru** | The national school information system (MINEDU) | 🔴 **NO EVIDENCE FOUND FOR THIS PLATFORM.** `siagie peru in:name,description` → **`total_count: 0`**. Reported per `agents/top.md` clause 4 as a platform-level absence with its probe named — **not** as a Peruvian zero, since Peru's one row ([`campus-cli`](https://github.com/alejooroncoy/campus-cli), ISC, 11★) targets Blackboard | `siagie peru` |

🔵 **What the four of them together say, and it is the most useful sentence on this page for a LATAM
engagement:** **Brazil has four national academic systems and a real builder community around each;
Mexico has one with a scraper community and no licences; Colombia's activity is aimed at the
ministry rather than the portal; and Peru's national system has no open-source footprint at all.**
Four countries, four different market shapes — which is why "LATAM" is not a strategy.

## 🟢 The category this page has been missing in the other direction: vendors that publish their own integration *(new, p134)*

🔴 **Every platform section above this one describes something a client runs and we attach to from
outside, usually unsanctioned.** These are the opposite: **the vendor ships the integration path
itself, under a permissive licence.** That makes them the shortest route to a defensible engagement,
and this KB had never listed one.

| platform | vendor / region | what the vendor publishes | licence |
|---|---|---|---|
| **WISEflow** | 🟢 **UNIwise ApS — EMEA (Denmark)** | [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) — user creation, flow setup, **assessor allocation** and **grade passback** against the WISEflow API. 🟢 **Licence payload-read and the holder is the vendor company itself.** WISEflow is a digital-assessment platform used across Nordic and UK higher education — so this is an **assessment** counterparty, the segment `intel/trends.md` records as the fastest-growing | **MIT** |
| **Blackboard Learn** | **Anthology — North America** | Two LTI 1.3 Advantage reference tools in Blackboard's own org: [`BBDN-lti-1p3-tool-example`](https://github.com/blackboard/BBDN-lti-1p3-tool-example) (Python/Flask, **Apache-2.0**) and [`BBDN-LTI-Adv-Node`](https://github.com/blackboard/BBDN-LTI-Adv-Node) (Node/React, 🔴 **no licence field**). 🟢 **Plus a public REST API that four of the seven Blackboard connectors in `agents/top.md` actually use** | **Apache-2.0** (one of two) |
| **TAO** | **Open Assessment Technologies — EMEA (Luxembourg)** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) — OneRoster import into the TAO assessment platform | 🟡 **GPL-2.0** |
| **Ed-Fi ODS** | 🟢 **Ed-Fi Alliance (standards body) — North America** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) — serves a **OneRoster 1.2 API from an Ed-Fi ODS**, pushed 2026-10-09 | 🟢 **Apache-2.0** |
| **Google Classroom estate** | 🟢 **Google — North America** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) — conformance tests proving a OneRoster integration correct | 🟢 **Apache-2.0** |
| **Aeries SIS + Edgenuity** | **North America (Fresno, California)** | [`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback) — keeps an **Aeries** gradebook current from **Edgenuity**. 🔴 **No licence field**, 0★. 🔴 **And its content could not be reached:** repo search returns it with metadata, but the raw lane returned 404 for 15 candidate paths across `HEAD`/`main`/`master`, so **this pass verified that the repository exists and did not verify that it contains anything.** 🟢 **Listed because of who owns it: a US school-district-adjacent org publishing its own passback job** — the K-12 integration need, in public, from the buyer's side | 🔴 **none** |
| **Agilix Buzz** | **North America (Idaho Digital Learning Alliance)** | [`RyanGravetteIDLA/qualtrics-lti-connector`](https://github.com/RyanGravetteIDLA/qualtrics-lti-connector) — LTI 1.3 bridge from Buzz LMS to Qualtrics with automated grade passback. 🔴 **ARCHIVED** | **MIT** |
| **Virtual Arkansas** | **North America (state virtual school)** | [`virtualarkansas/jupyterlite-zestables`](https://github.com/virtualarkansas/jupyterlite-zestables) — JupyterLite notebooks packaged as Canvas content with assessment and state persistence. 🔴 No licence field | 🔴 **none** |

🔵 **The pattern across this table is the sales argument.** 🟢 **Where a vendor or a public body
publishes its own integration, the licence is usually permissive and the auth is sanctioned.**
🔴 **Where a school district or state agency publishes one, it is usually unlicensed** — not out of
hostility but because nobody asked them to add a `LICENSE` file. **That is a conversation, not a
blocker: an unlicensed repo from an institutional owner is the one case where asking for a grant is
likely to succeed**, unlike the 20-odd unlicensed student scrapers elsewhere in this KB.

### 🆕 The open-source education ERP field, named properly *(p134)*

`repos/foundations.md` carries `openeducat_erp` (LGPL-3.0, 886★) and `frappe/lms` (AGPL-3.0). The
surrounding product field, for when a client asks what else exists:

| product | licence | what it covers | note for an engagement |
|---|---|---|---|
| **OpenEduCat** | LGPL-3.0 (payload-read, per `repos/foundations.md`) | Admissions, attendance, exams, fees; **73+ modules**; built on **Odoo**/Flectra, so it sits beside Odoo finance and HR | 🟢 **The Odoo base is the point** — an AI module attaches as an Odoo addon, and the client's non-education ERP data is already in the same schema. 🟡 Vendor lists a paid tier from ~US$575/yr alongside the free community edition; treat vendor TCO claims as marketing |
| **Frappe Education** | AGPL-3.0 | Student enrolment, class assignments, assessments, fee collection, on the Frappe framework | Same reasoning as `frappe/lms` — adjacency to Frappe/ERPNext finance and HR. 🔴 AGPL: fine inside a client estate, a problem if offered as a hosted service |
| **RosarioSIS** | 🟡 **GPL-2.0** | K-12 student information system; PHP + PostgreSQL/MySQL | 🔴 **Still zero agent coverage** — one of the open-source systems of record this KB has flagged as unserved for several passes. `compose/patterns.md` → **P9** |
| **openSIS** | varies by edition — **verify** | K-12 and higher-ed school information system | 🔴 **Community/commercial split: do not assume the public edition's licence covers the feature a client saw in a demo.** Unverified by this pass |
| **Gibbon** | not verified this pass | School platform | 🔴 **Named in listicles with no detail.** This pass found no primary evidence; it remains an unexamined row, recorded so a later pass does not mistake absence of evidence for evidence of absence |

🔴 **Instrument note on this subsection, because it is weaker than the rest of the page.** These
five rows come from **vendor pages and listicles via web search**, not from repo search or a payload
read. One review source was ~656 days old. 🟢 **Everything else on this page is repo-verified;
this table is not, and a client-facing claim should be re-verified against each project's own
repository first.**

## 🟢 Platforms added by p135 — and one licence cell finally resolved

| platform | licence *(hash-verified this pass)* | the attachment point | real AI-on-top that exists today |
|---|---|---|---|
| **OpenOlat** — [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), **447★**, pushed 2026-10-09 | 🟢 **Apache-2.0 + 2 attribution statements** (payload read, 10 982 B, Apache-2.0 core verbatim) | 🟢 **The richest attachment surface of any permissive LMS here**: QTI assessment, SCORM content, curriculum management, lecture management and course templates are all first-party, so AI attaches to a *standard* inside the platform rather than to a bespoke API. LTI for anything kept at arm's length | 🔴 **Nothing.** This KB has found no AI project targeting OpenOlat — and now that the licence is permissive and the surface is standards-native, 🟢 **this is the cleanest unclaimed platform slot on the page**, especially for a German-speaking-Europe engagement |
| **Mentingo** — [`Selleo/mentingo`](https://github.com/Selleo/mentingo), 92★, pushed **2026-10-10** | 🟢 **MIT** | Not an attachment at all — **the AI is the platform.** Fork it, white-label it, self-host it | 🟢 **It ships its own:** AI mentor, role-play scenarios, compliance/corporate training flows, SCORM and xAPI. Positioned explicitly as a self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX. 🔵 Small and vendor-led (Selleo, Poland), so read it as a **reference architecture and a fork base**, not as a mature platform |
| **Adapt Framework** — [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework), **630★**, pushed **2026-10-10** | 🔴 **GPL-3.0** | A **content authoring** platform rather than an LMS: it produces responsive, accessible, multi-language course packages that emit **SCORM and xAPI**, which any LMS above can then consume | Generation of course structure and items into Adapt's JSON authoring format, then export as a tracked SCORM package. 🔴 **Copyleft matters here in a specific way:** the client *runs* Adapt as a tool and owns the course output, so GPL-3.0 constrains redistribution of Adapt itself and not the courses it authors |

### 🟢 The OpenOLAT `NOASSERTION`, explained — and it is a general lesson

p132 recorded that GitHub's matcher does not recognise OpenOlat's licence and that its own
documentation claims Apache-2.0. **Both were right, and the reason is now measured.** The file is
Apache-2.0 **to the character** through all nine sections of the terms — and then, where
`END OF TERMS AND CONDITIONS` and the boilerplate appendix belong, it carries instead:

> `* * *` *Additional license statement for the original olat.org code base:* … *originally created
> by the OLAT Zentrum at the University of Zurich* … `* * *` *Additional license statement for the
> openolat.org code base:* … *OpenOLAT is initiated by frentix GmbH and is initially based on the
> OLAT 7.1 release.*

🟢 **Consequence for a client engagement: this is a permissive licence.** The grant, the patent
clause and the disclaimer are unmodified Apache-2.0. 🔴 **The obligation is the attribution:** both
statements must be carried into any redistribution, which is an ordinary Apache-2.0 `NOTICE`-style
duty stated in an unusual place.

🔵 **The general lesson, and it applies to every `NOASSERTION` on this page.** A licence matcher
answers *"are these bytes a template I know?"* A client needs the answer to *"what may we ship?"*
Those differ whenever a project appends institutional attribution — which **well-governed,
institution-derived projects are the most likely to do.** 🔴 **So `NOASSERTION` is biased towards
exactly the platforms an education engagement most wants to use**, and that is the second time this
KB has recorded that bias (`P134-F`).

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
  🟢 **FULLY RESOLVED BY p135 — both halves.** `openeducat_erp` resolves to **LGPL-3.0**, read from
  an 8 241-byte `master/LICENSE` by an earlier pass. 🟢 **`OpenOLAT` resolves to Apache-2.0 with two
  attribution statements replacing the appendix** — payload read this pass, core terms verbatim,
  permissive in effect (see *The OpenOLAT `NOASSERTION`, explained* above). **Rule, now with two
  instances behind it:** `NOASSERTION` means "GitHub's matcher did not recognise the file", never
  "no grant" — and it is **biased towards institution-derived projects**, because they are the ones
  that append attribution.
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
