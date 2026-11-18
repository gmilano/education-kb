---
industry: education
region: Global
updated: 2026-11-18
---

# Compose patterns — education

Concrete recipes. Each names the exact repos, how they wire together, the licence posture of
the result, and a realistic build estimate. Every repo referenced is verified in
`agents/top.md`, `repos/foundations.md` or `verticals/solutions.md`.

**Twenty-three patterns, plus the G1 licence gate added in p897 and extended with gate `904-G1` in p904** (**P22 added in `p903`** — the
national-curriculum corpus pattern, built from the Arabic-language channel's finding that the
curriculum exists at national scale and carries no grant; see `intel/trends.md` **T26**) (**P20 added in `p901`** — the first end-to-end permissive *synchronous* pattern in this file, unlocked by `p901`'s verification of `jitsi/jitsi-meet` at Apache-2.0) (**P19 added in `p900`** — the
first end-to-end permissive pattern in this file that is not offline-first, built entirely from
rows promoted out of this base's own unshelved ledger) (**P16 added in `p898`**) that runs ahead of all of them.
**p895 added P14** — offline-first literacy delivery on the one Africa-origin
permissive platform this KB has verified (`elimu-ai`), with the agent tier as studio IP because
the supply measurement leaves nothing licensed to adopt (see **T16**). **It is also the only
pattern here whose licence posture is permissive end to end.**

**p894 added P12 and P13** — the registrarial tier the KB has named as its
top opportunity for four passes, now scoped against the Apache-2.0 platform that turned out to
exist (`UniTime`), and a persona-stateless tutor design for the three regimes that have made
affective design a regulated activity for minors (see **T14**).

**Licence rule that governs all of these.** Open edX (AGPL-3.0), Canvas (AGPL-3.0) and Moodle
(GPL-3.0) are copyleft. Integrating over **LTI 1.3** or **MCP** keeps your tool a separate
work; forking the platform does not. Where a client needs a proprietary derivative, start from
**Artemis (MIT)**, **Kolibri (MIT)**, **elimu-ai/webapp (MIT)**, **Oppia (Apache-2.0)** or
**OpenOLAT (Apache-2.0)** instead.

---

## G1 — Licence pre-flight gate (run before *any* pattern below) — added p897

Every pattern here opens with a licence posture, and that posture is only as good as the licence
reading under it. **p897 byte-read the seven shelf rows whose licence was unresolved and five were
wrong as recorded** (see **T19**). This gate is the cheapest step in this file and it runs first.

### The script

[`compose/code/licence-grant-gate-p897/probe-grant.sh`](code/licence-grant-gate-p897/probe-grant.sh) —
no dependencies beyond `curl` and `sha256sum`.

```bash
./compose/code/licence-grant-gate-p897/probe-grant.sh frappe/lms OS4ED/openSIS-Classic
```

It probes **3 branches × 6 directories × 14 filenames** against `raw.githubusercontent.com` and
prints, for each hit, the **byte count and `sha256₁₂`** of the grant plus its first line. A repo
with no hit across the whole grid is reported as **unlicensed — do not ship**.

### Why the directory axis is the part people miss

GitHub's SPDX detector, and this KB's own probe until now, **classify the repository root only**.

| Repo | Root probe says | The gate finds |
|---|---|---|
| `OS4ED/openSIS-Classic` | `NONE` → reads as unlicensed | **GPL-2.0** at `master/docs/License.txt`, 17,286 B `224ac3d403e3` |
| `moodlehq/moodleapp` | `NO-LICENSE-FILE` | **Apache-2.0** at `main/COPYING.txt`, 11,358 B `cfc7749b96f6` |
| `frappe/education` | `NOASSERTION` | **GPL-3.0**, a **19-byte** `license.txt` naming the licence without reproducing it |

### The two failure modes it is built to stop

1. 🔴 **Shipping copyleft as permissive.** Several 2026 *"best open-source LMS"* comparisons list
   **Frappe LMS as MIT**. The gate reads **33,893 B of verbatim AGPL-3.0**. AGPL is
   **network-triggered** — hosting it for a client's students is a distribution event. The MIT
   belongs to `frappe/frappe`, the framework, not the LMS.
2. 🟡 **Discarding permissive options out of pessimism.** `Open-TutorAi/open-tutor-ai-CE` was
   carried as `OTHER` and therefore unusable; the gate reads **verbatim BSD-3-Clause**. In
   education, permissive is the scarce category — a false negative costs a real option.

### Gate rule

**No repo enters a client deliverable on the strength of a badge, a comparison article, or an
SPDX field.** Record the path, byte count and `sha256₁₂` of the grant next to the dependency. If
the grid returns nothing, the repo is all-rights-reserved regardless of how open it looks.
Budget: **minutes for a whole stack.**

### The payload axis, added as gate `904-G1` in p904

The directory axis above asks *where in the tree the licence file hides*. `904-G1` asks a different
question: **which licence governs the thing you are actually taking.** When a repository's payload
is data or content, the root `LICENSE` covers the code that produced it and **not** the asset.

| Repo | SPDX field says | Root byte-read says | The payload's actual grant |
|---|---|---|---|
| `bncc-dev/bncc-dados` | `MIT` | **MIT** (1,092 B) | 🔴 **CC BY 4.0** at `main/dados/LICENSE.md` (1,583 B) — **attribution required** |
| `bncc-dev/bncc-benchmark` | `NOASSERTION` | a Portuguese **index** to two files | **MIT** for `harness/`, **CC BY 4.0** for items, results and methodology |
| `bncc-dev/bncc-pacotes` | `NOASSERTION` | a Portuguese **index** to two files | **MIT** code + **CC BY 4.0** data + 🔴 **name and visual identity reserved** |

**Gate rule, additive to the one above.** Before recording a single SPDX value for a data or content
repository:

1. **Probe the payload directory for its own grant** — `dados/`, `data/`, `datasets/`, `content/`,
   `itens/`, `resultados/`, `corpus/`, `assets/`.
2. **Probe the split-licence index names** — `LICENSE-DADOS.md`, `LICENSE-CODIGO.md`,
   `LICENSE-DATA.md`, `LICENSE-CODE.md`, `LICENSE-CONTENT.md`. A root `LICENSE` that is *prose
   pointing elsewhere* is why GitHub returns `NOASSERTION`, and `p896`'s rule applies with a new
   mechanism behind it: **a `NOASSERTION` on a non-English repository is a prompt to read the file.**
3. **Ask the two questions no probe answers**: does the data licence impose **attribution** (if so it
   is a UI requirement, specified in the sprint that renders curriculum references — not a legal
   appendix), and **is the project's name or visual identity reserved** (see **T27**). A clean
   licence report is not evidence that the brand question was asked.

🔵 **Cost of skipping it, measured:** this KB's own 12-path probe would have published a 1,721-record
national-curriculum dataset as plain MIT, and a studio would have shipped a client product with an
unmet attribution obligation on its only substantive data dependency.

### The manifest axis, added as gate `905-G1` in p905

The two axes above ask which licence governs the code and which governs the payload. `905-G1` asks
the question that comes *after* both: **what else am I shipping, and can I ship it twice?** It was
written because the `p905` scan produced a wrong answer on two of its 14 targets before it produced a
right one.

**Rule 1 — an absent root manifest is not an absent dependency declaration. Probe the framework's
convention.**

| Stack | Where dependencies are actually declared | Root probe result if you skip it |
|---|---|---|
| Odoo addons (OpenEduCat, many LATAM ERP forks) | `<module>/__manifest__.py` → `depends`, and `'license'` lives here too | 🔴 no manifest at all |
| Moodle plugins | `version.php` → `$plugin->dependencies` | 🔴 no manifest at all |
| Open edX XBlocks | `setup.py` → `entry_points` | 🟡 misleading |
| Maven multi-module (Sakai) | the aggregator's `<module>` list, not the root `<dependency>` block | 🔴 undercounts |
| Python with extras (DeepTutor) | the leaves of the `-r` chain | 🔴 reports ~1 dependency |

**Rule 2 — a manifest under ~500 bytes is a pointer until proved otherwise.** Follow every `-r`,
`include:`, `extends` and `requires` to a fixed point and count at the leaves. `DeepTutor`'s
`requirements.txt` is 104 B: one comment and `-r requirements/full.txt`, which is itself 19 `-r`
lines into `requirements/modules/*.txt`. A root read gives a **floor**, never a total.

**Rule 3 — record the manifest depth beside every dependency count.** A figure without its depth is
not comparable between repositories, and that is exactly what made the largest education agent in
existence look like a one-dependency project.

**Rule 4 — read the pinning, and write it into the proposal.** Count `==` against the total:
`openedx/openedx-platform` **311/311**, `DeepTutor` **1/74**. If the base is unpinned and the client
needs a rebuildable handover, the lockfile is a **named week-one task with an estimate**, not a
footnote.

**Rule 5 — never infer a dependency-grant disclosure from a filename.** Of 14 education platforms,
`0` disclose their dependencies' grants, and the two files called `COPYRIGHT` disclose nothing: Odoo's
points at version-control history, Canvas's restates its own AGPL. **Open the file and count the
dependencies it names.** Zero is the expected answer, and it means the scan is the studio's to run
(`scancode-toolkit`, Apache-2.0) and the client's to be told about up front.

🔵 **Cost of skipping it, measured:** this pass's own scan would have published *"OpenEduCat declares
no dependencies"* and *"DeepTutor has one dependency"* — both false, both about platforms this KB
recommends — and would have handed a client the most-starred tutor in open source with no statement
that its build is not reproducible.

## P1 — Licence-clean AI tutor on a permissive LMS

**For:** any client who needs to keep the result closed, or who has no incumbent LMS.
**Region:** Global. Strongest fit EMEA (EU-origin stack, sovereignty-compatible).

```
ls1intum/Artemis (MIT)                  — LMS core, exercises, cohorts
  └── ls1intum/edutelligence (MIT)      — AI service suite, already integrated
        └── ls1intum/Pyris (MIT)        — LLM microservice behind the Iris tutor
              └── BerriAI/litellm (MIT) — provider gateway + per-course budget caps
                    └── ollama (MIT) or vllm-project/vllm (Apache-2.0)  — self-hosted inference
  └── ls1intum/Ares (MIT)               — automated programming assessment
  └── qdrant/qdrant (Apache-2.0)        — per-course retrieval, payload-filtered by course_id
  └── mem0ai/mem0 (Apache-2.0)          — per-learner memory ("what this student struggled with")
```

**Wiring.** Artemis already speaks to Pyris, so the integration work is configuration, not
code. Point Pyris at `litellm` instead of a provider SDK — that one indirection is what makes
inference swappable and gives you per-course cost caps. Scope every Qdrant query by
`course_id` in the payload filter; cross-course leakage is the most common correctness bug in
education RAG.

**Result licence:** fully permissive (MIT/Apache-2.0). Proprietary extensions are clean.
**Estimate:** 6–8 weeks to a departmental pilot.

---

## P2 — Governed AI tier over an existing Moodle or Canvas (no fork)

**For:** the common case — the client already runs Moodle or Canvas and cannot replace it.
**Region:** Global. LATAM/EMEA for Moodle, North America for Canvas.

```
Incumbent: moodle/moodle (GPL-3.0)  or  instructure/canvas-lms (AGPL-3.0)
   │
   ├── LTI 1.3 route:  Cvmcosta/ltijs (Apache-2.0)        — your tool, separate work
   │     (PHP shops: tsugiproject/tsugi, Apache-2.0)
   ├── MCP route (Canvas): vishalsachdev/canvas-mcp (MIT)  — agent tools over Canvas API
   ├── apereo/cas (Apache-2.0)                             — SSO, role-based access to the AI tier
   │
   └── Your AI tier (kept outside the LMS repo):
         langchain-ai/langgraph (MIT)     — orchestration; policy checks as explicit nodes
         BerriAI/litellm (MIT)            — gateway, per-user/per-course budgets
         HKUDS/LightRAG (MIT)             — graph RAG over the course corpus
         docling-project/docling (MIT)    — PDF/slide ingestion
         SYSTRAN/faster-whisper (MIT)     — lecture transcription
         yetanalytics/lrsql (Apache-2.0)  — xAPI statements for every AI interaction
         appsmithorg/appsmith (Apache-2.0)— teacher review queue
```

**Wiring.** The LMS stays untouched; your tool is an LTI 1.3 tool provider registered in it.
Make the human-review step a LangGraph node that *blocks* — if the teacher queue is down, the
AI output does not reach the student. Emit an xAPI statement to `lrsql` for every AI
interaction, including refusals; that log is both the efficacy evidence and the compliance
artefact. Moodle HQ's own `moodlehq/wiki-rag` (BSD) is the reference for first-party Moodle RAG.

**Result licence:** your tier is permissive and separate from the GPL/AGPL core.
**Estimate:** 8–10 weeks including LTI certification and SSO.

---

## P3 — North America K-12 policy-conformant assist (50-state configurable)

**For:** US districts and K-12 vendors facing fragmented state law.
**Region:** North America.

```
virtualryder/edu-ai-agents (MIT)        — governance spine: deny-by-default authz,
                                          student-PII masking, human-in-the-loop enforcement,
                                          tamper-evident audit (FERPA/COPPA/IDEA-504/ADA)
  └── Ed-Fi-Alliance-OSS/Ed-Fi-ODS (Apache-2.0)  — the K-12 data standard across most US states
  └── Policy-config layer  (studio IP)  — per-state rules as data, not code
  └── Deterministic rubric scorer (NOT an LLM) — required by Oklahoma SB 1734
  └── openedx/edx-ora2 (AGPL-3.0) or ls1intum/Ares (MIT) — the grading workflow it feeds
  └── appsmithorg/appsmith (Apache-2.0) — teacher review and override console
  └── yetanalytics/lrsql (Apache-2.0)   — audit + parent-disclosure record
```

**Wiring.** The critical design decision is that **grading scores come from a deterministic
rubric service and the LLM only drafts narrative feedback**, which a teacher approves. That
single split satisfies Oklahoma's prohibition on AI-only grading, Idaho's bar on AI replacing
teachers, and the teacher-review mandates generally — and `virtualryder/edu-ai-agents` is
already built that way, which is why it is the spine rather than a reference.

Model each state's rules as configuration: *AI-only grading permitted (no)*, *parent opt-out
required*, *minimum grade for direct student AI use* (New York A 9190 would set grade 9),
*district framework deadline* (Ohio: 1 July 2026). A district crossing state lines flips a
config value, not a code path. This layer is the defensible studio asset.

**Result licence:** permissive apart from the `edx-ora2` option — prefer `Ares` (MIT) for a
closed derivative.
**Estimate:** 10–12 weeks for the spine plus three states; ~1 week per additional state.

---

## P4 — EMEA AI Act conformity-by-construction (admissions / assessment / proctoring)

**For:** EU institutions and edtech vendors with a hard 2 December 2027 date.
**Region:** EMEA.

```
Classify first: is the system Annex III high-risk?
  admissions · assessment & learning-outcome determination ·
  educational-level assignment · exam monitoring   → YES, obligations from 2026/1744: 2 Dec 2027
  Already banned (since Feb 2025): emotion recognition in schools — do not build it
  Already in force (Aug 2026): Article 50 — tell the student they are talking to an AI

Sovereign-by-default stack (EUA Jan 2026 favours European LLMs):
  ollama (MIT) / vllm-project/vllm (Apache-2.0)   — inference inside the institution
  BerriAI/litellm (MIT)                           — gateway; NO US-hosted API in the data path
  qdrant/qdrant (Apache-2.0)                      — vector store, self-hosted
  ls1intum/Artemis + edutelligence + Pyris (MIT)  — EU-origin, permissive platform tier
  temporalio/temporal (MIT)                       — durable runs; execution history IS the log
  yetanalytics/lrsql (Apache-2.0)                 — xAPI evidence of human oversight
  langchain-ai/langgraph (MIT)                    — oversight + disclosure as explicit nodes
  promptfoo (MIT) + AI-for-Education/pedagogy-benchmark (MIT)  — versioned eval evidence
```

**Wiring.** Three things make conformity cheap later: Article 50 disclosure as a non-bypassable
node (not a UI string), Temporal's execution history as your immutable audit record, and
`promptfoo` running `pedagogy-benchmark` in CI so you can show *when* behaviour changed and
that you tested it. Deliver the Annex III classification memo as the first artefact — it scopes
everything else and is billable on its own.

**Caveat to state to the client in writing:** confirm the 2 December 2027 date against the
Regulation (EU) 2026/1744 text. Many published sources still carry the superseded 2 August 2026
date, and this is the most commonly mis-stated fact in the sector.

**Result licence:** fully permissive, self-hostable, no US data path.
**Estimate:** 4 weeks for classification + documentation; 12–14 weeks for the governed build.

---

## P5 — LATAM governance-and-enablement retrofit (the 53/22 gap)

**For:** institutions already using AI without guidelines — 53% of Brazilian administrators use
AI, 22% have policies; 87% of regional universities use AI, 26% have a strategy.
**Region:** LATAM.

```
Week 1–2  Discovery: what AI is already in use, by whom, on what student data
Week 2–4  Policy pack: acceptable-use, disclosure, assessment-integrity, data handling
             (anchor to Brazil PL 2338/2023's pending obligations — it covers education)
Week 3–6  Technical retrofit, not replacement:
             BerriAI/litellm (MIT)         — put every existing AI call behind one gateway,
                                             with per-department budget caps and full logging
             yetanalytics/lrsql (Apache-2.0) — xAPI record of AI use (the missing evidence)
             appsmithorg/appsmith (Apache-2.0) — teacher disclosure + override console
             openfun/ralph (MIT)           — alternative LRS if Python/French-stack preferred
Week 4–8  Teacher enablement (the real deliverable; TALIS says they already use AI)
             patchy631/ai-engineering-hub (MIT) — staff upskilling material
Ongoing   Portuguese/Spanish pedagogical localisation of an APAC/EMEA-origin tutor:
             HKUDS/DeepTutor (Apache-2.0) or THU-MAIC/OpenMAIC (MIT)
Public sector (Brazil):
             portabilis/i-educar (LGPL)    — SIS built around Brazilian regulatory requirements
Low-connectivity:
             learningequality/kolibri (MIT) + iiab/iiab (LGPL) + ollama (MIT) — fully offline tutor
```

**Wiring.** The `litellm` gateway is the highest-leverage single move: it converts "AI is
happening somewhere in our institution" into a metered, logged, budgeted channel in days,
without asking anyone to stop what they are doing. Everything else builds on that visibility.

**Why localisation rather than build:** there is effectively no LATAM-origin open education
agent (only `warleysr/ankipa`, an Anki add-on). Localising DeepTutor or OpenMAIC is faster and
the pedagogical localisation is itself the billable differentiation.

**Estimate:** 6–8 weeks.

---

## P6 — APAC multi-jurisdiction deployment with content provenance

**For:** regional edtech or a multinational operating across Korea, China, India and Japan.
**Region:** APAC.

```
langchain-ai/langgraph (MIT)  — one graph, per-jurisdiction policy nodes:
    VN  → Law on AI 134/2025/QH15 + Decree 142 + Decision 33/2026/QD-TTg (eff. 15 Aug 2026):
          EDUCATION IS STATUTORY HIGH-RISK (3 of 46 listed systems — behavioural monitoring,
          learner ranking, automated assessment). Existing systems: comply by 1 Sep 2027.
          New systems: 1 Mar 2027. Notification to MOST; registration can be refused.
          *** Build this node FIRST: it is the earliest statutory deadline in the region. ***
    KR  → AI Basic Act (in force 22 Jan 2026): risk classification + oversight duties.
          2026 is a guidance-first grace period; decrees still being finalised.
    CN  → service-type rules + AI-content labelling; Cybersecurity Law AI clause (1 Jan 2026)
    IN  → IT Rules: prominent labels + provenance markers on generated content (20 Feb 2026)
    AU  → no AI statute, but TEQSA moved to a REGULATORY-LED posture in 2026 and inspects the
          genAI action plan the provider already filed (all 203 providers, 2024, 100% response).
          The client's own action plan is the requirements document — read it before scoping.
          Binding layer: Higher Education Standards Framework (Threshold Standards).
          Schools: Australian Framework for Generative AI in Schools + state additions.
    JP  → promotion-first + voluntary guidelines, NO education-specific statute (confirmed
          absence, p890) → lowest-friction pilot geography

Provenance emitted at generation time (NOT retrofitted):
    every generated item carries model, version, prompt hash, timestamp, generator identity
    yetanalytics/lrsql (Apache-2.0) — provenance + interaction record
    temporalio/temporal (MIT)       — reproducible generation runs

Content pipeline tuned for the region:
    opendatalab/MinerU (Apache-2.0)   — CJK textbooks and formulas; beats Western-trained parsers
    SYSTRAN/faster-whisper (MIT)      — multilingual lecture transcription

Tutor core (APAC-origin, permissive — partner, don't rebuild):
    HKUDS/DeepTutor (Apache-2.0)      — agentic personalised tutoring, HKU
    THU-MAIC/OpenMAIC (MIT)           — multi-agent classroom, Tsinghua, v1.4.2 (2026-11-09)
    netless-io/flat (MIT)             — interactive classroom with whiteboard
```

**Wiring.** Labelling is a dated legal requirement in two of the four markets, so provenance
metadata is emitted by the generator and stored with the artefact — retrofitting labels across
an existing content library is the expensive path. `MinerU` is the specific reason this pattern
differs from P2: CJK textbook extraction quality determines whether the whole RAG tier works.

**Mandatory non-technical workstream.** Korea attempted a national AI-digital-textbook rollout
from 2025 and reduced it to optional status within a year after teacher and parent backlash.
Budget a named teacher- and parent-consent workstream. **Cite Korea when a client wants to skip
it** — the failure was social, not technical, and it is the cheapest lesson available.

**Sequencing added in p890.** Vietnam's clock (1 March 2027 for new systems) expires **before**
the EU's 2 December 2027, so an Annex-III-grade oversight architecture built for EMEA should be
*reused* here rather than rebuilt — and it is needed sooner. Australia inverts the usual sales
motion: the provider has already written and filed a genAI plan and is now being held to it, so
the engagement is implementation of an existing commitment, not persuasion.

**Estimate:** 12–14 weeks for two jurisdictions; ~3 weeks per additional jurisdiction. Add
~2 weeks for the Vietnam node (the high-risk list is closed and specific, so classification is
quick, but notification and registration are procedural).

---

## P7 — Evidence-of-efficacy tier (attach to any of the above)

**For:** any engagement that will face a procurement office or regulator asking "did it work?"
**Region:** Global.

```
yetanalytics/lrsql (Apache-2.0)                     — xAPI statements for every interaction
  └── openfun/ralph (MIT)                           — alternative LRS (Python stack)
AI-for-Education/pedagogy-benchmark (MIT)           — pedagogical ability, not subject knowledge
EleutherAI/lm-evaluation-harness (MIT)              — subject-knowledge benchmarks, extensible
promptfoo/promptfoo (MIT)                           — CI regression gates on prompts/models
HumanSignal/label-studio (Apache-2.0)               — rubric calibration, grading gold sets
argilla-io/argilla (Apache-2.0)                     — teacher feedback collection and curation
open-spaced-repetition/fsrs4anki (MIT)              — evidence-backed review scheduling,
                                                      instead of an invented schedule
```

**Wiring.** Build the gold set with teachers in `label-studio` *before* the tutor ships; it is
both the eval baseline and the rubric-calibration artefact. Wire `promptfoo` into CI so a model
or prompt change that regresses pedagogy fails the build. Use `fsrs4anki`'s FSRS scheduler
rather than having an agent invent review intervals — there is real evidence behind it.

**Why this pattern exists.** No credible primary evidence of learning gains from AI at scale
was found in this pass; the widely quoted "42% improvement" style figures trace to blogs with
no primary study. Almost no vendor ships a measurement tier, every regulator is converging on
demanding one, and a client who can answer the question has something their competitors cannot
buy.

**Estimate:** 3–4 weeks, and it makes every other pattern defensible.

---

## P8 — Per-institution AI metering, cost attribution and exit (the Jisc specification)

**For:** any institutional engagement in the UK, and increasingly anywhere a procurement office
reviews an AI contract. **Region:** EMEA primarily; the architecture is Global.
**New in pass p890.**

**Why this pattern exists.** Jisc, with Universities UK, GuildHE and the Association of
Colleges, published what is effectively a buyer-side specification: transparent pricing,
demonstrable value, meaningful institutional choice, protection of existing functionality,
**granular usage and cost controls**, interoperability, **data portability** and safeguards
against **vendor lock-in**. The trigger is usage-based pricing replacing per-seat licences, and
institutions paying several times over for overlapping AI embedded in different platforms. A
companion Jisc/EAUC report found vendors seldom publish institution-level usage at all. Every
other pattern in this file answers a regulator; **this one answers the person who signs the
cheque**, and they have written the requirements down.

```
Request path — attribution is established before inference, not inferred afterwards:

  apereo/cas (Apache-2.0)            — SSO; the identity that carries
                                       institution / faculty / course / role claims
    └── Cvmcosta/ltijs (Apache-2.0)  — LTI 1.3 launch; course + role context from the LMS,
                                       so the tool detaches from any one platform
        └── BerriAI/litellm (MIT)    — gateway: ONE virtual key per cost centre
                                       (institution → faculty → course), hard budget caps,
                                       provider-agnostic so the model layer stays swappable
            ├── ollama/ollama (MIT)  — local inference: the zero-marginal-cost tier
            ├── vllm-project/vllm (Apache-2.0) — self-hosted at throughput
            └── hosted API           — the exception, and now a visibly priced one

Metering and export — OpenTelemetry, because OTel IS the portability answer:

  traceloop/openllmetry (Apache-2.0, 7,541★)  — PREFERRED. OTel-native LLM tracing: the
                                                usage data lands in the observability stack
                                                the institution already runs. Nothing to
                                                migrate on exit because nothing was captive.
  openlit/openlit (Apache-2.0, 3,088★)        — OTel-native alternative with cost tracking
  Helicone/helicone (Apache-2.0, 6,287★)      — gateway-level logging and cost attribution
  (langfuse/langfuse, 37,577★ — LARGEST BUT SPLIT LICENCE: "MIT Expat" core, separate
   enterprise licence on ee/, web/src/ee/, worker/src/ee/, packages/shared/src/server/ee/;
   copyright now ClickHouse, Inc. Diligence before it enters a client deliverable.)

Evidence that the spend bought something:

  yetanalytics/lrsql (Apache-2.0)             — xAPI: usage joined to learning interactions,
                                                which is how "demonstrable value" stops being
                                                a slide and becomes a query
  qdrant/qdrant (Apache-2.0)                  — embeddings in a store the CLIENT owns
```

**Wiring.**

1. **Mint one `litellm` virtual key per cost centre, not per application.** Attribution has to
   exist at request time; a report that infers which faculty spent what is the thing the Jisc
   statement is complaining about.
2. **Carry institution/faculty/course/role from CAS and the LTI 1.3 launch into the gateway
   key** — the LMS already knows the context, so do not rebuild a hierarchy beside it.
3. **Emit OTel spans, not vendor events.** This is the single decision that satisfies data
   portability: the institution can point the exporter at its own collector on day one, and
   nothing has to be extracted on exit.
4. **Set hard caps, not alerts.** Usage-based pricing without a ceiling is the exposure; a
   budget cap that returns a graceful degradation (local `ollama` model instead of a hosted
   call) keeps the service up while the cost stays bounded.
5. **Write the exit into the build:** documented export of usage data, embeddings, prompts and
   content, plus an LTI 1.3 integration that the client can repoint at another tool. Deliver it
   as a runbook, because an untested exit is not an exit.
6. **Price per learner-outcome, not per token.** The buyer has stated publicly they will not
   sign per-token exposure.

**What makes this defensible.** None of the four metering repos is built for education: they
know about users and projects, not institutions, faculties, courses and cohorts. **Mapping an
OTel LLM-metering layer onto an academic hierarchy, with LTI-derived context and per-cost-centre
budget enforcement, is genuine studio IP** — it answers a published, signed, sector-wide
requirement, and no vendor currently ships it.

**Caveat.** The Jisc statement is a request to suppliers, not a regulation. It carries no
penalty. Its force is commercial: it is signed by the bodies representing most of UK higher and
further education, and it tells you precisely what a tender will ask.

**Estimate:** 5–7 weeks on top of an existing AI tier; ~9 weeks standalone. The exit runbook
and the per-cost-centre hierarchy are the long poles, not the tracing.

---

## P9 — Integrity by assessment redesign, not detection

**For:** any higher-education or senior-secondary client currently buying, piloting or being
pressured to buy AI-detection tooling.
**Region:** Global. Strongest fit **North America (Canada especially)** and **EMEA**; also the
compliant answer to the **UAE** exam-context prohibition.
**Added:** p891. Evidence behind it: **T10** in `intel/trends.md`.

### Why this pattern exists

Detection is being removed as a control by institutional counsel, not by faculty. All six
Canadian universities in a 2026 review declined to enable or endorse AI detection, privacy
cited at four; Concordia bars staff from using online detectors outright; UBC cites a Privacy
Impact Assessment. Sending student work to a third-party detector is a disclosure event under
FOIPPA/FIPPA, GDPR, and the US state student-data statutes — **California AB 1159 bars using
student data to train AI models at all**. Meanwhile the EU Council's October 2026 conclusions
ask member states for **academic-integrity policies**, and the UAE's classroom guide bans AI
**during exams and assessments**. Every regional signal asks for a *process control*. None asks
for a *classifier*.

**Sell this as the replacement for a detection line item that is about to be cancelled.**

### Stack

```
Incumbent LMS (Moodle GPL-3.0 / Canvas AGPL-3.0 / Open edX AGPL-3.0)
  │   integrate over LTI 1.3 — never fork; keeps your work a separate work
  ├── ls1intum/Artemis (MIT) ................ where a permissive core is available:
  │     └── ls1intum/edutelligence (MIT) .... already-integrated AI tier
  │                                           exercise + rubric model to copy
  ├── Submission-process instrumentation ..... draft history, revision timeline,
  │     (LMS-native: Moodle assign plugin /    time-on-task — product evidence
  │      Canvas submission API via            replaced by process evidence
  │      vishalsachdev/canvas-mcp, MIT)
  ├── openedx/edx-ora2 (AGPL-3.0) ........... open-response + peer/self/staff grading;
  │                                           the seam for structured oral defence
  ├── CAHLR/OATutor (MIT) ................... A/B-testable tutoring instrumentation —
  │                                           use it to prove the redesign worked
  ├── langchain-ai/langgraph (MIT) .......... rubric-reasoning agent as explicit,
  │                                           auditable policy nodes (not a verdict)
  ├── AI-for-Education/pedagogy-benchmark (MIT)  eval gate before anything touches a cohort
  └── ollama (MIT) / vllm-project/vllm (Apache-2.0) + BerriAI/litellm (MIT*)
        *litellm is MIT outside `litellm/enterprise/`; that directory is separately
         licensed. Use the OSS paths — see repos/foundations.md.
        └── student work never leaves the institution — this is what makes the PIA pass
```

### The design rule that makes it defensible

**No component emits a judgement about whether a student used AI.** The agent tier grades
*reasoning against a rubric* and surfaces *process artefacts* to a human marker. The integrity
finding is always made by a person, from evidence the student can see and contest. That is what
survives a privacy review, an appeal, and EU AI Act Article 14 human-oversight design — which
is deferred to **2 December 2027** but is the standard the architecture should already meet.

### Deliverables

1. **Assessment-redesign programme** — rubrics that grade reasoning, drafts and version history
   as graded artefacts, supervised in-class components, oral defence for a sampled subset.
2. **Process-evidence instrumentation** in the incumbent LMS, over LTI 1.3.
3. **Privacy artefact** — PIA, vendor-assessment template, data-flow diagram showing inference
   is local. In Canada this is the document that unlocks procurement.
4. **Appeals runbook** — how a contested finding is reviewed, by whom, on what evidence.
5. **Efficacy measurement** — attach **P7**; OATutor's instrumentation is the cheapest route to
   a defensible before/after.

### Licence posture

Clean. Everything load-bearing is MIT/Apache-2.0 and reached over LTI 1.3, so a GPL/AGPL
incumbent LMS stays a separate work. `edx-ora2` is AGPL — use it **in place** inside an existing
Open edX deployment, do not vendor it into a proprietary derivative.

### Estimate

**8–11 weeks.** Assessment redesign with faculty is the long pole, not the engineering —
budget roughly 40% of the effort for workshops and rubric development, and expect the
privacy artefact to gate go-live in Canada and EMEA. A detection-replacement framing shortens
the sales cycle considerably, because the budget already exists.

### Where it does not apply

Where a regulator has mandated proctoring or automated assessment outright — **Vietnam**, where
automated assessment is statutorily high-risk under Decision 33/2026/QD-TTg with an 18-month
education transition. There the engagement is **P6** plus conformity work, not this pattern.

## P10 — National curriculum-mandate delivery: teacher enablement at system scale

**New in pass p892.** Written once for **India** and **Saudi Arabia** because the two
engagements are the same build with the curriculum corpus and the language swapped. Also fits
Vietnam's 12-periods-per-year mandate and, with the student tier removed, the EU Article 4
staff-literacy duty.

### Why this pattern exists

Every other pattern in this file answers a constraint on AI *use*. This one answers a state
mandate to *teach* AI, which T11 establishes across India, Saudi Arabia, Vietnam, the UAE,
North Carolina and the African Union strategy. The distinguishing facts:

- **The curriculum already exists and the client owns it.** NCERT/CBSE in India; the National
  Curriculum Center in Saudi Arabia. **Do not author courseware.** Authoring it is both out of
  scope and politically unwinnable.
- **The constraint is teacher capacity, stated explicitly by the buyers** — 240,000 teachers in
  training in KSA (60,000 reached), and India's own commentary that adding a subject is not the
  same as preparing teachers to teach it.
- **The buyer is a ministry or board**, so evidence of coverage is a contractual artefact, not
  a nice-to-have.

### Stack

Every repo named is verified in this KB with licence and last-push date.

**1. Curriculum ingestion — the client's own documents, never a generic corpus**

| Component | Repo | Licence |
|---|---|---|
| PDF/DOCX curriculum → structured text | `docling-project/docling` | MIT |
| Heavier layout/formula extraction | `opendatalab/MinerU` | Apache-2.0 (SPDX NOASSERTION) |
| Retrieval over the ingested curriculum | `HKUDS/LightRAG` or `infiniflow/ragflow` | MIT / Apache-2.0 |
| Vector store the client owns | `qdrant/qdrant` | Apache-2.0 |

**2. Model layer — swappable, because sovereignty differs by market**

| Component | Repo | Licence |
|---|---|---|
| Gateway, per-district keys and budget caps | `BerriAI/litellm` | **MIT except `litellm/enterprise/` — do not vendor that path** |
| Local/self-hosted inference | `ollama/ollama` · `vllm-project/vllm` | MIT / Apache-2.0 |

Keep the gateway even if the first deployment calls a hosted API. It is what lets the Saudi
build answer a national-AI-company requirement and the Indian build answer a data-residency
one without re-architecture (T6).

**3. Teacher-facing generation — the actual deliverable**

| Component | Repo | Licence |
|---|---|---|
| Lesson/slide/quiz generation from curriculum | `THU-MAIC/OpenMAIC` | MIT |
| Local-first lesson-prep design reference | `SirhanMacx/Claw-ED` | MIT — **read it, do not pin it** (last push 2026-09-19) |
| Exercise/item rendering | `Khan/perseus` | MIT |
| Orchestration with explicit policy nodes | `langchain-ai/langgraph` | MIT |
| Durable long-running enrolment/cohort workflows | `temporalio/temporal` | MIT |

**4. Delivery and reach**

| Component | Repo | Licence |
|---|---|---|
| Training delivery to teachers | `oppia/oppia` (Apache-2.0) if greenfield; integrate to the client's LMS over **LTI 1.3** with `Cvmcosta/ltijs` (Apache-2.0) if not | Apache-2.0 |
| Low-bandwidth / offline cohorts | `learningequality/kolibri` | MIT |
| Admin and cohort-tracking console | `appsmithorg/appsmith` | Apache-2.0 |

**5. Evidence — the part that gets the contract renewed**

| Component | Repo | Licence |
|---|---|---|
| Pedagogical-quality eval gate on generated material | `AI-for-Education/pedagogy-benchmark` | MIT |
| Per-district/per-cohort usage and cost attribution, OTel-native | `traceloop/openllmetry` | Apache-2.0 |

### How it wires together

1. Ingest the ministry's curriculum with `docling` → chunk → embed → `qdrant`. **This corpus is
   the only authority the generation tier may cite.**
2. `langgraph` runs the generation flow with the policy checks as explicit nodes: grade-band
   check, curriculum-citation check, provenance-label emission, language check. Explicit nodes
   are what make the flow auditable to a ministry.
3. `litellm` fronts every model call, keyed per district so cost attribution exists from day one.
4. `OpenMAIC` generates the teacher's lesson, slides and quiz items; `perseus` renders items.
5. `pedagogy-benchmark` gates output on pedagogical quality before a teacher ever sees it.
6. Delivery through `oppia`, or into the client's existing LMS over LTI 1.3 via `ltijs`;
   `kolibri` carries the offline cohorts.
7. `openllmetry` emits coverage and cost per district into whatever observability stack the
   ministry already runs — which is also the portability answer (T9).

### The design rules that make it defensible

- **Retrieval over the ministry's curriculum, never training on it, and never on student or
  teacher data.** California AB 1159 forecloses the training architecture outright; building
  the no-training version once makes the same stack sellable in every market.
- **Emit provenance labels at generation time.** India's amended IT Rules require prominent
  labels and provenance markers on AI-generated content from **20 February 2026** (T7).
  Retrofitting a national content library is the expensive path.
- **Grade-banding is a policy node, not a prompt.** India's mandate is Classes III–VIII; the
  UAE prohibits under-13 and below-Grade-7 use entirely. The same deployment must be able to
  answer both, and a prompt instruction is not an answer a regulator accepts.
- **Teacher-in-the-loop is the product.** Generated material is a draft a teacher edits and
  approves, and the approval is logged. This is T1's oversight requirement and also the only
  posture that survives T8's consent problem.

### Deliverables

1. Curriculum-grounded lesson-preparation service, grade-banded, provenance-labelled.
2. Teacher training-delivery tier with per-cohort completion evidence.
3. Coverage and cost dashboard by district, exportable (the ministry's reporting obligation).
4. Policy-node configuration per jurisdiction — grade bands, prohibitions, labelling.
5. Evaluation report from `pedagogy-benchmark` on generated material, as an acceptance gate.

### Licence posture

Clean. Every component is MIT or Apache-2.0 except the carve-out in `litellm/enterprise/` (do
not vendor it) and `kolibri`'s MIT core, which is fine. **If the client's LMS is Moodle
(GPL-3.0) or Canvas (AGPL-3.0), integrate over LTI 1.3 and the deliverable stays a separate
work** — the single most important licence decision in this pattern (see `README.md`, fact 1).

### Estimate

**14–18 weeks** to a first district or regional cohort: 3–4 weeks curriculum ingestion and
retrieval quality, 4–5 weeks generation tier and policy nodes, 3–4 weeks delivery integration,
2–3 weeks evidence tier, 2 weeks evaluation and acceptance. Longer than every other pattern
here because the buyer is public-sector and acceptance is formal.

### Where it does not apply

- **Not for institutional self-service markets.** If the buyer is a single university, this is
  P2 or P8, not P10.
- **Not where no mandate exists.** Without a funded state programme this becomes speculative
  courseware, which is a product business and not a services engagement.
- **Not as a route to selling a student tutor.** The mandate is teacher capacity (T11). A
  student-facing tutor sold against it is the wrong deliverable, and every open tutor this KB
  tracks is English- or Chinese-first — in India and Saudi Arabia that is a localisation
  project, not a dependency.


## P11 — Read-only-first Moodle agent tier over MCP (added p893)

### Why this pattern exists

P2 already covers putting a governed AI tier over an existing Moodle or Canvas **without
forking it**, and it does so over LTI 1.3. p893 established that a second seam now exists and is
better suited to agents: **MCP** (see **T13**). LTI ships your tool *into* the LMS; MCP exposes
the LMS *to* your agent. P11 is the MCP half, and it exists as its own pattern because of one
property the LTI route does not have — **the community has already split read and write across
two separately-maintained MIT servers**, which makes a genuinely read-only pilot a
configuration choice rather than a promise.

Use this when the client runs Moodle (the most-installed LMS on earth), wants agent access to
real coursework, and has a data-protection function that will not approve write access to a
gradebook on day one. Which is most of them.

### Stack

Every repo named is API-verified and licence byte-read in this KB as at 2026-11-18.

**1. The LMS tool surface — staged by access posture**

| Stage | Component | Repo | Licence | ★ |
|---|---|---|---|---|
| Pilot | **Read-only** Moodle MCP — courses, assignments, quizzes, deadlines, files | `Faixiang/Moodle-MCP` | MIT | 208 |
| Pilot | Companion agent skill: diff new coursework, list unsubmitted work | `Faixiang/Moodle-Course-Watch` | MIT | 0 |
| Graduation | **Read-write** Moodle MCP — forums, grades, files-as-markdown | `G36maid/moodle-mcp` | MIT | 30 |
| Graduation (alt) | Write path with explicit idempotency guarantees | `MarcosNahuel/moodle-mcp` | MIT | 1 |
| Open edX variant | Staff/superuser admin facade (Ulmo) + Tutor plugin | `blend-ed/openedx-mcp` · `blend-ed/tutor-contrib-openedxmcp` | AGPL-3.0 | 3 · 2 |

**Do not use** `loyaniu/moodle-mcp` (58 ★) or `onbirdev/moodle-webservice_mcp` (19 ★): both
were licence-checked this pass and **have no licence file**, which means all rights reserved
regardless of how they are described elsewhere.

**2. The agent tier — unchanged from P2, reused deliberately**

| Component | Repo | Licence |
|---|---|---|
| Auditable orchestration — policy checks as explicit graph nodes | `langchain-ai/langgraph` | MIT |
| Gateway, per-institution keys, budget caps, model portability | `BerriAI/litellm` | **MIT except `litellm/enterprise/`** |
| Local / sovereign inference | `ollama/ollama` · `vllm-project/vllm` | MIT / Apache-2.0 |
| Retrieval over course material the institution owns | `qdrant/qdrant` | Apache-2.0 |

**3. The user-facing surface — still LTI, not MCP**

| Component | Repo | Licence |
|---|---|---|
| LTI 1.3 / Advantage tool provider | `Cvmcosta/ltijs` | Apache-2.0 |

MCP is how the agent reads the LMS. LTI is how the learner reaches the agent inside the LMS.
A serious build uses both; using MCP for the user surface means rebuilding auth and launch
context the LTI spec already solved.

**4. The evaluation gate — non-optional**

| Component | Repo | Licence |
|---|---|---|
| Pedagogical-ability benchmark | `AI-for-Education/pedagogy-benchmark` | MIT |
| Prompt/LLM regression testing in CI | `promptfoo/promptfoo` | MIT |

### How it wires together

1. Stand up `Faixiang/Moodle-MCP` against a **non-production Moodle clone** with a scoped
   service token. Read-only by construction, so the first conversation with the client's DPO is
   about token scope, not about what the agent might overwrite.
2. Put LangGraph in front of it. Every tool call the agent makes to the LMS passes a policy
   node — which courses, which fields, whose data — and that node writes an audit record. This
   is the part that is reusable when the client's regime changes; keep policy in configuration.
3. Expose the learner-facing surface through `ltijs` so launch, identity and course context come
   from the LTI launch rather than being reimplemented.
4. Gate every release on `promptfoo` suites plus `pedagogy-benchmark`. A tutor that regresses
   pedagogically but passes unit tests will ship otherwise.
5. **Graduate to write scope as a separate, documented decision** — swap in `G36maid/moodle-mcp`
   behind the same policy nodes. The audit trail from the read-only phase is the evidence that
   makes that approval obtainable.

### The design rules that make it defensible

- **Scope the token, not the prompt.** These servers typically run with the operator's own API
  token, so the agent inherits every permission that human has. A prompt instruction not to
  touch grades is not a control. A token without the grade capability is.
- **Read-only is a deployment artefact, not a claim.** The reason to use two separate servers
  rather than one with a flag is that a flag is a configuration error away from being wrong,
  and a server with no write code is not.
- **Keep the agent out of the gradebook of record for as long as possible.** Under the EU AI
  Act, assessment is Annex III high-risk from **2 December 2027**; under Oklahoma's rule AI-only
  grading is already barred; California AB 1159 forecloses training on student data entirely.
  Reading coursework to help a learner is a different regulatory object from writing a grade.
- **Pin versions.** Five of the seven Moodle MCP servers were created in the last six months and
  the ecosystem is unconsolidated. Vendor the one you choose.

### Deliverables

- A read-only Moodle agent tier running against the client's own course data, with a policy
  node per tool call and a complete audit log.
- A token-scoping specification and a DPO-facing note explaining why read-only is structural.
- Eval suites wired into CI with a recorded pre-deployment baseline.
- A written graduation plan to write scope, with the evidence requirements named up front.

### Licence posture

Clean. The Moodle servers, `ltijs`, LangGraph, Qdrant and both eval tools are MIT or
Apache-2.0, and nothing here forks Moodle — so Moodle's GPL-3.0 stays on Moodle's side of the
boundary and the client's tier can be closed. **Two exceptions to state explicitly:** the
Open edX variant is **AGPL-3.0** and is vendor-maintained rather than foundation-maintained, and
`litellm/enterprise/` must not be vendored.

### Estimate

**5–7 weeks** to a read-only pilot on a Moodle clone with policy nodes, audit and eval gates.
Add **3–4 weeks** for the graduation to write scope, most of it approval rather than code.

### Where it does not apply

- **Not on Canvas** — use `vishalsachdev/canvas-mcp` (MIT, read-write) or `boyuchengz/canvas-mcp`
  (MIT, read-only) in the same shape; the pattern transfers, the repos do not.
- **Not where the client wants a closed derivative of the platform itself.** That is Mentingo
  (MIT) or Artemis (MIT) and pattern **P1**, not an integration over somebody else's GPL core.
- **Not as a shortcut past LTI.** If the deliverable is a learner-facing tool inside the LMS,
  MCP alone will cost more than it saves.
- **Not where Moodle HQ support is a procurement requirement.** Moodle HQ has published no MCP
  server; every option here is community-maintained, and that must be said before signature.

## P12 — Registrarial agent tier over UniTime (the KB's named gap, scoped to what is actually missing)

### Why this pattern exists

Every pass of this KB has named the registrarial layer — enrolment, timetabling, transcripts,
financial aid — as the industry's clearest build-vs-adopt gap and the most defensible studio IP.
**p894 found that the gap was half misread**, and the half that was wrong changes the estimate by
months. The *agent* tier genuinely does not exist: a dedicated leg found only course capstones
(`aabbiisshhaa/student-support-agent`, 2 ★, no licence, Makerere University;
`vaibhav9895-lang/student-support-agent-assignment`, 0 ★, no licence;
`leechenwei/Ai-Agent-Timetable`, 0 ★, no licence, idle since 2025-02-24). But the **platform
underneath it exists, is permissive and was pushed yesterday** — `UniTime/unitime`, Apache-2.0,
360 ★, 2026-11-17 — and it had fallen out of `verticals/solutions.md` in the 2026-11-18 rewrite.

So this is not "write a registrarial platform". It is **"put an agent and a decisioning tier over
a maintained Apache-2.0 scheduler, and build only the parts that have nothing"** — which is a
10-week engagement rather than a multi-year product.

Use this where a university client has a timetabling or exam-scheduling pain, a registrar who
spends their week on conflict resolution and exception requests, and an SIS of record that is
not going to be replaced.

### Stack

Every repo named is API-measured and licence byte-read in this KB as at 2026-11-18.

**1. The registrarial core — adopt, do not build**

| Component | Repo | Licence | ★ | Note |
|---|---|---|---|---|
| Course and exam timetabling, student scheduling | `UniTime/unitime` | **Apache-2.0** | 360 | Pushed 2026-11-17. Runs standalone or interfaces to an existing SIS |
| The constraint solver underneath it | `UniTime/cpsolver` | **LGPL-3.0** | 84 | **Licence boundary — see below.** Do not static-link into a closed component |
| Small-scale permissive alternative | `GEOSOFT-GLOBAL/timetablely` | MIT | 27 | Idle since 2026-08-17; a starting point, not a dependency |
| SIS of record (LATAM public sector) | `portabilis/i-educar` | GPL-2.0 | — | Built around Brazilian regulatory requirements |
| K-12 SIS where a closed derivative is required | `Gego-K12/gegok12` | MIT | — | The only MIT-licensed SIS this KB has verified |

**2. The agent tier — this is the part you build**

| Component | Repo | Licence | Role |
|---|---|---|---|
| Orchestration with auditable policy nodes | `langchain-ai/langgraph` | MIT | Every eligibility and exception check is an explicit node, not a prompt instruction |
| Role split: registrar / scheduler / adviser / reviewer | `crewAIInc/crewAI` | MIT | Optional; use where the workflow genuinely has four hand-offs |
| K-12 data standard (North America) | `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | Apache-2.0 | Non-negotiable for a US K-12 engagement |
| SSO and per-role access to the agent tier | `apereo/cas` | Apache-2.0 | Same foundation as UniTime; already in most higher-ed estates |
| Human review queue | `appsmithorg/appsmith` | Apache-2.0 | What makes human-in-the-loop real instead of aspirational |
| Evidence that it helped | `yetanalytics/lrsql` + `agentscope-ai/OpenJudge` | Apache-2.0 both | Decision-quality and turnaround-time measurement; see **P7** |

### How it wires together

1. **UniTime stays the system of record for schedules.** The agent never writes a timetable
   directly; it proposes, and UniTime's solver validates. This is the single most important
   decision in the pattern — it keeps feasibility guarantees in the component that has them.
2. **Exception intake is the agent's first job, not scheduling.** Room-change requests, clash
   appeals, accommodation-driven constraints and late enrolment arrive as free text; the agent
   normalises them into UniTime constraints and explains what it changed.
3. **Eligibility and decisioning are policy nodes, deterministic, with the LLM confined to
   evidence extraction.** This is the one design rule the 0 ★ grading cohort got right
   (`Atmankhyar`, `timothyheeeee`, `virtualryder/edu-ai-agents`): the model reads documents and
   cites them, a rule engine decides.
4. **Every decision carries criterion-level evidence and a regrade path** — taken from
   `asu2304/auto-assessment-agent`. An appeal procedure is not a feature here; it is what makes
   the tier lawful in the EU.
5. **Accommodation constraints merge, never override.** From `SudhanvaJ-bit/project-samarth` via
   `P496-1`: the statutory accommodation baseline enters agent state such that the model **can
   add but cannot remove** a required accommodation. A scheduler that can drop an accessibility
   constraint is a Section 504 / ADA Title II incident, not a bug.
6. **Audit and metering per institution** as in **P8**, because this tier touches the registrar's
   authority and someone will ask who changed what.

### The design rules that make it defensible

- **Never let the agent make an admissions or financial-aid decision.** Those are **EU Annex III
  high-risk** and restricted under several US state laws. Scope the agent to *scheduling,
  exceptions and explanation*, and keep decisioning as an assisted human workflow with
  deterministic rules. This is the boundary that keeps a 10-week engagement out of a conformity
  assessment.
- **Honour the LGPL boundary on `cpsolver`.** UniTime is Apache-2.0 and its solver is LGPL-3.0.
  Keep the solver behind a process or service boundary; do not static-link it into a closed
  component. State this in the licence annex before signature.
- **Do not promise registrar-grade decisioning on day one.** Read-only proposal mode first, as
  in **P11** — the pattern that got the staged-access posture right.

### Deliverables

- UniTime deployed or integrated against the client's SIS of record, with the LGPL boundary
  documented.
- An exception-intake agent in proposal-only mode, with policy nodes, criterion-level evidence
  and an appeal path.
- Accommodation-merge enforcement (`P496-1`) with a test suite that proves a required
  accommodation cannot be dropped.
- A registrar review queue, an audit trail, and turnaround-time baselines before and after.
- A licence annex covering Apache-2.0 / LGPL-3.0 / the SIS licence, written for procurement.

### Licence posture

**Clean, with one named boundary.** UniTime, Ed-Fi, CAS, Appsmith, `lrsql` and OpenJudge are
Apache-2.0; LangGraph and CrewAI are MIT; nothing forks the SIS. **`cpsolver` is LGPL-3.0** and is
the only copyleft component — keep it at arm's length. Where the client's SIS is `i-educar`
(GPL-2.0) the SIS stays on its own side of the integration boundary; where a closed SIS
derivative is the requirement, `gegok12` (MIT) is the only verified permissive base.

### Estimate

**8–10 weeks** to a proposal-only exception agent over a UniTime instance with policy nodes,
accommodation-merge enforcement, audit and a registrar queue. Add **4–6 weeks** to extend to
write-through scheduling, most of it approval and regression testing rather than code. **Do not
quote decisioning** — that is a separate engagement with a conformity assessment in it.

### Where it does not apply

- **Not for admissions or financial-aid decisioning.** Annex III high-risk; different pattern,
  different estimate, legal review first.
- **Not where the client has no timetabling pain.** UniTime earns its keep on conflict-heavy
  estates (large programme catalogues, shared rooms, exam weeks). A small college does not need
  it and `timetablely` will not sustain an engagement.
- **Not in LATAM public K-12 without checking the SIS first.** `i-educar` is the substrate there
  and it is GPL-2.0; the integration boundary has to be designed before anything is promised.
- **Not as a replacement for the SIS of record.** Every registrar in this market has one, it is
  usually proprietary, and proposing to replace it will end the conversation.

## P13 — Persona-stateless tutor for age-banded, affect-regulated markets (China, UAE, US state statutes)

### Why this pattern exists

**Added p894, from T14.** Consumer tutoring products retain learners with affective design: a
persistent named character, rapport, streaks, companion framing. **Three separate regimes now
make that design a regulated activity when it is aimed at children**, and they converge on the
same architecture:

- **China** — the **Interim Measures for the Administration of Anthropomorphic AI Interaction
  Services** (reported as CAC Order No. 21, issued 10 April 2026, **in force 15 July 2026**)
  cover services providing *sustained emotional interaction through a simulated human
  personality*. **Education is listed outside scope, but conditionally** — one analysis frames
  the carve-out as covering education services *that lack continuous emotional interaction*, and
  the Measures define neither "continuity" nor "emotional interaction". Inside scope:
  **virtual-partner/virtual-relative services may not be offered to minors at all**, guardian
  consent under 14, a minor mode with time limits, a prohibition on inducing emotional
  dependence, machine disclosure, self-harm intervention, and algorithm filing.
- **UAE** — a 25-prohibition classroom guide including an **under-13 prohibition**.
- **United States** — New York's **A 9190** (classroom AI limited to grade 9 and above, with
  diagnostic and special-education exceptions), California's **AB 1159** (no training on student
  data), and Oklahoma's and Maryland's human-oversight rules.

**The architecture that keeps a product out of China's scope is the same architecture the other
two regimes require.** That makes this one build rather than three, which is the entire point of
the pattern.

### Stack

| Component | Repo | Licence | Role |
|---|---|---|---|
| Age-banded RAG tutor over curriculum, not student data | `Zenglian990/AI_Tutor_Release` | MIT | The reference: **age-banded by design** (K-9), retrieval-over-curriculum rather than training-on-learners |
| Learner-state modelling without a character | `amosblomqvist/learnharness` | **AGPL-3.0** | **Read it, do not ship it.** The persistent knowledge graph is the capability that replaces persona continuity. AGPL — reference design only |
| Authored teaching flow that constrains the model | `ai-shifu/ai-shifu` | Apache-2.0 | A script the author controls is the control structure "no AI-only instruction" rules actually require |
| Orchestration with policy nodes | `langchain-ai/langgraph` | MIT | Age band, disclosure and session-limit checks as explicit nodes |
| Local or sovereign inference | `ollama/ollama` · `vllm-project/vllm` | MIT · Apache-2.0 | Keeps learner text in-jurisdiction; see **T6** |
| Content provenance / labelling | see **P6** | — | China content labelling and India's IT-Rules duties |

### The design rules that make it defensible

1. **Persona-stateless.** No named character, no continuity of personality across sessions, no
   simulated affect. **Pedagogical persistence lives in the learner model** — mastery, gaps,
   next item — which is strictly more useful and carries none of the regulatory surface.
2. **Disclose the machine on every surface**, not once at onboarding.
3. **Age band by construction, not by setting.** The band gates features at the orchestration
   layer; a configuration flag is not a compliance control.
4. **No dependency loops.** No streaks, no "I missed you", no engagement mechanics tuned on
   session frequency. Tune on mastery per unit of time instead — which is also what **P7**
   measures.
5. **Guardian surfaces where the regime requires them** — consent under 14, time limits, risk
   alerts — built once and switched on per jurisdiction.
6. **Self-harm routing to a human**, unconditionally, in every market.

### Deliverables

A persona-stateless tutor over the client's curriculum corpus; an age-band gate with tests; a
disclosure and guardian-surface layer switchable per jurisdiction; a jurisdiction matrix mapping
each control to the instrument that requires it; and a design note recording what was
deliberately **not** built and why — the document that answers the client's growth team when
they ask for streaks.

### Licence posture

Clean if `learnharness` stays a reading. `AI_Tutor_Release`, LangGraph and Ollama are MIT;
`ai-shifu` and vLLM are Apache-2.0. **`learnharness` is AGPL-3.0: reference design only, never
vendored.**

### Estimate

**6–8 weeks** for the tutor plus the age-band and disclosure layer on an existing curriculum
corpus. Add **2–3 weeks** per additional jurisdiction for the control mapping and guardian
surfaces — mapping, not rebuilding, if rule 5 was honoured.

### Where it does not apply

- **Not for adult corporate L&D**, where none of these regimes applies and affective design is
  simply a product choice. Use Mentingo (MIT) and **P1**.
- **Not as a substitute for counsel on a China launch.** Every source behind T14 is secondary;
  the CAC text was not reachable from this session, and no source addressed a tutoring product
  specifically. **Confirm scope before signature.**
- **Not where the client's differentiator *is* the character.** This pattern removes it; say so
  before the engagement starts rather than in week six.

---

## P14 — Offline-first literacy delivery on an Africa-origin platform, with the agent tier as studio IP (added p895)

### Why this pattern exists

**Added p895, from T16 and the first dedicated Africa supply-side leg.** Every prior Africa
entry in this KB measured demand. The supply measurement changes the shape of the engagement:

- 🟢 **There is exactly one adoptable Africa-origin platform**, and it is permissive:
  https://github.com/elimu-ai/webapp — **MIT** (byte-read `main/LICENSE`, 1,065 B),
  **41 ★ / 67 forks**, created 2016, **pushed 2026-11-17**. Early-grade literacy for
  out-of-school children, Tanzania/Kenya.
- 🔴 **There is no adoptable agent layer.** The published Africa-origin tutor
  (ACL AfricaNLP 2026's EduNaija, https://github.com/Eddy-Emmanuel/EduNaija-LLM) has **no
  licence on any of 8 candidate paths**, 1 ★, idle since 2025-12-22. The national-exam channels
  return a **~1 ★ ceiling with almost nothing licensed**.
- **So the division of labour is forced, not chosen: adopt the platform, build the agent tier.**
  The agent tier is **defensible studio IP** here, which should be reflected in how the
  engagement is priced.

**The binding constraint is connectivity, and it is the reason the obvious design fails.**
EduNaija's grounding is a **Tavily web search behind an OpenAI call** — it cannot run where this
pattern deploys. Retrieval must be local and the model must be local.

### Stack

| Component | Repo | Licence | Role |
|---|---|---|---|
| Platform core (Africa-origin) | `elimu-ai/webapp` | **MIT** (1,065 B, byte-read) | Content + Android app hosting for early-grade literacy. Regional provenance that wins a public-sector procurement |
| App delivery with no network | `elimu-ai/appstore` | **MIT** | **Installs and updates APKs with no app store and no connectivity.** The hardest part of this pattern, already solved |
| Device-level learning path | `elimu-ai/launcher` | **MIT** | Android launcher enforcing an EGRA/EGMA literacy-and-numeracy path 🟡 *(claim unverified — licence and metadata only)* |
| Levelling + recommendation | `elimu-ai/ml-storybook-reading-level` · `ml-storybook-recommender` | **MIT** | Reading-level estimation and story selection — the adaptive seam |
| Alternative / additional core | `learningequality/kolibri` | MIT | Offline-first by design; use where the deployment is not Sub-Saharan or where Kolibri's channel ecosystem is wanted |
| Pedagogy-bearing content | `oppia/oppia` | Apache-2.0 | Explorations with misconception handling — built for emerging markets |
| Local inference | `ollama/ollama` | MIT | **Mandatory, not optional.** No cloud model call is reachable at the edge |
| Local retrieval | `qdrant/qdrant` | Apache-2.0 | Curriculum corpus on-device/on-server — the FAISS-shaped component EduNaija was described as having and does not |
| Orchestration with policy nodes | `langchain-ai/langgraph` | MIT | Language routing, accommodation floor, escalation as explicit nodes |
| Eval gate | `acheamponge/wassce-benchmark` | MIT | **The only African-curriculum open evaluation asset this KB has found.** Measure before you claim |

### Wiring

```
[Android device, intermittent connectivity]
  elimu-ai/launcher  ──enforces──>  EGRA/EGMA path
         │
  elimu-ai/appstore  ──sideloads/updates──>  tutor APK   (no app store, no network)
         │
         ├── on-device: reading-level estimate (ml-storybook-reading-level)
         │              story selection       (ml-storybook-recommender)
         │
         └──[sync when a link appears]──> school/district server
                                            elimu-ai/webapp   (content + roster)
                                            ollama            (local model)
                                            qdrant            (curriculum corpus)
                                            langgraph         (tutor policy graph)
                                                 │
                                            wassce-benchmark  (pre-release eval gate)
```

**Sync is store-and-forward, and that is a design rule, not a limitation.** The tutor must be
correct with a stale corpus and no server; the server is where the model and retrieval live, the
device is where the session happens.

### Design rules

1. **Local retrieval over the client's own curriculum. Never general web search.** This is the
   specific correction the EduNaija reading produced: web grounding is both unreachable at the
   edge and unaccountable to a syllabus.
2. **Language routing is a first-class node.** EduNaija's one genuinely transferable idea is
   detect-then-answer-in-language across five Nigerian languages including **Nigerian Pidgin** —
   the language learners actually use, and the one a formal corpus omits.
3. **Keep a verifier node.** The main → verifier → escalate shape is sound; replace its web-search
   escalation with *retrieve-more-locally, then defer to a teacher*.
4. **Merge the statutory/programmatic accommodation baseline into agent state** so the model can
   add but not remove a required accommodation — `P496-1`, unchanged here.
5. 🔴 **Exclude `elimu-ai/ml-authentication` (MIT, 16 ★).** It is **student login by on-device
   face recognition — biometric identification of children**, and it is the one repo in the org
   idle since 2025-02-25. Remove it deliberately, record the removal in the design note, and use
   roster codes or teacher-mediated login instead.
6. **Gate the release on `wassce-benchmark`**, and publish the number. In a market with no
   licensed competition, a measured result is the differentiator.

### Deliverables

An offline-capable tutor over the client's curriculum corpus; a store-and-forward sync tier; the
language-routing and verifier graph; an accommodation-floor layer; a WASSCE-benchmark eval report
run before release; and a design note recording the face-recognition exclusion and the
store-and-forward contract.

### Licence posture

🟢 **Clean and permissive throughout** — MIT and Apache-2.0 only, every licence byte-read. This
is unusual for this KB: the LMS cores a studio normally inherits (Moodle GPL-3.0, Open edX and
Canvas AGPL-3.0) are copyleft, so **a closed, branded derivative is genuinely available here.**
Two cautions: `elimu-ai/web3-wiki` is **CC0-1.0** (public-domain dedication — no patent grant, no
warranty disclaimer), so do not pull it in as if it were MIT; and **nothing unlicensed from the
exam-channel census may be vendored**, above all
https://github.com/Seunope/aloc-endpoints (223 ★, no licence, third-party exam copyright).

### Estimate

**8–10 weeks** for the tutor, local retrieval and sync tier on top of a standing `elimu-ai` or
`kolibri` deployment. Add **3–4 weeks** per additional language beyond the first two (corpus
preparation dominates, not code). Add **2 weeks** for the eval gate if the client wants the
benchmark report as a deliverable.

### Where it does not apply

- **Not for urban, connected deployments** — the offline machinery is real cost. Use **P1** or
  **P2**.
- **Not for secondary-exam coaching without a licensed corpus.** The question banks that exist
  are unlicensed; a client must bring its own content or license it.
- 🟡 **`elimu-ai`'s source has not been read** (`Gap 486-J`). The licences, stars, forks and push
  dates are measured; the EGRA/EGMA path, the ML components' quality and the Aragon DAO
  governance are **descriptions, not findings**. **Read the source during scoping** — this
  pattern asserts the platform is adoptable on licence and activity evidence, not on a code
  review.
- **Not a Middle East pattern.** Despite the shared EMEA bucket, this pass found **no Middle East
  education repository at all**; Gulf demand is real and the supply leg there is untried.

---

## P15 — Branded, closed mobile client and components over the client's existing copyleft LMS (added p896)

### Why this pattern exists

**Added p896, from T17.** The commonest licence impasse in an education engagement: the client
runs **Moodle (GPL-3.0)**, **Open edX (AGPL-3.0)** or **Canvas (AGPL-3.0)**, wants a branded
product with proprietary differentiators, and legal stops the conversation at the server's
licence. The standing answers are LTI 1.3 (**P2**) and MCP (**P11**), and both are good — but
they both put your work *beside* the platform and leave the learner's actual interface untouched.

🟢 **The platform vendors publish the interface layer permissively.** Restoring 34 rows to
`repos/foundations.md` and sorting them by licence made this visible: the mobile clients, the
component frameworks, the design systems and the analytics stacks of these copyleft platforms
are **Apache-2.0 or MIT**, maintained first-party. **A closed, branded client over a copyleft
server is a supported architecture.**

### What you build on

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Mobile client (Moodle) | https://github.com/moodlehq/moodleapp | **Apache-2.0** | Fork and brand; 1,007 ★, Moodle HQ-maintained. Licence at `main/COPYING.txt`. |
| Mobile client (Open edX) | https://github.com/openedx/openedx-app-android · https://github.com/openedx/openedx-app-ios | **Apache-2.0** | Same move on the other platform. |
| In-platform component | https://github.com/openedx/XBlock | **Apache-2.0** | Ship a proprietary learning component **inside** an AGPL LMS. Develop against https://github.com/openedx/xblock-sdk. |
| Design system | https://github.com/openedx/paragon · https://github.com/instructure/instructure-ui | **Apache-2.0** · **MIT** | Native-looking UI without touching platform code. |
| Interactive content | https://github.com/h5p/h5p-interactive-video · https://github.com/h5p/h5p-course-presentation · https://github.com/h5p/h5p-audio-recorder · https://github.com/h5p/h5p-speak-the-words | **MIT** (content types) | Compose the **MIT** content types; do **not** embed the **GPL-3.0** `h5p-php-library` in the closed part. |
| Content pipeline | https://github.com/h5p/h5p-cli | **MIT** | Makes generation scriptable — the step from demo to pipeline. |
| Agent tier | `ai-shifu` (Apache-2.0) or `Pyris` (MIT) behind https://github.com/Cvmcosta/ltijs | Apache-2.0 / MIT | Authored teaching flow, model layer kept swappable. |
| Analytics | https://github.com/davidpesce/moodle-logstore_xapi (**GPL-3.0**, in-platform plugin) → https://github.com/yetanalytics/lrsql (**Apache-2.0**) · https://github.com/openedx/openedx-aspects (**Apache-2.0**) | mixed | The plugin lives inside the copyleft platform where copyleft is expected; the LRS and your analysis stay permissive. |
| SSO | https://github.com/apereo/phpCAS (Moodle/PHP) · https://github.com/apereo/java-cas-client | Apache-2.0 | Join the institution's identity estate rather than minting accounts. |

### How to wire it

1. **Draw the licence boundary first, in writing.** Three zones: *copyleft server* (untouched,
   client-operated), *in-platform plugins* (`logstore_xapi`, any Moodle plugin — these are GPL
   and are published as such), and *your product* (forked Apache mobile client, Apache XBlocks,
   MIT components, the agent tier). Nothing crosses from zone 3 into zone 1 by linking.
2. **Fork the mobile client, do not rewrite it.** Rebrand, strip what the client does not need,
   add the agent surface. Keep the upstream remote: these apps track platform API changes, and
   that maintenance is the reason to start from them.
3. **Put the differentiator in an XBlock (Open edX) or a plugin-plus-LTI split (Moodle).** On
   Open edX the component runs in-platform under Apache. On Moodle, anything in-platform is GPL,
   so the proprietary part sits behind `ltijs` and only a thin GPL shim lives inside.
4. **Generate content through `h5p-cli`**, not by hand, and keep the generator in zone 3.
5. **Emit xAPI from day one** (`logstore_xapi` → `lrsql`) so **P7**'s outcome evidence exists
   without a later retrofit. On Open edX use `openedx-aspects` instead.
6. **Authenticate through the institution's CAS** before the first pilot cohort, not after.

### What makes it defensible

- 🟢 **Licence-clean by construction**, and provable: every zone-3 row above is Apache-2.0 or MIT,
  byte-read where the SPDX field was unreliable.
- 🟢 **The client keeps its system of record** — gradebook, enrolment, accreditation — so the
  engagement does not become a migration.
- 🟢 **First-party maintenance upstream.** You are forking repos maintained by Moodle HQ, the
  Open edX foundation and Instructure, not abandoned middleware.

### Estimate

**6–8 weeks** to a branded, agent-enabled mobile pilot over an existing LMS (fork, brand, agent
surface, SSO, xAPI). Add **3–4 weeks** for a first proprietary XBlock or LTI component. Add
**2 weeks** for the analytics tier if the client has no LRS.

### Where it does not apply

- 🔴 **Not where the client wants the *server* closed.** This pattern leaves the copyleft core in
  place. If a proprietary platform is the requirement, start from **Artemis**, **Kolibri**,
  **OpenOLAT** or **Mentingo** (**P1**).
- 🔴 **Not an EU proctoring or affect story.** Emotion inference in education is **prohibited in
  the EU since 2 February 2025**, and assessment/exam-access use is Annex III high-risk from
  2 December 2027 — see `verticals/solutions.md` and **P4**/**P9**.
- 🟡 **Verify the satellite licence per repo, per release.** The asymmetry is per-artefact and a
  relicence upstream closes this route for that platform (**T17** watch condition).
- 🟡 **`h5p-interactive-video` carries this KB's weakest licence evidence** — MIT on the search
  channel only, no licence file at twelve candidate paths. Confirm before it enters zone 3.

## P16 — Vernacular-medium second-language tutor, with the language relationship in the schema (added p898)

**The problem.** A client delivers instruction in a language that is neither English nor the language
being taught — a Bahasa-medium school teaching English, a Spanish-medium university teaching
Mandarin, a Portuguese-medium system teaching French. The default build (one LLM, one free-text
response field, a translated UI) collapses three distinct languages into one channel, and the
pedagogical scaffolding — *what the learner sees in their own language versus what they must produce
in the target language* — becomes a prompt convention that the model silently violates under load.

**Why this pattern exists separately from `P13`.** `P13` is persona-stateless tutoring for
age-banded, affect-regulated markets; its constraint is regulatory. This one's constraint is
**linguistic and structural**, and the fix is in the data contract. See **T20**.

### The recipe

| Tier | What to use | Licence | Why this one |
|---|---|---|---|
| **Schema contract** | [`brian901106/japanese-tutor-mugi`](https://github.com/brian901106/japanese-tutor-mugi) — **read it, reimplement it** | MIT (byte-read, 1,068 B) | The only verified implementation of target-language and native-language scaffolding as **separate typed fields**, streamed by partial-JSON parsing. Small and young — take the contract, not the codebase. |
| **Pedagogical frame** | [`Li-Evan/BloomTutor`](https://github.com/Li-Evan/BloomTutor) | MIT | Structures interaction by Bloom level, which gives the schema a second axis (cognitive level) alongside the language axis. |
| **Vernacular curriculum reference** | [`itsme-ganzu/belajar-ngoding-byGanzu`](https://github.com/itsme-ganzu/belajar-ngoding-byGanzu) | MIT | Worked example of reasoning-first drilling written natively in Bahasa Indonesia rather than translated into it. |
| **Pronunciation / production** | [`OpenPronounce/OpenPronounce`](https://github.com/OpenPronounce/OpenPronounce) | MIT | Open pronunciation assessment — the production half of a second-language loop, and the one tier where a generic LLM is weakest. |
| **Serving** | `ollama` or `vllm` + `litellm` | MIT / Apache-2.0 | Self-hosted inference. Required outright for EMEA sovereignty work and for any client that cannot export learner utterances. |
| **Learner state** | `qdrant` + a persistent store | Apache-2.0 | Carry per-learner error patterns across sessions. **`LearnHarness` is the reference design for learner-state modelling and is AGPL-3.0 — read it, do not link it.** |
| **Host platform** | Moodle (GPL) via `Faixiang/Moodle-MCP` (MIT) or `G36maid/moodle-mcp` (MIT) | MIT connectors over a GPL platform | The connector tier is permissive even where the platform is copyleft — **T17**'s third integration route. |

### The contract to implement

Every tutor turn returns **typed fields, not prose**:

- `target_text` — the utterance in the language being taught
- `native_hint` — scaffolding in the learner's own language
- `bloom_level` — the cognitive level this turn is pitched at
- `error_tags[]` — what the learner's previous production got wrong, for the state tier

🔵 **The whole point: `target_text` and `native_hint` are never the same field and never
concatenated.** That single constraint is what a translated English tutor cannot express, and it is
what makes the output renderable as two visually distinct channels, gradeable separately, and
analysable for whether the learner is actually producing target-language content or leaning on the
scaffold.

### Licence posture

🟢 **Permissive end to end** — MIT, Apache-2.0 and MIT-connectors-over-GPL. A closed, client-branded
derivative is clean, provided `LearnHarness` is read rather than linked and the Moodle tier stays on
the connector side of the boundary. This is the **second** pattern in this file (after `P14`) that is
permissive all the way down.

### Estimate and honest limits

**8–10 weeks** to a pilot on one language pair with one institution.

🔴 **What you are not getting.** Neither vernacular repo is substrate — they are a few dozen to a few
hundred stars and individually maintained. **The schema is the deliverable you are reusing; the
implementation is studio IP.** Budget accordingly, and do not price this as integration work.

🔴 **Unproven.** No learning-outcome study exists for the separate-fields contract. It is a
well-formed design argument supported by one working implementation, **not** an evidenced
intervention. Say so to the client rather than implying efficacy data that does not exist.


## P17 — AI grading assist over a BSD autograder, with the deterministic tier untouched (added p899)

### Why this pattern exists

A North American higher-ed client asking for "AI grading" is usually imagining the model marking
the work. **That is the one design that cannot be sold**, because it is simultaneously the
weakest pedagogically, the most exposed under FERPA and several US state statutes, and — from
2 December 2027 — an **EU AI Act Annex III high-risk** use if it determines learning outcomes.

🟢 **p899's measurement makes the alternative concrete: the deterministic grading substrate
already exists, under BSD, maintained by universities.** This KB previously recorded the grading
category as effectively empty; that was a keyword artefact (`898-G2`). It is not empty, and
nothing in the stack below needs to be built.

### Stack — every row licence byte-read 2026-11-18

| Layer | Repo | Licence | Why this one |
|---|---|---|---|
| **Grading platform** | https://github.com/Submitty/Submitty | **BSD-3-Clause** (`LICENSE.md@main`, `sha256₁₂ c123708cb4ef`) | 807 ★, RPI/RCOS, 12 years old, pushed 2026-11-18. Submission + autograding + **TA/manual grading with rubrics** in one system. **No copyleft, no patent clause, no enterprise carve-out — the derivative can be closed.** |
| **Notebook grading** | https://github.com/jupyter/nbgrader | BSD-3-Clause | For data-science courses; already shelved. Use instead of Submitty when the course is notebook-native |
| **Platform-free autograding** | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | Python **and R**, grades locally or in a container. Use when the client will not adopt a platform |
| **Sandboxed execution** | https://github.com/openedx/codejail *or* https://github.com/ls1intum/Ares | Apache-2.0 / MIT | **Never let an agent execute student code outside one of these** |
| **Learner model** | https://github.com/CAHLR/pyBKT | **MIT** (`LICENSE@master`, `sha256₁₂ ad0c7a38bf01`) | UC Berkeley CAHLR. Turns a response history into a per-skill mastery estimate — **the input that makes feedback adaptive rather than generic** |
| **Agent orchestration** | https://github.com/langchain-ai/langgraph | MIT | Policy checks become explicit, auditable graph nodes |
| **Rubric reference architecture** | https://github.com/virtualryder/edu-ai-agents | MIT | Deny-by-default authorisation, PII masking, HITL enforcement, tamper-evident audit, **deterministic rubric service rather than an LLM** |

🔴 **Do not reach for `PrairieLearn/PrairieLearn` here without reading `repos/foundations.md`
first.** Its Community Edition is **AGPL-3.0** and `apps/course-agent/` — the AI tier, i.e.
exactly this pattern's layer — is **proprietary Enterprise Edition**: production use needs a paid
subscription and the licence **assigns your modifications to PrairieLearn, Inc.** This KB
published that row as "MIT · Permissive" until p899.

### How it wires together

1. **Submitty grades deterministically and remains the system of record for the mark.** The agent
   never writes a grade. This is the load-bearing rule.
2. The agent reads `(submission, test results, rubric)` and drafts **feedback and a suggested
   rubric selection**, surfaced to the TA as a proposal.
3. **The TA accepts, edits or rejects** in Submitty's existing manual-grading UI. The accept/edit
   signal is the audit record *and* the evaluation dataset.
4. `pyBKT` consumes the mark history and returns per-skill mastery, which selects **what the
   feedback emphasises** — not what the mark is.
5. Every agent action is logged with the model version and prompt hash, per `edu-ai-agents`.

### The design rule that makes it defensible

🔵 **The mark is deterministic; the prose is generated; a human moves between them.** Under this
split the AI system is not "determining learning outcomes" — which keeps it out of Annex III
high-risk classification, satisfies the US state rules that prohibit AI-only grading decisions,
and gives the institution an appeal story that survives a student challenge. **It is also the
only split for which you can show the client a measured accept-rate.**

### Deliverables

- Submitty deployment + the feedback-assist service as a separate process (clean licence boundary)
- Rubric-selection evaluation harness with TA accept/edit/reject as ground truth
- `pyBKT` mastery service with a per-skill dashboard
- FERPA data-flow map and a written Annex III classification argument

### Licence posture

🟢 **Fully closable.** Submitty BSD-3-Clause, otter-grader BSD-3-Clause, nbgrader BSD-3-Clause,
pyBKT MIT, LangGraph MIT, edu-ai-agents MIT, codejail Apache-2.0. **No copyleft anywhere in the
stack**, which is rare in education and is the reason to prefer this composition over the
Open edX/`edx-ora2` route (AGPL-3.0) when the client wants to own the result.

### Estimate

**6–8 weeks** to a pilot on one course with real TAs. Add 3–4 weeks if Submitty is not already
deployed. 🔴 **Unproven:** no published study shows AI-drafted rubric feedback improves outcomes.
Sell the **TA time saved and the audit trail**, both of which you can measure in the pilot, and
do not imply learning-gain evidence that does not exist.

### Where it does not apply

K-12 in jurisdictions requiring parental opt-in before any AI touches student work (Florida's
2026 board rules), and any client who wants the mark itself generated — decline that scope and
explain why in one paragraph.

## P18 — Zero-provisioning teacher coaching over WhatsApp (added p899)

### Why this pattern exists

Every other pattern in this file assumes the learner or teacher has a provisioned device, an
account and a browser. **For a large part of the market that assumption is the project risk**, and
it is the reason public-sector education pilots stall between PoC and deployment.

🟢 **p899 verified the first open agent in this KB that removes the assumption entirely.**
https://github.com/Orenda-Project/rumi-platform (**Apache-2.0**, `LICENSE@main`, 11,287 B,
`sha256₁₂ c589d95090ce`) runs **wholly on WhatsApp**: no app to install, no login, no training
day. It delivers classroom coaching, reading assessment and lesson plans by **text and voice
note**, in **15 languages**, with voice transcription via Meta's MMS-ASR, and is explicitly built
to be cloned and run on your own API keys.

🔵 **Its target market is South Asia; the channel argument is at least as strong in LATAM**, where
WhatsApp is the dominant messaging surface and this KB has repeatedly recorded an
adoption-ahead-of-governance asymmetry among teachers (Brazil 56%, Chile 55%, Colombia 53% teacher
AI use against an OECD average of 36%).

### Stack

| Layer | Repo | Licence | Role |
|---|---|---|---|
| **Channel + agent** | https://github.com/Orenda-Project/rumi-platform | **Apache-2.0** | WhatsApp transport, voice-note handling, coaching flows. **Patent grant included** |
| **Local/sovereign inference** | https://github.com/ollama/ollama *or* vLLM | MIT / Apache-2.0 | Keeps teacher messages in-country where a ministry requires it |
| **Curriculum grounding (UK/EMEA)** | https://github.com/oaknational/oak-ai-lesson-assistant | **MIT** (code) | Curriculum-aligned lesson generation from a national curriculum body. 🟡 Content is **Open Government Licence**, trademarks excluded |
| **Curriculum grounding (Brazil)** | https://github.com/bncc-dev/bncc-pacotes | 🔴 `NOASSERTION` — **byte-read before use** | BNCC (Brazilian national curriculum) as packages + an MCP server. 10 ★ — thin, verify the grant |
| **Brazilian public data** | https://github.com/Mcp-Brasil/mcp-brasil | **MIT** | 1,865 ★. MCP over 70 Brazilian public-sector APIs — **the largest LATAM-origin asset this KB has verified** |
| **Offline fallback** | https://github.com/learningequality/kolibri | MIT | For the schools where even WhatsApp is intermittent |

### How it wires together

1. Teacher sends a voice note or text to a WhatsApp number. **No onboarding step exists.**
2. Rumi transcribes (MMS-ASR), routes to the coaching flow, and replies in the teacher's language
   — by voice if the teacher used voice.
3. Lesson-plan requests are grounded against the **national curriculum** package for that
   jurisdiction (Oak for England, `bncc-pacotes` for Brazil), not against model recall.
4. Inference runs locally via Ollama/vLLM where data residency is a procurement condition.
5. Usage is metered per school for the ministry's reporting, per **P8**.

### The design rules that make it defensible

- 🔴 **Teacher-facing only.** Do not put this channel in front of under-18 learners: WhatsApp's own
  age floor, the UAE under-13 prohibition and the US state parental-opt-in rules all land here.
  **Coaching the teacher is the defensible scope** and is also where the measured workload saving
  is (Oak reports teachers saving ~3.5 hours a week with Aila — **Oak's own figure, not
  independently verified**).
- 🔵 **Curriculum grounding is the quality control.** The reason to ground on BNCC or the Oak
  curriculum is not pedagogy theory — it is that a ministry will reject generated material that
  cannot be traced to its own standard.
- 🟡 **Meta dependency is a real risk.** The WhatsApp Business API terms and pricing are outside
  the client's control and outside this licence stack. Say so in the proposal.

### Deliverables

- Self-hosted Rumi deployment on the client's WhatsApp Business number and own API keys
- Curriculum grounding pack for the jurisdiction + traceability from reply to standard
- Teacher-cohort usage and workload-saving measurement
- Data-residency note covering transcription and inference

### Licence posture

🟢 **Closable.** Rumi Apache-2.0 (with patent grant), Ollama MIT, Kolibri MIT, mcp-brasil MIT, Oak
code MIT. 🔴 **Two conditions:** Oak's *content* is Open Government Licence and its marks are
excluded from the grant; `bncc-pacotes` reports `NOASSERTION` and **must be byte-read before it
reaches a build**.

### Estimate

**6–8 weeks** to a pilot with one teacher cohort. 🔴 **Honest limits:** Rumi is **25 ★ and young**
— this is a reference implementation and a channel argument, **not substrate**. Budget the
integration as studio IP, pin the version, and expect to maintain the fork.

---

## P19 — Standards-native assessment delivery a client can keep closed: QTI 3 in, xAPI out, no copyleft anywhere (added p900)

**The problem this solves.** A client has existing assessment content and wants an AI tier that
authors, delivers and scores items — **and wants to own the result**. Every route this file
previously offered ran through a copyleft platform: Open edX's `edx-ora2` (AGPL-3.0), Moodle
(GPL-3.0), or `Citolab/qti-components` (GPL-3.0) for the player itself. 🔵 **p900 shelved the
pieces that make an end-to-end permissive route exist for the first time.**

### The stack — every grant byte-read, every row verified 2026-11-18

| Layer | Repo | Grant | Why this one |
|---|---|---|---|
| Item format in | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (1,071 B) | Renders **and scores** QTI 3. TypeScript core with **zero third-party runtime dependencies**, plus converters for the client's older QTI. The permissive alternative to `Citolab/qti-components` (GPL-3.0) |
| Item authoring | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT | Generates MCQs and assessments from source content. 🟡 Idle since 2026-05-29 — vendor it, do not track it |
| Learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) + [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | MIT + MIT | Neural knowledge tracing **with its classical baseline beside it**. Ship both: pyBKT is what you show when the client asks whether the neural model earns its cost |
| Integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | Post-hoc similarity across submissions. 🔵 **Deliberately not proctoring** — see the regulatory note below |
| Evidence out | [`adlnet/xapi-spec`](https://github.com/adlnet/xapi-spec) + [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 + Apache-2.0 | The normative spec to validate against, and a SQL-backed LRS to write to |
| Legacy delivery | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | MIT | Ships the result into the client's existing LMS **without re-authoring**, because their content is already SCORM |
| Platform seam (optional) | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | MIT | Talks to AGPL-3.0 Canvas **over its API**, so the platform's licence does not reach your code |

### Wiring

1. **Ingest** the client's QTI 1.2/2.x through `qti3`'s conversion tooling; keep QTI 3 as the
   single internal item representation. Authoring agents emit QTI 3, never a bespoke JSON.
2. **Author** with `educhain` behind a review queue. 🔴 Generated items are *drafts*: the
   human-approval step is the deliverable, not a nicety — several jurisdictions in **T1**
   regulate automated assessment decisions, not automated assessment *content*.
3. **Deliver and score** in the browser with the `qti3` Web Component. Deterministic scoring
   stays in QTI's own response processing; **the AI tier never decides the grade**, which is
   what keeps this outside the Annex III high-risk box described below.
4. **Model** the learner with `pykt-toolkit`, fed from the scored responses; hold `pyBKT` as the
   baseline in the same evaluation harness.
5. **Emit** every interaction as xAPI statements into `lrsql`, validated against `xapi-spec`.
   This is the evidence layer that answers *"did it help"*, which **T23** argues clients now ask
   for before renewal.
6. **Integrate** by either publishing a SCORM package via `scorm-again` into whatever LMS they
   run, or talking to Canvas through `canvasapi`. 🔵 **Neither path forks a copyleft platform.**

### Licence posture

🟢 **MIT and Apache-2.0 end to end. There is no GPL, AGPL or LGPL component in this pattern** —
the second pattern in this file (after **P14**) that is permissive throughout, and the first one
that is permissive throughout *at enterprise scale* rather than on a single offline platform.
The studio's agent tier, the item bank and the learner model can all be client-owned IP.

### Regulatory posture — read this before scoping

🔴 **Scoring an exam that affects progression is an EU AI Act Annex III high-risk use.** The
Digital Omnibus (**Regulation (EU) 2026/1744**) moved those obligations to **2 December 2027**,
which is scoping time, not an exemption — and **transparency duties under Article 50 already
apply**. Two design choices follow and both are in the wiring above: **deterministic scoring
owns the grade**, and **integrity is post-hoc comparison (`dolos`) rather than proctoring**,
because exam monitoring carries its own Annex III exposure and, where biometric or emotion
inference is involved, runs into an outright prohibition in EU schools.

### Estimate

**8–12 weeks** to a pilot with one course's item bank converted, authoring behind review, live
delivery and an LRS receiving statements. The QTI conversion of the client's legacy bank is the
schedule risk and the part to timebox first — `qti3`'s converter handles the common cases and
not the exotic ones, and which of those a client has is not knowable from a statement of work.


## P20 — Permissive synchronous classroom with an AI teaching assistant the client can keep closed (added p901)

**The gap this closes.** Every synchronous-delivery pattern in this file so far routes through
BigBlueButton (`LGPL-3.0`) or assumes the client already runs Zoom/Teams. `p901` verified
`jitsi/jitsi-meet` at **Apache-2.0, 30,255★, 8,134 forks, pushed 2026-11-18** — which makes an
**end-to-end permissive live classroom** buildable for the first time in this KB. This is the
second pattern here (after **P14**) whose licence posture is permissive from top to bottom, and
the first that is not offline-first.

**Who it is for.** A client who teaches live — a university running tutorials, a training
provider, a ministry running teacher CPD — who wants session transcripts, attendance and
comprehension signals turned into teaching feedback, and who intends to keep the resulting
product closed or resell it. The copyleft route makes that last part expensive; this one does not.

### The stack, with the grant on every tier

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Live classroom | [`jitsi/jitsi-meet`](https://github.com/jitsi/jitsi-meet) | 🟢 `Apache-2.0` (byte-read `12,596 B`, `eae52e200cd8`) | Finished, self-hostable conferencing app with its own mobile SDKs. `30,255★`. **Not** BigBlueButton: BBB is `LGPL-3.0` and purpose-built for classrooms, which is the better fit *unless* the client needs to ship a closed derivative |
| Recording / capture | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟡 `ECL-2.0` | `513★`, pushed `2026-11-18`. Apache-derived with a patent clause; fine alongside, keep it a separate service |
| Transcription | `faster-whisper` | 🟢 `MIT` | Already the transcription tier elsewhere in this file; feed it Opencast output or Jitsi's recording hook |
| Mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 `MIT` | UC Berkeley CAHLR Bayesian Knowledge Tracing. **Do not invent a comprehension score** — this is the evidence-backed one, and it is the tier a general-purpose campus LLM stack does not provide |
| Spaced review | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 `MIT` | Turns the mastery estimate into a review schedule instead of a dashboard nobody reads |
| Teacher console | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 🟢 `Apache-2.0` | Human-in-the-loop queue. The teacher approves or discards every generated signal |
| LMS of record | Moodle / Open edX / Canvas | 🔴 `GPL-3.0` / `AGPL-3.0` | **Integrate over LTI 1.3 or REST. Do not fork.** This is the `G1` gate below |
| Agent tier | Studio IP | — | Closed, because every tier above it is permissive |

### Wiring

1. **Jitsi emits, it does not host your logic.** Self-host Jitsi Meet; use its recording and
   webhook hooks to drop session artefacts into object storage. Keep your services *outside*
   the Jitsi tree — the Apache-2.0 grant is clean, and forking is what loses you that.
2. **Opencast or Jitsi recording → `faster-whisper` → a per-session transcript** with speaker
   turns. Timestamps are what later make a comprehension signal attributable to a moment.
3. **Transcript + in-session quiz responses → `pyBKT`.** Mastery is estimated per skill from
   observed responses. 🔴 **The transcript alone is not evidence of mastery** — if the client
   has no in-session questioning, add it before promising a mastery number.
4. **`pyBKT` → `fsrs4anki`** for each learner's review schedule.
5. **Everything a teacher sees lands in Appsmith first.** Generated summaries, flagged
   learners and suggested re-teach points are proposals until a human accepts them.
6. **Write back to the LMS over LTI 1.3 / REST only.** Grades and completion go back through
   the documented interface. The LMS stays unmodified and its copyleft never reaches you.

### Licence posture of the result

🟢 **The client can keep the agent tier and the console closed.** Jitsi (Apache-2.0),
`faster-whisper`, `pyBKT`, `fsrs4anki` (MIT) and Appsmith (Apache-2.0) impose attribution, not
source disclosure. 🔴 **The one gate: the LMS.** Moodle is GPL-3.0 and Open edX/Canvas are
AGPL-3.0 — integrate across a network interface and you are fine; fork or link and the
derivative-work question is live. **Run `G1` before quoting.**

🔴 **Add a CI check, not a memo** — see **T24**. If the build ever vendors a repository whose
grant is path-dependent, assert in the pipeline that the restricted paths are absent from the
artifact. For this stack that check is currently trivial (no multi-grant component), which is
exactly when it is cheap to put in place.

### Estimate

**8–10 weeks** to a production pilot for one faculty or one training programme: 2 weeks Jitsi
self-hosting and recording pipeline, 2 weeks transcription and session modelling, 2–3 weeks
`pyBKT` calibration against the client's actual assessment data (**this is the step that slips**
— it needs historical response data, and if the client has none, the model has nothing to fit),
1–2 weeks Appsmith console, 1 week LTI write-back. 🔵 Jitsi self-hosting at class scale is the
underestimated line: budget real infrastructure time for TURN/JVB capacity.

### Where it sells

🟢 **APAC, strongly** — see `intel/market.md`: an NTU-shaped client whose undergraduates already
have a frontier general-purpose stack does not need another assistant; it needs the mastery and
assessment tier that stack does not provide, which is precisely tiers 4–6 here. 🟢 **EMEA** —
the whole stack is self-hostable, which answers the data-residency and sovereignty question
(Council of the EU `14902/26`) directly, and Jitsi self-hosted keeps session content in the
client's own infrastructure. 🟡 **North America** — viable, but `pyBKT` and `Submitty` land
better where the client already runs their own LMS; check state AI-in-education rules first
(**NC Session Law 2026-41**, **NY A 9190** restricting classroom AI to grade 9+, **CA AB 1159**
on student data and model training — AB 1159 matters here because transcripts are student
data). 🟢 **LATAM** — the permissive posture and self-hostability fit the budget and the
26%-have-a-formal-AI-strategy governance gap; pair with the P14 offline-first pattern where
connectivity is the binding constraint, since **this pattern assumes live video and therefore
assumes bandwidth.**


## P21 — Notebook-native course with deterministic marking and an AI feedback tier, permissive end to end (added p902)

**The gap this closes.** Every assessment pattern in this file routes through a platform — Submitty,
PrairieLearn, Open edX ORA, Artemis. None of them addresses the case where **the artefact the student
submits is a notebook**, which is how CS, data science, engineering and quantitative social science
are actually taught. `p902` verified the whole tier (`repos/trending.md` `902-R1`), and it is the
**only tier in this KB that is permissive from top to bottom with no copyleft and no enterprise
carve-out** — compare the LMS tier, where every incumbent is GPL or AGPL.

**Who it is for.** A university faculty, a bootcamp or a corporate upskilling programme teaching
Python/R at scale, that wants per-student environments with no install day, marking that is
reproducible enough to survive an appeal, and AI feedback that a lecturer signs off — while keeping
the result as their own IP.

### The stack, with the grant on every tier

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Student environment | [`jupyterhub/binderhub`](https://github.com/jupyterhub/binderhub) | 🟢 `BSD-3-Clause` (byte-read `1,522 B`, `611f531642d5`) | `2,673★`. A git repo becomes a running environment from a URL. **No lab image, no install day** |
| Auth + persistence | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 `BSD-3-Clause` | Use **instead of** BinderHub when students need identity and persistent storage; use **both** when you want ephemeral try-it plus a graded home |
| Content as text | [`mwouts/jupytext`](https://github.com/mwouts/jupytext) | 🟢 `MIT` (title line byte-read; ★ **unmeasurable**, `902-F3`) | Notebooks as `.py`/`.md`. **This is the tier that makes the curriculum reviewable in a pull request** — without it, course content is a blob and no agent can propose a diff to it |
| Assignment flow | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 `BSD-3-Clause` | `1,370★`. Release / collect / autograde / feedback. The course standard |
| Deterministic marking | [`computationalmodelling/nbval`](https://github.com/computationalmodelling/nbval) | 🟡 `BSD-3-Clause` — **SPDX `NOASSERTION`**, resolved from clause structure; Univ. of Southampton | `453★`. Validates a notebook against stored outputs under `pytest`. 🟢 **No model in the loop, so the mark is reproducible and appealable** |
| Language-agnostic autograding | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 `BSD-3-Clause` | Add when the course is **R as well as Python**, or when submissions arrive via Canvas/Gradescope |
| Sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | 🟢 `Apache-2.0` | **Before any agent or grader executes student code.** Non-negotiable |
| Notebook corpus | [`nbgallery/nbgallery`](https://github.com/nbgallery/nbgallery) | 🟢 `MIT` | `150★`. Sharing, search, usage analytics and health checks across the course's notebooks |
| Mastery model | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 `MIT` | Per-skill mastery from observed responses. UC Berkeley CAHLR |
| Teacher console | [`appsmithorg/appsmith`](https://github.com/appsmithorg/appsmith) | 🟢 `Apache-2.0` | The approval queue. Nothing generated reaches a student unreviewed |
| LMS of record | Moodle / Canvas / Open edX | 🔴 `GPL-3.0` / `AGPL-3.0` | **LTI 1.3 / REST only.** Grades out, roster in, no fork |
| Feedback agent | Studio IP | — | Closed, because every tier above is permissive |

🔴 **Two repos to read and not ship**, both verified this pass: `parmentelat/nbautoeval` is
**`CC-BY-SA-4.0` on executable code** (no patent grant, ShareAlike reaches derivatives — an exercise
bank built on it cannot stay closed) and `pyta-uoft/pyta` is **`GPL-3.0`**. PyTA's *idea* — linter
errors phrased for a beginner — is worth copying into the feedback prompt; its code is not worth
linking.

### Wiring

1. **Make the course a repository.** Notebooks are committed as text via `jupytext`; the `.ipynb` is
   a build artefact, never the source of truth. 🟢 This single decision is what makes every later
   step possible: diffs, review, CI, and an agent that proposes curriculum changes as pull requests.
2. **`nbgrader` owns the assignment lifecycle.** Author one source notebook per assignment with
   solution and test cells; release the student version; collect submissions.
3. **Mark deterministically first, with `nbval` under `pytest` inside `codejail`.** The numeric mark
   comes from here and **only** from here. 🔴 **Never let the model assign the grade** — this is the
   `P17` split, and in the US it is also a statutory line (**Oklahoma SB 1734** bars AI used solely
   for grading).
4. **Then, and only then, the feedback agent runs** — over the submission, the failing test output
   and the rubric — and writes *prose*, not a score: what the student got wrong, the beginner-phrased
   version of the error (the PyTA idea), and the next exercise.
5. **Every generated comment lands in the Appsmith queue** for the lecturer to accept, edit or
   discard. Acceptance rate is the metric that tells you whether the tier is working.
6. **`pyBKT` consumes the deterministic per-test outcomes**, not the model's opinion, so the mastery
   estimate stays defensible.
7. **Grades go back over LTI 1.3.** The LMS is never forked, so its copyleft never reaches the studio
   tier.
8. **`nbgallery` sits across the corpus** for search, usage analytics and health checks — and its
   health-check runner is the natural hook for an agent that *repairs* a notebook broken by a library
   upgrade rather than just flagging it. 🔵 That maintenance job is the recurring-revenue half of this
   engagement.

### Licence posture of the result

🟢 **Permissive end to end: BSD-3 (BinderHub, JupyterHub, nbgrader, nbval, otter-grader), MIT
(jupytext, nbgallery, pyBKT), Apache-2.0 (codejail, Appsmith).** Attribution only — no source
disclosure, no patent surprises, no enterprise carve-out of the kind `p899` found in PrairieLearn's
`apps/course-agent/`. **The client owns the feedback agent outright.** 🔴 **Two gates before quoting:**
the LMS stays across a network interface (`G1`), and **`riiid/ednet` must not be used to train
anything that ships** — it is `CC-BY-NC-4.0`, research only (`T25`, `902-R2`). Validate against
EdNet in a study; train on the client's own response data.

### Estimate

**6–8 weeks** to a production pilot for one course: 1 week BinderHub/JupyterHub on the client's
cluster, 1 week converting existing notebooks to `jupytext` and into git (🔵 **this is the step
clients underestimate** — the existing notebooks are usually undocumented and non-reproducible, and
fixing that is the real work), 1–2 weeks `nbgrader` + `nbval` test authoring per assignment set,
1 week `codejail` sandboxing and CI, 1–2 weeks feedback agent and Appsmith queue, 1 week LTI
write-back. `pyBKT` calibration is a further 2 weeks **and only if the client has historical response
data** — without it, leave the mastery tier out of scope rather than fitting a model to nothing.

### Where it sells

🟢 **North America, strongest** — the whole tier is built by its universities (Southampton aside:
Berkeley, Toronto, Michigan, RPI, CMU), the buyer already runs JupyterHub in most CS faculties, and
the 66%-institution-wide figure says they are past pilots and stuck on rollout. Check **CA AB 1159**
(student data must not train models) and **NY A 9190** (classroom AI restricted to grade 9+, so K-8
is out) before scoping. 🟢 **EMEA** — fully self-hostable, which answers the sovereignty question
(Council of the EU `14902/26`) without a vendor conversation; the UK's January 2026 school safety
standards are a procurement gate you can sell *against* rather than around. 🟡 **APAC** — strong in
higher ed, and the one region where the client may already have a frontier general-purpose stack
(NTU): sell the **deterministic marking and mastery** tiers, which that stack does not provide.
🟡 **LATAM** — the permissive, self-hostable posture and zero licence cost fit the ~USD 18.2M
rest-of-region market reality, but **BinderHub assumes bandwidth and a Kubernetes cluster**; where
neither holds, use `P14`'s offline-first pattern instead and keep only `nbgrader` + `nbval` as a
local marking tier.

## P22 — National-curriculum corpus as an agent-addressable skill tree, re-authored so the client owns the grant (added p903)

**When a client asks for this.** A ministry, a national exam board or a large private school group
has the curriculum — syllabus documents, approved textbooks, past papers — and wants an AI tutor
over *their* curriculum, not a generic one. `p903` found this already being done at national scale
and done in a way no studio can deliver: `revolover00/Bakloriya-AI-SKILLS` carries **Egypt's
complete approved 2026/2027 curriculum, 300 units across four stages, 28 MB**, with **no licence on
any of 12 byte-read paths** and no software at all. This pattern takes **its schema** — which is
free to copy — and supplies everything it lacks. See `intel/trends.md` **T26**.

### What you copy, and what you must not

🟢 **Copy the decomposition schema.** It is the most complete worked example of national-curriculum
sharding this base has measured, and a directory structure is not the copyrightable part:

```
skills/<stage>/<grade>/<term>/<subject>/
    SKILL.md        # routing index for the subject: the chapter tree
    glossary.md     # terms and core concepts
    patterns.md     # exam question patterns + solution keys
    cheatsheet.md   # the night-before summary
    chapters/ch01/  # one directory per teaching unit
             ch02/
```

🔴 **Do not copy the content, and do not vendor the repository.** 28 MB under default
all-rights-reserved copyright. Run **`G1`** before anything else; the corpus licence is the single
question that decides whether this engagement is an integration or a re-authoring, and for every
MENA corpus `p903` measured the answer was re-authoring.

🔴 **Do not copy its runtime, because it does not have one.** Its only control against hallucination
is a sentence in a prompt — *stay inside the syllabus, do not mix grades or terms.* That is not a
compliance story under EU Annex III or Vietnam's **Decision 33/2026/QD-TTg**, and it is the gap this
pattern's middle tier fills.

### The stack

| Tier | Component | Licence | Why this one |
|---|---|---|---|
| Corpus | **Client-owned curriculum**, re-authored into the schema above | Client's | The grant problem solved at the source. Where the client has no digital corpus, the permissive in-language assets in `repos/foundations.md` seed it: https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari (**MIT**, 2,432 ★, Turkish) and https://github.com/barnamenevisi/free-resources (**MIT**, 1,297 ★, Persian) |
| Path-scoped retrieval | https://github.com/qdrant/qdrant | Apache-2.0 | **This is the tier Bakloriya does not have.** Payload filtering enforces `stage`/`grade`/`term`/`subject` as a *hard* filter, so "do not mix grades or terms" becomes a query constraint instead of a request |
| Prerequisite structure | https://github.com/HKUDS/LightRAG | MIT | A curriculum *is* a prerequisite graph; `SKILL.md`'s chapter tree is the edge list. Use it so a stuck learner is routed backwards to the missing prerequisite, not re-shown the same unit |
| Agent tier | https://github.com/langchain-ai/langgraph or https://github.com/pydantic/pydantic-ai | MIT | Explicit nodes per teaching move — explain, worked example, graded probe, distractor explanation — mirroring what `patterns.md` already encodes per subject |
| Model serving | https://github.com/ollama/ollama (on-prem) or https://github.com/vllm-project/vllm (campus scale) | MIT / Apache-2.0 | Ministry work is data-residency work. Keep inference inside the client's boundary |
| Durable loops | https://github.com/temporalio/temporal | MIT | A term-long tutoring relationship is a long-running workflow, not a chat session |
| Delivery, connected | Moodle / Open edX over **LTI 1.3** | integrate, never fork | `G1`. The corpus and agent tier stay yours across the interface |
| Delivery, offline | https://github.com/learningequality/kolibri (MIT) or https://github.com/Crosstalk-Solutions/project-nomad (Apache-2.0) | MIT / Apache-2.0 | Where connectivity is the binding constraint, ship the corpus to the device and keep the agent tier optional |
| Audit trail | xAPI / LRS tier in `repos/foundations.md` | permissive | Annex III and Decision 33/2026/QD-TTg both want *per-learner, per-decision* records. Emit them from the agent nodes, not from the LMS |

### The zero-inference tier, and why it is a separate decision

`p903` also verified https://github.com/SalehGNUTUX/GT-MISHKATKIDS (**GPL-3.0**, byte-read 34,819 B,
pushed 2026-11-18): an Arabic early-years system that is **fully local, offline, and runs no AI at
runtime**, shipped as PWA, `AppImage`/`DEB`/`RPM` and Android `APK`, with the child's data never
leaving the device. Its loop is inverted — the child teaches an amnesiac robot (the protégé effect).

🟢 **Take the architecture as a design, for the early-years band only.** For ages 4–10 a
zero-inference build is usually *better*: no API bill, no egress, nothing to sign a DPA over, and no
hallucination surface. Pair it with the corpus tier above — the corpus drives a connected tutor for
secondary, a zero-inference consolidation loop for primary.
🔴 **GPL-3.0: study and reimplement, do not embed.** It is deployable and forkable as a system; it is
not a component for a closed deliverable. And its content sits in an explicit Islamic doctrinal
frame with Qur'anic recitation as a first-class module — portable architecture, non-portable content.

### Build estimate

| Phase | Work | Duration |
|---|---|---|
| 0 | **`G1` licence pre-flight on the client's curriculum corpus** and on every seed asset | 3–5 days |
| 1 | Schema adoption + ingestion of one stage/one term as the vertical slice | 2–3 weeks |
| 2 | Path-scoped retrieval (Qdrant payload filters) + prerequisite graph from `SKILL.md` trees | 2–3 weeks |
| 3 | Agent tier: teaching-move nodes, distractor explanation, graded probes | 3–4 weeks |
| 4 | Audit trail, evaluation harness, human-review console (Appsmith) | 3–4 weeks |
| 5 | Corpus scale-out to remaining stages and terms — **the long pole, and it is curriculum-writing labour, not engineering** | 8–16 weeks, parallelisable |
| | **Engineering total to first regulated pilot** | **10–14 weeks** |

🔵 **Price phase 5 honestly and separately.** Bakloriya's 300 units are the measurement of what the
content tier actually costs: a single maintainer produced them in under a month using models, which
means the labour is real but model-assisted, and a client who already has approved syllabus
documents is most of the way there. **The engineering is the 10–14 weeks; the corpus is a content
programme**, and conflating them is how this kind of engagement is underquoted.

### Regional notes

🟢 **EMEA (MENA first).** This is the pattern for the Gulf and North Africa. `p903` measured the
supply side: Saudi Arabia's Qiyas channel returns **12 repositories, all 0 ★, none licensed**,
against a demand side of 50 new curriculum units for 2026-27 and **240,000 teachers in training**;
Egypt has a complete national corpus with no grant. **There is nothing to adopt and the demand is
funded.** What a ministry is buying is the institutional engineering MENA's single-maintainer
projects do not have — licensing, evaluation, accessibility, audit trail, maintenance. Keep
`DigComp 3.0` on the EMEA checklist as an open question (`intel/market.md`): if AI-literacy
obligations are in scope, obtain the document before quoting.
🟡 **APAC.** The same stack, with the compliance tier promoted to the front: Vietnam's
**Decision 33/2026/QD-TTg** names education uses as high-risk with a **72-hour incident clock** and
pre-deployment registration, which makes the audit trail a phase-1 deliverable rather than phase 4.
🟢 **LATAM — rewritten `p904`, and it is now the *reference* region for this pattern rather than a
localisation afterthought.** The note here read *"LATAM supply is unchanged — Brazil-only, two small
repos"*; the Spanish/Portuguese channel falsified that. **Brazil has already executed this pattern
properly**: `bncc-dev/bncc-dados` publishes the national curriculum as 1,721 verified records with
per-record provenance, a reproducible pipeline, a Zenodo DOI and an `llms.txt` agent contract, under
**MIT code + CC BY 4.0 data**. 🔵 **So in LATAM, do not re-author — adopt the spine and build the
agent tier**, which is the inverse of the MENA instruction above and the reason **P23** exists as a
separate pattern. Elsewhere in the region, `bncc-dados` is the specification to quote when telling a
ministry what "curriculum as data, done properly" means. Pair with Latam-GPT where sovereign
inference is the ask, and keep the offline delivery row for low-connectivity deployments.
🔵 **North America.** The driver is not curriculum supply but **statute**: AI-literacy standards and
model-policy deadlines (NC Session Law 2026-41, Idaho SB 1227) create demand for exactly the audit
and evaluation tiers above. The corpus is usually the district's existing scope-and-sequence.


## P23 — Curriculum-grounded tutor with a **hallucination gate** as the acceptance test (added p904)

### Why this pattern exists

Every curriculum-aligned product makes one claim that a ministry or district will test directly:
*when this system cites a curriculum objective, the objective is real and the text is right.*
**P22** is for the case where the curriculum corpus does not exist and must be re-authored. **P23 is
for the case where it does** — and `p904` measured both the substrate and the failure mode it
prevents.

The failure mode, measured rather than asserted (`bncc-dev/bncc-benchmark`, round
`oficial-seca-2026-09`, 19 models × 900 responses, **all 17,100 raw responses published**): asked for
the exact text of a national-curriculum objective **without access to the source**, models
reproduce it faithfully between **88% and 3%** of the time, and accept codes **verified not to
exist** between **0% and 42%** of the time. 🔴 **Reproducing the right text and refusing an invented
code are distinct abilities** — the models scatter rather than falling on a diagonal, and one model
reproduces text at 76% while accepting 42% of fake codes. **An accuracy number alone will not
detect this, which is why the gate is two-metric.**

🔵 **The strategic point for a studio:** this converts the most common objection in a public-sector
education sale — *"your AI makes things up about our curriculum"* — from a reassurance into a
number, measured on the client's own curriculum, with a published harness the client can re-run
after handover.

### Stack

| Layer | Component | Licence posture |
|---|---|---|
| **Curriculum spine** | https://github.com/bncc-dev/bncc-dados — 1,721 objectives, per-record `fonte` + `localizador_pdf`, SQLite/CSV derivatives, DOI `10.5281/zenodo.21625233` | 🔴 **MIT code + CC BY 4.0 data** — **attribution is a UI requirement** |
| **Agent tool surface** | https://github.com/dfdb76/bncc-mcp (**MIT**, independent) and/or the MCP worker in https://github.com/bncc-dev/bncc-pacotes; `npx -y @bncc/mcp` runs locally | MIT; 🔴 **`bncc-pacotes` reserves the project name and visual identity** |
| **Query tier** | https://github.com/eumakerdev/bncc_api (**MIT**) — REST + semantic search returning official codes as citations | MIT |
| **Acceptance gate** | https://github.com/bncc-dev/bncc-benchmark `harness/` (**MIT**) — re-run against the client's model and curriculum | MIT harness, CC BY items/results |
| **Tutor tier** | `HKUDS/DeepTutor` (Apache-2.0) or `THU-MAIC/OpenMAIC` (MIT) for the teaching loop; `matheussilvano/mooose` (Apache-2.0) as the reference for rubric-bound grading | permissive throughout |
| **Retrieval + memory** | `qdrant` (Apache-2.0) with payload filters on curriculum code; `mem0` (Apache-2.0) for learner state | permissive |
| **Serving** | `vllm` or `ollama` where sovereign/local inference is required (`intel/trends.md` **T6**) | permissive |
| **LMS seam** | `ltijs` (Apache-2.0) over LTI 1.3, or the Moodle community MCP servers (`compose/patterns.md` **P11**) | permissive tool, platform untouched |
| **Review console** | `appsmith` (Apache-2.0) for human review of flagged citations | Apache-2.0 |

### How it wires together

1. **The spine is the only source of curriculum truth.** The agent never emits a curriculum code or
   objective text from model memory. Codes are keys (`EF67LP08`, `EM13LGG103`, `EI02TS01`) resolved
   through MCP or the API, and every response carries the per-record source the dataset ships.
   `bncc-dados`'s own `llms.txt` states this contract — **use official codes as keys, never invent
   codes or skill texts, cite the source attached to each record** — so the contract is adopted, not
   invented.
2. **Two MCP paths, deliberately.** `dfdb76/bncc-mcp` and the `bncc-pacotes` worker are
   independently maintained over the same data; the packages embed the data and **work offline**.
   Pin a commit and vendor the JSONs — availability of the hosted endpoint is never on the critical
   path.
3. **The gate runs in CI, not at the end.** Fork `bncc-benchmark`'s MIT `harness/`, point it at the
   client's curriculum records and the model the engagement actually ships, and run it per release.
   Two thresholds, agreed with the client in writing: **minimum faithful-text rate** and
   **maximum fake-code acceptance**, the second strict (the published range reaches 0%, so 0% is a
   defensible target for a *grounded* system — the benchmark measures ungrounded recall, and
   grounding is precisely what this pattern adds).
4. **Flagged citations go to a human**, through the Appsmith console, with the record and source page
   attached. That queue is also the audit artefact a regulator asks for.
5. **Attribution ships in the product.** CC BY 4.0 on the data means the UI component that renders
   curriculum references carries the credit. Put it in the sprint that builds that component.

### The design rules that make it defensible

- 🔴 **Never let the model be the source of a curriculum code.** Retrieval-grounded or refused —
  there is no third behaviour, and the 42% figure is why.
- 🔵 **Measure two things, not one.** Faithfulness and refusal are separate metrics with separate
  thresholds. A single "accuracy" score hides the dangerous failure.
- 🔵 **Re-run the vendor's benchmark rather than citing it.** `bncc-benchmark` is published by the
  same organisation that maintains the dataset and the hosted endpoint whose grounding it reports as
  fixing the problem. The raw responses and methodology are public and the harness is MIT, so the
  honest use is **replication**, and saying so to the client is a credibility gain, not a loss.
- 🟡 **This pattern proves grounding, not pedagogy.** It says the system cites the curriculum
  correctly. It says nothing about whether anyone learned more — that is **P7**, and this KB's
  standing finding that there is no credible primary evidence of learning-outcome gains at scale is
  untouched by anything in this pattern.

### Deliverables

- A grounded curriculum tool surface (MCP + API) over the client's curriculum, offline-capable.
- A two-metric hallucination gate wired into CI, with thresholds agreed in writing.
- A human-review queue for flagged citations, doubling as the audit trail.
- A licence register recording the **CC BY attribution obligation** and any **reserved mark**
  (gate `904-G1`, trend **T27**).
- Replication report of the benchmark on the client's own curriculum and model.

### Estimate

| Phase | Work | Duration |
|---|---|---|
| 0 | `G1` + `904-G1` licence pre-flight on the curriculum dataset **and its payload directory** | 2–4 days |
| 1 | Spine adoption: vendor the records, pin the commit, stand up MCP locally | 1–2 weeks |
| 2 | Grounded retrieval + citation rendering with attribution | 2–3 weeks |
| 3 | Hallucination gate: fork the harness, set thresholds, wire to CI | 1–2 weeks |
| 4 | Tutor tier over the spine (DeepTutor or OpenMAIC), review console | 3–4 weeks |
| | **Total to first measured pilot** | **7–11 weeks** |

🔵 **Cheaper than P22 by design**, because the expensive part of P22 — authoring the corpus — is
already done and licensed. **Where the curriculum is not published as data, run P22 first and P23
after**; the two compose, and `bncc-dados` is the specification P22's phase 5 should aim at.

### Where it does not apply

- 🔴 **Where no published, verifiable curriculum exists.** If the "curriculum" is a PDF with no
  stable identifiers, there is nothing to key on — that is P22.
- 🔴 **Where the curriculum's own texts are under restrictive copyright.** Brazil's case works
  because BNCC normative texts are **official state acts and not copyrightable** (art. 8º, IV, Lei
  9.610/1998) and the CC BY grant covers only the compilation. **That analysis is jurisdictional and
  must be redone per country** — in several it will come out the other way, and then the corpus is a
  licensing negotiation before it is an engineering task.
- 🟡 **Outside Brazil there is currently no equivalent dataset to adopt.** `p904` searched:
  `currículo nacional dados abertos` returns nothing at or above 3 ★ in Spanish or Portuguese. Treat
  `bncc-dev` as a **template**, not as a dependency with regional equivalents waiting.

## P24 — Rebuildable handover tier: the licence inventory and pinned build no upstream will give you (added `p905`)

### Why this pattern exists

Measured `p905`: of the 14 platforms an education engagement is built on, **`0` disclose the grants of
their dependencies**, and the two most-starred education agents in existence cannot be rebuilt from
their own manifests (`DeepTutor` pins 1 of 74; `OpenMAIC` ships no lockfile). Meanwhile the
procurement specifications in **T9** and the exit requirements in **P8** both demand exactly what is
missing: *what is in this, and can we rebuild it without you.*

🔵 **This is not a pattern you sell on its own — it attaches to P1–P11 as a priced tier**, the same
way **P7** (evidence-of-efficacy) does. It is the cheapest credibility a studio can add to an
education proposal, because the client's audit will ask for it either way and no competitor bidding
the same open base will have it.

### Stack

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| Dependency-grant scanner | https://github.com/aboutcode-org/scancode-toolkit | 🟡 SPDX `NOASSERTION` → 🟢 **Apache-2.0** byte-read (`develop/apache-2.0.LICENSE`, 11,357 B) | 2,676 ★, pushed 2026-11-11. The industry-standard scanner; resolves direct **and** transitive grants. Retrieved for exactly this purpose at `p531`. 🔵 Its own `NOASSERTION` is a `T19` instance — read the file, not the badge |
| SBOM emitter | https://github.com/CycloneDX/cyclonedx-cli | Apache-2.0 (11,341 B) | 563 ★, pushed 2026-10-19. Emits the format procurement offices accept; pairs with the scanner's output |
| Python pinning | `pip-compile` (https://github.com/jazzband/pip-tools) **or** https://github.com/astral-sh/uv | BSD-3-Clause (1,522 B, byte-read) / Apache-2.0-or-MIT | `uv` is 92,203 ★, pushed 2026-11-18 — use it for speed on a 74-package tree with 36 upper bounds. 🔵 `pip-tools` is **absent from `repo:` search and `200` on `raw@main`**: apply the `905-F6` test — one query against a suspected new name — before recording either as missing |
| Node pinning | `npm ci` against a committed `package-lock.json` | — | Required for Canvas (348 npm) and OpenMAIC (178 npm), neither of which ships a lockfile on the paths probed |
| PHP / Java | `composer.lock` (already present) / Maven `dependency:tree` + `versions:lock-snapshots` | — | Moodle and Gibbon already pin; Sakai and OpenOLAT need the tree captured |
| Vendoring target | the client's own registry or a git mirror at a SHA | — | `p110`: 200 of 296 shelf rows are one maintainer, so the artefact must survive upstream disappearing |

### How it wires together

1. **Resolve once, deliberately.** Build the chosen base in a clean container, capture the resolved
   set, commit it as a lockfile in the client's repository. For `DeepTutor` this means following the
   `-r` chain to the 19 `requirements/modules/*.txt` leaves first (gate `905-G1`, rule 2) — the root
   manifest shows nothing.
2. **Scan the resolved set, not the manifest.** Point `scancode-toolkit` at the installed tree. The
   manifest names 311 or 74 packages; the resolved tree is where the copyleft and the
   non-commercial surprises actually live, and it is the only artefact that answers the audit.
3. **Emit the SBOM in CycloneDX**, attach the scanner's licence inventory, and flag three classes by
   hand because no tool reports them correctly: **per-directory grants** (the directory axis of `G1`, added `p897` / **T24**),
   **data-and-content grants** (`904-G1`/**T25**), and **reserved marks** (**T27**).
4. **Write the two known scanner false positives into the handover note before the audit runs them.**
   `OpenOLAT`'s `LICENSE` is a truncated Apache-2.0 (10,982 B vs 11,358 B canonical) and `DeepTutor`'s
   is hand-edited (`560-D`). Both are **Apache-2.0 on a clause read** and both **will** be flagged by
   a byte-identity check. An explained flag is a non-event; an unexplained one stops a deployment.
5. **Pin the rebuild in CI.** A job that rebuilds from the lockfile and fails on drift. `p111` found
   38.9% of this shelf has a live CI signal and `p112` that only 21.3% is both checked and pinned —
   this step is what moves the client's own estate into that 21.3%.

### Deliverables

- A lockfile or resolved manifest committed in the client's repository, and a container build that
  reproduces it byte-for-byte.
- A licence inventory over the **resolved** tree, with the three hand-checked classes above.
- A CycloneDX SBOM.
- A one-page handover note naming the known scanner flags and why each is benign.
- A CI job that fails on dependency drift.

### Licence posture

Every instrument in the stack is **Apache-2.0, BSD-3-Clause or MIT**, so the tier itself adds no
licence obligation to the client's product — which matters, because its whole purpose is to be the
artefact the client's legal review trusts.

### Estimate

**1.5–2.5 weeks** for a single base, including the hand-checked classes and the CI job. Add **1 week**
if the base is unpinned *and* multi-ecosystem (Canvas: npm + gems; Moodle: composer + npm). 🟢 Reuse
across engagements is high — the scanner configuration, the three hand-check classes and the handover
note template are the same for every client on the same base.

### Where it does not apply

🔴 If the client is consuming a **hosted** platform rather than deploying one, there is no tree to
scan and this tier is theatre — sell **P8** (metering, attribution and exit) instead. 🔴 And if the
engagement's base is already pinned and single-ecosystem (`openedx/openedx-platform`: 311/311, Python
only), the pinning half is already done — scope the scan alone, at roughly half the estimate, and say
so rather than billing for work upstream has done for you.

## P25 — Chinese-curriculum grading and item-bank tier, assembled from the Mandarin cohort with the AGPL kept out of the deliverable (added `p906`)

### Why this pattern exists

Every pattern above the grading tier assumes the item bank and exam delivery already exist. For a
China or Chinese-curriculum engagement they do — and until `p906` this KB could not name them,
because `repos/foundations.md` held the entire `Assessment, grading and academic integrity` tier as
North American and European across twelve verified rows while the Mandarin channel `作业 批改`
returns **347 repositories**. **P17** is the equivalent pattern over a BSD autograder for code and
structured answers. **P25 is for prose, handwriting and mathematics on paper**, which is what the
Chinese cohort is actually built for and what P17's substrate cannot mark.

🔴 **The pattern's real work is licence routing, not integration.** The cohort is mixed in a way
that matters: of the twelve repositories verified, **five are MIT, two are Apache-2.0, three are
AGPL-3.0 and two are Mulan PSL v2** — and the single most useful-looking item in the channel
(`MathCyclus`, **156 ★**, OCR → LaTeX → TikZ maths item bank) **carries no licence file at all** and
is barred. A studio that reads this cohort as "Chinese open source, permissive enough" ships AGPL
into a client's closed product. The routing below is the deliverable.

🔵 **And one row inverts the usual scanner result.** `nengdou-ai-review-helper-web` (**193 ★**) is
labelled `MulanPSL-2.0` by GitHub and is **verbatim Apache-2.0 on a byte read** (11,356 B,
`sha256₁₂ 43070e2d4e53`). **An SPDX-driven gate rejects the best repository in the tier for a
restriction that does not exist.** Run `G1` before this pattern, not after — see gate `906-G1`.

### Stack

| Layer | Component | Licence posture |
|---|---|---|
| **Item bank + exam delivery** | https://github.com/yf-team/yf-exam-lite (**MIT**, 173 ★, byte-read `main/LICENSE` 1,074 B `sha256₁₂ b4cf55353a49`) — bank and item management, bulk import/export, automatic paper composition, wrong-answer drilling, enrolment, scoring | ✅ MIT. **Deliberately not an AI project**, which is why it is the spine: take the schema and exam delivery, add generation. 🟡 Idle since 2025-05-07 — **fork and own it**; treat it as a data model, not a live dependency. |
| **Offline/local item authoring** | https://github.com/BBkjdayup/BCTK (**MIT**, 58 ★, byte-read 1,065 B `sha256₁₂ 7208c5cd9088`) — Windows desktop bank + paper composer, local-by-default storage, maths formulae, Word/Excel import-export, duplicate-question detection | ✅ MIT. The **local-first** tier: no student data leaves the machine, so no data-processing argument is needed. |
| **Marking engine (prose + handwriting)** | https://github.com/yinuoguan/nengdou-ai-review-helper-web (**Apache-2.0 on byte read**, 193 ★) — multi-subject marking with written feedback; and https://github.com/QwenStorm/xl-frontend (**MIT**, 50 ★) for **essay marking + OCR** of handwritten work | ✅ Apache-2.0 (patent grant) + MIT. 🔴 **Record the byte read in the SBOM**, or the client's own scanner will flag `nengdou` as Mulan. 🟡 `xl-frontend` was created and last pushed the same day — read the pipeline, do not depend on the repo. |
| **Error → targeted practice loop** | https://github.com/shellery1988/k12-smart-teacher (**MIT**, 16 ★, byte-read 1,073 B `sha256₁₂ 4c5f6e74a09b`) — wrong-answer analysis and generation of fresh analogous items from the specific error made (举一反三) | ✅ MIT. **The pedagogically load-bearing step** and the one every other grading row in this KB stops short of. Small — reimplement the loop, vendor nothing. |
| **Reliability signal** | The dual-agent parallel-review control read from https://github.com/ai-lingnan/econai-agent-platform (**AGPL-3.0**, 41 ★) | 🔴 **AGPL — read, do not link.** Reimplement: two independent marking passes over one submission, disagreement above threshold routes to a human. **Design, not dependency.** |
| **Item-bank-as-a-skill (optional)** | https://github.com/weishao2/tizhuang-agent-skills (**MIT**, 42 ★) — question sampling and knowledge-point retrieval exposed as an agent skill | ✅ MIT **on the skill**. 🔴 The bank itself is a **hosted third-party service**: the MIT grant does not cover availability, terms or the claimed 20M items. Contract for it separately or do not depend on it. |
| **Reasoning trace (optional)** | https://github.com/PGshen/thinking-map (**Apache-2.0**, 187 ★) | ✅ Apache-2.0, patent grant. Externalises the marking rationale as a navigable graph — the appealability surface a parent or regulator asks for. |
| **Platform reference (do not ship)** | https://github.com/youufis/SmartKBS (**AGPL-3.0**, 99 ★, pushed 2026-11-18) | 🔴 **AGPL.** The most complete single implementation of this whole tier — bank, papers, marking, live classroom, attendance, analytics. **Read it as the reference architecture; deploy-and-extend only.** A closed branded derivative is not available. |
| **Pre-flight** | `G1` licence gate, with the branch-resolution step | 🔴 **Four of the twelve cohort repos default to `master`.** A `main`-only probe reports them unlicensed — this is `884-G2`, discharged in `p885` and **recurring in `p906`'s own instrument** (`906-G3`). Resolve the default branch from `search/repositories` *before* reading bytes. |

### Wiring

1. **Fork `yf-exam-lite`** and keep only the item schema, bank CRUD and exam-delivery paths. This is
   the system of record. Nothing AI touches it yet.
2. **Put the marking tier behind a queue, not inline.** A submission produces a *marking job*;
   `nengdou`'s pipeline (Apache-2.0) and `xl-frontend`'s OCR path handle prose and handwritten work.
   Two independent passes per submission, per the `econai` control reimplemented.
3. **Gate on disagreement, not on confidence.** Where the two passes differ by more than the agreed
   band, the submission routes to a teacher. This is the only cheap, defensible reliability proxy in
   the tier, and it is what a human-in-the-loop requirement can actually trigger on.
4. **Feed every confirmed error into the `k12-smart-teacher` loop** to generate analogous practice
   from the specific mistake, written back as new items in the forked bank — so the bank grows from
   real student error rather than from generation alone.
5. **Expose the marking rationale** through a `thinking-map`-style graph. Appealability is a
   requirement in every jurisdiction this KB tracks, and a mark without a rationale is not appealable.
6. **For a local-only client, substitute `BCTK`** for steps 1 and 4 and run the model locally. The
   result needs no cross-border data-processing argument at all.

### Licence posture of the result

🟢 **Shippable closed.** The deliverable touches MIT and Apache-2.0 only. The two AGPL components
(`econai-agent-platform`, `SmartKBS`) are **read as designs and reimplemented**, which is the same
discipline P15 and P14 apply, and the two Mulan PSL v2 repositories are not in the build path.
🔴 **Two things must be written into the SBOM by hand**: the `nengdou` byte read (or the client's
scanner will report a Mulan dependency that is not there), and the fact that `MathCyclus` was
**evaluated and barred for having no grant** — because it is the first thing a competent reviewer
will find in this channel and the first thing they will ask why you did not use.

### Estimate

**8–12 weeks.** The spine is a fork, not a build, and the marking pipelines are readable. The cost
sits in three places: **Chinese-language QA** (the cohort's documentation, tests and UI are in
Chinese — budget a Mandarin-reading engineer, not a translator); **reimplementing the two AGPL
controls** cleanly enough to survive a provenance question; and **the handwriting OCR accuracy bar**,
which is the one place this pattern can fail outright and which no repository in the cohort
publishes a measurement for. 🔴 **Measure OCR accuracy on the client's own scanned work before
committing to the handwriting scope** — that is this pattern's equivalent of P23's hallucination
gate, and the cohort gives you no published number to rely on.
