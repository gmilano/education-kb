---
industry: education
region: Global
updated: 2026-11-04
---

# 🗺️ Market map — Education

> Key players, market structure and opportunities placed by region.
> Sources this pass were predominantly vendor blogs, market-research marketing and policy trackers. Figures are **directional**; every number below names its source and flags where sources disagree.

## Market size — and why the numbers disagree

| Segment | Figure | Horizon | Source |
|---|---|---|---|
| AI tutors | $3.6B (2026) → $17.7B (2033) | 2026–2033 | Grand View Research |
| AI-powered education tools (broad) | >$17B by end of 2026 | 2026 | Vendor aggregate |
| AI in Education (global) | $11.4B → $57.2B | 2026–2030 | Grand View Research (carried, not re-verified) |
| AI in Education (global) — **conflicting CAGR on the same dollar figures** | $11.4B → ~$57B at **16.8%** CAGR | 2026–2033 | Coherent Market Insights |
| AI in Education — APAC | ≈ $2.85B, 35.3% CAGR | 2026 | market-research secondary |
| AI in Education — Europe | ≈ $2.64B | 2026 | market-research secondary |
| AI in Education — Middle East & Africa | ≈ $0.56B → $1.6B | 2026–2030 | market-research secondary |

**These do not reconcile**, and the disagreement is informative rather than noise. Note in particular that **two sources quote the same dollar figures with incompatible growth rates (25.9% and 16.8%)** over near-identical horizons, which means at least one is arithmetically wrong — a useful reminder that these are marketing documents, not research. Further: "AI tutors" ($3.6B) and "AI-powered education tools" (>$17B) differ by roughly 5× because one counts a product category and the other counts every tool with an AI feature. Do not quote a single market size to a client without naming the scope. Treat the AI-tutor figure as the addressable one for tutoring engagements.

## Global demand-side readings new at p652

| Reading | Scope | Source |
|---|---|---|
| **Only 15% of students say AI is integrated into many of their courses; only 29% believe their instructors are well equipped to guide AI use** | global higher education | Digital Education Council, AI in Higher Education Global Survey 2026 |
| **Purpose-built beats general-purpose, as a policy recommendation**: *"As general-purpose GenAI tools are not designed specifically for learning, education systems should incentivise the development of tools that aim to enhance teaching and learning"*; tools with an intentional pedagogical purpose *"tend to show sustained improvements in learning"*, while *"if designed or used without pedagogical guidance, outsourcing tasks to GenAI simply enhances performance with no real learning gains"* | OECD member systems | **OECD Digital Education Outlook 2026**, published January 2026 *(quoted from search excerpts of the PDF; `www.oecd.org` does not resolve in this session, so the report was not read at first hand)* |
| **April 2026 ADA accessibility deadline for large US public institutions** | United States | secondary (Campus Technology prediction round-up) |
| 2026 framed sector-wide as the year the question shifts from *whether* to use AI to *under what conditions* | global | 1EdTech |

🔵 **The OECD recommendation is the single most strategically useful sentence this page has acquired at p652, because it is an OECD-level endorsement of exactly what this KB's shelf is made of.** "Incentivise the development of tools that aim to enhance teaching and learning" is a policy instruction to fund purpose-built education AI over generic chatbots — and the purpose-built, permissively-licensed options are enumerated in `agents/top.md`. Pair it with the Digital Education Council's 15%/29% finding and the gap is explicit: systems are being told to buy purpose-built tools, 85% of students do not yet see AI in most courses, and 71% do not think their instructors could guide them if they did. **Tool supply is not the constraint; integration and teacher capability are.** That is a services market, and it is what Globant sells.

## Structural read of the market

Three facts shape every engagement:

1. **Usage has decisively outrun governance.** 86% of education organisations use generative AI, and most lack a policy. One 2026 benchmark reports 54% of K-12 students and 92% of university students using AI. The buying trigger in 2026 is frequently *governance*, not capability — institutions already have AI in the building and no control over it.
2. **Agent deployment is still rare.** The Bridges 2026 survey of K-12 and college leaders found relatively few districts and colleges running AI agents in day-to-day operations, with leaders explicitly wary of giving agents access to sensitive student data. The gap between "using chatbots" and "running agents" is where the integration work is.
3. **The evidence base is thin, and buyers know it.** A July 2026 scoping review of 474 studies found the field fragmented, with pedagogical design poorly connected to technical capability. A 2025 study found AI tutors adapt worse in real time than human tutors. Expect pilots with measurement attached, not big-bang rollouts.

## Global players

| Player | Type | AI strength | Weakness | Globant opportunity |
|---|---|---|---|---|
| **Instructure (Canvas)** | Commercial SaaS | Canvas AI: grading copilot, content suggestions | Cost, lock-in | `canvas-mcp` (MIT) agent layer on the client's existing Canvas — no platform migration needed |
| **Anthology (Blackboard)** | Commercial SaaS | Scale in North American HE | Legacy stack, post-merger drift | Migration to Moodle/Open edX plus an agent layer |
| **Khanmigo (Khan Academy)** | Nonprofit | Socratic tutoring at scale; the reference implementation | Not open source | UX reference, not a technical base |
| **OpenMAIC (Tsinghua)** | Open source, MIT | 42.7k ★, multi-agent classroom, v1.4.0 | Research-led; China-origin governance questions in some markets | Strongest permissive base for simulation-style learning |
| **DeepTutor (HKUDS)** | Open source, Apache-2.0 | 55k ★, lifelong learner model | Self-hosting and model costs fall on the client | The default tutoring base |
| **Microsoft Education AI** | Cloud/enterprise | Agentic admin workflows, Azure integration | Azure dependency | Globant as a vendor-neutral implementer |
| **Learning Equality (Kolibri)** | Nonprofit, open source, **MIT** | 1.2k ★ offline-first learning platform; the only permissive production platform found | Not an institutional LMS — no enrolment-at-scale or gradebook of the Moodle kind | The base for every low-connectivity engagement, and the one platform where a closed derivative is permitted |
| **AI-Shifu (Harbin Institute of Technology)** | Open source, Apache-2.0 | 331 ★; course authoring from a subject expert's intent, embeddable in the client's portal | Small relative to DeepTutor/OpenMAIC; research-led | The authoring end of the pipeline, where the client has subject experts but no instructional designers |
| **Squirrel AI** | Commercial (APAC) | Adaptive learning at scale in China | Closed, regionally bound | Competitive reference for APAC adaptive engagements |

## Opportunities by region

### North America

