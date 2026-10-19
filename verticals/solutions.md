---
industry: education
region: Global
updated: 2026-10-19
---

# Vertical platforms — education

## Pass 327 — the platform tier did not move for a fifth pass, and the tier that did move is a *vendor stack*, not a platform

🔴 **The prescribed `open source platform education ERP CRM MIT Apache` query returned nothing new
for the fifth consecutive pass.** It returned OpenEduCat's own glossary pages almost exclusively.
🟢 **One useful confirmation came out of it: those pages state OpenEduCat is LGPLv3** — weak
copyleft, built on Odoo — **which agrees with this KB's existing grade and refutes nothing.** 🔵
**Record it as a measured result: the permissive education-platform shelf is enumerated, and this
file has now re-walked it five times without adding a row.**

🟢 **What arrived instead is a tier this file has had to assemble by hand: a single vendor shipping
the data spine, the agent layer and the evaluation layer as three separate permissive-code
repositories.** `learning-commons-org` — **`knowledge-graph` (161 ★), `agent-skills` (40 ★,
Apache-2.0, `NOTICE` naming Anthropic, PBC), `evaluators` (86 ★)** — plus the named companion
`anthropics/k12-teacher-skills` (Apache-2.0, 575 ★). **All four licences read first-hand this
pass; full reads in `agents/top.md` and `repos/foundations.md`.**

🔵 **It is not a platform and does not replace one. It is what each platform below expects the
institution to supply, and what p326 said Moodle, Open edX, Canvas and Chamilo each leave empty —
except that this time the standards are *United States, state by state*, and the agent and
evaluation tiers come with it.**

| platform | licence | what it already has | what the Learning Commons stack adds on top of it |
|---|---|---|---|
| **Moodle** | GPL-3.0 | Competency frameworks and learning plans, **empty on install**; its own AI subsystem since 2026 | US state standards with **state↔CCSS crosswalks carrying a `jaccard` score** — so a Moodle competency can be mapped to another state's framework instead of re-authored |
| **Open edX** | AGPL-3.0 | Course structure, no cross-course skill model | The **Math Coherence Map** as a real learning-progression layer, plus the Eedi **misconceptions** graph for item generation |
| **Canvas** | AGPL-3.0 | Outcomes and rubrics, institution-authored | **19 evaluators** to score generated outcomes and feedback before a teacher sees them — the thing no LMS ships |
| **OpenOLAT** | Apache-2.0 | The permissive LMS; no LTI boundary needed (P8) | 🟢 **The only fully permissive pairing in this table: Apache-2.0 platform + Apache-2.0 skills + MIT evaluator code.** Build the whole stack with no copyleft seam |
| **`openfun/ralph`** | 🟢 MIT | xAPI learning records | A stable standards ID to key statements to, and an evaluator to judge the generated feedback those records trigger |

### 🔴 The procurement caveat, and it is in the data tier, not the code

**The code is permissive throughout. The data is not uniform, and the vendor says so in three
places.** `knowledge-graph` labels every dataset — and in some cases every *download* within a
dataset — **Open**, **Open + Gated** or **Gated**:

| access type | terms | examples read from the repo this pass |
|---|---|---|
| **Open** | Typically **CC BY 4.0**; a smaller number **CC0** | US academic standards (Math · ELA · Social Studies · Science), crosswalks, WIDA ELD Standards Framework, XQ Competencies, Carnegie Skills Progressions, Math + ELA learning components, Eedi Misconceptions Graph, Math Coherence Map, English Learners Success Forum guidelines |
| **Open + Gated** | Split **within one dataset, at the download level** | 🟡 **IM® v.360** — *Scope and sequence* is **Open**; *Instructional materials* and *Assessment materials* are **Gated** |
| **Gated** | 🔴 **No open licence. Publisher approval and a separate agreement** | **OpenSciEd**; **Learner Variability Navigator** (math and literacy models) |

🔴 **And the clause to put in front of counsel, quoted from `LICENSE.md`: compiling datasets into
your own build means you "take on the licensing and attribution obligations of every dataset and
download you include," and Learning Commons' "role as distributor doesn't consolidate those into a
single license for your build."** 🔵 **So the one thing you must not do is the obvious thing —
export the whole graph and call the result CC BY 4.0.** Attribution travels to each original
source, not to the distributor.

🟢 **The practical consequence for a bid is clean and worth stating plainly: build on the Open
tier and the whole stack is shippable; the moment a scope item needs IM® instructional materials
or OpenSciEd, it stops being an open-source integration and becomes a publisher negotiation —
and that is a line item, not a surprise.** The `agent-skills` README says the same thing in one
sentence: *"Knowledge Graph datasets carry varying licenses. Some datasets aren't readily
accessible by default due to license requirements."*

🔴 **Unverifiable this pass, stated as such:** the per-dataset licence labels above are read from
the repository's `README.md` and `LICENSE.md`. **The dataset catalog pages that carry the
authoritative download-level terms are on `docs.learningcommons.org` and
`platform.learningcommons.org`, and the network policy answered 403 to CONNECT for both.** No
record count is asserted. **A pass with reachable vendor docs should pin the download-level terms
before this stack enters a signed scope.**

## Pass 326 — the platform tier did not move, and the layer that did move goes *underneath* it

🔴 **The prescribed `open source platform education ERP CRM MIT Apache` query returned nothing new
for the fourth consecutive pass.** It surfaced OpenOLAT, Frappe LMS, Sakai, OpenEduCat, Moodle,
Open edX, Canvas, RosarioSIS and Gibbon — **every one already in this KB or its gap list.** 🔵
**Record it as a measured result, not as silence: the permissive education-platform shelf is
enumerated, and this file has now re-walked it four times without adding a row.**

🟢 **What did arrive is a tier this file has never had — the curriculum data that plugs under all
of them.** `withmarbleapp/os-taxonomy` (**ODbL-1.0 + CC BY-SA 4.0**, 6.1 ★k, read first-hand this
pass — see `repos/foundations.md`) is **1,591 micro-topics and 3,225 prerequisite edges across
seven national curricula.** It is not a platform and does not compete with one. **It is the thing
Moodle, Open edX, Canvas and Chamilo each expect the institution to supply and none of them
ships.**

| platform | licence | what it already has | what the taxonomy adds underneath it |
|---|---|---|---|
| **Moodle** | GPL-3.0 | Competency frameworks and learning plans, **empty on install** | A populated competency framework with **prerequisite ordering and age bands** — the part an institution normally pays a consultancy to author |
| **Open edX** | AGPL-3.0 | Course structure, no cross-course skill model | A skill graph spanning courses, so prerequisite gaps are detectable across a programme rather than within a unit |
| **Canvas** | AGPL-3.0 | Outcomes and rubrics, institution-authored | 1,591 outcomes with **1,591 ready assessment prompts** and 1,556 observable `evidence` descriptors |
| **`openfun/joanie`** (MIT) | 🟢 MIT | Headless enrolment, orders, certification | The *content* model Joanie deliberately does not own — it stays headless, the taxonomy stays the spine |
| **`openfun/ralph`** (MIT) | 🟢 MIT | xAPI learning records | A stable topic ID to key every xAPI statement to, which is what makes mastery computable rather than merely logged |

