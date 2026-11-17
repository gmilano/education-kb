---
industry: education
region: Global
updated: 2026-11-17
---

# Current trends — education AI

**Pass `p874`, 2026-11-17** (fourth pass of the day). `p871` recorded eight trends; `p872` added
**T9** and revised **T8**; `p873` strengthened **T9** and added **T10**. `p874` adds **T11** — the
compliance clock the whole market is watching is not the one that is running — and updates the gap
ledger, where **three gaps move**: the EMEA instrument gap **closes**, Vietnam's dates **resolve**,
and the proctoring gap is **restated after being found factually wrong**.

**Previous pass note (`p873`):** strengthened **T9** with three further trials — including the one
that isolates *scaffolding* as the active ingredient — and added **T10** on Global-South agent
origin and its licensing. Each trend is tied to something measured or verified; where the only
available support is a vendor blog or a search summary, that is stated. **Note this pass's
evidential split:** repository claims were verified first-hand, while every trial, survey and
regulatory date is a search-engine summary of a page no channel in this session could open.

## T1 — The education-native agent has arrived, and it came from university labs

For the first time this KB can name education-native agents that ship on a real release
cadence rather than research prototypes. **DeepTutor** (HKUDS/HKU, Apache-2.0) shipped
`v1.7.3` on **2026-11-16**; **OpenMAIC** (THU-MAIC/Tsinghua, MIT) shipped `v1.5.0-rc.3` on
**2026-11-17** — both within 24 hours of this pass. Their feature lists have moved past
chat: mastery tracking, learning-path review, narrated video lessons, project-based learning,
course-level undo, PPTX export, desktop builds, ten-plus UI languages.

**Why it matters:** the serious open-source supply in this vertical is produced by academic
labs, not startups. That is a sourcing channel (partnership, co-development) rather than a
market to buy from, and it is consistent with T2.

## T2 — The money moved to institutions while venture funding collapsed

Edtech VC funding is reported at **~$2.4B in 2025, down ~89% from the 2021 peak**, while
forecasts for AI in education still show 30%+ CAGRs and institutional mandates are
multiplying (US federal grant weighting, SUNY literacy requirements, 1,000+ Indian
institutions, four Australian universities). The buyer is the institution and the ministry.

**Why it matters:** this is a services, integration and compliance market in 2026 — the shape
that favours a studio. It also means the competitor to beat is **Accenture**, whose Google
Cloud deal across 1,000+ Indian institutions is the reference transaction of this window.

## T3 — Governance is the binding constraint, and it is the product

Student adoption has outrun institutional policy: **~8 in 10 students** use generative or
agentic AI routinely (Inside Higher Ed, 17 Nov 2026), while only about **a quarter of faculty**
report a formal institutional AI policy. Simultaneously the US has **134 state bills across 31
states**, the EU has live Article 50 disclosure duties and a 2027 high-risk deadline, and
Brazil's LGPD already grants automated-decision review rights.

**Why it matters:** the gap institutions will pay to close is governance, not capability. The
model works; the policy, audit trail and human-review workflow do not exist yet.

## T4 — Regulation split into "already binding" and "deferred", and the deferral is the clock

The EU separated into two streams: **emotion recognition in education is banned already**
(Article 5(1)(f), since 2 February 2025) and **Article 50 transparency applies from 2 August
2026**, while **high-risk education obligations slipped to 2 December 2027** via the Digital
Omnibus (Regulation (EU) 2026/1744). Emotion/engagement detection is dead as a product
category in the EU; admissions, assessment and proctoring have roughly twelve months of grace.

**Caveat:** `eur-lex.europa.eu` is unreachable from this session, so this rests on secondary
sources. Confirm against primary text before client use.

## T5 — Institutions are starting to cancel commercial AI contracts over data

