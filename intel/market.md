---
industry: education
region: Global
updated: 2026-10-21
---

# Education — market map and regional intelligence

Researched **2026-10-21**. Figures are attributed; where a number comes from a vendor
blog or a commercial research summary rather than a primary source, it says so. The
regional sections below are deliberately symmetric: a North America or EMEA
engagement should be as well served by this file as a LATAM one.

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

---

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
[Educativa — AI trends in education 2026](https://www.educativa.com/en/blog/ai-trends-in-education-for-2026/)