🔵 **The deployment note that matters for a platform integration, and it is not the usual
copyleft warning.** The ODbL obligation attaches to the **database**, not to the application.
Loading the taxonomy into a Moodle competency framework and running a tutor against it is a
*produced work* and triggers nothing; **extending the graph — adding topics, adding edges,
re-banding ages for a client's jurisdiction — produces a derivative database and that must be
published under ODbL.** 🟢 **For a public-sector or ministry client that is usually a selling
point rather than an objection:** the client's curriculum extension becomes a public asset with
their name on it. **For a private edtech it is a boundary to design for** — keep client-specific
extensions in a separate overlay table keyed by topic ID, rather than editing the graph in place.
`tbh-23/Homestead` (MIT, 15 ★) implements exactly this boundary and is worth reading before
wiring it into any platform; see **P13**.

### Two licences re-read first-hand this pass, because the roundups disagreed

- 🟢 **Sakai is ECL-2.0, and this KB was already right.** A 2026 comparison listed it as "Apache
  2.0" and another as "ECL v2" in the same breath. `master/LICENSE` read first-hand: *"Educational
  Community License, Version 2.0 (ECL-2.0) … consists of the Apache 2.0 license, modified to change
  the scope of the patent grant in section 3 to be specific to the needs of the education
  communities using this license."* **Both descriptions are reaching for the same fact and only
  one is correct.** The distinction is not cosmetic — **the patent grant is narrower than Apache
  2.0's** — and it is the kind of thing a client's counsel will find after the proposal has gone
  out. This file's row stands unchanged.
- 🟢 **Gibbon is GPL-3.0 specifically**, not the unversioned "GPL" the comparisons print.
  `GibbonEdu/core` `master/LICENSE` and `main/LICENSE` both return 200; the file is **35,121 bytes
  of GNU GPL v3 text.** An all-in-one K-12 school-management platform (admissions, timetabling,
  attendance, behaviour, markbook) — **the LMS/SIS hybrid the OpenEduCat row describes, at a
  different licence.** 🔴 **Recorded here rather than added as a row: it has no AI surface of its
  own, so it belongs on the far side of the integration boundary like Moodle and i-Educar** — the
  agent sits beside it, never inside it.

## Pass 325 — the permissive education ERP exists, it is headless, and it was in this KB's history for 198 passes

🔴 **The prescribed `open source platform education ERP CRM MIT Apache` query returned nothing new
for the third consecutive pass** — OpenEduCat (LGPL-3.0), ERPNext and Dolibarr (GPL-3.0), OFBiz and
Corteza (Apache-2.0, education layer is a build), and one vendor glossary that names Odoo as
OpenEduCat's base and then states OpenEduCat is LGPLv3. **The standing conclusion held: at the
platform tier this market is copyleft.** 🔵 **And it was wrong in one specific, important way,
which the search channel was never going to surface.**

🟢 **`openfun/joanie` is a headless education ERP under MIT, published by the operator of France's
national public MOOC platform** — *"a headless ERP for education to manage course
enrollment/subscription, payment and certificates delivery"* — and this KB has held it in
`repos/trending.md` since **p127** without ever carrying it here, where the question
*"is there a permissive Odoo for education?"* actually gets asked. **The answer is a qualified
yes:** headless and MIT, purpose-built for education rather than a general ERP with a module bolted
on, but **it is an API and a data model, not a product** — enrolment, subscription, payment and
certificate issue with the front end left to `richie` or to you.

🟢 **With it comes the rest of a coherent self-hostable public-sector stack, all MIT, all
re-verified first-hand this pass** (rows below; full licence evidence in `repos/foundations.md`):
`ralph` as the **xAPI Learning Record Store**, `potsie` as **Grafana dashboards-as-code** over it,
`ashley` as a **multi-tenant course forum**, `richie` as the portal CMS (already here since p315),
and `django-lti-toolbox` for the LTI seam. 🔴 **Two honest subtractions:** `warren`, the analytics
UI, **declares itself a proof of concept not suitable for production**, and `django-lti-toolbox`
**has no release and has not been pushed since 2024-11-14.** 🔵 **The commercially useful sentence:
this is the first stack in this file that an EU public buyer can adopt end-to-end without taking on
AGPL** — and the one AGPL-3.0 repository in the whole organisation, `openedx-docker`, carries it
because **Open edX is AGPL**, not because the operator chose copyleft. That is trend 4's
permissive-agent / copyleft-platform split showing up *inside a single org's repository list*.

| platform | licence | shape | how it sits beside the LMS |
|---|---|---|---|
| **`openfun/joanie`** (30 ★) | 🟢 **MIT** | Django REST Framework, Docker-first, Terraform + OpenStack Swift for media | **Not beside the LMS — underneath the commercial layer.** It owns enrolment, subscription, payment and certificate delivery; the LMS keeps the learning. The seam a training business actually bills on |
| **`openfun/ralph`** (51 ★) | 🟢 **MIT** | LRS (HTTP/xAPI, ADL standard) + CLI + library; Elasticsearch; PyPI `ralph-malph`, Docker image, Helm chart | **Alongside, collecting.** Open edX tracking logs and xAPI in, one queryable event history out. The audit substrate for any claim about learning |
| **`openfun/potsie`** (11 ★) | 🟢 **MIT** | Grafana dashboards as **Jsonnet/grafonnet**, 114 commits | **Reporting, as code.** Teacher and programme dashboards reviewable in a pull request, on a stack institutions already operate |
| **`openfun/ashley`** (12 ★) | 🟢 **MIT** | Django, **multi-tenant** | **Inside the course.** The cohort surface a tutor product needs, one deployment across many courses or institutions, and a natural xAPI emitter into `ralph` |


## Pass 324 — the platform tier did not move again, and a tier this file never had is now populated

🔴 **The platform search returned nothing new, for the second consecutive pass.** The prescribed
`open source platform education ERP CRM MIT Apache` query returned what it returned in p323 and
before: **Apache OFBiz** and **Corteza** (Apache-2.0, both already here and both requiring the
education layer to be built), **Huly/`hcengineering/platform`** (Apache-2.0, already here),
**Krayin** (MIT, a general CRM with no education surface), **OpenEduCat** (already here, LGPL-3.0),
**ERPNext** (GPL-3.0) and **Dolibarr** (GPL-3.0), plus one MIT toy (`asadbekme/education-crm`, a
small student/teacher/admin portal) and one unnamed Apache-2.0 "desktop university administration
platform" that the result did not identify and this pass could not resolve. 🔵 **The standing
conclusion is unchanged and is now three passes old: at the platform tier this market is
copyleft, and the permissive options are general-purpose frameworks on which the education layer
is a build, not a configuration.** The empty search is recorded rather than omitted.