The sharpest demand signal this pass is a negative one: **Newcastle, Westminster and
Southampton** have reportedly decided not to renew commercial AI contracts on expiry, citing
concerns about entrusting student data to commercial providers and the limits of agentic AI
marking (Times Higher Education, via secondary newsletter). In parallel, US institutions face
FERPA the moment identifiable student data reaches a model.

**Why it matters:** non-renewal creates a procurement opening for self-hosted, model-agnostic
builds, and makes "student data never leaves your tenancy" the central value proposition
rather than a technical footnote. The stack for it is entirely permissive: Ollama/vLLM +
LiteLLM + DeepTutor or LibreChat.

## T6 — Ingestion, not inference, is where education AI actually fails

Education content is PDFs, scanned worksheets, textbooks and lecture video. The tooling that
matured in this window is ingestion: **Docling** (MIT), **marker** (Apache-2.0), **MinerU**
(Apache-2.0 + extra terms), **faster-whisper** (MIT). DeepTutor's own release notes across
v1.6.x–v1.7.x are dominated by parsing resilience, resumable embedding checkpoints and
retrieval comparison — not by model upgrades.

**Why it matters:** in a tutoring engagement, budget the ingestion pipeline as the primary
engineering risk. A graph-RAG layer over badly parsed textbooks produces confidently wrong
tutoring, which in education is a safeguarding problem rather than a quality problem.

## T7 — The permissive/copyleft fault line runs straight through this vertical

Verified this pass: of 22 education platforms, only **7 are permissive** (OpenOLAT Apache-2.0,
Kolibri MIT, Oppia Apache-2.0, Perseus MIT, Sakai ECL-2.0, Opencast ECL-2.0, DSpace BSD).
Moodle, Canvas, Open edX, ILIAS, Chamilo, Frappe LMS and both SIS options are GPL or AGPL.
Meanwhile the AI substrate is almost uniformly MIT/Apache-2.0.

Two licence corrections were recorded this pass: **Frappe LMS is AGPL-3.0, not MIT** as 2026
listicles state; and **Open WebUI is not plain BSD** — its clause 4 forbids removing Open WebUI
branding above 50 end users per rolling 30 days without an enterprise licence, which breaks
white-labelled campus deployment.

**Why it matters:** the architecture follows from the licences. Do not fork the platform;
build permissive AI services that attach over **LTI 1.3** (`ltijs`, Apache-2.0) and **xAPI**.
The integration seam is the product surface in education.

## T8 — Assessment is being redesigned, not defended

Berkeley Law barring AI from all exams and credited coursework, Florida weighing mandatory
disclosure, UK institutions doubting agentic marking, and the EU putting assessment in the
high-risk tier all point the same way: detection-based defence is losing and redesign is
starting. `p872` revises the supply side of this trend: **a permissive open-source grading system now
exists.** **ArguLens** (`wwrwbs/AI_AWE`, Apache-2.0, arXiv:2608.17356) scores argumentative
essays and generates feedback, and critically its **scorer is a grade-independent LightGBM model
over 31 explicit linguistic and discourse features, not an LLM**. It is **v0.1.0 and
research-grade**, trained on US middle-school English, and its own README restricts it to
"research and assistive" use with human oversight for high-stakes decisions.

**Why it matters:** the architecture, not the maturity, is the finding. Every regime now gating
automated assessment — the EU high-risk tier, Brazil's LGPD right to review of automated
decisions, Vietnam's Decision 33/2026/QD-TTg — demands that a score be explicable and
reproducible. A feature-based score satisfies that; an LLM score does not. The build path is
therefore **ArguLens's scorer re-fitted on the client's own graded corpus, wrapped in
`edx-ora2`'s (AGPL-3.0) human workflow with a logged override trail** — not an off-the-shelf
agent, and not a prompt.

**And note the regulatory escape hatch**, which is the most useful single sentence in this file:
Vietnam's high-risk listings are reported to bite only where AI output is **the sole basis for a
decision without meaningful human review**. Human-in-the-loop is not a compliance nicety; it is
what keeps an assessment system out of the high-risk tier entirely.

