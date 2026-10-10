---
industry: education
region: Global
updated: 2026-10-10
---

# Education — current trends

**Pass 95, 2026-10-10.** ⏱️ **Fifth pass of this date.** 🆕 **Fourteen trends.** `T14` is new — **the
curriculum mandates split by education level, and the higher-education limb is a different market** —
located by Pakistan's HEC notification, the first mandate in this KB that binds universities rather than
schools. 🟢 **`T13` gains three measured negatives** (the open-response scorers that turn out to be
CC BY-SA or ungranted) **and one permissive row at an adjacent layer** (`otter-grader`, BSD-3).
🟢 **`T9` gains a demand signal from the buyer side**: Brazil's MEC has put *correção automatizada* on its
own list of endorsed teacher uses. 🔴 **And `T3`'s governance-gap claim is reinforced by a method defect
rather than a new survey** — see `P982` in `intel/market.md`: two passes of "Japan has no instrument" were
an artefact of querying in English. Everything else is carried.

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date.** 🆕 **Thirteen trends.** `T12` (the instrument in
a federal system is subnational — now a *predictive* rule, having located Mexico's) and `T13` (the
permissive supply for regulated assessment is the **evidence** layer, not the scorer) are new this pass, and
🟢 **`T4` gains the mechanism behind a wrong date this file has recorded six times: it is a conflation of a
deferred Annex III deadline with a live Article 50 one.** Everything else is carried.

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date.** **Eleven trends.** `T1`–`T9` are carried from
pass 92 with this pass's amendments marked **🆕 p93** inside them; `T10` and `T11` are new.
🔵 **Each trend is tied to something measured or dated. Where pass 93 added no evidence to a carried
trend, it says so rather than restating it as fresh.**

## T1 — The unit of delivery is the *agent skill*, not the application

🟢 **Holds on a second measurement.** `topics/ai-tutor` holds **664 repos** — unchanged from pass 90, so the
denominator is stable rather than inflating. Roughly a quarter of the first two pages are **skills for agent
harnesses** rather than web applications: markdown-plus-scripts packages with no UI, no hosting, no database
and no migration. `universal-examprep-skill` (303★), `universal-diagnostic-tutor-skill` (242★), `Bloom` (285★,
explicitly *"self-hostable AI tutor **and** Claude Code skill"*), `kaogong-skill` (166★), `education-skills`
(107★).

🟢 **Near-uniformly MIT** — every skill row verified this pass read MIT from the payload.
🟢 🆕 **And the shape has now crossed into a second tier.** `tomaszboloz/WCAG-Accessibility-Skills` (MIT) is
**both** an agent skill **and** an accessibility checker, and `Community-Access/accessibility-agents` (MIT)
ships eleven review agents for coding hosts. **The skill is becoming the delivery vehicle for compliance
tooling, not just for tutoring** — which is a more defensible sale, because it attaches to a standard.
🔴 **The counter-risk is unchanged:** a skill inherits the host's model, limits and data policy. Where
automated assessment is regulated (Korea, Vietnam) or student-data training restricted (California AB 1159),
"it is just a skill" is not a compliance position.

## T2 — A vertical with its own licence family gets undercounted as copyleft by generic tooling

🟢 **Pass 90's finding, now fixed in code rather than only described.** `Sakai` and `Opencast` are
**ECL-2.0** — the Educational Community License, OSI-approved, Apache-2.0-derived, **permissive**. v2's
classifier returned `OTHER/unclassified`; unclassified reads as risk and gets dropped, which is part of how
*"8 of 8 copyleft"* survived six passes. 🟢 **The shared classifier `lib/license_family.sh` tests ECL *before* Apache** (ECL is
Apache-derived, so an Apache test swallows it) and both rows now classify. `OTHER/unclassified` across the
92-slug shelf went **2 → 0**.

🟢 🆕 **The same reasoning extended, pre-emptively, to the licences this industry will meet next:**
**EUPL-1.2** (the European Union Public Licence — the grant EU public bodies are steered toward, so it will
appear in EMEA public-sector education tenders) and three **source-available, non-OSI** families now named
rather than dropped: **BSL-1.1**, **Fair Code** and the **Sustainable Use License**. 🔴 That last group
matters because `leemonade/leemons` (292★, listed on `topics/lms`) is **Fair Code License v1.0 — not open
source**, and v2 would have shown it as merely "unclassified".

🔵 **The transferable rule: name the family, including the families that are not open.** Silence and a
refusal are both "unclassified" to a reader, and only one of them is a warning.

## T3 — Adoption is near-universal; governance is the market

Consistent across every region measured. 🆕 The LATAM governance figure is now a *measured* one rather than a
paraphrase.

