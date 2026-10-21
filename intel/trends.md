---
industry: education
region: Global
updated: 2026-10-21
---

# Education — current trends

**Pass 361 · 2026-10-21.** Researched **2026-10-21**. Trends 1–6 are corroborated
across external sources. 🆕 **Trends 27–29 are `p361`'s**, and all three are
*measurement* findings rather than sector findings — the pass recovered an instrument
this base had written off and immediately found two published defects with it.
**Trends 24–26 are `p360`'s**: §24 **refutes**
the regional reading of §19 and §22 by designed test, §25 gives the cheap proxy that
replaces it — and the obvious proxy that fails — and §26 names the platform layer this
base had never held. Trends 22–23 are `p359`'s, and §22 reframed §19 without refuting
it; §24 is the test that refutes it. Trends 19–21 are `p358`'s; 16–18 are `p357`'s.
Trends **7–15** are **first-hand observations from this base's own repository
measurements** — they are not in the trade press, which is precisely why they are
worth holding.

🔴 **A provenance note on §§12–15, because it is a defect in this base and not a
finding about the sector.** The live `README.md`'s `p354` section states that three
findings were *"published as `T40`/`T41`/`T42` on `intel/trends.md`"* — the
autograder/online-judge vocabulary gap, the repository-age grant hazard, and Colorado's
replacement AI statute. **None of the three is on this file**, which carries eleven
numbered trends and no `T40`–`T42`. 🔵 This clone is shallow, so `p356` **cannot
attribute** which pass dropped them and does not guess. What it can do is publish them,
re-measured first-hand rather than restated: the vocabulary gap is **§12**, the
repository-age hazard is **§13**, and Colorado is in `intel/market.md` under North
America. Registered as `ACTION ZZ-ba`.

---

## 1. From pilots to governance

The single most consistent signal across every source. 2026 is the year AI in
education stops being a pilot portfolio and becomes governed infrastructure: explicit
policies, data boundaries, oversight. 1EdTech names the shift directly; Campus
Technology's panel expects AI embedded across admissions, advising and learning.

**Consequence for a studio:** the deliverable that wins is the one with an audit
trail, not the one with the best demo.

## 2. Evidence becomes a procurement gate

HolonIQ expects *selective* acceleration in 2026, with education systems demanding
**proof that a product improves learning quality** before buying. This is new: for
three years capability alone sold.

