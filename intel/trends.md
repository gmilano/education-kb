---
industry: education
region: Global
updated: 2026-10-19
---

# Current trends — education

**Pass 318 · 2026-10-19.** Eleven trends. Each names the evidence behind it and, where the evidence
is vendor marketing, says so. Pass 318 **added trend 11** — the sector's published metadata is
unreliable in both directions, which is a finding about method and it changes how every other row
in this KB must be sourced — and revised trends 2, 3 and 4 against first-hand evidence.

## 1. Institutional AI deployment is not landing — and that, not adoption, is the gap

Earlier passes framed this sector as "usage is ahead of governance". The Digital Education Council
AI in Higher Education Global Survey 2026 (**45,398 responses — 27,284 students, 18,114 faculty —
across 35 countries**) supports a sharper reading:

- **88% of students use AI; 77% of faculty do, up 16 points year on year.**
- **43% of students report no AI integration in their courses at all.**
- Among students who *have* experienced institutional AI integration, **only 5% say it transformed
  how they learn.**
- **Only 29% think their instructors are equipped to guide them — 17% in the US and Canada.**
- **64% of faculty have had AI literacy training; 31% feel involved in shaping AI policy.**

Adoption is solved. Institutional deployment is near-absent, and where present it is judged
worthless by 95% of the students exposed to it. **Implication:** the sellable work is not
"introduce AI" and not only "govern AI" — it is making an institutional deployment that students
can tell apart from the chatbot they already use. Training exists (64%) and is not working; that is
a programme-design problem, not a content-sourcing problem.

## 2. Procurement is policy-gated, and the US volume has gone up again

**134 AI-in-education bills across 31 states in 2026**, inside a wider wave NCSL counts at ~1,390
AI bills across 49 states. Ohio requires an AI framework in every public/community/STEM school by
2026-07-01; North Carolina's model policy is due 2026-12-31 with local policies by 2027-06-30;
Idaho SB 1227 mandates a statewide framework plus a human-teacher guarantee; California AB 1159 on
student data; Oklahoma and Maryland reported to require human oversight and bar AI from high-stakes
student decisions. Federally, H.R. 8747 (K-12 AI Literacy and Readiness Act of 2026) cleared
committee markup on 2026-07-21. **The RFP question has shifted from "what can your tutor do" to
"show me the audit trail."**

**Revised this pass: the binding constraint in US K-12 is not a bill, it is a rule already in
force.** Full compliance with the **amended COPPA Rule has been required since 2026-04-22**
(published 2025-04-22, effective 2025-06-23). **§312.5(a)(2) requires separate verifiable parental
consent before a child's personal information is disclosed to a third party**, with the exception
limited to disclosures *integral* to the service; the Rule also adds retention limits, a written
published retention policy, and biometric identifiers to the definition of personal information.
**Forwarding a K-6 pupil's prompts to a third-party model provider is such a disclosure.** State
bills set deadlines for *policies*; COPPA sets a live federal obligation on *architecture*, and
every K-12 AI deployment shipped before April 2026 should be assumed non-compliant until audited.
That is the most concrete near-term revenue line in this KB — see `intel/market.md`, North America.

## 3. Restriction is now a design requirement, not a market loss

New this reading of North America: **New York City runs a one-year moratorium on student-facing AI
through eighth grade**, and **Katy ISD (Texas) is banning generative AI chatbots for K-6.** These
are not outliers to wait out — they are the shape of K-12 procurement. A product that cannot
enforce **grade-band gating** and a **teacher-facing-only mode** is unbiddable in those districts,
and the gate is cheap to build. Treat restriction as a feature spec.

**Quantified by country this pass, and it does not follow the regulatory map** (Ipsos Education
Monitor 2026, support for banning AI in schools): **Indonesia 23%, India 26%, Japan 29%, South
Korea 31%**, with **Australia and New Zealand above all of them.** So the market with the region's
only binding AI statute (Korea) has middling public appetite for restriction, while the markets
with *no* AI statute (Australia, New Zealand) have the highest. **Restriction sentiment and
regulation are separate variables and must be scoped separately** — the gating feature is sold on
public and parental sentiment, the audit trail is sold on statute, and a bid can need one without
the other.

## 4. The permissive-agent / copyleft-platform split is real but softening — REVISED this pass

**Recounted this pass over larger tables, and the softening reversed.** 14 of 18 agents in
`agents/top.md` carry a permissive software licence. **13 of 19 platforms** in
`verticals/solutions.md` are GPL-2.0/GPL-3.0/LGPL-3.0/AGPL-3.0 — the platform ratio moved *against*
permissiveness this pass (6/16 → 6/19), because all three platforms added were AGPL: `frappe/lms`,
`LearnHouse` and `openedx/openedx-ai-extensions`. This is still the sector's structure and it still
dictates architecture: permissive agents across a network boundary from a copyleft LMS, LTI 1.3 as
the seam. **Pass 317 called the split "softening"; on a larger sample it is not. It is holding.**

