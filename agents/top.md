---
industry: education
region: Global
updated: 2026-10-10
---

# Education — AI agents shelf

**Pass 95, 2026-10-10.** ⏱️ **Fifth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; 94: 02:5x; this one 03:4x).

🔴 **The sandbox refuses to execute repository code for a THIRD consecutive pass** —
`grant-ladder-v4/ladder.sh --reach` denied before it started. 🟢 **So pass 95 wrote no classifier either**
(`P237`), ran the oracle map by hand and printed payloads instead of matching on them (`P970`).
**14 slugs resolved: 6 licence payload reads, 2 negative controls, 12 version reads, 4 release ladders, 2
registry-metadata reads.** Pass 92's 133-row census is **not** superseded (`P966`); every row not marked
🆕 p95 is carried at an earlier SHA and was **not** re-read this pass. **A `—` in the ★ column means not
read this pass. It never means zero** — and this pass it means **the GitHub API returned HTTP 403 for every
slug tried**, as it did for pass 94.

### 🟢 What pass 95 adds, in one line each

- 🔴 **`P980` — two unrelated projects, one name, incompatible grants.** A search summary said
  *"Otter-Autograder is GPL-3.0-or-later"*; the payload said BSD-3-Clause. **Both are true**:
  `otter-grader` 7.0.0 is [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
  (**BSD-3**) and `Otter-Autograder` 0.15.9 is
  [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) (**GPL-3.0**) — different orgs,
  different code, same problem domain. 🟢 **A tool is identified by its REPOSITORY; a distribution name is
  a hint, never an identity.**
- 🟢 **A permissive production autograder, new to this shelf** —
  [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (**BSD-3-Clause**, UC Berkeley,
  `v7.0.0`, Canvas + Gradescope). 🔵 **It does not close `Gap 372`** — it grades code against tests, not
  open responses. 🟢 **It closes a hole nobody had named**: the automated-feedback layer's only
  classroom-proven row was AGPL-3.0.
- 🔴 **`Gap 372` now has three MEASURED negatives instead of a shrug.** `GradeAid` is **CC BY-SA 4.0** (a
  content licence, carrying a ShareAlike term, applied to software); `RATASv1` and `emorynlp/llm-grading`
  have **no licence payload at all**. 🔴 **`P981`: "we publicly release our code" in a paper is not a
  grant** — and ungranted means all rights reserved.
- 🟢 **`eribean/girth_mcmc` discharged** — the lead pass 94 named and did not run. **MIT**, `0.6.0`, at
  **`LICENSE.txt`** while `LICENSE` is **404**. **Sixth row in the psychometric tier.**
- 🟢 **`P978` — the default branch reports the DEVELOPMENT version**, measured on four platforms rather
  than one. Sakai's root pom says `27-SNAPSHOT`; its newest tag is `25.2`. **Publish both, or publish a
  release nobody can install.**
- 🟢 **`P979` — the Maven `pom.xml` is a second licence oracle**, and Sakai's independently confirmed
  ECL-2.0 from a file read for an unrelated reason.
- 🟢 **Japan and Quebec both DISCHARGED**, each after two passes of returning nothing, and **neither by a
  new kind of query — by the method the previous pass had already written down.** See `intel/market.md`.
- 🟢 **Pakistan is a new jurisdiction and the FIRST higher-education mandate on this shelf** — an HEC
  notification making a 3-credit AI course compulsory in every UG and PG degree from session 2026.
- 🔴 **`Gap 376` — this KB's instrument has now been unrunnable longer than it was runnable.** The census
  denominator decays by ~12 hand-read rows per pass against a 133-row claim. **The first duty of the next
  pass that can execute code is corrective, not additive.**

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; this one 02:5x).

🔴 **The sandbox still will not execute repository code** — `grant-ladder-v4/ladder.sh` is refused before it
starts, for the second pass running. 🟢 **So pass 94 wrote no classifier either** (`P237`), ran the oracle
map by hand and **printed payload title blocks instead of matching on them** (`P970`). **12 slugs resolved:
9 licence payload reads at pinned SHAs, 1 negative control, 2 version-file reads.** Pass 92's 133-row census
is **not** superseded (`P966`); every row not marked 🆕 p94 is carried at an earlier SHA and was **not**
re-read this pass. **A `—` in the ★ column means not read this pass. It never means zero.**

### 🟢 What pass 94 adds, in one line each

- 🟢 **The scoring-*validation* layer, and it is permissive** — `rsmtool` (Apache-2.0, 2 916 commits) and
  `skll` (BSD-3) from **Educational Testing Service**, plus `NodeGrade` (MIT, LTI 1.1/1.3) for short
  answers. 🔵 **`Gap 372` is narrowed to the scorer**: the *evidence* a regulator asks for is open; the
  model is not. New tier below, costed as `P94-A`.
- 🔴 **One publisher, three grants** — ETS ships Apache-2.0, BSD-3 **and GPL-2.0** (`factor_analyzer`).
  `P975`: licence is a property of the repository, never of the publisher.
- 🟢 **`P974`: the clause probe, not the byte count, is the test for pass 93's `P971`.** `rsmtool` returns
  4 of 4 Apache clause headings; `AI_AWE` returns 0 of 4 — and an honest abridged copy (10 227 B) sits
  between them on size alone.
- 🟢 **`P972`/`P973`: platform versions are readable from the payload**, and the market leader is **5.3
  stable / 6.0dev alpha** while every blog read this pass said 5.2 — with `version.php` **not at the
  root**. `repos/foundations.md`, `verticals/solutions.md`, evidence in
  `compose/code/p972-platform-version-ladder/`.
- 🟢 **`Gap 370`'s failing path is resolved by hand**: `dados/LICENSE.md`, 676 B, HTTP 200 — and it carries
  a sovereignty clause no root licence could ([`repos/trending.md`](../repos/trending.md)).

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; this one
later the same day).