**Regulatory posture:** heavy state-level legislative activity, binding rules still uncommon. More than 134 bills across 31 states addressed AI in K-12 and higher education in the 2026 session (MultiState / FutureEd tracking). Enacted examples: **Idaho SB 1227** (statewide framework, local policies, AI-literacy standards, data-privacy requirements, and an explicit bar on AI replacing human teachers); **Maryland SB 720** (statewide guidance, district AI coordinators, the Maryland AI Education Collaborative); **Ohio** (districts required to adopt AI policies by 1 July 2026, but the statute is near-silent on content and names no enforcement mechanism); **Florida** (State Board approved AI rules for K-12 and the 28 state colleges). Federally, the K-12 AI Literacy and Readiness Act of 2026 advanced out of the House Education and Workforce Committee, and a 2026 federal grant rule prioritises AI literacy.

**Adoption (measured at p651):** the most mature market and the most policy-constrained.

| Reading | Source |
|---|---|
| **60% of US teachers use AI tools** | Gallup, via secondary reporting |
| **55% of high-school principals say their school has not blocked or restricted AI tool access** | secondary |
| ~70% of institutions across Europe and North America have guidance or are developing it | secondary |
| More than **1,500 AI-related bills** introduced across US legislatures in 2026; ~134 of them education-specific across 31 states | MultiState / FutureEd tracking |
| 92% university student usage against institutions that mostly lack policy | carried from p650 |

🔴 **One North America claim was tested this pass and does not verify.** A widely-repeated summary attributes to **North Carolina Session Law 2026-41** a state AI model policy due 2026-12-31, local district policies due 2027-06-30 and teacher training due 2028-06-30. Checked against the legislature's own summaries: **SL 2026-41 is the 2026 Appropriations Act (Senate Bill 257)**; it carries AI provisions (a DPI directed grant extending the AI Pilot Program to Alamance-Burlington Schools) but **no model-policy mandate was found in it**. The AI-literacy content-standards requirement appears under a **different** session law (**2026-61, House Bill 268**), and the DPI model-policy language appears only in *bills* — along with Senate Bill 981's proposed AI in Education Task Force reporting by 2028-03-15. **Those dates are not published on this page.** Full disposition in `intel/measured-unusable.md`.

🟢 **Canada, recorded for the first time after three consecutive passes where this leg returned only US sources.** The gap note below has said for three passes that "North America" on this page meant the United States. It no longer has to.

| | Reading (secondary; see the note on unreachable hosts) |
|---|---|
| Federal strategy | A **national AI strategy published 4 June 2026**, roughly 50 pages. Includes a **National AI Literacy Initiative** targeting **one million entry-level post-secondary students** and training **more than 3,000 educators** with AI learning kits. |
| Federal regulation | 🔴 **There is no Canadian AI Act.** AIDA (part of Bill C-27) **died when Parliament was prorogued in January 2025** and has not been reintroduced. Governance runs through privacy and sector law: PIPEDA federally, **Quebec's Law 25**, plus sector guidance (OSFI, Health Canada). The widely-circulated belief that AIDA is in force is wrong and worth correcting in any client conversation. |
| K-12 guidance | **Three provincial education ministries** had published K-12 AI guidance as of December 2025. **Quebec issued a March 2025 directive suspending the use of AI assistants**, still in place as of December 2025. **Nova Scotia has no provincewide policy** — regional centres set their own rules and the department calls provincewide guidance an "ongoing conversation". |
| Criticism of the strategy | No clear timelines or KPIs, and no named accountable owner in government. |

🔵 **What Canada actually is, commercially:** a large federal *capability* commitment with no binding regulation behind it and provincial policy ranging from an outright suspension (Quebec) to nothing at all (Nova Scotia). That is the opposite of the US profile on this page — there, mandates without guidance; here, funded ambition without mandates. The offers are therefore different, and a single "North America" proposal template will mis-fit one of the two countries.

**🆕 New at p653 (the rest of this section reproduced and is unchanged):**

| Reading | Source |
|---|---|
| **Four states — Maryland, Idaho, Oklahoma and Virginia — have 2026 laws requiring *both* statewide guidance *and* mandatory district-level AI policies.** This is the tightest binding pattern in the US and the one that creates a dated, funded procurement at district level | Pursuit policy tracking (secondary) |
| 🔴 **Washington DC issued a policy barring AI from grading, discipline and IEP decisions** — non-mandatory, but it is the clearest US articulation yet of *where* AI is unacceptable rather than how to adopt it, and it maps almost exactly onto EU AI Act Annex III's high-risk list | Pursuit (secondary) |
| **New York A 9190** would restrict classroom AI use to **ninth grade and above**, with carve-outs for diagnostics and special education | MultiState (secondary) |
| **The "STUDENTS FIRST Act of 2026"** — a national framework for AI in schools authored by students from all 50 states, published 3 August 2026, explicitly rejecting *both* an outright ban *and* unrestricted adoption | AASA |

🔵 **Why the DC item matters more than its legal weight.** A non-binding district policy is not a market. But *grading, discipline and IEP decisions* is the same prohibition shape as Annex III, arrived at independently — which is the first evidence this base has that the US and EU are converging on **which uses are unacceptable** even while diverging completely on instruments. A deliverable designed against Annex III is therefore more portable into North America than the regulatory divergence suggests. Note this is a **reversal of direction** from T8 (regulation is diverging by region): divergence holds for instruments, convergence is appearing in prohibited uses.

**Opportunities:**
- 🟢 **Canada's AI-literacy commitment is a curriculum sell, not a compliance sell.** One million post-secondary students and 3,000+ educators is a delivery problem with public money attached and no regulation to satisfy. This is the one North American opportunity on this page where the deliverable is teaching material and teacher capacity rather than controls — and `patchy631/ai-engineering-hub` (MIT, 41.1k★) is a permissive base for exactly that. See `compose/patterns.md` **P10**.
- 🔵 **Provincial fragmentation is the Canadian version of the policy-to-implementation gap**, with one twist: in Quebec the current posture is *suspension*, so the sellable work is the evidence and governance case that would let a directive be lifted, not a deployment. Do not pitch classroom AI into Quebec as though the Ontario or Alberta conversation applies.
- **Policy-to-implementation gap as a service.** Ohio-style mandates require a policy with no guidance on content, and Maryland requires a district AI coordinator role that districts have no one to fill. Globant can productise the compliance artefact *plus* the technical controls behind it, repeatable across districts.
- **Canvas-first agent pilots.** Canvas dominates North American HE. `canvas-mcp` (MIT, 317★) reaches real course data with no migration — the shortest credible path to a funded pilot.
- **"No AI replacing teachers" as a design constraint, not an obstacle.** Idaho's bar makes teacher-augmentation framing legally safer than autonomy. `Instructional Agents` (MIT) automates course *preparation* — exactly the defensible side of that line.
- OATutor (MIT, UC Berkeley) carries domestic academic provenance, which matters in public procurement here.