**But "the platforms are all copyleft" is no longer an accurate sentence**, and pass 317 found the
crack widening from both sides at once:

- **`OpenOLAT/OpenOLAT` — Apache-2.0, 448 ★, 31,877 commits.** A mature LMS from frentix GmbH
  (Switzerland), built on the University of Zurich's OLAT 7.1. Unlike mentingo this is not a
  promising young project; it is institution-grade software under a permissive licence, and it means
  there now exists a real LMS where Globant can link agent code into the platform instead of paying
  the LTI-boundary tax. **6 of 16 platforms are now permissive.**
- **`plastic-labs/tutor-gpt` — GPL-3.0, 932 ★.** Copyleft arriving in the *agent* tier, going the
  other way. One row, but the first.

**What has not changed is the advice**, and this is the important part: for a client already running
Moodle, Canvas or Open edX — which is nearly every client — the copyleft platform is a given and the
LTI boundary is still mandatory. The softening matters only for greenfield and sovereignty
engagements. Do not let it loosen the architecture discipline in the other 90% of cases.

**The deeper lesson is about method, not licences.** OpenOLAT has 31,877 commits and was missed by
316 passes because it has 448 stars. With Ed-Fi (12 ★) and Sunbird (41 ★) that is three
confirmations that **a star-ranked search cannot see this sector's institutional infrastructure** —
it is adopted through procurement, not GitHub. Treat the remaining declared gaps in this KB as
search-method artefacts until proven otherwise.

## 5. Deterministic pedagogy under a generative surface is now a shipped architecture

This KB has argued for three passes that the LLM should explain while a deterministic engine
decides. `ArnaudGuiovanna/tutor-mcp` (MIT, 467 commits) ships exactly that — skill graph, Bayesian
Knowledge Tracing, FSRS scheduling, prerequisite gating and cross-session narrative memory — under
the stated principle **"Generative teaching. Deterministic pedagogy."** DeepTutor's own framing is
"lifelong personalised tutoring" (41.7k ★, v1.6.15 on 2026-10-19, now with arXiv 2604.26962), and
gen-mentor's multi-agent ITS architecture was a WWW '25 oral.

The argument has moved from position to implementation. **A 2026 tutor needs a learner model that
persists across sessions and a non-LLM component that decides what comes next** — and that is now
something to integrate rather than build.

## 6. MCP, not LTI, is where agent integration is actually happening — NEW

Every integration artefact found this pass speaks **MCP**: `tutor-mcp` (an entire ITS as an MCP
server), `ankimcp/anki-mcp-server` (520 ★, spaced repetition exposed to any LLM client), Canvas
MCP servers in the wild, `iblai/api`. None of them speaks LTI 1.3, SCORM or xAPI.

This is a genuine fork in the road. MCP gets an agent to *tools*; LTI gets an agent into the
*institution* — launch context, roster, identity, gradebook passback. **A tutor that is MCP-native
and LTI-absent works beautifully for an individual learner and cannot be deployed by a university.**

**Revised this pass, and the revision is sharp: the LTI-native tutor does exist, and it has no
licence.** `blamb/lti-tutor` implements LTI 1.3 against Moodle with dynamic registration, deep
linking (each tutorial placed as its own External tool activity) and completion passback through
Assignment & Grade Services, on `ltijs`. **Its README states the licence as "To be decided." 0 ★,
39 commits.** Default copyright therefore applies and Globant cannot use it.

That is the second unlicensed repo this KB has had to reject at exactly this point in the stack
(after `luffycodes/Tutorbot-Spock`), and together they suggest something structural rather than
coincidental: **the work closest to the institutional integration problem is written by instructors
and university staff solving their own course, not by labs or vendors with legal review — so it is
the least likely work in the sector to carry a licence.** Expect to find the answer to an
integration problem in an unlicensed repo, and budget to rebuild it.

The glue therefore remains yours to write. `pylti1.3` (MIT, 138 ★, 178 commits) is still the only
solid library, and pass 317 confirmed it covers the full Advantage surface — Deep Linking, AGS,
Names and Roles, Course Groups, Submission Review, Data Privacy Launch. **"MCP server inside, LTI
tool outside" stays the integration shape to standardise on**, with one caveat now named: every
pattern in this KB crosses the LMS boundary through that single 138-star, single-maintainer library.
That concentration belongs in the risk section of any SOW.

## 7. The skill, not the app, is becoming the unit of educational AI — NEW

