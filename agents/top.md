---
industry: education
region: Global
updated: 2026-10-19
---

# Top open source AI agents — education

**Pass 315 · 2026-10-19.** Every row below was verified first-hand this pass by loading the
repository page and reading the licence label and star count GitHub itself displays. Nine rows,
nine real repos. No header rows, no placeholders, no example data.

Star counts are as GitHub rendered them on 2026-10-19 and move fast — treat them as a size signal,
not a metric.

## The table

| Agent | Repo | Licence | ★ (2026-10-19) | What it does | Use it for |
|---|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 41.7k | Lifelong personalised tutoring agent; v1.6.15 shipped 2026-10-19 | The strongest permissive starting point for a tutor product |
| Educhain | https://github.com/satvik314/educhain | MIT | 387 | Python package that generates educational content (MCQs, lesson plans, flashcards) with LLMs | Content-generation pipelines behind an authoring tool |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 268 | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase), from UC Berkeley's CAHLR | Mastery modelling / hint-sequencing where you must explain the pedagogy |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 111 | Educational, collaborative AI tutoring platform; described in arXiv 2602.07176 (Feb 2026) | An academically documented tutor platform you can fork and cite |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assigning, collecting and autograding Jupyter notebooks | Grading automation in any notebook-based curriculum |
| otter-grader | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | 161 | Python and R autograding solution with containerised execution | Autograding where submissions must run sandboxed |
| FSRS4Anki | https://github.com/open-spaced-repetition/fsrs4anki | MIT | 4.1k | Free Spaced Repetition Scheduler as an Anki scheduler | Retention scheduling — the review-timing half of a tutor |
| smolagents | https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | Minimal library for agents that think in code | The agent runtime under a tutor when you want small and auditable |
| AITutorAgent | https://github.com/Ebimsv/AITutorAgent | MIT | 15 | LangGraph tutoring loop: structured tutorial → Q&A → knowledge evaluation | Reference implementation of the loop shape only — see the caveat |

## Caveats a studio lead should read before quoting any of these

- **AITutorAgent is 15 ★ and 4 commits.** It is in the table because the LangGraph tutorial →
  Q&A → evaluation loop is exactly the control flow a tutor engagement needs, and reading 4 commits
  is cheaper than designing it. It is **not** a dependency to ship on. Copy the shape, not the repo.
- **Educhain is 387 ★, and earlier passes of this KB recorded it at "~12k ★".** That number was
  wrong. The sidebar reads 387 today. Its last version marker in the README is v0.3.13 and the
  Releases section is empty, so the project is small and slow-moving — fine for a content-generation
  helper, not a platform bet.
- **DeepTutor is the outlier in both directions.** 41.7k ★ and a release the same day as this pass
  (v1.6.15) make it the most active permissive tutor codebase in the sector; that same velocity
  means pinning a version is mandatory, not optional.
- **The three graders are BSD-3-Clause, not MIT.** Permissive either way and fine for Globant to
  build on, but the attribution clause is real — it belongs in the client's licence inventory.
- **smolagents and FSRS4Anki are not education products.** They are the runtime and the scheduling
  algorithm. They earn their rows because every tutor pattern in `compose/patterns.md` wires one or
  both underneath an education-specific agent.

## Licence split

Permissive across the board: MIT (4 — Educhain, OATutor, FSRS4Anki, AITutorAgent),
BSD-3-Clause (3 — Open TutorAI CE, nbgrader, otter-grader), Apache-2.0 (2 — DeepTutor, smolagents).
**9/9 are licences Globant can build on commercially.** This is the opposite of the platform tier
in `verticals/solutions.md`, which is predominantly copyleft — the split is the single most
important structural fact about this industry's open source, and it drives every pattern:
permissive agents on top, copyleft platform underneath, integration across a network boundary.

## What was searched and not found

- **No region-specific tutoring agent.** Searched for education agents out of EMEA, APAC and LATAM
  specifically; the agent tier above is entirely US/EU-authored or unplaced. The regionally placed
  open source in this sector sits in the *platform* tier (Sunbird for India, Richie for France,
  Kolibri for deployments across the global south) — see `repos/foundations.md`.
- **No dominant open source agent for assessment integrity / AI-detection**, despite that being the
  loudest 2026 procurement question in North America and EMEA. Declared gap, not an omission.
- **No open source LTI 1.3 *agent*.** There is a solid LTI 1.3 library (`pylti1.3`, MIT) but no
  agent that speaks LTI natively — the glue is yours to write in every engagement.
