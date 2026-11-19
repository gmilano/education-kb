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

### EMEA

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

### APAC

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

### LATAM

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

### Global

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

