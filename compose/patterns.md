---
industry: education
region: Global
updated: 2026-10-19
---

# Compose patterns — education

**Pass 327 · 2026-10-19.** **Eleven recipes. P14 is new and it is the first pattern in this file
whose three layers all come from one vendor** — the pre-wired K-12 stack (standards data over MCP +
Apache-2.0 teacher skills + MIT evaluators), with the Gated/Open boundary drawn as an architecture
decision rather than a licence footnote. **Every repo it names had its licence read first-hand at
p327.**

**P11 gains `dodona-edu/dolos`** (MIT, Ghent University, 3,838 commits) as the integrity engine
with a maintaining university behind it — previously this pattern named only `JPlag` and `jieplag`.
**P10 Variant A gains a model-selection gate**: `AI-for-Education/pedagogy-benchmark` (MIT, 1,143
questions from Chile's teacher-qualification exams, 920 CDPK + 223 SEND) answers "which model, in
Spanish, for teachers" with a number. **P5 gains `open-edge-platform/education-ai-suite`**
(Apache-2.0, Intel, OpenVINO, CPU/iGPU/NPU) as the on-device inference layer beside Kolibri.
**P3 and P6 gain `autolab/Autolab`** (Apache-2.0, CMU, 2,179 commits) and
`datakind/student-success-tool` (MIT, John Jay College CUSP, Google.org, 3,015 commits) as the two
US-institution-deployed artefacts for autograding and retention evidence.

**Pass 319 · 2026-10-19.** Ten recipes. Every repo named below is in `agents/top.md`,
`repos/foundations.md` or `verticals/solutions.md`, with the pass in which it was read first-hand
recorded there. Timings are engagement estimates, not measurements.

**Changes this pass. P10 is new and it is the most defensible pattern in this file**: the verified
curriculum spine, built on Brazil's `bncc-dev` stack, with a published number behind it — curriculum
hallucination **31.9% ungrounded, 2.3% when the model queries the verified dataset over MCP**. It
comes with a port variant for India, where the same artefact does not exist and a 2026-27 mandate
is arriving without it.

**P1 gains a "prove it teaches" stage**, because the evaluation layer this KB declared missing for
four passes now exists and its finding is that **LLM-judged helpfulness is not a pedagogy signal**
(`agents/top.md`). **P7 gains a per-pupil opt-out, an approval queue and a decision log**, which US
statute has turned from nice-to-have into bid-qualifying. **P5 gains two more permissive offline
components.** And the cross-cutting LTI risk now has a real alternative rather than an index —
`tsugiproject/tsugi`, Apache-2.0, 4,011 commits.

Carried from pass 317: **P8** — the permissive-LMS build on OpenOLAT (Apache-2.0), the first
pattern in this KB that does *not* require an LTI boundary. **P1 gains a FERPA-filtered retrieval
step.** **P4 gains the 2026-12-02 watermarking date and ports to South Korea**, whose Framework Act
on AI has been in force since 2026-01-22. **Every pattern now carries the `pylti1.3` concentration
risk explicitly** — one 138-star, single-maintainer MIT library is the seam in seven of eight
recipes, and that belongs in the SOW.

---

## P14 — The pre-wired K-12 stack: one vendor, three layers, and the Gated boundary as an architecture decision — NEW in p327

**Region: North America** (the data tier is US state standards). **Ports to any region for the
agent and evaluation tiers only — see *Portability* below.**

🔵 **Why this pattern exists.** Every pattern in this file from P1 onward assembles three layers by
hand: a curriculum spine, an agent that acts on it, and something that judges the output. **P14 is
the first time all three ship from one vendor with permissive code**, which changes the engagement
from *build the stack* to *integrate it and own the boundary*. 🔴 **That makes the licence boundary
the deliverable, because it is the only part the vendor has not already solved.**

### The three layers, each licence read first-hand at p327

| layer | artefact | licence | what it contributes |
|---|---|---|---|
| **Data** | `learning-commons-org/knowledge-graph` (161 ★, v1.15.0 of 2026-10-14) | 🟡 **MIT code; data per dataset *and per download*** — Open (CC BY 4.0 / CC0), Open + Gated, Gated | US academic standards by state · **state↔CCSS crosswalks with a `jaccard` score** · Math + ELA learning components · Math Coherence Map · **Eedi Misconceptions Graph** · WIDA ELD · XQ Competencies · Carnegie Skills Progressions |
| **Agent** | `learning-commons-org/agent-skills` (40 ★) and `anthropics/k12-teacher-skills` (575 ★) | 🟢 **Apache-2.0** both; `NOTICE` names **Anthropic, PBC** and **Learning Commons** | Four teacher workflows: lesson-plan creation · lesson differentiation (below / at / above proficiency) · lesson prep · **check for understanding, with distractors drawn from documented misconceptions** |
| **Evaluation** | `learning-commons-org/evaluators` (86 ★, 289 commits) | 🟡 **Code MIT · prompts + settings CC BY 4.0 · annotated corpora CC BY-NC-SA 4.0** | **19 evaluators**: text complexity (8), feedback (7, incl. **withholding answers**), graphics (2, early access), math standards alignment, critical thinking. Python + TypeScript SDKs |

### How to wire it

**1 — Stand up the data tier, pinned.** Take the **Open** datasets only. Two access routes, and
pick deliberately:

```shell
# MCP, for an agent runtime
claude mcp add --transport http learning-commons-kg \
  https://kg.mcp.learningcommons.org/mcp \
  --header "Authorization: Bearer $LC_API_KEY"
```

🔴 **Pin the version.** The repo tags releases and ships `.release-please-manifest.json`
(`{".": "1.15.0"}` at the time of this pass). **The vendor publishes its own regressions and they
are the silent kind:** v1.10.1 restored Texas↔CCSS math crosswalks *"incorrectly removed in
v1.9.0"* and told consumers to re-download; v1.13.1 restored a `jaccard` property *"unintentionally
removed in v1.12.0"*; v1.14.0 fixed four states' standards whose `inLanguage` claimed Spanish for
English text. 🟢 **Build against a pinned tag, diff the `CHANGELOG.md` before bumping, and treat a
spine bump as a release gate — not a dependency update.**

🔴 **And the trap that is documented but easy to miss:** v1.12.0 states that newly added standards
frameworks are **not yet aligned to learning components**, so *every* learning-component→standard
alignment still points at the superseded framework. **If your tutor resolves a standard to its
components, assert `isCurrent` on the framework and fail loudly rather than silently serving a
deprecated alignment.**

**2 — Install the skills, then fork them.** `npx skills add learning-commons-org/agent-skills`, or
the plugin route for the Anthropic companion:

```shell
git clone https://github.com/anthropics/k12-teacher-skills
claude plugin marketplace add ./k12-teacher-skills
claude plugin install k12-education@k12-teacher-skills
```

🟢 **Apache-2.0 on both, so forking is clean and patent-granted.** 🔵 **Fork rather than consume:
the four skills are written against the vendor's connector, and a client engagement almost always
needs a fifth skill and a different curriculum binding.** Keep the `NOTICE` attribution — Apache-2.0
requires it and the co-development credit is the part a client's counsel will check.

**3 — Make the evaluators the acceptance gate, not a report.** Install
`pip install learning-commons-evaluators` (or the npm package) and run the relevant family on every
generated artefact **before a teacher sees it**. 🟢 **The pairing that makes this defensible: the
skills ship their own `evals/` rubrics for pedagogy, rigor, formatting and model scaffolding, and
`evaluators` supplies the learning-science dimensions. Run both — the vendor's rubric for
"did the skill do its job" and the evaluator for "is this fit for a child of this grade."**

🔴 **The hard stop, and it is the whole reason this stage needs engineering.** The **expert-annotated
CLEAR and PERSUADE 2.0 corpora are CC BY-NC-SA 4.0.** You may ship the evaluators and their
prompts in a paid product; you may **not** ship those corpora, and you may not use them to validate
a commercial model release. 🟢 **So the billable, defensible work is re-annotating against the
client's own materials** — which also produces a better gate, because the thresholds end up
calibrated to the district's actual reading levels rather than to a research corpus.

**4 — Draw the Gated line before scoping, not during delivery.** Classify every content
requirement in the statement of work:

| requirement | tier | what it costs |
|---|---|---|
| Standards, crosswalks, learning components, misconceptions, progressions | 🟢 **Open** (CC BY 4.0 / CC0) | Attribution only — **to each original source, not to the distributor** |
| IM® v.360 **scope and sequence** | 🟢 **Open** | Attribution |
| IM® v.360 **instructional** or **assessment materials** | 🔴 **Gated** | **Publisher approval + separate agreement.** A line item and a lead time |
| **OpenSciEd** curriculum | 🔴 **Gated** | Same |
| **Learner Variability Navigator** (math / literacy models) | 🔴 **Gated** | Same |

🔴 **The clause to put in front of counsel, quoted from `LICENSE.md`:** compiling datasets into your
own build means you *"take on the licensing and attribution obligations of every dataset and
download you include,"* and the distributor's role *"doesn't consolidate those into a single license
for your build."* 🟢 **Never export the whole graph and label the result CC BY 4.0. Carry per-source
attribution, and keep an Open-only build target in CI so a Gated dataset cannot leak into a
deliverable by accident.**

**5 — Add the layers the vendor does not ship.** 🔴 **None of the three repositories touches
compliance, and in North America K-12 that is the bid-qualifying part.** Bring in, unchanged:
**P7** (grade-band gating, teacher-only mode, parent consent as state with an approval queue and a
decision log), **P9** (the COPPA disclosure boundary), **P3** (the policy-gated deployment layer).
🔵 **Add `autolab/Autolab`** (Apache-2.0, CMU) **where the engagement needs assessment *execution***
— so the agent advises and a deterministic grader adjudicates, which is the only arrangement that
survives a "did AI grade my child" question.

### What to sell, in order

1. **The Open/Gated classification of the client's content requirements** — a two-week audit that
   de-risks the whole programme and is sellable on its own.
2. **The pinned-spine release gate** — version pinning, `CHANGELOG` diffing, `isCurrent` assertion
   and a loud failure on deprecated alignments. 🟢 **Sold as correctness engineering, which it is.**
3. **Re-annotation of the evaluation corpus against client materials** — the lawful route to a
   commercial-grade acceptance gate.
4. **The fifth skill** — whatever workflow the client has that the four shipped skills do not.
5. **The compliance layer** (P7 + P9 + P3), which the vendor stack leaves entirely open.

### Portability

🟢 **The architecture ports everywhere. The data tier does not.** `agent-skills`, the Anthropic
companion and `evaluators` are jurisdiction-neutral — Apache-2.0 and MIT code, rebindable to any
spine. 🔴 **The Knowledge Graph data tier is US state standards and CCSS crosswalks: it does not
port to EMEA, APAC or LATAM.** Substitute the regional spine and keep the other two layers:

- **LATAM** → `bncc-dev` for Brazil (**P10 Variant A**), with
  `AI-for-Education/pedagogy-benchmark` as the model-selection gate. 🔴 **Re-annotate the
  evaluators for Spanish/Portuguese — the shipped rubrics are English and ELA-centric.**
- **EMEA** → 🔴 **no commercially usable national-curriculum graph exists in this KB for any
  European state.** Use `withmarbleapp/os-taxonomy` (ODbL + CC BY-SA, UK NC 2013 in full under OGL
  v3) via **P13**, and pair with OpenOLAT (Apache-2.0) for a **fully permissive** stack with no
  copyleft seam. Add `dodona-edu/dolos` (MIT, Ghent) for integrity per **P11**.
- **APAC** → `THU-MAIC/OpenMAIC` (MIT, 41.1k ★) for the multi-agent classroom shell, or
  `microsoft/Shiksha-Copilot` (MIT, MSR India + Sikshana) and `Orenda-Project/rumi-platform`
  (Apache-2.0, Taleemabad, Pakistan) where a named national deployment is the requirement.
  Add `open-edge-platform/education-ai-suite` (Apache-2.0, Intel/OpenVINO) for on-device per **P5**.

### 🔴 What was not verified, stated plainly

**The per-dataset licence labels and access tiers above are read from the repository's own
`README.md` and `LICENSE.md` at p327.** The authoritative download-level terms live on
`docs.learningcommons.org` and `platform.learningcommons.org`, and **the network policy answered
403 to CONNECT for both**, so **no dataset record count is asserted here and no download was
fetched.** 🔵 **Before this pattern enters a signed scope, pin the download-level terms from the
catalog pages — the Open/Gated split is the commercial hinge of the whole pattern and it deserves a
first-hand read.**

## P13 — The share-alike data boundary: shipping a proprietary product on an ODbL dataset — NEW in p326

**For:** every engagement in which the most valuable asset is **someone else's data under a
share-alike licence** — ODbL, CC BY-SA, ODC-BY — and the client intends to keep their product
proprietary. In this industry that is now the default case, not the exception: the sector's
largest open curriculum graph is **ODbL-1.0 + CC BY-SA 4.0**, and the usual reflex — *"share-alike,
so we can't use it"* — **is wrong and costs the client the best asset on the shelf.**

**The legal fact the whole pattern rests on.** ODbL binds a **derivative database**, not a
**produced work**. Modify the dataset → your modified dataset must be published under ODbL. Use
the dataset inside a product, a model or an application → **the product is yours.** CC BY-SA
covers the authored *text* in the same release on the same logic. **So the obligation is not
"open-source your tutor." It is "if you improve the graph, publish the improved graph."**

**Which turns a legal question into an architecture question — and it has a reference
implementation.** `tbh-23/Homestead` (**MIT**, 15 ★, 41 commits) ships this boundary:

**Wiring**
1. **Never vendor the dataset.** No copy in the repository, no copy in the container image, no
   copy in the deployment artefact. Homestead's README says so explicitly and its server enforces
   it. **A dataset committed into your tree is the single fact that makes the boundary arguable.**
2. **Fetch it at runtime from upstream, into a cache outside the repository**, pinned to a commit.
   Homestead caches under a private path and serves it to the browser from there.
3. **Verify on fetch.** Check the published SHA-256 per file; if the dataset ships no checksums,
   compute and store your own at pin time. A silent curriculum change is a correctness incident.
4. **Diff on refresh and surface the delta.** Homestead **notifies the user when topics are added
   or removed upstream** rather than absorbing the change invisibly. Do the same: an operator must
   see a curriculum move.
5. **Keep client-specific work in an overlay, keyed by the upstream ID — never as an edit to the
   graph.** Extra topics, re-banded ages, jurisdiction mappings, proprietary difficulty estimates
   all live in your own table joined on `topicId`. 🔵 **This is the commercial hinge of the whole
   pattern:** an overlay is a produced work and stays the client's; an in-place edit produces a
   derivative database and must be published.
6. **Carry the attribution, exactly as specified.** ODbL and CC BY-SA both require it and the
   upstream release gives the string to use. Put it in the product's about screen and in the data
   documentation — not only in a source file nobody renders.
7. **Audit the third-party layer separately.** A share-alike dataset can legitimately contain
   material the publisher could not relicense. In `os-taxonomy` four of seven curricula ship
   **codes only** and Common Core stays under its own purpose-limited licence. **Your product's
   rights posture is the union of the licences inside the dataset, not the licence on the
   dataset.**

**What to tell the client, in one sentence each.**
- **Private edtech:** *"We can build on it, you keep your product, and the only thing you owe back
  is changes to the public graph — which is why we are putting your changes in an overlay."*
- **Public sector or ministry:** *"Your jurisdiction extension becomes a public asset published
  under your name."* 🟢 **Lead with this; it is usually the thing they wanted anyway and could not
  justify paying for.**
- **Either:** *"The dataset ships checksums and we pin them. Your curriculum cannot change under
  your tutor without someone being told."*

**What this pattern does not do.** It does not clear **trademark** (NGSS is a WestEd mark with a
sample-approval requirement for commercial use), it does not clear **purpose-limited** upstream
licences (the CCSS Public License), and it does not make an **NC** dataset usable — `cn-math-
taxonomy` (CC BY-NC) and K12-KGraph's data (CC BY-NC-SA) stay out of client work no matter how
the code is arranged. **Share-alike is an architecture problem. NonCommercial is a wall.**

**Estimate:** 3–5 days of engineering inside any pattern that consumes external data, and it has
to be designed in at the start — **retrofitting a vendored dataset out of a shipped product is a
much worse week.**

---
## P12 — The measured-outcome public-school pilot: buy the evidence design, not the code — NEW in p325

**The problem this solves.** Every education bid ends at the same question — *does it actually
teach?* — and p323 established that the sector's usual answer (an LLM judge scoring helpfulness) is
the wrong instrument, while p319's own favourite example published judged scores about itself.
**This KB now holds exactly one artefact with a real classroom answer, and it cannot be used:**
`JustinoLM/STI-matematicas` (Universidad Tecnológica de Panamá) — **74 students, three sixth-grade
sections of a Panamanian public school, 710 practice sessions, pre→post 1.83 → 2.56 of 8,
Wilcoxon p = 0.0012, r = 0.41, SUS 70.1** — and **no licence file at all** (seven filenames probed
across five branch names), project finished, infrastructure decommissioned.

🟢 **So take its *design* and run it on components that are licensed.** This pattern is the
measurement protocol plus the permissive stack that can carry it. **It is the only pattern here
whose deliverable is a number rather than a system** — the system is a means to the number.

### What to wire, and why each piece

| role | component | licence | why this one |
|---|---|---|---|
| **pedagogy decision layer** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | Skill graph + **BKT** + **FSRS** + prerequisite rules behind MCP, SQLite local / PostgreSQL hosted. The mastery decision is **deterministic and inspectable** — the model never decides whether the learner has mastered anything |
| **hint ladder** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT | Read its hint sequencing, and mirror Panama's three rungs: *general strategy → step-by-step → a model-generated hint that points at the committed error without revealing the answer*. **The third rung is the only generative one** |
| **event capture** | [`openfun/ralph`](https://github.com/openfun/ralph) | MIT | xAPI **LRS** to the ADL standard, from a national public operator. **Install it before the tutor, not after** — a pre/post claim needs an event history that predates the intervention, or there is nothing to measure against |
| **teacher dashboard** | [`openfun/potsie`](https://github.com/openfun/potsie) | MIT | Grafana **dashboards-as-code** (Jsonnet/grafonnet) over the LRS. Reviewable in a pull request, on infrastructure a ministry already runs |
| **retention scheduling** | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | If you need FSRS outside `tutor-mcp`'s implementation |
| **enrolment / certificates** *(optional)* | [`openfun/joanie`](https://github.com/openfun/joanie) | MIT | Headless education ERP, when the pilot has to issue anything a learner keeps |
| **leakage check** | [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | MIT | Pre-registered audit of whether a helpfulness judge rewards handing over the answer. **Run it against your own prompt before the pilot**, not after |
| **pedagogical capability of the model** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🟡 CC BY / CC BY-SA (contradictory — see `agents/top.md`) | The one peer-reviewed benchmark that scores pedagogy **with a trained reward model against real teacher utterances rather than an LLM judge** |
| **calibration** *(optional)* | [`yjo2lee/knowsim`](https://github.com/yjo2lee/knowsim) | MIT | A learner simulator with a **known** knowledge state, for checking the tutor's confidence against what the learner actually knows |

🔴 **Not in the stack, deliberately:** `JustinoLM/STI-matematicas` itself (no grant),
`braivo/braivo` and `avps82/mentar` (**AGPL-3.0** — fine to run, fatal to link into client code),
and any artefact whose only quality evidence is a self-reported judged score.

### The privacy boundary — copy this verbatim, it is the first ministry question

Panama's design is the cheapest defensible answer this KB has read, and **four of its five controls
cost nothing**:

1. **No student data in the repository, ever** — the validation data was never published.
2. **Argon2** password hashing only.
3. **Server-verified admin token** for administrative functions; **teachers scoped to their own
   groups within their own school.**
4. 🟢 **Prompts leave with anonymous placeholders substituted server-side — never student names.**
   This is the control to put on the slide: it decouples *which model you call* from *what the model
   learns about a child*. Panama's system calls **DeepSeek** from a public primary school on that
   basis.
5. **Grade-band gating and teacher-only modes** where the jurisdiction requires them (**P7**, **P9**).

🔵 **Why this matters commercially: it converts the sovereignty objection into an engineering
line item.** A buyer who believes they must have a sovereign model has an expensive problem; a buyer
who needs *no identifiers to cross the boundary* has a middleware problem. Offer the sovereign path
too (`compose` **P4**, **P21** — GWDG / AcademicCloud in the EU), but price the placeholder boundary
first.

### The measurement protocol — the actual deliverable

**Stage 1 — instrument and baseline (2–3 weeks, before any AI is deployed).**
Build an **8-item pre-test** per target skill, administered on paper or in the LMS, and stand up
`ralph` so that baseline behaviour is already being recorded. Register the analysis **before data
collection**: the primary outcome, the test, the effect-size measure and the exclusion rule. The two
pre-registered audits in this KB (`conv-vs-ped-tutor`, `ability-levels-audit`) are the template, and
p323's finding is why it matters — **difference-in-differences on a bounded rating scale can
manufacture an effect from nothing.**

**Stage 2 — the pilot (6–10 weeks).** Panama's scale is the realistic floor and it was enough for
significance: **three class sections, ~74 learners, ~700 sessions.** Keep per-session events in the
LRS, not in application logs.

**Stage 3 — analysis, exactly this.**
- Pre→post on the 8-item instrument, **paired**, reported as a mean change with n stated.
- **Wilcoxon signed-rank** (not a t-test — these are bounded small-integer scores), with the
  **effect size r** alongside the p-value. Panama: *p = 0.0012, r = 0.41 (medium)*.
- **SUS** for perceived usability, n stated separately (learners who finished the survey ≠ learners
  who practised). Panama: *70.1 / 100*.
- Engagement as a **denominator-honest** figure: *65 of 74 completed at least one practice*, not
  "74 students used it".

**Stage 4 — the disclosure that makes the rest credible.** 🟢 **State the limit in the deliverable,
in one sentence, before anyone asks:** *without a control group the improvement cannot be attributed
to the system alone.* **Panama's README says exactly that, and it is why its numbers are worth
quoting at all.** Then offer the fix as the next phase: **a waitlist or stepped-wedge control** —
sections receive the system in sequence, so every class gets it and attribution becomes possible.
**That is the second engagement, and it is an easier sell after an honest first one.**

### What to sell, in order

1. **Stage 1 alone is billable** — instrument design, pre-registration and an LRS that works is a
   complete piece of work, and the client owns it whatever the pilot shows.
2. **The pilot.** Deterministic mastery, three-rung hints, placeholder boundary, dashboards-as-code.
3. **The attributable study.** Stepped-wedge, the number a ministry can act on.

🔴 **The risk to name in the proposal, because it is real: the pilot may show nothing.** A medium
effect from one school is the *good* case here. **Price Stages 1 and 2 so that a null result is
still a delivered engagement** — an instrumented school, a reviewable dashboard, a pre-registered
protocol and a permissive stack are assets regardless — and **never contract on an uplift target.**
Every vendor in this sector promises one; p323's evidence is that most of those promises are
measured with the wrong instrument.

### Portability

**LATAM first** — the Panama precedent, Spanish-language, public-school, and `repos/foundations.md`
now carries a pt-BR enablement track (`LucasSpinola/assistentes-educacionais-com-ia`) for the
knowledge-transfer line item. **EMEA next**, where the same stack is the public operator's own
software (**P21**, **P22**) and the EU AI Act's high-risk duties for assessment make a
pre-registered evidence file an asset rather than an overhead. **APAC as a build**, where
`muhammedalakbarli/imparo`'s 154-skill graph and `wwlwgo/cn-primary-math-knowledge-graph` show what
expressing a national curriculum costs.

## P11 — The academic-integrity evidence chain: sell the audit trail, never the verdict — NEW in p324

**Why this pattern exists now.** For seven passes this KB told studio leads there was no credible
open source in this category and to sell process evidence instead. **The first half of that was a
query artefact** (`intel/trends.md` trend 9, retracted in p324) — the components exist, three of
them measured first-hand this pass, and two are permissive. **The second half was right**, and it
is the design constraint of this pattern: every component here produces **evidence for a human
reviewer**, and nothing in it emits an authorship verdict.

**The stack, named repo by repo, with the licence posture each one forces.**

| # | stage | repo | licence | how it wires in |
|---|---|---|---|---|
| 1 | **Process evidence** (the foundation, already in this KB) | `jupyter/nbgrader`, `ucbds-infra/otter-grader`, `jupyterhub/jupyterhub` | BSD-3-Clause / BSD-3-Clause / BSD-3-Clause | **Deploy first and unchanged.** Submission history, execution provenance and per-cell autograding are the only artefacts in the chain that evidence *how* the work was produced. If a client will fund one stage, fund this one |
| 2 | **Prose, citation and stylometric signals** | `sunilgentyala/aegis-integrity` | **MIT** | `pip install "aegis-integrity[ml]"`, then run it **as an MCP server** — seven tools, of which `aegis_check_citations` and `aegis_analyze_paper` are the two to expose first. Pass `offline=true` by default; enable Crossref only with the client's written sign-off, and note in the DPIA that **reference metadata leaves the machine and the document never does** |
| 3 | **Text similarity against the institution's own corpus** | `NoplagLabs/noplag-engine` | **Apache-2.0** | `docker compose up` with PostgreSQL; load the institution's prior submissions through `POST /v1/corpus/documents`; call `POST /v1/checks` and read character-range matches from `/v1/checks/{id}/report`. 🔴 **Put an auth proxy in front of it on day one** — *"the API ships with no authentication"* |
| 4 | **Code similarity and collusion** (any CS, data or bootcamp engagement) | `jplag/JPlag` | 🟡 **GPL-3.0** | **Service boundary, never linked.** Run it as its own container exposing one HTTP endpoint; call it from the orchestrator. Twenty-odd languages, Java API or CLI, and its report viewer is local — *"No data will leave your computer!"* Substitute `thu-cs-lab/jieplag` (**MIT**, Rust) when the client's constraint is GPL avoidance rather than language coverage |
| 5 | **Orchestration and the review UI** | your code, plus the review-UI shape from `openeduhub/metadata-agent-canvas` | — | The canvas pattern this KB recorded in p322 is **exactly** the right interaction here: each signal shown with a **confidence badge**, inline annotation by the reviewer, and an **explicit confirm step** before anything is recorded. Reuse the interaction design; the repository's own grant is unverified, so do not depend on its code |
| 6 | **Calibration test before go-live** | `yjo2lee/knowsim` (MIT) for assistant-side calibration; the two pre-registered audits (`bydeng01/*`, MIT) for the measurement discipline | MIT | Run the "prove it teaches" discipline from p323 against *this* product too: pre-register what a positive finding means, freeze the evaluation set, log decisions |

**The wiring, in one sentence:** stage 1 runs continuously in the LMS; stages 2–4 run per
submission behind one orchestrator that **fans out and merges signals into a single reviewer
packet**; stage 5 is the only place a human decision is recorded; stage 6 gates the launch.

🔴 **The four rules that keep this sellable.**

1. **No verdict, ever.** Mirror `aegis-integrity`'s own language in the product copy: *"Results
   are a supporting signal for human review, not a determination of misconduct."* A client asking
   for an AI-authorship score is asking for the one thing the literature does not support.
2. **Do not ship the AI-text score as a finding.** Use it, if at all, as an internal triage
   ordering that the reviewer never sees as a number. `aegis-integrity`'s own README warns
   *"Do not treat AEGIS as having solved ESL false positives"*, and its changelog records an ESL
   multiplier that was **inverted** in an earlier release. **In any engagement with a
   second-language cohort — most of LATAM and much of EMEA and APAC — this stage is the fairness
   exposure, and the mitigation is not shipping its output.**
3. **Two licence boundaries, both structural.** JPlag is GPL-3.0 → separate process, HTTP only.
   `noplag-engine` is the **open core of a hosted product** → pin the version, read the diff on
   upgrade, and expect the roadmap to favour the hosted side.
4. **State the corpus limit in the proposal.** Both similarity engines match **only against what
   you load**. *"Plagiarism detection is corpus-based, not a live web/database crawl"* — a client
   expecting web-wide coverage is expecting the commercial product, and that expectation has to
   die in the sales conversation rather than in the pilot.

**Effort, measured against what is being assembled rather than guessed:** stages 1 and 3 are
deployment and data loading; stage 4 is a container and one endpoint; stage 2 is configuration plus
the DPIA conversation; stage 5 is the only real build. **The honest shape is 6–8 weeks for stages
1–4 plus a reviewer UI, and the long pole is the client's data-protection sign-off on stage 2, not
the code.**

**Where it sells, by region:** see `intel/market.md` under *Opportunities by region* — North
America on the human-oversight statutes, EMEA on the AI Act's high-risk assessment duties, APAC on
Vietnam's *"sole basis … without meaningful human review"* carve-out, LATAM on the 87%-use /
26%-strategy gap and the research-integrity remit of its university sector.

## P21 — The EU public-sector OER tutor: integrate the copyleft platform, own the permissive edges

**When to propose it.** A European public-sector or publicly funded education buyer — ministry,
federal state, national OER portal, university consortium — that already runs a content repository
and wants an AI tutor over it, under AI Act scrutiny and, increasingly, with a stated preference
for inference that stays in national or academic infrastructure.

**Why this recipe and not a fork.** Everything in the reference stack was read first-hand at p321,
and the licences do not permit the obvious move. The two layers with real engineering are
**`edu-sharing` (GPL-3.0, 16,110 commits)** and **`oeh-search-etl` (no licence file, 1,397
commits)**. The three permissive artefacts are a **dataset** and two **prototypes**. So the
architecture is forced, and that is a feature: it keeps Globant's deliverable on the permissive side
of the line.

**The wiring, named repo by named repo.**

1. **Leave the repository platform alone and talk to it over HTTP.**
   `edu-sharing/edu-sharing-community-repository` (**GPL-3.0**) stays a deployed service — either the
   client's existing instance or a stock install. **Do not link its code.** `openeduhub/tutor-chatbot`
   demonstrates the integration surface: the edu-sharing / WLO REST API, in its case
   `https://www.wirlernenonline.de/api/v1`. This is the same posture this KB takes on Moodle and
   OpenOLAT, so the copyleft question never reaches the deliverable.

2. **Take the competency model as data, from `openeduhub/oeh-metadata-vocabs` (CC0-1.0, 938
   commits).** SKOS/Turtle at `w3id.org/openeduhub/vocabs`: educational context, level, discipline,
   school type, rights and cost, machine-readable quality criteria, and **DigCompEdu, ESCO skills
   and EQF/DQR**. CC0 means no attribution condition — load it and move on. **This replaces the
   bespoke skill-taxonomy work that otherwise opens every one of these engagements**, and because
   the vocabularies are the ones the platform already annotates against, your tutor's skill graph
   and the client's content metadata share a vocabulary by construction rather than by mapping.

3. **Put the deterministic pedagogy in `tutor-mcp` (MIT), not in the prompt.** Skill graph, BKT,
   FSRS, prerequisite rules and narrative memory behind MCP, keyed to the vocabulary URIs from
   step 2. The vocabulary supplies the node identities; `tutor-mcp` supplies the mastery state and
   the decision about what to teach next. `agents/top.md` carries the row.

4. **Ground answers in the client's own content, not the open web.** `HKUDS/LightRAG` (MIT) over the
   material the platform returns for the learner's current objective. `tutor-chatbot`'s pattern is
   worth copying exactly here: **extract the learning metadata from the learner's question first,
   query the repository API with it, then attach the retrieved materials to the answer as direct
   links filtered by subject, content type and source** — so every claim carries a provenance link
   back into the client's repository. That is what makes the output defensible to an inspector.

5. **Make the inference provider pluggable from day one.** `tutor-chatbot` offers **OpenAI or GWDG**;
   `ki-prompt-benchmark` adds **AcademicCloud**. Build the same seam. For a publicly funded EU buyer
   this is no longer a nice-to-have — see the p321 trend in `intel/trends.md`.

6. **Ship the evaluation harness as part of the deliverable, modelled on
   `openeduhub/ki-prompt-benchmark` (Apache-2.0).** Judge-scored comparison of the current prompt
   against a candidate on **five criteria, 1–10, with a named winner and a written rationale**, plus
   generation time and token cost per provider, feedback accumulated across runs into a regenerated
   prompt per field. **It is three commits — take the design and build it properly.** Pair it with
   `AITutor-EvalKit` (MIT) if the buyer wants a teaching-quality measure rather than a
   metadata-quality one.

7. **Add `pylti1.3` (MIT) only if the tutor must appear inside an LMS**, and keep the AI Act posture
   from `intel/market.md`: Article 50 transparency has applied since `2026-08-02`, so the tutor
   discloses that it is an AI in the learner-facing surface, and anything touching admissions,
   assessment or learning-path steering is Annex III high-risk from `2027-12-02`.

**What the client ends up owning.** A permissively licensed tutor, a permissively licensed
evaluation harness, a CC0 competency model, and an HTTP integration against a GPL-3.0 platform they
already run. **Nothing in the deliverable is copyleft and nothing depends on an unlicensed
repository** — which is the whole reason the recipe is shaped this way.

**The honest caveat.** Steps 1, 2 and 7 rest on artefacts with 16,110, 938 and 178 commits. Steps 5
and 6 rest on prototypes of 10 and 3 commits, and step 6's reference exports to a schema
(`mds.xml` v10.0) that is specific to edu-sharing. **Budget real engineering for the pluggable
provider and the evaluation harness** — this recipe tells you the shape and the licence position,
not that the code exists.

## P22 — The OER catalogue enrichment pipeline: the first AI product a public education buyer will actually sign — NEW in p322

**When to propose it.** Any buyer that owns a large, badly catalogued body of learning content —
national or regional OER portal, ministry repository, university consortium, publisher backlist,
corporate academy after three acquisitions — and has been told to "do something with AI". It is the
pattern to lead with **instead of** a tutor (P1, P21) when the content layer is not yet trustworthy,
and p322's trend reading is the argument: Germany's public OER operator archived its chatbot in 2023
and spent the following three years building exactly this pipeline.

**Why it closes.** Every step is measurable against a before/after count, none of it touches a
child, none of it makes a pedagogical claim that has to be defended, and the output is the
prerequisite for every later AI phase. Under the EU AI Act this workload sits far away from the
Annex III education triggers that make P4 expensive — **it processes content, not learners.**

**The reference implementation exists, service by service, and was read first-hand at p322.** It is
`openeduhub` / WirLernenOnline. Use it as the architecture and **not** as the dependency set,
because the licences divide by layer:

| Step | Reference service (read p322) | Licence | Take it or rebuild it |
|---|---|---|---|
| 1. Harvest | `openeduhub/oeh-search-etl` (1,397 commits, Scrapy→Postgres→Elasticsearch) | 🔴 none | **Rebuild.** Use Scrapy directly; copy the spider layout only |
| 2. Clean text from a URL | `openeduhub/text-extraction` (77 commits) | 🔴 none | **Rebuild** on `trafilatura` + `markitdown` with a Playwright fallback — and copy its per-domain multibucket rate limiting, which is the part homegrown harvesters omit and publishers block over |
| 3. Deduplicate | `openeduhub/duplicate-detection` (25 commits, **MinHash over shingles**, URL + title normalisation) | **Apache-2.0** (`LICENSE` read first-hand; its README wrongly says MIT) | **Take it.** Hash-based, not embeddings: a MinHash threshold is defensible to a client, a cosine distance is not |
| 4. Extract metadata with an LLM | `openeduhub/metadata-agent-api` (24 commits, 11 schemas, **per-field origin tags**, `/generate` `/extract-field` `/validate` `/upload`) | 🔴 README says MIT, **no licence file** | **Rebuild to its endpoint shape.** Copy the schema set and the origin-tag idea; the origin tags are the provenance feature a public buyer now asks for by name |
| 5. Human review before anything is written | `openeduhub/metadata-agent-canvas` (60 commits, Angular 19 + LangChain, **confidence badge → inline edit → explicit confirm**) | 🔴 README claims Apache-2.0, **no licence file** | **Rebuild the interaction, which is the valuable part.** This is what a human-oversight requirement looks like as a UI instead of a policy sentence |
| 6. Capture from the teacher's browser | `openeduhub/metadata-browser-plugin-fuerAPI` (11 commits, **Manifest V3**, guest upload, lesson-plan cart) | **Apache-2.0** | **Take it** as the starting point for the contribution surface |
| 7. Readability / reading level | `openeduhub/text-statistics` (94 commits, Flesch Reading Ease + **Wiener Sachtextformel**, 200 WPM baseline, **no ML**) | 🟡 GPL-3.0 | **Deploy as a service behind HTTP, never link.** Confirm the Wiener formula before applying it outside German |
| 8. Accessibility + licence screen | `openeduhub/metalookup` (623 commits, Playwright + **Lighthouse**, `POST /extract`) | 🟡 GPL-3.0 | **Deploy as a service.** This is the compliance screen public procurement asks for and it already exists |
| 9. Predict missing metadata without labels | `openeduhub/its-jointprobability` (200 commits, **Pyro ProdLDA**, predicts discipline, resource type, audience, educational context, topic) | 🔴 none | **Rebuild** — and this is the row that justifies the engagement when the client has no labelling budget |
| 10. Subject classification | `openeduhub/discipline-classification` (73 commits, Keras/TF, **ships pretrained `wirlernenonline.oeh.h5`**, top-3 with scores) | 🟡 GPL-3.0 | **Service boundary**, and check the training-data provenance before shipping the weights |
| 11. Bulk-run one prompt over the catalogue | `openeduhub/z-api-runner` (37 commits, Swagger, model unstated) | 🔴 none | **Rebuild.** Trivial to write, universally needed, never budgeted |
| 12. Judge the output | `openeduhub/llm-judge` (1 commit, 6 criteria in `config.yaml`, gpt-4o-mini) + `openeduhub/ki-prompt-benchmark` (Apache-2.0, LLM-as-judge prompt bench, p321) | **Apache-2.0** | **Take the configuration shape, not the scores** — `llm-judge` publishes neither scale nor prompts nor aggregation, and it judges **factual accuracy, not pedagogy** |
| Everything above, to the platform | `openeduhub/edu-sharing-python-client` (519 commits, **389 operations generated from `openapi.json`**, verified against **edu-sharing 11.0**) | **Apache-2.0** | **Take it, and start here.** A permissive generated client is how you touch a GPL-3.0 edu-sharing instance with no linking question |
| Vocabularies for every field above | `openeduhub/oeh-metadata-vocabs` (938 commits, SKOS/Turtle, DigCompEdu/ESCO/EQF-DQR) | **CC0-1.0** | **Take it.** No attribution condition at all |

**The correction overlay, which is the non-obvious step.** `openeduhub/wlo-quellenliste`
(Apache-2.0, 6 commits) does the thing every one of these projects eventually needs and nobody
designs for: it merges the harvest with an **editorial correction CSV at serve time** rather than
mutating the harvested records. Build this in from day one — the harvest will be wrong, the
editorial team will be right, and overwriting the source destroys the ability to re-harvest.

**Inference placement, for an EMEA public buyer.** `metadata-agent-api` and `metadata-agent-canvas`
both ship a **B-API→AcademicCloud (`deepseek-r1`)** provider alongside OpenAI. A buyer that must
keep inference in national or academic compute therefore has a working reference for *this*
workload, not just for a tutor demo — quote it in the pitch, and see `intel/trends.md`.

**Sequencing and estimate.** Steps 1–3 and the client (the trustworthy-catalogue milestone) is where
the measurable win is: **6–8 weeks**. Steps 4–6 with human review in the loop: **a further 6–8
weeks**, and this is the phase that needs the client's editorial team committed, not just their IT.
Steps 7–12 are individually small and should be sold as a menu, not a block. **Timings are
engagement estimates, not measurements.**

**The three risks to put in the proposal yourself.**
1. **Six of the twelve reference services carry no licence** — 1,852 commits of it. The estimate
   above assumes rebuilding steps 1, 2, 4, 9 and 11, so do not let a reviewer price it as reuse.
2. **The GPL-3.0 analysers (7, 8, 10) must stay behind a process boundary.** Containerise and call
   over HTTP; if a client's security policy forbids that topology, those three steps become
   rebuilds too.
3. **Four of the reference repositories state a licence the repository does not carry.** Verify
   from the `LICENSE` file, not the README, on every one of them and on anything else you add — the
   full instance list is in `repos/foundations.md`.

## P1 — Curriculum-grounded lifelong tutor

**For:** any institution that wants a tutor answering from *its* material, with a learner model that
survives across sessions. The default education engagement.

**Stack**
- `HKUDS/DeepTutor` (Apache-2.0, 41.8k ★, **v1.6.15 released 2026-10-19**) — tutoring agent and lifelong learner state
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — the auditable agent loop for custom tools
- `dmitry-viskov/pylti1.3` (MIT, 138 ★) — LTI 1.3 tool so the tutor launches from the client's LMS
- Client LMS — `moodle/moodle` (GPL-3.0), `openedx/openedx-platform` (AGPL-3.0) or
  `instructure/canvas-lms` (AGPL-3.0), **unmodified**

**Wiring**
1. Ingest course material (syllabi, slides, past assignments) into LightRAG; one index per course,
   one namespace per institution. **Where a verified curriculum standard exists for the
   jurisdiction, ground against it rather than against the slides alone — see P10.** For Brazilian
   basic education that is `bncc-dev`; the measured difference is 31.9% → 2.3% curriculum
   hallucination.
1b. **Filter retrieved documents by student identity, institution and authorised category *before*
   prompt construction, and emit a disclosure record per retrieval.** New this pass. Copy the shape
   from `ashutoshrana/haystack-ferpa-filter` (Apache-2.0, 41 commits) — **read it, do not import it
   at 0 stars** — which returns filtered documents plus a `disclosure_record` for the caller to
   persist. This is cheap to build at design time, effectively impossible to retrofit after a
   FERPA/GDPR review, and it is the artefact that answers "prove this student could lawfully see
   that document". It also feeds P3's audit log for free.
2. Run DeepTutor as a service; pin the version — it released v1.6.15 on 2026-10-19 and moves weekly.
3. Expose the service as an LTI 1.3 Advantage tool via `pylti1.3`. The LMS launches it; the LMS is
   never patched. **This is what keeps Globant's code off the GPL/AGPL side of the line.**
4. Return grades/progress through LTI AGS so the gradebook stays authoritative.
   **Worked reference, new in pass 320.** This step has been asserted in every pattern in this file
   without a readable example of the passback itself. There is one now:
   **`adamzammit/LTIPlugin`** (**GPL-3.0**, 14 ★, 97 commits) makes LimeSurvey an LTI provider and
   **returns a 0.0–1.0 score to the gradebook, with README setup against Canvas, Moodle, openEdX
   and Blackboard.** **Read it; do not link it.** Three constraints: it is **not AI**, the page
   **never states an LTI version** and the bundled `LTI-Tool-Provider-Library-PHP` points at the
   **legacy 1.x Basic Outcomes path rather than 1.3 Advantage AGS** (verify the submodule before
   citing it as Advantage), and **GPL-3.0 is copyleft** — run it behind a process boundary, keep it
   out of the deliverable. **Use it to shorten the "how does the score actually land in four
   different gradebooks" question from four specifications to one repository.** For the permissive
   Advantage implementation you will actually ship against, `dmitry-viskov/pylti1.3` remains the
   dependency, with `tsugiproject/tsugi` as the heavier alternative.
5. Persist learner state in Globant-owned storage, keyed by the LTI `sub` claim — never by email.
6. **Prove it teaches, and do not use an LLM judge to do it. New this pass.** Before the pilot
   closes, run an evaluation the client's academics can defend:
   - Score tutoring behaviour with **`eth-lre/mathtutorbench`**'s task shapes — problem solving,
     socratic questioning, solution correctness, mistake location, mistake correction, scaffolding —
     which grade against **ground-truth teacher utterances via a reward model**, not a judge's
     opinion (licence caveat: CC BY badge vs CC BY-SA footer; resolve before extending it).
   - Borrow the discipline from **`bydeng01/conv-vs-ped-tutor`** and
     **`bydeng01/ability-levels-audit`** (both MIT): **pre-register the comparison, freeze and hash
     the data, keep a decisions log, separate registered analysis from post-hoc.**
   - **Measure answer leakage explicitly** — whether the tutor's "helpfulness" came at the cost of
     the student's later independent work. That is the failure mode an LLM helpfulness judge
     rewards.
   - **Never present a difference-in-differences on a bounded satisfaction scale as evidence of
     learning.** The audit above shows that design can manufacture an effect from nothing, and a
     client's statistician will eventually notice.
   **Cost:** 2–3 weeks inside the pilot. **Value:** it is the one claim in this market that
   competitors cannot make, in a sector where every deck asserts an uplift.

**Licence note:** every component Globant writes or links sits on the far side of the LTI boundary,
so the GPL-3.0/AGPL-3.0 platform never reaches it. Say this explicitly in the SOW.

**Competitive note, new this pass:** on Canvas, **Instructure's Project Athena (announced
2026-07-22) does this natively.** Do not sell P1 alone into a Canvas account. Sell P1 + P2 (the
pedagogy Athena does not do) or P1 + P3 (the audit trail the district must buy anyway).

**Estimate:** 8–10 weeks to a pilot with one faculty.

---

## P2 — Mastery-and-retention engine (the "actually pedagogical" tutor)

**For:** clients who will be asked by an accreditor or a ministry *why* the tutor showed what it
showed. P1 answers content; this one answers pedagogy. **This is the pattern that survives contact
with Canvas's native AI.**

**Stack**
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★, 467 commits) — **the engine.** Skill graph, Bayesian
  Knowledge Tracing, FSRS scheduling, prerequisite gating, cross-session narrative memory, as an
  MCP server. SQLite over stdio locally; PostgreSQL over HTTPS + OAuth in the institutional profile
- `CAHLR/OATutor` (MIT, 268 ★) — reference BKT implementation and hint sequencing; use to validate
  tutor-mcp's mastery estimates against a published academic implementation
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — standalone FSRS where you need
  scheduling outside the MCP server (offline clients, batch jobs)
- `satvik314/educhain` (MIT, 387 ★) — generate the item bank the engine consumes
- `HKUDS/DeepTutor` (Apache-2.0) — conversational surface
- `GeminiLight/gen-mentor` (CC0-1.0, 135 ★, WWW '25 oral) — **read, don't depend.** The
  peer-reviewed multi-agent ITS architecture to cite when a ministry asks for provenance
- `xiaoyang111222/cn-math-taxonomy` (**CC BY-NC 4.0**, 780 ★) — **new this pass; read, never
  ship.** The shape of the artefact step 1 asks the client's SMEs to produce, already built for
  Chinese K-9 mathematics: **531 knowledge points, 909 prerequisite edges distinguished as 788
  hard and 121 soft**, 2,271 items and 230 curriculum-standard entries, with a diagnostic engine
  and validation scripts. **NonCommercial rules it out of a deliverable, and its author states it
  is an AI-generated draft not reviewed by teachers** — so take two things from it: the
  **hard/soft prerequisite distinction** (a soft edge degrades the recommendation, a hard edge
  blocks progression) and the warning that a generated skill graph is a draft until a teacher signs
  each edge
- `brownplt/LTLTutor` (**GPL-3.0**, 12 ★, 320 commits, CAV 2025 Distinguished Paper) — **read,
  don't link.** Misconception-driven adaptation: it models the specific wrong beliefs learners hold
  and targets practice at them, which is a sharper decision rule than mastery probability alone

**Wiring**
1. Stand up tutor-mcp in the institutional profile (PostgreSQL, HTTPS, OAuth). Define the subject's
   skill graph — concepts and prerequisites — with the client's SMEs. **This is the engagement's
   real intellectual work and it is not LLM work.**
2. Educhain generates candidate items from the curriculum; a human SME approves into the bank.
   The approval step is not optional — Educhain is 387 ★ and slow-moving; treat output as a draft.
3. Let the engine decide: BKT tracks per-skill mastery, prerequisite rules gate progression, FSRS
   schedules review. **The LLM explains; the engine decides what comes next.** That separation is
   the entire defensibility argument and tutor-mcp enforces it architecturally.
4. Put DeepTutor (or any MCP-capable client) on the front as the conversational surface.
5. Validate against OATutor on a sample cohort before go-live — two independent BKT implementations
   agreeing is an evidence artefact an accreditor will accept.
6. **Have a teacher sign every prerequisite edge, and record who signed it. New this pass.** The
   skill graph is the engine's entire authority; a generated graph is a hypothesis. Borrow the
   hard/soft edge distinction from `cn-math-taxonomy` and treat an unsigned edge as soft.
7. **Run P1's stage 6 evaluation here too, and it matters more in this pattern than in P1** —
   because a mastery engine makes progression decisions. Pre-register the comparison, freeze the
   data, measure answer leakage, and **do not report an LLM-judged helpfulness score to an
   accreditor** (`agents/top.md`).

**The integration caveat that decides scope:** tutor-mcp's README names **no LTI, SCORM or xAPI
support.** It is MCP-only. For an institutional deployment you write the LTI 1.3 wrapper yourself
with `pylti1.3` and bridge it to the MCP server. Budget that bridge explicitly — it is the single
most-repeated unbudgeted item in this sector (see trend 6 in `intel/trends.md`).

**Estimate:** 6–8 weeks on top of P1; 10–12 weeks standalone. Add 2–3 weeks for the LTI bridge.

---

## P3 — Policy-gated deployment layer (North America, dated demand)

**For:** US districts and systems facing Ohio's 2026-07-01 framework requirement, Idaho SB 1227,
Oklahoma/Maryland human-oversight rules, or any of the 134 bills across 31 states in 2026.
**Sell this before selling a tutor.**

**Stack**
- Any tutor from P1/P2 as the governed subject
- `jupyterhub/jupyterhub` (BSD-3-Clause, 8.4k ★) — provenance-capturing compute for student work
- `jupyter/nbgrader` (BSD-3-Clause, 1.4k ★) + `ucbds-infra/otter-grader` (BSD-3-Clause, 161 ★) —
  autograding with a recorded execution trail
- `dmitry-viskov/pylti1.3` (MIT) — identity and grade passback from the LMS of record
- P7's gating layer (below) — grade-band enforcement is now part of the same deliverable

**Wiring**
1. Put every agent call behind a gateway that logs: prompt, retrieved sources, response, learner id,
   timestamp, model version. This log *is* the deliverable — it satisfies "educator supervision" and
   "no high-stakes automated decisions" in one artefact.
2. Hard-gate high-stakes actions (final grades, placement, discipline) behind human approval.
   Idaho's "AI cannot replace human teachers", and Oklahoma's and Maryland's reported bars on
   high-stakes AI decisions, are code-level constraints, not policy sentences.
3. Run assessment in JupyterHub; grade with nbgrader/otter-grader so the submission's execution
   history is evidence. This is the **process-evidence** answer to integrity — there is no credible
   open source AI-detector to buy instead, and there should not be (trend 9).
4. Generate the parent-disclosure and retention report from the same log. FERPA/COPPA retention
   windows are configuration, not a rewrite.

**Estimate:** 4–6 weeks; deployable before the tutor it governs.

---

## P4 — EU AI Act provider package (EMEA)

**For:** EMEA engagements where Globant builds the tool and therefore becomes the **provider** under
the AI Act, while the school is only the deployer. Annex III lists education as high-risk —
admissions, learning-outcome evaluation, student level placement, exam/behaviour monitoring.

**Stack**
- P1 tutor, plus:
- `openfun/richie` (MIT, 316 ★) — MIT portal/catalogue in front of an AGPL Open edX back end
- `overhangio/tutor` (AGPL-3.0, 1.1k ★) — reproducible Open edX deployment, in-region
- `learningequality/kolibri` (MIT, 1.2k ★) — where on-device/offline delivery is required
- Self-hosted models for data residency

**Wiring**
1. **Ship Article 50 transparency now.** It applied from 2026-08-02 and was *not* deferred: AI
   interaction disclosure in the UI and machine-readable marking of generated content. The smallest
   immediate billable item in EMEA. **The watermarking grace period for AI-generated content runs to
   2026-12-02** — six weeks from this pass — so machine-readable marking is a dated deliverable, not
   a backlog item.
2. **Check the 2026-12-02 prohibitions before that date** — new bans (non-consensual intimate
   imagery, CSAM) take effect six weeks from this pass. For an education product this is a
   content-safety and image-generation audit, and it is not deferred.
3. **Article 4 is now an obligation to take AI-literacy measures for staff** (relaxed, not removed).
   A documented staff-training programme discharges it, and the client needs one anyway (trend 1).
4. Build the high-risk conformity file *during* development: technical documentation, risk
   management, data governance, logging, human oversight, post-market monitoring. The deadline moved
   to **2027-12-02** under Regulation (EU) 2026/1744 — against 12–18 month public procurement
   cycles, conformity-ready is what wins 2026–27 bids. The deferral moved the date, not the
   substance.
5. **No emotion recognition anywhere in the stack.** Banned in schools since Feb 2025 — no
   engagement-detection from webcam, no affect scoring. Check this in code review.
6. Keep Open edX or Canvas unmodified behind Richie; AGPL's network clause reaches modified
   platforms, and not modifying it is the cheapest compliance decision available.

**Reuse note — the conformity file is the most portable artefact in this KB.** It travels to:
- **Brazil.** PL 2338/2023 is risk-based and passed the Senate in December 2024.
- **South Korea, and this one is already in force.** The **Framework Act on AI (Law No. 20676) has
  applied since 2026-01-22**, its **high-impact AI** category explicitly covers **student evaluation
  in early childhood, elementary and secondary education**, and high-impact operators owe
  **user-protection measures and records of safety and trust measures (Art. 34(1))** — the same
  documentation set as the Annex III file. The **fundamental-rights impact assessment is voluntary
  (Art. 35)**, so lead with it as a differentiator rather than a cost. **A foreign vendor without a
  Korean presence must appoint a domestic agent** — a commercial arrangement to settle before
  bidding, not an engineering task. Grace period on fines is reported as one year from entry into
  force. Read the Enforcement Decree and MSIT guidance before quoting thresholds.
- **Uruguay**, as the LATAM pilot: first in Latin America to sign the Council of Europe AI Framework
  Convention, so European-shaped evidence is the evidence it already expects.

**Estimate:** 10–12 weeks including the conformity file. Porting it to a second jurisdiction:
2–3 weeks, almost entirely mapping and review rather than build.

---

## P5 — Offline-first national curriculum delivery (APAC, Africa, and the India mandate)

**For:** India's compulsory AI + Computational Thinking rollout for Classes 3–8 from 2026-27 across
32,900 CBSE schools — 50 h/yr for Classes III–V, 100 h/yr for VI–VIII — where **64.7% of schools
have computers and 63.5% have internet.** A cloud tutor does not serve this brief. **Also the right
pattern for Sub-Saharan Africa**, where the strongest evidence base for low-resource AI tutoring
exists (World Bank Edo State, Nigeria; EIDU in Kenya, ~400k children) and Kenya's DigiSchool has
put over 1 million tablets into primary schools.

**Stack**
- `learningequality/kolibri` (MIT, 1.2k ★) — offline-first delivery; MIT, so AI can embed directly
- `Sunbird-Ed/SunbirdEd-portal` (MIT, 41 ★) — India's national stack; the integration target
- `zijinz456/OpenTutor` (MIT, 145 ★) — **new this pass.** Local-first adaptive workspace, 10+ LLM
  providers, runs on-device; the tutor shell when nothing may leave the building
- `satvik314/educhain` (MIT, 387 ★) — bulk generation of curriculum-aligned items, SME-reviewed
- `open-spaced-repetition/fsrs-rs` (BSD-3-Clause, 447 ★) — scheduling that works with no network
- `microsoft/ai-agents-for-beginners` (MIT, 77.5k ★) — white-labelled teacher-training base
- `elimu-ai/webapp` (MIT, 41 ★, **8,075 commits**) — **new this pass.** Per-language content hosting
  that pushes to Android devices for out-of-school children, with production deployments in Hindi,
  Tagalog, Thai, Vietnamese and English; the same org publishes MIT ML components for reading-level
  prediction and storybook/video recommendation
- `ipti/br.tag` — **new this pass**, and read for one design decision rather than adopted: school
  management built for rural schools with **data sync for schools without internet**. Its licence is
  unresolved (README says BSD-3-Clause, sidebar links GPL-2.0), so **copy the sync model, not the
  code**

**Wiring**
1. Generate and SME-approve the item bank **centrally and online**; the only step needing
   connectivity at scale.
2. Package approved content into Kolibri channels; distribute by sync server, USB or sneakernet.
   Kolibri is MIT, so an embedded on-device scheduler or small local model is licence-clean.
3. Use OpenTutor as the on-device adaptive surface where a local LLM is available; fall back to
   pre-generated Kolibri content where it is not. **Design for both — device capability varies
   school to school in exactly these markets.**
4. Run FSRS scheduling fully on-device; sync learner state opportunistically, not continuously.
5. Integrate with Sunbird for national reporting — verify the wider `Sunbird-Ed` org's component
   repos before scoping; the portal is one piece of a larger stack.
6. Deliver teacher training from the `ai-agents-for-beginners` curriculum. **Training is the
   engagement, not an add-on** — and per trend 1, delivering training that *lands* is the hard part.
7. **Stage the adoption and say so in the bid. New this pass, and it is the lesson of the most
   expensive failure in this sector.** South Korea mandated AI digital textbooks nationally, met
   teacher and parent resistance, retreated to voluntary adoption, and on **2025-08-04** the
   National Assembly removed them from the legal definition of a textbook, taking the funding with
   them; usage had already fallen from ~37% of eligible classes in the first semester of 2025 to
   19% in the second, and schools from ~4,190 to 2,095. **Every education ministry in APAC watched
   that.** So: opt-in pilot schools, published outcome measures (P1 stage 6), teacher capability
   before coverage, and a documented exit path. **Price change management as the main line item,
   not the technology.**

**Estimate:** 12–14 weeks for a state-level pilot.

---

## P6 — The roster and SIS data spine (North America)

**For:** any US district or state engagement, under any of the patterns above. An agent that does
not know who the student is, what they are enrolled in and which teacher owns them is a demo.
Earlier passes of this KB called this bespoke integration work; **it is not, and that was a
search error — see `repos/foundations.md`.**

**Stack**
- `Ed-Fi-Alliance-OSS/Data-Management-Service` (Apache-2.0, 12 ★, 1,105 commits) — the Ed-Fi API
  platform, successor to the ODS/API platform
- `Ed-Fi-Alliance-OSS/edfi-oneroster` (Apache-2.0, 6 ★, 151 commits) — serves a **OneRoster 1.2**
  API from data in an Ed-Fi ODS
- `dmitry-viskov/pylti1.3` (MIT) — LTI identity at launch, reconciled against the roster
- Whichever tutor and governance layer from P1/P2/P3

**Wiring**
1. Stand up the Data-Management-Service against the district's Ed-Fi ODS. **Pin to a commit —
   neither repo publishes GitHub releases.**
2. Expose OneRoster 1.2 through `edfi-oneroster` as the single read interface your agents use for
   enrolment, section and teacher-of-record data. One contract, not one per SIS vendor.
3. At LTI launch, resolve the `sub` claim to the roster identity; everything downstream — learner
   state, mastery estimates, audit log entries — keys off that resolved id, never off an email.
4. Feed the teacher-of-record relationship into P3's human-approval gates. "Educator supervision"
   has to name an actual educator, and this is where that name comes from.
5. Keep the roster read-only from the agent side. Writes go back through the LMS gradebook over
   LTI AGS, not into the SIS.

**The standards argument to put in the proposal:** 1EdTech's 2026 position is that interoperability
is the precondition for AI, naming CASE, Edu-API and OneRoster as the standards that give an AI
system trustworthy institutional context. This pattern is that position implemented on Apache-2.0
code.

**Scope limit, stated plainly:** Ed-Fi is a North American standard in practice. It is not a route
into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions. Everywhere
else, SIS sync is still bespoke.

**Estimate:** 3–5 weeks alongside P1 or P3; longer if the district's ODS is not already populated,
which is a data-quality project and should be priced as one.

---

## P7 — Grade-band gating and teacher-only mode (North America K-12)

**Pass 320 upgrade — model parent consent as state, not as a flag.** Pass 319 scoped the parent
opt-out from **a single tracker** reporting Oklahoma's statute and flagged it as unverified.
**There are now two independent instances by two different mechanisms:** Oklahoma's reported
opt-**out**, and **South Carolina H.B. 5253**, reported to require **written parental opt-in
consent**. Opt-in and opt-out are **not the same data model** — opt-in defaults a pupil to
*excluded* and blocks the product until a positive record exists; opt-out defaults to *included*
and must honour a withdrawal at any time, including retroactively for data already processed.
**Build the stricter one and configure down:** store a per-pupil consent record with a mode
(`opt-in` / `opt-out`), a timestamp, the granting party and the jurisdiction, and make the tutor
check it on every launch rather than at enrolment. **A product that cannot express both modes is
unbiddable in at least two states**, and the duty to provide **alternative access to core
instruction** for a non-consenting pupil is a curriculum-delivery requirement, not a feature flag —
it is what makes `learningequality/kolibri` (MIT, offline) useful in this pattern rather than
decorative. *(Both statutes are snippet-sourced; `www.future-ed.org` and `www.multistate.us` are
unreachable from this session. Verify before a bid — and scope for it regardless, because the cost
of building it is small and the cost of retrofitting it is not.)*

**For:** districts that restrict rather than adopt. **New York City runs a one-year moratorium on
student-facing AI through eighth grade; Katy ISD (Texas) is banning generative AI chatbots for
K-6.** A product that cannot be switched off for a grade band cannot be bid into these districts —
and they are not outliers.

**Stack**
- P6's roster spine — grade level is a roster attribute, and it is the only trustworthy source
- P3's logging gateway — the gate is enforced and evidenced at the same chokepoint
- Any P1/P2 tutor as the gated subject

**Wiring**
1. Resolve grade level from the roster at launch (P6), not from a profile field a student can edit.
2. Enforce three modes at the gateway, per grade band, as policy configuration rather than code:
   **student-facing**, **teacher-facing only** (the teacher may use the agent *about* the student's
   work; the student never sees it), and **off**.
3. Default to the most restrictive mode for any learner whose grade level does not resolve. Fail
   closed.
4. Emit the mode into every audit-log entry. "Prove no eighth-grader interacted with the AI" then
   becomes a query, which is exactly the question a district under a moratorium will ask.
5. Expose the configuration to district administrators. The policy will change mid-contract; make
   that a settings change, not a release.
6. **Add a per-pupil opt-out that degrades gracefully. New this pass.** Four states enacted
   education-AI statutes in 2026 — **Idaho, Maryland, Oklahoma, Virginia** — and per one tracker
   Oklahoma's gives **parents an opt-out from student-facing AI tools together with a duty to
   provide alternative access to core instruction** *(single-tracker claim; verify against the
   statute, build for it regardless)*. The flag belongs on the roster record (P6), is enforced at
   the same gateway as the grade band, and **must leave the pupil with the instruction minus the AI
   path** — an opt-out that removes the lesson is a civil-rights problem, not a feature.
7. **Add an approval queue.** Oklahoma permits AI only under educator supervision with human review
   and **bars it from high-stakes student decisions**. So nothing AI-written reaches a student, a
   parent or a record until a named educator signs it, and the signature is logged with the draft
   it approved. `JaimeArriagadaRosas/Plugin-Feedback-Canvas` implements exactly this shape against
   Canvas over LTI 1.3 and **has no licence** (`agents/top.md`) — read it, rebuild it.
8. **Add a decision log that can answer "was any high-stakes determination AI-made?" with a
   query.** Placement, discipline, promotion, eligibility. The answer a district needs is "no, and
   here is the record", not a policy document.

**Why this is worth building once:** it is small, every K-12 district in a restricting state needs
it, and teacher-facing-only mode **keeps the engagement alive in a district that has banned
student-facing AI.** That is the difference between a lost account and a smaller one. **With the
opt-out, approval queue and decision log added, this pattern is no longer defensive — in Oklahoma,
Idaho, Maryland and Virginia it is the compliance surface the statute asks for**, and
`SirhanMacx/Claw-ED` (MIT, 778 commits) is a working reference for the teacher-facing-only product
shape.

**Estimate:** 2–3 weeks on top of P3 and P6 for gating; **+2 weeks for the opt-out, approval queue
and decision log.**

---

## P8 — The permissive-LMS build: no LTI boundary (greenfield, and EMEA sovereignty) — NEW

**For:** two specific situations, and no others. (1) A **greenfield** build — a corporate academy,
a bootcamp, a new programme, a ministry standing up something new — where no incumbent LMS exists.
(2) An **EMEA sovereignty** engagement where the buyer needs the data, the platform and ideally the
vendor inside Europe.

**Why it is new:** every other pattern in this KB pays the same architectural tax — Globant's agent
code must sit on the far side of a network boundary because the LMS is GPL/AGPL. **`OpenOLAT` is
Apache-2.0 with 31,877 commits**, so for the first time that tax is optional.

**Stack**
- `OpenOLAT/OpenOLAT` (**Apache-2.0**, 448 ★, 31,877 commits) — the LMS. Teaching, learning,
  assessment, communication, modular course authoring. frentix GmbH (Switzerland), built on the
  University of Zurich's OLAT 7.1
- `ArnaudGuiovanna/tutor-mcp` (MIT, 52 ★) — the P2 pedagogy engine; BKT, FSRS, prerequisite gating
- `HKUDS/LightRAG` (MIT, 40.2k ★) — retrieval over the client's curriculum
- `HKUDS/DeepTutor` (Apache-2.0, 41.7k ★) — conversational surface
- `huggingface/smolagents` (Apache-2.0, 29.9k ★) — agent loop for custom tools
- Self-hosted models (in-region) for the sovereignty case
- **Not** `pylti1.3`. That is the point of this pattern

**Wiring**
1. Confirm the licence from the **file, not the page.** OpenOLAT's GitHub sidebar names no licence;
   `LICENSE` is the full Apache-2.0 text followed by two provenance notices crediting the OLAT
   Zentrum at the University of Zurich and the OpenOLAT community/frentix GmbH. **Those are
   attribution notices in the NOTICE tradition, not additional licence terms** — the grant is
   Apache-2.0. Record it that way in the licence inventory and attach the file to the SOW. Pin to a
   commit and keep the NOTICE attribution intact in any distribution.
2. Deploy OpenOLAT in-region. For the sovereignty case this is the whole proposition: European
   platform, European maintainer, client-controlled infrastructure, no US hyperscaler dependency.
3. **Integrate the agent in-process.** Apache-2.0 permits linking Globant's code to the platform, so
   ship one deployable instead of a tool plus a bridge. Keep the agent in its own module behind a
   clean interface anyway — not for licence reasons now, but so the work ports to a Moodle or Canvas
   client later across an LTI boundary (P1).
4. Run tutor-mcp as the pedagogy engine and LightRAG as the retrieval layer, exactly as in P1/P2.
   Add P1's **step 1b FERPA/GDPR retrieval filter** — in EMEA this is GDPR and Annex III evidence,
   not optional.
5. If the client is EMEA, **run P4 on top.** Apache-2.0 removes the licence boundary; it removes
   nothing about the AI Act. Globant is still the provider and still owes the conformity file.

**What this pattern does NOT do.** It does not apply to a client already running Moodle, Canvas,
Open edX or Sakai — which is nearly every client. There, the incumbent platform is a given and the
LTI boundary is mandatory; use P1. **Do not propose a migration to OpenOLAT.** 448 stars against
Moodle's 7.5k and Canvas's 6.9k is not a competitive position, the documentation's centre of gravity
is Swiss-German, and no institution is leaving Canvas for it. This pattern is for the cases where
there is nothing to migrate from.

**The honest risk:** a smaller community than Moodle or Open edX, which means fewer integrators,
less third-party plugin supply and a thinner hiring pool. Price support accordingly, and do not
present it as a like-for-like Moodle substitute.

**Estimate:** 8–10 weeks to pilot (greenfield), 12–14 weeks with P4's conformity file for an EMEA
public-sector buyer. Roughly 2–3 weeks less than the equivalent P1 build, because the LTI bridge
and its testing disappear.

---

## P9 — The COPPA disclosure boundary (North America K-12) — NEW

**Time**: 3–5 weeks for the audit, 6–10 weeks for remediation | **Licences**: all permissive
**Trigger**: the amended COPPA Rule, full compliance required since **2026-04-22**

**Why this is the shortest-cycle pattern in this file.** It does not ask the district to buy a new
capability. It tells them something they already own is out of compliance with a federal rule that
took effect six months ago, and then fixes it. The budget line exists before the conversation does.

**The legal mechanic, stated precisely because the whole pattern turns on it.** Amended
§312.5(a)(2) requires **separate verifiable parental consent before a child's personal information
is disclosed to a third party**, and the exception covers disclosures *integral* to the service,
not merely useful or convenient. A parent may consent to the product and refuse the disclosure.
The Rule also adds **retention limits**, a **written, published retention policy**, and
**biometric identifiers** to the definition of personal information.

**In a typical 2025-vintage K-12 tutor, the pupil's prompt goes to OpenAI, Anthropic or Google.
That is a disclosure to a third party.** If it was covered by a single blanket consent at
sign-up — which is the normal implementation — the deployment is non-compliant.

### Stage 1 — the posture audit (3–5 weeks, sellable on its own)

Inventory, for every AI feature the district runs:

1. **Egress**: which fields leave the district boundary, to which processor, under what contract.
   Prompts are the obvious one; transcript history, assignment text, IEP-adjacent notes and voice
   audio are the ones that get missed. Voice adds biometrics, which are now PII by definition.
2. **Consent structure**: is there one consent or two? If the parent cannot accept the product and
   decline third-party model disclosure *independently*, there is a finding.
3. **Retention**: is there a written, published retention policy, and does the system actually
   enforce it — including on the processor's side, where the contract usually says 30 days and
   nobody has checked.
4. **Integrality argument**: for each disclosure you intend to keep, write the sentence explaining
   why it is integral to the service the parent asked for. If that sentence is hard to write, the
   disclosure fails the exception.

Deliverable: a findings register mapped clause-by-clause, with each finding marked
*remediate-in-place* or *remove-the-disclosure*.

### Stage 2 — remediation, and there are only two real answers

**Answer A — separate the consent and keep the disclosure.** Split the consent flow in two, gate
model calls on the second grant, and degrade gracefully for pupils whose parents granted only the
first: the product must still work, teacher-facing or with local-only features. Add retention
enforcement as a scheduled job with an audit record per deletion, reusing the hash-chained audit
shape the governance layer in **P3** already builds. This is the cheaper path and it leaves the
district's existing vendor relationships intact.

**Answer B — remove the disclosure entirely.** If the model call never leaves the district
boundary, §312.5(a)(2) is not engaged for that call. Two routes, both already in this KB:

- **On-premise inference behind the LMS the district already runs.** Moodle's core AI subsystem
  takes an **Ollama** provider directly, and its **OpenAI-compatible** provider accepts a
  self-hosted **LiteLLM** or **LocalAI** gateway (`verticals/solutions.md`). The pupil's prompt
  reaches a model the district operates. No third party, no second consent, no retention exposure
  at a processor.
- **Offline-first delivery** where connectivity or policy makes even on-premise inference
  impractical — **Kolibri** (MIT) plus the local tutor shell in **P5**, with
  `zijinz456/OpenTutor` (MIT, 10+ providers incl. local) as the agent shell.

**Pair B with the deterministic pedagogy engine and the compliance story gets better, not worse.**
`tutor-mcp` (MIT) runs BKT, FSRS and prerequisite gating **locally against SQLite** — the mastery
model, which is the most sensitive longitudinal record in the system, never needs to leave the
building at all. The LLM is then only a language surface over a local decision engine, and the
smallest possible share of pupil data crosses any boundary. **This is the strongest commercial
argument in this KB for the architecture it has advocated for four passes, and it now has a
federal rule behind it rather than an aesthetic preference.**

### What not to build

**Do not build a COPPA compliance engine.** `repos/foundations.md` records about a dozen
FERPA/COPPA governance repos, every one at 8 stars or fewer and nearly all started in the two
months after the April deadline. The market is forming; none has won; and a client's compliance
posture should not sit behind a 1-star dependency. Build the audit as a method and the remediation
as architecture, reuse **P3**'s audit-logging layer, and keep the legal determination with the
district's counsel — the engagement is the disclosure-boundary redesign, not a legal opinion.

**Scope boundary to state in the SOW:** Globant determines where data flows and makes it match what
the district's counsel says the Rule requires. Globant does not certify COPPA compliance.

---

## P10 — The verified curriculum spine (LATAM now; APAC as a build; **cross-national and licensed, from p326**) — NEW

**For:** any engagement where the client is accountable to a **national or state curriculum
standard** — a ministry, a public school network, a board, a national edtech, a university serving
a regulated programme. This is the pattern that answers "how does your tutor know what my
jurisdiction requires it to teach?" with data instead of a prompt.

**Why it is new, and why it is the most defensible recipe in this file:** pass 319 found the first
artefact in this sector that turns a national curriculum into verified, permissively licensed,
machine-readable infrastructure **and publishes what it is worth.**

### Variant A — Brazil, today, with components that already exist

**Stack**
- `bncc-dev/bncc-dados` (**MIT code / CC BY 4.0 data**, 22 ★, 40 commits) — the BNCC as **1,721
  verified learnings** (1,580 basic-education skills across three stages plus the 141-item Computing
  complement), JSON canonical with SQLite/SQL/CSV builds, JSON Schema draft 2020-12, content version
  `dados-2026.08`
- `bncc-dev/bncc-pacotes` (**MIT code / CC BY 4.0 data**, 9 ★, 103 commits) — npm `@bncc/dados`,
  **npm `@bncc/mcp` (seven MCP tools)**, PyPI `bncc`, and a **hosted keyless MCP endpoint** at
  `mcp.bncc.dev`
- `bncc-dev/bncc-benchmark` (**MIT code / CC BY 4.0 items and results**, 9 ★, 82 commits) — the
  acceptance test
- `HKUDS/LightRAG` (MIT) + `HKUDS/DeepTutor` (Apache-2.0) — retrieval and tutoring, as in P1
- `portabilis/i-educar` (GPL-2.0, **34,948 commits**) and `portabilis/i-diario` (**licence not shown
  — read the file**) — the records layer a Brazilian public client is already running
- `dmitry-viskov/pylti1.3` (MIT) or `tsugiproject/tsugi` (Apache-2.0) — the boundary

**Wiring**
1. **Pin the curriculum dataset to a release, not a branch** (`dados-2026.08`, schema v1.1.0), and
   record the checksum. The packages already do this internally; your deployment must too, because
   a curriculum that changes silently under a tutor is a correctness incident.
2. **Resolve every learning objective through the MCP server or the typed package — never through
   the model's memory.** This is the whole point: a well-formed code that does not exist returns an
   explanatory error rather than `null`, which is what stops a tutor inventing a standard.
3. **Index the client's own material with LightRAG and link each chunk to one or more curriculum
   codes.** The codes are the join key between what the client teaches and what the state requires.
4. **Expose two retrieval paths to the tutor**: curriculum (authoritative, from the dataset) and
   course material (client-owned, from LightRAG). Keep them separate in the prompt and label them,
   so a citation can always be traced to one or the other.
5. **Run the benchmark as the acceptance test before go-live**, on the client's own model and
   configuration: direct lookup, existence (including plausible fake codes — this is the one that
   catches a confident tutor), open generation, reverse lookup. **Publish the result to the client.**
6. Keep Globant's agent on the far side of the LMS/SIS boundary as always: i-Educar is GPL-2.0, and
   i-Diário's licence is unresolved.

**What to promise, with the number behind it:** on this curriculum, an ungrounded model invents a
standard **31.9%** of the time; with the verified dataset queried over MCP, **2.3%**; with the data
pasted directly into the prompt, **0.2%**. Across the models the benchmark tested, faithful-text
rates ran from **88% down to 3%** — so **no model choice closes a 30-point grounding gap.**

**Estimate:** 5–7 weeks on top of P1, most of it in step 3 (mapping client material to codes).

### Variant B — India, where the artefact barely exists and the mandate is dated

> **🟡 UPDATE, pass 323.** This variant's premise was *"the artefact does not exist."* **It now
> partly does, and it has no licence.** `razi-03/NCERT-CKG` (`repos/foundations.md`) covers **Class X
> NCERT Mathematics from 18 PDFs**: **10,417 CKG nodes, 1,682 semantic nodes with provenance at
> 1,682 / 1,682, 13,757 provenance-aware edges** — and it **separates prerequisite reasoning from
> textbook ordering**, explicitly refusing to treat chapter order as prerequisite evidence. **That is
> step 1 of the build below, done correctly, by someone else, on one grade of one subject.**
>
> **What this changes about the engagement, concretely:**
>
> - **Step 0 is now "talk to `razi-03`."** 0 stars, 0 forks, **two commits, no LICENSE file**. A
>   permissive licence on that repository would hand this build a verified Class X Mathematics seed
>   and a method already aligned with Brazil's. **That is the cheapest possible acceleration of a
>   10–14 week build, and it costs one email.** If the answer is no, nothing is lost — the method
>   below is unchanged.
> - **Two unknowns to resolve before using any of it:** the README says **nothing about textbook
>   copyright or whether the 18 NCERT PDFs are bundled** (this KB has already recorded one NCERT
>   project that bundles textbook PDFs, and that is a live copyright question), and it **never
>   mentions an LLM**, so whether the edges are model-derived is **unknown rather than disclosed.**
>   Neither can be assumed benign; both are answerable by reading the tree.
> - **The deadline is unchanged and close:** AI + Computational Thinking compulsory for **Classes
>   3–8 from 2026-27 across 32,900 CBSE schools.** Class X Mathematics is not in that band, so the
>   seed does not cover the mandated grades — **it de-risks the method, not the scope.**
> - **The window is narrower than p319 priced it.** See Variant C: the uncontested-opportunity
>   framing no longer holds region-wide.

**The gap, as measured in p322 and now qualified:** GitHub's `ncert` and `cbse` topics hold 180
repositories and **nothing above 15 stars that is curriculum infrastructure** — and that sweep
**missed** the artefact above, which a query on the *artefact type* rather than the country topic
found in one search. The one MCP server
(`jinanshm/ncert-mcp`, 1 ★, 2 commits) is **unlicensed** and ingests by downloading the NCERT PDFs
and **tagging chunks with an LLM via OpenRouter with no human verification described** — which is a
hallucination source with a schema. `praj2408/RAG-Enhanced-NCERT-Tutor` (MIT, 3 commits) **bundles
textbook PDFs**, a copyright question of its own. The best data asset is a **2018** scrape of
~20,000 schools. Meanwhile **AI + Computational Thinking is compulsory for Classes 3–8 from
2026-27 across 32,900 CBSE schools.**

**The build, copying Brazil's method rather than its data**
1. **Extract against the official source and verify it.** Character-level checking against the
   published curriculum document, not LLM tagging. A code sweep for missing and extra codes.
2. **Publish a schema** and 25–30 contract and completeness checks that run in CI, so a divergence
   fails the build rather than reaching a classroom.
3. **Keep a decisions log** for every inconsistency found in the source. This is what makes the
   dataset citable by a ministry.
4. **Split the licence deliberately**: permissive for the pipeline, attribution-only for the data,
   with the normative texts identified as official acts. That is what makes it adoptable by
   competitors — which is the point of a moat built on a standard.
5. **Ship an MCP server and typed packages** over it, plus a hosted endpoint.
6. **Build the benchmark alongside it**, including the fake-code existence task, and publish the
   numbers.

**Why do this rather than a tutor:** whoever holds the verified curriculum layer for a jurisdiction
is in every bid in that jurisdiction, because the alternative is each vendor re-deriving it badly.
~~At 22 stars in Brazil, **nobody is competing for this yet.**~~ **Corrected in p323: pick the
jurisdiction deliberately, because one is now contested.** Brazil's `bncc-dev` is still at
low-double-digit stars and uncontested; **China's equivalent has 420 stars, 67 forks and a NeurIPS
2026 acceptance** (Variant C). India is contested by one unlicensed two-commit repository. **The
opportunity is per-jurisdiction, and it is no longer uniformly open.** It is fundable as a standalone asset
(a board, a ministry, a national edtech, or a foundation), it is reusable across every subsequent
engagement in the market, and it is the rare deliverable whose quality is **objectively
demonstrable** — the benchmark is the proof.

**Estimate:** 10–14 weeks for one subject across the mandated grades, including verification;
longer for a full curriculum. **Verification is the majority of the work and the entire value.**

**Where else this applies:** anywhere with a published national curriculum and no data layer —
which, on the topics swept this pass, is everywhere except Brazil. Germany's attempt was archived
in 2021; the Dutch and Spanish-language topics produced course material; the English `oer` topic
produced textbooks and no competency metadata. Ed-Fi (`repos/foundations.md`) is the North American
**rostering** standard and does not cover curriculum.

### Variant C — China and the method-reuse play, where the artefact exists and its data is NonCommercial — NEW in p323

**The situation that makes this a distinct variant:** `haolpku/K12-KGraph` (`repos/foundations.md`)
has already built what Variants A and B describe, for China's PEP K-12 curriculum, to a standard a
Globant build would be measured against:

| | What it holds |
|---|---|
| Scope | **48 PEP textbooks** — Mathematics 23, Physics 9, Chemistry 7, Biology 9 |
| Graph | **10,685 nodes**, **23,278 edges across 9 edge types**, **every edge carrying an `evidence` field** linking to textbook source text |
| Verification | **12 subject-qualified expert annotators, Fleiss' κ = 0.84**; DAG validation of `is_a` and `prerequisites_for`; 3-expert spot-check at **98.4% fully correct** |
| Proof | **K12-Bench, 23,640 multi-select questions**; K12-Train, 2,267 pairs; three fine-tuned checkpoints on Hugging Face |
| Standing | **NeurIPS 2026 Evaluations & Datasets Track**, 420 ★, 67 forks |
| Licence | **MIT (code) / CC BY-NC-SA 4.0 (graph, benchmark, training data)** |

**The licence is the whole design constraint, so state it to the client on day one:** the
**pipeline is MIT and reusable**; the **curriculum graph, benchmark and training data are
NonCommercial and ShareAlike and cannot enter a commercial deliverable — in China or anywhere
else.** ShareAlike would additionally attach to any derivative graph. **There is no version of this
engagement in which K12-KGraph's data ships.**

**What to actually sell, in order:**

1. **The method transfer, not the data.** Fork the **MIT pipeline** and run it against the client's
   own corpus — their textbooks, their syllabus, their licensed content. **The expensive, risky part
   of P10 has a working reference implementation** with a published quality bar; that converts a
   10–14 week verification project from a research bet into an execution task. **Price the saving,
   and be explicit that the saving is in the method.**
2. **Adopt its verification protocol as the acceptance criterion.** Per-edge source evidence,
   automatic DAG validation of the prerequisite subgraph, multi-annotator agreement with a reported
   κ, and a stratified expert spot-check. **This is the first externally published, peer-reviewed
   quality bar for a curriculum graph, and a client can hold a vendor to it.** Brazil's `bncc-dev`
   supplies the complementary half — character-level verification against the homologated source,
   contract checks in CI, a decisions log. **Together they are the specification Globant should be
   writing into its own P10 statements of work.**
3. **Use K12-Bench as an off-the-shelf evaluation instrument where the licence permits
   non-commercial use** — internal benchmarking, a research collaboration, a public-sector pilot
   with a university partner. **Not in a paid deliverable.** Check the specific use against
   CC BY-NC-SA 4.0 with counsel; "internal" and "non-commercial" are not synonyms.
4. **Where the client wants the graph itself and the licence forbids it, the answer is Variant A or
   B's build.** Rebuilt from the client's corpus with the client's grant. **The existence of a
   NonCommercial artefact is a reason the build is well understood, not a reason to skip it.**

**The competitive read, which is the real reason this variant exists.** p319 priced the verified
curriculum layer as an **uncontested** build-once opportunity at 22 stars. **In APAC it is
contested, by an academic group, with a peer-reviewed quality bar and 420 stars.** Two consequences:
**expect a Chinese or regional client to know this artefact already**, and **expect the quality bar
in any APAC curriculum-data bid to be K12-KGraph's, not this KB's.** The jurisdictions still open —
India (barely, see Variant B), most of LATAM beyond Brazil, most of EMEA, and everywhere on
`repos/foundations.md`'s unswept-language list — are where the uncontested framing still holds, and
**that framing now has a shelf life.**

**Estimate:** 4–6 weeks for a method-transfer engagement (fork, re-target the pipeline to the
client's corpus, stand up the verification protocol and acceptance criteria) before any curriculum
volume is processed; the per-subject build then prices as Variant B. **The first deliverable is the
acceptance criteria, and it is sellable on its own.**

### Variant D — the cross-national spine, available today, for a client with no jurisdiction mandate — NEW in p326

**For:** the engagement Variants A and B do not cover — an international school network, a
consumer or B2C learning product, a corporate foundation's K-6 programme, a pilot that has to run
before a ministry conversation exists, or **any client in a jurisdiction this KB has no curriculum
artefact for.** Variants A and B both start from a national mandate. **This one starts from the
absence of one.**

**Stack**
- `withmarbleapp/os-taxonomy` (**ODbL-1.0 database / CC BY-SA 4.0 text**, 6.1 ★k) — **1,591
  micro-topics, 3,225 prerequisite edges, ages 4–15, eight subjects, 2,189 links into 3,261
  standards across UK NC 2013, CCSS ELA, CCSS Math, NGSS K-5, NGSS MS, C3 and IB PYP PSPE.**
  Ships `assessmentPrompt` on **all 1,591** topics and `evidence` descriptors on 1,556
- `tbh-23/Homestead` (**MIT**, 15 ★) — **read it before you write anything**: the runtime-fetch
  boundary, the 90% mastery gate and the independently re-solved mastery tests are already built
- `ArnaudGuiovanna/tutor-mcp` (MIT) — BKT mastery state and prerequisite rules over MCP, keyed to
  the taxonomy's topic IDs
- `open-spaced-repetition/fsrs4anki` (MIT) — retention scheduling once a topic is mastered
- `openfun/ralph` (MIT) — xAPI learning records, **one statement per topic ID**
- `HKUDS/LightRAG` (MIT) — retrieval over the client's own material, chunks linked to topic IDs

**Wiring**
1. **Pin a commit and record the SHA-256s from `data/manifest.json`.** The dataset moves: every
   secondary description in circulation says 1,590 topics / 3,221 edges, and the file shipped on
   2026-10-19 is **1,591 / 3,225**. Verify the hash on every refresh and diff the topic set —
   Homestead does exactly this and surfaces added and removed topics to the user.
2. **Do not vendor the data. Fetch it at runtime into a cache outside your repository.** This is
   P13 and it is what keeps the ODbL database out of your product.
3. **Load `dependencies.json` as the ordering authority, and respect `strength`.** 2,030 edges are
   `hard` — gate on these. 1,195 are `soft` — surface them as *"this will be easier if…"*, never
   as a block. **Every edge carries a prose `reason`; show it to the learner or the parent.** It
   is the cheapest explainability win in the whole pattern and it was authored, not generated at
   request time.
4. **Use `assessmentPrompt` as the mastery check, not a model-generated question.** One per topic,
   all 1,591, with a `{{name}}` placeholder to substitute or strip. **Substitute server-side, as
   P12's Panama design does** — the prompt sent to the model should not carry the learner's name.
5. **Use `evidence` as the rubric.** Three observable can-do statements per topic on 1,556 of
   them; they are what a teacher or parent signs off against, and what an LLM judge should be
   scored on reproducing — not helpfulness. See the *"prove it teaches"* stage.
6. **Join the client's own material to topic IDs with LightRAG**, exactly as in Variant A. The
   topic ID is the join key between the spine and everything the client already owns.
7. **Write client-jurisdiction extensions into an overlay table keyed by topic ID — never into the
   graph.** This is the commercial decision in the whole pattern; see P13.

**What to promise, and what not to.** Promise **sequencing, age banding, standards alignment and
assessment coverage on day one** — those are shipped data, verifiable against published checksums,
and they are normally six weeks of authoring. 🔴 **Do not promise instructional effect.** The
dataset's own teaching-research layer is **agent-authored, unverified for this release, covers
1,051 of 1,591 topics** and describes itself as *"research-informed proposals, not empirically
validated interventions."* **English, History, Computing, Life Skills, PSD and Learning to Learn
have zero research records**, and the file says so per subject. Quote the coverage table; it is a
better slide than a claim.

🟢 **The one-slide pitch this variant unlocks, for North America and EMEA literacy mandates.**
The entire **`Computing` subject is AI literacy — 21 topics, ages 5–11**, sequenced, age-banded
and assessment-ready: *Smart Versus Not-Smart Devices*, *Voice Assistants and How They Work*, *AI
Mistakes and Limitations*, *Recommendation Systems and Filter Bubbles*, *Bias in AI Systems*, *AI
Data Collection and Privacy*, *Deepfakes and AI-Generated Content*, *Designing Fair AI Rules*,
*AI and the Future of Work*, *AI and the Environment*. **Against California AB 2876, Utah H.B.
273, Illinois HB 316 and the EU AI Act Article 4 staff-literacy duty**, that is a curriculum a
district can adopt rather than commission. 🔴 **It stops at age 11 and HB 316 is grades 6–12 —
scope and price the upper-secondary extension explicitly rather than letting it be assumed.**

🔴 **The licence check to run before the proposal goes out.** Four curricula ship **codes only**
(NGSS K-5, NGSS MS, C3 Social Studies, IB PYP PSPE) and **Common Core ships in full but under the
purpose-limited CCSS Public License, not ODbL.** **NGSS is a WestEd trademark with a
sample-approval requirement for commercial use.** The topic→standard *links* are unaffected, so
*"this lesson aligns to NGSS 1-ESS1-1"* is fine everywhere; **rendering the text of 1-ESS1-1 is
not.** Read `PROVENANCE.md`, and if the client needs verbatim text, clear it upstream — the
dataset's export tool takes a per-source switch for exactly that case.

**Estimate:** 3–4 weeks to a working mastery tutor on top of P1 or P2 — the shortest curriculum
path in this file, because **the spine is the part that is already built.** Most of the time goes
into step 6.

---

---

## The cross-cutting risk, re-stated in pass 319 — and now with a real alternative

**Eight of these ten patterns cross the LMS boundary through `dmitry-viskov/pylti1.3`: one MIT
library, re-verified in pass 319 at 138 stars, 84 forks, 178 commits, a single maintainer, 39 open
issues and still no published release.** It is the most load-bearing and least redundant component in this KB's architecture, and
pass 317 is the first pass to say so out loud.

It is good software — it covers the whole LTI Advantage surface (Deep Linking, AGS, Names and Roles,
Course Groups, Submission Review, Data Privacy Launch), which is why every pattern leans on it. The
risk is not quality, it is concentration. **Name it in the risk section of any SOW that depends on
it**, and know the fallbacks — which pass 318 made specific. `1EdTech/ltibootcamp` indexes LTI 1.3
implementations across seven languages: **`ltijs` and Atomic LTI Worker (Node)**, **OAT's core /
Deep Linking / Names & Roles libraries and a Symfony bundle (PHP)**, **UOC's library and Spring
Boot library (Java)**, **`LtiAdvantagePlatform` (.NET)**, **Atomic Jolt's starter app (Ruby)**,
**Atomic Forge (Rust)**, and `django-lti` alongside `pylti1.3` itself (Python). `ltijs` is the
route `blamb/lti-tutor` took to working deep linking and AGS passback against Moodle.
**Caveat before you scope on any of them:** that index carries no LICENSE file, its newest content
folder is `europe_tech_2020`, and its own README says the entries "have not been vetted" — verify
each against its repository. And **P8 avoids the dependency entirely.**

**Pass 319 found the alternative itself, not another index: `tsugiproject/tsugi` — Apache-2.0,
376 ★, 266 forks, 4,011 commits, Apereo Incubating**, maintained around the co-author of the LTI
specification, with an IMS ContentItem app store and low-level IMS libraries shared with Sakai.
Against 178 commits and one maintainer that is a different class of dependency. **Two caveats
before it goes in a SOW:** it is **PHP**, and **its GitHub page does not state which LTI versions or
Advantage services it implements** — verify the Advantage surface against the repository and the
Tsugi documentation first. Also recorded for breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229
commits)** covers **SCORM 1.2 and 2004** for the large installed base of courseware LTI does not
reach — **AICC was removed in v3.0.0 and cmi5/xAPI are roadmap "potential" only**, so promise
neither.

---

## The "prove it teaches" stage, specified — what to actually test, pass 323

p322 added a *prove it teaches* stage to P1 and pointed at MathTutorBench. **Pass 323 read four
2026 education benchmarks and the stage can now be specified as test cases rather than a gesture.**
Three of the four have **no public code** and the fourth has **no licence** (`intel/trends.md`), so
**this stage is something an engagement builds** — but the findings tell you exactly what to build.

**Run these four checks, in this order, on any tutor deliverable:**

1. **Pedagogy, scored without an LLM judge.** MathTutorBench's task shapes — problem solving,
   socratic questioning, solution correctness, mistake location, mistake correction, plus the
   pedagogy win-rate tasks — scored against ground-truth teacher utterances. **Never report an
   LLM-judged helpfulness score as evidence of learning**; the leakage audit
   (`bydeng01/conv-vs-ped-tutor`) exists because a judge will reward a tutor for handing over the
   answer.
2. **Demographic fairness, on the cues that actually move** — **language and immigration background
   first, then first-language, then SES, then gender.** EduFair-Bench's finding is that **language
   and immigration cues produce larger gaps than gender and SES**, which is the reverse of most
   fairness test plans. **And because capability and fairness are largely orthogonal, do not accept
   a model upgrade as a fairness remediation** — re-test after every model change.
3. **Adversarial safety with teacher personas, not generic jailbreaks.** EduGuardBench's shape:
   persona-based prompts targeting **academic misconduct** specifically, scored by attack success
   rate **and** a three-tier refusal-quality assessment. **Grade refusals, do not just count
   them** — its *Educational Transformation Effect* shows the best outcome is a refusal that becomes
   a teachable moment, and that capacity is **strongly negatively correlated with attack success
   rate.** A tutor that refuses bluntly and a tutor that redirects into learning score the same on a
   binary refusal metric and are not the same product.
4. **Model selection, tested rather than assumed.** Two results overturn common assumptions:
   **safety is not monotonic in model size** (mid-sized models were most vulnerable), and
   **education-specialised models led neither education module** of ELBench's nine-model comparison.
   **So: no "we used a bigger model" safety argument, and no domain-tuned-model premium without a
   head-to-head on the client's own tasks.**

**Discipline, borrowed from the two pre-registered audits and non-negotiable if the number will
appear in a bid:** pre-register the comparison, **freeze the dataset and hash it** before analysis
runs, separate registered diagnostics from post-hoc analysis, and keep a decisions log. The
`ability-levels-audit` headline is the warning — **difference-in-differences on a censored rating
scale can manufacture an effect that is not there**, and that is the shape of most tutoring-uplift
claims a client will be shown.

**Sellable on its own:** 3–4 weeks as an evaluation engagement over a client's existing tutor,
whoever built it. **It is the cheapest credible entry point in this KB**, and after this pass it is
the one with the clearest external references.

## Pattern selection by region

| Region | Lead with | Why |
|---|---|---|
| Greenfield / no incumbent LMS (any region) | **P8** | Apache-2.0 OpenOLAT removes the LTI boundary; one deployable, 2–3 weeks less build |
| North America | **P9 first**, then **P3 + P6**, then P7 where restricted, then P1/P2 | **P9 leads because the amended COPPA Rule has been in force since 2026-04-22 and most deployed K-12 AI is likely non-compliant** — it sells into the installed base rather than competing with a frontier-model seat licence. Then the dated policy requirements (Ohio 2026-07-01, NC model policy 2026-12-31, Idaho SB 1227, 134 bills/31 states); governance is the budgeted line and the roster spine is now open source |
| EMEA | **P4**, with **P8** where sovereignty decides the deal | Provider-side conformity under Annex III; Article 50 live, watermarking and new prohibitions both land 2026-12-02, 2027-12-02 the real deadline. OpenOLAT is the only permissive, EMEA-authored, EMEA-maintained LMS in this KB |
| EMEA — Gulf | **P1/P2 with Arabic-first localisation** | UAE ~28% of GCC edtech, National AI Strategy 2031; incumbents (Alef, Classera, Abwaab) are proprietary and buying integration, not platforms |
| EMEA — Africa | **P5** | Strongest low-resource evidence base in the world (Edo State, EIDU); DigiSchool tablets are installed hardware needing content |
| APAC | **P10 Variant B + P5** (India), P1 + labelling (China), P1 (Japan), **P4 ported** (South Korea) | Curriculum mandate plus infrastructure gap — **and pass 319 found the curriculum *data* gap under it: 180 NCERT/CBSE repositories and no verified dataset**, so the spine is a build, not a dependency. China needs labelling/registration at the generation step; Japan has the fewest blockers; **Korea's Framework Act on AI is in force since 2026-01-22 and names student evaluation as high-impact**, so the EMEA conformity file sells there now — and the 2025 AI-textbook reversal means every Korean and regional buyer is bidding on deployment risk, not capability |
| APAC — Australia / NZ | **P7**, then P1 | Ipsos 2026 finds ANZ public support for banning AI in schools *higher* than in Asian markets — closer to the US restriction posture than to the rest of APAC |
| LATAM — Brazil | **P10 Variant A**, then P2, with P4's artefacts ported | **The only jurisdiction with a verified open curriculum dataset, an MCP server over it and a published grounding measurement (31.9% → 2.3%)**, plus a 34,948-commit municipally originated SIS with no AI in it. Brazil's June 2026 AI/tech agreement with the EU means the conformity file transfers, and PL 2338 is risk-based |
| LATAM — Spanish-speaking | **P2**, with P4's artefacts ported, and P10 as a build | No equivalent curriculum data layer was found in the Spanish-language topic sweep, so P10 here is Variant B work. The 92%-usage / 30%-satisfaction gap and the 50/19 feedback gap are delivery problems, which P2 answers |
| Any region, no jurisdiction mandate — international schools, B2C, corporate foundations, pre-ministry pilots | **P10 Variant D + P13** | **New in p326.** The cross-national spine (`os-taxonomy`: 1,591 topics, 3,225 edges, seven curricula, ODbL + CC BY-SA) ships sequencing, age banding and 1,591 assessment prompts on day one, so the curriculum build that gates Variants A–C disappears. **P13 is not optional beside it** — it is what keeps the share-alike database outside a proprietary product. Strongest where a *literacy* mandate is the buying motion (Illinois HB 316, California AB 2876, Utah H.B. 273, EU AI Act Art. 4): the entire Computing subject is 21 AI-literacy topics, ages 5–11. **Age band stops at 11 — price the upper-secondary extension.** |

**P13, new in p326, is the second pattern selected by a *requirement* rather than a region, and the requirement is a licence.** It applies wherever the asset the client most wants is published under share-alike terms — which, since the sector's largest open curriculum graph is ODbL-1.0, is now the common case rather than the awkward one. 🔵 **Read it before quoting any engagement that consumes external data: it is three to five days designed in at the start and a bad week retrofitted.**

**P11, new in p324, is the first pattern in this file that is selected by a *requirement* rather
than by a region or a starting position** — it applies wherever assessment integrity is a stated
obligation, which on this pass's evidence is all four regions with a different statute behind it in
each: human-oversight mandates in North America (Oklahoma, Maryland, California AB 1159), high-risk
assessment duties under the EU AI Act in EMEA, Vietnam's *"sole basis … without meaningful human
review"* carve-out in APAC, and the 87%-use / 26%-strategy institutional gap in LATAM. **Lead with
it wherever the buyer has already written an integrity policy and has nothing to implement it
with**, and pair it with **P3** in North America, where it is the same governance sale.

**No pattern here is LATAM-only or North-America-only.** P1 and P2 are the portable core; P3, P4,
P5, P6, P7 and P9 are the regional wrappers that make them biddable. **P10 is portable in method and
regional in data** — Variant A is a Brazilian assembly job, Variant B is the same recipe anywhere a
curriculum is published and not yet machine-readable, which on this pass's evidence is everywhere
else. **P8, new this pass, is the only
one selected by the client's starting position rather than by region** — it applies wherever there
is no incumbent LMS, and it is strongest in EMEA because sovereignty and a permissive European
platform happen to answer the same objection.

**For LATAM specifically, pass 317 sharpened the pitch without needing a new pattern.** UNESCO
IESALC (2026-09-09; 200 institutions, 19 countries) found **87% of LAC higher-education institutions
using AI and only 26% with a formal AI strategy** — a 61-point gap, with adoption driven by
individuals rather than institutions. That is P3's governance deliverable with the compliance driver
swapped for an institutional-risk driver, and it is the same work this KB already sells in North
America.
