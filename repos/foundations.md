---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

**Pass 320 · 2026-10-19 (sixth pass of this date). Twenty-one repos** — one added, and it is the
only substantive addition anywhere in this KB this pass. **`adamzammit/LTIPlugin` is the first
artefact this KB has found at the grade-passback seam that carries an OSI-approved licence**
(GPL-3.0) rather than no licence at all; read the row's caveats before scoping it, because it is
not an AI tool and probably not LTI 1.3. The method constraint was **re-tested rather than
inherited** this pass and reproduces exactly: github.com is the only reachable origin, and
`www.future-ed.org`, `www.lw.com` and `www.iesalc.unesco.org` each failed at DNS when attempted
directly.

**Pass 319 · 2026-10-19.** Twenty repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says which pass took the licence/star
reading.

**Pass 319 is the largest single addition this file has had, and the find of the pass is Brazilian.**
The `bncc-dev` stack — a character-verified machine-readable national curriculum, an MCP server over
it, and a benchmark that measures what grounding on it is worth — is the artefact every pattern in
this KB has assumed a client would supply. **It exists in exactly one country, it has 22 stars, and
it publishes the number: curriculum hallucination drops from 31.9% to 2.3% when the model queries
it.** Detail below the table.

The pass also closed the `pylti1.3` concentration risk with a real alternative
(`tsugiproject/tsugi`, 4,011 commits, from the author of the LTI specification), added the
institutional-grade **EMEA** autograder this file lacked (`thm-mni-ii/feedbacksystem`, 2,248
commits at 24 stars), and swept GitHub topics **in four languages other than English** — which is
how most of this was found. The method note at the end is the part worth copying.

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/openeduhub/oeh-metadata-vocabs | **CC0-1.0** | 2 | p321 | Curriculum / competency metadata (EMEA) | **938 commits, 7 forks, 5 watchers.** All SKOS vocabulary files for OpenEduHub / WirLernenOnline, as Turtle (`.ttl`) under the namespace `w3id.org/openeduhub/vocabs`, generated into a browsable view with SkoHub-Vocabs at `vocabs.openeduhub.de`. Covers **learning-resource type** (including a LOM-based set, `lom_*`), **educational context, educational level, discipline, school type**, **rights and copyright restriction, cost and price**, **quality criteria** (`quality_*`: data privacy, didactics, language) and **competence frameworks — DigCompEdu, ESCO skills, EQF/DQR levels**. **CC0-1.0 is the most permissive tier this KB has recorded on any asset** — no attribution condition at all. This is the row that corrects the p319 Germany claim below |
| https://github.com/openeduhub/oeh-search-etl | 🔴 **NO LICENCE FILE** | 8 | p321 | Harvesting (EMEA) | The ETL behind WirLernenOnline: Scrapy spiders → Postgres → Elasticsearch, Python 3.13 managed with Poetry, Splash and Playwright containers for rendered sources; **1,397 commits on `master`** — the most heavily maintained artefact in the `openeduhub` org. 🔴 **Read it, do not depend on it.** No LICENSE file was present in the repository root when it was read first-hand at p321 and the page states no licence, so **there is no grant**. The commit count makes it the most tempting harvester in the sector and the missing licence makes it unusable in a client deliverable. Spider count is not stated in the README — `converter/spiders/` is not enumerated on the page, so this KB does **not** have a source count |
| https://github.com/virgiliojr94/book-to-skill | MIT | 35.3k | p319 | Enablement / authoring | Converts a technical book, document folder or source set (PDF, EPUB, DOCX, HTML) into a structured agent skill: `SKILL.md` index, per-chapter files, glossary, patterns, cheatsheet; 228 commits, 3.7k forks. **The MIT licence covers the converter only, explicitly not the books you process with it** — which is the copyright question every "turn our textbooks into a tutor" engagement has to answer on day one. Read first-hand this pass: no agent-directed star solicitation in the README |
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p319 | Retrieval | simple, fast RAG (EMNLP 2025), 10,873 commits, 5.7k forks. **Re-verified first-hand this pass** (the p316 reading was due a re-read): still MIT, unchanged. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`, 1.0k forks. Re-verified first-hand this pass: still MIT, still the only MIT platform in the sector, and the one that works without connectivity |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | 376 | p319 | Integration (LTI) | "A multi-tenant scalable LTI library and tool hosting environment", plus an administration/management/developer console and an **IMS ContentItem app store**; 4,011 commits, 266 forks, 43 watchers, **Apereo Incubating**, maintained around Dr Chuck (Charles Severance, co-author of the LTI specification); shares low-level IMS libraries with Sakai; PHP, with per-PHP-version branches. **Caveat: the GitHub page does not state which LTI versions or Advantage services it implements** — verify before scoping |
| https://github.com/jcputney/scorm-again | MIT | 356 | p319 | Integration (SCORM) | "A modern, fully-tested JavaScript runtime for SCORM 1.2 and SCORM 2004", LMS-agnostic, logs calls and data when no LMS endpoint is configured; 1,229 commits, 84 forks. **AICC support was removed in v3.0.0; cmi5 and xAPI are roadmap "potential" only.** The route into the large installed base of SCORM courseware that LTI does not reach |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p319 | Integration | LTI 1.3 Advantage tool implementation, 178 commits. Covers **Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch** — the whole Advantage surface. This is the repo that gets your agent *into* the client's existing LMS. **Re-verified p319: 84 forks, 39 open issues, still no published release** — pin a commit |
| https://github.com/adamzammit/LTIPlugin | **GPL-3.0** | 14 | p320 | Integration (LTI, outcome passback) | Makes **LimeSurvey act as an LTI provider**: the learner launches a survey or assessment from the LMS and the plugin **returns a score to the gradebook**, as a 0.0–1.0 value computed from a LimeSurvey expression; 97 commits on `master`, LimeSurvey 3.x–7.x. **README documents setup against four platforms — Canvas, Moodle, openEdX and Blackboard** — which makes it the broadest passback reference in this file. **Three caveats, all load-bearing.** (1) **It is not AI** — it is assessment delivery plus outcome passback; the intelligence would be yours. (2) **The page never names an LTI version** and it bundles `LTI-Tool-Provider-Library-PHP`, which points at the **legacy LTI 1.x Basic Outcomes path, not 1.3 Advantage AGS** — read the submodule before scoping. (3) **GPL-3.0 is copyleft**, so it sits with `tutor-gpt`/`lumen`/`LTLTutor` on the far side of this KB's architectural line: run it as a separate service, do not link it into a deliverable. **Its value is as a readable, four-LMS answer to "how does the score actually get back".** No release is published — pin a commit |
| https://github.com/bncc-dev/bncc-dados | **MIT (code) / CC BY 4.0 (data)** | 22 | p319 | Curriculum standard (LATAM) | **Brazil's national curriculum (BNCC) as verified open data**: 1,721 learnings — 1,580 from the three stages of basic education (93 Educação Infantil, 1,304 Ensino Fundamental, 183 Ensino Médio) plus 141 from the Computing complement (Parecer CNE/CEB 2/2022) — with 20 legal milestones and 5 reference profiles, in JSON (canonical), SQLite, SQL dump and CSV, under JSON Schema draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, status stable; 40 commits. Maintained by **Profy Tecnologias Educacionais Ltda**; docs pt with a full en translation |
| https://github.com/bncc-dev/bncc-pacotes | **MIT (code) / CC BY 4.0 (data)** | 9 | p319 | Integration (MCP, LATAM) | Machine interfaces to the dataset: npm `@bncc/dados` 0.7.0 (typed API with embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server, seven tools**: `bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`), PyPI `bncc` 0.5.0, and a hosted MCP endpoint at `mcp.bncc.dev` on Cloudflare Workers **requiring no API key**; 103 commits. Embedded data is synced from a pinned `bncc-dados` commit with version and checksum records; a well-formed code that is missing returns an explanatory error, not `null` |
| https://github.com/bncc-dev/bncc-benchmark | **MIT (code) / CC BY 4.0 (items, results, methodology)** | 9 | p319 | Evaluation (LATAM) | Measures how often LLMs invent BNCC codes and texts with no access to the source: four tasks — direct lookup, existence (including plausible fake codes), open generation, reverse lookup — scored against the verified dataset across five dimensions; 82 commits. Official round `oficial-seca-2026-09`; a held-out item set is never published so memorisation is detectable. **Carries the grounding measurement this KB has never had** |
| https://github.com/thm-mni-ii/feedbacksystem | Apache-2.0 | 24 | p319 | Autograding / feedback (EMEA) | Intelligent tutoring system that checks student submissions automatically, returns an immediate result with suggestions about the mistake, and **aggregates common errors so lecturers can address them in class**; 2,248 commits on `dev`, 147 issues, 94 PRs. Java 11/Gradle, Scala, MySQL, Docker Compose, Kubernetes + Helm for production. **Apache-2.0 © Technische Hochschule Mittelhessen** — institution-built, institution-run. No LMS or LTI integration described |
| https://github.com/elimu-ai/webapp | MIT | 41 | p319 | Offline content delivery | Hosts Android apps and educational content (texts, words, videos, storybooks) per language; the elimu.ai Appstore app pulls and installs it onto devices for **out-of-school children**; 8,075 commits, 68 forks, Java/Spring, REST API consumed by three Android apps. Production deployments listed for **Hindi, Tagalog, Thai, Vietnamese and English**. The org publishes 92 repos including real ML components — `ml-storybook-reading-level`, `ml-storybook-recommender`, `ml-video-recommender`, `ml-event-simulator`, `ml-datasets` — all MIT-org, all under 10 ★ |
| https://github.com/smashburger-dev/argmin | **MIT (code) / CC BY 4.0 (content)** | 6 | p319 | Enablement (EMEA) | A **German-language** browser course on how AI works: 50 lessons, 280+ exercises, 320-entry glossary, from maths basics through linear algebra, ML, deep learning, transformers and generative AI; Python runs in-browser via **Pyodide and the app works offline after first load**; 343 commits; self-hostable. The licence-clean German asset for the EU AI Act Article 4 staff-literacy duty |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure — read the caveat |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | Apache-2.0 | 12 | p316 | SIS / data standard | Successor to the Ed-Fi ODS/API platform; 1,105 commits. The standards-body reference implementation for student data |
| https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster | Apache-2.0 | 6 | p316 | Rostering | Serves a **OneRoster 1.2** API from data in an Ed-Fi ODS database; 151 commits |

**Licence split over 21: MIT (8), Apache-2.0 (5), BSD-3-Clause (2), MIT-code-with-CC-BY-4.0-data or
-content (5), GPL-3.0 (1 — `LTIPlugin`, new in p320) — 21/21 usable, 15/21 under a pure permissive
software licence.** The GPL-3.0 row is the first copyleft entry this file has ever carried, and it
is carried deliberately: **a copyleft licence is a constraint on how you deploy, not a bar on
reading or running it.** Keep it behind a process boundary and it stays usable; link it into a
client deliverable and it does not. The five dual-licensed rows
(the three `bncc-dev` repos, `argmin`, and by extension the eval tier in `agents/top.md`) are the
new shape in this file and they need handling: **CC BY 4.0 is attribution-only, so the data is
commercially usable, but it is data, and the attribution has to appear in the deliverable.** Put
the credit line in the product, not in a licence register nobody reads.

The structural fact is unchanged: **the copyleft in this industry lives entirely in the LMS/platform
tier** (`verticals/solutions.md`), and everything you would put *under* a product is permissive.

## The `bncc-dev` stack — the artefact every pattern in this KB assumed a client would supply

Three repositories under the `bncc-dev` organisation, maintained by **Profy Tecnologias
Educacionais Ltda** (Brazil), together do what no other source in this sector does: they turn a
**national curriculum standard into verified, machine-readable, permissively licensed
infrastructure, and then measure what it is worth.**

**1 — The data (`bncc-dados`, 22 ★, 40 commits).** 1,721 learnings: 1,580 from the BNCC's three
stages of basic education (Educação Infantil 93 objectives, Ensino Fundamental 1,304 skills, Ensino
Médio 183 skills) plus the **141-item Computing complement** added by Parecer CNE/CEB 2/2022, with
20 legal milestones and 5 reference profiles. JSON is canonical; SQLite, a SQL dump and CSV are
generated; JSON Schemas are draft 2020-12. Content version `dados-2026.08`, schema v1.1.0, declared
stable.

**The verification discipline is the part to copy.** Per its own documentation: the 1,580 BNCC-2018
texts were checked **character by character against the homologated PDF**; the 141 Computing texts
against the Parecer's annex; a code sweep confirms no missing or extra codes; `validar.py` runs
**30 contract and completeness checks**; the pipeline is reproducible and **CI fails on
divergence**; and every decision taken about an inconsistency in the source is recorded in
`DECISOES.md`. Licensing is split deliberately — **MIT for the pipeline, CC BY 4.0 for the data**,
on the stated reasoning that the compilation, structure and curation are Profy's work while the
normative BNCC texts are official acts.

**2 — The interfaces (`bncc-pacotes`, 9 ★, 103 commits).** npm `@bncc/dados` 0.7.0 (typed API,
embedded data), npm `@bncc/mcp` 0.6.0 (**MCP server with seven tools**: `bncc_lookup`,
`bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`,
`bncc_progressao_ei`), PyPI `bncc` 0.5.0, plus a **hosted MCP endpoint at `mcp.bncc.dev` on
Cloudflare Workers that needs no API key**. Embedded data is synced from a pinned `bncc-dados`
commit with version and checksum records in each package's `dados/VERSAO.json`. A well-formed code
that is absent returns an explanatory error rather than `null` — a small decision that prevents a
tutor from silently inventing a standard.

**3 — The measurement (`bncc-benchmark`, 9 ★, 82 commits), and this is the number to take to a
client.** The benchmark asks models about BNCC codes and texts with no access to the source, across
four tasks: direct lookup, **existence (which tests whether a model accepts plausible fake codes)**,
open generation, and reverse lookup. Score is the mean of five dimensions — recognising real codes,
rejecting fake ones, text fidelity, reverse lookup, correct citation in open generation. A held-out
item set is never published so memorisation remains detectable, and v0.3.0 moved to direct provider
APIs and corrected the judge rubric, making it incomparable with v0.2.0.

Its **grounding study (8 models, 300 items)** reports:

| Condition | Hallucination rate |
|---|---|
| No source available | **31.9%** |
| Curriculum data pasted into the prompt | **0.2%** |
| Model queries the `bncc.dev` MCP server | **2.3%** |

— an average drop of **30.6 points**. A 95% bootstrap confidence interval is reported; its bounds
are not shown on the page.

**This is the first quantified grounding claim in this KB.** Every pattern here has asserted that
retrieval grounding matters; now there is a published, reproducible, regionally specific number for
how much, on a national curriculum, with the MCP route costing about 2 points against pasting the
data in. Use it: *"on Brazil's national curriculum, an ungrounded model invents a standard about a
third of the time; querying the verified source takes that to roughly two percent."*

**Three caveats, stated because the repository states them:**

- **The maintainer declares a conflict of interest.** Profy ships commercial products that run LLMs
  on the BNCC. The disclosure is in the repository; treat the benchmark as credible-and-interested,
  the way you would a vendor-run benchmark that publishes its method and its held-out set.
- **The page's own totals disagree.** The README describes the official round as 19 models × 900
  responses with 17,100 raw responses published; the About line says 15,300 responses from 17
  models. **Cite the round identifier (`oficial-seca-2026-09`) and the per-model design, not the
  total**, until the discrepancy is resolved.
- **Model-level results are a snapshot and the labels are the benchmark's own.** Its published
  top five are GPT-6 Astra 94.7 (88% faithful text, 3% fake-code acceptance), Claude Fable 5.1 81.8
  (80%, 0%), Muse Spark 1.3 79.4 (73%, 10%), Gemini 3.1 Pro 78.0 (67%, 3%) and Claude Opus 5 76.8
  (71%, 4%), with faithful-text rates across all models ranging from 88% down to **3%**. **The
  ranking will be stale within a quarter; the 88%-to-3% spread will not be** — and that spread,
  not the leaderboard, is the argument for grounding over model selection.

**Why this is in the foundations file and not the market file.** It is a dependency you would put
under a product today: the data is CC BY 4.0, the code is MIT, the MCP server is hosted and
keyless, and nothing about it is experimental. For any engagement touching Brazilian basic
education — public-sector, private-network or edtech-vendor — **this is the curriculum spine, and
the benchmark is the acceptance test.** See pattern **P10**.

## The pylti1.3 concentration risk now has a real alternative, not just an index

Pass 317 flagged this and it remains the correct thing to worry about: **every pattern in this KB
crosses the LMS boundary through `pylti1.3`** — one MIT library, 138 stars, 178 commits, a single
maintainer and 39 open issues with no visible release cadence. That belongs in the risk section of
any SOW that depends on it, and it still does.

**Pass 319 found the alternative itself: `tsugiproject/tsugi` — Apache-2.0, 376 ★, 266 forks,
4,011 commits, Apereo Incubating.** It describes itself as "a multi-tenant scalable LTI library and
tool hosting environment", doubles as an administration/management/developer console, implements an
**IMS ContentItem app store**, shares low-level IMS libraries with Sakai, and is maintained around
**Dr Chuck — Charles Severance, co-author of the LTI specification**. It keeps per-PHP-version
branches (`master`, `php-80-x`, `php-74-x`, `php-72-x`) and its README notes production servers
pulling updates every 30 minutes.

**Against `pylti1.3`'s 178 commits and single maintainer, that is a different class of artefact** —
and it is Apache-2.0, which is the tier Globant prefers. **Two honest caveats:**

- **Its GitHub page does not state which LTI versions or Advantage services it implements.** No
  mention of LTI 1.3, Advantage, Deep Linking, AGS or Names and Roles; ContentItem is
  Deep-Linking-adjacent but not the same claim. **Verify the Advantage surface against the
  repository and the Tsugi documentation before it goes in a proposal** — this is the single
  highest-value verification item for pass 320, and it is one page load.
- **It is PHP.** For a Python shop that is a real cost; for a client already running Moodle or any
  PHP stack it is an advantage.

Also recorded for integration breadth: **`jcputney/scorm-again` (MIT, 356 ★, 1,229 commits)**, a
tested JavaScript runtime for **SCORM 1.2 and SCORM 2004**, LMS-agnostic, which reaches the large
installed base of SCORM courseware that LTI does not. **AICC support was removed in v3.0.0, and
cmi5/xAPI are roadmap "potential" only** — do not promise either.

Carried from pass 318: **`1EdTech/ltibootcamp`** (127 ★, 47 commits), a curated index of LTI 1.3
implementations maintained under the **1EdTech GitHub organisation** — the standards body itself.
It maps the library landscape across seven languages:

| Language | Implementations it names |
|---|---|
| Python | **PyLTI 1.3** (Flask/Django examples), UCF Flask starter template, `django-lti`, Robotest test tool (FastAPI), Open Learning LTI 1.3 Platform (Django) |
| JavaScript / Node | **ltijs** (1.3 core and services), Blackboard Node tool provider, Atomic LTI Worker |
| PHP | IMS 1.3 library and demo tool, TAO hosted test platform, OAT libraries (1.3 core, Deep Linking, Names & Roles, Symfony bundle) |
| Java | Unicon Spring Boot demo, UOC LTI 1.3 library + Spring Boot library + provider example |
| .NET | `LtiAdvantagePlatform` example platform (andyfmiller) |
| Ruby | Atomic Jolt LTI starter app |
| Rust | Atomic Forge |
| Other | An AWS LTI "shim" service |

**Three caveats, and they are not small:**

- **The repository itself has no LICENSE file.** It is an index of links, so there is little to
  licence, but it cannot be vendored and it is not in the table above for that reason.
- **It is stale.** Its only two content folders are `barcelona_2019` and `europe_tech_2020`, and
  it carries 47 commits. Entries may be dead; the LTI 1.3 specification has moved since 2020.
- **Its own README disclaims vetting:** *"The resources listed here are for information only and
  have not been vetted."* It sits under the 1EdTech organisation but reads as a community-curated
  list open to pull requests — treat it as a starting index, not a standards-body endorsement.

**What it is worth anyway:** the mitigation question for `pylti1.3` was previously answered with a
hand-wave ("reference implementations exist in other languages"). It now has specifics. If a
client's stack is Node, **`ltijs`** is the route — and it is the library `blamb/lti-tutor` chose to
implement working deep linking and AGS passback against Moodle (see `agents/top.md`). If the stack
is Java, the UOC libraries are the named option. **Verify any entry against its own repository
before scoping on it**; the index is five years stale and unvetted by its own admission.

## The method that found most of pass 319: search GitHub topics in the region's own language

This KB has written "a star-ranked search cannot see this sector's infrastructure" for three passes
without changing its search. Pass 319 changed it: **GitHub topic pages were swept in Portuguese,
Spanish, German and Dutch, and in the two curriculum-specific Indian tags.** The results are
asymmetric, and the asymmetry is itself a regional finding.

| Topic swept | What it surfaced |
|---|---|
| `educacao` (pt) | **Infrastructure.** `portabilis/i-educar` (720 ★, **34,948 commits**, school management, `verticals/solutions.md`), `portabilis/i-diario` (117 ★, 15,834 commits), `ipti/br.tag` (20 ★, 3,959 commits, offline sync for rural schools), and **the entire `bncc-dev` curriculum stack** |
| `educacion` (es) | **Teaching materials, almost exclusively.** 370 repos; the top entries are Spanish-language JavaScript and Python course guides, a Moodle–SENCE attendance plugin (29 ★), vocational-training course material, a Uruguayan school-finder (`datauy/ElijoEstudiar`, 5 ★). **No AI infrastructure, no curriculum data** |
| `ncert` + `cbse` (India) | **Hobby projects.** 55 + 125 repos; nothing above 15 ★ that is curriculum infrastructure. Detail in `agents/top.md` |
| `bildung` (de) | **One usable asset and one warning.** `smashburger-dev/argmin` (MIT + CC BY 4.0, 343 commits, German AI course, offline-capable) and `davidpomerenke/lernplattform` (GPL-3.0, **archived 2021-01-01**, which pointed to "wir lernen online" as its successor). Also **a 13-repository single-author cluster of near-identical "tech evangelism" pages at 1 star each** — topic pages can be padded, which is one more reason the ★ column is noise |
| `onderwijs` (nl) | **Rostering glue, no AI.** `sikkepitje/TeamSync` (9 ★, PowerShell, syncs Magister school records into Microsoft School Data Sync) and two open secondary-school course repos (`wiskunde.opmaat`, `natuurkunde.opmaat`) |
| `oer` (en, for contrast) | 419 repos of **textbooks and course materials**, nothing describing curriculum or competency metadata, and no AI |
| `pendidikan` (id) | **42 repos, and exactly one AI artefact.** `RozhakDev/EduPintarIPAS` (**MIT**, 20 ★, **1 commit**, Flask, **Azure AI Language Custom Question Answering**) answers `IPAS` science-and-social-studies questions for Indonesian year-6 pupils off a QA set the README says was built from the official `SD` curriculum, and is aimed explicitly at **3T regions** (*tertinggal, terdepan, terluar* — underdeveloped, frontier, outermost) where tutoring is scarce. Everything else in the topic is school administration at 0–4 ★ — enrolment (`PPDB-online`), tuition (`aplikasi-spp`), facilities (`sisp`), a boarding-school monitor. **The curriculum-grounded-QA pattern exists in Indonesian; the engineering behind it does not — one commit is a demo, not a dependency** |
| `enseignement` (fr) | **40 repos, zero AI.** Almost entirely teaching material for the French system: the `NSI` computer-science specialism at lycée, `CAPES` oral topic lists, LaTeX maths and geometry courses, a Python teaching IDE (`Pydiderot/pydiderotIDE`). The one infrastructure artefact, `ValbionGroup/Gadia` (**MPL-2.0**, 6 ★, 63 commits, Laravel/Blade school-life management — timetable, class notebook, grades, absences, canteen), was **archived by its owner on 2025-10-28 and is read-only**, and its README already warned the features were not guaranteed. **France's tag is pedagogy, not platform** |
| `kyoiku` (ja) | **1 repo, 0 ★.** `mitsurutech/joho-puroguramingu-renshu` — 48 Python, SQL and web (HTML/CSS/JS) exercises for Japanese high-school *jōhō*, starter code, deliberately no solutions. No AI, no infrastructure |
| `gyoyuk` (ko) | **The topic page exists and holds 0 repositories.** GitHub's own wording: "hasn't been used on any public repositories, yet". **This is the cleanest negative in the table — not a thin result, an empty one** |
| `shiksha` (hi) | **3 repos, ceiling 3 ★.** `arhaanb/shiksha` (3 ★, last touched 2022-04-07), `shiksha-platform/documentation` (1 ★, 2022-01-20, no description) and an **archived** `.shiksha` domain-name extract. No AI, and the two real ones have been untouched for four years |
| `taleem` (ar/ur) | **1 repo, 1 ★** — an Urdu-language Islamic blog of 370+ articles on static HTML. **Not education infrastructure, and the slug does not answer the Arabic question** — see the slug finding below |

**Two conclusions, and the second is the commercial one.**

1. **Adopt this as standing method.** Every regional gap this KB has declared was declared from
   English-language searches. One Portuguese topic page produced a verified national curriculum
   dataset, an MCP server, a published benchmark and a 34,948-commit SIS. **Before declaring a
   regional absence, sweep the topic in the region's language** — and record which language you
   swept, so the next pass knows what was actually tested.
2. **The gap is not uniform, and it is not about talent.** Brazil has curriculum-standard
   infrastructure because someone built it to a verification standard and licensed it cleanly.
   Spanish-speaking LATAM, India, Germany and the Netherlands do not have an equivalent — in the
   topics swept — and in India's case there is a hard curriculum mandate arriving in 2026-27 with
   nothing underneath it. **That is a build-once opportunity with a named template** (`bncc-dev`)
   and a named buyer (any ministry, board or national edtech with a mandate and no data layer).
   Pattern **P10**.

**Limits of the claim, stated so pass 320 does not over-read it.** These were topic-page sweeps of
the first ~20 repositories per topic, not exhaustive searches; GitHub topics are
author-applied, so an unlabelled repository is invisible to this method; and only six topics in
five languages were swept. **"Not found in the topics swept" is the finding. "Does not exist" is
not.** Untested and worth a pass: Arabic, Hindi, Japanese, Korean, French and Indonesian topic
tags, and the `wirlernenonline` organisation, whose GitHub org page could not be read this pass.

## Pass 321: the p319 to-do list, executed — and the Germany claim it corrects

Pass 319 ended its sweep section with a named to-do: *"Untested and worth a pass: Arabic, Hindi,
Japanese, Korean, French and Indonesian topic tags, and the `wirlernenonline` organisation, whose
GitHub org page could not be read this pass."* **All seven were attempted at p321.** Six are
negatives and are in the table above, written down rather than left as silence. The seventh is the
find of the pass.

### 1. The correction: Germany *does* have a competency-metadata layer, and this file said it did not

Pass 319 concluded, from the `bildung` and `oer` sweeps, that **"Spanish-speaking LATAM, India,
Germany and the Netherlands do not have an equivalent"** to Brazil's `bncc-dev` curriculum stack,
and that the `oer` topic held "nothing describing curriculum or competency metadata." **For Germany
that is now wrong, and the artefact is better licensed than the Brazilian one.**

`openeduhub/oeh-metadata-vocabs` is **CC0-1.0** with **938 commits** and carries SKOS vocabularies
for educational context, level, discipline and school type, rights and copyright restriction, cost
and price, machine-readable quality criteria, and the **DigCompEdu, ESCO and EQF/DQR competence
frameworks** — published under a stable `w3id.org` namespace with a browsable SkoHub front end.
That is a competency-metadata layer by any reading.

**Why p319 missed it, and the lesson is about method rather than luck.** The repository is tagged
for neither `bildung` nor `oer`; it lives in an organisation p319 looked for **under the wrong
name**. `github.com/wirlernenonline` is **404**. The account is `openeduhub`, and the only way this
pass reached it was by searching the *project* name and reading the owners off the results. **A
topic sweep cannot see an untagged repository, and an org sweep cannot see an org whose GitHub
handle differs from its public brand.** Both failure modes are now demonstrated, not hypothesised.

### 2. The slug finding — why "sweep the topic in the region's language" needs one more rule

`https://github.com/topics/教育` returns **404**. GitHub topic slugs are ASCII-normalised, so a CJK
term cannot be typed in as a topic even when it is the word the region actually uses. The sweeps
that worked were the **transliterations** — `kyoiku`, `gyoyuk` — and one of those turned out to hold
zero repositories. So p319's standing method gains a clause: **sweep the region's language, and for
non-Latin scripts sweep the romanisation, because the topic namespace will not accept the script.**
Pass 319 could not have discharged "Japanese, Korean" by typing the obvious thing.

