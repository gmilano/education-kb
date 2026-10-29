---
industry: education
region: Global
updated: 2026-10-29
---

## 🆕 `p518` — `2026-10-29` — **🟢 THIS SHELF GAINS ITS LARGEST ROW AND ITS CLEANEST LATAM ROW IN THE SAME PASS: `freeCodeCamp` — **BSD-3-Clause**, **458,132★** — and 🇧🇷 `Universidade-Livre/ciencia-da-computacao` — **MIT**, **20,985★**. 🔴 And it loses a row it never actually had: `openedx/edx-platform` is a RENAMED repo, invisible to the search API under the slug this base carried.**

🔵 **What belongs here.** A foundation is something a studio builds *on* — a platform, a
curriculum corpus, a runtime, or a provenance index. Agents compose; foundations carry. Every
row re-read `2026-10-29` against the repository API with a single-licence assertion per repo.

### 🟢 The permissive foundations, re-asserted today

| Repo | Origin | Licence (asserted today) | ★ | Default branch | What a studio builds on it |
|---|---|---|---|---|---|
| [`freeCodeCamp/freeCodeCamp`](https://github.com/freeCodeCamp/freeCodeCamp) | 🇺🇸 freeCodeCamp.org | **BSD-3-Clause** | **458,132** (48,718 forks) | `main` | 🟢 **The largest education codebase in open source, and permissively licensed.** Platform *and* curriculum: math, programming, CS, plus a certification engine. A studio can lift the curriculum data model, the challenge/test-runner pattern, or the whole platform |
| [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao) | 🇧🇷 | **MIT** | **20,985** (1,688 forks) | `main` | *"Um caminho para a educação autodidata em Ciência da Computação"* — a structured, community-maintained CS curriculum **in Portuguese**. 🟢 For a 🇧🇷 engagement this is the curriculum spine that does not need translating |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🌐 Project Jupyter | **BSD-3-Clause** | **8,359** (2,125 forks) | `main` | Multi-user notebook server. The standard way to give a cohort identical, isolated, pre-provisioned compute — the substrate under almost every university CS/DS course |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🌐 Oppia Foundation (nonprofit) | **Apache-2.0** | **6,951** (5,861 forks) | `develop` | Authoring + delivery of *interactive* lessons with built-in misconception handling. 🟢 Permissive and pedagogically opinionated — rare together |
| [`Universidade-Livre/matematica`](https://github.com/Universidade-Livre/matematica) | 🇧🇷 | **MIT** | **1,422** (92 forks) | `main` | The mathematics counterpart to the CS curriculum above. Same org, same grant, same language |
| [`llm-jp/awesome-japanese-llm`](https://github.com/llm-jp/awesome-japanese-llm) | 🇯🇵 LLM-jp (NII-led) | **Apache-2.0** | **1,442** (49 forks) | `main` | The authoritative index of Japanese LLMs **and their licences**. 🔵 An index, not a product: licence-and-provenance routing for a 🇯🇵 engagement starts here rather than at a model card |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🌐 Learning Equality | **MIT** | **1,163** (1,012 forks) | `develop` | **Offline-first** learning platform built for low- and no-connectivity deployment. 🟢 The foundation under `P526`; the only row here designed for a school with no reliable uplink |
| [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🇨🇱 | **MIT** | **136** (12 forks) | `main` | Chilean public data — **including education** — curated, normalised, validated, queryable from Polars/DuckDB/SQLite in one line. 🔵 Small, but it is the shape a regional grounding corpus should have |

### 🔴 The renamed-repo failure, recorded as infrastructure guidance

🔴 **`openedx/edx-platform` does not resolve through the API.** `repo:openedx/edx-platform`
returns *"The listed users and repositories cannot be searched either because the resources do
not exist or you do not have permission to view them."* The live repository is
[`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) — **AGPL-3.0**, 8.2k★,
README: *"Formerly known as 'edx-platform'"*. 🔵 **The lesson is about the instrument, not Open
edX:** GitHub serves a browser redirect for a renamed repo and does **not** serve one to the
search API. So a human spot-check passes while automated verification reports the repo missing —
the two checks disagree, and the human one is the misleading one. 🟢 **Rule for this base: resolve
a repo by API before recording its slug, and record the slug the API returns.**

### 🔴 A 4,877★ "open" curriculum corpus that is non-commercial — and disagrees with itself

🔴 [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) —
**4,877★**, created `2026-10-18`, 1,242 forks. A 🇨🇳 K-12 knowledge graph spanning mathematics
(primary→senior high), English (grade 3→senior high) and junior/senior-high physics, aligned to
the national curriculum standard, shipped with an adaptive prerequisite diagnostic. On supply
shape alone it is exactly what this shelf wants. 🔴 **It is blocked twice over:**

1. 🔴 **The grant is `CC BY-NC 4.0`** — *non-commercial*. Read from the README (GitHub's
   classifier declines it, so the sidebar shows only a bare "License" link). It covers the
   knowledge graph, the question bank, the diagnostic tool code **and** the documentation; only
   the vendored Cytoscape/dagre libraries under `assets/vendor/` stay MIT. A client engagement is
   commercial use. **This cannot ground a client tutor.**
2. 🔴 **The repo's own counts do not agree with each other**, read the same day:

| Quantity | About blurb | README tally |
|---|---|---|
| Knowledge points | **1,644** | **~1,838** (math 845, English 724, physics 269) |
| Prerequisite edges | **2,403** | **~2,926** (≈1,769 hard, 1,157 soft) |
| Questions | **6,723** | **7,427** (math 3,467, English 2,896, physics 1,076) |

🔴 **And the README states the content is an AI-generated first draft that has not been reviewed
by teachers, with prerequisite relationships and difficulty levels unvalidated.** 🔵 Recorded here
in full because its star count will keep surfacing it: a studio that shelves it on stars alone
inherits a non-commercial grant, unverified pedagogy, and a corpus whose size it cannot state.

### 🔴 Declared gaps on this shelf

🔴 **No permissive national-curriculum corpus was found for EMEA.** 🇧🇷 has `bncc-dados` (MIT,
already held) and now two `Universidade-Livre` curricula; 🇨🇳 has `cn-math-taxonomy` but
non-commercially; 🇯🇵 has a licence index. Searched this pass for Spanish/Portuguese
(`educacion|educativa|educacao|escolar in:name,description stars:>120`) and for
`sunbird|diksha education india stars:>80` — **the India leg returned zero repositories**, despite
NCERT's DIKSHA being one of the largest national education platforms in the world. 🔵 That is a
discovery-channel nil, not an absence claim: DIKSHA's code is published under the Sunbird
programme, and nothing matching surfaced under these queries.

## 🆕 `p517` — `2026-10-29` — **🟢 THIS SHELF GAINS A LAYER THE LATAM PASS ESTABLISHED THE NEED FOR AND COULD NOT FILL FOR APAC: a licence-and-provenance index for a national LLM ecosystem — 🇯🇵 `llm-jp/awesome-japanese-llm`, **Apache-2.0**. 🟢 And it gains the instrument itself: `ingest/probe-grant.sh` is now foundational infrastructure for this base, not a one-pass script. 🔴 8 of 12 APAC education repos probed this pass carry NO GRANT.**

### 🟢 The instrument is a foundation — `ingest/probe-grant.sh`

🔵 **Why a script belongs on the foundations shelf.** Every other row here is something a studio
builds *on*. This one is something a studio must run *before* it builds on anything — and this
base spent **eight passes** on a false LATAM nil and **one more** on a false APAC claim for want
of it.

🟢 **What it is:** `git ls-remote --symref` to resolve the default branch and liveness, then **53
grant filenames across 14 languages** probed at that branch over `raw.githubusercontent.com`.
🟢 **What it refuses to do:** emit the word *unlicensed*. It emits **`UNRESOLVED`**, which is a
measurement. 🔵 Full rationale, self-test and the two bugs found in it: `agents/top.md` `p517`.

🟢 **It closes `Gap 516-A`**, which `p509` opened in prose and `p516` reproduced six passes later —
the base's clearest demonstration that a finding written into narrative does not survive, and a
finding written into an instrument does.

### 🟢 Curriculum-and-licence provenance for 🇯🇵 — the APAC half of `p516`'s curriculum-as-data layer

🔵 **`p516` added the LATAM half:** `bncc-dados` (MIT) emits Brazil's national curriculum as 1,721
provenance-tracked learning objectives. 🔴 **There is no APAC equivalent on these shelves** — no
national curriculum published as machine-readable open data was found in the Mandarin, Japanese,
Korean or Hindi legs. 🟡 **What exists instead, and is foundational for a different reason:**

| Repo | Origin | Licence (from bytes) | HEAD @ branch | Why it is foundational |
|---|---|---|---|---|
| [`llm-jp/awesome-japanese-llm`](https://github.com/llm-jp/awesome-japanese-llm) | 🇯🇵 **LLM-jp** — NII-led cross-organisational project (arXiv `2407.03963`) | 🟢 **Apache-2.0** (`LICENSE` @ `main`) | `4fa4630ddbdd` @ `main` | The authoritative index of Japanese LLMs **with their licences**. 🟢 A 🇯🇵 engagement's model-selection and grant-routing decision starts here rather than in vendor prose |

🟢 **The provenance fact that makes it load-bearing:** LLM-jp publishes weights **Apache-2.0**, and
switched to Apache-2.0 **as a matter of policy from March 2025** after criticism of a restricted
licence on `llm-jp-3-172b`. 🔵 So for a Japanese engagement there is a *national-scale, permissively
licensed* base-model line, and this index is its map. 🔵 Adjacent, same policy: **GPT-OSS Swallow**
(20B/120B reasoning models, Japanese-strengthened, weights Apache-2.0) and **Tanuki**.

🟡 **`llm-jp/bridge-ai-for-edu`** — the same org's **education** repo — is 🔴 **`UNRESOLVED`**
(no grant on 53 names @ `main`, HEAD `31c82c466375`), 2★, **no description**, 56 commits, last
touched `2026-10-14`. 🟢 **Watched as `Gap 517-D`:** if LLM-jp grants it Apache-2.0 as it did its
weights, it becomes the first 🇯🇵 national-scale education asset on these shelves.

### 🟢 One new permissive runtime reference — small, and shelved at its size

| Repo | Origin | Licence | ★ | HEAD @ branch | What it is |
|---|---|---|---|---|---|
| [`yqy624/eduagent-digital-workforce`](https://github.com/yqy624/eduagent-digital-workforce) | 🇨🇳 | 🟢 **MIT** (`LICENSE` @ `main`) | 🔴 **3** (1 fork) | `a52bf227145c` @ `main` | FastAPI + LangChain + YOLO + RAG, 75 commits. 🟢 **Foundational for its *gate design*, not its size:** grading requires teacher confirmation before any grade is written; classroom vision logs events without acting; analytics is read-only and makes no final judgement; supervision de-duplicates and requires manual confirmation. 🔵 Its own page calls it *"a demonstrable MVP rather than a production system"* |

🔴 **Why that is worth a foundations row at 3★.** Every education buyer on these shelves asks for
human-in-the-loop guarantees, and this base's patterns have had to specify them from scratch each
time. This repo states them **per agent, in code structure**, under MIT — so it is citable as a
reference design even though it is not deployable at scale.

### 🔴 The foundations-shelf nil that is real, and is now measured rather than assumed

🟢 **Stated as information, which is the point of writing it down.** Searched this pass in Mandarin,
Japanese, Korean, Hindi and Indonesian for an APAC **national curriculum as open data** — the
`bncc-dados` equivalent. 🔴 **Nothing was found in any of the five languages.** 🔵 Unlike the LATAM
and APAC supply claims this pass refuted, this nil is **grep-checked against these shelves first**
and holds: no such row exists here, and none was discoverable. 🟡 **It is a genuine gap, not an
instrument artifact** — and `Gap 517-C` (Gitee/GitCode unprobed) is the one channel that could
still overturn it.


## 🆕 `p516` — `2026-10-29` — **🟢 THE FOUNDATIONS SHELF GAINS A LAYER IT HAS NEVER HAD: a national curriculum as machine-readable, provenance-tracked open data — 🇧🇷 `bncc-dados`, MIT, 1,721 learning objectives in JSON/SQLite/CSV — plus the MCP package that serves it to agents. 🔴 Found only because the discovery query was run in Portuguese; eight English-language passes missed it. 🔴 Two licence verdicts on this shelf's probe method were WRONG for the same reason.**

### 🟢 The missing layer — curriculum-as-data, and why it is foundational

🔵 **What this shelf has always had:** tutoring runtimes, LMS cores, scheduling algorithms,
retrieval stacks. 🔴 **What it has never had:** the *curriculum standard itself*, in a form an
agent can resolve against. Every adaptive-learning pattern on
[`compose/patterns.md`](../compose/patterns.md) has had to assume the client supplies a competency
map. 🟢 **`bncc-dados` is that map, for Brazil, under MIT.**

| Repo | Licence (read from bytes) | HEAD @ default branch | Role on this shelf |
|---|---|---|---|
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | **MIT** — root `LICENSE` @ `main`, *"Copyright (c) 2026 Profy Tecnologias Educacionais Ltda"* | `9c268978efa2` @ `main` | 🟢 **Curriculum ground truth.** Brazil's **BNCC** (*Base Nacional Comum Curricular*) as open, verified data: **1,721** learning objectives, emitted as **JSON, SQLite and CSV**, with **provenance per record** |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **SPLIT** — code **MIT** (`LICENSE-CODIGO.md`), embedded data **CC BY 4.0** (`LICENSE-DADOS.md`) | `e9b4985adf83` @ `main` | 🟢 **The access layer.** npm + PyPI packages **and an MCP server** (`mcp-worker/src/`) that serves BNCC objectives to an agent as tools. Data JSONs are **synced from a pinned commit** of `bncc-dados`, keeping that repo's grant |
| [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟡 **SPLIT** — code **MIT**, items/results/methodology **CC BY 4.0** | `4713901ce5d7` @ `main` | 🟢 **The evaluation layer.** Open LLM-hallucination benchmark **grounded in the curriculum** — the only curriculum-anchored factuality benchmark on these shelves. **12★**, 1 fork |

🟢 **Together they are a three-layer stack this base could not previously assemble:** ground truth
(`bncc-dados`) → agent access (`bncc-pacotes`, MCP) → factuality measurement (`bncc-benchmark`).
🔵 All three are 🇧🇷-originated, which is also the refutation carried in
[`agents/top.md`](../agents/top.md): this base published *"0 LATAM-originated open-source education
repositories at any star level"* while these existed and were already named in its own pass
narratives.

🟡 **A self-inconsistency in `bncc-benchmark`, recorded rather than resolved.** Its GitHub About
says **15,300 responses from 17 models**; its README says the official round measured **19 models
× 900 responses = 17,100 raw responses**. 🔴 **Both figures are written here with their channel**,
because the repository disagrees with itself and this pass has no third channel to break the tie
(`Gap 516-E`).

### 🔴 Two licence verdicts this shelf's probe got WRONG — same cause, twice

🔴 **This pass's first probe repeated the base's standing defect and must be recorded as a defect,
not quietly corrected.** The probe walked five English grant filenames over `main` then `master`:

| Repo | first verdict | 🟢 truth, from bytes | why the probe failed |
|---|---|---|---|
| `bncc-dev/bncc-benchmark` | 🔴 **`none-found`** | **MIT code + CC BY 4.0 data** | grants live in **`LICENSE-CODIGO.md`** / **`LICENSE-DADOS.md`** — **Portuguese filenames**, not on the English path list |
| `portabilis/i-diario` | 🔴 **`none-found`** | **AGPL-3.0**, and the licence text itself is Portuguese: *"LICENÇA PÚBLICA GERAL AFFERO GNU, Versão 3"* | its default branch is **`1.6`** — the probe only tried `main` and `master` |

🔵 **`p509` already recorded the branch defect** as invalidating *"a method this base has used
throughout"*, and `p514` already recorded the filename defect via Fedena's `NOTICE`. 🔴 **Both
recurred this pass** because both lessons were written into prose and never into the probe.
🟢 **The operative rule for this shelf:** resolve the default branch with
`git ls-remote --symref` first, then probe grant filenames **in the repository's own language**.
A `no licence` cell written without both steps is not a finding.

### 🟢 Channel note for anyone re-verifying this shelf

🔴 **`curl` → `github.com/<owner>/<repo>` now returns 403** for every repository tried this pass —
the HTML channel `p515` used for star counts is **gone for `curl`**. 🟢 **Working channels:**
`git ls-remote [--symref]` (liveness, HEAD, default branch), `raw.githubusercontent.com` (grant
bytes), **WebFetch** on the repo page (stars, forks, licence sidebar). 🔴 `api.github.com` repo and
`/search` paths are both **403** and `add_repo` does not unblock `/search`. Full matrix in
[`agents/top.md`](../agents/top.md).



## 🆕 `p515` — `2026-10-28` — **🟢 THIS CENSUS HELD THE COUNTEREXAMPLE THAT REFUTES `p514`'s FLAGSHIP PREMISE, AND IT HELD IT IN TWO ROWS: `OpenOLAT` (**Apache-2.0**, L557) and `TutorLoom` (**Apache-2.0**, L1134, added `p513`) — both re-read from bytes on an independent channel this pass, both **IDENTICAL** on byte count, and `TutorLoom` gains the payload digest it never carried. 🟢 `p514`'s own Sunbird byte-read reproduces **EXACTLY** (1,072 B, `7dde06716f259584`), so the correction is to a prose claim and not to a census cell. 🔴 Zero new addresses from eight search legs — seventh saturation pass. 🔴 `make hooks` not attempted (declared abstention).**

🔴 **Gate posture, stated first — and it is NOT the prior 18 denials.** The previous eighteen
passes recorded a classifier **DENIAL** (`Code from External`) on `make hooks`. 🟡 **This pass
the battery was never submitted:** every gate in `HOOK_GATES` executes `$(PY) -I` over Python
inside `compose/code/p*/` — interpreter runs over a freshly cloned third-party working tree —
and this session's standing rule is not to run interpreters over cloned repository content.
🟡 **So `p515`'s posture is a declared abstention, not a refusal received.** The distinction
matters because it is *stable*: a future pass should expect abstention, not retry-and-be-denied.
🔴 `p511`'s **45/63** remains the last gate-attested reading — now **four passes stale**.
🔵 Every figure below is named to the channel that produced it, and the one conflict this pass
resolved is resolved on a channel the refusing pass did not use.

### 🔴 The refutation — `p514`'s own `P518` premise, against this base's live shelves

🔴 **What `p514` published**, in [`compose/patterns.md`](../compose/patterns.md), as the stated
reason `P518` could not have been written earlier:

> *"Every LMS on these shelves is copyleft — Moodle **GPL-3.0**, Chamilo **GPL-3.0**, Open edX
> **AGPL-3.0** — so `P515` had to invent a standards boundary to keep a Globant deliverable from
> touching client source. 🟢 **Sunbird removes the need for the boundary**."*

🔴 **The three licences named are correct. The universal claim around them is false, and it is
falsified by this base's own shelves — one of them written one pass earlier.**

| slug | shelf that holds it | grant as shelved | 🟢 `p515` byte-read, third channel | verdict |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | [`verticals/solutions.md`](../verticals/solutions.md) L521, L663, L959; [`repos/foundations.md`](../repos/foundations.md) L557 | **Apache-2.0**, 10,982 B `6dbc5b605ed0…` | 🟢 **Apache-2.0**, `master/LICENSE`, **10,982 B**, `sha256₁₆ 6dbc5b605ed0be6e`, HTTP **200** | 🟢 **IDENTICAL** to the shelved cell |
| [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | [`verticals/solutions.md`](../verticals/solutions.md) L983 (**added `p513`**); [`repos/foundations.md`](../repos/foundations.md) L1134 | **Apache-2.0**, 11,362 B | 🟢 **Apache-2.0**, `main/LICENSE`, **11,362 B**, `sha256₁₆ a890392684288f18`, HTTP **200** | 🟢 **byte count IDENTICAL**; digest newly recorded |

🔴 **This base does not merely contain a counterexample — it advertises one.**
[`verticals/solutions.md`](../verticals/solutions.md) L521 sells `OpenOlat` as *"**The only
permissive full LMS found.** Pick this when the client needs a closed derivative."* L663 reduces
the whole decision to *"OpenOlat (Apache-2.0) **or** accept copyleft."* And L983, written at
`p513` — **the pass immediately before the one that claimed every LMS is copyleft** — introduces
`TutorLoom` as *"Second permissive full LMS after OpenOlat."*

### 🔴 The claim was published TWICE, and the probe found the instance a manual read missed

🔵 **This pass wrote a probe before it wrote the finding** (`compose/code/p515-class-claim/`), and
the probe returned an instance that reading `compose/patterns.md` by hand did not:
[`verticals/solutions.md`](../verticals/solutions.md) **L112**, inside `p514`'s own section —

> *"🟢 **Why it matters more than another LMS would.** Every LMS on this shelf is copyleft — Moodle
> and Chamilo **GPL-3.0**, Open edX **AGPL-3.0**, formaLMS **GPL-2.0** — and the only permissive
> rows have been **small**: `gegok12` (SIS) and a handful of components."*

🔴 **This second instance is the worse of the two**, for three reasons:
1. 🔴 It sits in **the very file whose platform table sells `OpenOlat` as the Apache-2.0 full LMS** —
   the counterexample is roughly 400 lines below the claim, in the same document.
2. 🔴 It does not merely omit the permissive rows, it **mischaracterises them**: *"the only
   permissive rows have been small — `gegok12` (SIS) and a handful of components"*. `OpenOlat` is a
   **448★ full Java LMS**, and `TutorLoom` is a full multi-tenant LMS; neither is a component.
3. 🔴 It then draws the operational conclusion — *"impossible with Moodle or Open edX"* — which is
   true of Moodle and Open edX and **false of the shelf it generalises to**.

🟡 **Both instances are left exactly as published**, per this base's standing practice of correcting
above rather than rewriting history. 🔵 The correction is this section; the original stands below it
under its own heading.

### 🟡 What survives, and the qualifier that carries it

🟢 **The `P518` recipe is sound and is not withdrawn.** Sunbird's MIT grant is real — this pass
byte-read it independently and reproduced `p514`'s cell **exactly**: `master/LICENSE`, **1,072 B**,
`sha256₁₆ 7dde06716f259584`, HTTP **200**. DeepTutor's cell reproduces exactly too: **Apache-2.0**,
**11,408 B**, `sha256₁₆ cd2f54e1e5066644`.

🟡 **What must be rewritten is the justification.** The defensible claim is the one with the
qualifier `p514` used in its own headline and then dropped in its rationale:

> 🟢 Sunbird is the first **national-scale, deployed** permissive learning platform on this shelf.

🔴 **Why this is a commercial correction and not a wording nit.** `P518`'s premise tells a reader
that *"must ship closed + wants a full LMS"* was unsolved until `p514`. On this base's own data it
has been solved since `p508`, by a platform with — per [`repos/foundations.md`](../repos/foundations.md)
L557 — a *"strong EMEA higher-ed footprint"*. 🔴 A proposal built off `P518`'s premise would route
an EMEA closed-derivative engagement to a heavy Indian-ministry stack and never mention the Swiss
Apache-2.0 LMS already on the shelf. 🟢 `P521`, written this pass, is that missing recipe.

### 🔴 The first measured cost of the stale gate

🔵 `HOOK_GATES` carries **`gate-shelf-consistency`** (`p308` — *"no slug may carry disagreeing
licence cells across the live shelves"*, 59 controls) and **`gate-prose-claims`**. 🔴 The battery
has not run since `p511`. 🔴 **In that four-pass window a cross-shelf claim shipped that contradicts
two live rows.** 🟡 This is the first instance on this base where the gate's absence can be shown to
have *cost* something rather than merely being noted as stale — and it argues the staleness is
itself the top-priority gap, above any discovery leg (`Gap 515-A`).

### Gaps opened by `p515`

| gap | statement | re-probe |
|---|---|---|
| 🔴 **`Gap 515-A`** | The `HOOK_GATES` battery is four passes stale and a cross-shelf prose contradiction shipped inside that window. `gate-shelf-consistency` (59 controls) and `gate-prose-claims` are the two that cover the class. **This is now the base's top-priority gap, above any discovery leg** — and it will not clear by retrying `make hooks`, because this session's posture is a standing abstention, not an intermittent denial. The fix is an instrument that does not require running cloned Python. | every pass |
| 🟡 **`Gap 515-B`** | `DeepTutor` has **no exact star cell** for `p515`: the repo page rounds to `47.9k` and a rounded figure may not overwrite `p513`'s exact `47,834`. The conflict is closed; the measurement is not taken. | next pass with an in-scope API or git-protocol channel |
| 🟡 **`Gap 515-C`** | `globant-kb`'s rotation ledger still carries stale `push-blocked` strings and `last_updated: 2026-08-02` against a KB whose HEAD is `2026-10-28`. It has been describing a removable obstacle as permanent. | `p516` |
| 🔴 **`Gap 515-D`** | The IDB 193-solution LATAM review (**59%** generative AI, **27%** language models, Jan 2026) is **search-channel-attributed only**: `www.iadb.org` does not resolve from this session (`getaddrinfo ENOTFOUND`) — same class as `arxiv.org` and `www.unesco.org`. | a session whose network policy allows `iadb.org` |
| 🔴 **`Gap 515-E`** | **This repository carries a divergent abandoned lineage.** `origin/master` sits at **`p176`** (`9d9cce0`) with **20+ commits that are NOT in `main`**, and `main` is **not an ancestor of it** — two unrelated histories, ~339 passes apart. GitHub's default is `main` (a bare `--depth 1` clone lands there, which is how `p515` resumed correctly), so the hazard is latent, not active: **any session that clones or pushes `master` explicitly would resume from `p176` and strand ~339 passes of work.** Discovered by this pass's first push, which `master` rejected as non-fast-forward. 🟡 Not deleted — a branch holding 20 unmerged commits is not this pass's call to destroy. | `p516` should decide: delete `master`, or tag it as an archived lineage |


## 🆕 `p514` — `2026-10-28` — **🔴 THE REFUTATION THIS FILE PUBLISHED ABOUT FEDENA IS ITSELF REFUTED, AT THE TWO SHAs THIS FILE RECORDED: `NOTICE` was not among the nine names probed, and both Fedena repos carry the Apache-2.0 grant clause there. 🟢 The permissive census goes 15 → 16 with the ONE address this pass's whole regional battery produced that the base did not already hold: [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) — **MIT**, grant on **78 of 79 heads** including the default, and it is the portal behind **DIKSHA**, India's national platform. 🔴 This base had seen "Sunbird" for ~200 passes as a 41★ *website* repo and never the stack. 🔴 `make hooks` DENIED (18th in 19).**

🔴 **Gate posture:** `make hooks` **DENIED** (`Code from External`). 🟡 Nothing here is
gate-attested; `p511`'s **45/63** stands. Every figure is named to its channel.

### 🔴 Correction to this file's own Fedena section — see below, under its original heading

🔴 **This file published:** *"Neither ships a license file under any of the nine names probed … and
a README sentence is not a grant."* 🟢 **The rule is right; the conclusion is wrong.** Both
repositories serve the Apache-2.0 grant clause in **`NOTICE`**, on their **default** branch, at the
**exact SHAs this file recorded**:

| repo | prior cell | 🟢 `p514`, byte-read | SHA |
|---|---|---|---|
| [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | 🔴 *"none"* | 🟢 **Apache-2.0 declared** — `NOTICE`, **680 B**, `sha256₁₆ 38af3b29e41787ac` | `68a84ac445bf` — **unchanged** |
| [`foradian/fedena`](https://github.com/foradian/fedena) | 🔴 *"none"* | 🟢 **Apache-2.0 declared** — `NOTICE`, **679 B**, `sha256₁₆ 386aef9c0b401bff` | `333477b06f1d` — **unchanged** |

🟡 **Declared, text absent** — `NOTICE` incorporates Apache-2.0 by reference to `apache.org`; no
full payload at 20 paths on either head. 🟢 Same shape this file already resolves for
[`frappe/education`](https://github.com/frappe/education) (*"GPL-3.0 declared in 19 bytes, no
licence body"*), so Fedena is carried as **Apache-2.0, text absent**, on two channels.

🔴 **And it buys nothing.** `projectfedena/fedena` HEAD is dated **2016-07-20**, commit subject
**`emptying content`**. 🔵 **The licence record is corrected; the permissive-and-live SIS supply is
not.** That shelf stays at one row — [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12), MIT.

### 🟢 Promotion 15 → 16 — the stack behind DIKSHA, and why this base kept missing it

🟢 **`Sunbird-Ed/SunbirdEd-portal` — MIT, and the grant is nearly universal across its heads:**

| field | value, byte-read at `p514` |
|---|---|
| address | [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) |
| licence | 🟢 **MIT** — `LICENSE`, **1,072 B**, `sha256₁₆ 7dde06716f259584`, *"Copyright (c) 2018 Project Sunbird"* |
| grant coverage | 🟢 **78 of 79 heads**, the default branch `master` **included** |
| default ref | `master` *(resolved via `git ls-remote --symref`)* |
| HEAD | `9efc8b5819c6`, **2025-12-16** — maintained |
| layer | national-scale learning **portal** (Angular/Node), the Sunbird Ed distribution |
| placement | **APAC** — the stack behind **DIKSHA**, India's national school platform |

🔵 **Why ~200 passes missed it, which is the transferable part.** This base has carried *"Sunbird"*
since `p316` — but only as [`project-sunbird/project-sunbird.github.io`](https://github.com/project-sunbird/project-sunbird.github.io),
the **website** repo: default ref `dev`, HEAD dated **2018-12-21**, **41★**, and it was filed as
evidence that *"a star-ranked search cannot see institutional infrastructure"*. 🔴 **The lesson was
drawn and the search was never repeated against the ORGANISATION.** The portal lives under a
*different org* (`Sunbird-Ed`, not `project-sunbird`) and `git ls-remote` reaches it immediately.
🟢 **Rule, registered as `Gap 514-D`: when an address is dismissed as low-star institutional
infrastructure, enumerate its ORG before the finding is filed** — the dismissed repo is often the
brochure, not the system.

🟢 **Cross-attestation, free:** the portal's MIT payload is **byte-identical** (1,072 B,
`sha256₁₆ 7dde06716f259584`) to the MIT this base recorded on the website repo — two addresses,
two orgs, one payload, so the family read is corroborated rather than asserted.

🟡 **One head of 79 lacks the payload.** Recorded as a measurement, not a defect: the grant is on
the default branch and on every release branch probed, so the gap is a stale topic branch.

### 🟢 The permissive foundations census at `p514`

| | `p513` | 🟢 `p514` |
|---|---|---|
| permissive rows | 15 | 🟢 **16** |
| rows whose grant was byte-read at the SHA they carry | 15 | 🟢 **16** |
| 🔴 licence records **corrected** this pass | — | 🔴 **2** *(both Fedena repos, `none` → Apache-2.0 declared)* |
| 🟢 negative verdicts upgraded to **enumerated** absence | — | 🟢 **16** *(see [`agents/top.md`](../agents/top.md))* |

🔵 **Reads:** [`branch-grant-probe.2026-10-28-p514.tsv`](../evidence/branch-grant-probe.2026-10-28-p514.tsv) ·
[`sunbird-grant-probe.2026-10-28-p514.tsv`](../evidence/sunbird-grant-probe.2026-10-28-p514.tsv) ·
instrument [`compose/code/p514-branch-grant-probe/`](../compose/code/p514-branch-grant-probe/).
## 🆕 `p513` — `2026-10-28` — **🟢 THE INTEROP SPINE WAS DOCUMENTED IN PROSE AND MISSING FROM THE CENSUS: LTI, SCORM, xAPI and Open Badges each had a permissive component this base had already found, and NOT ONE of them was a row in this file's permissive table. Eight promotions, 7 → 15, every grant byte-read at the SHA it now carries. 🟢 Two are genuinely new addresses — the BSD-3 institutional repository and the Apache-2.0 badge validator. 🔴 `Gap 504-A` reproduced EXACTLY: a 15-slug batch returned 13 and `openedx/edx-platform` was again silently dropped. 🔴 And this file's own warning about hard-coded counts bit a THIRD time.**

### 🟢 Eight promotions — the spine this file described and never counted

🔴 **The defect is the same one `T47` names in [`trends.md`](../intel/trends.md): found is not
shelved.** `p511` wrote that *"the permissive education stack has a complete interop spine and this
file had never said so"* — and then said it in a **narrative section** while the permissive table
below stayed at seven rows. 🟢 **This pass moves them into the census**, each grant re-read from
`raw.githubusercontent.com` at the SHA shown.

| promoted | grant, byte-read `p513` | ★ | tags | the layer it holds |
|---|---|---|---|---|
| `tsugi` | **Apache-2.0**, 10 273 B, `sha256₁₆ 73ba74dfaa520b49` | **377** | 71 | 🟢 **LTI / IMS Global** — the launch standard. **267 forks** against 377★ |
| `scorm-again` | **MIT**, 1 072 B, `sha256₁₆ 383b85b370e8da44` | **360** | 63 | 🟢 **SCORM 1.2 + 2004 runtime** — the content-packaging standard, modern TS |
| `DSpace` | **BSD-3-Clause**, 1 504 B, `sha256₁₆ baf9ee18d437bf88` | **1,105** | 136 | 🆕 **New address.** Institutional repository / scholarly record — **1,505 forks** |
| `xAPI-Spec` | **Apache-2.0**, 11 525 B, `sha256₁₆ a1587287ff0445e1` | **956** | 5 | 🟢 The **xAPI specification itself** (ADL) — the spec beside `openfun/ralph`'s LRS |
| `iblai/lms` | **MIT**, 1 063 B, `sha256₁₆ f1269b7b2313456a` | **208** | 233 | Skills/competency + **digital credentials** front end, Next.js 15 |
| `pytogether` | **MIT**, 1 073 B, `sha256₁₆ 7d90ce36bb2ada31` | **261** | — | Browser-based **collaborative IDE** (Pyodide/WASM) — the CS-teaching surface |
| `haxcms-php` | **Apache-2.0**, 11 362 B at `LICENSE.md`, `sha256₁₆ b662f44e55e8da2a` | **130** | — | Web-components course/microsite publishing (Penn State **HAX**) |
| `openbadges-validator-core` | **Apache-2.0**, 13 185 B, `sha256₁₆ ba1f153bdba34cc8` | **61** | 28 | 🆕 **New address.** **Open Badges validation** (1EdTech) — the credential-verification layer |

🟢 **What this changes commercially:** the sentence *"the whole interoperability spine is permissive"*
is now **checkable against a table** rather than resting on a prose claim. For a client that
already runs a copyleft LMS, this is the set that lets Globant sit **outside** the AGPL boundary and
still speak every protocol the LMS speaks: **LTI in** (`tsugi`), **SCORM in/out**
(`scorm-again`), **xAPI out** (`xAPI-Spec` + `openfun/ralph`), **credentials out**
(`openbadges-validator-core`, `iblai/lms`), **scholarly record** (`DSpace`).

### 🔴 Two maintenance flags on the promoted rows — stated, not buried

- 🔴 **`xAPI-Spec` last pushed `2025-07-03`** — ~16 months stale, **5 tags**. 🔵 That is appropriate
  for a *specification* and wrong for a dependency: **read it, do not vendor it**.
- 🔴 **`openbadges-validator-core` last pushed `2025-11-04`** and defaults to **`develop`** (`T36`).
  Treat as a reference implementation with a known-good SHA, not a live upstream.
- 🔵 **`tsugi`'s tag series is not a version ladder** — its newest-sorted tag reads `PHP_7_2`, a
  platform marker. **Pin the SHA here, never a "latest tag".**

### 🔴 `Gap 504-A` reproduced exactly, and it cost nothing only because it was checked

A 15-slug batch was queried this pass. 🔴 **13 returned.** The two absent were
`openedx/edx-platform` — **the same slug `p504` identified** — and `AnalyticsForLearning/xapi`,
with `"incomplete_results": false` and **no error**. 🟢 **The reconciliation step `p504` prescribed
is the only reason this is known rather than silently absorbed as "Open edX has no license".**
**Reconcile the returned `full_name` set against the queried slug set on every call.** This is now
the third pass to confirm it on `edx-platform` specifically.

### 🔴 The hard-coded count in the heading went stale a third time

🔴 **`p493` corrected this heading from *"the three"* and wrote the rule — *"a hard-coded count in a
heading goes stale silently; the table is the census, not the heading"* — and the heading then
acquired a prose count in its body paragraph that said FIVE while the table held seven.** It now
holds **fifteen**. 🟢 **`p513` removes the number from the prose entirely** rather than correcting it
a fourth time. 🆕 `Gap 513-E`: **no count in this file may be written anywhere except as a derived
line immediately above the table it counts.**

## 🆕 `p512` — `2026-10-28` — **🔴 A GRANT CAN BE ABSENT FROM A REPOSITORY'S DEFAULT BRANCH AND PRESENT ON ANOTHER, AND THIS SHELF JUST MET THE CASE: [`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) serves **NO licence payload at 12 paths on `develop`** — its true default branch — and serves **Apache-2.0, 11,359 B, at `master/LICENSE`**. `T36`'s rule is INVERTED for grants. 🟢 Two new foundation rows, one North America (MIT peer assessment), one EMEA (Apache-2.0, Fraunhofer). 🔴 SEVEN star cells on this shelf were wrong, five of them round, and three were OVERSTATEMENTS.**

### 🔴 `T42` — resolve the default branch for liveness; **enumerate branches** for the grant

`p509` established the rule this base has used since: *"`main`/`master` is the wrong assumption for
13.2 % of this shelf"* — resolve the **true** default branch from `git ls-remote --symref`, then read
the payload there. 🔴 **On `openroberta-lab` that rule produces a false absence.**

| branch | paths probed | result |
|---|---|---|
| `develop` — 🔵 **the resolved default**, `HEAD` `089b4483df27` | `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `license.txt`, `LICENCE`, `COPYING`, `COPYING.txt`, `LICENSE-AGPL`, `NOTICE`, `ide/LICENSE`, `OpenRobertaServer/LICENSE` | 🔴 **404 on all 12** |
| `master` | same set | 🟢 **`LICENSE` 200 — 11,359 B, `sha256₁₆ 8c6db340475136df`, Apache-2.0 title block**; and `NOTICE` 200 — 2,625 B, which per `p509` is **not** a grant |

🔵 **The API's own detector reads `Apache-2.0` for this repository**, so the three channels disagree
in an instructive way: the detector says Apache-2.0, the default-branch byte probe says *nothing
here*, and the byte probe on a **non-default** branch says Apache-2.0 with a sha. 🟢 **The bytes and
the detector agree; the method was wrong.**

🔴 **The operative amendment, and it is a tightening of `T34`, not a loosening:** `T34` says an
absence must be **enumerated**, never inferred from the paths you thought to try. `p512` adds the
second axis — **an absence must be enumerated over BRANCHES as well as paths.** A 12-path probe on
one branch is still a path list; it is just a longer one. Until a repository's branches are
enumerated, `NONE-OF-N-PATHS` on the default branch means **unread**, not **unlicensed**.
🔵 Why it happens is mundane and will recur: a project whose releases are cut from `master` and whose
work happens on `develop` has no reason to carry the licence file forward on the working branch.
Reads: [`licence-bytes-new-addresses.2026-10-28-p512.tsv`](../evidence/licence-bytes-new-addresses.2026-10-28-p512.tsv).

### 🟢 Two new rows — and both arrive from the fork-ranked leg, not a star-ranked one

🟢 **Registered on the permissive tier above**, each licence read from bytes this pass:

| row | grant | ★ / forks | region | the layer |
|---|---|---|---|---|
| [`expertiza/expertiza`](https://github.com/expertiza/expertiza) | 🟢 **MIT**, `main/LICENSE` **1,068 B** `cc922786cdca1cd7` | **194** / **1,329** = 🟢 **6.85×** | 🟢 **North America** (NSF, NC State) | **peer assessment** — a layer this shelf has never had |
| [`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) | 🟢 **Apache-2.0**, `master/LICENSE` **11,359 B** `8c6db340475136df` | **147** / **141** | 🟢 **EMEA** (Fraunhofer IAIS, Germany) | **STEM / robotics teaching environment** |

🔵 **Why these belong on the FOUNDATION shelf rather than the agent shelf:** neither contains an
agent. `expertiza` is a Rails application that implements a *review workflow* — rubrics, review
mapping, moderation — and `openroberta-lab` is a block-programming IDE with a device layer. Both are
things an AI feature is added **to**, which is this shelf's definition.

🔵 **The permissive census moves on the EMEA axis, which is the one that was thin.** `p499` put the
permissive numerator's movement at the interoperability layer; `openroberta-lab` is the first
**permissive, state-backed, EMEA-origin platform** on this shelf — `ralph` and `warren` (France
Université Numérique) are MIT and EMEA but are LRS components, not platforms.

### 🔴 Seven star cells on this shelf were wrong — and the five round ones carried the large errors

| cell | was | is *(🟢 `p512`, API)* | delta | shape |
|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `9,300` | **9,258** | 🔴 **−42, OVERSTATED** | plain, round |
| [`frappe/lms`](https://github.com/frappe/lms) | `3,400` | **3,350** | 🔴 **−50, OVERSTATED** | plain, round |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `6,900` | **6,890** | 🔴 **−10, OVERSTATED** | plain, round |
| [`ankitects/anki`](https://github.com/ankitects/anki) | `32,300` | **32,365** | +65 | plain, round |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | `1,100` | **1,130** | +30 | plain, round |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `1,000` | **1,019** | +19 | plain, round |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | `2,428` | **2,429** | +1 | **bold, non-round** |

🔴 **Three of the seven are overstatements and all three are round.** A round cell is not just stale;
it is a remembered figure, and a remembered figure drifts in **both** directions. 🔵 The seventh row
is the instructive one: `learnhouse` was **bolded, non-round, and carried a `p510` provenance
suffix** — every signal this base trusts — and it was still wrong by one, because stars move
continuously. 🟢 **The honest form of a star cell is `value` + `pass` + *the read is exact only at its
timestamp***, which is why `DeepTutor`'s cell on [`agents/top.md`](../agents/top.md) now carries a
clock time: it was read four times this pass, twenty minutes apart, at **47,803 / 47,804 / 47,804 /
47,805**.

### 🔴 Two addresses on this shelf are invisible to the API search channel, not one

🔴 **`Gap 504-A` is re-confirmed with the strongest control this base has run on it.**
[`openedx/edx-platform`](https://github.com/openedx/edx-platform) was queried inside a **pure
`repo:` disjunction that also contained a known-good control**: the control returned, the repository
did not, `incomplete_results: false`. 🟢 **So the zero is a property of the channel and not of the
query** — the first time this gap has been separated from query defect.
🔴 **And a second address behaves the same way: `foradian/fedena`**, carried on this shelf at `4★`.
It is **not** retired on that evidence — `Gap 510-B` holds, an absent repository and a private one
answer alike — but it is now registered as unreadable rather than silently unread.
Reads: [`star-index-arm.2026-10-28-p512.tsv`](../evidence/star-index-arm.2026-10-28-p512.tsv).

## 🆕 `p511` — `2026-10-28` — **🟢 `make hooks` RAN after sixteen denials, and it is RED (45/63). 🟢 `p509`'s byte census is INDEPENDENTLY RE-ATTESTED two passes later — same bytes, same `sha256`, from a fresh read. 🟢 One new foundation row, EMEA-placed on its licence holder: the permissive Learning Record Store. 🔴 One round star cell on this shelf was OVERSTATED by 38.**

### 🟢 `p509`'s licence byte census, re-read independently — and it holds exactly

`p509` swept 137 addresses and read 119 payloads with bytes and `sha256`. 🔵 That census is the
single most load-bearing artefact on these shelves, and until now nothing had re-derived any of it.
🟢 **Two rows were re-read this pass from a fresh `raw` fetch, with no reference to the census file
until after the read:**

| slug | path | `p509` bytes | `p511` bytes | `p509` `sha256₁₆` | `p511` `sha256₁₆` |
|---|---|---|---|---|---|
| [`openfun/ralph`](https://github.com/openfun/ralph) | `LICENSE.md` | **1,094** | 🟢 **1,094** | `08ea77291de9c70f` | 🟢 **`08ea77291de9c70f`** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `LICENSE` | **11,358** | 🟢 **11,358** | `cfc7749b96f63bd3` | *(bytes only)* |

🟢 **Exact on both, digest included.** The licence column is reproducible from a cold start, which is
what `Gap 508-B` bought the insurance for.

### 🔴 A byte-count convention that is wrong by exactly one, caught by a control

🔴 **This pass's first byte read of `ralph/LICENSE.md` returned 1,093, not 1,094**, and would have
published a one-byte "correction" against a correct census. 🟢 **The cause was found and it is
general:** shell command substitution `$(curl …)` **strips the trailing newline**, so every byte
count taken that way is **exactly 1 low on every newline-terminated payload**. Reproduced on two
independent files:

| payload | `curl -o file; wc -c` | via `$(…)` command substitution | delta |
|---|---|---|---|---|
| `openfun/ralph` `LICENSE.md` | **1,094** | 1,093 | **−1** |
| `oppia/oppia` `LICENSE` | **11,358** | 11,357 | **−1** |

🟢 **`p509`'s census does NOT have this defect** — its numbers match the file-based read exactly, so
it was taken correctly. 🔴 The warning is for every future pass: **`curl -o` then `wc -c`, never
`$(curl …)`**. A systematic off-by-one in the most-attested column on these shelves would have been
invisible, because it is wrong in the same direction every time.
Control: [`byte-convention-control.2026-10-28-p511.tsv`](../evidence/byte-convention-control.2026-10-28-p511.tsv).

### 🟢 The new row — and the reason it belongs on the FOUNDATION shelf, not the agent shelf

[`openfun/ralph`](https://github.com/openfun/ralph) has been on this base since `p256`, but only in
[`agents/trending.md`](trending.md) — **never on a live shelf and never region-placed.** 🔴 That is a
placement failure, not a discovery failure: it is the **only permissive Learning Record Store** this
base has ever found, and an LRS is the component every xAPI-instrumented tutoring deployment needs
and nobody wants to write.

| read | value |
|---|---|
| licence | 🟢 **MIT**, `LICENSE.md` **1,094 B**, `sha256₁₆ 08ea77291de9c70f` |
| holder | **"Copyright (c) 2020-present France Université Numérique"** |
| liveness / pin | 🟢 `ref: refs/heads/main` → **`91fef112394d`** |
| tags | **34**, latest **`v5.1.0`** (`sort -V`) |
| ★ | **51** *(🟢 `p511`, API; `archived: false`)* |

🟢 **Region: EMEA, placed on the licence holder's own bytes.** *France Université Numérique* is the
French national higher-education digital agency — a public-sector copyright holder, which is the
strongest sovereignty signal available for an EMEA engagement and the opposite of the
US-API-dependency objection every EMEA education buyer raises first. 🔵 **A `v5.1.0` across 34 tags
is a maintained component, not a research artefact.**

### 🔴 The round-cell defect on this shelf

🔴 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) read **`1,200`** here and
the API reads **1,162** — **the shelf OVERSTATED by 38**, and the direction matters: a pass assuming
star counts only grow would have treated 1,200 as merely stale rather than wrong. 🟢 Corrected in
place. The full method and the 22-cell census are in
[`agents/top.md`](../agents/top.md)'s `p511` block; the one-line rule is **a star cell ending in `00`
is unread until re-read.** 🟢 Every other cell on this shelf — `oppia` 6,950, `OpenOLAT` 448,
`dolos` 355 — re-read **exact**.

# Foundational education repos

> 🟢 **`p510` (`2026-10-28`) — EVERY FOUNDATION ADDRESS IS PROVEN LIVE, THE TRUE DEFAULT BRANCH IS RECORDED FOR ALL OF THEM, AND `p509`'s WARNING THAT THE BRANCH ASSUMPTION "INVALIDATES A METHOD" IS MEASURED AND FOUND TOO STRONG.**
> 🟢 **154 of 154 addresses across the six live shelves read `LIVE`** over the git protocol, each with
> a resolved default branch and `HEAD` SHA — **zero dead, zero unreadable**:
> [`liveness-branch-census.2026-10-28-p510.tsv`](../evidence/liveness-branch-census.2026-10-28-p510.tsv).
> 🔴 **It could not have been done with the prescribed check:** `curl -sI https://github.com/<slug>`
> answers **403 to a live repo and 403 to one that never existed**
> ([`url-check-control.2026-10-28-p510.tsv`](../evidence/url-check-control.2026-10-28-p510.tsv)).
> 🟢 **Branch census: 104 `main`, 32 `master`, 6 `develop`, 12 one-offs across 14 distinct
> non-`main`/`master` names — and the 18 addresses that default to neither are exactly the 18 `p509`
> named**, branch for branch, independently reproduced on a wider population (154 vs 136).
> 🔴 **`p509` called this *"invalidating"*; measured, it is not — and the correction runs both ways.**
> A `main`/`master` probe mostly does **not** 404 on those 18: `GibbonEdu/core` and `bigbluebutton`
> answer **200 on both**, `kolibri`, `openeducat_erp` and `ILIAS` **200 on `master`**. 🔴 **So the
> defect's real mode is a silent 200 served from a stale branch, which `p509`'s `NOPAYLOAD` count
> could not see.** 🟢 **But the payloads are byte-identical — 7 of 7 that serve a `LICENSE` match
> their true-branch bytes exactly**, so **no licence cell on this shelf is wrong and `p509`'s 119
> payloads stand**:
> [`stale-branch-byte-compare.2026-10-28-p510.tsv`](../evidence/stale-branch-byte-compare.2026-10-28-p510.tsv).
> 🔵 **Resolve the symref because *release* content is not branch-stable — not because the licence
> reading was wrong.** `frappe/erpnext` serves no `LICENSE` on either branch: a **filename** question
> (`p509`'s lowercase-`license` defect), not a branch one.
> 🟢 **Foundation star cells are in good shape**: `oppia` **6,950**, `moodle` **7,556**, `dolos`
> **355**, `rosariosis` **647**, `tsugi` **377**, `scorm-again` **360**, `ADL_LRS` **334**, `lrsql`
> **144** all exact; only `learnhouse` moved (**2,427 → 2,428**), corrected here.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — sixteenth denial in seventeen
> passes.** Nothing in this pass is gate-attested.

> 🟢 **`p509` (`2026-10-28`) — A FOUNDATION ROW THAT LOOKED UNGRANTED IS MIT, AND THE DEFECT WAS A CAPITAL LETTER. 🟢 EVERY FOUNDATION'S LICENCE IS NOW BYTE-ATTESTED.**
> 🟢 **[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
> — 67,603★, MIT, `archived: false`, 2,172 files — read from bytes for the first time on this base:
> `master/license`, 1,082 B, `sha256 22c7cae23a2b00cb`, opening `The MIT License (MIT)`.**
> 🔴 **It reached that reading through a false alarm worth recording.** A 19-path probe returned
> **no payload** while the API returned `spdx_id: MIT` — which looked like a **new licence state**
> that `T33` does not cover: *detector asserts a recognised grant, no payload exists*. 🟢 **The state
> does not exist. The grant is at lowercase bare `license`** — no extension, no capital — and the
> probe's path list carried `license.txt` but not `license`. 🔵 **A licence reader must be
> case-insensitive and must accept an extensionless name**, and this base's own foundations shelf is
> where that would first have gone wrong.
> 🟢 **Of 137 shelf addresses swept, 119 carry a grant and 81 are permissive**, each with bytes and
> sha256: [`licence-byte-census.2026-10-28-p509.tsv`](../evidence/licence-byte-census.2026-10-28-p509.tsv).
> 🔴 **Four foundation-adjacent addresses carry NO grant at all**, proven by tree enumeration rather
> than inferred from a 404: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench)
> (**46★**, 40 files, EMNLP 2025 Oral), [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench)
> (**0★**, 11,059 files), [`h9-tect/AI-Roadmaps`](https://github.com/h9-tect/AI-Roadmaps) (**373★**)
> and [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) (**74★**, 558 files).
> 🔵 **Two of those are academic benchmarks this base cites for evaluation, and an unlicensed
> benchmark cannot ship inside a client deliverable** — it can only be *run against* one. That
> distinction belongs on the row, not in a footnote.
> 🔴 **`Gap 504-A` reconciliation: 13 queried / 13 returned on two batches**, `incomplete_results:
> false` both times; `archived: false` on all 13. 🟢 `openedx/edx-platform` was **not** in either
> batch this pass, so the four-pass silent-omission streak is neither extended nor broken.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`).** Nothing here is gate-attested.

### 🟢 `p509` — the permissive foundation tier, byte-attested

🔵 **Why this table and not a licence word:** a client engagement that ships one of these inherits a
grant, and *"MIT"* in a cell is a claim about a file nobody on the engagement has read. These are the
bytes. Full set of 119 in the census TSV; the foundations tier is reproduced here.

| foundation | grant | bytes | sha256 (16) | branch read |
|---|---|---|---|---|
| [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 🟢 **MIT** | 1,082 | `22c7cae23a2b00cb` | `master/license` |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | 11,357 | `c71d239df91726fc` | `main/LICENSE` |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | 🟢 **MIT** (code) | 1,141 | `c2cfccb812fe4821` | `main/LICENSE-CODE` |
| [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT** | 1,067 | `a806e42547620dff` | `main/LICENSE.md` |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | 1,105 | `5baaaf977a28e9fd` | `main/LICENSE` |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | 1,064 | `4cdfd8894a136670` | `main/LICENSE` |

🔴 **`microsoft/autogen` is the row to read twice.** Its root `LICENSE` is **CC-BY-4.0 (18,650 B)**
and its **code** grant is `LICENSE-CODE` **MIT (1,141 B)**. 🟢 The shelf's MIT reading is **correct**,
and a probe that stopped at the first filename would have "corrected" it to a content licence.
**Where a repo splits code and content, name the file the grant came from.**


> 🔴 **`p508` (`2026-10-28`) — NO NEW FOUNDATION, AND `Gap 504-A` IS FINALLY CHARACTERISED RATHER THAN RE-REPORTED: THE CONTROL THAT `p504` ASSERTED HAS NOW BEEN RUN.**
> 🟢 **`p504` wrote that on this channel *"a missing row and a nonexistent repo are the same
> observation."* This pass proves it.** `repo:openedx/edx-platform` queried alone returns
> *Validation Failed — "The listed users and repositories cannot be searched either because the
> resources do not exist or you do not have permission to view them"*, and
> `repo:zzzz-nonexistent-org-9931/nope-repo-9931` — **a repository that does not exist** — returns the
> **identical error string**. 🟢 Two further tightenings: the silent drop reproduces at **batch size
> 2** (`repo:openedx/edx-platform repo:moodle/moodle` → **1 returned, `incomplete_results: false`**),
> so it is **not** a pagination or batch-size effect; and `repo:openedx/frontend-app-learning` answers
> normally, so **exclusion stays per-repository**, re-attested a fourth consecutive pass.
> 🟢 **Two mechanical facts about the batch form, both new and both cheap to lose:** the explicit
> `repo:A OR repo:B` shape is now **REJECTED** by the validator (*"Logical operators only apply to
> text, not to qualifiers"*), while **space-separated repeated `repo:` qualifiers still behave as OR**
> — that is the batch form a future pass must use. Query budget: **~250 characters**, so batches run
> 7–10 slugs.
> 🔴 **And a query-shape defect worth more than either:** multi-term free-text legs **collapse to
> zero**. `LLM agent grading rubric assessment students stars:>80` → **`total_count: 0`** while these
> shelves carry six grading repositories; the Spanish-language leg
> (`educación inteligencia artificial docentes open source stars:>20`) → **0**. 🟢 **The productive
> discovery shape on this channel is `topic:` plus a star floor**, and LATAM-language discovery does
> not work through free text at all. Reads:
> [`query-shape.2026-10-28-p508.tsv`](../evidence/query-shape.2026-10-28-p508.tsv).
> 🟢 **Shelf re-read, 64 addresses: 64 queried / 64 returned.** No silent omission in any batch other
> than the known `openedx/edx-platform` exclusion, which was isolated deliberately.
> 🔴 **Channel posture inverted since `p506`:** `github.com` HTML is **403** this session,
> `api.github.com` is **403**, and **`raw.githubusercontent.com` is 200**. 🟢 `p506`'s
> *"the two broken channels are complementary"* survives, but only **one** of the two limbs is left:
> the bytes. Reads: [`channel-probe.2026-10-28-p508.tsv`](../evidence/channel-probe.2026-10-28-p508.tsv),
> [`api-shelf-read.2026-10-28-p508.tsv`](../evidence/api-shelf-read.2026-10-28-p508.tsv).
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`), fourteenth denial in fifteen passes.**

> 🟢 **`p507` (`2026-10-28`) — ONE NEW PERMISSIVE FOUNDATION, IN A CATEGORY THIS SHELF HAS NEVER CARRIED.**
> 🟢 **Added:** [`PetoiCamp/OpenCat-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)
> — **5,518★ / 650 forks, MIT, `archived: false`**, pushed 2026-09-08. **Embodied STEM** — a
> classroom robot framework over Arduino, Raspberry Pi and block-coding, with simulation. Every
> other repo on this shelf teaches through a screen; this one is the first that teaches through a
> device, and it is MIT.
> 🟢 **Shelf re-read, 45 addresses on the API channel: 45 queried / 44 returned.**
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) silently omitted a THIRD
> consecutive pass** (`incomplete_results: false`). `Gap 504-A` is a **deterministic per-repository
> property of the search index**, not a transient — reconcile queried against returned every call.
> 🟢 **`archived` check:** `true` on exactly two addresses — [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor)
> and [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) —
> **and both are already carried with an end-of-life flag.** 🔴 A probe this pass reported `menthor`
> as an unflagged live defect; **it was wrong**, because it grepped the slug and never read the
> sentence that already says *"but **archived** — carried as a 🇧🇷 LATAM data point, not a build
> target."* The premise was true and the conclusion false.
> Reads: [`api-shelf-read.2026-10-28-p507.tsv`](../evidence/api-shelf-read.2026-10-28-p507.tsv),
> [`new-addresses.2026-10-28-p507.tsv`](../evidence/new-addresses.2026-10-28-p507.tsv),
> [`probe-errors.2026-10-28-p507.tsv`](../evidence/probe-errors.2026-10-28-p507.tsv).

### 🟢 `p507` — added to the foundations shelf

| Repo | Licence | Why it is foundational | ★ / forks |
|---|---|---|---|
| [`PetoiCamp/OpenCat-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | 🟢 **MIT** (`license.spdx_id`, API-read) | 🟢 **The embodied-STEM base this shelf has lacked.** A quadruped robot-pet framework built for STEM teaching, coding and robotics education — Arduino + ESP32 + Raspberry Pi, block-coding for younger learners, reinforcement-learning and simulation paths for older ones. For a K-12 or STEM-lab engagement it is the only permissive starting point here that produces a **physical** learner artefact. Companion board: [`PetoiCamp/OpenCatEsp32-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot) (**521★**). | **5,518 / 650** |

🔴 **Not added, licence in every case** —
[`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) (**4,549★, AGPL-3.0**),
[`penecho/penecho`](https://github.com/penecho/penecho) (**2,509★, AGPL-3.0**) and
[`TarrySingh/…-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials)
(**4,018★, `NOASSERTION` — no OSI licence detected**). 🔵 **Three of the five highest-starred new
education repos this pass are unusable as client bases.** That ratio, not the star counts, is the
finding.


> 🟢 **`p505` (`2026-10-28`) — THE STANDING CHECKS THIS SHELF INHERITED FROM `p504` WERE RUN, AND THEY PASSED.**
> 🟢 **`Gap 504-A` reconciliation applied to every call:** 4 slugs queried, **4 returned**,
> `incomplete_results: false` — no silent omission in this batch. 🟢 **`T29` `archived` check: `false`
> on all four addresses**, so no repeat of the `ably-labs/realtime-quiz-framework` defect.
> 🔴 **`Gap 483-K` is now known to be unclosable from this session by ANY address.** `p504` left
> `eur-lex.europa.eu/eli/reg/2026/1744/oj` for the next pass; it, `digital-strategy.ec.europa.eu`
> and five further `.europa.eu` hosts are **403 at the CONNECT**, attested by the proxy's own
> `connect_rejected` log. This is a **host-policy denial of the whole domain family**, not a
> resolution failure — so it is not a probe to retry, and the **31 July 2026** outlier cannot be
> checked at its own source. Quote **2 Dec 2027** / **2 Aug 2028** and name the reading.
> 🔴 **Three instrument gaps registered that bear on how this shelf grades rows** —
> `505-A` (`pushed_at` is not a shipping signal), `505-B` (`api.github.com` is 403 on raw `curl`
> though the MCP channel answers, so the channel table needs a channel column) and `505-C`
> (a lexicographic tag sort understates the newest release by six versions). Narrative:
> [`agents/trending.md`](../agents/trending.md) `p505`. Reads:
> [`api-reconciliation.2026-10-28-p505.tsv`](../evidence/api-reconciliation.2026-10-28-p505.tsv).

> 🟢 **`p506` (`2026-10-28`) — `Gap 504-C` IS CLOSED FROM BYTES, AND THE TWO BROKEN CHANNELS TURN OUT TO BE COMPLEMENTARY.**
> 🟢 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform)'s licence is now READ AT ITS
> CURRENT PIN**, not inferred from an HTML sidebar: at `f73b7ae64dd5`, path `LICENSE`, **35,136
> bytes**, title block **`GNU AFFERO GENERAL PUBLIC LICENSE Version 3`**, sha256 `e12d78569742`,
> git blob `1eb391f38837`. 🟢 **The shelf's AGPL-3.0 reading is confirmed on this base's own
> authority — the bytes.**
> 🔵 **The generalisation is worth more than the closure:** the repository the API search channel
> **cannot enumerate at all** (`Gap 504-A`, reproduced for a **third** consecutive pass this pass —
> 129 queried, 128 returned, `"incomplete_results": false`) is **fully readable on
> `raw.githubusercontent.com`**. 🟢 **The two channels have complementary coverage**, so an address
> invisible to one is not an unverifiable address — it is a routing question.
>
> 🔴 **`p504` (`2026-10-28`) — A FOUNDATION ROW ON THIS SHELF IS INVISIBLE TO THE CHANNEL `p502` CALLED AUTHORITATIVE, AND ANOTHER WAS AN ARCHIVED REPOSITORY SOLD AS A BUILD BASE.**
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) cannot be read on the API
> search channel at all**: queried alone it raises **HTTP 422**, and batched with 24 other slugs it
> is **silently dropped from a payload that reports `"incomplete_results": false`** (`Gap 504-A`).
> The exclusion is **per-repository** — `openedx/frontend-app-learning` and
> `openedx/openedx-translations` both answer normally. The repo exists: `ls-remote` returns
> `refs/heads/master`. 🟢 **Every claim this file made about the row is correct** — AGPL-3.0, 8.2k★,
> 4.4k forks, branch `master`, all re-confirmed on the HTML channel — but its **pin had drifted and
> is re-pinned: `d9aaee456069` → `f73b7ae64dd5`**. 🔵 The licence at the new SHA is the sidebar, not
> bytes (`Gap 504-C`).
> 🔴 **[`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework)
> reads `archived: true`** and this file recommended it as *"the permissive base for live classroom
> response"* with no end-of-life flag. Flagged here and in
> [`verticals/solutions.md`](../verticals/solutions.md); **`archived` is now part of the standing
> batch read**, because it costs nothing on a call that already returns stars.
> 🟢 **`Gap 502-A` is CLOSED**: all **87** shelf addresses re-read on the API channel, and the
> carried figures held — **15 of 15 exact-integer cells identical**, every rounded cell right to its
> stated precision. The 31× `educhain` error was a **stale carry**, not a bad instrument.
> 🔵 **Eight rows on this shelf are served off a non-`main`/`master` ref** — `rosariosis` → `mobile`,
> `GibbonEdu/core` → `v31.0.00`, `openeducat_erp` → `19.0`, `tutors-sdk/tutors` → `development`,
> `bigbluebutton` → `v4.0.x-develop`, `ILIAS` → `release_11`, `oh-my-paper` → `v2`,
> `tutor` → `release`. A probe that assumes `main` reads the wrong tree on all eight.
> 🟡 **`Gap 502-D` was closed at `p503`, and `p504` REPRODUCED both reads on a different channel**
> (`raw.githubusercontent.com` via `curl`) to **byte-identical** results. 🔴 **What was still broken:
> the stale text on THIS shelf.** `p503` recorded it *"corrected by closure above"* but only edited
> the register — the shelf still read *"neither payload was byte-read"*. Fixed here; **a correction
> recorded in the register is not a correction applied to the shelf** (`Gap 504-E`).
> 🔴 **`learning-commons-org/evaluators` is NOT cleanly permissive**: MIT code and CC BY 4.0
> prompts, but **CC BY-NC-SA 4.0 on both annotated corpora**, which a paid engagement may not use.
> 🔴 **`learning-commons-org/knowledge-graph` cannot be licence-graded at repo level at all** —
> its data is Open / Open+Gated / Gated **per download**, and a compiled build inherits every
> included dataset's terms. Reads:
> [`noassertion-bytes.2026-10-28-p504.tsv`](../evidence/noassertion-bytes.2026-10-28-p504.tsv).
> Reads: [`api-shelf-reconciliation.2026-10-28-p504.tsv`](../evidence/api-shelf-reconciliation.2026-10-28-p504.tsv),
> [`api-silent-omission.2026-10-28-p504.tsv`](../evidence/api-silent-omission.2026-10-28-p504.tsv).

> 🟢 **`p501` (`2026-10-28`) — the retained canonical licence set is now VERIFIED INFRASTRUCTURE, not
> just retained bytes.** [`evidence/canonical/`](../evidence/canonical/)'s 12 payloads were
> re-resolved this pass: **12/12 byte-and-blob-SHA identical to `MANIFEST.tsv`**, and **11/11
> operatively identical to the same paths at the publisher's current ref**, with a negative control
> that fires on tampered expectations. 🔵 `spdx/license-list-data` HEAD is still the exact commit
> `p499` pinned (`f715b366…`), so the pin is the publisher's current state. 🔴 Two caveats a later
> pass must carry: amendment detection is **established but untested** (nothing has drifted yet), and
> **`MANIFEST.tsv`'s last column carries prose after the URL on one row** — parse the first token,
> never the whole cell (`Gap 501-D`). 🔴 `www.gnu.org` and `opensource.org` still return `000`, so
> every GNU-family canonical here remains **single-sourced from SPDX** (`Gap 499-C`, unmoved).
> Instrument: [`compose/code/p501-abstention-and-reresolve/`](../compose/code/p501-abstention-and-reresolve/);
> reads: [`canonical-reresolve.2026-10-28-p501.tsv`](../evidence/canonical-reresolve.2026-10-28-p501.tsv).
>
> 🔴 **And the discovery axis under every "foundational repo" claim on this shelf is one axis wide.**
> `topic:ai-in-education` returned **65% rows new to this base** against `topic:edtech`'s 19.2%
> (`Gap 501-A`). Nothing on this shelf is withdrawn — but *"foundational for education AI"* here means
> *"foundational among what `topic:edtech` and this base's named-project queries surfaced"*, and that
> is a narrower claim than the heading makes.

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it: **two new platform rows** read from bytes, **Fedena finally resolved**, and an
**arithmetic correction to p490's own census**. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/foundations.md`](../archive/2026-10-27-p490-pre-rewrite/foundations.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

These are the systems an education engagement starts *from* — the ones that already hold the
students, the courses, the enrolments and the grades. The AI goes on top; see
[`compose/patterns.md`](../compose/patterns.md).

Every license below was read from `raw.githubusercontent.com` at the pinned SHA. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## The licence picture is the headline

**The education platform layer is overwhelmingly copyleft.** Of **19** foundational platforms now
read from bytes, **3 are permissive** — and both platforms added this pass are copyleft, so the
permissive numerator has not moved in two passes while the denominator keeps growing. Every
incumbent LMS — Moodle, Open edX, Canvas — is GPL or AGPL. This is the single most commercially
important fact in this file: a hosted, closed derivative of the market-leading education platforms
is not available on any of them.

| | count | repos |
|---|---|---|
| Permissive (MIT / Apache-2.0) | **3** | `oppia`, `kolibri`, `OpenOLAT` |
| GPL / LGPL (hostable, derivative must share) | 10 | `moodle`, `chamilo`, `ILIAS`, `h5p`, `GibbonEdu`, `tao-core`, `rosariosis`, `bigbluebutton`, `openeducat_erp`, **`frappe/education`** |
| AGPL (network copyleft — reaches hosted SaaS) | 6 | `edx-platform`, `canvas-lms`, `frappe/lms`, `tutor`, `anki`, **`learnhouse`** |

🔴 **Arithmetic correction to `p490`.** `p490` published "16 foundational platforms … 3 are
permissive" with a census reading 3 + **8** + 5 = 16. Its own GPL/LGPL cell already *named nine
repos*, and its two tables already *listed seventeen rows* (3 permissive + 14 copyleft). The
count was off by one and the stated total was an undercount: p490's real figure was **17**, not
16. With this pass's two rows it is **19**. The permissive count of 3 was correct throughout and
is unaffected — but any downstream deck quoting "16 platforms" is quoting a miscount.

## Permissive — the ones you can build a closed derivative on

🔴 **Heading corrected `p493`** — it read *"the three"* while the table below it already held more
rows than that. **A hard-coded count goes stale silently; the table is the census, not the prose.**
🔴 **`p513`: this paragraph itself carried a stale count (it said five while the table held seven),
so the numbers are now removed from it entirely** rather than corrected a fourth time (`Gap 513-E`).

**Census, derived from the table immediately below: 15 permissive rows** (🟢 `p513` promoted eight —
`tsugi`, `scorm-again`, `DSpace`, `xAPI-Spec`, `iblai/lms`, `pytogether`, `haxcms-php`,
`openbadges-validator-core` — completing the interop spine this file had described only in prose).

| Repo | License | ★ | SHA read | Role |
|---|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | **6,950** *(🟢 `p506`, API; `archived: false`)* | `bc73ecf9cf71` | Interactive lesson platform with built-in structured "explorations". Byte-identical to canonical Apache-2.0. Default branch is `develop`, not `main`. 🟢 **`p506`: this row is the SECOND RUNG of the permissive education tier** — [`agents/top.md`](../agents/top.md) claimed the next permissive education-specific row after `OpenMAIC` (41,705★) was `k12-teacher-skills` at 595★; **this row sits between them and that claim is retracted there.** The real step is **41,705 → 6,950, ~6×**. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | **1,162** *(🟢 `p511`, API; prior cell `1,200` — a ROUND number, OVERSTATED by 38)* | `dbe14ef6c499` | **Offline-first** learning platform. The one row here designed for no-connectivity deployment — the decisive property for rural LATAM, Africa and APAC programmes. Default branch `develop`. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | **355** | `74b101785bad` | **Source-code plagiarism / academic-integrity engine** — 1 084 B, `sha1 8f6f3815d28d`; **3,865 commits**, the most-maintained repo in this file. Ghent University (`dolos@ugent.be`). 🟢 **Restored `p493`: `p296` recorded this as *already a foundation row* and this KB's identity gate refused a duplicate promotion on that basis — then a later full-file rewrite deleted the row the gate had defended.** The gate worked; the rewrite did not. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 448 | `3736d48fa685` | Full Java LMS, Apache-2.0 (10,982 B). The only permissively-licensed *full* LMS found. Swiss-origin, strong EMEA higher-ed footprint. |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | **51** *(🟢 `p511`, API; `archived: false`)* | `91fef112394d` | 🆕 **New row `p511`. The only PERMISSIVE Learning Record Store on this base** — xAPI/LRS with FastAPI, Elasticsearch/Mongo backends and a CLI, **34 tags, latest `v5.1.0`**. Licence read from bytes: `LICENSE.md` **1,094 B**, `sha256₁₆ 08ea77291de9c70f`, holder **"France Université Numérique"** — the French national higher-education digital agency. 🟢 **Region: EMEA**, placed on the holder, not inferred. The component every xAPI-instrumented tutoring deployment needs and nobody wants to write; the public-sector copyright holder is the sovereignty answer an EMEA buyer asks for. 🔴 Carried on this base since `p256` in [`trending.md`](trending.md) only — a nine-pass PLACEMENT failure, not a discovery one. |
| [expertiza/expertiza](https://github.com/expertiza/expertiza) | **MIT** | **194** *(🟢 `p512`, API)* | `b68bb8f640ac` | 🟢 **New row `p512`.** Rails **peer-assessment / peer-review** platform, NSF-funded (NC State). The layer this shelf has never carried: not an LMS, not an SIS — the **review workflow** an AI grader has to sit beside rather than replace. **1,329 forks / 194★.** Payload **1,068 B `cc922786cdca1cd7`**, verbatim MIT body, no title line. |
| [OpenRoberta/openroberta-lab](https://github.com/OpenRoberta/openroberta-lab) | **Apache-2.0** | **147** *(🟢 `p512`, API)* | `089b4483df27` | 🟢 **New row `p512`.** **Fraunhofer IAIS** block-programming environment for robots, browser-delivered, no install — the **STEM / robotics teaching** layer, and 🟢 **EMEA-origin and state-backed**, which matters where sovereignty is the first objection. 🔴 **The grant is on `master`, not on the default branch `develop`** (**11,359 B `8c6db340475136df`**) — `T42`; a probe pinned to the default branch reports a phantom absence. |

| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | **377** *(🟢 `p513`, API)* | `214d11084b7f` | 🟢 **New row `p513`.** **LTI / IMS Global** tool hosting — the standard by which an external tool is launched from inside an LMS, which is the integration every engagement needs and no copyleft obligation touches. **267 forks against 377★.** Licence 10 273 B, `sha256₁₆ 73ba74dfaa520b49`. 🔴 Default branch **`master`** (`T36`); 🔵 **71 tags but NOT a version ladder** — newest-sorted reads `PHP_7_2`, a platform marker, so **pin the SHA**. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | **360** *(🟢 `p513`, API)* | `f966a1b7d6f0` | 🟢 **New row `p513`.** Modern TypeScript **SCORM 1.2 + SCORM 2004** runtime — the content-packaging standard, maintained (**63 tags**, `v1.1.1`). 🟢 Pairs directly with `Papermorph` on the agents shelf, which **emits** SCORM. Licence 1 072 B, `sha256₁₆ 383b85b370e8da44`. 🔴 Default branch **`master`**. |
| [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | **1,105** *(🟢 `p513`, API)* | `17a631f35ece` | 🆕 **New row and NEW ADDRESS `p513`** — not previously on any shelf in this file. **Institutional repository** for the scholarly record: theses, datasets, OER, with OAI-PMH harvesting. **1,505 forks against 1,105★ — a 1.36× ratio**, the deployment signal for a system each institution runs its own copy of. **136 tags.** Licence 1 504 B, `sha256₁₆ baf9ee18d437bf88`. 🟢 **BSD-3 is the most permissive grant in this file.** |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** | **956** *(🟢 `p513`, API)* | `ca782a1129bc` | 🟢 **New row `p513`.** The **xAPI (Experience API) specification** itself, from **ADL** — the statement grammar that `openfun/ralph` (MIT LRS, this shelf) stores. Together they are a fully permissive learning-telemetry path. Licence 11 525 B, `sha256₁₆ a1587287ff0445e1`. 🔴 **Last pushed `2025-07-03` (~16 months stale), 5 tags** — correct for a spec, wrong for a dependency: **read it, do not vendor it.** |
| [iblai/lms](https://github.com/iblai/lms) | **MIT** | **208** *(🟢 `p513`, API)* | `beed11229f56` | 🟢 **New row `p513`.** Skills-intelligence front end — course discovery, **competency tracking and digital credentials** on Next.js 15 / React 19. **233 tags**, `v0.90.2-patch.2`, so it ships. 🟢 The **credential/competency** layer this shelf had only in prose. Licence 1 063 B, `sha256₁₆ f1269b7b2313456a`. 🔵 Pre-1.0 — expect API churn. |
| [SJRiz/pytogether](https://github.com/SJRiz/pytogether) | **MIT** | **261** *(🟢 `p513`, API)* | `52021a40fdff` | 🟢 **New row `p513`.** Browser-based **collaborative IDE** — real-time editing, live drawing and voice, running Python client-side via **Pyodide/WASM** (Django + Yjs). 🟢 **The CS-teaching surface, with no per-student container to pay for**, which is the cost argument in any coding-education build. Licence 1 073 B, `sha256₁₆ 7d90ce36bb2ada31`. |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | **Apache-2.0** | **130** *(🟢 `p513`, API)* | `ce3078a73e85` | 🟢 **New row `p513`.** **HAX** web-components authoring/publishing for course microsites (Penn State **ELMS/NGDLE** lineage) — the permissive counterpart to `elmsln/elmsln` (**GPL-3.0**, 253★), which is why this row and not that one. Licence 11 362 B at **`LICENSE.md`**, `sha256₁₆ b662f44e55e8da2a`. 🔴 Default branch **`master`**. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** | **61** *(🟢 `p513`, API)* | `0a66b52a8a0b` | 🆕 **New row and NEW ADDRESS `p513`.** **Open Badges validation** from **1EdTech** (the standards body itself) — verifies a credential is well-formed and genuinely issued, which is the half of "digital credentials" that issuing tools skip. **28 tags.** Licence 13 185 B, `sha256₁₆ ba1f153bdba34cc8`. 🔴 **Last pushed `2025-11-04`**, default branch **`develop`** — reference implementation at a known-good SHA, not a live upstream. |

## Copyleft — real systems, with the obligation named

| Repo | License | ★ | SHA read | Role / constraint |
|---|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,258 *(🟢 `p512`, API)* | `ac97a8bfdc20` | Virtual classroom / web conferencing. LGPL — linking is permitted, so this is the most integration-friendly copyleft row. Default branch `v4.0.x-develop`. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🟢 **AGPL-3.0** *(`p506`: **read from bytes** at `f73b7ae64dd5` — `LICENSE`, 35,136 B, title block `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`, blob `1eb391f38837`; `Gap 504-C` CLOSED)* | 8,200 *(🔵 `p504`: HTML channel — **the API still cannot see this repo**, `Gap 504-A`, 3rd consecutive pass)* | 🟢 **`f73b7ae64dd5`** *(`p504` re-pin; stable at `p506`)* | The Open edX LMS + Studio. Dominant in higher ed and workforce. AGPL: hosting a modified copy for a client triggers source release. Default branch `master`. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | **7,556** *(🟢 `p504`, API; prior rounded cell 7,600)* | `46c042e7da65` | Largest installed base and the largest plugin ecosystem (2,000+). Grant is at `COPYING.txt`, **not** `LICENSE` — a root-`LICENSE` probe reports "no grant" here. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | 6,890 *(🟢 `p512`, API)* | `1c9f0bb8013e` | The open LMS by Instructure; heavy North America higher-ed share. AGPL. Default branch `master`. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | 3,350 *(🟢 `p512`, API)* | `6054772c0426` | Frappe-framework LMS. **Widely published as MIT — it is not.** Grant at `license.txt` (lowercase), 33,893 B, AGPL-3.0; the GitHub sidebar agrees. |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0** | **2,429** *(🟢 `p512`, API; `p510` 2,428; `p504` 2,427; prior rounded cell 2,400)* | `2d75337273ac` | **New row `p491`.** "Next-gen open source learning platform" — modern course/content platform. At 2,400★ it outranks Kolibri and Chamilo, and was absent from this KB entirely. AGPL confirmed on both channels (`LICENSE`, 34,522 B; sidebar `AGPL-3.0 license`). Default branch **`dev`**. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared only)* | 682 | `73ce33ef2719` | **New row `p491`.** Frappe school-management / SIS app — **a different product from `frappe/lms`, under a different license family.** Its grant is a **19-byte** `license.txt` reading `License: GNU GPL V3` with **no license text at all**; GitHub's classifier cannot resolve it and shows a bare "License" link. See the note below. Default branch `develop`. |
| [ankitects/anki](https://github.com/ankitects/anki) | **AGPL-3.0** | 32,365 *(🟢 `p512`, API)* | `d87cb22bf337` | Spaced-repetition engine; the reference implementation of SRS scheduling. AGPL. Useful as an algorithm reference even where the code can't be taken. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **AGPL-3.0** | 1,130 *(🟢 `p512`, API)* | `aa5d1a764b6c` | Docker-based Open edX distribution — the realistic way anyone actually deploys Open edX. Default branch `release`. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,019 *(🟢 `p512`, API)* | `2d1e97ee4244` | LMS focused on ease of use and accessibility. Notable francophone + LATAM public-sector footprint. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | `fa5f4b66caf4` | Student Information System for school management. **Correct path — `RosarioSIS/RosarioSIS` is a 404** and was cited on this KB. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | `65f86bf061fa` | K-12 school management platform (teachers, students, parents, leadership). Default branch `v31.0.00`. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | `db9582e3cd3e` | German-origin LMS, strong DACH public-sector and university use. Default branch `release_11`. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | `1e21b7a2da4a` | Interactive content types (the H5P core). Embeds into Moodle/Canvas/Open edX; the standard way interactive exercises get authored. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 *(🟢 `p512`, API)* | `46a5d7d40082` | Education **ERP** on Odoo — admissions, fees, hostel, library, timetable. The Odoo-for-education answer. Default branch `19.0`. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | `d9b3da5e6b0a` | Computer-based **assessment** platform core (QTI). The serious open assessment/exam engine. |

## The 19-byte license, and why it matters more than it looks

`frappe/education`'s entire grant is the string `License: GNU GPL V3` — 19 bytes, no license body.
Three consequences, none of them academic:

1. **GitHub cannot classify it.** The sidebar shows a bare "License" link with no SPDX identifier,
   so every tool that trusts the GitHub license field — including this KB's page-fetch channel —
   reports *unknown*, not *GPL-3.0*.
2. **It is a declaration, not a text.** GPL-3.0 is enforced through its own terms; a repository
   that names the license without shipping it still signals GPL-3.0 intent, but a client's counsel
   will ask for the text. Treat the family as **GPL-3.0 and the paperwork as incomplete**.
3. **Two Frappe education products, two license families.** `frappe/lms` is **AGPL-3.0** (p490,
   read at `license.txt`, 33,893 B) and `frappe/education` is **GPL-3.0** (19 B). Anyone who
   generalises "Frappe education apps are X" is wrong whichever X they pick.

## Fedena: resolved, and the Apache-2.0 claim does not survive contact with the repository

`p490` recorded Fedena as "could not be confirmed … not carried as a row." It resolves — to **two**
repositories, both of which `git ls-remote` reaches:

| repo | ★ | grant at SHA | sidebar |
|---|---|---|---|
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 547 | 🟢 **Apache-2.0 declared** — `NOTICE`, 680 B, `sha256₁₆ 38af3b29e41787ac` (`68a84ac445bf`) 🔴 *corrected `p514`; this row read* **none** *for 24 passes* | text absent (incorporated by reference); sidebar shows no licence |
| [foradian/fedena](https://github.com/foradian/fedena) | 4 | 🟢 **Apache-2.0 declared** — `NOTICE`, 679 B, `sha256₁₆ 386aef9c0b401bff` (`333477b06f1d`) 🔴 *corrected `p514`* | text absent (incorporated by reference); sidebar shows no licence |

Both are "Fedena SIS"; the 4★ one is a **fork** of the 547★ one. Neither ships a license file under
any of the nine names probed. The **Apache-2.0** that comparison tables and vendor blogs print for
Fedena traces to a single sentence in the README — *"Fedena is released under the Apache License
2.0"* — and a README sentence is not a grant.

> 🔴 **`p514` — THE PARAGRAPH ABOVE IS REFUTED ON THE BYTES, AND IT IS KEPT HERE RATHER THAN
> REWRITTEN** so the correction is auditable (`gate-prose-claims`). 🔴 **`NOTICE` was not one of the
> nine names probed.** Both repositories serve the Apache-2.0 grant clause at `NOTICE` on their
> **default** branch — 680 B `sha256₁₆ 38af3b29e41787ac` and 679 B `sha256₁₆ 386aef9c0b401bff` — at
> `68a84ac445bf` and `333477b06f1d`, **the exact SHAs this section records**. 🟢 *"A README sentence
> is not a grant"* remains correct as a rule; the grant simply was not only in the README. 🟡 The
> text is **incorporated by reference**, so Fedena is carried as **Apache-2.0, body absent** — the
> shape this file already resolves for `frappe/education`. 🔴 **It buys nothing operationally:**
> HEAD is dated **2016-07-20**, commit subject **`emptying content`**. See the `p514` section at the
> top of this file.

🔴 **Not carried as a permissive row, and the reason is now evidential rather than "unresolved."**
This *strengthens* the finding below: the one candidate that would have broken "no permissive SIS
exists" turns out to have no license at all. Also note the 40,000-schools / 100-countries figures
attached to Fedena in listicles describe the **commercial hosted product**, not these repositories.

## Branch-name trap, worth its own note

**Twelve** of these repos do **not** default to `main` (p491 adds `learnhouse` → `dev` and
`frappe/education` → `develop`; p490's prose said "six" while its own list named ten):
`oppia`, `kolibri` and `frappe/education` (`develop`), `learnhouse` (`dev`),
`edx-platform` and `canvas-lms` (`master`), `tutor` (`release`), `openeducat_erp` (`19.0`),
`GibbonEdu/core` (`v31.0.00`), `ILIAS` (`release_11`), `bigbluebutton` (`v4.0.x-develop`),
`tao-core` (`develop`), and `projectfedena`/`foradian` `fedena` (`master`). Any raw-content fetch
that hardcodes `/main/` returns 404 on all of them — which reads as "file absent" rather than "wrong branch". Resolve the ref with
`git ls-remote --symref` first.

## Declared gaps

- **No permissive SIS exists — confirmed harder this pass.** Every student-information system
  found (`rosariosis` GPL-2.0, `GibbonEdu` GPL-3.0, `openeducat_erp` LGPL-3.0, `openSIS` GPL-2.0,
  `frappe/education` GPL-3.0-declared) is copyleft, and **Fedena — the only candidate published as
  Apache-2.0 — ships no license grant at all**. A client needing a closed-source SIS derivative has
  no open starting point. That is a build, not a fork.
- **No permissive assessment/QTI engine exists.** `tao-core` is GPL-2.0 and is the only
  substantial one.
- ~~**`Fedena` could not be confirmed.**~~ 🟢 **Closed this pass** — it resolves to two repos, both
  unlicensed. See the section above. The claim was not wrong about the repos existing; it was wrong
  about them being licensed.
- **Commit recency is still absent from this file.** The page-fetch channel does not expose the
  latest-commit date (every fetch this pass returned a commit *count* and no date), and
  `api.github.com` is 403 for unattached repos. So **no row here can be shown to be maintained** —
  `fedena` at 547★ may well be abandoned and this file cannot tell. Rows carry a pinned SHA, which
  proves existence and content but not liveness.


## 🆕 `p492` — `2026-10-28` — the permissive numerator moves 3 → 4

Evidence: [`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv).
Narrative: [`repos/trending.md`](trending.md).

`p491` recorded that "the permissive numerator has not moved in two passes while the denominator
keeps growing." 🟢 **It moved this pass**, and in the layer where this file's only option was
copyleft.

| repo | licence | ★ | SHA read | note |
|---|---|---|---|---|
| [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** | 688 | `79b71bcb39f8` | Virtual classroom / web conferencing: video, IM, **whiteboard**, collaborative document editing; media via **Kurento Media Server**. Apache-2.0 read from **51 425 B** (`sha1 d30124557187`); the sidebar shows only an unnamed "License" link, the bytes are unambiguous. Latest release **`v9.1.0`, a security release**. Default branch `master`. **ASF governance** rather than a single maintainer. |

### The census, corrected

| | `p491` published | `p492` |
|---|---|---|
| platforms read from bytes | 19 | **20** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | **4** |
| GPL / LGPL / AGPL and other copyleft | 16 | **16** |
| permissive *full LMS* | 1 (`OpenOLAT`) | **1** — unchanged; **OpenMeetings is not an LMS** |

🔵 **The standing finding survives the correction.** The education platform layer is still
**16 of 20 copyleft**, and every hard gap this file established **still holds**: **no permissive
SIS exists** (both `fedena` repos ship no grant at all) and **no permissive assessment/QTI engine
exists** (`tao-core` remains GPL-2.0). OpenMeetings closes a **conferencing** gap and nothing else.

### How to read this row against BigBlueButton — honestly, in both directions

| | [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | [`apache/openmeetings`](https://github.com/apache/openmeetings) |
|---|---|---|
| ★ | **9,300** | 688 |
| licence | LGPL-3.0 — **linking permitted** | **Apache-2.0** |
| verdict | **still the default** for a live-classroom deployment | a **considered fallback**, not a recommendation |

**BigBlueButton is 13× larger and remains the right default.** LGPL already permits linking, which
is why this file calls it the friendliest copyleft here. The case OpenMeetings uniquely serves is
narrow and real: a deliverable that must ship **modified platform source inside a proprietary
product**, where LGPL's linking allowance does not help. **That case is rare — but this file
previously had no answer for it.** Verify the Kurento dependency and the `v9.1.0` security notes
before proposing it.

### 🔵 Recorded as a teaching resource, deliberately not a foundations row

[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
— **MIT**, 1 082 B, `sha1 b3428e1f52c0` (`2be1800d141e`), **67,600★**. At 67.6k it is the
largest-starred MIT repo this KB has read and would top any table it entered. It holds **no
students, no courses, no enrolments, no grades** — it is 60+ annotated PyTorch paper
implementations, i.e. CS-education *content*. **A foundation here is a system that already holds
the records.** This is not one.

🔵 **Probe-list fix worth more than the row:** its licence file is lowercase **`license`**. A probe
trying only `LICENSE`/`LICENSE.md` reports "no licence" on an MIT repo — the `fedena`
false-negative mechanism in reverse. **Add lowercase `license` to the nine probed names.**

### 🟢 The maintenance gap is partly closed

This file has declared, for several passes, that "no row here can be shown to be maintained."
**That was too strong.** The page-fetch channel **does** expose tagged releases with dates —
`openmeetings v9.1.0`, `canvas-mcp v1.16.0` (Oct 2026), `DeepTutor v1.6.15` (`2026-10-19`),
`education-agent-skills v3.1.0` (`2026-10-22`). For any repo that tags releases, **liveness is
readable**. The remaining limit is real but narrower: repos that never tag have no signal, and
`api.github.com` stays 403 for unattached repos. **Next pass should read a release date for every
row in this file** — it is available and this file was not using it.


## 🆕 `p493` — `2026-10-28` — the census was measuring this KB's bookkeeping, not the ecosystem

Reads: [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).
Narrative and the full list of dropped rows: [`agents/trending.md`](../agents/trending.md) `p493`.

🔴 **`p490` rewrote `agents/top.md` in full and `p383`/`p391`/`p392` rewrote this file in full.
A full-file rewrite re-derives its tables from the rewriting pass's own reads, so any row an
earlier pass promoted but that pass did not re-read is deleted without a marker.** Eight addresses
this KB had recorded as promoted are absent from both shelf files at HEAD `cb6a4be`; `dolos` is the
one that belongs here and it is restored above.

### The census, corrected again — and the correction is about the denominator's authority

| | `p491` | `p492` | `p493` |
|---|---|---|---|
| platforms read from bytes | 19 | 20 | **21** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | 4 | **5** |
| copyleft | 16 | 16 | **16** |
| permissive *full LMS* | 1 | 1 | **1** — `OpenOLAT`, unchanged |

🔴 **Do not read the `4 → 5` as ecosystem movement.** `p492`'s `3 → 4` was a real find
(`apache/openmeetings`). **`p493`'s is a repair**: `dolos` was always in the ecosystem and was
previously in this file. Two passes in a row have now moved the permissive numerator for
**different reasons**, and conflating them would turn a bookkeeping fix into a false trend.

### What still holds, and what does not

🟢 **Holds, and `p493` re-confirms it:** the **full-LMS** layer is copyleft-bound —
`OpenOLAT` (Apache-2.0, 448★) is the only permissive full LMS, against Moodle (GPL-3.0),
Open edX (AGPL-3.0), Canvas (AGPL-3.0), `frappe/lms` (AGPL-3.0, widely mispublished as MIT) and
`learnhouse` (AGPL-3.0). **No permissive SIS exists** (both `fedena` repos ship no grant).
**No permissive assessment/QTI engine exists** (`tao-core`, GPL-2.0). These are the gaps that
actually constrain an engagement and none of them moved this pass.

🔴 **Does not hold:** the generalisation that *the education stack* is copyleft-bound. With the
restored rows (see [`repos/trending.md`](trending.md) `p493`), the courseware, tutoring-platform,
teacher-workflow, academic-integrity and evaluation layers each have a permissive option, and an
end-to-end all-permissive stack is assemblable for the first time — wired up as
[`compose/patterns.md`](../compose/patterns.md) `P493-1`. **The constraint is specific to the
LMS/SIS/assessment core, and saying so is both more accurate and more useful than the blanket
claim.**

### 🔵 Declared gap, unchanged and restated

**No permissive SIS and no permissive QTI assessment engine** — searched again this pass across the
brief's platform query (`open source platform education ERP SIS student information system MIT
Apache 2026`). 🔴 **The query returned no permissive candidate at all**: OpenEduCat (LGPL-3.0),
RosarioSIS (GPL-2.0), `frappe/education` (GPL-3.0), Unifiedtransform (GPL-3.0), openSIS and Gibbon
(GPL-3.0). **Every education ERP/SIS this KB can find is copyleft.** That is now a four-pass
consistent result and should be treated as a property of the sector, not of the search.

## 🆕 `p494` — `2026-10-28` — census unchanged, and the denominator's authority is re-tested

Reads: [`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).
Narrative: [`../agents/trending.md`](../agents/trending.md) `p494`.

🟢 **No new foundation rows, no drift, no licence changes.** `p493`'s correction — that this file's
permissive census was measuring **this KB's bookkeeping rather than the ecosystem** — stands, and
this pass re-tested it the only way that is meaningful: by looking for *more* dropped material.

🔴 **It found some, and this time it was prose, not a row.** `p493` proved that full-file rewrites
silently delete promoted **table rows**, and fixed eight. `p494` finds the same mechanism deleting
**paragraphs**: an entire APAC jurisdiction posture (Singapore's Model AI Governance Framework, its
generative-AI framework, its **agentic AI framework**, and AI Verify) was removed by `p315`'s rewrite
of [`../intel/market.md`](../intel/market.md) and left no marker. 🔴 **A dropped row can be found by
`grep`-ing a repo URL. A dropped paragraph has no key to grep for** — which makes prose loss the
larger and wholly undetected surface. See [`../intel/trends.md`](../intel/trends.md) `T14`.

🔵 **Why that belongs in this file.** This file's census is a count over rows, and `p493` established
that the count's authority depends on the shelf being complete rather than on the ecosystem being
small. `p494` extends the caution: **completeness cannot be audited for prose at all with the tools
this KB has**, so any claim in this file that rests on narrative context — rather than on a
byte-pinned row — carries that uncertainty. **The row-level census is sound; the prose around it is
not audited.**

### 🟢 Re-reads this pass

| repo | KB pin | `p494` read | verdict |
|---|---|---|---|
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT, `74b101785bad` | not re-read this pass | 🟢 `p493`'s restoration row stands; 3,865 commits |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | AGPL-3.0, 34 522 B | **AGPL-3.0**, **34 522 B**, `sha1 3cd688cb1bd7` @ `7d9e9052bc5a` | 🟢 **byte-identical** — re-read because a `p494` discovery query returned it as if new |

🔴 **Declared gap, unchanged and restated for a fifth pass.** [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0) remains **the only permissive full LMS**, and there is still **no permissive SIS and no
permissive QTI exam engine** — so `T2`'s binding constraint holds at the institutional layer and
nowhere else. An engagement needing enrolment plus a gradebook has one permissive answer; an
engagement needing a SIS or a standards-based exam engine has **none**, and the copyleft conversation
is unavoidable. **Say so in week one.**


## 🆕 `p495` — `2026-10-28` — the census is unchanged, and the LGPL anchor is byte-read for the first time

🟢 **No change to the permissive numerator or the denominator this pass.** No foundations candidate
was promoted, and the reason is a supply fact rather than an absence of effort: the mandated
vertical-platform query — `open source platform education ERP CRM MIT Apache` — **returned no
MIT- or Apache-licensed education platform for the third consecutive pass**. What it returns is
`OpenEduCat` (**LGPL-3.0**), `Apache OFBiz` (Apache-2.0 but **not education**), generic MIT CRMs
(not education), and `CK-ERP` (a 2010 release, licence unconfirmed, effectively dead).

🔵 **That is `p493`'s conclusion arriving from a third independent direction and it should now be
treated as structural:** in the education **platform** layer, the permissive licences are not
where the mature systems are. The mature systems are GPL/LGPL/AGPL, and the engagement question
is never "find a permissive LMS" but **"which obligation can this client carry."**

### 🟢 `openeducat_erp` — the row this shelf points LATAM and APAC engagements at, now verified from bytes

| field | before `p495` | `p495` first-hand read | channel |
|---|---|---|---|
| pin | `46a5d7d40082` | 🟢 `46a5d7d40082` — **unchanged** | `git ls-remote` |
| licence | `LGPL-3.0` *(shelf tag)* | 🟢 **LGPL-3.0 confirmed from the payload** — `8 241 B`, `sha1 2979df12244d`, 178 lines, titled *"GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* | `raw.githubusercontent.com` |
| attribution | — | 🔴 **DEFECT: line 1 of `LICENSE` reads *"For copyright information, please see the COPYRIGHT file"* — and `COPYRIGHT` returns `404`** | `raw` probe |

🔴 **Why the dangling `COPYRIGHT` matters, and it is not pedantry.** LGPL-3.0 is a *conditional*
grant: §4 and the GPL-3.0 terms it incorporates require preserving copyright notices and stating
changes. 🔴 **The repository points its notice obligation at a file that does not exist**, so an
integrator cannot discharge the notice requirement from the grant alone — there is nothing
authoritative to reproduce. 🔵 **Practical instruction for an engagement:** reproduce the `LICENSE`
file verbatim, cite the **pin** (`46a5d7d40082`) as the provenance of what you received, and
**ask the maintainers for the `COPYRIGHT` file in writing** rather than reconstructing attribution
from commit authorship — which `p349`/`ACTION ZZ-bn` already established is not a reliable
ordering.

🔵 **This is the same genus as the *19-byte license* note above**: the licence *name* is not the
grant. The grant is the bytes, and the bytes here are correct but **incomplete by their own
reference**.

### 🟢 Pins re-read this pass

| repo | pin | verdict |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | 🟢 stable + licence byte-read |
| [`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam) | `ed5bf6359413` | 🟢 **MIT byte-pinned** — `1 071 B`, `sha1 25cb945a99ab` *(a trending row, not a foundations row — the generator is a hosted proprietary model)* |

### 🔴 Declared gap, restated and now *registered* rather than merely restated

🔴 **No permissive education platform exists at the ERP/SIS/LMS layer.** Searched again this pass
with the brief's own query; found nothing new. 🟢 **This absence is now a registered claim in**
[`../compose/code/p495-prose-claim-gate/claim_register.tsv`](../compose/code/p495-prose-claim-gate/claim_register.tsv)
**(`NO-PERMISSIVE-PLATFORM`)**, because `p494` established that a declared gap deleted by a later
rewrite is indistinguishable from coverage — and this gap is load-bearing: three patterns choose
their base on it.



## 🆕 `p496` — `2026-10-28` — the census does not move, and the vertical-platform leg is now **three passes empty**

🔵 **Nothing this pass promotes a foundations row, and that is the honest result rather than a quiet
one.** The eight addresses discovery produced (see [`../agents/top.md`](../agents/top.md) `p496`) are
all *application-layer* — IEP drafting, rubric grading, plain-language rendering. **None is
infrastructure**, so none belongs here. Recording that explicitly, because an unchanged file looks
identical to an unexamined one.

### 🟢 Pins re-read this pass — and two branch-name traps in one sweep

| repo | KB pin | `p496` `git ls-remote --symref` | default ref |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | `46a5d7d40082` | 🔵 **`refs/heads/19.0`** — a version branch |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `bc73ecf9cf71` | `bc73ecf9cf71` | 🔵 **`refs/heads/develop`** |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | `21a43a395ab4` | `21a43a395ab4` | `refs/heads/main` |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `e137ca47cbec` | `e137ca47cbec` | `refs/heads/main` |

🔴 **This file's branch-name note is stronger than it reads.** Two of the four anchors above do **not**
default to `main`, and they are the two a LATAM or APAC engagement is most likely to clone. A licence
or liveness probe that hard-codes `main` reports both as **nonexistent** — not as unlicensed, which
is the more dangerous of the two failure modes because "missing" tends to be retried while
"unlicensed" tends to be believed. 🟢 `git ls-remote --symref` resolves the real ref in one call and
every read in this pass uses it.

### 🔴 The vertical-platform leg returned a single vendor, for the third pass running

The brief's platform query (`open source platform education ERP SIS LMS MIT Apache self-hosted`)
returned **nine pages from one domain — `openeducat.org`** — in eight languages, and no second
platform at all.

🟢 **It does corroborate the byte read `p495` made:** OpenEduCat is **LGPL-3.0** (8 241 B,
`sha1 2979df12244d`), not the MIT or Apache the query asked for, and the vendor's own glossary page
is what states the permissive/copyleft distinction. 🔴 **So the query's own premise returned
nothing**: there is still **no permissive education ERP/SIS platform** on these shelves, and the
LGPL-3.0 anchor remains the recommendation for exactly the reason `p495` recorded — LGPL's obligation
attaches to the *module*, not to the whole deployment, which is survivable where AGPL is not.

### 🟡 Recorded, deliberately **not** a foundations row

[`SahilC/AutomaticEssayGrading`](https://github.com/SahilC/AutomaticEssayGrading) — **MIT**, 1 074 B,
`sha1 cd4c5b7304aa` at `8bf6dc6b678b`, 13★, 55 commits, default ref **`master`**. Classical ML essay
scoring: SVM, decision trees, random forests, LSTM. **No LLM anywhere in it.**

🔵 **Why it is worth a line despite being old and small:** it is a *comparator*, and this sector has
almost none. When a client asks why rubric scoring needs a model at all, this is the pre-LLM baseline
that answers the question with code rather than assertion. 🔴 **It is not a dependency** — it is
TensorFlow-era research code and this KB does not propose building on it.

### 🔴 Declared gap — restated, and now with the reason it keeps recurring

- 🔴 **No permissive (MIT / Apache / BSD) education ERP or SIS platform.** Third consecutive pass
  that the mandated platform query returns no such thing. The permissive answer in the *full-LMS*
  layer remains **OpenOLAT** (Apache-2.0) alone; in the *education-ERP* layer there is **no
  permissive answer at all**, and `openeducat_erp` (LGPL-3.0) is the recommendation by elimination.
- 🔴 **No foundational repository originated in LATAM or Africa.** Unchanged. 🔵 `p496` adds a
  supply-side datum rather than a search artefact: the function-shaped queries that broke the
  *agent*-layer drought this pass produced **zero** infrastructure addresses from either region.
  **The gap is in infrastructure supply, not in this KB's queries** — which is a different and more
  defensible sentence than the one this file carried before.

## 🆕 `p497` — `2026-10-28` — the census does not move, the **vertical-platform leg is four passes empty**, and the "no MIT ERP" question is now answered

Evidence: [`licence-and-stars.2026-10-28-p497.tsv`](../evidence/licence-and-stars.2026-10-28-p497.tsv),
[`branch-ref-census.2026-10-28-p497.tsv`](../evidence/branch-ref-census.2026-10-28-p497.tsv),
[`saturation-census.2026-10-28-p497.tsv`](../evidence/saturation-census.2026-10-28-p497.tsv).

### 🔴 The census is unchanged: 19 platforms, 3 permissive

**No platform row added or removed.** The vertical-platform discovery leg is now **four consecutive
passes empty** (`p494`–`p497`).

🟢 **But this pass asked the question the census implies and got an answer**, which is better than a
fourth empty leg: *does a permissively-licensed education ERP exist at all?* Searched explicitly.

| candidate | licence | verdict |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | already the KB's row; the Odoo-for-education answer |
| ERPNext | GPL-3.0 | lists Education among its verticals; copyleft |
| Odoo Community | LGPL-3.0 | the thing OpenEduCat is built on |
| Dolibarr | GPL-3.0 | ERP+CRM, no education vertical |
| Apache OFBiz | **Apache-2.0** | 🔵 permissive **but has no education vertical** — ERP/CRM primitives only |

🔴 **Conclusion, and it is a conclusion rather than a backlog item: there is no permissively-licensed
education ERP.** The only permissive ERP found (OFBiz) has no education domain model, and every
system that *does* model students, enrolments, fees and timetables is GPL, LGPL or AGPL.

🟢 **This strengthens `T2` instead of narrowing it.** The copyleft constraint is not an artefact of
this KB's sampling at the LMS layer — it holds independently at the **ERP** layer, reached by a
different query. For a client needing a closed derivative of an education *ERP*, the honest answer is
**build the domain model, or accept LGPL-3.0 and keep the Odoo modules separable**. There is no third
option to find, and future passes should stop looking for one.

### 🔴 The branch-name trap: the note above needs upgrading from two variants to five

The *"Branch-name trap, worth its own note"* section above was written for `19.0`. It is now a
five-variant pattern, each resolved by `git ls-remote --symref` this pass:

| repo | `default_ref` | ★ | status |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **`refs/heads/mobile`** | **647** | 🔴 **NEW `p497` — and it is a row in the table above.** This KB's own foundational SIS has a default ref that reads as a feature branch |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `refs/heads/19.0` | 900 | recorded; also a row above |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `refs/heads/develop` | — | recorded `p496` |
| [`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) | `refs/heads/v2` | 1 | NEW `p497` |
| [`AgnellusX1/GodsEye`](https://github.com/AgnellusX1/GodsEye) | `refs/heads/PreProduction` | 30 | NEW `p497`, archived |

🔴 **Two of the five are foundational rows in this very file** (`rosariosis`, `openeducat_erp`), so a
licence re-verification script that assumes `main` would report **this KB's own platform layer** as
partly nonexistent. 🔵 `mobile` and `PreProduction` are the variants to fear: they are
indistinguishable from feature branches by eye.

### 🟢 `rosariosis` re-read from bytes this pass — the row is correct

| field | KB record | `p497` read | verdict |
|---|---|---|---|
| HEAD SHA | `fa5f4b66caf4` | `fa5f4b66caf4` | 🟢 stable, 11th stable pin this pass |
| default ref | — | **`refs/heads/mobile`** | 🔴 newly recorded |
| licence | GPL-2.0 | **GPL-2.0**, 15 214 B, `sha1 58cb1cfbf839`, title block *"GNU GENERAL PUBLIC LICENSE Version 2, June 1991"* | 🟢 confirmed from bytes |
| ★ | 647 | **647** | 🟢 exact |

🟢 **Four of four recorded fields reproduce.** Set against `p496`'s finding that one of four re-read
byte counts did **not** reproduce, the running tally on `T14` (this KB's records are not
self-verifying) is now **seven of eight reproduced across two passes**. 🔵 The practice that surfaces
the errors is re-reading a pin before building on it — keep doing it.

### 🔵 The SIS axis, ranked for the first time

`topic:student-information-system` holds **180** repositories. The four above ~9★ —
`rosariosis` (647), `academico` (409), `openSIS-Classic` (347), `koakademy` (9) — are **all already
held here**. 🟢 The platform layer this file covers is enumerated at the top of its distribution; the
tail below ~80★ is student coursework and single-institution projects, which is why it produces no
rows. 🔴 **This axis is spent for discovery** — its value this pass was the `mobile` branch trap, not
a platform.

---

## 🆕 `p498` — `2026-10-28` — the permissive numerator moves, and the census denominator was wrong by one

🟢 **Added to the foundations shelf** — read as payloads at pinned commits:

| Repo | Licence | Why it is foundational | ★ / forks |
|---|---|---|---|
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | **MIT** (1 068 B · blob `b000bdffeaa2`, at `LICENSE.md`) | The document-to-agent-knowledge step every education build needs and most rebuild badly. Python; default ref 🔴 `master`. | 36 339 / 3 858 |
| [`beltromatti/get-it`](https://github.com/beltromatti/get-it) | 🟡 **Apache-2.0, §6 edited** (11 359 B · blob `29492aec7faa`) | A working knowledge-graph + spaced-repetition loop over arbitrary source material — the learner-model substrate the permissive shelf has otherwise lacked. 🇮🇹 EMEA. | 1 138 / 136 |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | **MIT** (1 069 B · blob `f461737043ac`) | 🟢 **Emits SCORM.** The only new row that lands inside an institutional LMS without an integration project. | 982 / 135 |

🔴 **Not added, and the reason is the same reason twice:**
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) is
**CC BY-NC 4.0** and [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) carries a bespoke
**"PageLM Community License"** with four non-commercial clauses. Both are content/curriculum assets.
🟡 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) is genuinely **Apache-2.0**
(11 337 B · blob `08c875b2050c`, canonical §6) but **archived** — carried as a 🇧🇷 LATAM data point,
not a build target.

### 🔴 The census had an arithmetic error in it, and it was a refusal

🔵 This shelf's licence census has counted [`formalms/formalms`](https://github.com/formalms/formalms)
as having **no readable grant** for multiple passes, and `Gap 488-L` asked for it to be marked
unusable. 🟢 **It is GPL-2.0.** The grant sits at `html/license.txt` (18 346 B · blob
`e823963cd437`) and at `html/lib/System/license/license_english.txt` (15 146 B · blob
`b6e1c33e0499`) **with eight further language translations** — a project that serves its licence to
users through its own web UI, and therefore has no copy at the repository root where every previous
probe looked.

🔴 **So every `NO_LICENCE` denominator this shelf has published is one too high.** 🟢 The
re-probe ran tree-wide on all twelve zero-root-grant rows and **eleven of twelve held** — the defect
is real, and its yield is 1 in 12. Detail and the eleven pinned SHAs:
[`repos/trending.md`](trending.md) `p498`.

### 🟢 `learningequality/kolibri` — the one permissive institutional platform, finally read

🔵 `Gap 488-K`: *"the only permissive institutional platform on these shelves and has never been
read — no code read, no AI-surface census, no star or activity figure. The one row the brief's
licence preference points to is the least examined."* 🟢 Closed.

| | measured |
|---|---|
| grant | 🟢 **MIT**, 1 097 B, blob `6506702f35f3`, **one** grant path in the whole tree. *"Copyright (c) 2021 Learning Equality and other contributors"* |
| ref / HEAD | 🔴 default ref **`develop`** · HEAD `08e3ecace444` · last commit **2026-10-27** · `pushed_at` **2026-10-28T01:21:58Z** |
| scale | ★ **1 162** · forks **1 012** · open issues **574** · 185 MB · Python |
| code read | **6 040 tracked files** — 1 231 `.py`, 657 `.vue`, 1 183 `.js` |
| 🔴 **AI surface** | **zero.** One regex hit across all 3 071 Python/Vue/JS files, and it is a **false positive**: the word *"transformers"* in a comment about Django `from_db_value` field transformers, at `kolibri/core/content/viewsets/import_metadata.py:152` |
| 🟢 **AI-on-top surface** | `kolibri/plugins/` — **21 in-tree plugins**, a formal hook contract, and **21 `api_urls.py`** DRF surfaces |

🟢 **The plugin contract, read from the code** (`kolibri/plugins/__init__.py`,
`kolibri/plugins/hooks.py`, `kolibri/plugins/registry.py`):

- A plugin is **a Django app with a `kolibri_plugin` module**; enabling it adds its apps to
  `INSTALLED_APPS`.
- `KolibriPluginBase` exposes `url_module` and `api_url_module`, so a plugin mounts **its own URLs
  and its own DRF API** inside Kolibri.
- 🟢 **Plugins are enabled and disabled from the CLI or a UI**, and through
  `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`. **That is an
  operational kill switch for an AI surface, with no rebuild** — which is the single most useful
  fact on this page for a ministry pilot or a regulator conversation.
- Hooks are singletons: `KolibriHook` with metaclass `KolibriHookMeta(SingletonMeta)` and an explicit
  `HookSingleInstanceError`. 🔴 **One registration per hook** — a real constraint if two vendors ship
  plugins into the same deployment.
- The project's own rule, in its own docs: *"a plugin should **never** modify internals of Kolibri or
  other plugins without using the hooks API."*
- 🟢 **Out-of-tree plugins are an exercised path, not a theory.** The repository ships four as
  `python_packages/`: `kolibri-oidc-provider-plugin`, `kolibri-sentry-plugin`,
  `kolibri-sync-extras-plugin`, `kolibri-context-translation-plugin`. An OIDC **provider** as a
  plugin is proof the extension surface reaches authentication.

🔵 **Why this matters more than the star count:** every recipe on
[`compose/patterns.md`](../compose/patterns.md) has treated Kolibri as a **content sink** — generate
packages centrally, ship them into offline channels. The code says it is a **host**. See `P498-1`.

🔵 **Not new here:** Kolibri's 0.87 fork-per-star was already recorded by `p489` as a deployment
proxy. This pass adds the licence payload, the activity, the code read and the extension contract —
not the ratio.

### 🆕 Registered

| gap | statement |
|---|---|
| 🟡 **`Gap 498-F`** | Kolibri's AI-surface census is a **keyword census** over Python/Vue/JS. A hosted inference call made through a generic HTTP client with no provider name in the source would not match. The verdict is "no provider-named integration", which is narrower than "no AI". |
| 🟡 **`Gap 498-G`** | Kolibri's **574 open issues** and `develop`-as-default both indicate an active trunk, but **no release cadence was read** — no tag list, no version file (the version is re-exported from `kolibri._version`, which was not resolved). `P498-1` therefore pins a commit, not a release. |
| 🔴 **`Gap 498-H`** | The three new permissive rows are **licence-and-description reads**. None was cloned and run, so "emits SCORM" is `Papermorph`'s claim, not a measurement. `Gap 484-A` still bounds everything on these shelves. |

---

## 🆕 `p499` — `2026-10-28` — **🟢 the permissive numerator finally moves, and it moves at the layer that matters: INTEROPERABILITY**

**Pass `p499` — reads of 2026-10-28.** This section **extends** the file; nothing above is rewritten.
Rows come from the promotion repair described in [`agents/trending.md`](../agents/trending.md)
`p499` (`Gap 499-A`). Every licence below was fetched from `raw.githubusercontent.com` at the pinned
SHA and graded on the operative-span instrument against the retained canonical set
([`evidence/canonical/MANIFEST.tsv`](../evidence/canonical/MANIFEST.tsv)).
Reads: [`new-rows-licence-bytes.2026-10-28-p499.tsv`](../evidence/new-rows-licence-bytes.2026-10-28-p499.tsv).

### 🟢 The headline this file has been waiting eight passes for

This file's standing lede is that **the education platform layer is overwhelmingly copyleft** — of
19 foundational platforms, 3 permissive — and that this is "the single most commercially important
fact in this file". 🟢 **It is still true of the LMS layer. It is not true of the layer above it.**

🟢 **The two interoperability standards that every education integration has to cross are both
permissive, and neither was on this shelf:**

| Layer | Repo | Licence (read from bytes) | ★ | Operative verdict | Why it changes the picture |
|---|---|---|---|---|---|
| 🟢 **LTI / IMS Global / Common Cartridge** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0**, 10 273 B `214d11084b7f` | **377** | 🟡 DEVIANT (−4: the `(a)`–`(d)` list enumerators in §4) | 🟢 **The LTI tool framework.** LTI is how anything reaches *inside* Moodle, Canvas, Open edX, Blackboard or D2L. Apache-2.0 means **the integration layer can be closed even when the LMS underneath is AGPL**. |
| 🟢 **SCORM / CMI runtime** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT**, 1 072 B `86ab328f0e5b` | **360** | 🟢 **IDENTICAL** | 🟢 A modern SCORM JavaScript runtime — SCORM 1.2, SCORM 2004, CMI, cross-frame. The other half of the standards boundary, and MIT. Active **2026-10-26**. |

🔵 **`tsugi`'s −4 was checked by hand before promotion, because an Apache deletion is exactly what
`p498` found in `get-it`.** It is **not** an alteration: the four §4 condition *bodies* are present
verbatim — "You must give any other recipients…", "You must cause any modified files…", "You must
retain, in the Source form…", "If the Work includes a \"NOTICE\" text file…" — and only the
parenthesised `(a)`/`(b)`/`(c)`/`(d)` enumerators are absent from the de-indented rendering. **The
conditions stand; the bullet letters do not.**

### 🟢 Six further platform rows, all read from bytes

| Layer | Repo | Licence | ★ | Operative verdict | Note |
|---|---|---|---|---|---|
| **LMS — permissive, new** | [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | 🟢 **Apache-2.0**, 11 362 B `ef4bca4c9b34` | 52 | 🟢 IDENTICAL | 🟢 **Only the second permissive full LMS on these shelves** after `OpenOlat`. Multi-tenant, Django + React, self-hosted, markets itself as a Moodle alternative. 🔴 **Repo created 2026-10-07 — three weeks old, 13 forks, 10 open issues. Do not stake an engagement on it yet;** carry it as the row to re-read every pass. |
| **Skills / credentials** | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 **MIT**, 1 063 B `18f76c220561` | 208 | 🟢 IDENTICAL | Skills-intelligence platform — competency tracking, digital credentials, course discovery. 🟢 The **competency/credential** layer had no permissive row before. Active 2026-10-27. |
| **Collaborative coding classroom** | [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) | 🟢 **MIT**, 1 073 B `52021a40fdff` | 261 | 🟢 IDENTICAL | Browser-based collaborative Python IDE with real-time editing — the teaching-lab primitive. |
| **Course CMS / microsites** | [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | 🟢 **Apache-2.0**, 11 362 B `ecac353f6e80` | 130 | 🟢 IDENTICAL | HAX + CMS for course microsites, PHP backend. Pushed **2026-10-28**. Same stable as `elmsln`. |
| **Course reader** | [`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors) | 🟢 **MIT**, 1 088 B `3f578d9362e6` | 125 | 🟢 IDENTICAL | The Tutors Reader application. 🔵 Last push 2026-07-23. |
| **Language exchange** | [`langx/langx`](https://github.com/langx/langx) | 🟢 **BSD-3-Clause**, 1 520 B `8dd6541f1ce8` | 109 | 🟡 DEVIANT (clause-3 name substitution `of the copyright holder` → `LangX`) | Peer language practice; a HelloTalk alternative. 🔵 The substitution is **what BSD-3 instructs** the licensor to do, not an edit. Active 2026-10-28. |
| **Widgets / games over LTI** | [`ucfopen/Materia`](https://github.com/ucfopen/Materia) | 🔴 **AGPL-3.0**, 34 523 B `723f2b22cec6` | 52 | 🟢 IDENTICAL | Embeddable course widgets and games. Same UCF stable as `UDOIT` and `Obojobo`. 🔴 AGPL — hosted derivative must share. |
| **Offline-first content/services** | [`Wakoma/Lokal`](https://github.com/Wakoma/Lokal) | 🟢 **MIT**, 1 063 B `f3c821e1820c` | 53 | 🟢 IDENTICAL | Offline-first content and local network services, built for low-connectivity communities. 🟢 Pairs with `Kolibri` — see [`compose/patterns.md`](../compose/patterns.md) `P490-3`. 🔵 Last push 2025-11-15. |

### 🔵 The licence census, restated with this pass's rows

| | before `p499` | added `p499` | now |
|---|---|---|---|
| foundational platforms read from bytes | 19 | **+10** | **29** |
| 🟢 of which **permissive** (MIT / Apache-2.0 / BSD) | 3 | **+8** | **11** |
| permissive share | 15.8% | | 🟢 **37.9%** |

🔴 **Read this carefully — it is not a reversal of the copyleft finding.** Every *incumbent LMS*
remains GPL or AGPL: Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas (AGPL-3.0). What changed is
that the **standards, credential, authoring and client layers around them are permissive**. 🔵 The
correct strategic sentence is therefore: *you cannot close the LMS, but you can close everything
you build against it.*

### 🟢 `frappe/education`'s "*(declared only)*" qualifier is resolved

The row above records `GPL-3.0 *(declared only)*`. 🟢 Read from bytes this pass: `license.txt` at
`73ce33ef2719` is **19 bytes** and contains exactly `License: GNU GPL V3`. 🔵 So the repo **does**
state GPL-3.0 in its own bytes — the qualifier can go — but it **ships no licence text at all**,
which for GPL-3.0 is a conveyance problem in its own right. 🔴 **Two rows do the same thing** —
`codeforlife-education/rapid-router` and `codeforlife-education/codeforlife-portal`, both a
**121-byte `LICENSE.md`** reading *"Find our license here"* plus a link — which makes **grant by
reference a class on these shelves, not an anecdote.**

### 🆕 Declared gaps — `p499` (foundations)

| gap | statement | cost to close |
|---|---|---|
| 🔴 **`Gap 499-G`** | All ten rows above are **licence-and-description reads**. None was cloned, built or run — the same standing limit as `Gap 498-H`. "Tsugi crosses the LTI boundary" is the project's claim and the standard's definition, **not a measured integration.** | needs an execution-permitted session |
| 🟡 **`Gap 499-H`** | `TutorLoom` is **three weeks old** and its Apache-2.0 grant is clean, but **nothing about its maintenance is established** — no tag list read, no release, no contributor count. It is promoted as a watch row, and a pass that treats it as a deployable LMS will be wrong. | one read per pass |
| 🟡 **`Gap 499-I`** | The permissive share moved 15.8% → 37.9% because **this pass added rows at the layers it chose to look at**. That is a selection effect, not a measured change in the sector. The denominator is this shelf, not the market. | one pass, defined sampling frame |

---

## 🆕 `p500` — `2026-10-28` — the interoperability leg gains a row, and the census axis is declared exhausted

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Licences fetched from `raw.githubusercontent.com` at commit SHAs resolved with
`git ls-remote`. Reads:
[`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv),
[`residual-promotion.2026-10-28-p500.tsv`](../evidence/residual-promotion.2026-10-28-p500.tsv).

### 🟢 Registered

| Layer | Repo | Licence @ pinned SHA | ★ | Operative body | Why this one |
|---|---|---|---|---|---|
| 🔴 **Realtime quiz / classroom response — UPSTREAM ARCHIVED** | [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 🟢 **Apache-2.0**, 11 357 B `c4c0cb0b30b5` | 77 | 🟢 **IDENTICAL** to the apache.org steward form | 🔴 **`p504`: `archived: true` on the API — this repository is FROZEN upstream, and this row recommended it with no end-of-life flag for ~20 passes.** Fork it or lift the pattern; do not expect fixes. The permissive base for live classroom response — the "everyone answers at once" problem (fan-out, join-mid-round, scoring) solved as a networking framework rather than a product. Pushed 2026-03-06: live, not fast-moving. |

### 🟢 The permissive census — and why the denominator stops moving here

The `topic:edtech` **50–400★** axis, enumerated by `p499` and re-joined against the three curated
shelves this pass, is **spent**. Of 52 rows, **21 are now shelved (40.4%)** — `p499` promoted 20
in its own pass — and of the **31** that remain:

| why unshelved | n |
|---|---|
| 🔴 copyleft (AGPL-3.0, GPL-3.0/2.0, LGPL-2.1, MPL-2.0, CERN-OHL-S-2.0) | 11 |
| 🔴 no resolvable grant at any root path | 6 |
| 🔴 dormant (no push since 2024 or earlier) | 9 |
| 🟡 permissive but dormant | 2 |
| 🟢 **permissive and live — promotable** | **4** |

**The whole remaining yield of this axis is four rows.** That is the honest reason this file's
permissive numerator has crept rather than jumped for ten passes: **not** curator inattention, but
a population that is mostly copyleft, unlicensed or abandoned. `Gap 500-A` asks the next discovery
pass for a different axis.

### 🟢 `OpenOLAT`'s Apache-2.0 grant stands — the deviation was ours

[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), re-read at `cd91a957ea2e`
(**10 982 B**), is this file's **only permissive full LMS**, so its licence was re-graded from
bytes rather than carried forward. Operative body **1 511** words against the apache.org steward's
**1 412**: the +99 is two appended paragraphs crediting the **OLAT Zentrum at the University of
Zurich** and **frentix GmbH**. 🟢 **No added condition — the Apache-2.0 grant is materially
unaltered.**

🔴 Two instrument faults are recorded against this one row. Its copy carries **no `APPENDIX`
heading**, so the marker-based operative cut removed nothing and graded attribution prose as
operative — `Gap 499-E` firing on the file's most load-bearing row. And every Apache verdict in
this file written before `p500` was scored against SPDX's 1431-word form alone, which manufactures
a **−19** phantom for any repository shipping the steward's 1412-word copy. `Gap 500-B` holds the
unmeasured blast radius; `Gap 500-C` holds the attribution-vs-restriction blindness.

### 🔴 Not registerable, recorded so the next pass does not re-read them

| Repo | ★ | Finding |
|---|---|---|
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | **Elastic License 2.0** (3 860 B @ `4449f765bdd0`) — source-available, not OSI. Forbids hosted provision to third parties. |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | 🟢 code **MIT** (5 789 B @ `a7547180c47d`); 🔴 datasets licensed **per download**, not uniformly. Shelvable as code, not as data. |
| [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) | 74 | **No grant** at any of 7 root paths (all 404). All rights reserved. |
| [`abdullaitcenter-hue/comet-trail-archives`](https://github.com/abdullaitcenter-hue/comet-trail-archives) | 70 | **No grant** at any of 7 root paths. All rights reserved. |


## 🆕 `p502` — `2026-10-28` — **🟢 the record layer reaches this shelf, 35 passes after it was graded**

`Gap 467-I` was opened because *"no permissive row exists at the LRS / learning-analytics tier; an
xAPI analytics component cannot enter a proprietary deliverable from these shelves."* It was
**closed by grading nine rows** — and closure moved **nothing onto this shelf**. 🔴 This file has
carried an LMS/SIS census for ~35 passes with **no record layer in it at all**, while
[`intel/open-gaps.md`](../intel/open-gaps.md) carried the grades. 🔵 **A gap can be answered and
still leave the base unable to answer a client.** Registered as `Gap 502-C`; five rows promoted here.

Measurement this pass used a channel this base recorded as closed — the **GitHub REST API**, reachable
through the MCP server (`Gap 502-A`, and `agents/top.md`'s verification table is corrected). Licence
family is taken from `license.spdx_id` **and** confirmed against the first 200 bytes at a pinned SHA,
per the standing two-channel rule. 🔴 **Dates are from git only**: the API's `pushed_at` counts a push
to any ref and overstated one mainline here by **708 days** (`Gap 502-B`).

### Permissive — the record layer you can put in a closed deliverable

| Repo | Licence (bytes at the pinned SHA) | ★ | forks | mainline | region | What it is |
|---|---|---|---|---|---|---|
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** — 11,357 B `1128f8f91104` | **334** | 156 | 🔴 **502 d** `efa045e` | North America | The **US DoD ADL Initiative's** own Learning Record Store, Python/Django. 🔴 **Reference implementation, not a base** — `master` has not moved since `2025-06-13` |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** — 11,356 B `58853eb8199b` | **144** | 41 | 🟢 **2 d** `6159416` | North America | SQL-backed LRS (Clojure, SQLite/Postgres). 🟢 **The live permissive LRS — build here.** Yet Analytics, `sqllrs.com` |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** — 1,045 B `f1083e4aa47d` | 78 | 53 | 🔴 419 d `5bc232d` | North America | The **official xAPI conformance suite** (`lrstest.adlnet.gov`). 🟢 This is how you prove an LRS you built or forked is conformant — the acceptance instrument for the whole tier |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | **Apache-2.0** — 11,357 B `1128f8f91104` | 59 | 34 | 🔴 281 d `806c0ba` | North America | **cmi5** player + test suite. cmi5 is the xAPI profile that replaces SCORM for launch-and-track |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** — 1,093 B `14a2c9fcad08` | 17 | 1 | 🔴 **708 d** `839fcbb` | **EMEA** | Learning-analytics visualisation over xAPI. 🔵 Region is read from the licence line itself — *"Copyright (c) 2023-present **France Université Numérique**"* — not inferred |
| [`yetanalytics/project-persephone`](https://github.com/yetanalytics/project-persephone) | **Apache-2.0** — 11,356 B `58853eb8199b` | 8 | 1 | 🟢 recent | North America | Validates xAPI Statements against **Profiles**. 🟢 New to this base. Small, but it is the piece that turns "we emit xAPI" into "we emit xAPI that conforms to a stated profile" |

🟢 Already carried, re-confirmed: [`openfun/ralph`](https://github.com/openfun/ralph) — MIT, 51★,
mainline **16 d** (`91fef11`), **EMEA** (France Université Numérique). `Gap 467-I` named it the
permissive exemplar; 🔴 **it is the third-largest permissive LRS on this shelf, not the first**, so
that closure understated its own tier by 2.8× on stars.

### 🔴 Two orderings that disagree, and the one a `pushed_at` read gets wrong

| | by stars | by mainline freshness |
|---|---|---|
| 1 | `ADL_LRS` **334** | `lrsql` **2 d** |
| 2 | `lrsql` 144 | `ralph` 16 d |
| 3 | `lrs-conformance-test-suite` 78 | `CATAPULT` 281 d |
| … | | `ADL_LRS` 🔴 **502 d** |

🔵 **The orderings are nearly inverted, and the API's convenient date field hides it:** `ADL_LRS`
reports `pushed_at` `2025-11-14` against a last `master` commit of `2025-06-13` — **154 days apart**.
🟢 **Shelf rule: cite `ADL_LRS` as the reference, build on `lrsql`, and prove conformance with
`lrs-conformance-test-suite` regardless of which you pick.**

### 🔵 One byte, two canonical Apache-2.0 payloads

`11,356 B` / `58853eb8199b` (Yet Analytics ×2) and `11,357 B` / `1128f8f91104` (ADL ×2) differ by a
single trailing byte in the appendix — **not a terms difference**. 🟢 The `1128f8f91104` payload is
**byte-identical to the one this base already recorded for
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)**, an independent
confirmation of that earlier read from an unrelated org.

### Declared gaps

| id | statement |
|---|---|
| 🆕 **`Gap 502-C`** | **Graded ≠ shelved.** `Gap 467-I` closed by grading and promoted nothing for ~35 passes. Five rows land here; **26 of the 31 tier addresses read this pass are still unshelved.** 🔴 Open and general: *how many other closed gaps closed without a promotion?* No instrument here answers that |
| 🆕 **`Gap 502-D`** | **`NOASSERTION` is three states wearing one label** — no licence, custom licence, and a licence GitHub's matcher did not recognise — with opposite procurement consequences. [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) (164★) and [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (87★) both return it, while their sibling `agent-skills` is cleanly Apache-2.0. 🟢 **CLOSED at `p503`; INDEPENDENTLY REPRODUCED at `p504` on a different channel** (`curl` against `raw.githubusercontent.com` at the HEAD SHA) with **byte-identical results** — same byte counts, same blob SHA-1s. 🔴 **But this very sentence was still live on this shelf at `p504`:** `p503`'s register entry says the stale text was *"corrected by closure above"*, and it corrected [`intel/open-gaps.md`](../intel/open-gaps.md) **without touching this file**. The register moved; the shelf did not. Corrected here now. Root cause of the `NOASSERTION`: both carry **`LICENSE.md`, a prose licensing FRAMEWORK rather than a canonical licence text**, which no matcher can classify — a **fourth** state beyond the three this gap named. `evaluators` (1 615 B, blob `86eebd7ebc43`, HEAD `b9d47891c1b8`) is 🟢 **MIT code + CC BY 4.0 prompts** but 🔴 **CC BY-NC-SA 4.0 on both annotated corpora (CLEAR, PERSUADE 2.0) — REFUSED for paid work**. `knowledge-graph` (5 789 B, blob `6320adcd726e`, HEAD `a7547180c47d`) is 🟢 **MIT code** over 🔴 **data that is NOT uniformly licensed at all**: per-dataset *and per-download* access types (Open / Open+Gated / Gated), where Gated carries no open licence and needs provider approval, a compiled build inherits every included dataset's obligations, and terms may change between releases. 🔴 **Neither is answerable at repo level** — see [`noassertion-bytes.2026-10-28-p504.tsv`](../evidence/noassertion-bytes.2026-10-28-p504.tsv) and `p503`'s closure in [`intel/open-gaps.md`](../intel/open-gaps.md). 🔴 **Original `p502` note, retained for the record:** neither payload was byte-read at `p502`, and they are the larger two |
| 🟡 carried | 🔴 **The whole record layer above is one region.** Five of six promoted rows are North America (US DoD and a Baltimore vendor); the sixth is EMEA and **708 days stale**. 🔴 **There is no APAC or LATAM LRS on this shelf, and none was found** — stated as a measured absence, not coverage |

### 🟢 `p490`'s `tao-core` correction survives a direct attack — and the attack is the reusable finding

`p490`'s correction table records that this base **overclaimed**
[`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) as `GPL-2.0-or-later` when *"the `or-later`
election is **not** readable from the payload."* 🔴 A one-line grep appears to overturn that
immediately: the payload at `2f4f12f6dbad` (**18,025 B**, `sha1 946b7346e0ed`) **does** contain the
string *"any later version"* — twice.

🟢 **It does not overturn it. Both hits are canonical GPL-2.0 text, and neither is an election:**

| line | location | what it is |
|---|---|---|
| 245 | inside **§9 of the terms** | the clause describing what happens *if* a program specifies a version number — a conditional, not a choice |
| 299 | **after line 280, `END OF TERMS AND CONDITIONS`**, inside *"How to Apply These Terms to Your New Programs"* (line 282) | the **sample notice template** the FSF supplies for authors to copy |

🔵 **Rule, and it generalises to every GNU payload on these shelves: the `-or-later` election is
never readable from a canonical GNU licence body, because the canonical body contains the phrase
twice by construction.** The election lives in the *project's own* notice — source-file headers, a
`README`, or a declared SPDX identifier — never in the licence text. 🔴 A body scan for
*"any later version"* therefore returns **true for every GPL-2.0 and GPL-3.0 repository in
existence**, election or not, and would have mis-corrected a cell that was right.

🟢 **`p490`'s cell stands: `GPL-2.0`, election not readable.** 🔵 This also sharpens `Gap 467-B`,
which records readable `-or-later` elections on `i-educar`, `i-diario`, `moodle-sence`,
`LearningLocker` and `EdOptimize` — those must have been read from a channel **other than** the
licence body, and the gap should say which, or they inherit this same defect.

🟢 **Re-confirmed independently this pass:** [`frappe/education`](https://github.com/frappe/education)'s
grant payload is still the **19-byte** `license.txt` reading exactly `License: GNU GPL V3`
(`sha1 425d2be709a6`, at `develop` `73ce33ef2719`) — the fixture behind this file's *"19-byte
license"* section. 🔴 Its default branch is **`develop`, not `main`**; `main` does not resolve, which
is this file's branch-name trap in its original instance.

## 🆕 `p503` — `2026-10-28` — **🟢 `Gap 502-D`'s TWO PAYLOADS ARE RE-READ AND BOTH SHELF CELLS HOLD — the gap text next to them says *"neither payload was byte-read this pass"* while the rows above it carry the byte counts, so the GAP is stale, not the cells. 🟢 Both now carry a blob SHA-1, which is what a drift check needs and neither had. 🟢 One MIT simulator shelved. 🔴 And the LMS-plugin-registry axis `Gap 500-A` asked for is UNREACHABLE from this session, which is an informed gap, not an unmined one.**

Reads: [`licence-bytes.2026-10-28-p503.tsv`](../evidence/licence-bytes.2026-10-28-p503.tsv),
[`channel-boundary.2026-10-28-p503.tsv`](../evidence/channel-boundary.2026-10-28-p503.tsv).

### 🟢 `Gap 502-D` — re-resolved from bytes, and the terms are richer than one cell can hold

Both payloads re-fetched at the **same pinned commits this file already cites**, bytes and git
blob SHA-1 computed locally:

| repo | path | bytes | blob SHA-1 | pinned commit | vs the cell above |
|---|---|---|---|---|---|
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | `LICENSE.md` | **5 789** | 🆕 blob `6320adcd726e` · sha256₁₆ `d849ffef4f9816cb` | `a7547180c47d` | 🟢 **byte count identical** |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | `LICENSE.md` | **1 615** | 🆕 blob `86eebd7ebc43` · sha256₁₆ `86c7be78af8ba536` | `b9d47891c1b8` | 🟢 **byte count identical** |

🔵 **Why the blob SHA-1 matters and the byte count does not suffice:** a byte count collides
trivially — any one-character substitution preserves it. The blob SHA-1 is what `p501`'s retention
check (`MANIFEST.tsv`) compares, and neither of these rows could be checked that way until now.

🟢 **`knowledge-graph`'s terms, in full, because the one-line cell flattens three states into one:**

| access type | grant | where the licence lives |
|---|---|---|
| **Open** | 🟢 CC BY 4.0 (most) or CC0 (a minority) | row-level attribution in the dataset |
| **Open + Gated** | 🟡 **split per download** — e.g. *Scope and sequence* Open while *Instructional materials* and *Assessment materials* are Gated | stated per download on the dataset page |
| **Gated** | 🔴 **not covered by any open licence**; access requires Data Provider approval under separate terms | on request from the publisher |

🔴 **The clause that decides whether this is shelvable for a paid engagement**, quoted:
*"If you compile datasets from the catalog into your own Knowledge Graph build, you take on the
licensing and attribution obligations of every dataset and download you include."* And:
*"Attribution travels with the data, not with Learning Commons."* 🟢 **Shelf rule, unchanged but now
grounded: build on the MIT code; treat every dataset as a separate procurement question, and never
publish a derivative build as uniformly CC BY 4.0.**

🔵 `evaluators` is the same shape with a sharper edge: **code MIT**, prompts and settings
**CC BY 4.0**, and the two annotated corpora it ships — **CLEAR** and **PERSUADE 2.0** —
**CC BY-NC-SA 4.0, non-commercial**. The code is billable; the rubric corpora are not.

### 🟢 Shelved — an MIT teaching simulator, with its limits stated

| Repo | Licence @ pinned SHA | ★ | Operative body | What it is | Region basis |
|---|---|---|---|---|---|
| [`xevrion/breakscale`](https://github.com/xevrion/breakscale) | 🟢 **MIT**, 1 080 B `c58de512f3ae` (blob `0c920ce1638e`, sha256₁₆ `33ea9e6b8b9621dc`) | **1 858** | 🟢 **IDENTICAL** to retained canonical MIT | A **load-it-until-it-breaks** system-design simulator: build an architecture on a canvas, drive traffic through it, watch the queueing behaviour explain the failure. TypeScript + React, `queueing-theory` in its own topics. | 🔴 **unplaced** — English artefact, `breakscale.tech`, no locale signal; recorded as unplaced rather than defaulted to a region |

🔴 **What it is not:** there is no AI in it, and the subject is one topic (distributed systems), so
it is **courseware machinery, not an education platform** — the reusable part is the
simulate-then-explain loop, which is the shape an agentic lab assistant needs and which this
shelf had no permissive instance of.

### 🔴 The registry axis is blocked, not unmined — three probes each

`Gap 500-A` asked for *"topic co-occurrence, LMS plugin registries, or a non-GitHub forge"* and
`Gap 502-E` named non-GitHub forges as the likeliest blind spot. Probed:

| channel | 3 probes | verdict |
|---|---|---|
| `download.moodle.org/api/1.3/pluginlist.php` | `000 000 000` | 🔴 **BLOCKED** by this session's network policy — the Moodle plugin registry cannot be read here |
| `codeberg.org/api/v1/repos/search` | `000 000 000` | 🔴 **BLOCKED** |
| `huggingface.co/api/models` | `000 000 000` | 🔴 **BLOCKED** |
| `api.npmjs.org/downloads/point/...` | `000 000 000` | 🔴 **BLOCKED** — no demand-side signal (downloads) is obtainable |
| `registry.npmjs.org/-/v1/search` (control) | `200 200 200` | 🟢 works |
| `gitlab.com/api/v4/projects?search=` | `200 200 429` | 🟢 **ANSWERS, rate-limited** |

🟢 **One non-GitHub forge is reachable** — `gitlab.com`'s REST API, and `git ls-remote` pins SHAs
there exactly as it does on GitHub (verified against `gitlab-org/gitlab-foss`). 🔴 **The registry
axis needs a network-policy change, not another pass** — same class as `Gap 499-C`'s `gnu.org`.
Registered as `Gap 503-B`.
