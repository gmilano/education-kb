---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

**Pass 317 · 2026-10-19.** Eleven repos. "Foundational" here means: you would put it *under* an
education product, not ship it as the product. **Checked** says which pass took the licence/star
reading.

Pass 317 re-verified `pylti1.3` and `smolagents` first-hand and read the former's full service
coverage for the first time — it matters more than it looks, because `pylti1.3` is the single
component every pattern in this KB depends on.

| Repo | Licence | ★ | Checked | Layer | Why it is foundational |
|---|---|---|---|---|---|
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | p315 | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | p316 | Retrieval | Simple, fast RAG (EMNLP 2025), 10,873 commits. The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | p315 | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/learningequality/kolibri | MIT | 1.2k | p316 | Offline delivery | Offline-first learning platform, 39,803 commits on `develop`. The only MIT platform in the sector and the one that works without connectivity |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | p315 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | p315 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | p317 | Integration | LTI 1.3 Advantage tool implementation, 178 commits. Covers **Deep Linking, Assignment & Grade Services, Names and Roles, Course Groups, Submission Review and Data Privacy Launch** — the whole Advantage surface. This is the repo that gets your agent *into* the client's existing LMS |
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
- **`pylti1.3` is the most load-bearing 138 stars in this KB.** Pass 317 read its README in full
  and confirmed it implements the complete LTI Advantage service set, not just launch: Deep Linking
  (so faculty place the tutor as a course activity), AGS (so grades reach the gradebook), NRPS (so
  the agent can see the roster), plus Course Groups, Submission Review and Data Privacy Launch.
  Every pattern in `compose/patterns.md` crosses the LMS boundary through this one MIT library, and
  it is a single-maintainer project with 39 open issues and no visible release cadence.
  **That is the concentration risk in this KB's architecture and it should be named in any SOW that
  depends on it.** Mitigation if it ever matters: the reference implementations are maintained by
  1EdTech members in other languages, and `ltijs` (Node) is the route `blamb/lti-tutor` took.
- **LightRAG + DeepTutor remains the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive, ~82k ★ between them, covering retrieval and tutoring. Pattern P1 is built on it.
- **Licence split: MIT (6), Apache-2.0 (3), BSD-3-Clause (2) — 11/11 permissive.** As with the agent
  tier. The copyleft in this industry lives entirely in the LMS/platform tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). Every engagement rebuilds this. It remains the clearest build-once opportunity
  in the sector and it is listed as such in `intel/market.md`. Note that Ed-Fi gives you the data
  *model* and API, not the consent, retention and disclosure machinery around it.
  **Searched directly in pass 317 and still declared.** Three candidates were found and none
  qualifies: `capetron/ferpa-compliance-checklist` is documentation rather than code;
  `CSOAI-ORG/coppa-ferpa-mcp` is MIT but has 1 star, 16 commits and two contradictory price lists in
  one README (rejected in `agents/top.md`); and `ashutoshrana/haystack-ferpa-filter` (**Apache-2.0,
  0 ★, 41 commits**) is the right *shape* — Haystack components that filter retrieved documents by
  student identity, institution and authorised category before prompt construction, emitting a
  `disclosure_record` for the caller to persist — but at 0 stars it is a design to copy, not a
  dependency to take. Its README is commendably clear that it does not authenticate users or
  establish legal compliance. **Build the FERPA-filtered retrieval step into pattern P1 using that
  shape; do not import it.**
- **No LATAM-authored foundational repo — fifth pass declaring it, now with a measured backdrop.**
  The **Linux Foundation's December 2025 report on open source AI in Latin America** found
  **Mexico (65%) and Brazil (46%) lead the region in organisational use of open source AI** — so
  consumption is high while authorship of education infrastructure stays absent, which is the
  sharper version of this finding. The OEI/ProFuturo mapping's named LATAM education-AI examples
  (**Letrus**, Portuguese-language writing, Brazil; **MusíGlota**, English learning, Chile) are
  private-sector and not open source. Searched again for Brazilian and Mexican open source
  education infrastructure. The LATAM open source story in 2026 is Latam-GPT (a model, not a
  repo-level foundation) and Kolibri *deployments*, not LATAM-authored code. The LATAM activity
  this pass found is venture-funded and closed-source (Teachy, Ginia, Vetto, Mattilda — see
  `intel/market.md`), which is itself the finding.
- **No EMEA- or APAC-equivalent of Ed-Fi.** Ed-Fi closes the North American rostering gap only.