### 3. What `openeduhub` is, and why a 0 ★ org is worth a section

**67 public repositories.** The org profile describes itself as the account behind
WirLernenOnline.de: *"This OER-Infrastructure makes (O)ER findable and usable in connected
platforms,"* based on **edu-sharing**, WordPress and others — i.e. Germany's publicly funded open
educational resources portal, with its plumbing on GitHub. Four repositories were read first-hand
this pass:

| Repo | Licence | ★ | Commits | What it is |
|---|---|---|---|---|
| `oeh-metadata-vocabs` | **CC0-1.0** | 2 | **938** | SKOS/Turtle vocabularies incl. DigCompEdu, ESCO, EQF/DQR — see the row above |
| `oeh-search-etl` | 🔴 **none** | 8 | **1,397** | Scrapy → Postgres → Elasticsearch harvester — see the row above |
| `tutor-chatbot` | **Apache-2.0** | 0 | 10 | RAG tutor over the WLO API with Bloom-taxonomy analytics — `agents/top.md` |
| `ki-prompt-benchmark` | **Apache-2.0** | 0 | 3 | LLM-as-judge prompt bench, exports `mds.xml` — `agents/top.md` evaluation table |

Also present and unread at p321, named here so p322 does not re-discover them: `metalookup`
(5 ★, Python, domain metadata including licensing), `oeh-search-frontend` (5 ★, TS),
`edu-sharing-python-client` (0 ★), `lernpfadeditor` (learning-path editor with differentiation and
content assignment), `wlo-quellenliste`, `metadata-browser-plugin-fuerAPI`. **57 of the 67 were not
listed on the first page and remain unenumerated.**

