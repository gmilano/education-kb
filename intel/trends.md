---
industry: education
region: Global
updated: 2026-11-18
---

# Current trends — education

**Twenty-four trends** (**T24 added in `p901`** — path-dependent licences, the first trend in this file derived from repositories the SPDX channel refused to resolve at all; **T23 added in `p900`** — the first trend in this file derived from a
licence census of this base's *own unshelved backlog* rather than from search or from a
repository probe)

**Twenty trends** (**T20 added in `p898`**, the first trend in this file sourced from byte-level repository probes rather than search snippets) (the count in this line read *"sixteen"* through the addition of T17 and T18 and is corrected in **p897**), each with the evidence behind it and what it implies for delivery. **T19 added in p897**, from the licence re-read of every unresolved row. **T16 added in p895**, from four cohort measurements that only become one finding when read together. **T14 and T15 added in p894** — the first from the operative content of China's anthropomorphic-AI Measures, which this file had been carrying as a bare date; the second from four repository cohorts measured in a single batch, which is the only way the correlation it names becomes visible. Researched
2026-11-18; T9 added and T1/T3/T6 extended in **p890**, T10 added in **p891**, and **T11 added in
p892** from the India and Saudi Arabia legs — all the same day. Legal facts here were
sourced through search snippets with the source named — every non-GitHub host is blocked by this
session's network policy, so primary texts could not be byte-read. See the verification note in
`intel/market.md`.

## T1 — Regulation has moved from guidance to binding rules, and it regulates *use*, not existence

Across every region the question has shifted from "is AI allowed" to "under what oversight".
Oklahoma SB 1734 bars AI used solely for grading, discipline or promotion. Ohio districts must
have an AI framework by 1 July 2026. Korea's AI Basic Act is in force since 22 January 2026.
The EU AI Act is generally applicable since 2 August 2026. MultiState counts at least 25 US
states with enacted or introduced K-12 AI legislation, and **134 AI-in-education bills across
31 states in the 2026 session**.

**Three additions from pass p890 sharpen this considerably.** **Vietnam** now makes education
AI *statutorily* high-risk: Decision 33/2026/QD-TTg (effective 15 August 2026) lists 46
high-risk systems across six sectors with **education among them**, under the Law on AI
(134/2025/QH15) — existing education systems must comply by **1 September 2027**, new ones by
**1 March 2027**. **North Carolina** (Session Law 2026-41) requires a state model AI policy by
**31 December 2026** and local policies by **30 June 2027**. **California AB 1159** bars using
student data to train AI models outright. And in **Australia**, TEQSA has moved from an
educative to a **regulatory-led** posture in 2026, so the genAI action plans all 203 providers
submitted in 2024 are now inspected.

**Implication (revised).** The binding deadlines are no longer all in late 2027. The nearest is
**six weeks out** (North Carolina, 31 December 2026) and the first statutory education high-risk
clock outside Europe expires **1 March 2027** (Vietnam). California's rule is stronger than a
deadline — it forecloses a whole architecture. **Build retrieval-over-institutional-content with
no training feedback loop, and treat the policy layer as per-jurisdiction configuration rather
than a document.**

**Implication.** Oversight architecture is the product. A tutor without an audit trail and a
teacher-review path is unsellable to an institution in 2026, regardless of how good the model
is.

## T2 — The best open education agents are coming out of universities, not startups

Every institution-grade open education agent verified in this pass is academic: Artemis /
EduTelligence / Pyris (TU Munich, MIT), DeepTutor (HKU, Apache-2.0), OpenMAIC (Tsinghua, MIT),
OATutor (UC Berkeley, MIT), EduWork (ECNU, Mulan PSL v2). The commercial tutoring players
(Khanmigo, Duolingo, Microsoft Elevate) are closed.

**Implication.** The permissive, high-quality assets are academic and their authors want
implementation partners. This inverts the usual open-source posture: the studio is not
competing with these projects, it is the deployment arm they lack.

## T3 — The EU's high-risk deadline moved to December 2027, and that is a selling window

Regulation (EU) 2026/1744 postponed Annex III high-risk obligations for stand-alone education
systems from 2 August 2026 to **2 December 2027**. Transparency duties (Article 50) still apply
from August 2026, and the emotion-recognition ban in schools has been in force since February
2025.

**But one EU duty is already live and almost nobody is selling against it.** **Article 4, the
AI-literacy obligation, has applied since 2 February 2025**, binds **providers *and* deployers**,
is **not limited to high-risk systems** — a school using an ordinary chatbot is in scope — and
reaches staff and contractors operating AI on the organisation's behalf. The Commission's
position is that supervision and enforcement began **2 August 2026**. No education-specific
guidance on it has been issued by the Commission or any national authority that this pass could
find.

**p891 resolves p890's open question: the Digital Omnibus did rewrite Article 4, and it
softened it — but it did not repeal it.** Six independent secondary sources agree on the
following, and none dissents:

- Article 4 was **replaced, not removed**, by **Regulation (EU) 2026/1744** — the same
  instrument that moved the Annex III high-risk date. Published in the Official Journal
  **24 July 2026**, in force **27 July 2026**.
- The standard dropped. The duty to *ensure a sufficient level* of AI literacy became a duty to
  **take measures to support** it, and the amended text states expressly that it **does not
  require providers or deployers to guarantee any specific level of AI literacy of any
  individual**.
- The obligation itself has applied since **2 February 2025** and still binds **providers *and*
  deployers**, high-risk or not.
- Enforcement sits with **national market surveillance authorities** — not the AI Office — and
  began **2 August 2026**.
- A Council document of 13 March 2026 frames the amendment's purpose as reducing burden on
  deployers, especially smaller ones, while still promoting literacy.
- The same timeline defers **Article 14 (human oversight)** to **2 December 2027** alongside the
  rest of Annex III.

*Verification standing: multi-source agreement, not primary-verified. EUR-Lex and
`data.consilium.europa.eu` are blocked by this session's network policy. Confirm the amended
Article 4 text against the Official Journal before it goes in a client deck — but the "is it
still in force" question is now answered, and the answer is yes.*

**What the softening changes commercially — this is the load-bearing part.** The old reading
supported selling a *measurable competence* programme: assess staff, train to a level, certify.
That pitch is now weaker, because no specific level is required of any individual. What
replaces it is **demonstrable, proportionate, documented effort**: a literacy measure
appropriate to the institution's context and the systems it actually deploys, with evidence
that it was delivered. Narrower, cheaper, and easier to close — and the buyer is now a market
surveillance authority's idea of reasonableness, not a certification body's.

**Implication.** Institutions have a known deadline and now have time to comply properly —
which is exactly when conformity work gets funded. Treat admissions, assessment and proctoring
as high-risk engineering with a December 2027 date. **Verify the date against the regulation
text:** many sources still carry the superseded August 2026 figure, and this is the most
commonly mis-stated fact in the industry right now. **And do not wait for 2027 to sell:**
Article 4 is enforceable now, applies to every institution using any AI, and has no official
playbook — a staff AI-literacy programme with evidence of completion is a deliverable that can
be scoped this quarter, and it is the natural door-opener to the 2027 conformity work.

## T4 — Adoption has outrun governance, most measurably in LATAM

TALIS 2024: Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52% teacher AI use against an OECD
average of 36%. But in Brazil only 22% of administrators report school guidelines while 53%
use AI, and UNESCO IESALC finds 87% of universities using AI with 26% holding a formal strategy.