🟢 **What did move is a tier this file has never carried: assessment integrity as a deployable
platform layer.** p324 measured three engines first-hand (detail in `repos/foundations.md`,
wiring in `compose/patterns.md` **P11**), and they belong here rather than only in the agent tier
because they are **self-hosted services an institution runs**, in the same sense as an LMS:

| platform | licence | shape | how it sits beside the LMS |
|---|---|---|---|
| **`jplag/JPlag`** (2.0k ★, 376 forks, **5,708 commits**) | 🟡 **GPL-3.0** | Java service, **Maven Central**, CLI or Java API, local report viewer — *"No data will leave your computer!"* | **The most-maintained platform-tier artefact added to this file in many passes**, and it is a *companion* to the LMS, not a plugin: twenty-odd languages of code similarity and collusion detection behind one HTTP endpoint. 🔴 GPL-3.0 → separate process, never linked. 🔴 **Its README names no LMS or Moodle integration at all**, so the LMS seam is your build |
| **`NoplagLabs/noplag-engine`** (86 ★) | 🟢 **Apache-2.0** | FastAPI + **PostgreSQL** (winnowing fingerprints as GIN-indexed `bigint[]`), `docker compose up`, five REST endpoints | The permissive text-similarity service. Load the institution's own prior submissions as the corpus — *"the open-source engine matches against your local corpus only."* 🔴 **No authentication as shipped**; it is the open core of hosted noplag.com |
| **`sunilgentyala/aegis-integrity`** (17 ★) | 🟢 **MIT** | Python package with a **local web UI** (`aegis ui`), **MCP server**, Docker Compose, GHCR image | The citation/provenance layer. Runs on the institution's own machine; sends **reference metadata** to Crossref and **never the document**, with an explicit `offline=true` |

🔵 **Why this matters for the platform read specifically.** Every other tier in this file is a
story about copyleft incumbents and permissive edges. **The integrity tier inverts it:** the
largest artefact is GPL-3.0, and the two *permissive* ones are the newer, smaller, more
agent-shaped entrants — the same shape the agent tier has, arriving in a tier this file had
written off as *"MOSS-style code-plagiarism detectors"*. **An institution that already runs Moodle
or Open edX can add this tier without touching the platform licence**, which is the practical
reason it belongs in a verticals file: it is the rare AI-adjacent capability that composes with a
copyleft LMS by sitting **next to** it rather than inside it.

🔴 **Declared gap, new and specific: no integrity engine in this tier ships an LTI 1.3 or Moodle
plugin.** JPlag's README names no LMS integration; `noplag-engine` exposes REST only;
`aegis-integrity` exposes MCP and a local UI. **The LMS seam is a build in every case** — which is
the same conclusion `intel/trends.md` trend 6 reaches from the other direction (MCP, not LTI, is
where 2026 integration is actually happening), and one more datum for the eight-pass LTI gap.

**Pass 320 · 2026-10-19 (sixth pass of this date). No platform added; two readings re-confirmed
first-hand, and one candidate named for promotion.**

**`CaviraOSS/PageLM`'s licence was re-read this pass and pass 319's finding stands exactly:**
`LICENSE.md` is present and it is the **"CaviraOSS Community License"** — free to use, share and
modify for **personal and educational** purposes, with **commercial use or resale requiring prior
written permission from CaviraOSS**. 2.0k ★, 234 commits. **It is not OSI-approved and Globant
cannot bill against it.** Re-verified rather than inherited because this is the single most
commercially consequential licence reading in this file, and pass 318 established that secondary
sources misstate licences in this sector.

**Named for promotion if a client asks for assisted marking: `laurauguc/grading_assistant`
(GradeMate) — MIT, 4 ★, but 260 commits.** Teacher-facing grading of written work with curated
**or teacher-uploaded rubrics** (`rubrics/` plus a `load_grading_rubric_data` management command),
ReactJS over Django. It sits in `agents/top.md`'s rejection list because **it is a teacher tool, not
an agent** — which is precisely what makes it a candidate for *this* file. **One hard constraint
before it is proposed: it requires a `GOOGLE_API_KEY` and the model is not pluggable as shipped**,
so a client with a sovereignty or vendor-neutrality requirement cannot take it unmodified. It is not
added as a row this pass because its platform-tier behaviour (multi-tenancy, auth, data retention)
has not been read.

**Pass 319 · 2026-10-19.** Twenty-seven platforms — the real systems a client is already running,
or would run, with AI built on top. **Checked** says which pass took the licence/star reading.

**The headline this pass closes a gap pass 318 explicitly left open.** Pass 318 wrote: *"No
LATAM-originated **platform** at this tier."* **`portabilis/i-educar` closes it with 34,948
commits** — Brazilian school-management software, originally built by the municipality of Itajaí
(SC) and published on the federal government's Portal do Software Público in 2008, now maintained
by Portábilis, with 720 stars and 549 forks. Two related Brazilian systems come with it
(`portabilis/i-diario`, `ipti/br.tag`). None of the three has any AI features, which is precisely
why they belong here: **they are substrate with a mandate, waiting for the layer Globant sells.**

**The second finding is a licence shift, and it is the uncomfortable one.** The three
highest-starred *new* platforms read this pass are **not open source**: `CaviraOSS/PageLM` (2.0k ★,
a bespoke "Community Licence" requiring written permission for commercial use),
`canyongbs/advisingapp` (340 ★, **Elastic Licence 2.0**, Gates-Foundation-supported) and — in
`agents/top.md` — `cn-math-taxonomy` (780 ★, CC BY-NC 4.0). Pass 318 found that secondary sources
*misstate* licences; pass 319 finds that the licences themselves are **moving away from open
source** at the popular end of this market. Detail at the end of this file.

