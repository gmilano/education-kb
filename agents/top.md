---
industry: education
region: Global
updated: 2026-10-19
---
# Top open source AI agents — education

## Pass 325 · 2026-10-19 (eleventh pass of this date) — the sweep measured this KB's own coverage, and the nine-pass LTI gap stopped being an absence

**Twenty-five repositories were put through a three-axis supply sweep. Twenty were already held.**
Nine new slugs were added across this KB — **every licence read first-hand this pass** — and
**not one of them is above 14 ★**. 🔵 **That ratio is the pass's first finding and it is a
statement about this base, not about the sector:** a fresh broad sweep at this KB's depth now
returns **36% novelty and 0% above 14 ★**. The `intelligent-tutoring-system` axis census, the whole
**France Université Numérique** stack and every artefact the fresh-push window returned were
already on these shelves. **Discovery is no longer where the margin is in this industry; composition
is.** The rows are in `repos/foundations.md`, the sweep itself in `agents/trending.md`.

🟢 **The pass's main finding upgrades the longest-standing gap in this file from *absent* to
*diagnosed*, and it is the first positive evidence trend 6 has ever had.** Nine passes have
recorded *no LTI 1.3 AI agent*. This pass tested it on a **third instrument, GitHub code search,
new to this KB** — `lti_1p3 mcp server tutor language:python` → **0**;
`"pylti1p3" OR "ltijs" mcp agent tutor` → **6 hits, none an agent.** But the diagnosis came from
the supply side: **`openfun/django-lti-toolbox` — MIT, 14 ★, 34 commits, *"a Django application to
build LTI Tool Providers"*, no release, and last pushed `2024-11-14`, roughly twenty-three months
untouched.** The permissive LTI plumbing **exists, is published by a national public operator, and
is being left to rot** while the same operator's MCP-era peers ship weekly and its own analytics UI
(`openfun/warren`) still renders *inside an LTI iframe*. 🔵 **The gap is not missing libraries. It
is agent-side adoption of a working, permissive, unmaintained standard** — which is a different
sentence to put in front of a client, and a cheaper one to act on.

🔴 **The second finding is a method failure caught on this pass itself, and it refines p324's
declared-gap discount.** This pass searched `special education IEP AI assistant pushed:>2026-01-01
stars:>3` → **0 results**, then `IEP individualized education program generator LLM` → **0
results**, and was one step from declaring a special-education gap. **This KB already holds
`iblai/k-12-agents` — an MIT `special-education-agent` grounded in IDEA 2004, the thirteen
disability categories and §504 — recorded at p288 as the correction of exactly that claim.** The
search *terms* were fine. **`stars:>3` and `pushed:>2026-01-01` removed it.** 🔵 **Record the
sharper rule: p324 said a declared gap is a statement about the query. It is narrower than that —
a gap declared behind a star or recency filter is a statement about the filter.** The highest-stakes
tier in this sector is the one most likely to be published by an institution at two stars.

🔴 **And an instrument caveat that will only get worse: the code-search channel now returns this
KB's own files.** Two of the six hits for the LTI probe were
`gmilano/education-kb/archive/2026-10-19-p315-pre-rewrite/repos-foundations.md` and
`gmilano/education-kb/compose/code/p436-fork-hypothesis/homepage.2026-10-07.tsv`. **This base is now
part of the corpus it searches.** Every future novelty count on this channel must exclude
`gmilano/*` or it will score its own history as supply.

### Added to the table

- **`dymchenkko/claude-study-agent` — MIT, 2 ★, created 2026-10-10.** The **fresh-push window's only
  substantial artefact**: a university study agent that takes *the learner's own* slides, PDFs and
  **lecture recordings** (Whisper), OCRs them, indexes them for semantic search, then quizzes with
  spaced repetition, tracks mistakes and builds mock exams. Local-first, no external vector store.
  It is `universal-examprep-skill`'s shape with the **recording** leg added — the first artefact here
  to treat the lecture itself as ingestible learner-owned corpus.

### Added to the evaluation table

- **`Kyyota-Wang/cloverailab` — 🔴 NO LICENCE, 0 ★.** GRE Analytical Writing reviewer and writer
  agents: **LLM-as-judge against the published ETS rubric with officially scored anchors, no
  fine-tuning, QWK 0.825**, harness and results committed. 🔵 **It is the second artefact in this
  tier to publish a real agreement figure and the second that cannot be used** — `EduGuardBench`
  (p323) was the first. **The eval tier's measured edge keeps arriving without a grant.**

### Recorded below the listing bar

- **`wildcat430524/Steps2Great-skill` — MIT, 2 ★, zh/en.** A Socratic **mastery-learning** Agent
  Skill that will not advance until a **three-dimension assessment is all-green** — the gate from
  `leap-framework`'s State Guard expressed as a prompt contract instead of a server. APAC-authored,
  consistent with trend 7.
- **`010Ankushsharma/AdaptaLearn` — 🔴 NO LICENCE, 0 ★.** DKVMN knowledge tracing + PPO, with a
  claim of training on **131M+ interactions**. Recorded, **not** recommended: the claim is
  unverifiable from the repository and there is no grant.