**Pass p890 adds the student side, and it is more extreme than the teacher side.** **PISA 2025**:
across the **13** Latin American and Caribbean countries assessed, **nine in ten 15-year-olds
have already used AI chatbots for schoolwork**. The **Digital Education Council's 2026 LATAM
survey**: **92% of students** across 29 institutions and **79% of faculty**. Meanwhile **CENIA**
finds **13 of 19** LAC countries do not teach early AI adoption in schools at all. So the
sequence is: near-universal student use, majority faculty use, minority institutional strategy,
and a curriculum that does not mention it.

**Implication.** The sales motion in high-adoption/low-governance markets is not "adopt AI" —
it is "govern the AI you are already using". Shorter cycle, visible pain, faster close.

## T5 — Agentic education is small, and analysts cannot agree whether it is growing

Research and Markets: $2.1B in 2026 at **4.5%** CAGR. Mordor: $2.37B in 2026 at **37.92%** to
$11.83B by 2031. Same segment, same year, an 8x disagreement on growth.

**Implication.** Do not build a client business case on a single analyst number. Build it on
the client's own cost base — graded submissions per term, support tickets per course, hours of
lecture transcription. Mordor's structural observation is the reliable part: tutoring is the
gateway purchase that seeds platform penetration.

## T6 — Sovereign and local inference is becoming a procurement requirement, not a preference

The European University Association's January 2026 report explicitly favours European LLMs.
EU data-residency expectations, plus the offline reality of rural deployment, push the same way.

**Two developments from pass p890 harden this from preference into policy.** In EMEA, a
**Council of the EU** document of **29 October 2026** (ST-14902-2026) presses digital
sovereignty and strategic autonomy in AI for education — the preference is now a Council
position, not a university association's opinion. And LATAM finally has its own instance:
**Latam-GPT** (CENIA, Chile) launched **10 February 2026** as an open model trained on Latin
American data, and **UNESCO's Santiago office signed a cooperation agreement with CENIA** in
late February 2026 naming Latam-GPT integration as an early milestone, intended to serve
Ministries of Education. Previously every sovereignty instance in this KB was European.

**Implication.** Self-hosted inference (`ollama`, `vllm`) behind a gateway (`litellm`) with a
local vector store (`qdrant`) should be the default architecture, with hosted APIs as the
exception that needs justifying. Keep the **model layer swappable** — that is what lets the same
build answer "European LLM" in EMEA and "Latam-GPT" in LATAM without re-architecture, and it is
why `litellm` sits in the design rather than a direct SDK call. This also happens to be what makes the offline/low-bandwidth
segment (Kolibri, Internet-in-a-Box, Project NOMAD) technically possible at all.

## T7 — Content-provenance labelling is now a dated legal requirement in APAC

India's amended IT Rules require prominent labels and provenance markers on AI-generated
content from **20 February 2026**. China's rules on labelling AI-generated content are in
force, alongside the amended Cybersecurity Law (1 January 2026) carrying its first AI clause.

**Implication.** Generated courseware, quiz items and feedback need provenance metadata
emitted at generation time. Retrofitting labels across an existing content library is far more
expensive than emitting them from the start.

## T8 — Stakeholder consent, not model quality, is what kills national deployments

South Korea rolled out AI-powered digital textbooks from 2025 and, after parental and teacher
backlash, reduced them to optional "educational material" status within a year. Separately,
Katy ISD banned generative AI chatbots for K-6.

**Implication.** The most expensive failure mode in this industry is social, not technical. Any
rollout plan above a single department needs a named teacher- and parent-consent workstream
with its own budget line. Korea is the case study to cite when a client wants to skip it.

## T9 — Procurement economics, not pedagogy, is becoming the blocker — and buyers have written the spec

**New in pass p890.** **Jisc**, with **Universities UK**, **GuildHE** and the **Association of
Colleges**, issued a joint statement asking AI suppliers for transparent pricing, demonstrable
value, meaningful institutional choice, protection of existing functionality, **granular usage
and cost controls**, interoperability, **data portability** and safeguards against **vendor
lock-in**. The driver is the shift from predictable per-seat licences to **usage-based pricing**,
which makes institutional budgeting impossible, compounded by institutions paying repeatedly for
overlapping AI capabilities embedded across several platforms. A related **Jisc/EAUC** report
found vendors seldom publish institution-level usage figures at all — universities cannot even
measure their own AI emissions.

**Why this is a trend and not a news item.** Every other trend in this file is about what
regulators require. This one is about what *buyers* require, it is written down, and it is
signed by the bodies that represent most of UK higher and further education. It is the closest
thing to a published RFP in this KB.

**Implication — and it is unusually concrete.** The deliverables are named for you:

1. **Per-institution, per-faculty, per-course usage and cost attribution**, exportable. Build it
   with `BerriAI/litellm` (MIT) for per-key budget caps plus an OpenTelemetry-native metering
   layer — **`traceloop/openllmetry` (Apache-2.0)** preferred, because OTel means the data lands
   in whatever stack the institution already runs, which *is* the portability answer.
   `Helicone/helicone` and `openlit/openlit` are Apache-2.0 alternatives.
   **Licence warning:** `langfuse/langfuse` is the largest option but its grant is split — MIT
   Expat core, separate enterprise licence on `ee/` paths, and the copyright now reads
   ClickHouse, Inc. See `repos/trending.md`.
2. **No-lock-in architecture as a contractual artefact**, not a slide: model layer behind
   `litellm`, content and embeddings in a store the client owns (`qdrant`), integration over
   **LTI 1.3** (`ltijs`) so the tool detaches from any one LMS.
3. **A cost model priced per learner-outcome, not per token** — because the buyer has just said
   in public that per-token exposure is the thing they will not sign.

Pricing transparency is now a differentiator a studio can actually win on, and it costs
engineering rather than research to deliver.

## T10 — Detection is being abandoned as an integrity control, and assessment redesign is what replaces it

The clearest evidence this pass is Canadian. A review of **six Canadian universities** found
that **every one of them declined to enable or endorse AI-detection tooling**, and privacy was
the stated reason at four. UBC cites a Privacy Impact Assessment; **Concordia bars staff and
faculty from using online AI detectors at all**, on provincial privacy grounds — sending
student work to a third-party detector is itself a disclosure. This is not a pedagogy argument
being lost; it is a **privacy-law argument being won**, which makes it durable.

It converges with three findings from other regions:

- **North America:** the shift in the practitioner literature is explicitly *from policing
  academic integrity toward reducing cognitive load*.
- **EMEA:** the Council of the EU's October 2026 conclusions call on member states to set
  policies on **academic integrity and plagiarism** — note that the instrument asked for is a
  *policy*, not a detector.
- **Middle East:** the UAE Ministry of Education's 2026 classroom guide bans AI **during exams
  and assessments** outright. The control is the assessment design and the invigilation rule,
  not a probability score on submitted text.

**Why detection loses.** Detectors produce an unfalsifiable probability, carry a known false-
positive bias against non-native writers, and — the decisive point — require shipping student
work to a processor, which is a data-protection event under FOIPPA/FIPPA in Canada, GDPR in
EMEA, and the student-data statutes now passing in US states (California AB 1159 bars using
student data to train models at all).

