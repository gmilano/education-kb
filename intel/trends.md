---
industry: education
region: Global
updated: 2026-10-31
---

# Current trends — education AI

<!-- machine-readable count claim, p570, for ingest/derive-counts.py -->
`derived trends: **24**` — numbered trend headings on this page, counted with
that gate's own regex.

🔴 **`p573` corrects this claim twice over, and the second correction is a defect,
not a stale number.** The claim read **15**; the regex counts **24**. 🔴 **The
difference is not drift — it is a numbering collision: trends `15`, `16`, `17` and
`18` are each used *twice on this page for different trends*.** The `p572` block
at the top opened a new series at 15 (permissive supply in the plumbing;
source-available licences; lesson-planning as agent skill; self-reported metrics)
while the body already carried a 15–18 on entirely different subjects (vocabulary
artefacts; findings not reaching the shelf; tag variants; the verification
command). 🔵 **So `24` headings express only `20` distinct trend numbers, and four
of those numbers are ambiguous references.** 🟢 `p573`'s own additions are
numbered **19** and **20**, which were free. 🔴 **A citation to "trend 16" on this
page currently resolves to two different claims — anything referencing 15–18
should name the subject, not the number, until the series is renumbered.**

Confidence is stated per trend. Where a trend was **measured first-hand** from
GitHub's own index rather than read from a source, that is said explicitly —
those are the most reliable items on this page and the least likely to appear
anywhere else.


## `p572` (2026-10-31) — trends 15–18

### 🟢 15. The permissive supply in education is in the *plumbing*, not the platforms

🔵 Every full education platform of any scale is copyleft — Moodle GPL-3.0,
Open edX AGPL-3.0, Canvas AGPL-3.0, ILIAS GPL-3.0, ERPNext GPL-3.0, Gibbon
GPL-3.0, RosarioSIS GPL-2.0, Odoo/OpenEduCat LGPL-3.0 — with **two** exceptions
now on the shelf: **Sakai (Apache-2.0)** and, found this pass, **Artemis (MIT)**.
🟢 **But the integration layer is almost entirely permissive**: LTI 1.3 in Python
(**MIT**) and PHP (**Apache-2.0**), the xAPI store (**Apache-2.0**), Open edX's
component framework (**Apache-2.0**), Canvas MCP (**MIT**).

🔵 **The trend to state to a client: you do not win the licence argument by
choosing a different platform, you win it by never forking the one they already
run.** The permissive supply is positioned exactly where integration happens,
which is also where the billable work is.

### 🔴 16. "Open source" in education increasingly means a bespoke source-available licence

🔴 Three of this pass's higher-star education finds are **not** open source
despite reading that way: **`CaviraOSS/PageLM`** (2.1k★) ships a bespoke
*"PageLM Community License"* — non-commercial, redistribution **prohibited**,
commercial use gated behind a **revenue-sharing agreement**, and **revocable**;
**`xiaoyang111222/cn-math-taxonomy`** (5.6k★) is **CC BY-NC 4.0**; and
**`chewyenhan/malaysia-uec-teacher-workflow`** puts its substance under
**CC BY-NC-SA 4.0** while the MIT covers only `scripts/` and `tests/`.

🔵 **The pattern is consistent: the code is given away and the *content* is
withheld** — wordlists, knowledge graphs, item banks, audio. In education the
content *is* the product, so a content carve-out is a commercial block even when
the repository is genuinely generous with its code. 🔵 **Read the content licence
before the code licence in this industry.**

### 🟢 17. Teacher lesson-planning tooling is being built as an agent *skill*, by teachers, outside the anglophone web

🟢 `topic:lesson-plan` holds **44** repositories — small enough that nine passes of
star-sorted sweeping never reached it — and its content is striking: these are
Claude Code / Cowork / DSH **plugins and skills**, not applications, written
largely in Chinese and Malaysian-Chinese school contexts, converging independently
on the same feature chain: **lesson plan → courseware → item bank → dictation →
marking**.

🟢 **One of them states a property no commercial vendor leads with:
`全程本机运行，不联网、不收集数据` — runs entirely locally, no network, no data
collection.** 🔵 That is the single most common blocker in school procurement
being treated as a headline feature, by a 2★ repository, three days old.

### 🔴 18. Self-reported repository metrics are the weakest evidence in this KB, and the fix is cheap

🔴 Carried forward from `570-A` and now reinforced: **stars and commit counts are
claims a repository makes about itself.** `570-A` caught a `2,137`-commit
synthetic history; this pass found the opposite failure mode — **`arthurflor23`
shows `3,642/3,645` author-date-equals-committer-date across a genuine 7.4-year
project**, so that check *alone* flags honest repositories that push directly
rather than merge pull requests.

🟢 **The signals an author cannot unilaterally manufacture are the licence text,
the dependency manifest, and the behaviour of the code.** This pass read `28`
grants and `7` dependency manifests byte-for-byte and found **three** commercial
blocks and **one** GPL-3.0 licence surface hiding behind a clean MIT file — none
of which any star or commit figure would have shown.

## `p573` (2026-10-31) — trends 19–20

### 🟢 19. The psychometric measurement layer splits by **programming language**, not by quality — permissive in Python, copyleft in R (high confidence — measured first-hand, 20 grants read byte-for-byte)

🔵 **The observation.** Education AI's assessment work needs item calibration,
DIF, equating and adaptive item selection. Those algorithms exist twice over in
open source — once in Python/JVM, once in R — and **the two populations have
almost disjoint licensing.**

| tier | grants read this pass | result |
| --- | --: | --- |
| 🟢 Python / JVM | 9 | 🟢 **MIT ×5, Apache-2.0 ×2, BSD-3 ×1** (+1 ungranted) |
| 🔴 R / CRAN | 12 | 🔴 **GPL-family ×11, LGPL ×1** |
| 🟢 R, permissive exception | 1 | 🟢 **`OpenMx/OpenMx` — Apache-2.0** |

🔴 **Why this is a trend and not a coincidence.** It follows the two communities'
distribution channels. **CRAN's culture and its dominant packages are GPL**, and
an R package that wants to depend on `mirt` or `TAM` inherits that; **PyPI has no
such centre of gravity**, and the education-ML packages were published out of
labs that default to MIT. 🔵 **Neither community chose this with a commercial
deliverable in mind, and that is exactly why it catches engagements late.**

🔴 **The consequence is not symmetric, because the two tiers are not
interchangeable in *evidentiary* terms.** `mirt`, `TAM`, `sirt` and `GDINA` are
the implementations **exam boards, ministries and peer reviewers accept**. The
permissive Python tier is good code with less standing in a psychometric report.
🔴 **So the licence boundary and the credibility boundary run in opposite
directions** — the code you may ship is the code your client's statistician
trusts least.

🟢 **Prediction, falsifiable next pass:** this split will hold for any
measurement-adjacent axis where the academic practice lives in R —
check `topic:structural-equation-modeling` and `topic:meta-analysis`. 🔵 If either
returns a majority-permissive population, this trend is weaker than stated.

