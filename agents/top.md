---
industry: education
region: Global
updated: 2026-10-19
---
# Top open source AI agents — education

## Pass 321 · 2026-10-19 (seventh pass of this date) — the named-gap sweep, executed

**One row added here, one to the evaluation table, two to `repos/foundations.md`, and six measured negatives recorded in that file's sweep table.** Pass 319 closed its topic-sweep section with an explicit to-do: *"Untested and worth a pass: Arabic, Hindi, Japanese, Korean, French and Indonesian topic tags, and the `wirlernenonline` organisation, whose GitHub org page could not be read this pass."* **Pass 321 executed that list in full.** Six of the seven items are negatives, and they are written down in `repos/foundations.md` rather than left as silence. The seventh is the pass's find.

**The find is an organisation, not a repository.** `wirlernenonline` is **404 — the org does not exist under that name.** The real account is **`openeduhub`**, and it holds **67 public repositories** of OER infrastructure for WirLernenOnline.de, built on edu-sharing. Four were read first-hand this pass: an Apache-2.0 tutor, an Apache-2.0 LLM-as-judge prompt bench, a **CC0-1.0 SKOS competency vocabulary with 938 commits**, and a 1,397-commit ETL **with no licence file at all**. The vocabulary repository corrects a claim this KB has carried since p319 — see `repos/foundations.md`.

**Method, re-tested this pass rather than inherited, and it reproduces.** `github.com` is reachable with the fetch tool and **non-GitHub origins are not**: `www.multistate.us` failed at DNS (`getaddrinfo ENOTFOUND`) when attempted directly. A `curl -sI` probe and a proxy-status probe were both **refused by the sandbox classifier as "Exfil Scouting"** and were **not worked around** — so this pass measured reachability by fetching, not by scanning. **Every repository claim below and in `repos/foundations.md` is first-hand off github.com; every regional claim is snippet-sourced and labelled as such in `intel/market.md`.**

**The prescribed global search battery returned nothing this KB did not already hold, at lower precision than the KB holds it.** The four regional searches returned the EU AI Act Annex III deferral, `H.R. 8747`, the 134-bills/31-states count, Canada's *AI for All*, the NYC moratorium, Korea's 2026-01-22 commencement, India's Class 3 mandate and Brazil's Bill 2338 — **all already in `intel/` with OJ numbers, dates and tracker caveats the snippets lacked.** That is the second pass in a row to reach that verdict, and it is why this pass spent its budget on the GitHub channel instead.

**Pass 320 · 2026-10-19 (sixth pass of this date). No rows added, and that is the finding.**
Five new candidates were read first-hand off GitHub this pass; **all five were rejected** — four on
weight or licence, one because it is not an agent. They are recorded in the rejection section so
pass 321 does not re-find them. **Three existing rows were re-verified** and one moved
(`DeepTutor` 41.7k → 41.8k ★). The count stands at twenty-six.

**The method constraint was re-tested this pass rather than inherited, and it reproduces exactly.**
`curl -sI https://github.com/...` returns **403 at the session proxy**; `www.future-ed.org`,
`www.lw.com` and `www.iesalc.unesco.org` were each attempted directly with the fetch tool this pass
and all three failed at DNS (`getaddrinfo ENOTFOUND`). **github.com remains the only reachable
origin.** Every repository claim below is first-hand; everything in `intel/market.md` is
snippet-sourced and labelled there.

**The one material addition this pass is in `repos/foundations.md`, not here:**
`adamzammit/LTIPlugin` (**GPL-3.0**, 14 ★, 97 commits) is the first artefact this KB has found at
the grade-passback seam that carries **an actual OSI-approved licence** rather than no licence at
all. It is not an AI tool and probably not LTI 1.3 — read the caveat with it — but it narrows the
"everything at this seam is unlicensed" claim this file has made for four passes.

**Pass 319 · 2026-10-19.** Twenty-six rows, twenty-six real repos. No header rows, no placeholders,
no example data.

Verification method, re-confirmed and stated more precisely this pass. `curl -sI` to github.com
returns **403 at this session's proxy**; the session's fetch tool reaches **github.com and nothing
else** — `arxiv.org`, `unesco.org`, `education.ec.europa.eu`, `koreaherald.com`, `k12dive.com` and
`iadb.org` are all refused at connect time (`connect_rejected`) by the egress policy. So every row
below was read off its GitHub page first-hand, and **every non-GitHub fact anywhere in this KB this
pass rests on search snippets, not a primary read.** The **Checked** column says which pass took
the repository reading.

**Pass 319 adds eight rows and closes the gap this KB has declared for five passes: the
evaluation layer.** Four permissively licensed artefacts for measuring whether a tutor *teaches*
now exist, and their convergent finding is that **LLM-judged "helpfulness", the metric the sector
reports, is unsound** — see the eval section below. That forces a correction to pass 318's own
reading of `lumen`.

**Pass 319 also escalates pass 318's star finding.** Pass 318 found a README asking AI agents to
star a repo. This pass found the same pressure *productised*: `karanb192/algo-sensei` (MIT, 293 ★,
**9 commits**) ships `scripts/star_invitation.py`, a once-per-machine gate, with a unit test and a
dedicated CI workflow. Detail below. With pass 317's finding that stars run too *low* on
institutional infrastructure, the ★ column is a rough size signal and nothing more. **Rank on
commit count, release cadence and licence.**

## The table