### EMEA

**Regulatory posture:** the most binding regime in the world, and the timeline just moved. The **Digital Omnibus (Regulation (EU) 2026/1744)** deferred high-risk obligations for stand-alone education AI from 2 August 2026 to **2 December 2027**. Guides still citing August 2026 are out of date. High-risk covers **admissions, learning-outcome evaluation, student level placement, and exam/behaviour monitoring**. **Article 50 transparency duties apply from 2 August 2026** — a school running a student-facing chatbot owes disclosure *now*. **Emotion recognition in schools has been prohibited since February 2025.** Article 4's AI-literacy duty was softened from "ensuring a level of AI literacy" to "taking measures". Schools are **deployers** under the Act.

🟢 **The Africa and Middle East half of EMEA, recorded for the first time.** Previous passes declared "no Africa-specific regulation or adoption data" as a gap. p651 found demand-side material and can now locate the gap precisely rather than leaving it as silence.

| | Reading (secondary sources; directional) |
|---|---|
| Market split | **Europe ≈ $2.64B (2026)**; **Middle East & Africa ≈ $0.56B (2026) → $1.6B (2030)**. Europe is ~5× MEA today and MEA grows faster. |
| K-12 leaders in Europe | Finland, Estonia and the Netherlands named as furthest along on integration |
| Institutional guidance | ~70% of institutions across Europe and North America have guidance or are developing it |
| Gulf policy | **Saudi Arabia has made AI literacy a mandatory component of undergraduate education**; the **UAE** has extended AI-focused programmes across all education levels. Gulf states lead the region on policy, and the emphasis is economic development and tertiary education rather than the ethics-and-transparency framing dominant in Western Europe (academic corpus comparison of six Western European and six MENA countries). |
| Africa regional frame | The African Union's **CESA 16-25** sets the continental digital-education direction; implementation varies widely by country and most structured AI use is government- or NGO-piloted. |
| Africa, this week | **Google launched a free, offline-capable AI and digital-skills training platform for Nigeria and other African markets around 3 November 2026** — lessons downloadable over Wi-Fi then usable without mobile data, in English, Swahili and Arabic with Hausa being added. Proprietary. Separately, **Google and Fab AI are working with innovators in Kenya, Ghana and South Africa on open Gemma models, with datasets, evaluation suites and open-source models stated to be released publicly** — the clearest forward signal of African open-source education supply this base has seen. *(`blog.google` does not resolve under this session's network policy, so Google's own announcement could not be read at first hand; both items rest on secondary reporting and should be re-verified.)* |
| Africa, supply side | **Mdali** (Johannesburg) adapts open-source models into an offline-first maths tutor for CAPS Grades 10–12 that runs on basic phones and keeps student data on-device; NVIDIA Inception member. **No public repository found.** Kenya's M-Shule (SMS-based) and Ghana/Côte d'Ivoire's Chalkboard Education are older offline-learning precedents. |

🔵 **Where that leaves the Africa gap:** it is **not** a demand gap and **not** an absence of builders. African AI-education products are real, offline-first by design, and built *on* open weights — but they ship as **proprietary applications rather than open repositories**. That is a precise, actionable finding: the partnering motion for Africa is co-development with existing product teams, not adoption of an African open-source stack, because there is not yet one to adopt. Watch the Google/Fab AI open-model releases, which would change this.

🟢 **The United Kingdom, recorded for the first time.** Posture is light-touch, principle-based and delivered through existing regulators rather than a statute — but two concrete, dated education instruments now exist: the **Department for Education's generative AI product safety standard for education (January 2026)**, and **Ofqual's resources on AI and coursework integrity (March 2026)**. A product safety standard is the most directly useful of the two for a vendor-side engagement: it is a published bar an edtech product can be built and tested against, in a market with no AI Act obligations to wait for.

🟢 **Africa, country level — the gap p651 located is now populated, and the shape of it is confirmed rather than overturned.** p651 declared that no country-level education AI regulation existed for any Sub-Saharan African state. Searched specifically this pass; the accurate statement is narrower and more useful: **national AI *strategies* with explicit education commitments exist; education-sector *rules* do not.**

| Country | Instrument | Education content | Status |
|---|---|---|---|
| **Kenya** | **National AI Strategy 2025–2030**, launched 27 March 2025 | Talent pillar commits to **AI literacy across all demographics and integration of AI into primary, secondary and higher-education curricula**, plus expanded STEM with a focus on women and underrepresented groups; **DigiKen** Digital Innovation Hubs as curriculum anchors | Strategy, not a rule. 🔴 **No national AI-literacy framework has been published**: a September 2026 report describes the Education Cabinet Secretary and the government's Special Envoy on Technology *planning* how the system should prepare, with curriculum framing around Kenya's languages and local values, and education commentary from roughly two months ago still calls for a framework aligned to the Competency-Based Curriculum. A separate **Kenya AI Bill (2026)** is a legislative item, not education policy. |
| **South Africa** | Draft **National AI Policy** | — | 🔴 **Published for comment 10 April 2026 and withdrawn/abrogated 27 April 2026** — seventeen days. Status should be re-verified before it is quoted. Separately, the Department of Basic Education has pursued coding-and-robotics curriculum reform including AI elements. |
| **Nigeria** | **National Digital Economy Policy and Strategy (2020–2030)** | References AI; application in education systems is **aspirational rather than systemic** | Strategy, not a rule |
| **Continental** | African Union AI strategy | **Phase 1 (2025–2026) is establishing governance structures and national strategies** — i.e. the continent is, by its own timeline, still at the strategy stage | On schedule, by design |

🔵 **So the Africa finding is now two-sided and consistent.** p651 established that African AI-education *supply* is real but ships as proprietary apps rather than open repositories. p652 establishes that African AI-education *governance* is real but sits at strategy level rather than rule level. **Both halves point at the same engagement:** there is no compliance deadline to sell against and no open stack to adopt, so the motion is capability-building and co-development with existing teams and ministries — on a strategy's commitments, not a regulation's deadline. Kenya is the furthest along and the clearest entry point; its missing AI-literacy framework is a named, unfilled deliverable in a published national strategy.

**🆕 New at p653 — the capability denominators, which this base did not hold:**

