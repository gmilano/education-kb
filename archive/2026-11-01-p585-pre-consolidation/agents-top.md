---
industry: education
region: Global
updated: 2026-11-01
---

## p584 — 2026-11-01 — **`583-F` refuted at `41×`: the "education integration is a library tier, the agent is always the build" rule does NOT generalise — `38` agent-shaped artefacts in `483` education-relevant addresses on four axes never queried in `583` passes, against `1 in 538` on the integration axes. And `FILED = 0`: not one of the `38` had ever reached a curated page, one after `36` history mentions.**

🔵 **`583-A` was run first, as it now requires, and this is the first pass where its gate
*cleared* a sweep instead of aborting one.** The token-check published before any claim:

| disposition | addresses | note |
|---|--:|---|
| 🟢 FILED on a curated page | **`0`** | 🔴 the entire tier was unshelved |
| 🔴 UNFILED — append-only history only | **`9`** | re-found up to **`36×`** |
| 🆕 NEW to this base | **`29`** | |

🟢 **`NEW (29) > UNFILED (9)`, so the sweep was correctly aimed and proceeded.** `p583`'s
case was the inverse (`4` new against `18` unfiled) and its sweep should have been
re-aimed. 🟢 **The gate is therefore two-sided — it is a go/no-go, not a veto** — which is
new information about `583-A` itself and could only be learned by running it on a sweep
that deserved to run.

### 🔴 The central measurement: `583-F`'s generalisation is refuted

`583-F` prescribed testing the integration axis's `1-in-538` agent ratio on `topic:sis`,
`topic:gradebook` and `topic:proctoring` **before generalising it**. All three were swept,
plus `topic:student-information-system`. **`596` rows, `586` unique addresses, every
denominator first-hand:**

| axis | repositories | education-relevant | agent-shaped |
|---|--:|--:|--:|
| `topic:sis` | `141` | `64` | `11` |
| `topic:student-information-system` | `180` | **`180`** | `13` |
| `topic:gradebook` | `125` | **`125`** | `7` |
| `topic:proctoring` | `150` | `114` | `19` |
| **total (deduplicated)** | **`586`** | **`483`** | **`38`** |

🔴 **`38 / 483` = `7.9 %` against `1 / 538` = `0.19 %` on the integration axes — a `41×`
difference.** The "assessment-interchange is a library tier and the agent is always the
build" rule is **not a property of education integration**. It is a property of the
*assessment-interchange layer alone*, and `583-F`'s instruction to test before
generalising was correct to the point of saving a published rule from being wrong in
engagement material.

### 🟢 Shelved — the agent tier of the SIS / gradebook / proctoring layer

Every grant below **byte-read first-hand** this pass (`curl` → `raw.githubusercontent.com`,
byte counts piped to `wc -c`); **zero `NONE`** among the shelved rows. `pushed_at` carried
on every row per `580-E`.

