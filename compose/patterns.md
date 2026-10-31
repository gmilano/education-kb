---
industry: education
region: Global
updated: 2026-10-31
---

# Compose patterns — education

Concrete recipes. Every component is a repo verified first-hand on 2026-10-31
with its licence named, and every pattern obeys the one hard constraint of this
industry: **the platform of record is copyleft, so you attach to it, you do not
fork it.**

Shared rule for all five patterns — the licence boundary:

```
  [ client's LMS of record ]          GPL-3.0 / AGPL-3.0  ← never forked, never patched
   Moodle | Open edX | Canvas | Chamilo | i-educar
            │
            │  attach ONLY across a standard, permissively licensed boundary:
            ├── LTI 1.3 ....... Cvmcosta/ltijs        Apache-2.0  (launch + grades back)
            ├── MCP ........... canvas-mcp/moodle-mcp MIT         (agent reads LMS data)
            └── xAPI → LRS .... adlnet/xAPI-Spec      Apache-2.0  (telemetry out)
                                openfun/ralph         MIT
            │
  [ Globant-built layer ]             your licence, your IP
```

---

## P-568-A — LTI-attached AI tutor over a copyleft LMS (6–8 weeks)

**For:** any client on Moodle, Open edX, Canvas or Chamilo who wants AI tutoring
inside their existing LMS without a platform migration or a licence problem.
**Regions:** all. This is the default engagement shape.