🔴 **This pass could not run the shelf's own instrument, and that is the first thing to say.**
`compose/code/grant-ladder-v4/ladder.sh` is committed and correct, but **this session's sandbox declines to
execute repository code.** 🔴 **The move that would have produced a clean-looking page — write a fresh
classifier — is the one `P237` forbids, and it is exactly what cost pass 91 two platform licences and one
client recommendation.** 🟢 **So pass 93 wrote no classifier.** It ran v4's oracle map by hand
(`git ls-remote --symref` → existence, ref, SHA; `raw.githubusercontent.com/<slug>/<SHA>/<name>` → payload)
and **printed each payload's title block instead of matching on it** — `P970`, stated in
`repos/foundations.md`.

**Consequence, stated plainly so no reader over-reads this page: 13 slugs were resolved this pass — 11
with a licence payload read at a pinned SHA, 1 negative, 1 invented control. Every other row on this page
is carried at its pass-92 SHA and was NOT re-read.** 🟢 Each new
row carries bytes, filename, ref and SHA so v4 can re-derive it mechanically next pass and contradict this
one on the record. **A `—` in the ★ column means not read this pass. It never means zero.**

🔵 **Marker convention, because three passes ran on one date.** A bare 🆕 is inherited from the pass that
added the row and was **not** re-flagged; **rows added by this pass are marked 🆕 p93.** Nothing on this
page silently changes its own provenance.

**Two-sided control.** 🟡 `moodle/moodle` → `COPYING.txt` **35 147 B** at `main` · `f205347` —
byte-identical to pass 92 **and at the same SHA**, so a re-read of the same object, **not** an independent
eleventh measurement; said rather than counted. 🟢 Invented slug → `ABSENT`. 🟢 And a free third-party
control: `OS4ED/openSIS-Classic` → 404 on `LICENSE`, `LICENSE.txt` **and** `LICENSE.md`, independently
reproducing a no-grant negative this KB already carried, with a different instrument.

### 🟢 What pass 93 adds, in one line each

- 🟢 **The psychometric layer** — BKT, IRT, CAT and spaced-repetition scheduling, **five permissive
  libraries whose seams their own READMEs name**. In `repos/foundations.md` Tier 2c; wired in `P93-A`.
- 🟢 **A national curriculum as verified open data** — Brazil's BNCC, MIT code + CC BY 4.0 data, with an
  MCP server. **The counter-example to the "frameworks are ungranted" shape** this shelf has carried for
  two passes. `repos/foundations.md` Tier 1b.
- 🟢 **A measured number for grounding**, which this KB has argued for 90 passes without one:
  **31.9 % → 0.2 %** hallucination. `intel/trends.md` `T11`.