## Pass 324 · 2026-10-19 (tenth pass of this date) — the seven-pass integrity gap was a query artefact, and it is closed

**One row added here, one to the evaluation table, ten to `repos/foundations.md` (now forty-eight),
all six of p322's named-unread `openeduhub` repositories measured. Fourteen repositories measured
first-hand.**

🟢 **The pass's finding: `intel/trends.md` trend 9's premise — *"there is still no credible open
source AI-detection or academic-integrity project"*, declared for seven consecutive passes — is
false, and the query was what was wrong.** The sweeps behind it searched *AI detection* and
*AI-detection agent*. Searching the GitHub topic **`plagiarism-detection`** instead returns twelve
repositories pushed since 2026-01-01 above ten stars, and three are substantial: **`sunilgentyala/
aegis-integrity`** (MIT, 17 ★, **an academic-integrity MCP server with seven tools**),
**`NoplagLabs/noplag-engine`** (Apache-2.0, 86 ★, winnowing over PostgreSQL) and **`jplag/JPlag`**
(GPL-3.0, **2.0k ★, 5,708 commits**, twenty-odd languages, Java API or CLI). 🔵 **Trend 9's
*conclusion* survives and is strengthened** — `aegis-integrity`'s README is the most careful
statement of the human-in-the-loop posture this KB has read from a tool that could have
overclaimed, and it publishes no accuracy figure for itself. **The premise was false; the
recommendation was right.** Full detail and the two cautions in `agents/trending.md`; the engines in
`repos/foundations.md`; the wiring in `compose/patterns.md` **P11**.

🔴 **Fourth consecutive instance of this KB's most reliable method finding.** p318 → tool name;
p322 → topic sweep; p323 → changed query, two curriculum artefacts; **p324 → changed query, a
seven-pass gap overturned.** A declared gap is a statement about the query, not about the world.

🔴 **The other finding is a licence contradiction running the opposite way to every one before it.**
`ZhijieXiong/pyedmine` (82 ★, 220 commits, the broadest educational-data-mining library this KB has
measured) ships **the MIT text in `LICENSE` — under `Copyright (c) 2023 Stanford Future Data
Systems`, an unrelated holder — while its README says *"All data and code in this project may be
used only for academic purposes."*** Every previous instance in this KB was a README claiming a
grant the repository did not carry; **this is the documented grant being narrower than the licensed
one, which is the direction dependency scanners do not catch.** Treat it as academic-use-only.
`repos/foundations.md` has the full row.

🟢 **Instrument change, stated because every number in this pass depends on it: the GitHub REST
search API is reachable in this session** via the MCP `search_repositories` tool, where earlier
cycles recorded it blocked. Star, fork, push-date, archived and topic values here are structured
API values, not readings off a rendered page — **and the supply tail p323 measured was reproduced
exactly on this second instrument** (six repositories, ceiling 41 ★). 🔴 `get_file_contents` is
refused — credentials are scoped to one repository — and **`curl` to `github.com` returns `403`
through this session's proxy**, so file-level verification ran through `raw.githubusercontent.com`
and the rendered page. 🔴 **And a probe caveat that nearly produced right verdicts for wrong
reasons: the `openeduhub` ITS tier writes `README.org`, not `README.md`, so a Markdown-shaped 404
probe 404s on every repository in the org.** Licence verdicts below were taken over **seven
candidate filenames** and corroborated against the rendered sidebar. Both characterised in
`repos/trending.md`.

### Added to the table

- **`sunilgentyala/aegis-integrity` — MIT, 17 ★, 5 forks, 68 commits, changelog at v3.3.2.** The
  first integrity artefact in this file, and the **second MCP-exposed agent** in it — which is
  further evidence for trend 6: an integrity reviewer built in 2026 ships **seven MCP tools and no
  LTI surface at all.**

### Added to the evaluation table

- **`yjo2lee/knowsim` — MIT, 4 ★.** arXiv 2608.17150. It is **the simulated learner, not the
  tutor**: a knowledge-state-aware user simulator for measuring whether an assistant's confidence
  tracks what the learner actually knows. The only calibration-focused artefact in this KB.

### The standing LTI gap — eighth pass, and now the first gap here to survive a changed instrument

Three changed queries on the new instrument: `topic:lti topic:ai` → **2 results**, neither an agent
(a profile README, and a third-party API profile of the **commercial** Packback "Originality");
`lti 1.3 mcp server education stars:>0` → **0**; `topic:lti lti-1-3 OR lti1p3 OR lti-advantage ai
agent` → **0**. 🔵 **Every other gap this KB declared and then re-tested with a changed query has
fallen. This one has not** — which is the first positive evidence that it is a property of the
sector rather than of the search.

## Pass 323 · 2026-10-19 (ninth pass of this date) — two new rows, one unlicensed benchmark, and a trend headline retracted

**Two rows added here, one to the evaluation table, three to `repos/foundations.md`, four
repositories recorded below the listing bar, two named gaps from p322 executed and still empty, and
one open question from p319 closed with a negative answer.** Nine repositories read first-hand.

