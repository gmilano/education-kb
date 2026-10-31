---
industry: education
region: Global
updated: 2026-10-31
---

# Current trends — education AI

Confidence is stated per trend. Where a trend was **measured first-hand** from
GitHub's own index rather than read from a source, that is said explicitly —
those are the most reliable items on this page and the least likely to appear
anywhere else.

## 1. Education AI has stopped shipping as applications and started shipping as agent skills (high confidence — measured first-hand)

**The biggest change since the previous pass, and it is measured, not reported.**
Querying GitHub directly for `topic:agent-skills topic:education stars:>50`
returns **13 repositories**. **Six of the fourteen** agents on
[`../agents/top.md`](../agents/top.md) are skill bundles — markdown instruction
sets (`SKILL.md`, `AGENTS.md`, `CLAUDE.md`) loaded by an existing harness, with
**no runtime, no service and no API**. The cohort on GitHub, by stars:

| Repo | ★ | Licence | What it is |
| --- | --: | --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 4,843 | **CC BY-SA 4.0** | 23,000+ skills for empirical research across 8 social-science disciplines; CoPaper.AI / Stanford REAP |
| [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | 2,750 | **none** | Brazilian study-mentor agent bundle; runs on 5 named harnesses |
| [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | 1,201 | MIT | PDFs/books/papers → traceable interactive learning pages |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 586 | unresolved | K-12→career skill tree, 30+ skills, ships an MCP server |
| [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | 295 | MIT | Bloom's 2-sigma as a skill **plus** a self-hostable app |
| [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 213 | MIT | Chinese civil-service exam prep |
| [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | 203 | MIT | Project-driven mastery learning |
| [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | 119 | MIT | Teaching/tutoring skill collection incl. *gaokao* |

**Why this matters more than it looks.** Three consequences for an engagement:

1. **There may be nothing to host.** The deliverable is a prompt contract. That
   collapses infrastructure cost and collapses the recurring-revenue story with
   it. Price the authoring and the maintenance, not the running.
2. **Versioning and evaluation become the hard problems.** A skill bundle has no
   semver discipline, no test suite by convention, and changes behaviour when the
   *harness* or the *model* changes underneath it — neither of which the client
   controls. This is the strongest argument for the evaluation layer in trend 7.
3. **Licence screening gets harder, not easier.** The largest member of the
   cohort is **CC BY-SA 4.0** — a share-alike *content* licence on a code-shaped
   artefact, which propagates to derivatives of the skill text. The
   second-largest has **no licence at all**. A skill bundle looks like
   documentation and is governed like a work of authorship.

The cohort is also **overwhelmingly APAC-origin** (six of the eight above are
Chinese-language or China-maintained), with a Stanford exception at the top and a
Brazilian one in second place.

## 2. From experimentation to governance (high confidence — every source agrees)

The consistent framing across industry sources: AI moves from standalone pilots
into admissions, advising, learning and administration as embedded
infrastructure. HolonIQ expects attention to shift to ethics, transparency,
agentic use cases and *proven instructional benefit* over broad personalisation
promises; 1EdTech frames it as evolving from isolated use cases to coordinated,
policy-guided ecosystems. The hard numbers behind it are in
[`market.md`](market.md): 87/26 in LATAM, 63% teacher use in EMEA, 60% in the US,
7-of-39 operational governance in Australia. **The gap between use and governance
is the market.**

## 3. Purpose-built beats general-purpose (high confidence)

Vendors and analysts converge on movement away from generic assistants toward
platforms built for education. This KB's own evidence agrees from the supply
side: the two largest education agents in the world are **purpose-built
education** projects from universities (DeepTutor/HKU, OpenMAIC/Tsinghua), not
education wrappers on general agents — and the prescribed "top open source AI
agents education" search returns only general-purpose listicles, i.e. the
*commentary* layer still has no education-specific map while the *code* layer
clearly does.

## 4. The compliance calendar and the capability calendar have come apart (high confidence — re-verified independently, and extended)

The previous pass recorded this correctly and in detail; this pass **re-verified
it from fresh sources and added two things it did not have.** The table stands:

| Regime | Status on 2026-10-31 |
| --- | --- |
| EU AI Act — stand-alone Annex III high-risk (incl. education) | Deferred to **2027-12-02** by the Digital Omnibus amendment, in effect late July 2026 |
| EU AI Act — AI embedded in regulated products | Deferred to **2028-08-02** |
| EU AI Act — **Article 50 transparency duties** | **Not deferred. In force since 2026-08-02** ← *new this pass* |
| EU — AI-generated intimate imagery / abuse material ban | Coming into force **December 2026** |
| South Korea AI Basic Act | **In force 2026-01-22**; enforcement decrees pending, guidance-first grace period through 2026 |
| Vietnam AI law | **Effective 2026-03-01**; high-risk designation covers education incl. automated assessment |
| Australia (TEQSA) | Institutional generative-AI action plans required of **all** higher-ed providers — **100% response rate achieved** ← *new this pass* |

**What is new.** First, the postponement is attributed by multiple independent
legal commentaries to **Regulation (EU) 2026/1744**, in force 27 July 2026 after
Council approval on 29 June 2026 — a citeable instrument, where the previous pass
had only "the Digital Omnibus amendment". Second, and more useful commercially:
**Article 50 transparency duties were not part of the deferral** and have applied
since **2 August 2026**. The calendar therefore has *two* tracks, and conflating
them misprices the work in both directions: **transparency obligations are live
today; conformity assessment is ~14 months out.**

**Widely-repeated error to avoid, restated because it is still in circulation:**
guidance claiming EU high-risk obligations apply from August 2026 was superseded.
Enforcement *machinery* (the AI Office and national authorities) did begin on
2 August 2026 — which is probably the source of the confusion — but the high-risk
*duties* did not.

Meanwhile the capability calendar runs on weeks: OpenMAIC went from repository
creation (2026-03-11) to 41,981★ and `v1.3.0` in under eight months. Capability
deadlines in Asia still land before Europe's.

## 5. Adoption is ahead of governance, and it is now measured on all four regions (high confidence)

Previously high-confidence only in LATAM. Now:

- **LATAM** — UNESCO IESALC/UNU-IAS, 200 institutions, 19 countries: **87%** use,
  **26%** strategy, **55%** no budget, **4%** dedicated funding at public
  universities. Cetic.br: Brazil **53%** of administrators use AI, **22%** have
  guidelines. Ceibal: **75%** of Uruguayan public-school teachers.
- **EMEA** — **63%** teacher use, from two independent surveys that agree exactly
  (European Commission School Education Gateway, April 2026, n=1,130; Sanoma
  Learning, 20,000+ teachers, 14 countries). Eurydice's *Digital education at
  school in Europe 2026* is the member-state source.
- **North America** — **60%** of US teachers (Gallup); most public schools have no
  formal student AI policy; **134** state bills across **31** states; **42.3%** of
  Ontario boards have a student AI policy.
- **APAC** — now primary: TEQSA's **100%-response** institutional census, and
  operational governance structures documented in only **7 of 39** Australian
  universities (AJET). MEXT's pilot covers **478 schools** in **149
  municipalities** — under **2%** of Japanese schools.

## 6. Mandated content without teacher buy-in fails, and there is now a measured case (medium-high confidence — single country, strong detail)

**South Korea's AI textbooks reached below 30% adoption by March, and lawmakers
subsequently removed their official status.** This is the first instance in this
KB of a national education-AI mandate being measured and then *reversed*. Set
against Singapore's approach — a **Teacher AI Literacy Professional Learning
Roadmap** with one compulsory module by end 2026 and two recommended by end 2027,
i.e. capability before content — it reads as a real design lesson rather than an
anecdote: **fund the teacher, not the artefact.** Any national-rollout proposal
should carry an adoption-risk section citing Korea.

## 7. Evaluation is the missing layer, and the absence is now specific (high confidence — measured first-hand)

Three passes of searching have located exactly **three** evaluation assets for
education AI:

- [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
  — MIT, 13★, 1,143 questions from real teacher-qualification exams (CDPK 920,
  SEND 223). Measures whether a model knows how to **teach**.
- [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
  — `NOASSERTION`, 87★, research-backed **rubrics** for scoring generated
  instructional content.
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
  — code MIT / datasets per-publisher, 164★, standards-and-curriculum data layer
  with an MCP server, used to check **alignment**.

**None of the three is a runtime monitor.** There is no open-source way to detect
that a deployed tutor has drifted, regressed after a model upgrade, or started
teaching something off-syllabus. Given trend 1 — skill bundles whose behaviour
changes when the harness or model changes beneath them — this is the single
largest unmet need in education AI, and it is where every region's governance gap
actually bites.

## 8. Credentials and skills-based models (medium confidence — still single-source)

1EdTech continues to point to digital credentials as a key development, with
employer expectations accelerating a skills-driven ecosystem. **No second
independent source surfaced on this pass either**, so this remains a watch item
rather than a trend. Three passes without corroboration is itself informative:
it suggests the credentials story is being carried by the standards body with an
interest in it.

## Licence-structure trend (measured first-hand)

**The agent layer is permissive; the platform layer is not — and the exception
appeared this pass.** Eleven of fourteen shelved agents are MIT, two Apache-2.0.
Platforms of record are AGPL/GPL almost without exception. The new exception,
**`Selleo/mentingo` (MIT, Poland, 102★)**, is the first AI-native LMS a client
can fork and keep closed; **`DSpace` (BSD-3-Clause)** remains the only
permissive platform of record at category-leader scale, in the institutional
repository.

A second structural finding, now firm after three passes: **there is no
permissively licensed education ERP.** The whole category is LGPL (OpenEduCat,
Odoo) or GPL/AGPL (Frappe ×2, i-educar, openSIS). This is no longer recorded as
a search gap; it is recorded as the answer.

## Licence hygiene: the sidebar is not the licence, and `NOASSERTION` is three different things (measured; sharpened this pass)

The method rule stands — **read the file, not the sidebar** — and this pass added
a mechanism and a correction.

**The mechanism:** GitHub's REST API (`license.spdx_id`, `stargazers_count`) was
reachable this run via the MCP GitHub server, after earlier passes recorded it as
proxy-blocked. It is strictly better than reading rendered pages, because it
returns GitHub's own licence determination. It also supports a cheap
*corroborating* query: `license:mit repo:owner/name` returns zero results if
GitHub detects no MIT grant — which independently re-confirmed the
`mcp-canvas-lms` defect that earlier passes established by 404-ing filenames.

**The correction:** `NOASSERTION` does **not** mean "unlicensed". Three distinct
states collapse into it or near it:

| State | Example | What it actually means |
| --- | --- | --- |
| Licence file present, non-standard filename, **split grant** | `learning-commons-org/knowledge-graph` (164★) | `LICENSE.md`; README badges read **code MIT / datasets "By data publisher"**, some datasets **gated**. Code safe; each dataset cleared individually. |
| Licence claimed in prose, **file absent** | `DMontgomery40/mcp-canvas-lms` (104★) | README says "MIT License - see LICENSE file"; that file 404s on every name and both branches. Default: exclusive copyright. |
| **No licence field at all** | `digitalinnovationone/dio-agent` (2,750★) | Genuinely unlicensed. All rights reserved. |

And a fourth shape that is not ambiguous, just wrong for the artefact: a
**content licence on code-shaped work** — `Auto-Empirical-Research-Skills`
(4,843★) under **CC BY-SA 4.0**, share-alike, the largest education agent-skills
repo in existence.

**Across three passes, every licence defect found has been in the agent layer.**
Platforms state copyleft clearly and accurately. The fast-moving layer claims MIT
loosely, ships share-alike, or says nothing — and does so at thousands of stars,
where it is most likely to be adopted without checking.

## A governance trend about AI itself, which belongs here (high confidence)

**South Africa's draft National AI Policy was withdrawn because its citations
were fabricated.** Gazetted 10 April 2026 (Notice 3880); withdrawal announced 26
April 2026 and formalised in a Gazette of 12 June 2026; cause: at least **10% of
the academic references in the reference list were fictitious**.

A national AI policy failed on provenance. For an education client — whose entire
product is claims about what is true, assessed against a syllabus — this is the
most persuasive available argument that **citation provenance is a deliverable,
not a nicety**. It is also why this KB states its method, names its sources, and
records what it could not verify.

## Declared gaps

- **Most trend sources are vendor blogs or market-research summaries.** The load-
  bearing citations are OECD, UNESCO/IESALC, 1EdTech, the European Commission and
  Eurydice reports, TEQSA, the AJET study, named statutes — and, for trends 1, 7
  and the licence sections, **this KB's own first-hand measurements of GitHub's
  index**, which are the most reliable items here.
- **EU AI Act primary text not read.** The 2 December 2027 Annex III date is
  consistent across many legal commentaries citing Regulation (EU) 2026/1744, but
  the Official Journal was not fetched. This KB now gives date-specific advice;
  the next pass should read the OJ.
- **Trend 8 (credentials) is single-source for the third consecutive pass** and
  stays a watch item.
- **Trend 6 rests on one country.** Korea's reversal is well detailed but it is
  one case; Singapore's contrast is a policy design, not yet an outcome.
- **No runtime evaluation tooling exists to recommend** (trend 7). Stated as a
  finding, but it means the governance advice this KB gives cannot currently be
  *operationalised* with open-source components. That is an honest limit on the
  whole page.
- **The agent-skills cohort has no provenance metadata.** Region was assigned
  from README language and maintainer org only; several members have no stated
  country and are left unassigned rather than guessed.
