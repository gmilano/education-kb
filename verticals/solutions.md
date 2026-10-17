---
industry: education
region: Global
updated: 2026-10-17
---

# Vertical solutions — Education

> Real, running platforms a studio engagement can start from and put an agentic layer on
> top of — the Odoo-for-ERP pattern applied to education. Licences read first-hand from
> payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds three platforms, kills two that vendor comparisons recommend, and takes
> the permissive-LMS count from one to three. Extended by
> [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv) — pass 267
> **corrects this file's own claim that Canvas is "commercial SaaS, not a base to build on"**
> (its source is AGPL-3.0, 78,765 commits), and adds a European public-sector school platform, an
> e-testing platform and an offline assessment platform.

## The platform shelf

| Platform | Repo | Licence | Stack | Where it fits |
|----------|------|---------|-------|---------------|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(`COPYING.txt`)* | PHP + MySQL/PostgreSQL | The default LMS of public education worldwide. Has a **first-party AI subsystem since 4.5** — provider-pluggable, so a client can point it at OpenAI, Azure, or a local Ollama/vLLM endpoint. Start here for K-12 and public universities. |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** — 🟢 **RIDER-CLEARED at payload, pass 272** *(`master/LICENSE`, 10,982 B; `TERMS AND CONDITIONS` byte-identical to upstream; the 375 B shortfall vs stock is the optional APPENDIX replaced by two attribution notes — University of Zurich / frentix GmbH — carrying no restriction. See `T39`)* | Java | **The only Apache-2.0 full LMS found this pass.** Swiss-maintained, used across German-speaking higher education. If procurement rules out copyleft, this is the shelf — and it is the single most under-used finding in this file. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | Python/Django + React | MOOC-scale, the platform behind edX. Extend through [XBlock](https://github.com/openedx/XBlock) (Apache-2.0), never by forking core. **The AGPL network clause applies to hosted deployments** — price it before the SOW, not after. |
| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | Java/Spring + Angular | Interactive learning with **automated feedback** and an integrated exercise runner (TUM Applied Education Technologies; 819★, 12,437 commits, self-hosted by universities in several countries). The permissive choice when the deliverable is assessment rather than content delivery. **Pass 266 — the AI layer is already built and config-gated:** **Iris** (LLM tutor, MIT), **Pyris** (LLM microservice, MIT), **Athena** (feedback suggestion, **licence UNVERIFIED**), **Hyperion** (AI exercise authoring on Spring AI, no separate repo). "Config-gated" is the commercially important word — the same deployment runs with AI off, so a high-risk EU AI Act classification can be met by configuration rather than by re-architecture. |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | TypeScript | **AI-native LMS**, self-hosted, positioned against Docebo/TalentLMS. Ships an AI mentor with voice role-play and auto-scoring, an AI course builder that converts policy documents into courses, open-ended answer grading, **Langfuse tracing of model calls**, an **MCP endpoint**, and bring-your-own-key. The closest thing to a 2026-native corporate L&D starting point under MIT. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | Odoo (Python) | Education **ERP**: admissions, SIS, gradebook, library, fees — the Odoo-for-education pattern. Active branches for Odoo 17.0 / 18.0 / 19.0. **The repo path this base previously published (`OpenEduCat-Inc/OpenEduCat`) is a 404; this is the canonical one.** |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | PHP | Lightweight LMS with the deepest LATAM public-sector footprint of any platform here. The pragmatic base for ministry-scale work in Spanish-speaking markets. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | PHP | The institutional LMS of German-speaking EMEA (DE/CH/AT), with a strong assessment module and the compliance posture that market expects. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | Java/Spring | North American higher-ed consortium LMS. **Prior cell said Apache-2.0; the payload is the Educational Community License 2.0** — Apache-derived and OSI-approved, but with patent-grant language scoped to educational use. A real distinction for a commercial deliverable. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | PHP | School management / SIS: timetabling, attendance, behaviour, pastoral records. Complements rather than replaces an LMS. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | PHP | K-12 SIS, light enough for a single school to self-host. |
| **Richie + Marsha** | [openfun/richie](https://github.com/openfun/richie) · [openfun/marsha](https://github.com/openfun/marsha) | MIT · MIT | Django + React | Course catalogue portal and education video platform from France Université Numérique. MIT, EMEA-origin, nationally proven. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | Docker-first | Multimodal tutoring platform: voice, video, configurable 3D avatars, local LLMs via Ollama. **Licence re-confirmed this pass** — the payload is the verbatim BSD-3 form; its opening *"All rights reserved"* belongs to that form and is not a reservation. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | Python/Angular | *"A free, online learning platform to make quality education accessible for all."* 6.9k stars, **17,004 commits**. Structured lessons with formative feedback built into the lesson model rather than bolted on. **The second Apache-2.0 complete platform in this KB** and the highest-adoption permissive one. Its lesson structure is the cleanest place to attach a tutoring agent without touching an LMS. |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | Python/Django + Vue | *"the offline app for universal education."* 1.2k stars, **39,803 commits**. Runs fully **offline** and syncs opportunistically — built for schools with intermittent power and bandwidth. **MIT, which makes it the first permissive full platform in this KB that is not Apache-2.0.** The right base for rural LATAM, low-bandwidth APAC and anywhere a prompt cannot assume a network. |
| **Sunbird** | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) · [project-sunbird/knowledge-platform](https://github.com/project-sunbird/knowledge-platform) | **MIT** · **MIT** | Java/Angular + mobile | **India's national education stack, and the APAC-origin platform this KB spent 265 passes declaring absent.** The codebase beneath **DIKSHA** (NCERT / Ministry of Education); README mission: *"improve learning outcomes for **200 million children across India**"*. **38,046 commits, 317 forks — and 41 stars**, which is why star-sorted search never found it. Modular by design: portal, `knowledge-platform` backend, [mobile app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). **MIT at national scale is the single most permissive large-platform option in this file** — for an APAC public-sector engagement it is the installed-base answer the way i-Educar is in Brazil. ⚠️ Slug trap: `Sunbird-Ed/sunbird-ed-portal` does not resolve; the live slugs are camel-case. |
| **Numbas** | [numbas/Numbas](https://github.com/numbas/Numbas) | **Apache-2.0** | Python 3 compiler → JS runtime | **E-assessment that executes entirely in the browser** (Newcastle University; 215★, 4,209 commits). Randomised questions, algebraic marking, SCORM-packaged output. Not a full LMS — it is the assessment engine you drop *into* one. Its architecture is the selling point under GDPR or a data-residency rule: **the submission never leaves the device**, so residency is satisfied structurally rather than by a processing agreement. |
| **i-Educar + i-Diário** | [portabilis/i-educar](https://github.com/portabilis/i-educar) · [portabilis/i-diario](https://github.com/portabilis/i-diario) | GPL-2.0 · **AGPL-3.0** | Laravel/PHP | **The Brazilian public-sector stack.** School management (SIS) plus a teacher portal, originally built by the *prefeitura de Itajaí (SC)* and published on the federal **Portal do Software Público in 2008**. 719 stars, 34,948 commits, last commits **2026-10-14** and **2026-10-09**. For a Brazilian municipal or state network this is the installed-base answer, and its provenance matches MEC's sovereignty framing exactly. **Legal note:** i-Diário's licence payload is a *Portuguese translation* of AGPL-3.0, not the FSF English text — cite the English original. |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | Ruby on Rails + React | **The market-leading LMS of North American higher education — and its source is published.** *"The open LMS by Instructure, Inc."* **78,765 commits** (2.1x Kolibri, 6.3x Artemis), 6.9k★, 3.0k forks. ⚠️ **This file previously listed Canvas under "not on the shelf" as "commercial SaaS, not a base to build on". That was wrong** — see the correction below. The practical posture barely changes, but the *reason* does: you stay out of core because of the **AGPL-3.0 network clause**, not because the code is closed. Integrate through the Canvas API, LTI (`tsugi`), or [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (**MIT**) — an **AGPL platform with an MIT doorway**. |
| **TAO** | [oat-sa/package-tao](https://github.com/oat-sa/package-tao) · [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **GPL-2.0** · GPL-2.0 | PHP (Composer) | Open-source **e-testing** platform for authoring and delivering assessments — *"created by the University of Luxembourg"*, maintained by **Open Assessment Technologies** (README-quoted → EMEA-origin). The assessment platform to know where the deliverable is *high-stakes testing* rather than coursework, which is where Artemis and Numbas stop. **GPL-2.0 is the most restrictive licence on this shelf for a commercial deliverable** — it is not even AGPL-compatible — so the boundary is the delivery API, not the engine. ⚠️ **Secondary sources routinely attach famous international assessment programmes to TAO; the README claims none, and this KB asserts none.** |
| **Schul-Cloud** | [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) · [hpi-schul-cloud/nuxt-client](https://github.com/hpi-schul-cloud/nuxt-client) | **AGPL-3.0** · AGPL-3.0 | Node/NestJS + Nuxt | **The European public-sector school platform this shelf was missing.** *"Schulcloud-Verbund-Software-Server"* — **16,192 commits**, 81★ — a German school-cloud stack built around data-protection-first school IT, which is the posture EMEA procurement actually tests for. The counterpart to Sunbird (APAC) and i-Educar (LATAM) in the public-sector lane. ⚠️ **Provenance is org-handle grade only** — the handle is `hpi-schul-cloud` and the README links `dbildungscloud.dev`, but **it names no ministry, funder or Land**; do not brief it as a federal programme. ⚠️ The GitHub sidebar shows a License link **with no label**; the payload is the only licence evidence. AGPL network clause applies to hosting. |
| **Tangerine** | [Tangerine-Community/Tangerine](https://github.com/Tangerine-Community/Tangerine) | **GPL-3.0** | Angular/PouchDB-CouchDB | **Offline-first *assessment* and data collection for low-resource settings** — **8,064 commits**, 70★. Runs on tablets and phones with no connectivity and syncs when a link appears; built originally for early-grade reading and maths. **The missing half of the offline lane:** Kolibri (MIT) delivers content offline, Tangerine measures learning offline. Logo is a registered trademark of **RTI International**. ⚠️ README claim, not independently verified: *"5 million+ assessments across 65 countries and 80+ organisations"* — **no country list is served**, so no named deployment is asserted. |
| **Kolibri Studio** | [learningequality/studio](https://github.com/learningequality/studio) | **MIT** | Python/Django + Vue | *"Content curation tools for Kolibri"* — **15,493 commits**, 193★, 312 forks. The authoring and publishing half of the offline stack: builds content channels Kolibri imports, **remixes channels against national curricula and special-needs requirements**, and authors learning pathways and assessments. Shelved because a Kolibri deployment without Studio is a reader with no content pipeline — and the pipeline is where a ministry engagement's actual work sits. *MIT: the copyright line carries an "(internal apps)" parenthetical; the grant clauses are unmodified standard MIT.* |

| **Koha** | [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 *(`main/LICENSE`, 35,151 B)* | Perl + MySQL/MariaDB | **The world's most deployed open-source integrated library system (ILS)** — 594★, the adjacent system of record in virtually every academic-library engagement: catalogue, circulation, acquisitions, patrons, OPAC. **Added in pass 271, and the reason it was missing is recorded rather than quietly fixed:** it has been carried on `repos/trending.md` and `agents/trending.md` for several passes and never reached this shelf, which is the one a studio reads when it needs something to stand up. Licence re-measured blind this pass and it **agrees to the byte**. 🔵 **Where the AI layer goes:** Koha's catalogue is the cleanest authority file for a retrieval index in a university engagement — subject headings and holdings are already curated, so a RAG layer over Koha starts from librarian-maintained metadata instead of scraped text. ⚠️ GPL-3.0: keep the deliverable on the API side of the boundary. |
| **H5P** *(content authoring)* | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · [tunapanda/h5p-standalone](https://github.com/tunapanda/h5p-standalone) · [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🔴 **GPL-3.0** *(`master/LICENSE.txt`, 35,146 B)* · 🟢 **MIT** *(1,077 B)* · 🟢 **MIT** *(1,073 B)* | PHP core; JS player | **Interactive content types — the authoring ecosystem embedded inside Moodle, Canvas and Drupal**, so it is already present in most incumbent estates. **Not a standalone platform; a subsystem** — shelved here because it is a running component a client already has, not an app to deploy. 🔴 **The licence is per-repository and that is the whole point** *(discharges `ACTION PW`)*: the **authoring core is GPL-3.0** and there is **no permissive H5P authoring server**; the MIT rows are **playback** (`h5p-standalone`) and **SCORM packaging** (`scorm-h5p-wrapper`). `Lumieducation/Lumi` (desktop) is **AGPL-3.0**. 🔵 **So the buildable move is to generate H5P content and play it through the MIT runtime**, never to fork the GPL authoring core. ⚠️ Path trap: `master/LICENSE` is a **404**, `master/LICENSE.txt` is a **200**, and the default ref is `master`. |

**24 platform rows, all licence-verified from payload** (13 from pass 264, 4 in pass 265, 5 added in
pass 267, **2 in pass 271**). Pass 267's five came from **commit-ranking and hand-probing named programmes**, not from
a topic listing — four of the five have under 200 stars and over 8,000 commits each.

## Not on the shelf — and why

| Candidate | Verdict |
|-----------|---------|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **Excluded.** Ships a bespoke *PageLM Community License*: non-commercial only, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"* without written permission. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv` grades it `MIT`.** That cell is wrong and a studio acting on it would have shipped unlicensed code to a client. |
| `OpenEduCat-Inc/OpenEduCat` | **Dead.** Repository page returns 404 and no raw path serves a payload. Replaced above by `openeducat/openeducat_erp`. |
| ~~Canvas / Instructure~~ | 🔴 **CORRECTED IN PASS 267 — this verdict was wrong.** This row read *"Commercial SaaS, not a base to build on."* [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) serves an **AGPL-3.0 payload (34,520 bytes)** and has **78,765 commits** — it is the largest education codebase in this KB and it is **open source**. Canvas is now on the platform shelf above. **What this error would have cost:** a North America engagement briefed to treat the market-leading LMS as a closed incumbent to migrate *off*, when the available move is to deploy or extend it and keep the deliverable outside the AGPL boundary. Instructure's **hosted service** is commercial; its **code** is not closed, and this file conflated the two. |
| Blackboard / Anthology | Commercial, closed. Genuinely not a base to build on — the incumbent to integrate with or migrate off. See [`intel/market.md`](../intel/market.md). |
| [OpenEMIS/OpenEMIS-Core](https://github.com/OpenEMIS/OpenEMIS-Core) | **Not shelved — and the reason is worth more than the row would be.** OpenEMIS is the education-management system most associated with *ministry-level* deployment, so pass 267 probed it by hand. What is reachable is a **32-commit Docker packaging repository, 7★, with no licence on any of 76 path/ref combinations, no label in the page sidebar, and no ministry or country named in its README.** Application source not located. **Ministry provenance is not established — do not brief it as a public-sector reference.** |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | **Not shelved — split licence, not a single grant.** 12,061 commits and a genuinely strong problem-driven assessment system, but the payload partitions the tree: Community Edition AGPL-3.0, `apps/prairielearn/src/ee/` an **Enterprise Edition under separate terms**, **all client-side JavaScript** AGPL-3.0, UIUC and outside-contributor portions MIT. The sidebar shows a License link **with no label**. Usable with legal review; **not** shelvable under one licence cell. |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | **Not shelved — MIT over a commercial dependency.** The grant is MIT, but the payload's first paragraph excepts the **Handsontable** component, which is **commercial software** requiring a compliance contact, plus two textbook texts under their own terms. The shape that passes a licence audit and fails procurement. |
| **Plan Ceibal (Uruguay)** | **Nothing to shelve, verified.** LATAM's most-cited national edtech programme: its `ceibal` GitHub organisation exists and states *"This organization has no public repositories"*, with no public members. Its platforms are **not open code**. A Ceibal-adjacent engagement is **integration, not adoption** — and briefing it as an open-source national stack (the way Sunbird genuinely is) would be wrong. |
| [formalms/formalms](https://github.com/formalms/formalms) (forma.lms) | **Excluded on licence, after being recommended to us.** A 2026 open-source-LMS review lists forma.lms as **Apache-2.0**. Its licence payload — `html/license.txt` — is the **GNU GPL, Version 2**. The project is alive (last commit 2026-07-17) and perfectly usable; it is simply *not* the permissive LMS that comparison implied, and it does not change the permissive count. |
| Fedena ([foradian/fedena](https://github.com/foradian/fedena), [projectfedena/fedena](https://github.com/projectfedena/fedena)) | **Excluded on abandonment.** Vendor comparisons still name Fedena as *the* Apache-2.0 education ERP/SIS. Both repositories are live pages over dead code: `foradian/fedena`'s last commit is **2012-10-12**, the community fork's is **2016-07-20** (message: *"emptying content"*). There is also no licence payload — Apache-2.0 is stated in `README.markdown` and `NOTICE` only. A Rails 2 application last touched in 2016 is not a starting point. |
| [os4ed/openSIS-Classic](https://github.com/os4ed/openSIS-Classic) | **Not shelved — licence unverified.** Repository resolves, but no licence payload was served on any path tried this pass. Commonly cited as GPL-2.0; this KB does not publish a licence it has not read. |

## How to add AI on top

### Pattern A — Moodle AI subsystem (public education, lowest friction)
Moodle has shipped a provider-pluggable AI subsystem since **4.5**; **5.0** added `Explain`
and AI Reports, and **5.1** added DeepSeek support plus **per-course and per-activity
enable/disable** — which is precisely the granularity an EU AI Act compliance story needs.
Point the subsystem at a local Ollama/vLLM endpoint and no student prompt leaves the
institution. Vendor sources describe a 5.2 standardized subsystem and a 5.3 LTS in
October 2026; treat those specific version claims as **vendor-sourced and unconfirmed**
against Moodle's own release notes.

> Core Moodle still has **no** AI question generation, **no** conversational practice and
> **no** AI over SCORM content. Those three absences are the studio's billable surface.

### Pattern B — LTI tool, not a fork (works against any compliant LMS)
Build the agent as an LTI 1.3 tool with [`tsugi`](https://github.com/tsugiproject/tsugi)
(Apache-2.0), [`pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) or
[`lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) (Apache-2.0).
The tool stays permissively licensed and the client's GPL/AGPL LMS stays untouched — this is
how you keep a copyleft platform from colouring the deliverable.

### Pattern C — XBlock inside Open edX (MOOC and corporate)
`openedx/XBlock` is Apache-2.0 and is the sanctioned extension point. The AGPL obligation
attaches to `edx-platform` itself, so keeping the agent in an XBlock is both the cleanest
architecture and the cleanest licence boundary.

### Pattern D — start AI-native (corporate L&D)
`Selleo/mentingo` (MIT) already has the agent, the tracing and the MCP endpoint. When the
client has no LMS legacy to protect, starting here beats retrofitting Moodle.

### Pattern E — offline-first, where the network is the constraint
`learningequality/kolibri` (MIT) is a complete platform that assumes no connectivity, so the
agent has to follow it: a quantised model served locally (Ollama) against Kolibri's own content
channels, with `fsrs4anki`-style scheduling for retention and sync-on-contact for telemetry.
Nothing in this stack is copylefted and nothing in it requires a data centre — which is the
only honest architecture for rural deployments in LATAM and low-bandwidth APAC.

### Pattern F — the Brazilian municipal network, sovereignty by construction
`i-educar` (GPL-2.0) holds enrolment, attendance and results; `i-diario` (AGPL-3.0) is where
teachers already work. Build the AI layer **outside both**, as a service the portals call over
HTTP/LTI, and the copyleft stays on the platform side of the boundary while the studio's model
code, prompts and evaluation harness stay permissive. The pitch writes itself: federal
software-public provenance, Brazilian maintainers, local inference, no student prompt leaving
the municipality.

### Pattern G — Sunbird for APAC public-sector scale (MIT, national precedent)

```
Sunbird-Ed/SunbirdEd-portal (MIT) + project-sunbird/knowledge-platform (MIT)
  └── already proven at DIKSHA scale under NCERT
  └── agent layer attaches at the knowledge-platform API, not in the portal
       ├── tutoring: ls1intum/Iris + Pyris (MIT) pointed at the course content store
       ├── assessment: numbas/Numbas (Apache-2.0) embedded, browser-side execution
       └── learner model: pykt-toolkit (MIT) over Sunbird telemetry
  └── MIT throughout — no copyleft obligation anywhere in this stack
```

Why this pattern and not "import a Western LMS": a ministry that already runs DIKSHA has the
platform, the content pipeline and the political precedent. The engagement is the **agent
layer over an existing national deployment**, which is a far shorter path than a migration —
and every component above is MIT or Apache-2.0, so nothing in it forces source disclosure.

**The licence point worth putting in a pitch:** Sunbird, Iris, Pyris, Numbas and pykt are all
permissive. This is the only full stack in this file with **no copyleft component at all**.

### Pattern H — Canvas, through an MIT MCP server, not a fork *(new in pass 267)*

The highest-frequency North American situation in this file, and the one it previously had no
answer for: **the client already runs Canvas.**

1. **Leave `instructure/canvas-lms` alone.** It is AGPL-3.0 with 78,765 commits. A fork is both a
   copyleft obligation and a maintenance commitment against the fastest-moving codebase in
   education open source.
2. **Reach it with [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, 295★, 1,026 commits, v1.14.0 Oct 2026)** — 102–126 tools plus 8 agent skills over the
   Canvas API, speaking MCP to whatever assistant the client runs. **MIT, so the deliverable
   stays yours.**
3. **Put the pedagogy in a component that is also permissive** — [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris)
   (MIT) for the LLM pipeline with RAG over instructor material, or `tutor-mcp` (MIT) for a
   constrained tutoring loop.
4. **Grade with BSD-3, not with the LMS** — [`Submitty`](https://github.com/Submitty/Submitty) or
   [`otter-grader`](https://github.com/ucbds-infra/otter-grader), the latter of which already ships
   a **Canvas autograder adapter**.
5. **Keep the AGPL boundary at the network edge.** You call Canvas's API; you never link its code.
   Nothing in your deliverable derives from an AGPL work, and that is a sentence a client's legal
   team can check.

**Why this is the pattern and not a variation:** every licence in the delivered stack is MIT or
BSD-3, the only copyleft component is the one the client already owns and operates, and no
migration is proposed. **Where the client runs Moodle instead,** the equivalent doorway is
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) — **AGPL-3.0,
open-core, 10 free tools, 1★** — or Moodle Web Services directly. Price the Moodle variant higher;
its MCP surface is roughly 1/300th as adopted as the Canvas one.

## Declared gaps

- **Retracted twice: "permissive LMS options are one deep" → three → now five.** With
  **Sunbird** (MIT, national scale) and **Artemis** (MIT, assessment-first) the permissive
  shelf is **five** deep. Each previous count was published as though settled; the pattern is
  the lesson. The original three: **OpenOLAT**
  (Apache-2.0, institutional/higher-ed, Java), **Oppia** (Apache-2.0, structured-lesson
  delivery, highest adoption at 6.9k) and **Kolibri** (MIT, offline-first). They are not
  interchangeable — OpenOLAT is the one that behaves like an institutional LMS, Oppia is
  lesson-delivery, Kolibri is offline-first distribution — so the honest pitch is *"three
  permissive candidates, each strong at a different job"*, not *"exactly one"*. Everything
  else at full-LMS scale remains GPL or AGPL.
- **Two platforms that comparison sites recommend do not survive verification.** forma.lms is
  GPL-2.0 (published as Apache-2.0) and Fedena has been abandoned for a decade. Both were
  recommended to this KB *this pass*, by 2026-dated sources. The shelf is only as good as the
  last payload read.
- **RETRACTED in pass 266: "no APAC-origin platform on the shelf."** **Sunbird is MIT, has
  38,046 commits, and is the stack under DIKSHA** — a national deployment serving Indian school
  education under NCERT. It is now on the shelf above. This was the last surviving piece of
  this base's "APAC is supply-poor" framing, and it is gone: APAC publishes at the agent layer
  (DeepTutor, 41.5k★, University of Hong Kong), the research layer (EduData, EduStudio) **and**
  the platform layer (Sunbird, MIT, national scale).
  **The failure was instrumental, not empirical.** Star-sorted GitHub topic search is
  structurally blind to ministry-funded code: Sunbird has **41 stars against 38,046 commits**,
  so no amount of re-running the same query could have surfaced it. Rank the platform layer by
  **commits and forks**; probe national programmes by name. The earlier note that APAC
  engagements imply "localisation, not a different base" now reads the other way round for
  India specifically — the base **is** national, and the work is the agent layer on top (see
  Pattern G).
- **Star counts are deliberately absent from this file.** Platform choice here turns on
  licence, stack and deployment footprint; carrying unverified star numbers forward is how
  the errors corrected above were introduced.

### Added in pass 267

- **This file published a wrong verdict about the largest open-source LMS in its own market, for
  266 passes.** Canvas was in "not on the shelf" as *"commercial SaaS, not a base to build on"*.
  Its source is **AGPL-3.0 with 78,765 commits.** 🔵 The generalisable lesson is not "check
  Canvas": it is that **"commercial product" and "closed source" are different claims**, and this
  file merged them. Any other vendor-named row deserves the same payload test — the "incumbent to
  migrate off" framing is exactly where this error hides.
- **The permissive full-platform count is unchanged at five** (OpenOLAT, Oppia, Kolibri, Sunbird,
  Artemis). Pass 267 added five platform rows and **not one of them is permissive**: Canvas
  AGPL-3.0, TAO GPL-2.0, Schul-Cloud AGPL-3.0, Tangerine GPL-3.0 — with **Kolibri Studio (MIT)**
  the single exception, and it is a companion to a platform already shelved rather than a new one.
  🔵 **Worth stating plainly because it cuts against the trend of recent passes:** the permissive
  *agent and component* layer keeps growing, while **the complete-platform layer is still mostly
  copyleft**. Five permissive platforms is the number, and commit-ranking did not raise it.
- **The offline lane is now covered end to end, at two different prices.** Kolibri (**MIT**)
  delivers content with no network; **Tangerine (GPL-3.0)** measures learning with no network.
  Pairing them gives a complete low-connectivity deployment, but the assessment half carries
  copyleft — so the integrity of the "offline-first is a licence-free lane" claim in
  [`intel/trends.md`](../intel/trends.md) (T11) holds **only for delivery**, not for assessment.
- **Public-sector platforms now exist on this shelf for three regions** — Sunbird (APAC, MIT),
  i-Educar/i-Diário (LATAM, GPL-2.0/AGPL-3.0), Schul-Cloud (EMEA, AGPL-3.0) — **and still none for
  North America**, where the public-sector code found this pass is a UK-style *service* layer
  (`DFE-Digital`, MIT) rather than a platform. That is the remaining regional hole in this file.
  **🔴 RETRACTED IN PASS 268 — and it was never a hole, it was a shelving failure.** See
  *Added in pass 268* below: the **Ed-Fi** stack is Apache-2.0, North American, and has been
  carried as *the only permissive system of record* in this base's own gap register for roughly
  200 passes. The honest correction is narrower than the retraction, though: North America
  publishes an **interoperability and system-of-record layer**, not a platform. The sentence
  should never have said "none"; it should have said **"a different layer."**
- **Still open:** `os4ed/openSIS-Classic` remains licence-unverified after a 19-path x 4-ref probe;
  `OpenEMIS`'s application source was not located; and no LATAM-origin *permissively licensed*
  platform exists — Uruguay's Ceibal, probed by hand this pass, **publishes no code at all**.

### Pattern I — Ed-Fi as the system of record for a North American engagement *(new in pass 268)*

**When the client is a US district, a state education agency, or a vendor selling into them.**
This is the pattern that was missing while this file said North America had no public-sector base.

| layer | component | licence |
|-------|-----------|---------|
| Data model | [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** |
| System of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) + [`Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** |
| New builds | [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** |
| Agent surface over the LMS beside it | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** |
| Learner event stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** |

🟢 **Why this composes cleanly:** every layer is permissive, so the deliverable has no copyleft
boundary anywhere — which is the thing an AGPL-first market (Canvas, Open edX) otherwise denies.
The agency's students are already modelled in Ed-Fi, so the integration is *conformance*, not
mapping.

🔴 **Three prices to quote from the register, not the README:**
1. **DMS adoption is a re-platforming with a data migration**, stated normatively in
   `docs/PRD-v8.0.md` (`Gap 303`). Never price it as an in-place cutover.
2. **DMS provisioning is create-only** (`Gap 314`). An AI deliverable that writes anything back —
   a predicted risk flag, an AI-assisted grade, generated evidence — is a **data-model extension
   and a re-provision**. The cheap route is to write AI-generated evidence into the **LRS**
   instead and leave the system of record alone.
3. **OneRoster is absent from DMS v8.0** (`Gap 309`) while native OneRoster 1.2 shipped in the
   **ODS/API 7.3.2** line. Say which line you are quoting.

⚠️ **Do not brief a state count.** Neither Ed-Fi README names a state or an agency; the 14-state
list is third-party, and the South Carolina department page that would settle it **did not resolve
from this environment**. Quote the licence (payload-read) and let the client's own procurement
confirm their state's status.

### Pattern J — Code.org's engine without Code.org's curriculum *(new in pass 268)*

**When the client must deliver a K-5 or K-12 AI/CS literacy mandate.** Four jurisdictions now
mandate AI instruction (`Gap 367`), and this is the shape of the only honest answer.

- ✅ **Reuse under Apache-2.0:** [`code-dot-org/code-dot-org`](https://github.com/code-dot-org/code-dot-org)'s
  **platform** — 215,796 commits of lesson delivery, progress tracking, classroom management and
  block-based programming environment. This is a genuinely enormous permissive engine.
- 🔴 **Do NOT plan to reuse:** the lessons, videos, artwork, characters, sounds, logos or fonts.
  The payload confines them to *"Code.org's own web site, mobile applications, or social media
  channels ... without modification or embedding in another format"*, and the `NOTICE` shows why
  Code.org could not grant them anyway — the engaging activities are **licensed entertainment IP**
  (Minecraft, Star Wars, Frozen, Ice Age, Angry Birds, Plants vs. Zombies, Gumball, The Bad Guys),
  plus **Font Awesome Pro**.
- 🟢 **So the engagement is content origination on a free engine**, and the budget belongs in
  instructional design and localisation, not in platform build. 🔵 **Say this in the first
  meeting.** A client who has seen Code.org assumes the curriculum comes with the code; the
  licence says the opposite, and discovering that after the SOW is signed is the expensive way.


### Pattern K — an MEA ministry mandate, where there is no regional platform to start from *(new in pass 269)*

🔴 **State the absence first, because it is the whole shape of the engagement.** Pass 269 ran the
Kenya / Nigeria / South Africa / Egypt legs this base specified in pass 267 and never executed.
**There is no African or Middle Eastern education platform on this shelf, and pass 269 did not find
one.** What it found instead:

- **Two African-context education agents, both serving NO GRANT** —
  [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South Africa, Grades 8–12,
  **pre-licence**: the README still carries *"Add the project's chosen license here before
  publishing"*) and [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria, no
  payload on 19 paths and no `license` field in `package.json`).
- **Two named national systems that are unreachable rather than absent** — Nigeria's **Naija Teacher
  AI** (UNESCO SDG4 case study, offline-first, target **1.5M teachers by Q3 2026**) **states no
  licence**; Kenya's **Kytabu SOMANASI** is **proprietary**.
- **One piece of Africa-engaged permissive code, already on this base's shelves** —
  [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse)
  (**MIT**, Sierra Leone MBSSE national lesson plans → structured JSON, corpus shipped) —
  **research-grade, a method rather than a dependency.**

🟢 **So the platform layer is imported and the national layer is built.** The stack is
`kolibri` (**MIT**, offline-first, 39,803 commits) for delivery, `instructional_agents` (**MIT**,
EACL'26) for teacher-facing authoring, `Claw-ED` (**MIT**) for local-first drafting, `lineage-skill`
(**Apache-2.0**) for provenance, and `Tangerine` (**GPL-3.0** ⚠️, 5M+ assessments across 65
countries per its README) **deployed beside the deliverable, never linked into it**, where national
assessment is in scope. The per-country work — parsing the national curriculum into structure,
language, teacher capability — is the billable part and the part that does not port.

🔵 **Entry point differs by country, and getting it wrong wastes the first meeting.** Kenya and Egypt
have **national anchors** (the KDEAP rollout; the UNESCO teacher-competency framework of
**2026-06-03**), so a ministry conversation has an instrument to attach to. **South Africa has no
national instrument at all** — its Draft National AI Policy 2026 was **abrogated on 2026-04-27** —
while **North-West University became the first SA university with an official AI policy in January
2026**. **Enter South Africa at institution level.** Full recipe: [`compose/patterns.md`](../compose/patterns.md) `P19`.

⚠️ **And two things not to say.** Egypt's delivery platform is reported three different ways
(**QUREO** / the Japanese **Kiryo** / a **Sprix** contract approved January 2026) — **brief the
framework, not the vendor.** And every regional figure here is **secondary-source grade**: `p268`
established the non-GitHub DNS failure as environmental, and no ministry document was read.

## Pass 270 note — what the platform shelf does and does not cover, after the EMEA re-verification

🟢 **No platform rows were added this pass, and none needed changing.** The only supply leg run
(`Gap 367`'s Spanish limb) returned nine repositories, eight of them university student course
portfolios and the ninth already held. The three generic platform/ERP/SIS legs were **deliberately
not re-run** — `p269` measured them saturated across four consecutive passes and instructed that
they be spent last. **This file's shelf is stable, and that is a measurement, not an omission.**

🔴 **But pass 270 found the shelf's sharpest gap by looking at what a national government actually
bought.** Estonia — the one EMEA jurisdiction where national-scale deployment is a *measured fact*
rather than a plan — has **~half of its 20,000 upper-secondary students** on an **OpenAI-partnered
proprietary platform** (Education and Research Minister **Kristina Kallas** to *Politico*, **May
2026**). 🔵 **Every platform on the shelf above is open source, and the country that moved fastest
in Europe did not pick one of them.**

🟢 **That is not an argument that the shelf is wrong — it is the sales argument for the shelf**, and
it has a number attached. The **Sanoma Learning 2026 European Teacher Survey** (>20,000 teachers,
14 countries) found **63% of European teachers using AI** and **only 16% believing general-purpose
AI improves learning outcomes** (`T28`). **A proprietary general-purpose platform is exactly what
84% of them are unconvinced by.** The platforms here — **Moodle** (GPL-3.0, with its
provider-pluggable AI subsystem since 4.5), **Open edX**, **Canvas** (AGPL-3.0 at source),
**Kolibri** (MIT **on `develop`**, 404 on `main` — the ref matters, `p269`) — are the ones that can
be bound to a client's own curriculum and assessment rules, which is the thing the general-purpose
tool cannot do.

⚠️ **One category correction, so this file is not read as offering something it does not.**
[`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) (**CC BY-SA 4.0**, verified at
payload this pass) appears in `agents/trending.md`, `repos/trending.md` and new pattern **`P20`** —
but it does **not** belong on this shelf and has not been added to it. **It is a prompt/knowledge
framework (schemas + prompts for LOMLOE programaciones), not a running platform**: GitHub detects no
language in it, and it is 0 stars at 50 commits. **This shelf is for systems a client can stand up
and put an agent on top of.** `OpenDidactia` is read as a specification, never deployed — see `P20`
for the ShareAlike boundary that distinction rests on.


## Pass 271 note — two real platforms were on the other shelves and not on this one

🔴 **This shelf was missing two licence-verified, actively maintained systems that the base already
held elsewhere**, and the omission is recorded as a defect rather than silently patched:

| platform | where it already lived | why the absence counted |
|---|---|---|
| **Koha** (GPL-3.0, 594★, ILS) | `repos/trending.md`, `agents/trending.md` | the shelf a studio reads for *"what can we stand up"* did not list the most-deployed open-source library system |
| **H5P** (GPL-3.0 core + MIT playback) | `repos/foundations.md`, `repos/trending.md` | present in most incumbent Moodle/Canvas estates already, so it is an integration surface on nearly every engagement |

🟢 **Both were checked against this file's own "Not on the shelf — and why" table first — neither was
there**, so neither had been excluded on judgement. 🔵 **This is `T34`'s defect class on the verticals
shelf**: the datum existed, the file that needed it did not have it, and nothing in either file
contradicted the other, so no `grep` for a *disagreement* would have found it. **The check that finds it
is asking, of each shelf, "what should be here that is held somewhere else?"**

🟢 **The H5P row also discharges the register's `ACTION PW`** by doing what it asked — naming the
repository in the cell. The MIT-vs-GPL "conflict" was **two repositories with two grants**, so both
prior cells were right and the defect was the project-level cell. **Every multi-repository project on
this shelf now needs its repository named**, and the commercially load-bearing consequence is stated in
the row: **there is no permissive H5P authoring server**, so a deliverable generates content and plays
it through the MIT runtime rather than forking the GPL core.

🔵 **No other platform rows changed, and the three generic platform/ERP/SIS legs returned nothing new
for the sixth consecutive pass** — including an explicit negative worth keeping: **no education ERP
under MIT or Apache-2.0 was located.** The permissive end of this shelf remains **OpenOLAT**
(Apache-2.0), **Oppia** (Apache-2.0), **Kolibri** (MIT, on `develop`), **Sunbird** (MIT), **Artemis**
(MIT), **Richie + Marsha** (MIT) and **Numbas** (Apache-2.0). ⚠️ One leg returned ten results from a
**single vendor's glossary** across ten localised URLs — *ten results, one source*, which is `T33`'s
single-aggregator failure in a different channel.

🟢 **New in `intel/market.md` and relevant to a Dutch engagement off this shelf:** the Netherlands has a
**dated** AI-literacy mandate — `kerndoelen digitale geletterdheid`, AI literacy explicit, **primary +
lower-secondary**, legally official **2027-08-01**, inspected from **2031**. See new pattern **`P21`**,
which wires it to **Moodle** and the **MIT** H5P runtime rather than to the GPL authoring core.

## Pass 272 — the permissive LMS recommendation is now rider-cleared, and two vendor licence claims died at payload

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) *(5 repositories)*.

🟢 **`OpenOLAT` is the single most load-bearing row on this shelf** — it is what this file tells a studio
to use when procurement rules out copyleft, so its grant deserves more than a licence label.
`p272` read the payload and found **10,982 B against stock Apache-2.0's 11,357 B**. 🔵 **A *short* Apache
file is the shape of a rider**, and `p252` found a real **Commons Clause** on a row this base had blessed
for four passes. 🟢 **Diffed: the whole terms section is byte-identical to upstream; the missing span is the
optional APPENDIX, replaced by provenance notes with no legal effect.** Recommendation stands and is now
**rider-cleared**, not merely licence-labelled. The generalisation is `T39`.

### 🔴 Two platforms a vendor comparison recommends, both refuted at payload

The brief's SIS/ERP leg surfaced two permissive claims. **Neither survived.**

| platform | the claim, and who makes it | `p272` verdict |
|---|---|---|
| **GegoK12** | *"free core is free forever under the MIT licence; 26 of 38 modules free, 12 Pro modules $100–$250"* — a vendor listing | 🔴 **NOT ESTABLISHED.** No licence payload on **15 path/ref combinations**. ⚠️ And read the claim's shape: **MIT core plus paid modules** is the open-core pattern, so even if the grant were verified it would cover a *subset* of the product a client is shown. **Do not shelve.** |
| **Fedena** | Apache-2.0, per a comparison page | 🔴 **NOT ESTABLISHED, and this independently reproduces `p265`'s refutation.** `p272` adds *why the false claim circulates*: the page asserting Apache-2.0 is **openeducat.org — a direct competitor's comparison**. ⚠️ **A licence claim sourced from a rival vendor is not a licence.** |

🟢 **One claim did survive, and it beat its own source.** `academico-sis/academico` — already shelved
here — is served **MIT at payload (1,094 B)** while the comparison page that surfaced it says the licence
*"is not named"*. **The first-hand read was better than the aggregator in the one case the aggregator was
hedging.** That is the asymmetry worth keeping: aggregators are wrong in both directions, and only the
payload settles it.

⚠️ **Unchanged by this pass:** the permissive full-platform count stays at **five**, and **no education ERP
under MIT or Apache-2.0 has been located** — now tested from a second channel (`p271` tested it from the
platform/ERP leg, `p272` from the SIS/school-management leg) with the same result.
