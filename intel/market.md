---
industry: education
region: Global
updated: 2026-10-22
---

# Education market intelligence

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/intel-market.md`](../archive/2026-10-22-p383-pre-rewrite/intel-market.md).

🆕 **Pass `p386` · 2026-10-22.** All four regional legs were run again. **Three off-shelf facts are
promoted here this pass** — one of them absent from this entire repository until now (the OECD/EC
**AILit framework**, EMEA), one recorded only in [`policy-matrix.tsv`](policy-matrix.tsv) (Korea's
**AI Basic Act**, APAC), one never recorded at all (**H.R. 8747**, North America). 🔴 Channel state
unchanged: `www.oecd.org`, `www.congress.gov` and `eur-lex.europa.eu` all return DNS `ENOTFOUND`
from this sandbox, so **every policy fact added below is graded `CONVERGENT-SECONDARY, PRIMARY
UNREAD`** and says so.

All four regions were searched this pass and **all four are placed with findings** — none by a
declared nil. Where a claim could not be traced to a primary source it is marked
🔴 **UNCONFIRMED** and the reason is given, because an informed gap is information and silence
looks exactly like coverage.

## Market size — use the range, never a single figure

The spread between reputable houses is roughly **1.7×** on the current year and far wider on the
forecast, because "AI in education" is defined differently by each. Quote the range:

| source | 2026 | forecast | CAGR |
|---|---|---|---|
| Precedence Research | **$9.58B** | $136.79B by 2035 | 34.5% |
| Grand View Research | **$11.4B** (from $8.3B in 2025) | $57.2B by 2033 | 25.9% |
| Research and Markets | **$10.6B** | $42.48B by 2030 | 41.5% |
| Markwide Research | **$8.7B** | $100.21B by 2035 | 31.2% |

**Working figure: $8.7–11.4B for AI-specific education spend in 2026, growing 25–45% annually.**
North America is the largest region (Precedence). Broader edtech is an order of magnitude larger —
an aggregator cites HolonIQ at **$404B in 2026 @16.3%**, but that page carries several
unverifiable statistics, so treat the edtech total as directional only.

## The one number that should shape every pitch

| measure | value | source |
|---|---|---|
| Students/educators using AI in academic work | **95%** (n=4,200, 5 countries) | Coursera |
| Students using AI in learning | **88%** (n=45,398, 35 countries) | Digital Education Council |
| Faculty using AI in teaching | **77%** | Digital Education Council |
| Educators whose institution has a **formal AI policy** | 🔴 **26%** | Coursera |
| Aware of *any* governing policy or guideline | 🔴 **54%** | EDUCAUSE 2026 |
| Institutional AI adoption (vs 49% prior year) | **66%** (n=779) | Ellucian, 3rd annual survey |
| Institutions investing in AI | **~80%** | Inside Higher Ed / Hanover |
| CTOs saying AI met or exceeded ROI expectations | 🔴 **29%** | Inside Higher Ed / Hanover |
| Provosts using AI weekly themselves | ~7 in 10 | Inside Higher Ed |
| Provosts reporting a **centralised** AI strategy | 🔴 **1 in 10** | Inside Higher Ed |
| US/Canada faculty intent to keep using AI | **76% → 67%** (2025→2026) | Digital Education Council |

**Adoption is finished; governance and proof are not.** Usage sits at 88–95% while policy awareness
sits at 26–54% and ROI satisfaction at 29%. Ellucian names **data privacy as the top barrier**.
The sellable work in 2026–27 is not "introduce AI" — it is **governance, evidence and
consolidation of what is already in use.**

## Opportunities by region

### Global

Opportunities that do not belong to one region, because the evidence for them is global:

1. **Governance before capability.** 88–95% usage against 26–54% policy awareness is the same gap
   in every region surveyed. The first deliverable in almost any engagement is a governed gateway
   with SSO, quota and an audit log — [LibreChat](https://github.com/danny-avila/LibreChat) (MIT) —
   plus the policy-to-configuration work that makes an institution's written rules enforceable
   settings. Data privacy is the named top barrier (Ellucian), and the audit log is the answer.
2. **Evidence as a product, because procurement is being rewired around it.** ~80% of institutions
   investing against 29% CTO ROI satisfaction, and a US federal push for measurable outcomes in
   procurement. Baseline and re-measure on the client's own subject mix with
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
   [MMLU](https://github.com/hendrycks/test) and [GSM8K](https://github.com/openai/grade-school-math)
   — all MIT, so there is no licence reason to omit it from any engagement.
3. **Compose over a copyleft platform; never fork it.** The platform tier is GPL/AGPL/ECL/LGPL and
   the agent tier is MIT/Apache/BSD, measured over 58 live repositories this pass. Build across
   LTI 1.3, MCP or web services. Where the client must own closed extensions to the platform
   itself, [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0) is the only major
   open-source LMS that permits it.
4. **Teacher-facing as the default, student-facing as a switch.** The restriction countertrend (DC's
   prohibited uses, ANZ sentiment, Brazil's draft law, an unconfirmed NYC moratorium) makes
   "teacher-facing only" a configuration a product must support from day one in every region.
5. **Regional configuration as a requirement, not a port.** The same tutor needs EU Art. 50
   transparency notices, Indian and Chinese provenance labelling, a DC-style prohibited-uses
   lockout and an ANZ teacher-facing mode. Build the regional policy layer once; four regimes now
   diverge far enough that a single global configuration is unsellable.

### North America

**Market.** Largest single region for AI-in-education spend. Canvas dominates higher-ed LMS.

**Regulation — state-by-state, and it moved fast in 2026.**
- **134 bills across 31 states** on AI in education — 🆕 `p384` **attribution corrected**: that is
  **MultiState's** count (as of **Mar 2026**), *not* a figure both trackers share. **FutureEd**
  counts **~71 bills across 27 states**, and a third tracker **77 across 27**. 🔵 The spread is a
  **definitional** difference, not a data error — the trackers draw the boundary of "AI in
  education" differently, so the counts are **not comparable** and should never be averaged. Cite
  one tracker by name with its date, or give the range **71–134**. **33–35 states plus Puerto Rico**
  have issued official guidance; guidance remains far more widespread than binding law.
- **Idaho SB 1227** — statewide generative-AI framework, signed **19 Mar 2026**, effective
  **1 Jul 2026**: district-level policies plus AI-literacy standards.
- **Oklahoma SB 1734** (Responsible Technology in Schools Act) — every district must adopt a
  written AI policy **before the 2027-28 school year**, covering approved and prohibited uses, data
  protection, family transparency and periodic review.
- **Maryland SB 720** — MSDE must publish guidance, offer professional development and help
  districts evaluate AI tools; establishes a statewide K-12 AI collaborative.
  🆕 `p385` **Dates and the clock that matters:** approved by the Governor **26 May 2026** (SB 720 /
  HB 1057, the *Artificial Intelligence Ready Schools Act*), reported effective **1 Jun 2026** — and
  local school systems must adopt an AI policy **aligned to MSDE's guidance within 120 days of its
  release**. 🔵 That is a procurement trigger with a deadline attached to someone else's publication
  date: when MSDE publishes, every Maryland district has four months. Worth watching rather than
  filing.
- 🆕 `p385` **Illinois SB 2909 — the first US limit found on AI in *teacher* evaluation.** Amends
  §24A-5 of the Illinois School Code to restrict the use of AI in evaluating teachers, **effective
  1 Jan 2027**. Separately, **ISBE released statewide guidance on 9 Jul 2026** covering AI in teaching,
  learning and school operations. 🔵 DC's non-mandatory policy already barred AI from teacher
  evaluations; Illinois makes that a statute. **Employment-adjacent AI is becoming its own regulated
  surface in education, distinct from student-facing AI** — and a product that grades teachers is a
  different compliance object from one that grades students.
- **Alabama HB 329** — an approved CS course including AI instruction becomes a graduation
  requirement.
- **Illinois** — AI-literacy instruction for grades 6–12 from **1 Aug 2026**; one source describes
  it as enacted without the governor's signature. 🟡 Verify against the statute before citing.
- **California AB 1159** (proposed) — would bar student data from training AI models unless the
  training directly benefits the school.
- **District of Columbia** 2026-27 policy (non-mandatory) — bans AI from **grading, discipline, IEP
  decisions and teacher evaluations**.
- **Federal:** US Department of Education "Dear Colleague" letter urges states to evaluate AI and
  ed-tech by **measurable learning outcomes rather than screen time**, and to build **evidence
  requirements into procurement**. No new federal rules.
- 🆕 `p386` **Federal legislation — the first AI-in-education bill found moving through Congress,
  and it is a *funding-eligibility* change, not a mandate.** **H.R. 8747, the K–12 AI Literacy and
  Readiness Act of 2026** (119th Congress), introduced by **Rep. Randy Fine (R-FL)** on
  **12 May 2026**, was **ordered to be reported (amended) by the House Education and Workforce
  Committee on 21 Jul 2026, 18–15**. It would amend the **Elementary and Secondary Education Act**
  so districts may spend **existing federal funds** on AI curriculum and teacher training.
  🔴 **No floor vote, no Senate action, not law** — and the committee vote was close and party-split,
  so do not price on it passing. 🟢 **What it is useful for anyway:** it names the funding streams a
  district would use, which is the question a K-12 buyer asks before the question about the product.
  🟡 Grade: `CONVERGENT-SECONDARY, PRIMARY UNREAD` — congress.gov and govinfo both carry it, neither
  is reachable from this sandbox; one snapshot still shows only "introduced and referred", so cite
  the **21 Jul 2026** committee action with its source.
- 🆕 `p386` **District-level bans are now specific enough to name.** **Katy ISD (Texas)** prohibits
  generative-AI chatbots for **K-6** and phases in supervised access **from grade 7, starting in
  2026-27**. 🔵 This is the shape the restriction movement actually takes — **not a state ban but a
  district age-gate** — and it is a procurement constraint a vendor meets in configuration: an
  age-banded deployment where the youngest cohorts get no chatbot surface at all. 🟡 Secondary
  sources only.
- 🟡 `p386` **The New York City moratorium: a second independent sighting, same grade.** This pass's
  North America leg returned the **one-year moratorium on student-facing AI through eighth grade**
  from a different source than the EdWeek item below. 🔴 **Still `UNCONFIRMED`** — two secondaries
  with inconsistent date metadata are not a primary, and the NYC Chancellor's office is not
  reachable from here. Keep it out of a client deck.
- 🆕 **Federal privacy — the amended COPPA Rule is the binding deadline that already passed.** The
  FTC's amended Children's Online Privacy Protection Rule took effect **23 Jun 2025** with **full
  compliance due 22 Apr 2026**. It brings a **broader definition of personal information**,
  **mandatory data-retention limits**, **separate parental consent for third-party data sharing**,
  and new **consent-verification methods**. 🟢 Unlike state guidance, this is enforceable now, and
  it bites directly on any K-12 AI deployment touching under-13 learners.
- 🔴 🆕 **And the gap inside it, which is the part that matters for ed-tech.** The Commission
  **did not finalize** the proposed **ed-tech / school-authorization** amendments, citing possible
  conflict with **anticipated FERPA rulemaking**. So **"the school consented" is not a mechanism the
  amended Rule provides.** A K-12 build cannot lean on school-authorized consent as a COPPA answer;
  it needs verifiable parental consent, or a design that never collects the personal information in
  the first place. 🟡 This is also a **moving target** — expect the gap to be closed by FERPA
  rulemaking, so write the data path to be reconfigurable rather than hard-coding today's answer.
- 🆕 **Higher ed is standardising at system level, not campus level.** The **SUNY** system adopted a
  **systemwide AI policy** that embeds **AI literacy into general education from fall 2026**. 🟢 The
  buying unit in US public higher ed is shifting from the campus to the system — one engagement,
  many institutions, and a single policy to implement against.
- 🔴 **UNCONFIRMED:** an EdWeek item reports a **New York City moratorium** on student-facing
  generative AI (attributed to Mayor Mamdani and Chancellor Samuels) as part of a wider restriction
  movement. The item's **date metadata is inconsistent** — do not put this in a client deck without
  primary confirmation. Several vendor-blog specifics (a Florida SB1194, Puerto Rico Copilot
  mandates) likewise did not verify.

**Opportunities.**
1. **Evidence-and-evaluation engagements, not pilots.** 80% investing against 29% ROI satisfaction,
   plus a federal push for evidence in procurement, is a procurement-grade measurement product:
   baseline on the client's own subject mix with
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) + MMLU + GSM8K
   (all MIT), then re-measure. Sells to the 71% without a centralised strategy.
2. **Policy-to-configuration.** 33–35 states' guidance and the Oklahoma/Idaho mandates are
   documents nobody has turned into enforced settings. Convert a state framework into LMS
   configuration, role permissions, retention rules and an audit trail that survives an inspection.
   DC's prohibited-uses list (grading, discipline, IEP, teacher evaluation) is a ready-made
   technical control set.
3. **Consolidation.** 95% usage with 26% policy means shadow AI everywhere. A governed campus
   gateway — [LibreChat](https://github.com/danny-avila/LibreChat) (MIT) with SSO, quota and audit —
   is the smallest credible first deliverable, and privacy is the named top barrier it answers.
4. 🆕 **COPPA-safe K-12 architecture, sold as a deadline response.** Full compliance was due
   **22 Apr 2026** and school-authorized consent is **not** available under the amended Rule. The
   deliverable is an architecture that keeps under-13 personal information out of the model path
   entirely: pseudonymised learner IDs, retention limits enforced in the store rather than in
   policy, no third-party sharing without separate consent, and an audit trail that shows it.
   🟢 Self-hostable components make this provable —
   [Kolibri](https://github.com/learningequality/kolibri) (MIT),
   [Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3),
   🆕 `p386` [OpenTutor](https://github.com/zijinz456/OpenTutor) (**MIT**, runs on local
   open-weight models with **no external model call at all** — the strongest form of this argument)
   and [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API) keep the
   student record on the client's own infrastructure. Pairs with the DC/Maryland prohibited-uses
   control set in opportunity 2.
5. 🆕 **Sell to the system, not the campus.** SUNY's systemwide policy with AI literacy in general
   education from fall 2026 is the template other public systems will copy. A system-level
   implementation — policy-to-configuration across member institutions, one evidence baseline,
   shared gateway — is a materially larger engagement than a single-campus pilot for the same work.

### EMEA

**Regulation — the dates are the product.**
- **Regulation (EU) 2026/1744** (the "Digital Omnibus on AI", published in the Official Journal
  **24 Jul 2026**) moved the AI Act deadline for **stand-alone high-risk education systems** from
  **2 Aug 2026** to 🟢 **2 Dec 2027**. 🆕 `p385` **corroboration upgraded: `p384` had two independent
  sources; this pass reproduces the same regulation number, the same OJ date and the same deferral across
  **nine** independent houses** (Cooley · FPF · Gibson Dunn · Jones Walker · Usercentrics · ActuIA ·
  Winston Taylor · Praxikon · aiacto). 🔴 **The grade does not change: `CONVERGENT-SECONDARY, PRIMARY
  UNREAD`.** EUR-Lex, `artificialintelligenceact.eu` and every law-firm host return DNS `ENOTFOUND` from
  this sandbox, so no primary text was read. Nine agreeing secondaries are still not the Official Journal.
- 🆕 `p385` **The nearest binding date is not 2027 — it is six weeks away.** The **Art. 50 transitional
  deadline for machine-readable marking of AI-generated content on systems ALREADY on the market is
  2 Dec 2026.** A tutor the client is running *today* is in scope on that date; the 2027 deferral does
  nothing for it. 🔵 This date was recorded in `intel/open-gaps.md` but had never reached this shelf,
  which is the shelf an engagement reads.
- 🆕 `p385` **Annex I (AI embedded in regulated products) moves to 2 Aug 2028** — a different date from
  the Annex III education one, and routinely conflated with it in vendor summaries.
- 🔴 **What did *not* move:** **Article 50 transparency obligations apply from 2 Aug 2026.**
- 🔴 **Already in force:** **Article 4 AI-literacy duty since 2 Feb 2025**, binding on every
  organisation that *uses* an AI system — therefore every school.
  🆕 `p386` **And as of this pass there is an official competence model to discharge that duty
  against — it was absent from this entire knowledge base.** The **OECD and the European
  Commission** published **"Empowering Learners for the Age of AI: an AI literacy framework for
  primary and secondary education"** (the **AILit framework**) as a **final** report on
  **18 Jun 2026**, after a May 2025 draft and a consultation the authors describe as involving
  **2,000+ people**, with support from **CodeAI** (formerly Code.org). Structure: **four domains —
  *Engage*, *Create*, *Manage*, *Shape* AI — 19 competences**, each on a **three-level learner
  progression**, mixing technical knowledge with dispositions (responsibility, curiosity, empathy),
  plus classroom examples on bias, misinformation and human oversight.
  🔴 **It is non-binding** — and that is exactly why it matters: **Article 4 is binding and vague,
  the AILit framework is detailed and optional**, so it is what a ministry, an inspectorate or a
  procurement panel will reach for when it has to say what "sufficient AI literacy" *means*.
  🟡 Grade: `CONVERGENT-SECONDARY, PRIMARY UNREAD` — the OECD publication page, the EC pages and
  every secondary host are DNS-unreachable from this sandbox; the title, the publisher pair, the
  18 Jun 2026 date and the 4-domain / 19-competence / 3-level structure reproduce across
  independent secondaries, the OECD catalogue listing included. **Emotion recognition in
  education institutions has been prohibited since 2 Feb 2025** (narrow medical/safety exception).
- **High-risk when it lands:** admissions, assessment, proctoring, plagiarism/AI-detection used in
  assessment, and personalised-learning systems that **steer learning paths**.
- **Extraterritorial:** any company placing an AI product on the EU market or deploying one that
  affects EU learners is in scope regardless of headquarters.
- **European Schools (eursc.eu):** **no generative AI tool has been officially approved for
  system-wide use.** The institutional buyer is still unresolved.

**Market.**
- Europe edtech ≈ **$61.11B in 2026, 12.85% CAGR** to 2034 (single source); **UK, Germany, France**
  lead. HolonIQ's 2026 Europe EdTech 200 puts the **UK first, Germany 13%, France 12%**; German
  names include Seven Education, Edurino, Tomorrow University.
- 🔴 **Germany figures conflict by ~80×** between sources ($9,241.7M for 2025 vs $107M).
  **Do not quote a single German market number.** DigitalPakt Schule's €6.5bn school-infrastructure
  commitment is the one solid German figure found.
- **Sovereign stack:** openDesk (ZenDiS), **v1.0 released 20 Oct 2024**; ZenDiS + France's DINUM
  (LaSuite) shipped videotelephony, notes and SSO across both suites in **100 workdays**.
  🔴 **The "8,600 schools" figure carried by an earlier pass remains UNCONFIRMED and this pass
  found no school deployment of openDesk in any source** — named users are administrative bodies.
  Sell the architecture (ILIAS + OpenProject behind SSO), not the number.
- 🟡 **Spain:** an earlier pass's Spanish-language search surfaced Spain's first AI-in-teaching
  regulation, invisible to English-language queries. **Not re-verified this pass** — carry the
  *method* (search in-language for EMEA regulation) and re-establish the claim before use.

**Opportunities.**
1. **A dated compliance roadmap, which is now a 14-month product.** "Article 4 AI literacy and
   Article 50 transparency **now**; high-risk conformity by **2 Dec 2027**" is specific enough to
   price. Most vendors are telling clients the deadline slipped and nothing is due — that is wrong
   and verifiably so.
2. **The licence constraint bites hardest here**, where public-sector clients demand both
   sovereignty and ownership. [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**) is
   the only major LMS a studio can extend with closed code; everything else in the tier is
   GPL/AGPL/ECL. Leading with OpenOLAT in EMEA public-sector bids is a real differentiator.
3. **Refusal-by-design assessment tooling.** Art. 50 transparency plus the high-risk assessment
   category favour citation-grounded architectures that decline to answer unsupported questions —
   [paper-qa](https://github.com/Future-House/paper-qa) (Apache-2.0) as the reference behaviour.
4. **Avoid, and say why:** proctoring and AI-detection-in-assessment. High-risk, no credible
   permissive open-source base, and emotion recognition is already outright prohibited.
5. 🆕 `p384` **The Gulf is the under-covered half of this region.** **Alef Education** (UAE) is
   named as a leading regional AI-in-education platform (🟡 vendor market-research sourced —
   reported, not verified), and it is the only Gulf player any search this pass surfaced. 🔴 **An
   informed gap, stated rather than left silent:** the four regional searches run this pass returned
   **substantial** material for the EU and the UK, and **almost nothing** for the Gulf, Türkiye,
   Israel or sub-Saharan Africa — no regulation, no named open-source supply, no market sizing.
   That is a **coverage gap in the sources, not evidence of low activity**, and it is the obvious
   place for a next pass to search in-language (Arabic, Turkish) the way the Spain finding was made.
   Do not read this file as saying EMEA = EU.

🆕 `p386` **6. AI-literacy compliance as a product, now that there is a framework to deliver
against.** **Article 4 has been binding on every school since 2 Feb 2025** and says only that
deployers must ensure sufficient AI literacy. As of **18 Jun 2026** the **OECD/EC AILit framework**
supplies the missing operational content: **4 domains, 19 competences, 3 proficiency levels**.
🟢 That combination — a binding duty with no definition, plus an official non-binding definition —
is the most sellable shape in EMEA education right now, and the deliverable is concrete rather than
advisory:
- map the client's existing curriculum and staff training onto the **19 competences**, producing a
  gap matrix per competence and per progression level;
- turn it into evidence an inspectorate accepts: who was trained, on what, when, assessed how;
- 🟡 and make the AI the client already runs part of the answer — a tutor that **cites its sources
  and declines without evidence** ([paper-qa](https://github.com/Future-House/paper-qa), Apache-2.0)
  teaches the *Manage* and *Shape* domains by being used, which is the only form of AI literacy
  that survives contact with a classroom.
🔴 **Sell it with the deadline that is actually near, not the 2027 one:** Art. 50 machine-readable
marking of AI-generated content for systems **already on the market** is **2 Dec 2026** — six weeks
out — and the AILit work is the same engagement's natural second phase.

### APAC

**Regulation — no single model, and education is explicitly named in one regime.**
- **Binding AI rules:** South Korea, China, Vietnam. **Guidance/existing law:** Japan, Singapore,
  Hong Kong, Australia, India.
- 🆕 `p386` **South Korea's rule now has a name and a date on this shelf.** The **AI Basic Act**
  (Framework Act on AI Development and Trust) **takes effect January 2026** and is described across
  independent sources as among the **first comprehensive national AI statutes anywhere**, structured
  around risk tiers, transparency duties for generative output and a domestic-representative
  requirement for large foreign providers. 🔵 It is **not** education-specific — that distinction in
  APAC still belongs to Vietnam — but it is the regime a Korean engagement is governed by, and Korea
  is also where one of the two named regional edtech players sits (**Riiid**). 🔴 **This fact was
  already in [`policy-matrix.tsv`](policy-matrix.tsv) and had never reached this shelf** — the same
  failure mode `p385` recorded for the Art. 50 date: recorded is not delivered.
  🟡 Grade: `CONVERGENT-SECONDARY, PRIMARY UNREAD`. 🔴 **And a claim this pass refuses:** one market
  report asserts education-specific AI statutes in Korea and Japan (e.g. a Korean "AI Data
  Protection Act" for EdTech). That conflicts with every regulatory summary read and is **not
  recorded as fact** — it is recorded here as a vendor claim to disbelieve.
- **Vietnam** — its decree names **education among six high-risk sectors**, covering **automated
  assessment and behavioural monitoring**. The most education-specific binding rule in the region.
  🆕 `p384` **the dates, which change how it is sold:** compliance is due **1 Mar 2027**, and
  systems **already operating in education before 15 Aug 2026** get an **additional six-month
  grace period** on top (Linklaters). 🟢 Two consequences. First, there is a **real deadline to
  price against**, as in EMEA — Vietnam is the APAC analogue of the EU high-risk roadmap. Second,
  the grace period rewards **being already deployed**: an education AI system live before
  15 Aug 2026 buys roughly six extra months of runway over one that goes live after. For a client
  still deciding, that date is a genuine input to the schedule, not a footnote.
- **China** — no general AI law; a stack of specific rules: recommendation algorithms (2022), deep
  synthesis/deepfakes (2022), generative AI service measures (2023), and **AI-generated-content
  labelling applicable from 1 Sep 2025**. **988 services had completed filing by 30 Jun 2026.**
- **India** — no dedicated AI law yet; amended **IT Rules require prominent labels and provenance
  markers on AI-generated content from 20 Feb 2026**; a dedicated law is in stakeholder
  consultation and drafting (IAPP).
- 🆕 `p385` **Australia — the governing document is still non-binding, and that is the finding.**
  The **Australian Framework for Generative AI in Schools** was agreed by education ministers in
  **Oct 2023** and applied from **Term 1 2024**; it covers privacy, student data, teaching/learning
  outcomes and wellbeing, and it is **not legislation — schools are not required to follow it**. The
  federal **National AI Plan (Dec 2025)** names education a priority and folds the schools framework
  into its commitments. 🔴 **A targeted search found no 2026 ministry update**, so a pitch that assumes
  Australia has moved to binding school rules this year is wrong. Sell to the framework's language and
  to institutional risk appetite, not to a mandate that does not exist.
- 🆕 `p385` **Commercial signal — TCS × Pearson, announced Mar 2026.** A multi-year alliance pairing
  Pearson's assessment products with TCS consulting and the **TCS iON** learning platform, including
  putting Pearson's **Versant** English test into TCS hiring and workforce programmes, plus AI-validated
  skill benchmarking and certification. 🔵 Relevant as **competitive context, not a client**: the
  corporate-skills/assessment lane in APAC is being consolidated by integrators, which is the same lane
  a Globant L&D engagement sells into. 🟡 Vendor-announced; not independently verified.
- 🔴 **UNCONFIRMED, both widely repeated:** that AI became a **compulsory subject in China from age
  six** by Sep 2025 with **≥8 hours/year** in Beijing schools; and that **India** will make AI and
  computational thinking **compulsory from Class 3 in 2026-27**. Neither was found in a government
  source this pass — check the PRC Ministry of Education and India's Ministry of Education before
  citing.

**Market and sentiment.**
- APAC AI market ≈ **USD 102B as of Mar 2026**; **India the fastest-growing at 38.9% CAGR**.
- One regional report's conclusion: **adoption breadth is extraordinary, depth remains shallow**.
- **Ipsos Education Monitor 2026:** *lower* support for banning AI in schools across the Asian
  markets examined — while **Australia and New Zealand record the highest support for banning**.
  One region, two opposite mandates. 🆕 `p384` **the global baseline that makes the split legible:
  39% globally favour banning AI in schools.** Asian markets sit below that line, ANZ above it — so
  the ANZ position is not regional caution, it is **above the world average**, and the restriction
  countertrend has a number attached to it.
- 🆕 **Named regional commercial players** (🟡 vendor market-research sourced — **reported, not
  verified**): **Squirrel AI** (China, adaptive tutoring), **Riiid** (South Korea, assessment and
  test-prep AI), **Byju's** (India). Global majors named as regional leaders: Google, Microsoft,
  IBM, Pearson. 🔵 Useful as competitive context for a bid; not usable as market-share evidence.

**Opportunities.**
1. **Provenance and labelling as an engineering deliverable.** India (20 Feb 2026) and China
   (1 Sep 2025) both require labels/provenance on AI-generated content. Any tutoring or
   content-generation product shipped into IN/CN needs watermarking and provenance **in the
   generation path**. This is a build, not a policy memo, and it is already overdue.
2. **The region is the open-source supply.** The strongest permissive education agents are APAC:
   [DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, HKU),
   [ai-shifu](https://github.com/AI-Shifu/ai-shifu) (Apache-2.0, China),
   [educhain](https://github.com/satvik314/educhain) (MIT, India),
   [Flat](https://github.com/netless-io/flat) (MIT) — and Moodle itself is Australian in origin.
   An APAC engagement can be built almost entirely on region-native permissive code.
3. **Shallow-depth remediation.** "Breadth extraordinary, depth shallow" is the brief: clients have
   bought tools and not changed outcomes. Pair an agent with
   [FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (MIT) retention measurement to show
   depth rather than usage.
4. **ANZ needs the restriction-compliant build** — highest ban support in the Ipsos data. Teacher-
   facing, no student-facing generative surface, full audit trail.
5. 🆕 **Vietnam has a dated high-risk roadmap, and almost nobody is selling against it.** Education
   is named high-risk; compliance lands **1 Mar 2027**, with six extra months for systems live
   before **15 Aug 2026**. That is a priceable 2026-27 engagement of exactly the shape that works in
   EMEA — classify the system, design human oversight into automated assessment, document it — and
   it is **portable**: an EU AI Act Annex III conformity asset adapts to Vietnam's risk model far
   more cheaply than it rebuilds. 🟢 Same asset, three markets: EU, Mexico, Vietnam.

### LATAM

**Adoption — the best-measured region in this pass.**
- **IDB** reviewed **193 initiatives** across Latin America and the Caribbean; its **Jan 2026**
  summary reports **59% used generative AI**.
- **CENIA** (cited by Foreign Policy): **13 of 19** LAC countries studied **do not yet teach early
  AI adoption in schools**.
- **Google.org** is funding an AI-literacy rollout (**$4.6M**) across **Argentina, Brazil, Chile,
  Colombia, the Dominican Republic, El Salvador, Mexico, Peru and Uruguay**, targeting
  **1.25M students by 2028**.
- **UNESCO's** regional AI-in-education observatory has a **Mexico pilot with CONALEP and DGETI
  announced Aug 2026**; partners include **CETIC.br** (Brazil) and **Tecnológico de Monterrey**
  (Mexico).
- 🔴 🆕 `p386` **The LATAM leg was re-run in full and returned nothing new — stated so that silence
  is not read as coverage.** Everything it surfaced is already on this shelf: the UNESCO
  IESALC/UNU-IAS survey (**200 institutions, 19 countries, 87% using AI in at least one area, 26%
  with a formal AI strategy**), the **LAC Observatory** launched **14 Apr 2026** at ECLAC in
  Santiago, Uruguay as the first LAC signatory of the Council of Europe AI convention, Colombia's
  **CONPES 4144**, Peru's sandbox-based framework and Mexico's pending federal bill. 🟢 Re-running a
  leg that returns only known facts **is** a result: it means this shelf is current, not that the
  search failed.
- 🔴 🆕 `p386` **And the one thing the leg still does not return, for the fourth consecutive pass:
  a LATAM-native open-source education agent address.** The targeted Spanish-language search
  returned exactly one candidate — [`jarodise/Language-Transfer`](https://github.com/jarodise/Language-Transfer),
  which is **ungranted** (verified this pass) and teaches Spanish *to non-speakers* rather than
  teaching *in* Spanish. **The regional supply gap is structural, not a search artefact.**

🆕 `p385` **A second, independent survey lands on the same gap — and adds the one split that tells a
studio what to BUILD.** The **Digital Education Council's *AI in Higher Education LATAM Survey 2026***
(**30,000+ responses, 29 institutions**) reports **92% of students** and **79% of faculty** actively
using AI, against **~30% of LATAM universities with a published AI policy** (Tec de Monterrey summary).
🟢 That is a **third** independent instrument converging on the 26–30% governance band already recorded
here from Coursera and IESALC — different method, different sample, same answer. Stop hedging it.

🔵 **And the actionable split, which the headline adoption numbers hide:** **50% of students support
AI-assisted feedback on their assignments, while only 19% of faculty currently use AI that way.** 🟢
**A 31-point demand gap on one named feature** — not "AI in education" in general, but *feedback on
submitted work*. That is a build target with its own evidence, and it points at the assessment stack
already on these shelves ([edx-ora2](https://github.com/openedx/edx-ora2) rubrics,
[pybryt](https://github.com/microsoft/pybryt) for approach-level assessment,
[nbgrader](https://github.com/jupyter/nbgrader)) rather than at another tutor.
🟡 Industry-produced survey; treat the figures as directional and cite the Council by name.

🆕 `p385` **Regulation, placed by country — heterogeneous, and no regional framework exists.**
**Chile** is furthest along: a **National AI Policy since 2021** and a law under discussion.
**Brazil** (PL 2.338/2023) and **Colombia** (CONPES 4144) have national strategies **with no
education-sector rules**. **Mexico** has proposals from **SEP**, **ANUIES** and the Observatorio IA
that **lack binding force**. 🔵 **The consequence for an engagement: in most of LATAM the binding
constraint is the institution's own policy, not the state's** — which is exactly why the 70% of
universities with no published policy is a services opportunity and not merely a risk statistic.
Instruments to cite: **ILIA** (Latin American AI Index, 19 countries, with ECLAC/CEPAL) and the
**IDB**'s AI-regulation and AI-in-education frameworks.

**🆕 `p384` — the governance gap now has a number, and it is the single most useful statistic in
this file for a LATAM pitch.** UNESCO IESALC's *AI Implementation in Higher Education in Latin
America and the Caribbean*, launched at **Digital Learning Week, Paris, September 2026**, surveyed
**200 institutions across 19 countries**:

| finding | figure |
|---|---|
| institutions using AI in **at least one area** | **87%** |
| using it in **teaching and learning** | **74%** |
| using it in **research** | **57%** |
| institutions with a **formal AI strategy** | 🔴 **26%** |

🟢 **Read the gap, not the adoption number.** 87% adoption against 26% strategy means the
sellable work in LATAM higher education is **not** "introduce AI" — it is governance, policy,
monitoring and evaluation retrofitted onto deployments that already exist and were never planned.
The study attributes adoption to **individual academics, researchers and students** rather than
institutional plans, and finds **public institutions more resource- and capacity-constrained** than
private ones. An engagement that opens with a tutoring pilot is selling into the 87%; one that
opens with an AI governance framework is selling into the 74-point gap.

**School-level adoption is equally high, from an independent source.** OECD **TALIS 2024** reports
roughly **half or more** of secondary teachers using AI in **Brazil, Chile, Colombia and Costa
Rica**, against an **OECD average of 36%** — LATAM teachers are *ahead* of the OECD mean, which
inverts the usual framing. Uruguay's **Ceibal** reports **75% of public-school teachers** using
these tools. 🔵 Combined with the IESALC strategy figure, the regional profile is consistent:
**high practitioner uptake, thin institutional governance.**

**Players.** HolonIQ's **2026 LATAM EdTech 100** finds the region's focus shifted to **workforce and
K-12**, with AI positioning concentrated in **teacher-facing instructional tools rather than
consumer tutoring**. Named: **Teachy** (Brazil, AI lesson preparation, has expanded beyond the
region into Asia), **Ginia** (Mexico, AI-driven employability linking employers, institutions and
students), **Vetto** (Brazil, raised new capital on a similar thesis).

**Regulation.**
- **Brazil PL 2.338/2023** — passed the **Senate**, now in the **Chamber of Deputies**. Reported to
  classify **"selection of students for access to education"** as high-risk. 🔴 **Bill text not
  verified this pass** — confirm against the Câmara record before relying on the classification.
- **LGPD** applies to all student data processing (transparency, security, accountability).
- Brazil's **CNE** has issued guidance on regulating educational AI (reported by Valor);
  🔴 the guidance text itself was not located.
- **Mexico** has a generic AI regulation that **seeks to replicate the EU AI Act's risk model**
  (AlSur consortium study) — meaning EU-shaped compliance work is partly portable to Mexico.
- 🆕 **Colombia chose policy before binding rules: CONPES 4144** (**Feb 2025**) sets out actions and
  a budget running **through 2030** rather than immediate obligations. 🟢 For a studio this is the
  friendliest LATAM jurisdiction to deploy in now — and the one where a governance framework is
  procurable as policy alignment rather than forced by a compliance deadline.
- 🆕 **Chile** has a government bill on the **same risk-based model**, tied to the forthcoming data
  protection authority; still at **committee stage in the Chamber**. Not yet a compliance deadline.
- 🆕 **Institutional anchor:** UNESCO launched the **Observatory on AI in Education for Latin
  America and the Caribbean** in **April 2026 at ECLAC, Santiago**, to steer public policy; UNESCO
  also runs AI-ethics and regulation training for officials in **Ecuador and Chile**. 🔵 A regional
  policy counterparty now exists — relevant to any public-sector bid.
- 🆕 **Talent shape (ILIA 2025, Latin American AI Index):** **AI literacy is far more widespread
  than advanced specialised talent**; school-level AI education and postgraduate programmes are
  growing but remain exceptions. 🟢 Implication for staffing a LATAM engagement: expect to find
  users and trainers locally and to import or build deep engineering capacity.

**🔴 The open-source supply gap, measured rather than assumed.** A targeted search for
LATAM-origin open-source education software on GitHub — SIGAA source, Portuguese/Spanish-language
academic management, AI-enabled administration from the region — **returned nothing usable**. No
SIGAA source is published; no AI-enabled open-source academic-management system from the region was
found. The only regionally-fitted options are
[academico-sis/academico](https://github.com/academico-sis/academico) (MIT, Laravel, Spanish built
in, SME-scale) and [Chamilo](https://github.com/chamilo/chamilo-lms)'s public-sector install base,
plus OpenEduCat's Brazil/Mexico country pages, which are **vendor marketing with unverified feature
claims**. This is a genuine supply gap, not a search failure — and it is **the clearest
build-vs-buy opening in the entire rotation.**

**Opportunities.**
1. **Build the gap.** A permissive, Portuguese/Spanish-native academic-management layer with AI
   built in has no open-source incumbent. Start from `academico` (MIT) or OpenEduCat's Odoo base
   (LGPL) rather than from zero. 🆕 `p386` **A third starting point, verified this pass and
   licence-clean:** [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (**MIT**, ref
   `master`) + [krayin/laravel-crm](https://github.com/krayin/laravel-crm) (**MIT**, ref `2.2`) —
   a plugin-based Laravel ERP plus a CRM for the admissions funnel, the same stack `academico`
   already proves fits the region's SME school market, with the client owning every line including
   the education modules. 🔴 Cost it as a build: no education module ships in either.
2. **Teacher-facing, which is where the market and the regulation agree.** HolonIQ finds regional AI
   concentrated in instructional support, and Brazil's draft law targets **student-selection** uses.
   Lesson preparation, assessment drafting and feedback — [educhain](https://github.com/satvik314/educhain)
   (MIT) — carry the market and sidestep the regulatory hot zone.
3. **Offline-first is not optional.** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
   default ref `develop`) for connectivity-constrained deployments; the Google.org rollout's nine
   countries are exactly this profile.
4. **AI-literacy delivery at scale.** 13 of 19 countries do not teach early AI adoption while
   Google.org funds 1.25M students by 2028 — curriculum, teacher training and measurement are
   fundable now, and the permissive courseware exists
   ([ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners), MIT;
   [agents-course](https://github.com/huggingface/agents-course), Apache-2.0).
5. **Portable EU compliance.** Mexico replicating the EU risk model means an EMEA compliance asset
   can be re-sold into Mexico with adaptation rather than rebuilt.
6. 🆕 **Sell the governance retrofit, not the pilot.** 87% of LAC higher-ed institutions already
   use AI and only 26% have a strategy (IESALC, Sept 2026). The deliverable with the clearest buyer
   is an **AI governance, policy and evaluation framework** applied to systems already running —
   inventory, risk classification, human-oversight design, monitoring and an evidence baseline.
   It needs no new platform, it is fundable from existing institutional budgets, and Colombia's
   CONPES 4144 gives it a public-policy hook. Pair it with
   [`lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) (MIT) so the
   framework ships with measurement instead of a policy PDF.

