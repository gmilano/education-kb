---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p791` — two agents added, one count corrected, one candidate REFUSED, one tree re-audited

🟢 **Method unchanged from `p790` and extended once.** Existence via `git ls-remote` (exit status read directly). Grant by **anchored title lines** in the served licence bytes, reported as a **set** when the file is an anthology (`T875`). Stars are claim-channel reads of `search/repositories` with a `repo:` qualifier, which return **exact integers**. 🟢 **New instrument this pass:** `git clone --filter=blob:none --no-checkout --depth 1` followed by `git cat-file -p HEAD:<path>` — it enumerates the whole tree, is case-exact, and fetches only the blobs actually read. It is now the cheapest byte channel this base has, and it is what settled `T882`.

| Agent | Repo | Grant, on the bytes | ★ (exact) | Last push | Verdict for Globant |
|---|---|---|---|---|---|
| **Study-Mate** 🆕 | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 **MIT** · `1,064 B` · `1b105b8e1b6b` | `1,436` | `2026-11-06` | 🟢 **Added, and the most directly reusable new row this pass.** A multi-agent builder turns a one-sentence goal into a private course, then a **course-scoped RAG tutor** teaches it with **per-lesson citations**. 🟢 The citation scoping is the valuable part: it is the architecture that answers *"where did the tutor get this?"* — the question every education client asks. 🟡 `363` files; vendors KaTeX (`lib/katex/LICENSE`, MIT) — clean to the first layer |
| **tutor-gpt** 🆕 | [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🔴 **GPL-3.0** · `35,149 B` · `f288702d2fa1` | `932` | `2026-02-20` | 🟡 **Added with two warnings, because the trend digests that surface it state neither.** A *diagnosis-first* tutor — it reasons about the learner's state before answering, which is the pedagogically interesting part. 🔴 **It is GPL-3.0, not permissive**, so it is a boundary deployment, never an embed. 🔴 **And it is `~9` months stale** (`2026-02-20`), so treat it as a reference architecture to read, not a dependency to adopt. 🔵 Its licence is also a live `T875` specimen: §13 at line `552` *names* the Affero GPL and a substring grader returns `AGPL-3.0` — the grant is GPL-3.0 |
| **Educhain** ✏️ | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** · `1,092 B` · `b46290b36e7f` | 🔴 **`388`** | `2026-05-29` | ✏️ **CORRECTED — this base published `~9k★` (cycle 2) and `~12k★` (cycle 3). The exact count is `388`**, and a full name sweep finds no `educhain` anywhere above `★22`, so the figure described no real repository (`T881`). 🟢 **The tool is still genuinely useful** — MIT, document/YouTube-to-course generation — but it is a small, six-month-stale project and must be presented as one |
| **OpenMAIC** 🔍 | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟡 **`TREE[MIT root + LGPL + ARPHIC-PL + OFL + bespoke-CN font]`** · root `1,065 B` · `76abc5f13261` | `43,376` | `2026-11-12` | 🔍 **Carried row, re-audited on the full `4,388`-file tree, and the root grant is not the tree's grant (`T882`).** Tsinghua MAIC's multi-agent interactive classroom; the largest education-specific agent repository this base holds after DeepTutor, and pushed today. 🟢 Root and all `7` first-party sub-packages are MIT. 🔴 `packages/mathml2omml` is **LGPL**; the renderer ships **three font grants**, one of them a non-OSI Chinese-language licence with **no-rename** and **no-resale-as-product** terms. 🟢 Usable — **carry the font licences and keep font names intact** |
| **DeepTutor** 🔍 | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · `11,408 B` (control reproduced) | `58,554` | `2026-11-07` | 🟢 **Carried, and still the single strongest permissive starting point in the sector.** 🔵 **Count re-read this pass: `58,554`.** For scale on how fast this row moves, this base published `~22k` at cycle 2 and `~24k` at cycle 3; search-channel digests put it near `52,800` on `2026-11-01`. 🟢 Apache-2.0, agent-native, actively pushed — the default spine for a tutoring engagement |

### 🔴 `p791` REFUSES one candidate, and says why

| Candidate | Why it was surfaced | Why it is REFUSED |
|---|---|---|
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | A GitHub trend digest presents it as *"6 specialized agents for personalized education"* — exactly the shape this base collects | 🔴 **There is no licence file anywhere in its tree.** `19` files enumerated on a blobless clone, `0` match `licen|copying|legal|terms|notice`; `search/repositories` independently returns `license: none`. 🔴 **No grant means no rights** — not "permissive by default". `★66`, last push `2025-11-04`, so it is also a year stale. 🔵 It is listed here rather than silently dropped, so the next pass does not spend the same probe on it |

🔵 **This refusal is the brief's rule working as intended: `fewer real rows always beat padding`.** `p791` adds `2` agents, corrects `1` count, re-audits `2` trees and refuses `1` candidate — and the refused row is the one a star-ranked digest would have published.


# Education AI agents — `p790`

**Every row below was verified this pass on two byte channels:** existence via `git ls-remote`
(exit status read directly, never through a pipe), and the licence grant by **clause presence** in
the served `LICENSE` bytes. No row is carried on a vendor claim, a star ranking or a blog.

🔴 **New rule this pass, and it reverses one of this base's own published verdicts (`T875`).** A
licence file may **quote other licences**. Grading one by substring presence is therefore unsound in
both directions: GPL-3.0's own §13 *names* the GNU Affero GPL, and a bundled dependency's
`All rights reserved.` line sits inside a file whose own grant is open. **A file containing `N`
licence titles is an ANTHOLOGY and has no single family** — it is graded by anchored title lines and
reported as a set. `Kosudo/nextSIS` is the row this cost, and it is corrected below.

> **Channel discipline (`T844`, amended this pass — `T860`).** Repository existence and licence
> bytes are **byte-verified**. 🔴 **The page channel is GONE this pass:** `github.com` returns
> `403` through this session's proxy for every non-attached repository, and so does
> `api.github.com/repos/{owner}/{repo}`. 🟢 **Stars below are claim-channel reads of
> `search/repositories` with `repo:` qualifiers — which return EXACT integers**, not GitHub's
> rounded `58.5k`, and which reproduced every rounded page-read `p787` published. Every market,
> adoption and regulatory figure in this base remains **search-channel testimony**.

**Controls for this pass:** 7 of 7 known-good rows reproduced the bytes this base already recorded
(`HKUDS/DeepTutor` 11,408 B · `moodle/moodle` 35,147 B · `sakaiproject/sakai` 11,120 B ·
`frappe/lms` 33,893 B · `hedyorg/hedy` 13,827 B · `jupyter/nbgrader` 1,512 B · `oppia/oppia`
11,358 B). 2 planted negatives were DEAD as designed. 🔴 **6 defects in this pass's own
instruments were caught by those controls and fixed before any verdict shipped** — see
`intel/trends.md` `T860`–`T863`.

🔴 **The one thing to read before using this file.** `p787-D` is discharged below and it changes how
every row here must be read: **a repository-level grant says nothing about the grant on its
dependencies, and 4 of the 7 highest-star permissive education repos carry copyleft in their
declared direct dependencies.** See `## Dependency grants` at the foot of this file.

## The two poles — both APAC-origin, both permissive at the repository level

| Agent | Address | Grant, on the bytes | ★ (exact) | Region | What it is |
|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · `11,408 B` · `60fb3bdfddb3` | `58,508` | APAC | Lifelong personalised tutoring workspace — tutoring, retrieval over the learner's own materials, practice, mastery tracking. **The most permissively-granted mature tutor in the sector.** ⚠️ **`pyte` (LGPL-3.0) is a declared direct dependency** (`T861`) |
| **OpenMAIC** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT · `1,065 B` · `717b69cbe2f4` | `43,365` | APAC | Tsinghua's Open Multi-Agent Interactive Classroom — turns a topic or document into a classroom with AI teacher and AI classmates, generating slides, quizzes, simulations and PBL activities. ⚠️ **2 of 181 direct dependencies are copyleft:** `mathml2omml` (LGPL-3.0-or-later) and `jszip` (`MIT OR GPL-3.0-or-later`, so the MIT arm must be **elected in writing**) |

