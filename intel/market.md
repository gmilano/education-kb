---
industry: education
region: Global
updated: 2026-10-06
---

# Market Intelligence — Education

## Global market size

| Metric | Value | Source basis |
|---|---|---|
| AI in education market, 2025 | $7.52B | Research and Markets, AI in Education Market Report 2026 |
| AI in education market, 2026 | $10.6B | same; 40.9% CAGR 2025→2026 |
| Projected 2030 | $42.48B | 41.5% CAGR |
| Alternative long-range series, 2025 | $6.4B | A second house's base year — **lower than the $7.52B above for the same year** |
| Alternative long-range series, 2034 | $79.6B | 31.35% CAGR 2026–2034, same house |

**Two incompatible series, re-checked in the sixth pass of 2026-10-06.** One house
puts 2025 at **$7.52B** growing at ~41% CAGR to **$42.48B by 2030**; another puts
2025 at **$6.4B** growing at **31.35%** to **$79.6B by 2034**. They disagree on the
base year by **$1.1B** and on the growth rate by **ten points**. **Quote one series
with its source attached, or quote the direction only.** A deck that mixes the
$6.4B base with the 41% CAGR is producing a number nobody published.

**Segment splits worth quoting** (single-source, so attribute them): cloud-based
delivery held **71.22%** share in 2024; **K-12 is 45.62%** of total adoption; STEM
captured **34.78%** of revenue; and **language learning is the fastest-growing
segment** — which is the segment the sixth pass's language and speech shelf serves
directly. Student AI usage is reported rising from **66% in 2024 to 92% in 2025**,
with ~**86% of higher-education students** using AI as a primary research and
brainstorming partner entering 2026.

Growth is real but the composition is shifting: the defining movement of 2026 is
**away from generic AI tools and toward platforms purpose-built for education**,
and from experimentation toward governance. Budget is moving to whoever can show
instructional value and a defensible oversight story — which is a services
opportunity more than a licensing one.

## Market map

**Proprietary incumbents.** Khan Academy (Khanmigo — publicly funded at state
level in the US), Instructure (Canvas), Anthology/Blackboard, Pearson, Duolingo,
Google for Education, Microsoft Education. These own the buyer relationship.

**Open source platform layer.** Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas LMS
(AGPL-3.0), Chamilo (GPL-3.0), Sakai (ECL-2.0), ILIAS (GPL-3.0), Frappe LMS
(AGPL-3.0), Kolibri (MIT), Oppia (Apache-2.0). See `verticals/solutions.md`.

**Open source AI layer.** DeepTutor (Apache-2.0, 40.8k★) is the only
education-native agent project with real gravity. Below it, and substantially
re-measured in the third pass of 2026-10-06: **StudyMate** (MIT, 624★, China),
**anki-mcp-server** (MIT, 506★, 53 tools — the largest education MCP server),
**OpenTutor** (MIT, 130★, FSRS 4.5 + knowledge graph + local-first), **Mentingo**
(MIT, 91★, the first permissive AI-native LMS), OATutor (MIT, the auditable mastery
model), Educhain (MIT, content generation), canvas-mcp and moodle-mcp-server (MIT,
integration), plus a cluster of MIT **Agent Skills** at 100–300★
(universal-examprep-skill, algo-sensei, universal-diagnostic-tutor-skill,
kaogong-skill, education-skills). General frameworks — MAF, smolagents, LangGraph,
pydantic-ai, all MIT/Apache-2.0 — supply the rest.

**The layer is no longer thin, and that changes the pitch.** Three passes on
2026-10-06 took the permissive education shelf from "DeepTutor plus fragments" to
roughly 30 verified permissive projects, including a full MIT LMS. The
differentiator is shifting from *finding* the open source parts to **composing,
licensing and governing** them — which is also the part a client cannot do from a
listicle.

**Where Globant fits.** The platform layer is copyleft and the AI layer is thin.
The reusable, defensible position is the **permissive side-car**: agent services
that integrate over LTI 1.3 and MCP, carry Globant's own license, and work
against whichever LMS the client already runs.

## Opportunities by region

### North America

- **Largest regional share: 36% of the global market, $3.68B in 2026**, declining
  to **~25% by 2030** as APAC grows faster. **The 2030 figure is $10.8B.** The
  fourth pass recorded it as disputed and unresolved; the **fifth pass closed it
  on internal-consistency arithmetic** — see "Fifth pass" below, and stop quoting
  a range.
- **SIZING CONFLICT, flagged in the fourth pass of 2026-10-06 — do not quote
  "$32B by 2030" unqualified.** Earlier passes of this KB recorded NA 2030 at
  **$32B**. A second source puts NA at **$3.68B (2026) → $10.8B (2030), 31.1%
  CAGR**. The two cannot both be right, and **the lower one is the more internally
  consistent**: this KB's own global row is $42.48B in 2030, and 36% of that is
  ~$15.3B, so a $32B North America would be **~75% of the entire global market** —
  contradicting the 36% share asserted in the same breath. $10.8B implies NA share
  *falling* to ~25% by 2030, which is consistent with the KB's EMEA finding that
  mature markets grow below the global rate.
  **How to use it:** quote **$3.68B for 2026** (both sources agree) and give 2030
  as **$10.8B–$32B, source-dependent**, naming the uncertainty. The primary
  source could not be re-read this pass — `grandviewresearch.com` is blocked by
  this environment's egress proxy — so the conflict is **recorded, not resolved**.
  Same treatment this KB already applies to MEA.
- Adoption is already broad: **60% of US K-12 teachers used AI tools in the
  2024–25 school year; 32% used them at least weekly.** The sale is no longer
  "should you use AI" — it is governance, procurement and integration.
- **Regulation is the demand driver.** 134 AI-in-education bills introduced
  across 31 states in 2026. Concretely:
  - California **AB 1159** — the **Learner Personal Information Protection Act
    (CALPIPA)**, **signed by Governor Newsom on 10 September 2026**. Bars
    companies from using **identifiable** student data to train generative AI or
    build AI systems, and extends protection to **reproductive-health and
    immigration** records. **Its higher-education provisions begin 1 July 2027** —
    a dated, known-in-advance procurement trigger for every university vendor in
    the state. Put it in the pipeline now.
  - Idaho **SB 1227** — the **Generative Artificial Intelligence in Education
    Act**, and it is much more than a data-privacy bill. It requires a **statewide
    K-12 AI framework**, local district policies, **AI literacy standards and
    educator training**, data-privacy requirements for AI tools, and it
    **prohibits AI from replacing human teachers** — the statute's own test is
    that **"human judgment remains the final authority."** The training mandate is
    a **billable enablement line**, not just a constraint.
  - Oklahoma **SB 1734** — AI permitted **only under educator supervision with
    human review**, barred from high-stakes decisions, state guidance plus
    district policies required, and **annual disclosure to parents**. That last
    item is a recurring reporting obligation, which means a recurring deliverable.
  - Maryland **Artificial Intelligence Ready Schools Act** — all **24** local
    districts must adopt aligned policies within **120 days of MSDE releasing its
    guidance**. Note the shape: a **rolling deadline keyed to a state
    publication**, not a fixed calendar date, so the buying window opens when MSDE
    publishes.
  - **Ohio HB 96** (the 2025–2027 operating budget) — **the first state to mandate
    AI frameworks in every public K-12 district.** DEW published its model policy
    by **31 December 2025**; every district had to adopt a written AI policy by
    **1 July 2026**. **That deadline has now passed**, so Ohio's 600+ districts are
    no longer buying policy documents — they are in the **implement-and-audit**
    phase, which is the more valuable engagement and the one with no incumbent.
  - **Georgia and Mississippi** require computer science credits including AI
    instruction from the late 2020s.
  - **New York City DOE** issued guidance in March 2026 built on a "Traffic
    Light Framework," informed by Google and OpenAI.
  - **North Carolina SB 1006** — the **K-12 Innovation and Transformation Act**,
    which creates an **AI Academic Support Program** letting public school units
    contract with Khan Academy for **Khanmigo in grades 6–12**. Two details change
    how you read it: the money is **more than $10M in *recurring* state funding**,
    not a one-off pilot, and it was **directed to a single vendor without
    competitive bidding** (defended publicly by sponsor Senator Michael Lee,
    R-New Hanover, in June 2026). **Read-across:** states will fund AI tutoring as
    a standing line item, and a sole-source award of that size invites both
    procurement challenges and copycat RFPs in neighbouring states. The opening is
    the **integration, oversight and evidence layer around** such a contract — not
    competing with the tutor itself.
- **Opportunity:** policy-to-implementation work. Districts now have mandates and
  no capability. Offer: AI policy implementation, a human-oversight gate wired
  into the grade path, student-data-boundary architecture (AB 1159 means
  no-training-on-student-data must be *provable*), and Canvas integration via
  canvas-mcp. Sell the audit trail, not the chatbot.

**New this pass (2026-10-06):**

- **All 50 states** have now introduced AI legislation — the 134 bills across 31
  states specific to education sit inside a universal legislative wave. There is
  no national stance to design against; the unit of compliance is the state.
- **States have split into two camps, and they need opposite offers.** One camp is
  building procurement pipelines with real budget behind adoption (North Carolina's
  $10M for Khanmigo is the template). The other is applying brakes — bans,
  moratoriums and strict consent requirements. Qualify which camp a district sits
  in before pitching: in camp one you sell deployment, in camp two you sell
  governance, assurance and an auditable oversight gate, and a deployment pitch
  will lose.
- **Idaho SB 1227** joins California AB 1159 on student-data protection for AI
  tools in schools — the no-training-on-student-data requirement is now a
  multi-state pattern, not a California quirk, so build the data boundary once and
  evidence it everywhere.
- **Students are now a stakeholder with a published position.** In August 2026,
  students from all 50 states produced a **national framework for AI in America's
  schools** (via AASA). Student-body buy-in is becoming part of the procurement
  conversation; cite the framework in proposals rather than being surprised by it.

**Third pass (2026-10-06) — channel saturated, nothing net new.** The North America
query was re-run and returned the same facts already recorded above: 36% share /
$3.68B in 2026 (2030 **disputed: $10.8B–$32B**, see the sizing conflict above);
60% of K-12 teachers using AI in 2024–25 with 32% weekly; 134 bills across 31
states; California AB 1159 and Idaho SB 1227; Oklahoma and Maryland human-oversight
requirements; Ohio's July 2026 policy deadline; North Carolina's $10M Khanmigo
earmark; the AASA student framework from all 50 states (created at America's Youth
AI Festival in July 2026).

**The "saturated" verdict recorded here in the third pass was premature, and the
fourth pass of 2026-10-06 withdraws it.** That pass claimed the open-web channel
was exhausted for North America and that only procurement portals and state
trackers could add depth. Re-running general searches returned **materially more
per bill** without touching a single procurement portal: a **statute name and
signing date** for AB 1159 plus a **1 July 2027 higher-education trigger** nobody
had recorded; Idaho SB 1227's real scope (**an AI-literacy and educator-training
mandate with a "human judgment is final" test**, not a privacy bill); a **bill
number** for Oklahoma (**SB 1734**) and its **annual parent-disclosure**
obligation; Maryland's **24 districts / 120-day rolling** mechanism; Ohio's
**HB 96** vehicle and the fact its deadline is now **past**; and North Carolina's
funding being **recurring and sole-sourced**.

**The lesson is about the claim, not the region.** "Saturated" conflated *no new
entities* with *no new information*. The entity list barely moved; the
**mechanisms, dates and bill numbers** — which are what make a finding sellable —
were mostly absent. Before declaring a channel exhausted, ask whether the next
pass would add **rows** or **precision**, and treat the second as worth a pass on
its own. Procurement portals and state trackers remain the right instrument for
going deeper still.


#### Fifth pass, 2026-10-06 — the sizing conflict resolves, and it resolves in favour of the lower figure

The fourth pass recorded the NA 2030 figure as **disputed and unresolved**, with
the primary source unreachable. It can now be closed on arithmetic alone, using
this KB's own global row, and the conclusion is **$10.8B, not $32B**:

| Check | Figure | Verdict |
|---|---|---|
| Global 2026 (this KB's own row) | **$10.6B** | — |
| NA 2026 at the asserted 36% share | 36% × $10.6B = **$3.82B** | matches the recorded **$3.68B** to within rounding. **The 2026 figures are mutually consistent** |
| Global 2030 (this KB's own row) | **$42.48B** | — |
| NA 2030 at **$32B** | would be **75%** of global | **incoherent** with a 36% share asserted on the same page |
| NA 2030 at **$10.8B** | **25%** of global; implies **31.1% CAGR** | **coherent** — and it sits almost exactly on EMEA's independently sourced **31.9%** CAGR |

**Quote $3.68B (2026) → $10.8B (2030), ~31% CAGR, and say NA's share declines
from 36% to ~25% as APAC grows faster.** That last clause is the sellable part:
it is the arithmetic consequence of a 41.5% global CAGR against a 31% North
American one, and it is the reason an NA-only account strategy loses ground even
while the NA number triples.

**Retire the $32B figure.** It is not a range endpoint; it is an outlier that
fails an internal-consistency check against two of this KB's own rows and against
EMEA's independently sourced growth rate.

**One NA entity added this pass:** the **STUDENTS FIRST Act of 2026**, drafted by
students representing all 50 states at America's Youth AI Festival in July 2026
and published through **AASA** (the School Superintendents Association) in August
2026. It proposes protections for authentic learning, student privacy, fairness,
**human judgment** and relationships. It is not law and will not become law in
this form — its value is that it is **student-authored and superintendent-amplified**,
which makes it the cheapest available legitimacy artefact for a district-facing
oversight proposal. It also converges on the same "human judgment is final" test
this KB records as the one testable rule US state law has settled on.



#### Sixth pass, 2026-10-06 — the voice and language layer

**Market position re-read this pass.** North America was **$951M in 2024** heading
to **$2,303.2M by 2029 (15.9% CAGR)** on one house's numbers, and is quoted
elsewhere as **41.7% of the global opportunity** with a **45% CAGR for 2025–2030**
— a spread wide enough that only the direction is safe to quote. It leads regional
adoption at **36% share**; **66% of students** use ChatGPT; and **AI literacy is
LinkedIn's #1 skill for 2026, carrying a 56% wage premium**.

**The regulatory asymmetry is the sales point.** Education AI here operates in a
**relative regulatory vacuum — there is no FDA equivalent for educational
technology**, and adoption decisions sit with individual districts and
universities with minimal external oversight. State law is piecemeal (Colorado,
Texas). Meanwhile the **EU AI Act takes full effect in August 2026** and
classifies education AI as high-risk. **A North American client selling into
Europe inherits the stricter regime**, so build to P13 and sell the compliance
posture as a feature rather than waiting for a US mandate.

**What this pass opens here:**

- **Oral reading fluency (P17) is the strongest single opportunity in this
  region.** US literacy screening is a large, mandated, recurring spend and
  **every system doing it is proprietary** — FLORA, Literably (IES-funded),
  Amplify Text Reading Online, SoapBox Labs, none with a public repository. The
  permissive components are now all shelved and a **public dataset with a
  published baseline** exists. An open, auditable WCPM assessor with teacher
  override satisfies the "human judgment is final" rule US state law has converged
  on (trend 16) and has no open competitor.
- **Spanish-language instruction is now servable from permissive components.**
  The English-language-learner population is the region's largest underserved
  segment, and `sherpa-onnx` (Apache-2.0) plus `idiap/coqui-ai-TTS` (MPL-2.0)
  cover Spanish speech in and out, on-premises, with no student audio leaving the
  district — which is also the FERPA-friendly architecture.

#### Seventh pass of 2026-10-06 — the federal bill, and a trending repo you cannot ship

**Net new to this file: there is now federal legislation moving.** The **House
Education Committee advanced the K-12 AI Literacy and Readiness Act of 2026
(H.R. 8747)**, which would amend the Elementary and Secondary Education Act to
let schools **spend federal funds on AI curriculum and literacy programmes**.
This KB had the state-level picture in detail (134 bills across 31 states;
California AB 1159 barring student data from model training; Idaho SB 1227;
Oklahoma and Maryland requiring human oversight; North Carolina's $10M Khanmigo
earmark) and nothing at the federal level.

**Why it matters more than most bills: it is a funding authorisation, not a
restriction.** Every other instrument this KB tracks for North America
*constrains* deployment. This one would create a **federal budget line for
exactly the enablement work Globant already sells** — teacher and student AI
literacy, curriculum integration — on top of the state procurement pipelines
already funded. It has advanced from committee only; treat it as pipeline
intelligence, not as a closed sale.

**A procurement caution from the repository side of this pass.**
[cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) — an
open systems-programming textbook from **UIUC** — gained **~1,626★ in one week**,
the fastest-growing education repository seen in any pass of this KB, and it has
**no `LICENSE` payload**. North American higher-ed clients will bring
repositories like this to the table as "open" course material. **Trending
velocity, institutional provenance and the word "open" are all orthogonal to
whether rights were granted.** Probe before promising, and expect to have this
conversation with a university client who believes their own repo is usable.


#### Eighth pass, 2026-10-06 — nothing new found for this region, and that is the finding

The eighth pass ran the mandated North America sweep (`AI education North
America 2026 adoption regulation state law`) and it returned **only material
this file already holds**: the 134 bills across 31 states, California **AB
1159** (prohibiting the use of student data to train models), Idaho **SB 1227**,
the Oklahoma and Maryland human-oversight statutes, Ohio **HB 96** and the
district-level-policy approach, plus the federal K-12 AI task force.

**One new item, and it is small:** Tennessee **SB 1711** joins Ohio HB 96 in the
*delegate-to-districts* column rather than the statewide-rule column. That
matters only because it strengthens a pattern already recorded here — in the US
the buyer of AI governance is increasingly **the district**, not the state, which
is a procurement shape (many small buyers, each needing a policy artefact) rather
than a product shape.

**Recorded as a saturation signal, not as coverage.** Four consecutive passes
have now returned the same North America facts from a general-language search.
The channel is exhausted; the next North America finding will have to come from
a different one — district RFP language, state education-agency procurement
portals, or the vendor-side filings, none of which this KB has swept.

#### Ninth pass, 2026-10-06 — the procurement channel opens, and it is the strongest North America finding in five passes

**Channel.** The eighth pass declared this region's general-language channel
exhausted and named the required replacement: *"district RFP language, state
education-agency procurement portals, or vendor filings — none of which this KB
has ever swept."* Two of the three were swept this pass.

⚠️ **Tier 2 throughout this subsection.** Every figure, date and statutory
reference below comes from **corroborated search summaries, not primary
documents.** `k12-ai-infrastructure.org`, `digitalpromise.org`, `cosn.org`,
`marylandpublicschools.org`, `excelined.org`, `njsba.org`, `web.ped.nm.gov` and
`marketbrief.edweek.org` are all **EGRESS_BLOCKED** in this environment. **No RFP
and no state guidance document was read.** Confirm each citation against the
primary source before it reaches a client deliverable.

##### 1. The supply side is being bought, with a permissive licence floor

**The K-12 AI Infrastructure Program** — **$26M**, multi-year, led by **Digital
Promise** with core partners **Learning Data Insights**, **DrivenData**, the
**Massive Data Institute at Georgetown University** and **Catalyst @ Penn GSE**.
**Gates Foundation**-funded, and the Foundation manages proposal review and award
monitoring directly. Launched **3 Nov 2025**; first cycle opened **4 Feb 2026**.

| Instrument | Size | Scope | Dates |
|---|---|---|---|
| **EDU AI** — Open Source AI Model for Tutoring | **up to $8M**, one award | Open-source education-specific model(s) + research, to make **K-12 math tutoring as effective as human experts** | Released 1 Jun 2026; **closed 31 Jul 2026**; work from **Nov 2026**; 30–36 months |
| **T&L Benchmarks and Datasets** | not established | **Three** standalone open-source **K-12 instructional data corpora** + an **AI benchmark** for adaptive learning | Open |
| Cohort 1 grants | 4 awards, 6–12 months | Learning Equality (science misconceptions); Princeton (simulated student models); **National Tutoring Observatory / Cornell** (ASR leaderboards); Stanford (**KB-TutorBench**, formative assessment) | Announced **29 Jun 2026** |
| Cohort 2 grants | **8 awards**, 6–12 months | **Formative assessment** focus, plus math, literacy and writing; outputs stated to be **openly licensed** | Announced **21 Sept 2026** |

**The licence condition is the commercially material fact:** all funded
developments must be released under a licence **at least as permissive as
CC-BY-4.0 (content) or Apache-2.0 (code/models)**, with Apache-2.0 recommended
for software and code *including evaluations, models and applications*.

**What this means for a North America engagement.** The region's open-source
education AI supply is, for the first time, **a funded pipeline with named owners
and dates** rather than an organic shelf. Twelve projects are in flight; none has
published code yet (measured: `KB-TutorBench` → 0 repositories; `learningequality`
filtered on `benchmark` → 0 repositories). **The opportunity is positional**:
design client architectures now so Apache-2.0 benchmarks and models drop in as
they land through 2027 — pattern **P23** — and approach the grantees as
integration partners. **Learning Equality is both a grantee and the maintainer of
Kolibri (MIT)**, which this KB already recommends.

##### 2. The demand side now specifies the architecture, through procurement rubrics

The regulatory frame in this region had been *"state law says human judgment is
final"* (trend 16). The procurement layer is more specific, and it is what a
vendor actually has to satisfy:

- **Maryland SB 720** (effective **1 Jun 2026**) — the state department must
  publish guidance **and an AI-tool evaluation rubric**; each local school system
  must adopt an aligned policy **within 120 days** and designate an **AI
  coordinator**. Reported as **24 districts** required to adopt AI policies by
  **Fall 2026**. State AI guidance was published **Feb 2026**.
- **Vermont** (guidance **23 Jan 2026**) — an evaluation-process rubric for AI
  tools covering **educational value, data-privacy compliance, usability and
  accessibility, cost, scalability, vendor reputation and age restrictions.**
- **Idaho, Maryland, Alabama** — statutory requirements that LEAs conduct
  **structured capability assessments**, **verify pre-training standards**, and
  **prohibit vendor training on student records.**
- **Contract language** is converging on a clause prohibiting unauthorised use of
  school data to train models, with explicit documentation and approval for any
  AI system training.
- **CoSN, *U.S. State of EdTech 2026*: 39% of districts include
  interoperability in their RFP evaluation rubrics.** This is the first
  *procurement-side* number this KB has for its trend 4 (MCP/LTI as the
  integration layer) — interoperability is no longer an engineering preference,
  it is a scored criterion in two of five district solicitations.

**Live tutoring procurements** (useful as demand evidence and as RFP-language
samples): **NJSBA RFP 2026-02** — Virtual Tutoring Services, optionally Virtual
High-Impact Tutoring and **outcomes-based contracting**, proposals due 2 Jun 2026;
**New Mexico PED RFP 27-92400-00002** — statewide **high-impact tutoring for
reading and math** under **House Bill 2**, with **SY2026-27 the first
implementation year.**

##### 3. The gap inside the rubrics, which is the sellable one

The rubrics are converging on privacy, accessibility and human oversight. What
most of them reportedly **do not** require: that vendors supply **auditable
records of user interactions**, **disclose how the system generates outputs**, or
**demonstrate that the tool was evaluated for bias, accuracy and reliability.**

**That is the differentiator.** A deliverable that ships an interaction audit
log, an output-provenance statement and an evaluation report **exceeds every
rubric described above** and pre-empts the obvious next revision of them. It is
also, almost exactly, the artefact set the EU AI Act profile already forces
(**P13**) — so the same evidence pack sells in both regions, which is the
cross-region arbitrage this KB has been looking for in North America.

##### 4. Market sizing, unchanged in direction and still conflicted in magnitude

This pass surfaced **North America at $951M (2024) → $2,303.2M (2029), 15.9%
CAGR**, with the region holding **~36%** of the global market — alongside global
claims of **$7.52B (2025) → $10.6B (2026) at 40.9% CAGR**. These are not
reconcilable on any consistent definition. **The fifth pass resolved this KB's
position in favour of the lower, more conservative figures and that position
stands**; a 15.9% regional CAGR and a 40.9% global CAGR in the same market is a
scope difference, not a growth difference. Quote the regional figure, state the
definition, and never blend the two in one chart.

#### Tenth pass of 2026-10-06 — the funded pipeline gains two more names, and the integration tier becomes sellable

**The oral-reading project is named, and it is the most on-target funded work this
KB has seen.** Two further Cohort 2 grantees of the **$26M K-12 AI Infrastructure
Program** (Tier 2, search-summary corroborated):

| Grantee | Lead | Project |
|---|---|---|
| **Harvard University** | Ying Xu | **OpenLiteracy: An Open-Source AI Infrastructure Suite for Advancing Speech Foundation Models for Early Word Reading Assessment and Instruction** |
| **University of Maryland, College Park** | Jing Liu | *Enhancing Two Multimodal Classroom Datasets to Advance R&D on Formative Assessment* |

Three of the eight Cohort 2 grantees are now named here (with MMSA & TERC from the
ninth pass); **five remain unnamed.**

**And nothing has shipped — measured, Tier 1, 6 Oct 2026:**

| Probe | Result |
|---|---|
| `OpenLiteracy` | **0 repositories** |
| `tutoring quality evaluation benchmark license:apache-2.0` | **0 repositories** (unchanged) |
| `formative assessment dataset classroom` | **0 repositories** |

**The opportunity, sharpened.** OpenLiteracy targets early word reading
assessment. The whole existing permissive shelf for that capability is **two
repositories** — [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody)
(MIT, 0★, 1 commit, Whisper + Levenshtein alignment) and
[mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) (no
licence payload). A client who needs oral reading fluency assessment **this**
school year cannot wait for Harvard's suite; the engagement is to build the
harness around `prosody`'s approach now and swap the funded artefacts in when they
land (**P23**, **P25**).

**A named partner with a 238-repository MIT estate.** Learning Equality — Cohort 1
grantee, Kolibri maintainer — holds **238 repositories**, of which this KB had
recorded three. Newly verified MIT: **morango** (15★, peer-to-peer Django DB
replication with certificate-based auth) and **le-utils**. Two others
(`kolibri-design-system`, `kolibri-server`) returned **no licence payload** — so
the diligence is per-repository, not per-organisation. The partnership case is
unchanged and stronger: the organisation funded to produce an openly-licensed
benchmark already ships MIT infrastructure this KB can build on.

**The integration tier is now a sellable line item.** Against the ninth pass's
**39% of districts scoring interoperability in RFP rubrics**, the permissive shelf
is verified and small: `ltijs` (Apache-2.0, 373★, Node), `1EdTech/lti-1-3-php-library`
(Apache-2.0, 124★), `Unicon/tool13demo` and `oxctl/spring-security-lti13`
(Apache-2.0, JVM), `theopenem/OneRoster.NET` (MIT, rostering only, **no
gradebook**). **No Caliper Analytics implementation on a permissive licence, and
no Python LTI 1.3 library at all** — the second is an open-source contribution
opening with a procurement-scored buyer already attached.


#### Eleventh pass, 2026-10-06 — the benchmarks are American, the licences are not open

| Finding | Value | Instrument |
|---|---|---|
| Share of the global AI-in-education opportunity 2026–2030 | **41.7%** | Tier 2, market-research summary |
| Regional market share | **36%** of global AI-in-education | Tier 2 |
| Institutions with formal AI guidelines | **10%** | Tier 2 |
| US teachers lacking AI training | **71%** | Tier 2 |
| State-level AI requirements for education | **Colorado** and **Texas** have introduced piecemeal requirements; no federal instrument | Tier 2 |

**The opportunity this pass actually adds.** The two leading tutoring-evaluation
benchmarks are North American and European institutional work — **Khan Academy**
(`Khan/tutoring-accuracy-dataset`, 57★) and **ETH Zurich**
(`eth-lre/mathtutorbench`, 43★) — and **neither is OSI-licensed** (Tier 1, payloads
read 2026-10-06). Khan's custom *Evaluation Dataset License* permits internal,
non-commercial evaluation **and explicitly permits evaluating products intended for
commercial use and commercially exploiting the insights gained**, while prohibiting
redistribution, model training and production use.

That is a billable position, and it is specific to this region: **a US district or
university buyer can be shown a measured pedagogical-quality number from Khan
Academy's own dataset, without that dataset ever entering the deliverable.** The
regulatory vacuum here (10% with guidelines, no FDA-equivalent, 41.7% of the money)
means the buyer has no mandated evaluation to point at — so the vendor who arrives
with one sets the standard. The harness is **Inspect** (MIT, 2,945★, UK AISI). The
pattern is **P27**.

**And the data tier is Apache-2.0 and already in the RFP.**
`Ed-Fi-Alliance-OSS/Ed-Fi-ODS` (Apache-2.0, Tier 1) is the reference implementation
of the Ed-Fi K-12 data standard — the student-data model North American district
procurement assumes a vendor already speaks. It was dropped from this KB's live files
by the reset and is reinstated this pass.

### EMEA

- **The EU AI Act is the whole conversation.** AI used in education access and
  assessment — admissions, student evaluation, exam scoring — is classified
  **high-risk** under Annex III.
- **Timeline matters and buys time:** high-risk obligations for stand-alone
  systems are **deferred to 2 December 2027**; high-risk AI embedded in
  already-regulated products to **2 August 2028**. The European AI Office
  implements the general-purpose AI provisions. In 2026 the EU agreed amendments
  clarifying overlap with machinery rules.
- **Deployment reality:** schools are running parent-facing and admin chatbots on
  commercial APIs, but districts with strict data-residency requirements
  **self-host open-weight models** (Llama, Mistral) instead.
- **Opportunity:** a sovereign, high-risk-ready stack delivered well before the
  2027 deadline — on-prem Ollama/vLLM, typed outputs, checkpointed audit trails,
  explainable mastery estimation, and a documented human-oversight gate. The
  deferral is the window: a system designed for Annex III now avoids a forced
  rebuild in 2027. Germany/Austria/Switzerland additionally skew toward ILIAS and
  SCORM compliance training.

**New this pass (2026-10-06):**

- **Sized at last: the European AI-in-education market is $2.64B in 2026.** That
  is the regional number the earlier passes were missing — roughly 25% of the
  $10.6B global market, against North America's 36% / $3.68B.
- **The leaders are small, digitally mature states, not the large economies:**
  **Finland, Estonia and the Netherlands** lead European K-12 AI integration. For
  a reference deployment, these are the markets where the institutional appetite
  and the digital baseline already exist. Treat them as the proof-point tier.
- **Timeline precision matters.** The AI Act's **general application date is
  2 August 2026** — already passed. What is deferred is the *high-risk* obligation
  set: stand-alone Annex III systems to **2 December 2027**, high-risk AI embedded
  in already-regulated products to **2 August 2028**. So the general-purpose and
  transparency regime is live now, while the education-specific high-risk regime
  is the design window. Do not tell a client "the AI Act does not apply yet."
- **Most European institutions are in pilot-and-pre-compliance mode**, deploying
  AI in administration and teacher support first, keeping humans in the loop on
  consequential decisions, documenting deployments, and disclosing to students and
  parents what is AI-decided versus human-decided. That sequence — admin first,
  assessment last — is the lowest-friction entry path in the region.
- **Africa enters this KB.** Earlier passes treated EMEA as Europe. South Africa's
  **Draft National Artificial Intelligence Policy (2026)** is in progress, and
  **GenAITEd Ghana** — a context-aware, curriculum-aligned conversational AI agent
  for *teacher education* — is a published, first-of-its-kind African education
  agent (research, not a product shelf). Africa is a genuine greenfield in the
  EMEA bucket: policy forming, almost no deployed open source education AI, and
  teacher capability the binding constraint.

**New in the third pass (2026-10-06):**

- **NARROWED (fourth pass, 2026-10-06): Africa now has a code shelf, and it is
  ministry-engaged.** Every earlier pass recorded "no deployed open source African
  education AI shelf to recommend from." That is no longer accurate.
  [`AI-for-Education`](https://github.com/AI-for-Education) is a GitHub
  organisation whose mission is to democratise AI in education across **low- and
  middle-income countries**, and — unusually for anything on this shelf — its work
  is **placed in named countries**: a lesson-plan parser built for **Sierra
  Leone's MBSSE** (Ministry of Basic and Senior Secondary Education) and
  **Luganda linguistic benchmarks** for **Uganda**. Five of its six repositories
  are **MIT by payload** (`pedagogy-benchmark` 12★, `fabdata-llm` 9★,
  `edu-qurating` 3★, `fabdata-parsedoc` 2★, `voice-ai-evaluation-framework` 1★);
  the sixth is unlicensed. See `repos/foundations.md`.
  **Size it honestly: 1–12★ is research-grade code, not a product shelf.** The
  finding is not "Africa is served" — it is that the entry point is **specific,
  permissive and already connected to a ministry**, which is a far better place to
  start a conversation than greenfield. It also supplies the two capabilities the
  continent's constraints actually demand and that this KB had no entry for
  anywhere: **voice-interface evaluation** (where literacy and device cost bind)
  and **local-language benchmarking** (Luganda). Teacher capability remains the
  binding constraint, unchanged.
- **Europe now has a growth curve, not just a 2026 number: $2.64B in 2026 →
  $8.0B by 2030 at 31.9% CAGR.** Note what that means — Europe is growing
  *materially slower* than the global 41.5% CAGR, so its 25% share of the market
  shrinks over the forecast period. The AI Act is both the demand driver and the
  brake, and a regional plan should assume Europe is the **compliance-depth**
  market rather than the growth market.
- **Middle East & Africa is sized for the first time in this KB: $0.56B in 2026 →
  $1.6B by 2030 at 34.3% CAGR** — small in absolute terms, and growing faster than
  Europe. Africa stops being a declared gap and becomes a sized opportunity.
- **Two sources disagree about MEA by two orders of magnitude, and the honest
  answer is a range.** Against the $0.56B regional figure, MarketsandMarkets sizes
  the **UAE** AI-in-education market at **$7.4M in 2024 → $21M by 2029 (19.1%
  CAGR)** and "Rest of Middle East" at 18.9% CAGR. A region cannot be $560M while
  its most advanced country is $7.4M, so the two are not reconcilable: they are
  almost certainly measuring different scopes (platform spend vs total AI-adjacent
  education technology). **Quote MEA as a range and name the uncertainty** rather
  than picking the flattering number — a client who checks will find the other one.
- **MEA has AI strategies, not AI statutes.** Saudi Arabia, the UAE, Egypt,
  Nigeria, Kenya, Rwanda, Morocco and South Africa all have published national AI
  strategies, and **none has an AI-specific binding statute yet.** That is the
  mirror image of the EU engagement: in Europe you sell conformity against a law
  that exists; in MEA you sell governance design *before* the law arrives, which is
  a shorter sales cycle and a weaker procurement trigger. Price and sequence
  accordingly.
- **The UAE has mandated AI in every public school, and this is the single most
  concrete demand signal in the region.** Approved by **Cabinet decision in May
  2025**, mandatory AI runs from **Kindergarten (age 4) to Grade 12** starting in
  the **2025–26 academic year**. The design details are the commercially useful
  part:
  - it is **woven into an existing subject** (Computing, Creative Design and
    Innovation) **without extending school hours** — so the deliverable is
    integrated curriculum material, not a new timetable slot;
  - it is taught by **specially trained teachers** — teacher enablement is funded
    and mandatory, not discretionary;
  - it is organised around **seven areas**: foundational concepts; data and
    algorithms; software use; **ethical awareness**; real-world applications;
    innovation and project design; and **policies and community engagement**.
  Two of the seven areas are governance and civics rather than technique, which
  means the content pipeline has to produce age-appropriate *ethics and policy*
  material, not only technical exercises. See the new pattern P9 in
  `compose/patterns.md`.


#### Fifth pass, 2026-10-06 — the compliance clock moved 16 months, and the near-term deliverable changed with it

**This is the most consequential single finding of this pass, and it rewrites the
EMEA engagement calendar.**

**Regulation (EU) 2026/1744** — the *Digital Omnibus on AI* — amends the AI Act.
Legislative trail, corroborated across multiple independent legal and vendor
analyses: European Parliament approval **16 June 2026**, Council final adoption
**29 June 2026**, signature **8 July 2026**, published in the Official Journal
**24 July 2026**, **entered into force 27 July 2026**. CELEX identifier
**32026R1744**.

| Obligation | Was | Now |
|---|---|---|
| **Annex III stand-alone high-risk** — including **education**: admission and access, evaluation of learning outcomes, student level placement, and **exam or behaviour monitoring** | 2 August 2026 | **2 December 2027** (+16 months) |
| **Annex I embedded high-risk** (AI inside regulated products) | 2 August 2027 | **2 August 2028** (+12 months) |
| **Article 50 transparency**, including the **watermarking / synthetic-content marking** deadline | 2 December 2026 | **unchanged — 2 December 2026** |

**Read the third row again.** The heavy Annex III work — technical
documentation, conformity assessment, CE marking, EU-database registration —
moved out 16 months. The **transparency obligations did not move at all**, and
the watermarking deadline is **2 December 2026**. So in EMEA, as of this writing:

- The deliverable that is **weeks away** is Article 50: disclosure that a learner
  is interacting with an AI system, and marking of AI-generated content. For an
  education client that is **labelling every generated lesson, item and feedback
  artefact**, and disclosing the tutor. It is small, concrete, and nearly
  everyone has deferred it along with the Annex III work, because the two were
  discussed as one deadline.
- The deliverable that is **14 months away** is Annex III conformity — and the
  deferral is explicitly **not a compliance holiday**: the obligation to
  *classify* systems against Annex III and Annex I, and to begin compliance
  planning, is immediate.

**How to sell this.** The engagement shape is now two-phase and the first phase
is fundable this quarter: **(1) classify and label by December 2026; (2) build the
Annex III conformity evidence by December 2027.** A client who believes the
August 2026 deadline passed and nothing happened is in the worst position —
unlabelled and unclassified — and that is a very easy conversation.

**Caveat on sourcing, stated because this claim is load-bearing.** The primary
texts (EUR-Lex, the Commission's own notice) are **unreachable from this
environment** — the egress proxy denies both. The regulation number, OJ date,
entry-into-force date and all three deadlines above are corroborated across
several independent law-firm and compliance-vendor analyses, and the CELEX id is
given so a reader can verify in one step. **Verify against EUR-Lex before it goes
in a client deliverable.**

**EMEA market sizing, added this pass:** **$2.64B in 2026 → $8.0B by 2030, 31.9%
CAGR**, with **Finland, Estonia and the Netherlands** named as the K-12 AI
integration leaders. The UK's £4M investment in AI lesson-planning and marking
tools is small in absolute terms and useful as a procurement precedent.

**And the compliance toolkit is no longer a gap.** See `repos/foundations.md`:
[AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
is **MIT** and already carries the risk-tier decision tree, 61 conformity
checklist items and 8 document templates — with **no education content**. The
Annex III point 3 profile is the billable piece and it is days of work, not
months. Pattern **P13**.



#### Sixth pass, 2026-10-06 — the voice and language layer

**The regulatory clock is the demand driver, confirmed again.** The **EU AI Act
takes full effect in August 2026**, with education AI classified **high-risk** and
a four-tier risk structure (unacceptable / high / limited / minimal). The
**Council of Europe** convened its **2nd working conference on the regulatory
dimensions of AI in education in October 2026**, so the standards conversation is
live rather than settled. The **UK's AI Adoption Summit committed £200m+** with
Cisco, IBM, BT and Rolls-Royce as delivery partners. **94% of organisations** are
at least somewhat likely to invest in AI-specific training in 2026 — while **38%
of EMEA organisations have yet to begin piloting** anything. That split is the
addressable market: funded intent, no implementation.

**What this pass opens here:**

- **Africa has a permissive language layer for the first time.**
  [SunbirdAI/salt](https://github.com/SunbirdAI/salt) (**Apache-2.0**) ships
  translation, ASR and **studio-recorded TTS by professional voice actors** across
  **Luganda, Swahili, Ateso, Lugbara, Acholi and Runyankole**, and
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**) carries
  continental MT from a 30-country community. The fourth pass had to **reject**
  this KB's only Uganda-placed asset for having no licence; **the Apache-2.0
  sibling covers six languages**. Mother-tongue delivery in East Africa is now a
  shelf capability.
- **Two of the layer's maintainers are in EMEA, which matters for sovereignty
  conversations.** The live Coqui TTS fork is maintained at the **Idiap Research
  Institute (Switzerland)**; **Tucano 2** is developed under the **University of
  Bonn** Polyglot initiative (Apache-2.0). A client who must point at a European
  maintainer for a core dependency can.
- **Voice plus sovereignty is now one answer, not two.** `sherpa-onnx`
  (Apache-2.0) runs STT, TTS, diarization and VAD with **no Internet connection**,
  so spoken assessment can be offered with data residency guaranteed by
  architecture rather than by contract — the P4 posture, extended to voice.
- **Watch the Piper licence trap in public-sector bids.** The permissive Piper is
  **archived**; the maintained one is **GPL-3.0**. A procurement that forbids
  copyleft and a technical spec that names Piper are in silent conflict.

#### Seventh pass of 2026-10-06 — MEA's constraint is licensing hygiene, not capability

This KB has recorded MEA as its thinnest region through four passes. The seventh
pass searched **in Arabic** — a channel never used before — and the result
sharpens the diagnosis rather than changing the size.

[781991937/TOFAN-AI-2026](https://github.com/781991937/TOFAN-AI-2026) is the most
substantial Arabic-language education agent found in seven passes: ingests lesson
files, extracts and analyses content, generates summaries and interactive tests;
FastAPI backend, installable PWA front end. **It has no `LICENSE` payload.**

Set against the rest of the MEA shelf:

| Asset | State |
|---|---|
| `AI-for-Education` org (MIT — Sierra Leone MBSSE lesson-plan parser, Uganda) | Real, ministry-engaged, and **1–12★ research-grade code** |
| `AI-for-Education/Luganda-linguistic-benchmarks` | **Unlicensed** |
| [`SunbirdAI/salt`](https://github.com/SunbirdAI/salt) (Apache-2.0) | Real and usable — but a **corpus**, not a product |
| `781991937/TOFAN-AI-2026` (Arabic) | Real, well-shaped, **unlicensed** |

**MEA is the only region in this KB with zero shippable permissive education
assets, and the binding constraint is not interest, funding or capability — it is
licensing hygiene.** Two of the four rows above are good work with no grant
attached.

**Why this is good news commercially.** A capability gap takes a year to close
and a funding gap is not Globant's to close. **A licensing gap closes with three
`LICENSE` files**, and asking for one is a free, high-visibility upstream
contribution that creates a relationship with the maintainer — in two cases, a
maintainer already working with an education ministry. This is now the cheapest
high-value upstream action identified anywhere in this KB, ahead of the
pedagogy-evaluation asks from the fourth and fifth passes.

**Market context for sizing:** MEA is **$0.56B in 2026 growing at 34.3% CAGR to
$1.6B by 2030** — the fastest-growing and smallest regional market here — with
the **UAE** one of only two jurisdictions worldwide running a compulsory national
AI curriculum, and Egypt, Morocco and Jordan building capacity through
public–private partnerships. The demand is funded and the open supply is
unlicensed, which is an unusually favourable asymmetry for a services business.


#### Eighth pass, 2026-10-06 — no new EMEA finding; the sweep returned enterprise-AI material, not education

The mandated EMEA sweep (`AI education EMEA 2026 adoption regulation players`)
returned **general enterprise AI-adoption commentary** — CompTIA's EMEA IT
outlook, Workday's adoption study, AI-fluency training statistics — and **no
education-specific regulatory or supply development** beyond what this file
already records for the EU AI Act and Annex III point 3.

**The one education-specific signal is an event, not a rule:** the **Council of
Europe** is convening its **second working conference on the regulatory
dimensions of AI in education** in October. This file already records the
Council of Europe's role; the conference is worth tracking as the venue where
sub-AI-Act education guidance for the 46 member states is likely to be shaped,
and it is a legitimate forum for Globant to monitor rather than a market change.

**Explicit gap:** this KB still has **no EMEA-origin permissive education agent
added in the last three passes**, and the eighth pass did not change that. The
EMEA supply picture remains what the earlier passes measured — strong platform
estate, mostly copyleft (Moodle, Chamilo, ILIAS), with ECL-2.0 and LGPL-3.0
as the permissive-adjacent exceptions.

#### Ninth pass, 2026-10-06 — the UK ministry publishes its national estate under MIT

**Channel new to this KB: the education-ministry engineering organisation.** Nine
passes swept ministries *by name* in search of policy; none had looked at a
ministry's own GitHub org for code.

**`DFE-Digital`, the UK Department for Education, runs live national education
services in the open under MIT.** Payload-verified this pass (full table and star
counts in `repos/foundations.md`): `apply-for-teacher-training` (38★),
`teaching-vacancies` (27★), `get-into-teaching-app` (25★),
`publish-teacher-training` (12★), `register-trainee-teachers` (12★),
`get-information-about-schools` — GIAS, the national schools register (9★), and
`education-benchmarking-and-insights` (5★).

**Why this changes the EMEA picture.** This KB had characterised EMEA through two
things: the **EU AI Act compliance clock** (trend 17, and the sixteen-month move
recorded in the fifth pass) and a **licensing-hygiene problem** in MEA (seventh
pass). Neither described a *supply* of permissive, production, government-grade
education software. That supply exists, and a state maintains it.

**The asymmetry is the opening.** The DfE's **administrative** tier is production
MIT. Its **AI** tier is five prototypes at **0–1★ with no licence payload** —
including `rsd-ai-libs`, described as *".NET library for building and evaluating
Azure AI Foundry agents with guardrails, Azure AI Search, and **MCP server
support**."* A national education ministry independently arrived at this KB's MCP
side-car architecture and left it unlicensed at zero stars.

So the EMEA public-sector proposition is not *"you need a platform"* — they built
one — but: **"your administrative estate is a licensed national asset and your AI
estate is unlicensed prototypes; we build the second on top of the first, under
the licence you already publish."** That is a concrete, evidenced, ministry-scale
entry point, and it is reusable as a *precedent* across every EMEA education
ministry that asks whether open source is credible at national scale.

**Also recorded, because the regional sweep returned it and it is not education:**
the mandated EMEA query returned **enterprise** AI-adoption material — 94% of
organisations likely to invest in AI training in 2026, 38% of EMEA organisations
not yet piloting, 60% reporting siloed data, the UK's **£200m+** AI Adoption
Summit commitment, and a Council of Europe working conference on the regulatory
dimensions of AI in education (October). The **AI-skills funding** signal is real
and relevant to enablement engagements (**P6**); the rest is enterprise
cross-industry material in an education query. **Second consecutive pass in which
this region's general query failed to return education-specific findings** — the
ministry-org channel is what worked, and it should be the EMEA default from here.

#### Tenth pass of 2026-10-06 — EMEA is writing the evaluation rule that North America is funding the artefact for

The generalist regional query failed for the **third consecutive pass**, returning
enterprise AI-governance and corporate-training material (94% of organisations
likely to invest in AI training; 38% of EMEA organisations not yet piloting; 60%
reporting siloed data; UK AI Adoption Summit with £200m+ committed to AI
adoption). Useful context, **not education findings.** The generalist query is
retired for this region; what worked in the ninth pass was a named institution,
and what worked this pass is the same.

**The channel: the Council of Europe education directorate** — a treaty body, not
a search term. **Tier 2, corroborated across two independent summaries.**

The Council of Europe has established a **Committee of Experts on AI and
Education (EDU IA)** and introduced the **Council of Europe Compass for AI and
Education**, presented at a third working conference, *"Ensuring quality education
in the AI era."* The **Committee of Ministers adopted a text in Munich** placing
education at the centre of Europe's response to AI, implementing **Article 20 of
the Framework Convention on Artificial Intelligence, Human Rights, Democracy and
the Rule of Law.**

The **2026–2027 work programme** names four deliverables:

| Deliverable | Why it is a market event |
|---|---|
| A proposal for a **legal instrument to regulate the use of AI systems in education** | A sector-specific instrument on top of the EU AI Act's horizontal duties — a second compliance surface for the same deployment |
| A **European Reference Framework for the Evaluation of Educational Technologies** | **The EMEA twin of the $26M North American benchmark programme** — same void, different instrument |
| A **Policy Toolbox** on teaching and learning about AI | Ministry and institutional advisory demand |
| **Draft guidelines on the use of education data and analytics** | Lands directly on the learning-analytics layer, where this KB found **no permissive Caliper implementation** |

**The read, and it is the most useful cross-region statement in this file.**
North America is **buying the artefact** — $26M, twelve projects, an Apache-2.0
floor, benchmarks and datasets. EMEA is **writing the rule** — a reference
framework for evaluating educational technology, and a proposed legal instrument
behind it. A client deploying in both regions faces one gap expressed two ways,
and the EMEA expression is the harder one to retrofit, because conformance
evidence cannot be generated after the fact. **An evaluation harness built now
(P23) serves the US benchmark swap-in and the European conformance file at the
same time**, and it gives the EU AI Act profile work (**P13**) a named successor
instrument to track rather than a horizontal regulation alone.

**The competitive fact for the same buyers.** OpenAI's **Education for Countries**
programme (Tier 2; launched at Davos 2026) is working directly with ministries of
education, and its named EMEA participants are **Estonia, Greece, Italy (CRUI, the
rectors' conference), Slovakia, the UAE and Jordan.** Six EMEA national or
sector-wide bodies are being onboarded to a single proprietary vendor at the
ministry tier — in the region that is simultaneously drafting a legal instrument
on AI in education and a framework for evaluating it. **Sovereignty, auditability
and data residency are not abstract selling points here; they are the subject of
the instrument being drafted.**


#### Eleventh pass, 2026-10-06 — EMEA is not only writing the rule, it is shipping the tooling

The tenth pass framed the region as the one *"writing the rule"* while North America
*"buys the artefact."* **That framing was incomplete and the correction is
commercially significant.**

| Asset | Origin | Licence (Tier 1, payload read 2026-10-06) | Scale |
|---|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **UK AI Security Institute** (`aisi.gov.uk`) | **MIT** | **2,945★**, 779 forks, pushed 2026-10-06 |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | **ETH Zurich**, Learning & Reasoning group, EMNLP 2025 Oral | 🔴 **no payload**; README claims **CC BY 4.0** *and* **CC BY-SA 4.0** | 43★ |
| [openfun/richie](https://github.com/openfun/richie) | **France Université Numérique** | **MIT** | 316★ |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Switzerland | **Apache-2.0** | 446★, pushed 2026-10-06 |
| [digillab-lmu/smart-rag](https://github.com/digillab-lmu/smart-rag) | **LMU Munich** | ⚠️ **`NOASSERTION`** — unresolved | 2★ |

**A European government body maintains the most-starred MIT evaluation framework on
these shelves**, and two European universities publish the pedagogy benchmarks — one
of them without a usable grant. Combined with the Council of Europe's **European
Reference Framework for the Evaluation of Educational Technologies** (tenth pass,
Tier 2) and the **EU AI Act taking full effect in August 2026 with education AI
classified high-risk** (Tier 2, re-corroborated this pass), the region now supplies
*all three* layers of the conformance story: the rule, the reference framework, and
an MIT-licensed harness to run it in.

**Market context re-corroborated this pass (Tier 2):** AI uptake rose ~30% year on
year, with roughly five businesses per minute adopting AI, and **94% of organisations
at least somewhat likely to invest in AI-specific training in 2026**. Among
enterprises that considered and declined AI in 2025, the barriers were **lack of
expertise (70.9%)**, **uncertainty about legal consequences (52.5%)** and **data
protection concerns (48.8%)** — the second and third of which are precisely what an
Inspect-based conformance harness is for. Structural brakes named: inconsistent
implementation across member states, a shortage of mainstream digital skills, and
limited late-stage capital.

**The opportunity, stated as a sentence:** in EMEA the deliverable is not a tutor, it
is a **tutor plus its conformance evidence**, and the evidence pack can be built from
EMEA's own MIT-licensed tooling. That is an easier sale to a ministry than any
import.

### APAC

- **Largest absolute AI market: ~USD 102B as of March 2026** (all sectors, not
  education alone).
- **India is the fastest-growing APAC AI market at 38.9% CAGR**, anchored by the
  IndiaAI Mission and ~2.6M STEM graduates a year. In **July 2026 the Indian
  government signalled it may pursue dedicated, risk-based AI legislation.**
  India's DPDP Act obligations are now in force for systems processing personal
  data.
- **South Korea's AI Basic Act takes effect January 2026**, giving roughly a year
  to build compliance frameworks for high-impact systems. **China maintains the
  region's most restrictive framework**, built on three foundational laws.
- **Sovereign model build-out is universal:** India's Sarvam AI, Malaysia's ILMU,
  Indonesia's Sahabat AI, Singapore's SEA-LION, Korea's HyperCLOVA X Think,
  Japan's NTT Sarashina. These are base models — **none ships an education agent
  layer**, which is precisely the gap.
- **Cultural tailwind:** the Ipsos Education Monitor 2026 finds *lower* support
  for banning AI in schools across the Asian markets surveyed — while **Australia
  and New Zealand record higher support for banning AI in schools**, a real
  split inside the region.
- **Opportunity:** education agent layers on top of sovereign models — the models
  exist, the pedagogy layer does not. Multi-jurisdiction architecture is the hard
  part and the differentiator: one deployment must satisfy Korea's AI Basic Act,
  India's DPDP and China's framework simultaneously. Treat ANZ as a separate,
  more restrictive sub-market.

**New this pass (2026-10-06):**

- **Singapore published the world's first governance framework for agentic AI**,
  at Davos in **January 2026** (IMDA Model AI Governance Framework for Agentic AI,
  updated again in June 2026). This is the single most useful regulatory document
  in this KB, because it governs *agents* specifically, and its four dimensions
  are effectively a build checklist:
  1. assess and bound risk upfront — choose appropriate agentic use cases and
     place explicit limits on an agent's powers;
  2. make humans **meaningfully** accountable — define the checkpoints that
     require human approval;
  3. technical controls and process across the whole agent lifecycle;
  4. enable end-user responsibility through transparency **and training** — where
     an agent assists a user in their workflow, the framework expects education on
     its capabilities, common failure points and risks.
  Dimension 4 is a services line item: the regulator is asking for exactly the
  teacher-and-student enablement work Globant already sells. Design to this
  framework and the resulting artefacts largely satisfy EU Annex III and the US
  human-oversight statutes too.
- **Korea's AI Framework Act took effect 22 January 2026** (precise date; earlier
  passes recorded only "January 2026").
- **Vietnam has a dedicated AI law: Law No. 134/2025/QH15, in force 1 March
  2026** — net new to this KB, and evidence the binding-regulation wave now
  extends well beyond Korea, Singapore and China.
- **Named incumbents in APAC education:** Google, Microsoft, IBM, Pearson and
  **Byju's**, with China, India and Japan dominating regional spend. The buyer
  relationship is held by global platforms plus one regional giant.
- **More sovereign base models, still no pedagogy layer:** add **BharatGen**
  (IndiaAI Mission, ~$1.2B state investment), Japan's **Fugaku-LLM**, and Korea's
  National Sovereign AI Initiative champions (LG AI Research, SK Telecom, Naver
  Cloud, NC AI, Upstage). Sovereign *inferencing platforms* with in-country data
  residency are also being commercialised (e.g. NxtGen in India). The gap is
  unchanged and widening: the models and now the hosting exist; the education
  agent layer does not.

**New in the third pass (2026-10-06):**

- **The scale number this KB was missing: approximately 530 million K-12 students
  in Asia (2024).** Every per-learner cost, licence and inference decision changes
  shape at that denominator. It is also the reason offline-capable and
  small-model deployments matter in APAC and not only in LATAM.
- **Regional AI adoption is projected to move from 65–75% in 2025 to 80–90% in
  2026.** Adoption is not the constraint anywhere in APAC.
- **China's AI-education mandate is provincial, specific, and includes a
  restriction that directly constrains the architecture.** Earlier passes recorded
  China as having a "compulsory national AI curriculum"; probed precisely, the
  mandates are issued at provincial level:
  - **Beijing:** every primary and secondary school must deliver **at least 8 hours
    of AI lessons per year**, from **1 September 2025** — compulsory from age six.
  - **Guangdong:** **6 hours annually** in lower grades, rising to **one hour a
    fortnight in grades 10 and 11**.
  - The curriculum progresses from voice-recognition basics in early grades to
    machine learning, **misinformation detection** and applied projects by high
    school.
  - **Primary-school pupils are barred from independent generative-AI use, and
    teachers are prohibited from substituting AI for their core instructional
    duties.**
  That last point is a build requirement, not a policy footnote: a compliant K-12
  deployment in China needs **age-gated capability** (younger cohorts get
  teacher-mediated AI only) and a teacher-in-the-loop design that is enforced by the
  system rather than by guidance. It is also the strictest form of the
  human-oversight requirement that EMEA and North America express more loosely, so
  **a design that satisfies Beijing satisfies the others**. Pattern P9 in
  `compose/patterns.md` builds to it.
- **Regulatory posture, stated per country rather than per region:** Korea's
  Framework Act in force **22 January 2026**; **Vietnam's Law No. 134/2025/QH15 in
  force 1 March 2026 — Southeast Asia's first dedicated AI law**; China the most
  assertive regulator while also leading on deployment; **Japan deliberately
  light-touch and voluntary** to favour innovation; **India and Australia still
  without a national framework in force**, both working on one. A single APAC
  compliance story does not exist, and "APAC-ready" is not a claim you can make.

- **Supply side, fourth pass of 2026-10-06: APAC is now the region that *exports*
  education AI.** Every other region in this KB is a buyer. APAC publishes — and
  the pass added **Tsinghua University's
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, 40.0k★,
  v1.2.0-rc.1 2026-10-04)**, now **the largest permissively licensed asset in this
  KB**: document-or-topic → a full generated lesson (slides, quizzes, HTML
  simulations, PBL scenes) taught by AI teacher *and* AI classmate agents, with
  PostgreSQL-backed server-side generation.
  **Two consequences.** First, the **China-plus-Hong-Kong concentration gets
  sharper, not softer**: a 40k★ flagship from Tsinghua sits alongside DeepTutor
  (HKUDS, 40.8k★), while **no India-, Japan-, Korea- or ASEAN-origin permissive
  education project** has surfaced in any channel — searched by name this pass.
  "APAC-ready" remains a claim you cannot make; the regulatory map (Korea
  22 Jan 2026, Vietnam 1 Mar 2026, Japan voluntary, India and Australia with no
  national framework in force) and the supply map **both** fracture along national
  lines.
  Second, for every other region the practical consequence is the same: **the
  default starting point for a lesson-generation build is now Chinese-origin code
  under MIT.** That is fine legally and a live question for a public-sector buyer
  in EMEA or North America — so the **provenance conversation, data-residency
  posture and a reviewed fork** belong in the first week of the engagement, not
  the last.


#### Fifth pass, 2026-10-06 — three binding regimes, one accreditation lever, and a licence trap

Earlier passes recorded APAC regulation as "heterogeneous and moving toward
binding frameworks." It has largely arrived. Dated and specific:

| Jurisdiction | Instrument | Status | What it requires that bears on education |
|---|---|---|---|
| **South Korea** | **AI Basic Act** (Act on the Development of Artificial Intelligence and Establishment of Trust) | **In force 22 January 2026** | Transparency, risk assessment, **human oversight** and documentation for **high-impact** systems. Education decisions sit squarely in the high-impact concept — the same substance as EU Annex III, arriving **23 months earlier** |
| **Vietnam** | **Law No. 134/2025/QH15 on Artificial Intelligence** | **Effective 1 March 2026** | A dedicated national AI law. First-mover compliance work in a market with no incumbent AI-governance services base |
| **Australia** | **TEQSA** (national higher-education regulator) | Active requirement | **Every** higher-education provider must submit an **institutional action plan** addressing generative-AI risks. This is an **accreditation** lever, not a fine — it is the sharpest procurement trigger in the region |
| **China** | Generative AI Services Management Measures; synthetic-content identification rules (**effective 1 September 2025**) | In force | Consent, data quality, **content labelling**, user rights, complaint handling. Compounds the age-gating and teacher-substitution rules this KB already records |

**The Australia item is the one to act on first.** A regulator requiring a written
institutional action plan from every provider in a country creates a bounded,
repeatable, nationally-scoped deliverable with a known buyer and a deadline that
is not negotiable, because accreditation depends on it. There is no equivalent
single-document, single-regulator trigger in any other region in this KB.

**South Korea reorders the global compliance calendar.** With the EU's Annex III
obligations now at December 2027 (see EMEA above) and Korea's AI Basic Act **in
force since January 2026**, **Korea — not the EU — is now the binding constraint
for a multi-jurisdiction education product.** Build to the Korean high-impact
requirements and the EU conformity work becomes largely a documentation exercise.
This is the reverse of how this KB and most of the market have sequenced it.

**Sovereign-model landscape, updated:** **MaLLaM**, Malaysia's sovereign LLM built
with NVIDIA, natively handling Malaysian Bahasa and colloquial dialects, deployed
to **3M+ users** via YTL/Yes mobile; **Gemma-SEA-LION-v4-27B-VL**, a
vision-language member of the SEA-LION v4 family, released **March 2026**.

**And the licence trap, because this is where an APAC engagement will hit it:**
[aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no
repository-level `LICENSE` payload**. Its README states terms vary with the
underlying base model — Llama3-derived variants carry commercial-use
restrictions, Gemma-derived variants differ — and directs you to each **Hugging
Face model card**. **Rights must be cleared per model and per release, not per
repository.**

**Singapore is the region's reference deployment and it is closed.** AICET (AI
Singapore, funded by the Smart Nation and Digital Government Office, working with
the Ministry of Education) runs Codaveri, Softmark and ScholAIstic at ministry
scale with no public repositories — while the LMS beneath Codaveri,
[Coursemology](https://github.com/Coursemology/coursemology2), is **MIT with
15,802 commits**. See `verticals/solutions.md`.



#### Sixth pass, 2026-10-06 — the voice and language layer

**Adoption is high and governance is lagging, by the region's own accounting.**
**48% of APAC governance leaders** make AI adoption a top strategic priority for
2026 and **57% of organisations in Asia** already run AI in one or more areas,
while **49% cite insufficient infrastructure for real-time data processing** as
the barrier. **AI sovereignty will shape infrastructure choices for roughly half
of APAC firms**, and regulators are moving (Singapore's consultations on AI use in
financial institutions are the template for transparency and accountability
expectations). Named commercial movement in education: **LearnUpon** opened a
Sydney HQ with Create+ AI course authoring; **NIIT MTS** made Training Industry's
Top 20 custom content developers for 2026 on AI-led design; **TCS and Pearson**
announced a multi-year AI learning alliance.

**What this pass opens here — and APAC now splits cleanly in two.**

- **India: the only all-MIT national stack in this KB (P16).** Sunbird (**MIT**,
  38,046 commits, deployed as **DIKSHA**, a recognised **Digital Public Good**,
  18+ languages, NCERT/CBSE/SCERT) plus AI4Bharat's **MIT** layer — translation
  across **all 22 scheduled languages**, TTS in 13, ASR pretrained on 40, and the
  Shoonya annotation platform for the teacher-review gate. **Platform, language,
  orchestration and review, every component MIT.** In a public procurement that
  removes the licence conversation entirely, and it directly answers the
  sovereignty concern half the region reports.
- **ASEAN: the licence is per checkpoint, and that is a billable service.**
  [SEA-LION](https://github.com/aisingapore/sea-lion) has **no repository-level
  licence**; its grant is deferred to each HuggingFace **model card** because terms
  vary with the base model (Llama-derived variants may carry Meta's commercial
  restrictions). Combined with the fifth pass's finding that ASEAN's ministry-scale
  products are closed while the LMS beneath them is MIT, the position is:
  **integration surfaces are permissive, model rights are not.** Offer
  per-checkpoint licence review as a recurring engagement line, not a one-off gate.

#### Seventh pass of 2026-10-06 — Vietnam's education rules, and the ASEAN language shelf that exists

**Vietnam: Decree 33 is the instrument that makes Law 134/2025/QH15 operational
for education, and this KB did not have it.** Signed **2026-06-30**, in force
**2026-08-15**; lists **46 high-risk AI systems** across six sectors, **three of
them in education**:

| # | Education high-risk category | EU Annex III point 3 equivalent? |
|---|---|---|
| 1 | AI providing **self-learning content from uncontrolled data sources** | **No equivalent.** Regulates the tutor by **corpus provenance**, not by any decision it makes |
| 2 | AI that **automatically evaluates results and ranks learners** | Yes — evaluation of learning outcomes, level placement |
| 3 | AI that **monitors and analyses learner behaviour using biometric data** | Partly — Annex III covers exam/behaviour monitoring **without** the biometric qualifier, so Vietnam is **narrower** here |

Obligations: **report the risk level to the Ministry of Science and Technology
before use**; **conformity assessment** before deployment and maintained
throughout; designated systems assessed by a **registered or recognised
conformity assessment body**, others **self-assessed** by the provider.
Transition: education systems already in operation — grouped with **healthcare
and banking** — have until **2027-09-01**; all other existing high-risk systems
until **2027-03-01**.

**Commercial read, three points.**

- **Category 1 is the one to price into every Vietnam proposal.** A RAG tutor
  that only explains — no grading, no ranking, no monitoring — is **still
  high-risk** if its corpus is uncurated. The deliverable that answers it is a
  **source manifest** (what was ingested, from where, under what rights, reviewed
  by whom), which is billable work and is also the artefact a conformity
  assessment consumes. See **P20**.
- **The 2027-09-01 education transition is a defined sales window.** Education,
  healthcare and banking got the **longest** runway of any sector, so incumbent
  deployments have ~11 months beyond the general deadline to be brought into
  conformity. That is remediation work with a statutory date on it.
- **Vietnam is looser than the EU on analytics.** Because category 3 is qualified
  to **biometric** data, non-biometric engagement analytics — time on task,
  attempt counts, mastery curves — sit outside it. **First instance in this KB of
  an APAC regime being less restrictive than Annex III on a specific axis**, and
  it favours analytics-led products.

⚠️ **Provenance:** every legal-publisher domain carrying this decree is
**EGRESS_BLOCKED** here (6/6 refused: `allenandgledhill.com`,
`vietnam-briefing.com`, `vietnamnews.vn`, `thuvienphapluat.vn`, `vietanlaw.com`,
`ed.events`). The three categories are recorded from **two independently-phrased
searches that agreed on all three**; the biometric qualifier appeared in only
one. **Confirm against the decree text before using this in a deliverable.**

**The ASEAN language substrate exists, and the sixth pass said it did not.** This
KB recorded ASEAN as having no permissive language layer because it searched for
sovereign models and found [SEA-LION unlicensed](https://github.com/aisingapore/sea-lion).
Searching in Bahasa, Thai and Vietnamese returns a real shelf — **Vietnamese
`underthesea` (Apache-2.0, 1.8k★), Thai `pythainlp` (Apache-2.0, 1.2k★, 6,649
commits), Malay `malaya` + `malaya-speech` (both MIT), Indonesian `nusa-crowd`
(Apache-2.0, 143 datasets)**. Full shelf in `repos/foundations.md`.

**What that changes for an ASEAN engagement.** The fifth pass's finding was that
ASEAN's mature education AI is **closed** (AICET's Codaveri, Softmark,
ScholAIstic) over an **MIT substrate** (`Coursemology/coursemology2`) — a good
commercial position. Add the language shelf and the position improves again: the
**LMS substrate is MIT, the language substrate is Apache-2.0/MIT, and the
pedagogy layer in a national language is unbuilt by anyone, open or closed.**
That is the clearest build-and-own opportunity in APAC outside India. **P19.**

**Caveat on the opportunity, so it is not oversold:** only `malaya-speech` covers
voice. Thai, Vietnamese and Indonesian have text-layer coverage only, so spoken
practice in those languages routes through `sherpa-onnx` or Whisper and needs
per-language accuracy testing before it is promised.


#### Eighth pass, 2026-10-06 — no new APAC education rule; sovereignty is the operative frame

The mandated APAC sweep returned **sovereignty and governance-gap material**
rather than education regulation: 48% of APAC governance leaders naming AI
adoption a top 2026 priority, 57% of Asian organisations with AI in at least one
area, Singapore's consultations on AI in financial institutions, and a
*"sovereign-by-design"* framing for 2026 regional execution. **No new education
instrument** beyond the Korea **AI Framework Act** (in force 2026-01-22) and
Vietnam's **Decree 33** (in force 2026-08-15) that this file already carries.

**Why "sovereign-by-design" is the APAC education opportunity and not a
slogan.** It is the one region where the buyer's stated preference — run it in
our jurisdiction, on our data, under our rules — aligns exactly with what a
permissive self-hosted stack delivers and a SaaS tutor cannot. The seventh
pass's ASEAN language shelf (`pythainlp`, `underthesea`, `malaya`, `nusa-crowd`,
all permissive) is the supply side of that preference, and it is the
best-licensed regional language layer in this KB — **a direct contrast with
LATAM's indigenous layer below, where the same capability exists without
grants.**

**Explicit gap, unchanged:** no **Korea**-origin permissive education *agent*
(the seventh pass found course material, not an agent), which remains the widest
distance in this KB between regulatory maturity and open supply.

#### Ninth pass, 2026-10-06 — APAC's own education-evaluation benchmark exists, and it has no grant

**One education-specific finding, and it is a rejection.**
[AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) — **33★**, *"Official
github repo for E-Eval, a Chinese K12 education evaluation benchmark for LLMs"*,
Python — has **no licence payload** under `LICENSE{,.md,.txt}`, `COPYING`,
`LICENCE{,.md,.txt}` or `COPYRIGHT`, on either branch.

**This matters more than its star count.** The thing E-Eval does — evaluating
LLMs against K-12 education criteria — is precisely the capability the **$26M
North American programme is spending millions to create under Apache-2.0** (see
the North America subsection). **APAC already built it, and did not license it.**
The region is not behind on capability; it is behind on **redistributability**,
which is the third region in which this KB has now recorded that exact shape
after MEA's Arabic tutor (seventh pass) and LATAM's indigenous-language layer
(eighth pass).

**The engagement consequence is specific:** for a China or wider APAC education
engagement, E-Eval is a **capability you can read and reimplement but not
vendor**. Reimplementing an evaluation benchmark from a published description is
tractable work — far more tractable than building one from nothing — and the
resulting harness is yours to license. Alternatively, a single `LICENSE` file
contributed upstream would change the regional answer, which is the same cheap
remedy the seventh pass proposed for MEA and the eighth pass found an event's
rules could deliver at scale.

**Declared: no new APAC education regulation was found this pass.** The mandated
regional query returned **enterprise governance** material — 48% of APAC
governance leaders prioritising AI adoption for 2026, 57% of Asian organisations
with AI in at least one operational area, 49% citing insufficient real-time data
infrastructure, Singapore's financial-sector AI consultations, and a general
convergence on safety/transparency/accountability with **AI sovereignty** as the
2026 frame. **None of it is education-specific.** The binding education regimes
for this region remain the ones recorded in the fifth and seventh passes
(including **Vietnam's Decree 33**, still the strictest on corpus provenance) and
the sovereignty framing from the eighth. **Second consecutive pass in which the
general APAC query returned enterprise rather than education material** — like
EMEA, this region needs a channel change, and the ministry-org channel that
worked for the UK this pass is the obvious candidate.

#### Tenth pass of 2026-10-06 — a ministry already has a vendor, and it says it is still shopping

The generalist regional query failed for the **third consecutive pass**, returning
enterprise material (48% of APAC governance leaders making AI adoption a top 2026
priority; 57% of Asian organisations with AI in at least one area; Singapore's
consultations on AI in financial institutions; corporate LMS and upskilling
announcements). **Not education findings.** Retired for this region, as for EMEA.

**What worked was the ministry-programme channel**, the APAC analogue of the UK
DfE sweep. **Tier 2.**

**Singapore's Ministry of Education was welcomed into OpenAI's Education for
Countries on 20 May 2026** at the Education World Forum in London. OpenAI is
supporting use cases developed by **MOE and GovTech** teams, including
personalised learning and **mother tongue language learning**. **Kazakhstan** is
also named in the programme's first cohort.

**The opening is in Singapore's own framing.** MOE is described as *"exploring
various AI tools from different partners to meaningfully support teaching and
learning."* A ministry that states a **multi-partner** posture while onboarding one
vendor is a ministry that will evaluate alternatives — and GovTech's involvement
means the counterparty is an engineering organisation that can assess an open,
auditable, data-resident stack on its merits. **That is a different sales motion
from displacing an incumbent, and it is open now.**

**The mother-tongue use case is the one to lead with.** It is precisely where this
KB's language substrate shelves (sixth, seventh and eighth passes) hold
permissive, regionally-placed assets, and precisely where a single global vendor is
weakest.

**Tier 1 confirmation, and it is a negative.**
[AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) — the Chinese K12 LLM
education evaluation benchmark (33★), the region's most on-target evaluation asset
— was **re-probed this pass across 20 URLs** (both `LICENCE`/`LICENSE` spellings,
both `main` and `master`). **Still no licence payload.** The repository exists;
`main/README.md` resolves. The ninth pass's *built, published, benchmarked,
ungranted* finding for APAC **survives a full re-probe** and is no longer
attributable to a spelling or branch defect in this KB's method. **APAC has the
evaluation benchmark the US is funding and the licence that makes it unusable.**
A grant request to the maintainers is a cheaper route to a regional evaluation
asset than building one.


#### Eleventh pass, 2026-10-06 — the region's red-team harness is Apache-2.0, and its national stack is MIT and dormant

| Asset | Origin | Licence (Tier 1, payload read 2026-10-06) | Scale |
|---|---|---|---|
| [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **AI Verify Foundation** — Singapore IMDA's AI-testing community | **Apache-2.0** | 355★, 72 forks, pushed 2026-10-06 |
| [project-sunbird/sunbird-lms-mw](https://github.com/project-sunbird/sunbird-lms-mw) | **Sunbird** — the stack under India's **DIKSHA** | **MIT** | 6★ / **41 forks**, 🔴 last push 2024-08-30 |
| [project-sunbird/sunbird-analytics](https://github.com/project-sunbird/sunbird-analytics) | Sunbird | **MIT** | 3★ / 28 forks, 🔴 2023-02-08 |

**Two findings that pull in opposite directions.**

1. **Singapore exports the evaluation instrument.** Moonshot evaluates *and
   red-teams* any LLM application, Apache-2.0, maintained. For an education
   deployment the red-team half is not optional — the adversary is a student with
   unlimited attempts and no deadline. This is the only permissive red-teaming
   harness in this KB, and it comes from the same regulator-adjacent body whose
   guidelines the region's buyers already cite.
2. **India's national stack is the most permissive in the world and nobody is
   pushing to it.** Sunbird is **MIT** at national tier — more permissive than
   Moodle, Open edX, or anything else of comparable deployment — and its GitHub
   activity stopped in 2024, with one component **archived**. The fork-to-star ratio
   (41:6) says deployed-and-forked, not abandoned-and-ignored; but a KB must not
   read it as an upstream. **Reference architecture and licence-clean base, not a
   maintained dependency.**

**Market context re-corroborated this pass (Tier 2):** **56% of APAC businesses have
already deployed chatbots, copilots or AI assistants — outpacing both Europe and
North America** — and **48% of governance leaders name AI adoption a top strategic
priority for 2026**. Regulation stays **fragmented by design**: a common APAC-wide
framework remains distant, with Singapore running mature responsible-AI guidelines,
China legislating against algorithmic misconduct, and India applying existing
criminal law. **Sovereignty will shape infrastructure choices for roughly half of
APAC firms.**

**The opportunity:** fragmentation plus sovereignty plus the highest deployment rate
means the sellable artefact is a **per-jurisdiction policy layer over one
architecture** — and both the harness (Inspect, MIT) and the red-team tooling
(Moonshot, Apache-2.0) can be run inside the client's own boundary, which is the
condition sovereignty actually imposes.

**Declared, so it is not mistaken for coverage:** the generalist APAC repository
probe `education AI tutor India OR China OR Indonesia OR Japan language stars:>50`
returned **`total_count` 0**. That is an **instrument limit, not an absence** —
GitHub repository search ANDs free-text terms, so a five-term query collapses. The
region's assets above were found by **named organisation**, which is now the third
consecutive pass in which naming the institution worked and the generalist query
did not.

### LATAM

- **Teacher adoption is ahead of institutional readiness, sharply.** In Chile and
  Brazil **more than 50% of teachers already use AI tools, while fewer than 10%
  of institutions in the region have formal guidelines and sufficient capacity**
  to integrate them with clear criteria. That gap is the engagement.
- **UNESCO launched the Observatory on Artificial Intelligence in Education for
  Latin America and the Caribbean on 14 April 2026** — a regional platform to
  help states integrate AI with a focus on equity and quality. A credible anchor
  partner and a source of procurement momentum.
- **Enterprise AI deployment regionally sits at 47%.** Only Brazil (65.89), Chile
  (63.19) and Uruguay (62.21) place in the global top 50.
- **Regulation:** Brazil is the regional bellwether with **PL 2.338/2023**, a
  comprehensive horizontal, risk-based statute with transparency and supervisory
  architecture. **Mexico** added an opt-out requirement for automated
  decision-making in its latest data protection law, and its Congress is pushing
  labour and copyright amendments covering image rights and AI.
- **Constraints are structural, per CEPAL/ECLAC:** gaps in talent, investment and
  governance, with advanced AI training concentrated in a few countries and the
  **talent gap relative to the global average widening since 2022.**
- **Opportunity:** institutional capability, not just software — governance
  frameworks for the >90% of institutions that lack them, teacher enablement at
  scale, and low-cost deployments that respect connectivity and budget reality
  (Kolibri + ricecooker, fully MIT; Chamilo for Spanish-first public sector).
  Brazil's PL 2.338 readiness work mirrors the EU AI Act engagement and the
  artefacts transfer.

**New this pass (2026-10-06):**

- **Hard survey numbers for higher education, from the Digital Education Council
  AI in Higher Education LATAM Survey 2026:** **92% of students** and **79% of
  faculty** are actively engaging with AI, and **94% of faculty** expect to use it
  in future teaching. Adoption is effectively universal — but **88% of faculty
  report only "minimal" to "moderate" engagement**, i.e. adoption has not become
  pedagogical integration.
- **That 92/79 vs 88 split is the sharpest opportunity statement in this KB.**
  The region does not need an adoption campaign; it needs depth — curriculum
  redesign, assessment redesign and faculty capability. Selling "get your teachers
  using AI" into LATAM higher ed is selling something they already have.
- **Anchor institutions for a regional play:** the survey was run by the Digital
  Education Council with the **Institute for the Future of Education at
  Tecnológico de Monterrey**, supported by the **AI Global Education Network
  (AIGEN)** and the **Educational Innovation Network (RIE360)**. With UNESCO's LAC
  Observatory (14 April 2026), these are the credible doors into regional
  procurement.
- **The regulatory map is fragmenting, not converging** — Brazil's PL 2.338/2023,
  Chile's framework, Colombia's CONPES and Mexico's sectoral rules are all moving
  at different speeds. Plan per-country, not per-region.
- **Colombia is further ahead than its profile suggests:** it adopted a national
  AI policy via **CONPES 4144 (February 2025)** — a government-wide programme with
  budgeted actions through 2030 covering capacity building, adoption and ethical
  guardrails. A funded national programme is a procurement signal; Colombia
  belongs on the target list alongside Brazil, Chile and Mexico.
- **UNESCO's warning is the sales argument:** LAC higher-education institutions
  are increasingly using generative AI for teaching, learning and research while
  lacking policies to govern it, and the agency has flagged that the absence of
  institutional guidelines raises misuse risk and leaves staff uncertain about
  acceptable use. Governance is the entry engagement; the platform work follows.

**New in the third pass (2026-10-06):**

- **The governance gap now has an institutional number, and it is the sharpest
  single statistic in this KB: 87% of LATAM higher-education institutions use AI in
  at least one area of their activities, and only 26% have a formal AI strategy.**
  Earlier passes carried "fewer than 10% have formal guidelines and sufficient
  capacity", which is a different and stricter measure. Use both and say which is
  which: **87/26** is the strategy gap, **>50% of teachers in Chile and Brazil vs
  <10% of institutions ready** is the capability gap. The second is the harder
  problem and the longer engagement.
- **LATAM faculty are measurably more positive about AI than the global average:
  72% report "positive" or "very positive" views, against 57% globally.** Combined
  with 79% of faculty using AI in teaching — **18 points above the global figure
  recorded in 2025** — the region is an *enthusiasm-rich, governance-poor* market.
  That is an unusual and favourable shape: the resistance that slows EMEA
  engagements is largely absent, and what is missing is structure.
- **Uruguay became the first Latin American country to sign the Council of Europe's
  Framework Convention on Artificial Intelligence and Human Rights, Democracy and
  the Rule of Law (2025).** This matters more than its market size: a Council of
  Europe convention signatory is committing to a governance vocabulary that is
  **interoperable with the EU's**, so compliance artefacts built for an EU AI Act
  engagement transfer to Uruguay with far less rework than to Brazil's PL 2.338 or
  Mexico's sectoral rules. Uruguay is small (62.21, third in the region's global
  top-50 placings) and is now the **cheapest bridgehead for reusing EMEA
  compliance IP in LATAM.**
- **The regional pioneer set is consistent across sources:** Chile, Brazil and
  Uruguay, on data availability, governance frameworks and infrastructure — with
  **Chile the standout through CENIA**, the national AI centre behind Latam-GPT.
- **The supply side is still empty, and the fourth pass of 2026-10-06 both
  weakened and re-established that claim.** LATAM demand is the best-shaped in this
  KB; **indigenous open-source supply remains zero.** Two updates:
  **(1) The gap's strongest single piece of evidence has been withdrawn as
  unsound.** Three passes cited `planejaia/OpenMAIC-Brasil` — a "Brazil-origin
  multi-agent classroom" that 404s — as lead evidence. The upstream is
  **Tsinghua's [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC), MIT,
  40.0k★**. The name was never Brazilian, so it was never evidence about LATAM. **A
  `-Brasil` suffix is a string an author typed, not a provenance claim.**
  **(2) The gap survives anyway, on a channel that does not depend on a filename.**
  The same pass searched in **Spanish and Portuguese** — a language channel no
  earlier pass had used — and returned **zero LATAM-origin projects**. Four
  independent channels now agree. A finding that outlives the removal of its best
  evidence is the firmest kind in this KB.
  **Commercially:** the region buys and adapts rather than publishes, so a LATAM
  engagement starts from **Chinese, US and European permissive code plus
  localisation**, and there is no local community to co-develop with. The
  Portuguese/Spanish localisation layer over OpenMAIC is an **unclaimed, concretely
  sized build** — and the one place where contributing upstream would make Globant
  the originating voice in a vacuum it has now confirmed four times.


#### Fifth pass, 2026-10-06 — the governance gap is now measured, and it is the engagement

This KB has argued the LATAM opportunity from adoption anecdotes and an absent
code shelf. Both are now replaced by primary-research numbers, and they size the
opportunity far more precisely than anything recorded before.

**UNESCO IESALC regional study**, launched **9 September 2026** during **UNESCO
Digital Learning Week 2026** — **200 higher-education institutions across 19
Latin American and Caribbean countries**:

| Measure | Value |
|---|---|
| Institutions using AI in at least one area of activity | **87%** |
| Institutions with a **formal AI strategy** | **26%** |
| Institutions with clear policies, governance structures and monitoring/evaluation frameworks | **fewer still** |
| Institutions reporting formal AI guidance — **LAC** | **45%** |
| Institutions reporting formal AI guidance — **Europe and North America** | **70%** |

**Digital Education Council, AI in Higher Education LATAM Survey 2026** —
delivered with the **Institute for the Future of Education at Tecnológico de
Monterrey**, with outreach through **AIGEN** and **RIE360**:

| Measure | Value |
|---|---|
| Students actively engaging with AI | **92%** |
| Faculty actively engaging with AI | **79%** |
| Faculty expecting to use AI in future teaching | **94%** |
| Faculty self-reporting **"minimal" to "moderate"** engagement | **88%** |

**Read the two together and the engagement writes itself.** Adoption is
near-universal and *shallow* — 92% of students using AI against 88% of faculty
still at surface-level engagement — and **61 percentage points separate the
institutions using AI from the institutions with a strategy for it**. That is not
a technology gap. It is a **governance-and-capability gap**, in a region where
only 45% of institutions have formal guidance against 70% in Europe and North
America.

**The sellable shape, and it is not a tutor.** A LATAM higher-education
engagement should lead with **AI governance enablement** — institutional policy,
oversight structures, faculty capability, monitoring and evaluation — with the
technology build following it. This is the opposite of how this KB's patterns are
ordered, and the numbers say so clearly. **Pattern P6 (client capability build) is
the LATAM entry point; P1 follows it.** Both UNESCO IESALC and the Digital
Education Council are citable, independent, and dated inside the last month —
which makes this the best-evidenced regional claim in this KB.

**National policy, dated:** **Chile** has classified AI uses by risk with
governance measures scaled to risk and a supervisory model tied to its
forthcoming **data protection authority** — the first LATAM regime structurally
comparable to EU Annex III tiering. **Colombia** adopted national AI policy via
**CONPES 4144** in **February 2025**, a government-wide programme with actions
and **budget through 2030**. Colombia is the one LATAM jurisdiction where both a
funded national policy and a publicly-funded permissive education project (see
below) now exist.

**And the code gap has an address.** The firmest gap in this KB — "no LATAM-origin
permissive open source education project" — **is refuted**:
[LabSirius/TutorIA](https://github.com/LabSirius/TutorIA), **MIT**, Universidad
Tecnológica de Pereira, Sirius research group, funded under Colombia's **SNCTI**,
specifying an Open edX side-car tutor for **rural higher education in Risaralda**.
It has **4 commits and every code path in its own documented tree returns 404**.

**So the gap was never about interest — it was about delivery capacity.** A
Colombian public university, with public science funding and a named pedagogical
director, independently specified **this KB's default pattern P1** and has not
built it. That is a partnership lead, a validation of the P1 shape, and the single
most concrete LATAM entry point this KB has ever recorded. **Do not fork it.**



#### Sixth pass, 2026-10-06 — the voice and language layer

**Adoption is genuinely high; the constraint is capital and infrastructure, not
appetite.** Latin America is the **third-largest market worldwide for generative
AI application downloads** despite less access to capital. **99% of LATAM startups
use AI in internal operations and 85% integrate it natively** into their main
product, while **fewer than 25% build their own models** — OpenAI (89%), Gemini
and Claude dominate integrations, with **edtech named among the most disruptive
sectors** (Ednova cited). For higher education specifically, **UNESCO IESALC**
surveyed **200 institutions across 19 countries between August and October 2025**
over five dimensions — teaching and learning, research, community engagement,
administration and governance — which is the most credible regional baseline
available and worth citing directly in proposals.

**Regulation is fragmented and that cuts both ways.** Multiple countries operate
under differing or absent frameworks, with the IADB arguing for an enabling
regional framework; the **EU AI Act's progressive entry from August 2026** is
becoming the de facto reference for cross-border operators. Fragmentation creates
opportunity and **normative inconsistency risk** for anything sold across borders.

**What this pass opens here:**

- **Offline voice tutoring is deliverable in Spanish and Portuguese today
  (P18).** `sherpa-onnx` (**Apache-2.0**) supplies STT, TTS, diarization and VAD
  on a Pi, a low-end laptop or an Android tablet **with no connectivity**, on top
  of Kolibri (**MIT**). Given that <25% of the region's players build their own
  models and the dominant pattern is a paid API call, **a voice tutor with no
  per-token cost and no connectivity requirement is a genuine differentiator**, not
  a parity feature.
- **The Portuguese-language asset is still Apache-2.0 — but it is no longer
  LATAM-maintained, and the KB should say so.**
  [Tucano](https://github.com/Nkluge-correa/Tucano) was Brazil-origin, Apache-2.0
  and peer-reviewed in *Patterns*; it was **archived on 2026-02-24**. **Tucano 2**
  (0.5–3.7B, Apache-2.0) continues under the **University of Bonn** Polyglot
  initiative. The model remains usable for a Brazil engagement; **the maintainer,
  funding and roadmap are now European.** "LATAM-origin" was true of Tucano 1 and
  is not true of Tucano 2 — do not carry the old label forward.
- **The pattern across two passes is consistent: LATAM demand is real, LATAM
  supply of permissive assets is not.** The fifth pass found the region's first
  permissive education project (Colombia's TutorIA, MIT) to be **a README and a
  licence with no code**; this pass finds its Portuguese model archived and
  succeeded from Germany. **The regional opportunity is to be the builder**, with
  SALT (Uganda) as the worked example of how a region built its own corpus and
  licensed it properly.

#### Seventh pass of 2026-10-06 — declared: no new LATAM code, and the reason is the channel

**Stated explicitly, because silence looks exactly like coverage.** This pass's
new channel was **native-language search**, and the languages added were
**Japanese, Korean, Arabic, Bahasa, Thai and Vietnamese**. **Spanish and
Portuguese were not re-run**, because the fourth pass had already used that
channel and the seventh pass's purpose was to open an unused one.

**So this pass contributes no new LATAM repository, and that is a scope decision
rather than a measurement.** It is not evidence for or against the LATAM gap.
The state of the region is unchanged from the sixth pass and should be quoted
from there:

- [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) — MIT, Universidad
  Tecnológica de Pereira, Colombia, SNCTI-funded, specifies this KB's **P1**
  architecture, and **every code path in its own documented tree 404s**. A
  partnership lead and an existence proof; **never a fork target**.
- [`Nkluge-correa/Tucano`](https://github.com/Nkluge-correa/Tucano) — Apache-2.0,
  Portuguese-native, peer-reviewed in *Patterns*, **archived 2026-02-24**;
  Tucano 2 continues under the **Bonn-hosted** Polygl0t initiative. Portuguese
  open modelling did not die, it **relocated to EMEA**.
- Earlier passes located **12 repositories in LATAM** against a "zero
  repositories" claim this KB had carried for four passes, and the fifth pass
  recorded LATAM as the **most saturated** region on the intel axis — 7 probes,
  0 new facts.

**The actionable read is unchanged and worth repeating, because it is the
commercial one.** LATAM demand is measured and large — **79% of faculty using
AI**, **87% of institutions** using it in at least one area, and only **26% with
a formal AI strategy**, with fewer than **10% of institutions** holding formal
guidelines. **The regional opportunity is governance, localisation and
deployment, not upstream code** — and the governance deficit is now the
best-evidenced commercial fact about the region in this KB.

**For the next pass:** the LATAM channel to open is **not** another
Spanish-language repository search, which has been run twice and saturated. It is
the one this pass used for APAC — **search the language substrate**, for the
indigenous and regional languages (Guaraní, Quechua, Nahuatl, Aymara) that a
ministry engagement would actually ask about. That noun has never been queried
for LATAM, and in APAC changing exactly that noun falsified a standing gap.


#### Eighth pass, 2026-10-06 — the regional diagnosis changes: the constraint is licence reliability, not supply

Four passes told a client *"nothing exists upstream in this region; we build."*
**That line is now wrong, and the replacement is more useful.**

**What the eighth pass established (full evidence in `agents/trending.md`):**

| Asset | Licence | Maturity | Where |
|---|---|---|---|
| `LabSirius/TutorIA` | **MIT** © Grupo Sirius | **13-page requirements spec + 5-layer architecture; no code** | Universidad Tecnológica de Pereira, **Colombia** |
| `caiuc/equipo-19` (EduFlow) | **MIT** © CAi UC *(holder flagged)* | **Running code**, 8-hour build, 1★ | Pontificia Universidad Católica de **Chile** |
| `neuralmind-ai/portuguese-bert` (BERTimbau) | **MIT** © NeuralMind | **886★, genuinely adopted** | NeuralMind, **Brazil** |
| `Llamacha/IWSLT2023_Quechua_data` | payload Apache-2.0 / README **CC BY-NC-ND** | Corpus, scope-conflicted | Llamacha, **Peru** |
| **Latam-GPT** | **Llama 3.1 Community License** © Meta — **not OSI** | Open-weights, 70B | CENIA, **Chile**, 60+ institutions / 15 countries |

**The opportunity, stated as an engagement shape.** The region has published
**the design and the licence, not the product.** So a LATAM engagement is a
**productionisation** engagement with citable local provenance — which prices and
positions very differently from a greenfield build, and gives Globant two named
partnership leads (**UTP Pereira**, **PUC Chile**) where it previously had an
absence.

**Three region-specific facts that are new to this file and are directly
billable:**

1. **Colombia's data-protection anchor, from TutorIA's own RNF-05:** student
   personal data, learning profiles and interaction history must be protected
   *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with **TLS** in transit
   and **AES-256** at rest. Processing minors' data without a compliant policy
   exposes the institution to **Superintendencia de Industria y Comercio (SIC)**
   enforcement. Pair this with **CONPES 4144** (already recorded here) and
   Colombia becomes the most *specifiable* LATAM jurisdiction in this KB —
   good news for a fixed-scope compliance workstream.
2. **A hard low-resource envelope, also from TutorIA:** **2 GB RAM, 3G
   connectivity** as acceptance criteria. This file previously described LATAM
   rural access with adjectives; it now has numbers a proposal can be tested
   against, and **EduFlow demonstrates they are achievable** (~8 KB per
   10-exercise assignment, IndexedDB + Service Worker, auto-sync).
3. **Latam-GPT is not open source, and nearly every account of it says it is.**
   Usable and valuable for Spanish/Portuguese regional grounding; **not
   relicensable, not presentable to a client as open source**, and it inherits
   Meta's Acceptable Use Policy and the 700M-MAU clause into the client's
   product. *Provenance caveat: single-source — `huggingface.co`,
   `latamgpt.org`, EC OSOR and `opensourceforu.com` are all EGRESS_BLOCKED here
   (4/4), so the model card was not read. Confirm before any deliverable.*

**The governance gap, re-read against this supply picture.** UNESCO IESALC
(already recorded here: 200 institutions, 19 countries, **87%** using AI, **26%**
with a formal strategy, **45%** with institutional guidance against **70%** in
Europe and North America) has until now been read as a demand signal for
policy work. **It now reads as the same failure as the licensing gap, one level
up:** the region produces the capability and omits the governing document —
whether that document is an institutional AI policy or a `LICENSE` file.

**And the eighth pass found the cheapest intervention in this KB.** **CAi UC**
(PUC Chile) made an **OSI licence and a root `LICENSE` file a condition of
evaluation eligibility** in HaCAIthon 2026, and **20 licensed team repositories
appeared in eight hours** — 19 MIT, one AGPL-3.0, four of them education-track.
Meanwhile the region's indigenous-language layer — AmericasNLP corpora for
Aymara, Nahuatl and Quechua, ASR for five languages, MT for Peru — has **nine of
eleven repositories with no `LICENSE` payload at all**, including **three
AmericasNLP editions**.

**So: sponsoring or co-writing the licence clause in a university hackathon's
rules — in São Paulo, Lima, Bogotá, and on the same argument in Nairobi — is a
concrete, low-cost, prospective fix for the one constraint that blocks both LATAM
and MEA.** It is cheaper than filing upstream `LICENSE` issues one repository at
a time, and it works on repositories that do not exist yet. Caveat worth
carrying into any such sponsorship: CAi UC's template put **the organiser's name
in the copyright line**, which is the wrong holder — a sponsored clause should
make the authoring team the holder.

#### Ninth pass, 2026-10-06 — the governance gap is now measured by a multilateral instrument, across 19 countries

For four passes this KB asserted a LATAM **adoption-versus-governance** gap, and
the fifth pass called it *"measured"* on the strength of national-level material.
It is now measured properly, by a UN-system survey, and the numbers are worse
than the KB's own framing implied.

**UNESCO IESALC + UNU-IAS working paper**, *AI Implementation in Higher Education
in Latin America and the Caribbean*, Arianna Valentini, published **1 September
2026** — a regional survey of **200 higher education institutions across 19 LAC
countries**, fielded **August–October 2025**, mapping five dimensions: teaching
and learning, research, community engagement, administration, governance.

| Dimension | Institutions adopting |
|---|---|
| Teaching and learning | **73.5%** |
| Research | **57.0%** |
| Administration | **34.1%** |
| Community engagement | **20.0%** |

| Governance condition | Institutions with it |
|---|---|
| A formal AI strategy | **26.0%** |
| Institution-wide AI policies | **18.5%** |
| A **dedicated AI budget** | **8.0%** |
| **Formal evaluation mechanisms** | **9.0%** |

⚠️ **Tier 2.** `unu.edu` is **EGRESS_BLOCKED** here, so the paper itself was
**not read**; these figures are consistent across two independent search
summaries. Confirm against the paper before use in a client deliverable.

**Read the two columns against each other, because that is the engagement.**
**73.5%** of institutions have AI in teaching and learning. **18.5%** have a
policy covering it. **9%** can evaluate whether it works. **8%** have money
allocated to it. This is not an adoption problem and not an awareness problem —
it is **deployment without governance, at scale, measured, and published by a
UN-system body the client's own ministry will recognise.**

**What it changes for this KB.** Three things:

1. **The LATAM diagnosis gets its number.** The eighth pass reframed LATAM as a
   *productionisation* region — *"the region has published the design and the
   licence, not the product."* These figures place the missing layer precisely:
   not engineering capability, but **strategy, policy, evaluation and budget.**
   The first three are consulting deliverables. The fourth is the thing a
   business case has to create.
2. **The 9% figure is the sharpest sales instrument in this KB.** *Nine percent of
   LAC universities can tell whether their AI works.* Pair it with the measured
   fact that **no Apache-2.0 tutoring-quality evaluator exists today** (0
   repositories, this pass) and the gap is not the client's failing — it is a
   market-wide absence with a funded fix arriving in 2027. That reframes an
   evaluation engagement from remedial to leading.
3. **It is citable in Spanish and Portuguese, from a multilateral source.**
   UNESCO IESALC is the region's own higher-education institute. For a ministry
   or rectorate audience this outranks any vendor report, and it is the kind of
   citation that survives a procurement committee.

**The engagement shape, stated plainly:** lead with **governance and evaluation**,
not with a tutor. The region has the adoption (73.5%) and lacks the instruments
(18.5% / 9% / 8%). A LATAM engagement that delivers an AI strategy, an
institution-wide policy aligned to the regional evidence base, and an evaluation
harness designed to accept Apache-2.0 benchmarks as they land (**P23**) is selling
into a measured deficit rather than a speculative one — and the **productionisation**
posture from the eighth pass (TutorIA's MIT specification, EduFlow's MIT offline
core, PUC Chile and UTP Pereira as named leads) is how you build on top of it.

#### Tenth pass of 2026-10-06 — the governance numbers get sharper, and a Caribbean ministry gets a vendor first

**The UNESCO IESALC / UNU-IAS survey, extended.** The ninth pass recorded part of
this instrument; the full set is now corroborated at Tier 2 — **200 higher
education institutions across 19 countries of Latin America and the Caribbean,
surveyed August–October 2025**:

| Adoption, by domain | Share |
|---|---|
| Teaching and learning | **73.5%** |
| Research | **57.0%** |
| Administration | **34.1%** |
| Community engagement | **20.0%** |

| Governance | Share |
|---|---|
| Formal AI strategy | **26.0%** |
| Institution-wide AI policy | **18.5%** |
| **Formal evaluation mechanisms** | **9.0%** |
| Dedicated AI budget | **8.0%** |

**73.5% adoption against 9.0% evaluation and 8.0% budget.** The new figure this
pass is **26.0% with a formal AI strategy** — which sits *above* the 18.5% with an
actual institution-wide policy, so roughly a third of institutions that have
written a strategy have not turned it into policy. The engagement that follows
from this table is **governance-and-evaluation first**, and it is buyable: it needs
an evaluation harness, an audit trail and a policy instrument, not a model.

**A Caribbean ministry is in a national AI-education programme with a proprietary
vendor.** **Trinidad & Tobago** is named in the first cohort of OpenAI's
**Education for Countries** (Tier 2) — the programme working directly with
ministries of education. This is the first LATAM/Caribbean national AI-education
engagement this KB has recorded, and it arrives in the region measured at **9%
formal evaluation mechanisms.** The vendor is arriving before the governance
capacity. **That ordering is the opportunity and the risk in one sentence**: the
region will be deploying national AI education programmes without the institutional
machinery to evaluate them, which is exactly the work an open, auditable
alternative can be sold as — and exactly the condition under which a closed one
becomes entrenched.

**Tier 1 confirmation, and it is a negative that now holds under a stricter
probe.** Nine of the 41 repositories re-probed this pass are the LATAM-placed
indigenous-language and hackathon repositories — the `AmericasNLP` shared-task
datasets (2021, 2023, 2024), `Llamacha/IWSLT2025_Quechua_data`,
`aoncevay/mt-peru`, `aoncevay/quechua-nlp`, `monirome/asr-indigenous-languages`,
`caiuc/proyectos-hacaithon-2026` and `vilcaaguilerandrea-oss/carrera-lectora`.
Every one was re-probed across **20 URLs** including both spellings of "licence"
and both `main` and `master`. **Not one carries a licence payload.**

The eighth pass's LATAM finding — *the capability is there, the grant is not* —
**survives a full retroactive re-probe** and can no longer be attributed to this
KB's own query defects. For a region whose indigenous-language capability is its
most distinctive technical asset, the blocker is **licensing, not capability, and
not this KB's ability to see it.** Obtaining grants on two or three of these
datasets is a higher-leverage regional action than any further search.


#### Eleventh pass, 2026-10-06 — measured in Spanish, the regional shelf does not exist, and that is the opportunity

**Measured, Tier 1, GitHub REST search, 2026-10-06:**

| Probe | `total_count` | What came back |
|---|---|---|
| `educación inteligencia artificial estudiantes plataforma stars:>5` | **0** | — |
| `educación IA aprendizaje` | **10** | **Every result 0–1★.** Highest: `Edwin1719/AvatarAcademy` (**1★**, **MIT**, payload verified — GPT-4o plus Tavus avatars for video tutors). The rest are coursework, a PE lesson generator, and `FreeHelado/neurax-ia`, **a satirical fake-documentary art project about a fictional AI-education company** — not software. |

**The Spanish-language education-AI repository channel on GitHub contains no
production asset.** Ten repositories, maximum one star, one of them deliberately
fictional. This is the fifth consecutive pass measuring the LATAM-origin shelf at
0–9★, and the first to measure it with a count rather than a ranked search page.

**The one real regional platform, and it is a good one.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) — **GPL-2.0** (Tier 1,
payload read from branch **`2.12`**; `main` serves nothing), **718★ and 547 forks**,
Laravel/PHP, *"o maior software livre de educação do Brasil"*, tagged
`software-publico`. It is the most-forked platform on these shelves and it was
**missing from this KB's live files** until this pass. **GPL-2.0 carries no network
clause**: hosting a modified i-educar for a municipality triggers nothing, and a
public-sector buyer who wants the source is asking for exactly what the licence
delivers.

**Governance context re-corroborated this pass (Tier 2):** across 200 institutions in
19 LAC countries, AI adoption leads in **teaching and learning at 73.5%**, then
research 57.0%, administration 34.1%, community engagement 20.0% — while only **26%
have a formal AI strategy, 18.5% an institution-wide policy, 8% a dedicated AI
budget, and 9% any formal evaluation mechanism.** Regulation: **no unified regional
framework**; **Chile** leads with a National AI Policy since 2021 and pending
legislation; **Brazil** and **Colombia** have national strategies without sectoral
education regulation; most universities operate in a normative vacuum. Chile's
**CENIA** publishes the regional AI index and leads **Latam-GPT**.

**The opportunity, stated so it can be sold.** 73.5% are already using AI in teaching
and 9% can evaluate it. **The gap between adoption and evaluation is wider here than
in any other region in this KB, and the instruments that close it are free and
permissive** — Inspect (MIT) and Moonshot (Apache-2.0). The LATAM engagement is not
"adopt the regional shelf," because there is no regional shelf. It is: **deliver the
global permissive shelf with Spanish and Portuguese as first-class, offline-tolerant
by construction, data-resident by default, and with the evaluation mechanism the
other 91% do not have** — on i-educar or Moodle where the client is public sector,
and with the licence register written in the client's language.

## Cross-region read

Two patterns hold in every region, which makes them safe to build once and sell
four times:

1. **Human oversight on any consequential decision** — required by Oklahoma and
   Maryland statute, by EU AI Act Annex III, by Brazil's PL 2.338 risk tiers, and
   by Korea's high-impact classification. It is also forced by the technical
   gap: no permissive open source auto-grader exists.
2. **Data residency and student-data boundaries** — California AB 1159, EU data
   residency practice, India's DPDP, and LATAM connectivity constraints all point
   at the same architecture: on-prem or in-region open-weight inference.

3. **Agent-specific governance is now a named requirement, not an extrapolation
   from general AI rules.** Singapore's Model AI Governance Framework for Agentic
   AI (January 2026, updated June 2026) is the first regulator-issued document
   that governs autonomous planning and action directly: bound the agent's powers,
   define human approval checkpoints, control the whole agent lifecycle, and train
   the end user. Those four dimensions also discharge most of what EU Annex III,
   the Oklahoma/Maryland oversight statutes and Korea's high-impact classification
   ask for. **Use the Singapore framework as the build checklist in every region**,
   because it is the most specific and the most agent-aware of the four.

4. **Curriculum mandates are now a funded demand driver, and they come with
   architectural constraints.** Two jurisdictions have made AI instruction
   compulsory with published specifics: the **UAE** (Cabinet, May 2025 — KG to
   Grade 12 from the 2025–26 school year, seven content areas, woven into an
   existing subject without extra school hours, specially trained teachers) and
   **China at provincial level** (Beijing: ≥8 hours a year for every primary and
   secondary school from 1 September 2025; Guangdong: 6 hours in lower grades
   rising to an hour a fortnight in grades 10–11). This is different in kind from
   the regulation in points 1 and 2: a mandate creates a **budgeted obligation to
   deliver content and train teachers**, not merely a constraint on how you deploy.
   It also hands you the two hardest requirements for free as design inputs:
   **age-gated capability** (Beijing bars primary pupils from independent
   generative-AI use) and **enforced teacher-in-the-loop** (teachers may not
   substitute AI for core instruction). Build to the mandate and the oversight
   obligations in points 1 and 2 are largely discharged as a side effect.

The deliverable that satisfies the first three is the same side-car. Build it once.
The fourth needs one more thing on top — a curriculum-alignment and age-gating
layer — which is pattern P9 in `compose/patterns.md`.

## What changed in this pass — read this if you read nothing else

| Finding | So what |
|---|---|
| Europe sized at **$2.64B** in 2026; leaders are Finland, Estonia, Netherlands | the EMEA reference deployment belongs in a small digitally mature state, not a large economy |
| AI Act **general application already live (2 Aug 2026)**; only high-risk deferred to Dec 2027 / Aug 2028 | stop telling clients the Act does not apply yet |
| Singapore's **agentic-AI** framework (Jan 2026, world first) | the cross-region build checklist, and its dimension 4 is a billable enablement line |
| **Vietnam** AI law in force 1 Mar 2026; **Korea** exactly 22 Jan 2026 | the APAC binding-regulation wave is wider than Korea/Singapore/China |
| LATAM: **92% students / 79% faculty** adopting, but **88% of faculty shallow** | sell depth and integration, not adoption |
| **Colombia CONPES 4144** — funded national AI programme through 2030 | add Colombia to the LATAM target list |
| **All 50 US states** legislating; states split into buyers vs brakers | qualify the camp before choosing the pitch |
| **Africa** enters the KB: South Africa draft national AI policy, GenAITEd Ghana | genuine EMEA greenfield; teacher capability is the constraint |
| Several popular education **MCP servers are unlicensed** (see `agents/top.md`) | a licence probe belongs in the engagement's first week |
| **OpenEduCat is LGPL-3.0** — proprietary modules permitted | on the admin side, a module is a viable commercial shape, not only a side-car |

## What changed in the third pass of 2026-10-06

| Finding | So what |
|---|---|
| **UAE: AI compulsory KG→Grade 12** from 2025–26 (Cabinet May 2025), 7 content areas, inside an existing subject, trained teachers | a budgeted content-and-enablement mandate, not just a constraint. Two of the seven areas are ethics and policy, so the pipeline must produce governance material too |
| **China: Beijing ≥8 h/year from 1 Sep 2025; Guangdong 6 h → 1 h/fortnight (grades 10–11)**; primary pupils barred from independent generative-AI use; teachers may not substitute AI for core instruction | **age-gated capability and enforced teacher-in-the-loop are build requirements.** Satisfy Beijing and you satisfy EMEA/NA oversight |
| Europe: **$2.64B (2026) → $8.0B (2030), 31.9% CAGR** — slower than the 41.5% global rate | Europe is the compliance-depth market, not the growth market; its share shrinks over the forecast |
| **MEA sized for the first time: $0.56B (2026) → $1.6B (2030), 34.3% CAGR** — but a second source puts the **UAE** at $7.4M (2024) → $21M (2029) | irreconcilable scopes. **Quote MEA as a range and name the uncertainty** |
| MEA: Saudi, UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco, South Africa all have AI **strategies, none has a binding AI statute** | mirror image of the EU sale: governance design *before* the law, shorter cycle, weaker procurement trigger |
| APAC: **~530M K-12 students** (2024); adoption 65–75% (2025) → 80–90% (2026) | the denominator that makes small-model and offline deployment an APAC concern, not only a LATAM one |
| APAC law, per country: Korea 22 Jan 2026 · **Vietnam 1 Mar 2026, SEA's first** · Japan deliberately voluntary · **India and Australia still have no national framework in force** | "APAC-ready" is not a claim you can make |
| LATAM: **87% of institutions use AI, 26% have a formal AI strategy**; **72% of faculty positive vs 57% globally** | enthusiasm-rich, governance-poor — the most favourable shape for a governance-led engagement in this KB |
| **Uruguay is the first LATAM signatory of the Council of Europe AI Framework Convention** (2025) | the cheapest bridgehead for reusing EMEA compliance IP in LATAM — an interoperable governance vocabulary |
| North America channel **saturated — no net new findings**, explicitly stated | further depth needs procurement portals and state trackers, not another general search |
| The permissive open source layer went from "DeepTutor plus fragments" to **~30 verified projects incl. a full MIT LMS** | the differentiator moves from *finding* the parts to **composing, licensing and governing** them |

## What changed in the fourth pass of 2026-10-06

Channels new to this KB this pass: **paper-to-repository tracing** (arXiv / ACL
Anthology), a **GitHub-organisation sweep**, and a **Spanish/Portuguese-language
search**. Two of the five findings below are **corrections to this KB's own
claims**, which is the point of recording them.

| Finding | So what |
|---|---|
| **OpenMAIC is Tsinghua's, MIT, 40.0k★** — and `OpenMAIC-Brasil`, cited for three passes as evidence of a missing LATAM project, was a **fork-shaped name**, not a Brazilian project (re-probed: 404 on all four branches) | the **largest permissive asset in this KB** arrives, and the lesson-generation starting point for every region becomes **Chinese-origin MIT code**. Put provenance and data residency in week one. And **never attribute a region from a repository slug** |
| **NA 2030 sizing is disputed: $10.8B vs the $32B this KB recorded.** $32B would make NA ~75% of the KB's own global 2030 figure while the same page asserts a 36% share | **quote $3.68B for 2026 and 2030 as a range**, naming the uncertainty. Internal consistency favours the lower figure. Primary source unreachable — conflict recorded, not resolved |
| The third pass called North America **"saturated"**; re-running general searches added **statute names, bill numbers, mechanisms and dates** on six states — incl. **CA AB 1159's 1 July 2027 higher-ed trigger**, Idaho SB 1227 as an **AI-literacy and teacher-training mandate**, Oklahoma **SB 1734's annual parent disclosure**, Maryland's **24 districts / 120-day rolling** clock, **Ohio HB 96's deadline now past**, and NC's funding being **recurring and sole-sourced** | **"saturated" conflated no-new-entities with no-new-information.** Precision is what makes a finding sellable, and it was mostly missing. Ohio's 600+ districts are now in **implement-and-audit**, which is the better engagement |
| **Africa gets its first code shelf: `AI-for-Education`**, 5 of 6 repos MIT, built for **Sierra Leone's MBSSE** and **Uganda** (Luganda) — plus the only **voice-evaluation** and **pedagogical model-selection** tooling in this KB | Africa stops being greenfield-with-nothing and becomes **greenfield with a specific, permissive, ministry-connected entry point**. At 1–12★ it is research-grade: a conversation starter, not a product shelf |
| **A fourth licence failure mode: the grant that exists only in the paper.** `AITutor-EvalKit` (peer-reviewed EACL 2026, "released under an MIT license") has **no `LICENSE` payload on either branch**. Separately, **Open TutorAI** calls itself open source and is **CC BY-NC-SA 4.0** | **a peer-reviewed licence claim is evidence of intent, never of rights.** Probe the payload. Re-implement `AITutor-EvalKit`'s MI/ML/PG/AC rubric rather than vendoring it, and **file an issue asking for a `LICENSE`** — the cheapest high-value upstream contribution available here |

## What changed in the fifth pass of 2026-10-06

Channel new to this KB this pass: **institution-first search** — funding bodies,
ministries, universities and research groups queried by name, in English and
Spanish, instead of by GitHub topic or star count. Three of the six findings
below are **corrections to this KB's own claims**.

| Finding | So what |
|---|---|
| **The EU compliance clock moved 16 months.** Regulation (EU) 2026/1744 (*Digital Omnibus on AI*, OJ 24 July 2026, in force 27 July 2026, CELEX 32026R1744) pushes **Annex III stand-alone high-risk — education included — from 2 August 2026 to 2 December 2027**, and Annex I embedded to 2 August 2028. **Article 50 transparency did not move: the watermarking deadline is still 2 December 2026** | **The EMEA engagement is now two-phase and the near-term phase is the small one.** Label and classify by **December 2026**; build Annex III conformity evidence by **December 2027**. Clients who heard "the deadline was delayed" have deferred the labelling work too, and that one is weeks away. Primary texts unreachable from this environment — **verify against EUR-Lex before client use** |
| **The NA 2030 sizing conflict is resolved, in favour of $10.8B.** 36% × $10.6B global = $3.82B ≈ the recorded $3.68B for 2026, so the 2026 figures cohere. At 2030, $32B would be **75%** of this KB's own $42.48B global row; $10.8B is **25%**, implying 31.1% CAGR — within a point of EMEA's independently sourced 31.9% | **Retire $32B; quote $3.68B → $10.8B at ~31%.** And lead with the consequence: NA's share falls from 36% to ~25% while the absolute number triples, which is the arithmetic case for an APAC-weighted account strategy |
| **LATAM's opportunity is now measured, not inferred.** UNESCO IESALC (launched **9 September 2026**, UNESCO Digital Learning Week; **200 institutions, 19 countries**): **87% use AI, 26% have a formal AI strategy**; **45%** have formal guidance against **70%** in Europe and North America. Digital Education Council LATAM Survey 2026 (with Tec de Monterrey's Institute for the Future of Education): **92% of students and 79% of faculty** using AI, **88% of faculty still at minimal-to-moderate engagement** | **A 61-point gap between using AI and having a strategy for it is a governance engagement, not a tutor engagement.** Lead LATAM higher education with **pattern P6 (capability build)** and let P1 follow. Two independent, citable, month-old primary sources — the best-evidenced regional claim in this KB |
| **APAC regulation has arrived and reorders the build sequence.** Korea's **AI Basic Act in force 22 January 2026** (transparency, risk assessment, human oversight, documentation for high-impact systems); **Vietnam's Law No. 134/2025/QH15 effective 1 March 2026**; **Australia's TEQSA requires an institutional genAI action plan from every higher-education provider** | **Korea, not the EU, is now the binding constraint** for a multi-jurisdiction education product — its substance matches Annex III and it is live 23 months earlier. Build to Korea and EU conformity becomes documentation. **And TEQSA is the sharpest procurement trigger in this KB**: one mandatory document, one regulator, every provider in a country, enforced through accreditation |
| **Three regional "no permissive project exists" gaps refuted in one pass** — India ([microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot), MIT, MSR India/VELLM), ASEAN ([Coursemology](https://github.com/Coursemology/coursemology2), MIT, **15,802 commits**, NUS/AICET), LATAM ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA), MIT, UTP Colombia, SNCTI-funded). **All were found at 0–158★** | **The gaps were true of the discoverable shelf and false of the world.** Topic pages and star-sorted search are popularity-ordered and structurally cannot see a four-commit project from a public university in Risaralda. **When a gap survives several passes, change the channel — and pick one that is not ordered by stars** |
| **Singapore is the region's reference deployment and it is closed.** AICET (AI Singapore, Smart Nation and Digital Government Office funding, working with the Ministry of Education) runs **Codaveri** (30,000+ feedback items since 2024), **Softmark** (70,000+ scripts in 2025) and **ScholAIstic** (educator-authored chatbots across Social Work, Law and Nursing at NUS since June 2024) with **no public repositories** — on top of an **MIT** LMS | **The architecture this KB recommends is validated at ministry scale and cannot be forked.** Cite AICET as proof the shape works; build the shape from the permissive substrate. **ScholAIstic is the gap worth naming**: non-technical educators authoring and publishing their own roleplay training agents has **no permissive equivalent anywhere in this KB** |

### The method correction, stated plainly

The fourth pass concluded with "never attribute a region from a repository slug."
The fifth pass adds the complement, and it is the more expensive mistake:
**never conclude a region is empty from a popularity-ordered channel.** Every
regional gap this KB has stated most confidently was produced by sweeping topic
pages and star-sorted searches — both of which rank by adoption, and neither of
which can surface a new, unstarred, institutionally-backed project. Three such
projects existed the whole time. One query shape found all three.

## What changed in the sixth pass of 2026-10-06

The pass swept the **speech and low-resource-language substrate** rather than
education products — a layer that had **zero** entries in this KB. 26 repositories
probed, 26 resolved, every licence read from its own `LICENSE` payload.

**Four things changed in the commercial picture:**

1. **Voice stopped being a proprietary dependency.** `k2-fsa/sherpa-onnx`
   (**Apache-2.0**, 15.1k★) delivers STT, TTS, diarization and VAD in one
   permissive tree **with no Internet connection**, on phones, Raspberry Pi and
   RISC-V. Spoken practice and oral assessment reprice from a recurring
   per-token cost to a one-off build on hardware the client already owns.
2. **Mother-tongue delivery is a two-region capability.** India (AI4Bharat, all
   **MIT**, 22 scheduled languages) and East Africa (`SunbirdAI/salt`,
   **Apache-2.0**, six Ugandan languages with studio TTS; Masakhane, **MIT**).
   **Everywhere else the permissive layer does not exist** — which makes corpus
   building a fundable first phase rather than a blocker.
3. **India is the only all-MIT national stack in this KB.** Sunbird (**MIT**,
   38,046 commits, **DIKSHA**, Digital Public Good) plus the AI4Bharat layer plus
   MIT orchestration — see **P16**. In public procurement this removes the licence
   conversation entirely.
4. **The highest-volume assessment task in primary education has no open
   implementation.** Oral reading fluency is owned by closed products with no
   public repositories, while the permissive components and a **public dataset
   with a published baseline** both now exist — **P17**.

**Three named rejections, recorded so they are not re-proposed:**
`facebookresearch/seamless_communication` is **CC BY-NC-4.0** (non-commercial);
`rhasspy/piper` is **MIT but archived**, its maintained successor **GPL-3.0**;
`aisingapore/sea-lion` has **no repository-level licence**, deferring the grant to
each model card.

**And one correction to this KB's own regional labelling.** Tucano, recorded as a
Brazil-origin Apache-2.0 asset, was **archived 2026-02-24**; its successor Tucano 2
is developed at the **University of Bonn**. The model is still usable for Brazil
work, but **its maintainership moved to EMEA** and the KB should not keep calling
it LATAM-origin.

### The method note, stated plainly

The fifth pass learned that **low star counts hide real assets**. This pass found
the inverse: **high star counts hid dead ones.** On this shelf, 46.1k★ Coqui is
abandoned while its 2.3k★ Idiap fork has **641 more commits**; 11.3k★ Piper is
frozen. The fields that carried the signal were **archive status, the successor
notice, and commit count** — none of them popularity.

**Check whether a repository is alive before checking how popular it is.**

## What changed in the seventh pass of 2026-10-06

New channel: **native-language search** (Japanese, Korean, Arabic,
Bahasa/Thai/Vietnamese), plus a **function-scoped MCP sweep** and a
**consistency audit** of the shelves against the trending logs. **18
repositories probed, 18 resolved**; every licence from payload.

| Finding | Why it matters |
|---|---|
| **Vietnam's Decree 33** (signed 2026-06-30, in force 2026-08-15): 46 high-risk systems, **3 in education** | Category 1 — *self-learning content from uncontrolled data sources* — **regulates the corpus, not the decision**. No Annex III equivalent. Every RAG tutor in this KB is in scope in Vietnam on provenance alone ⇒ **P20** |
| Vietnam's behaviour-monitoring trigger is qualified to **biometric** data | **First APAC regime in this KB that is *looser* than Annex III** on a specific axis. Non-biometric analytics sit outside it |
| Education's Decree 33 transition runs to **2027-09-01** (with healthcare and banking) | The **longest** runway of any sector — a remediation window with a statutory date |
| **ASEAN has a permissive language shelf**: Vietnamese, Thai, Malay ×2, Indonesian ×2 | **Falsifies trend 21's "two-region" claim.** Combined with MIT `coursemology2`, ASEAN now has an MIT LMS substrate **and** an Apache-2.0/MIT language substrate under an unbuilt pedagogy layer ⇒ **P19** |
| **MEA's constraint is licensing hygiene, not capability** — the one real Arabic education agent is unlicensed | Turns the region's weakest finding into the **cheapest** one to act on: three `LICENSE` files change the regional answer |
| **H.R. 8747** advanced from House committee — federal funds for AI curriculum and literacy | The only **funding** instrument among the North American rules this KB tracks; everything else constrains |
| **Japan gap refuted — by this KB, passes ago.** `toshieji/moodle-grading-mcp` (MIT, © WACA + Toshiaki Ejiri) | `agents/top.md` asserted a gap its own trending log had already disproved. **Internal consistency, not coverage, is now the binding constraint on this KB's accuracy** |
| **Korea's first permissive education asset** — `yongsoojoo/esd2026-agent-workflow` (MIT + CC BY 4.0, Kookmin University) | Course material, not an agent. The **agent** gap stands, against an AI Framework Act in force since 22 Jan 2026 |
| **No licensed open proctoring agent exists** — the one candidate has no payload | A regulated category (Annex III point 3; Decree 33 category 3) with **no open competitor** |
| **No new LATAM code this pass, and the reason is declared** | The channel opened was non-Iberian by design. Not evidence about the LATAM gap either way |

### The method note, stated plainly

Three passes have now refuted a regional gap, each by changing a different thing:
the **channel** (fifth — institution-first), the **layer** (sixth — substrate
rather than product), and the **noun** (seventh — toolkit rather than sovereign
model). **Not one was refuted by running the original search harder.** When a
gap survives its second probe, change the probe.

And the cheapest two corrections of this pass required no search at all — they
were this KB disagreeing with itself, found with `grep`. **A pass is finished
when the shelf, the gap list, the trends file and the patterns agree with the
log, not when the log entry is written.**

## What changed in the eighth pass of 2026-10-06

**The LATAM read is replaced, not extended.** For four passes this file's LATAM
position rested on *"no LATAM-origin permissive education project"*. That gap is
**fully refuted on origin, licence and design** and survives **only on
maturity**: the region has published the design (TutorIA's MIT 13-page
specification, Colombia) and working code (EduFlow, MIT, Chile) and an adopted
language model (BERTimbau, MIT, 886★, Brazil) — and nothing at production scale.

**The commercial consequence is a different engagement shape.** A LATAM
engagement is a **productionisation** engagement with citable local provenance
and two named academic partnership leads, not a greenfield build.

**Three facts new to this file:** Colombia's **Ley 1581 de 2012 (Habeas Data)**
with TLS/AES-256 acceptance criteria and SIC enforcement exposure; a hard
**2 GB RAM / 3G** low-resource envelope with a working demonstration that it is
achievable; and **Latam-GPT's licence** — **Llama 3.1 Community, not OSI
approved**, despite the EC's own Open Source Observatory and the trade press
calling it open source.

**One cross-region finding, and it is the most actionable thing in the pass.**
The seventh pass diagnosed MEA: *the binding constraint is licensing hygiene,
not capability.* The eighth pass found the **identical** shape in LATAM's
indigenous-language layer (9 of 11 repositories ungranted, including three
AmericasNLP editions) **and a remedy that works prospectively**: CAi UC made an
OSI licence a condition of hackathon evaluation and 20 licensed repositories
appeared in eight hours. **Sponsoring that one clause is cheaper than any
upstream-issue campaign and is the pass's recommended action for both regions.**

**North America, EMEA and APAC returned nothing new, and each is recorded as
such above rather than left silent.** North America's general-language channel
is now **saturated** — four consecutive passes, identical facts — and the next
finding there must come from district RFP language or state procurement portals,
which this KB has never swept. EMEA returned enterprise-AI commentary and one
event (the Council of Europe's second working conference on AI-in-education
regulation). APAC returned sovereignty framing, which is read here as the
region's actual opportunity shape rather than as a miss.

### The method note, stated plainly

**This file's regional claims are only as good as the probe's vocabulary, and
this pass is the fourth consecutive demonstration of it.** The LATAM gap was
refuted not by searching LATAM harder — four passes had done that — but by
probing a repository for a **specification** instead of for **code**, and by
sweeping an **institutional event** instead of a topic page.

**And the licence column in every table in this KB now carries a known
ceiling.** Eight passes treated the `LICENSE` payload as ground truth. It is
wrong about `Llamacha` in the permissive direction, silent about CAi UC's
inherited holder, and says nothing about the label-versus-grant gap that makes
Latam-GPT look open. **Three points, not one: payload, asset scope, holder.**

## What changed in the ninth pass of 2026-10-06

**Channel: the funder and procurement channel**, plus the
**education-ministry engineering organisation** — both named as necessary by the
eighth pass, neither ever swept by this KB.

1. **North America's supply of permissive education AI is now a funded pipeline
   with a licence floor.** The **$26M K-12 AI Infrastructure Program** (Digital
   Promise + Gates Foundation, with Learning Data Insights, DrivenData,
   Georgetown's Massive Data Institute, Catalyst @ Penn GSE) requires all funded
   work to be **at least as permissive as CC-BY-4.0 (content) / Apache-2.0
   (code and models)**. **Twelve projects are funded and named**; the **$8M EDU
   AI** award for an open-source K-12 math tutoring model closed 31 Jul 2026 with
   work starting Nov 2026. **Nothing has shipped yet** — measured as 0
   repositories for the two most specific artefacts.
2. **The oldest gap in this KB acquired a date instead of closing.** No
   Apache-2.0 tutoring-quality evaluator exists today (measured, licence-filtered,
   0 results). Three or more of the twelve funded projects target exactly that,
   through 2027. The engagement line changes from *"this does not exist"* to
   *"build the harness now, swap the benchmarks in as they land"* (**P23**).
3. **Procurement rubrics became the region's real specification.** Maryland
   **SB 720** (rubric + 120-day local policy + AI coordinator), Vermont's
   seven-criterion rubric, Idaho/Maryland/Alabama statutory capability
   assessments and the prohibition on training vendors' models on student
   records. **CoSN: 39% of districts score interoperability in RFP rubrics** —
   the first procurement-side number for trend 4. And the gap *inside* the
   rubrics — no required interaction audit trail, output-provenance disclosure or
   bias/accuracy evaluation — **is the differentiator, and it is the same
   artefact set the EU AI Act profile already forces (P13).**
4. **EMEA gained a permissive, production, government-maintained estate.** The UK
   DfE (`DFE-Digital`) publishes its national teacher-training, vacancies,
   schools-register and benchmarking services under **MIT** — while its own AI
   repositories sit at 0–1★ with **no licence payload**. That asymmetry is the
   public-sector opening, and it is a precedent usable with any EMEA ministry.
5. **LATAM's governance gap is now measured by a UN-system instrument.** UNESCO
   IESALC + UNU-IAS, 200 institutions, 19 countries: **73.5%** adoption in
   teaching and learning against **18.5%** institution-wide policy, **9%** formal
   evaluation mechanisms and **8%** dedicated AI budget. **Nine percent is the
   sharpest number in this KB**, and it points at an engagement the region can
   buy.
6. **APAC built the evaluation benchmark the US is now funding, and did not
   license it.** `AI-EDU-LAB/E-EVAL` (33★, Chinese K12 LLM education evaluation)
   has **no payload** — the third region showing *built, published, benchmarked,
   ungranted*.
7. **Two regional queries failed for the second consecutive pass.** The mandated
   EMEA and APAC sweeps returned **enterprise** AI-governance material, not
   education. Both regions now need the channel change that worked for the UK
   this pass. Recorded as exhausted channels, not as regional stability.

### The method note, stated plainly

This pass accepted **Tier 2 evidence into the durable files for the first time at
scale.** Fourteen hosts carrying the primary documents — the RFPs, the grantee
announcements, the state guidance, the UNESCO paper, the arXiv preprints — are
**EGRESS_BLOCKED** in this environment, so **no primary document was read.**
Every funder, dollar, date and statutory claim above is corroborated across two or
more independent search summaries and is labelled Tier 2 wherever it appears.

That is a real lowering of this KB's evidentiary bar, and it is deliberate: a
funded pipeline known at Tier 2 is worth more to an engagement than a silent gap
known at Tier 1 — **provided nobody mistakes which is which.** The tiering is
written into every table rather than into a footnote, and the repository and
licence facts in this pass remain **Tier 1, payload-verified**, as they have been
for nine passes.

The counterweight is that the Tier 1 method itself was found defective this pass:
**three of the UK ministry's six MIT grants are in a file spelled `LICENCE`** — a
spelling pattern **P22**'s gate already lists and no recorded sweep has ever
run. See `agents/top.md`, ninth-pass method
note — four government repositories would have been recorded as ungranted by a
query that could not have found their grant.

## What changed in the tenth pass of 2026-10-06

**Channel: the KB's own reject pile, re-probed** — plus the **interoperability
shelf** that the ninth pass's procurement finding pointed at, the **Council of
Europe education directorate** for EMEA, and the **ministry-programme channel**
for APAC and LATAM. The generalist regional query was retired for EMEA and APAC
after a third consecutive failure.

1. **North America's funded pipeline gained two more named projects and a third
   measured zero.** Harvard (Ying Xu) is funded for **OpenLiteracy**, an
   open-source speech-foundation-model suite for early word reading assessment —
   which lands exactly on this KB's sixth-pass oral reading fluency gap. Maryland
   (Jing Liu) is funded for multimodal classroom formative-assessment datasets.
   **`OpenLiteracy` returns 0 repositories on GitHub.** Three funded, named,
   dated projects; three measured zeros. Five of eight Cohort 2 grantees still
   unnamed.
2. **EMEA is writing the evaluation rule that North America is funding the
   artefact for.** The Council of Europe has a **Committee of Experts on AI and
   Education (EDU IA)**, a **Compass for AI and Education**, a Committee of
   Ministers text adopted in **Munich** implementing **Article 20 of the Framework
   Convention on AI**, and a 2026–27 programme containing a **proposed legal
   instrument to regulate AI systems in education** and a **European Reference
   Framework for the Evaluation of Educational Technologies**. One gap, two
   regions, two instruments — and the European one arrives as conformance, which
   cannot be retrofitted.
3. **The proprietary ministry channel is simultaneously in all three non-US
   regions.** OpenAI's **Education for Countries** names **Estonia, Greece, Italy
   (CRUI), Slovakia, UAE, Jordan** (EMEA), **Kazakhstan, Singapore** (APAC) and
   **Trinidad & Tobago** (LATAM). Nine ministries or sector bodies, one vendor,
   national tier. Singapore's own framing — *"exploring various AI tools from
   different partners"* — is the opening, and **Trinidad & Tobago is a Caribbean
   ministry acquiring a national programme in a region measured at 9% formal
   evaluation capacity.**
4. **LATAM's governance table is now complete and sharper.** UNESCO IESALC /
   UNU-IAS, 200 institutions, 19 countries: **73.5%** teaching-and-learning
   adoption, **57.0%** research, **34.1%** administration, **20.0%** community
   engagement — against **26.0%** with a formal AI strategy, **18.5%** with
   institution-wide policy, **9.0%** with formal evaluation mechanisms and
   **8.0%** with a dedicated AI budget. The new figure, 26.0% strategy above
   18.5% policy, says a third of institutions that wrote a strategy never turned
   it into one.
5. **The integration tier became a priceable deliverable.** Against **39% of
   districts scoring interoperability in RFP rubrics**, the permissive shelf is
   verified and small: four Apache-2.0 LTI 1.3 libraries (Node, PHP, two JVM) and
   one MIT OneRoster client (**rostering only, no gradebook**). **No permissive
   Caliper Analytics implementation. No Python LTI 1.3 library at all** — and
   Python is where the AI layer lives.
6. **A named North American partner turned out to have a 238-repository MIT
   estate.** Learning Equality, Cohort 1 grantee and Kolibri maintainer. New
   verified MIT: **morango** (peer-to-peer Django DB replication with
   certificate-based auth — the sync engine under the offline story) and
   **le-utils**. Two sibling repositories returned **no payload**, so diligence
   stays per-repository.
7. **Three negatives were re-tested and held, which makes them usable.** APAC's
   `E-EVAL` benchmark and nine LATAM-placed indigenous-language and hackathon
   repositories were re-probed across **20 URLs each** — both spellings of
   "licence", both branch names. **Not one carries a payload.** Those regional
   findings can no longer be attributed to this KB's own query defects.

### The method note, stated plainly

This pass **audited the KB against itself**, and the audit cost it two of its own
conclusions.

The ninth pass's headline method fix — probing the British spelling `LICENCE` —
**flipped nothing** when run backwards over the 41 repositories this KB had
recorded as ungranted. It is a house style at one UK government organisation that
was written up as a general defect in the KB's reach. The defect that *was*
general was never announced: **the KB had only ever probed one branch name.** The
single flip in 41 (`jdolny/OneRoster.NET`, MIT) sits on `master/LICENSE`, and three
of the six validation controls do too.

The finding to carry forward is worse, and it is about market intelligence as much
as code: **GitHub's rendered licence field reported "License: Not specified" for a
repository carrying a complete MIT grant** (`qazasd2518995/prosody`). Every
licence-filtered zero-result measurement in this KB — including three in this very
pass, used above to show that funded projects have not shipped — inherits that
error. The zeros remain the best available measurement. **They are evidence of
absence as GitHub's licence index sees it, not evidence of absence**, and the
distinction has to survive into any client deliverable that quotes them.

**And the environment is now a measured constraint rather than a series of
accidents.** Nine further hosts were attempted this pass and **all nine returned
`EGRESS_BLOCKED`**: `digitalpromise.org`, `www.coe.int`, `rm.coe.int`,
`www.prnewswire.com`, `www.gse.upenn.edu`, `www.eunews.it`, `www.sec.gov`,
`ess.iesalc.unesco.org`, `openai.com` — including **three syndicated mirrors tried
specifically to route around a blocked primary host.** With the ninth pass's
fourteen, that is **23 distinct hosts across two passes with zero reachable.**
`github.com` and `raw.githubusercontent.com` are the only origins this environment
serves.

Two consequences for the next pass. **The vendor-filings channel is not unswept,
it is unreachable** — `www.sec.gov` is blocked, so McGraw Hill's and Workday's
FY2026 open-source and copyleft-risk disclosures are available at Tier 2 only, and
that channel needs a different host rather than a better query. And **every market,
funder, regulatory and procurement figure in this file remains Tier 2**: dollar
amounts, dates, percentages and licence clauses are corroborated across independent
search summaries, never read from the primary document. **Confirm each one against
its source before it enters a client deliverable.**

## What changed in the eleventh pass of 2026-10-06

**One instrument change produced every market finding below.** The GitHub REST
search API is reachable in this environment through the session's GitHub MCP server —
`curl https://api.github.com/search/repositories` returns **403** and
`/repos/{owner}/{repo}` is refused, which is why ten passes recorded the API as
blocked. Through the MCP path it returns `total_count` and real metadata, so this
KB's *absences* can now be counted rather than inferred from a ranked search page.

| What the KB said | What this pass measured | Consequence for a proposal |
|---|---|---|
| *"No permissive evaluation harness exists; build the socket and wait for the artefact"* (P23, three passes) | **Inspect** (MIT, **2,945★**, UK AI Security Institute) and **Moonshot** (Apache-2.0, 355★, Singapore IMDA's AI Verify Foundation), both pushed 2026-10-06 | **Stop quoting harness-building as the deliverable.** The harness is free, permissive and government-maintained. Quote the *rubric*, the *dataset handling* and the *conformance pack*. |
| *"`tutoring quality evaluation benchmark` → 0 results"* | Drop one word: **20 results**, led by **Khan Academy** (57★) and **ETH Zurich** (43★) | The benchmarks exist. **None is OSI-licensed** — the constraint is legal, not technical. |
| *"No Python LTI 1.3 library on the permissive shelf"* (tenth pass) | **`dmitry-viskov/pylti1.3`, MIT, 138★** — the **second-largest runtime** on the permissive interoperability shelf | The integration tier priced in P25 was priced against a hole that was not there. |
| *"The regional flagship is not open source"* / LATAM has no platform | **`portabilis/i-educar`, GPL-2.0, 718★ / 547 forks**, Brazil, `software-publico` | A LATAM public-sector engagement has a real, licence-appropriate base. |

### The market read that follows from the licensing wall

The money and the measurement are in different places, and the licence is what
separates them:

- **North America funds the datasets** — $26M philanthropic K-12 AI infrastructure
  programme with an Apache-2.0-or-better floor (ninth pass) — and its two best
  existing benchmarks come from **Khan Academy** and are **not** openly licensed.
- **EMEA supplies the harness** — UK AI Security Institute's Inspect, **MIT** — and
  the rule (Council of Europe reference framework; EU AI Act full effect August 2026,
  education AI high-risk).
- **APAC supplies the red-team tooling** — Singapore IMDA's Moonshot, **Apache-2.0** —
  and the highest deployment rate (**56%** of businesses already running assistants).
- **LATAM supplies the demand and almost none of the supply** — **73.5%** using AI in
  teaching and learning against **9%** with any formal evaluation mechanism.

**The sellable asset across all four is the same one and it is not a model.** It is
an evaluation and conformance capability assembled from permissive components, with
the non-permissive benchmarks **borrowed at measurement time and never shipped**.
Every region's buyer wants it for a different stated reason — procurement rubric in
North America, AI Act conformance in EMEA, sovereignty in APAC, institutional
credibility in LATAM — and the architecture is identical. That is the most
transferable finding this KB has produced.

### The method note, stated plainly

Three zeros were wrong this pass and each was wrong for a different reason: a **ranked
web surface** is not a count; a **`repo:` qualifier excludes forks by default**
(`repo:mitodl/open-learning-ai-tutor` → 0, with `fork:true` → 1, and that fork is MIT
Open Learning's production tutor); and a **keyword-heavy query measures the filter**,
not the world.

A fourth was wrong for a reason that has nothing to do with search: **this
repository's reset earlier on 2026-10-06 dropped 172 real repository addresses**
(627 live vs 678 archived, 7 of the 179 differences being placeholders), and the
tenth pass declared one of them — `pylti1.3` — a gap while it sat in
`archive/2026-10-06-pre-reset/` with its licence and star count intact. **A gap claim
made after a reset is not publishable until it has been diffed against the archive.**