## Sources

Precedence Research · Grand View Research · Research and Markets · Markwide Research · Technavio ·
Coursera (AI in Higher Education, 2026) · EDUCAUSE 2026 AI survey · Ellucian 3rd Annual Higher
Education AI Survey · Inside Higher Ed / Hanover Research · Digital Education Council Global AI
Survey 2026 · MultiState · ExcelinEd · EdWeek · US Department of Education Dear Colleague letter ·
Regulation (EU) 2026/1744 (OJ 24 Jul 2026) · European Schools (eursc.eu) · HolonIQ Europe EdTech
200 and LATAM EdTech 100 · Wikipedia (openDesk, ZenDiS) · IAPP · Latham & Watkins APAC AI
regulation · Ipsos Education Monitor 2026 · IDB · CENIA via Foreign Policy · UNESCO LAC AI-in-
Education Observatory · AlSur · EdTech Innovation Hub (Google.org).

**Added `p385`:** Digital Education Council, *AI in Higher Education LATAM Survey 2026*
(30,000+ responses, 29 institutions) · Tecnológico de Monterrey (TecScience) on LATAM university AI
policy coverage · Illinois **SB 2909** and **ISBE** statewide guidance (9 Jul 2026) · Maryland
**SB 720 / HB 1057** *Artificial Intelligence Ready Schools Act* (approved 26 May 2026) ·
**Australian Framework for Generative AI in Schools** (education ministers, Oct 2023; applied Term 1
2024) and Australia's **National AI Plan** (Dec 2025) · TCS–Pearson alliance announcement (Mar 2026,
vendor-announced) · nine-house corroboration of **Regulation (EU) 2026/1744** (Cooley, FPF, Gibson
Dunn, Jones Walker, Usercentrics, ActuIA, Winston Taylor, Praxikon, aiacto) — 🔴 **all secondary;
EUR-Lex and every law-firm host are DNS-unreachable from this sandbox, so the primary text remains
unread and the EU dates keep their `CONVERGENT-SECONDARY` grade.**