| agent | address | grant (byte-read) | ★ | pushed | region | what it is |
|---|---|---|--:|---|---|---|
| **NTU COOL MCP** | [PsychQuant/che-ntucool-mcp](https://github.com/PsychQuant/che-ntucool-mcp) | 🟢 **MIT** (`1,066 B`) | 1 | `2026-10-18` | APAC | 🔴 **UNFILED `19×` before this pass.** MCP server over **NTU COOL** (National Taiwan University's Canvas): `10` tools reading courses, assignments and submissions. 🟢 The attach-boundary pattern applied to a *named national university's* LMS tenancy |
| **Canvas LMS skill** | [timdrichards/canvas-lms-skill](https://github.com/timdrichards/canvas-lms-skill) | 🟢 **MIT** (`1,069 B`) | 1 | `2026-07-30` | Global | 🔴 **UNFILED `11×`.** A Claude Code skill for the Canvas LMS API — rosters, assignments, quizzes. The skill-shaped sibling of the MCP row above |
| **Google AI Classroom** | [wongcyrus/Google-AI-Classroom](https://github.com/wongcyrus/Google-AI-Classroom) | 🟢 **MIT** (`1,062 B`) | 0 | `2026-10-28` | Global | 🆕 Edge-to-cloud **multimodal** agent for smart classrooms **and exam invigilation** — the first row in this base that puts invigilation and classroom sensing in one agent |
| **LastBell** | [noestudios/lastbell](https://github.com/noestudios/lastbell) | 🟢 **MIT** (`1,067 B`) | 1 | `2026-10-16` | North America | 🔴 **UNFILED `10×`.** Self-hosted **ParentVUE + Canvas** grade and assignment monitor with whole-family alerts. 🟢 **Region placed from the product** — ParentVUE is a US K-12 parent portal. 🟢 **A guardian-facing agent, a tier this base had no row for** |
| **Cubite MCP** | [amirtds/cubite-mcp](https://github.com/amirtds/cubite-mcp) | 🟢 **MIT** (`1,063 B`) | 0 | `2026-09-23` | Global | 🆕 MCP server for Cubite LMS (hosted Open edX). Third attach-boundary row, third distinct LMS |
| **Carreau** | [a8naaijetvi2lunk/carreau](https://github.com/a8naaijetvi2lunk/carreau) | 🟢 **MIT** (`1,069 B`) | 0 | `2026-10-01` | EMEA | 🆕 **Region placed from the language of the artefact** — *"QCM surveillés sur téléphone pour la classe : QR code renouvelé"*. Phone-based proctored multiple-choice with a rotating QR code; a low-infrastructure invigilation design |

🔴 **Declared and not shelved — the unshippable half of the tier.** The most
*architecturally* interesting proctoring artefacts carry no grant at all:
`aryashinod/Multi-Agent-Online-Exam-Invigilation-System` (**no licence**, `5` specialised
agents — identity, gaze, phone detection) and `umair801/sis-agent` (**no licence**,
FastAPI + LangGraph + Claude + React + Supabase). 🔵 Both are **reference architectures to
read, never dependencies to ship** — and they are why the `7.9 %` figure must not be read
as `7.9 %` of *shippable* supply.

### 🔴 `topic:sis` is a homonym axis, and the long form is the clean one

`77 of 141` `topic:sis` rows are **not education at all**: *Sovereign Intelligence System*,
*Starlight Intelligence System*, **Safety Instrumented System** (industrial AI testing),
plus epidemic simulation and a NetLogo model. **`55 %` pollution.**
🟢 **`topic:student-information-system` is `0 %` polluted and `180` rows — larger than the
short form.**

🔵 `Trend 17` of this base says tag variants split a capability's population *and the short
form is the empty one*. 🟢 **Here the short form is neither empty nor smaller — it is
polluted**, and the long form is both clean and bigger. Filed as `Trend 40`; the practical
rule is that an acronym axis must be measured for homonyms before its denominator is
quoted, because `141` would have been reported as education supply and `55 %` of it is not.


## p583 — 2026-11-01 — **the integration axis was never unswept, it was unshelved: `538` repositories on the four axes `p582` called never-swept, `29 of 33` already in this base, and the one agent artefact on the axis**

🔵 **Method note (unchanged channel, re-attested per `580-G` before use).** Every figure
below comes from `gh api -X GET search/repositories -f q='repo:owner/name'`, which returns
`license.spdx_id`, `stargazers_count`, `pushed_at`, `archived`, `forks_count` and `topics`
in one call at `30` calls/minute. 🔴 **`curl -sI` against `github.com` is still inoperable
here** — the run prompt mandates it, and it returns `403` for real and fabricated
addresses alike. 🔵 Grants are byte-read from `raw.githubusercontent.com`; a single
unresolvable `repo:` qualifier returns `422`, which for a **single** qualifier is a usable
"absent" signal (the `422` false-zero hazard of `580-A` applies only to OR-batches).
Records: [`integration-axis-sweep`](../evidence/integration-axis-sweep.2026-11-01-p583.tsv),
[`grants-byte-read`](../evidence/grants-byte-read.2026-11-01-p583.tsv).

### 🔴 The central result: `p582`'s first priority rested on a false premise

`p582` prescribed sweeping `topic:lti`, `topic:lti-provider`, `topic:xapi` and `topic:qti`
singly, on the stated ground that the integration axis — *"the base's most important
unreplaced dependency"* — had **never been swept with the corrected query form**. All four
were swept this pass. The axis is not unswept:

| disposition | addresses | meaning |
|---|--:|---|
| 🟢 **FILED** on a curated page | **`11`** | already recommended to a reader |
| 🔴 **UNFILED** — in the append-only history only | **`18`** | owned, re-found up to `15×`, never shelved |
| 🆕 **NEW** to the base | **`4`** | and all four are marginal: `80★`, `10★`, `4★`, `1★` |

🔴 **`29 of 33` measured addresses were already in this base.** The axis was never a
discovery problem; it is `Trend 16` — a finding in this base's history not reaching its
shelf — landing on the dependency the base itself calls most load-bearing. Denominators:
`topic:lti` `184`, `topic:xapi` `280`, `topic:qti` `52`, `topic:lti-provider` **`22`**
(the whole world's LTI-provider topic is twenty-two repositories).

### 🟢 WITHDRAWN: "no maintained permissive LTI 1.3 library"

🔴 `intel/trends.md` carries this as **NEW and load-bearing**. It is **refuted**, and the
refuting address has been in this base's own history **`15` times** without ever reaching a
shelf:

| repo | licence (byte-read) | ★ | `pushed_at` | region | what it is |
|---|---|--:|---|---|---|
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (`1,528 B`) | 73 | `2026-10-05` | North America | 🟢 **Implements `LTI13Authenticator` and `LTI11Authenticator`** for JupyterHub against Canvas, Moodle and Open edX. Module `ltiauthenticator/lti13/auth.py` read first-hand. Owner **Project Jupyter** → region on owner identity. 🔴 **`15` history mentions, `0` curated.** |
| [StevenWeathers/peregrine-lti](https://github.com/StevenWeathers/peregrine-lti) | 🟢 **Apache-2.0** (`11,357 B`) | 7 | `2025-11-20` | Global | LTI 1.3 launch library in **Go**; topics `lti1p3`, `ltiadvantage`. 🟡 Inside the one-year recency cut but only just. Provenance unknown. |
| [swisnl/laravel-lti-provider](https://github.com/swisnl/laravel-lti-provider) | 🟢 **MIT** (`1,108 B`) | 4 | `2026-08-28` | EMEA | 🆕 **NEW.** Laravel LTI provider. Owner **SWIS** (Netherlands) → region on owner identity. |
| [LtiLibrary/LtiLibrary](https://github.com/LtiLibrary/LtiLibrary) | 🟢 **Apache-2.0** (`11,325 B`) | 80 | `2025-06-02` | Global | 🆕 **NEW**, and 🔴 **LTI 1.1.1 only, not 1.3** — recorded so the next pass does not mistake it for a 1.3 option. .NET. |

🔵 **The accurate restatement, which is narrower and still useful:** there is no
permissive, maintained, *framework-independent* LTI 1.3 library for **Python**.
`dmitry-viskov/pylti1.3` (MIT, `138★`) remains the most-starred Python option and was last
pushed `2024-08-18` — `26.5` months, not the `27` the base rounds to. The maintained
permissive options exist in **Go**, **PHP-on-Laravel** and **JupyterHub**, and the
maintained PHP option of record, `oat-sa/lib-lti1p3-core` (`37★`, `2026-10-24`), is
🔴 **GPL-2.0**. That is a *language* gap, not an *ecosystem* gap, and it is a far cheaper
thing to fix.

### 🆕 The one agent artefact on the axis

| agent | repo | licence (byte-read) | ★ | `pushed_at` | region | what it does |
|---|---|---|--:|---|---|---|
| **canvas-quiz-skill** | [rikardroitto/canvas-quiz-skill](https://github.com/rikardroitto/canvas-quiz-skill) | 🟢 **MIT** (`1,070 B`) | 1 | `2026-08-07` | Global | 🆕 An **agent skill**: author a quiz in Markdown, get a QTI 1.2 package importable into Canvas. 🔵 Shelved at `1★` not for its traction but because it is the **only agent-shaped artefact** on four axes and `538` repositories — which is itself the measurement. Provenance unknown. |

🔵 **What the absence means for a studio.** The assessment-interchange layer is a
**library** layer, not an agent layer: `538` repositories and exactly one agent artefact.
A client asking for "an AI agent that writes assessments into our LMS" is asking for a
build, where the QTI/LTI plumbing is bought (permissively, see `repos/foundations.md`) and
the agent is the deliverable.


## p582 — 2026-11-01 — **one new agent row, the "largest permissive repository" claim withdrawn and replaced, and a dual-licence repository resolved from its bytes**

🟢 **Instrument unchanged:** `q=repo:owner/name` against `search/repositories`, one call
per row, returning licence, stars, forks, `pushed_at`, `archived`. Every number on this
page section was measured this pass. Record: `evidence/verified-rows.2026-11-01-p582.tsv`.

### 🟢 New agent row

| Agent | Repo | Licence | Stars | Forks | Last push | Region | What it does |
|---|---|---|--:|--:|---|---|---|
| **Paper2Poster** | [Paper2Poster/Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | 🟢 **MIT** | **4,032** | 288 | `2026-10-23` | Global | **NeurIPS 2025.** Multi-agent pipeline turning a paper into a conference poster. Topics: `agent`, `multi-agent-systems`, `pptx`, `task-automation` |

🔵 **Why this one is an agent and the other `26` rows from this pass are not.** It plans,
decomposes and executes over a document with multiple cooperating roles. The rest of
`p582`'s yield is capability libraries — OCR, ASR, parsers, renderers — and is shelved on
[`../repos/foundations.md`](../repos/foundations.md) and
[`../verticals/solutions.md`](../verticals/solutions.md). 🟢 **It is also the first row
here that automates a scholarly *output*** rather than a learning input, which is a
distinct engagement type: research-office and university-communications work.

### 🔴 WITHDRAWN: "the largest permissively licensed repository anywhere in this knowledge base"

This base asserts that of `hugohe3/ppt-master` in five places across four pages. 🔴 **The
claim is false and is corrected here rather than merely supplemented:**

| repo | licence | stars (`2026-11-01`) | status |
|---|---|--:|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 🟢 **MIT** | **193,266** | 🆕 **the largest permissive repository in this base** |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 MIT | `71,711` | 🔴 claim withdrawn — `2.7×` smaller |
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `52,957` | largest *education-native* row |

🟢 **The replacement row is also better evidence than the one it displaces.**
`ppt-master` is carried with *"⚠️ Provenance unverified … no region is assigned."*
`markitdown` is owned by **Microsoft**, so it places to **North America** on owner
identity — the one region signal this base accepts as sound while `users/{login}` is
`403`. 🔵 `ppt-master` is not demoted on quality: it moved `71,498 → 71,711★` this pass
and remains live. Only the superlative was wrong.

### 🔴 Licence resolved from bytes: `microsoft/autogen` is two licences, and both the API and this base's ledger were half right

`autogen` is **not** a row on this page — it is referred to in prose as a general agent
framework "with an education angle bolted on", and that placement stands. But the
rotation ledger carries it as `AutoGen(MIT,~60k★)`, the API now returns something else,
and the conflict is worth settling because studios reach for it:

| source | licence reported |
|---|---|
| `search/repositories` API detector | 🔴 **CC-BY-4.0** |
| this base's ledger | 🟢 MIT |
| 🟢 **`LICENSE` bytes, `main` + `master`, `18,649 B`** | **CC-BY-4.0** — "Attribution 4.0 International" |
| 🟢 **`LICENSE-CODE` bytes, `main` + `master`, `1,140 B`** | **MIT License, Copyright (c) Microsoft Corporation** |

🟢 **Both are correct about different files, and neither is correct alone.** The
repository ships **two** licence files: the code is **MIT** via `LICENSE-CODE`; the
default `LICENSE` is **CC-BY-4.0**, which covers documentation, samples and content.
🔵 **The practical consequence for a studio:** the library is MIT and shippable, but
**material lifted from its docs, notebooks or samples carries an attribution
obligation** — and GitHub's detector, reading only `LICENSE`, will label the whole
repository CC-BY-4.0 in any automated compliance scan a client runs. 🟢 **Measured, not
inferred** — four byte reads, two branches, two filenames.

### 🟢 Agent shelf anchors, re-measured first-hand this pass

| Agent | Repo | Licence | Stars | Forks | Last push | Region |
|---|---|---|--:|--:|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | **52,957** | 6,483 | 🟢 `2026-10-31` | APAC |
| **smolagents** | [huggingface/smolagents](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 | **30,158** | 3,176 | 🟢 `2026-10-29` | EMEA |
| **Paper2Poster** | [Paper2Poster/Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | 🟢 MIT | **4,032** | 288 | 🟢 `2026-10-23` | Global |
| **learn-agentic-ai** | [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | 🟢 MIT | **4,393** | 1,006 | 🔴 `2025-10-26` | APAC |
| **pykt-toolkit** | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | **456** | 141 | 🟢 `2026-10-18` | APAC |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | 🟢 MIT | **387** | 76 | 🟡 `2026-05-29` | APAC |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 MIT | **274** | 164 | 🟢 `2026-10-31` | North America |

🔴 **`panaversity/learn-agentic-ai` crossed the staleness line.** Last push
`2025-10-26` — **just over 12 months** as of today, so it moves out of the live tier by
this base's own `p580` criterion. It is a curriculum rather than a deployable agent, which
softens the impact, but it should no longer be presented as maintained.

🔵 **Scale note worth keeping, because it is a `2,000×` spread.** `DeepTutor` at
`52,957★` and `educhain` at `387★` sit on the same shelf. **The education-agent tier is
one large project and a long tail of small ones** — and `DeepTutor` alone grew from the
`~24,000★` recorded in this base's cycle-3 notes to `52,957★` now. Any claim about "the
open-source education agent ecosystem" is, numerically, a claim about `DeepTutor`.


## p581 — 2026-11-01 — **the lecture-media sweep `p580` prescribed, run: five new permissive rows, and the two crossed-topic query forms that made four passes of sweeps come back empty**

🟢 **`Gap "lecture-video tooling remains unswept"` closes — it was the declared next-pass
job on [`../intel/trends.md`](../intel/trends.md) and it paid.** Five addresses enter the
shelf, the largest at **`11,026★` MIT**. 🔴 **But the headline finding is a method defect,
not a repo:** the sweep form this base has been using crosses two topics
(`topic:tts+topic:education`), and **every crossed form returns `total_count = 0`** — not
few results, *zero*. That is why `hugohe3/ppt-master` (MIT, `71,498★`) went unfound for
four passes and had to be surfaced by web search instead.

```
gh api -X GET search/repositories -f q="topic:X" -f sort=stars -f order=desc
  then filter licence/recency client-side        ← WORKS
gh api -X GET search/repositories -f q="topic:X+topic:education"
  → total_count = 0, six times out of six        ← COLLAPSES
```

🔵 **Why: education repositories do not carry capability topics.** `DeepTutor` carries
`ai-tutor`, not `video`. `ppt-master` carries `pptx`, not `education`. The intersection is
empty as a property of how maintainers tag, so **sweep single capability topics and filter
by licence — never cross two topics.** Six nil legs recorded in
`evidence/sweep-nil-legs.2026-11-01-p581.tsv`.

### 🟢 New agent rows, every field first-hand `2026-11-01`

| Agent | Repo | Licence (first-hand) | Stars | Last push | Region | Note |
|---|---|---|--:|---|---|---|
| **autoclip** | [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 🟢 **MIT** | **9,898** | `2026-10-31` | APAC | 🟢 **The one genuinely agentic row here** — topics include `ai-agent` and `mcp`. Cuts long-form video into clips with subtitles, covers and captions. 🟢 **Its own description names 课程 (courses) as an input class**, alongside podcasts and interviews — so unlike `MoneyPrinterTurbo` this is lecture-shaped, not only social-shaped. `1,758` forks. |
| **VidBee** | [nexmoe/VidBee](https://github.com/nexmoe/VidBee) | 🟢 **MIT** | **11,026** | `2026-10-31` | APAC | 🟢 **Largest permissive addition this pass.** Fetch + local Whisper transcription with **speaker diarisation** (`speaker-diarization` topic) and AI summary. The diarisation is what makes it a seminar/panel tool rather than a download utility. `863` forks. |

🔵 **Two rows, not five, on *this* page** — the other three are libraries, not agents, and
are shelved on [`../repos/foundations.md`](../repos/foundations.md) where they belong. **Three
real agent-shelf rows would have been padding; two is what the sweep actually produced.**

### 🔴 A non-finding recorded so the next pass does not re-publish it as a discovery

The same sweep ran `topic:item-response-theory`, `topic:psychometrics` and
`topic:computerized-adaptive-testing` against the standing gap *"abundant permissive
tooling for generating content and none for generating psychometrically defensible items"*.
🔴 **Every row returned was already on these shelves** — `catsim` (138 references),
`eribean/girth` (84), `EduCDM` (40), `Agent4Edu` (35), `pypsy` (19). **The gap stands
exactly as written**, and it is narrower than "no psychometric tooling": calibration and
adaptive-test *simulation* are shelved and permissive; **item *generation* is the hole.**
🔵 This is `Trend 11`'s pathology — a closed gap re-published — caught before publication
rather than after, by grepping the shelf before writing the row.

🔵 **Method correction, because the run prompt mandates the broken form.** `curl -sI
https://github.com/owner/name` returns **`403` for every GitHub URL** through this
session's proxy — including addresses confirmed to exist. **A `403` here is the proxy, not
a dead link, and `curl` cannot distinguish a live repo from a 404.** URL verification must
use `q=repo:owner/name` against the search endpoint, which returns `200` with licence,
stars, forks, `pushed_at` and `archived` in one call. Every row above was verified that way.


# Top AI agents for education

## p580 — 2026-11-01 — **every agent row on this page re-measured first-hand in one sitting, `579-C` blocked, `579-E` placed — and the licence field that made it cheap is the one field it gets wrong**

🔴 **`Gap 579-A` closes, and the correction belongs on this page above all others, because
the instrument was already documented here.** The "Method note" further down this file
records, from `p577`: *"Every repository URL on this page was confirmed by
`search_repositories` with `repo:owner/name`, which returns id, licence determination, star
count, fork count and push date in one call."* 🔴 **`p579` nonetheless published that a
first-hand star count was "still none", and this pass drafted the qualifier as a
discovery.** Three passes, one instrument. 🟢 **What is new below is scale — the first
census across the whole shelf rather than one page — and the `422` guard that makes
batching safe.** The call, for the record:

```
gh api -X GET search/repositories -f q="repo:HKUDS/DeepTutor"
  → stargazers_count · license.spdx_id · archived · pushed_at · forks_count · topics
```

🔵 **The `403` is this harness's repository allowlist** — its body says *"sessions are
bound to their configured repositories"*. 🔵 **That diagnosis is `p515`'s** (`2026-10-28`),
not this pass's, and it was lost for ~65 passes. `users/{login}` is blocked by the same
boundary, so owner `location` is unreachable — the consequence this page already records
under "Method note" via `search_users`. Every placement below is therefore made from
**description language, topics and institutional names**, and says so.

### 🟢 The agent shelf, re-measured first-hand `2026-11-01` — stars, licence, recency, all one call each

| Agent | Repo | Licence (first-hand) | Stars | Last push | Region | Note |
|---|---|---|--:|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | **52,849** | `2026-10-31` | APAC | Lifelong personalised tutoring; `6,469` forks. 🟢 Still the field's only education agent at frontier scale. Topics include `ai-tutor`, `multi-agent-systems`, `rag`. |
| **nbgrader** | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** ⬅️ *was `unstated` in the ledger* | **1,370** | `2026-10-28` | North America | Assign, autograde and release Jupyter notebooks. 🟢 **The licence settled this pass** — Project Jupyter governance, `346` forks. The autograding row to build on. |
| **Proctoring-AI** | [vardanagarwal/Proctoring-AI](https://github.com/vardanagarwal/Proctoring-AI) | 🟢 **MIT** | **633** | — | Global | 🟢 **The highest-starred genuinely institution-accountable education artefact found anywhere in this base** (see the `579-D` falsifier on [`../intel/trends.md`](../intel/trends.md)). Gaze/face/phone detection for exam proctoring. |
| **pyKT** | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **456** | `2026-10-18` | APAC | PyTorch knowledge-tracing library; the reference for modelling what a learner knows. 🔴 *Note: this base previously carried `1.2k★` for this row from a secondary source; the first-hand figure is `456`.* |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | 🟢 **MIT** ⬅️ *was `unstated`* | **387** | `2026-05-29` | APAC | LLM content generation for education — MCQs, lesson plans, flashcards. India-origin (Build Fast with AI). |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** ⬅️ *was `unstated` across 6 pages* | **310** | `2026-11-01` | North America | MCP server for Canvas LMS, `102` tools, **University of Illinois**, FERPA-aware. 🟢 Pushed the day of this census. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | **274** | `2026-10-31` | North America | Intelligent tutoring with Bayesian Knowledge Tracing; **UC Berkeley CAHLR**. React + Firebase. |
| **EduCDM** | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 **Apache-2.0** ⬅️ 🔴 *the ledger had this `no-grant`* | **203** | 🔴 `2024-10-25` | APAC | Cognitive diagnosis models (DINA, IRT, MIRT, NCDM). 🟢 **Shippable, and this base had it filed as unusable.** 🔴 Stale ~12 months. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** ⬅️ *was `unstated`* | **114** | `2026-06-26` | EMEA | Tutoring platform with voice, video and 3D avatars; Docker-first, local LLMs via Ollama. |
| 🆕 **Lama Loca** | [emil-a-dev/lama-loca](https://github.com/emil-a-dev/lama-loca) | 🟢 **MIT** | **59** | `2026-03-04` | **EMEA** | 🆕 **Placed this pass** (`579-E`). Russian-language, **fully offline** study assistant: learns from the user's own books, produces reports, slides and notes. Python, `qwen`, `chromadb`, `gradio`. |
| 🆕 **BCTK / TK试题题库** | [BBkjdayup/BCTK](https://github.com/BBkjdayup/BCTK) | 🟢 **MIT** | **53** | `2026-09-28` | **APAC** | 🆕 **Placed this pass** (`579-E`). Chinese-language Windows item-bank and paper-composition desktop app for teachers, **local-offline-first**. Tauri 2 + Vue 3 + Rust + SQLite; Word import/export without Microsoft Office. |

🔵 **Eleven rows, every figure measured first-hand today.** Five licences marked ⬅️ were
`unstated` or wrong in this base's ledger before this pass.

### 🔴 `Gap 579-C` CLOSED — the row is unlicensed and is now blocked

`A-R007/Multi-Agent-Study-Assistant` (`64★`) was cited in three files as `unstated`.
Twelve probes — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE`, `license`
across both `main` and `master` — **all `404`**, and the API reports `spdx_id: NONE`.
Last pushed **`2025-11-04`**, twelve months stale.

🔴 **No grant exists. Unlicensed is all-rights-reserved → `BLOCK`.** Moved to the unusable
register, and stated with its full path set so it is a finding rather than `Trend 24`'s
upper bound.

### 🔴 Two rows to stop recommending, both for recency rather than licence

| row | licence | stars | last push | why |
|---|---|--:|---|---|
| `DMontgomery40/mcp-canvas-lms` | 🟡 **`MIT\|no-grant`** — declared, not shipped | `104` | `2026-05-31` | 🔴 **No licence file at 8 paths × 2 branches**, API says `NONE` — but `package.json` declares `"license": "MIT"` and lists a `LICENSE` that does not exist. 🔴 **Do not gate on this as MIT**; it is a question for counsel. 🟢 `vishalsachdev/canvas-mcp` (MIT, `310★`, real licence file) does the same job — prefer it. |
| `bigdata-ustc/Agent4Edu` | 🔴 **`NONE`** | `100` | `2026-09-29` | 🔴 Unlicensed learner-simulation agent. Confirms the gap `p573` named: **learner simulation is still unlicensed**, now re-checked first-hand. |

### 🔴 Method correction this page should carry: the licence field is the one field to distrust

🟢 The new channel is authoritative for existence, stars, forks, `archived` and
`pushed_at`. 🔴 **It is wrong about licences for any project that declares its grant in a
package manifest** — `3 of 4` R/CRAN packages tested report `spdx_id: NONE` while
declaring GPL in `DESCRIPTION` (trend 33). Base-wide, **`67 of 265` shelf rows
(`25.3 %`) return `NONE` or `NOASSERTION`**, and `NONE` must not be read as *ungranted*
until the manifest has been checked.

🔴 **And a new false-zero to avoid:** OR-batching `repo:` qualifiers is cheap but **one
unresolvable qualifier returns `422` for the whole batch**, zeroing every good address in
it. On this pass's first run it cost `tw93/Kami` (`12,185★`, MIT) — which would have been
filed as dead. Detect the `422` and fall back to single calls.

🔵 **`curl -sI` remains noise, and now the mechanism is named:** every
`https://github.com/...` request from this harness returns **`403`** through the agent
proxy — real repositories and fabricated controls alike. That is why `p575` found the
prescribed verifier certifies nothing. 🟢 **The replacement is `q=repo:owner/name`**,
which returned a record for all `265` live addresses and nothing for both deliberate
controls (`gmilano/nonexistent-repo-xyz`, `this-does-not-exist-xyz123/nope`).
🔴 **With one caveat that needs the org listing to resolve: a *renamed* repository is
indistinguishable from a deleted one by `repo:` search, and indistinguishable from a live
one by an HTML check.**

## p579 — 2026-11-01 — **two additions, and the channel this base registered as unreachable is live: first-hand stars and licences, 30 calls a minute**

🟢 **`Gap 464-D` and `Gap 505-B` are REFUTED.** Both record the GitHub **search** API as
`403` from this session — `464-D` adds that "its failure looks like an empty result", and
[`open-gaps.md`](../intel/open-gaps.md) concluded at the figure-claim register that **a
first-hand star count is "still none"**. Four invocation forms were tried this pass and
**all four answered `200`**:

| Form | Invocation | Response |
|---|---|---|
| A | `gh api "search/repositories?q=topic:knowledge-tracing&per_page=2"` — 🔵 *the exact form `464-D` recorded as 403* | 🟢 **200**, `total_count` `96` |
| B | `gh api -X GET search/repositories -f q='…'` | 🟢 **200**, `96` |
| C | inline with `%3A` percent-encoding | 🟢 **200**, `96` |
| D | `curl -s https://api.github.com/search/repositories?q=…` — 🔵 no `gh`, no token | 🟢 **200**, `96` |
| E | `gh api repos/pykt-team/pykt-toolkit` | 🔴 **403** *"GitHub access to this repository is not enabled for this session"* |
| F | `gh api rate_limit` → `.resources.search` | 🟢 `limit: 30`, `remaining: 30` per minute |

🔴 **The `403` belongs to the per-repo endpoint `/repos/{owner}/{repo}`, not to search.** The
two were collapsed into one gap, and the consequence is large: every search hit carries
`license.spdx_id`, `stargazers_count`, `pushed_at` and `archived` **straight from GitHub**,
for any public repository, at 30 calls a minute. This pass re-measured **47 addresses** with
it. 🔵 This does not resurrect `curl -sI`, which remains uninformative — `403` on all 50
addresses tried here, `moodle/moodle` among them, exactly as `p571`/`P914` already
established.

| Agent | Repo | Licence | Stars | Region | What it is |
|---|---|---|---|---|---|
| Instructional Agents | https://github.com/Hyan-Yao/instructional_agents | MIT | 22 | Global | **ADDIE-model instructional-design system — and the live address for a paper this base has cited at a dead one.** Generates a course end to end: syllabus, slide decks (`.tex`, `.pdf`, `.pptx`), lecture scripts and assessments. *Instructional Agents: Reducing Teaching Faculty Workload through Multi-Agent Instructional Design* — **EACL 2026 Main**, arXiv:2508.19611. 🔵 **`120` forks against `22` stars** — a fork-to-star ratio of `5.5`, the inverted shape of a repository being *run on courses* rather than bookmarked. New to a `3,168`-address ledger. |
| exameow (过了喵) | https://github.com/heshengtao/exameow | Apache-2.0 | 93 | APAC | **Assessment generation, offline-first.** Upload material, get multiple-choice, true/false, fill-in-the-blank and short-answer items. Banks, practice records and wrong-answer history stay **on the device**; the network is only the model call, and that takes any OpenAI-compatible endpoint — DeepSeek, Qwen, GLM — or Ollama locally. Rust (Tauri + Axum) + Vue 3 + SQLite. Simplified and Traditional Chinese READMEs. 🔵 First seen `p201`, carried in the discard **378 passes**, read first-hand this pass. |

### 🟢 Eight licence resolutions the new channel settles in one call each

These are not new licences in the world — they are entries this base's **address ledger**
carried as `unstated` or two-valued *because it believed it had no authoritative channel*.
That belief was the gap refuted above.

| Row | Ledger carried | Resolves to | Stars |
|---|---|---|---|
| `HKUDS/DeepTutor` | `unstated` since `p2`, across `126` mentions | **Apache-2.0** | **52,811** |
| `SirhanMacx/Claw-ED` | `Apache-2.0 \| MIT` | **MIT** | 63 |
| `openedx/XBlock` | `AGPL-3.0 \| Apache-2.0` | **Apache-2.0** | 471 |
| `GeminiLight/gen-mentor` | `CC0-1.0 \| MIT` | **CC0-1.0** | 135 |
| `Citolab/qti-components` | `GPL-3.0 \| GPL-2.0` | **GPL-3.0** | 18 |
| `Li-Evan/Bloom` | `unstated` | **MIT** | 295 |
| `ZhijieXiong/pyedmine` | `unstated` | **MIT** (also read first-hand) | 82 |
| `HumphreySun98/Smart-Study-Agent` | `unstated` | **MIT** | 57 |

🟢 **`DeepTutor` re-measured at `52,811★`** — the `p577` shelf figure of `52.7k` holds — and
independent daily trend reports put it as GitHub's **largest single-day star gainer on both
2026-10-30 and 2026-10-31** (≈`1,930` and ≈`2,280` in a day).

### 🔴 Two ledger rows that contradict this base's own published verdict

Neither is a new licence finding. Both licences were read and published passes ago. What is
new is that the **machine-readable ledger column disagrees with the pages**, and the ledger
is what the gates read:

| Address | Ledger column | What the pages already say | Defect |
|---|---|---|---|
| `CaviraOSS/PageLM` | **`MIT`** | `BLOCK` / `REFUSED` / "bespoke non-commercial"; `LICENSE.md` read at `8,563 B`; recorded as *"MIT's body verbatim, then commercial-use, SaaS and resale restrictions"* | 🔴 ledger only — and the verbatim-MIT body is exactly why a body-matching reader says MIT |
| `xiaoyang111222/cn-math-taxonomy` | **`CC-BY`** | **CC BY-NC 4.0** (`19,347 B`), with `Gap 572-C` declaring the NonCommercial block | 🔴 ledger only — the **NC** term, the one that decides commercial use, is absent from the column |

🔵 **The pages are right and were right.** The lesson is about instrument hygiene: a
licence column that drops a NonCommercial term is worse than an empty one, because a gate
reading it will pass the row.

### 🔴 The dead-address test — `422` and `0` mean different things

| Address | Response | Reading | Live address |
|---|---|---|---|
| `openedx/edx-platform` | **`422`** | name no longer resolves — look for a rename | `openedx/openedx-platform`, **AGPL-3.0**, `8,213★` (this base has carried it since `p28`) |
| `OpenEduCat-Inc/OpenEduCat` | **`422`** | the *owner* no longer resolves either | `openeducat/openeducat_erp`, **LGPL-3.0**, `903★` (carried since `p2`) |
| `DaRL-GenAI/instructional_agents` | **`0` results** | owner resolves, repository does not exist | `Hyan-Yao/instructional_agents`, **MIT**, `22★` — shelved above |

🔵 `422` says *the name is wrong*; `0` says *the name is right and the thing is gone*. The
`DaRL-GenAI` org still exists with `15` repositories, of which the only survivors of this
work are `instructional_agents-skills` (`1★`), `_studio` (`0★`) and `_homepage` (`0★`) —
which is why the `0` rather than a `422`.


## p578 — 2026-10-31 — **four agents added, every one from an axis never queried in 577 passes, and the head of the largest of those axes is GPL-3.0**

🟢 **The shelf is `20`.** The sixteen rows `p577` verified stand unchanged — they were
verified the same day, by the same instrument, and nothing on this pass contradicts them.
The four rows below are **new addresses to this base**, each verified this pass by fetching
its repository page and reading the licence, star count and description off that page.

| Agent | Repo | Licence | Stars | Region | What it is |
|---|---|---|---|---|---|
| Clew | https://github.com/miuuyy/Clew | MIT | 214 | Global | **Prerequisite-graph learning harness.** You state what you know and what you want to learn; it builds an interactive map of topics and prerequisites and proposes a path. Ships as a desktop app (graphs stored locally) and as a ChatGPT plugin. The curriculum-sequencing layer this base had no permissive component for. |
| Antura | https://github.com/vgwb/Antura | BSD-2-Clause (code); CC-BY-4.0 (art and media) | 128 | EMEA | **Literacy and language-learning game for children.** Unity 6.x, iOS / Android / desktop. Ships Arabic, **Darija**, English, French and Polish. Descends from the Antura *EduApp4Syria* game. 🟢 **The largest EMEA-placeable row on this shelf — 5.3× `feedbacksystem` (24★)** — and the only one with a non-Latin-script content pipeline. |
| GeoChat | https://github.com/tiwe0/GeoChat | Apache-2.0 | 125 | Global | **Local-first AI maths visualisation over GeoGebra.** Describe a construction in natural language; it builds it on the canvas, checks it and explains it beside the figure. Reads the live canvas and the current selection; 2D and 3D; native tool calling; bring-your-own API key; keys and chat history stay on the device. Tauri + React + Bun, macOS and Windows. |
| Coding-Tutor | https://github.com/iwangjian/Coding-Tutor | Apache-2.0 | 92 | Global | **Traver** (trace-and-verify) dialogue-tutoring agent — knowledge tracing plus turn-by-turn verification — shipped with **DICT**, an evaluation protocol that pairs **simulated students** with coding tests, plus trained verifier checkpoints (`jwanglvy/Verifier-7B`). ACL 2025 Findings, arXiv `2502.13311`. |

### 🟢 `Coding-Tutor` partly closes the gap `p573` named

`p573` registered, for this page, that *"there is no usable learner-simulation agent, which
is how a tutor gets tested before it meets a student."* **DICT is that instrument, under
Apache-2.0**: simulated students paired with pre- and post-tests, with the dialogues
(`output/dialogue.zip`) and the verifier checkpoints published. 🔴 **It is not a general
learner simulator** — the task domain is code, and the coding tasks come from
`EvoCodeBench-2403`, which must be downloaded separately under its own terms. So the gap
narrows from *absent* to *domain-bound*, which is a different engagement conversation.

### 🔴 Rejected this pass, and the first rejection is the head of the axis

- **`plastic-labs/tutor-gpt` — GPL-3.0, 933★.** It heads **two** of the five axes swept
  (`topic:tutoring` and `topic:literacy`) and is **the largest dedicated tutoring agent
  this base has found outside APAC** — 3.4× the largest North-America-placed row on this
  shelf. 🔴 **And it is copyleft**, so it fails the permissive bar every pattern on
  [`../compose/patterns.md`](../compose/patterns.md) is built to. Recorded rather than
  shelved: a studio that reaches for "the obvious open-source AI tutor" lands here, and
  needs to be told why it cannot ship it.
- **`eth-lre/mathtutorbench` — 46★, EMNLP 2025 Oral, and the grant contradicts itself on
  its own page.** The badge reads *License: CC BY 4.0*; the closing text reads
  *"Attribution-**ShareAlike** 4.0 International"*. 🔴 Either way it is a **content**
  licence on a code-and-benchmark repository. Unusable as a dependency until the holder
  resolves it — and it is painful, because an EMEA-origin pedagogical benchmark is exactly
  what this base is short of (it holds one evaluation instrument, `pedagogy-benchmark`,
  and that one is LATAM).
- **`Doenet/DoenetApps` — AGPL-3.0, 17★.** Copyleft and below any size floor. No funder or
  affiliation is stated on the page, so the NSF-style provenance a reader might assume
  from `doenet.org` **is not evidenced** and is not recorded.
- **`goplus/xgo` — 9.5k★, heads `topic:stem-education`, and is a programming language.**
  Second instance of the class `p577` caught with `ux-ui-agent-skills`: the biggest row on
  an education axis need not be an education tool. Its sibling `goplus/spx` (Apache-2.0,
  124★) **is** the education artefact in that org and is shelved one page over, in
  [`../repos/foundations.md`](../repos/foundations.md), because it is an engine, not an agent.

### 🔵 Skill bundles found this pass — components, not shelf rows

The standing convention (see *Agent-skill bundles* below) holds, and it costs a big row to
honour it: **`SenmuuuuW/universal-diagnostic-tutor-skill` is MIT and 254★** — larger than
**13 of the 16** rows `p577` verified — and is still **not** shelved, because it is one
narrow instruction set rather than an agent an engagement is built around. Same disposition
for `ndpvt-web/deeptutor-claude-skill` (37★) and `lowwwbank/anything-to-course` (29★), both
already known to [`trending.md`](trending.md). 🔵 Recorded explicitly so a later pass does
not read their absence as an oversight and "fix" it.

### 🔵 Adoption caveat on `GeoChat`, stated because it is not in the licence field

Its README grants **GeoChat's own source and documentation** under Apache-2.0. The
GeoGebra component it drives is a **separate work under its own terms, which were not read
this pass.** Read them before shipping GeoChat to a client; the permissive grant on the
wrapper says nothing about the engine inside it.

### 🔵 Method — the verifier is still `WebFetch`, and `curl -sI` is still noise

`p577`'s method correction was re-exercised, not assumed: every row and every rejection
above came from a `WebFetch` of the repository page. The axis denominators came from
single-topic GitHub search URLs — never the `topic:X OR topic:Y` form, which `p576` proved
returns a false zero (`576-A`). Denominators in
[`../evidence/axis-denominators.2026-10-31-p578.tsv`](../evidence/axis-denominators.2026-10-31-p578.tsv),
row-by-row verdicts in
[`../evidence/verified-repos.2026-10-31-p578.tsv`](../evidence/verified-repos.2026-10-31-p578.tsv).

## p577 — 2026-10-31 — verified shelf

Every row below was verified individually on 2026-10-31 by fetching its GitHub
repository page and reading the licence, star count and description off that page.
No row is carried over on trust from an earlier pass. Rows that failed
verification, or that turned out not to be education tools, are listed under
*Rejected this pass* and are not in the table.

**16 agents qualified.** They are ordered by size, and each is placed in a region
when the repository itself supports a placement.

| Agent | Repo | Licence | Stars | Region | What it is |
|---|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 52.7k | APAC | Lifelong personalised tutoring. The largest open-source education agent found in any region. HKUDS (University of Hong Kong). |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 42.2k | APAC | Open Multi-Agent Interactive Classroom — a one-click immersive multi-agent learning experience. Tsinghua (THU-MAIC). |
| Oppia | https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Global | Free online learning platform built around interactive "explorations". Both a platform and an authoring model. |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Global | Assigns and autogrades Jupyter notebooks. The autograding seam for technical coursework. |
| educhain | https://github.com/satvik314/educhain | MIT | 387 | Global | Python package that generates educational content with generative AI. Item-bank and worksheet generation. |
| ltijs | https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | Global | Turns an application into a full LTI 1.3 tool provider. The integration seam into any LMS without forking it. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 274 | North America | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase). UC Berkeley CAHLR. |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 159 | Global | Block-based adaptive learning workspace that runs locally; self-hosted, 10+ LLM providers. |
| catsim | https://github.com/douglasrizzo/catsim | BSD-3-Clause | 153 | Global | Computerised Adaptive Testing simulator. Lets you simulate item selection before exposing learners to it. |
| girth | https://github.com/eribean/girth | MIT | 127 | Global | Item Response Theory package for Python. Item calibration. |
| feedbacksystem | https://github.com/thm-mni-ii/feedbacksystem | Apache-2.0 | 24 | EMEA | Intelligent, personalised feedback for students. Technische Hochschule Mittelhessen (Germany) — the org slug `thm-mni-ii` is the institution and faculty. |
| Terracotta | https://github.com/terracotta-education/terracotta | Apache-2.0 | 21 | North America | LMS plug-in that randomly assigns content variations to student groups for controlled education experiments, with consent hidden from the instructor and identifiers stripped from exports. |
| warren | https://github.com/openfun/warren | MIT | 17 | EMEA | Learning-analytics visualisation toolkit (xAPI). **Its own README states it is a proof of concept, not yet suitable for production** — do not put it in front of a client. Org `openfun`; affiliation not stated on the repo page. |
| libro-3d-interactivo | https://github.com/csepulvedai/libro-3d-interactivo | MIT | 14 | LATAM | Claude Code skill producing interactive 3D pop-up educational books in Three.js, with Chilean-Spanish narration, aligned to Chilean curriculum objective OA 13. Author at Universidad de Los Lagos, Chile. |
| pedagogy-benchmark | https://github.com/AI-for-Education/pedagogy-benchmark | MIT | 13 | LATAM | Benchmark of the pedagogical knowledge of LLMs, built from exams developed by Chile's Agencia de la Calidad de la Educación and CPEIP. The only verified evaluation instrument on this shelf. |
| potsie | https://github.com/openfun/potsie | MIT | 11 | EMEA | Grafana dashboard suite for learning analytics. The production-ready alternative to `warren` for dashboards. |

### Licence position

Fifteen of the sixteen are MIT, Apache-2.0 or BSD-3-Clause — all buildable. The
agent layer licenses *permissively*, which is the opposite of the platform layer
(see [`../repos/foundations.md`](../repos/foundations.md), where every LMS of
record is copyleft). That asymmetry is the single most useful fact on this page:
the AI can be built permissively and attached to a copyleft LMS from the outside.

### Rejected this pass

These were on the shelf, or were candidates, and do not belong on it:

- **github.com/plugin87/ux-ui-agent-skills** — MIT, 3.1k stars, and **not
  an education tool at all**. It is a design-system knowledge layer for coding
  agents ("Turn Claude into a senior design architect"). It mentions no student,
  learner or classroom use. It was the second-highest-starred row on the previous
  shelf, which is how a miscategorisation survives: size reads as credibility.
- **github.com/bigdata-ustc/Agent4Edu** — 100 stars, AAAI 2025 oral
  presentation, and **no licence file**. Academically real, legally unusable for
  client work. Merit does not substitute for a grant.
- **github.com/littlebordercollie/mcd-together-order** — 101 stars. A
  prototype for ordering at McDonald's through MCP, so that students with
  intellectual disabilities can choose meals from picture cards and a parent
  completes the purchase. It is assistive communication, not tutoring; the README
  states it is a contest prototype with **no trial with students yet**; and the
  licence type is not named on the repository page. Three independent reasons not
  to recommend it.
- **github.com/bayshores/godspeed** — AGPL-3.0 and **7 stars**. Fails the
  permissive-licence bar and any reasonable size floor. It is a fork of
  LearnHarness.
- **Ten `github.com/topics/...` URLs** (`topic:adaptive-learning`,
  `topic:qti`, `topic:knowledge-tracing`, `topic:dyslexia`, `topic:flashcards`,
  `topic:sign-language`, `topic:curriculum`, `topic:lesson-plan`,
  `topic:handwriting-recognition`, `topic:intelligent-tutoring-system`) were
  sitting in repository columns. A topic listing page is a **search axis**, not a
  repository. It cannot be cloned, has no licence, and must never compile into an
  entity.

### Corrections to figures this base has been publishing

Verified today against the repository pages. The previous star figures were wrong
in both directions, so they were not a consistent scaling error — they were not
measured:

| Repo | Previously published | Verified 2026-10-31 |
|---|---|---|
| HKUDS/DeepTutor | ~24k | **52.7k** |
| CAHLR/OATutor | ~1.5k | **274** |
| zijinz456/OpenTutor | ~9xx | **159** |
| thm-mni-ii/feedbacksystem | flagship EMEA agent | **24** |

### Method correction — the prescribed URL verifier certifies nothing

The standing instruction is to verify every URL with `curl -sI`. In this
environment **that check cannot distinguish a real repository from a fabricated
one.** The agent proxy returns `HTTP 403` for every `github.com` URL, including a
control URL that does not exist:

```
403  https://github.com/moodle/moodle                     (real)
403  github.com/gmilano/nonexistent-repo-xyz      (does not exist)
```

`gh api repos/<owner>/<name>` is also unavailable — GitHub API access is scoped to
`gmilano/globant-kb` and returns "GitHub access to this repository is not enabled
for this session" for every third-party repo. The proxy itself is healthy
(`bundleCoversEveryHost: true`, no recent relay failures), so this is policy, not
breakage.

**WebFetch does discriminate**, and is the verifier that works: a real repository
returns its licence, stars and description; a non-existent one returns `HTTP 404`.
Every row on this page was verified that way. Any future pass that reports
`curl -sI` output as verification is reporting noise.

---

## Prior passes (superseded, retained for history)

Everything below predates p577 and was **not** re-verified. The figures in it are
known to be unreliable — see the corrections table above. It is kept because it
records the search axes that have been swept, which is still useful, and because
`agents/trending.md` references it.

### (archived) Top AI agents for education

<!-- machine-readable count claim, p569, for ingest/derive-counts.py -->
`derived shelf: **39**` — the shelf table below, counted with that gate's own row
regex, bounded at the first `###`. 🟢 **`p576` added `4` rows** (`L.A.R.A`,
`gaokao-mentor-wisdom`, `gaokao-advisor`, `libro-3d-interactivo`), all `4` addresses new to
this base, every grant read first-hand and every byte figure re-measured by piping to
`wc -c`. 🔴 **Not** the figure the gate actually derives: its scan runs `## The shelf` →
next `##` and so swallows `### Carried with a known defect` and `### Agent-skill bundles`,
deriving **48**. 🔵 `p574` recorded that spread as `33`; `p575` remeasured it at
**44 against 35**, and `p576` at **48 against 39** — the `9`-row difference is exactly those
two sub-tables, unchanged. See `568-E`, now quantified as `575-B`.

🟢 **CORRECTION TO `575-B`, AND IT IS THIS PASS'S BEST NEWS: THE GATE RAN.**
`python3 -I ingest/derive-counts.py` **executed from this session**, so `575-B`'s
"no gate can run" was over-generalised from a single denial. 🟢 **It derived `48` against
`claimed=None` and reported `AMBER no count in the shelf heading; nothing to compare
against` — confirming `575-B`'s diagnosis exactly, and confirming this claim block's own
predicted figure of `48`.** 🔴 Still **deliberately not patched**, per `574-G`.

Every row below was verified on 2026-10-31. **The fifth pass swept the axis the
fourth pass named as blind: capability topics rather than industry topics.** The
fourth pass closed with an explicit instruction — *"sweep by capability
(`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`) and licence, not
only by industry topic"* — and that sweep returned a large, permissively licensed
**horizontal supply layer** which is shelved in
[`../repos/foundations.md`](../repos/foundations.md), not here, because none of it
is an education agent.

**Twenty-four agents qualified, up from nineteen.** The five new rows came from
two axes the industry-topic sweeps cannot reach:
`topic:intelligent-tutoring-system` and `topic:learning-analytics`. Both are
small populations (5 repositories each above the star floor) and **both were
unswept in four passes** — which is why a 135★ WWW-2025 oral-track system and the
KB's **first verifiable EMEA-origin education agent** were both missing.

**Two standing gaps moved this pass:**

- **EMEA agent origin is no longer empty.** `thm-mni-ii/feedbacksystem` is
  **Apache-2.0** and its licence file reads *"Copyright 2021 Technische
  Hochschule Mittelhessen"* — a named German university, in the grant itself.
- **Region became recoverable for institutional publishers.** See the method note:
  the licence file's copyright line places a repository when the holder is an
  **institution**, and the seven rows this KB records as `Global` were re-probed
  against that instrument and **stay Global** — their holders are individuals.

**The `topic:ai-education` axis is now genuinely saturated**, which is a
different claim from the one the previous pass retracted. Re-running the fourth
pass's own discovery query (`topic:ai-education stars:>150 pushed:>2026-10-20`)
returns the **same 6 repositories**, all already shelved. The axis is exhausted;
the population is not, and the capability sweep is the proof.

## 🆕 `p576` — fourteenth pass, 2026-10-31 — 🔴 **FOUR AGENTS ADDED, ALL FOUR THIN, AND THE PASS'S REAL RESULT FOR THIS PAGE IS THAT A QUERY FORM THIS BASE HAS USED SIX TIMES RETURNS A FALSE ZERO**

🔴 **`topic:X OR topic:Y` in a GitHub search URL returns `0 results` — "Your search did
not match any repositories" — where the same two topics, queried singly, return hundreds.**
Measured with controls on four pairs:

| query | results |
| --- | --: |
| `topic:autograding OR topic:autograder` | 🔴 **0** |
| `topic:autograding` | 🟢 **93** |
| `topic:autograder` | 🟢 **128** |
| `topic:educacion OR topic:educacao` | 🔴 **0** |
| `topic:educacion` / `topic:educacao` | 🟢 **410** / **378** |
| `topic:cbse OR topic:ncert` | 🔴 **0** |
| `topic:cbse` | 🟢 **131** |

🔴 **This base has recorded six axes in that form** — `topic:deped OR topic:nigeria` (×6),
`topic:cbse OR topic:ncert` (×6), `topic:kaoyan OR topic:gaokao` (×3),
`topic:special-education OR topic:iep` (×2),
`topic:intelligent-tutoring-system OR topic:learning-analytics`,
`topic:autograding OR topic:autograder`. **Any nil they produced is void.** Registered as
**`576-A`**, filed as **trend 25**, evidence in
[`../evidence/or-form-false-nil.2026-10-31-p576.tsv`](../evidence/or-form-false-nil.2026-10-31-p576.tsv)
and [`../evidence/or-form-axes-in-base.2026-10-31-p576.tsv`](../evidence/or-form-axes-in-base.2026-10-31-p576.tsv).

🟢 **And the honest half, which matters more than the defect:** four of those axes were
re-run as singles and read deep. **Of the `24` top-of-ladder repositories they returned,
`18` were already in this base** — so **the broken form corrupted this base's published
denominators, not its discovery.** 🔵 The supply had been reached by other axes. **Six
addresses were new, and every one is small**; four of them qualified on licence and are
shelved below, with their star counts stated plainly.

🟢 **`topic:intelligent-tutoring-system` (`43`) is the one axis where the void nil hid
something real** — its head is `open-spaced-repetition/fsrs4anki` at **`4,100★`**, and
`tutor-mcp` and `GenMentor`, already on this shelf, both sit on it. 🔵 Nothing new to shelve
there; the axis belongs in the method note so the next pass does not re-run it hopefully.

🔴 **A second instrument result, about this pass's own probe.** The grant probe silently
fetched **nothing** for `8` real repositories — `curl` read a `-w` format string beginning
with `@` as *"load format from file"* and errored on every call — **while the fabricated
control still returned `DEAD-OR-ABSENT` and so still looked like a pass.** 🔵 **The control
exercised only the `git ls-remote` branch, and therefore certified nothing about the
`raw.githubusercontent.com` branch it was there to protect.** Caught, fixed, re-run.
Registered as **`576-D`**: *a control must exercise every branch of the instrument it
certifies* — the same family as `575-F`, found the same way, in this pass's own work.

🔴 **Byte counts in this pass were initially `0`–`2` B low**, because `$(...)` strips
trailing newlines: this page's existing `1,068 B` for `education-skills` was right and the
probe's `1,067 B` was wrong. 🟢 **Every byte figure written this pass was re-measured by
piping straight to `wc -c`**, and the two instruments agree once the offset is known. 🔵
Trend 24 — *a count without its instrument is not a measurement* — applied to this base's
own byte figures.

## 🆕 `p575` — thirteenth pass, 2026-10-31 — 🟢 `574-C` closed as a **BUILD recommendation**: the education-specific special-education layer is a hobby tier, and the `topic:iep` axis tops out at **7★**

🟢 **`574-C` prescribed four axes and all four were swept, with denominators read off
GitHub's own result counts:** `topic:special-education` (**89**),
`topic:assistive-technology` × `topic:education` (**27**), `topic:iep` (**34**) and
`topic:screen-reader` (**594**) — **`744` repositories across four axes never queried
in `574` passes.**

🔴 **The answer `574-C` asked for is the one it guessed: there is no mature,
education-specific, permissively licensed accessibility agent, and the reason is
not licensing — it is that nobody has built one.** The education-specific tier is a
**hobby tier**, and the star ladder is the whole finding:

| axis | repositories | top ★ | then | verdict |
| --- | --: | --: | --- | --- |
| `topic:special-education` | **89** | **101** | 10, 7, 5, 4, 3, 3, 3, 1, 1 | 🔴 one repo above 11★ |
| `topic:iep` | **34** | **7** | 3, 3, 2, 1, 1, 1, 0, 0, 0 | 🔴 **the entire axis is under 8★** |
| `topic:assistive-technology` × `education` | **27** | **8** | 4, 3, 3, 2, 1, 1, 1, 1, 0 | 🔴 nothing above 8★ |
| `topic:screen-reader` | **594** | **2,700** | 728, 591, 431, 291, 173, 158, 150 | 🟢 real engineering — but **horizontal** |

🔵 **Read those two bottom rows together and the recommendation writes itself.** The
`screen-reader` axis has NVDA at `2.7k★` and a tested automation layer at `591★`;
the `iep` axis — the one that names the artefact every US special-education
engagement turns on — **has nothing above 7★.** The supply is not badly licensed,
it is **absent**, and `574-C` was right to say that an informed absence is the more
valuable answer. 🟢 **So: BUILD, on the horizontal layer, shelved in
[`../repos/foundations.md`](../repos/foundations.md).** The recipe is
[`P-575-A`](../compose/patterns.md).

🟢 **Six rows did qualify** — MIT, every grant read byte-for-byte from the licence
file itself — and they are shelved below. 🔴 **Five of the six are at or under 3★,
and the shelf says so in each row**; they are shelved because the axis is new and
the fit is exact, not because the artefact is mature. The one real find is
**`mcd-together-order`** (`101★`, MIT): the **first MCP-native AAC agent** this base
has seen, and it is **pre-pilot by its own admission** — no student trials, one ¥12
order created and never paid.

🔴 **A defect in this page's own count gate, measured exactly (`575-B`).** The header
claim below reads `29` and it is **correct about the shelf table**. But
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) scans `## The shelf` →
**next `##`**, which swallows `### Carried with a known defect` and `### Agent-skill
bundles`, and derives **`38`** — so the gate, if it could compare at all, would call
a right page RED by `9` rows. 🔵 **It cannot compare**: it reads the claim with
`re.search(r"(\d+)", lines[start])` from the *heading line*, `## The shelf` carries
no digit, so the gate has **AMBERed on this page since it was written** while the
prose figure drifts unchecked. 🔵 That is `568-E` — but quantified: `29` against
`38`, and the two `###` sub-tables are exactly the `9`.
## 🆕 `p574` — twelfth pass, 2026-10-31 — 🔴 NO NEW AGENT QUALIFIED AGAIN, and the reason is worth more than a row: the layer the `2027`/`2028` **accessibility deadlines** create demand for has **agent-shaped MIT supply that is horizontal, not educational** — `2` MIT agent bundles enforcing **WCAG 2.2 AA**, shelved in [`../repos/foundations.md`](../repos/foundations.md) under the fourth pass's own rule

🔵 **Why this pass went looking here.** `p572` shelved the LTI 1.3 / xAPI plumbing
layer after finding it in the discard pile. This pass asked the next question —
*what else does an LMS engagement bill for that this base has never named?* — and
the answer is **digital accessibility**, which is the one education obligation on
these shelves with a **dated legal deadline in two regions**. 🔴 **`Title II`
appears `0` times in `573` passes of this base's history: not in the README, not in
the gap register, not on any shelf page.**

### 🟢 Six GitHub axes, none of them ever queried in 573 passes, `911` repositories visible

| axis | repositories | prior queries in this base | new addresses read |
| --- | --: | --: | --: |
| 🟢 [`topic:accessibility` × `topic:education`](https://github.com/search?q=topic%3Aaccessibility+topic%3Aeducation&type=repositories) | **425** | 🔴 `0` | 4 |
| 🟢 [`topic:dyslexia`](https://github.com/topics/dyslexia) | **257** | 🔴 `0` | 5 |
| 🟢 [`topic:aac` × `topic:accessibility`](https://github.com/search?q=topic%3Aaac+topic%3Aaccessibility&type=repositories) | **126** | 🔴 `0` | 6 |
| 🟢 [`topic:qti`](https://github.com/topics/qti) | **52** | 🔴 `0` | 8 |
| 🟢 [`topic:wcag` × `topic:accessibility`](https://github.com/search?q=topic%3Awcag+topic%3Aaccessibility&type=repositories) | **29** | 🔴 `0` | 3 |
| 🟢 [`topic:sign-language`](https://github.com/topics/sign-language) (`stars:>80`) | **22** | 🔴 `0` | 4 |

🟢 **`29` addresses read byte-for-byte, `13` of them new to a 573-pass base, and
`24 of 25` checked were absent from EVERY shelf page.** Full grant reads in
[`../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv`](../evidence/accessibility-qti-licence-bytes.2026-10-31-p574.tsv)
(`30` rows: `29` addresses + `1` fabricated control, which answered
`DEAD-OR-ABSENT`, so the channel discriminates).

### 🔴 Why no row was added to THIS page

🔴 **The two qualifying MIT artefacts are not education agents.** The fourth pass
set the rule this page still runs on — *a horizontal capability layer is shelved in
`foundations.md`, not here, because none of it is an education agent* — and both
of this pass's MIT finds are exactly that:

- [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents)
  — **MIT**, licence file `1,069 B`, `package.json` agrees — **431★**. Eleven
  review specialists enforcing **WCAG 2.2 AA** for Claude Code, GitHub Copilot and
  Claude Desktop. Agent-shaped, and **domain-agnostic**: nothing in it knows what a
  course is.
- [`plugin87/ux-ui-agent-skills`](https://github.com/plugin87/ux-ui-agent-skills)
  — **MIT**, licence file `1,073 B`, `package.json` agrees — **3.1k★**. DTCG
  tokens, 52 components, **WCAG 2.2 AA–AAA**, 138 design systems.

🟢 **Both are shelved, with first-hand grants, in
[`../repos/foundations.md`](../repos/foundations.md).** 🔵 This is the second
consecutive pass whose honest result for this page is *a placed gap rather than a
row*, and the gap is now specific: **there is no education-specific accessibility
agent — nothing that reads a course, a cohort or an IEP and acts on it.** The
nearest candidate found,
[`Jojobeans1981/Ember-Campfire-Edition`](https://github.com/Jojobeans1981/Ember-Campfire-Edition)
(an AI dyslexia-intervention platform, 24★), **carries no licence file on a
44-name ladder** — so it is unshelvable, not merely small. Registered `574-C`.

## Eleventh pass (`p573`, 2026-10-31) — 🔴 NO NEW AGENT QUALIFIED, and the pass's result for this page is a **gap with a name**: there is no usable learner-simulation agent, which is how a tutor gets tested before it meets a student

🔴 **Two agent-native axes were swept to exhaustion of their top rows and yielded
`0` addresses new to this base:**

| axis | repositories | rows read | new to this base |
| --- | --: | --: | --: |
| 🔴 [`topic:intelligent-tutoring-system`](https://github.com/topics/intelligent-tutoring-system) | **42** | 20 | 🔴 **0** |
| 🔴 [`topic:knowledge-tracing`](https://github.com/topics/knowledge-tracing) | **102** | 20 | 🔴 **0** |
| 🔴 [`topic:adaptive-learning`](https://github.com/topics/adaptive-learning) | **635** | 20 | 🔴 **0** |
| 🔴 `WebSearch`, four mandated legs | — | 4 | 🔴 **0** |

🟢 **That is a real result, not a blank pass.** `topic:intelligent-tutoring-system`
is the axis most precisely named for this page's subject, and **every one of its
top 20 was already shelved here** — `fsrs4anki`, `education-agent-skills`,
`gen-mentor`, `tutor-mcp`, `Tutorbot-Spock`, `Bloom`, `OpenTutor`,
`TheGrandQuiz`. 🔵 **This page's tutoring-agent shelf can now be stated as
measurably complete against GitHub's own topic vocabulary**, which is a stronger
claim than the "saturated" language earlier passes used, and it is the first time
it has been checked against the *correctly named* axis rather than against
star-sorted general search.

🔴 **`topic:adaptive-learning` (635) is a polluted axis and should not be swept
again.** Its top 20 contains a screen-brightness daemon (`wluma`, 955★),
adaptive flight control, Monte Carlo materials-design libraries and concept-drift
detection for IoT streams. **"Adaptive learning" in GitHub's tag space mostly
means adaptive *machine* learning.** Recorded so the next pass spends its budget
elsewhere.

### 🔴 The gap this pass can name precisely: learner simulation is unlicensed

🔵 **Why it matters.** Before a tutoring agent is pointed at students, the honest
way to test it is against *simulated* learners with known ability parameters —
you can then check whether the tutor's inferences recover the truth. Every
efficacy pattern in this KB (`P-570-C`, `P-571-A`) implicitly needs this.

🔴 **The only purpose-built learner-simulation agent located in this base is
[bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu)** (100★,
AAAI 2025 — "LLM-based agents that generate simulated learner response data"),
🔴 **and it has no licence file on `HEAD`** (`LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING` all 404 this pass). 🔴 **It is cited on `4` live files of
this KB with no such caveat.** Default is exclusive copyright: it may be read,
not shipped.

🟢 **The usable substitute, and it is a downgrade stated honestly:** generate
synthetic response matrices from a calibrated IRT model using the **permissive
Python tier** — [eribean/girth](https://github.com/eribean/girth) (**MIT**,
first-hand) or [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim)
(**BSD-3-Clause**, first-hand), which simulates examinees directly. 🔵 That gives
statistically controlled synthetic learners but **not** the LLM-mediated
conversational behaviour Agent4Edu models. 🔴 **So the gap is real and stays
open: no permissively licensed *conversational* learner simulator exists.**
Registered `573-A`.

### 🔴 Licence correction to a row this page carries

| Row | Status before this pass | Read first-hand this pass |
| --- | --- | --- |
| [bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) | cited on `4` live files, no grant stated | 🔴 **⛔ NO LICENCE — all-rights-reserved** |

🟢 **Control that passed:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
re-read byte-for-byte this pass — `LICENSE` is **11,408 B** and opens "Apache
License / Version 2.0, January 2004". 🟢 **This page's `Apache-2.0` is correct**,
and two third-party roundups circulating this month that call DeepTutor "MIT" are
wrong. 🔵 Recorded because it is the cheap half of trend 18: the sidebar-free
byte read settles it in one probe.

### 🔵 Gate posture — probed, and the mandated command is unsafe here

🔴 **`curl -sI https://github.com/…` answers `403` on this harness for real and
invented repositories alike**, so the prescribed verification cannot discriminate
and its failure direction is *unsafe* — a `403` is not a `404`, so an invented
address passes. 🟢 **`raw.githubusercontent.com/{repo}/HEAD/{path}` discriminates
`200`/`404` correctly** (controls in `repos/foundations.md`, eleventh pass) **and
returns licence bytes in the same call.** Every licence claim added this pass used
that channel.


## Tenth pass (`p572`, 2026-10-31) — 🟢 THE NIL BROKE, AND IT BROKE ON A NEVER-SWEPT AXIS OF `44` REPOSITORIES — while the real finding is that this base has seen `3,455` addresses and shelved `170`

🟢 **`derived shelf: 29`, up from `24`.** 🟢 **`12` addresses new to a 571-pass
base, after NINE consecutive nil passes** — and not one of them came from the
eight mandated legs.

| channel | legs / rows | addresses NEW to this base |
| --- | --: | --: |
| 🔴 `WebSearch`, the eight mandated legs (4 global, 4 regional) | 8 | 🔴 **`0`** — **TENTH consecutive nil** |
| 🟢 [`topic:lesson-plan`](https://github.com/topics/lesson-plan) (**44** results) | 10 | 🟢 **`6`** |
| 🟢 [`topic:handwriting-recognition`](https://github.com/topics/handwriting-recognition) (**672**) | 10 | 🟢 **`6`** |
| 🔴 [`topic:flashcards`](https://github.com/topics/flashcards) (**3.3k**) | 10 | 🔴 **`1`** — `read-frog`, `word-atlas`, `LibreLingo` all already held |
| 🔴 [`topic:curriculum`](https://github.com/topics/curriculum) (**1.5k**) | 10 | 🔴 **`0`** — the `topic:mooc` pattern exactly: course *materials*, not delivery software |
| 🟢 `raw.githubusercontent.com` grant reads | 32 addresses | 🟢 **`28` grants read byte-for-byte**, 2 proved ungranted at 40 probes each |
| 🟢 `git clone --filter=blob:none` + `git rev-list` | 8 | 🟢 **8 exact commit counts, 0 failures** |
| 🔴 `curl -sI` → `github.com` / `api.github.com` | 2 | 🔴 **403 both.** The harness's prescribed link check is unavailable; existence proved by `raw` 200/404 with a fabricated control instead |

### 🟢 `topic:lesson-plan` is the smallest productive axis this base has ever swept

🟢 **`44` results — and `6` of the top `10` were new.** 🔵 The reason the big axes
are exhausted and this one was not: **`44` repositories is too small a field to
reach any "top" list**, so nine passes of star-sorted sweeping could not see it.
🟢 The field is also **overwhelmingly non-anglophone** — mainland-China K-12,
Malaysian Chinese Independent Schools (独中), a Chinese medical-licensing toolkit —
which is why **four of the six new rows place outside North America on first-hand
evidence**, against three passes that published "EMEA/APAC gained no placed row".

🔴 **And every one of them is thin.** The six new `lesson-plan` rows carry
`5`, `7`, `8`, `16`, `41` and `2` commits. 🔵 **This is a template tier, not a
dependency tier**, and it is shelved as such: the value is the *feature taxonomy*
these teachers converged on independently (lesson plan → courseware → item bank →
dictation/marking), not the code.

### 🔴 The pass's largest finding is about this base, not about GitHub

🔴 **`3,455` distinct GitHub addresses appear in this base's own history.
`170` of them — `4.9 %` — have ever reached a shelf page.** 🔵 A low rate is
*correct* for a curated shelf; the defect is not the rate but **what sits in the
discard**. Ranked by recurrence, the top of the unshelved list is not noise:

| address | times seen | status |
| --- | --: | --- |
| `openedx/edx-platform` | **218** | 🔴 **LINKING DEFECT** — named `15×` in shelf prose, **never with its address** |
| `openedx/XBlock` | **123** | 🔴 absent entirely — **Apache-2.0**, now shelved |
| `bruchris/canvas-lms-mcp` | **115** | 🔴 absent entirely — **MIT**, now shelved |
| `ls1intum/Artemis` | **97** | 🔴 absent entirely — **MIT**, now shelved |
| `opencast/opencast` | **93** | 🔴 absent entirely — **ECL-2.0**, now shelved |
| `francoisjacquet/rosariosis` | **92** | 🔴 absent entirely — GPL-2.0, now shelved |
| `frappe/erpnext` | **84** | 🔴 absent entirely — GPL-3.0, now shelved |
| `GibbonEdu/core` | **83** | 🔴 absent entirely — GPL-3.0, now shelved |
| `yetanalytics/lrsql` | **70** | 🔴 absent entirely — **Apache-2.0**, now shelved |

🔴 **Four of those nine are permissive, and the whole LTI 1.3 / xAPI integration
layer — the plumbing every LMS engagement actually bills for — was absent from
every shelf page in this KB while being re-found `70`–`123` times.** 🟢 **`11` of
the `12` tested are absent *entirely*, not merely unlinked**, so this is a
shelving failure and not a citation-style quibble. 🔵 **Rule, stated to transfer:
discovery and shelving are different pipelines, and this base has been measuring
only the first.** Registered as `572-A`.

### 🔵 Method note: the mandated legs are now measurably the weakest channel

🔵 Across **ten** passes the eight mandated `WebSearch` legs have produced **zero**
addresses new to this base. This pass they also re-served a figure this base
**retired at `p455`** ("134 bills / 31 states"), which `p455` demoted after three
other trackers disagreed by `2.6×`. 🟢 **The two *targeted* intel queries run
instead of a tenth re-run — Cetic.br and Canadian provincial guidance — both
returned placeable material** (see [`../intel/market.md`](../intel/market.md)).
🔵 The leg text is not the problem; **re-running an exhausted query is**.

## Ninth pass (`p571`, 2026-10-31) — 🔴 the shelf holds at `24` and the pass found NOTHING new; its value is that it caught this base contradicting itself

🟢 **`derived shelf: **24**` — unchanged.** 🔴 **And this pass's honest headline is
a nil: zero addresses new to this base, from eight `WebSearch` legs AND four
GitHub topic axes.**

| channel | legs / rows | addresses NEW to this base |
| --- | --: | --: |
| 🔴 `WebSearch`, the eight mandated legs (4 global, 4 regional) | 8 | 🔴 **`0`** — **ninth consecutive nil** |
| 🔴 `topic:question-generation` (241) | 20 | 🔴 **`0`** — bought at **pass 85**; `Gap 352` refuses it at ~30% precision |
| 🔴 `topic:essay-scoring` (17) | 17 | 🔴 **`0`** — a tag-variant decoy, see below |
| 🔴 `topic:language-learning` (4.8k) | 10 | 🔴 **`0`** — `read-frog`, `Echo-Loop`, `LLPlayer`, `word-atlas` all already held |
| 🔴 `topic:mooc` (661) | 20 | 🔴 **`0`** — `hypatia`, `scikit-learn-mooc`, `course-tencent-cloud` all already held |

🔵 **Four axes, 67 rows read, zero new addresses. That is a saturation
measurement, and it is worth more than a padded row would have been.**

### 🔴 The defect this pass caught: a tier found at pass 85 never reached any shelf, while a pattern kept asserting it was missing

Pass 85 (`2026-10-09`) recorded *"An item-generation tier exists now, **5 of 5
MIT**"*. 🔴 **Verified against `HEAD` this pass: all seven item-generation rows
were on ZERO shelf pages** — absent from this page and from
[`../repos/foundations.md`](../repos/foundations.md) alike — while
[`../compose/patterns.md`](../compose/patterns.md) `P-571-A` continued to ship
*"nothing permissive generates psychometrically defensible items"* with its
authoring step left to a bare model prompt.

🟢 **Fixed this pass:** the tier is shelved in
[`../repos/foundations.md`](../repos/foundations.md), `P-571-A`'s premise is
amended, and `P-574-A` wires it concretely. 🔵 **The lesson generalises past
education: this base's `trending` history is 63k lines and its shelves are
hundreds — a discovery recorded in history is not shelved, and nothing was
checking the difference.** An inventory grep of the *shelf* files (which is how
this pass started) reports an absence that the *history* files refute.

🔵 **Why these rows still do not belong on THIS page:** they are libraries and
fine-tuned T5 checkpoints, not agents. The shelf gate is correct to exclude them;
the defect was that no page included them at all.

### ⚠️ Instrument note — `P914` reproduced, with a sharper failure mode

🟢 **Pass 85 already recorded (`P914`) that the brief's prescribed
`curl -sI https://github.com/<slug>` is dangerous**: the agent proxy answers
`HTTP/1.1 200 Connection Established` first, so `curl -sI | head -1` reads **200
for every slug on earth, including one invented thirty seconds ago.**

🔴 **This pass adds the other half: the same command with different flags gives the
opposite wrong answer.** With `-o /dev/null -w "%{http_code}"` it returns **403
for every github.com URL — real and fabricated alike.**

| read of the same command | known-real repo | fabricated control | wrong answer it produces |
| --- | --- | --- | --- |
| 🔴 `curl -sI \| head -1` (`P914`) | 200 | **200** | ⛔ everything verifies — **admits fabrications** |
| 🔴 `curl -sI -w "%{http_code}"` 🆕 | **403** | 403 | ⛔ nothing verifies — **would delete real rows** |
| 🟢 rendered repository page | name + ★ + licence | 🟢 **HTTP 404** | ✅ discriminates |
| 🟢 `raw.githubusercontent.com/…/LICENSE` | 🟢 **200** + bytes + holder | 🔴 404 | ✅ the grant instrument |

🔵 **So the hazard is not "curl says 200"; it is that `curl -sI` against this proxy
is uninformative in BOTH directions and the direction depends on your flags.**
🔴 `api.github.com` is additionally unavailable this session — scoped to the
harness repository, every other path returning
`"GitHub access to this repository is not enabled for this session"` — so the
header claim on [`../repos/foundations.md`](../repos/foundations.md) that metadata
comes from the *"GitHub REST index"* **did not hold for `p571`**. Rows added this
pass say which channel answered.

## Eighth pass (`p570`, 2026-10-31) — the shelf holds at `24`, and the pass's yield was in a layer this page does not own

🟢 **`derived shelf: **24**` — unchanged, and reported as a measured null rather
than a quiet absence.** Four axes were swept that **569 passes had never
queried**, and the result for *this* page is honest and small:

| axis queried (never swept before `p570`) | results | new addresses | agents qualifying here |
| --- | --: | --: | --: |
| `topic:rubric` | **187** | 🟢 **7** | 🔴 **0** — all seven are evaluators or tooling |
| `topic:spaced-repetition` | **3.2k** | 🟡 2 | 🔴 **0** — learning apps, not agents |
| `topic:academic-integrity` | **121** | 🔴 **0** — all ten head rows already in-base | 🔴 **0** |
| `topic:automated-grading` | **49** | 🔴 **0** — all ten head rows already in-base | 🔴 **0** |

🔵 **Two of the four axes were already covered without this page knowing it** —
`academic-integrity` and `automated-grading` returned **ten of ten** addresses
already recorded somewhere in this base, which is a genuine and reassuring
result about coverage. 🟢 **`topic:rubric` was the real blind spot**, and its
seven rows are shelved in [`../repos/foundations.md`](../repos/foundations.md)
under a new **rubric and evaluation layer**, because none of them is an agent and
padding this shelf with evaluators would misrepresent the agent population — the
same judgement the fourth pass made for `ppt-master` and the fifth for the
capability sweep.

### 🟢 What the sweep did for this page: the evaluation gap this page has published for six passes is narrower

🔴 This page's longest-standing declared gap reads *"No education-specific agent
**observability** or **regression** tooling was found — sixth consecutive
pass."* 🟢 **The regression half moves**, and the reason it never moved before is
a property of the queries, not the field: every prior sweep searched
`evaluation` / `benchmark` / `observability` **under `topic:education`**, while
the assets sit on `topic:rubric` — a string that appeared **zero times** in every
live page of this base before this pass. 🟢 **[`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics)**
(Apache-2.0, 368★) is the first asset in this KB that evaluates an **agent
trajectory** rather than a finished document, which is the right shape for a
multi-turn tutor. 🔴 **The observability half does not move: there is still no
education-specific runtime drift detector, seventh consecutive pass.**

### 🔴 The pass's warning, and it is about this base's newest rule

🔴 **`p569` adopted commit count as the admission signal for the tooling layer.
`p570` found the counterexample on the first axis it applied the rule to.**
[`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune) reads **35★
with `2,137` commits dated from `2014-06-10`** — and the history is **synthetic**:
monotonic `1.69×` commits-per-year across 12 years against the real control's
`658×`, **408 of 408** pre-2017 commits carrying a commit convention that
postdates them, **zero** author/committer date divergence across all 2,137, and a
first commit reading `refactor:`. 🔵 **A star gate is gamed by recruiting other
people; a commit gate is gamed with a loop.** The replacement signal is *cheaper*
to forge than the one it replaced. 🟢 The check is now an instrument —
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass, validated against two real controls — and the rule
this page should carry forward is: **commit density admits a row only together
with its date distribution.** See `570-A`.

🔵 **The `p569` watch item is NOT yet due.** `voyage` and `throughline` were
left for `p573` and are deliberately untouched here; nothing in this pass
supersedes that instruction.

### 🔴 Gate posture — probed, not inherited (`569-B` satisfied)

🔴 **`python3 -I ingest/validate-pages.py` → DENIED**, verbatim
*"Code from External"* — **third consecutive pass**, so `p569`'s reading holds
and `p565`'s does not, in this session. 🟢 **`python3 -I` on an instrument this
session authored → RAN, `exit 0`** (`ingest/history-plausibility.py`),
confirming `569-B`'s corollary a second time: code this session writes is not
"external". 🔴 **`curl` → `github.com` and `api.github.com`: 403, re-probed, 3 of
3 including `moodle/moodle`** — so the harness's prescribed `curl -sI` URL check
**cannot be run from this session at all**, and existence was instead verified by
**successful `git clone`** (8 of 8 candidates) and **`raw.githubusercontent.com`
200s** (9 of 10), both of which are strictly stronger evidence than a HEAD
request. 🔵 **A pass that reported those 403s as dead links would have deleted
live repositories**; the uniform-status rule on this page is what prevents it.

---

## Seventh pass (`p569`, 2026-10-31) — no new agent qualified again, and this time the floor itself was tested

🟢 **The shelf is unchanged at `24` rows. What changed is that this pass tested
the admission rule instead of applying it**, because `568-C` showed the rule had
discarded this base's own best new row.

### 🟢 The band below the star floor was swept, and it is not empty

🟢 `topic:ai-tutor` answers **793 results at `stars:<50`** against **816 sorted by
stars** — 🔴 **so the field this shelf draws from is almost entirely below its own
floor.** Five addresses new to this base came off that band, four of them MIT.
They are recorded in [`trending.md`](trending.md), **not here**, and the reason is
a rule this pass is adopting explicitly:

| layer | admission signal | why |
| --- | --- | --- |
| 🟢 **Tooling / infrastructure** | 🟢 **commit count** | Used by few, committed to heavily. `DaniyalMlk/calibrate` is **0★ / 214 commits** and closes a six-pass gap; `onionviolet/itembank` is **3★ / 1,175 commits**. A star floor discards both |
| 🔴 **Tutors / agents** | 🔴 **stars** | For an agent a client is asked to adopt, stars *are* the adoption evidence. `throughline` (2★), `voyage` (1★) and `banxue` (0★) all carry 200+ commits and **none is shelved** |

🔵 **The two rules disagree on purpose.** `p568` wrote the distinction —
commit count is the better signal *"on a tooling layer (as opposed to a tutor,
where stars track adoption)"* — and this is the pass that acts on it. 🔴 **A
studio handed a 1★ tutor as a starting point has been handed somebody's personal
project**, however busy its history; a studio handed a 0★ psychometrics engine
with 214 commits and no runtime dependencies has been handed a library. The
asymmetry is the finding.

### 🔴 So the honest statement about this shelf is narrower than "saturated"

🔴 **Four passes called `topic:ai-education` and `topic:ai-tutor` saturated. The
axes were saturated *at the floor this base sorts by*, and the floor was never
examined.** 🟢 Both statements are now on record with denominators, and the
second one is the useful one for a successor: **the next agent to qualify here
will most likely come from the `stars:<50` band on an adoption trajectory, not
from a star-sorted sweep.** `voyage` and `throughline` are the two to re-read at
`p573`.

### 🔴 Gate posture — not attested this pass, and the channel inverted

🔴 **`python3 -I ingest/validate-pages.py` and `ingest/derive-counts.py` were both
DENIED this pass** — *"Code from External"*: this session may not execute code it
cloned. 🟢 `p565` had established the opposite (the instruments *can* be invoked
even though `make hooks` is denied) and corrected seven passes on it. 🔵 **Both
readings were right in their own window; the durable lesson is that the gate
channel must be re-probed every pass and never inherited.**

🟢 **The `derived shelf: **24**` claim above is the machine-readable form
`568-E` asked this page for, and it is supplied now**, computed by replicating
`derive-counts.py`'s own row regex against this page. 🔴 **Note what it does NOT
fix:** that gate's shelf scan runs from `## The shelf` to the next `##` and
swallows the two `###` sub-tables, so it derives **`33`** where the shelf proper
is **`24`** — both figures reproduced this pass. 🔴 **The scan was deliberately
not patched**, because a gate that cannot be executed cannot be verified, and
`568-E` is the record of what shipping an unverified gate costs. See `569-C`.

---

## Sixth pass (`p568`, 2026-10-31) — no new agent qualified, and the measurement says so

🔴 **The shelf is unchanged at twenty-four agents.** This pass added nothing here,
and that is reported as a measured null rather than a quiet absence:

| axis queried | results | already shelved | new agents |
| --- | --: | --: | --: |
| `topic:ai-tutor`, sorted by stars | **816** (82 pages) | top 10 of 10 | **0** |
| `topic:psychometrics`, sorted by stars | **510** | — | **0** |
| `"learning analytics" dashboard` | **289** | — | **0** |

🟢 The `topic:ai-tutor` head re-read clean: `DeepTutor`, `Study-Mate`,
`human-skill-tree`, `anki-mcp-server`, `universal-examprep-skill`, `algo-sensei`,
`Bloom`, `universal-diagnostic-tutor-skill`, `freelingo` and `kaogong-skill` —
**all ten already on this page or already rejected with a reason.** 🔵 `DeepTutor`
reads **52.4k★** on the topic page against the `52,208` in the table below; that is
a ±drift inside the documented artefact class and not a correction.

🔴 **`WebSearch` returned 0 addresses new to this base for a fifth consecutive
pass**, across 8 legs (4 global, 4 regional). Every asset this pass did add came
off a **GitHub search page read through `WebFetch`, sorted by stars** — `curl` to
`github.com` and `api.github.com` were both re-probed at **403**. A successor
should spend its discovery budget accordingly.

**Where the pass did pay was one layer down**, in components rather than agents —
an item-bank gate, a lecture-video pipeline and a learning-analytics stack, all in
[`../repos/foundations.md`](../repos/foundations.md). 🟢 **Two standing gaps on
this page moved as a result:**

- 🟢 **The assessment gap is half-closed, from the end nobody swept.** Five passes
  searched for an item *generator* and found nothing permissive.
  [`onionviolet/itembank`](https://github.com/onionviolet/itembank) (**MIT**, 3★,
  **1,175 commits**) is not a generator — it is the **gate a generator must pass**:
  a blocking linter, deterministic scoring with **no model in the scoring path**,
  and short-answer items that are *never* auto-graded. 🔵 That property is a
  conformity artefact for the AI Act's **Annex III** evaluation-of-learning-outcomes
  category, which this base prices against **2 December 2027**. 🔴 Item
  *calibration* remains genuinely open — the permissive libraries are stale and
  the capable one is ungranted.
- 🔴 **A gap this base was publishing had already been closed by its own shelf.**
  [`../repos/trending.md`](../repos/trending.md) still carried *"no open-source
  learning-analytics dashboard"* while this repository already held
  [`openfun/warren`](https://github.com/openfun/warren) and
  [`openfun/potsie`](https://github.com/openfun/potsie), both **MIT**, both from
  **France Université Numérique** — the same national public operator as
  `openfun/ralph`. 🔵 The mechanism matters more than the miss: the claim lived in
  a narrative summary on an append-only page, and nothing re-checks those against
  the shelf. Registered as `568-A`.

🟢 **And the EMEA institutional-provenance request in `567-A` has an answer**, from
the instrument the fifth pass built rather than from a better search: `ralph`,
`potsie` and `warren` all name *"France Université Numérique"* in the grant
itself. 🔴 **LATAM gained no new address this pass** — the only placed LATAM agent
on this page, `dio-agent` (2,750★), is still **ungranted**, so the region's
local-supply story and its build-on-it story remain about different repositories.

## The shelf

| Agent | Repo | Licence | ★ | Region | What it is |
| --- | --- | --- | --: | --- | --- |
| L.A.R.A | [BootlegYouki/L.A.R.A](https://github.com/BootlegYouki/L.A.R.A) | **MIT** (1,113 B ✅ first-hand, `main/LICENSE`) | 5 | APAC | 🟢 **The whole `topic:deped` axis in one row, and the design is better than its star count.** "Offline LAN-Based Classroom with Hybrid Socratic SLM Tutor and Paperless Quizzes for Philippine Elementary Schools (DepEd Grades 1-6)." 🔵 **Three properties that are hard to buy and expensive to build: offline, LAN-local, and a *small* language model chosen deliberately** — which together answer the connectivity and data-residency constraints that stop school deployments in exactly this market. 🔴 **`5★`, and it is a capstone project by its own README.** Shelved as a design to copy, not a dependency to adopt. 🔵 It is also the top of its axis: `topic:deped` holds **`10`** repositories and **nothing on it exceeds `5★`**. |
| gaokao-mentor-wisdom | [dongsheng123132/gaokao-mentor-wisdom](https://github.com/dongsheng123132/gaokao-mentor-wisdom) | **MIT** (1,072 B ✅ first-hand, `main/LICENSE`) | 66 | APAC | 🟢 **Shelved for its shape, not its content: a domain corpus deliberately structured for machine consumption.** `张雪峰语录大全 · 高考志愿填报指南` — university-major selection, institution recommendations and employment-prospect analysis for the gaokao admissions decision, "整理成结构化 JSON 数据集，方便考生家长查阅，也方便 AI 应用直接集成调用" — *organised as a structured JSON dataset, for families to consult and for AI applications to integrate directly*. 🔵 **That last clause is the pattern worth stealing**: the asset is advice turned into a typed dataset, which is what makes it composable. 🔴 Content is one commentator's corpus, so the editorial bias travels with it. |
| gaokao-advisor | [Zylcyl/gaokao-advisor](https://github.com/Zylcyl/gaokao-advisor) | **MIT** (1,056 B ✅ first-hand, `master/LICENSE`) | 19 | APAC | `高考志愿填报智能顾问` — a gaokao application adviser built on a **multi-skill coordination architecture**. 🔵 Shelved as the agent-shaped counterpart to the row above: same decision, same market, one supplies the structured corpus and this one the orchestration. 🔴 **`19★`, default branch `master`.** Thin, and the admissions rules it encodes are annual — treat the logic as perishable. |
| libro-3d-interactivo | [csepulvedai/libro-3d-interactivo](https://github.com/csepulvedai/libro-3d-interactivo) | **MIT** (1,086 B ✅ first-hand, `main/LICENSE`) | 14 | LATAM | 🟢 **The only LATAM-origin agent artefact found this pass, and it is permissively licensed — which is not the regional norm on this page.** A Claude Code skill that builds interactive 3D pop-up educational books in Three.js, with narration and a guide cursor. Author `Cristian Sepúlveda-Irribarra`. 🔵 Contrast it with `DIO Agent` further up this shelf — `2,750★`, LATAM, and **unusable because it carries no licence at all**. 🔴 **`14★`.** Shelved because a usable LATAM grant is rarer here than a popular LATAM repository, and because **Chile's Mineduc now owns an AI curriculum mandate from pre-school onward** (see [`../intel/market.md`](../intel/market.md)) — a pre-school-facing, permissively licensed Chilean artefact is directly on that line. |
| canvas-lms-mcp | [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | **MIT** (1,070 B ✅ first-hand, `main/LICENSE`) | 10 | North America | 🟢 **Shelved at last: this base has seen this address `115` times across its history and never once placed it.** "Canvas LMS MCP server — read courses, assignments, submissions, rubrics, quizzes; grade and comment from any AI agent." TypeScript, 446 commits. 🔵 `p565` concluded that **`canvas-mcp` is the North America answer** and withdrew its own Moodle-based NA recommendation on exactly that ground — then the concrete Canvas MCP server the sweeps kept returning stayed unshelved for seven more passes. Sidebar and grant file agree. |
| lesson-plan-magic | [revjake1/lesson-plan-magic](https://github.com/revjake1/lesson-plan-magic) | **MIT** (1,069 B ✅ first-hand) | 1 | North America | "K-12 lesson planning AI plugin for Cowork & Claude Code — learns your voice, fills your district's template, and generates standards-aligned…" 🟢 **The district-template framing is the commercially interesting part** — it is the first row in this KB that targets the US *district* procurement unit rather than a teacher or an institution. 🔴 **Thin: 16 commits over a 3-day span, first commit `2026-04-21`, 1★.** Graded as a pattern to copy, not a dependency to adopt. |
| lesson-plan-skill | [Dragon-01-you/lesson-plan-skill](https://github.com/Dragon-01-you/lesson-plan-skill) | **MIT** (1,070 B ✅ first-hand, `master/LICENSE`) | 4 | APAC | "AI-Powered Lesson Plan Generator for Claude Code \| 智能教案生成器 - 5分钟生成完整教案". Python, packaged with `pyproject.toml`. 🔴 **Thin: 5 commits, every one dated `2026-08-06`, span 0 days.** A single-sitting repository. Shelved because the axis it came from is new to this base, not because the artefact is mature. |
| dsh-teacher-kit | [LeonhardJY/dsh-teacher-kit](https://github.com/LeonhardJY/dsh-teacher-kit) | **MIT** (1,071 B ✅ first-hand) | 2 | APAC | DSH plugin for mainland-China secondary teachers: exam papers, item-bank assembly, dictation sheets, lesson plans, courseware, whole-lesson bundles, plus `docx`/`pptx` batch processing against the school's own blank template. 🟢 **States `全程本机运行，不联网、不收集数据` — runs entirely on the local machine, no network, no data collection.** That is a *data-residency* property, which is the single most common blocker in school procurement. 🔴 7 commits, created `2026-10-28` (three days old). |
| teacher-workbench | [deepseek-harness-java/teacher-workbench](https://github.com/deepseek-harness-java/teacher-workbench) | ⛔ **NO LICENCE** — 40 probes | 2 | APAC | Java teacher workbench: 学情热力 (learning heatmaps), 错题归集 (error-item collection), 分层练习 (tiered practice), 教案初稿 (lesson-plan drafts), 作文批改 (essay marking) — a genuinely well-chosen feature set for the market it names. 🔴 **Ungranted, and this is now evidenced to the hilt: `4` branches × `10` filenames including case variants = `40` probes, all 404.** Default is exclusive copyright. Read it for the feature taxonomy; ship nothing from it. |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 52,208 | APAC | Lifelong personalised tutoring; multi-agent pipelines over LLM + RAG. Python, created 2025-12-28. Data Intelligence Lab, University of Hong Kong. **Still the largest education agent on GitHub.** Fourth-pass reading, 2026-10-31 10:42 UTC: **52,208★**, **6,394 forks** (6,388 at 09:40), 256 open issues, pushed 10:39 the same day; the homepage field now carries `arxiv.org/abs/2604.26962`. |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,984 | APAC | **The most consequential new row in this KB.** "Open Multi-Agent Interactive Classroom" — turns a topic or uploaded documents into an interactive lesson with AI teachers *and* AI classmates: slides, quizzes, simulations, speech, whiteboard, live discussion. Exports PPTX, single-file offline HTML, or classroom ZIP. TypeScript (Next.js 16/React 19), **6,501 forks** read at 10:10 UTC (6,502 at 09:40), 212 open issues, `v1.3.0` dated 2026-10-29. Created **2026-03-11** — 42k★ in under eight months. `LICENSE` reads "MIT License, Copyright (c) 2026 THU-MAIC"; contact domain is `tsinghua.edu.cn`. |
| DIO Agent | [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | ⛔ **NO LICENCE** — see note | 2,750 | LATAM | **The first LATAM-origin education agent found in three passes, and it cannot be built on.** A study-mentor agent bundle: `AGENTS.md`, `CLAUDE.md`, and `skills/` with one `SKILL.md` per skill (study planning, hinting without answering, concept explanation, web search, portfolio review, career guidance). Runs on Claude Code, Codex, OpenCode, Antigravity, Hermes. 347 forks, created 2026-05-27. README is Portuguese; org links `dio.me`, a bootcamp/`formações` platform. **Licence defect, now verified by three methods:** the API returns **no `license` field at all**, the repo page names none, and this pass fetched all five standard licence filenames on both branches over `raw.githubusercontent.com` — all 404. Default is exclusive copyright, i.e. all rights reserved. Fork and read, do not ship. |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1,280 | APAC | Self-study companion agent: builds a route through a subject, teaches it, and sets projects, with spaced repetition. JavaScript, 60 forks, created 2026-09-17. Chinese-language. |
| learn-from-materials | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | MIT | 1,201 | APAC | Turns PDFs, books and papers into interactive learning webpages that stay traceable to the source and carry quizzes and notes. Python, 109 forks, created 2026-09-08. The closest thing on the shelf to a document-to-course pipeline. |
| Papermorph | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | MIT | 1,034 | Global | **The fastest-growing education agent on this shelf: 1,034★ in four weeks.** "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created 2026-10-03. Topics include **`scorm`** and `interactive-textbook` — it targets the installed courseware base, not only the web. MIT read first-hand from `main/LICENSE` (1,069 B). ⚠️ The copyright line reads "Copyright (c) 2026 TedKaczynski", a pseudonym: the grant is valid, the holder is unidentifiable, and that is a diligence item for a client deliverable. |
| Claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT | 557 | Global | "An open-source alternative to Udemy and Coursera": give Claude a topic, it researches the web and builds a course of **2-minute audio lessons with cited sources**. Python, 67 forks, created 2026-10-14, ElevenLabs TTS. **Cited sources as a design feature** is rare here and makes it the one content-generating agent that starts from provenance rather than retrofitting it. MIT, `main/LICENSE` 1,069 B, "Copyright (c) 2026 Assaf Kipnis". |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 539 | Global | MCP server giving an agent control of **Anki**, the spaced-repetition flashcard system. TypeScript, 39 forks, created 2025-09-29. The retention layer: the one verified way to hand an agent a real SRS scheduler instead of reimplementing one. Origin not stated. |
| SocialCoach | [GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach) | Apache-2.0 | 463 | Global | Social-emotional learning by role-play: conflict handling and communication skills with personalised feedback. TypeScript, 60 forks, created 2026-09-03. The only verified **SEL** agent found; SEL is a budget line in K-12 that no other row addresses. Origin not stated. |
| Exam Cram Coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 364 | APAC | Exam-prep tutor that teaches **from the instructor's own slides with page citations**, crops figures, and quizzes from real homework. Explicitly engineered against hallucination (`anti-hallucination` topic) and to run on small cheap models. Python, created 2026-06-24. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 310 | North America | The most established Canvas LMS MCP server. Sidebar: "up to 102 tools and 8 agent skills"; README has said 128. Python, 101 forks, created 2025-02-28. Ships agent skills including pre-semester course audit and accessibility auditor. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 295 | APAC | Socratic private tutor that reads how a learner actually learns; Bloom's 2-sigma research packaged as an agent skill **plus** a self-hostable FastAPI/React app. 44 forks, created 2026-03-10. The clearest instance of the skill-and-app dual shape (see [`../intel/trends.md`](../intel/trends.md)). |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America | Intelligent tutoring system with **Bayesian Knowledge Tracing**, React + Firebase. 164 forks — the highest fork-to-star ratio on the shelf, which is what a teaching-materials project looks like in use. Published at CHI '23. Owning org CAHLR; a UC Berkeley connection is indicated by the authors, not stated on the repo page. |
| WordLink | [orionsheep/wordlink](https://github.com/orionsheep/wordlink) | MIT | 262 | Global | Vocabulary learning on a **fine-tuned 1.5B model (SFT+DPO) that runs entirely offline in the browser** via WebGPU. TypeScript, 38 forks. Topics include **`sdg4`** (UN Sustainable Development Goal 4) and the Qwen/ModelScope stack. **The only in-browser offline model in this KB**, and therefore the only agent here that works with no connectivity and no inference bill. MIT, `main/LICENSE` 1,093 B. |
| AI Learning Guide | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | MIT | 242 | Global | Interactive desktop app with **51 labs** across ML fundamentals, transformers, RAG, agents, fine-tuning and quantisation. TypeScript + ONNX, **offline-first**, 23 forks, created 2026-10-05. Not a tutor — **AI-literacy delivery as a shippable artefact**, which is what Singapore's and the UAE's mandates actually procure. MIT, `main/LICENSE` 1,081 B. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT | 213 | APAC | High-stakes civil-service exam preparation (行测/申论/职测/综应), including a wrong-answer review loop. Python, created 2026-04-06. Shelved as the reference example of **one named credential, fully modelled** — the shape a client asks for by name. |
| Cram Engine | [liuliu667/cram-engine](https://github.com/liuliu667/cram-engine) | MIT | 176 | APAC | A **four-stage interactive cram skill grounded in learning science**: get the material understood, retained, and usable on exam answers inside a fixed time budget. Chinese-language; topics `learning-sciences`, `aied`. Created 2026-06-06. Shelved because it is the only row that models **time-boxed revision** — the request a client actually receives before an exam season. MIT, `main/LICENSE` 1,064 B. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 158 | Global | Block-based adaptive learning workspace that runs **locally**: upload material, get notes, quizzes, flashcards and an adaptive tutor, over 10+ LLM providers, with a knowledge graph. Python/TypeScript, 38 forks. **Star-count correction:** an earlier cycle of this KB recorded OpenTutor at ~900★; the API says **158**. The earlier figure was wrong. |
| Pedagogy Benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | Not a tutor — an **evaluator**. 1,143 questions from real teacher-qualification exams: CDPK (920, general pedagogy) and SEND (223, Special Educational Needs and Disabilities). Code for *Benchmarking the Pedagogical Knowledge of Large Language Models*. Its parent organisation is the LMIC-focused supply side this KB spent three passes failing to find — see [`../repos/foundations.md`](../repos/foundations.md). |
| GenMentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 135 | Global | **Peer-reviewed, and released into the public domain — the most permissive grant in this KB.** Official code for *"LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System"*, **WWW 2025 Industry Track, accepted as an Oral presentation**. Goal-oriented tutoring: it works backwards from a stated learner goal to a skill gap to a path. TypeScript, 23 forks, created 2024-11-16, pushed 2026-10-30. `main/LICENSE`, **7,048 B: "Creative Commons Legal Code — CC0 1.0 Universal"** — a public-domain dedication, so a derivative needs neither attribution nor share-alike. **The one row on this shelf with both an academic citation and no licence friction at all.** Same owner as `SocialCoach`; origin not stated, recorded Global. |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 61 | Global | **The attach-boundary tutor: an MCP server that turns any LLM into an intelligent tutoring system.** Implements **Bayesian Knowledge Tracing** behind the MCP protocol, so the mastery model lives in the server and the model is swappable — the inverse of every app-shaped row here. **Go**, 10 forks, created 2026-03-30, pushed 2026-10-31. `main/LICENSE` 1,073 B, "Copyright (c) 2026 Arnaud Guiovanna". Shelved below the usual star bar for one reason: it is the only asset in this KB that puts a **real BKT scheduler** on the permissive side of an attach boundary, which is exactly what pattern [`P-568-A`](../compose/patterns.md) has had to hand-roll. Origin not stated. |
| Knowledge Spaces | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | MIT | 30 | **North America** | **Region placed from the licence text, not inferred.** `main/LICENSE` 1,090 B: *"Copyright (c) 2025 **Vanderbilt Data Science Institute**"*. Ten Claude Code skills implementing the full **Knowledge Space Theory** pipeline: course materials → knowledge graph → adaptive assessment → personalised materials → just-in-time instruction planning. Python, 5 forks, created 2026-02-12. **The only row where a named research university publishes an agent-skill bundle permissively** — which makes it the reference citation when a North American institutional client asks whether this is academically grounded. Small and young; cite it, do not stake a deployment on it. |
| THM Feedbacksystem | [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | Apache-2.0 | 24 | **EMEA** | **The EMEA-origin gap, open for four passes, closes here.** *"Intelligent, personalised feedback for students using artificial intelligence"* — automated checking and feedback on student submissions, in production use in university teaching. TypeScript, 10 forks, default branch **`dev`** (no `main`), created 2018-08-17, pushed 2026-10-28. `dev/LICENSE` 10,785 B: *"Copyright 2021 **Technische Hochschule Mittelhessen** — Licensed under the Apache License, Version 2.0"*. **Read the caveat as loudly as the finding:** 244 open issues on 24 stars, and an eight-year-old codebase that predates LLM tutoring entirely. This is a **provenance** asset and a reference deployment for a European university conversation — it is not a product to ship. |
| Paideia | [OPTIMETA/PAIDEIA](https://github.com/OPTIMETA/PAIDEIA) | MIT | 91 | Global | **Fully local exam readiness — the data-residency answer.** A Claude Code plugin that *"forms exam readiness locally. Stop renting your own learning."* Runs on **Ollama** with **Qwen3-VL** for vision, does its own **OCR**, and writes into **Obsidian** markdown; maths and physics. Python, 4 forks, created 2026-04-21, pushed 2026-10-31. `main/LICENSE` 1,068 B, "Copyright (c) 2026 Taewoo Park". **Why it matters commercially:** every sovereignty-constrained engagement in this KB — EMEA public sector, Vietnam, Korea — asks for a tutor that sends no student data anywhere, and this is the only row that is local-first by construction rather than by configuration. Holder is an individual, so no region is assigned. |

| mcd-together-order | [littlebordercollie/mcd-together-order](https://github.com/littlebordercollie/mcd-together-order) | **MIT** (1,308 B ✅ first-hand, `main/LICENSE`) | 101 | APAC | 🟢 **The first MCP-native AAC agent in this base, and the only credible education-specific find on four never-queried axes.** 麦麦一起点: a student in a 培智学校 (special-needs school) picks a meal from a few picture cards with short audio; the parent then checks list, store and price and pays through official McDonald's channels. A local service calls **McDonald's own MCP** for stores, items and prices. 🔴 **Pre-pilot, and says so: 10 commits, no student trials run, one ¥12 trial order created and never paid.** A contest prototype, not a product. 🔵 Region placed by language and by the 培智学校 framing — the grant's copyright line reads "mcd-together-order contributors" and places nothing (`574-F`). |
| shravyamudra | [tejasbhor/shravyamudra](https://github.com/tejasbhor/shravyamudra) | **MIT** (1,069 B ✅ first-hand, `main/LICENSE`) | 1 | APAC | Real-time text → **Indian Sign Language** gesture translation with learning modules, Python. 🟢 **The second India-specific row on these shelves**, and it lands against the one education-specific accessibility instrument this base has confirmed (the AICTE / RPwD code, `574-D`). 🔴 1★ — shelved for the axis and the jurisdiction fit, not for maturity. |
| SPLWD | [VoxDroid/SPLWD](https://github.com/VoxDroid/SPLWD) | **MIT** (1,061 B ✅ first-hand, `main/LICENSE`) | 3 | Global | PHP school-management system **for students with learning and working disabilities**, role-based dashboards. 🟢 The only *administrative* system on the special-education axis — every other row there is a single-learner tool. 🔵 Copyright line reads `Izeno`, which places no region. |
| worksheet-generator | [ellmos-ai/worksheet-generator](https://github.com/ellmos-ai/worksheet-generator) | **MIT** (1,068 B ✅ first-hand, `main/LICENSE`) | 1 | Global | Generates **individualised worksheets** for educational and therapeutic professionals, Python. 🔵 The differentiation step an IEP goal actually needs, and the nearest thing on this axis to a reusable component. 🔴 1★. |
| AAC-Web_Project | [manavrenjith/AAC-Web_Project](https://github.com/manavrenjith/AAC-Web_Project) | **MIT** (1,084 B ✅ first-hand, `main/LICENSE`) | 3 | Global | Flask **AAC** board with text-to-speech. 🔵 Permissive where the deployed AAC platform this base already shelves (`cboard`, GPL-3.0) is copyleft — so this is the row you may vendor. 🔴 3★, student-project scale. |
| special-education-due-process-complaint | [b33kman/special-education-due-process-complaint](https://github.com/b33kman/special-education-due-process-complaint) | **MIT** (1,068 B ✅ first-hand, `main/LICENSE`) | 1 | North America | Chat-app plugin that drafts **IDEA due process complaints**. 🟢 **The only row on these shelves that acts on education *law* rather than education content** — IDEA is the US statute behind every IEP, and the complaint is its enforcement instrument. 🔵 Copyright `2026 Mark Beekman`. 🔴 1★. |
### Carried with a known defect

| Agent | Repo | Licence | ★ | Region | Note |
| --- | --- | --- | --: | --- | --- |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ⛔ MIT claimed in README only — **no LICENSE file** | 104 | North America | Canvas LMS MCP server, `v2.2`, 54 tools, containerised. **Defect now confirmed by three independent methods.** (1) Earlier passes 404-ed every licence filename on both branches. (2) GitHub's own licence index (`license:mit repo:DMontgomery40/mcp-canvas-lms`) returns **zero results**. (3) This pass fetched all five standard filenames on **both** `main` and `master` over `raw.githubusercontent.com` — the channel that successfully returned 21 other licence files the same hour — and every one 404s. There is no MIT grant. Prefer `vishalsachdev/canvas-mcp`. |
| moodle-mcp | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | 27 | APAC | Rust MCP server operating Moodle: courses, assignments, forums, grades, files-as-markdown. Validated against Moodle 3.7 → 5.x. Only Rust implementation found. No defect — listed here because at 27★ and created 2026-10-12 it is too young to carry an engagement alone. |

### Agent-skill bundles verified MIT this pass — components, not shelf rows

Six more education skill bundles clear the licence gate but are deliberately
**not** shelved: each is a single narrow instruction set rather than an agent an
engagement would be built around, and padding the shelf with them would
misrepresent the agent population. They are recorded because they are real,
MIT-licensed, and immediately usable as components inside a larger deliverable —
and because the licence text of every one was read this pass.

| Bundle | Repo | Licence | ★ | Region | Use it for |
| --- | --- | --- | --: | --- | --- |
| learn-anything-with-AI | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | MIT (1,065 B) | 203 | Global | Project-driven **mastery learning** with mastery checks and authoritative sources — the scaffolding layer under a subject tutor. |
| awesome-student-ai-skills | [cuic19053-hue/awesome-student-ai-skills](https://github.com/cuic19053-hue/awesome-student-ai-skills) | MIT (1,070 B) | 147 | APAC | 35 Chinese university application-document skills (大创申报书, 挑战杯, 国家奖学金, 保研). The reference example of **one national paperwork regime, fully modelled**. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT (1,068 B) | 119 | APAC | Teaching and tutoring collection including *gaokao* preparation. |
| montessori-skill | [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | MIT (1,063 B) | 78 | APAC | **Montessori pedagogy as a skill** — child education, self-directed learning, environment design. The only named pedagogical *philosophy* in this KB. |
| research-field-onboarding | [ljx-chase/research-field-onboarding](https://github.com/ljx-chase/research-field-onboarding) | MIT (1,111 B) | 75 | Global | Onboarding a learner into an unfamiliar research field; literature review. Higher-ed and R&D clients. |
| assignment-check | [henryyu333/assignment-check](https://github.com/henryyu333/assignment-check) | MIT (1,086 B) | 53 | Global | **Pre-submission checking against the brief, the rubric, evidence and citations.** The closest thing in open source to a student-side quality gate, and the cheapest row here to wire into pattern P-568-K. |

And one that cannot be shelved but can be **partly** used:
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree)
(586★) is **AGPL-3.0** — but its `skills/` directory is **dual-licensed AGPL-3.0
or MIT at the adopter's option**, read first-hand from `master/LICENSE`. The
platform is disqualified for a proprietary derivative; **the skill bundles inside
it are not.** See the resolution note below.

## Why this shelf is shaped the way it is

**The agent layer is permissive; the platform layer is not.** Of the nineteen
shelf rows, **16 are MIT, 2 Apache-2.0, and 1 has no licence at all** — all five
new rows this pass are MIT, read from the licence file. Every platform of record
these agents attach to is copyleft, with two exceptions now documented in
[`../repos/foundations.md`](../repos/foundations.md). The integration surface is
buildable; the substrate mostly is not forkable on commercial terms. The
composition pattern that follows is in [`../compose/patterns.md`](../compose/patterns.md).

**Education AI has stopped shipping as applications.** **Nine of nineteen** shelf
rows are **agent skills** — markdown instruction bundles loaded by an existing
harness (Claude Code, Codex, OpenCode, Cursor, Antigravity) rather than
deployable services: `dio-agent`, `Study-Mate`, `learn-from-materials`,
`Papermorph`, `Claudemy`, `Exam Cram Coach`, `Bloom`, `kaogong-skill` and
`Cram Engine`. `Bloom` ships as a skill **and** a self-hostable app, which is the
hybrid shape to expect next. Counting the six component bundles above, **15 of
the 25 agents on this page have no runtime at all.**
This is measured, not reported: `topic:agent-skills topic:education stars:>50`
returns **13 repositories** — the same count as the previous pass, so that axis is
genuinely saturated — and this pass read **all thirteen licence files**. The
distribution is the finding: **11 MIT, 1 CC BY-SA 4.0, 1 unlicensed, 1
dual-grant — and the two non-permissive members are the two largest, at 4,843★
and 2,750★.** In this cohort, popularity is anti-correlated with licence
usability. Consequences for an engagement are in
[`../intel/trends.md`](../intel/trends.md); the short version is that the
"product" a client now adopts may be a prompt contract, with no runtime to host
and no API to version.

**Origin has concentrated in APAC — but the new rows are unplaceable, and that
is its own finding.** Of the nineteen shelf rows, **8 are APAC**, and the two
largest (52k★, 42k★) are both Chinese-university projects, HKU and Tsinghua. The
rest: **Global 7, North America 2, LATAM 1 (unlicensed), EMEA 1 (13★)**. Adding
the two defect-table rows puts North America at 3 and APAC at 9.

**Global is now the largest bucket after APAC, and it grew because the
instrument shrank, not because origin diversified.** Four of this pass's five
new rows are Global because owner location **cannot be read from this session at
all**: `search_users` returns login, id and avatar with no `location` field, and
`api.github.com` is 403. Region was assigned only where the artefact itself
states it. Do not read "Global 7" as geographic spread — read it as **seven rows
whose provenance is unknown**, which for client-facing use is a diligence
backlog, not a feature.

**MCP is still the integration shape, but no longer the dominant one.** Two shelf
rows are MCP servers (`canvas-mcp`, `anki-mcp-server`), and so are both rows in
the defect table (`mcp-canvas-lms`, `moodle-mcp`) — four of the twenty-one
shelved-and-defect agents on this page, and four of twenty-five counting the
component bundles. Where an agent must *reach into* a system of record, assume MCP; where
it must *teach*, assume a skill bundle.

## Rejected this run, with reasons

| Candidate | Why it is not on the shelf |
| --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | **4,843★ — would be the third-largest row — and rejected on licence.** A library of 23,000+ agent skills for empirical research across eight social-science disciplines, maintained by CoPaper.AI from Stanford REAP (North America). **Evidence upgraded this pass from the README badge to the licence file itself:** `main/LICENSE`, 620 bytes, "Creative Commons Attribution-ShareAlike 4.0 International" — a *content* licence with share-alike. Derivatives of the skill text must be released under the same terms, which is the opposite of what a client wants from a billable methodology asset. |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **932★ — the most substantively relevant rejection in this KB — and also CC BY-SA 4.0.** **165 evidence-grounded AI skills for teachers, school leaders and EdTech builders**: pedagogy, learning science, curriculum design, assessment, competency-based education, inclusive design, retrieval practice, systems thinking. TypeScript, 131 forks, created 2026-03-01, pushed 2026-10-31, runs on Claude, Codex and Hermes. On substance this is the best-targeted education skills library found in four passes — written for the *professional* buyer rather than the student. `main/LICENSE`, 1,230 bytes: "Creative Commons Attribution-ShareAlike 4.0 International, Copyright (c) 2026 Gareth Manning". **Two share-alike libraries now sit at the top of this category (4,843★ and 932★), which makes it a pattern rather than an instance:** authors of large pedagogical skill libraries reach for CC licences because the artefact reads as writing. The consequence is fixed — **the best-curated pedagogy content in open source cannot be absorbed into a proprietary methodology asset.** Use it internally, reference it, point clients at it; do not rebadge it. |
| [ystemsrx/sql-to-ER](https://github.com/ystemsrx/sql-to-ER) | **192★ — not an education agent.** Converts SQL or DBML to ER diagrams; tagged `education` because it is used in database courses. It surfaces inside `topic:agent-skills topic:education` and is the clearest instance of **topic-tag dilution** in that cohort. Logged so the next pass does not re-triage it. |
| [bayshores/godspeed](https://github.com/bayshores/godspeed) | **AGPL-3.0, 7★.** An MCP-native tutor that runs inside Claude Code, Codex or any MCP client and keeps mastery in a knowledge graph. Re-read this pass: still **7★**, created 2026-10-27, pushed 2026-10-31. Copyleft and too young. It is also, as of this pass, **the only repository returned by `topic:ai-tutor created:>2026-10-25 stars:>3`** — i.e. the six-day fresh-tutor cohort is a population of one. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 217★. Self-hosted AI language-learning platform (CEFR plans, voice conversation, flashcards, spaced repetition, local or cloud LLMs) — technically a good fit and licence-disqualified for a proprietary derivative. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned to it. Recorded so the next pass does not re-discover it. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **Licence RESOLVED this pass — `AGPL-3.0`, with a per-directory dual grant.** 586★, 33 forks, TypeScript. "AI-Powered Skill Tree for Lifelong Human Learning", 30+ skills K-12 → career, cognitive-science framing, ships an MCP server. `master/LICENSE`, 1,063 bytes: "GNU AFFERO GENERAL PUBLIC LICENSE Version 3 … Copyright (c) 2026 Human Skill Tree Contributors", followed by a `DUAL LICENSING NOTE`: *"The SKILL.md files in the `skills/` directory may be used under either this AGPL-3.0 license OR the MIT license, at your option."* **So the platform is rejected and the skill bundles are usable** — the fifth distinct licence shape catalogued in this KB, and the first a licence *column* cannot express. **Note the branch:** its default is `master`; every `main/LICENSE*` probe 404s. Probing only `main` manufactures false "no licence" readings, which is how two passes left this unresolved. |
| [AFRICAN-AI-NETWORK/learnhouse](https://github.com/AFRICAN-AI-NETWORK/learnhouse) | **A 0★ fork, and the trap this pass nearly fell into.** It surfaced as the leading hit for an African education-AI search and the organisation name reads as African supply side. It is a fork of [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) (**AGPL-3.0** plus a separate Enterprise Licence, 2.4k★, maintainer Badr B. / `@swve`, country not stated), with 0 stars and 1 fork and no stated African content. The African signal is the **org name only**. Same failure mode as the `NelsonSpencer/canvas-mcp` fork rejected on the previous pass: an organisation name is not provenance. |
| [profitsylivester-ux/tujifunze-agent](https://github.com/profitsylivester-ux/tujifunze-agent) | **MIT (README), 0★, 11 commits, no releases, empty Languages panel.** LangGraph + MCP + Qwen 2.5 decision-support agent tracking multi-term learner trajectories and producing cited plain-language student profiles with human-in-the-loop oversight. Built for the **African Agentic AI Design Challenge, Education track**; "Tujifunze" is Swahili; no country stated. Below the shelf bar, but **logged as a watch item and as evidence**: it is the first African-context education agent this KB has located in three passes, and its design — citations plus mandatory human review over learner records — is the right shape for ministry work. |

| [anandpatikat/guru-latihan-dinamis](https://github.com/anandpatikat/guru-latihan-dinamis) | **NO LICENCE FILE, 115★ — and the second time a placed regional finding has been blocked by licence rather than by absence.** *"Revolutionizing Indonesian Exam Prep: AI Teacher Tools 2026"* — teacher tools built against **Kurikulum Merdeka**, Indonesia's national curriculum, with `indonesia` and `kurikulum-merdeka` among its topics. TypeScript/HTML monorepo (Hono, Drizzle, Effect-TS, Better Auth), created 2026-06-28, pushed 2026-10-31, 0 forks; built for a hackathon (`cerebral-valley`). All five standard licence filenames probed on `main` over `raw.githubusercontent.com` — **every one 404s**, so default exclusive copyright applies. **The pattern now has three instances** (`dio-agent`, LATAM, 2,750★; `guru-latihan-dinamis`, APAC-Indonesia, 115★; `mcp-canvas-lms`, North America, 104★): *the regionally placed education agents this KB finds are disproportionately the ones with no usable grant.* Recorded as a supply signal — a national-curriculum-aligned agent exists for Indonesia — and as unusable. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT, 75,894★ — the largest MIT-licensed repository this KB has ever located, and not an education agent.** *"Learn AI Engineering! Learn it. Build it. Ship it for others."* Python/Rust/TypeScript, **13,381 forks**, created 2026-03-18, pushed 2026-10-31; reached **#1 on GitHub Trending on 2026-05-24**. `main/LICENSE` 1,070 B, "Copyright (c) 2026 Rohit Ghumare". It is a **curriculum**, not a tutor: no learner model, no assessment loop, no runtime. Logged here rather than shelved because padding the shelf with it would misrepresent the agent population — the same judgement the fourth pass made for `ppt-master`. It is, however, a genuine **courseware asset**: see [`../repos/foundations.md`](../repos/foundations.md). |
| [ArturoNereu/AI-Study-Group](https://github.com/ArturoNereu/AI-Study-Group) | **NO LICENCE FILE, 1,372★.** A curated resource list ("Resources to learn AI"), surfaced by the prescribed `github trending education AI 2026` search. Both probes on `main` 404. An awesome-list with no grant: read it, link it, copy nothing from it. |

## Method note — the two channels that work, and the three that do not

**Existence and metadata: the GitHub REST index.** Every repository URL on this
page was confirmed by `search_repositories` with `repo:owner/name`, which returns
id, licence determination, star count, fork count and push date in one call.

**Licence text: `raw.githubusercontent.com`, new this pass and the better
instrument.** `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/LICENSE`
returns **HTTP 200** from this session. Twenty-one licence files were read
byte-for-byte this pass, which closed two licence questions that three earlier
passes could not answer (`evaluators`, `human-skill-tree`) and added a third
confirmation to two standing defects. **Read the file, on every plausible
filename and on every branch** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
`licence`, `COPYING`, against both `main` and `master`. `human-skill-tree` is
AGPL-3.0 on `master` and 404 on `main`.

**Region, for institutional publishers: the licence file's copyright line.** The
fourth pass declared owner country unobtainable — `search_users` exposes no
`location` and `api.github.com` is 403 — and left seven rows `Global`. That
conclusion was right about *people* and wrong about *institutions*. An
institutional copyright holder names itself in the grant:

| Read from the licence file | Places |
| --- | --- |
| "Copyright 2021 Technische Hochschule Mittelhessen" | `feedbacksystem` → **EMEA** |
| "Copyright (c) 2025 Vanderbilt Data Science Institute" | `knowledge-spaces` → **North America** |
| "Copyright (c) 2026 THU-MAIC" (+ `tsinghua.edu.cn` contact) | `OpenMAIC` → APAC |
| "GIP FUN MOOC" | `openfun/richie` → EMEA |
| "ENGAGESPHERE TECHNOLOGY PRIVATE LIMITED" | `euron-open-lms` → APAC |

🔴 **New limit, measured at `p570`: the rule is LICENCE-FAMILY-DEPENDENT and
cannot work at all on Apache-2.0.** Apache-2.0's template contains **no copyright
line** — its only use of the word is the boilerplate *"'Licensor' shall mean the
copyright owner…"* definition. **Four of four** Apache rows probed this pass
(`AdaRubrics`, `rubrictrail`, `AutoRubric-as-Reward`, `ScoreRune`) carry **no
holder**, so region is unrecoverable from them **by construction, whether or not
the holder is an institution**. The `terracotta` placeholder observation this
page recorded as a one-off trap is the *normal case* for that family. 🔵 And the
companion extension works where a **registry mandates authorship**: `p570` placed
**six** R-tier rows from `DESCRIPTION`'s `Authors@R` (three EMEA, two North
America, one LATAM†) because CRAN enforces the field, while **5 of 7** npm-shaped
rows have no `package.json` at all. See `570-C`, `570-D` and
[`../repos/foundations.md`](../repos/foundations.md).

**And the limit is as important as the rule, because it was tested.** All seven
`Global` rows were re-probed against this instrument this pass. **None resolved**
— every holder is an individual or a pseudo-collective: "Anatoly Tarnavsky"
(`anki-mcp-server`), "Zijin Zhang" (`OpenTutor`), "TedKaczynski" (`Papermorph`),
"Assaf Kipnis" (`Claudemy`), "OrionSheep and WordLink contributors" (`WordLink`),
"Discover AI contributors" (`AILearningGuide`), and `SocialCoach`'s Apache
boilerplate, which carries **no copyright line at all**. So: **region is
recoverable from the licence file if and only if the copyright holder is an
institution.** Those rows stay `Global`, now for a stated reason rather than for
want of an instrument. A personal name is not a country — `PAIDEIA`'s holder
reads Korean and `tutor-mcp`'s reads French, and both are recorded `Global`.

**Two traps in the metadata that a licence column cannot show:**

- **`archived: true`.** `supertone-oss-archive/supertonic` is MIT, 13,757★,
  1,566 forks — and **archived**, which only the `archived` field says. The
  licence is clean and the code is frozen. Check the flag before shelving on
  stars.
- **An Apache licence with the template placeholders still in it.**
  `terracotta-education/terracotta`'s `LICENSE` is unmodified Apache-2.0
  boilerplate, including the literal `Copyright {yyyy} {name of copyright
  owner}`. GitHub's determination of "Apache-2.0" is correct; the grant names
  **no licensor**. Usable, and a diligence note.

**Three channels that do not work from this session, each failing in a way that
could be mistaken for a finding:**

- **`curl` to `github.com` or `api.github.com` → uniform HTTP 403.** A sweep of
  all 57 github.com URLs on this page returned 403 for every single one,
  including `moodle/moodle` and `odoo/odoo`. That is the outbound proxy, not the
  repositories. **If a check returns a uniform status for every URL, it is
  measuring the network, not the data.** A pass that treated those 403s as
  findings would have deleted the entire KB.
- **MCP `get_file_contents` → access denied for any third-party repo.** It is
  **repo-scoped** to the session's own attached repositories. It cannot be used
  to read a licence; `raw.githubusercontent.com` is the substitute.
- **`search_users` → no `location` field.** It returns login, id and avatar
  only, so a maintainer's country is unobtainable and region cannot be inferred
  from the owner profile. This is why four of this pass's five new rows are
  **Global**.

## Declared gaps

- **No published ranking of education AI agents exists.** The prescribed search
  `top open source AI agents education 2026 github MIT` returned, for the
  **fourth** consecutive pass, general-purpose agent listicles (OpenHands, CrewAI,
  AutoGen, Hermes) with an education angle bolted on, plus
  `ashishpatel26/500-AI-Agents-Projects`, a catalogue of use cases rather than
  agents. Four passes is enough to call it a property of the commentary layer
  rather than a gap in the search.
- **But "query the index, not the listicles" was too strong, and this pass
  disproved it.** The prescribed `github trending education AI 2026` search
  surfaced [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) — **MIT,
  71,498★**, formerly described here as the largest permissively licensed repository anywhere in this KB (🔴 **superseded `p582` by `microsoft/markitdown`, MIT, `193,266★`**) —
  which **no index sweep found**, because it carries no education topic. It is
  shelved in [`../repos/foundations.md`](../repos/foundations.md) as a
  content-production component rather than here, because it is not an education
  agent and padding this shelf with it would misrepresent the agent population.
  **Index sweeps find what is tagged; the open web finds what is famous.** Both
  channels are required.
- **The sweeps have a blind axis, now measured.** This shelf was built from
  `topic:ai-tutor` and `topic:agent-skills topic:education`. Adding
  `topic:ai-education stars:>150 pushed:>2026-10-20` returned **6 repositories,
  5 of them not on the shelf**, the largest at 1,034★. The previous pass's
  saturation finding was true of its axes and wrong as a claim about the
  population. **Next pass: sweep by capability (`topic:pptx`,
  `topic:text-to-speech`, `topic:pdf`, `topic:ocr`) and licence, not only by
  industry topic** — that is where the rest of the horizontal supply is hiding.
- ~~**LATAM: no LATAM-origin education agent qualified.**~~ **Closed, with a
  sting.** Two prior passes searched in English and in Spanish/Portuguese prose
  and concluded the absence was real. It was not — it was a *search-surface*
  gap. Querying GitHub directly with Portuguese and Spanish terms
  (`tutor OR educación OR educacao OR escola OR aprendizaje IA agente stars:>20`)
  returned [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent)
  at **2,750★** — larger than every North American row on this shelf. It is
  **unlicensed**, so the finding is simultaneously a closure and a new blocker.
  Correction to this KB's record: the earlier "two independent search strategies
  support this gap" was overconfident. Both strategies searched the *web*; neither
  searched the *index*.
- **EMEA agent origin is still effectively empty.** The one EMEA row
  (`pedagogy-benchmark`, 13★) is an evaluator, not a tutor. The previous pass's
  only EMEA candidate, `braiinz94/braiinz-education`, remains 0★ alpha. For EMEA
  engagements the *agent* layer is imported; the *platform* layer is now local
  and permissive — see `Selleo/mentingo` (MIT, Poland) in
  [`../repos/foundations.md`](../repos/foundations.md).
- **Seven rows have no stated geographic origin** — `anki-mcp-server`,
  `SocialCoach`, `OpenTutor`, and this pass's `Papermorph`, `Claudemy`,
  `WordLink` and `AI Learning Guide` — and are recorded as **Global** rather than
  guessed at. The count rose because the **instrument shrank**, not because
  origin diversified: `search_users` exposes no `location` in this session and
  `api.github.com` is 403, so owner country is unobtainable by any route.
  Guessing from a maintainer's name would have placed `Claudemy` and
  `Papermorph`; both are left Global. Region is a closed vocabulary here, and
  inventing a value to fill a column is how a filter starts lying.
- **No shelf candidate remains licence-unresolved — a first.** Both standing
  questions closed this pass from the licence text:
  `human-skill-tree` is **AGPL-3.0 with a dual-licensed `skills/` directory**,
  and `Auto-Empirical-Research-Skills` is **CC BY-SA 4.0 in the file**, not just
  the badge. One shelved row stays licence-defective (`mcp-canvas-lms`, now on
  three independent methods). Across four passes, **every licence defect found
  has been in the agent layer** — platforms state copyleft clearly; agents claim
  MIT loosely, ship share-alike, or say nothing, and do so at thousands of stars.
- **`Papermorph`'s copyright holder is a pseudonym** ("TedKaczynski"). The MIT
  text is a valid grant; the holder is unidentifiable. Recorded as a diligence
  item on a 1,034★ row, not as a disqualification.
- **Star counts for the two leaders are timestamped readings, not levels — and
  one circulating growth rate does not reproduce.** DeepTutor: **52,167★ at
  09:40 UTC**, **52,208★ at 10:42 UTC** — **+41 in ~62 minutes**. OpenMAIC:
  41,981★ at 09:40, **41,984★ at 10:10**. A third-party trend digest reports
  DeepTutor at **+2,282 stars on 2026-10-31**, which sustained would be ~95★/hour
  against the 41★/hour measured here. One hour is a thin sample and star arrivals
  cluster by timezone, so this does not refute the daily total — but **no pass
  should quote +2,282 as a rate.** The same digest family was recorded emitting
  "0 total stars with +2,870 today" at an earlier pass.
- **No education-specific agent *observability* or *regression* tooling was
  found — fifth consecutive pass, and this pass the gap got slightly worse.**
  `pedagogy-benchmark` (MIT, knowledge) and `learning-commons-org/evaluators`
  (rubric scoring) remain the only evaluation assets located, and neither is a
  runtime monitor. `evaluators`' licence is now **resolved and partly
  restrictive**: code **MIT**, prompts **CC BY 4.0**, but its two annotated
  corpora (CLEAR, PERSUADE 2.0) are **CC BY-NC-SA 4.0 — non-commercial**. So the
  hand-built regression suite that pattern **P-568-K** prescribes must **source
  its own corpus**; it cannot ship the one that exists. A tutor in production
  still has no open-source way to detect that it has drifted. This remains the
  clearest unmet build opportunity in the industry.

### Added on the fifth pass

- **The capability axis was swept, and it is where the volume is.** Four queries
  (`topic:text-to-speech license:mit`, `topic:ocr`, `topic:pptx`,
  plus `topic:intelligent-tutoring-system` / `topic:learning-analytics`) returned
  a permissive layer far larger than the entire education-agent population:
  **docling 69,909★ (MIT), PaddleOCR 92,024★ (Apache-2.0), tesseract 77,267★
  (Apache-2.0), MinerU 82,860★, OfficeCLI 32,854★ (Apache-2.0)**. None is an
  education agent and none is shelved here. **The lesson generalises past this
  KB:** the education-specific supply is thin and the *horizontal* supply that
  education work actually runs on is enormous, permissive, and invisible to every
  industry-topic sweep. Shelved in
  [`../repos/foundations.md`](../repos/foundations.md).
- **`topic:ai-education` is saturated — and this is the narrow claim, not the one
  that was retracted.** The fourth pass's own discovery query re-run this pass
  returns the identical 6 repositories, all shelved. Stating it as "the axis is
  exhausted" is supportable; stating it as "the population is covered" is the
  error the fourth pass corrected, and the capability sweep above is why.
- 🟡 **No education-specific agent *observability* or *runtime regression*
  tooling was found — sixth consecutive pass.** 🟢 **Half-superseded `2026-10-31`
  (`p570`): the *regression* half is now supplied** by the `topic:rubric` layer in
  [`../repos/foundations.md`](../repos/foundations.md) — seven granted assets,
  including the first that scores an **agent trajectory** (`AdaRubrics`,
  Apache-2.0, 368★). 🔴 **The *observability* half stands, seventh consecutive
  pass:** nothing education-specific detects a deployed tutor drifting. Read the
  original sentence below as true of its date and half-true now. Two differently shaped queries returned
  nothing new: a text search for evaluation/benchmark assets under
  `topic:education` returned **0 results**, and the ITS/learning-analytics sweeps
  surfaced no monitor. **But the gap is now one notch less absolute**, and the
  asset that narrows it is not an AI tool:
  [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
  (**Apache-2.0**, 21★, Java) is an **LTI-attached randomised-controlled-trial
  platform** for education research — random assignment, treatment variation
  inside real assignments, consent hidden from the teacher, non-consenting
  participants filtered from exports, identifiers stripped. That is **efficacy
  measurement**, not drift detection: it answers "did this intervention work",
  which no other asset in this KB does, and it still does not answer "has the
  tutor in production degraded since Tuesday". Both are needed; one now exists.
- **The regional-supply finding sharpened into something uncomfortable.** Across
  five passes, the education agents this KB has managed to place in a region are
  **systematically the licence-defective ones** — `dio-agent` (LATAM, 2,750★, no
  licence), `guru-latihan-dinamis` (Indonesia, 115★, no licence),
  `mcp-canvas-lms` (North America, 104★, no licence file). The regionally
  *placeable* and the legally *usable* sets barely intersect, and the reason is
  structural: regional provenance is easiest to read off hackathon and community
  projects, which are the least likely to have had a licence conversation. **For
  a client this means the local-supply story and the build-on-it story are
  usually about different repositories**, and conflating them is the most
  expensive mistake available on this page.
