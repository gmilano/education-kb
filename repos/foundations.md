---
industry: education
region: Global
updated: 2026-10-19
---

## 🟢 Pass 305 — THE DEFAULT BRANCH IS NOW READ RATHER THAN GUESSED, WHICH RETIRES A WHOLE CLASS OF FALSE ABSENCE FROM THIS FILE

⏱️ **Pass 305 of `2026-10-19`.** Evidence:
[`p305-channel-calibration.2026-10-19-p305.tsv`](../evidence/p305-channel-calibration.2026-10-19-p305.tsv) ·
[`p305-licence-payload.2026-10-19-p305.tsv`](../evidence/p305-licence-payload.2026-10-19-p305.tsv) ·
[`p305-topic-census.2026-10-19-p305.tsv`](../evidence/p305-topic-census.2026-10-19-p305.tsv).

🟢 **`p304` recorded that this environment yields no repository metadata: `curl` on a `github.com` repo path
returns `403` for every slug including a fabricated control, and `api.github.com` is an authorization
boundary. 🟢 Both CONFIRMED against the same control. 🟢 But a third channel works, and `p304` did not have
it: `git ls-remote --symref` returns existence AND the default branch.**

| channel | control that cannot exist | real slug | discriminates | yields |
|---|---|---|---|---|
| `curl https://github.com/{slug}` | `403` | `403` | 🔴 **NO** | nothing |
| `curl https://api.github.com/repos/{slug}` | `403` | `403` | 🔴 **NO** | nothing |
| `raw.githubusercontent.com/{slug}/{br}/LICENSE` | `404` | `200` | 🟢 YES | the licence **payload** |
| 🟢 **`git ls-remote --symref {url} HEAD`** | **credential prompt** — `p293`: a MEASUREMENT, not an inconclusive result | `sha` + `ref: refs/heads/{br}` | 🟢 **YES** | 🟢 **existence AND DEFAULT BRANCH** |

🔴 **Why this matters to a foundations file more than to any other shelf: substrate repositories are old,
and old repositories do not publish on `main`.** `p303`'s ladder cost **6 filenames × 3 branches = 18
probes** per slug and still could only find a branch it had guessed. 🟢 **`p305` pays 1 `ls-remote` + ≤6
raw probes on the ONE correct branch — fewer requests AND strictly more coverage.**

🔴 **Two branches this pass prove it is not theoretical:**

