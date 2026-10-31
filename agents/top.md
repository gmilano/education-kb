---
industry: education
region: Global
updated: 2026-10-31
---

# Top AI agents for education

Every row below was verified first-hand on 2026-10-31 by reading the repository
page itself. Licence, star count and description are what the repo states — not
what an aggregator or listicle reports. Where a repo's sidebar and README
disagree, both readings are given.

**Six agents qualified.** That is the real count, not a target. Two candidates
found during this run were rejected and are listed under *Rejected* with the
reason, because an informed rejection is worth more than a padded table.

## The shelf

| Agent | Repo | Licence | ★ | Region | What it is |
| --- | --- | --- | --: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 52,000 | APAC | Lifelong personalised tutoring. Multi-agent pipelines (`Deep Solve`, `Deep Research`) over LLM + RAG. `v1.7.0`, dated 2026.10.28. Data Intelligence Lab, University of Hong Kong. Docker image at `ghcr.io/hkuds/deeptutor`. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 310 | North America | The most established Canvas LMS MCP server. Sidebar says "up to 102 tools and 8 agent skills"; README says 128 tools. `v1.16.0` (Oct 2026), 1,206 commits on `main`. Ships agent skills incl. pre-semester course audit and accessibility auditor. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America | Open-source intelligent tutoring system with Bayesian Knowledge Tracing, in React + Firebase. Published at CHI '23. Owning org is CAHLR; a UC Berkeley connection is indicated by the authors and a Berkeley press link but is not stated on the repo page. |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | MIT claimed in README only — **no LICENSE file in the repo** | 104 | North America | Canvas LMS API MCP server, `v2.2`, 54 tools, runnable as a container. TypeScript by file layout (`tsconfig.json`); the Languages panel is empty. **Licence defect, verified 2026-10-31 (second pass):** the README says "MIT License - see [LICENSE](LICENSE) file for details", but that file does not exist — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING` and `license` all return 404 on both `main` and `master`. The grant is a README sentence pointing at a missing file. Treat as licence-unresolved until the maintainer adds it; prefer `vishalsachdev/canvas-mcp` (MIT, LICENSE present). |
| moodle-mcp | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | 27 | APAC | Rust MCP server letting agents operate Moodle: courses, assignments, forums, grades, files-as-markdown. Validated live against Moodle 3.7 → 5.x. The only Rust implementation found in this field. |
| Pedagogy Benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | Global | Not a tutor — an **evaluator**. 1,143 questions drawn from real teacher-qualification exams: CDPK (920, general pedagogy) and SEND (223, Special Educational Needs and Disabilities). Code for the paper *Benchmarking the Pedagogical Knowledge of Large Language Models*. |

## Why this shelf is shaped the way it is

**The agent layer is permissive; the platform layer is not.** Five of six rows
above are MIT, one is Apache-2.0. Every major platform of record these agents
attach to is copyleft (see [`../repos/foundations.md`](../repos/foundations.md)).
That asymmetry is the single most consequential fact for a Globant engagement:
the integration surface is buildable, the substrate is not forkable on
commercial terms. The composition pattern that follows from it is written up in
[`../compose/patterns.md`](../compose/patterns.md).

**The field clusters on two LMS platforms.** Canvas and Moodle account for five
of six rows. There is no comparable agent population for Blackboard, Brightspace
or Google Classroom — small Brightspace and Google Classroom MCP servers exist
per aggregator listings but none reached the verification bar this run.

**MCP is the dominant integration shape.** Four of six are MCP servers. An
engagement that needs LMS data in an agent should assume MCP as the transport
rather than designing a bespoke connector.

## Rejected this run, with reasons

| Candidate | Why it is not on the shelf |
| --- | --- |
| [NelsonSpencer/canvas-mcp](https://github.com/NelsonSpencer/canvas-mcp) | A **fork** of `vishalsachdev/canvas-mcp` with **0 stars**. Advertises "80+ tools and 5 agent skills" — fewer than the upstream it forked. Use the upstream. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | **AGPL-3.0** and **1 star**. The licence is the disqualifier for a build-on recommendation, not the star count; recorded here so the next pass does not re-discover it. Its design note is still useful: it works through Moodle Web Services, so it needs no plugin install. |
| [braiinz94/braiinz-education](https://github.com/braiinz94/braiinz-education) | **Apache-2.0, 0★, `v0.1 alpha`, 37 commits, no releases.** Found on the second pass of 2026-10-31 while hunting specifically for a non-US/non-APAC agent. It is a *real* project, not a stub — three named agents (Tuteur Socratique, Coach Pratique, Diagnostiqueur with FSRS spaced repetition), French-curriculum pack, PISA-aligned diagnostics, test suite, CI. Code Apache-2.0, educational content CC-BY-SA-4.0. **Not shelved:** 0★ and alpha is below the bar this shelf applies to everyone. Logged as a *watch item* because it is the only EMEA-origin education agent located in two passes, and because a dual code/content licence split is the right shape for curriculum work. Re-check next pass. |

## Declared gaps

- **No published ranking of education AI agents exists.** The prescribed search
  `top open source AI agents education 2026 github MIT` returned only
  general-purpose agent listicles (OpenHands, CrewAI, OpenClaw, OpenAI Agents
  SDK) with an education angle bolted on. This shelf is assembled from
  first-hand repo verification because there was nothing to copy.
- **Aggregator tool counts are unreliable.** `vishalsachdev/canvas-mcp` is
  reported at 99, 102 and 128 tools across its own sidebar, its own README and a
  third-party listing. Treat any tool count as version-specific.
- **Star counts for DeepTutor are moving too fast to cite loosely.** Third-party
  listings ranged from 17.8k to 42k while the repo page itself read 52.0k on
  2026-10-31. Only the repo page figure is used above.
- **LATAM: no LATAM-origin education agent qualified this run.** `ltijs`
  (Apache-2.0, 373★) has a Brazilian maintainer but is spec infrastructure, not
  an agent, so it sits in foundations instead. **Re-searched on the second pass**
  with a Spanish/Portuguese-language query (`open source education AI agent LATAM
  Brazil Spanish github MIT 2026 tutor`): still nothing. The region's flagship
  open-source AI asset is **Latam-GPT** (Chile-led consortium, Spanish and
  Portuguese primary content) — a *model*, not a tutor, and its licence was not
  established from the sources seen. Two independent search strategies now
  support this gap, so treat it as a real absence rather than a missed query.
- **EMEA: no EMEA-origin education agent is on the shelf either** — a regional
  hole not named in the first pass. All six shelved agents are North America
  (3), APAC (2) or Global (1). The only EMEA candidate found in two passes,
  `braiinz94/braiinz-education`, is 0★ alpha (see *Rejected*). For EMEA
  engagements the agent layer is therefore imported; the *attachment* layer is
  local (`openfun/ralph`, MIT, France; H5P, Norway; Tutor, France).
- **Aggregator licence claims are wrong, not just stale.** A second-pass search
  result asserted DeepTutor is MIT. The repository sidebar says **Apache-2.0**,
  which is what this KB records. Same failure mode as the star counts: verify on
  the repo page, never from a listicle.
