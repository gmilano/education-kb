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