| Platform | Repo | Licence | ★ | Checked | What it is | AI-on-top angle |
|---|---|---|---|---|---|---|
| Joanie | https://github.com/openfun/joanie | 🟢 **MIT** (`LICENSE` read first-hand, *Copyright (c) 2021 France Université Numérique*) | 30 | p325 | **Headless education ERP** — course enrolment and subscription, payment, and certificate delivery, over Django REST Framework. Built to sit behind the `richie` catalogue (*"Power up Richie catalog"*); Docker-first with `make bootstrap`/`make demo`; Terraform scripts and docs for media on OpenStack Swift. 45 open issues, active | **This is the permissive answer to "an Odoo for education", and the AI angle is the certificate and entitlement boundary.** Put an agent on the catalogue and the tutor; leave enrolment, payment and credential issue to a deterministic ERP with an API — then every AI-side decision that affects a learner's entitlement has an auditable, non-generative system of record behind it. **Also the cleanest place to attach an LRS-backed completion rule** (`ralph`) instead of a hand-written one |
| Ralph | https://github.com/openfun/ralph | 🟢 **MIT** (`LICENSE.md` read first-hand, *Copyright (c) 2020-present France Université Numérique*; 🔴 `LICENSE` 404s) | 51 | p325 | **xAPI Learning Record Store, CLI and library** to the ADL LRS standard, with converters for **Open edX tracking logs**; Elasticsearch backend; FastAPI + Pydantic; shipped as `ralph-malph` (PyPI), `fundocker/ralph` (Docker Hub) and an `openfuncharts/ralph` Helm chart. Replaced the operator's own deprecated Learning Locker deployment | **The data layer that makes an AI claim checkable, and the one almost nobody installs first.** An agent that recommends, scaffolds or gates needs an event history that predates its own deployment, or there is nothing to measure against; this is the permissive, standards-based place to put it. **Wire it as the capture layer under any pattern in `compose/patterns.md` that promises evidence** |
| Potsie | https://github.com/openfun/potsie | 🟢 **MIT** (`LICENSE.md` read first-hand, *Copyright (c) 2021-present France Université Numérique*) | 11 | p325 | **Grafana dashboard suite for learning analytics**, authored as Jsonnet with grafonnet; 114 commits | **Dashboards-as-code is the deliverable a public buyer can audit.** The reporting half of an analytics engagement, versioned and reviewable, on infrastructure the institution already runs — and the production-ready alternative to `warren`, which declares itself a proof of concept. 🟡 The Ralph binding is not documented in its README; read the Jsonnet |
| Ashley | https://github.com/openfun/ashley | 🟢 **MIT** (`LICENSE` read first-hand, *Copyright (c) 2020-present GIP FUN MOOC.*) | 12 | p325 | **Self-hosted multi-tenant discussion forum for learning**, Django | **The cohort layer, and multi-tenancy is why it is listed.** One deployment serving many courses or institutions is the shape a studio actually ships; a per-course forum is not. **AI-on-top:** discussion is the richest unstructured signal in a course — summarisation, unanswered-question detection and escalation-to-human routing all sit here, and every event can be emitted as xAPI into `ralph` |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.2k | p315 | Web conferencing purpose-built for virtual classrooms | Post-session agents: transcription, participation analytics, summary-to-LMS |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | p317 | LMS + Studio behind large-scale MOOCs and corporate academies; 68,824 commits. The older `openedx/edx-platform` URL redirects here | Agents as XBlocks or LTI tools; AGPL makes the network boundary non-negotiable |
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.5k | p317 | The world's most deployed open source LMS; 123,234 commits | **Ships its own core AI subsystem since 4.5 — read the Moodle note below before proposing a custom tutor** |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | p316 | The open LMS by Instructure; 78,765 commits | Same AGPL discipline as Open edX — and see the Project Athena note below |
| frappe/lms | https://github.com/frappe/lms | AGPL-3.0 | 3.3k | p318 | "Easy to use, open source, Learning Management System" on the Frappe framework; 7,837 commits, 1.6k forks. Courses/chapters/lessons, batches with Zoom live classes, quizzes, PDF assignments, certificates | **No AI features in the product at all** — a clean, well-adopted LMS substrate for an external agent. Distinct from `frappe/education` below |
| LearnHouse | https://github.com/learnhouse/learnhouse | **AGPL-3.0 + separate Enterprise Licence** | 2.4k | p318 | "Next-gen Open Source learning platform"; 2,804 commits, 580 forks. Next.js/React/Tiptap over FastAPI/Postgres/Redis; block editor, assignments, discussions, analytics, certificates | **AI-native**: "context-aware AI for learning & teaching", AI-generated playgrounds/simulations, code execution with auto-grading in 30+ languages. Google Gemini + LlamaIndex in the stack. **Open-core — see caveat** |
| PageLM | https://github.com/CaviraOSS/PageLM | **"CaviraOSS Community Licence" — NOT open source** | 2.0k | p319 | Study-material platform: contextual chat over PDF/DOCX/MD/TXT, Cornell-style SmartNotes, spaced-repetition flashcards, quizzes, AI podcasts, voice transcription, homework planner, exam simulation, debate practice; 234 commits, 277 forks; Node/TS + LangChain/LangGraph, Vite/React, JSON storage with optional vector DB, Docker Compose; Gemini, OpenAI, Anthropic, Grok, MiniMax, **Ollama (fully local)**, OpenRouter | **Free for personal and educational use; commercial use or resale requires prior written permission from CaviraOSS.** The most capable feature set added this pass and the one Globant cannot bill against. Use it as a requirements checklist |
| ClassroomIO | https://github.com/classroomio/classroomio | **AGPL-3.0 + enterprise `LICENSE_KEY` features** | 1.7k | p319 | Customer/partner/employee training platform; 2,127 commits, 399 forks; SvelteKit + Tailwind over Hono, Postgres, Redis, Better Auth; course builder, cohorts, certificates, 10+ languages, branded academies on custom domains, learning paths, REST API and webhooks | **AI-native and MCP-native**: AI Lesson Tutor for learners, an AI course assistant for authoring (disabled by default, needs a provider key — OpenAI, Google or Anthropic; picker exposes Gemini 2.5 Flash and GPT-4o), and **an MCP server that lets external agents create courses and drive the platform**. Open-core: SSO, token-auth and no-tracking are enterprise-only behind a licence key |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | p317 | Learning, teaching, research and collaboration platform used in higher ed; 55,483 commits | ECL-2.0 is an Apache-2.0 derivative with an academic-attribution twist — the most permissive mature LMS core here |
| Kolibri | https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline-first learning platform for low-connectivity settings; 39,803 commits. Re-verified first-hand this pass | The only MIT general platform — AI can embed directly, but must run on-device or batch-sync. **README describes no AI features**; the platform is the delivery substrate, the agent is yours |
| Tutor | https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | p315 | Docker-based Open edX distribution | How you actually stand up Open edX in an engagement; the plugin system is the clean AI insertion point — and how `openedx-ai-extensions` installs |
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 889 | p315 | Education ERP on the Odoo framework — SIS, LMS, finance, HR, CRM | The Odoo-of-education: admin-side agents (enrolment, scheduling, fee chasing) rather than tutoring |
| i-Educar | https://github.com/portabilis/i-educar | GPL-2.0 | 720 | p319 | **Brazil's open source school-management system** — "um software livre de gestão escolar totalmente on-line" for secretaries, teachers, coordinators and managers; **34,948 commits** on the 2.12 branch, 549 forks, 85 watchers; PHP/Laravel, Composer, Vite, Docker; originally developed by the Prefeitura de Itajaí (SC) and released on the Portal do Software Público do Governo Federal in 2008; maintained by Portábilis; ships an **Educacenso module** for the national school census | **No AI features at all** — the LATAM substrate an agent sits beside. GPL-2.0, the only v2 licence here besides RosarioSIS, so keep agent code external |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 669 | p316 | School management system on the Frappe/ERPNext framework; 1,095 commits | ERPNext-shop clients already run the framework; GPL-3.0 confirmed from `license.txt`, not assumed |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 647 | p316 | K-12 Student Information System (PHP + PostgreSQL/MySQL); 8,034 commits | A real, maintained open source SIS. **GPL-2.0** — the only v2 licence in this KB; keep agents external |
| menthor | https://github.com/menthorlabs/menthor | Apache-2.0 | 582 | p319 | "Plataforma gratuita e open-source de ensino de programação" — free open source platform for teaching programming; 273 commits, Nuxt/Vue, Turborepo, Clerk; Portuguese-language docs and a `menthor.io` domain | **Archived by its owner on 2024-12-12 and read-only.** No AI. Recorded because it is permissively licensed, Portuguese-language and 582 ★ — LATAM authorship in this sector has history, and this is what it looks like when it stops |
| OpenOLAT | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | 448 | p317 | Web-based LMS for teaching, learning, assessment and communication; 31,877 commits; frentix GmbH, from the University of Zurich's OLAT 7.1 | **The most permissively licensed mature LMS in this KB.** Agent code can link directly — no LTI boundary required. See P8 in `compose/patterns.md` |
| Advising App | https://github.com/canyongbs/advisingapp | **Elastic Licence 2.0 — source-available, not OSI** | 340 | p319 | Student-success platform and recruitment **CRM** for colleges and universities: student messaging, guided outreach, student profiles, dynamic groups, campus-system integration; **9,495 commits**, 76 forks; TALL stack (Tailwind, Alpine, Laravel, Livewire) on Filament; Canyon GBS Inc., created and released with support from the **Gates Foundation** Postsecondary Success team | **AI Chat answers routine student questions from approved campus content.** The nearest thing to "Salesforce for student success" in the open; source-available licensing means read, learn, and do not fork into a deliverable |
| edrys | https://github.com/edrys-org/edrys | MPL-2.0 | 334 | p319 | "Open-source app that helps you teach remotely" — live classrooms, **remote labs driving real equipment**, modular extensions; 275 commits, Deno + Vue; sponsor logos include TU Bergakademie Freiberg | **"This project is not under active development anymore"**, superseded by a serverless peer-to-peer successor (`edrys-labs`). No AI. The remote-lab model is the part worth reading for engineering and vocational engagements |
| Richie | https://github.com/openfun/richie | MIT | 316 | p315 | Education-portal CMS (France Université Numérique) | MIT front end over an AGPL Open edX back end — the licence-safe catalogue/portal layer |
| freelingo | https://github.com/artcc/freelingo | AGPL-3.0 | 188 | p316 | Self-hosted AI language-learning platform: CEFR study plans, AI tutor, voice, flashcards, spaced repetition; 1,168 commits | A complete AI-native vertical to study or fork — AGPL, so fork consciously |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 151 | p315 | Interactive content types embedded in Moodle/Open edX/Canvas | Generate H5P content JSON with an agent; the renderer stays untouched, so GPL stays contained |
| i-Diário | https://github.com/portabilis/i-diario | **licence not shown on the repository page — verify** | 117 | p319 | Teacher portal integrated with i-Educar ("Portal do professor integrado com o software livre i-Educar"); **15,834 commits** on the 1.6 branch, 62 forks; Ruby on Rails with Node/Yarn, RSpec, Playwright, Docker; tagged `software-publico` | No AI features described. **A LICENSE file exists but the page does not name the licence — read the file before any use.** The teacher-facing half of the Brazilian stack, and therefore where a teacher-facing agent would attach |
| mentingo | https://github.com/Selleo/mentingo | MIT | 96 | p316 | Open-source AI-native LMS with an AI mentor and role-play, self-hostable; 1,348 commits | The first MIT AI-native LMS in this KB — small, but licence-clean |
| Sunbird | https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Portal of India's national digital-education stack | The base for an APAC public-sector engagement; see the caveat in `repos/foundations.md` |
| ipti/br.tag | https://github.com/ipti/br.tag | **conflicting: README says BSD-3-Clause, sidebar links GPL-2.0 — unresolved** | 20 | p319 | TAG (Tecnologia de Apoio à Gestão), free school-management software built as a social technology for basic education and **especially rural schools**, with **data sync for schools without internet**; 3,959 commits; PHP/Yii; IPTI (Instituto de Pesquisas em Tecnologia e Inovação) with the Prefeitura Municipal de Santa Luzia do Itanhy/SE | No AI features. **Two licences claimed in one repository — resolve before use.** The offline-sync design is directly relevant to pattern P5, and it is Brazilian rather than imported |
| openedx-ai-extensions | https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | p318 | **Official Open edX AI plugin**, built by eduNEXT (Bogotá) as FC-111; 703 commits, 11 forks; docs v2.6.0 dated 2026-09-01. Multi-provider via **LiteLLM** (OpenAI, Anthropic, Gemini, local models); Learning + Authoring MFE integration, content summarisation, config-driven workflows, XBlock AI service registration | **LATAM-authored — and explicitly not production-ready.** See below |