**The star counts are 0, 0, 2 and 8, and that is this KB's Ed-Fi lesson repeating in a second
jurisdiction.** The Ed-Fi section below makes the argument from 12 ★ and 6 ★ of US state-adopted
infrastructure. `openeduhub` makes it again from a German federal-state-funded portal with a
1,397-commit harvester at 8 ★. **A star-ranked search cannot see publicly funded education
infrastructure in any region, and two independent instances is no longer a coincidence.**

### 4. The licence split inside one org, which is the practical warning

The same organisation ships **CC0-1.0**, **Apache-2.0** and **no licence at all**, and the
unlicensed repository is the one with the most commits. **Do not infer an org-level licence
posture from one repository.** On this evidence the rule for `openeduhub` is: take
`oeh-metadata-vocabs` (CC0) and the two Apache-2.0 tools freely; treat `oeh-search-etl` as
documentation of a harvesting design and **write your own**, or open an issue asking for a licence
before any engagement depends on it.

## The Ed-Fi finding — the gap this KB declared three passes running, closed in p316

The Ed-Fi Alliance publishes its platform as Apache-2.0 under the `Ed-Fi-Alliance-OSS` GitHub
organisation. The Data-Management-Service has 1,105 commits; `edfi-oneroster` serves OneRoster 1.2
off an Ed-Fi ODS and has 151. Both are Apache-2.0 — the licence tier Globant prefers.

