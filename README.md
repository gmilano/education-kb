---
industry: education
region: Global
updated: 2026-11-19
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

**A third probe axis was added in `p904`:** when a repository's payload is data, the licence of the
asset can live inside the payload directory (`dados/LICENSE.md`), which a root-only probe reports
wrongly rather than not at all. See gate `904-G1` in `compose/patterns.md`.

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

- 🔴 **The "no education agent originates from LATAM" bullet that stood here was wrong, and `p904`
  retracted it — it was an artefact of searching only in English.** No pass before `p904` had run a
  Spanish- or Portuguese-language repository search. 26 such queries, including LATAM national
  examination names, produced **six LATAM-origin agents in `agents/top.md`** (up from one), a
  **five-repository Brazilian national-curriculum cluster** in `repos/foundations.md` and two AGPL
  platforms in `verticals/solutions.md`, every licence byte-read. 🟢 **The corrected claim is more
  useful: LATAM open source builds against the two artefacts every school in a country shares — the
  national examination and the national curriculum** (ENEM essay grading and mock exams, Saber 11
  prompt generation, and the BNCC published as verified open data with a Zenodo DOI). What LATAM does
  *not* produce is the general-purpose tutor, which tops out at **6 ★ and unlicensed**. So the
  localisation advice inverts: **bring the tutor, adopt the curriculum spine** (`compose/patterns.md`
  **P23**). 🟡 The gap moved rather than closed — **Spanish-speaking LATAM outside Colombia** is still
  nearly empty, and **Mexico returned a 0 ★ ceiling and no repository in any of the 26 queries.**
  🟢 **`p927` strengthened this and retired `926-G2`'s harder version of it.** `p926` measured
  eleven Spanish- and Portuguese-language rows, found **none** permissively licensed, and published
  *"the default licence state is no licence at all"* as a fact about the region. A second search
  vocabulary byte-read **MIT** on `uemanet/harpia` — the academic system of **Universidade Estadual
  do Maranhão**, open since 2017 — plus `DerickxP/Learn-Quest-Serious-Game`,
  `alberto2005-coder/detector-ia` and `Gehiner/KodlandFaster`. **LATAM permissive supply exists and
  it is institutional**: registrarial spines and integrity tooling, not tutors. That is the same
  instrument failure as `926-R1`, one level up — a claim about a leg list published as a claim
  about a region.
  India, Africa and the Middle East remain as `p892`–`p903` recorded them, with MENA producing
  individuals rather than institutions.
- **Africa and the Middle East are covered thinly, not absently** (updated p892). Dedicated
  legs ran in p891 (Africa, UAE/Dubai) and p892 (**Saudi Arabia**). Both regions file under
  **EMEA** because the region vocabulary is closed to five values; the country is in the prose.
  Primary government sources in both regions are blocked by this session's network policy, so
  the evidence is corroborated secondary reporting, labelled as such.
- **Canada has its own subsection as of p891**, and it is the clearest evidence for T10: no
  national rule, formal educator guidance in four provinces only, and a higher-education sector
  that has broadly refused AI-detection tooling on privacy grounds.
- **No open *agent* for student information systems, admissions, financial aid or proctoring.**
  The largest build-vs-adopt gap in the industry — and the most defensible studio IP, with the
  caveat that several of these are EU Annex III high-risk categories. **Two qualifications
  added p896.** (1) The *integration* layer is not missing: `UniversityOfHelsinkiCS` publishes
  SIS import, credit-registration and namespace tooling under MIT/Apache, restored to
  `repos/foundations.md`. (2) Proctoring is not an empty category but an **unadoptable** one —
  six open tools, the largest at 16 ★ and dormant since 2025, against an EU prohibition on
  emotion inference that has been in force since 2 February 2025. 🟢 **Qualified in `p927`: the
  category is still unadoptable, but the architecture is no longer the problem.**
  `topic:proctoring` — 176 repositories, never asked before `p927` — returns three MIT rows built
  **local-first and in-browser**: `tinyproctorjs` infers **no affect at all**, and
  `Local-Exam-Proctoring-Engine` keeps **every frame on the candidate's device**. The prohibition
  is on emotion inference, not on video. So proctoring moves from *"do not propose this"* to **a
  scoped build with three reference designs and a stated compliance boundary** — while remaining
  Annex III high-risk, which no architecture changes. See `intel/trends.md` **T64**,
  `compose/patterns.md` **P55** and `verticals/solutions.md`.
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