**Wiring:**
1. **Tutor core** — [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
   (Apache-2.0, 52k★, `v1.7.0`). Deploy from `ghcr.io/hkuds/deeptutor`. Apache-2.0
   permits commercial use and the derivative stays yours.
2. **Mastery model** — [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT).
   Take its **Bayesian Knowledge Tracing** implementation as the per-skill
   mastery estimator rather than letting the LLM self-assess mastery. This is the
   step that makes the tutor defensible under "proven instructional benefit."
3. **Attachment** — [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs)
   (Apache-2.0). Wrap the tutor as an LTI 1.3 tool provider: Deep Linking so
   instructors place it in a course, Names and Role Provisioning for roster and
   role, **Assignment and Grade Services to write results back to the gradebook**.
   Zero lines of LMS code modified.
4. **Telemetry** — emit [xAPI](https://github.com/adlnet/xAPI-Spec) (Apache-2.0)
   statements into [`openfun/ralph`](https://github.com/openfun/ralph) (MIT) as
   the LRS.
5. **Acceptance gate** — score the tutor on
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) **before** go-live and keep the score as release evidence.

**Why it holds up:** steps 1–5 are Apache-2.0/MIT throughout. The client's
AGPL obligations are never triggered because their platform is never modified.

---

## P-568-B — Canvas agent fleet with a read-only default (3–4 weeks)

**For:** institutions on Canvas wanting agent access to course data for staff and
students. **Region:** North America primarily (Canvas's install base, and the
verified agents are North American).

**Wiring:**
1. **Base server** — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, 310★, `v1.16.0`). The most established option; also ships ready-made
   agent skills — **pre-semester course audit** and **accessibility auditor** —
   which are deliverables on their own and the fastest demonstrable value here.
2. **Lean alternative** — [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms)
   (MIT per README, `v2.2`, 54 tools) where a smaller, containerised surface is
   preferred over maximum coverage.
3. **Write-surface decision, made explicitly.** Tool counts here run from 54 to
   128 and some tools mutate LMS state (submit, grade, delete). Enumerate the
   tool list of the exact version you deploy, classify each tool read vs. write,
   and **expose the read set by default**; every write tool is enabled
   deliberately, per role, never by default. Do not infer the surface from the
   README — tool counts are version-specific and the README and sidebar of the
   same repo disagree.
4. **Grades stay on the sanctioned path.** Writes back to the gradebook go
   through LTI AGS (`ltijs`), not through an MCP write tool — AGS is the
   auditable, spec-sanctioned channel.
5. **Audit** — xAPI → `ralph`, so every agent action against student data is
   reconstructible. This is what satisfies a district AI policy.

---

## P-568-C — District AI policy instrumentation, North America (8–10 weeks)

**For:** US districts and state education agencies. **Region:** North America.
**Driver:** Maryland, Idaho, Oklahoma and Virginia now **require** state guidance
*and* district-level AI policy adoption; 134 bills across 31 states in 2026. Most
US public schools have no formal student AI policy. This is statutory work
districts cannot self-serve.

**Wiring:**
1. **Policy → machine-checkable rules.** Translate the district's adopted AI
   policy into enforceable predicates, not a PDF. The NY A 9190 shape —
   classroom AI restricted to **grade 9 and above, with exceptions for
   diagnostics and special education** — is the worked example: it requires
   per-cohort age gating plus a documented exception path.
2. **Enforcement point** — the MCP layer from **P-568-B**. Roster and role come
   from LTI Names and Role Provisioning (`ltijs`, Apache-2.0), so grade-level
   gating is driven by the SIS's own data rather than a hand-maintained list.
3. **Evidence layer** — xAPI into `ralph` (MIT), retained as the compliance
   record: who used which AI tool, in which course, under which policy version.
4. **Instructional-quality evidence** — `pedagogy-benchmark` (MIT) scores on any
   tool the district approves, including the special-educational-needs subset
   (**SEND, 223 questions**), which maps directly onto the special-education
   exception the statutes carve out.
5. **Deliverable.** Policy document, enforcement configuration, audit pipeline,
   and a per-tool evaluation report — the four artefacts a district needs to show
   it complied.

**Procurement note:** the contested USD 10 m Khanmigo earmark in North Carolina
SB 1006 shows large single-vendor AI tutoring buys are politically exposed.
Platform-neutral, policy-first work is the easier sell.

---

## P-568-D — EU AI Act Annex III conformity package (10–12 weeks)

**For:** EMEA institutions and edtech vendors whose systems evaluate learners or
affect access to qualifications — **Annex III high-risk** under the EU AI Act.
**Region:** EMEA.

**Timing, which is the whole reason to run this now:** stand-alone Annex III
obligations were **deferred to 2027-12-02** (Digital Omnibus, in effect late July
2026), and embedded-in-product to 2028-08-02. That is a ~14-month readiness
runway. Guidance still claiming August 2026 is superseded.

**Wiring:**
1. **Substrate choice matters here.** Where the client wants a
   licence-clean European build rather than an attachment,
   [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0 per
   README badge, Switzerland) is the only permissively licensed institutional LMS
   verified in this KB. Otherwise attach to Moodle via `ltijs` as in P-568-A.
2. **Human oversight, built in, not bolted on.** Implement the
   lesson-plan/assessment flow as **draft-for-teacher-review** — the shape
   Educativa reports the market converging on and the shape Annex III requires.
   The teacher's approval event is an xAPI statement, so oversight is evidenced
   rather than asserted.
3. **Evaluation evidence** — `pedagogy-benchmark` (MIT) gives reproducible,
   documented pedagogical-knowledge scores for the technical documentation pack.
4. **Telemetry under data-protection constraint** — self-host `ralph` (MIT) in
   region; xAPI's actor model lets you pseudonymise the learner at emission.
5. **Package** — risk classification memo, human-oversight design, technical
   documentation, evaluation results, post-market monitoring plan.

**Also in scope for EMEA:** the December 2026 ban on certain AI-generated
intimate imagery and abuse material — a content-safety obligation on any
deployment handling student-generated media, and it lands *before* the high-risk
duties.

---

## P-568-E — LATAM institutional AI strategy, from 87% use to 26% strategy (6–8 weeks)

**For:** Latin American universities and ministries. **Region:** LATAM.
**Driver:** UNESCO IESALC / UNU-IAS across 200 institutions in 19 countries —
**87% already use AI somewhere, only 26% have a formal strategy**, with adoption
driven by individuals rather than institutions. The client's problem is not
starting; it is that it already started without them.

**Wiring:**
1. **Shadow-use census first.** The engagement opens by measuring what is
   already in use, because individual-led adoption means nobody has the list.
   `ralph` (MIT) as LRS plus xAPI emission from sanctioned tools turns shadow use
   into an inventory.
2. **Strategy artefacts on UNESCO's own recommendations** — fold higher education
   into the national AI strategy, develop institutional guidance, fund it, and
   **integrate AI literacy and governance into accreditation and quality
   assurance**. That last one is the procurement wedge: accreditation is already
   a budgeted, calendared institutional function, so the work attaches to an
   existing budget line rather than requesting a new one.
3. **Public-sector build path, Brazil** —
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (**GPL-2.0**,
   722★) is the reference municipal platform for *Secretarias de Educação*.
   GPL-2.0 means the AI layer attaches over LTI/xAPI; an i-educar fork would have
   to be released.
4. **Spanish/Portuguese-language capability** — Chamilo (GPL-3.0) has a notable
   LATAM and francophone install base and is a second common platform of record.
5. **Convening route** — the **UNESCO Observatory on AI in Education for Latin
   America and the Caribbean**, launched 2026-04-14 in Santiago with **CAF**
   (Development Bank of Latin America and the Caribbean). Partners include CENIA
   (Chile), Cetic.br (Brazil), ECLAC, Fundación Ceibal (Uruguay), Fundación
   Santillana, Tecnológico de Monterrey, ProFuturo and IRCAI. A funded regional
   body with a named partner list is a better entry point than institution-by-
   institution outreach.

---

## APAC note — no standalone pattern, and why

APAC is the most deadline-driven region (Korea's AI Basic Act in force
2026-01-22; Vietnam effective 2026-03-01 reaching systems live before
2026-08-15 and naming education/automated assessment explicitly; TEQSA action
plans required of all Australian providers), but it needs **P-568-D run per
jurisdiction** rather than a distinct recipe — the conformity artefacts are the
same, the thresholds differ by country.

Two APAC-specific build notes:
- **Moodle is an APAC product** (Moodle HQ, Perth, Australia). Moodle depth is a
  home-region capability here, not an import.
- [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (MIT, Rust) is the
  verified APAC-origin Moodle agent, validated against **Moodle 3.7 → 5.x** —
  useful precisely because APAC institutional Moodle estates run old versions.
- Avoid [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)
  for build-on work (**AGPL-3.0**), but borrow its design choice: it works through
  **Moodle Web Services**, so it needs no plugin installed on the client's server
  — which matters when you cannot get change-control approval on the LMS.

## Declared gaps

- **No pattern for Blackboard, Brightspace or Google Classroom.** No agent
  population for these platforms reached verification this run, so no recipe is
  offered rather than a speculative one.
- **No Africa-specific pattern.** No African education-AI findings surfaced this
  run; `learningequality/kolibri` (MIT, offline-first) is the obvious component
  for low-connectivity deployments but the regional demand evidence is missing.
