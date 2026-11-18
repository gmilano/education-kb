---
industry: education
region: Global
updated: 2026-11-18
---

# Current trends — education

Eleven trends, each with the evidence behind it and what it implies for delivery. Researched
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
