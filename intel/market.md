---
industry: education
region: Global
updated: 2026-10-11
---

# Education — market map and opportunities

**Pass 130, 2026-10-11.** Full rewrite. Figures below are attributed to the kind of source they
came from, because the spread between sources is itself the finding.

## Market size — the honest range

Estimates for the **2026 global AI-in-education market** collected this pass span
**~$6.4B to ~$11.4B**. That is a 1.8× spread for the current year, which means no single number
should be quoted to a client without its source.

| estimate for 2026 | forecast | implied CAGR | source type |
|---|---|---|---|
| $10.6B | → $42.48B by 2030 | 41.5% | market-research firm |
| $10.4B | → $32.27B by 2030 | 31.2% | market-research firm |
| ~$9.58B | → ~$136.79B by 2035 | — (aggressive long-range) | market-research firm |
| ~$11B | — | — | market-research blog |
| ~$6.4B (low end of range found) | — | — | market-research aggregator |
| $4.09B (**higher education only**) | → $13.46B by 2030 | 34.7% | market-research firm |

**How to use this:** quote the *range and the disagreement*, and anchor commercial conversations on
the segment figure (higher ed, ~$4.09B in 2026) rather than the headline, which bundles K-12,
higher ed, corporate training and tooling under inconsistent definitions.

Regional share, as reported: **North America ~36%** (largest), **Asia-Pacific fastest-growing at
~35.3% CAGR**.

## The structural fact of this market

Adoption by individuals has outrun institutional governance, and the gap is where the work is:

- **88%** of students worldwide report using generative AI; **95%** of UK undergraduates.
- **60%** of US K-12 teachers used AI tools in the 2024-25 school year; **32%** weekly.
- **18%** of US teachers have a written policy telling them how.
- An IDB review of **193** AI-in-education initiatives in Latin America found **59%** used
  generative AI.

Students and teachers are already using these tools; institutions have neither policy, procurement,
nor audit trail. **The sellable work is governance, integration and evidence — not another chatbot.**

## Key players

- **Platforms (the installed base):** Instructure/Canvas (dominant in North American higher ed),
  Moodle (largest global deployment, HQ in Perth), Open edX / Axim Collaborative, Blackboard and
  D2L (proprietary, significant higher-ed share, almost no open-source connectors), Google
  Classroom, Microsoft (Education AI Toolkit updated April 2026 with agentic features for
  institutions).
- **Open-source agent supply:** concentrated and thin — `HKUDS/DeepTutor` (41k★, Apache-2.0) is
  the only education-specific agent with real scale; everything else on the shelf is under 1k stars.
- **Institutional/multilateral actors who shape procurement:** UNESCO (regional AI-in-education
  observatory for LAC; OECD's 2026 Digital Education Outlook argues for purpose-built educational
  AI over general-purpose tools), IDB, Google.org (AI-literacy funding across nine LATAM
  countries), teachers' unions (NEA, AFT, CTA have all issued classroom AI guidance).

## Opportunities by region

### North America

- **Market position:** largest share (~36%), reported at ~$3.68B in 2026 by one tracker. Canvas is
  the platform of record in higher ed, and it has the best connector ecosystem — the MCP work is
  largely done, so engagements start further along.
- **The binding constraint is state-by-state policy, and it is now mandatory, not advisory.**
  134 AI-in-education bills were introduced across 31 states in 2026. **Ohio requires every K-12
  district to adopt a formal AI use policy by 1 July 2026** — a hard date with no accompanying
  capacity. California AB 1159 bars using student data to train models. Oklahoma and Maryland
  require human oversight and bar AI from high-stakes decisions about students. More than 30 states
  have guidance documents. Federally, the K-12 AI Literacy and Readiness Act (H.R. 8747) advanced
  from committee on 21 July 2026.
- **Opportunity:** *policy-to-implementation*. A district with a mandated policy and no technical
  means to enforce it needs data-flow inventory, a model-routing layer that can prove student data
  never reached a training endpoint, human-in-the-loop gates on anything high-stakes, and an audit
  log a board can read. Sell the compliance artefact, deliver the platform underneath it. Build on
  the Canvas MCP connectors plus `tutor-mcp` for auditable pedagogical decisions.
- **Second opportunity:** the AI-literacy curriculum funding line that H.R. 8747 would open, paired
  with `GarethManning/education-agent-skills` as a content base (licence review required).

### EMEA

- **The regulatory clock moved, and that is the single most important EMEA fact this pass.**
  High-risk obligations for Annex III education use cases (admissions, grading, proctoring) were
  **postponed to 2 December 2027** under the Digital Omnibus on AI, approved by the European
  Parliament in June 2026 — but **the Council had not yet formally adopted the text** as of this
  pass. Treat the delay as politically agreed, not final.
- **What already binds, regardless of the delay:** emotion recognition in education has been
  **prohibited since 2 February 2025**; **AI literacy duties (Article 4) have applied since
  February 2025**; public schools face a fundamental-rights impact assessment.
- **Adoption is deliberately slow:** no generative AI tool has been approved for system-wide use in
  the European Schools network, and the approval procedure is still being written.
- **Opportunity:** the delay to December 2027 is a *sales window, not a reprieve* — institutions
  that start in 2026 can build conformity in rather than retrofit it. Concretely: AI inventory and
  classification against Annex III, vendor-contract review, AI-literacy programmes that discharge
  an obligation already in force, and architecture that keeps grading and admissions decisions
  human-made by construction. **Avoid emotion recognition entirely** — it is already illegal here,
  and products built elsewhere ship it.