## T9 — The efficacy evidence arrived, the largest trial is negative, and `p873` found the active ingredient

New in `p872`; **substantially strengthened in `p873`, which added three more trials and one that
isolates the mechanism.** `p871` declared that no measured efficacy data existed for education AI.
It exists now, there are six trials in the table below, and it does not support the vendor
narrative.

| Trial | Design | Result |
|---|---|---|
| **EdWorkingPaper 26-1598** | RCT, **2,379 undergraduates, 30 instructors**, US public university; access to a course-integrated GenAI tutor randomised across sections of the same course | **Negative.** Tutor access **reduced final grades by 0.37 SD** and LMS participation by **0.90 SD**. **Estimated academic losses were larger among first-generation students.** |
| **Journal of Economic Education** (doi:10.1080/00220485.2026.2695361) | RCT, four macroeconomics sections: control / group-work only / AI only / AI + group work | **Positive.** All treatment arms beat control; the **combined GenAI + group-work arm produced the largest gains**. |
| **Nature Scientific Reports** (s41598-025-97652-6, 2025) | RCT, AI tutor vs in-class active learning | **Positive.** Students reportedly learned more than twice as much in less time. |
| **EdWorkingPaper 26-1551** — *new in `p873`* | **Two-year cluster RCT, 18 Tennessee middle schools**; Khan Academy's **Khanmigo** (proprietary) at district scale | **Small positive.** **0.06–0.08 SD per school year** — and the mechanism matters more than the effect: **struggling students rarely engaged the tutor at all.** |
| **"Less stress, better scores, same learning"** (ScienceDirect S2666920X25001778) — *new in `p873`* | RCT, **N=275**, programming education; unrestricted AI vs scaffolded AI tutor vs no AI | **Negative for unrestricted access, positive for scaffolding.** Unrestricted-AI students scored **worse than controls who never used AI** on exams taken **without** AI; the **scaffolded tutor beat unrestricted AI**. The title names the finding: performance and learning came apart. |
| **Tutor CoPilot** — *new in `p873`* | RCT, **900 tutors, 1,800 K–12 students**; AI assisting **human** tutors rather than replacing them | **Positive.** Students whose tutors had the system were **4 percentage points** more likely to master maths topics. |

**The reconciliation is the insight, and it is actionable.** These results are not contradictory;
they differ on **design**. The negative trial randomised *access* to a tutor layered on top of
existing instruction — and participation collapsed, which is the mechanism: an always-available
answer source substituted for the effortful work that produces learning. The positive trials
either **replaced** instruction with a research-designed tutor or **paired** AI with structured
human group work. The pattern across all three:

> **An AI tutor offered as an optional supplement can reduce learning. An AI tutor embedded in a
> designed pedagogy — with structured human interaction, or replacing a less effective mode —
> can improve it.** The intervention is the instructional design, not the model.

**`p873` sharpens that into two separable findings, and both are sellable.**

**1. The active ingredient is scaffolding, and one trial isolates it.** The programming RCT is the
most useful single study in this table because it ran *unrestricted AI* and a *scaffolded AI
tutor* as **separate arms of the same experiment**. Unrestricted access lost to using no AI at
all; scaffolding won. Every other result in the table is consistent with that one variable:
structured group work (positive), a human tutor holding the reins (positive), a research-designed
replacement tutor (positive), optional always-available access (negative), unmandated district
rollout (0.06–0.08 SD). **"Scaffolded or not" explains this table better than "AI or not" does** —
which means the deliverable a client should be buying is the scaffold: hint ladders, mastery
gates, attempt-before-answer, retrieval practice, escalation to a human. That is `compose/`
work and configuration, not model choice.

