---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI — Current Trends

**Pass `p526` · 2026-10-29.** Eight trends, each with the evidence that produced it
and the consequence for a studio engagement. Where a trend rests on a weak source
it says so.

## 1. The governance gap is the market

**Evidence.** 86% of students across 16 countries use AI in their studies (Digital
Education Council, 2025). K-12 teacher use of generative AI went 25% → 53% in one
year (RAND, 2025). Under 10% of schools have rules for AI use (secondary source,
no primary — directional only).

**Consequence.** Capability is commoditised; nobody is short of a chatbot. What
institutions cannot buy is a deployment that is *auditable*: who saw what, which
decision a human made, what the model was asked. Lead every engagement with the
audit trail, not the tutor.

## 2. Open-source education agents are now APAC-academic, and they are large

**Evidence.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) — Apache-2.0,
**48.9k★**, University of Hong Kong, **v1.7.0 on 2026-10-28**.
[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — MIT, **41.7k★**,
Tsinghua, **v1.3.0 on 2026-10-29**. Together over 90k stars, both permissive, both
shipping releases within 48 hours of this pass. DeepTutor gained roughly
1,600-2,400 stars in a single day per trend aggregators.

**Consequence.** The centre of gravity in open-source education AI is not in San
Francisco. For any tutoring brief anywhere in the world, the correct first move is
to start from one of these two rather than build an agent loop from scratch.

## 3. Pedagogy is becoming measurable, and almost nobody is measuring it

**Evidence.** [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
(MIT, 13★) ships the **CDPK** and **SEND** benchmarks from the paper *Benchmarking
the Pedagogical Knowledge of Large Language Models*.
[anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills)
(Apache-2.0, 601★) ships **eval rubrics** alongside its skills.

**Consequence.** Thirteen stars on the benchmark against 48.9k on the tutor is the
whole story of this field's maturity. Running a published pedagogy benchmark is
currently a *differentiator* in a procurement conversation. It will be table
stakes within a year, which is exactly why it is worth doing now.

## 4. MCP has become the education integration layer

**Evidence.** [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
308★, v1.16.0 Oct 2026) exposes Canvas LMS to assistants with ~102-128 tools.
[anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) (MIT, 538★, v0.27.0)
exposes spaced repetition. The GitHub `ai-tutor` topic now carries multiple
*skill*-shaped repositories rather than applications.

**Consequence.** This is the clean answer to the AGPL problem in §6. An MCP server
talks to Canvas or Moodle **over a process boundary**, so the permissive agent
never links the copyleft core. Integration-by-MCP is both the fastest and the most
licence-safe path, and it is the pattern this base now defaults to.

## 5. Compliance timelines have become build windows

**Evidence.** The **Digital Omnibus, Regulation (EU) 2026/1744** (OJ 24 Jul 2026,
applies from 27 Jul 2026) moved the high-risk deadline for stand-alone education
AI — grading, admissions triage, exam proctoring — from **2 Aug 2026 to
2 Dec 2027**. **Article 50 transparency still applies from 2 Aug 2026**;
emotion-recognition in schools has been banned since Feb 2025. In the US,
**Oklahoma bars AI as the primary basis for grading, discipline or placement**, and
**Maryland, Idaho, Oklahoma and Virginia** require district-level AI policies in
2026. **India requires AI-content labels and provenance markers from 20 Feb 2026.**

**Consequence.** Two products fall straight out of this: (a) a **16-month
conformity scaffolding** engagement in the EU, and (b) **structural
human-in-the-loop** — grading paths where the model *technically cannot* be the
decider. Transparency and labelling obligations are live today and need no new
technology, only an audit.

## 6. The sector is copyleft, and that decides the architecture

**Evidence.** Moodle GPL-3.0 (7.6k★), Open edX AGPL-3.0 (8.2k★), Canvas AGPL-3.0
(6.9k★), Frappe LMS AGPL-3.0 (3.4k★). A deliberate search for a mainstream
Apache/MIT LMS found none. The permissive exceptions are smaller:
[Oppia](https://github.com/oppia/oppia) (Apache-2.0, 7.0k★),
[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, 449★),
[Sakai](https://github.com/sakaiproject/sakai) (ECL-2.0, 1.2k★),
[Kolibri](https://github.com/learningequality/kolibri) (MIT, 1.2k★).

**Consequence.** AGPL-3.0 §13 reaches network users, which is the hosted shape every
engagement wants. **Integrate, do not fork** — and when a fork is genuinely
required, fork a permissive core. This is a licence decision that has to be made
before the first commit, not after.

## 7. Licences in this sector lie, and the lie is on the title line

**Evidence.** [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) opens its
licence with the MIT grant sentence and then prohibits redistribution outright and
demands a revenue share before commercial use — its title reads "PageLM Community
License". [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) (340★)
is **Elastic-2.0**, which forbids the hosted-service shape. A maths corpus titled
*"Attribution-NonCommercial 4.0"* grades as `CC-BY-4.0` to a body-matching probe.
[rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (**107.5k★**)
serves its grant at `LICENSE.txt` and the repository page names **no licence type**,
so single-filename probes file it as ungranted. 🟡 Counter-note: `cn-math-taxonomy`'s
page badge reads `CC BY-NC 4.0` *correctly* — that trap exists only in the probe,
not in what GitHub serves.

**Consequence.** Grade licences from the **title block**, check `LICENSE`,
`LICENSE.txt` and `LICENSE.md`, and never drop a `NonCommercial` qualifier from a
family name. This is a due-diligence step with real money behind it: PageLM's §4
makes a revenue-share agreement a precondition of commercial deployment.

## 8. The buyer is shifting from the learner to the teacher

**Evidence.** Teachers using AI weekly save **5.9 hours/week** (Gallup + Walton,
2025) — a measurable, CFO-legible number. The 2026 Holon IQ LATAM EdTech 100 shows
AI positioning moving **toward teachers**, with Brazil's **Teachy** (AI lesson
preparation) as a regional incumbent and upskilling losing ground as a category.
Anthropic's K-12 repository is teacher-skills-and-rubrics, not a student tutor.

**Consequence.** Teacher-facing tooling has a shorter sales cycle, a defensible ROI
number and far less regulatory exposure than anything touching grades or
admissions. It is the right opening move in almost every market — and in LATAM it
is where the market has already gone.

## Counter-signals worth holding

- **Trust is not uniformly rising.** Ipsos Education Monitor 2026 finds **Australia
  and New Zealand more supportive of banning AI in schools** than Asian markets.
  China shut a ~$100B private tutoring industry in 2021; India's BYJU'S collapsed
  into insolvency. In those markets the restraint story sells better than the
  capability story.
- **Adoption is thinner than the headlines.** **CENIA finds 13 of 19 LAC countries
  studied have not yet introduced early AI adoption in schools**, against a global
  narrative of universal uptake.
- **Advising research is genuinely immature.** A literature review found only **67
  relevant papers** on chatbots or AI in academic advising and concluded the area
  has weak empirical validation. Claims that agents can own advising decisions are
  projections, not findings — Georgia State's Pounce answers routine enrolment and
  aid questions with staff handling the rest, and that remains the honest ceiling.
- **Assessment integrity's credible tooling has no LLM in it.**
  [Dolos](https://github.com/dodona-edu/dolos) (MIT, Ghent) does code-similarity
  detection, and a finding that must survive an academic appeal cannot rest on "the
  model thought so."

## Source-quality note

Market-size and funding figures in this pass come from trade aggregators and
vendor blogs, not primary research-firm reports, and they disagree with each other.
Adoption figures (RAND, Gallup/Walton, Digital Education Council, IDB, CENIA,
Ipsos) carry named primaries and are the ones to quote. Regulatory dates were
cross-checked across multiple sources but not read from the Official Journal text
directly; **Regulation (EU) 2026/1744** should be confirmed at source before it
appears in a client deliverable.