Among the highest-starred repos under GitHub's `ai-tutor` topic, a striking share are **agent
skills rather than applications**: `GarethManning/education-agent-skills` (878 ★, 165
evidence-grounded teaching skills), `ZeKaiNie/universal-examprep-skill` (309 ★),
`SenmuuuuW/universal-diagnostic-tutor-skill` (247 ★), `KeWang0622/kaogong-skill` (189 ★),
`flysheep-ai/education-skills` (116 ★). `Li-Evan/Bloom` (MIT, 289 ★) ships **both** a skill bundle
and a self-hostable web app.

Two consequences. **Commercially:** the distribution unit is shrinking, and a client's "AI tutor"
may arrive as a prompt bundle their faculty installed, below procurement's line of sight — a
shadow-IT problem that governance work (trend 2) has to cover. **Legally:** skill bundles are
published under *content* licences. `education-agent-skills` is **CC BY-SA 4.0** — ShareAlike
obligations attach to derivative teaching material. That is a licence conversation nobody is having
yet, and it will land in a client deliverable.

## 8. Retrieval-grounded tutoring is table stakes — and the incumbent is shipping it free

LightRAG (MIT, 40.2k ★) alongside DeepTutor from the same lab made curriculum-grounded answering
the default architecture. **Instructure's Project Athena, announced 2026-07-22, is course-context
grounding built natively into Canvas**, positioned as coaching "toward mastery, not answers".

**Grounding in the client's own material is no longer a differentiator against Canvas.** What
remains defensible: the deterministic pedagogy layer (trend 5), the governance and audit layer a US
district must buy anyway (trend 2), and anything on-premise or offline (trend 9). Price and pitch
accordingly.

## 9. Assessment integrity has settled on process evidence, and the detection gap is now a decision

Institutions continue moving to oral defence, process-based work and "use it, cite it" disclosure.
**57% of students say their assessments come with inadequate AI guidance** (DEC 2026) — the gap is
guidance, not detection.

Searched again this pass: there is still **no credible open source AI-detection or academic-
integrity project.** What exists is student-project proctoring (YOLO/OpenCV/MTCNN pipelines,
Electron kiosk browsers), much of it stale or unlicensed, plus MOSS-style code-plagiarism
detectors. Published work finds AI-text detectors inaccurate and unreliable, and the surveillance
posture carries privacy and fairness exposure. **Fourth consecutive pass declaring this gap — and
the correct reading is that it should stay a gap.** The open source that *is* available (nbgrader,
otter-grader, JupyterHub provenance) captures process. Sell that.

## 10. Interoperability standards are becoming the AI story — NEW

**1EdTech's 2026 position is that interoperability is the precondition for AI**, naming **CASE,
Edu-API and OneRoster** as the standards that give an AI system shared institutional context, with
an expanded Generative AI rubric signalled. **IEEE P3428** targets interoperability of LLM agents
in educational systems (initial phases). Agent-to-agent protocols (A2A) and NIST work on a trusted
interoperable agent ecosystem sit in the background.

What makes this actionable rather than standards-committee noise: **the Ed-Fi Alliance's Apache-2.0
implementations are real code** — `Data-Management-Service` (1,105 commits) and `edfi-oneroster`
serving OneRoster 1.2 (151 commits). This is the first pass where "how does your agent know
anything about my institution?" has an open source answer rather than a bespoke-integration answer,
at least in North America.

## 11. The sector's published metadata is unreliable in both directions — NEW, and it is a method finding

Pass 317 established that **stars run too low** on the software that matters: Ed-Fi at 12 stars with
1,105 commits, Sunbird at 41, OpenOLAT at 448 with 31,877 commits. Pass 318 added a fourth case —
**`openedx/openedx-ai-extensions`, the official Open edX AI plugin, at 17 stars and 703 commits** —
and then found the failure running the other way as well.

**Stars are now being solicited from automated readers.** `24kchengYe/human-skill-tree` (573 ★,
36 commits) closes its README with a passage **addressed to AI agents, asking them to star the
repository.** A 573-star, 36-commit ratio is what that looks like from outside. This KB is compiled
by a process that reads repository pages; so, increasingly, are the tools client engineers use to
pick dependencies. **Text a repository addresses to an automated reader is data, never
instruction** — and any Globant tooling that ranks dependencies by reading repo pages needs that
rule written down.