| Agent | Repo | Licence | ★ | Checked | What it does | Use it for |
|---|---|---|---|---|---|---|
| tutor-chatbot | https://github.com/openeduhub/tutor-chatbot | Apache-2.0 | 0 | p321 | Learning-companion chatbot for **WirLernenOnline.de**, Germany's publicly funded OER portal: blends a curated QA dataset with LLM answers, queries the WLO / edu-sharing API (`https://www.wirlernenonline.de/api/v1`) for matching learning materials and attaches them to the answer as direct links, filters by subject, content type and source, and reports **Bloom-taxonomy learning analytics**; extracts learning metadata from the learner's question. Provider is **OpenAI or GWDG** (German academic compute). 10 commits, React/Vite, Apache-2.0 stated in both the LICENSE and the README | **The only Apache-2.0 public-sector tutor in this KB, and the only one with a sovereign-inference path** — read it for the architecture, not as a dependency: 10 commits is a prototype |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 41.8k | p320 | Lifelong personalised tutoring agent; v1.6.15 (2026-10-19), 2,935 commits, 5.3k forks, paper arXiv 2604.26962. README now describes it as an "agent-native learning workspace" with an inspectable three-layer memory, Co-Writer, Book and Partners | The strongest permissive starting point for a tutor product |
| Study-Mate | https://github.com/Miaotofu01/Study-Mate | MIT | 1.1k | p319 | Maths/CS study partner shipped as a skill bundle: plans a learning route, explains concepts, drives project work; five roles (material collection, illustration, course design, teaching, exercise evaluation); progress stored as files in a local workspace with a shared cross-subject memory of skill level and effective explanation styles; 723 commits; packaged for DeepSeek Harness, Google Antigravity and Codex/ChatGPT Work; docs zh + en | The largest permissive APAC skill bundle — read it for the files-as-learner-state pattern |
| instructional_agents | https://github.com/DaRL-GenAI/instructional_agents | MIT | 488 | p319 | ADDIE-model multi-agent instructional design: generates syllabus, slides, scripts and assessments; catalog mode for structured input, copilot mode for per-phase feedback; LaTeX/PDF, HTML and PPTX output; web UI, CLI (`run.py`) and REST API; 95 commits, 106 forks; arXiv 2508.19611, **accepted to EACL 2026 Main**; a public fork of `Hyan-Yao/instructional_agents` | Course-production work — the peer-reviewed answer to "reduce faculty workload" |
| lineage-skill | https://github.com/JuneYaooo/lineage-skill | Apache-2.0 | 459 | p319 | Distils course videos, audio, books, PDFs and transcripts into a source-backed teaching skill: micro-lessons with ASCII/SVG diagrams, two formative questions per topic with feedback, practice/error/review tracking, source references kept on key claims; 50 commits; docs zh + en | **The first permissively licensed skill bundle at scale** — the licence-clean alternative to `education-agent-skills` |
| universal-examprep-skill | https://github.com/ZeKaiNie/universal-examprep-skill | MIT | 309 | p319 | Exam-prep tutor as an Agent Skill: teaches chapter by chapter with page citations, crops figures out of the learner's own slides, quizzes from their past papers, tracks mistakes, builds a cheat sheet; state local, **no external vector DB**; 183 commits; installs across 40+ agent hosts via `npx skills add`; docs en + zh | Engagements where the learner owns the corpus and nothing may leave the machine |
| claudemy | https://github.com/assafkip/claudemy | MIT | 317 | p319 | Skill that researches a topic and builds ~12 two-minute audio lessons with cited sources, each with a summary card, one practice task and a playbook rule; 20 commits | Audio-first micro-course generation; read for the lesson-shape template |
| algo-sensei | https://github.com/karanb192/algo-sensei | MIT | 293 | p319 | LeetCode/DSA mentor skill for Claude Code and claude.ai with tutor, hint, review, interview and pattern-mapper modes, hint-first by design; 9 commits, 63 forks; solution write-ups in Python, Java, C++, JavaScript, Go | The hint-ladder design — **and the star-invitation finding below** |
| smolagents | https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Minimal library for agents that think in code; 1,059 commits | The agent runtime under a tutor when you want small and auditable |
| FSRS4Anki | https://github.com/open-spaced-repetition/fsrs4anki | MIT | 4.1k | p317 | Free Spaced Repetition Scheduler as an Anki scheduler; 482 commits | Retention scheduling — the review-timing half of a tutor |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | p317 | Assigning, collecting and autograding Jupyter notebooks; 3,477 commits | Grading automation in any notebook-based curriculum |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 878 | p316 | 165 evidence-grounded teaching skills (pedagogy, assessment, curriculum) for Claude/Codex/Hermes; 149 commits | Prompt and pedagogy assets — **not** a code dependency, see caveat |
| iblai/os | https://github.com/iblai/os | MIT | 821 | p316 | Agent platform (Next.js → web/desktop/mobile) with chat, voice, SSO; 3,518 commits | A front end only — the backend is **not** in the repo, see caveat |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **MIT/AGPL-3.0 dual (skills); AGPL-3.0 (app)** | 573 | p318 | 33 agent skills turning Claude/ChatGPT/Gemini into structured tutors on spaced-repetition and active-recall principles, plus a Next.js 16 app (React Flow, Supabase, OpenRouter); K-12 through career and social skills; bilingual EN/zh; 36 commits | APAC-authored evidence for trend 7 — **and the star-solicitation caveat below** |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 62 | p319 | Local-first teacher assistant: imports PDF/DOCX/PPTX/TXT/MD, drafts teacher DOCX, student DOCX, PPTX slides, multi-week units and assessments for human review; local dashboard and API, MCP server, Telegram bot, Drive integration; Anthropic/OpenAI/Gemini/Ollama/OpenRouter; v9.18.2026.1 (Beta), 778 commits; MacxLabs | **The teacher-facing-only build** (trend 3, pattern P7) — and it states plainly that local storage does not mean local processing |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT | 520 | p316 | MCP server exposing the Anki flashcard app to any LLM client; 258 commits | Wiring a real spaced-repetition store to an agent without writing a scheduler |
| Educhain | https://github.com/satvik314/educhain | MIT | 387 | p317 | Python package generating MCQs, lesson plans and flashcards with LLMs; 578 commits | Content-generation pipelines behind an authoring tool |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** | 932 | p317 | AI tutor built on Theory-of-Mind reasoning: reasons about the learner's needs and rewrites its own prompts to suit them; v0.8.0, 356 commits | Study the ToM prompting approach — **copyleft, see caveat** |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 289 | p316 | Socratic adaptive tutor shipped as both portable agent skills and a self-hostable React/FastAPI app; 76 commits | The clearest worked example of the skill-plus-app delivery shape |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 268 | p317 | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase), UC Berkeley CAHLR; 1,045 commits. README: "For LMS integration, a middleware backend is required by Learning Tools Interoperability (LTI)" | Mastery modelling / hint sequencing where you must explain the pedagogy |
| otter-grader | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | 161 | p315 | Python and R autograding with containerised execution | Autograding where submissions must run sandboxed |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 145 | p316 | Local-first block-based adaptive workspace: upload material → notes, quizzes, flashcards, tutor; 10+ LLM providers, 194 commits | An offline/on-prem tutor shell when data cannot leave the building |
| gen-mentor | https://github.com/GeminiLight/gen-mentor | CC0-1.0 | 135 | p316 | LLM multi-agent framework for goal-oriented learning in an ITS; WWW '25 oral, arXiv 2501.15749; 91 commits | A peer-reviewed multi-agent ITS architecture you can cite in a bid |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 111 | p315 | Educational collaborative AI tutoring platform; arXiv 2602.07176 (Feb 2026) | An academically documented tutor platform you can fork and cite |
| lumen | https://github.com/ahmedEid1/lumen | **GPL-3.0** (LICENSE file; README badge wrongly says MIT) | 89 | p318 | Multi-agent orchestrator builds a private course from a one-sentence goal in ~50s, then a course-scoped RAG tutor teaches it; v2.0.0 2026-06-06, 828 commits; FastAPI + Next.js 15 + pgvector; BYOK envelope-encrypted | **Read for its published evals, not for its licence** — see below |
| LTLTutor | https://github.com/brownplt/LTLTutor | **GPL-3.0** | 12 | p319 | Misconception-driven adaptive tutor for Linear Temporal Logic: models the specific wrong beliefs learners hold and targets practice at them; Brown PLT; 320 commits; CAV 2025 **Distinguished Paper** (Prasad, Greenman, Nelson, Krishnamurthi) | **Read, do not link.** The clearest worked example of misconception modelling as the decision layer |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 52 | p316 | MCP server that turns any LLM into an ITS: skill graph, BKT, FSRS, prerequisite rules, narrative memory; SQLite local / PostgreSQL hosted; 467 commits | The deterministic-pedagogy engine — still the architectural find of p317 |