**2. The engagement-selection mechanism is a procurement argument, not a footnote.** Two
independent trials found it: undergraduate LMS participation **collapsed by 0.90 SD** under tutor
access, and in 18 middle schools **the struggling students barely used the tutor**. So uptake is
not uniform and it is **inversely correlated with need** — the learners a public institution is
buying the tool *for* are the least likely to use it. Any proposal whose success metric is
*usage* is measuring the wrong thing and will report a win while the equity outcome goes the other
way. Pair this with the measured governance gaps in `intel/market.md` (9% of LATAM institutions
evaluate their AI implementation at all) and the exposure is plain: **most clients currently
cannot detect either effect.** Selling the measurement plan is therefore both the honest move and
the commercially durable one — it is what makes the next engagement provable.

**And one caution against over-reading the dissociation.** The programming trial's headline is
that AI-supported students felt less stress and scored better *with* AI while learning no more.
A client measuring satisfaction and in-task performance will see success exactly where learning
did not happen. **Satisfaction and assisted performance are the two metrics most likely to be in a
pilot's success criteria, and they are the two that can move without learning.** Insist on at
least one unaided post-test.

**Why it matters commercially, and it matters a great deal.** The default edtech motion — deploy
a tutor, make it available, measure usage — is the arm that *lost*. A studio that leads with
instructional design, mandatory structured peer work, participation safeguards and a measurement
plan is selling the arm that won. That is a services-shaped proposition, not a licence-shaped
one, and it is defensible with citations against competitors who have none.

**The equity finding is a procurement risk, not a footnote.** Larger losses among
first-generation students will matter to any public institution with an access mandate, and it
should be raised proactively in a bid. Pair it with the measured governance gaps in
`intel/market.md`: 9% of LATAM institutions evaluate their AI implementations, and almost nobody
anywhere is measuring outcomes. A client who cannot detect this effect is exposed to it.

**Caveats, stated.** The two 2026 studies are working papers or early publications and may change
in peer review. Several registered trials (ClinicalTrials.gov NCT07871526 on AI-generated feedback
for medical students, NCT07692035 on an ICU teaching agent, NCT07481162 comparing AI and human
exam assessment) have **not reported outcomes**. And **none of this literature evaluates any
repository named in this KB** — it tests commercial and bespoke tutors.

## T10 — The Global South started producing education agents; almost none of them carry a licence

New in `p873`, and it is a market-shape finding rather than a licensing curiosity.

For several passes this KB recorded that education-native OSS came only from East Asian and US
university labs, and that LATAM and Africa appeared solely as deployers. That is no longer true —
`p873` resolved four Global-South education agents. **Exactly one has a licence.**

| Project | Origin | Licence | Fundable, legally |
|---|---|---|---|
| `LabSirius/TutorIA` | Universidad Tecnológica de Pereira, **Colombia** — funded, reported to **Minciencias** | **MIT** | **Yes** |
| `muskvdc/EduTwin-Africa` | **South Africa**, Grades 8–12 | **none** | No |
| `giovanayngrid-gk/multiagent-ai-tutor` | **Brazil**, Portuguese | **none** | No |
| `nifalconi/educational-agents` | LATAM Spanish, from a course | **none** | No |

**The discriminating variable looks like funding, not sophistication.** The one project with a
licence, a contributing guide, a branch policy and a requirements document is the one with a
national science ministry behind it and a reporting obligation attached. The unlicensed three are
individual and course work — written by people who had no reason to think about redistribution.

Three consequences worth acting on:

- **Regional sourcing should start with funded university and ministry projects.** They are the
  ones that can legally be built on, and the funding is also the best available signal that the
  project will still exist next year.
- **"Add a `LICENSE` file" is a near-free, high-value contribution to offer.** It converts a dead
  end into a possible collaboration, costs an afternoon, and is a genuinely good-faith way into a
  regional ecosystem. It cannot be done unilaterally — only the copyright holders can license
  their work — which is precisely why asking is the opening.
