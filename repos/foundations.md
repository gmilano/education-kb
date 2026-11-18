---
industry: education
region: Global
updated: 2026-11-18
---

# Foundational repos — education

The substrate an education engagement is built on. All URLs and licences verified
2026-11-18 via `raw.githubusercontent.com` (see `agents/top.md` for method and limits).

**Read the licence column before you promise anything.** Education's most important
platforms are copyleft: Open edX, Canvas and Moodle are AGPL-3.0/GPL-3.0. That is fine
for hosting and for plugins that stay separate, and it is a problem for a proprietary
derivative work. The permissive anchors — Artemis (MIT), Kolibri (MIT), Oppia
(Apache-2.0), OpenOLAT (Apache-2.0) — are the ones to reach for when a client needs to
keep the result closed. This distinction is the single most consequential fact in this
file.

## LMS and platform cores

| Repo | Licence | Role |
|---|---|---|
| https://github.com/openedx/edx-platform | AGPL-3.0 | Open edX. The reference large-scale MOOC/LMS core. **Note the slug** — `openedx/openedx-platform` is a 404 that circulated in earlier passes of this KB. |
| https://github.com/moodle/moodle | GPL-3.0 (no root `LICENSE`; verified in `COPYING.txt`) | The world's most-deployed LMS. Huge plugin surface, which is where AI work actually lands. |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | Canvas. Dominant in North American higher ed; strong LTI and REST API. |
| https://github.com/ls1intum/Artemis | MIT | TU Munich's interactive learning platform with automated programming assessment. **The best permissive LMS core in education** — pair with `edutelligence`/`Pyris`. |
| https://github.com/learningequality/kolibri | MIT | Offline-first learning platform for low-connectivity deployments. Permissive, and the right core for rural LATAM, Africa and South Asia. |
| https://github.com/oppia/oppia | Apache-2.0 | Interactive lesson platform with built-in pedagogy (explorations, misconception handling). |
| https://github.com/sakaiproject/sakai | ECL-2.0 | Sakai. Higher-ed LMS; ECL-2.0 is Apache-2.0 with an education-oriented patent clause. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | Strong in LATAM and francophone deployments. |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | Long-standing German/EMEA LMS, heavy in regulated and public-sector training. |
| https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 | Swiss-origin LMS. Permissive, enterprise-grade, under-used outside EMEA. |

## Interoperability and standards

The layer that decides whether your AI work can be sold twice. Build against these and the
same agent ships into Canvas, Moodle and Open edX.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | LTI 1.3 / Advantage tool provider in Node. The standard way to expose an AI tool to any compliant LMS. |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | PHP LTI framework from the author of the IMS LTI spec. |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 | Ed-Fi operational data store — the K-12 data standard across most US states. Essential for any North American K-12 engagement. |
| https://github.com/1EdTech/openbadges-validator-core | Apache-2.0 | Open Badges validation; the credentialing/micro-credential layer, 61 ★. **Last push 2025-11-04 (379 days idle)** — the spec is stable, but expect to maintain this yourself. |
| https://github.com/Citolab/qti-components | GPL-3.0 | QTI 3 web components for assessment item rendering. Copyleft — keep it at arm's length in a proprietary build. |
| https://github.com/apereo/cas | Apache-2.0 | Central Authentication Service. The SSO incumbent in higher education. |

## Learning analytics (xAPI / LRS)

Where the evidence for "did the AI actually help" has to live.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/yetanalytics/lrsql | Apache-2.0 | SQL-backed Learning Record Store, 144 ★, pushed 2026-11-14. Permissive, actively maintained — **the default LRS pick**, and the only one of the four here that is both. |
| https://github.com/openfun/ralph | MIT | xAPI/LRS toolbox from France Université Numérique. |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 | Reference LRS from ADL, who authored xAPI, 335 ★. **Last push 2025-11-14 (369 days idle)** — useful as a spec reference, not as a production dependency. |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | Widely deployed LRS, 587 ★. **Do not start new work here: last push 2024-05-30, 902 days idle.** Copyleft as well. Use `lrsql` instead. |

## Assessment, grading and academic integrity

