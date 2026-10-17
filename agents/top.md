---
industry: education
region: Global
updated: 2026-10-17
---

# Top AI agents — Education

> Education-specific open source agents Globant AI Studios can compose or customize.
> Every licence in the tables below was read **first-hand** this pass from the repository's
> own `LICENSE` payload (`raw.githubusercontent.com`), not from a secondary source.
> Star counts are as served by the repository page or the GitHub topic listing on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv),
> extended by [`verified-repos.2026-10-17-p266.tsv`](../evidence/verified-repos.2026-10-17-p266.tsv)
> (pass 266: the Artemis/Iris/Pyris rows and the first payload-verified Portuguese-language agent).

## Build-on-this tier — permissive licences (MIT / Apache-2.0 / BSD)

These are the rows a studio engagement can start from without copyleft or
non-commercial friction.

| Agent | Repo | Licence | Stars | What it does |
|-------|------|---------|-------|--------------|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 41.5k | Lifelong personalized tutoring: a persistent student model that survives between sessions, multi-agent orchestration, citation-grounded feedback. Release v1.6.14 dated 2026.10.8. The single most adopted education agent on GitHub. |
| Artemis | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | Platform for interactive learning with individual feedback, from the Applied Education Technologies group at **TU Munich**; 12,437 commits, self-hosted by universities in several countries. Ships three config-gated AI subsystems: **Iris** (LLM tutor), **Athena** (feedback suggestion for text/modelling/programming) and **Hyperion** (AI exercise authoring on Spring AI). Programming submissions are built, tested and analysed automatically. The answer to "where is the open grading agent" — it is inside a platform. |
| Iris | [ls1intum/Iris](https://github.com/ls1intum/Iris) | MIT | — | Artemis's virtual AI tutor: hints and leading questions rather than answers. Deployable with Artemis, and the cleanest MIT reference for a tutor that is pedagogically constrained by design. |
| Pyris | [ls1intum/Pyris](https://github.com/ls1intum/Pyris) | MIT | 12 | The LLM microservice behind Iris: a REST API fronting swappable LLM pipelines, with exercise feedback, RAG over instructor-supplied course material, and automated competency generation. The reusable piece — it will serve a stack that is not Artemis. |
| Instructional Agents | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | MIT | 488 | EACL'26 Main paper. Multi-agent ADDIE pipeline: syllabus → LaTeX slides → assessments, with Teaching Faculty / Instructional Designer / TA / Coordinator roles. Also ships as a Claude Code Skills release (2026.4.15). |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1.0k | AI study partner that plans learning paths, explains concepts and guides projects end to end. |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 516 | MCP server exposing the Anki flashcard app to any MCP client. The cleanest way to put spaced repetition behind an agent. |
| lineage-skill | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | Apache-2.0 | 458 | Turns videos, PDFs, transcripts and notes into teacher-style agent skills that stay tied to their sources — provenance is a first-class output, not an afterthought. |
| universal-examprep-skill | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 308 | Exam-prep coach that teaches from the institution's own slides, with page-level citations and generated quizzes. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 288 | Private AI tutor that adapts lessons to the learner. Ships both as an agent skill and as a web app. |
| universal-diagnostic-tutor-skill | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | MIT | 246 | Diagnosis-first tutor for STEM and CS: establishes the misconception before it teaches. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 267 | Intelligent tutoring system with Bayesian Knowledge Tracing, ReactJS + Firebase. UC Berkeley CAHL lab, 1,045 commits. The reference open ITS for maths/STEM. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 142 | Local, block-based adaptive workspace that generates notes, quizzes and flashcards. Runs without a cloud dependency. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT | 114 | Collection of education-focused agent skills for teaching and tutoring workflows. |
| Claw-ED | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | MIT | 62 | Local-first assistant that drafts editable lessons, student materials and slides from a curriculum. Teacher-reviewed beta — human-in-the-loop by design. |
| AI_Tutor_Release (EduAgent) | [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release) | MIT | 65 | RAG tutor targeted at grades 1–9. |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 49 | MCP server that turns any LLM into an intelligent tutoring system. Small, readable, and the right shape for embedding in a client's existing assistant. |

**17 permissive rows, all licence-verified from payload.** (14 from passes 264-265, plus
Artemis, Iris and Pyris verified in pass 266.)

## Verified but licence-restricted — read before you build

Real projects, real code, but the licence changes the engagement. None of these is a
"no"; each is a "price".

| Agent | Repo | Licence | Stars | The constraint |
|-------|------|---------|-------|----------------|
| gen-mentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | 135 | Official code for an LLM multi-agent goal-oriented tutoring framework. CC0 is a public-domain dedication — permissive in effect, but it is a *content* instrument, so warranty/patent language a client's legal team expects is simply absent. |
| education-agent-skills | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | CC-BY-SA-4.0 | 873 | 165 evidence-grounded skills for teachers and school leaders. **ShareAlike**: derivatives of the skill content must carry the same licence. Excellent reference, awkward to embed in a proprietary deliverable. |
| human-skill-tree | [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | AGPL-3.0 | 571 | AI skill tree for lifelong learning, 30+ skills. AGPL reaches through network use — a hosted deployment triggers source obligations. |
| freelingo | [artcc/freelingo](https://github.com/artcc/freelingo) | AGPL-3.0 | 179 | Self-hosted language learning with AI tutor and spaced repetition. Same AGPL network clause. |
| lumen | [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | GPL-3.0 | 89 | Builds private courses and tutors learners with course-scoped RAG. GPL-3.0 copyleft on distribution. |
| ai_tutor_forge | [guedesindev/ai_tutor_forge](https://github.com/guedesindev/ai_tutor_forge) | GPL-3.0 | 18 | Python 3 CLI that forges a personalized tutor over a user-chosen LLM. Notable as the **first Portuguese-language education agent this KB has payload-verified** — see the provenance caveat in the gaps below. GPL-3.0 copyleft on distribution, and at 21 commits it is a personal project, not a dependency. |

## Verified but licence-UNVERIFIED — do not assume the parent's licence

| Repo | Status | Why it is not shelved |
|------|--------|----------------------|
| [ls1intum/Athena](https://github.com/ls1intum/Athena) | LIVE, **no licence payload** | Artemis's feedback-suggestion engine. No licence file served on `develop`, `main` or `master` across `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`. Artemis itself is MIT; **that does not license Athena.** Treat as all-rights-reserved until a payload says otherwise. If Athena matters to an engagement, ask TUM for the licence in writing. |
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | LIVE, **no licence payload** | Parent `kolibri` is MIT (pass 265). The design-system repo serves no licence of its own. |
| [autograder-org/autoGrader-frontend](https://github.com/autograder-org/autoGrader-frontend) | LIVE, **no licence payload** | README claims LLM-based assignment grading; 22 commits. Early-stage and unlicensed. |

## Licence corrections this pass

Three cells this base previously published are wrong, and one repository it listed is gone.
Correcting them is the point of the pass.

| Row | Published | Read from payload 2026-10-17 |
|-----|-----------|------------------------------|
| `DaRL-GenAI/instructional_agents` | Apache-2.0 | **MIT** |
| `pykt-team/pykt-toolkit` stars | 1.2k | **450** (topic listing, descending-stars sort) |
| `HKUDS/DeepTutor` stars | 22k+ | **41.5k** — the project nearly doubled, the old cell understated it |
| `CaviraOSS/PageLM` | MIT, per this base's own `evidence/verified-repos.2026-10-15-p213.tsv` | **PageLM Community License** — non-commercial, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"*. **Not usable in a client deliverable.** See the trends file. |
| `OpenEduCat-Inc/OpenEduCat` | live vertical platform | **404.** Canonical repo is [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0). |
| `GeminiLight/awesome-ai-llm4education` | MIT | **No LICENSE file served** on `main`/`master`/`develop`. The MIT claim is not substantiated; treat the repo as all-rights-reserved until a payload says otherwise. |
| `Open-TutorAi/open-tutor-ai-CE` | BSD-3-Clause | **BSD-3-Clause — confirmed.** The payload opens *"All rights reserved"*, which is part of the standard BSD form, not a reservation on top of it. Flagging it would have been a false positive. |

## Agents by function

### Personalized tutoring
**DeepTutor** (Apache-2.0, 41.5k) is the default starting point — persistent student model,
multi-agent, actively released. **OATutor** (MIT) when the client wants Bayesian Knowledge
Tracing they can audit rather than an LLM they must trust. **Bloom** and
**universal-diagnostic-tutor-skill** when the deliverable is a skill inside an assistant the
client already runs.

### Teacher workload / instructional design
**Instructional Agents** (MIT, EACL'26) is the only peer-reviewed option here and it is
permissively licensed — syllabus through assessments. **Claw-ED** for local-first lesson
drafting where student data cannot leave the building. **lineage-skill** when provenance of
generated material is a procurement requirement (it is, increasingly, in EMEA).

### Agents over existing study tooling
**anki-mcp-server** and **tutor-mcp** are the two MCP servers worth knowing: they let an
agent drive spaced repetition and tutoring loops without rebuilding either.

### Assessment, grading and feedback
**Artemis** (MIT, TU Munich) is the starting point when assessment is the deliverable: automated
build-test-analyse on programming submissions, **Athena** for text/modelling feedback, and
human-in-the-loop by construction. **Numbas** (Apache-2.0, Newcastle) when assessment must run
**entirely in the browser** — no student submission leaves the device, which answers a data-residency
objection before it is raised. **nbgrader** (BSD-3-Clause) for notebook-based courses. Note Athena's
unverified licence above.

### Knowledge tracing / learner modelling
Not agents but the models underneath them — see [`repos/foundations.md`](../repos/foundations.md):
`pykt-toolkit`, `pyedmine`, `EduStudio`, `EduData`.

## Provenance correction — the top row on this shelf is APAC-origin

This file previously declared that **no APAC-origin education agent had surfaced**. That claim
was false against this file's own first row.

`HKUDS/DeepTutor`'s README states the project is *"led by Bingxi Zhao within the **HKUDS
Group**"* and thanks the *"director of the **Data Intelligence Lab @ HKU**"*. HKUDS is the
Data Intelligence Lab at the **University of Hong Kong**. The single most-adopted education
agent in open source — **41.5k stars, Apache-2.0** — is APAC-origin, and so is much of the
learner-modelling layer beneath it: `bigdata-ustc/EduData` (University of Science and
Technology of China) and `HFUT-LEC/EduStudio` (Hefei University of Technology), both named in
their own GitHub org handles.

**Evidence grades, stated honestly:** DeepTutor's affiliation is **payload-quoted** from the
repository README. EduData's and EduStudio's are **org-handle** evidence — the institution is
named in the handle, not in a payload. For `pykt-team/pykt-toolkit` and `ZhijieXiong/pyedmine`
no affiliation statement was located this pass, so no provenance is claimed for them.

**Why this matters commercially:** "APAC is supply-poor in education AI" would have been
briefed into APAC engagements as a reason to import a stack. The opposite is closer to true —
APAC is where the research supply lives. What APAC has not produced is a **platform** (see
[`verticals/solutions.md`](../verticals/solutions.md)), which is a far narrower gap and points
at integration work rather than wholesale import.

## Declared gaps

- **RETRACTED in pass 266 — "no LATAM-origin education agent" is no longer the claim.**
  [`guedesindev/ai_tutor_forge`](https://github.com/guedesindev/ai_tutor_forge) (GPL-3.0,
  payload-verified, 18★) is a Portuguese-language education agent, now on the restricted
  shelf above. **But state the evidence at its real grade:** the README, file descriptions
  and interface are in Portuguese, and the repository page does **not** state the author's
  country — this is *language* evidence, weaker than the org-handle evidence used for EduData
  and far weaker than DeepTutor's payload-quoted affiliation. So "LATAM-origin" is not
  asserted; "Portuguese-language" is. **The defensible gap is now: no Spanish- or
  Portuguese-language education agent with adoption.** LATAM's real open-source education
  supply remains the platform layer — `portabilis/i-educar` and `i-diario`, actively
  maintained Brazilian systems, both committed to in October 2026.
- **Star-sorted search cannot see publicly-funded code — the instrument, not the world.**
  Pass 265 concluded that fourteen permissive rows "is the size of this category today". Pass
  266 added three MIT rows (Artemis, Iris, Pyris) and an MIT national platform
  (`Sunbird-Ed/SunbirdEd-portal`, **41★ against 38,046 commits**) without a single new search
  term — by probing named projects directly. Every agent and repo leg this KB runs sorts
  GitHub topics **by stars**, and a ministry-funded project accrues commits, forks and
  deployments but almost no stars. **Rank the platform layer by commits and forks; probe
  national-programme names by hand.** See [`repos/trending.md`](../repos/trending.md).
- **REVISED in pass 266 — the grading gap was a question about the wrong shape of thing.**
  There is still no standalone education grading *agent repo* with adoption (`MUJINN/question-marking`
  and `MUJINN/intelligent-correction` remain single-digit-star). But the *function* is served,
  permissively and at university scale, by a platform **this base already had on its own
  foundations shelf**: **[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) is MIT**,
  819★, 12,437 commits — `repos/foundations.md` has carried it as "the strongest MIT-licensed
  teaching platform" while *this* file called the category empty. New in pass 266 is what it
  ships: **Athena** (automated feedback for text, modelling and programming), **Iris** (LLM
  tutor) and **Hyperion** (AI exercise authoring on Spring AI). Beside
  it: `jupyter/nbgrader` (BSD-3-Clause, 1.4k), `autolab/Autolab` (Apache-2.0, 808, CMU-origin)
  and `numbas/Numbas` (Apache-2.0, 215, Newcastle, browser-only execution). **Caveat that
  changes procurement:** Athena's own repo serves **no licence payload** — the MIT grant covers
  Artemis, not necessarily Athena. Get it in writing before it ships in a deliverable.
- **`mcp-server-education` as a GitHub topic is empty** — "hasn't been used on any public
  repositories, yet" — while two real education MCP servers exist. The category is real and
  unlabelled; that is a naming gap, and a small opening for whoever labels it first.