One substantive error was reported corrected — and `p896` found the correction itself was the
error. See *Pass p896* below.

### Pass p927 (2026-11-19, latest)

**One job: take `926-R1` seriously.** `p926` had opened thirteen topic words `p925` never asked,
returned **601 unheld repositories**, and written the rule — *a discovery channel is exhausted only
against the vocabulary it was asked with* — then added: *the next pass should assume the same of
this leg list.* `p927` asked **35 more words**.

- 🔴 **2,298 unheld repositories**, deduplicated against the **8,432** slugs this base has ever
  named — **3.8× `p926`'s own record**, from the channel `p926` had just measured. **36 grants
  byte-read, 36 of 36 resolved, zero 404s. 34 rows shelved.**
- 🔴 **And the number is a floor, not a measurement.** Fifteen of the 35 legs reported a
  `total_count` larger than the 100-row page this base fetches — `topic:student-management`
  **1,651**, `topic:ai-tutor` **986**, `topic:study-tools` **817**. 🔵 **Every sentence this base
  has written about what the topic channel contains has been a sentence about a 100-row page.**
  `p928`'s first job is to paginate.
- 🔴 **A published row is materially qualified, and it opens a fifth licence axis (`T63`).**
  `CAHLR/OATutor` (MIT, UC Berkeley) is carried as an ITS *"with open problem banks"*. The problem
  banks are a **separate repository** — `CAHLR/OATutor-Content` — with **no licence file on 14
  probed paths** and SPDX `NONE` on the search channel, so **both channels agree and no divergence
  check fires**. The grant is **prose in the README** (CC BY 4.0), with attribution recorded **per
  JSON record**. New gate **`927-G1`**: probe the payload *repository*, and read the README when
  there is no licence file.
- 🔴 **`926-G2`'s LATAM conclusion did not survive a second vocabulary.** That pass measured eleven
  Spanish- and Portuguese-language rows, found none permissive, and published it as a fact about the
  region. `p927` byte-read **MIT grants** on `uemanet/harpia` (the academic system of a **Brazilian
  state university**, open since 2017), `DerickxP/Learn-Quest-Serious-Game`,
  `alberto2005-coder/detector-ia` and `Gehiner/KodlandFaster`. 🟢 **The corrected claim is sharper:**
  LATAM permissive supply is **institutional** — registrarial spines, integrity tooling — and not
  general-purpose tutors, where `p904` measured a 6 ★ ceiling. *Bring the tutor, adopt the
  institutional spine.*
- 🟢 **Three tiers this base had no row for at all**: **SCORM** authoring and packaging
  (`scorm-kit` + `storycraft`, both MIT, identical grant hash) — the one delivery form indifferent
  to which LMS the client runs, and the basis of new pattern **P54**; **non-blockchain
  credentialing** under **W3C Verifiable Credentials 2.0** (`sanad`, Apache-2.0) and Open Badges
  (`open-badges-bundle`, MIT) — **T65**; and **H5P with no H5P server** (`h5p-toolkit`, MIT).
- 🟢 **`T17` found in production.** `artevelde-uas/canvas-lms-app` (**ISC**, maintained by a Belgian
  university since 2018) is a permissively licensed branding layer on an **AGPL** LMS — the
  architecture `T17` was inferred from licence sorting, now a row that has been running for eight
  years.
- 🟢 **First `0BSD` row** (`xxinjie21/Smart-Quiz-Tutor`) — public-domain-equivalent, no attribution
  requirement at all. New country origins: **Azerbaijan**, **Bulgaria**, **Japan**.
- 🔵 **Regional legs returned 0 repositories and real intel**, now in `intel/market.md`: only **6%
  of teachers say their school's AI policy is clear** (Stanford AI Index 2026) while half of schools
  have none — **T67**, the operable-policy gap; **APAC virtual-tutor adoption at 30%** against
  80-percent-plus general AI use, with **connectivity** the stated barrier — **T66**, which makes
  offline-first the APAC lead; LATAM at **92% student use / 30% of universities with a published
  policy**; and the **IDB's 193-solution map** of AI already running in LATAM classrooms.
