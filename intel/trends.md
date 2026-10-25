---
industry: education
region: Global
updated: 2026-10-25
---

# 📈 Trends — Education AI

> Current trends, re-measured each pass. Trends 1–8 are the standing set; 9–11 were added
> or amended on 2026-10-25 from first-hand measurement.

## 🆕 Trend 30 — `p433` In North America the **district**, not the state, is now the layer that decides whether a build is legal

Every regulatory read on these shelves has been organised by **state**: 134 bills across 31
states, California AB 1159, Oklahoma and Maryland on human oversight, Ohio HB 96 and Tennessee
SB 1711 on policy mandates, Alabama HB 329 on graduation. That framing is now **the wrong unit for
a build decision**, and this pass can say why with three cases rather than one.

**What the states actually did.** Read the mandates together and a pattern appears: the states
that legislated mostly legislated *procedure*. Ohio and Tennessee require districts **to write
their own AI policies** — Ohio's deadline was **1 July 2026** and has passed. 35+ states publish
**guidance**. Oklahoma and Maryland set a *standard* ("not the sole basis") rather than a
prohibition. **A state telling every district to write a policy is a state declining to write
one.** The binding text ends up one level down, and by statutory design.

**What the districts did with that delegation.** They prohibited things, specifically and
unevenly:

| District | Instrument | What it bars |
|---|---|---|
| **New York City** | 2026-27 guidance, enacted **2026-09-02** | Student-facing generative AI, **grades 2K-8** (~600,000 students); **companion chatbots in every grade**, high school included. Preliminary (March 2026) red tier was reported to bar grading, discipline, counselling, placement **and special-education / 504 plan development** (🟡 survival into the enacted text unresolved — `Gap 433-B`) |
| **Charleston County** | district policy | Discipline, placement, **special-education determination** |
| **Katy ISD** | district policy | Generative chatbots K-6, scaffolded access to grade 12 |

🔴 **The three do not agree with each other, and none of them is a state rule.** NYC draws its
line at **grade 8** and adds an all-grades companion-chatbot ban; Katy ISD draws it at **grade 6**;
Charleston County draws it by **decision type** rather than by grade. A vendor compliant in Texas
is non-compliant in New York on the same product.

**Why this is a trend and not a list.** The delegation is *structural*: Ohio and Tennessee
**require** per-district policy, so the number of binding, mutually inconsistent AI rules in US
K-12 grows with the number of districts — roughly **13,000** of them — not with the number of
states. State-level tracking, which is what every tracker and every vendor summary does, is
measuring the layer that chose not to decide.

**What it changes in a build, concretely:**

1. **Student-facing vs teacher-facing stops being a product decision and becomes a
   configuration axis.** `Trend` guidance on this file already said *"student-facing optional
   should be an architectural switch from day one"*. NYC makes it unavoidable: the same deployment
   must run teacher-facing-only in grades 2K-8 and limited-student-facing in high school, **in one
   district**. A product that cannot be switched per grade band cannot be sold to NYC at all.
2. **Grade band becomes a first-class policy input**, alongside jurisdiction. Not a setting in an
   admin screen — a constraint the agent layer enforces and logs.
3. **Companion-chatbot shape is separately regulated from AI generally.** NYC bars companion
   chatbots in **every** grade while permitting teacher-facing AI. A persistent-persona tutor and a
   task-scoped assistant are now **different regulatory objects** even though they are the same
   technology, which is an argument for building the task-scoped one.
4. **Due diligence moves from statute to district policy.** `Pattern AL` now carries this as a
   go/no-go in week 1 rather than a formality.

🔵 **The honest limit on this trend.** All three district instruments are read from secondary
reporting; `Gap 433-C` records that no government primary is reachable from this host, so **none
of the three was read in its official text**. The *structure* of the argument — states delegating
by statute, districts prohibiting unevenly — rests on the Ohio and Tennessee mandates, which are
themselves corroborated across independent trackers. 🔴 Three districts is also not a census: this
is a pattern with three data points and a stated mechanism, not a measured rate across 13,000
districts. **What would strengthen it:** a sweep of the twenty largest US districts' AI policies.
No instrument on this base does that, and this pass did not build one.

## 🆕 Trend 28 — `p432` Regulatory intensity and open-source supply are **inversely** correlated in education, and special education is the proof

Every other trend on this file reads the market from the demand side. This one reads it from the
supply side and finds the opposite of what a market should do.

Rank education's surfaces by how hard the law constrains them, and special education is first in
North America by a wide margin: IDEA and §504 make the individualised education program a
**statutory instrument** with mandated timelines, mandated team composition and a mandated human
decision. Oklahoma and Maryland bar AI as the sole basis for a high-stakes student decision;
Charleston County names special-education determination explicitly. There is no surface in this
industry where "an agent drafts, a human signs" is more clearly *required* rather than merely
advisable.

Now rank the same surfaces by open-source supply. Measured this pass:

| surface | established open-source bases | ceiling |
|---|---|---|
| tutoring | DeepTutor, OATutor, OpenTutor, Bloom, Study-Mate, tutor-gpt, … | **42 610 ★** |
| LMS / platform | Moodle, Open edX, Canvas, Sakai, OpenOLAT, Kolibri, Chamilo, … | institutional scale |
| LMS agents (MCP) | ~40 addresses across Canvas, Moodle, Classroom, Blackboard, D2L | hundreds of ★ |
| evaluation (`p431`) | tutorbench, tutor_gym, MathTutorBench | low hundreds |
| **special education / IEP** | **none** | **1 ★** |

584 addresses match the category and the top 30 by recency are all ≤ 5 ★. Three MIT tools exist;
they were created on 2026-10-14, 2026-10-23 and (the parent corpus) maintained to 2026-10-24.

**Why the inversion happens, and it is not mysterious.** Open source in education is built by the
people who can ship it — researchers, platform engineers, teachers automating their own marking.
A statutory workflow cannot be shipped by any of them alone: it needs district authorisation, a
system of record, a privacy review and professional liability. So the hardest-regulated surface is
the one hobbyist supply cannot reach, and the commercial market (PowerSchool Special Programs,
Frontline, SEIS) owns it uncontested.

**What it means commercially — and this is the actionable half.** The inverse correlation is a map
of where a services studio is *structurally* advantaged. Globant can supply exactly the things the
open-source channel cannot: the district relationship, the authorisation path, the audit trail and
the liability posture. On tutoring, Globant competes with a 42 k-star project; on IEP workflow,
there is no incumbent open base at all, and the three MIT seeds that exist are fork-and-own by
construction.

🔴 **The honest counterweight, stated so no deck overstates this.** No incumbent also means no
validation: no benchmark, no reference deployment, no second contributor on any of the three
addresses, and no evaluation harness that scores IEP goal quality (`p431`'s evaluation tier does
not reach this category). A first engagement here is a build, not an integration, and it must be
priced and sold as one.

🔵 **Prediction this base can be held to:** if the inversion is structural rather than a sampling
artefact, the special-education tier will still have no address above ~50 ★ in six months, while
tutoring adds another order of magnitude. Re-measure and record either way.

---

## 🆕 Trend 29 — `p432` GitHub's `license` field is a detector, not a verdict — and it failed in **both** directions in one eleven-repo sample

This base already carries three licence-trap trends: `Trend 6` (the permissive frontier runs
across the stack), `Trend 9` (a permissive licence has a shelf life) and `Trend 27` (a grant with
no title, a title with no grant). `Trend 29` is narrower and more mechanical, and it invalidates a
shortcut that is tempting precisely because it is cheap.

Two of eleven addresses measured this pass returned `license: NOASSERTION` ("Other") from the
GitHub API. **Neither was unlicensed.** Reading the payload at the pinned SHA resolved them to two
real licences at opposite ends of the commercial spectrum:

| Address | API said | Payload says, at HEAD | Commercial consequence |
|---|---|---|---|
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | `NOASSERTION` | **AGPL-3.0-or-later** · `LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f` | 🔴 Strong network copyleft. Cannot be vendored into a client deliverable. |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `NOASSERTION` | **CC BY-SA 4.0** · `LICENSE` 1 229 B · `40db9b472090` @ `135d6275e7db` | 🟡 Commercial use **and** adaptation expressly permitted — with a ShareAlike obligation on derivatives. |

**Why the detector abstained, in both cases for a formatting reason rather than a legal one.**
AlloFlow's grant sits behind a project title line and an SPDX header (`AGPL-3.0-or-later`) instead
of the stock licence title; the skills repo ships a short CC BY-SA notice-and-summary rather than
the full legal code. Both are perfectly valid grants. Neither matches the templates
`licensee` scores against.