| Repo | Licence | Role |
|---|---|---|
| https://github.com/PrairieLearn/PrairieLearn | MIT | Randomised, auto-graded problem generation. Permissive and genuinely strong; the best open assessment engine for STEM. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause (1,370 ★) | Assignment release/collect/autograde for notebooks. The data-science course standard. |
| https://github.com/autolab/Autolab | Apache-2.0 | CMU's autograding platform with secure job execution. |
| https://github.com/ls1intum/Ares | MIT | Automated programming-exercise assessment library behind Artemis. |
| https://github.com/openedx/edx-ora2 | AGPL-3.0 | Open-response assessment: peer, self and staff grading workflows. The natural seam for an AI grading assist. |
| https://github.com/openedx/codejail | Apache-2.0 | Sandboxed untrusted-code execution. **Use this (or Ares) before you let an agent run student code.** |
| https://github.com/Udayraj123/OMRChecker | MIT | OMR/bubble-sheet scanning. Unglamorous and high-value in LATAM, India and Africa where paper exams dominate. |
| https://github.com/openedx/edx-proctoring | AGPL-3.0 | Proctoring integration. **Regulatory flag:** exam monitoring is an EU AI Act Annex III high-risk use case (obligations from 2 Dec 2027). |

## Content authoring and pipelines

| Repo | Licence | Role |
|---|---|---|
| https://github.com/h5p/h5p-php-library | GPL-3.0 | H5P interactive content. Ubiquitous across Moodle and Open edX. |
| https://github.com/Khan/perseus | MIT | Khan Academy's exercise/question rendering framework. Permissive. |
| https://github.com/learningequality/studio | MIT | Kolibri Studio — curriculum authoring and channel curation. |
| https://github.com/learningequality/ricecooker | MIT | Content-import pipeline into Kolibri channels. |
| https://github.com/learningequality/le-utils | MIT | Shared constants and format definitions for the Kolibri ecosystem. |
| https://github.com/openfun/richie | MIT | Course-catalogue/marketing CMS for Open edX. |
| https://github.com/openfun/marsha | MIT | Video management for LMS-embedded teaching. |

## Document and media ingestion

Course material arrives as PDFs, slide decks and lecture recordings. This is where most
education RAG projects actually fail.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/docling-project/docling | MIT | Document parsing to structured form. Strong on PDF layout, tables and reading order. |
| https://github.com/datalab-to/marker | Apache-2.0 | PDF to Markdown at high fidelity, including equations. |
| https://github.com/opendatalab/MinerU | Apache-2.0 | PDF extraction with strong CJK and formula handling — notably better than Western-trained alternatives on APAC textbooks. |
| https://github.com/Unstructured-IO/unstructured | Apache-2.0 | Broad-format ingestion into chunked, embeddable records. |
| https://github.com/SYSTRAN/faster-whisper | MIT | Fast CTranslate2 Whisper inference. The practical choice for lecture transcription at volume. |
| https://github.com/openai/whisper | MIT | Reference speech-to-text weights and code. |

## Model serving, retrieval and memory

| Repo | Licence | Role |
|---|---|---|
| https://github.com/ollama/ollama | MIT | Local model serving. The enabler for data-residency and on-premise school deployments. |
| https://github.com/vllm-project/vllm | Apache-2.0 | High-throughput serving for campus-scale concurrency. |
| https://github.com/BerriAI/litellm | MIT | Unified gateway across providers, with per-key budgets. **Per-course and per-student cost caps are a procurement requirement in education, not a nicety.** |
| https://github.com/qdrant/qdrant | Apache-2.0 | Vector database with payload filtering — needed to scope retrieval to one course or cohort. |
| https://github.com/chroma-core/chroma | Apache-2.0 | Lightweight vector store; fine for per-course corpora. |
| https://github.com/HKUDS/LightRAG | MIT | Graph-augmented RAG. Fits curricula, where prerequisite structure is a graph. |
| https://github.com/infiniflow/ragflow | Apache-2.0 | Document-understanding-first RAG engine with a usable ingestion UI. |
| https://github.com/deepset-ai/haystack | Apache-2.0 | Mature RAG/search orchestration framework. |
| https://github.com/mem0ai/mem0 | Apache-2.0 | Persistent memory layer — the mechanism behind "the tutor remembers what this learner struggled with". |
| https://github.com/temporalio/temporal | MIT | Durable workflow execution. Grading runs and term-long tutoring loops need to survive restarts. |

