---
industry: education
region: Global
updated: 2026-10-30
---

## 🆕 `p555` — `2026-10-30` — **🟢 `Trend 65`: A PLATFORM `NOASSERTION` IS A FOUR-WAY AMBIGUOUS SIGNAL, AND ON THIS BASE **3 OF 8 ARE COSMETIC** — THE ARTEFACT IS PERMISSIVELY LICENSED AND EVERY TOOL SAYS OTHERWISE. 🟢 `Trend 66`: AN AGGREGATOR ATTACHES AI POLICY TO A COUNTRY'S MOST FAMOUS CURRICULUM BRAND, AND THE REAL INSTRUMENT IS ALWAYS A LATER, SUBJECT-LEVEL ONE.**

🔴 **Gate posture: `make hooks` denied** (`Code from External`). 🟢 `gate-dates` run directly at
`HEAD`: **0 `ASSERTED`**, 1 `ATTRIBUTED`. 🟢 `gate-tables` and `gate-region-headings` also green.

### 🟢 `Trend 65` — `NOASSERTION` does not mean what this base was about to assume

🔵 **The inference this pass drafted and then disproved:** that GitHub's `NOASSERTION` *detects*
a composite or non-standard grant, and so hands this base a free classifier for the hardest
class on these shelves. 🔴 **It does not.** Measured on **8 of 79** education repositories, the
verdict has **four distinct causes**, and they call for opposite actions:

| Cause | n | Example | What a reader must do |
|---|---|---|---|
| 🟢 **Presentation defect over a stock licence** | **3** | `OpenOLAT` — two blank lines above `Apache License` | 🟢 **nothing** — ship it; the grant is verbatim |
| 🔴 **Genuine code/corpus or per-path split** | **3** | `learning-commons-org/evaluators` — MIT code, `CC BY-NC-SA 4.0` corpora | 🔴 read both grants; the corpus may forbid shipping |
| 🔴 **Non-OSI source-available** | **1** | `Oriole-FDU/Wisepen` — `BUSL-1.1` | 🔴 priced door — commercial licence required |
| 🔴 **Grant asserted, not carried** | **1** | `frappe/education` — a 19 B `license.txt` | 🔴 no grant exists to rely on |

🟢 **So the signal is real and the classifier is not.** `NOASSERTION` says only *"this is not
the stock text I expected"*. 🔵 **The discriminator that works** is containment — does the
payload hold a known licence's **operative body**, verbatim? — implemented as
[`../ingest/operative-body.py`](../ingest/operative-body.py), **9/9 controls**, and it is
window-free by construction, which is why it survives the decoration that defeats `licensee`.

🔴 **The commercially sharp half of `Trend 65`:** a cosmetic `NOASSERTION` makes a **permissive**
artefact read as the riskiest thing on the shelf, in the single field that SBOM generators,
licence scanners, GitHub's own sidebar and procurement reviewers all read. 🔴 **Three of this
base's platforms are in that state, and one of them is the recommended EMEA base.** The failure
is silent, it is in the safe-looking direction for the tool and the unsafe direction for the
deal, and **no amount of reading the README fixes it** — `OpenOLAT`'s README is not where its
Apache-2.0 grant lives.

🟢 **The inverse exists too, and it is the reason this cannot be a one-way rule.**
`openeducat/openeducat_erp` (901★) is the row where the platform field is **right** and this
base's shelf was under-informed: it asserts LGPLv3 plus the full GPL text and ships **~10 %** of
it, truncated before `END OF TERMS AND CONDITIONS`. 🔵 **A trend that said "distrust
`NOASSERTION`" would have shipped that defect.** The trend is: **`NOASSERTION` is a question,
and the payload is where it gets answered.**

### 🟢 `Trend 66` — the famous-curriculum mis-attribution, observed twice in one return

🔵 `Gap 554-G` carried two APAC leads from one aggregator: Indonesia's **Merdeka Belajar** and
the Philippines' **MATATAG**, both named as shaping national AI-adoption guidance. 🟢 **Both
grounded this pass, and both named the wrong instrument.**

| Country | Aggregator named | The instrument that actually carries AI |
|---|---|---|
| 🇮🇩 Indonesia | 🔴 *Merdeka Belajar* (the flagship curriculum) | 🟡 **`Permendikdasmen No. 13/2025`** — an elective inserted between Arts. 32–33; schools may stay on **Kurikulum 2013 *or* Merdeka** |
| 🇵🇭 Philippines | 🔴 *MATATAG* (the flagship curriculum) | 🟢 **`DepEd Order No. 003, s. 2026`** + **`CHED Memorandum Order No. 21, s. 2026`** — held on this base since `Gap 488-Q` |

🟢 **The shape:** national AI-in-education content arrives through a **separate, later,
subject-level instrument** — a regulation creating an elective, a department order setting
rules — while the aggregator attaches it to **the curriculum brand a reader will recognise**.
🔵 **Operational rule for this base:** a regional claim that names a famous curriculum should be
treated as **probably mis-attributed** until the subject-level instrument is found, and the
subject-level instrument is what a client engagement must be scoped against — because the two
imply different work. A curriculum mandate creates a **procurement**; Indonesia's elective
creates a **teacher-readiness problem**, which is a different deliverable at a different price.

🔴 **And the attestation limit that bounds both rows:** all four hosts carrying the primary
sources — `antaranews.com`, `bgtksumsel.kemendikdasmen.go.id`, `region8.deped.gov.ph`,
`iesalc.unesco.org` — are **`000`** through this session's egress proxy. 🔵 Both rows are
**ATTRIBUTED to the search channel, asserted by nothing**. `Gap 555-G`.


## 🆕 `p554` — `2026-10-30` — **🟢 `Trend 63`: ABOUT **ONE EDUCATION REPOSITORY IN TEN** CONTRADICTS ITS OWN DOCUMENTATION ABOUT ITS LICENCE — MEASURED ON 84, NOT ARGUED. 🟢 `Trend 64`: IN EDUCATION THE GOVERNING GRANT IS INCREASINGLY THE **CORPUS** LICENCE, NOT THE CODE LICENCE, AND THE CODE LICENCE IS THE ONE EVERY INDEX SHOWS.**

🔴 **Gate posture: `make hooks` DENIED** (`Code from External`) — thirteenth denial in
fourteen passes, not gate-attested. 🟢 Four gates run directly; three green **when run** — 🔴 the post-splice re-run was DENIED, so their state at `HEAD` is unverified. `Gap 554-F`.

### 🟢 `Trend 63` — the disagreement rate, measured

🔵 `p553` found one artefact whose three channels named three licences and asked for a
larger sample. 🟢 **84 education repositories, three channels each**: the grant payload at a
resolved branch, the README read in a licence-section window, and the package manifest's
licence field.

| Verdict | Rows | Share |
|---|---|---|
| 🟢 `CHANNELS-AGREE` | 54 | 64 % |
| 🔵 `DOC-SILENT` | 18 | 21 % |
| 🔴 `GRANT-DISAGREES-WITH-DOCUMENTATION` | **8** | **9.5 %** |
| 🔵 `ALL-CHANNELS-SILENT` | 4 | 5 % |

🔴 **All eight were read by hand before this number was published.** Five are true
contradictions; three are correctly-disclosed bundled components (`Gap 554-B`). 🟢 So the
defensible statement is: **5 of 84 (6 %) contradict themselves outright, 8 of 84 (9.5 %)
would fail a naive three-channel check**, and a reader who checks one channel learns the
wrong thing about roughly one repository in ten either way.

🔵 **Two things this number is not.** It is **not** a sample of GitHub — it is this base's
own shelves plus four new rows, which are *better* documented than average because they
survived prior passes' filters. 🔴 The true population rate is therefore most likely
**higher**, not lower. And it is a **lower bound even on this sample**: before `554-E` was
fixed the manifest channel was read with prose patterns and missed bare SPDX ids entirely.

🟢 **Prediction, stated so a successor can falsify it:** the disagreement rate will be
**higher** in repositories that ship data than in those that ship only code. 🔵 On this
sample it already is — four of the five true contradictions involve a corpus, a dataset or
authored content.

### 🟢 `Trend 64` — the governing grant has moved from the code to the corpus

🔴 **This is the trend with commercial teeth, and it is specific to education.** The
artefacts a studio wants in this vertical are increasingly **content-bearing**: annotated
corpora, hint and scaffold banks, curriculum knowledge graphs, benchmark sets. 🔴 Their
**code** is permissive almost without exception. 🔴 Their **content** is not.

