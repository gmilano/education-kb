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

**Upgraded on the second pass of 2026-10-31 — now the best-evidenced trend in
this KB.** The first pass rested on an OECD recommendation plus a vendor blog.
The **Sanoma Learning European Teacher Survey 2026** asked **20,000+ teachers
across 14 European countries** and its headline is literally that teachers are
adopting AI rapidly *but want tools built for education*. That is the same claim
measured on the largest sample anywhere in this research, from the demand side
rather than as a policy recommendation. The OECD's June 2026 *Empowering
Learners for the Age of AI* is a second OECD publication pointing the same way.

So the trend now has three independent legs: an **institutional mandate**
(OECD), **20,000 teachers** saying it themselves (Sanoma), and an
**evidentiary bar** (HolonIQ's "proven instructional benefit"). It is no longer
a soft trend.

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
- **EMEA, added second pass — and the gap here is *training*, not policy:**
  **63%** of EU teachers use AI at least partly for explanations or practice
  (European Commission School Education Gateway survey, Apr 2026, n=1,130;
  corroborated at 63% by Sanoma across 20,000+ teachers), while only **~30%**
  have had AI training and only **~1/3** of national curricula include AI
  competences. In the UK, **49%** of schools have no AI policy for staff or
  students (NEU). One counter-signal worth noting: **41% of EU teachers do not
  use AI for grading or summative assessment at all** — the one place adoption
  has *not* run ahead, and it happens to be the Annex III high-risk boundary.
- **EMEA/Africa, added second pass — the sharpest deficit in the entire KB:**
  only **14%** of higher-education respondents confirm an institutional AI
  policy, **17%** say there is none, and **69% do not know** (Frontiers in
  Education, 2026). "Don't know" is worse than "none": it means the policy
  question has not reached the people using the tools.
- **Canada, added second pass — a genuine outlier.** Quebec issued a **March
  2025 directive suspending the use of AI assistants**: the only jurisdiction in
  this research where governance moved *ahead* of adoption by withdrawing it.
  Ontario, by contrast, has no ministry memorandum and **42.3%** board coverage.

The gap is the market. It is also a risk the client already owns, which makes it
an easier conversation than a net-new capability pitch.

**Ranked by severity, the governance deficit now reads:** Africa (14% confirmed,
69% unaware) → LATAM (87% use, 26% strategy) → UK (49% no policy) → Ontario
(42.3% board coverage) → EU (policy maturing, training at ~30%) → Quebec
(suspended, i.e. governed by prohibition). That ordering is a territory-
prioritisation input, and it did not exist before this pass.

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

## Licence hygiene: the sidebar is not the licence (measured second pass, 2026-10-31)

A method finding, and it changes how this KB should be maintained. The first
pass read licences off repository **sidebars**; the second pass fetched the
licence **files**. Four of six repos checked that way came back different from
what the sidebar implied:

| Repo | Sidebar said | The file says |
| --- | --- | --- |
| `odoo/odoo` | *no licence named* | **LGPL-3.0** (`LICENSE`, branch `20.0`) |
| `frappe/education` | *no licence named* | **GPL-3.0** (`license.txt`) |
| `OS4ED/openSIS-Classic` | *no licence named*; README says "GPL" | **GPL-2.0** specifically (`docs/License.txt`) |
| `DMontgomery40/mcp-canvas-lms` | *no licence named*; README says "MIT — see LICENSE file" | **no licence file exists** — 404 on six filename variants across both branches |

**Three distinct conditions look identical in a sidebar**: the licence is
present but unparsed by GitHub (Odoo, Frappe), the licence is present but a
different *version* than claimed (openSIS — GPL-2.0 has no patent grant and is
incompatible with GPL-3.0-only code), or **there is no grant at all**
(mcp-canvas-lms). The last is a procurement blocker, not a formatting detail:
without a licence file the default is exclusive copyright, whatever the README
says.

**Standing rule for this KB:** a licence recorded for a repo Globant would build
on must come from the licence file, with the branch and path noted. Sidebar-only
licences are a claim, not a verification. Version numbers matter as much as
family names.

**Counter-note — the structural claim survived the stricter method.** Every
correction above moved a repo *within* copyleft or into unresolved; none moved a
platform of record into permissive. The one genuine permissive discovery,
`DSpace/DSpace` (**BSD-3-Clause**), was found by checking a category the first
pass had not looked at, and it narrows the "no permissive substrate" claim to
the LMS category rather than overturning it.

## Declared gaps

- **Most trend sources are vendor blogs or market-research summaries**, not
  independent studies. The OECD, UNESCO, 1EdTech, the **European Commission /
  Eurydice** reports of 2026-09-22 and named statutes are the load-bearing
  citations; vendor percentages were excluded where unverifiable.
- ~~**No African or Canadian trend evidence.**~~ **Closed on the second pass of
  2026-10-31** — both are now in trend 5 and in
  [`market.md`](market.md). African evidence is one peer-reviewed study plus
  analysis pieces; Canadian evidence is provincial documents plus one think-tank
  survey. Thinner than the EU material, so weighted accordingly.
- ~~**No education-specific LATAM regulatory trend.**~~ **Closed, and the trend
  is that there barely is one:** Peru's Ley 31814 + DS 115-2025-PCM is the
  region's only binding instrument naming education, Chile's MINEDUC document is
  guidance, Brazil's PL 2338 is contested. The Universidad de los Andes /
  Konrad Adenauer study (Aug 2026) frames the regional pattern as volume without
  quality — *legislar rápido no es legislar bien*.
- **Still open — APAC is now the weakest-evidenced region**, resting on
  market-research vendor outputs with no primary survey behind them. The EMEA
  closure this pass overtook it. Priority for the next pass.
- **Trend 6 (credentials) is still single-source** and unchanged; no second
  source surfaced on this pass, so it stays a watch item rather than a trend.