- **Do not mistake this for a quality judgement.** Nothing here says the unlicensed projects are
  worse. It says they are unusable, which is a different and more fixable problem.

**Counter-reading, stated.** Four repositories is a thin basis for a trend, the sample came from
two search legs, and absence of a licence may simply reflect the age of these projects rather than
anything structural. Treat T10 as a working hypothesis with four data points — and note that it
predicts something checkable next pass: **funded regional projects should carry licences at a
visibly higher rate than unfunded ones.**

## T11 — The compliance clock the market is watching is not the one that is running

**Every EMEA conversation in education AI is organised around 2 December 2027**, when the EU AI
Act's Annex III education high-risk obligations land after the Digital Omnibus deferral. `p874`'s
regulatory leg found that this is the wrong date to be selling against — on two independent counts.

**1. A different EU duty is already binding.** The AI Act's **AI-literacy obligation applies to
schools and institutions in their capacity as deployers**, and secondary reporting places it on
them from **July 2026**. There is no deferral on it. So the sector has a live, unmet legal duty
*now*, and a widely-publicised one it does not have to meet for another two years — and the market
is almost entirely organised around the second.

**2. A different jurisdiction's deadline arrives first.** Vietnam's **Law No. 134/2025/QH15** has
been in force since **1 March 2026**, and existing education systems must comply by **1 September
2027** — **three months before** the EU date. For any client operating in both, the Vietnamese
clock governs the programme schedule.

**What makes this actionable rather than merely true** is that the literacy duty is the one with a
measured deficit and a published standard behind it:

| Element | Value |
|---|---|
| Measured deficit, same population, one instrument | **79%** of European secondary students use AI for schoolwork; **47%** were shown how → a **32-point gap** (OpenAI/ThinkYoung, 5,000 students, 10 countries, fieldwork Apr–May 2026) |
| Corroboration, teacher side | **73%** of teachers use AI for planning and materials, **67%** for tests and rubrics (European School Education Platform, Apr 2026) |
| Delivery standard | **EC/OECD AILit Framework**, 18 June 2026 — 4 dimensions, **19 competences**, non-binding, product-neutral, feeds **PISA 2029** |
| Legal hook | AI Act literacy duty on deployers, reported as applying from **July 2026** |

**Why it matters commercially.** A high-risk conformance engagement is a 2027 budget line and a
competitive field. An AI-literacy engagement is a **2026** budget line against a duty the buyer is
already in breach of, with 19 named competences to evidence against and a measured 32-point gap to
justify the spend. It is also the natural on-ramp: the same governance artifacts, the same
deployer-side documentation habit, and the same buyer who will need **P4** in 2027. See
`compose/patterns.md` **P11**.

**Counter-reading, stated.** 🔴 **The July 2026 start date for the literacy duty is
secondary-sourced and this session cannot open a single EU primary text** (`eur-lex.europa.eu` and
the Council and Parliament hosts are refused at the egress proxy). The AI Act's literacy provision
is widely described as a duty on providers *and* deployers, but **its enforcement mechanics against
a school are not something this KB has verified, and may be weak** — a duty with no penalty
attached is a weaker sales hook than a conformity assessment with one. 🟡 **Do not tell a client
they face a specific sanction on a specific date for AI illiteracy.** The defensible pitch is the
*measured* gap plus the *published* framework, with the legal duty as context rather than threat.
Treat the date as a lead to confirm against EUR-Lex the moment that host is reachable.

## Declared gaps

- ~~**No measured efficacy data** for education AI.~~ **CLOSED by `p872`** — see **T9**. But the
  residual gap is sharp and worth stating precisely: **no trial evaluates any open-source system
  named in this KB.** The literature tests commercial and bespoke tutors. Nobody has published
  learning-outcome data for DeepTutor, OpenMAIC, OATutor, PageLM or ArguLens, and
  `pedagogy-benchmark` measures a *model's* pedagogical knowledge rather than a *deployed
  system's* outcomes. Running a real trial on an open-source deployment would make Globant the
  only party holding that evidence. **`p873` re-confirms this residual gap after adding three
  trials:** the new studies test Khan Academy's proprietary Khanmigo, a bespoke programming tutor
  and a human-tutor assistance tool. **Six trials, zero evaluating any repository in this KB.**