**Implication for delivery, and it is a large one.** An engagement pitched as "AI-integrity
detection" is selling into a control that institutional counsel is actively removing. The
fundable work is **assessment redesign**: process evidence over product evidence — drafts,
version history, oral defence, in-class supervised components, and rubrics that grade
reasoning rather than prose. That is build work (LMS workflow, submission instrumentation,
rubric services), not a licence resale, and it suits exactly the permissive stack this KB
tracks. See **P9** in `compose/patterns.md`.

**Caveat on the Canadian evidence:** the six-institution review is a secondary source; the
named institutional positions (UBC, Concordia) are the strongest part of it. The direction is
corroborated across four regions, the specific count is not primary-verified.

## T11 — AI literacy is becoming a statutory *curriculum* mandate, and teacher capacity is the binding constraint

**New in pass p892**, and it is the trend the two gap-closing legs (India, Saudi Arabia) made
visible. Every other trend in this file is about constraining AI *use*. This one is about
states compelling AI *teaching* — a different buyer, a different deliverable, and dates that
are mostly nearer than the conformity deadlines in T1 and T3.

| Jurisdiction | Mandate | From |
|---|---|---|
| **India** | NCERT/CBSE Computational Thinking + AI curriculum, **Classes III–VIII**, integrated into existing subjects; 15-hour SOAR module already in **18,000+ CBSE schools**; NCERT writing Grade 11–12 AI textbooks | **2026–27** |
| **Saudi Arabia** | AI units across public education; **50 further AI units across 22 revised subjects**; **240,000 teachers** in training under the Human Capability Development Program | 2025–26, expanding **2026–27** |
| **Vietnam** | **12 periods per class per year of AI content, grades 1–12** (Ministry of Education; distinct from its high-risk classification) | in force |
| **UAE** | Cabinet-approved AI curriculum across public *and* private schools (2 September 2026); start date contested across sources | 2025–26 / 2026 |
| **North Carolina** | Specified **professional development for teachers** | by **30 June 2028** |
| **EU** | Article 4 AI-literacy duty — staff and contractors, not students, but the same direction | live since 2 Feb 2025 |
| **Africa** | AU Continental Education Strategy 2026–2035 treats AI as cross-cutting; Ghana's strategy calls for primary-level coding; Kenya's curriculum review includes AI literacy | drafting / phased |

**What makes it a trend rather than a list.** Four of these were found in separate regional legs
run for unrelated reasons, and they converge on the same deliverable. The mandates are
**curriculum-shaped, not compliance-shaped**: a ministry has written or commissioned the
content, so the buyer is not asking for courseware. What every one of them lacks is the capacity
to deliver it to teachers.

**The constraint is explicit in the evidence, not inferred.** Saudi Arabia is funding 240,000
teacher trainings and has reached 60,000. India's own commentary makes the point plainly —
adding a subject to the curriculum is not the same as preparing teachers to teach it — and CBSE
schools additionally carry an infrastructure obligation for AI as a subject. North Carolina
legislated the teacher-development deadline separately from the policy deadline, which is a
legislature conceding the same thing.

**Implication — and it inverts this KB's usual sales motion.** T4's motion is *"govern the AI
you are already using"*; T3's is *"conform before the deadline"*. T11's is **"deliver the
programme the state has already funded"**. The buyer is a ministry or a board rather than an
institution, the content is given rather than authored, and the work is enablement, assessment
and evidence at national scale. It also travels: the same build answers India and Saudi Arabia
with the curriculum corpus and the language swapped, which is why `compose/patterns.md` **P10**
is written once rather than per-country.

**Two cautions.** First, **this is public-sector delivery** — procurement cycles, local-partner
requirements and political risk, not the quarter-length engagements T4 implies. Second,
**resist the temptation to sell a tutor into it.** The mandate is for teaching AI, and the
product the gap calls for is teacher enablement and evidence of coverage. A student-facing
tutor sold against a teacher-capacity mandate is the wrong deliverable answering the right
need, and every open tutor in `agents/top.md` is English- or Chinese-first anyway.


## T12 — An open education agent has acquired a third-party plugin ecosystem, which has not happened before

**The observation.** `amosblomqvist/learnharness` (AGPL-3.0) went from creation on **2026-10-16**
to **10,002 ★ on 2026-11-18** — 27 days. That alone is only a popularity fact. The structural
fact is what grew around it in the same window, all independently owned:

| Repo | Licence | ★ | What it is |
|---|---|---|---|
| https://github.com/kerr-mwv/learning-path-plugin | AGPL-3.0 | 12 | Plugin: build and follow a pedagogical learning path grounded in a canonical source |
| https://github.com/kkgosu/reasoned | AGPL-3.0 | 11 | Native **Android** learning app inspired by LearnHarness — AI lessons, practice, personal knowledge graph |
| https://github.com/tn-lorenz/awesome-learnharness | none | 7 | Community plugin and theme list |
| https://github.com/heohlee/learnharness-git | AGPL-3.0 | 6 | Back up and sync LearnHarness learning data with Git |
| https://github.com/808arc/meme-plugin | AGPL-3.0 | 2 | Turns LearnHarness concepts into memes |

**Why this is a trend and not a curiosity.** Every other agent in `agents/top.md` is a
destination: you adopt DeepTutor, or OpenMAIC, or Artemis. **None of them has third parties
building on top of it.** DeepTutor has 60,258 ★ and no plugin ecosystem. LearnHarness has a
sixth of the stars and five independent extensions, a reimplementation on another platform, and
an awesome-list — within a month. That is the difference between a product people use and a
**platform people build on**, and in open source the second is a far stronger durability signal
than stars.

**Three things follow for an engagement.**

1. **The extension points are where the standard forms.** The plugin set is already clustering
   around the same three concerns — pedagogical path construction, persistence/portability of
   the learner's knowledge graph, and an alternative client. Those are exactly the seams a
   client will need. If a platform-shaped standard emerges in open education tooling in 2027,
   this is currently the most likely place it comes from.
2. **The licence forecloses the obvious play.** LearnHarness and every substantial plugin are
   **AGPL-3.0**. You cannot take this into a closed client derivative. What you *can* do is
   read it as the reference design for **learner-state modelling** — probe before teaching,
   dependency-map to the goal, persist the model across sessions — which is the capability
   almost every permissive tutor in `agents/top.md` lacks, and which is reimplementable from
   the design rather than the code.
3. **It is unproven as pedagogy.** There is no published learning-outcome study and users
   report being tested before being taught. **The ecosystem is evidence of developer
   enthusiasm, not of learning.** Do not present velocity as efficacy — that conflation is the
   industry's standing failure (see the ESSA-tier finding in `intel/market.md`).

**Watch condition.** Two signals would promote this from "interesting" to "plan around it":
a plugin crossing **100 ★**, or any plugin appearing under a **permissive** licence, which
would mean the ecosystem is routing around the AGPL core. Neither has happened. Re-check
weekly — at this growth rate the monthly cadence this KB uses for stars is too slow for
this one repo.

## T13 — The LMS is becoming an agent tool surface via MCP, and Moodle got there through the community

**The observation.** Until p893 this KB tracked exactly one LMS-to-agent bridge pattern — two
`canvas-mcp` servers. A discovery leg found that **Moodle, the most-installed LMS on earth, now
has at least seven independent MCP servers**, none of them from Moodle HQ:

| Repo | Licence | ★ | Access posture |
|---|---|---|---|
| https://github.com/Faixiang/Moodle-MCP | MIT | 208 | **Read-only**, zero-dependency, 10-language README |
| https://github.com/loyaniu/moodle-mcp | **none** | 58 | — (unusable, no grant) |
| https://github.com/peancor/moodle-mcp-server | MIT | 45 | The original (2025-03), now idle since 2026-02 |
| https://github.com/G36maid/moodle-mcp | MIT | 30 | **Read-write** — courses, assignments, forums, grades |
| https://github.com/onbirdev/moodle-webservice_mcp | **none** | 19 | A Moodle *plugin* implementing MCP server-side; pushed 2026-11-18 |
| https://github.com/MarcosNahuel/moodle-mcp | MIT | 1 | Write path with idempotency guarantees |
| https://github.com/stojandev/moodle-downloader-mcp | MIT | 0 | Bulk export for offline/agent use |

Open edX has its own, **`blend-ed/openedx-mcp`** (AGPL-3.0) plus a Tutor plugin — announced via
the official Open edX blog in September 2026 but **owned by a vendor org, not the foundation**.

**What this changes.** The KB's structural rule has been *integrate over LTI 1.3 and your tool
stays a separate work*. **MCP is now a second such seam, and it is the better one for agents.**
LTI ships your tool into the LMS; MCP exposes the LMS to your agent. They are complementary and
a serious build will use both — LTI for the user-facing surface, MCP for the agent's reach into
coursework, deadlines and grades.

**The governance point is the sellable one.** The read-only/read-write split is already explicit
across two MIT servers from different authors, which means a client can run a **genuinely
read-only pilot** against real coursework and graduate to write scope as a deliberate, separate
decision. That maps onto FERPA and onto the EU's assessment-related high-risk classification
far more cleanly than a single server with a permissions flag. And the caution travels with it:
these servers typically run on the user's machine with that user's API token, so **the agent
inherits every permission the human has**. Scope the token, do not scope the prompt.

**The absence worth naming: Moodle HQ has published no MCP server.** It shipped `wiki-rag`
(BSD-3-Clause) for its own documentation but has left the LMS-to-agent bridge entirely to the
community, where three of the seven servers have no licence at all. **For a client standardising
on Moodle this is a real risk and a real opening** — first-party-grade MCP for Moodle, built to
the organisation's conventions, is unclaimed work.

## T14 — Affective design is now a regulated feature in China, and the carve-out for education is conditional on *not* doing the thing that drives retention

**Added p894.** China's **Interim Measures for the Administration of Anthropomorphic AI
Interaction Services** (reported as **CAC Order No. 21**, issued **10 April 2026** by five
agencies, **in force 15 July 2026**) regulate services that provide *sustained emotional
interaction through a simulated human personality*. This KB has carried the effective date since
p890 and none of the content; the content is what matters.

**Where the Measures apply, the obligations are product-defining**, and several bite hardest on
education's user base: **virtual-partner and virtual-relative services may not be offered to
minors at all**; **guardian consent under 14**; a **minor mode** with time limits, real-world
reminders and guardian risk alerts; **age verification with an appeal channel**; a prohibition on
**inducing emotional dependence or addiction that damages real-world relationships**;
machine-disclosure reminders; mandatory intervention on a self-harm signal; and **algorithm
filing plus security assessment** before launch.

**Education is listed outside scope — and the listing is not a sector exemption.** Law-firm
analysis puts education alongside intelligent customer service, knowledge Q&A, work assistants
and scientific research as excluded (Bird & Bird); a second analysis frames the exclusion as
covering education and learning services **that lack continuous emotional interaction**
(Geopolitechs); a third notes the Measures **define neither "continuity" nor "emotional
interaction"** (Lexology). The test is behavioural, so the sector label settles nothing.

**Why this is a trend and not a compliance footnote.** The whole industry is moving toward
affective engagement — persistent named tutors, rapport, streaks, companion framing — because it
is what retains learners, and **China is the single largest producer of open education agents in
the world** (`DeepTutor`, 60,274 ★; `OpenMAIC`, 43,878 ★; `EduAgent`; `ECNU EduWork`;
`TeachMeCoding`). The jurisdiction supplying the category's best open source is the jurisdiction
that has made its most effective retention mechanic a regulated activity when aimed at children.

**What to do about it.** For a China-market education product, design **persona-stateless**:
hold pedagogical persistence in the learner model, not in a character; disclose the machine on
every surface; omit affect simulation and dependency loops; and band by age by construction, as
`Zenglian990/AI_Tutor_Release` already does. **The architecture that keeps you out of scope is
also the architecture the UAE's under-13 prohibition and several US state statutes require**, so
it is a single build, not a China tax. **Watch condition:** any CAC guidance, enforcement action
or published definition of "continuity" that places a tutoring product inside scope — that would
move this from a design constraint to a market-entry gate.

**Channel caveat.** All sources are secondary (law-firm guides and policy analysis); the CAC text
is blocked by this session's network policy, and **no source addressed a tutoring product
specifically.** Confirm scope with counsel before a China engagement.

## T15 — Open source has built least where regulation has decided most, and the correlation is now measured rather than asserted

**Added p894**, from four cohorts measured in one batch on one day — which is the only way this
trend is visible, because each cohort on its own reads as a small sad category.

| Use case | Regulatory status | Open-source supply (measured 2026-11-18) |
|---|---|---|
| Tutoring / content generation | **largely unregulated** as to the system itself | **60,274 ★** ceiling (`DeepTutor`); 34 agents on this KB's shelf |
| LMS-to-agent integration | unregulated | **208 ★** ceiling across seven MCP servers; permissive |
| **Automated grading** | **EU Annex III high-risk**; Vietnam high-risk list; Oklahoma and Maryland human-oversight rules | **0 ★ ceiling across seven repos; three carry no licence** |
| **Special education / accommodation** | **IDEA / Section 504 / ADA Title II**, statutory in the US; India's RPwD Act 2016 | **1 ★ ceiling across four repos; half unlicensed or AGPL** |
| **Admissions and financial-aid decisioning** | **EU Annex III high-risk**; restricted under several US state laws | **nothing — no repository found in any pass** |
| Registrarial scheduling | unregulated | **360 ★**, Apache-2.0, actively maintained (`UniTime`) |

**The pattern is monotonic across six rows: the more a use case is regulated, the less open
source exists for it.** The causal story is not mysterious — liability, procurement review,
domain expertise and the need for an auditable appeal path are exactly what volunteers and
weekend projects cannot supply, and they are what a regulator requires. **But the commercial
reading is the useful one, and it is the inverse of how an open-source-first studio usually
reasons.** The crowded categories are crowded *because* they are cheap to enter and nobody has
to defend them; the empty categories are empty *because* entry requires the thing a consultancy
sells.

**Consequences for how an engagement is scoped.** Where regulation is heavy, **there is nothing
to adopt and the regulation is the specification** — grading, accommodation and financial-aid
decisioning are builds, and the conformity work *is* the product rather than a tax on it. Where
regulation is light, **do not build**: compose, integrate and spend the budget on the governance
tier instead (`compose/patterns.md` **P2**, **P11**). The two design ideas worth carrying out of
the empty categories both came from 0 ★ repositories and both already sit in this KB's patterns:
**confine the LLM to evidence extraction and keep scoring deterministic**, and **anchor evidence
per criterion with a separate regrade path** — the second is what makes an appeal procedure
possible, which is precisely what Annex III demands.