## The evaluation layer exists now — and its first finding is that the sector's metric is unsound

Five passes of this KB have declared: *no credible open source way to measure whether a tutor
teaches.* **That gap is closed.** Four artefacts were read first-hand this pass, three of them MIT,
and they do not agree with the way this sector reports quality.

| Artefact | Repo | Licence | ★ | Commits | What it is |
|---|---|---|---|---|---|
| ki-prompt-benchmark | https://github.com/openeduhub/ki-prompt-benchmark | Apache-2.0 | 0 | 3 | **An LLM-as-judge prompt bench published by a public OER operator.** Compares the metadata-generation prompts live in edu-sharing's `mds.xml` v10.0 against an optimised set: a judge model scores both on **five criteria, 1–10**, names a winner and gives a rationale, while the harness measures generation time and token usage across providers (OpenAI direct, B-API→OpenAI, **AcademicCloud**). Test material can be a sample, a WLO repository item or any URL via a text-extraction service. Judge feedback is accumulated across runs to regenerate an improved prompt per field, and prompt sets export back to `mds.xml`. Next.js 15 / React 19 / TS 5 |
| MathTutorBench | https://github.com/eth-lre/mathtutorbench | **CC BY 4.0 badge / CC BY-SA 4.0 footer — contradictory, see below** | 45 | 25 | Peer-reviewed benchmark for open-ended pedagogical capability: 3 teacher skills, 7 tasks, 9 configs — problem solving, socratic questioning, solution correctness, mistake location, mistake correction, plus four pedagogy win-rate tasks. **Pedagogy is scored by a ~1.5B scaffolding reward model against ground-truth teacher utterances, not by an LLM judge.** EMNLP 2025 main, oral (arXiv 2502.18940); Macina, Daheim, Hakimi, Kapur, Gurevych, Sachan; reward-model data on Hugging Face (`dmacjam/pedagogical-rewardmodel-data`) |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT | 3 | 8 | Evaluation framework for LLMs as maths tutors: a LoRA-finetuned automated evaluator, an open LLM-as-judge path (`prometheus-eval/prometheus-7b-v2.0`) and a GPT-5 judge path; backend plus a frontend demo; v1.0.0, 1 Dec 2025; ships a 10-example sample only — you bring the dataset. MBZUAI EduNLP Lab (Naeem, Maurya, Petukhova, Kochmar), arXiv 2512.03688 |
| conv-vs-ped-tutor | https://github.com/bydeng01/conv-vs-ped-tutor | MIT | 3 | 12 | **Pre-registered audit** of whether an LLM helpfulness judge rewards answer leakage that reduces a student's later independent work. Two tutors wrap the same frozen base model and differ only in policy structure — ConvTutor is a single LangGraph node, PedTutor a multi-node state machine — against a no-tutoring cold baseline, in algebra. Per-turn/per-session/per-replicate tables, metric summaries and inference verdicts committed; ~100 MB of transcripts released separately under SHA-256 manifests. arXiv 2607.28128 |
| ability-levels-audit | https://github.com/bydeng01/ability-levels-audit | MIT | 4 | 8 | Pre-registered LLM-judge audit with frozen data: 990 accepted judge ratings, a complete 55 × 3 × 2 grid checked by hash before analysis runs, registered diagnostics separated from labelled post-hoc analysis, and the pre-registration, amendments and decisions log in `protocol/`. Headline result is a methodological one: **difference-in-differences on a censored rating scale can manufacture an effect that is not there.** arXiv 2608.27309, NewInML @ NeurIPS 2026 |

**What they jointly establish, and it is uncomfortable for everyone selling in this sector:**

1. **LLM-judged "helpfulness" is not a pedagogy signal.** The leakage audit exists precisely because
   a judge can reward a tutor for handing over the answer. A separate study found at AIME-Con 2026
   concludes that human oversight remains necessary for nuanced instructional assessment
   *(snippet-sourced, not read first-hand)*.
2. **A bounded rating scale plus a before/after comparison can produce an effect from nothing.**
   That is the shape of almost every tutoring-uplift claim a client will be shown.
3. **The one peer-reviewed benchmark here deliberately avoids an LLM judge** and scores pedagogy
   with a trained reward model against real teacher utterances instead.