## Pass 323 — the platform tier did not move, and the honest version of that is a short section

**No rows added, no rows changed, and that is a finding rather than a skipped step.** The mandated
vertical-platform search (`open source platform education LMS SIS MIT Apache 2026`) returned
**one vendor's marketing content for ten of ten results** — OpenEduCat's own comparison and glossary
pages, in eight languages. **It confirmed nothing and licensed nothing:** the pages discuss Moodle,
Open edX, Sakai, ILIAS, Canvas, Chamilo and OpenEduCat as a landscape and **state the licence of
none of them**, while asserting the general shape this file already holds — that open-source LMS
platforms are mostly GPL, AGPL, LGPL, BSD or Apache, and that OpenEduCat consolidates LMS, SIS, fees
and a parent app on one database. **Nothing in the result set was specific to 2026.**

**Recorded for three reasons:**

1. **The licence split in this file stands unchanged over 27**, re-stated rather than re-counted: the
   platform tier remains predominantly copyleft against a predominantly permissive agent tier, and
   OpenOLAT remains the crack in that rule. **No new candidate was found to test it with.**
2. **It is further evidence for this pass's method note** (`intel/market.md`): the generic
   category query returns vendor aggregation, and every usable artefact this pass came from a query
   naming an artefact type, a statute or a repository. **For the platform tier specifically, the
   productive channel has been GitHub organisation sweeps** — p321 and p322 found `edu-sharing` and
   its twelve-service pipeline that way, not through platform searches.
3. **An unrecorded empty search reads exactly like a covered one.** This file's own p322 line about
   regional gaps applies to categories too.

**What p324 should do instead of repeating this query:** the platform-tier leads currently outstanding
are **Moodle's AI subsystem** (already a section here — re-check its version and whether the agentic
features moved), **`openedx/openedx-ai-extensions`** (recorded, still not shippable — re-check), and
**OpenEduCat's actual repository and licence**, which this pass could not establish because every
result was the vendor's own marketing. That last one is a concrete, answerable question and belongs
in the next pass's first batch.

## openedx-ai-extensions: the LATAM gap is no longer empty, and the row is still not shippable

Six passes of this KB have declared the same gap: **no LATAM-authored open source education
infrastructure.** Pass 318 found it, and in the least star-visible place possible.

