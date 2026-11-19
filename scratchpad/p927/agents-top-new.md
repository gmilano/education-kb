## The topic vocabulary, asked thirty-five more ways — 21 rows, added `p927`

🟢 **Why this section exists, and what it retires.** `p925` opened GitHub's **topic** index and
shelved 19 rows. `p926` re-ran `p925`'s legs, found them near-empty, asked thirteen words `p925`
never used and returned **601 unheld** repositories — then wrote `926-R1`: *a discovery channel is
exhausted only against the vocabulary it was asked with.* `p927` asked **35 more words**:
**2,298 unheld repositories**, deduplicated against the **8,432** slugs this base has ever named.
🔴 **Fifteen of the 35 legs reported a `total_count` larger than the 100-row page this base
fetches** — `topic:student-management` **1,651**, `topic:ai-tutor` **986**, `topic:study-tools`
**817** — so **2,298 is a floor and not a measurement.** Full yields:
`evidence/topic-vocabulary-yield.2026-11-19-p927.tsv`.

**Method.** `gh api search/repositories` for discovery; every row below then had its licence file
fetched from `raw.githubusercontent.com` across **14 probed paths** and the **grant text read**,
with byte size and `sha256₁₂` recorded. **36 probed, 36 resolved, 0 404s**
(`evidence/grant-byte-read.2026-11-19-p927.tsv`). Stars as at **2026-11-19**.

🟡 **Read the star column before you read anything else in this section.** Most of these rows are
0–10 ★ and weeks old. They are shelved because of **what they demonstrate**, not because they are
dependencies: three of them are the first compliant proctoring designs this base has seen, four
correct a regional claim this base published as fact, and one is the most permissive grant it has
ever recorded. **Treat them as reference designs and build-vs-buy evidence, not as a supply chain.**

### 🟢 `927-F4` Proctoring, local-first — the category this base called unadoptable

This base records proctoring as *"an **unadoptable** category — six open tools, the largest at 16 ★
and dormant since 2025, against an EU prohibition on emotion inference in force since 2 February
2025."* `topic:proctoring` returned **176 repositories and had never been asked.** 🔵 **The
prohibition is on emotion inference, not on video.** A browser-integrity signal that never infers
affect, and a vision pipeline whose frames never leave the candidate's machine, sit outside both
that prohibition and the privacy objection that made Canadian higher education refuse this tooling.

| Agent | Repo | Licence (byte-read) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **Local-Exam-Proctoring-Engine** | https://github.com/SHUBHJAIN139/Local-Exam-Proctoring-Engine | **MIT** (1,067 B, `91a47a93bbca`) | 0 | 2026-10-12 | 🟢 **Private, local-first, in-browser** exam proctoring: WebAssembly MediaPipe and TF.js vision running on the candidate's own machine. **No video leaves the device**, which removes the transfer that the privacy objection and most of the DPIA burden attach to. | 🔵 unplaced |
| **tinyproctorjs** | https://github.com/tanzir71/tinyproctorjs | **MIT** (1,085 B, `cc1b9d2387e8`) | 0 | 2026-11-17 | Integratable JS agent plus session dashboard for real-time **browser-integrity** monitoring — focus loss, tab switching, session state. 🟢 **It infers no affect at all**, which is the cleanest position relative to the EU prohibition of anything in this category. | 🔵 unplaced |
| **Examshield-AI** | https://github.com/Aryansh909/Examshield-AI | **MIT** (1,070 B, `75107b398587`) | 1 | 2026-08-01 | Real-time computer-vision proctoring: YOLOv8 object detection plus MediaPipe 468-point facial landmarks. 🟡 **The most capable and the most exposed of the three** — 468-point landmark tracking is the input affect inference is built from, so the compliance argument depends entirely on what is computed from it and where. Read it as the capability ceiling, and `tinyproctorjs` as the compliant floor. | 🔵 unplaced |