**Watch condition:** any repository in the grading or accommodation rows crossing **100 ★** with
a permissive licence. That would mean the correlation is breaking, and the build-vs-adopt advice
for the most valuable categories in this industry would have to be rewritten.

## T16 — Published open education AI and deployable open education AI are two different
populations, and the published one is systematically unlicensed (new p895)

Across four cohorts this KB has now measured in a batch, a pattern holds that matters more for
procurement than any star count: **the repositories attached to papers, conferences and course
capstones are overwhelmingly unlicensed, and the repositories that are actually deployed are
overwhelmingly permissive.** They barely overlap.

| Cohort (measured) | Population | Licence reality |
|---|---|---|
| African-curriculum agents, p895 (`WAEC`/`KCSE`/`BECE`/`CAPS` channels) | ~1 ★ ceiling | Almost all **no licence**, including the 223 ★ `aloc-endpoints` |
| ACL AfricaNLP 2026's EduNaija tutor, p895 | 1 ★ | **No licence** on 8 candidate paths; idle 11 months |
| Automated grading, p894 | all **0 ★** | **3 of 7 no licence**, one GPL-3.0 |
| Special education / IEP, p894 | **1 ★** ceiling | Half **unlicensed or AGPL** |
| Deployed platforms (`elimu-ai`, `kolibri`, `oppia`, `Artemis`, `UniTime`) | 41–360 ★, fork-heavy, pushed this week | **MIT / Apache-2.0**, byte-verified |

**Why this happens is structural, not careless.** A paper's artefact is evidence for a claim;
its author's incentive ends at publication, and adding a licence is a step nobody's career
requires. A deployed platform cannot be installed by a ministry or a school district without
one. **So licence presence is a proxy for deployment intent** — and a better one than stars,
which measure discovery.

**Three consequences for delivery.**

1. **A citation is not a supply chain.** The strongest-sounding regional signal — a
   peer-reviewed agent built for the exact curriculum a client teaches — can be legally
   unusable and technically a prototype at the same time. p895 found precisely this: the
   EduNaija paper is real, and the code behind it has no licence, no evaluation beyond
   *"design-based"*, and a web-search grounding that fails in the low-connectivity setting it
   targets. **Read the artefact before you cite the venue.**
2. **In an under-served region, the agent tier is studio IP by default.** Not as a
   positioning choice — as an arithmetic consequence of there being nothing licensed to adopt.
   That raises the defensible-IP share of such an engagement and should raise its price.
