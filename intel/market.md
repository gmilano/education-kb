---
industry: education
region: Global
updated: 2026-11-19
---

# Market intelligence — education

Researched 2026-11-18, extended in pass **p890** the same day with four fresh regional legs.
Sources are named inline. Where estimates conflict, both are given and the conflict is stated
rather than averaged away.

**Verification channel, stated honestly.** GitHub facts in this KB are byte-verified. The legal
and statistical facts below are **not**: in this session the network policy blocks every
non-GitHub host (`403` on CONNECT via curl, `getaddrinfo ENOTFOUND` via WebFetch), so
`ncleg.gov`, `data.consilium.europa.eu`, `unesco.org`, `teqsa.gov.au` and the law-firm
analyses could not be opened and read. What follows is **search-snippet evidence with the
source named**, and where two or more independent sources agree that is said. Anything marked
*(single source)* should be confirmed against the primary text before it goes in a client
deck. This is a gap in the environment, not in the finding.

## Market size — and why the numbers disagree

**Broad AI-in-education market, 2026 base year:** estimates cluster between **$9.6B and
$11.4B**, and diverge sharply on growth.

| Source | 2026 base | Forecast | Implied CAGR |
|---|---|---|---|
| Research and Markets | $10.6B | $42.48B by 2030 | 41.5% |
| Coherent Market Insights | $11.40B | $57.25B by 2033 | 16.8% |
| Precedence Research | $9.58B | ~$136.79B by 2035 | 34.52% |

**Agentic AI in education specifically** — a much smaller base, and the single widest
disagreement we found in any industry:

| Source | 2026 base | Forecast | Implied CAGR |
|---|---|---|---|
| Research and Markets | $2.1B | — | **4.5%** |
| Mordor Intelligence | $2.37B | $11.83B by 2031 | **37.92%** |

Two reputable firms differ by **8x on the growth rate of the same segment in the same
year**. Do not cite either alone in a client deck. The defensible statement is: *agentic
education AI is a ~$2.1–2.4B segment in 2026, roughly a fifth of the broader AI-in-education
market, and analysts do not agree whether it compounds at 5% or 38%.*

**The whole-EdTech envelope, for context (new, 2026-11-17).** A GlobeNewswire release dated
**17 November 2026** puts the *global EdTech market* — not the AI slice — on a **10.8% CAGR to
2033, a $437.54B opportunity**, with personalised learning named as the driver. Use it only as
the denominator: at ~$10B in 2026, AI-in-education is roughly **2–3% of EdTech spend**. The
useful read is that the AI segment compounds at 3–4x the rate of the market containing it,
which is the shape of a category that is still early.

**AI tutors sub-segment:** $3.6B in 2026 → $17.7B by 2033 at 30.5% CAGR (Grand View, via
IdeaPlan). Mordor's framing is the useful one: **tutoring is the gateway purchase that seeds
broader platform penetration.** Sell the tutor, land the platform.

**Caveat on secondary sources.** Several widely circulated pages (x-pilot, TechRT) quote
outcome statistics such as "42% improvement in learning outcomes" and "54% higher test
scores" with no traceable primary study. They are excluded here. A claim about learning
gains needs a primary citation or it does not go in a client deck.

## Key players

**Proprietary / commercial.** Microsoft launched **Microsoft Elevate for Educators**
(Jan 2026). Khan Academy (Khanmigo) and Duolingo are the most-cited tutoring deployments,
though the frequently repeated "50M+ students" figure is unverified. Instructure (Canvas),
Anthology, Ellucian and PowerSchool hold the North American institutional stack.

**Open-source institutional.** The credible AI-in-education engineering is coming out of
universities rather than startups: **TU Munich** (Artemis, EduTelligence, Pyris — MIT),
**HKU** (DeepTutor — Apache-2.0), **Tsinghua** (OpenMAIC — MIT), **UC Berkeley** (OATutor —
MIT), **ECNU** (EduWork — Mulan PSL v2), **Moodle HQ** (wiki-rag — BSD). That concentration
is the central strategic fact of this KB: the best permissive assets are academic, and
academic projects welcome implementation partners.

🔵 **`p925` (2026-11-19) — four fresh regional legs, and the standing honesty caveat above applies
to every number in them.** The legs were `AI education {North America | EMEA | APAC | LATAM} 2026
adoption regulation players`. All four returned material; **none returned a primary source**, and
the figures below are from trackers, law-firm notes, market-research blogs and
multilateral-organisation summaries. Where two sources conflict the conflict is stated.
🔴 **Three specific conflicts were found and are recorded in place rather than averaged:** the
rank of South Korea's AI Basic Act (first comprehensive statute, or second after the EU AI Act);
the size of the EMEA education-AI market (two incompatible figures); and whether Argentina's AI
bill regulates or de-regulates. 🟢 **The new regional finding with the most engagement value is in
APAC and LATAM, not North America** — see each section.

## Opportunities by region

🔵 **p899 added a *supply-side* leg to every region below.** Prior passes placed **demand**
(regulation, adoption, budgets) by region well and left **supply** — who actually builds the open
software — mostly at `Global`. This pass placed supply with an instrumented origin test
(`compose/code/p899-origin-strip/`, 36 controls) and refused to place two candidates whose
apparent regional signal turned out to be a language switcher and a supported-languages list.
**The regional supply picture that emerges is lopsided in a way worth selling against:** North
America builds the *assessment and learner-modelling infrastructure*, APAC builds the *tutors*,
EMEA builds the *institutional and curriculum-governed* systems, and LATAM builds *public-sector
data access* rather than education agents.


### North America

#### 🆕 `p928` — the two largest model vendors have made the teacher-assistant layer **free at the point of use** for US K-12, and this file had neither of them

🟢 **New to this file, both on primary vendor channels, both verified this pass.**

| Vendor | Offer | Dates | Channel |
|---|---|---|---|
| **Anthropic** | **Claude for Teachers** — free for verified US K-12 educators; then a **free *Enterprise* tier for schools and districts** with central management under one set of K-12 terms. Bundles Claude Code and Claude Cowork; integrates ASSISTments, Brisk Teaching, Canva Education, Diffit, Eedi, MagicSchool, Snorkl, TeachFX. Data not used for training; **K-12 Data Processing Addendum written to FERPA**. Evaluation planned with **Detroit Public Schools Community District**; collaboration with the **American Federation of Teachers** | individual educators **2026-07-14**, districts **2026-08-28** | `anthropic.com/news/claude-for-teachers`, `claude.com/blog`, EdWeek, EdSurge |
| **Google** | **Gemini in Workspace for Education** — Gemini features added to the **core** Education editions (Feb 2026); **Workspace Studio** (agent builder) a core service in **all** editions; Gemini in Classroom to Fundamentals/Standard/Plus, **expanded to users of all ages from 2026-08-10**; **Gemini student hub** to all ages Oct 2026, extended to the **EEA on 2026-10-19**; `Google AI Pro for Education` is the paid upgrade | Feb / Aug / Oct **2026** | `workspaceupdates.googleblog.com`, `blog.google` Bett 2026 |

🔴 **The commercial consequence, and it is the reason this belongs in a market file rather than a news log: in North America, cost is no longer an argument for open source in the teacher-assistant tier.** A district can now get a managed, FERPA-papered, centrally administered assistant from either vendor for **nothing**. Every pitch in this file that rested on licence cost has to be re-grounded on the three things the free tiers do not give: **data residency and on-device execution**, **control of the curriculum and the prompt surface**, and **the right to modify and re-licence the system**. 🔵 That is exactly the axis `agents/top.md` already shelves for: `robzilla1738/Memorwise` and `siyegs/rung` answer it architecturally, and `P52` (the offline tutoring appliance) is the pattern that sells it.

🟡 **A second-order effect worth watching rather than asserting.** Anthropic's offer is a *distribution* play into named edtech ISVs (ASSISTments, MagicSchool, Brisk and six more are integration partners, not competitors). For a studio, those integrations are the realistic **attach point** in US K-12 — the assistant is given away and the margin moves to the tools around it. This pass does not have deployment numbers for any of them and does not claim any.

🔵 **The rest of this pass's North America leg was a nil, and the named facts are listed so the nil is checkable.** `NY A 9190`, `NC Session Law 2026-41`, Maryland's dual state-guidance-plus-district-policy mandate, `Alabama H.B. 1227`, Florida `SB1194`, the **134 bills across 31 states** count, the **35+ states with departmental guidance**, the federal grant-priority rule of 2026-04-13, the student-drafted `STUDENTS FIRST Act`, and the Berkeley Law exam ban — **all ten were already held by this file.** The two vendor rows above are the only additions.


#### 🆕 `p926` — two instruments this file had not recorded, and an on-device answer to the one that bites

🟢 **New to this file.** The **US Department of Education published a *Framework for Responsible Use
and Development of Artificial Intelligence in Education* in March 2026** *(single source: Allainews
2026 guide; confirm against the primary text before it goes in a deck)*. Federal AI policy otherwise
runs through executive action rather than statute. 🟢 **Florida SB1194** — the State Board adopted a
**parental-notification** policy, joining the Florida rule requiring its **28 public colleges** to
bar AI on graded work unless the instructor permits it. Both are additions to the deadline table
above, not replacements for it.

🔵 **The commercial reading has not changed, and one of this pass's shelved rows speaks to it
directly.** The binding constraint in this region is **student data leaving the institution**, which
is what California AB 1159 and the state privacy bills are all circling.
`agents/top.md` now carries two rows that answer it architecturally rather than contractually:
**`robzilla1738/Memorwise`** (MIT) does NotebookLM-class document chat with chunking and embedding
**on the student's own machine** and a bring-your-own provider, and **`siyegs/rung`** (MIT) runs an
SAT coaching loop **entirely on the phone** — the demo asks you to cut your connection mid-session.
🟡 **Rung is aimed at the North American exam market but is not North America-origin**; this file
places it as Global and names the market here, because the two are different facts.


#### 🆕 `p925` — the regulatory surface is now the engagement, and it has dates attached

**Volume.** One tracker counts **134 AI-in-education bills introduced across 31 states in 2026**,
and **35+ states** had official AI guidance from their education departments as of June 2026. The
consistent characterisation across trackers is **guardrails rather than mandates** — states are
legislating on transparency, privacy and human oversight, not on classroom adoption.

**Dates a delivery plan can be built against** — this is the part that matters commercially, because
each one is a deadline a client must meet:

| Jurisdiction | Instrument | Deadline |
|---|---|---|
| North Carolina | Session Law 2026-41 | **model policy by 2026-12-31**; local policies by **2027-06-30**; teacher training by **2028-06-30** |
| US Dept of Education | final rule, 2026-04-13 | grant **priority** for projects advancing AI understanding or ethical use in education |
| US House | K-12 AI Literacy and Readiness Act of 2026 | advanced out of committee |

**The oversight clauses are the product requirement.** Alabama H.B. 1227 would bar AI as the
*primary basis* for grading or discipline and give parents an opt-out; Hawaii H.B. 5253 would
require parental **opt-in**; Washington DC's 2026-27 policy bars AI from grading, discipline, IEP
decisions and teacher evaluations; California AB 1159 would bar student data from training AI
models; Idaho SB 1227 would require privacy protections for school AI tools. New York A 9190 would
limit classroom AI to **ninth grade and above**, with diagnostic and special-education exceptions.
NYC Public Schools issued a **traffic-light** framework in March 2026.

🟢 **Opportunity — the compliance layer is a product, not a clause.** Every instrument above
requires the same four capabilities: (1) a **human-in-the-loop record** proving AI was not the
primary basis for a grade or a discipline decision; (2) **consent state** per student, opt-in or
opt-out depending on jurisdiction; (3) a **data-flow attestation** that student data did not reach a
training set; (4) **grade-band gating**. 🔵 None of the 19 permissive agents shelved this pass has
any of the four. That gap is buildable, sellable, and dated — North Carolina's districts need it
inside seven months. Build it on `openedx/openedx-aspects` or the LRS tier (`yetanalytics/lrsql`,
Apache-2.0) for the audit record, and gate the agent at the orchestration layer.

🔵 **`microsoft/StudentSim` (MIT, shelved this pass) is the evaluation half of the same sale.** The
US Dept of Education rule gives grant priority to *ethical use*, and the OECD line is *durable
learning gains*; a bid that can show a tutoring method was tested against simulated learners before
it reached children is answering a question the funders are now asking in writing.

🔴 **Gap, declared.** These legs returned **nothing on Canada and nothing on Mexico** — the vendor
landscape was also absent from every result. North America here means the United States. Mexico's
education supply was measured directly in `p920` (74 repositories, `agents/top.md`), and **Canada
was run as its own leg in an earlier pass** — see the *"Canada — closing the one-pilot leg gap"*
subsection below, whose finding (no national rule, formal guidance in only four provinces, nothing
province-wide in Ontario) is **unchanged and unrefreshed by this pass's legs**. 🔵 So the gap is
narrower than it looks: North America's *policy* surface is measured, its *vendor* surface is not.


#### 🆕 `p924` — one new instrument, and it regulates a *device*, not a model
🟢 **Utah H.B. 44** — new to this shelf. It lets school districts adopt policies governing **AI
glasses** in schools, scoped to safety, special education and medical need. 🔵 **Why it is worth a
row in a market file:** every other North American instrument this base tracks regulates a *use* of
a model (Oklahoma bars AI-only grading; California **AB 1159** bars training on student data at
all). This one regulates **hardware in the room** — always-on capture by a wearable — and that is a
different compliance surface, closer to recording consent than to model governance. 🔵 For a
Globant engagement it is a leading indicator rather than a constraint today: a district that has
written a wearable-capture policy has already decided who owns classroom audio and video, which is
the prerequisite conversation for any multimodal classroom product. 🔴 **Secondary source, single
leg** — read the bill text before it is quoted to a client.

#### 🆕 `p923` — one new figure, and it is a secondary one
🟡 **"Institution-wide implementation of AI has reached 66%"** — a market-research figure surfaced
by this pass's North America leg and **new to this shelf**. 🔴 File it as **secondary and
unreconciled**: the same leg returned *86% of North American educational organizations use
generative AI* from a different house, and the two are not measuring the same thing — *use somewhere*
and *implemented institution-wide* differ by roughly the whole governance problem this base
documents in `T4`. 🔵 In a proposal, quote the **gap between the two numbers**, not either one:
it is the most defensible statement of the pilots-to-production distance in the region, and it is
the distance a Globant engagement is sold to close.

Everything else the leg named was already held — ~100 state bills, Virginia S.B. 394, Illinois'
1 July 2026 deadline, the ECS policy tracker, Chegg's 45% staff cut. **Zero repositories.**

#### 🆕 `p922` — the leg ran, returned nothing new, and this line is the whole entry per `920-G3`
12 named facts from the 8 mandated legs probed mechanically against the live shelf: **12 of 12
already present** — Stanford AI Index's *6% of teachers say their school's AI policy is clear*,
the PIE Network's ~100 state bills, Virginia S.B. 394, Illinois' 1 July 2026 guidance deadline,
and the rest. **Zero repositories, forty-first consecutive nil.** 🔵 **The regional budget is
better spent on language supply than on English-language demand**, which is where it went this
pass — see the entry under *Global* below.

#### 🆕 `p921` — the leg was run and returned nothing again; this line is the whole entry, by rule

🔵 `920-G3` made this a one-line filing. The North America mandated leg returned **seven named facts,
all seven already in this file** (federal framework March 2026, Illinois' 1 July 2026 guidance
deadline, Virginia S.B. 394, Ohio's July 2026 mandate, NYC's March 2026 guidance, the Stanford AI
Index teacher-policy figure, the state-bill count)
([probe](../evidence/websearch-exhaustion-probe.2026-11-19-p921.tsv)). 🔴 **Third consecutive pass
with zero new North America facts.** `919-G7`'s budget rule holds: re-check quarterly or on a named
legislative event.

#### 🆕 `p919` — the regional leg was re-run and returned **nothing this file did not already hold**, which is itself the measurement

- 🟢 **Corroboration, not news.** A fresh North America leg returned the **134 bills across 31
  states**, **North Carolina Session Law 2026-41** (AI-literacy standards; model policy 31 Dec 2026,
  local policies 30 Jun 2027, teacher training 30 Jun 2028), **California AB 1159**, **New York
  A 9190**, **Idaho SB 1227**, **Executive Order 14277**, the Department of Education's April 2026
  K-12 guidance and OET's March 2026 responsible-AI framework, and the **April 2026 ADA web
  accessibility deadline** — every one already published in the `p918` block below, at the same
  values.
- 🔵 **Why that is worth a line rather than silence.** This base's North America regulatory picture is
  now **stable across two independent legs one day apart**. A repeated measurement that agrees is
  weak evidence that the *picture* is right and strong evidence that **the channel is exhausted** —
  the marginal regional WebSearch leg for North America is no longer buying anything, and the budget
  belongs on supply-side and non-English legs, which returned 14 unseen repositories this pass
  against this leg's zero.
- 🔴 **Mexico remains unmeasured.** Two consecutive North America legs have returned **no Mexican
  source at all**, and this file's "North America" is in practice the United States plus a single
  Canadian employment-law reference. Declared as `919-G6` rather than left to look like coverage.


#### 🆕 `p918` — the nearest deadlines are state-level, and the volume of bills is now the story

- **134 AI-in-education bills were introduced across 31 states** in the 2026 session, concentrated
  on data privacy, classroom-use limits and curriculum (MultiState legislative tracking; corroborated
  by FutureEd's 2026 state tracker). 🔵 **The buying trigger is no longer federal.**
- **Idaho SB 1227** requires a statewide framework, local policies, AI-literacy standards, educator
  training and data-privacy rules for K-12 AI tools.
- **North Carolina Session Law 2026-41** — carried since `p890`, re-corroborated this pass — state
  model policy by **31 December 2026**, local policies by **30 June 2027**, teacher training by
  **30 June 2028**.
- **New York A 9190** would restrict classroom AI use to **ninth grade and above**, with carve-outs
  for diagnostics and special education. 🔵 If it passes it is the first *age-banded* restriction in
  the region, and it invalidates a single-product K-12 pitch.
- **California AB 1159** (carried): bars training models on student data unless it directly benefits
  the school. 🔴 **This forecloses an architecture, not a workflow** — the most consequential rule in
  this file for how a studio designs a deployment.
- **The US Department of Education published a responsible-AI framework in March 2026**, alongside
  Executive Order 14277 on AI education for American youth.
- **Canada** stands as `p891` recorded it: no national education rule, formal educator guidance in
  four provinces only. 🔴 **This pass searched and found no new Canadian education-specific
  instrument** — a declared nil result, not an unsearched country.
- 🔵 **Offer:** an auditable policy-conformance layer that can be *re-pointed per state*. A client
  operating in more than one state is buying the differences, not the model.

🟢 **Opportunity added `p917` — the maths-hint layer, and it is the only new education-specific
agent 28 discovery legs produced.** `DigitalHarborFoundation/llm-math-education` (**MIT**, byte-read
1,073 B, 47 ★, pushed 2026-11-14) is placed here on `digitalharbor.org` in its `pyproject.toml`. It
generates **hints**, not answers — the output an intelligent-tutoring deployment needs — and it
composes with `CAHLR/OATutor`'s Bayesian mastery estimates, which this base already holds and which
is also North American (UC Berkeley). **The region's supply pattern from `p899` holds: North America
builds the assessment and learner-modelling layer.**

🔴 **Demand-side, re-measured `p917`.** Roughly **100 state bills** touching K-12 AI were tracked
this year and **at least 15 states** have introduced or passed AI-in-education legislation — which
for a national vendor is a **compliance-surface** problem, not a product problem, and is sellable as
one. The US Department of Education released **$169M** in FIPSE awards including responsible-AI use.
🔵 And the cautionary datum for anyone pitching homework-help: **Chegg cut 45% of staff (388 roles)**
as AI tools took its traffic. 🟡 Every figure here is from secondary reporting; the state-level
items are the better-sourced half.


🟢 **Opportunity added `p916` — the registrarial and advising tier, and it is the one North American
tier with *permissive* supply.** `p916`'s degree-audit and advising legs placed four rows in this
region by README content: `Longhorn-Developers/Degree-Audit-Plus` (**MIT**, UT Austin, pushed
2026-11-19), `Aaryan-Kapoor/degreeworks-cli` (**MIT**, Kennesaw State), `sandboxnu/graduatenu`
(GPL-3.0, Northeastern) and `chtzvt/PyEdsby` (**MIT**, for the Canadian SIS **Edsby**).
🔵 **The shape to sell:** every one of these is a bridge built *per institution* on a commercial
registrarial product — DegreeWorks, Edsby, PeopleSoft — by students, on their own credentials,
because the vendor has no agent story (`T30`). A North American university client is already running
the system and already has shadow bridges to it. **Offer the sanctioned version** (`P26`), and
`916-F3`'s fluency tier adds a K-12 line: `OSU-slatelab/AIRFluTe` is Apache-2.0 and Ohio State's.
🔴 **The retention tier, which is what this region asks for most, has no adoptable supply at all** —
see `P36` and price it as a build.


🟢 **Promoted in `p902` — three facts that had been sitting in the append-only log, unpublished.**
`p901` scored the mandated research legs as a "null yield" by grepping each fact against the whole
tree, which includes an 87,000-line log; re-scored against this file, **11 of 19 facts were missing**
([record](../evidence/surface-yield.2026-11-18-p902.tsv), method in `agents/trending.md` `902-F1`).
North America's three:

- **Virginia S.B. 394 is enacted**, directing state AI guidance that **includes teacher training**.
  It joins NC Session Law 2026-41, Oklahoma SB 1734, Ohio's 1 July 2026 framework deadline, Idaho SB
  1227, New York A 9190 and California AB 1159 in this file's US statute set — and it is the one that
  names **enablement** rather than restriction, which is the side of the ledger a studio sells into.
- **Institution-wide implementation has reached 66%** in North America (Technavio), against the 86%
  *any-use* figure this file already carries. 🔵 **The 20-point gap between "adopted" and
  "institution-wide" is the addressable market**: the buyers are past pilots and stuck on rollout.
- 🔴 **Chegg cut 45% of its staff — 388 roles.** The incumbent homework-help business model is being
  destroyed by general-purpose AI and AI search summaries. **This is the clearest commercial signal
  in this file that content-as-product is over in consumer edtech**; the money moves to institutional
  workflow, where the data and the compliance obligations sit.

🟢 **Supply side, placed p899: North America builds the assessment and learner-model layer, and
this KB had almost none of it.** Three university-built, permissively licensed systems were
verified and shelved this pass, all from the two institutions that already anchor this category:

- **`Submitty/Submitty`** — **BSD-3-Clause**, 807 ★, pushed 2026-11-18, twelve years of
  development at the **Rensselaer Center for Open Source Software, RPI**. Submission +
  autograding + TA grading + rubrics. **The most permissive full grading platform in open
  source.**
- **`CAHLR/pyBKT`** — **MIT**, 292 ★, **UC Berkeley CAHLR** (same lab as `OATutor`). Bayesian
  Knowledge Tracing: the learner-mastery model that `agents/top.md` describes as the capability
  every tutor but one lacks.
- **`ucbds-infra/otter-grader`** — **BSD-3-Clause**, 162 ★, **UC Berkeley Division of Data
  Sciences**. Python *and* R autograding that works without adopting a platform.

🔵 **The engagement consequence.** A North American higher-ed client asking for "AI grading"
should not be sold a greenfield build: **the deterministic grading substrate already exists under
BSD, from their peer institutions**, and the defensible design is an AI *assist* on the manual
tier over an unchanged deterministic autograder — which is also what several state statutes and
`EDU AI Agent Suite`'s FERPA-aligned architecture require. See `compose/patterns.md` **P13**.

🟡 **Demand side, refreshed p899 (search-mediated, secondary sources — not byte-read):**
**134 AI-in-education bills across 31 states** in the 2026 session on one tracker, with a broader
count of 45 states / 1,500+ AI bills overall. **Four states** (Maryland, Idaho, Oklahoma,
Virginia) now require *both* state guidance *and* mandatory district policy adoption. Florida's
Board of Education approved statewide AI rules with **parental opt-in**, and its Board of
Governors is weighing a rule requiring all public colleges to adopt AI-use policies — of which,
on the BOG's own presentation, **only two institutions have formal policy today**. **SUNY**
embeds AI literacy into general-education requirements for undergraduates entering **fall 2026**.
🔵 **The largest single higher-ed deployment located in any region:** **California State
University**, ChatGPT Edu to **460,000+ students and 63,000+ staff across 23 campuses** on a
reported ~$17M contract. At the restrictive end, **UC Berkeley Law bans AI for all exams and
credited coursework from Summer 2026**. 🔴 A **March 2026 White House framework** urges Congress
to pre-empt state AI regulation; whether it passed is **not established** from these sources, and
it is the single biggest swing factor in this region's procurement picture.


**Regulatory posture: state-level, binding, and fragmenting fast.** At least **25 states**
have enacted or introduced K-12 AI legislation as of spring 2026 (MultiState); bill counts
vary by tracker — one cites 134+ bills across 31 states, another 1,500+ AI-related bills
overall. There are **zero binding federal AI curriculum standards** as of May 2026. Named
statutes:

- **Idaho SB 1227** — statewide K-12 AI framework, AI-literacy standards, bar on AI replacing
  human teachers; AI literacy embedded in general education for all incoming undergraduates
  from Fall 2026.
- **Oklahoma SB 1734** — mandatory teacher review of AI output, parent opt-out; the May 2026
  law **prohibits AI tools used solely for grading, discipline or student promotion**.
- **Maryland SB 720** — state guidance plus local AI policies and a statewide K-12 AI
  collaborative.
- **Ohio** — districts must adopt an AI framework by **1 July 2026**.
- **New York A 9190** (proposed) — would restrict direct student AI use to grade 9 and above,
  **with exceptions for diagnostics and special education** (MultiState).
- **North Carolina Session Law 2026-41** (Senate Bill 257) — **new in this pass, and the
  nearest hard deadline in any region.** The Department of Public Instruction must publish a
  **model AI policy by 31 December 2026**; each public school unit must then adopt its own
  student-and-staff AI-use policy by **30 June 2027**; further obligations run through the
  **2028-29 school year**, with teacher training by **30 June 2028**. The law took effect
  1 July 2026 and required content includes AI literacy covering non-consensual intimate
  imagery. Two independent trackers plus the `ncleg.gov` session-law text agree on the
  31 December 2026 date. Separately, North Carolina has a **$10M AI-tutoring earmark for Khan
  Academy's Khanmigo**, which is locally contested. **Do not confuse SL 2026-41 with NC H 301**,
  a different bill with similar content whose status is unclear.
- **California AB 1159** — **bars the use of student data to train AI models** (MultiState).
  This is the single most architecturally consequential US rule found: it forecloses the
  fine-tune-on-your-own-students pattern and makes retrieval-over-institutional-content, with
  no training feedback loop, the compliant design.
- **Virginia** — school boards must adopt policies consistent with Department of Education
  guidance.

Federal activity is guidance and funding: the Department of Education issued *Artificial
Intelligence in K-12 Education* with UNESCO and named AI a grantmaking priority; the
**K-12 AI Literacy and Readiness Act of 2026** advanced out of House committee. District-level
bans exist too (Katy ISD bans generative AI chatbots for K-6). Higher education is tightening independently of
legislation: **Berkeley Law banned AI on all exams and credited coursework from summer 2026**.

**Canada — previously missing from this section.** "North America" in this KB had been
US-only, which is a defect for a Canadian engagement. What this pass established: there is
**no Canadian federal AI-in-education statute**; the binding instruments are provincial and
employment- or privacy-based (Ontario's **Working for Workers Four Act, 2024**, with
hiring-disclosure rules pending), and institutions are moving ahead of regulation — the
**University of Guelph** is piloting AI to help staff review supporting documents in
**international student applications** (SchoolFinder, Nov 2026). Note the exposure: admissions
document review is exactly the use the EU classes as Annex III high-risk and Vietnam now lists
as high-risk, so a Canadian pilot built without oversight architecture will not travel. This
remains a **thin leg** — one pilot and one adjacent statute is not coverage of a G7 country.

**Institutional readiness (new).** An Inside Higher Ed survey cited this pass found roughly
**70% of respondents use AI in their own work at least weekly, while only about one in ten
report a centralised institutional AI strategy** *(single source; the survey population is not
stated in the snippet, so treat the ratio as indicative)*. It is the same adoption/governance
asymmetry this KB documents for LATAM, in a market with far more money.

**Policy clarity is the measured gap, not policy existence (added p895).** The Stanford **AI
Index 2026** reports that **only 6% of teachers say their school's AI policy is clear.** Set
that beside the 25-state legislative picture above and the conclusion inverts the usual
reading: **the US problem is not an absence of rules, it is rules that never reach a
classroom-operable form.** Corroborating adoption figures from the same window: **more than 4
in 5 teens have used AI tools** with over two-thirds using them regularly (June 2026), against
reports that **about half of schools have no policy at all**.

🔵 **Commercial read.** This is the single best-evidenced opening in the North America
section, because it is a *translation* problem a studio can actually deliver: statute →
configuration → classroom-visible behaviour, with the conformance evidence attached. It is
exactly what **P3** (50-state configurable policy conformance) builds, and the 6% figure is the
number to open that conversation with. *Confidence: moderate — the AI Index figure came via
secondary reporting; the report itself was not read in this session.*

**Opportunity.** The binding constraint is *human oversight you can prove*, not model
quality. Oklahoma's "no AI-only grading" rule and the general teacher-review mandates make
**auditable human-in-the-loop architecture the product**. Build on
`virtualryder/edu-ai-agents` (MIT — deny-by-default auth, PII masking, tamper-evident audit,
FERPA/COPPA/IDEA/ADA alignment, deterministic rubric scoring rather than LLM grading) and
**Ed-Fi-ODS** (Apache-2.0), the K-12 data standard across most US states. A
**50-state policy-conformance layer** — one AI tier, per-state policy configuration — is a
genuinely defensible studio asset, because fragmentation is the client's actual pain.
Higher-ed second play: Canvas is dominant, so `canvas-mcp` (MIT) plus CAS SSO is the fastest
institutional pilot.


#### p891 additions — North America

**The dual-mandate cluster is now four states.** Maryland, **Idaho, Oklahoma and Virginia** all
require *both* state-level guidance *and* mandatory district-level AI policy adoption. That is
the pattern to design for: a vendor selling into these states must ship a **policy artefact**,
not only software, and the district is the buyer of record for it.

**Federal activity, which this KB previously recorded as near-absent, is real but non-binding.**
The US Department of Education's **Office of Educational Technology published a "Framework for
Responsible Use and Development of Artificial Intelligence in Education" in March 2026**,
followed by a **K-12 guidance document in April 2026**. Separately, **$169M in FIPSE awards**
was released, including support for responsible AI use in higher education. None of this
creates binding curriculum standards — the earlier finding stands — but it does create a
**citable federal reference** that a district policy can be written against, and a funding line.

**Two more named instruments:**

- **California AB 1159** — bars using student data to train AI models outright. The hardest
  single constraint in the region: it rules out the default fine-tuning architecture, not just
  a vendor choice.
- **Idaho SB 1227** — adds explicit privacy requirements for AI tools used in schools (this
  complements the AI-framework provisions already recorded above).

**Non-legislative forces that behave like regulation:**

- **Berkeley Law banned AI for all exams and credited coursework, effective summer 2026** — an
  elite-institution signal that propagates through peer policy.
- **Chicago, Denver and Charlotte-Mecklenburg** have issued district-level AI policies. Large
  districts are now policy *authors*, not policy *takers*.
- The **National Education Policy Center** approved a **risk-tier framework in May 2026** — a
  non-governmental classification scheme that procurement is likely to cite.
- **OpenAI and Common Sense Media** jointly proposed a California ballot measure, the
  **"Parents & Kids Safe AI Act"**, which would set standards for AI products used by minors.
  A vendor-originated standard aimed at the referendum route is a new mechanism in this market
  and worth watching.
- **Khan Academy's Khanmigo is the subject of a $10M North Carolina earmark** — the clearest
  single data point that incumbent tutors are being bought at state scale while open
  alternatives are not on the shortlist.

#### Canada — closing the "one-pilot leg" gap

Run as its own leg this pass. **The finding is that Canada has no national rule and patchy
provincial coverage, and that this is the opportunity rather than the obstacle.**

- **No national K-12 AI rule exists.** Education is provincial jurisdiction.
- **Only four provinces have formal AI guidance for educators: British Columbia, New
  Brunswick, Newfoundland and Labrador, and Quebec.** **Manitoba** is developing its own.
- **Ontario's Ministry of Education has published no memorandum on AI** — so despite being the
  largest system in the country, no province-wide rule applies. The **Ontario Teachers'
  Federation issued a discussion paper (March 2026)** pressing provincial and territorial
  governments to set direction. Demand exists; supply of policy does not.
- **Nova Scotia has no province-wide policy**, and regional education authorities are setting
  divergent expectations, leaving individual teachers to set guardrails.
- **Privacy is the binding constraint, and it is provincial:** Ontario FIPPA/MFIPPA, BC
  FOIPPA, Alberta FOIP. The practitioner guidance is privacy impact assessments, tightened
  vendor contracts and written AI-use rules. Federal, provincial and territorial privacy
  regulators issued a **joint resolution in October 2025** warning that AI may infer sensitive
  traits from student data and urging child-privacy priority in tool selection.
- **In higher education, AI detection is effectively off the table.** A review of six Canadian
  institutions found **all six declined to enable or endorse AI-detection tools**, privacy
  being the stated reason at four; **UBC** cites a Privacy Impact Assessment and **Concordia**
  bars staff and faculty from using online AI detectors. See **T10** in `intel/trends.md`.

**Opportunity — Canada.** The sellable unit is **the policy plus the privacy artefact**, not
the model. A province or board needs a PIA-backed AI-use framework, a vendor-assessment
template and a defensible assessment-redesign programme — and in six of thirteen provinces and
territories there is no provincial document to inherit from. Pair it with **sovereign/local
inference** (`ollama`/`vllm` + `litellm`), because the privacy analysis is far easier when
student work never leaves the institution. The integrity engagement must be pitched as
**assessment redesign, not detection** — detection is the thing counsel has already removed.
*Source caveat: several of these points come from vendor and advocacy blogs; the provincial
counts and institutional positions are corroborated across more than one source, the specific
legal citations are not primary-verified.*

#### p893 additions — North America: the buyer has started building a procurement gate

**Delaware's AI Assurance Lab is the first state-run evaluation body for classroom AI**, and
the state's own stated reason for building it is the commercially important part: Delaware's
education department found AI adoption already happening across its schools **"in ways that
went beyond what vendors described."** The lab evaluates tools centrally so that every district
gets the same vetted options instead of each one researching vendors alone, and the 2025
coverage says it is also intended to feed state AI standards for schools. Membership was still
being formed at announcement — school technologists, superintendents, teachers, students and
the state technology department.

**Why this is the North America finding of the pass.** Until now this KB has tracked US
regulation as *restrictions on use* (Oklahoma's no-AI-grading rule, California AB 1159's ban on
training over student data). Delaware is a different instrument: **a conformity gate in front of
procurement.** A vendor does not argue with it after deployment; it either passes the
evaluation or it is not on the menu. If the model spreads — and "first-of-its-kind" invites
copying — the deliverable shifts from a compliance memo to **an evidence pack built to survive
third-party evaluation**, which is a larger and more defensible engagement.

**The burden it exists to remove is real and measured.** Stateline (12 August 2026) found that
districts still carry most AI vetting themselves, and the standard gauntlet is a data
processing agreement, a security questionnaire, and legal, privacy and security reviews. That
is per-district, per-tool, and most districts cannot staff it.

**Legislative volume has roughly doubled year over year.** An AAAS EPI Center policy briefing
(July 2026) counts **53 AI-in-education bills across 21 states in 2025**, rising to **118 bills
across 32 states in 2026, with 25 enacted laws in 16 states**. A MultiState count from March
2026 tracked 134 bills across 31 states for the session — the counts differ by date and
methodology, so treat the direction as firm and the absolute numbers as approximate.
**Idaho, Maryland, Oklahoma and Virginia** enacted education-specific AI measures in 2026,
clustering in three areas: governance frameworks, student-use restrictions and student-data
privacy. Roughly **35 state education agencies** have issued AI guidance.

**The federal layer now pulls in two directions, and that is a planning risk to name.** The US
Department of Education finalised an **AI in Education grant priority** directing discretionary
funds to AI literacy, personalised learning and educator development, with first competitions
expected in the **2026-27 cycle**. Simultaneously a White House framework recommends that
Congress **pre-empt state AI laws** to avoid a 50-state patchwork. A client building to the
50-state-configurable pattern (`compose/patterns.md` P3) should be told plainly that the
configurability may become unnecessary — and that this is a reason to keep policy in
configuration rather than in code, not a reason to delay.

**Opportunity — North America.** Two distinct offers now exist, and they go to different
buyers. To **districts**: the vetting pack — DPA, security questionnaire responses, privacy and
legal review evidence — productised once and reused, because the Stateline finding says they
are all doing it badly and separately. To **states and vendors**: readiness for an
assurance-lab-style evaluation. The second is the higher-margin one and almost nobody is
selling it yet.


**`p896` additions — search-snippet evidence, source named.**

- 🟢 **Ohio's deadline has a second half.** Districts must adopt an AI framework by **1 July
  2026** (already recorded above), and the state undertook to publish a **model policy by the end
  of 2026**. 🔵 A published state model policy is a template an engagement can be quoted against,
  the same role the **Jisc** specification plays in EMEA (**T9**) — watch for it rather than
  drafting from scratch.
- 🟡 **Bill counts still disagree by tracker, and the disagreement is stable**: ~100 state bills
  affecting student AI use (PIE Network) against **134 bills** (MultiState, April 2026). Use the
  range, not a figure.
- 🟢 **Two primary-ish instruments now exist to quote**: the **Education Commission of the
  States' April 2026 state AI guidelines** survey, and the **CRPE *States and AI* 2026 report**,
  built from documentary evidence across **20 states** plus state-agency interviews. ECS's
  recommendations include **AI procurement policy** explicitly — the procurement thread **T9**
  tracks in EMEA is appearing in North America through state guidance rather than buyer consortia.
- 🔴 **The higher-education governance gap is the sales motion**: secondary reporting puts
  student AI use near-universal while **around 70% of universities still lack a clearly defined
  AI policy**, alongside the "campus AI deal" pattern of institution-wide contracts with model
  vendors. 🟡 Secondary-blog figure — corroborated in direction by the K-12 numbers above
  (45% of districts have any AI policy; 35% provide student AI training), not in magnitude.
- 🔵 **Adoption datapoint for the teacher-facing offer**: **85% of K-12 teachers used AI for
  lesson planning in the 2024-25 school year.** Teacher-facing tooling is the segment with
  demonstrated pull and the thinnest row count in `agents/top.md`.


#### p905 — North America: searched, nothing new

🟡 **Declared null, not silence.** The `p905` regional leg
(`AI education North America 2026 adoption regulation players`) returned 9 sources and **0 facts
absent from this file**. Re-checked and already held: the 134-bills/31-states introduction count
(🔴 still refused as a figure under `557-D` — MultiState's `134/31` disagrees with FutureEd's own
`13 enacted`, now the sixth occurrence, see `560-G`); North Carolina **Session Law 2026-41** and its
model-policy and training deadlines; the Idaho, Oklahoma, Virginia and Maryland district-policy laws;
the New York grade-9 floor and New Jersey curriculum bills; the US Department of Education's
April 2026 K-12 guidance and the March 2026 OET framework; the **K-12 AI Literacy and Readiness Act
of 2026**; California's **Parents & Kids Safe AI Act** ballot initiative; the contested **$10M
Khanmigo** earmark; the NEPC risk-level framework; and the **April 2026 ADA** accessibility deadline.
🔵 **The opportunity statement above is unchanged by this pass and that is the finding** — a region
whose policy surface stops moving between passes is a region where the *conformity product* can be
specified once and sold repeatedly (**P3**).

#### p906 — North America: searched, nothing new

🟡 **Declared null, not silence.** The `p906` leg
(`AI education North America 2026 adoption regulation players`) returned 9 sources and **0 facts
absent from the delivery files**. Re-checked and already held: the **134 bills across 31 states**
count; **North Carolina Session Law 2026-41** with its AI-literacy standards and the
2026-12-31 / 2027-06-30 / 2028-06-30 deadline ladder; **Idaho SB 1227**; **New York A 9190**
limiting classroom AI to grade 9 and above with diagnostic and special-education exceptions;
**California AB 1159** barring student data from model training; the US Department of Education's
April 2026 K-12 guidance and the Office of Educational Technology's March 2026 framework; the
**K-12 AI Literacy and Readiness Act of 2026** in committee; the OpenAI / Common Sense Media
**"Parents & Kids Safe AI Act"** California ballot initiative; **Florida's** restriction on AI in
graded work; and the North Carolina **Khanmigo** earmark. 🔵 No supply-side finding: the Mandarin
cohort this pass shelved is APAC-origin, and no North-America-origin repository surfaced that the
tree did not hold.


#### Added `p907` — three facts this file was missing on its largest region

- **Federal: a named bill, and what it would actually fund.** Rep. **Suzanne Bonamici** planned to
  introduce legislation mandating **AI risk assessment** and creating grants for **training,
  credentialing, research on AI's impact on education, and equitable AI access**. Separately a House
  committee **advanced the `K-12 AI Literacy and Readiness Act of 2026`**, and the White House has
  urged Congress to set a unified federal approach that would **preempt much of what the states have
  built**. 🔵 **The preemption threat is the commercially material part**: a 50-state configurable
  compliance product (`compose/patterns.md` **P3**) is valuable precisely because state divergence
  persists — federal preemption is the risk that would devalue it, and it is now on the record as an
  administration objective.
- **States: a public university system is about to be required to have a policy at all.** Florida's
  **Board of Governors** is weighing a rule requiring **all public colleges** to adopt policies
  covering staff and student AI use; **only two have adopted formal policy, one of them the
  University of Florida**. 🔵 This is the sharpest available datum on the *governance* gap in US
  higher ed: not that institutions have weak AI policies, but that in a large state system almost
  none have one, with a mandate arriving. That is a near-term, repeatable engagement — the same
  deliverable sold to dozens of institutions in one jurisdiction on one deadline.
- **Vendor footprint: the anchor deals are systemwide.** The **California State University** system's
  **ChatGPT Edu** rollout reached **460,000+ students and 63,000+ faculty and staff**, and
  **Northeastern joined Anthropic's "Claude for Higher Education"** initiative. 🔵 Read against
  Ellucian's 49 to 66 per cent jump in institution-wide adoption and the Inside Higher Ed finding
  that **52 per cent of presidents believe the sector is not prepared**, the picture is **procured
  first, governed second** — which is the condition `P5` was written for, and it is not only a LATAM
  condition.

🟡 **Evidence grade: search-snippet with the source named, not primary text.** Every non-GitHub host is refused at this session's egress proxy (`403` on `unesco.org`, `eur-lex.europa.eu` and `oecd.org`, all re-probed `p907`). Confirm against the primary instrument before a client deck.

#### `p908` — the dated compliance calendar, and why it is a procurement window

Measured from the `AI education North America 2026 adoption regulation players` leg. 🟡 **Sources are
legislative trackers and advocacy summaries, not statute text; bill *statuses* should be re-checked
against the official record before they go in front of a client.**

- **134 AI-in-education bills across 31 states** in the 2026 session, concentrated on student-data
  privacy, classroom-use restrictions and curriculum. Named instruments: **California AB 1159**
  (bars using student data to train AI models), **New York A 9190** (classroom AI limited to grade 9
  and above), and an **Alabama** bill requiring human oversight of high-stakes decisions.
- **35+ states** had official AI guidance from their education department as of June 2026.
- 🟢 **North Carolina Session Law 2026-41 is the one with dates**: state model policy by
  **2026-12-31**, local district policies by **2027-06-30**, teacher training by **2028-06-30**.
  **That is a three-stage, publicly-scheduled demand curve** — model policy work this quarter,
  district-level implementation through 2027, teacher enablement into 2028.
- The **US Department of Education** finalised a rule **prioritising federal education grants** for
  projects that expand understanding of AI or its appropriate and ethical use — grant-funded, so the
  buyer has money attached to the requirement.
- The **K-12 AI Literacy and Readiness Act of 2026** was advanced by the House Education and
  Workforce Committee (advanced, not enacted).
- Institutional posture at the edges: **Clark County School District** bars AI as the *sole* basis
  for high-stakes decisions; **Berkeley Law** banned AI on all exams and credited coursework.

🔴 **Declared gap, stated rather than left silent: this leg returned nothing on Canada or Mexico.**
The one "North America" regulation overview it surfaced is about the United States. Canadian
provincial ministries and Mexico's SEP are **unmeasured here**, and the `North America` reading
above should be understood as *United States*.

#### `p909` — the FIPSE commitment is quantified

🟢 This file already records the Department of Education's **FIPSE** awards as the quarter's
largest public funding commitment touching responsible AI use. The figure it lacked is
**$169 million**. 🟡 Two independent searches carried it; no primary source could be fetched this
pass (`WebFetch` failed DNS on every host tried), so it is a search-snippet figure and is labelled
as one.

🔵 **Why the amount changes the read and not just the record.** A nine-figure federal programme
whose scope explicitly includes responsible AI use is the first North American money on these
shelves that is **neither state-level guidance nor a district pilot**. The regulatory picture in
this region is 134 bills across 31 states and 35 states-plus-Puerto Rico issuing guidance — a
compliance surface with no procurement behind it. $169M is procurement. 🔵 **An engagement that
has been selling AI governance to US districts should be reading FIPSE-funded institutions as the
buyer with a budget line, and the state guidance as the specification that buyer must satisfy.**

#### `p910` — explicitly no new North America evidence this pass

🔴 **`p910`'s instrument was APAC- and EMEA-weighted and produced *no* North America supply
evidence.** The fourteen exam terms run (`906-G2`'s channel — `KSSM`, `SNBT`, `UTBK`, `TOPIK`,
`suneung`, `CSAT`, `JLPT`, `NAPLAN`, `HKDSE`, `bagrut`, `Tawjihi`, `GCSE`, `PSLE`, `SPM`) include
**no US or Canadian term**: `SAT`, `ACT`, `AP`, `Regents`, `STAAR`, `EQAO` and `CEGEP` were **not
queried**. This section is therefore unchanged by this pass, and that is a **gap in coverage, not a
finding of absence**.

🟡 **The one inference worth carrying, flagged as an inference.** In every market `p910` did
measure, open national-exam supply was *hobbyist and ungranted* while the institutional tier was
absent or government-published (Australia's `nsip/nias2`, Apache-2.0). The US has the largest
state-level standards apparatus in this file (`T11`, and the Education Commission of the States'
April 2026 guidelines) **and** the most mature open assessment infrastructure already on this
KB's shelf (`PrairieLearn`, `Submitty`, `edx-ora2`, `otter-grader`, `nbgrader`). 🔵 **If the pattern
holds, the US gap is not tooling but *alignment artefacts* — machine-readable state standards —
and that is testable with an `SAT`/`AP`/`STAAR` run of this instrument.** Registered as the
highest-value North America probe for a later pass; **not asserted here**.


🟢 **Added `p911` — the prescribed North America leg, and it is the first time this file can state
the *governance* gap as a measured number rather than as a shape.**

- 🔴 **Only `6%` of teachers say their school's AI policy is clear** — Stanford's **AI Index 2026**,
  reported via The Next Web. 🔵 **Why this is the most commercially useful number in the leg**:
  every other figure in this file measures *adoption*, and this one measures whether anyone knows
  the rules. It is the demand signal for governance work, which is the service line that does not
  depend on a district having budget for a product.
- 🔴 **More than `4` in `5` US teens have used AI tools and over two-thirds use them regularly**
  (June 2026 report, *single source*), against **half of schools having no AI policy at all**.
  🟡 Adoption has outrun governance here exactly as `T4` records for LATAM; the difference is that
  the US has a legislative response in flight and LATAM largely does not.
- 🟢 **The state-level instruments are named, and they are deadlines rather than aspirations.**
  **Illinois** requires the state board to publish district and educator AI guidance by
  **2026-07-01** (already carried in this KB — recorded here as a corroborating second channel, not
  a new fact). **North Carolina** directs its state board to adopt **K-12 AI standards** covering
  core functions and responsible use. **Virginia `S.B. 394`** directs the state education agency to
  issue guidance **including teacher training**. 🔵 Counts diverge by tracker — *"at least 15
  states"* on one, *"nearly 100 state bills this year"* on another — so the **direction** is
  multi-source and the **magnitude** is not; quote the named instruments, not the tally.
- 🟢 **Federal money has a stated AI priority with a dated competition.** The US Department of
  Education's *AI in Education* discretionary-grant priority directs funding at AI literacy,
  personalised learning and educator professional development, with **first competitions expected
  in the 2026-27 cycle**. 🔵 **This is a procurement calendar, not a trend**: it tells a studio when
  a proposal has to exist.
- 🟡 **North America is still the largest market at a reported `38%` share** (*single source*,
  secondary) **while the fastest expansion is in APAC** (OECD-based analysis). Both halves matter:
  the budget is here and the growth is not.

🔴 **Declared null for this leg, stated rather than left as silence:** no open-source North American
education artefact was surfaced by this pass. The channel that paid this pass was the
national-examination channel (`911-F1`), and **the United States has no single national examination**
for it to query — the SAT/ACT/AP tier is privately owned and its item banks are not published under
any licence. 🔵 **That is a structural property of the market, not a gap in the search**, and it is
why `agents/top.md` has no US exam-prep row to promote.

#### `p914` — North America: searched, nothing new, and the channel failure is measured this time

The leg ran (`AI education North America 2026 adoption regulation players`). **Nothing new was
admitted and nothing was invented to fill the space.** Every fact the search surfaced was already
written here — checked by string, not by impression:

| Fact the search returned | Already in this file |
|---|---|
| 134 AI-in-education bills across 31 states, 2026 | 🟢 yes (`134 bills` ×4, `31 states` ×6) |
| 35+ states with departmental AI guidance | 🟢 yes |
| US Dept. of Education final rule, 13 April 2026 | 🟢 yes — `p908` compliance calendar |
| North Carolina Session Law 2026-41 — model policy 31 Dec 2026, local policies 30 Jun 2027 | 🟢 yes (`2026-41` ×6) |
| New York A 9190 — classroom AI restricted to ninth grade and above | 🟢 yes (`A 9190` ×4) |
| `K-12 AI Literacy and Readiness Act of 2026`, advanced in committee | 🟢 yes (×5) |
| Berkeley Law AI ban on exams and credited coursework, summer 2026 | 🟢 yes (×4) |
| Hawaii proposed parental opt-in consent | 🟢 yes |

🔴 **This is the fourth consecutive nil pass for this region** (`p905`, `p906`, `p910`, `p914`), and
this pass can separate the two causes instead of guessing between them:

1. **The file is genuinely ahead of the open web here** — demonstrated above for eight specific
   facts, and this remains the region with the densest coverage in the base.
2. 🔴 **The channel was degraded, measurably.** Every non-GitHub host probed this pass was
   unreachable under the session's network policy — `curl` returned `000` to `unesco.org`,
   `eur-lex.europa.eu`, `data.consilium.europa.eu`, `oecd.org`, `future-ed.org` and
   `digitaleducationcouncil.com`. **WebSearch result summaries were the only demand-side instrument
   available, and no primary document was read.**

🔵 **Why cause 2 matters more than cause 1 for this particular region.** North America's demand
signal is *state-level and incremental*: a model policy amended, a transition date moved, a grant
priority re-weighted. A search summariser surfaces national-scale facts and compresses exactly that
class of detail away. The two legs that **did** produce rows this pass (LATAM, APAC) did so because
a national policy and a national plan are large enough to survive summarisation. 🔴 **Do not read
this leg as "North America is settled."** See `914-G3`.

#### `p915` — North America: a government-published permissive supply row

🟢 **Supply (new).** `bcgov/SIMS` — **Apache-2.0** (byte-read, 11,358 B), 29 ★, 636 open issues,
pushed 2026-11-19. The **Government of British Columbia's** post-secondary **student financial aid**
system, developed in the open. 🟢 **The first government-published, permissively licensed student
system in this base**, and the significance is not the star count: a provincial government maintaining
a real aid-and-eligibility system under Apache-2.0 makes it **citable as a reference architecture** in
any public-sector engagement *and* reusable inside a closed derivative. It also covers a tier no other
row here does — eligibility and aid, not registrar.

🟢 **Supply (new).** `Yuanpeng-Li/gradescope-mcp` — **MIT**, 8 ★. The first **Gradescope** bridge in
this base, on a platform central to North American higher-ed grading. Every write is **previewed
before it is applied**.

🟡 **Opportunity, and it is the clearest one this pass produced.** `T1`'s North American statutes
regulate **use**: Oklahoma SB 1734 bars AI as the *sole* determinant of grading, discipline or
promotion, and Maryland, Idaho, Oklahoma and Virginia require district-level AI policy adoption while
North Carolina's deadlines land 31 December 2026 and 30 June 2027. 🔵 **What that market buys is
oversight evidence, not model quality** — a per-decision audit trail showing a human decided. `P35`
builds exactly that from `gradescope-mcp`'s preview gate plus `langfuse` retention, and `bcgov/SIMS`
gives the public-sector half a permissive reference to cite. **Sell the audit trail; the grading is
the easy half.**

🔴 **Demand side: nil, fifth consecutive pass.** 134 bills / 31 states, NC Session Law 2026-41, NY
A 9190, EO 14277, the US Department of Education framework and Berkeley Law were all returned and all
already written.


#### 🆕 `p927` — the first figure this file has for how clear school AI policy is to the people inside it

🔴 **The gap this base has described as "adoption has outrun governance" now has a number from the
teacher's side.** Reporting on the **Stanford AI Index 2026** education chapter states that **only
6% of teachers say their school's AI policy is clear**, and that roughly **half of schools have no
policy at all** *(single source: TNW summarising the AI Index; confirm against the primary chapter
before it goes in a deck)*. 🔵 **Read the two together and the sale is not "write a policy" — it is
"make the policy you already have operable by a teacher on a Tuesday."** A policy that exists and
cannot be applied produces the same audit exposure as no policy, and it is a far cheaper engagement
to fix, because the governing decisions have already been taken.

🟢 **Volume and deadlines, both new to this file.** The **PIE Network** tracked **close to 100 state
bills** in the 2026 session that could directly affect students' use of AI in K-12 — a larger count
than the **134 bills across 31 states** this file already carries from MultiState, and measuring a
different thing (student-facing effect rather than all AI-in-education bills); both are recorded,
neither is averaged. Named deadlines added this pass:

- **Illinois** — the State Board of Education must **publish AI guidance for districts and
  educators by 1 July 2026**.
- **Virginia SB 394** — directs the state education agency to issue guidance explicitly covering
  **teacher training**.
- **Ohio** — Columbus City Schools adopted a district policy **ahead of** the state's July 2026
  mandate, which this file already carries.
- A **White House national AI policy framework (March 2026)** places workforce training and
  education at the centre.
- The **Education Commission of the States** published a state-by-state AI guidelines compilation
  in **April 2026** — the closest thing to a single consolidated US map, and the right primary
  source for a North America engagement.

🔵 **Why this sharpens `T11` rather than repeating it.** Every instrument above lands on the same
constraint: **teacher capacity**. Illinois and Virginia name teacher guidance and training in the
statute itself. The studio-side implication is unchanged and now better evidenced —
`compose/patterns.md` **P10** is the answer and it was written for India and Saudi Arabia. It
transfers to the US with the curriculum swapped and the compliance wrapper changed.


### EMEA

#### 🆕 `p928` — the mandated EMEA leg returned **nothing this file did not hold**, and the one thing it got *wrong* is worth more than the nil

🔴 **Zero new facts.** The leg named the EU AI Act's education high-risk classification, the UK DfE/Ofqual 2026 generative-AI and coursework-integrity materials, Dubai **KHDA** guidance to private schools, Saudi Arabia and Kazakhstan as national-competitiveness cases, the March 2026 European Parliament briefing alongside the Digital Education Action Plan, and OpenAI's government partnerships in **Estonia, Slovakia, Greece and Italy**. **Every one is already in this file.**

🟡 **The leg disagreed with itself on the date that this file sells on, and the disagreement is instructive.** One source placed the Annex III education obligations at **August 2026**; another at **2 December 2027** under the 2026 AI Omnibus. 🔵 **This file is not in doubt and should not be softened**: `intel/trends.md` `T3` carries the instrument by number — **Regulation (EU) 2026/1744**, moving stand-alone Annex III education systems from 2 August 2026 to **2 December 2027**, with Article 50 transparency duties still from August 2026 and the emotion-recognition ban in force since February 2025. 🔴 **The reading to carry into a client conversation is that secondary EMEA coverage is still publishing the superseded date**, so a client who has read the trade press may arrive believing they are already in scope. That is a conversation to have deliberately, and `T3`'s standing risk flag — the Commission may pull the date *forward* — points the same way.


#### 🆕 `p926` — the region supplied this pass's most reusable asset, and it did not come from Europe

🟢 **Two EMEA-origin rows were shelved this pass, and the more valuable one is African.**
**`clementina-tom/PLRS`** (MIT) is a prerequisite-constrained learning recommender — SAKT with
Ebbinghaus decay over a DAG constraint layer, **0% prerequisite-violation rate against 81%+ for
collaborative-filtering baselines** — and it **ships two knowledge maps built from the Nigerian
NERDC secondary-school curriculum (JSS3–SS2)**. 🔵 **That is a national curriculum graph under a
permissive licence**, which is the asset `intel/trends.md` **T26** records as existing at national
scale almost everywhere and carrying no grant almost everywhere. It joins `elimu-ai` as the second
Africa-origin permissive education asset this KB has verified, and unlike `elimu-ai` it is a
*model*, not a delivery platform.

**`tep00018/LEA-platform`** (Apache-2.0) is a tri-modal agentic STEM tutor — chat, guided tutoring
and calibrated quizzing over knowledge-component modelling — from an **MSc thesis at Abertay
University, Scotland**. 🟡 **Scope it against its own data-availability note**: the institutional
course materials, KC models, vector stores and real-course evaluation data are **not released**. The
architecture transfers; the content and the evidence do not.

🔵 **Regulatory position is unchanged from `p925` and remains the commercial clock**: the Digital
Omnibus, **Regulation (EU) 2026/1744**, moved the Annex III stand-alone high-risk obligations —
which is where admissions, student evaluation and exam scoring sit — to **2 December 2027**. Sources
still conflict on this date and it should be confirmed against the Official Journal before it goes
in a deck. The UK DfE generative-AI product safety standards (January 2026) and Ofqual's
coursework-integrity material (March 2026) are the national-level instruments underneath it.


#### 🆕 `p925` — the EU AI Act's enforcement teeth landed in August 2026, and education is named high-risk

**The regulatory fact with the most consequence.** The **AI Office gained full enforcement powers on
2026-08-02**, and the EU AI Act classifies as **high-risk** AI systems that *determine access to
education* and those that *assess learning outcomes*. 🔴 **Both of those describe the admissions
agent and the grading agent** — the two highest-demand education agents in this KB. A high-risk
classification pulls in conformity assessment, risk management, data governance, logging,
human oversight and post-market monitoring obligations; it is not a disclosure clause.

**Market size — two incompatible figures, both from secondary sources.** One puts the **European**
education-AI market at ≈ **$2.64 B in 2026**, with Finland, Estonia and the Netherlands leading K-12
integration, and **MEA at ≈ $0.56 B growing to $1.6 B by 2030**. Another reports **Sub-Saharan Africa
at 19% AI penetration**, concentrated in Kenya and Nigeria. 🔴 These do not reconcile and neither is
primary; use them for direction, not for a business case.

**Players named.** European Commission (Digital Education Action Plan); African Union (CESA 16-25);
**KHDA** and the UAE Ministry of Education in the Gulf; the **UK government**, which announced
tutoring tools for **450,000 disadvantaged children with national rollout by 2027**; **Rwanda**,
which signed a three-year MoU with Anthropic in February 2026 covering AI in health, education and
the public sector. MEA is characterised as **strategy-led rather than legislation-led** — every
government covered in one governance guide has a national AI strategy or framework, with Morocco's
legislative proposal still pending; Saudi Arabia and the UAE are described as light-touch.

🟢 **Opportunity 1 — the high-risk conformity package.** A studio that can deliver an admissions or
assessment agent **with its Annex-IV-shaped technical documentation, logging and human-oversight
design already in place** is selling the only version of that agent a European institution can
lawfully deploy after August 2026. 🔵 The permissive substrate for the audit trail already exists on
this base: `yetanalytics/lrsql` (Apache-2.0), `openfun/ralph` (Apache-2.0), and
`thm-mni-ii/feedbacksystem` (Apache-2.0, **shelved this pass**) — which is EMEA-origin, ships a Helm
chart, and is built around *personalised feedback with the institution running it*, which is the
posture the Act rewards.

🟢 **Opportunity 2 — accessibility is a tender line item, and there is exactly one open artefact.**
`ucfopen/UDOIT` (GPL-3.0, shelved this pass) scans an LMS course, reports accessibility defects and
explains the fix. European public-sector procurement routinely requires WCAG conformance. 🔴 It is
GPL-3.0, so it is `DELIVERABLE — COPYLEFT`: run it as a service beside the LMS rather than linking
it into a proprietary deliverable.

🔵 **Placement note.** `thm-mni-ii/feedbacksystem` is the only repository shelved this pass that is
**hard-placed to EMEA** (org = TH Mittelhessen, Fachbereich MNI, Germany). `chuma-beep/mathua` is
weakly placed here on a `selar.com` sponsor link (a Nigerian payments host) and should be treated as
unplaced until a second signal confirms it.


#### 🆕 `p924` — the Gulf has the most concrete classroom rule this base has met, and the **APAC** leg is what found it
🟢 **The UAE Ministry of Education issued 25 generative-AI prohibitions for schools in February
2026**, covering age suitability, privacy, academic integrity and exam restrictions. New to this
shelf. 🔵 **It is the opposite shape to everything else in EMEA.** The EU AI Act postponed
high-risk education obligations to **2 December 2027** while Article 50 disclosure and the Article 4
AI-literacy duty already bite; member states are, as this file records, fragmented to the point of
Spain having no national classroom rule at all. Against that, an **enumerated list of 25 prohibited
uses** is a specification, and a specification is something a delivery team can build a conformance
check against. 🔵 **Commercially: the Gulf is the region where "auditable human oversight is the
product" can be sold as a checklist rather than a principle.** 🔴 Secondary source, single leg —
obtain the ministry circular before quoting the number.

🔴 **And the finding carries a method warning, recorded in `agents/trending.md` `924-F11`:** this
fact was returned by the **APAC** leg. The UAE is **EMEA** in this base's closed vocabulary. The
region field is a property of the *subject*, never of the *query that found it* — file it where the
country is, or the filter silently stops meaning anything.

#### 🆕 `p923` — the EMEA leg returned **nothing new**, and that is recorded rather than left silent
🔵 All six named facts the leg produced were **already on this shelf**: Futuresource's *67% of
teachers now using AI tools*; the Epson survey (~3,360 respondents across the UK, France, Italy,
Germany, Spain and Poland, Jul–Aug 2026) and its *87% of students use AI at least weekly*;
Eurydice's *Digital education at school in Europe 2026*; the Council of Europe's education-specific
guidance work; Fosway's *vendor AI features 11% → 26%*; and Spain's absence of national classroom
AI regulation. 🔴 **Zero repositories, zero new facts** — a measured nil, not an unsearched region.

🔵 **What this means for the regional budget.** EMEA's *demand-side* English-language channel is
exhausted at this cadence — six for six, after 26-of-28 in `p921` and 12-of-12 in `p922`. The
yield this pass came from the **supply** side instead: `p922` put Finnish, Hungarian and Czech on
the deliverable list, and `p923` byte-read their catalogue tier (`repos/foundations.md`) — where
Finland's index is CC0-1.0 and Hungary's 287 ★ index carries **no grant at all**.

#### 🆕 `p922` — EMEA gains three deliverable language tiers and loses one
🟢 **Finnish, Hungarian and Czech all pass `918-R1` at the substrate layer** — measured, byte-read:
`huspacy/huspacy` **194 ★ Apache-2.0** (pushed 2026-11-16), `mikahama/uralicNLP` **101 ★
Apache-2.0** (2026-11-13), `ufal/udpipe` **426 ★ MPL-2.0** (2026-06-11, ~100 UD treebanks from one
binary). 🟡 Czech is **weak, file-level copyleft**, which is a reading a proposal must make
explicitly; it is GPL-compatible and composes with a Moodle or ILIAS plugin.
🔴 **Basque fails, and it is the result that should change how this base reasons about EMEA
public funding.** The IXA/HiTZ group at UPV/EHU is one of Europe's longest-funded NLP centres; its
largest repository is a **445 ★ English** information-extraction model and its Basque LLM
(`latxa`, 38 ★) has not been pushed in **339 days**. **A funded institution is not evidence of a
maintained vernacular stack** — check the stack.
🔵 Demand-side, nothing new: Futuresource's 67% of teachers, Epson's 80%-worried / 87%-weekly, the
Fosway 11%→26% vendor-feature move and the EU AI Act's August 2026 full-enforcement date are all
already on this shelf.

#### 🆕 `p921` — Türkiye and the Gulf acquire a supply story, and it is the substrate tier, not the agent tier

- 🔴 **This file's EMEA supply picture has been built on a verdict that named no layer.** `p903`
  measured the Arabic/Persian/Hebrew/Turkish **agent** tier — best member **6 ★**, mostly unlicensed —
  and this base reasoned from it as *"there is nothing to adopt."* `p921` measured the **substrate**
  tier in the same languages and found the two largest permissive language assets it holds outside
  East Asia:
  [`ahmetaa/zemberek-nlp`](https://github.com/ahmetaa/zemberek-nlp) — **1,379 ★, Apache-2.0
  (byte-read; the index says `NOASSERTION`), pushed 2026-11-17** — and
  [`CAMeL-Lab/camel_tools`](https://github.com/CAMeL-Lab/camel_tools) (594 ★, MIT, NYU Abu Dhabi).
  🟢 **A Türkiye or Gulf free-text-marking engagement now has a permissive stack to adopt**; the
  engagement shape is `compose/patterns.md` **P43**.
- 🆕 **New demand fact, and one of only two the eight mandated legs produced this pass.**
  **Futuresource Consulting reports 67% of teachers now using AI tools**, framing EMEA adoption as
  moving *"from experimentation to structured implementation"*, and **Fosway's 2026 EMEA AI Market
  Assessment puts vendor AI delivery at 26% of features, up from 11% in 2025**. 🟡 Both are
  **secondary-sourced** (vendor/analyst summaries; the full reports were not read) and are marked so
  under this file's standing rule.
- 🔵 **Why the pairing matters for a proposal.** Demand is institutionalising (67%, structured
  implementation) at the same moment the supply verdict flips from *nothing* to *a permissive
  parsing layer*. The gap is the pedagogy tier, which is the billable part.

#### 🆕 `p919` — the postponement corroborates for a third time, and the primary text is unreadable for a ninth pass

- 🟢 **`Regulation (EU) 2026/1744` re-corroborated on a fresh leg**: stand-alone Annex III education
  obligations at **2 December 2027**, transparency duties (Article 50) from **2 August 2026**,
  emotion-recognition ban in schools in force since **2 February 2025**.
- 🟢 **Article 4 AI literacy, stated explicitly this pass**: the obligation **has applied since 2
  February 2025 to every organisation that deploys an AI system — which is every school already using
  one**, irrespective of the 2027 high-risk date. 🔵 This is the nearest live EMEA obligation and it is
  the one most often mistaken for a future one; it is a reason to open a conversation *now* rather
  than against the 2027 window.
- 🔴 **`919-G1` — ninth consecutive pass with no primary legal text.** Re-tested this pass:
  `eur-lex.europa.eu`, `data.consilium.europa.eu` and `www.unesco.org` **all fail DNS resolution**
  from this session (`getent hosts` → no result; an HTTPS attempt returns code `000`). `915-F2`
  established the failure is DNS and not HTTP, and this pass confirms it on two further hosts. Every
  EU AI Act date in this file remains **secondary-sourced and marked so**.


#### 🆕 `p918` — the postponement holds, and the UK has moved first on product safety

- **The EU Annex III education obligations remain at 2 December 2027**, re-corroborated this pass
  against further secondary analysis. 🔴 **Primary text is still unreadable from this session**
  (`eur-lex.europa.eu` does not resolve — DNS, not HTTP; `918-G1`), so this date stays
  secondary-sourced and is marked so everywhere it appears.
- 🔵 **The live obligations are the ones nobody is selling against:** Article 50 transparency, and
  the **Article 4 AI-literacy duty, in force since 2 February 2025** for every organisation using any
  AI system. **That duty is billable today; the high-risk regime is not.**
- **UK — the sharpest new signal this pass.** The Department for Education issued **generative-AI
  product safety standards for education in January 2026**, and **Ofqual published March 2026
  guidance on AI and coursework integrity**. 🟢 A published product standard is a specification a
  studio can build and certify against — the closest thing in EMEA to the Jisc buyer-written spec in
  `README.md`.
- **Gulf:** the UAE remains policy-led, with **KHDA (Dubai)** having issued explicit responsible-use
  guidance to private schools.
- **Vendor-government partnerships are the channel into smaller EMEA systems** — OpenAI reports
  education partnerships with **Estonia, Slovakia, Greece and Italy**, centred on AI literacy and
  teacher skills. 🔵 For a studio that is a *displacement* risk at national level and an
  *implementation* opportunity underneath it.
- 🔴 **Africa: no new instrument surfaced this pass.** The region stands as `p891` and `p892`
  recorded it — covered thinly, not absently — and files under EMEA because the region vocabulary is
  closed to five values. The country is in the prose.

🟢 **Opportunity added `p917` — and it is the strongest regional asymmetry this base has measured.**
`p917` discharged `916-G4` and found that the verifiable-credential tier is not built from education
repositories at all but from the **eIDAS 2.0 / OpenID4VCI wallet estate** — eleven repositories
shelved, **ten of them Apache-2.0 or BSD**, five placed EMEA, and **three published by the European
Commission itself** (`eu-digital-identity-wallet/*`). See `repos/foundations.md`.

🔴 **Why this is an EMEA opportunity and not a global one.** EMEA is the only region with a
**statutory** driver: Europass plus eIDAS 2.0 make a learner-held, machine-verifiable diploma a
compliance target, so the build-versus-adopt question is already settled by the Commission
publishing the reference implementation under Apache-2.0. Everywhere else the same technology has to
be sold on employer-verification value. **The engagement shape is integration, not invention.**

🟡 **Demand-side, re-measured `p917`, and the regulatory date is unchanged and still unverified at
source.** Six independent secondary analyses place Annex III / education high-risk obligations at
**2 December 2027** under **Article 113(c)**; emotion recognition in schools has been prohibited
since **2 February 2025**. Adoption is high and ungoverned — a Europe-wide study of adult educators
found adoption *"largely autonomous and without a clear regulatory framework"*, with **>90% of
Spanish respondents** using AI in their work, while the Commission's own Eurydice report finds
school-level access to advanced AI *uneven*. 🔴 **Seventh consecutive pass with no primary legal
text**: `eur-lex.europa.eu` does not resolve from this environment (`917-G1`).


🟢 **Opportunity added `p916` — credentialing and in-LMS analytics, both with the copyleft question
already answered.** `openbadgefactory/salava` (**Apache-2.0**, Discendum, **Finland**) is the only
permissive Open Badges platform in open source and has been idle since 2020 — a **fork-and-own**
proposition for any EMEA client needing a white-label micro-credential product, and there is no
permissive alternative to compare it against (`916-F4`). `rwthanalytics/moodle-local_learning_analytics`
(GPL-3.0, **RWTH Aachen**) is learning analytics built *inside* Moodle by a university running it at
scale — the reference a German, Austrian or Swiss public client will recognise.
🟢 **And a second Africa-origin row:** `Kanjo-Elkamira-Ndi/Compass` (**MIT**, **Cameroon**) turns a
standard SIS into an AI advisor — after `elimu-ai`, the second African permissive row this base
holds. 🔵 **The EU AI Act framing for all of it:** education is Annex III high-risk, deferred to
2 December 2027 under Article 113(c), so the window to ship and *then* retrofit is real and closing —
sell conformity-by-design now (`P36`), not compliance later.


🟢 **Promoted in `p902` — four facts held only in the log until now** (see `902-F1`; the
[record](../evidence/surface-yield.2026-11-18-p902.tsv) lists all eleven):

- **The UK introduced generative-AI safety standards for schools in January 2026.** Non-statutory
  where the EU AI Act is binding, but it is a *procurement* gate: a supplier sells against the
  standard.
- 🔴 **The UAE Ministry of Education introduced 25 generative-AI prohibitions in schools in February
  2026**, covering age suitability, privacy, academic integrity and exam restrictions. This base
  already carried the UAE as a persona/affect-regulated market (`intel/trends.md` T14, `P13`); the
  **prohibition count and date are published here for the first time**. A deployment in the Gulf is
  scoped by an enumerated deny-list, not by a principles document — read the list before designing
  the feature.
- **DEC Leadership Summit EMEA 2026 (Paris): 41 senior leaders from 30 institutions across 14
  countries.** Small, and the useful part is the shape — EMEA buying decisions are made in
  cross-border consortia, so a reference from one institution travels further here than in NA.
- **Fosway Group published a 2026 AI Market Assessment for EMEA learning leaders** — the corporate
  L&D side of the same region, which is where `Mentingo` (MIT) and `Frappe LMS` sell.

🔵 **Placement note.** The UK and UAE facts were returned by the **APAC** search leg. They are filed
here, under this base's closed five-value region vocabulary. **A leg's name is not a region**
(`902-F1`).

🟢 **Supply side, placed p899 — and EMEA is where the *institutionally governed* code is.**

- **`oaknational/oak-ai-lesson-assistant` (Aila)** — **MIT** code, 35 ★, pushed 2026-11-18, from
  **Oak National Academy**, England's publicly funded national curriculum body. In production for
  teachers since September 2024, with an independent **NFER/EEF** evaluation run June–September
  2026. 🔵 **Multi-grant and the structure is the lesson for public-sector work:** code **MIT**,
  documentation **Open Government Licence**, **trademarks and logos excluded**. 🟡 Its README
  states it is *"intended primarily for internal use"* with no expectation of external
  contribution — **published, not maintained as a product.** **This is the only artefact in this
  KB published by a national curriculum body, and it is the reference to put in front of any
  ministry engagement.**
- **`beltromatti/get-it`** — Apache-2.0, 1,168 ★, built at **GDG AI Hack Milan 2026** (placed on
  the event, not on language). Idle since June 2026.
- Already shelved and reconfirmed: **`Selleo/mentingo`** (MIT, Poland), **`ls1intum/*`** (MIT, TU
  Munich), **`moodlehq/wiki-rag`** (BSD-3-Clause, Moodle HQ).

🟡 **Demand side, refreshed p899 (search-mediated; see the `884-G4` note under Declared gaps —
the primary texts are unreachable from this session on *every* channel).** Consistent across
sources: the **Digital Omnibus, cited as Regulation (EU) 2026/1744**, deferred the Annex III
high-risk obligations for education (admissions, grading, exam monitoring) from **2 August 2026
to December 2027**; **Article 50 transparency duties were *not* deferred and apply from 2 August
2026**; **emotion recognition in schools and universities has been prohibited since February
2025**; and **Article 4 was reworded from guaranteeing a level of AI literacy to taking measures
to support it** — a materially weaker obligation that changes what a compliance offer can
promise. Public institutions deploying high-risk systems also owe a **fundamental rights impact
assessment** (Art. 27). 🔵 **The deferral is the selling window, not a reprieve** — see T3.


**Regulatory posture: one regime, and a deadline that moved.** The EU AI Act became generally
applicable **2 August 2026**. Critically, the 2026 Digital Omnibus — cited as **Regulation
(EU) 2026/1744** — **postponed the Annex III high-risk obligations for stand-alone education
systems from 2 August 2026 to 2 December 2027**. Sources conflict on this (several
pre-Omnibus pages still say August 2026), so confirm against the regulation text before
advising a client. What is in force now:

- **Emotion recognition in schools is banned** (since February 2025, not postponed).
- **Article 50 chatbot transparency duties apply from August 2026** — a student must be told
  they are talking to an AI.
- High-risk categories when they land: **admissions, assessment/learning-outcome
  determination, educational-level assignment, and exam monitoring**.
- **Article 4 AI-literacy duty — in force since 2 February 2025 and not postponed.** New in
  this pass and the most immediately billable item in EMEA. It binds **providers *and*
  deployers**, is **not limited to high-risk systems** (a school using a general chatbot is in
  scope), and extends to staff and to contractors operating AI on the organisation's behalf.
  The Commission's position is that **supervision and enforcement began 2 August 2026**;
  sources conflict, with one arguing national enforcement started August 2025 once Member
  States had designated authorities. **Caveat:** several secondary sources say the Digital
  Omnibus *rewrote* Article 4 into a softer duty to "take measures to support the development"
  of AI literacy, dropping the "sufficient level" standard. That could not be checked against
  the Official Journal in this session — **confirm before pricing a compliance package on the
  stricter reading.** No education-specific Commission or national guidance on Article 4
  surfaced, which is itself the opening: nobody has told schools what compliance looks like.
🟢 **Added `p916` — the article, and the second deferral this file did not hold.** The 2 December
2027 education date sits in **Article 113(c)** of the consolidated AI Act; this file has carried the
date since `p890` without its locus, which is what a client's counsel asks for first. And **Annex I**
high-risk systems (safety components of regulated products) defer separately to **2 August 2028** —
six months *beyond* the Annex III education date. 🔴 Both facts are **search-snippet evidence from
six independent secondary analyses, none of them primary**: every pass since `p911` has been unable
to resolve `eur-lex.europa.eu` (`915-F2`: a DNS allowlist, not a proxy refusal). 🔵 **None of the six
mentions any Commission power to bring the date forward, and one states the education deadline is
fixed in law rather than conditional** — so `T3`'s selling window stands, at secondary-source
strength. `916-G1` carries the byte-read forward.

- **Precision on the Omnibus:** Regulation (EU) 2026/1744 has **applied since 27 July 2026**;
  the education high-risk date it sets is 2 December 2027.

Players and signals: the **European University Association** (Jan 2026 report) urges
considered adoption and **favours European LLMs** — a sovereignty preference with
procurement consequences. **That preference is now institutional, not advisory:** a
**Council of the EU** document dated **29 October 2026** (ST-14902-2026) presses **digital
sovereignty and strategic autonomy in AI for education** and calls for teacher- and
institution-level support on AI policy, and a **European Parliament briefing** of March 2026
(784574) frames public authorities and education systems as the bodies that "strategically
orchestrate" AI governance in education, pointing to the Digital Education Action Plan and the
European Education Area. Sovereignty has moved from a vendor preference to a stated Council
position inside the last month.

**New: UK procurement has organised itself against AI vendors.** **Jisc**, with **Universities
UK**, **GuildHE** and the **Association of Colleges**, issued a joint statement asking AI
suppliers for **transparent pricing, demonstrable value, meaningful institutional choice,
protection of existing functionality, granular usage and cost controls, interoperability, data
portability and safeguards against vendor lock-in** — driven by the shift from predictable
per-seat licences to **usage-based pricing**, and by institutions paying repeatedly for
overlapping AI capabilities embedded across platforms. A related Jisc/EAUC report found vendors
seldom release institution-level usage figures at all, which is why universities cannot measure
their own AI emissions. **This converts "governance" from a policy document into a metering
requirement with named deliverables**: per-institution, per-faculty, per-course usage and cost
attribution, exportable, with no proprietary trap. See `intel/trends.md` T9 and the new
observability tier in `repos/trending.md`. It is a buyer-side specification written by the
buyers — the closest thing to a published RFP this KB has found in any region. Finland's **Generation AI** project (Prof. Matti Tedre, University
of Eastern Finland) won the 2026 European Digital Skills Award. The **Russell Group's** five
AI principles remain the UK university reference model. Most institutions are in
pilot/pre-compliance mode rather than enforcement.

**Opportunity.** **The 2 Dec 2027 postponement is a 12-month selling window, not a reprieve** —
institutions now have time to do conformity properly, and budget-holders know the date. Sell
**AI Act conformity-by-construction**: Annex III classification, technical documentation,
human-oversight design and logging, built in from the start. The sovereignty preference makes
**self-hosted inference non-optional**: `ollama`/`vllm` plus `litellm` plus `qdrant`, no
US-hosted API in the data path. The permissive EMEA assets are unusually strong —
**Artemis + EduTelligence + Pyris (all MIT, TU Munich)** is the best licence-clean, EU-origin,
AI-capable LMS stack in existence, and OpenOLAT (Apache-2.0) and ILIAS serve the
German-speaking public sector. Proctoring and admissions work should be approached as
high-risk-system engineering with a 2027 compliance date, priced accordingly.


#### p891 additions — EMEA

**Article 4 is resolved — see T3 in `intel/trends.md`.** Regulation (EU) 2026/1744 (OJ 24 July
2026, in force 27 July 2026) **rewrote Article 4 rather than repealing it**, replacing "ensure
a sufficient level" with "take measures to support", and expressly disclaiming any required
level for any individual. Enforcement by **national market surveillance authorities** began
**2 August 2026**. The same instrument defers **Article 14 (human oversight)** to 2 December
2027 with the rest of Annex III. **The AI-literacy engagement survives the Omnibus but changes
shape**: sell proportionate, documented, evidenced effort — not certified competence.

**The Council of the EU has made sovereignty an education-specific position.** Its October 2026
conclusions (`ST-14902-2026`) state that reducing dependencies on AI tools developed outside
Europe — **naming education and training** — is critical, and call for policies on **academic
integrity and plagiarism**. This is the strongest procurement signal in the file: it converts
the sovereignty preference recorded above from a market sentiment into a **stated Council
priority with education named in the text**. An EU-origin, self-hostable, permissively licensed
stack is now aligned with an explicit institutional position, not merely a buyer mood.

The **European Parliament's March 2026 briefing** (`IUST_BRI(2026)784574`) sets the pedagogical
frame: AI in education must remain human-centred, and governance requires coordination across
public authorities, education systems, technology providers and researchers.

#### Africa — first dedicated leg (closing a four-pass-old gap)

This KB has filed Africa under EMEA and never searched it. Run directly this pass. **Coverage
is thin and the single most useful finding is a cautionary one.**

- **South Africa published a draft National AI Policy on 10 April 2026 — and withdrew and
  abrogated it on 27 April 2026, after the minister confirmed the draft contained fictitious
  sources in its reference list.** A national AI policy was retracted because it appears to
  have been drafted with unverified AI-generated citations. For a studio selling AI governance
  work this is the most quotable incident in the file: **it is the strongest available argument
  that provenance and verification are deliverables, not overhead** — and it happened to a
  government, in public, this year.
- **Nigeria** has a **National EdTech Strategy covering 2025–2030**, addressing power,
  broadband, devices, education data systems, teacher capacity, financing, governance and safe
  AI use. The most complete national framing found on the continent.
- **Kenya** — **M-Shule** delivers AI-backed learning over **SMS and compressed video**, which
  is the realistic architecture for the bandwidth available. Structured AI literacy at
  foundational level remains limited, with most exposure arriving informally through innovation
  hubs and private-sector partnerships.
- **Continental:** the **African Union's Continental AI Strategy (September 2024)** names
  education a strategic priority and encourages national frameworks. In **November 2026**,
  **AI Research Foundations**, a Google.org-backed programme, launched with **30 universities
  across Ghana, Kenya, Nigeria and South Africa**.

**Opportunity — Africa.** Two distinct plays. (1) **Offline-first delivery**: `kolibri` (MIT)
plus local inference is not a downgrade here, it is the only architecture that works, and this
KB already tracks the stack. (2) **Governance with verifiable provenance** — the South African
retraction created live demand and a named failure mode to sell against.
*Confidence: low-to-moderate. The South African retraction is well-corroborated; the Nigerian
and Kenyan adoption figures circulating in 2026 edtech reports could not be verified and are
deliberately omitted.*

##### Africa — the supply side, measured for the first time (p895)

Every Africa leg before this one measured **demand**. This one measured **what a studio can
actually pick up**, and the answer reshapes the opportunity above.

- 🟢 **One adoptable platform, and it is Africa-origin.**
  https://github.com/elimu-ai/webapp — **MIT** (byte-read, 1,065 B), **41 ★ / 67 forks**,
  created 2016, **pushed 2026-11-17** — early-grade literacy for out-of-school children,
  Tanzania/Kenya. Its sibling https://github.com/elimu-ai/appstore (MIT, 29 ★) **installs and
  updates Android apps with no app store and no network**. **This changes play (1) above:** the
  offline-first answer is no longer `kolibri` alone — it is `kolibri` *or* `elimu-ai`, and
  `elimu-ai` carries the regional provenance that wins a public-sector procurement. Note the
  org ships on-device **face-recognition student login** (`ml-authentication`): exclude it
  explicitly — biometric identification of children is a regime nobody budgets for.
- 🔴 **No adoptable agent layer.** The published Africa-origin tutor
  (ACL AfricaNLP 2026's EduNaija, https://github.com/Eddy-Emmanuel/EduNaija-LLM) is
  **unlicensed, 1 ★ and idle since 2025-12-22**, and its retrieval is general web search
  requiring OpenAI + Tavily — unusable where connectivity is the constraint. National-exam
  channels (`WAEC`, `KCSE`, `BECE`, `CAPS`/`IEB`) return a **~1 ★ ceiling with almost nothing
  licensed**; the highest-star find, https://github.com/Seunope/aloc-endpoints (223 ★), is an
  exam question bank with **no licence and third-party exam copyright**.
- **Therefore: adopt the platform, build the agent tier.** The agent tier is **defensible
  studio IP in this region**, not a commodity integration — the same verdict p894 reached for
  registrarial work. Delivery recipe: `compose/patterns.md` **P14**. The eval gate already
  exists: https://github.com/acheamponge/wassce-benchmark (MIT), the only African-curriculum
  open evaluation asset this KB has found.

**Governance correction worth carrying into a proposal (p895).** A 2026 governance review
(CASRAI) finds **no binding AI-specific law** across the eight MEA governments it covers —
Saudi Arabia, UAE, Egypt, Nigeria, Kenya, Rwanda, Morocco, South Africa — only strategies and
frameworks, **and it warns that some compliance trackers wrongly list these countries as
regulated.** Nigeria has a National AI Strategy and the **Nigeria Data Protection Act 2023**
(which reaches AI that processes personal data) but **no AI-specific statute**; Kenya's
Ministry of ICT published the **Kenya National AI Strategy 2025–2030 Implementation Roadmap in
December 2025**, which is policy, not law. 🔴 **Commercial consequence: do not price an
African engagement off a compliance tracker.** The binding constraints are data-protection law
and procurement rules, not an AI act — and a proposal that claims otherwise will be corrected
by the client. *Confidence: moderate; single-source for the CASRAI framing, and the primary
instruments were not read (`aclanthology.org` and most non-GitHub hosts do not resolve here).*

#### EMEA demand — three measures added p895

- **Adoption has crossed from pilots to programmes.** Futuresource Consulting puts **67% of
  teachers now using AI tools** and describes the shift as experimentation → **structured
  implementation** backed by formal policy and professional development. It also forecasts
  **AI-capable PCs at ~15% of institutional PC shipments in 2026**, higher education leading.
  🔵 **Read that as a budget signal:** structured implementation is where enablement and
  governance work gets funded, and it is what `compose/patterns.md` **P10** sells into.
- **Teacher confidence is the brake, and it is measured.** A six-country European survey of
  ~3,360 respondents (Jul–Aug 2026, commissioned by Epson) found **~80% of teachers worry AI
  is entering classrooms faster than schools can manage.** Pair with T11: capacity, not
  licensing, is the binding constraint.
- **Institutional leadership names its own gaps.** The Digital Education Council's EMEA summit
  (Paris, 2026; 41 senior leaders from 30 institutions) reported **governance and measurement**
  as the unresolved agenda items — which is the demand statement for **P7** (evidence-of-efficacy)
  and **P8** (metering and cost attribution).

*Confidence: moderate. All three are vendor- or council-commissioned research; the underlying
instruments were not read.*

#### Middle East — first dedicated leg

- **UAE, federal.** The Ministry of Education's **"Safe and Responsible Use of Artificial
  Intelligence in Classrooms 2026"** sets **25 prohibitions** on generative AI in schools. The
  central age rule **bars students under 13, and those below Grade 7, from using AI tools**, and
  a separate prohibition covers **AI during exams and assessments**. The **Cabinet approved an
  AI curriculum across public and private schools on 2 September 2026**; sources conflict on
  whether the subject became mandatory from KG–Grade 12 in 2025-26 or from August 2026, and **no
  private-school timetable has been published**.
- **Dubai, KHDA.** KHDA is preparing its own private-school AI guidelines, **expected to take
  effect for the 2027-28 academic year**. Reported design: **KHDA will not mandate specific AI
  platforms**, and will instead set safeguards schools must weigh before adopting any platform.
  Until then **Dubai private schools largely set their own AI policies**.

**Opportunity — Middle East.** The UAE is the inverse of Canada: **the mandate exists and the
implementation does not**. A curriculum is approved across public *and* private schools with no
published private-school timetable, and a platform-neutral safeguards regime arrives in
2027-28. Platform-neutral is the key commercial fact — it **favours integration and assurance
work over platform resale**, which suits a services studio and disadvantages a single-product
vendor. The deliverable is a safeguards-conformant reference implementation plus the evidence
pack: age-gating below Grade 7, exam-context lockout, and the 25-prohibition list expressed as
enforceable policy in the LMS. Age-gating and assessment-context detection are **product
requirements here, not features** — and this KB's permissive stack can implement both.
*Source caveat: the UAE detail comes from news reporting and vendor blogs; WAM, Ministry and
KHDA primary publications are blocked in this session. The 25-prohibition figure and the
under-13 rule appear in more than one outlet; the curriculum start date does not agree across
sources and is recorded as contested.*

#### Saudi Arabia — first dedicated leg (closing the gap p891 declared a search-reach failure)

p891 recorded *"Saudi Arabia returned nothing — treat as unsearched, not as absent"* and judged
a true absence implausible given Vision 2030 education spending. **That judgement was correct.**
Run as its own leg this pass, KSA returns the most concretely specified national AI-in-education
*programme* in this entire file — more specified than the UAE's, and specified as delivery
rather than as prohibition.

- **It is a curriculum build, already shipping.** The **National Curriculum Center**, with the
  **Ministry of Education**, the **Ministry of Communications and Information Technology** and
  **SDAIA**, introduced AI units across public education from the **2025–26 academic year**,
  explicitly under the **Human Capability Development Program** of **Vision 2030**. A
  foundational *Introduction to Artificial Intelligence* course for third-year secondary
  students preceded it.
- **2026–27 is an expansion, not a pilot.** Education Minister **Yousef Al-Benyan** stated that
  **22 subjects have been revised and 50 AI educational units added** for the coming academic
  year (reported 18 August 2026).
- **Teacher capacity is the stated bottleneck and is being funded as such.** **More than 240,000
  teachers** are being trained under the Human Capability Development Program, **60,000 of them
  in the past year**.
- **There is ethics guidance, and it is pro-teacher rather than prohibitive.** The Ministry of
  Education and SDAIA have issued guidance on the ethical and responsible use of generative AI
  in general education, framed around keeping teachers central to instruction.
- **SDAIA is building teacher-workload tooling with a national AI company.** Tools to reduce
  teachers' administrative burden are in technical trials with **SDAIA** and **Humain**, with
  **HADAF** involved on the workforce side.

**Opportunity — Saudi Arabia.** This is the opposite profile to every other market in this file.
Elsewhere the KB sells *governance for AI already in use* (LATAM), *conformity against a
deadline* (EMEA), or *policy configuration* (North America). **Here the state is the buyer, the
programme is funded, the curriculum is written, and the gap is delivery capacity at national
scale** — 240,000 teachers, 22 revised subjects, 50 units. The commercial shapes that fit:

1. **Teacher-enablement delivery at scale** — not courseware authoring, which the National
   Curriculum Center owns, but the training-delivery, assessment and evidence tier underneath a
   240,000-teacher programme. `moodle` or `frappe/lms` plus a retrieval tier over the Center's
   own curriculum; see **P10** in `compose/patterns.md`.
2. **Teacher administrative-workload automation**, which SDAIA has publicly named as the target
   and is trialling with Humain. An integration and assurance role around a national
   programme, not a competing product.
3. **Arabic-first retrieval and assessment.** Every tutor in `agents/top.md` is English- or
   Chinese-first. Arabic curriculum alignment is a localisation gap, not a model gap.

*Confidence: moderate. SPA (state news agency) and Saudi Gazette carry the curriculum and
minister's statements and agree with each other; the 240,000/60,000 teacher-training figures and
the SDAIA–Humain trial come from regional trade outlets. Ministry and National Curriculum Center
primary documents are blocked by this session's network policy. The 50-unit figure for 2026–27
should be confirmed against the Ministry's own announcement before it enters a client deck.*

#### Africa — addendum to the p891 leg: an open-model programme with a publication commitment

p891's Africa leg was thin by its own admission. One material addition, and it is directly
relevant because it produces **assets this KB can track rather than policy it can only cite**:

**Google DeepMind, Fab AI, Google.org and the Gates Foundation** have partnered to build
education tooling on **open Gemma models** with local innovator cohorts in **Kenya, Ghana and
South Africa**, stating an intent to **publish the resulting datasets, evaluation suites and
open-source models publicly** so others can adapt them. Google's free **AI Educator Series**
begins in **South Africa**, with **Nigeria, Kenya and Ghana in 2027**. This sits alongside the
separate **AI Research Foundations** programme already recorded (30 universities; a March 2026
DeepMind programme put Gemma and Gemini access into 15 African universities with ~$4M).

**Why it changes the Africa entry.** The continent's gap in this KB has been the absence of
*usable artefacts* — policy to cite, nothing to build on. `google-deepmind/gemma`
(**Apache-2.0**, 5,856 ★) and `google/gemma.cpp` (**Apache-2.0**, 7,088 ★) are permissive and
already verified in this KB's stack, and the partnership's output is promised under open terms.

**Opportunity — Africa, revised.** The offline-first play (`kolibri`, MIT) and the
provenance-governance play (the withdrawn South African draft policy) both stand. Add a third:
**be the integration partner for Gemma-based African education tooling** before the datasets
land. The asset is coming, it is permissively licensed, and the cohorts are local innovators
who will need delivery capacity.

*Confidence: moderate on the partnership (Google's own announcement, corroborated by regional
education press); low on timing — **no dataset name, licence or release date has been
published**, and an open-release *intent* is not an open release. Do not promise a client an
asset that does not yet exist. Re-check next pass.*

#### Africa — p894 re-check of the Gemma commitment: the commitment is now dated and named, the artefacts are still unshipped

**The gap narrows for the first time in three passes, and the verdict does not change.** Google's
own Africa blog post of **4 November 2026** states the programme in its own words rather than
through trade press: with **Fab AI, Google.org and the Gates Foundation**, bringing open
**Gemma**-powered tools and training to educators in **Kenya, Ghana and South Africa** for
foundational learning; **Fab AI leads a cohort of local innovators** across the three countries;
**Google DeepMind supplies compute credits and technical expertise**; and — the operative
sentence — *"we will share resulting datasets, evaluation suites, and open-source models
publicly so the wider education ecosystem can adapt and scale them."* A separate strand, the
**AI Educator Series**, is expanding across Sub-Saharan Africa starting with **South Africa**,
with **Nigeria, Kenya and Ghana planned for 2027**.

**What is still missing is the only thing that matters to a delivery estimate: a timeline and an
artefact.** No dataset name, no evaluation-suite name, no licence, no date. **The standing
instruction holds — do not promise a client this asset** — but the gap statement changes from
*"a commitment with nothing published"* to *"a dated, first-party commitment with a named lead
partner and an explicit public-release promise, no timeline and no artefact."* The difference is
worth recording because it is the difference between a rumour and a roadmap item: it is now
reasonable to position for integration work, and still unreasonable to scope against the data.

#### Africa — p893 re-check of the Gemma commitment: still unshipped, but the surrounding shelf is real

p891 instructed a re-check before any client-facing claim. Done, and the answer splits in two.

**The named programme has still shipped nothing.** The November 2026 Google announcement —
**Google, Fab AI, Google.org and the Gates Foundation**, supporting open Gemma-based tools and
teacher training for foundational learning in **Kenya, Ghana and South Africa**, with Fab AI
leading a cohort of local innovators — remains a commitment. The datasets, evaluation suites
and open-source models are **promised, not published**: still **no name, no licence, no release
date**. The p891 caution stands unchanged. **Do not promise a client this asset.**

**But the question "is there open, African-curriculum AI material to build on?" now has a
different answer than "wait and see."** Adjacent work has already shipped under open terms:

| Artefact | What it is | Status |
|---|---|---|
| **NILEAGI-SUB** (Cohere Labs, 2026) | Swahili language-understanding evaluation built **from school curriculum questions** — first release **2,569 expert-reviewed multiple-choice items** from the Swahili-subject curriculum, scored across eight small open models (Gemma led six of eight grade bands) | Released; private held-out split and human baselines planned |
| **AfriMMT-EA** (EACL 2026 Findings) | Multi-domain machine translation for low-resource East African languages; authors fine-tuned Gemma-3 270M/1B into **Safari-270M / Safari-1B** | Dataset and models released |
| **AfriqueLLM** (arXiv 2601.06395) | Gemma-3-12B continued-pretrained on ~26B tokens across **20 African languages** | Model suite released |
| **WAXAL** (Google) | Open speech dataset covering **21 Sub-Saharan African languages** | Released; no clear Gemma linkage |
| **`acheamponge/wassce-benchmark`** | MIT, 4 ★ — open LLMs scored on the **WASSCE**, sat by ~2 million West Africans a year | On GitHub; verified this pass, see `repos/foundations.md` |

**The revision that matters.** This KB has twice recorded Africa as a region with policy and
programmes but no technical assets. **That is no longer accurate.** Two of the five rows above
are *curriculum-derived evaluations* — NILEAGI-SUB from the Swahili curriculum, wassce-benchmark
from the West African school-leaving exam — and an evaluation built from the actual curriculum
is the single hardest artefact to produce in any education engagement. The models are
Gemma-derived and the evals are curriculum-grounded, which is exactly the pairing a localisation
build needs.

**Opportunity — Africa, revised again.** Stop waiting for the Google datasets. **The
evaluation layer already exists and nobody is building products against it.** An offline-first
Kolibri/Ollama tutor running an AfriqueLLM or Safari derivative, gated on NILEAGI-SUB and
wassce-benchmark scores, is buildable today with licensed components and is measurable against
the curriculum learners are actually examined on — which answers the efficacy-evidence hole
(**P7**) in the one region where this KB had assumed no evidence base existed.

*Confidence: high on the existence, licensing and content of the five artefacts (ACL Anthology,
arXiv and GitHub are reachable; `wassce-benchmark` was API-verified and licence byte-read).
Moderate on NILEAGI-SUB's item count and the AfriqueLLM token figure, which are from the
projects' own descriptions and were not independently reproduced.*


#### p893 additions — EMEA: the Commission has published the AI-literacy benchmark it was missing

**The AILit Framework was launched on 19 June 2026** — a joint **European Commission and OECD**
framework for AI literacy in **primary and secondary education**, developed with Code.org
(CodeAI) and international experts. It is organised in four domains — **engage with, create
with, manage, and shape AI** — and it feeds the **Innovative Domain of PISA 2029**.

**This materially changes the Article 4 position recorded in `intel/trends.md`.** That file has
carried, across several passes, the finding that *no education-specific guidance on the AI Act's
Article 4 AI-literacy duty exists* and that clients are therefore designing compliance packages
with no safe harbour. **That finding is now half wrong and needs reading precisely:**

- **What AILit is:** the first Commission-co-published, education-specific statement of what AI
  literacy actually consists of, with a competence structure a school can be assessed against.
  For the *content* of an Article 4 programme, the benchmark now exists, and a client's package
  should be mapped to its four domains rather than invented.
- **What AILit is not:** a legal safe harbour. It is a curriculum and competence framework, not
  guidance issued under the AI Act, and it names no compliance threshold. Regulation (EU)
  2026/1744 lowered Article 4 to a duty to *take measures to support* AI literacy while
  expressly disclaiming any required level for any individual — so "proportionate and
  documented" is still undefined by any authority.

**The honest formulation for a client is therefore: there is now a defensible benchmark to
build to, and still no authority that will certify you met it.** Mapping to AILit is the
strongest available evidence of proportionality. Say that, and do not oversell it.

**The Commission has also quantified the implementation gap (Eurydice, September 2026).**
Roughly **two-thirds of European education systems** now address AI through a national strategy,
guidance or policy framework, but **only about one-third include AI-related skills in the
national curriculum** — concentrated in Western and Southern Europe — and implementation remains
early-stage with uneven access to advanced AI tools. Eunews, reporting the same release, leads
on the binding constraint: **fewer than 30% of EU teachers have received AI training.**

**Read those three numbers together and they describe a single sellable sequence:** policy
exists (two-thirds), curriculum does not (one-third), and the teachers who would deliver either
are untrained (under 30%). The strategy work is largely done and the delivery work is almost
entirely undone. This is the same shape as the Saudi and Indian findings — **AI-in-education in
2026 is a delivery-capacity market, not a strategy market** — and it now holds inside the EU too.

**Country detail.** **Italy** issued school AI guidelines under its 2024–2026 national AI
strategy. **Slovakia** updates national education programmes to include AI from the **2026/27
school year**. **Romania** is reported by Romanian coverage of the Commission study as one of
only four EU countries with no AI-in-school integration policy — single-source and not verified
against the Commission text, so treat it as a lead rather than a fact. The **Council of
Europe** presented a *Compass for AI and education* in October 2025, which sits alongside the EU
instruments rather than inside them. Separately, the AI Act's **prohibition on emotion
recognition in education has applied since 2 February 2025** — already a hard design constraint,
not a forthcoming one.

**Opportunity — EMEA, sharpened.** The teacher-training number is the wedge and AILit is the
spec. An **AILit-mapped teacher AI-literacy programme with per-institution evidence of
delivery** answers the Article 4 duty with the only benchmark a regulator is likely to
recognise, and it addresses the 70%+ of EU teachers who have had no training. It is sellable in
every member state at once because the framework is supranational — which is rare in EMEA
education and is the reason to lead with it.


**`p896` additions — search-snippet evidence, source named, not byte-read primary text.**

- 🟡 **The Omnibus has a political-agreement date: 7 May 2026.** Secondary coverage of the AI
  Act simplification package dates the Council/Parliament provisional deal to **7 May 2026**,
  which is the instrument behind the postponement recorded above. The conflict in sources over
  the education high-risk date persists and is now **three-way**: 2 December 2027 (school-facing
  guides, citing Regulation (EU) 2026/1744), 2 August 2027 (university-facing coverage), and
  pre-Omnibus pages still saying August 2026. 🔴 **Do not quote a date to a client without the
  regulation text.** `intel/market.md` carries 2 December 2027 as the working figure.
- 🟢 **Article 4 was recalibrated, not removed.** Coverage of the Omnibus reports that since
  **July 2026** the AI-literacy duty no longer requires an organisation to *guarantee* any
  specific level of competence — the obligation to take measures remains. **This makes the duty
  easier to satisfy and no less mandatory**, which is the opposite of how it is usually relayed.
- 🟢 **There is now a framework to satisfy it against: the EU–OECD AI Literacy Framework,
  released 18 June 2026** — **four domains, 19 competences**. A named external framework is what
  turns "AI literacy" from a procurement adjective into a deliverable with a scope.
  `compose/patterns.md` **P10** should be quoted against it.
- 🔵 **Teachers are now a Council-level file.** The Council of education ministers approved
  **conclusions on teachers in the era of AI on 11 May 2026**, and the Commission's ethical
  guidelines update runs through the European Digital Education Hub. Teacher capacity is where
  EMEA money will move, matching the **T11** finding for India and Saudi Arabia.
- 🔵 **Demand-side figure (UK, HEPI):** **92% of students report using AI tools in their
  learning, up from 66% a year earlier.** Attributed here to EMEA because HEPI is a UK body;
  do not read it as a global number.
- 🟡 **Universities carry double duties.** Where an institution both builds its own tools and
  deploys third-party ones it is **provider and deployer at once**. That is a services
  opportunity (one conformity programme covering both roles) and the reason a university
  engagement cannot inherit a vendor's compliance posture wholesale.



#### p898 additions — EMEA

**UK: the assessment-integrity regulator has published, and it is a separate obligation from the
DfE's product standards.** **Ofqual** has issued resources on **AI and coursework integrity**,
alongside the **DfE's generative-AI product safety standards for education dated January 2026**.
*(Search-snippet evidence, two independent sources; `ofqual.gov.uk` and `gov.uk` are unreachable from
this session.)*

🔵 **The distinction a UK engagement has to get right.** These are **two different compliance
surfaces with two different owners**. The DfE standards bind the **product** — what a tool may do,
how it handles pupil data, what safety properties it must demonstrate. Ofqual's material governs the
**assessment**, meaning whether work produced with AI can count toward a qualification at all. 🔴 **A
tool can be fully DfE-conformant and still produce output that is inadmissible as coursework.**
A studio that clears only the product bar has cleared half of the UK market's requirement.

🔵 This is the UK instance of the pattern `P9` is built on — *integrity by assessment redesign, not
detection*. Ofqual's involvement means the redesign argument now has a **regulatory** counterpart in
the UK, not only a pedagogical one, which makes `P9` easier to sell there than in most markets.

#### p900 additions — EMEA: one new instrument from the Africa leg, and the first MENA-origin permissive model this base can name

🟢 **Ethiopia — Medemer Artificial Intelligence University.** The Council of Ministers approved
the draft regulation **formally establishing Medemer AI University as an autonomous public
university on 2 March 2026**. 🔵 **This is the only instrument returned by six regional legs this
pass that this base did not already hold** — the other fourteen checked facts were all present.
It is a different kind of instrument from the rest of this file: not a rule governing AI *use*
in education, but **a state building an institution whose subject is AI**. For a studio, the
reachable work is curriculum, assessment infrastructure and faculty tooling for a greenfield
public institution, which is a procurement shape rather than a compliance shape.
*(Single source — Wikipedia, citing the Council of Ministers' approval. Confirm against the
Federal Negarit Gazeta before it goes in a client deck.)*

🟢 **Middle East, supply side — `tokenaii/horus-taleeq-0.2b-base` (MIT).** An **Arabic-only
small language model** with training code and a reproducibility record published permissively,
by **TokenAI**, *"a startup and nonprofit organization focused on open Arabic AI research and
model development"*. 🔴 **It was found in this base's own unshelved ledger, not by search** — it
had been logged five times while `p899` was declaring *"no supply-side regional leg for Africa
or the Middle East"*. 🔵 **The regional gap was in promotion, not in research**, and a gap in
promotion is invisible to any instrument that measures coverage by reading the shelves. It is a
**base** model: a starting point for continued pretraining, not a deployable Arabic tutor.
Shelved in `agents/top.md`.

🟡 **What the Africa and Middle East legs could not establish this pass, stated so the silence
is not read as coverage.** Both legs returned preprints, Wikipedia and vendor blogs where the
North America and EMEA legs return law-firm analyses and primary gazettes. Two claims were
rejected rather than written: **Saudi Arabia's reported six-million-student first-year AI
rollout** (single vendor-authored source) and the **exact form of the UAE age cutoff** (sources
split between *under 13* and *below Grade 7*). The **source quality gap between regions is
itself the finding** — it is why a LATAM or MENA engagement cannot be briefed from secondary
search at the confidence a North America one can.

🟢 **`p903` measured MENA on the *supply* side for the first time, and the result reframes the
regional offer.** Every MENA entry in this file above is **demand** — a UAE mandate, 25 Emirati
prohibitions, Saudi curriculum units, 240,000 teachers in training, KHDA guidelines due for 2027-28.
`agents/top.md` had carried the matching supply question as an explicitly **untried channel**:
Arabic-language repository search. It was run this pass, across four Arabic queries plus Persian,
Hebrew and Turkish, with every licence byte-read (method and counts: `agents/trending.md` `903-F5`).

- 🟢 **The channel is populated, not empty.** Two MENA-origin education artefacts are real and were
  **absent from this entire base**: `revolover00/Bakloriya-AI-SKILLS` (Egypt — **Egypt's complete
  approved 2026/2027 curriculum**, all four stages, **300 units**, 28 MB) and
  `SalehGNUTUX/GT-MISHKATKIDS` (**GPL-3.0**, offline, zero-inference, pushed 2026-11-18).
- 🔴 **And it is commercially unusable at the top.** The highest-star Arabic education repository in
  the channel (`MjeedBakr/Student-Success-Kit`, 67 ★) and the largest (Bakloriya, 28 MB) **both carry
  no licence on any of 12 byte-read paths.** The ceiling for a *licensed* MENA education agent is
  **3 ★**.
- 🔴 **Saudi supply, counted against Saudi demand.** The Qiyas exam channel (`قدرات تحصيلي` —
  Qudurat, Tahsili) returns **12 repositories in total, all 0 ★, none licensed.** Set that beside
  this file's Saudi demand leg — 50 new curriculum units for 2026-27, 240,000 teachers — and the
  gap is not a nuance: **the most aggressive public AI-in-education programme in the region has
  essentially no open supply beneath it.**
- 🟡 **Permissive in-language *corpora* do exist, and they are the asset.** Turkish
  (`deeplearningturkiye/turkce-yapay-zeka-kaynaklari`, **2,432 ★, MIT**) and Persian
  (`barnamenevisi/free-resources`, **1,297 ★, MIT**, maintained 2026-10-11) both dwarf anything in
  Arabic, and both are content rather than software. See `repos/foundations.md`, new section.

🔵 **What this changes about the EMEA offer.** The region's binding constraint is not ideas and not
demand — it is that **MENA produces individuals where East Asia and Europe produce institutions**.
Both MENA finds are single-maintainer, zero-fork projects; the comparable entries elsewhere come out
of HKU's Data Intelligence Lab, Tsinghua, MIT Open Learning and Oak National Academy. The sellable
asset into Gulf ministries is therefore **institutional engineering around existing local
pedagogy** — licensing, evaluation, accessibility, procurement evidence, maintenance — not a
tutor built from scratch, and not a localised import either. The Egyptian corpus is the proof that
the pedagogy and the curriculum work already exists at national scale; what it lacks is everything
that makes software deliverable.

🟡 **A named EMEA framework this base does not hold: `DigComp 3.0`.** The EMEA leg returned it as
the EU's **AI-literacy framework for primary and secondary education**, cited in the Council of the
EU conclusions **ST-14902-2026 (29 October 2026)** — a document this file *already* cites, for the
separate point about reducing dependency on non-European AI. **`DigComp 3.0` returns zero hits
across this entire `intel/` tree.** It is recorded here as a **gap, not as a fact**:
`ec.europa.eu` and `data.consilium.europa.eu` are refused at the egress proxy in this session
(`403`), so its contents cannot be read and nothing about its requirements should be briefed from a
search snippet. **If AI-literacy obligations are in scope for an EU engagement, this is the first
document to obtain**, and obtaining it needs a session with open HTTP.

- **ISO/IEC 42001 is the management-system standard EMEA academic work benchmarks education AI
  against** (promoted from the research log, `p904`). 🔵 **Why it belongs in this file:** the EU AI
  Act's high-risk education obligations are deferred to **2 December 2027**, which leaves a buyer
  with nothing to point at in the meantime — and a certifiable management system is what
  procurement reaches for in that vacuum. For a studio it converts "AI governance" from a
  deliverable the client has to take on trust into an auditable artefact, and it is the cheapest
  credible answer to "how will you show us this is governed" before the Act's own conformity
  machinery exists. Pair it with `compose/patterns.md` **P4**.

#### p905 — EMEA: searched, nothing new (one global count promoted, see Global)

🟡 **Declared null, not silence.** The `p905` leg
(`AI education EMEA Europe Middle East Africa 2026 adoption regulation players`) returned 10 sources
and **0 facts absent from this file**. Re-checked and already held: the EU AI Act's Annex III
education obligations deferred to **2 December 2027** by the Digital Omnibus; the **Article 4**
AI-literacy duty in force since February 2025; **Council document ST-14902-2026** (29 October 2026)
on reducing dependence on non-European AI in education; the European Parliament briefing
**784574 (2026)**; the UK DfE's **January 2026** generative-AI product safety standards and
**Ofqual's March 2026** coursework-integrity resources; and Dubai **KHDA** guidance to private
schools. 🟢 One fact from this leg *was* an orphan — UNESCO's **68 countries** regulating AI in
education, up from 14 in 2021 — but it is a worldwide count, so it is promoted under **Global**
below rather than attributed to this region.
🔴 **The standing Africa limitation is re-confirmed:** this leg produced **no country-level African
adoption statistic**, the fifth consecutive pass to record that, and `www.unesco.org` plus
`digital-skills-jobs.europa.eu` are refused at this session's egress proxy — so the gap is a
**reach** failure, not an absence of data in the world. The Africa supply-side measurement at
`p895` remains this file's only primary-measured African content.

#### p906 — EMEA: searched, nothing new, and `DigComp 3.0` remains unreadable

🟡 **Declared null, not silence.** The `p906` leg
(`AI education EMEA Europe Middle East Africa 2026 adoption regulation players`) returned 10 sources
and **0 facts absent from the delivery files**: the EU AI Act's Annex III classification of
admissions, student evaluation and exam scoring as high-risk, with the **2 December 2027** date for
stand-alone Annex III systems under the 2026 Digital Omnibus changes (this file already carries that
instrument with its date conflict intact); the European Parliament's March 2026 briefing and the
Digital Education Action Plan; and **Dubai KHDA's** guidance to private schools. 🔴 **`DigComp 3.0`
is a named gap for a third consecutive pass** — `ec.europa.eu` and `digital-skills-jobs.europa.eu`
are still **refused at the egress proxy**, re-tested at the top of `p906`. Recorded as a gap, not as
a fact. 🟡 The snippets again carried **no EMEA adoption statistics and no named EMEA edtech
vendors**, and **Africa coverage was again thin** — consistent with the dedicated Africa and Middle
East legs in `p891`/`p900`, and still the reason the market-share gap below stays open.


#### Added `p907` — the regional leg that was missing from this file

- **The `PIO Education Model` (Catalonia) — a per-system self-assessment instrument, not a policy
  template.** Reported as *"applicable to any AI system in use or under consideration in the
  school"*, i.e. it is run **per tool**, which is the granularity the AI Act's deployer duties
  actually demand. 🔵 **Why it matters commercially:** `T11` and `P4` both assume an institution
  needs a conformity *process* built for it; Catalonia has published one. For an EMEA engagement
  this is a free, regionally credible starting artefact — and a competitor if a studio proposes to
  build the same thing from scratch. *(single source)*
- **Sweden's school leaders' union has stated that schools are already running AI systems that are
  high-risk under the AI Act**, naming **grade-recommendation tools**. 🔵 This is the clearest
  public statement by a *deployer-side* body that the December 2027 obligation already has live
  inventory behind it — useful in discovery, because it reframes AI Act work from future compliance
  to existing exposure. *(single source)*

🟡 **Evidence grade: search-snippet with the source named, not primary text.** Every non-GitHub host is refused at this session's egress proxy (`403` on `unesco.org`, `eur-lex.europa.eu` and `oecd.org`, all re-probed `p907`). Confirm against the primary instrument before a client deck.

#### `p908` — the high-risk date is still contested, and a second independent source now says 2027

Measured from the `AI education EMEA 2026 adoption regulation players` leg.

- 🔴 **The EU AI Act date conflict is live in the sources, not resolved.** Education AI used for
  admissions, assessment and exam scoring is **high-risk**. One source has the high-risk obligations
  applying from **August 2026**; another has them **delayed to 2027-12-02 under the 2026 AI
  Omnibus**. 🟢 **This base already records the December 2027 reading in [`T3`](trends.md#t3--the-eus-high-risk-deadline-moved-to-december-2027-and-that-is-a-selling-window);
  `p908` is an independent second source for it, and also evidence that the earlier date is still in
  circulation.** Neither source is the official text, so the citation a client sees must be the
  Regulation itself.
- **UK**: the Department for Education issued **generative AI product safety standards for
  education in January 2026** — a product-level conformance target, which is the most directly
  sellable compliance artefact in the region.
- **Gulf**: **KHDA (Dubai)** has issued explicit responsible-AI guidance to private schools.
- **Vendor–government partnerships** named in this leg: OpenAI education partnerships with
  **Estonia, Slovakia, Greece and Italy**, covering tool access, AI-literacy programmes and
  evaluation. 🟡 The source is a secondary write-up of OpenAI's own account.
- **EU policy frame**: the European Parliament's **March 2026 briefing** points to the **Digital
  Education Action Plan** and the **European Education Area** as the instruments that carry digital
  skills and teacher training.
- **Adoption**: QS research puts **67% of academics and 62% of students** using generative AI
  weekly. 🟡 Secondary citation; the QS instrument was not read.

🔵 **The institutional-bridge evidence places the same region from the other direction.** `p908`
filed six EMEA campus bridges built *by* university members — UNED and USC (🇪🇸), UJI (🇪🇸), TU
München (🇩🇪), SPbPU (🇷🇺), SRCE's national Croatian Moodle (🇭🇷) and Sweden's Skolverket open data
(🇸🇪). **Regulation in this region is top-down; the supply is bottom-up, and the two are not talking
to each other** — which is the gap a studio sells into.

#### `p909` — EMEA finally has named players and a measured buyer, and the UK is shipping a public specification

This region's standing weakness on these shelves has been that its **regulation** was documented
in detail and its **market** was not: who buys, and from whom, was unanswered across several
passes. `p909` closes both halves.

🔵 **The buyer is central government, by a factor of eleven.** Across **390 public
AI-in-education tenders in 25 countries**, **central government ran 124**; **individual schools,
school trusts and colleges ran 11**. A go-to-market built on per-school selling is addressing
roughly 3% of Europe's public AI-in-education money. This is the European analogue of `p576`'s
Colombia-versus-Argentina finding — **in EMEA, as in Colombia, the buyer is national.**

🟢 **The named cohort: the UK's AI Tutoring Tools Pioneer Programme** (Find a Tender
`056738-2026`), **8 × £300,000 = £2.4m**, awarded to **Medly AI, Zero Gravity Tech, Learn Anything
Education, Flint, Pearson Education, ElevenLabs, Eedi and Google UK**. Scope: **Years 9–10**,
English, maths, science and modern foreign languages, targeting pupils from underrepresented
backgrounds; awards summer 2026, national availability a **2027 ambition, not a deadline**.

🔵 **The opportunity is the specification, not the contract.** **The standard co-designed under
these contracts is owned by DSIT/i.AI and will be shared with the wider market.** A public tutoring
standard, authored by the buyer, published to everyone, landing in the window before the EU's
Annex III education obligations bite on **2 December 2027** — that is the same structure `T3`
identifies as a selling window and `T9` identifies as buyer-written spec, now with a document to
point at. 🔵 **The sellable position: be the integrator who has already built against the DSIT/i.AI
standard and can evidence Article 50 transparency, while the high-risk clock has not yet run.**

🟡 **Conflict recorded, not resolved.** One secondary source reports **six** winners from **53**
applications rather than eight awards. The eight-award figure comes from the tender notice's
awardee listing and is the one carried.

🔴 **Two programmes that failed corroboration and are deliberately not carried as facts.** Poland's
AI-lab framework (**12,000 kits**, 8,000 primary / 4,000 secondary, six suppliers, early 2026) and
France's **P2IA** (six AI services tested in classrooms since January 2026) each rest on **one**
source and **failed a second targeted search that returned nothing on either**. Recorded as open
leads with the failed query attached. 🔵 Poland and France are the two largest unmeasured EMEA
cells on this file's register; the next pass should run them in **Polish** and **French**, since
`p576` and `p374` both found that national-language press is where this material lives.

#### `p910` — national-examination supply in EMEA: two markets measured, one first-ever row

🔵 `p910`'s instrument (`906-G2`, see [`repos/trending.md`](../repos/trending.md) `p910`) was run
on two EMEA exam systems. It is **not** a regional survey — Germany (`Abitur`), France, the Gulf
and all of Africa were **not queried on this channel** — and the two results point in opposite
directions:

- 🇬🇧 **United Kingdom — `GCSE`: 2,636 nominal hits, 358 co-termed, and the tier is consumer-grade.**
  The top result by stars on `GCSE revision` is a **bookmarklet-hacks-for-school** repository
  (182 ★). The permissive finds are a resource index
  ([`StudentSuite/awesome-study-resources`](https://github.com/StudentSuite/awesome-study-resources),
  MIT, 79 forks against 39 stars) and a **GCSE/A-Level network emulator**
  ([`milesberry/networx`](https://github.com/milesberry/networx), MIT) built by a teacher. 🟡 The UK's
  open GCSE supply is pupils and teachers building revision aids, not institutions building
  platforms — which is consistent with `T9`: the buyer here has written a procurement spec, and the
  open tier has not answered it.
- 🇮🇱 **Israel — `bagrut`: 332 nominal hits, 27 co-termed, and this KB's first Israel-origin row.**
  [`peleg-jpg/israeli-bagrut-psychometric`](https://github.com/peleg-jpg/israeli-bagrut-psychometric)
  (MIT) covers both the **Bagrut** matriculation and the **Psychometric** entrance exam. 🟢 Its
  licence is the only **provenance-aware grant** this tree has found in the wild — two copyright
  lines, one for the upstream contributors and one for the packager's "security vetting and
  distribution" — which is exactly what `P24`'s handover tier argues a client should receive. 🟡
  The rest of the Israeli cohort is student final projects: real, live, and almost all ungranted.

🔴 **Declared, not implied: `DigComp 3.0` is still unreadable from this environment.**
`ec.europa.eu` and `digital-skills-jobs.europa.eu` both returned `connect_rejected` from the egress
proxy when re-tested on 2026-11-19. Third consecutive pass. The EU AI-literacy framework remains a
**gap in this file, not a fact in it**.


🟢 **Added `p911` — Africa enters this file as placed intelligence for the first time, and the
instrument that paid was the national-examination channel (`911-F1`), not a news leg.**

🔴 **Nigeria is the single most actionable procurement in this pass, in any region.** **WAEC** and
**NECO** are moving the **WASSCE to full computer-based testing**, with reports that **both the
objective *and* essay components go computer-based by May–June 2026**, delivered through
**accredited `JAMB` and `NOUN` CBT centres rather than schools**. **JAMB** separately *"rounded off
automation of question setting"* (July 2026).

- 🔵 **Why this is a Globant-shaped opportunity rather than a news item**: a national board putting
  **essay** components on screen has, by construction, created demand for **automated and
  assisted marking at national scale** — the exact capability `T21`'s permissive grading tier and
  `Gap 246`'s feature-extractor work are about. The buyer is identified, the deadline is published,
  and the delivery estate (`JAMB`/`NOUN` centres) already exists.
- 🟡 **And the risk is published with it.** Stakeholders have raised readiness objections; the CBT
  centre proprietors' association flags the cost of networked computers for schools; and one report
  refers to a **House of Representatives request to suspend computer-based WAEC until 2030**
  (*single source, detail not readable in this environment*). 🔴 **Do not price a 2026 delivery on
  the 2026 date alone** — the political risk is live and is the first thing a client will raise.
- 🟢 **Local supply exists and is permissive**, which is new to this file: `p911` byte-read and
  promoted Nigerian CBT simulators and exam-prep tools under **MIT** and **Apache-2.0** (see
  `agents/top.md`, `repos/foundations.md`). Commercial incumbents are also named — **Class54**
  (AI tools for JAMB/WAEC, *"over 300,000 students"*, self-reported) and **EDUVATE CBT** (AI topic
  tutor, 49 institutions, founder's own post) — so a studio is entering a contested market, not an
  empty one.

🟢 **Kenya — the strategy names the buyer and the teacher pipeline is already funded.** Kenya's
**National AI Strategy 2025–2030** places **higher-education institutions at the centre** of
national implementation, the OECD lists a **nationwide AI curriculum** among its measures, and the
Ministry of Education reports **more than 62,000 teachers trained in ICT integration by July 2026**.
A June 2026 Nairobi dialogue was convened specifically on the **gap between AI ambition and
institutional adoption** in higher education. 🔵 **Read commercially**: the mandate and the teacher
base exist, and the declared gap is *adoption*, which is delivery work.

🟡 **South Africa — the regulation is the least settled of the three and the institutions are the
most advanced.** The OECD's April 2026 table lists South Africa's AI policy framework as **still
under development** (**POPIA** and an **NRF AI Skills Fund** are what exist), while **the University
of Cape Town, the University of Johannesburg and the University of KwaZulu-Natal have all adopted
official institutional AI policies** — reported as **the main exception among African universities**.
**Microsoft** has a stated goal of AI and digital skills for **a million South Africans by 2026**.
🔵 **So the entry point here is institutional, not ministerial**: the universities are the ones with
a policy to implement.

🔴 **The regional frame a client will ask for, and it is unflattering in a useful way.** A study of
**47 African higher-education institutions and 199 edtech companies** (November 2025) found that
**over 83% of African AI startup funding in early 2025 went to four countries — Kenya, Nigeria,
South Africa and Egypt**, and a February 2026 report on the same study found **60% of African
universities lack an AI policy**. 🔵 **Both halves are the pitch**: capital is concentrated in
exactly the markets above, and the governance deficit is the service line.

🟡 **Germany — the framework moved in October 2026 and the exam reform is dated to 2030.** The
**KMK** adopted an update to its competency framework *Bildung in der digitalen Welt* on
**2026-10-16**, and a **"KMK-Navigator für KI-Kompetenzen"** is to be integrated into the
**shared `AIS.chat` chatbot**. 🔴 **The criticism is as load-bearing as the decision**: commentary
(GEW) notes the resolution names **neither additional resources nor binding teacher-qualification
requirements**. In **North Rhine-Westphalia**, AI use in new examination formats is foreseen under
conditions, the **APO-GOSt** draft went to the Landtag in **April 2026**, and the reform starts in
the **2027/28** school year, with the **first Abitur under the new rules in 2030**. 🔵 **`AIS.chat`
is the named state-level artefact to investigate** — a public education chatbot with a federal
framework being wired into it is the procurement shape this file should be tracking in EMEA.

🔴 **Declared nulls for this leg, because an informed gap is information:**

- **No open-source CBT or marking platform for the WAEC/NECO transition was found**, on a leg run
  specifically for it. 🔵 Remedy and cost: the supply promoted this pass is **candidate simulators,
  not board-grade delivery software**; the board-grade tier is a **build**, and that is the finding.
- **No KMK decision regulating AI in the Abitur specifically, and nothing at all on open source in
  German examination software.** The Abitur co-term leg also returned the pass's worst collision
  rate (`911-F2`), so German supply is not merely unfound — it is **unreachable on this channel**.
- 🔴 **`DigComp 3.0` — fourth consecutive pass blocked.** `ec.europa.eu`,
  `digital-skills-jobs.europa.eu` and `eur-lex.europa.eu` all returned connection failure from the
  egress proxy at `2026-11-19`. Recorded as a gap (`Gap 56`, `Gap 241`), not a fact.

🟢 **Ethiopia — queried for the first time in `p912`, discharging `911-G4`.** Ethiopia entered this
KB by accident: two Ethiopian artefacts arrived on `p911`'s South-African `matric` legs, which is a
homonym rather than a channel. Queried directly on five terms, the market reads as follows.

- **Supply exists and is the weakest this KB has measured.** `43` distinct repositories across
  `EUEE`, `NEAEA`, `Ethiopia matric`, `Ethiopian national exam` and `ethiopia grade 12`:
  🔴 **`81.4%` carry no licence file at all** (against `p911`'s `73.7%` and the curated shelf's
  `5.3%`), `70%` sit at zero stars, **none clears `100 ★`** and the ceiling is **`7 ★`**.
  🟡 **It is live, not abandoned** — `40%` pushed on or after `2026-09-01`, three within the seven
  days to `2026-11-19`.
- **The examination names are not stable in the supply itself.** The same instrument is written
  `EUEE`, `ESSLCE`, `EHSLCE` and `EAES` across repositories, and the university **exit** examination
  is a separate instrument that the acronym `EUEE` is also used for. 🔵 **Normalise the examination
  vocabulary before any item-bank or blueprint work** — this is a data-contract problem on arrival,
  not a later refinement.
- **Three promotable rows, in `agents/top.md`**: an Apache-2.0 adaptive learning platform for the
  Grade 12 examination (`7 ★`, the cohort ceiling), an MIT **offline** Grade 9–12 practice app, and
  an MIT **Telegram** results bot. 🔵 **Offline and messaging are the two delivery surfaces the
  market itself chose**, which is `T22` showing up in the poorest market measured.
- 🔴 **No ministry or agency publication.** `moe-ethiopia` resolves on the search index with `0`
  repositories; `NEAEA` does not resolve as an owner at all. **Ethiopia is a build, with no board
  interface to integrate against** — the same posture `p912` measures for every examination board
  in the table in `verticals/solutions.md`.
- 🔴 **Declared gap:** this leg measured **supply only**. No Ethiopian policy, procurement,
  connectivity or budget instrument was retrieved this pass, so the demand side of this market is
  **unmeasured** rather than absent. Carried as `912-G3`.


#### `p913` — Ethiopia's demand side, discharging `912-G3`: the market is state-led, already vendor-occupied, and power-constrained before it is model-constrained

`912-G3` recorded that `p912` measured Ethiopian **supply** only and that the demand side was
*unmeasured rather than absent*. Two dedicated regional legs were run this pass. **The gap is
discharged, and the answer reverses the engagement shape the supply finding alone would suggest.**

- 🔴 **The national-curriculum AI tier is already occupied, by an OEM, at exactly the grades this
  KB's Ethiopian rows target.** The Ministry of Education and **Huawei** began trialling a
  **national-curriculum AI teaching assistant for grades 9–12 on 2026-05-14**. `p912` promoted three
  Ethiopian rows into `agents/top.md`: an Apache-2.0 adaptive platform for the Grade 12 examination,
  an MIT **offline** Grade 9–12 practice app and an MIT Telegram results bot. 🔵 **The open tier and
  the national pilot are addressing the same grades**, and the open tier is the one with `81.4%`
  of its repositories carrying no grant at all. **The competitor in Ethiopia is not another studio
  — it is a bundled vendor programme with a ministry relationship.**
- 🟡 **The policy instruments exist and are mid-revision, which is the window.** Ethiopia's
  **National AI Policy dates from June 2024**; the **Digital Education Strategy and Implementation
  Plan 2023–2028** is in force; and the Ministry is preparing a **revised Digital Education Strategy
  and Implementation Plan for 2026/27–2030** whose published priorities are expanded digital content
  and interactive textbooks, **AI pilots**, infrastructure and connectivity, and partnerships.
  Separately, reporting from **September 2026** has the Ministry preparing a national **and
  institutional** AI policy for **higher education**, aimed primarily at online learning, and the
  Ministry is working with **UNESCO** on a national AI-in-education framework. 🔵 A strategy being
  rewritten *now*, with AI pilots named as a priority, is a specification a supplier can sell
  against — the same shape this file records for the UK and Saudi Arabia.
- 🔴 **The binding constraint is electricity and connectivity, and it is not close.** `43%` of rural
  residents have electricity against `94%` in cities and supply is frequently interrupted (BTI
  2026); the World-Bank-supported **ELEAP** programme has reached about **19,000 public facilities**
  including schools; national internet penetration was **21.7% (29.5M users) at end-2025**. The
  Digital Education Strategy targets connecting **at least half of all schools**, and its own
  implementation plan records **1,500 schools connected so far — 1,200 via SchoolNet and 300 with
  World Bank support**, with bandwidth leased from telecom operators.
  🔵 **This is the single most actionable fact in the leg.** `T22` records that open education
  agents differentiate on **delivery surface**; in Ethiopia the delivery surface is **not a
  browser**. The two Ethiopian artefacts the market itself produced are an **offline** app and a
  **Telegram** bot, which is the market stating its own constraint. **Any Ethiopian engagement is
  offline-first and store-and-forward, or it does not run** — and `P-*` patterns that assume an LMS
  reachable over the network do not apply.
- 🟡 **The 2026 framing has moved from connectivity to coordination.** Ethiopian edtech reporting
  this year argues the constraint is shifting from raw connectivity toward **fragmentation** —
  school systems that cannot share data with one another. 🔵 If that holds, the sellable work is
  **interoperability** (`repos/foundations.md` → the standards shelf: OneRoster, xAPI, QTI) rather
  than another front-end, which is a far better fit for what this KB actually holds.
- 🔴 **Still not retrieved, and named so it is not mistaken for coverage: procurement and budget.**
  No Ethiopian tender, framework agreement or federal education-budget line was returned by either
  leg. 🔵 **The named next step is specific**: the Public Procurement and Property Disposal Service,
  and the federal education budget for the current fiscal year. `912-G3` is therefore discharged on
  **policy, connectivity and the vendor landscape** and **re-registered, narrowed, as `913-G7` for
  procurement and budget alone.**

*Confidence: moderate, and lower than the GitHub measurements in this KB. The Digital Education
Strategy figures come from the strategy document and its implementation plan; the electrification
and penetration figures from BTI 2026, World Bank and telecoms reporting; the Huawei pilot, the
higher-education policy and the UNESCO framework from news reporting. **None of it is byte-verified
and the Huawei pilot in particular is a single-sourced news claim** — it is the load-bearing fact of
this leg and it should be confirmed with the Ministry before it is put in front of a client.*

#### `p914` — EMEA: searched, nothing new, and `p908`/`p909`'s contested date now has a third concurring source

The leg ran (`AI education EMEA Europe 2026 adoption regulation players`). **No new instrument,
player or figure was admitted.** What the search returned, against what is already written:

| Fact the search returned | Already in this file |
|---|---|
| EU AI Act classifies education **access and assessment** — admission, evaluation, exam scoring — as Annex III high-risk | 🟢 yes |
| The AI-**literacy** duty has applied since **2 February 2025** to every organisation using AI systems, therefore to every school | 🟢 yes |
| `Digital Omnibus on AI` published in the Official Journal **24 July 2026** as **`Regulation (EU) 2026/1744`**, deferring stand-alone Annex III obligations to **2 December 2027** | 🟢 yes (`2026/1744` ×8) |
| AI Office enforces general-purpose AI obligations, enforcement beginning 2026 | 🟢 yes |
| Council of the EU digital-sovereignty and strategic-autonomy push, **29 October 2026** (`ST-14902-2026`) | 🟢 yes |
| Guidance layer: OECD, UNESCO, Digital Education Action Plan | 🟢 yes |

🟢 **One thing did move, and it is a confidence update rather than a new fact.** `p908` recorded
the high-risk date as *contested*, with one source saying August 2026 and a second saying 2 December
2027; `p909` built `P28` around the deferral window. This pass the **2 December 2027** reading
appeared again, with the OJ publication date and regulation number attached, and the August 2026
reading appeared **only** in guidance written before the amendment. 🔵 **Three independent
secondary sources now concur and the only dissent is stale.** That is enough to stop hedging the
date in client-facing material — while still recording that 🔴 **no primary read of
`Regulation (EU) 2026/1744` has ever been performed by this base**, because `eur-lex.europa.eu` has
been unreachable in every session that tried. The deferral is the single most load-bearing date in
`P4` and `P28`, and it rests entirely on secondary sources.

🔴 **Fourth consecutive nil pass for this region**, with the same two causes as the North America
leg: genuine saturation on the instruments, plus a demand-side channel reduced to search summaries
with every primary host unreachable (`000` to all six probed). See `914-G3`, which this leg is the
strongest argument for.

#### `p915` — one supply row, and a timing risk on the EU window

🟢 **Supply (new).** `QkeleQ10/Study-Tools` — **AGPL-3.0** (byte-read, 34,523 B), 32 ★, Netherlands,
pushed 2026-11-08. A browser extension improving **Magister**, the Dutch **national student
information system**. 🔵 This is `T30` — the per-institution bridge built on the **user's own
credentials**, needing no institutional consent — landing on a *national SIS* rather than an LMS, for
the first time in this base. The system holds grades and enrolment for a whole country's schools; the
bridge is one person's browser extension. 🔴 AGPL-3.0 on a distributed extension means source
disclosure on distribution: **a pattern to learn from, not a component to bundle.**

🟡 **Opportunity, and it is a timing one.** `T3` is annotated in `p915` with an **unverified
single-source claim that the 2 December 2027 high-risk date is conditional and may be brought
forward** by the Commission once standards and guidance land. If that is right, the "selling window"
framing understates the urgency and the asymmetry favours **telling an EMEA client early**: a
conformity programme scoped to a 2027 outer limit is cheap insurance, while one scoped to a date that
moves forward is a missed deadline. 🔴 Do not state it as fact in a client deck — `915-G2` names the
primary text (Article 1 of Regulation (EU) 2026/1744) and `915-G1` records why this pass could not
read it.

🔴 **Demand side: nil, fifth consecutive pass.** Annex III classification, the Article 4 standard-drop,
`Regulation (EU) 2026/1744`, the 2 Dec 2027 deferral, Ofqual and the UK DfE product-safety standards
were all returned by this pass's EMEA leg and **all were already written here**. 🔵 Per `915-F2` the
channel cause is now measured on two independent channels and is a **DNS allowlist**, not a search
problem — so this nil is still not evidence of saturation.


#### 🆕 `p927` — European teachers are not resisting AI, they are reporting that it is arriving faster than their institution can absorb

🟢 **New to this file, and it is a procurement signal rather than a sentiment one.** An **Epson**
survey of roughly **3,360 respondents across six European countries** found **80% of teachers worry
AI is entering the classroom faster than schools can manage** *(single source; vendor-commissioned —
treat the direction as sound and the figure as indicative)*. Alongside it, **Futuresource
Consulting** reports **67% of teachers now use AI tools** and characterises 2026 as the year
adoption moved **"from experimentation to structured implementation"**, with **AI PCs at roughly 15%
of institutional PC shipments**. **Fosway Group**'s 2026 assessment records vendor AI features
rising from **11% in 2025 to 26% in 2026**.

🔵 **Put the three together and they describe one buyer.** Usage is high, institutional capacity to
govern it is the stated constraint, and **vendor AI features have more than doubled in a year** —
so the institution is absorbing new AI surface faster than it is absorbing new policy. 🟢 **That is
the Jisc specification (`T9`) restated from the supply side**, and it is why `compose/patterns.md`
**P8** — per-institution metering, cost attribution and exit — reads as a direct answer to a
published buyer requirement rather than as studio positioning.

🟢 **Two primary instruments to read before an EMEA engagement**, both new to this file:

- **Eurydice, *Digital education at school in Europe 2026*** — the Commission's own comparative
  survey of how AI and digital tooling are being integrated into school education. The right
  national-by-national baseline, and the EU's, not a vendor's.
- **Council of Europe, report of the 3rd working conference on AI and education (2026)** — builds
  on the **AI Act and GDPR** and argues for **education-specific, capacity-focused guidance**.
  🔵 Note what that implies: the Council of Europe's own position is that the AI Act **does not by
  itself** tell an education institution what to do. That is the gap a studio sells into.

🟡 **And a counter-example worth carrying, because it breaks the "EMEA means compliance" shorthand.**
Reporting in *Il Sole 24 Ore* records that **Spain has no specific national rule on classroom AI
use**, leaving adoption to individual teachers. 🔵 **EMEA is not uniform** — the regulated-market
assumption holds for the AI Act's horizontal obligations and **not** for national education rules,
which range from Vietnam-style statutory high-risk to nothing at all. Ask per country.


### APAC

#### 🆕 `p928` — nil on players and adoption; the regulatory spine re-confirmed, and this file should record that the leg **could not** find adoption data

🔴 **Zero new facts, and one honest gap.** The leg re-named **South Korea's AI Basic Act in force 2026-01-22** with a guidance-first grace period through 2026; **Vietnam's AI law effective 2026-03-01**, whose high-risk category **explicitly includes education** and requires pre-deployment registration in the **National AI Database**; Australia's absent statute alongside **TEQSA**'s requirement that providers file institutional generative-AI action plans; China as the most comprehensive current framework (registration plus labelling); and Japan, Singapore (**AI Verify**) and New Zealand on principles-and-existing-law. **All held.**

🔵 **The gap is the finding.** The leg returned **no APAC adoption figures, no school or university deployment trends, and no named regional edtech vendors** — it returned regulation and nothing else. That is the third mandated APAC leg in this base's recent history to come back regulation-only. 🔴 **An APAC engagement therefore cannot be sized from this file's demand side the way a LATAM or North America one can**, and a pass that wants to close it should go at national education ministries and the regional university associations directly rather than at English-language "APAC adoption" queries, which this base has now shown twice do not carry that data.

🟡 **One cross-region mechanism re-confirmed:** the EU AI Act reaches APAC providers whose outputs are used in the EU, so APAC-built proctoring and admissions tooling is in Annex III scope regardless of local law. That is a **sales** argument in this region, not just a compliance note.


#### 🆕 `p926` — Vietnam's registration mechanism, and the region that supplied half this pass's shelf

🟢 **New to this file: Vietnam's high-risk regime has an *operating* mechanism, not just a
classification.** Education is one of the six sectors on the high-risk list set by a **July 2026
decision**, covering automated assessment and behavioural systems, and the obligations are
procedural: **pre-deployment registration in the National AI Database**, conformity assessment,
**mandatory human oversight**, and **incident reporting within 72 hours**. Systems already operating
in education are given extra time to comply. 🔴 **Dates conflict sharply across sources** — one
gives the law an effective date of 1 March 2026, another runs education deadlines to September 2027,
a third cites March 2027 *(multiple sources, mutually inconsistent; confirm against the official
text before committing to any date in a client plan)*. 🔵 **The commercial point does not depend on
the date**: registration and 72-hour incident reporting are *build* requirements. An assessment
agent shipped into Vietnam needs an audit trail and an incident path designed in, and retrofitting
those is the expensive path.

🟢 **APAC supplied the majority of this pass's shelved rows**, and the spread is the signal — India,
China, Vietnam and Indonesia, four countries, none of them a port of the others:

- **India** — `ArushJain-697/namma-ai` (**SAKSHI**, MIT): a tutor on a **Raspberry Pi 5 with the
  network off**, shipping its own 0.6B model, **winner of the Namma AI Hackathon 2026 (Arm × IIIT
  Bangalore × NASSCOM), Problem Statement 1 — AI for Inclusive Education**. Plus
  `lagnever-learning-knowledge-graph` (MIT, CBSE/JEE curriculum graph on Neo4j, production-adjacent)
  and `vedic-math-hybrid-kt` (MIT, knowledge tracing **under noisy skill tags**).
- **China** — `xingjunm/autoppt` (MIT): interactive courseware generation driven by Claude Code or
  Codex, which **displaces this KB's standing claim** that open courseware production is AGPL-only.
  Plus `wysking/postgrad-study-engine` (MIT, 考研, per-learner forgetting-curve fitting).
- **Vietnam** — `VuongPhan-09/vuongedu` (MIT): textbook RAG with **page citations**, SM-2 spaced
  repetition over an 82-topic prerequisite graph, and a study-plan agent that **checks and repairs
  its own plan against explicit rules**. 🔵 That self-repair step is exactly the "mandatory human
  oversight"-adjacent control the registration regime above will ask about.
- **Indonesia** — `farroshsy/hcie-system` (MIT): cold-start adaptive tutoring with **no embeddings
  and no GPU**, written for the case **Indonesia created in 2025 by opening coding and AI as a
  school subject**, where every learner and every concept starts cold. Reports **AUC 0.6051** and
  says so. Plus `Litera-AI` Android/iOS (MIT).

🔵 **The regional pattern worth carrying into an engagement**: APAC's open education supply is
**constraint-shaped** — no connectivity, no GPU, no prior interaction history, a national exam to
clear. Those constraints produce architectures that transfer to any underserved market, which is why
this cohort is worth more to a global studio than its star counts suggest.


#### 🆕 `p925` — two statutes in force, education named high-risk in one, and a curriculum mandate with a period count

**Regulation is a patchwork with three shapes**, per a law-firm overview: **comprehensive**
obligations (South Korea, Vietnam), **targeted** rules (China), **light-touch** (Japan, Singapore,
Australia; Australia relies on existing law plus voluntary guidance rather than a standalone AI act).

| Jurisdiction | Instrument | In force | Education-specific |
|---|---|---|---|
| South Korea | **AI Basic Act** | **2026-01-22** | 🔴 Sources conflict on whether this is the world's *first* comprehensive AI statute or the *second* after the EU AI Act — recorded, not resolved |
| Vietnam | **Law on Artificial Intelligence** | **2026-03-01** | 🟢 **classifies education among high-risk sectors** |
| Vietnam | Decision 2422 | — | 🟢 **12 periods per class per year of AI content, grades 1–12** |
| UAE | KHDA guidance | — | explicit guidance to private schools on responsible AI use |

**Adoption, and the public mood runs against it.** The Ipsos Education Monitor 2026 found support
for *banning* AI in schools **rose in Japan, Australia and South Korea** and **fell in Indonesia**,
with Australia and New Zealand showing the highest support for a ban. 🔵 **That is a sales constraint,
not a footnote**: in ANZ the buyer's community is moving toward restriction while the institution
adopts, so the deliverable needs an off switch and an audit trail more than it needs capability.
Meanwhile **NTU Singapore** gave every undergraduate full access to Google's AI tools from
**August 2026**, and Asian universities produce the bulk of global AI research output. Southeast
Asian adoption is tied to curriculum reform — Indonesia's **Merdeka Belajar**, the Philippines'
**MATATAG**.

🟢 **Opportunity 1 — Vietnam's Decision 2422 is a content procurement with a unit of measure.**
Twelve periods × twelve grades is a **144-period AI curriculum per school**, mandated, nationwide,
and it does not exist yet. 🔵 This base holds the Vietnamese language substrate
(`undertheseanlp/underthesea`, `tuanone123/awesome-vietnamese-llm-dataset`) and
`LearnPress/learnpress` is ThimPress — a Vietnamese WordPress LMS vendor, though 🔴 its grant is
**unresolved by file** (`925-F5`), so do not build the delivery platform on it without reading
`readme.txt`.

🟢 **Opportunity 2 — APAC is where the permissive multi-tenant and billing tiers actually exist.**
Four of this pass's shelved rows are hard-placed APAC on their own description language, and two of
them fill gaps nothing else on this base fills: `3yangyang9/DeepTutor-AILearning` (Apache-2.0) is a
**multi-tenant platform with a billing-policy layer** for offline training institutions, and
`xiaochong0302/course-tencent-cloud` (GPL-2.0, 1,177 ★) is a **knowledge-payment** system explicitly
offered for commercial use under its copyleft grant. 🔵 Every other LMS on this base is single-tenant
or has no commerce tier; the APAC supply solved the business model first.

🔴 **The region's largest curriculum asset is not usable.**
`xiaoyang111222/cn-math-taxonomy` — 8,648 ★, 1,644 knowledge points, 2,403 prerequisite edges,
6,723 items, aligned to the Chinese national standard — is **`CC BY-NC 4.0`**. It is the single best
curriculum graph for the region and **it forbids commercial use**. See `925-F3`. An engagement that
needs this structure must license it from the author or rebuild it.


#### 🆕 `p924` — the APAC leg returned **no new APAC fact**, and its one new fact belongs to EMEA
🔴 **A measured nil, and an unusually clean one.** Every APAC-located fact the leg returned was
already on this shelf: the Ipsos *Education Monitor 2026* finding of lower support for school AI
bans across Asian markets; Cambridge English's May 2026 Asia-Pacific ministerial summit; the World
Bank **Global EdTech Policy Academy, Seoul, 31 Aug – 4 Sep 2026**; and the regional-share and
China/Japan revenue-pool framing. 🔴 The leg's **only** new concrete instrument — the UAE Ministry of
Education's 25 generative-AI prohibitions — is **EMEA**, and is filed there (`924-F11`).

🟢 **Where APAC did move is the substrate layer, not the market layer.** `p924`'s second-shape probe
confirmed the **Philippines/Tagalog** tier as the one APAC language tier with a maintained,
permissive, *general* NLP stack — `ljvmiranda921/calamanCy`, 77 ★, MIT, re-read hash-identical this
pass. For a Philippine BPO or public-education engagement that is the difference between localising
and building. 🔴 It also carries a licence trap this file should state plainly: calamanCy's **code**
is MIT, but its **training corpora are not** — TLUnified is GPL-3.0 and UD_Tagalog-Ugnayan is
CC-BY-NC-SA-4.0. 🔵 **A model trained on a non-commercial corpus is not a commercial deliverable**,
whatever the code licence says. Run licence triage per artefact class (`T25`), not once.

#### 🆕 `p923` — the regional-share figure, and why it is quotable in only one direction
🟡 **"APAC is over 45% of global EdTech market share"** — new to this shelf, from a vendor-adjacent
analyst blog. 🔴 It is **EdTech**, not AI-in-education, and it is a share claim with no stated
denominator, so it does not belong in a sizing slide. 🟢 It *is* usable as a **prioritisation**
argument, where it agrees with three figures this base already holds from independent sources
(China as the largest country revenue pool, India as the fastest-growing, APAC as the fastest
expansion against a North American revenue lead). 🔵 When four houses disagree on the number and
agree on the ranking, **sell the ranking**.

🔵 The rest of the leg was already held: the UAE's 25 generative-AI school prohibitions (Feb 2026),
the World Bank's Seoul Global EdTech Policy Academy (31 Aug – 4 Sep 2026), Cambridge English's
May 2026 Asia-Pacific summit, the Ipsos education monitor, EdTech Hub's Southeast Asia briefs, and
the 30% virtual-tutor adoption figure.

#### 🆕 `p922` — the Philippines is open for a vernacular engagement and Cambodia and Laos are not
🟢 **Tagalog/Filipino passes.** `ljvmiranda921/calamanCy` — **77 ★, MIT, pushed 2026-10-05**,
spaCy pipelines trained on Universal Dependencies and TLUnified. 🔴 **This base had predicted this
tier was dead**, which matters commercially: the Philippines is a major APAC delivery and BPO
market and the stack is permissive and maintained.
🟢 **Bengali passes** — `sagorbrur/bnlp`, **313 ★ MIT**, pushed 19 days ago, ~270 M speakers across
Bangladesh and West Bengal.
🔴 **Khmer and Lao do not.** Khmer's general artefact (`khmer-nltk`, 86 ★ Apache-2.0) is **247 days
idle** and its only live ≥50 ★ member is an **ungranted** catalogue; Lao's `LaoNLP` is maintained
and Apache-2.0 but **35 ★**, failing on size alone. 🔵 **Lao is the cheapest tier on this shelf to
change**: one engagement's upstream contribution would carry it past `918-R1`.
🟢 **Indonesian re-probed and unchanged** — `har07/PySastrawi` still 2026-05-21, now **182 days**,
two days outside the window. The threshold was not renegotiated.
🔵 Demand-side, nothing new: Arizton's >45% APAC share of global EdTech and the UAE's 25
generative-AI school prohibitions (Feb 2026) are both already held.

#### 🆕 `p921` — Indonesia and India measured at the substrate layer: both empty, and the Indian national catalogue is ungranted

- 🔴 **Indonesia (`920-G4` discharged).** Five candidates byte-read; **every one fails `918-R1`**.
  `IndoNLP/indonlu` (659 ★, Apache-2.0) is **733 days idle**; `Wikidepia/indonesian_datasets`
  (131 ★) carries **no licence file**. 🟡 Nearest miss in the entire ten-tier measurement:
  `har07/PySastrawi` (366 ★, MIT) at **182 days — two days outside the window.**
- 🔴 **India, measured at this layer for the first time.** The largest education market this file
  tracks had **no substrate verdict at all**. All four candidates fail: `goru001/inltk` (838 ★,
  1,034 days idle), `anoopkunchukuttan/indic_nlp_library` (654 ★, 895 d),
  `AI4Bharat/IndicTrans2` (497 ★, 412 d), and **`AI4Bharat/indicnlp_catalog` — 641 ★ and carrying
  no licence file on any of 25 probed paths.**
- 🔵 **Read with `p920`'s APAC finding, this is the regional shape:** East and Southeast Asia's
  *hard-tokenising* languages have maintained permissive substrates (`HanLP` 36,539 ★, `PyThaiNLP`,
  `Kiwi`, `underthesea`, `vibrato`); the region's two largest *easy-tokenising* markets have none.
  **Market size predicts the opposite of what is true here** — see `intel/trends.md` **T55** and
  `compose/patterns.md` **P44**.
- 🆕 **New demand fact (second of the two from the mandated legs).** **Arizton (June 2026) puts APAC
  at over 45% of the global EdTech market**, with growth driven by government programmes and
  enterprise demand; MarketsandMarkets' APAC AI-in-education line ($591.6 M 2024 → $1,848.1 M 2029)
  is already in this file. 🟡 Secondary-sourced, marked so.


#### 🆕 `p920` — the APAC language substrate is permissive, maintained, and was invisible to 919 passes of education-shaped searching

🟢 **All four APAC vernacular tiers that `p918` graded `PRESENT — NOT DELIVERABLE` at the agent layer
pass at the substrate layer** — the layer that makes a student's answer parseable at all
([record](../evidence/apac-substrate-layer.2026-11-19-p920.tsv)). Best member per language, every
grant byte-read this pass: **Mandarin** `hankcs/HanLP` **36,539 ★** Apache-2.0 (pushed 2026-11-07);
**Vietnamese** `undertheseanlp/underthesea` 1,818 ★ Apache-2.0 (2026-11-19); **Korean**
`bab2min/Kiwi` 810 ★ Apache-2.0 (2026-11-16); **Japanese** `daac-tools/vibrato` 431 ★ MIT *or*
Apache-2.0 (2026-10-25).

- 🔴 **HanLP is larger than every education agent this base holds except DeepTutor and OpenMAIC**, and
  it had never appeared in 919 passes — because every prior Mandarin leg asked for *education*.
- 🔴 **Two licence facts that change what may be built.** `konlpy/konlpy` (1,490 ★), the package most
  Korean NLP teaching uses, reports `NOASSERTION` on the search channel and byte-reads as
  **GPL-3.0-or-later** — a closed Korean tutor that imports it inherits that. And `taku910/mecab`
  reports as ungranted on both channels while being **tri-licensed GPL-2.0 / LGPL-2.1 / BSD-3-Clause**
  in a subtree file, so a closed Japanese build *is* permitted via the BSD arm.
- 🔴 **The Japanese dictionary is a separate work with a separate owner.** UniDic is BSD, © The UniDic
  Consortium, in `LICENSE.unidic`; IPAdic is a bespoke NAIST/ICOT text that is not an OSI licence.
  Budget licence triage per artefact, not per repository.
- 🔵 **What this means for an APAC engagement:** there is no vernacular tutor to fork in any of these
  markets, and there is a maintained permissive language stack to build one on in all four. The
  engagement is a build, and the substrate is free.

#### 🆕 `p919` — Indonesia's "no supply" was a query artefact; Thailand's is real at one layer and false at the layer below

- 🔴 **Indonesia: 10 repositories where `p918` measured zero, and 0 of 10 are deliverable.** Re-asked
  on the national curriculum programme (`Kurikulum Merdeka`) and the teacher-facing artefact (`modul
  ajar`) rather than on English topic words. The most-starred Indonesian education agent —
  `anandpatikat/guru-latihan-dinamis`, **115 ★, pushed today** — **carries no licence file at all**,
  and 6 of the 10 are ungranted. [Record](../evidence/apac-id-th-supply.2026-11-19-p919.tsv);
  `agents/top.md` carries the tier.
- 🟢 **Thailand: no open education agent, and a maintained permissive language stack.**
  `PyThaiNLP/pythainlp` — **1,175 ★, Apache-2.0 byte-read, pushed 2026-11-13** — passes `918-R1`,
  while the agent tier is genuinely empty. 🔵 Thai is written **without spaces between words**, so a
  segmenter is a precondition for any tutor that marks free-text Thai, not an optimisation.
- 🔵 **The opportunity this creates, stated as a difference from the rest of APAC.** In Indonesia and
  Thailand a studio is **not competing with an incumbent open agent — there isn't one.** The
  deliverable is a built agent on permissive substrate, with the local curriculum vocabulary taken
  from the practitioner repositories above (read for requirements, never as a dependency — `T52`).
  That is a **shorter engagement than the "no supply" reading implies**, and it is the opposite
  conclusion to the one `918-G7`'s nil would have supported.
- 🟡 **Regulatory picture re-corroborated and unchanged**: Korea's AI Basic Act in force 22 January
  2026 with a guidance-first grace period through 2026; Vietnam's AI law effective March 2026 naming
  education among high-risk areas; Australia's TEQSA institutional action plans; Singapore's AI
  Verify toolkit; China's labelling and consent obligations; Japan principles-based. The EU Act's
  extraterritorial reach continues to bind APAC vendors whose outputs are used in the EU.


#### 🆕 `p918` — demand is large and documented; vernacular open supply exists and is not deliverable

- **Korea's AI Basic Act entered into force 22 January 2026.** Enforcement decrees are still being
  finalised and a **guidance-first grace period runs through 2026** — the enforcement cliff is 2027,
  not now.
- **Vietnam's Law on Artificial Intelligence took effect 1 March 2026, and education is on the
  statutory high-risk list** (automated assessment named explicitly). New systems comply by
  **1 March 2027**, existing ones by **1 September 2027** — 🔵 **both ahead of the EU date**, making
  Vietnam the earliest hard education-AI deadline this base tracks anywhere in the world.
- **Japan** remains principles-based, relying on existing law and cooperation rather than penalties.
- **Australia — the most concrete institutional demand in the region:** **TEQSA requires every
  higher-education provider to submit an institutional action plan** addressing generative-AI risk.
  🟢 A mandated deliverable with a named owner at every university in the country.
- **The EU AI Act reaches APAC vendors** selling into EU schools through Annex III — a compliance
  cost that falls on exporters regardless of local law.
- 🟢 **Supply, measured for the first time this pass (`918-F2`).** Querying in the vernacular returns
  **157 repositories this base had never seen** — Mandarin 79/78/23, Japanese 60, Korean 27/21,
  Vietnamese 16. 🔴 **Bahasa Indonesia and Thai return 0.** The tier is **`PRESENT — NOT
  DELIVERABLE`** under `918-R1`: the best permissive, byte-read member is **36 ★ and 383 days idle**.
- 🔵 **Offer:** bring the agent; read the vernacular shelf for the requirement. The gap between
  documented demand (~86% South-East Asian teacher use) and deliverable local supply is the widest of
  any region in this file — and **in Indonesia and Thailand it is total**.

🔴 **`p917` placed NOTHING in this region, and that is recorded rather than left as silence.** Of
this pass's **17** promotion candidates, **zero** placed APAC on any channel — not a README, not a
packaging manifest, not an institutional e-mail domain. 🔵 **The gap is not low AI activity.** The
regional WebSearch leg returned a great deal: roughly **86% of Southeast Asian teachers** already
using AI tools (EdTech Hub, March 2026); the fastest regional growth of any market, though the CAGR
estimates conflict badly (**20.9%** vs **35.3%**, which is itself the finding); and the Philippines'
Department of Education launching **`AGAP.AI`** in January 2026, described as the country's first
nationwide responsible-AI programme in basic education. **The gap is that none of this activity is
arriving as permissively-licensed public repositories.** Governance is ministry-split across ASEAN
and **fewer than half** of educators report confidence in institutional or government AI policy.

🟡 **The delivery read.** APAC demand is real, large and *not* mediated by open source, so an APAC
engagement is served by this base's `Global` tier plus national-programme integration — not by
regional supply, because `p899`'s "APAC builds the tutors" pattern has produced no new permissive
row in this pass. `917-G3`.


🔴 **Declared gap, `p916`: eleven discovery legs produced *no* APAC-placed row.** The legs were
dropout/early-warning, academic advising, degree audit, open badges, verifiable credentials, learner
record, reading fluency, virtual laboratory, knowledge tracing, student information system and
learning analytics. Not one returned a repository whose README carries an APAC country signal.
🔵 **This is an absence in these eleven angles, not an absence of APAC supply** — `p906` measured a
full Mandarin education tier at scale (347 repositories in grading alone) and `verticals/solutions.md`
carries `youufis/SmartKBS` from it. It is written down because an unstated regional absence is
indistinguishable from coverage, which is the whole reason this file places findings by region.
🟡 **The instrument limit is known and named:** `906-G2` established that a repository with English
metadata and vernacular content is invisible to a vernacular query, and the converse holds — these
eleven English-phrase legs cannot see vernacular-metadata supply. A pass that wants APAC rows in
these tiers must run the legs in Mandarin, Japanese and Korean.


🟢 **Promoted in `p902` — two convening facts, plus the region's one dataset-scale supply row**
(method: `902-F1`):

- **The World Bank is running its Global EdTech Policy Academy on AI in Seoul, 31 August – 4 September
  2026.** 🔵 **Korea is being used as the venue where other countries' education AI policy gets
  written**, which is consistent with the Korean AI Basic Act (in force 22 January 2026) that this
  file already tracks. A studio with a Korean reference can sell it across the cohort that attends.
- **Cambridge English convened APAC leaders in Kuala Lumpur, 23–24 April 2026**, on practical
  implementation across policy, institutions and classrooms — the assessment-and-certification end of
  the market.
- 🔴 **`riiid/ednet` is the largest public education dataset in the world and it is licensed
  `CC-BY-NC-4.0`, research purposes only.** 131,441,538 interactions from 784,309 students of the
  Korean *Santa* test-prep app; 13,169 problems, 1,021 lectures, 293 skill tags. **There is no licence
  *file*** — the grant is prose in the README, so SPDX reports `null` and any automated gate reads it
  as "unlicensed, probably fine" when it is the most restrictive grant in this KB.
  🟢 **Delivery line: validate a learner model against EdNet in a study; never train the model you
  ship on it.** With `CAHLR/pyBKT` (MIT) as the estimator that split is clean. Full row in
  `repos/trending.md` `902-R2`. **This is also APAC's only dataset-scale supply row** — the region
  builds the tutors *and* owns the benchmark data, and the data is the part Globant cannot resell.

🔵 **Demand side, restored `p901` (`901-G1`).** **Nanyang Technological University, Singapore,
announced that from August 2026 every undergraduate receives full access to Gemini Enterprise,
Google AI Studio and Vertex AI.** This datapoint was present in this KB through `p787` and was
**lost in a rewrite** — `p901` found it only under `archive/2026-11-12-p787-pre-rewrite/` and
`archive/2026-11-18-pre-cleanup/`, not in the live tree. It is restored here because it is the
clearest single instance of the APAC pattern this section describes: **higher education in the
region is moving faster than schools, and it is moving by institution-wide licensing rather
than by procurement of education-specific tools.**

🔴 **Why it matters commercially, and why it cuts against this KB's own default.** A campus
where every undergraduate already has a frontier general-purpose stack is **not** a market for
another general-purpose assistant. It is a market for the things that stack does not do:
curriculum alignment, mastery modelling, assessment integrity, and integration with the
institution's LMS and SIS of record. 🟢 That is precisely the tier this KB is strongest in
(`Submitty`, `pyBKT`, `OATutor`, the LMS-MCP rows) — **the NTU-shaped client is a composition
engagement, not a model engagement.**

🟡 **Source and confidence.** Search-snippet evidence, single source, reported via an industry
summary. The standing verification note at the top of this file governs it: every non-GitHub
host returns `403` in this session, so the NTU announcement could not be opened and read.
**Confirm against NTU's own announcement before it goes in a client deck.** 🔵 The *loss* of
the datapoint, by contrast, is byte-verified — it is in `archive/` and not in the live tree.

🔵 **Process finding this produced.** The mandated regional research legs **cannot detect a
dropped fact**, because a leg that re-finds a fact and a leg that finds it for the first time
look identical. `p901`'s regional legs returned this fact and would have written it as new;
only the mandatory grep-before-write caught that it had once been held and lost. **The grep
rule is now doing regression detection, not just duplicate prevention.** See `agents/trending.md`
`901-F1`.


🟢 **Supply side, placed p899: APAC builds the tutors, and it builds them in the vernacular.**
Five of this pass's eighteen new agents placed APAC on dispersed, exclusive-marker evidence
(spread ≥ 0.96 — not on repository names, and not on language switchers):

- **`Miaotofu01/Study-Mate`** — MIT, **1,488 ★**, CJK 1,490.
- **`SenmuuuuW/universal-diagnostic-tutor-skill`** — MIT, 279 ★, **diagnosis-first**: it
  establishes the learner's error before selecting what to teach.
- **`KeWang0622/kaogong-skill`** — MIT, 250 ★, Chinese **civil-service exam** preparation
  (行测/申论/职测) — a jurisdiction-specific exam system that exists nowhere else.
- **`ZeKaiNie/universal-examprep-skill`** — MIT, 396 ★, exam coaching with **source-traced
  handouts to suppress hallucination**.
- **`SimonsTang/feifei-companion`** — Apache-2.0, 117 ★, **K-12** (idle since April 2026).

🔵 **India, which this KB has repeatedly recorded as a gap, has an entry at the platform layer:**
**`pupilfirst/pupilfirst`** — **MIT**, **982 ★**, from **Pupilfirst Pvt. Ltd., India** — a
cohort-based LMS with review and mentoring workflows. **It is nine times larger than Mentingo**,
which this KB had been calling its counter-example to "education platforms are all copyleft".
🟡 Idle since 2025-12-09: fork it, do not track it. And **`Orenda-Project/rumi-platform`**
(Apache-2.0) targets **15 languages including a full Indian-language suite and Pakistan's
regional languages** over **WhatsApp** — origin unplaced, target market unambiguous.

🟡 **Demand side, refreshed p899 (search-mediated):** **South Korea** — AI Basic Act in force
January 2026, explicitly covering high-impact systems **in education**; enforcement decrees still
being finalised with **2026 run as a guidance-first grace period**; KERIS piloting teacher
development at scale. **China** — the most binding regime: generative-AI filing with CAC,
**550+ services filed by mid-2026**. **India** — still **no dedicated AI statute**, signalled as
possible as of July 2026, but **AI-generated content must carry prominent labels and provenance
markers from 20 February 2026**. **Japan** — principles-based under METI guidance, no
education-specific statute (confirmed negative, p890). 🔴 **No regional harmonisation exists**,
so a multi-country APAC deployment is four compliance postures, not one — `compose/patterns.md`
**P6**.


**Regulatory posture: four incompatible regimes, no regional harmonisation.**

- **South Korea** — the **AI Basic Act in force since 22 January 2026**; described as the
  closest analogue to the EU AI Act, though shorter. The most comprehensive regime in APAC.
  **Refinement this pass:** enforcement decrees are still being finalised and **2026 is a grace
  period oriented to guidance rather than penalties**. So Korea is a compliance-led market with
  a soft landing *this year* — the window to get architecture right before penalties bite.
  🟢 **p897 adds the operative provision, which this KB had been carrying as a bare characterisation.**
  **Article 31(1) — prior notice.** An operator providing a **generative AI** service must notify
  users **in advance** that the product or service runs on generative AI. **An AI tutor is squarely
  within this**, so the duty is not theoretical for an education engagement. **Article 43 sets a fine
  of up to KRW 30 million** for failing to give that notice — the one duty in the Act with a direct
  monetary penalty attached, where labelling and high-impact duties are enforced through
  investigation and corrective orders instead. **MSIT's transparency guidelines** accept either
  advance notice **or an on-screen indicator** for chatbots, and say the disclosure belongs in the
  terms, contract or interface — so for a tutoring UI this is an interface requirement, costed in
  days, not a programme. **Exemptions:** notice and labelling fall away, wholly or partly, where the
  AI use is **obvious** or the system is used **only for the operator's internal purposes** —
  relevant to teacher-facing lesson-prep tooling, which may escape the duty that the student-facing
  tutor cannot. **Article 35** additionally asks high-impact operators to make **best efforts** to
  assess fundamental-rights impact in advance — best-efforts, explicitly not a hard mandate, which
  is the sharpest contrast with the EU's Article 27 FRIA.
  🔴 **One claim could not be corroborated and is recorded as open, not as fact.** A secondary
  source states that the Act names **education among six sectors** carrying specific obligations for
  **automated assessment**. A dedicated search returned **nothing** on an education-specific or
  automated-assessment duty under the Act — the targeted result set addressed Article 31 fully and
  the education question not at all. It may sit in the Enforcement Decree or separate MSIT guidance,
  neither of which is reachable: `law.go.kr` and `msit.go.kr` are outside this session's allowed
  domains. **Do not plan a Korean engagement on the assumption that automated assessment is
  separately regulated there** until it is read in the primary text; the Article 31(1) duty above is
  the one that is corroborated and the one that binds.
- **China** — regulates by service type rather than one statute: recommendation algorithms,
  deep synthesis, generative AI services, and **labelling of AI-generated content**. The
  amended **Cybersecurity Law (in force 1 January 2026)** carries China's first AI clause.
  **p894 adds the operative content of the instrument this KB had been carrying as a bare date,
  and it is the most directly product-shaping rule in the region.** The **Interim Measures for
  the Administration of Anthropomorphic AI Interaction Services** (reported as **CAC Order
  No. 21**, issued **10 April 2026** by five agencies, **in force 15 July 2026**) govern
  services providing *sustained emotional interaction through a simulated human personality*.
  Where they apply, the obligations are severe and several are education-specific in effect:
  **virtual-partner and virtual-relative services may not be offered to minors at all**;
  **guardian consent is required under 14**; a **minor mode** with time limits and real-world
  reminders plus guardian risk alerts; **age verification with an appeal channel**; a
  prohibition on **inducing emotional dependence or addiction that damages real-world
  relationships**; machine-disclosure reminders; mandatory intervention when a user signals
  self-harm; and **algorithm filing plus security assessment** before launch.

  **The education carve-out is real but conditional, and that distinction is the whole
  engagement risk.** Law-firm analysis lists *education* alongside intelligent customer service,
  knowledge Q&A, work assistants and scientific research as outside the Measures (Bird & Bird),
  and a second analysis frames the carve-out as covering education and learning services **that
  lack continuous emotional interaction** (Geopolitechs). Scope therefore turns on a test, not a
  sector label — and a third source notes the Measures **define neither "continuity" nor
  "emotional interaction"** (Lexology). **Consequence for delivery:** the retention features a
  consumer tutor instinctively ships — a persistent named persona, affective rapport, streaks,
  a "study buddy" character, companion framing — are exactly what argues a product *into* scope,
  and the category that produces `DeepTutor` and `OpenMAIC` is the category most likely to ship
  them. **For a China-market education product the safe design is persona-stateless, disclosed,
  and free of affect simulation**, with the pedagogical persistence held in the learner model
  rather than in a character. That inverts a product instinct, which is why it belongs in a
  market file and not only in a compliance annex. **Channel caveat:** every source here is
  secondary (law-firm guides and policy analysis); the CAC text itself is blocked by this
  session's network policy, and **no source addressed a tutoring product specifically**.
- **Vietnam** — **new in this pass, and the most consequential APAC finding of the pass.**
  Vietnam has a dedicated **Law on Artificial Intelligence (No. 134/2025/QH15)**, in force from
  **1 March 2026**, with **Decree 142** and **Prime Minister Decision 33/2026/QD-TTg** (signed
  **30 June 2026**, effective **15 August 2026**) setting a **closed list of 46 high-risk AI
  systems across six sectors** — transport (31, the largest), **education**, ethnic and
  religious affairs, healthcare, banking and judicial proceedings. **Education accounts for
  three of the 46**, reported as **behavioural monitoring, learner ranking and automated
  assessment** *(the three-item breakdown is single-source and weaker than the rest; the
  46/6/education-included structure is corroborated by two law firms and one legal-news
  service)*. Compliance clock: systems **already running** in education before 15 August 2026
  have until **1 September 2027**; others until **1 March 2027**. Notification applies to
  medium- and high-risk systems and the Ministry of Science and Technology enforces, including
  by refusing registration. **Why this matters more than its market size:** Vietnam is the
  second jurisdiction after the EU to make education AI *statutorily* high-risk, and its
  deadlines (March and September 2027) **land before the EU's 2 December 2027**. An
  Annex-III-grade oversight architecture built for EMEA is reusable here — and needed sooner.
- **Australia** — **also new, and also previously missing.** No AI-specific statute, but the
  higher-education regulator **TEQSA** required **all 203 registered providers to submit
  institutional action plans on generative AI** (June 2024, **100% response**), and from
  **2026 moved from an educative to a regulatory-led approach**, so those plans are now
  examined in ordinary oversight. TEQSA published *Assuring quality learning in a gen AI-
  integrated future* on **24 June 2026** and maintains a GenAI Knowledge Hub; the binding layer
  is the **Higher Education Standards Framework (Threshold Standards)**, with the action plans
  sitting alongside it as expectations. Schools are covered separately by the **Australian
  Framework for Generative AI in Schools**, with state-level additions. **Practical read:** every
  Australian provider already has a written genAI plan and is now being held to it — the sale is
  *implementing an existing commitment*, which is a materially easier conversation than
  persuading an institution to adopt one.
- **Japan** — **the gap this KB declared is now closed, with a negative answer.** Japan's
  posture is promotion-first and light-touch: a promotion-focused AI law backed by voluntary
  guidelines, and **no education-specific AI statute or classroom regime** on a second targeted
  pass. That is the finding, not a failure to find — and it is why Japan remains the
  lowest-friction pilot geography in APAC.
- **Singapore** — governs by toolkit rather than statute (**AI Verify**). **New Zealand** —
  explicitly updating existing privacy and consumer law instead of writing AI law.
- **India** — no dedicated AI law yet; in **July 2026** the government signalled it may pursue
  one. Amended **IT Rules require prominent labels and provenance markers on AI-generated
  content from 20 February 2026**.

**The cautionary case is Korea's.** It attempted a national rollout of AI-powered digital
textbooks in schools from 2025 and, after parental and teacher backlash, **walked it back to
optional "educational material" status within a year**. This is the most instructive
deployment failure in the industry: the blocker was stakeholder consent, not technology.
Any APAC pilot plan that lacks a teacher- and parent-consent workstream is repeating it.

Market structure: China's tutoring crackdown reshaped edtech, with non-academic STEM/coding/AI
tutoring rebounding — **TAL pivoted into AI learning hardware**. India's **PhysicsWallah**
launched its own AI tutor.

**Extraterritorial note.** The EU AI Act reaches APAC vendors selling proctoring or admissions
software into EU schools. For an APAC product company, EU conformity work is an export
prerequisite, not a European nicety — and with Vietnam's dates falling earlier, the same
engineering now has two buyers.

**Opportunity.** APAC is where the best open education agents are being built — **DeepTutor
(HKU, Apache-2.0)** and **OpenMAIC (Tsinghua, MIT)** are the two most significant open
tutoring assets globally, and both are permissive. A studio can be an implementation partner
for assets it did not have to fund. Content labelling is a concrete, dated engineering
requirement in both China and India — build provenance marking into generated courseware by
default. `MinerU` (Apache-2.0) handles CJK textbook extraction better than Western-trained
parsers. Korea is a compliance-led market under the AI Basic Act (on a 2026 guidance-first grace
period); Japan's voluntary posture makes it the lowest-friction pilot geography in the region.
**The new priority order for a regional compliance build is Vietnam first** — statutory
education high-risk with a March/September 2027 clock — **then Korea, then Australia** (where
the client's own TEQSA action plan is the requirements document), with Japan and Singapore as
low-friction pilot grounds.


#### p891 additions — APAC

**Public opinion is now measured, and it is moving *against* permissiveness in three of four
markets.** The **Ipsos Education Monitor 2026** records support for **banning AI in schools**:

| Market | Support for a ban, previous | Support for a ban, 2026 | Direction |
|---|---|---|---|
| Australia | 47% | **52%** | ▲ +5 |
| South Korea | 27% | **31%** | ▲ +4 |
| Japan | 21% | **29%** | ▲ +8 |
| Indonesia | 30% | **23%** | ▼ −7 |

Japan is the largest single move in the table. This KB records Japan as the
**lowest-friction APAC pilot geography** because it has no education-specific statute — that
remains true legally, and this is the counterweight: **regulatory headroom is widening while
public consent is narrowing**. A Japanese pilot should be designed to survive a consent
argument, not merely a compliance one (see T8). Overall, Ipsos finds support for banning AI in
schools lower than support for restricting children's social media — the ceiling on
restriction is not yet near.

**Vietnam is now the most concretely specified education-AI regime in the region.**

- The **Law on Artificial Intelligence is in force from 1 March 2026**. Education is one of the
  sectors with an extended transition: **12 months for systems already in operation generally,
  18 months for health care, education and finance**.
- **Decision 33/2026/QD-TTg** identifies high-risk systems across six sectors with **education
  among them**, naming **automated assessment** explicitly.
- Separately, the **Ministry of Education has set 12 periods per class per year of AI content
  for grades 1 to 12** — a curriculum volume mandate, distinct from the risk classification.
  *Sources conflict on whether Vietnam's education rules are a risk classification or a
  curriculum requirement; this pass finds they are **both**, from two different instruments, and
  records them separately for that reason.*

**Regional framing.** Law-firm analysis sorts APAC into three groups: **comprehensive
horizontal obligations** (South Korea, Vietnam), **targeted AI regulation** (China), and
**sector-based approaches**. **South Korea, Taiwan and Vietnam brought AI-specific statutes into
force in 2026**; China, India and Singapore regulate through rules and guidance. Australia
relies on existing law plus voluntary adoption guidance rather than a standalone AI act.

**Opportunity — APAC, sharpened.** Vietnam is the one market where the compliance object is
*named*: automated assessment is statutorily high-risk, with an 18-month education transition
and a dated curriculum obligation running to grade 1. That is a scoped, biddable programme
rather than a readiness conversation. Australia's rising ban sentiment (52%) makes
**human-in-the-loop evidence a sales requirement**, not a design preference.

#### India — first dedicated leg (closing the gap p891 called "the highest-value remaining")

p891 recorded: *"India has never been covered by this KB, in any pass. The largest school system
in the world, and this file has no position on it."* Run as its own leg this pass. **India is
not a regulation story — it is a curriculum-mandate and teacher-capacity story, and the dates
are now.**

- **AI and Computational Thinking enter the school curriculum from the 2026–27 academic year.**
  A **Press Information Bureau** release (August 2026) states that **NCERT**, working with
  **CBSE**, has introduced a Computational Thinking and AI curriculum for **Classes III to
  VIII** from 2026–27, designed for integration with existing subjects from the foundational
  stage rather than as a bolt-on subject. A **CBSE circular dated 1 April 2026** formally
  launched the framework. The expert committee that drafted it was chaired by an IIT Madras
  professor, with NCERT review and an NCF-SE coordination committee for quality assurance.
- **The upper grades are already further along than the new mandate.** CBSE has offered **AI as
  an elective in Classes 9–12** for several years, and a **15-hour SOAR module** runs for
  Classes 6–8 in **more than 18,000 CBSE schools**. **NCERT has formed a team to write AI
  textbooks for Grades 11–12.** Reporting on whether Classes 9–10 become compulsory in 2027–28
  conflicts across sources and is recorded as contested.
- **Infrastructure is a stated school obligation.** The PIB release notes CBSE schools must
  ensure adequate infrastructure for students taking AI as a subject — which, across a system of
  this size, is the binding constraint rather than the pedagogy.
- **Content rules already bind, and this KB already tracks them.** India's amended IT Rules
  require prominent labelling and provenance markers on AI-generated content from **20 February
  2026** (T7). In **July 2026** the government signalled it may pursue **dedicated AI
  legislation** rather than continuing to regulate through the intermediary framework — so the
  regulatory posture is live and could change inside a delivery window.
- **Scale context.** India is the fastest-growing AI market in APAC at a **38.9% CAGR**, against
  Singapore's regional lead on diffusion (60.9% among working-age adults).

**Opportunity — India.** The mandate is dated, national and already in force for the coming
academic year, and the honest constraint is the one a secondary source put most plainly:
**adding a subject to the curriculum is not the same as preparing teachers to teach it.** That
is the engagement.

1. **Teacher enablement and content localisation at system scale**, against a curriculum
   somebody else owns (NCERT/CBSE) — the same shape as the Saudi opportunity above, and the
   reason **P10** in `compose/patterns.md` is written once for both.
2. **Provenance-by-construction is non-optional here.** Any generated courseware for an Indian
   classroom must carry labels and provenance markers under the IT Rules from February 2026.
   Emit at generation time; retrofitting across a national content library is the expensive
   path (T7, **P6**).
3. **Low-bandwidth and multilingual delivery.** The offline stack this KB tracks for Africa
   (`kolibri` MIT, `iiab`) applies directly, and Indian language coverage is a localisation
   gap in every tutor in `agents/top.md`.

**And note what India is not.** There is no education-specific AI statute, no high-risk
classification like Vietnam's, and no prohibition regime like the UAE's. The compliance surface
is content labelling, not system conformity. **India is a delivery-capacity market, not a
conformity market** — which makes it closer to Saudi Arabia than to the EU, and that is the
single most useful sentence in this subsection for engagement planning.

*Confidence: moderate-to-good on the mandate (PIB is a primary government channel, corroborated
by careers360 and multiple education outlets; the CBSE circular date appears in secondary
reporting only). Low on the Classes 9–10 timeline, which conflicts across sources. The 38.9%
CAGR is an analyst figure from a regional AI report, not an education-specific one. PIB and CBSE
primary documents are blocked by this session's network policy and were read through search
snippets.*


#### Southeast Asia — first dedicated leg (the region this KB had least coverage of)

APAC coverage in this KB has been China, Japan, Korea, Singapore, Australia/NZ, Vietnam and —
since p892 — India. **Southeast Asia as a bloc had never been run as its own leg.** It has now,
and it produced the largest single national programme found in any region this pass.

**The Philippines: Project AGAP.AI, launched 9 January 2026 by the Department of Education**,
with President Marcos at the launch. Named from the Filipino *agapay*, "to support or
accompany". Verified details:

| Field | Value |
|---|---|
| Scale | Up to **1.5 million participants** — ~1.05M learners, ~300,000 teachers, ~150,000 parents, phased through 2026 |
| Instrument | **DepEd Order 003, s. 2026** — *Foundational Guidelines on AI in Basic Education* (responsible use, learner protection, inclusivity, ethics, data privacy) |
| Training arm | Branded **"AI Ready ASEAN Philippines"**; modules on AI fundamentals, misinformation detection, privacy and ethical use |
| Partners | **ASEAN Foundation**; **MIT RAISE** and **Day of AI** on curriculum integration and teacher training; **Microsoft** (February 2026) on AI literacy and learning recovery, and separately an ARAL programme reaching ~3,000 teachers across ~1,500 schools |
| Curriculum | AI concepts and computational thinking to be integrated into the basic education curriculum |

*Sourcing note: January coverage described the guidelines as forthcoming; February coverage
reports DepEd Order 003 s. 2026 as issued. The order number is from a single secondary report
and the Philippine government primary sources are blocked by this session's network policy —
**confirm the order number before citing it to a client.***

**Why the Philippines matters commercially more than its size suggests.** It is the only
national programme found anywhere that **names the parents as a trained cohort** (150,000 of
them). Every stakeholder-consent failure this KB has recorded (trend **T8**) has been a failure
to bring guardians along. The Philippines has made that an explicit, budgeted workstream — so
it is both a reference model to cite elsewhere and, right now, a delivery contract with 300,000
teachers in it and no obvious local capacity to serve them.

**The regional picture (ASEAN Foundation *Digital Outlook* / AI Ready ASEAN, February 2026).**
**Thailand has the highest AI adoption rate in ASEAN**, driven by rapid uptake among students
and teachers. But **fewer than half of educators across the bloc express strong confidence in
their institution's AI policies and governance frameworks**, and EdTech Hub describes teachers
across Southeast Asia already using AI largely without formal training or institutional
support. The Jakarta Post's framing of the same report — *a region eager for AI but lacking
guidance* — is the whole finding in six words.

**Public opinion is not a tailwind (Ipsos Education Monitor 2026, nine markets: Australia,
India, Indonesia, Japan, Malaysia, New Zealand, Singapore, South Korea, Thailand).** Globally
**39% think AI should be banned in schools outright**. Support for a ban runs lower in the
Asian markets than the global figure, but it is not negligible anywhere, and it is not uniform
across APAC. Any national programme pitched here needs a public-legitimacy workstream, not just
a technical one — which is **T8** again, measured.

**Opportunity — Southeast Asia.** This is the **adoption-outran-governance pattern (T4) in its
purest form**: highest-in-bloc adoption in Thailand, under-half confidence in governance
region-wide, and teachers improvising without support. The LATAM "governance and enablement, not
adoption" offer (`compose/patterns.md` P5) transfers here essentially unchanged, and the
Philippines national-mandate delivery pattern (**P10**) has a live, funded, named buyer. The
ASEAN Foundation's bloc-level convening role means a reference built in one member state is
visible in the other nine — the regional leverage that EMEA's AILit framework provides in
Europe.


**`p896` additions — search-snippet evidence, source named.**

- 🟢 **China is exporting the platform, not just the policy.** At the **World Digital Education
  Conference in Hangzhou, May 2026**, China launched a **global AI education service platform**,
  extending *Smart Education of China* to roughly **220 countries and regions**. 🔵 For a studio
  this is competitive intelligence with a delivery edge: a state-backed free platform reaching
  emerging markets changes what a paid LATAM or African offer has to beat, and it is the clearest
  instance yet of **T6** (localisation, not origination, is where the non-APAC work is).
- 🔴 **Public support for *banning* AI in education is rising across APAC, not falling** (Ipsos,
  nine APAC markets): **Japan 21% → 29%**, **Australia 47% → 52%**, **South Korea 27% → 31%**;
  India sits lower at **26%**. Australia's majority is the number to carry into a TEQSA-era
  conversation. **Adoption momentum and public consent are moving in opposite directions**, which
  is an argument for the auditable-oversight posture this KB already recommends, delivered as a
  public-trust artefact rather than a compliance one.
- 🔵 **Market shape (secondary, Markets&Markets):** APAC AI-in-education **$591.6M (2024) →
  $1,848.1M (2029), 20.9% CAGR**, with **China ($417.5M)** and **Japan ($318.7M)** the largest
  national pools. 🟡 That CAGR is roughly **half** the global 41.5% figure carried at the top of
  this file — one of the two is wrong, or they measure different baskets. Recorded as a
  discrepancy rather than resolved.
- 🟢 **Japan's precondition is already met:** 1:1 device provision at compulsory-education level
  is **complete**, and official digital textbooks are next. Japan is the APAC market where a
  software-only offer needs no hardware story.



#### p898 additions — APAC

**The Philippines has a national higher-education AI framework, and this KB had it in a trending
note instead of the market map.** The **Commission on Higher Education (CHED)** issued
**Memorandum Order 21**, a national framework covering AI in **teaching, research and operations** —
all three, not classroom use alone. *(Search-snippet evidence; `ched.gov.ph` is unreachable from this
session — see the verification note at the top of this file. The order number and its three-way
scope are corroborated across two independent regional summaries; the clause detail is not.)*

🔵 **Why it changes the APAC priority order rather than just extending it.** The standing APAC
finding ranks **Vietnam first** because its statute names education as high-risk with a concrete
compliance object. The Philippines is a *different* opportunity shape: the framework covers
**operations**, which is the registrarial and administrative tier — the tier `P12` is built for and
the one this KB has named as its top under-served opportunity for several passes. A framework that
explicitly covers operations is a procurement hook for that tier, not for the tutor tier.

**Opportunity — Philippines.** English-medium instruction, a large public HE system, and a national
framework whose scope includes operations. **The registrarial agent tier (`P12`) is the fit**, not
tutoring. 🔴 **Unverified against primary text** — confirm MO 21's actual obligations before any
client commitment.

- **Promoted from the research log in `p904`** (captured in earlier passes, never published here):
  **virtual-tutor adoption across the surveyed APAC cohort sits at 30%** (Times Higher Education),
  against a regional picture that the same reporting calls patchy, with connectivity a limiting
  factor — 🔵 **the number to quote when a client assumes APAC tutor adoption is uniformly ahead of
  the West; it is not.** And the **Acer Edu Summit (Asia Pacific)** is worth tracking as a channel
  rather than a vendor event: device makers bundling infrastructure, hardware and partnerships is
  how AI reaches APAC classrooms that have no cloud budget, which is the same economics that makes
  `Kolibri` and `GT-MISHKATKIDS` deployable in `verticals/solutions.md`.

#### p905 — APAC: searched, nothing new

🟡 **Declared null, not silence.** The `p905` leg
(`AI education APAC Asia Pacific 2026 adoption regulation players`) returned 9 sources and **0 facts
absent from this file**. Re-checked and already held: South Korea's **AI Basic Act** in force
January 2026; **Vietnam's** AI law (March 2026) with education and automated assessment on the
high-risk list, and its ministry-mandated AI instruction hours for grades 1–12; India's
AI-generated-content labelling requirement from February 2026; Australia's reliance on existing law
and voluntary guidance; Japan's voluntary industry-led guidelines; the **Ipsos Education Monitor
2026** splits (support for banning AI in schools lower across most Asian markets, rising in Japan and
South Korea, falling in Indonesia, higher in Australia and New Zealand); **NTU Singapore** giving
every undergraduate access to Google's AI tools from August 2026; and virtual-tutor adoption at
**30%** (Times Higher Education). 🔵 The multi-jurisdiction divergence this section has recorded for
several passes is what **P6** is priced against, and it widened again rather than converging.

#### p906 — APAC: the supply side of this region is now measured by language, and it is one country

🔴 **This is an APAC finding in its entirety, which is the part worth noticing first.** `p906` ran
the eight language channels this base had declared untried — **Mandarin, Hindi, Urdu, Indonesian,
Vietnamese, Japanese, Korean and Thai**. All eight are APAC languages. **Seven of the eight return
no usable supply; the eighth returns a whole tier this KB had never shelved.** Ceilings, queries,
result counts and query-shape controls:
[`nonenglish-ceiling.2026-11-18-p906.tsv`](../evidence/nonenglish-ceiling.2026-11-18-p906.tsv).

| Language / market | Repos matching | Topical ★ ceiling | Licensed | Sourcing answer for an engagement |
|---|---|---|---|---|
| **Mandarin — China** | **347** (`作业 批改`) + 169 (`题库 组卷`) | **193** | mostly yes | 🟢 **Adopt.** A real automated-grading and item-bank tier; 12 repositories verified, 6 shelved to `agents/top.md`, 5 to `repos/foundations.md`, 1 to `verticals/solutions.md`. |
| **Hindi — India** | **113** | **2** | **0 of 113** | 🔴 **Build.** Volume without supply — see below. |
| Indonesian — Indonesia | 14 | 1 | none | 🔴 **Build.** |
| Thai — Thailand | 9 | 0 | none | 🔴 **Build.** |
| Vietnamese — Vietnam | 6 | 1 | none | 🔴 **Build.** |
| Korean — South Korea | 2 | 2 | none | 🔴 **Build.** |
| Japanese — Japan | 1 | 0 | none | 🔴 **Build.** |
| Urdu — Pakistan | 1 | 0 (sole hit is not education software) | n/a | 🔴 **Build.** |

🔵 **India is the commercially important line and it is not the obvious one.** The Hindi channel is
**not empty — it is the second-densest of the eight**, with 113 repositories matching `शिक्षा`
("education"). But the star ceiling is **2**, and **not one of the 113 carries a licence file.**
Every hit inspected is a school, NGO or foundation *website*, or a non-AI teacher-rating project.
🔴 **So for an India engagement the answer is not "search harder in Hindi". It is that the
Hindi-language layer on GitHub is content and institutional web presence, not software, and none of
it is legally reusable.** That is the same conclusion `p904` reached for **Mexico** by a different
route, and it now holds for the two largest emerging education markets in the world. Budget the
vernacular tier as build in both.

🟡 **This does not say Indian or Korean education software does not exist** — it says it does not
exist *with vernacular metadata on GitHub*. `search/repositories` matches name, description and
README, so a project whose metadata is English and whose content is Hindi is invisible to this
instrument. The shelved Indonesian row `itsme-ganzu/belajar-ngoding-byGanzu` (MIT, 66 ★) proves the
blind spot exists: **this pass's own Indonesian queries did not find it.** The ceilings are ceilings
on *vernacular-metadata supply*, which is what a regional sourcing claim actually rests on — and
they are also the reason the India figure should be re-probed in English-metadata form before any
engagement prices it.

🟢 **China is now the second-best-covered supply market in this KB, after the anglophone one.** The
cohort `p906` shelved is **assessment and item-bank infrastructure**, not tutors — the layer
`repos/foundations.md` held as entirely North American and European across twelve verified rows. The
commercial reading: for a China or Chinese-curriculum engagement there is a usable grading and
exam-delivery substrate to adopt, with the standing caveat that **three of the twelve are AGPL-3.0
and one is Mulan PSL v2**, so the closed-derivative question has to be asked per repository rather
than per cohort.


#### Added `p907` — Japan's instruments, and the education app this file had no row for

- **Japan is the region's clearest promotion-first regime, and it now has a second-phase plan.**
  The **AI Promotion Act** (2025) is a promotion statute rather than a prohibition regime, and the
  Cabinet adopted a **second-phase AI Basic Plan in July 2026**. 🔵 For delivery this is the
  opposite posture to the EU's: the binding constraint in Japan is **copyright**, which sources
  describe as the live point of contention, not high-risk classification. A Japanese engagement
  should put rights-clearance of training and retrieval corpora where an EMEA engagement puts
  conformity assessment. *(two sources on the Act; the Basic Plan phase is single source)*
- **ByteDance's `Gauth` became one of the top education apps in the United States.** 🔵 The concrete
  instance of a pattern this file argues elsewhere: **APAC edtech capital is now exported into North
  American consumer demand**, so the competitive set for a US K-12 or test-prep engagement includes
  an APAC-origin free app, not only US incumbents. 🟡 "Top education app" is an app-store ranking
  claim with no date or store named in the source — directional only. *(single source)*

🟡 **Evidence grade: search-snippet with the source named, not primary text.** Every non-GitHub host is refused at this session's egress proxy (`403` on `unesco.org`, `eur-lex.europa.eu` and `oecd.org`, all re-probed `p907`). Confirm against the primary instrument before a client deck.

#### `p908` — education is now a *named* high-risk sector in a second APAC jurisdiction

Measured from the `AI education APAC 2026 adoption regulation players` leg.

- 🟢 **Vietnam is the most education-specific instrument found in this leg.** **Decision No.
  33/2026/QD-TTg** identifies high-risk AI systems in six sectors **including education** — with
  **automated assessment** given as the example. 🔴 Sources disagree on the compliance deadline
  (**September 2027** in one, **1 March 2027** in another); the official text must settle it before
  this goes in a proposal.
- **South Korea's AI Basic Act** is the region's comprehensive law — transparency, risk assessment,
  human oversight and documentation for high-impact systems. **MSIT has signalled 2026 as
  effectively a pilot period with limited enforcement and a one-year grace period on penalties.**
  🟢 That makes 2026 the cheapest year to deploy and document in Korea, and 2027 the expensive one.
- **Australia**: **TEQSA required *all* higher-education providers to submit institutional action
  plans** addressing generative-AI risk — a regulator-mandated document per institution, which is a
  deliverable shape, not just a constraint. A new **Office of AI** coordinates policy across
  government.
- **China**: targeted rather than comprehensive — layered rules on algorithmic recommendation,
  deepfakes and generative AI outputs.
- **India** has signalled it may pursue dedicated AI legislation; **Hong Kong's** 2026 agenda centres
  on responsible adoption through ethics and data-privacy governance.
- 🔵 **Extraterritorial pull, and it runs the unexpected way**: the EU AI Act reaches *"providers and
  deployers … located in a third country, where the output … is used in the Union"*, which pulls APAC
  proctoring and admissions vendors selling into EU institutions into EU scope.

🔴 **Declared gap: this leg returned no adoption statistics, no market sizing and no list of
education AI companies for the region.** The regulatory picture for APAC is well covered here and the
*commercial* picture is not. A future pass should run the APAC leg per country in that country's
language, which is the method `p708` proved for LATAM and `p908` re-confirmed.

#### `p909` — China's AI-in-education plan has a teacher-*credentialing* limb, which is a different buyer

🟢 The April 2026 **"AI + Education"** action plan — five central departments, MOE-led, 2030
horizon — is already on these shelves, as is Beijing's **≥8 class hours** of AI per student per
academic year. The limb this base did **not** hold: **AI is to be incorporated into teacher
qualification examinations and certification.**

🔵 **Why that is a category change rather than a detail.** Every other instrument on this file
treats teacher AI capability as **professional development** — a budget line that competes with
every other budget line and slips. Putting AI into the **qualification exam** makes it a
**licensing gate**: a cohort that must be trained to a published standard on a statutory timetable,
with an assessment attached. 🔵 **That is the single largest addressable training-and-assessment
population in this region, and it is compulsory rather than discretionary.** The composable
asset for it is the grading and item-bank tier `P25` assembles from the Mandarin cohort — the
buyer is a certification authority, not a school.

🟡 Two searches carried the plan; the credentialing limb appeared in official-outlet summaries
(`english.www.gov.cn`) as reported by the search channel. 🔴 No primary source could be fetched
(`WebFetch` DNS failure), and the plan's **full text was not read** this pass.

🔴 **Not published, because it did not corroborate.** A claim that the Ministry **bars primary
pupils from using generative AI independently** — and bars teachers from substituting AI for core
instruction — appeared on **one** aggregator, which the search channel itself flagged as
unverified against any official source. If true it would materially constrain any K-6 tutor
deployment in China, so it is recorded as a **high-value open lead**, not as a fact.

🔴 **The region's standing absence, restated because silence reads as coverage.** **No first-hand
APAC classroom-adoption measurement exists on these shelves** — no infrastructure, teacher-usage
or student-usage rates for China, India or Japan. Both APAC legs this pass returned **policy
ambition only**, and one reported explicitly that it found nothing on adoption in those countries'
schools. 🔵 Every APAC opportunity above is therefore inferred from **instruments**, not from
measured usage, and should be presented to a client that way.

#### `p910` — the national-examination supply floor, market by market

🔵 **New instrument, APAC-weighted.** `p910` ran the English-metadata-plus-exam-term channel
(`906-G2`) across eight APAC markets. This is the first time this file can price *local* supply per
market instead of reasoning from regional adoption statistics. Method and caveats:
[`repos/trending.md`](../repos/trending.md) `p910`. Counts are nominal GitHub hits (exact);
posture figures are a top-25-by-stars sample (`910-G3`).

| Market | Exam | Bare / co-termed hits | Adoptable local supply | What to assume in a bid |
|---|---|---|---|---|
| 🇯🇵 Japan | `JLPT` | 3,446 / 360 | 🟡 **Tools yes, corpora no** — 5 MIT tools incl. `hanabira.org` (436 ★) and `furiganamaker` (312 ★) | Adopt the tooling; **the deck corpora are CC BY-NC / BY-SA / AGPL**, so generate or capture per learner |
| 🇰🇷 Korea | `TOPIK`, `suneung` | 3,008 / 15 | 🔴 **One MIT benchmark, one *ungranted* agent** | The only AI-native TOPIK build (`topik-shortcut`) has **no licence** — budget a rebuild |
| 🇬🇧→🇭🇰 Hong Kong | `HKDSE` | 307 / 17 | 🟡 3 MIT applications, all ≤1 ★ | Subject-scoped mocks + a JUPAS admissions calculator exist; **institutional tier does not** |
| 🇮🇩 Indonesia | `SNBT`, `UTBK` | 923 / 36 | 🟡 One MIT CAT engine (`cat-snbt-skd`) | The **exam rules** are encoded locally and worth adopting; everything else is build |
| 🇸🇬 Singapore | `PSLE` | 286 / 10 | 🟡 One MIT agent (`bandup`, essay marking) | 🔴 **The MOE syllabus dataset is CC BY-NC** — the curriculum spine cannot be adopted (**P29**) |
| 🇦🇺 Australia | `NAPLAN` | 140 / 3 | 🟢 **Apache-2.0 government-adjacent infrastructure** (`nsip/nias2`) | The strongest institutional artefact in the region; validation plumbing is already open |
| 🇲🇾 Malaysia | `KSSM` | 165 / **2** | 🔴 **Prompts only** — `Prompt-libraries-for-Malaysia-Educators` (MIT) | Ceiling is **2 repositories**. Assume nothing local to adopt; the 2026–2035 National Education Plan creates the demand and no supply answers it |
| 🇯🇴 Jordan | `Tawjihi` | 228 / 4 | 🔴 **None — all four ungranted** | **First market in this KB with education supply and zero adoptable supply.** Everything is build |

🟢 **The opportunity this creates, stated as a sales position rather than a lament.** In six of
these eight markets the exam format is public, the demand is state-driven, and the open supply is
**unlicensed hobby code**. A studio that arrives with a licence-clean, re-authored curriculum spine
and a governed agent tier is not competing with an incumbent open platform, **because there is
none** — the competition is the client's own unfinished internal build. 🔴 The converse is the
risk: a delivery team that greps GitHub for "KSSM" or "SNBT" will find Kotlin state machines and
Minecraft serialisation libraries (`910-F1`), and a team that finds the real repositories will find
no grant on two-thirds of them.


🟢 **Added `p911` — and this block exists to close `Gap 254`, which recorded that APAC coverage in
this file was *regulation only, for a second consecutive pass* while the three highest-adoption
agents on `agents/top.md` are APAC university projects.** 🔵 **`Gap 254`'s prescribed remedy was
per-ministry legs rather than a fifth generic English query. The leg below was run that way — India's
ministry and boards by name — and it returned a curriculum rollout with dates, owners and a named
binding constraint.**

🔴 **India has made AI a mandatory school subject with a dated rollout, and the dates are inside a
studio's planning horizon.**

- 🟢 **AI and Computational Thinking become mandatory from `Class 3`, starting the `2026-27`
  academic year**, with **Classes 9–10 expanding in `2027-28`** (Ministry of Education; carried by
  several independent outlets).
- 🟢 **Ownership is named and it is split**: **`NCERT`** reviews the draft curriculum and a
  **`NCERT`–`CBSE` Coordination Committee** oversees integration. 🔵 **That matters for who a studio
  sells to** — the content authority and the examining board are different bodies, and this KB's
  `P22`-shaped curriculum-spine work has to satisfy both.
- 🟡 **What `CBSE` actually offers today is much smaller than the mandate**: a **15-hour AI skills
  module for Class VI** and an **elective AI subject for Classes IX–XII**. 🔵 **The gap between the
  15-hour module and a Class-3-upward mandate is the work.**
- 🔴 **The binding constraint is stated by the officials themselves: teacher capacity, with over
  `10 million` teachers needing training.** This is `T11` ("AI literacy is becoming a statutory
  curriculum mandate, and teacher capacity is the binding constraint") instantiated at the largest
  scale this KB has recorded. 🔵 **Teacher-facing enablement is therefore the larger line item than
  student-facing product**, and it is the one with a statutory deadline behind it.
- 🔴 **Two demand-side cautions a client will raise first.** **State board schools — which enrol the
  overwhelming majority of India's students — are described as operating in "an entirely different
  infrastructure reality"** from CBSE schools, and one report finds **most students stop using AI
  tools after one or two sessions**. 🟡 **So a deliverable priced for CBSE-grade connectivity does
  not transfer to the state boards**, which is where the volume is.
- 🟢 **Singapore** (Smart Nation) plans to **train teachers at all levels on AI in education by
  2026** — a second APAC market whose teacher pipeline is a funded programme rather than an
  aspiration.

🟢 **Supply, and this is the half `Gap 254` said was missing.** The `CBSE`/`NCERT`/`JEE`/`NEET` legs
of `911-F1` surfaced and byte-read the first **India-specific, permissively licensed, curriculum-
aligned** rows this KB holds — a **14,000-item JEE Main previous-year question store**, two
**grounded RAG tutors over NCERT textbooks that cite their source**, a **curriculum-drift differ for
NCERT textbooks across editions**, and a repository tracking **`CBSE` AI subject code `417`**
itself. All are on `agents/top.md` and `repos/foundations.md` with byte-read grants. 🔵 **`Code 417`
is the row to notice**: it is open supply tracking the exact subject the mandate above expands.

🔴 **Declared limit on this leg, stated plainly:** it was run against **India** by ministry and board
name, and **only** India. **China, Japan, Korea and Australia were not queried for procurement this
pass** — the generic APAC English leg returned, as `p910` predicted it would, nothing this tree did
not already hold. 🔵 `Gap 254`'s remedy named Japanese, Korean and Simplified-Chinese ministry legs;
India consumed the budget and **those three remain unrun**. Carried forward as `911-G3`.

🟢 **`911-G3` DISCHARGED — the Japanese, Korean and Simplified-Chinese ministry legs, run `p912`.**
`Gap 254`'s remedy predicted these would return **procurement rather than news**, and all three did.
Evidence: `evidence/p912-ministry-legs.2026-11-19-p912.tsv`.

**China — the plan is interministerial, and examination assessment is inside its 2026 scope.**

- 🟢 **《"人工智能+教育"行动计划》 — the "AI+Education" Action Plan, `教科信〔2026〕1号`, issued
  April 2026 by *five* bodies jointly**: the Ministry of Education with the **NDRC**, **MIIT**, the
  **Ministry of Science and Technology** and the **National Data Administration**. 🔵 **Five
  signatures is the fact to carry into a China conversation**: this is industrial policy with an
  education delivery arm, not a curriculum circular, and the data regulator is a signatory.
- 🟢 **The February 2026 national basic-education deployment meeting (Langfang) set the 2026 target
  as AI into `课程标准` (curriculum standards), `日常教学` (daily teaching) and `考试评价`
  (examination and assessment).** 🔴 **`考试评价` is the item to price**: assessment is the most
  regulated education use case in every jurisdiction this KB tracks, and China pairs it with
  **mandatory content labelling** (`T7`) and the affective-design restrictions of `T14`.
- 🟢 **Standing instruments it builds on**: 《中小学人工智能通识教育指南（2025年版）》 (K-12 AI
  general-education guide), 《中小学生成式人工智能使用指南（2025年版）》 (K-12 generative-AI use
  guide), and revised `信息科技` curriculum standards for compulsory and senior-secondary education.
  The plan also directs support for **rural and remote schools through the national platform** and
  strengthening of K-12 AI education bases. **Horizon: deep integration by 2030.**
- 🟡 **One widely repeated claim is media-only and is not carried as fact here**: that AI literacy
  will enter students' `综合素质评价` (comprehensive quality evaluation). It was not located in the
  plan's own text. Flagged, not used.

**Japan — a guideline revision is open *now*, and it names agentic AI.**

- 🟢 **The operative text is MEXT's 「初等中等教育段階における生成AIの利活用に関するガイドライン
  Ver.2.0」** (December 2024), addressed to teachers and boards of education. 🔵 **It neither bans
  nor mandates classroom generative AI**, and its organising principle is that **the final judgment
  and responsibility remain human** — which is the same human-oversight predicate `P7` and `P9` are
  built around, arriving as guidance rather than statute.
- 🟢 **A revision to `Ver.2.1` was opened on `2026-06-30`** at the Central Council for Education's
  Special Committee on Digital Learning Infrastructure, **deliberately ahead of the next
  `学習指導要領`**, in order to reflect **`エージェントAI` — agentic AI — explicitly**, alongside
  international debate and the academic risk literature. Planned within FY2026; **as of September
  2026 it had not been published**. Committee papers of `2026-04-30` and `2026-06-30` are primary
  PDFs on `mext.go.jp`.
- 🟢 **`2026-07-03`: MEXT revised its generative-AI *and security* guidance together**, in the
  frame of `次世代校務DX` — next-generation school-administration digital transformation.
  🔵 **Administration, not instruction, is where Japan is spending**, and that is an unusual
  entry point for this industry: the buyer is the board of education's back office.
- 🟢 **Why this is a window rather than a fact.** A national guideline whose revision is *in
  progress* and whose stated subject is agentic AI is the single most favourable timing signal in
  this file: the specification is being written, and `T1`'s rule — that regulation governs **use**,
  not existence — means a studio can build to the Ver.2.0 predicate and be ready for Ver.2.1.

**Korea — the clearest procurement inversion in APAC: a national mandate became a school choice.**

- 🔴 **The AI Digital Textbook (`AI 디지털교과서`, AIDT) was reclassified by the National Assembly
  from `교과서` (textbook) to `교육자료` (educational material).** It is **not abolished** — but a
  textbook is procured centrally and an educational material is **selected by the school**, subject
  to review by the `학교운영위원회` (school operating committee).
- 🟢 **The Ministry of Education's 2026 work plan drops "AI 디지털교과서" in favour of
  "`AI 교육자료`"**, and its named tasks are: **guidance on autonomous selection criteria**,
  development of **`K-교육 AI`** for both instruction and administration, and expansion of
  AI-focus schools. Reported rollout to elementary grades 5–6 and middle/high year 2 from
  **March 2026**. The 2026 ministry budget is **₩106.3607 trillion**, with AI money distributed
  across talent, infrastructure and capability rather than one AIDT line.
- 🟡 **Conflicting school counts, carried as a conflict**: one account gives **1,000 AI-focus
  schools** (`AI 중점학교`), another **1,900 AI-leading schools** (`AI 선도학교`) from 2026. Do not
  quote either as settled.
- 🔵 **Commercially this is the most actionable item in the APAC section.** The buyer moved from one
  ministry to **a thousand-plus schools and their committees**, the selection test became
  *"verified tools only"*, and the reported field complaints are **device management, teacher
  training and staffing** — none of which is a model problem. 🟢 **That is a services market, not a
  licence market**, and `P10` (teacher enablement at system scale) and `P8` (per-institution
  metering and exit) are the two patterns written for it.

#### `p914` — APAC: Australia is the region's **loosest regulation over its most AI-sceptical public**, and that inverts where the risk sits

`p908` recorded education becoming a *named* high-risk sector in a second APAC jurisdiction
(Vietnam, from 1 March 2026), alongside Korea's `AI Basic Act` in force 22 January 2026. Australia
is the counter-case, and this file had no row for its instrument (`National AI Plan` appeared zero
times before this pass).

| | **National AI Plan** (Australia) |
|---|---|
| Released | **2 December 2025** |
| Shape | **3 goals, each supported by 3 pillars of action.** One goal covers keeping Australians safe through legislative and regulatory frameworks |
| 🟢 Standalone AI Act | **Explicitly declined.** The government chose not to adopt an EU-style standalone AI Act, pursuing a flexible approach over existing law and voluntary guidance |
| Education status | Named a **national priority**; the plan references the schools framework and includes **piloting generative AI in schools** |
| The schools instrument | **Australian Framework for Generative AI in Schools** (2023) — endorsed by Education Ministers, 🔴 **guidance, not law**, and reported as released with no dedicated funding, no implementation support and no enforcement mechanism |
| Skills limb | Action 5, *"Support and train Australians"* — digital skills, training access, an AI-ready pipeline, led in part by education departments |

🔴 **The inversion, which is the actual finding.** This base already records (from the **Ipsos
Education Monitor 2026**, `T18`) that support for *banning* AI in schools **rose** in Japan,
Australia and South Korea, and that Australia and New Zealand showed the region's **strongest**
support for a ban. Put the two measurements together and Australia is the jurisdiction with the
region's **most permissive regulation and its least permissive public**.

🔵 **What that means for an engagement, concretely.** In Vietnam or Korea the binding constraint is
a statute: it is knowable in advance, it is the same for every bidder, and `P6` and `P4` exist to
build against it. In Australia the binding constraint is **consent** — parental, teacher-union and
ministerial — and there is no statute to point at as evidence of diligence, because the plan
declined to create one and the schools framework carries no enforcement. A deployment there fails
politically, not legally, and the mitigations are different in kind: opt-in defaults, teacher
authority over the agent's outputs, visible data residency, and an evidence tier (`P7`) sized for a
sceptical parent rather than a regulator. 🔴 **Do not reach for `P4`'s conformity apparatus here —
it answers a question nobody is asking and reads as deflection.** `P13`'s persona-stateless design
is the closer fit, since the objection it answers is about the relationship between child and
agent rather than about documentation.

🔵 **The pilot limb is the opening.** The plan includes piloting generative AI *in schools* and
Action 5 is led partly by education departments. That is a funded buyer with a mandate and no
compliance gate — the same structural position as Colombia's `CONPES 4144` (`p914`, LATAM), and the
two should be sold the same way.

🔴 **Provenance.** As with the LATAM leg this pass: non-GitHub hosts were unreachable from this
session (all six probed returned `000`), so this is **WebSearch summaries only, single channel**.
The release date, the declined AI Act, the 3×3 structure and the schools framework's non-binding
status are consistent across the sources; one source dates the higher-education framework in a way
inconsistent with the rest and is not relied on here. **Declared gap `914-G2`: read the
`National-AI-Plan-December-2025` PDF and the Australian Framework for Generative AI in Schools
directly, and extract Action 5's funded quantum.**

#### `p915` — one teacher-facing, in-language supply row

🟢 **Supply (new).** `forgemorrow/Chinese-Teaching-AI-Agent` — **MIT** (byte-read, 1,068 B), 8 ★,
pushed 2026-11-14. A lesson-prep assistant for **K-12 Chinese-language teachers**, Streamlit with the
MiMo/Anthropic SDK. 🔵 Two things make a small repository worth a row here: it is **teacher-facing**
rather than learner-facing, which is the thinner half of this market's supply, and it is
**in-language**, which is the shape `T29` measured as largely absent outside a single country. It is
also permissive, where the Chinese-origin platform tier in `verticals/solutions.md` (`SmartKBS`) is
AGPL-3.0.

🟡 **Opportunity.** `T29` and `T11` together say the binding constraint in APAC is **teacher
capacity**, not learner tooling, and the instruments that bind are curriculum mandates and teacher
licensing rather than AI statutes. A teacher-facing, in-language lesson-prep tier is therefore the
part of the stack a ministry or a provider can actually buy — and at 8 ★ this is a **component to fork
and own**, not a vendor to partner with.

🔴 **Demand side: nil.** Korea's AI Basic Act, Vietnam's education-high-risk listing, TEQSA's
regulatory-led posture and Australia's National AI Plan were all returned and all already written.


#### 🆕 `p927` — an adoption ceiling with a number on it, and a reading that contradicts `T18`

🟢 **The first APAC adoption figure in this file that is not a market forecast.** A *Times Higher
Education* survey of Asian institutions found **virtual-tutor adoption at 30% across the cohort**,
with uptake of new technology **"patchy"** across the region and **connectivity named as a
barrier** *(single source)*. 🔵 **30% is low against the 86%-of-organisations and
67%-of-teachers figures this file carries for generative AI generally** — which says the gap is not
*AI* adoption but **tutor** adoption specifically, and the stated reason is infrastructure. That is
the clearest regional case this file has for the **offline-first and on-device** tier
(`compose/patterns.md` **P14**, **P52**), and it is the argument to lead with in APAC rather than
the model quality.

🔴 **A contradiction this file is recording rather than resolving.** `p896` added **`T18`** on the
strength of Ipsos data showing support for **banning** AI in education **rising** across APAC, with
Australia at a **52% majority**. This pass's leg returns a summary of the **Ipsos Education Monitor
2026** stating that support for banning AI in schools is **lower** across the Asian markets
examined. 🔵 **Both readings are snippet-level summaries of the same publisher's work and the
markets in each cohort are probably not the same** — Australia is not "the Asian markets". The
honest position is that **`T18`'s direction is not confirmed by this pass and is not refuted by
it**, and that this file should not use either figure in a client deck until the Ipsos tables are
read directly. 🔵 Logged as an open question for `p928` rather than quietly dropped.

🟢 **Two convening instruments, new to this file, that are where APAC education-AI policy is
actually being written:**

- The **World Bank Global EdTech Policy Academy on AI**, **Seoul, 31 August – 4 September 2026** —
  a multi-country ministry-level programme.
- **Cambridge English** convened **200+ senior leaders including Ministries of Education** across
  Asia Pacific in **May 2026** to accelerate action on AI in education.
- **EdTech Hub** ran a Southeast Asia session in **March 2026** launching AI-in-education topic
  briefs on ethical governance, with **ASEAN–UK SAGE** support.

🔵 **Why a studio should care about convenings.** This file has repeatedly measured APAC as
**government-led** — the buyer is a ministry, and ministries buy after they have agreed a position
in rooms like these. **The procurement follows the convening by 12–24 months**, which makes the
attendee list a forward pipeline rather than conference news. **BCG (April 2026)** names the
binding constraint as **institutional alignment across ministries, providers, employers and
funders** — not technology — which is the same finding from the consulting side.


### LATAM

#### 🆕 `p928` — nil, and the nil is the strongest form of this region's standing story

🔴 **Zero new facts.** The leg re-named the Digital Education Council **AI in Higher Education LATAM 2026** survey (**92% of students, 79% of faculty** actively engaging with AI), the UNESCO **IESALC** finding that **87% of institutions use AI in some capacity while only 26% have a formal AI strategy**, PISA 2025's **nine in ten 15-year-olds** across thirteen regional countries having used AI chatbots for schoolwork, Brazil's **53% of school administrators using AI against 22% of schools with guidelines**, the **716 AI-related regulatory instruments across 23 countries and territories**, Brazil's EU-style draft framework against Argentina's explicitly deregulatory bill, and the **UNESCO Observatory on AI in Education for Latin America and the Caribbean** launched April 2026 with CAF, CENIA, Cetic.br/NIC.br, ECLAC, Fundación Ceibal, Fundación Santillana, Tecnológico de Monterrey, ProFuturo, Universidad del Desarrollo and IRCAI. **Every one already held.**

🟢 **That the leg is stable is itself the commercial point.** The adoption-versus-governance gap this file has sold against in LATAM for many passes — near-universal use, formal strategy in roughly a quarter of institutions — is **not** a transient measurement. It has now been returned by independent legs across multiple passes with the same shape. 🔵 **The deliverable that gap implies is the governance and evidence layer, not the tutor** — which is `P48` (the regulated-market tutor: ship the evidence layer, not the agent) and `P53` (attaching evidence to a tutor the client already has). A LATAM client overwhelmingly **already has** the AI; what they do not have is the policy, the audit trail and the outcome measurement.


#### 🆕 `p926` — the supply gap, measured: the software exists, in the right subject, with no licence on it

🔴 **This file has reported a LATAM open-source supply gap for many passes without measuring it.
`p926` measured it.** Of **601 unheld repositories** returned by 30 topic-qualified legs,
**11 are Spanish- or Portuguese-language education repositories, and not one is permissively
licensed.** Five were probed byte-level on `raw.githubusercontent.com`
(`evidence/latam-supply-grant-probe.2026-11-19-p926.tsv`):

| Repository | What it is | Grant, byte-read |
|---|---|---|
| `laurahernandez7-sudo/Tutor-inteligente-ingles---EVA` | Spanish-language **adaptive AI tutor for English learning** — precisely this KB's subject | 🔴 **no licence file on any probed path** |
| `jhondados/edu-desempenho-alunos` | ML prediction of student performance on Brazil's **ENEM**, identifying learning gaps | 🔴 **no licence file** |
| `reamat/Calculo` | Brazilian collaborative open courseware (UFRGS REAMAT estate, 6 repos) | 🔴 **no licence file** |
| `reamat/CalculoNumerico` | Same estate, numerical calculus | 🟡 **Creative Commons, written in Portuguese** (`master/LICENSE.md`, 303 B, `sha256₁₂ 54a16da9fcb5`). The search channel reports `NOASSERTION` — a **licence false negative in the non-English direction**, and a *content* licence, not a software one |
| `vruizz22/innova-backend-serverless` | Innova EdTech backend, NestJS + TypeScript + Prisma | 🟡 **GPL-3.0**, confirmed byte-read (35,149 B, `sha256₁₂ 3972dc9744f6`) |

🔵 **So the finding is not "nothing exists in LATAM".** The region's open education software exists,
it is in the right subject, and **its default licence state is no licence at all** — which under
default copyright means a Globant engagement cannot build on it, fork it or ship it. This is the
regional instance of the pattern `intel/trends.md` **T29** measured across eight languages, and it
is a **sharper** result than the global one because the subject match is exact.

🟢 **The opportunity that follows is different in kind from the other three regions.** Elsewhere the
work is to adopt permissive upstreams and add a layer. Here:

1. **Licensing as the first deliverable.** The assets exist and are unusable. An engagement that
   begins by getting a grant attached — with the institution that wrote the code — converts a dead
   repository into a reusable one, and is cheap.
2. **Bring the measurement layer to the curriculum, not the other way round.** `clementina-tom/PLRS`
   (MIT) is a prerequisite-constrained recommender that ships a **national curriculum graph for
   Nigeria**. Nothing equivalent exists for any LATAM national curriculum. The same pattern against
   the Brazilian BNCC or a Mexican SEP curriculum is a studio asset, and `repos/foundations.md`
   now carries the seven permissive knowledge-tracing implementations that would sit under it.
3. **The governance gap remains the live commercial opening** — 92% student adoption against 26% of
   institutions with a formal AI strategy (`p925`, above). That has not changed, and it is still the
   largest in the world.

🔴 **Declared gap, stated rather than implied: this pass found no LATAM-origin permissively licensed
AI-education repository at all.** Not a small one, not an old one. That is a measured nil against a
named channel (30 topic legs, 601 rows, dedupe against 6,535), not an unsearched one.


#### 🆕 `p925` — the highest adoption numbers in the world, attached to the thinnest institutional strategy

**The adoption figures are the headline, and they come from interested parties.** A Digital
Education Council survey of the region's higher education reports **92% of students and 79% of
faculty actively engaging with AI** — faculty accelerating but still behind students. **UNESCO
IESALC** found that among institutions using AI, **only 26% have a formal AI strategy**, and that
adoption is driven by individual academics, researchers and students rather than institution-wide
policy. In schools: **nine in ten 15-year-olds** across the 13 PISA 2025 countries in the region
have used AI chatbots for schoolwork; in **Brazil, 53% of school administrators use AI and only 22%
of those say their school has guidelines**.

🟢 **That gap — 92% usage against 26% strategy — is the engagement, stated in one line.** The demand
side is already saturated. What does not exist is governance: an acceptable-use policy with
technical enforcement, a disclosure record, an integrity posture, and an evidence trail. 🔵 This is
the inverse of the EMEA sale (there, the regulation exists and the capability is the gap; here, the
capability is in use and the governance is the gap).

**Regulation is voluminous and fragmented.** A 2026 Universidad de los Andes study identified **716
AI-related regulatory instruments, rules and legislative proposals across 23 countries and
territories**, mostly new since 2023; the WEF characterises regional AI and digital regulation as
**fragmented**. 🔴 **Brazil and Argentina are moving in opposite directions**: Brazil's legislature
is considering a framework borrowing heavily from the EU's approach *and* signed an AI and
tech-regulation agreement with the EU in June 2026, while Argentina's president submitted a bill
reported to include "a commitment to keep AI unregulated". 🔵 A regional deliverable cannot assume
one compliance posture; build the policy layer as configuration.

**Education-specific rules are sparse.** Chile's **CENIA** found **13 of 19** Latin American and
Caribbean countries studied **do not teach early AI adoption in schools**.

**Players.** The **UNESCO Observatory on AI in Education for Latin America and the Caribbean**,
launched **April 2026**, led by UNESCO with **CAF, CENIA, Cetic.br/NIC.br, ECLAC, Fundación Ceibal,
Fundación Santillana, Tecnológico de Monterrey and ProFuturo**. CENIA also produces the **Latin
America AI Index** and leads **Latam-GPT**.

🟢 **Opportunity — the Observatory is a named, funded, multilateral counterparty with a mandate and
no implementation arm.** Its consortium members are exactly the institutions that would commission
the governance layer above. 🔵 The permissive substrate for it is already on this base:
`portabilis/i-educar` and `portabilis/i-diario` (Brazilian SIS, in production in Brazilian
municipalities), `chamilo/chamilo-lms` for the LMS side, and `yetanalytics/lrsql` (Apache-2.0) for
the disclosure record. `zoonk/zoonk` (MIT, shelved this pass) is 🔵 **unplaced** — `925-F7` found no
artefact in the repository that places it, so it is *not* counted here as LATAM supply despite being
the kind of artefact this region produces.

🔴 **Gap, declared.** This leg returned **no repositories** and **no vendor landscape** — it is
entirely policy, survey and multilateral material. One source's country adoption table
(e.g. "Mexico (2026): 68%") is repeated and unsourced and is **not** used here.


#### 🆕 `p924` — the LATAM leg returned **nothing new**, for the second consecutive pass
🔴 **A measured nil.** Every named fact was already held: the UNESCO IESALC regional survey (200
institutions, 19 countries) and its adoption/governance gap; the LATAM higher-education survey's
**92%** of students using AI regularly and **67%** weekly; *only ~30% of universities have published
an AI policy*; the IDB's **193**-initiative catalogue and its *"AI Here!"* call; the ProFuturo/OEI
report; and the EdTech Hub / Fundación Ceibal partnership. Mexico's framing — that generative AI
*"requires regulatory alignment, institutional reform and curriculum redesign"* — is a restatement of
`T4`, not a new instrument.

🔵 **Two consecutive nils is itself the finding.** LATAM's constraint, as measured, is **not** a
shortage of pilots or of research voices; it is that **adoption has outrun governance by more than in
any other region this base tracks** — students at 92%, institutional policy at 30%. That gap is the
engagement: the saleable artefact is the policy-and-audit layer, not another tutor. 🔴 **Still
unmeasured here, and now two passes old:** no national AI-in-education statute for Brazil, Mexico,
Chile or Colombia has reached this shelf through any leg.

#### 🆕 `p923` — the LATAM leg returned **nothing new**, and the reason is worth naming
🔵 Every named fact was already held: the UNESCO IESALC working paper and its 200-institution,
19-country regional survey; the Digital Education Council / Tec de Monterrey LATAM survey
(29 universities, **92%** of students using AI regularly, **67%** weekly, **79%** of faculty);
*only 30% of universities have published an AI policy*; the IDB's 193-initiative catalogue; the
ILIA's *14% of global AI-tool visits against 11% of internet users*; and the EdTech Hub /
Fundación Ceibal partnership (Sept 2026). 🔴 **Zero repositories.**

🔴 **The gap that is not closing.** Four passes of English-language LATAM legs have returned
adoption and governance figures and **no open-source supply**. 🔵 That is consistent with what this
base measured directly: Brazilian Portuguese is **`NOT DELIVERABLE`** at the substrate tier
(`p921`, re-graded `p922` under `922-R1` — it passed only on a 106 ★ LGPL-3.0 verb conjugator), and
`p923` found the Portuguese catalogue tier is a **19 ★ index, ungranted, idle since 2017**
(`davidsbatista/awesome-Portuguese-NLP`, 507 B README). 🟢 **Cost a LATAM vernacular engagement as
P44 — deliberately no substrate** — and read the regional opportunity as governance retrofit
(`P5`), which is where the measured demand actually is.

#### 🆕 `p922` — Portuguese is **downgraded**, and the downgrade is this base correcting itself
🔴 **Portuguese moves from `DELIVERABLE` to `NOT DELIVERABLE`** under `922-R1`, the role test. It
had passed `918-R1` only on [`bretttolbert/verbecc`](https://github.com/bretttolbert/verbecc) —
**106 ★, LGPL-3.0, a verb conjugator for five Romance languages**. That is not a Portuguese stack
and it is not permissive, and a tier verdict that rests on it was overstating Brazil's open supply.
🔵 **What this changes for a Brazilian engagement:** the vernacular line item is a multilingual
model plus your own evaluation set and glossary — not an adoptable library. The
**national-curriculum data** cluster (`portabilis/i-educar` + `i-diario`, AGPL-3.0, 117 ★) is
unaffected and remains LATAM's strongest open asset.
🔵 Demand-side, nothing new: the Digital Education Council's LATAM survey (92% of students, 79% of
faculty, 30,000+ responses across 29 institutions), the IDB's 193 mapped initiatives and the
EdTech Hub / Fundación Ceibal partnership are all already on this shelf.

#### 🆕 `p921` — Brazil's Portuguese substrate measured, and the honest answer is that there is nothing to adopt

🔴 **Portuguese joins Indonesian and Indic in the empty column.** The tier's largest member,
[`ajdavidl/Portuguese-NLP`](https://github.com/ajdavidl/Portuguese-NLP) (375 ★), is a **curated list
with no licence file on either channel** — `search` reports `NULL` and the grant authority finds
nothing on 25 names over 4 branches. `Nkluge-correa/Tucano` (86 ★, Apache-2.0) is **268 days idle**.
The only maintained member, [`bretttolbert/verbecc`](https://github.com/bretttolbert/verbecc)
(106 ★), is **LGPL-3.0** and is a verb conjugator for five Romance languages, not a Portuguese stack.

🔵 **What to do with that in a Brazilian proposal, stated plainly because it is the commercially
useful part:** cost the engagement as *no substrate* — multilingual model, your own marked-answer
evaluation set, a versioned **BNCC** glossary, and a priced human-in-the-loop first cohort
(`compose/patterns.md` **P44**). 🔴 A competitor costing "we adopt the Brazilian NLP toolkit" is
costing a library that has not moved in two years, and the difference shows up in week six.

🟢 **This completes the LATAM supply picture this file has been assembling since `p917`:** Brazil's
*curriculum* cluster is deliverable (`portabilis/i-educar` + `i-diario`, AGPL-3.0, 117 ★), Mexico's
teacher-published supply is the clearest demand signal and the least deliverable (`920-F7`, largest
repo **2 ★**), and the *language* layer underneath both is **absent**.

#### 🆕 `p920` — Mexico, measured for the first time: 74 repositories, the largest is 2 ★

🔴 **Until this pass Mexico had never been measured by this base** (`919-G6`). Four Spanish-language
supply legs — `Nueva Escuela Mexicana`, `planeación didáctica`, `CONALEP`, `telesecundaria` — returned
**74 distinct repositories, every one of them previously unseen**, and the whole population tops out at
**2 ★** with **4 of 74** carrying any licence
([record](../evidence/mx-supply.2026-11-19-p920.tsv)).

- 🔵 **Read this as a demand signal, not a supply one.** These are working teachers shipping
  *planeación didáctica* generators aligned to the **Nueva Escuela Mexicana** — *campos formativos*,
  *ejes articuladores* — for their own classrooms, several pushed within the last month, and almost
  none of them licensed. The need is being met by hand, repository by repository, because nothing
  buyable or forkable addresses it.
- 🔴 **There is nothing in it to adopt.** Zero of 74 pass this base's deliverability threshold
  (`918-R1`: ≥ 50 ★ · a byte-read grant that is not `NONE` · pushed within 180 days). Four of eight
  repositories byte-read carry **no licence file on any probed path**.
- 🔵 **And unlike the APAC tiers there is no substrate layer to fall back on, because Spanish does
  not need one.** Thai and Japanese require a tokeniser somebody must ship, so a Thai engagement can
  stand on `PyThaiNLP` with no tutor; Spanish is served by the global substrate this file already
  holds. **For Mexico the agent-layer verdict is the whole verdict** (`repos/trending.md` `920-R2`).
- 🟢 **The offer:** build the agent, adopt the NEM curriculum vocabulary. The *campos formativos* and
  *ejes articuladores* encoded by hand across those 74 repositories are precisely the part a tutor
  built outside Mexico gets wrong, and they are free to read.
- 🟡 **Scope limit, stated rather than implied:** these four legs measure **open-source supply**. They
  say nothing about the Mexican commercial market, SEP procurement, or institutional adoption rates,
  none of which this file has ever carried for Mexico. That remains open.

#### 🆕 `p919` — a second independent leg returns the same two headline figures, and the gap between them is still the offer

- 🟢 **Corroborated on a fresh leg, at the same values**: the Digital Education Council's 2026 LATAM
  higher-education survey at **92% of students and 79% of faculty** actively using AI, UNESCO IESALC
  at **87% of institutions using AI and 26% holding a formal strategy**, the **716 AI regulatory
  instruments across 23 countries** counted by Universidad de los Andes (80%+ initiated since 2023),
  and the **UNESCO Observatory on AI in Education for LATAM** (April 2026, with CAF, CENIA, Ceibal,
  Fundación Santillana, Tecnológico de Monterrey and ProFuturo).
- 🆕 **One figure this file did not hold**, from the PISA 2025 regional read: across the **13 LATAM
  countries assessed, around nine in ten 15-year-olds have already used an AI chatbot for
  schoolwork**, while in Brazil **53% of school administrators report using AI and only 22% report
  their school has any guidance on it**. 🔵 That is the `87%/26%` institutional gap reproduced **one
  tier down, in schools rather than universities** — the same shape, measured on a different
  population by a different instrument, which is the strongest form this file's central LATAM claim
  has taken.
- 🔵 **The offer is unchanged and better evidenced: governance, not capability.** Adoption is
  near-universal and self-directed at both tiers; strategy, policy and teacher guidance are where the
  measured deficit is, in higher education and in schools alike.


#### 🆕 `p918` — the governance gap is now quantified by UNESCO, and it is the offer

- **UNESCO IESALC 2026, 200 institutions across 19 countries: 87% use AI in at least one area and
  only 26% have a formal strategy.** 🟢 **The best-sourced statistic in this file for the LATAM
  pitch** — the sale is governance for AI already in use, not adoption.
- **The Digital Education Council LATAM survey (with Tecnológico de Monterrey) reports 92% of
  students and 79% of faculty actively engaging with AI.**
- **K-12, national sources:** Uruguay **75% of public-school teachers** use these tools (Ceibal);
  Brazil **53% of school administrators** use AI with **22%** reporting guidelines (Cetic.br).
- **Regulatory volume, newly measured:** a 2026 **Universidad de los Andes** study counts **716
  AI-related regulatory instruments, rules and legislative proposals across 23 countries and
  territories**, most launched since 2023. 🔵 Fragmentation *is* the product requirement.
- **Brazil** `PL 2.338/2023` (risk-based) passed the Senate 10 December 2024; the Chamber stage is
  still pending. **Colombia** took the softer route — **CONPES 4144** (February 2025), a funded
  national policy to 2030 rather than immediate horizontal obligations.
- **UNESCO launched a regional Observatory on AI in Education in Santiago in April 2026.** 🔵 A named
  regional convener is a route to reference customers.
- 🟢 **Supply (carried, now graded under `918-R1`):** the **national-curriculum and
  national-examination cluster passes all three deliverability tests** — `portabilis/i-educar` +
  `i-diario`, AGPL-3.0, 117 ★, actively pushed. 🔴 **The general-purpose vernacular tutor fails all
  three**, in Spanish (240 results, 5 ★ ceiling, unlicensed) and Portuguese (27, 7 ★, unlicensed).
- 🔵 **Offer, sharpened:** **bring the tutor, adopt the curriculum spine** — and sell the governance
  layer that the 87%/26% gap describes.

🟢 **One row placed LATAM this pass, and the channel that placed it is the transferable part.**
`marceloschmitt/moodle-block_analytics_graphs` (GPL-3.0-or-later) was carried **unplaced** by `p916`
and is now placed **Brazil** — from the `@copyright` line of its Moodle `version.php`, which carries
the institutional e-mail domain `poa.ifrs.edu.br` (Instituto Federal do Rio Grande do Sul, Porto
Alegre), with a **2026** copyright year. Half of `916-G6` discharged. 🔵 The generalisation now
drives a committed instrument (`ingest/p917-affiliation-manifest.sh`): **where a README carries no
country signal, the packaging manifest often does.**

🔴 **And a correction to how this base has been reading LATAM supply.** `p917` refuted `p890`'s
LATAM Spanish and Portuguese "voids" **on count** — `plataforma educativa aprendizaje` returns
**240** against the original shape's 4, and `educacao plataforma ensino` returns **27** against 2.
🔴 **But the shelf is still empty: the most-starred row in those 240 has 5 stars**, and in the 27 it
has 7. **A refuted count is not a populated shelf**, and publishing the 240 without the
top-of-shelf figure would misrepresent regional supply as something a client could build on
(`917-F2`, `T978`).

🟡 **Demand-side, re-measured `p917`, and the adoption-governance gap is the sellable one.** The
Digital Education Council's 2026 LATAM survey puts **92% of students and 79% of faculty** actively
engaging with AI while **only 30%** believe their institution has responded effectively — the widest
adoption-versus-readiness gap of any region this base measures. UNESCO IESALC's September 2026
working paper finds significant gaps **between private and public universities**; the IDB's analysis
of **193 initiatives** describes the region as building *hybrid, context-sensitive* systems rather
than importing designs. EdTech Hub and **Fundación Ceibal** announced a regional partnership in
September 2026. 🔵 **The engagement is institutional AI governance, not tooling** — the tools are
already in use.


🟢 **Opportunity added `p916`, and it is the strongest regional supply finding in this pass.**
**The only actively-developed standalone open-source Open Badges platform this base can find, in any
region, is LATAM-origin**: `gdgguadalajara/open-badges-platform` (**AGPL-3.0**, Guadalajara,
**Mexico**, pushed 2026-08-31), self-described as *"sovereign, immutable and standard-compliant
recognition"*. Everything else with stars in that tier is a dead 2011–2020 Mozilla artefact
(`916-F4`). 🔵 **"Sovereign" is the client-facing word here** — a Mexican, Colombian or Brazilian
public client evaluating micro-credentials gets a regionally-authored, standards-compliant base and
a data-residency story in one. 🔴 AGPL-3.0, so this is **deploy-and-extend or reference
architecture, never white-label**; if the client needs a closed product the fork point is Finnish
and five years idle (`salava`).

🟢 **And the fluency tier reaches Brazil:** `JambuOverflow/lepic` (GPL-3.0, **University of Pará**)
won the **ICSE 2021** Student Contest on Software Engineering for exactly the early-literacy
workflow `P37` describes. Idle since 2021 — a design reference, and a credible local citation.


🟢 **Promoted in `p902` — two facts held only in the log** (method: `902-F1`):

- **UNESCO IESALC surveyed 200 institutions across 19 countries (2025).** This file already carried
  IESALC's 87%-use / 26%-formal-strategy headline; **the sample behind it is published here for the
  first time**, and it matters when the number is quoted to a client: 200 institutions across 19
  countries is a regional census, not a convenience sample, which is more than can be said for most
  figures in this file.
- 🔴 **The "Rest of Latin America" AI-in-education market is estimated at roughly USD 18.2M (2024).**
  Set against a global market of ~USD 10.6B, that is **under 0.2%**. 🔵 **This is the honest frame
  for a LATAM engagement, and it is not a reason to deprioritise the region** — it says the money is
  not in licence-fee markets outside Brazil and Mexico, so the sellable work is **public-sector
  delivery, enablement and governance retrofit** (which is exactly what `P5` and `P14` scope) rather
  than per-seat product. Quote it before a client's board does.

🟢 **Supply side, p899 — and this materially qualifies this KB's standing "LATAM supply is near
zero" finding.** It is near zero *in education-specific agents*. It is **not** near zero in the
public-sector substrate education runs on:

- 🔵 **`Mcp-Brasil/mcp-brasil` — MIT, 1,865 ★**, an MCP server over **70 Brazilian public-sector
  APIs**. Placed LATAM on a stripped-README Portuguese score of **228 at spread 0.977**.
  **This is 66× the largest LATAM-origin asset this KB had previously verified** (`usp-mcp`,
  28 ★). It is not an education product — it is the **government-data access layer** a Brazilian
  public-education engagement would otherwise hand-build, and it is permissively licensed.
- **`menthorlabs/menthor`** — **Apache-2.0**, 581 ★, a free Brazilian programming-education
  platform. 🟡 **Last push 2024-04-21 — 19 months dormant.** Evidence of what was built, not a
  dependency.
- Already shelved: `portabilis/i-educar` + `i-diario` (the Brazilian public-school stack),
  `CaioCastro1/usp-mcp`, `warleysr/ankipa`, `Antonio-Neves/Gestao-Escolar`.

🟡 **Demand side, refreshed p899 (search-mediated secondary sources; figures conflict and are
labelled):** **CEPAL (2026)** places **Chile, Brazil and Uruguay** in the pioneer group for AI
readiness, and reports the number of countries with AI content in school curricula rising from
two (2024) to several in 2026, with **enterprise adoption still early-stage**. A UNESCO figure
relayed secondhand holds that **LATAM has the world's highest GenAI adoption rate among
university students while only ~19% of institutions have an approved internal policy** — the
adoption/governance asymmetry this section already documents, now visible at the institutional
layer. **Money, named:** **Google.org committed $4.6M to AI education across nine Latin American
countries**, implemented by the **Raspberry Pi Foundation** (Experience AI), targeting **24,000
educators and 1.25M students by 2028**; **Luca (Mexico)** raised an **$8M Series A** led by
6 Degrees Capital for K-12 AI; **Elevify (Brazil)** raised **$1.35M** seed; **Teachy (Brazil)**,
an AI lesson-preparation incumbent, **has expanded into Asia**. **HolonIQ's 2026 LATAM EdTech
100** puts **Brazil at nearly half the cohort** and most deal activity. 🔴 **Two cautions.**
Sector share is contested — one source puts EdTech at **4–6% of LATAM VC deals and declining**
even as AI funding hits records; and a widely repeated *"$412M for educational AI 2026–2028"*
figure is **Colombia's, not Brazil's**, and is miscited in at least one secondary source.
🔴 **Regulatory state:** Brazil's **PL 2338/2023** is reported both as approved and as still in
passage by different sources — **unresolved here**; **Mexico has no federal AI law** (as of
July 2026), though the **Estado de México amended Article 61 of its state education law in April
2026** to promote responsible AI use in upper-secondary and higher education; Chile has had a
National AI Policy since 2021 with a bill in discussion.


**Adoption is genuinely ahead of the OECD — governance is not.** This is the region's defining
asymmetry, and it is quantified:

- **Teacher AI use (TALIS 2024):** Brazil **56%**, Chile **55%**, Colombia **53%**, Costa Rica
  **52%** — against an **OECD average of 36%**. LATAM teachers use AI more than their OECD
  peers.
- **The governance gap:** in Brazil, **53% of school administrators use AI but only 22% report
  school guidelines** on its use. In higher education, **UNESCO IESALC finds 87% of
  universities already use AI but only 26% have a formal strategy**.
- **IDB** reviewed 193 regional initiatives: **59% used generative AI**, many combining several
  modalities.
- **Students, not just teachers (new, PISA 2025):** across the **13 Latin American and
  Caribbean countries** assessed, **nine in ten 15-year-olds have already used AI chatbots for
  schoolwork**. This is the strongest adoption datapoint in this file for any region, and it
  comes from an international assessment rather than a vendor survey.
- **Higher education (new, Digital Education Council LATAM survey 2026):** **92% of students**
  across **29 institutions** and **79% of faculty** actively engaging with AI.
- **Curriculum is the laggard, not usage (new, CENIA):** of **19** LAC countries studied by
  Chile's National Centre for AI, **13 do not teach early AI adoption in schools**. Students and
  teachers are using AI that the curriculum does not acknowledge.
- UNESCO: AI is spreading quickly but unevenly, with institutional rules lagging.

**Regulation.** **Brazil** is the regional bellwether — **PL 2338/2023**, a comprehensive
horizontal statute whose text covers education applications, remains **pending**. **Mexico**
is behind: a 2018 national AI strategy under revision, and **no Mexican AI bill enacted as of
early 2026**.

**The fragmentation is now quantified (new).** A 2026 **Universidad de los Andes** study
identified **716 AI-related regulatory instruments, rules and legislative proposals across 23
countries and territories**, **more than 80% initiated since 2023**. And the region is
polarising rather than converging: **Brazil signed an AI and tech-regulation cooperation
agreement with the EU** (June 2026), aligning itself with the Brussels model, while
**Argentina's** president submitted a bill carrying "a commitment to keep AI unregulated".
**Delivery consequence:** a LATAM multi-country rollout cannot assume one compliance target the
way an EMEA one can. Build the policy layer as configuration — the same per-jurisdiction
pattern `compose/patterns.md` P3 uses for US states — and price the jurisdiction matrix as
discovery work, not as an afterthought.

**Institutional players (new, and this is the BD map).** The **UNESCO Observatory on AI in
Education for Latin America and the Caribbean** launched in **April 2026 in Santiago**, led by
**UNESCO** with the **Development Bank of Latin America and the Caribbean (CAF)** and Chile's
**CENIA**, and including **ECLAC**, **Fundación Ceibal** (Uruguay), **Fundación Santillana**,
**Tecnológico de Monterrey** and **ProFuturo**. That is a named, funded, multilateral coalition
with a regional mandate — the right door for a regional education engagement, and a shorter
path than approaching ministries one at a time.

**Sovereign inference now has a LATAM answer (new).** **Latam-GPT**, built by **CENIA**,
launched **10 February 2026** as an open model trained on Latin American data, framed by CENIA
as "a foundational open technology base" for regional derivative models; later versions are
planned on a supercomputer at the **Universidad de Tarapacá**. In late February 2026 **UNESCO's
Santiago office and CENIA signed a cooperation agreement** on responsible AI in education, with
**Latam-GPT integration named as an early milestone** and the model intended to support
**Ministries of Education** and the Observatory itself. **Why it matters:** this KB's T6 thesis —
sovereign/local inference as a procurement requirement — previously had European instances only.
LATAM now has a regional model with multilateral backing. *Caveat: schools use is a stated
expectation, not a documented deployment, and sources disagree on launch dates (one gives
February 2025, one a September launch). Verify status before committing it to a client
architecture; `ollama` with an open-weights model remains the defensible default.*

**Players and funding.** Brazil accounts for **nearly half** of HolonIQ's 2026 Latin America
EdTech 100 cohort and the clear majority of deal and award activity; named AI companies include
**Teachy** (AI lesson preparation) and **Vetto** (recently raised). In Mexico, **Ginia**
(AI-driven employability), **Talisis** and **Mattilda** (post-secondary and financing).
**Google.org committed $4.6M** with the **Raspberry Pi Foundation** to scale the Experience AI
curriculum across **nine countries**, targeting **1.25M students by 2028**.

**Opportunity.** The 53%-use/22%-guidelines gap is the offer: **governance and enablement, not
tooling**. Institutions are already using AI and know they are exposed. A packaged
"AI-use policy + teacher training + audit logging" engagement sells against a problem the
client can already see, and it is deliverable in weeks. Brazilian public-sector work has a
specific substrate — **i-Educar (LGPL)** is built around Brazilian regulatory requirements and
is the right SIS starting point. Cost discipline matters more here than elsewhere: `litellm`
budget caps plus local `ollama` inference keep per-student cost predictable in
currency-volatile markets. Equity/connectivity work is a real segment — **Kolibri (MIT)**,
**Internet-in-a-Box (LGPL)** and **Project NOMAD (Apache-2.0)**. Note the build gap: there is
almost no LATAM-origin open education agent (only `warleysr/ankipa`, an Anki add-on), so
expect to localise APAC- or EMEA-origin assets — and note that Spanish/Portuguese pedagogical
localisation is itself billable differentiation. **Two additions from this pass.** First, the
PISA 2025 nine-in-ten figure changes the pitch for school systems: the question is not whether
students will use AI but whether the institution has any visibility into use that is already
universal — which makes **detection-free, assessment-redesign work** (not proctoring) the
honest offer. Second, the **UNESCO/CAF/CENIA Observatory** is the regional entry point, and
**Latam-GPT** gives a sovereignty story that does not depend on a US API — pair it with the
`ollama`/`litellm`/`qdrant` stack so the model stays swappable while the architecture stays
local.


#### p891 additions — LATAM

**The adoption-governance gap is now quantified at three levels, and every number points the
same way.**

| Level | Use | Governance | Source |
|---|---|---|---|
| Higher ed, students / faculty | **92% / 79%** actively engaging with AI | — | Digital Education Council with Tecnológico de Monterrey, 2026 |
| Institutions | **87%** use AI in some capacity | **only 26%** have a formal AI strategy | UNESCO IESALC |
| Schools (Brazil) | **53%** of administrators use AI | **only 22%** report school guidelines | cited via UNESCO |
| Students, 15-year-olds | **~9 in 10** have used AI chatbots for schoolwork, across the 13 regional countries assessed | — | PISA 2025 via UNESCO |

**A 61-point gap between institutional use (87%) and institutional strategy (26%) is the single
largest quantified governance deficit in this entire KB, in any region.** The KB's existing
"53/22 gap" pattern (P5) was built on the Brazilian school figure; it now has a higher-education
analogue, at a larger institution size and with a bigger gap.

**Regulatory fragmentation is now counted.** A **2026 Universidad de los Andes study counted 716
AI-related regulatory instruments, rules and legislative proposals across 23 countries and
territories, more than 80% initiated since 2023.** The region's problem is not absence of
regulation; it is **incoherence** — and that is a different, more tractable service offering
(multi-jurisdiction mapping) than the compliance-readiness work sold in EMEA.

**The two poles are now explicit.** **Brazil's** legislature is considering a draft AI framework
borrowing heavily from the EU approach, and **Brazil signed an AI and tech-regulation agreement
with the EU in June 2026**. **Argentina** is moving the opposite way: the Milei government
submitted a bill containing *a commitment to keep AI unregulated*. A regional client with
operations in both cannot run one compliance posture, and that divergence is itself the
engagement.

**School-level AI education barely exists.** **CENIA reports that 13 of the 19 Latin American
and Caribbean countries studied do not teach early AI adoption in schools.**

**The institutional map has a new centre.** **UNESCO launched the Observatory on Artificial
Intelligence in Education for Latin America and the Caribbean in April 2026**, at ECLAC
headquarters in Santiago, Chile — led by UNESCO with **CAF, CENIA, ECLAC, Fundación Ceibal,
Fundación Santillana, Tecnológico de Monterrey and ProFuturo**. UNESCO IESALC's accompanying
recommendation is that governments **fold higher education into national AI strategies, fund it,
issue national guidance, and integrate AI literacy and governance into accreditation**.

**Why that last clause is the commercially important one.** *Accreditation* is a budget trigger
in a way that guidance is not. If AI governance enters accreditation criteria, every institution
acquires a dated, externally audited obligation — and the Observatory's partner list is
precisely the set of bodies that would carry it. **Track the Observatory's outputs as a leading
indicator of LATAM demand**, and note that CENIA — which also runs **Latam-GPT** and the annual
Latin America AI Index — sits inside it, which links the governance agenda to a regional model
this KB already tracks.

**Opportunity — LATAM, sharpened.** The 87/26 institutional gap is the headline: near-universal
use, almost no strategy, at institutions with procurement capacity. Lead with **governance
retrofit at higher-education scale** (P5 applies, resized), attach **multi-jurisdiction mapping**
against the 716-instrument fragmentation, and position against accreditation rather than against
legislation — the former has a budget owner.

#### p893 additions — LATAM: a far larger adoption dataset, and the governance gap holds at scale

The LATAM section's headline numbers have been the Brazilian 53%/22% school figure and the
87%/26% regional-university figure. **A larger and better-sourced dataset now corroborates both
and raises the adoption side.**

**Digital Education Council × Tecnológico de Monterrey, *AI in Higher Education LATAM Survey
2026*:** **92% of students and 79% of faculty are actively engaging with AI**, from **7,319
faculty respondents across 29 higher-education institutions** in the region. Against that,
coverage of the same survey reports **only ~30% of Latin American universities have published
policies on how AI should be used**.

**So the gap is now measured three times, at three sample sizes, and it widens as the sample
grows:**

| Source | Use | Governance | Gap |
|---|---|---|---|
| Brazilian school administrators | 53% | 22% have guidelines | 31 pts |
| Regional universities (earlier pass) | 87% institutional use | 26% have a strategy | 61 pts |
| **DEC × Tec de Monterrey, 7,319 faculty / 29 institutions** | **79% faculty / 92% students** | **~30% have published policies** | **~49 pts (faculty), ~62 pts (students)** |

**This is the most robust finding in the LATAM section and it should lead the pitch.** Three
independent instruments, three different populations, one result: **use is near-universal,
governance is at roughly a quarter to a third, and nothing in the trend suggests governance is
catching up.** The DEC survey also characterises LATAM faculty as *high adoption, conservative
usage* — they are using it cautiously and without institutional cover, which is precisely the
population a governance-and-enablement engagement serves.

**UNESCO IESALC working paper (September 2026)** maps AI use across universities on five
dimensions — teaching and learning, research, community engagement, administration, and
governance — and finds adoption "neither uniform nor evenly distributed", calling for stronger
governance and greater investment in digital literacy. A UNESCO-linked survey of **200
institutions across 19 countries** reports the adoption/governance divergence as especially
pronounced in the region.

**Institutional players to know, because in LATAM the convenors are the route to market:**
**UNESCO IESALC** and **UNU-IAS** (research and policy); **Digital Education Council** with
**Tec de Monterrey's Institute for the Future of Education** (the survey instrument);
**UNESCO and Chile's CENIA**, who have signed a cooperation agreement on ethical AI in
education **that explicitly covers integrating Latam-GPT**, the regional open LLM; **EdTech Hub
and Fundación Ceibal**, who announced a regional AI-in-education partnership in September 2026;
the **IDB**; and **ECLAC** through the eLAC digital agenda.

**The UNESCO–CENIA agreement is the one to act on.** Latam-GPT moving from a research artefact
into a UNESCO-blessed education deployment path is the first time this KB has seen a regional
sovereign model with an institutional channel into classrooms. Pattern **P5** already names
Latam-GPT in its stack; this gives that choice an endorsement to cite in a procurement document,
which is usually what it lacks.

**Caveat.** There is **no binding regional AI-in-education regulation**; the regulatory picture
is national and institutional. The ~30% policy figure is reported second-hand from survey
coverage, and a separate finding that ~30% of students believe their institution responded
effectively is a *different* statistic — do not conflate them, as some coverage does.


**`p896` additions — search-snippet evidence, source named.**

- 🟢 **UNESCO has launched an AI-in-Education Observatory for Latin America and the Caribbean**,
  presented at the **2026 LAC Forum on Sustainable Development in Santiago**. 🔵 This is the
  region's first standing instrument for comparable AI-in-education data, and it is the natural
  venue to publish the outcome measurement **P7** exists to produce. An engagement that
  instruments its results against the Observatory's framing gets regional visibility that a
  vendor case study does not buy.
- 🟡 **The regulatory volume is large and none of it is education-specific.** A regional AI
  regulation database (v3.1) records **716 instruments**, concentrated in **Brazil (212)**,
  **Mexico (126)** and Colombia — while **fewer than a quarter of Ibero-American countries have
  specific AI regulation at all** (Forbes Chile, Feb 2026), and analyses of higher education find
  **no unified regulatory framework for AI in education anywhere in the region**. 🔵 **This
  sharpens the standing LATAM finding rather than contradicting it**: the gap is not an absence of
  rulemaking, it is an absence of *sectoral* rulemaking. The binding constraints on a LATAM
  education build are **data protection and consumer law**, not an education AI statute.
- 🟡 **Chile's bill is still a bill.** Boletín **N° 16.821-19** remained in Senate passage through
  March–April 2026. Chile leads the region on national AI policy (since 2021) and still has no
  statute in force.
- 🔵 **Mexico has neither a national AI law nor binding university guidelines**, while university
  AI use grows — the governance-after-adoption shape this file documents for Brazil, in a market
  with 126 recorded instruments and none of them sectoral.



#### Supply side — rewritten `p904` after the first Spanish/Portuguese repository search

- 🔴 **This file's standing "LATAM produces almost no open education software" finding was an
  artefact of searching in English.** No pass before `p904` had run a Spanish- or
  Portuguese-language repository search. 26 such queries, including the national-examination names
  (`ENEM`, `vestibular`, `simulado ENEM`, `Saber 11 ICFES`, `PAES`, `EXANI`), returned **six
  LATAM-origin agents now shelved in `agents/top.md`** (up from one), a **five-repository Brazilian
  national-curriculum cluster** in `repos/foundations.md`, and **two AGPL platforms** in
  `verticals/solutions.md`. Every licence byte-read.
- 🟢 **What LATAM builds, stated as a market fact a studio can sell against: the national
  examination and the national curriculum.** ENEM essay grading
  (`matheussilvano/mooose`, Apache-2.0), ENEM mock exams (`migueldsants/OpENEM`, AGPL-3.0),
  Saber 11 prompt generation (`CREARED-EDU-CO/GenPrompt-Pre-ICFES-11`, Colombia, AGPL-3.0), and
  **Brazil's Base Nacional Comum Curricular published as verified open data with a Zenodo DOI,
  per-record provenance, npm/PyPI packages, two independent MCP servers and an open
  LLM-hallucination benchmark** (`bncc-dev`, MIT + CC BY 4.0, maintained by **Profy Tecnologias
  Educacionais Ltda**, Brasília). 🔵 **These are the artefacts every school in a country shares,
  which is why open source forms around them and why they are the right entry point for a
  public-sector engagement.**
- 🔴 **What LATAM does not build is the general-purpose tutor.** The Spanish-language tutor channel
  tops out at **6 ★ and unlicensed**; the Portuguese at 3 ★. **So the localisation offer inverts
  the one this file used to give**: bring the tutor, adopt the curriculum spine.
  `compose/patterns.md` **P23** is written for that shape.
- 🔴 **The gap moved rather than closed, and it is now actionable: Spanish-speaking LATAM outside
  Colombia.** Mexico — the region's second-largest education system — returned a **0 ★ ceiling** on
  `EXANI examen` and **no repository in any of the 26 queries**. Argentina, Peru and Central
  America returned nothing. Chile's only licensed entry
  (`HuemulSolutions/Enola-AI`, BSD-3-Clause) is **1 ★ and dormant since 2024-12-31**.
- **Adoption evidence promoted from the research log this pass** (it had been captured and never
  published here): the Digital Education Council's LATAM survey — run with **Tecnológico de
  Monterrey** and its Institute for the Future of Education, already cited in this file by its
  92%/79% headline — rests on **over 30,000 responses from 29 institutions**, which is what makes
  it citable in a procurement conversation rather than a statistic. **88% of faculty report
  "minimal" to "moderate" engagement**, and only **~30% believe their institution has responded
  effectively** to AI: the governance-after-adoption gap this file documents, measured on the
  faculty side.
- **The IADB has published a review of 193 AI-in-education solutions** across Latin America and
  the Caribbean (promoted from the log, `p904`). 🔵 **Read it as the region's de facto solution
  landscape** — the nearest thing to a market map a studio can cite to a ministry — and as
  corroboration that the region's activity is in *deployment*, while the open-source supply
  measured above is in *curriculum and assessment infrastructure*.
- **`OpenAI "Education for Countries"` is reported at eight adopting countries** (promoted from
  the log, `p904`; industry reporting, not an OpenAI primary source — the egress proxy blocks
  every non-GitHub host, so it is recorded as a named, unverified claim). 🔵 **If accurate it is
  the competitive frame for every national-scale LATAM education engagement**: the studio is not
  selling against another integrator, it is selling governance, localisation and curriculum
  grounding on top of a free national offer.


#### p905 additions — LATAM: the early-AI-curriculum gap, promoted out of the trend log

- 🔴 **13 of the 19 Latin American and Caribbean countries studied by CENIA (Chile's National Centre
  for Artificial Intelligence) do **not** teach early AI adoption in schools.** This KB has carried
  the figure since the pass that found it, in `intel/trends.md` and the append-only log — **never in
  this file**, which is where an engagement looks for what to sell into a region. Promoted here by
  the `902-G1` re-score.
  🔵 **Why it is an opportunity and not just a deficit.** It sits directly against two facts already
  in this section: **92% of LATAM higher-education students and 79% of faculty** actively use AI
  (Digital Education Council), and **only 22% of Brazilian schools whose administrators use AI have
  any guideline on its use** (53% use / 22% governed). Demand is present at the student layer,
  governance is absent at the institution layer, and **curriculum** is absent at the system layer.
  The sellable unit is the middle one — see `compose/patterns.md` **P5** (governance-and-enablement
  retrofit) and **P10** (curriculum-mandate delivery at system scale), the second of which has a
  buyer in every one of the 13.
  🔴 **Attribution, not verification.** CENIA's study is cited here from secondary coverage;
  `www.unesco.org` and the other primary hosts are refused at this session's egress proxy, so the
  count is recorded with its source named and **not** as a measured figure, under the `557-D` rule
  that has already refused five US legislative counts.

#### p906 — LATAM: searched, nothing new

🟡 **Declared null, not silence.** The `p906` leg
(`AI education LATAM Latin America 2026 adoption regulation players`) returned 9 sources and **0
facts absent from the delivery files**. Re-checked and already held: the **Digital Education
Council** 2026 regional survey (92% of students, 79% of faculty engaging with AI); **UNESCO
IESALC** (87% using AI in at least one area, 74% in teaching and learning, **only 26% with a formal
AI strategy**); **PISA 2025** showing nine in ten 15-year-olds across thirteen LAC countries having
used AI chatbots for schoolwork; Brazil's 53%-of-administrators / 22%-with-guidelines split; the
**Universidad de los Andes** count of **716 regulatory instruments across 23 countries**, 80%+ since
2023; **CENIA's** finding that 13 of 19 countries do not teach early AI; the Brazil-versus-Argentina
regulatory divergence; **Latam-GPT**; and the **UNESCO LAC Observatory** launched April 2026 at ECLAC
Santiago with its full partner list. 🔵 **Supply side unchanged from `p904`:** this pass's
discovery budget went to the eight APAC language channels, so the Spanish/Portuguese ceiling
`p904` measured still stands, and **Mexico remains the largest supply-side hole in this KB.**


#### Added `p907` — Mexico's instrument named, and the regional observatory

- **Mexico: the `Federal Law Regulating Artificial Intelligence` is the named instrument, and it is
  still under Senate discussion.** Sources conflict on status — one holds that *enacted 2026
  amendments already create the first binding obligations with direct compliance implications*,
  another that *multiple AI bills have been introduced and none enacted as of early 2026*, a third
  that the Federal Law *remains under Senate discussion with passage expected in 2026*. 🔴 **The
  conflict is recorded rather than averaged.** A separate criminal-law reform on AI deepfakes is
  pending Senate approval. Mexico's renewed data-protection law adds a **right to object to
  automated decisions**, which is the operative obligation a school-facing deployment meets today.
  🔵 **Mexico remains this file's largest LATAM gap on both axes** — `p904` found no Mexico-origin
  education repository in 26 queries and no `EXANI` tooling above 0 stars, and the statute that
  would govern a deployment there is not yet law.
- **Brazil: pending `PL 2338`, the operative supervisory body is the `ANPD`** and the operative
  instrument is the **LGPD**, which already recognises a right to request review of automated
  decisions. 🔵 This is the practical answer to "what do we comply with now" for a Brazilian
  engagement, and it is a *data-protection* answer, not an AI-Act-shaped one.
- **UNESCO has launched an observatory of AI in education for Latin America and the Caribbean.**
  🔵 A regional, institutionally credible reference point a studio can cite in public-sector
  procurement — and the only pan-LATAM education-specific AI body this file has identified.

🟡 **Evidence grade: search-snippet with the source named, not primary text.** Every non-GitHub host is refused at this session's egress proxy (`403` on `unesco.org`, `eur-lex.europa.eu` and `oecd.org`, all re-probed `p907`). Confirm against the primary instrument before a client deck.

#### `p908` — **both of `p907`'s declared LATAM gaps are refuted: Argentina and Central America are now placed**

`p907` closed with *"Argentina and Central America remain unrefuted (Peru is now refuted)"*. `p908`
ran the two legs **in Spanish**, which is the method `p708` established and this pass re-confirms,
and both returned real, named, dated instruments.

**Argentina — fragmented by design, and the fragments are provincial**

- 🟢 **Educ.ar (national)** ran free virtual teacher-training courses on AI and AI literacy through
  2026, in at least **two editions** (a second with enrolment to **30 October**). This is the
  national delivery channel, and it is **teacher training, not platform procurement**.
- 🟢 **Salta** is the **first province to train primary teachers in AI and computational thinking**,
  around its own **CodeAI** platform, delivered on the **AI School** platform in four 90-minute
  sessions, with the NGO **Pequeños Pasos** supplying resources.
- **Entre Ríos**: the Consejo General de Educación ran an asynchronous, semi-assisted generative-AI
  course on the **Atamá** platform.
- **CABA** published a guide for critical AI use in schools (2025), including advice that students
  not share sensitive information.
- A **national bill in the Chamber of Deputies** would promote the incorporation of AI in education;
  🟡 **its status was not established in this leg**.
- Pre-existing deployment: **Mendoza's Dirección General de Escuelas early-warning system** for
  students at risk of dropping out.
- 🔴 **Policy posture, and it is the commercially relevant fact: Argentina has no AI law and the
  current government favours a light touch** — tax incentives, limited liability for companies
  operating AI agents, and an explicit position against pre-emptive regulation. **Several bills are
  introduced and none enacted.** Compare EMEA: there is no compliance deadline here to sell against,
  so the buying trigger is capability and cost, not conformance.
- 🔵 **The supply side agrees with the policy side.** `p908` filed **six Argentine institutional
  bridges** into [`agents/top.md`](../agents/top.md) — UTN (×3: `utn-mcp`, `Skill-Moodle`,
  `aulasvirtuales-toolkit`), UdeSA, UCEMA (unlicensed, not filed) and the **SIU-Guaraní** servers
  (`siu-guarani-mcp`, `UniMCP`). **Argentina is the single best-supplied country in this base's
  institutional-bridge class, and it has the least regulation driving it.** The demand is coming from
  students and teachers, not from a compliance office.

**Central America — Costa Rica is the regional instrument-maker, and the rest is a measured gap**

- 🟢 **Costa Rica, MEP**: a **teacher guide on AI in the classroom** published 2026
  (`GuiaDocenteIA.pdf`, on `mep.go.cr`) for primary and secondary, framed inside **MICITT's National
  AI Strategy 2024–2027**. 🟢 **A ministry-published pedagogical artefact is the strongest
  government signal found anywhere in Central America.**
- **Costa Rica, higher education**: the **UCR** launched a teacher module in October 2026
  (*"¿Qué significa enseñar con IA en la UCR?"*); **SINAES** presented **TEC** work on using AI in
  **quality-assurance** processes.
- 🟢 **Regional convening exists and is datable**: the **Foro de Inteligencia Artificial en
  Educación 2026**, held in Costa Rica, drew delegations from **nine countries** — Costa Rica,
  Nicaragua, El Salvador, Guatemala, Honduras, Panamá, the Dominican Republic, Peru and Ecuador.
  **That is the room an engagement would want to be in, and it already meets.**
- **Adoption, measured**: a Microsoft report for **Q2 2026** puts generative-AI use among 15–64s at
  **29.7% in Costa Rica** (regional leader) and **24.2% in Panamá**; **Guatemala** sits between the
  global and Global-South averages; **Nicaragua lags**. 🟡 Vendor-published measurement.
- **CEPAL/CENIA ILIA 2025**: AI adoption is **accelerating fastest in Central America and the
  Caribbean**. 🟡 Secondary citation of the index.
- Private capacity-building: **INCAE** launched a management/sustainability/AI master's in April
  2026 aimed at professionals in Panamá, Guatemala and the region.
- 🟢 **First open-source row from Central America**: `franc1sc0sv/udb-copilot` (**MIT**, byte-read
  `1,066 B`), a study copilot for **Universidad Don Bosco, El Salvador** — Moodle, cited notes, the
  teacher's method, mail and a daily digest. Filed in `agents/top.md`.
- 🔴 **The gap that remains, stated precisely: no national AI-in-education policy was found for
  Panamá or Guatemala.** Both attended the regional forum; neither surfaced an instrument. 🔵 **Where
  the next pass should look: `meduca.gob.pa` (Panamá) and `mineduc.gob.gt` (Guatemala) directly** —
  the English-language and Spanish-language web legs both reached the forum coverage and stopped
  there. Guatemala's Mineduc appears in UNESCO material on open technical-training courses (NOOCS)
  with **no AI focus**, which is a near-miss worth recording so it is not re-found as a hit.

**Regional frame, unchanged but re-sourced**

- **Peru's Ley N° 31814 (published in *El Peruano*, 5 July 2023) is still the only *enacted* AI
  statute in Latin America.** Mexico has federal bills and no law; Chile's bill is pending;
  Argentina has none. 🔴 **Brazil's bill has been stuck in the lower house since the Senate approved
  it in 2024** — one source in this leg claimed a 2021 Brazilian framework; it is the weaker account
  and should not be carried.
- **Costa Rica** is among the countries that have formally adopted the **OECD AI Principles**;
  Brazil, Chile, Mexico, Uruguay and several Central American and Caribbean states have engaged
  **UNESCO's Readiness Assessment Methodology**.

#### `p909` — Peru acquires an education-specific AI instrument, and LATAM legislative attention has moved *off* AI

🟢 **Peru, `PL 00569/2026-CD`, Cámara de Diputados.** It would amend the **Ley General de
Educación** to incorporate digital literacy and AI training **transversally and progressively into
educación básica**: critical and ethical use of AI, detection of disinformation and bias, data
protection, **teacher training**, and **limits on the use of automated systems in pedagogical
decisions**.

🟡 **Published with its evidence split stated, because the halves differ in strength.** The **bill
number** rests on **one** channel — the Uniandes *Sistemas de Algoritmos Públicos* ficha, returned
by both Peru legs. The **existence of a Peruvian legislative push on AI in basic education** is
corroborated across several independent Peruvian outlets (Gestión, Andina, Caretas, lpderecho.pe),
which describe a related bill delegating curriculum development to **Minedu** from **2028** rather
than creating a standalone AI course, and another institutionalising AI training in *educación
básica regular* with a **Programa Nacional de Capacitación Docente en IA** under **Ley 31814 and
its reglamento**. 🔴 **None of that coverage could be tied to the `00569` number**, and the bill's
committee status could not be established on any channel.

🔵 **What this does to this file's Peru verdict — it refines it rather than overturning it.**
`Gap 445-B` retired Peru as a genuine **supply** absence after four nil channels, and the `p576`
instrument table carries Peru only as *"Minedu, 205 rural schools for 2026"*. Nothing here
disturbs that: **Peru is still supply-absent and is now regulation-active.** 🔵 **That is precisely
the profile that argues for a *build* engagement rather than a *compose* one** — statutory demand
forming, with no local open-source estate to assemble from, which is the inverse of Brazil (where
`i-educar` and the standard-anchored agents exist) and of Colombia (where `Ley 2626 de 2026`
mandates the curriculum nationally).

🟢 **And the region now has a denominator that reconciles.** CELE's *Observatorio Legislativo*
records digital-technology bills in LATAM congresses for **January 2025 – April 2026**: Argentina
**63**, Brazil **36**, Mexico **35**, **Peru 17**, Chile **16**, Colombia **14**, Paraguay **14**,
Ecuador **5**, Guatemala **1**. **That sums to exactly 201** — the total the first leg reported
independently — which is the only reason the figure is carried at all. 🟡 The first leg gave the
window as January 2025 – **February** 2026 for the same 201; the breakdown-bearing source's window
is carried and the conflict recorded.

🔴 **The finding inside the denominator is the one worth acting on, and it runs against this
file's assumption.** The most frequent themes in that window are **honour and reputation,
cybersecurity and content moderation** — **AI led only in January–April 2025.** LATAM legislative
attention has moved *off* AI as a standalone subject, even as education-AI bills keep appearing
inside the broader digital-technology flow. 🔵 **Commercial consequence: a LATAM pitch built on
"AI regulation is coming" is selling against a receding wave.** The durable pitch is the one
Colombia and Peru both evidence — **curricular mandate and teacher capacity**, which is `T11`, not
risk compliance, which is `T1`.

🔴 **Restated absence.** **No LATAM real-adoption data** — infrastructure, teacher or student usage
rates — was returned by the regional leg, which raised the gap as its own caveat. Peru's **17**
bills and Argentina's **63** measure legislative *activity*, not classrooms.

#### `p910` — explicitly no new LATAM evidence this pass

🔴 **No LATAM term was run on `p910`'s instrument.** The pass covered fourteen APAC and EMEA
national examinations; **`PAES` (Chile), `ICFES` (Colombia), `EXANI` (Mexico), `ENEM` (Brazil) and
`PSU`/`UBA` entrance routes were not queried on this channel.** Nothing in this section was
measured or revised by this pass, and the silence is recorded rather than left to look like
coverage.

🟡 **What stands from earlier passes, unchanged and still the operative position:** `p904` measured
**Mexico** as the largest supply-side hole in this KB (`EXANI examen` → 0 ★ ceiling, no
Mexico-origin education repository in 26 Spanish/Portuguese queries), and `bncc-dev` remains the
reference specification for a curriculum spine anywhere in the region. 🔵 `p910`'s Singapore
finding **sharpens why that matters**: the one market in this pass with a machine-readable national
syllabus published it under **CC BY-NC**, which is unusable in a paid engagement. A studio that
holds a re-authored, grant-clean BNCC spine (`P22`) holds the thing that six of this pass's eight
APAC markets lack entirely — and that is a **LATAM-built asset sellable outside LATAM**.


🟢 **Added `p911` — the four LATAM national-examination markets this KB had never queried
(`PAES`, `EXANI`, `COMIPEMS`, `ICFES`/`Saber 11`), plus the regulatory and adoption leg run in
Spanish.** 🔵 **`p904` recorded Mexico as this base's largest supply-side hole and `p910` did not
touch it. It is touched here, and the answer is specific rather than encouraging.**

🔴 **The region's adoption numbers are the highest in this file, and they are student-led.**

- **AI in Higher Education LATAM Survey 2026: `92%` of students use AI regularly and `67%` at least
  weekly.** In **Mexico**, **`66%` of university students use these tools at least weekly and `79%`
  use them to generate text**. 🔵 **Read against `T4`**: adoption has outrun governance here more
  than anywhere, and the `79%` text-generation figure is an **assessment-integrity** number before
  it is an adoption number — it is the business case for `T10`'s assessment redesign.
- **Chile** was studied at scale on the supply side of the classroom: a study of **more than 2,000
  teachers** on AI knowledge and classroom use.

🟡 **Regulation splits the two biggest markets in opposite directions, and this is the single most
useful distinction for scoping a LATAM engagement:**

- 🟢 **Chile leads**: a **National AI Policy since 2021** and **a law in discussion** (January 2026
  analysis). **Brazil and Colombia** have national strategies **but no education-sector-specific
  regulation**.
- 🔴 **Mexico has no national law, no binding guidelines, and has chosen not to make any.** The
  **SEP**'s stated approach is a set of **ten principles rather than prohibitions**. 🔵 **For a
  studio this is a *faster* market, not a looser one**: with no statutory spec to build to, the
  buyer's own governance document becomes the acceptance criterion — which is exactly the
  deliverable `P14`-shaped governance work produces. 🟡 **A Tec de Monterrey critique names the
  failure mode**: rules that *"enumerate aspirations without explaining how to apply them in schools
  with different resources"*. Quote it; it is the objection a Mexican client will already have.
- 🟢 **UNESCO signed an agreement with Chile's CENIA** to promote ethical AI in education across the
  region, **including the integration of `Latam-GPT`**, the open regional language model. 🔵 **This
  is the regional sovereignty channel (`T6`) with an education mandate attached** — and `Latam-GPT`
  is already a named asset in this KB.

🟢 **Supply, byte-read this pass — and LATAM's permissive examination tier is no longer empty.**
`p911` promoted the first **Chilean `PAES`** row (**MIT**, a configurable PAES mock-exam generator),
the first **Colombian `Saber 11`/`ICFES`** rows (**MIT** item generation and an **Apache-2.0**
assessment platform), and a **Mexican `COMIPEMS`** syllabus repository (**Apache-2.0**) — see
`agents/top.md`, `repos/foundations.md` and `verticals/solutions.md`. 🔵 **Colombia, not Brazil or
Mexico, has the deepest permissive exam tier of the four**, which inverts the order a studio would
assume from market size.

🔴 **Declared nulls and measured limits for this leg — all four are informative, none is silence:**

- 🔴 **`EXANI` and `COMIPEMS` are the weakest channels measured anywhere in this pass.** `EXANI`
  bare returns `215` nominal hits at **100% collision** (the acronym matches the `exania` product
  name), and its co-term leg returns **one** repository. **`COMIPEMS examen` returns `0`** — the
  co-term **annihilated** the channel (`911-F2`). 🔵 **So `p904`'s "Mexico is the largest supply hole"
  is now explained rather than merely restated: Mexican exam supply is not hidden, it is
  substantially absent, and the one permissive row found is a student's subject list.**
- 🔴 **No Spanish-language source was found connecting AI policy to `PAES` or `EXANI` specifically.**
  The Spanish leg returned national AI policy and university adoption, and **nothing on the
  admissions examinations themselves**. 🔵 One indirect signal was seen and **is not carried as a
  fact**: an August 2026 CIPER piece referring to AI-linked problems in UNAM admissions testing,
  which could not be opened in this environment.
- 🟡 **`PAES` surfaces non-Chilean supply.** The `PAES` leg returned a **Vietnamese** university's
  exam clients (`anhvlttfs/FPTExamClients`) and the `matric` leg returned **Ethiopian** matric
  tooling — `3` of `45` hand-adjudicated rows were real education supply attributed to the **wrong
  country** (`evidence/p911-adjudication.2026-11-19-p911.tsv`). 🔵 **Recorded as a property of the
  channel**: a national-exam acronym is not a national boundary, and the misattribution is a *source
  of discovery* (Ethiopia was never queried) as well as an error.

#### `p914` — LATAM: Colombia's instrument is **budgeted and non-binding**, which inverts the usual sequencing

This base has recorded Brazil's `PL 2.338/2023`, Peru's education-specific instrument (`p909`),
Mexico's (`p907`), El Salvador's and the regional observatory. **Colombia's national AI policy was
missing from this file entirely** (`CONPES` appeared zero times before this pass). It is the one
instrument in the region whose shape favours a vendor rather than gating one.

| | **CONPES 4144 — Política Nacional de Inteligencia Artificial** (Colombia) |
|---|---|
| Instrument type | 🟢 **A `CONPES` policy document, not a law.** Approved by the Consejo Nacional de Política Económica y Social, February 2025 |
| Money | **COP 479,273 million ≈ USD 116 million** committed to 2030, from the national general budget (`Presupuesto General de la Nación`) |
| Scope | **106 actions** to 2030, distributed across named public entities |
| Education limb | Education is a policy pillar; the *talent* line runs training and certification **from basic education through scientific specialisation** |
| Oversight | **Semiannual implementation reports until 2030** |
| 🔴 Obligations on a private supplier | **None.** The analysis in the sources is explicit: it distributes actions and budget among public entities and creates no obligations and no sanctions for private companies |

🟢 **Why this is the most sellable regulatory posture in the region.** Everywhere else in this
file, the instrument arrives as a gate: the EU AI Act classifies assessment as high-risk, Vietnam
names education high-risk, Peru's instrument is education-specific, and `P4` exists to build
conformity into the architecture. Colombia has done the opposite — it has put **budget, named
owners, a six-year horizon and a public reporting cadence** behind AI capability, including
education, **without** creating a compliance surface a supplier must clear first. For an
engagement that means the sales motion is to the *public entity holding an action and a budget
line*, not to a compliance officer, and the semiannual report is the artefact that makes a pilot
legible to the buyer's own oversight.

🔵 **How to use the reporting cadence.** The semiannual report is a deliverable the buyer already
owes someone else. A pilot scoped so that its evidence tier (`P7`) produces exactly what that
report needs — actions completed, learners reached, measured outcome — is a pilot the buyer can
defend internally without extra work. That is the same mechanism `P28` uses against the UK
specification, applied to a budget cycle instead of a standard.

🔴 **Provenance, stated because it is weaker than this file's norm.** Every non-GitHub host was
**unreachable from this session** — `unesco.org`, `eur-lex.europa.eu`, `data.consilium.europa.eu`,
`oecd.org`, `future-ed.org` and `digitaleducationcouncil.com` all failed DNS resolution under the
session's network policy (measured, not assumed: `curl` returned `000` to all six). So the figures
above come from **WebSearch result summaries only, single channel, no primary-document read**. The
`479,273` million COP figure and the `106` actions are consistent across three independent
secondary sources; the **approval date is reported as both 14 and 15 February 2025**, so it is
given here as "February 2025". The official document at `sisconpes.dnp.gov.co` is the read that
would settle the education share of the budget, which these sources do **not** break out.
**Declared gap `914-G1`: fetch `CONPES 4144` from `dnp.gov.co` from a session whose network policy
allows it, and extract the education-pillar budget line.**

#### `p915` — 🔴 **explicit nil on both sides, and what was searched**

**Stated rather than left silent, because silence here looks exactly like coverage.**

- 🔴 **Supply: nil.** Twelve discovery legs (lesson planning, rubric grading, special education,
  curriculum generation, campus MCP, spaced repetition, item generation, SIS, accessibility, teacher
  agent, proctoring, packaged education skill), each bounded by recent push date and diffed against
  the 442 addresses already written, returned **no LATAM-origin repository** not already in this base.
  🔵 Note what that is *not* evidence of: this base already carries a dense LATAM supply tier —
  `portabilis/i-educar` and `i-diario`, the BNCC corpus repositories, `academico-sis/academico`,
  `theteacherbot/ICFES-Exam-Engine`, `migueldsants/OpENEM` and the campus-MCP cohort. The nil means
  **no new supply this window**, not thin coverage.
- 🔴 **Demand: nil.** UNESCO IESALC's 87 % adoption / 26 % formal strategy / 9 % evaluation figures,
  the 55 %-no-AI-budget finding, the Digital Education Council LATAM survey (92 % of students, 79 % of
  faculty), **CONPES 4144**, the 716-instrument regulatory count, Brazil's PL 2.338/2023 and the
  UNESCO regional observatory were all returned by this pass's LATAM leg and **all seven were already
  written here.**
- 🔴 **One instrument limit worth recording against this region specifically.** `iesalc.unesco.org`
  and `unesco.org` are both unreachable from this session on **both** channels (`915-F2`), and UNESCO
  is the single most important primary source for LATAM demand-side evidence. **The LATAM figures in
  this file are therefore secondary-sourced throughout** — multi-source agreement, not primary-read.
  `915-G1` covers it.

🟡 **The opportunity is unchanged and is the one `CONPES 4144` creates:** budget to 2030 with **no
obligations or sanctions on private suppliers**, which remains the most sellable regulatory posture in
the region — a funded buyer with no compliance gate to clear.


#### 🆕 `p927` — the adoption-governance gap, now with both numbers on the same page

🟢 **New figures, and they are the sharpest version of this file's standing LATAM thesis.** A 2026
regional survey reports **92% of students use AI regularly and 67% at least weekly**, with **79% of
faculty** also using it — while **only 30% of Latin American universities have published policies
on how to use it** *(single source for each; corroborated in direction by the UNESCO IESALC work
below)*. 🔵 **Set the two side by side: 92% use, 30% governed.** This file has described the LATAM
offer as *"governance for AI already in use, not adoption"* since `p890`; this is the first pass
where both halves of that sentence have a number attached from the same year.

🟢 **The authority to cite, new to this file.** **UNESCO IESALC**, with **UNU-IAS**, published a
2026 study on AI implementation in Latin American and Caribbean **higher education** (author
Arianna Valentini), finding adoption *"neither uniform nor evenly distributed"* and mapping it
across **five dimensions — teaching and learning, research, community engagement, administration
and governance.** 🔵 **Those five dimensions are a ready-made engagement scope.** A LATAM
university that has governed none of them is not buying a tutor; it is buying a programme, and the
dimension list is the structure to propose it in.

🟢 **Two instruments that change how a LATAM engagement should open:**

- The **IDB**'s *"AI Here!"* call mapped **193 AI solutions already in use in real classrooms**
  across the region. 🔵 **That is a competitive and partnership map a studio does not have to
  build** — and it is evidence against proposing a greenfield build in a market where 193 things
  are already running.
- **EdTech Hub and Fundación Ceibal** launched a partnership in **September 2026** to help LATAM
  education systems respond to AI. Ceibal is Uruguay's national programme and the region's most
  credible public implementer; a partnership that names it is the closest thing to a public-sector
  route to market in this file.

🟡 **And the supply-side correction this pass owes LATAM.** `926-G2` measured eleven
Spanish- and Portuguese-language repositories and concluded that LATAM open education supply is
**unlicensed by default**. A second search vocabulary returned **MIT-licensed LATAM rows with the
grants byte-read** — including **`uemanet/harpia`**, the academic system of a **Brazilian state
university**, open since 2017. 🟢 **The corrected claim is better for an engagement, not worse:**
LATAM's permissive open source is **institutional** — registrarial systems, integrity tooling,
accessibility work — and not general-purpose tutors, where `p904` measured a **6 ★ ceiling**. So
the standing advice is unchanged and its evidence is stronger: **bring the tutor, adopt the
institutional spine.** See `agents/top.md` `927-F5` and `verticals/solutions.md`.


### Global

#### 🆕 `p928` — the four mandated prose legs are a **nil for the forty-seventh consecutive pass**, and this pass measured the channel that is not nil

🔴 **The four global prose legs (`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`, `open source platform education ERP CRM MIT Apache`, `AI education industry trends 2026`) returned zero repositories this base does not hold.** Named and already shelved: DeepTutor, OpenMAIC, `patchy631/ai-engineering-hub`, `withmarbleapp/os-taxonomy`, PageLM, Hermes, OpenClaw, OpenHands, CrewAI, LangGraph, AutoGen, DSPy, Langflow, Agenta, OpenEduCat, `frappe/education`, Krayin, iDURAR, Huly, Apache OFBiz, Dolibarr, Axelor. **22 named, 22 held.** Evidence: `evidence/websearch-legs.2026-11-19-p928.tsv`.

🔵 **This is no longer a surprising result and should stop being reported as one.** The useful statement is comparative, and this pass can finally make it with both numbers measured rather than one of them capped — see `intel/trends.md` `T68` and `agents/trending.md` `928-F1`. The prose channel's yield is **0**; the topic channel's, measured without the page cap for the first time, is in the thousands.


#### 🆕 `p925` — the cross-regional reading, and the one number every region's sources agree on

🟢 **Direction of travel, consistent across all four legs:** AI in education moved from pilot to
**operations** in 2026 — embedded in lesson preparation, content adaptation, formative feedback and
guided practice rather than demonstrated in a chatbot. The second consistent signal is a **shift
from general-purpose AI to purpose-built educational AI**; the **OECD 2026 Digital Education
Outlook** is cited as recommending exactly that, on the grounds of **durable learning gains**.

🔴 **Market-size estimates do not reconcile and are all secondary.** One puts AI in education at
**$11.4 B in 2026 → $57 B by 2033 (25.9% CAGR)**. The regional figures in the EMEA section above
conflict with each other. 🔵 Treat the *direction* as evidence and the *magnitudes* as marketing
until a primary report is in hand.

🟢 **Two adoption numbers worth carrying into a pitch**, both secondary but both from surveys of
practitioners rather than from vendors' forecasts: **93% of higher-education staff expect to expand
their use of AI for work purposes over the next two years**, and **AI and data made up 12% of
higher-education partnerships in 2026, up from 2.1% in 2021** — a near-sixfold shift in where
institutions are choosing to partner.

🔵 **The regulatory asymmetry is the single most useful cross-regional fact for a studio.** The same
agent is a different product in each region:

| Region | What the regulation does to an assessment or admissions agent |
|---|---|
| EMEA | 🔴 **High-risk** under the EU AI Act; AI Office enforcing since **2026-08-02**. Conformity documentation is part of the deliverable. |
| North America | 🔴 Human-oversight statutes: AI may not be the **primary basis** for a grade or discipline decision; consent is opt-in in some states, opt-out in others; dated district deadlines. |
| APAC | 🔴 **Vietnam names education high-risk** (in force 2026-03-01); South Korea comprehensive (2026-01-22); Japan/Singapore/Australia light-touch. Public opinion in ANZ moving *toward* restriction. |
| LATAM | 🟢 Sparse and fragmented — **716 instruments across 23 jurisdictions**, Brazil tightening toward the EU model, Argentina explicitly loosening. Governance, not capability, is the gap. |

🔵 **So the portable asset is not the agent. It is the evidence layer underneath it** — the consent
state, the human-in-the-loop record, the data-flow attestation and the learning-outcome evidence.
That layer satisfies the EU's conformity file, the US oversight statutes, Vietnam's high-risk
classification and LATAM's missing institutional strategy with the same implementation, and it is
the one component none of the 19 permissive agents shelved in `p925` provides.


#### 🆕 `p923` — student usage, and the one number that moves a procurement conversation
🟡 **"~54% of students use AI every week; 24% use it daily"** — new to this shelf. 🔵 It matters
because it is the **Global** counterpart to two regional figures this base already carries and
which are far higher: **87%** of EMEA students use AI at least weekly (Epson, ~3,360 respondents
across six countries, Jul–Aug 2026) and **92%** of LATAM students use it regularly with **67%**
weekly (Digital Education Council / Tec de Monterrey, 29 universities).

🔴 **Do not average these.** They are different instruments on different populations and the spread
is the finding: **student adoption is already universal in the two regions where institutional
governance is measurably weakest** (`T4`). 🟢 The procurement sentence that follows is the same in
both: the question is not whether students use it, it is whether the institution can evidence how —
which is what `P5` (LATAM governance retrofit) and `P4` (EMEA AI Act conformity) are built to sell.

#### 🆕 `p922` — the twenty-tier table, and the retraction behind it
🔴 **`921-R1` — published one pass ago as the mechanism behind every language verdict in this base
— scored 4 of 10 against tiers chosen to break it, and a successor hypothesis pre-registered this
pass scored 1 of 4.** Both are retired. What a studio should carry into a proposal is the measured
table in `repos/foundations.md`, not a story about why: 🟢 **DELIVERABLE** — ZH, JA, TH, VI, KO,
TR, AR, FI, HU, TL, CS (weak copyleft), AM, BN; 🔴 **NOT DELIVERABLE** — ID, HI, PT, KM, LO, SW, EU.
🔵 **The one generalisation that survived** is the one about size: *speaker population and market
size predict nothing here.* Bengali at 270 M and Basque at 750 k land on the opposite sides of the
line from the ones their size implies.
🔴 **`922-R2` — the licence trap has a new address: the national catalogue.** Four of five
byte-read carry **no licence file at all** (`indicnlp_catalog` 641 ★, `awesome-bangla` 580 ★,
`awesome-hungarian-nlp` 287 ★, `awesome-khmer-language` 207 ★); the one that does is the smallest.
In three of those tiers the ungranted catalogue is the **largest member**, and curation is exactly
what a localisation engagement copies first.

#### 🆕 `p918` — the market numbers still disagree, and the disagreement is the finding

Three independent 2026 estimates for AI in education, collected this pass and **all secondary**:
**$10.4B (2026) → $32.27B (2030)**; **$11.4B (2026) → $57B (2033)**; **$12.3B by 2026** (HolonIQ).
🔴 **The 2030 and 2033 endpoints imply materially different CAGRs from a nearly identical base**, so
this KB publishes the range and not a point estimate — consistent with *Market size — and why the
numbers disagree* above.

🔵 **The two directional claims every source agrees on**, which matter more than the sizing:

1. **AI is moving from pilots into core operations** — admissions, advising, student services,
   assessment and accessibility — rather than staying a classroom experiment.
2. **The OECD's 2026 Digital Education Outlook recommends moving beyond general-purpose tools toward
   purpose-built educational AI** designed for durable learning gains. 🟢 A vendor-neutral
   institution recommending exactly the vertical build this KB is organised around.

🔴 **Governance lags everywhere, on every source**: roughly a quarter of faculty report a formal
institutional AI policy. With the UNESCO LATAM 87%/26% measurement, the *adoption-outruns-governance*
pattern is now corroborated on three continents and is the most reliable commercial signal here.

🔴 **Unchanged and still true: there is no credible primary evidence of learning-outcome gains from
AI at scale.** `compose/patterns.md` **P7** exists to measure it rather than claim it.

Cross-regional plays that do not depend on one jurisdiction.

- **Licence-clean AI-on-LMS.** Open edX, Canvas and Moodle are AGPL/GPL. A client wanting a
  proprietary derivative needs the permissive path: **Artemis (MIT)**, **Kolibri (MIT)**,
  **Oppia (Apache-2.0)**, **OpenOLAT (Apache-2.0 — byte-read `p905`, with a scanner flag: see
  the Global additions below)**. Licence triage is a billable first
  engagement in its own right, and it is the question most often got wrong.
- **LTI 1.3 as a multiplier.** Build the AI tool once against `ltijs` (Apache-2.0) or `tsugi`
  (Apache-2.0) and it ships into every compliant LMS. One build, many clients.
- **Evidence of efficacy.** Every regulator and procurement office is converging on
  "show me it helped". An LRS (`lrsql`, Apache-2.0) plus `pedagogy-benchmark` (MIT) plus
  `promptfoo` (MIT) regression gates is the measurement tier almost no vendor ships.
- **The unserved category: SIS and registrarial *agents* — and p894 sharpens where the gap
  actually is.** Tutoring, grading and content generation are crowded. The *agent* tier for
  enrolment, transcripts and financial aid has **no credible open option anywhere** — but the
  *platform* tier for timetabling and student scheduling does: **`UniTime/unitime`, Apache-2.0,
  360 ★, pushed 2026-11-17** (Apereo). So the opportunity is not "write a registrarial
  platform", it is **"build the agent tier over UniTime and the decisioning tier where nothing
  exists"** — a much smaller and much more defensible scope. Still the highest defensible-IP
  opportunity in the industry, with the caveat that admissions and financial-aid decisioning are
  EU Annex III high-risk and restricted under several US state laws, so build it oversight-first.
  See `compose/patterns.md` **P12**.
- **The efficacy argument now has a primary-source anchor, and it is stronger than this KB has
  been stating (p894).** The **OECD *Digital Education Outlook 2026*** (subtitle: *How can AI
  help human beings learn and grow?*, DOI `10.59350/1bqm0-1d126`) reports that **without
  pedagogical guidance, outsourcing tasks to generative AI improves measured performance with no
  real learning gain** — the sharpest available formulation of the "performance is not learning"
  problem, and a better sales argument than any market forecast. It also finds **purpose-built
  educational tools outperform general chatbots, more consistently**; frames GenAI's contribution
  to tutoring as turning rigidly scripted tutors into **digital pedagogical agents** that
  question, nudge and change strategy; concludes that educational GenAI can augment teaching
  **while preserving teacher agency**; and reports **37% of lower-secondary teachers used AI for
  their job in 2024** (consistent with the OECD TALIS 36% figure this file already carries).
  **Why this matters commercially:** the OECD's own position is that the product differentiator
  is pedagogical control, not model quality — which is the thesis `compose/patterns.md` **P7**
  and **P9** already sell, now attributable to the sector's most-cited policy publisher.
  **Channel caveat:** the report page and DOI resolve, the full text is blocked by this session's
  network policy, and the quoted findings are from the publisher's own summary pages and
  conference commentary. **Verify the exact wording before it goes in a client deck.**

#### p905 additions — Global

- 🟡 **UNESCO counts 68 countries now regulating AI in education, up from 14 in 2021.** Held in the
  append-only log since the pass that found it and in **no** delivery file until now; promoted by the
  `902-G1` re-score. 🔵 **The use of the number is the comparison, not the level**: a near-fivefold
  rise in five years is the argument for selling *conformity* as the product rather than treating it
  as a tax on delivery — which is the premise of **P3** (North America, 50-state configurable),
  **P4** (EU AI Act conformity-by-construction) and **P6** (APAC multi-jurisdiction). 🔴 Secondary
  source; the primary host is refused at this session's proxy, so it is attributed, not verified.
- 🟢 **The permissive-path recommendation above now rests on a byte-read for OpenOLAT.** Its
  `master/LICENSE` is **10,982 B** (`sha256₁₂ 6dbc5b605ed0`) — all nine Apache-2.0 sections present
  and verbatim, so **Apache-2.0 holds** — but the terms-end marker and APPENDIX are replaced by two
  provenance paragraphs, which is why GitHub reports `NOASSERTION` and why a client scanner will flag
  it. 🔴 **Raise it before the legal review**, and note the same applies to `DeepTutor`'s hand-edited
  Apache-2.0 (`560-D`). Full read in `verticals/solutions.md`.
- 🔴 **A proposal claim this base can now support with measurement: no open education platform
  discloses the grants of its dependencies.** 14 platforms, 350 byte-reads, `0` third-party grant
  disclosures, against 316 resolved packages in Moodle and 355 in Gibbon. 🔵 This converts a
  compliance anxiety into a **scoped, billable first-week deliverable** — the dependency-grant scan —
  and `scancode-toolkit` (Apache-2.0) is the instrument. See `repos/foundations.md`.


#### `p907` note

*(`p907` added regional facts to `### North America`, `### EMEA`, `### APAC` and `### LATAM` above.
No Global-scope fact was added this pass: of 31 facts scored from the eight mandated search legs,
the 10 absent from the delivery surface were all regional. See `agents/trending.md` `907-F8`.)*

#### `p908` — what the eight prescribed legs are *for*, measured against what actually produced rows

🔵 **This pass ran all eight mandated legs and then measured which channel produced the filed rows,
because the answer keeps being the same one and it should be written down rather than rediscovered.**

| Channel | What it produced in `p908` |
|---|---|
| 4 global web legs (`agents`, `trending`, `verticals`, `trends`) | 🟡 **Context and one usable platform lead.** The `agents` leg returned general-purpose frameworks and aggregator listicles with conflicting star counts; its own summary said *"the search turned up few education-specific projects"*. The `verticals` leg returned **one** vendor (OpenEduCat, LGPL) and **eduTrac SIS** (GPL-3.0) and explicitly found **no MIT/Apache SIS** |
| 4 regional web legs (English) | 🟢 **The regulation and adoption facts above.** This is what the English legs are good at: instruments, dates, percentages |
| 2 extra legs **in Spanish** (Argentina, Central America) | 🟢 **Both of `p907`'s declared regional gaps refuted**, with ministry artefacts and a nine-country forum |
| GitHub **code search** in Spanish | 🟢 **13 of the 13 newly-filed repository rows.** `"aula virtual" mcp` (`total_count 389`) alone yielded the Ecuador, Mexico, El Salvador, Peru and Spain bridges |

🟢 **Transferable rule, now held on two independent passes (`p708`, `p908`): a region leg run in
English finds the *regulator*; a region leg run in the region's language finds the *supply*.** The
prescribed leg text contains the token `LATAM`, which is analyst vocabulary — the people publishing
the code write `aula virtual`, `campus virtual` and `autogestión`.

🟡 **Market-size note, recorded for the conflict rather than the number.** This pass's trends leg
surfaced **$11.4B** and **$12.3B** for AI in education in 2026 from two different secondary sources.
Both are vendor-blog citations of unnamed primary reports. **See
[`## Market size — and why the numbers disagree`](#market-size--and-why-the-numbers-disagree); `p908`
adds two more disagreeing figures and no new primary source.**

## Declared gaps

### Declared in `p917`

- 🔴 **`917-G1` — seventh consecutive pass with no primary legal text.** `eur-lex.europa.eu`,
  `oecd.org` and `unesco.org` do not resolve from this environment; `915-F2` established the failure
  is **DNS, not HTTP**, so another HTTP client is wasted effort. Every EU AI Act date in this file
  is from secondary analysis and is marked as such. Remedy: one pass from a session whose network
  policy resolves those three hosts.
- 🔴 **`917-G3` — APAC placed zero rows against a demand picture that is large and well-sourced.**
  See the APAC subsection. Remedy: a pass that queries APAC supply in **non-English shapes** — the
  LATAM legs this pass showed a vernacular query can move a count by two orders of magnitude, and
  that experiment has never been run for Mandarin, Japanese, Korean, Bahasa or Hindi.
- 🟡 **`917-G4` — market size is unquotable and this file should stop implying otherwise.** The
  `p917` legs returned, for the same year: **$10.6B → $42.48B by 2030 at 41.5% CAGR**, and
  **$47.78B (2025) → $1,169.44B by 2035**. These differ by a factor of ~25 on the out-year. Remedy:
  quote adoption rates, which are survey-measured and broadly agree, and quote market size only with
  the source named inline.

### Declared in `p915`

- 🔴 **`915-G1`** — re-declares `914-G3` **with its mechanism now known.** The demand side needs one
  pass from a session whose network policy *resolves* `eur-lex.europa.eu`, `oecd.org`,
  `unesco.org` and `iesalc.unesco.org`. Both the session container (`curl` → `000`) and the
  server-side fetcher (→ `getaddrinfo ENOTFOUND`) fail, the latter at **DNS**, so the hosts are
  outside an allowlist rather than refused at the HTTP layer. 🔵 **Do not spend a leg on another HTTP
  client, library or user-agent — none will work.** This is the fifth consecutive pass in which no
  primary legal text could be byte-read, and it is the highest-value outstanding gap in the base.
- **`915-G2`** — read **Article 1 of Regulation (EU) 2026/1744** and establish whether the
  2 December 2027 Annex III date is **conditional and advanceable by the Commission**. `T3` is
  annotated with this as an unverified single-source risk; it decides whether `T3`'s "selling window"
  framing is sound.
- **`915-G3`** — bound the instrument limit `915-F7` found: **how often does `search/repositories`
  report an SPDX licence for a repository with no readable payload?** Until it is measured, a
  search-reported licence counts as **one** channel, not two.
- **`915-G4`** — `T43`'s by-reference grant class was measured in the **GNU** family only. Probe
  whether Apache-2.0 and MPL payloads are also distributed by reference at small byte sizes, because
  band-shaped rules exist or are implied for those.

- 🟢 **`p914` ADVANCES `910-G4` by three byte-reads, and the `NOASSERTION` tier is now 3 of 5
  NonCommercial across this base.** `910-G4` asked what `NOASSERTION` rows actually *say*, having
  resolved two of two to CC BY-NC. `p914` byte-read three more: `Jeremy-xuan/SocraticNovel`
  **CC BY-NC-SA 4.0** (NonCommercial — barred), `aaryansamanta/NextGen-AI` **MIT on code with brand
  assets reserved ©** (usable), and `Andiii208/seu-handbook-skill` **MIT on code with the handbook
  corpus in `references/`/`data/` under CC BY-NC-SA 4.0** (🔴 the corpus *is* the product, so the
  skill is effectively NC). **Cumulative: 5 `NOASSERTION` byte-reads, 3 NonCommercial, 2 split with
  a usable code grant, 0 plain single-licence repos.** 🔵 The predictive content of the field is now
  worth stating: `NOASSERTION` has never once meant "merely unlabelled" in this base — it has meant
  a split grant or a non-software licence **5 times out of 5**. Promoted to `intel/trends.md`
  `T40`, which also records that `NONE` behaves differently (5/5 genuinely empty) and should
  therefore be read **second**. 🔴 **`910-G4`'s core question is still open**: the **29
  `NOASSERTION` rows in the curated shelf** (`p909`'s census) remain unaudited, and at a 3-in-5
  observed NC rate the expected number of NonCommercial rows sitting in the shelf is **not zero**.
  That audit is still the highest-value one outstanding.
- 🔴 **New gap `914-G3` — the demand side of this KB needs one pass run from a session whose network
  policy permits the primary hosts, and until then four consecutive nil legs are uninterpretable.**
  Measured this pass, not assumed: `curl` returned `000` to **`unesco.org`, `eur-lex.europa.eu`,
  `data.consilium.europa.eu`, `oecd.org`, `future-ed.org` and `digitaleducationcouncil.com`** —
  every non-GitHub host probed. GitHub hosts were fully reachable, which is why the supply side of
  `p914` is dense and the demand side is thin. **No primary document has been read by this base in
  this session, and the most load-bearing date in `P4` and `P28` — the 2 December 2027 Annex III
  deferral under `Regulation (EU) 2026/1744` — rests entirely on secondary sources.** North America
  and EMEA have now returned nil on `p905`, `p906`, `p910` and `p914`; that is consistent with
  genuine saturation **and** with a channel that compresses away exactly the state-level, dated,
  incremental detail those two regions signal through. Re-run both legs from a permitted session
  before anyone records them as saturated.
- 🔴 **New gap `914-G1` — Colombia's `CONPES 4144` education budget line is unread.** The policy's
  headline is firm across three secondary sources (**COP 479,273 M ≈ USD 116 M to 2030, 106 actions,
  semiannual reporting**) and the sources **do not break out education's share**, while disagreeing
  on the approval date (14 vs 15 February 2025). The official document at `sisconpes.dnp.gov.co`
  settles both. This is the one LATAM instrument in this file with budget and no compliance gate, so
  the size of its education line is directly a deal size.
- 🔴 **New gap `914-G2` — Australia's `National AI Plan` Action 5 has no quantum in this file.** The
  plan (2 December 2025) declines a standalone AI Act, names education a national priority and
  includes piloting generative AI in schools; Action 5 *"Support and train Australians"* is led in
  part by education departments. **Its funded amount is unread**, as is the 2023 Australian
  Framework for Generative AI in Schools, which secondary sources describe as carrying no funding,
  no implementation support and no enforcement. Read both directly.
- 🔴 **New gap `914-G4` — `T41`'s mechanism is a hypothesis and must not be promoted on one tier.**
  `p914` measured H5P's runtime half as GPL-3.0 (readable, byte-identical across the PHP and Node
  implementations) and **both** its authoring surfaces as carrying no licence payload at all, while
  pushed within eight days of measurement. The proposed mechanism — a runtime ships to everyone and
  acquires a grant early, an editor is used by the project's own team first and acquires one late —
  is **already not universal**: `learningequality/studio`, `openfun/richie`, `oppia/oppia` and
  `Khan/perseus` were byte-read this pass as controls and all four are permissive. Probe another
  industry's content-authoring tier before generalising.
- 🟢 **`p910` PARTIALLY DISCHARGED `906-G2`, the English-metadata channel this file has carried as
  "the highest-value remaining instrument" since `p906` — and the instrument needed fixing before
  it worked.** Fourteen national-examination terms with no prior occurrence anywhere in this tree
  were queried: **11,508 nominal hits bare, and 63% of the sampled rows are homonyms** (`SNBT` is
  Minecraft's serialisation format, `KSSM` is a Kotlin state-machine library, `TOPIK` is topic
  modelling, `PSLE` is `psleep`). Adding one co-term takes the collision rate to **4%** and the
  nominal count to 832. 🔴 **But the co-term has a measured recall cost** (`910-G1`): the best
  institutional row of the pass — `nsip/nias2`, Apache-2.0, Australia's NAPLAN validation
  infrastructure — appears **only on the bare term**, because infrastructure describes itself as
  *validation*, not *assessment*. **The channel must be run both ways, and the bare run must be
  read rather than filtered.**
- 🔴 **`906-G2` is NOT fully discharged, and the part left undone is the part it was raised for.**
  It named India as the claim this instrument would price. **`CBSE` and `NCERT` were not run on the
  co-term instrument** (they appear in this tree from earlier passes through other channels), and
  neither were **Nigeria** (`WAEC`, `JAMB`), **Kenya** (`KCSE`), **South Africa** (`CAPS`,
  `matric`), **Chile** (`PAES`), **Mexico** (`EXANI`, still the largest hole — `p904`), **Brazil**
  (`ENEM`), **Germany** (`Abitur`) or any **US/Canada** term (`SAT`, `AP`, `STAAR`, `Regents`,
  `EQAO`). **India remains unpriced. North America and LATAM have no supply evidence from this
  instrument at all**, and the regional sections above say so explicitly rather than staying silent.
- 🔴 **New gap `910-G4` — `NOASSERTION` resolved to NonCommercial twice out of two byte-reads in
  this tier, and this file has no idea how common that is.** Both reads were CC BY-NC 4.0 — the
  3,149 ★ `5mdld/anki-jlpt-decks` and Singapore's machine-readable MOE maths syllabus. 🔵 This tree
  has catalogued `NOASSERTION` as *"requires a byte-read"* since `p906`; it has never recorded what
  the bytes **say**. **Unaudited: the 29 `NOASSERTION` rows in the curated shelf** (`p909`'s
  census) — how many of those are NonCommercial rather than merely unlabelled? **NC bars the
  engagement, not just the distribution**, so if even one shelf row is NC it is a worse defect than
  any licence finding in this file to date. This is the highest-value audit outstanding.
- 🔴 **New gap `910-G3` — the 255-repository posture figures are a sample, not a census.** The sweep
  took the **top 25 by stars per term**, and **46% of the cohort has zero stars**, so the sort is
  close to arbitrary over most of the tier. The nominal counts (11,508 / 832) are exact; the
  63.9%-ungranted figure is a sample statistic and must not be quoted as a census.
- 🟢 **`p906` closed the language-channel gap this file has carried since `p903` — all eight
  declared-untried channels were run, and the answer is a shape, not a list.** `p903` left "Urdu and
  Indonesian untried"; `p904` widened it to "Hindi, Vietnamese, Thai, Japanese, Korean and Mandarin"
  and called Mandarin the highest-value remaining channel. **All eight ran in `p906`. Mandarin was
  the highest-value channel and the other seven are empty** — ceilings of 0–2 ★, and in Hindi,
  Korean, Japanese, Thai and Vietnamese **not one hit carries a licence file**. Mandarin returned
  **347 repositories** in grading alone and twelve verified, shelved rows. 🔵 **The discovery channel
  that paid for four passes is now exhausted at the language level**, and the honest statement of
  what replaced it is below. Record:
  [`nonenglish-ceiling.2026-11-18-p906.tsv`](../evidence/nonenglish-ceiling.2026-11-18-p906.tsv).
- 🔴 **New gap `906-G2` — the English-metadata blind spot, which `p906` created by closing the one
  above.** `search/repositories` matches name, description and README, so a repository with English
  metadata and vernacular content is invisible to a vernacular query. **This base can prove the
  blind spot is real: `itsme-ganzu/belajar-ngoding-byGanzu` (MIT, 66 ★) is a shelved Indonesian row
  that `p906`'s own Indonesian queries did not return.** Every ceiling in the table above is
  therefore a ceiling on *vernacular-metadata* supply, not on existence. **Untried and now the
  highest-value remaining channel: English-metadata queries carrying a country or curriculum term**
  (`CBSE`, `NCERT`, `KSSM`, `TOPIK`, `JLPT`, `gaokao`, `UTBK`), which reach projects that describe
  themselves in English for a single national market. This is the instrument that would price the
  India claim properly.
- 🔴 **New gate `906-G1` — the SPDX field can be wrong in the *restrictive* direction, and this base
  had only ever recorded the permissive direction.** `yinuoguan/nengdou-ai-review-helper-web`
  (193 ★) is labelled `MulanPSL-2.0` by GitHub and its `LICENSE` is **verbatim Apache-2.0**
  (11,356 B, `sha256₁₂ 43070e2d4e53`, byte-identical to `PGshen/thinking-map`'s, which is labelled
  correctly). Prior cases in `intel/measured-unusable.md` were all fields *silent about a
  prohibition*; this is a field **inventing** one. **A scanner reading the field rejects software the
  byte-read clears.** The gate: for any repository a studio intends to adopt, the SPDX field decides
  nothing in either direction — only the bytes do.
- 🔴 **`906-G3` — not a new gap: `884-G2` RECURRED, and it recurred inside `p906`'s own
  instrument.** `884-G2` ("the grant ladder probes two branch names") was discharged in `p885` with
  a fix and 13 controls, after measuring that **26.5% of permissive repositories with a
  non-standard default branch had been published as having no licence**. The fix is to resolve the
  default branch from `search/repositories` before reading bytes. 🔴 **`p906`'s licence probe did
  not do that** — it iterated the two hardcoded names `{main, master}`, which is the pre-fix
  instrument. **Four of the twelve cohort repositories default to `master`, so the regression was
  invisible: it happened to cover them.** 🟢 **The two barred repositories were re-probed on their
  real default branches before publication** (`MathCyclus` → `main`, `EduMultimark` → `master`,
  six paths each including lowercase `license`, all `404`), **so both absence claims hold.** The
  lesson is that a discharged gate does not stay discharged unless the next pass inherits the
  instrument: `884-G2`'s fix lived in `p885`'s script, not in a shared one. **Registered: the
  licence probe needs to be a single checked-in tool, not rewritten per pass.** Still not audited —
  **how many rows already in this tree were licence-read on two hardcoded branch names**, and
  whether any were barred on that basis.

- 🟡 **`p904` ran all eight mandated legs. Third consecutive pass in which generic English search
  produced no repository this tree did not already hold** — the three candidates it named
  (`SirhanMacx/Claw-ED`, `geekjourneyx/interactive-learning`, `TapXWorld/ChinaTextbook`) are all in
  the live tree, two with rows in delivery files. 🔵 **The null is now a property of the base, not
  of the queries, and it is recorded rather than left silent.** Where the legs *did* pay was prose:
  **6 of 21 regional facts** were absent from every delivery file and are promoted in this pass
  (DEC LATAM survey base, IADB 193 solutions, OpenAI Education for Countries, ISO/IEC 42001, APAC
  virtual-tutor 30%, Acer Edu Summit APAC). `p903` named **Urdu and Indonesian** as the untried
  language channels; `p904` ran **Spanish and Portuguese** instead, because the LATAM supply claim
  was the oldest unfalsified one in the tree — and it did not survive. **Urdu and Indonesian remain
  untried**, and so now do **Hindi, Vietnamese, Thai, Japanese, Korean and Mandarin**, the last of
  which is the highest-value remaining channel given that two of this KB's three largest agents are
  Chinese-university projects.
- 🔴 **`DigComp 3.0` is still a named gap, second consecutive pass.** The EU's AI-literacy
  framework for primary and secondary education, cited in Council conclusions **ST-14902-2026**
  which this file already cites for a different point. `ec.europa.eu` and
  `digital-skills-jobs.europa.eu` are both **refused at the egress proxy** (`connect_rejected`,
  re-tested at the top of `p904`), so it cannot be read. **Recorded as a gap, not as a fact.**
- 🟡 **Mexico is the largest supply-side hole in this KB and `p904` measured it as such rather than
  inferring it.** `EXANI examen` returned a **0 ★ ceiling** and no Mexico-origin education
  repository appeared in any of 26 Spanish/Portuguese queries. For a Mexican engagement, assume
  nothing local to adopt and budget the curriculum spine as build, using `bncc-dev` as the
  reference specification.

- 🟡 **`p903` ran all eight mandated legs and they produced *nothing this file did not already
  hold* — recorded here because an unrecorded null result is indistinguishable from not having
  looked.** The four global legs returned fifteen repositories, **every one already in the tree**
  (checked against all 5,790 repository references in it). The four regional legs were *less*
  precise than this file: the snippets gave "Vietnam's AI law, education in the high-risk list"
  where this file holds **Law 134/2025/QH15 plus Decision 33/2026/QD-TTg and Decree
  142/2026/ND-CP** with a 72-hour incident clock; "TEQSA required providers to submit action plans"
  where this file holds **all 203 registered providers**; and the EU delay "not yet formally
  adopted" where this file holds **Regulation (EU) 2026/1744** with its three-way date conflict
  intact. 🔵 **The operative conclusion is about method, and `p902` half-anticipated it:** generic
  search is now a **confirmation** channel for this base, not a discovery one. The channels that
  still discover are the ones that read bytes — licence paths, curated-index audits (`902-F2`) and
  **non-English repository search**, which is what `p903` spent its budget on and what produced
  everything new in this pass. The two obvious untried language channels are **Urdu and
  Indonesian**.

- 🔴 **Eleven facts in this file were published in `p902` after sitting unpromoted in
  `agents/trending.md`.** `p901` scored the mandated research legs as a *null yield* by grepping each
  fact against the whole tree — which includes an 87,000-line append-only log — and concluded the
  search channel was saturated. Re-scored against this file and the three other reference files,
  **11 of 19 facts were missing**
  ([record](../evidence/surface-yield.2026-11-18-p902.tsv)). The correct claim is narrower: **the
  legs stopped producing facts this base had never seen; they did not stop producing facts this base
  had never published.** Nothing yet measures how long a fact waits in the log before it reaches this
  file — that is `902-G4`.

- **No 2026 market-share data for AI education providers** was found in any region. Market
  *size* estimates exist; vendor *share* does not.
- ~~**No AI-in-education policy for Japan**~~ — **closed in pass p890 with a negative answer.**
  Japan's AI law is promotion-focused and backed by voluntary guidelines; a second targeted pass
  found **no education-specific statute or classroom regime**. Absence confirmed, not unknown.
- ~~**No Africa or Middle East specific leg**~~ — **closed in p891.** Both were run as
  dedicated legs; see the Africa and Middle East subsections under EMEA. They remain filed under
  `region: EMEA` because this KB's region vocabulary is closed to five values — the country is in
  the prose, as the schema requires. Coverage is now thin-but-real rather than absent.
- ~~**Star counts and repo-popularity metrics are absent**~~ — **closed.** Batched `repo:`
  qualifiers against `gh api search/repositories` work; 116 of 119 tracked repos resolve. See
  `agents/top.md` for the three that do not. This line was stale and is corrected here.
- 🔴 **Primary legal and statistical texts are UNREACHABLE — reclassified p899 from "not done"
  to "structurally impossible from this session", measured on two independent channels.**
  `884-G4` has been carried for seven passes in language that reads like an unfinished job. It is
  not one. Measured 2026-11-18 ([record](../evidence/host-reachability.2026-11-18-p899.tsv)):

  | Host | `curl` | `WebFetch` | Class |
  |---|---|---|---|
  | `raw.githubusercontent.com` | 301 | — | 🟢 reachable |
  | `api.github.com` | 200 | — | 🟢 reachable |
  | `eur-lex.europa.eu` | **000** | **ENOTFOUND** | 🔴 unreachable |
  | `arxiv.org` | **000** | **ENOTFOUND** | 🔴 unreachable |
  | `unesco.org` | **000** | — | 🔴 unreachable |
  | `digital-strategy.ec.europa.eu` | **000** | — | 🔴 unreachable |

  **Both channels fail at DNS for every non-GitHub host**, so this is the session's allowed-domain
  policy, not a blocked fetch, a rate limit or a missing effort. 🔵 **The consequence must be
  stated plainly rather than carried as a to-do: every legal date in this KB — the December 2027
  Annex III deferral, the 2 August 2026 Article 50 date, Regulation (EU) 2026/1744 itself, the
  Korean AI Basic Act commencement — is *search-mediated secondary reporting*, and secondary
  sources demonstrably disagree with each other on several of them.** They are good enough to
  scope an engagement and **not** good enough to put in a compliance deliverable without counsel
  reading the primary text. **Revised acceptance test:** close `884-G4` only when either (a) the
  allowed-domain list gains `eur-lex.europa.eu` and `unesco.org`, or (b) a client-side legal
  review is recorded against the claims. Re-running searches will never close it.
- **No vendor-share, pricing or win/loss data in any region.** Market size exists; competitive
  position does not. The Jisc statement is the closest proxy — it tells you what buyers are
  unhappy about, which is more actionable than share figures anyway.
- ~~**Africa and the Middle East remain unexamined**~~ — **closed in p891** after four passes.
  Africa yielded the South African draft-policy retraction (10 April 2026, abrogated 27 April
  2026 over fictitious references), Nigeria's National EdTech Strategy 2025–2030, Kenya's
  M-Shule, the AU Continental AI Strategy and the November 2026 AI Research Foundations launch
  across 30 universities. The Middle East yielded the UAE's 25-prohibition classroom guide and
  KHDA's platform-neutral 2027-28 regime.
- ~~**Canada is a one-pilot leg**~~ — **closed in p891.** Canada now has its own subsection:
  no national rule, formal educator guidance in only four provinces (BC, New Brunswick,
  Newfoundland and Labrador, Quebec), nothing from Ontario's ministry, and a higher-education
  sector that has broadly refused AI detection on privacy grounds.
- ~~**Saudi Arabia is unsearched, not absent**~~ — **closed in p892.** Run as its own leg, as
  p891 directed. The judgement that a true absence was implausible was correct: KSA has AI units
  in public education from 2025–26, **50 further AI units across 22 revised subjects for
  2026–27**, MoE/SDAIA ethics guidance, **240,000 teachers in training**, and an SDAIA–Humain
  trial on teacher administrative workload. See the Saudi Arabia subsection under EMEA. **The
  gap was in the search, not in the world** — which is the argument for running named gaps as
  dedicated legs rather than hoping a regional query surfaces them.
- ~~**India has never been covered**~~ — **closed in p892.** India now has its own subsection
  under APAC. The headline: **NCERT/CBSE Computational Thinking and AI curriculum for Classes
  III–VIII from 2026–27**, a CBSE circular of 1 April 2026, a 15-hour SOAR module already in
  18,000+ schools, and **no education-specific AI statute** — the compliance surface is IT-Rules
  content labelling (20 February 2026), not system conformity. **India is a delivery-capacity
  market, not a conformity market.** Contested: whether Classes 9–10 become compulsory in
  2027–28.
- ~~**No open-source education agent originates from India, Africa or the Middle East**~~ —
  **corrected in p893, and the correction is a sharpening rather than a reversal.** A dedicated
  repository-discovery leg across Swahili, African, Indian/NCERT, Arabic, Nigerian and
  Hindi education-AI search terms found that **such repositories do exist in all three
  regions** — the earlier statement was too strong. What they do not have is traction or, in
  most cases, a licence. Verified examples: `acheamponge/wassce-benchmark` (MIT, **4 ★**),
  `7irelo/aptiverse` (South Africa, CAPS-aligned, **no licence**, 4 ★),
  `thesavvybyjude/Offline-First-Android-AI-Tutoring-App` (MIT, 1 ★, on-device RAG over the
  WAEC/NERDC curriculum), `kadioko/ElimuAI` (Tanzania/Swahili, no licence, 1 ★),
  `codingbilla/ShikshaSetu-Ai` (MIT, 0 ★, Gemma Hindi/Hinglish for rural learners),
  `devilking7x/guruji` (MIT, 0 ★, Hindi-first Classes 6–10),
  `Dhananjay-234/shikshaedge-app` (no licence, 0 ★, Gemma-3 fine-tuned on NCERT, offline).
  **The accurate finding: the ceiling across all three regions is 4 ★, and roughly half carry
  no licence at all.** The commercial conclusion is unchanged and now better evidenced —
  these are consumer markets for agents built elsewhere, and a localisation market — but the
  reason is *absence of traction and licence hygiene*, not absence of builders. **Note the
  shared architecture:** nearly every one is offline-first, small-model and RAG-over-national-
  curriculum. That is a reusable reference design, and it is the design the regions converged
  on independently.
- **Correction to the standing LATAM-origin finding.** `warleysr/ankipa` (10 ★) is no longer
  the only verified LATAM-origin education agent, nor the largest. **`CaioCastro1/usp-mcp`
  (MIT, 28 ★, pushed 2026-11-13)** — a Portuguese-language MCP server over Universidade de São
  Paulo's e-Disciplinas (Moodle) coursework, catalogue and campus services — is roughly 3×
  its size. Both are small; the point is that the "one agent" formulation was a search artefact,
  and it has now been wrong twice in the same direction.
- **The Gemma-for-African-education datasets have no name, licence or date — re-checked in
  p893 and still true.** The Google / Fab AI / Google.org / Gates Foundation programme for
  Kenya, Ghana and South Africa remains a commitment with nothing published. **Do not promise
  a client this asset.** What changed is the context, not the gap: p893 found five adjacent
  African-language and African-curriculum artefacts that *have* shipped under open terms
  (NILEAGI-SUB, AfriMMT-EA/Safari, AfriqueLLM, WAXAL, `wassce-benchmark`). See the Africa
  p893 re-check subsection. Re-check the Google programme again next pass.
- **Saudi Arabia's primary sources were not reachable.** The Ministry of Education and National
  Curriculum Center publications are blocked by this session's network policy; the 50-unit and
  240,000-teacher figures are from SPA, Saudi Gazette and regional trade press. Corroborated
  across outlets, not primary-verified.
- **Africa and Middle East findings are low-to-moderate confidence.** Primary government
  sources (WAM, UAE Ministry of Education, KHDA, South African DCDT) are blocked in this
  session; the South African retraction is well-corroborated, the UAE curriculum start date is
  contested across sources, and 2026 African edtech adoption figures were omitted as
  unverifiable rather than reported with a caveat.

- **No Southeast Asian primary source was reachable (p893).** The Philippine DepEd order number
  (**003, s. 2026**), the AGAP.AI participant breakdown and the ASEAN Foundation *Digital
  Outlook* figures all come from regional press and secondary coverage; `deped.gov.ph`,
  `aseanfoundation.org` and the Philippine government portals are blocked by this session's
  network policy. **Confirm DepEd Order 003 s. 2026 before citing it in a client document.**
- **The AILit Framework was not byte-read (p893).** Its existence, 19 June 2026 launch date,
  four-domain structure, EC/OECD joint authorship and PISA 2029 linkage are corroborated across
  the Commission's own EACEA newsroom item and secondary analysis, but `ailiteracyframework.org`
  and the Commission PDF could not be opened here. The **18 vs 19 June** launch date is
  contested across sources. Before an AILit-mapped engagement is scoped, the framework document
  itself must be read — a competence mapping built from summaries will not survive review.
- **No vendor-share, pricing or win/loss data — still absent after six passes (p893).** Six
  consecutive passes have searched for it in every region and found market *size* only. This
  should now be treated as a structural property of the sector rather than a research failure:
  the buyers are public institutions, the procurements are not aggregated anywhere, and no
  analyst publishes share. **Stop re-searching it every pass.** The Jisc specification and the
  Delaware assurance-lab criteria are better proxies for competitive position and are
  actionable; vendor share is not coming.
- **No learning-outcome evidence base, and p893 found the measurement of that absence (new).**
  One 2026 edtech review reports that **only ~45% of the most-used education tools have
  published research meeting an ESSA evidence tier**, and the OECD's 2026 *Digital Education
  Outlook* is reported as warning that AI helps learning only when pedagogy stays in control.
  Both are secondary-sourced and the ESSA figure's methodology was not obtainable. If it
  survives verification it is the strongest single argument for the efficacy tier in
  `compose/patterns.md` **P7** — **verify it before using it in a pitch.**
- **LearnHarness has 10,002 ★ and no published efficacy study (new, p893).** The
  fastest-growing education repo this KB has ever measured has a documented design, an active
  plugin ecosystem, and **no learning-outcome evidence whatsoever** — and user reports describe
  being tested before being taught. This is the industry's evidence problem reproduced at speed
  in open source, and it is worth watching as a test case: if a 10k-star project cannot produce
  outcome data, the "measure it" argument gets harder to sell, not easier.
- **The ESSA "~45%" figure failed verification a second time (p894).** A dedicated leg paired
  the OECD *Digital Education Outlook 2026* with ESSA evidence-tier terms. **The OECD half
  resolved and is now written up in the Global subsection above with its DOI; the ESSA half
  returned nothing** — no source on ESSA Tier 1–4 coverage of widely used education tools, and
  no route to the original review's methodology. **Two independent failures is enough to stop
  treating this as a research gap and start treating it as an unusable number: do not cite the
  ~45% figure.** The OECD finding carries the same argument and is attributable.
- **LATAM produced no new fact this pass, and that is stated rather than left as silence
  (p894).** The regional leg re-surfaced only figures this file already carries — IDB's review of
  **193** AI initiatives (**59%** generative AI), UNESCO IESALC's **87% / 26% / 9%**,
  Cetic.br's Brazilian **53% use vs 22% with guidelines**, TALIS teacher use, HolonIQ's 2026
  LATAM EdTech 100 with Brazil at nearly half the cohort, the Raspberry Pi Foundation's
  **$4.6M** Google.org-funded *Experience AI* programme (**24,000** educators and **1.25M**
  students targeted by 2028, with Sincroniza Educação in Brazil and Educación para Compartir in
  Mexico), and the UNESCO Santiago observatory. **An informed nil.** The one thing the leg
  confirmed as still missing is **regulation**: no source tied Brazilian or Mexican AI law to
  schools beyond **PL 2338/2023**, which this file already carries as a draft. LATAM remains a
  governance-gap market, not a conformity market.
- **This KB's canonical files and its append-only history have diverged, and that is now the
  highest-value gap in the file (new, p894).** `UniTime/unitime` (Apache-2.0, 360 ★, pushed
  2026-11-17) was verified and licence-hash-checked by an earlier pass, recorded in
  `repos/trending.md`, and **absent from `verticals/solutions.md` and `repos/foundations.md`**
  until this pass restored it. `agentscope-ai/OpenJudge` (Apache-2.0, 1,113 ★) was in the same
  state. Worse, p892 then **re-derived an absence** — "the SIS category is small, static, and
  copyleft or licence-unclear end to end" — from a table that had already lost its
  counter-example, and p894 had to retire that claim. **The remedy is cheap and it is a process,
  not a search: diff each canonical table against the trending history before rewriting it.**
  **The cost of not doing it is the one failure mode this KB cannot absorb** — it published a
  false negative about a market opportunity, in the file a studio opens first. Unresolved beyond
  the four rows restored here; the full diff has not been run.

#### p898 additions — Global

**Employers, not ministries, are now a top-tier funder of AI skilling — roughly $3.6 BN in named
corporate commitments.** **Microsoft $2.5 BN**, **AWS $1 BN** and **Caterpillar $100 M** are the
three largest named programmes. *(Search-snippet evidence; the three figures are reported together by
a single EdTech-sector source, so treat the $3.6 BN total as indicative and the individual figures as
requiring confirmation before they go in a client deck.)*

🔵 **Why this belongs in a market map and not a trends note.** Every regional section in this file
reads the demand side as **institutional** — ministries, regulators, universities, school systems —
with procurement cycles measured in years and budgets set by public finance. A $3.6 BN **corporate**
skilling pool is a parallel buyer with a different cycle, a different procurement path and, crucially
for a studio, **no public-tender requirement**. Caterpillar's $100 M is the instructive one: an
industrial manufacturer, not a technology vendor, funding AI skilling directly.

🔵 **What it implies for Globant specifically.** The corporate-skilling buyer wants **workforce
curriculum plus delivery**, which is the one tier where this KB's permissive supply is strongest —
`simranjeet97/AI_Engineer_Roadmap_2027` (Apache-2.0, added `p898`), the `P10` teacher-enablement
pattern retargeted at employees, and the Apache-2.0/MIT content repos generally. 🔵 **It is also the
tier least constrained by the education regulation that dominates this file**: corporate L&D is not
schooling, so the Annex III high-risk classification, the US state classroom statutes and the
age-banding rules largely do not reach it. **The compliance barrier that gates the institutional
market does not gate this one.**

🔴 **Informed gap.** No regional split is available for these commitments — the source gives global
totals only. Whether the $3.6 BN lands in North America, EMEA, APAC or LATAM is **unmeasured**, and
that is a live question for a studio deciding where to staff against it.