**The correction this forces on pass 318.** Pass 318 called `ahmedEid1/lumen` "the most credible
artefact of the pass" for publishing authoring 3.85/5, tutor 2.33/5 and ingest 0.83/5 about itself.
Publishing unflattering numbers is still to its credit — **but those are judged scores, and this
pass's evidence is that judged scores of helpfulness are the wrong instrument.** Read lumen for the
*habit* of publishing an eval, not for the values. Where a client needs a number, run
MathTutorBench and report what it measures.

**Two licence warnings on this tier, both material:**

- **MathTutorBench's licence is self-contradictory**: the README badge says CC BY 4.0, the footer
  says CC BY-SA 4.0. **That is the fifth licence inconsistency this KB has verified**, and the
  first in the eval layer. ShareAlike on a benchmark attaches to derivative benchmark *data* — the
  annotated items a Globant engagement would add. Resolve it with the authors before building a
  client-specific extension on it.
- **All four are content or research licences, not product dependencies.** CC on the benchmark data,
  MIT on audit code that ships with its own frozen data. Use them as measurement instruments inside
  an engagement; do not vendor them into a deliverable.

**What to do with this tomorrow:** add an eval stage to every tutor engagement, score with
MathTutorBench's task shapes, borrow the audits' discipline — pre-register the comparison, freeze
the data, hash it, keep a decisions log — and **never report an LLM-judged helpfulness score as
evidence of learning.** See pattern P1's new "prove it teaches" stage.

## The LTI gap, pass 319: re-checked, unchanged — and now a third unlicensed artefact

`blamb/lti-tutor` was re-read first-hand this pass. **Its licence is still "To be decided", it still
has 0 stars, 0 forks and 39 commits.** Nothing has moved since pass 317 — two passes of no change.

**And the pattern behind it repeated again this pass.** `JaimeArriagadaRosas/Plugin-Feedback-Canvas`
(0 ★, **160 commits**, Spanish-language docs) is a full-stack **LTI 1.3 plugin for Canvas** in which
an instructor generates academic feedback from templates, context variables and a choice of AI
provider, and **must review and approve it before it reaches the student** — the human-in-the-loop
control that Oklahoma's 2026 statute and every US district AI policy now demand, built and working.
React/Vite over Node/Express, Postgres and Redis, Gotenberg for document conversion, Vitest/
Playwright/Testcontainers for test, and a README that honestly states it is in pre-production
validation. **It has no LICENSE file.** That is the third artefact at exactly this seam that cannot
be used — after `luffycodes/Tutorbot-Spock` and `blamb/lti-tutor` — and the first written in
Spanish, which makes it the closest thing in this KB to a LATAM-authored LMS-integrated AI tool.
**Ask the author for a licence; it costs an email.** Until then, read the shape and rebuild it.

This matters because it is the single highest-value watch item in this KB: it implements LTI 1.3
against Moodle with dynamic registration, deep linking and completion passback through Assignment
& Grade Services on `ltijs` — precisely the artefact this KB has declared missing for four passes —
and **one commit adding a LICENSE file would make it the most strategically valuable repo here.**
Until then default copyright applies and Globant cannot use it, fork it, or copy its approach into
a client deliverable.

**Re-check it every pass. It is a one-line check with a large payoff.**

**Pass 320: re-checked, and the gap stands — but it is now a narrower claim.**
`adamzammit/LTIPlugin` (**GPL-3.0**, 14 ★, 97 commits, `master`) makes **LimeSurvey act as an LTI
provider**: a learner launches a survey or assessment from the LMS and the plugin **returns a
score back to the gradebook** as a value between 0.0 and 1.0 derived from a LimeSurvey expression,
with **setup instructions in the README for Canvas, Moodle, openEdX and Blackboard** and support
for LimeSurvey 3.x–7.x. **Two caveats decide how this may be used.** First, it is **not an AI
tool** — it is assessment delivery with outcome passback. Second, **the page never names an LTI
version**, and it bundles `LTI-Tool-Provider-Library-PHP`, which points at the **legacy LTI 1.x
Basic Outcomes path rather than 1.3 Advantage AGS** — so do not scope it as an Advantage
implementation without reading the submodule. **What it does change:** for four passes this file
has said that every artefact at the grade-passback seam is unlicensed. That is no longer true.
**GPL-3.0 is a real licence**, it sits on the same copyleft side of this KB's architectural line as
`tutor-gpt`, `lumen` and `LTLTutor`, and the plugin is a readable, four-LMS reference for how
outcome passback is actually wired. **The unfilled gap is specifically an AI tutor speaking LTI
1.3 Advantage under a permissive licence. Nothing found this pass changes that.**

**What did change on the library side:** `repos/foundations.md` now records **`tsugiproject/tsugi`
(Apache-2.0, 376 ★, 266 forks, 4,011 commits, Apereo Incubating)** — an LTI library and
multi-tenant tool-hosting environment an order of magnitude larger than `pylti1.3`, from the
author of the LTI specification. **Its GitHub page does not state which LTI versions it
implements**, so the Advantage-surface question is open; verify before scoping. It does not replace
an LTI-native tutor, but it materially changes the concentration risk this KB has flagged since
pass 317.

The gap stands as worded in pass 317: there is no *usably licensed* open source LTI 1.3 AI tutor.
What pass 318 adds is a mitigation for the *other* half of the problem — see the `ltibootcamp`
finding in `repos/foundations.md`, which maps the LTI 1.3 library landscape across seven languages
and takes some of the concentration risk off `pylti1.3`.

## Star solicitation has been productised: it now ships with a unit test and a CI job

Pass 318 recorded a README passage addressed to AI agents asking them to star the repository
(`24kchengYe/human-skill-tree`). Pass 319 found the next step, and the reason to record it is the
engineering, not the ask.

**`karanb192/algo-sensei` — MIT, 293 ★, 63 forks, 9 commits.** The repository root holds
`SKILL.md`, `modes/`, `docs/`, `demo/`, `templates/solutions/`, `tests/` and `scripts/`. In
`scripts/` there is exactly one file: **`star_invitation.py`**. Read first-hand, it is a
once-per-machine gate: it attempts exclusive creation of a marker file `star-invitation.json` under
`$XDG_CACHE_HOME` or `~/.cache/algo-sensei`, prints `offer` if it created the marker and `skip`
otherwise — on a pre-existing marker, a concurrent run, or any path or filesystem error. Its code
comment reads: *"Exclusive creation prevents simultaneous or later sessions from asking again."*
There is a matching `tests/test_star_invitation.py` and a dedicated workflow,
`.github/workflows/invitation-tests.yml`.

