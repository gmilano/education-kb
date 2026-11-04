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
| AI in Education (global) | $11.4B → $57.2B, 25.9% CAGR | 2026–2030 | Grand View Research (carried, not re-verified) |

**These do not reconcile**, and the disagreement is informative rather than noise: "AI tutors" ($3.6B) and "AI-powered education tools" (>$17B) differ by roughly 5× because one counts a product category and the other counts every tool with an AI feature. Do not quote a single market size to a client without naming the scope. Treat the AI-tutor figure as the addressable one for tutoring engagements.

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
| **Squirrel AI** | Commercial (APAC) | Adaptive learning at scale in China | Closed, regionally bound | Competitive reference for APAC adaptive engagements |

## Opportunities by region

### North America

**Regulatory posture:** heavy state-level legislative activity, binding rules still uncommon. More than 134 bills across 31 states addressed AI in K-12 and higher education in the 2026 session (MultiState / FutureEd tracking). Enacted examples: **Idaho SB 1227** (statewide framework, local policies, AI-literacy standards, data-privacy requirements, and an explicit bar on AI replacing human teachers); **Maryland SB 720** (statewide guidance, district AI coordinators, the Maryland AI Education Collaborative); **Ohio** (districts required to adopt AI policies by 1 July 2026, but the statute is near-silent on content and names no enforcement mechanism); **Florida** (State Board approved AI rules for K-12 and the 28 state colleges). Federally, the K-12 AI Literacy and Readiness Act of 2026 advanced out of the House Education and Workforce Committee, and a 2026 federal grant rule prioritises AI literacy.

**Adoption:** the most mature market and the most policy-constrained. 92% university student usage against institutions that mostly lack policy.

**Opportunities:**
- **Policy-to-implementation gap as a service.** Ohio-style mandates require a policy with no guidance on content, and Maryland requires a district AI coordinator role that districts have no one to fill. Globant can productise the compliance artefact *plus* the technical controls behind it, repeatable across districts.
- **Canvas-first agent pilots.** Canvas dominates North American HE. `canvas-mcp` (MIT, 317★) reaches real course data with no migration — the shortest credible path to a funded pilot.
- **"No AI replacing teachers" as a design constraint, not an obstacle.** Idaho's bar makes teacher-augmentation framing legally safer than autonomy. `Instructional Agents` (MIT) automates course *preparation* — exactly the defensible side of that line.
- OATutor (MIT, UC Berkeley) carries domestic academic provenance, which matters in public procurement here.

### EMEA

**Regulatory posture:** the most binding regime in the world, and the timeline just moved. The **Digital Omnibus (Regulation (EU) 2026/1744)** deferred high-risk obligations for stand-alone education AI from 2 August 2026 to **2 December 2027**. Guides still citing August 2026 are out of date. High-risk covers **admissions, learning-outcome evaluation, student level placement, and exam/behaviour monitoring**. **Article 50 transparency duties apply from 2 August 2026** — a school running a student-facing chatbot owes disclosure *now*. **Emotion recognition in schools has been prohibited since February 2025.** Article 4's AI-literacy duty was softened from "ensuring a level of AI literacy" to "taking measures". Schools are **deployers** under the Act.

**Opportunities:**
- **The December 2027 window is the commercial story.** Clients have roughly 13 months of runway to get high-risk systems conformant. Conformity-by-design engagements for admissions and assessment scoring are sellable now and have a deadline attached — the strongest forcing function in any region.
- **Transparency is live today.** Article 50 compliance for existing chatbots is immediate, small, and a clean door-opener into larger work.
- **Data-residency tutoring.** Self-hosted DeepTutor or Open TutorAI CE with local models via Ollama keeps learner data in-jurisdiction — the architecture EMEA public education actually buys.
- **Avoid, or price carefully:** proctoring and emotion-adjacent features. Emotion recognition is banned outright, and exam monitoring is high-risk. ILIAS (GPL-3.0) is the incumbent base in German-speaking markets.

### APAC

**Regulatory posture:** fragmented and service-specific rather than horizontal. **China** regulates by service — Generative AI Regulation (2023), Deep Synthesis (2022), Recommendation Algorithm (2022); companion-service rules effective 15 July 2026; the amended Cybersecurity Law adds the first AI clause (Article 20). **India** has no dedicated AI law and governs via the DPDP Act and 2025 Rules plus voluntary MeitY guidelines; amended IT Rules on **synthetic-content labelling take effect 20 February 2026**. **Japan**'s AI Promotion Act (May 2025) is deliberately non-binding, with a government AI Basic Plan adopted by Cabinet in July 2026.