| Reading | Source |
|---|---|
| 🔴 **Only about one third of national school curricula in the EU include AI-related competences** | European Commission, AI-and-skills brief, 23 October 2026 |
| 🔴 **Around 30% of teachers have taken part in any AI-focused training**, and the Commission states plainly that most teachers still lack the skills to use AI responsibly in the classroom | European Commission, same brief |
| **The Apply AI Alliance** convenes AI providers, industry, public sector, academia and social partners — the Commission's chosen vehicle for closing the adoption gap | European Commission |
| Finland's SME upskilling programme is named by the Commission as the model to replicate | European Commission |

🟢 **These two numbers are the most commercially useful readings in this section, because they are the denominators under the compliance deadline.** EMEA has the world's most binding education-AI regime, with high-risk obligations falling due **2 December 2027** and Article 50 transparency duties live since 2 August 2026 — and **two thirds of curricula and seven in ten teachers are not ready.** A conformity-by-design deliverable sold without a teacher-capability component is being sold into a system that cannot operate it. That makes AI literacy a **gating dependency of the compliance sale in EMEA**, not an adjacent upsell — the same conclusion `compose/patterns.md` P10 reached for funded mandates, arrived at here from the supply side.

🟢 **Supply-side change in this region, new at p653:** the Apache-2.0 institutional LMS this base found this pass, **OpenOlat**, is an EMEA asset — descended from the University of Zurich's OLAT, maintained by frentix GmbH in Zurich, with its deepest adoption in German-speaking higher education, and with `langchain4j` already in-tree so an in-jurisdiction no-egress deployment is configuration rather than a fork. For a European public-sector engagement that is the strongest licence-and-residency position on this shelf. See `verticals/solutions.md` **Pattern F** and `compose/patterns.md` **P11**.

**🆕 New at p654 — the private-capital picture, which this section did not hold.** EMEA has been
covered here through policy and open-source supply. The commercial supply side was absent, and it names
the competitors and potential partners a Globant engagement meets in the room:

| Company | Round | Detail | Source |
|---|---|---|---|
| **Multiverse** (London) | **$70M at a $2.1B valuation**, announced **15 May 2026**, led by **Schroders Capital** | AI workforce training. Tracxn files it as **Series D**; it is the company's **first round since 2022**, and it follows the **January 2026 acquisition of StackFuel** (Germany, data and AI training). Total raised is reported inconsistently — **~$570M** in one source against **$485M over 6 rounds** in Tracxn | FT via secondary reporting; Tracxn |
| **Ed.ai** | ~$5.8M, September 2026 | AI-assisted grading, expanding across France and Europe | secondary |

🔴 **A name-clash trap worth recording before it causes an error.** **Multiverse** (London, edtech) and
**Multiverse Computing** (quantum and model compression, $215M Series B in June 2025) are different
companies, and search results mix them freely. One secondary source already attributes the edtech round to
"Multiverse Computing". Any funding figure for "Multiverse" must be checked against the business
description, not the name.

🟡 **Two further EMEA rounds were found and could not be confirmed, so they are filed as unverified
rather than published as readings:** **Medly AI** (reported $8M seed, August 2026, GCSE exam preparation)
and **Lucida AI** (reported $5.4M seed, April 2026, voice-first language coach). A targeted follow-up
search returned nothing on either. Treat as leads, not facts.

🔵 **The market context these sit in cuts against the funding headlines.** HolonIQ counted roughly
**$1B of global edtech venture funding in H1 2026, down 26% year over year** — so Multiverse's $70M is a
large share of a shrinking pool, which is a consolidation signal rather than a growth one. A claim that
Europe captured **62.3% of year-to-date 2026 edtech capital** circulates alongside it; it rests on a
small sample driven by a few large deals and should not be quoted as a market share.

**Opportunities:**
- 🟢 **Kenya's unwritten AI-literacy framework is the most specific unfilled deliverable this page holds for Africa.** A national strategy commits to AI literacy across three education levels; no framework implements it; the ministry is at the planning stage as of September 2026; and the published asks are alignment to the Competency-Based Curriculum and to UNESCO's competency frameworks, with teacher training and equitable access. That is a scope statement written by the client.
- 🟢 **The UK product safety standard is a build-to-spec opportunity with no waiting period.** Unlike the EU, there is nothing to be conformant *by*; there is a published bar to be conformant *to*, now. For a vendor-side client it de-risks procurement into UK schools immediately.
- **The December 2027 window is the commercial story.** Clients have roughly 13 months of runway to get high-risk systems conformant. Conformity-by-design engagements for admissions and assessment scoring are sellable now and have a deadline attached — the strongest forcing function in any region.
- **Transparency is live today.** Article 50 compliance for existing chatbots is immediate, small, and a clean door-opener into larger work.
- **Data-residency tutoring.** Self-hosted DeepTutor or Open TutorAI CE with local models via Ollama keeps learner data in-jurisdiction — the architecture EMEA public education actually buys.
- 🟢 **Gulf tertiary mandates are a procurement trigger, not a policy debate.** Saudi Arabia requiring AI literacy in undergraduate education creates curriculum, platform and teacher-capacity demand with an institutional buyer and no ambiguity about whether to proceed. This is the one part of EMEA where the sell is capability rather than compliance.
- 🟢 **Offline-first is the architectural requirement in Sub-Saharan Africa, and the open source shelf can meet it.** Every credible African offering found is offline-capable by design. `Kolibri` (MIT, offline-first) plus a local model via Ollama plus `fsrs-rs` (BSD-3-Clause) for on-device review scheduling is a stack that works without connectivity and keeps learner data on the device — which is also the posture African builders have already chosen for trust reasons.
- **Avoid, or price carefully:** proctoring and emotion-adjacent features. Emotion recognition is banned outright, and exam monitoring is high-risk. ILIAS (GPL-3.0) is the incumbent base in German-speaking markets.

### APAC

**Regulatory posture:** no longer merely fragmented — **APAC now has a binding, horizontal, risk-tiered AI statute that names education explicitly**, and this KB did not hold it until p651.

🔴 **South Korea — the AI Basic Act (Law No. 20676), in force 22 January 2026.** The world's second comprehensive AI statute after the EU AI Act. Its **"high-impact AI" category covers AI used for student assessment in early-childhood, elementary and secondary education** — named in the statutory definition, not inferred from a sector list. Operators must determine whether their system qualifies before deployment (and may request a determination from MSIT), and must make efforts to assess the system's impact on fundamental rights before putting it into a product or service. **MSIT has signalled a grace period of at least one year before administrative fines**, so the enforcement edge falls around **January 2027**, with the interim focused on guidance through a new integrated support centre. A promotion-focused amendment commences 21 July 2026. *(Enactment date 21 January 2025 per the official text; one secondary source says December 2024 — rely on the official text. Grace-period length is reported as "at least one year"; confirm with MSIT before relying on it contractually.)*