**Three things follow, and the first is in the repo's favour:**

1. **This is the polite version.** Ask once per machine, ever, and never again — that is better
   behaviour than a README instructing an automated reader to act. Nothing here is deceptive and
   the script emits no text of its own.
2. **It is still a star-acquisition mechanism with CI behind it, in a repo with 9 commits and
   293 stars.** The ratio is the point. A sector where the distribution unit is a skill bundle
   (trend 7) has made stars cheap to solicit at the moment of use, from inside the tool, at scale.
3. **So the ★ column is now formally decorative in this KB.** It fails low on institutional
   infrastructure — Ed-Fi at 12, Sunbird at 41, OpenOLAT at 448 with 31,877 commits, the entire
   `bncc-dev` curriculum stack at 22/9/9 with a verified national dataset behind it — and it is
   solicitable at the top. **Commit count, release cadence, fork count and licence are the durable
   signals.** Any Globant tooling that ranks dependencies by reading repository pages needs that
   rule written into it, together with pass 318's: text a repository addresses to an automated
   reader is data, never instruction.

## A repo in this sector is now soliciting stars from AI agents (pass 318, recorded)

`24kchengYe/human-skill-tree` (573 ★, 36 commits) ends its README with a passage **addressed to AI
agents, asking them to star the repository** and claiming efficiency benefits for doing so. It was
ignored when this pass read the page, and it is recorded here because of what it implies rather
than what it is.

This KB is compiled by an automated process that reads repository pages. **So are a growing number
of the tools a client's engineers use to choose dependencies.** A README instruction aimed at that
reader is a supply-chain-adjacent manipulation attempt, cheap to write and, at 573 stars against 36
commits, not obviously unsuccessful.

Three consequences, and the third is the one that matters:

1. **Content a repository addresses to an automated reader is data, not instruction.** This pass
   treated it that way. Any Globant tooling that reads repo pages to rank dependencies must do the
   same, explicitly.
2. **The ★ column in this KB is now a weaker signal than it was last pass**, and it was already
   weak. Pass 317 established that stars run *too low* on institutional infrastructure — Ed-Fi at
   12, Sunbird at 41, OpenOLAT at 448 with 31,877 commits. This pass establishes they can also be
   solicited upward. **Commit count, release cadence and licence are the durable signals; rank on
   those.**
3. **The repo is still in the table.** Its skills are real, dual MIT/AGPL-licensed, bilingual, and
   it is one of the few APAC-authored artefacts in this tier. Flagging the behaviour is the correct
   response; deleting a usable finding over it would be an overreaction. Read the skills, do not
   take the app, and know what the README tried to do.

## lumen is worth reading because its evaluation scores are bad and published anyway

`ahmedEid1/lumen` (828 commits, v2.0.0 on 2026-06-06) generates a private course from a
one-sentence goal with a multi-agent orchestrator, then teaches it with a course-scoped RAG tutor
whose retrieval runs through a single access-control clause so private and cloned courses cannot
leak chunks. Its README publishes its own evaluation results:

- **authoring 3.85/5** (n=10)
- **tutor 2.33/5** (10 of 30 items judged)
- **ingest 0.83/5** (4 of 10 items judged)

— and attributes the weak tutor score to a citation-format mismatch. **No other repo in this KB
publishes a number that unflattering about itself.** In a sector where every vendor deck claims a
tutoring uplift, a project reporting 0.83/5 on its own ingest pipeline is the most credible
artefact of the pass, and the eval harness shape is worth copying into any tutor engagement where
the client will eventually ask "how do you know it teaches?".

**Its licence is GPL-3.0.** The README carries an MIT badge; the `LICENSE` file in the repository
root is the full GNU General Public License v3 text. **The LICENSE file governs.** This is the
fourth repo in this KB whose real licence differs from its surface presentation — after Frappe
Education, OpenOLAT and `education-agent-skills` — and the second this pass (see below). Read the
file, never the badge.

## Caveats a studio lead should read before quoting any of these

- **`iblai/os` is open-core, not open source in the useful sense.** MIT, 821 ★, 3,518 commits — and
  its README says plainly: *"ibl.ai/os requires the ibl.ai backend platform for authentication, AI
  agent APIs, and data services. The backend is not included in this repository."* You can read and
  fork the client; you cannot self-host the product.
- **`education-agent-skills` is CC BY-SA 4.0 — ShareAlike, and a content licence, not a code
  licence.** Derivative teaching material must be released under the same terms. That is a live
  constraint on a client deliverable.
- **`human-skill-tree` is dual-licensed and the halves differ.** The skills are MIT/AGPL-3.0 dual;
  **the web app is AGPL-3.0 only.** Take the skills, leave the app, and record both licences
  separately in the inventory — a single "MIT/AGPL" line in a licence register is not good enough
  when the permissive half is the only half you can use.
- **`gen-mentor` is CC0-1.0.** Usable, but a paper-companion release (91 commits) with no warranty
  culture. Cite the architecture; do not take the dependency.
- **`Educhain` is 387 ★** — earlier passes recorded "~12k ★", which was wrong.
- **`DeepTutor` is the outlier in both directions.** Re-verified first-hand this pass: Apache-2.0,
  41.7k ★, 5.3k forks, 2,935 commits, **v1.6.15 released 2026-10-19**. A release on the day of this
  pass makes pinning a version mandatory, not advisable.
- **`Bloom`, `OpenTutor` and `anki-mcp-server` are small but honest.** 76, 194 and 258 commits.
  Reference shapes and composable parts, not platforms.
- **The three graders are BSD-3-Clause, not MIT.** Permissive, but the attribution clause is real.
- **The eight rows added in pass 319 split into three kinds, and the difference matters when
  quoting.** Four are **skill bundles** (Study-Mate, lineage-skill, universal-examprep-skill,
  algo-sensei, plus claudemy) — prompt and pedagogy assets that run inside a client's chosen agent
  host, not services you deploy; they are cheap to adopt, invisible to procurement and carry no
  SLA. Two are **applications** (instructional_agents, Claw-ED) with real commit histories, both
  MIT, both human-review-first by design. One is a **research tutor** (LTLTutor, GPL-3.0) to read
  rather than link.
