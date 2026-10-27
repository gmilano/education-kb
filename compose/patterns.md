---
industry: education
region: Global
updated: 2026-10-27
---

# Compose patterns — concrete education AI recipes

**Pass `p490` — reads of 2026-10-27.** Rewritten this pass; 77 prior pass-sections preserved in
[`archive/2026-10-27-p490-pre-rewrite/patterns.md`](../archive/2026-10-27-p490-pre-rewrite/patterns.md).

Every component below is a row verified this pass in [`agents/top.md`](../agents/top.md),
[`repos/foundations.md`](../repos/foundations.md) or
[`verticals/solutions.md`](../verticals/solutions.md) — real repo, license read from bytes at a
pinned SHA.

**Read the licence column as a deployment constraint.** A pattern marked 🟢 can ship as a closed
hosted derivative. A pattern marked 🔴 cannot, and the obligation is named.

---

## P490-1 — Canvas agent assistant for US higher ed 🟢

**Why:** Canvas dominates US higher ed and is the only incumbent LMS with a maintained agent tool
surface. Fastest path to a working engagement in the largest market.

| Component | Repo | License | Role |
|---|---|---|---|
| Tool surface | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | ~102 Canvas tools + 8 agent skills over MCP |
| Agent loop | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | code-writing agent runtime |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | quizzes, lesson plans, flashcards |

**Wiring:** run `canvas-mcp` against the institution's Canvas API token → expose as MCP tools to a
`smolagents` agent → `educhain` generates assessment items that the agent writes back through
`canvas-mcp`'s content tools.

**Do this or it is negligent:** start from `canvas-mcp`'s **read-only** tool subset
(`get_*`/`list_*`), enable write tools individually through its operator allowlist, and treat its
published advisory **GHSA-hmr8-mvr2-mvw5** as the threat model. Its own source makes the point to
honour: *a confirmation token does not prove a human approved anything.* Put a human gate on
anything that writes a grade.

**Licence note:** Canvas itself is AGPL-3.0, but you are **integrating over its API, not
modifying it** — no obligation attaches. All three components above are permissive. 🟢

**Scope:** 4–6 weeks to a governed pilot on one faculty.

---

## P490-2 — EU-conformant tutor where Globant is the provider 🟢

**Why:** under the EU AI Act the vendor is the **provider** and carries the conformity duties.
Education tutoring that touches assessment or admissions is high-risk. The Digital Omnibus moved
that deadline to **2 Dec 2027** — but Article 50 transparency still bites **2 Dec 2026**.

| Component | Repo | License | Role |
|---|---|---|---|
| LMS base | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | the only permissive full LMS; closed derivative permitted |
| Tutoring engine | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | graph-RAG lifelong tutoring |
| Mastery model | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | Bayesian Knowledge Tracing — an *auditable* learner model |
| Governance substrate | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | governed, authoritative knowledge with provenance |

**Wiring:** OpenOlat holds courses and enrolments → DeepTutor serves tutoring over course
material → OATutor's BKT maintains per-skill mastery as the explainable learner state → KSoR
holds the authoritative curriculum so every tutor claim is traceable to a source.

**Conformity work that is the actual deliverable:**
1. **Article 50 content marking by 2 Dec 2026** — mark every AI-generated artefact. Nearest
   real deadline.
2. **Human oversight** on assessment and progression decisions; BKT is chosen over an opaque
   model precisely because a learner model that determines an educational path must be explainable.
3. **Technical documentation + logging** from day one — provider duties, not retrofits.
4. 🔴 **Ship no emotion recognition, attention tracking or sentiment detection.** Banned in
   education in the EU since 2 Feb 2025. Audit the roadmap for it.

**Licence note:** all four permissive — closed hosted derivative is clean. 🟢

**Scope:** 10–14 weeks. Verify Omnibus dates against EUR-Lex before contracting.

---

## P490-3 — Offline-first ministry deployment for LATAM / APAC 🟢

**Why:** LATAM shows the highest measured individual adoption (56% of Brazilian secondary
teachers vs 36% OECD; 92% of LATAM HE students) against the weakest institutional delivery (30%
satisfaction). Public money sits in ministry programmes, and connectivity cannot be assumed.