🔴 **Vietnam — the dated hook p651 left open is closed, and it names education in a decision, not an inference.** The **Law on Artificial Intelligence (No. 134/2025/QH15)**, passed 10 December 2025, in force **1 March 2026**, sets a three-tier risk framework. The operative instrument is **Decision 33/2026/QD-TTg**, effective **15 August 2026**, which promulgates the list of high-risk AI systems: **46 systems across six sectors, of which education accounts for three.**

The primary education entry covers AI used to **automatically run examinations or assessments, assess learning outcomes, and rank learners** — and it is scoped: it applies **only where the results serve as the official basis** for assessing learning outcomes or ranking learners within the national education system. That scoping clause is the commercially important part. A formative or practice tool falls outside it; the same model wired into the system of record falls inside.

**Transition:** systems already operating before 15 August 2026 have until **1 September 2027** to comply in education, healthcare and finance (other listed sectors: 1 March 2027).

*(Law and decision numbers, dates and the education entry's wording are from law-firm and compliance summaries plus a reproduction of the decision text; the primary Vietnamese text was not read at first hand. Two further entries reported by one commentary — systems that monitor and analyse learner behaviour, and self-study tools generating content from uncontrolled sources — **could not be confirmed against the decision text and are not published here as fact.**)*

**Singapore** relies on governance toolkits rather than a statute: new AI governance guidance covering **generative and agentic** AI, with MAS consulting on AI Risk Management Guidelines. No education-specific rule.

🔴 **A claim about Australia was tested this pass and does not verify.** A widely-repeated summary states that **TEQSA requires all higher education providers to submit institutional action plans addressing generative-AI risks** — which would have been the most education-specific regulatory action in the region. **No such submission mandate was found.** What exists is guidance and a standards hook: TEQSA published *"Assuring quality learning in a gen AI-integrated future"* on **24 June 2026**, maintains a Gen AI Knowledge Hub for providers, staff and students, and frames academic-integrity risk through **Threshold Standard 5.2** rather than a new instrument; prior key documents are a 2024 report on gen AI strategies and a 2025 guide to enacting assessment reform. Australia's posture is therefore unchanged from what this page already says — existing law plus sector guidance — and the contradicting claim is recorded as rejected rather than quietly dropped.

🟢 **Two genuinely procurement-grade Australian assets surfaced while testing that claim**, and they are the kind of thing this page has been declaring absent in APAC: a **Zenodo dataset (October 2026) recording the public student generative-AI disclosure rules of all 220 providers on the TEQSA National Register**, and an **AJET study (July 2026) analysing how 39 universities align with TEQSA's gen-AI principles.** A census of every provider's published rule is exactly the artefact that lets an engagement open with the client's own position already mapped.

**China** regulates by service — Generative AI Regulation (2023), Deep Synthesis (2022), Recommendation Algorithm (2022); companion-service rules effective 15 July 2026; the amended Cybersecurity Law adds the first AI clause (Article 20). **India** has no dedicated AI law and governs via the DPDP Act and 2025 Rules plus voluntary MeitY guidelines; amended IT Rules on **synthetic-content labelling took effect 20 February 2026**. **Japan**'s AI Promotion Act (May 2025) is deliberately non-binding, with a government AI Basic Plan adopted by Cabinet in July 2026. **Australia and Hong Kong** apply existing law and sector guidance rather than a standalone AI act.

**Market:** APAC is the fastest-growing region — roughly **$2.85B in 2026 at a 35.3% CAGR**, about a fifth of global share (market-research secondary sources; directional). **South Korea spent roughly $740M on training teachers to use AI across 2024–2026.** Readiness is uneven: UNESCO notes China and Singapore have established AI-in-education policies while others have none, and adoption lags in rural South Asia and parts of the Pacific.

**Public sentiment (Ipsos Education Monitor 2026, support for banning AI in schools):** South Korea 31%, Japan 29%, Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%. Japan rose from 21% to 29%. Australia and New Zealand record higher support for a ban than the Asian markets.

**🆕 New at p653: essentially nothing, and the leg is recorded as reproduced rather than skipped.**

The APAC search was run and returned **no reading this base did not already hold**: South Korea's AI Basic Act (in force 22 January 2026), Vietnam's binding law and its **1 September 2027** education transition, the ≈$2.85B / 35.3% CAGR market estimate, the Ipsos Education Monitor 2026 ban-support figures (South Korea 31% down to Indonesia 23%), and UNESCO's China-and-Singapore-versus-the-rest readiness split were all already sourced above. The only additions on offer were vendor-named player lists (Google, Microsoft, IBM, Pearson, Byju's, Squirrel AI) from market-research summaries with no primary citation, and a Microsoft announcement of expanded education commitments — **neither is recorded as a finding.**

🔵 **Stated explicitly because silence would look like coverage:** this is a *reproduction*, which is evidence the APAC picture is stable, not evidence it was re-investigated deeply. The genuine APAC gap is unchanged and is a supply gap, not an intelligence gap — APAC produces the overwhelming majority of this KB's agent supply (DeepTutor, OpenMAIC, AI-Shifu, OmniEdu) and almost none of its *regional* demand-side primary sourcing, because the statutes have not been read at first hand.

**Opportunities:**
- **This region is the open source supply side, not just a market.** Both leading permissive education agents originate here — OpenMAIC (Tsinghua, MIT, 42.7k★) and DeepTutor (HKU, Apache-2.0, 55k★). Globant can contribute to and productise these with regional credibility.
- 🟢 **South Korea is the one APAC engagement with a deadline attached, and it is the EMEA playbook in a second jurisdiction.** Student-assessment AI in K-12 is high-impact by statute; the fine window opens around January 2027. Conformity-by-design work for assessment and placement systems — the same offer that sells against the EU's 2 December 2027 date — is sellable in Korea now, against an *earlier* date. A client operating in both markets needs one conformity programme with two jurisdictional profiles, not two programmes.
- **Synthetic-content labelling (India, since 20 Feb 2026) is a concrete build.** AI-generated course material needs provenance labelling — a narrow, dated compliance requirement that is already live.
- 🟢 **Vietnam is the third jurisdiction for the conformity-by-design offer, and it has the sharpest scoping line.** The high-risk trigger is "results serve as the official basis" for assessment or ranking. That makes the architecture decision itself a billable deliverable: keeping an agent demonstrably on the formative side of the system of record is a design and evidence exercise, and the alternative — conformity work on a system of record — is a much larger programme with a **1 September 2027** deadline for anything already running. Clients with existing deployments in Vietnamese education are already inside the transition window.
- 🔵 **Lead Australian conversations with the census, not with a rule.** There is no submission mandate to comply with, so the compliance framing does not land. The 220-provider disclosure-rule dataset and the 39-university alignment study do: they let a proposal state where the client sits relative to every peer before any discovery work is done.
- **Rising public resistance is a positioning signal.** With ban-support climbing in Japan and high in ANZ, transparent, teacher-in-the-loop designs sell better than autonomous ones. Lead with OpenMAIC's visible AI-classmate framing rather than invisible automation.

