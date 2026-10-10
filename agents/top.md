---
industry: education
region: Global
updated: 2026-10-10
---

# Education — AI agents shelf

**Pass 91, 2026-10-10.** Every row was resolved this pass with **`compose/code/grant-ladder-v3/ladder.sh`**:
existence and default branch from `git ls-remote --symref`, then the **licence read from the payload** at
`raw.githubusercontent.com/<slug>/<SHA>/<file>`, pinned to the resolved commit SHA — never from a badge, never
from a blog. **120 slugs resolved** (`compose/code/grant-ladder-v3/pass91-results.tsv`).
Two-sided control: four invented slugs returned `ABSENT`, and `moodle/moodle` returned `COPYING.txt` at
**35 147 B** on nine runs — byte-identical to the seven prior passes that measured it.

**🆕 The instrument changed this pass, and that changed two published numbers.** v2 probed **12** filenames
while six shelf rows claimed "17" and five more claimed "16". v3 probes **24** and prints the count on demand.
Re-measured over the same 92 slugs at the same SHAs: `NO-LICENCE-PAYLOAD` falls **6 → 5**, `AGPL-3.0` rises
**11 → 12**, and `OTHER/unclassified` falls **2 → 0** as ECL-2.0 becomes classifiable.
See `compose/code/grant-ladder-v3/README.md`. **A `—` in the ★ column means not read this pass. It never means zero.**

## The shelf

### Platform-grade AI (production, named deployments)

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `main` · `6cf793b` | 41k | **APAC** (HKU Data Science lab) | The reference agent-native tutoring workspace. Real agent loop with `web_search`/`rag`/`exec`/`consult_subagent` tools, MCP servers, **multi-engine RAG** (LlamaIndex, PageIndex, GraphRAG, LightRAG) and a **three-layer file-backed memory** (L1 traces → L2 summaries → L3 synthesis). An `ask_user` tool lets a turn pause for clarification — the pedagogically correct primitive. |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | **MIT** · 1 091 B · `develop` · `760e2e1` | 816 | **EMEA** (TU München, AET group) | A production university platform, MIT, with three named LLM subsystems: **Iris** (virtual tutor giving hints and leading questions), **Athena** (feedback suggestion for text, modelling and programming exercises) and **Hyperion** (AI-assisted exercise authoring on Spring AI). All optional and config-gated. The best starting point in this industry for a closable deliverable. |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD** · 1 531 B · `main` · `196c547` | ~107 | 🔵 unplaced | Permissive, peer-reviewed (arXiv 2602.07176), Ollama and OpenAI-compatible, **local RAG over course materials**. The BSD grant makes it the cleanest base for a closed client deliverable. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Selleo, Poland) | AI-native LMS; vendor documents an AI Mentor with Teacher / Mentor / Roleplay modes. 🟡 Open-core boundary still unverified (`Gap 362`) — stays out of every costed pattern. |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | **MIT** · 1 092 B · `main` · `38adb1e` | — | **APAC** (India) | Content and assessment generation from arbitrary sources; the long-standing generator row on this shelf. |