🔵 **What this changes for an engagement.** Proctoring moves from *"do not propose this"* to **a
build line with three reference designs and a stated compliance boundary**. It remains an EU
Annex III high-risk category; the architecture changes the privacy and emotion-inference exposure,
not the risk classification. `compose/patterns.md` **P55**.

### 🔴 `927-F5` LATAM — four permissive rows, and a correction to `926-G2`

`926-G2` measured eleven Spanish- and Portuguese-language rows in its backlog and found **none**
permissively licensed, and recommended *licensing and productising LATAM supply* on that basis. A
second vocabulary returns MIT rows with the grants byte-read. 🔵 **The finding was true of eleven
rows from one leg list and was published as a fact about a region** — the same failure `926-R1`
names, one level up. 🟢 **The corrected claim is sharper:** LATAM permissive supply exists and sits
in **institutional** software, not in general-purpose tutors, where `p904` already measured a 6 ★
ceiling. `p904`'s advice stands and its evidence is now stronger: **bring the tutor, adopt the
institutional spine.**

| Agent | Repo | Licence (byte-read) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **detector-ia** | https://github.com/alberto2005-coder/detector-ia | **MIT** (1,079 B, `d7766590a996`) | 2 | 2026-11-19 | Spanish-language detector for **AI-generated text *and* copying between submissions**, across Jupyter, PDF, DOCX, MD and TXT. 🔵 The cross-submission axis is the one most AI-detection tools omit, and it is the one an academic-integrity office actually asks for. | LATAM 🇪🇸 *(description in Spanish)* |
| **Learn-Quest** | https://github.com/DerickxP/Learn-Quest-Serious-Game | **MIT** (1,071 B, `da1aeec572db`) | 1 | 2026-10-22 | Unity/C# 2D educational game **for children with Down syndrome**, with OpenAI and speech recognition. 🟢 First accessibility-first row in this table, and the first serious game. | LATAM 🇧🇷 *(description in Portuguese)* |
| **KodlandFaster** | https://github.com/Gehiner/KodlandFaster | **MIT** (1,064 B, `61c63d0a04e1`) | 1 | 2026-10-06 | Chrome extension plus Python tooling that automates **tutor back-office** work. 🔵 The only row here aimed at the *operator* of tutoring rather than the learner. | LATAM 🇪🇸 *(description in Spanish)* |
| **harpia** | https://github.com/uemanet/harpia | **MIT** (1,063 B, `afa9cfe1dcb6`) | 28 | 2026-11-15 | 🟢 **The academic system of Universidade Estadual do Maranhão**, a Brazilian **state** university — open since 2017-12-21, still pushed. Full row in `verticals/solutions.md`; listed here because it is the evidence that carries `927-F5`. | LATAM 🇧🇷 |

### 🟢 Agent tier — the rest of the shelf

