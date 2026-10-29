---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI — Current Trends

**Pass `p530` · 2026-10-29.** **Fifteen** trends. Each one is stated so it could be
*wrong* — a trend you cannot disconfirm is a slogan. Where this pass's evidence
**narrowed or contradicted** a trend carried from `p526`, that is marked and the
trend is rewritten rather than quietly restated.

> 🆕 **`p528`, a same-day second pass**, rewrote **Trend 4** (the Moodle reading
> was wrong in shape), sharpened **Trend 9**, and added **Trend 11** on a
> deletion. Trends 1–3, 5–8 and 10 were not re-evidenced this pass and stand on
> `p527`'s sourcing.

> 🆕 **`p529` rewrote Trend 4 again — `p528`'s shape was right and its magnitude
> was wrong by 20× — and added Trends 12 and 13.** Trend 12 is the one a client
> hears first: **the unit of LMS integration is the institution, not the
> product.** Trend 13 is about this base's own instruments. Trends 1–3, 5–11
> were not re-evidenced this pass and stand on their recorded sourcing.
> 🟢 **Trend 2 gained hard numbers:** `DeepTutor` **49,216★** and `OpenMAIC`
> **41,756★**, API-exact rather than rounded.

## 1. The governance gap is the market

Adoption is near-universal and governance is near-absent. **86%** of students
across 16 countries use AI (Digital Education Council); **53%** of K-12 teachers
use generative AI for work, up from 25% in a year (RAND); most US public schools
still have no formal AI policy (Child Trends / US Dept. of Education).

🟢 **Sharpened this pass with a named primary and a sample.** UNESCO IESALC +
UNU-IAS surveyed **200 LATAM higher-ed institutions across 19 countries**:
**87% use AI somewhere, 26% have a formal AI strategy.** A **61-point** deficit,
and the study's own explanation is the important half — adoption is driven by
**individual faculty and students, not institutional policy**. The AI is already
inside the institution, unmanaged.

**So the scarce good is not a tutor. It is a defensible, auditable tutor** — and
increasingly, **governance over AI the client already has** rather than new AI.

**What would disconfirm it:** governance figures catching up to adoption
figures inside a year, or buyers paying for capability over auditability.

## 2. Open-source education agents are APAC-academic, and they are large

[DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0, **49.0k★**, Univ. of
Hong Kong) and [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (MIT, **41.8k★**,
Tsinghua) are the two largest open-source education agents in the world, both
permissive, both from APAC university labs, **90.8k★ between them**. Both cut
releases on 28-29 October 2026. Four of the thirteen agents on
[`../agents/top.md`](../agents/top.md) are APAC-placed; one is EMEA-placed; none
is LATAM-origin.

**What would disconfirm it:** a North American or European lab shipping a
permissive education agent at 10k★+, or either of these two changing licence.

## 3. Pedagogy is becoming measurable, and almost nobody is measuring it

Two artefacts now exist for "is this agent any good *as a teacher*", as distinct
from "is it any good at the subject":
[pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT)
running **CDPK** and **SEND**, and
[k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
(Apache-2.0, 601★) shipping **eval rubrics** alongside the skills.

🟢 **New evidence, and it is a sales argument.** The pedagogy benchmark is built
on exams from **Chile's Agencia de la Calidad de la Educación and CPEIP**, and
the **SEND** half covers special educational needs and disabilities — the area
where regulators and parents apply the most pressure and where essentially no
vendor can show evidence. Thirteen stars on the repository. 🆕 The **OECD 2026
Digital Education Outlook** reportedly tells institutions to move **beyond
general-purpose AI toward purpose-built educational AI**, which is the same
argument arriving from the procurement side.

**So:** running a pedagogy benchmark costs almost nothing and almost nobody does
it. That asymmetry is a differentiator for as long as it lasts.

**What would disconfirm it:** CDPK/SEND scores appearing in vendor marketing as
standard, or a major lab publishing pedagogical evals by default.

## 4. 🔴 MCP is the education integration layer — **except for the largest LMS**

**This trend is rewritten this pass. `p526` stated it without the exception, and
the exception is most of the market.**

MCP genuinely is the seam where it exists:
[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT, **308★**, v1.16.0
Oct 2026, ~102-128 tools) for Canvas, and
[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) (MIT, 538★) for
retention. Both are licence-clean seams into AGPL and desktop systems that must
not be forked.

> 🔴 **`p529` correction.** `p528` rewrote this trend as *"eleven codebases,
> nobody converged"*. The GitHub search API reports **222**. The conclusion
> *"no credible bridge"* **survives** — the ceiling is **52★ and ungranted**, and
> the permissive leader is 45★ and eight months stale — but *"eleven people
> tried"* becomes *"hundreds tried, one per campus"*. See **Trend 12**, which is
> what the real number turned out to mean.

🔴 **But Moodle — the sector's largest install base and plugin ecosystem — still
has no credible MCP server**, and ⚠️ **`p527`'s account of *why* was wrong.** It
read the field as *"roughly three real codebases."* `p528` probed **twelve
addresses first-hand** (existence first, then the licence title block) for a
census of **thirteen**, and found
**eleven independent codebases plus two forks**, in four languages, with tool
counts from **8 to ~230**, and **37 stars across every counter read**. Ceiling
unchanged at **27★**
([G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp), MIT, Rust, the only
one naming three live-tested Moodle versions). Full census in
[`../repos/foundations.md`](../repos/foundations.md).

🟢 **So the honest form of the trend, restated:** MCP is the *intended*
integration layer and the *actual* one only for Canvas and Anki — **not because
nobody built a Moodle bridge, but because eleven people each built their own.**
Ten of the eleven are **MIT**, so the blocker is neither licensing nor effort:
it is 🔴 **the absence of a shared tool vocabulary.** Eight tools in one server,
~230 in another, three of them contradicting their own READMEs on the count.
**Tool counts in this field are marketing, not measurement.**

🔵 **Why that reframes the opportunity.** "Nothing exists" argues for a
greenfield build. "Eleven permissive half-builds and no standard" argues for a
**consolidation plus a specification** — materially cheaper, and the
specification is the defensible part. See **P553**.

**What would disconfirm it:** a Moodle MCP server past ~500★, Moodle shipping an
official one, or 🆕 **two of the eleven converging on one tool vocabulary.** The
third is now the one to watch, and it is the cheapest of the three to cause.

## 5. Compliance timelines have become build windows — and now **differ by buyer type**

**Regulation (EU) 2026/1744** (Digital Omnibus, OJ 24 July 2026, in force 27 July
2026) moved Annex III high-risk education AI from 2 Aug 2026 to **2 Dec 2027**.
Not moved: **Article 50 transparency, live since 2 Aug 2026**, and the
**emotion-recognition ban in schools, live since Feb 2025**.

🆕 **Three dates added this pass, and one of them splits the market.** Two new
Article 5 prohibitions phase in **2 Dec 2026**; national regulatory sandboxes move
to **2 Aug 2027**; Annex I embedded systems to **2 Aug 2028**; and **high-risk
systems used by public authorities, including those already in service, to 2 Aug
2030**. State schools and public universities *are* public authorities across most
of the EU.

**So the EU is not one clock, it is two**, more than two and a half years apart,
and which one a client is on depends on whether they are public or private. Pitch
urgency accordingly — and verify the 2030 date against the regulation before
quoting it to a public client (see the gap note in
[`market.md`](market.md#declared-gaps-this-pass)).

**What would disconfirm it:** a further omnibus, or guidance collapsing the
public/private distinction.

## 6. The sector is copyleft, and that decides the architecture

Moodle GPL-3.0, Open edX and Canvas AGPL-3.0, i-educar and RosarioSIS GPL-2.0,
ILIAS GPL-3.0, H5P GPL-3.0. The permissive cores are
[Oppia](https://github.com/oppia/oppia) (Apache-2.0, 7.0k★),
[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, 449★),
[Sakai](https://github.com/sakaiproject/sakai) (ECL-2.0),
[Kolibri](https://github.com/learningequality/kolibri) (MIT) and
[Mentingo](https://github.com/Selleo/mentingo) (MIT, 101★) — and that is the
whole list. Searched again this pass; still no mainstream Apache/MIT LMS.

🆕 **And the last genuinely unresolved cell resolved the copyleft way.**
[frappe/education](https://github.com/frappe/education) (685★), red on `p526`, is
**GPL-3.0** — while Frappe LMS on the same stack is **AGPL-3.0**. One vendor, one
framework, **two different copyleft regimes**. The lesson generalises: grade the
licence per app, never per vendor.

**So:** build permissive agents that attach across a process or network boundary.
**Never fork an AGPL core.**

**What would disconfirm it:** a major LMS relicensing permissively, or a
permissive LMS reaching mainstream deployment.

## 7. Licences in this sector lie, and the lie is on the title line

Four confirmed traps, all read from the licence file's title block this pass:
[PageLM](https://github.com/CaviraOSS/PageLM) (2.1k★) opens with the MIT sentence
and is a bespoke non-commercial licence titled *"PageLM Community License"*;
[advisingapp](https://github.com/canyongbs/advisingapp) (340★) is **Elastic-2.0**;
[cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) (5.1k★) is
**CC-BY-NC-4.0** and only looks like BY-4.0 if a probe drops `NonCommercial`.

🆕 **And a fourth, found this pass, where the repository contradicts itself:**
[ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) (91★) — sidebar
`GPL-3.0`, **README badge `License: MIT`**, licence file title block `GNU GENERAL
PUBLIC LICENSE Version 3`. **The grant wins; a badge is a claim.**

**So the rule, now four-part:** grade from the **title block**; check
`LICENSE.md`/`LICENSE.txt`/`license.txt` as well as `LICENSE`; when badge and
sidebar disagree, **the licence file decides**; and never drop a `NonCommercial`
qualifier. Run it as a gate — see
[`../compose/patterns.md`](../compose/patterns.md).

**What would disconfirm it:** a pass finding no new trap. Seven consecutive
passes have found at least one.

## 8. 🆕 "No licence at all" is the failure mode nobody writes down

A separate category from the mislabelled, and this pass is the first to record it
on this base: repositories with real stars and **no licence file at any common
path**, on any common branch. Default copyright applies; the code cannot be used.

[A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant)
(**64★**, 6 agents, RAG Q&A) offers only a README sentence — *"open source and
available for educational purposes"* — which names no licence and grants nothing.
[idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow)
(25★) shows a **"License" entry in the sidebar that anchors into the README**, not
to a file — the most convincing version of the mistake.
[tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) was described in a
search result as *"MIT licensed"* and has no licence file at all.

**So:** an absent grant is a *harder* blocker than a bad one — there is no
counterparty to negotiate an exception with. And a search summary is not a
verification channel.

**What would disconfirm it:** these repositories adding licences; it would not
disconfirm the category.

## 9. 🆕 The packaging unit is becoming the *skill*, and the differentiator is provenance

The fast-growing tail is no longer applications but **agent skills**:
🆕 [lineage-skill](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0,
462★, 70 forks**) is the highest-starred new entry on
[`../agents/top.md`](../agents/top.md) this pass, and
`universal-examprep-skill` (361★), `universal-diagnostic-tutor-skill` (252★),
`kaogong-skill` (210★) and `education-skills` (119★) sit underneath it.
[Bloom](https://github.com/Li-Evan/Bloom) (294★) ships as a skill *and* a web app.

🟢 **The sharpening:** what distinguishes `lineage-skill` is not that it is a
skill but that its output is **source-backed** — a generated lesson traces to the
material it came from. That is the same property Trend 1 says buyers are short of,
Trend 3 says is measurable, and Trend 5 says India and China now *require* for
AI-generated content. **Provenance is where the governance gap, the evaluation
gap and the labelling rules converge**, and it is the cheapest thing to design in
and the most expensive to retrofit.

🆕 **`p528` adds the licence half of this trend, and it is the part that bites.**
The largest skills library in education is
[GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills)
— **926★, 130 forks, 165 skills across 20 domains, 157 MCP tools**, `v3.1.0` on
22 Oct 2026 — and it is **CC BY-SA 4.0**, a *content* licence. ShareAlike
propagates to adaptations, there is no patent grant, and the repository ships a
working server and 165 prose skills under one grant without drawing the
code/content line. 🔵 **As the packaging unit shifts from application to skill,
the licensing question shifts with it — from "can we fork this code" to "what
does this grant actually cover."** A content licence on an artefact that an agent
executes is a new question, and `MIT`-shaped intuitions answer it wrongly. See
the fourth verdict band on [`../agents/top.md`](../agents/top.md).

**What would disconfirm it:** skills plateauing while monolithic apps resume
growth, provenance staying absent from procurement questions, or the big skill
libraries relicensing to Apache-2.0 — which would retire the licensing half
without touching the packaging half.

## 10. The buyer is shifting from the learner to the teacher

The 2026 Holon IQ LATAM EdTech 100 shows AI positioning moving **toward
teachers**, with upskilling losing ground; **Teachy** (Brazil, AI lesson
preparation) is the regional incumbent. Gallup + Walton put weekly teacher AI
users at **5.9 hours/week saved** — a measurable, CFO-legible ROI number that no
learner-facing claim matches.

🟢 **This pass adds the supply side.**
🆕 [Claw-ED](https://github.com/SirhanMacx/Claw-ED) (MIT, 63★) and `lineage-skill`
(462★) are both **teacher-facing authoring tools**, and both are local-first with
teacher review in the loop. The tooling is now arriving where the money is.

**What would disconfirm it:** learner-facing subscription products reclaiming
funding share, or teacher tools failing to convert at district level.

## 11. 🆕 Integrity is the half that gets cut — and the evidence is a merge commit

The clearest signal this pass is a **deletion**, which is a stronger form of
evidence than a launch because nobody ships a deletion for attention.

🔴 [`AIEd-Innovations/assessment_agent`](https://github.com/AIEd-Innovations/assessment_agent)
(**Apache-2.0**) was the one open agent doing grading **and** integrity in one
pipeline. **PR #19 — *"Remove the integrity check: the agent only grades"* —
merged to `main` on 27 Oct 2026.** It removed the anomaly-detection LLM call, the
anomaly report log, the `GET /anomalies` endpoint and the `anomaly_report` result
field. An integrity risk **no longer routes a submission to review.** The stated
reason is cost: **one LLM call per submission instead of two.**

🔵 **Read it as unit economics, not as one team's preference.** Integrity was the
second inference call, it doubled the per-submission cost, and it was the half
that went. That is the same pressure every grading deployment is under, and it
predicts where the open tooling will keep thinning out.

🟡 **Meanwhile the permissive supply exists and nobody uses it.** Two MIT
candidates were verified this pass and **both sit at 0★ / 0 forks**:
[gradeops](https://github.com/sonowalvaibhav/gradeops) (VLM grading of handwritten
answers, JSON rubrics, TA override, plus plagiarism detection that looks for
*shared anomalous logic and identical erroneous reasoning* — the right primitive,
because matched *errors* are far harder to explain away than matched text) and
[Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent)
(**zero external APIs, fully on-device**, from-scratch logistic regression
producing an **evidence breakdown for human review rather than a verdict**).

🟢 **Why the posture of that second one matters commercially:** from 2 Dec 2027 an
EU deployer running AI over grading or proctoring is in the high-risk band, where
"explainable evidence for a human decision-maker" is the compliant shape and "a
cheating verdict" is not. **The 0★ repo has the right architecture and no
adoption; the funded deployments have adoption and just deleted the feature.**

⚠️ **Both are single-author projects with self-reported metrics**, and the
proctoring one contradicts itself on its own test count (94 vs 344). Signals, not
dependencies.

**What would disconfirm it:** an integrity capability landing *back* in a
maintained open grading agent, or one of these two passing ~100★ with external
contributors.

## 12. 🆕 The unit of LMS integration is the **institution**, not the product

**Stated so it can be wrong:** *if this trend is right, the Moodle-bridge field
should show many single-institution codebases and no scaled product; if it is
wrong, we should see two or three bridges with most of the stars and real
deployment counts.*

🟢 **The evidence says institution.** Of the 26 highest-starred addresses in a
222-address field, **14 exist to bridge one named university's Moodle** —
Universidade de São Paulo, FICH-UNL, UTN, UTN FRLP, Universidad de San Andrés,
Vietnamese-German University, SLIIT, Nottingham Ningbo, Taylor's, UNSW, SPbPU,
RTU MIREA (×2), TU Wien. Almost all are read-only, almost all are student-built,
almost all are under 10★. **No product has consolidated them**, and the field's
most-starred artefact carries **no licence at all**.

🔵 **Why this is the most commercially useful line on this base.** It says the
opportunity is **not** a better Moodle bridge. Hundreds of people can already
write one in a weekend; what none of them can do is make it safe, auditable and
maintainable for an institution that will be asked about FERPA, the EU AI Act or
a ministry's data rules. **The deliverable is a generator plus a governance
model** — tool vocabulary, read-only default, write-gating, token custody,
audit log — not another bridge. See `P558`.

🔴 **The regional distribution is part of the trend, not a footnote.** LATAM
ships **5**, APAC **5**, EMEA **4**, **North America 0**. NA has the largest
AI-education market and builds none of these, which is the signature of a region
that **buys** institutional integration. That is where a productised bridge finds
a buyer rather than a hundred hobbyist competitors.

## 13. 🆕 A measurement channel is a finding, and this base just changed one

**Stated so it can be wrong:** *if this trend is right, re-measuring old records
with a new instrument should change conclusions, not just confirm them.*

🟢 **It did, in both directions, on the same day.** The GitHub search API became
reachable this pass after months of `github-api-proxy-blocked`. It **confirmed**
all fourteen shelf rows, grant and counter — the hand-probe method had been this
base's only instrument, hence unfalsifiable, and it passed. It then **destroyed**
`p528`'s Moodle headline, raised **two** new shelf rows, and showed that **25 of
80 census addresses were already in this base's history** with only 9 ever filed.

🔴 **And it produced two new failure modes within one pass**, which is the part
worth generalising:

1. **`NOASSERTION` is uninformative.** It resolved to a permissive grant, a
   copyleft grant, a non-OSI grant *and* no grant at all. Reading it as
   "ungranted" would have thrown away `thm-mni-ii/feedbacksystem`, which is
   **Apache-2.0**.
2. **Absence from an API search is not non-existence.** A real repository
   (`packbackbooks/lti-1-3-php-library`) did not come back from a call that
   returned six others.

🔵 **The trend, not the anecdote:** every new channel arrives with its own
credulity. This base already had a rule about trusting search summaries; it
needed the *same* rule for a structured API, and did not have it until the API
nearly produced a phantom. **A faster instrument does not reduce the need for a
second one — it raises it**, because speed is what makes skipping the check
tempting.

## 14. 🆕 The new entrants are choosing network copyleft, so the sector's copyleft is a *present-tense* decision

**The claim.** This base has carried *"education is copyleft"* since `p526` as a
statement about **legacy** platforms — Moodle GPL-3.0, Open edX AGPL-3.0, Canvas
AGPL-3.0. `p530` measured the **new** cohort, the AI-native LMS entrants, and the
pattern is not inherited. It is being chosen now:

| Address | Grant | Stars |
|---|---|---|
| [frappe/lms](https://github.com/frappe/lms) | 🔴 AGPL-3.0 | 3 353 |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 AGPL-3.0 | 2 430 |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 AGPL-3.0 | 1 290 |
| [artcc/freelingo](https://github.com/artcc/freelingo) | 🔴 AGPL-3.0 | 213 |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 101 |

🔴 **Every AI-native LMS with traction is AGPL-3.0; the single permissive entrant
is the smallest by an order of magnitude.** AGPL is the open-core commercial
posture — it permits the project while making a hosted competitor
license-impossible — and it is what a 2026 founder picks.

**Why it matters more than the legacy reading.** A legacy copyleft core can be
worked around by sitting beside it. **A copyleft core that is also the AI layer
cannot** — the thing you want to extend is the thing the licence protects. So the
permissive surface of this sector is shrinking in exactly the layer where AI
value accrues.

🔵 **How this is disconfirmed.** If a permissive AI-native LMS passes ~1 000★
within two quarters, or if one of the four relicenses, the trend inverts. Watch
`Selleo/mentingo` as the single clean indicator.

## 15. 🆕 In this sector, retrieval is a harder problem than discovery — and that is a claim about *buyers*, not just this base

**The claim.** `Gap 529-A` is usually read as housekeeping. `p530`'s measurement
says it is the sector's shape: **3 098 addresses in this base, 79 filed, 97
permissive repos described five or more times and never used.** The supply of
open-source education software is not scarce. **What is scarce is the ability to
find the right piece at the moment of need.**

**The evidence that this generalises past this base.** Asked for an open-source
grader this pass, generic web search answered *"I found no open-source agent that
grades students."* There are **three permissive autograders totalling 2 337★**
([nbgrader](https://github.com/jupyter/nbgrader),
[Submitty](https://github.com/Submitty/Submitty),
[otter-grader](https://github.com/ucbds-infra/otter-grader)), two of them from
named universities, all of them a decade old. 🔴 **The market's own
discovery channel reported a mature capability as absent.** An institution
running that same search reaches the same wrong conclusion and buys a vendor
product.

**Why it matters commercially.** It reframes what a studio sells. If supply were
scarce, the asset would be building the missing component. Supply is not scarce,
so **the asset is the curated, licence-verified, regionally-placed index** — and
the evidence that it is an asset is that this base, which exists to be exactly
that, failed at it for 400 passes until it built an index of its own contents.

🔵 **How this is disconfirmed.** If a later pass's promotion queue comes back
near-empty after the ledger runs in front of every pass, then the debt was a
one-off backlog rather than a structural property. **The queue size at `p540` is
the test.**

## Counter-signals worth holding

- **ANZ leans toward banning AI in schools** (Ipsos Education Monitor 2026) while
  the rest of APAC leans against a ban. Capability-led pitches fail there.
- **Trust in the sector is damaged, not neutral.** China shut its ~$100B private
  tutoring industry in 2021; India's BYJU'S collapsed into insolvency. APAC AI
  tutoring is rebuilding from a low base of trust, not a high one.
- **Market-size estimates diverged rather than converged** this pass: the 2026
  band is now **USD 6.4B-12.3B**. Quote the 30-35% CAGR, not a point estimate.
- 🆕 **Policy is not deployment.** UNESCO's APAC analysis is blunt that adoption
  needs **infrastructure, connectivity and teacher training**, and that much of
  the region has unmet basic educational needs first. CENIA says **13 of 19 LAC
  countries** have not begun. A regulatory calendar is not a readiness signal.
- 🆕 **Stars are not maturity, in either direction.** `pedagogy-benchmark` is the
  most procurement-useful repository on this base at **13★**; `ralph`, the xAPI
  seam the whole analytics argument rests on, has **51★**. Meanwhile 64★ bought
  no licence at all. Read the repo.

## Source-quality note

Trends 4, 5, 6, 7 and 8 rest on **primary artefacts** — licence files and
repository pages read first-hand this pass, plus a named EU regulation. Trends 1,
3 and 10 rest on **named studies** (UNESCO IESALC + UNU-IAS, RAND, Gallup +
Walton, Digital Education Council, Holon IQ, Ipsos, OECD). Trend 2 and 9 rest on
**repository evidence**, with star counts as rounded page values because
`api.github.com` is unreachable from this session.

Weakest links, named: **market sizing** (vendor and blog aggregation, widening
band), **EMEA vendor funding detail** (trade aggregators that disagree with each
other), the **EU public-authority 2 Aug 2030 date** (single commentary source),
the **OECD Outlook recommendation** (reported, not read from the Outlook itself),
and **APAC curriculum status** (sources mutually contradictory).