- 🔴 **One claim corrected before publication, recorded because the near-miss is the lesson.**
  `jonsorr/D2L_Brightspace_APIs` was first written up as the *first Brightspace row in this base*.
  It is not — `p914` closed that seam. 🔵 **The slug was unheld, so every mechanical gate passed it,
  and "unheld slug" is not "uncovered category".** `927-R3`: before writing *first*, grep the tree
  for the **platform name**, not the repository address.
- 🔵 **Honest nulls:** four mandated prose legs **nil for the forty-sixth consecutive pass**; the
  vertical leg returned the **OpenEduCat marketing site for the fourth consecutive pass** and should
  not be re-run as written; `T18`'s APAC direction is **contradicted** by this pass's Ipsos summary
  and both readings are snippet-level, so **neither belongs in a client deck** until the tables are
  read directly.

Append-only discipline preserved: `agents/trending.md` 93,286 → 93,562 lines,
`repos/trending.md` 71,054 → 71,149; history untouched below.

### Pass p904 (2026-11-18)

**One job: run the discovery channel no pass had ever run.** `p903` established that generic English
search is now a confirmation channel and that what still yields is byte-reading and **non-English
repository search**, and it named Urdu and Indonesian as the untried channels. `p904` ran
**Spanish and Portuguese** instead — because the oldest unfalsified claim in this tree was that LATAM
produces almost no open education software — with the `p903` exam-name trick applied to LATAM
national examinations. **The claim did not survive.**

- 🔴 **The LATAM supply finding this KB had carried since its first pass was an artefact of language,
  not a measurement.** 26 queries returned six LATAM-origin agents (now shelved, up from one,
  including the **first Colombia-origin row**), a five-repository Brazilian curriculum cluster and
  two AGPL platforms. The corrected claim is sharper and sells better: **LATAM builds against the
  national examination and the national curriculum**, and does not build general-purpose tutors.
- 🟢 **The find of the pass: `bncc-dev`.** Brazil's Base Nacional Comum Curricular as **1,721 verified
  records** with per-record provenance, character-by-character verification against the official MEC
  PDF, a reproducible pipeline in CI, a **Zenodo DOI**, an `llms.txt` agent data contract, npm/PyPI
  packages, **two independently maintained MCP servers**, and an **open LLM-hallucination benchmark**
  publishing 17,100 raw responses across 19 models. `p903` found Egypt's curriculum published the same
  way with **no licence at all**; Brazil's has a dual grant. **Same structural shift (`T26`), opposite
  rigour** — so the form is not inherently a licence trap, it is one when nobody does the work.
- 🔴 **And it had been logged in this KB between 12 and 40 times without ever being shelved.** Four
  repositories, up to 26 ★, MIT and CC BY, appearing in `agents/trending.md` and `repos/trending.md`
  for passes, with **one** mention anywhere in the six files an engagement opens. `p899`'s finding
  recurring: **discovery was never the bottleneck, promotion was.**
- 🔴 **A gate failure in this KB's own instrument, found and fixed.** `bncc-dados` reports SPDX `MIT`
  and byte-reads MIT **at its root** — and the dataset a studio actually consumes is **CC BY 4.0**,
  licensed at `dados/LICENSE.md`, a path the 12-path root probe never looks at. New gate **`904-G1`**:
  when the payload is data or content, probe the payload directory and the split-licence index names
  before recording any SPDX value. Three `NOASSERTION` rows in the same cluster are the same failure
  from the other side — their root `LICENSE` is a **Portuguese-language index to two other licence
  files**.
- 🟢 **A third licence axis, new to this KB: the mark.** `bncc-pacotes` grants MIT code and CC BY data
  and **withholds the project name and visual identity** — *"the code is free; the mark is not"*. No
  SPDX field, scanner or SBOM can express it, and it surfaces at launch rather than at architecture
  review. Written up as **T27**.
- 🟢 **New pattern `P23`** — curriculum-grounded tutor with a **two-metric hallucination gate** as the
  acceptance test, built on the cluster above, 7–11 weeks, and cheaper than `P22` by design because
  the corpus already exists. The benchmark it uses is a **vendor benchmark**, so the pattern says to
  **re-run it, not cite it**.
- 🟡 **Method: a fourth way an existence check can lie.** `SirhanMacx/LearnHarness` is dead on **both**
  channels; the project was **transferred** to `amosblomqvist/learnharness` (10,194 ★). A transfer
  leaves nothing at the old address, so `p896`'s rename-alias signature (raw `200` + `repo:` 0 hits)
  cannot detect it. No row in this KB was broken — the canonical address was already carried.
