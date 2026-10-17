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
> (pass 266: the Artemis/Iris/Pyris rows and the first payload-verified Portuguese-language agent),
> extended again by [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv)
> (pass 267: the LMS-side MCP servers, and a re-probe of every "no licence payload" row against a
> 19-path x 4-ref set that includes the **British spelling `LICENCE`**),
> and extended again by [`verified-repos.2026-10-17-p268.tsv`](../evidence/verified-repos.2026-10-17-p268.tsv)
> (pass 268: the **third** MCP-addressable LMS — Google Classroom / Workspace for Education — eight
> servers probed, seven permissive and **one a custom all-rights-reserved licence wearing the same
> description**),
> and extended again by [`verified-repos.2026-10-17-p269.tsv`](../evidence/verified-repos.2026-10-17-p269.tsv)
> (pass 269: the first two **African-context** education agents this base has located — both of
> which serve **no grant at all** — plus a blind re-measure of three carried APAC rows that
> **reproduced every published figure**, and the search-leg ledger
> [`p269-websearch.2026-10-17-p269.tsv`](../evidence/p269-websearch.2026-10-17-p269.tsv)).

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
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 295 | **Canvas LMS MCP server — the agent row with the shortest path to a live client system.** 102–126 tools plus 8 agent skills over the Canvas API, works with Claude, Cursor, Codex and other MCP clients. v1.14.0 released October 2026, 1,026 commits, University of Illinois Urbana-Champaign named in the README. It makes the LMS a client **already runs** addressable by an agent **without forking the LMS** — see the tool-count caveat below. |
| google-classroom-mcp | [adriasantacreu/google-classroom-mcp](https://github.com/adriasantacreu/google-classroom-mcp) | MIT *(metadata — see grade note)* | 2 | **Google Classroom MCP server, and the most capable of its family: "46 fully implemented tools"** over courses, assignments, grading, rosters and Drive file management. 11 commits. ⚠️ Licence is **metadata grade** (`package.json` plus a README statement); the sidebar shows no licence and no payload is served. Build on it only with that written down. |
| edu-workspace-mcp | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | MIT | 1 | **Google *Workspace for Education* MCP server** — Docs, Sheets, Slides, Forms, Drive **and** Classroom, 29 tools in the README table. 42 commits. **The first Korean-language education agent this KB has payload-verified** (README in Korean, references Korean curriculum standards, and ships `docs_import_hwp` / `docs_export_hwpx` for Korea's national document formats). Widest reach in this family — and therefore the widest blast radius: see the scope warning below. |
| classroom-mcp | [OmarNiazi/classroom-mcp](https://github.com/OmarNiazi/classroom-mcp) | MIT | 0 | Google Classroom for **students**, *"read-only: it can't submit work, post, or change anything."* 7 commits. Read-only by construction is the right shape for a student-side pilot and the wrong shape for an institutional deliverable. |
| moodle-mcp *(teacher side, **write**)* | [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | MIT | 1 | **The permissive Moodle doorway this shelf implied did not exist.** stdio MCP server exposing **40 high-level facades plus a `ws_raw` escape hatch** over Moodle Web Services: courses, sections, content, quizzes (GIFT import), enrolment CSV, groups, roles, gradebook, messaging, calendar, badges. Every write is **upsert-by-`idnumber`**, so republishing never duplicates. Works against **any Moodle 4.x/5.x** with Web Services on. ⚠️ **Three prices, all recorded below:** the write half needs a companion Moodle `local_` plugin (→ the deployed combination is GPL-3.0, see pass 273 note); this base's own `T4` finding is that its writes are **ungated**; and at 1★/59 commits it is a **reference implementation, not a dependency**. Tool surface is in **Spanish**. |
| moodle-mcp-server *(student side, read + submit)* | [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | MIT | 0 | MCP server **and REST API** in **Go** connecting any model to any Moodle instance: courses, contents, grades, assignments, deadlines, calendar, notifications — **13–14 tools**, student-facing. The only Go implementation this base has located. ⚠️ `submit_assignment` means it is **not read-only**, which its own framing underplays. ⚠️ Its documented install is `irm …/install.ps1 \| iex` / `curl …/install.sh \| bash` — **pipe-to-shell from a 0★ repo is not an institutional install path**; build from source. Unproven, but clean at payload. |
| Athena | [ls1intum/Athena](https://github.com/ls1intum/Athena) | MIT *(metadata — 12 of 14 manifests; see grade note)* | 6 | **Artemis's feedback-suggestion engine — the open grading agent, and new to this tier in pass 275 after three passes shelved as all-rights-reserved.** Generates feedback suggestions for text, modelling and programming exercises; each module (`module_text_llm`, `module_programming_llm`, `module_modeling_llm`) is an independently installable Poetry package, which is the reusable unit. ⚠️ Licence is **metadata grade and serves no licence FILE** — the tree was *enumerated* (691 files, zero licence-like paths), but **12 of its 14 manifests declare `license = "MIT"`**, unanimous, none declaring anything else. That is TUM's own written declaration, repeated twelve times, and it retracts this base's *"treat as all-rights-reserved, ask TUM in writing"*. Build on it with the grade written down; a payload is still worth requesting. |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | MIT *(manifest + registry — see grade note)* | 103 | **Canvas LMS MCP server, 54 tools, `v2.3.1`** — full student functionality plus account management, vitest suite, 19 releases on npm as `canvas-mcp-server`. 🔴 **`p276` withdrew this shelf's own *"Do not use. No licence = all rights reserved"*:** `package.json` l.66 declares `"license": "MIT"` and npm ships it MIT across **19** versions. ⚠️ **Grade note:** manifest + registry, **no payload in the tree** (36 paths enumerated; the `files` array names a `LICENSE` the repo does not contain). Same grade this shelf already gives `adriasantacreu/google-classroom-mcp`. [evidence](../evidence/manifest-channel.2026-10-17-p276.tsv) |
| fsrs4anki-helper | [open-spaced-repetition/fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper) | MIT | 325 | **FSRS spaced-repetition scheduling** — the retention-optimising scheduler a tutoring agent can call instead of inventing review intervals: reschedule, postpone, advance, load-balance. 🔴 **`p276` refuted *"NO GRANT in 6 filenames"*:** the grant is at **`License`** — mixed case, **no extension** — `1 079` B, read at payload. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| EduChat *(code tier only)* | [ECNU-ICALK/EduChat](https://github.com/ECNU-ICALK/EduChat) | Apache-2.0 **for the code** · 🔴 `AGPL-3.0` model · 🔴 `CC-BY-NC-4.0` data | 973 | **Educational LLM from ECNU** (retrieval-augmented tutoring, emotional support, essay assessment). 🔴 **`p276` withdrew *"cannot be used"*:** at the same ref `fa30b6d5632c` the tree serves `LICENSE/LICENSE.txt` — **Apache-2.0, `11 357` B**, the pristine length. 🔵 **Six path probes and GitHub's API both missed it because `LICENSE` is a DIRECTORY**, so each probe hit a tree, not a blob. ⚠️ **Build on the CODE only:** shipping the weights pulls in `AGPL-3.0`, and the data is non-commercial. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |

**24 permissive rows.** (14 from passes 264-265, plus Artemis, Iris and Pyris in pass 266, plus
`canvas-mcp` in pass 267, plus three Google Classroom servers in pass 268, plus **two MIT Moodle
servers in pass 273**, plus **`ls1intum/Athena` in pass 275** — moved here from the licence-UNVERIFIED
table below, not newly discovered.) **22 are payload-verified; `adriasantacreu/google-classroom-mcp`
and `ls1intum/Athena` are metadata grade and are marked as such in their own cells** — the count is
not allowed to launder the weaker rows.

⚠️ **Cite `canvas-mcp`'s tool count as a range, not a number.** Its About blurb says *"up to 102
tools"*; its README body says *"up to 126"*, and adds that the default profile registers fewer than
either. Two numbers on one page is not a finding to resolve by picking one — quote the range and
count the tools you actually enable.

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
| moodle-mcp-server | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 | 1 | The Moodle-side counterpart to `canvas-mcp`: an MCP server over Moodle Web Services, 10 tools in the README table, 57 commits. **Two separate prices, not one.** AGPL-3.0's network clause reaches a hosted deployment, *and* the project is **open-core — the README sells premium plugin tools separately**. Scope any estimate to the free tool set, and note that the Moodle side of this category is roughly 1,000x less adopted than the Canvas side. 🟢 **Pass 273: this is no longer the only Moodle door.** Two **MIT** Moodle servers are now on the permissive shelf above — [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) (teacher side, 40 tools) and [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (student side). **Neither is more adopted than this row; both are more permissive.** Choose on the licence and the tool surface, not on the star count — none of the three has one. |
| canvas-mcp (minimal) | [admin978/canvas-mcp](https://github.com/admin978/canvas-mcp) | MIT | 4 | *"Local-first Canvas LMS MCP server. Stdio transport, ~125 lines of Python."* Permissive and worth **reading** — it is the smallest complete example of the pattern — but at 33 commits it is a reference, not a dependency. Listed here rather than on the build-on-this shelf for that reason, not for its licence. |
| mewcp-google-classroom | [AStheTECH/mewcp-google-classroom](https://github.com/AStheTECH/mewcp-google-classroom) | **"AStheTECH Community License (ACL)" — proprietary** | — | ⚠️ **Not open source, and it arrived describing itself exactly like the seven MIT rows above.** Its payload sits at `LICENSE.md` and opens *"Copyright (c) 2026 AStheTech. **All rights reserved**"* with an acceptance-of-terms clause. **Second instance of the PageLM pattern** — a permissive-looking education repo whose grant is a bespoke licence. Not usable in a client deliverable. It is **not** a lure (it passes all three substantive predicates of the `p238` gate); it is simply **not permissive**, which is why the gate can never replace reading the grant. |

## Verified but licence-UNVERIFIED — do not assume the parent's licence

| Repo | Status | Why it is not shelved |
|------|--------|----------------------|
| [ls1intum/Athena](https://github.com/ls1intum/Athena) | 🔴 **RETRACTED in pass 275 — MIT at *metadata* grade. Now a row in the build-on tier above.** | **This base carried Athena as all-rights-reserved across three passes and 76 path/ref probes, and the verdict was false.** It is true that no licence FILE exists — pass 275 settled that by *enumerating* the tree rather than guessing at it (`git ls-tree -r`: **691 files, zero licence-like paths**, so the absence is now definitive rather than probabilistic). But **12 of Athena's 14 manifests declare `license = "MIT"`** — `athena/`, `llm_core/`, `assessment_module_manager/`, `log_viewer/` and all eight `modules/*/` packages — unanimous, with none declaring anything else. 🔴 **Why 76 probes missed it:** pass 267's list (quoted in this file until this pass) probed *"the package metadata (`package.json`, `pyproject.toml`, …)"* — **at the ROOT**. Athena's root `pyproject.toml` is a 632-byte Poetry *workspace stub* containing **zero occurrences of the string `license`**; it is the one manifest in the repository that is silent. The ladder probed precisely it, four times over, and the miss was structurally guaranteed. **A monorepo declares its grant per package.** *"Ask TUM for the licence in writing"* is withdrawn: TUM has written it down, twelve times, in the repository. Evidence: [`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv). |
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | **RESOLVED in pass 267 — MIT at *metadata* grade** | This base carried the row as "no payload, parent `kolibri` is MIT" — which is an **inference from the parent**, the weakest grade there is. The repo's `main/package.json` declares `"license": "MIT"`. That is the **project's own declaration**, so publish it as **MIT (metadata)**: stronger than an inference, weaker than a payload, and enough to build on while a payload is requested. It still serves no licence *file*. |
| [autograder-org/autoGrader-frontend](https://github.com/autograder-org/autoGrader-frontend) | LIVE, **no licence payload — upheld against the 19-path x 4-ref probe** | README claims LLM-based assignment grading; 22 commits. Early-stage and unlicensed. Pass 267 confirms it is not a detection artefact. |
| [OpenEMIS/OpenEMIS-Core](https://github.com/OpenEMIS/OpenEMIS-Core) | LIVE, **no licence payload**, none in the page sidebar | *"Manage students and staff information at school, district, and national level."* OpenEMIS is the education-management system most associated with **ministry-level** deployment, which is why pass 267 probed it by hand. What this KB can actually reach is a **32-commit Docker packaging repo (7★) with no licence and no ministry or country named in it.** The application source was not located this pass. **Ministry provenance is not established — do not brief it as a public-sector reference.** |
| [muskvdc/EduTwin-Africa](https://github.com/muskvdc/EduTwin-Africa) | LIVE, **PRE-LICENCE — the placeholder is still in the README** *(new in pass 269)* | Curriculum-aware tutor over **South African** curriculum knowledge, **Grades 8–12**: RAG, adaptive learning, bounded multi-agent collaboration, ReAct tools, guardrails. 0★ / 0 forks / 7 commits, default ref `main`. **No payload on 19 of 19 paths, no `license` field in `pyproject.toml`**, and the README says, in the author's own words: *"Add the project's chosen license here before publishing if a specific open-source license is required."* 🔵 **This is a state this shelf has not carried before.** `Athena` and `autoGrader-frontend` are *silent*; this one is **explicitly not yet licensed**. The practical difference is that it is the one row here where asking costs nothing and might work — the author has written down that they know it is missing. Until then: all rights reserved. |
| [Valexxy/edunaija-os](https://github.com/Valexxy/edunaija-os) | LIVE, **no grant on any channel** *(new in pass 269)* | *"A security-conscious starter codebase for a Nigerian-first learning platform"*; `package.json` name is `nigeria-learning-platform`. 0★ / 0 forks / 6 commits. No payload on 19 of 19 paths and **no `license` field in `package.json`** — the two channels that could have carried a grant both empty. Names **no exam board and no institution**. 🔴 **Cite it carefully: it is NOT the EduNaija AI Tutor of the AfricaNLP 2026 paper** (that system is a five-agent LangChain + FAISS RAG tutor with English/Yoruba/Hausa/Igbo support; this is a starter codebase with a similar name). **Two different artefacts, one name** — see the trends file. |

## Pass 276 — the queue was worked, and this shelf gains three rows: two from a channel the gate does not read, one from a path no ladder spells

**30 of `p275`'s 124 queued negative verdicts enumerated** in two channels — tree *and* manifest.
30/30 slugs resolve. **9 verdicts refuted, 7 positive controls passed, 18 absences now sayable in both
channels.** Evidence: [`tree-enumeration`](../evidence/tree-enumeration.2026-10-17-p276.tsv) ·
[`manifest-channel`](../evidence/manifest-channel.2026-10-17-p276.tsv).

🔴 **The grade this shelf already owned, and withheld from one row.** `adriasantacreu/google-classroom-mcp`
is tabled above as **MIT *(metadata)*** — no licence file, `"license": "MIT"` in `package.json`.
`DMontgomery40/mcp-canvas-lms` has **the same evidence plus 19 MIT releases on npm**, and this shelf
published *"NONE … Do not use."* **Two rows, one evidence shape, opposite verdicts.** `p274`'s sentence —
*"a correction applied to one instance is not a correction to the class"* — now has its eighth
consecutive instance, and this time the class was a grade this base had already defined.

🔵 **Taken with `p275`'s 2-of-13, the measured error rate of a ladder-shaped negative verdict is 11 of
43.** Roughly one in four. `QUEUE-UNENUMERATED` falls **124 → 70**; `VERIFIED-ABSENT` rises **28 → 48**.

⚠️ **One row on this shelf cannot hold its own licence.** `ECNU-ICALK/EduChat` carries **three** grants —
Apache-2.0 code, `AGPL-3.0` weights, `CC-BY-NC-4.0` data. A single Licence column is the wrong shape for
it, and the row says so rather than picking the flattering value.

🔴 **A refuted absence is not a permission (`P-N1`).** `dssg/student-early-warning` was carried as
`RESERVED`/`CONDITIONAL-GRANT` — and that was **right**: the grant exists (`2 069` B, read this pass) and
it permits only *"academic research or other not-for-profit scholarly purposes"*, expressly excluding
*"any service or part of selling a service."* **Enumeration can refute an absence without clearing a row
for use**, and the grade must come from the payload's terms, not from the existence of a file.


## Pass 275 — the row this shelf told studios not to use has declared MIT twelve times, and the refusal came from probing one 632-byte file

⏱️ **Twenty-first pass of `2026-10-17`.** Evidence:
[`tree-enumeration.2026-10-17-p275.tsv`](../evidence/tree-enumeration.2026-10-17-p275.tsv) *(13 slugs: `ls-remote` positive control + full tree enumeration, zero searches)* ·
[`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv) *(14 manifests, every one read at payload)* ·
[`verified-repos.2026-10-17-p275.tsv`](../evidence/verified-repos.2026-10-17-p275.tsv) ·
[`p275-websearch.2026-10-17-p275.tsv`](../evidence/p275-websearch.2026-10-17-p275.tsv) *(8 legs)*.

### 🟢 `p274`'s top-ranked item was run, and it returned a real negative — then the thing it was testing turned out not to be the problem

`p274` ranked, at zero searches: *"re-probe every negative licence verdict with `ls-remote` as a
positive control first — because the mechanism that produced the `gegok12` false negative is not
specific to that row."*

🟢 **Run over 13 slugs. The mechanism is NOT endemic:** `gegok12/gegok12` fails `ls-remote` with
`rc=128` exactly as a nonexistent repository does, and **all twelve other negative-verdict slugs
resolve**. The backlog item is **discharged with a measured answer**, not deferred.

🔴 **And then the same sweep refuted two of this base's own published verdicts** — not because a slug
was wrong, but because **a path ladder cannot prove absence** (`T46`):

| row | this shelf published | enumeration found |
|---|---|---|
| **`ls1intum/Athena`** | *"no grant across 76 path/ref probes over three passes; treat as all-rights-reserved; ask TUM for the licence in writing"* | 🔴 **12 of 14 manifests declare `license = "MIT"`.** Now the **24th permissive row** |
| **`os4ed/openSIS-Classic`** *(`verticals/`)* | *"no licence payload served on any path tried"* | 🔴 **`docs/License.txt` — verbatim GPL-2.0, 200, 17 286 B** |

### 🔴 The box this pass earned

| the finding | how it surfaced | why it had not been found |
|---|---|---|
| 🔴 **A 76-PROBE REFUSAL WAS AIMED AT THE ONE MANIFEST IN THE REPOSITORY THAT IS SILENT** | 🟢 By **enumerating** the tree (`git ls-tree -r` over a blobless clone) instead of extending the ladder a fifth time | 🔴 `p267`'s list is sound *as written* — `pyproject.toml` is on it. It is aimed at the **root**, and Athena's root `pyproject.toml` is a **632 B Poetry workspace stub with zero occurrences of `license`**. **A monorepo declares its grant per package** (`T47`). Every added path made the refusal feel better-evidenced while leaving the unexamined space the same size |
| 🔴 **THIS BASE HELD THE PRINCIPLE *AND* THE CODE FOR ~180 PASSES AND NEVER APPLIED EITHER TO LICENCES** | 🟢 By finding [`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/) — **pase 93, `2026-10-04`** — which states **`P275`** (*to sustain an absence in a tree you must ENUMERATE it*) and **`P278`** (*a ZERO over a path that does not exist in that ref measures the PATH, not the content*) and ships a working blobless-clone enumerator | 🔴 **`P278` describes both of this pass's false negatives exactly.** The principle was applied to **directory** trees (ILIAS, `frappe`, `openeducat`) and **never to licence paths**, where `p267` built a `19 × 4` ladder instead. 🔵 **`p274` wrote the diagnosis — *"a correction applied to one instance is not a correction to the class"* — and this is that sentence about `p274` itself.** Sixth consecutive pass whose defect species was invisible to the prior check, **and the first where the lesson existed in general form, in code** |
| 🔴 **A CHANNEL PROBED AT ONE PATH NEARLY PUBLISHED A FALSE CHANNEL STATE** | 🟢 By probing the path to be **used** rather than a cheaper neighbour | 🔴 `api.github.com/rate_limit` → **200** with a plausible body; `api.github.com/repos/<slug>` → **403** *(session-scope message, not a rate limit)*. Reading the 200 as access would have invited the next pass to refresh **star counts** from an API this session does not have (`T48`) |

### 🔵 Registered, not claimed

- 🟢 **The instrument is BUILT, not described** — `make gate-enumeration` is in `make hooks`, with **30
  controls** (`compose/code/pass275-grant-enumeration/`). `p274`'s own lesson was that *"an amendment that is
  not built gets violated by the next pass"*; this pass did not repeat it.
- 🔴 **Running the gate on the live shelves corrected the gate three times**, each for the same reason —
  **one line can carry two subjects**. It first reported `ls1intum/Artemis`, an MIT row with a root
  `LICENSE`, as **refuting itself** (the phrase on that line is about Athena, four slugs later); then
  missed a subject named in bold **prose** rather than as a link; then flagged **this pass's own new
  Athena row**, because that row opens *"**Artemis's** feedback-suggestion engine"* — **a possessive is a
  modifier, not a subject.** Teaching it prose names found **2 further live occurrences** of the openSIS
  claim the slug-only rule had missed.
- 🔵 **`QUEUE-UNENUMERATED=124`.** 124 negative licence verdicts on these shelves still rest on a path
  ladder. **That is not a failure signal — it is the first honest measurement of the exposure**, and it
  prints on every `make hooks` run.
- ⚠️ **No star count in this pass was read from GitHub.** `api.github.com` 403 on `/repos` and `/search`,
  `github.com` HTML 403. Athena's `6★` and every other figure on this shelf is **carried** and marked so.
- 🟢 **The permissive count moved 23 → 24 and `make recount` was updated with it**, so `T37` still
  re-derives it from the rows: `STALE=0 of 4`.

## Pass 274 — the gap this file declared was contradicted by a row in this file, and the MCP count was two platforms short of its own evidence

⏱️ **Twentieth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p274.tsv`](../evidence/verified-repos.2026-10-17-p274.tsv) *(12 probes, every
grant read at payload, channel re-tested not inherited)* ·
[`quantity-recount.2026-10-17-p274.tsv`](../evidence/quantity-recount.2026-10-17-p274.tsv) *(5 registered
quantities, zero searches)* ·
[`p274-websearch.2026-10-17-p274.tsv`](../evidence/p274-websearch.2026-10-17-p274.tsv) *(10 legs)*.

### 🟢 The eight-pass nil on agent supply ENDS — and not through the supply channel

| what | result |
|---|---|
| 🟢 **Six rows added to the MCP table** | `bruchris/canvas-lms-mcp` (MIT, FERPA pseudonymisation), `RohanMuppa/brightspace-mcp-server` (MIT), `felipedias-ie/blackboard-mcp` (MIT), `NiccoloSalvini/mcp-blackboard-ucsc` (MIT), `blend-ed/tutor-contrib-openedxmcp` (AGPL-3.0) — **and every one was already on [`trending.md`](trending.md) with a payload-read grant.** Nothing was discovered; something was **shelved** |
| 🔴 **The `Bloom`/`Lumen` gap was FALSE** | `Li-Evan/Bloom` is a row in this file's own build-on tier. `ahmedEid1/Lumen` was in this base's `p195` census. **Two passes called them unresolvable and a third ranked searching again** |
| 🔴 **A twice-carried licence REFUTATION is itself refuted** | `Gego-K12/gegok12` serves **MIT**, `1 150` B, diffed and byte-accounted. See `T44` and [`verticals/solutions.md`](../verticals/solutions.md) |
| 🔴 **The count was wrong on both shelves** | **15** slugs tabled here (prose said 13; `T21` said 12) and **6** platforms reachable (both shelves said 3) |

### 🔴 The box this pass earned

| the finding | how it surfaced | why it had not been found |
|---|---|---|
| 🔴 **A FILE CAN DECLARE A GAP THAT ONE OF ITS OWN ROWS REFUTES, AND EVERY CROSS-SHELF CHECK ON THIS BASE PASSES IT** | 🟢 By doing what `p273` costed — **reading a shelf top to bottom as a reader** — rather than grepping between shelves | 🔴 `T29` greps the **destination** file; `T34` greps the **other** shelves; `T37` re-counts a **quantity**. **The Bloom contradiction is INTRA-FILE and QUALITATIVE**: a row at line `46` and a sentence at line `456` of the same file. 🔵 **Fifth consecutive pass whose defect species was invisible to the check written one pass before** — and this time the check that would have caught it (`T34`) existed and ran |
| 🔴 **AN AMENDMENT THAT IS NOT BUILT GETS VIOLATED BY THE NEXT PASS** | 🟢 By **building** `T37` instead of citing it (90 lines, no network) and running it | 🔴 `T37` was written in `p272` and ranked seventh by `p273`. In the two passes between the amendment and its implementation, **three more stale quantities were published.** 🟢 `make recount` now derives them. See `T43` |
| 🔴 **THIS SHELF HELD AN MIT DOORWAY INTO AN INCUMBENT THE STRATEGY SHELF SAYS TO REPLACE** | 🟢 By grouping the MCP rows **by platform** instead of counting them | 🔴 `p267` found this exact shape for Canvas (*"the opening is the opposite of migration"*) and the correction **never generalised**. Blackboard carries **two MIT servers** on `trending.md` while `market.md` sells a replacement engagement against it. **A correction applied to one instance is not a correction to the class** |

### 🔵 Registered, not claimed

- 🟢 **Every grant in this pass's ledger reproduces its carried byte count exactly** where one existed
  (`RohanMuppa` `1 068`, `blend-ed` `34 524`, `Bloom` `1 069`, `Lumen` `35 149`). Per `T39` that proves
  **stability, not correctness** — but it does confirm `P929`'s measurement method is being applied
  consistently across passes, which is the first thing that was ever in doubt.
- 🔴 **`DMontgomery40/mcp-canvas-lms` is NOT shelved as a row, and the reason belongs here:** it carries
  **its own security disclosure of a broken access control that exposed other students' personal
  information.** 🔵 Same category and same search-result description as the MIT rows above —
  the `PageLM` pattern in its **security** dimension rather than its licence one (`T45`).
- ⚠️ **No star count in this pass was read from GitHub.** `api.github.com` **403**, `github.com` HTML
  **403**, `codeload` **403**, `raw.githubusercontent.com` **200** — re-tested this pass, not inherited.
  Star figures in the new rows are **carried from `trending.md`** and marked `—` where none exists.
## Pass 273 — the Moodle door was permissive all along, and this base had measured it four times without shelving it

🔴 **Stated first, because it is a finding about this KB and not about the market.** Both MIT rows added
to the permissive table this pass —
[`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) and
[`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) — are **not new to
this base.** Its own instrumentation has graded `MarcosNahuel/moodle-mcp` **MIT at payload on at least
four separate occasions** (`p114` 2026-10-02, `p170` 2026-10-03, `p191` 2026-10-14, `p725` 2026-10-08),
measured its 40-tool surface, its auth posture and its release cadence — and **it has never appeared on a
single live shelf.** Before this pass, `agents/top.md`, `repos/foundations.md`,
`verticals/solutions.md`, `intel/market.md`, `intel/trends.md` and `compose/patterns.md` contained
**zero** occurrences of the string `MarcosNahuel`.

🔵 **This is the Koha species of defect, and it is now the second confirmed instance** — a row carried for
passes in the instrumentation and never promoted to the shelf a studio actually reads. The practical
consequence here was worse than with Koha, because the shelf did not merely omit the row: the only Moodle
cell it *did* carry, [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server),
is **AGPL-3.0 and open-core**, so a studio reading this file came away believing **the Moodle side of the
MCP category has a copyleft-plus-paywall price**. It does not. 🟢 **Both corrected cells now cross-reference
each other.**

🟡 **And the reasons the rows were *correctly* withheld as dependencies are preserved rather than
deleted**, because they are the honest half of the finding: `1★ / 1 fork / 59 commits`, a *burst-and-silence*
release pattern, and this base's own **`T4`** finding that the writes execute **with no confirmation and no
disclosure**. 🔵 **The fix is not to promote them to dependencies. It is to stop letting the shelf imply an
absence that the instrumentation had already refuted** — they belong on the shelf as the **permissive
reference implementations of the Moodle agent doorway**, with their prices in the cell. That is what they
now are.

### 🔴 The genuinely new finding: this repo contains a second artefact, under a second licence regime, and the base's grading model cannot see it

`MarcosNahuel/moodle-mcp` is graded `SOLE` / `OWN-GRANT-AT-ROOT` by this base's own
`p283`/`p257` instrumentation — one grant, at the root, covering the repository. **That grading is
correct about the file and wrong about the artefact.** The repository ships **two** deliverables:

| artefact | what it is | grant served |
|---|---|---|
| `@nahuelalbornoz/moodle-mcp` | the TypeScript MCP wrapper — the thing you run | **MIT**, `main/LICENSE`, **1,065 B**, read in full this pass, **byte-identical to stock MIT, zero rider keywords** |
| `local_italiciamcp` | a **Moodle `local_` PHP plugin** in `plugin-companion/` — the thing that performs **every write** | 🔴 **no grant of its own.** No `LICENSE` and no `README` in the plugin directory (both **404**); **zero GPL notices across the six plugin files that serve** |

🔵 **The detail that makes it a finding rather than a nit.** The plugin's `version.php` opens with
Moodle's own file header — `// This file is part of Moodle - http://moodle.org/` — and **the GPL
paragraph that follows that exact line in every Moodle core file has been replaced** by a description of
the project. The plugin declares `MOODLE_INTERNAL`, requires **Moodle 4.0+**, supports `[400, 501]`, and
its `classes/external/upsert_page.php` calls **`core_external\external_api`** — it links Moodle's
internal API by construction. Moodle's own documentation puts the platform at **GPLv3-or-later** and tells
new projects to use GPLv3+.

🟢 **This is NOT a "do not use" finding, and must not be briefed as one.** MIT is **GPL-compatible**, so
there is no conflict in the grant itself. The consequence is about the **combination**, and it is a
narrow, cheap one:

- **The wrapper stays MIT.** It talks to Moodle over REST Web Services and links nothing. Build on it freely.
- **The deployed combination — Moodle + the `local_` plugin — is a GPL-3.0 work.** If a client *distributes*
  that combination (a packaged distro, an appliance, an image handed to a third party), it goes out under
  **GPL-3.0**, not MIT.
- 🟢 **For a hosted deployment that is a non-event**, because GPL-3.0 — unlike the **AGPL-3.0** on
  `csmediapro/moodle-mcp-server` — **has no network clause.** So on the price that actually decides most
  education engagements, the MIT row is still strictly cheaper than the row this shelf used to carry alone.

⚠️ **One correction to this base's own record while we are here:** the dormancy note (*"8 releases in 4 days
and nothing in 5 months"*, pinned to npm `2026-04-23`) is **stale**. The repository's `CHANGELOG.md`
documents plugin `v0.5.0` dated **`2026-05-03`**, after that pin.

Evidence: [`verified-repos.2026-10-17-p273.tsv`](../evidence/verified-repos.2026-10-17-p273.tsv) ·
[`p273-moodle-plugin-governance.2026-10-17-p273.tsv`](../evidence/p273-moodle-plugin-governance.2026-10-17-p273.tsv).
Wiring recipe: **`P23`** in [`compose/patterns.md`](../compose/patterns.md). Trend: **`T41`**.

## Pass 272 — this file gains no rows for the seventh consecutive pass, and the count it publishes was wrong

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) ·
[`p272-websearch.2026-10-17-p272.tsv`](../evidence/p272-websearch.2026-10-17-p272.tsv).

🔵 **Seventh consecutive measured nil on education-specific agent supply.** The generic legs ran last, per
`p269`. Everything returned was already shelved (`HKUDS/DeepTutor`, whose **Apache-2.0** grant `p272`
re-read at payload: `main/LICENSE`, **11,408 B**) or unresolvable to a slug (`Bloom`, `Lumen` — named in a
topic listing with no owner, recorded as an informed gap on `repos/foundations.md`, **not** written in as
rows).
🔴 **RETRACTED IN PASS 274 — BOTH LIMBS, AND THE COUNTER-EVIDENCE FOR ONE OF THEM IS 410 LINES ABOVE
THIS SENTENCE.** `Bloom` is [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom), **MIT, `1 069` B**,
and it has been **a row in this file's own build-on tier** since `p264` — the sentence above declares
unresolvable a slug this file tables. `Lumen` is [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen),
resolved from this base's **own `p195` licence census** via
[`compose/code/p196-population-diff/`](../compose/code/p196-population-diff/), and it is **GPL-3.0 at
payload (`35 149` B) against an MIT badge in its own README** — see
[`repos/foundations.md`](../repos/foundations.md). 🔵 **Neither needed a search. `p272` spent a leg, and
`p273` ranked spending another, on two slugs this base already held** — `T25`'s finding (*"the most
productive research channel was this knowledge base"*) re-earned, and `T34`'s amendment (*grep the other
shelves before re-declaring an absence*) **failed on a gap whose counter-evidence was in the same
file.** 🟢 **Nothing was added to meet the brief's five-row minimum; this file holds 42 rows and clears it
many times over.**

🔴 **The defect this file earned: it was the better source and the other shelf never caught up.** This
file's MCP-server count said **eleven** in prose while **12 distinct slugs** are actually tabled, and
`intel/trends.md` said **five**. Passes 267 and 268 added servers and updated **one shelf**. Both numbers
are corrected and the generalisation is `T37`: **a quantity inside a gap statement is a carried datum —
re-count it from the rows, on every shelf that states it.**

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

### Agents over the systems the client already runs (MCP)
Pass 268 takes this from four servers to **eleven**, and from two LMSs to **three**. 🟢 **Pass 273 takes it to thirteen, and ends Moodle's status as the one LMS reachable only through copyleft.**
🔴 **PASS 274, by re-count rather than by search: this file tabled `15` MCP server slugs when the prose
said thirteen and `T21` said twelve — and with this pass's five additions it tables `20`. `SIX`
platforms are reachable, not three** — Canvas, Moodle, Google Classroom / Workspace,
**Brightspace / D2L**, **Blackboard Ultra** and **Open edX**. The last three were on
[`agents/trending.md`](trending.md) with payload-read grants and never reached this table. The number
is now **derived** by [`compose/code/p274-quantity-recount/recount.py`](../compose/code/p274-quantity-recount/recount.py)
rather than incremented by hand (`T43`); the three platform rows below were **payload-read first-hand in
`p274`** ([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)).

| Server | Licence | Stars | What it reaches |
|--------|---------|-------|-----------------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | 295 | **Canvas LMS itself** — courses, assignments, grades, 102–126 tools, 8 agent skills |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0, open-core | 1 | **Moodle** via Moodle Web Services — 10 free tools, premium tools sold separately |
| [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** | 1 | **Moodle, teacher side and it WRITES** — 40 facades + `ws_raw`: courses, sections, content, quizzes/GIFT, enrolment, gradebook, messaging, badges. Needs a `local_` plugin for writes → **combination is GPL-3.0, no network clause** |
| [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** | 0 | **Moodle, student side** — grades, deadlines, notifications, `submit_assignment`. Go; also exposes a REST API for non-MCP models |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 516 | The learner's **Anki** collection — spaced repetition |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 49 | No external system — it **is** the tutoring loop |
| [adriasantacreu/google-classroom-mcp](https://github.com/adriasantacreu/google-classroom-mcp) | MIT *(metadata)* | 2 | **Google Classroom** — 46 tools: courses, assignments, grading, rosters, Drive |
| [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** | 1 | **Google Workspace for Education** — Classroom *plus* Docs, Sheets, Slides, Forms, Drive (29 tools) |
| 🆕 [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | **MIT** *(`1 070` B, `p274`)* | — | **Canvas, with the consent problem solved at the tool boundary** — courses, assignments, submissions, rubrics, quizzes; grade and comment. 🟢 **Ships an opt-in FERPA mode that PSEUDONYMISES student names and contact details before tool output reaches the model.** The one row on this shelf that answers the blocker the market actually states (`T45`) |
| 🆕 [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** *(`1 068` B, `p274`)* | 59 | **Brightspace / D2L** — grades, assignments, rosters. **A fourth LMS this table never listed**; two declared derivatives and a Rust implementation sit beside it on [`trending.md`](trending.md) |
| 🆕 [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | **MIT** *(`1 084` B, `p274`)* | 1 | **Blackboard Ultra** — courses, content, grades, deadlines. 🔴 **`intel/market.md` tells a studio to pitch REPLACING Blackboard. It has an MIT doorway** — the error `p267` corrected for Canvas, left standing for the other NA higher-ed incumbent |
| 🆕 [NiccoloSalvini/mcp-blackboard-ucsc](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) | **MIT** *(`1 073` B, `p274`)* | 0 | **Blackboard over the PUBLIC REST API** — no institutional plugin to get approved, which is the cheapest pilot shape on this table |
| 🆕 [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | 🔴 **AGPL-3.0** *(`34 524` B, `p274`; default ref `master`)* | 1 | **Open edX** — 33 tools, Tutor plugin + a Django facade at `/api/mcp/`. **A sixth platform.** ⚠️ AGPL **and** `/health` unauthenticated: price the network clause and fix the endpoint before any pilot |
| [pengusto/google-classroom-mcp](https://github.com/pengusto/google-classroom-mcp) | **MIT** | — | **Google Classroom** — a correctly-attributed fork of `adriasantacreu` (dual copyright in the payload) |
| [alanmagno1/google-classroom-mcp](https://github.com/alanmagno1/google-classroom-mcp) | **MIT** | 0 | **Google Classroom** — multi-account; Spanish About line, English README |
| [OmarNiazi/classroom-mcp](https://github.com/OmarNiazi/classroom-mcp) | **MIT** | 0 | **Google Classroom** — student-side, read-only by construction |
| [praisethefacts/google-classroom-mcp](https://github.com/praisethefacts/google-classroom-mcp) | **MIT** | — | **Google Classroom** — read-only courses, coursework, rosters, submissions |
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** | — | **Google Classroom** — readonly scopes; oldest copyright line in the family (2025) |
| [AStheTECH/mewcp-google-classroom](https://github.com/AStheTECH/mewcp-google-classroom) | ⚠️ **proprietary** | — | **Google Classroom** — same description, bespoke all-rights-reserved licence |

**The distinction that matters commercially:** `anki-mcp-server` and `tutor-mcp` reach *study
tooling*, which the learner owns. The Canvas, Moodle and Google Classroom servers reach the
**institution's system of record**, which is where the client's data, roster and grades actually
live. That is the difference between a demo and an engagement.

**And the three systems of record are not equally served — openness and adoption point in
opposite directions.** Pass 268 measured the third one:

| LMS | servers found | best licence | best adoption | what that means for a quote |
|-----|---------------|--------------|---------------|------------------------------|
| **Canvas** | 2 | **MIT** (payload) | **295★ / 1,026 commits** | One obvious choice, maintained, university-named. Quote it. |
| **Moodle** | 1 | AGPL-3.0, **open-core** | 1★ / 57 commits | One choice, and you pay twice (network clause + premium tools sold separately). |
| **Google Classroom** | **8** | **MIT** (payload, on 6 of 8) | **2★ / 11 commits** at best | **The most servers and the least adoption anywhere on this shelf.** Seven permissive implementations of the same idea, none of them maintained by anyone but its author, and one proprietary impostor among them. |

🔵 **Read that table as a supply signal, not a scoreboard.** A category with eight competing
MIT implementations and no adopted one is not a solved problem — it is an **unconsolidated** one.
For Canvas you adopt; for Google Classroom you **fork the closest server and own it**, and you
price the maintenance, because nobody upstream is carrying it. Do not promise "Google Classroom
support" on the strength of a repository count.

⚠️ **Scope warning specific to the Google Classroom family, and it is the biggest in this file.**
`canvas-mcp` reaches a course API. `Kimmahone/edu-workspace-mcp` reaches **Docs, Sheets, Slides,
Forms, Drive and Classroom** — a whole Google Workspace for Education tenant. The OAuth consent a
pilot asks a school for is therefore far wider than the feature being piloted, and
`OmarNiazi/classroom-mcp`'s own README states *"Google hasn't verified this app."* In EMEA that is
a GDPR conversation before it is an engineering one; in the US it is a FERPA/COPPA one. **Scope the
consent to the tools you enable, and say so in the SOW.**

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

- 🔴 **NEW in pass 269 — no AFRICAN-ORIGIN permissively licensed education agent, measured at the
  payload.** Both African-context agents located this pass serve no grant (above). The only
  Africa-engaged permissive code this base carries is
  [`AI-for-Education`](https://github.com/AI-for-Education) — MIT, LMIC-focused, Sierra Leone MBSSE
  lesson plans and Luganda benchmarks — and it is **research-grade at 1–12★**, not a deliverable.
  🔵 **Two named systems remain unreachable rather than absent:** Nigeria's **Naija Teacher AI**
  (UNESCO SDG4 case study, offline-first, target 1.5M teachers by Q3 2026) states **no licence** and
  publishes no repository this pass could find; Kenya's **Kytabu SOMANASI** is **proprietary**.
  **State it as "unreachable", not "nonexistent" — the distinction is what a client's own ministry
  contacts can change.**
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
  repositories, yet" — while **12 distinct education MCP server slugs are shelved in this file**
  (11 permissive + 1 all-rights-reserved; counted from the rows by pass 272, which found
  `intel/trends.md` still carrying **"five"** — see `T37`) (pass 267 added the
  two LMS-side ones; pass 268 added seven permissive Google Classroom servers and one proprietary
  one). **The gap got four times worse in two passes, which is the point:** the index is not
  lagging the category, it is structurally disconnected from it. The category is real and unlabelled; that is a naming gap, and a
  small opening for whoever labels it first. **Note what it cost to find them:** the topic index is
  empty, so they were located through a web search for *"MCP server Moodle Canvas LMS"* and then
  payload-verified by hand. A topic-listing leg will keep reporting this category as non-existent.
- **The Spanish-language gap was re-tested in Spanish this pass, and it holds.** A search leg run
  in Spanish — *"github tutor IA educación código abierto español 2026 repositorio"* — returned **no
  Spanish-language education agent repository at all**: the results were GitHub Education marketing
  pages, a 2019 Universidad Politécnica de Madrid paper on teaching with Git, and unrelated blog
  guides. So the gap is not an artefact of searching in English. The nearest thing located is
  [`admin978/canvas-mcp`](https://github.com/admin978/canvas-mcp) (MIT, 4★), *"Built by AGENTE 404
  S.L."* — a **Spanish company form**, but its README is in English and **no country is stated**,
  which is weaker evidence than the Portuguese-language `ai_tutor_forge` row above. **Standing
  claim, unchanged: no Spanish- or Portuguese-language education agent with adoption.**
- **Pass 268 tested the Spanish gap a third way — against a family of eight, not a query — and it
  still holds.** The Google Classroom MCP family contains
  [`alanmagno1/google-classroom-mcp`](https://github.com/alanmagno1/google-classroom-mcp), whose
  **About line is in Spanish** (*"Servidor MCP para Google Classroom: cursos, tareas pendientes,
  entregas y materiales desde Claude"*) — and whose **README is in English**. The most capable
  server in the family is by an author with a Catalan name, and **its README is in English too,
  with no country stated.** 🔵 **The nearest-miss evidence has therefore got *weaker*, not
  stronger:** `ai_tutor_forge` had a Portuguese README; this has a Spanish *metadata field*.
  Record the grade and do not let a Spanish sentence in a sidebar become a LATAM or Iberian
  provenance claim in a deck.
- **🆕 A Korean-language education agent now exists at payload grade, and that is a new APAC
  datum.** [`Kimmahone/edu-workspace-mcp`](https://github.com/Kimmahone/edu-workspace-mcp) (MIT,
  payload) has a **Korean README**, references **Korean curriculum standards**, and implements
  `docs_import_hwp` / `docs_export_hwpx` — HWP/HWPX being Korea's national document formats, which
  is implementation evidence rather than prose. **Graded exactly as `ai_tutor_forge` was: LANGUAGE
  evidence.** No country and no institution is stated, so "Korea-origin" is **not** asserted;
  "Korean-language, Korean-format-aware" is. It pairs with South Korea's **AI Basic Act, in force
  22 January 2026** — the one APAC jurisdiction with a comprehensive statute — so the language
  supply and the regulatory demand have appeared in the same country in the same year.

## Pass 270 note — this table gains no rows, and the reason is a measurement

🟢 **Zero agents were added this pass, and nothing was added to meet the brief's five-row minimum —
the table above clears it many times over.** This is the **fifth consecutive measured nil return**
on the education-agent supply channel.

**What was and was not searched, so the absence is informed rather than silent:**

| leg | run? | why |
|---|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **no** | measured **saturated across four passes**; `p269`'s standing instruction is to spend the generic legs **last, not first**. A fifth identical measurement buys nothing. |
| `github trending education AI 2026` | 🔴 **no** | same |
| `open source platform education ERP / CRM / SIS` | 🔴 **no** | same |
| `curriculum abierto IA primaria ... licencia MIT GitHub 2026` *(Spanish)* | 🟢 **yes** | `Gap 367`'s one unspent language limb |

🔴 **The Spanish leg's yield: nine repositories, eight of them university student course
portfolios** (`ia-aplicada-2026` and forks, `InteligenciaArtificial`, `proyecto_ia`, `cursoIA2026`)
**and the ninth already on this base** ([`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia),
CC BY-SA 4.0 at payload — `p268`'s slug gate caught it). **No row qualified.**

🟢 **`Gap 367` therefore holds in a fourth language** — Hindi and Chinese (`p269`), Spanish (`p270`),
and English throughout. **There is still no permissively licensed primary-band AI-literacy
curriculum.** 🔵 The nearest permissive primary-band artefact,
`DECK6/korean-elementary-learning-map` (**MIT**), is an ontology of a primary **curriculum**, not a
primary **AI-literacy course** — a distinction that decides whether it answers the gap, and it
does not.

🟢 **One falsifiable limb remains and it costs an email:** `datawhalechina/ai-edu-for-kids` carries
CC-BY-NC-SA-4.0 as **organisational template boilerplate**, not as a decision (`p269`, `T27`) — so
it is the licence on this base **most likely to move if asked.**

## Pass 269 — the African agent tier exists, and the question it answers is not the one that was asked

Pass 267 instructed *"Kenya, Nigeria, South Africa and Egypt as four separate queries, never
paired"*, and pass 268 restated it as the cheapest fix for **"EMEA means Europe in this base."**
Pass 269 ran it. Four legs, four substantive returns — and on the **agent** shelf specifically, the
result is sharper than "nothing found".

🟢 **Two African-context education agents are now located and graded**, which is two more than this
base has ever carried: [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South
Africa, Grades 8–12) and [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria).
Both are in the licence-UNVERIFIED table above, because **neither serves a grant on any channel** —
no payload on 19 paths, and no `license` field in the package metadata either.

🔴 **The gap's grade therefore goes UP, not away.** This base previously recorded, in
[`agents/trending.md`](trending.md), that an Africa-focused leg *"returned no repository-level asset
— only a training provider, not code."* That was a **search-level** absence. Pass 269 replaces it
with a **payload-level** one: the repositories exist, they were resolved by ref, probed on 19 paths
and read in their metadata, **and the grant is missing in both.** 🔵 **An absence measured at the
payload is a different and stronger claim than an absence measured at the query**, and it is the one
to brief: *"there is African-built education-AI code, and none of it is licensed for you to ship."*

🟡 **The two rows fail differently, and the difference is the actionable part.** `edunaija-os` is
simply silent. `EduTwin-Africa` ships the **placeholder text** — *"Add the project's chosen license
here before publishing"* — which means its author has already written down that the grant is
missing. **That is the one row on this shelf where a request has a plausible answer**, and it costs
an email rather than a fork. Contrast [`ls1intum/Athena`](https://github.com/ls1intum/Athena), which
has survived 76 path/ref probes in silence across three passes.

🔵 **And a naming hazard worth one line in any proposal.** `Valexxy/edunaija-os` is **not** the
EduNaija AI Tutor published at ACL AfricaNLP 2026 (DOI `10.18653/v1/2026.africanlp-main.11`) — that
is a five-agent LangChain + FAISS system with English/Yoruba/Hausa/Igbo support, **whose code this
pass could not locate at all**. The repository that shares its name is a starter codebase for a
different thing. **The paper is not the repo, and the repo is not the paper.**

## Pass 268 provenance note — Iris and Pyris are MIT at PAYLOAD grade, and serve no README

Both rows were re-probed this pass because `P17` in [`compose/patterns.md`](../compose/patterns.md)
now depends on them.

🟢 **The grant is stronger than this file previously recorded.** Both
[`ls1intum/Iris`](https://github.com/ls1intum/Iris) and [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris)
serve **MIT at `main/LICENSE`**, and the copyright line reads **"Copyright (c) 2023 TUM Applied
Software Engineering"** — so TU Munich provenance for these two is **payload-quoted**, not
README-quoted, which is a grade *above* the evidence this file carries for Artemis itself.

🔴 **And a defect worth recording: neither repository serves a README.** `README.md`, `readme.md`,
`README.rst` and `README` were all probed across `main`/`master`/`develop` — **404 on every
combination**, while `LICENSE` returns 200 on `main`. The descriptions in the rows above therefore
have **no source inside these repositories**; they derive from the Artemis documentation. 🔵 **Record
it rather than quietly relying on it:** a row whose capability claims cannot be traced to its own
repository is fine to build on and wrong to quote verbatim to a client. Confirm Iris's pedagogical
constraints against the Artemis docs, or against a deployment, before they reach a proposal.