| Agent | Repo | Licence (byte-read) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **Smart-Quiz-Tutor** | https://github.com/xxinjie21/Smart-Quiz-Tutor | 🟢 **0BSD** (664 B, `2cb3ff984068`) | 10 | 2026-09-22 | AI quiz generation, **SM-2 spaced repetition**, wrong-answer tracking. 🟢 **First `0BSD` row in this base.** Zero-Clause BSD is public-domain-equivalent — **no attribution requirement at all**, the most permissive grant recorded here and the one class where `924-F1`'s *"grade on the clause"* warning cannot bite, because there are no clauses. | 🔵 unplaced |
| **geogebra-mcp** | https://github.com/haison8x/geogebra-mcp | **MIT** (1,065 B, `32508be1d078`) | 1 | 2026-10-20 | **MCP server** that lets an agent draw, check and fix **plane-geometry figures** live in GeoGebra. 🟢 The first row in this base where the agent's tool is a *construction* the learner can see, rather than text — and GeoGebra is already deployed in most EMEA and LATAM maths classrooms. | 🔵 unplaced |
| **mathos-webmcp** | https://github.com/fireheartjerry/mathos-webmcp | **MIT** (1,075 B, `2388ed41fa64`) | 0 | 2026-09-04 | A **shared live maths canvas** where learner and AI tutor edit the same objects, over **WebMCP**. 🔵 Pairs with `geogebra-mcp` as the two halves of a manipulable-maths seam; both MIT. | 🔵 unplaced |
| **self\_regulated\_learning\_copilot** | https://github.com/devissaputra/self_regulated_learning_copilot | **MIT** (1,076 B, `c10726bddc58`) | 2 | 2026-09-26 | **Agency-preserving** copilot for planning, monitoring and strategy adaptation — it coaches the learner's *process* and declines to do the task. 🟢 The design answer to the `little-socrates` problem this base has recorded: a tutor that solves the homework has taught nothing. | APAC 🇮🇩 *(author name and framing)* |
| **learning-methodologies** | https://github.com/siberius/learning-methodologies | **MIT** (1,072 B, `55b44f528c81`) | 4 | 2026-11-14 | Agent skill for **designing** educational apps: connects learning goals to activities, scaffolding and assessment. 🔵 Instructional design as a reusable artefact rather than as consultant knowledge. | 🔵 unplaced |
| **elifba** | https://github.com/nijataliyev7/elifba | **MIT** (1,069 B, `c79aae99a979`) | 2 | 2026-11-19 | Learn to read **Azerbaijani** through letter, syllable, word and sentence games, built for classroom use. 🟢 **First Azerbaijan-origin row in this base**, and the second early-literacy row after `elimu-ai`. | EMEA 🇦🇿 |
| **daskal.ai** | https://github.com/angel-georgiev/daskal.ai | **MIT** (1,071 B, `394e9f40c94d`) | 0 | 2026-11-13 | *Даскал AI* — assistant for the **Bulgarian** teacher: annual plans and lesson preparation in Bulgarian. 🟢 **First Bulgaria-origin row.** Joins the vernacular-teacher-preparation cohort with China and France. | EMEA 🇧🇬 |
| **MathDesk** | https://github.com/orangewk/MathDesk-snapshot | **MIT** (1,065 B, `92511e2244a8`) | 0 | 2026-06-01 | Open-source edition of an AI maths tutoring system **for Japanese high-school students**. 🟢 **First Japan-origin agent row.** `p890` confirmed Japan has no education-specific AI regime; this is the first supply-side evidence from the same market. | APAC 🇯🇵 |
| **exam-deep-seek** | https://github.com/WDMoonMoonBird/exam-deep-seek | **MIT** (1,089 B, `ebd20e036a20`) | 1 | 2026-11-02 | AI judging platform for **computer-science coursework**: automatic objective-question scoring and code-question assessment. | APAC 🇨🇳 *(description in Chinese)* |
| **BestTeach** | https://github.com/deeding2030-boop/bestteach-public | **MIT** (1,159 B, `3fae65c81ef1`) | 0 | 2026-05-26 | 贝特教 — lesson-preparation assistant for **Chinese K-12 teachers**, built on DeepSeek. 🔵 Joins `T11`'s teacher-capacity tier: the binding constraint in every statutory AI-literacy market is teacher time, not technology. | APAC 🇨🇳 |
| **autograder-py** | https://github.com/Apurba94/autograder-py | **MIT** (1,071 B, `2d870f5fb212`) | 0 | 2026-11-04 | Grades Python assignments in **isolated runs with resource limits**, hidden tests and partial marks. 🔵 Complements `nbgrader` and `otter-grader` in `repos/foundations.md` by being the one that assumes **no platform at all**. | 🔵 unplaced |
| **privacy-preserving-educational-telemetry** | https://github.com/CarlosEkRaigoza/privacy-preserving-educational-telemetry | **MIT** (1,117 B, `760d2ca71ae9`) | 0 | 2026-11-04 | Reference implementation of a **modular privacy-preserving telemetry architecture** for education. 🟢 **The only artefact in this base that treats learning analytics as a privacy-engineering problem with a published design** — directly addressable to **California AB 1159**, which bars training models on student data outright. | 🔵 unplaced |
| **openbridge** | https://github.com/JaneKoch/openbridge | **MIT** (1,080 B, `caa5e03bca02`) | 0 | 2026-11-19 | Open-source AI **reading tutor** with adaptive stories. 🟡 Created and pushed the day it was measured; shelved as a dated observation, not a recommendation. | 🔵 unplaced |
| **ReadU** | https://github.com/willfeldman/readu | **MIT** (1,069 B, `8fe5f43417ff`) | 0 | 2026-06-13 | Adaptive AI **reading comprehension** for middle schoolers, personalised by skill and interest. 🔵 With `openbridge` and `elifba`, reading is now the best-covered subject on this shelf after maths. | 🔵 unplaced |
| **faq-assistant** | https://github.com/uloya1234/faq-assistant | 🟡 **MPL-2.0** (16,726 B, `3f3d9e0024b1`) | 4 | 2026-07-30 | Local AI FAQ assistant running **entirely in the browser** via WebGPU and Transformers.js. 🟡 **File-level copyleft**: modifications to MPL files must be published, but it can be combined with proprietary code in a larger work. Usable in a closed deliverable **if the MPL files stay separable** — which is a build-system constraint, not a licence table entry. | 🔵 unplaced |