**The pass's finding is not in this file.** `haolpku/K12-KGraph` — 420 ★, 67 forks, **NeurIPS 2026
Evaluations & Datasets Track**, China's PEP K-12 curriculum as an evidence-linked knowledge graph
with 12 expert annotators at Fleiss' κ = 0.84 — **makes `intel/trends.md` trend 12's headline
("exactly one country has built it") wrong.** Two countries have. **Exactly one licensed the data
for commercial use:** K12-KGraph splits *"Code (this repository): MIT"* from *"Dataset (graph,
benchmark, training data): CC BY-NC-SA 4.0."* Full read in `repos/foundations.md`.

**The licence shape is new and it pairs with p322's.** p322 found licences dividing **by
architectural layer** inside one organisation — permissive shells, GPL analysers, unlicensed
inference core. This pass found licences dividing **by artefact type** inside one repository —
permissive code, NonCommercial data. **Both are the same sentence: permissive at the edges,
restricted at the thing that actually took the work.** In Germany it was the inference core; in
China it is the curriculum. A studio that reads only the sidebar badge gets both wrong.

### The method lesson, and this is its third consecutive instance

p318 declared `AITutor-EvalKit` nonexistent; p322 found it by searching the paper's tool name and
wrote down the lesson. **p322 then swept the `ncert` and `cbse` topics — 180 repositories — and
declared "no verified curriculum dataset at all."** This pass changed the query to *curriculum
knowledge graph / prerequisite* and found two artefacts the topic sweep could not see, one of them
the largest in this KB. **A topic sweep is a query, not a census, and a declared gap must be
re-tested with a changed query — which is now the third time this file has had to say so.**

### What is new in the table

- **`zhangl1001/civil-ai` (MIT, 41 ★, 100 commits)** — **the highest-starred education agent pushed
  since 2026-10-01**, and a *foundation* rather than an app by its own careful statement. Local-first
  on iOS and Web, storage behind repository ports, an agent runtime with checkpoints, leases,
  cancellation and recovery, and an evidence-based capability model with mastery projection. **It
  volunteers its own weakness** — domain portability unvalidated, both bundled packages exam-style.
  APAC-authored.
- **`ibenian/algebench` (MIT, 8 ★, 519 commits)** — an **interruptible** 3D maths narrator: stop the
  scene, ask why, watch the visualisation answer. Gemini-only BYOK keeps it out of the dependency
  tier. **519 commits at 8 stars is the second measured instance of this file's p320 lesson that a
  star count is not a volume measure.**

### The eval tier gained its first in-proceedings artefact, and it has no licence

**`YL1N/EduGuardBench` — 🔴 NO LICENCE, 5 ★, 2 commits — arXiv 2511.06890, AAAI proceedings
(article 40399).** Role-playing Fidelity Score for teacher-simulation fidelity; persona-based
adversarial prompts for academic misconduct scored by Attack Success Rate and a three-tier refusal
assessment; 14 models. **Two results worth a bid slide:** the safest models convert harmful requests
into teachable moments via *Educational Refusals*, a capacity **strongly negatively correlated with
ASR** — safety and pedagogy pulling the same direction for once — and a **scaling paradox** in which
mid-sized models are the most vulnerable, so "bigger is safer" is false in this domain. **It ships
its two datasets as `.xlsx`, its scripts, a notebook and an appendix PDF, with empty `Results/`
folders — and no LICENSE file.**

**The correction this forces on p322, stated narrowly.** One pass ago this file retired the
five-pass gap *"no credible open source way to evaluate pedagogical quality"* and called the eval
layer **"a real and usable tier."** That stands — MathTutorBench, AITutor-EvalKit and the two
pre-registered audits are all still there and all still usable. **But the tier's newest entrant, and
the only one published in conference proceedings rather than on arXiv alone, cannot be used.** The
tier is real; its peer-reviewed edge is not yet licensed. **And of the four 2026 education
benchmarks this pass touched — EduGuardBench, EduClaw-Bench, EduFair-Bench, ELBench — one has code
without a licence and three have no code at all.** That is the actual state of educational-AI
evaluation in late 2026: the papers are arriving much faster than the artefacts.

### Both p322-named gaps, executed

- **EduClaw-Bench (arXiv 2608.03206)** — 55 scenarios (11 learner personalities × 5 study schedules)
  over **30 virtual days** each, scored on learning gain, responsiveness and helpfulness plus Gagné
  and Rosenshine curriculum-design axes. Unggi Lee +5, 4 Aug 2026. **Still only the anonymous review
  link** `anonymous.4open.science/r/educlaw-bench-anonymous-ED3F`. The author name was searched
  directly this pass as well; no named repository, no licence.
- **EduFair-Bench (arXiv 2609.12949)** — EPFL (Zhao, Radmehr, Fawzi, Nazaretsky, Käser), 11 Sep
  2026; nine demographic levels over gender, immigration background, first language and SES. **No
  repository, no licence.** Its two findings are usable without the code: **capability and fairness
  are largely orthogonal**, and **language and immigration cues produce larger gaps than gender and
  SES** — which is not where fairness review effort usually goes.