**The stars are 12 and 6, and that is the whole lesson.** A star-ranked search systematically
cannot see public-sector education infrastructure, because it is adopted through state education
agencies and SIS vendors rather than through GitHub. **Pass 318 added a fourth confirmation of
this** — `openedx/openedx-ai-extensions`, the official Open edX AI plugin, has **17 stars and 703
commits** (see `verticals/solutions.md`) — and a fifth datapoint from the opposite direction: a
repo in this sector now openly solicits stars from AI agents (see `agents/top.md`). **Rank
candidates on commit count, release cadence and licence. Stars are noise in both directions.**

Two caveats before scoping on Ed-Fi:
- Neither repo has a published release on its GitHub Releases page. Pin to a commit, not a tag.
- Ed-Fi is a **North American** standard in practice (US state education agencies). It is not a
  route into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions.

## Caveats

- **Sunbird's 41 ★ are not a quality signal**, for the same reason Ed-Fi's 12 are not. Government
  adjacent infrastructure in India, adopted through state deployments. Verify the wider
  `Sunbird-Ed` org's component repos before scoping.
- **`ai-agents-for-beginners` is a curriculum, not a library.** It sits here deliberately: 77.5k ★
  of MIT teaching material is a reusable asset for the "train the client's team" phase that ends
  most education engagements.
