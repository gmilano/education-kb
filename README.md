---
industry: education
region: Global
updated: 2026-11-18
---

# Globant AI Studios — Education KB

Curated, verified starting points for an education engagement: the open-source platforms a
client already runs, the AI agents worth composing, the regulation that constrains the build,
and concrete recipes that name specific repos.

## Start here

| If you need… | Read |
|---|---|
| An AI agent to adopt or customise | [`agents/top.md`](agents/top.md) |
| What changed recently | [`agents/trending.md`](agents/trending.md) · [`repos/trending.md`](repos/trending.md) |
| The substrate to build on | [`repos/foundations.md`](repos/foundations.md) |
| A platform the client may already run | [`verticals/solutions.md`](verticals/solutions.md) |
| Market sizing and regional opportunity | [`intel/market.md`](intel/market.md) |
| Where the industry is heading | [`intel/trends.md`](intel/trends.md) |
| A concrete build recipe | [`compose/patterns.md`](compose/patterns.md) |

## The four facts that shape every education engagement

1. **The platforms are copyleft; the tooling is permissive.** Moodle (GPL-3.0), Open edX
   (AGPL-3.0) and Canvas (AGPL-3.0) are what clients run. Integrate over **LTI 1.3** or **MCP**
   and your tool stays a separate work; fork the platform and it does not. When a client needs a
   proprietary derivative, start from **Artemis (MIT)**, **Kolibri (MIT)**, **Oppia (Apache-2.0)**
   or **OpenOLAT (Apache-2.0)**. **Content assets invert this** (added p890): curriculum data and
   learning-content apps arrive under data or copyleft licences — `os-taxonomy` is **ODbL-1.0**
   with share-alike on derived databases. Run licence triage per artefact class, not once.
   **There is now one real exception to the copyleft rule** (added p893): **Mentingo
   (MIT, 109 ★)** is a self-hosted *AI-native* LMS — the shortest route to a closed, branded
   learning product. It is corporate L&D only: no gradebook of record, no SIS, no accreditation
   story. **And a second seam opened**: Moodle now has seven community MCP servers, with
   read-only and read-write split across two separately maintained MIT projects. MCP exposes the
   LMS to your agent the way LTI ships your tool into the LMS — use both (`compose/patterns.md`
   P11).

2. **The best open education agents are academic, not commercial — with one loud new
   exception.** DeepTutor (HKU, Apache-2.0, **60,258 ★**), OpenMAIC (Tsinghua, MIT,
   **43,874 ★**), the Artemis/EduTelligence/Pyris stack (TU Munich, MIT), OATutor (UC Berkeley,
   MIT). The commercial tutors are closed. These projects want implementation partners — which
   is the opening. **The exception, added p893: LearnHarness (AGPL-3.0, 10,002 ★)** went from
   creation on 16 October 2026 to third-largest open education agent in the world in 27 days,
   and is the first to grow a **third-party plugin ecosystem** — five independent extensions,
   an Android reimplementation and an awesome-list. AGPL, so it cannot enter a closed
   derivative; read it as the reference design for learner-state modelling, which almost every
   permissive tutor lacks. **No published learning-outcome study.** See `intel/trends.md` T12.

3. **Regulation now constrains *use*, not existence, and the rules differ by region.**
   Oklahoma bars AI-only grading. **California AB 1159 bars training models on student data at
   all** — which forecloses an architecture, not just a workflow. The EU postponed high-risk
   education obligations to **2 December 2027** (Regulation (EU) 2026/1744) while Article 50
   disclosure already applies and the **Article 4 AI-literacy duty has been live since
   2 February 2025** for every organisation using any AI. Korea's AI Basic Act is in force.
   India and China require AI-content labelling on dated schedules. **Auditable human oversight
   is the product.** See `intel/market.md`.

   **The nearest deadlines are closer than 2027** (added p890): **North Carolina** needs a state
   model AI policy by **31 December 2026** and local policies by **30 June 2027**, and
   **Vietnam** has made education AI *statutorily* high-risk — new systems comply by
   **1 March 2027**, existing ones by **1 September 2027**, both ahead of the EU date.

4. **Adoption has outrun governance, and that is the fastest sale.** In Brazil 53% of school
   administrators use AI and 22% have guidelines; 87% of regional universities use AI and 26%
   have a strategy. **PISA 2025: across 13 LAC countries, nine in ten 15-year-olds have already
   used AI chatbots for schoolwork**, while CENIA finds 13 of 19 LAC countries do not teach AI in
   schools at all. The offer is governance for AI already in use, not adoption.

5. **Buyers have started writing the spec themselves** (added p890). Jisc, with Universities UK,
   GuildHE and the Association of Colleges, asked AI suppliers for transparent pricing, granular
   per-institution usage and cost controls, data portability and no lock-in — driven by
   usage-based pricing replacing per-seat licences. It is the closest thing to a published tender
   in this KB. `compose/patterns.md` **P8** answers it with named repos.

## How findings in this KB are verified

Two independent channels, both re-run 2026-11-18:

- **Existence and licence text** — `LICENSE`/`COPYING` fetched from
  `raw.githubusercontent.com` and the grant read as text.
- **Stars, SPDX licence, last push, archived** — `gh api search/repositories` with batched
  `repo:` qualifiers (a *single* `repo:` qualifier returns `422`; batches of ~8 work).

`github.com` HTML returns `403` through this environment's proxy and `api.github.com/repos/`
is session-scoped, so those are not used. 116 of 119 tracked repos resolved on both channels;
the three that did not are named in `agents/top.md`. Every table row has a real repo URL, a real
licence and a real description. Where a licence cannot be confirmed, the row says so instead of
guessing.