**The three failure modes this produces, all of which cost money:**
1. **`NOASSERTION` read as "no licence"** → a usable base (CC BY-SA, commercially permitted) is
   discarded. A cost of omission, invisible in any audit.
2. **`NOASSERTION` read as "probably fine, it's on GitHub"** → AGPL-3.0 enters a hosted
   deliverable. This is the expensive one.
3. **A roundup's unsourced claim substituted for the file** → one article we read asserted
   "CC BY-SA 4.0" without citing the payload and happened to be right. The same article would have
   read identically if it were wrong.

**The rule, and it costs seconds.** `NOASSERTION` is not a value — it is a *flag to read the file*.
`git ls-remote` for the SHA, fetch the payload at that SHA, size + `sha256` it, read the first
twenty lines. And "no licence" is only ever established by `git ls-tree -r` over the whole tree:
that is how `grasped-dev/staircase` (0 of 33 files) and
`eakarsu/ai-special-education-iep-compliance` (0 of 29 files) were confirmed ungranted this pass,
rather than by a missing-file guess at one candidate path.

🔵 **New obligation family on these shelves.** CC BY-SA 4.0 is the first *content* ShareAlike grant
to land on a build-relevant row. `Trend 11` recorded data licences (ODbL on `os-taxonomy`);
ShareAlike-on-prompts is a third category again, and it bites a studio hardest where the
deliverable *is* text: a skill pack, a prompt library, a curriculum corpus. A pack derived from
those 165 skills must ship under CC BY-SA 4.0 — publishable, not proprietary. Decide that before
the statement of work, not after.

---

## 🆕 Trend 26 — `p431` The evaluation layer arrived, and it is permissive — which moves the sellable unit from *adoption* to *evidence*

For many passes this file carried `Trend 8` as a standing, unclosed **measurement gap**: this base
could supply tutoring agents but could not name the instrument that scores them. Measured
first-hand on 2026-10-25, **that gap closes on the tutoring side**:

| Harness | Grant | Maintained | What it scores |
|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 (code) | 🟢 commit 2026-10-25 | Scenario-based pedagogical failure + **regression** after a fix |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | 🔴 silent since 2025-09-10 | A model as **tutor** and as **simulated student**, inside real ITSs |

**Why this is a trend and not an inventory note.** `Trend 1` says adoption is finished and
governance is the market; `Trend 2` says procurement is being rewired around **evidence**. Both have
pointed at a deliverable this base could not actually build, because *“our tutor is pedagogically
sound”* was an assertion with no instrument behind it. With an MIT harness that binds to
`CAHLR/OATutor` — already on this base's verified shelf — and `pykt-toolkit` (MIT) underneath for
knowledge tracing, **tutor → measurement → evaluation is MIT end to end.**

🟢 **What that changes commercially.** The sellable unit stops being the tutor and becomes the
**evidence pack**: a scored baseline, a regression suite, and a re-test after each change. That is
the artefact HolonIQ's “evidence of improved learning” expectation, the EU's Article 50 transparency
duty, and a US district's procurement review each separately ask for — **one deliverable, three
jurisdictions**, which is `Trend 3`'s divergence problem answered rather than absorbed.