### LATAM

**Regulatory posture:** the least settled region. Only **Peru** has an enacted AI law. **Brazil**'s EU-inspired bill is the most developed framework in the region (tiered risk, civil liability) but remains pending; a regulatory sandbox launched in 2025. **Mexico** has no horizontal AI law; a February 2026 bill would create a body to classify AI systems by risk. **Chile**'s comprehensive bill is pending (Boletín 16821-19), with the National AI Policy updated in 2024 carrying explicit funding and sectoral mandates.

**Adoption:** usage far ahead of governance — and p651 adds the denominators that were missing.

| Reading | Scope | Source |
|---|---|---|
| **87% use AI in at least one area; only 26% have a formal strategy; 55% have no specific AI budget** | ~200 higher-education institutions across **19 countries** | UNESCO IESALC with UNU-IAS |
| **92% of students and 79% of faculty** actively engaging with AI | LATAM higher education | Digital Education Council, LATAM survey 2026 |
| **53% of school administrators use AI; only 22% say their school has guidelines on its use** | **Brazil**, K-12 | Cetic.br |
| >50% of teachers in Chile and Brazil use AI tools; <10% of institutions have formal guidelines or sufficient capacity | regional | UNESCO |
| **716 AI-related regulatory instruments, rules and legislative proposals across 23 countries and territories** | regional | Universidad de los Andes, 2026 |

🟢 **p652 re-derived the IESALC figures from an independent search and they reproduce**: ~200 higher-education institutions, 19 countries, **87%** using AI in at least one area, **26%** with a formal strategy, and **~9% evaluating what their AI use delivers**. The 9% outcome-evaluation figure is new to this page and is the most damning of the three — it means roughly one institution in eleven can say whether any of this worked. Two further national readings, also new: **75% of public-school teachers in Uruguay** use these tools, and **65% of Brazilian internet users aged 9–17** report using AI. The Uruguayan figure is the highest teacher-adoption number in this KB for any country in any region.

🔵 **Two of those figures look contradictory and are not.** UNESCO's "<10% have formal guidelines" and IESALC's "26% have a formal strategy" measure different objects — an operative guideline document that staff must follow, versus an institutional strategy. Quote them separately and name the scope; a client will notice if they are blended. The pair is also the clearest statement of the regional problem: roughly a quarter of institutions have decided what they want, under a tenth have written down what staff may do, and **more than half have allocated no money at all.** UNESCO launched its **Observatory on AI in Education for Latin America and the Caribbean** on 14 April (regional event in Santiago). A Chilean university reported **194 pedagogical agents across nearly 100 courses serving 4,600+ students** in February 2026 — the most concrete agentic-education deployment found anywhere this pass. Mexico's Public AI Training Center (INFOTEC + TecNM with 14 companies) targets 10,000 AI specialists in 2026 and 25,000/year thereafter. **Tecnológico de Monterrey signed an agreement with UNESCO on AI in education in March 2026** — the region's most visible institutional partner, and a reference account for any peer-institution sell.

**🆕 New at p653:**

| Reading | Scope | Source |
|---|---|---|
| 🔴 **45% of institutions in Latin America and the Caribbean have AI guidance or are developing it, against ~70% across Europe and North America** | regional | UNESCO (secondary) |
| 🟢 **UNESCO launched the Regional Observatory on AI in Education for Latin America and the Caribbean on 14 April 2026 in Santiago, Chile.** Named partners: **CAF, CENIA (Chile), Cetic.br/NIC.br, ECLAC, Fundación Ceibal (Uruguay), Fundación Santillana, Tecnológico de Monterrey, ProFuturo, Universidad del Desarrollo, IRCAI.** A further partnership with Efekta Education Group was announced in October 2026 | regional | UNESCO |
| **UNESCO IESALC's standing recommendations to governments**: bring higher education into national AI strategies, fund it specifically, publish national guidance, and **integrate AI literacy and governance into accreditation and quality assurance** | regional | UNESCO IESALC |

🟢 **The accreditation recommendation is the most actionable item in this section and deserves to be read as a demand signal.** This region's defining problem, already measured above, is that usage runs far ahead of governance — 87% of institutions using AI, 26% with a strategy, 55% with no AI budget. **A governance deliverable with no budget line is a hard sell; the same deliverable attached to accreditation is a compliance obligation with an owner and a deadline.** If IESALC's recommendation lands in any national quality-assurance framework, the LATAM governance-first play in `compose/patterns.md` **P5** stops being a discretionary purchase. Worth monitoring per country, and worth naming in a proposal as the trajectory even before it lands.

🔵 **The named partner list is itself usable intelligence** — it is the shortest available map of who holds convening power on education AI in this region, and `Fundación Ceibal`, `CENIA` and `Tecnológico de Monterrey` are all plausible engagement counterparties or references rather than merely institutions to cite.

**🆕 New at p654 — Brazil's AI sandbox, measured rather than mentioned.** This page has carried
"a regulatory sandbox launched in 2025" for several passes. It is a named instrument with a published
end date, a scoring rubric and a result worth recording:

| Reading | Detail | Source |
|---|---|---|
| **The ANPD's pilot AI-and-data-protection regulatory sandbox runs until December 2026** | Up to three participants, selected under **Edital/Notice 2/2025**. Testing began **March 2026**; the ANPD published a first partial monitoring report in **early July 2026** and held a public consultation on **13 August 2026** setting four themes | ANPD launch notice + monitoring coverage (secondary) |
| 🔴 **A participant scored 45 of 100 on the sandbox's ethics framework — against a stated continuation floor of 50 — and was kept in** | The participant is Synapse (metro route recommendation) | ppc.land (secondary, single source) |
| 🟡 **The participant list does not reconcile across sources** | One list: Synapse, **Prevvine Tecnologia** (STAIDOC, a medical LLM chatbot), **Metatext**. The October 2025 Notice 2/2025 selection list instead names Metatext, Synapse and **IA Greenworld**. The third slot is disputed | two secondary lists, unreconciled |
| **A follow-on sandbox cycle is signalled but undated** | A legal bulletin refers to the regulator moving on to its next cycle; no dates published | TozziniFreire bulletin (secondary) |

