---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

**Pass 316 · 2026-10-19.** Eleven repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says whether the licence/star reading was
taken in this pass (p316) or earlier the same day (p315).

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p316 | Retrieval | Simple, fast RAG (EMNLP 2025), 10,873 commits. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p315 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p316 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`. The only MIT platform in the sector and the one that works without connectivity |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p315 | Integration | LTI 1.3 Advantage tool implementation. This is the repo that gets your agent *into* the client's existing LMS |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure — read the caveat |
| https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service | Apache-2.0 | 12 | p316 | SIS / data standard | **Closes a three-pass gap.** Successor to the Ed-Fi ODS/API platform; 1,105 commits. The standards-body reference implementation for student data |
| https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster | Apache-2.0 | 6 | p316 | Rostering | Serves a **OneRoster 1.2** API from data in an Ed-Fi ODS database; 151 commits |

## The Ed-Fi finding — the gap this KB declared three passes running is now closed

Passes 313–315 all recorded "no open source OneRoster / Ed-Fi reference implementation found at a
usable maturity", and drew the conclusion that SIS sync is vendor-specific integration work in
every engagement. **That conclusion was wrong, and it was wrong because of how it was searched.**

The Ed-Fi Alliance publishes its platform as Apache-2.0 under the `Ed-Fi-Alliance-OSS` GitHub
organisation. The Data-Management-Service has 1,105 commits; `edfi-oneroster` serves OneRoster 1.2
off an Ed-Fi ODS and has 151. Both are Apache-2.0 — the licence tier Globant prefers.

**The stars are 12 and 6, and that is the whole lesson.** This KB's search strategy has been
star-ranked, and standards-body infrastructure does not accumulate stars: it is adopted through
state education agencies and SIS vendors, not through GitHub. Sunbird (41 ★, India's national
stack) is the same phenomenon and was nearly missed for the same reason. **A star-ranked search
systematically cannot see public-sector education infrastructure** — which is precisely the segment
with the budget in this sector.

Two caveats before scoping on it:
- Neither repo has a published release on its GitHub Releases page. Pin to a commit, not a tag.
- Ed-Fi is a **North American** standard in practice (US state education agencies). It is not a
  route into EMEA, APAC or LATAM rostering, and nothing equivalent was found for those regions.

## Caveats

- **Sunbird's 41 ★ are not a quality signal**, for the same reason Ed-Fi's 12 are not. Government
  adjacent infrastructure in India, adopted through state deployments. Verify the wider
  `Sunbird-Ed` org's component repos before scoping — the portal is one piece of a larger stack.
- **`ai-agents-for-beginners` is a curriculum, not a library.** It sits here deliberately: 77.5k ★
  of MIT teaching material is a reusable asset for the "train the client's team" phase that ends
  most education engagements.
- **LightRAG + DeepTutor remains the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive, ~82k ★ between them, covering retrieval and tutoring. Pattern P1 is built on it.
- **Licence split: MIT (6), Apache-2.0 (3), BSD-3-Clause (2) — 11/11 permissive.** As with the agent
  tier. The copyleft in this industry lives entirely in the LMS/platform tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). Every engagement rebuilds this. It remains the clearest build-once opportunity
  in the sector and it is listed as such in `intel/market.md`. Note that Ed-Fi gives you the data
  *model* and API, not the consent, retention and disclosure machinery around it.
- **No LATAM-authored foundational repo.** Searched again for Brazilian and Mexican open source
  education infrastructure. The LATAM open source story in 2026 is Latam-GPT (a model, not a
  repo-level foundation) and Kolibri *deployments*, not LATAM-authored code. The LATAM activity
  this pass found is venture-funded and closed-source (Teachy, Ginia, Vetto, Mattilda — see
  `intel/market.md`), which is itself the finding.
- **No EMEA- or APAC-equivalent of Ed-Fi.** Ed-Fi closes the North American rostering gap only.