### Composable agents and protocol surface

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** · 1 074 B · `main` · `ed6774d` | 511 | 🔵 unplaced | Exposes Anki to any MCP client. **Spaced repetition becomes a tool call** — the cheapest way to give an agent durable retention mechanics instead of reimplementing them. |
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** · 1 073 B · `main` · `3708287` | 44 | 🔵 unplaced | Go MCP server that turns any LLM into an intelligent tutoring system. Model-agnostic by construction. |
| 🆕 [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) | **MIT** · 1 069 B · `main` · `bd14b95` | 8 | 🔵 unplaced | 🟢 **Self-hostable MCP server that assembles SCORM-compliant courses.** The interop spec becomes a tool call. |
| 🆕 [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** · 1 070 B · `main` · `fd5f110` | 6 | 🔵 unplaced | 🟢 Converts HTML exports **into** SCORM packages and **validates** SCORM zips. The second of its shape — see the note below. |
| [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | **Apache-2.0** · 11 386 B · `main` · `1b7fbe0` | 31 | 🔵 unplaced | Agentic RAG tutor built on LangGraph — a readable reference for the orchestration layer rather than a product. |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **MIT** · 1 094 B · `main` · `f88f69f` | 17 | 🔵 unplaced | Knowledge graph + local LLM + **Bayesian skill tracking**. One of very few rows carrying an explicit learner model rather than relying on prompt context. |

🆕 🟢 **New shape, n=2 not n=1: MCP × SCORM.** Two independent MIT servers now put *content packaging* behind
the Model Context Protocol — one authoring packages, one validating them. 🔵 **This matters more than either
repo's star count.** Every education engagement eventually has to get content into a platform the client
already runs; until this pass that was always build-it-yourself glue. Both are tiny and both are MIT, so they
are cheap to fork and audit. See `P91-C`.

### 🆕 The checker tier — and the gap this shelf declared for five passes is now **half closed**

🔴 **What the shelf said, in three files:** *"a targeted search for AI accessibility/alignment checkers in
education returned nothing usable"*, and *"the only accessibility checker found is `ucfopen/UDOIT` — GPL-3.0,
and not AI-driven."* 🟢 **The accessibility half of that is now FALSE.** Permissive, AI-driven WCAG checkers
exist, were found on the first targeted query, and verified from the payload:

| checker | grant (payload · bytes · ref · SHA) | region | scope |
|---|---|---|---|
| 🆕 [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) | **MIT** · 1 070 B · `main` · `1b095c2` | 🔵 unplaced | 🟢 **The best row in this tier.** WCAG 2.1/2.2 audit CLI **and** agent skill, with CI regression gates — and an **explicit manual-review boundary**: it states it cannot declare legal conformance from an automated pass. 🔵 **That refusal is the feature.** A checker that overclaims is a liability in a Section 508 dispute. |
| 🆕 [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents) | **MIT** · 1 069 B · `main` · `decf6ba` | 🔵 unplaced | Eleven WCAG 2.2 AA review agents for Claude Code and Copilot. Aimed at stopping AI coding tools **generating** inaccessible output — the preventive position rather than the audit one. |
| 🆕 [`9mtm/WCAG-Checker`](https://github.com/9mtm/WCAG-Checker) | **MIT** · 4 219 B · `main` · `d34decd` | 🟡 **EMEA** (publisher is an Austrian/German GmbH per the payload's copyright line) | Websites **and PDF files** — PDF matters, because course handouts are where institutional accessibility exposure actually lives. |
| 🆕 [`nsip/curriculum-mapper`](https://github.com/nsip/curriculum-mapper) | **Apache-2.0** · 11 357 B · `master` · `2b405d5` | 🟢 **APAC** (NSIP — National Schools Interoperability Program, Australia) | ML mapping **between curricula**. 🔴 **Archived and read-only**, and keyword-based rather than semantic. Read it as a spec for the problem, not a dependency. |
| 🆕 [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟡 **four-way split grant** · `LICENSE.md` 1 615 B · `main` · `59d2396` | 🔵 unplaced | LLM-as-a-judge scoring of generated text **against research-backed educational rubrics**, with expert-annotated corpora. 🔴 **Read the licence note below before costing it.** |
| 🆕 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🟡 code **MIT**, data **per-dataset** · `main` · `65701e9` | 🔵 unplaced | A data layer for educational AI, tagged to academic standards. 🔴 Licensing is **per dataset and per download** (`Open` / `Open + Gated` / `Gated`) through a platform catalogue. |

🔴 **The licence structure in this tier is the finding, not the repo list.** `learning-commons-org/evaluators`
ships **one** `LICENSE.md` granting **four different things**: code **MIT**, prompts and settings
**CC-BY-4.0**, and the Annotated CLEAR Corpus and Annotated PERSUADE 2.0 Corpus **CC-BY-NC-SA-4.0**.
🔴 **The non-commercial clause sits on the corpora — which are the part that makes it an evidence-backed
evaluator rather than a prompt.** 🔵 **So the question in the checker tier is not "is it permissive" but
"is the permissive part the valuable part".** Here it is not. The code and prompts are usable in a paid
deliverable; the annotated corpora are not, and a studio must bring or buy its own.

🔴 **Four checker candidates have NO grant at all** (24 filenames each) and one of them is published as MIT:

| row | what is claimed | what the payload says |
|---|---|---|
| [`qed42/ai-accessibility-checker`](https://github.com/qed42/ai-accessibility-checker) | 🔴 a search summary states plainly *"It is MIT-licensed"* | 🔴 **No licence payload in 24 filenames** · `main` · `5716afc`. The most capable-looking row in the tier — Python CLI **plus** GitHub Action, WCAG 2.0–2.2 A/AA/AAA — and **unusable**. |
| [`albertomf1979/wcag-accessibility-agent`](https://github.com/albertomf1979/wcag-accessibility-agent) | WCAG 2.1 agent with CLI and PDF/DOCX export | 🔴 **No licence payload in 24 filenames** · `main` · `472c6bb` |
| [`Zion-support/curriculum-alignment-checker`](https://github.com/Zion-support/curriculum-alignment-checker) | checks materials against standards, flags gaps | 🔴 **No licence payload in 24 filenames** · `main` · `c148b67`. Self-describes as batch-generated app-network content. |
| [`lovejzzz/CourseMapper`](https://github.com/lovejzzz/CourseMapper) | course mapping with browser-local AI | 🔴 **No licence payload in 24 filenames** · `main` · `63d8172`. Its own README logs source-attribution and answer-quality failures. |

🔵 **What is still genuinely missing, stated narrowly.** 🟢 The **accessibility** checker gap is closed —
permissive, AI-driven, and three independent rows. 🔴 **The instructional-alignment checker gap stands.**
Nothing found audits whether content actually meets a learning outcome under a permissive grant with usable
evidence: `nsip/curriculum-mapper` is archived and keyword-based, `evaluators`' corpora are NC, and the two
alignment-named repos carry no grant. **That is the build, and it is now a sharper specification than
"checkers barely exist".**

### 🆕 The AI-literacy tier — because literacy is now a statutory duty, not a nice-to-have

🟢 **Four jurisdictions now *mandate* AI instruction rather than regulate AI systems** (see `intel/trends.md`
`T7`): China's MoE (≥8 h/year from age six), Singapore's MoE (March 2026), India's CBSE (Classes 3–8 from
2026-27) and the EU AI Act's **Article 4 staff AI-literacy duty — which is already in force and was NOT
deferred to December 2027 with the high-risk obligations.** Someone has to write, localise and assess that
curriculum. These are the permissive starting points, all verified from the payload this pass:

| curriculum repo | grant (payload · bytes · ref · SHA) | ★ | note |
|---|---|---|---|
| 🆕 [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | **MIT** · 1 141 B · `main` · `ff2ba66` | ~67k (search-reported) | Twelve lessons on building AI agents. The largest permissive AI curriculum found; vendor-backed and translated. |
| 🆕 [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** · 1 070 B · `main` · `b6a7a17` | — | 🟢 **Reached #1 on GitHub Trending on 24 May 2026** (Trendshift). Build-it-yourself AI engineering. |
| 🆕 [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | **MIT** · 1 091 B · `main` · `da3f9df` | ~796 (search-reported) | Agents from first principles **against a local LLM** — the right shape where student data cannot leave the building. |
| 🆕 [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | 🔴 **CC-BY-NC-SA-4.0** · `LICENSE.md` 1 891 B · `main` · `dd01b98` | — | 🔴 **Non-commercial.** Usable as reference, **not** in a paid deliverable. 🔵 This row is also where this pass's own instrument misfired — see `compose/code/grant-ladder-v3/README.md`. |
| 🆕 [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | **CC0-1.0** · 6 464 B · `main` · `d146ae6` | — | A list, not software, and public-domain dedicated — so quotable without attribution obligations. |

🔵 **Why this tier belongs on an *agents* shelf.** A mandated curriculum is the one education deliverable with
a legal deadline attached and no incumbent product, and the content layer is where a studio adds most value per
hour. 🔴 **The licence split matters sharply here**: curriculum is content, and content is where NC clauses
cluster. Two of the five rows above are CC, and one of those forbids commercial use.

### The agent *skill* as the unit of delivery

Carried from pass 90 and re-verified at the same SHAs. ~1 in 4 rows on `topics/ai-tutor` (**664 repos**, total
unchanged from pass 90) is a **skill for an agent harness** rather than an application — markdown-plus-scripts
with no UI, no hosting and no database, and overwhelmingly MIT.

| skill | grant (payload · bytes · ref · SHA) | ★ | region | scope |
|---|---|---|---|---|
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | **MIT** · 1 064 B · `main` · `2cd8393` | 772 | 🔵 unplaced | Self-study agent: plans learning paths, explains concepts, guides projects |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | **MIT** · 1 065 B · `main` · `b9e84f5` | 303 | 🔵 unplaced | Slide-based teaching with page citations, **cross-session memory** |
| [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) | **MIT** · 1 081 B · `main` · `25ea970` | 286 | 🔵 unplaced | DSA mentor with progressive hints and mock interviews |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | **MIT** · 1 069 B · `main` · `b391898` | 285 | 🔵 unplaced | Adaptive tutor built on **Bloom's 2-sigma** research; self-hostable *and* a skill |
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | **MIT** · 1 102 B · `main` · `075c189` | 242 | 🔵 unplaced | **Diagnosis-first** tutoring for STEM/CS — assesses before teaching |
| [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | **MIT** · 1 083 B · `main` · `c85ca76` | 166 | **APAC** (China, civil-service exams) | Jurisdiction-specific exam coaching |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** · 1 068 B · `main` · `f0142f2` | 137 | 🔵 unplaced | **Local-first**; notes, quizzes, flashcards from uploaded material |
| 🆕 [`PrepLabsAI/InterviewMentor`](https://github.com/PrepLabsAI/InterviewMentor) | **MIT** · 1 071 B · `main` · `609d311` | 112 | 🔵 unplaced | AI mock interviews for technical hiring — the corporate-reskilling adjacency |
| 🆕 [`SimonsTang/feifei-companion`](https://github.com/SimonsTang/feifei-companion) | 🟡 **Apache-2.0 variant** · 10 227 B · `main` · `c9c6295` | 106 | **APAC** (China) | K-12 AI education companion. 🟡 **10 227 B is not canonical Apache-2.0 (11 357 B)** — an abridged copy; read it before relying on the patent clause. |
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | **MIT** · 1 068 B · `main` · `b4c9352` | 107 | 🔵 unplaced | A *collection* of teaching/study skills — the bundle pattern |
| 🆕 [`codeXsidd/Studivexa`](https://github.com/codeXsidd/Studivexa) | **MIT** · 1 068 B · `main` · `6ac2799` | 72 | 🔵 unplaced | Student productivity workspace |

### LATAM

Placed rows, not a gap. 🟢 **Every one was found by querying in Portuguese or Spanish** — confirmed again this
pass as the single highest-yield move for this region.

| row | grant (payload · bytes · ref · SHA) | ★ | region | note |
|---|---|---|---|---|
| [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) | **MIT** · 1 085 B · `main` · `bbeea5a` | — | **LATAM** (Brazil, pt-BR) | Interactive pt-BR platform, **205 modules**, AI tutor "Nilo" with optional OpenAI-compatible LLM and an **offline local fallback**; React + FastAPI + SQLite. MIT end to end. |
| 🆕 [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | 🔴 **AGPL-3.0** · 34 523 B · `master` · `fce1ede` | 199 | **LATAM** (Argentina) | 🟢 **Student programming practice with automated feedback** — a real, long-running Argentine autograding platform used in schools and universities. 🔴 AGPL: network copyleft, so integrate, do not absorb. **The strongest LATAM row in the assessment tier.** |
| [`programadores-obreros/Agente-editor-inet`](https://github.com/programadores-obreros/Agente-editor-inet) | 🔴 **GPL-3.0** · 35 149 B · `main` · `0fa7298` | — | **LATAM** (Argentina, INET) | Teaching agent for Arduino/ESP32 in Argentine technical schools; runs **offline, double-click**. Pedagogically excellent, 🔴 copyleft. |

## Negatives and licence flags — read before you quote a blog

Each re-read from the payload this pass. 🟢 Four rows advanced their HEAD since pass 90 and **kept their
grant** — `LAION-AI/Desktop_BUD-E` → `13ba697`, `ahmedEid1/lumen` → `07635d3`, `artcc/freelingo` → `ce978cf`,
`yh2072/edgameclaw` → `4d92b73`. Activity without licence drift is the normal case; it is worth measuring
because this shelf pins SHAs.

| row | what is widely claimed | what the payload says |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 a widely-cited LMS comparison lists it as **MIT** | 🔴 **AGPL-3.0**, `license.txt` (lowercase), 33 893 B, `develop` · `933fc60`. 🆕 **And this row is why v3 exists**: v2 never probed `license.txt` and recorded it as *no grant*. Now resolved automatically. |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | listed in roundups as a permissive open tutor | 🔴 **GPL-3.0**, 35 149 B, `main` · `5c2f924` |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | "MIT" | 🟡 **Split grant, now detected mechanically** by `ladder.sh --all`: `LICENSE` = **CC-BY-4.0** (18 650 B), `LICENSE-CODE` = **MIT** (1 141 B). 🔴 **A first-match read returns CC-BY — the wrong answer for anyone shipping the code.** Cite the file. |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 567★, prominent on `topics/ai-tutor` | 🔴 **AGPL-3.0** (1 134 B — a short-form AGPL grant, unusual) |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | self-hosted language tutor, 164★ | 🔴 **AGPL-3.0**. Self-hosting does not imply a permissive grant. |
| [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | learner-owned AI education platform, 88★ | 🔴 **GPL-3.0** |
| [`yh2072/edgameclaw`](https://github.com/yh2072/edgameclaw) | material → game-based course, 71★ | 🔴 **AGPL-3.0** |
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 62★, six specialised agents | 🔴 **No licence payload in 24 filenames** (was 12 — the negative is now twice as strong) |
| [`LAION-AI/Desktop_BUD-E`](https://github.com/LAION-AI/Desktop_BUD-E) | LAION educational voice assistant, 43★ | 🔴 **No licence payload in 24 filenames** |
| 🆕 [`mahseema/aibooks`](https://github.com/mahseema/aibooks) | 91★ curated AI/ML book list on `topics/ai-tutor` | 🔴 **No licence payload in 24 filenames** · `master` · `0d71402` |

🟢 **The standing rate, re-measured with the corrected instrument: 5 of the 92 established slugs carry no
licence payload — ~1 in 18, not pass 90's ~1 in 15.** 🔵 **The change is an instrument correction, not a
change in the world**: `frappe/lms` was never ungranted, it was unreachable by a 12-name probe. Pass 87's
much worse 1-in-3 figure was measured on *fresh* `ai-tutor` rows rather than established ones and is not
withdrawn — the sampling difference remains the explanation.

## What this shelf still does not have

- 🔴 **An instructional-alignment checker.** Narrowed, not closed — see the checker tier above. The
  accessibility half is done; outcome alignment has no permissive row with usable evidence.
- 🔵 **Region placement.** 20 rows above are honestly **unplaced** — the publisher's country could not be
  established from the repo this pass. Recorded rather than guessed.
- 🔵 **Learner models.** Only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma) carry an explicit
  learner model. Everything else relies on the context window, which is not a mastery estimate.
  🔴 **`Gap 335` (knowledge tracing) is untouched for an eighth pass** and is named here rather than carried quietly.

*Prior pass content is preserved in git history at commit `306eb06` and earlier; it is not duplicated here.*
