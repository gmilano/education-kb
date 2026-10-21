---
industry: education
region: Global
updated: 2026-10-21
---

# Education — current trends

Researched **2026-10-21**. Trends 1–6 are corroborated across external sources.
Trends 7–10 are **first-hand observations from this pass's own repository
measurements** — they are not in the trade press yet, which is precisely why they are
worth holding.

---

## 1. From pilots to governance

The single most consistent signal across every source. 2026 is the year AI in
education stops being a pilot portfolio and becomes governed infrastructure: explicit
policies, data boundaries, oversight. 1EdTech names the shift directly; Campus
Technology's panel expects AI embedded across admissions, advising and learning.

**Consequence for a studio:** the deliverable that wins is the one with an audit
trail, not the one with the best demo.

## 2. Evidence becomes a procurement gate

HolonIQ expects *selective* acceleration in 2026, with education systems demanding
**proof that a product improves learning quality** before buying. This is new: for
three years capability alone sold.

**Consequence:** instrumentation is a feature. Randomised in-LMS experimentation
([`terracotta`](https://github.com/terracotta-education/terracotta), Apache-2.0) moves
from academic curiosity to commercial necessity.

## 3. Purpose-built beats general-purpose

The market is moving away from generic assistants toward platforms built for
education — curriculum-aligned, rubric-aware, standards-mapped. A wrapper around a
frontier model is no longer a product.

## 4. Agentic and adaptive, not conversational

Sources describe agents that **plan and draft teaching materials** and adaptive
systems that adjust difficulty in real time, with the frontier moving from single
prompts toward multimodal, multi-step systems. The repository evidence agrees: the
fastest-growing education projects this pass are agents with memory and sequencing
([`DeepTutor`](https://github.com/HKUDS/DeepTutor), [`Bloom`](https://github.com/Li-Evan/Bloom),
[`Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent)), not chatbots.

## 5. Regulatory divergence is now a design constraint

Three regions, three regimes, all live in 2026: the **EU AI Act** treats admissions
and assessment AI as **high-risk** under Annex III point 3 — with obligations
**postponed to 2 December 2027** by the Digital Omnibus, **Regulation (EU) 2026/1744**
(in force 27 July 2026), while prohibitions, AI literacy and Article 50 transparency
bind now; the **US**
regulates through **134 state bills across 31 states**; **Korea's AI Framework Act**
(22 January 2026) and **Vietnam's risk-based law** (1 March 2026, education named
high-risk) anchor APAC. A single global product configuration is no longer viable.

## 6. Credentials as the skills-based hiring substrate

1EdTech points to digital credentials becoming a core mechanism for skills-based
learning and hiring. [`learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
(MIT, OpenWallet Foundation) is the open reference implementation.

---

## 7. 🟢 MCP has quietly become the LMS integration layer

**First-hand, this pass.** A `topic:education topic:mcp` query returns **328
repositories**. Counting only what this base actually shelves,
**11 distinct education MCP server slugs are shelved** on `agents/top.md`,
and MCP reaches **6 distinct LMS platforms** across both agent shelves.
Every major LMS now has at least one community MCP server, and **almost all are MIT**:

| Target LMS | Servers found | Licences |
|---|---|---|
| Canvas | [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`canvas-ed-mcp`](https://github.com/r1ckyIn/canvas-ed-mcp), [`canvas-lms-agent`](https://github.com/likr/canvas-lms-agent) | MIT ×3 |
| Brightspace (D2L) | [`brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server), `brightspace-d2l-mcp` | MIT, unclassified |
| Open edX | [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp), [`openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | MIT, AGPL-3.0 |
| Moodle | [`moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | MIT |
| Google Classroom | [`classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | MIT |
| Anki | [`anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | MIT |
| National/institutional portals | [`schoolinfo-mcp`](https://github.com/chrisryugj/schoolinfo-mcp) (KR), [`ku-portal-mcp`](https://github.com/SonAIengine/ku-portal-mcp) (KR), [`mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (BR) | MIT ×3 |

🟢 **And the cross-shelf census is far larger than the live shelf shows.** The
`recount` instrument folds every MCP address across `agents/top.md` **and**
`agents/trending.md`'s full history, case-insensitively, and counts **159 distinct
education MCP server slugs** by platform:

| Platform | Distinct MCP servers shelved |
|---|---:|
| Canvas | **33** |
| Moodle | **19** |
| Google Classroom / Workspace for Education | **12** |
| Blackboard | **7** |
| Brightspace / D2L | **5** |
| Open edX | **3** |
| Anki | **1** |

🔵 **Read the Canvas and Moodle rows as the finding.** Thirty-three independent Canvas
MCP servers and nineteen Moodle ones means this is not a handful of experiments — it is
a crowded, redundant layer. For an engagement that cuts two ways: the connector is
certainly already written, and almost none of these are maintained to production
standard. **Pick and harden, do not write from scratch, and do not trust a random
one.**

**Why it matters more than it looks.** Education's hardest integration problem has
always been reaching the incumbent LMS, whose licence (AGPL for Canvas and Open edX)
makes forking commercially awkward. MCP solves the licence problem *and* the technical
one at once: it is a **protocol boundary**, so copyleft does not reach across it. The
starting cost of an education engagement has dropped materially, and the trade press
has not noticed.

## 8. 🟢 Skills-as-packaging: curriculum shipped as agent instructions

A new distribution format appeared on this shelf: pedagogy packaged as agent skills
rather than as software or content.
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)
(Apache-2.0), [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills)
(Apache-2.0) and [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
(CC-BY-SA-4.0, **165 skills**) all ship evidence-grounded teaching practice as
instructions an agent loads.

🔵 **Note the licence shift this implies:** when the deliverable is prose rather than
code, the grant moves from software licences to **content licences** — CC-BY-SA
carries share-alike obligations that an MIT codebase does not.

## 9. 🟢 Curriculum-as-open-data is the real moat, and it is regionally lopsided

Agents are commoditising; the **curriculum graph underneath them is not**. This pass
verified five substantial curriculum data assets — and their distribution is uneven
in a way that directly shapes engagement strategy:

| Asset | Region | Licence | Usable commercially |
|---|---|---|---|
| [`bncc-dados`](https://github.com/bncc-dev/bncc-dados) — Brazil BNCC, 1 721 objectives | LATAM | MIT | 🟢 Yes |
| [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) — China K-12, 1 244 nodes | APAC | **CC-BY-NC-4.0** | 🔴 **No** |
| [`knowledge-import-pipeline`](https://github.com/clownjee/knowledge-import-pipeline) — textbook → KG | APAC | Apache-2.0 | 🟢 Yes |
| [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — skills/subject taxonomy | — | ODbL-1.0 | 🟡 Yes, share-alike on derivative databases |
| [`knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | North America | MIT code / **gated data** | 🟡 Per dataset |

**Brazil has official national standards as clean MIT data. Spanish-speaking LATAM
has nothing equivalent.** That asymmetry is the most actionable single fact in this
file.

## 10. 🔴 Licence drift away from OSI in education AI

A counter-trend worth tracking, measured first-hand on this pass's own rows. The more
commercially serious an education AI project is, the less likely its licence is
actually open:

- [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (340 ★) —
  **Elastic License 2.0**: source-available, no managed-service rights.
- [`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (1 704 ★) —
  **CC-BY-NC**: the best Chinese curriculum graph, barred from paid work.
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) —
  MIT code, but datasets labelled **Gated** carry **no open licence**.
- [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) — an **IMS
  specification licence**, not a software grant.

🔵 Three of these four read as open source from their GitHub landing page. Licence
due diligence on education AI assets is becoming a billable service in its own right.

## 11. 🔵 A methodological finding, recorded for successors

This base reported **twelve consecutive passes with no new agent row** and published a
denominator defending it. The streak was an artefact of **query shape**: prose legs
("top open source AI agents education 2026") return commercial listicles, while
**topic intersections** (`topic:education topic:llm`, `topic:edtech`,
`topic:education topic:mcp`, `topic:lti`) return repositories. The same channel, asked
differently, produced **26 new verified rows in one pass**.

Generalised: *on this base, a topic intersection is a channel and a prose phrase is
not.* Any future claim of saturation should name which leg shape produced it.