| Artefact | Code | Content / corpus | What a naive read shows |
|---|---|---|---|
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 MIT | 🔴 **CC BY-NC-SA 4.0** — CLEAR Corpus, PERSUADE 2.0 | 🔴 an **MIT badge** |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🟢 MIT | 🔴 **per dataset, per download** — `Open` / `Open + Gated` / `Gated`, plus Terms of Use | 🔴 an **MIT badge** |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | 🟡 **CC BY 4.0** on all hints and scaffolds, attribution recorded per JSON file | 🟡 an **MIT `LICENSE`** |
| [`juanmoisesd/…-latin-america-dataset`](https://github.com/juanmoisesd/ai-educational-impact-latin-america-dataset) | — | 🔴 **CC0 (abridged) vs CC BY 4.0 vs MIT**, asserted in three places | 🔴 `NOASSERTION` |

🔴 **The mechanism is not carelessness; it is structural.** A repository has **one**
`LICENSE` file, one manifest field and one platform licence badge — all three designed for
**code**. The content grant has nowhere canonical to live, so it goes into prose, and prose
is the one channel no tool reads.

🟢 **The operational rule this base should carry forward:** in education, **clear the corpus
before the code**. The code licence is almost always the easy answer and almost never the
binding one. 🔵 `P609` makes it a gate; `Trend 63` says how often it will fire.

🔵 **Relation to `Trend 61`.** `p553` found the platform's licence field blind to non-OSI
and abridged grants. `Trend 64` is the wider case: the field is blind to **everything that
is not the code's licence**, which in this vertical is the part that decides the deal.
🔴 This pass could not re-measure `Trend 61` — `api.github.com` is **403** on this session
(`Gap 554-A`) — so `Trend 61` stands on `p553`'s seven rows and is **not** extended here.

## 🆕 `p553` — `2026-10-30` — **🟢 `Trend 61`: THE PLATFORM'S OWN LICENCE METADATA IS BLIND TO EXACTLY THE GRANTS THAT DECIDE A DELIVERABLE — GITHUB RETURNS `NOASSERTION` FOR BOTH THE BUSL-1.1 ROW AND THE ABRIDGED-CC0 ROW. 🟢 `Trend 62`: GRANT **COMPLETENESS** IS A SECOND AXIS, INDEPENDENT OF GRANT **FAMILY**, AND IT SHOWS UP IN RESEARCH AND DATA REPOSITORIES.**

🔴 **Gate posture, stated first and corrected before commit: `make hooks` RAN — for the
first time in twelve passes it was not DENIED — and it **FAILED, 48 of 68 gates green**.
🟢 **None of the 20 red gates is this pass's doing**: the identical red set was reproduced on
a pristine tree with `p553`'s edits stashed. 🔵 See `Gap 553-G`.

### 🟢 `Trend 61` — the licence field fails precisely where the money is

🔴 Seven addresses were read on two channels this pass: the grant payload, and GitHub's own
`license.spdx_id`. 🔴 **They disagree on two of seven, and the two are the only rows whose
licence changes what Globant may do.**

| Address | GitHub `license.spdx_id` | Payload, first-hand | Consequence |
|---|---|---|---|
| [`Oriole-FDU/Wisepen`](https://github.com/Oriole-FDU/Wisepen) | 🔴 `NOASSERTION` | 🔴 **BUSL-1.1**, excludes `consulting deliverable` | 🔴 A priced commercial door, invisible to a `license:` filter |
| [`juanmoisesd/ai-educational-impact-latin-america-dataset`](https://github.com/juanmoisesd/ai-educational-impact-latin-america-dataset) | 🔴 `NOASSERTION` | 🟡 **CC0-1.0, abridged** | 🔴 A public-domain dedication, read as *no licence* |
| five other rows read this pass | 🟢 matches | 🟢 matches | 🟢 agreement where the family is canonical and complete |

🔵 **Why this is structural and not a bug.** GitHub matches against a canonical licence
corpus and emits `NOASSERTION` when it **cannot** match. So it fails in exactly two cases: a
**non-OSI source-available** grant it does not carry, and an **abridged** grant that no
longer matches a template. 🔴 Those are `Gap 552-B` and `Gap 553-C` — the two bands this base
built verdicts for *because* they decide shippability. **The platform is most silent where
the stakes are highest.**

🟢 **Prediction, stated so a later pass can falsify it:** as source-available licensing
spreads in education (`Trend 60`), the share of education repositories reading `NOASSERTION`
will **rise**, and that rise will be misread as a rise in unlicensed code. 🔵 It is not. It
is a rise in licences the detector does not carry. **Rule:** the platform licence field is a
hint, never a verdict and never a discovery filter.

### 🟢 `Trend 62` — completeness is a second axis, and nothing on these shelves measured it

🔵 This base has graded grants on **family** for 553 passes. `p553` adds the axis the LATAM
row forced: **is the grant the whole legal code, or an excerpt of it?**

| Address | Family | Bytes carried | Canonical | Reading |
|---|---|---|---|---|
| [`juanmoisesd/ai-educational-impact-latin-america-dataset`](https://github.com/juanmoisesd/ai-educational-impact-latin-america-dataset) | CC0-1.0 | **1 259 B** | ~7 000 B | 🟡 **abridged** — title, disclaimer, Statement of Purpose, waiver sentence; **no s2, s3 or s4** |
| [`frappe/education`](https://github.com/frappe/education) | asserts GPL-3.0 | **19 B** | ~35 000 B | 🔴 **not carried at all** — a family name |
| [`Oriole-FDU/Wisepen`](https://github.com/Oriole-FDU/Wisepen) | BUSL-1.1 | **4 539 B** | ~4 300 B | 🟢 complete, parameter block included |

🔴 **Abridgement is not cosmetic, and the LATAM row shows why in its own region.** The clause
the 1 259 B file drops includes CC0 **s3, the Public License Fallback** — the provision that
makes CC0 operate where a bare copyright waiver is not recognised in law, **which is most of
LATAM's civil-law jurisdictions.** 🔵 So the one artefact this base has placed in LATAM is
missing the clause that would make its own dedication work there.

🔵 **Why this is a trend and not an anecdote:** an abridged grant is what you get when a
licence is **copy-pasted from a web page** rather than installed from a template — the
Creative Commons *deed* summary rather than the legal code. 🟢 Research and dataset
repositories are where this base finds it, because their authors are researchers publishing a
DOI, not maintainers wiring a licence into a release process.

### 🔵 Market figures returned this pass — spread recorded, not averaged

| figure | source class | value |
|---|---|---|
| AI-in-education market, 2026 | secondary, vendor blog | *past* **$12.5 B** in 2026 |
| AI-in-education market, 2026 | secondary, HolonIQ cited | **$12.3 B** globally by 2026 |

🔵 **Both secondary; the spread is ~1.6 % and is recorded rather than averaged**, per this
base's standing rule. 🔴 One widely repeated claim — *83 % of institutions plan AI teaching
assistant deployment* — traces to a **secondary citation of an EDUCAUSE survey** that the
search channel could not resolve to the primary instrument. **Not adopted.**

## 🆕 `p552` — `2026-10-30` — **🟢 `Trend 59`: ACADEMIC RELEASE PRACTICE, NOT DISCOVERY, IS THE BINDING CONSTRAINT ON EDUCATION-AI SUPPLY — 3 OF THIS PASS'S 5 BEST RESEARCH ARTEFACTS ARE LIVE, ON-DOMAIN AND UNGRANTED. 🟢 `Trend 60`: THE SOURCE-AVAILABLE LICENCE ARRIVES IN EDUCATION, AND IT EXCLUDES CONSULTANCIES BY NAME.**

### 🟢 `Trend 59` — the supply ceiling is a licensing ceiling

🔴 **Measured, not asserted.** The curated-list channel yielded five novel addresses; **one**
carries a grant. The three that do not are not weak projects:

- [`eth-lre/PedagogicalRL`](https://github.com/eth-lre/PedagogicalRL) — **53★**, **EMNLP 2025
  Oral**, ETH Zurich Learning & Reasoning: multi-turn RL for *"aligning models to be tutors
  instead of answerers"*. 🔵 The exact capability every tutoring engagement asks for.
- [`zamling/LecSlides_370K`](https://github.com/zamling/LecSlides_370K) — **ICCV 2025**, a
  370 K lecture-slide corpus.
- [`ai4ed/COMA-LessonPlan`](https://github.com/ai4ed/COMA-LessonPlan) — **19★**, multi-agent
  lesson-plan generation.

🔴 **All three: live, on-domain, published at top venues, and with no licence file on 10
filenames across 3 branches.** 🔵 **The trend:** education AI's research frontier is being
published at a rate the shelves can see and **cannot use**. A paper acceptance creates an
address; it does not create a grant. 🟢 **What follows for Globant:** for this domain the
highest-value, lowest-cost intervention is often *asking* — a licence request to an academic
group costs one email and converts a `NO-GRANT` row into a buildable one, and it is cheaper
than reimplementing an EMNLP-Oral method. 🔵 `Gap 552-E`.

### 🟢 `Trend 60` — source-available arrives, and the exclusion is aimed at us

🔴 [`Oriole-FDU/Wisepen`](https://github.com/Oriole-FDU/Wisepen) (**122★**, Fudan) is
**BUSL-1.1** while describing itself as open source. Its Additional Use Grant permits
personal, educational, academic and non-commercial production use and excludes *"commercial
product, paid service, hosted service, SaaS offering, **consulting deliverable**, or
revenue-generating business activity"*.

🔵 **Why this is a trend and not an anecdote:** BUSL is the licence a project picks when it
wants adoption by its own community and revenue from everyone else. 🔴 **Education is a
near-perfect fit for that shape** — the community is universities, who adopt freely, and the
paying party is the integrator. 🔵 **Prediction, stated so a later pass can falsify it:** more
university-origin education platforms will ship BUSL-1.1 or similar source-available terms,
and the clause that bites Globant will be the *user-class* exclusion, not the copyleft
trigger. 🟢 **Operational consequence today:** `BUSL`, `SSPL`, `Elastic`, `Fair Source` and
`PolyForm` must each be read as a **parameter block**, not a family name — two BUSL-1.1
repositories can differ completely on whether a deliverable may contain them.

### 🔵 Market figures returned this pass — spread recorded, not averaged

| source | 2026 size | later | note |
|---|---|---|---|
| Research and Markets | **$10.6 B** | $42.48 B by 2030 | the broad "AI in education" definition |
| Mordor Intelligence | **$2.37 B** | ~$11.83 B by 2031 | **agentic AI in education specifically** — a narrower cut |
| secondary blogs | $2.4 B – $11 B | — | 🔴 the spread *is* the definition problem, not disagreement |

🔵 **The two anchors are not in conflict** — they measure different things, and a 4.5× gap
between "AI in education" and "agentic AI in education" is the most useful single number on
this table. 🟢 Segment detail worth carrying: **Intelligent Tutoring Systems 26.04 %** share
(2025); **Assessment & Feedback Agents** the fastest-growing segment at **44.36 % CAGR** to
2031. 🔴 **Efficacy is the counterweight and belongs next to the growth figure:** a cited NWEA
2025 study found **0.1–0.2 SD** gains in maths — real, and about **half** the effect of
high-quality human tutoring. 🔵 All figures here are secondary; none was read from a primary
report.

## 🆕 Trend 57 — **The licence, the runtime and the *jurisdiction* are three separate gates, and only the first one is on any shelf**

🟢 **Measured this pass, on this pass's own best finds.** `Trend 55` established that a grant
answers *who owns the code*, not *whether you can run it* — `Gap 550-B`, a desktop app that
is MIT and needs a paid consumer subscription to start. 🟢 **`p551` found the third gate, one
layer further out.**

| gate | question | what surfaces it | this pass's example |
|---|---|---|---|
| **licence** | may we fork it? | 🟢 a grant probe — [`../ingest/probe-grant.sh`](../ingest/probe-grant.sh) | MIT, 1 068 B, title block read |
| **runtime** | can it start? | 🔴 nothing on these shelves — found by reading a README | `Gap 550-B` (ChatGPT Plus required) |
| **jurisdiction** | may it be deployed *here*? | 🔴 nothing on these shelves — found only by holding the regulation beside the repo | **`Gap 551-C`** |

🔴 **The instance.** This pass's two best-starred permissive finds —
[`kmhmubin/Face-Recognition-Attendance-System`](https://github.com/kmhmubin/Face-Recognition-Attendance-System)
(**584★**, MIT, updated `2026-10-28`) and
[`aashishrai3799/Automated-Attendance-System-using-CNN`](https://github.com/aashishrai3799/Automated-Attendance-System-using-CNN)
(**127★**, MIT) — are **biometric attendance systems**. Both pass the licence gate cleanly and
both start. 🔴 **Neither is deployable in EMEA as written**: emotion recognition in schools has
been **prohibited under the EU AI Act since `2025-02-02`** and Annex III point 3 makes
education high-risk where a system assesses or monitors. Neither repository carries a
retention policy, a template-storage boundary, an on-device constraint or a human-confirm step.

🟢 **Why this is a trend and not a note about two repositories.** The three gates fail in
**decreasing order of detectability**: a licence probe is a `curl`, a runtime constraint needs
a README read, and a jurisdiction constraint needs the regulation **held beside** the
artefact — which is the one thing a repository-shaped census never does. 🔴 **So a shelf
built on star counts and licences will systematically over-promise in exactly the regions
with the most regulation**, and the error grows as the shelf gets better at the first gate.

🟢 **The consequence for an engagement is a sequencing one.** The *weakest* regulatory region
in this base's four (LATAM, no binding instrument) imposes the **most demanding reporting**
requirement — an accreditation-grade evidence export — while the strictest (EMEA) imposes a
**prohibition**, which is cheaper to satisfy because it is a hard block rather than a
feature. 🔵 A product designed against EMEA's denylist and LATAM's export is deployable in
all four; one designed against star counts is deployable in none of them without rework.
🔵 Recipe **`P604`** on [`../compose/patterns.md`](../compose/patterns.md#-p551--2026-10-30).

---

## 🆕 Trend 58 — **An artefact's value as a *channel* is independent of its value as a *row*, and every ranking signal this base uses measures only the row**

🟢 **Measured, with a clean comparison in the same pass.** Three discovery legs ran against
the same industry on the same day:

| channel | shape | new addresses |
|---|---|---|
| `open source platform education ERP CRM MIT Apache` | mandated search query, **12th consecutive run** | 🔴 **0** |
| re-phrased sibling query (`Gap 549-D`'s remedy) | search query, first run | 🟡 **4** |
| [`ishandutta2007/Awesome-Attendance-Management`](https://github.com/ishandutta2007/Awesome-Attendance-Management) | **curated list**, 0★, one month old | 🟢 **9 of 13 listed** |

🔴 **Every ranking signal on these shelves would have discarded the winner.** It has **0
stars, 0 forks**, was created and pushed on a **single day** (`2026-09-27`), and sits far
under [`../ingest/config.json`](../ingest/config.json)'s `minStars: 200`. 🟢 It out-supplied
the mandated leg **twelve-to-nothing** and the re-phrased sibling **nine-to-four**.

🟢 **The mechanism is structural, not luck.** A search query returns what an index ranks, so
it **saturates** — `Gap 549-D` measured that, and a re-phrased sibling only moves the
saturation point. A curated list is a **different shape**: one address yields many, it is
assembled by a human with a topical interest rather than by a ranker, and **its usefulness
does not depend on its own popularity.** 🔴 Popularity measures how many people found the
list; it says nothing about how many addresses are *in* it.

🔵 **What this base is missing, registered as `Gap 551-D`:** a **channel-shape axis**. Every
disposition on these shelves grades an artefact *as a row* — grant, stars, liveness, region.
None asks *"is this thing worth more as a channel than as a row?"* 🟢 This pass answered that
question correctly only because the row was so obviously weak that the list had to be read
for something else. 🔴 **An artefact that is a strong row and a strong channel would be
graded on the row axis and its channel value never noticed** — which is the failure mode the
axis exists to prevent, and it is not detectable from inside the current disposition set.

## 🆕 Trend 54 — **A burst rate and a sustained rate differ by 7×, and every trend feed publishes the burst**

🟢 **Measured, not argued.** [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor),
derived offline from this base's own 709 commits by
[`../compose/code/p550-star-velocity/`](../compose/code/p550-star-velocity/README.md):

| Window | Movement | Rate |
|---|---|---|
| 2 days (`p472 → p526`) | `44 177 → 48 900` | 🔴 **+2 361 ★/day** |
| 1 day (`p537 → p550`) | `49 850 → 51 323` | **+1 473 ★/day** |
| **30 days** | `40 600 → 51 323` | 🟢 **+330 ★/day** |

🟢 **The feeds are not fabricating.** `p549` recorded a digest claiming *"2 371 stars
today"*; this base's independent derivation gives **+2 361 ★/day** over that window —
**within ten stars**. 🔴 **What they are doing is quoting a spike as a rate.** The
sustained figure is **7× lower**, and no feed publishes it, because a sustained rate is
not news.

🔵 **Why this is a trend and not a curiosity.** Momentum is the number that decides
whether a studio treats an artefact as a dependency or as a reference. 🔴 **Sized off a
trend digest, `DeepTutor` looks like it is adding a mid-sized project's entire star count
every fortnight.** Sized off 30 days, it is growing fast but ordinarily. 🟢 **The correct
instrument was already in `git log`** — a base that records its own figures over time can
grade every velocity claim in its sector without the channel that makes them, and
`Gap 547-E` proved that channel can vanish for passes at a time.

🟢 **The operational rule: never quote a velocity without its window.** A delta is not a
rate; a rate is not a trend.

---

## 🆕 Trend 55 — **An open-source grant answers who owns the code, not whether you can run it — and the second question is now the binding one**

🔴 **The case.** [`miuuyy/Clew`](https://github.com/miuuyy/Clew) is **MIT**, grant read
first-hand from the payload, clean title block, 9 releases, 212★. 🔴 **Its README:
*"The desktop app requires a ChatGPT **Plus or Pro** plan and permission to use that
plan."*** 🟢 The code is free. **The running system is gated on a third party's paid
consumer subscription.**

🔵 **No probe on this base would have caught it.** This base screens `LICENSE` payloads,
manifests and registry metadata — `Trend 7` (*licences in this sector lie, and the lie is
on the title line*), `Trend 8` (*no licence at all*), shelf rule 16 (*manifest
declaration*). 🟢 **All three channels say MIT here, and all three are correct.** The gate
is in the **install instructions**, which this base reads for version numbers and never
for executability.

🟢 **Registered as a verdict band (`Gap 550-B`): *granted, runtime commercially gated*.**
It sits beside four bands this base already has, and it is the only one that is not about
ownership:

| Band | Question |
|---|---|
| granted / ungranted | is there a grant? |
| not a *code* licence | is it a code grant? |
| per-artefact | does it cover this file? |
| manifest, payload missing | is the grant where it should be? |
| 🆕 **runtime commercially gated** | 🆕 **can it be executed at all?** |

🔴 **Why it is the binding one for an education buyer specifically.** An MIT tutor that
needs every learner to hold a consumer AI subscription is **not deployable into a school
system** — not on cost, not on procurement, and not on the child-data posture that
`Trend 5`'s compliance windows describe. 🔴 **The licence audit passes and the deployment
fails**, which is the most expensive order to discover those two facts in.

🟢 **The remedy is a column, not an instrument:** record, per row, whether the artefact
runs against a **self-hostable** model path. 🔵 This base already wrote the positive case
without recognising it as an axis — [`Swon010191/Math_teacher`](https://github.com/Swon010191/Math_teacher)
*"runs local-first with no API key required (Ollama)"*, which this base noted was *"what
makes it deployable under a data-protection regime rather than only demonstrable."*
🟢 **That sentence is this trend, written one pass early about one row.**

---

## 🆕 Trend 56 — **The sector is copyleft at the platform layer, and the first documented exception is 14 years old and nobody had found it**

🟢 `Trend 6` says *"the sector is copyleft, and that decides the architecture."* 🔴 **Every
institutional platform this base holds confirmed it:** Moodle **GPL-3.0**, Open edX
**AGPL-3.0**, OpenEduCat **LGPL-3.0**, RosarioSIS **GPL-2.0**, openSIS **GPL-2.0**,
ILIAS **GPL**, Sakai. 🔴 The mandated platform leg this pass asked for **MIT or Apache
explicitly** and returned **none** — the search channel cannot find a permissive education
platform because the sector's platforms are not permissive.

🟢 **The exception: [`ilios/ilios`](https://github.com/ilios/ilios) — MIT, `Copyright (c)
2017 The Regents of the University of California`, 560 releases, `v3.141.1`, continuously
maintained since 2012, pushed the day before this pass.**

🔵 **Three things make it a trend rather than one row.**

1. 🔴 **It was invisible to eleven passes of the prescribed queries** and surfaced on a
   topic/licence sweep instead. A 14-year-old, state-funded, permissively licensed
   platform is exactly what the mandated leg asks for **by name**, and the leg has never
   returned it. 🟢 `Trend 13` (*public education code is published more often than it is
   findable*) now has its largest instance.
2. 🟢 **88 stars.** Any star floor would have rejected it. Its real maturity signals are
   **560 tags** and **243 open issues against 42 forks** — a running institutional system,
   not a demo. 🔵 `Trend 47` and `p549`'s `oak-*` row said institutional artefacts
   under-star; this is the strongest case yet.
3. 🟢 **It positions itself UNDER the LMS, not against it** — *"for schools using Moodle or
   Canvas, Ilios provides a **backbone of curricular information**."* 🔵 `Trend 12` says the
   unit of LMS integration is the **institution**, not the product. Ilios is what that
   looks like when someone builds it: the **curriculum ontology** the LMS does not own.

🟢 **The commercial consequence.** A permissive platform changes what a studio can sell:
fork, extend and ship without a copyleft conversation with client legal. 🔴 **That the
only such platform in this sector sat unfound for eleven passes is a statement about the
discovery channel, not about the supply.**

> 🟢 **`p546` adds Trends 44, 45 and 46, and all three are measured rather than
> read.** Trend 44 is the one to take to a client: **the only anchor that is
> region-portable is the interoperability standard** — and the maintained
> implementation of it is usually not the official one. Trend 45 retires a
> source channel this base has been quoting. Trend 46 is about the shelf's own
> decay. 🔴 **Trend 44 also corrects this pass's own first reading**, which had
> the standards layer rotting uniformly; dated per standard it is a clean
> succession, and the retraction is recorded in the trend itself.

> 🟢 **`p547` adds Trends 47 and 48, both measured on this pass's own yield rather
> than read from a channel.** Trend 47 is the one to take to a client: **across six
> newly-found systems only one carried a usable grant**, and the three failure modes
> are not the ones a licence ladder tests for. Trend 48 is an instrument warning with
> a commercial edge — **a repository can be fresh, active and not written by a human**.
> 🔴 **Trend 47 also records a retraction of this pass's own first framing**, which
> claimed the grant-scarcity result as new when `p543` and `p544` had already
> established it and `Gap 543-D` had opened a register precisely to stop it being
> re-discovered.

> 🟢 **`p548` adds Trends 49 and 50, and both are about the instrument rather than
> the market — which is where this pass's evidence actually is.** Trend 49 is the
> one to take to a client, because it changes how a due-diligence report should be
> read: 🔴 **an "unlicensed" verdict in any open-source audit is usually a statement
> about where somebody looked.** Trend 50 measures how long the multilingual-discovery
> escape lasts. 🔵 Trend 47 (*the grant is the binding constraint*) is **reinforced,
> not revised**: `p548`'s one new address is ungranted, making it 1 usable of 7
> across two passes.

> 🟢 **`p549` adds Trends 51, 52 and 53, and all three are measured on this pass's own
> instruments rather than read from a channel.** Trend 51 is the one to take to a client,
> because it is about due diligence on *any* open-source shortlist: 🔴 **a repository can be
> cloneable, licensed and completely absent from GitHub's search index** — so a shortlist
> built from search alone has a blind spot whose size cannot be measured from inside it.
> Trend 52 is the uncomfortable one and it is about this base: 🔴 **a measurement ceiling
> two passes reported was self-imposed**, and the channel that lifted it was written down in
> this base's own shelf rules three passes earlier. Trend 53 is a demand-side finding with a
> number attached: **adoption outruns governance by 3-to-1 in Latin American higher
> education**, measured by an institution rather than a vendor.
>
> 🔵 **`Trend 47` (*the grant is the binding constraint*) is revised for the first time, not
> merely reinforced:** `p549` found six candidates and **one carried a usable grant** — the
> same ratio — but 🟢 **the usable one is the best-granted artefact on this base**, with
> `762` of `854` tracked files carrying an in-header SPDX identifier. 🔵 So the constraint is not
> that permissive grants are rare; it is that **they do not correlate with discoverability**.

## 🆕 Trend 51 — **A repository can be licensed, maintained and cloneable while being invisible to GitHub search — and every open-source census runs through search**

🔴 **The finding, measured rather than argued.** [`PKulal/LMS`](https://github.com/PKulal/LMS)
is an Apache-2.0, REUSE-compliant, multi-tenant LMS: **854 files**, **764** of them carrying
an in-header `SPDX-License-Identifier: Apache-2.0`, `HEAD 2abdade` dated **2026-10-08**,
copyright **Pace Wisdom Solutions Pvt. Ltd.** 🔴 **Two independent GitHub search queries deny
that it exists** (`repo:PKulal/LMS` → `total_count: 0`; `LMS in:name user:PKulal` →
`total_count: 0`), and a full owner enumeration (`user:PKulal`, **31 repositories over two
pages**) does not list it. 🟢 **Three other channels serve it**: the raw payload (HTTP 200,
licence 11 362 B), the git smart-HTTP refs endpoint (HTTP 200, `HEAD 2abdade5…`) and a
`--depth 1` clone (854 files).

🔵 **Why it is a trend and not a curiosity.** Every open-source shortlist in this industry —
including every census on this base since `p529` — is built by asking an index what exists.
🔴 **The index's false negatives are, by construction, the one error class that no
absence-check catches**: `p528` added a resolution probe (`README.md` on `main` *and*
`master`) precisely to stop phantom "ungranted" verdicts, and that probe would have **passed**
here, because the repository is genuinely there. The failure is upstream of it.

🟢 **What to do about it, concretely, in a due-diligence setting:**

1. 🟢 **Never conclude "no permissive option exists" from a search result set.** The strongest
   permissive option in this category was invisible to the instrument and surfaced from a
   plain web search of the artefact class.
2. 🟢 **Verify an address on three channels before grading it:** search metadata (screen),
   `raw.githubusercontent.com` (grant bytes), and `git ls-remote` (existence + releases).
   Absence on any **one** is never absence. Recipe **`P603`**.
3. 🔵 **Record which channel answered.** `Gap 549-A` makes that a cell format, because a
   verdict whose provenance is unrecorded cannot be audited for coverage.

🔵 **Cause not determined and not guessed:** index exclusion has several causes (recency,
owner opt-out, spam heuristics, indexing lag) and this session cannot distinguish them.
🟢 The measurement does not depend on the cause.

## 🆕 Trend 52 — **A measurement ceiling is a claim about a pass, not about a session — and two consecutive passes here proved it the expensive way**

🔴 **The finding.** `p547` recorded *"**Stars are UNREAD for all six new systems, not zero.**
`api.github.com` **and** `github.com` both return **HTTP 403**"*, registered it as
`Gap 547-E`, and `p548` carried the posture. 🔴 **Both `curl` facts are true. The conclusion
is false.** This base's own **shelf rule 17**, written at `p536`, states that the MCP GitHub
server's *search* method is a **separate channel**, that it is open, and that it returns
*"existence, SPDX screen, exact counters, `pushed_at`, default branch"*.

🟢 **Measured this pass: the channel answered 19 of the 20 distinct addresses asked of it**, and all six `UNREAD` cells
resolved — to **0, 0, 0, 0, 2 and 14 stars**.

🔵 **The cost accounting is the interesting part, and it cuts both ways:**

- 🟢 **Signal lost: almost none.** Every one of the six is `0–2★`, which `Trend 47` predicts.
- 🔴 **Credibility lost: real.** Two passes published a ceiling against a measurement the base
  had already shown itself how to take, and `Gap 547-E` was registered against the wrong
  object — the **sidebar** is genuinely gone, the **counter** never was.
- 🔴 **A second cost, found only because the channel came back:** the shelf's largest row,
  [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor), was carrying **49 850★** from
  `p537` against an actual **51 247★** — **+1 397, +2.8 %**. 🟢 Every other re-measured row
  was accurate to within 4 stars and two were exact. 🔵 **Rounded figures decay fastest at the
  top of the shelf**, so a re-measurement budget should be spent **by rank, not by rota**.

🟢 **The generalisation, which is rule 15 sharpened by one turn.** Rule 15 says a *channel* is
the unit of a blockage; rule 17 narrows it to *the method on a server*. 🔴 **Trend 52 adds the
time axis: a blockage is also scoped to the pass that measured it.** A closed-channel note is
evidence about one request at one moment, and carrying it forward as a standing ceiling is how
a base stops taking a measurement it is perfectly able to take. 🔵 **Re-probe every recorded
blocker on the pass that depends on it** — the refutation here cost **one call**.

## 🆕 Trend 53 — **In Latin American higher education, AI adoption outruns governance by 3-to-1 — and the deliverable is the governance, not the model**

🟢 **The finding, from primary institutional sources rather than vendor surveys.**

| Measure | Adopted | Governed | Gap | Source |
|---|---|---|---|---|
| Higher-education institutions, 19 countries | 🟢 **87 %** use AI in ≥1 area | 🔴 **26 %** have a formal framework | 🔴 **3.3×** | **UNESCO IESALC**, 200 institutions |
| Schools, Brazil | 🟢 **53 %** of administrators use AI | 🔴 **22 %** have school guidelines | 🔴 **2.4×** | **Cetic.br, 2026** (national statistical agency) |

🔵 **Why this is a trend and not a statistic.** The gap is **stable across two independent
sources at two different levels of the system** (tertiary and school, regional and national),
which is the pattern that survives re-measurement. 🟡 A third source — the Digital Education
Council's LATAM survey, **92 %** of students and **79 %** of faculty engaging — points the
same way and is labelled a survey, not a census.

🔴 **The complicating number, which must travel with the other two.** A 2026 Universidad de
los Andes census counted **716** AI-related regulatory instruments, rules and legislative
proposals across **23** countries and territories. 🔴 **So there is no single regime to build
against**: a product's compliance surface in this region is **per-country by construction**.

🟢 **What it means for an engagement, stated as work rather than as insight.** The thing
61–74 % of these institutions do not have is **not a model**. It is a framework, an audit
trail, and staff capability — and because the regulatory surface is fragmented, the only
artefact that ports across it is one **anchored to a standard** rather than to a regime.
🔵 That is `Trend 44`'s portability finding arriving a second time, from the demand side:
this base's LATAM supply rows are exactly the standard-anchored ones
([`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) on ENEM,
[`GuilhermeScarpini/agente-bncc-professores`](https://github.com/GuilhermeScarpini/agente-bncc-professores)
on BNCC codes), and 🔴 both are `0★`, so they are architectures to read, not dependencies to
take.

## 🆕 Trend 49 — **An "unlicensed" verdict is a claim about the prober, not the project — and this base just proved it against itself at 347 stars**

🔴 **The finding.** This base published ⛔ **no grant** for
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (347★, 288 forks) for
**nineteen passes**, and told the field *"do not build on it, and do not believe the table
that says you can."* 🔴 **The repository serves the complete, verbatim GNU GPL v2** at
`docs/License.txt` — **17 286 B**, `sha256 224ac3d403e3…b8ba`, declared in prose at
`README.md` **L49–51**, with a second RTF copy at 61 575 B. 🔴 Root `LICENSE`: **404**.

🔴 **The mechanism, which is the transferable part.** Every probe was **root-scoped**:
`p529` tested 5 root filenames, `p547` escalated to **159 filename variants** — all at the
root. 🔴 **Breadth at one directory is not depth**, and escalating variants bought exactly
nothing. 🔴 **`p448` had already published the file's byte count and blob prefix as a
reproduction control** and the shelf still said ungranted, because nothing in the pipeline
ever dereferenced a path it had already enumerated.

🟢 **Why this is a sector trend and not a local bug.** Education platforms are
disproportionately **long-lived institutional PHP/Java codebases** — openSIS, Moodle,
Chamilo, ILIAS, Sakai, i-educar — whose repository conventions predate the
`LICENSE`-at-root norm that modern tooling and every licence-detection API assume. 🔵 GitHub's
own sidebar, SPDX scanners, SBOM tools and procurement questionnaires all read the root.
🔴 **So in this sector specifically, "no licence detected" correlates with repository age,
not with legal status**, and the older and more institutionally embedded a platform is, the
more likely a root-scoped audit will mis-report it as unusable.

🟡 **What a studio does with it.** 🟢 Treat every ⛔ *unlicensed* row in any inherited audit —
including a client's own — as **unread, not absent**. Read the tree recursively, read the
README's licence section, and read the **payload**, not the filename. 🔴 The failure is
asymmetric and expensive in one direction: it **discards usable assets**, and it discards
the oldest and largest ones first. 🔵 Recorded as verdict class `ENUMERATED-NOT-READ`
(`Gap 548-A`) and as a three-field grant read — `declared`, `served`, **and the path**
(`Gap 548-B`).

## 🆕 Trend 50 — **Multilingual discovery works once per corpus, and five of six corpora saturate on first contact**

🟢 **The measurement.** `p547` broke nine consecutive supply saturations by changing the
query *language*, and concluded that corpora *"saturate one at a time."* 🔵 That predicts
that six fresh corpora should yield roughly twice what three fresh ones did. 🔴 **`p548`
ran it: six unexhausted corpora (`fr`, `ja`, `ar`, `hi`, `ko`, `tr`) returned ONE new
address between them, against `p547`'s six from three corpora** — and the one is ungranted
and sixteen months stale.

| Pass | Fresh corpora | New addresses | Usable |
|---|---|---|---|
| `p547` | 3 (`de`, `vi`, `es`) | 6 | 🟡 1 |
| `p548` | 6 (`fr`, `ja`, `ar`, `hi`, `ko`, `tr`) | 🔴 **1** | 🔴 **0** |

🟢 **The discriminator is not language, it is where a country's education developers
publish.** The corpora that yielded for `p547` — German, Vietnamese, Spanish — are ones
whose national edtech developer communities **put code on GitHub with national-language
descriptions**. 🔴 The corpora that saturated immediately route education-AI discussion into
**blogs, news and journal papers** and return the *same English repositories* when asked
for code. 🔴 **Turkish is the extreme case: the leg returned five general-purpose agent
frameworks and not one education artefact.**

🔵 **Said carefully, because the opposite reading is tempting and wrong:** this measures the
**search channel**, not those countries' activity. Japan, Korea and the Gulf plainly build
education AI; this base simply cannot see it through a keyword index in those languages.
🟢 **The operational consequence:** multilingual discovery is a **one-shot** instrument per
corpus, worth running on a corpus *once*, and the remaining unexhausted corpora are a
depleting resource rather than a repeatable method. 🔴 For the regions behind the saturated
corpora, a different instrument is needed — institutional registries, national procurement
portals, conference proceedings — and this base does not have one.


## 🆕 Trend 47 — **The binding constraint on open education AI is not discovery, it is the grant — and the three ways it fails are not the ones anyone tests for**

🔵 **Measured on `p547`'s whole yield, not on a sample.** Eight mandated English-language
legs returned **0** systems this base did not hold. Five language-shifted legs
(`de` `zh` `vi` `pt` `es`) returned **6**. 🔴 **One of the six carries a grant Globant can
build on.**

| Failure mode | Count | What it looks like |
|---|---|---|
| 🟢 **usable** | **1** | `Swon010191/Math_teacher` — MIT, grant file read at `HEAD`, 1 066 B |
| 🔴 **ungranted** | **3** | nothing licence-shaped in the tree, nothing declared anywhere — incl. one with **245 commits** |
| 🔴 **NonCommercial** | **1** | CC BY-NC-SA 4.0, and the prose extends it to *"su código fuente"* |
| 🔴 **declared-but-unserved** | **1** | MIT in `plugin.json` **and** README, **no licence file at any path**, holder `"anonym"` |
| 🔴 **not software** | **1** | 64 bot commits over 11 near-duplicate keyword-slug HTML articles |

🔴 **This is a replication, and the first draft of this trend wrongly claimed it as a
discovery.** `p543` found **3 Vietnamese agents / 0 licences**; `p544` found **1 Russian
agent / 0 licences** and already called the grant gate *"the strongest regularity on this
axis"*; `Gap 543-D` opened
[`measured-unusable.md`](measured-unusable.md) **so the class would stop being
re-discovered**. 🔵 The register caught this pass making exactly the error the register
exists to prevent, which is the strongest argument for keeping it.

🟢 **What is genuinely new, and it is what a client should hear:** the gate now holds in
**two further corpora** (`de`, `es`), and **two of the three failure modes above are
invisible to a licence check.** A procurement step that reads `plugin.json` concludes MIT.
A procurement step that reads the licence *file* concludes "no licence" and misses that the
author asserted MIT twice. 🔴 **And a third mode is not about licensing at all** — see
`Gap 547-B`: an artefact whose tooling decrypts AES-256-CTR schoolbook DRM is unusable
**however it is licensed**, because the regulated act is reading the content
(**UrhG § 95a**, **InfoSoc 2001/29/EC Art. 6**).

🟢 **The action that follows is cheap and this base has prescribed it since `ACTION
p417-A`: ask for the licence.** Three of six are otherwise shelf-eligible, the
counterparties are identifiable individuals rather than corporations, and **one `LICENSE`
commit** moves each from unusable to usable.

## 🆕 Trend 48 — **A repository can be fresh, active and not written by a human — so recency is not liveness**

🔴 [`MarinaVeauvy/ia-educacion`](https://github.com/MarinaVeauvy/ia-educacion) reached
`p547` through the `es` supply leg presenting every signal of a live project: **64 commits,
most recent `2026-10-29`** — the day before the pass. 🔵 **Read at `HEAD` it is a content
farm:** 32 files, no `README`, no licence, and `articles/` holding **eleven near-duplicate
HTML files** whose slugs are permutations of one keyword string
(`como-usar-chatgpt-planificar-clases-eficiente…`). 🔴 **Every commit is authored by
`github-actions[bot]`.**

🔵 **Why this is a trend and not an anecdote.** `p546` closed `Gap 544-C` by dating every
shelf address, and `Gap 546-D` asks the promotion ratchet to rank on that date. 🔴 **A
ratchet ranking on recency alone would have placed this content farm above
`Math_teacher`** (`2026-09-17`, human) — the only artefact in the pass that could be
promoted. 🟢 **So the date field needs a second column it was never specified with:
committer identity.** Registered as `Gap 547-C`: compute staleness from the last **human**
commit, and treat a wholly bot-authored history as `UNDATED`, not `FRESH`.

🟡 **The commercial edge.** Generated edtech content at this scale is now cheap enough to
be ambient, and it is **indexed by the same channels a studio researches through**. 🔵 For
a client this cuts two ways: diligence on an open-source dependency must read the
**committer**, and a client whose own curriculum content competes for search attention is
now competing with machine-generated near-duplicates of it.

## 🆕 Trend 44 — **A curriculum anchor is a border. An interop-standard anchor is a passport.**

🟢 **Stated so it can be disconfirmed:** *of the anchors a domestic education agent can be
built against, only the interoperability standard survives a change of region; curriculum,
statute and institution anchors are non-portable by construction.*

**The evidence is a census of 64 artefacts' own READMEs**
([`../evidence/anchor-classes.2026-10-30-p546.json`](../evidence/anchor-classes.2026-10-30-p546.json)),
run to answer `Gap 544-B`:

| Anchor class | Artefacts | Portable across this base's five regions? |
|---|---|---|
| institution | 8 · 12.5 % | 🔴 **No** — a ministry or a university is one jurisdiction |
| 🆕 **standard** (xAPI · SCORM · LTI · OneRoster · Ed-Fi · ESCO · QTI) | **5 · 7.8 %** | 🟢 **Yes** |
| curriculum (BNCC, National Curriculum, GDPT, OBEC) | 4 · 6.2 % | 🔴 **No** — a curriculum *is* a country |
| statute (Lei 15.100, AI Act, FERPA, LGPD) | 2 · 3.1 % | 🔴 **No** |
| form (plano de aula, ДПО) | 1 · 1.6 % | 🔴 **No** — and never occurs alone, so not an independent class |
| 🔴 no anchor at all | **47 · 73 %** | 🟡 portable because it is anchored to **nothing** |

🔵 **Why this is a trend and not a taxonomy note.** `p543` concluded that domestic supply
is predicted by *"coding against a named national institution or curriculum"*, and treated
that as the thing to look for. 🟢 **It is the thing to look for when counting supply and
the thing to avoid when buying it**: three of the four curriculum-anchored artefacts on
this shelf anchor on Brazil's **BNCC**, which makes them excellent evidence of a live
Brazilian developer community and **useless as a starting point for an engagement in
Madrid, Austin or Jakarta.**

🟢 **The commercial form of the trend:** an engagement that needs to travel should anchor
on the standard and treat the curriculum as **data loaded into it**, not as structure
compiled into it. 🔵 That is exactly the shape
[`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem)
ships — a national curriculum exposed *through* an MCP server and an API — and it is why
that row survived `p546`'s date field while two of its sibling promotions did not.

🔴 **Disconfirming evidence to watch for:** a curriculum-anchored artefact that gets
adopted outside its own country, or a standards-anchored one that turns out to encode one
jurisdiction's profile of the standard so tightly that it does not travel either. 🔴 **And
the measurement's own limits**, which bound the strength of the claim: READMEs only (the
GitHub About line has no byte-exact channel here), and a **named-term** regex, so an
anchor the list does not name reads as absent. Both errors push the 73 % **up**, so the
anchorless share is a ceiling and the class ranking is unaffected.

## 🆕 Trend 45 — **The daily "AI trends" digests are one generator wearing seven hats, and one of them contradicts itself**

🟢 **Stated so it can be disconfirmed:** *the identically-titled daily "AI Open Source
Trends" issues published from many GitHub accounts are a single generator run repeatedly,
so agreement between two of them is one measurement reported twice and is not
corroboration.*

🟢 **Tested at `p546`** (`Gap 545-B`), by reading two accounts' issue bodies for the **same
date**: identical title template, identical *"auto-generated by agents-radar"* footer, and
**identical star figures to the unit** for the repositories they share
(`ollama/ollama` **185 261**, `huggingface/transformers` **168 331**) — with only the
selection and section ordering differing. 🔴 **So this base's two previous uses of
cross-digest agreement as corroboration were invalid**, exactly as `545-B` suspected.

🔴 **And the channel is worse than non-independent, it is internally inconsistent:** one
digest lists four repositories at **`0` total stars** while crediting them **`+2 870`,
`+1 187`, `+1 117` and `+1 034` stars gained today**. 🔵 **A number that contradicts its
own row cannot be rescued by a second opinion from the same generator.**

🟢 **Consequence, and it is a rule rather than an observation:** digests may be used to
*discover an address* and never to *establish a figure*. Every star count on this base
should trace to a sidebar read or an API read; 🔴 the API is refused for unattached
repositories here, so **rounded sidebar figures are the ceiling** and this base should say
"rounded" rather than implying precision.

## 🆕 Trend 46 — **`LIVE` is not `maintained`, and the gap between them is six years wide**

🟢 **Stated so it can be disconfirmed:** *address liveness and project maintenance are
independent properties of a curated shelf, and a shelf measured only for liveness
systematically overstates what a studio can build on.*

🟢 **`p546` closed `Gap 544-C` and dated all 273 addresses on both shelves** (96 seconds,
zero failures). `p545` had reported **`162/162 LIVE`** and read it as evidence that *"a
curated shelf decays more slowly than the queue it came from."*

| | `agents/top.md` (98) | `repos/foundations.md` (175) |
|---|---|---|
| committed within 30 days | 🟢 65.3 % | 🟢 60.0 % |
| 🔴 **no commit for over a year** | **7.1 %** | 🔴 **16.0 %** |
| 🔴 **no commit for over six years** | 0 | 🔴 **6 addresses** |

🔴 **All 273 resolve. Twenty-eight of them have had no commit in over a year, and the
stalest is 11.9 years old.** 🔵 **`LIVE` answers *does this address resolve*; it does not
answer *is anyone still there*.** The concrete case is an entire named project family on
the foundations shelf — the **Apereo Learning Analytics Initiative**, five repositories,
none touched in over six years — which is the layer a learning-analytics engagement would
have started from.

🟢 **The usable form of this trend is a procurement rule, and it is region-neutral:**
*choose an implementation by its last commit date, not by whose logo is on it.* 🔴 On this
base's own evidence the official repository is the dead one in **four of five**
interoperability standards — the ADL reference LRS superseded by Yet Analytics, the
community OneRoster .NET pair by Ed-Fi's own, `amp-up-io/qti3-item-player` by Longsight's
and OpenOLAT's, and `pylti1.3` by `ltijs` and the PHP library. 🔵 **Full succession table
on [`../repos/trending.md`](../repos/trending.md#-p546--2026-10-30).**

🔴 **One distinction the rule must not flatten:** a **ratified specification** that stops
changing is finished, not abandoned. `adlnet/xAPI-Spec` at 1.3 years is fine; its
**reference implementation** `adlnet/ADL_LRS` at 1.4 years is not, because running code
that stops is a liability. 🔵 **Apply the date rule to implementations, not to
specifications.**

# Education AI — Current Trends

**Pass `p546` · 2026-10-30.** 🟢 **highest trend declared: **46****. 🔴 **`p546` could not
reproduce the carried figure "43" and declines to increment it:** of the numbered trends
only **11 — Trends 36 to 46 — carry a heading on this page**, and 1–35 are carried in
prose and tables with no heading to count. 🔵 **"43" was pass arithmetic — the same defect
`Gap 544-E` found behind "seventy-two".** Registered as **`Gap 546-F`**: this page needs a
per-trend declaration, as [`../ingest/foundations-disposition.tsv`](../ingest/foundations-disposition.tsv)
is for tables, before any count of it is trustworthy. Each one is stated so it could be
*wrong* — a trend you cannot disconfirm is a slogan. Where this pass's evidence
**narrowed or contradicted** a trend carried from `p526`, that is marked and the
trend is rewritten rather than quietly restated.

> 🟢 **`p545` adds Trends 42 and 43 and *narrows* Trend 40.** Trend 40 said a search leg
> measures the index it reaches, not the artefact's origin. 🟢 **`p545` shows when reading
> the artefact's own language is nonetheless sound — and the condition is sharp enough to
> apply before the fact.** See Trend 42.

> 🆕 **`p528`, a same-day second pass**, rewrote **Trend 4** (the Moodle reading
> was wrong in shape), sharpened **Trend 9**, and added **Trend 11** on a
> deletion. Trends 1–3, 5–8 and 10 were not re-evidenced this pass and stand on
> `p527`'s sourcing.

> 🆕 **`p529` rewrote Trend 4 again — `p528`'s shape was right and its magnitude
> was wrong by 20× — and added Trends 12 and 13.** Trend 12 is the one a client
> hears first: **the unit of LMS integration is the institution, not the
> product.** Trend 13 is about this base's own instruments. Trends 1–3, 5–11
> were not re-evidenced this pass and stand on their recorded sourcing.
> 🟢 **Trend 2 gained hard numbers:** `DeepTutor` **49,216★** and `OpenMAIC`
> **41,756★**, API-exact rather than rounded.

> 🆕 **`p536` added Trends 22 and 23, and 22 is the one that changes a deliverable.**
> **Trend 22** — the evaluation layer arrives as *permissive rubrics with a
> non-commercial marked corpus attached*, measured across three unrelated publishers —
> is the first pass on which Trend 3's instruments **exist**, and it decides what a
> studio may ship. **Trend 23** is narrow and operational: a grant can live in the
> package manifest, which matters because this sector's measurement tooling ships in R.
> 🟢 **Trend 3 is advanced rather than rewritten** (its instruments are now named and
> filed), and **Trend 21 gains its missing half** — `terracotta` (Apache-2.0) supplies
> the *assignment* and consent machinery `p535` said the estimation libraries could not.
> 🟢 **Trend 20 — popularity is anti-correlated with fitness — gained four
> instances**: `microsoft/Shiksha-Copilot` at **9★**, `terracotta` at **21★**,
> `edu-sharing-python-client` at **0★** and `learning-commons-org/agent-skills` at
> **40★** are all more useful to an engagement than most of this base's four-figure
> rows. 🔴 **And Trend 15 — retrieval is harder than discovery here — is no longer a
> claim about buyers only**: this base files **173 of the 4 141 addresses** it holds,
> and nine passes called that a supply problem. Trends 1–2, 4–14, 16–19 were not
> re-evidenced this pass and stand on their recorded sourcing.

> 🆕 **`p535` added Trend 21 — the procurement gate is becoming causal evidence** — and
> re-checked nothing else: this pass's supply legs returned **zero** unfiled agents, so
> no carried trend gained or lost evidence from them. Trends 1–20 stand on their
> recorded sourcing. 🔴 **Trend 21 is deliberately filed as single-channel**, because
> every host carrying its primary is unreachable from this session.

## 1. The governance gap is the market

Adoption is near-universal and governance is near-absent. **86%** of students
across 16 countries use AI (Digital Education Council); **53%** of K-12 teachers
use generative AI for work, up from 25% in a year (RAND); most US public schools
still have no formal AI policy (Child Trends / US Dept. of Education).

🟢 **Sharpened this pass with a named primary and a sample.** UNESCO IESALC +
UNU-IAS surveyed **200 LATAM higher-ed institutions across 19 countries**:
**87% use AI somewhere, 26% have a formal AI strategy.** A **61-point** deficit,
and the study's own explanation is the important half — adoption is driven by
**individual faculty and students, not institutional policy**. The AI is already
inside the institution, unmanaged.

**So the scarce good is not a tutor. It is a defensible, auditable tutor** — and
increasingly, **governance over AI the client already has** rather than new AI.

**What would disconfirm it:** governance figures catching up to adoption
figures inside a year, or buyers paying for capability over auditability.

## 2. Open-source education agents are APAC-academic, and they are large

[DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, **49.0k★**, Univ. of
Hong Kong) and [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, **41.8k★**,
Tsinghua) are the two largest open-source education agents in the world, both
permissive, both from APAC university labs, **90.8k★ between them**. Both cut
releases on 28-29 October 2026. Four of the thirteen agents on
[`../agents/top.md`](../agents/top.md) are APAC-placed; one is EMEA-placed; none
is LATAM-origin.

**What would disconfirm it:** a North American or European lab shipping a
permissive education agent at 10k★+, or either of these two changing licence.

## 3. Pedagogy is becoming measurable, and almost nobody is measuring it

Two artefacts now exist for "is this agent any good *as a teacher*", as distinct
from "is it any good at the subject":
[pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT)
running **CDPK** and **SEND**, and
[k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
(Apache-2.0, 601★) shipping **eval rubrics** alongside the skills.

🟢 **New evidence, and it is a sales argument.** The pedagogy benchmark is built
on exams from **Chile's Agencia de la Calidad de la Educación and CPEIP**, and
the **SEND** half covers special educational needs and disabilities — the area
where regulators and parents apply the most pressure and where essentially no
vendor can show evidence. Thirteen stars on the repository. 🆕 The **OECD 2026
Digital Education Outlook** reportedly tells institutions to move **beyond
general-purpose AI toward purpose-built educational AI**, which is the same
argument arriving from the procurement side.

**So:** running a pedagogy benchmark costs almost nothing and almost nobody does
it. That asymmetry is a differentiator for as long as it lasts.

**What would disconfirm it:** CDPK/SEND scores appearing in vendor marketing as
standard, or a major lab publishing pedagogical evals by default.

## 4. 🔴 MCP is the education integration layer — **except for the largest LMS**

**This trend is rewritten this pass. `p526` stated it without the exception, and
the exception is most of the market.**

MCP genuinely is the seam where it exists:
[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT, **308★**, v1.16.0
Oct 2026, ~102-128 tools) for Canvas, and
[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) (MIT, 538★) for
retention. Both are licence-clean seams into AGPL and desktop systems that must
not be forked.

> 🔴 **`p529` correction.** `p528` rewrote this trend as *"eleven codebases,
> nobody converged"*. The GitHub search API reports **222**. The conclusion
> *"no credible bridge"* **survives** — the ceiling is **52★ and ungranted**, and
> the permissive leader is 45★ and eight months stale — but *"eleven people
> tried"* becomes *"hundreds tried, one per campus"*. See **Trend 12**, which is
> what the real number turned out to mean.

🔴 **But Moodle — the sector's largest install base and plugin ecosystem — still
has no credible MCP server**, and ⚠️ **`p527`'s account of *why* was wrong.** It
read the field as *"roughly three real codebases."* `p528` probed **twelve
addresses first-hand** (existence first, then the licence title block) for a
census of **thirteen**, and found
**eleven independent codebases plus two forks**, in four languages, with tool
counts from **8 to ~230**, and **37 stars across every counter read**. Ceiling
unchanged at **27★**
([G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp), MIT, Rust, the only
one naming three live-tested Moodle versions). Full census in
[`../repos/foundations.md`](../repos/foundations.md).

🟢 **So the honest form of the trend, restated:** MCP is the *intended*
integration layer and the *actual* one only for Canvas and Anki — **not because
nobody built a Moodle bridge, but because eleven people each built their own.**
Ten of the eleven are **MIT**, so the blocker is neither licensing nor effort:
it is 🔴 **the absence of a shared tool vocabulary.** Eight tools in one server,
~230 in another, three of them contradicting their own READMEs on the count.
**Tool counts in this field are marketing, not measurement.**

🔵 **Why that reframes the opportunity.** "Nothing exists" argues for a
greenfield build. "Eleven permissive half-builds and no standard" argues for a
**consolidation plus a specification** — materially cheaper, and the
specification is the defensible part. See **P553**.

**What would disconfirm it:** a Moodle MCP server past ~500★, Moodle shipping an
official one, or 🆕 **two of the eleven converging on one tool vocabulary.** The
third is now the one to watch, and it is the cheapest of the three to cause.

## 5. Compliance timelines have become build windows — and now **differ by buyer type**

**Regulation (EU) 2026/1744** (Digital Omnibus, OJ 24 July 2026, in force 27 July
2026) moved Annex III high-risk education AI from 2 Aug 2026 to **2 Dec 2027**.
Not moved: **Article 50 transparency, live since 2 Aug 2026**, and the
**emotion-recognition ban in schools, live since Feb 2025**.

🆕 **Three dates added this pass, and one of them splits the market.** Two new
Article 5 prohibitions phase in **2 Dec 2026**; national regulatory sandboxes move
to **2 Aug 2027**; Annex I embedded systems to **2 Aug 2028**; and **high-risk
systems used by public authorities, including those already in service, to 2 Aug
2030**. State schools and public universities *are* public authorities across most
of the EU.

**So the EU is not one clock, it is two**, more than two and a half years apart,
and which one a client is on depends on whether they are public or private. Pitch
urgency accordingly — and verify the 2030 date against the regulation before
quoting it to a public client (see the gap note in
[`market.md`](market.md#declared-gaps-this-pass)).

**What would disconfirm it:** a further omnibus, or guidance collapsing the
public/private distinction.

## 6. The sector is copyleft, and that decides the architecture

Moodle GPL-3.0, Open edX and Canvas AGPL-3.0, i-educar and RosarioSIS GPL-2.0,
ILIAS GPL-3.0, H5P GPL-3.0. The permissive cores are
[Oppia](https://github.com/oppia/oppia) (Apache-2.0, 7.0k★),
[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, 449★),
[Sakai](https://github.com/sakaiproject/sakai) (ECL-2.0),
[Kolibri](https://github.com/learningequality/kolibri) (MIT) and
[Mentingo](https://github.com/Selleo/mentingo) (MIT, 101★) — and that is the
whole list. Searched again this pass; still no mainstream Apache/MIT LMS.

🆕 **And the last genuinely unresolved cell resolved the copyleft way.**
[frappe/education](https://github.com/frappe/education) (685★), red on `p526`, is
**GPL-3.0** — while Frappe LMS on the same stack is **AGPL-3.0**. One vendor, one
framework, **two different copyleft regimes**. The lesson generalises: grade the
licence per app, never per vendor.

**So:** build permissive agents that attach across a process or network boundary.
**Never fork an AGPL core.**

**What would disconfirm it:** a major LMS relicensing permissively, or a
permissive LMS reaching mainstream deployment.

## 7. Licences in this sector lie, and the lie is on the title line

Four confirmed traps, all read from the licence file's title block this pass:
[PageLM](https://github.com/CaviraOSS/PageLM) (2.1k★) opens with the MIT sentence
and is a bespoke non-commercial licence titled *"PageLM Community License"*;
[advisingapp](https://github.com/canyongbs/advisingapp) (340★) is **Elastic-2.0**;
[cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) (5.1k★) is
**CC-BY-NC-4.0** and only looks like BY-4.0 if a probe drops `NonCommercial`.

🆕 **And a fourth, found this pass, where the repository contradicts itself:**
[ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) (91★) — sidebar
`GPL-3.0`, **README badge `License: MIT`**, licence file title block `GNU GENERAL
PUBLIC LICENSE Version 3`. **The grant wins; a badge is a claim.**

**So the rule, now four-part:** grade from the **title block**; check
`LICENSE.md`/`LICENSE.txt`/`license.txt` as well as `LICENSE`; when badge and
sidebar disagree, **the licence file decides**; and never drop a `NonCommercial`
qualifier. Run it as a gate — see
[`../compose/patterns.md`](../compose/patterns.md).

**What would disconfirm it:** a pass finding no new trap. Seven consecutive
passes have found at least one.

## 8. 🆕 "No licence at all" is the failure mode nobody writes down

A separate category from the mislabelled, and this pass is the first to record it
on this base: repositories with real stars and **no licence file at any common
path**, on any common branch. Default copyright applies; the code cannot be used.

[A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant)
(**64★**, 6 agents, RAG Q&A) offers only a README sentence — *"open source and
available for educational purposes"* — which names no licence and grants nothing.
[idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow)
(25★) shows a **"License" entry in the sidebar that anchors into the README**, not
to a file — the most convincing version of the mistake.
[tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) was described in a
search result as *"MIT licensed"* and has no licence file at all.

**So:** an absent grant is a *harder* blocker than a bad one — there is no
counterparty to negotiate an exception with. And a search summary is not a
verification channel.

**What would disconfirm it:** these repositories adding licences; it would not
disconfirm the category.

## 9. 🆕 The packaging unit is becoming the *skill*, and the differentiator is provenance

The fast-growing tail is no longer applications but **agent skills**:
🆕 [lineage-skill](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0,
462★, 70 forks**) is the highest-starred new entry on
[`../agents/top.md`](../agents/top.md) this pass, and
`universal-examprep-skill` (361★), `universal-diagnostic-tutor-skill` (252★),
`kaogong-skill` (210★) and `education-skills` (119★) sit underneath it.
[Bloom](https://github.com/Li-Evan/Bloom) (294★) ships as a skill *and* a web app.

🟢 **The sharpening:** what distinguishes `lineage-skill` is not that it is a
skill but that its output is **source-backed** — a generated lesson traces to the
material it came from. That is the same property Trend 1 says buyers are short of,
Trend 3 says is measurable, and Trend 5 says India and China now *require* for
AI-generated content. **Provenance is where the governance gap, the evaluation
gap and the labelling rules converge**, and it is the cheapest thing to design in
and the most expensive to retrofit.

🆕 **`p528` adds the licence half of this trend, and it is the part that bites.**
The largest skills library in education is
[GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills)
— **926★, 130 forks, 165 skills across 20 domains, 157 MCP tools**, `v3.1.0` on
22 Oct 2026 — and it is **CC BY-SA 4.0**, a *content* licence. ShareAlike
propagates to adaptations, there is no patent grant, and the repository ships a
working server and 165 prose skills under one grant without drawing the
code/content line. 🔵 **As the packaging unit shifts from application to skill,
the licensing question shifts with it — from "can we fork this code" to "what
does this grant actually cover."** A content licence on an artefact that an agent
executes is a new question, and `MIT`-shaped intuitions answer it wrongly. See
the fourth verdict band on [`../agents/top.md`](../agents/top.md).

**What would disconfirm it:** skills plateauing while monolithic apps resume
growth, provenance staying absent from procurement questions, or the big skill
libraries relicensing to Apache-2.0 — which would retire the licensing half
without touching the packaging half.

## 11. 🆕 The query language, not the query depth, is what bounds a sector census

🔵 **Measured this pass, and it is the most actionable methodological result
on this base.** The mandated research legs — run in English at full depth —
produced **twenty candidates and zero new findings**: five supply addresses
and fifteen regional policy claims, every one already held
([`gate-restated-presence`](../compose/code/p541-restated-presence/) graded
them against the committed tree, so this is a measurement rather than an
impression). The **same legs in Spanish and Portuguese, at the same depth,
returned eight new addresses out of ten.**

🔴 **What that implies for anyone sizing an open-source sector:** an
English-only census of education AI is not a census that is slightly
incomplete, it is one that is **saturated and therefore looks finished**. The
appearance of completeness is the failure. 🔵 `p529` established that
*"saturated" is a property of the query, not of the region*; this pass shows
the same holds for the **language** of the query, and the effect size is
larger.

🟢 **The practical form:** for a LATAM or Iberian engagement, run the supply
survey in the client's own language before concluding anything about available
components. For this base, the artefacts that turned up — an accessibility
adapter from a Brazilian federal university, an offline teacher assistant for
rural schools, a Moodle-exchanging skill pack from Spain — are **not** the
kind of thing an English listicle surfaces, and none of them is a translation
of something that is.

## 12. 🆕 A licence title is a claim about a licence, and six of this sector's lie about the body underneath

🔴 **The sector-specific finding, with a denominator.** Of the 37 unresolved
grants in p540's residue, **six reproduce a stock licence body verbatim under
a title that is not that licence** — `SATA` (MIT plus an obligation to star
the repository), *PySilicon Research* (MIT restricted to non-commercial
research), *O'Saasy License Agreement*, `snflwr.ai`'s *Proprietary Software
License* (over a body a classifier reads as AGPL-3.0), `open-webui`'s clause-4
branding restriction over BSD-3, and `INGInious`'s scoped *"most of the
files"* AGPL.

🔵 **Trend 7 on this page already said "licences in this sector lie, and the
lie is on the title line." This pass measured the rate — 6 of 37, 16 % of the
unresolved residue — and found the inverse case matters more:** the title is
*honest* and the **body** is the thing that misleads an automated reader. A
tool that matches licence bodies gets all six wrong in the dangerous
direction, naming a permissive grant where the repository granted something
narrower.

🟢 **So the operational rule, which this base now enforces in code:** read the
**title block** first, and refuse to name a family when the title is outside
the stock table — whatever the body says. A false permissive verdict is the
only licence error a studio actually builds on.

## 13. 🆕 Public education code is published more often than it is findable

🟢 **Seven national-scale education systems — curriculum, learner identity,
study records, admissions, institution register, vocational plans, state
funding — are published in the open by Finland's National Agency for
Education, and this base held none of them as a row for 540 passes.** They
were invisible to the grant instruments for a structural reason worth
generalising: the `LICENSE` file **names** the licence (EUPL 1.1) and **points
at a URL** instead of reproducing the text.

🔵 **The pattern to expect elsewhere:** public-sector code follows
jurisdictional licensing conventions — EUPL in the EU, and the version in force
when the repository was created, not the current one. Six of these seven say
**1.1** while every tool on this base knows only **1.2**. 🔴 Any sector census
that grades grants by matching reproduced licence text will systematically
**miss the public sector**, which is precisely the buyer an education
engagement most often has.

## 10. The buyer is shifting from the learner to the teacher

The 2026 Holon IQ LATAM EdTech 100 shows AI positioning moving **toward
teachers**, with upskilling losing ground; **Teachy** (Brazil, AI lesson
preparation) is the regional incumbent. Gallup + Walton put weekly teacher AI
users at **5.9 hours/week saved** — a measurable, CFO-legible ROI number that no
learner-facing claim matches.

🟢 **This pass adds the supply side.**
🆕 [Claw-ED](https://github.com/SirhanMacx/Claw-ED) (MIT, 63★) and `lineage-skill`
(462★) are both **teacher-facing authoring tools**, and both are local-first with
teacher review in the loop. The tooling is now arriving where the money is.

**What would disconfirm it:** learner-facing subscription products reclaiming
funding share, or teacher tools failing to convert at district level.

## 11. 🆕 Integrity is the half that gets cut — and the evidence is a merge commit

The clearest signal this pass is a **deletion**, which is a stronger form of
evidence than a launch because nobody ships a deletion for attention.

🔴 [`AIEd-Innovations/assessment_agent`](https://github.com/AIEd-Innovations/assessment_agent)
(**Apache-2.0**) was the one open agent doing grading **and** integrity in one
pipeline. **PR #19 — *"Remove the integrity check: the agent only grades"* —
merged to `main` on 27 Oct 2026.** It removed the anomaly-detection LLM call, the
anomaly report log, the `GET /anomalies` endpoint and the `anomaly_report` result
field. An integrity risk **no longer routes a submission to review.** The stated
reason is cost: **one LLM call per submission instead of two.**

🔵 **Read it as unit economics, not as one team's preference.** Integrity was the
second inference call, it doubled the per-submission cost, and it was the half
that went. That is the same pressure every grading deployment is under, and it
predicts where the open tooling will keep thinning out.

🟡 **Meanwhile the permissive supply exists and nobody uses it.** Two MIT
candidates were verified this pass and **both sit at 0★ / 0 forks**:
[gradeops](https://github.com/sonowalvaibhav/gradeops) (VLM grading of handwritten
answers, JSON rubrics, TA override, plus plagiarism detection that looks for
*shared anomalous logic and identical erroneous reasoning* — the right primitive,
because matched *errors* are far harder to explain away than matched text) and
[Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent)
(**zero external APIs, fully on-device**, from-scratch logistic regression
producing an **evidence breakdown for human review rather than a verdict**).

🟢 **Why the posture of that second one matters commercially:** from 2 Dec 2027 an
EU deployer running AI over grading or proctoring is in the high-risk band, where
"explainable evidence for a human decision-maker" is the compliant shape and "a
cheating verdict" is not. **The 0★ repo has the right architecture and no
adoption; the funded deployments have adoption and just deleted the feature.**

⚠️ **Both are single-author projects with self-reported metrics**, and the
proctoring one contradicts itself on its own test count (94 vs 344). Signals, not
dependencies.

**What would disconfirm it:** an integrity capability landing *back* in a
maintained open grading agent, or one of these two passing ~100★ with external
contributors.

## 12. 🆕 The unit of LMS integration is the **institution**, not the product

> 🟢 **`p534` restores this trend's load-bearing clause, which
> `make gate-prose-claims` reported as `CLAIM-LOST`:**
> the integration layer inherits the authority of the system it attaches to,
> **and none of its defences**. 🔵 An MCP server mounted on an LMS speaks with a teacher's or an
> admin's token, so it can grade, enrol and message — while the LMS's own
> consent flows, audit trail and rate limits sit on the *web* path the agent
> does not use. 🔴 That is why every bridge on this base is graded on its
> **write** model (default-off, course allow-list, `confirm=true`) and not on
> its tool count, and why `p534` specifies the Canvas read and write servers as
> two separate mounts in `P569`.

**Stated so it can be wrong:** *if this trend is right, the Moodle-bridge field
should show many single-institution codebases and no scaled product; if it is
wrong, we should see two or three bridges with most of the stars and real
deployment counts.*

🟢 **The evidence says institution.** Of the 26 highest-starred addresses in a
222-address field, **14 exist to bridge one named university's Moodle** —
Universidade de São Paulo, FICH-UNL, UTN, UTN FRLP, Universidad de San Andrés,
Vietnamese-German University, SLIIT, Nottingham Ningbo, Taylor's, UNSW, SPbPU,
RTU MIREA (×2), TU Wien. Almost all are read-only, almost all are student-built,
almost all are under 10★. **No product has consolidated them**, and the field's
most-starred artefact carries **no licence at all**.

🔵 **Why this is the most commercially useful line on this base.** It says the
opportunity is **not** a better Moodle bridge. Hundreds of people can already
write one in a weekend; what none of them can do is make it safe, auditable and
maintainable for an institution that will be asked about FERPA, the EU AI Act or
a ministry's data rules. **The deliverable is a generator plus a governance
model** — tool vocabulary, read-only default, write-gating, token custody,
audit log — not another bridge. See `P558`.

🔴 **The regional distribution is part of the trend, not a footnote.** LATAM
ships **5**, APAC **5**, EMEA **4**, **North America 0**. NA has the largest
AI-education market and builds none of these, which is the signature of a region
that **buys** institutional integration. That is where a productised bridge finds
a buyer rather than a hundred hobbyist competitors.

## 13. 🆕 A measurement channel is a finding, and this base just changed one

**Stated so it can be wrong:** *if this trend is right, re-measuring old records
with a new instrument should change conclusions, not just confirm them.*

🟢 **It did, in both directions, on the same day.** The GitHub search API became
reachable this pass after months of `github-api-proxy-blocked`. It **confirmed**
all fourteen shelf rows, grant and counter — the hand-probe method had been this
base's only instrument, hence unfalsifiable, and it passed. It then **destroyed**
`p528`'s Moodle headline, raised **two** new shelf rows, and showed that **25 of
80 census addresses were already in this base's history** with only 9 ever filed.

🔴 **And it produced two new failure modes within one pass**, which is the part
worth generalising:

1. **`NOASSERTION` is uninformative.** It resolved to a permissive grant, a
   copyleft grant, a non-OSI grant *and* no grant at all. Reading it as
   "ungranted" would have thrown away `thm-mni-ii/feedbacksystem`, which is
   **Apache-2.0**.
2. **Absence from an API search is not non-existence.** A real repository
   (`packbackbooks/lti-1-3-php-library`) did not come back from a call that
   returned six others.

🔵 **The trend, not the anecdote:** every new channel arrives with its own
credulity. This base already had a rule about trusting search summaries; it
needed the *same* rule for a structured API, and did not have it until the API
nearly produced a phantom. **A faster instrument does not reduce the need for a
second one — it raises it**, because speed is what makes skipping the check
tempting.

## 14. 🆕 The new entrants are choosing network copyleft, so the sector's copyleft is a *present-tense* decision

**The claim.** This base has carried *"education is copyleft"* since `p526` as a
statement about **legacy** platforms — Moodle GPL-3.0, Open edX AGPL-3.0, Canvas
AGPL-3.0. `p530` measured the **new** cohort, the AI-native LMS entrants, and the
pattern is not inherited. It is being chosen now:

| Address | Grant | Stars |
|---|---|---|
| [frappe/lms](https://github.com/frappe/lms) | 🔴 AGPL-3.0 | 3 353 |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 AGPL-3.0 | 2 430 |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 AGPL-3.0 | 1 290 |
| [artcc/freelingo](https://github.com/artcc/freelingo) | 🔴 AGPL-3.0 | 213 |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 101 |

🔴 **Every AI-native LMS with traction is AGPL-3.0; the single permissive entrant
is the smallest by an order of magnitude.** AGPL is the open-core commercial
posture — it permits the project while making a hosted competitor
license-impossible — and it is what a 2026 founder picks.

**Why it matters more than the legacy reading.** A legacy copyleft core can be
worked around by sitting beside it. **A copyleft core that is also the AI layer
cannot** — the thing you want to extend is the thing the licence protects. So the
permissive surface of this sector is shrinking in exactly the layer where AI
value accrues.

🔵 **How this is disconfirmed.** If a permissive AI-native LMS passes ~1 000★
within two quarters, or if one of the four relicenses, the trend inverts. Watch
`Selleo/mentingo` as the single clean indicator.

## 15. 🆕 In this sector, retrieval is a harder problem than discovery — and that is a claim about *buyers*, not just this base

**The claim.** `Gap 529-A` is usually read as housekeeping. `p530`'s measurement
says it is the sector's shape: **3 098 addresses in this base, 79 filed, 97
permissive repos described five or more times and never used.** The supply of
open-source education software is not scarce. **What is scarce is the ability to
find the right piece at the moment of need.**

**The evidence that this generalises past this base.** Asked for an open-source
grader this pass, generic web search answered *"I found no open-source agent that
grades students."* There are **three permissive autograders totalling 2 337★**
([nbgrader](https://github.com/jupyter/nbgrader),
[Submitty](https://github.com/Submitty/Submitty),
[otter-grader](https://github.com/ucbds-infra/otter-grader)), two of them from
named universities, all of them a decade old. 🔴 **The market's own
discovery channel reported a mature capability as absent.** An institution
running that same search reaches the same wrong conclusion and buys a vendor
product.

**Why it matters commercially.** It reframes what a studio sells. If supply were
scarce, the asset would be building the missing component. Supply is not scarce,
so **the asset is the curated, licence-verified, regionally-placed index** — and
the evidence that it is an asset is that this base, which exists to be exactly
that, failed at it for 400 passes until it built an index of its own contents.

🔵 **How this is disconfirmed.** If a later pass's promotion queue comes back
near-empty after the ledger runs in front of every pass, then the debt was a
one-off backlog rather than a structural property. **The queue size at `p540` is
the test.**

## 16. 🆕 The reusable layer in this sector is **delivery**, not intelligence — and it is permissive

🔴 **Measured, this pass, over 349 addresses.** `Gap 530-A` asked `p531` to
triage every address a rewrite had dropped from this base. Reading the grant
first-hand for all 349: **203 permissive (58.2%)**, 50 copyleft, 96 unresolved.
🔵 **The useful half of the result is not the ratio — it is what the permissive
203 turn out to be.**

| What the permissive drop set actually contains | Count |
|---|---|
| General-purpose AI/infra that is not education software (`vllm`, `ragflow`, `llama_index`, `dspy`, `qdrant`, `mem0`, `litellm`, `storm`, `gpt-researcher`, `unstructured`, `jitsi`, `appsmith`, `mcp-go`, `syft`, `ort`, `cyclonedx-cli`, `oauthlib`, `synthea`, `basemaps`, `RAG-Anything`, `django-machina`) | **21 of the 38 above 100★** |
| Education systems and libraries | **17 of the 38** |
| The largest single coherent cluster: the **JupyterHub deployment family** (9 live repos, **2 309★**, BSD-3-Clause throughout) | 9 |

🟢 **The trend claim.** The parts of an education deliverable that are already
built, permissively licensed, maintained and boring are the **delivery** parts:
spawn a server per student, authenticate them out of the LMS over LTI, hold the
records in an LRS, schedule the review with FSRS, select the next item with IRT.
🔴 **The parts that are not built are the pedagogical ones** — and that is the
inverse of how the sector's marketing reads, where the model is the product and
the delivery is assumed.

🔵 **What it means for an engagement.** The first week should be spent choosing
from this layer, not writing it; the differentiator has to live in the
pedagogy, the evaluation and the institutional integration. 🔴 **And the layer
is permissive while the platform cores are AGPL-3.0** — so the boundary between
"what we ship" and "what we attach to" is drawn by the licence map, not by
preference. See [`../repos/foundations.md`](../repos/foundations.md) and
pattern `P562`.

---

## 17. 🆕 A field *size* is a fork artefact; a *starred* census is not — and this base had the hole in every query

🔴 **`Gap 530-B` registered that `fork:true` was absent from every API query this
base has ever run, and predicted the fork share would be large.** `p531`
measured it:

| Census | without `fork:true` | with `fork:true` | Δ |
|---|---|---|---|
| `moodle mcp in:name,description` — `p529`'s published field | **223** | 🔴 **312** | **+89 (+39.9%)** |
| `moodle mcp`, unscoped | **251** | 🔴 **340** | **+89** |
| `moodle mcp in:name,description stars:>5` | **14** | 🟢 **14** | **0** |
| `student information system school management in:name,description stars:>40` | **4** | 🟢 **4** | **0** |
| `topic:student-information-system stars:>40` | **4** | 🟢 **4** | **0** |

🟢 **The prediction holds and the consequence does not.** The fork-shaped hole is
real and large — **89 addresses, 28.5% of the forked total** — and it lies
**entirely in the zero-star tail**. At any star floor at all, including the
lowest one this base uses, `fork:true` changes nothing.

🔵 **The rule, which is the part worth carrying:** add `fork:true` when
publishing a **raw field size**, because a field size without it is a floor and
reads like a count. Omit it when the query carries a **star floor**, because it
cannot change the answer and implies a precision the measurement does not have.
🔴 **`p529`'s `total_count: 222` was therefore a floor, not a census** — and
every decision this base took from that field was taken on a starred subset,
where the number was right all along.

## 18. 🆕 The institution ships the platform and the intelligence as **two repositories** — so a platform census under-counts the sector's agents

**The claim, stated so it can fail:** in this sector, an institutional producer
publishes its LMS and its AI layer as **separate addresses under the same org**,
and any instrument that inventories platforms will therefore report the agents as
absent.

🟢 **The evidence this pass is first-hand and it is about this base's own
blindness.** TU München publishes
[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) (**MIT**, 823★, the
platform) and [`ls1intum/edutelligence`](https://github.com/ls1intum/edutelligence)
(**MIT**, 17★, the agents: **Iris** tutor, **Athena** assessment, **Atlas**
competency modelling). This base filed the first on three curated pages across
several passes and **never held the second**, while writing on two of those pages
that *"the agent attaches as a feedback generator behind the existing
autograder"* — a build recommendation for software the maintainers had already
shipped.

🔵 **Why it is a trend and not an anecdote.** The split is what institutional
engineering *looks like*: the LMS has a multi-year release train and a conformance
surface, the AI layer moves on model timelines, so they cannot share a version.
**EduTelligence publishes a 21-row compatibility matrix against Artemis
releases** precisely because the two are decoupled — the matrix is the seam made
visible. `mitodl` shows the same shape (platform elsewhere,
[`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor)
as its own repo), and `1EdTech`, `Ed-Fi-Alliance-OSS` and `learningequality` all
split standards, server and client the same way.

🔴 **The consequence for an engagement, which is the point:** *"there is no open
agent for platform X"* is not a finding until the platform's **org** has been
enumerated, not just its flagship repository. Twice this pass that enumeration
turned "build it" into "mount it". **Disconfirmed if** a sweep of the
institutional orgs this base already cites turns up no further unfiled AI layers
— the test is `Gap 533-A`, and it is cheap: one API call per org.

> 🟢 **`p534` RAN THAT TEST, AND THE TREND SURVIVES IT — with its claim
> strengthened in one dimension and weakened in another.**
>
> 🟢 **Strengthened: the split is not two-way, it is n-way.** MIT Open Learning
> publishes **three** AI repositories, and the one this base had filed was the
> smallest. [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor)
> (MIT, 1★, 159 commits) is the **pedagogical engine**;
> [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai) (**MIT**, 0★, **816
> commits**) is the **service** that runs four agents on LangGraph over Django
> Channels with RAG evaluation and three tracing backends; and
> [`mitodl/agent-kit`](https://github.com/mitodl/agent-kit) (**BSD-3-Clause**,
> 551 commits) is the **toolchain** under both. 🔵 So the unit of institutional
> publication is not "platform + intelligence" but **one repository per release
> cadence** — engine, service and toolchain each move on a different clock, which
> is the same mechanism the Artemis↔EduTelligence compatibility matrix makes
> visible, applied one level deeper.
>
> 🟢 **Also confirmed on a third org:** `Ed-Fi-Alliance-OSS`, whose standards and
> service repositories were filed here, ships
> [`Fiona`](https://github.com/Ed-Fi-Alliance-OSS/Fiona) and
> [`AI-Tools-for-Ed-Fi-SDLC`](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC)
> (both **Apache-2.0**, both **0★**) and neither was held.
>
> 🔴 **Weakened: one named org produced a clean negative.**
> `learningequality` — Kolibri's org, **238 repositories** — ships **no AI-layer
> repository at all**; its two keyword hits are substring false positives
> (`sushi-chef-aimhi`, `sushi-chef-aiep`). `1EdTech`, `jupyterhub` and `adlnet`
> returned zero as well. 🔵 **So the trend is a property of institutional
> *producers of intelligence*, not of institutional producers generally** — a
> standards body or an offline-first platform team may simply have no AI layer,
> and this trend must not be used to assert that an unfound one exists.
>
> 🔴 **And the instrument has a stated limit:** the enumeration matched the
> keyword `ai`, and the pass's most consequential negative —
> [`frappe/flow_client`](https://github.com/frappe/flow_client), **archived
> 2026-10-22** — only appeared under a second query on `flow`. Four of the five
> negatives above are therefore weaker than they read (`Gap 534-A`).

## 19. 🆕 The grant is becoming **path-scoped**, because the artefact is becoming a **dataset**

**The claim:** as this sector's open contribution shifts from code to **corpora,
item banks and benchmarks**, a single repository increasingly carries **two
grants** — a permissive one for the harness and a Creative Commons one for the
data — and a licence model with one grant per repository returns the wrong answer
for exactly the artefacts that matter most.

🟢 **The evidence.** [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark)'s
licence file is titled with the bare word `# Licenças`, names no licence family on
its title line, and then assigns **MIT** to `harness/`, `test/` and config and
**CC BY 4.0** to the item bank (`itens/`), the run results (`resultados/`),
`METODOLOGIA.md` and the documentation — *"porque contém duas coisas de natureza
diferente"*. GitHub's API grades the whole repository `NOASSERTION`. 🔵 The same
division is already visible, less explicitly, in
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
(MIT code, Chilean ministry exam material) and in
[`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) (MIT grader,
separately-credited Essay-BR corpus).

🔴 **Why it bites hardest where the sector's value is growing.** A tutor's
differentiator is the curriculum it is grounded in, and curricula are national
and published by ministries — so the *data* half arrives under CC terms with
attribution and sometimes NonCommercial, while the *code* half is permissive.
🔴 **`CC BY 4.0` is not a software licence and does not grant patent or
sublicensing terms**, so shipping an item bank inside a proprietary deliverable is
a different legal act from shipping the harness, even when one `git clone`
produced both.

🟢 **The practical rule, now in [`../compose/patterns.md`](../compose/patterns.md)
as `P568`:** resolve the grant **per path** before a dataset-bearing repository
enters a deliverable, and record it as `grant | grant@path`. **Disconfirmed if**
the dataset-bearing repositories on this base turn out to be predominantly
single-grant on inspection — which is the backfill `Gap 533-B` asks for and
nobody has run.

## 20. 🆕 In this sector, **popularity is anti-correlated with fitness** — and every ranked instrument on this base has it backwards

**The claim, stated so it can fail:** for an education engagement, an
open-source repository's star count predicts how *useful* it is **negatively**,
because the sector's deployable assets are institutional and its popular assets
are curricula.

🟢 **The evidence is a single table, and it is this base's own promotion
history.** The three highest-star assets it has ever promoted, and the largest
find of this pass:

| Address | Stars | Fitness | What a client could deploy |
|---|---|---|---|
| [`freeCodeCamp/freeCodeCamp`](https://github.com/freeCodeCamp/freeCodeCamp) | **458 181** | `curriculum` | 🔴 nothing — it is a curriculum |
| [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | **78 100** | `curriculum` | 🔴 nothing — it teaches a person |
| [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | **~1 100** | `curriculum` | 🔴 nothing — twelve lessons |
| 🟢 [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai) | 🔴 **0** | `dependency` | 🟢 **four production education agents**, RAG eval, three tracing backends, 816 commits |

🔵 **Why it holds rather than being a coincidence of four rows.** A star is a
signal from *readers*, and the readers of education-AI code on GitHub are
overwhelmingly learners, not institutions. An institution's own deployment
repository has no audience at all: nobody stars the service their university
runs. 🔴 So the sector's two populations — **people learning to build agents**
and **institutions running them** — produce star counts that differ by five
orders of magnitude in the *wrong* direction for a studio deciding what to
build on.

🔴 **The concrete failure this caused, inside this base:** `p533` built a
materiality-ranked promotion queue that gates on grant and liveness and then
orders by **measured stars**. Run against this pass's finds, that queue ranks a
**1★, 159-commit** engine above the **0★, 816-commit** service that runs it,
and both below a curriculum. 🟢 **The fix is not to drop stars but to add the
two dimensions a star cannot carry** — `fitness` (filed this pass on
[`../agents/top.md`](../agents/top.md)) and **depth** (commits, open PRs,
release discipline, a named deployment host). → `Gap 534-C`.

**Disconfirmed if** a star-ordered queue and a depth-ordered queue over the same
gated address set produce substantially the same top ten. 🔵 That comparison is
one run of
[`../ingest/promotion-rank.py`](../ingest/promotion-rank.py) with a second sort
key, and it has never been done.

## 21. 🆕 The procurement gate is becoming **causal evidence**, and the open-source shelf has none

**The claim.** Through 2026 the binding constraint on selling AI into education stops
being capability or compliance and becomes **proof that learning improved** — and
because none of the open-source projects on this base carries such proof, the studio
that ships *measurement* alongside the agent wins the engagement over the studio that
ships a better agent.

**The evidence, and it is one channel.** A coalition reported as **140+ organisations**
(the Alliance for Learning Innovation) published a report on **2026-10-15** urging
Congress and the administration to fund research into whether AI tools actually help
students learn. The review behind the push is reported as finding that of **800+ K-12
AI studies**, only about **20 produced strong causal evidence of learning impact**
(attributed to the **Stanford Accelerator for Learning**). Alongside it, HolonIQ's 2026
outlook holds that systems increasingly *"expect evidence that products improve learning
quality, persistence, well-being, or job-relevant skills"*, and **1EdTech** reports
institutions standing up evaluation processes rather than pilots.

🔴 **Single-channel, and declared as such.** `edweek.org`,
`acceleratelearning.stanford.edu`, `aasa.org`, `holoniq.com` and
`campustechnology.com` are **all `ENOTFOUND` or 000** from this session
([`../evidence/channel-allowlist.2026-10-29-p535.tsv`](../evidence/channel-allowlist.2026-10-29-p535.tsv)),
so the 800/20 ratio is a search-backend report of a review this base **has not read**.
Treat the *ratio* as indicative and the *direction* as the trend.

**What this adds to Trend 3, which it does not replace.** Trend 3 says pedagogy is
becoming measurable and almost nobody is measuring it — an observation about **supply**.
This is the **demand** half, and it is newer and harder: the people with the money have
started asking for causal evidence by name, in the same year venture funding into the
sector fell ~**89%** from peak (see [`market.md`](market.md)). 🔵 Scarce capital plus an
evidence bar is the combination that kills feature-led pitches.

**Why it lands on the open-source shelf specifically.** Of the agents filed in
[`../agents/top.md`](../agents/top.md), the ones with any evaluation apparatus at all are
the minority: [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (**MIT**, 274★) carries
BKT and came out of a university lab, [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai)
(**MIT**, 0★) ships RAG evaluation with LangSmith/PostHog/Opik tracing, and
[`abhijeetgupta23/ai-agent-to-learn-faster-and-better`](https://github.com/abhijeetgupta23/ai-agent-to-learn-faster-and-better)
(**MIT**, 4★) is built around an eval harness. 🔴 **The 49.7k★ flagship,
[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor), is a tutoring system, not a
trial** — which is not a criticism of it and is exactly the gap a buyer will probe.
🟢 **This is Trend 20 again from the demand side**: the repositories with the
measurement apparatus are the ones with no stars.

**How to disconfirm it.** Any of these would falsify or blunt it: a 2027 procurement in
which an AI-in-education award is made with no efficacy requirement in the tender; the
ALI push failing to produce appropriated research funding; a flagship open-source
education agent publishing a randomised trial and *not* gaining adoption from it; or
evidence that buyers accept vendor-run studies, in which case the gate is **marketing**,
not evidence, and the studio play is different.

**What a studio does about it on Monday.** Ship the measurement as a first-class
component of the engagement, not a report at the end — see `P571` in
[`../compose/patterns.md`](../compose/patterns.md).

## 22. 🆕 The evaluation layer is arriving as **rubrics with a non-commercial corpus bolted on** — and the split runs straight through the deliverable

🟢 **Trend 3 has argued since early passes that pedagogy is becoming measurable and
almost nobody is measuring it. `p536` is the first pass on which the instruments
actually exist** — and they arrive with a licence shape that decides what a studio can
ship.

[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
(**87★**, pushed *inside this pass's window*) is exactly the artefact Trend 3 asked
for: *"Evaluation for AI outputs against trusted educational rubrics… research-backed."*
🔴 **Its `LICENSE.md` grants three different things three different ways:**

| Artefact | Grant | Can a studio ship it? |
|---|---|---|
| Evaluator **code** | **MIT** | 🟢 Yes |
| Evaluator **content** — the prompts and settings, i.e. the rubrics | **CC BY 4.0** | 🟢 Yes, with attribution |
| Annotated **CLEAR Corpus** (orig. CommonLit) | 🔴 **CC BY-NC-SA 4.0** | 🔴 **No** — non-commercial, and ShareAlike |
| Annotated **PERSUADE 2.0** (orig. [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0)) | 🔴 **CC BY-NC-SA 4.0** | 🔴 **No** |

🔵 **Why this is a trend and not one repository's choice.** The same shape appears
three times in this base's own holdings, from three unrelated organisations:

- `evaluators` — permissive code and rubrics, **non-commercial marked corpora**.
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
  — MIT code, data licensed **per dataset and per download** (Open / Open + Gated /
  Gated), with the payload stating that distribution *"doesn't consolidate those into a
  single license for your build."*
- [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) (`p533`) —
  **MIT** for `harness/` and `test/`, **CC BY 4.0** for the item bank and the results.

🔴 **The common structure: the executable part is permissive and the *marked ground
truth* is not.** That is not stinginess — marked data is the expensive artefact, it
usually carries an upstream grant the publisher cannot widen, and in `evaluators`' case
both corpora were already `CC BY-NC-SA` before Learning Commons annotated them.
🟢 **The consequence for an engagement is specific and plannable:** you can ship the
evaluator, the rubrics and the pipeline; you cannot ship, redistribute or
commercially train on the corpus you calibrated against. So **calibration becomes a
licensing question**, and the only fully permissive alternative on this base is
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
(**MIT**, 13★ — CDPK and SEND).

🔵 **The architectural answer, and it is cheap if decided early:** keep the corpus on
the *other side* of a boundary. Calibrate in a non-shipped evaluation environment,
record the rubric version and the resulting thresholds, and ship the thresholds — not
the data. That is `P572`'s second half, and it is the same move `p535` made for
efficacy estimation running beside the LMS rather than inside it.

🔴 **What would falsify this trend:** a permissively-licensed, *annotated* education
corpus of comparable size appearing from any publisher. None exists on this base today,
and `pedagogy-benchmark` is a benchmark of **model** pedagogical knowledge, not a marked
corpus of **student** work — so it does not fill the hole, it sidesteps it.

## 23. 🆕 A grant can live in the **package manifest**, and this sector's measurement tooling is where that bites

🟡 Narrow, cheap to act on, and it falsified three of this base's own instruments in one
row. [`sonsoleslp/tna`](https://github.com/sonsoleslp/tna) is a CRAN package
(**`tna` 1.3.1**, Transition Network Analysis) whose `LICENSE` file is **45 bytes**:

```
YEAR: 2025-2026
COPYRIGHT HOLDER: tna authors
```

🔴 That is not a grant and not an absence — it is **R's two-parameter template file**,
and the family is declared in the manifest: `DESCRIPTION` reads
`License: MIT + file LICENSE`. 🔴 **Three instruments, three wrong answers:** the GitHub
API says `NOASSERTION`; a title-block reader finds no family; an absence-reader finds a
file present and records *"granted, family unknown"*.

🔵 **Why it matters here rather than in general.** This sector's *measurement* layer —
learning analytics, psychometrics, educational data mining, item-response theory — ships
disproportionately in **R**, so a base that reads only licence payloads will
systematically mis-grade the exact tooling an efficacy or evaluation engagement needs.
`tna` is the instance; `sonsoleslp/tna`, CRAN's `ltm`, `mirt` and `lavaan` are the
class. 🟢 Remedy is **shelf rule 16**: read `DESCRIPTION`, `package.json`,
`pyproject.toml`, `Cargo.toml` and `*.gemspec` before grading, resolve manifest-vs-payload
conflicts to the payload, and record which channel answered.


## 24. 🆕 A "trending" query in this sector measures an **aggregator**, not a field — and it bottoms out at 2★

**Stated so it can be wrong:** *if the mandated `github trending {industry} AI {year}`
leg were reaching GitHub's own trending signal, its results would be distributed like a
trending list — a few large repositories and a tail of mid-size ones. If instead it is
reaching machine-written digests, the tail will be absurd.*

🔴 **It is absurd.** `p537` ran the leg and resolved every education repository it
surfaced alongside DeepTutor:
[`LeoLiu363/ai-video-understanding`](https://github.com/LeoLiu363/ai-video-understanding)
**2★**, [`upstream1119/Traceable-Ideological-Education-RAG`](https://github.com/upstream1119/Traceable-Ideological-Education-RAG)
**2★**, [`tanghua-git/skill-instructional-design`](https://github.com/tanghua-git/skill-instructional-design)
**2★** — all three sourced from auto-generated *"AI Open Source Trends"* GitHub
**issues** in bot repositories, not from `github.com/trending`.

🔵 **Why this is a trend about the sector and not just about a query.** Education
is a thin slice of AI open source, so general-purpose AI aggregators have almost nothing
education-shaped to rank — and rather than return nothing they return their own
distribution's floor. 🔴 **The practical consequence is a measurement error this
base made nine times**: the leg's nil result was read as evidence that education agent
supply is thin, when it is evidence about an aggregator. Supply this pass found in the
base's own prose included [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil)
at **1 840★**.

🟢 **Disconfirmed by:** a trending leg returning an unfiled education repository
above, say, 200★. That has not happened in ten passes.

## 25. 🆕 The Gulf inverts this sector's licence gradient: **highest adoption, least buildable supply**

**Stated so it can be wrong:** *the usual pattern on this base is that adoption and
permissive supply move together — North America and APAC are high on both, and the
EMEA blank was a measurement gap rather than a real one. If that generalises, the Gulf's
exceptional adoption should come with exceptional supply.*

🔴 **It does not.** The region carrying the highest teacher-adoption figure this
base holds (**UAE ~75 %**, `p535`) publishes, across its two leading AI institutions,
nine education-relevant repositories of which **one** is permissively licensed:

- 🔴 **4 × GPL-3.0** — KAUST Academy courseware, flagship at **443★ / 88 forks**
- ⛔ **4 × no grant at 21 probed paths** — including two pushed within ten weeks of the read
- 🟢 **1 × Apache-2.0** — [`mbzuai-oryx/groundingLMM`](https://github.com/mbzuai-oryx/groundingLMM)
  (969★), and it is a capability model, not an education project

🔵 **The mechanism, and it is what makes this a trend rather than a tally.** The
Gulf's AI institutions are *universities publishing teaching and research output*, not
vendors publishing products — and university output defaults to GPL-3.0 (courseware) or
to no grant at all (paper code). A region whose AI capacity is built institution-first
will therefore look adoption-rich and supply-poor **by construction**, and the inference
"high adoption ⇒ forkable supply" fails exactly there.

🟢 **Disconfirmed by:** a Gulf ministry or Gulf vendor publishing a permissively
licensed education platform. None was found; `Khalifa University`, `KFUPM` and
`NYU Abu Dhabi` returned nothing education-relevant.

## 26. 🆕 The EU's education obligations have **split in time**, and the 16-month gap is the sequencing window

**Stated so it can be wrong:** *"the EU AI Act applies to education from August 2026"
is the claim a single-date reading produces. If the obligations have actually split, a
deployer's near-term work and its 2027 work are different work.*

🔴 **They have split.** Under the **Digital Omnibus, Regulation (EU) 2026/1744**:

| Obligation | Status |
|---|---|
| Article 50 — chatbot / AI-interaction **transparency** | 🔴 **Live, on schedule, 2026-08-02** |
| Annex III **high-risk** duties for stand-alone education systems (access, progression, assessment) | 🟡 **Deferred 2026-08-02 → 2027-12-02** |
| **Emotion recognition** in schools | ⛔ **Banned since 2025-02** |
| AI-literacy duty | 🟡 **Disputed across sources** — recorded as unresolved, not settled |

🔵 **What follows for an engagement, and it is the opposite of "we have until
2027".** Disclosure, logging and the deployer-vs-provider boundary are **due now** and
are cheap; conformity assessment, risk management and human-oversight evidence for
grading and admissions are **due 2027-12-02** and are expensive. 🟢 So the correct
EMEA sequence is *transparency and record-keeping first, conformity work second* — and a
studio that sells those as one 2027 programme has mispriced the near half.

🔴 **The deployer/provider split is the part clients get wrong:** a school that
licenses a platform is a **deployer**; the vendor is the **provider** and carries most
design and conformity duties. A studio building *for* an institution may be making that
institution a provider.

## 27. 🆕 This sector's permissive supply sits at the **edges** of the stack while its **centre** is copyleft — so an engagement inherits both problems at once

**The claim.** In education specifically, licence permissiveness is
*anti-correlated with architectural centrality*. The systems an institution
actually operates are overwhelmingly copyleft; the tools that would extend them
are overwhelmingly MIT and overwhelmingly abandoned-scale.

**The evidence, from this base's own tables rather than a survey.** Platform
cores: **Moodle** GPL-3.0, **Open edX** AGPL-3.0, **OpenSIS** GPL-2.0,
**OpenEduCat** LGPL-3.0. Edge tools filed at `p538`:
[`SIMG`](https://github.com/guruduan/SIMG) MIT **1★**,
[`EduShield`](https://github.com/oas114/EduShield) MIT **11★**,
[`EDUCA`](https://github.com/shishiv/EDUCA) MIT **1★**,
[`SwiftyPSCore`](https://github.com/dougpenny/SwiftyPSCore) MIT **6★**,
`capy-note` and `prep-ybara` MIT **1★** each, the three `mizcausevic-dev`
compliance repos MIT **0–1★**. 🔴 **Nine of the eleven newly filed permissive
artefacts are in single digits of stars.** Meanwhile `p537`'s Gulf set returned
**four GPL-3.0** courseware repositories and **four with no grant at all**.

**Why it matters commercially, and it is not the obvious point.** The obvious
read is "copyleft at the centre is a licensing problem." It is not, for most
engagements: running a GPL LMS and writing a separate agent against its API
triggers nothing. 🔴 **The real cost is that the permissive layer cannot be
depended on** — a 1★ single-author repository with no release is a specification
you read, not a dependency you pin. So an engagement pays twice: **once in
copyleft discipline at the platform boundary, and once in writing the edge
tooling that exists but is not yet dependable.**

**How to disconfirm it.** Find an education edge tool — an LMS plugin, an
anonymisation layer, a SIS client, a compliance artefact — that is permissively
granted, above ~500 stars, and has tagged releases. 🟢 **One candidate already
exists and is the exception that sharpens the rule:**
[`alterem/knowledge-grab`](https://github.com/alterem/knowledge-grab), MIT,
**567★**, 52 forks. It is an edge tool, permissive and genuinely adopted — and
it is a **content-acquisition** tool, not an extension of any platform. Find
three more that *do* attach to a platform and this trend is wrong.

## 28. 🆕 **Offline-first is turning from a connectivity workaround into a compliance architecture**

**The claim.** Local-only processing in education software used to be about bad
networks. It is now also being chosen for **regulatory** reasons, and the two
rationales are converging on the same designs.

**The evidence.** The EU's stand-alone Annex III high-risk obligations land
**2 Dec 2027** for systems that evaluate learners or gate qualifications
(Regulation (EU) 2026/1744), with Article 50 transparency already at
**2 Aug 2026**. Against that: `p538` filed
[`capy-note`](https://github.com/florianchristophnowak-dot/capy-note) — **offline**
grading of scanned exams, Electron, no service — and
[`prep-ybara`](https://github.com/florianchristophnowak-dot/prep-ybara), a local
Windows lesson planner, both German-language. 🟢
[`oas114/EduShield`](https://github.com/oas114/EduShield) (Taiwan) does
de-identification as **one static HTML file with no backend**, with an optional
**local** LLM scan over Ollama. And the proctoring candidate this base already
holds,
[`Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent),
is *"fully local, zero external APIs"* with from-scratch logistic regression for
**explainable** risk.

🔵 **The convergence is the finding.** A school in rural Indonesia and a
Gymnasium in Bavaria are arriving at the same architecture for opposite
reasons — one cannot rely on the network, the other does not want the data
leaving the building. **That makes offline-first a single engineering investment
serving two distinct markets**, which is unusual and worth pricing accordingly.

**How to disconfirm it.** Show that the German and Taiwanese artefacts above are
offline for *convenience* (single-developer projects avoiding hosting) rather
than by design. 🟡 **That is a live possibility** — all three are 1–11★
single-author projects, and a solo developer avoids a backend because backends
cost money. **The regulatory reading is an inference from timing and
jurisdiction, not a claim any of their READMEs makes.** Stated so it is not
quoted as their authors' intent.

## 29. 🆕 In a given category, **the most-starred project can be the one you may not use** — and visibility does not predict a usable grant

**The claim.** Star count carries no information about whether a grant exists.
In this sector the *leader* of a category is, with some regularity, ungranted.

**The evidence.** The Moodle MCP field's most-starred bridge is
[`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) — **52★, 14 forks,
24 documented tools, the richest published tool vocabulary in the category** —
and it has **no licence entry in its sidebar and none in its title block**. The
three alternatives below it are all MIT. 🔴 **The census on this base read the
field as *"ten of eleven MIT"*; its leader is the eleventh.** Across the top 80
Moodle-MCP addresses by stars, `p529` measured **18 with no licence and 4
`NOASSERTION` — 27.5 % with no usable grant.** The pattern repeats elsewhere
here: `A-R007/Multi-Agent-Study-Assistant` at **64★** ungranted,
`DMontgomery40/mcp-canvas-lms` at **104★** which only resolved as MIT once its
*manifest* was read.

**Why it matters.** Any ranked shortlist built from popularity — which is what a
trending query, an awesome-list or a search summary gives you — is **biased
toward the unusable** at the top. 🔵 **So grant resolution has to happen before
ranking, not after.** This base learned that the expensive way: it has a
dedicated verdict band for *"stars but no grant at all"*, a second for
*"granted, but not under a code licence"*, and a third for *"the grant is
per-artefact."*

**How to disconfirm it.** Take any education category on this base, rank by
stars, and show the top entry is permissively granted in **four of five** cases.
🔵 The honest counter-evidence is that the sector's single largest agent,
[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) at **49 850★**, is clean
**Apache-2.0** — so this is a claim about *category leaders in thin categories*,
where one 50★ project can lead, and not about the sector's headline projects.

## Counter-signals worth holding

- **ANZ leans toward banning AI in schools** (Ipsos Education Monitor 2026) while
  the rest of APAC leans against a ban. Capability-led pitches fail there.
- **Trust in the sector is damaged, not neutral.** China shut its ~$100B private
  tutoring industry in 2021; India's BYJU'S collapsed into insolvency. APAC AI
  tutoring is rebuilding from a low base of trust, not a high one.
- **Market-size estimates diverged rather than converged** this pass: the 2026
  band is now **USD 6.4B-12.3B**. Quote the 30-35% CAGR, not a point estimate.
  🆕 **`p534` widens it further and the widening is the signal.** Three firms
  read this pass: The Business Research Company **$10.6B (2026)** at 40.9 %,
  IMARC $6.4B (2025) → $79.6B (2034) at 31.35 %, Persistence **$3.7B (2026)** at
  21 %. 🔴 **High over low for the same year is 2.9×**, all three are
  vendor-sponsored, and the band should be quoted as **$3.7B–$10.6B, 21–41 %**.
  🔵 **The one figure from that sweep worth more than the band:** teacher AI
  professional development moved **29 % (early 2024) → 50 % (late 2025)**, and
  K-12 holds **45.62 %** of adoption while higher education holds the revenue —
  the sector's users and its money are in different segments.
- 🆕 **Policy is not deployment.** UNESCO's APAC analysis is blunt that adoption
  needs **infrastructure, connectivity and teacher training**, and that much of
  the region has unmet basic educational needs first. CENIA says **13 of 19 LAC
  countries** have not begun. A regulatory calendar is not a readiness signal.
- 🆕 **Stars are not maturity, in either direction.** `pedagogy-benchmark` is the
  most procurement-useful repository on this base at **13★**; `ralph`, the xAPI
  seam the whole analytics argument rests on, has **51★**. Meanwhile 64★ bought
  no licence at all. Read the repo.

## Source-quality note

Trends 4, 5, 6, 7 and 8 rest on **primary artefacts** — licence files and
repository pages read first-hand this pass, plus a named EU regulation. Trends 1,
3 and 10 rest on **named studies** (UNESCO IESALC + UNU-IAS, RAND, Gallup +
Walton, Digital Education Council, Holon IQ, Ipsos, OECD). Trend 2 and 9 rest on
**repository evidence**, with star counts as rounded page values because
`api.github.com` is unreachable from this session.

Weakest links, named: **market sizing** (vendor and blog aggregation, widening
band), **EMEA vendor funding detail** (trade aggregators that disagree with each
other), the **EU public-authority 2 Aug 2030 date** (single commentary source),
the **OECD Outlook recommendation** (reported, not read from the Outlook itself),
and **APAC curriculum status** (sources mutually contradictory).

---

## 🆕 `p533` — the seventeen carried trends re-checked; **two added, none contradicted**

🔵 All four global legs and all four regional legs were run. **No carried trend
was narrowed or contradicted**, and two were added from first-hand evidence
rather than from a market query — which is where this pass's new information came
from generally.

- 🟢 **Trend 2 confirmed, sharper counter.** `DeepTutor` reads **49,574★**
  (API-exact) against `p529`'s 49,216 and `p532`'s "49.5k", still **Apache-2.0**,
  still the sector's largest. 🔴 **And the trend's APAC-academic framing now has
  a measured counterweight:** the two largest *institutional* permissive assets
  filed this pass are **EMEA** (`Artemis` + `EduTelligence`, TU München) and
  **North American** (`Autolab`, Carnegie Mellon). The trend's claim was about
  the *top of the star distribution* and that is unchanged; its implied claim
  that permissive institutional supply is APAC-only is **narrowed**.
- 🟢 **Trend 6 confirmed and made more precise, which lowers a cost.** "The
  sector is copyleft, and that decides the architecture" stands — but this pass
  separates **GPL-3.0 from AGPL-3.0** in practice: [`judge0/judge0`](https://github.com/judge0/judge0)
  (**GPL-3.0**, 4,498★) is deployable as a **separate network service** a
  proprietary deliverable calls, because GPL-3.0 has no §13, where
  [`classroomio/classroomio`](https://github.com/classroomio/classroomio)
  (**AGPL-3.0**, 1,735★) in the same position is not. 🔵 This base had been
  collapsing both into "integrate, do not fork" — correct for AGPL, needlessly
  expensive for GPL.
- 🟢 **Trend 4 (Moodle) and Trend 12 (the institution is the integration unit)
  both confirmed by the same new row.** [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp)
  (**MIT**, PyPI `2.5.0`) bridges **Librus Synergia**, a *national* Polish
  gradebook — the first non-Anglosphere register bridge here, and the shape
  Trend 12 predicts.
- 🟢 **Trend 15 confirmed emphatically** ("retrieval is harder than discovery in
  this sector"). Six consecutive passes of generic search producing no new
  shelf-grade supply, while this base's **own history** yielded a 458,181★
  BSD-3-Clause asset and a three-agent MIT suite in a single pass. See
  [`../repos/trending.md`](../repos/trending.md).
- 🟡 **Trend 1 (the governance gap is the market) holds and gains its cleanest
  number**, LATAM: **74%** of surveyed institutions using AI in teaching and
  learning against **26%** holding a formal AI strategy, over a 200-institution,
  19-country UNESCO IESALC base.
- 🔴 **Not re-evidenced this pass and standing on recorded sourcing:** Trends 3,
  5, 7–11, 13, 14, 16, 17.

## 🆕 `p532` — the seventeen trends re-checked, and nothing moved

🔵 **A trend list that only ever grows is a slogan list.** This pass ran all four
global legs and all four regional legs and re-tested the carried trends against
what came back. **No trend was added, narrowed or contradicted** — and that is a
reportable result rather than an empty pass.

- 🟢 **Confirmed, with a sharper number.**
  [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) reads **49.5k★** today
  and holds at **`v1.7.0` (2026-10-28)**. Independent trending digests put it at
  **+1.6k to +2.4k stars/day** this window — the fastest sustained climb this
  base has recorded for any education asset, and the strongest single piece of
  evidence for the *persistent-memory tutoring* trend.
- 🟢 **Confirmed and now served by a permissive stack.** The **offline-first /
  sovereign-deployment** trend had exactly one component on this base (Kolibri,
  MIT, 1.2k★). `p532` adds
  [`Project-NOMAD`](https://github.com/Crosstalk-Solutions/Project-NOMAD)
  (**Apache-2.0, 41.3k★**) — the *server* side, model included. 🔵 The trend is
  no longer an argument with one repo behind it; see **`P600`** (`P565` until `p548`).
- 🟢 **Confirmed.** The **agent-skills-not-applications** shift `p526` first
  named holds: three of this pass's four new shelf rows are *skills* on the open
  Agent Skills spec or a Claude Code skill (`claudemy`,
  `learn-from-materials`), not standalone apps.
- 🔴 **Unchanged and still the regulatory headline:** stand-alone high-risk
  education obligations under the EU AI Act sit at **2027-12-02** per Regulation
  (EU) 2026/1744, while Art. 50 transparency duties applied from **2026-08-02**,
  and **Vietnam's Decision 33/2026/QD-TTg** remains the only APAC instrument that
  names education as a high-risk sector outright.
- 🔴 **A void, restated because it has now survived four passes:** there is still
  **no binding education-specific AI rule in Brazil or Mexico**. PL 2338 is
  pending in the Chamber (*aguardando parecer do relator*, mid-Oct 2026) with no
  education provision; for Mexico, search returns nothing. 🔵 Against LATAM's
  *highest-in-the-world* teacher adoption, that gap is the region's commercial
  opening and its governance risk at the same time — which is what **P554**
  exists to sell.

## 30. 🆕 The institutional source finally says what this base has been filing: **purpose-built beats general-purpose**, and the proof is anchoring to a named standard

**The claim.** Education AI is converging on tools built against a *named,
published standard* — a curriculum, a competency framework, an assessment rubric,
a records schema — and generic assistants are losing the serious buyer.

🟢 **Why it is a trend and not a preference, as of this pass.** The **OECD's 2026
Digital Education Outlook** reportedly recommends institutions move beyond
general-purpose AI tools toward **purpose-built educational AI**, and a separate
2026 trend survey independently describes the field moving *away* from generic
tools toward platforms with curriculum alignment and child-safety features. This
base has been filing the evidence for that for hundreds of passes without a
citation that was not its own prose.

🟢 **The shelf is the corroboration, and the pattern is exact.** Every row this
base has filed that survives contact with an institution is anchored to a
standard someone else published and maintains:

| Row | The standard it is anchored to | Who maintains the standard |
|---|---|---|
| `GuilhermeScarpini/agente-bncc-professores` | **BNCC** competency codes | MEC, Brazil |
| `dsvi-b/corretor-enem` | **ENEM** five official competencies, calibrated on 11 147 examiner-marked essays | INEP, Brazil |
| `oaknational/oak-open-curriculum-ecosystem` | **National Curriculum for England (2014)** | DfE / Oak National Academy |
| `KonstantinosPetrakis/esco-skill-extractor` | **ESCO / ISCO** | European Commission |
| `DavidLMS/learnmcp-xapi` | **xAPI** | ADL / 1EdTech ecosystem |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | **Ed-Fi** data standard | Ed-Fi Alliance |

🔵 **The mechanism, which is what makes this sellable.** A standard supplies the
one thing a generative system cannot generate: an **external referent**. A lesson
plan tagged `EF06MA13` is checkable by someone who has never seen the model. That
is simultaneously the pedagogy argument, the procurement argument and the
regulatory argument — Annex III conformity is far cheaper when the output maps to
a published code.

🔴 **How to disconfirm it.** If a general-purpose assistant with no standards
anchoring wins a national procurement in any region, or if the shelf's
standards-anchored rows stay at 0–30★ for another ten passes while generic
tutors grow, the trend is a preference of this base's filing criteria rather than
a property of the market. 🔴 **And the honest weakness today is exactly that:**
four of the six rows above are under 35★. The *institutions* behind the standards
are real; the *adoption* of these particular implementations is not yet evidence.

## 31. 🆕 **Education's permissive supply is institutional, and it is published by the state** — not by startups

**The claim.** The permissive (MIT/Apache/BSD) education supply that is actually
mature is increasingly coming from **government departments, national academies
and publicly funded research projects**, not from companies.

🟢 **The evidence this pass, all read first-hand.** England's **Department for
Education** ships `teaching-vacancies` (MIT, **19 739 commits**) and publishes
*"Guidance for AI coding agents"* inside it. **Oak National Academy** with the
**Education Endowment Foundation** ships an API, SDK **and MCP server** over
national curriculum data (MIT, **6 835 commits**). The **SKILLAB EU Horizon**
project ships ESCO extraction (MIT). The **Ed-Fi Alliance** ships the US K-12
records substrate (Apache-2.0, **48 forks against 28 stars**). **NYU Tandon**
ships `Anubis` (MIT, 382★). Brazil's row sources its standard from the **MEC**'s
own PDF.

🔵 **Why it follows from the sector's economics.** A permissive grant is a gift,
and the organisations that can afford to give away education infrastructure are
the ones not selling it — public bodies with a statutory mandate and research
projects with a grant to spend. Commercial education AI stays closed or
copyleft-with-a-commercial-licence, which is trend 6's finding from the other
direction.

🟢 **What it changes for an engagement.** The starting asset is likelier to be a
*public* repository with low stars, high commit counts and no community — which
is a very different diligence problem from a popular startup repo. **Forks
against stars is the better signal**: Ed-Fi's 48 forks against 28 stars means
people deploy it, not that they admire it.

🔴 **How to disconfirm it.** If the next ten permissive education rows filed here
are company-authored, or if the state-published rows prove unmaintained on a
liveness check, this is a sampling artefact of where this base has been looking.

## 32. 🆕 **Regulation has stopped being a posture and become a calendar** — and the dates do not line up across regions

**The claim.** Education AI compliance is now driven by specific dated
obligations in each region, not by principles, and a multi-region institution
faces a staggered schedule rather than one standard.

🟢 **The dates, as read this pass.** Ohio districts had to adopt AI-use policies
by **1 Jul 2026**; the ADA web-accessibility update for large US public
institutions landed in **Apr 2026**; South Korea's **AI Basic Act** came into
force **22 Jan 2026**; **Vietnam's** risk-based AI law took effect **1 Mar 2026**
with **education named in its high-risk list**; **Australia's TEQSA** has already
required every higher-education provider to submit a generative-AI risk action
plan; and the EU's **Annex III high-risk** obligations fall on **2 Dec 2027**
(standalone) and **Aug 2028** (embedded). **LATAM has no binding regional
education date at all**, against 716 regulatory instruments across 23 countries.

🔵 **Why the staggering is the commercial point.** Three of those dates have
already passed, which means the buyer is out of compliance *now* rather than
planning for later — and the EU's is far enough out to be a build window instead
of an emergency. 🟢 A studio selling into both reads the same system two ways:
**remediation** in APAC and North America, **design-for-conformity** in EMEA.

🔴 **The caveat that must travel with this trend.** The EU dating is attested only
by secondary sources that disagree with each other on how the delay was enacted
(a *Digital Omnibus* amendment effective July 2026, published as **Regulation (EU)
2026/1744** on 24 July 2026, versus a political agreement postponing to 2 Dec
2027). 🔴 **Read the Official Journal before citing either to a client.** The
Annex III *scope* is not in doubt; only the date's provenance is.

🔴 **How to disconfirm it.** If the EU date slips again, or if any major
jurisdiction replaces its dated obligation with a principles-based code, the
"calendar" framing weakens back into posture.

## 33. 🆕 **"Unknown licence" is not missing information — it is a 62 % probability of a restricted one**

**The claim.** In education open source, a repository whose grant file exists
but whose title names no standard licence is **far more likely to be restricted
than permissive**. The `UNKNOWN` bucket is not where the data is thin; it is
where the risk concentrates.

**The evidence, measured this pass.** 450 live backlog addresses were probed at
their resolved default branch (`p540`, extending `Gap 539-B`'s gate from 150 to
600). **37 — 8.2 % — served a grant whose title the matcher could not name.**
Every one was then read by hand, and 🟢 **none was unnameable**. 🔴 **23 of
37 (62 %) are not buildable permissively**, against ~0 % in the MIT / Apache /
BSD buckets, which are permissive by construction. Evidence:
[`../evidence/unknown-residue-graded.2026-10-30-p540.tsv`](../evidence/unknown-residue-graded.2026-10-30-p540.tsv).

**Twelve dialects, and they are not random.** `source-available` bespoke
licences (7), sector licences the matcher never heard of (`ECL-2.0` ×6,
`EPL-2.0`), jurisdiction licences (`EUPL` ×7), untitled permissive payloads (5),
R template stubs (3), **non-English copies of standard texts** (2), and one each
of titled-variant, split-grant, leading-whitespace, field-of-use and
data-licence.

🔵 **Why the restricted ones cluster here, mechanically.** A permissive licence
is adopted by copying a canonical text, which keeps its title line intact. A
restricted licence is **drafted**, and a drafted licence gets a bespoke
name — `Nakafa Source Available License 2.0`, `OpenGaokao Source-Available
License 1.0`, `O'Saasy License Agreement`, `Evaluation Dataset License`. 🔴
**The title line is unrecognisable precisely because somebody wrote it on
purpose**, and the purpose was usually to retain something. `PrairieLearn`
(527★ · 410 forks) is the fully-worked case: three grants in one file, and the
GitHub sidebar renders a bare "License" link naming nothing.

**What follows for a studio.** An unresolved `UNKNOWN` must gate **red**, not
amber. The cost of resolving one is a single file read; the cost of rounding it
to "probably fine" is discovering at integration time that the directory you
need is the vendor's enterprise tier.

🔴 **How to disconfirm it.** Gate a further 600 addresses and grade their
`UNKNOWN` residue. If the non-buildable share falls below roughly 30 %, the
62 % is a small-sample artefact of this slice and the rule weakens to "read
it", which is advice rather than a trend. n = 37 here, and that is stated.

## 34. 🆕 **Grant classifiers are English-keyed, so the open-source map systematically under-counts LATAM**

**The claim.** Tooling that identifies a licence by matching its English title
line will record non-English licence files as "no grant found", and downstream
that reads as "no supply". The effect is not uniform across regions — it falls
hardest on exactly the regions whose projects document in their own language.

**The evidence.** [`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital),
a Brazilian school pre-enrolment platform, serves the **standard AGPL-3.0 text
in Portuguese** — *"LICENÇA PÚBLICA GERAL AFFERO GNU, Versão 3, 19 de novembro
de 2007"*. This base's gate graded it `UNKNOWN`. It is ordinary AGPL-3.0 and
always was. A second instance in the same 450-address slice,
`yuanjiusheng/cloud-learning-ce`, reserves all rights **in Chinese** and was
equally invisible.

🔵 **Why this is a trend and not a bug report.** Every published count of "how
much permissive education software exists in LATAM" that this base or anyone
else has produced was produced by an English-keyed instrument. 🔴 **Those
counts are lower bounds, and nobody has been saying so.** This base has
declared LATAM supply gaps repeatedly across its history; this pass is the
first that can say part of that gap is **measurement, not absence** — and can
say it with an instance rather than a suspicion.

**What follows.** Add Portuguese and Spanish title strings for the
GPL / AGPL / MIT / Apache families before quoting any regional supply figure,
and re-run over the addresses already gated to see how many verdicts move
(→ `Gap 540-B`). Until that number exists, every "no grant found" on a LATAM
address is unsafe to repeat.

🔴 **How to disconfirm it.** Add the strings, re-run over the 600 gated
addresses, and if **zero** verdicts move beyond the one instance already known,
this is an anecdote and not a trend. The denominator is available and the fix
is cheap, so there is no excuse for carrying it unmeasured for more than a pass
or two.

## 35. 🆕 **Fork count divided by star count separates software you run from software you import — and the star count does not**

**The claim.** In this sector, forks-per-star is a usable proxy for *deployment
model*: software an institution runs its own copy of accumulates forks relative
to attention; software an institution imports as a dependency does not.

**The evidence.** Fourteen repositories, every star and fork count read
first-hand this pass, **classed first by what the software is** and only then
ordered by the ratio
([`../evidence/forks-per-star-rank.2026-10-30-p540.tsv`](../evidence/forks-per-star-rank.2026-10-30-p540.tsv)).
🟢 **The classes separated with an empty band:** every deploy-per-institution
point at **f/★ ≥ 0.250**, every import-as-dependency point at **≤ 0.182**, no
instance in the 0.068 between them.

| | f/★ | |
|---|---|---|
| [`dspace/dspace`](https://github.com/dspace/dspace) | **1.364** | 🟢 more forks than stars — institutional repository |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 0.250 | last point above the band |
| [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym) | 0.182 | first point below it |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 0.106 | 30.1k★ and firmly a dependency |

🔵 **Stars do not do this.** `smolagents` (30.1k★) and `jupyterhub` (8.4k★) are
both large, both widely used, and land on opposite sides — because popularity
and deployment model are different properties, and only one of them tells a
studio whether to budget for carrying a fork.

**What follows.** `f/★ ≥ 0.25` → fork it, budget migrations and local schema.
`f/★ ≤ 0.15` → pin it, budget version drift. Between, or under ~50 stars → the
ratio says nothing; read the repository.

🔴 **Two limits, stated rather than buried.** **n = 14**, one sector, one hour —
a boundary fitted to fourteen points is a hypothesis, and `Gap 540-C`
re-measures at n ≥ 60 before any recipe may depend on it. And 🔴 **the ratio
ranks without vetting**: the second-placed repository on this very ranking,
[`Apereo…/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS)
at 0.809, describes itself as *"Deprecated"*. Forks-per-star measures how
software **was** used. A liveness read stays mandatory.

🔴 **How to disconfirm it.** Class 60 repositories by deployment model without
looking at the ratio, then compute it. If the 0.18–0.25 band fills in, or if
any deploy-per-institution project lands below 0.15, the threshold is noise and
only the direction survives.

## 🆕 `p542` — Trend 36: **an English-keyed scan returns the English-publishing corpus, and the gap is invisible from inside it**

**Stated so it can be wrong:** if the language of a discovery query were merely
a *phrasing* choice, then running the same legs in any language would return
roughly the same artefacts, and non-English legs would yield new supply at a
rate close to zero.

🟢 **Measured, and it is wrong in a specific way.** `p542` ran this base's
mandated legs in English plus eight languages. English restated **9 of 9**.
The eight new legs produced **12 distinct artefacts, 7 of them absent from a
base holding 3 202 addresses**. But the yield is not spread evenly across
"non-English":

- **Distinct-corpus languages yield:** Indonesian **2 of 2**, Chinese
  **2 of 2**, and `p541`'s Spanish and Portuguese **8 of 10**.
- **Same-corpus languages do not:** German, Japanese and Korean yielded
  **0 absent artefacts of 3**, because their developer populations publish into
  the same GitHub corpus in English.

🔵 **So the trend is sharper than "search in other languages":** the axis is
**whether a language indexes a separate publishing corpus**, and only then is a
leg worth its cost.

> ### 🔴 `p543` — REWRITTEN. The "distinct corpus" formulation above is **falsified**, by the disconfirming case the trend itself asked for
>
> `p542` named the evidence that would break it: *"a single pass of one leg per
> language is a weak sample."* 🟢 **`p543` ran four untried legs — `ru`, `vi`,
> `tr`, and `it` as a designated control — with the prediction registered
> first** ([`../scratchpad/p543/predictions.txt`](../scratchpad/p543/predictions.txt)).
>
> 🔴 **Russian is the falsifier, and it falsifies the *positive* half rather
> than the negative one.** Russian indexes one of the largest separate
> publishing corpora on the internet — the leg returned Habr, DTF,
> `braintools.ru` and `thecode.media`, four Russian-language outlets answering
> in Russian — and it yielded **zero** education artefacts. 🔵 **Because what
> that corpus publishes is *localised rankings of the English corpus*** —
> Habr's *"100 лучших ИИ-репозиториев на GitHub в 2026 году"* ranks
> `rasbt/LLMs-from-scratch`, `500-AI-Agents-Projects`, `OpenHands` and `goose`,
> every one already on this base. **A distinct corpus that aggregates is a
> mirror, not a source.** Distinctness is necessary and **not sufficient**.
>
> 🟢 **The predictor that survives all twelve legs measured so far is narrower
> and more useful: whether the language's developers are coding against a
> NAMED NATIONAL INSTITUTION OR CURRICULUM.** Every artefact the yielding legs
> produced is anchored to one — **TÜBİTAK 2209-A** and **BTK course 514** (`tr`),
> the **GDPT 2018** curriculum and the **Vietnam AI in Education Pioneer Award**
> (`vi`), **BNCC** and **ENEM** (`p541`'s `pt`), a **provincial maths taxonomy**
> (`p542`'s `zh`). 🔴 **The five legs with no such anchor in their results —
> `de`, `ja`, `ko`, `it`, `ru` — returned nothing, which is now 0 absent
> artefacts of 4 legs plus `p542`'s 0 of 3.**
>
> 🔵 **Why the refinement is worth more than the original:** "find a distinct
> corpus" is not actionable, while **"find the country's curriculum, exam board
> or research funder, then search in its language"** is a procedure. It also
> explains the `it` control without appeal to corpus size: Italian education
> developers in these results are not building against a named national
> instrument.
>
> 🟡 **`Gap 542-E` is answered for the languages tested and stays open for
> `de`/`ja`/`ko`**: `p543` added `ru` and `it` as negatives rather than
> re-measuring p542's three, so those remain one-pass negatives.

⚠️ **The part that makes this a trend and not a tip:** the omission is
**invisible from inside the scan.** A missing result and an absent artefact
look identical, so a team scanning an Indonesian or Brazilian education market
in English gets a confident, complete-looking, systematically short answer —
and no signal that it is short.

## 🆕 `p544` — Trend 40: **a search leg measures the index it reaches, not the place the artefact came from — and treating the two as one has already produced a wrong published finding**

🔵 **Stated so it can be disconfirmed:** the language of a query predicts *which
index answers it*. It does not predict the **origin** of what comes back. Any
claim of the form *"language L's developers build X"* that was measured by
querying in L is unsupported.

🟢 **The disconfirming case that forced this trend, read first-hand.** `p543`
published, as its headline, that the Russian leg *"RETURNED **ZERO** … because
what that corpus publishes is localisations of the English corpus."* 🔴 `p544`'s
**Ukrainian** leg returned
[`fairyofmiracle/edu_course_agent`](https://github.com/fairyofmiracle/edu_course_agent)
— **a Russian artefact**: Russian README and UI, **Cloud.ru** and **GigaSchool**
gateways, Russian **ДПО** professional-development paperwork. 🔴 **Russian
domestic education supply exists and the Russian-language query did not reach
it.** The zero measured the query.

🔴 **Why this is a trend and not a one-off correction:** `p542` and `p543` built
*twelve legs* of conclusions on this conflation — "the yield tracks the corpus",
"a distinct corpus is necessary and not sufficient" — and both statements are
about artefact origin while both instruments only saw query language. 🔵 **Two
variables, one measurement, two passes of published inference.**

🟢 **What to do instead, concretely:** read origin off the artefact — README
language, the stack's hosting and gateways, the institution or statute it names —
and record *how* it was established. 🔵 This base's better rows already do exactly
that (`oak-open-curriculum-ecosystem` marked *stated* on the National Curriculum
for England; `agente-bncc-professores` on the BNCC and the MEC). 🔴 **What the
column does not yet distinguish is "inferred from the artefact" from "inferred
from the leg"**, which is `Gap 544-A`.

🔴 **How this trend could be wrong:** if a wider sample showed that leg language
and artefact origin coincide in, say, 95 % of cases, the conflation would be a
tolerable approximation rather than an error. 🔵 **That sample does not exist on
this base** — and the first counter-example appeared in the first four legs run
after the claim was published, which is weak evidence for a high coincidence rate.

## 🆕 `p544` — Trend 41: **domestic, non-English education supply is systematically ungranted — so "local open-source capability exists" and "you can build on it" are different claims**

🔵 **Stated so it can be disconfirmed:** education-specific agents built for a
domestic, non-English-speaking market are **real and live but carry no licence**,
at a rate high enough that a regional supply claim is unsafe without a grant
read.

🟢 **The measurement, re-probed first-hand at `p544` at each repo's *resolved*
default ref, 10 filenames each:**

| Address | Origin | Head @ `p544` | Grant |
|---|---|---|---|
| [`MaiQuangPhuoc/edu_agents`](https://github.com/MaiQuangPhuoc/edu_agents) | APAC (Vietnam) | `main` · `03e43219c66a` | 🔴 `UNRESOLVED` |
| [`dungptt-dng/smart-ict-classroom`](https://github.com/dungptt-dng/smart-ict-classroom) | APAC (Vietnam) | `main` · `a9c56b3b7496` | 🔴 `UNRESOLVED` |
| [`minhdevtry/AI-Teacher-Assistant-Agent`](https://github.com/minhdevtry/AI-Teacher-Assistant-Agent) | APAC (Vietnam) | `main` · `f3bcc636da1d` | 🔴 `UNRESOLVED` |
| [`fairyofmiracle/edu_course_agent`](https://github.com/fairyofmiracle/edu_course_agent) | EMEA (Russia) | `main` · `c425a51c2512` | 🔴 `UNRESOLVED` |

🔴 **Four artefacts, two unrelated origins, zero grants.** 🟢 `p543` observed this
in Vietnam and called it *regional*; `p544` found it again in an unrelated region,
which **promotes it from a regional peculiarity to a property of the supply
class**. 🔵 `Trend 39` is therefore **narrowed, not replaced**: its artefact-count
vs usable-count gap is real, and its attribution to *region* was too narrow.

🔵 **The consequence that changes what may be said to a client:** in these markets
the honest answer to *"what local open-source foundations can we build on?"* is
**"local capability exists and none of it is licensed for reuse."** 🔴 Counting
artefacts without reading grants overstates every regional supply claim. 🟢 The
cheapest corrective is to **ask** — one `LICENSE` commit moves a row from unusable
to shelf-eligible — and the class now has a register at
[`measured-unusable.md`](measured-unusable.md) so the next pass does not
rediscover it.

🔴 **How this trend could be wrong, and the honest weakness:** **n = 4**, and all
four were found by the same discovery method (non-English search legs). 🔵 A
licence-first search of the same markets — or a read of a domestic forge this
environment cannot reach, which `p542` showed is the case for `gitee.com` and
`gitlink.org.cn` — could turn up a granted domestic population this method is
blind to. 🟢 **The claim is about what this instrument can see, and is written
that way.**

## 🆕 `p543` — Trend 39: **a language leg's artefact count and its *usable* artefact count are different numbers, and the gap is regional**

**Stated so it can be wrong:** if open-source supply discovered in a national
language were usable at roughly the rate English-corpus supply is, then the
grant rate of artefacts found on a non-English leg would be close to the grant
rate of this base's shelf as a whole (which is dominated by MIT and Apache-2.0).

🔴 **Measured on this pass's four legs, and it is wrong by the widest margin
this base has recorded on any supply axis.**

| Leg | Education-specific artefacts found absent | Carrying a permissive grant |
|---|---|---|
| `vi` Vietnamese | **3** | 🔴 **0** |
| `tr` Turkish | **3** | 🟢 **3** (one of them a localisation of a held upstream) |
| `ru` Russian | 0 | — |
| `it` Italian | 0 | — |

🔵 **The Vietnamese three are not casual projects:** 75 commits and a 19 251 B
README on `edu_agents`, a NestJS/Mastra/Prisma/BullMQ backend on `ZaloAgent`, a
national award entry on `smart-ict-classroom`. **They carry no licence on any
of three channels** — 180 filenames at the resolved default branch, the
repository sidebar, and the README prose. 🟢 **Türkiye's three are MIT, and both
of the non-fork ones are anchored to a state institution** (BTK, TÜBİTAK),
which is likely the mechanism rather than a coincidence: **an artefact produced
inside an institutional frame inherits a licensing habit; a teacher's or
student's project does not.**

🔴 **Why this matters more than it looks.** A market scan that counts artefacts
concludes *Vietnam out-produced Türkiye this pass*. A scan that counts what can
be built on concludes *Vietnam produced nothing*. 🟢 **Both are true and they
imply opposite engagements** — adopt-and-extend in Türkiye, versus licensing,
governance and productisation of domestic prototypes in Vietnam. **The grant is
not a footnote on a supply finding; it is half of it.**

⚠️ **The disconfirming evidence to watch for:** this is one pass of two
yielding legs, n=6 artefacts. A Vietnamese leg next pass returning two
MIT-licensed domestic agents would collapse the asymmetry into noise, and a
Turkish leg returning three ungranted ones would too. 🔵 **The cheap test is
`p541`'s Spanish and Portuguese artefacts: grade the grant rate of those eight
retrospectively** — they are already on this base, and nobody has counted them
that way.

## 🆕 `p542` — Trend 37: **the permissive end of education software is pedagogy; the administrative end is copyleft, and that is stable**

**Stated so it can be wrong:** if licence choice in education software were
independent of what the software *does*, then MIT and Apache repos would be
spread evenly across tutoring, classroom, repository, SIS, ERP and CRM
functions.

🟢 **They are not, and `p542`'s vertical leg returned no counter-example.** The
mandated `open source platform education ERP CRM MIT Apache` leg returned eight
platforms — OpenEduCat, Moodle, Koha, Nextcloud, Jitsi, DSpace, LibreOffice,
Odoo — and **not one permissive education ERP or CRM.** The administrative end
is **copyleft or nothing**: OpenEduCat LGPLv3, ERPNext GPLv3, Odoo community
LGPLv3. Meanwhile the newly shelved pedagogy-side artefacts are MIT
(`instructional_agents`, `mini-kode`) and MIT + CC-BY-4.0 (`ocademy`).

🔵 **The mechanism is plausible and worth stating as the reason:** administrative
systems are sold as *hosted products* whose vendors use copyleft to protect a
commercial edition, while pedagogy tools are published by *academics and
individuals* optimising for citation and adoption. 🟢 **The engagement
consequence is concrete:** an administrative build either accepts copyleft on
the platform and keeps the AI layer across a process or network boundary, or it
integrates against a hosted product. 🔴 **It is not a gap to be closed by
searching harder** — this base has now run that leg to saturation for several
passes, and should state the constraint instead of re-running the query.

## 🆕 `p542` — Trend 38: **a licence verdict is only as good as the probe's shape, and three different defects all read out as "no grant"**

**Stated so it can be wrong:** if a `LICENSE`-at-`main` probe were an adequate
licence instrument, then "no grant found" would mean "no grant exists".

🔴 **On this pass it meant three different things, and only one of them was
true.** [`ocademy-ai/machine-learning`](https://github.com/ocademy-ai/machine-learning)
has **two** grants under `LICENSE-CODE` (MIT) and `LICENSE-TEXT` (CC-BY-4.0)
and returns 404 on twelve conventional probes;
[`minmaxflow/mini-kode`](https://github.com/minmaxflow/mini-kode) keeps a
canonical 1 066 B MIT file on **`master`**;
[`bigdata-ustc/Agent4Edu`](https://github.com/bigdata-ustc/Agent4Edu) genuinely
has nothing. 🟢 **Three identical outputs, three different causes — absent,
elsewhere, other-branch.**

🔵 **Why this is a sector trend and not only this base's bug:** the
split-grant shape (**code permissive, content CC-BY**) is the *correct* way to
license a teaching corpus, so an education KB meets it more often than any
other industry would. 🟢 **The trend, then: as education open source
professionalises, its licensing gets more structurally precise and
simultaneously harder for naive automated classifiers to read.** The
corollary is a standing one — **on a content-bearing education repo, treat "no
licence found" as "not yet probed"**, and read the bytes before writing the
verdict (`Gap 542-A`, `542-B`).

⚠️ **And a second-order case this pass measured:** GitHub's own sidebar names
**nothing** for [`1111philo/learn`](https://github.com/1111philo/learn) because
an 18-line program preamble — the form the FSF's own instructions recommend —
precedes the AGPL-3.0 text. **Following the licence's own guidance defeats the
platform's classifier**, so the artefacts most carefully licensed are among
those most likely to read as unlicensed.

## 🆕 `p545` — Trend 42: **an artefact's language places it only where that language is confined to one region — and for Spanish and Portuguese it is not**

**The claim.** Reading a region off an artefact's own language is sound **if and only if
that language is confined to a single region of a five-value vocabulary**
(`North America · EMEA · APAC · LATAM · Global`). `de`, `zh`, `id` and `vi` are confined.
🔴 **`es` and `pt` are not: both span EMEA and LATAM** — Spain and Portugal sit on one
side, nineteen American states and Brazil on the other.

**Why it matters commercially and not just methodologically.** A studio that places
supply by language will systematically **mis-assign Iberian work to LATAM and LATAM work
to EMEA**, in exactly the two languages where the region's supply is thickest. 🟢 The
same trap is waiting in **French** (France is EMEA, Canada is North America) and would
have fired silently on the next leg.

**How it could be wrong.** If a shelf row placed on `de`, `zh`, `id` or `vi` turns out to
originate outside the predicted region, the confinement rule is insufficient and
something else is doing the work. 🟢 **Tested at `p545` on five such rows; none
contradicted it.** The rule also says nothing about *Global* placements, which remain
judgements.

**What `p545` measured.** Seven shelf rows place a region on language. Five are confined
and survive. The two that are not — [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(`es`) and [`maiatechdev/avit`](https://github.com/maiatechdev/avit) (`pt`) — **both have
the right region and neither had the right evidence**: one cited three things that name no
country while the artefact names Colombia four ways; the other cited a phrase **not present
in the artefact at all.**

## 🆕 `p545` — Trend 43: **the agentic segment of education AI is now priced separately — and it is about a quarter of the market, with tutoring as the wedge**

**The claim.** Until this pass every figure on this base sized *AI in education entire*.
🟢 **Mordor Intelligence now prices the agentic segment on its own: USD `2.37 B` (2026) →
USD `11.83 B` (2031)**, against a whole-market 2026 band the research firms themselves put
between **USD `6.4 B` and `11.4 B`**. 🟢 **Grand View Research** prices *AI tutors* at
**USD `2.7 B` (2026)**, CAGR **30.5 %** to 2033. **So agentic is roughly a quarter of the
whole, and tutoring is most of the agentic quarter.**

**The go-to-market consequence, which is the useful part.** Mordor states it directly —
*tutoring remains the gateway purchase that seeds broader platform penetration*. 🔵 **For
an engagement that means the tutor is the door, not the product**: the administrative,
assessment and records work is where the other three quarters are, and it is reached
through a tutor deployment rather than sold beside one.

**How it could be wrong.** 🔴 **The two figures overlap and are not additive**, and
neither firm says where "agentic" stops and "tutor" starts — a definitional boundary, not
a measurement. 🔴 **Both are research-firm marketing pages, not audited data.** If a third
firm prices the agentic segment at half or double, the *ratio* claim fails and only the
sequencing claim survives. 🟢 Stated as a ratio precisely because the absolute numbers are
the weakest part.