- **ELBench (arXiv 2608.09548)**, new to this KB, no code: four modules over nine models, and
  **the education-specialised models lead neither education module.** Authors state the data is
  synthetic and the benchmark text-only. Snippet-and-abstract sourced, not read first-hand.

### Recorded below the listing bar — permissive, real, too thin to list

Consistent with the p322 rejection of `CristianHeyde/language-teaching-skills` on weight alone:

- **`fcescob/understand` (MIT, 5 ★, 6 commits)** — **the most explicit mastery gate in this KB.** A
  stage passes only **cold, unprompted**: explain it, give an example *and a near miss*, name a
  misconception, transfer it to a new context — and **retention counts only on a later-day pass**,
  on a **1 / 3 / 7 / 21 / 60-day ladder**, with per-answer confidence 1–5 and hints before answers.
  Installs to Claude Code, oh-my-pi, Codex. Documents its own portability defect: **claude.ai
  uploads and the Skills API reject it over its frontmatter fields.** Read the gate, not the repo.
- **`fanfanfanfanfan626/mastery-tutor` (MIT, 3 ★, 19 commits, v0.4.1)** — `mastery-coach` plus
  `mastery-tool-creator`, guided HTML lessons, one local classroom per thread, state in `.mastery/`,
  no account and no hosted database; records **how much help was needed** and can mark earlier
  mastery **fragile**. Names no scheduling algorithm. **Says of itself "research-informed, not
  outcome-proven" and tests software and teaching contracts rather than learning outcomes** — the
  honest version of the claim every vendor here makes.
- **`grey8-io/learn-ai-with-grey8` (10 ★)** and **`CGSeb/lessonfolk` (3 ★)** — courses about AI with
  a tutor attached. Curriculum content, not agent dependencies.

### The APAC skill tier has a personality-rights problem, and this KB has not raised it before

**`tong666-bit/liu-xiaoyan-skill` (MIT, 18 ★, 6 commits)** teaches CET-4/6 and postgraduate-entrance
English *in the teaching style of a named, living educator* (刘晓艳); its sibling
**`tong666-bit/song-hao-math` (4 ★)** does the same for 宋浩 across calculus, linear algebra,
probability and complex analysis. **The disclaiming is explicit and unprompted** — *"非本人、非官方
出品"* (not by the person, not an official product), About reads *"刘晓艳风格，非官方"*, and the README
states the class-style lines *"不冒充老师原话"*, they do not pass themselves off as the teacher's
actual words.

**The point for a studio: the MIT licence covers the code and says nothing about the persona.** The
product value here is a named individual's pedagogical identity, and right-of-publicity exposure
travels with whoever ships it. **Read these for the pedagogy; never carry the persona framing into a
client deliverable.** Trend 7 has treated skills as a packaging story — this is the first evidence
that the packaging can carry a legal payload. No equivalent exists in the Western skill tier yet.

### The new-supply tail, measured

GitHub repositories matching *education / AI / tutor / agent* **pushed since 2026-10-01**, sorted by
stars: **the first page holds ten results and the top one has 41 stars.** Four of ten are
Chinese-language exam-prep skills, three are courses about AI, three are local-first mastery tutors
at 3–8 stars. **Nothing with real weight entered this category in three weeks, and what did enter is
skill-shaped and disproportionately APAC-authored.** Both reinforce trend 7; neither supports a
claim that this tier is consolidating.

## Pass 322 · 2026-10-19 (eighth pass of this date) — the `openeduhub` org, enumerated in full, and the finding is licence-by-layer

**Three rows added here, one to the evaluation table, twelve to `repos/foundations.md`, one measured
404.** Pass 321 found the `openeduhub` organisation, read four of its repositories and wrote down the
names of six it had not read, explicitly *"so p322 does not re-discover them"*, closing with
**"57 of the 67 were not listed on the first page and remain unenumerated."** Pass 322 enumerated all
sixty-seven — by paging the org listing under two different sort orders, because one sort order hides
what the other shows — and read **sixteen repositories first-hand**, every one of the AI-era ones.

**The finding is not a repository, it is a shape.** Germany's publicly funded OER portal has shipped a
twelve-service AI metadata pipeline: extraction, human review, deduplication, readability scoring,
accessibility and licence lookup, Bayesian metadata prediction, discipline classification, bulk prompt
running, factual-accuracy judging and a unified gateway over the lot. **And its licences divide by
architectural layer, not by repository:**

| Layer | Repos | Commits | Licence |
|---|---|---|---|
| Thin shells — UI, REST wrapper, browser plugin, path editor | `metadata-agent-canvas`, `metadata-browser-plugin-fuerAPI`, `lernpfadeditor`, `tutor-chatbot`, `llm-judge`, `wlo-quellenliste`, `duplicate-detection` | 60, 11, 6, 10, 1, 6, 25 | **Apache-2.0** (or claimed — see the README hazard) |
| Analysers and classifiers | `metalookup`, `text-statistics`, `discipline-classification` | 623, 94, 73 | 🟡 **GPL-3.0** |
| **The inference core** | `python-kidra`, `its-jointprobability`, `text-extraction`, `z-api-runner`, `its-qna`, `oeh-search-etl` | 137, 200, 77, 37, 4, 1,397 | 🔴 **none at all** |

