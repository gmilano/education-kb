---
industry: education
region: Global
updated: 2026-10-31
---

# Foundational open source repos for education

The substrate an education engagement builds on or integrates with. Licences and
star counts on this page were read from the **GitHub REST API** on 2026-10-31
where the API was reachable for that repository, and from the repository page
otherwise; the source is stated per row where it matters.

**Read the licence column before the star column.** The platforms of record are
overwhelmingly **copyleft** — the opposite of the agent layer. Two exceptions
have now been established, and one of them is new this pass and important.

## Platforms of record

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8,200 | North America | ⛔ copyleft | The Open edX LMS & Studio. Python + JavaScript. The reference MOOC-scale platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | ⛔ copyleft | The world's most-deployed LMS. Note the region: Moodle HQ is in Perth, **Australia** — commonly misfiled as EMEA because of its European install base. |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 7,000 | Global | ✅ permissive | Free online learning platform built around structured, explorable lessons. Python, Angular, Google App Engine. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | North America | ⛔ copyleft | "The open LMS by Instructure, Inc." Dominant in North American higher ed, and the platform the strongest verified agent ecosystem attaches to (see [`../agents/top.md`](../agents/top.md)). |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0 + separate Enterprise Licence** | 2,400 | Global | ⛔ copyleft **and** dual-licensed | "The Next-gen Open Source learning platform for everyone." Next.js/FastAPI/Postgres/Redis, 593 forks, includes "LearnHouse AI: The Teachers and Students copilot". **Added this pass, as a correction:** the African-education search returned a **0★ fork** of this repo under an African organisation name; the real project is this one, maintained by Badr B. (`@swve`), country not stated. The licence shape is the thing to carry forward — AGPL core with features held back under a commercial licence means the open repo is not the whole product. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | 1,200 | North America | ✅ permissive | Platform for learning, teaching, research and collaboration. ECL-2.0 is an Apache-2.0 derivative written for academic consortia — permissive, with a patent clause tuned for universities. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | Global | ✅ permissive | "The offline app for universal education." The reference choice for low- or no-connectivity deployments. Python + JavaScript. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1,100 | EMEA | ⛔ copyleft | The Docker-based Open edX distribution. In practice this, not raw `openedx-platform`, is how Open edX actually gets deployed. France. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | ⛔ copyleft | LMS focused on ease of use and accessibility. Strong francophone and LATAM install base. |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | 102 | **EMEA** | ✅ permissive | **The licence exception that changes the EMEA answer.** "Open-source AI-native LMS with AI Mentor & role-play. Self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX." TypeScript, 31 forks, created 2024-08-01, pushed 2026-10-30. Ships **SCORM and xAPI** and is explicitly white-label. Maintained by **Selleo**, a software company whose GitHub profile states its location as **Poland**. MIT confirmed via the API (`license.spdx_id: MIT`). At 102★ it is not a platform of record — but it is the only AI-native LMS found that a client can fork, rebrand and keep closed. |

## Interoperability and analytics layer