- **Honest nulls, recorded:** third consecutive null yield from the four generic legs (all three
  candidates already in-tree); **no Mexico-origin education repository in any of 26 queries**
  (`EXANI examen` ceiling **0 ★**); nothing from Argentina, Peru or Central America; no `bncc-dev`
  equivalent for any other national curriculum; `DigComp 3.0` still unreadable behind the egress
  proxy for a second pass.

### Pass p896 (2026-11-18)

**One job: the shelf-vs-history slug diff that `p895` recommended.** `p894` and `p895` had each
found a single row deleted by a rewrite. The diff finds **93**, and **all 93 are live
repositories** — zero 404s.

- 🟢 **38 of the 93 sit at ≥ 10 ★ and are not covered by the cleanup's stated rationale.** That
  rationale — removing single-author student projects — is sound and accounts for the 47 rows at
  0–2 ★, which stay out. The rest is institution-maintained plumbing: `cmu-db/bustub` (5,171 ★),
  `moodlehq/moodleapp` (1,007 ★), `apereo/java-cas-client` (949 ★), `instructure/instructure-ui`
  (487 ★), `openedx/XBlock` (471 ★), `oppia/oppia-android` (422 ★), the TUM Artemis clients, the
  Helsinki SIS tooling, the UCT Sakai estate. **The deletion was biased by form**: what looks
  like a product survived, what looks like plumbing did not — and plumbing is most of what an
  education engagement touches. **52 rows restored** across the three shelves.
- 🟢 **The restoration produced a new structural finding (`T17`), not just rows.** Sorting the
  restored set by licence shows the copyleft platforms publish their **extension points, design
  systems, mobile clients and analytics tiers under Apache-2.0 or MIT**. A branded closed client
  over a client's AGPL LMS is a supported architecture, not a workaround. `compose/patterns.md`
  **P15** builds it.
- 🔴 **`openedx/openedx-platform` exists and is the canonical slug; the p895 correction ran
  backwards.** Measured: `repo:openedx/openedx-platform` → **8,242 ★, AGPL-3.0, pushed
  2026-11-17**; `repo:openedx/edx-platform` → **nothing**. Both serve byte-identical files on
  raw. The "404 on every branch" is reproducible only against **`main`**, and this repo's default
  branch is **`master`**.
- 🟢 **A reusable gate came out of it.** `raw.githubusercontent.com` follows rename redirects;
  the search API's `repo:` qualifier does not — so a slug that 200s on raw and returns 0 hits
  from `repo:` is a **rename alias**. Run over all 172 live slugs it returns exactly three, all
  recorded backwards in this KB: `openedx/edx-platform`, `All-Hands-AI/OpenHands`
  (canonical **`OpenHands/OpenHands`**, **93,731 ★**) and `danny-avila/LibreChat` (canonical
  **`LibreChat-AI/LibreChat`**, **47,317 ★**). Two star counts carried as *unavailable* for
  several passes were recovered this way.
- 🔴 **Two licence byte-reads correct the SPDX field toward *stronger* copyleft.**
  `portabilis/i-diario` (117 ★, Brazil) reports `NOASSERTION` and is **AGPL-3.0** — its licence
  file is the Affero GPL **in Portuguese translation**, which SPDX template-matching cannot
  recognise. `8infinitelabs/eucompliance` is **EUPL-1.2**, same failure. **A `NOASSERTION` on a
  non-English repo is a prompt to read the file, not evidence that it is unlicensed.**
- 🟢 **Regional research ran on all four regions** and added `T18`: China launched a **global AI
  education service platform** (Hangzhou, May 2026) reaching ~220 countries, while Ipsos finds
  support for *banning* AI in education **rising** across APAC (Australia now a majority at 52%).
  Also new: the **EU–OECD AI Literacy Framework** (18 June 2026, four domains, 19 competences),
  Ohio's promised **state model policy by end-2026**, and **UNESCO's AI-in-Education Observatory
  for Latin America and the Caribbean**.
- 🟡 **Method fix:** this KB's 8-path licence probe misses `main/COPYING.txt` and
  `master/LICENSE.TXT`; extended to twelve paths.

Append-only discipline preserved: `agents/trending.md` 87,095 → 87,162 lines,
`repos/trending.md` 68,371 → 68,518; history untouched below.

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