- 🔴 **A blind spot in this KB's own licence reach**, proved on a real row and confirmed by a second,
  independent oracle. `P969` / `Gap 370`.

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
| 🆕 p93 [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant at the root** · `LICENSE` 1 299 B (index) · `main` · `ac9feb8` → **MIT** code (`packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests) + **CC BY 4.0** data | 9 | 🟢 **LATAM** (Brazil — the licence payload is in Portuguese and its attribution clause names **MEC/CNE**) | 🟢 **A national curriculum behind an MCP server.** `@bncc/mcp` 0.2.0 exposes **7 tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`) over **1 721 verified BNCC learning objectives**, **with the dataset embedded so queries run locally** — no network call per lookup, which is the property that matters in a school. 🔵 **Curriculum alignment stops being a prompt-engineering problem and becomes a tool call against data with per-record provenance.** 🟡 Pre-1.0 (npm `@bncc/dados` 0.3.1, PyPI `bncc` 0.2.0). |
| 🆕 p93 [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · `LICENSE` 1 218 B · `main` · `f94ca6a` | — | 🟡 **LATAM** (Brazil by subject matter — the payload's copyright line is a username, so the region is **not** `P800`-grade here and is labelled accordingly) | A **second, independent** MCP server over the BNCC skills, by a different author. 🔵 **n=2, so this is a shape rather than one project** — the same test pass 92 applied to MCP × SCORM. |
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
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🔴 **`MULTI-GRANT-FRAMEWORK`** · `LICENSE.md` 5 789 B · `main` · `65701e9` | 🔵 unplaced | A data layer for educational AI, tagged to academic standards. 🆕 🔴 **Its `LICENSE.md` grants NOTHING — it is a licensing *framework* document** (`P965`). It names *"Code … MIT"* and *"Open … CC BY 4.0 … CC0"*, and then the clause that governs: **"Gated — Not covered by an open license. Access requires Data Provider approval"**, and **"Gated content isn't yours to redistribute by default."** 🔴 **A classifier reading it returned `CC0-1.0` — the most permissive family the document merely mentions — for a payload whose operative term is the opposite.** Resolve the grant **per dataset and per download** in the catalogue before costing anything. |

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
| 🆕 [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | 🔴 **CC-BY-NC-SA-4.0** · `LICENSE.md` 1 891 B · `main` · `dd01b98` | — | 🔴 **Non-commercial.** Usable as reference, **not** in a paid deliverable. 🔵 Pass 91’s instrument misfired on this row (it recorded `Unlicense/PD`, and its committed TSV still does); re-derived correctly this pass — see `compose/code/grant-ladder-v4/README.md` (`P954`, `P966`). |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | **CC0-1.0** · 6 464 B · `main` · `d146ae6` | — | A list, not software, and public-domain dedicated — so quotable without attribution obligations. 🆕 🔵 **This row is also the payload that proved the shared classifier's CC0 branch was unreachable for canonical CC0 text** (`P962`) — pass 91's own results file recorded it as `OTHER/unclassified` while the shelf published `CC0-1.0`, found by hand. |
| 🆕 [`ai-builders-foundation/ai-builders-curriculum`](https://github.com/ai-builders-foundation/ai-builders-curriculum) | **MIT** · 1 079 B · `main` · `fe2da3d` | — | 🟢 **Vendor-neutral, 501(c)(3)-backed**, full-stack AI application curriculum with hackathon starter kits. The cleanest governance story in this tier — a foundation rather than a vendor, which matters for a public-sector procurement. 🔴 Adult/developer audience, like every other row here. |
| 🆕 [`fborrasumh/tutoria`](https://github.com/fborrasumh/tutoria) | **MIT** · 1 120 B · `main` · `65b2903` | — | 🟢 **EMEA** (Universidad Miguel Hernández de Elche, Spain — from the payload's copyright line). **Evidence-based tutor where the teacher VALIDATES the lesson before the student sees it**, then hints → diagnosis → check → review. 🔵 **The teacher-in-the-loop gate is the compliance-relevant primitive**: under the EU AI Act's Annex III, assessing learning outcomes is high-risk and needs human oversight, and this is that oversight expressed as a product step rather than a policy document. |

🔵 **Why this tier belongs on an *agents* shelf.** A mandated curriculum is the one education deliverable with
a legal deadline attached and no incumbent product, and the content layer is where a studio adds most value per
hour. 🔴 **The licence split matters sharply here**: curriculum is content, and content is where NC clauses
cluster. Three of the eight rows above are CC, and one of those forbids commercial use.

### 🔴 The framework every mandate points at is **ungranted** — and primary school is still empty

🔴 **`Gap 367` (no permissive AI curriculum for primary) STANDS, unchanged from pass 92.** Not re-queried
this pass; carried verbatim rather than re-asserted on no new evidence. A K-5-specific query returned
**no GitHub repository at all**; every permissive curriculum repo on this shelf is written for adult
developers. 🟢 The named non-GitHub alternative stands too: **MIT Day of AI** (`dayofai.org`,
**CC-licensed** — K-2 *"AI Foundations for Early Childhood"*, grades 3-5 *"How We Teach Machines"*) plus
Code.org's AI modules, both organised around the **AI4K12 Five Big Ideas** (Perception · Representation
and Reasoning · Learning · Natural Interaction · Societal Impact).

🔴 **And the finding that matters for a deliverable, also carried:** AI4K12 is the framework the K-12
guidance and India's CBSE curriculum align to, jointly sponsored by **AAAI and CSTA** — and its
repository, [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12), carries **no licence payload in
24 filenames** (`master` · `727b8bb`).

### 🟢 🆕 p93 But the *shape* of that gap is now refuted — by Brazil, and with better engineering than the framework it refutes

🔴 **What this shelf generalised from `ai4k12` and `learning-commons-org/knowledge-graph` was a rule:**
*reference frameworks and curriculum standards are authored by bodies that do not grant them, so a
studio can cite the structure but never ship it.* 🟢 **That rule is now false in at least one
jurisdiction, and the counter-example is not a near-miss — it is strictly better built than the artefact
it contradicts.**

**Brazil's *Base Nacional Comum Curricular* is published as verified open data at `bncc.dev`** (run by
Profy), licences read from the payload at pinned SHAs and tabled in `repos/foundations.md` **Tier 1b**:

| property | `touretzkyds/ai4k12` (AAAI/CSTA) | 🟢 `bncc-dev/bncc-dados` |
|---|---|---|
| grant | 🔴 **no payload in 24 filenames** | 🟢 **MIT** code · **CC BY 4.0** data (🟡 and see `P969` — the data grant is *not* at the root) |
| machine-readable | 🔴 no | 🟢 **JSON, SQLite, CSV — 1 721 learning objectives** |
| provenance | 🔴 none per item | 🟢 **per record**: `fonte` → spreadsheet row + official PDF page |
| verifiable against the official text | 🔴 not offered | 🟢 **1 576 of 1 580** BNCC-2018 texts match the MEC/CNE PDF **character for character**; the 4 mismatches are documented in `DECISOES.md`; **141 of 141** for the Computing supplement |
| reproducible | 🔴 — | 🟢 **CI re-runs the extraction pipeline on every change and rejects divergence** |
| agent-reachable | 🔴 — | 🟢 **MCP server, 7 tools, dataset embedded** (`bncc-dev/bncc-pacotes`, and an independent second one in `dfdb76/bncc-mcp`) |

🔵 **So the correct statement of the gap is narrower and more useful than the one this shelf carried:**
**it is not that curriculum standards are ungranted — it is that the *anglophone AI-curriculum* frameworks
are, while a national curriculum base in LATAM is available as audited open data.** 🔴 **And the method
that found it is the one this KB has now recorded five times: the query was in Portuguese.** `P870`.

🟡 **What it does not fix.** BNCC is **Brazil's** curriculum, not an AI-literacy framework — it does not
discharge `Gap 367`, which is about **K-5 AI instruction material**. 🔵 It refutes the generalisation, not
the gap. And the four other mandates (China MoE, Singapore MoE, India CBSE, EU Art. 4) still have no
comparable artefact — **recorded as `Gap 371`: does a BNCC-shaped open-data publication exist for any
other national curriculum?** The question is now worth asking precisely because one exists.

### 🆕 p93 Automated essay scoring — the regulated activity, and the thinnest supply on this shelf

🔵 **`T9` says the regulated activity is assessment.** A targeted search for permissive automated essay
scoring returned **one** candidate with a usable grant, and it is a research artefact, not a dependency:

| repo | grant (payload · bytes · ref · SHA) | ★ | region | read |
|---|---|---|---|---|
| 🆕 p93 [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) | 🟡 **Apache-2.0 *by reference*** · `LICENSE` **1 865 B** · `main` · `41ae3bd` | 2 | 🔵 unplaced | Qwen2.5-7B + LoRA discourse-move classifier plus a **LightGBM** scorer, over the **PERSUADE 2.0** corpus. 🔴 **Read the licence note below before costing it.** |

🔴 🆕 **`P971` — a LICENSE file can be the Apache *header notice* rather than the Apache *licence*.**
Canonical Apache-2.0 is **11 357 B** (measured on this shelf a dozen times). This payload is **1 865 B, 29
non-empty lines**, and it opens with the canonical title block — *"Apache License / Version 2.0, January
2004"* followed by *"Licensed under the Apache License, Version 2.0 … You may obtain a copy of the License
at http://www.apache.org/licenses/LICENSE-2.0"*. 🔴 **A grep of the payload for the clause headings
returns nothing: no "Grant of Patent License", no "Grant of Copyright License", no "Redistribution", no
"trademark", no "APPENDIX".**
🔵 **The grant is real — incorporation by reference works — but the terms are not in the repository.**
Practical consequences, both concrete: **(a)** a classifier matching the title block returns `Apache-2.0`
and is not wrong, so this defect is invisible to every instrument on this shelf; **(b)** the single
biggest reason to prefer Apache-2.0 over MIT is **§3, the express patent grant**, and **a deliverable that
vendors this repository ships none of that text** — if a procurement requires the licence text in the
bundle, you add it yourself.
🟡 **Independent of the licence, this is a 2★ research repo.** Its README does **not** use the name
*"ArguLens"* that its paper publishes it under, and the paper's headline **QWK 0.813** does not appear in
the README — a claim-versus-payload divergence of exactly the shape `compose/code/description-drift-audit/`
was built for. 🔵 **Shelve it as a reference for the architecture (classifier + gradient-boosted scorer,
not one end-to-end LLM), never as a dependency.**

🔴 **And the honest negative that goes with it.** The other AES repositories the same search surfaced are
**CC0-1.0 competition notebooks** (`kjgpta/Data-Augmentation-for-Automated-Essay-Scoring-using-Transformer-Models`,
`kjgpta/SHL-Automated-Essay-Scoring`) or carry no stated grant — **not resolved from the payload this pass
and therefore not tabled.** 🔵 **There is no production-grade permissive AES library in this industry.**
`Gap 372`. For the activity the EU AI Act names high-risk by name, that is the most consequential supply
gap on this shelf.

### 🟢 🆕 p94 The scoring-**validation** tier — `Gap 372` narrowed to the scorer, and the half that a regulator asks for is permissive

🔴 **What this shelf concluded one pass ago:** *"there is no production-grade permissive AES library in this
industry."* 🟢 **True of the scorer. False of the deliverable.** Under Annex III the obligation attached to
assessing learning outcomes is **evidence of validity and fairness, with an explanation owed to the person
assessed** — and that layer is Apache/BSD, has 2 916 commits, and is published by the house that runs TOEFL
and the GRE.

| repo | grant (payload · bytes · file · ref · SHA) | ★ | region | what it is |
|---|---|---|---|---|
| 🆕 p94 [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🟢 **Apache-2.0** · **11 358 B** · `LICENSE` · `main` · `a844f71` | 71 | 🟢 **North America** (Educational Testing Service) | 🟢 **2 916 commits.** Config-driven pipeline that builds and **evaluates** automated scoring models and emits a customisable HTML statistical report; scikit-learn + SHAP in the stack, `fairness` among its own topics, Python ≥ 3.8. 🔴 **Its README states it is *"not a scoring engine itself"*** — which is exactly why it is the row that matters. |
| 🆕 p94 [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** · 1 555 B · `LICENSE.txt` · `main` · `b350eb0` | — | 🟢 **North America** — `P800`-grade: *"Copyright (c) 2012–2022 Educational Testing Service"* | Runs scikit-learn experiments from configuration instead of code. `rsmtool` pins it at `skll==5.0.1`, so the pair is one dependency decision, not two. |
| 🆕 p94 [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 **MIT** · 1 062 B · `LICENSE` · `main` · `8e144ac` | 3 | 🟡 **EMEA** (Germany — by the ECSEE '25 citation and its authors; the payload's holder line reads only *"HASKI"*, so this is **not** `P800`-grade) | 🟢 **Short-answer grading built as a node graph, with LTI 1.1/1.3 and 421 commits.** NestJS + Prisma + Postgres, React/Vite PWA on litegraph.js, Python sentence-embedding worker, providers pluggable (**local**, OpenAI, OpenRouter, OpenAI-compatible), facilitator-run workshop mode. 🔵 **The only open-response grader on this shelf that already speaks the protocol an LMS speaks** — and 3★, which is why it is tabled with its commit count rather than its popularity. |

🔴 **Where the production AES code actually lives, measured this pass:**

| repo | payload | read |
|---|---|---|
| 🆕 p94 [`openedx/ease`](https://github.com/openedx/ease) | 🔴 **AGPL-3.0** · 35 136 B · `LICENSE.txt` · `master` · `056da0a` | edX's *Enhanced AI Scoring Engine* — the first place anyone looks, and network copyleft. |
| 🆕 p94 [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · 35 135 B · `LICENSE` · `master` · `1b7ae59` | Open Response Assessment: peer, self and staff assessment inside Open edX. Same grant. |

🔵 **So the engagement shape is a boundary, not a fork.** Score behind the AGPL service boundary (or buy the
score), **validate with Apache/BSD**, and keep the evidence pack as the client's own artefact. 🔴 **What is
still genuinely missing is one thing, precisely stated:** a permissive, production-grade **scorer** for
open-response work. That is the whole of `Gap 372` now.

#### 🔴 `P975` — one publisher, three grants, measured in a single sitting

| slug | payload | family |
|---|---|---|
| `EducationalTestingService/rsmtool` | 11 358 B · Apache title block · **4 of 4** clause headings | 🟢 Apache-2.0 |
| `EducationalTestingService/skll` | 1 555 B · *"New BSD License"* | 🟢 BSD-3-Clause |
| 🆕 p94 `EducationalTestingService/factor_analyzer` | 18 092 B · *"GNU GENERAL PUBLIC LICENSE / Version 2, June 1991"* · `main` · `de933d2` | 🔴 **GPL-2.0** |

🔴 **`factor_analyzer` is dependency-shaped** — exploratory and confirmatory factor analysis, the kind of
library a scoring pipeline imports without reading — **and it is GPL-2.0-only from the organisation whose
other two repositories are permissive.** 🔵 **A sophisticated publisher is not a licence guarantee.**
🟢 Negative control: `EducationalTestingService/rsmexplain`, named by a search summary, **does not resolve**
(`git ls-remote` exit 128).

#### 🟢 `P974` — the clause probe is the test; the byte count is only a smell

Pass 93's `P971` caught an Apache **header notice** masquerading as the Apache **licence** by its size
(1 865 B against 11 357 B). 🔴 **Size alone misjudges an honest abridged copy** — this shelf carries
`SimonsTang/feifei-companion` at 10 227 B, which is real. 🟢 **Probing for the four clause headings settles
it**: *Grant of Patent License* · *Grant of Copyright License* · *Redistribution* · *APPENDIX*.

| payload | bytes | clause headings present | reading |
|---|---|---|---|
| `rsmtool` `LICENSE` | 11 358 | 🟢 **4 of 4** | the licence |
| `wwrwbs/AI_AWE` `LICENSE` | 1 865 | 🔴 **0 of 4** | the notice, grant by reference only (`P971`) |

🔵 **And the clause that decides it is one of the four:** §3's express patent grant is the single strongest
reason to prefer Apache-2.0 over MIT, so a payload missing the heading is missing the reason.

#### 🟢 Two rows upgraded from the payload

- [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — **MIT** · 1 105 B · `main` · `939eb0e`; holder line
  *"Zachary A. Pardos (@zpardos) - CAHL research lab"* → 🟢 **region placed: North America** (`P800`),
  previously unplaced on this shelf. 🔵 **A `Gap 369` candidate in its own right**: Bayesian Knowledge
  Tracing **and** LTI in one MIT repository — a mastery estimate that can already reach an LMS.
- 🆕 p94 [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) — **MIT** · 1 072 B · `main` ·
  `09fdd67`; holder *"Ebrahim Mousavi"* → 🔵 unplaced. LangGraph tutoring loop (structured tutorials, Q&A,
  knowledge checks). 🟡 **Reference, not dependency**: no learner model, no LTI.

### 🟢 🆕 p95 The permissive autograder tier — and the registry collision that nearly cost it

🟢 **The automated-feedback layer had exactly one row with real classroom use, and it was AGPL-3.0**
(`mumuki/mumuki-laboratory`, LATAM). **There is now a BSD-3 option**, which moves the deliverable from
*integrate across a service boundary* to *fork and own*.

| repo | grant (payload · bytes · file · ref · SHA) | version | ★ | region | what it is |
|---|---|---|---|---|---|
| 🆕 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `LICENSE` · `master` · `190c1a4` | **7.0.0** | — | 🟢 **North America** (UC Berkeley Data Science Education Program) | 🟢 **Production autograder for Python scripts and Jupyter notebooks at course scale.** Parallel Docker grading, an Otter-managed grading VM, a student-side client for public checks, and **native Canvas and Gradescope support**. Zenodo DOI; CI and coverage live. |

🟢 **Three-layer licence agreement, which this shelf rarely gets to record.** The `LICENSE` payload says
BSD-3-Clause, `pyproject.toml` says `license = "BSD-3-Clause"`, and the PyPI classifier says
`License :: OSI Approved :: BSD License`. 🔵 **Payload, manifest and registry concur** — the opposite of
`P975` and `P342`, where they do not. 🟢 **And the default branch agrees with the tag ladder** (`7.0.0` =
`v7.0.0`), which under `P978` makes it the one platform-grade row on this shelf whose published version is
also the shippable one.

#### 🔴 `P980` — two unrelated projects, one name, incompatible grants

| what you cite | PyPI | repository | grant (payload · bytes · ref · SHA) |
|---|---|---|---|
| `otter-grader` | `otter-grader` **7.0.0** | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `master` · `190c1a4` |
| `Otter-Autograder` | `Otter-Autograder` **0.15.9** | [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🔴 **GPL-3.0** · 35 149 B · `main` · `2d9555f` |

🔴 **Different organisations, different repositories, different licences, seven major versions apart — and
both are autograders for programming coursework.** 🟢 **Resolving "the Otter autograder" by name picks
between them at random; resolving it by repository cannot.** This KB already holds
`p253-registry-first-identity` and `p791-registry-id-provenance`; **`P980` is the case where the registry
is itself the ambiguity**, and the only disambiguator is the `project_urls` → repository link.

🟡 **A second defect in the same reads, worth knowing before trusting any registry licence field.**
`Otter-Autograder`'s PyPI `license` field holds **the entire 35 kB GPL-3.0 text pasted into the metadata
field**, with `license_expression` set to `None`. 🔵 A consumer reading `info.license` for an SPDX id gets a
licence *document*; one reading its first 20 characters gets `"GNU GENERAL PUBLIC LI"`. **Prefer the
`classifiers` array — it was correct for both packages.**

#### 🔴 `Gap 372`'s three measured negatives — the open-response scorers that are not grants

| candidate | what the paper or index claims | what the payload says |
|---|---|---|
| [`edgresearch/code-automaticgrading-2022`](https://github.com/edgresearch/code-automaticgrading-2022) (**GradeAid**) | a published ASAG framework with released code | 🔴 **CC BY-SA 4.0** · 20 130 B · `LICENSE` · `master` · `309bb7e`. **A content licence, carrying a ShareAlike obligation, applied to software** — no patent or linking language, and Creative Commons itself advises against CC for code. **Unusable for a studio deliverable.** |
| [`datalab912/RATASv1`](https://github.com/datalab912/RATASv1) (rubric-based grading) | *"the authors publicly release all code on GitHub"* | 🔴 **No licence payload in 8 candidate filenames** · `main` · `04dd983` |
| [`emorynlp/llm-grading`](https://github.com/emorynlp/llm-grading) | *"an open-source auto-grading toolkit"* | 🔴 **No licence payload in 8 candidate filenames** · `master` · `b37150e` |

🔴 **`P981`: "we publicly release our code" in a paper is not a grant.** Two of these three are reachable,
populated and ungranted — which under copyright default is **all rights reserved**. 🔵 **The academic
sentence and the legal position point in opposite directions, and this industry's scoring supply is
largely academic**, so the defect is systematic rather than incidental.

### The agent *skill* as the unit of delivery

Carried from pass 90 and re-verified at the same SHAs. ~1 in 4 rows on `topics/ai-tutor` (🆕 p94 **665 repos** — 664 at pass 90, 664 at pass 93, so
flat for three passes; the churn is inside the existing population, not new entrants) is a **skill for an agent harness** rather than an application — markdown-plus-scripts
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
| 🆕 [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** · 1 069 B · `main` · `032b5aa` | — | **LATAM** (Colombia) | 🟢 **The strongest new LATAM row this pass, and the only one that is permissive end to end.** Autonomous virtual tutor agent for **rural higher education in Risaralda**, from Universidad Tecnológica de Pereira. 🟢 **It integrates with Open edX** — so it attaches to the platform tier this shelf already carries instead of replacing it. 🔵 **Region evidence is the payload's own copyright line** (`Grupo Sirius`), not an inference from the README (`P800`). 🟡 Depends on a hosted model API, which is the constraint to raise first with a public institution. |
| 🆕 p93 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · `dev` · `7e6caae` | 153 | 🟡 **LATAM** (Brazil) | 🟢 **The only computerized-adaptive-testing engine on this shelf, and the strongest LATAM row in the *psychometrics* tier** — item selection, ability estimation, stopping rules and a simulator, BSD-licensed, 877 commits. 🟡 **Region evidence is weaker than `P800`**: the payload's copyright line is a personal name, and Brazil comes from the project's own documentation host (`douglasrizzo.com.br`) linked throughout the README — labelled, not upgraded. 🟡 Default branch is `dev`. Tabled in `repos/foundations.md` **Tier 2c**. |
| 🆕 p93 [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **MIT at root / CC BY 4.0 for the data** · `LICENSE` 1 073 B · `main` · `daabd7d` | 20 | 🟢 **LATAM** (Brazil) | 🟢 **Brazil's national curriculum base as audited open data — 1 721 learning objectives, per-record provenance, 1 576/1 580 character-exact against the official MEC/CNE PDF.** 🔵 **The counter-example to this shelf's "frameworks are ungranted" rule**, and the anchor of `P93-B`. 🔴 **Read `P969` before costing it: the CC BY 4.0 data grant is NOT at the repo root.** |

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
- 🟢 **Learner models — `Gap 335` DISCHARGED after eight passes untouched.** The complaint stands for
  the *agents* on this shelf: only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma) carry an
  explicit learner model, and everything else relies on the context window, which is not a mastery
  estimate. 🟢 **But the missing layer exists and is MIT:**
  [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (**MIT**, 1 066 B, `77c3e90`,
  ~430★) — the reference deep-knowledge-tracing benchmark library, 7 datasets and a model zoo (DKT,
  DKVMN, SAKT, SAINT, AKT, GKT, LPKT). Shelved in `repos/foundations.md` **Tier 2b**.
  🔵 **It was found on the first query that named the TECHNIQUE instead of the industry** — `P955`
  holding for a second consecutive pass, now on a gap that had survived eight.
  🔴 **What remains open is composition, not availability:** nothing on this shelf wires a tracing
  model to an agent's turn, so `pykt-toolkit` → agent is a build, not an integration. See `Gap 369`.
  🟢 🆕 **p93 widens the available layer from one library to four techniques, and reverses the
  recommendation inside it.** `repos/foundations.md` **Tier 2c** now carries `CAHLR/pyBKT` (MIT, 282★,
  Bayesian Knowledge Tracing), `nd-ball/py-irt` (MIT, 173★, Bayesian IRT), `eribean/girth` (MIT, 126★,
  IRT estimation), `douglasrizzo/catsim` (**BSD-3-Clause**, 153★, the only **adaptive-testing engine** on
  this shelf) and `open-spaced-repetition/py-fsrs` (MIT, 506★, review scheduling).
  🔵 **And the ordering matters more than the count: for a deliverable, prefer the classical
  psychometrics over the deep model.** `catsim` has 877 commits and a BSD grant where `pykt-toolkit` is a
  research benchmark — but the deciding reason is regulatory, not maturity. Under Annex III, assessing
  learning outcomes is high-risk and owes an explanation; **an item-difficulty parameter and a per-skill
  mastery probability are explanations, and a trained network's activation is not.**
  🟢 **`Gap 369` is narrowed by `P93-A` in `compose/patterns.md`, which specifies the wiring — but no
  repository found this pass ships it, so it stays open.**

- 🟡 🆕 **p94: `Gap 372` is narrowed, not closed.** The missing thing is a permissive production-grade
  **scorer** for open-response work. 🟢 **The validation layer that a regulator actually asks for exists and
  is permissive** — `EducationalTestingService/rsmtool` (Apache-2.0, 2 916 commits) with
  `EducationalTestingService/skll` (BSD-3), plus `HASKI-RAK/NodeGrade` (MIT, LTI 1.1/1.3) for short answers.
  🔴 **And the production scoring code is copyleft**: `openedx/ease` and `openedx/edx-ora2` are both
  AGPL-3.0, read from the payload this pass. **Score behind a service boundary, validate with Apache/BSD.**
  See the scoring-validation tier above and `P94-A`.
- 🔴 🆕 **p95: `Gap 372` is unchanged in direction and three measurements stronger.** The three
  open-response candidates the literature names were probed and **all three fail**: `GradeAid` is
  **CC BY-SA 4.0**, `RATASv1` and `emorynlp/llm-grading` carry **no licence payload**. 🟢 **So the standing
  statement is now evidence-backed rather than asserted:** *the permissive supply for regulated
  open-response scoring is the **validation** layer (`rsmtool` Apache-2.0, `skll` BSD-3); the production
  scoring code is **copyleft** (`openedx/ease`, `openedx/edx-ora2`, AGPL-3.0); the research scoring code is
  **ungranted or CC-licensed**.* **Score behind a service boundary, validate with Apache/BSD.**
  🔵 **What pass 95 did add at this layer is adjacent, not the gap**: `ucbds-infra/otter-grader` (BSD-3)
  grades **code against tests**, which is a different assessment type from a constructed response.
- 🔴 🆕 **p95: `Gap 376` — this shelf's instrument has been unrunnable for three consecutive passes**, and
  that is the only item here getting worse rather than narrower. `grant-ladder-v4` carries ten registered
  corrections in a shared classifier and **has not executed since pass 92**; passes 93, 94 and 95 each
  hand-read ~12 rows against a published 133-row census. 🔴 **The decay is in the denominator, not the
  method.** 🟢 **The first duty of the next pass that can execute code is to re-derive the full census and
  disagree with these pages on the record** — every other item on this list is additive; this one is
  corrective.
- 🔴 🆕 **p93: this shelf cannot see a per-directory licence** (`P969` / `Gap 370`). A dataset repository
  can present MIT at the root while the data it exists to publish is CC BY 4.0 one directory down, and
  **both the 24-name ladder and GitHub's own sidebar return the root answer.** Proved on
  `bncc-dev/bncc-dados`; mechanism in `repos/foundations.md`.

*Prior pass content is preserved in git history at commit `306eb06` and earlier; it is not duplicated here.*