**1,852 commits of ML and data plumbing carry no grant whatsoever, and they are precisely the part a
studio cannot write in a sprint.** Pass 321 observed that "the unlicensed repository is the one with
the most commits" and read it as one bad apple. It is not one repository — **it is the entire
inference core, and the permissive surface contains none of the org's machine learning.** The
practical rule for an engagement is in `repos/foundations.md`: take the shells and the API client,
reimplement or negotiate the brains, and keep the GPL-3.0 analysers behind a process boundary.

**The README hazard, now at four instances in one organisation.** Four repositories state a licence
in their README that the repository does not carry:

| Repo | README says | Repository actually carries | Verified how |
|---|---|---|---|
| `duplicate-detection` | "MIT License" | **Apache-2.0** | `LICENSE` read first-hand — it is the Apache 2.0, January 2004 text |
| `wlo-quellenliste` | "Lizenz: MIT" | **Apache-2.0** (sidebar + `LICENSE`) | sidebar and file listing |
| `metadata-agent-api` | "Lizenz: MIT" | 🔴 **nothing** — no `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING` in the root | root file listing enumerated first-hand |
| `metadata-agent-canvas` | "Apache License 2.0", "Copyright 2025 Jan Schachtschabel" | 🔴 **no licence file in the root listing**; sidebar shows no licence | root file listing enumerated first-hand |

The pattern is a copied README template, and it cuts both ways: twice it understates the grant, twice
it asserts a grant the repository does not make. **The rule this KB now applies: the `LICENSE` file
governs, and a README licence claim with no file behind it is not a grant.** That is the opposite of
the assumption a reader makes when a README says MIT.

**One measured 404.** `python-kidra`'s README lists seven bundled services; six have public
repositories in the org and **`openeduhub/wlo-topic-assistant` returns 404.** `wlo-classification`
does not exist under that name either — it **redirects to `openeduhub/discipline-classification`**,
a GPL-3.0 fork of `yovisto/wlo-classification`. Recorded rather than left silent: the gateway
advertises a capability whose source is not public under this org.

**Method, re-tested this pass rather than inherited, and it reproduces exactly.** `github.com` is
reachable with the fetch tool; non-GitHub origins are not —
`www.digitaleducationcouncil.com` failed at DNS (`getaddrinfo ENOTFOUND`) when attempted directly
this pass. No scanning probe was attempted, because passes 319–321 recorded that `curl -sI` returns
403 at the session proxy and that two probe attempts were refused by the sandbox classifier.
**Every repository and licence claim in this pass is first-hand off github.com. Every regional claim
in `intel/` remains snippet-sourced and is labelled there.**

**The prescribed search battery returned nothing this KB did not already hold — third pass running.**
All four global searches and all four regional searches were run. The global battery returned
general-purpose agent roundups with no education focus, one vendor LMS comparison, and market
forecasts spanning USD 6.4bn–10.6bn for the same year. The regional battery returned the Digital
Education Council LATAM survey, the IESALC 200-institution survey, the Carnegie Mellon/Gates USD 55m
courseware investment, OpenAI's eight-partner country programme, the TCS–Pearson alliance and the
50/19 feedback gap — **every one already in `intel/market.md`, most with a precision the snippets
lacked.** Two numbers were checked individually against the KB and were also already held. The
verdict and what it implies for how a pass should spend its budget are in `intel/trends.md`.

