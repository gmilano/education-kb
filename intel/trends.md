---
industry: education
region: Global
updated: 2026-10-31
---

# Current trends — education AI

Research date 2026-10-31. Six trends, each with the evidence behind it and the
confidence it deserves.

## 1. From experimentation to governance (high confidence — every source agrees)

The single most consistent finding of this run. 1EdTech frames 2026 as the year
AI in education shifts "from experimentation to governance." Tutorflow describes
the main change as a shift from experimentation to operational use. Campus
Technology's industry panel expects AI to move from experimentation to **embedded
infrastructure** in higher education — admissions, advising, administration.

**Why it matters commercially:** governance work is budgeted, repeatable and
auditable in a way pilots never were. The buyer changes from an innovation team
to an operations or compliance owner.

## 2. Agentic use cases are the named 2026 capability (high confidence)

Educativa names AI agents as the year's big development, specifically agents
that **plan lessons and draft assessments for teacher review** — note the
human-in-the-loop framing, which is also what the high-risk regimes require.
HolonIQ expects focus on agentic use cases alongside ethics and transparency.

**Measured corroboration:** the field is visibly agentic and visibly MCP-shaped.
Four of six agents on [`../agents/top.md`](../agents/top.md) are MCP servers, and
the one breakout project is agent-native by design — DeepTutor ships multi-step
agent pipelines (`Deep Solve`, `Deep Research`) rather than a chat wrapper.

## 3. Purpose-built beats general-purpose (high confidence — incl. an OECD mandate)

The **OECD's 2026 Digital Education Outlook recommends moving toward
purpose-built educational AI rather than general-purpose tools.** Teachbetter
independently calls the move away from generic AI tools toward platforms
purpose-built for education "the defining trend." HolonIQ's framing — **proven
instructional benefit over broad personalisation promises** — is the same trend
stated as an evidentiary bar.

**Why it matters:** this is an explicit institutional mandate against "we
connected ChatGPT to it," and it is the clearest validation of vertical,
integrator-delivered work in the whole research set.

## 4. The compliance calendar and the capability calendar have come apart (high confidence)

A genuine counter-trend, and the detail most likely to be gotten wrong:

| Regime | Status on 2026-10-31 |
| --- | --- |
| EU AI Act — stand-alone Annex III high-risk (incl. education) | Deferred to **2027-12-02** by the Digital Omnibus amendment, in effect late July 2026 |
| EU AI Act — AI embedded in regulated products | Deferred to **2028-08-02** |
| EU — AI-generated intimate imagery / abuse material ban | Coming into force **December 2026** |
| South Korea AI Basic Act | **In force 2026-01-22**; enforcement decrees pending, guidance-first grace period through 2026 |
| Vietnam AI law | **Effective 2026-03-01**; high-risk designation covers education incl. automated assessment, reaching systems live before 2026-08-15 |
| Australia (TEQSA) | Institutional generative-AI action plans required of **all** higher-ed providers |

**Widely-repeated error to avoid:** guidance still in circulation says EU
high-risk obligations apply from **August 2026**. That was superseded by the
Digital Omnibus. Capability deadlines in Asia now land *before* Europe's.

## 5. Adoption is ahead of governance, and it is measured (high confidence in LATAM, medium elsewhere)

- **LATAM, strongest evidence:** UNESCO IESALC / UNU-IAS, 200 institutions in 19
  countries — **87% use AI in at least one area; 26% have a formal AI strategy.**
  Adoption is driven by individual academics and students, not institutions.
- **North America:** 60% of US teachers use AI tools (Gallup), while most US
  public schools lack formal student AI policies (Child Trends / US Dept. of
  Education). 30 states had issued guidance as of January 2026.
- **Higher ed, Europe + North America:** ~70% of institutions have or are
  developing guidance — the furthest-along segment.

The gap is the market. It is also a risk the client already owns, which makes it
an easier conversation than a net-new capability pitch.

## 6. Credentials and skills-based models (medium confidence — single source)

1EdTech points to the long-anticipated rise of **digital credentials and digital
competencies**, with employer expectations accelerating a skills-driven model.
Only one source in this run raised it, so it is logged as a watch item rather
than an established trend. It is worth watching because it is interoperability
work, which is where the permissive licences are.

## Licence-structure trend (measured first-hand this run, not reported)

Not a press trend — an observation from verifying 25 repositories on
2026-10-31, and it has been stable across this KB's history:

**The AI layer is being built permissively on top of a copyleft substrate.**
5 of 6 education agents are MIT (1 Apache-2.0). Every platform of record is
GPL/AGPL. Every standard integration boundary — LTI 1.3, xAPI, LRS, MCP — is
Apache-2.0 or MIT. The ecosystem is, in effect, standardising on
attach-don't-fork. Design accordingly; see
[`../compose/patterns.md`](../compose/patterns.md).

**One correction this run:** H5P was recorded as MIT in earlier passes of this
KB. It is **GPL-3.0**. Verified on the repository page.

## Declared gaps

- **Most trend sources are vendor blogs or market-research summaries**, not
  independent studies. The OECD, UNESCO, 1EdTech and named statutes are the
  load-bearing citations; vendor percentages were excluded where unverifiable.
- **No African or Canadian trend evidence** surfaced this run.
- **No education-specific LATAM regulatory trend** was found — only general AI
  policy across 23 countries.
