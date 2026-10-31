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
| [openfun/warren](https://github.com/openfun/warren) | **MIT** | 17 | EMEA | ✅ permissive | **xAPI learning-analytics dashboards — the layer this page spent five passes recording as absent.** Same operator as `ralph` and `potsie`; pushed `2026-10-11`. **Added in the sixth pass**, and not because it was found: it was already recorded in [`trending.md`](trending.md) while the fifth-pass summary on that same page was still publishing *"no open-source learning-analytics dashboard"*. France Université Numérique. |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** (`main/LICENSE.md`, 1,094 B) | 11 | EMEA | ✅ permissive | **Grafana dashboard suite for learning analytics**, written in Jsonnet — so the dashboards are generated, reviewable and diffable rather than clicked together in a UI, which is what makes them deliverable as code. Last pushed `2024-12-18`: stable rather than active. Grant read byte-for-byte in the sixth pass, *"Copyright (c) 2021-present **France Université Numérique**"*. |

## Content, standards and evaluation layer (new this pass)

The layer that answers *"is what the agent produced actually any good, and does
it match the curriculum?"* — and the layer where licences stop being binary.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | ⚠️ **split: code MIT, datasets "By data publisher"** | 164 | Global | ⚠️ conditional | "The data layer for smarter educational AI" — enriched datasets linking academic standards, curricula, learning progressions and instructional guidance under one schema, reachable via browser explorer, agent plugins, local files, a REST API **and an MCP server**. Run by Learning Commons (`learningcommons.org`), country not stated. **Licence mechanics matter here:** the API reports `NOASSERTION` because the file is `LICENSE.md` and because the grant is split — README badges read "License for Knowledge Graph code: MIT" and "License for Knowledge Graph datasets: By data publisher", and **some datasets are gated**. The code is safe; each dataset must be cleared individually. |
| [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **three-tier split: code MIT · prompts CC BY 4.0 · two corpora CC BY-NC-SA 4.0** | 87 | Global | ⚠️ **conditional — the corpora are non-commercial** | "Evaluation for AI outputs against trusted educational rubrics" — research-backed rubrics for scoring generated instructional content. TypeScript, 17 forks, pushed 2026-10-31. **The only rubric-scoring asset located in this KB**, and the natural quality gate in front of any content-generating agent. **Licence RESOLVED in the fourth pass** by reading `main/LICENSE.md` (1,615 B), after three passes carried it as unresolved. It grants: *evaluator **code** → MIT*; *evaluator **content**, i.e. the prompts and settings → CC BY 4.0*; ***Annotated CLEAR Corpus** → CC BY-NC-SA 4.0*; ***Annotated PERSUADE 2.0 Corpus** → CC BY-NC-SA 4.0*. **The code and the rubric prompts are commercially usable with attribution; the two annotated corpora are NC and cannot ship in a billable deliverable or a commercial regression suite.** The upstream originals (CommonLit's CLEAR Corpus, PERSUADE 2.0) are themselves CC BY-NC-SA 4.0, so there is no cleaner version upstream to substitute — an engagement must bring its own corpus. Note the direction: this is the **inverse** of its sibling `knowledge-graph` (code MIT / data by publisher). |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** (file, 11,323 B — see note) | 21 | Global | ✅ permissive | **Efficacy measurement, and the only asset in five passes that narrows the evaluation gap.** *"Tool for Education Research with RAndomized COnTrolled TriAls"* — an **LTI plug-in to the LMS** that differentiates the contents of online assignments into experimental treatment variations and assigns students randomly between them. It also carries the ethics apparatus that makes that legal in a school: **informed consent hidden from the teacher**, non-consenting participants filtered out of result summaries and exports, and student identifiers stripped from exports. Java, 9 forks, branch **`development`**, created 2021-05-10, pushed 2026-10-29. **Be precise about what it is:** this measures *"did this intervention change outcomes"* under randomisation — it is **not** runtime monitoring and will not tell you a deployed tutor has drifted. ⚠️ Its `LICENSE` is unmodified Apache boilerplate with the template placeholders intact (`Copyright {yyyy} {name of copyright owner}`), so the grant **names no licensor**; the `NOTICE` credits Oxford University for LTI cookie-handling code. Origin not establishable from this session, recorded Global. |
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

## Document-ingestion layer (new in the fifth pass — the capability sweep)

The fourth pass closed with an instruction to itself: *sweep by capability
(`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`), not by industry
topic.* **This is what that sweep returned, and it is the largest layer in this
KB by an order of magnitude.** Every education engagement begins with the
client's existing material — textbooks, past papers, lecture PDFs, scanned
worksheets — and **none** of these tools carries an education topic, which is why
five passes of industry-topic sweeping never saw them.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | **Apache-2.0** (file, 11,376 B) | **92,024** | APAC | ✅ permissive | *"Turn any PDF or image document into structured data for your AI."* The highest-starred asset in this entire knowledge base. Strongest **Chinese-language and handwriting** OCR in open source, which is the deciding factor for scanned worksheets and handwritten exam scripts. Pushed 2026-09-16; **11,594 forks**, 259 open issues. Baidu's PaddlePaddle organisation (China). |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + commercial thresholds** — read the note | **82,860** | APAC | ⚠️ conditional (thresholds are far above any education engagement) | *"Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows."* Strong on **formulas, tables and multi-column academic layout** — i.e. STEM textbooks, the hardest input in education. **6,857 forks**, branch **`master`**, pushed 2026-10-31. **The licence is a shape this KB had not catalogued.** GitHub reports `NOASSERTION`; `master/LICENSE.md` (3,301 B) reads *"MinerU is licensed under Apache License 2.0 and is subject to the additional terms below"*, then adds: **(1)** a separate commercial licence is required above **100 million MAU or USD 20 million monthly revenue**; **(2)** an **attribution obligation** — any online service built on MinerU must state prominently, in the interface or public documentation, that MinerU is used; **(3)** automatic termination of all rights if either is breached. **For Globant the thresholds are irrelevant and clause 2 is not** — it is a deliverable requirement that must reach the client's product team, not just legal. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (file, 11,358 B) | **77,267** | Global | ✅ permissive | The reference OCR engine, LSTM-based, **100+ languages**, **10,879 forks**, pushed 2026-10-28. Runs fully offline on commodity hardware with no model licence and no inference bill — which is why it, and not a hosted vision model, is the realistic answer for ministry and offline-first work (see pattern `P-568-F`). |
| [docling-project/docling](https://github.com/docling-project/docling) | **MIT** (file, 1,072 B) | **69,909** | Global | ✅ permissive | *"Get your documents ready for gen AI."* **The pick of this layer for most education work, and on licence grounds as much as technical ones: MIT, where its larger rivals are Apache-with-terms or Apache.** PDF, DOCX, **PPTX**, XLSX and HTML → clean markdown or JSON with layout and **table structure** preserved. Python, 5,222 forks, pushed 2026-10-31. `main/LICENSE`: *"Copyright The Docling Contributors"* — a collective holder, so **no region is assigned**, though the project is widely associated with IBM Research and is now under the LF AI & Data Foundation; neither is verifiable from this session and neither is asserted here. |
| [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | **Apache-2.0** (file, 11,358 B) | **30,129** | Global | ✅ permissive | *"PDF Parser for AI-ready data. **Automate PDF accessibility.** Open-source."* The differentiator is in its topics: `accessibility`, `a11y`, `pdf-accessibility` and **`eaa`** — the **European Accessibility Act**. Java, **2,881 forks**, pushed 2026-10-30. **This is the only asset in this KB that addresses accessibility compliance as a product feature**, and accessibility conformance is a procurement gate in EMEA public education that nothing else here answers. See pattern `P-570-B`. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** (file `LICENSE.md`, 11,360 B) | 15,651 | Global | ✅ permissive | Open-source ETL for LLMs: 20+ document types into a uniform structured form, with first-class LangChain integration. The **pipeline** choice rather than the single-document choice — right when a client hands over a repository of mixed legacy material rather than a textbook. 1,377 forks. |

## Narration, speech and retention layer (new in the fifth pass)

The accessibility and language side of the same sweep. Education's two
highest-volume accessibility requirements — **read-aloud** and **captions** — are
served entirely by permissive horizontal tooling.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [supertone-oss-archive/supertonic](https://github.com/supertone-oss-archive/supertonic) | **MIT** (file, 1,070 B, "Supertone Inc.") | 13,757 | APAC | ⚠️ **ARCHIVED — read before shelving** | *"Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX."* Bindings for Swift, Kotlin/Java, C++, C#, Go, Rust, Node, Python, Flutter and **WebGPU**; 1,566 forks. On-device multilingual TTS with an MIT grant is close to ideal for offline read-aloud. **But the `archived` flag is `true`** — the organisation is literally named `supertone-oss-archive`. The grant is clean and perpetual and the code still runs; **there will be no fixes, no security patches and no new languages.** Fork it deliberately or not at all. *The only reason this row is honest is that the `archived` field was checked — stars and licence both look excellent.* |
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | **MIT** (file, 1,070 B) | 8,165 | Global | ✅ permissive | TTS, STT and speech-to-speech on **Apple Silicon** via MLX. The practical choice when the client's constraint is "it must run on the teacher's MacBook", which in private-school and university faculty estates is common. Pushed 2026-10-31. |
| [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** (file, 1,069 B) | 6,179 | Global | ✅ permissive | *"Generate audiobooks from **EPUBs, PDFs** and text with **synchronized captions**."* Kokoro-82M under the hood. **Synchronised captions are the whole point**: a caption track is simultaneously an accessibility deliverable, a search index and a transcript, and this produces all three from the material a client already owns. The shortest path from "here is our textbook" to an accessible audio course. |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | **MIT** (file, 1,085 B, "Vineet Suryan, **Collabora Ltd.**") | 4,339 | **EMEA** | ✅ permissive | Near-real-time Whisper: live transcription and captioning of lectures, with TensorRT and OpenVINO backends. **Region placed from the licence file's own copyright line** — Collabora Ltd. is a UK company. Live captioning is an accessibility obligation in most EMEA higher-education estates. |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | **MIT** (file, 1,071 B) | 4,637 | Global | ✅ permissive | *"The python library for real-time communication."* The plumbing a **spoken** tutor needs — WebRTC audio in and out with STT/TTS hooks — rather than another model. The missing piece between a text tutor and a conversational one. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (file, 1,079 B) | 4,119 | Global | ✅ permissive | The **Free Spaced Repetition Scheduler** — a modern, ML-fitted replacement for SM-2, used as Anki's scheduler. **The retention layer's algorithm, permissively licensed**, where `anki-mcp-server` on the agent shelf only gives an agent control of the Anki *application*. 165 forks, 8 open issues. Build FSRS in; do not invent a review schedule. |

## Assessment and item-bank layer (new in the sixth pass)

The layer that decides whether a generated question may be put in front of a
student. **Five passes looked for an item *generator* and recorded a gap; the
sixth found the *gate* instead**, which is the artefact an exam board actually
buys and the one the EU AI Act's Annex III evaluation category needs evidence of.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 onionviolet") | 3 | Global | ✅ permissive | **The pick of this layer, and it would have been discarded by a star gate: 3★ against 1,175 commits on `main`.** "Author, validate and render exam-style question banks in markdown. A machine-checkable contract for LLM-authored questions." Local-first — nothing leaves the machine but an optional update check. `itembank lint` **blocks on error** per item number (each distractor must explain when it *would* be correct; answer-position skew; select-count against keyed-count; duplicate stems) and `itembank guard` **fails CI** if real banks are committed. **Scoring is deterministic with no model in the path**: short-answer items are *never* auto-graded and stay pending for rubric marking, `fill` is all-or-nothing, `check` runs learner code against hidden cases, and the README states model output is never accepted as a score. Retention is **FSRS** — the same scheduler as `fsrs4anki` below. Exports **Anki TSV, GIFT, answer-key TSV**; key-free JSON session protocol (`start`/`next`/`submit`/`report`/`teach`) built for agents. ⚠️ **Read the limits:** QTI/CASE/SCORM interchange is explicitly backburner — the README says it *"waits for a named consumer"* — the MCP surface is labelled "Phase 999.3" and unshipped, and the wider "course workspace" is not yet runnable. Python-dominant with a Rust `src-tauri/` shell. Holder is a handle; recorded Global. |
| [sudazc/open-question-bank](https://github.com/sudazc/open-question-bank) | ⚠️ **split: code + docs MIT, bank content NOT granted** (1,063 B, "Copyright (c) 2026 sudazc") | 0 | Global | ⚠️ conditional | Schema, validation and rule-based test assembly (`组卷`), TypeScript, 108 commits. **Shelved for its licence shape rather than its traction**, which is near zero. The README is explicit that MIT covers **the framework code and its documentation only**: permission to use, modify or redistribute **a bank's content** is set by that bank's own `bank.yaml` and source-licence fields, and the framework grant conveys none of it. ⚠️ **The default licence for a new bank is a placeholder reading `"TBD - not for publication"`** — so a bank authored with this tool is unpublishable until someone sets it. README states online practice and learning records are not yet implemented. Chinese-language; the grant names a handle, so **not placed** — this page does not place an artefact on its language. |
| [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** (11,346 B) | 203 | APAC | ✅ permissive | Model zoo of **cognitive diagnosis** models — IRT, MIRT, DINA, NCDM and others — from a named university group (USTC). **Be precise about what it does and does not do:** cognitive diagnosis infers *what a learner knows* from responses; it does **not calibrate items**. It is the live, permissive, education-specific half of the psychometrics layer, and the calibration half is the gap (see below). Last pushed 2024-10-25. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (1,079 B) | 4,119 | Global | ✅ permissive | **FSRS** as an algorithm rather than an application — the modern spaced-repetition scheduler. Carried forward from the fifth pass's capability sweep and repeated here because it is the retention component both `itembank` and `braiinz-education` independently chose. |

⚠️ **The honest statement of what is still missing, so nobody reads this layer as
complete.** There is **no permissive, live, education-specific item *calibration*
asset.** The two libraries that could calibrate an item bank —
[`eribean/girth`](https://github.com/eribean/girth) (127★, MIT, last pushed
**2022-09-09**) and [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy)
(242★, MIT, last pushed **2018-11-16**) — are both permissive, both capable and
**both stale by years**. The most capable pure-psychometrics library on the axis,
[`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) (114★, Java,
classical test theory + IRT), carries **no licence file at any of five filenames
across three branches**. The R options are copyleft (`lavaan` GPL-2+, `blavaan`
GPL-3). **So: author and gate items permissively today; calibrating them means
adopting a stale dependency, taking the Java library's licence risk, or building
it.** Say that to a client rather than implying the layer is solved.

## Lecture-video layer (new in the sixth pass — the fifth pass's `topic:video` ask)

**The sweep ran and the result is thin, which is itself the finding:** there is no
open-source lecture-video product to adopt, and there *is* a well-understood
four-stage pipeline to assemble — slides → page images → narration script → TTS
and mux. Every stage has a permissive component already on this page.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [galaxyproject/video-lectures](https://github.com/galaxyproject/video-lectures) | **MIT** (`master/LICENSE`, 1,071 B, "Copyright (c) 2024 Galaxy Project") | 2 | Global | ✅ permissive | **The reference pipeline and the only institutionally held row on this axis.** Pandoc turns `src/*.md` into HTML slides plus a hands-on document; `wkhtmltoimage` extracts one image per slide; `extract-script-from-html.js` pulls the narration text; `ari` muxes images and script into a narrated video; Yarn/Jake orchestrates. 67 commits on `master`, forked from `jxtx/covid-lessons`. ⚠️ **It terminates in Amazon Polly and the Jakefile needs AWS credentials** — swap the TTS stage before quoting it to any data-residency-constrained client. |
| [jhudsl/ari](https://github.com/jhudsl/ari) | **MIT** — declared in `DESCRIPTION` (`License: MIT + file LICENSE`); the `LICENSE` file is a **40 B stub** | — | North America | ✅ permissive | The narration-and-assembly **engine** under the row above, an R package from the **Johns Hopkins Data Science Lab** — a named institution, which is what places it. ⚠️ Its grant is **not readable from `LICENSE`**: the CRAN idiom this page already records puts the licence in `DESCRIPTION` and leaves `LICENSE` holding only a year and a holder. |
| [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) | **MIT** (1,070 B, "Copyright (c) 2024 Yongheng Chen") | — | Global | ✅ permissive | PDF deck plus a plain-text script, slides split on a `NEWSLIDE` marker, out to a narrated video. **The one row on this axis that can run with no cloud TTS at all** — it supports optional local voice cloning, which makes it the default pick for an offline or sovereignty-constrained engagement. |
| [htlin222/slides-to-video](https://github.com/htlin222/slides-to-video) | **MIT** (1,065 B, "Copyright (c) 2026 htlin222") | — | Global | ✅ permissive | ImageMagick page images → **model-generated speaker notes** → TTS → `ffmpeg`. The only row that *drafts* the narration rather than requiring a finished script, which is the stage a content team actually wants automated. |

🟢 **The substitution that makes this layer deliverable.** Three of the four rows
end in a proprietary cloud TTS. The permissive replacements are already shelved in
the narration layer below: [`denizsafak/abogen`](https://github.com/denizsafak/abogen)
(**MIT**, and it emits **synchronised captions** — an accessibility deliverable,
and the European Accessibility Act is a procurement gate across EMEA public
education), [`Blaizzy/mlx-audio`](https://github.com/Blaizzy/mlx-audio) (**MIT**,
Apple Silicon), and [`supertone-oss-archive/supertonic`](https://github.com/supertone-oss-archive/supertonic)
(**MIT**, on-device, ⚠️ **archived** — the grant is perpetual, the patches are not).

⛔ **Explicitly not shelved:** `harry0703/MoneyPrinterTurbo` (MIT, 136,744★) stays
rejected on the fourth pass's reasoning — it is short-form social video, not
lecture content, and its star count makes it the most likely thing on this axis to
be mis-offered as courseware tooling.

## Deck and document generation — extending the fourth pass's layer

The fourth pass found `ppt-master` (MIT, 71,498★) through a listicle. The
capability sweep confirms it sits in a **cohort**, which matters because
single-repo dependencies on a 71k★ project with unverifiable provenance are a
risk a client will ask about.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | **Apache-2.0** (file, 11,375 B) | 32,854 | Global | ✅ permissive | *"The first and best Office suite purpose-built for AI agents to read, edit and automate"* — DOCX, XLSX, PPTX from a CLI. The **agent-facing** alternative to `ppt-master`'s generate-from-scratch model: it edits the client's existing documents in place, which is what "update our 400 lesson plans" actually requires. C#, single binary, no Office install needed; 2,234 forks, created 2026-03-15. |
| [dream-num/univer](https://github.com/dream-num/univer) | **Apache-2.0** (file `dev/LICENSE`, 10,173 B) | 22,832 | Global | ✅ permissive | *"The Office Harness for AI Agents"* — embeddable spreadsheets, docs, slides and canvas as an SDK. Branch **`dev`**. Use when the deliverable is an **in-product editing surface** (a worksheet the student fills in) rather than a file. |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | **Apache-2.0** (file, 11,345 B) | 11,418 | Global | ✅ permissive | *"Free, open-source AI Office suite"* — Docs, Sheets, Slides, PDF, Markdown and HTML editors, **local-first**, LibreOffice-backed. Pairs with `PAIDEIA` for a fully offline authoring stack. |
| [tw93/Kami](https://github.com/tw93/Kami) | **MIT** (file, 1,061 B) | 12,173 | Global | ✅ permissive | *"Layout rules and templates that let AI agents export PDF, PPTX…"* — **typesetting quality**, which is the usual reason generated courseware looks unusable to a teacher. The cheapest fix for the "it works but it looks wrong" objection. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** (file, 1,070 B) | **75,894** | Global | ✅ permissive | Not a tool — **courseware**. A full AI-engineering curriculum, 13,381 forks, #1 on GitHub Trending 2026-05-24. **MIT means a client's internal academy can fork, rebrand and extend it**, which is the single fastest route to a credible AI-upskilling programme and is worth more to a corporate-L&D buyer than any generator on this page. Rejected from the agent shelf (see [`../agents/top.md`](../agents/top.md)) because it has no learner model. |

**How this layer changes the economics.** The content-production layer generates;
this layer **ingests what the client already owns**. That ordering is the
commercial point: an engagement that starts by generating new material competes
with the client's own faculty, while one that starts by ingesting the existing
textbook, past papers and lecture notes is **migration work**, which is easier to
scope, easier to value and impossible for the client to do with a chatbot
subscription. Pattern **P-570-A** wires the two together.

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
- ~~**Horizontal tooling is systematically under-covered.**~~ **Swept and closed
  on the fifth pass — and the prediction was an understatement.** The fourth pass
  guessed the blind spot hid "document parsers, TTS pipelines, assessment-item
  generators and video tooling". The capability sweep returned **sixteen
  permissively licensed repositories, five of them above 30,000★ and three above
  69,000★** — `PaddleOCR` (92,024), `MinerU` (82,860), `tesseract` (77,267),
  `ai-engineering-from-scratch` (75,894), `docling` (69,909), `OfficeCLI`
  (32,854), `opendataloader-pdf` (30,129). **The horizontal layer is larger than
  the entire education-specific supply in this KB combined**, and it had been
  invisible for four passes to a filter nobody questioned. Two sub-gaps remain
  open: **assessment-item generators** returned nothing permissive and
  education-specific, and **video tooling** was not swept (`MoneyPrinterTurbo`,
  MIT, 136,744★, surfaced incidentally and is short-form social video, not
  lecture content — it is not shelved and should not be treated as courseware).
- **The generalisable lesson, since it will recur in every other industry KB:**
  a sweep filtered on an industry topic measures *how a repository markets
  itself*, not what it does. The tools an industry runs on are usually tagged by
  **capability**, because their authors are selling to everyone. Sweep both axes
  or report an undercount.
- **`ulearn`'s maturity is unassessed beyond its stack.** 701★ MIT is the largest
  permissive LMS found and Laravel 5.8 is five major versions behind. Nobody
  should be told it is a starting point without an upgrade estimate attached.
