---
industry: education
region: Global
updated: 2026-10-31
---

# Foundational open source repos for education

The substrate an education engagement builds on or integrates with. Star counts
and metadata on this page come from the **GitHub REST index** on 2026-10-31.
**Licences on rows added or re-read in the fourth pass were read from the licence
file itself** over `raw.githubusercontent.com` (HTTP 200 from this session, while
`api.github.com` and `github.com` HTML are 403), with byte counts recorded;
older rows carry GitHub's licence determination and say so where it matters.

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

### Permissive platforms one tier down — new in the fourth pass

Not platforms of record. These are **actively maintained, permissively licensed
education platforms at the small-and-medium-institution tier**, which is where
the "no permissive substrate exists" finding stops being true.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [safytech/ulearn](https://github.com/safytech/ulearn) | **MIT** (file, 1,066 B) | 701 | Global | ⚠️ permissive, **stale stack** | "ULEARN — Open Source (FREE) LMS script." 299 forks. **The largest MIT-licensed LMS located anywhere.** Laravel **5.8** + React **16.9** — both long past end of life, so a fork is a framework-upgrade project before it is a product. Quote an upgrade estimate or do not quote it. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | **MIT** (file, 1,094 B, "Thomas Debay and project contributors") | 410 | Global | ✅ permissive | "Laravel & Filament-based school management platform for small and medium institutions." 151 forks, pushed 2026-10-30, topic **`student-information-system`**. **The permissive education SIS this KB spent three passes concluding did not exist.** The 410★/151-fork ratio is the signature of a system in real deployment. Current stack, unlike `ulearn`. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** (file, 1,079 B, **"Copyright (c) 2018-present GIP FUN MOOC"**) | 318 | **EMEA** | ✅ permissive | A Django **CMS for building education portals**, designed to front Open edX and Moodle catalogues. 94 forks. **Region placed from the licence file itself:** GIP FUN MOOC is France Université Numérique — the same publisher as `openfun/ralph` below. Two MIT components, one French public publisher. |
| [iblai/lms](https://github.com/iblai/lms) | **MIT** (file, 1,063 B, "ibl.ai") | 208 | Global | ✅ permissive | "Skills intelligence platform — discover courses, track competencies, earn credentials, and accelerate workforce development." Next.js 15 / React 19, created 2026-03-04. **The first open-source asset located for the digital-credentials and skills-pathways trend**, which had been single-source commentary for three passes. |
| [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** (file, 11,362 B) | 54 | APAC | ✅ permissive, very young | Self-hosted **multi-tenant** LMS — course builder, trainer and student portals, progress tracking. Django + React + Flutter, created **2026-10-07**. Explicit `moodle-alternative` and `corporate-training`. Region inferred from the publisher, **not stated on the repo**. |
| [Azure/Moodle](https://github.com/Azure/Moodle) | **MIT** (file, 1,090 B, "Microsoft Corporation") | 185 | Global | ✅ permissive tooling | Not a platform: **MIT deployment tooling for scalable Moodle clusters on Azure**. 187 forks on 185★, i.e. consumed as a template. Worth citing to a client as the attach-don't-fork doctrine practised by Microsoft against a GPL-3.0 platform. |

**The population, with a denominator — because scarcity claims need one.**
`topic:learning-management-system license:apache-2.0 stars:>50` returns **2
repositories in the world**: `TutorLoom` (54★, three weeks old) and
`AcademicsToday/academicstoday-django` (Apache-2.0 confirmed from `LICENSE.md`,
11,358 B, 220★, **created 2015**, effectively stale).
`topic:lms license:mit stars:>80` returns **15**, and the topic is polluted —
it includes `SWE-agent` (20,693★, a coding agent), `tompazourek/Colourful` (298★,
a .NET **colour-space** library, "LMS" as in cone response) and `freeitsm` (118★,
ITSM). **Six of those fifteen are education platforms.** So the whole permissive
LMS population above 50★ is roughly **eight repositories**, the largest is 701★
on an end-of-life stack, and Moodle alone carries 7,600★ under GPL-3.0.

⚠️ **One archived trap.** [`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI)
— MIT, 132★, 52 forks, an LTI tool surfacing the Microsoft Learn catalogue inside
an LMS — is **archived**. It looks exactly like the component an engagement would
reach for, it is permissive, and it is dead. The `microsoftarchive` org name is
the only warning on the URL.

## Interoperability and analytics layer

Where the permissive licences live, and the layer an AI integration actually
touches.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | North America | ✅ permissive | The xAPI specification: how systems communicate learner activity. The vocabulary any learning-analytics or agent-telemetry design should speak. ADL Initiative (US). |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | Global | ✅ permissive | Turns an application into a full **LTI 1.3** tool provider: launches, Deep Linking, Assignment & Grade Services, Names and Role Provisioning, Dynamic Registration. **Still the single most important repo on this page for a Globant engagement** — the sanctioned, licence-clean way to attach new software to a copyleft LMS without touching its code. Brazilian maintainer. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 153 | EMEA | ⛔ copyleft | The H5P interactive-content runtime. **Licence correction carried forward:** earlier passes recorded H5P as MIT. It is **GPL-3.0**. Norway. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (file, 1,072 B, "Jonathan Putney") | 362 | Global | ✅ permissive | "A modern SCORM JavaScript runtime library" — **SCORM 1.2, SCORM 2004 and cross-frame**, tagged `offline-first`. 85 forks, pushed 2026-10-30. **New in the fourth pass, and it closes a hole this KB never named:** three passes built the attach doctrine on LTI, MCP and xAPI and omitted **the standard the installed base actually ingests**. xAPI is the better specification; SCORM is the incumbent, it is what corporate L&D procurement asks for by name, and it is what `Selleo/mentingo` ships alongside xAPI. A permissive, maintained SCORM runtime means Globant-built courseware can be delivered into a client's existing LMS **without touching the LMS and without an xAPI migration project first.** |
| [openfun/ralph](https://github.com/openfun/ralph) | MIT | 51 | EMEA | ✅ permissive | Learning Record Store for learning analytics; consumes xAPI statements. The permissive LRS option. France Université Numérique — same publisher as `richie` above. |

## Content, standards and evaluation layer (new this pass)

The layer that answers *"is what the agent produced actually any good, and does
it match the curriculum?"* — and the layer where licences stop being binary.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | ⚠️ **split: code MIT, datasets "By data publisher"** | 164 | Global | ⚠️ conditional | "The data layer for smarter educational AI" — enriched datasets linking academic standards, curricula, learning progressions and instructional guidance under one schema, reachable via browser explorer, agent plugins, local files, a REST API **and an MCP server**. Run by Learning Commons (`learningcommons.org`), country not stated. **Licence mechanics matter here:** the API reports `NOASSERTION` because the file is `LICENSE.md` and because the grant is split — README badges read "License for Knowledge Graph code: MIT" and "License for Knowledge Graph datasets: By data publisher", and **some datasets are gated**. The code is safe; each dataset must be cleared individually. |
| [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **three-tier split: code MIT · prompts CC BY 4.0 · two corpora CC BY-NC-SA 4.0** | 87 | Global | ⚠️ **conditional — the corpora are non-commercial** | "Evaluation for AI outputs against trusted educational rubrics" — research-backed rubrics for scoring generated instructional content. TypeScript, 17 forks, pushed 2026-10-31. **The only rubric-scoring asset located in this KB**, and the natural quality gate in front of any content-generating agent. **Licence RESOLVED in the fourth pass** by reading `main/LICENSE.md` (1,615 B), after three passes carried it as unresolved. It grants: *evaluator **code** → MIT*; *evaluator **content**, i.e. the prompts and settings → CC BY 4.0*; ***Annotated CLEAR Corpus** → CC BY-NC-SA 4.0*; ***Annotated PERSUADE 2.0 Corpus** → CC BY-NC-SA 4.0*. **The code and the rubric prompts are commercially usable with attribution; the two annotated corpora are NC and cannot ship in a billable deliverable or a commercial regression suite.** The upstream originals (CommonLit's CLEAR Corpus, PERSUADE 2.0) are themselves CC BY-NC-SA 4.0, so there is no cleaner version upstream to substitute — an engagement must bring its own corpus. Note the direction: this is the **inverse** of its sibling `knowledge-graph` (code MIT / data by publisher). |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | ✅ permissive | 1,143 questions from real teacher-qualification exams — CDPK (920, general pedagogy) and SEND (223, special needs). Measures whether a model knows how to *teach*, not whether it knows the subject. |

## Content-production layer (new in the fourth pass)

Not education projects. Horizontal tools that the industry's highest-volume
artefact — lecture decks, courseware, interactive texts — is actually built from.
**This layer was invisible to four passes of sweeping because every sweep filtered
on an education topic and none of these carries one.**

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (file, 1,069 B, on both `main` and `master`) | **71,498** | Global | ✅ permissive | **The largest permissively licensed repository anywhere in this knowledge base** — 1.4× DeepTutor, 1.7× OpenMAIC. "AI turns documents or topics into real, native PowerPoint decks — with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own `.pptx` templates." Python, **5,578 forks**, created 2025-12-10, pushed 2026-10-30. **Why it belongs here:** `.pptx` is the format schools and universities actually exchange; *"support for your own `.pptx` templates"* is institutional branding compliance, which is what normally kills generated-content pilots; and audio narration from speaker notes is a lecture-capture path for free. Deliberately **not** on the agent shelf — it is not an education agent. ⚠️ **Provenance unverified:** 71,498★ and the owner profile cannot be read from this session, so **no region is assigned**. For a component this central, check it independently before client-facing use. |
| [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (file, 1,069 B) | 1,034 | Global | ✅ permissive | "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created **2026-10-03** — 1,034★ in four weeks. Topics include **`scorm`** and `interactive-textbook`, so pair it with `scorm-again` to deliver into an existing LMS. Also shelved as an agent in [`../agents/top.md`](../agents/top.md). ⚠️ Copyright line is a pseudonym. |
| [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** (file, 1,069 B, "Assaf Kipnis") | 557 | Global | ✅ permissive | Topic in, **course of 2-minute audio lessons with cited sources** out; web research plus ElevenLabs TTS. Python, 67 forks, created 2026-10-14. The only content generator in this KB that **starts** from citation provenance rather than retrofitting it. |

**How to use this layer honestly.** These produce *artefacts*, not *assessed
learning*. Nothing here knows whether the deck it generated is pedagogically
sound or on-syllabus — which is exactly what the evaluation layer above is for,
and why pattern **P-569-B** wires a quality gate between them rather than
shipping generator output directly.

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
  platform internals; and — **new in the fourth pass** — **SCORM**
  (`scorm-again`, MIT) to deliver courseware *into* the platform the way the
  installed base already ingests it. All four are permissive. This remains the
  default, and it now covers content delivery as well as launch, read and
  telemetry.
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
  true, now bounded on three sides and **measured**. It holds for the **LMS of
  record** category. It does **not** hold for the **institutional repository**
  (DSpace, BSD-3-Clause, category leader), it is **weakening** for the
  **AI-native LMS** niche (`mentingo`, MIT, 102★), and as of this pass it does
  **not** hold at the **small-and-medium-institution SIS** tier
  (`academico`, MIT, 410★, 151 forks). The denominator is now on the record: the
  entire permissive LMS population above 50★ is about **eight repositories**.
  A client needing a permissive substrate at *university* scale still assembles
  rather than adopts; a language school, training institute or private school
  group no longer has to.
- ~~**No African-origin repo appears anywhere on this page.**~~ **Closed, with the
  qualification stated above:** `AI-for-Education` is an LMIC-focused
  organisation with MIT tooling built against Sierra Leonean curriculum and
  Ugandan language data, but its own **location is not stated** and its repos are
  0–13★. African *artefacts* are mapped; African-*domiciled* publishers are not.
  That is the next pass's question, and it should be asked on GitHub's index, not
  the open web — which is what finally worked here.
- ~~**`NOASSERTION` is not the same as "no licence".**~~ **Closed as a question
  and promoted to a catalogue.** Both `learning-commons-org` repos reported
  `NOASSERTION`; both are now read first-hand and they are **different** split
  grants — `knowledge-graph` is code-MIT / data-per-publisher, `evaluators` is
  code-MIT / prompts-CC-BY-4.0 / **corpora-NC**. `digitalinnovationone/dio-agent`
  (2,750★) returns no `license` field at all and has no file on either branch:
  genuinely unlicensed. `24kchengYe/human-skill-tree` (586★) matched no licence
  filter and is **AGPL-3.0 on `master` with a dual-licensed `skills/`
  directory**. **Four distinct states behind one ambiguous API value, plus a
  branch-name trap.** The rule that resolves all of them is now executable from
  this session: **read the file, on every filename, on every branch.**
- **The instrument that made this possible is new and should be used
  deliberately.** `raw.githubusercontent.com` returns HTTP 200 here;
  `api.github.com` and `github.com` HTML return 403; MCP `get_file_contents` is
  **repo-scoped** and refuses third-party repositories; `search_users` exposes no
  `location`. Twenty-one licence files were read this pass. **Region, by
  contrast, got harder** — owner country is unobtainable by any available route,
  so new rows are placed only from licence-file copyright holders (which is how
  `richie` was placed to EMEA), publisher or payment-stack signals (flagged as
  inferred), or left **Global**.
- **Licence defects cluster in the agent layer.** Across three passes: platforms
  state copyleft clearly and accurately; agents claim MIT in prose with no file
  (`mcp-canvas-lms`), ship share-alike content licences on code-shaped artefacts
  (`Auto-Empirical-Research-Skills`, CC BY-SA 4.0, 4,843★), or state nothing at
  2,750★. The substrate is honest; the fast-moving layer is not.
- **No open-source learning-analytics *dashboard* was located**, only the LRS
  (`ralph`) that feeds one. The presentation layer of learning analytics appears
  to be entirely commercial; not re-verified this pass.
- **Horizontal tooling is systematically under-covered, and the cost is now
  quantified.** `ppt-master` — **MIT, 71,498★**, the largest permissive repo in
  this KB — went unfound for four passes because every sweep filtered on an
  education topic and it carries none. The same blind spot presumably hides
  document parsers, TTS pipelines, assessment-item generators and video tooling
  that education depends on and nobody tags `education`. **Next pass: sweep by
  capability (`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`,
  `topic:scorm`) crossed with licence, not by industry topic.**
- **`ulearn`'s maturity is unassessed beyond its stack.** 701★ MIT is the largest
  permissive LMS found and Laravel 5.8 is five major versions behind. Nobody
  should be told it is a starting point without an upgrade estimate attached.