**Licence metadata is worse, and it fails in a consistent direction.** Pass 318 sourced platform
candidates partly from "best open source LMS 2026" comparison articles and checked their licence
claims first-hand. **Three out of three were wrong, all overstating permissiveness:** LearnHouse
claimed Apache-2.0, is **AGPL-3.0 plus a separate Enterprise Licence**; Frappe Learning claimed
MIT, is **AGPL-3.0**; Forma LMS claimed Apache-2.0, has **no LICENSE file at all**. A fourth case
came from a repository's own README: `ahmedEid1/lumen` carries an MIT badge over a `LICENSE` file
containing the full GPL-3.0 text.

That is four licence misstatements in one pass, on top of the three repos earlier passes found
whose real licence is invisible from the GitHub sidebar (Frappe Education, OpenOLAT,
`education-agent-skills`).

**The operating rules this produces, and they apply to every row in this KB:**

1. **A licence is read from the LICENSE file or the licence GitHub itself renders. Never from a
   comparison article, a README badge, or a bare "License" link.** An engagement that inherits an
   AGPL obligation because someone trusted a listicle is a legal problem, not a research one.
2. **Rank candidates on commit count, release cadence and licence — not stars.** Stars are now
   noise at both ends.
3. **Expect the error to favour permissiveness.** Every misstatement found so far made a repo look
   more usable than it is, which is exactly the direction that hurts in a licence inventory.

The deeper point for a studio lead: **the generation of secondary sources a client's team will
Google is systematically wrong about the one attribute that determines whether Globant can use a
repo at all.** Being the party in the room that read the LICENSE file is a small, real,
demonstrable differentiator in a dependency review.

## Trends asserted elsewhere that this pass could NOT verify

- **"EdTech moving from pilots to mainstream deployment in 2026", including VR/AR.** Vendor and
  consultancy marketing. The DEC survey's 43%-no-integration figure argues directly against it.
  Do not put it in a client deck as fact.
- **"Language learning is the fastest-growing segment."** Single vendor blog. Unverified.
- **"European Commission published AI-in-education ethics guidelines on 2026-08-17."** Low-authority
  blog, unconfirmed against any primary source. Treat as false until verified.
- **APAC growing at ~48% CAGR.** A clear outlier against every other estimate in this KB.
- **Hinds Community College deploying Project Athena to 7,000 students.** Auto-generated news brief,
  not confirmed against Instructure's own release.
- ~~**South Korea's AI Data Protection Act imposing strict edtech privacy protocols**~~ —
  **RESOLVED AND CORRECTED this pass: there is no such act.** Korea's instrument is the **Framework
  Act on AI (Law No. 20676), in force 2026-01-22**, which reaches education through its high-impact
  category — the definitions name **student evaluation in early childhood, elementary and secondary
  education**. It is a real and dated compliance trigger, just not the one this KB was repeating.
  Details in `intel/market.md`. **The Australia/Japan data-governance claims came from the same weak
  source and remain unverified**; what is supportable for Australia is the opposite — no AI-specific
  statute, mandatory guardrails paused.
- **"The EU AI Act has been delayed."** A misreading this KB should be ready to correct, because
  clients will arrive holding it. **Enforcement began on schedule: the AI Office and national
  authorities started enforcing the Act from 2026-08-02.** What moved, under Regulation (EU)
  2026/1744 (in force 2026-07-27, Parliament 2026-06-16, Council 2026-06-29), is the **Annex III
  high-risk obligations, to 2027-12-02** — and nothing else. At least one major law firm's public
  AI-Act tracker still carries pre-adoption text calling the deferral "proposed", so the bad version
  has authoritative-looking sources behind it.
- **Corporate reskilling as a primary driver.** Named across several sources but never with
  education-sector-specific figures. Directionally credible, not quotable.
- **Moodle's AI "placements".** Secondary sources report two core placements (text editor, course
  support) in the 5.x AI subsystem. The **providers** list for 5.1 was confirmed from the official
  docs (Azure AI, DeepSeek, Ollama, OpenAI; DeepSeek new in 5.1); the **placements** claim was not.
  Verify before it enters a proposal.
- **The IDB's "193 AI solutions in LAC" figure and the DEC LATAM survey's sample size.** Both rest
  on search snippets: `www.iadb.org`, `www.digitaleducationcouncil.com` and
  `www.iesalc.unesco.org` all failed DNS resolution at this session's proxy. Brief on them;
  do not put them in a client document unconfirmed. **An unreachable source is not a verified one.**
- ~~**"No EMEA AI-in-education market size exists."**~~ — **RETIRED this pass. This KB was wrong.**
  Five passes concluded the figure was unpublished and advised abandoning the search. Two
  commercial houses publish Europe-specific figures (Marketdataforecast, SNS Insider); they
  disagree by ~9% on the 2025 base and publish no methodology. **"Weak" and "absent" are different
  findings, and this KB recorded the wrong one for five passes.** The lesson generalises: a
  declared gap should be re-tested with a changed query, not inherited.