`openedx/openedx-ai-extensions` is an `edx-platform` plugin housing tools and helpers for working
with AI. It sits under the **official `openedx` GitHub organisation**, is covered by the Open edX
maintainers programme, and its README states it was **"developed by edunext as part of FC-111"** —
FC-111 being an Open edX funded-contribution project. It has **703 commits** and its documentation
is published on `docs.openedx.org` at **version 2.6.0, changelog dated 2026-09-01** (1.0.0 was
2025-12-24). Architecture decision records cover dynamic workflow configuration, LLM caching
strategy and XBlock AI service registration. It installs through Tutor.

**eduNEXT is headquartered in Bogotá, Colombia.** Its co-founders, Felipe Montoya and Juan Camilo
Montoya, have been named Open edX core committers since at least the 2021 Core Contributor pledge,
and the company describes 12+ years of contribution to the platform. *(Provenance note: the Bogotá
location is sourced from a vendor-profile directory and the co-founder's own regional LinkedIn
profile, not from an official eduNEXT corporate page, which this session could not retrieve. The
Open edX core-committer relationship is documented in the Open edX wiki. Treat the headquarters as
well-supported, not primary-sourced.)*

**Three things a studio lead must hold at once:**

1. **The gap is closed in the sense that mattered.** This KB's LATAM finding has been "high
   consumption, zero authorship" for five passes, with the Linux Foundation's 65%/46% figures for
   Mexico and Brazil as the backdrop. That sentence is now wrong. A Colombian company is the named
   author of the official AI extension layer for one of the world's two largest open source LMS
   platforms. **For a LATAM engagement this is a credibility asset before it is a technical one.**
2. **It is explicitly not usable in production.** The README states: *"This plugin is in active
   development and should not be used in production environments."* It is labelled Experimental
   throughout and self-describes as a proof-of-concept. Nothing in this KB's patterns should depend
   on it this quarter.
3. **It is AGPL-3.0**, like the platform it extends. So it changes nothing about the architectural
   boundary: Globant's own agent code still belongs on the far side of it.

**What to do with it now:** treat it as the reference for *how Open edX intends AI to be
extended* — the XBlock AI service registration pattern and the LiteLLM provider abstraction are
the platform's own answers, and building against those shapes is cheaper than inventing a parallel
one that the platform later contradicts. Track its releases. The moment it drops "experimental",
every Open edX engagement's AI integration estimate changes.

## The Brazilian stack — pass 318's last platform gap, closed, and it has no AI in it

Pass 318 declared: *"No LATAM-originated **platform** at this tier. The LATAM finding this pass is
an extension layer for a North-American-origin platform, which is a real change but not the same
thing."* **Pass 319 found the platforms.** Three of them, all Brazilian, all substantial:

| System | Commits | What it is | Licence |
|---|---|---|---|
| `portabilis/i-educar` | **34,948** | School management: enrolment, records, staff, reporting, an Educacenso module for the national school census | GPL-2.0 |
| `portabilis/i-diario` | **15,834** | The teacher portal that integrates with i-Educar — the daily register, grades, attendance | **not named on the page; read the file** |
| `ipti/br.tag` | **3,959** | "TAG", school management as a social technology for basic and **rural** education, with **data sync for schools without internet** | **conflicting — README BSD-3-Clause, sidebar GPL-2.0** |

**Provenance is the part that matters commercially.** i-Educar was originally developed by the
**Prefeitura de Itajaí (Santa Catarina)** and released through the **Portal do Software Público do
Governo Federal in 2008**; Portábilis maintains it now. br.tag came out of **IPTI** with the
Prefeitura Municipal de Santa Luzia do Itanhy (Sergipe). These are municipally originated,
publicly released systems with second-decade commit histories — the Brazilian public sector's own
software, not a vendor's open-core play.

**None of the three has any AI feature.** That is the opportunity in one sentence: *the installed
base exists, the data model exists, the mandate exists (`intel/market.md`: 87% of LAC institutions
using AI somewhere, 26% with a strategy), and the intelligence layer is unbuilt.* Put beside
`bncc-dev`'s verified curriculum data and MCP server (`repos/foundations.md`), **a LATAM engagement
can now be scoped end-to-end on Brazilian open source**: i-Educar/i-Diário for the records, BNCC
for the standards, an agent on the far side of the boundary for the teaching. See pattern **P10**.

**Three constraints to carry into the SOW:**

- **GPL-2.0 on i-Educar is the strictest platform licence in this file after RosarioSIS**, and
  GPL-2.0 has no AGPL-style network clause but also no Apache-style patent grant. Keep Globant's
  agent in a separate process talking over HTTP; do not build an in-tree module.
- **Two of the three have unresolved licences** — i-Diário's is not displayed on its GitHub page
  at all, and br.tag claims BSD-3-Clause in its README while its sidebar links GPL-2.0. **Read the
  LICENSE files before quoting.** This is pass 318's rule applied twice in one pass.
- **PHP and Ruby, not Python.** i-Educar is PHP/Laravel, i-Diário is Rails, br.tag is PHP/Yii. A
  Python-first studio integrates across the network boundary anyway, which this KB already
  mandates — but staffing a modification to the platform itself is a different skill mix.

## edu-sharing — the EMEA OER repository platform, found at p321 and copyleft

Pass 321's `openeduhub` finding (`repos/foundations.md`) names the platform its tooling sits on, and
it is a real system of the Odoo/Moodle/OpenMRS kind this file exists to track.

**`edu-sharing/edu-sharing-community-repository` — GPL-3.0, 30 ★, 16,110 commits, running since
2007.** Read first-hand at p321. The README describes it as developing "networked E-Learning
environments for managing and sharing educational contents" **across organisations** — i.e. a
federated repository for educational content and its metadata, not an LMS and not a course player.
Backend, Frontend, Cordova and webapp trees; the page shows no dominant language and the Releases
section is empty, with releases pointing to a separate `edu-sharing-projects-community` repository.
The branch read was **`maven/fixes/10.0`**.

**The version number is the useful detail.** `openeduhub/ki-prompt-benchmark` benchmarks the
metadata-generation prompts in **`mds.xml` v10.0** — the same major version. So the AI tooling and
the platform are in step, and the metadata schema the prompts write into is the platform's own.
That is a complete, inspectable chain from harvester to vocabulary to platform to AI prompt, all
public, in one jurisdiction.

| Layer | Artefact | Licence | Commits |
|---|---|---|---|
| Platform | `edu-sharing/edu-sharing-community-repository` | 🟡 **GPL-3.0** | 16,110 |
| Harvest | `openeduhub/oeh-search-etl` | 🔴 **none** | 1,397 |
| Metadata | `openeduhub/oeh-metadata-vocabs` | 🟢 **CC0-1.0** | 938 |
| Tutor | `openeduhub/tutor-chatbot` | 🟢 **Apache-2.0** | 10 |
| Evaluation | `openeduhub/ki-prompt-benchmark` | 🟢 **Apache-2.0** | 3 |

**Read the licence column before proposing the stack.** The two layers with real engineering behind
them are the two Globant cannot simply take: the platform is **GPL-3.0** and the harvester has **no
grant**. The three permissive artefacts are the three with 10, 3 and 938 commits — and the 938 is
data, not code.