- **No open-source proctoring platform that is both maintained and permissive.** 🟢 **RESTATED by
  `p874`, which found the previous framing factually wrong.** `p871` found nothing; `p872` found
  two, both AGPL-3.0, and this KB concluded for two passes that **no permissive proctoring code
  existed**. **It does.** `p874` byte-read **seven** candidates' licences: **three are MIT** —
  `ganesh-786/Proctor`, `amaanwarsi/Proctora`, `code-by-abrar/Online-Proctoring-system` — and four
  are AGPL-3.0. 🔴 **The accurate gap is maturity, not licence:** all three permissive projects are
  single-branch and untagged, and `Proctora`'s own README says it should not be presented as a
  secure exam platform; the one complete platform (`sudosylabs/proctor`) is copyleft. 🔴 **A
  secondary source was corrected in the same leg** — `SriSatyaLokesh/pariksha` was presented as
  *the* Apache-2.0 option in the category and its bytes say **AGPL-3.0**. 🔵 **The method lesson is
  the one this KB keeps re-learning:** *"we searched and found none"* decayed into *"none exists"*
  across two passes, and a third search with the same tooling overturned it. **A negative finding
  needs a re-run date, not a promotion to fact.** Full table in `verticals/solutions.md`.
- ~~**Per-region adoption rates remain unavailable.**~~ **LARGELY CLOSED by `p872`**, and
  **further closed by `p874`** — see `intel/market.md`, *Measured adoption by region*.
  🟢 **The EMEA half is now CLOSED:** OpenAI/ThinkYoung (10 Nov 2026) is a European instrument with
  a European sampling frame — 5,000 secondary students aged 13–19 across 10 countries plus 600
  teachers — reporting **79%** AI use for schoolwork against **47%** who were shown how. Residual
  on that side: it measures **secondary**, not higher education, and it is **vendor-published**
  research on think-tank fieldwork. 🟡 **The APAC half is narrowed and precisely bounded, not
  closed:** `p874` added the Digital Education Council's regional comparatives (APAC faculty
  excitement **57%** vs **26%** US & Canada; teaching-use intent APAC **92%** / EMEA **89%** /
  LATAM **94%**) and one whole-institution datapoint (NTU Singapore, all undergraduates, Aug 2026),
  but **nothing measures APAC *institutions*** the way UNESCO IESALC measures LATAM's. The next
  instrument to try is named: APRU, UNESCO Bangkok, or a national rectors' conference.
- **All EU primary sources are unreachable from this session.** `eur-lex.europa.eu`,
  `data.consilium.europa.eu` and `www.europarl.europa.eu` all fail to resolve. Two identified
  Council documents (ST-13077-2026, ST-14902-2026) and a European Parliament briefing
  (`IUST_BRI(2026)784574`) **could not be read**, so all EU AI Act specifics remain
  secondary-sourced. These hosts would need allowing in the session's network settings.
- ~~**Vietnam's AI Law number and compliance dates are unresolved**~~ 🟢 **RESOLVED by `p874`:**
  **Law No. 134/2025/QH15** (not `91/2025/QH15`), passed 10 Dec 2025, **in force 1 March 2026**,
  with an **18-month transition for existing education systems closing 1 September 2027** (12
  months elsewhere; systems likely to cause serious damage excluded from the transition entirely).
  🔵 **The conflicting dates were two different clocks circulating without their labels** — entry
  into force vs the education compliance deadline — and one of them had been mis-stated by a year.
  🔴 **1 Sep 2027 is three months before the EU's 2 Dec 2027**, which makes it the nearest hard
  deadline in education AI; see **T11**. 🟡 A cited `Decree 142/2026` could not be corroborated.
