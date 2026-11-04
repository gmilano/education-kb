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

**Opportunities:**
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

**Opportunities:**
- **The December 2027 window is the commercial story.** Clients have roughly 13 months of runway to get high-risk systems conformant. Conformity-by-design engagements for admissions and assessment scoring are sellable now and have a deadline attached — the strongest forcing function in any region.
- **Transparency is live today.** Article 50 compliance for existing chatbots is immediate, small, and a clean door-opener into larger work.
- **Data-residency tutoring.** Self-hosted DeepTutor or Open TutorAI CE with local models via Ollama keeps learner data in-jurisdiction — the architecture EMEA public education actually buys.
- 🟢 **Gulf tertiary mandates are a procurement trigger, not a policy debate.** Saudi Arabia requiring AI literacy in undergraduate education creates curriculum, platform and teacher-capacity demand with an institutional buyer and no ambiguity about whether to proceed. This is the one part of EMEA where the sell is capability rather than compliance.
- 🟢 **Offline-first is the architectural requirement in Sub-Saharan Africa, and the open source shelf can meet it.** Every credible African offering found is offline-capable by design. `Kolibri` (MIT, offline-first) plus a local model via Ollama plus `fsrs-rs` (BSD-3-Clause) for on-device review scheduling is a stack that works without connectivity and keeps learner data on the device — which is also the posture African builders have already chosen for trust reasons.
- **Avoid, or price carefully:** proctoring and emotion-adjacent features. Emotion recognition is banned outright, and exam monitoring is high-risk. ILIAS (GPL-3.0) is the incumbent base in German-speaking markets.

### APAC

**Regulatory posture:** no longer merely fragmented — **APAC now has a binding, horizontal, risk-tiered AI statute that names education explicitly**, and this KB did not hold it until p651.

🔴 **South Korea — the AI Basic Act (Law No. 20676), in force 22 January 2026.** The world's second comprehensive AI statute after the EU AI Act. Its **"high-impact AI" category covers AI used for student assessment in early-childhood, elementary and secondary education** — named in the statutory definition, not inferred from a sector list. Operators must determine whether their system qualifies before deployment (and may request a determination from MSIT), and must make efforts to assess the system's impact on fundamental rights before putting it into a product or service. **MSIT has signalled a grace period of at least one year before administrative fines**, so the enforcement edge falls around **January 2027**, with the interim focused on guidance through a new integrated support centre. A promotion-focused amendment commences 21 July 2026. *(Enactment date 21 January 2025 per the official text; one secondary source says December 2024 — rely on the official text. Grace-period length is reported as "at least one year"; confirm with MSIT before relying on it contractually.)*

**Vietnam — Law on Artificial Intelligence**, passed 10 December 2025, in force **1 March 2026**. Not read at first hand this pass; recorded as a dated hook to verify.

**China** regulates by service — Generative AI Regulation (2023), Deep Synthesis (2022), Recommendation Algorithm (2022); companion-service rules effective 15 July 2026; the amended Cybersecurity Law adds the first AI clause (Article 20). **India** has no dedicated AI law and governs via the DPDP Act and 2025 Rules plus voluntary MeitY guidelines; amended IT Rules on **synthetic-content labelling took effect 20 February 2026**. **Japan**'s AI Promotion Act (May 2025) is deliberately non-binding, with a government AI Basic Plan adopted by Cabinet in July 2026. **Australia and Hong Kong** apply existing law and sector guidance rather than a standalone AI act.

**Market:** APAC is the fastest-growing region — roughly **$2.85B in 2026 at a 35.3% CAGR**, about a fifth of global share (market-research secondary sources; directional). **South Korea spent roughly $740M on training teachers to use AI across 2024–2026.** Readiness is uneven: UNESCO notes China and Singapore have established AI-in-education policies while others have none, and adoption lags in rural South Asia and parts of the Pacific.

**Public sentiment (Ipsos Education Monitor 2026, support for banning AI in schools):** South Korea 31%, Japan 29%, Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%. Japan rose from 21% to 29%. Australia and New Zealand record higher support for a ban than the Asian markets.

**Opportunities:**
- **This region is the open source supply side, not just a market.** Both leading permissive education agents originate here — OpenMAIC (Tsinghua, MIT, 42.7k★) and DeepTutor (HKU, Apache-2.0, 55k★). Globant can contribute to and productise these with regional credibility.
- 🟢 **South Korea is the one APAC engagement with a deadline attached, and it is the EMEA playbook in a second jurisdiction.** Student-assessment AI in K-12 is high-impact by statute; the fine window opens around January 2027. Conformity-by-design work for assessment and placement systems — the same offer that sells against the EU's 2 December 2027 date — is sellable in Korea now, against an *earlier* date. A client operating in both markets needs one conformity programme with two jurisdictional profiles, not two programmes.
- **Synthetic-content labelling (India, since 20 Feb 2026) is a concrete build.** AI-generated course material needs provenance labelling — a narrow, dated compliance requirement that is already live.
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

🔵 **Two of those figures look contradictory and are not.** UNESCO's "<10% have formal guidelines" and IESALC's "26% have a formal strategy" measure different objects — an operative guideline document that staff must follow, versus an institutional strategy. Quote them separately and name the scope; a client will notice if they are blended. The pair is also the clearest statement of the regional problem: roughly a quarter of institutions have decided what they want, under a tenth have written down what staff may do, and **more than half have allocated no money at all.** UNESCO launched its **Observatory on AI in Education for Latin America and the Caribbean** on 14 April (regional event in Santiago). A Chilean university reported **194 pedagogical agents across nearly 100 courses serving 4,600+ students** in February 2026 — the most concrete agentic-education deployment found anywhere this pass. Mexico's Public AI Training Center (INFOTEC + TecNM with 14 companies) targets 10,000 AI specialists in 2026 and 25,000/year thereafter. **Tecnológico de Monterrey signed an agreement with UNESCO on AI in education in March 2026** — the region's most visible institutional partner, and a reference account for any peer-institution sell.