| region | adoption | governance |
|---|---|---|
| North America | 86 % of orgs; 60 % of K-12 teachers | 🔴 134 bills / 31 states; 🆕 **only ~10 % of institutions have formal guidelines, and 71 % of teachers report no AI training** |
| LATAM | 🟢 87 % of institutions (UNESCO IESALC, 200 institutions / 19 countries, fieldwork **Aug–Oct 2025**); 92 % of students, 🆕 **79 % of faculty** | 🔴 🆕 **26 % have any formal framework** (UNESCO's own figure); no sectoral regulation anywhere in the region |
| APAC | fastest growth, 28.1 % CAGR | 🟡 the world's most advanced *and* most fragmented law — **plus three curriculum mandates** (see `T7`) |
| EMEA | 🟡 🆕 **first numbers ever recorded here** — UK: 36 % feel encouraged by their institution, 38 % are provided AI tools (HEPI, n=1 054) | 🟢 the most defined calendar: AI Act high-risk **2 Dec 2027**, 🆕 **Art. 4 literacy duty in force now** |

🟢 **The number to carry into a pitch has changed, and it is stronger than pass 90's.** Not "92 % use against
30 % effective" — which rested on a figure this pass found mis-stated — but **92 % of LATAM students using AI
against 26 % of institutions having any framework at all**, both from named instruments with stated sample
sizes. 🔵 **The purchasable artefact is governance plus capability: policy, disclosure, assessment redesign,
staff training, and an audit trail.** North America's 71 %-untrained figure says the capability half is the
bigger one.

## T4 — The EU AI Act has **two** deadlines, and the one that binds now is the one nobody cites

🟡 High-risk obligations — education among them — moved to **2 December 2027** (Digital/AI Omnibus, Council
approval 29 Jun 2026); embedded high-risk systems to 2 Aug 2028. Enforcement *powers* still begin 2 Aug 2026.
🔴 **A large share of vendor and consultancy guidance still states August 2026 for high-risk duties, and this
pass found that exact error again in a current source.**
🔴 🆕 **p93 found it a fifth time, and in a source that is otherwise *correct and current*** — a commentary
on the European Commission's **March 2026** ethical-guidelines update (see `T9`) which states that
*"obligations for Annex III high-risk AI systems apply from 2 August 2026, and education is expressly a
high-risk area."* 🔵 **The second half is right and the date is wrong by sixteen months.**
🟢 **Five independent instances across five passes is no longer an anecdote about sloppy blogs: the wrong
date is the majority reading of this regulation in the market.** That is a commercial fact, not a
correction — it means **a client's incumbent adviser is more likely than not to have given them the wrong
deadline**, and arriving with the dated Council decision is a differentiator rather than a pedantry.

🟢 🆕 **The addition that changes the pitch: Article 4's staff AI-literacy duty is already in force and was
not deferred.** So the EMEA conversation is not "prepare for a 2027 deadline" — which invites delay — but
"there is a duty you are already subject to, and a 14-month window on the larger one". 🔵 **Two deadlines, two
sales: literacy now, high-risk conformity by Dec 2027.** The first funds the second.


### 🟢 🆕 p94 amendment to T4 — the wrong date is a **conflation**, and that changes the sales motion

🔴 **Sixth instance, and pass 94 stopped counting and found the mechanism.** 2 August 2026 **was** the
Annex III date. The **Digital Omnibus on AI — `Regulation (EU) 2026/1744`** (European Parliament 16 Jun
2026, Council 29 Jun 2026, signed 8 Jul 2026; 🔴 **sources conflict on OJ publication, 24 Jul vs entry into
force 27 Jul 2026, and neither was read primary**) moved it to **2 December 2027**, with Annex I to
2 Aug 2028. 🟢 **But 2 August 2026 did not become an empty date — it became an Article 50 date.**

| limb | date | so what |
|---|---|---|
| Annex III high-risk, education included (point 3(b)) | **2 Dec 2027** | the big build, 14 months out |
| **Article 50** transparency | 🔴 **conflicting**: from **2 Aug 2026**; Art. 50(2) synthetic-content marking **2 Dec 2026**; **2 Feb 2027** for systems already on the market | **live or nearly live** |
| **Article 4** staff AI-literacy duty | **already in force** | 🟢 sells now |
| **Article 5** — **emotion recognition in education** | 🟢 **prohibited since 2 Feb 2025** | 🔴 **enforceable today** |

🔵 **So the market's "August 2026" is a stale date that collides with a live one, which is why correcting it
flatly has never worked.** 🟢 **The move is a question, not a correction:** *which article do you mean?*
Annex III → they are 16 months early and will under-build; Article 50 → they are right, and probably
unprepared.

🔴 **And the obligation none of the six sources mentioned is the only one already enforceable: emotion
recognition in education is prohibited outright.** 🔵 **That is not a 2027 planning item — it is a feature
audit of whatever the client already runs**, because engagement detection, attention tracking and affect
inference ship switched on in proctoring and "engagement analytics" products. **It is also the cheapest
possible opening deliverable in EMEA: a one-week inventory against a prohibition that is already law.**

## T5 — Generators are saturated; the checker gap is now **half closed**, and the remaining half is sharper

🔴 **What this KB published for five passes:** *"a targeted search for AI accessibility/alignment checkers in
education returned nothing usable"* and *"the only accessibility checker found is `UDOIT` — GPL-3.0, and not
AI-driven."* 🟢 **The accessibility half is FALSE and was falsified on the first targeted query this pass.**
Three permissive, AI-driven WCAG checkers verified from the payload: `tomaszboloz/WCAG-Accessibility-Skills`
(MIT), `Community-Access/accessibility-agents` (MIT), `9mtm/WCAG-Checker` (MIT, covers **PDF** as well as web).

🔵 **Why the shelf missed them, and this is the transferable part: the query named the industry.** Searching
*"accessibility checker **education**"* returns LMS plugins, and the LMS plugin in this space is GPL. Dropping
the industry term and searching the **standard** — WCAG — returns permissive, AI-driven tools immediately.
🟢 **A compliance tool is named after the standard it enforces, not the sector that buys it.** This is `P870`
(re-point the vocabulary) in a new guise, and it is the second time this pass that changing the query word
rather than the query target discharged a long-standing gap — the other being **CBSE** for India.

🔴 **What still does not exist: an instructional-alignment checker under a permissive grant with usable
evidence.** The narrowed specification, which is more useful than the old blanket claim:

| candidate | why it does not close the gap |
|---|---|
| `nsip/curriculum-mapper` (Apache-2.0, Australia) | 🔴 **archived, read-only**, keyword-based not semantic |
| `learning-commons-org/evaluators` | 🔴 **the corpora that make it evidence-backed are CC-BY-NC-SA** — see `T6` |
| `Zion-support/curriculum-alignment-checker` | 🔴 no licence payload in 24 filenames; self-describes as batch-generated |
| `lovejzzz/CourseMapper` | 🔴 no licence payload in 24 filenames; own README logs attribution failures |

🔵 **A checker remains the easier enterprise sale** — it does not displace the educator, it evidences
compliance. With North America at ~10 % guideline coverage and WCAG/508 exposure, **the accessibility half can
now be composed rather than built, and the alignment half is a clean, specified build.**

## T6 — 🆕 In the checker and dataset tier, the grant splits along code / prompt / corpus lines — and the permissive part is not the valuable part

🟢 **The most commercially consequential finding of this pass.**
[`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) ships **one**
`LICENSE.md` granting **four different things**:

| layer | grant | usable in a paid deliverable? |
|---|---|---|
| evaluator **code** | **MIT** | 🟢 yes |
| **prompts and settings** | **CC-BY-4.0** | 🟢 yes, with attribution |
| **Annotated CLEAR Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |
| **Annotated PERSUADE 2.0 Corpus** | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no** |

🔴 **The non-commercial clause sits precisely on the annotated corpora — which are what make it an
evidence-backed rubric evaluator rather than a prompt template.** 🔵 **So the question in this tier is not
"is it permissive" but "is the permissive part the valuable part". Here it is not.**

🟢 **A second shape, same lesson:** `learning-commons-org/knowledge-graph` licenses **per dataset and per
download** — `Open` / `Open + Gated` / `Gated` — through a platform catalogue, and states in terms that its
gated content is **not** covered by the CC licences the same file references. **A repo-root licence read
cannot resolve a data-layer grant.**

🔵 **Generalisation worth carrying to every other industry KB: as AI work moves from code to
code-plus-evaluation-data, licence risk migrates from the repository to the corpus, and corpora are where
non-commercial clauses live.** Pass 90 found a 2-way split (`microsoft/autogen`: docs CC-BY, code MIT) and it
was benign. This is a 4-way split and it is binding.

## T7 — 🆕 The regulatory frontier has moved from *regulating AI systems* to *mandating AI instruction* — and that is a services market, not a compliance cost

🟢 🆕 **p93: FIVE jurisdictions now compel AI *teaching* — and the fifth one resolves a misattribution this
KB recorded rather than used.**

| jurisdiction | instrument | from | reach |
|---|---|---|---|
| 🇨🇳 China | Ministry of Education — compulsory from **age six**, tiered primary→secondary | **Sep 2025** | **≥ 8 hours per year, nationwide** |
| 🇸🇬 Singapore | Ministry of Education — AI literacy across curriculum, co-curriculum and self-directed learning, with developmental milestones | announced **Mar 2026** | **all schools by 2027**, via Student Learning Space + IMDA modules |
| 🇮🇳 India | CBSE — *Computational Thinking and AI*, **Classes 3–8**, notification **9 Apr 2026** | session **2026-27** | CBSE-affiliated schools; aligned to NEP 2020 / NCFSE 2023 |
| 🇪🇺 EU | **AI Act Article 4** — staff AI-literacy duty | 🟢 **in force now** | every institution deploying an AI system |
| 🆕 p93 🇦🇪 UAE | **Cabinet-approved AI curriculum**, compulsory **kindergarten → Grade 12** in government schools; seven strands (foundational concepts · data and algorithms · software use · ethical awareness · real-world applications · innovation and project design · policies and community engagement) | announced **May 2025** (Sheikh Mohammed bin Rashid Al Maktoum); taught inside *Computing, Creative Design and Innovation* in **2025-26** | 🟢 **All government schools.** 🟡 Standalone-subject timing (*"Artificial Intelligence and Technology"*, 2026-27) and **private-school scope are contradicted between sources** and are **not** recorded as settled; one report of a **Sep 2026** cabinet approval extending it to private schools with **22 000 teachers trained** is **single-source and not used.** |

🔵 **Why this is a different business from everything else in this file.** A risk-classification regime
creates work that is defensive, legal-led and priced as compliance. A **curriculum mandate creates work that
is constructive, educator-led and priced as delivery**: someone must write the material, localise it to each
jurisdiction's scope and hours, train the teachers who have never taught it, and assess it.
🔴 **And the supply is thin where it matters.** The permissive AI-literacy curricula that exist
(`microsoft/ai-agents-for-beginners`, `rohitg00/ai-engineering-from-scratch`,
`pguso/agents-from-scratch`, `huggingface/agents-course` — all MIT or Apache-2.0) are written for **adult
developers**, not for **eight-year-olds in Class 3**. 🟢 **Nothing on this shelf addresses the primary-school
mandate that China has already implemented and India starts this session.**
🔴 **And curriculum is content, so it is where NC clauses cluster** — `cccareers/open-source-curriculum` is
**CC-BY-NC-SA**, unusable in a paid deliverable.

🔵 **This also corrects a sentence this KB carried for several passes.** The shelf said *"Singapore and Japan
stay deliberately voluntary"*. 🟢 **True of Singapore's position on regulating AI systems; false of its
position on AI in schools.** Voluntary regulation and mandated curriculum are different axes, and conflating
them understated the region's most purchasable commitment.

## T8 — 🆕 APAC's AI statutes name education **high-risk by sector**, and that is a different market from the curriculum mandates

🟢 **Three binding instruments arrived or took effect in APAC and two name education explicitly:**
**South Korea's AI Basic Act** (in force **22 Jan 2026**, with a signalled **one-year penalty grace
period**), **Vietnam's standalone AI statute** — the first in Southeast Asia — which puts **education
alongside finance and healthcare as high-risk**, with **pre-deployment registration in a National AI
Database**, conformity assessment, mandatory human oversight and **72-hour incident reporting**, compliance
due **Sep 2027**; and **Taiwan's AI Basic Act** (Dec 2025).

🟢 🆕 **p93 — the non-convergence claim is now corroborated by an independent analyst, in stronger words
than this KB used.** Pass 92 wrote that *"APAC compliance" is not a product* because the region does not
converge. Forrester's 2026 outlook states that a common APAC-wide AI legislative framework **"will remain a
distant dream"**, noting Singapore promoting responsible AI through mature *guidelines* while China
legislates against algorithmic misconduct, and that regional instruments such as the **ASEAN Guide on AI
Governance and Ethics** are still early-stage. 🔵 **A finding this KB derived from counting statutes is
the same finding a research house derived from watching legislatures. The sell is per-jurisdiction, and it
will stay per-jurisdiction.**

🔵 **Why this is a separate trend from `T7` and not an extension of it.** `T7` is about jurisdictions
*mandating that AI be taught* — a **content and curriculum** market. This is about jurisdictions *regulating
the AI an institution runs* — a **governance, logging and audit** market. 🔴 **Same region, different buyer,
different deliverable, different skill set.** A studio that reads them as one offer will mis-staff both.

🔴 **And the region does not converge, so it cannot be priced as one.** Korea and Vietnam are
comprehensive-and-binding; **Japan is deliberately voluntary and innovation-first**; Singapore's frameworks
are largely voluntary; India and Australia still lean on sectoral and privacy law. 🔵 **"APAC AI
compliance" is not a product.** Per-jurisdiction scoping is the product.

🟢 **The one transferable design constraint, and it is an architecture decision rather than a policy one:**
**72-hour incident reporting** means logging, alerting and a named owner have to be in the system from the
first sprint. 🔵 **It converges with the EU's Article 27 FRIA and with Oklahoma's and Maryland's
human-oversight floors** — three regions, three instruments, **one engineering requirement: a human-decision
gate with an audit trail.** 🟢 **Build that once and it sells in all three.** That is the single most
reusable finding in this file.

## T9 — 🆕 The regulated activity is **assessment**, and it is being adopted at sector scale right now

🟢 **Jisc reported early findings in May 2026 from year-long AI marking-and-feedback pilots across 38 UK
colleges and universities** *(search-summary)*, and analysts name assessment and grading the
fastest-growing AI-in-education category — driven, circularly, by student AI use.

🔴 **The EU AI Act's Annex III catches exactly this**: evaluating learning outcomes, screening applicants,
and monitoring candidates during examinations. 🔴 **So the fastest-growing category is the regulated
category**, and the shelf should be read accordingly:

- 🟢 The permissive assessment tier is unusually strong — **`Numbas` (Apache-2.0)**, **`Submitty` (BSD)**,
  **`otter-grader` / `nbgrader` (BSD)**, **`webtech-network/autograder` (Apache-2.0)**.
- 🔴 **The best full QTI platform is copyleft, and this pass corrected its family**: `oat-sa/tao-core` is
  **GPL-2.0**, not the LGPL this KB published last pass. The licence question on an assessment engagement is
  therefore sharper than it looked a day ago.
- 🟢 **`fborrasumh/tutoria` (MIT, Spain)** makes the teacher validate the lesson before the student sees it.
  🔵 **Human oversight expressed as a product step rather than a policy document is the most saleable
  compliance primitive in this industry** — and `AyudantIA` at UC Chile is the same idea bought at scale.
- 🔴 **Trust, not capability, is the stated barrier**: learners and parents remain sceptical of automated
  marking, and high-stakes assessment still needs teacher review. 🔵 **So "AI marks it" is not the product.
  "AI drafts it, a teacher signs it, and the trail proves it" is.**

### 🆕 p93 amendment to T9 — the EMEA instrument that landed is **guidance for teachers**, and it is dated March 2026, not June

🟢 🆕 **p93 adds the instrument, and corrects a date before it entered this file.** A newsletter summary
reported that the European Commission updated its *ethical guidelines on AI in education* **"on 9 June"**.
🔴 **It did not.** The update was published **5 March 2026**, as one of **four** Digital Education Action
Plan guideline sets released together (the others covering digital literacy and disinformation, selecting
digital content, and teaching informatics).

| property | the 2026 update |
|---|---|
| date | 🟢 **5 March 2026** |
| supersedes | the **2022** version, written by the Expert Group on AI and Data in Education and Training |
| author | the **Working Group on the Ethical Use of AI and Data in Education**, convened through the **European Digital Education Hub** |
| structure | three parts — founding principles and legal framing · guiding questions with scenarios · support resources — plus an **updated AI and data glossary** |
| audience | 🟢 **teachers and school leadership**, not ministries |
| stated driver | the growth of AI use in schools after generative AI, **and the AI Act entering into force** |
| languages | English first, with translation into all official EU languages during spring 2026 |

🔵 **Why the audience is the finding.** The Commission's answer to Article 4 is **a document for
teachers**, which is a statement about where the obligation lands: **on the institution's staff, as
capability.** 🟢 **That is purchasable** — the duty is on the deployer, the deadline is now, and the
official material is guidance rather than a product. 🔴 **And the same commentary stream that reported
this update is where `T4`'s wrong date showed up for the fifth time**, which is the practical shape of this
market: correct subject, wrong deadline, confident tone.

### 🟢 🆕 p95 amendment to T9 — the buyer has now said it out loud

🟢 **`T9` has argued for five passes that assessment is the regulated activity, from the regulator's side.
Pass 95 found the same claim from the buyer's side.** Brazil's **MEC** published **「Inteligência Artificial
na Educação Básica」** on **2026-04-08** (with UNESCO cooperation, project **914BRZ1157**), and among the
teacher-support uses it names explicitly is **`correção automatizada e detecção de plágio`** — automated
correction and plagiarism detection.

🔵 **A national education ministry putting automated correction on its own list of endorsed teacher uses is
a procurement signal, not a policy observation.** 🟢 **It converts the scoring stack from a technical thesis
into a line item**, and it lands in the region where this KB already holds the deepest curriculum open-data
rows (`bncc-dev`) and a classroom-proven automated-feedback platform (`mumuki`, AGPL-3.0, Argentina).
🔴 **And it sharpens `Gap 372` rather than easing it**: the demand is now explicit while the permissive
production scorer still does not exist.

🟡 **Evidence grade: search-summary** — `www.gov.br` is egress-blocked, so the two official PDFs are
identified and unread. **The document is orientative, not binding.**

## T10 — 🆕 In the learner-model tier, the **permissive** option and the **explainable** option turn out to be the same one

🟢 **Pass 92 opened this tier with one library** (`pykt-team/pykt-toolkit`, deep knowledge tracing) and
wrote that the learner model had arrived. 🟢 **Pass 93 found the rest of the stack by naming three more
techniques, and the structure inside it is the trend:**

| technique | repo | grant | ★ | what it emits |
|---|---|---|---|---|
| Bayesian Knowledge Tracing | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | **MIT** | 282 | 🟢 four interpretable parameters per skill — prior, learn, slip, guess |
| Item Response Theory | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) · [`eribean/girth`](https://github.com/eribean/girth) | **MIT** · **MIT** | 173 · 126 | 🟢 item difficulty and discrimination, learner ability, on one scale |
| Computerized Adaptive Testing | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** | 153 | 🟢 the next item, and a defensible stopping rule |
| review scheduling | [`open-spaced-repetition/py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** | 506 | 🟢 when the learner will forget |
| deep knowledge tracing | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | ~430 | 🟡 a predicted probability from a trained network |

🔵 **The trend is the coincidence of three properties that usually trade off against each other.** The
classical psychometric layer is simultaneously (a) **permissive** — MIT and BSD throughout, (b) **more
production-worn** — `catsim` carries 877 commits against `pykt-toolkit`'s research-benchmark posture, and
(c) **the only part of the tier that produces an artefact you can put in front of a regulator.**

🔴 **And (c) is the one that decides an engagement.** Under the EU AI Act's Annex III, assessing learning
outcomes is high-risk and owes an explanation to the person assessed. **A 2-parameter logistic item curve
is an explanation. A per-skill slip-and-guess probability is an explanation. An LSTM activation is not.**
🟢 **So the advice inverts the usual instinct to reach for the newest model: in this tier, the older
mathematics is the compliant choice, and it is also the cheaper and better-licensed one.**

🟢 **The seams are named by the tools, not by this KB** — `catsim`'s README states outright that
*"catsim does not implement item parameter estimation"* and points at `py-irt` and `girth`. 🔵 **A stack
whose boundaries its own authors document is a different risk than one an integrator invents.** Costed as
`P93-A`.

🔴 **What is still missing, and it is not a library.** Nothing found this pass wires any of this into an
agent's turn (`Gap 369`), and there is **no permissive production-grade automated essay scorer at all**
(`Gap 372`) — so the tier covers **structured** assessment well and **open-response** assessment not at
all. 🔵 **Which is to say it covers the part the EU names high-risk least well.**

## T11 — 🆕 Grounding a curriculum-aligned tutor in verified standards data is now **measured**, and the number is 31.9 % → 0.2 %

🟢 **This KB has argued for ninety passes that the interoperability and standards tier is where the value
is. It has never had a number for it. It does now, and the number is somebody else's, published,
reproducible and adversarial to its own publisher's interest.**

[`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) measures LLM hallucination against
Brazil's national curriculum base. Its grounding study — **8 models, 300 items**:

| condition | hallucination rate |
|---|---|
| 🔴 no source in context | **31.9 %** |
| 🟢 **dataset in the prompt** | **0.2 %** |
| 🟡 **querying the MCP server** | **2.3 %** |

🔵 **Three readings, in descending order of how much they should change what a studio builds.**

1. 🟢 **Grounding is worth ~160× on this task.** Not "improves accuracy" — **31.9 % → 0.2 %**. For any
   deliverable that cites curriculum codes to a teacher, the standards dataset is not an enhancement, it
   is the product's correctness boundary.
2. 🔴 **The MCP route is ten times worse than embedding the data** (2.3 % vs 0.2 %), while still ~14×
   better than nothing. 🔵 **That is an architecture decision with evidence behind it: for curriculum
   alignment, ship the dataset in the context, and keep the tool call for what the dataset cannot
   answer.** It also explains why `bncc-dev/bncc-pacotes` embeds the data inside its MCP server rather
   than calling home.
3. 🔴 **Ungrounded faithfulness varies from 88 % to 3 % across models**, so "which model" is a much weaker
   lever than "is the source in the context". 🔵 **Model selection is the cheap question; grounding is
   the expensive one, and only one of them is usually on the agenda.**

🟡 **Two reasons to cite this carefully, both from the repository itself.** 🟢 **Its README declares a
conflict of interest in its own words** — *"Vale declarar o conflito de interesse: a Profy opera produtos
que usam LLMs sobre a BNCC"* — and publishes methodology, items, raw responses and judgments so the
numbers can be recalculated. 🔵 **A disclosed conflict with reproducible workings is a better evidentiary
position than most vendor benchmarks on this shelf.** 🔴 **But its own two surfaces disagree on the
corpus size:** the repository description says **15 300 responses from 17 models**, while the README
describes the official round as **19 models × 900 = 17 100 published raw responses**.
🔵 **Cite the grounding percentages, which are the study's own headline, and do not cite a corpus size
from the description** — this is `compose/code/description-drift-audit/`'s shape appearing inside a source
this pass otherwise rates highly.

🔴 **Generalisation limit, stated.** One benchmark, one curriculum, one language, 300 items. **The
direction is almost certainly general and the magnitude is not.** Use it to justify the architecture, not
to promise a client 0.2 %.

## T12 — 🆕 p94 In a federal system the instrument is **subnational**, and this is now a predictive rule rather than an observation

🟢 **Pass 93 observed it in Canada. Pass 94 used it to find Mexico's instrument on the first attempt. That
is the difference between a note and a method.**

| federation | national instrument | where the instrument actually is |
|---|---|---|
| **Canada** | 🔴 none | BC (ministerial guidance, K-12 resources to May 2026, Jan 2026 post-secondary principles) · Alberta (three-year agreement with **Amii**) · 🔴 **Ontario: none, and its largest board publicly asked the ministry for one** |
| **Mexico** | 🔴 none; a **PT bill of 29 Apr 2026** sits in the Education Committee | 🟢 **Estado de México: reform to Art. 61 of the state `Ley de Educación`** — upper-secondary and higher education must promote *responsible, ethical and gradual* use of AI. 🔴 Promulgation date unresolved (Apr 2026 per one source; a 31 Jan–15 Jul 2026 window per another) |
| **United States** | 🟡 **two bills of the same shape** — `H.R. 8747` (reported, not enacted) and `S. 5225` — both make AI instruction an **eligible use of existing federal K-12 funds** | 🟢 **State law**: Idaho SB 1227, Oklahoma, Maryland SB 720; plus NYC's district-level Traffic Light Framework |

🔵 **Three consequences, all operational.**

1. 🔴 **A national query reports an empty world.** Five passes of this KB recorded "Mexico: no AI law" and
   every one of them was accurate and useless. 🟢 **The fix is `P955` applied to jurisdictions: name the
   instrument and the level, not the country.**
2. 🟢 **A federal market is a repeatable one.** A deliverable built for one state or province fits the next,
   because the instruments converge in content — *responsible use*, *teacher review*, *local policy*, *a
   designated coordinator* — even when they differ in form.
3. 🔵 **And the US federal shape tells you who signs.** When the federal lever is **fund eligibility**
   rather than mandate, 🟢 **the buyer is the district administrator with a Title IV-A line, not a federal
   programme office** — and Maryland has already named that person: **an AI coordinator per local school
   system**.

🟡 **The limit, stated:** three federations, one of them (the US) known since pass 90. 🔴 **Quebec, Brazil's
states and India's states are untested**, and Brazil is the interesting one — it has a national curriculum
base as audited open data (`T11`) **and** 26 states, so the rule predicts state-level AI instruments there
that this KB has never looked for.

## T13 — 🆕 p94 The permissive supply for regulated assessment is the **evidence layer**, not the scorer

🟢 **This trend exists because `Gap 372` was stated too broadly for one pass and is now stated correctly.**

Pass 93: *"there is no production-grade permissive AES library in this industry"* — one 2★
Apache-by-reference research repo was the whole supply, for the activity the AI Act names high-risk most
explicitly. 🟢 **Pass 94 read the payloads and the picture inverted along a seam nobody had drawn:**

| layer | what a regulated deliverable needs it for | permissive supply |
|---|---|---|
| **the scorer** | producing a grade | 🔴 **absent.** The production code is AGPL-3.0 — `openedx/ease`, `openedx/edx-ora2` |
| **the validation and fairness harness** | 🟢 **the artefact the regulator and the appeal process actually consume** | 🟢 **present and mature** — `EducationalTestingService/rsmtool` (Apache-2.0, 2 916 commits), `skll` (BSD-3) |
| **open-response grading with LMS reach** | getting a grade back into the platform the client runs | 🟢 **`HASKI-RAK/NodeGrade`** (MIT, LTI 1.1/1.3, 421 commits) |
| **the explanation** | 🟢 Annex III owes the assessed person a reason | 🟢 the psychometric tier — BKT / IRT / CAT, all MIT or BSD (`T10`) |

🔵 **The commercial reading is the opposite of the obvious one.** The scorer is the part a client can buy
from a vendor, and the part that is cheapest to replace. 🟢 **The validity argument, the fairness analysis
and the explanation are the parts nobody sells as a product, that every regulated deployment needs, and
that are available under Apache and BSD from the house that runs TOEFL and the GRE.** 🔴 **Which is why
"we cannot do automated scoring, there is no open scorer" was the wrong conclusion**: the open supply
covers the defensible half, and the half it does not cover is the half with a market price.

🔴 **And a caution that belongs in this trend rather than a footnote.** The same publisher ships
**GPL-2.0** in `factor_analyzer` — a factor-analysis library of exactly the kind a scoring pipeline imports
without reading (`P975`). 🔵 **In this tier the licence audit is a per-dependency job, not a per-vendor
one.**

### 🟢 🆕 p95 amendment to T13 — the claim is unchanged in direction and three measurements stronger

🔴 **Pass 94 asserted that the research scoring supply was thin. Pass 95 probed it and it is worse than
thin — it is ungranted.** The three open-response candidates the literature names:

| candidate | claim | payload |
|---|---|---|
| [`edgresearch/code-automaticgrading-2022`](https://github.com/edgresearch/code-automaticgrading-2022) (**GradeAid**) | published ASAG framework, code released | 🔴 **CC BY-SA 4.0**, 20 130 B — **a content licence with a ShareAlike obligation, applied to software.** No patent or linking language; CC advises against CC for code |
| [`datalab912/RATASv1`](https://github.com/datalab912/RATASv1) | *"the authors publicly release all code"* | 🔴 **no licence payload in 8 filenames** |
| [`emorynlp/llm-grading`](https://github.com/emorynlp/llm-grading) | *"an open-source auto-grading toolkit"* | 🔴 **no licence payload in 8 filenames** |

🔴 **`P981`: "we publicly release our code" in a paper is not a grant** — and an ungranted repository is, by
copyright default, **all rights reserved**. 🔵 **Because this industry's scoring supply is overwhelmingly
academic, the defect is systematic**: the sentence that signals openness in a paper and the legal position
of the artefact point in opposite directions.

🟢 **So `T13` holds in its strong form.** The permissive supply for regulated open-response scoring is the
**validation** layer (`rsmtool` Apache-2.0, `skll` BSD-3); the **production** scoring code is copyleft
(`openedx/ease`, `openedx/edx-ora2`, AGPL-3.0); the **research** code is ungranted or CC-licensed.
**Score behind a service boundary; validate with Apache/BSD.**

🟢 **And one genuine addition at an adjacent layer, which `T13` must not be read as covering.**
[`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) is **BSD-3-Clause**, `v7.0.0`, UC
Berkeley, Canvas- and Gradescope-native. 🔴 **It grades code against tests, not constructed responses**, so
it leaves `Gap 372` exactly where it was. 🟢 **What it changes is that the automated-feedback layer's only
classroom-proven row is no longer AGPL-only** — which moves a programming-assessment deliverable from
*integrate across a service boundary* to *fork and own*.

## T14 — 🆕 p95 The curriculum mandates split by education LEVEL, and the higher-education limb is a different market

🟢 **Every curriculum mandate this KB has recorded until now binds schools.** China, Singapore, the UAE's
K→G12 programme, Mexico's Edomex reform, the EU's Article 4 literacy duty — **the buyer is a ministry of
education, the unit is a school system, and the procurement cycle is a national programme.**

🟢 **Pakistan's HEC notification (February 2026, effective academic session 2026) binds universities**: a
**3-credit AI course in every undergraduate and postgraduate degree**, public and private, deliverable as
an elective, interdisciplinary or supporting subject. 🔵 **That is the same regulatory instrument type
pointed at an entirely different market.**

| | the K-12 limb | 🆕 **the higher-education limb** |
|---|---|---|
| buyer | ministry / national programme office | 🟢 **the institution itself** — provost, registrar, faculty development |
| unit of sale | one programme, many schools | 🟢 **one institution, repeated** — and there are hundreds |
| procurement | public tender, multi-year | 🟢 **institutional budget, annual** |
| the artefact | curriculum, teacher training, content packaging | 🟢 **syllabus + LMS delivery + disclosure workflow + faculty training** |
| the platform | whatever the ministry runs | 🟢 **the university's own LMS — Moodle, Canvas, Sakai, OpenOLAT, Artemis** |
| examples here | China, Singapore, UAE, Edomex, EU Art. 4 | 🟢 **Pakistan (binding)**; India (in drafting); Quebec & Brazil (higher-ed frameworks) |

🟢 **Why this is a trend and not a single data point.** Three other jurisdictions in this KB already carry a
higher-education-specific instrument: **Quebec's `Cadre de référence` on deploying AI in higher education
(Aug 2025)**, **Brazil's CNE draft guidelines, which include a higher-education chapter (March 2026)**, and
**India's AICTE/UGC undergraduate AI curriculum, in drafting with Nasscom and a stated ~6-month horizon**.
🔵 **Pakistan is the first to make it binding, not the first to aim at the level.**

🟢 **And the recurring-revenue shape is in Pakistan's draft policy rather than its mandate.** The **August
2026 draft** asks universities to **write their own institutional rules**, **requires disclosure of AI
use**, **requires annual AI training for faculty, students and staff**, and **directs AI literacy into
curricula within two years**. 🔵 **A 3-credit course is one syllabus delivered once. "Annual training for
all staff" and "write your own policy" are deliverables that recur per institution per year** — which is
the difference between a content engagement and a retained one.

🔵 **What this changes in the shelf.** The K-12 limb pulled this KB toward curriculum data and content
packaging (`P91-G`, the `bncc-dev` rows, `Gap 367`'s missing K-5 curriculum). 🟢 **The higher-education limb
pulls toward the university platform tier this KB is already strongest in** — `Artemis` (MIT, with Iris,
Athena and Hyperion already built), `Sakai` (ECL-2.0), `OpenOLAT` (Apache-2.0) — **plus the disclosure and
assessment-integrity workflow the draft policy names.** 🟢 Costed as `P95-A` in `compose/patterns.md`.

🔴 **The honest limit.** Pakistan's mandate is **read at search-summary grade** from Pakistani press
(APP, The News, ProPakistani, Digital Pakistan) with consistent dates and content across outlets; **the HEC
notification itself was not read**, and the August draft is explicitly a **draft**. 🟡 **And a vocabulary
note: Pakistan is bucketed APAC here under this task's five-value region field**, which hides that it is a
South Asian market adjacent to India's, not an East Asian one.

## Instrument note carried forward

🟢 **`git ls-remote --symref` and `raw.githubusercontent.com` discriminate; `curl` on `github.com` and
`api.github.com` return 403 for real and invented slugs alike and must not be used.**
🆕 **Newly recorded: `WebFetch` on `https://github.com/topics/<t>` renders the page, its star counts and the
topic total, while `curl` on the identical URL is 403.** That is where star counts and topic denominators come
from.
🔴 🆕 **p93: the sandbox adds a second limit on top of the egress one — repository code cannot be
executed.** `compose/code/grant-ladder-v4/ladder.sh` could not be run, so this pass ran its *oracle map* by
hand and **printed each payload's title block rather than classifying it** (`P970`). 🔵 **Declining to
classify is the correct failure mode here; forking the shared classifier is the one `P237` forbids and the
one that cost pass 91 two platform licences.** Every row added this pass carries bytes, filename, ref and
SHA so v4 can re-derive it and contradict this pass on the record.
🟢 🆕 **p93 oracle addition: `WebFetch` on `https://github.com/<owner>/<repo>` renders star counts, fork
counts and the sidebar licence**, which is where this pass's ★ figures come from. 🔴 **And it exposed a
blind spot shared with the ladder** — the sidebar reports the **root** licence only, so
`bncc-dev/bncc-dados` reads *"MIT license"* while the data it exists to publish is CC BY 4.0 one directory
down (`P969`).

🔴 **Re-confirmed (`P944`/`P950`): the policy-source block is an EGRESS ALLOWLIST, not DNS.** Four primary
hosts needed this pass — `cbse.gov.in`, `digitaleducationcouncil.com`, `hepi.ac.uk`, `unu.edu` — returned
`000`/0 B under `curl` and `ENOTFOUND` under `WebFetch`. Not retried per host.
🆕 **p93 adds three to the blocked list:** `www.marketsandmarkets.com`, `bncc.dev` and `profy.com.br`, all
`ENOTFOUND` under `WebFetch`. 🟢 **The `bncc.dev` block cost nothing, because its repositories are on
GitHub and the payloads were read there directly** — but the `marketsandmarkets.com` block is why the
regional-versus-global arithmetic in `intel/market.md` cannot be closed against that firm's own global
figure. Figures from them are labelled
*search-summary* in `intel/market.md`.

*Prior pass content is preserved in git history at commit `306eb06` and earlier.*
