---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI — Current Trends

**Pass `p527` · 2026-10-29.** Ten trends. Each one is stated so it could be
*wrong* — a trend you cannot disconfirm is a slogan. Where this pass's evidence
**narrowed or contradicted** a trend carried from `p526`, that is marked and the
trend is rewritten rather than quietly restated.

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

🔴 **But Moodle — the sector's largest install base and plugin ecosystem — has no
credible MCP server.** Every candidate was licence-probed and page-read this pass:
the whole field tops out at **27★**
([G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp), MIT), the eight
search results collapse to roughly **three real codebases** once fork lineages are
traced, and the most-visible option
([csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server),
1★) is **AGPL-3.0**. See the lineage table in
[`../repos/foundations.md`](../repos/foundations.md).

**So the honest form of the trend:** MCP is the *intended* integration layer and
the *actual* one only for Canvas and Anki. For Moodle, the plugin boundary is
still the seam — and the gap is the clearest build opportunity on this base.

**What would disconfirm it:** a Moodle MCP server past ~500★, or Moodle shipping
an official one. Either would make this the fastest-moving line on the base.

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

**What would disconfirm it:** skills plateauing while monolithic apps resume
growth, or provenance staying absent from procurement questions.

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