**A recount, because the number in the p321 text was stale.** This file's main table holds
**twenty-seven rows before this pass, thirty after** — p321's prose said twenty-six, which was the
count before its own addition. `repos/foundations.md` holds twenty-three before this pass,
thirty-five after.


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
| claude-study-agent | https://github.com/dymchenkko/claude-study-agent | MIT (`LICENSE` read first-hand — *MIT License, Copyright (c) 2026 dymchenkko*) | 2 | p325 | **A local-first study agent over the learner's own course material, including the lectures.** Ingests slides, PDFs and **lecture recordings** — Whisper for the audio, OCR for scanned pages — then builds a semantic index and runs a study loop over it: spaced-repetition quizzing, mistake tracking and **generated mock exams**. Built on Claude Code; topics declare `local-first`, `rag`, `anki-alternative` and `notebooklm-alternative`. Created 2026-10-10, pushed 2026-10-19, 0 forks | **The lecture-recording leg no other artefact in this file has.** Where `universal-examprep-skill` assumes the learner owns slides and past papers, this one assumes they also own the *recording* of the class — the single richest unexploited corpus in formal education, and the one most likely to carry a consent question. Read it for the ingest chain; treat the recording as personal data from the first line of the proposal |
| aegis-integrity | https://github.com/sunilgentyala/aegis-integrity | MIT (sidebar + `LICENSE`, Copyright (c) 2026 Sunil Gentyala) | 17 | p324 | **Local-first academic-integrity reviewer exposed as an MCP server** — *"Free, local-first academic integrity checker and MCP server"*. **Seven MCP tools**: `aegis_analyze_paper`, `aegis_check_citations`, `aegis_check_guidelines`, `aegis_compare_papers`, `aegis_index_add`, `aegis_index_summary`, `aegis_status`. Five signal families: **citation-hallucination resolution against Crossref** with verdicts `VALID`/`MISMATCH`/`HALLUCINATED`/`UNRESOLVABLE`/`NO_DOI`; AI-text via **GPT-2 perplexity, burstiness, a stylometric ensemble and lexical-tell density** plus a semantic-coherence analyser; plagiarism via **n-gram MinHash + SBERT/FAISS against a corpus you supply**; ghostwriting via **Burrows' Delta**; and an experimental keyless watermark heuristic that *"never affects the overall integrity risk score"*. Self-plagiarism, essay-mill batch analysis, citation-network analysis and **venue-guideline checks for IEEE, ACM and Elsevier**. `pip install "aegis-integrity[ml]"` + `aegis ui` for a local web app; Claude Code plugin; Claude Desktop `.mcpb`; `docker compose`; GHCR image; `install.bat` on Windows. Crossref/OpenAlex/DataCite are called with **reference metadata only, never the document**, and there is an explicit `offline=true`. 68 commits, 5 forks, changelog at v3.3.2 | **The artefact this KB declared absent for seven passes — and the reason to use it is what it refuses to claim.** It publishes **no accuracy figure for itself**, cites third-party studies instead, and states *"Results are a supporting signal for human review, not a determination of misconduct"* and, on ESL bias, *"Do not treat AEGIS as having solved ESL false positives; keep a human in the loop."* 🔴 **Read its own tension before quoting it:** the marketing section says per-language calibration *"reduce[s] this bias"* while the ESL section says the non-English multipliers *"rarely fire"*, and the changelog records an earlier ESL multiplier that was **inverted** and fixed. Deploy it as the **citation and process-evidence** layer of an integrity review (`compose/patterns.md` **P11**); do not deploy its AI-text score as a finding |
| civil-ai | https://github.com/zhangl1001/civil-ai | MIT (sidebar + LICENSE) | 41 | p323 | **A reusable, local-first foundation for adaptive education agents on iOS and Web** — its own words: *"Civil AI is a reusable, local-first foundation for building adaptive education Agents on iOS and Web"*, with the Chinese civil-service-exam package as *"the current end-to-end reference adapter"* that *"does not define the scope of the foundation."* Vue 3 + TypeScript, Capacitor iOS shell; **SQLite on iOS and IndexedDB on Web behind repository ports**, with migrations; Anthropic and OpenAI-compatible provider gateway with providers as replaceable adapters; agent runtime with tools, skills, **checkpoints, leases, cancellation and recovery**; an *"evidence-based capability model"* with mastery projection and review priority, and spaced review in the reference app (no algorithm named). English README with a Chinese positioning section; 100 commits, 7 forks; docs reference a v1.2.0 upgrade guide, Releases empty | **The highest-starred education agent pushed since 2026-10-01, and the only artefact in this KB that separates an education-agent runtime from its exam adapter on purpose.** Read it for the ports-and-adapters shape when a client wants one tutor engine across several subjects — and read its own caveat first: **it states that domain portability is unvalidated because both bundled packages are exam-style, question-driven study** |
| algebench | https://github.com/ibenian/algebench | MIT (sidebar) | 8 | p323 | **Interactive 3D mathematics visualiser with an interruptible AI narrator**: the learner stops a running lesson scene to ask what/how/why and the narrator answers in real time while the visualisation responds, with step-by-step proofs and a semantic graph kept in sync with the 3D view. Scenes built from adjustable parameters and live simulations; Three.js frontend; **lessons stored as JSON files**; runs via a `./algebench` script or Docker image on localhost. **Google Gemini only, bring-your-own-key.** 519 commits, 1 fork | **The interruption is the pedagogy** — this is the only artefact here where the learner controls the explanation mid-stream rather than after it, and lessons-as-JSON makes the scene format readable. **Not a dependency: Gemini-only means the model is not pluggable as shipped**, the same disqualifier this file applied to GradeMate. **519 commits at 8 stars — see the p320 lesson on star counts** |
| lernpfadeditor | https://github.com/openeduhub/lernpfadeditor | **Apache-2.0** (sidebar + LICENSE) | 0 | p322 | **AI-assisted editor for differentiated learning paths** (*"Ein KI-gestützter Editor zur Erstellung differenzierter Lernpfade"*), built for WirLernenOnline.de: generates a path template from a natural-language description, performs automatic internal differentiation (*Binnendifferenzierung*) into tiered tasks, and ranks WLO resources for assignment to each step. **GPT-4o** for template generation and resource ranking, **Whisper** for dictation, **up to 20 parallel AI calls**; React + TypeScript + Vite, TailwindCSS, Zustand; needs Node 18+ and an OpenAI key. 6 commits | **Differentiation is the teacher-facing feature clients ask for by name and this KB had no permissive implementation of it.** 6 commits is a prototype — read the differentiation prompt design, not the code |
| metadata-agent-canvas | https://github.com/openeduhub/metadata-agent-canvas | 🟡 **README claims Apache-2.0 — no licence file in the root listing** | 0 | p322 | **Human-in-the-loop metadata canvas**: an Angular web component that fills schema fields from a text in parallel via LLM, shows each extracted value with a **confidence badge** for inline editing, validates required fields against controlled vocabularies, normalises values, enriches addresses with geocoordinates (Photon/OpenStreetMap through a server-side proxy) and ends on an explicit *Bestätigen* confirm step before JSON download or submission to the WLO repository. Standalone, bookmarklet and browser-plugin modes. Angular 19, Angular Material, RxJS, **LangChain (`@langchain/openai`)**, Netlify Functions / Vercel / Docker+nginx. Providers: OpenAI direct, B-API→OpenAI, **B-API→AcademicCloud (DeepSeek-R1)**. 60 commits — the most-developed AI artefact in the org | **The review-UI pattern this KB has been describing in the abstract since p317, implemented.** Confidence badge → inline edit → explicit confirm is the shape a human-oversight requirement actually takes in a product. 🔴 **Do not depend on it:** the README states Apache-2.0 and the repository root carries no licence file, so the grant is unverified — read it for the interaction design |
| metadata-browser-plugin-fuerAPI | https://github.com/openeduhub/metadata-browser-plugin-fuerAPI | **Apache-2.0** (sidebar + LICENSE) | 0 | p322 | **Manifest V3 extension for Chrome and Edge (v2.1.0)** that indexes educational resources from the page the teacher is on: extracts metadata *per KI*, lets the user review it, and uploads to the WLO repository **either signed in or as a guest**; plus a "shopping cart" that collects materials into a printable lesson plan, and a watch list and upload history. Calls a deployed backend at `metadata-agent-api.vercel.app` — `/generate` for extraction, `/upload` for guest submission. 11 commits, 1 fork | **The browser is the capture surface for teacher-contributed OER, and this is a working instance of it.** Also the clearest evidence in this KB that the metadata-agent line is deployed, not just committed: the plugin points at a live Vercel host |
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
| cloverailab | https://github.com/Kyyota-Wang/cloverailab | 🔴 **NO LICENCE** (7 candidate filenames probed across 5 branch names on the `raw` channel, none returns 200) | 0 | — | **The tier's second measured agreement figure, and the second one with no grant.** GRE **Analytical Writing** reviewer *and* writer agents: an **LLM-as-judge scored against the published ETS rubric using officially scored anchor essays, with no fine-tuning**, reporting **QWK 0.825 against those official anchors** — with the evaluation harness and the results committed to the repository rather than asserted in a README. TypeScript on Cloudflare Workers. 🔵 **Why it matters out of proportion to its zero stars:** every uplift claim a client will be shown in this sector is a judged score, and p323 established that judged helpfulness is the wrong instrument. **This is the opposite case — a judged score against a published rubric and real anchors, which is the one form of LLM-as-judge that can be defended** — and QWK against official anchors is the figure a testing organisation will actually recognise. 🔴 **Read the method and rebuild it; the repository carries no licence, so neither its harness nor its results can enter a deliverable** |
| knowsim | https://github.com/yjo2lee/knowsim | MIT (`LICENSE` read first-hand — *MIT License, Copyright (c) 2026 Yoonjoo Lee*) | 4 | — | **The simulated learner, not the tutor.** *"Knowledge-state-aware user simulator for evaluating information calibration in LLM assistants"* — arXiv 2608.17150. It supplies the piece every evaluation in this tier has to improvise: a student whose knowledge state is **controlled and known**, so that an assistant's confidence can be scored against what the learner actually knows rather than against an answer key. **Calibration, not pedagogy and not accuracy** — the only artefact in this KB aimed at it, and the complement to MathTutorBench (pedagogy) and `llm-judge` (content accuracy). Small and single-author; read it for the simulator contract |
| EduGuardBench | https://github.com/YL1N/EduGuardBench | 🔴 **NO LICENCE** (no sidebar licence entry, no LICENSE file) | 5 | 2 | **The eval tier's first artefact published in conference proceedings — and the only one that cannot be used.** arXiv 2511.06890 (10 Nov 2025), **AAAI proceedings article 40399**; Yilin Jiang +7. Dual-component: a **Role-playing Fidelity Score (RFS)** for professional teacher-simulation fidelity, and **persona-based adversarial prompts** targeting general harms and specifically **academic misconduct**, scored by **Attack Success Rate (ASR)** and a **three-tier refusal-quality** assessment, across **14 models**. Ships `SATAs.xlsx` (Select-All-That-Apply teaching-harm items), `adversarial_prompts.xlsx`, Python scripts for both experiments, a shared utilities folder, an analysis/figures notebook and a full appendix PDF (scenarios, ethics taxonomies, dataset design, annotation guidelines) — **with empty `Results/` folders.** Two results worth quoting: an **"Educational Transformation Effect"** in which the safest models convert harmful requests into teachable moments as ideal **Educational Refusals**, a capacity **strongly negatively correlated with ASR**; and a **scaling paradox** in which mid-sized models are the most vulnerable, so safety is **not monotonic in model size**. **Read the paper and the appendix; the repository has no grant, so its data and scripts cannot enter a deliverable** |
| llm-judge | https://github.com/openeduhub/llm-judge | **Apache-2.0** (sidebar + README + LICENSE) | 0 | 1 | **A factual-accuracy judge for educational content, published by a public OER operator** — *"KI-gestütztes Bewertungstool für Sachrichtigkeit von Bildungsinhalten"*. Scores the description field of a learning object (`cclom:general_description`) against **six criteria declared in `config.yaml`**: factual correctness, clarity and comprehensibility, objectivity, relevance, structure and length, language and style. Input is JSON with `node.properties` and a `sys:node-uuid`; single or batch; `gpt-4o-mini` default or `gpt-4o` via `MODEL_ID`, with an optional `BASE_URL` to point at a different endpoint; 30 s default API timeout. Outputs CSV scores, JSON with improvement suggestions, and interactive charts — **1 commit** — this is a published intent, not a tool. And note what it judges: **content accuracy, not pedagogy.** It is the complement to the four pedagogical evaluators above, not a substitute, and the README states neither the scoring scale, the prompts nor the aggregation — so its numbers are not comparable to anything |
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