**Added `p384`:** UNESCO IESALC, *AI Implementation in Higher Education in Latin America and the
Caribbean* (Digital Learning Week, Paris, Sept 2026 — 200 institutions, 19 countries) · OECD
**TALIS 2024** · **Ceibal** (Uruguay) · **CONPES 4144** (Colombia, Feb 2025) · UNESCO Observatory
on AI in Education for LAC (ECLAC, Santiago, Apr 2026) · **ILIA 2025** Latin American AI Index ·
FTC **amended COPPA Rule** (effective 23 Jun 2025, full compliance 22 Apr 2026; ed-tech /
school-authorization amendments **not finalized**, deferred to anticipated FERPA rulemaking) ·
**SUNY** systemwide AI policy · **MultiState** (Mar 2026, 134 bills / 31 states) and **FutureEd**
(~71 / 27) trackers, counted separately · **Linklaters** on Vietnam's high-risk AI decree dates ·
Precedence Research (regional players — vendor-sourced, reported not verified).

🔵 **Source-grade note.** Of what `p384` added, the IESALC study, TALIS, CONPES 4144 and the FTC
Rule are **primary or institutional** and can be cited in a client deck as they stand. The named
commercial players (Squirrel AI, Riiid, Byju's, Alef Education, Teachy, Ginia, Vetto) come from
**vendor market research** and are competitive context only. The distinction is the difference
between a defensible slide and a retracted one.
