---
industry: education
region: Global
updated: 2026-10-21
---

# Education — market map and regional intelligence

**Pass 359 · 2026-10-21.** Researched **2026-10-21**. Figures are attributed; where a
number comes from a vendor blog or a commercial research summary rather than a primary
source, it says so. The
regional sections below are deliberately symmetric: a North America or EMEA
engagement should be as well served by this file as a LATAM one.

🔵 **`p359` ran all four prescribed regional legs and they returned no fact this file did
not already carry** — the **134 bills / 31 states**, `H.R. 8747`, the NYC moratorium,
Canada's *AI for All*, the EU AI Act's 2 Aug 2026 enforcement date and 27 Jul 2026
omnibus, the UK's £4 m programme, Vietnam's Decision 33/2026, Korea's AI Basic Act, the
UNESCO IESALC **87 % / 74 %** pair, the LAC Observatory and the TALIS figures. 🟢 **Stated
rather than passed over in silence, because an informed null result is the only thing that
distinguishes a saturated channel from an unrun one.** What `p359` adds to this file is a
**market-size spread** (below) and, for the first time, **regional supply placement
derived from the commit channel** rather than from prose.

---

## Market size

| Scope | Figure | Source quality |
|---|---|---|
| Global AI-in-education, carried from prior cycles | $9.58 B (2026) → **$42.48 B by 2030**, CAGR ~41.5 % | 🟡 Carried; commercial research, not re-verified this pass |
| **Europe** AI-in-education | **$2.64 B (2026) → $8.0 B by 2030**, CAGR **31.9 %** | 🟡 Secondary (vendor summary) |
| North America share of global market | **~36 %** — the largest regional share | 🟡 Secondary (vendor roundup) |

🔵 **A note on these numbers.** Every market figure available this pass traces to a
commercial research product or a vendor blog, not to a primary statistical source.
They are directionally consistent — a high-growth market in the $10 B range heading
toward the $40 B range — and should be used for framing, never quoted to a client as
established fact. The *adoption* and *regulatory* figures below are substantially
better sourced.

### 🔴 🆕 `p359`: the spread between research firms is the number worth putting in a deck

🟢 **One prescribed leg produced something this file lacked, and it is not a figure — it
is the disagreement between figures.** Six commercial estimates for **the same market in
the same year**, collected in one pass:

| Firm | 2026 base | Forecast | CAGR |
|---|---|---|---:|
| Market Reports World | **$1.94 B** | $48.36 B by 2035 | 42.95 % |
| TrendX Insights | $5.21 B *(2025)* | $61.26 B by 2034 | 31.50 % |
| Precedence Research | **$9.58 B** | $136.79 B by 2035 | 34.52 % |
| Research and Markets | **$10.6 B** | $42.48 B by 2030 | 41.5 % |
| Grand View Research | **$11.4 B** | $57.2 B by 2033 | 25.9 % |
| Technavio | — *(+$3.37 B increment)* | 2025–2030 | **45 %** |

🔴 **The 2026 base figures differ by roughly 6×, and the CAGRs by 19 percentage
points.** 🔵 Precedence states the cause plainly in its own summary: the figure depends on
**where the market boundary is drawn and whether embedded AI revenue counts** — which is
not a methodological footnote but the entire question. A platform that ships an AI
feature inside an existing LMS licence either is or is not "AI in education" revenue, and
that single choice spans most of the 6×.

🟢 **The engagement consequence, which is the point of recording it.** A client deck that
quotes one of these as *the* market size is making an unforced error that any analyst in
the room can puncture. 🟢 **Quote the spread and the reason for it**: the market is
growing fast, nobody agrees what it contains, and **the client's own addressable slice is
the only number worth modelling.** 🔵 This base carries `$9.58 B → $42.48 B` as its
framing figure and now carries the spread beside it, so the framing figure is never
mistaken for a measurement.

## The structural shift of 2026

The consistent finding across every source this pass: AI in education has moved
**from pilots to governed, embedded operation**, and the binding constraint is no
longer capability but **governance and evidence**.

- 1EdTech frames 2026 as the shift "from experimentation to governance" — policies,
  data boundaries and oversight rather than tool-collecting.
- HolonIQ expects *selective* acceleration, with systems increasingly demanding
  **evidence that products improve learning quality** before procurement.
- Campus Technology's industry panel expects AI to be embedded infrastructure across
  admissions, advising and learning in higher education.
- The move is away from generic assistants toward **education-purpose-built**
  platforms.

For a studio, this inverts the sales motion: the differentiator is no longer a demo,
it is **auditability, curriculum alignment and an evidence story**.

## Key players by layer

| Layer | Players |
|---|---|
| Hyperscalers / model providers | Google, Microsoft, OpenAI, NVIDIA, Anthropic, IBM — all named in the US "Pledge to America's Youth" (200+ companies) |
| Incumbent publishers / EdTech | Pearson, Instructure (Canvas), Anthology, D2L (Brightspace), Byju's (APAC) |
| Open-source platform stewards | Moodle HQ, Open edX (Axim Collaborative), Learning Equality (Kolibri), Frappe, OpenOLAT, Chamilo Association |
| Standards and governance bodies | 1EdTech (LTI, Caliper), UNESCO (IESALC, LAC Observatory), OECD (Digital Education Outlook), OpenWallet Foundation |
| Agent/skill-layer entrants | Learning Commons, Anthropic (K-12 teacher skills), HKU Data Science (DeepTutor), Cavira (PageLM) |

---

## Opportunities by region

### North America

**Regulatory and adoption state.** Regulation is **state-level and fragmented**:
**134 AI-in-education bills across 31 states** in the 2026 session, focused on student
data privacy, limits on classroom use, and barring AI from high-stakes decisions about
students. Federally, the **K-12 AI Literacy and Readiness Act (H.R. 8747)** advanced
out of the House Education and Workforce Committee on **21 July 2026**, largely along
party lines, and would let schools spend federal funds on AI curriculum. Adoption is
high but contested: **~60 % of US K-12 teachers used AI tools in 2024-25 and 32 %
weekly**, while **New York City has a one-year moratorium on student-facing AI through
eighth grade**. Canada has **no federal AI statute**; its "AI for All" strategy
(launched **4 June 2026**) includes an AI-literacy push but no legislative date.
Mexico has bills but no enforcing regulator.

