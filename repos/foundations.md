---
industry: education
region: Global
updated: 2026-10-19
---

# Foundational repos — education

**Pass 315 · 2026-10-19.** Nine repos, each verified first-hand this pass. "Foundational" here
means: you would put it *under* an education product, not ship it as the product.

| Repo | Licence | ★ (2026-10-19) | Layer | Why it is foundational |
|---|---|---|---|---|
| https://github.com/HKUDS/LightRAG | MIT | 40.2k | Retrieval | Simple, fast RAG (EMNLP 2025). The course-material grounding layer under a tutor; same lab as DeepTutor, so the two compose without friction |
| https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | Agent runtime | Minimal code-thinking agent loop; small enough to audit, which matters when a ministry asks how the tutor decides |
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Compute | Multi-user notebook server — the delivery substrate for every CS/data curriculum, and what nbgrader and otter-grader plug into |
| https://github.com/microsoft/ai-agents-for-beginners | MIT | 77.5k | Enablement | 18 lessons on building agents. Not a dependency — the fastest way to bring an engagement team to a shared baseline |
| https://github.com/learningequality/kolibri | MIT | 1.2k | Offline delivery | Offline-first learning platform for universal education. The only MIT platform in the sector and the one that works without connectivity |
| https://github.com/open-spaced-repetition/fsrs-rs | BSD-3-Clause | 447 | Scheduling | FSRS optimiser and scheduler in Rust — embeddable retention scheduling, no Anki dependency |
| https://github.com/openfun/richie | MIT | 316 | Portal/CMS | Education-portal CMS from France Université Numérique. MIT, EMEA-authored, built to front Open edX |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | Integration | LTI 1.3 Advantage tool implementation. This is the repo that gets your agent *into* the client's existing LMS |
| https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | Platform (APAC) | Web portal of Project Sunbird, the stack behind India's national digital-education infrastructure. MIT, low stars, national scale — read the caveat |

## Caveats

- **Sunbird's 41 ★ are not a quality signal.** It is government-adjacent infrastructure in India,
  where adoption happens through state deployments rather than GitHub stars. It is in this table
  because it is the one MIT-licensed platform placed in APAC, which makes it the natural base for an
  India engagement. Verify the wider `Sunbird-Ed` org's component repos before scoping — the portal
  is one piece of a larger stack.
- **`ai-agents-for-beginners` is a curriculum, not a library.** It sits here deliberately: 77.5k ★
  of MIT-licensed teaching material is a reusable asset for the "train the client's team" phase that
  ends most education engagements.
- **LightRAG + DeepTutor is the highest-leverage pair in this KB.** Both from HKUDS, both
  permissive (MIT and Apache-2.0), 82k ★ between them, and they cover retrieval and tutoring
  respectively. Pattern P1 in `compose/patterns.md` is built on exactly this.
- **Licence split: MIT (6), BSD-3-Clause (2), Apache-2.0 (1) — 9/9 permissive.** As with the agent
  tier. The copyleft in this industry lives entirely in the LMS/platform tier.

## Declared gaps — searched, not found

- **No foundational open source repo for student-data privacy compliance** (FERPA / COPPA / GDPR
  record handling). Every engagement rebuilds this. It is the clearest build-once opportunity in
  the sector and it is listed as such in `intel/market.md`.
- **No LATAM-authored foundational repo.** Searched for Brazilian and Mexican open source
  education infrastructure specifically and found none at this tier. The LATAM open source story in
  2026 is Latam-GPT (a model, not a repo-level foundation — see `intel/market.md`) and Kolibri
  *deployments*, not LATAM-authored code. Stated so the gap is visible rather than silent.
- **No open source OneRoster / Ed-Fi reference implementation** found at a usable maturity. SIS
  sync remains vendor-specific integration work in every region.