- **`instructional_agents` is a fork, and the fork is the one with the stars.**
  `DaRL-GenAI/instructional_agents` (488 ★) is a public fork of `Hyan-Yao/instructional_agents`.
  Pin the fork you actually read, and record which upstream it tracks.
- **`Claw-ED`'s own README is the model for how to describe a "local-first" product.** It states
  that local storage does not mean local processing: hosted models still receive prompts and
  content, and web search, image retrieval, Telegram, Google integration and package installation
  all reach out. Running genuinely local needs a local model and those features off. **Quote that
  distinction in any on-premise proposal** — it is the honest version of a claim most vendors make
  loosely, and it is the same distinction the COPPA finding in `intel/market.md` turns on.
- **`tutor-gpt` and `lumen` are the two copyleft rows.** Both GPL-3.0, both in the table to be read
  rather than linked. `tutor-gpt` for its Theory-of-Mind prompting, `lumen` for its eval harness.

## Rejected after verification — recorded so the next pass does not re-find them

**Pass 320 added five rejections and no rows. They are listed first.**

- **`Willie-Liao/lesson-library` — NO LICENCE, and 1 commit.** 0 ★. An MCP server for teachers in
  which an agent searches a lesson library, folds near-duplicate materials together with vector
  search, proposes progression/regression/related links, and **stages every change for teacher
  approval in a local web UI before it is written as Markdown/YAML**; graph, timeline and calendar
  views; docs marked v0.3.2, 2026-10-12. **The shape is right and the review gate is the one this
  KB keeps asking for.** Three disqualifiers: there is no LICENSE file (the README offers a prose
  "educational research and non-commercial school lesson preparation" use statement, which is not a
  licence and reads as a restriction), **the repository has a single commit**, and although the
  description claims "any subject", **the only documented deployment is middle-school FLAG football
  (Grade 6/7, 3 teachers, ~60 students)** and the motor-skill taxonomy is football-specific. A
  general design with a single-domain implementation. Watch the licence.
- **`CristianHeyde/language-teaching-skills` — MIT, but 0 ★ and 4 commits.** Six standalone agent
  skills for language teachers: `staff-assistance`, `task-design`, `submission-review`,
  `study-planning`, `course-architecture`, `lesson-planning`. The README is explicit that the skills
  **guide procedure only and grant no tools or permissions**, which is the correct design for this
  category. **The licence is clean and the taxonomy is sensible; the weight is four commits.**
  Rejected on the same standard this file applied to `Gchism94/ai-tutor` in pass 318 — recorded
  rather than listed so the rule stays consistent. Re-check if it grows.
- **`Bimbi-Dev/OpenTeacher` — NO LICENCE, and the agent logic is not written yet.** 0 ★, 32
  commits. **Peru**, Hackathon AIdea Lima 2026, README in Peruvian Spanish, aimed at MINEDU
  teachers: a WhatsApp agent to which a teacher reports a classroom incident by text or audio, which
  replies with emotional containment and immediate tactics and logs the incident for per-student and
  per-classroom reports. **What actually runs is the web simulator**, audio capture behind a consent
  gate, Whisper transcription and an Anthropic SDK wrapper, both with mock modes. The WhatsApp
  webhook is marked *"Congelado, sirve de evidencia"* and **`lib/prompts.ts` and `lib/agents.ts` are
  marked `PENDIENTE`** pending a product brief. Searched for and recorded **because it is
  LATAM-authored supply, which this KB has repeatedly declared its scarcest category** — the
  placement is the finding, not the code. Not usable.
- **`alarcon7a/english-teacher-ai` — MIT badge with NO LICENSE FILE.** 5 ★, 11 commits. Spanish
  README; a spoken English tutor taking Spanish or English in and returning text and audio, on
  Gradio + LangChain with Gemma 2 (9B) via Ollama or Gemini, and **Meta's SeamlessM4Tv2 for both
  STT and TTS** — a genuinely interesting local-first speech choice. Rejected on two counts: the
  licence is **declared in a badge but not filed**, so default copyright applies, and the README
  does not match the tree (it tells you to run `teacher.py`; the file is
  `English_teacher_with_gemma2.py`) while listing Ollama under "Google tools". **The badge-without-
  a-file pattern is now frequent enough in this sector to be worth stating as a rule: a licence
  badge is a claim, a LICENSE file is a licence.**
- **`laurauguc/grading_assistant` (GradeMate) — MIT, 4 ★, and it carries a correction to this KB's
  own conclusion.** Already carried: an earlier pass read its licence blob and recorded it at 4 ★
  inside the "agentic-grading cluster" whose three repos total 4 stars, and concluded **"grading has
  no open-source shelf."** **This pass read the commit count that conclusion was drawn without:
  260 commits.** That does not overturn the conclusion but it narrows it — *one* of those three
  repos has real volume behind it, and "4 stars across three repos" invited the reading that all
  three were weekend projects. Teacher-facing grading of written work with curated **or
  teacher-uploaded rubrics**, a `rubrics/` folder and a `load_grading_rubric_data` management
  command; ReactJS over Django. **It stays out of the table for two reasons that are not weight:**
  it is a teacher tool rather than an agent, and it **requires a `GOOGLE_API_KEY`**, so the model is
  not pluggable as shipped. Promote it to `verticals/solutions.md` if a client asks for assisted
  marking. **The general lesson: a star count is not a volume measure, and this file has now been
  caught reasoning from one.**

- **`blamb/lti-tutor` — NO LICENCE ("To be decided").** Re-verified p319: unchanged at 0 ★, 39
  commits. The LTI 1.3 tutor this KB needs, and unusable. Watch it every pass.
- **`JaimeArriagadaRosas/Plugin-Feedback-Canvas` — NO LICENCE FILE.** p319: 0 ★, 160 commits.
  LTI 1.3 + Canvas + AI-generated feedback behind mandatory instructor approval, Spanish docs,
  pre-production by its own account. The artefact this KB's North American patterns describe, and
  unusable. Ask the author.