| repo | default branch | would a `main`/`master`/`dev` ladder find it? |
|---|---|---|
| [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | **`dev`** | 🟡 Yes, but only on the third try |
| [`im-rk/SkillTrace`](https://github.com/im-rk/SkillTrace) | 🔴 **`development`** | 🔴 **NO — the branch is not in the ladder at all** |

⚠️ **A ladder would have published `NO_PAYLOAD` for `SkillTrace` — a FALSE ABSENCE on a branch it never
asked for.** 🟢 **That is the failure mode this base polices hardest (`gate-absence`, `ACTION p275`), and it
was reachable by construction until this pass.** 🔵 **Standing recommendation: read the branch before
probing the payload, always.**

### 🟢 New permissive foundations rows, every grant read as a payload

| Repo | Licencia | bytes · sha256₁₂ | branch | Por qué es foundational | ★ |
|------|----------|---|---|------------------------|---|
| [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | **Apache-2.0** | 10 785 · `65125d9e480b` | `dev` | AI-driven personalised student feedback, built and run by **TH Mittelhessen**. 🟢 **Institutional provenance + Apache-2.0 + EMEA placement — the combination this file has been short of.** Feedback-at-scale is the workflow every LMS engagement hits first | 24 |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | 1 073 · `1e05c9440068` | `main` | 🟢 **The composition point for this whole vertical.** An MCP server turning any LLM into an ITS — so tracing, scheduling and content layers sit behind ONE interface an agent host already speaks. **This is the row that makes `P84` assemblable** | 51 |
| [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 7 048 · `a2010f343487` | `main` | WWW '25 multi-agent framework for goal-oriented learning. 🟢 **CC0 is a public-domain dedication — MORE permissive than MIT, with no attribution condition — so it is the one row that cannot contaminate anything it is combined with.** See `P85` Zone B | 135 |
| [sohan1611/BloodCoded_Agentic](https://github.com/sohan1611/BloodCoded_Agentic) | **MIT** | 1 104 · `4b15a1e898b3` | `main` | 🟢 **Three layers in one small repository: LangGraph orchestration + Bayesian knowledge tracing + a prerequisite DAG.** At 2★ it is immature, but it is the only row on these shelves that wires all three together — read it as a reference architecture | 2 |
| [bydeng01/ability-levels-audit](https://github.com/bydeng01/ability-levels-audit) | **MIT** | 1 154 · `fef00f185287` | `master` | 🟢 **Pre-registered LLM-judge audit of ability-level assignment, shipped WITH frozen data.** Pre-registration + frozen data is what turns a mastery claim into an auditable one | 4 |
| [bydeng01/conv-vs-ped-tutor](https://github.com/bydeng01/conv-vs-ped-tutor) | **MIT** | 1 150 · `a1c6b65c5bb1` | `main` | 🟢 **The control for the withholding-pedagogy cluster** `p303` found convergent across four implementations — audits tutor helpfulness against **answer leakage**. A cascade is unfalsifiable without exactly this | 3 |
| [ocala/peolatsi](https://github.com/ocala/peolatsi) | **Apache-2.0** | 11 357 · `c71d239df917` | `master` | Electronics virtual lab monitored by CTAT-built tutoring. 🟢 **5th recurrence of the stock Apache-2.0 payload hash `p303` identified** — the hash instrument now has five confirmations | 1 |
| [khayyam-math/khayyam-math](https://github.com/khayyam-math/khayyam-math) | **MIT** | 1 079 · `4068e5e09efd` | `main` | Voice-narrated maths figures from one-line prompts, with a live tutor. 🟡 Small, but the **generated-figure + narration** pairing is a reusable content primitive | 4 |

🔵 **All seven MIT/Apache payloads above fall inside `p304`'s 1 060–1 180 B band (for MIT) or match a known
stock Apache hash — the band is corroborated with seven fresh samples and keeps its use as a cheap SCREEN.**
🔴 **It is NOT a classifier: see `agents/top.md`'s 842 B reserved grant, which clears every length threshold
this base has written.** 🟢 **The deciding test is the PERMISSION CLAUSE** → `P83`.

### 🔴 Refused for this file, with the reason

- 🔴 **[`ShuyunYuan/talentcoach`](https://github.com/ShuyunYuan/talentcoach)** — **RESERVED GRANT**, 842 B
  `76d0b7213617`. *"All rights reserved… portfolio and code-review purposes only."* **Refutes `p304`'s
  `bytes < 400` rule.**
- 🔴 **[`tianshuo/trainingllm`](https://github.com/tianshuo/trainingllm)** — **PHANTOM GRANT**: README
  `## License / MIT`, no file on `main`. **Third instance of `p303`'s class in three passes.**
- 🔴 **[`mskljns/ComprehensionProblems_DAiSEE`](https://github.com/mskljns/ComprehensionProblems_DAiSEE)** —
  ungranted, **and a prohibited practice** under EU AI Act Art 5(1)(f) (in force since `2025-02-02`).
  ⚠️ **Its MIT sibling is refused for the same second reason despite a clean grant** → `P84`.
- 🔴 **[`JustinoLM/STI-matematicas`](https://github.com/JustinoLM/STI-matematicas)** — ungranted. 🟡 **The
  only row in all 41 with a stated classroom validation (74 students), LATAM-placed. Cite the result;
  reimplement the system.**
- 🔴 **11 further tail rows (ranks 21–40) ungranted** — see
  [`p305-licence-payload`](../evidence/p305-licence-payload.2026-10-19-p305.tsv).

⚠️ **`make hooks` could not be run this pass** — the environment refused the recipe as external code.
🔴 **These rows are published WITHOUT the base's 31-control gate**, and `p304` had found two gates already
RED at `HEAD`. 🟢 **Each grant above was read first-hand as a payload by an instrument calibrated 8/8 this
pass**, but the gate is an open item → `ACTION p305-R`.


## 🟢 Pass 304 — `ACTION PG-5` ITEM 3 DISCHARGED AFTER FOUR PASSES OF BEING DEFERRED, AND THE TEN CELLS PAID A NEW INSTRUMENT: FORK-TO-STAR RATIO SEPARATES THE REPOS PEOPLE *DEPLOY* FROM THE ONES THEY *READ*

⏱️ **Pass 304 of `2026-10-19`.** Evidence:
[`p304-starcells.2026-10-19-p304.tsv`](../evidence/p304-starcells.2026-10-19-p304.tsv) ·
[`p304-licence-payload.2026-10-19-p304.tsv`](../evidence/p304-licence-payload.2026-10-19-p304.tsv) ·
[`p304-reachability.2026-10-19-p304.tsv`](../evidence/p304-reachability.2026-10-19-p304.tsv).

🟢 **`ACTION PG-5` item 3 — *"the ten remaining star/forks cells, UNTOUCHED FOR A FOURTH PASS"* — is
DISCHARGED. All ten were read this pass, with forks and sidebar licence alongside.**

### 🟢 The discharge: ten cells, three moved, and the mover is the one that matters

| repo | prior | `p304` | Δ | forks | fork : star | sidebar licence |
|---|---|---|---|---|---|---|
| [`learningequality/studio`](https://github.com/learningequality/studio) | 193★ | 🟢 **213★** | 🟢 **+20** | **314** | 🟢 **1.47** | 🟢 **MIT** |
| [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | 70★ | 🟢 **76★** | 🟢 **+6** | 36 | 0.47 | 🔴 **GPL-3.0** |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 519★ | 🟢 **521★** | 🟢 **+2** | **404** | 0.78 | ⚠️ **not rendered** |
| [`uPortal-Project/uPortal`](https://github.com/uPortal-Project/uPortal) | 286★ | 286★ | — | **278** | 🟢 **0.97** | 🟢 **Apache-2.0** |
| [`hpi-schul-cloud/schulcloud-server`](https://github.com/hpi-schul-cloud/schulcloud-server) | 81★ | 81★ | — | 22 | 0.27 | ⚠️ **not rendered** |
| [`DFE-Digital/apply-for-teacher-training`](https://github.com/DFE-Digital/apply-for-teacher-training) | 38★ | 38★ | — | 11 | 0.29 | 🟢 **MIT** |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 28★ | 28★ | — | **48** | 🟢 **1.71** | 🟢 **Apache-2.0** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 1.4k★ | 1.4k★ | — | 343 | 0.25 | 🟢 **BSD-3-Clause** |
| [`numbas/Numbas`](https://github.com/numbas/Numbas) | 215★ | 215★ | — | 129 | 0.60 | 🟢 **Apache-2.0** |
| [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) | 7★ | 7★ | — | 9 | 🟢 **1.29** | ⚠️ **not rendered** |

🔵 **`p295` refuted 2 of 11 cells; `p304` moved 3 of 10 — so the prior on "a deferred star cell is stale" is
holding at roughly 25-30%, and item 3 was worth buying.** 🟢 **The mover that matters is
[`learningequality/studio`](https://github.com/learningequality/studio) at +20 (193 → 213, ~10% in the
deferral window) — MIT, and the content-authoring half of the Kolibri stack this base already carries for
offline-first deployments.** 🔵 **Growth in the authoring tool, not the player, is a signal about who is
adopting Kolibri: organisations making their own curriculum, not just serving someone else's.**

### 🟢 The instrument the discharge produced: fork-to-star ratio as a DEPLOYMENT-INTENT proxy

🟢 **Item 3 asked only for stars. Reading forks in the same request cost nothing and separated this tier
cleanly in two** — and the split is not by popularity, it is by what people DO with the repository:

| band | fork : star | rows | what the band is |
|---|---|---|---|
| 🟢 **FORKED TO DEPLOY** | **≥ 0.95** | `Ed-Fi-ODS` 1.71 · `studio` 1.47 · `OpenEMIS-Core` 1.29 · `uPortal` 0.97 | 🟢 **Administrative, data-standard and content-authoring systems.** You cannot use these without standing up your own instance, so adoption *requires* a fork |
| 🔴 **STARRED TO READ** | **≤ 0.30** | `nbgrader` 0.25 · `schulcloud-server` 0.27 · `apply-for-teacher-training` 0.29 | 🔴 **Pedagogical tools and reference services.** Bookmarked far more often than stood up |
| 🟡 middle | 0.47 – 0.78 | `Tangerine` 0.47 · `Numbas` 0.60 · `PrairieLearn` 0.78 | 🟡 Assessment tools — deployed by institutions, read by individuals |

🟢 **Why this is worth more to a studio than a star count: `Ed-Fi-ODS` has 28★ and 48 forks.** 🔵 **On stars
it is the weakest row in the table and would be cut from any shortlist. On forks it is the most
deployed-per-watcher row this base has measured** — which is exactly what you would predict of a **state
education data standard**, where every adopting agency runs its own ODS. ⚠️ **A shortlist built on stars
systematically discards the administrative tier, which is the tier most education engagements actually
begin in.**

🔵 **Stated as a rule for future passes: for substrate, read forks; for agents, read stars.** A substrate's
users are operators who fork; an agent's users are developers who bookmark. 🟡 **The ratio is a proxy and
not proof** — forks also accumulate from coursework and from abandoned PR branches, and GitHub does not
distinguish them. **Cite it as an intent signal, never as an install base.**

### 🟡 A licence-rendering gap, now measured rather than assumed

⚠️ **3 of 10 repository pages do NOT render a licence in the sidebar** — `PrairieLearn`,
`schulcloud-server` and `OpenEMIS-Core`. 🔵 **All three have a `License` link or a `LICENSE` file in the
tree; the label is simply absent from the rendered sidebar.** 🔴 **So the sidebar is unreliable at a
measured rate of 30% on this tier, and "no licence shown" must never be written down as "no licence."**
🟢 **This is precisely the case `probe_payload.sh` exists for, and all three are candidates for `PG-5`
item 1.**

### 🔴 Restated and still open from `ACTION PG-5`

🔴 **Item 1 — PAYLOAD-GRADE THE WHOLE SHELF.** **425 of 525 permissive orphans remain unshelved** and the
27 sidebar-only rows from `p297` / `p299` are still unpinned. 🟢 **The channel is confirmed open again this
pass** (11 probes, 11 answers) — `source compose/code/lib/probe_payload.sh; probe_repo <slug>`.
🔵 **Start with the three rows above whose sidebar renders nothing; they are the highest-value pins
available.**
🔴 **Item 2 — re-run `ACTION PG-4`'s candidate selection** with `p299`'s rule (table rows only; narrow
vocabulary). Remaining credential cluster: `digitalcredentials/sign-and-verify-core` and `oneorigin-2-0`'s
three predecessor repositories.
🟢 **Item 3 — DISCHARGED this pass.** See above.
🟡 **Item 4 — put the row count in `recount`.** Still outstanding as a gate change; `p304` ran the gate
rather than extending it.
🟡 **Item 5 — audit the xAPI layer against version 2.0.** Untouched. Every xAPI row here except
[`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) implements **1.0.3**.

### 🔴 What this pass did NOT do on this file

🔴 **No new foundational substrate row was added.** 🔵 **That is the correct outcome, not a nil:** the leg
`p303` directed at `ai-education` page 3 returned **applications and courses, no substrate**, and all five
admitted rows are agent-shaped, so they went to [`agents/top.md`](../agents/top.md).
🔴 **No code, build or test suite was read in any of the ten repositories** — stars, forks and sidebar
labels are rendered values.
🔴 **`api.github.com` was NOT re-tested** (`p303` settled it as an authorization boundary), so **no exact
star integer and no SPDX field exists for any row above.** `nbgrader` is recorded as `1.4k` because that is
what the page renders.

## 🟢 Pass 303 — THE LEARNER-MODEL LAYER FINALLY HAS A PERMISSIVE DATA MODEL, THE SPACED-REPETITION DEPENDENCY CHAIN IS NOW CLEAN END TO END, AND THE SECTOR'S BEST LEARNING-SCIENCE TUTOR TURNS OUT TO HAVE NO GRANT

⏱️ **Pass 303 of `2026-10-18`.** Evidence:
[`p303-licence-payload.2026-10-18-p303.tsv`](../evidence/p303-licence-payload.2026-10-18-p303.tsv) ·
[`p303-topic-paging.2026-10-18-p303.tsv`](../evidence/p303-topic-paging.2026-10-18-p303.tsv) ·
[`p303-reachability.2026-10-18-p303.tsv`](../evidence/p303-reachability.2026-10-18-p303.tsv) ·
[`p303-websearch.2026-10-18-p303.tsv`](../evidence/p303-websearch.2026-10-18-p303.tsv).

🔴 **The mandated foundations phrasing nil'd for the twenty-third consecutive window** (`open source platform
education ERP CRM MIT Apache student information system` → **OpenEduCat** LGPL-3.0, **openSIS**, **Kuali** —
all carried, none permissive; the sources themselves could not name an MIT- or Apache-licensed education ERP).
🟢 **The paged GitHub-topic leg paid instead, and what it added is the layer BELOW the agents: the learner
model and the scheduling algorithm.**

### 🟢 New foundational row — a permissive learner-model data layer, and it draws the distinction this tier needed

🟢 **[`hakimihou/capability-space`](https://github.com/hakimihou/capability-space)** — **MIT** (payload
`LICENSE`, `1 086 B`, `sha256₁₂` `465174e71a3b`) — **10★**, Python.

Its one-line description is the contribution: *"A learner-owned adaptive knowledge space that keeps
**activity, evidence, and mastery distinct**."*

🔵 **Why a 10-star repository earns a foundational row — and this is a judgement, stated as one.** Every
adaptive-tutoring build has to answer "what does this learner know?", and almost every one answers it by
conflating three different things: that the learner *did* something (activity), that something was *produced*
which bears on competence (evidence), and that a model *infers* competence from it (mastery). 🟢 **Keeping
them in separate structures is exactly what makes a claim auditable** — and auditability is now a regulatory
requirement, not a nicety: Vietnam's education listing reaches systems that *assess, grade or rank* students
and Korea's AI Basic Act reaches high-impact AI ([`intel/market.md`](../intel/market.md)). 🔵 **An auditor asks
"show me the evidence behind this mastery score"; a schema that cannot separate the two cannot answer.**

🟢 **The reusable asset is the three-way schema, and it is reusable at any scale and in any subject.** ⚠️ **It
is 10★ and a single author — copy the data model, do not take the dependency.** ⚠️ "Learner-owned" is the
project's framing; whether a client deployment can honour learner data ownership is a contract question this
row does not settle.

### 🟢 The spaced-repetition dependency chain is now permissive end to end

🟢 **[`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki)** — **MIT**
(payload `LICENSE`, `1 079 B`, `sha256₁₂` `2ec9e6e61ed8`) — **4.1k★**, the **highest-starred repository in the
`intelligent-tutoring-system` topic** and the reference implementation of the **Free Spaced Repetition
Scheduler**.

🔵 **Why this pin matters more than its novelty.** This base has carried FSRS as an *algorithm name* across
many passes — `OpenTutor`'s FSRS6, `Bhala-Srinivash/agent-tutor-skill`, `smart-study-agent`'s "FSRS picks the
timing" — without ever pinning the grant on the thing those rows depend on. 🟢 **It is MIT.** So the chain
**scheduler → tutoring skill → engagement deliverable** is permissive at every link, with no copyleft and no
unlicensed hop. ⚠️ **One boundary:** `fsrs4anki` is a *scheduler for Anki*; the portable part is the FSRS
algorithm and its parameter fitting, not the Anki integration. Lift the algorithm.

### 🟢 A competency framework with an institutional copyright holder — and the tier's first BSD grant

🟢 **[`aimclub/ai-competency-model`](https://github.com/aimclub/ai-competency-model)** — 🟢 **BSD-3-Clause**
(payload `LICENSE.md`, `1 531 B`, `sha256₁₂` `bbbc8f2f3ed4`, holder **© 2022 NSS Lab, ITMO University**) —
**30★**.

A structured **professional AI-competency model** (*"Модель профессиональных компетенций в области ИИ"*).
🟢 **Two firsts for this file:** the **first BSD-3-Clause grant** on any tier here (every prior permissive row
was MIT or Apache-2.0), and only the **second permissive row with an institutional copyright holder** rather
than an individual — the other being [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem)
(Apache-2.0, THM).

🔵 **Why institutional provenance is a foundational property and not a footnote:** a ministry, university or
accreditation body procuring a competency framework asks who stands behind it. An individual's MIT repository
cannot answer; a university lab's can. ⚠️ **Boundaries, stated:** this is a **framework document**, not
running software — do not brief it as a system; and the holder is a **Russian state university**, so **an
engagement must run its own counterparty and sanctions review before adoption**. That is a procurement
question, and this base is not competent to answer it — it is flagged so it is not discovered late.

### 🔴 The foundational loss of the pass: the learning-science tutor has no grant

🔴 **[`luffycodes/Tutorbot-Spock`](https://github.com/luffycodes/Tutorbot-Spock) — 56★ — NO LICENCE**
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` all 404 on `main`, `master` and `dev`). Its
sibling [`Tutorbot-Spock-Phys`](https://github.com/luffycodes/Tutorbot-Spock-Phys) (9★), which generates
conversations with **code soliloquies for reliable calculations**, is **equally ungranted**.

🔵 **This is the single most painful refusal on this file, because of what it is**: an LLM tutoring chatbot
*"built on learning science principles"* with academic provenance — precisely the artefact an engagement wants
to point at when a client asks whether the pedagogy is real rather than asserted. 🔴 **No grant means no
permission.** 🟢 **The usable residue is the published work, not the code:** cite the papers and reimplement
the mechanism (the code-soliloquy idea — making the model emit computation separately so arithmetic is not
hallucinated — is a *technique*, and techniques are not what a licence withholds). 🔵 **Pair it with
[`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor), which is the same kind of artefact with
the opposite licence outcome** — WWW '25 paper code under **CC0 1.0** (payload `7 048 B` `a2010f343487`,
verified this pass), i.e. a public-domain dedication. **Academic provenance predicts nothing about the grant;
read it every time.**

### 🔴 And the misconception-based tutor — the best pedagogy in the topic — is AGPL

🔴 **[`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor)** — **AGPL-3.0** (payload `LICENSE.txt`,
`35 148 B`, `sha256₁₂` `8b1ba204bb69`), **12★**, from **Brown University's Programming Languages Team**. A
**misconception-based** tutor for Linear Temporal Logic.

🔵 **"Misconception-based" is a stronger pedagogical claim than anything else in the `intelligent-tutoring-system`
topic**, including the rows this file already carries: instead of scoring an answer right or wrong, it models
*which specific wrong belief* produces the error and teaches against that. 🟢 **The reusable asset is the
misconception catalogue as a design artefact** — enumerate the wrong beliefs for a subject, then write
diagnostics that discriminate between them. 🔴 **AGPL-3.0's network clause reaches a hosted deployment**, so
the code cannot sit inside a client platform. Same verdict for
[`IgorFonck/logicits`](https://github.com/IgorFonck/logicits) (**AGPL-3.0**, `35 149 B` `3972dc9744f6`, Java
natural-deduction ITS).

### 🟢 The `intelligent-tutoring-system` topic is now FULLY enumerated at its head, and that is a completeness claim

🟢 **Population 41; this pass read the entire star-ordered head (ranks 1–20) and recorded every row with its
prior-carry status** in
[`p303-topic-paging.2026-10-18-p303.tsv`](../evidence/p303-topic-paging.2026-10-18-p303.tsv).
🔴 **Nineteen of twenty were already carried** — only
[`HyeonahKang/LatentVariableModel-IntelligentTutor`](https://github.com/HyeonahKang/LatentVariableModel-IntelligentTutor)
(4★, **R**; latent transition analysis in Mplus and hidden Markov analysis) was new, and it is **research code,
not a system**. 🔴 **It also has NO GRANT** — no licence in its sidebar, confirmed on the rendered page
(default branch `main`, 17 commits, root holding `A2_LTM_Analysis.inp`, `A3_HMM_Analysis.R`, `fitstat.R`).
🔵 **So the ITS head's one new row is unusable anyway** — cite the method, not the code.

🔵 **Read that as a positive result, not a nil.** It means this base's coverage of the *academically framed*
ITS corpus is effectively complete — the tail below rank 20 runs from 1★ to 4★ — and that future legs should
go to `ai-tutor` and `ai-education`, where the population is 750 and 528 and the new material actually is.
🟢 **Below rank 8 the topic is entirely single-digit stars**, so "41 repositories" describes a very small real
corpus.

### 🔴 What this pass could NOT do

🔴 **No primary source — twenty-second consecutive pass — and the mechanism is now corrected.** `curl`
receives **`CONNECT tunnel failed, response 403`** from the agent proxy for every non-GitHub host, while
`WebFetch` receives `ENOTFOUND`; `p302` saw only the latter and inferred a resolver scope. 🔵 **It is a network
POLICY on hosts that resolve fine.** Consequence for this file: **every market and regulatory datum
referenced from here is search-snippet-attributed**, never publisher-read.
🔴 **`api.github.com` answers and is authenticated (15 000-request core limit) but is bound to this session's
configured repositories** — `/search/repositories` is refused by name. **No exact star integers, no
`licence_spdx`, no `pushed_at` for any row on this file, and this is an authorization boundary rather than a
transport fault, so it will not clear on a retry.**
🔴 **`make hooks` was NOT run** (third consecutive pass).
🔴 **`feedbacksystem`'s AI mechanism is still unread** — carried from `p302` as an open item; this pass did not
read its code, so the "SQL checker only" boundary stands unchanged.
🔴 **No repository on this file had its commit history or test suite read.** Maturity statements are from
rendered pages: star counts, fork counts and visible commit totals.

## 🟢 Pass 302 — THE EVALUATION TIER FINALLY HAS PERMISSIVE CODE IN IT, AND THE BENCHMARK THIS SHELF MOST WANTED TURNED OUT TO HAVE NO GRANT

⏱️ **Pass 302 of `2026-10-18`.** Evidence:
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv) ·
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv) ·
[`p302-websearch.2026-10-18-p302.tsv`](../evidence/p302-websearch.2026-10-18-p302.tsv).

🔴 **The mandated foundations phrasing nil'd again** (`open source platform education ERP CRM MIT Apache
student information system` → OpenEduCat LGPL-3.0, OpenSIS GPL-2.0, RosarioSIS GPL-2.0, Frappe, GegoK12,
Fedena, SchoolTool — **every one already carried**; see [`verticals/solutions.md`](../verticals/solutions.md)
for the twenty-second consecutive nil on a *permissive* education ERP/CRM). 🟢 **The directed GitHub-topic
leg paid instead, and what it added belongs in the FOUNDATIONS tier rather than the agent tier: evaluation
and feedback infrastructure.**

### 🟢 New foundational row — an institution-held automatic feedback service

**[`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem)** — 🟢 **Apache-2.0**
(**payload** `LICENSE`, `10 785 B`, sha256₁₂ `65125d9e480b`, holder **© 2023 Technischen Hochschule
Mittelhessen**) — **24★ / 9 forks**, default branch **`dev`**.

*"Intelligent, personalized feedback for students using artificial intelligence."* It **automatically checks
submissions and returns an immediate result**, proposes fixes for the student's mistakes, and — the property
that makes it foundational rather than a demo — **aggregates common mistakes so the lecturer can address
them in class.** Ships **Helm charts and Kubernetes** production install instructions, with a THM-hosted
project site at `frits.mni.thm.de`.

🟢 **Why this sits on `foundations.md` and not on `agents/top.md`:** it is a *service a university holds the
copyright to*, with a deployment story, not a personal repository with a clever prompt. This shelf has
repeatedly noted that the open grading agent turns out to live **inside a platform**
([`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) and its
[`Athena`](https://github.com/ls1intum/Athena) feedback service being the standing example) — `feedbacksystem`
is the **second** independent instance of that pattern, from a second German institution, and the two
together make it a pattern rather than an anecdote. ⚠️ **Boundaries, stated:** the AI mechanism is **not
documented** on the rendered page, the Languages panel is **empty**, the only visible demo is an **SQL
checker**, and production use at THM is **implied by a Helm chart, not stated**. Read the code before
promising any subject beyond SQL.

### 🟢 The evaluation tier — two MIT audits, and they answer a question this base has been asking since `p288`

This file has carried [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) as the
permissive evaluation framework, which is a *harness*. 🟢 **What it lacked was a worked education-specific
evaluation DESIGN.** Two arrived:

| repo | licence (payload) | stars | what it establishes |
|---|---|---|---|
| 🆕 [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | 🟡 **Apache-2.0 — MANIFEST-GRANTED, not payload-pinned** *(`pom.xml`, branch `master`, 3 752 B, sha256₁₂ `54d5d8152efb`: `<licenses><license><name>The Apache Software License, Version 2.0</name>…<distribution>repo</distribution>`; README states it independently. ⚠️ **No `LICENSE` file at any ladder name, no sidebar label**, read `p304`)* | **114★ / 47 forks** (ratio 0.41), Java, branch `master` | 🟢 **THE MEASUREMENT LAYER THIS TIER WAS MISSING, and it was on this base's shelves marked UNGRANTED.** A Java psychometrics library: **classical test theory, item response theory (IRT), factor analysis** and related measurement techniques. 🔵 **Pairs directly with `p303`'s learner-model data layer** — `capability-space` gives you somewhere to put activity/evidence/mastery, this gives you a defensible way to ESTIMATE mastery, and IRT is the method an assessment regulator already recognises. 🔴 **Corrected `p304`:** a prior pass published it as *"IRT and BKT code with no grant"* — wrong, and wrong in the expensive direction. `gate-enumeration` caught it on the first hooks run in four passes. ⚠️ **Cite the manifest AND the README together; a manifest grant is a weaker pin than a file.** |
| [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT** `1 150 B` `a1c6b65c5bb1` | 3★ | Pre-registered audit (arXiv:2607.28128) of whether an LLM helpfulness judge **rewards answer-leakage that reduces later independent work**. One frozen base model, two policies — `ConvTutor` (single-node LangGraph) vs `PedTutor` (state tracker + decomposer + **deferral gate** + hint cascade) — against a cold baseline, weak simulated student (**Llama-3.1-8B**), Opus primary judge + second-judge robustness check, a **frozen leakage matcher** (`protocol/leakage.py`), and ablations removing tracker / gate / cascade individually. **10 replicates × {cold, conv, ped}** per base; GPT and Gemini bases run separately and **never pooled**. |
| [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** `1 154 B` `fef00f185287` | 4★, branch **`master`** | Pre-registered audit of LLM judges with analysis of **bounded-rating bias** across ability levels — whether one judge can score a weak and a strong learner on the same scale, which every adaptive-tutoring claim assumes. |

🔵 **Why two repositories in the low single digits of stars earn foundational rows:** the binding constraint
in this industry has moved from *can an agent tutor* to *can you show it does not harm learning* — Vietnam's
Decision 33 and Korea's AI Basic Act both now reach automated assessment
([`intel/market.md`](../intel/market.md)). An engagement that arrives with `inspect_ai` as the harness and
**this** as the design is answering the actual question. 🟢 **The reusable asset is the structure — frozen
base model, policy-only variation, pre-registration, a leakage matcher frozen before scoring, and
per-component ablations** — and it is reusable whatever the subject.

⚠️ **Hard boundary on both: NO RESULTS ARE STATED ON EITHER PAGE.** The READMEs give commands to recompute
from tracked tables in `results/`; the hypotheses live in a `paper-plan.md` this pass did **not** read.
**Cite the design. Never cite an effect size from these rows.** ⚠️ And `ability-levels-audit`'s default
branch is **`master`** — a pin written against `main` will 404, which is exactly the failure mode this base
priced as a rate at `p301`.

### 🔴 The benchmark this shelf most needed has NO GRANT

🔴 **[`DAMO-NLP-SG/M3Exam`](https://github.com/DAMO-NLP-SG/M3Exam) — 105★ — no `LICENSE`, `LICENSE.md`,
`LICENSE.txt` or `COPYING` on `main` or `master`.** A **multilingual, multimodal, multilevel** benchmark of
real exam questions for evaluating LLMs: on paper the single most useful evaluation asset for an education
engagement outside the OECD core, since it is built from *actual national exams* across languages. 🔴 **No
grant means the question of whether Globant may redistribute or build on it has an answer, and the answer is
no.** 🔵 **Brief it as readable prior art — use it to argue that national-exam evaluation is feasible — and
build the deliverable on the MIT audit designs above.**

### 🔴 Also refused into this tier this pass

🔴 **[`blessed0x/scratch-unified-mcp`](https://github.com/blessed0x/scratch-unified-mcp) — no licence** —
a **headless Scratch VM exposed over MCP with 108 tools** for an agent to build, test and publish Scratch
projects. **The best-shaped K-12 computing artefact this base has seen** — Scratch is the near-universal
primary-school programming environment, and a headless VM behind MCP is precisely the missing piece for an
agent that *teaches programming by doing it*. 🔴 **1★ and no grant.** 🔵 **Record the shape and build it: the
capability is a tractable project, and there is no permissive equivalent on this shelf.**

🔴 **[`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor)** — **GNU GPL** (payload `LICENSE.txt`,
`35 148 B`, `8b1ba204bb69`), 12★, from **Brown PLT**. A misconception-targeting tutor for **Linear Temporal
Logic** — academically serious and the right *pedagogy* (teach to the misconception, as
[`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill)
does permissively). 🔴 **GPL. Study the misconception catalogue; do not link the code.**

### 🟢 New offline-capable row — relevant wherever egress is the constraint

**[`Fazmin/AILearningGuide`](https://github.com/Fazmin/AILearningGuide)** — 🟢 **MIT** (**payload** `LICENSE`,
`1 081 B`, sha256₁₂ `e29ef713b542`, holder **Discover AI contributors**) — **202★**. An **offline desktop**
application with **51 interactive labs** on machine-learning topics. 🔵 **On this file because of the offline
property, not the content**: this base has repeatedly flagged that ministry and rural deployments cannot
assume egress (the standing example being [`learningequality/kolibri`](https://github.com/learningequality/kolibri)),
and this is a permissive, self-contained AI-literacy curriculum that runs with no network. 🔵 **Pairs with
Kolibri for an offline AI-literacy package** — Kolibri carries it, this is payload. ⚠️ **It teaches AI; it is
not an agent.** Internals unread this pass.

### 🔴 What this pass could NOT do

🔴 **Twenty-first consecutive pass with no primary government or IGO source, and the cause is now NAMED.**
This session's resolver answers **`github.com` and `raw.githubusercontent.com`**; every other host tried
returned **`getaddrinfo ENOTFOUND`** — `www.congress.gov`, `www.govinfo.gov`, `docs.house.gov`,
`digital-strategy.ec.europa.eu`, `www.iesalc.unesco.org`, `www.vietnam-briefing.com`,
`www.allenandgledhill.com`. 🟢 **That makes it a resolver scope rather than government-specific blocking** —
a more useful fact, because it predicts the outcome of every future leg. Matrix:
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv).
🔴 **`api.github.com` is intercepted by the agent proxy**, so no exact star integer, no `licence_spdx` and no
`pushed_at` for any row; **all star figures are rendered and rounded.**
🔴 **`make hooks` was NOT run** — this base's gates could not be executed from this session, reproducing
`p301`. The licence instrument used instead was the direct `raw.githubusercontent.com` payload read, recorded
with byte length and `sha256₁₂` for every row so any later pass reproduces it exactly.
🔴 **The IESALC LATAM triple (87/74/26) has still never been read at its publisher** — open since `p282`,
and the host is unreachable from here. It stays **AGGREGATOR-ATTRIBUTED**.

## 🟢 Pass 301 — THE BACKLOG'S RANKED ITEM 1 DISCHARGED AT FIVE TIMES `p300`'S SCALE: 105 PAYLOAD READS, 146 UNPINNED ROWS FOUND MECHANICALLY, AND TWO OF THIS BASE'S ANECDOTES TURNED INTO RATES

⏱️ **Twenty-third pass of `2026-10-18`.** Evidence:
[`p301-payload-grade.2026-10-18-p301.tsv`](../evidence/p301-payload-grade.2026-10-18-p301.tsv) ·
[`p301-probe-calibration.2026-10-18-p301.tsv`](../evidence/p301-probe-calibration.2026-10-18-p301.tsv) ·
[`p301-instrument-substitution.2026-10-18-p301.tsv`](../evidence/p301-instrument-substitution.2026-10-18-p301.tsv) ·
[`p301-websearch.2026-10-18-p301.tsv`](../evidence/p301-websearch.2026-10-18-p301.tsv).

🟢 **`p300`'s backlog item 1 — *"payload-grade the whole shelf… the cheapest large gain in twenty
passes"* — is DISCHARGED for 105 rows.** `p300` read 20 payloads and called that its best-ever batch;
`p301` read **105**.

### 🟢 The target set was derived mechanically, not chosen

🔵 **Which rows needed grading was not a judgement call.** Every `github.com/<owner>/<repo>` on this
file and [`agents/top.md`](../agents/top.md) was extracted, de-duplicated, and partitioned by whether
any non-archive line mentioning the slug also carries a sha256 or a 12-hex pin:

| shelf slugs, de-duplicated | **265** |
|---|---|
| 🟢 already carrying a payload pin | **119** |
| 🔴 **unpinned — the actual backlog** | **146** |
| 🟢 **read at payload this pass** | **105** *(72 % of the backlog)* |
| 🔴 left for `p302` | **41** |

### 🟢 The result, and it is the same asymmetry `p300` found — stated again because it replicated

| family | rows |
|---|---|
| 🟢 **MIT** | **53** |
| 🟢 **Apache-2.0** | **16** |
| 🟢 **BSD-3-Clause** | **6** |
| 🟢 **MPL-2.0** | **1** |
| 🔴 **AGPL-3.0** | **5** |
| 🔴 **GPL-3.0** | **4** |
| 🟡 **LGPL** | **2** |
| 🟡 **CC** *(not a software licence)* | **2** |
| 🔴 **no payload served at all** | **13** |
| 🟡 `UNCLASSIFIED` *(triaged by hand below)* | **3** |

🟢 **Permissive — MIT + Apache-2.0 + BSD + MPL — is 76 of 105, or 72 %.** 🔴 **Copyleft is 11, or
10.5 %.** 🔵 **And not one carried licence cell was REFUTED.** Every row whose published licence this
pass could check came back the same, several of them **byte-exact** against figures this base printed
in earlier passes:

| row | carried cell | `p301` payload | verdict |
|---|---|---|---|
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | **AGPL-3.0 (34 524 B)** | AGPL-3.0, **34 524 B**, sha256₁₂ `8d56b405468a` | 🟢 **BYTE-EXACT** |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | **AGPL-3.0, 34.143 B** | AGPL-3.0 at `LICENSE.md`, **34 143 B**, sha256₁₂ `281e174e4d5f` | 🟢 **BYTE-EXACT** |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | **IMS Specification Document License, 12.402 B** | the IMS document licence, **12 402 B**, sha256₁₂ `6178707d6c68` | 🟢 **BYTE-EXACT** |
| [`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) | **CC BY-SA 4.0, 2 123 B** | CC family at `LICENSE.md`, **2 123 B**, sha256₁₂ `c5faf8ce5bec` | 🟢 **BYTE-EXACT** |
| [`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) | **proprietary "AStheTECH Community License", all rights reserved** | *"limited, non-exclusive, non-transferable, non-sublicensable, and revocable… All rights not expressly granted are reserved"*, 6 489 B | 🟢 **CONFIRMED verbatim** |
| [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | **GPL-3.0** | GPL-3.0 at **`LICENSE.txt`**, 35 147 B | 🟢 **CONFIRMED** |
| [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) | *"LIVE, no licence payload"* | **NO-PAYLOAD** on `master` | 🟢 **CONFIRMED** |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | root manifests disagree; **no single grant** | **NO-PAYLOAD** on `develop` | 🟢 **CONFIRMED** |
| [`digitalcredentials/sign-and-verify`](https://github.com/digitalcredentials/sign-and-verify) | **ARCHIVED `2026-08-26`; payload clean and silent about it** | MIT, 1 075 B, sha256₁₂ `09e4c03a44a7` — **silent on archive status** | 🟢 **`p300`'s finding REPRODUCED on a second read** |

🔵 **`p300` wrote that its sidebar-grade rows were *"accurate; unproven, not wrong."* `p301` is the
larger sample that holds it: 105 reads, zero refutations.** 🟢 **The value delivered is not corrected
data — it is that 105 rows a studio may now quote are pinned to a byte count and a hash.**

### 🟢 TWO ANECDOTES BECAME RATES — and both are larger than this base assumed

🔵 **`compose/code/lib/probe_payload.sh` documents its traps with three or four measured examples
each. 105 reads price them.**

🔴 **Trap 1 — the default branch is not `main`/`master`: 11 of 105, `10.5 %`.** A probe that hardcodes
the branch writes **one row in ten** down as ungranted:

| branch | rows |
|---|---|
| `develop` | `oat-sa/tao-core` · `oppia/oppia-android` · `datakind/student-success-tool` · `LearnPress/learnpress` |
| `dev` | `pressbooks/pressbooks` |
| `staging` | `code-dot-org/code-dot-org` |
| `unstable` | `learningequality/studio` |
| `v6.2.0` | `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` |
| `0.7` / `3.x` | `php-xapi/client` · `php-xapi/model` |
| 🔴 **`51`** | [`eledia/moodle-block_elediaai_tutor`](https://github.com/eledia/moodle-block_elediaai_tutor) — **a bare integer as a default branch** |

🔴 **Trap 2 — the grant is not at plain `LICENSE`: 9 of 105, `8.6 %`.** `LICENSE.md` **×7**
(`1EdTech/caliper-spec`, `AStheTECH/mewcp-google-classroom`, `codelitdev/courselit`,
`datakind/student-success-tool`, `haxtheweb/haxcms-php`, `nmarafo/OpenDidactia`,
`pressbooks/pressbooks`), `LICENSE.txt` **×2** (`Tangerine-Community/Tangerine`,
`davemckain/qtiworks`). 🟢 **`p295` found this on `Submitty` and called it *"a THIRD spelling"*; at
this sample it is a standing property of the corpus, not a curiosity.**

🔵 **Taken together, a one-path probe on a hardcoded branch would misreport roughly 1 row in 5 on this
shelf.** That is the quantified case for the shared instrument — and `p301` could not run it.

### 🔴 THIRTEEN shelf rows serve NO licence payload at all — named, because an unnamed count is not actionable

| row | branch |
|---|---|
| [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) | `main` |
| [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | `develop` |
| [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) | `master` |
| [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) | `main` |
| [`arijit8972/agentic-automated-assignment-grading`](https://github.com/arijit8972/agentic-automated-assignment-grading) | `main` |
| [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance) | `main` |
| [`eledia/moodle-block_elediaai_tutor`](https://github.com/eledia/moodle-block_elediaai_tutor) | `51` |
| [`hdronamraju/sped-agent`](https://github.com/hdronamraju/sped-agent) | `main` |
| [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | `master` |
| [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | `main` |
| [`openstax/os-webview`](https://github.com/openstax/os-webview) | `main` |
| [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) | `master` |
| [`yoyoconnor/BlackboardMCP`](https://github.com/yoyoconnor/BlackboardMCP) | `main` |

⚠️ **`NO-PAYLOAD` is a statement about the FILENAME LADDER, not a finding of "unlicensed."** This
pass's probe did **not** implement the shared instrument's README-link arm, so a grant living at an
unusual subdirectory path would be missed here — and `p300` recorded exactly that case
(`OS4ED/openSIS-Classic`, GPL-2.0 at `docs/License.txt`). 🔴 **Three of these rows sit in special
education and IEP compliance** (`eakarsu/…-iep-compliance`, `hdronamraju/sped-agent`) **or automated
grading** (`arijit8972/…`) — the highest-stakes uses in the corpus, with no grant a client can rely
on. **Do not brief any of the thirteen as buildable until the gap is closed.**

### 🟢 The three permissive rows worth naming out of this sweep

🟢 **[`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) — MIT, 1 081 B,
sha256₁₂ `c593c2afc813`, holder *UK AI Security Institute*.** An evaluation framework from a
**national AI safety institute**, permissively licensed. 🔵 This base has recorded *"no dominant OSS
agent eval"* as a gap in a sibling industry; for education it is the instrument that lets a studio
**measure** a tutor instead of demonstrating one — and its provenance is the kind a ministry accepts.

🟢 **[`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite)
— Apache-2.0, 11 351 B, sha256₁₂ `3f17cff4210f`, holder **Intel Corporation**.** Already carried;
now pinned, and the holder is confirmed at payload rather than inferred from the org name.

🟢 **[`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) —
MIT, 1 074 B, sha256₁₂ `7df20dcdf919`.** The governance layer every regional leg this pass asked for
(LATAM's **26 %-with-a-strategy** gap, Kazakhstan's data-protection clause) and the one a studio can
ship without a licence negotiation.

### 🔴 What this pass could NOT do

🔴 **The repository's own payload instrument was UNRUNNABLE.** `bash -c '. compose/code/lib/probe_payload.sh;
probe_repo …'` was **DENIED by the sandbox** (*"Code from External"*), as was `make hooks`. 🟢 **The
substitution is declared, and it was CALIBRATED before it was trusted** — see
[`intel/trends.md`](../intel/trends.md) `T-p301a` and
[`p301-probe-calibration.2026-10-18-p301.tsv`](../evidence/p301-probe-calibration.2026-10-18-p301.tsv).
🔴 **41 of the 146 unpinned rows are still unread**, and the ladder used was **narrower** than the
shared instrument's (no README-link arm), so every `NO-PAYLOAD` above is weaker than the shared tool's
would be.
🔴 **No standing gate ran against this file.** `gate-tables`, `gate-enumeration`, `gate-absence` and
the rest are part of the same denied chain.
🔴 **The ten star/forks cells remain untouched — FIFTH pass of asking.**


## 🟢 Pass 300 — THE PAYLOAD CHANNEL THREE PASSES RECORDED AS ABSENT WAS THIS BASE'S OWN INSTRUMENT, UNCALLED — AND `p299`'S FIFTEEN ROWS WERE NEVER ON THIS TABLE

⏱️ **Twenty-second pass of `2026-10-18`.** Evidence:
[`p300-promotion-gap.2026-10-18-p300.tsv`](../evidence/p300-promotion-gap.2026-10-18-p300.tsv) ·
[`p300-payload-grade.2026-10-18-p300.tsv`](../evidence/p300-payload-grade.2026-10-18-p300.tsv) ·
[`p300-raw-channel-control.2026-10-18-p300.tsv`](../evidence/p300-raw-channel-control.2026-10-18-p300.tsv) ·
[`p300-subject-oracle.2026-10-18-p300.tsv`](../evidence/p300-subject-oracle.2026-10-18-p300.tsv) ·
[`p300-gate-masking.2026-10-18-p300.tsv`](../evidence/p300-gate-masking.2026-10-18-p300.tsv) ·
[`p300-websearch.2026-10-18-p300.tsv`](../evidence/p300-websearch.2026-10-18-p300.tsv).

🟢 **`ACTION PG-4` discharged: 20 slugs read, 17 admitted, 3 rejected, 0 absent — and every single
licence is a PAYLOAD read with a sha256, the first batch in this base's history of which that is
true.** 13 are new rows here, 1 is a new row on [`agents/top.md`](../agents/top.md), and 3 were
**already shelved** and are upgraded in place.

### 🔴 The finding that cost the most: `p297` and `p299` graded 27 rows "sidebar-only" against a channel that was open, and the instrument for it was already in this repository

`p297` wrote the bound plainly: *"No `LICENSE` payload was read for any of them. `curl` 403 on 4/4,
no `api.github.com`, **no raw path**."* `p299` inherited it and graded 14 of its 15 rows
sidebar-grade. 🔴 **Two of those three clauses reproduce exactly at `p300`. The third is false:**

| channel | result at `p300` | status |
|---|---|---|
| `curl` → `github.com/<slug>` | **403**, 378 B | 🔴 as recorded |
| `curl` → `api.github.com/repos/<slug>` | **403**, 378 B | 🔴 as recorded |
| `curl` → **`raw.githubusercontent.com/<slug>/<branch>/LICENSE`** | 🟢 **200, 1 525 B, the grant itself** | 🔴 **RECORDED AS ABSENT. IT IS OPEN** |

🔴 **And it is worse than an unmeasured channel, because this base had already built the loop.**
[`compose/code/lib/probe_payload.sh`](../compose/code/lib/probe_payload.sh) — *"SHARED PAYLOAD PROBE
— source this, do not rewrite it"* — reads exactly that path, resolves the real default branch with
`ls-remote --symref`, walks a filename ladder and classifies with the hardened shared classifier. It
answered on the **first call**, correctly, including the two traps its own header documents:

- `impierce/digital-credential-data-models`' default branch is **`dev`** — not `main`, not `master`.
- `digitalcredentials/verifier-core`'s grant is at **`LICENSE.md`**; `dhodges47/...` at **`LICENSE.txt`**.

🔵 **The generalisable error, and it is not "a channel was mislabelled".** `p297` concluded *"no raw
path"* from probes of **two other hosts**. That is `p294`'s own refuted move — *measure channel A,
conclude about B* — and it survived three passes because the conclusion was written as a **property
of the session** rather than as what it was: **a property of the two URLs actually tried.** 🟢 The
clause this base's oracle gains: *name the host you measured, and never generalise a refusal across
hosts.*

### 🔴 `p299`'s fifteen rows were announced on this file and were never written to its table

🔴 **Measured at `p300`: of the fifteen slugs `p299` admitted, ZERO appear on a row of
`## Permissive foundations`.** They live only inside `p299`'s own narrative table, further up this
same file. `p298`'s thirteen, by contrast, all reached the table.

🔵 **Why this matters more than a formatting slip: "shelved" has two meanings here and they came
apart.** The canonical table is what a studio reads under *"Permissive foundations"*; the pass
sections are history. A reader of this file's shelf was **fifteen rows short of what the pass
announced**. 🟢 **All fifteen are restored above, marked ♻️**, with `p299`'s own figures and
boundaries carried intact.

🔴 **And the file's prose total had drifted again, by exactly the thirteen rows `p298` added** — the
defect `p297` had corrected one pass earlier. Both corrections are recorded at the table.

### 🟢 The thirteen new rows, by layer — and the layer counts that were zero

| layer | rows before `p300` | after | the row that carries it |
|---|---|---|---|
| **credentialing** | 🔴 **1** *(a validator)* | 🟢 **12** | [`learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) — 89★, iOS **and** Android |
| **xAPI 2.0 capable** | 🔴 **0** | 🟢 **1** | [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) — and it takes over an `lrsql` database **in place** |
| **SCORM** | 1 | 🟢 **3** | [`dhodges47/SCORM-LearningManagementSystem`](https://github.com/dhodges47/SCORM-LearningManagementSystem) — 184★ / 95 forks on 36 commits |
| **EU skills taxonomy (ESCO)** | 🔴 **0** | 🟢 **1** | [`BeBadges/escobadges`](https://github.com/BeBadges/escobadges) — in the hour EMEA returned its twelfth nil |

🔵 **Six of the twelve credentialing rows are one family — the `digitalcredentials/*` repositories of
the MIT-based Digital Credentials Consortium, 2 732 commits between them — and `ACTION PG-4` named
none of them.** It named the standards body's validator instead, which was already on this table.

### 🔴 What `ACTION PG-4` got wrong, measured: 3 of its 7 named slugs were already shelved, and 1 was not xAPI at all

| slug `PG-4` named | what it turned out to be |
|---|---|
| `1EdTech/digital-credentials-public-validator` | 🔴 **already a row on this table**, shelved `p297` |
| `1EdTech/OpenCASE` | 🔴 **already a row on this table**, shelved `p297` |
| `adlnet/xAPI-Spec` | 🔴 **already a row on this table** (ungraded) — upgraded, not added |
| `xapi-labs/xapi-cli` | 🔴 **NOT EXPERIENCE API.** It is `xapi-to` (`xapi.to`): agent capability/API calling, with crypto, `x402` payments and Cloudflare Workers. **Zero** Experience-API markers in a 50 919-byte README; 22 hits for API-credential/auth senses |
| `pelotech/xapi-lrs` | 🟢 new, correct, and the best row of the batch |
| `sr258/scorm-h5p-wrapper` | 🟢 new and correct |
| `dhodges47/SCORM-LearningManagementSystem` | 🟢 new and correct |

🔴 **`p299` published the rule that would have caught three of these four errors in the same breath
as the instruction that made them.** Its own `ACTION PG-4` item 1 reads: *"a plain text diff of the
list against the shelf files is WRONG… match only lines whose first non-space character is a pipe."*
That rule was applied to the **shelf** side of the diff and never to the **candidate** side.

🔵 **The error class, stated for reuse: a layer backlog assembled by SUBSTRING MATCH on the slug is
not a layer backlog.** `xapi` in an owner name is not the Experience API; `credential` in a README is
as likely to mean an API key as a learner's diploma — **measured this pass: the word `credential`
fires 15 times in `xapi-cli`'s README and not once about learning.** A candidate must be checked
against the shelf and against the layer's *narrow* vocabulary before a pass is told to spend its
budget on it.

### 🔴 The two rejections that were not about licences

🟢 **All 20 payloads were permissive — 13 MIT, 6 Apache-2.0, 1 BSD-3-Clause, zero copyleft.** So for
the first time on this file the licence gate rejected **nothing**, and all three rejections turned on
substance:

| rejected | why, and the channel that said so |
|---|---|
[`xapi-labs/xapi-cli`](https://github.com/xapi-labs/xapi-cli) | 🔴 wrong subject entirely — see the table above |
[`digitalcredentials/sign-and-verify`](https://github.com/digitalcredentials/sign-and-verify) | 🔴 **ARCHIVED BY ITS OWNER `2026-08-26`, read-only.** 7★ / 9 forks / 197 commits, and its README names `sign-and-verify-core` only as a **dependency**, never as a successor. 🔵 An archive notice is a *rendered-page* signal: the payload read was clean and said nothing about it |
[`issuebadge/mcp-server`](https://github.com/issuebadge/mcp-server) | 🔴 **5 commits, 0★, no description — and it requires an `ISSUEBADGE_API_KEY` from a hosted commercial issuer, which mints the certificates.** The MIT grant covers a thin client to somebody else's service. Rejected on substance; it was the pass's one *agent-shaped* near-miss |

🔵 **Note the asymmetry worth keeping: the payload channel settles the GRANT and is silent on
everything that matters next.** Archived-ness, a fork banner, a vendor key requirement and the real
subject all live on the rendered page or in the README. A base that upgrades to payload grade and
stops reading the page will shelve archived repositories with beautiful digests.

### 🟢 Sidebar against payload: 10 of 10 agreed, so the old rows were unproven, not wrong

🔵 Ten rows were read on **both** channels this pass. **All ten agreed** (MIT×6, Apache-2.0×3,
and `digitalcredentials/vc`'s BSD-3-Clause, where the sidebar was also right and the README adds a
second, narrower MIT claim). 🟢 **That is worth saying plainly, because it is good news about this
base's history:** the sidebar-grade rows `p297` and `p299` published were **accurate**; what they
lacked was proof and a digest. The payload read adds the pin, the holder and the path — and catches
the `LICENSE.md` / `LICENSE.txt` / `dev`-branch cases a sidebar cannot see.

### 🔴 Standing action for the next pass — `ACTION PG-5`

**425 of 525 permissive orphans remain unshelved.** Ranked:

1. 🟢 **PAYLOAD-GRADE THE WHOLE SHELF. The channel is open and the loop is written** —
   `source compose/code/lib/probe_payload.sh; probe_repo <slug>`. Every row still marked
   *(sidebar, read `pNNN`)* can be pinned with a sha256 this pass. Start with the 27 rows `p297` and
   `p299` published sidebar-only, then the ♻️ fifteen restored above.
2. 🔴 **Re-run `ACTION PG-4`'s candidate selection with the rule `p299` already wrote.** Before
   naming any slug for a layer: (a) check it against **table rows only** — first non-space character
   a pipe; (b) check the layer's **narrow** vocabulary, not the bare token. The remaining credential
   cluster is `digitalcredentials/sign-and-verify`'s successor `sign-and-verify-core`, and
   `oneorigin-2-0`'s three predecessor repositories, which its README says were standalone under a
   `digitalcredentials` org.
3. 🔴 **The ten remaining star/forks cells — UNTOUCHED FOR A FOURTH PASS.** `uPortal` 286★ ·
   `schulcloud-server` 81★ · `studio` 193★ · `Tangerine` 70★ · `DFE-Digital` 38★ · `Ed-Fi-ODS` 28★ ·
   `nbgrader` 1.4k★ · `Numbas` 215★ · `PrairieLearn` 519★ · `OpenEMIS` 7★. The prior is not zero:
   `p295` refuted 2 of 11.
4. 🔴 **Put the row count in `recount`.** This prose total has now drifted twice (`p297`: 31 vs 39;
   `p300`: 48 vs 61) and been corrected twice by hand. A count that is re-derived by a gate cannot
   drift; one that a pass must remember to re-sum will.
5. 🟡 **Audit the xAPI layer against version 2.0.** Every xAPI row on this file except
   `pelotech/xapi-lrs` implements **1.0.3**, and `adlnet/xAPI-Spec` says so of itself. A client
   briefed on "standards-shaped analytics" is being briefed on a superseded version unless the row
   says which.


## 🟢 Pass 299 — FIFTEEN NEW PERMISSIVE SUBSTRATES, AND THE ONE LAYER `ACTION PG-3` PUT FIRST TURNED OUT TO HAVE BEEN WITHDRAWN FROM PUBLIC VIEW

⏱️ **Twenty-first pass of `2026-10-18`.** Evidence:
[`p299-promotion-gap.2026-10-18-p299.tsv`](../evidence/p299-promotion-gap.2026-10-18-p299.tsv) ·
[`p299-caliper-layer.2026-10-18-p299.tsv`](../evidence/p299-caliper-layer.2026-10-18-p299.tsv) ·
[`p299-channel-control.2026-10-18-p299.tsv`](../evidence/p299-channel-control.2026-10-18-p299.tsv) ·
[`p299-shelf-diff.2026-10-18-p299.tsv`](../evidence/p299-shelf-diff.2026-10-18-p299.tsv).

🟢 **`ACTION PG-3` discharged on both of its instructions, and the first one is refuted.** `p298`
ordered **~12 from the layers still at zero rows — Caliper analytics, SCORM tooling, QTI
authoring/conversion** — and ordered the list de-duplicated case-insensitively first. `p299` read
**twenty-eight slugs**, admitted **fifteen**, rejected **three**, and found **five more that no longer
exist.** Fourteen reads are sidebar-grade `github.com` HTML; **five are payload reads**, because this
pass is the one where the sidebar stopped being good enough.

### 🔴 Caliper: the layer is at zero rows because the code was taken away, not because this base missed it

`p298` wrote the instruction *"Search the list for `caliper`."* 🔴 **It was searched. `p989`'s list
contains the string `caliper` exactly ZERO times in 528 rows** — so the instrument `ACTION PG-3`
named could not have supplied this layer at all. It was sourced by WebSearch instead, and what came
back is the finding:

| Caliper artefact | grant | state |
|---|---|---|
| `IMSGlobal/caliper-php-public` · `IMSGlobal/caliper-ruby-public` · `Brightspace/ims-caliper-python` · `1EdTech/caliper-python` · `1EdTech/caliper-java` | — | 🔴 **ALL FIVE 404.** Every reference **client library**, in every runtime |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | 🔴 **`Other`** *(org listing)*; `/blob/master/LICENSE` is **404** | live · 22★ · 17 forks · 1 058 commits |
| [`1EdTech/CaliperBootcamp`](https://github.com/1EdTech/CaliperBootcamp) | 🟢 **`MIT`** | live · 2★ · **20 commits** — a playground, not a library |
| [`1EdTech/caliper-js-example`](https://github.com/1EdTech/caliper-js-example) | 🔴 `LGPL-3.0` *(payload)* | live · 8★ · 67 commits |
| [`1EdTech/caliper-ontology`](https://github.com/1EdTech/caliper-ontology) | 🔴 `LGPL-3.0` | 🔴 **archived** |
| [`1EdTech/moodle-logstore_caliper`](https://github.com/1EdTech/moodle-logstore_caliper) | 🔴 `GPL-3.0` | live · 0★ · 13 commits |
| [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | 🔴 `LGPL-3.0` | live · 3★ · **365 commits** on branch `public` |
| [`ucsd-ets/openedx-caliper-tracking`](https://github.com/ucsd-ets/openedx-caliper-tracking) | 🔴 `GPL-3.0` | 🔴 **archived** |
| `ims_caliper` *(RubyGems)* | 🔴 `LGPL-3.0` | v1.0.1, **2016-07-15**, **55 610 downloads**, and its linked source URL is a **404** |

🔴 **The University of Michigan fork says why, in its own description: it "has been unarchived since
1EdTech made the upstream `caliper-php` private."** A university un-archived a dead fork because the
standards body closed the original. 🔴 **So the honest row for Caliper is still zero** — the only
permissive artefact in the whole layer is a **20-commit proof-of-concept playground**, and everything
load-bearing is LGPL, GPL, archived, or gone.

🔵 **This is the exact opposite shape to `p298`'s LTI and QTI finding, and it lands on `p298`'s own
advice.** `p298` showed the integration boundary is permissive in six runtimes and told clients
*"integrate, do not fork."* 🔴 **At Caliper that advice has no permissive surface to land on.** A
studio that needs standards-shaped analytics events has three options and no fourth: take the
copyleft, implement the spec from a document whose own grant is `Other`, or **use xAPI instead** —
which is why the xAPI rows below matter more than their star counts suggest.

### 🟢 The fifteen new rows, read `2026-10-18`

| repo | licence (read `2026-10-18`) | stars | forks | commits | branch | layer, and the boundary in the row |
|---|---|---|---|---|---|---|
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | 🟢 `MIT` *(sidebar)* | **78** | **52** | **1 039** | `master` | **The highest-adoption row in this batch.** NodeJS suite testing the **`MUST` requirements of the xAPI spec** — from **ADL**, who author the spec. 🟢 This is how you prove an LRS claim instead of repeating it. ⚠️ Its own README: basic auth only, **"should not be run against a production LRS endpoint"** |
| [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | 🟢 `Apache-2.0` *(sidebar)* | **60** | 33 | 153 | `master` | The **xAPI Profiles** companion specification, also from ADL. 🔵 **The permissive counterpart to everything Caliper no longer offers:** a standards document you may actually build on. Pairs directly with [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe), shelved `p298`, which filters by Profile templates |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **`BSD-3-Clause`** *(**payload**: `LICENSE.txt`, 2.01 KB — sidebar is **unlabelled**)* | 3 | 2 | 🔴 **2 087** | `master` | **QTI 2.1 delivery engine + JQTI+ Java library + MathAssess extensions.** By far the deepest QTI implementation on this file. 🔴 **Pick this fork, NOT the 68★ upstream** — see the inverted gate below |
| [`S4-NetQuest/react-scorm-provider`](https://github.com/S4-NetQuest/react-scorm-provider) | 🟢 `MIT` *(sidebar)* | **67** | 23 | 19 | `master` | React components wrapping the **SCORM API**. 🟢 **The first SCORM row in this base.** 19 commits against 67 stars — a small, finished adapter, which is what this layer should look like |
| [`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti) | 🟢 `MIT` *(sidebar)* | 4 | 1 | 🔴 **794** | `master` | **QTI 2.1, 2.2 AND 3.0** players plus a bidirectional **QTI ↔ PIE** transform framework, with CLI, web app and IMS Content Package support. ⚠️⚠️ **Its own README: pre-1.0, "not fully conformant or certified", and do not use for untrusted or high-stakes delivery without a backend-authoritative integration.** 🔴 **Never brief this as exam-grade; brief it as the migration tool it is** |
| [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) | 🟢 `MIT` *(sidebar)* | 2 | 0 | 102 | `main` | **Markdown → QTI 3.0 XML packages**, TypeScript CLI on npm, manifest-driven ordering/IDs/points. 🟢 **The authoring half of the QTI layer `p298` left open** — it had armed playback and packaging only |
| [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | 🟢 `MIT` *(sidebar)* | **0** | **0** | 47 | `main` | QTI 3.0 item XML → **HTML**, with scoring, report and explanation rendering and response-to-prompt binding. 🔴 **Zero stars, zero forks, 47 commits** — the same shape as `Kennisnet/php-qti3` and the fourth confirmation that stars misrank substrate |
| [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground) | 🟢 `MIT` *(sidebar)* | 4 | 0 | 167 | `main` | Web app to **view, edit and live-preview QTI 3.0 XML** in a split pane. 🔵 The one row in this layer aimed at a **human author** rather than a runtime — useful in a workshop, not in a pipeline |
| [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert) | 🟢 `Apache-2.0` *(sidebar)* | 22 | 6 | 42 | `main` | Converts a **Canvas QTI export package** to **JSON or Word (.docx)**. 🟢 **The only row on this file that reaches backwards into a vendor's export format** — which is the format a migration engagement is actually handed |
| [`examplary/qti`](https://github.com/examplary/qti) | 🟢 `MIT` *(sidebar)* | 1 | 0 | 39 | `main` | TypeScript toolkit building **and** parsing **QTI 3.0 and 2.1** packages, manifests, items, tests and stimuli, with automatic version detection. 🔴 **Bare-name collision with [`instructure/qti`](https://github.com/instructure/qti), already shelved — and they are NOT the same thing.** See the gate note |
| [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | 🟢 `MIT` *(sidebar)* | 3 | 1 | 88 | `main` | `@ae-studio/qti-renderer` — framework-agnostic QTI 3.x item renderer with response processing and feedback. ⚠️⚠️ **Boundaries from its own README: NO scoring, single items only (no test structure), `choice-interaction` ONLY, partial expressions, no adaptive behaviour, and MathJax must be supplied by the host.** 🔴 Narrower than [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player); shelve both, sell that one |
| [`raccoongang/edx_xblock_scorm`](https://github.com/raccoongang/edx_xblock_scorm) | 🟢 `Apache-2.0` *(**payload**: `LICENSE`, 11.1 KB — sidebar is **unlabelled**)* | 32 | 🔴 **65** | 49 | `master` | **SCORM 1.2 and 2004 inside Open edX** as an XBlock, Studio-editable, reporting scores and state to the progress tab. 🔴 **ARCHIVED `2023-11-27`** — read it as a pattern, not a dependency. 🔵 **65 forks against 32 stars**: the deployment signature again, and the strongest case yet that an archived repo can still be the live one in practice |
| [`php-xapi/client`](https://github.com/php-xapi/client) | 🟢 `MIT` *(sidebar)* | 23 | 11 | 137 | `0.7` *(branch read)* | **xAPI client for PHP** via Composer. 🟢 Puts the xAPI boundary in the runtime **Moodle and Tsugi already are** — the same argument `p298` made for `1EdTech/lti-1-3-php-library` |
| [`php-xapi/model`](https://github.com/php-xapi/model) | 🟢 `MIT` *(sidebar)* | 3 | **8** | 340 | `3.x` *(branch read)* | xAPI **model classes** under the client above. Forks (8) exceed stars (3) again. 🔴 **Neither `php-xapi` repo exposes a default branch on its page** — both were read on the branch GitHub served; cite the branch when you pin |
| [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) | 🟢 `MIT` *(sidebar)* | 7 | 0 | 27 | `main` | A **Laravel** Learning Record Store package — and 🟢 **the only row in this base that names `cmi5`**, serving `/api/cmi5/**` with `x-experience-api-version: 1.0.3`. 🔵 The permissive, embeddable alternative to standing up [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) beside a PHP application |

### 🔴 The identity gate inverted: this pass the LOW-star fork is the correct slug

`p298`'s gate replaced a 3★ copy with its 138★ canonical original and published the rule. 🔴 **`p299`
found the case that runs the other way, and a star test alone gets it wrong:**

| | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks) *(upstream)* |
|---|---|---|
| stars / forks | 3 / 2 | 🟢 **68** / **55** |
| commits | 🟢 **2 087** | **2 073** |
| description | the engine, plainly | 🔴 **"This project will be closed in early 2023!"** |
| README | — | 🔴 **"no longer supported and is going to be closed"** |
| verdict | 🟢 **SHELVE THIS ONE** | 🔴 abandoned |

🔵 **The fork carries fourteen commits the canonical upstream never got, and the upstream announces
its own death in its description.** 🟢 **So the gate's test is not "prefer the canonical slug" — it is
"prefer the slug where the history continues."** Stars measure the past; the commit delta and the
description measure whether anyone is still there. `p298`'s substitution was right for the reason it
gave; **its rule was one measurement short.**

🟢 **And the gate's other firing SAVED a row rather than rejecting one.** `examplary/qti` tripped a
bare-name check against the shelved `instructure/qti`, and the two are unrelated: **TypeScript
building QTI 3.0/2.1 packages** against **a Ruby gem parsing QTI 1.2/2.1**. Different runtime,
different QTI generations, different direction of travel. 🔴 **A pass that skipped the name as a
duplicate would have lost the only permissive QTI 3.0 *packaging* row in TypeScript.** The gate has
now fired four times in three passes: twice to reject (`p297`, `p298`), once to reject here
(`ashleycribb/learnmcp-xapi`, a **declared fork** of the already-shelved `DavidLMS/learnmcp-xapi`),
and **once to admit.**

### 🔴 An unlabelled licence sidebar has at least FOUR causes, and they point to opposite decisions

`p298` registered the rule *"treat an unlabelled sidebar as a question about which repository you are
on."* 🔴 **Five unlabelled sidebars this pass, and only one of them was that question:**

| repo | what the bare `License` sidebar actually meant | consequence |
|---|---|---|
| `raccoongang/edx_xblock_scorm` | 🟢 a **standard `Apache-2.0`** payload, simply unclassified by GitHub | **promoted** |
| `OpenOLAT/qtiworks` | 🟢 a **`BSD-3-Clause`** payload in `LICENSE.txt`, not `LICENSE` | **promoted** |
| `1EdTech/caliper-js-example` | 🔴 **`LGPL-3.0`** — *and the org listing labelled it while the sidebar did not* | **rejected** |
| `1EdTech/caliper-spec` | 🔴 **no `LICENSE` file at that path at all** (`404`); org listing says `Other` | **rejected** |
| `ashleycribb/learnmcp-xapi` | 🔴 licence **only in the README**, on a declared fork of a shelved repo | **rejected** |

🔴 **Two of the five were permissive and two were copyleft. A scanner that treats the unlabelled
sidebar as a single signal gets half of them wrong in both directions.** 🟢 **The rule that survives:
an unlabelled sidebar is a question about WHERE THE GRANT LIVES, and only a payload read answers it.**
🔵 **And a new surface is now on the record:** `github.com/orgs/<org>/repositories?q=` **classifies
licences the repository's own sidebar leaves bare** — same repository, same payload, two GitHub
surfaces, two different verdicts. Read the org listing when the sidebar is silent; read the payload
before you shelve.

### 🔴 Standing action for the next pass — `ACTION PG-4`

**455 of 525 permissive orphans remain unshelved, row-grade** — and that number is now measured
correctly, which is itself the instruction:

1. 🔴 **A plain text diff of the list against the shelf files is WRONG, and it has been wrong for
   three passes.** `p299` measured it: **only 70 slugs sit on an actual table row**, **11 appear ONLY
   in shelf-file prose**, and **444 are absent entirely**. The 11 are counted as *shelved* by any
   naive match — **and five of them are the very slugs `ACTION PG-3` named**, because `p298` wrote
   them into an instruction. 🟢 **Match only lines whose first non-space character is a pipe.**
2. **Take ~12 from the layers still at zero rows**, and the three now worth naming are
   **credentialing** ([`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator),
   [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE)), **the remaining xAPI movement layer**
   (`pelotech/xapi-lrs`, `xapi-labs/xapi-cli`, `adlnet/xAPI-Spec`), and **SCORM packaging**
   (`sr258/scorm-h5p-wrapper`, `dhodges47/SCORM-LearningManagementSystem`).
3. 🔵 **`p298` reported 21 bare-name collisions; the count is 20**, and it is 20 both before and after
   case-folding, so the three case-only duplicates are not the cause. Resolve them by **owner**, never
   by name — `canvas-mcp` is still ten owners deep.
4. 🟢 **Read the payload whenever the sidebar is bare, and read the org listing too.** This pass turned
   two unlabelled sidebars into shelvable permissive rows and two into rejections. **Three of the
   fifteen admissions above would have been lost to a sidebar-only read.**


## 🟢 Pass 298 — THIRTEEN NEW PERMISSIVE SUBSTRATES, AND THEY ARM AN INSTRUCTION THIS BASE HAS GIVEN FOR 297 PASSES WITHOUT THE CODE TO FOLLOW IT

⏱️ **Twentieth pass of `2026-10-18`.** Evidence:
[`p298-promotion-gap.2026-10-18-p298.tsv`](../evidence/p298-promotion-gap.2026-10-18-p298.tsv) ·
[`p298-channel-control.2026-10-18-p298.tsv`](../evidence/p298-channel-control.2026-10-18-p298.tsv) ·
[`p298-identity-gate.2026-10-18-p298.tsv`](../evidence/p298-identity-gate.2026-10-18-p298.tsv).

🟢 **`ACTION PG-2` discharged.** `p297` ordered the next pass to take **~12 from the layers still at
zero or one row** — assessment integrity, retention/early-warning, student-records interop — and to
**skip the adapter cluster entirely**. `p298` read **fourteen slugs**, admitted **thirteen**, rejected
**one**, and **read not a single adapter**. Every read is first-hand at `github.com` rendered HTML.
**All thirteen land on this file. None belongs on [`agents/top.md`](../agents/top.md)** — and that is
a finding, not an omission (see that file's `p298` note).

### 🔴 The finding: this base's oldest piece of advice was unarmed

Every pass that has touched [`verticals/solutions.md`](../verticals/solutions.md) has told a client the
same thing about a copyleft LMS: **"integrate, do not fork."** Reach Moodle (GPL-3.0), Canvas
(AGPL-3.0) and Open edX (AGPL) **at the integration boundary** and keep the studio deliverable on the
permissive side of it. 🔴 **The advice was correct and the toolkit for it did not exist on these
shelves.** Before this pass:

| boundary layer | rows before `p298` | added `p298` |
|---|---|---|
| **LTI tool provider** | **1** — [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (Apache-2.0, PHP framework) | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) · [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) · [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) · [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) |
| **QTI — assessment items** | 🔴 **0** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) · [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) · [`instructure/qti`](https://github.com/instructure/qti) |
| **OneRoster — rostering client/server** | 🔴 **0** *(prose only, via Ed-Fi)* | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) · [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) |
| **xAPI — statement movement** | 1 store *(`lrsql`)* + 1 spec | [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) |
| **integrity — AI-text detection** | 🔴 **0** | [`baoguangsheng/fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) |
| **integrity — proctoring** | 🔴 **0** | [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) ⚠️ boundary in the row |
| **integrity — code similarity** | 1 *(`dolos`)* | [`automoss/automoss`](https://github.com/automoss/automoss) |
| **Caliper — analytics events** | 🔴 **0** | 🔴 **still 0.** Declared, not glossed |

🔵 **The language coverage is the point, not the row count.** The boundary was reachable in **PHP
only**. It is now reachable in **PHP, Node/TypeScript, Python, Go and Ruby**, plus **JupyterHub** as a
first-class tool provider. A studio can now meet an AGPL LMS from whatever runtime the engagement
already uses, instead of standing up PHP to do it.

### 🟢 The thirteen rows, read `2026-10-18`

| repo | licence (read `2026-10-18`) | stars | forks | commits | branch | layer, and the boundary in the row |
|---|---|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 `Apache-2.0` *(sidebar)* | **373** | 86 | **575** | `master` | LTI 1.3 in TypeScript — launches, Deep Linking, AGS, NRPS, Dynamic Registration. **The highest-adoption permissive LTI row this base has.** README says *"educational environments"* and never *students* |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 `Apache-2.0` *(sidebar)* | 124 | **107** | 110 | `master` | LTI 1.3 from **the standards body itself**. 🔵 **107 forks against 124 stars** — the deployment signature this file named on Submitty and `gegok12`: this is a library institutions *run*, not one developers *star* |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 `MIT` *(sidebar)* | 138 | 84 | 178 | `master` | LTI 1.3 Advantage in Python, **Django + Flask adapters**. 🔴 **This is NOT the slug `p989` named** — see the identity-gate note below |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **`BSD-3-Clause`** *(sidebar)* | 73 | 56 | **523** | `main` | Makes **JupyterHub** an LTI Tool Provider, **LTI 1.1 and 1.3**, naming Canvas, Moodle, Open edX, Blackboard. 🟢 It sits directly under [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) (8.4k★), already the highest-adoption permissive row on this file |
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 `MIT` *(sidebar)* | 30 | 6 | **596** | `main` | **The first QTI row in this base.** Browser component that renders 1EdTech **QTI 3** items, saves item state and runs response scoring. 596 commits against 30 stars |
| [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | 🟢 `MIT` *(sidebar)* | **0** | **0** | **255** | `main` | QTI 3.0 **packages**, tests and items in PHP: import, export, validate, parse, generate, edit-in-package. 🇳🇱 **Kennisnet** is the Dutch public-education ICT foundation. 🔴 **Zero stars, zero forks, 255 commits** — the clearest case on this file for the rule below |
| [`instructure/qti`](https://github.com/instructure/qti) | 🟢 `MIT` *(sidebar)* | 8 | 10 | 174 | `master` | Ruby gem parsing **QTI 1.2 and 2.1** — the legacy item formats a migration actually meets. 🔵 **Authored by Instructure under MIT while [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) is AGPL-3.0**: the vendor's own licence split is where the integration boundary physically is |
| [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | 🟢 `Apache-2.0` *(sidebar)* | 17 | 9 | 310 | `main` | **LRSPipe** — one-way xAPI statement forwarding between Learning Record Stores, filtered by xAPI **Profile templates/patterns**, resumable via file system or Redis. The sibling of [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql), already shelved: `lrsql` stores, `xapipe` **moves** |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 `Apache-2.0` *(sidebar)* | 6 | 5 | 151 | `main` | Serves a **OneRoster 1.2** API from an **Ed-Fi ODS**; Data Standards **4.0, 5.x, 6.1**; `classes`, `courses`, `users`, `schools`. 🟢 **This is the bridge for `Gap 309`** — the register records OneRoster as *absent* from DMS v8.0 while native OneRoster 1.2 shipped in ODS/API 7.3.2 |
| [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) | 🟢 `MIT` *(sidebar)* | 8 | 1 | 237 | `master` | OneRoster API server in **Go** on MongoDB. 🔵 It **adds `PUT` create/update/upsert beyond the spec's read-only `GET` surface** — useful and non-standard, so say which one you are selling. 🔴 **Bare-name collision:** `fffnite/go-oneroster` is also on `p989`'s list and was **not** read |
| [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) | 🟢 `MIT` *(sidebar + README)* | **633** | **351** | 86 | `master` | Vision **+ audio** proctoring: eye tracking, mouth-open, person and phone detection, head pose, face spoofing, speech transcription against a question paper. ⚠️⚠️ **Three boundaries, all from its own README: face spoofing *"accuracy is not good currently"*, speech-to-text *"might not work well for all dialects"*, and the facial-landmark model was trained on NON-COMMERCIAL datasets.** 🔴 **Never brief this as a shippable proctoring product; it is a reference implementation of the capability** |
| [`baoguangsheng/fast-detect-gpt`](https://github.com/baoguangsheng/fast-detect-gpt) | 🟢 `MIT` *(sidebar)* | **436** | 85 | 76 | `main` | Zero-shot detection of machine-generated text via **conditional probability curvature**, **ICLR 2024**. The highest-adoption permissive row in the integrity layer and **the only one with a peer-reviewed method behind it.** 🔴 README names no education use |
| [`automoss/automoss`](https://github.com/automoss/automoss) | 🟢 `MIT` *(sidebar)* | 157 | 26 | **791** | `main` | Local web app automating **Stanford MOSS** code-similarity runs across a set of assignments. Composes with [`dolos`](https://github.com/dodona-edu/dolos): **two independent similarity engines on one submission set is a defensible integrity finding; one is an accusation** |

### 🔴 The identity gate changed one row's owner, and the licence gate is the reason

`p989`'s list named **`ucfopen/pylti1.3`**. `p298` read it and **did not shelve it.**

| | `ucfopen/pylti1.3` | `dmitry-viskov/pylti1.3` |
|---|---|---|
| sidebar licence label | 🔴 **a `License` link with NO label** | 🟢 **`MIT license`** |
| root `LICENSE`, line 1 | `MIT License` | — |
| copyright line | 🔴 **`Copyright (c) 2019 Dmitry Viskov`** | *(the same holder, on his own repository)* |
| stars / forks / commits | **3** / 1 / 180 | **138** / **84** / 178 |

🔴 **The list named the three-star copy, not the 138-star original** — and the copy carries the
original author's copyright line verbatim. GitHub flags neither as a fork, so this is a
**re-publication, not a fork relationship**, and no banner would have warned a reader.

🔵 **The new licence-gate shape, and it is one this base has not recorded: GitHub's licence
classification is not a property of the payload.** `p267`'s signal — *a `License` link with no
label* — has always been read as a property of the **file**. Here the **same grant, same holder, same
name**, is **classified on the original and unclassified on the copy.** A scanner reading sidebars
would grade the copy *unlicensed* and the original *MIT*. 🟢 **The rule: an unlabelled sidebar is a
question about the repository, not a verdict on the grant — and the answer may be that you are looking
at the wrong repository.**

### 🔴 What the star column would have done to this batch — a third confirmation, and now it is a rule

`p296` measured it, `p297` confirmed it on a wider sample, `p298` confirms it a third time and the
spread is again extreme:

- [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) — **0★, 0 forks, 255 commits**, and it
  is the only QTI 3 **packaging** library on this file. A star filter at `>0` deletes it.
- [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) — **107 forks
  against 124 stars.** Forks exceeding stars, from the standards body itself.
- [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) — **633★**, the
  second-highest in the batch, and **its own README disqualifies two of its five subsystems.**

🟢 **Promoted from finding to standing rule on this file: rank substrate rows by commits, by forks
against stars, and by named deployment. Stars rank the developer audience, and on this layer the
developer audience is not the buyer.** ⚠️ `p295`'s warning still binds: these are **rendered** reads
and are **not** monotonic.

### 🔵 The channel, with a negative control that is now decisive

`curl -sI` returned **`HTTP/1.1 200 Connection Established` on 4 of 4** probes — **including an
invented hostname and including `api.github.com`.** 🔴 **That line is the proxy's `CONNECT`
handshake, not an origin status**, so under `-I` a `200` here licenses **no existence claim** —
strictly stronger than `p294`'s rule, which was written about a `403`. A full `GET` returned **`403`
with a `378`-byte body that is byte-identical for a real repository and a fabricated one.**

🟢 **What is new is that `api.github.com` answered in words.** Its `403` body reads: *"GitHub access
to this repository is not enabled for this session. Use add_repo to request access."* 🔵 `p294`-`p297`
inferred *"there is no `api.github.com` channel"* from status codes alone. **The inference was right
and the mechanism is now documented: this is session repo-scoping, not rate limiting and not repo
absence.** All fourteen reads are `WebFetch` over rendered `github.com` HTML — **sidebar-grade, not
payload-grade**, except `ucfopen/pylti1.3`, whose root `LICENSE` was read at payload (1.04 KB) because
the gate demanded it.

### 🔴 Next batch for this file — `ACTION PG-3`

**456 of the 528 permissive orphans remain unshelved.** `p298` adds a correction to `p297`'s
partition rule: **cluster SIZE and cluster SATURATION are different measurements, and `p297`
conflated them.** The interop cluster `p298` worked is **~60 slugs — three times the adapter
cluster — and it stood at zero rows.** The test is **rows-on-shelf against cluster-size**, never
size alone.

The next pass should take ~12 from:

1. **Caliper analytics** — 🔴 still **0 rows**, and it is the third 1EdTech standard after LTI and
   QTI. Search the list for `caliper`.
2. **SCORM tooling** — 3 mentions, 1 row (`scorm-again`); the list carries
   `S4-NetQuest/react-scorm-provider`, `raccoongang/edx_xblock_scorm`, `sr258/scorm-h5p-wrapper`.
3. **QTI conversion** — `rolfis/qti-convert`, `metyatech/markdown-to-qti`,
   `metyatech/qti-html-renderer`: the **authoring** half of the layer `p298` opened at the
   **playback** half.
4. 🔴 **And resolve the three case-duplicate slugs and the 21 bare-name collisions `p298` measured
   before reading any of them** — `canvas-mcp` alone has **ten distinct owners** on this list.

## 🟢 Pass 297 — NINE NEW PERMISSIVE SUBSTRATES, AND THEY ARE ALL ONE THING: THE LAYERS BETWEEN THE AGENT AND THE INSTITUTION

⏱️ **Nineteenth pass of `2026-10-18`.** Evidence:
[`p297-promotion-gap.2026-10-18-p297.tsv`](../evidence/p297-promotion-gap.2026-10-18-p297.tsv) ·
[`p297-channel-control.2026-10-18-p297.tsv`](../evidence/p297-channel-control.2026-10-18-p297.tsv).

🟢 **This file grew by NINE rows and not one came from a search.** `p296` left `ACTION PG` — work
[`p989`'s orphan list](../compose/code/p989-sha-identity-fork/promotion-gap-permissive-orphans.txt)
before running the mandated leg. `p297` ran a named batch of twelve out of it: **nine admitted here,
two onto [`agents/top.md`](../agents/top.md), one rejected outright.**

🔵 **The nine are not a miscellany. Sorted by what they sit between, they are one finding:** this
base had shelves for the **agent** (42 rows) and for the **platform** (Moodle, Canvas, Open edX,
Kolibri) and **almost nothing for the layers in between** — the ones an institution actually
contracts about.

| layer | rows before `p297` | added `p297` |
|---|---|---|
| **evaluation** | 1 *(`pedagogy-benchmark`, `p296`)* | [`inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) · [`edu-qurating`](https://github.com/AI-for-Education/edu-qurating) · [`voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework) |
| **curriculum standards interop** | 🔴 **0** | [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) |
| **credentialing** | 🔴 **0** | [`digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) |
| **governance / audit** | 🔴 **0** | [`agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) |
| **autograding platform** | 2 *(`Autolab`, `Artemis`)* | [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) · [`google/prog-edu-assistant`](https://github.com/google/prog-edu-assistant) ⚠️ archived |
| **language substrate** | several *(regional)* | [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2) |

🔴 **Two rows on this file are deliberately NOT education repositories, and both say so in their own
cell.** [`inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) (3.0k★, **8 033 commits**, UK AI
Security Institute) and
[`agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) (6.4k★, 2 880
commits) **mention neither education nor teaching nor students in their READMEs.** They were kept off
the agents shelf on `p293`'s README test and admitted here as **substrates**, because the two things
every regional leg names as the binding constraint — *documented evaluation* and *auditable
governance* — had **zero rows** on any shelf in this base. The boundary is in the row; a reader
cannot pick either up believing it was built for a classroom.

⚠️ **One row is archived and is shelved anyway, with the date in the cell.**
[`google/prog-edu-assistant`](https://github.com/google/prog-edu-assistant) was **archived by its
owner on `2025-07-23`** and is read-only. Apache-2.0 is irrevocable and the notebook-autograding
shape has not moved, so it is a **complete worked reference** for a client teaching Python in Colab —
and it must **never** be briefed as maintained software.

### 🔴 What the star column would have done to this batch, again

`p296` measured that ranking these rows on stars inverts them. `p297` is a second confirmation from a
wider sample, and the spread is now extreme:

- [`voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework) — **1★**, and it is the only instrument in this base that measures **child** speech recognition, which every literacy pattern here silently assumes works.
- [`edu-qurating`](https://github.com/AI-for-Education/edu-qurating) — **3★ / 277 commits**, and it scores teaching material on **pedagogical quality** rather than readability.
- [`agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) — **6.4k★**, and it is **not an education repository at all.**

🔵 **The rule this file now states plainly: on the substrate layer, stars measure the size of the
repo's developer audience, not its usefulness to an education engagement.** The three most
engagement-critical rows added this pass have **5 stars between them.**

### 🔵 The channel

`curl -sI` over `github.com`: **403 on 4 of 4**, **including an invented hostname that returned the
identical 403** — so `p294`'s rule stands, a `403` **licenses no existence claim**, and there is no
`api.github.com` path. All twelve reads are `WebFetch` over rendered `github.com` HTML (sidebar/About
licence label plus README body). Star and fork figures are **rendered** reads and `p295` showed they
are **not monotonic**.

### 🔴 Next batch for this file — `ACTION PG-2`

**481 of the 528 permissive orphans are still unshelved**, but `p297` measured that they are **not
equally worth reading**: the densest cluster (~20 LMS-integration MCP adapters) is **already covered
four times over** on the agents shelf. The next pass should take ~12 from the layers still at **zero
or one row** — assessment integrity, retention/early-warning, and **student-records interop**, where
`1EdTech` has further repositories on the list (`lti-1-3-php-library`, `OpenCASE`'s siblings) — and
**skip the adapter cluster** unless a candidate reaches a system no shelved row reaches.

## 🟢 Pass 296 — THREE NEW PERMISSIVE SUBSTRATES, TWO SELF-CORRECTIONS, AND NOT ONE OF THE FIVE WAS A DISCOVERY

⏱️ **Eighteenth pass of `2026-10-18`.** Evidence:
[`p296-promotion-gap.2026-10-18-p296.tsv`](../evidence/p296-promotion-gap.2026-10-18-p296.tsv).

🔴 **The mandated vertical/foundation leg is nil again. This file grew by three rows anyway**, because
`p296` stopped searching and worked
[`p989`'s orphan list](../compose/code/p989-sha-identity-fork/promotion-gap-permissive-orphans.txt)
instead — ~500 slugs that appear in this repository with a permissive grant **and appear on no
shelf**. `p989` published that list on `2026-10-10` and no pass had promoted a row out of it.

| new row | grade read `p296` | what it closes |
|---|---|---|
| [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) | 🟢 MIT, sidebar · **3 015 commits**, `develop` | 🆕 dropout early-warning with a named deployment outcome |
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 🟢 Apache-2.0, sidebar + README · 450 commits | the on-prem inference runtime every sovereign pattern hand-rolled |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT, sidebar · 12★ | **the pedagogical-evaluation gap**, with a Chilean MINEDUC question bank |

🔵 **Three of the five are more than 2 000 commits deep and none has more than 352 stars.** On this
file the star column has been doing work it cannot do: `student-success-tool` at **8★** carries
`3 015` commits and a reported graduation gain at a named college. **Rank these rows by commits and
by named deployment, not by stars** — and see the `p296` note in
[`agents/top.md`](../agents/top.md) for why the star column misled this base's own agents shelf.

⚠️ **One row is deliberately shelved at a weaker grade than the rest.** `autolab/Autolab` declares
Apache-2.0 **in README prose only**, and its sidebar shows a License link with **no licence name** —
this base's `p267` signal. It is shelved because `808★ / 2 179 commits` is too useful to omit, and it
is marked `README-ONLY` because the grant was not read. **Request the payload before it ships.**

## 🟢 Pass 294 — two NEW permissive substrates read at pins, and the boundary is in the row

⏱️ **Sixteenth pass of `2026-10-18`.** Evidence:
[`p294-pin-grant.2026-10-18-p294.tsv`](../evidence/p294-pin-grant.2026-10-18-p294.tsv).

🔴 **No new education foundation for the fifteenth pass running.** What the mandated ERP/CRM leg
and the agent leg returned were **general-purpose** repositories with real permissive grants. They
are shelved here as *substrates* — `p293`'s precedent for `tokenaii/Horus-Taleeq-0.2B-Base` — with
their disqualification stated in the row, because a substrate mis-shelved as an education platform
is the error this file exists to prevent.

| Repo | Grant, read FIRST-HAND at the pin | Pin | What it is | 🔴 Boundary |
|---|---|---|---|---|
| [`ONLYOFFICE/CommunityServer`](https://github.com/ONLYOFFICE/CommunityServer) 🆕 | **Apache-2.0** · `LICENSE` `200` · **11 357 B** · sha256₁₂ **`c71d239df917`** · title @33 · no dual grant | `fe1fa7babd093969e939ba6ff45a9fee1299dc93` (`refs/heads/master`, from the symref) | "ONLYOFFICE Groups" — document management, project tracking, collaboration for an institution | **0 education tokens in 6 262 B of README.** Not an LMS, not a CRM, not an ERP. A collaboration layer an engagement can *put under* an education product |
| [`ChurchCRM/CRM`](https://github.com/ChurchCRM/CRM) 🆕 | **MIT** · `LICENSE` `200` · **1 076 B** · sha256₁₂ **`82ad0787803a`** · title @4 · no dual grant | `bcf15df5de17cb9907f8db94fe44893a93bf72c4` (`refs/heads/master`) | PHP membership management: members, groups, events, finances | **0 education tokens in 5 703 B of README.** Shelved only as the **closest permissive analogue** to a member-institution CRM — the shape an education CRM would take, not an education CRM |

🔵 **Why these are worth a row at all.** The ERP/CRM leg has returned nil for fifteen passes, and
the standing reason is that the education verticals are **copyleft** — OpenEduCat `LGPL-3.0`,
Moodle `GPL-3.0`, Open edX `AGPL-3.0`, Frappe CRM `AGPL-3.0`. A studio that needs a permissive
base has to assemble one. 🔴 **Stated as a bound, not a recommendation:** neither row is an
education system, and calling either one would be the `p286` category error.

### 🟢 The two the index already held, re-read anyway

| Repo | Grant at the pin | Why it is here and not on [`agents/top.md`](../agents/top.md) |
|---|---|---|
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | **MIT** · **1 070 B** · sha256₁₂ **`821556e63367`** · title @0 · pin `9e01b44dd23978f9ff40b7837467f3a9f1582130` | **0 education tokens in 16 924 B.** A general local-first agent. 🔴 `CARRIED` since `p275` — and `p294` nearly re-opened it as new by querying the index with a **guessed** slug (`NousResearch/Hermes`, which is `ABSENT-OR-PRIVATE`) |
| [`MadsLorentzen/ai-job-search`](https://github.com/MadsLorentzen/ai-job-search) | **MIT** · **1 071 B** · sha256₁₂ **`accbf0accb87`** · title @0 · pin `30158c0493ae8ae1610769955ad04b189049afe8` | **3 education-ish tokens in 34 105 B** (1× *course*, 2× *education*). Careers tooling. 🔴 `CARRIED` |

### 🟢 `HKUDS/DeepTutor`'s grant has not moved

Re-read at a **new** pin, `6cf793bd868ba5ecbe64722936d4be8fab5a01df`: **Apache-2.0**, `11 408 B`,
sha256₁₂ **`cd2f54e1e506`** — 🟢 **byte-identical to the blob already on record.** Same payload at a
different commit, so the row keeps its grade without re-grading.

🔵 **The channel note that makes all of the above reproducible.** `github.com` answers **`403`** to
curl in this environment; every grant in this section was nonetheless read through
**`raw.githubusercontent.com`**, which answers `200`. 🔴 A refusal on one host is not evidence about
a repository — see [`p798`](../compose/code/p798-proxy-refusal-ledger/README.md), which `p294`
extended and wired into `make hooks` for exactly this reason.

## 🟢 Pass 293 — ONE NEW ROW, and it is the first EMEA-origin permissive grant this base has read rather than been told about

⏱️ **Fifteenth pass of `2026-10-18`.** Evidence:
[`p293-websearch.2026-10-18-p293.tsv`](../evidence/p293-websearch.2026-10-18-p293.tsv) ·
[`p293-slug-oracle.2026-10-18-p293.tsv`](../evidence/p293-slug-oracle.2026-10-18-p293.tsv).

🔴 The mandated legs returned their **nineteenth** (agents), **tenth** (trending) and
**fourteenth** (permissive vertical) consecutive nils. All twelve legs — four mandated, four
regional, four directed — are written out with what each returned in the evidence TSV.

### 🟢 ADMITTED: `tokenaii/Horus-Taleeq-0.2B-Base` — as a SUBSTRATE, with its boundary in the row

`p292` registered this as ranked item 1 — *"recover the slug, then read the grant at a pin"* —
with the posture `CANDIDATE-ATTRIBUTED` and four refused verification channels. 🟢 Discharged.

| field | value, first-hand |
|---|---|
| slug | [`tokenaii/Horus-Taleeq-0.2B-Base`](https://github.com/tokenaii/Horus-Taleeq-0.2B-Base) |
| alias | [`tokenaii/Horus-Taleeq-0.2B`](https://github.com/tokenaii/Horus-Taleeq-0.2B) — 🟡 **same HEAD, one tree under two names** (see below) |
| default branch | `main`, read from the **symref**, not inferred |
| pin | `f7a7700289791a9c114ab038af73b4d45c17c7e7` |
| grant | 🟢 **MIT · `GRANTED-AT-PIN`** — `LICENSE` **`200`**, **1 080 B**, sha256₁₂ **`96c22722c817`**, family by the shared `p228`/`P237` classifier, **title line @0**, no dual-grant preamble |
| README channel | 🟢 **`AGREE`** — the README states MIT too. Posture **`BUILD-ON`** (`p288`) |
| what it is | Arabic-only **small language model**, decoder-only causal Transformer, **exactly 199 916 160 parameters**, 24 layers, hidden 640, 10 heads, **2 KV heads (GQA)**, 128 000-token SentencePiece vocabulary, 4 096-token context, RoPE θ=1 000 000, tied embeddings, bf16 |
| ledger | **6 000 308 224** tokenizer IDs (3 616 305 152 initial + 2 384 003 072 raw continuation); core pretraining **28 h 40 m 20.604 s** |
| shipped with it | 🟢 **training code, training stages, data policy and a compute profile** — `configs/`, `docs/CURRENT_MODEL.md`, `TRAINING_STAGES.md`, `DATA_SOURCES.md`, `DATA_AND_REPRODUCIBILITY.md`, `COMPUTE_PROFILE.md` |
| holder | **TokenAI** and **Assem Sabry** (from the `LICENSE` copyright line, not from press) |

🔵 **Why it earns a row here and not on the agent shelf.** This layer had **no EMEA-origin
permissive model**, and an Arabic-only base model released *with its corpus policy and training
code* is exactly the substrate an Arabic-medium tutoring or assessment build has to supply from
somewhere — the gap `P39`'s ministry assistant and `P40`'s two-corpus tutor both open.
🔴 **And the boundary belongs in the row, because the README states it plainly:** this is a
**base-model development release**, *"not a finished production chat model"*, with **no
instruction tuning and no safety alignment**. A studio adds both. 🔴 It also **does not claim
full corpus reproducibility** — the historical raw streams and the cleaned Parquet export are
not identical, and the repo says so itself.

🔴 **Zero education claims in it.** The one `teacher` hit is *"teacher outputs"*, i.e.
distillation. 🔵 It is a substrate, filed as a substrate. `p286`'s rule, applied to a candidate
this base wanted to be more than it is.

### 🟡 NOT admitted: the rest of the family, and each for a different measured reason

| slug | oracle verdict | grant |
|---|---|---|
| [`tokenaii/Horus-Lens-1.0`](https://github.com/tokenaii/Horus-Lens-1.0) | 🟢 `EXISTS-PUBLIC`, pin `86cade44ab562fb929539a482f440aef28ca301c` | 🔴 **`DANGLING-CLAIM`** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` all **`404`** at the pin; README (5 138 B, sha256₁₂ `46be1ff03067`) asserts *"licensed under the Apache License 2.0"*. Posture **`ASK`**. 🔴 And it is a **text-to-image** model fine-tuned from `Tongyi-MAI/Z-Image` — not education, not language |
| `tokenaii/Horus-1.0-4B` | 🔴 `ABSENT-OR-PRIVATE` | press reports MIT; **no GitHub repository under that name**. The search leg places the weights on Hugging Face, which stays unreachable |
| `tokenaii/Horus-Hiero-9B` | 🔴 `ABSENT-OR-PRIVATE` | as above |
| `tokenaii/Horus`, `tokenaii/horus` | 🔴 `ABSENT-OR-PRIVATE` | 🔵 **two of `p292`'s four guesses, now adjudicated as negatives rather than left inconclusive** |

🟡 **The HEAD collision is a finding, not a verdict.** `Horus-Taleeq-0.2B-Base` and
`Horus-Taleeq-0.2B` return the **identical** HEAD `f7a7700289791a9c114ab038af73b4d45c17c7e7`, so
they are one tree under two names, and the shelf carries **one** row — `p283`'s rule, reused
rather than re-invented. 🔵 It also explains the parameter discrepancy the press carried: the
*"older 0.2B repo"* and the base repo are not two repositories with two parameter counts; the
repo says **199 916 160** at this pin and the 204.6M figure belongs to the Hugging Face card.

### 🔵 How the slug was recovered, since the method is the reusable part

🔴 `p292` spent four `git ls-remote` probes on **guessed spellings** and recorded the result as
*"an anonymous credential prompt … INCONCLUSIVE and not a negative"*. 🟢 Calibrated against a
known-real and a known-fake control, that prompt **discriminates** — it is this channel's answer
for *"no repository I will serve you"*, and it is a different string from its answer for *"I
could not reach the host"*. The slug itself came from a **search leg**, in the first result, the
moment one was aimed at the path rather than at the licence.

🟢 Both halves are now an instrument:
[`compose/code/p293-slug-existence-oracle`](../compose/code/p293-slug-existence-oracle/README.md)
— **45 offline controls**, a closed five-token verdict vocabulary, and a calibration pair that
**gates every verdict**. 🔴 Its honest bound is a control: the signature cannot separate *absent*
from *private*, so the token is **`ABSENT-OR-PRIVATE`** and `C9` forbids a bare `ABSENT` from
ever entering the vocabulary.

## 🔴 Pass 292 — NO NEW FOUNDATIONAL ROW for a second pass, and the candidate that would have been the first EMEA-origin one could not be resolved to a slug

⏱️ **Fourteenth pass of `2026-10-18`.** Evidence:
[`p292-websearch.2026-10-18-p292.tsv`](../evidence/p292-websearch.2026-10-18-p292.tsv).

🔴 **No new foundational repository this pass.** The mandated agent leg returned its
**eighteenth** consecutive nil, the trending leg its **ninth** for education, and the vertical
leg its **thirteenth** for a new permissive platform. All eleven legs — four mandated, four
regional, three directed — are written out with what each returned in the evidence TSV.

### 🟡 The candidate, and exactly why it is not a row

**TokenAI (Cairo), the Horus family** — reported `Horus 1.0-4B` **MIT**, `Horus Taleeq 0.2B
Base` **MIT** (Arabic-only, ~6 B Arabic tokens, **shipped with its training code and data
sources**, pretraining-only), `Horus Lens 1.0` **Apache-2.0**, plus two further models with no
stated grant.

🔵 **Why it matters.** This shelf has **no EMEA-origin permissive model row**, and an
Arabic-only base model released with its training corpus is precisely the foundation an Arabic
tutoring or assessment build needs — the layer that `P40`'s two-corpus tutor and `P39`'s
ministry assistant both have to supply from somewhere.

🔴 **Why it is not admitted.** Every grant above is **press-reported, not read.** Four channels,
all closed or inconclusive this pass: `huggingface.co` `403` via curl **and** `ENOTFOUND` via
WebFetch (two distinct egress paths); the one outlet carrying the licence claims `ENOTFOUND`;
`git ls-remote` on four guessed `tokenaii/*` slugs → anonymous credential prompt, **inconclusive
rather than negative**; `raw.githubusercontent.com` `404` on two guessed paths.
🔴 **No source named a repository path**, so the slug itself is unknown and the probe had nothing
correct to ask for. 🟡 Posture **`CANDIDATE-ATTRIBUTED`**. 🔵 `p293`'s top directed leg: recover
the slug, then read the grant **at a pin** — `p291`'s standing method, which works wherever
`raw.githubusercontent.com` answers.

### 🟢 What this layer gained instead

🟢 A **first-party** component rather than a found one:
[`compose/code/p292-decision-evidence-store`](../compose/code/p292-decision-evidence-store/README.md)
— **106 offline controls**, standard library only, no network, no server, wired into
`make hooks`. 🔵 It is the one layer in `P45`-`P49` that no repository on these shelves supplies
after 292 passes of looking, which is exactly why it is the billable half of those engagements.
🔴 It is a reference implementation to adapt, **not a dependency to install**, and it is
tamper-**evident** rather than tamper-proof — control `C18` asserts that limit as a control.

## 🔴 Pass 291 — the foundation layer gained NO NEW ROW, and what changed instead is that an existing row's grant is now verified across **all seven** of its repositories

⏱️ **Thirteenth pass of `2026-10-18`.** Evidence:
[`submodule-pin-grant.2026-10-18-p291.tsv`](../evidence/submodule-pin-grant.2026-10-18-p291.tsv) ·
[`p291-websearch.2026-10-18-p291.tsv`](../evidence/p291-websearch.2026-10-18-p291.tsv).

🔴 **No new foundational repository this pass, and the reason is the finding.** The mandated
agent leg returned its **seventeenth** consecutive nil and the trending leg its **eighth** for
education; both returned the same agent-engineering curricula they have returned since `p275`.
🔵 A filler row would be worse than the gap: `p288` set that precedent and it holds.

🟢 **What did change is verification depth, not breadth.** The `iblai` configuration set
already on these shelves was carried on **2 of its 7** repositories. All seven are now read
**at the commit the superproject pins** — `GRANTED-AT-PIN`, `MIT`, one root `LICENSE` each,
every payload byte-identical (1 063 B, sha256₁₂ `f1269b7b2313`):

| repository | pinned gitlink | files at the pin | grant |
|---|---|---|---|
| [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) | `1a2d898bbd04` | 90 | 🟢 MIT |
| [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | `54ee9d91eecd` | 79 | 🟢 MIT |
| [`iblai/enterprise-agents`](https://github.com/iblai/enterprise-agents) | `7f00879a9f57` | 77 | 🟢 MIT |
| [`iblai/government-agents`](https://github.com/iblai/government-agents) | `fbf903250c96` | 77 | 🟢 MIT |
| [`iblai/legal-agents`](https://github.com/iblai/legal-agents) | `b059cd452bf3` | 75 | 🟢 MIT |
| [`iblai/financial-services-agents`](https://github.com/iblai/financial-services-agents) | `6ea18f015b1e` | 78 | 🟢 MIT |
| [`iblai/medical-healthcare-agents`](https://github.com/iblai/medical-healthcare-agents) | `cd0d9fcfa523` | 76 | 🟢 MIT |

🔵 **The technique is the transferable part, and it is cheap.** A submodule's grant does not
have to be read at `HEAD` and then reconciled against the pin:
`raw.githubusercontent.com/<owner>/<repo>/<pinned-sha>/LICENSE` serves the payload **at the
pin**, which is the commit a `--recurse-submodules` clone actually lands on. 7/7 answered
`200`. Any foundational row that is a submodule of something else can be verified this way,
and [`gate-pin-grant`](../compose/code/p291-submodule-pin-grant/README.md) now requires it.

🔴 **A standing caution this pass re-measured, unchanged:** `api.github.com` and `github.com`
HTML both answer `403` from this environment. No star count on this shelf is first-hand.

## 🟢 Pass 290 — the early-warning layer gets its first two foundational rows, and one of them is a US STATE EDUCATION AGENCY's own code

⏱️ **Twelfth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`p290-websearch.2026-10-18-p290.tsv`](../evidence/p290-websearch.2026-10-18-p290.tsv).

🔵 **Why these are foundations and not agent rows.** Neither is an agent and neither wants to
be. They are the **measurement layer** underneath `retention-agent` and
`special-education-agent`: the thing that produces a risk score an agent then has to act on
without treating it as a verdict.

| repo | grant (read from payload) | what it gives you | base for AI? |
|---|---|---|---|
| 🟢 [`cedanl/student-signal`](https://github.com/cedanl/student-signal) | 🟢 **MIT** — root `LICENSE`, **1 078 B**, HEAD `4463e8d17cfb`, sha256₁₂ `2c4289f4e480` | 🇳🇱 Dropout prediction as a **domain library**: `prepare()` cleans and transforms, `rank()` orders students by predicted probability, `evaluate()` reports **precision/recall at multiple invitation thresholds** with a traffic-light status. Bring any sklearn-compatible estimator. **Invitation-rule methodology (Eegdeman, 2022)**. 36 files, Python 3.13+, `uv`, CI/docs/publish workflows, 4 test modules, synthetic demo data committed | 🟢 **yes — the cleanest foundation found for this layer.** It deliberately does NOT choose your model, so the agent layer sits on top without a rewrite |
| 🟡 [`jknowles/EWStools`](https://github.com/jknowles/EWStools) | 🟡 **GPL-3.0 only** — root `LICENSE`, **35 156 B**, sha256₁₂ `65a7aee2cb0d`; `DESCRIPTION`: `License: GPL-3` | 🇺🇸 R tooling for building and testing education early-warning models on top of `caret`: ROC testing, model search, post-prediction adjustment. 71 files. 🟢 **Provenance is the value**: README names it the source behind modules of the **Wisconsin Dropout Early Warning System** (Wisconsin Dept of Public Instruction; author `Jared.Knowles@dpi.wi.gov`) | 🔴 **no.** Last commit **`2016-02-03`**, `DESCRIPTION` Date `2015-02-10`, version `0.9.2.9000`, Travis badges. 🟢 Read it as the **reference design** a state agency actually shipped — the model-search and ROC-testing structure is the reusable part, not the code |

🔴 **The licence boundary, stated because the two rows are not interchangeable.**
`student-signal` is MIT: a client's proprietary model, features and scoring thresholds stay
proprietary beside it. `EWStools` is **GPL-3.0 only** — no "or later" bound; the three *"any
later version"* strings in its payload are the How-to-Apply boilerplate, **not** a grant on
this package. An R deliverable that links it is a derivative work. 🟢 In practice this costs
nothing, because nobody should take a 2016 dependency: **port the method, not the package.**

🟡 **Two addresses the same leg returned and neither is on this shelf:**
`anwarulh007/eduprotect` **does not resolve** on either channel while `awesome.ecosyste.ms`
publishes an **MIT licence field** for it, and `ekoffi2/Machine-learning` resolves with **no
grant in a 2-file tree**. Recorded in
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) so no
later pass re-reads them.

🔴 **Mandated verticals leg: no new permissive education ERP/CRM, ELEVENTH consecutive pass.**
The whole result set was `openeducat.org`'s own glossary in seven languages. 🟢 One datum kept,
from the vendor's own page: **OpenEduCat is LGPLv3, not MIT or Apache** — the vendor itself
rules out the licence class the leg asks for. Both it and Odoo are already carried.

# Foundational repos — Education

> The layer below the agents: platforms, standards, assessment engines and learner-model
> libraries that an engagement builds *on* rather than *with*. Licences read first-hand from
> each repository's `LICENSE` payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds 13 payload-verified repositories, refutes two published permissive claims
> (forma.lms, Fedena) and **retracts this file's own LATAM gap**. Extended by
> [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv) — pass 267
> ranks this layer by **commits** instead of stars and by that measure finds the largest education
> codebase in open source (`instructure/canvas-lms`, **78,765 commits**) was missing from this file
> altogether, along with three permissive autograding/infrastructure rows and a **national education
> ministry publishing production services under MIT**. Extended again by
> [`verified-repos.2026-10-17-p268.tsv`](../evidence/verified-repos.2026-10-17-p268.tsv) — pass 268
> probes the rows this base **named but never read**, and that corrects the sentence above: the
> largest education codebase in open source is **`code-dot-org/code-dot-org`, 215,796 commits**,
> 2.7x Canvas. Pass 268 also shelves the **Ed-Fi** stack, which this base's own gap register has
> carried as the only permissive North American system of record for roughly 200 passes while
> *this* file carried no Ed-Fi row at all.

## 🟢 Pass 289 — THE FOUNDATION LAYER GAINS A **NATIONAL CURRICULUM AS A VALIDATABLE GRAPH**, and the grant under it is a restatement

⏱️ **Eleventh pass of `2026-10-18`.** Evidence:
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv) ·
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../evidence/curriculum-authority-egress.2026-10-18-p289.tsv) ·
[`p289-websearch.2026-10-18-p289.tsv`](../evidence/p289-websearch.2026-10-18-p289.tsv).

🔴 **Mandated vertical/ERP leg: no new permissive education row, TENTH pass running.** Apache
OFBiz (Apache-2.0), Huly (Apache-2.0), Krayin CRM (MIT), Aureus ERP (MIT), Atomic CRM (MIT),
iDempiere, Compiere, ERPNext (**GPL-3.0**, the only system in the leg naming Education among
its verticals), Dolibarr (GPL-3.0), Twenty (**AGPL-3.0 / BSL — source-available, not open
source**). 🔵 The leg's own summary states the finding: *"The results don't identify any MIT or
Apache project built for education."* **Ten passes. The education ERP/CRM gap is a gap in the
world, not in this base's searching** — administration is served by copyleft or by proprietary
SIS vendors, and a studio needing a permissive admin core **builds** it.

### 🟢 The new foundation row, and it is a layer this file did not have

| repo | grant (read from payload) | what it puts under an engagement |
|---|---|---|
| [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) | 🔵 **SPLIT** — **MIT** (`CODE-LICENSE.md`, 1 491 B, sha256₁₂ `427f1d8b0cc1`) for `scripts/` and workflows · **OGL v3.0** (`DATA-LICENSE.md`, 2 408 B, `c117e319f357`) for `ontology/`, `data/`, `docs/` | The **National Curriculum for England (2014)** as a formal graph: 31 classes, 75 properties, **38 SHACL shapes**, served as Turtle, JSON-LD, RDF/XML, N-Triples, SQLite and property-graph JSONL. 50 948 key learning points, 11 207 misconceptions, 7 432 prerequisites, 160 progression threads, 12 subjects |

🔵 **Why this belongs on the foundation shelf and not only on a trending one.** Every other
row in this file is a *platform* — something an engagement runs. This is a **curriculum
substrate**: an agent that claims a learning objective can be made to *validate* that claim
against 38 SHACL shapes instead of asserting it. 🔴 **This base has published
"curriculum-aligned" for ~200 passes with no alignment target in it.** This is the first row
that is one.

### 🔴 The grant beneath it is not the kind this file has been grading

`ACTION p289` separates two populations `p742` collapses:

- **`AUTHORITATIVE-BODY`** — the payload *is* the licence; the body travels with the clone.
  Every MIT/Apache/AGPL row on this shelf is one.
- **`RESTATEMENT`** — the payload *paraphrases* a licence authored by a third party, and names
  an off-repo host for the real text. **Both grade `GRANTED` under `p742`.**

The OGL half of this row is a `RESTATEMENT`, and 🔴 **the authority it names
(`nationalarchives.gov.uk`) is one of 12 licensing-authority hosts measured
`POLICY-REFUSED` from this environment — 2 independent egress paths, 12/12, zero reachable.**

🔵 **Stated plainly for a studio:** the structure, the ontology and the SHACL shapes are
**usable and commercially clear** — read first-hand from the payload:
*"exploit the information commercially and non-commercially … by including it in your own
product or application."* What is **not** closable from the payload is the exemption for
*"third party rights Oak National Academy is not authorised to license"* across 50 948 learning
points. **Build on the graph; clear the assets per engagement.**

🟡 **One obligation to get right, because the payload states it twice and differently.** OGL
prescribes `"Contains public sector information licensed under the Open Government Licence
v3.0."`; the same file's summary block asks for `"Oak National Academy"`. **Ship both.** The
cheaper reading is the one the file's own terms do not support.

## 🔴 Pass 288 — the foundation layer gained NOTHING this pass, and the reason is worth more than a filler row

⏱️ **Tenth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p288.tsv`](../evidence/verified-repos.2026-10-18-p288.tsv) ·
[`p288-websearch.2026-10-18-p288.tsv`](../evidence/p288-websearch.2026-10-18-p288.tsv).

🔴 **Mandated vertical/ERP leg: no new permissive education row, NINTH pass running.** The leg
returned a clean set of general-purpose systems and **not one education-specific one under a
permissive grant**:

| system | licence as the leg reported it | why it is not a foundation row here |
|---|---|---|
| Apache OFBiz | Apache-2.0 | ERP/CRM/HR automation suite. **No education vertical** — no student records, no admissions, no enrolment |
| Huly Platform | Apache-2.0 | Team/project platform, not an education system |
| Krayin CRM | MIT | CRM only |
| Aureus ERP | MIT | ERP with a plugin system; no education module |
| Atomic CRM | MIT | CRM only |
| ERPNext | **GPL-3.0** | 🟡 **The only system in the whole leg that names Education among its verticals** — and it is copyleft, so it cannot join the permissive tier |
| Dolibarr | GPL-3.0 | Copyleft; no education module |
| Twenty | AGPL-3.0 / BSL-1.1 | 🔴 **Source-available, NOT open source.** Recorded so a later pass does not read it as permissive |

🔵 **Stated plainly: the education ERP/CRM gap is not a gap in this base's searching — it is a
gap in the world.** Nine passes have run this leg. The answer each time is that education
administration is served either by copyleft (ERPNext, OpenEduCat, Dolibarr) or by proprietary
SIS vendors, and the permissive tier has no entrant. A studio needing a permissive admin core
builds it; it does not adopt one.

### 🔴 The Blackboard integration surface is real, and nothing on it is vendorable

The directed LMS-MCP leg added **Blackboard Learn** to the MCP-addressable set (see
[`agents/top.md`](../agents/top.md) for the full comparison against Moodle, Canvas, Google
Classroom and Open edX). As a *foundation* question the answer is negative and precise:

- 🔴 [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) — **no grant** in 9
  enumerated files, though its `readme.md` claims MIT. **An ASK, not a licence.**
- 🔴 [`yoyoconnor/BlackboardMCP`](https://github.com/yoyoconnor/BlackboardMCP) — **no grant**
  in 9 files; `pyproject.toml` carries no `license` key.
- 🟡 [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) — **already carried**;
  AGPL-3.0 per the Open edX project's own announcement, targets Ulmo, Tutor local and
  Kubernetes, and re-checks platform staff/superuser flags live on every request.

🟢 **What IS a foundation here is the API, not the server.** The Blackboard Learn **REST API**
is the stable surface; the community MCP servers in front of it are 9-file wrappers with no
grants. `P41` in [`compose/patterns.md`](../compose/patterns.md) wires that surface directly
and names what must be written fresh.

🔴 **No row is added to the tables below this pass.** Five real foundation repos were sought
and none was found that is both education-specific and permissively licensed. **Fewer real
rows beat padding**, and the searches that produced this nil are written down leg by leg in
[`p288-websearch`](../evidence/p288-websearch.2026-10-18-p288.tsv).

## 🟢 Pass 287 — a Bangla NLP toolchain is the foundation layer a Bengali engagement has had no answer for, and the mandated vertical leg again found nothing

⏱️ **Ninth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p287.tsv`](../evidence/verified-repos.2026-10-18-p287.tsv) ·
[`p287-websearch.2026-10-18-p287.tsv`](../evidence/p287-websearch.2026-10-18-p287.tsv).

🔴 **The mandated verticals leg produced no new permissive row, for the ninth time in ten
passes.** It returned `OpenEduCat` (Odoo-based, licence unstated by the source; this shelf
already carries it), **ERPNext GPL-3.0**, and **Twenty CRM under BSL-1.1** —
*source-available, not open source*, which is the `PageLM`/`Suna`/`OpenGaokao` pattern arriving
for the fourth time through a fourth channel. 🟢 **Said plainly: there is still no education
ERP or CRM under MIT or Apache that this base has been able to locate**, and nine passes of
the same query is now evidence about the supply, not about the search.

### 🟢 The genuinely new foundation row, and it came from a NIL

🔵 **The Bangladesh leg found no tutor and that is not what makes it useful.** It found that
**real Bangla open source exists and is INFRASTRUCTURE**:

| repository | what it is | why it is a FOUNDATION and not an agent |
|---|---|---|
| [`sagorbrur/bnlp`](https://github.com/sagorbrur/bnlp) | *"Natural language processing toolkit for Bengali Language"* — tokenisation, embeddings, NER, POS | 🟢 **The layer a Bengali-medium tutor is built ON.** No education repo on any shelf here can serve a 🇧🇩 learner in Bangla without something at this level |
| [`banglakit/awesome-bangla`](https://github.com/banglakit/awesome-bangla) | A collection of tools, datasets and resources for Bangla computing | 🔵 An **index of the layer**, which is how a studio finds the rest of it in week one |
| [`me-shaon/bangla-programming-resources`](https://github.com/me-shaon/bangla-programming-resources) | Bangla-language programming tutorials and references | Content, not code — relevant to a **teacher-training** scope rather than a learner-facing one |

🟡 **Licences NOT read first-hand this pass and therefore NOT published here as grants** — these
rows arrived from a search result, and this base's own two-pass record is that **three of four
secondary "open source" claims are wrong**. They are **leads at the right layer**, and probing
them is a `p288` item. Recording them as leads rather than as shelf rows is the whole point of
the distinction.

🟢 **What this pass DID establish about them, because it is cheap and it shortens `p288`'s
probe: all three RESOLVE, and their default refs are resolved rather than assumed.**

| lead | `ls-remote --symref` default ref |
|---|---|
| `sagorbrur/bnlp` | `main` |
| `banglakit/awesome-bangla` | `main` |
| `me-shaon/bangla-programming-resources` | 🔴 **`master`** |

🔴 **The third row is the reason this table exists rather than a sentence.** A `p288` probe that
hardcodes `main` would publish `NONE_IN_TREE` over it — which is the exact failure this pass saw
a third time in four passes (`AIProf` on `dev`, `eledia` on `master`, `twiga` on `development`).
**Resolve the ref; never assume it.**

🔵 **The general lesson, which is about where this base looks for foundations:** the language
legs keep returning **tutors that are proprietary** and **language infrastructure that is
open**. For every non-English market probed so far — 🇧🇩 Bangla, 🇻🇳 Vietnamese, 🇮🇩 Indonesian,
🇹🇿 Swahili — *the permissive code sits one layer BELOW the agent*, and an engagement that goes
looking for a tutor finds nothing while the thing it actually needs is sitting there unclaimed.

### 🔴 A correction to how this shelf has been reading `NONE_IN_TREE`

🔴 **`saif2012004/PrepifyAI` (389 files, no grant) shows that a code grant is not always the
binding constraint.** Its tree carries **20 `Extracted text books/` JSON files** for
`FBISE_CLASS9/10` and `PUNJAB_CLASS9/10`. 🔵 **This shelf's standing remedy for a
`NONE_IN_TREE` row is "ask the author for a written grant"** (`P17`, `P19`, and `p286` item 5's
licence-intake ask). 🔴 **That remedy would not clear this repository**: the author cannot grant
what they do not hold, and board textbook text is third-party copyright. 🟢 **So the remedy for
a `NONE_IN_TREE` row depends on WHAT IS IN THE TREE**, and this shelf has been treating the
verdict as though it had one remedy. Annotated, not rewritten. `T-p287c`.

🟢 **The same seam, documented from the supply side by `avps82/mentar`'s own
`docs/CONTENT_LICENSES.md`** — see [`repos/trending.md`](trending.md) and
[`compose/patterns.md`](../compose/patterns.md) `P40`. Two independent arrivals at the same
boundary in one pass: **the code grant and the content grant are different questions, and the
content one is the one that bites a PAID deliverable.**

## 🟢 Pass 286 — a national EXAM-RESULTS channel joins this shelf, and it is the layer an East African engagement has had no answer for

⏱️ `2026-10-18`, eighth pass. Evidence:
[`regional-intake.2026-10-18-p286.tsv`](../evidence/regional-intake.2026-10-18-p286.tsv).

🟢 **One row added, and it is a FOUNDATION rather than an agent** —
[`vincent-laizer/NECTA-API`](https://github.com/vincent-laizer/NECTA-API), **MIT**, root `LICENSE`
1 092 B, payload-read `2026-10-18`. A Python package that fetches results of Tanzania's national
examinations (**NECTA**). 🔵 **Why it belongs on this shelf and not on `agents/top.md`:** it carries
no model and no pedagogy — it is the **system-of-record channel** that a tutor, a dropout-prediction
model or a ministry dashboard reads underneath. This shelf's thinnest column has been *national
assessment data outside Europe and North America*, and this is the first row in it.

⚠️ **Two cautions, both from the author's own words:** it is **not an official NECTA API** (it reads
the published results service, so it breaks when that service changes) and it is **still in
development**. 🟢 The licence, however, is clean and permissive — which is the part a studio cannot
fix for itself.

🟢 **Also permissive, also new, and shelved as a platform rather than a foundation:**
[`Jahirrrr/sekolahyuk-app`](https://github.com/Jahirrrr/sekolahyuk-app) (🇮🇩, **MIT**, 1 064 B) — see
[`verticals/solutions.md`](../verticals/solutions.md).

🔴 **What this shelf did NOT gain, and the reason is a licence rather than an absence.** Seven
Indonesian and six Vietnamese addresses were probed. The one with the most platform-shaped scope,
[`sira313/rapkumer`](https://github.com/sira313/rapkumer) — a working alternative to Indonesia's
official **e-Rapor** report-card system, with an AI generator for learning objectives from **BSKAP**
outcomes — serves a **bespoke non-commercial licence** and therefore cannot be a foundation for
anything billable. 🔵 **Recorded here because the next pass must not re-discover it as a candidate:
the grant is the blocker, and it is a written policy of its author, not an omission.**

## 🟢 Pass 285 — the `Kuali` lead is RESOLVED AT PAYLOAD, and "open foundation, therefore permissive" is refuted on the limb that mattered

⏱️ `2026-10-18`, seventh pass. Evidence:
[`tree-enumeration.2026-10-18-p285.tsv`](../evidence/tree-enumeration.2026-10-18-p285.tsv).

🔵 `p284` registered **Kuali** as a lead and graded it honestly: *"HE **ERP/SIS/research admin** —
the thinnest column on the vertical shelf. Source **undated**, **no ref or payload read**, and
*'open foundation therefore permissive'* is the **parent-inference** grade this base ranks weakest."*
🟢 **Resolved this pass, one `ls-remote` and one payload read per repository** — and the
parent-inference was wrong in both directions at once:

| repository | resolves? | grant, read from payload `2026-10-18` | what it is |
|---|---|---|---|
| [`kuali/rice`](https://github.com/kuali/rice) | 🟢 yes | 🟢 **ECL-2.0** — `master/LICENSE.txt`, 11 182 B, *"Educational Community License, Version 2.0, April 2007"* | middleware. **Apache-derived, permissive** — the only permissive row in the family |
| [`kuali/kfs`](https://github.com/kuali/kfs) | 🟢 yes | 🔴 **AGPL-3.0** — `master/LICENSE`, 33 755 B, title window *"The GNU **Affero** General Public License … requires the operator of a network server to provide the source code"* | **Financials / ERP**. Network copyleft |
| [`kuali/kc`](https://github.com/kuali/kc) | 🟢 yes (HEAD `53fee5c1abef`) | 🔴 **no grant anywhere in the tree** — **20 627 files enumerated**, every licence-like hit is a Java class, an XML config or a help page (`NoticeOfOpportunity*.java`, `copyingadocument.htm`, `copyrightandlicensing.htm`) | Coeus — research administration |
| [`kuali/student`](https://github.com/kuali/student) | 🔴 **DOES NOT RESOLVE** | — | 🔴 **the SIS — i.e. the exact thing the thin column needed** |
| [`kuali/ole`](https://github.com/kuali/ole) | 🔴 **DOES NOT RESOLVE** | — | library system |

🔴 **So the answer to the lead is "no", and it is specific:** there is **no public Kuali SIS
repository**; the ERP is **AGPL-3.0**, not permissive; the research-admin codebase serves **no
grant at all** across twenty thousand files; and the one permissive grant in the family
(**ECL-2.0**) covers **middleware**, not an administrative system.
🟢 **This confirms, at payload grade, this base's own earlier conclusion that *Kuali's licence is
per REPO, not per ORGANISATION*** — which secondary sources (Wikipedia, EDUCAUSE, Maven Central,
linux.com) flatten into a single *"Kuali is licensed pursuant to the ECL, Version 2.0"*.

🔵 **The vertical shelf's thinnest column stays thin — but now for a MEASURED reason rather than an
unread lead.** The permissive HE-administration row this base has wanted for many passes is still
`Gego-K12/gegok12` (MIT, open-core), and Kuali does not join it.

**Pass 273 — no rows added, eighth consecutive nil, and the reason is now specific.** The scheduled
platform/SIS/ERP leg returned only systems already shelved here or on
[`verticals/solutions.md`](../verticals/solutions.md), and two listicles contradicted each other on
`forma.lms` (Apache-2.0 vs GPL) — a question this base settled at payload in `p265`. 🔵 **One nil is now
explained rather than repeated:** the battery's *"github trending education AI"* leg returns repositories
that **teach AI** (`generative-ai-for-beginners`, `nanochat`, `developer-roadmap`), not repositories that
**serve the education sector** — a query defect, not an absence of supply. ⚠️ **This file's layer was not
where pass 273's finding landed**; it landed on the agent shelf and on licence method — see `T41` and
[`repos/trending.md`](trending.md).

## 🟡 Pass 284 — no row added, and the one candidate the leg produced is NOT shelved, on purpose

⏱️ `2026-10-18`, sixth pass. Evidence: [`p284-websearch.2026-10-18-p284.tsv`](../evidence/p284-websearch.2026-10-18-p284.tsv).

🔴 **What was searched and what came back.** The leg
`open source platform education ERP CRM MIT Apache student information system` returned
**OpenEduCat** (LGPL-3.0, built on Odoo) — **already on this base's vertical shelf** — and
explicitly returned **nothing MIT- or Apache-licensed**. The result's own words: *"It did not return
anything on MIT- or Apache-licensed education platforms."*

🟡 **One candidate, named and deliberately NOT shelved: the `Kuali Foundation`.** A Linux.com article
describes it as *"the premiere open source educational administration project"*, producing **ERP, SIS
and research-administration systems** for higher education — a category this base's vertical shelf
has thin coverage of. 🔴 **Three reasons it stays off the shelf this pass:**

1. 🔴 **The source is undated**, and it names **Compiere** and **Openbravo** alongside it — projects
   whose heyday was over a decade ago. That dates the article, not Kuali, but it means the
   *currency* of the claim is unestablished.
2. 🔴 **No repository, no grant, no ref was read.** This base's standing rule is that a row carries a
   licence read **first-hand from the payload**. Nothing was read here.
3. 🔵 **Kuali's licence history is the specific reason not to guess:** the project is widely
   associated with a move toward a commercial entity, so an inference of *"it is an open foundation,
   therefore the code is permissive"* is exactly the **parent-inference grade** this base ranks
   weakest and has already been burned by (`kolibri-design-system`, `Athena`).

🟢 **Registered, not published.** Resolving it costs one `git ls-remote` plus one payload read and
would extend the thinnest part of the vertical shelf (**higher-education administration**). It is in
the backlog in [`../README.md`](../README.md) rather than in a table, because a row here is a
recommendation and this is a lead.

## 🔴 Pass 283 — the Artemis row on THIS shelf recommended one repository twice, and `p282`'s correction never reached it

⏱️ `2026-10-18`, fifth pass. Evidence: [`repo-identity.2026-10-18-p283.tsv`](../evidence/repo-identity.2026-10-18-p283.tsv) · [`ladder-case-audit.2026-10-18-p283.tsv`](../evidence/ladder-case-audit.2026-10-18-p283.tsv) · [`p283-websearch.2026-10-18-p283.tsv`](../evidence/p283-websearch.2026-10-18-p283.tsv).

🔴 `p282` established that `ls1intum/Iris` and `ls1intum/Pyris` are **one repository** (identical
HEAD `d7b2c095204e`, 245 refs, root tree `4e2f096df767`, 203 files, the same 1 088-byte MIT payload)
and corrected `agents/top.md`, `compose/patterns.md` and `verticals/solutions.md`.

🔴 **It did not correct this file.** The `ls1intum/Artemis` row went on naming *"**Iris** (LLM tutor,
`ls1intum/Iris`, MIT)"* and *"**Pyris** (the LLM microservice behind it, `ls1intum/Pyris`, MIT)"* as
**two distinct config-gated AI subsystems**, inside a single cell. A studio reading this row would
have scoped two integrations where one exists. 🟢 **Corrected above.**

🟢 **Found by `make gate-identity`, which `p283` built and wired, on its first run** — the whole
point of the gate, demonstrated on the pass that shipped it. 🔵 The count that matters for this
shelf: **138 live addresses across the three shelves, 138 distinct HEADs, 0 unreachable** — no other
row on any shelf recommends one repository twice.

🔵 **No new foundation this pass**, and the star column stays **frozen at `2026-10-17`** — `p282`'s
channel finding is re-confirmed and sharpened: `github.com` pages and `api.github.com` still answer
`403`, while the **git** channel answered **138 of 138**. Grants and identity are current; only
popularity is stale.

## 🔴 Pass 282 — no new foundation, and the star column on this shelf is FROZEN

🔴 The mandated vertical and trending legs returned **no foundational repository this base does not
already hold**. Every candidate they named — `Apache OFBiz` (Apache-2.0, a general business suite,
not education), `Huly` (Apache-2.0), `OpenEduCat` (**LGPL-3.0**, Odoo-based, 73+ modules),
`frappe/lms`, `LearnHouse` — returned `CARRIED` under `make carried`. 🔵 The leg's own words:
*"the search turned up few education-specific platforms under MIT or Apache."*

🔴 **And the channel that serves star counts is shut this pass:** `github.com/<slug>`,
`/topics/*`, `/trending` and `api.github.com` all answer **`403`**, while
`raw.githubusercontent.com` and `git ls-remote` answer normally. 🟢 **So every licence on this shelf
is still first-hand and current, and every star figure is carried from `2026-10-17` and was not
re-measured.** Evidence:
[`channel-reach.2026-10-18-p282.tsv`](../evidence/channel-reach.2026-10-18-p282.tsv).

🟢 `ls1intum/Artemis` was re-read at payload this pass — **MIT, `main/LICENSE`, 1 090 B, HEAD
`dc78a2bcba53`** — unchanged. 🔴 **Note for anyone composing from it:** `ls1intum/Iris` is **not** a
second repository to pair with `Pyris`; it is an alias of `Pyris`. See
[`agents/top.md`](../agents/top.md) pass 282.

## Permissive foundations (MIT / Apache-2.0 / BSD)

> 🆕 **Pass 274 adds the first row to this table in nine passes, and it is a row this base REFUSED
> twice.** See the `gegok12` retraction below and `T44`.

| Repo | Licence | Stars | Why it is a foundation |
|------|---------|-------|------------------------|
| 🆕 [digitalcredentials/learner-credential-wallet](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 **MIT** *(**payload** `LICENSE`, 1 092 B, sha256₁₂ `1032f65dd2f6`, read `p300`)* | **89★ / 50 forks / 1 309 commits / `main`** | **The highest-adoption row of the `p300` batch, and the credentialing layer's anchor.** Cross-platform **iOS and Android** wallet for storing and sharing digital learner credentials; TypeScript + React Native/Expo. 🟢 From the **Digital Credentials Consortium** — the MIT-based body whose six repositories `ACTION PG-4` never named. 🔵 This is the row that makes the layer *end-user reachable*: everything else in it issues or verifies; this is where the learner keeps the credential. |
| 🆕 [digitalcredentials/verifier-plus](https://github.com/digitalcredentials/verifier-plus) | 🟢 **MIT** *(**payload** `LICENSE`, 1 087 B, sha256₁₂ `85569d7ed8fc`, read `p300`)* | **19★ / 14 forks / 397 commits / `main`** | *"VerifierPlus allows users to verify any supported digital academic credential"* — a Next.js app where a credential is pasted, uploaded, linked or **scanned**, then checked for signature, expiry, revocation status and issuer, plus an optional MongoDB-backed store that returns a shareable link. 🔴 **Boundary in the row: Verifiable Credentials v1 and v2 and Open Badges v3 — NOT Open Badges v2.** A client still on OBv2 needs a conversion step first; that is the next row but one. |
| 🆕 [digitalcredentials/verifier-core](https://github.com/digitalcredentials/verifier-core) | 🟢 **MIT** *(**payload** `LICENSE.md`, 1 087 B, sha256₁₂ `6e7a616c4d70`, read `p300`)* | **2★ / 4 forks / 272 commits / `main`** | The verification **engine** beneath `verifier-plus`. 🔴 **FIFTH licence spelling on this shelf** — the grant is at `LICENSE.md`, and `p295` was bitten by exactly this on `Submitty`, where plain `LICENSE` was `404`. 🔵 **2★ against 272 commits** is the substrate signature this file has now recorded five times. Take this one, not the app, when embedding verification in a client's own interface. |
| 🆕 [digitalcredentials/issuer-coordinator](https://github.com/digitalcredentials/issuer-coordinator) | 🟢 **MIT** *(**payload** `LICENSE`, 1 087 B, sha256₁₂ `ca28a7ae5c7e`, read `p300`)* | **11★ / 4 forks / 55 commits / `main`** | *"An app that issues signed Verifiable Credentials and allows them to be revoked."* 🟢 **Revocation is the half most credentialing demos omit — and the half a registrar actually asks about.** 55 commits, small because it coordinates rather than implements. |
| 🆕 [digitalcredentials/vc](https://github.com/digitalcredentials/vc) | 🟡 **BSD-3-Clause** *(**payload** `LICENSE`, 1 525 B, sha256₁₂ `4f0d287e80be`, holder **Digital Bazaar, Inc.**, read `p300`)* | **6★ / 5 forks / 502 commits / `main`** | JavaScript implementation of the **W3C Verifiable Credentials** standard, underneath the DCC stack above. 🔴 **A DECLARED FORK of [`digitalbazaar/vc`](https://github.com/digitalbazaar/vc)**, taken at v1.0.0 to add React Native compatibility — and cited here rather than upstream because *this* is the one the DCC stack depends on. 🔴 **TWO GRANTS IN ONE ROW:** the payload is New BSD (3-clause) © 2020-2021 Digital Bazaar; the README *additionally* declares **MIT** over *"DCC — TypeScript compatibility"*. The payload is what this shelf grades; the MIT claim covers only the DCC additions and is **README-stated, not payload-read**. |
| 🆕 [impierce/credential-converter](https://github.com/impierce/credential-converter) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 356 B, sha256₁₂ `efd09e39cb61`, read `p300`)* | **12★ / 2 forks / 250 commits / `main`** | **Rust** CLI and library translating between credential data formats — **Open Badges v3 ↔ ELM**, the European Learner Model that Europass consumes — extensible to any standard with a JSON Schema, and able to import mappings from **DESM CSV** files. 🟢 **The one row on this shelf that crosses the Atlantic standards divide**, and so the first row an EMEA engagement with a US-shaped credential stack needs. |
| 🆕 [impierce/digital-credential-data-models](https://github.com/impierce/digital-credential-data-models) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 357 B, sha256₁₂ `c71d239df917`, read `p300`)* | **5★ / 1 fork / 8 commits / 🔴 `dev`** | Rust library modelling **Open Badges v3.0** and **European Learner Model v3.2**, under the converter above. 🔴 **ITS DEFAULT BRANCH IS `dev`, NOT `main` OR `master`** — trap #1 in this base's own [`lib/probe_payload.sh`](../compose/code/lib/probe_payload.sh) header, met live. A probe with a hardcoded branch writes this repository down as **ungranted**; the grant is there, on `dev`. 🔵 8 commits: a data-model crate, correctly small. |
| 🆕 [BeBadges/escobadges](https://github.com/BeBadges/escobadges) | 🟢 **MIT** *(**payload** `LICENSE.md`, 1 067 B, sha256₁₂ `95fc2f1c5370`, read `p300`)* | **5★ / 1 fork / 18 commits / `master`** | *"A Badge Builder web app based on the ESCO classification"* — designs and issues **Open Badges** against the **EU's ESCO skills pillar**, reached over its API. 🟢 **The one EMEA-anchored row of this pass — and it arrived in the hour the mandated EMEA leg returned its TWELFTH nil.** Not from that leg: from the promotion backlog. 🔴 **Boundary: 18 commits, and a Travis CI badge for a service that no longer runs that way.** A worked ESCO-binding reference, never a maintained dependency. |
| 🆕 [TanimowoObaloluwaDavid/credential-lens](https://github.com/TanimowoObaloluwaDavid/credential-lens) | 🟢 **MIT** *(**payload** `LICENSE`, 1 080 B, sha256₁₂ `f65f32330671`, read `p300`)* | 🔴 **0★ / 0 forks / 3 commits / `main`** | *"Inspect and validate Open Badges 3.0 / W3C Verifiable Credentials. Zero dependencies, works offline."* A CLI (`credlens`), a library (`validate`, plus `window.CredentialLens`) and a static web UI; JSON output for CI; every finding carries a JSON Pointer, a message and a suggested fix; score 0-100, any error capping it at 59. 🔴 **THREE COMMITS — the thinnest row on this file, published with that in the row rather than hidden.** 🟢 **Why it is here:** it states its own non-goals out loud — *no signature verification, no status-list fetching, no DID resolution* — which is more than most of this layer does, and zero-dependency offline validation is what an air-gapped ministry pilot can actually run. |
| 🆕 [CogniPilot/credentials](https://github.com/CogniPilot/credentials) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 357 B, sha256₁₂ `c71d239df917`, read `p300`)* | 🔴 **0★ / 0 forks / 365 commits / `main`** | *"Credentials platform for OpenBadges3.0"* — issuing, updating, revoking and **W3C-validating** OBv3 badges, in production for a **non-education engineering community** (example badges: *"Rumoca Maintainer"*). 🟢 **Why a non-education repository earns a row on an education shelf: it is the proof that this layer is domain-neutral**, and at 365 commits it is the most complete worked OBv3 *deployment* in the batch. 🔴 **Boundary: an INSTANCE, not a library.** Read its wiring; do not import it. |
| 🆕 [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 357 B, sha256₁₂ `c71d239df917`, read `p300`)* | 🔴 **0★ / 0 forks / 128 commits / `main`** | 🟢 **THE ONLY xAPI 2.0 ROW ON THIS BASE, and the most strategically important row of the pass despite zero stars.** An xAPI-conformant Learning Record Store implementing **both 1.0.3 AND 2.0**, on Hono with PostgreSQL *or* **PGlite** (embedded, for local and offline use), with statement validation, attachments, **Server-Sent Events** for real-time statement streaming, JWT and Basic auth, an admin UI and OpenTelemetry metrics. 🟢 **Its migration story is the row's real value: it can take over an existing [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) database IN PLACE** — so the 1.0.3 stack this base shelved across `p298`-`p299` has a forward path to 2.0 that does not open with a data-migration project. |
| 🆕 [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 **MIT** *(**payload** `LICENSE`, 1 073 B, sha256₁₂ `e5a1f41b0bb5`, read `p300`)* | **58★ / 32 forks / 32 commits / `master`** | *"A NodeJS application that packs H5P content into SCORM objects"* — packages H5P so it runs in any SCORM-capable LMS, reporting scores back through the SCORM API. 🟢 **The bridge between the two content layers this base already shelves and the SCORM rows beside it.** 🟢 **Shelved partly BECAUSE of its own README**, which ships a *"Disadvantages"* section — no cross-content library caching, no in-LMS H5P editing, no library updates, larger packages — and concludes *"you should only package H5P into SCORM if there are compelling reasons to do so."* **Quote that to a client before the feature list.** |
| 🆕 [dhodges47/SCORM-LearningManagementSystem](https://github.com/dhodges47/SCORM-LearningManagementSystem) | 🟢 **MIT** *(**payload** `LICENSE.txt`, 1 091 B, sha256₁₂ `8e079631dedc`, holder *David Hodges dba Outermost Software, LLC*, read `p300`)* | **184★ / 95 forks / 36 commits / `master`** | *"Open Source SCORM Learning Management System demo"* — .NET Core 2.1, EF Core and SQL Server: upload SCORM packages, play them in a built-in **SCORM Player**, track results per student. **SCORM 1.2, with some 2004 support.** 🔴 **184★ and 95 forks on 36 commits, and its own README calls the pages *"very lightly styled"*** — a reference implementation a great many people have cloned, not a product. 🔵 **A 0.52 fork-to-star ratio: the deployment signature this file keeps finding on substrate rows.** 🔴 Grant at `LICENSE.txt` — the fourth spelling, again. |
| ♻️ [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | 🟢 **MIT** *(sidebar, read `p299`)* | **78★ / 52 forks / 1 039 commits / `master`** | *(**row restored to this table by `p300`** — `p299` admitted it and never wrote it here)* NodeJS suite testing the **`MUST` requirements of the xAPI specification**, from **ADL**, who author the spec. 🟢 **The highest-adoption row of `p299`'s batch, and how you prove an LRS claim instead of repeating it.** ⚠️ Its own README: basic auth only, *"should not be run against a production LRS endpoint."* |
| ♻️ [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | 🟢 **Apache-2.0** *(sidebar, read `p299`)* | **60★ / 33 forks / 153 commits / `master`** | *(**row restored by `p300`**)* The **xAPI Profiles** companion specification, also from ADL. 🔵 **The permissive counterpart to everything Caliper no longer offers:** a standards document you may actually build on. Pairs directly with [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe), which filters by Profile templates. |
| ♻️ [OpenOLAT/qtiworks](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** *(**payload** `LICENSE.txt`, 2.01 KB, read `p299`; sidebar unlabelled)* | **3★ / 2 forks / 🔴 2 087 commits / `master`** | *(**row restored by `p300`**)* **QTI 2.1 delivery engine, the JQTI+ Java library and MathAssess extensions** — by far the deepest QTI implementation on this file. 🔴 **Pick this fork, NOT the 68★ upstream [`davemckain/qtiworks`](https://github.com/davemckain/qtiworks)**, whose own description announces *"This project will be closed in early 2023!"*. The fork carries 14 commits the original never got: `p299`'s rule is **prefer the slug where the history continues.** |
| ♻️ [S4-NetQuest/react-scorm-provider](https://github.com/S4-NetQuest/react-scorm-provider) | 🟢 **MIT** *(sidebar, read `p299`)* | **67★ / 23 forks / 19 commits / `master`** | *(**row restored by `p300`**)* React components wrapping the **SCORM API**. 🟢 **The first SCORM row this base ever shelved.** 19 commits against 67 stars — a small, finished adapter, which is what this layer should look like. |
| ♻️ [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🟢 **MIT** *(sidebar, read `p299`)* | **4★ / 1 fork / 🔴 794 commits / `master`** | *(**row restored by `p300`**)* **QTI 2.1, 2.2 AND 3.0** players plus a bidirectional **QTI ↔ PIE** transform framework, with a CLI, a web app and IMS Content Package support. ⚠️⚠️ **Its own README: pre-1.0, *"not fully conformant or certified"*, and not for untrusted or high-stakes delivery without a backend-authoritative integration.** 🔴 **Never brief this as exam-grade; brief it as the migration tool it is.** |
| ♻️ [metyatech/markdown-to-qti](https://github.com/metyatech/markdown-to-qti) | 🟢 **MIT** *(sidebar, read `p299`)* | **2★ / 0 forks / 102 commits / `main`** | *(**row restored by `p300`**)* **Markdown → QTI 3.0 XML packages**, a TypeScript CLI on npm, with manifest-driven ordering, IDs and points. 🟢 **The authoring half of the QTI layer**, which `p298` had left open having armed playback and packaging only. |
| ♻️ [metyatech/qti-html-renderer](https://github.com/metyatech/qti-html-renderer) | 🟢 **MIT** *(sidebar, read `p299`)* | 🔴 **0★ / 0 forks / 47 commits / `main`** | *(**row restored by `p300`**)* QTI 3.0 item XML → **HTML**, with scoring, report and explanation rendering and response-to-prompt binding. 🔴 **Zero stars, zero forks, 47 commits** — the same shape as `Kennisnet/php-qti3`, and the fourth confirmation on this file that **stars misrank substrate.** |
| ♻️ [sonyccd/qti-playground](https://github.com/sonyccd/qti-playground) | 🟢 **MIT** *(sidebar, read `p299`)* | **4★ / 0 forks / 167 commits / `main`** | *(**row restored by `p300`**)* A web app to **view, edit and live-preview QTI 3.0 XML** in a split pane. 🔵 The one row in this layer aimed at a **human author** rather than a runtime — useful in a workshop, not in a pipeline. |
| ♻️ [rolfis/qti-convert](https://github.com/rolfis/qti-convert) | 🟢 **Apache-2.0** *(sidebar, read `p299`)* | **22★ / 6 forks / 42 commits / `main`** | *(**row restored by `p300`**)* Converts a **Canvas QTI export package** into **JSON or Word (.docx)**. 🟢 **The only row on this file that reaches backwards into a vendor's export format** — which is the format a migration engagement is actually handed on day one. |
| ♻️ [examplary/qti](https://github.com/examplary/qti) | 🟢 **MIT** *(sidebar, read `p299`)* | **1★ / 0 forks / 39 commits / `main`** | *(**row restored by `p300`**)* TypeScript toolkit building **and** parsing **QTI 3.0 and 2.1** packages, manifests, items, tests and stimuli, with automatic version detection. 🔴 **Bare-name collision with [`instructure/qti`](https://github.com/instructure/qti), also on this shelf — and they are NOT the same thing**: TypeScript building QTI 3.0/2.1 against a Ruby gem parsing QTI 1.2/2.1. A pass that skipped the name as a duplicate would have lost the only permissive QTI 3.0 *packaging* row in TypeScript. |
| ♻️ [agencyenterprise/qti-3-player](https://github.com/agencyenterprise/qti-3-player) | 🟢 **MIT** *(sidebar, read `p299`)* | **3★ / 1 fork / 88 commits / `main`** | *(**row restored by `p300`**)* `@ae-studio/qti-renderer` — a framework-agnostic QTI 3.x item renderer with response processing and feedback. ⚠️⚠️ **Boundaries from its own README: NO scoring, single items only (no test structure), `choice-interaction` ONLY, partial expressions, no adaptive behaviour, and MathJax must be supplied by the host.** 🔴 Narrower than [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player); shelve both, sell that one. |
| ♻️ [raccoongang/edx_xblock_scorm](https://github.com/raccoongang/edx_xblock_scorm) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11.1 KB, read `p299`; sidebar unlabelled)* | **32★ / 🔴 65 forks / 49 commits / `master`** | *(**row restored by `p300`**)* **SCORM 1.2 and 2004 inside Open edX** as an XBlock, Studio-editable, reporting scores and state to the progress tab. 🔴 **ARCHIVED `2023-11-27`** — read it as a pattern, not a dependency. 🔵 **65 forks against 32 stars:** the deployment signature again, and the strongest case on this file that an archived repository can still be the live one in practice. |
| ♻️ [php-xapi/client](https://github.com/php-xapi/client) | 🟢 **MIT** *(sidebar, read `p299`)* | **23★ / 11 forks / 137 commits / `0.7`** *(branch read)* | *(**row restored by `p300`**)* **xAPI client for PHP**, via Composer. 🟢 Puts the xAPI boundary in the runtime **Moodle and Tsugi already are** — the same argument `p298` made for `1EdTech/lti-1-3-php-library`. 🔴 Exposes no default branch on its page; cite the branch when you pin. |
| ♻️ [php-xapi/model](https://github.com/php-xapi/model) | 🟢 **MIT** *(sidebar, read `p299`)* | **3★ / 8 forks / 340 commits / `3.x`** *(branch read)* | *(**row restored by `p300`**)* xAPI **model classes** beneath the client above. Forks (8) exceed stars (3) again. 🔴 Also exposes no default branch. |
| ♻️ [EscolaLMS/LRS](https://github.com/EscolaLMS/LRS) | 🟢 **MIT** *(sidebar, read `p299`)* | **7★ / 0 forks / 27 commits / `main`** | *(**row restored by `p300`**)* A **Laravel** Learning Record Store package — and 🟢 **the only row in this base that names `cmi5`**, serving `/api/cmi5/**` with `x-experience-api-version: 1.0.3`. 🔵 The permissive, embeddable alternative to standing up [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) beside a PHP application. 🔴 **Pinned to 1.0.3** — see `pelotech/xapi-lrs` above for the 2.0 path. |
| 🆕 [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** *(sidebar, read `p298`)* | **373★ / 86 forks / 575 commits / `master`** | **LTI 1.3 tool provider in TypeScript — the highest-adoption permissive LTI row on this file.** Launches, Deep Linking, Assignment & Grade Services, Names & Roles, Dynamic Registration, with the security and validation already implemented. 🟢 **This is how a Node studio puts its own application inside Moodle, Canvas or Open edX without touching the LMS codebase** — the `p298` arming of this file's oldest instruction, *"integrate, do not fork."* ⚠️ README says *"educational environments"* and never *students*: it is a protocol library, not a teaching product. |
| 🆕 [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🟢 **Apache-2.0** *(sidebar, read `p298`)* | **124★ / 107 forks / 110 commits / `master`** | **LTI 1.3 from the standards body itself**: OIDC login, message launches, Deep Linking, Names & Roles, Assignments & Grades. 🔵 **107 forks against 124 stars** — forks exceeding stars is this file's established deployment signature (`Submitty`, `gegok12`, `Ed-Fi-ODS`): institutions **run** this, developers do not **star** it. Pair with [tsugi](https://github.com/tsugiproject/tsugi) when you want a whole tool framework rather than a protocol library. |
| 🆕 [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** *(sidebar, read `p298`)* | **138★ / 84 forks / 178 commits / `master`** | **LTI 1.3 Advantage in Python, with Django and Flask adapters** (other frameworks by reimplementing `OIDCLogin` and `MessageLaunch`). The row a Python-first engagement needs to reach a copyleft LMS. 🔴 **`p989`'s orphan list named [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) instead — 3★, 1 fork, no sidebar licence label, and a root `LICENSE` reading `Copyright (c) 2019 Dmitry Viskov`.** That is a **re-publication of this repository**, not a fork GitHub tracks, and `p298` substituted the canonical slug at the identity gate. **Cite this owner.** |
| 🆕 [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** *(sidebar, read `p298`)* | **73★ / 56 forks / 523 commits / `main`** | **LTI 1.1 *and* 1.3 authenticators that make JupyterHub an LTI Tool Provider** — students reach the hub only through a compliant platform, never directly. Its README names **Canvas, Moodle, Open edX and Blackboard**. 🟢 **It sits directly under [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (8.4k★, the highest-adoption permissive row on this file) and under both permissive notebook autograders** (`nbgrader`, `otter-grader`): this is the row that turns a notebook teaching stack into something an institution's LMS can launch. 🔵 **BSD-3-Clause, the same grant as the `jupyterhub` and `nbgrader`/`otter-grader` rows it sits with — the notebook teaching lane is now permissive from authentication to grading.** |
| 🆕 [amp-up-io/qti3-item-player](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** *(sidebar, read `p298`)* | **30★ / 6 forks / 596 commits / `main`** | 🟢 **THE FIRST QTI ROW IN THIS BASE — the assessment-item layer was at zero for 297 passes.** A browser component that loads and renders **1EdTech QTI 3** items, saves item state, and runs response scoring. README says *"classroom assessment settings"*. 🔵 **Why it matters more than its star count:** QTI is how item banks move between systems, so without a QTI row every "migrate their assessments" conversation had to be answered with bespoke parsing. **596 commits against 30 stars.** |
| 🆕 [Kennisnet/php-qti3](https://github.com/Kennisnet/php-qti3) | 🟢 **MIT** *(sidebar, read `p298`)* | 🔴 **0★ / 0 forks / 255 commits / `main`** | **QTI 3.0 packages, tests and items in PHP** — import and export as ZIP or folder, validate, parse, generate, and edit items inside a package. 🇳🇱 **Kennisnet is the Dutch public-education ICT foundation**, so this is an EMEA public-sector grant, not a hobby repository. 🔴 **Zero stars and zero forks against 255 commits makes this the single clearest case on this file for the rule that stars do not rank substrates** — it is the only QTI **packaging** library here, and a `stars > 0` filter deletes it. Pair with `qti3-item-player`: this one builds and validates the package, that one plays it. |
| 🆕 [instructure/qti](https://github.com/instructure/qti) | 🟢 **MIT** *(sidebar, read `p298`)* | **8★ / 10 forks / 174 commits / `master`** | Ruby gem parsing **QTI 1.2 and 2.1** — True/False, Multiple Choice, Multiple Answer — exposing manifests, assessments and items to Ruby. **The legacy item formats a real migration actually meets**, as against `qti3-item-player`'s QTI 3. 🔵 **The briefing-grade detail is the authorship: Instructure publishes this under MIT while [instructure/canvas-lms](https://github.com/instructure/canvas-lms) is AGPL-3.0.** The vendor's own licence split marks exactly where the integration boundary physically lies — tooling permissive, platform copyleft. |
| 🆕 [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | 🟢 **Apache-2.0** *(sidebar, read `p298`)* | **17★ / 9 forks / 310 commits / `main`** | **LRSPipe** — standalone middleware that continually forwards xAPI Statements **one-way** from source Learning Record Stores into target stores, across one or more jobs. Filters forwarded statements by **xAPI Profile Statement Templates or Patterns**, and persists progress to the file system or Redis so an interrupted job **resumes**. 🟢 **The companion to [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) already on this table: `lrsql` stores statements, `xapipe` moves them** — which is what a data-residency or multi-tenant engagement actually needs (keep the institution's LRS authoritative, forward a filtered subset to the analytics estate). |
| 🆕 [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** *(sidebar, read `p298`)* | **6★ / 5 forks / 151 commits / `main`** | **Serves a OneRoster 1.2 API from an Ed-Fi ODS** — Data Standards **4.0, 5.x and 6.1** — exposing `classes`, `courses`, `users` and `schools`. 🟢 **This is the bridge for `Gap 309`**, which records OneRoster as *absent* from DMS v8.0 while native OneRoster 1.2 shipped in ODS/API 7.3.2: a client on the ODS/API line can speak OneRoster to a vendor **today**, from a permissive grant, without waiting on DMS. 🔵 The first OneRoster **implementation** row on this file — the standard was prose here until `p298`. |
| 🆕 [bgwdotdev/go-oneroster](https://github.com/bgwdotdev/go-oneroster) | 🟢 **MIT** *(sidebar, read `p298`)* | **8★ / 1 fork / 237 commits / `master`** | **OneRoster-compliant REST API server in Go**, backed by MongoDB. 🔵 **It deliberately exceeds the specification: beyond OneRoster's read-only `GET` surface it supports create, update and upsert via `PUT`** — genuinely useful when the roster must be *written*, and **non-standard**, so name which of the two you are selling before a vendor conformance conversation. 🔴 **Bare-name collision: `fffnite/go-oneroster` is also on `p989`'s list and was not read** (`p298` identity gate) — cite the owner, never `go-oneroster`. |
| 🆕 [vardanagarwal/Proctoring-AI](https://github.com/vardanagarwal/Proctoring-AI) | 🟢 **MIT** *(sidebar + README, read `p298`)* | **633★ / 351 forks / 86 commits / `master`** | **The first proctoring row in this base** — vision **and** audio: eye tracking, mouth-open detection, person and phone detection, head-pose estimation, face-spoofing detection, plus speech transcription flagged against a question paper. ⚠️⚠️ **THREE BOUNDARIES, ALL QUOTED FROM ITS OWN README: face-spoofing *"accuracy is not good currently"*; speech-to-text *"might not work well for all dialects"*; and the facial-landmark model was trained on NON-COMMERCIAL datasets.** 🔴 **Never brief this as shippable proctoring software. It is a complete reference implementation of the capability** — and the dialect caveat lands hardest in exactly the LATAM, African and Indic engagements this base places most of its work in. 🔴 Any deployment touching student evaluation is **EU AI Act Annex III high-risk** (`T-p296a`). |
| 🆕 [baoguangsheng/fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) | 🟢 **MIT** *(sidebar, read `p298`)* | **436★ / 85 forks / 76 commits / `main`** | **Zero-shot detection of machine-generated text via conditional probability curvature — ICLR 2024** (*"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"*). Ships a local demo scoring how likely a passage is machine-generated, plus experiment scripts across several models. 🟢 **The only row in this base's integrity layer with a peer-reviewed method behind it**, which is the difference between an instrument and a hunch when a student contests a finding. 🔴 **Its README names no education use** — shelved as a substrate. ⚠️ **Zero-shot detectors carry false-positive rates that harm non-native writers: never wire this to an automated penalty, only to a human review queue.** |
| 🆕 [automoss/automoss](https://github.com/automoss/automoss) | 🟢 **MIT** *(sidebar, read `p298`)* | **157★ / 26 forks / 791 commits / `main`** | Local web app (via `make run` or Docker) that **automates Stanford MOSS code-similarity runs across a whole set of assignments**, with a user manual. README says *"computer science assignments"*; the repository's own topics say `academic-dishonesty` and `plagiarism-detection`. 🟢 **Composes with [dolos](https://github.com/dodona-edu/dolos) above, and the composition is the point: two independent similarity engines agreeing on one submission set is a defensible integrity finding — one engine is an accusation.** 791 commits against 157 stars. |
| 🆕 [Gego-K12/gegok12](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** *(`main/LICENSE`, `1 150` B, payload read + diffed, `p274`; 🟢 **re-read at a NEW pin `p295`** — `99da145f55a17d26ac2d67ae258a4f9beb385874`, `LICENSE` `200`, **1 150 B**, sha256₁₂ **`b8694396d7dc`**, title `MIT License` — **byte size identical, the grant has not moved**)* ⚠️ **its GitHub sidebar shows a License link with NO LABEL** — `p267`'s signal fires here on the plainest possible payload, so **the signal is not specific and this row is NOT downgraded by it** — ⚠️ **core only: 12 Pro modules sold separately** | 🔴 **54★ / `101` forks / `123` commits** *(re-read `p295` — the cell carried **98** forks and self-declared "no star read this pass"; it was the best-labelled target in this file and it was wrong)* | **Self-hosted school ERP / SIS** on PHP 8.4 + Laravel. 🟢 **The permissive SIS layer this base has said for nine passes does not exist** — and the reason it was missing is that the base probed a slug that does not resolve, twice (`T44`). 🔵 **Its fork network is its adoption evidence**: 98 forks, near-zero fork stars, institution-shaped fork names across **India, Indonesia and Vietnam** (`P933` — software institutions RUN rather than developers EXTEND). ⚠️ **Deployment-placed APAC; origin not established.** ⚠️ **Price the Pro modules before the SOW** |
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | **Interactive learning with automated feedback**, from TUM Applied Education Technologies. Programming, quiz, modelling and text exercises with automatic assessment and an integrated CI runner. The strongest MIT-licensed teaching platform found this pass — production-grade and university-maintained. **Pass 266:** it ships three *config-gated* AI subsystems — **Iris/Pyris** (the LLM tutor and the microservice behind it: 🔴 **`p283`: ONE repository, [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), MIT** — `ls1intum/Iris` is a name alias of it, not a second subsystem; `p282` established the identity and corrected `agents/top.md`, `compose/patterns.md` and `verticals/solutions.md`, and **this row was missed**. *Iris* is the user-facing name of the tutor Pyris powers) and **Athena** (feedback suggestion, [`ls1intum/Athena`](https://github.com/ls1intum/Athena), 🟢 **MIT at metadata grade since p275** — no licence *file* exists (tree enumerated, 691 paths) but **12 of 14 manifests declare `license = "MIT"`**; the earlier *"all-rights-reserved"* verdict is retracted), plus **Hyperion** (AI exercise authoring, not a separate repo). Config-gated matters: the platform runs identically with AI off, which is the posture an EU AI Act high-risk classification wants. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | 4.1k | FSRS, the modern spaced-repetition scheduler. The highest-adoption learning-science component in open source. Pair with [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) (BSD-3-Clause) for a Rust core you can embed. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 450 | The reference PyTorch knowledge-tracing benchmark library: standard datasets, standard splits, comparable baselines. If a client asks "can you predict what this student knows", this is the honest starting point. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | 🟢 **MIT** *(sidebar, re-read `p296`)* | **352★ / 48 forks / 3 838 commits / `main`** *(`p296` — the row carried stars only)* | Source-code plagiarism detection (**Ghent University**, Team Dodona). In the GenAI era this is no longer a niche: it is the integrity layer every coding course now needs. 🟢 **`p296` adds the three numbers that make it rankable: `3 838` commits makes this the most-developed EMEA-origin permissive substrate on this file**, and `p296` also read that it ships in **three consumption shapes — CLI, interactive visualisations, and a usable JavaScript library** — so it drops into a pipeline, a dashboard or a marking workflow **without a fork**. Use the JS library when the integrity result must land in the client's own record rather than a separate tool's UI. Composes with `autolab/Autolab` below: Autolab runs the submission, Dolos is the evidence. See `P52`. |
| [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | Apache-2.0 | 313 | Education datasets plus download/preprocess tooling. Removes the first two weeks of any learner-modelling project. |
| [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT | 82 | Knowledge tracing **plus** cognitive diagnosis **plus** exercise recommendation in one library. Broader than pyKT where the deliverable is a recommender, not a predictor. |
| [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) | MIT | 78 | Unified library for student cognitive modelling, with a configuration-driven pipeline. Good for sweeping many models when the client wants a comparison, not a bet. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | Apache-2.0 | 215 | Maths and science e-assessment: randomised questions, algebraic marking, SCORM-packaged output. Apache-2.0 makes it embeddable in a commercial deliverable. **Pass 266:** 215★, 4,209 commits, 130 forks, **Newcastle University** School of Maths, Stats & Physics (README-quoted → EMEA-origin). Tests run **entirely in the browser** — a Python 3 compiler producing a JavaScript runtime — so no student submission need leave the device. That answers a data-residency objection structurally rather than contractually. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | — | Framework for building **LTI** tools that plug into any compliant LMS. The sanctioned way to put an AI tool inside Moodle/Canvas/Open edX without forking the LMS. |
| ⬆️ [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 525 B, sha256₁₂ `a1587287ff04`, read `p300`)* | **955★ / 402 forks / 1 835 commits / `master`** | The xAPI (Experience API) specification itself — the vocabulary for *"what did this learner actually do"* across systems. 🔴 **`p300` UPGRADED THIS ROW FROM UNGRADED TO PAYLOAD, AND READING IT FOUND THE LAYER'S BIGGEST QUALIFICATION: this repository holds 1.0.3 ONLY.** Its own README states that the current version is **xAPI 2.0**, that the specification's home has moved to **IEEE** (`opensource.ieee.org/xapi/xapi-base-standard-documentation`), and that *"the next version of the specification has not been planned."* 🔵 **So the highest-starred xAPI artefact on this shelf is a superseded version of the standard, still carrying 955★ and 402 forks** — the Caliper shape from `p299` in a milder form: not withdrawn, but relocated, and only the repository's own text says so. 🟢 The permissive 2.0-capable row is [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs), above. 🔵 **Byte note:** its 11 525 B against the stock 11 357 B is **entirely encoding** — 200 CRLFs, minus one trailing newline, minus 31 title-line spaces = exactly 168 B. Same grant, and `rider_restriction` is empty. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | — | SQL-backed **Learning Record Store** for xAPI. The missing piece between an agent that observes learning and a model that needs training data. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | — | Modern SCORM 1.2 / 2004 and AICC runtime. Most institutional content is still SCORM; this is how an agentic front end keeps reading it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | MOOC portal CMS (Django + React) from France Université Numérique. MIT means the client's catalogue front end is genuinely theirs. |
| [openfun/marsha](https://github.com/openfun/marsha) | MIT | — | Video management for education, same FUN-MOOC provenance. The companion to Richie when the course is video-first. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | MIT *(payload-measured **1,094 B**, `main/LICENSE`, pass 272)* | — | Student information system (Laravel): enrolment, attendance, results. MIT SIS data is the input every dropout-prediction model needs. |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | Apache-2.0 | — | HAX authoring/CMS for web-component-based course content. Content as components survives an LMS migration; content as LMS pages does not. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 *(README-stated — see note)* | — | The component API for Open edX. The entry point for putting an agent inside an Open edX course. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** | 46 | **The K-12 student-data standard of North American public education, and it is permissive.** *"Serves as the foundation for enabling interoperability among secure education data systems."* 370 commits on `v6.2.0`. The vocabulary a US district or state agency already models its students in — so an AI deliverable that speaks Ed-Fi needs no bespoke integration per district. ⚠️ **Neither this README nor `Ed-Fi-ODS`'s names a single US state or education agency** — see the provenance note below before any state count reaches a deck. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | **Apache-2.0** *(payload at `LICENSE.txt`, not `LICENSE`)* | 28 | The Operational Data Store and ODS API — the running system behind the standard. 1,054 commits, and **48 forks against 28 stars**: forks exceeding stars is the deployment signature this file named on Submitty. The permissive **system of record** that the "North America publishes no education platform" framing said did not exist. |
| [Ed-Fi-Alliance-OSS/Data-Management-Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** | — | The ODS/API's declared successor. ⚠️ **Price this one from the register, not the README:** `intel/open-gaps.md` (`Gap 303`) establishes from `docs/PRD-v8.0.md` that it is *"a ground-up rewrite"* and that adoption is a **re-platforming with a data migration, not an in-place cutover**. `Gap 314` adds that provisioning is **create-only**, so any AI deliverable writing back to the system of record — a predicted risk flag, an AI-assisted grade — is a **data-model extension and a re-provision**, not an insert. |
| [Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** *(payload at `LICENSE.txt`)* | — | End-user applications and extensions over the ODS/API. The deployment surface of the row above. |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 6.9k | Full online learning platform built for low-resource contexts: structured lessons, built-in formative feedback, learner-progress model. **17,004 commits** on `develop`. The highest-adoption *permissively licensed* complete learning platform located by this KB — larger than Artemis and larger than every education agent except DeepTutor. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1.4k | *"A system for assigning and grading notebooks."* **Autograding that already exists.** This file previously declared that no high-adoption open-source grading option was found; nbgrader is 1.4k stars, BSD-3-Clause and the default in university data-science teaching. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1.2k | *"the offline app for universal education"* — a complete learning platform that runs with **no internet connection**, syncing when a link appears. **39,803 commits.** MIT, which makes it the second permissive complete platform in this KB and the only one designed for intermittent connectivity. The natural base for rural LATAM and low-bandwidth APAC deployments. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | 🟡 **Apache-2.0 — `README-ONLY` grade** *(`p296`: README states *"Autolab is released under the Apache License 2.0"*; 🔴 **the GitHub sidebar shows a License link with NO licence name**, so no classified label and no payload were read)* | **808★ / 234 forks / 2 179 commits / `master`** *(`p296` — the row carried stars only)* | *"Course management service that enables auto-graded programming assignments."* Initially developed by students at **Carnegie Mellon University** per its README. Apache-2.0 autograding with a course-management shell around it — the permissive counterpart to Artemis. 🔴 **`p296` DOWNGRADES this row's grade without downgrading its usefulness:** the cell published a bare `Apache-2.0` as though it were classified, and it is **README prose only** — this base's `p267` signal (unlabelled sidebar licence) fires here, and unlike `Gego-K12/gegok12` there is **no payload read behind it**. ⚠️ **Request the `LICENSE` file in writing before this becomes a dependency.** ⚠️ Default branch is **`master`** — a ladder probing `main` reads nothing and reports an absence. |
| [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** | 41 ⚠️ | **India's national education stack — the APAC-origin platform this KB said did not exist.** The codebase under **DIKSHA**, run by NCERT/Ministry of Education. README: *"next-generation scalable open-source learning solution for teachers and tutors"*, mission *"improve learning outcomes for 200 million children across India"*. **38,046 commits, 317 forks — against 41 stars.** ⚠️ **Do not read the star count as adoption**: ministry-funded digital public infrastructure accrues commits, forks and deployments but almost no stars, which is precisely why star-sorted search never surfaced it. Backend: [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) (MIT). Mobile: [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). |
| [oppia/oppia-android](https://github.com/oppia/oppia-android) | Apache-2.0 | — | The Android client beside `oppia/oppia`. Pairs with `learningequality/kolibri` (MIT) wherever mobile-first, low-connectivity delivery is the actual constraint rather than an afterthought. |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | **BSD-3-Clause** — ⚠️ **the payload is at `LICENSE.md`; plain `LICENSE` is `404`** *(`p295`, pin `81fb6a2334633ad0fe6148c201e04160db6a9bdb`, `1 542 B`, sha256₁₂ **`c123708cb4ef`**, title `BSD 3-Clause License`)*. **Third licence-path spelling on this shelf** after `DFE-Digital`'s `LICENCE` and `Ed-Fi`'s `LICENSE.txt`, and GitHub reports **two** licence entries, not one | 802 | *"Homework Submission, Automated Grading, and TA grading system."* From the **Rensselaer Center for Open Source Software** in RPI's CS department (README-quoted → NA-origin). **9,316 commits** *(🟡 `9,321` at `p295` — drift, not a correction)*, **and 1.1k forks against 802 stars** — forks exceeding stars is the signature of software that gets *deployed*, not bookmarked. The most permissive licence in this base's assessment layer, and it covers submission, autograding *and* the TA grading workflow in one system. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD-3-Clause** | 161 | *"A Python and R autograding solution"* from the **UC Berkeley Data Science Education Program**. 3,825 commits. Grades scripts and notebooks, and ships **adapters for the Canvas and Gradescope autograders plus a student-side check client** — so it attaches to the LMS the client already runs instead of replacing it. R support matters: it is the one autograder here that covers statistics teaching. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** | **8.4k** | *"Multi-user server for Jupyter notebooks."* 8,913 commits, 2.1k forks. The substrate under notebook-based teaching and under both permissive notebook autograders (`nbgrader`, `otter-grader`). At 8.4k stars it is the **highest-adoption permissive row in this file** — this base had catalogued the graders without the thing they run on. |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | **Apache-2.0** | 286 | *"Enterprise open source portal built by and for the higher education community."* 17,158 commits, 278 forks. The campus portal / single-pane-of-glass layer: where an institution aggregates its systems, and therefore where an agent surface reaches the most students per integration. **Note the licence divergence inside Apereo:** uPortal is Apache-2.0, while its siblings `sakaiproject/sakai` and `apereo/opencast` are ECL-2.0 — so the educational-use patent scoping this base flagged on those two **does not apply here**. |
| [learningequality/studio](https://github.com/learningequality/studio) | **MIT** | 193 | *"Content curation tools for Kolibri"* — **Kolibri Studio**, the authoring and publishing half of the offline-first stack this file already shelves. 15,493 commits, 312 forks. Organises content into channels Kolibri can import, remixes existing channels against **national curricula**, and builds learning pathways and assessments. Without it, a Kolibri deployment is a reader with no pipeline. *Licence note: the MIT copyright line reads "(internal apps)", but the grant and condition clauses are unmodified standard MIT — reading that parenthetical as a restriction would be a false positive.* |
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** *(under Crown Copyright)* | 38 | **A national education ministry's production service, MIT-licensed.** *"A service for applying to teacher training courses"* — **34,414 commits**, run by the **UK Department for Education** at `apply-for-teacher-training.service.gov.uk`. The payload reads *"Copyright (c) Crown Copyright (Department for Education)"*. Beside it, [`DFE-Digital/teaching-vacancies`](https://github.com/DFE-Digital/teaching-vacancies) (MIT, *"Department for Education - Digital"*). ⚠️ **38 stars against 34,414 commits** — the same instrument blindness as Sunbird. ⚠️ **And the licence file is spelled `LICENCE`**: a probe trying only `LICENSE` reads this MIT service as unlicensed. |
| 🆕 [meyerjp3/psychometrics](https://github.com/meyerjp3/psychometrics) | 🟢 **Apache-2.0** *(`pom.xml` `<licenses>`, `distribution=repo`, read first-hand `p276`; **no payload in the tree** — 395 paths enumerated)* | 57 | **The permissive psychometrics layer this shelf had no answer for.** Java: IRT (Rasch/2PL/3PL/GPCM), CTT, factor analysis, finite mixture models, **IRT linking (Mean-Mean, Mean-Sigma, Stocking-Lord) and score equating**. 🔵 An adaptive-assessment engagement needs exactly this under the model layer, and `OATutor`'s BKT does not cover equating. ⚠️ Modules: `-core`, `-ctt`, `-factor`, `-fmm`, `-irt`. [evidence](../evidence/manifest-channel.2026-10-17-p276.tsv) |
| 🆕 [open-spaced-repetition/fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper) | 🟢 **MIT** *(`License` — mixed case, no extension — `1 079` B, payload read `p276`)* | 325 | **FSRS scheduling as a foundation, not a feature.** Retention-targeted interval computation, load balancing, postpone/advance, reschedule-all. 🔴 Carried as *"NO GRANT in 6 filenames"* until `p276` enumerated the tree. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| 🆕 [datakind/student-success-tool](https://github.com/datakind/student-success-tool) | 🟢 **MIT** *(sidebar, `p296`)* | **8★ / 2 forks / 3 015 commits / `develop`** | 🟢 **PROMOTED AT `p296`, and the star count is the least informative number on this row.** A **3 015-commit** Python pipeline for data-assisted academic advising: ingestion, feature creation, exploratory analysis, modelling and tests, built to surface the students who most need contact. From **DataKind**, funded by **Google.org**; README reports a senior-graduation gain at **John Jay College** (CUSP). Default branch is **`develop`** — read it there or read nothing. 🔵 **The early-warning layer `P3` and `P13` both call for, now with a permissive grant** and a named deployment outcome rather than a benchmark. |
| 🆕 [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** *(sidebar + README, `p296`)* | **0★ / 11 forks / 450 commits / `main`** | 🟢 **PROMOTED AT `p296` — the on-premise *runtime* answer, from Intel.** Reference apps, libraries, microservices and **benchmarking tools** for education AI workloads: audio and video pipelines shipped as *Smart Classroom* and *Teaching Assistant* applications, with tooling to decide **which hardware a use case actually needs**. Targets **Intel CPUs, integrated GPUs and NPUs** via **OpenVINO**. ⚠️ **0★ — this is a vendor reference stack, not a community project; its 11 forks and 450 commits are the only adoption signal.** 🔵 **Why it matters anyway:** every sovereign / air-gapped pattern on this base (`P7`, `P9`, `P12`) has had to hand-roll its inference layer. ⚠️ **It is hardware-coupled by design** — price the lock-in, and do not brief it as portable. |
| 🆕 [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** *(sidebar, `p296`)* | **12★ / 0 forks / 5 commits / `main`** | 🟢 **PROMOTED AT `p296` — and it is the first row on this file that measures *pedagogical* competence rather than code.** Two benchmarks that test how well an LLM understands **teaching**, built from **teacher-qualification exam** questions, with the extraction and preprocessing scripts included. Paper: *Benchmarking the Pedagogical Knowledge of Large Language Models* (**arXiv:2506.18710**). 🔴 **Its question bank is LATAM:** the acknowledgements credit **Chile's Ministry of Education** — *Agencia de la Calidad de la Educación* and **CPEIP** — for developing and sharing the exams. 🔵 **This is the partial answer to this base's standing "no education-specific eval" gap**, and the first time that gap has had a LATAM-sourced instrument. ⚠️ **5 commits: it is a benchmark release, not a maintained harness** — and a model that scores well on Chilean teacher-certification items has not thereby been shown to teach a Chilean child. |
| ⬆️ [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 264 B, sha256₁₂ `ccf5a4564e72`, re-read `p300`; sidebar `p297`)* | 9★ / 3 forks / **191 commits** / `main` *(confirmed exactly, `p300`)* | **The curriculum-standards layer, published by the standards body itself.** *"Implementations of CASE Server and Editor"* — CASE (Competencies and Academic Standards Exchange) **1.0 and 1.1**, and the README states it is **ready for 1EdTech certification**. 🔵 **Why this is a foundation and not a nice-to-have:** every pattern on [`compose/patterns.md`](../compose/patterns.md) that claims *"curriculum-aligned"* has so far meant *aligned to a PDF someone parsed*. CASE is the interchange format ministries and publishers actually exchange standards in, which makes alignment **checkable by a machine instead of asserted in a slide**. Promoted from `p989`'s orphan list. |
| ⬆️ [1EdTech/digital-credentials-public-validator](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 11 357 B, sha256₁₂ `c71d239df917` — the stock Apache text, byte-identical to three other rows, so **no rider**, read `p300`; sidebar `p297`)* | 17★ / 12 forks / **628 commits** / `main` *(confirmed exactly, `p300`)* | **The credentialing layer — the first row on this file that validates what a learner walks away with.** Validator for **Open Badges 3.0**, also accepting 2.0 submissions. 628 commits from the standards body. ⚠️ **Boundary, read rather than assumed:** the sidebar description also says *"Comprehensive Learner Record"*, **but the README describes Open Badges validation only.** Do not promise CLR conformance on this row until the CLR path is read at payload. Promoted from `p989`'s orphan list. |
| 🆕 [AnubisLMS/Anubis](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT** *(sidebar, read `p297`)* | **382★** / 54 forks / **1 638 commits** / `main` | **A whole autograding LMS under a permissive grant, with a named university behind it.** *"Distributed LMS for automating Computing Science Courses From NYU"* — each student gets a **GitHub repo per assignment**, pushes trigger tests, and **results are visible before the deadline**; plus one-click browser **Cloud IDEs** and *"Insights"*, which derives topic understanding from submission and test-result **timestamps**. README names **NYU Tandon**, used there for several semesters. 🔵 This is the permissive answer to *"where is the open grading platform"* that does not require entering `Artemis`'s Java stack — and the **timestamp-derived insight** is an early-warning signal that needs no extra instrumentation. |
| 🆕 [AI-for-Education/edu-qurating](https://github.com/AI-for-Education/edu-qurating) | 🟢 **MIT** *(sidebar, read `p297`)* | 3★ / 0 forks / **277 commits** / `main` | **Educational-text quality scoring, and it is the first row here that scores teaching material on PEDAGOGY rather than on readability.** A QuRating fork that scores, samples and trains over a Fineweb-Edu-fortified dataset, with a filter keeping the **top 50th percentile on three named axes: factual accuracy, pedagogical quality and lesson engagement.** Ships three templates — *Core Educational*, *Foundational Literacy – Teacher-Facing*, *Foundational Literacy – Student-Facing* — and is tied to an arXiv paper, with trained models on HuggingFace. ⚠️ **The weights are on `huggingface.co`, which is closed at this environment's resolver** (`p295`): the **code** is readable here, the **models are not**. |
| 🆕 [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | 🟢 **MIT** *(sidebar, read `p297`)* | 1★ / 0 forks / 61 commits / `main` | **Child-speech evaluation — a layer no row on any shelf here had.** Evaluates **NeMo ASR models on Early Grade Reading Assessment (EGRA)** for **Kiswahili child speech**, everything in Docker (CPU-only or GPU). 🔵 **Why a 1★ repo is a foundation row:** every literacy-tutor pattern this base has written assumes a speech front-end that works on a six-year-old in a noisy classroom, and **adult-speech WER does not predict that.** This is the instrument that measures the assumption. ⚠️ The README **names no country**; Kiswahili implies East Africa, and the row says so rather than inventing a deployment. |
| 🆕 [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | 🟢 **MIT** *(sidebar, read `p297`)* | **482★** / 135 forks / 124 commits / `main` | **The language layer for an Indian engagement.** *"Translation models for 22 scheduled languages of India"* — the README's list runs to 26 entries, 25 Indic variants (with Kashmiri, Sindhi and Manipuri appearing in more than one script) plus English. From **AI4Bharat**, whose other repositories (`IndicTTS`, `IndicWav2Vec`, `Shoonya`, `IndicLLMSuite`) remain **unshelved on `p989`'s list** and are the obvious next batch. ⚠️ **Boundary: the page mentions no education use.** It is a substrate — the thing a Hindi or Tamil tutor is *built on*, not an education instrument itself. |
| 🆕 [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | 🟢 **MIT** *(sidebar, read `p297`)* | **3.0k★** / 827 forks / **8 033 commits** / `main` | **The evaluation harness this base has declared a gap for several passes — and it is a government's.** *"Inspect: A framework for large language model evaluations"*, from the **UK AI Security Institute** (`UKGovernmentBEIS`). **8 033 commits** makes it the deepest history admitted to this file this pass by a factor of five. 🔴 **Boundary, and it is the reason this row is NOT on [`agents/top.md`](../agents/top.md): the README mentions neither education, teaching nor students.** It is a general eval framework. 🔵 It earns a foundation row because the EU's Annex III high-risk classification for student evaluation (`T-p296a`) demands **documented, reproducible evals**, and a UK-government-maintained harness is an easier artefact to defend to a regulator than a bespoke test script. |
| 🆕 [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** *(sidebar, read `p297`)* | **6.4k★** / 1.1k forks / **2 880 commits** / `main` | **The governance layer, and governance is the barrier every regional leg on [`intel/market.md`](../intel/market.md) keeps naming.** *"Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents"* — it checks whether an agent's tool call is **allowed** before it runs, binds actions to a specific agent identity, keeps **tamper-evident audit records**, and ships compliance mapping. 🔴 **Boundary: the README does not mention education.** Substrate, not an education instrument. 🔵 Against **LATAM's 30%-of-universities-have-a-published-AI-policy** figure and the EU literacy duty already in force, the auditable-log half of this repo is the part that converts a pilot into something an institution can sign. |
| 🆕 [google/prog-edu-assistant](https://github.com/google/prog-edu-assistant) | 🟢 **Apache-2.0** *(sidebar, read `p297`)* | 34★ / 17 forks / 165 commits / `main` | ⚠️ **ARCHIVED BY ITS OWNER ON `2025-07-23`, read-only — shelved WITH that written down, not quietly.** *"An easy system to create autograding tests in Jupyter Python notebook and deploy to cloud"*: autograding for Python courses run in Jupyter or Colab, with three execution modes — inside the student notebook, hosted on Google Cloud Run, or by script. 🔵 **Why an archived repo is still a row:** Apache-2.0 is irrevocable, the notebook-autograding shape is stable, and for a client teaching Python in Colab this is a **complete worked reference** — 165 commits, Google's. 🔴 **Never brief it as maintained.** Vendor the pattern; do not take a dependency on it. |

**89 permissive foundation rows, counted by enumerating the table at `p300`.** The arithmetic closes
exactly: **61** (the table as `p298` left it) **+ 15** (`p299`'s admissions, which never reached this
table and were **restored here by `p300`** — marked ♻️) **+ 13** (`p300`'s own new rows, marked 🆕) =
**89**. Three further rows were **upgraded, not added** (marked ⬆️): `adlnet/xAPI-Spec`,
`1EdTech/OpenCASE` and `1EdTech/digital-credentials-public-validator`.

🔴 **`p300` CORRECTION, AND IT IS THE SECOND TIME THIS SENTENCE HAS DRIFTED.** It read *"48
permissive foundation rows, re-enumerated at `p297`"* while the table held **61** — thirteen behind,
because `p298` added thirteen rows and did not re-sum. 🔴 **That is precisely the defect `p297`
corrected one pass earlier**, quoted immediately below, and it came back in the very next pass. 🔵 So
the lesson `p297` drew was right and insufficient: *"count the table, don't carry the sum"* is a rule
a pass has to remember, and [this base's own Makefile header](../Makefile) says the quiet part —
**a rule that has to be remembered is not a control.** The count belongs in `recount`, which is
registered below as `ACTION PG-5` item 4 rather than claimed as done.

🔴 **`p297` CORRECTION, kept on the record: this sentence read *"31 permissive
foundation rows"* and had done for several passes — the table held 39.** The figure was written as a
sum of the passes that had added rows (17 at `p264`, 4 at `p265`, 6 at `p267`, 4 at `p268`) and then
never re-summed as later passes appended, so it drifted exactly like the star cells `p294` refuted.
**It is now a COUNT OF THE TABLE, measured by enumerating it, not a running total carried in prose.** Pass 267's six were all found by **ranking candidates by commits
and probing named institutions and ministries by hand** — not one of them would surface in a
star-sorted topic listing. **Pass 268's four were not found by searching at all**: they were sitting
in this base's own gap register, Apache-2.0 and payload-read, while this file had no row for them.
🔵 **The cheapest source of new shelf rows this pass was the base itself.**

> **Note on XBlock:** the repository's `README.rst` states *"The code in this repository is
> licensed the Apache 2.0 license unless otherwise"* and points at `LICENSE.txt`, but that
> path did not serve a payload on the raw paths tried this pass. The licence is therefore
> **README-stated, not payload-read** — the weakest evidence grade in this file, and marked
> as such rather than quietly promoted.

## Copyleft foundations — real, but priced

> 🆕 **Pass 274 adds [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen) — `GPL-3.0` at payload
> (`35 149` B, reproduced from this base's own `p195` census) — AND FLAGS ITS OWN README.** The README
> carries a **`License: MIT` badge that links to that GPL-3.0 payload**. 🔴 **A studio reading the badge
> would carry GPL-3.0 code into a deliverable believing it was MIT**, and this is a *platform-grade*
> artefact, not a snippet: a **learner-owned two-role e-learning platform**, shipped to production as
> `2.0.0`, with an authoring orchestrator that builds a private course from a one-sentence goal, a
> **course-scoped RAG tutor with lesson citations and a visible tool-call trace**, BYOK across four
> providers with envelope-encrypted keys, and **an MCP server registered in the official MCP registry**
> as `io.github.ahmedEid1/lumen`. 🔵 **The badge/payload split is `T9`'s species at its most expensive
> location — the project's front door** — and it is the inverse of `T9`'s `Open-TutorAi` case, where an
> alarming phrase turned out to be harmless boilerplate. **Here a reassuring badge is the error.**
> 🟢 **Usable across an HTTP boundary like any GPL-3.0 platform on this shelf** (GPL-3.0 has **no**
> network clause, unlike the AGPL rows); **not usable as a code base for a proprietary deliverable.**
> ⚠️ **Ask upstream which one is intended before anything else** — one of the two is a mistake, and
> `T27` says a grant nobody chose deliberately is the one most likely to move.


| Repo | Licence | Why you still care |
|------|---------|--------------------|
| [datawhalechina/ai-edu-for-kids](https://github.com/datawhalechina/ai-edu-for-kids) | **CC-BY-NC-SA-4.0 — README prose only, NO payload** *(new in pass 269)* | *"面向中小学的人工智能通识课开源课程"* — an open-source **AI general-education course for primary and secondary schools**, 128★ / 27 forks / 57 commits. 🔴 **It is the most-adopted primary-band AI-curriculum artefact this base has located, and it is the one licence form a studio cannot use: NonCommercial *and* ShareAlike.** No `LICENSE` file resolves on 19 paths; the claim lives in the README body. 🔵 **Why you still care: as a CURRICULUM SPECIFICATION it is free to read.** Pattern `P17` already exists for exactly this case — originate the content yourself on a free engine, using sources like this one to establish *what* a Class-3–8 course must cover rather than shipping its text. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | **The largest education codebase this KB has located — 78,765 commits — and it was missing from this file entirely.** *"The open LMS by Instructure, Inc."* 6.9k stars, 3.0k forks. Canvas is the dominant LMS in North American higher education **and it is open source**, which makes "North America is a proprietary-LMS market" a briefing error this file could have produced. AGPL-3.0: the network clause reaches a hosted deployment, so the integration boundary (LTI, the Canvas API, or `canvas-mcp` under MIT) is where the engagement lives — not a fork. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(in `COPYING.txt`, not `LICENSE`)* | The world's most deployed LMS and the largest plugin ecosystem in education. GPL is survivable because the integration point is a plugin boundary. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | MOOC-grade platform behind edX. **This base previously published Apache-2.0 for this repo — that was wrong, and the error mattered**: AGPL's network clause is exactly the kind of obligation a hosted-deployment engagement must price in from day one. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 *(prior cell said GPL-2.0)* | Lightweight LMS with deep LATAM public-sector deployment. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | The institutional LMS of the German-speaking EMEA market. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | School management / SIS. Attendance and behaviour data — the signal dropout models actually run on. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | K-12 student information system, light footprint, widely self-hosted. |
| [Vacademy-io/vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Modern e-learning platform with assessment management. AGPL network clause applies. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 *(re-read at its true default branch **`2.12`**, not `master` — `p281`)* | **Brazilian school-management system, and the LATAM-origin foundation this file previously said did not exist.** Originally built by the *prefeitura de Itajaí (SC)* and published on the Brazilian federal **Portal do Software Público in 2008** for Secretarias de Educação nationwide. 719 stars, **550 forks** *(forks re-read `p295`; never previously published — **76 %** of the star count, the municipal-deployment signature)*, **34,948 commits**, last commit **2026-10-14**. Laravel/PHP. Government provenance is exactly what Brazil's digital-sovereignty guidance asks for. |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | AGPL-3.0 | The teacher-facing portal for i-Educar (*portal do professor*), last commit **2026-10-09**. **Note for legal review: the licence payload in this repo is a Portuguese translation of the AGPL-3.0 text, not the FSF's English original.** FSF translations are unofficial; cite the English AGPL-3.0 in any SOW. AGPL's network clause applies to a hosted deployment. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 | Lecture capture and academic video management, university-consortium maintained. ECL-2.0 is Apache-derived and OSI-approved but scopes its patent grant to educational use — the same distinction this KB flagged on Sakai. |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 | Autograding platform from UCLouvain. The EMEA counterpart to Autolab, at an AGPL price. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0** | Interactive content types (the H5P authoring ecosystem embedded in Moodle, Canvas and Drupal). **H5P is widely cited — including in earlier Globant KB cycles — as MIT. The PHP library's payload is GPL-3.0.** Content authored *with* H5P is yours; the library you ship is not permissive. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Web conferencing built for teaching (breakouts, whiteboard, LMS integrations). LGPL means linking is survivable; modification is not free. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 | School ERP on the Frappe stack: admissions, fees, assessment. The Frappe/ERPNext alternative to OpenEduCat's Odoo lineage. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | Frappe Learning. AGPL network clause; pairs with `frappe/education` when the client is already on ERPNext. |
| [OpenBoard-org/OpenBoard](https://github.com/OpenBoard-org/OpenBoard) | GPL-3.0 | Interactive-whiteboard software (Geneva-origin) with pt-BR localisation. Classroom-front-end, not server-side; GPL is rarely a problem for a desktop deployment. |
| [oat-sa/package-tao](https://github.com/oat-sa/package-tao) | **GPL-2.0** | **TAO** — an open-source e-testing platform for authoring and delivering assessments, *"created by the University of Luxembourg"* and maintained by **Open Assessment Technologies** (README-quoted → EMEA-origin). Core framework: [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core), same GPL-2.0 payload. The permissive-assessment shelf (Artemis, Numbas, Submitty, otter-grader) does **not** include it — TAO is copyleft, and at GPL-2.0 it is not even AGPL-compatible. ⚠️ **Secondary sources routinely tie TAO to large-scale international assessment programmes; its README makes no such claim and this KB asserts none.** Verify any programme reference with OAT before it reaches a client deck. |
| [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) | **AGPL-3.0** | The server half of the **German school-cloud** stack — *"Schulcloud-Verbund-Software-Server"*, **16,192 commits**, 81 stars. Front end: [`hpi-schul-cloud/nuxt-client`](https://github.com/hpi-schul-cloud/nuxt-client) (AGPL-3.0). The nearest thing this base has to a *European public-sector school platform*, and a working reference for data-protection-first school IT. ⚠️ **Provenance is org-handle grade only:** the handle is `hpi-schul-cloud` and the README links `dbildungscloud.dev` docs, but **the README names no ministry, no funder and no Land.** Do not brief it as a federally-funded programme on this evidence. ⚠️ The GitHub sidebar shows a License link **with no label** — the payload is the only licence evidence that exists here. |
| [Tangerine-Community/Tangerine](https://github.com/Tangerine-Community/Tangerine) | **GPL-3.0** | *"Open-source software platform designed to support data collection in low-resource settings, especially in education."* **8,064 commits.** Offline-first assessment on tablets and phones that syncs when connectivity appears, built originally for early-grade reading and maths. The **assessment** counterpart to Kolibri's offline *delivery* — together they cover the low-connectivity lane end to end, at a GPL-3.0 price on this half. The logo is a registered trademark of **RTI International** (the only institutional statement the README serves). ⚠️ README claim, not independently verified: *"more than 5 million assessments and surveys across 65 countries and more than 80 organisations"* — **no country list is served**, so no specific national deployment is asserted. |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | **SPLIT LICENCE — read the payload, not the label** · *holder 🟢 `FILLED` (`p281`): `2021-present PrairieLearn, Inc.` jointly with `2013-2021 University of Illinois Board of Trustees`* | *"Online problem-driven learning system"*, 12,061 commits, 519 stars, 404 forks, UIUC in the copyright line. **This row exists as a warning as much as a recommendation.** The GitHub sidebar shows a License link *with no label*, and the payload partitions the tree four ways: the **Community Edition** (everything outside `apps/prairielearn/src/ee/`) is **AGPL-3.0**; `apps/prairielearn/src/ee/` is the **Enterprise Edition under its own separate licence**; **all client-side JavaScript**, served or compiled, is **AGPL-3.0**; and portions copyright UIUC and outside contributors are **MIT**. Any single-label cell — "AGPL-3.0" included — is wrong in two directions at once. |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | **MIT, with exceptions — one of them commercial** | The Runestone interactive-textbook platform. The grant is MIT, but the payload's **first paragraph** excepts, among others, the **Handsontable component, which is commercial software**: *"if you make a copy of this software, you must contact https://handsontable.com/ to verify your compliance with their license."* Two textbook texts also carry their own terms (GNU Documentation License; a publisher's copyright). **An MIT headline over a paid dependency** — exactly the shape that passes a licence audit and fails a procurement review. |
| [code-dot-org/code-dot-org](https://github.com/code-dot-org/code-dot-org) | **Apache-2.0 OVER A PROPRIETARY CURRICULUM — read the payload, not the label** | **The largest education codebase in open source, and pass 267's "largest" cell was wrong.** *"The code powering code.org and studio.code.org"* — **215,796 commits** (read twice, independently, `p268`) — 🟡 **`215,808` when re-read `p295` (`2026-10-18`); stars and forks exact at 901★ / 538 forks.** 🔵 **A commit count DRIFTS: quote the ratio, not the integer.** That is **2.7x `instructure/canvas-lms`'s 78,765**. The GitHub sidebar shows a License link **with no label** — `p267`'s signal, and it fired correctly. The payload grants **Apache-2.0** over *"all source codes and assets"* **with one exception that swallows the deliverable**: Code.org's *"proprietary or licensed artwork, graphics, sounds, lectures, videos, logos, characters, fonts"* *"may not be used or distributed or accessed in any manner other than directly via Code.org's own web site, mobile applications, or social media channels ... **without modification or embedding in another format**."* And the `NOTICE` says why Code.org could not grant them even if it wanted to: the curriculum is built on **licensed entertainment IP** — Minecraft (Microsoft), Star Wars (Disney/Lucasfilm), Frozen (Disney), Ice Age (20th Century Fox), Angry Birds (Rovio), Plants vs. Zombies (PopCap), The Amazing World of Gumball (Cartoon Network), The Bad Guys (DreamWorks) — plus **Font Awesome Pro** and the Geist font (SIL OFL). 🔵 **So the engine is permissive and the lessons are not.** See `Gap 367` below: this row is the answer to it, and the answer is not the one that was being searched for. |
| [pressbooks/pressbooks](https://github.com/pressbooks/pressbooks) | **GPL-3.0** | Open-textbook authoring and publishing (WordPress-based). Shelved with a companion measurement: [`openstax/os-webview`](https://github.com/openstax/os-webview), the front end of the **OpenStax** open-textbook programme, declares **AGPL-3.0** in `package.json` (metadata grade — it serves no licence file). **The open-textbook layer is copyleft on both rows measured this pass**, which is worth knowing before an OER engagement is scoped as permissive. |

## What to reach for, by job

- **"Put an AI tutor inside our existing LMS"** → 🆕 **pick the LTI library by the runtime you already
  have, not by the LMS**: `ltijs` (Apache-2.0, TypeScript), `1EdTech/lti-1-3-php-library` or `tsugi`
  (both Apache-2.0, PHP), `dmitry-viskov/pylti1.3` (MIT, Django/Flask), `jupyterhub/ltiauthenticator`
  (BSD-3-Clause) when the deliverable is notebooks — or `openedx/XBlock` for Open edX specifically.
  **Do not fork the LMS.** *(`p298` — before this pass the only answer here was PHP.)*
- 🆕 **"Migrate / exchange their assessment items"** → `amp-up-io/qti3-item-player` to play QTI 3,
  `Kennisnet/php-qti3` to build and validate the packages, `instructure/qti` to read the **QTI 1.2 /
  2.1** legacy items a real migration meets. *(`p298` — this layer was at zero rows.)*
- 🆕 **"Roster our students between systems"** → `Ed-Fi-Alliance-OSS/edfi-oneroster` to serve
  **OneRoster 1.2** off an Ed-Fi ODS (the `Gap 309` bridge), or `bgwdotdev/go-oneroster` for a Go
  server — ⚠️ the latter adds non-standard `PUT` writes, so say which surface you are selling.
- 🆕 **"Move learning events without moving the system of record"** → `yetanalytics/lrsql` to store,
  🆕 `yetanalytics/xapipe` to forward a **Profile-filtered** subset onward. This is the permissive
  answer to a data-residency objection.
- **"Automatically assess student work"** → `Artemis` for programming and modelling, `Numbas` for maths.
- **"Tell us which students are at risk"** → `academico` or `GibbonEdu` for the data, `pykt-toolkit` or `pyedmine` for the model, `lrsql` + `xAPI-Spec` for the event stream.
- **"Make retention stick"** → `fsrs4anki` / `fsrs-rs`. Spaced repetition is the one intervention with a scheduler worth reusing instead of inventing.
- **"We must prove academic integrity"** → `dolos`, 🆕 **plus a second independent engine**:
  `automoss/automoss` for code (two engines agreeing is a finding; one is an accusation), 🆕
  `baoguangsheng/fast-detect-gpt` (ICLR 2024) for machine-written prose — ⚠️ **into a human review
  queue, never an automated penalty**, because zero-shot detectors misfire on non-native writers. 🆕
  `vardanagarwal/Proctoring-AI` is the **reference implementation** of proctoring, not a product: its
  own README disqualifies its face-spoofing accuracy and warns on dialects.
- **"Our content is all SCORM"** → `scorm-again`, and keep the content where it is.
- **"Grade programming work automatically"** → `Submitty/Submitty` (BSD-3) where submission, autograding *and* TA grading must all be covered, `autolab/Autolab` (Apache-2.0) for a course-management shell with autograding, `jupyter/nbgrader` (BSD-3) or `ucbds-infra/otter-grader` (BSD-3, also R) where the work is notebooks, `Artemis` (MIT) where feedback matters more than marks. **Five permissive options, none of them an agent** — this is a solved, copyleft-free problem.
- **"The client runs Canvas"** → do **not** start from `instructure/canvas-lms` (AGPL-3.0, 78,765 commits). Reach it through its API — `vishalsachdev/canvas-mcp` (MIT) for an agent surface, LTI via `tsugi` for a tool — and keep your deliverable outside the AGPL boundary.
- **"Notebook-based data-science teaching"** → `jupyterhub/jupyterhub` (BSD-3) for the substrate, then `nbgrader` or `otter-grader` on top. All BSD-3: the whole lane is permissive end to end.
- **"We are a ministry or a public agency"** → the precedent is real and MIT: `Sunbird-Ed/SunbirdEd-portal` (India, 38,046 commits) and `DFE-Digital/apply-for-teacher-training` (UK, 34,414 commits). Public-sector education code is **shelf-grade**, and star counts hide all of it.
- **"Our learners lose connectivity"** → `learningequality/kolibri` (MIT). Offline-first is an architecture, not a setting, and retrofitting it onto a server-rendered LMS is a rebuild.
- **"We are a US district or state education agency"** → the **Ed-Fi** stack (Apache-2.0):
  `Ed-Fi-Data-Standard` for the model, `Ed-Fi-ODS` for the running system of record,
  `Data-Management-Service` for new builds. This is the permissive North American public-sector
  layer, and it is a **data standard and API** rather than a platform — which is the correct shape
  for this market, where the LMS is already bought. ⚠️ Price DMS adoption as a **re-platforming
  with a data migration** (`Gap 303`) and any write-back as a **model extension and re-provision**
  (`Gap 314`).
- **"Deliver a K-5 or K-12 AI/CS literacy mandate"** → reach for `code-dot-org/code-dot-org`'s
  **platform** under Apache-2.0, and **plan to originate or commission the lessons**. Do **not**
  plan to reuse Code.org's videos, characters, artwork or Minecraft/Star Wars activities: the
  payload forbids it and the `NOTICE` explains that Code.org cannot grant them either. The content
  is the deliverable; the engine is the freebie. See `Gap 367`.
- **"Brazilian municipal or state network, sovereignty-first"** → `portabilis/i-educar` (GPL-2.0) for the SIS and `i-diario` (AGPL-3.0) for the teacher portal, both actively maintained in October 2026, both already inside the federal software-public lineage. Keep studio code on the permissive side of an LTI or API boundary.

## Declared gaps — and three retractions

### Retracted: "no LATAM-maintained foundational repo identified"

**This was wrong, and it was wrong in the direction that costs the studio most.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) is a Brazilian school-management
system with **34,948 commits**, a commit from **2026-10-14**, origin in the *prefeitura de
Itajaí (SC)*, and publication on the **Portal do Software Público** of the Brazilian federal
government in 2008. Its teacher portal `i-diario` committed on **2026-10-09**. The region does
publish this layer; this KB had not looked in Portuguese.

The accurate, narrower claim: **no LATAM-origin *permissively licensed* foundation and no
LATAM-origin *agent* has been identified.** i-Educar is GPL-2.0 and i-Diário is AGPL-3.0 — the
LATAM supply exists and arrives copylefted, which is a pricing question, not an absence.

### Retracted: "no high-adoption open-source grading option"

`jupyter/nbgrader` (BSD-3-Clause, 1.4k) and `autolab/Autolab` (Apache-2.0, 808, CMU-origin)
are both higher-adoption than every education *agent* in this KB except DeepTutor. What does
not exist is a grading **agent**; autograding **platforms** are permissive, mature and
boring — which is the correct thing to put in front of a regulator.

### Retracted in pass 266: "no APAC-origin education platform"

Pass 265 narrowed its APAC conclusion to this one remaining gap and briefed integration work
on the strength of it. **[`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
is MIT, 38,046 commits, 317 forks, and is the stack beneath DIKSHA** — India's national school
education platform under NCERT. APAC publishes the platform layer, at national scale, under the
most permissive licence this KB tracks.

**Why it hid for 265 passes, stated as a method defect rather than bad luck:** every leg this
base runs sorts GitHub topic listings **by stars**, and `SunbirdEd-portal` has **41**.
Ministry-funded digital public infrastructure is used by system integrators and education
departments, not by developers who star repositories. The instrument cannot see this class of
code at all.

| | Sunbird | A star-findable agent |
|---|---|---|
| Stars | **41** | 300 – 41,500 |
| Commits | **38,046** | 21 – 12,437 |
| Forks | **317** | 1 – 395 |

**Standing instruction for later passes:** rank the *platform* layer by **commits and forks**,
and probe national-programme names by hand (DIKSHA/Sunbird, i-Educar, Kolibri, Me Capacito,
Ceibal). Also note the slug trap: `Sunbird-Ed/sunbird-ed-portal` does **not** resolve — the
live slugs are camel-case, and a kebab-case guess returns nothing that looks any different
from absence.

### Still open

- **Permissive complete platforms are at least three deep, not one** *(superseded in pass 266 — see the corrected count below)*. **OpenOLAT** (Apache-2.0),
  **Kolibri** (MIT) and **Oppia** (Apache-2.0) are now all payload-verified; see
  [`verticals/solutions.md`](../verticals/solutions.md) for how they differ in scope. The
  previous "exactly one candidate" framing understated the shelf and should not be repeated in
  a pitch. Everything else at full-LMS scale is still GPL or AGPL.
- **Star counts marked `—`** were not re-verified this pass; the licence was. An unverified
  number is left blank rather than carried forward from a prior pass, because carried-forward
  numbers are how this base previously published "pykt 1.2k" for a 450-star repository.
- **~~No LATAM-maintained foundational repo identified.~~ — struck in pass 266 as an
  internal contradiction.** This bullet survived in "Still open" while the *top of this same
  section* retracted exactly that claim on the evidence of `portabilis/i-educar` (34,948
  commits, commit 2026-10-14). Both statements were published in the same file on the same
  day. The accurate version: **LATAM publishes this layer and it arrives copylefted** —
  i-Educar is GPL-2.0, i-Diário AGPL-3.0. What is still missing is a LATAM-origin
  **permissively licensed** foundation. Chamilo, often cited for its deep LATAM public-sector
  footprint, is European-maintained (Belgium/Spain) and GPL-3.0.
- **Cross-shelf consistency is now a required check.** Two contradictions were found *inside
  this base* in pass 266 — this bullet, and `agents/top.md` declaring the grading category
  empty while line 21 of this file carried an MIT automated-feedback platform. Both were
  falsifiable with one `grep`, not more searching. **Before republishing any declared gap,
  grep the other shelves for its own counter-evidence.**
- **Permissive platform count, corrected again:** with **Sunbird** (MIT) and **Artemis** (MIT)
  the permissive complete-platform shelf is **five** deep — OpenOLAT, Kolibri, Oppia, Sunbird,
  Artemis — not three and certainly not one. Each prior count was published as if final.

### Added in pass 267

- **The commit-ranked view is not a refinement of the star-ranked one — it returns different
  software.** Ranking candidates by commits and probing named institutions by hand produced
  `instructure/canvas-lms` (**78,765 commits**, 6.9k★), `DFE-Digital/apply-for-teacher-training`
  (**34,414 commits**, 38★), `uPortal` (17,158, 286★), `hpi-schul-cloud/schulcloud-server`
  (16,192, 81★), `learningequality/studio` (15,493, 193★), `Submitty` (9,316, 802★),
  `jupyterhub` (8,913, **8.4k★**) and `Tangerine` (8,064, 70★). **Stars and commits agree on one
  of those eight.** This is the same instrument defect pass 266 found with Sunbird, now measured
  across a batch instead of a single row.
- **A licence LABEL cannot carry the SHAPE of a grant, and two rows this pass prove it.**
  `PrairieLearn` is AGPL-3.0 *plus* an Enterprise-Edition directory under separate terms *plus*
  MIT-licensed portions *plus* AGPL client-side JS; `RunestoneInteractive/rs` is MIT *over a
  commercial Handsontable dependency*. Both would be mis-shelved by any single-label field —
  including this file's own `Licence` column, which is why both carry their shape in prose
  instead of a name. **Add to the method note: when the GitHub sidebar shows a License link with
  no label, that is a signal to read the payload in full, not a missing datum.**
- **`LICENCE` — the British spelling — must be in every probe's path set.** `DFE-Digital/apply-for-teacher-training`
  serves MIT at `main/LICENCE` and **nothing** at `main/LICENSE`. Any prior pass that probed this
  class of repository would have published "unlicensed" for a live, MIT-licensed government
  service. Pass 267's path set is 19 paths x 4 refs, including `.md`/`.txt` variants, lowercase,
  `COPYING`, `docs/`, `.github/`, `NOTICE` and package metadata.
- **Four of this base's five "no licence payload" rows survived that wider probe** — `ls1intum/Athena`,
  `autograder-org/autoGrader-frontend`, `os4ed/openSIS-Classic` and
  `GeminiLight/awesome-ai-llm4education` serve nothing on any of the 76 combinations. **The earlier
  calls were right, and that is worth recording as plainly as a correction would be.** The fifth,
  `learningequality/kolibri-design-system`, resolves to **MIT at metadata grade** (`package.json`).
- **Still open, and now with the instrument named:** no LATAM-origin *permissively licensed*
  foundation. Pass 267 probed the most-cited LATAM national programme directly — **Uruguay's Plan
  Ceibal — and its GitHub organisation exists with ZERO public repositories** and no public
  members. Ceibal's platforms are not open code; a Ceibal-adjacent engagement is **integration,
  not adoption**. Brazil remains the only LATAM country in this file with published education
  source, and it arrives copylefted.
- **`OpenEMIS` is not shelved, and the reason is specific:** the EMIS most associated with
  ministry deployment serves, on the repo this KB can reach, a **32-commit Docker packaging
  project with no licence on any of 76 path/ref combinations and no ministry or country named in
  it.** The application source was not located. An unshelved row with a stated reason is worth
  more than a plausible one.

### Added in pass 268

- **🔴 Correction to pass 267's headline: the largest education codebase in open source is
  `code-dot-org/code-dot-org`, at 215,796 commits — not `instructure/canvas-lms` at 78,765.**
  Pass 267 published "the largest education codebase this KB has located" on a commit-ranked
  sweep; Code.org is **2.7x** larger and was not in the candidate set, because the sweep ranked
  *repositories this base had already named* and Code.org had only ever been named as a
  **curriculum vendor** in a gap note, never as a repository. 🔵 **The generalisable defect is the
  same one pass 267 found on Canvas and did not finish fixing:** this base reliably mistakes
  *"organisation known for a product"* for *"organisation with no source."* Canvas was in "not on
  the shelf" as commercial SaaS; Code.org was in a gap note as a curriculum provider. **Both
  publish at enormous scale.** The commit figure was read twice independently (repository page and
  `tree/staging`), both times 215,796, precisely because this base has a history of publishing
  numbers it read once.
- **🟢 The Ed-Fi stack is shelved, and the reason it was missing is the most uncomfortable finding
  of the pass: it was never missing from the *base*, only from the *shelves*.**
  `intel/open-gaps.md` carries Ed-Fi across at least six numbered gaps (`286`, `303`, `309`,
  `311`, `314`, and `ACTION TM`/`TR`), records all five repositories as **Apache-2.0,
  payload-read, placed North America**, and states plainly that **Ed-Fi DMS is the only permissive
  system of record this base has found.** Meanwhile *this* file had no Ed-Fi row, and
  [`verticals/solutions.md`](../verticals/solutions.md) published, in pass 267, that public-sector
  platforms exist for three regions *"and still none for North America."*
  🔵 **This is the third cross-shelf contradiction in three passes** (pass 266 found two: the LATAM
  gap bullet and the grading-category claim). The pass-266 standing instruction — *"before
  republishing any declared gap, grep the other shelves for its own counter-evidence"* — was
  followed against the four `.md` shelves and **still missed this**, because the counter-evidence
  lives in the **gap register**, which is not a shelf. **Amended standing instruction: grep
  `intel/open-gaps.md` too, and grep for the SLUG as well as the prose claim.** Pass 268 found
  Code.org by grepping for `code-dot-org` and getting **zero hits across every `.md` in this
  repository** while `Code.org` the phrase hit four files.
- **🟡 Ed-Fi's agency provenance is NOT established, and the state count must not be briefed.**
  Neither Ed-Fi README names a US state or an education agency; the Alliance's own pages give no
  number. A third-party directory lists 14 statewide adoptions (AZ, NM, TX, TN, GA, SC, KS, NE, IN,
  MI, WI, MN, VT, DE) and search reports South Carolina's own department page naming ODS/API 7.3
  for SY2025-26 plus a Texas Education Exchange deployment — but **`ed.sc.gov` and
  `www.ed.sc.gov` both returned `getaddrinfo ENOTFOUND` from this environment, so none of it was
  read first-hand.** Shelved on the **licence**, which is payload-grade; the **adoption** is
  search-summary grade and labelled as such. This is the `OpenEMIS` discipline applied to a row
  that *passes*: the licence earns the shelf, the provenance does not earn a claim.
- **🟢 2026 roadmap detail worth a sentence in a proposal** (search-summary grade, Ed-Fi's own
  docs blog): native **OneRoster 1.2** support shipped in **ODS/API 7.3.2**, the platform moved to
  **.NET 10** ahead of .NET 8 end-of-support in **November 2026**, and Ed-Fi API v8 and Admin API
  v2.4 are on the 2026 release line. 🔵 The OneRoster item matters because `Gap 309` records
  OneRoster as *absent* from DMS v8.0 — so the rostering story differs between the ODS/API line
  and its successor, and a proposal must say which line it is quoting.
- **🔵 The permissive complete-platform count is still five.** `classroomio/classroomio` was
  recommended to this pass by a 2026-dated source as the open alternative to Moodle and edX; its
  payload is **AGPL-3.0**, consistent with what the register already carried (AGPL core, MIT `mcp`
  package, plus a `LICENSE_KEY` gate on self-hosted enterprise features). Ed-Fi and Code.org are
  **not** platforms — one is a data standard, the other a curriculum delivery system with an
  unlicensable content layer — so neither raises the count. **Three consecutive passes have now
  added permissive rows without adding a permissive platform.**

### Added in pass 269

- **🟢 Gap 367's Chinese limb — the limb pass 268 itself named as the cheapest way to falsify its
  own biggest claim — was run, and the closure HELD.** Pass 268 closed `Gap 367` (*"primary-school
  AI literacy has no permissive curriculum"*, carried ~175 passes) as **correctly empty**, on the
  licences of three **Western** sources: Code.org (Apache-2.0 over a proprietary-materials
  carve-out), MIT Day of AI (CC), `touretzkyds/ai4k12` (no payload). It then wrote down, honestly,
  that it had **not** run the gap's own costed next step — *"probe CBSE/MoE-aligned repos in Hindi
  and Chinese"* — and that a permissive Hindi or Chinese primary curriculum would reopen the gap.
  **Pass 269 ran both legs. Neither reopens it, and each fails for a different reason.**
- **🔴 The Chinese leg found the row this base had never seen, and p268's amended rule is exactly
  why.** [`datawhalechina/ai-edu-for-kids`](https://github.com/datawhalechina/ai-edu-for-kids) is
  now on the table above. 🔵 **The mechanism matters more than the row:** the *organisation*
  `datawhalechina` already appears on two shelves here — so a prose or org-level check would have
  reported this as covered — while the **slug** `ai-edu-for-kids` returns **zero hits in every file
  of this base.** That is `p268`'s `code-dot-org` finding (*"grep the SLUG as well as the prose
  claim"*) firing one pass later, in a second language, on a different organisation. **The rule is
  not a one-off patch; it is load-bearing.**
- **🔴 And the licence is a TEMPLATE DEFAULT, which is a new failure mode on this base's list.**
  `ai-edu-for-kids` carries CC-BY-NC-SA-4.0 under a `## LICENSE` heading followed by this, verbatim:
  *"注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议"* — **"note: CC 4.0 is used by default,
  you may choose another licence depending on your project."** 🔵 The most restrictive attribute of
  the most on-point curriculum artefact in this category is therefore **boilerplate carried over
  from an organisation's project template, not a decision anyone made about this course.** `T20`
  catalogues licence risk by the *shape* of a grant; this is risk from a grant's *provenance*.
  Practically: it is the kind of licence that an upstream maintainer may well change if asked, and
  the kind a studio must never assume.
- **🟢 The Hindi leg found supply — ONE BAND TOO HIGH, which restates the gap more precisely than
  it has ever been stated here.** India has the hardest deadline in this KB (AI and computational
  thinking **compulsory from Class 3**, CBSE **Circular Acad-15/2026**, implementation from the
  2026–27 session, with IIT Madras, IIT Gandhinagar and Azim Premji University named as
  contributors and NCERT approving the framework — ⚠️ search-summary grade; the circular itself was
  not read, per `p268`'s DNS finding). The permissive Indian supply this base carries —
  [`Naitik-xd/CurriculumCraft-AI`](https://github.com/Naitik-xd/CurriculumCraft-AI), **MIT at
  payload** — targets **grades 9–12**. 🔵 **So the correct form of `Gap 367` is not "no permissive
  AI curriculum" and not "a search-language artefact": it is BAND-SPECIFIC. Permissive
  curriculum-generation supply exists for the senior secondary band and not for the primary band,
  in the one country where the primary band is legally mandated.** That is a sentence a studio can
  take to a ministry.
- **🟢 Three carried APAC rows were re-measured BLIND and reproduced exactly — recorded as
  prominently as a correction would be.** `CurriculumCraft-AI` (MIT at `main/LICENSE`, 1,091 B,
  0★, 7 commits), `arjav0703/cbse-ai` (AGPL-3.0, **34,523 B — agreeing to the byte** with
  `evidence/p244-withheld.2026-10-16-p244.tsv`, and still archived), and
  `crpf-mitadt/Indian-AI-for-Education` (CC0-1.0, 7,048 B). 🔵 **`p268` warned that rewriting a
  good figure on noise is as bad as publishing a bad one. Three independent agreements, including
  one to the byte, say this base's APAC licence cells are sound.**

## Pass 280 — the bound on "no grant here" was the example's own size, and lifting it corrected the biggest count on this shelf

🔵 **Evidence:** [`channel-conflict.2026-10-18-p280.tsv`](../evidence/channel-conflict.2026-10-18-p280.tsv)
*(14 slugs, 19 columns, `MANIFEST_CAP` `14 → 250`, **0 skipped on every row**)* ·
[`package-provenance.2026-10-18-p280.tsv`](../evidence/package-provenance.2026-10-18-p280.tsv) *(192
manifests graded per package)*.

`p279` closed by making every vendored-manifest count on these shelves **a lower bound**, because a
path vocabulary is a floor. 🟢 **Two of the three bounds are now closed, and the third is named.**

| bound | p279 | p280 |
|---|---|---|
| 🔴 the **cap** — `MANIFEST_CAP = 14`, which is `ls1intum/Athena`'s own manifest count | `leemonade/leemons`: **12 declaring of 114, 100 skipped** | 🟢 **72 declaring of 114, 0 skipped** — a **6× correction** |
| 🔴 the **residual** no path convention reaches (`ui/static/pyodide/`) | *"only reachable by name … this base has no such list"* | 🟢 **reached, with no list** — the payload declares `pyodide/pyodide` in `repository` **and** `homepage` |
| 🟡 the **path vocabulary** itself | two conventions added | 🟡 **a third class added** (`.vite` `.next` `.nuxt` `.turbo` build caches), **and it is still a floor** — stated, not claimed closed |

### 🔴 `leemonade/leemons` — the same verdict, six times better evidenced

**72 of 114 manifests declare `MIT`.** The committed `LICENSE.md` (10 830 B) is **FAIRCODE**.
🔵 `p121`'s operational rule is what a studio needs here — *"a manifest licence field is a HINT; the
committed licence file is the GRANT"* — and the number of hints is now 72. 🔴 **Any manifest-reading
licence scanner returns PASS on this repository**, and the obligation it misses is non-commercial.
🟢 **42 of the 114 declare nothing at all**, which is the honest remainder: silence, not a grant.

### 🟢 The counts that did NOT move are the control

`ls1intum/Athena` reads **14 in tree / 12 declaring / 1 distinct / 0 skipped** — `p275`'s census
exactly, now reproduced by a **third** independent instrument (`p275`'s enumeration, `p279`'s walk,
`p280`'s per-package grader). 🔵 **A vendoring predicate that rejects a monorepo's own workspace
packages destroys the very count it was added to protect** — `p279` measured that when a root-name
check rejected 12 of Athena's 14 — so `Athena` is the negative control, and it is unchanged.

## Pass 279 — a vendored-path exclusion is a FLOOR, so every "no grant here" on this shelf is a lower bound

🟢 **`p278` established that *a licence file inside a repository is not the repository's licence*
(`T58`). `p279` found the same principle one channel over, and it bites harder: a MANIFEST inside a
repository is not the repository's manifest either**, and the predicate this base uses to tell them
apart is weaker than the repositories it is pointed at.

🔴 **Measured, not inferred.** `tadreeb-lms/tadreeblms` vendors `moment`, `swiper`, `tailwindcss`,
`prismjs` and three CKEditor builds **twice**, under two different directory spellings in the same
repository:

| spelling | caught by `is_bundled` before `p279`? |
|---|---|
| `public/assets/libs/…` | 🔴 **no** — the vocabulary knew `node_modules/`, `vendor/`, `third_party/`, `dist/`, `build/`, `bower_components/`, `Pods/`, `.yarn/`, `target/`, `site-packages/` and not this |
| `resources/views/backend/assetslib/libs/…` | 🔴 **no** — and still not after `assets/libs` was added, which is the point |
| `inc/libraries/…` *(LearnPress, the WordPress convention)* | 🔴 **no** |

🟢 **All three spellings are in `lib/licence_path.sh` now, with 10 new controls — 4 positive and 6
negative, so the widening cannot swallow a real workspace package** (`packages/ai-assistant/`,
`apps/api/`, Athena's `assessment_module_manager/` and `src/libs/` are all asserted NOT vendored).
The **byte-for-byte identity control against `p196`'s copy stays green**, which is how this base stops
a shared predicate becoming a fork: the suite went **44/44 → 54/54**.

🔴 **The honest consequence for this shelf: a path vocabulary can only reject the conventions somebody
enumerated, and one repository defeated it twice inside one hour.** So every vendored-manifest count
published here is a **LOWER BOUND**, and the residual is named rather than hidden —
`Open-TutorAi/open-tutor-ai-CE`'s `ui/static/pyodide/package.json`, a bundled Pyodide runtime under a
path no convention names. 🔵 **The durable channel reads a package `name` against a list of known
third-party projects. This base does not have that list.** Registered for `p280`.

🔵 **And the controls themselves taught the lesson a third time.** They were first appended **below**
the suite's `echo "$p/$t"; [ "$p" = "$t" ] || exit 1` line — so they ran, graded nothing, and could
not have failed the build. **The count gave it away: 44/44 both before and after adding ten
assertions.** Position relative to the thing that reads you is load-bearing.

---

## Pass 278 — a licence file inside a repository is not the repository's licence, and the biggest LMS plugin on this base proves it twice

🔵 **Evidence:** [`tree-enumeration.2026-10-17-p278.tsv`](../evidence/tree-enumeration.2026-10-17-p278.tsv)
*(6 trees, every path enumerated)* ·
[`channel-conflict.2026-10-17-p278.tsv`](../evidence/channel-conflict.2026-10-17-p278.tsv).

🔴 **[`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) enumerates to 1,985 paths at
`ca5296320435`, and BOTH of its licence-like paths belong to something else:**

| path | what it is | verdict |
|---|---|---|
| `inc/libraries/wp-background-process/license.txt` | a **vendored third-party library's** grant | 🔴 not the project's |
| `inc/TemplateHooks/Admin/Notices/AdminNotesTemplate.php` | a **PHP source file** matching the licence-name pattern | 🔴 not a grant |

🟢 **`pass275-grant-enumeration`'s scope test rejects both** — `VENDORED` catches the first, `SOURCEY`
the second — confirmed by running `candidate_grants()` on the enumerated paths this pass, which
returns `[]`. **So the repository commits no grant of its own, and `p120`'s resolution stands: the
licence is GPL-3.0, declared in the WordPress `readme.txt`.**

🔵 **Why this belongs on a FOUNDATIONS shelf rather than only in a licence ledger.** A client's SCA
scanner that reports *"GPL-3.0 found"* from `inc/libraries/.../license.txt` has found a **dependency's**
grant and attributed it to the parent. **An intake gate must ask whose grant a path carries, not only
which grant it is** — the mirror image of the manifest problem, where the declared field is read as the
grant. Both errors are automatic, and both default to the wrong answer.

🟢 **`p277`'s declared sub-rule `T57` is discharged on this shelf too: every absence now carries its
path count**, and the counts span three orders of magnitude (15 → 15,448). *"No licence file in 15
paths"* and *"no licence file in 15,448 paths"* are the same sentence and different claims.

🟢 **And one declared item was already closed before it was ranked.** `p277` registered the `.vue`
false-candidate class for `p278` — `learningequality/kolibri-design-system`'s **15,448** paths carry
**7** licence-like paths, every one a **Material Design icon component**
(`precompiled-icons/.../copyright/*.vue`, `mdi/license.vue`). **`p277` had already fixed it in `p277`**
(`precompiled-icons` in `VENDORED`, `.vue` in `SOURCEY`); verified here rather than assumed.

## Pass 277 — six absences on this base stopped resting on path ladders, and one of them changed meaning when enumerated

🟢 **No row on this shelf changed licence this pass.** What changed is the **grade** under six absence
verdicts, which `P275`/`P278` hold is the difference between a sayable absence and an unmeasured one:
*to sustain an absence in a tree you must ENUMERATE it; a count of zero over a path that does not exist
in that ref measures the **path**, not the content.*

Each row below was re-run first-hand this pass — `git ls-remote` for existence, then a blobless
`--depth 1 --filter=blob:none --no-checkout` clone, then `git ls-tree -r HEAD`, then every candidate
path read at payload, plus eight manifest paths. Evidence:
[`tree-enumeration.2026-10-17-p277.tsv`](../evidence/tree-enumeration.2026-10-17-p277.tsv).

| row | was carried as | now rests on | licence-like paths | manifest grant |
|---|---|---|---|---|
| [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) | *"no payload on 19 of 19 paths"* | 🟢 **310 paths enumerated** | **0** | none |
| [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) | *"(no payload)"*, `repos/foundations.md` | 🟢 **190 paths enumerated** | **0** | none |
| [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) | absence asserted, 3 lines | 🟢 **119 paths enumerated** | **0** | none |
| [`autograder-org/autoGrader-frontend`](https://github.com/autograder-org/autoGrader-frontend) | absence asserted | 🟢 **36 paths enumerated** | **0** | none |
| [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) | absence asserted, 2 lines | 🟢 **31 paths enumerated** | **0** | none |
| [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) | absence asserted | 🟡 **11 paths enumerated** | **0** | none |

🔴 **`OpenEMIS/OpenEMIS-Core` is the row where enumeration did not confirm the verdict so much as
reframe it.** **Eleven paths in total is not a codebase.** The absence is true of *this repository* and
tells a studio **almost nothing about OpenEMIS the product** — an education-management system used by
ministries. A reader told *"OpenEMIS serves no grant"* will conclude the platform is unlicensed; what
was actually measured is an eleven-file shell, which is consistent with the code living elsewhere (a
release artefact, a different org, or submodules a blobless clone does not expand).

🟢 **New sub-rule, and it is cheap to apply: publish the path count beside every absence.** An absence
over **310** paths and an absence over **11** are not the same claim, and this shelf has been writing
them in the same words. 🔵 **The counts are already being collected** — every enumeration this base runs
produces one — so this costs a column, not a probe. Registered for `p278` as `T57`.

⚠️ **One limit of the method, stated because it bounds all six rows above.** A blobless
`--no-checkout` clone enumerates the tree **at one ref** — `HEAD` — and `p269` already paid for ref
sensitivity here (`learningequality/kolibri` serves **MIT on `develop`** and **404 on `main`**). **These
six are enumerated at `HEAD` only.** A grant sitting on a non-default branch would still be missed, and
six clean trees do not discharge that. **The absences are upgraded, not closed.**

## Pass 276 — the permissive table was missing its separator, and two foundations were missing their grants

🔴 **A formatting defect first, because it hid `p274`'s own prize row.** The permissive table's
`|------|` separator sat **below** the `Gego-K12/gegok12` row rather than above it, so the row this base
spent two passes recovering rendered **as part of the table header**. Restored this pass. 🔵 **No gate on
this base reads table structure**, which is why a defect in the shape of the evidence outlived several
passes of scrutiny of its content.

🟢 **Two rows join the permissive tier, and neither came from a search:**

- **`meyerjp3/psychometrics`** — `Apache-2.0`, declared in `pom.xml` `<licenses>`. This base already
  graded it correctly at manifest grade; `p276` read the manifest first-hand and promoted it onto this
  shelf, where the **IRT-linking and score-equating** layer had no permissive answer at all.
- **`open-spaced-repetition/fsrs4anki-helper`** — `MIT`, at **`License`**: mixed case, no extension. Six
  filename probes missed it; one `git ls-tree -r` found it.

🔴 **And one absence became a procurement finding.**
[`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials)
— the **European Commission's own** European Digital Credentials reference implementation — serves **no
grant across `2 970` enumerated paths** and **no `license` element in its `pom.xml`**. Its only
licence-like files are three `licenseInfo.mustache` codegen templates. ⚠️ **An EMEA credentialing
engagement cannot build on it as open source**, and this is the first time that is stated from an
enumeration rather than from a ladder.

**State:** `QUEUE-UNENUMERATED` **124 → 70**, `VERIFIED-ABSENT` **28 → 48**, `REFUTED` **0**.


## Pass 275 — a GPL-2.0 grant was sitting at `docs/License.txt`, and the ladder that missed it had been extended four times

⏱️ **Twenty-first pass of `2026-10-17`.** Evidence:
[`tree-enumeration.2026-10-17-p275.tsv`](../evidence/tree-enumeration.2026-10-17-p275.tsv) ·
[`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv) ·
[`verified-repos.2026-10-17-p275.tsv`](../evidence/verified-repos.2026-10-17-p275.tsv).

- 🟢 **`ls1intum/Athena` is CLOSED, and it closed upward.** Carried on this shelf as *"still silent — no
  grant across 76 path/ref probes over three passes."* **12 of its 14 manifests declare
  `license = "MIT"`**, unanimous. The 76 probes were aimed at the **root** `pyproject.toml` — a 632-byte
  Poetry workspace stub with **zero occurrences of `license`**. See `T47`: **a monorepo declares its
  grant per package**, and Athena's reusable modules are exactly the packages that declare it.
- 🔴 **`os4ed/openSIS-Classic` was never unverifiable** (`verticals/solutions.md`): **`docs/License.txt`**
  serves verbatim **GPL-2.0**, HTTP 200, **17 286 B**, complete instrument, rider-cleared. The ladder
  tried `docs/LICENSE`; it never tried **mixed case + `.txt`**. The vendor comparison articles this base
  dismissed were right.
- 🟢 **Eleven carried absences are now DEFINITIVE rather than probabilistic**, because the trees were
  *enumerated* rather than sampled — and two are explained rather than merely confirmed:
  `datawhalechina/ai-edu-for-kids` has no payload because **its tree holds two files**, and
  `OpenEMIS/OpenEMIS-Core` holds **11**, confirming `p267`'s read that what this base can reach is a thin
  Docker packaging repo and **not** the ministry application source.
- ⚠️ **A licence-like path is not a grant.** `kolibri-design-system` enumerates **7** licence-like paths
  and **all 7 are Vue icon components** (`KIcon/precompiled-icons/mdi/license.vue`); openSIS carries **20**
  vendored dependency licences (ckeditor, PhpSpreadsheet, htmlpurifier); Artemis carries a
  `LicenseService.java`. The gate in `compose/code/pass275-grant-enumeration/` has a control for each.
- 🟢 **`make gate-enumeration` is now in `make hooks`** and will fail any shelf that asserts an absent
  grant an enumeration refutes. **`QUEUE-UNENUMERATED=124`** negative verdicts across this base still
  rest on a ladder — the honest size of the backlog, printed on every run.

## Pass 274 — the nine-pass nil on this file ENDS, with a row this base had refused twice

⏱️ **Twentieth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p274.tsv`](../evidence/verified-repos.2026-10-17-p274.tsv) ·
[`p274-websearch.2026-10-17-p274.tsv`](../evidence/p274-websearch.2026-10-17-p274.tsv) *(leg 9)*.

🔵 **The brief's platform/SIS/ERP leg ran and did what `p273` predicted: it re-served a claim this base
had already refuted.** 🟢 **And this time the re-service was RIGHT and the refutation was wrong.**

| what the leg returned | what `p274` established first-hand |
|---|---|
| *"GegoK12 … free, MIT-licensed open-source school ERP, built for self-hosting, PHP 8.4 + Laravel, core free forever under MIT with optional paid add-on modules"* | 🟢 **MIT CONFIRMED** at `Gego-K12/gegok12` `main/LICENSE`, `1 150` B, diffed and byte-accounted. 🟢 **The "optional paid add-on modules" half CONFIRMS this base's own open-core caveat** — so the vendor page and this base were each half right, about different things |
| Gibbon (GPL-3.0), RosarioSIS (GPL), OpenEduCat CE, openSIS, Academico, OpenOLAT (Apache-2.0) | 🔵 **All already shelved here or on [`verticals/solutions.md`](../verticals/solutions.md).** `Academico` reproduces `p272`'s MIT-at-payload finding |
| 🔴 **NOT ONE platform returned describes any AI feature** | 🟢 **Corroborates this base's standing structural read from the OUTSIDE:** the SIS/ERP layer has no AI, so the agent layer is the opening and the platform is the installed base. **An absence that confirms a thesis is worth recording as a result** |

🔴 **The method finding, and it is the one to carry forward.** Both of this file's standing refusals were
produced by probing a slug. **One slug was wrong** (`gegok12/gegok12` → `Gego-K12/gegok12`) and the
refusal recorded the probe count — *"15 path/ref combinations"* — **which reads as thoroughness and was
15 probes against a string.** ⚠️ **A negative licence result must record the slug and ref it probed AND
a positive control that the slug resolves at all** (`git ls-remote` returning refs), or it is not a
measurement. 🟢 **This base's ledger format already has the columns.** See `T44`.
## Pass 272 — no new rows, one measurement supplied, and two candidate rows refused

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) ·
[`p272-websearch.2026-10-17-p272.tsv`](../evidence/p272-websearch.2026-10-17-p272.tsv).

🔵 **This file gains no rows: the SEVENTH consecutive measured nil on education-specific supply.**
The brief's generic legs ran **last**, per `p269`'s standing instruction. Stated precisely, because *how*
it failed is the information:

- 🟢 **`academico-sis/academico`'s byte column is filled in** — `1,094 B`, `main/LICENSE`, MIT,
  *"Copyright (c) 2020 Thomas Debay and project contributors"*. The row carried `MIT | —` since it was
  shelved. 🔵 Worth noting the direction: the vendor page that surfaced it this pass says the licence
  **"is not named"**; the payload names it. **An aggregator's hedge is not evidence of absence.**
- 🔴 **`gegok12/gegok12` REFUSED** *(**SUPERSEDED** — overturned immediately below; the slug does not exist)* — an MIT claim with no payload on 15 path/ref combinations, and an
  **open-core shape** (26 of 38 modules free, 12 Pro modules sold) that would not deliver what the claim
  implies even if verified.
  🔴 **OVERTURNED IN PASS 274, AND THE SENTENCE ABOVE CONTAINS ITS OWN DIAGNOSIS: THE SLUG IS WRONG.**
  `gegok12/gegok12` **does not exist** — it fails `git ls-remote` identically to any nonexistent
  repository, so *"no payload on 15 path/ref combinations"* was 15 probes against a **string**. The
  repository is [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12), and it serves **MIT** at
  `main/LICENSE`: **HTTP 200, `1 150` B, full payload read, normalised terms diff against stock differing
  only in line-wrap column, zero rider keywords.** The `+82` B over stock accounts **exactly**: `+39`
  SPDX HTML comment, `+8` four typographic quotation marks, `+35` a longer copyright holder
  (*"GegoSoft Technologies and GegoK12 Contributors"*). 🔵 **Two instruments produced the same false
  negative and both read like a measurement:** a kebab-case slug guess (`T15`'s trap, here taking down a
  licence verdict) and a byte **ceiling** (`T39`'s proof, upward). See `T44`.
  🟢 **The open-core half of the refusal STANDS and is the only live caveat**: MIT covers the core, **12
  Pro modules are sold separately** (`T20`, failure mode 3). **Quote the grant, scope the modules.**
  🟢 **Row added below** — and note where it lands: this base's standing APAC gap is *platform supply*,
  and `P933` has already measured this repository's **98 forks with near-zero fork stars and
  institution-shaped fork names across India, Indonesia and Vietnam** — the signature of software that
  institutions **run**. ⚠️ **Deployment-placed APAC on that fork evidence; origin NOT established** (a
  copyright holder's name is not a provenance read).
- 🔴 **`projectfedena/fedena` REFUSED, reproducing `p265`** — and `p272` adds the provenance of the false
  claim: it comes from **a direct competitor's comparison page**.
- 🟡 **Two repositories were LOCATED BUT NOT RESOLVABLE, and they are recorded as an informed gap rather
  than as rows: `Bloom`** (Socratic-method tutoring) **and `Lumen`** (self-hosted, course-scoped RAG with
  citations). A GitHub topic listing named them **without an owner/repo**, so there is no slug to probe.
  ⚠️ **A project name is not a row.** Resolving these two is a cheap, named step for `p273`.
  🔴 **RETRACTED IN PASS 274 — BOTH LIMBS WERE ALREADY IN THIS BASE.**
  **`Bloom` = [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom), MIT, `1 069` B** — and it has been a
  **row on [`agents/top.md`](../agents/top.md)** since `p264`, which is where the contradiction is
  sharpest: *that* file declares the same slug unresolvable in a later section of itself, 168 lines below
  the row that tables it.
  **`Lumen` = [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen)**, resolved from this base's **own
  `p195` licence census** via [`compose/code/p196-population-diff/`](../compose/code/p196-population-diff/),
  which recorded it at **GPL-3.0, `35 149` B** — reproduced to the byte in `p274`.
  🔵 **Neither resolution needed a search; one needed a `grep` of this repository and the other needed a
  `grep` of this file's sibling.** `p272` spent a search leg on them and `p273` ranked spending another.
  **`T25` re-earned, and `T34`'s amendment — grep the other shelves before re-declaring an absence —
  failed because nobody ran it on this gap.**

🔵 **The supply conclusion is now stable across seven passes and three languages:** education-specific
permissive *agents* are scarce, the generic legs return either general-purpose frameworks this base already
holds or **learning-ABOUT-AI** teaching material, and the growth on these shelves comes from
**platforms, standards and assessment engines** — this file's actual subject — rather than from agents.
**Nothing was added to meet a quota.**

## Pass 270 note — no rows added, and the three legs that would have added them were not run on purpose

🟢 **This file gains no repositories this pass.** `p269` measured the generic supply legs
(`top open source AI agents education`, `github trending education AI`, `open source platform /
ERP / SIS`) as **saturated across four consecutive passes** — nine platforms returned, **all nine
already shelved**, zero education-specific agents — and instructed that they be spent **last, not
first**. **Pass 270 did not spend them at all.** It ran one targeted supply leg instead
(`Gap 367`'s Spanish limb), which returned **nine repositories, eight of them university student
course portfolios and the ninth already held.**

🔵 **The brief's five-repo minimum is met many times over by the table above, and nothing was added
to pad it.** An informed nil return is the honest output of a saturated channel; a padded row is
not. **Where this base's shelf-grade rows have come from for five consecutive passes is probing a
named thing by hand or grepping this repository** — not from a generic search leg.

🟡 **Where this file is still weak, restated rather than quietly inherited:**
- 🔴 **No permissive North American system of record.** The **Ed-Fi** stack remains shelved
  (`p268`), and nothing has replaced it.
- 🟢 **CLOSED in `p275` — `ls1intum/Athena` was never silent, and the 76 probes were aimed at the
  one manifest that is.** No licence *file* exists (tree **enumerated**: 691 paths, zero
  licence-like), but **12 of 14 manifests declare `license = "MIT"`**, unanimous. The ladder
  probed the ROOT `pyproject.toml` — a 632-byte Poetry workspace stub with **zero occurrences of
  `license`**. 🔵 **A monorepo declares its grant per package**, so a root-only metadata probe
  cannot see it. The *"worth an email"* judgement is inverted too: Athena needed no email, and
  `muskvdc/EduTwin-Africa` (`PRE-LICENCE`, `p269`) remains the row where asking is the only path —
  its tree was enumerated this pass as well (384 paths, nothing licence-like).
- ⚠️ **A ref-sensitivity reminder that cost a published figure once:** `learningequality/kolibri`
  serves **MIT on `develop`** and **404 on `main`**. Probe the **resolved** default ref
  (`git ls-remote --symref`), never a guessed one.
