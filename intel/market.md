---
industry: education
region: Global
updated: 2026-10-25
---

# 🗺️ Market map — Education

> Key players, market size and opportunities **placed by region**. Regional legs are run
> every pass and a nil result is written down as a nil, because silence reads exactly like
> coverage.

## 🆕 `p430` · 2026-10-25 — **Four regional legs, four returned material, no nil.** 🟢 All four regulatory postures re-read and dated; the LATAM governance gap (87% adoption / 26% strategy) is confirmed as the strongest single number in the file. 🔴 This shelf carried **12** `## Opportunities by region` blocks, eleven of them marked SUPERSEDED — the task fixes **one**. The eleven are consolidated into the single current block below; every one of them remains in `git log`.

🔵 **Structural change, stated plainly:** the per-pass narrative that opened this file now
lives in `intel/trends.md` and the append-only trending shelves. This file leads with the
market map, which is what an engagement reads.

## Market size — use the range, never a single figure

| Segment | 2026 | Horizon | CAGR | Source class |
|---|---|---|---|---|
| AI in Education (global) | **$6.9B – $11.4B** | $41B – $57B by 2030–2033 | 26% – 43% | Multiple market-research firms, mutually inconsistent |
| North America share | ~**36%** of global, ≈$3.68B | — | — | Aggregator stats page |
| e-Learning (global, all tech) | ~$250B | ~$450B | ~15% | Multiple |

🔴 **Never quote a single figure.** The spread between reputable firms is a factor of ~1.7
on today's size and ~1.4 on the horizon. Quote the range and name it as a range; a pitch
that cites one number is citing one vendor's model. Market-research education forecasts are
systematically optimistic — treat the low end as the planning number.

## The one number that should shape every pitch

**87% of Latin American higher-education institutions use AI in at least one area, and
26% have a formal AI strategy** (UNESCO IESALC, 200 institutions across 19 countries).
In Brazilian schools, **53% of administrators use AI and 22% work under any school
guideline** (Cetic.br).

That gap — adoption far ahead of governance — is the engagement. The buyer does not need
to be persuaded to adopt AI; they have already adopted it, without a policy, an audit
trail, or a human-in-the-loop story. **Globant's sellable unit in education is governed
adoption, not adoption.** It is also the one thing the copyleft platform tier cannot
supply and a permissive agent layer can.

## Opportunities by region

### North America

**Regulatory posture — restrictive on autonomy, permissive on assistance.** 134 AI-in-education
bills across 31 states in the 2026 session, concentrated on student-data privacy, classroom
use limits and curriculum. California **AB 1159** bars using student data to train AI models.
Oklahoma and Maryland require human oversight and **prohibit AI as the sole basis for
high-stakes decisions** about a student. Charleston County extends that to discipline,
placement and special-education determination. The federal **K-12 AI Literacy and Readiness
Act of 2026 (H.R. 8747)** advanced out of committee on 21 July 2026. Districts add their own
layer: Katy ISD bans generative chatbots for K-6 with scaffolded access to grade 12.
**Canada** launched *AI for All* on 4 June 2026 — national AI literacy, watermarking of
AI-generated content, and a Canada Trusted AI Certification — direction-setting, not yet law.

**Demand signal.** 60% of US K-12 teachers used AI tools in the 2024-25 school year, 32% at
least weekly. Largest regional market share (~36%).

**Where Globant wins.** The binding constraint is *decision autonomy*, not capability. Every
one of these rules is satisfied by the same architectural move: an agent that **drafts and a
human that signs**. [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp)
(MIT) already produces a draft-for-review **by default** — it is the cheapest compliant
starting point on the shelf, and it is Canvas-native, which is the dominant NA LMS.
Pair with [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT, UC Berkeley) where a
district wants an auditable, non-LLM knowledge model behind the tutoring claim.

🔴 **Gap:** the institutional-agent supply measured on these shelves remains largely
non-US; the NA opportunity is in **integration and governance**, not in sourcing NA-built
components.

### EMEA

**Regulatory posture — the most specific in the world, and the deadline just moved.**
The 2026 Digital Omnibus, **Regulation (EU) 2026/1744**, pushed the high-risk obligation for
stand-alone education AI — **grading, admissions, exam proctoring** — from 2 August 2026 to
**2 December 2027**; systems embedded in Annex I regulated products get until 2 August 2028.

🔴 **Do not read the delay as a reprieve.** Three things bite now:
- **Article 50 transparency** applies from **2 August 2026**: disclose AI interaction, mark
  synthetic audio/image/video/text in machine-readable form.
- **Emotion recognition in educational institutions is prohibited outright** since
  2 February 2025 (narrow medical/safety exception). This kills a whole category of
  engagement-detection and proctoring product in the EU.
- **Article 4 AI literacy** has applied since February 2025; softened on 27 July 2026 to
  *taking measures* to support staff skills rather than *ensuring* a level — no mandatory
  hours, no certification.

The European Schools network has **no generative AI tool approved for system-wide use**,
with an assessment procedure still being built.