| Component | Repo | License | Role |
|---|---|---|---|
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | offline-first, the only permissive one |
| Lesson structure | [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | explorations with misconception handling |
| Study-pack generation | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | source → quizzes + flashcards + SRS |
| SRS scheduling | [ankitects/anki](https://github.com/ankitects/anki) | AGPL-3.0 | **reference only — see note** |

**Wiring:** generate study packages **centrally, online** with `Skill-Anything` over the
ministry's approved curriculum → ship them into Kolibri's offline content channels → Oppia
explorations carry the interactive remediation → spaced repetition schedules review locally with
no network.

**The licence line that matters:** Kolibri, Oppia and Skill-Anything are permissive 🟢. **Anki is
AGPL-3.0** — use it as an *algorithm reference* and implement the scheduler, or accept the AGPL
obligation. Do not vendor Anki code into a closed deployment. 🔴

**Regional fit:** Portuguese/Spanish first. Align to the **UNESCO Observatory on AI in Education
for LATAM & the Caribbean** (launched 14 Apr 2026) and the **CONALEP/DGETI** centre-of-excellence
pilot in Mexico. Note there is **no LATAM AI statute** to sell conformity against — sell delivery.

**Scope:** 8–12 weeks per ministry pilot; content pipeline is the long pole, not the app.

---

## P490-4 — Jurisdiction-routing provenance layer for APAC 🟢

**Why:** APAC is the fastest-growing region (35.3% CAGR) with the least public resistance, but
four incompatible regimes. Content labelling is **mandatory in China and India**, absent in
**Japan**, and South Korea's AI Basic Act has been binding since **22 Jan 2026**. One product
must behave differently per market.

| Component | Repo | License | Role |
|---|---|---|---|
| Agent loop | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | runtime |
| Provenance / authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | source-of-truth + provenance records |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | material generation |
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | delivery |

**Wiring:** every generated artefact gets a KSoR provenance record at creation. A policy module
keyed on deployment jurisdiction then decides the output treatment:

| Market | Behaviour required |
|---|---|
| India | prominent AI label + provenance marker (live **20 Feb 2026**) |
| China | AI-content label + service **filing** before launch |
| South Korea | AI Basic Act obligations (binding **22 Jan 2026**) |
| Japan | no binding duty — label anyway, cost is zero |

**Beachhead:** South Korea for a compliance-first pitch (only comprehensive mandatory APAC law);
India for volume.

**Licence note:** all permissive. 🟢 **Scope:** 12–16 weeks across three markets.

---

## P490-5 — Policy-configurable K-12 assistant for the US patchwork 🟢

**Why:** ~34 states plus DC and Puerto Rico have AI guidance, and the enacted laws demand
*different* things. One assistant with per-district policy configuration beats 34 forks. There is
**no federal law** — H.R. 8747 advanced in committee only, so do not plan around it.

| Component | Repo | License | Role |
|---|---|---|---|
| LMS base | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | AI-native LMS; multi-tenant via Postgres RLS |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | lesson plans, assessments |
| Mastery model | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT, explainable |
| Canvas bridge | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | where the district runs Canvas |

**Wiring:** `mentingo`'s Postgres **row-level security** is the load-bearing choice — tenant
isolation is enforced in the database, not in application code, so a district is a tenant and its
policy settings cannot leak across. Each tenant carries a policy record:

| Policy toggle | Driven by |
|---|---|
| Parent opt-out | Oklahoma **S.B. 1734** |
| AI-literacy standards + mandatory local policy | Idaho **S.B. 1227** |
| State guidance alignment | Maryland **S.B. 720** |
| Grade-band restriction (e.g. no genAI for K-6) | district rule — Katy ISD pattern |
| Human-oversight gate on high-stakes decisions | recurring across states |
| "Learning aid, not submitted work" | Columbia Law pattern (HE) |

**Licence note:** all four MIT 🟢 — closed hosted derivative is clean, which matters since this is
a SaaS-shaped product.

**Scope:** 6–10 weeks to a two-district pilot.

---

## P490-6 — Open education-AI evaluation harness (build, not compose) 🟡

**Why:** this is the sector's largest structural gap. **No open-source education-AI evaluation
harness above 60★ exists** — every instrument found sits below that floor, so every star-ordered
search is blind to the tier, and nobody can currently demonstrate that an AI tutor improves
outcomes. Buyers in all four regions are starting to ask, and EU high-risk conformity will
require evidence by **2 Dec 2027**.

| Component | Repo | License | Role |
|---|---|---|---|
| Ground-truth mastery | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT as the reference learner model |
| Item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | generate assessment items at volume |
| Curriculum authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | authoritative answer keys with provenance |
| Harness runtime | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | drive candidate tutors under test |
| Subject under test | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | first candidate |

**Wiring:** KSoR holds curriculum + answer keys → `educhain` generates held-out item banks →
`smolagents` drives each candidate tutor through simulated learner trajectories → OATutor's BKT
scores mastery gain against the key → report per-skill learning gain, not token overlap.

🟡 **Marked amber deliberately:** unlike P490-1 to P490-5 this composes no existing harness,
because none exists. It is a build on permissive parts. That is also why it is the strongest
differentiator in this file — and it would close the gap this KB has carried for dozens of passes.

**Licence note:** all permissive. 🟢 Could be published as open source as a credibility asset.

**Scope:** 10–14 weeks for v1 on one subject domain.

---

## Patterns deliberately **not** offered

- **Nothing on Moodle or Open edX at the agent layer.** Neither has an MCP/tool surface at a
  usable star floor; the connector is unbudgeted build work. Use P490-1 (Canvas) where possible
  and price the connector explicitly otherwise.
- **No closed SaaS on an incumbent LMS fork.** Moodle is GPL-3.0; Open edX, Canvas, Frappe LMS
  and Tutor are **AGPL-3.0** — hosting a modified copy owes source to users. Only OpenOlat,
  Kolibri, Oppia and mentingo support that shape.
- **No closed SIS or assessment product.** Every SIS found (`rosariosis` GPL-2.0, `GibbonEdu`
  GPL-3.0, `openeducat_erp` LGPL-3.0) and the only real assessment engine (`tao-core` GPL-2.0)
  are copyleft. There is no permissive base — it is a ground-up build.
- **Nothing using `ChatTutor` (AGPL-3.0) or `tutor-gpt` (GPL-3.0)** in a hosted commercial
  pattern, despite both being capable. Named here so the omission is visible rather than silent.