- **`CaviraOSS/PageLM` — 2.0k ★ and NOT open source.** 234 commits, 277 forks; a genuinely
  capable study-material platform (contextual chat over PDF/DOCX/MD/TXT, Cornell SmartNotes,
  spaced-repetition flashcards, quizzes, AI podcasts, exam simulation, debate practice;
  Node/TS/LangChain/LangGraph + Vite/React; Gemini, OpenAI, Anthropic, Grok, MiniMax, Ollama,
  OpenRouter; Docker Compose; fully self-hostable). **Its licence is the "CaviraOSS Community
  Licence": free for personal and educational use, commercial use or resale requires prior written
  permission.** It is the highest-starred new education-AI project this pass and Globant cannot
  build a client deliverable on it. Read it as a feature checklist; do not plan on it.
- **`xiaoyang111222/cn-math-taxonomy` — CC BY-NC 4.0, and self-declared unreviewed.** 780 ★,
  188 forks, 11 commits. Exactly the artefact pattern P2 wants: 531 knowledge points (216 primary,
  315 junior-high), **909 prerequisite edges (788 hard, 121 soft)**, 2,271 questions, 230 curriculum
  standard entries, aligned to China's 2022 compulsory-education mathematics standards and the PEP
  textbook sequence, with a diagnostic engine, validation scripts and a static web UI. **Two
  disqualifiers:** NonCommercial rules out client work, and **the author states it is an
  AI-generated draft not reviewed by teachers**, with several textbook volumes third-party and
  unverified. 780 stars on an unreviewed generated knowledge graph that someone will put in front
  of children is this pass's clearest argument for reading the README to the end.
- **`aaryansamanta/ai-ethos` — NO LICENCE.** 499 ★, 0 forks, 27 commits; the website source for
  AI Ethos, Inc., a 501(c)(3) in Cupertino, CA providing AI tutoring to low-income, rural,
  multilingual and neurodiverse students across "7 languages". A real nonprofit and a creditable
  mission; the repository is a website with no licence and no platform code. Cite the programme,
  not the repo.
- **`jinanshm/ncert-mcp` — NO LICENCE, and the data problem is worse than the licence.** 1 ★,
  2 commits. 13 MCP tools over NCERT textbooks (lookup, semantic search with grade/subject/Bloom
  filters, curriculum map, prerequisites, learning path, question-paper generation) plus a REST
  API — the right shape. But **no data ships**: `bun run ingest` downloads the K-12 NCERT PDFs,
  chunks them and **tags the chunks with an LLM via OpenRouter, with no human verification
  described.** See the India gap below; this is the contrast case to Brazil's `bncc-dev` stack.
- **`luffycodes/Tutorbot-Spock` — NO LICENCE FILE.** 56 ★, 8 commits. Notable work (CLASS, EMNLP
  2023, arXiv 2305.13272; Pedagogical Alignment of LLMs, EMNLP 2024, arXiv 2402.05000).
  **Read the papers, not the repo.**
- **`CSOAI-ORG/coppa-ferpa-mcp` — MIT, but rejected in p317 and not revisited.** 1 ★, 16 commits,
  two contradictory price lists in one README. Compliance tooling is the last place to accept
  vendor self-description.
- **`artcc/freelingo` — AGPL-3.0, 188 ★.** A real self-hosted AI language-learning platform; it
  sits in `verticals/solutions.md` as a platform because AGPL puts it on the copyleft side of this
  KB's architectural line.
- **`AITutor-EvalKit` — no repository located.** The paper (arXiv 2512.03688, MBZUAI: Naeem, Maurya,
  Petukhova, Kochmar) describes a tool for evaluating the *pedagogical* quality of tutor responses
  in student-mistake remediation, which is exactly the eval layer this sector lacks. The authors
  call it an early research prototype and **no GitHub repository or licence could be found this
  pass.** Cite the paper as evidence that the eval problem is being worked; do not plan on the code.

## Licence split, recounted over 26

MIT (14 — FSRS4Anki, iblai/os, anki-mcp-server, Educhain, Bloom, OATutor, OpenTutor, tutor-mcp,
Study-Mate, instructional_agents, universal-examprep-skill, claudemy, algo-sensei, Claw-ED),
BSD-3-Clause (3 — nbgrader, otter-grader, Open TutorAI CE), Apache-2.0 (3 — DeepTutor, smolagents,
lineage-skill), **GPL-3.0 (3 — tutor-gpt, lumen, LTLTutor)**, dual MIT/AGPL-3.0 (1 —
human-skill-tree, skills only), CC0-1.0 (1 — gen-mentor), CC BY-SA 4.0 (1 — education-agent-skills).