**Where Globant wins.** The December 2027 deadline is an eighteen-month runway to build
conformity *into* a grading or admissions system rather than retrofit it — the highest-value
and most defensible education engagement available anywhere right now. Sovereignty is a
first-class requirement: [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(BSD-3) runs local models via Ollama; [`openfun/richie`](https://github.com/openfun/richie)
(MIT) is the French public-sector MOOC front-end; [`exelearning/exelearning`](https://github.com/exelearning/exelearning)
(AGPL-3.0) is led by Spain's Ministry of Education — state-backed credibility, copyleft terms.
[`huggingface/smolagents`](https://github.com/huggingface/smolagents) (Apache-2.0) is the
EU-domiciled agent base.

### APAC

**Regulatory posture — the widest divergence of any region; there is no "APAC approach".**
- **South Korea:** AI Basic Act in force **January 2026** — the region's most binding
  framework, with explicit high-impact-system obligations.
- **Vietnam:** the most education-specific rules anywhere. A decree names **automated
  assessment and behavioural monitoring** as high-risk; compliance due **March 2027**, with
  six extra months for systems already running before August 2026.
- **China:** mandatory model. **Japan, Singapore:** voluntary guidance. **Australia:** still
  developing.

**Demand signal.** Ipsos Education Monitor 2026: support for *banning* AI in schools is low
across most Asian markets — 23% Indonesia to 31% South Korea — and notably **higher in
Australia and New Zealand**. Sovereign model programmes are live: Singapore's SEA-LION,
India's Sarvam AI, Japan's NTT Sarashina.

**Where Globant wins.** A single regional product is the wrong shape here — the compliance
surface differs per jurisdiction. The right architecture is **one agent core with pluggable
policy nodes**, so Korea's high-impact duties and Vietnam's high-risk classification are
configuration, not forks. [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit)
(MIT) is APAC-built and is the strongest open knowledge-tracing base;
[`satvik314/educhain`](https://github.com/satvik314/educhain) (MIT) covers content
generation. Pair with a sovereign model where procurement demands it. Low ban-sentiment in
SE Asia plus Vietnam's dated deadline makes **Vietnam the clearest near-term APAC entry**.

### LATAM

**Regulatory posture — fragmented and mostly non-binding, converging on a risk taxonomy.**
Uruguay became the first Latin American country to sign the Council of Europe Framework
Convention on AI and Human Rights (2025). Colombia set national AI policy via **CONPES 4144**
(February 2025). Mexico has a 2024 federal bill proposing an oversight authority **and no
regulator to enforce it**. UNESCO launched a regional **Observatory on AI in Education for
LAC** in April 2026. 🔴 **Declared gap:** no source found in this pass gives a grounded
account of *education-specific* AI rules in these countries — the regional instruments are
general-purpose AI law, not education law.

**Demand signal — the strongest of any region.** UNESCO IESALC: **87%** of 200 HEIs across
19 countries use AI in at least one area, **74%** in teaching and learning, **26%** have a
formal strategy. TALIS 2024 teacher use: Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%.
Brazil is the regional market leader, backed by its National AI Strategy. Tecnológico de
Monterrey signed a UNESCO agreement in March 2026.

🔴 **Equity is a measurable constraint, not a talking point.** In Argentina AI use reaches
**75% in high socio-economic groups and 42% in low** — a 33-point gap inside one country.
A deployment that assumes connectivity widens it.

**Where Globant wins.** This is the region where the governance gap is largest and best
evidenced, and where Globant's delivery presence is strongest — the natural first market for
a **governed-adoption** offer: policy, audit trail and human-in-the-loop wrapped around AI
that institutions are already running informally.
[`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**, offline-first)
is the answer to the equity gap and the only MIT platform on the shelf.
[`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) has deep regional
footprint — integrate over its API, do not vendor it.


### Global

**The cross-region opportunity is the thing every regional section above has in common:
adoption has already happened and governance has not.** It is the same sale in four
jurisdictions with four different compliance skins, which makes it a *product*, not four
bespoke engagements.

**Two structural facts that hold everywhere, both re-measured at source on 2026-10-25:**

1. **The permissive supply is in the agent layer, not the platform layer** — 14 of 14
   verified agent/MCP rows are MIT/Apache-2.0/BSD-3, against 3 of 10 platforms. Any global
   offer must put the AI beside the LMS and talk over an API or component SDK, or it
   inherits copyleft in seven of ten client estates.
2. **"Draft, then human sign-off" is the one architecture that satisfies US state law, the
   EU AI Act and Vietnam's decree simultaneously.** Build it once; configure the policy
   per jurisdiction. See `compose/patterns.md`, Pattern AH.

🔴 **A permissive licence has a shelf life.** One component on these shelves relicensed to
proprietary two days before this pass, with a clause naming educational institutions
specifically. Re-read every component's licence payload at its commit SHA before an
engagement commits to it — the full sweep costs minutes.

🔴 **Declared global gap:** the education-specific MIT agent search returned **zero** new
addresses for the fourth consecutive pass. The agent supply in this industry is being built
as **MCP servers over existing LMS platforms**, not as standalone education agents — so
future discovery legs should be keyed on the platform name (Canvas, Moodle, Classroom,
Blackboard), not on the word "education".
---

## Regional evidence base — detail carried from earlier passes

### Global

**🆕 `p395` · 2026-10-23.** 🟡 **Use the range and name the spread, because the sources disagree by an
order of magnitude.** Readings taken this pass: **$6.4 B (2025) → $79.6 B by 2034** (IMARC);
**$8.3 B (2025) → $11.4 B (2026)**; **$7.52 B (2025) → $10.6 B (2026)**. 🔴 The 2025 base alone spans
**$6.4 B to $8.3 B**, so any single figure quoted from this base would be a choice disguised as a
fact. 🔵 All are vendor or market-research estimates with commercial interests; none is primary.

🟢 **The adoption figures are directionally consistent and more useful than the sizing:** student AI
use reported at **66 % (2024) → 92 % (2025)**, with roughly **86 % of higher-education students**
using AI as a research and brainstorming partner entering 2026. 🔵 Paired with North America's **10 %
of institutions having formal AI guidelines**, the global picture is near-universal student adoption
against near-absent institutional governance — which is the gap every engagement in this base is
ultimately selling into.

Opportunities that do not belong to one region, because the evidence for them is global:

🔴 🆕 `p387` **What this pass's prescribed regional legs actually returned, stated because silence
reads like coverage.** The four `AI education {region} 2026 adoption regulation players` legs were
run. **North America** and **LATAM** returned education-specific, citable material (the LATAM leg
reproduced the Digital Education Council and IESALC figures already on this shelf, from
independent write-ups). **EMEA and APAC returned almost nothing education-specific** — the EMEA leg
came back with enterprise-IT and HR-platform commentary, the APAC leg with enterprise tech-priority
reports and corporate-training vendors. Neither is evidence about schools or universities, and
neither was promoted. 🔵 The region-specific facts added to EMEA and APAC this pass came from
**targeted** legs (the AI Act deferral; the supply probes), not from the prescribed regional leg —
which is a finding about the instrument: *a regional leg phrased for market-research keywords
returns market research.*

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


#### 🆕 `p389` — Global: the supply is dated now, and that reprices two lines of every proposal

- 🟢 **A maintenance signal exists for the whole open-source supply, at ~1.2 s per repository.** A
  blobless shallow clone returns the real default ref, the HEAD SHA and the **last commit date**, and
  `git show HEAD:LICENSE` returns the grant from the payload. **60 addresses dated this pass**:
  [`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Why it belongs in market
  intelligence and not only in a method note:** a licence decides whether a client *may* build on
  something; a date decides whether they will be **alone** on it. Those are two different lines in an
  estimate, and until this pass this base could only fill in one of them.
- 🟡 **The distribution is better than the industry's reputation:** 58 live, 2 dead, **48 of 58 moved
  within 30 days** and 17 on the day of the pass. **7 of 58 are past 120 days — and four of those seven
  were carrying a recommendation on these shelves.** Details in [`intel/trends.md`](trends.md),
  *Trend 13*.
- 🔵 **Governance, not adoption, is the global line that now holds in every region.** Reports across
  all four legs describe the same move from experimentation to **embedded, governed infrastructure** —
  admissions, advising, administration — with **evidence of learning benefit** demanded at procurement
  and **education-specific** tools displacing generic assistants. The regional sections below differ in
  *which instrument* forces it, not in whether it is forced.
- 🔴 **One number this base will not publish: star counts as a ranking.** `api.github.com/search/*`
  and `/repos/*` return **403** in this sandbox ("sessions are bound to their configured
  repositories"), so the supply cannot be enumerated or ranked. A count can be *confirmed for an
  address already in hand* by fetching the repository page; two such counts appear in this pass and
  each says where it came from. Earlier cycles in the rotation had to publish a correction for
  pipeline-inflated stars — that correction stands.

#### 🆕 `p431` — Global: the evidence pack becomes a sellable artefact, because the harness is finally permissive

The market-size range in this file is unchanged this pass and the spread remains ~1.7×; nothing
measured today moves it. **What moved is what can be sold inside it.** HolonIQ's 2026 read — that
systems increasingly expect *evidence* that a product improves learning quality, persistence or
job-relevant skills — has been a demand signal this base could not supply against, because scoring
a tutor required either a closed vendor or an ungranted academic benchmark.

Measured at source today: [`shuangyan123/tutorbench`](https://github.com/shuangyan123/tutorbench)
(Apache-2.0 code, maintained) and [`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym)
(MIT). **The evidence pack — scored baseline, regression suite, re-test after each change — is now
a deliverable Globant can build on permissive terms and hand to the client as their own.**

🔵 It also prices a line this base previously had to leave open: an evaluation engagement is
**weeks, not months**, because the fixtures exist. The cost is a licence read per address and,
for `tutor_gym`, a fork budget.

### North America

**🆕 `p395` · 2026-10-23.** 🟡 **A richer sizing picture, and `Gap 393-C` explicitly still open.**
North America is sized at **~$951 M (2024) → ~$2.3 B by 2029, 15.9 % CAGR** (MarketsandMarkets), and
a 2026 statistics roundup puts the region at a **36 % share** of the global market with APAC growing
fastest. 🔴 **The governance gap is the sellable finding, not the market size:** the same roundup
reports **only 10 % of institutions have formal AI guidelines** and **71 % of U.S. teachers lack AI
training**. A studio that arrives with a governance artefact — an acceptable-use policy, a
human-in-the-loop design, an audit trail — is selling into a 90 % vacancy.

🔴 **`Gap 393-C` is NOT closed and this pass did not even attempt it**, because the channel for it is
refused: `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and every other primary-text host tested
this pass returned `connect_rejected` from the egress proxy. U.S. state rules remain carried **from
trackers and committee reporting only**. 🔵 Canada's proposed **AIDA** is recorded the same way, from
secondary description.

🟢 **New North American supply, and its condition is the point.**
[`macewan-cs/lti`](https://github.com/macewan-cs/lti) is MIT LTI 1.3 work from **MacEwan University**
(Canada), funded by its Faculty of Arts and Science — institutional provenance in exactly the region
that buys the most LMS integration work, and 🔴 **untouched for 1,918 days**, self-declared unstable,
deep linking unimplemented. Institutional authorship is not maintenance.

**Market.** Largest single region for AI-in-education spend. Canvas dominates higher-ed LMS.

🆕 `p393` 🔴 **A correction to a claim in wide circulation, and this base nearly carried it.** The
North America research leg returned, as its headline, *"Boston Public Schools became the first major US
district to mandate AI fluency as a graduation requirement, starting September 2026."* **The primary
coverage does not say that.** Two separate things were conflated:
- 🟢 **Boston** runs a **district AI-literacy programme** — funded by a **$1 M gift**, curriculum built
  with **UMass Boston** and a local industry group, teacher cohort trained over the summer, high-school
  programming from **September**. The mayor's stated *goal* is that *"every single BPS graduate will have
  fluency."* A goal and a funded programme — **not a diploma requirement**.
- 🟡 **The graduation requirement is at STATE level and is still a PROPOSAL.** The **Massachusetts DESE**
  is developing an **Artificial Intelligence and Digital Literacy** graduation requirement, recommended
  in **June** by the **Statewide Graduation Council**. Not adopted.

🔵 **Why this is on a market shelf and not only in a gap log.** The difference decides whether a studio
pitches a **compliance-driven mandate** (a requirement a district must satisfy) or a **discretionary
literacy programme** (a budget a district chose). Those are different buyers, different cycles and
different money. 🔴 And `Gap 393-C` records the exposure plainly: this base holds **no primary-source US
state or district education-AI rule**, and the secondary summaries it does hold have now been caught
overstating one.

🆕 `p393` 🟢 **The integration opportunity, now that the data standard has a granted client.** US K-12
runs on **Ed-Fi**, and [`edanalytics/edfi_api_client`](https://github.com/edanalytics/edfi_api_client)
(🟢 **Apache-2.0**, stock payload, HEAD **2026-10-06 — 16 d**) is a maintained Python client for it —
the roster-and-outcomes join that `Gap 391-B`'s district-targeting instrument needs. 🔴 The
**Canvas / Google Classroom / Schoology → Ed-Fi** extractors
([`Ed-Fi-Exchange-OSS/LMS-Toolkit`](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit), Apache-2.0) were
**archived by their owner on 2025-03-10**. 🔵 **That is the engagement:** the standard is alive, the
reference integration is abandoned, and the field mappings are readable. Porting them is a scoped,
defensible piece of work with no licence obstacle — and it is **not** available as a product.

🆕 `p393` **Adoption and training, from this pass's leg (vendor-sourced, so treat as directional):**
**10 %** of institutions have formal AI guidelines and **71 %** of US teachers report no AI training.
🔵 The gap between use and governance is the sellable one: policy, training and audit, not models.

**Regulation — state-by-state, and it moved fast in 2026.**

🆕 `p390` **Canada and Mexico, because "North America" on these shelves has meant the US.**
- 🇨🇦 **Canada has a strategy, not a statute.** The federal **"AI for All"** national strategy
  launched **4 Jun 2026**, with a national **AI-literacy** commitment at its centre. There is still
  **no federal AI Act** (AIDA died with the previous parliament) and **no confirmed date** for one,
  so procurement is governed by **PIPEDA plus provincial privacy law** — and education is provincial,
  so the binding requirements are per-province (BC, Ontario and Quebec differ materially; Quebec's
  Law 25 is the strictest). 🟢 **Consequence for a studio:** an AI-literacy programme is the
  fundable, politically-backed entry point in Canada right now, ahead of an assessment tool.
  Pair it with the granted BC curriculum layer already on these shelves
  ([`pdg6/bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server), MIT).
- 🇲🇽 **Mexico: bills, no regulator.** Several AI bills are in play and **no enforcement body is
  yet constituted**, so the operative constraints are the **LFPDPPP** (data protection) and SEP
  curriculum rules. 🟡 Treat an unregulated market as a *timing* advantage with a **documented
  governance posture anyway** — the rules will land mid-contract, and Chamilo's Spanish-language
  public-sector footprint is the realistic base.
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

6. 🆕 `p388` **Maryland's act is a procurement gate, not just a policy deadline — and that changes
   who the buyer is.** The instrument is **Chapter 634** (SB 720 / HB 1057). Beyond the 120-day
   clock `p385` recorded, three provisions make it a sales fact: **(a)** MSDE must publish an
   **AI-tool evaluation rubric that a district applies *before it pilots or purchases* any AI
   product** — so in Maryland the rubric, not the demo, is the first gate a studio's product meets;
   **(b)** every district must designate a **central-office, non-instructional AI coordinator** —
   a named, findable buyer who did not exist in the org chart last year; **(c)** **AI literacy enters
   state standards by 1 Jun 2027**, which is a curriculum engagement with a date on it. 🟢 The
   priceable work is *passing someone else's rubric*: an evidence pack mapped to MSDE's published
   criteria, reusable across all 24 districts. 🔵 Sources are secondary trackers and vendor blogs
   that disagree on detail; the primary instrument is Chapter 634, and one tracker's claim that the
   act **bans high-stakes automated decisions** could **not** be corroborated — it is not recorded
   here as fact.
7. 🆕 `p388` **The parent/guardian is an unserved persona with a granted, maintained surface — and no
   incumbent.** Three MIT servers now exist (see [`agents/top.md`](../agents/top.md) **Tier 5**),
   including [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
   (**47 releases**) over **Infinite Campus**, a major North American K-12 SIS this base could
   previously only name as closed. 🟢 **Why this is commercially interesting rather than merely new:**
   the parent portal is a *feature of the SIS*, not a market, so there is no incumbent vendor
   defending it; and **family transparency is written into the statutes** — Oklahoma SB 1734 names it
   explicitly, Maryland's act is built on guidance districts must hand down. A parent-facing surface
   is the one place "transparency" becomes a product instead of a PDF. 🔴 **The whole engagement turns
   on one line:** these tools authenticate as *a person*. A family running one for their own child is
   exercising their own access; **a studio hosting one for a district turns the same call into a
   FERPA-governed disclosure of an education record.** That boundary — not the licence — is the
   deliverable. See `Pattern P`.
8. 🆕 `p388` **Canada: the curriculum-data layer is granted, and jurisdictional content is the moat.**
   [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) serves
   the entire **BC Ministry of Education K–12 curriculum** over 12 MCP tools in its real three-column
   KDU structure — **including the First Peoples Principles of Learning**, which no generic tutor
   carries and no US-built product will. 🟢 This makes North America the **third region** with a
   curriculum-grounding asset (after Brazil's BNCC agent and `os-taxonomy`), so `Pattern H` is now
   demonstrable in a Canadian engagement rather than described. 🟡 Two releases, both **2026-03-27**,
   and the data is a crawl — **budget for currency, not for licence risk**: the grant is clean, the
   freshness is the liability, and a re-crawl is a maintenance line item a client should see quoted.


#### 🆕 `p389` — North America: what moved, and the one supply correction

- 🟡 **State legislative volume is the number to quote, not any single bill.** **134 AI-in-education
  bills across 31 states** in the 2026 session (MultiState tracker), weighted toward **data privacy,
  classroom restriction and curriculum** rather than mandated adoption. Named instruments:
  **California AB 1159** (limits use of student data to train AI models) and **Idaho SB 1227**
  (privacy protections for school AI tools); Oklahoma and Maryland require **human oversight** and bar
  AI from high-stakes decisions about students. *CONVERGENT-SECONDARY, PRIMARY UNREAD.*
- 🟡 **Federal:** the **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)** was advanced by the
  House Education and Workforce Committee at a **21 July 2026** markup, largely along party lines; it
  would let schools spend federal funds on AI curriculum. Still a bill, not law. *Recorded in `p386`;
  re-confirmed this pass, status unchanged.*
- 🔵 **Restriction is being authored by students, which is new.** A national framework produced with
  **Day of AI** and **AASA** (the "STUDENTS FIRST" proposal, August 2026) would **ban AI-generated
  assignments at all grade levels** and permit limited use from grade 9 with teacher permission. Treat
  it as a signal about how a district's own stakeholders will frame a pilot, not as policy.
- 🟢 **Opportunity — the North American curriculum-grounding asset is MIT and seven months stale.**
  [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) (MIT) grounds a
  tutor in the full BC K-12 curriculum including the **First Peoples Principles of Learning**, and its
  last commit is **2026-03-27 — 209 days**. The grant permits re-crawling; the work is a currency
  refresh plus a second jurisdiction. 🔵 **This is the cheapest credible differentiator in the
  region**: a district rubric asks whether the system teaches *its* standards, and a generic tutor
  cannot answer.
- 🔴 **And the correction.** [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)
  circulates in round-ups as a Canvas integration option. It has **no licence file** and has not moved
  in **144 days**. Use [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
  1 d) or [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) (MIT, 0 d) instead.
- 🟡 **Market share:** North America ≈ **36%** of the global AI-in-education market, ≈ **$3.68B in
  2026**, on one secondary roundup; the same source reports **60% of US K-12 teachers** used AI tools
  in 2024-25 and **32% weekly**. Quote with the source named, never as bare figures — the *Market
  size* range above is the honest form.


#### 🆕 `p391` Qualify the district before the pitch — the targeting data is open, keyless and MIT

🟢 **The opportunity:** US school AI money is not discretionary the way enterprise AI money is — it
arrives on identifiable federal, state and local lines, and the largest flexible federal line,
**Title I**, is allocated on **Census child-poverty counts rather than enrolment**. That means a
studio can price a pilot against a named district's real budget *before* the first call, and almost
nobody does.

[`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data) (🟢 **MIT**,
HEAD 2026-10-21) exposes four keyless federal sources as MCP tools: the **NCES Common Core of Data**
district and school directory (enrolment, teacher counts, charter/magnet status, grade range,
free/reduced-price lunch counts), the **CCD F-33 school-district finance survey** (revenue split
federal / state / local, expenditure by function, **computed per-pupil spending**) and **Census
SAIPE** child-poverty estimates for ages 5–17. Wiring and the three caveats are `Pattern W`.

🔴 **The qualifier that keeps this honest:** the finance survey **lags the directory by 1–2 years**,
the integration is **unofficial**, and the default endpoint is a **hosted gateway** — the data is
public, but which districts a studio is sizing up is commercially sensitive, so self-host before
running it against a named client list.

🟢 **Where the margin is:** high child-poverty rate **plus** low per-pupil spend identifies districts
with federal money and no incumbent vendor — the cheapest pilot to land and the hardest to displace.

#### 🆕 `p394` — North America: the legislative surface is countable now, and it is state-level

🟢 **The prescribed North America leg was the richest of the four this pass**, and what it returned is
a *buying-cycle* map rather than a market size.

| fact | figure | provenance |
|---|---|---|
| State bills on AI in education, 2026 session | **134 bills across 31 states** | MultiState tracker |
| Privacy-led examples | **California AB 1159**, **Idaho SB 1227** | same |
| States requiring **human oversight** of high-stakes AI decisions about students | **Oklahoma, Maryland** | same |
| States adding AI instruction to **CS graduation requirements** | **Georgia, Mississippi** | same |
| Federal | **H.R. 8747**, K-12 AI Literacy and Readiness Act of 2026 — advanced out of House Education & Workforce **2026-07-21**, largely along party lines | committee reporting |
| Canada | **"AI for All"** national strategy launched **2026-06-04**, including AI literacy | 🔴 a strategy, **not** a statute |
| New York City | proposed **one-year moratorium** on student-facing AI through grade 8; feedback window to 2026-05-08 | district proposal |
| Regional share | NA = **36%** of the AI-in-education market; **$3.68B (2026) → $32B (2030)** | 🔴 **vendor statistics compilation, single source — flagged, not to be quoted as a range** |

🔵 **The actionable reading is the oversight clause, not the bill count.** Oklahoma and Maryland
requiring a human in the loop for high-stakes decisions about students means a **placement, grading or
progression** agent sold into those states must expose a reviewable decision and an override path as a
*product feature*, not as a policy promise. 🟢 **That is the same obligation the EU AI Act imposes
under *EMEA* below**, so the two largest regulated markets are converging on one engineering
requirement and a studio can build it once. 🔴 **And the same clause disqualifies the
autonomous-grading pitch** in those states — which is exactly the pitch the autograding supply on
these shelves most readily supports.

🔴 **`Gap 393-C` is NOT closed, and is restated rather than quietly dropped.** `p393` caught a
widely-repeated Boston graduation-requirement claim that conflated a district programme with a state
proposal. This pass added **no** primary-source state rule either: every figure above comes from a
tracker or from committee reporting, not from a statute read first-hand. **This base still holds no
primary US state education-AI rule.**

#### 🆕 `p431` — North America: the region supplies the evaluation tier, and its statutes are the reason to sell it

**Supply.** The one MIT tutoring-evaluation testbed found anywhere this pass is North American:
[`Teachable-AI-Lab/tutor_gym`](https://github.com/Teachable-AI-Lab/tutor_gym), Georgia Tech
(Weitekamp, MacLellan, Siddiqui), with lineage back through `DannyWeitekamp/tutorenvs` to
`Teachable-AI-Lab/tutorenv`. It binds to `CAHLR/OATutor` (MIT, UC Berkeley) — also North American,
also already on this base's shelf. **The whole tutor-plus-scorer stack is NA-origin and MIT.**

**Why the statutes make it the pitch.** The 2026 state surface this file already records — 134 bills
across 31 states, **Oklahoma and Maryland barring AI from high-stakes decisions about students**,
NYC's K–8 student-facing moratorium, California AB 1159 on training-data use, Idaho SB 1227 — is a
demand for **demonstrable human oversight and demonstrable quality**, not for less AI. Federally,
the **K-12 AI Literacy and Readiness Act of 2026 (H.R. 8747)** advanced out of the House Education
and Workforce Committee on 21 July 2026, which funds literacy rather than restricting tools.

🟢 **The engagement, concretely:** a district or state system that must show a board *why* an AI
tutor is safe to deploy can be handed a scored baseline and a regression suite built entirely from
MIT components developed in its own jurisdiction. **That provenance is itself a procurement
argument**, and it is free.

🔴 **The NA-specific hole:** Oklahoma and Maryland regulate **high-stakes decisions** — i.e.
grading and placement. `Gap 431-C` says there is no open harness for the grading path. **In this
region the unmeasured surface is precisely the regulated one.**

### EMEA

**🆕 `p395` · 2026-10-23.** 🔴 **The single hardest product constraint in this base, and it is a
prohibition rather than an obligation: emotion-inference systems in educational settings are banned
outright under the EU AI Act** — unacceptable risk, alongside social scoring and predictive policing,
**not** a high-risk tier you can conformity-assess your way into. 🔵 Any "engagement detection",
"attention scoring" or "frustration sensing" feature in an EU classroom deliverable is not a
compliance cost; it is **unshippable**. This belongs in the first design review, not the legal review.

🟢 **And the high-risk scope is now quotable at clause level.** **Annex III ¶3** makes education AI
high-risk where it: determines **access or admission** to an institution; **evaluates learning
outcomes**; **assesses the appropriate level of education** for a person; or **monitors and detects
prohibited behaviour by students during tests**. 🔵 Those four verbs, not the word "education", are
what pull a system in — which is why `p394`'s assessment-heavy component tier is the regulated half of
this base and its content-generation tier largely is not.

🟡 **`394-D` narrows but does not close.** A second independent source now dates the **Digital
Omnibus** with a procedural chain: **European Parliament endorsed 2026-06-16, Council of the EU final
approval 2026-06-29**, moving stand-alone **Annex III** high-risk obligations from **2026-08-02** to
🆕 **2027-12-02**. That **corroborates `p394`'s December 2027** figure and supplies the missing
procedure. 🔴 **It is still not the Official Journal**, and `eur-lex.europa.eu` is refused on this
environment's egress — so the date stays **contested-but-converging**, and no conformity deadline
should be quoted to a client off this base alone.

🔴 **Stale advice is live in the wild**, which is itself worth telling a client: an EdTech compliance
guide read this pass **still counts down to 2026-08-02** as the enforcement deadline. Anyone who
budgeted against that guide has the wrong date in their plan.

🟢 **Article 4 AI-literacy duties have been enforceable since 2025-02-02** — already in force, cheap
to satisfy, and routinely missed.
🟡 **Provider vs deployer decides the obligation set:** a university that *builds and makes available*
a tool takes provider obligations; one that merely *deploys* takes deployer obligations. An
institution forking an open-source tutor and running it for its own students is a **deployer**; the
moment it offers that fork to other institutions it becomes a **provider**.

🔵 **Context for adoption, flagged as non-education data:** Eurostat-based figures put enterprise AI
adoption across the EU from **5.21 % (Romania) to 42.03 % (Denmark)** in 2025. That is businesses, not
schools, and is carried as background only.
🟢 **New EMEA supply:** [`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core), MIT, from
**Universitat Oberta de Catalunya** (Spain) — 🔴 **1,193 days dead**, and the only permissive Java LTI
1.3 core this base has found in any region.

🆕 `p393` 🔴 **This pass's EMEA research leg returned NO education-sector content, and that is written
down rather than left silent.** The prescribed leg (*"AI education EMEA 2026 adoption regulation
players"*) returned **enterprise** AI adoption only — CompTIA's 2026 IT outlook, a Workday study whose
cited post is dated **2023** — with **no named education player, ministry or school rule**. The two
figures worth keeping are not education-specific and are labelled as such: **38 %** of EMEA
organisations have not begun piloting AI, and **94 %** say they are at least somewhat likely to invest
in AI-specific training in 2026.

🆕 `p393` 🔴 **And `p392`'s procurement-shaped replacement leg does NOT generalise out of Spanish and
Portuguese.** `p392` found that a **buyer-shaped** leg in es/pt returned five live LATAM tenders where
English supply-shaped legs returned nothing. Ported to **French and German** this pass, the same shape
returned **no ministry tender for AI in education in France or Germany**. What it did return:
🟡 **Aalborg University (DK)**, *"call for AI pilot projects 2026"* — an institutional buyer, not a
ministry — and a **Council of Europe** consultancy call on AI in education that is **dated 2023**.
🔵 **The honest reading:** either EMEA education-AI procurement is not published where this channel can
see it, or it runs through framework agreements rather than discrete tenders. `Gap 393-D`. Until that is
resolved, **an EMEA engagement should not be sized from tender flow** the way `p392` sized LATAM.

🆕 `p393` 🟢 **One concrete EMEA supply fact to put in a proposal, because it bears on cost.**
Assessment migration to **QTI 3.0** now has a working converter —
[`Citolab/qti-convert-python`](https://github.com/Citolab/qti-convert-python), from the lab of **Cito,
the Dutch national assessment institute** — but it is 🔴 **GPL-3.0**, as is its TypeScript sibling,
**byte-identical payload**. 🔵 So the *licence* constraint here is **organisation-shaped, not
language-shaped**: switching language does not escape it. Budget it as an **arm's-length batch service**
(a container a pipeline invokes), which is a deployment component, not a library call — the same budget
line `p391` wrongly attached to LTI.

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

🆕 `p387` **Two EMEA public-sector references a studio can name in a pitch, both verified this pass,
both answering the objection that open source cannot be deployed institutionally.**
- **Bavaria (Germany) ships the multi-tenant AI layer for Moodle as open source.**
  [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
  (GPL-3.0-or-later, release 5.1.1) is a **multi-tenant** AI backend with per-role provider
  routing, rate limits, usage monitoring and an **Ollama** path for on-premises models — the
  sovereign stack in `Pattern E`, running in a state school system rather than proposed in a deck.
  🔵 Also published at `mebis-lp/moodle-local_ai_manager`: identical HEAD sha, **one project**.
- **Radboud University (NL) ships Brightspace grading automation as MIT.** `bscli` (PyPI, v0.3.13,
  **2026-09-04**, MIT) bulk-downloads submissions, distributes them to graders and **writes grades
  back** against the official Brightspace API — the institution-grade half of the LMS story that
  the MCP shelf does not have. 🟡 Its source address could not be resolved from this sandbox
  (`bscli.science.ru.nl` is DNS-unreachable); the grant and the release date were read from PyPI.

🆕 `p388` **The institution-shaped integration exists now, and it is the best governance reference on
these shelves.** [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) (**MIT**,
`main` · `3c680e0`) spans **four** systems a real European university runs — Brightspace, **OSIRIS**
(official academic records), MyTimetable and the public Study Guide — behind **one browser sign-in
including MFA**, with a self-renewing session. 🟢 **Every write action (submitting an assignment,
joining a group, replying in a discussion, registering for a course or exam) shows a preview and
requires explicit confirmation.** That is precisely the human-oversight control EU high-risk
obligations ask for, shipped as a default rather than written into a compliance annex — which makes
it the cheapest available *demonstration* of Annex III readiness for an EMEA pitch. 🔵 Note what it
implies about scope: a European engagement is rarely "integrate the LMS". It is **the LMS plus the
system of record plus the timetable**, each with its own auth, and this repository is the first
worked example of that on these shelves.

🔴 🆕 `p388` **Gap, stated rather than left as silence: still no national-ministry adoption data for
the UK, Germany, France or the Gulf states.** The prescribed EMEA leg returned EU AI Act framing and
the Digital Omnibus dates this base already resolved at `p380` — **no new regulatory fact and no new
supply.** This is the **fourth consecutive pass** with that gap, and the prescribed English-language
phrasing demonstrably does not reach it. 🟢 The fix is known and tested: **national-language legs**
are what broke the four-pass LATAM null at `p387`. `p389` should run German, French and Arabic legs
before concluding anything about EMEA supply or adoption depth.


#### 🆕 `p389` — EMEA: the Gulf is now the most aggressive AI-education jurisdiction in the world

- 🟢 **UAE — a compulsory subject in *every* school, with a training number attached.** A **Cabinet
  decision in September 2026** approved rollout of an AI curriculum across **all public *and private*
  schools**, with **22,000 teachers and education professionals** to be trained. For **2026-27** the
  Ministry of Education merged Design, Innovation and Computer Science with the AI curriculum into one
  subject — **"Artificial Intelligence and Technology"**, KG–Grade 12 — covering seven areas including
  foundational concepts, data and algorithms, and **ethical awareness**. 🔴 Sources disagree on whether
  the binding step was the 2025 announcement (AI as a subject in government schools from 2025-26) or
  the September 2026 Cabinet decision extending it to private schools; both are reported.
  *CONVERGENT-SECONDARY, PRIMARY UNREAD.*
- 🟢 **Saudi Arabia — comprehensive AI curriculum across all levels of public education from the
  2025-26 academic year**, led by the **National Curriculum Center** with **SDAIA** and partner
  ministries. 🔴 A vendor blog's "≈6 million students in year one" could not be traced to a primary
  source — **UNCONFIRMED**.
- 🟡 **EU AI Act timing is the thing clients get wrong.** Education used for **access, admission,
  evaluation and exam scoring** is **Annex III high-risk**, and the obligations reach non-EU systems
  whose outputs affect EU-based students. Under the **Digital Omnibus** amendment the high-risk
  application dates are reported as **2 December 2027** (stand-alone Annex III) and **2 August 2028**
  (AI embedded in regulated products). 🔵 **The sales consequence is counter-intuitive:** a deadline
  moving *out* does not reduce the work, because the conformity assessment must be complete **before**
  the system is placed on the market — so a 2027 go-live means the evidence is gathered in the
  engagement happening now. Sell the assessment artefacts as a deliverable dated to the client's
  go-live, not to the Act's.
- 🟡 **Soft law is the practical instrument meanwhile:** the European Commission's ethical guidelines
  for educators (AI Act + GDPR framing) and the OECD/EC **AILit** framework recorded in `p386`.
- 🔴 **Supply gap, and it is the sharpest in the rotation.** **No Gulf-origin and no Arabic-first
  open-source education agent or platform was found** — not one address, against the strongest
  statutory demand in the world. The permissive supply that exists is **EN + zh-CN**. The buildable
  gap is **Arabic-first curriculum grounding** aligned to the UAE MoE's seven areas, plus the
  **teacher-training surface** those 22,000 professionals must be trained on. 🟡 Informed gap, not a
  finding: the leg was English-language; an Arabic-language search is the next step.
- 🔴 **Africa: declared nil, and it is the fifth consecutive pass.** The prescribed leg returned
  **nothing** for **Nigeria** or **South Africa** — no national AI-in-education strategy, no regulator,
  no local EdTech vendor, no repository. That is a property of English-language search against this
  sandbox's channels as much as of the region, and it is recorded as a gap so it cannot be mistaken
  for coverage. The one asset that *is* placed for the continent is
  [Kolibri](https://github.com/learningequality/kolibri) (MIT, committed **0 d**) — offline-first by
  design — and it is not African in origin.


#### 🆕 `p391` The LTI integration path is open, which changes the cost of an EMEA LMS engagement

🟢 EMEA institutional education runs on **Moodle, ILIAS, Chamilo and Open edX** — copyleft platforms
where the commercial question is always *how does permissive work talk to an AGPL/GPL platform without
being absorbed by it*. The answer is the **LTI 1.3 boundary**, and `p390` had recorded that boundary
as having no maintained implementation.

🔴 **That was wrong, and the correction is worth money here specifically.** Both
[`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0, npm **v7.0.7, 2026-10-06**, 207
versions) and [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library)
(Apache-2.0, packagist **v6.4.4, 2026-09-23**, 68 versions) are live. An EMEA proposal therefore does
**not** need to budget for vendoring and security-reviewing a six-year-stale JWT/key-rotation library
— it needs a maintained dependency and an integration. See `Trend 19`.

🔴 🆕 `p392` **And the line `p391` added to the budget here comes back out.** `p391` wrote: *"there is
no maintained Python LTI library, so the interop edge is a separate Node or PHP service in front of a
Python agent — a real deployment component, cost it explicitly."* **Withdrawn.**
[`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) is 🟢 **MIT**
(1,098 B, © The Regents of the University of Michigan), HEAD **2026-10-20 — 2 days**, PyPI
**`django-lti` v0.10.1** (17 releases, 2026-08-07), **26 ★**, and it puts **LTI Advantage inside the
Django process**: one installed app, one middleware, one migration.
[`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**,
**73 ★**, HEAD 2026-07-01) does the same for a JupyterHub, which is what most EMEA CS and
data-science teaching already runs. 🟢 **What this is worth to an EMEA proposal, concretely:** no
second runtime to deploy, monitor, patch and explain to the client's security review — the edge
becomes a dependency and an integration test. 🔴 The constraint that does survive is **framework
shape, not language**: a FastAPI or Flask agent still handles the launch outside its own process, and
[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) — the best-maintained
Python implementation of the three, HEAD **2026-10-22** — is **AGPL-3.0**, so it is a boundary to
respect rather than a dependency to ship. `Gap 391-A` **CLOSED**; `Pattern A`, `Pattern B` and
`Pattern N` updated.

🔵 **Regulatory position unchanged this pass.** Four regional legs and a targeted EU Digital Omnibus
leg returned nothing this base does not already hold more precisely. 🔴 And `eur-lex.europa.eu` is
**DNS-unreachable** from this sandbox, so the EU dates on these shelves still rest on multi-house
secondary corroboration rather than the primary text — stated so no one mistakes repetition for
verification.

#### 🆕 `p394` — EMEA: `p393`'s nil REVERSES, and the EU AI Act's education trigger is now explicit

🟢 **This is a correction to a recorded absence, which is why it leads.** `p393` wrote that this exact
leg *"returned no education content at all — enterprise AI only, one source dated 2023"*. Re-run on
2026-10-22, **it does not repeat**: the leg returned the EU AI Act's education provisions directly.
🔵 **So a single nil from a prescribed leg is not evidence of a dry region** — it is evidence about
that run. This base has now seen the same leg return nothing and then something within 24 hours, and
that is worth more than either result alone.

🔴 **The trigger, stated precisely, because the precision is the whole value.** Under the EU AI Act,
education systems that **grade learners**, **assign them to programmes**, or **influence access to
qualifications** are **high-risk**, and require a **conformity assessment before deployment**.

🔵 **Map that onto this base's own supply and the consequence is immediate.** The autograding and
psychometrics tier added this pass — `gradethis`, `ottr`, `cran/exams`, `mirt`, `catR` — does *exactly*
the three things the Act names. 🔴 **An autograding engagement in the EU is a high-risk AI deployment,
not an integration project**, and it has to be sized with a conformity assessment in the plan. 🟢 The
same human-override design that Oklahoma and Maryland now require under *North America* is the
mitigation here too.

🔴 **A timing claim recorded as CONTESTED, not as fact.** One source dates the **Digital Omnibus** in
force **2026-07-27**, with high-risk obligations deferred to **December 2027** (stand-alone systems)
and **August 2028** (embedded systems). 🔴 **That disagrees with the European Commission's own
published timeline.** Both readings are recorded and neither is promoted: a studio sizing a
compliance deadline must read the Official Journal text, not this shelf and not the secondary
summaries. 🔵 Registered as **`Gap 394-D`**.

🟡 **And one market-condition signal, dated the day before this pass.** Reuters, **2026-10-21**: an AWS
EMEA executive says regulation, funding and skills gaps are pushing some European startups to consider
relocating. 🔵 Weigh it as what it is — a cloud vendor's public argument against the regulation its
customers are subject to — but the *skills* half corroborates the delivery-capacity constraint this
shelf already records for EMEA.

#### 🆕 `p431` — EMEA: the region's contribution to the evaluation tier is **ungranted**, and the compliance clock is the sales argument

🔴 **A nil on supply, stated as a nil.** The EMEA entry in this tier is
[`eth-lre/MathTutorBench`](https://github.com/eth-lre/MathTutorBench) (ETH Zurich, EMNLP 2025) — the
most-cited open pedagogy benchmark for LLM tutors. Measured at HEAD `6faed173ec2b` it carries **no
licence file anywhere in its tree**, and its README cites **CC-BY-4.0** in a badge and
**CC-BY-SA-4.0** in its licence section. **Europe's flagship tutoring benchmark cannot be shipped in
a client deliverable.** For an EMEA engagement the usable harnesses are the NA-origin and
Global ones.

**The clock, re-read this pass.** The **Digital Omnibus on AI, Regulation (EU) 2026/1744**, moved the
deadline for stand-alone Annex III high-risk education systems from 2 August 2026 to **2 December
2027** (and 2 August 2028 for AI embedded in regulated products). Two duties did **not** move:
**Article 50 transparency applies from 2 August 2026**, and the **Article 4 AI-literacy obligation has
applied since 2 February 2025** to every organisation using AI, schools included. The Commission and
the OECD published *Empowering Learners for the Age of AI* — an AI literacy framework for primary and
secondary education — on **18 June 2026**, alongside updated guidelines on ethical AI use in teaching.

🟢 **How to sell into that shape.** The delay is not relief; it is a **budget window with a fixed
end**. Annex III names assessment, admissions triage and proctoring as high-risk, and conformity
work on those cannot start from nothing in late 2027. An evidence pack built now on Apache-2.0
`tutorbench` is **the same artefact** the Article 50 disclosure and the eventual Annex III
conformity file will both draw on — and `huggingface/smolagents` (Apache-2.0, EU-domiciled) keeps the
agent layer in-region for a sovereignty-sensitive buyer.

### APAC

**🆕 `p395` · 2026-10-23.** 🟢 **APAC supplies the best new address in this pass, which reverses the
direction this base usually records.** [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) —
MIT, **1.3k ★**, HEAD **2026-10-13 — 10 d** — is an education-native personal learning agent with
layered memory and a Practice Lab, and it is placed in APAC on a **functional** signal: its shipped IM
channels are **Feishu and WeChat**, and its post-training runs on **Qwen3.6 35B**. 🔵 `p394` added the
EMEA-authored *platform* layer (LAMB, UPC Barcelona); `p395` adds the APAC-authored *agent* layer. The
non-US supply this base kept declaring missing is arriving — it is just not arriving through English
search legs.

🟡 **Sizing:** APAC AI-in-education **$591.6 M (2024) → $1,848.1 M by 2029, 20.9 % CAGR**
(MarketsandMarkets), and it is consistently named the **fastest-growing** region. A competing forecast
of a 46.12 % global CAGR is carried only to show the spread; the two cannot both be right.

🔴 **Regulation is fragmented by design, and that is the engagement risk.** Forrester describes a
landscape unlike the EU's single instrument: **Singapore** with mature guidelines, **China** with rules
against algorithmic misconduct, **India** applying existing criminal law, and the **ASEAN Guide on AI
Governance and Ethics** still early-stage. Its 2026 outlook puts regional priorities at
**sovereignty, security and responsible deployment**. 🔵 For a multi-country APAC rollout the
governance layer is **per-jurisdiction**, which is a build cost the EU's single conformity path does
not impose — the opposite of the usual assumption that Europe is the hard one.

🔴 **Vietnam's Law on AI** names **education** in its high-risk tier (`p394`); its commencement
remains **contested** and this pass could not read the statute — the primary-text channel is refused.
🔴 **No education-sector adoption figure for APAC was found on any leg.** Enterprise proxies exist
(56 % of APAC businesses running assistants; 48 % of governance leaders ranking AI top-priority for
2026) and are **not** education data. Written down as a gap rather than substituted.

🆕 `p393` **What this pass's APAC leg added — commercial motion, and a declared regulatory nil.**
- 🟢 **TCS and Pearson** announced a **multi-year AI learning alliance** aimed at employer skills gaps
  and at proving return on technology investment — the clearest signal that **corporate reskilling**,
  not K-12, is where APAC education-AI budget is moving.
- 🟢 **LearnUpon** opened a **Sydney headquarters** with **Create+** AI course authoring; **Alteryx**
  relaunched its Academy with personalised AI learning paths and credentials.
- 🟡 **OpenAI hired an ANZ policy lead** as **Canberra tightens AI governance and copyright rules** —
  copyright, in an education context, is a **content-licensing** question before it is a model question.
- 🔴 **Governance lags adoption, measured:** **87 %** of organisations encourage AI-agent use while
  **47 %** have governance, oversight and controls for them. **49 %** cite insufficient real-time data
  infrastructure as the barrier.
- 🔴 **Declared nil:** the leg returned **no education-specific regulation** — no ministry policy, no
  school or university rule. The binding regimes named below come from earlier passes, not this one.

🔵 **The APAC engagement shape this implies:** agent **governance and oversight** retrofitted onto
programmes that already deployed agents, and **corporate academies** rather than ministry platforms.

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
   [ai-shifu](https://github.com/ai-shifu/ai-shifu) (Apache-2.0, China),
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

6. 🆕 `p388` **The most advanced agent-native tutoring products in the world right now are
   Chinese-first, MIT, and invisible to an English-language search.** Three of them are on these
   shelves: [BaronCyrus/dsh-aha-tutor](https://github.com/BaronCyrus/dsh-aha-tutor) (**MIT**,
   published **2026-10-22**), [TecFancy/dsh-deeptutor](https://github.com/TecFancy/dsh-deeptutor)
   (manifest MIT) and `p385`'s [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell).
   🟢 **Two are built on DeepSeek Harness as a *platform*** — an agent-extension ecosystem for
   education forming outside the Western stack entirely. Aha Tutor's feature set is the most complete
   statement of adaptive-tutoring design read anywhere on these shelves: it establishes the learner's
   baseline, goal and time budget *before* writing the syllabus; **records answer confidence** so a
   lucky guess and a confident error are different events; and exposes a **"this step is wrong?"**
   control that re-checks, corrects, and **re-grades past attempts and the mastery estimate**.
   🔵 The commercial reading: the *pedagogy* is ahead of the Western open-source supply while the
   *packaging* is behind it — all three are single-maintainer, Chinese-first projects. **That is
   exactly the arbitrage a studio is for:** the design work is done and permissively licensed; the
   tenancy, localisation, support and institutional packaging are not. 🔴 A studio reading only
   English roundups sees none of this and will quote a build that already exists.
7. 🔴 🆕 `p388` **One regulatory detail deliberately *not* promoted:** sources disagree on Vietnam's
   instrument — one describes a law effective **1 Mar 2026** naming education among its high-risk
   sectors, another a *Digital Technology Industry Law* beginning in 2026. This base already carries
   a dated Vietnam roadmap (opportunity 5 above, compliance **1 Mar 2027**). 🔵 **The name and the
   date are not settled**, and the two readings imply different deadlines for the same client, so
   nothing here is revised on the strength of a search summary. Resolve against the primary
   instrument before quoting any Vietnamese date.


#### 🆕 `p389` — APAC: the region stopped being a market and became the supply

- 🟢 **The headline, and it was absent from this entire base until this pass.**
  [**THU-MAIC/OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, **Tsinghua University**,
  ~**41.3k ★**, committed **2026-10-22**, paper in **JCST 2026**, grown out of the internal **MAIC**
  system and validated on **700+ students**. It generates and then *teaches* a whole classroom: AI
  teacher with a voice, teaching assistants, simulated classmates, narrated slides, auto-graded
  quizzes, HTML interactives, shared whiteboard. **It is the largest education-native repository in
  the open-source supply and the licence is clean** — read from the payload, with `package.json`
  agreeing. 🔴 A 2026 third-party review reports it as **AGPL-3.0 with paid commercial licensing**;
  that is **false**, and it is exactly the kind of error that silently disqualifies an asset from a
  proposal. Full write-up in [`verticals/solutions.md`](../verticals/solutions.md) and
  [`agents/top.md`](../agents/top.md).
- 🔵 **This is a structural shift, not one repository.** The Tier-1 tutor shelf is now **majority APAC
  by origin** — DeepTutor (HKU, Apache-2.0, 3 d), ai-shifu (Apache-2.0), educhain (India, MIT),
  OpenTutor (MIT), Aha Tutor (MIT), learn-shell, ChatTutor — and the pedagogy is being designed *in
  the repositories*: confidence recorded separately from correctness, FSRS review, cognitive-load
  detection, misconception-aware branching. The authors are **university teaching groups**, which is
  why the licences are permissive and the evaluation claims arrive with papers attached.
- 🟡 **Regulation: education is named high-risk by statute here, which it is not in the US.**
  **Vietnam's Decision 33/2026/QD-TTg** lists **education among six high-risk sectors**, naming
  **automated assessment and behavioural monitoring**; many systems qualify only where the output is
  the **sole basis for a decision without meaningful human review**, and systems already operating
  before **15 August 2026** get a six-month grace period. **Korea's AI Basic Act** took effect
  **22 January 2026** (the region's first comprehensive statute), **Vietnam's Law on AI** on **1 March
  2026**, and **Taiwan's AI Basic Act** passed **December 2025**. China regulates by output type —
  recommendation algorithms, deep synthesis, generative AI, labelling — not by sector.
  *CONVERGENT-SECONDARY, PRIMARY UNREAD.*
- 🔵 **The engagement shape this creates.** Vietnam's "sole basis for a decision" test is a **design**
  test, not a paperwork test: an assessment agent with a recorded human review step falls outside the
  high-risk trigger, and one that auto-finalises a grade falls inside it. 🟢 That is the same control
  [tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) (MIT, EMEA) already ships as a default —
  preview-and-confirm on every write — so **the compliant pattern exists and crosses regions**.
- 🟡 **Public opinion is the constraint on classroom deployment, and it is measurable.** Ipsos
  Education Monitor 2026 support for **banning AI in schools**: Indonesia 23%, Thailand 25%, India
  26%, Singapore 28%, Japan and Malaysia 29%, **South Korea 31%**, with Australia and New Zealand
  higher. Teacher-facing deployments do not meet this resistance; student-facing ones do — which is
  the same conclusion *Trend 5* reached from growth data.


#### 🆕 `p391` APAC's export is now a *packaging model*, not only repositories

`Trend 14` recorded APAC as the net exporter of open-source education AI. This pass sharpens what is
being exported: **the harness-extension model**. Three MIT education plugins to the *same* agent
harness, by three unrelated maintainers, all published within about ten days —
[`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (tutor),
[`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (diagnosis-first
runtime) and [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (K8s + OIDC
multi-tenant hosting) — all China-origin, all bilingual EN/zh-CN. `Trend 18` has the mechanism.

🟢 **The opportunity for a studio:** these ship faster and cheaper than anything built application-first,
and the **separation of pedagogy from runtime** that `dsh-diagnostic-tutor` demonstrates is directly
reusable in a regulated market (`Pattern X`) — an auditor can read the teaching policy without reading
the application.

🔴 **The constraint to price in:** a harness extension is not deployable without its harness, so an
engagement that cannot adopt DeepSeek Harness buys the *structure*, not the package.

#### 🆕 `p394` — APAC: a SECOND jurisdiction now makes education AI high-risk by statute, and it is Vietnam

🟢 **This leg's find of the pass is one clause in one statute.** **Vietnam's Law on Artificial
Intelligence, in force 2026-03-01**, uses a risk-based structure, and its **high-risk tier names
education** alongside healthcare and finance. 🔵 **That makes Vietnam the second jurisdiction after the
EU to put education AI in a statutory high-risk tier** — and the first in APAC. An edtech AI
deployment there is a compliance target by default, not by interpretation.

| jurisdiction | instrument | status | education-specific? |
|---|---|---|---|
| **Vietnam** | Law on Artificial Intelligence | 🔴 **in force 2026-03-01** | 🔴 **YES — education named in the high-risk tier** |
| **South Korea** | AI Basic Act | 🔴 **in force 2026-01-22**; also carries SME/startup adoption support | not education-specific |
| **Taiwan** | AI Basic Act | passed **Dec 2025** | not education-specific |
| **China** | registration + content-labelling regime | 🔴 **the most binding in the region**: mandatory registration, strict content labelling | not education-specific |
| **Singapore** | agentic-AI framework | 🟡 best-practice **guidance, not law** | no |
| **Japan** | AI Promotion Act | 🟡 **no penalties** | no |
| **ASEAN** | Responsible AI Roadmap (2025) | governance track **through 2030** | no |

🔴 **Sources disagree on Vietnam's commencement date**, so it is recorded as a contested date and the
law should be read first-hand before an engagement is sized on it. 🔵 Same discipline as the Digital
Omnibus dispute under *EMEA*.

🔴 **An informed gap, stated so the silence cannot read as coverage: this leg returned NO
education-specific adoption figures for APAC at all.** No enrolment numbers, no institutional
penetration, no ministry spend. The only adoption-shaped claim on offer was a single vendor report
naming Google, Microsoft, IBM, Pearson and Byju's as "key players" and asserting that China, India and
Japan dominate — which is a vendor's player list, not an adoption measurement, and is **not** promoted
to a figure here. 🔵 So APAC on this shelf is now **well mapped on regulation and effectively unmapped
on adoption**, and that asymmetry is the opposite of LATAM's below.

#### 🆕 `p431` — APAC: 🔴 an explicit NIL on evaluation supply, and the reason it matters more here than anywhere else

**This leg returned nothing, and that is the finding.** Searched this pass for an APAC-origin or
APAC-language tutoring evaluation harness: none resolved to a repository with a readable grant.
`L2-Bench` (arXiv 2607.08842), a pedagogy-led benchmark for **second-language education** and the
single most relevant artefact to this region, surfaced with **no resolvable repository address**
(`Gap 431-A`). `ELBench` (arXiv 2608.09548) surfaced as a title only.

🔴 **Why the nil bites hardest in APAC.** This base's APAC story (`Trend 14`) is that the region
became the **net exporter** of open-source education AI, and its strongest engagement shape is
**in-language tutoring** — sovereign models are the regional supply: Sarvam AI (India), SEA-LION
(Singapore), ILMU (Malaysia), Sahabat AI (Indonesia), HyperCLOVA X Think (South Korea), Sarashina
(NTT, Japan), TAIDE (Taiwan). **Every harness measured today is English-first.** A tutor built on a
sovereign model therefore cannot be scored by anything this base can ship — the measurement layer
does not speak the language the product is sold in.

**The regulatory clock is nonetheless the most concrete in the world here.** South Korea's **AI Basic
Act took effect 22 January 2026** — the second comprehensive AI law after the EU's. **Vietnam places
education on its high-risk list by name** (automated assessment, behavioural monitoring), with
obligations from **1 March 2027** and a six-month extension only for systems already in operation
before 15 August 2026. China runs mandatory registration; Japan, Singapore and Australia remain
voluntary. Ipsos' Education Monitor 2026 puts support for **banning** AI in schools at 23%
(Indonesia) to 31% (South Korea) — restriction is live public opinion here, not a fringe view.

🟢 **The consequence for a proposal:** in APAC, **scope the evaluation harness as build work, not
as a component.** Translating or re-authoring `tutorbench` scenarios into the target language is a
real line item — and, under its CC-BY-4.0 content grant, one that is legally clean to do.

### LATAM

**🆕 `p395` · 2026-10-23.** 🔴 **`394-E` cannot be closed from this environment, and the reason is a
measured channel refusal rather than an absence of evidence.** `p394` predicted the *why* behind
LATAM's low assessment adoption would already be written down in **UNESCO IESALC's** instrument. 🟢
**The document was located:** a **UNESCO IESALC / UNU-IAS** working paper, *AI implementation in higher
education in Latin America and the Caribbean*, surveying **200 institutions across 19 countries**,
fielded **August–October 2025**, listed September 2026. 🔴 **And it is unreachable:** `unu.edu`,
`iesalc.unesco.org` and `www.unesco.org` all return `connect_rejected` from the egress proxy — checked
on **both** tools before this absence was written down, so this is a real block, not a tool artefact.
🔵 `repositorio.cepal.org` (ILIA 2025, whose governance section carries a regulation subdimension) and
`2023.indicelatam.cl` are refused the same way. **Every LATAM primary source this pass tried is off
the allowlist.**

🔴 **So `394-E`'s question — greenfield, or faculty declining assessment AI for good reasons — is still
unanswered, and a successor in this environment should not pre-register "read the IESALC instrument"
again.** It will fail identically. See `Gap 395-B`.

🔴 **The one sizing figure available is unusable and should not be quoted.** MarketsandMarkets sizes
*"Rest of Latin America"* at **$18.2 M (2024) → $36 M by 2029, 12.1 % CAGR** — but that bucket
**excludes Brazil and Mexico**, which is most of the regional market. 🔵 A figure that omits the two
largest economies is not a regional figure; this base should keep using the per-country framing it
already has.

🟡 **Two qualitative findings that survive the channel problem**, both from secondary sources and
labelled as such: **Chile** is named the regional leader in AI readiness, with an AI roadmap that
**survived a change of administration** — the durability point, not the ranking, is what matters to a
multi-year engagement; and the regional pattern is described as enthusiastic users with hesitant
institutions, producing *"a patchwork of pilot policies, vulnerable to being tossed out with each new
administration."* 🔵 That is a direct argument for scoping LATAM work so a deliverable outlives the
sponsor who bought it.

🆕 `p393` 🟢 **The LATAM leg was the ONLY prescribed regional leg this pass that returned
primary-institutional research**, and it is the most structurally useful adoption data on this shelf.
- **UNESCO IESALC with UNU-IAS** surveyed **200 institutions across 19 countries**, fielded
  **Aug–Oct 2025**. Adoption by function: **teaching and learning 73.5 %**, **research 57.0 %**,
  **administration 34.1 %**, **community engagement 20.0 %**.
- 🔴 **Only 26 % have any formal framework** governing it. 🔵 **That single pair of numbers is the
  LATAM pitch:** three quarters are teaching with it and one quarter has a policy for it.
- **Adoption is uneven by institution type**, which decides who can actually buy: **private non-profit
  84 %**, **public 68 %**, **private for-profit 52 %**.
- A **Digital Education Council** survey with **Tecnológico de Monterrey** reports **92 % of students**
  and **79 % of faculty** actively engaging with AI. 🔴 Different sample, not comparable with the
  UNESCO figures — both are kept, neither is averaged.
- **Regulation is uneven and mostly non-binding:** **Chile** leads with a National AI Policy (since
  2021) and a law under discussion; **Brazil** and **Colombia** have national strategies **without
  education-sector regulation**; in **Mexico**, SEP, ANUIES and the Observatorio IA have issued
  recommendations that are **not binding**. The **IDB** publishes the **ILIA** index across 19 countries.
- 🟢 🆕 **Brazil's MEC is running a REGULATORY SANDBOX for AI in education** — surfaced by this pass's
  French/German procurement leg, of all things, via a federal university's internal call to select the
  research group that will represent it. 🔵 A sandbox is a **named, time-boxed entry point** for a
  studio with a compliance story, and it is the most actionable single item this pass found in the region.

🆕 `p393` 🟢 **And the platform gap this section has carried since `p387` is now partly closed by
supply, not by analysis.** [`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) —
🟢 **Apache-2.0**, © BMO … **Sociedad Anónima, Nicaragua**, 676 files, 505 commits, 57 releases, HEAD
**2026-08-31** — is the **only Spanish-language LMS on these shelves that a studio can fork, extend and
ship closed**. Chamilo and i-educar are the public-sector incumbents and both are GPL. 🔴 At **21 ★**
with no multi-tenancy claim it is an **SME and pilot** base, not a ministry platform — but it changes
the four-way decision on [`verticals/solutions.md`](../verticals/solutions.md) for the first time in the
region's favour.

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

7. 🆕 `p387` **Stop pitching LATAM as a supply desert — and stop building the Spanish tutor from
   zero.** This base told four passes of readers that LATAM-native agent supply was a *"structural"*
   null. It is not. Three granted, LATAM-built agents were re-read first-hand on 2026-10-22 and are
   now shelved on [`agents/top.md`](../agents/top.md):
   - [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, Universidad Tecnológica de
     Pereira, **Colombia**) — a Spanish-language tutor delivered **as an Open edX plugin**, with a
     teacher statistics panel and TTS, built for **rural** higher education. For any LATAM
     engagement on Open edX this is a starting point, not a competitor.
   - [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
     (**MIT**, **Brazil**) — lesson plans and exams anchored to **BNCC** skill codes, with invented
     codes discarded before the teacher sees them. It is the curriculum-grounding pattern
     (`Pattern H`) already built against Brazil's national curriculum, and it exposes a keyed
     **API** so a school system can call it.
   - [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) (**MIT**, UFAPE, **Brazil**).
   **What the region is genuinely short of is not agents — it is tenancy, support and
   institutional-grade packaging**, which is what a studio sells. The honest pitch is *"your
   national-curriculum agent exists and is MIT; we make it multi-tenant, governed and supported."*
8. 🆕 `p387` **The Brazilian SIS is the integration surface, and it is GPL.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (GPL-2.0-or-later, **real default
   ref `2.12`**) is the student-records system a Brazilian municipal engagement is likely to already
   run. Quote integration **over its API**, never a fork: it keeps the deliverable clean and it is
   also the cheaper answer. See [`compose/patterns.md`](../compose/patterns.md) **Pattern O**.

9. 🆕 `p388` **A major regional publisher has shipped AI tutoring code — and a studio cannot build on
   it.** The registry sweep surfaced **`@santillana-ai/*`**: **Santillana**, one of the largest
   education publishers in Spain and Latin America, and the first major regional publisher's own
   tutoring code to appear on these shelves. 🔴 **It is ungranted.** The MIT claim sits on the
   *scaffolder* (`create-tutor-app`, 63 versions) whose published tarball contains **no licence file
   at all**; the package a client's codebase would actually depend on —
   **`typescript-tutor-sdk`, 115 published versions** — **declares no licence whatsoever**, ships no
   licence text, and names no repository. The GitHub address prompts for credentials: **closed, not
   missing**. Both are in any case clients for a **proprietary keyed API**, so a clean grant would
   have bought an SDK, not a tutoring engine. 🔵 **What it tells a studio about the region:** the
   commercial LATAM/Iberia education stack is **arriving as closed SaaS with an npm veneer**, while
   the *granted* LATAM supply remains the university and individual work `p387` shelved (TutorIA,
   the BNCC agent, techTutor). The competitive pitch writes itself — *your national-curriculum agent
   is already MIT and auditable; the publisher's is neither* — but it must be made before publisher
   SDKs become the default integration path. 🟡 The tie between the `@santillana-ai` npm scope and
   Santillana the company is **unverified** (`Gap 388-E`); the licence verdict does not depend on it.
10. 🆕 `p388` **The adoption numbers hold, and the shape of them is the opportunity.** The prescribed
   LATAM leg returned the **Digital Education Council LATAM survey 2026** — **92% of students and
   79% of faculty** engaging with AI, from **7,319 faculty across 29 institutions** — alongside
   **UNESCO IESALC (Sep 2026)**, which finds adoption widespread **while governance lags**. 🟢 The
   actionable detail is not the headline: **88% of faculty sit at "minimal" to "moderate"
   engagement**, and the *lowest* adoption is in **assessment** uses — feedback generation and
   academic-integrity checking — while **61% of students fear misuse by peers**. So the region is
   not short of enthusiasm or access; it is short of **depth in exactly the surface that carries the
   most governance risk**. An engagement that lands assessment-side AI *with* the governance wrapper
   sells into a near-universal adoption base against almost no incumbent depth. 🔴 Note the method
   fact too: the English-language leg returns survey PDFs, **not supply** — `p387`'s Spanish- and
   Portuguese-language legs are what found the actual agents, and that remains the only phrasing
   that works here.


#### 🆕 `p389` — LATAM: adoption is near-universal, governance is not, and that *is* the engagement

- 🟢 **The number to lead a LATAM pitch with.** A **UNESCO IESALC / UNU-IAS** study of **200 higher
  education institutions across 19 countries** found **87% use AI in at least one area of their
  activities** while **only 26% have a formal AI strategy**. Use is strongest in teaching and is
  **driven by faculty, researchers and students rather than institutional policy**.
  🔵 **Read that gap as the scope of work:** the institution does not need convincing to adopt — it
  has already adopted, without a policy. The sellable deliverable is **governance over use that
  already exists**: an inventory of what is in use, a data-boundary decision per use, and a human
  review step on anything consequential. That is a 2026 engagement with a named buyer, and it does
  not start with a model.
- 🟡 **The regional institutional layer is real and worth citing by name:** UNESCO launched the
  **Observatory on Artificial Intelligence in Education for Latin America and the Caribbean** on
  **14 April 2026**, and ran AI-ethics and regulation capacity work with officials in **Ecuador** and
  **Chile**. The **Latin American AI Index (ILIA)** records progress in school-level AI education and
  postgraduate programmes while noting these remain exceptions.
- 🟡 **Statutes:** **Uruguay** was the first in the region to sign the Council of Europe Framework
  Convention on AI (2025); **Colombia** adopted a national AI policy via **CONPES 4144** (February
  2025); **Brazil's** ENIA strategy dates from 2022 and **PL 2338/2023 — passed by the Senate in
  December 2024 — is still in the Câmara** as of October 2026, so **the LGPD is the binding instrument
  today**; **Mexico** has a federal AI bill mirroring the risk-based approach with a proposed
  oversight authority, not in force.
- 🔴 **The named failure case for the parent surface, and a LATAM client will know it.** In 2023 São
  Paulo's state education department (**SEDUC**) had its ***Minha Escola*** app installed on parents'
  phones **without notice or consent**; Data Privacy Brasil assessed it as a probable **LGPD**
  violation. Under **LGPD Art. 14**, children's data used beyond core teaching requires **specific,
  explicit, recorded and revocable parental consent** — which is precisely where a district-hosted
  parent assistant sits. 🟢 **So the deliverable is the consent mechanism itself**: per-guardian,
  recorded, revocable, auditable, shipped as a feature rather than a checkbox. See `Pattern P` in
  [`compose/patterns.md`](../compose/patterns.md) and *Trend 15* in [`trends.md`](trends.md).
- 🟢 **Supply, dated.** [portabilis/i-educar](https://github.com/portabilis/i-educar)
  (GPL-2.0-or-later, real ref **`2.12`**) remains the Brazilian municipal SIS an engagement will
  actually meet; [academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**,
  committed **1 d**) is still the only permissive Spanish-native administration base;
  [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) committed **0 d**. All three are live —
  worth saying explicitly, because "open source in LATAM" is routinely assumed to mean unmaintained.
- 🟡 **Mexico: informed gap.** No education-specific AI guidance or student-data rule for Mexico was
  found in this pass. The general position — data-protection law in force, no AI statute — is all that
  is supported. Stated rather than inferred.


#### 🆕 `p391` An informed gap, not coverage: there is no LATAM analogue of the district-targeting data

🔴 **Stated explicitly because silence here would look like coverage.** The North America opportunity
added this pass rests on US federal data being **open, keyless and per-district** (NCES CCD, CCD F-33
finance, Census SAIPE). **No equivalent instrument exists on these shelves for LATAM** — no
per-district enrolment, spend or poverty source that a studio could use to size and price a pilot
before the first meeting. Brazil's INEP and Mexico's SEP publish education statistics, but nothing
was found this pass exposing them as a queryable, granted component, and `zenodo.org` and `doi.org`
— the channels most likely to carry a research-deposited one — are **both DNS-unreachable** here.

Recorded as `Gap 391-B`. 🔵 It is a **channel-and-supply** gap, not a claim that the data does not
exist: a pass with working DNS to those hosts, or one that reads INEP/SEP portals directly, should
re-test it rather than inherit this line.

#### 🟢 🆕 `p392` — CLOSED for Brazil, 24 hours later, by a component this base already carried

🔴 **It was a reading gap, not a supply gap, and the instrument built this pass is what found it.**
The sentence above — *"nothing was found this pass exposing them as a queryable, granted component"* —
was published while [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) sat in this
base's own harvest log with a licence, a star count and a date against it.

| | |
|---|---|
| **what it is** | An MCP server over **70 Brazilian public data sources** — 533 tools, 131 resources, **66 APIs needing no key** — with the large datasets cached locally and queried through embedded **DuckDB** |
| **the education half** | **INEP `censo_escolar`** — the national school census, which is the per-school enrolment and infrastructure base a Brazilian pilot is scoped and priced against — and **INEP `enem`**, the national exam microdata |
| **grant** | 🟡 **MIT, 1,072 B, code only** (© 2025-2026 MCP Brasil; `pyproject.toml` and the PyPI classifier agree). 🔴 The README is explicit that the grant covers **the code alone**: each of the 70 sources carries its own licence in `SOURCES.md`, under an `ACCEPTABLE_USE.md` policy |
| **dates** | HEAD `2efb258` · **2026-08-18 — 65 days**; PyPI **`mcp-brasil` v0.14.0**, 18 releases, 2026-04-24 |
| **LGPD posture** | 🟢 Documented, not assumed: `SOURCES.md` grades *Educação* **RISCO ALTO**, records INEP's **2022 withdrawal** of microdata under LGPD and its **2024 anonymised resumption**, states the bundled snapshot is **2023, post-LGPD**, and names a **code safeguard** — `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate categories only (UF, sex, age band, race, school) and **excludes** `NU_INSCRICAO`, name and CPF |
| 🔴 **limits to put in the proposal** | The data is a **2023 snapshot** — currency is the risk, not the licence; the project's own note is to *validate a sample to confirm anonymisation*; and it is **explicitly not an official government service**, so a ministry engagement cites INEP and uses this as the access layer |

🟢 **What a Brazilian engagement can now do before the first meeting**, which is the whole point of
the North American instrument this one answers: size the municipality or state network from the school
census, locate the schools by infrastructure and enrolment band, and put a per-school number in the
proposal — **keyless, MIT code, no procurement to read the data.**

🔴 **Still open, and narrowed rather than closed:** there is no equivalent for **Mexico** (SEP), none
for **EMEA**, none for **APAC**. `Gap 391-B` is **CLOSED for LATAM/Brazil** and **carried for the other
three regions** — and its successor is a sharper question than the original: *who exposes a national
education-statistics office as a granted, queryable component?* Brazil, now. Nobody else found yet.

#### 🆕 `p392` LATAM is procuring AI education platforms right now, and not one tender asks for open source

🔵 **The prescribed regional legs were replaced, as `Gap 387-D` asked.** A **public-procurement-shaped**
leg in Spanish and Portuguese — the buyer's side rather than the supplier's — returned four live 2026
instruments where three passes of stars-sorted English legs returned nothing:

| buyer | instrument | what is being bought | 🔴 open source named? |
|---|---|---|---|
| **Santa Fe province, Argentina** — Ministry of Government and Public Innovation | Public Tender **01/26**, offers opened end of June 2026 | *Subscriptions* to AI-enhanced educational and corporate cloud platforms | **No** |
| **OEI (Organization of Ibero-American States), Chile** | **OEI-LIC-1-25** | Design and build of an **AI platform for administrative management in Chilean schools** — regulatory, financial and operational data, with personalised compliance recommendations | **No** |
| **UNOPS, Argentina** | **ITB/2026/62779**, closed 10 June 2026 | Long-term agreements for **educational platform software licences**, 2 years + 2×1 extensions | **No** |
| **CIEDEPAR consortium, Paraná, Brazil** | registry-of-prices, opened 15 Sep 2026 | Multi-municipality **SaaS integrated education-management platform** | **No** |
| **Francisco Morato (SP), Brazil** | opened 24 Jul 2026 | AI-supported education management, **R$1,924,665.00** | **No** |

🔴 **The finding is the absence in the last column.** LATAM public buyers are buying **subscriptions
and licences**, specified as products, while this knowledge base's entire thesis is permissive
open-source assembly. 🟢 **Two things follow for a studio, and they are opposite in sign.** (1) The
*competitive* opening is real: an open-source-assembled platform can be bid against subscription
pricing with a total-cost argument the incumbents cannot match, and the OEI-Chile scope — administrative
management over regulatory and financial data — is almost exactly the `i-educar` + agent shape on these
shelves. (2) 🔴 But the *procurement* will not ask for it, so the open-source case has to be made inside
a specification written for a product, which is a bid-writing problem before it is an engineering one.
🟡 **Graded `ATTRIBUTED-UNVERIFIED`**: each tender is from an aggregator or a news item, and no official
portal (COMPR.AR, ChileCompra, PNCP) is reachable from this sandbox to read the primary notice.

🟢 **What has not changed:** `p387`'s replacement claim still stands — LATAM's shortage is not agents
(Tier 4 shelves four LATAM-native ones) but **tenancy, support and institution-grade packaging**, which
remains LATAM opportunity 7 above. 🟡 `GuoMonth/dsh-multi-tenant` (MIT) supplies a **generic**
multi-tenant hosting substrate that a LATAM integrator could use for the hosting half of that gap —
it has no LMS surface, so it narrows the problem rather than solving it.

#### 🆕 `p394` — LATAM: the lowest-adoption use case is ASSESSMENT, which is where this base's supply sits

🟢 **A second independent survey corroborates near-universal adoption**, and one of its breakdowns is
worth more to a studio than the headline.

| source | scope | finding |
|---|---|---|
| **Digital Education Council**, AI in Higher Education LATAM Survey **2026** | **30,000+ responses, 29 institutions** | **92% of students** and **79% of faculty** actively engaging with AI |
| same | by use case | faculty use concentrates on **creating teaching materials, multimedia content and administrative support**; 🔴 **assessment uses — feedback generation, integrity checking — have the LOWEST adoption of all** |
| **UNESCO IESALC** | **200 HEIs across 19 LAC countries** | governance frameworks and institutional strategies **are not keeping pace with adoption** |
| **ILIA** (Latin American AI Index), 3rd edition | regional | country tiering — Pioneers, Adopters and below; 🔴 no education-specific cut |

🔵 **The assessment finding is the engagement, and it cuts both ways.** This base's deepest supply is
exactly assessment: `otter-grader`, `gradethis`, `ottr`, `nbgrader`, `cran/exams`, `qti_package_maker`,
`mirt`, `catR`. 🟢 **So the richest component tier here points at the thinnest regional demand** —
which is either the clearest greenfield on this shelf or a signal that LATAM faculty are *declining*
assessment AI for reasons a vendor should understand before pitching it. 🔴 **This base cannot tell
which from the data it holds**, and that distinction decides whether the correct move is to lead with
assessment or to lead with content generation. Registered as **`Gap 394-E`** rather than guessed.

🟢 **And one component now addresses the obvious objection.** If the reluctance is about
connectivity, invigilation or auditability rather than about AI, then **`cran/exams`'s NOPS mode** —
a printed exam, scanned, marked automatically, with the paper retained as the audit trail — is the
only thing in this whole base that puts automated assessment where there is no reliable network and
leaves a physical record behind. 🔵 It is GPL-2 | GPL-3, so it is delivered as a service behind a
process boundary; `Pattern AB` on [`compose/patterns.md`](../compose/patterns.md) wires it.

🔵 **The governance lag is the same shape as EMEA's compliance burden, inverted.** EMEA has a statutory
trigger and institutions that must meet it; LATAM has near-total adoption and, per IESALC,
**institutions without the frameworks to govern it**. 🟢 **The deliverable differs accordingly:** in
EMEA a studio sells conformity; in LATAM it sells the governance scaffold the institution has not
built — and that is advisory work attached to a platform engagement, not a licence sale.

#### 🆕 `p431` — LATAM: 🔴 a second explicit NIL on supply — and the region where the evidence pack is nonetheless the easiest sale

**Nil, stated as a nil.** No LATAM-origin tutoring evaluation harness resolved this pass, and no
Spanish- or Portuguese-language pedagogy benchmark resolved to a readable repository (`Gap 431-A`
again). The region that most needs the instrument supplies none of it.

**But the demand side is the strongest in this file, and it is measured.** UNESCO IESALC, across
**200 institutions in 19 countries**: **87%** use AI in at least one area, **74%** in teaching and
learning — and only **26%** have a formal AI strategy. OECD TALIS 2024 secondary-teacher AI use:
**Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%**, against an OECD average of **36%**. Ceibal
reports **75%** of Uruguayan public-school teachers using these tools. UNESCO launched its
**Observatory on Artificial Intelligence in Education for Latin America and the Caribbean** at ECLAC
in Santiago on **14 April 2026**.

🟢 **Why the nil does not block the engagement here.** LATAM's buyer has adoption without
governance — the 87%/26% gap is this file's headline number. **The evidence pack is exactly the
missing 74 points.** The harnesses are permissive and portable, and the scenario content under
`tutorbench`'s CC-BY-4.0 grant can be **translated and re-authored into Spanish and Portuguese
lawfully** — which converts `Gap 431-A` from a blocker into **billable localisation work with a
clean licence path**. Pair it with `learningequality/kolibri` (MIT, offline-first) where
connectivity is the constraint.

🔵 Against this base's standing finding that LATAM public tenders procure AI education platforms
as **subscriptions** and **no tender asks for open source** (`Trend 21`): the evidence pack is sold
as **advisory and assurance work attached to the platform**, not as a licence. That is the shape the
procurement actually has room for.

## Sources

Precedence Research · Grand View Research · Research and Markets · Markwide Research · Technavio ·
Coursera (AI in Higher Education, 2026) · EDUCAUSE 2026 AI survey · Ellucian 3rd Annual Higher
Education AI Survey · Inside Higher Ed / Hanover Research · Digital Education Council Global AI
Survey 2026 · MultiState · ExcelinEd · EdWeek · US Department of Education Dear Colleague letter ·
Regulation (EU) 2026/1744 (OJ 24 Jul 2026) · European Schools (eursc.eu) · HolonIQ Europe EdTech
200 and LATAM EdTech 100 · Wikipedia (openDesk, ZenDiS) · IAPP · Latham & Watkins APAC AI
regulation · Ipsos Education Monitor 2026 · IDB · CENIA via Foreign Policy · UNESCO LAC AI-in-
Education Observatory · AlSur · EdTech Innovation Hub (Google.org).

**Added `p389`:** 🟢 **First-hand, reproducible, no source grade needed** — `git` read access over 54
public repositories (real default ref, HEAD SHA, last commit date, licence text from the payload):
[`verified-repos.2026-10-22-p389.tsv`](verified-repos.2026-10-22-p389.tsv), method in
[`agents/top.md`](../agents/top.md#verification-method). `THU-MAIC/OpenMAIC` `LICENSE` and
`package.json`, read at `main` @ `269fde2d991f`; its `README.md` release log (v0.3.1 → v1.3.0-rc.1)
for dates, breaking-change conditions and the GHSA security releases. 🟡 **Secondary:** Gulf Business
/ Arabian Post / Gulf News on the **UAE Cabinet AI-curriculum decision (Sept 2026)**, the 22,000
teacher-training figure and the 2026-27 *Artificial Intelligence and Technology* subject merge · Gulf
News on **Saudi Arabia's** National Curriculum Center / **SDAIA** curriculum from 2025-26 · UNESCO
IESALC / **UNU-IAS** 19-country, 200-institution higher-education survey (87% use / 26% strategy) ·
**Data Privacy Brasil** on the São Paulo **SEDUC *Minha Escola*** app and LGPD Art. 14 · status of
Brazil's **PL 2338/2023** in the Câmara as of Oct 2026 · **Vietnam Decision 33/2026/QD-TTg** (education
among six high-risk sectors; 15 Aug 2026 grace period), **Korea AI Basic Act** (22 Jan 2026),
**Vietnam Law on AI** (1 Mar 2026), **Taiwan AI Basic Act** (Dec 2025) · **Digital Omnibus** high-risk
application dates (2 Dec 2027 / 2 Aug 2028) · **MultiState** 2026 session count, **California AB 1159**,
**Idaho SB 1227** · **Day of AI / AASA** student-authored framework (Aug 2026) · **Ipsos Education
Monitor 2026** AI-ban support by country. 🔴 **All policy items above are
`CONVERGENT-SECONDARY, PRIMARY UNREAD`** — the primary-text hosts remain unreachable from this
sandbox. 🔴 **Refuted this pass and recorded as such:** a 2026 third-party review stating OpenMAIC is
AGPL-3.0 with paid commercial licensing — contradicted by two independent reads inside the payload.
🔴 **UNCONFIRMED:** "≈6 million students in year one" for the Saudi curriculum (vendor blog); the
North America ≈36% / $3.68B share and the 60% / 32% US teacher-use figures (secondary roundup, quoted
as such).

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
