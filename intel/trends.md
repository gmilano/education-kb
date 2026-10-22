---
industry: education
region: Global
updated: 2026-10-22
---

# Education industry trends

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/intel-trends.md`](../archive/2026-10-22-p383-pre-rewrite/intel-trends.md).

> The previous version's headline trends were about **what this knowledge base could see** —
> channel yield, address supply, star thresholds. Those are facts about a scraper, not about
> education. They are preserved in the archive and in
> [`agents/trending.md`](../agents/trending.md); this shelf is now about the industry.


## 🆕 `p390` — note on what was removed from this shelf

Two `p387` sections that stood here (*"Date the artefact, not the repository"* and *"The LATAM
supply gap was a reading gap too"*) were **measurement-apparatus notes, not industry trends** —
exactly what `p383`'s rewrite note above says this shelf is not for. They are preserved verbatim in
[`archive/2026-10-22-p390-pre-trim/intel-trends.md`](../archive/2026-10-22-p390-pre-trim/intel-trends.md)
and their durable content lives where it belongs: the dating method in
[`agents/top.md`](../agents/top.md) under *How these rows were verified*, and the LATAM supply in
`Tier 4` of that same shelf. Nothing was lost; it was filed.

## 🆕 `p386` — The LMS-integration gap is not a licence gap any more. It is a **tenancy** gap.

For four passes this base recorded Blackboard and D2L as the two platforms where
*"a permissively-licensed MCP server would be a genuine contribution."* `p386` probed all fifteen
addresses first-hand: **6 MIT grants on Blackboard, 6 on D2L, 1 ungranted, 2 dead.** The licences
were there the whole time; nobody had read them.

🔵 **What replaced the gap is a sharper and more useful trend.** Eleven of the twelve granted
servers authenticate **as the signed-in student** — the learner's own browser SSO/MFA session or
session cookies, no admin API key, read-only because nothing else is possible from that position.
They are built by students, for themselves, at their own university, and several hard-code it.

That makes the 2026 community LMS-MCP supply a **personal-tooling** supply, and it does not become
an institutional one by being licensed well:

| what an institution needs | what a session-scraping server has |
|---|---|
| tenant identity, per-role scope | the rights of whoever signed in |
| an audit trail of every agent action | nothing, or stdout |
| a stable contract against the vendor's API | a login page that changes without notice |
| a data-protection answer for a DPO | the student's session cookie in a config file |

🟢 **Exactly one address read as institution-grade** — [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
(MIT): official REST API, OAuth2, role gate, FERPA handling, PII scrub, JSON audit log, Prometheus
metrics, grade write-back (maintainer self-claims, read not executed). **One in twelve.**

🔵 **The consequence for a studio, and it is a sellable one.** The scarce artefact in LMS
integration is no longer a permissive server — it is a **hardened** one. The work is: take a granted
community server, put tenant auth, role scoping, rate limiting and an audit trail around it, and
pin it to the vendor's documented API rather than its login page. That is a small, well-bounded
engagement with a deliverable the client can show their data-protection officer, and it is
available on **every** major LMS as of this pass. 🔴 On D2L it is still partly greenfield: all six
granted Brightspace servers are student-side.

🔴 **And the methodological trend underneath it, because it will recur in every industry in this
rotation:** a census that counts **addresses** and a census that counts **grants** are different
measurements, and the first one silently masquerades as the second. *"Nine servers and not one
verified grant"* described this base's own reading, not the world — the honest word for a count of
zero reads is **unread**, never **ungranted**.

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
- 🔴 **UNCONFIRMED:** a reported **New York City moratorium** on student-facing generative AI
  (EdWeek; date metadata inconsistent). If it holds, the largest US district has gone the other way.

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

🔴 **And the language asymmetry is the architecture constraint.** Node and PHP have maintained LTI
1.3; **Python does not**, and almost every agent on these shelves is Python. The interop edge is
therefore a **separate Node or PHP service** in front of the agent — not a library call inside it.
That is a deployment component a proposal has to cost, and it is recorded as `Gap 391-A`.

