---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

**Pass 318 · 2026-10-19.** Eleven repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says which pass took the licence/star
reading.

Pass 318 re-verified `kolibri` first-hand and **found a direct mitigation for the single largest
concentration risk in this KB's architecture** — the fact that every pattern crosses the LMS
boundary through one 138-star, single-maintainer library. It is not a new dependency; it is a map
of the alternatives, and it is below the table.

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p316 | Retrieval | Simple, fast RAG (EMNLP 2025), 10,873 commits. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`, 1.0k forks. Re-verified first-hand this pass: still MIT, still the only MIT platform in the sector, and the one that works without connectivity |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p317 | Integration | LTI 1.3 Advantage tool implementation, 178 commits. Covers **Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch** — the whole Advantage surface. This is the repo that gets your agent *into* the client's existing LMS |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure — read the caveat |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | Apache-2.0 | 12 | p316 | SIS / data standard | Successor to the Ed-Fi ODS/API platform; 1,105 commits. The standards-body reference implementation for student data |
| https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster | Apache-2.0 | 6 | p316 | Rostering | Serves a **OneRoster 1.2** API from data in an Ed-Fi ODS database; 151 commits |

**Licence split: MIT (6), Apache-2.0 (3), BSD-3-Clause (2) — 11/11 permissive.** Unchanged. The
copyleft in this industry lives entirely in the LMS/platform tier (`verticals/solutions.md`).

## The pylti1.3 concentration risk now has a named mitigation list

Pass 317 flagged this and it remains the correct thing to worry about: **every pattern in this KB
crosses the LMS boundary through `pylti1.3`** — one MIT library, 138 stars, 178 commits, a single
maintainer and 39 open issues with no visible release cadence. That belongs in the risk section of
any SOW that depends on it, and it still does.

Pass 318 found **`1EdTech/ltibootcamp`** (127 ★, 47 commits), a curated index of LTI 1.3
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
  DeepTutor was re-verified p318 (v1.6.15, 2026-10-19); **LightRAG's reading is from p316 and is
  due a re-read next pass.**
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
- **The LATAM authorship gap is no longer absolute — but it closed in the platform tier, not
  here.** Five passes declared "no LATAM-authored foundational repo". Pass 318 found
  **`openedx/openedx-ai-extensions`, the official Open edX AI plugin, authored by eduNEXT of
  Bogotá** (full detail and provenance caveats in `verticals/solutions.md`). It is AGPL-3.0 and its
  README says it must not be used in production, so **it does not qualify for this file** — nothing
  experimental and copyleft belongs under a client product. What changes is the sentence this KB
  has been repeating: LATAM is no longer only a consumer of open source education AI. The backdrop
  stands — the Linux Foundation's December 2025 report puts **Mexico at 65% and Brazil at 46%** for
  organisational use of open source AI — and the named LATAM education-AI companies (Teachy, Ginia,
  Vetto, Mattilda, Letrus, MusíGlota) remain private and closed-source.
- **No EMEA- or APAC-equivalent of Ed-Fi.** Ed-Fi closes the North American rostering gap only.
  Searched again; still nothing comparable for European or Asian rostering standards.