3. **Licence-read the cohort before you scope, not after.** Eight candidate paths
   (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` × `main`/`master`) against
   `raw.githubusercontent.com` costs seconds and has repeatedly changed this KB's verdict on a
   whole category. **It is the cheapest high-value check in this entire knowledge base.**

**Signal to watch:** whether any funder attaches a licence requirement to education-AI research
output. Google's Fab AI programme (Kenya/Ghana/South Africa) states an intent to release
datasets, evaluation suites and **open-source models** publicly — if that commitment lands with
an actual OSI licence, it would be the first mechanism to merge these two populations. Tracked
in `intel/market.md`.

## T17 — The copyleft platforms publish their extension points, design systems and mobile clients under *permissive* licences, and that is a third integration route

**New in `p896`, and it emerged from a licence sort rather than a search.** This KB's first
structural fact is that the platforms clients run are copyleft (Moodle GPL-3.0, Open edX
AGPL-3.0, Canvas AGPL-3.0) while the tooling around them is permissive, and the standing advice
is to integrate over **LTI 1.3** or **MCP** so your work stays a separate work. Restoring 34
rows to `repos/foundations.md` and sorting them by licence shows a route the advice misses: the
platform vendors themselves ship the parts you extend under **Apache-2.0 or MIT**.

| Platform (server) | First-party permissive satellites |
|---|---|
| Moodle — **GPL-3.0** | `moodlehq/moodleapp` **Apache-2.0**, 1,007 ★ |
| Open edX — **AGPL-3.0** | `XBlock` **Apache-2.0** (471 ★), `xblock-sdk`, `paragon` **Apache-2.0** (141 ★), `openedx-app-android` / `-ios` **Apache-2.0**, `openedx-aspects` **Apache-2.0** |
| Canvas — **AGPL-3.0** | `instructure/instructure-ui` **MIT** (487 ★), `common-cartridge-viewer` **MIT** (95 ★) |
| H5P host library — **GPL-3.0** | every content type **MIT**: `h5p-interactive-video` (267 ★), `h5p-cli` (79 ★), `h5p-course-presentation`, `h5p-audio-recorder`, `h5p-speak-the-words` |

🔵 **Why it matters commercially.** The licence conversation in an education engagement usually
ends at "the client runs an AGPL platform, so our work must stay at arm's length." That is true
of the *server*. It is not true of the **component, the design system, the mobile client or the
analytics tier**, each of which the platform's own maintainers publish permissively. A branded,
closed mobile experience over a client's existing Moodle is a **supported architecture**, not a
workaround — and `openedx/XBlock` being Apache-2.0 means a studio can ship a proprietary
learning component into an AGPL LMS without a derivative-work argument.

🟡 **Two cautions.** First, the asymmetry is per-artefact, so it has to be verified per repo, not
assumed per vendor. Second, it runs the other way for *content*: curriculum data arrives under
ODbL and content applications under GPL (see `verticals/solutions.md`). Permissive client,
copyleft server, copyleft content — three licence classes in one engagement.

**Watch condition:** if a platform relicenses a satellite toward its server's licence, this route
closes for that platform. Re-run the licence sort on the satellites each quarter.

## T18 — A free, state-backed AI education platform is being exported into the emerging markets a studio sells into, while public support for banning AI in schools *rises*

**New in `p896`.** Two movements that look unrelated and are not.

🟢 **Supply.** At the **World Digital Education Conference (Hangzhou, May 2026)** China launched a
**global AI education service platform**, extending *Smart Education of China* to roughly **220
countries and regions**. This KB already records (**T6**) that open education agents originate
from East-Asian and European universities and that every other region localises them. A free,
state-funded platform aimed at the same markets changes the **baseline a paid offer has to
beat** in exactly the regions — LATAM, Africa, South and Southeast Asia — where this KB's
regional work found the most demand and the least domestic supply.

🔴 **Consent.** In the same window, Ipsos finds support for **banning** AI in education *rising*
across APAC: **Japan 21% → 29%**, **Australia 47% → 52%** (a majority), **South Korea 27% →
31%**. Canada's higher-education sector has broadly refused AI-detection tooling on privacy
grounds (`intel/market.md`), and the EU's emotion-recognition prohibition has been in force since
February 2025.

🔵 **The read.** Adoption momentum and public consent are moving in **opposite** directions, and a
free platform does not fix consent — it raises the volume of deployed AI that consent has to
cover. The defensible studio position is therefore **not** cheaper delivery, which loses to free,
but **the auditable, consent-bearing layer on top**: provenance, oversight records, opt-out
handling and published outcome evidence (**P7**, **P9**). That is also the one thing an exported
national platform structurally cannot supply to a foreign ministry.

**Watch condition:** a LATAM or African ministry announcing adoption of the exported platform.
That converts this from a pricing pressure into a named integration opportunity.

## T19 — Published licence metadata is wrong often enough to be a procurement risk, and the errors run *both* ways

This is the trend with the shortest path to money, because it is the one that decides whether a
client can keep what a studio builds. **Seven repositories carried on this KB's shelves with an
unresolved licence were byte-read in p897. Five were wrong as recorded, and the errors did not
share a direction.**

🔴 **p899 escalated this trend from "third parties get licences wrong" to "this KB got one
wrong, in the expensive direction".** Every prior case above was an error that cost a *missed
opportunity* — a permissive repo recorded as unclear, a copyleft one the SPDX matcher could not
read. **The PrairieLearn row is the first that would have cost a client money**: a studio reading
`MIT · Permissive` and building an AI assessment tier on `apps/course-agent/` would have shipped
subscription-gated code into production and signed the client's modifications over to a third
party. 🔵 **The structural lesson is about what survives review: an error that looks permissive
is never challenged, because nobody audits good news.** The mechanical catch — *a claimed MIT or
BSD over a licence file larger than ~5 KB must be re-read* — is `899-G3`, and it would have
caught this one on file size alone (**37,237 B**).

| Source of the error | Case | Recorded | Actual |
|---|---|---|---|
| **Popular comparison sites** | **Frappe LMS** — several 2026 *"best open-source LMS"* round-ups list it **MIT** | MIT (third-party) | 🔴 **AGPL-3.0**, 33,893 B of verbatim text. The MIT belongs to `frappe/frappe`, the **framework** |
| **Detector blind spot (directory)** | **openSIS Classic**, 351 ★ | "none declared", *"get written clarification"* | 🔴 **GPL-2.0** at `docs/License.txt`; the README links it |
| **Detector blind spot (filename)** | **Moodle App**, 1,006 ★ | `NO-LICENSE-FILE` | 🟢 **Apache-2.0** at `COPYING.txt` — and *not* Moodle core's GPL-3.0 |
| **Over-cautious internal reading** | **Open-TutorAi CE**, 118 ★ | `OTHER` | 🟢 **BSD-3-Clause, verbatim** — the permissive SPDX was right all along |
| **Declaration without text** | **Frappe Education**, 714 ★ | `NOASSERTION` | 🔴 **GPL-3.0**, declared in a **19-byte** file reading only `License: GNU GPL V3` |
| 🔴 **This KB's own shelf, p899** | **PrairieLearn**, 533 ★ | **`MIT` · *"Permissive"*** — published in `repos/foundations.md` | 🔴 **AGPL-3.0 Community Edition + a PROPRIETARY Enterprise Edition covering `apps/course-agent/`** — the AI tier. Production use of EE requires a paid subscription **and the licence assigns your modifications to PrairieLearn, Inc.** |
| **Source-available masquerade, p899** | **Advising App**, 339 ★ | `NOASSERTION` | 🔴 **Elastic License 2.0** — not open source; forbids managed-service provision |
| **Content licence on a code shelf, p899** | **cn-math-taxonomy**, 8,508 ★ | `NOASSERTION` | 🔴 **CC BY-NC 4.0** — NonCommercial, bars client work outright |

**Why both directions matter.** The familiar failure is a copyleft project being sold as
permissive — Frappe LMS is exactly that, and AGPL-3.0 is **network-triggered**, so merely hosting
it for a client's students is a distribution event. But the opposite error has a real cost too:
**Open-TutorAi** sat unusable on a shelf for passes because a permissive, verbatim BSD-3-Clause
grant had been demoted to `OTHER`, and **openSIS** carried a *"do not ship without written
clarification"* warning for a licence that was in the repository the whole time. Pessimism is not
free: it discards usable permissive options, which in education is the scarce category.

**Three structural causes, all of which produce silent errors:**

1. **SPDX detectors classify the root only.** openSIS keeps its grant one directory down and is
   therefore reported `NONE` — indistinguishable, in any table, from genuinely unlicensed code.
2. **A licence can be *named* without being *reproduced*.** A 19-byte `license.txt` defeats every
   template matcher, so a clearly-intended GPL-3.0 reads as "unknown".
3. **Comparison content inherits the org's most famous licence.** Frappe is "the MIT low-code
   framework", so its LMS gets written up as MIT. The same mechanism will mislabel any
   permissively-licensed vendor's copyleft products.

**What to do with it.** Treat a licence as unknown until its bytes are read, probe the **`docs/`,
`legal/` and `LICENSES/` directories** as well as the root, and never let a secondary comparison
page be the evidence for a licence claim in a client deliverable. On this KB's own numbers the
base rate of error in unresolved rows was **5 of 7** — high enough that byte-reading is cheaper
than the first conversation with a client's counsel. See `repos/trending.md` (p897) for the full
measurements and `repos/foundations.md` for the corrected rows.

## T20 — Vernacular education agents are appearing, and they are *not* translations of English ones — the native language is in the data contract

**Added `p898`**, from byte-level README probes rather than search snippets.

**The measurement.** A ten-repository origin probe (method and full table in
[`agents/trending.md`](../agents/trending.md), `p898`) placed **three repositories by README script
and lexicon**: two MIT entrants in APAC and one unlicensed Chinese-language repo. The seven others
have English READMEs and are carried `Global` because the instrument could not place them.

🔵 **The finding is not "some repos are in other languages". It is *where* the language sits.**

- [`brian901106/japanese-tutor-mugi`](https://github.com/brian901106/japanese-tutor-mugi) (MIT, 105 ★)
  is a **Chinese-language interface teaching Japanese conversation**. The tutor's UI language, the
  target language and English are three different things. Its LLM contract returns **JSON Schema**
  output in which the **Japanese line and the Chinese hint are separate fields**, streamed by
  partial-JSON parsing.
- [`itsme-ganzu/belajar-ngoding-byGanzu`](https://github.com/itsme-ganzu/belajar-ngoding-byGanzu)
  (MIT, 66 ★) teaches Python **in Bahasa Indonesia**, with the tutor drilling reasoning rather than
  supplying answers.

🔴 **Why "it's just localisation" is the wrong read, and the expensive one.** A localised product
puts language in the **presentation layer** — strings come out of a resource bundle and the model
reasons in English underneath. `japanese-tutor-mugi` puts it in the **schema**: target-language
content and native-language scaffolding are distinct typed fields that the model must fill
separately, so the pedagogical relationship between the two languages is enforced by the data
contract rather than by the prompt. **You cannot retrofit that by translating an English tutor.**
Any second-language or vernacular-medium tutor built on a single free-text response field has
already lost the distinction, and recovering it is a schema change, not a translation pass.

🔵 **Why it shows up in APAC first, and what that predicts.** The regions where instruction is
routinely delivered in a language that is neither English nor the language being taught are
precisely where this contract is forced. Indonesia alone is the **fourth-largest school system in the
world**. The same structure is latent in LATAM (Portuguese- and Spanish-medium instruction) and
across Africa — and this KB has verified **one** LATAM row of this kind
([`CaioCastro1/usp-mcp`](https://github.com/CaioCastro1/usp-mcp), MIT, Portuguese) and **no** new
LATAM-origin supply in this window.

**What it implies for delivery.**

1. 🟢 **Treat the separate-fields contract as a reusable design, not a repo to adopt.** Both repos
   are small and young; neither is substrate. The schema is the transferable asset, and it is MIT in
   both cases, so it can be read and reimplemented freely.
2. 🔴 **Scope vernacular work as a data-contract decision at design time.** If a client's engagement
   is vernacular-medium, the schema question has to be settled before a tutor tier is built, because
   it is not a late-stage localisation task.
3. 🟡 **Expect the supply to stay small.** These are individual-scale projects, not institutional
   releases — consistent with **T16**'s split between *published* and *deployable* open education AI.
   They are evidence of where demand is surfacing, not of a market you can buy into.

🔴 **Limit of the instrument, stated.** README language is a **proxy** for origin, and it
under-detects **EMEA specifically**, because European projects publish in English. A `Global` row in
this leg is decent evidence of "not APAC" and weak evidence of "not EMEA".

## T21 — The open grading tier is mature, permissive and university-built — and the licence traps are concentrated in the *AI* layer bolted onto it

**Measured p899, by name rather than by keyword rank.** The deterministic grading substrate a
client needs is already built, already permissive, and already maintained by universities:
**`Submitty`** (BSD-3-Clause, 807 ★, RPI, twelve years old, pushed today), **`jupyter/nbgrader`**
(BSD-3-Clause, 1,370 ★), **`ucbds-infra/otter-grader`** (BSD-3-Clause, 162 ★, UC Berkeley),
**`autolab/Autolab`** + **`Tango`** (Apache-2.0, CMU), **`webtech-network/autograder`**
(Apache-2.0). **Four of the five carry no copyleft and no patent clause at all.**

🔴 **The encumbrance is not in the grader. It is in the AI.** The one system in the category with
a commercial model — PrairieLearn — is AGPL for the Community Edition and **proprietary
Enterprise Edition specifically for `apps/course-agent/`**, the agent tier. The same shape
appears at `canyongbs/advisingapp` (Elastic-2.0, an **AI** advising assistant) and in the Open
edX estate, where the platform is AGPL and the **first-party AI extension point**
(`openedx-ai-extensions`) is AGPL too.

🔵 **Read as a market signal, this is unambiguous.** Open source has commoditised *assessment
mechanics* and is actively fencing off *assessment intelligence*. **That is precisely the layer a
studio sells**, and it means the build-vs-adopt line in an education engagement now falls between
the grader and the agent, not around the platform. The defensible architecture — AI assist on the
manual tier, deterministic rubric service untouched underneath — is also the one that survives
FERPA, several US state statutes and EU Annex III. See `compose/patterns.md` **P13**.

## T22 — Open education agents are differentiating on *delivery surface*, not on model capability

Across the eighteen agents verified in p899, the distinguishing claim is almost never "a better
model". It is **where the agent meets the learner**, and every variant answers a constraint that
is regulatory, economic or infrastructural rather than technical:

| Surface | Agent | The constraint it answers |
|---|---|---|
| **WhatsApp, voice notes, no app** | `Orenda-Project/rumi-platform` (Apache-2.0) | **Zero device provisioning and zero training.** 15 languages incl. a full Indian-language suite and Pakistan's regional languages |
| **Pen and paper, deliberately off-screen** | `nichochar/ari` (MIT, 222 ★) | Screen-time rules and parental-consent regimes |
| **Local-first inference** | `helixnow/deep-student` (AGPL), `artcc/freelingo` (AGPL), `zhangl1001/civil-ai` (MIT) | **EMEA sovereignty procurement and California AB 1159** — no data-processing argument needed |
| **Inside the LMS over MCP** | `Faixiang/Moodle-MCP`, `G36maid/moodle-mcp`, `canvas-mcp` ×2 | No migration; the institution's system of record is unchanged |
| **Inside a coding agent, as a skill** | `book-to-skill` (38,369 ★), `universal-examprep-skill`, `PAIDEIA`, `claudemy` | **No deployment at all** — the runtime is already on the learner's machine |
| **Age-banded by construction** | `Zenglian990/AI_Tutor_Release` (K-9), `SimonsTang/feifei-companion` (K-12) | UAE under-13 prohibition; US state statutes |

🔵 **Why this matters for scoping.** The highest-leverage question in an education engagement is
no longer "which model" — the open agents mostly delegate that to whatever the client supplies.
It is **"what surface does this population already have?"** In LATAM and South Asia that answer is
WhatsApp; in a sovereign EMEA ministry it is a local model on institutional hardware; in North
American higher ed it is the LMS the registrar already runs. 🔴 **An engagement that picks the
surface last has already constrained its own addressable population**, and the `rumi` case shows
the ceiling: it is the only agent in this KB that reaches a teacher with **no device
provisioning whatsoever**, and it has 25 ★ — the market has not yet priced this axis.

## T23 — Education's permissive supply is real but **unaddressable**: a third of it carries no readable grant, and a meaningful share is invisible to the index everyone searches with

**The evidence.** p900 measured 300 addresses this KB had logged from its own research and
never shelved — the largest licence census this base has run on its backlog
([record](../evidence/ledger-measured.2026-11-18-p900.tsv)). Two numbers matter and they point
in opposite directions.

**The good one: 49.2% is permissive** — MIT 76, Apache-2.0 43, BSD 3, ISC 1, out of 250 that
resolve. Education's open supply skews *permissive*, against this file's own long-standing
framing that the category is dominated by copyleft. **That framing is true of the deployable
platforms (Moodle, Open edX, Canvas) and false of the libraries and agents around them**, and
the distinction decides what a studio can keep.

**The bad one: 36.4% has no readable grant** — 61 `NOASSERTION` plus 30 with no licence at all.
🔴 **And SPDX is not reliable where it does answer:** `p897` byte-read seven unresolved rows and
**five were wrong as recorded**; `p899` found `PrairieLearn` published here as MIT when its AI
tier is proprietary. So the real cost of adopting from this supply is not discovery — it is **a
licence byte-read per candidate**, and that is why 36 of 40 top backlog rows sat unabsorbed for
passes.

**The part that is not about licences at all.** 🔴 **Of 50 addresses that `search/repositories`
reported as non-existent, 22 (44%) resolve on `raw.githubusercontent.com`** — four as
rename/transfer redirects, the rest simply missing from the search index. Among the unindexed:
**MIT Open Learning's production tutor backend, a zero-dependency QTI 3 scoring engine, and the
only permissive Arabic education model this KB has found.** 🔵 **Three of the most
institutionally credible assets in this file's whole domain are unreachable through the ranked
search everyone uses to survey a market** — including, until this pass, this KB.

**Implication for delivery.** Two concrete consequences. (1) **Budget a licence read into
selection, not into legal review** — at 36.4% no-grant and a measured SPDX error rate, a
shortlist assembled from badges is not a shortlist. (2) **Do not conclude a capability is
missing from a market because search returns nothing.** p894 recorded automated grading as *"a
category with nothing in it"*; p899 found 2,400 ★ of permissive grading software. The instrument
was wrong, not the market. **Where a client asks "is there anything open for X", the defensible
answer requires a second channel.**

## Trends we looked for and could not substantiate

- **Measured learning-outcome gains from AI.** The widely circulated figures ("42% improvement
  in learning outcomes", "54% higher test scores") trace to secondary blogs with no primary
  study. We found no credible primary evidence of learning gains at scale. This is a real
  evidentiary hole, and it is why the measurement tier in T3/`compose/patterns.md` matters.
- ~~**A November 2026 education-agent launch.**~~ **Overturned in p893, and not marginally.**
  Three passes concluded nothing had launched. A repository-discovery leg found
  **`amosblomqvist/learnharness`** — **AGPL-3.0, 10,002 ★, created 2026-10-16**, pushed
  2026-11-12 — now the **third-largest open education agent in existence** behind only DeepTutor
  and OpenMAIC. It was missed because it is a *desktop learning harness*, not an LMS plug-in or
  a tutor service, and the earlier legs searched for tutors. **Method lesson, and it is the
  third of this shape in four passes:** p892 learned that cohort findings need the cohort
  re-enumerated; p893 learns that **"nothing launched" is only ever a statement about the
  queries you ran.** A negative finding about an entire category needs the category
  re-enumerated by independent search terms before it is reported as fact. See **T12**.
- **Traction for the "tutor as an agent skill" form.** Measured again in p890: the whole cohort
  tops out at **118 ★** and not one member gained a star since the previous measurement. The
  form is real and the time-to-pilot argument holds, but it has no adoption. Demo material, not
  roadmap material.
- **Vendor market-share data in any region.** Market size exists; share does not.
- ~~**Japanese AI-in-education policy.**~~ **Resolved in p890 with a negative answer:** Japan's
  AI law is promotion-focused with voluntary guidelines and there is **no education-specific
  statute or classroom regime**. Confirmed absence, which is why Japan is the lowest-friction
  APAC pilot geography.
- ~~**Any education-specific guidance on EU AI Act Article 4.**~~ **Half-resolved in p893, and
  the half matters.** The **AILit Framework**, launched **19 June 2026** by the **European
  Commission jointly with the OECD** (with Code.org/CodeAI), *is* education-specific,
  Commission-co-published, structured in four competence domains — engage with, create with,
  manage, shape AI — and wired into the **PISA 2029** Innovative Domain. For the **content** of
  an Article 4 programme there is now a benchmark, and a client's package should be mapped to
  it rather than invented. **What is still missing is the legal half:** AILit is a curriculum
  and competence framework, not guidance issued under the AI Act, and it sets no compliance
  threshold — so "proportionate and documented" remains undefined by any authority. **The
  correct client sentence is: there is now a defensible benchmark to build to, and still no
  authority that will certify you met it.** Previous passes said no guidance existed at all;
  that was true when written and is no longer true. See `intel/market.md` EMEA.
- ~~**Whether the Digital Omnibus softened Article 4.**~~ **Resolved in p891: yes, and it did
  not repeal it.** Regulation (EU) 2026/1744, in force 27 July 2026, replaced Article 4 with a
  duty to *take measures to support* AI literacy and expressly disclaims any required level for
  any individual; enforcement by national market surveillance authorities began 2 August 2026.
  Six secondary sources agree, none dissents; the Official Journal text still could not be
  opened here. See T3 for what the softening does to the commercial pitch.
- **Whether any member state has issued an Article 4 safe harbour since the amendment.** The
  rewrite lowered the standard but named no benchmark, so "proportionate and documented" is
  still undefined by any authority. Searched this pass; nothing found. Unresolved.
- ~~**Saudi Arabia's position on AI in education.**~~ **Resolved in p892**, and the suspicion
  was right: it was a search-reach failure, not an absence. KSA has ministry/SDAIA ethics
  guidance, a national curriculum mandate and a 240,000-teacher training programme. See **T11**
  and the Saudi Arabia subsection in `intel/market.md`. **The method point generalises:** a
  named gap needs a dedicated leg, because the regional query that missed it the first time
  will miss it again.
- ~~**India.**~~ **Resolved in p892.** Covered as its own leg: NCERT/CBSE Computational Thinking
  and AI curriculum for **Classes III–VIII from 2026–27**, no education-specific AI statute, and
  content-labelling duties under the amended IT Rules since 20 February 2026. See **T11** and
  `intel/market.md`. **Still open within India:** whether Classes 9–10 become compulsory in
  2027–28 — sources conflict — and whether the July 2026 signal toward dedicated AI legislation
  produces a bill.

## T24 — The next licence trap is not an *unreadable* grant, it is a **readable grant that changes by directory** — and every one-licence-per-repo tool reports it wrong

**Added `p901`**, from byte-reads of the two repositories in this pass's vertical audit that
`gh api` could not resolve to an SPDX identifier.

**T23** named education's *unreadable* supply: repos with no licence file, or a grant no
detector can parse. **T24 is the opposite failure and a worse one**, because it produces a
confident wrong answer instead of a blank.

**The evidence.** Two repositories, both returning `NOASSERTION` from
`gh api search/repositories`, both with a perfectly legible `LICENSE` file:

- [`RocketChat/Rocket.Chat`](https://github.com/RocketChat/Rocket.Chat) `46,488★` —
  `master/LICENSE`, `1,654 B`, `sha256₁₂ ba8df3ebff76`. The text grants **MIT (Expat) for all
  content *outside* `ee/` and `apps/meteor/ee/`**; those directories are governed by a
  separate enterprise licence file. One repository, two grants, split by path.
- [`mattermost/mattermost`](https://github.com/mattermost/mattermost) `39,646★` —
  `master/LICENSE.txt`, `47,763 B`, `sha256₁₂ 0a3d65b9301f`. **Three** grants by path:
  `AGPL-3.0` for source you build yourself, `MIT` for binaries Mattermost compiled, and
  **`Apache-2.0` for `server/templates/`, `server/i18n/`, `server/public/` and `webapp/`** —
  plus a written covenant not to enforce AGPL copyleft against integrations that use only the
  Admin Tools and Configuration Files without creating a modified work.

**Why this is a trend and not two anecdotes.** Both are commercial open-core products that
grew a paid tier without relicensing the whole tree, which is now the standard way that
transition is made. Education stacks meet them constantly as the messaging layer. And the
same shape already appears inside this KB's own tier: `withmarbleapp/os-taxonomy` carries
**`ODbL-1.0`** — a *database* licence on a curriculum graph, correct for the asset and
invisible to anyone who assumes a software licence because the repo contains code.

**What it means for delivery.** Three things, and the first is the one that bites.

1. 🔴 **`NOASSERTION` is not "unlicensed" and it is not "risky".** It means the detector
   declined. Both repos above are usable; one is MIT for the part you want. A studio that
   treats `NOASSERTION` as a red flag discards usable permissive supply, and a studio that
   treats it as green ships an AGPL build.
2. 🔴 **A licence column is the wrong data shape for these repos.** This KB's own files —
   and the compiler that reads them — assume one licence per repo. For a path-dependent
   grant the honest entry names the *paths*, as the rows in `repos/trending.md` `901-R2` now
   do. Anything shorter is a guess with a citation attached.
3. 🟢 **The seam is usually clean enough to engineer around.** "Do not ship `ee/`" and "use
   only the Admin Tools and Configuration Files" are both testable in CI — a build-time check
   that the enterprise paths are absent from the artifact is a few lines, and it converts a
   legal question into a pipeline assertion. **That check belongs in the delivery template,
   not in a lawyer's memo.**

**Limit of this finding.** Two repositories is a small base. What is measured is that the
class exists, is common in adjacent infrastructure, and defeats the single-SPDX channel —
not how prevalent it is inside education specifically. 🔵 **Open as `901-G2`:** run the
`NOASSERTION` cohort across this base's full 6,494-slug population and measure the rate, the
way `p900` measured false absence. Until that runs, T24 is a named hazard, not a quantity.