**Public sentiment (Ipsos Education Monitor 2026, support for banning AI in schools):** South Korea 31%, Japan 29%, Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%. Japan rose from 21% to 29%. Australia and New Zealand record higher support for a ban than the Asian markets.

**Opportunities:**
- **This region is the open source supply side, not just a market.** Both leading permissive education agents originate here — OpenMAIC (Tsinghua, MIT, 42.7k★) and DeepTutor (HKU, Apache-2.0, 55k★). Globant can contribute to and productise these with regional credibility.
- **Synthetic-content labelling (India, from 20 Feb 2026) is a concrete build.** AI-generated course material needs provenance labelling — a narrow, dated compliance requirement.
- **Rising public resistance is a positioning signal.** With ban-support climbing in Japan and high in ANZ, transparent, teacher-in-the-loop designs sell better than autonomous ones. Lead with OpenMAIC's visible AI-classmate framing rather than invisible automation.

### LATAM

**Regulatory posture:** the least settled region. Only **Peru** has an enacted AI law. **Brazil**'s EU-inspired bill is the most developed framework in the region (tiered risk, civil liability) but remains pending; a regulatory sandbox launched in 2025. **Mexico** has no horizontal AI law; a February 2026 bill would create a body to classify AI systems by risk. **Chile**'s comprehensive bill is pending (Boletín 16821-19), with the National AI Policy updated in 2024 carrying explicit funding and sectoral mandates.

**Adoption:** usage far ahead of governance. UNESCO reports **more than half of teachers in Chile and Brazil already use AI tools, while fewer than 10% of regional institutions have formal guidelines** or the capacity to apply them. UNESCO launched its **Observatory on AI in Education for Latin America and the Caribbean** on 14 April (regional event in Santiago). A Chilean university reported **194 pedagogical agents across nearly 100 courses serving 4,600+ students** in February 2026 — the most concrete agentic-education deployment found anywhere this pass. Mexico's Public AI Training Center (INFOTEC + TecNM with 14 companies) targets 10,000 AI specialists in 2026 and 25,000/year thereafter.

**Opportunities:**
- **The governance gap is the largest single opportunity in this KB.** >50% teacher usage against <10% institutional guidelines is an unmanaged-risk position at national scale. Institutional AI governance frameworks plus the technical controls to enforce them, delivered in Spanish and Portuguese, is a repeatable offering across the region.
- **The Chilean 194-agent deployment is a reference architecture.** It proves scaled pedagogical agents work in a LATAM university. That is a sellable case pattern for every peer institution in the region.
- **Moodle and Chamilo are the installed base**, both GPL-3.0 and both reachable with out-of-tree agents over REST. No migration required — the lowest-friction entry in any region.
- **Low regulatory load is a window, not a permanence.** Brazil's bill will pass in some form. Designs that are already EU-AI-Act-shaped will survive it; expedient ones will need rebuilding.
- Mexico's training-capacity push signals public money moving toward AI skills — adjacent demand for curriculum and platform work.

## Regional comparison

| | North America | EMEA | APAC | LATAM |
|---|---|---|---|---|
| Binding AI-education rules | State-level, patchy | **Yes — strongest** | Service-specific | Mostly pending (Peru only) |
| Key date | Ohio policies due 1 Jul 2026 | **High-risk 2 Dec 2027**; transparency 2 Aug 2026 | India labelling 20 Feb 2026 | — |
| Institutional readiness | Moderate | Moderate–high | Mixed | **Low (<10% have guidelines)** |
| Dominant LMS | Canvas, Blackboard | Moodle, ILIAS | Mixed | **Moodle, Chamilo** |
| Primary sell | Compliance + Canvas agents | Conformity by design | Co-development + labelling | **Governance + scaled tutoring** |

## 🔴 Declared gaps — searched and not found

- **No education-specific AI regulation found for Brazil, Mexico or Chile.** All three have horizontal AI bills pending; none has published education-sector rules. Searched; genuinely absent, not merely unlocated.
- **No named edtech players or education-specific AI rules surfaced for China, India or Japan**, despite regulatory material being available. The APAC player map is a real hole on the demand side, even though APAC dominates the open source supply side.
- **No Canadian or Mexican material surfaced in the North America leg** — that leg returned almost entirely US sources. "North America" on this page currently means the United States, and that limitation is stated rather than hidden.
- **Market-size figures were not reconciled to primary research reports.** All are secondary citations of vendor and market-research marketing.