🔴 **The half that did not arrive, and it is the regulated half.** Everything measured scores
**tutoring**. **Nothing open scores grading.** The one grading-side candidate
([`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader)) is non-commercial by clause 2 of its
licence. Meanwhile NA (Oklahoma, Maryland: no high-stakes AI decisions without human oversight),
EMEA (Annex III: assessment is high-risk) and APAC (Vietnam: automated assessment on the high-risk
list) all regulate **assessment** hardest. **The most exposed surface is the one with no harness.**
Tracked as `Gap 431-C`; it is now the most valuable open gap in this base.

## 🆕 Trend 27 — `p431` The licence trap inverted: a grant with no title, and a title with no grant, in the same eleven-repo sample

`Trend 25` says a string matched as though it were a meaning is this base's most productive error
class. This pass produced **both directions of that error at once**, which is worth separating out
because the two need *different* instruments:

| Direction | Address | What a naive read returns | What the payload says |
|---|---|---|---|
| **Grant without title** | `Teachable-AI-Lab/tutor_gym` | `UNKNOWN` — the payload never contains the string `MIT License`; it opens at `Copyright 2025 …` | 🟢 **Verbatim MIT**, fully permissive |
| **Title without grant** | `sdrangan/llmgrader` | `MIT` — the file is named `LICENSE` and its first grant sentence is the MIT one, word for word | 🔴 **“PySilicon Research License”** — clause 2 forbids commercial use |

🔵 **The practical consequence: no single cheap check is sound.** A title sweep false-negatives the
first row and false-positives the second. A byte-size heuristic fails too — `llmgrader` is 1 224 B
against the stock MIT ~1 069 B, a 155 B difference that looks like a longer copyright line. A
`sha256` sweep catches the second only *after* someone has read it once and recorded the digest.

**The only instrument that is correct on both is reading the operative clauses.** For a studio this
is a cost line, not a philosophy: **budget one human licence read per address you intend to ship**,
and let the digest sweep do what it is actually good at — detecting *change* at a known address
between passes, which is how `p429` caught the `pengusto` relicensing within 24 hours.

🟡 **A third variant, same family:** `eth-lre/MathTutorBench` has **no licence file at all**, and a
README that cites CC-BY-4.0 in a badge and CC-BY-**SA**-4.0 in its licence section. Here even
reading does not settle it — the repository contradicts itself, so the honest record is
*ungranted*, not *probably CC*.

## 🆕 `p430` · 2026-10-25 — **Three trends added from first-hand measurement: a permissive licence has a SHELF LIFE (`Trend 9`), education's permissive supply is in the agent layer and not the platform layer (`Trend 10`), and DATA licences have arrived in education (`Trend 11`).**

## 🆕 Trend 9 — A permissive licence has a shelf life, and nothing in this industry measures it

The sharpest finding of 2026-10-25, and it generalises well beyond education.
`pengusto/google-classroom-mcp` was read as **MIT** by three separate passes
(2026-10-03, 2026-10-20, 2026-10-21). Every one of those readings was **correct when
taken**. On 2026-10-23 the maintainer relicensed to a proprietary **"Pengusto Commercial
License 1.0"**, effective 2026-10-24, whose §3 requires a paid agreement from
*"an educational institution or training provider, whether nonprofit or commercial"* — by
name, the exact buyer in this industry.

🔴 **The failure mode is not a wrong reading; it is a stale one.** A dependency inventory
that records `licence: MIT` with no re-read date will keep asserting MIT indefinitely.
Badges, package manifests and MCP directories all lagged the change.

🟢 **The practice that follows, and it is cheap:** read the licence payload at the commit
SHA you are actually consuming, record the SHA and a digest alongside the family, and
re-read before any engagement commits. On this pass the whole 24-repo sweep cost minutes.
Digest equality is also a *discovery* instrument: the abandoned MIT bytes
(1 145 B, `a01639b20880`) were found alive at `vTanco/google-classroom-mcp`, so the lane
was recovered rather than written off.

## 🆕 Trend 10 — Education's permissive supply is in the agent layer, and the platform layer is closed to it

Re-measured in full on 2026-10-25 across ten platforms and fourteen agents.

- **Platform tier:** 7 of 10 are copyleft — Moodle (GPL-3.0), Open edX (AGPL-3.0),
  Chamilo (GPL-3.0), eXeLearning (AGPL-3.0), Frappe LMS (AGPL-3.0), BigBlueButton
  (LGPL-3.0), OpenEduCat (LGPL-3.0). Only **OpenOLAT** (Apache-2.0), **Kolibri** (MIT) and
  **Sakai** (ECL-2.0) are permissive.
- **Agent / MCP tier:** **14 of 14** verified rows are MIT, Apache-2.0 or BSD-3.

🟢 **This is a structural fact an engagement can be designed around**, not a complaint: put
the AI in the agent layer, talk to the platform over its API or component SDK
(`openedx/XBlock`, Apache-2.0, is the supported seam), and no copyleft obligation reaches
the client's IP. Building AI *into* the platform inherits its licence.

## 🆕 Trend 11 — Data licences are arriving in education, and they bite differently

`withmarbleapp/os-taxonomy` — the one genuinely new trending in-domain address this pass,
a 1 590-topic curriculum graph mapped to NGSS and Common Core — is **ODbL**, not a code
licence. Share-alike attaches to *derived databases*. A client's curriculum graph built on
it inherits the obligation.

🟡 As curriculum knowledge graphs become the substrate for adaptive learning, **licence
review in education has to cover data, not just code**. A code-only audit passes this repo
and misses the only obligation it carries.

---

## Trend 1 — Adoption is finished. Governance is the market.

**88–95% of students and faculty already use AI; 26–54% can name a governing policy.**
That gap, not the adoption curve, is what 2026–27 budget buys.

- Coursera (n=4,200, 5 countries): **95%** using AI academically, **26%** of educators report a
  formal institutional policy.
- EDUCAUSE 2026: only **54%** are aware of *any* policy or guideline.
- Ellucian (n=779): institutional adoption **49% → 66%** year on year, with **data privacy the top
  barrier**.
- Digital Education Council (n=45,398, 35 countries): **88%** of students, **77%** of faculty.

- 🆕 `p384` **UNESCO IESALC** (n=**200 institutions, 19 countries**, Sept 2026): **87%** of LAC
  higher-ed institutions use AI in at least one area — **74%** in teaching and learning, **57%** in
  research — against **26%** with a formal AI strategy. 🟢 **An independent, institutional source
  landing on the same 26%** as Coursera's educator-reported figure, in a different region with a
  different method. The governance gap is no longer an inference from one survey; it replicates.
- 🆕 **OECD TALIS 2024** puts teacher AI use at **~50%+** in Brazil, Chile, Colombia and Costa Rica
  against an **OECD average of 36%**; Uruguay's **Ceibal** reports **75%** of public-school
  teachers. 🔵 Practitioner uptake is running ahead of the OECD mean in LATAM — the governance gap
  is widest exactly where adoption is fastest, which is the opposite of the usual assumption.

**So:** stop selling introduction. Sell policy-to-configuration, audit trails and a governed
gateway. The shadow-AI estate already exists on every campus. 🟢 And sell it **hardest in LATAM**,
not last — the 87%/26% split there is the widest measured in this file.

## Trend 2 — The ROI reckoning arrived, and procurement is being rewired around evidence

- **~80%** of institutions are investing in AI; **29%** of CTOs say it met or exceeded ROI
  expectations (Inside Higher Ed / Hanover).
- **~7 in 10 provosts** use AI weekly themselves; **1 in 10** report a centralised institutional
  strategy. Personal adoption has outrun institutional capability.
- The **US Department of Education's "Dear Colleague" letter** tells states to evaluate ed-tech by
  **measurable learning outcomes rather than screen time**, and to put **evidence requirements into
  procurement**.
- **US/Canada faculty intent to keep using AI fell 76% → 67%** in one year.

**So:** a before/after measurement on the client's own subject mix is becoming a procurement
precondition, not a nice-to-have. [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness),
MMLU and GSM8K are all MIT; there is no licence reason not to ship this with every engagement.

## Trend 3 — Regulatory divergence hardened in 2026. One global configuration is no longer viable.

Four regimes moved in four different directions in a single year:

| region | 2026 direction |
|---|---|
| **EU** | **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) pushed high-risk education systems from 2 Aug 2026 to **2 Dec 2027** — while **Art. 50 transparency still starts 2 Aug 2026** and **Art. 4 AI literacy has bound every school since 2 Feb 2025**. Emotion recognition in education: prohibited. 🆕 `p385` **The nearest date is neither of those: machine-readable marking of AI-generated content on systems ALREADY on the market is due 2 Dec 2026.** Annex I (AI embedded in regulated products) moves to **2 Aug 2028**. |
| **US** | No federal rule; **134+ bills across 31 states**, **33–35 states** with guidance, and binding district-policy mandates (Idaho SB 1227 effective 1 Jul 2026; Oklahoma SB 1734 by 2027-28). |
| **India / China** | **Content labelling and provenance**: India's amended IT Rules from **20 Feb 2026**; China's labelling measures from **1 Sep 2025** (988 services filed by 30 Jun 2026). |
| **Vietnam / Brazil / Mexico** | **Sectoral high-risk designation**: Vietnam names education among six high-risk sectors; Brazil's PL 2.338/2023 reportedly covers student selection; Mexico replicates the EU risk model. |

**So:** regional configuration is now a product requirement. The same tutor needs provenance
watermarking for India, a transparency notice for the EU, a prohibited-uses lockout for DC, and a
teacher-facing-only mode for ANZ and Brazil.

🆕 `p385` **Two corrections to how this trend gets sold.** First, **the EU deferral is widely
misread as breathing room.** It defers the *high-risk* regime; it defers nothing for a system already
deployed, which owes machine-readable marking on **2 Dec 2026**. A client told "the EU moved to 2027"
and nothing else has been misinformed about the only date within the current budget year. Second,
**employment-adjacent AI is separating from student-facing AI as its own regulated surface**:
**Illinois SB 2909** restricts AI in *teacher* evaluation from **1 Jan 2027**, where DC had only a
non-mandatory ban. A product that evaluates staff is a different compliance object from one that
teaches learners, and the two are still being scoped as one in most pitches.

## Trend 4 — Restriction is a real countertrend, not noise

For two years the only direction was adoption. In 2026 the brake appeared:

- **District of Columbia** 2026-27 policy bans AI from **grading, discipline, IEP decisions and
  teacher evaluations** — four of the highest-value automation targets.
- **Ipsos Education Monitor 2026:** **Australia and New Zealand show the highest support for
  banning AI in schools**, while Asian markets show the lowest. One company, two opposite mandates.
- **European Schools:** **no** generative AI tool approved for system-wide use.
- 🟢 **CONFIRMED at `p433`** (held 🔴 `UNCONFIRMED` from `p386`): the **New York City moratorium**
  on student-facing generative AI was **enacted 2026-09-02** for the 2026-27 school year, grades
  **2K-8**, ~600,000 students, with **companion chatbots barred in every grade**. **It holds — the
  largest US district has gone the other way**, which is no longer a conditional.

**So:** "student-facing optional" should be an architectural switch from day one, not a retrofit.
A product that cannot run teacher-facing-only is unsellable in a growing share of the market.

## Trend 5 — Teacher-facing is beating student-facing where growth is fastest

HolonIQ's **2026 LATAM EdTech 100** finds regional AI positioning concentrated in **teacher-facing
instructional tools rather than consumer tutoring** — Teachy (Brazil) in lesson preparation, Ginia
(Mexico) in employability. The regulation points the same way: Brazil's draft law targets
**student selection**, DC bans AI in grading and discipline, ANZ sentiment is restrictive.

**So:** the market and the regulator agree for once. Lesson preparation, assessment drafting,
feedback generation and administrative load carry the growth and avoid the hot zone.

## Trend 6 — The permissive-licence frontier runs *across* the stack, not along it

Measured first-hand this pass over 58 live repositories:

- **Platform tier is copyleft**: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, Chamilo
  GPL-3.0, ILIAS GPL-3.0, Tutor AGPL-3.0, Frappe LMS AGPL-3.0, Sakai ECL-2.0, Opencast ECL-2.0,
  OpenEduCat LGPL-3.0, H5P GPL-3.0.
- **Exactly one permissive major LMS**: **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT),
  Apache-2.0** — and no roundup we read mentions it.
- **Agent tier is permissive almost throughout**: MIT / Apache-2.0 / BSD-3.

**So:** the architecture follows from the licences. Compose permissive agents **over** a copyleft
platform across **LTI 1.3**, **MCP** or web services — never fork the platform. The interop boundary
is a legal artefact as much as a technical one.

## Trend 7 — MCP reached the LMS, and that is genuinely new

As of 2026 the LMS is addressable by agents without a fork:

- **Moodle's own plugin directory** carries **`webservice_mcp`**, exposing Moodle's external
  functions as **MCP tools over JSON-RPC 2.0** — **Moodle 4.5–5.2**, latest release
  **23 Jul 2026**, gated on the `webservice/mcp:use` capability.
- **Canvas** is served by community MIT servers ([r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp),
  fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp)).
- 🔴 **No official server from Instructure or Moodle HQ**, and two of the most-advertised community
  Canvas/Moodle servers are **unlicensed** — see [`agents/top.md`](../agents/top.md).
- 🆕 `p387` **27 distinct education MCP server slugs are shelved** on
  [`agents/top.md`](../agents/top.md) — re-derived by this base's own `recount` instrument, which
  was runnable this pass for the first time in several (the figure stood at **12** here while the
  shelf had grown to 27). Across both agent shelves **MCP reaches **6 distinct LMS platforms**** —
  Canvas, Moodle, Google Classroom, Blackboard, Brightspace/D2L and Open edX. The cumulative
  harvest behind that is lopsided: **35 Canvas servers and 20 Moodle**, against **2 for Open edX**.
- 🔴 🆕 `p387` **A correction this shelf owed since `p386`, and did not carry.** The bullet above
  used to end *"Blackboard has 9 with not one verified grant and D2L has 6 with the only one
  checked ungranted"* — and concluded that a permissive server on either platform *"would be a real
  contribution."* `p386` probed all fifteen addresses and found **6 MIT grants on Blackboard and 6
  on D2L**; it corrected [`agents/top.md`](../agents/top.md) and **left this sentence standing**.
  🔵 The live claim is: on Canvas and Moodle the work is *selection*; on Blackboard and D2L the
  grants exist and the missing thing is **tenancy** — every granted server there authenticates as
  the signed-in student (see `compose/patterns.md` **Pattern N**, and `Gap 387-A`).

**So:** the integration cost of an LMS-aware agent dropped by an order of magnitude this year, and
the remaining risk moved from engineering to licensing.

## Trend 8 — Measurement gap in this pass, stated rather than papered over

**No popularity metric is published this pass.** Every star channel was closed in this sandbox:
`api.github.com` 403, `github.com` HTML 403, `img.shields.io` blocked, `api.star-history.com`
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated across several industries**; carrying unverifiable numbers forward would
repeat that error. Licence, default ref and liveness **were** verified first-hand for all 58 live
addresses — see [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

**So:** rank by licence permissiveness, maintenance signal and fit. Popularity was never the
decision criterion for a studio engagement anyway.

🟢 🆕 `p387` **Partially closed — and by a channel, not by a workaround.** "Maintenance signal" was
the one criterion in that sentence this base could not actually measure. It can now: **package
registries publish dates**, and 26 education packages are dated in
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv). 🔴 **Still open:** repository
commit activity, contributor counts and issue latency (all behind `api.github.com`, 403), and the
many shelf entries that are **not published packages at all** — for those, publication is absent
rather than old, which is itself worth telling a client.

## Trend 9 — 🆕 `p384` The curriculum-data layer arrived, and its licence is a *database* licence

**Every adaptive-learning pitch rests on knowing what a learner must master before the next topic.
Until this pass, no shelf here held that artefact. Now one does — and it is not licensed like code.**

[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) `v1` publishes **1,930
micro-topics** and **4,102 prerequisite edges** as a DAG — each edge tagged `hard`/`soft` with a
one-line reason — over **9 subjects**, aligned to **NGSS, Common Core, the UK National Curriculum**
and the Australian curriculum. Its grant, read first-hand at `main/LICENSE` (25,289 B), is the
**Open Data Commons Open Database License (ODbL)**. There is **no separate code grant**.

**Why this is a trend and not just a row.** Every licence question these shelves have answered so
far was a **copyright** question about code: can we link to it, can we ship closed extensions. ODbL
is a **share-alike database right**, and it draws its line in a different place:

- **§4.3 — a *Produced Work*** (the tutor's output: a lesson plan, a next-topic choice, an
  explanation) needs **an attribution notice and nothing else**. 🟢 This is the permissive path.
- **§4.4 — a *Derivative Database*** (the client's topics merged in, standards remapped, the graph
  re-cut) must be publicly used **only** under ODbL, a later ODbL, or a compatible licence. §4.4(b)
  is explicit that extracting *"the whole or a Substantial part of the Contents into a new
  database"* **is** a Derivative Database. 🔴 This is the trap, and it is the thing a studio would
  naturally do next.

🔴 **A licence scanner pointed at code will not see this at all.** Neither will a licence badge:
ODbL is not in the permissive/copyleft taxonomy these shelves have been using, so the row cannot be
classified green or red — it is **green on one axis and red on the other, depending on what you
ship**. `Pattern L` was built for the case where a badge misreports a code grant; this is the case
where the *category* is wrong.

**So:** three concrete consequences.
1. **Ground on it, do not fork it.** Keep client curriculum data in a separate store joined at
   query time, so the taxonomy stays an **input** rather than a component of the deliverable. That
   is **Pattern H** in [`compose/patterns.md`](../compose/patterns.md).
2. **Add a data-rights question to intake.** Alongside "what licence is the code", ask "what rights
   govern the **data** we ground on". Education runs on standards, item banks and curriculum maps —
   this will not be the last ODbL/CC-BY-SA artefact on these shelves.
3. **Check coverage before promising it.** The maintainers state their own gap: teaching research
   covers **1,049** topics (Science and Mathematics) and **881 topics have none**. A
   research-backed-guidance claim is true for roughly half the graph.

## Trend 10 — 🆕 `p388` The parent is the unserved persona in education AI, and the statutes are pushing toward them

Every market map this base has built, and every roundup it has read, segments education AI into
**student-facing** and **teacher-facing** — `Trend 5` is about which of the two is growing faster.
Both categories are about people *inside* the institution. **The parent is outside it, and is the
person who actually logs into the portal.**

**The supply arrived this pass and it is not a prototype tier.**
[chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) (**MIT**, 20 tools
over **Infinite Campus / Campus Parent**, **47 published releases**) and
[chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) (**MIT**, 18 tools,
**43 releases**) are maintained, deliberately scoped to the observer surface, and built by one
maintainer working the same problem across two platforms — which is what a real need looks like
rather than a weekend demo.

**Three reasons this is a trend and not a curiosity:**

1. **The statutes are already there.** Every North American instrument this base tracks puts
   **family transparency** in the text — Oklahoma SB 1734 names it outright; Maryland's Chapter 634
   is built around guidance districts must hand down to families. Regulators keep asking
   institutions to *explain AI to parents*; nobody is building the surface that would.
2. **There is no incumbent to displace.** The parent portal is a **feature of the SIS**, not a
   market. No vendor defends it, and the SIS vendors have no incentive to open it. That is the rarest
   condition in education software, where every other surface has a 20-year incumbent.
3. **It inverts the tenancy problem instead of solving it.** `p386`'s finding — every granted LMS
   server authenticates as the signed-in user, so a studio cannot hand one to an institution — reads
   as a *defect* for student and teacher tools. For the parent it is **the correct architecture**:
   the parent's own credential, the parent's own child, no institutional tenancy required at all.

🔴 **And the boundary that defines the engagement, because it is not a licence boundary.** Hosted by a
family, these tools are a person exercising their own access. **Hosted by a studio for a district, the
identical API call becomes a FERPA-governed disclosure of an education record.** The code does not
change; the obligation does. 🔵 So the honest market shape is **two different products**: a
parent-side tool (no tenancy, no FERPA exposure, no institutional sale) and a district-side one (full
tenancy, full FERPA, a real procurement cycle). Conflating them is how this gets sold wrong.
`Pattern P` in [`compose/patterns.md`](../compose/patterns.md) is built on that split.

## Trend 11 — 🆕 `p388` Jurisdictional curriculum content is becoming the defensible layer, and it is arriving region by region

`Trend 9` recorded that a curriculum-data layer had arrived and that its licence was a **database**
licence. `p388` shows the *shape* that layer is taking, and it is not one global graph:

| region | asset | licence | what makes it local |
|---|---|---|---|
| **North America** | 🆕 [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 🟢 MIT | The **BC Ministry** K–12 curriculum in its real three-column **KDU** structure — and the **First Peoples Principles of Learning**, a provincial requirement no imported product carries |
| **LATAM** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) (`p387`) | 🟢 MIT | **BNCC** skill codes, Brazil's national curriculum, with invented codes discarded before a teacher sees them |
| **Global** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (`p384`) | 🟡 **ODbL** (database licence) | 1,590 topics / 3,221 prerequisite edges mapped to NGSS and Common Core |

**The pattern across the three:** the model is interchangeable, the *curriculum authority* is not.
A tutor that cites a BNCC code, a BC Big Idea or an NGSS standard is doing something a
general-purpose tutor **cannot** — not because its reasoning is better, but because it is anchored to
the instrument the jurisdiction grades against.

**Three consequences for an engagement:**

1. **Curriculum grounding is now demonstrable in three regions, not described in one.** `Pattern H`
   stops being a proposal and becomes a reference build with a local example in hand.
2. 🟡 **The risk on these assets is currency, not licence.** The BC server is 🟢 MIT — clean — but it
   is a **crawl** of `curriculum.gov.bc.ca`, last published **2026-03-27**. Curricula are revised on
   political timetables. **Quote the re-crawl as a maintenance line item**, and never let a client
   believe a crawl is a feed.
3. **Keep asking the data-rights question from `Trend 9`.** Two of the three assets above are code
   (MIT); one is a **database** under ODbL. "What licence is the code?" and "what rights govern the
   data we ground on?" remain two different intake questions with two different answers.

## Trend 12 — 🆕 `p388` An exhausted channel is not an exhausted supply — and "published but unreadable" is now a real category

This is a trend about **how this industry's open-source supply is actually distributed**, and it has
a direct procurement consequence.

**The discovery finding.** `p382` recorded that this industry's address supply was **exhausted**.
What was exhausted were four search-engine legs. **`registry.npmjs.org/-/v1/search` is open**, and 29
education queries returned **383 GitHub addresses absent from this entire base**, of which **22 are
granted and education-specific** — the largest single intake in this base's recorded history. 🔵 The
general lesson, and it is the third of its kind here: `p386` learned *a count of addresses is not a
count of grants*; `p387` learned *a null leg is not a null supply*; `p388` adds *an exhausted channel
is not an exhausted supply*. All three are one error — **a property of the instrument reported as a
property of the industry.**

🔵 **Why a package registry is structurally the better instrument for this industry.** A trending page
ranks by attention over days. Education tooling is **institutional, unglamorous and
low-star** — a 47-release parent-portal server for a US K-12 SIS will never trend anywhere. The
registry indexes it anyway, and returns its **entire publish history in the same call**, which
answers "is it maintained?" at the moment of discovery rather than two steps later.

🔴 **The new supply category, and it is the uncomfortable half.** Of 32 addresses probed, **6 publish
to npm from a repository that is not publicly readable** — `git ls-remote` prompts for credentials,
so the repository is **closed, not missing**. The package installs; the provenance cannot be audited.
The costliest instance is **103 published versions** of an AI-generation quiz library **with SCORM
support** ([thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)); the
most instructive is [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest
declares **`"SEE LICENSE IN LICENSE"` — pointing at a file inside a repository nobody can read.**

**So the licence-reading discipline this base built needs one more rule.** `Pattern L` clears a
repository by reading its **subtree**; for these there *is* no subtree. The rule that replaces it:
**for an npm-only dependency, the manifest is a claim and the tarball is the evidence** —
`registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves the published artefact even when the repository is
closed, and **it is the licence that actually ships**. 🔴 That is how this pass established that a
major publisher's tutoring SDK (**115 published versions**) carries **no licence at all**: not from
the repo, which is private, but from the artefact, which is not. 🔵 And the corollary a studio should
internalise: **commercial education vendors are starting to distribute as closed SaaS with an npm
veneer.** The npm scope looks like open source, installs like open source, and grants nothing.

🔵 🆕 `p391` **The channel now has a decay curve, not just a verdict.** Re-run with 32 queries of
*fresh* vocabulary (tenancy, SEN/IEP, proctoring, QTI, xAPI, OneRoster, FERPA, standards, personas):
**321** addresses absent from this base → 37 past a domain filter → 11 probed → **3 shelvable**.
That is **0.9%**, against `p388`'s **5.7%** (22 of 383). 🟢 The channel is **depleting, not
exhausted** — it still produced three rows, one of which opened a category (`Pattern W`). 🔴 But the
seam `p388` opened is largely mined, so the next pass should change **channel**, not vocabulary.
🔴 **And the instrument nearly lied:** the first draft of the domain filter matched the query column
of its own output and "confirmed" 37 education rows that were Vercel, AWS and Storybook packages.
Caught before a shelf. *A filter that scores its own prompt is not a filter.*

## Trend 13 — 🆕 `p389` The supply has a currency problem, and it is now a number

This base has built a careful discipline about *licences* and almost none about *time*. `p387` and
`p388` both recorded that no maintenance signal was available. It was: **`git` read access is open to
every public repository**, and a blobless shallow clone returns the last commit date at the real
default ref in about a second. Sixty addresses were dated this pass.

**The distribution, which is the trend.** 58 live, 2 dead. **48 of 58 moved within 30 days**, and 17
of those were committed **on the day of the pass**. That is a healthier supply than this industry's
reputation suggests — education tooling is unglamorous, not abandoned. But **7 of 58 are past 120
days, and four of those seven carried a recommendation on these shelves**:

| stale address | days | what it was being recommended for |
|---|---|---|
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 343 | a Tier-1 tutor |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 242 | Moodle integration |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | 209 | North American curriculum grounding |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 144 | Canvas integration — **and it is ungranted** |

🔵 **The general shape, and it is this base's fourth instance of one error.** `p386`: a count of
addresses is not a count of grants. `p387`: a null leg is not a null supply. `p388`: an exhausted
channel is not an exhausted supply. **`p389`: a closed popularity channel is not a closed maintenance
channel.** Four passes, one mistake — *a property of the instrument reported as a property of the
industry* — and each time the fix was to ask which channel was actually being measured.

🔴 **The procurement consequence, which outlives the instrument.** A licence tells you whether you
*may* build on something. A date tells you whether you will be **alone** on it. Those are different
risks and they price differently: an MIT repository that has not moved in eight months is a
**vendoring decision with a maintenance line in the estimate**, not an integration. Both numbers
belong in the same row of a proposal, and until this pass only one of them was here.

🟡 **And the limit, stated so the number is not over-read.** A commit date says someone pushed — not
to the branch a release is cut from, and not that the project is healthy.
[instructure/canvas-lms](https://github.com/instructure/canvas-lms) is the case in point: `master` is
175 days behind while its `stable/*` branches move, because that is how Instructure ships. A
specification or a dataset that is *finished* is not decaying either. Read the date against what the
artefact is.

## Trend 14 — 🆕 `p389` APAC has become the net exporter of open-source education AI, and the Gulf the net importer

**The supply side.** The largest education-native repository in open source is
[**OpenMAIC**](https://github.com/THU-MAIC/OpenMAIC) — **MIT**, ~41.3k ★, from **Tsinghua
University**, committed the day of this pass, published in **JCST 2026** and validated inside the
university on **700+ students**. It is not an outlier in its region: the Tier-1 tutor shelf on
[`agents/top.md`](../agents/top.md) is now **majority APAC by origin** — DeepTutor (HKU, Apache-2.0),
ai-shifu (China, Apache-2.0), educhain (India, MIT), OpenTutor (China, MIT), Aha Tutor (China, MIT),
learn-shell (China), ChatTutor (APAC) — against one EMEA entry (mentingo, Poland) and, at Tier 1, one
North American (tutor-gpt, now 343 days stale). 🔵 **The pattern is not "China ships a lot of AI."**
It is that **the pedagogy is being designed in the repository** — mastery estimates that record
*confidence* separately from correctness, FSRS review built in, cognitive-load detection,
misconception-aware branching — in projects whose authors are university teaching groups rather than
startups. That is a supply a studio can build a practice on, and its licences are permissive.

**The demand side, created by statute rather than by procurement.** The **UAE** approved an AI
curriculum across **all public and private schools** by Cabinet decision in September 2026, with
**22,000 teachers and education professionals** to be trained, and for 2026-27 merged Design,
Innovation and Computer Science into a single subject, *Artificial Intelligence and Technology*,
KG–Grade 12. **Saudi Arabia** began a comprehensive AI curriculum across all levels of public
education in the 2025-26 academic year, led by the **National Curriculum Center** with **SDAIA**.
These are the most aggressive AI-in-education mandates anywhere: not permission to pilot, a
**compulsory subject with a teacher-training number attached**.

🔴 **And the mismatch is the opportunity.** This pass found **no Gulf-origin and no Arabic-first
open-source education agent or platform** — not one address. The region with the world's strongest
statutory demand for AI teaching material has, as far as this base can see, **no local open-source
supply at all**, while the permissive supply that does exist is EN + zh-CN. The gap is not a model
gap; it is **curriculum-grounding and language**: Arabic-first content, alignment to the UAE MoE's
seven curriculum areas, and the teacher-training surface those 22,000 professionals will be trained
on. 🟡 Recorded as an informed gap, not a finding: the searches run were English-language, and an
Arabic-language search is the obvious next leg.

## Trend 15 — 🆕 `p389` The parent surface now has a cautionary case, and it is in LATAM

`p388` added the parent/guardian persona and named **FERPA** as the line that splits a family-run
assistant from a district-hosted one. The LATAM equivalent of that line is **LGPD Article 14**, and
unlike FERPA it already has a public failure attached to it.

- **Brazil has no AI statute in force.** As of October 2026 **PL 2338/2023** — passed by the Senate
  in December 2024 — is still in the Câmara dos Deputados, with reports that the vote resumes after
  the October 2026 elections. So the binding instrument for an education engagement today is the
  **LGPD**, not an AI law.
- **Children's data has its own consent basis.** For core teaching a school generally relies on
  contract and legal obligation, but uses **beyond** that — images, communications, extracurricular
  activity — require **specific, explicit, recorded and revocable consent from a parent or guardian**
  under Art. 14. An AI parent portal is squarely in the "beyond" category.
- **The cautionary case.** In 2023 the São Paulo state education department (**SEDUC**) had its
  *Minha Escola* app installed on parents' phones without notice or consent; Data Privacy Brasil
  assessed it as a probable LGPD violation. 🔵 **This is the precise failure mode of the persona
  `p388` added** — a district-hosted parent surface deployed *to* families rather than *for* them —
  and it is the reference a LATAM client will have in mind, so bring it up first.

🟢 **What this makes defensible rather than risky.** The pattern that survives Art. 14 is the one
`Pattern P-1` already describes: the **family runs the agent and exercises its own access right**, so
no new disclosure is created. For the district-hosted variant (`P-2`), the deliverable a Brazilian
client should be sold is the **consent and revocation mechanism itself** — per-guardian, recorded,
revocable, auditable — as a first-class feature, not a checkbox. 🟡 **Mexico: informed gap.** No
education-specific AI guidance or student-data rule was found for Mexico in this pass; the general
position is a data-protection regime and no AI statute. Stated, not inferred.

## Trend 16 — 🆕 `p390` The copyleft firewall moved inside the platform, and it is a packaging decision rather than a licensing one

For several passes this shelf framed "permissive agent + copyleft platform" as a problem solved at
the **boundary**: hold the agent outside the LMS and talk to it over LTI or MCP, so no copyleft
reaches your code. That is still a valid pattern, but `p390` found the cleaner answer was in the
platforms' own packaging the whole time, and **nobody had read it per-package**:

| package | role | licence |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | the platform you deploy | 🔴 **AGPL-3.0** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | the component API your plugin imports | 🟢 **Apache-2.0** |
| [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | what you develop against | 🟢 **Apache-2.0** |
| [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) | newer core data layer | 🔴 **AGPL-3.0** |

All four read from the payload at their real default ref on **2026-10-22**; the two Apache grants are
at `LICENSE.TXT`, which is also why a badge-level or root-`LICENSE` read misses them.

**Why this is a trend and not a trivium.** It means the in-platform plugin — the deepest, most
useful integration, with full access to course state and no network hop — is **also** the one that
can stay MIT or proprietary. The industry had been treating depth of integration and licence freedom
as a trade-off, and for Open edX specifically they are not. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA)
(MIT, Universidad Tecnológica de Pereira) has been shipping on exactly this basis.

🔴 **The trend has a sharp edge: the boundary is per-package, and it is moving.** `openedx-learning`
is the newer core data layer and it is **AGPL-3.0**. As more platform functionality migrates there,
the set of imports that keeps a plugin permissive **shrinks**. Audit the dependency list in CI, not
once at kick-off. The general rule this generalises to: **licence is a property of the package you
import, not of the organisation that publishes it** — and in education, where every major platform is
copyleft, that distinction is worth real money.

## Trend 17 — 🆕 `p390` Voice is the next interface gap, and the open-source supply has not arrived

Across seven passes these shelves accumulated tutors, graders, LMS connectors, parent portals and a
generated classroom. **Every one of them is text-first.** `p390` found exactly **one** granted
voice-first education agent in the open-source supply — [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
(MIT, Brazil, pt-BR, 15 days old, self-described as *"in development"* with no public deployment).

**Why the gap matters commercially.** Voice is not a convenience feature in this industry; it is an
access feature, and it maps onto precisely the markets with the fastest growth and the least supply:

- **Early grades**, where reading and typing fluency is the thing being taught, not assumed.
- **Shared-device and phone-only households** — the LATAM and APAC reality `Trend 10` documents.
- **Language learning**, where pronunciation *is* the assessed skill and text cannot carry it.
- **Accessibility**, which in EMEA public procurement is frequently a scored requirement rather
  than a nice-to-have.

**Why the gap is narrow rather than deep, which is the opportunity.** The hard parts are already
permissive and maintained: [`livekit/agents`](https://github.com/livekit/agents) (Apache-2.0) solves
turn detection, interruption and barge-in — the things that actually make a spoken tutor usable — and
[`mozilla/common-voice`](https://github.com/mozilla/common-voice) supplies **CC0-1.0** speech corpora
across ~130 language variants for ASR evaluation and fine-tuning. What is missing is not
infrastructure; it is **an education-grade assembly of it** — mastery model in the loop, symbolic
checking behind the arithmetic, and the biometric/disclosure posture a school can sign.
🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md) is that assembly.

🔴 **`Gap 390-A` — the informed gap, stated rather than left as silence.** The searches this pass ran
for an open-source voice or multilingual tutor in an **African or South Asian language** returned
**nothing granted and maintained**. What came back instead: one India-first multilingual *toolkit*
(not a tutor), an arXiv framework for low-cost home language learning with **no public code located**,
and a repository that teaches *Spanish to non-speakers* inside an agent CLI — which is the inverse of
a Spanish-language tutor for Spanish-speaking learners, a category error this base recorded in `p388`
and which keeps recurring in search results. 🔵 **Read this as a null result in the open-source
supply, not a null in demand** — Africa is among the fastest-growing online-education markets. For a
client engagement in those languages the honest position is: **the substrate is permissive and ready,
the localised tutor does not exist and would be built, and Common Voice is where its evaluation set
comes from.**


## Trend 18 — 🆕 `p391` Education AI is shipping as **harness extensions**, not standalone applications

Three of this base's education rows are now plugins to the *same* agent harness, by **three
unrelated maintainers**, all MIT, all published inside about ten days:

| row | what it is | published |
|---|---|---|
| [`BaronCyrus/dsh-aha-tutor`](https://github.com/BaronCyrus/dsh-aha-tutor) (`p388`, Tier 1) | narrated-blackboard adaptive tutor | npm v1.7.0, 2026-10-22 |
| [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🆕 `p391`, Tier 1) | diagnosis-first learning runtime | npm v0.1.1, 2026-10-17 |
| [`GuoMonth/dsh-multi-tenant`](https://github.com/GuoMonth/dsh-multi-tenant) (🆕 `p391`) | K8s + OIDC multi-tenant hosting for the same harness | npm v0.10.0-rc.1, 2026-10-12 |

They are extensions to **DeepSeek Harness**, and the pattern is not harness-specific — this pass also
read [`mackt/pi-language-tutor`](https://github.com/mackt/pi-language-tutor) (MIT) as an extension to
the Pi agent. 🟢 **Why it is a trend and not a coincidence:** a harness extension inherits model
plumbing, tool calling, auth, UI shell and a distribution channel for free, so a single maintainer can
ship a credible tutor in weeks. The economics now favour the plugin over the application.

🔵 **The operational consequence, and it explains a channel result this base has hit repeatedly.** The
distribution channel for education AI is becoming **the agent harness's package registry** — which is
why `registry.npmjs.org` keeps yielding education supply while `moodle.org` has never once been
reachable *or* necessary. Looking for education AI in LMS plugin directories is looking where it was
built in 2019.

🔴 **The cost a studio inherits, stated plainly.** A harness extension is **not deployable without its
harness**. `dsh-diagnostic-tutor` requires DeepSeek Harness; adopting it means adopting that runtime,
its update cadence and its governance. For a client who cannot, the move is to copy the *structure*
(see `Pattern X`) rather than the package — which is exactly why `Pattern X` separates the pedagogy
from the runtime instead of recommending the repository wholesale.

## Trend 19 — 🆕 `p391` The standards body's reference implementation goes stale; the **vendor fork** carries the maintenance

`p390` dated [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) at 2,332
days and concluded the LTI 1.3 integration path had no installable implementation. The grant and the
dating were both right; the conclusion was wrong, because the maintained line is not at the
authoritative-looking address:

| address | last commit | registry | verdict |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **2026-10-16** | packagist `lti-1p3-tool` **v6.4.4**, 68 versions, 2026-09-23 | 🟢 **install this** |
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (Node) | **2026-10-13** | npm `ltijs` **v7.0.7**, 207 versions, 2026-10-06 | 🟢 **install this** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | 2020-06-03 | — | 🔴 spec citation only |
| [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) | 2020-06-03, **identical sha `3a192de`** | — | 🔴 the same project, renamed org |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (Python) | 2022-11-21 | PyPI `PyLTI1p3` 2.0.0, **2022-11-20** | 🔴 genuinely dead |

🟢 **The generalisable rule:** in standards-driven education interop, the consortium publishes the
spec and a demonstration; a **vendor with production traffic** maintains the library. So when a
reference implementation dates badly, the next question is *who ships this in production* — not
*should we vendor the spec*. Check the fork network and the package registry before concluding a path
is closed.

🔴 🆕 `p392` **The "language asymmetry" half of this trend is WITHDRAWN, and withdrawing it sharpens
the rule above rather than weakening it.** `p391` closed this trend with: *"Node and PHP have
maintained LTI 1.3; Python does not… the interop edge is therefore a separate Node or PHP service in
front of the agent."* Read first-hand this pass, **Python has three**:

| address | grant | last commit | registry | role |
|---|---|---|---|---|
| [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | **2026-10-20 — 2 d** | PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07 | 🟢 **in-process**, Django app + middleware |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 — 113 d | PyPI **v1.6.3**, 15 releases | 🟢 LTI 1.1 **and** 1.3 into JupyterHub |
| [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **AGPL-3.0** (34,520 B) | **2026-10-22 — 0 d** | PyPI `lti-consumer-xblock` **v11.4.2** | 🔴 best-maintained of the three, **copyleft** |

🟢 **And the maintainer pattern holds in Python too, which is the trend's real content.** The three
Python implementations are maintained by a **university innovation centre** (Michigan), an
**ecosystem project** (Jupyter) and a **platform vendor** (Open edX) — not by the standards body. The
rule is unchanged and now has six instances instead of four: *in standards-driven education interop,
ask who ships this in production.*

🔴 **What survives as a constraint is licence-shaped, not language-shaped**, and that is a more useful
thing to tell a client: the best-maintained Python LTI implementation is **AGPL-3.0**, the
best-maintained Node one is Apache-2.0, and the permissive Python options are smaller (26 ★ and 73 ★)
and framework-bound. The question is never *"does this language have LTI"* but *"does the maintained
implementation in my language carry a grant I can ship?"* `Gap 391-A` **CLOSED**.

## Trend 20 — 🆕 `p392` The granted proctoring supply covers the **lockdown**, not the **inference** — which is the opposite of the regulatory exposure

For four passes this base recorded proctoring as having *"no credible permissive open-source option"*
and treated that as a liability boundary to name rather than fill. Probed first-hand, the supply
exists — and its **shape** is the trend:

| component | grant | last commit | what it actually does | the AI part |
|---|---|---|---|---|
| [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) | 🟢 **MIT** (1,069 B, manifest agrees) | **2026-09-28** | tab-switch, right-click, DevTools shortcuts, clipboard events, camera state, **faces**, audio loudness, **virtual-camera / loopback / screen-share detection** | 🟢 **real** — face-api on TF.js, **in the browser** |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 🔴 **CONFLICT** — Apache-2.0 payload, `ISC` manifest **and** npm | **2026-10-13**, 398 commits | blocks copy/paste/cut, right-click, selection, shortcuts; detects `tabSwitch`, `browserBlur`, `exitTab`, `fullScreen`; periodic page and webcam snapshots POSTed to an endpoint you build | 🔴 **absent** — object detection, multi-face and eye tracking are marked *"(To be Done)"* |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🔴 **AGPL-3.0** | 🆕 re-read `p392`: `master` HEAD **2026-10-22 — 0 d** (this base's harvest row said 2026-05-30; the live read is today), 253 releases | the exam **workflow** — attempts, review states, integration points | 🔴 none; it brokers a vendor |

🔵 **The asymmetry, stated as a rule:** open-source proctoring is **deterministic browser lockdown and
event telemetry**, while the **inference** — identity, gaze, multiple faces, behavioural scoring — is
either absent, roadmapped, or the proprietary service the AGPL workflow brokers. 🟢 **And the
regulatory exposure runs the other way.** Lockdown and event logs do no biometric inference: they
are not what the EU AI Act's Annex III is reaching for, and they are explainable to a student
(*"you left fullscreen at 14:03"*). The inference layer is where high-risk obligations, biometric
rules and the whole evidentiary argument live — and that is exactly the layer the permissive supply
does not have.

🟢 **So the honest advice to a client flips, and it is now sellable in both directions:** *we can
build the integrity layer you can defend — lockdown, event trail, human review — permissively and
today; the part that would flag a student automatically is the part that makes you a deployer of a
high-risk system, and neither of us should want it in v1.* 🔴 The obligation attaches to the
**deployment**, not the dependency, so an open-source grant transfers no compliance relief whatsoever.

## Trend 21 — 🆕 `p392` LATAM's public buyers are procuring AI education platforms as **subscriptions**, and no tender asks for open source

A replacement regional leg shaped like a **buyer** rather than a supplier — public-procurement
vocabulary in Spanish and Portuguese — returned five live 2026 instruments where three passes of
English, stars-sorted supply legs returned nothing: Santa Fe province (Argentina, Tender 01/26,
*subscriptions* to AI-enhanced educational cloud platforms), **OEI-Chile `OEI-LIC-1-25`** (design and
build of an AI platform for **administrative management in Chilean schools** over regulatory,
financial and operational data), UNOPS Argentina `ITB/2026/62779` (educational platform **licences**,
2+2 years), the **CIEDEPAR** consortium in Paraná (multi-municipality SaaS education management) and
Francisco Morato, SP (**R$1,924,665.00**).

🔴 **Not one of the five specifies free or open-source software.** The spend is real, the AI framing
is explicit, and the procurement shape is **product subscription**.

🔵 **Why this is a trend and not five anecdotes:** it is the demand-side mirror of *Trend 6*. This
base's whole thesis is permissive assembly, and the buyers writing the cheques are specifying
subscriptions — so the binding constraint on an open-source education engagement in LATAM is **the
specification, not the licence frontier**. 🟢 The opening is a total-cost bid against subscription
pricing, with the OEI-Chile scope (administrative management, compliance recommendations) matching the
`i-educar` + agent shape these shelves already hold; the work is to get *"or equivalent open-source
implementation"* into a specification written for a product. 🟡 Graded **`ATTRIBUTED-UNVERIFIED`** —
aggregators and news items; no official portal (COMPR.AR, ChileCompra, PNCP) is reachable here.


## Trend 22 — 🆕 `p393` The education **interoperability layer is Python** while the agent layer is TypeScript, and a one-registry sweep answers half the question

**What was measured.** `p393` opened the channel `Gap 392-C` said did not exist: `pypi.org/simple/`
under PEP 691 returns **920,784 project names in 45,189,043 B in 1.4 seconds**, unauthenticated. A
sweep of 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, 13 live and
verified first-hand.

**What came back was a layer, not a list.** Not more tutors or more agents — **plumbing**:

| standard / surface | granted Python supply found | grant |
|---|---|---|
| **LTI 1.3 / Advantage** | `openfun/django-lti-toolbox` (France Université Numérique), `Harvard-University-iCommons/django-lti-dynamic-registration` | 🟢 MIT, 🟢 MIT |
| **QTI** (assessment exchange) | `vosslab/qti_package_maker`, `Citolab/qti-convert-python` (Cito, NL) | 🟡 LGPL-3.0, 🔴 GPL-3.0 |
| **OneRoster / Caliper** | the `timeback-*` family — 🔴 **source unresolvable** | 🔴 unauditable |
| **Ed-Fi** (US K-12 data) | `edanalytics/edfi_api_client`; `Ed-Fi-Exchange-OSS/LMS-Toolkit` 🔴 archived | 🟢 Apache-2.0 ×2 |
| **LMS → agent bridge** | `Dathis/swiss-moodle-mcp`, `Snaw80/moodle-mcp` | 🟢 MIT ×2 |
| **Autograding** | `edulinq/autograder-py`; `otter-grader` already carried, now measured at **161 ★** | 🟢 MIT, 🟢 BSD-3 |

🔵 **Why this is a trend and not a haul.** The split is systematic. The **agent** layer — MCP servers
for Canvas, tutors, parent agents — is overwhelmingly **npm/TypeScript**, which is why eleven passes of
npm sweeps built a rich agent shelf. The **standards and institutional-data** layer is
**PyPI/Python**, because it lives next to the Django and Flask applications that universities and
ministries actually run (Open edX, `now-lms`, campus SIS integrations) and next to the
notebook-and-grading stack. 🔴 **A supply claim is therefore only as wide as its registry.** This base
published *"there is no maintained Python LTI 1.3 library"* (`Gap 391-A`) from a channel that
**cannot index PyPI** — and then found five.

🟢 **The rule for a studio:** one discovery channel per ecosystem, named before any absence is
published. This base's set is now npm + PyPI + Packagist (measured, 0 yield) + `git ls-remote` and
`raw.githubusercontent.com` for verification. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** —
and CRAN matters here, because `otter-grader` grades **R** and the statistics-teaching stack is
R-shaped.

🔴 **The cost of the channel, stated with it:** the dump carries **names only**, so it discovers by
token and a token is not a capability. Two of fifteen candidates were pure collisions — `proctor-ai`
is a **prompt-engineering** library, `xapi-python` is the **xStation5 broker API** — and whole keys are
unusable (`canvas` returns 146 names dominated by HTML-canvas and AWS Nova Canvas; `d2l` is
Dive-into-Deep-Learning). Discovery is cheap; **adjudication is the work**.

## Trend 23 — 🆕 `p393` A new supply class: **live releases, dead source** — and the licence claim is unauditable in principle

**The instances, found the same hour.** [`superbuilders/timeback-dev-python`](https://github.com/superbuilders/timeback-dev-python)
is the declared `Repository` of **three** actively-released PyPI packages — `timeback-qti`,
`timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last
**2026-07-18**, each declaring **MIT**, together the most complete 1EdTech client family in Python on
paper. 🔴 **The repository does not resolve for an unauthenticated clone.** Second instance:
`moodle-mcp-bridge` v1.7.0, advertising *"a Moodle site as 88 typed AI tools"* → `NmaaAlhawary/MCP-Moodle`,
also unresolvable.

🔵 **Why this is a distinct class and not a variant of an existing one.** This base already grades
three failure modes, and none of them covers this:

| class | the payload | the verdict |
|---|---|---|
| `UNGRANTED` (no licence file) | exists, is empty of a grant | read, and found wanting |
| `README-ONLY` / `MANIFEST-ONLY` | a grant **asserted** somewhere other than a payload | downgraded, because the assertion is checkable against the absence |
| 🆕 **`LIVE-RELEASES-DEAD-SOURCE`** | 🔴 **cannot be fetched at all** | **not assessable** — there is nothing to read, and no amount of care fixes it |

🔴 **The procurement consequence is sharper than it looks.** `p388`'s *"published but unreadable"* was
about a payload that says nothing; this is about a payload that **cannot be obtained**. A studio can
install these packages — pip will resolve them happily — but it **cannot warrant the licence to a
client**, because warranting a grant means having read it. And an MIT declaration in registry metadata
is a claim by the uploader, not a grant in a distributable artefact.

🟢 **What to do with it.** Evaluate in a sandbox if the capability is needed; **never ship it into a
client deliverable**; ask the publisher to open the repository, which is a cheap request and a fair
one. 🔵 And record the class, because the economics favour its growth: publishing to a registry is
free and keeping a public repository is a maintenance commitment, so **more supply will arrive this
shape**, not less.

## Trend 24 — 🆕 `p394` In the teaching stack the **delivery** layer is permissive and the **measurement** layer is copyleft, and a language boundary rides along with it

🟢 **The observation.** `p394` opened the R half of the CS-teaching stack and the licence column split
cleanly down the middle of the pedagogy:

| what it does | components | licence |
|---|---|---|
| **Deliver** the teaching loop — present, accept, grade, respond | `rstudio/gradethis` (**MIT**, 164 ★), `rstudio/learnr` (**Apache-2.0**, 738 ★), `ucbds-infra/ottr` (**BSD-3-Clause**) | 🟢 **permissive, all three** |
| **Measure** the learner — item response theory, adaptive item selection, exam generation, item analysis | `cran/exams` (**GPL-2 \| GPL-3**), `philchalmers/mirt` (**GPL >= 3**), `cran/catR` (**GPL >= 3**), `cran/TAM` (**GPL >= 2**), `ShinyItemAnalysis` (**GPL-3**) | 🔴 **copyleft, all five** |

🔵 **Why it is not a coincidence.** The delivery components are **vendor-authored** — Posit, a company
selling an R platform, and a university programme that needed its autograder to be adoptable. The
measurement components are **academic instruments**, written by psychometricians inside a GPL research
culture and in some cases decades old. **The licence tracks who paid for the code and why**, and it has
produced a split running exactly along the boundary between *product* and *science*.

🟢 **Why that is good news rather than a blocker.** The boundary falls where a studio's product
boundary has to fall anyway: own the teaching loop, reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. 🔴 **The
trap is reading it as a licence problem and swapping in a permissive psychometrics library instead.**
There is no credible permissive equivalent of `mirt` or `catR`; building one is a multi-year research
project and approximating one is how a studio ends up shipping an adaptive engine whose claims it
cannot defend. 🔵 This base already carries the symptom: `adaptive-knowledge-graph` (~350 ★) and
`OATutor` implement IRT and BKT from scratch, and `mirt` — **235 ★, committed daily** — is the thing
they are approximating.

🔵 **And the language boundary rides along with it.** `Trend 22` recorded that the agent layer is
npm/TypeScript while the standards layer is PyPI/Python. `p394` adds that the **measurement** layer is
**CRAN/R**. Three layers, three registries — and a supply claim is still only as wide as the registry
it was swept from. 🔴 **R is the worst case of the three**, because its registry is unreachable here on
**both** tools and its grants are invisible to GitHub's licence sidebar (`Gap 394-B`): five granted GPL
packages in this tier show **no licence** in the GitHub UI, because the grant lives only in
`DESCRIPTION`. **So a GitHub-UI-driven sweep does not merely under-count R supply — it reports it as
unlicensed.**

## Trend 25 — 🆕 `p394` A string matched as though it were a meaning is this base's most productive error class, and it runs in three directions

🟢 **The observation, as a count rather than an impression.** Three independently-found defects, three
different instruments, one mechanism:

| gap | instrument | direction | what the string was |
|---|---|---|---|
| `Gap 392-A` | capability-absence gate | 🔴 **over-refutes** — denies a real absence | a runtime key read as a capability |
| `Gap 393-A` | PyPI index channel | 🔴 **over-discovers** — invents supply | a package *name* read as a capability (`proctor-ai`, `xapi-python`, `canvas`, `d2l`) |
| **`P459`** 🆕 | `licence-grant-gate` | 🔴 **strips a grant** — denies a real permission | **"all rights reserved"**, line 2 of the canonical BSD template, read as a refusal |

🔵 **`P459` is the most expensive of the three and it was the last to be found**, because the other two
produce *visible* nonsense — a claim you can check, a candidate you can reject — whereas this one
produces a **false absence of a grant**, which looks exactly like diligence. A usable component is
quietly marked unshippable and nobody re-opens the question. 🟢 On these shelves its realised damage
was **nil** — no published row was graded from an untitled BSD payload, checked rather than assumed —
and its exposure was **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells.

🔴 **And the fourth instance is on this base's own shelf rather than in an instrument.**
`anastasasenov/bbmcps` sat in the Blackboard census for eight passes because its URL scheme reads
`blackboard://`. It is a shared-memory MCP server; the word is an **architectural metaphor**. So the
class does not only mis-discover and mis-refute — **it mis-files what the base already owns**, and a
census cell inherited as a count is exactly where it hides.

🟢 **The transferable rule, and it is cheap.** Before a token decides a verdict, ask what else that
token means. The gate that got this wrong already holds the right idea one screen away:
`AMBIGUOUS_WORDS = ("apache", "nginx", "mit", "bsd")`, with a comment noting each is simultaneously a
licence name and something else. 🔵 **The insight was applied to licence names and never to licence
clause text, nor to package names, nor to URL schemes.** One lexicon separating a **string** from a
**capability** would close `Gap 392-A`, `Gap 393-A` and the `bbmcps` class together — which is why
`p393` ranked that unification fifth and why `p394` ranks it **first**.