## Teaching-as-a-skill — the packaging shift, now with a derivative in the wild

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **agent_skills** (`socratic-tutor`) | [`janestreet/agent_skills`](https://github.com/janestreet/agent_skills) | MIT · `1,120 B` · `7c6715c29548` | `6,813` | North America | Jane Street's skill set; the `socratic-tutor/` skill turns an LLM into a strict tutor — diagnostic, skill map with levels 0–5, one question at a time, spaced review, final assessment. **Tutoring shipped as a skill directory, not an application.** Canonical owner is `janestreet`; `jane-street/agent_skills` is DEAD |
| **socratic-tutor** `NEW` | [`nuwaves/socratic-tutor`](https://github.com/nuwaves/socratic-tutor) | MIT · `1,143 B` · `2e34df6e23bd` | `2` | Global | 🟢 **The first downstream derivative of the above, created `2026-11-09`** — the same skill extracted as a standalone, installable unit with saved progress. `T851` predicted this packaging would travel; it has, in under a week |
| **china-k12-teacher-skills** | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | Apache-2.0 · `11,359 B` · `f1c6c4420e7d` | `3` | APAC | China-localised K-12 teacher skills with curriculum-aware lesson planning |

## EMEA — the gap `p787` recorded as empty, and it is not

🟢 **`ACTION p787-E` discharged by refutation (`T862`).** `p787` searched for a European-origin
open-source education agent **in English**, found only sovereign-LLM infrastructure, and recorded the
slot as empty. Querying the same slot in **Dutch, German, French and Greek** returned agents on the
first attempt. Every row below is byte-verified and **new to this base**.

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **onderwijsin/agents** `NEW` | [`onderwijsin/agents`](https://github.com/onderwijsin/agents) | **MIT** · `1,079 B` · `0b3eabc034fa` | `0` | EMEA | 🟢 **The find that refutes `T856`.** Provider-agnostic AI plugins and skills for Dutch **onderwijs** (education). 🔵 Found by querying `onderwijs AI agent`, which returned **exactly one** repository — this one. At `0★` it is below every star floor this base has ever used |
| **sherpa** `NEW` | [`SeydinaBANE/sherpa`](https://github.com/SeydinaBANE/sherpa) | **MIT** · `1,063 B` · `6411f2de98c1` | `0` | EMEA | French-language exam-preparation tutor: **grounded RAG with citations** plus agents. 🔵 Citation-grounding is the single feature `T859` argues an education deliverable most needs |
| **parcours-maths-ia** `NEW` | [`Warok-dev/parcours-maths-ia`](https://github.com/Warok-dev/parcours-maths-ia) | **MIT** · `1,066 B` · `51dc673f15a0` | `0` | EMEA | 2D educational maths game for French **CE1–CE2** with automatic exercise generation — curriculum-specific, primary-level |
| **dowze** `NEW` | [`Louisdelez/dowze`](https://github.com/Louisdelez/dowze) | **MIT** · `1,068 B` · `2a30b43ecd06` | `0` | EMEA | French lifelong-learning AI tutor, explicitly framed as a **bien commun** (commons) |
| **skepsis** `NEW` | [`ionpetro/skepsis`](https://github.com/ionpetro/skepsis) | **MIT** · `1,072 B` · `31a864169289` | `3` | EMEA | Teaches the Greek hiding inside everyday English in 3-minute lessons; ships a web app **and an MCP server**, so another agent can teach from it |
| **eagle-aig** `NEW` | [`LIST-LUXEMBOURG/eagle-aig`](https://github.com/LIST-LUXEMBOURG/eagle-aig) | **Apache-2.0** · `11,358 B` · `99cecb066ecf` | — | EMEA | 🟢 **Luxembourg Institute of Science and Technology** — a national public research institute. **Rescued from this base's ungranted class this pass** (`p787-B`): it was filed as an absence and has carried Apache-2.0 all along |
| 🟢 **EduAgentic** `NEW` | [`kamalelafoui/Agentic-AI-EdTech-J33-J34`](https://github.com/kamalelafoui/Agentic-AI-EdTech-J33-J34) | 🟢 **MIT** · `1,071 B` · `7685db14663f` | `0` | EMEA (francophone) | 🟢 **The first EMEA row in this base that is an MCP **server** plus an A2A multi-agent system rather than an application** — six EdTech tools exposed over **MCP**, agents that **discover and delegate** over **A2A**, and a Streamlit dashboard to observe both. Dated `2026-11-11`. 🟢 **`100 % synthétiques · 0 apprenant réel`** — the author states on the record that no real learner data is present, which is the declaration an EMEA deployment has to make anyway. 🔵 Francophone, authored under a *Centre des Très Petites Entreprises Solidaires* programme; **the country is not stated in the repository and is not inferred here** |

### 🟢 `elimu-ai` — a 66-repository MIT African education ecosystem this base was already citing

🔴 **This base cited `elimu-ai` at `agents/trending.md:24964` and never placed it.** It surfaced only
because it was the **single false positive** of `p787-A`'s login-validity clause (`T863`). All seven
core repositories are **MIT, `1,065 B`, identical licence text, pushed within the last week.**

| Repo | Address | Grant, on the bytes | ★ | Role |
|---|---|---|---|---|
| **webapp** | [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) | MIT · `1,065 B` · `f471cb573ae3` | `41` | Hosts the Android applications and the educational content library |
| **appstore** | [`elimu-ai/appstore`](https://github.com/elimu-ai/appstore) | MIT · `1,065 B` · `65a7ab4e8d50` | `29` | On-device APK download/install/update — **content delivery without an app store**, which is the binding constraint it is built for |
| **ml-authentication** | [`elimu-ai/ml-authentication`](https://github.com/elimu-ai/ml-authentication) | MIT · `1,065 B` · `0a7a6bb02ab6` | `16` | On-device student authentication. ⚠️ Biometric identification of children — read `T854` and EU Art. 5 before deploying this in EMEA or North America |
| **launcher** | [`elimu-ai/launcher`](https://github.com/elimu-ai/launcher) | MIT · `1,065 B` · `b50a175a7056` | `9` | Android launcher that constrains the device to a single instructional path |
| **ml-storybook-reading-level** | [`elimu-ai/ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) | MIT · `1,065 B` · `119642b8b1c3` | `8` | 🟢 ML model predicting a storybook's reading level — **a real, permissive levelling model**, which no other row in this base supplies |
| **ml-storybook-recommender** | [`elimu-ai/ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | MIT · `1,065 B` · `940048e2cc32` | `3` | Predicts likability of unread storybooks |
| **model** | [`elimu-ai/model`](https://github.com/elimu-ai/model) | MIT · `1,065 B` · `5f16dd17e351` | `4` | Shared library across the webapp and the Android apps |

## APAC — `ACTION p787-F` discharged, and the three countries differ completely

### 🟢 India — the region's richest curriculum-specific supply

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **OpenVidya** `NEW` | [`dpaul0501/OpenVidya`](https://github.com/dpaul0501/OpenVidya) | 🔴 **AGPL-3.0** · `34,523 B` · `1224dcd5693b` | `2` | 🟢 **The most strategically interesting row of the pass: an OpenMAIC derivative redesigned for NCERT/CBSE.** 🔴 **And it relicensed upward** — OpenMAIC is MIT, this fork is AGPL-3.0. MIT permits that, and it means the India-localised classroom **cannot** be embedded in a client deliverable the way its parent can |
| **RAG-Enhanced-NCERT-Tutor** `NEW` | [`praj2408/RAG-Enhanced-NCERT-Tutor`](https://github.com/praj2408/RAG-Enhanced-NCERT-Tutor) | MIT · `1,072 B` · `adf4c082db90` | `5` | Retrieval-grounded tutor over the **NCERT** national curriculum |
| **CBSE_Home-Tutor** `NEW` | [`mandarab76/CBSE_Home-Tutor`](https://github.com/mandarab76/CBSE_Home-Tutor) | MIT · `1,077 B` · `f987f634f5e0` | `1` | **CBSE** tutor spanning classes 1–12 |
| **ai-agent-to-learn-faster-and-better** `NEW` | [`abhijeetgupta23/ai-agent-to-learn-faster-and-better`](https://github.com/abhijeetgupta23/ai-agent-to-learn-faster-and-better) | MIT · `1,071 B` · `df69fd3331dd` | `4` | Adaptive tutor that personalises **lesson modality** from a learning-science knowledge graph |
| **FunctionVisualizer-V3** `NEW` | [`Adarsh-61/FunctionVisualizer-V3`](https://github.com/Adarsh-61/FunctionVisualizer-V3) | MIT · `1,056 B` · `10099c811f61` | `3` | Interactive NCERT mathematics visualisation |
| **NCERT-AI-Teacher-Assistant** `NEW` | [`Prady029/NCERT-AI-Teacher-Assistant`](https://github.com/Prady029/NCERT-AI-Teacher-Assistant) | 🔴 GPL-3.0 · `35,149 B` · `5e24bf860660` | `5` | Lesson plans and question sets for teachers. 🔴 Copyleft |

🟢 **`p787-F`'s India finding, stated plainly:** India's gap was never supply, it was **vocabulary**.
`tutor agent education India curriculum` returned `0`. `NCERT AI` returned **`330`**.

### 🟢 South Korea — placed for the first time, behind a semantic trap

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **spring-ai-tutor** `NEW` | [`jungtaejin/spring-ai-tutor`](https://github.com/jungtaejin/spring-ai-tutor) | MIT · `1,069 B` · `8ca838adabcc` | `0` | Korean tutoring API on Spring AI — structured output, conversation memory, tool calling, SSE streaming |
| **Haeksim** `NEW` | [`Seongbong-Ha/Haeksim`](https://github.com/Seongbong-Ha/Haeksim) | MIT · `1,069 B` · `242b3f09aa73` | `0` | 핵심 ("core") — an NLP AI learning-tutor project |

🔴 **The trap, recorded because it will recur.** Korean **교육** means both *education* and
*corporate training*. The query `AI 교육 에이전트` returned `20` repositories of which **almost none
are education agents** — they are agent-training course materials (a Samsung practitioner
curriculum, "AI maestro" week-4 coursework). 🟢 The productive query was `학습 튜터 AI`
(*learning tutor*), which returned `12`. **A word that means two things returns the wrong head.**

### 🟢 Japan — the measured gap, DISCHARGED, and it was a category error (`p789`)

🔴 **`p788` measured Japan at `3` repositories and called it this base's only *measured* supply
gap, surviving in-language querying.** 🟢 **It does not survive the right *category*.** Japanese
education-AI work is published under **`校務`** (*kōmu* — school administrative duties), not under
tutoring vocabulary. The supply is **administrative and curricular, not conversational** — the
opposite of the Indian and Chinese supply this base has placed (`T870`).

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| 🟢 **jp-k12-digital-ai-textbook** `NEW` | [`masa-san-jp/jp-k12-digital-ai-textbook`](https://github.com/masa-san-jp/jp-k12-digital-ai-textbook) | 🟢 MIT · `1,068 B` · `d7c583c9f444` | `1` | 🟢 **The best Japan-origin education artefact this base has placed, and it is permissive.** All `12` grades (小1–高3), aligned to the **next 学習指導要領** *and* the **UNESCO AI Competency Framework** |
| 🟢 **school-office-generative-ai-30** `NEW` | [`kumaken-1/school-office-generative-ai-30`](https://github.com/kumaken-1/school-office-generative-ai-30) | 🟢 **MIT · `1,102 B` · `c42f19d27c4d`** (`LICENSE-CODE`) **+ CC BY 4.0 · `925 B` · `738b8fc14a61`** (`LICENSE-CONTENT`) | `0` | 「生成AI 30のチャレンジⅡ〜校務編〜」 — `30` graded exercises on real school-administration tasks for staff who have finished an introductory course. 🔵 Its split grant is defect `7` of this pass (`T869`) |
| 🟡 **tracen-ai-tazuna** `NEW` | [`naritaroad/tracen-ai-tazuna`](https://github.com/naritaroad/tracen-ai-tazuna) | 🟢 MIT · `1,067 B` · `5aff4e618c56` | `0` | A school **administrative** AI proof-of-concept. 🔴 **Barred from client work despite its grant:** an unofficial *Uma Musume* fan project — MIT covers the authors' code, never the franchise's trademarks or characters |

🔴 **The one that is barred, which is the useful half of the finding.**
[`nahisaho/teacher-genai-playbook`](https://github.com/nahisaho/teacher-genai-playbook) — teacher
generative-AI training material for classroom *and* `校務` use, the most engagement-shaped Japanese
artefact found — is **CC BY-NC 4.0 · `1,222 B` · `92625a14d19b`. NonCommercial: it cannot be used in
a paid engagement.** The search channel said `NOASSERTION`; the bytes name the bar precisely.
🔴 Also measured: [`chc-chupea/news-grade-reader`](https://github.com/chc-chupea/news-grade-reader)
**GPL-3.0 · `35,149 B` · `3972dc9744f6`** — grade-levelled news rewriting against MEXT curriculum
guidance, copyleft, and it states in terms that it is *not* MEXT-endorsed.

🔵 **Measured Japanese totals, so the shape of the supply is on the record:** `校務 AI` → **`5`** ·
`塾 AI 学習` → **`7`** · `学習指導要領 AI` → **`2`** · `教育 LLM 日本語` → **`1`** ·
`授業 支援 AI 教材` → **`0`**. 🔴 [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset)
remains **ungranted** and remains worth asking for.

### 🟢 Malaysia — `p789`'s declared gap, DISCHARGED (`p790`)

🔴 `p789` recorded Malaysia as one of its three thinnest *measured* regions at **`1`, ungranted**.
🟢 **It is now placed, and the repository is granted.**

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| 🟢 **StudyLah** `NEW` | [`haziqhalifi/StudyLah`](https://github.com/haziqhalifi/StudyLah) | 🟢 MIT · `1,069 B` · `c6ee7bb5db4a` | `0` | 🟢 **Malaysia placed.** Adaptive learning for **SPM Form 5 Mathematics**: diagnostic quiz inferring misconceptions per topic, next-question selection from weakest topic + recent accuracy trend, generated MCQs targeting measured skill gaps, spaced-repetition scheduling — and **explanations written in Bahasa Malaysia**. 🔵 It also matches *explanation style* (step-by-step / formula-first / shortcut / analogy) to measured accuracy, which is a pedagogy choice almost no row in this base makes explicit. ⚠️ Hackathon-origin, single contributor |

🔵 **Measured Malaysian totals, so the shape is on the record:** `AI tutor SPM Malaysia` → **`1`** ·
`tutor AI pendidikan Malaysia` → **`0`**. 🔴 **The supply is one repository.** It is placed because it
is real and granted, not because it is deep — and the national demand behind it is large
(`intel/market.md`, APAC).

### China

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **AI-tutor** `NEW` | [`qiyuxi24/AI-tutor`](https://github.com/qiyuxi24/AI-tutor) | MIT · `1,065 B` · `046f65596541` | `4` | Knowledge-graph-driven guidance agent: knowledge map, learning path, learner profile, question generation. `413` test cases, L1–L4 live-API evaluation, BM25 gating with RRF hybrid retrieval — **the most explicitly evaluated small agent in this base** |
| **VeryMath-textbook-copilot** | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | Apache-2.0 · `11,338 B` · `1183af0d8197` | `21` | Textbook pane beside a coding-agent pane: explanations, exercises, mind maps, knowledge graphs, LaTeX courseware |
| **Math-Modeling-Agent-Flow** | [`mantou6666/Math-Modeling-Agent-Flow`](https://github.com/mantou6666/Math-Modeling-Agent-Flow) | MIT · `1,067 B` · `69b2a4f15995` | `28` | Four-stage Solver→Paper pipeline for the CUMCM / MCM-ICM modelling competitions |
| **xuelian-agent** | [`llwand1/xuelian-agent`](https://github.com/llwand1/xuelian-agent) | MIT · `1,062 B` · `956783be029f` | — | Chinese-language study agent |

## 🟢 School operations — `p788`'s standing gap, discharged with `5` permissive rows (`p789`)

🔴 **`p788`: "School-operations agents (timetabling, attendance, safeguarding) — still no
permissive row."** 🟢 **There are five, and the category has a genuine architectural signature: a
constraint solver with a human approval gate, not a chatbot** (`T874`).

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| 🟢 **schoolflow-agent** `NEW` | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) | 🟢 MIT · `1,081 B` · `1b7481d92d0f` | `0` | Global | 🟢 **The row the gap was asking for.** Timetable **disruptions**, teacher absences and substitutions, with **human-approved** schedule updates. 🔵 The approval gate is the project's own design, not this base's retrofit |
| 🟢 **school-timetable-timefold-case-study** `NEW` | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | `1` | Global | 🟢 **The reference architecture for the category:** a real **constraint solver** (Timefold) on Quarkus, driven by coding agents. Scheduling is a solver problem with an LLM at the edges |
| 🟢 **Timable** `NEW` | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | `1` | Global | High-school timetabling on **OR-Tools** + Streamlit. The second independent solver row, which is what makes it a pattern rather than a project |
| 🟢 **classcharts-agent** `NEW` | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | `0` | EMEA 🇬🇧 | 🟢 **Read-only** CLI and agent skill over **ClassCharts** (UK homework/behaviour system). 🔵 A deliberately read-only attachment to a live school system — the safest first integration, and this base's second EMEA LMS/MIS attachment point after `brightspace-d2l-mcp` |
| 🟢 **TIMETABLE-SOFTWARE** `NEW` | [`jeevanjacob1/TIMETABLE-SOFTWARE`](https://github.com/jeevanjacob1/TIMETABLE-SOFTWARE) | 🟢 MIT · `1,056 B` · `1126322e2cc8` | `0` | Global | Clash-free generator on React + TypeScript + Supabase — the web-stack variant of the same job |
| 🟢 **ai-adoption-education** `NEW` | [`VictorOsondu/ai-adoption-education`](https://github.com/VictorOsondu/ai-adoption-education) | 🟢 **CC BY 4.0 content + MIT code**, one `752 B` file · `2e9c34096bf9` | `2` | Global | 🟢 **Safeguarding-first** AI adoption guidance for schools and higher ed, with task-suitability and assessment-integrity material. 🔵 Search channel said `NOASSERTION`; the bytes grant **commercial** use with a named attribution string |

🔴 **Ungranted in this category and worth asking for:**
[`NSK-394/schoolbridge-mcp`](https://github.com/NSK-394/schoolbridge-mcp) — an MCP server giving
agents **role-based** access to school ERP data (attendance, fees, student records). 🔵 Role-based
access over an SIS is exactly the control surface a school engagement needs.
🔴 [`zulfahmi93/susun-jadual`](https://github.com/zulfahmi93/susun-jadual) 🇲🇾 — Malaysian
*sekolah rendah/menengah* timetabling, ungranted; **Malaysia remains unplaced.**

## 🟢 Africa — Nigeria and South Africa placed for the first time (`p789`)

🔴 **`p788`: "African national curricula other than Kenya's CBC and Morocco's Bac — none found."**
🟢 **They exist in quantity.** `WAEC AI tutor` alone returns **`35`** repositories. 🔴 **And `32` of
them serve no grant** — the ratio is the finding, not the count (`T871`).

| Agent | Address | Grant, on the bytes | ★ | Country | What it is |
|---|---|---|---|---|---|
| 🟢 **Offline-First-Android-AI-Tutoring-App** `NEW` | [`thesavvybyjude/Offline-First-Android-AI-Tutoring-App`](https://github.com/thesavvybyjude/Offline-First-Android-AI-Tutoring-App) | 🟢 MIT · `1,070 B` · `a2fe733bd153` | `1` | 🇳🇬 NG | 🟢 **The headline African row, and the artefact `p788` asked for by name.** `p788` flagged an offline NCERT doubt-solver as "exactly the shape a low-connectivity engagement needs" **and had to file it ungranted**. This is that shape for Africa **with a grant**: on-device LLM, RAG over the **WAEC/NERDC** curriculum, spaced repetition |
| 🟢 **ai-tutor-app** `NEW` | [`nitoni-jim/ai-tutor-app`](https://github.com/nitoni-jim/ai-tutor-app) | 🟢 MIT · `1,074 B` · `d33e0685ea0f` | `1` | 🇳🇬 NG | Intelligent tutoring system over **WAEC / NECO / JAMB** — all three Nigerian examination boards in one tree |
| 🟢 **waec-ai-tutor** `NEW` | [`Ass-Gaye/waec-ai-tutor`](https://github.com/Ass-Gaye/waec-ai-tutor) | 🟢 MIT · `1,065 B` · `54383781845a` | `0` | 🇳🇬 NG | The third permissive WAEC row of the `35` |
| 🟢 **homework-hero-sa** `NEW` | [`Masondo86/homework-hero-sa`](https://github.com/Masondo86/homework-hero-sa) | 🟢 MIT · `1,070 B` · `88eb94d99d6c` | `0` | 🇿🇦 ZA | 🟢 **South Africa placed for the first time.** Homework scheduling and learner accountability on the **CAPS** curriculum — an operations tool, not a tutor |
| 🟢 **nextgen-learn** `NEW` | [`daddysystem/nextgen-learn`](https://github.com/daddysystem/nextgen-learn) | 🟢 **BSL-1.0 (Boost) · `1,338 B` · `c9bff7573892`** | `0` | 🇿🇦 ZA | Free **CAPS**-following study site with an AI tutor. 🟢 **A licence family new to this base:** Boost is permissive, OSI-approved, and waives attribution for object-code-only distribution |

#### 🔴 Tanzania, Ghana and Kenya — probed this pass, and NOT discharged (`p790`)

🔴 **`p789` named Tanzania (`0`), Ghana (`1`, ungranted) and Malaysia (`1`, ungranted) as its
thinnest measured regions. Malaysia is discharged above. The two African ones are not, and the
reasons differ.**

| Country | What was measured | Verdict |
|---|---|---|
| 🔴 🇹🇿 **Tanzania** | `elimu AI Tanzania` → **`2`**. One is ungranted (`kadioko/ElimuAI`, Swahili e-learning with M-Pesa). The other, [`sangadanson1-dot/-Vet-IDEA-TZ`](https://github.com/sangadanson1-dot/-Vet-IDEA-TZ), **is MIT · `1,067 B` · `238c1bbb3bc0`** | 🔴 **NOT DISCHARGED — and the MIT row is a CATEGORY ERROR IN THE OPPOSITE DIRECTION FROM JAPAN'S (`T877`).** Read in Swahili, `Vet Idea TZ` serves **wafugaji na wataalamu wa mifugo** — livestock keepers and veterinary professionals. It teaches **afya ya wanyama, magonjwa, chanjo, lishe** (animal health, disease, vaccination, nutrition). 🟢 It is real, granted, AI-bearing education — **veterinary extension education, not school education.** 🔵 Placing it would have discharged the gap on paper and left a client engagement with nothing. **Tanzania's school-education agent supply is still `0`** |
| 🔴 🇬🇭 **Ghana** | `WASSCE AI tutor` → **`11`**; `Ghana education AI tutor curriculum` → **`0`**. `5` probed on the byte channel: `3` ALIVE serving **no grant**, **`2` DEAD** (`Bestisco/My-WASSCE-Companion`, `Elite2828/ACE-AI-Tutor` — both `rc=2`, re-probed and confirmed) | 🔴 **NOT DISCHARGED, and now QUANTIFIED rather than estimated.** `p789`'s "`1`, ungranted" understated the supply by about `10×` and read the grant correctly. 🟢 **Ghana's WASSCE supply is substantial and its grant rate is `0`** — the same shape `T871` recorded for Africa generally, measured at one country. 🔵 **And the search index is stale here specifically:** `2` of `5` addresses it returned no longer exist |
| 🔴 🇰🇪 **Kenya** | `AI tutor Kenya CBC curriculum` → **`3`**, all probed. `2` serve no grant | 🔴 **The third is a HARDER bar than an absence.** [`gabrielmahia/shule-ai`](https://github.com/gabrielmahia/shule-ai) — KCPE/KCSE prep on the **CBC** syllabus answering in Kiswahili — serves **`209 B` · `9dd285c3704d`: Creative Commons `CC BY-NC-ND 4.0`**. 🔴 **NonCommercial *and* NoDerivatives — it cannot be used in a paid engagement and cannot be modified at all**, which bars even the adaptation a curriculum row exists for. 🔵 **The search channel indexed it `NOASSERTION`.** Third consecutive pass in which index silence hid a grant, and the second in which the hidden grant was a *bar* (`T863`) |

🔵 **The useful sentence for an African engagement, now measured across four countries:** Nigeria and
South Africa are **placed and granted** (`5` rows above); **Ghana, Kenya and Tanzania have real
supply and no usable grant.** The remedy is the same in all three and it is not engineering — it is
an upstream licence request, carried as `ACTION p790-B`.

🔵 **Measured African totals, so the remaining gaps are informed ones:** `WAEC AI tutor` → **`35`**
(`3` permissive) · `CAPS curriculum South Africa AI` → **`10`** (`2` permissive) ·
`Nigeria curriculum AI tutor` → **`6`** · `BECE Ghana AI education` → **`1`**, and it is ungranted
([`ghwmelite-dotcom/brilla-study-platform`](https://github.com/ghwmelite-dotcom/brilla-study-platform),
BECE/WASSCE/NSMQ) · `NECTA Tanzania education AI` → 🔴 **`0` — a measured zero, not an unexamined silence.**

🔴 **Ungranted and worth asking for:** [`7irelo/aptiverse`](https://github.com/7irelo/aptiverse) 🇿🇦
`4★` — CAPS-aligned practice tests with **auditable marking**, the highest-starred and most
engagement-shaped African artefact found; and
[`tosinamuda/teacher-agent-itu-hackathon`](https://github.com/tosinamuda/teacher-agent-itu-hackathon)
🇳🇬 — *Plan-to-Tutor*, a **teacher-in-the-loop** agent on the Nigerian curriculum from the
**ITU AI for Good** Lab hackathon. 🔵 Teacher-in-the-loop and auditable marking are the two design
choices this base keeps recommending — both found in African repositories, both ungranted.

## Tutors and adaptive engines

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT · `1,105 B` · `fae8cc474484` | `279` | North America | UC Berkeley (CAHLR) adaptive tutoring with **Bayesian Knowledge Tracing** mastery estimation. 🟢 **`0` of `43` direct dependencies are copyleft — the cleanest dependency tree measured this pass** |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT · `1,068 B` · `cfe41f874290` | `175` | Global | Block-based adaptive learning workspace that runs locally. 3 specialist agents (Tutor, Planner, Layout), 10+ LLM providers. 🟢 `1` direct dependency, `0` copyleft. ⚠️ `cosark/OpenTutor` is a FORK at `0★` |
| **examprep-agent** `NEW` | [`ZeKaiNie/examprep-agent`](https://github.com/ZeKaiNie/examprep-agent) | MIT · `1,065 B` · `83fad934ea90` | `1` | Global | Study agent that teaches **only** from the learner's own slides and homework — a scoping constraint, not a limitation |
| **claude-study-agent** `NEW` | [`dymchenkko/claude-study-agent`](https://github.com/dymchenkko/claude-study-agent) | MIT · `1,067 B` · `527f9ac590a0` | `3` | Global | University-course study agent built on a coding-agent host, learning from the learner's own slides and PDFs |
| **lessonfolk** `NEW` | [`CGSeb/lessonfolk`](https://github.com/CGSeb/lessonfolk) | MIT · `1,063 B` · `7710ddf025ab` | `3` | Global | Learn AI from zero to advanced with an agent as the tutor |
| **algebench** `NEW` | [`ibenian/algebench`](https://github.com/ibenian/algebench) | MIT · `1,063 B` · `6794217849f9` | `8` | Global | Interactive **3D** maths visualiser with an agentic tutor — concepts explored through live simulation |
| **rag-tutor** `NEW` | [`villadalmine/rag-tutor`](https://github.com/villadalmine/rag-tutor) | **Apache-2.0** · `7,450 B` · `b0bc280f04ec` | `2` | Global | Sovereign, local-first tutor over technical books: hybrid RAG + agentic loop + MCP server. 🔴 **GitHub indexes this `NOASSERTION`; the bytes are Apache-2.0 with all `9` operative sections verified individually** — the `3,907 B` shortfall is the omitted non-operative APPENDIX only (`T845`: length is not a verdict) |
| **Thesaurus** `NEW` | [`Ahhsaaaaan/Thesaurus`](https://github.com/Ahhsaaaaan/Thesaurus) | Apache-2.0 · `11,343 B` · `dc29f0d739ff` | `0` | Global | Classroom knowledge base: teachers upload course documents, students query them over RAG |
| **Learning-Agent-System** | [`VaishnaviSingh-Analyst/Learning-Agent-System`](https://github.com/VaishnaviSingh-Analyst/Learning-Agent-System) | MIT · `1,086 B` · `fb2da327c928` | — | Global | LangGraph tutor on Ollama: checkpointed learning paths, tiered 5-3-2 assessment, a 70% pass bar, Feynman-style re-teaching |
| **no-vibe** | [`rizukirr/no-vibe`](https://github.com/rizukirr/no-vibe) | MIT · `1,065 B` · `5b8cb2f6d072` | `48` | Global | Turns a coding agent into a tutor that reads the learner's level and adapts — pedagogy applied to the agent rather than the content |
| **llm-edu-suite** `NEW` | [`ZoodiacR/llm-edu-suite`](https://github.com/ZoodiacR/llm-edu-suite) | MIT · `1,065 B` · `da605cdaf27e` | `3` | Global | Learn LLM engineering by building and measuring each layer — tokenizer, transformer, pre-training |
| 🟢 **coursewright** `NEW` | [`shivarajbakale/coursewright`](https://github.com/shivarajbakale/coursewright) | 🟢 MIT · `1,072 B` · `4fd5e20735ab` | `0` | Global | Name a subject; **a team of agents writes the course** — chapters from first principles, step-by-step diagrams, quizzes, projects, notes beside every chapter, and a tutor that answers **from the generated course only**. 🔵 The scoping constraint (`examprep-agent`'s virtue) applied to *generated* rather than supplied material |
| 🟢 **spanish-tutor-ai** `NEW` | [`MrEug3n1o/spanish-tutor-ai`](https://github.com/MrEug3n1o/spanish-tutor-ai) | 🟢 MIT · `1,069 B` · `6f0ebd566861` | `0` | Global | 🟢 **The most complete local-only tutor this base has placed, and the sovereignty pattern's best single reference.** Runs **entirely on local open-source models — no API keys, no per-token bill** — and checks its own work: chat tutor with tools, synthetic-data generator, retrieval over grammar notes, a **QLoRA-fine-tuned** article checker, and an agent that **plans each day's lesson itself**. Wrong quiz answers return the topic to tomorrow's plan. 🔵 Named for the language taught, not a region — it is `P788-4`'s missing reference implementation |
| 🟢 **Multimodal-RAG-AI-Tutor-Agent** `NEW` | [`yashpandey2409/Multimodal-RAG-AI-Tutor-Agent`](https://github.com/yashpandey2409/Multimodal-RAG-AI-Tutor-Agent) | 🟢 MIT · `1,068 B` · `59d3fe71eea6` | `0` | Global | Multimodal retrieval-grounded tutor — the multimodal variant of the citation-grounded shape `T859` argues an education deliverable most needs |
| **learnharness** | [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | 🔴 **AGPL-3.0** · `34,523 B` · `cb25c8e49b85` | — | Global | Agent harness for learning difficult subjects. 🔴 **Copyleft: network-use triggers source disclosure** — reference or separately-deployed service only |

## Assessment and grading

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **GradeAI** | [`orancs11/GradeAI`](https://github.com/orancs11/GradeAI) | MIT · `1,061 B` · `93bd8bebe253` | `4` | Global | Automated grading. Small, but the grant is clean and the scope is exactly what EU Annex III and several US states now regulate |
| **instructional_agents** | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | MIT · `1,067 B` · `f835eb45f508` | — | Global | Multi-agent generation of instructional material and courseware |

## LATAM

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **TutoriasITA** | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | MIT · `1,077 B` · `3184f6e7f75a` | `7` | LATAM | Institutional tutoring system, **Tecnológico Nacional de México, Campus Acapulco** |
| **TutorLSM** | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | Apache-2.0 · `11,357 B` · `ae26aa487282` | `0` | LATAM | **Mexican Sign Language (LSM)** learning and practice — accessibility supply in Spanish, permissively granted |
| **paes-mcp** | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | **MIT (Spanish text)** · `2,018 B` · `84e7f6106b38` · 🔴 **SCOPE-LIMITED** | `0` | LATAM | MCP server over Chile's **PAES** university-admission test. 🔴 **CORRECTION TO `p787` (`T864`): the MIT grant covers the SOURCE CODE AND DOCUMENTATION ONLY.** The licence text states in terms that it does *not* — and *could* not — cover the PAES items, figures and answer keys, whose rights belong to **DEMRE, Universidad de Chile**; that material is included from freely published official sources for educational use with attribution. **`P787-3` was built on this row as though the corpus were MIT. It is not** |
| **teams-facultad-mcp** | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | MIT · `1,088 B` · `17b51f4db2b0` | `0` | LATAM | Local MCP server over Teams Educación — coursework, announcements, documents |
| **Tlamatini** `NEW` | [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) | MIT · `1,062 B` · `b1f06f7e736f` | `15` | LATAM | Speak an idea, build the real thing: voice-driven AI into code, 3D worlds and hardware. 🔵 **`Tlamatini` is Nahuatl for *one who knows*** — named in an Indigenous Mexican language, which is why no English query reaches it |
| 🟢 **bncc-lesson-generator** `NEW` | [`iagommendes/bncc-lesson-generator`](https://github.com/iagommendes/bncc-lesson-generator) | 🟢 MIT · `1,068 B` · `171e1db7278e` | `0` | LATAM 🇧🇷 | 🟢 **BRAZIL PLACED FOR THE FIRST TIME, and against the country's brand-new national framework.** Open-source lesson-plan generator aligned to the **BNCC**: the teacher fills an ordinary form, the system assembles the pedagogical prompt behind the scenes and returns a structured A4/PDF plan. **"Zero-prompt para o professor"** — the teacher never writes a prompt, which is the single biggest adoption barrier `T876` names. Next.js + TypeScript; the public demo runs on mocked data, real generation needs your own key |
| 🟢 **mi_icfes** `NEW` | [`jolicastrog/mi_icfes`](https://github.com/jolicastrog/mi_icfes) | 🟢 MIT · `1,068 B` · `1c05d19ed1d3` | `0` | LATAM 🇨🇴 | 🟢 **COLOMBIA PLACED FOR THE FIRST TIME.** PWA that **predicts** a **Saber 11** result. ⚠️ **Read the use before the grant:** predicting a student's state-examination outcome is score *prediction*, not tutoring — under the EU AI Act this shape is Annex III high-risk, and it is the one LATAM row in this base that a North American or EMEA client could not simply re-deploy |
| 🟢 **awesome-ia-sala-de-aula** `NEW` | [`ciro-maciel/awesome-ia-sala-de-aula`](https://github.com/ciro-maciel/awesome-ia-sala-de-aula) | 🟢 **CC0-1.0** · `7,049 B` · `be5467501439` | `0` | LATAM 🇧🇷 | Curated register of classroom AI assistants **with each one's minimum age and privacy posture, and the Brazilian education rules that apply**. 🟢 **CC0 is a new licence family for this base and the most permissive grant it holds** — a public-domain dedication, no attribution condition at all. 🔵 Its subject matter is exactly `P790-1`'s compliance input |
| 🔴 **GenPrompt-Pre-ICFES-11** `NEW` | [`CREARED-EDU-CO/GenPrompt-Pre-ICFES-11`](https://github.com/CREARED-EDU-CO/GenPrompt-Pre-ICFES-11) | 🔴 **AGPL-3.0** · `34,523 B` · `1ca3134446d7` | `4` | LATAM 🇨🇴 | Generator producing thousands of distinct Pre-**ICFES** grade-11 prompts — **the highest-starred Colombian education-AI repository measured**. 🔴 **Copyleft, and network use triggers disclosure:** reference or separately-deployed service only, never embedded in a client deliverable |

## 🟡 The largest permissive education-agent repository set this base has met — and what it actually contains

| Address | Grant, on the bytes | Measured | Verdict |
|---|---|---|---|
| 🟡 **education-ai-ecosystem** `NEW` | [`jinlize-tech/education-ai-ecosystem`](https://github.com/jinlize-tech/education-ai-ecosystem) | 🟢 **Apache-2.0** · `11,358 B` · `b59ceae4181d` · licence sha `cfc7749b96f6` | **`132` repositories in the org; `100` of `100` sampled are Apache-2.0** | 🟡 **Real grant, real scale, and by its OWN README mostly unbuilt** |
| 🟡 **edu-ai-usage-policy-agent** `NEW` | [`jinlize-tech/edu-ai-usage-policy-agent`](https://github.com/jinlize-tech/edu-ai-usage-policy-agent) | 🟢 **Apache-2.0** · `11,358 B` · `dab9f0cd5a3c` · **identical licence sha `cfc7749b96f6`** | — | 🟢 The one member most relevant here: an **AI-usage-policy** agent, which is the artefact every regulated engagement in `intel/market.md` needs |

🟢 **The claim checked out and the honesty is the finding.** The hub declares **`130` products — `97`
Skills and `33` Agents**, each in its own repository, all Apache-2.0. `search/repositories` returns
**`132`** repositories for the owner and **`100` of `100`** sampled carry Apache-2.0, so *the
licensing claim is true at scale* — this is, by a wide margin, the largest permissively-granted
education-agent repository set this base has ever measured.

🔴 **And its own README states what it has not got:** `WorkBuddy platform validation: 0/130,
NOT_EXECUTED` · `GitHub Release verified: 30/130` · *"They do not prove WorkBuddy parsing,
installation, model behavior, review, or publication."* Sampled agent repositories are described
`Agent | … | Planned / 待研发` — **planned / to be developed.** The agents are organised by business
centre (招生营销 admissions-marketing, 教学教研 teaching-research, 教务运营 academic-operations,
财务运营 finance, 人力组织 HR, 校区标准化 multi-campus standardisation).

🔵 **So it is placed as `2` rows with a measured org count, not as `33` agents (`T878`).** Writing
"`33` education agents, Apache-2.0" would have been the single largest padding event available to
this base this pass, and the repository itself supplies the refutation. 🟢 **What it is genuinely
worth:** a **product taxonomy for the education back office** — the `8`-centre decomposition is
reusable intelligence even where the code is not, and `edu-ai-usage-policy-agent` addresses a need
`P790-1` has to meet anyway.

## Agent-adjacent infrastructure this base composes with

| Component | Address | Grant, on the bytes | ★ | Region | Role |
|---|---|---|---|---|---|
| **brightspace-d2l-mcp** `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 MCP server over **D2L Brightspace** — the third major North American LMS, and until now the only one this base had no attachment point for. Rescued from the bespoke bucket this pass |
| **xapi-service** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **xAPI learning-record service, MIT — rescued from this base's ungranted class.** This base called its Caliper/QTI/xAPI cluster "its most dead cluster"; the live, permissive half of it was filed as an absence |
| **xapi-validation** `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | **MIT** · `1,070 B` · `13ffff748515` | — | Global | xAPI statement validation — the evidence layer under any audit-trail claim |
| **mcp-regulated-ai-compliance** | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | Apache-2.0 · `12,227 B` · `72e4b0734bcc` | — | Global | MCP compliance layer — Art. 27 FRIA evidence for every regulated-deployment recipe here |
| **collect** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | ODK Collect — offline mobile data collection. The field-survey instrument for a readiness diagnostic where connectivity fails |
| **ai-agents-for-beginners** | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | MIT · `1,141 B` · `4bcf574c06d3` | — | Global | 18-lesson agent course. Curriculum, not a runtime — the fastest onboarding path for a studio squad |
| **annotated_deep_learning_paper_implementations** `NEW` | [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT** · `1,082 B` · `db59a04a8a2c` | — | Global | Annotated implementations of DL papers — rescued from the ungranted class; a teaching corpus under a permissive grant |

## Dependency grants — `ACTION p787-D` discharged, and it is this pass's headline

🔴 **A repository-level grant describes one file. It does not describe what the project pulls in.**
Direct dependencies were read from each project's own manifest and each dependency's grant from the
npm or PyPI registry (`ingest/p788-dep-audit`). 🔵 **Transitive dependencies were NOT audited** —
this is the first layer only, and the first layer was already enough to change four rows.

| Repo | Repo grant | Direct deps | Copyleft found | Verdict |
|---|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `171` | 🔴 **`angular-shepherd` — AGPL-3.0** | 🔴 **The most serious finding of the pass.** This base lists Oppia under *"build on these, link them, **ship them in client code**"*. An **AGPL-3.0** dependency in a browser-delivered bundle is the hardest copyleft there is, and network delivery is its trigger. **Remove or replace `angular-shepherd` before Oppia goes into a client deliverable** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `32` | 🔴 `zeroconf-py2compat` (LGPL-2), `json-schema-validator` (LGPL) | 🟡 This base's *"most valuable permissive row"* carries **two** LGPL dependencies. 🟢 **LGPL tolerates dynamic linking**, which is how Python imports work, so Kolibri stays usable — but the components must remain replaceable and their source available. **Not the unqualified MIT story the base has been telling** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `27` | 🔴 `pyte` — LGPL-3.0 | 🟡 The sector's **#1 agent at `58,508★`** carries a copyleft dependency. `pyte` is a terminal emulator — likely droppable. **Check whether the tutoring path needs it at all** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT | `181` | 🔴 `mathml2omml` (LGPL-3.0-or-later); 🟡 `jszip` (`MIT OR GPL-3.0-or-later`) | 🟡 `p787` found `mathml2omml` as a bundled workspace package; it is **also a declared dependency**. 🔵 **`jszip` is NEW and is dual-licensed** — a dual grant is permissive only if you **elect** the MIT arm, in writing, on the record |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | `43` | 🟢 **none** | 🟢 **Clean.** One unresolvable private scope (`@common/global-config`) is unpublished, not unlicensed |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 | `18` | 🟢 **none** | 🟢 **Clean — and this is the component that anchors `P788-1`, the flagship grading pattern.** The one row a regulated deliverable most depends on is the one that audits cleanest |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | `1` | 🟢 **none** | 🟢 Clean |

🟢 **The number to carry into a client conversation: 4 of 7.** Four of the seven highest-star
permissive education repositories carry copyleft in their **declared direct dependencies**, and in
every case the repository's own `LICENSE` file says nothing about it. 🔵 **The two that audit clean
— `nbgrader` and `OATutor` — are the two this base's grading pattern already rests on**, which is
luck rather than design, and is now on the record as a reason to keep resting on them.

## 🔴 CORRECTION TO THIS BASE — `Kosudo/nextSIS` is NOT proprietary (`p790`)

🔴 **This base published, at `p787-B` and again at `p789`: *"PROPRIETARY, newly measured … a
`39,890 B` licence file is not evidence of an open grant — it is evidence of a long one."* That
verdict is FALSE, and the reasoning that produced it is the thing worth keeping.**

🟢 **Measured this pass.** The address is alive at `60e422c7d93e` — **the exact sha this base
recorded**, so nothing moved. Its grant is served at **`license.txt`** (lowercase, `.txt`), which is
why `p789`'s `11`-path probe reported `NO-GRANT-SERVED` and mine did too until the tree was
enumerated. The file is `39,890 B` · `cd7a49230f22`, and it is a **licence anthology** with a table
of contents:

| § | Contents | Whose terms |
|---|---|---|
| 1 | Overview | nextSIS |
| 2 | **nextSIS GNU General Public License Version 3** | 🟢 **nextSIS's own grant — full operative GPL-3.0 text, `Version 3, 29 June 2007`, `5 ×` `TERMS AND CONDITIONS`** |
| 3 | CodeIgniter License | EllisLab, Inc. (bundled framework) |
| 4 | Twitter Bootstrap License | Bootstrap (bundled front end) |

🔴 **The single `All rights reserved.` in the file is at line `703`. It is the second line of §3 —
`Copyright (c) 2008 - 2011, EllisLab, Inc.` — and EllisLab's very next clause reads `You are
permitted to use, copy, modify, and distribute the Software`.** So the line this base graded on
does not belong to nextSIS, **and the licence it does belong to is not proprietary either.** The
verdict was wrong twice over on one line.

🟢 **Corrected verdict: `Kosudo/nextSIS` is `GPL-3.0`** — a named, open-source Student Information
System. 🔴 **Copyleft, so it is flagged, not cleared:** deploy it as a separate system and integrate
at its boundary; **never embed it in a proprietary client deliverable.** 🟢 **But it moves from
`barred` to `usable-with-care`, and it is the only open SIS this base holds** — against `T852`'s
point that the famous names are copyleft, this is one more confirmation, not an exception.

🔵 **Why this is a method change and not an erratum (`T875`):** my own instrument graded the same
file **`AGPL-3.0`**, because GPL-3.0's §13 *names* the GNU Affero GPL, and it fired the NonCommercial
bar, because GPL-3.0 §6 *uses the word* "noncommercial". **Three different probes, three different
wrong answers, one cause: a licence file that quotes other licences cannot be graded by substring
presence.** The grader now matches **anchored title lines** and reports a **set**, and `nextSIS`
reads `ANTHOLOGY[GPL-3.0, +CodeIgniter]`. This is the same defect class as `metabase`'s
split-by-directory finding, **split by section instead.**

## 🔴 Probed this pass and NOT usable

| Address | Finding | Why it is barred |
|---|---|---|
| [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | ALIVE · `aa476a6a6a03` · `1,296 B` bespoke | 🔴 **PROPRIETARY**, now graded rather than left `UNGRADED`. Source-available multi-agent learning OS |
| [`metabase/metabase`](https://github.com/metabase/metabase) | ALIVE · `6006cc9c65dd` · `855 B` | 🔴 **SPLIT BY DIRECTORY, not one licence.** AGPL-3.0 outside `enterprise/`, **Metabase Commercial License** inside it. 🟢 Reporting one family for this repo would be the error; the boundary is the fact. Same shape as `764-C` |
| [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) | ALIVE · `9ed32d5c2577` · `362 B` | 🔴 **CORRECTION — this base's published reason was WRONG.** `p786` recorded *"a file named `LICENSE` containing a Latin boast and no grant of any kind"*. The Latin boast is line 1; **lines 3–5 grant CC BY-NC-SA 4.0, in Spanish, with a link to the Spanish legal code**, and a scope clause excluding the downloaded BOE/BOC statutory texts. Still barred commercially — but **NonCommercial is a harder bar than an absence, and the stated reason was false** (`T863`) |
| [`cosark/OpenTutor`](https://github.com/cosark/OpenTutor) | ALIVE · MIT · fork of `zijinz456/OpenTutor` at `0★` | 🔴 **Not a distinct project** |
| [`gabrielmahia/shule-ai`](https://github.com/gabrielmahia/shule-ai) | ALIVE · `01d074b6aaf3` · **`209 B` · `9dd285c3704d`** | 🔴 **`CC BY-NC-ND 4.0` — NonCommercial AND NoDerivatives.** Kenya's CBC/KCSE tutor answering in Kiswahili. **Barred twice: not in a paid engagement, and not modifiable at all.** 🔵 Indexed `NOASSERTION` by the search channel |
| [`Bestisco/My-WASSCE-Companion`](https://github.com/Bestisco/My-WASSCE-Companion) · [`Elite2828/ACE-AI-Tutor`](https://github.com/Elite2828/ACE-AI-Tutor) | 🔴 **DEAD — `git ls-remote` `rc=2`, re-probed and confirmed** | 🔴 **Returned by the search channel this pass and gone from the byte channel.** `2` of the `5` Ghanaian addresses probed. 🔵 A search result is a claim; `rc` is the fact |
| [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) ≡ [`NikolasSchaeffner/lehrer-agent`](https://github.com/NikolasSchaeffner/lehrer-agent) | Both ALIVE · **identical `HEAD` `3ddcfbbabc56`** · neither serves a licence | 🔴 **ONE German teacher agent, carried by this base as TWO ungranted rows.** 🟢 **`ACTION p787-G` discharged mechanically (`T865`):** `p787` said only a page read could separate a fork from a project. **Identical `HEAD` sha proves it on the byte channel**, and the page channel is `403` this pass |
| [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) | ALIVE · `212cb10e48eb` · no licence on 10 filenames × 3 branches | 🔴 Japan's best education-AI artefact, **ungranted**. An upstream licence request, not a permanent exclusion |
| [`silja-graf/Didaktikus-…-LP21`](https://github.com/silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21) | ALIVE · `8d747cda689e` · no licence | 🔴 A **Swiss LP21-curriculum** lesson-planning and assessment agent — the single most engagement-shaped EMEA artefact found, and ungranted. 🔵 **Ask for this one** |
| [`RAFCERAY/horizonia`](https://github.com/RAFCERAY/horizonia) · [`redoneabouaali-lab/najih`](https://github.com/redoneabouaali-lab/najih) · [`MRiARC/VidyaSetu`](https://github.com/MRiARC/VidyaSetu) · [`TaoYu-ds/TutorMesh`](https://github.com/TaoYu-ds/TutorMesh) · [`kaikai52125/NeoTutor`](https://github.com/kaikai52125/NeoTutor) · [`SoukhyadP991/Multilingual-NCERT-Doubt-Solver`](https://github.com/SoukhyadP991/Multilingual-NCERT-Doubt-Solver) · [`mingxuanyan07-lgtm/ai-for-education-showcase`](https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase) | all ALIVE · none serving a licence | 🔴 **7 further ungranted agents, placed by region so the absence is useful:** FR, Morocco, IN, CN, CN (a DeepTutor re-implementation on LangGraph), IN (offline NCERT doubt-solver), CN (auditable multi-agent maths teaching). 🟢 These are **licence requests**, and three of them are the best artefact found for their country |

## Counts for this pass

| | Count |
|---|---|
| Agents and components listed with a byte-verified grant | **75** (was 62) |
| of which **permissive** (MIT · Apache-2.0 · ECL-2.0 · BSD · BSL-1.0 · **CC0-1.0** · CC BY 4.0 content) | **69** |
| of which copyleft, flagged | **8** (`learnharness` AGPL-3.0, `OpenVidya` AGPL-3.0, `GenPrompt-Pre-ICFES-11` AGPL-3.0, `NCERT-AI-Teacher-Assistant` GPL-3.0, **`nextSIS` GPL-3.0 — corrected from "proprietary" this pass**, `frappe/lms` AGPL-3.0, `news-grade-reader` GPL-3.0, `frametell` AGPL-3.0) |
| 🟢 **NEW to this base this pass** | **13** |
| Placed **LATAM** | **9** (was 5) — 🟢 **🇧🇷 Brazil and 🇨🇴 Colombia placed for the first time** |
| Placed **APAC** | **17** (6 India · 2 Korea · 5 China · 3 Japan · **1 Malaysia**) — 🟢 **Malaysia placed, `p789` gap discharged** |
| Placed **EMEA** | **20** (7 agents + 7 `elimu-ai` + 5 Africa + 1 🇬🇧) |
| Placed **North America** | **4** |
| Placed **Global** | **21** |
| Probed and rejected | **25** (1 split-by-directory, **3** NonCommercial — one of them also NoDerivatives, 1 fork, 1 duplicate address pair, **17** ungranted, **2 DEAD**) · 🟢 **`1` row LEFT this bucket: `nextSIS`** |
| 🔴 Rows whose published verdict this pass CORRECTED | **1** — [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS), **proprietary → GPL-3.0**, on a licence *anthology* graded by one line belonging to a bundled dependency |
| 🔴 Defects found in this pass's OWN instruments, by controls, before publication | **7** — `0` found by inspection |
| 🟢 Controls reproduced exactly before any verdict shipped | **10 of 10** known-good rows · `3` planted negatives DEAD as designed |

### Where the three declared gaps of `p789` stand

| `p789` gap | `p790` disposition |
|---|---|
| 🇲🇾 **Malaysia** (`1`, ungranted) | 🟢 **DISCHARGED** — `haziqhalifi/StudyLah`, MIT, SPM Form 5 mathematics in Bahasa Malaysia |
| 🇬🇭 **Ghana** (`1`, ungranted) | 🔴 **NOT discharged, and RE-MEASURED at `11` repositories with `0` grants** — `p789` understated the supply ~`10×` and read the grant rate correctly. `2` of `5` probed addresses are DEAD |
| 🇹🇿 **Tanzania** (`0`) | 🔴 **NOT discharged.** `2` repositories exist; the only granted one (MIT) is **veterinary extension education**, not school education — a category error in the opposite direction from Japan's (`T877`) |

🟢 **The honest summary of this pass: `1` region placed, `1` region placed for two countries, `2`
regions measured and still empty, and `1` of this base's own published verdicts reversed.** 🔴 **The
reversal is the most valuable item**, because the instrument that produced it — grading a licence
file by substring presence — is still in use everywhere else licence files are read, and three
independent probes got three different wrong answers from the same file.

🔵 **The thinnest regions are now Tanzania (`0` school-education agents, measured), Ghana (`11`
repositories, `0` grants) and Kenya (`3` repositories, `0` usable grants — one barred `NC-ND`).** All
three are measured; none is inferred; and all three have the same remedy, which is a licence request
rather than an engineering task.