**Pass 323 added two rejections, both of them artefacts this KB wanted to exist.**

- **`YL1N/EduGuardBench` — NO LICENCE, and it is in the AAAI proceedings.** 5 ★, 3 forks, 2
  commits. Full read in the evaluation table above. **It is listed there rather than only here
  because the measurement it defines is usable even though the repository is not** — RFS, ASR and
  the three-tier refusal assessment are described in the paper and the appendix PDF, and a studio can
  implement them. **What cannot be used is the shipped material**: two `.xlsx` datasets and the
  experiment scripts carry no grant. **This is the first unlicensed artefact in this KB's eval tier
  and the fourth consecutive pass to record a peer-reviewed education artefact whose repository has
  no licence file.** Ask the authors — a one-line LICENSE commit would make an AAAI-published
  safety benchmark immediately usable, and that is a cheap ask.
- **`razi-03/NCERT-CKG` — NO LICENCE, 0 ★, 2 commits, one grade of one subject.** Class X
  NCERT Mathematics from 18 PDFs into CKG JSON: **10,417 CKG nodes, 1,682 semantic nodes with
  provenance at 1,682 / 1,682** (*"every semantic node is required to have source evidence"*) and
  **13,757 provenance-aware edges**. **Rejected on licence and weight, recorded because the method is
  right:** *"prerequisite reasoning is treated separately from textbook ordering"* and a
  prerequisite *"must instead be supported by conceptual dependency evidence or an explicit inference
  procedure"* — the discipline this file praised in `bncc-dev` and faulted `jinanshm/ncert-mcp`
  for lacking. Two things the README does not say and both matter: **nothing about textbook
  copyright or whether the 18 NCERT PDFs are bundled**, and nothing about whether an LLM derived the
  edges — it never mentions an LLM at all, so this is unknown rather than concealed. **It makes
  India's curriculum gap contested rather than empty. Watch the licence; ask the author.** See
  `repos/foundations.md` and pattern P10 Variant B.

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