🟢 **What to do with it:** `P-575-A` (permissive Python-only calibration
pipeline) and `P-575-B` (arm's-length GPL psychometrics service) write up the two
postures. Choose on the first day of the engagement, not after the statistician
has picked their tooling.

### 🔴 20. The commonest licence failure in education AI is **no licence at all**, and it concentrates in peer-reviewed academic code (high confidence — measured first-hand, 26 repositories)

🔵 **The measurement.** Of **26** repositories whose grants were read
byte-for-byte this pass, 🔴 **7 (27 %) have no licence file of any kind** on
`HEAD` — not `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING`.

🔴 **And they are not the abandoned toys. They are the published research:**

| repo | standing | grant |
| --- | --- | --- |
| [bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) | **AAAI 2025**, 100★ | 🔴 **none** |
| [meyerjp3/psychometrics](https://github.com/meyerjp3/psychometrics) | 114★ Java CTT/IRT library | 🔴 **none** |
| [kervias/DCD](https://github.com/kervias/DCD) | **NeurIPS 2023** | 🔴 **none** |
| [CSLiJT/HCD-code](https://github.com/CSLiJT/HCD-code) | **SIGKDD 2022** | 🔴 **none** |
| [ShawnYu98/RDGT](https://github.com/ShawnYu98/RDGT) | **TKDE 2024** | 🔴 **none** |
| [inuyasha2012/vipsy](https://github.com/inuyasha2012/vipsy) | IRT/CDM variational inference | 🔴 **none** |
| [Mr-nnng/ICD](https://github.com/Mr-nnng/ICD) | interpretable CDM for ITS | 🔴 **none** |

🔴 **The inference this field keeps making, and it is wrong: that peer review
implies permission.** A paper at NeurIPS or SIGKDD licenses nothing. **Code with
no grant is exclusively copyrighted** — readable, reimplementable, **not
shippable**. 🔵 The methods are published and free to reimplement from the paper;
the *repository* is not free to vendor.

🔴 **Why this bites harder in education than elsewhere.** The state of the art in
learner modelling, cognitive diagnosis and knowledge tracing **is** academic
code — there is no industrial alternative to fall back on, the way there is for,
say, web frameworks. 🔴 **So "the best available implementation" and "an
implementation you may use" diverge systematically in this industry.**

🟢 **Operational rule, cheap and now proven on this harness:** read the grant
bytes before a component enters a deliverable, and treat a missing file as a
**hard stop**, not a question to resolve later. 🟢 **One `raw.githubusercontent.com`
probe settles existence and grant together** (trend 18's channel), 🔴 **while the
`curl -sI https://github.com/…` check this base is instructed to use returns `403`
for real and invented repositories alike on this session — it cannot discriminate,
and it fails in the unsafe direction.** `P-573-B` is the gate; this trend is the
measured reason it is needed.

🟢 **Second-order finding worth carrying to every industry base here: a licence
*ladder* that probes filenames will never find an R package's grant, because R
declares it in `DESCRIPTION`.** 🔴 **That single convention gap made `12` GPL
packages look ungranted.** A per-ecosystem manifest check (`DESCRIPTION`,
`pyproject.toml`, `Project.toml`, `*.gemspec`, `Cargo.toml`) belongs in the
instrument, not a longer list of filename variants.


## 1. Education AI has stopped shipping as applications and started shipping as agent skills (high confidence — measured first-hand)

**Measured, not reported — and this pass the measurement is complete.**
`topic:agent-skills topic:education stars:>50` returns **13 repositories**, the
**same count as the previous pass**, so that axis is genuinely saturated. What is
new is that the previous pass reported only the leader; this pass enumerated all
thirteen and **read every one of their licence files** over
`raw.githubusercontent.com`. **Nine of the nineteen** agents on
[`../agents/top.md`](../agents/top.md) are skill bundles — markdown instruction
sets (`SKILL.md`, `AGENTS.md`, `CLAUDE.md`) loaded by an existing harness, with
**no runtime, no service and no API**; counting six further component bundles,
**15 of the 25 agents on that page have no runtime at all.** The complete cohort:

| Repo | ★ | Licence (read first-hand) | What it is |
| --- | --: | --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 4,843 | ⛔ **CC BY-SA 4.0** (620 B) | 23,000+ skills for empirical research across 8 social-science disciplines; CoPaper.AI / Stanford REAP |
| [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | 2,750 | ⛔ **none** — no file on either branch | Brazilian study-mentor agent bundle; runs on 5 named harnesses |
| [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | 1,201 | ✅ MIT | PDFs/books/papers → traceable interactive learning pages |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 586 | ⚠️ **AGPL-3.0**, `skills/` **dual AGPL/MIT** (1,063 B, `master`) | K-12→career skill tree, 30+ skills, ships an MCP server |
| [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | 295 | ✅ MIT | Bloom's 2-sigma as a skill **plus** a self-hostable app |
| [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 213 | ✅ MIT | Chinese civil-service exam prep |
| [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | 203 | ✅ MIT (1,065 B) | Project-driven mastery learning |
| [ystemsrx/sql-to-ER](https://github.com/ystemsrx/sql-to-ER) | 192 | — **not an education agent** | SQL/DBML → ER diagrams; tagged `education` because it is used in database courses. Topic-tag dilution. |
| [cuic19053-hue/awesome-student-ai-skills](https://github.com/cuic19053-hue/awesome-student-ai-skills) | 147 | ✅ MIT (1,070 B) | 35 Chinese university application-document skills |
| [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | 119 | ✅ MIT (1,068 B) | Teaching/tutoring skill collection incl. *gaokao* |
| [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | 78 | ✅ MIT (1,063 B) | Montessori pedagogy as a skill |
| [ljx-chase/research-field-onboarding](https://github.com/ljx-chase/research-field-onboarding) | 75 | ✅ MIT (1,111 B) | Onboarding a learner into an unfamiliar research field |
| [henryyu333/assignment-check](https://github.com/henryyu333/assignment-check) | 53 | ✅ MIT (1,086 B) | Pre-submission check against brief, rubric, evidence, citations |

**The distribution is the finding: 11 MIT, 1 share-alike, 1 unlicensed, 1
dual-grant — and the two non-permissive members are the two largest, at 4,843★
and 2,750★.** In this cohort **popularity is anti-correlated with licence
usability**. The previous pass asserted something close to this from two data
points; it is now measured across the whole cohort with a denominator. Add the
**932★** `GarethManning/education-agent-skills` — 165 evidence-grounded skills for
teachers and school leaders, **also CC BY-SA 4.0**, read first-hand — and the
pattern is no longer an instance: **authors of large pedagogical skill libraries
reach for CC licences, because the artefact reads as writing.** The consequence is
fixed and worth saying in a SoW: the best-curated pedagogy content in open source
**cannot be absorbed into a proprietary methodology asset.**

**Why this matters more than it looks.** Three consequences for an engagement:

1. **There may be nothing to host.** The deliverable is a prompt contract. That
   collapses infrastructure cost and collapses the recurring-revenue story with
   it. Price the authoring and the maintenance, not the running.
2. **Versioning and evaluation become the hard problems.** A skill bundle has no
   semver discipline, no test suite by convention, and changes behaviour when the
   *harness* or the *model* changes underneath it — neither of which the client
   controls. This is the strongest argument for the evaluation layer in trend 7.
3. **Licence screening gets harder, not easier.** The largest member of the
   cohort is **CC BY-SA 4.0** — a share-alike *content* licence on a code-shaped
   artefact, which propagates to derivatives of the skill text. The
   second-largest has **no licence at all**. A skill bundle looks like
   documentation and is governed like a work of authorship.

The cohort is also **overwhelmingly APAC-origin** (six of the eight above are
Chinese-language or China-maintained), with a Stanford exception at the top and a
Brazilian one in second place.

## 2. From experimentation to governance (high confidence — every source agrees)

The consistent framing across industry sources: AI moves from standalone pilots
into admissions, advising, learning and administration as embedded
infrastructure. HolonIQ expects attention to shift to ethics, transparency,
agentic use cases and *proven instructional benefit* over broad personalisation
promises; 1EdTech frames it as evolving from isolated use cases to coordinated,
policy-guided ecosystems. The hard numbers behind it are in
[`market.md`](market.md): 87/26 in LATAM, 63% teacher use in EMEA, 60% in the US,
7-of-39 operational governance in Australia. **The gap between use and governance
is the market.**

## 3. Purpose-built beats general-purpose (high confidence)

Vendors and analysts converge on movement away from generic assistants toward
platforms built for education. This KB's own evidence agrees from the supply
side: the two largest education agents in the world are **purpose-built
education** projects from universities (DeepTutor/HKU, OpenMAIC/Tsinghua), not
education wrappers on general agents — and the prescribed "top open source AI
agents education" search returns only general-purpose listicles, i.e. the
*commentary* layer still has no education-specific map while the *code* layer
clearly does.

## 4. The compliance calendar and the capability calendar have come apart (high confidence — re-verified independently, and extended)

The previous pass recorded this correctly and in detail; this pass **re-verified
it from fresh sources and added two things it did not have.** The table stands:

| Regime | Status on 2026-10-31 |
| --- | --- |
| EU AI Act — **Article 4 AI-literacy duty** | **In force since 2025-02-02** for every organisation that *uses* an AI system — i.e. every school and university, now, already overdue where nobody has done it. Not risk-classified, not deferred ← *new this pass, and the earliest of the three EU tracks* |
| EU AI Act — **Article 50 transparency duties** | **Not deferred. In force since 2026-08-02** |
| EU AI Act — stand-alone Annex III high-risk (incl. education) | Deferred to **2027-12-02** by the Digital Omnibus amendment, in effect late July 2026 |
| EU AI Act — AI embedded in regulated products | Deferred to **2028-08-02** |
| EU — **Article 50 marking of synthetic content, systems already on the market** | **2026-12-02** — machine-readable marking/watermarking of AI-generated output. **The nearest EU deadline in this KB, roughly one month out**, and 13 months earlier than the Annex III date most guidance leads with ← *new on the fifth pass, multi-source* |
| EU — AI-generated intimate imagery / abuse material ban | ⚠️ **Still single-source, and not corroborated on the fifth pass.** Carried as "December 2026". The December 2026 EU date that *does* corroborate from several sources is the Article 50 marking deadline above; the two may have been conflated upstream. Treat as unverified |
| **Council of Europe** — Legal Instrument on AI in Education | **Planned for 2026**, "establishing rules to protect the integrity of education"; follows a 2025 recommendation. Binds by ratification across 46 states, so it reaches non-EU Europe ← *new this pass, single-source* |
| North Carolina **Session Law 2026-41** | State model policy **2026-12-31**, district policies **2027-06-30**, teacher training **2028-06-30** ← *new this pass; the nearest statutory deadline in this KB* |
| South Korea AI Basic Act | **In force 2026-01-22** — and the **Enforcement Decree entered into force the same day**, correcting this table's earlier "decrees pending". The grace is on *penalties*: **fact-finding and fines suspended for ≥1 year from 2026-01-22**, except extreme cases such as loss of life. Education named **high-impact**, specifically *evaluation of students in early childhood, elementary and secondary education* ← *corrected and sharpened on the fifth pass* |
| Vietnam AI law | Law **No. 134/2025/QH15**, **effective 2026-03-01**. The high-risk list is **Decision 33**, effective **2026-08-15**: **46 systems across six sectors**, with **three** in education — (1) automatic **testing/evaluation/ranking** of learners, (2) **monitoring and analysis of learner behaviour**, (3) **self-study tools generating content from uncontrolled data sources**. Existing education systems transition to ≈**2027-09-01** ← *instrument named and categories enumerated on the fifth pass* |
| Australia (TEQSA) | Institutional generative-AI action plans required of **all** higher-ed providers — **100% response rate achieved** |

**What is new.** First, the postponement is attributed by multiple independent
legal commentaries to **Regulation (EU) 2026/1744**, in force 27 July 2026 after
Council approval on 29 June 2026 — a citeable instrument, where the previous pass
had only "the Digital Omnibus amendment". Second, and more useful commercially:
**Article 50 transparency duties were not part of the deferral** and have applied
since **2 August 2026**. The calendar therefore has *two* tracks, and conflating
them misprices the work in both directions: **transparency obligations are live
today; conformity assessment is ~14 months out.**

**Widely-repeated error to avoid, restated because it is still in circulation:**
guidance claiming EU high-risk obligations apply from August 2026 was superseded.
Enforcement *machinery* (the AI Office and national authorities) did begin on
2 August 2026 — which is probably the source of the confusion — but the high-risk
*duties* did not.

**Two further changes this pass, and one of them merges two markets into one
programme.** Vietnam's 18-month transition for systems already running in
education expires around **1 September 2027** — within three months of the EU's
Annex III date of **2 December 2027**. The two most binding education-AI
deadlines in the world now land in the same quarter, so a multinational client
needs **one** conformity programme with two annexes, not two programmes. And the
calendar is no longer only EU-plus-Asia: **North Carolina's Session Law 2026-41**
carries the nearest deadline in this KB at **31 December 2026**, two months out,
followed by district policies in June 2027 and teacher training in June 2028 — a
statutory three-stage pipeline that writes its own engagement plan.

Meanwhile the capability calendar runs on weeks: OpenMAIC went from repository
creation (2026-03-11) to 41,984★ and `v1.3.0` in under eight months, and
`DozenTwelve/Papermorph` took **1,034★ in four weeks**. Capability deadlines in
Asia still land before Europe's.

## 5. Adoption is ahead of governance, and it is now measured on all four regions (high confidence)

Previously high-confidence only in LATAM. Now:

- **LATAM** — UNESCO IESALC/UNU-IAS, 200 institutions, 19 countries: **87%** use,
  **26%** strategy, **55%** no budget, **4%** dedicated funding at public
  universities. Cetic.br: Brazil **53%** of administrators use AI, **22%** have
  guidelines. Ceibal: **75%** of Uruguayan public-school teachers.
- **EMEA** — **63%** teacher use, from two independent surveys that agree exactly
  (European Commission School Education Gateway, April 2026, n=1,130; Sanoma
  Learning, 20,000+ teachers, 14 countries). Eurydice's *Digital education at
  school in Europe 2026* is the member-state source.
- **North America** — **60%** of US teachers (Gallup); most public schools have no
  formal student AI policy; **134** state bills across **31** states; **42.3%** of
  Ontario boards have a student AI policy.
- **APAC** — now primary: TEQSA's **100%-response** institutional census, and
  operational governance structures documented in only **7 of 39** Australian
  universities (AJET). MEXT's pilot covers **478 schools** in **149
  municipalities** — under **2%** of Japanese schools.

## 6. Mandated content without teacher buy-in fails, and there is now a measured case (medium-high confidence — single country, strong detail)

**South Korea's AI textbooks reached below 30% adoption by March, and lawmakers
subsequently removed their official status.** This is the first instance in this
KB of a national education-AI mandate being measured and then *reversed*. Set
against Singapore's approach — a **Teacher AI Literacy Professional Learning
Roadmap** with one compulsory module by end 2026 and two recommended by end 2027,
i.e. capability before content — it reads as a real design lesson rather than an
anecdote: **fund the teacher, not the artefact.** Any national-rollout proposal
should carry an adoption-risk section citing Korea.

## 7. Evaluation is the missing layer, and the absence is now specific (high confidence — measured first-hand) — 🟡 **HALF-SUPERSEDED `2026-10-31` (`p570`), see trend 15**

> 🟡 **Dated correction, `2026-10-31` (`p570`).** The *regression* half of this
> trend is **wrong as a supply claim** and was wrong for six passes: seven granted
> rubric-scoring assets exist on
> [`topic:rubric`](https://github.com/search?q=topic%3Arubric) (187 results), an
> axis this base never queried, and they are now shelved in
> [`../repos/foundations.md`](../repos/foundations.md). The ***observability***
> half stands — there is still no education-specific detector for a deployed
> tutor drifting, seventh consecutive pass. Read what follows as accurate about
> runtime monitoring and as superseded about scoring machinery.

Three passes of searching have located exactly **three** evaluation assets for
education AI:

- [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
  — MIT, 13★, 1,143 questions from real teacher-qualification exams (CDPK 920,
  SEND 223). Measures whether a model knows how to **teach**.
- [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
  — 87★, research-backed **rubrics** for scoring generated instructional content.
  **Licence resolved this pass from `main/LICENSE.md` (1,615 B) after three
  passes unresolved, and it is partly restrictive:** evaluator **code → MIT**,
  evaluator **content (prompts and settings) → CC BY 4.0**, but the **Annotated
  CLEAR Corpus** and **Annotated PERSUADE 2.0 Corpus → CC BY-NC-SA 4.0**,
  i.e. **non-commercial**. The upstream originals are NC too, so there is no
  cleaner substitute. **The scoring machinery is commercially usable; the
  benchmark data is not.**
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
  — code MIT / datasets per-publisher, 164★, standards-and-curriculum data layer
  with an MCP server, used to check **alignment**.

**None of the three is a runtime monitor, and this pass the gap got slightly
worse rather than better.** There is no open-source way to detect that a deployed
tutor has drifted, regressed after a model upgrade, or started teaching something
off-syllabus. Given trend 1 — skill bundles whose behaviour changes when the
harness or model changes beneath them — this is the single largest unmet need in
education AI, and it is where every region's governance gap actually bites.

**What got worse:** the fallback this KB prescribes — hand-build the regression
suite (pattern **P-568-K**) and score it with `evaluators` — now has a known
licence boundary. The rubric **code and prompts** clear commercially; the two
**annotated corpora are NC**. So an engagement must **bring its own corpus**, and
the one public corpus of annotated instructional text cannot be the basis of a
billable regression suite. The capability gap is unchanged and the cost of
closing it went up.

## 8. Credentials and skills-based models (medium confidence — still single-source)

1EdTech continues to point to digital credentials as a key development, with
employer expectations accelerating a skills-driven ecosystem. **No second
independent *commentary* source surfaced this pass either** — four passes with
the story carried by the standards body that has an interest in it, which is
itself informative.

**But the supply side corroborated it for the first time.** Two MIT repositories
located this pass are built specifically for credentials and competencies:
[`iblai/lms`](https://github.com/iblai/lms) (MIT, 208★, "discover courses, track
competencies, **earn credentials**, accelerate workforce development", Next.js 15,
created 2026-03-04) and, at five days old,
[`euron-sde-team/euron-open-lms`](https://github.com/euron-sde-team/euron-open-lms)
(MIT, 10★) which ships **verifiable certificates**. Code being written against a
trend is weaker evidence than an independent survey and **stronger** than a
second press release: somebody is spending engineering time on it. Upgraded from
*watch item* to **medium confidence, supply-side corroborated**.

## Licence-structure trend (measured first-hand)

**The agent layer is permissive; the platform layer is not — and the exception
appeared this pass.** Eleven of fourteen shelved agents are MIT, two Apache-2.0.
Platforms of record are AGPL/GPL almost without exception. The new exception,
**`Selleo/mentingo` (MIT, Poland, 102★)**, is the first AI-native LMS a client
can fork and keep closed; **`DSpace` (BSD-3-Clause)** remains the only
permissive platform of record at category-leader scale, in the institutional
repository.

A second structural finding, stated too broadly last pass and **corrected here**:
*"there is no permissively licensed education ERP"* holds **at
platform-of-record scale** — that category is LGPL (OpenEduCat, Odoo) or
GPL/AGPL (Frappe ×2, i-educar, openSIS) without exception. It does **not** hold
one tier down: [`academico-sis/academico`](https://github.com/academico-sis/academico)
is **MIT**, 410★, 151 forks, topic `student-information-system`, pushed
2026-10-30 — a permissively licensed, actively maintained education SIS for small
and medium institutions. The scope was wrong, not the observation.

**And the scarcity now has a denominator.**
`topic:learning-management-system license:apache-2.0 stars:>50` returns **2
repositories in the world**; `topic:lms license:mit stars:>80` returns 15 of
which **six are education platforms** (the topic also catches a coding agent and
a .NET colour-space library). The entire permissive LMS population above 50★ is
roughly **eight repositories**, the largest at 701★ on an end-of-life stack,
against Moodle's 7,600★ under GPL-3.0. "Assemble rather than adopt" survives as
advice for university-scale work — and one tier down it is no longer true.

A third structural finding, **new this pass**: the interoperability layer was
missing **SCORM** for three passes. `jcputney/scorm-again` (MIT, 362★, SCORM 1.2
and 2004, offline-first) is the permissive runtime for the standard the installed
base actually ingests and that procurement asks for by name. The attach doctrine
now has four legs — LTI, MCP, xAPI **and SCORM** — and only the fourth one
delivers content *into* the platform.

## Licence hygiene: the sidebar is not the licence, and `NOASSERTION` is three different things (measured; sharpened this pass)

The method rule stands — **read the file, not the sidebar** — and this pass added
a mechanism and a correction.

**The mechanism, upgraded twice in two passes.** The third pass reached GitHub's
REST index through the MCP server (`license.spdx_id`, `stargazers_count`) — better
than rendered pages, because it returns GitHub's own licence *determination*. The
fourth pass went one level deeper: **`raw.githubusercontent.com` answers HTTP 200
from this session**, so the licence **text** is readable. Twenty-one files were
read byte-for-byte, which closed two three-pass-old licence questions and added a
third confirmation to two standing defects.

The channels, and what each one is for:

| Channel | Status here | Use it for |
| --- | --- | --- |
| MCP `search_repositories` | ✅ works | Existence, stars, forks, push date, licence *determination*, cohort enumeration with denominators |
| `raw.githubusercontent.com` | ✅ **works — new** | The licence **text**. Try every filename (`LICENSE`, `.md`, `.txt`, `licence`, `COPYING`) on **every branch** |
| `license:<spdx> repo:owner/name` search | ✅ works | A cheap second opinion: zero results means GitHub detects no such grant |
| MCP `get_file_contents` | ⛔ repo-scoped | Nothing — it refuses any repository not attached to the session |
| `api.github.com`, `github.com` HTML via `curl` | ⛔ uniform 403 | Nothing. A uniform status across every URL measures the network, not the data |
| MCP `search_users` | ⚠️ no `location` | Nothing for region. Owner country is unobtainable, which is why seven shelf rows are **Global** |

**The correction:** `NOASSERTION` does **not** mean "unlicensed". Three distinct
states collapse into it or near it:

| State | Example | What it actually means |
| --- | --- | --- |
| Licence file present, non-standard filename, **split grant** | `learning-commons-org/knowledge-graph` (164★) | `LICENSE.md`; README badges read **code MIT / datasets "By data publisher"**, some datasets **gated**. Code safe; each dataset cleared individually. |
| Licence claimed in prose, **file absent** | `DMontgomery40/mcp-canvas-lms` (104★) | README says "MIT License - see LICENSE file"; that file 404s on every name and both branches. Default: exclusive copyright. |
| Licence file present, non-standard filename, **three-tier split with a non-commercial tier** | `learning-commons-org/evaluators` (87★) ← *resolved this pass* | `LICENSE.md`, 1,615 B: code **MIT**, prompts/settings **CC BY 4.0**, two annotated corpora **CC BY-NC-SA 4.0**. The machinery is commercial; the data is not. **The inverse split from its own sibling.** |
| **No licence field at all** | `digitalinnovationone/dio-agent` (2,750★) | Genuinely unlicensed. All rights reserved. Confirmed this pass by a second method: no file on either branch. |
| Copyleft with a **per-directory dual grant**, on a **non-`main` default branch** | `24kchengYe/human-skill-tree` (586★) ← *resolved this pass* | `master/LICENSE`, 1,063 B: **AGPL-3.0**, plus a `DUAL LICENSING NOTE` making `skills/*.md` usable under **AGPL-3.0 *or* MIT at the adopter's option**. Platform disqualified, bundles usable. A licence **column cannot express this row** — and probing only `main` returns a false "no licence". |

And a fourth shape that is not ambiguous, just wrong for the artefact: a
**content licence on code-shaped work** — `Auto-Empirical-Research-Skills`
(4,843★) under **CC BY-SA 4.0**, share-alike, the largest education agent-skills
repo in existence.

**Across three passes, every licence defect found has been in the agent layer.**
Platforms state copyleft clearly and accurately. The fast-moving layer claims MIT
loosely, ships share-alike, or says nothing — and does so at thousands of stars,
where it is most likely to be adopted without checking.

## A governance trend about AI itself, which belongs here (high confidence)

**South Africa's draft National AI Policy was withdrawn because its citations
were fabricated.** Gazetted 10 April 2026 (Notice 3880); withdrawal announced 26
April 2026 and formalised in a Gazette of 12 June 2026; cause: at least **10% of
the academic references in the reference list were fictitious**.

A national AI policy failed on provenance. For an education client — whose entire
product is claims about what is true, assessed against a syllabus — this is the
most persuasive available argument that **citation provenance is a deliverable,
not a nicety**. It is also why this KB states its method, names its sources, and
records what it could not verify.

## 9. The layer education AI actually runs on is horizontal, permissive, and was invisible to this KB for four passes (high confidence — measured first-hand)

**This is the fifth pass's main finding, and it is a correction to the shape of
the whole KB rather than an addition to it.**

Every sweep in passes one to four filtered on an education topic. Running the
capability axes instead (`topic:ocr`, `topic:pdf`, `topic:pptx`,
`topic:text-to-speech`) returned **sixteen permissively licensed repositories,
five above 30,000★ and three above 69,000★** — `PaddleOCR` (Apache-2.0, 92,024★),
`MinerU` (82,860★), `tesseract` (Apache-2.0, 77,267★), `docling` (MIT, 69,909★),
`OfficeCLI` (Apache-2.0, 32,854★), `opendataloader-pdf` (Apache-2.0, 30,129★).

**For scale: the largest education-specific asset in this KB is DeepTutor at
52,208★, and the entire education-agent shelf summed is smaller than `PaddleOCR`
alone.**

**Why this is a trend and not just a gap-closure.** It says where the engineering
value in education AI sits. The education-specific layer supplies *pedagogy* —
learner models, tutoring loops, assessment design — and it is thin, young and
licence-inconsistent. The horizontal layer supplies *capability* — ingestion,
OCR, speech, document generation — and it is enormous, mature, and permissive.
**A credible education build is therefore mostly horizontal components with a
thin education-specific layer on top**, which is close to the inverse of how this
KB's first four passes implicitly described the market.

**The commercial consequence.** It reorders what an engagement should start with.
Generating new material competes with the client's own faculty. **Ingesting the
material the client already owns** — the textbook, the past papers, the lecture
notes, the scanned worksheets — is *migration* work: easier to scope, easier to
value, and impossible for the client to replicate with a chatbot subscription.
See pattern **P-570-A**.

**The method lesson generalises past education**, and it should be carried to
every other industry KB in this collection: *a sweep filtered on an industry
topic measures how a repository markets itself, not what it does.* Tools an
industry depends on are tagged by capability, because their authors sell to
everyone. Sweep both axes or report an undercount.

## Licence-structure trend, extended: two more shapes, and "Creative Commons" now spans the whole range

The licence-shape catalogue in this KB grew from five to **seven** this pass, and
the two additions sit at opposite ends.

**Shape 6 — Apache-2.0 *plus commercial thresholds and an attribution duty*
(`MinerU`, 82,860★).** `master/LICENSE.md` (3,301 B, read first-hand) grants
Apache-2.0 "subject to the additional terms below", then imposes: a **separate
commercial licence above 100 M MAU or USD 20 M monthly revenue**; a **prominent
attribution obligation** on any online service built with it; and **automatic
termination** of all rights on breach of either. GitHub reports the whole thing as
`NOASSERTION`.

**Read the two clauses differently.** The threshold is commercially irrelevant to
any education engagement — no school system has 100 M MAU, and the clause is
aimed at hyperscalers. **The attribution clause is not irrelevant at all**: it is
a *product* requirement that lands on the client's UI and public documentation,
so it has to reach their engineering and UX teams and not just their legal
review. This is the first licence in this KB whose main consequence is a
**design** obligation rather than a distribution one.

**Shape 7 — CC0-1.0, a public-domain dedication (`gen-mentor`, 135★,
WWW 2025 oral).** 7,048 bytes of CC0: no attribution, no share-alike, no notice.
**More permissive than MIT.**

**And that juxtaposition is the actual finding.** Last pass rejected the two
best-curated pedagogy libraries in open source *because they were Creative
Commons* — `Auto-Empirical-Research-Skills` (CC BY-SA 4.0, 4,843★) and
`education-agent-skills` (CC BY-SA 4.0, 932★). This pass shelved a peer-reviewed
tutoring framework *because it was Creative Commons*. **"It's Creative Commons"
now predicts nothing about usability in this KB: the family spans the most
permissive grant on the shelf and the two most commercially obstructive ones.**
The only reliable move is the one this KB adopted two passes ago — read the file,
every time.

## Metadata hygiene: two fields that a licence column cannot express (measured first-hand)

Both were caught this pass only because they were checked explicitly, and both
look like clean findings if they are not.

- **`archived: true`.** `supertone-oss-archive/supertonic` is **MIT**,
  **13,757★**, **1,566 forks**, on-device multilingual TTS with bindings for ten
  languages — an almost ideal offline read-aloud component. It is **archived**.
  The grant is perpetual and the code still runs, but there will be no patches,
  no security fixes and no new languages. **Stars and licence are both excellent
  and both irrelevant to that fact.** A shelf built on stars-plus-licence would
  have recommended it without qualification.
- **An Apache licence with the template placeholders still in it.**
  `terracotta-education/terracotta`'s `LICENSE` is unmodified Apache-2.0
  boilerplate including the literal `Copyright {yyyy} {name of copyright owner}`.
  GitHub's "Apache-2.0" determination is correct and the grant **names no
  licensor**. Usable; a diligence note on any deliverable that depends on it.

**The general rule this suggests**, after five passes of licence work: the
licence answers *may we*, and it is the field this KB has learned to read
properly. It does not answer *should we* — `archived`, `pushed_at`, open-issue
ratios and the presence of a named licensor do, and they are cheaper to check
than a licence file.

## Region attribution: recoverable for institutions, not for people (measured first-hand)

The fourth pass concluded region was unobtainable — `search_users` exposes no
`location`, `api.github.com` returns 403 — and left seven rows `Global`. **That
was true of individuals and false of institutions.** An institutional copyright
holder names itself in the grant, and reading the licence file placed
`feedbacksystem` to **EMEA** ("Technische Hochschule Mittelhessen"),
`knowledge-spaces` to **North America** ("Vanderbilt Data Science Institute") and
`WhisperLive` to **EMEA** ("Collabora Ltd.").

**The limit was then tested, which is the part worth keeping.** All seven
`Global` rows were re-probed against the instrument and **none resolved**: every
holder is an individual or a pseudo-collective, and one Apache boilerplate
carries no copyright line at all. So the rule is conditional —
**region is recoverable from the licence file if and only if the copyright holder
is an institution** — and the `Global` rows stay `Global` for a stated reason
instead of for want of a method. Two holders whose *names* read Korean and French
are both recorded `Global`, deliberately: a personal name is not a country, and
inventing a region to fill a closed-vocabulary column is how a filter starts
lying.

## 10. The defensible-assessment trend: the gate is becoming the product, not the generator (high confidence — measured first-hand)

**Five passes of this KB looked for an AI that *writes* good exam questions and
recorded a gap. The sixth found that the thing being built instead is the
mechanism that *refuses* bad ones** — and on reflection that is the correct
response to the regulatory calendar, not a consolation prize.

🟢 [`onionviolet/itembank`](https://github.com/onionviolet/itembank) (**MIT**, 3★,
**1,175 commits**) describes itself as *"a machine-checkable contract for
LLM-authored questions"*. It assumes the items are model-written and spends its
engineering on constraining them:

- a **blocking linter** per item number — every distractor must explain when it
  *would* be correct; answer-position skew; select-count against keyed-count;
  duplicate stems;
- a **CI guard** that fails the build if real banks are committed;
- **deterministic scoring with no model in the path** — `fill` all-or-nothing,
  `check` running learner code against hidden cases, and **short-answer items
  never auto-graded**, held pending for rubric marking.

🟢 **Why this is a trend and not one repository's taste.** The same inversion shows
up independently across this base: `learning-commons-org/evaluators` scores
generated instructional content against **research-backed rubrics**;
`terracotta-education/terracotta` measures whether an intervention *worked* under
randomisation, with consent hidden from the teacher and identifiers stripped from
exports; `Claudemy` and `ZeKaiNie/universal-examprep-skill` both make **source
citation and anti-hallucination** the headline feature rather than fluency. 🔵 Four
unrelated authors, one pattern: **the differentiator has moved from generation
quality to provable constraint.**

🟢 **The commercial reading, which is the point.** The EU AI Act's Annex III
high-risk category covers **evaluation of learning outcomes**, with obligations
landing **2 December 2027**. The artefact that category demands is not a better
question-writer — it is **evidence that a human marked everything a machine could
not defensibly mark**. `itembank`'s architecture is that evidence, and it is MIT.
🟢 The same property answers the US state-policy wave from a different direction:
local-first operation with nothing leaving the machine is a direct response to
proposals like California's A.B. 1159 on training against student data.

🔴 **The half that is genuinely still missing, stated so this is not read as
solved.** Gating items is not calibrating them. There is **no live, permissive,
education-specific item-calibration asset**: `eribean/girth` (MIT) last shipped
**2022**, `inuyasha2012/pypsy` (MIT) **2018**, `meyerjp3/psychometrics` (the most
capable, Java) carries **no licence file at all**, and the R options are copyleft.
`bigdata-ustc/EduCDM` (Apache-2.0, 203★) is live and permissive but does
**cognitive diagnosis, not item calibration**. 🔵 So the honest client sentence is:
*author and gate items permissively today; calibration means a stale dependency,
a licence risk, or building it.*

## 11. A KB-hygiene trend that generalises to every industry base here: a closed gap keeps being published (measured first-hand)

🔴 **The sixth pass's second finding was an error in this base, and the mechanism
is portable enough to be worth stating as a trend.**

[`../repos/trending.md`](../repos/trending.md) was still publishing *"**No
open-source learning-analytics dashboard** still, sixth pass — only the LRS
(`openfun/ralph`) that would feed one"* while this same repository already held
[`openfun/warren`](https://github.com/openfun/warren) (**MIT**, 17★, pushed
2026-10-11, *"xAPI learning-analytics dashboards"*) and
[`openfun/potsie`](https://github.com/openfun/potsie) (**MIT**, Grafana suite) —
from the **same publisher as `ralph` itself**.

🔵 **The mechanism, which is what transfers.** The false claim lived in a
**narrative summary at the top of an append-only page**. Append-only is the right
policy for trend history — it is what stops an hourly pass from destroying the
record it exists to keep — but it has a failure mode nobody instrumented: *a
prose claim written into history keeps being read as current.* This base has
`crosspage-figure-claims.py` comparing **figures** across pages; it has nothing
comparing **existence claims** against the shelf.

🟢 **The generalisable rule for the other industry bases in this collection:**
every *"no X exists"* sentence is a claim with an expiry date, and it needs either
a date stamp that marks it stale or an instrument that re-checks it against the
shelf. 🔴 Absence claims are the highest-value and highest-risk statements a KB
makes — a client is told to build rather than adopt on the strength of one — and
they are the only claims here that nothing verifies. Registered as `568-A`.

## 12. The open-source education field is mostly below the star floor, and every search method in common use is blind to it (high confidence — measured first-hand)

🟢 **Measured this pass, with denominators on both sides of the comparison.**

| axis | results sorted by stars | results at `stars:<50` |
| --- | --: | --: |
| `topic:ai-tutor` | **816** | 🔴 **793** |
| `topic:psychometrics` | **510** | 🔴 **496** |
| `topic:learning-analytics` | **289** (`"learning analytics" dashboard`) | 🔴 **382** |

🔴 **On every axis the sub-50-star band is nearly the whole field.** For
`topic:ai-tutor` that is **97%** of results. 🟢 **And the band is not junk:** one
sweep of 30 rows produced **13 addresses new to a base that has run 568 passes
over this industry**, four of them with more than 200 commits, two of them
closing gaps this base had published for five and six passes.

🔵 **Why this is a trend and not a quirk of one KB.** The economics are
structural: an education-AI project is typically one practitioner — a teacher, a
graduate student, a psychometrician — solving their own problem, in their own
language, with no launch and no audience. **It accrues commits before it accrues
stars, and it may never accrue stars at all.** 🟢 **Three of this pass's four
high-commit finds are non-English-first** (Chinese `砚席`/`伴学`, plus a Spanish
Moodle plugin and a Portuguese IRT study in the tail). 🔴 **A star-sorted search
is therefore not merely incomplete, it is regionally biased** — it systematically
under-reports APAC and LATAM supply, which is precisely the supply a global
studio needs placed.

🔵 **The actionable form, for any industry on this harness:** stars measure
adoption and nothing else. For **tooling**, rank by commits. For **agents a
client must adopt**, stars remain the right floor. Recipe: `P-572-C`.

## 13. "MIT" on a platform is now routinely false at the directory level, and the cause has shifted from publisher choice to dependency inheritance (high confidence — measured first-hand)

🟢 **`568-D` recorded the split-grant shape at `4 of 4` instances. This pass makes
it `5`, and the fifth has a different mechanism from the first four.**

| instance | shape | mechanism |
| --- | --- | --- |
| `learning-commons-org/evaluators` | code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA 4.0 | publisher's choice |
| `24kchengYe/human-skill-tree` | AGPL-3.0 platform · `skills/` MIT at adopter's option | publisher's choice |
| `langfuse/langfuse` | MIT-Expat outside four `ee/` directories | publisher's choice (open-core) |
| `sudazc/open-question-bank` | code + docs MIT · bank content per-`bank.yaml`, default *"TBD - not for publication"* | publisher's choice |
| 🆕 **`swsgbl/ai-learning-os`** | 🔴 **MIT root · AGPL-3.0 obligations on `services/api/`** | 🔴 **a single in-process dependency (PyMuPDF, AGPL-3.0)** |

🔴 **The fifth instance is the dangerous class, because the repository's own
grant is MIT everywhere and the obligation is invisible to a licence-file read.**
This base's primary instrument — `raw.githubusercontent.com/<repo>/main/LICENSE`,
read byte-for-byte — returns a clean 1,084-byte MIT text for `ai-learning-os`.
The AGPL-3.0 §13 network obligation lives in `NOTICE.md`. 🟢 **Nothing about the
instrument is wrong; it is answering a narrower question than anyone was asking.**

🔵 **The rule, stated so it transfers:** a repository's **licence** is in
`LICENSE`; its **licence surface** is in its dependency manifest. For a library
the two usually coincide. **For a platform they routinely do not**, and a platform
is what an engagement deploys. 🟢 The contrast inside this one pass is the proof:
`DaniyalMlk/calibrate` declares MIT and has **zero runtime dependencies**, so its
licence surface *is* its licence; `ai-learning-os` declares MIT and drags a
network-copyleft obligation onto the one directory a studio would host.

🟢 **Operationally this is cheap to check and cheap to fix** — read the manifest
and `NOTICE`, then price the swap. In this instance a BSD-3 or MIT PDF parser in
place of one AGPL dependency clears the whole platform (`P-572-B`). 🔴 **What is
expensive is finding out after deployment.**

## 14. Provenance is now forged at the layer this field just started trusting (high confidence — measured first-hand, with controls)

🔴 **A git history can be synthetic, and nobody checks.** This KB moved its
tooling-layer admission signal from **stars** to **commit count** at `p569`,
for a good reason: a star floor was discarding genuinely useful libraries
(`calibrate`, 0★ / 214 commits; `itembank`, 3★ / 1,175 commits). 🔴 **One pass
later, the first never-swept axis returned
[`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune): 35★,
`2,137` commits, history beginning `2014-06-10` — and the history is
manufactured.**

| check | `ScoreRune` | control `mirt` (real, 16 yrs) | control `dexter` (real, 10 yrs) |
| --- | --- | --- | --- |
| commits/year, max:min | 🔴 **1.69×** and monotonic for 12 years | 🟢 **658×** | 🟢 **34.5×** |
| pre-2017 commits using Conventional-Commits prefixes | 🔴 **408 / 408** | 🟢 1 / 2,113 | 🟢 0 / 0 |
| commits where author date ≠ committer date | 🔴 **0** of 2,137 | 🟢 19 of 3,467 | 🟢 1 of 276 |
| subject of the repository's first commit | 🔴 **`refactor: evidence kinds`** | 🟢 `improved the README…` | 🟢 `version 0.1.7` |
| distinct author addresses | 🔴 **2**, both GitHub `noreply` | 🟢 21 | 🟢 7 |

🔵 **Why this is a trend and not an anecdote: the economics changed direction.**
Buying stars requires other people, or at least accounts that look like them.
**Synthesising a 12-year commit history requires a loop and `GIT_AUTHOR_DATE`.**
So the moment a community — this KB, a procurement checklist, a "trending" digest
— starts rewarding commit density, it has adopted a signal that is **strictly
cheaper to forge than the one it replaced.** Every base on this harness that
shortlists on commit count has the same exposure.

🟢 **What to do, and it is cheap.** Read commit count **only together with its
date distribution**. Real histories are *bursty* — a launch spike, a plateau, a
quiet year, a revival. A smooth monotonic ramp is a generator artefact. Three
further checks cost nothing: commit-message conventions that postdate their own
timestamps, author/committer date divergence of exactly zero across thousands of
commits, and a repository whose first commit is a `refactor:`. 🟢 Implemented as
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass; it reproduces its founding case and passes both
controls above. Evidence:
[`../evidence/history-plausibility.2026-10-31-p570.tsv`](../evidence/history-plausibility.2026-10-31-p570.tsv).

🔴 **The uncomfortable corollary for this page.** Every star count and commit
count quoted anywhere in this KB is a *claim made by a repository about itself*.
Stars have a known failure mode this base already documents (third-party digests
reporting impossible rates). Commits now have one too. **The only signals read so
far that an author cannot unilaterally manufacture are the licence text, the
dependency manifest, and the behaviour of the code.**

## 15. A multi-pass "gap" is often a vocabulary artefact, not an absence (high confidence — measured first-hand, twice in two passes)

🔴 **This KB published *"no education-specific agent evaluation or regression
tooling exists"* for six consecutive passes.** It searched `evaluation`,
`benchmark` and `observability` under `topic:education`, got nothing, and
escalated the claim each pass until it read as the industry's clearest unmet
build opportunity. 🟢 **The assets were on
[`topic:rubric`](https://github.com/search?q=topic%3Arubric) — 187 results — and
the string `topic:rubric` appeared ZERO times in every live page of this base
before `p570`.** Seven of its top ten were addresses new to a 569-pass base, all
granted, four Apache-2.0.

🔵 **This is the second consecutive pass in which a long-published absence
dissolved on contact with a different access method, not with new supply:**

| pass | published absence | what actually caused it |
| --- | --- | --- |
| `p569` | *"the `topic:ai-tutor` axis is saturated"*, four passes | 🔴 **The sort.** `816` results by stars, `793` at `stars:<50` — 97% of the field sat below the floor the base ranked by |
| `p570` | *"no education-specific evaluation tooling exists"*, six passes | 🔴 **The vocabulary.** The layer is tagged `rubric`, a word the base never queried |

🟢 **The generalisable control, and it is the cheapest quality gate available to
any industry base on this harness:** before publishing an absence, state the
**query** that failed and the **denominator** it returned. An absence with no
query attached is unfalsifiable, and this base has now twice shipped one for
multiple passes. 🔵 An absence claim should carry three things — *the query, the
result count, and the date* — and `569-A`'s second ask (a mandatory date stamp on
every absence claim; **414 of 565** currently carry none) is the first third of
that control.

🔴 **Note what did *not* dissolve, because the discipline cuts both ways.** Two of
the four never-swept axes — `topic:academic-integrity` (121 results) and
`topic:automated-grading` (49) — returned **ten of ten** head rows already
in-base. **Not every unswept axis hides a finding, and reporting the two nils is
what makes the one hit credible.**

## 16. A finding recorded in this base's history does not reach its shelf, and nothing was checking the difference (high confidence — measured first-hand, with a verified HEAD check)

🔵 **This is trend 11 (*a closed gap keeps being published*) in its mirror image: an
OPEN finding that never got published.** Trend 11 catches the base repeating a null
it had already refuted. `p571` catches the opposite — the base **holding an asset
it never shelved**, and simultaneously **shipping a pattern that asserts the asset
is missing.**

🟢 **The measurement.** Pass 85 (`2026-10-09`) recorded *"An item-generation tier
exists now, **5 of 5 MIT**"* in `agents/trending.md`. Checked against `HEAD` at
`p571`, **86 passes later**:

| page | item-generation rows present at HEAD |
| --- | --: |
| `agents/top.md` | 🔴 **0 of 7** |
| `repos/foundations.md` | 🔴 **0 of 7** |
| `compose/patterns.md` `P-571-A` | 🔴 asserts *"nothing permissive generates psychometrically defensible items"*, authoring slot left to a **bare model prompt** |

🔴 **So the base's history, its shelves and its patterns disagreed with each other
for 86 passes, and no instrument compared them.**

🔵 **Why this is structural rather than an oversight, which is what makes it a
trend.** `agents/trending.md` is **63,000 lines**; the shelf pages are hundreds.
The history is append-only and grows every pass; the shelf is curated and grows
rarely. 🔴 **An inventory built by grepping the shelves — the obvious and cheap
move, and the one `p571` itself made first — reports absences that the history
refutes.** `p571` drafted five "new" addresses and a "never queried in 570 passes"
claim on exactly that mistake, and caught it only by grepping `trending.md`
afterwards.

🟢 **The corrective, as a procedure, and it is one line:** build the
already-have inventory from **`trending.md` + `intel/open-gaps.md`**, never from
the shelf pages. The shelves record what was *promoted*; the history records what
was *seen*. 🔵 **Generalises to every industry base on this harness**, all of which
have the same append-only-history / curated-shelf split.

🔴 **A second-order consequence worth stating: a saturated base's failure mode
flips from under-collection to under-promotion.** Nine consecutive passes of
`WebSearch` nils and four fully-saturated topic axes at `p571` mean discovery is
largely done. 🟢 **In that regime the highest-yield work is auditing
history-against-shelf, not buying new channels** — `p571` produced seven shelf
rows and a corrected pattern from **zero new addresses**.

## 17. Tag variants split a capability's population, and the short form is the empty one (high confidence — measured first-hand)

🟢 **Measured on automated essay scoring, where this base holds both tags:**

| tag | population | ★ ceiling | permissive grants |
| --- | --: | --: | --: |
| 🟢 `topics/automated-essay-scoring` (pass 84) | **35** | — | 🟢 **8**, incl. `doheejin/ProTACT` **BSD-3-Clause** |
| 🔴 `topic:essay-scoring` (`p571`) | 🔴 **17** | 🔴 **34** | 🔴 **0** |

🔴 **Had `p571` swept only the short tag it would have published *"no permissive
automated-essay-scoring implementation exists"* — contradicting this base's own
pass-84 record of eight permissive grants on the long tag.** The short form
collects the abandoned, the coursework and the ungranted; the 34★ ceiling is the
signature.

🟢 **Rule, checkable before spending: when a capability has both a long hyphenated
tag and a short synonym, sweep the LONG form.** 🔵 This refines `P909`/`P910`'s
existing precision rule, which scored tags by **word count** — word count predicts
*precision*, and this predicts *population completeness*. They are different
failures: a low-precision tag wastes the budget, a short-form tag **manufactures a
false null**, which is worse because it gets published.

🔵 **It also explains a standing regional result rather than overturning it.** The
short tag's 17 rows include three Brazilian/Portuguese-language ENEM-adjacent
repositories; two were re-probed at `p571`
(`renan-aalmeida/AES_Enem_Competencia5`, `DaviSantos-23/Reda-o`) and **neither
grants anything** — reproducing `Gap 235`'s conclusion that the Portuguese
essay-scoring tier is **ungranted, not absent** on a second, independent tag. 🟢
The permissive asset in that tier remains the **corpus** (`lplnufpi/essay-br`,
MIT, human-graded on ENEM C1–C5), not a scorer.

## 18. The prescribed verification command fails in both directions on this harness, and the direction depends on the flags (high confidence — measured with controls, reproducing `P914`)

🟢 **Pass 85 recorded `P914`:** `curl -sI https://github.com/<slug> | head -1`
reads the agent proxy's `HTTP/1.1 200 Connection Established` and therefore
reports **200 for every slug on earth, including one invented thirty seconds
ago.** 🔴 **`p571` reproduces the hazard with the opposite symptom:** the same
command read via `-o /dev/null -w "%{http_code}"` returns **403 for every
github.com URL**, real and fabricated alike.

| read of the same command | known-real | fabricated control | the wrong answer it produces |
| --- | --- | --- | --- |
| 🔴 `curl -sI \| head -1` | 200 | **200** | ⛔ everything verifies — **admits fabrications** |
| 🔴 `curl -sI -w "%{http_code}"` | **403** | 403 | ⛔ nothing verifies — **would delete real rows** |
| 🟢 rendered repository page | name + ★ + licence | 🟢 **404** | ✅ discriminates |
| 🟢 `raw.githubusercontent.com/…/LICENSE` | 🟢 **200** + bytes + holder | 🔴 404 | ✅ the grant instrument |

🔵 **The generalisable point is stronger than `P914` alone.** It is not that curl
reports a misleading 200; it is that **`curl -sI` against this proxy carries no
information in either direction**, and a pass inherits whichever error its flags
happen to produce. 🔴 A pass reading 403 as *"repository gone"* would **delete
verified rows**; one reading 200 as *"verified"* would **admit fabrications**.
🟢 **Therefore: calibrate on a known-real AND a known-fabricated control before
trusting any pass's verification, and record which channel answered each row.**

🔴 **Also unstable across passes: `api.github.com`.** At `p568` it was reachable
and `foundations.md`'s header still claims metadata from the *"GitHub REST
index"*. At `p571` it is **scoped to the harness repository** — every other path
returns `"GitHub access to this repository is not enabled for this session"`. 🔵
**A channel claim in a page header is a statement about one past session, not a
standing property.** Date it or drop it.

## Declared gaps

- **Most trend sources are vendor blogs or market-research summaries.** The load-
  bearing citations are OECD, UNESCO/IESALC, 1EdTech, the European Commission and
  Eurydice reports, TEQSA, the AJET study, named statutes — and, for trends 1, 7
  and the licence sections, **this KB's own first-hand measurements of GitHub's
  index**, which are the most reliable items here.
- **EU AI Act primary text cannot be read from this session — established, not
  deferred.** Attempted this pass: **`eur-lex.europa.eu` does not resolve**, nor
  does the `artificialintelligenceact.eu` mirror, the same failure class as
  `camara.leg.br`. It is a **network-policy constraint**, so it should stop being
  carried as an action item for the next pass and start being a request to allow
  the domain. Everything here on Regulation (EU) 2026/1744, the Annex III and
  embedded-product dates, Article 50 and Article 4 stays **multi-source
  secondary**.
- **The Council of Europe education instrument is single-source** and the Ipsos
  Education Monitor ban-support shifts (Japan 21→29%, Australia 47→52%, Korea
  27→31%) are single-source with unpinned baseline years. Both are carried as
  directionally reliable and not pinned.
- **Trend 8 (credentials) has no second *commentary* source after four passes**,
  but now has supply-side corroboration (`iblai/lms`, `euron-open-lms`, both
  MIT). Upgraded to medium confidence; the commentary gap stands.
- **Trend 6 rests on one country.** Korea's reversal is well detailed but it is
  one case; Singapore's contrast is a policy design, not yet an outcome.
- **No runtime evaluation tooling exists to recommend** (trend 7). Stated as a
  finding, but it means the governance advice this KB gives cannot currently be
  *operationalised* with open-source components. That is an honest limit on the
  whole page.
- **The agent-skills cohort has no provenance metadata, and this pass proved the
  limit is the instrument.** Region was assigned from README language, named
  national credentials (*gaokao*, 行测, 大创申报书) and licence-file copyright
  holders only. `search_users` exposes **no `location`** here and
  `api.github.com` is 403, so a maintainer's country is unobtainable by any
  route; four of five new shelf rows are therefore **Global**. Read "Global" as
  *provenance unknown*, not as *geographically spread*.
- **13 of 13 agent-skills licences are now read; 0 of 13 declare a version or
  ship a test suite.** The versioning and regression problem named in trend 1 is
  **unmeasured because there is nothing in the cohort to measure it with** — not
  a gap in this KB's searching, a property of the artefact class.
- **Horizontal tooling is systematically under-covered, and the miss was
  expensive.** `hugohe3/ppt-master` — **MIT, 71,498★**, the largest permissively
  licensed repository anywhere in this KB — went unfound for four passes because
  every sweep filters on an education topic and it carries none. It was surfaced
  by the prescribed *web* search, which cuts against the previous pass's "query
  the index, not the listicles". **Both channels are required; next pass should
  sweep by capability (`topic:pptx`, `topic:text-to-speech`, `topic:pdf`,
  `topic:ocr`, `topic:scorm`) crossed with licence.**

### Added on the fifth pass

- **Sixth consecutive pass with no education-specific agent observability or
  runtime regression tooling.** Two differently shaped queries returned nothing
  new. The gap narrowed by one notch and not by the expected route:
  `terracotta-education/terracotta` (Apache-2.0, 21★) provides **randomised
  controlled trials inside LMS assignments**, with informed consent hidden from
  the teacher and student identifiers stripped from exports. That is **efficacy
  measurement** — "did this intervention change outcomes" — and it is the first
  open-source answer to that question in this KB. It is **not** drift detection.
  A tutor in production still has no open-source way to detect that it has
  degraded, and that remains the clearest unmet build opportunity in the industry.
- **Assessment-item generation is a newly *specific* gap.** The capability sweep
  found abundant permissive tooling for generating *content* and none for
  generating **psychometrically defensible items**. That distinction is what an
  exam board or certification body actually buys, and nothing located addresses
  it.
- **Lecture-video tooling remains unswept.** `harry0703/MoneyPrinterTurbo` (MIT,
  136,744★) surfaced incidentally and is **short-form social video, not lecture
  content**; it is deliberately not shelved. A `topic:video` capability sweep is
  the next pass's job, on the evidence that capability sweeps are where the volume
  has been.
- **Market sizing is unchanged and still vendor-only, now at five passes.** The
  2026 figure reproduced again at **USD 10.6 bn** from the ResearchAndMarkets
  family, with **USD 42.48 bn by 2030**; HolonIQ's **USD 12.3 bn** also
  reproduced. **No independent estimate has been located in five passes.** Quote
  the range, never a point.