- **Platform reality:** EMEA procurement runs on ILIAS, OpenOLAT, Chamilo and Moodle far more than
  on Canvas, and all four have essentially no AI-on-top. Standards and accessibility compliance are
  scored in tenders. Richie (MIT, France) is proven at national scale for the public-facing layer.

### APAC

- **Fastest-growing region (~35.3% CAGR), and the only one where curriculum mandates are driving
  demand from the top down.** China made AI a compulsory subject from age six as of September 2025.
  **India makes AI and computational thinking mandatory from Class 3 starting in the 2026-27
  academic year**, across government and private schools.
- **Regulation is real and heterogeneous — one compliance posture will not travel:** South Korea's
  **AI Basic Act took effect 22 January 2026**; China has six binding AI regulations including
  content-labelling and Cybersecurity Law amendments effective January 2026; India signalled in
  July 2026 that it may pursue dedicated legislation and already requires labels on AI-generated
  content; Japan's AI Promotion Act is light-touch, with a second AI Basic Plan approved by Cabinet
  on 14 July 2026; **Vietnam's Decision 33/2026/QD-TTg explicitly names education — including
  automated assessment and behavioural monitoring — as high-risk.**
- **Opportunity:** teacher-capacity tooling at national scale. A Class-3-onward AI mandate in India
  requires curriculum, teacher training and assessment at a volume no vendor can staff manually —
  this is a content-generation and teacher-support engagement, and `satvik314/educhain` (MIT) plus
  `GarethManning/education-agent-skills` are the closest existing bases. Supply-side advantage:
  APAC-origin open source is unusually strong here — `HKUDS/DeepTutor` (Apache-2.0, 41k★),
  `frappe/lms`, `openeducat_erp`, and Moodle HQ itself.
- **Public attitudes are a real constraint:** support for *banning* AI in schools ranges from 23%
  (Indonesia) to 31% (South Korea), with India 26% and Japan 29% (Ipsos Education Monitor 2026).
  Roughly a quarter to a third of the public wants these tools out of classrooms.

### LATAM

- **Adoption is ahead of governance, more starkly than anywhere else.** UNESCO IESALC reports
  widespread AI adoption across higher education in Latin America and the Caribbean with governance
  lagging. The IDB's review of 193 regional initiatives found 59% using generative AI. In Brazil,
  generative AI reportedly reaches 43% of teachers and 58% at high-school level (secondary source —
  verify before quoting).
- **Regulation is pending almost everywhere, and education-specific rules are essentially absent.**
  Brazil's PL 2338/2023 is advanced but not enacted. Mexico's AI amendments to date are in
  copyright, labour and audiovisual law — **not education**. Brazil, Argentina, Chile, Colombia and
  Costa Rica are each advancing their own frameworks. There is no regional instrument.
- **Capital and institutional momentum are real:** HolonIQ's 2026 LATAM EdTech 100 shows AI-native
  positioning quadrupling since 2020 and the cohort leaning toward instructional support rather
  than consumer tutoring; Brazil is ~45% of the regional cohort. Google.org is funding AI literacy
  across Argentina, Brazil, Chile, Colombia, the Dominican Republic, El Salvador, Mexico, Peru and
  Uruguay, targeting 1.25M students by 2028. UNESCO launched a regional AI-in-education observatory
  and, in August 2026, a pilot with CONALEP and DGETI in Mexico.
- **Opportunity:** be the governance layer that regulators have not yet imposed. Institutions
  adopting at speed with no legal framework will face one within the engagement's lifetime — build
  for Brazil's PL 2338 shape now. Second, **offline and low-bandwidth delivery is a first-class
  requirement here, not an edge case**: Kolibri (MIT, offline-first) plus a small local model is a
  differentiated, legally clean offer. Third, **Blackboard and Chamilo matter in this region** and
  are unserved — `campus-cli` (ISC, Peru) shows demand with an 11-star answer.
- **Supply-side gap, stated plainly:** LATAM-origin open-source education AI is nearly nonexistent.
  One repository (`alejooroncoy/campus-cli`, 11★) was found this pass. Globant's regional position
  is a genuine advantage precisely because nothing is being built locally.

### Global / unplaced

- Open-source supply is **not** regionally distributed in any useful way: one Apache-2.0 agent at
  41k stars (APAC-origin) and a long tail under 1k. Most agent repos carry **no location evidence at
  all** — 11 of the 17 agent rows in `agents/top.md` are marked unplaced rather than guessed.
- The **absent benchmark** is global: nothing open source measures whether a tutoring agent improves
  learning outcomes. Every engagement must bring its own evaluation harness, and the client that
  gets one is buying evidence no competitor can show.

## Declared gaps in this market picture

- **Africa and the Middle East are inside "EMEA" here but are not covered by it.** The regional
  evidence found was overwhelmingly EU-specific (AI Act, European Schools). No Gulf, African or
  Israeli education-AI market or regulatory data surfaced this pass. This is a real blind spot in
  a closed five-value vocabulary, not a finding of absence.
- **No reliable open-source market-share data** for which LMS actually runs where, by region. The
  platform-share claims above come from vendor and roundup sources.
- **The 2026 market-size spread (~$6.4B–$11.4B) was not resolvable** against primary sources from
  this runner; all figures are market-research firms' own.