## Licence split, recounted over 28

MIT (16 — FSRS4Anki, iblai/os, anki-mcp-server, Educhain, Bloom, OATutor, OpenTutor, tutor-mcp,
Study-Mate, instructional_agents, universal-examprep-skill, claudemy, algo-sensei, Claw-ED,
**civil-ai**, **algebench**),
BSD-3-Clause (3 — nbgrader, otter-grader, Open TutorAI CE), Apache-2.0 (3 — DeepTutor, smolagents,
lineage-skill), **GPL-3.0 (3 — tutor-gpt, lumen, LTLTutor)**, dual MIT/AGPL-3.0 (1 —
human-skill-tree, skills only), CC0-1.0 (1 — gen-mentor), CC BY-SA 4.0 (1 — education-agent-skills).

**24 of 28 carry a permissive *software* licence Globant can build on commercially** (counting
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
  LTI 1.3 with instructor approval, Spanish docs, no LICENSE). `pylti1.3` (MIT, re-verified p319: 138 ★, 84 forks, 178 commits, 39 open issues, **no published
  release**) is still the solid Python library. **The p319 question about `tsugiproject/tsugi` is
  closed this pass, and the answer is that the repository does not say:** Apache-2.0, 376 ★, 266
  forks, **4,011 commits, Releases section empty**, and the README **names no LTI version at all** —
  only *"a multi-tenant scalable LTI library and tool hosting environment"* and *"implements an IMS
  ContentItem App store"* (ContentItem being the LTI 1.1-era content-selection message, which hints
  at the older generation without declaring it). **An LTI integration cannot be scoped from Tsugi's
  README**, so the concentration risk is unrelieved: one maintained library, no release tags, and
  the only alternative does not state what it speaks (`repos/foundations.md`).
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