🔴 **None of the participants is an education project, and that is the finding.** The sandbox is a
**mechanism** precedent, not an education precedent — it does not weaken this page's standing gap that
Brazil has published no education-sector AI rules. Read correctly it is still the most concrete LATAM
opportunity on this page, for two reasons. First, **it is a closing window**: a December 2026 end date is
seven weeks out, so an engagement that intends to use *this* cycle is already late, and the realistic play
is positioning for the undated next cycle. Second, **the 45-of-100 result is the more durable
intelligence**: a regulator that keeps a participant below its own published floor is telling the market
that this cycle is calibration rather than enforcement. Both facts are secondary-sourced and the
participant list is contradictory, so verify against the ANPD's own site before either goes in front of a
client.

🔴 **Unchanged and still the sharpest asymmetry in this KB:** no LATAM education agent repository has been found in any pass under a usable licence. The one real, LATAM-placed project (`Micel357/Edu-mentor-AI`, Recife, Brazil) has **no grant file**. The region with the widest adoption gap has the thinnest open source supply.

**Opportunities:**
- 🔴 **Qualify on budget before qualifying on need.** **55% of LATAM universities have no specific AI budget** (IESALC). The governance gap is real and the demand is real, but in more than half of these institutions there is no line item to sell into. The practical consequence: lead with a small, fixed-fee governance artefact that a dean can authorise from discretionary funds, and use it to create the budget line for the implementation work — not the reverse. An engagement sized to the need will not close in a majority of this market.
- **The governance gap is the largest single opportunity in this KB.** >50% teacher usage against <10% institutional guidelines is an unmanaged-risk position at national scale. Institutional AI governance frameworks plus the technical controls to enforce them, delivered in Spanish and Portuguese, is a repeatable offering across the region.
- 🟢 **The ~9% outcome-evaluation figure is a product, not just a statistic.** 87% adoption against 9% evaluation means the region's institutions have no instrument for answering their own boards. A measurement and evaluation wrapper — baseline, control, learning-outcome instrumentation, reporting a dean can take upstairs — is small, fixed-fee, authorisable from discretionary funds, and it is the thing that creates the budget line that 55% of these institutions lack. It is also the offer most defensible against this KB's own **T10**: nobody has to believe a vendor's efficacy claim if the engagement's deliverable is the client's own measurement. See `compose/patterns.md` **P5**.
- 🔵 **Uruguay is the highest-adoption teacher population in this KB (75%, public schools) and it is small enough to be a national reference account.** A country-scale proof point in Spanish, with a public-sector buyer and existing teacher uptake, is worth more as a reference than a larger fragmented market. Note also that Uruguay has academic standing in this field: the **RETUYT-INCO** group (Universidad de la República) published on AI-tutor evaluation with lightweight models at the BEA 2025 shared task — a local research partner rather than an imported one.
- **The Chilean 194-agent deployment is a reference architecture.** It proves scaled pedagogical agents work in a LATAM university. That is a sellable case pattern for every peer institution in the region.
- **Moodle and Chamilo are the installed base**, both GPL-3.0 and both reachable with out-of-tree agents over REST. No migration required — the lowest-friction entry in any region.
- 🟢 **Position for the ANPD's next sandbox cycle, not this one.** The pilot closes December 2026. A sandbox place is the cheapest regulatory cover available in this region for a product that does student profiling or automated assessment, and no education project has held one yet — so the slot is uncontested in this vertical. The deliverable that wins it is the governance artefact this section already recommends selling, which means the same small fixed-fee engagement serves both purposes.
- **Low regulatory load is a window, not a permanence.** Brazil's bill will pass in some form. Designs that are already EU-AI-Act-shaped will survive it; expedient ones will need rebuilding.
- Mexico's training-capacity push signals public money moving toward AI skills — adjacent demand for curriculum and platform work.

## Regional comparison

| | North America | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Binding AI-education rules | State-level, patchy; **no Canadian AI Act (AIDA died Jan 2025)** | **Yes — EU AI Act, risk-tiered**; UK light-touch but has a DfE **product safety standard** (Jan 2026) | **Yes, in two jurisdictions — South Korea** (AI Basic Act, education named in the high-impact definition) **and Vietnam** (Decision 33/2026/QD-TTg: education is 3 of 46 high-risk systems) | Mostly pending (Peru only) |
| Nearest enforcement date | No single federal date; state deadlines vary and several 2026 claims do not verify (see above). Canada: none | **High-risk 2 Dec 2027**; Article 50 transparency live since 2 Aug 2026 | **Korea administrative fines ≈ Jan 2027**; **Vietnam education transition 1 Sep 2027**, high-risk list live since 15 Aug 2026; India labelling live since 20 Feb 2026 | — |
| Market size (2026, directional) | largest | Europe ≈ $2.64B; MEA ≈ $0.56B | ≈ $2.85B, **35.3% CAGR — fastest** | growing; **55% of universities have no AI budget** |
| Institutional readiness | Moderate; 60% of teachers use AI, 55% of schools unrestricted | Moderate–high; ~70% have or are developing guidance | Mixed (China, Singapore have policies; much of the region does not) | **Low — 26% have a strategy, <10% have guidelines** |
| Dominant LMS | Canvas, Blackboard | Moodle, ILIAS; **OpenOlat** in German-speaking HE | Mixed | **Moodle, Chamilo** |
| Open source supply | Modest (OATutor); `canvas-mcp` 317★ serves the Canvas-dominant market | 🟢 **Upgraded at p653: the only region that owns a permissive institutional *platform* — `OpenOlat`, Apache-2.0, 449★ / 32,210 commits, `langchain4j` in-tree.** Agent layer still thin (`feedbacksystem` 24★; Moodle bridges cap at 27★) | **Dominant — DeepTutor, OpenMAIC, AI-Shifu, and now the model layer (OmniEdu)** | Real but **licence-nil** (`Edu-mentor-AI`); no LATAM education agent repo found in any pass |
| Primary sell | Compliance + Canvas agents | Conformity by design; Gulf capability builds; **offline-first in Africa** | **Conformity by design (Korea)** + co-development + labelling | **Governance first, small and fixed-fee** |

🔵 **The single most useful shift in this table at p651:** the EMEA conformity-by-design offer is no longer region-specific. South Korea's AI Basic Act names student assessment in the high-impact category and its enforcement edge (≈ January 2027) falls **before** the EU's (2 December 2027). The same engagement shape now has two jurisdictions and two dates, with Korea the earlier one.