Where the permissive licences live, and the layer an AI integration actually
touches.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | North America | ✅ permissive | The xAPI specification: how systems communicate learner activity. The vocabulary any learning-analytics or agent-telemetry design should speak. ADL Initiative (US). |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | Global | ✅ permissive | Turns an application into a full **LTI 1.3** tool provider: launches, Deep Linking, Assignment & Grade Services, Names and Role Provisioning, Dynamic Registration. **Still the single most important repo on this page for a Globant engagement** — the sanctioned, licence-clean way to attach new software to a copyleft LMS without touching its code. Brazilian maintainer. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 153 | EMEA | ⛔ copyleft | The H5P interactive-content runtime. **Licence correction carried forward:** earlier passes recorded H5P as MIT. It is **GPL-3.0**. Norway. |
| [openfun/ralph](https://github.com/openfun/ralph) | MIT | 51 | EMEA | ✅ permissive | Learning Record Store for learning analytics; consumes xAPI statements. The permissive LRS option. France Université Numérique. |

## Content, standards and evaluation layer (new this pass)

The layer that answers *"is what the agent produced actually any good, and does
it match the curriculum?"* — and the layer where licences stop being binary.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | ⚠️ **split: code MIT, datasets "By data publisher"** | 164 | Global | ⚠️ conditional | "The data layer for smarter educational AI" — enriched datasets linking academic standards, curricula, learning progressions and instructional guidance under one schema, reachable via browser explorer, agent plugins, local files, a REST API **and an MCP server**. Run by Learning Commons (`learningcommons.org`), country not stated. **Licence mechanics matter here:** the API reports `NOASSERTION` because the file is `LICENSE.md` and because the grant is split — README badges read "License for Knowledge Graph code: MIT" and "License for Knowledge Graph datasets: By data publisher", and **some datasets are gated**. The code is safe; each dataset must be cleared individually. |
| [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ `NOASSERTION` | 87 | Global | ⚠️ unresolved | "Evaluation for AI outputs against trusted educational rubrics" — research-backed rubrics for scoring generated instructional content. TypeScript, 17 forks, pushed 2026-10-31. **The only rubric-scoring asset located in this KB**, and the natural quality gate in front of any content-generating agent. Licence must be read before use. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | ✅ permissive | 1,143 questions from real teacher-qualification exams — CDPK (920, general pedagogy) and SEND (223, special needs). Measures whether a model knows how to *teach*, not whether it knows the subject. |

## The LMIC supply side — `AI-for-Education` (closes a three-pass gap)

Three consecutive passes of this KB declared: *"no African education platform or
agent repository appears anywhere."* That gap is now closed, and the thing that
closed it is an organisation rather than a repository.

[**AI-for-Education**](https://github.com/AI-for-Education) describes itself as
*"Empowering Education in LMIC's with AI"* and *"a collaborative hub for
developing and sharing AI tools and resources aimed at revolutionizing education
in low and middle-income countries (LMICs)."* Site `ai-for-education.org`.
**Location is not stated** on the profile, so the organisation is recorded as
EMEA on the balance of its one published benchmark paper and contact domain, and
that inference is flagged rather than hidden.

**19 repositories; 10 are MIT** (confirmed by querying GitHub's licence index,
`license:mit org:AI-for-Education`). The ones that matter:

| Repo | Licence | ★ | What it is, and why it closes the gap |
| --- | --- | --- | --- |
| [lesson-plan-parse-mbsse](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | MIT | 1 | **Sierra Leone's Ministry of Basic and Senior Secondary Education (MBSSE)** publishes Maths and Language Arts lesson plans as PDFs; this converts them to structured JSON and cleans them with an LLM. One star, and it is the most important row on this page for an African engagement: it is **real ministry curriculum, parsed, in the open, under MIT**. |
| [luganda-linguistic-benchmarks](https://github.com/AI-for-Education/luganda-linguistic-benchmarks) | — | 0 | Linguistic benchmarks for **Luganda** (Uganda). Evidence that African-language evaluation assets exist at all. |
| [global-proficiency-framework](https://github.com/AI-for-Education/global-proficiency-framework) + [gpf-alignment](https://github.com/AI-for-Education/gpf-alignment) | — / MIT | 0 / 1 | Digitising the **Global Proficiency Framework** and automating alignment to it. GPF is the cross-country learning-standards frame used where no rich national standard exists — the LMIC analogue of US state standards. |
| [nemoasr-android](https://github.com/AI-for-Education/nemoasr-android) | — | 1 | On-device ASR on Android (Kotlin). Speech recognition **without connectivity** is the binding constraint in low-bandwidth classrooms; this is the only repo in this KB that addresses it. |
| [voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | MIT | 1 | Evaluation harness for voice AI — the modality that works where literacy or devices do not. |
| [fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | MIT | 9 | The org's own LLM client library, 10 forks. The plumbing the rest depends on. |
| [edu-qurating](https://github.com/AI-for-Education/edu-qurating) | MIT | 3 | Quality rating of educational content. |
| [primerpro](https://github.com/AI-for-Education/primerpro) | — | 0 | Python port of PrimerPro decodability functions — early-reading text levelling. |

**How to read this honestly.** This is a **supply side measured in single-digit
stars**. It is not a market; it is a toolkit, and most of it is pre-1.0. But it
is MIT-licensed, it is pointed at named African ministries and languages, and it
is the only thing of its kind located in three passes of searching. For an
engagement in sub-Saharan Africa it is the starting point. For a commercial
engagement anywhere else, the GPF-alignment and decodability work is reusable
wherever a client lacks a rich standards corpus.

## Adjacent systems of record

Not learning platforms, but systems an institution already runs — and what an AI
search or discovery agent is usually pointed at.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | ✅ permissive | "(Official) The DSpace digital asset management system that powers your Institutional Repository." Java. **The most permissively licensed platform of record anywhere in this KB** — confirmed in the sidebar and in `LICENSE` on `main` ("BSD 3-Clause License, Copyright (c) 2002-2021, LYRASIS"). LYRASIS is a US non-profit. |
| [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | ⛔ copyleft | "Koha is a free software integrated library system (ILS)." Uses its **own bug tracker rather than GitHub issues** — relevant to any contribution plan. Origin not stated on the repository page. |

**Why DSpace matters more than its star count suggests.** Every other platform of
record in education is GPL or AGPL. DSpace is BSD-3-Clause, so the one category
where a client *can* own a proprietary derivative is the institutional
repository — theses, datasets, faculty output, grey literature. That is also the
corpus a RAG research agent most wants.

## What this means in practice

A client on Moodle, Open edX, Canvas or Chamilo cannot have AI features delivered
as a proprietary fork — AGPL/GPL forbid it on any hosted-service reading. The
licence-clean routes are:

- **Attach across a standard boundary.** **LTI 1.3** (`ltijs`, Apache-2.0) to
  launch a tool inside the LMS and write grades back; **MCP** (the servers in
  [`../agents/top.md`](../agents/top.md), MIT) for agent read access; **xAPI →
  LRS** (`xAPI-Spec` Apache-2.0, `ralph` MIT) for telemetry without touching
  platform internals. All three are permissive. This remains the default.
- **Or replace the substrate, which is newly possible.** `Selleo/mentingo` (MIT,
  Poland) is an AI-native LMS with xAPI and SCORM built in and white-labelling as
  a stated goal. At 102★ it carries adoption risk a Moodle install does not —
  but it is the first time this KB can offer a permissive substrate instead of
  only a permissive boundary.
- **Gate the output.** `learning-commons-org/evaluators` for rubric scoring and
  `pedagogy-benchmark` for pedagogical knowledge are the two verified ways to
  show a client that generated instructional content was *measured* and not just
  generated. Both are small; both are the only options.

## Declared gaps

- **No permissive platform of record exists at Moodle/Open edX scale.** Still
  true, and now more precisely bounded. It holds for the **LMS of record**
  category; it does **not** hold for the **institutional repository** (DSpace,
  BSD-3-Clause, category leader) and it is **weakening** for the **AI-native
  LMS** niche (`mentingo`, MIT, 102★). A client needing a permissive substrate at
  university scale still assembles rather than adopts.
- ~~**No African-origin repo appears anywhere on this page.**~~ **Closed, with the
  qualification stated above:** `AI-for-Education` is an LMIC-focused
  organisation with MIT tooling built against Sierra Leonean curriculum and
  Ugandan language data, but its own **location is not stated** and its repos are
  0–13★. African *artefacts* are mapped; African-*domiciled* publishers are not.
  That is the next pass's question, and it should be asked on GitHub's index, not
  the open web — which is what finally worked here.
- **`NOASSERTION` is not the same as "no licence", and this pass learned the
  difference the hard way.** Both `learning-commons-org` repos report
  `NOASSERTION` from the API: one because the file is named `LICENSE.md` and the
  grant is **split between code (MIT) and data (per-publisher)**, the other
  unread. A third repo, `digitalinnovationone/dio-agent` (2,750★), returns **no
  `license` field at all** — genuinely unlicensed. Three distinct states, one
  ambiguous API value. Read the file.
- **Licence defects cluster in the agent layer.** Across three passes: platforms
  state copyleft clearly and accurately; agents claim MIT in prose with no file
  (`mcp-canvas-lms`), ship share-alike content licences on code-shaped artefacts
  (`Auto-Empirical-Research-Skills`, CC BY-SA 4.0, 4,843★), or state nothing at
  2,750★. The substrate is honest; the fast-moving layer is not.
- **No open-source learning-analytics *dashboard* was located**, only the LRS
  (`ralph`) that feeds one. The presentation layer of learning analytics appears
  to be entirely commercial; not re-verified this pass.