### 🔴 `927-F3` Correction to a published row — `CAHLR/OATutor`'s problem banks are a separate, unlicensed repository

This file publishes **`CAHLR/OATutor`** (MIT, byte-read `1,105 B`, 283 ★, **UC Berkeley CAHLR**) as
an *"Intelligent tutoring system with **open problem banks**"*. **The problem banks are not in that
repository.** They are in **`CAHLR/OATutor-Content`** (9 ★, pushed 2026-11-13), and:

- 🔴 **No licence file on 14 probed paths**, and the search channel reports `NONE` — so the two
  channels **agree**, and no divergence check flags it.
- The grant exists **only as prose in the README**, byte-read this pass: *"All content in this
  repository is made available under the Creative Commons Attribution 4.0 International (CC BY 4.0)
  license. Attribution is given within each json file, indicating the authoring organization and
  license for each hint, scaffold, and problem."*
- So it is **not one grant**. The content is curated from **OpenStax** plus classroom syllabi across
  seven textbooks, and the README says the operative licence is recorded **per record**.

🟡 **The MIT code row stands** — `CAHLR/OATutor-Tooling` is MIT on the same byte-read, and CC BY 4.0
is permissive and attribution-only, so the content **is** usable. What changes is the delivery
obligation: **attribution is per hint, per scaffold and per problem**, which a studio has to build
for rather than record in a licence column. Probe:
`evidence/oatutor-content-licence-probe.2026-11-19-p927.tsv`. Gate: `compose/patterns.md`
**`927-G1`**, which extends `904-G1` from *probe the payload directory* to **probe the payload
repository, and read the README when there is no licence file.**

### 🔵 `927-G2` What the mandated legs returned

**Four prose legs, 0 unheld education repositories — the forty-sixth consecutive nil.** The only
repository they named that could plausibly have been unheld,
`GarethManning/education-agent-skills` (1,005 ★), **is already in this table**, and its grant was
re-byte-read this pass: unchanged at **CC BY-SA 4.0, `1,230 B`**, first line *"Creative Commons
Attribution-ShareAlike 4.0 International"*. The **vertical leg returned the OpenEduCat marketing
site for the fourth consecutive pass** and should not be re-run as written. The four **regional**
legs returned 0 unheld repositories but non-trivial new policy and adoption intel, written into
`intel/market.md`. `evidence/websearch-legs.2026-11-19-p927.tsv`.