**Opportunities.**
1. **Fifty-state compliance tooling.** Fragmentation is the product opportunity: a
   policy-aware guardrail layer that applies the right rules per district. Build on
   [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (MIT code).
2. **Canvas-native LTI tools.** Canvas dominates US higher education and is AGPL —
   so the deliverable is an **LTI 1.3 tool**, not a fork. [`CACCL`](https://github.com/harvard-edtech/caccl) (MIT, Harvard) plus [`ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) is the clean stack.
3. **Evidence instrumentation.** With procurement demanding efficacy proof,
   [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta) (Apache-2.0) runs randomised experiments *inside* the LMS — a differentiator almost nobody offers.
4. **Accessibility remediation at scale.** [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) against Section 508 obligations, with AI generating the fixes rather than only flagging them.
5. **AI-literacy curriculum delivery**, positioned for H.R. 8747 federal funding if it passes.
6. 🆕 **Autograding and code-execution for CS and bootcamp clients.** `p356` verified a
   fifteen-row execution tier, **six rows of it permissive**, including
   [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (BSD-3-Clause,
   UC Berkeley) for Python *and* R notebooks and [`okpy/ok-client`](https://github.com/okpy/ok-client)
   (Apache-2.0, Berkeley). Both are North-American university tooling, both are
   licence-clean for a closed deliverable, and neither was on this base one pass ago.
   See `verticals/solutions.md` and Pattern 9.

🔴 **State rules are now binding, not advisory, and the dates have passed or are
imminent** (🟡 secondary sources this pass — check the primary bills before advising):
**Ohio** requires districts to adopt an AI framework by **1 July 2026**; **Idaho SB
1227** is enacted with a statewide framework, AI-literacy standards and a bar on AI
replacing human teachers; **Vermont HB 650** requires education-technology providers to
**register and certify privacy compliance annually** — a vendor-side obligation that
lands on a studio shipping into Vermont districts, not only on the district.
🆕 **Colorado repealed and replaced its AI Act** with the **ADMTA (SB 26-189)**, signed
**14 May 2026**, effective **1 January 2027**. 🔵 The consequence is strategic: the US
has **stopped converging** on a single compliance shape, so a multi-state deployment
needs a posture per state rather than one national one. 🔴 One source in this pass's
leg claims the Colorado framework **carves out FERPA-covered institutions**; nine
others on the same statute do not mention it, so **it is not published here** — it is
recorded as unverified so that no successor promotes it out of this base's own prose.

🆕 **`p357` — the assessment-integrity market is reversing, and it is a North American
reversal first.** Yale, Cornell and the University of Wisconsin–Madison now
**discourage or bar AI-detection scores in academic-misconduct cases**; a Stanford
study found detectors flagged **61 % of essays by non-native English speakers** as
machine-written. Institutions are moving to **oral examination, proctored assessment and
grading the writing process**. 🔴 This is a *demand-side* collapse of a product
category, not a regulatory change — see `intel/trends.md` §16 for which of this base's
four detection repos survive it and which do not.

**Opportunities (`p357`).**
1. 🆕 **Process-evidence instrumentation — the thing detection is being replaced
   with.** Draft history, revision sequence and time-on-task are **telemetry**, and
   Caliper and xAPI already carry them. Build on
   [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) (🔴 implement the
   standard; its licence covers a document, not software) with
   [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
   (Apache-2.0) to evidence it as an in-LMS randomised study. 🟢 **This is the rare
   opportunity where a procurement objection (§2's evidence gate) and a product gap
   point at the same build.**
2. 🆕 **AI-literacy degree and credential programmes as delivery work.** The
   **University of Arkansas at Little Rock** began its first AI bachelor's programme
   this autumn, and **Thomas College (Maine)** is building AI literacy on a **$3 million
   US Department of Labor grant** with its course and major structure still undecided.
   🟢 Institutions with funding and an undefined curriculum are a curriculum-design
   engagement, not a software sale.
3. 🆕 **Administrative automation, now with a measurable claim attached.** Reporting
   this month attributes the **first decline in US higher-education non-teaching
   administrative headcount in decades** to AI. 🟡 This is analyst attribution in a
   general-interest outlet, not an institutional study, and should not be quoted to a
   client as established — but it is the first time the administrative-efficiency case
   has had a directional number behind it.

🔵 **One source in this leg is recorded and not published as supply:** an opinion piece
describing an evaluation agent scoring coursework against rubrics with humans handling
exceptions. It is **commentary, not a reported deployment**, and this base does not
promote a described architecture into evidence of one.
#### 🟢 `p358` additions — the legislative curve, and two district policies that define the real constraint

🟢 **The 2026 bill count has a baseline now, and the curve is the story.** The 2025
session saw **53 AI-in-education bills across 21 states**, with four states enacting
(Illinois, Louisiana, Nevada, New Mexico). The 2026 figure of **134 bills across 31
states** is therefore roughly a **2.5× increase in one session**. 🔵 For a studio that
sells compliance tooling, the slope matters more than the level: a guardrail layer
written against 2026 rules will be out of date by the next session, which argues for
**policy-as-configuration** rather than policy-as-code.

**Named instruments this pass:** 🟢 **California AB 1159** and **Idaho SB 1227** on
student data and AI tools · **Oklahoma** and **Maryland** requiring human oversight and
barring AI from high-stakes decisions about students · **Georgia** and **Mississippi**
folding AI instruction into computer-science credit requirements.

🟢 **Two district policies show the shape procurement actually takes**, and they are more
useful than the bill counts because they are already binding:

- **Katy ISD (Texas)** bans generative-AI chatbots for **K-6** outright and phases in
  *supervised* access from grade 7.
- **Charleston County Schools** bars AI from being the **sole basis** for high-stakes
  decisions such as discipline or placement.

🔵 **Read both as the same requirement in different words: an age gate and a
human-in-the-loop record.** That is a build specification, and it is the one capability
most AI-education demos lack. 🟢 It maps directly onto a row this base verified this
pass — [`AnonymousOnyx22/canvas-lms-student-mcp`](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp)
(MIT, read-only **by construction**: it cannot submit, edit or delete) and
[`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) (MIT, whose
every write tool refuses to mutate without `confirm_write=True`). **A capability ceiling
and a confirmation protocol are the two auditable answers to "AI may not decide."**

**Federal and industry context.** A **White House executive order on AI education** and a
**"Pledge to America's Youth"** with **200+ participating companies** (Google, OpenAI,
Microsoft, NVIDIA, Salesforce among them); the **American Federation of Teachers** runs an
AI instruction academy with Microsoft, OpenAI and Anthropic. 🟡 Market share: North
America is cited at **~36 % of the global AI-in-education market, ≈ $3.68 bn in 2026** —
a commercial-aggregator figure, not a primary source.

### EMEA

**Regulatory and adoption state.** The **EU AI Act is the binding frame, and education
is squarely in scope**: AI used for **admissions, student evaluation and exam scoring
is classified high-risk** under **Annex III point 3**. 🔴 **The deadline moved.** The
Digital Omnibus on AI, **Regulation (EU) 2026/1744** (published 24 July 2026, in force
**27 July 2026**), postponed Annex III high-risk obligations from 2 August 2026 to
**2 December 2027**; Annex I (AI embedded in regulated products) moves to 2 August 2028.
Parliament and Council set **fixed** dates — there is no mechanism to postpone
2 December 2027 again for missing standards. 🟢 **What binds an education provider
today** is not the high-risk regime but the **prohibitions**, the **AI-literacy duty**,
and **Article 50 transparency/labelling** (sources differ on whether the labelling date
is 2 August 2026 or 2 December 2026 — check the Official Journal before advising).

🟢 **`p356` re-ran this leg and the held date survived a direct challenge.** Several
sources in this pass's EMEA leg still assert **2 August 2026** for the Annex III
education obligations. 🔴 **That date is not published here**: this base already refuted
it, and a **European Commission AI Office slide in this same leg gives 2 December 2027**
for Annex III. The refutation stands, now corroborated on the Commission's own channel.
🔵 Two further points from the leg that an engagement needs and this file did not carry:
**emotion-recognition AI in schools has been prohibited since February 2025**, and a
school that merely *licenses* an AI platform for teaching, marking or admissions is a
**deployer** with its own obligations — so the compliance deliverable has a buyer on
**both** sides of the contract.
The Commission has issued
**ethical guidelines for educators** on AI and data use. The UK takes a light-touch,
principles-based route through existing regulators and has invested a reported **£4 M**
in AI lesson-planning and marking tools. **Finland, Estonia and the Netherlands** lead
K-12 integration. Critically, one survey of 450+ institutions found **only ~10 % have
formal AI-use guidelines** (source unclear — treat as indicative).

**Opportunities.**
1. **AI Act high-risk conformity, as a 14-month readiness programme.** The strongest
   single opportunity in any region this pass — but sell it on the **real** date.
   Admissions and assessment AI will need documented risk management, data governance,
   human oversight and logging by **2 December 2027**. 🔵 The runway is the pitch: a
   provider starting now has time to build conformity properly, where one told it was
   already bound in August 2026 buys panic remediation. Against ~10 % of institutions
   having any formal AI guideline, readiness work is available now and the deadline is
   fixed.
2. **Assessment integrity.** EMEA universities built this tooling and will buy its
   AI-era successor: [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT) and [`INGInious`](https://github.com/INGInious/INGInious) are the bases.
3. **Permissive-platform modernisation.** [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland) is the one full HE platform that can be extended into closed deliverables — a licence advantage worth leading with.
4. **Multilingual content generation** across 24 official EU languages, via [`h5p/h5p-cli`](https://github.com/h5p/h5p-cli) (MIT) and [`openpatch/hyperbook`](https://github.com/openpatch/hyperbook) (MIT).
5. **Africa / low-connectivity delivery.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, offline-first) and [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) (MIT, Tanzania) — real assets for Sub-Saharan deployments, with no copyleft reach.

🆕 **Opportunity added this pass.** The EU's **Apply AI Alliance** is live and its **AI
Skills Academy** sector-tailored AI-literacy training **starts Q4 2026 — now**. That is
the funded, demand-side counterpart to the Article 4 literacy duty this file already
carries: the obligation and the money to discharge it are both current, and the
curriculum-and-assessment layer under it is `compose/patterns.md` Pattern 9 plus the
item-bank tier on `agents/top.md`.

🆕 **`p357` — the Gulf is the only place on earth where AI-in-education is compulsory
and already shipping, and this base had been reading it as an adoption story.** It is a
**procurement** story:

| | UAE | Saudi Arabia |
|---|---|---|
| Status | Cabinet-approved **mandatory** AI subject, public schools, from **2025-26** | National AI curriculum **launched August 2025** |
| 2026-27 change | Design, Innovation and Computer Science **merged into one subject, "Artificial Intelligence and Technology"**, across the first, second and third educational cycles | 🟢 **50 AI units added** and **22 existing subjects updated** (Education Minister) |
| Reach | All public schools **and all private schools following the national MoE curriculum**, with teacher training alongside | ~**6 million students** nationally, elementary through university |
| Higher education | — | 🟢 **SDAIA's national cross-disciplinary data-and-AI curriculum, becoming mandatory for all undergraduates across every discipline** |
| Framework | National Artificial Intelligence Curriculum Framework | — |

🟢 **Why that is a different engagement from an EU one.** EMEA's EU half is a
**compliance** market: the binding question is conformity against the AI Act, and the
deliverable is auditability. The Gulf half is a **delivery** market: the mandate already
exists, the curriculum is written, and the gap is content, teacher capability and
platform at national scale. 🔵 A studio pitching AI-Act conformity into Riyadh or Abu
Dhabi is answering a question nobody asked.

🆕 **Africa — the region this base has carried as a gap, now with a structure and four
national positions.** 🔵 Published because an *informed* gap is worth more than silence,
and because three of these are procurement calendars rather than aspirations:

- **Continental.** The **African Union Continental AI Strategy** runs to **2030**, and
  its **first phase (2025-2026)** is explicitly governance structures and national
  strategies, with a named commitment to *"continent-wide AI education initiatives with
  curriculum development for youth at all levels."*
- **Kenya** — the furthest along. Its **National AI Strategy 2025-2030** commits to
  embedding AI literacy across education and to piloting **Digital Innovation Hubs
  (DigiKen)** as curriculum anchors; the **Competency-Based Curriculum** (2017) already
  carries digital literacy and coding, and the Digital Literacy Programme has reached
  **over a million learners**. 🔴 **And the gap is specific and buildable:** a 2024
  study found **AI is not yet in the teacher-training curriculum** — a strategy with
  delivery capacity and no teacher pipeline is a teacher-enablement engagement.
- **South Africa** — a **draft National AI Policy (2026)** targeting AI education and
  skills through **STEAM curricula and community AI centres**; coding and robotics with
  AI elements were earlier proposed for compulsory schooling. Microsoft has a public
  target of AI and digital skills for **a million South Africans by 2026**. 🟡 The
  policy is a **draft** and this base does not treat it as in force.
- **Nigeria** — 🔴 **the honest negative.** Its National Digital Economy Policy
  references AI, but application in education is **aspirational rather than systemic**,
  and ML courses sit mainly in universities and private hubs **concentrated in urban
  areas**. 🟢 One hard datapoint cuts the other way: a **randomised trial of
  ChatGPT-based English tutoring with 800 students** showed gains in English, digital
  literacy and AI knowledge.
- **Ghana** — **AI microcredential enrolments rose 95 %** (Coursera *Global Skills
  Report 2026*). 🟡 Vendor-published, and the clearest demand signal in the leg.
- **Delivery reality.** **Eneza Education** (Kenya) delivers curriculum-aligned lessons
  **by SMS to basic phones** and reports **10 million-plus learners** across several
  African countries. 🟢 That is the region's actual distribution channel, and it is the
  argument for [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
  (MIT, offline-first) over anything assuming connectivity.
- **Scale of the ask.** One roadmap proposes a call for proposals from edtech firms and
  consortia **late 2026 into 2027**, estimating **~$3 billion** continent-wide for AI
  and STEM learning centres and teacher training. 🟡 Proposal, not committed funding.

🔴 **The gap that remains, stated so it is not mistaken for coverage.** No source in
this pass's legs gives a **confirmed 2026 AI-curriculum rollout** in Kenya, South
Africa, Nigeria or Ghana — strategies and drafts, not mandates. 🟢 The Gulf has
mandates; Africa has plans and one measured demand figure. Those are different markets
and this file no longer averages them into "EMEA".

🆕 **Supply, not just policy:** EMEA gains its first curriculum **data** asset this
pass — [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology),
the Oak National Academy curriculum as OWL/SKOS aligned to the **National Curriculum
for England**, with the ontology and data under **OGL-3.0** (commercial use, attribution
only, **no share-alike**) and the scripts under MIT. 🟢 **It is the best-licensed
curriculum asset anywhere on this base** — see `agents/top.md` for the comparison
against `os-taxonomy`'s ODbL share-alike.
#### 🟢 `p358` additions — the AI Act is live, and EMEA's two unserved thirds

🔴 **The EU AI Act's enforcement date has passed, and education is squarely inside it.**
From **2 August 2026** the **AI Office and national authorities began enforcing** the Act.
Education uses the Act classes as **high-risk** are precisely the ones a studio is asked
to build: **admission decisions, student evaluation, and exam scoring**. 🟢 The Commission
has also issued **updated guidelines on the ethical use of AI and data in teaching and
learning**, citing the Act and AI literacy. 🟡 One source in this pass's leg dates
amendments to June 2026 with entry into force on 27 July 2026, which conflicts with the
2 August enforcement date other sources give — **verify against the official timeline
before a compliance deliverable rests on either.**

🔵 **The engagement consequence is a documentation burden, not a model choice.** High-risk
classification brings conformity assessment, technical documentation, logging and human
oversight obligations. 🟢 That makes the **audit trail the product**, and it is why the
`confirm_write`/read-only connector pattern above is as saleable in the EU as in Texas.
🔴 It also makes `verticals/solutions.md`'s licence-reach column load-bearing in a new
way: AGPL on a platform the client *deploys* is manageable, but AGPL on a **connector the
engagement ships** sits inside the system being assessed.

**Leading adopters and figures.** **Finland, Estonia and the Netherlands** are named as
leading K-12 AI integration. The **UK** keeps a light-touch, principle-based approach via
existing regulators. 🟡 The European AI-in-education market is cited at **$2.64 bn in
2026 → $8.0 bn by 2030 (31.9 % CAGR)** — a statistics page citing no primary source,
flagged as such. Germany's **€20 bn AI investment commitment (2025–2030)** is broad AI
investment, **not** education-specific.

#### 🔴 EMEA is three regions and this file has been serving one

🔵 On the closed vocabulary, EMEA is Europe **and** the Middle East **and** Africa. Every
row on `agents/top.md`'s EMEA bucket was European until this pass. Here is what the
other two thirds returned:

**Middle East — a commercial incumbent and no open-source supply.** **Alef Education**
(UAE) signed five private school groups in **February 2026**, reaching **33 000+ students
across 28 schools**, and reports a **12.1 % improvement in final-exam performance** among
ESSA Tier 2 students in Abu Dhabi (🟡 company-reported). With Microsoft it trained
**~25 000 educators across 710 UAE schools between 11 May and 30 June 2026**, delivered
through the **Ministry of Education, ADEK, Dubai's KHDA and the Sharjah Private Education
Authority** — 🟢 the most concrete regulator-linked programme in this pass's legs. Alef's
own site claims **90 000+ educators across 20 000+ schools**; 🟡 that is a different scope
from the 25 000 figure and the two must not be combined. 🔴 **The leg returned no Gulf
open-source education repositories and no formal Gulf rules on AI in schools.** Stated as
a measured absence: the opportunity here is **partnership or displacement of an
incumbent**, not greenfield.

**Africa — the first supply, and it is thin.** 🟢 Two MIT rows, both Kenya:
[`gabrielmahia/elimu-mcp`](https://github.com/gabrielmahia/elimu-mcp) (national school
registry, KCSE/KCPE, HELB loans, TVET — 🔴 read its DEMO-data caveat on `agents/top.md`)
and [`Moha-abshir/SMS`](https://github.com/Moha-abshir/SMS) (CBC school management, and
the first permissive administration row on `verticals/solutions.md`). 🔴 Two of the most
interesting addresses in the leg are unlicensed: `elewastem` (offline-first tutor for 16+
African languages) and `AI-CONNECT-AFRICA` (on-device Gemma 3, updates by USB drive or
school LAN). 🟢 **Kenya's National AI Strategy 2025–2030** is the policy anchor.
🔵 **The constraint that defines African delivery is connectivity, and this base already
holds the licensed answer to it:** `learningequality/kolibri` is **MIT** and offline-first
by design. The build is Kolibri plus an on-device model, not a cloud tutor.

**Opportunity, stated plainly.** 🟢 An EMEA engagement in Nairobi or Abu Dhabi is
currently served by *two* rows and *one* platform, against **sixteen** for Europe. That is
the largest unserved gap in this file and the cheapest to close: it needs legs run in
Swahili, Arabic, French and Portuguese, which no pass has done. Registered on
`intel/trends.md` as the regional arm of **`ACTION ZZ-bf`**.

### APAC

**Regulatory and adoption state.** The region is **diverging rather than converging**.
**South Korea's AI Framework Act took effect 22 January 2026** — the region's most
comprehensive statute, combining a policy framework with adoption support (public data
sharing, SME measures). **Vietnam's risk-based AI law took effect 1 March 2026**, and
its high-risk category **explicitly covers education** (dates vary between sources —
verify against the official text). **Japan's AI Promotion Act is a principles law with
no penalties.** **China** is the outlier with binding rules on algorithms, deep
synthesis and generative AI. Most other markets rely on voluntary guidance backed by
existing law. Commercial research names **Google, Microsoft, IBM, Pearson and Byju's**
as leading players, with **China, India and Japan** dominating regional spend.

**Opportunities.**
1. **Korea-first agentic compliance.** Korea has both the clearest statute and real
   first-party supply — [`schoolinfo-mcp`](https://github.com/chrisryugj/schoolinfo-mcp) and [`ku-portal-mcp`](https://github.com/SonAIengine/ku-portal-mcp) (both MIT) already wrap national school data and university portals. A compliant Korean K-12 agent is buildable now.
2. **Vietnam high-risk education AI.** Education is named in the high-risk tier of a
   live statute. The same conformity playbook as EMEA applies, and almost no vendor
   is positioned for it.
3. **India institution-wide stacks.** [`frappe/lms`](https://github.com/frappe/lms) (AGPL-3.0) plus [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0, on Odoo) is a complete India-origin academic + administrative stack.
4. **Curriculum-graph tutoring.** APAC has the densest curriculum-data supply:
   [`clownjee/knowledge-import-pipeline`](https://github.com/clownjee/knowledge-import-pipeline) (Apache-2.0) extracts a knowledge graph from textbooks and exposes it over MCP. 🔴 Note that [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy), the best Chinese K-12 graph available, is **CC-BY-NC** and cannot be used commercially — the pipeline must build its own.
5. **Agent-native tutoring at scale.** [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (Apache-2.0, ~41.9 k ★) is the largest education agent anywhere and is APAC-origin.

🆕 **`p356` reframes this region's gap, and the reframing is the finding.** For the
**fifth consecutive pass** the prose leg returned **no education-specific APAC adoption
figure** — only general-enterprise AI material (56 % of APAC businesses have deployed
chatbots or copilots; regional leaders prioritising sovereignty, security and AI
literacy in 2026). 🟢 **In the same pass, the function legs placed 18 of 36 verified
repositories in APAC** — China, Hong Kong, India, Korea, Bangladesh and Iran — across
item banks, online judges, grading agents and scheduling. 🔵 **The two measurements
disagree and the repository evidence is the better one.** What is missing is an
English-language analyst narrative, not the software.

**Opportunities.**
1. 🆕 **AI-native item banking.** Four of this pass's rows are item banks and **all four
   are Chinese-language** — [`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank)
   (330 ★, LaTeX + formula OCR + LLM solving) and
   [`gygy-open/question-bank`](https://github.com/gygy-open/question-bank) (73 ★, Word and
   image import with a review workflow) among them. 🔴 Both are **AGPL-3.0**, so they are
   a reference architecture and a client-side deployment, not a studio product.
2. 🆕 **University judge platforms as a delivery base.** The two largest judges on this
   base — [`hydro-dev/Hydro`](https://github.com/hydro-dev/Hydro) (AGPL-3.0, 7 137 ★) and
   [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge) (**MIT**, 6 552 ★) —
   are both APAC university software with large real deployments. The MIT one is the
   licence-clean base for a regional coding-academy build.
3. 🔴 **Korea's AI-textbook programme fell below 30 % adoption and lost official
   status**, so the APAC delivery risk is **adoption, not compliance** — the inverse of
   EMEA. Price change management accordingly.

🆕 **`p357` — two mandates, one marking-governance precedent, and a correction to how
this file frames India.**

- **India is the largest single mandate in the world and it is dated.** From
  **2026-27**, **AI and computational thinking become mandatory from Class 3** across
  government and private schools, alongside a national AI mission. 🔴 **And the
  constraint is named by the sources, not inferred:** the rollout is **ahead of teacher
  readiness**. 🟢 For a studio that is the engagement — teacher enablement and
  curriculum delivery at national scale, not a tutoring product.
- **China** has had AI as a **compulsory subject from age six since September 2025**,
  and its binding rules are already in force, including **content-labelling measures
  applicable from 1 September 2025**.
- **India's rules, for an engagement that ships there:** no AI statute and voluntary
  guidance, but **February 2026 IT-rule amendments require platforms with over 5 million
  users to label AI-generated content**, and the data-protection law's obligations phase
  in **until May 2027**. 🔵 A national-scale education platform crosses that 5-million
  threshold by design.
- 🔴 **Japan's AI Basic Plan date is contested and this base publishes neither.** One
  source gives adoption **23 December 2025**; another a Cabinet revision **14 July
  2026**. The *substance* is not in dispute — the **AI Promotion Act carries no fines
  or prohibitions** — so the posture is publishable and the date is not.

🆕 **The marking-governance precedent, because it is the first institutional rule of its
kind this base has found.** The **University of Newcastle (Australia)** requires that
any use of generative AI **in marking** be communicated to students, **with an opt-out**.
🟢 Paired with a **1 339-teacher experiment** showing a harsh AI grade **survives review
more often when labelled as AI**, this is a design constraint rather than a policy note —
`intel/trends.md` §17 has the three things that follow from it.

🟡 **Adoption, flagged as weakly sourced.** A CIO-focused report places **Japan, India
and China as relative laggards** in enterprise AI maturity with **Singapore leading**,
and **only ~1 in 10 APAC enterprises** self-describing as "very mature". 🔵 Consistent
with §15: the analyst narrative and the repository evidence disagree about this region,
and this base holds that the repository evidence is the better measurement.
#### 🟢 `p358` additions — APAC now has binding AI law, and education is a named high-risk sector

🔴 **Vietnam has the region's first dedicated AI statute and it reaches foreign firms.**
**Law No. 134/2025/QH15 on Artificial Intelligence** took effect **1 March 2026**.
**Education is one of six sectors** covered by its high-risk list, with **automated
assessment and behavioural monitoring** given as examples. 🟢 The dates are the actionable
part: identified systems must comply by **1 March 2027**, with an **additional six months**
for education systems already in operation before **15 August 2026**. 🔵 **So there is a
live compliance window and it closes inside this engagement cycle** — a Vietnamese
institution running an automated-assessment system today has a dated obligation, which is
a sales motion rather than a forecast.

**The rest of the region, by posture:** 🔴 **South Korea's AI Basic Act** took effect
**January 2026**, with risk-management and disclosure duties for high-impact systems ·
🔴 **China** operates the most restrictive framework — mandatory registration, substantial
penalties · 🟡 **Japan, Singapore and Taiwan** rely on voluntary or framework-style
instruments · 🟡 **Australia** relies on existing technology-neutral law and its mandatory
guardrails are **paused**.

🟢 **An attitudinal finding that cuts against the regulatory one.** The **Ipsos Education
Monitor 2026** records **lower** support for banning AI in schools across the Asian
markets surveyed, and **higher** support for banning it in **Australia and New Zealand**.
🔵 That inverts the usual reading: the markets with the strictest *statutes* have the most
permissive *publics*, and the market with the lightest-touch law (Australia) has the most
restrictive public opinion. For a studio, that means **the objection to handle differs by
country**: in Vietnam and Korea it is documentary compliance; in Australia and New Zealand
it is parent and teacher consent.

🟡 **Named commercial players** (from paid market reports, indicative not authoritative):
**Riiid** (South Korea), **Squirrel AI** (China), **Alef Education** (UAE), **Byju's**,
alongside Google, Microsoft, IBM and Pearson. 🔴 One report's claims that Japan and Korea
introduced education-specific AI data rules in 2023, and of a "South Korea AI Data
Protection Act", **could not be corroborated** in this pass's legs and are recorded as
unverified rather than repeated.

🟢 **APAC remains the densest supply region on this base — 21 rows on `agents/top.md`** —
and the Vietnam window is the first time a *regulatory* date, rather than supply, is the
reason to lead with the region.

### LATAM

**Regulatory and adoption state.** Adoption is **high and ungoverned** — the clearest
opportunity-shaped gap in any region. The **UNESCO IESALC study** (with UNU-IAS) across
**200 institutions in 19 countries** found **87 % use AI somewhere in operations but
only 26 % have a formal AI strategy**, with adoption driven by individual faculty and
students rather than institutional policy. The **Digital Education Council LATAM 2026
survey** covers 30 000+ responses across 29 institutions. **UNESCO launched a regional
Observatory on AI in Education for LAC in April 2026** at ECLAC headquarters in
Santiago, with a Mexican pilot through **CONALEP and DGETI** building centres of
excellence. Regulation is emerging nationally: **Uruguay** was the first in the region
to sign the Council of Europe AI Framework Convention (2025); **Peru** has a phased AI
law with regulatory sandboxes; **Mexico** has a federal AI bill in the Senate;
**Colombia** adopted national AI policy **CONPES 4144** (2025). **ILIA 2025** reports
school-level AI education is growing but remains the exception.

**Opportunities.**
1. **Institutional AI strategy and governance.** The 87 %-adoption / 26 %-strategy gap
   is a direct, sizeable consulting engagement, and UNESCO's Observatory gives it
   regional political cover. This is the highest-confidence LATAM opportunity.
2. **Curriculum-aligned agents on national standards.**
   [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) (MIT) publishes Brazil's **BNCC as 1 721 verified learning objectives** in JSON/SQLite/CSV. A BNCC-aligned tutor or lesson planner can be grounded in official standards today — and nothing equivalent exists for Spanish-speaking markets, which is itself the opening.
3. **Spanish-language curriculum data as a build, not a buy.** 🔴 The
   Spanish/Portuguese discovery leg run this pass returned **10 repositories and zero
   usable education assets**. Mexico's SEP, Colombia's and Argentina's national
   standards have **no open machine-readable equivalent of BNCC**. Building one is a
   defensible regional asset.
4. **Public-sector K-12 systems.** [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) (GPL-2.0) and [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) both have mature Spanish/Portuguese localisation and real public-sector deployments — the realistic bases for ministry-scale work.
5. **Offline-first rural delivery.** [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) for low-connectivity regions, licence-clean for closed deliverables.
6. **Brazilian public data integration.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (MIT) exposes Brazilian public datasets, education among them, over MCP.
7. 🆕 **Spanish-language assessment tooling, with the gap now precisely located.**
   `p356` re-ran the regional leg using **function words** rather than prose —
   `calificación`, `corrección`, `banco de preguntas`, `banco de questões`, `examen` — and
   it returned **228 209 results and zero education tooling**. 🔵 **But the hits are
   informative rather than empty:** the education-relevant ones are **exam-content
   archives** — FAMAF/UNC (Argentina), Instituto Tecnológico de Costa Rica,
   `111milprogramadores` — students sharing past papers.
   🟢 **So Spanish-language assessment *content* exists in volume while the *tooling*
   does not.** That is a sharper brief than "nothing found": there is raw material for a
   Spanish-language item bank and no incumbent to displace. 🔴 Licences on those corpora
   were **not** verified this pass and must be before any use.
8. 🆕 **Ceibal × EdTech Hub as the route to ministries.** **Fundación Ceibal** (Uruguay)
   announced a partnership with **EdTech Hub** in **September 2026** to bring
   AI-in-education evidence and guidance to governments across Latin America and the
   Caribbean. For a studio this is the credible entry point to public-sector work in the
   region: it is an evidence-and-guidance channel, and `intel/trends.md` §2 says evidence
   is becoming the procurement gate.

🆕 **`p357` — one date that moved, one programme that is real, and the structural
finding restated.**

- 🔴 **Chile's data-protection date moved, and it is the one LATAM date most likely to
  be wrong in a client deck.** The executive sent **bill 18.623-07** to Congress to push
  the general effective date of **Personal Data Protection Law No. 21.719** from
  **1 December 2026 to 1 December 2027**. 🟢 This matters to education AI specifically
  because that law governs **profiling** — which is what adaptive learning is. Chile's
  AI bill (**bulletin 16821-19**, introduced 7 May 2024) remains **in committee**.
  🟡 A bill to move a date is not the moved date: verify against the official record
  before advising.
- **Brazil remains the region's most advanced and the timing is now electoral.**
  **PL 2338/2023** was approved by the **Senate on 10 December 2024** and sits in the
  **Chamber of Deputies**, with reports indicating the vote resumes **after the October
  2026 elections**. Its risk tiers place **education among high-risk uses**, bringing
  mandatory impact assessments and human oversight. Brazil's **first AI regulatory
  sandbox launched in 2025**.
- 🆕 **Mexico — the concrete item is workforce, not classroom.** The **Public AI
  Training Center**, run by **INFOTEC and TecNM with 14 technology companies**, aims to
  graduate **10 000 specialists in 2026**. 🔵 Published with that framing deliberately:
  it is a **skills-pipeline** programme, and this base does not promote it into evidence
  of classroom AI policy. 🔴 Sources disagree on whether Mexico enacted AI amendments in
  2026 — one says yes, another says no bill has passed — **so no Mexican legislative
  status is asserted here.**
- 🟢 **And the structural finding holds, now from a second instrument:** *"education
  systems are quietly integrating AI tools into classrooms — often without oversight or
  guidelines."* That is the 87 %-adoption / 26 %-strategy gap restated by a different
  source, which is what makes the governance engagement above the region's
  highest-confidence opportunity.

🔴 **`p357` ran no LATAM *supply* leg**, so the two LATAM rows on `agents/top.md` are
unchanged and **unretested**. 🔵 Stated because an unchanged count across two passes
reads as confirmation and is not one.
#### 🟢 `p358` additions — the region with the highest teacher adoption, the weakest governance, and the least usable code

🟢 **The adoption numbers are now primary-sourced and they are high.** **UNESCO IESALC**
surveyed **200 institutions across 19 countries**: **87 % already use AI in at least one
area** and **74 % in teaching and learning** — while **only 26 % have a formal AI
strategy**. Adoption splits by sector: **private non-profit 84 %, public 68 %, private
for-profit 52 %**. In schools, **TALIS 2024** puts secondary-teacher AI use **above the
OECD average of 36 %** across the region: **Brazil 56 %, Chile 55 %, Colombia 53 %, Costa
Rica 52 %**. Uruguay's **Ceibal** reports **75 % of public-school teachers** using these
tools.

🟢 **Policy and institutions.** **UNESCO launched the Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean in April 2026, at ECLAC
headquarters in Santiago**, to guide public policy. Legislatively: **Brazil's PL
2.338/2023** is in the Chamber of Deputies (🟡 its text can still change); **Chile's**
government-sponsored bill is in its first constitutional stage; **Colombia** has a
national AI policy via **CONPES 4144**, with budget running to **2030**.

#### 🔴 The three findings line up, and together they are this pass's clearest regional thesis

Put this pass's three LATAM measurements side by side:

| Measurement | Value | Source |
|---|---|---|
| Institutions using AI somewhere | 🟢 **87 %** | UNESCO IESALC, 200 institutions / 19 countries |
| Institutions with a formal AI strategy | 🔴 **26 %** | same |
| 🔴 **Live LATAM education repos carrying a licence** | 🔴 **3 of 13 (23 %)** | 🟢 **this base, payload channel, this pass** |

🟢 **Adoption is ahead of governance, and governance is ahead of licence hygiene.** The
third row is this base's own first-hand contribution and it is the one no market report
has: the region's open-source education tooling **exists** — a Saber Pro item bank, a BNCC
municipal assessment platform, four ENEM platforms, an autograder doing RAG over open
answers, a *Nueva Escuela Mexicana* school platform — and **ten of thirteen live
addresses carry no grant at all.**

🔵 **So the LATAM offer is not "AI for education". It is governance and provenance**, and
all three measurements point at the same deliverable: an institution that has adopted AI
without a strategy, in a region whose available code cannot be legally used, needs the
**audit trail, the licence position and the human-in-the-loop record** before it needs a
better model.

🟢 **Opportunities, now placed against named instruments rather than sentiment:**

1. 🟢 **Colombia is the best-evidenced entry point on this base.** Two verified rows and a
   funded national policy: [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
   (MIT, Universidad Tecnológica de Pereira, an autonomous tutor **inside Open edX** for
   **rural** higher education in Risaralda) and
   [`Dramoscuello/openpiar`](https://github.com/Dramoscuello/openpiar) (AGPL-3.0),
   which implements the **PIAR** that **Decreto 1421 de 2017** makes mandatory and the
   inclusive-education duties of **Ley 2216 de 2022**. 🔵 **That is a statutory
   deliverable, not a pilot** — the document a school is obliged to produce — and
   **CONPES 4144** is the budget line it sits against.
2. 🟢 **Rural and low-connectivity delivery is a licensed stack today.** `TutorIA`'s own
   target is rural higher education; pair it with `learningequality/kolibri` (MIT,
   offline-first) and [`Riskbreaker2077/open-test`](https://github.com/Riskbreaker2077/open-test)
   (MIT — local server, school intranet, **every student a different paper**, no
   internet). 🔵 All three permissive; none requires connectivity the region may not have.
3. 🟢 **Brazil: the window is PL 2.338/2023's passage.** `mcp-brasil` and `bncc-dados`
   (both MIT) are the licensed Brazilian rows; the four ENEM platforms are **not usable**,
   so BNCC-aligned assessment is a **build on open data**, not a fork.
4. 🟢 **The 26 % strategy figure is the governance sale**, and it is the same deliverable
   the EU AI Act forces in EMEA — 🔵 which means **one audit-trail and oversight product
   serves both regions**, rather than two regional builds.
5. 🟡 **Ask before you build.** Ten unlicensed addresses are ten authors who published
   publicly and plainly intend their work to be used. For `banco-preguntas-saberpro`'s
   Saber Pro item bank in particular, **requesting a `LICENSE` costs an email and is
   cheaper than re-authoring an item bank.** 🔴 Nothing may be used until one exists.

### Global

1. **MCP as the LMS integration layer.** Every major LMS now has a community MCP
   server (Canvas ×3, Moodle, Open edX ×2, Brightspace ×2, Google Classroom, Anki) and
   nearly all are MIT. An engagement can reach a client's existing LMS **without
   building a connector** — a change in starting cost that did not exist two cycles ago.
2. **Digital credentials for skills-based hiring.** 1EdTech names credentials as a core
   mechanism for 2026. [`learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) (MIT, OpenWallet Foundation) is the reference base.
3. **Legacy SCORM estates.** Corporate learning content remains overwhelmingly SCORM.
   [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT) wraps that estate so AI can be layered on it without re-authoring.
4. **Licence due diligence as a deliverable.** This pass found a NonCommercial grant
   on the best Chinese curriculum graph, an Elastic Licence on a leading advising app,
   per-dataset gating on a prominent "open" data layer, a licence in a directory, and
   a licence that exists only as a `package.json` field. Clients consistently
   mis-assess open-source education assets. See `agents/top.md` and
   `verticals/solutions.md` for the flagged rows.
5. 🆕 **Grading infrastructure as a product line.** `p356` found that the
   code-execution and autograding layer — the thing every coding course needs — is a
   mature, fifteen-row tier with **six permissive rows**, headed by an **MIT** judge at
   6 552 ★. Any client that grades code (bootcamps, CS faculties, certification bodies,
   developer academies) can be served from a licence-clean base today. 🔵 **Costing that
   work as a greenfield build is now a pricing error**, and the studio that knows this
   tier exists quotes differently from the one that does not.
6. 🆕 **Retention, not generation, as the measurable outcome.** The scheduling layer
   (`intel/trends.md` §12, and the FSRS rows on `agents/top.md`) is MIT at every rung and
   small enough to drop into an existing tutor. It changes what a client can measure from
   *content produced* to *knowledge retained* — which is the evidence procurement is
   starting to demand (§2).

7. 🆕 **Curriculum-as-open-data is now licensable in two regions, and the licences
   differ in a way that decides the build.** Brazil's BNCC
   ([`bncc-dados`](https://github.com/bncc-dev/bncc-dados), MIT) and England's Oak
   ontology ([`oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology),
   OGL-3.0 data + MIT code) both permit commercial use **with no share-alike**, while
   the general skeleton everyone reaches for first
   ([`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy), ODbL-1.0) imposes
   share-alike on a **derivative database**. 🟢 For any client whose enriched curriculum
   model must stay closed, start from a national asset, not a general one.
8. 🆕 **Authorship detection is not a product line and supervision still is.** §16's
   reversal is global in implication even though its evidence is North American: the
   claim "a machine wrote this" cannot be made at an acceptable false-positive rate
   across language backgrounds, and **that is an equity failure, not a model-quality
   one** — which means a better model does not fix it. 🟢 Proctoring and
   plagiarism-similarity are untouched. Any education roadmap carrying an "AI detection"
   line item should move that budget to **process telemetry**.

---

#### 🟢 `p358` addition — the one regional conclusion that is not regional

🟢 Across four regional legs this pass, **the same deliverable came back under four
different regulatory justifications**: an **age gate, a human-in-the-loop record and an
audit trail**.

| Region | The instrument that demands it |
|---|---|
| North America | Oklahoma and Maryland human-oversight statutes; Charleston County's "not the sole basis" rule; Katy ISD's K-6 age gate |
| EMEA | 🔴 **EU AI Act, enforced from 2 August 2026** — admissions, student evaluation and exam scoring are **high-risk** |
| APAC | 🔴 **Vietnam Law 134/2025/QH15**, in force 1 March 2026 — automated assessment and behavioural monitoring named high-risk, compliance by 1 March 2027 |
| LATAM | 🟡 No binding instrument yet (Brazil and Chile pending) — but **only 26 %** of institutions have a formal AI strategy, against **87 %** already using AI |

🔵 **That convergence is worth more than any single regional note in this file.** Four
jurisdictions arriving at one requirement means the oversight layer is a **product**, not
four localisations of a project — and the two rows this base verified this pass that
already embody it (`canvas-lms-student-mcp`'s read-only capability ceiling,
`gradescope-mcp`'s `confirm_write` protocol) are both **MIT**. 🟢 The compliance story and
the licence story point the same way for once.

## 🆕 Regional supply placement — `p359`, from the commit channel

🟢 **New instrument, and it answers a question this file could previously only answer for
regulation.** Every address `p359` added was placed by reading committer timezones from
`git log` over a blobless shallow clone — no API, no star count, no self-reported
location. Sixteen new addresses:

| Region | New addresses | Permissive among them | What they are |
|---|---:|---:|---|
| **APAC** | **7** | 3 | IEP management (China, `+0800`), IEP planning (Australia, `+1100`), IEP goals (Thailand, `+0700`), Moodle agent CLI (Hong Kong), proctoring platform (India), LTI proctoring tool, IRT-for-benchmarks (China) |
| **EMEA** | **3** | 1 | Moodle AI grader (`+0200`), special-education RAG (Türkiye, `+0300`), IRT on PyTorch (Sweden) |
| **North America** | **3** | 1 | Parent-facing IEP explainer, district IEP workflow *(dead since 2023)*, OneRoster warehouse *(dead since 2018)* |
| **LATAM** | **2** | 0 | Brazilian education data *(BNCC/SAEB/SARESP)*, Brazilian pedagogical assistant |
| 🟡 unplaceable | 1 | 1 | Commit stream splits `+0000` / `-0600` |

🟢 **APAC leads the new supply, 7 to 3.** 🔵 That is the fourth independent corroboration
of §15 of `intel/trends.md` — *APAC's "gap" is in the trade press, not in the supply* —
and this time it arrives from legs that never named a region, which is a stronger form of
the finding than a regional leg returning regional results.

🔴 **And the regional reading of the licence gap does not survive the same table.** LATAM
is 0 for 2, which looks like §19 confirmed — until North America is also **1 for 3** and
EMEA **1 for 3**. 🟢 **The variable is producer type, not geography** — see §22 of
`intel/trends.md`, where the full cross-tab sits.

🟡 **One honest limit on the instrument.** A committer timezone places where the commits
were *made*, not where the author is from or who the software serves: `elimu-mcp` serves
Kenya on this base and commits from Europe, and `mcp-brasil` is placed LATAM on its
subject matter. 🔵 Timezone is strong corroboration and weak attribution, and this file
uses it as the former.

## Sources

[Campus Technology 2026 predictions](https://campustechnology.com/articles/2026/01/29/2026-predictions-for-ai-and-ed-tech-what-industry-leaders-are-saying.aspx) ·
[1EdTech — three trends for 2026](https://www.1edtech.org/blog/three-trends-were-watching-in-2026) ·
[HolonIQ 2026 Education Trends Snapshot](https://www.holoniq.com/notes/2026-education-trends-snapshot) ·
[MultiState — AI in education legislation 2026](https://www.multistate.us/insider/2026/4/9/how-states-are-regulating-ai-in-education-this-legislative-session) ·
[Pursuit — AI in education news and policies](https://www.pursuit.us/news/ai-in-education-news-policies-innovations) ·
[CDT — states and responsible AI use](https://cdt.org/insights/states-focused-on-responsible-use-of-ai-in-education-during-the-2025-legislative-session/) ·
[AI for Education — state AI guidance](https://www.aiforeducation.io/ai-resources/state-ai-guidance) ·
[European Education Area — ethical guidelines for educators](https://education.ec.europa.eu/focus-topics/digital-education/actions/plan/ethical-guidelines-for-educators-on-using-artificial-intelligence) ·
[European Commission — European approach to AI](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence) ·
[Gibson Dunn — AI Act omnibus: postponed high-risk deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) ·
[Orrick — Digital Omnibus finalizes 8 compliance changes](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes) ·
[ActuIA — obligations in force and delays under omnibus 2026/1744](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/) ·
[Technology.org — AI Act deadlines after the Digital Omnibus](https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/) ·
[Latham & Watkins — AI regulation in APAC](https://www.lw.com/admin/upload/SiteAttachments/AI-Regulation-in-APAC-Diverging-Approaches-Across-the-Region.pdf) ·
[CX Network — how 9 APAC countries regulate AI](https://www.cxnetwork.com/artificial-intelligence/articles/ai-regulation-in-apac-current-developments-and-key-areas) ·
[OneTrust — where AI regulation is heading in 2026](https://www.onetrust.com/blog/where-ai-regulation-is-heading-in-2026-a-global-outlook/) ·
[Ken Research — APAC AI in education market](https://www.kenresearch.com/industry-reports/asia-pacific-ai-in-education-market) ·
[UNESCO IESALC — AI adoption in LAC higher education](https://www.iesalc.unesco.org/en/articles/new-unesco-iesalc-study-reveals-widespread-ai-adoption-higher-education-across-latin-america-and) ·
[UNESCO — Observatory on AI in Education for LAC](https://www.unesco.org/en/articles/observatory-artificial-intelligence-education-latin-america-and-caribbean) ·
[Dig Watch — UNESCO LAC mapping](https://dig.watch/updates/unesco-ai-adoption-latin-american-education) ·
[ILIA 2025 key findings](https://indicelatam.cl/wp-content/uploads/2026/03/ILIA-2025.-Key-Findings-Applied-Artificial-Intelligence-and-Human-Talent-compressed.pdf) ·
[EU IP Helpdesk — AI and IP in Latin America](https://intellectual-property-helpdesk.ec.europa.eu/news-events/news/recent-developments-artificial-intelligence-and-ip-latin-america-pt-iii-2026-05-04_en) ·
[Digital Education Council — LATAM survey 2026](https://www.digitaleducationcouncil.com/resource-library-items/ai-in-higher-education-latam-survey-2026) ·
[Azumo — AI in education statistics](https://azumo.com/artificial-intelligence/ai-insights/ai-in-education-statistics) ·
[Educativa — AI trends in education 2026](https://www.educativa.com/en/blog/ai-trends-in-education-for-2026/) ·
[Education Commission of the States — AI in education state policy trends](https://www.ecs.org/ai-in-education-state-policy-trends/) ·
[Bellwether — The Leading Indicator, AI in education](https://bellwether.org/ai-newsletter/the-leading-indicator-ai-in-education-issue-fifteen/) ·
[Futuresource Consulting — AI adoption across K-12 and higher education](https://www.futuresource-consulting.com/the-source/industry-pulse/new-futuresource-consulting-research-reveals-that-ai-adoption-across-k-12-and-higher-education-is-moving-from-experimentation-to-structured-implementation/) ·
[AIGL — AI in education: an EU AI Act guide](https://www.aigl.blog/ai-in-education-an-eu-ai-act-guide.md) ·
[Rockefeller Institute — EU AI and higher education](https://www.rockinst.org/wp-content/uploads/2025/11/EU-AI-and-Higher-Education-web.pdf) ·
[Forrester — APAC predictions](https://www.forrester.com/blogs/predictions-2025-apac) ·
[UNU — AI implementation in higher education in Latin America and the Caribbean](https://unu.edu/publication/ai-implementation-higher-education-latin-america-and-caribbean) ·
[EdTech Hub — Latin America and the Caribbean](https://edtechhub.org/?p=73866) ·
[Brookings — smart AI regulation strategies for Latin American policymakers](https://www.brookings.edu/articles/smart-ai-regulation-strategies-for-latin-american-policymakers)

**🆕 `p357` additions.**
[ETC Journal — US universities give up on AI detectors (7 Oct 2026)](https://etcjournal.com/2026/10/07/briefing-10-7-26-us-universities-give-up-on-ai-detectors/) ·
[ETC Journal — agentic automation and institutional scale (19 Oct 2026)](https://etcjournal.com/2026/10/19/the-ai-multiplier-how-agentic-automation-is-reshaping-institutional-scale/) ·
[ETC Journal — "BS in artificial intelligence" (13 Oct 2026)](https://etcjournal.com/2026/10/13/briefing-10-13-26-bs-in-artificial-intelligence/) ·
[Harvest Kernel — AI grading: why a harsh AI mark survives review (1 339 teachers)](https://www.harvestkernel.com/ai-grading-anchoring-grade-blind-first/) ·
[Washington Times — AI reversing increases in higher-education administration (20 Oct 2026)](https://washingtontimes.com/news/2026/oct/20/ai-reversing-increases-higher-education-administration-first-time) ·
[Middle East AI News — Saudi nationwide AI education in schools](https://www.middleeastainews.com/p/saudi-to-deploy-ai-education-in-schools) ·
[Middle East AI News — SDAIA national data and AI university curriculum](https://www.middleeastainews.com/p/sdaia-launches-national-data-and) ·
[MENA Startup Digest — Saudi Arabia to add 50 AI units to the national curriculum in 2026-27](https://menastartupdigest.com/saudi-arabia-to-add-50-ai-units-to-national-curriculum-in-2026-27/) ·
[Arabian Post — UAE extends AI curriculum to every school](https://thearabianpost.com/uae-extends-ai-curriculum-to-every-school/) ·
[arXiv:2604.27708 — towards an ethical AI curriculum: a pan-African, culturally contextualised framework](https://arxiv.org/html/2604.27708) ·
[UNICEF Innocenti — how AI can transform Africa's learning crisis into a development opportunity](https://www.unicef.org/innocenti/stories/how-ai-can-transform-africas-learning-crisis-development-opportunity) ·
[APO — AI microcredential enrolments in Ghana rise 95 % (Coursera Global Skills Report 2026)](https://africa-newsroom.com/press/artificial-intelligence-ai-microcredential-enrollments-in-ghana-rise-95-courseras-global-skills-report-2026?lang=en) ·
[Latham & Watkins — AI regulation in APAC: diverging approaches](https://www.lw.com/admin/upload/SiteAttachments/AI-Regulation-in-APAC-Diverging-Approaches-Across-the-Region.pdf) ·
[IA Governance — AI regulation in Asia-Pacific: what each country requires in 2026](https://iagovernance.com/en/blog/ai-regulation-asia-pacific/) ·
[CiberLATAM — Chile, Brazil and Paraguay advance AI laws](https://ciberlatam.com/en/news/chile-brazil-paraguay-advance-ai) ·
[Scientika — Mexico AI: where government AI stands in 2026](https://scientika.org/en/blog/mexico-ai-government-readiness-2026/) ·
[CASRAI — Latin America AI law status compared](https://casrai.org/compare/latin-america-ai-law-status-compared)

🔵 **Source-quality note for `p357`'s additions.** Every regional item above is **trade
press, a practitioner blog, a law-firm briefing or a vendor report** — the Gulf
curriculum items are the best sourced (news outlets reporting ministry announcements),
the Africa items are policy analyses and one arXiv preprint, and the Ghana figure is
vendor-published. 🔴 **No primary ministry or legislative document was read this pass**,
and three items are published as *contested* rather than as fact: Japan's AI Basic Plan
date, Mexico's legislative status, and Chile's effective-date move. 🟢 By contrast every
**repository** row added this pass was read first-hand from the payload — see
`agents/top.md`.

🔵 **Source-quality note for `p356`'s additions.** The regional legs this pass returned
mostly trade press, consultancies and practitioner blogs. The state-bill details (Ohio,
Idaho, Vermont, Colorado) are **secondary** and are marked as such; the EU date is
corroborated on a Commission AI Office slide; the Ceibal × EdTech Hub partnership is on
EdTech Hub's own channel. Every **repository** figure in this base, by contrast, was
read first-hand today — which is why the shelves and this file should be quoted
differently to a client.