**What that implies for an EMEA engagement, stated plainly.** This is not a fork-the-platform
opportunity. It is an **integrate-and-extend** one: take the CC0 vocabularies as your competency
model, build against edu-sharing's API the way `tutor-chatbot` does rather than linking its code,
and keep your own tutor and evaluation layers permissive. The GPL-3.0 platform then stays a
deployed service you talk to over HTTP — the same posture this file takes on Moodle and OpenOLAT.
Pattern **P21** in `compose/patterns.md` wires it.

## Pass 322 — edu-sharing re-verified, and the pipeline that runs on it is now mapped

**No platform row added this pass. One platform re-read first-hand and one structural addition to
what is already here.**

**`edu-sharing/edu-sharing-community-repository` re-verified at p322, and p321's reading stands
exactly:** **GPL-3.0** (sidebar and `LICENSE.txt`), **30 ★, 20 forks, 16,110 commits** on the
`maven/fixes/10.0` branch building `maven-fixes-10.0-SNAPSHOT`, a project running since 2007, Maven
with separate Backend and Frontend trees, a Cordova folder, an Alfresco module path, Docker and
Kubernetes packaging. **No AI features are described in the README or the About section** — which is
the point: the AI lives in the services around it, not in it. One new and verifiable detail: **the
repository root contains a `CLAUDE.md`**, an AI-assistant configuration file. Recorded as observed;
the page does not explain its contents, and it says nothing about product features.

**The structural addition: this platform is no longer the whole EMEA public-sector story.** Pass 322
enumerated all 67 repositories of `openeduhub`, the operator account that runs WirLernenOnline on
edu-sharing, and read sixteen first-hand. Around the GPL-3.0 platform sits a **twelve-service AI
metadata pipeline** — LLM extraction into eleven schemas, a human-review canvas with per-field
confidence badges, MinHash deduplication, Flesch/Wiener readability, Lighthouse accessibility and
licence screening, a Pyro Bayesian metadata predictor, a Keras discipline classifier shipping its
weights, bulk prompt running, a factual-accuracy judge and a unified gateway. **Rows for all twelve
are in `repos/foundations.md`; the recipe that assembles them is P22 in `compose/patterns.md`.**

**Why that changes how this file should be used for an EMEA bid.** The platform question
("which LMS or repository?") is answered here and is copyleft almost everywhere. The *buildable*
question is the service layer, and there the licences divide by architectural layer rather than by
product: **119 commits of Apache-2.0 interaction shells and a 519-commit Apache-2.0 generated API
client are takeable; 790 commits of GPL-3.0 analysers are service-boundary-only; and 1,852 commits
containing every model and every harvester carry no licence at all.** The permissive surface of
Germany's publicly funded education AI contains none of its machine learning — so for a public OER
buyer, **the platform is integration work and the pipeline is build work**, which is the better half
of the engagement anyway.

**The deployment evidence, because "committed" and "running" are different claims.** The
Manifest V3 browser extension `metadata-browser-plugin-fuerAPI` (Apache-2.0) points at a live
backend host for both `/generate` and guest `/upload`. This KB has not probed that host — the
sandbox reaches github.com only — but a shipped extension configured against a deployed endpoint is
the strongest evidence available from the code that this pipeline is in use and not a prototype
shelf.

## Moodle ships its own AI subsystem now — check it before proposing a tutor

Moodle's core **AI subsystem** (since 4.5, documented through 5.3) is not a plugin a client has to
find; it is in the platform. Two concepts matter when scoping:

- **Providers** — in **Moodle 5.1** the documented set is **Azure AI, DeepSeek, Ollama API and
  OpenAI API**, with **DeepSeek new in 5.1**. Because the OpenAI API shape is the de facto
  standard, self-hosted gateways such as LiteLLM or LocalAI can be wired in through the OpenAI
  provider — which is the practical route to an on-premise Moodle deployment with no third-party
  data egress (and see the COPPA finding in `intel/market.md`, which makes that route a compliance
  requirement rather than a preference for US K-12).
- **Placements** — where AI actions surface in the UI. Secondary sources report **two core
  placements, the text editor and course support**; this could not be confirmed against the
  official placements documentation this pass and should be verified before it goes in a proposal.

*(Dating note: the Moodle 5.3 documentation is marked work-in-progress targeted at 2026-10-05, so
the 5.x docs are moving. Cite the version-specific docs page, not "Moodle docs".)*

**The commercial read is the same as Project Athena's.** The incumbent platform ships the obvious
AI feature for free to its installed base. Summarisation and a chat box inside Moodle are not a
deliverable any more. The deterministic pedagogy layer, the governance and audit layer, and
on-premise operation still are.

## Licence drift: at the popular end, this market is leaving open source

Pass 318's finding was that *secondary sources misstate licences*, always in the direction of
permissiveness. Pass 319 found something adjacent and worse: **the licences themselves are
changing.** Among the platforms and agents read first-hand this pass, the three highest-starred new
projects are all outside open source:

| Project | ★ | Actual terms | What it blocks |
|---|---|---|---|
| `CaviraOSS/PageLM` | 2.0k | **"CaviraOSS Community Licence"** — free for personal and educational use; commercial use or resale needs prior written permission | Any paid engagement. Bespoke, so no precedent and no lawyer's shelf opinion |
| `xiaoyang111222/cn-math-taxonomy` (`agents/top.md`) | 780 | **CC BY-NC 4.0** | Commercial use of the only curriculum-aligned maths knowledge graph in this KB |
| `canyongbs/advisingapp` | 340 | **Elastic Licence 2.0** — source-available | Hosting it as a service; forking into a deliverable |

Add the two open-core structures already in the table — `LearnHouse` (AGPL plus a separate
Enterprise Licence) and `ClassroomIO` (AGPL with SSO, token-auth and no-tracking behind a
`LICENSE_KEY`) — and **five of the most capable systems in this file are commercially unavailable
or partially withheld.**

**Why this is happening is not mysterious and it should be said to clients plainly:** an education
AI product is cheap to clone and expensive to support, so authors who want revenue reach for
community, NonCommercial or source-available terms. The consequence for a studio is operational,
not philosophical. **Three rules:**

1. **"Open source" in this sector is now a claim to check, not a category to filter on.** A GitHub
   repository with 2,000 stars and a README headed "open-source" can carry terms that forbid the
   engagement you are scoping.
2. **Read the licence *name*, then the licence *file*, then ask what it forbids.** Elastic 2.0 and
   CC BY-NC both permit reading and learning; neither permits the deliverable. Pass 318's rule —
   never a comparison article, never a badge — stands and is now insufficient on its own.
3. **Keep a two-column inventory per engagement: what we can ship, and what we may only read.**
   The second column is where most of this pass's best material lives — PageLM for features,
   cn-math-taxonomy for the prerequisite-graph shape, advisingapp for the student-success data
   model, lumen for eval harness design, LTLTutor for misconception modelling. **It is a reading
   list, and it is genuinely valuable; it is just not a bill of materials.**

## The licence-verification finding — and it should change how candidates get sourced