**Consequence:** instrumentation is a feature. Randomised in-LMS experimentation
([`terracotta`](https://github.com/terracotta-education/terracotta), Apache-2.0) moves
from academic curiosity to commercial necessity.

## 3. Purpose-built beats general-purpose

The market is moving away from generic assistants toward platforms built for
education — curriculum-aligned, rubric-aware, standards-mapped. A wrapper around a
frontier model is no longer a product.

## 4. Agentic and adaptive, not conversational

Sources describe agents that **plan and draft teaching materials** and adaptive
systems that adjust difficulty in real time, with the frontier moving from single
prompts toward multimodal, multi-step systems. The repository evidence agrees: the
fastest-growing education projects this pass are agents with memory and sequencing
([`DeepTutor`](https://github.com/HKUDS/DeepTutor), [`Bloom`](https://github.com/Li-Evan/Bloom),
[`Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent)), not chatbots.

## 5. Regulatory divergence is now a design constraint

Three regions, three regimes, all live in 2026: the **EU AI Act** treats admissions
and assessment AI as **high-risk** under Annex III point 3 — with obligations
**postponed to 2 December 2027** by the Digital Omnibus, **Regulation (EU) 2026/1744**
(in force 27 July 2026), while prohibitions, AI literacy and Article 50 transparency
bind now; the **US**
regulates through **134 state bills across 31 states**; **Korea's AI Framework Act**
(22 January 2026) and **Vietnam's risk-based law** (1 March 2026, education named
high-risk) anchor APAC. A single global product configuration is no longer viable.

## 6. Credentials as the skills-based hiring substrate

1EdTech points to digital credentials becoming a core mechanism for skills-based
learning and hiring. [`learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
(MIT, OpenWallet Foundation) is the open reference implementation.

---

## 7. 🟢 MCP has quietly become the LMS integration layer

**First-hand, this pass.** A `topic:education topic:mcp` query returns **328
repositories**. Counting only what this base actually shelves,
**11 distinct education MCP server slugs are shelved** on `agents/top.md`,
and MCP reaches **6 distinct LMS platforms** across both agent shelves.
Every major LMS now has at least one community MCP server, and **almost all are MIT**:

| Target LMS | Servers found | Licences |
|---|---|---|
| Canvas | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`canvas-ed-mcp`](https://github.com/r1ckyIn/canvas-ed-mcp), [`canvas-lms-agent`](https://github.com/likr/canvas-lms-agent) | MIT ×3 |
| Brightspace (D2L) | [`brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server), `brightspace-d2l-mcp` | MIT, unclassified |
| Open edX | [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp), [`openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | MIT, AGPL-3.0 |
| Moodle | [`moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | MIT |
| Google Classroom | [`classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | MIT |
| Anki | [`anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | MIT |
| National/institutional portals | [`schoolinfo-mcp`](https://github.com/chrisryugj/schoolinfo-mcp) (KR), [`ku-portal-mcp`](https://github.com/SonAIengine/ku-portal-mcp) (KR), [`mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (BR) | MIT ×3 |

🟢 **And the cross-shelf census is far larger than the live shelf shows.** The
`recount` instrument folds every MCP address across `agents/top.md` **and**
`agents/trending.md`'s full history, case-insensitively, and counts **159 distinct
education MCP server slugs** by platform:

| Platform | Distinct MCP servers shelved |
|---|---:|
| Canvas | **33** |
| Moodle | **19** |
| Google Classroom / Workspace for Education | **12** |
| Blackboard | **7** |
| Brightspace / D2L | **5** |
| Open edX | **3** |
| Anki | **1** |

🔵 **Read the Canvas and Moodle rows as the finding.** Thirty-three independent Canvas
MCP servers and nineteen Moodle ones means this is not a handful of experiments — it is
a crowded, redundant layer. For an engagement that cuts two ways: the connector is
certainly already written, and almost none of these are maintained to production
standard. **Pick and harden, do not write from scratch, and do not trust a random
one.**

**Why it matters more than it looks.** Education's hardest integration problem has
always been reaching the incumbent LMS, whose licence (AGPL for Canvas and Open edX)
makes forking commercially awkward. MCP solves the licence problem *and* the technical
one at once: it is a **protocol boundary**, so copyleft does not reach across it. The
starting cost of an education engagement has dropped materially, and the trade press
has not noticed.

## 8. 🟢 Skills-as-packaging: curriculum shipped as agent instructions

A new distribution format appeared on this shelf: pedagogy packaged as agent skills
rather than as software or content.
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)
(Apache-2.0), [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills)
(Apache-2.0) and [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
(CC-BY-SA-4.0, **165 skills**) all ship evidence-grounded teaching practice as
instructions an agent loads.

🔵 **Note the licence shift this implies:** when the deliverable is prose rather than
code, the grant moves from software licences to **content licences** — CC-BY-SA
carries share-alike obligations that an MIT codebase does not.

## 9. 🟢 Curriculum-as-open-data is the real moat, and it is regionally lopsided

Agents are commoditising; the **curriculum graph underneath them is not**. This pass
verified five substantial curriculum data assets — and their distribution is uneven
in a way that directly shapes engagement strategy:

| Asset | Region | Licence | Usable commercially |
|---|---|---|---|
| [`bncc-dados`](https://github.com/bncc-dev/bncc-dados) — Brazil BNCC, 1 721 objectives | LATAM | MIT | 🟢 Yes |
| [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) — China K-12, 1 244 nodes | APAC | **CC-BY-NC-4.0** | 🔴 **No** |
| [`knowledge-import-pipeline`](https://github.com/clownjee/knowledge-import-pipeline) — textbook → KG | APAC | Apache-2.0 | 🟢 Yes |
| [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — skills/subject taxonomy | — | ODbL-1.0 | 🟡 Yes, share-alike on derivative databases |
| [`knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | North America | MIT code / **gated data** | 🟡 Per dataset |

**Brazil has official national standards as clean MIT data. Spanish-speaking LATAM
has nothing equivalent.** That asymmetry is the most actionable single fact in this
file.

## 10. 🔴 Licence drift away from OSI in education AI

A counter-trend worth tracking, measured first-hand on this pass's own rows. The more
commercially serious an education AI project is, the less likely its licence is
actually open:

- [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (340 ★) —
  **Elastic License 2.0**: source-available, no managed-service rights.
- [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (1 704 ★) —
  **CC-BY-NC**: the best Chinese curriculum graph, barred from paid work.
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) —
  MIT code, but datasets labelled **Gated** carry **no open licence**.
- [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) — an **IMS
  specification licence**, not a software grant.

🔵 Three of these four read as open source from their GitHub landing page. Licence
due diligence on education AI assets is becoming a billable service in its own right.

## 11. 🔵 A methodological finding, recorded for successors

This base reported **twelve consecutive passes with no new agent row** and published a
denominator defending it. The streak was an artefact of **query shape**: prose legs
("top open source AI agents education 2026") return commercial listicles, while
**topic intersections** (`topic:education topic:llm`, `topic:edtech`,
`topic:education topic:mcp`, `topic:lti`) return repositories. The same channel, asked
differently, produced **26 new verified rows in one pass**.

Generalised: *on this base, a topic intersection is a channel and a prose phrase is
not.* Any future claim of saturation should name which leg shape produced it.

## 12. 🟢 The grading-execution substrate is large, mature and permissive — and nobody calls it AI

**First-hand, `p356`.** Education's code-execution layer — online judges, sandboxes,
autograders — is a **fifteen-row tier headed by 7 137 ★**, and it was absent from this
base's entire 2 000-plus-address corpus until this pass. It is invisible to
agent-shaped discovery because it does not describe itself as AI: it is a queue, a
sandbox and a verdict.

| What it is called | What it does for an education engagement |
|---|---|
| "online judge" | runs untrusted student code safely and returns a verdict |
| "autograder" | scores an assignment and writes feedback back to the LMS |
| "judger" / "sandbox" | the seccomp boundary that makes the above safe to host |

🟢 **And the permissive option is the biggest one.** Six of the fifteen are MIT, BSD or
Apache-2.0, including [`QingdaoU/OnlineJudge`](https://github.com/QingdaoU/OnlineJudge)
(**MIT, 6 552 ★**), a complete Dockerised judge. The GPL-3.0 row most teams reach for
first — `judge0` — is *smaller* than the MIT alternative.

**Consequence for a studio:** any engagement that grades code — bootcamps, CS
departments, developer academies, certification bodies — has a licence-clean,
production-grade base available today. Costing that work as a build is now wrong.

## 13. 🔴 Education's grant hazards fail CLOSED, and the cause is repository age

**First-hand, `p356`,** confirming a mechanism this base had stated and never shelved.
Of **36 repositories probed this pass**, the default branch is **`master` for 18**,
`main` for 16, and something else entirely for 2 — `newnew` and `Version-1`. 🔴 **A
sweep that probes `main` only reports 20 of 36 (55.6 %) as grantless.**

The same age effect drives the grant *path*: of this pass's 36 rows, the grants not at
`LICENSE` sit at `license.txt` (lower-case), `LICENSE.txt`, `LICENSE.md` and
`docs/License.txt`.

🔵 **Why it compounds.** GitHub's default moved to `main` in 2020; education
infrastructure is mostly older than that. Every failure here is the same direction:
**a live, correctly-licensed repository reads as unlicensed**, so tooling calibrated on
2024-era repositories systematically **under-reports what education has**. That is the
opposite of the usual risk, and it means a "no open option exists" finding in this
sector should never be trusted without checking the branch and the path.

## 14. 🔴 A badge is not a grant — and three of this pass's rows prove it differently

**First-hand, `p356`.** Three high-visibility repositories read as MIT and are not:

| Row | The appearance | The payload |
|---|---|---|
| [`reneverland/CBIT-AiExam-plus`](https://github.com/reneverland/CBIT-AiExam-plus) (277 ★) | an MIT shields.io badge at the head of the README | the `LICENSE` the badge links to **404s**, along with four other rungs. **No grant exists** |
| [`JinLingxi/MathCyclus…`](https://github.com/JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant) (147 ★) | nothing visible | one prose sentence in the README claiming MIT. A pointer, not a licence |
| [`lebmatter/exampro`](https://github.com/lebmatter/exampro) (72 ★) | MIT, per GitHub | stock MIT at `license.txt` with **`Copyright (c) [year] [fullname]` never filled in** — family certain, **licensor absent** |

🟢 **And the mirror case, which is the useful half:**
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) (575 ★)
reads as plain AGPL-3.0 and is a **split grant**: a 1 134-byte short-form AGPL notice
*plus* an explicit option to use everything under `skills/` as **MIT**. The code is
network copyleft; the curriculum is embeddable.

🔵 **Two lessons for licence diligence as a billable deliverable (`§10`).** First, the
channels that look authoritative — the badge, the classifier, the README — are the
three that were wrong here. Second, **size tells you nothing**: an AGPL-3.0 notice at
1 134 bytes is MIT-sized, so any byte-band heuristic reads it as permissive. Open the
file.

## 15. 🔵 APAC's "gap" is in the trade press, not in the supply

**First-hand, `p356`.** For the **fifth consecutive pass**, the prose leg asking about
APAC AI-in-education adoption returned no education-specific figure — only
general-enterprise AI material. In the same pass, the function legs placed **18 of 36
verified rows in APAC**: China, Hong Kong, India, Korea, Bangladesh and Iran, across
item banks, judges, graders and scheduling agents.

🟢 **So the two measurements disagree, and the repository evidence is the better one.**
What APAC lacks is an English-language analyst narrative; what it has is first-party
education software in volume. An engagement brief that reports "APAC adoption data
unavailable" and stops there is describing the trade press, not the region.

---

## 16. 🔴 🆕 The AI-detector market is being abandoned by its own customers — and this base shelves four detection repos

**`p357`, external sources, North America-led but assessment-wide.** The single
sharpest reversal in this pass's legs: **US universities are giving up on AI
detectors.** Yale, Cornell and the University of Wisconsin–Madison now **discourage or
bar the use of AI-detection scores in academic-misconduct cases**, on false-positive
grounds. The figure driving it is an equity problem, not a quality one: a Stanford
study found detectors flagged **61 % of essays by non-native English speakers** as
machine-written.

🟢 **What replaces detection is not a better detector.** The same sources describe the
substitution directly: **oral examination, proctored assessment, and grading the
writing *process*** rather than the artefact.

🔴 **This cuts against supply this base carries.** Four rows exist to detect or monitor:

| Row | What it does | What §16 does to it |
|---|---|---|
| [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) | vision-based exam monitoring | 🔴 Demand-side risk — the institution may not accept the evidence |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | proctoring subsystem for Open edX | 🟢 **Survives** — *proctored assessment* is named as a replacement, not a casualty |
| [`eLearning-BS23/moodle-quizaccess_proctoring`](https://github.com/eLearning-BS23/moodle-quizaccess_proctoring) | Moodle proctoring access rule | 🟢 Survives, same reason |
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | source-code **plagiarism** similarity | 🟢 **Survives, and is the distinction that matters** — it compares submissions to *each other*, and makes no claim about machine authorship |

🔵 **The distinction is the finding, and it is a sentence a studio can use in a
procurement meeting.** What is collapsing is **authorship attribution** — the claim
"a machine wrote this" — because it cannot be made at an acceptable false-positive rate
across language backgrounds. **Supervision** (proctoring) and **similarity**
(plagiarism) are untouched, because neither claims to know what produced the text.

🟢 **The build consequence, stated as an opportunity rather than a loss.** Process
evidence is a *telemetry* problem, and telemetry is what this base's interoperability
tier is for: **Caliper** events and **xAPI** statements already carry draft history,
revision sequence and time-on-task. An engagement that instruments the writing process
through [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) (🔴 implement
the standard, do not vendor the document) is building the thing detection is being
replaced *with* — and
[`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
(Apache-2.0) can run it as a randomised in-LMS study, which §2's procurement gate asks
for anyway.

🟡 **Scope honesty.** Three named institutions and one study is a strong signal, not a
census; the sources are trade briefings. The *direction* is well corroborated across
this pass's leg, the extent is not measured, and no policy date is asserted.

## 17. 🔴 🆕 AI marking has acquired a disclosure duty and a measured anchoring bias

**`p357`, external sources, APAC-first.** Two findings that belong together, because one
is the hazard and the other is the response.

🔴 **The hazard is measured.** An experiment with **1 339 teachers** found that a harsh
AI-assigned grade **survived human review more often when the review was told the grade
came from AI**. The human-in-the-loop is not a neutral check: labelling a grade as
machine-produced **anchors** the reviewer to it. 🔵 That is the inverse of the
assumption nearly every grading-agent design rests on — that disclosure plus human
review makes automated marking safe.

🟢 **The response is already institutional policy.** The **University of Newcastle
(Australia)** requires that any use of generative AI in marking be **communicated to
students**, with students given the **opportunity to opt out**.

🟢 **Together they define the design constraint for every grading agent on this base.**
A rubric-bound grader is not safe because a human signs off, and it is not compliant
because it discloses. Three things follow, and all three are buildable:

1. **Blind the reviewer to provenance** on the first pass. The anchoring effect is
   attached to the *label*, so withhold the label until the human has scored.
2. **Build the opt-out as a data path, not a policy page.** A student who opts out
   needs a human-marked route that the LMS can actually route to —
   [`ltijs`](https://github.com/Cvmcosta/ltijs) (Apache-2.0) and
   [`pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) carry the role claims
   that make that routing possible.
3. **Keep the rubric as the artefact of record**, which is why the item-bank and
   rubric-bound tier on `agents/top.md` is the right starting point: a rubric score is
   reviewable in a way a model's judgement is not.

🔵 **Why this is a trend and not a caveat.** §2 established that evidence is a
procurement gate. §17 says the evidence will be asked for about **the marking process
itself** — disclosure, opt-out and reviewer independence — and a studio that can show
all three has a procurement answer competitors will not.

## 18. 🔴 🆕 Non-OSI licensing in education AI now has a second shape: the noncommercial source-available build

**First-hand, `p357`.** §10 recorded licence drift away from OSI terms. `p357` adds a
measured instance of a **different** shape, and the shape matters more than the count.

| Shape | Example | What it does to a paid engagement |
|---|---|---|
| **Source-available, commercial-hostile** | [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) — Elastic License 2.0 | Cannot be offered as a managed service |
| **Data-only noncommercial** | [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) — CC-BY-NC-4.0 | Unusable in paid work |
| 🆕 **Noncommercial source-available software** | [`mrgutierrezmario/lecture-note-app`](https://github.com/mrgutierrezmario/lecture-note-app) — **PolyForm Noncommercial 1.0.0** | Usable for study, research and charities; **commercial use needs a separate licence from the holder** |
| 🆕 **Open-core copyleft connector** | [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) — AGPL-3.0, README names it the connector behind a commercial product | Network copyleft reaches the agent talking to it |

🔴 **Both new rows call themselves open source and both would pass a keyword filter.**
PolyForm Noncommercial is a real, well-drafted licence from a credible source — it is
simply not an open-source one, and its text is friendly enough that it reads as
permissive on a skim: *"you may use, modify and share it for noncommercial purposes."*

🟢 **The operational rule this base already follows is what caught both: read the
payload, then read it for a *field* rather than a family name.** The PolyForm row needed
the word **"noncommercial"**; the AGPL connector needed the realisation that **a
connector sits inside the engagement**, not across the protocol boundary that keeps a
copyleft *platform* at arm's length. 🔵 **The second one is the genuinely new idea**:
this base's governing rule — reach copyleft over LTI, web services or MCP — assumes the
copyleft thing is the *platform*. When the copyleft thing **is the MCP server**, the
boundary is on the wrong side of it, and the rule inverts.

---

## 19. 🔴 🆕 In one region, "no open source for this" means "no LICENSE file", and the two are opposite problems

🟢 **`p358` measured it.** Sixteen LATAM-origin education addresses were run through the
payload channel: **13 live, and 3 carry a grant — 23 %.** The same pass's other legs
(LTI, MCP, assessment, Africa) returned **19 live and 14 grants — 74 %**.

🔵 **The reason this is a trend and not a statistic** is that three consecutive passes of
this base reported the same observation as a *supply* problem. `p356` called it a supply
gap, then refined it to a **tooling** gap: *"what does not exist is a Spanish-language
item bank, autograder or judge."* 🔴 All three exist. A Saber Pro item bank
(`DVLASZ/banco-preguntas-saberpro`), an autograder doing RAG over open answers
(`Jairh1294/Auto-Grader`), four ENEM platforms, a BNCC municipal assessment platform.
**They are all rights reserved.**

🔴 **The two diagnoses imply opposite actions, which is why the distinction is expensive:**

| Diagnosis | What a studio does | Cost |
|---|---|---|
| Supply gap (wrong) | 🔴 build the item bank | weeks of authoring |
| Licence gap (right) | 🟢 **ask the author for a `LICENSE`** | an email |

🟢 **And it explains a search-channel artefact that has misled this base twice.** A
listicle or a trade roundup lists what it can *link*, and an unlicensed repository links
exactly as well as a licensed one — so prose legs show supply where the payload shows
none, and the absence only appears when something reads the `LICENSE` file. 🔵 **The
general form: discovery channels measure existence; only the payload channel measures
usability**, and for a paid engagement usability is the only one that counts.

🟡 **The bound on this, stated because the 23 %/74 % figure is quotable.** The comparator
is this pass's **English-language** legs — a different, uncontrolled population. The
split measures two samples and is **not** evidence that LATAM authors license less
carefully; it could as easily reflect project age or venue. **`ACTION ZZ-bf`** registers
the control: run the same function-word legs in a third language and compare.

## 20. 🟢 🆕 Four jurisdictions, four statutes, one product: the oversight record is converging

🟢 **`p358`'s four regional legs returned the same build requirement under four unrelated
legal justifications** — an **age gate**, a **human-in-the-loop record** and an **audit
trail**:

- 🔴 **EU AI Act**, enforced by the AI Office and national authorities **from 2 August
  2026**: admissions, student evaluation and exam scoring are **high-risk**, bringing
  conformity assessment, technical documentation, logging and human oversight.
- 🔴 **Vietnam Law 134/2025/QH15**, in force **1 March 2026** — the region's first
  dedicated AI statute. **Education is one of six high-risk sectors**, naming automated
  assessment and behavioural monitoring; compliance by **1 March 2027**, with six extra
  months for systems running before 15 August 2026.
- 🔴 **South Korea's AI Basic Act**, effective **January 2026**: risk management and
  disclosure for high-impact systems.
- 🟢 **US states and districts**: Oklahoma and Maryland require human oversight and bar
  AI from high-stakes student decisions; **Charleston County** bars AI as the *sole
  basis* for discipline or placement; **Katy ISD** bans generative AI for **K-6** and
  phases in supervised access from grade 7.

🔵 **The architectural reading.** These are not content-moderation requirements and not
model-selection requirements. They are **provenance requirements**: show who decided,
show a human saw it, show the record. 🟢 **Two rows this base verified on `p358` already
embody the two auditable answers**, and both are MIT:
[`AnonymousOnyx22/canvas-lms-student-mcp`](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp)
is read-only **by construction** — a *capability ceiling* — and
[`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) makes every
write tool preview-first, refusing to mutate without `confirm_write=True` — a
*confirmation protocol*.

🟢 **So "AI may not decide" has two implementations and an engagement should know which
it is selling:** remove the capability, or gate it behind a recorded human confirmation.
🔵 The first is cheaper to audit and the second is the only one that still does the work.

🔴 **One counter-current, recorded so the convergence is not overstated.** The **Ipsos
Education Monitor 2026** finds **lower** support for banning AI in schools across the
Asian markets surveyed and **higher** support in **Australia and New Zealand** — i.e. the
jurisdictions with the strictest statutes have the most permissive publics, and
Australia, which relies on technology-neutral law with its mandatory guardrails
**paused**, has the most restrictive public opinion. 🔵 **Statutory pressure and social
licence are not the same axis**, and in APAC they point opposite ways: the objection to
handle in Hanoi or Seoul is documentary, and in Sydney it is consent.

## 21. 🔵 🆕 A connector's copyright holder is a maintenance forecast, and this base now has two instances

🟢 **`p358` discharged `ACTION ZZ-bc` and the result generalises.** Reading the copyright
holder out of the `LICENSE` payload across rows sharing a slug stem found **two copies
whose grant names a different repository's owner** — and in **both** cases the copy was
measurably behind its upstream:

| Upstream | Tools | Copy | Tools | Behind by |
|---|---:|---|---:|---:|
| `vishalsachdev/canvas-mcp` | 126 | `NelsonSpencer/canvas-mcp` | 99 | **27** |
| `bruchris/canvas-lms-mcp` | 183 | `algorithm0r/canvas-lms-mcp` | 165 | **18** |

🔵 **Why this is a trend rather than two anecdotes.** The MCP connector tier is the
fastest-growing supply in education AI — six independent Canvas addresses on this base
now — and it grows partly by **copying**, because an MCP server is small enough to fork in
an afternoon. 🔴 Nothing in the licence separates a copy from its upstream (all MIT, all
live, all verifying), and on this tier **not even the description does**:
`algorithm0r/canvas-lms-mcp` and `bruchris/canvas-lms-mcp` publish the *same sentence*.
🟢 **The holder field is the only cell that separates them**, and in two of two cases it
predicted staleness.

🟡 **Two measured limits.** The test only reaches rows sharing a **slug stem** — a renamed
copy is invisible (**`ACTION ZZ-be`** keys it on the holder string instead) — and it is
**blind to Apache-2.0 rows**, whose boilerplate carries no holder field at all, as
`edugatorlabs/ltijs` demonstrated against `Cvmcosta/ltijs`.

🟢 **The engagement rule is simple and cheap:** before vendoring any connector, read its
`LICENSE` holder. If it names someone other than the repository owner, you are looking at
a fork — install by registry identifier, which resolves upstream, and keep the capability.


## 22. 🔴 🆕 A `LICENSE` file is a distribution habit, not a regional one — and that reframes §19

🟢 **§19 stands as a measurement and is re-named here.** `p358` measured LATAM education
AI at **23 % permissive against 74 % elsewhere** and called it a regional licensing gap.
🔴 **`p359` ran eight legs aimed at *functions* and never named a region, and the
permissive rate came back at 31 %** — within a few points of the LATAM figure, from a
sample drawn without reference to geography.

🟢 **The variable that predicts a missing grant is who publishes, not where they are.**
Sixteen addresses new to these shelves, every licence read from the payload, every
producer type read from the repository itself:

| Producer type | Addresses | Permissive | No grant at all |
|---|---:|---:|---:|
| Teacher, parent, hackathon team or civic-innovation lab | 7 | **1** | 4 *(+2 explicitly noncommercial)* |
| University research lab *(an AAAI 2026 oral, an LMU NLP group, a CRAN package)* | 3 | **0** | 2 *(+1 GPL declared in `DESCRIPTION`)* |
| Volunteer regional data publisher | 2 | **0** | **2** |
| 🟢 **Vendor or organisation shipping tooling for others to deploy** | 4 | **4** | **0** |

🔵 **The mechanism is mundane and that is why it generalises.** A `LICENSE` file is not a
legal opinion — it is a **step in a release checklist**. Someone who publishes a package
to npm, PyPI, crates.io or a plugin directory acquires that step because the registry, the
CI template or the first downstream user forces it. 🔴 **Someone who publishes a tool they
built for their own classroom, their own child's IEP, or their own paper never encounters
the forcing function.** They are not withholding a grant; they have not been asked for
one.

### 🟢 The control case is inside one country and one month

| Publisher | What it ships | Grant |
|---|---|---|
| **`bncc-dev`** *(Profy Tecnologias Educacionais Ltda — a company)* | Brazil's BNCC as 1 721 verified learning objectives, plus npm/PyPI packages, an MCP server and a hallucination benchmark | 🟢 **MIT code + CC BY 4.0 data**, per-record provenance, a reproducible extraction pipeline, and a reasoned statement of *why* the data is licensable at all |
| [`pedrosoale/tempo-docente`](https://github.com/pedrosoale/tempo-docente) | BNCC, SAEB and SARESP data *"com fonte oficial"* | 🔴 **no grant**, 7 paths probed |
| [`SayvaBR/assistente-ped`](https://github.com/SayvaBR/assistente-ped) | a pedagogical assistant adopting BNCC provenance | 🔴 **no grant**, 7 paths probed |

🔵 **Same country, same subject matter, same month, opposite licensing.** The difference
is not Brazil. 🟢 **One is a company that ships packages; two are people who publish
data.**

### 🔴 Why the reframing changes what a studio does about it

🔴 **Read as regional, §19 implies a regional remedy** — a LATAM licence-hygiene
initiative, a Portuguese-language `LICENSE` template, a regional partner. 🟢 **Read as a
producer-type effect, the remedy is the same everywhere and it is cheaper:** when an
engagement's best technical fit is a teacher's, parent's, lab's or volunteer's
repository, **ask for the grant**. The author has no reason to refuse and usually has no
position at all — and a two-line email is the whole intervention.

🔵 **It also tells a studio where *not* to look for a licence problem.** The four
vendor/organisation rows are 4 for 4 permissive. 🔴 **And three of those four are stale or
near-empty** — `OpenLRW` dead since 2018, `OpenProct/openproct` at four commits,
`eribean/girth` untouched since 2022. **Shipping for others produces a `LICENSE` file
reliably and maintenance not at all**, so the two risks are *anti*-correlated: the rows
with clean grants are the ones to check for a pulse, and the rows with a pulse are the
ones to check for a grant.

🟡 **Stated limits.** `n = 16`, drawn from eight function legs in one pass, with producer
type read by hand from each repository rather than from a field. 🔵 The direction is
strong (4/4 against 1/12) and the sample is small; what makes it worth holding is that it
**predicts** where to spend verification effort, which §19's regional reading does not.

## 23. 🔴 🆕 Special education is the industry's largest licensed-supply hole, and it is a statutory function

🟢 **The demand is not in question and the supply exists.** An IEP is a **statutory
document** — under IDEA in the United States, and with force of law in most of the
jurisdictions on `intel/market.md`. 🔴 **What does not exist is a grant.** Seven
special-education addresses measured first-hand at `p359`:

| | Count |
|---|---:|
| 🟢 permissive *(MIT)* | **1** |
| 🔴 explicitly **noncommercial** *(CC-BY-NC-4.0, PolyForm NC)* | **2** |
| 🔴 **no licence file at any of 7 probed paths** | **4** |

🔴 **And the two best-maintained addresses on the tier are both noncommercial by
construction** — `The-Burnes-Center/a-iep` at 836 commits and 7 authors, and
`boktoday/iep-agent-hermes-agent`. 🔵 That is the inverse of the usual trap: it is not
that the usable rows are immature, it is that **the mature rows are the ones a paid
engagement cannot touch.**

🟢 **Scoped honestly, because this base has over-corrected here before.** These are the
seven addresses `p359` measured, and the *"zero permissive for special education"* claim
filed as `T-p288b` remains **CORRECTED**. 🔴 **But it is corrected by one row.**
[`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) is **MIT** (verified
first-hand at `p359`) and ships a `special-education-agent` among twelve specialists.
`eakarsu/ai-special-education-iep-compliance` — held on these shelves, and the closest
thing here to an IEP *compliance* surface — carries **no grant in 21 files**, also
re-confirmed at `p359`.

🟢 **So the whole permissive special-education supply this base can name is two
addresses:** `iblai/k-12-agents` and `p359`'s `dg13788/iep-system` (38 commits). 🔵 Two
usable addresses against a statutory function in every major jurisdiction is the measured
form of this trend, and it is why §23 is a market condition rather than a shelf gap.

🔵 **Why it reads as a trend rather than a shelf fact.** Special education concentrates
every pressure the rest of this file tracks: §1's governance shift (an IEP decision is
exactly the "high-stakes decision about a student" that Oklahoma and Maryland now require
human oversight of), §2's evidence gate, §5's regulatory divergence (Annex III of the EU
AI Act names education assessment by type), and §17's disclosure duty for AI marking.
🟢 **A function under that much statutory pressure attracting almost no licensed open
source is a durable market condition, not a gap waiting to close** — and it is the
clearest build-rather-than-adopt case on these shelves. 🆕 **Pattern 16** on
`compose/patterns.md` is the build.

## 24. 🟢 🆕 `ACTION ZZ-bf` discharged: the regional licensing reading is refuted by designed test, not merely reframed

🟢 **§19 measured it, §22 reframed it, and §24 tested it.** The distinction matters.
`p358` measured LATAM education AI at **23 %** permissive against **74 %** elsewhere and
read it regionally. `p359` got **31 %** from eight legs drawn *without reference to
geography* and concluded the variable is who publishes — a reframing from a sample that
could not isolate region. 🟢 **`p360` held region as the variable deliberately**, running
`p358`'s exact method — web search aimed at `github.com`, vernacular **function words**,
no prose — in two languages belonging to two different regions.

| Leg | Language | Region | Live | Grant read from payload | Grant rate |
|---|---|---|---:|---:|---:|
| `p360` | 🇫🇷 French | **EMEA** | 19 | 6 | 🔴 **31 %** |
| `p360` | 🇮🇩 Indonesian | **APAC** | 20 | 3 | 🔴 **15 %** |
| `p358` | 🇪🇸🇵🇹 Spanish / Portuguese | **LATAM** | 13 | 3 | 🔴 23 % |
| `p358` | 🇬🇧 English | mixed | 19 | 14 | 🟢 **74 %** |

🔴 **LATAM sits in the middle of three non-English populations, not at the bottom.** Four
languages, three regions, three independent collections: **15 %, 23 %, 31 %** against a
single English outlier at **74 %**. 🟢 **Nothing about Latin America was ever being
measured**, and this base came within one registered action of publishing that it was.

🟢 **What is actually being measured is project kind.** The vernacular legs return
single-author apps built against one country's curriculum — a *rapor* generator for
Kurikulum Merdeka, a *cahier de textes*, a Saber Pro item bank. The English legs return
frameworks, libraries and MCP servers published by organisations. 🔵 **Language and region
were riding along with publisher type the whole way**, which is why two passes that never
controlled for it both found the same number.

🟢 **The engagement consequence is unchanged in substance and much stronger in standing.**
For any region, assume the nationally-specific supply is unlicensed until the payload says
otherwise, and treat **"ask the author"** as a first-class option — the fix is one file and
it costs an email. 🔴 What must stop is the inference that a regional development culture
is careless. It was never in the data.

## 25. 🟢 🆕 A cheap proxy for licence hygiene — and the obvious proxy fails

🟢 **Both candidate proxies cost one `ls-remote` and neither needs the GitHub index**,
which has now been **403** for five consecutive passes. Measured across the **39 live**
addresses of §24's two legs:

| Proxy | Bucket | n | With a grant | Rate |
|---|---|---:|---:|---:|
| 🟢 **≥ 1 git tag** | tagged | **7** | **4** | 🟢 **57 %** |
| 🟢 **0 git tags** | untagged | **32** | **5** | 🔴 **15 %** |
| 🔴 Branch count | 1 | 22 | 5 | 22 % |
| 🔴 Branch count | 2–4 | 10 | 1 | 🔴 **10 %** |
| 🔴 Branch count | 5+ | 7 | 3 | 42 % |

🟢 **Tag presence separates by 3.7×.** Cutting a release and writing a licence are the same
habit — the moment someone intends another person to *use* the thing, both appear.
🔴 **Branch count does not separate at all**: it is non-monotonic and the middle bucket is
the worst of the three.

🔵 **Published as a pair on purpose.** Branch count is the proxy anyone would reach for
first, and it is useless here; the tag channel is incidental and it works. That is only
visible because both were measured rather than one being assumed — and it is the reusable
lesson, not the ratio. 🟡 **n = 39, so this is a signal to re-test, not a law** —
`ACTION ZZ-bi` re-measures it on the next vernacular leg and is 🔴 *refuted if the tagged
bucket does not beat the untagged one by at least 2×*.

## 26. 🔴 🆕 The national school *portal* is the unclaimed layer, and education's interchange layer is not

🟢 **This base's own shelves make the asymmetry visible.** The interchange layer is
richly supplied and largely permissive: LTI 1.3, SCORM, xAPI, Caliper, LRS
implementations, OneRoster. The **platform** layer is a row of LMSes. 🔴 **The layer in
between — the thing a region actually procures for every school in it — had no row on this
base for 359 passes.**

🟢 **There is exactly one substantial open implementation and `p360` shelved it.** France's
**ENT** (*Espace Numérique de Travail*), standardised by the Ministry of Education and the
Caisse des dépôts since **2003**, procured per *région*, with `edificeio/entcore` as its
modular kernel: **AGPL-3.0**, 21 authors, a commit on **2026-10-20**.

🔴 **Three structural facts make this a trend and not a repository note.**

1. 🔴 **The scale is procurement scale, not project scale.** One French region's
   deployment reports **2.7 M users across 5 790 institutions**. The incumbent comparison
   is not a GitHub project; it is Pronote and a public tender.
2. 🔴 **Coverage is incomplete and officially criticised.** The IGÉSR inspectorate (15 Jul
   2025) puts ENT in **62 %** of French public primary schools and records that one family
   can face **three different solutions** across école, collège and lycée, recommending
   harmonisation. 🟢 **An inspectorate asking for harmonisation is a migration market.**
3. 🔴 **The licence sets the architecture before anyone chooses one.** The whole tier is
   **AGPL-3.0**, so network copyleft reaches a fork but not a separate service over its
   HTTP API. 🟢 Every viable pattern here is a service beside the portal.

🔵 **The generalisable point for other regions.** The portal layer is where statutory
data lives — the lesson log, attendance, the competency record — and statutory data is
what an AI feature needs and what an institution will not let leave. 🟢 **The layer is
under-supplied in open source everywhere, and in the one place it exists it is copyleft.**
That combination is a build-and-integrate market rather than a customise-a-platform one,
and it is the opposite of the `Moodle` or `Open edX` engagement shape this base is
otherwise organised around.

## 27. 🔴 🆕 A channel recorded as closed stayed closed for five passes because nobody enumerated its transports

🔴 **`p356` through `p360` each recorded `api.github.com/search/*` **403** and reasoned
that a credential scoped to one repository cannot read the index. The 403 was real. The
inference was wrong.** The same query, in the same session, on the same credential,
through the session's **GitHub MCP search tool**, returns the index in full — stars,
forks, default branch, topics, `archived`, `pushed_at`, SPDX classifier.

🔵 **The boundary turned out to be per-tool, not per-credential.** `search_repositories`
answers for any public repository; `get_file_contents` refuses anything outside the two
attached repositories with an explicit scope error. 🟢 **One tool on a credential being
scoped says nothing about another tool on the same credential.**

**Cost of the error, measured:** 78 star cells published as `not re-derived` across two
files, five passes of discovery conducted with function-word web queries instead of
ranked search, and — see §28 and §29 — **two corpus defects that the available channels
were structurally incapable of finding.**

**Consequence for a studio.** 🟢 **Before recording a data source as unavailable,
enumerate every transport that reaches it** — SDK, CLI, MCP tool, proxy, partner API —
and record *which transport* failed, not *which source*. A client engagement that writes
off a data source on one failed transport builds the wrong architecture around the gap.
🔴 This base did exactly that for five passes, and it is the cheapest mistake on this
file to avoid.

## 28. 🔴 🆕 Absence from a search index is not death — and the mechanism is fork exclusion, rename, and transfer

🔴 **The GitHub index resolved 261 of this corpus's 277 addresses. All 16 of the rest are
alive on `git ls-remote --symref`.** A pass that had read index absence as death would
have published **16 false deaths, 5.8 % of the base**. `p361` established the mechanism
for 15 of the 16 by designed test:

| Mechanism | n | Proof | Recovery |
|---|---:|---|---|
| **Fork exclusion** — repo search omits forks unless asked | **12** | re-query `fork:true`: all 12 return, all 12 carry `fork: true` | add `fork:true` |
| **Repository rename** | **1** | `openedx/edx-platform` and `openedx/openedx-platform` return the **same HEAD SHA** | index holds the new name only |
| **Owner rename / transfer** | **2** | `naiayti/TeachingKG` ≡ `Teaching-Knowledge-Graph/TeachingKG`; `christophblessing/quiz-recap` ≡ `openHPI/quiz-recap` — identical SHAs | search by name, not address |
| **Unexplained** | **1** | `JeabtiE/jump-hackathon-demo` live, absent under `fork:true` and by name | 🔴 stated, not guessed |

🔴 **And fork exclusion is not merely a counting artefact — it is how a bad row gets
shelved.** `p359` published [`jeffyding/OpenLRW`](https://github.com/jeffyding/OpenLRW)
as *"the only address that carries OneRoster"*. It is a **fork at 0 ★**, created and
last touched the same day in 2018. The canonical upstream
[`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
has **62 ★** and a different HEAD. 🟢 **A ranked search puts 62 ★ above 0 ★ and the
question answers itself; a non-ranked search cannot tell them apart at all.** This base
already held the same organisation's `Larissa` and still shelved a fork of its sibling
project.

**Consequence for a studio.** 🟢 Liveness is a `git` question and must be answered on
`git`. Discovery and ranking are index questions. 🔴 **Using either instrument for the
other's job produces confident, wrong rows** — and the failure is silent in both
directions: the index invents deaths, and `ls-remote` cannot see a fork, a rename or an
archive.

## 29. 🔴 🆕 Three fields called "recency", a 6½-year spread, and only one of them is a commit

🔴 **Measured on one address this pass,
`Apereo-Learning-Analytics-Initiative/OpenLRW`:**

| Field | Value | What it tracks |
|---|---|---|
| `updated_at` (the field a minimal search returns) | **2026-08-04** | repository *metadata* — stars, topics, watches |
| `pushed_at` (full output only) | **2025-09-12** | a push to *any* ref, a tag or a branch delete included |
| 🟢 `git log -1` on the default branch | **2020-02-06** | 🟢 **the last commit** |

🔴 **A shelf built on `updated_at` publishes a project abandoned in 2020 as current**, and
`updated_at` is the field that comes back by default. 🔵 This generalises a rule
`p359` found on a GitHub *topic page* ("updated September 2025" for a 2018 fork) to the
API's own fields: **a date that is not a commit date is not a maintenance signal.**

🟢 **And one property exists only in the index, which is the mirror of §28.** `archived`
— read-only upstream, no commits or issues ever again — is nowhere in `git`, and an
archived repository answers `ls-remote` exactly like a healthy one. 🟢 **`p361` swept all
277 addresses (`archived:true fork:true`): one hit, `zmievsa/autograder`, published
unflagged on `repos/foundations.md`** — the shelf whose stated purpose is *the systems an
engagement starts from*. 🔴 **360 passes of liveness sweeps could not have found it.**

**Consequence for a studio.** 🟢 Three questions, three instruments, and they do not
substitute: *does it exist* → `ls-remote`; *is it maintained* → `git log` on the default
branch; *is it still open for contributions* → the index's `archived` flag. 🔴 **Any
dependency recommendation that answers fewer than three of those is incomplete**, and
the third one is the one every open-source due-diligence checklist this base has seen
omits.