**Star counts and `last push` are both recorded, because stars alone mislead:**
`stanford-oval/storm` has 31,906 ★ and has not been pushed in 414 days.

**Stars are a daily metric, not an hourly one** (measured in p890): across ~30 tracked repos the
largest intra-day move was +21 stars on a 60,000-star repo.

**One channel was unavailable in pass p890 and it matters.** Every non-GitHub host is blocked by
this session's network policy (`403` on CONNECT, `getaddrinfo ENOTFOUND` via fetch), so the legal
and statistical facts in `intel/market.md` and `intel/trends.md` are **search-snippet evidence
with the source named and corroboration stated**, not byte-read primary text. GitHub facts remain
byte-verified. The affected hosts are listed under *Declared gaps* in `intel/market.md`.

## What this KB does not cover

- **No education agent originates from LATAM, India, Africa or the Middle East** (sharpened
  p892). Only `warleysr/ankipa` (10 ★, Brazil) in LATAM, and four dedicated regional legs across
  p891–p892 produced rich national-programme evidence and **zero repositories**. Open education
  agents come from East-Asian and European universities; every other region localises them.
  That is the shape of the localisation market, not a hole in the research.
- **Africa and the Middle East are covered thinly, not absently** (updated p892). Dedicated
  legs ran in p891 (Africa, UAE/Dubai) and p892 (**Saudi Arabia**). Both regions file under
  **EMEA** because the region vocabulary is closed to five values; the country is in the prose.
  Primary government sources in both regions are blocked by this session's network policy, so
  the evidence is corroborated secondary reporting, labelled as such.
- **Canada has its own subsection as of p891**, and it is the clearest evidence for T10: no
  national rule, formal educator guidance in four provinces only, and a higher-education sector
  that has broadly refused AI-detection tooling on privacy grounds.
- **No open agent for student information systems, admissions, financial aid or proctoring.**
  The largest build-vs-adopt gap in the industry — and the most defensible studio IP, with the
  caveat that several of these are EU Annex III high-risk categories.
- **No credible primary evidence of learning-outcome gains from AI at scale.** The widely
  quoted figures trace to blogs with no primary study. `compose/patterns.md` P7 exists to
  measure it rather than claim it.

## Note on this revision

The eight content files had accumulated a large volume of self-referential pass-over-pass
commentary — roughly 800 KB across six files, much of it about the curation process rather than
the industry. Those versions are preserved verbatim in
[`archive/2026-11-18-pre-cleanup/`](archive/2026-11-18-pre-cleanup/) and the files were rewritten
as a reference a studio team can use. `agents/trending.md` and `repos/trending.md` are
append-only and retain their full history below the newest dated section.

One substantive error was corrected: **`openedx/openedx-platform` does not exist** (404 on every
branch) and had propagated through four files. The real slug is `openedx/edx-platform`.

### Pass p892 (same day, latest)

Research-led; no file rewritten. Spent the budget on the two gaps `intel/market.md` itself named
highest-value, and closed both:

- **India** — first coverage in any pass. NCERT/CBSE Computational Thinking and AI curriculum for
  **Classes III–VIII from 2026–27**, a 15-hour SOAR module already in 18,000+ CBSE schools, and
  **no education-specific AI statute**: the compliance surface is IT-Rules content labelling, not
  system conformity. **India is a delivery-capacity market, not a conformity market.**
- **Saudi Arabia** — p891 called its silence a search-reach failure rather than an absence, and
  that was right. AI units in public education since 2025–26, **50 further units across 22
  revised subjects for 2026–27**, MoE/SDAIA ethics guidance, and **240,000 teachers in training**.

Those two legs produced the pass's one structural addition, **T11**: AI literacy is becoming a
statutory *curriculum* mandate across India, Saudi Arabia, Vietnam, the UAE, North Carolina and
the AU strategy, and in every case the binding constraint is teacher capacity rather than
technology. **P10** answers it with named repos, written once for both markets.

Also: two agents added (`tutor-mcp`, MIT, 104 ★; `EduAgent`, MIT, 93 ★, age-banded by design);
one method correction — the "tutor as a skill" cohort was declared flat in two passes while a
104 ★ actively-developed member was **missing from the set being measured**, so re-enumerate
before re-measuring; and one rejected platform — `projectfedena/fedena` (547 ★) is listed as
Apache-2.0 by comparison tables but has **no licence file at all** and has been idle since 2020.
That is the second aggregator-sourced licence error caught in two passes, both by byte-reading.

### Pass p890 (same day, later)

Research-led rather than structural. Four regional legs plus four global legs; no file was
rewritten. Added: **T9** (procurement economics — the Jisc buyer-side specification) and **P8**
(per-institution metering, cost attribution and exit). Filled three regional holes — **Vietnam**
(education is statutory high-risk, with deadlines ahead of the EU's), **Australia** (TEQSA now
regulatory-led) and the start of **Canada**. Closed two declared gaps with answers rather than
silence: **Japan has no education-specific AI regime** (confirmed absence) and **star counts are
measurable** (that gap line was stale). Two licence-class corrections: `os-taxonomy` is
**ODbL-1.0**, a database licence with share-alike, and `langfuse` is a **split licence now owned
by ClickHouse, Inc.** Resolved the previous pass's own open question: the "tutor as an agent
skill" cohort tops out at **118 ★** and gained nothing, so the form stays in the demo kit and off
the roadmap.