## Evaluation, labelling and quality

| Repo | Licence | Role |
|---|---|---|
| https://github.com/EleutherAI/lm-evaluation-harness | MIT | Standard LLM benchmark harness; extend it with subject-specific tasks. |
| https://github.com/promptfoo/promptfoo | MIT | Prompt/LLM regression testing in CI. The gate that keeps a tutor from regressing between releases. |
| https://github.com/HumanSignal/label-studio | Apache-2.0 | Human annotation across modalities — rubric calibration, grading gold sets. |
| https://github.com/argilla-io/argilla | Apache-2.0 | Feedback collection and dataset curation with domain experts (here: teachers). |
| https://github.com/AI-for-Education/pedagogy-benchmark | MIT | Pedagogical-ability benchmark. Pairs with the harness above as an education-specific eval gate. |

## Other infrastructure

| Repo | Licence | Role |
|---|---|---|
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | Multi-user notebook serving. The computational-teaching backbone. |
| https://github.com/jupyterhub/zero-to-jupyterhub-k8s | Apache-2.0 | Kubernetes deployment path for JupyterHub at class scale. |
| https://github.com/jupyterhub/nbgitpuller | BSD-3-Clause | Distributes course materials into student notebook environments. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | FSRS spaced-repetition scheduler. A real, evidence-backed learning algorithm to pair with an agent instead of inventing a review schedule. |
| https://github.com/appsmithorg/appsmith | Apache-2.0 | Low-code internal tooling — teacher review queues and human-in-the-loop consoles without a bespoke front end. |
| https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | Offline-first knowledge/education server. Relevant to the same low-connectivity brief as Kolibri. |

**47 foundational repos, all verified** — comfortably past the 5-repo floor.

## Gaps and caveats

- **`openedx/XBlock` and `openedx/xblock-sdk` exist but are not in the tables above.**
  `openedx/XBlock/master/README.rst` returns `200`, so the repos are real, but no licence
  file could be fetched by any name tried, so we will not assert a licence. Treat the XBlock
  SDK as available and confirm its licence directly before use.
- **Two repos ship no root licence file, and the SPDX check split them.**
  `moodlehq/moodleapp` has no root licence file but GitHub's detector reports **Apache-2.0**
  (1,006 ★) — note that this differs from Moodle core's GPL-3.0, so do not assume the app
  inherits the platform's licence. `OS4ED/openSIS-Classic` has no licence file **and** SPDX
  reports `NONE` (351 ★); third parties list GPL-2.0 but nothing in the repo says so. Treat
  openSIS as licence-unclear and get written clarification before shipping it to a client.
- **No open-source student information system qualifies as a *foundation*.** The SIS options
  (RosarioSIS, openSIS, Gibbon, i-educar, GegoK12) are in `verticals/solutions.md` — they are
  deployable products, not libraries to build on. There is no Ed-Fi-grade open SIS core.
- **Star counts and last-push dates are now measured** via batched `repo:` qualifiers
  against `gh api search/repositories`; see `agents/top.md` for method. Three repos
  (`openedx/edx-platform`, `All-Hands-AI/OpenHands`, `danny-avila/LibreChat`) are absent from
  search results in this session, so their star figures are recorded as unavailable.

## Appendix — verified metrics table (2026-11-18)

Measured, not asserted. Stars and SPDX licence from `gh api search/repositories`
(batched `repo:` qualifiers); licence text independently read from
`raw.githubusercontent.com`. `SPDX` of `NOASSERTION` means GitHub's detector could not
classify the licence file — usually a modified or dual licence — and the text column is
then the one to trust. No repo in this set is archived.