🔴 **And the shift at p652 inverts the assumption underneath this whole page: the EU is now the *last* of three binding education-AI deadlines, not the forcing function.** Ordered:

| Date | Jurisdiction | What falls due |
|---|---|---|
| **≈ Jan 2027** | South Korea | Administrative fines become available after MSIT's signalled grace period; student assessment in early-childhood/elementary/secondary education is high-impact by statute |
| **1 Sep 2027** | Vietnam | Compliance deadline for education systems already operating before 15 Aug 2026 (health and finance share the date; other sectors 1 Mar 2027) |
| **2 Dec 2027** | EU | Stand-alone Annex III high-risk obligations, after the Digital Omnibus deferral from 2 Aug 2026 |

Three consequences, and they are not cosmetic. **(1)** A client selling education AI into all three markets needs one conformity programme with three jurisdictional profiles, sequenced to the Korean date — not an EU programme with APAC bolted on. **(2)** Any proposal that frames December 2027 as "the deadline" is eleven months late for a client with Korean exposure. **(3)** The EU deferral bought European clients runway and bought APAC clients nothing, so the regions that looked least regulated on this page a year ago are now the ones with the nearest dates. **The habit of treating EMEA as the compliance region and APAC as the supply region is now wrong in both directions** — APAC supplies the open source *and* has the earliest deadlines.

## 🔴 Declared gaps — searched and not found

- **No education-specific AI regulation found for Brazil, Mexico or Chile.** All three have horizontal AI bills pending; none has published education-sector rules. Searched; genuinely absent, not merely unlocated. 🟢 **p654 strengthens this from an absence to a measurement for Brazil:** the ANPD's pilot AI regulatory sandbox — the country's one operating AI-governance instrument — admitted up to three participants under Notice 2/2025 and **none of them is an education project** (mobility routing, a medical LLM chatbot, and an AI-agent security layer; the third slot is disputed across sources). The gap is not that Brazilian education AI rules are unlocated. It is that the regulator's only live sandbox has no education participant to write them from.
- 🟢 **Partly closed: APAC now has one education-specific binding rule.** South Korea's AI Basic Act names student assessment in early-childhood, elementary and secondary education inside its high-impact definition. The gap as previously stated ("no education-specific AI rules surfaced for China, India or Japan") still holds for those three countries, and the named-player hole in APAC on the demand side is unchanged: the regional player lists available are vendor market-research rankings (Google, Microsoft, IBM, Pearson, Byju's, Squirrel AI), not procurement-grade intelligence.
- 🟢 **Closed at p652: country-level African AI policy.** The gap as previously stated — "country-level education AI regulation for any Sub-Saharan African state" — is resolved into an accurate statement rather than left as silence: **national AI strategies with explicit education commitments exist (Kenya 2025–2030, Nigeria's digital economy strategy), and education-sector rules do not.** South Africa's draft National AI Policy was published 10 April 2026 and withdrawn seventeen days later. The African Union's own timeline puts Phase 1 (2025–2026) at establishing governance structures and national strategies, so the continent is at the strategy stage **by design, on schedule** — this is not a lag to be explained, it is where the roadmap says it should be. Kenya's unwritten AI-literacy framework is a named, unfilled deliverable inside a published strategy. African *open-source supply* remains genuinely absent (p651): builders ship proprietary apps on open weights.
- 🟢 **Closed at p652: the Canadian half of the North America leg**, after three consecutive passes of this page admitting that "North America" meant the United States. Canada now has its own block above: the 4 June 2026 national AI strategy, the National AI Literacy Initiative (1M students, 3,000+ educators), the absence of any AI Act after AIDA died on prorogation in January 2025, and K-12 policy ranging from Quebec's suspension directive to Nova Scotia's nothing. **The leg is hereby re-scoped to the United States and Canada explicitly**, and Mexico is covered under LATAM, which resolves the filing inconsistency this page flagged. 🔴 **Still open: Mexican *education-specific* material.** Mexico appears only through capacity-building and horizontal-bill sources (INFOTEC/TecNM training centre, the February 2026 risk-classification bill); no Mexican education AI rule or adoption survey has surfaced in any pass.
- 🔴 **One claim was tested and rejected rather than published** — the North Carolina SL 2026-41 model-policy dates. Recorded in `intel/measured-unusable.md`. This is the first pass in a long run where a mandated web leg produced a *negative* result worth keeping: the leg's value was in stopping a wrong date from entering the KB, not in adding a right one.
- **Market-size figures were not reconciled to primary research reports.** All are secondary citations of vendor and market-research marketing. p652 adds two more secondary figures without reconciling them either, and they disagree with each other and with this page's existing range: the AI-education market at **~$11.4B in 2026 → $57.25B by 2033** (Coherent Market Insights), against other 2026 compilations citing ~$12.3B for 2026 and $136.79B by 2035. **Europe is quoted at $2.64B (2026) → $8.0B (2030) at a 31.9% CAGR** — the 2030 endpoint and CAGR are new; the 2026 figure reproduces what this page already held. Treat all of these as definitional artefacts, not measurements, and never put two of them in the same sentence.
- 🔴 **Five hosts did not resolve under this session's network policy at p652**, and the claims that depend on them are marked secondary rather than presented as read: `www.unesco.org` and `www.iesalc.unesco.org` (the LATAM IESALC figures — independently re-derived from search, and they reproduce), `www.oecd.org` (the Digital Education Outlook 2026 recommendations, quoted below from search excerpts of the PDF rather than from the PDF), `www.dlapiper.com` (the Canadian strategy analysis), and `huggingface.co` (OmniEdu's weight licence — which is why `agents/top.md` gates that row). This is the second consecutive pass where a network restriction, not a research failure, set the ceiling on first-hand verification for specific claims. It is cheap to fix and worth fixing: allowing `oecd.org`, `unesco.org` and `huggingface.co` would convert several of this KB's load-bearing secondary citations into primary ones.
- 🟢 **A negative result worth keeping, for the second consecutive pass.** p651 rejected the North Carolina SL 2026-41 model-policy dates. p652 rejected the claim that **TEQSA requires Australian higher education providers to submit institutional gen-AI action plans** — it does not; TEQSA publishes guidance and leans on Threshold Standard 5.2. Two passes, two mandated web legs whose value was stopping a wrong claim rather than adding a right one. That is now a pattern rather than an anomaly, and it argues for keeping the regional legs even in passes where they look unproductive: **the regional leg's job is partly adversarial.**