- **`pylti1.3` is the most load-bearing 138 stars in this KB.** See the mitigation list above.
- **LightRAG + DeepTutor remains the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive, ~82k ★ between them, covering retrieval and tutoring. Pattern P1 is built on it.
  DeepTutor was re-verified p318 (v1.6.15, 2026-10-19); **LightRAG was re-verified first-hand in
  p319 — MIT, 40.2k ★, 5.7k forks, 10,873 commits, unchanged. That re-read is now done.**
- **Kolibri's README describes no AI features.** Re-read first-hand this pass. It is the delivery
  substrate for offline contexts; the intelligence layer is yours to add, which is exactly why it
  is in this file and not in the agent tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). **Sixth pass declaring it — and the first pass where the gap is contested
  rather than empty.** GitHub's `ferpa` topic now holds about a dozen governance projects created
  or last updated in September–October 2026, **every one of them at 8 stars or fewer**: Rego policy
  packs (`Principled-Evolution/gopal`), PII-scrubbing ingestion with hash-chained audit trails
  (`marc-shade/docsingest`), identity-scoped RAG patterns and policy middleware (three repos by
  `ashutoshrana`, the same author as p317's `haystack-ferpa-filter`), a FERPA-safe Canvas toolkit
  (`chaz-clark/canvas-toolbox`), Bedrock agents with PII masking (`virtualryder/edu-ai-agents`) and
  an MCP server that audits tutors for FERPA/COPPA (`mizcausevic-dev/mcp-ai-tutor`).
  **None is a dependency.** But a dozen independent authors starting the same component within two
  months of the **COPPA compliance deadline of 2026-04-22** (see `intel/market.md`) is a market
  forming in real time. The build-once opportunity is still the clearest in the sector and the
  window on it is now visibly shorter. Note that Ed-Fi gives you the data *model* and API, not the
  consent, retention and disclosure machinery around it.
- ~~**No LATAM-authored foundational repo.**~~ **CLOSED PROPERLY THIS PASS, and the correction is
  worth stating precisely because this KB has now been wrong about it twice.** Five passes declared
  the gap. Pass 318 found `openedx/openedx-ai-extensions` (eduNEXT, Bogotá) and had to disqualify it
  from this file: AGPL-3.0 and explicitly not for production. **Pass 319 found three Brazilian
  repositories that qualify without caveats** — `bncc-dados`, `bncc-pacotes` and `bncc-benchmark`
  (Profy, MIT code / CC BY 4.0 data, verified against the homologated curriculum PDF, a hosted MCP
  server, a published benchmark). They are infrastructure, they are permissive, they are
  production-usable today, and **they were found by searching a Portuguese-language GitHub topic.**
  The backdrop figures still stand (Linux Foundation, December 2025: **Mexico 65%, Brazil 46%** for
  organisational use of open source AI) and so does the commercial point — the named LATAM
  education-AI companies (Teachy, Ginia, Vetto, Mattilda, Luca, Letrus, MusíGlota) remain private
  and closed-source — but "LATAM consumes open source and does not write it" is finished as a
  sentence. **Spanish-speaking LATAM is a different matter: the `educacion` topic sweep found
  teaching materials and no infrastructure, so the regional finding is Brazil specifically, not
  LATAM generally.**
- **No EMEA- or APAC-equivalent of Ed-Fi — but the gap now needs splitting in two, because one half
  moved and the other did not.** On **rostering**, nothing comparable was found for Europe or Asia;
  the closest artefact is `sikkepitje/TeamSync` (9 ★, PowerShell, Magister → Microsoft School Data
  Sync), which is one country's glue script, not a standard. On **curriculum standards**, Brazil now
  has `bncc-dev` and **nobody else in this KB does** — the German attempt (`lernplattform`) was
  archived in 2021, the Dutch and Spanish-language topics produced course material rather than data,
  and India's NCERT/CBSE repositories are hobby-scale with no verified dataset at all
  (`agents/top.md`). **Ed-Fi remains North-America-only, and it is a data model plus API, not a
  curriculum.** The two gaps are different products and should be scoped separately.
- **elimu.ai's region is not stated and should not be assumed.** Its GitHub organisation page gives
  its location as "Worldwide"; the `webapp` repository lists production deployments for **Hindi,
  Tagalog, Thai, Vietnamese and English**. This KB has an open MENA/Africa supply gap
  (`verticals/solutions.md`) and elimu.ai does **not** close it on the evidence read this pass —
  its documented deployments are APAC-language-first. Recorded here so no proposal cites it as an
  African platform without checking.