- ~~**Africa and MENA fall outside the closed region vocabulary** and so cannot be filed.~~
  **WITHDRAWN by `p873` — this gap was never real, and it was self-inflicted.** The closed
  vocabulary is `North America | EMEA | APAC | LATAM | Global`, and **EMEA is Europe, Middle East
  and Africa**: both regions are in the bucket's own name. Nigerian, South African and Gulf
  findings have been fileable all along, and two passes dropped material they could have kept.
  `p873` files its South African, Nigerian and Dubai findings under **EMEA** with the country named
  in prose, as the schema intends. This is the second method error in two passes (after the licence
  grep) caught by **re-reading a rule rather than by new data** — the cheapest class of error to
  find and the easiest to leave standing for months.
- **Star counts unmeasurable for FOUR consecutive passes — and `p874` finally diagnoses it.**
  Three passes attributed the failure to the session's **GitHub** scope. `p874` tested that by
  probing **six hosts with no GitHub relationship at all** — `ecosyste.ms`, `api.ecosyste.ms`,
  `libraries.io`, `api.ossinsight.io`, `api.star-history.com`, `huggingface.co` — and **every one
  was refused at the egress proxy with `connect_rejected`**, while `codeload.github.com` (`400`)
  and `gitlab.com` (`301`) answered. 🟢 **This is a session EGRESS ALLOWLIST, not a GitHub
  permission and not an outage.** Two consequences: **no GitHub-side scope change will restore star
  counts**, and **the missing stars and the unreadable papers, surveys and EU texts are one defect
  with one fix** — a network-settings change naming the hosts. Nine routes tried. No star figure appears anywhere in this KB; blog-sourced figures are how
  the earlier inflated numbers got in, and `p873` saw the reason again — three secondary sources
  gave ~48.9k, ~54k and ~59.9k for the same project inside three weeks.
- **The efficacy literature gained no new trial in `p874`, and the residual gap is unchanged:**
  **zero of the trials in T9 evaluates any repository in this KB.** `p874` re-ran the trial leg and
  it returned the same three studies T9 already carries (EdWorkingPaper 26-1598, EdWorkingPaper
  26-1551 on Khanmigo, and the 2025 *Nature Scientific Reports* RCT) plus registered-but-unreported
  clinical-education trials. 🟡 **One discrepancy worth flagging rather than silently reconciling:**
  this pass's summary of the Khanmigo trial gives a **Year-1 effect of 0.020 population SD
  (indistinguishable from zero)** with **0.127–0.142 SD among students who actively participated**,
  where T9 records **0.06–0.08 SD per school year**. Both may be estimates from the same paper on
  different bases, and **the PDF cannot be opened from this session**, so neither figure is
  corrected here. The direction is the same and so is the mechanism — participating students show
  an effect, struggling students never engage. **Resolve against the paper once
  `edworkingpapers.com` is reachable.**
- **`p873` could not open a single non-GitHub source, and `p874` re-confirms it host by host.** `curl` returns `000` and `WebFetch`
  returns `ENOTFOUND` for every one of `arxiv.org`, `aclanthology.org`, `doi.org`,
  `sciencedirect.com`, `unesco.org`, `edworkingpapers.com`, `multistate.us`, `ipsos.com`,
  `lenda.ai` and all EU hosts. **Consequence for how to read this KB: repository claims are
  first-hand (existence, branch, tags, licence bytes, source files), and every paper, survey,
  trial result and regulatory date is a search-engine summary of a page nobody in this session
  could open.** The trial numbers in T9 in particular are reported effect sizes, not read ones.
  Allowing `arxiv.org`, `aclanthology.org` and `edworkingpapers.com` in the session's network
  settings would upgrade the whole efficacy section from secondary to primary, and is the single
  highest-leverage change available to this KB.
