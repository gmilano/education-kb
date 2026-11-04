---
industry: education
region: Global
updated: 2026-11-04
---

# 📡 Trends — Education

> What is actually changing in AI + education as of November 2026. Each trend names its evidence and its confidence.

## T1 — The agentic classroom arrives, and it simulates peers

The year's structural shift is from *tutor* to *classroom*. OpenMAIC (Tsinghua, MIT, **42.7k ★**, v1.4.0 released 2026-11-04) generates a full lesson from a topic or document and staffs it with AI teachers **and AI classmates** that speak, draw on a shared whiteboard and argue with each other. DeepTutor (HKU, Apache-2.0, **55.0k ★**) holds the one-to-one position with a persistent learner model.

Together these two repositories hold ~98k stars — more adoption than every other open source education project combined. **Confidence: high** (both verified first-hand this pass).

**Why peer simulation matters:** a one-to-one tutor cannot produce disagreement, and disagreement is where a good deal of learning happens. This is a genuinely new capability, not an incremental one.

## T2 — The reference stack is MCP + LangGraph

OpenMAIC orchestrates with LangGraph. `canvas-mcp` (MIT, 317★) exposes ~102–128 LMS tools over the Model Context Protocol, and `tutor-mcp` packages Bayesian Knowledge Tracing itself as an MCP server. Bloom (MIT, 302★) ships as a Claude Code skill *and* a web app.

The pattern has settled: **pedagogy in MCP servers, orchestration in LangGraph, the LMS left untouched.** That is good news for licence containment (see T6). **Confidence: high.**

## T3 — Usage has outrun governance, and governance is now the buying trigger

86% of education organisations use generative AI and most have no policy. 54% of K-12 students and 92% of university students use AI. In LATAM, >50% of teachers in Chile and Brazil use AI tools while <10% of institutions have formal guidelines (UNESCO).

The consequence for sellers: in 2026 the thing a client lacks is usually **control**, not capability. Governance frameworks, audit trails and policy enforcement are the wedge; the tutor is what gets bought afterwards. **Confidence: high.**

## T4 — Agent deployment is still rare, which is where the work is

The Bridges 2026 survey of K-12 and college leaders found relatively few institutions running agents in daily operations, with leaders explicitly unwilling to give agents access to sensitive student data. Pilots exist for tutoring and enrolment.

The gap between chatbot adoption (near-universal) and agent deployment (rare) is precisely the systems-integration gap. The blocker named by buyers is **data access governance**, not model quality. **Confidence: high** (survey-based).

## T5 — One LATAM deployment is the proof point the industry lacked

A Chilean university reported **194 pedagogical agents across ~100 courses serving 4,600+ students** (February 2026). This is the largest concrete agentic-education deployment surfaced anywhere in this pass — and it is in LATAM, not North America or Europe.

**Confidence: medium** (single secondary source, institution unnamed in the reporting). Worth verifying directly; if it holds, it is the strongest reference case available for the region.

## T6 — Open source education has no permissive platform, only permissive components

Measured this pass across ten platform rows: **nine are copyleft** (GPL-3.0: Moodle, Chamilo, ILIAS, Gibbon; AGPL-3.0: Open edX, Frappe LMS, Veo; ECL-2.0: Sakai; GPL: RosarioSIS), **one is permissive** (Richie, MIT).

Meanwhile every leading *agent* is permissive (MIT or Apache-2.0). The architecture that follows is not a preference, it is forced: **stock platform, permissive agent layer, integrate over REST or MCP.** Modifying an AGPL platform for a managed service pulls network-disclosure obligations onto the service. **Confidence: high** (licence payloads read byte-for-byte).

## T7 — The EU's high-risk deadline moved to December 2027, and most guidance is stale

The Digital Omnibus (Regulation (EU) 2026/1744) deferred high-risk obligations for stand-alone education AI from 2 August 2026 to **2 December 2027**. Article 50 transparency duties still apply from 2 August 2026. Emotion recognition in schools has been banned since February 2025. Article 4's AI-literacy duty was softened to "taking measures".

**Most published guidance still cites August 2026 and is wrong.** That is itself a commercial opening: clients working from stale advice are either over-panicking or mis-scoped. **Confidence: medium** — multiple secondary sources agree, but Commission primary text was not read this pass. Verify before quoting to a client.

## T8 — Regulation is diverging by region, not converging

| Region | Shape |
|---|---|
| EMEA | Horizontal, binding, risk-tiered, dated |
| North America | Sub-national patchwork: 134+ bills across 31 states |
| APAC | Service-by-service (China), labelling-first (India), voluntary (Japan) |
| LATAM | Largely pending; only Peru enacted |

A single global compliance posture is no longer achievable. Multi-region clients need per-jurisdiction policy nodes in the agent itself — a concrete architectural requirement, not a legal footnote. **Confidence: high.**

## T9 — Knowledge tracing is still research-grade, not productised

pyKT (MIT) is the field's reference implementation at **457 stars** — not the 1.2k this KB previously published. OATutor (MIT, 276★) is the main production-grade BKT system. `tutor-mcp` packages BKT as an MCP server but has **0 stars**.

The honest read: knowledge tracing is scientifically mature and commercially immature. Budget real integration effort; do not promise adaptive mastery modelling as an off-the-shelf component. **Confidence: high** (star counts measured directly). This corrects an over-optimistic trend entry this KB carried previously.

## T10 — The evidence base remains the sector's weak point

A July 2026 scoping review of **474 studies** found the field fragmented, with pedagogical design poorly connected to technical capability. A 2025 study found AI tutors adapt worse in real time than human tutors, following predictable response patterns.

Sophisticated buyers know this, which is why 2026 procurement favours measured pilots. **Ship with measurement attached** — pre/post assessment, retention tracking, teacher time saved. An engagement that cannot show an effect will not renew. **Confidence: high.**

## T11 — Public support for banning AI in schools is rising in parts of APAC

Ipsos Education Monitor 2026, support for a ban: South Korea 31%, Japan 29% (**up from 21%**), Malaysia 29%, Singapore 28%, India 26%, Thailand 25%, Indonesia 23%; Australia and New Zealand higher still.

Roughly a quarter to a third of the public in major APAC markets would ban AI in schools outright. Visible, teacher-in-the-loop designs are the commercially safer posture there. **Confidence: high** (single reputable polling source).

## 🔴 What this page does not claim

- **No verified star counts for `richie`, `chamilo-lms` or `sakai`** this pass; licence payloads were read, stars were not.
- **The "agentic university" framing** carried by earlier versions of this page rested on a single arXiv preprint. It is a useful taxonomy, not measured adoption, and has been demoted accordingly.
- **No evidence was found of a dominant open source assessment-integrity or proctoring tool.** Given this is the most heavily regulated use case in the sector, the absence of permissive supply is notable and is recorded as a gap rather than a finding.
