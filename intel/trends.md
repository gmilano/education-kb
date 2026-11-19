---
industry: education
region: Global
updated: 2026-11-19
---

# Current trends — education

**Thirty-one trends** (**T30 and T31 added in `p907`** — the LMS-to-agent bridge being built per-institution on the *user's own credentials*, which needs no institutional consent; and the agent-skill marketplaces having no education tier at all, which makes `T26`'s distribution channel measurably empty. Both are the first trends in this file derived from **global code search**, an instrument this base had recorded as unusable; **T29 added in `p906`** — vernacular open education supply measured across eight languages and found to be a single-country phenomenon, with *no licence at all* the default state in the other seven; **T26 added in `p903`** — the unit of publication shifting from the
application to the agent-addressable curriculum corpus, the first trend in this file derived from a
non-English repository channel; **T25 added in `p902`** — the licence trap moving from code to the data
and content assets, where no index can see it; **T24 added in `p901`** — path-dependent licences, the first trend in this file derived from repositories the SPDX channel refused to resolve at all; **T23 added in `p900`** — the first trend in this file derived from a
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
to **10,002 ★ on 2026-11-18** — 27 days. 🟢 **Re-measured in `p904`: 10,194 ★**, and the ecosystem is
still live — `kerr-mwv/learning-path-plugin` was **pushed 2026-11-18** and `tn-lorenz/awesome-learnharness`
now stands at 7 ★. 🔴 **`p904` also found the project's *old* address, `SirhanMacx/LearnHarness`, dead
on both verification channels** (`404` on 15 raw paths, `422` from `search/repositories`): the project
was **transferred**, not renamed, and a transfer leaves nothing behind for the rename-alias gate to
detect. No row in this KB is broken — `agents/top.md` already carries the canonical address — but the
method consequence is recorded in `agents/trending.md` `904-F8`. That alone is only a popularity fact. The structural
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

🔵 **Extended `p907`, and the extension changes who the buyer is.** Every server this trend was
built on reaches the LMS through an *institutional* surface — the Moodle Web Service API, Open edX
staff credentials. Global code search found a second route that this trend had not seen: **bridges
that act as the signed-in person and therefore need no institutional surface at all.**
`GuanmingQiao/POLITEMALL-MCP` (MIT, 2 ★) states it outright — *"talks directly to each tenant's own
REST API as the signed-in person — no institutional API key or app registration involved"* — and
`andrsnrua/universidad-pacifico-mcp` (ISC, 1 ★, Peru) says the same in Spanish while declaring
itself *"no oficial"*. 🔵 **So the MCP-over-LMS pattern has split into two products with different
buyers**: a *sanctioned* integration sold to the institution, and an *unsanctioned* one adopted by
the student or parent with no procurement at all. The second is spreading faster because it has no
gatekeeper. See **T30**.

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

🔴 **`p906` found the direction this trend had never recorded: a published field that *invents* a
restriction.** `yinuoguan/nengdou-ai-review-helper-web` (**193 ★**, the star ceiling of the Mandarin
education channel) is labelled **`MulanPSL-2.0`** by GitHub's classifier. Its `LICENSE` at `main` is
**verbatim Apache-2.0** — 11,356 B, `sha256₁₂ 43070e2d4e53`, opening `Apache License / Version 2.0,
January 2004`, and **byte-identical to `PGshen/thinking-map`'s**, which the same classifier labels
`Apache-2.0` correctly. 🔵 **Every prior case in this trend, including the expensive PrairieLearn
one, was a field that was silent or over-permissive. This is a field that is over-*restrictive*, and
it fails in the one way nobody checks for.** Mulan PSL v2 is OSI-approved and permissive but absent
from many enterprise approved-licence lists, so an SPDX-driven scanner routes this repository to
legal review or rejects it outright — **while the actual grant is Apache-2.0, patent grant included,
and is on every such list.** The asymmetry noted above inverts here: *an error that looks
restrictive is never challenged either, because nobody audits a rejection.* Gate `906-G1`: for
anything a studio intends to adopt, the field decides nothing in either direction — only the bytes
do.

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


🔵 **Extended `p907` with two further cases, and the second is a *new failure class* running against
the studio's interest.** (1) `swl10/pyslet` (76 ★) is **verbatim BSD-3-Clause** — three numbered
conditions, the endorsement clause, *"Copyright 2017 Steve Lay"*, byte-read at 2,906 B — and the
search index reports **`NOASSERTION`**. The index cannot classify a textbook-standard permissive
licence. (2) `LJKelly3141/coursepack` is **MIT**, and the index reports `NOASSERTION` because the
file it reads, root `LICENSE`, is **41 bytes containing no grant at all**:

```
YEAR: 2026
COPYRIGHT HOLDER: Logan Kelly
```

— the unfilled `usethis::use_mit_license()` R template stub, with the real MIT text sitting beside
it in `LICENSE.md`. 🔴 **This is the direction of error this trend had only one example of: the
index under-reporting permissiveness.** A sourcing pipeline that filters out `NOASSERTION` rows to
stay safe will silently discard usable permissive supply — and in a channel where the education
ceiling is 76 ★, discarding the top row is discarding the channel. **Operational rule, now gate
`907-G1` in `compose/patterns.md`: when SPDX reports `NOASSERTION`, read `LICENSE` *and*
`LICENSE.md` *and* the `README` licence declaration before concluding anything.**

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


## T25 — The licence trap has moved from the code to the **data and content assets**, where no tool can see it at all

`T19` established that published licence *metadata* is wrong often enough to be a procurement risk.
`T24` narrowed the next trap to a **readable grant that changes by directory**. `p902` found the one
after that, and it is worse in a specific way: **education's data and content assets carry
non-software or non-commercial grants, declared in prose, with no licence file for a tool to read.**

**Three instances, all verified by byte-read, none of them resolvable by SPDX:**

| Asset | What the index says | What the bytes say | Why it bites |
|---|---|---|---|
| [`riiid/ednet`](https://github.com/riiid/ednet) | SPDX `null` — **no licence file exists** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `NOTICE` all `404`) | 🔴 **`CC-BY-NC-4.0`, "for research purposes"** — prose in `README.md` | The **largest public education dataset on earth** (131,441,538 interactions, 784,309 students) is **commercially unusable**, and an automated gate reads "no licence file" as benign |
| [`parmentelat/nbautoeval`](https://github.com/parmentelat/nbautoeval) | SPDX `NOASSERTION` | 🔴 **`CC-BY-SA-4.0` on executable code** (289 B, Inria) | **No patent grant, and ShareAlike reaches derivative works** — an exercise bank built on it cannot stay closed |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | `ODbL-1.0` | 🔴 **a *database* licence on a curriculum graph** | Correct for the asset, and a trap for anyone who reads the repo as software |

🔵 **Why this is a trend and not three anecdotes.** The three sit at the three points where education
differs from other industries Globant serves: **the benchmark data** (knowledge tracing cannot be
evaluated without it), **the exercise content** (the asset a course actually is), and **the
curriculum graph** (the structure a syllabus is). In each case the thing being licensed is *not
software*, so the licensor reaches for a Creative Commons or Open Data grant — and **every tool in
the open-source supply chain, SPDX included, is built to read software licences.** The code tier of
this KB is now well characterised; the asset tier is where the unpriced risk has moved.

🔴 **The failure mode is silent and permissive.** All three read as *more* open than they are:
`NOASSERTION` and `null` look like "unlicensed, probably fine", and `CC-BY-*` reads as "open" to
anyone who has not checked whether it is `NC` or `SA`. Compare `p899`'s PrairieLearn finding — same
direction, different layer.

**Implication for delivery.** Put a **three-question gate on every non-code asset** before it enters
a client deliverable, and run it by reading the README, not by querying an index:

1. Is there a licence **file**? If not, the grant is in prose or absent — read the README.
2. Is it a **software** licence? A `CC-*` or `ODbL` grant on something you will compile, import or
   redistribute is a defect, not a formality.
3. Does it carry **`NC`** or **`SA`**? `NC` ends the conversation for a paid deliverable; `SA`
   decides whether the client can keep the result closed.

🟢 **And state the split in the proposal.** Research-only data can still earn its place: it validates
a model in a study and never trains the one that ships. That sentence is the difference between using
EdNet correctly and not being able to use it at all.

## T26 — The unit of publication is shifting from the *application* to the **agent-addressable curriculum corpus** — and the licence discipline has not followed it

**Evidence (`p903`, byte-verified).** https://github.com/revolover00/Bakloriya-AI-SKILLS publishes
**Egypt's complete approved 2026/2027 curriculum** — Egyptian Baccalaureate (78 units), General
Secondary (102), Preparatory (42), Primary grades 1–6 (78): **300 units, its own table reporting
"no chapter missing"** — as **28,402 KB of Markdown and nothing else.** No server, no model, no
framework, no front end. Each subject is sharded into `SKILL.md` (a routing index), `glossary.md`,
`patterns.md` (exam question patterns and solution keys), `cheatsheet.md` and a `chapters/` tree,
beneath a single path grammar: `skills/<stage>/<grade>/<term>/<subject>/`. The delivery mechanism is
an `AGENTS.md` routing guide **at a raw URL**, plus a prompt the learner pastes into *any* model,
which then walks the tree unaided.

**This is a different thing from T22 and from the agent-*skill* cohort, and the difference is the
artefact.** T22 records agents differentiating on *delivery surface* — MCP server, IDE skill, desktop
harness — but those are still **programs**. The cohort in `agents/top.md` ("the tutor as an agent
skill") tops out at **125 ★** and every member is a *tool*. Bakloriya ships **no program at all**:
the repository *is* the product, and the runtime is whatever model the learner already has. Three
properties follow, and they are what make this a trend rather than one odd repository:

1. 🟢 **Distribution cost collapses to zero.** No hosting, no inference bill, no app store, no
   installation. A national curriculum reaches every learner who has access to any chat model.
2. 🔴 **Quality control becomes a prompt, not a system.** Its only anti-hallucination mechanism is a
   **corpus-scoping instruction** — *stay inside the syllabus, do not mix grades or terms* — with no
   retrieval layer, no grounding check and no evaluation. The guarantee is that the *content* is
   curriculum-accurate; there is none that the model's rendering of it will be.
3. 🔴 **Stars stop measuring anything.** 6 ★ on a corpus used by Egyptian secondary students is not
   comparable to 6 ★ on a developer tool, and no star threshold will ever fire on a
   national-curriculum repository however many learners it serves. **The instrument this KB uses to
   rank supply does not work on this form** — the replacements are curriculum coverage and
   maintenance recency, on which this repository reads complete and current.

🔴 **And the licence discipline has not made the move with it.** The corpus form arrives carrying the
exact defect T25 identified in data and content assets, now at national scale: **`404` on all 12
byte-read licence paths.** 28 MB of curriculum content under default all-rights-reserved copyright.
The same holds for the channel's highest-star Arabic repository
(`MjeedBakr/Student-Success-Kit`, 67 ★, no licence) and for the Saudi Qiyas channel, where **12 of
12 repositories carry no grant**. Where the application form had settled into MIT/Apache norms,
**the corpus form is being published with no grant at all** — because its authors are teachers and
curriculum writers publishing content, not maintainers publishing software, and nothing in that
workflow prompts for a licence.

**What it implies for delivery.**
- 🔵 **Expect to meet this form in MENA and South Asian engagements, and expect it to be
  unlicensed.** Ask for the corpus licence in the first technical conversation, before any
  architecture discussion: it decides whether the engagement is an integration or a re-authoring.
- 🟢 **The schema is the transferable asset, and it is free to copy.** `SKILL.md` + `glossary` +
  `patterns` + `cheatsheet` + `chapters`, under a strict path grammar, is the most complete worked
  example of national-curriculum sharding this base has measured. **A schema is not copyrightable
  the way the content under it is** — re-author the corpus against material the client owns or
  licenses, and keep the structure. That is `compose/patterns.md` **P22**.
- 🔴 **Do not let the zero-infrastructure story into a regulated use case unexamined.** This form has
  no audit trail, no version pinning per learner, and no evaluation harness. Under EU Annex III, or
  Vietnam's Decision 33/2026/QD-TTg, "the model reads our Markdown and tutors the student" is not a
  compliance story. The corpus can be the content tier of a compliant system; it cannot be the
  system.



**🟢 The counter-example, added `p904`, and it changes the trend's conclusion.** Brazil executed the
same shift with full discipline. https://github.com/bncc-dev/bncc-dados publishes the **Base Nacional
Comum Curricular as 1,721 verified records** — 1,580 basic-education objectives plus 141 from the
Computing supplement — with **per-record provenance** (`fonte` plus the page of the official document
where each text was checked), **character-by-character verification** against the homologated MEC
PDF, a completeness proof, a reproducible extraction pipeline guarded by CI, JSON Schema, documented
interpretation decisions, an archived release under **DOI `10.5281/zenodo.21625233`**, and an
**`llms.txt`** agent data contract. Licensed **MIT for the pipeline and CC BY 4.0 for the data**, by a
company (**Profy Tecnologias Educacionais Ltda**), with two independent MCP servers, npm/PyPI
packages and an **open hallucination benchmark** built on top.

🔵 **So the licence discipline has not "failed to follow" the shift — it is bimodal, and the
difference is who publishes.** Egypt's corpus is a teacher-maintainer publishing content: 28 MB, no
grant, 6 ★. Brazil's is an organisation publishing a dataset: dual grant, DOI, provenance, 26 ★ and a
consumption ecosystem. **The form is not inherently a licence trap; it is a licence trap when nobody
does the work.** For delivery this means the first question about a curriculum corpus is not *"is it
licensed"* but **"was it published by someone whose workflow includes licensing"** — and where the
answer is no, `compose/patterns.md` **P22** re-authors it, while where the answer is yes, **P23**
adopts it and spends the budget on the agent tier instead.

## T27 — The licence split has a third axis — **the mark** — and no SPDX field, scanner or SBOM can express it

**Evidence (`p904`, byte-read).** `intel/trends.md` **T24** records the licence trap moving from the
repository to the **directory**; **T25** records it moving into **data and content assets**. Brazil's
`bncc-dev` cluster confirms both in the wild and adds a third axis in the same file.
https://github.com/bncc-dev/bncc-pacotes carries, in one `LICENSE` of 1,299 bytes:

| Axis | Grant | What it governs |
|---|---|---|
| **Code** | **MIT** | `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests, config |
| **Data** | **CC BY 4.0** | the curriculum JSONs in `packages/bncc/dados/` and `python/bncc/dados/` — attribution required |
| **Name and visual identity** | 🔴 **not licensed at all** | `"bncc.dev"`, `"BNCC.dev"`, the logo, wordmark, colours and typography |

Verbatim: *"O código é livre; a marca não"* — the code is free, the mark is not — with the explicit
condition that derivatives **must not present themselves as being bncc.dev** nor use the mark
without authorisation. And the artefacts ship mixed: **the npm tarball and the PyPI wheel each carry
MIT code and CC BY data in the same package.** `bncc-dev/bncc-benchmark` uses the same two-file
split (`LICENSE-CODIGO.md`, `LICENSE-DADOS.md`); `bncc-dev/bncc-dados` puts the data grant at
`dados/LICENSE.md`, below the root.

**Why it is a trend and not a quirk.** The two axes T24 and T25 describe both constrain **use** —
what you may run, modify and redistribute — and both are, in principle, discoverable by a scanner
that walks the tree. The trademark axis constrains **naming and presentation of the delivered
product**, which is:

- 🔴 **invisible to every tool in the licence-compliance stack.** SPDX has one field per package;
  GitHub's detector returned `NOASSERTION` on all three of these repositories; an SBOM records
  `MIT` and is not wrong, merely silent on the two obligations that actually bind. **A clean
  licence report is not evidence that the brand question was asked.**
- 🔴 **raised at the worst possible moment in a delivery.** Licence review happens at architecture
  time; naming, logo and launch collateral happen at the end. A reserved mark discovered during
  launch prep is a rebrand, not a review comment.
- 🟢 **and it is a *reasonable* thing for a maintainer to do**, which is why it will spread. A
  public-good dataset maintainer wants maximum reuse of the data and zero confusion about who
  certifies it. Expect the pattern wherever a named project publishes authoritative public-sector
  data — exactly the asset class T26 says is becoming the unit of publication.

**What it implies for delivery.**
- 🔵 **Add two questions to licence triage, and ask them per artefact rather than per repository:**
  *where does the payload's own licence file live* (the root `LICENSE` is not it when the payload is
  data), and *is the project's name or identity reserved*. Gate **`904-G1`** in
  `compose/patterns.md` `G1` encodes the first; the second is a prose question no probe will answer.
- 🔵 **Attribution is a build requirement, not a legal footnote.** CC BY on a curriculum dataset
  means the product's UI must carry the credit — so it belongs in the component that renders
  curriculum references, specified in the sprint that builds it, not in a licence appendix nobody
  implements.
- 🟢 **A withheld mark is usually a *neutral* fact for a studio engagement**, because the client
  wants its own brand on the product anyway. It becomes a problem in exactly one case: when the
  open project's name was going to be the credibility story ("built on X"). Decide that explicitly.

## T28 — Open education's dependency layer is undocumented and, at the top of the shelf, unpinnable — and the two properties move *against* popularity

Measured `p905` across the 14 platforms an education engagement is actually built on: 350 byte-reads
of manifest and grant-disclosure paths, each on the repository's real default branch. Ledger:
[`dep-grant-scan.2026-11-18-p905.tsv`](../evidence/dep-grant-scan.2026-11-18-p905.tsv).

**The two measurements.**

- 🔴 **Grant disclosure: `0` of 14.** Not one platform states the licences of what it bundles. Two
  return a file named `COPYRIGHT` and neither enumerates a dependency — Odoo's (433 B) points the
  reader at *"the history of the source version control system"*, Canvas's (621 B) restates Canvas's
  own AGPL-3.0. The only other artefacts in the class are two `dependabot.yml` files, which are
  update automation. Meanwhile Moodle resolves **316** packages and Gibbon **355**.
- 🔴 **Pinning, at the top of the shelf: `DeepTutor` pins 1 of 74** (79 `>=`, 36 `<`) across a
  three-level script-generated manifest tree; `OpenMAIC` declares 178 npm packages with no lockfile
  on any path probed. 🟢 **`openedx/openedx-platform` pins 311 of 311.**

**Why this is a trend and not a list of defects.** The direction is consistent and it runs *opposite*
to the signal this KB and everyone else records. Stars, forks and push recency all say `DeepTutor`
(60,451 ★) and `OpenMAIC` (43,899 ★) are the healthiest things in open education; reproducibility says
they are the least deployable, and that the most deployable base has **8,244 ★**. The mechanism is
not neglect — it is **velocity**. Both flagships ship weekly, and a range constraint (`>=`, `<`) is
what a fast-moving project writes so it can keep moving; an exact pin is what a platform with
institutional deployers writes because someone downstream has to rebuild it in three years. 🔵 **The
age and governance of a project predict its reproducibility better than its popularity does**, which
is the same university-versus-startup axis as **T2**, measured on a different quantity.

**What follows for a studio, concretely.**

1. 🟢 **Choose the base on the reproducibility column, not the star count**, whenever the client must
   be handed a rebuildable artefact — which, under the procurement specifications in **T9** and the
   exit requirements in **P8**, is most engagements.
2. 🟢 **Where a flagship is the right pedagogical choice anyway, the lockfile is the studio's work.**
   `pip-compile` / `uv lock` / `npm ci` against a resolved set, vendored at a SHA, named as a week-one
   task in the estimate. It is small work discovered late, which is the expensive kind.
3. 🟢 **Sell the dependency-grant scan rather than absorbing it**, priced as `compose/patterns.md`
   **P24**. No upstream will answer the
   procurement question, so it is a deliverable: `scancode-toolkit` (Apache-2.0) over the resolved
   tree, output as the licence inventory the client's audit will ask for.
4. 🔴 **Do not read a missing disclosure as a clean one.** This is the trap half of the trend: both
   `COPYRIGHT` files are written in a compliance register and disclose nothing, so the absence
   *presents as a presence* to any reviewer who stops at the filename.

🔵 **Relation to T19 and T24–T27.** Those four trace licence facts that are wrong or invisible at the
*repository* level — bad metadata, per-directory grants, data-and-content grants, the mark. T28 is
the same failure one layer down, at the **dependency** level, and it is the layer where no field
exists to be wrong in the first place: there is nothing to misread because nothing is written.



## T29 — Vernacular open education supply is a **single-country** phenomenon, and in the other seven languages measured the default state is *no licence at all*

**Added `p906`**, from an eight-language census of `search/repositories` rather than from search
snippets or a sampled probe. Record:
[`nonenglish-ceiling.2026-11-18-p906.tsv`](../evidence/nonenglish-ceiling.2026-11-18-p906.tsv).

🔵 **This trend qualifies T20 rather than extending it.** T20 established — correctly, from byte
reads — that vernacular education agents exist and that the native language sits inside the data
contract rather than in a translation layer. **It did not establish how many languages that is true
of.** `p906` measured all eight channels this base had declared untried, and the answer is **one**.

| Language | Repos matching | Topical ★ ceiling | Carry a licence |
|---|---|---|---|
| **Mandarin** | **347** (`作业 批改`) | **193** | mostly yes |
| Hindi | **113** | 2 | **0 of 113** |
| Indonesian | 14 | 1 | none |
| Thai | 9 | 0 | none |
| Vietnamese | 6 | 1 | none |
| Korean | 2 | 2 | none |
| Japanese | 1 | 0 | none |
| Urdu | 1 | 0 | n/a (sole hit not education software) |

🔴 **The two kinds of emptiness are not interchangeable, and the distinction is the commercially
useful part.** Thai, Japanese, Urdu and Korean are **thin** — few repositories exist at all. **Hindi
is the opposite, and it is the finding that matters**: at 113 repositories it is the second-densest
channel of the eight, so the vernacular layer is not missing — **it is the wrong kind.** Every hit
inspected is a school, NGO or foundation *website*, or a non-AI teacher-rating project, and **not
one of the 113 carries a licence file.** For the world's largest school system the answer to *"is
there local open source to build on?"* is therefore neither yes nor "we found nothing": it is
**there is a great deal of it, and none of it is software a studio can adopt.**

🔴 **This is also the sixth concealment direction in `intel/measured-unusable.md`, and the first
that is a property of a channel rather than of a repository.** The five prior directions all
describe *how a grant is hidden* — a silent SPDX field, a source-available licence that reads like
open source, a non-commercial clause on the most useful asset, a hand-edited grant, barred repos
skewing large. **Here nothing is hidden: there is simply no grant, and that is the norm, not the
exception.** T23 measured a third of education's permissive supply as carrying no readable grant;
in six of these seven languages the figure is effectively all of it.

🟢 **Mandarin is the counter-case and it is a full tier, not a handful of repositories.** The
grading channel alone returns 347 results; twelve were verified on two channels and shelved, into a
tier (`Assessment, grading and academic integrity`) that this KB had held as **entirely North
American and European** across twelve rows. 🔵 **The structural point for a studio: the discovery
failure was in the query language, not in the coverage.** A section that looks full does not read as
a gap, which is how an entire national supply tier stayed unrecorded here for 905 passes.

🟡 **The honest limit on this trend, which also makes it falsifiable.** `search/repositories` matches
name, description and README, so a project with English metadata and vernacular content is invisible
to a vernacular query. **This base can prove that blind spot is real: `belajar-ngoding-byGanzu`
(MIT, 66 ★) is a shelved Indonesian row that `p906`'s own Indonesian queries did not return.** Every
ceiling above is a ceiling on *vernacular-metadata* supply — which is what a regional sourcing claim
actually rests on, and not a proof of non-existence. The instrument that would test it is named as
gap `906-G2`: English-metadata queries carrying a national curriculum term (`CBSE`, `NCERT`,
`gaokao`, `UTBK`, `JLPT`, `TOPIK`). **Until that runs, read this trend as a statement about what is
findable, and price the India vernacular tier as build either way.**

## T30 — The LMS-to-agent bridge is being built **per institution, on the user's own credentials** — which removes procurement from the critical path, and removes the licence with it

**Evidence (`p907`, global code search — a channel no earlier pass could use).** Seven bridges, all
created within the last eight months, none above 4 ★, each wired to **one named institution's**
learning platform:

| Bridge | Licence | Institution / system | Region |
|---|---|---|---|
| `GuanmingQiao/POLITEMALL-MCP` | **MIT** | POLITEMall + NYP — Singapore polytechnic/ITE **D2L Brightspace** | APAC |
| `andrsnrua/universidad-pacifico-mcp` | **ISC** | Universidad del Pacífico, Perú — Blackboard Ultra, **70 tools** | LATAM |
| `cculb/schoolconnect` | **MIT** | **PowerSchool Parent Portal** — the guardian, not the student | North America |
| `bolgerru/blackboard-mcp` | 🔴 none | Trinity College Dublin Blackboard | EMEA |
| `chenshi5858/CanvasGPTAssistant` | 🔴 none | Canvas | — |
| `PaoloJN/lms-data-bridge` | 🔴 none | "any LMS", via Chrome extension + MCP | — |
| `MikeTheGreat/MarkdownToCanvasLMS` | 🔴 none | Canvas authoring | — |

**What makes this a trend and not a list.** Four properties hold across the set, and together they
describe a different product from `T13`'s community plugins:

1. **No institutional surface is used.** These call the tenant's own REST API *as the signed-in
   person*. No API key, no app registration, no vendor partnership, no procurement.
2. **They are per-tenant, not per-platform.** The unit of publication is *my university's Moodle
   instance*, not "Moodle" — which is why there are seven of them for four platforms and why there
   will be more.
3. **They are geographically distributed in a way open education supply normally is not.**
   Singapore, Peru, Ireland and the US in one seven-row cohort. This base has spent several passes
   establishing that open education supply is concentrated in the US, EMEA and China; **the bridge
   tier is not**, because the thing being built is local by definition.
4. **Four of the seven carry no licence at all.** They are built by students for their own
   institution, not published as supply — which is `T23`'s unaddressability arriving in a new tier.

🔵 **Why it matters commercially, and it cuts both ways.** For a studio, the *pattern* is the
finding: an agent surface over a client's existing LMS can be demonstrated in days without touching
procurement, which is the single slowest step in an education engagement. **That is the fastest
credible demo in this KB.** And the same property is the risk — a bridge acting as the signed-in
person is, from the institution's side, difficult to distinguish from credential sharing, and three
of these projects declare themselves unofficial precisely because they know it. 🔴 **So the
deliverable is the sanctioned version of an unsanctioned pattern**: same user-facing capability,
institutional consent and an auditable service identity underneath. `compose/patterns.md` **P26**
scopes exactly that, and the governance note is the point of the pattern rather than a caveat on it.

🟡 **Honest limits.** Seven repositories is a cohort, not a census; the channel is one pass old and
its exclusion rules were derived after the queries ran. The claim here is that the *form* is
recurring independently in four regions, which seven independent instances do support — not that
this tier has scale. **None of these is adoptable as a dependency.**

## T31 — `T26`'s distribution channel exists, is permissive, is enormous — and is **empty where education belongs**

**T26** holds that the unit of publication is shifting from the application to the
agent-addressable corpus. The obvious vehicle is the published **agent-skill collection**, and
`p907` measured the two largest that global code search surfaced:

| Collection | ★ | Licence | Published skills | Education tier |
|---|---|---|---|---|
| `sickn33/agentic-awesome-skills` | **49,962** | MIT | 2,955+ | 🔴 **none found** |
| `LeoYeAI/agent-master-skills` | **2,206** | MIT | 2,700+ | 🔴 **none found** |

**How this was measured, because the raw numbers say the opposite.** Repo-scoped code search returns
42 hits for `curriculum` and 266 for `lesson plan` in the 49,962 ★ collection — which looks like an
education tier until the **paths** are read. They are `skills/product-design-harness/`,
`skills/offers/references/`, `skills/linkedin-profile-optimizer/SKILL.md`, `skills/loki-mode/` and
`tools/scripts/build-catalog.js`: marketing, sales and product-design skills using the word
"curriculum" in passing. In the 2,206 ★ collection, **`tutor pedagogy` returns `0`**.

🔵 **The implication is the cleanest opportunity statement in this file.** Two MIT-licensed
collections with a combined ~5,650 published skills and tens of thousands of stars are the
distribution channel a studio would want for education IP — and education is **not in them**.
Meanwhile the corpora themselves are being published nationally and *unlicensed*: `p903`'s Arabic
national-curriculum agent-skill corpus, `p904`'s Brazilian `bncc-dev` cluster (MIT + CC BY 4.0, and
the only licensed one). 🔵 **So the asset is appearing and the shelf it would sit on is bare.**
Publishing a licensed, curriculum-grounded education skill pack into these channels is low-cost,
high-visibility studio marketing with no incumbent to displace.

🟡 **Limits, stated.** Measured by hit count and path inspection, **not** by enumerating every skill
file — so "none found" is strong evidence of absence, not proof. Both collections are themselves
aggregators of other people's skills, so their licence covers the collection, not necessarily each
item. And this is two collections: the largest two this channel reached, not the market.

## T32 — The education **agent-skill** tier is appearing under **Creative Commons**, not under software licences — and ShareAlike on prompt text is a copyleft nobody is scanning for

**Measured in `p908`, by byte-reading grants that SPDX reports as `NOASSERTION`.**

`T31` found that the agent-skill marketplaces are enormous, permissive and **empty where education
belongs**. `p908` found what fills that shelf when someone does publish into it, and the licence
shape is not the one the tooling assumes.

| Asset | ★ | SPDX from the API | Grant **byte-read from the payload** | What it actually is |
|---|---|---|---|---|
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **1,000** | `NOASSERTION` | 🔴 **CC BY-SA 4.0** (`1,230 B`, `sha256₁₂ f952182df4eb`) | **165 evidence-grounded skills** for teachers, school leaders and EdTech builders — pedagogy, learning science, curriculum |
| [`kaveheng/GenAi-in-education`](https://github.com/kaveheng/GenAi-in-education) | 0 | `NOASSERTION` | 🔴 **CC BY 4.0** (`442 B`, `sha256₁₂ 5217b43fb5d4`) | Course implementations using generative AI in teaching and assessment, by year |

🔴 **Why `CC BY-SA 4.0` on a skill pack is the sharpest licence trap in this base so far.** The
licence text in that repository is explicit that it covers *"the educational skills, documentation,
examples, and curriculum materials"* — that is, **the prompt text itself**, which is the entire
substance of an agent skill. ShareAlike then requires derivatives to carry the same licence. So a
studio that forks 165 teacher skills, rewrites them for a client's curriculum and ships the result as
part of a proprietary assistant has produced a **derivative of a ShareAlike work** and owes it under
CC BY-SA. 🟢 **Commercial use is explicitly permitted** — the obligation is not a ban, it is that the
adapted prompt library must stay open.

🔵 **And no tool in the normal pipeline will tell you.** Three independent reasons, each measured:

1. **SPDX reports `NOASSERTION` for both**, so a licence gate keyed on the API field sees "unknown",
   not "copyleft" — and `T19` already established that this base's passes find published licence
   metadata wrong in both directions.
2. **SBOM and dependency scanners read manifests and code**, and a skill pack has neither. There is
   nothing for them to resolve.
3. **`T27` named the *mark* as the third licence axis; `T25` named *data and content*. This is the
   fourth: the licence on the instructions.** A prompt is simultaneously the product and the
   documentation, and the CC family is what authors reach for when they think of their work as
   writing rather than as software.

🟢 **The commercial read is not "avoid it".** A CC BY-SA skill corpus is the **cheapest credible
starting point** for an education assistant that exists — 165 skills, 1,000 ★, grounded in learning
science, free to use commercially. 🔵 **The discipline is architectural: keep the ShareAlike corpus as
a loaded, attributed *input* behind a stable interface, and keep the client's own curriculum
adaptations in a separate, independently-licensed layer.** That is the same separation `P24` built for
reproducibility and `P25` built to keep AGPL out of a deliverable; this pass adds a third reason to
build it.

🟡 **Limits, stated.** Two assets, both found in `p908`, one of them at 0 ★. **This is a named shape
with two instances, not a measured population** — the claim is that the shape exists and is invisible
to tooling, not that it is yet the dominant licence of the tier. 🔵 **The test for the next pass:
enumerate the education entries in the two marketplaces `T31` measured and read each grant from the
payload.** If the CC share there is material, `T32` graduates from a shape to a distribution.

## T33 — The regulatory lever is moving from *AI-as-subject* to *AI embedded in other instruments*, and LATAM is where the shift is measured

Every trend above this one reads regulation the way `T1` framed it: AI statutes, risk
classification, compliance dates. `p909` measured something that cuts across that reading — the
**standalone AI instrument is no longer where the attention is**, and the duties are migrating
into education law, teacher-licensing law and procurement documents instead.

**The measurement, and it is LATAM's.** CELE's *Observatorio Legislativo* records
digital-technology bills in Latin American congresses for **January 2025 – April 2026**:
Argentina **63**, Brazil **36**, Mexico **35**, Peru **17**, Chile **16**, Colombia **14**,
Paraguay **14**, Ecuador **5**, Guatemala **1** — **201 in total, and the breakdown sums exactly
to 201**, which is why the figure is carried. 🔴 **The most frequent themes in that window are
honour and reputation, cybersecurity and content moderation. AI led only in January–April 2025.**

🔵 **That is a receding wave, and this KB had been assuming a rising one.** Several passes have
framed the LATAM opportunity as *"AI regulation is coming"*. On the only quantified regional
series these shelves hold, AI peaked as a standalone legislative subject **eighteen months ago**
and has since been displaced by three other digital-policy topics.

**But the education duties did not recede — they changed vehicle.** In the same window and the
ones around it:

- 🇵🇪 **Peru** — `PL 00569/2026-CD` puts AI into the **Ley General de Educación**, not into an AI
  act: digital literacy and AI training transversally through *educación básica*, teacher
  training, and limits on automated systems in **pedagogical decisions**.
- 🇨🇴 **Colombia** — `Ley 2626 de 2026` was already this base's clearest case of the same shape:
  binding by **curricular mandate** rather than risk regulation.
- 🇨🇳 **China** — the April 2026 *"AI + Education"* plan carries AI into **teacher qualification
  examinations and certification**, making it a **licensing** duty rather than a professional-
  development aspiration.
- 🇬🇧 **United Kingdom** — the AI Tutoring Tools Pioneer Programme puts the duty in a
  **procurement standard** owned by DSIT/i.AI and published to the market.
- 🇪🇺 **EU** — and the counterpoint that completes the picture: the one jurisdiction whose lever
  *is* a standalone AI statute **deferred its education obligations to 2 December 2027** (`T3`).

🔵 **The commercial consequence, which is the point of the trend.** A compliance-led pitch —
risk classification, conformity assessment, Annex III documentation — is aimed at the vehicle that
is slowing down. The instruments that are **binding now** are curriculum mandates, teacher
licensing and procurement specifications, and those buy **curriculum alignment, teacher capacity
and standards conformance** (`T11`, `T9`) rather than AI governance. 🔵 **Read with `T15`** — open
source has built least where regulation has decided most — **this says the gap is not in
governance tooling, it is in curriculum-aligned and credential-aligned delivery.**

🟡 **Limits, stated.** The 201-bill series is **one source**, reached on two searches, and
**no primary source could be fetched this pass** (`WebFetch` DNS failure on every host tried); a
second leg gave the window as January 2025 – **February** 2026 for the same total, and the
breakdown-bearing window is the one carried. The non-LATAM items are each individually evidenced
on these shelves but are **not a measured series** — they are five instruments read as a shape, so
the claim is that the shape is visible in five jurisdictions, **not** that the migration is
quantified outside LATAM.

🔵 **The test for the next pass.** Take the CELE series and split the LATAM education-AI bills out
of the 201 by vehicle — education-code amendment versus standalone AI act. If education-code
amendments are rising while standalone AI bills fall, `T33` graduates from a shape to a measured
distribution, and the ordering in `T1` needs revisiting.

## T25 — National-curriculum-aligned supply is the **inverse** of the curated open-source shelf: live, diffuse, and two-thirds ungranted (measured `p910`)

🔵 **The claim this trend replaces.** Every trend above this one is about the open education tier
that *can* be adopted — `T21`'s mature permissive grading stack, `T17`'s permissive extension
points, `T23`'s measured permissive-but-unaddressable supply. All of them describe a **curated**
population: `p909` measured this KB's shelf at **68.8% permissive** across 337 repositories. That
figure is the product of 909 passes of filtering, and nothing in this file said what the tier
underneath looked like.

🔴 **Now measured.** `p910` queried fourteen national examinations — JLPT, TOPIK, suneung/CSAT,
HKDSE, PSLE, SNBT/UTBK, KSSM/SPM, NAPLAN, GCSE, bagrut, Tawjihi — and sampled **255 distinct live
education repositories**:

| | National-exam tier | Curated shelf |
|---|---|---|
| Permissive | 🔴 **25.1%** | 🟢 **68.8%** |
| **No `LICENSE` file at all** | 🔴 **63.9%** | 5.3% |
| Zero stars | 🔴 **46%** | — |
| Pushed since 2026-09-01 | 🟢 **29%** | — |

🟢 **It is not abandoned and it is not fake.** 19 of the 255 were pushed in the seven days to
2026-11-19, one on the day of the measurement. Students, teachers and tuition centres are building
exam-prep software in public, continuously, in every one of these markets — **and they are not
adding a licence.**

🔴 **Three consequences a studio should price differently because of this.**

1. **The exam-aligned content layer is a build, not an adoption.** In six of the eight APAC markets
   measured, local supply is either ungranted or prompts-only. Malaysia's entire permissive
   national-curriculum supply is **one MIT prompt library**; Jordan's is **nothing** — four live
   Tawjihi repositories, zero licences. A bid that assumes "there will be something open for the
   local curriculum" is wrong more often than it is right.
2. **The restriction concentrates exactly where the value is.** The permissive artefacts are
   *tools* and small derived datasets; every broad-coverage **corpus** found is CC BY-NC, CC BY-SA
   or AGPL — including the largest artefact in the tier (3,149 ★, **CC BY-NC**) and Singapore's
   machine-readable **MOE primary mathematics syllabus** (**CC BY-NC**). 🔴 **NonCommercial is a
   different class of problem from copyleft**: copyleft constrains how you distribute, NC bars the
   paid engagement itself. No architecture fixes it.
3. **Discovery of this tier is an instrument problem, not a search-effort problem.** The bare
   national-exam acronym is **63% homonym noise** (`910-F1`); one co-term takes it to 4% but
   silently drops the institutional artefacts (`910-G1`). Teams will either find Minecraft
   libraries or miss the government infrastructure, and both failures look like "we searched".

🟢 **Where the opportunity actually is, and it follows directly from the measurement.** In these
markets a studio is not displacing an incumbent open platform — **there is none**. The competition
is the client's unfinished internal build. The defensible asset is the **re-authored, grant-clean
curriculum spine** (`compose/patterns.md` **P22** for Brazil's BNCC, **P29** for the APAC exam
tier): the one thing the open tier cannot supply here, because where a national syllabus *has* been
published machine-readably, it was published NonCommercial.
