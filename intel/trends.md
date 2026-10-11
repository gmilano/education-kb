---
industry: education
region: Global
updated: 2026-10-11
---

# Education — current trends

**Pass 130, 2026-10-11.** Full rewrite. Each trend below is stated with the evidence that supports
it and, where it matters, what would falsify it.

## T1 — The governance gap is the market

Student and teacher adoption has outrun institutional policy by an order of magnitude: **88%** of
students worldwide (95% of UK undergraduates) use generative AI, **60%** of US K-12 teachers used it
in 2024-25, and **18%** of US teachers have a written policy telling them how. This is the defining
condition of education AI in 2026. It means the buyer's problem is not capability — the tools are
already in the building — but control, evidence and defensibility.

**Consequence for engagements:** lead with inventory, data-flow proof, human-in-the-loop gates and
audit logs. A tutoring demo does not address the thing keeping the client awake.

## T2 — Mandates with hard dates replaced guidance

2026 is the year education AI rules acquired deadlines:

- **Ohio:** every K-12 district must adopt a formal AI use policy **by 1 July 2026**.
- **South Korea:** AI Basic Act in force **22 January 2026**.
- **India:** AI and computational thinking mandatory **from Class 3, 2026-27 academic year**.
- **China:** AI compulsory from age six since September 2025; Cybersecurity Law AI amendments
  effective January 2026.
- **Vietnam:** Decision 33/2026/QD-TTg names education — including automated assessment and
  behavioural monitoring — as high-risk.
- **EU:** AI literacy duties in force since February 2025; emotion recognition in education
  **prohibited** since 2 February 2025.
- **US states:** 134 bills across 31 states in 2026; 30+ states with guidance.

**The trend is not "regulation is coming" — it is "obligations are already in force and capacity is
missing."**

## T3 — The EU's high-risk clock slipped to December 2027, and that is a sales window

Annex III education obligations (admissions, grading, proctoring) were postponed to **2 December
2027** via the Digital Omnibus on AI, approved by the European Parliament in June 2026 — **Council
adoption was still outstanding** as of this pass, so the delay is politically agreed rather than
final. Meanwhile Article 4 AI-literacy duties and the emotion-recognition prohibition bind now.

**Read it as:** eighteen months to build conformity in by design rather than retrofit it, not
eighteen months of nothing to do. **Falsifier to watch:** if the Council fails to adopt, the
original high-risk dates snap back and every EMEA roadmap compresses.

## T4 — Supply is extraordinarily concentrated, and one repo is the whole mid-market

`HKUDS/DeepTutor` (Apache-2.0) stands at **41 136 stars**. The next education-specific agent found
this pass is `GarethManning/education-agent-skills` at 847 (and its licence does not resolve to an
OSI identifier), then `satvik314/educhain` at 388 and `vishalsachdev/canvas-mcp` at 288. There is
**no middle of this market** — one large permissive agent and a long tail of sub-1k projects.

**Consequence:** a client wanting "the open-source tutoring stack" gets DeepTutor plus bespoke
integration. Budget for the integration, not the engine.

**Correction to this KB's own record:** earlier passes recorded DeepTutor at "~22k★" and then
"~24k★", and `educhain` at "~9k★" then "~12k★". Verified today: DeepTutor **41 136**, educhain
**388**. The educhain figure was overstated by roughly 30×. Star counts in this KB predating pass
130 should not be trusted without re-verification.

## T5 — Connector effort has pooled on Canvas, and fork swarms inflate the apparent supply

Five-plus Canvas MCP servers exist; Moodle — the most deployed LMS in the world — has three AI
plugins and no permissively licensed MCP route; eight of the fifteen platforms in
`verticals/solutions.md` have **no** AI-on-top project at all.

Worse, the apparent supply is padded by **fork swarms**: at least five repositories carry a
byte-identical `canvas-mcp` description under different owners, and `tutor-mcp` appears under two.
A fork-excluding search resolves each to a single canonical upstream
(`vishalsachdev/canvas-mcp`, `ArnaudGuiovanna/tutor-mcp`); one fork still advertises an older
tool count as current. Counting repos overstates the field substantially.

## T6 — Licence risk is concentrated exactly where the traction is

The most-starred education agent-skills collection (847★) reads as **NOASSERTION**. A 103-star
Canvas MCP server has **no licence file at all**. The cleanest Moodle→MCP route is **unlicensed**.
Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to OSI identifiers.

Meanwhile the platforms are mostly **AGPL-3.0** (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse,
ClassroomIO), which network-copyleft binds any client offering a hosted service. The permissive
shortlist is small and worth memorising: **Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT),
Academico (MIT), Richie (MIT), H5P (MIT), XBlock (Apache-2.0), codejail (Apache-2.0)**.

**Consequence:** licence review belongs at the start of an education engagement, not at hardening.
The highest-traction components are the riskiest ones.

## T7 — The missing instrument: nobody measures learning

No open-source benchmark or evaluation harness for *learning outcomes* from agentic tutoring was
found this pass. The OECD's 2026 Digital Education Outlook argues for moving beyond general-purpose
tools toward purpose-built educational AI that produces **durable learning gains** — a standard
nothing in the open-source shelf can currently demonstrate.

**This is the most commercially valuable gap in the KB.** A client who can show measured outcomes
has something no competitor can show, and the measurement apparatus is buildable: `OATutor` and
`tutor-mcp` already expose Bayesian Knowledge Tracing mastery estimates, which gives a defensible
quantitative basis that an LLM's self-report does not.

## T8 — Offline and low-bandwidth stopped being an edge case

Kolibri (MIT, offline-first, content sync by LAN or USB) is the clearest instance of a trend driven
by where growth actually is: APAC at ~35.3% CAGR, India mandating AI from Class 3 across government
schools, LATAM adopting ahead of infrastructure, Google.org targeting 1.25M LATAM students by 2028.
Small local models make an offline tutor technically possible for the first time, and the data never
leaving the device resolves most of the privacy problem in T1 and T2 by construction.

**Nobody has built it:** no AI agent on top of Kolibri was found. MIT licence, offline design,
regulatory tailwind, no incumbent.

## T9 — Administrative automation is the most-cited driver and the least-served

Intelligent tutoring, personalised learning, administrative automation, AI-driven assessment and
virtual assistants are the standard trend list; administration is where institutions report the
clearest return. Yet there is **no open-source agent for a student information system** — no
enrolment, records or timetabling agent. The only candidates are `openeducat_erp` (licence unclear)
and `academico` (MIT, 404★, small). The gap between the stated driver and the available software is
total.

## Watch list for the next pass

- Whether the **EU Council formally adopts** the Digital Omnibus (T3) — binary, high-impact.
- Whether `instructure/canvas-lms` resumes activity; its last push was **2026-04-30**, ~5 months
  quiet, while every other major platform pushed within days of this pass.
- Whether any **Kolibri-based AI project** appears (T8) — the clearest unclaimed slot.
- Whether an **education-specific evaluation harness** emerges (T7).
- Whether **Open edX MCP** moves past experimental; `blend-ed/openedx-mcp` sits at 2 stars.
- **Africa and the Middle East:** no regional evidence surfaced under the EMEA bucket this pass.
  Needs a dedicated query next cycle rather than being folded into EU findings.
