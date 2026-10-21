---
industry: education
region: Global
updated: 2026-10-21
---

# Education — current trends

**Pass 358 · 2026-10-21.** Researched **2026-10-21**. Trends 1–6 are corroborated
across external sources. 🆕 **Trends 19–21 are `p358`'s**, and §19 is the first trend on
this file whose evidence is a **licence-hygiene rate** rather than a count of
repositories. Trends 16–18 are `p357`'s.
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