**Opportunities:**
- 🔴 **Qualify on budget before qualifying on need.** **55% of LATAM universities have no specific AI budget** (IESALC). The governance gap is real and the demand is real, but in more than half of these institutions there is no line item to sell into. The practical consequence: lead with a small, fixed-fee governance artefact that a dean can authorise from discretionary funds, and use it to create the budget line for the implementation work — not the reverse. An engagement sized to the need will not close in a majority of this market.
- **The governance gap is the largest single opportunity in this KB.** >50% teacher usage against <10% institutional guidelines is an unmanaged-risk position at national scale. Institutional AI governance frameworks plus the technical controls to enforce them, delivered in Spanish and Portuguese, is a repeatable offering across the region.
- **The Chilean 194-agent deployment is a reference architecture.** It proves scaled pedagogical agents work in a LATAM university. That is a sellable case pattern for every peer institution in the region.
- **Moodle and Chamilo are the installed base**, both GPL-3.0 and both reachable with out-of-tree agents over REST. No migration required — the lowest-friction entry in any region.
- **Low regulatory load is a window, not a permanence.** Brazil's bill will pass in some form. Designs that are already EU-AI-Act-shaped will survive it; expedient ones will need rebuilding.
- Mexico's training-capacity push signals public money moving toward AI skills — adjacent demand for curriculum and platform work.

## Regional comparison

| | North America | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Binding AI-education rules | State-level, patchy | **Yes — EU AI Act, risk-tiered** | **Yes — South Korea AI Basic Act, education named in the high-impact definition** | Mostly pending (Peru only) |
| Nearest enforcement date | No single federal date; state deadlines vary and several 2026 claims do not verify (see above) | **High-risk 2 Dec 2027**; Article 50 transparency live since 2 Aug 2026 | **Korea administrative fines ≈ Jan 2027** (MSIT grace period); India labelling live since 20 Feb 2026; Vietnam in force 1 Mar 2026 | — |
| Market size (2026, directional) | largest | Europe ≈ $2.64B; MEA ≈ $0.56B | ≈ $2.85B, **35.3% CAGR — fastest** | growing; **55% of universities have no AI budget** |
| Institutional readiness | Moderate; 60% of teachers use AI, 55% of schools unrestricted | Moderate–high; ~70% have or are developing guidance | Mixed (China, Singapore have policies; much of the region does not) | **Low — 26% have a strategy, <10% have guidelines** |
| Dominant LMS | Canvas, Blackboard | Moodle, ILIAS | Mixed | **Moodle, Chamilo** |
| Open source supply | Modest (OATutor) | Modest (`feedbacksystem`, 24★) | **Dominant — DeepTutor, OpenMAIC, AI-Shifu** | Real but **licence-nil** (`Edu-mentor-AI`) |
| Primary sell | Compliance + Canvas agents | Conformity by design; Gulf capability builds; **offline-first in Africa** | **Conformity by design (Korea)** + co-development + labelling | **Governance first, small and fixed-fee** |

🔵 **The single most useful shift in this table at p651:** the EMEA conformity-by-design offer is no longer region-specific. South Korea's AI Basic Act names student assessment in the high-impact category and its enforcement edge (≈ January 2027) falls **before** the EU's (2 December 2027). The same engagement shape now has two jurisdictions and two dates, with Korea the earlier one.

## 🔴 Declared gaps — searched and not found

- **No education-specific AI regulation found for Brazil, Mexico or Chile.** All three have horizontal AI bills pending; none has published education-sector rules. Searched; genuinely absent, not merely unlocated.
- 🟢 **Partly closed: APAC now has one education-specific binding rule.** South Korea's AI Basic Act names student assessment in early-childhood, elementary and secondary education inside its high-impact definition. The gap as previously stated ("no education-specific AI rules surfaced for China, India or Japan") still holds for those three countries, and the named-player hole in APAC on the demand side is unchanged: the regional player lists available are vendor market-research rankings (Google, Microsoft, IBM, Pearson, Byju's, Squirrel AI), not procurement-grade intelligence.
- 🟢 **Partly closed: the Africa and Middle East leg returned material for the first time**, and the remaining gap is now located rather than merely declared — Gulf policy and African demand are documented, African *open-source supply* is genuinely absent because builders there ship proprietary apps on open weights. The thing still missing is **country-level education AI regulation for any Sub-Saharan African state**; the African Union's CESA 16-25 is a continental strategy, not a rule.
- **No Canadian or Mexican material surfaced in the North America leg** — a third consecutive pass where that leg returned almost entirely US sources. "North America" on this page means the United States, stated rather than hidden. Mexico appears only through LATAM-framed sources (the INFOTEC/TecNM training centre, the February 2026 risk-classification bill), which is a filing inconsistency worth resolving: Mexico is being covered as LATAM, so the North America leg should be re-scoped to the US and Canada explicitly.
- 🔴 **One claim was tested and rejected rather than published** — the North Carolina SL 2026-41 model-policy dates. Recorded in `intel/measured-unusable.md`. This is the first pass in a long run where a mandated web leg produced a *negative* result worth keeping: the leg's value was in stopping a wrong date from entering the KB, not in adding a right one.
- **Market-size figures were not reconciled to primary research reports.** All are secondary citations of vendor and market-research marketing.