**22 of 26 carry a permissive *software* licence Globant can build on commercially** (counting
human-skill-tree's skills half, and excluding its AGPL app). The exceptions are three copyleft
agents and two content/dedication licences, all flagged above.

**Pass 319 improved that ratio and the improvement is real but narrow:** six of the eight rows
added are MIT and one is Apache-2.0, and two of them — `lineage-skill` (Apache-2.0, 459 ★) and
`universal-examprep-skill` (MIT, 309 ★) — are the **first permissively licensed skill bundles at
scale**, which answers the legal half of trend 7. Last pass this KB said skill bundles arrive under
content licences and that the ShareAlike conversation was coming; it still is for
`education-agent-skills`, but it is no longer the only option on the shelf.

**The counter-movement is in the rejected list and it is the bigger story.** The three
highest-starred *new* projects read this pass are **PageLM (2.0k ★, bespoke "Community Licence")**,
**cn-math-taxonomy (780 ★, CC BY-NC 4.0)** and **advisingapp (340 ★, Elastic Licence 2.0 — see
`verticals/solutions.md`)**. None is open source. Popularity in this sector is drifting toward
source-available and NonCommercial terms, which is a procurement problem that looks like a
licensing footnote.

The structural fact holds and is now measured over 18: **the agent tier is predominantly permissive
and the platform tier in `verticals/solutions.md` is predominantly copyleft.** Pass 318 widened the
crack in it from the platform side again — see `openedx/openedx-ai-extensions` and the two new
AGPL AI-native LMS rows there — without changing the architectural advice.

## What was searched and not found

- **No *usably licensed* open source LTI 1.3 agent. Re-checked directly, and the count of
  unlicensed artefacts at this seam went from two to three** — `blamb/lti-tutor` (0 ★, 39 commits,
  "To be decided") and now `JaimeArriagadaRosas/Plugin-Feedback-Canvas` (0 ★, 160 commits, Canvas
  LTI 1.3 with instructor approval, Spanish docs, no LICENSE). `pylti1.3` (MIT, re-verified p319:
  138 ★, 84 forks, 178 commits, 39 open issues, **no published release**) is still the solid
  Python library; **`tsugiproject/tsugi` (Apache-2.0, 4,011 commits) is the newly recorded
  alternative** with an unresolved question about which LTI versions it implements
  (`repos/foundations.md`).
- ~~**No credible open source way to evaluate pedagogical quality.**~~ **RETIRED this pass.** Five
  passes declared it, pass 318 searched for `AITutor-EvalKit` and concluded "no repository located."
  **That was wrong: `kaushal0494/AITutor-EvalKit` exists, is MIT and is public** (3 ★, 8 commits,
  v1.0.0 on 1 Dec 2025). With MathTutorBench (EMNLP 2025), the two pre-registered audits and
  `bncc-dev/bncc-benchmark` (`repos/foundations.md`), the eval layer is a real and usable tier.
  **The lesson repeats pass 318's own: a declared gap must be re-tested with a changed query — the
  repo was found this pass by searching GitHub for the paper's tool name, which is exactly what the
  previous pass believed it had done.** Two 2026 benchmarks seen only in search snippets are
  **not** counted here and should be re-checked for a public repo and licence: **EduClaw-Bench**
  (arXiv 2608.03206; 30-day simulated learner, three-judge panel; code behind an anonymous review
  link) and **EduFair-Bench** (arXiv 2609.12949; pedagogical fairness across student demographics,
  judged by `gpt-oss-120b`).
- **No verified, machine-readable NCERT/CBSE curriculum dataset — NEW, and it is the most
  actionable gap in this KB.** India has the hardest curriculum mandate in the sector (AI +
  Computational Thinking compulsory for Classes 3–8 from 2026-27, 32,900 CBSE schools). GitHub's
  `ncert` (55 repos) and `cbse` (125 repos) topics were swept this pass: **nothing above 15 stars
  that is curriculum infrastructure.** The AI entries are one- and two-commit hobby projects —
  `praj2408/RAG-Enhanced-NCERT-Tutor` (MIT, 5 ★, 3 commits, Ollama + Chroma + Groq, and it
  **bundles Class 12 Physics textbook PDFs**, which is its own copyright question),
  `jinanshm/ncert-mcp` (unlicensed, LLM-tagged chunks, no verification),
  `thegauravmahto/sparks-ai-math-tutor` (2 ★, Hindi/English voice tutor on Gemini Live),
  `Sarika-stack23/Advanced-Mathematics-Assistant` (1 ★, RAG + SymPy), `dpaul0501/OpenVidya` (2 ★).
  The only substantial data asset is `deedy/cbse_schools_data` (52 ★) — a **2018** scrape of ~20,000
  schools. **Meanwhile Brazil has exactly this artefact, verified character-by-character and
  permissively licensed** (`bncc-dev`, `repos/foundations.md`). Porting that pattern to NCERT/CBSE
  is the clearest build-once opportunity this KB has identified — see pattern **P10**.
- **No credible open source agent for assessment integrity / AI-detection. Sixth consecutive pass.**
  The published evidence on AI-text detection accuracy continues to argue this should stay a gap.
- **No usable open source student-data-privacy compliance component — but the shape of the gap
  changed this pass and the change is the finding.** GitHub's `ferpa` topic now carries a *cluster*
  of governance repos that did not exist in earlier passes: `Principled-Evolution/gopal` (8 ★, Rego
  policies), `marc-shade/docsingest` (6 ★, PII/PHI ingestion with hash-chained audit),
  `chaz-clark/canvas-toolbox` (5 ★, FERPA-safe Canvas toolkit),
  `virtualryder/edu-ai-agents` (4 ★, Bedrock agents with PII masking),
  `ashutoshrana/regulated-ai-governance`, `ashutoshrana/enterprise-rag-patterns` and
  `ashutoshrana/voice-ai-governance` (1–2 ★ each), `Polycentric-Labs/regrails` (1 ★),
  `mizcausevic-dev/mcp-ai-tutor` (0 ★, an MCP server that audits tutors for FERPA/COPPA).
  **Every one is at or below 8 stars and nearly all were last updated in September or October
  2026.** Nothing here is a dependency. But a dozen independent authors starting the same component
  in the same two months is a market forming in real time, triggered by the COPPA deadline in
  `intel/market.md`. **Sixth pass declaring this gap, and the first pass able to say it is
  contested rather than empty — which shortens the window on the build-once opportunity.**
- **The regional picture moved in two places this pass.** **APAC authorship is now the largest
  bloc in the skill tier**, not a token presence: `Miaotofu01/Study-Mate` (MIT, 1.1k ★, 723
  commits, zh/en), `JuneYaooo/lineage-skill` (Apache-2.0, 459 ★, zh/en, acknowledging the Datawhale
  and LINUX DO communities), `ZeKaiNie/universal-examprep-skill` (MIT, 309 ★, en/zh),
  `24kchengYe/human-skill-tree` (573 ★) and the previously recorded `KeWang0622/kaogong-skill`
  (189 ★) and `SimonsTang/feifei-companion` (108 ★). **LATAM authorship appeared in the agent tier
  for the first time and it has no licence** — `Plugin-Feedback-Canvas`, above. And see
  `repos/foundations.md` for the pass's largest regional finding, which is Brazilian and is not an
  agent at all.
- **No region-specific tutoring agent as a product, still** — though the APAC skill-layer presence is now
  represented in the table by `human-skill-tree` (573 ★, bilingual EN/zh) alongside the previously
  recorded `Miaotofu01/Study-Mate` (1.1k ★), `KeWang0622/kaogong-skill` (189 ★) and
  `SimonsTang/feifei-companion` (108 ★). **The LATAM picture changed this pass, but in the platform
  tier, not here** — see `openedx/openedx-ai-extensions` in `verticals/solutions.md`.