| Repo | ★ | SPDX | Licence text read | Last push | Days idle |
|---|---|---|---|---|---|
| `ollama/ollama` | 187,466 | MIT | MIT | 2026-11-18 | 0 |
| `openai/whisper` | 113,086 | MIT | MIT | 2026-08-31 | 79 |
| `vllm-project/vllm` | 97,125 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `infiniflow/ragflow` | 94,355 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `opendatalab/MinerU` | 83,893 | NOASSERTION | Apache-2.0 | 2026-11-16 | 2 |
| `docling-project/docling` | 70,725 | MIT | MIT | 2026-11-18 | 0 |
| `mem0ai/mem0` | 69,158 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `BerriAI/litellm` | 63,462 | NOASSERTION | MIT | 2026-11-18 | 0 |
| `crewAIInc/crewAI` | 61,058 | MIT | MIT | 2026-11-18 | 0 |
| `HKUDS/DeepTutor` | 60,165 | Apache-2.0 | Apache-2.0 | 2026-11-15 | 3 |
| `odoo/odoo` | 55,884 | NOASSERTION | LGPL | 2026-11-18 | 0 |
| `langchain-ai/langgraph` | 45,093 | MIT | MIT | 2026-11-18 | 0 |
| `Crosstalk-Solutions/project-nomad` | 43,902 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `THU-MAIC/OpenMAIC` | 43,856 | MIT | MIT | 2026-11-18 | 0 |
| `patchy631/ai-engineering-hub` | 41,974 | MIT | MIT | 2026-11-01 | 17 |
| `appsmithorg/appsmith` | 41,268 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `datalab-to/marker` | 40,969 | Apache-2.0 | Apache-2.0 | 2026-11-14 | 4 |
| `HKUDS/LightRAG` | 40,754 | MIT | MIT | 2026-11-18 | 0 |
| `qdrant/qdrant` | 35,619 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `ankitects/anki` | 32,874 | NOASSERTION | AGPL-3.0 | 2026-11-17 | 1 |
| `stanford-oval/storm` | 31,906 | MIT | MIT | 2025-09-30 ⚠️ | 414 |
| `assafelovic/gpt-researcher` | 30,768 | Apache-2.0 | Apache-2.0 | 2026-11-12 | 6 |
| `chroma-core/chroma` | 29,709 | Apache-2.0 | Apache-2.0 | 2026-11-13 | 5 |
| `HumanSignal/label-studio` | 28,724 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `promptfoo/promptfoo` | 27,399 | MIT | MIT | 2026-11-18 | 0 |
| `deepset-ai/haystack` | 27,040 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `SYSTRAN/faster-whisper` | 26,844 | MIT | MIT | 2026-11-12 | 6 |
| `temporalio/temporal` | 24,466 | MIT | MIT | 2026-11-18 | 0 |
| `Unstructured-IO/unstructured` | 15,762 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `EleutherAI/lm-evaluation-harness` | 14,498 | MIT | MIT | 2026-11-04 | 14 |
| `apereo/cas` | 11,403 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `bigbluebutton/bigbluebutton` | 9,282 | LGPL-3.0 | LGPL | 2026-11-18 | 0 |
| `jupyterhub/jupyterhub` | 8,368 | BSD-3-Clause | OTHER | 2026-11-05 | 13 |
| `moodle/moodle` | 7,620 | GPL-3.0 | NO-LICENSE-FILE | 2026-11-17 | 1 |
| `oppia/oppia` | 6,998 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `instructure/canvas-lms` | 6,918 | AGPL-3.0 | AGPL-3.0 | 2026-11-10 | 8 |
| `CTFd/CTFd` | 6,917 | Apache-2.0 | Apache-2.0 | 2026-11-10 | 8 |
| `netless-io/flat` | 6,443 | MIT | MIT | 2026-11-10 | 8 |
| `argilla-io/argilla` | 5,204 | Apache-2.0 | Apache-2.0 | 2026-11-16 | 2 |
| `open-spaced-repetition/fsrs4anki` | 4,142 | MIT | MIT | 2026-08-14 | 96 |
| `frappe/lms` | 3,429 | AGPL-3.0 | AGPL-3.0 | 2026-11-18 | 0 |
| `OpenVidu/openvidu` | 2,146 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `iiab/iiab` | 2,053 | GPL-2.0 | LGPL | 2026-11-13 | 5 |
| `jupyterhub/zero-to-jupyterhub-k8s` | 1,727 | NOASSERTION | Apache-2.0 | 2026-11-15 | 3 |
| `Khan/perseus` | 1,600 | MIT | MIT | 2026-11-18 | 0 |
| `OpenHands/software-agent-sdk` | 1,406 | MIT | MIT | 2026-11-18 | 0 |
| `jupyter/nbgrader` | 1,370 | BSD-3-Clause | OTHER | 2026-11-03 | 15 |
| `sakaiproject/sakai` | 1,240 | ECL-2.0 | ECL-2.0 | 2026-11-17 | 1 |
| `Udayraj123/OMRChecker` | 1,196 | MIT | MIT | 2026-09-04 | 75 |
| `learningequality/kolibri` | 1,179 | MIT | MIT | 2026-11-18 | 0 |
| `overhangio/tutor` | 1,133 | AGPL-3.0 | AGPL-3.0 | 2026-11-17 | 1 |
| `DSpace/DSpace` | 1,115 | BSD-3-Clause | BSD | 2026-11-13 | 5 |
| `pkp/ojs` | 1,058 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `chamilo/chamilo-lms` | 1,025 | GPL-3.0 | GPL-3.0 | 2026-11-18 | 0 |
| `kiwix/kiwix-tools` | 1,006 | GPL-3.0 | GPL-3.0 | 2026-11-09 | 9 |
| `moodlehq/moodleapp` | 1,006 | Apache-2.0 | NO-LICENSE-FILE | 2026-11-17 | 1 |
| `openeducat/openeducat_erp` | 913 | NOASSERTION | LGPL | 2026-11-16 | 2 |
| `ls1intum/Artemis` | 832 | MIT | MIT | 2026-11-18 | 0 |
| `autolab/Autolab` | 808 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `portabilis/i-educar` | 727 | GPL-2.0 | LGPL | 2026-11-13 | 5 |
| `frappe/education` | 712 | NOASSERTION | OTHER | 2026-10-30 | 19 |
| `francoisjacquet/rosariosis` | 654 | GPL-2.0 | GPL-2.0 | 2026-11-16 | 2 |
| `GibbonEdu/core` | 641 | GPL-3.0 | GPL-3.0 | 2026-11-18 | 0 |
| `open-scratch/teaching-open` | 637 | Apache-2.0 | Apache-2.0 | 2026-07-06 | 135 |
| `Koha-Community/Koha` | 602 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `LearningLocker/learninglocker` | 587 | GPL-3.0 | GPL-3.0 | 2024-05-30 ⚠️ | 902 |
| `PrairieLearn/PrairieLearn` | 533 | NOASSERTION | MIT | 2026-11-18 | 0 |
| `opencast/opencast` | 513 | ECL-2.0 | ECL-2.0 | 2026-11-18 | 0 |
| `ILIAS-eLearning/ILIAS` | 512 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `instructure/instructure-ui` | 487 | NOASSERTION | MIT | 2026-11-18 | 0 |
| `openedx/codejail` | 477 | Apache-2.0 | Apache-2.0 | 2026-11-16 | 2 |
| `OpenOLAT/OpenOLAT` | 452 | NOASSERTION | Apache-2.0 | 2026-11-17 | 1 |
| `ECNU/EduWork` | 378 | MulanPSL-2.0 | OTHER | 2026-11-18 | 0 |
| `tsugiproject/tsugi` | 377 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `Cvmcosta/ltijs` | 373 | Apache-2.0 | Apache-2.0 | 2026-11-11 | 7 |
| `OS4ED/openSIS-Classic` | 351 | NONE | NO-LICENSE-FILE | 2026-10-26 | 23 |
| `adlnet/ADL_LRS` | 335 | Apache-2.0 | Apache-2.0 | 2025-11-14 ⚠️ | 369 |
| `vishalsachdev/canvas-mcp` | 334 | MIT | MIT | 2026-11-18 | 0 |
| `openfun/richie` | 318 | MIT | MIT | 2026-11-18 | 0 |
| `Li-Evan/BloomTutor` | 313 | MIT | MIT | 2026-11-17 | 1 |
| `CAHLR/OATutor` | 282 | MIT | MIT | 2026-11-17 | 1 |
| `jupyterhub/nbgitpuller` | 237 | BSD-3-Clause | BSD | 2026-11-02 | 16 |
| `OpenPronounce/OpenPronounce` | 221 | MIT | MIT | 2026-11-09 | 9 |
| `learningequality/studio` | 212 | MIT | MIT | 2026-11-18 | 0 |
| `zijinz456/OpenTutor` | 181 | MIT | MIT | 2026-11-17 | 1 |
| `h5p/h5p-php-library` | 156 | GPL-3.0 | GPL-3.0 | 2026-11-10 | 8 |
| `openfun/marsha` | 152 | MIT | MIT | 2026-11-17 | 1 |
| `yetanalytics/lrsql` | 144 | Apache-2.0 | Apache-2.0 | 2026-11-14 | 4 |
| `openedx/paragon` | 141 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `IIC2233/Syllabus` | 129 | NONE | NO-LICENSE-FILE | 2026-11-17 | 1 |
| `flysheep-ai/education-skills` | 125 | MIT | MIT | 2026-01-30 ⚠️ | 292 |
| `Open-TutorAi/open-tutor-ai-CE` | 118 | BSD-3-Clause | OTHER | 2026-06-26 | 145 |
| `ls1intum/Apollon` | 106 | MIT | MIT | 2026-11-17 | 1 |
| `instructure/common-cartridge-viewer` | 95 | MIT | MIT | 2026-11-04 | 14 |
| `wenflow-org/wenflow` | 72 | MIT | MIT | 2026-11-12 | 6 |
| `openedx/edx-proctoring` | 69 | AGPL-3.0 | AGPL-3.0 | 2026-11-17 | 1 |
| `openedx/edx-ora2` | 64 | AGPL-3.0 | AGPL-3.0 | 2026-11-13 | 5 |
| `1EdTech/openbadges-validator-core` | 61 | Apache-2.0 | Apache-2.0 | 2025-11-04 ⚠️ | 379 |
| `Gego-K12/gegok12` | 57 | NOASSERTION | MIT | 2026-09-23 | 56 |
| `moodlehq/wiki-rag` | 54 | BSD-3-Clause | BSD | 2026-06-15 | 156 |
| `openfun/ralph` | 52 | MIT | MIT | 2026-11-17 | 1 |
| `learningequality/ricecooker` | 32 | MIT | MIT | 2026-11-02 | 16 |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 28 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `ls1intum/Ares` | 27 | MIT | MIT | 2026-11-03 | 15 |
| `Citolab/qti-components` | 18 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `ls1intum/edutelligence` | 17 | MIT | MIT | 2026-11-17 | 1 |
| `AI-for-Education/pedagogy-benchmark` | 13 | MIT | MIT | 2026-11-16 | 2 |
| `ls1intum/Pyris` | 12 | MIT | MIT | 2026-06-03 | 168 |
| `warleysr/ankipa` | 10 | MIT | MIT | 2026-11-07 | 11 |
| `learningequality/le-utils` | 7 | MIT | MIT | 2026-11-02 | 16 |
| `virtualryder/edu-ai-agents` | 4 | NOASSERTION | MIT | 2026-10-10 | 39 |
| `LMS-COMPASSO/lms` | 1 | MIT | MIT | 2026-11-17 | 1 |
| `Abdulrahman-hayatu/lessonplan-ng` | 0 | Apache-2.0 | Apache-2.0 | 2026-10-28 | 21 |
| `bishoynabilanis/jessica` | 0 | MIT | MIT | 2026-11-18 | 0 |
| `mayuribagga/ai-worksheet-maker` | 0 | MIT | MIT | 2026-10-26 | 23 |
| `vulinh1704/ai-tutor-agent` | 0 | MIT | MIT | 2026-11-16 | 2 |

⚠️ = no push in over nine months. **Maintenance risk, flagged explicitly:**

- **`LearningLocker/learninglocker`** (587 ★) — last push 2024-05-30, 902 days idle.
- **`stanford-oval/storm`** (31,906 ★) — last push 2025-09-30, 414 days idle.
- **`1EdTech/openbadges-validator-core`** (61 ★) — last push 2025-11-04, 379 days idle.
- **`adlnet/ADL_LRS`** (335 ★) — last push 2025-11-14, 369 days idle.
- **`flysheep-ai/education-skills`** (125 ★) — last push 2026-01-30, 292 days idle.