Pass 318 sourced platform candidates partly from "best open source LMS 2026" comparison articles.
**Three of those articles' licence claims were checked first-hand and all three were wrong, all in
the same direction — overstating permissiveness:**

| Claimed in a comparison article | Actual, read off the repo | Delta |
|---|---|---|
| LearnHouse — "Apache-2.0" | **AGPL-3.0** plus a separate Enterprise Licence | Permissive → strong copyleft + open-core |
| Frappe Learning — "MIT licence with self-hosted data ownership" | **AGPL-3.0** (`frappe/lms`) | Permissive → strong copyleft |
| Forma LMS — "Apache 2.0" | **No LICENSE file in the GitHub repo at all** (37 ★, 7,494 commits, self-described "mirror repository") | Permissive → unlicensed; default copyright |

Together with `ahmedEid1/lumen` — whose README badge says MIT while its `LICENSE` file is GPL-3.0
(see `agents/top.md`) — that is **four licence misstatements verified in a single pass**, three of
them from secondary sources and one from a repo's own README.

**The rule this KB should now state explicitly: a licence is only ever read from the repository's
LICENSE file or the licence GitHub itself renders. Never from a comparison article, never from a
badge, never from a sidebar that shows a bare "License" link.** An engagement that inherits an AGPL
obligation because someone trusted a listicle is a legal problem, not a research one.

**`formalms/formalms` is therefore rejected**, not merely unverified: an unlicensed mirror of a
7,494-commit PHP LMS is unusable regardless of what forma.lms publishes elsewhere on its own site.

## OpenOLAT remains the crack in the copyleft-platform rule

Unchanged from pass 317 and still the most useful single fact in this file for a greenfield or
EMEA-sovereign engagement: **`OpenOLAT/OpenOLAT` is Apache-2.0 with 31,877 commits** — a mature,
institution-grade LMS from frentix GmbH (Switzerland), based on the University of Zurich's OLAT
7.1. It is the only **EMEA-authored, EMEA-maintained, permissively licensed** LMS here, which lands
directly on the EMEA sovereignty requirement in `intel/market.md`.

**Read the licence file, not the sidebar.** The sidebar shows a bare "License" link with no name;
the `LICENSE` file is the full Apache-2.0 text followed by two provenance statements crediting the
University of Zurich's OLAT Zentrum and the OpenOLAT community/frentix GmbH. **Those are
NOTICE-tradition attribution statements, not additional licence terms** — the grant is Apache-2.0.

It is the one real LMS where this KB's standing architectural tax — agent code on the far side of
an LTI boundary — is **optional**. See **P8** in `compose/patterns.md`. Do not oversell it: 448 ★
against Moodle's 7.5k is not market share, and no client is migrating off Canvas to it.

## Canvas, Project Athena, and the competitive read

**Instructure announced Project Athena on 2026-07-22** — an AI study coach grounded in the
student's own Canvas course context, the first project of its "Instructure Foundry" venture,
positioned as coaching "toward mastery, not answers". It was described as under development; one
secondary report of a 7,000-student deployment at Hinds Community College could not be confirmed
against Instructure's own release and should not be repeated to a client.

The read for a studio lead: **the incumbent LMS vendor is building exactly pattern P1 natively**,
and with Moodle's core AI subsystem the same is now true at the other end of the market. Course
grounding is table stakes. Sell the deterministic pedagogy layer, the governance and audit layer,
and on-premise/offline operation.

## The licence split, recounted over 27

Permissive: **MIT (4 — Kolibri, Richie, mentingo, Sunbird)**, **Apache-2.0 (2 — OpenOLAT, menthor
*(archived)*)**, **ECL-2.0 (1 — Sakai, Apache-derived)** = **7 of 27**.
Weak copyleft: **MPL-2.0 (1 — edrys, *not under active development*)**.
Copyleft: GPL-2.0 (2 — RosarioSIS, i-Educar), GPL-3.0 (3), LGPL-3.0 (2), **AGPL-3.0 (8 — Open edX,
Canvas, Tutor, freelingo, frappe/lms, LearnHouse, ClassroomIO, openedx-ai-extensions)** =
**15 of 27**.
**Not open source: 2 — PageLM (bespoke Community Licence), Advising App (Elastic 2.0).**
**Unresolved: 2 — i-Diário (no licence shown on the page), ipti/br.tag (README and sidebar
disagree).**

Read that distribution as three facts, not one. **The platform tier is still copyleft** — 15 of 27,
and the AGPL count went from 7 to 8. **The two permissive additions this pass are both dead code**
— menthor archived in December 2024, edrys explicitly superseded — so the usable permissive set has
not grown. And **four rows are now either outside open source or of unknown licence**, a category
this file did not need before pass 319.

**The architectural consequence is unchanged and the pass reinforced it from a new direction: put
Globant's agent code on the far side of a network boundary.** LTI 1.3 tool, external service, MCP
server, webhook consumer — not inside the platform process. That holds for AGPL (which reaches
network use of a *modified* platform), for GPL-2.0 (i-Educar, RosarioSIS), and now for the
source-available rows as well, where the boundary is what keeps a reading-only dependency from
becoming a shipping one. `pylti1.3` and `tsugi` (`repos/foundations.md`) are the repos that make it
practical.

The consequence is concrete and identical in every region: **put Globant's agent code on the far
side of a network boundary** — LTI 1.3 tool, external service, MCP server, webhook consumer — not
inside the platform process. AGPL in particular reaches network use of a *modified* platform, so
leaving Canvas, Open edX or Moodle unmodified and talking to it over LTI keeps Globant's work
separately licensed. `pylti1.3` (MIT) is the repo that makes this practical, and
`repos/foundations.md` now names its alternatives.

## Declared gaps

- **No MENA- or Africa-originated open source platform** found. The region has the clearest named
  players of any in this KB — Alef Education, Classera, Abwaab, EIDU — and **all of them are
  proprietary.** That is a finding, not an absence: in MEA the open source story is deployment of
  global platforms and the AI layer is commercial. Note that the **UAE was first in the world with
  a nationwide mandatory K-12 AI curriculum (May 2025)**, so the demand signal is real and the
  supply is closed-source.
- ~~**No LATAM-originated *platform* at this tier.**~~ **CLOSED this pass**: `portabilis/i-educar`
  (GPL-2.0, 720 ★, **34,948 commits**), `portabilis/i-diario` (117 ★, 15,834 commits) and
  `ipti/br.tag` (20 ★, 3,959 commits) are Brazilian, municipally originated and publicly released.
  See the Brazilian-stack section above. **What remains true is narrower and still useful: there is
  no LATAM-originated platform with AI in it.** All three ship zero AI features, which is the
  opening rather than the gap. Note also that this is a **Brazil** finding — the Spanish-language
  topic sweep (`repos/foundations.md`) found no equivalent in Spanish-speaking LATAM, and
  public-sector deployments there still run imported platforms, notably Kolibri.
- **Blackboard/Anthology and D2L Brightspace are closed source** and so correctly absent, but they
  are LMS incumbents a client may be running. Integration is LTI 1.3 either way.
