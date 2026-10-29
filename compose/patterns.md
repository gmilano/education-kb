---
industry: education
region: Global
updated: 2026-10-29
---

## 🆕 `p522` — `2026-10-29` — **🟢 THREE RECIPES, EACH BUILT ON SOMETHING THIS PASS MEASURED RATHER THAN ASSUMED. `P536` is the shelf-attestation gate — the sweep that re-derived 23 of 23 published family+byte cells today, wired as a standing check, and it exists because 8 of those 23 repositories do NOT develop on `main`. `P537` is the EU `2 December 2026` marking build, scoped by WHO the grace actually covers, which the "delayed to 2027" headline buries. `P538` is the retention loop: a fully-MIT spaced-repetition + knowledge-tracing stack, every grant read from bytes today, and it is the layer `P534`'s institutional stack does not have.**

---

### `P536` — Shelf attestation: re-derive every published licence cell, branch-resolved

**Problem it solves.** This base publishes `family` and `bytes` cells to clients and has
historically checked them by hand, one pass at a time. 🔴 `p512` found **39 wrong star cells**
on a single sweep; a wrong *licence* cell is worse, because it decides whether work is legal.
🔴 And a probe that assumes `main`/`master` cannot read **8 of the 23** rows on this shelf.

**Components — all in-repo, no network beyond two public channels:**

| Component | Grant | Role |
|---|---|---|
| [`compose/code/p522-family-resolution/`](code/p522-family-resolution/) | this KB | SPDX family **with version**, posture incl. `PUBLIC-DOMAIN`, 42-check offline suite |
| [`compose/code/p521-commercial-posture/`](code/p521-commercial-posture/) | this KB | Restriction scan — imported, not replaced; its `\b` anchors are load-bearing |
| `git ls-remote --symref` | — | 🟢 Default branch **resolved**, exact HEAD SHA. Works on arbitrary public repos here |
| `raw.githubusercontent.com` | — | 🟢 The only licence-bytes channel open in this session class |

**Wiring:**

1. **Parse the published cells out of the shelf file** — slug, family, byte count — so the check
   never reads the row it is checking from the same sentence that wrote it.
2. **Resolve the default branch** with `git ls-remote --symref <url> HEAD`. 🔴 **Never assume.**
   On this shelf the answer is `develop` three times, `release`, `release_11`, `v31.0.00` and
   `v4.0.x-develop` once each.
3. **Probe the grant path** at that branch across the filename ladder — `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license.txt`, `NOTICE`, then
   [`ingest/probe-grant.sh`](../ingest/probe-grant.sh)'s 14-language set. 🔴 `moodle` answers at
   `COPYING.txt`, `frappe/lms` at `license.txt`.
4. **Grade with `family_resolution.resolve()`**, and compare BOTH cells: family and exact served
   byte count from `curl -w %{size_download}`. 🔵 **Do not measure bytes with
   `printf '%s' "$body" | wc -c`** — it strips a trailing newline and under-reports by 1, which
   is enough to break a byte-identity cell.
5. **Report three verdicts only** — `MATCH`, `DIFFERS`, `UNCHECKED`. An `UNCHECKED` row (channel
   refused) must never be rendered as agreement.

**First run, `2026-10-29`:** 23 rows, **23/23 MATCH on both cells**. Full table in
`repos/foundations.md` `p522`.

**What it costs.** ~2 minutes of network for 23 rows. **Run it on every pass that touches a
shelf**, and before any deck that quotes a licence.

---

### `P537` — The `2 December 2026` marking build, scoped to who the grace actually covers

**Problem it solves.** `P535` built the EU Article 50 marking pack. 🔴 **What it does not do is
tell the client whether the deadline applies to them at all** — and the scope is the whole
decision, because it splits the client's own product line in two.

**The rule, from this window's convergent reading (`intel/market.md` `p522`):**

| The generative system was placed on the EU market… | Marking obligation (Art. 50(2)) |
|---|---|
| **before `2026-08-02`** | 🟡 grace — but it **expires `2026-12-02`** |
| **on or after `2026-08-02`** | 🔴 **no grace at all** — mark from the moment of placement |
| content generated **before `2026-08-02`** | 🟢 no retroactive labelling required (encouraged) |

🔴 **And three Art. 50 duties never had a grace period:** chatbot disclosure, deepfake
labelling, emotion-recognition notification — all live since `2026-08-02`. 🔴 Emotion
recognition in education is **prohibited** outright (Art. 5, since `2025-02-02`, €35 m / 7%).

**Wiring — a two-week engagement, not a programme:**

1. **Inventory by placement date.** Split every generative feature into *pre-* and
   *post-`2026-08-02`*. The post- set is already non-compliant if unmarked; it goes first.
2. **Mark the output, machine-readably.** C2PA-style provenance on generated media; a
   watermark or embedded marker on generated text where the surface allows it; the marker must
   survive the export paths the product actually has (PDF export, LMS upload, print).
3. **Wire the disclosure surfaces** — tutor chat ("you are interacting with an AI system"),
   synthetic media labels, and the removal of any emotion-inference feature from EU education
   deployments. 🔴 Not a banner: a per-surface, per-locale assertion.
4. **Produce the evidence pack** the Annex III work will need in 2027 anyway — model cards,
   data lineage, human-oversight description, logging. 🔵 **Build it now while it is optional;
   it is the same artefact the deferred obligations will demand.**
5. **Cross-check the regional clocks before go-live** against
   [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv): 🇰🇷 Korea (education assessment
   high-impact, in force, penalties ~`2027-01-22`), 🇻🇳 Vietnam (`2027-03-01`/`2027-09-01`),
   🇮🇳 India (content labelling since `2026-02-20`), 🇨🇱 Chile (**Ley 21.719, `2026-12-01`**,
   deferral bill pending).

🔵 **Why it sells.** The client has read that Europe moved education AI to 2027. The thing that
binds them is five weeks out, cheaper than they expect, and reusable in four other
jurisdictions. 🔴 **Price the marking work separately from the Annex III work** — one is due
now, the other is a 2027 programme.

---

### `P538` — The retention loop: a fully-MIT spaced-repetition and mastery stack

**Problem it solves.** `P534` ships a permissive institutional stack — LMS, tutoring agent,
knowledge tracing, classroom. 🔴 **It has no retention layer.** A tutoring agent that cannot
schedule review teaches a session, not a semester, and "did the learner retain it?" is the
question a ministry or a corporate L&D buyer actually pays for.

**Components — every grant read from served bytes `2026-10-29` at the resolved default branch:**

| Layer | Component | Grant | Served | Branch @ HEAD |
|---|---|---|---|---|
| **Scheduler** | [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | `1 079` | `main` @ `ff7c85cee735` |
| **Agent surface over the deck** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** | `1 074` | `main` @ `e0e347f7f399` |
| **Mastery model** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `1 066` | `main` @ `ccbaf37b07e3` |
| **Host + reporting** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **MIT** | `1 062` | `main` @ `e137ca47cbec` |
| **ITS orchestration** | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | 🟢 **CC0-1.0** | `7 048` | `main` @ `79fc182c5d80` |
| **Structured tutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | `1 105` | `main` @ `e24c8456e5f7` |
| **Material → cards** | [`SYuan03/Skill-Anything`](https://github.com/SYuan03/Skill-Anything) | MIT | 🟡 shelf-carried, **not re-read this pass** | — |

🟢 **Zero reciprocity anywhere in the stack, and one component — `gen-mentor` — carries no
attribution duty at all.** 🔴 **Note the family cell:** `p521`'s instrument reads that payload as
`CC-BY`, which would have imposed an attribution obligation the grantor waived. Graded here with
[`p522-family-resolution`](code/p522-family-resolution/).

**Wiring:**

1. **`Skill-Anything` ingests** the client's source material (PDF, video, web, audio) and emits
   quiz items and flashcards. 🟡 Re-read its grant before contracting — this pass did not.
2. **`fsrs4anki` schedules** them. FSRS is the scheduler of record for spaced repetition; take
   the algorithm and the parameter optimiser, not the Anki add-on packaging.
3. **`anki-mcp-server` exposes the deck to the agent over MCP** — so the tutor can *add* a card
   when it detects a gap and *read* due counts before choosing today's activity. 🔵 **This is
   the join that makes the loop agentic instead of a cron job.**
4. **`pykt-toolkit` models mastery** per skill from the review log (DKT/SAKT/BKT family), and its
   output — not the raw review count — gates progression.
5. **`OATutor` handles the structured remediation** when `pykt` says a skill is not mastered;
   **`gen-mentor` orchestrates** the goal-oriented path across skills.
6. **`mentingo` hosts it and reports** — enrolment, cohorts, dashboards, Postgres **RLS** tenant
   isolation, so a multi-institution deployment does not rely on application-layer filtering.

**Where it breaks.** 🔴 Four of the seven components are small single-maintainer repositories —
fork and own them, do not take a runtime dependency. 🔴 `fsrs4anki`'s optimiser expects a review
history; a cold-start cohort has none, so ship with the published default parameters and
re-optimise at ~1 000 reviews. 🟡 EU deployments: a mastery model that gates progression is an
**Annex III learning-path-steering** system — deferred to `2027-12-02`, not exempt (see `P537`).

---


## 🆕 `p521` — `2026-10-29` — **🟢 THREE RECIPES, AND ONE OF THEM REPAIRS AN INSTRUMENT THIS BASE HAS BEEN RELYING ON. `P533` is the licence-clearance gate rebuilt after finding that [`licence-grant-gate`](code/licence-grant-gate/) returns `granted: True` for BOTH repositories `p520` refused — shipped with a 40-check offline suite and served-bytes fixtures. `P534` is the fully-permissive INSTITUTIONAL stack, buildable because `OpenOLAT` is Apache-2.0 and re-confirmed this pass. `P535` is the EU Article 50 marking pack for the deadline five weeks away that the "delayed to 2027" headline is burying.**

---

### `P533` — Licence clearance that cannot be defeated by an incipit

**Problem it solves.** A studio runs one automated licence check before building. `p521` showed
that check is defeated by a grant that opens with the MIT sentence and restricts below it, and by a
`CC` family label that hides the `-NC` variant. 🔴 **Both failures pass code that may not be used
in paid work.**

**Components — all permissive, all read from bytes `2026-10-29`:**

| Component | Grant | Role |
|---|---|---|
| [`compose/code/p521-commercial-posture/`](code/p521-commercial-posture/) | this KB | Posture verdict + cited clause |
| [`compose/code/licence-grant-gate/`](code/licence-grant-gate/) | this KB | Grant existence (run it too — it answers a different question) |
| `raw.githubusercontent.com` | — | The only working licence-bytes channel this session |

**Wiring:**

1. **Enumerate** candidate dependencies from the manifest (`package.json`, `pyproject.toml`,
   `go.mod`), not from a curated list.
2. **Fetch bytes** — `raw.githubusercontent.com/<slug>/<branch>/<file>` across
   **`3` branches × `8` names**: `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING`,
   `COPYING.txt`, `LICENCE`, `license`. 🔵 **Eight names is not padding:** `frappe/lms` serves at
   `license.txt` and `moodle/moodle` at `COPYING.txt`; a two-name probe records both as ungranted.
3. **Read the root listing** when no blob is found. 🔵 **This is what closed `Gap 516-B`:** name
   enumeration can only fail to find, while listing the directory proves there is nothing to find.
   Absence of a grant is a REFUSAL, not an unknown — default copyright is all rights reserved.
4. **Grade** with `licence_grant_gate.verdict()` **and** `commercial_posture.posture_of()`.
   🔴 **Gate them on the second.** Ship only `PERMISSIVE`; route `COPYLEFT` / `WEAK-COPYLEFT` to an
   explicit written acceptance of the reciprocity obligation; **block** `NON-COMMERCIAL`,
   `BESPOKE-RESTRICTED`, `NOT-OSI` and `UNKNOWN`.
5. **Fail closed on disagreement.** Where the two tools differ — exactly the `PageLM` case — stop
   the build and require a human read. 🔵 **The disagreement is the signal.**
6. **Archive the bytes.** Store each payload with its byte count, as
   [`fixtures/`](code/p521-commercial-posture/fixtures/) does, so a later audit re-grades without
   re-fetching and a relicensing is detectable as a byte diff.

🔵 **Never grade from:** a vendor comparison page (wrong twice today — `frappe/lms` "MIT", "no
Apache LMS exists"), a README badge **alone** (a badge is a claim, not a grant — though it is a
cue to re-probe), or GitHub's sidebar label (blank for `PageLM`).

**Effort: 1-2 weeks** to wire into CI. **Run it before the first commit of an engagement, not at
delivery.**

---

### `P534` — The fully-permissive institutional stack

**Problem it solves.** A university or ministry wants a customised, self-hosted LMS with AI
tutoring, and cannot accept a network-copyleft obligation on a hosted modified build. 🔴 **Open edX,
Tutor and `frappe/lms` are all AGPL-3.0** — hosting a modification obliges source release to users.

**Components — every grant read from bytes `2026-10-29`, no reciprocity anywhere in the stack:**

| Layer | Component | Grant | Bytes |
|---|---|---|---|
| **LMS of record** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `10 982` |
| **Tutoring agent** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) `v1.7.0` | **Apache-2.0** | `11 408` |
| **Knowledge tracing** | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `1 066` |
| **Structured ITS** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | `1 105` |
| **Virtual classroom** | [`apache/openmeetings`](https://github.com/apache/openmeetings) | **Apache-2.0** | `51 425` |
| **Course portal** | [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | `1 079` |
| **Offline delivery** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | `1 097` |
| **Pedagogical eval** | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | `1 064` |
| **Capability eval** | [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** | `1 067` |

**Wiring:**

1. **`OpenOLAT` is the system of record** — enrolment, groups, gradebook, assessment. 🔵 **Do not
   replace it with an agent.** Everything below writes back into it.
2. **`Richie` in front** as the public catalogue/portal; `OpenOLAT` stays the authenticated
   interior.
3. **`DeepTutor` as the tutoring surface**, scoped per course. Its lifelong-memory model is the
   reason to prefer it over a bare LLM call — the tutor must persist across a term.
4. **`pykt` behind the tutor** to maintain per-learner mastery estimates; `DeepTutor` reads mastery
   to choose what to practise. 🔵 **This is the join that makes it adaptive rather than
   conversational.**
5. **`OATutor` for structured domains** (mathematics) where Bayesian Knowledge Tracing and a
   problem bank beat free-form dialogue.
6. **`OpenMeetings` for synchronous sessions**, launched from the `OpenOLAT` course context.
7. **`Kolibri` for the offline edge** — where connectivity is the binding constraint, the same
   content ships offline-first and syncs back.
8. **Gate every model change** on `pedagogy-benchmark` (pedagogical quality) **and**
   `lm-evaluation-harness` (capability). 🔵 **Pedagogical quality and raw capability are different
   axes; a stronger model can tutor worse.**
9. **Run `P533` over the whole dependency tree** before shipping.

🟢 **Why this pattern did not exist before `p520`:** this base generalised that *"every deployed LMS
of record is copyleft"*, which made a fully-permissive institutional stack look impossible.
`OpenOLAT` being Apache-2.0 refuted it. 🔵 **Re-confirmed independently this pass from a fresh byte
read.**

**Effort: 10-14 weeks.** 🟢 **Strongest fit: EMEA** (sovereignty and self-hosting pressure) **and
public-sector LATAM/APAC** where redistribution terms are scrutinised.

---

### `P535` — The EU Article 50 marking pack, due `2 December 2026`

**Problem it solves.** 🔴 **Five weeks from today** the grace period for machine-readable marking of
AI-generated content expires. The sector headline — "high-risk delayed to Dec 2027" — is causing
exactly the wrong preparation. **Article 50 was not deferred.**

**Scope — what must be true on `2 Dec 2026` for an EdTech product serving EU learners:**

1. **Interaction disclosure** — a learner talking to a tutoring agent is told it is an AI.
2. **Generated-content marking** — every AI-generated quiz item, feedback comment, summary and
   lesson asset carries a **machine-readable** mark, not only a visible label.
3. **Provenance through the LMS** — the mark survives the agent → LMS → export path. 🔵 **This is
   where implementations fail:** content is marked at generation and the mark is stripped on
   import into the gradebook or on PDF/SCORM export.

**Components:**

| Role | Component | Grant |
|---|---|---|
| Existing Art. 50 instrumentation in this KB | [`compose/code/aiact-50-2-marking/`](code/aiact-50-2-marking/), [`aiact-50-2-spans/`](code/aiact-50-2-spans/), [`aiact-50-2-pack/`](code/aiact-50-2-pack/), [`aiact-50-2-exposure/`](code/aiact-50-2-exposure/) | this KB |
| LMS of record | `OpenOLAT` (Apache-2.0) or `Moodle` (GPL-3.0) | permissive / copyleft |
| Generation surface | `DeepTutor` (Apache-2.0) | permissive |

**Wiring:**

1. **Inventory generation points** — every path that emits learner-visible text or media.
   🔵 **Include the ones nobody calls AI:** autogenerated feedback, rubric suggestions, translated
   captions.
2. **Mark at the generation boundary**, never at the presentation layer, so the mark cannot be lost
   by a downstream renderer.
3. **Carry the mark across the LMS write**, and re-test it on **export** (PDF, SCORM, gradebook
   CSV) — the step most often missed.
4. **Disclose interaction** in the tutor UI at session start, not buried in terms.
5. 🔴 **Remove emotion inference entirely.** Emotion recognition is **prohibited**, already in
   force, and no marking or documentation makes a proctoring/engagement feature that infers
   emotional state lawful. **This is a deletion, not a compliance task.**
6. **Then, and separately,** begin the Annex III programme for `2 Dec 2027` — conformity
   assessment, technical documentation, logging and human oversight for the four named functions:
   admissions screening, evaluating learning outcomes, determining education level, exam
   monitoring. 🔵 **Design to human-final-decision now** and the 2027 assessment becomes
   documentation.

🔴 **Caveat to carry into the client conversation.** The amending instrument is reported as
**Regulation (EU) 2026/1744** (OJ `24 Jul 2026`, in force `27 Jul 2026`), but
`eur-lex.europa.eu` is **DNS-blocked in this session** and the primary text is **not read here**
(`Gap 521-D`); the `2 Dec 2026` marking date is **single-sourced** (`Gap 521-E` neighbour).
🔵 **Brief the direction, verify the citation before it reaches a contract.**

**Effort: 3-5 weeks** for the marking pack. 🟢 **The nearest-dated billable education-AI engagement
in EMEA.**

---

## 🆕 `p520` — `2026-10-29` — **🟢 THREE RECIPES, AND ONE RETRACTION `Gap 520-A` ASKED FOR BY NAME: `P530` is the licence-clearance gate rebuilt around the finding that in education the blocking grant is a CONTENT licence — with a working reader and 40 controls. `P531` is the first fully-permissive INSTITUTIONAL stack this base can offer, newly buildable because `OpenOLAT` is Apache-2.0. `P532` is the substitution recipe for `cn-math-taxonomy`, which is CC BY-NC and cannot be used at all. 🔴 And `Pattern 32`'s TEXT is retracted here, not merely superseded — `P529` replaced its architecture while leaving the withdrawn premise on the shelf.**

### 🔴 `Pattern 32` — RETRACTED IN TEXT, as `Gap 520-A` required

🔴 **The gap's wording was precise and it named two actions:** *"read the guidelines, and rewrite
`Pattern 32` — `P529` replaces its architecture but does not retract its text."* 🟢 Both are done.

🔴 **`Pattern 32` is withdrawn.** Its premise — *Quebec public bodies may not integrate,
experiment with, acquire or deploy generative-AI assistants* — was true from **March 2025**
(*indication d'application* `IA-RI-2025-001-OP`) and **ceased to be true in December 2025**. Any
recipe built on "you cannot deploy generative AI in the Quebec public sector" is **wrong as of
3–5 December 2025** and has been for ~11 months.

🟢 **What replaces it is not a prohibition pattern but a compliance-remediation one**, because the
new instruments carry a deadline that has **already passed**:

| instrument | date |
|---|---|
| *arrêté ministériel révisé* | **3 December 2025** |
| *indication d'application* (generative AI) | **5 December 2025** |
| announced by the MCN | **19 December 2025** |
| 🔴 full compliance due | 🔴 **5 June 2026 — PASSED** |

🔵 **Required artefacts, enumerated by the instrument itself**: data protection, **staff training**,
stated criteria for selecting generative-AI use cases, a **governance framework**, risk management,
control measures, and an updated statement of principles with **12 ethical principles**. 🟢 `P529`
is the architecture that produces them; the sales motion is *"you are past your deadline"*, not
*"you are now permitted"*.

🔴 **Declared caveat, carried into every use of this:** the MCN texts are **not read first-hand** —
`cyber.gouv.qc.ca` is non-allowlisted from this session. Dates are corroborated across four
independent Quebec outlets; **clause text is not asserted** and must be read before a compliance
opinion is given to a client.

---

### 🟢 `P530` — The licence-clearance gate, rebuilt for an industry that ships curriculum

🔵 **Who it is for:** every education engagement, as the first gate before any repo enters a
proposal. 🔴 **Why the previous version was insufficient**, stated as a measured defect rather than
a worry: this pass graded seven high-profile education repos whose grant had been unreadable, and
the three highest-starred blockers were **CC BY-NC 4.0**, a **bespoke non-commercial** licence and
**CC BY-SA 4.0**. 🔴 **Not one is a code licence.** A clearance step that asks *"is it MIT, Apache
or BSD?"* has no verdict for any of them, and the common failure mode is to read the first line,
see MIT-shaped words, and pass it.

🟢 **The recipe — four stages, each with a channel and a refusal:**

1. 🟢 **Existence, on two channels.** GitHub search API (`repo:<slug>`) **and**
   `curl -s -o /dev/null -w '%{http_code}' https://raw.githubusercontent.com/<slug>/HEAD/README.md`.
   🔴 If they disagree, the row is **not shelvable on one channel** — `kvnloo/tutor-mcp` serves at
   `200` while search returns `total_count: 0` (`T520-6`).
2. 🟢 **Liveness, from `archived` and `pushed_at` only.** 🔴 **Never from `updated_at`**, which moves
   when metadata moves (`p519`, `menthorlabs/menthor`). 🔴 A repo that is not archived can still be
   dead: `pupilfirst` is MIT, 980★, unarchived, and unpushed since `2025-12-09`.
3. 🟢 **The grant, from SERVED BYTES — never from the classifier label.**
   `curl -sL https://raw.githubusercontent.com/<slug>/HEAD/LICENSE` and probe
   `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` in turn. Record **byte count** and
   **`git hash-object`** so the read is reproducible. 🔴 A `NOASSERTION` label is a *blocker that
   one read clears*, not a grant (`T520-3`).
4. 🟢 **Grade the payload with the reader, not by eye** —
   [`compose/code/p520-licence-bytes/grade.py`](code/p520-licence-bytes/grade.py), **40/40
   controls green**, runnable under `python3 -I` from the repo root or its own folder.

🟢 **The four refusal classes the reader enforces**, and each exists because a live repo on these
shelves has that shape:

| class | what it looks like | live example | posture |
|---|---|---|---|
| **`NON_COMMERCIAL_REFUSED`** | CC BY-**NC**, or a bespoke grant limiting use to *"personal, educational or non-commercial"* | `cn-math-taxonomy`, `PageLM` | 🔴 **HARD NO for paid work.** Not cured by attribution, by a fee, or by "internal evaluation only" |
| **`SOURCE_AVAILABLE_RESTRICTED`** | Elastic-2.0 / BSL shape: source open, **hosting** restricted | `advisingapp` | 🔴 Self-host for the client; **never** offer as a managed service |
| **`SHAREALIKE_CONTENT`** | CC BY-**SA** | `education-agent-skills` | 🟡 Commercial use fine; **derivatives must ship CC BY-SA**. Quarantine adaptations in their own directory |
| **`WRAPPER`** | bespoke name on line 1, standard body beneath | `Claroline`→AGPL-3.0, `pupilfirst`→MIT | 🟡 **Read the body, grade on the body.** Line 1 misleads in both directions |

🔴 **Two instrument rules the reader encodes, both learned the hard way this pass:**
🟢 read the **GNU family from the first six lines**, never from the body — canonical GPL-3.0 names
the AGPL in its own §13, and a body scan grades verbatim GPL-3.0 as AGPL-3.0 (`T520-5`);
🟢 grade a **bespoke non-commercial licence before** any MIT body match, because such licences
borrow MIT's *"Permission is hereby granted, free of charge…"* opening verbatim.

🟢 **Deliverable:** a per-repo TSV — slug, path, HTTP, bytes, blob SHA-1, served SPDX, verdict,
permissive, paid-client-work, basis, prior belief — exactly
[`evidence/licence-bytes.2026-10-29-p520.tsv`](../evidence/licence-bytes.2026-10-29-p520.tsv).
🔵 **Effort: ~0.5 day for a 20-repo shortlist**, and it is the cheapest insurance in the engagement:
this pass found **three refusals among seven rows** that two prior passes had carried or shelved.

---

### 🟢 `P531` — The fully-permissive INSTITUTIONAL stack (no copyleft anywhere)

🔵 **Who it is for:** a **greenfield** institutional build — a new programme, a new campus, a
training arm, a corporate academy — where the client wants to own and possibly close the result.
🔴 **Why this did not exist before this pass:** every LMS of record on these shelves was copyleft
(Open edX AGPL-3.0, Moodle GPL-3.0, `frappe/education` GPL-3.0, `openeducat_erp` LGPL-3.0), so
`P528` had to route the agent *around* the platform across a SCORM/LTI package boundary.
🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is Apache-2.0** — read from served
bytes, `10 982` B, blob `e8870c0f5f52` — so the boundary is no longer required.

🟢 **The stack, every rung permissive and every grant byte-verified:**

| rung | component | licence | why this one |
|---|---|---|---|
| System of record | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Full institutional LMS — courses, assessment, groups, portfolio, curriculum. 🇨🇭 **EMEA**, descended from University of Zurich OLAT, 448★ / 166 forks, pushed `2026-10-28` |
| *(alternative)* | Sakai | 🟢 **ECL-2.0** | Apache-2.0 + educational patent clause; consortium governance. Use where research-collaboration workflows matter |
| Interop | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** | LTI + Common Cartridge. 13 years maintained, 267 forks (`p519`) |
| Content runtime | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | SCORM 1.2 / 2004, offline-first (`p519`) |
| Mastery tier | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | Bayesian Knowledge Tracing — reproducible, auditable, no LLM in the decision |
| Lesson surface | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | Authoring model encodes misconceptions explicitly → maps onto BKT skill nodes. 6,951★ / 5,861 forks |
| Dialogue tier | `DeepTutor` (Apache-2.0) · 🇨🇳 [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, 41,726★) · 🇫🇷 [`braiinz94/braiinz-education`](https://github.com/braiinz94/braiinz-education) (Apache-2.0) | 🟢 permissive | Explains, hints, re-teaches. **Reads** the mastery estimate; never computes one |
| Offline edition | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | Low-connectivity deployments (`P526`) |

🟢 **Why it sells:** the client may fork any rung, ship a **closed** derivative, and owes
reciprocity to nobody. 🔵 No package boundary, no plugin-vs-derivative argument, no AGPL network
clause — the licence conversation ends at "attribution and a NOTICE file".

🔴 **When NOT to use it.** If the client is **already** on Moodle or Open edX — which is most
institutional clients — `P528` remains correct and this pattern is a migration proposal, not an
integration one. 🔴 Do not pitch replacing a working Moodle estate to win a licence argument.

🔵 **Effort: 10–12 weeks** for a working institutional pilot (system of record + interop + mastery
+ one dialogue agent), assuming no SIS integration. 🔴 **There is still no permissive SIS at
institutional scale** on these shelves (`Gap 521-A`), so a student-records requirement forces
OpenEduCat (LGPL-3.0) and a separate-module boundary.

---

### 🟢 `P532` — Substituting for a corpus you may not use (the `cn-math-taxonomy` problem)

🔵 **Who it is for:** any APAC maths or STEM engagement, and more generally any engagement whose
obvious best corpus turns out to be non-commercial. 🔴 **The concrete problem:**
[`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) is the richest curriculum
corpus this base has found — **1,644 knowledge points, 2,403 prerequisite edges, 6,723 problems**,
PRC-curriculum-aligned, 4,925★ in eleven days — and it is **CC BY-NC 4.0**. 🔴 It cannot be
ingested, embedded, fine-tuned on, or shipped in paid work. **There is no workaround**, and
"evaluation only, inside a paid engagement" is still commercial use.

🟢 **The recipe — build the structure, licence the content separately:**

1. 🟢 **Take the *shape*, not the data.** A prerequisite graph over knowledge points is **not
   copyrightable as an idea**; this corpus's particular expression is. 🟢 So model the schema —
   knowledge point, prerequisite edge, problem, diagnostic path — in your own repository, and
   populate it from sources you may use. 🔴 Do **not** copy its node set, its edge list or its
   problem text, and do not have a model trained on it emit them.
2. 🟢 **Populate from the client's own curriculum.** In an institutional engagement this is the
   *correct* source anyway: the client owns its syllabus, its past papers and its question banks,
   and a corpus built from them is aligned to the assessment that actually matters.
   🔵 [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) (MIT, `p519`) is built exactly
   for this — editable artefacts from *the school's own* curriculum.
3. 🟢 **Fill gaps with permissive corpora.** 🇧🇷
   [`Universidade-Livre/ciencia-da-computacao`](https://github.com/Universidade-Livre/ciencia-da-computacao)
   (**MIT**, 20,985★) for CS; [`oppia/oppia`](https://github.com/oppia/oppia)'s (Apache-2.0)
   exploration content for maths, whose misconception encoding is the part BKT needs.
4. 🟢 **Wire mastery with [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor)** (MIT) over your own
   graph, so prerequisites drive the next item deterministically — `P525`'s tier 1.
5. 🟡 **If the PRC-curriculum alignment itself is the requirement**, licence it: CC BY-NC permits
   a **separately negotiated** commercial grant from the rights-holder. 🟢 That is a procurement
   conversation to open early, not a blocker to discover at delivery.

🔵 **Effort: 4–6 weeks** to a populated graph over a single subject and year-group from client
materials. 🔴 **State the licence finding to the client in writing.** The failure mode this recipe
exists to prevent is an engineer finding the corpus independently mid-build and ingesting it,
because its README does not say "non-commercial" — only its `LICENSE` does.

## 🆕 `p519` — `2026-10-29` — **🟢 TWO RECIPES, AND BOTH EXIST BECAUSE OF SOMETHING THAT CHANGED TODAY: `P528` wires a FULLY PERMISSIVE pipeline INTO a copyleft LMS without touching it, across a package boundary — newly buildable because the LTI and SCORM runtimes were verified permissive this pass. `P529` is the Quebec public-sector deployment, newly buildable because the suspension `Pattern 32` was built around turns out to have been LIFTED in late 2025.**

🔵 **Reading note.** Every repo named below was existence- and licence-asserted on `2026-10-29`
through the GitHub search API, with two negative controls refused
([`../evidence/liveness-fields.2026-10-29-p519.tsv`](../evidence/liveness-fields.2026-10-29-p519.tsv)),
or carried from `p518`'s same-day reads. 🔴 **Nothing whose grant reads `NOASSERTION` appears in a
recipe** — which excludes `cn-math-taxonomy` and `canyongbs/advisingapp` despite both being
substantively attractive. Where a part is copyleft the recipe says so and puts it across a process
or package boundary rather than pretending it is permissive.

---

### 🟢 `P528` — Permissive end-to-end, shipped INTO the client's existing copyleft LMS

**The ask it answers.** *"We want a client-owned, closed derivative. Our LMS is Moodle / Open edX
and we are not migrating off it."* 🔴 Until this pass these shelves had no clean answer: every
system of record in education is copyleft (**AGPL-3.0** Open edX, **GPL-3.0** Moodle), and an agent
linked into one invites the derivative-work question.

🟢 **The move: the only thing that crosses into the LMS is a STANDARD PACKAGE.** A file format is
not linkage. The agent stack stays permissive and entirely outside the copyleft work.

| layer | part | licence | why this one |
|---|---|---|---|
| **Source → content** | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | **MIT** | Turns a book into an animated, narrated, interactive experience **and emits SCORM** — the one emitter on these shelves that already speaks the boundary format |
| **Source → teacher assets** | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** | Distils videos, PDFs and transcripts into **source-backed** teacher skills — so the generated material carries its citations, which is what an evaluation story needs |
| **Adaptive sequencing** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | **MIT** | Reads how the learner learns and sets the next lesson; self-hostable (FastAPI + React), so no learner data leaves the institution |
| **Auditable mastery** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | **Bayesian Knowledge Tracing** — a mastery estimate that is deterministic and inspectable rather than model-generated. 🟢 This is the component that survives a regulator asking *"how was this score produced?"* |
| **Retention** | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** | MCP server over Anki: the agent writes into a spaced-repetition schedule the learner already keeps |
| 🟢 **THE BOUNDARY — runtime** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | SCORM **1.2 + 2004** runtime, offline-first. Plays the package; reports completion and score back through the standard |
| 🟢 **THE BOUNDARY — tool launch** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | **LTI** + Common Cartridge. Use instead of SCORM when the agent must stay a *live* tool the LMS launches rather than a packaged asset. Pushed `2026-10-29`; 267 forks |
| **System of record (optional)** | [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 🟢 Only when the client wants a **permissive SIS too** — the first on these shelves. Scope honestly: small-and-medium institutions, **not** a ministry-scale Moodle replacement |
| **Delivery where connectivity is poor** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Offline-first runtime; 1,012 forks. Shares `P526`'s deployment shape |

**Wiring, concretely.**

1. **Ingest** the client's own source material through `lineage-skill` (teacher-facing assets) and
   `Papermorph` (learner-facing interactive content). Both run in your infrastructure; neither
   touches the LMS.
2. **Hold learner state** in `Bloom` + `OATutor`. 🔵 `OATutor` owns the *mastery number*; `Bloom`
   owns *what to teach next*. Keep them separate — it is what lets you show a deterministic
   mastery estimate alongside a model-chosen sequence.
3. **Emit a SCORM package** from `Papermorph`; validate it against `scorm-again` **in CI, before
   any LMS sees it**. 🔴 The failure mode here is not licensing, it is the SCORM data model: get
   `cmi.completion_status` and `cmi.score.scaled` wrong and the LMS records nothing. A local
   `scorm-again` harness makes that a test, not a pilot incident.
4. **Deliver** either as a SCORM package the existing LMS plays, **or** as an LTI tool launched
   through `tsugi`. Choose by whether the experience must be *live* (LTI) or *packaged* (SCORM).
5. **Write retention** through `anki-mcp-server`; write completion back through the SCORM/LTI
   return channel only.

🔴 **The boundary rules — the whole pattern rests on these.**

- 🔴 **Do not fork, patch or link into Moodle or Open edX.** The moment you ship a modified AGPL/GPL
  work, the client's obligation to publish attaches. Interact **only** through SCORM or LTI.
- 🔴 **Do not put `cn-math-taxonomy` in this pipeline**, however well its 1,644 knowledge points and
  2,403 prerequisite edges would fit `OATutor`'s skill model. Its grant is `NOASSERTION` and
  unread. 🟢 **The substitution if the client needs a prerequisite graph now:** build it from the
  client's own curriculum with `lineage-skill`, which produces source-backed output you own.
- 🟡 **`Papermorph` is four weeks old** (created `2026-10-03`) and `ari` eleven days. Treat
  freshly-created supply as a dependency you may have to maintain yourself, and say so in the
  estimate.

**Effort:** 6–8 weeks for a single-subject pilot against an existing LMS; add 3–4 weeks if
`academico` replaces the SIS. **The deliverable that de-risks it:** a SCORM conformance harness in
CI from week one.

---

### 🟢 `P529` — The Quebec / governed-use public-sector deployment (replaces `Pattern 32`'s premise)

🔴 **Why this pattern exists, stated as a correction.** `Pattern 32` on these shelves is built
around Quebec's **13 March 2025** MCN order suspending generative-AI assistants in public bodies.
Read `2026-10-29`: **that suspension was lifted in late 2025**, replaced by MCN *lignes directrices*
written after a risk exercise with **14 public bodies**. 🔴 So `Pattern 32`'s premise — *this
jurisdiction cannot buy* — is withdrawn. The jurisdiction can buy, **under published guidelines**.

🟡 **Tier, declared before anything is built on it:** index-level reads (UQAM *Collimateur*, *École
branchée*), with the March 2025 order's origin in *Le Soleil*. 🔴 `cyber.gouv.qc.ca` and
`collimateur.uqam.ca` are unreachable from this session, so **the guidelines' own text has not been
read and their exact date is not asserted**. 🔴 **Do not quote the guidelines to a client from this
base.** Read them first — `Gap 520-A`.

🟢 **The architecture, and it generalises past Quebec.** Four instruments on
[`../intel/market.md`](../intel/market.md) point the same way: NYC bars AI from grading and
discipline (March 2026); California **AB 1159** would bar training on student data; Vietnam's AI
Law names **automated assessment** and **behavioural monitoring**; Quebec now requires conformance
to published guidelines. 🔵 **One architecture satisfies all four** — learner data never leaves the
institution, and no consequential decision is the model's.

| requirement it comes from | part | licence | role |
|---|---|---|---|
| data must not leave the institution | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | **MIT** | **Local-first** teacher-facing assistant producing *editable* lesson drafts, student materials and slides **from the school's own curriculum**. 🟢 Teacher edits the artefact — so a human is the author of record |
| same, learner-facing | [`nichochar/ari`](https://github.com/nichochar/ari) | **MIT** | **Local-first** learner tool (pen + paper + AI). 🟡 Created `2026-10-18` — eleven days old; pilot-grade, and estimate it as such |
| AI must not grade | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | BKT mastery estimate is **deterministic and auditable**, and it is *formative*. 🔴 It feeds teacher judgement; it does **not** emit a grade of record |
| no behavioural monitoring | — | — | 🔴 **An omission is part of the build.** Do not ship engagement tracking, attention inference or affect detection. Vietnam names it; NYC's framework implies it. Log *task* events, never *person* signals |
| offline / low-connectivity delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Offline-first delivery where school connectivity is the constraint |
| must map to the ministry's own framework | — | — | 🟢 Quebec's **updated digital-competency framework (21 April 2026)** integrates **AI literacy into existing competencies** rather than creating a dedicated AI course. 🔵 **Map the deliverable onto those competencies**; a standalone "AI module" fights the framework |

**Wiring, concretely.**

1. **Deploy `Claw-ED` teacher-side first**, on institution infrastructure with a locally-hosted
   model. Teachers get editable drafts; nothing is published to students unreviewed.
2. **Add `OATutor` as the formative mastery layer.** Make the audit trail a feature of the pitch:
   every mastery number is reproducible from the response history.
3. **Keep the decision boundary explicit in the data model** — a `recommendation` table the model
   writes, and a `decision` table only a human writes. 🟢 This is `P525`'s rule and it transfers
   unchanged to the Vietnamese statute's named mechanisms.
4. **Write the conformance memo as a deliverable**, mapped to the competency framework and to the
   MCN guidelines **once their text is read**.
5. **Ship nothing that infers emotion, attention or engagement.**

🟢 **Why this is commercially live rather than theoretical:** Quebec's public sector spent roughly
a year unable to procure generative-AI assistants. The constraint lifted, the guidelines are
published, and the permissive local-first supply to build against them landed on these shelves
**today**. **Effort:** 8–10 weeks teacher-side pilot; the conformance memo is week one, not week
ten.

## 🆕 `p518` — `2026-10-29` — **🟢 FOUR RECIPES, EACH WIRED FROM REPOS VERIFIED TODAY AND EACH ANSWERING A REGULATORY OR OPERATIONAL CONSTRAINT RATHER THAN A FEATURE REQUEST: `P524` the fully-permissive tutoring stack (closed derivative permitted end to end), `P525` the Annex-III / Oklahoma-S.B.-1734 architecture where the consequential decision is NOT the model's, `P526` the offline deployment for Ghana/Kenya AI-literacy and rural LATAM, `P527` the licence-clearance gate as a three-mechanism checklist.**

🔵 **Reading note.** Every repo named below was existence- and licence-verified on `2026-10-29`
(see [`agents/top.md`](../agents/top.md), [`repos/foundations.md`](../repos/foundations.md),
[`verticals/solutions.md`](../verticals/solutions.md)). Where a part is copyleft the recipe says
so and places it across a process boundary rather than pretending it is permissive.

---

### 🟢 `P524` — The fully-permissive tutoring stack: a closed client derivative, end to end

🔵 **Who it is for:** any client — region-independent — that will not accept a copyleft
obligation on its own modules, which in practice means most private edtech and most enterprise
L&D buyers.

🟢 **Every part is MIT, Apache-2.0, BSD-3-Clause or ECL-2.0. There is no copyleft anywhere in
this stack**, which is why it is the default recommendation.

| Layer | Part | Licence | Why this one |
|---|---|---|---|
| System of record | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) (HiEd) **or** [`gongfuxiang/schoolcms`](https://github.com/gongfuxiang/schoolcms) (K-12) | **ECL-2.0** / **Apache-2.0** | 🟢 The only two systems of record on these shelves a studio can fork and ship closed |
| Orchestrator | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | Apache-2.0 | Minimal surface, code-writing agents; nothing to unpick later |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 48,177★, v1.7.0 `2026-10-28`; keeps a persistent learner model across sessions |
| Classroom simulation | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT | Instructor + peer + assessor agents, for cohort dynamics a 1:1 tutor cannot produce |
| Content ingestion | [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | MIT | Client's own textbooks/manuals → retrievable skill packages |
| Content transformation | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | MIT | 🟢 **Emits SCORM** — output drops into the LMS the client already owns, no integration work |
| Course generation | [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | MIT | Topic → 2-minute audio lessons **with cited sources** |
| Retention | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | MIT | Writes into the learner's own spaced-repetition schedule instead of inventing a new one |
| Content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT | Questions, MCQs, lesson plans as a library call |

🟢 **How it wires.** Sakai/SchoolCMS stays the system of record and is the **only** writer of
enrolment, grades and transcript. `smolagents` runs the orchestration; `DeepTutor` owns the
learner model and the dialogue; `book-to-skill` + `educhain` + `claudemy` produce material from
the client's own corpus; `Papermorph` renders it to SCORM so the LMS ingests it through a path
it already supports; `anki-mcp-server` carries retention. 🔴 **The one hard rule:** the agents
read the SIS and write only to their own store — a tutoring agent that writes a grade is both an
architectural mistake and, under `P525`'s regimes, an illegal one.

🔵 **Substitutions by region:** 🇨🇳 swap in `Study-Mate` (MIT) and `universal-examprep-skill`
(MIT) for Mandarin-native UX; 🇪🇺 swap in `get-it` (Apache-2.0, 🇮🇹) for an in-region provenance
story; 🇧🇷 add `ciencia-da-computacao` / `matematica` / `bncc-dados` (all MIT) as the curriculum
spine.

---

### 🟢 `P525` — The architecture where the model is **not** the decision-maker (EU Annex III, Oklahoma S.B. 1734)

🔵 **Who it is for:** any EU institution doing learner evaluation or admissions (Annex III
**high-risk**), and any US district under Oklahoma-style language barring AI as the **primary
basis** for grading or discipline. 🟢 **One architecture satisfies both**, because both regimes
regulate *where the consequential decision lives*, not what model you use.

🔴 **The anti-pattern this replaces:** an LLM is shown a transcript and asked "has this student
mastered X?" Its answer is unreproducible, unexplainable and is the decision. That fails
conformity assessment and fails the Oklahoma test.

🟢 **The pattern — three tiers with the boundary enforced in code:**

1. 🟢 **Deterministic mastery tier — [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor), MIT, UC Berkeley.** Bayesian Knowledge Tracing computes mastery from observed correct/incorrect responses. 🔵 **This is the whole point of the recipe:** BKT yields a probability with a stated model, auditable inputs and a reproducible result — a number you can put in front of a regulator or a parent. No LLM participates in it.
2. 🟡 **Explanation / dialogue tier — `DeepTutor` (Apache-2.0) and/or `get-it` (Apache-2.0, 🇮🇹).** The model explains, hints, re-teaches, generates practice and converses. It **reads** the mastery estimate and never computes one. `get-it` earns its place here on the Feynman-technique loop (learner explains it back) which produces evidence of understanding rather than an assertion of it.
3. 🟢 **Human gate — logged, blocking, on the decision boundary.** Progression, grading and discipline require an educator action. Log: the BKT inputs, the estimate, the model's explanation, the human's decision, and the timestamp. 🔵 **That log is the conformity artefact** — it is what documentation, human-oversight and record-keeping obligations actually ask for.

🟢 **Delivery surface:** [`oppia/oppia`](https://github.com/oppia/oppia) (Apache-2.0) for the
interactive lessons, since its authoring model already encodes misconceptions explicitly, which
maps onto BKT skill nodes. 🟢 **System of record:** Sakai (ECL-2.0). 🔴 **If the client is on
Moodle (GPL-3.0) or Open edX (AGPL-3.0)**, integrate as a plugin/XBlock over the documented API
and keep tiers 1–3 in a separate service — do not fork.

🟢 **Why it sells.** The compliance artefact is a by-product of a better architecture, not an
overhead bolted on. And it is portable: the same build answers Maryland's 24 districts, every
state copying Oklahoma's language, and an EU Annex III assessment.

---

### 🟢 `P526` — Offline-first AI literacy for Ghana/Kenya pillars and rural LATAM

🔵 **Who it is for:** 🇬🇭 Ghana (*National AI Strategy 2025–2035*, launched 24 April 2026,
**education as pillar one**; KG→P6 AI-literacy curriculum revisions presented July 2026),
🇰🇪 Kenya (*National AI Strategy 2025–2030*, AI literacy across education), and the rural and
Indigenous-language LATAM contexts that UNESCO IESALC's 87%-adoption figure does **not** reach.

🔴 **The binding constraint is not cost, it is connectivity** — and it rules out every
cloud-API tutoring product on the market.

| Layer | Part | Licence | Why |
|---|---|---|---|
| Platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 🟢 Offline-first by design, built for exactly this deployment; syncs opportunistically |
| Local inference | [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | **MIT** | 🟢 Agents on a **local** LLM — *"no frameworks, no cloud APIs, no hidden reasoning"*. The architecture is legible, which matters when the ministry must audit it |
| Mastery | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | 🟢 BKT runs on-device at negligible cost; no inference needed for the mastery estimate at all |
| Curriculum corpus | [`freeCodeCamp`](https://github.com/freeCodeCamp/freeCodeCamp) (BSD-3-Clause) + [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) (MIT) | permissive | 🟢 AI-literacy content that already exists, permissively licensed, and is what the pillars actually ask for |
| Retention | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** | Anki is offline-native; spaced repetition survives an uplink that does not |

🟢 **The design move.** Put `OATutor`'s BKT and `Kolibri`'s content on the device, and treat model
inference as **optional enrichment** rather than the critical path. A learner with no uplink
still gets curriculum, practice, mastery tracking and spaced repetition; when a local model is
available they also get explanation and dialogue. 🔴 **A stack that degrades to nothing without
inference cannot be deployed under these pillars** — that is the single most common failure in
this segment.

🔴 **Pricing note, stated as a risk not a plan.** A ResearchGate proposal pairs a $50M Phase-1
1M-device rollout with open-source components and asks all 54 African countries to adopt AI
education strategies — 🔴 **it is a recommendation, not funded policy.** Do not build a commercial
case on it. The funded, named hooks are Ghana's and Kenya's adopted strategies.

🟡 **For rural LATAM** the same stack applies with `bncc-dados` (MIT) or
`ciencia-da-computacao` (MIT) as the corpus; 🔴 Indigenous-language support is **not** solved by
anything on these shelves and should be scoped as original work, not as configuration.

---

### 🟢 `P527` — The licence-clearance gate: three mechanisms, three checks

🔵 **Who it is for:** the studio itself, before any education repo enters a client build. 🟢 This
pass measured three *distinct* ways a high-star education repo defeats the usual check, so the
gate is three checks, not one.

🔴 **What the usual check is, and why it fails.** Filter on stars, confirm a LICENSE link exists.
🔴 **All four repos in [`agents/top.md`](../agents/top.md)'s blocked block pass that filter.**

🟢 **Check 1 — resolve the repo by API, and record the slug the API returns.**
🔴 `openedx/edx-platform` serves a browser redirect and returns *"the resources do not exist"* to
the search API; the live name is `openedx/openedx-platform`. 🔴 `microsoft/autogen` is **archived**
— *"no longer maintained"* — and a browser glance does not say so as loudly as a star count says
otherwise. 🟢 **Assert existence, archived status, default branch and last push by API. A
renamed or archived repo is a supply risk before it is a licence question.**

🟢 **Check 2 — when GitHub's classifier declines the grant, read the served file, not the README.**
🟢 `openeducat_erp` classifies as `NOASSERTION`; `LICENSE` @ branch `19.0` opens *"GNU LESSER
GENERAL PUBLIC LICENSE, Version 3, 29 June 2007"* — **LGPL-3.0**, workable. 🟢 `frappe/education`
is unclassified; `license.txt` @ `develop` says *"License: GNU GPL V3"* — **GPL-3.0**, not
workable as a fork. 🔵 Run [`ingest/probe-grant.sh`](../ingest/probe-grant.sh) (53 grant filenames,
14 languages, default branch resolved) first, then read the title block of whatever it finds.

🟢 **Check 3 — read the grant for a non-commercial or bespoke term, which a family name hides.**
🔴 `cn-math-taxonomy` is `CC BY-NC 4.0`: Creative Commons, permissive-*looking*, **non-commercial**
— unusable for a client engagement. 🔴 `PageLM` carries a **"CaviraOSS Community License"**, free
for personal and educational use, *"commercial use or resale requires prior written permission"* —
not OSI at all. 🟢 **The check is literal: grep the grant for `NonCommercial`, `-NC`, `-ND`,
`prior written permission`, `resale`, and for any licence title that is not a recognised SPDX
name.**

🟢 **Gate output, per repo, three fields:** `{resolved_slug, archived}` · `{spdx_id, read_from}` ·
`{commercial_use: permitted | permission_required | prohibited}`. 🔴 **Any repo that cannot fill
all three does not enter the build.** 🔵 And one secondary check worth the minute it costs: where
a repo publishes its own counts (`cn-math-taxonomy`: 1,644 vs ~1,838 knowledge points, 6,723 vs
7,427 questions), **disagreement between its About blurb and its README is a data-quality signal
about the corpus itself**, independent of the licence.

## 🆕 `p517` — `2026-10-29` — **🟢 `P522` — the first recipe on these shelves built end-to-end from APAC-originated, licence-verified parts, and the first that permits a CLOSED derivative, because every part is Apache-2.0 or MIT. 🟢 `P523` — the licence-clearance gate, which is a runnable script in this repo rather than advice.**

### 🟢 `P522` — A fully permissive APAC school stack: SIS of record + lesson generation + curriculum-grounded tutor + gated ops agents

🔵 **Who it is for:** a Chinese (or broader APAC) school group or municipal education bureau that
wants AI tutoring, lesson generation and operational automation **on top of an open SIS it
controls**, and that needs the right to ship a **proprietary** derivative.

🟢 **Why this recipe could not be written before `p517`:** the SIS was missing. `p516`'s LATAM
recipe (`P521`) is built on `i-educar`, which is **GPL-2.0** — so it cannot offer a closed
derivative. 🟢 **Every part below is Apache-2.0 or MIT, verified from bytes this pass.**

| Role | Part | Licence (from bytes) | HEAD @ default branch |
|---|---|---|---|
| **System of record** (students, grades, teachers, enrolment, exams) | [`gongfuxiang/schoolcms`](https://github.com/gongfuxiang/schoolcms) 🇨🇳 | 🟢 **Apache-2.0** | `21d6a41b89e4` @ **`master`** |
| **Lesson generation** (topic or document → interactive lesson, slides, quizzes) | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) 🇨🇳 | 🟢 **MIT** | `e95c1d0bf23b` @ `main` |
| **Curriculum-grounded tutor** (K-9, textbook-faithful, Socratic) | [`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) 🇨🇳 | 🟢 **MIT** | `525d977f230a` @ **`master`** |
| **Gated operations agents** (Q&A, grading, vision, analytics, supervision) | [`yqy624/eduagent-digital-workforce`](https://github.com/yqy624/eduagent-digital-workforce) 🇨🇳 | 🟢 **MIT** | `a52bf227145c` @ `main` |
| **Jurisdiction policy routing** (Korea / Vietnam / Japan / Australia) | LangGraph policy nodes — **build**, no off-the-shelf part exists | MIT (LangGraph) | — |
| **Model layer** | 🇯🇵 route via [`llm-jp/awesome-japanese-llm`](https://github.com/llm-jp/awesome-japanese-llm) (Apache-2.0 index) for a Japanese deployment; GPT-OSS Swallow / Tanuki weights are Apache-2.0 | 🟢 Apache-2.0 | `4fa4630ddbdd` @ `main` |

🟢 **How the parts wire together — the load-bearing constraint is that the SIS stays authoritative:**

1. 🟢 **`schoolcms` remains the only writer of grades and enrolment.** Expose it to the AI layer
   through a **read-only replica** of its MySQL schema. 🔴 **No agent writes to `schoolcms`
   directly** — this is the single rule that makes the stack defensible to an education buyer.
2. 🟢 **Curriculum ingestion → `OpenMAIC`.** Feed syllabus documents and textbook units in; it emits
   interactive lessons with slides, quizzes and project work. Store lesson artifacts in your own
   store keyed by the `schoolcms` course ID.
3. 🟢 **Tutoring → `AI_Tutor_Release`.** Point its RAG index at the licensed textbook corpus
   (🔴 **the corpus is the client's licensing problem, not the repo's** — PEP/人教版 texts are
   copyrighted; the repo ships the retrieval pattern, not the books). Keep its two documented
   behaviours: quote the textbook's original wording in preference to paraphrase, and ask Socratic
   questions rather than returning answers.
4. 🟢 **Operations → `eduagent-digital-workforce`, gates preserved exactly as the repo defines
   them.** Grading writes to a **teacher-confirmation queue**, never to the grade table; vision
   **logs events without acting**; analytics is **read-only**; supervision de-duplicates and
   requires manual confirmation. 🟢 The confirmation queue is the only path from an agent to
   `schoolcms`, and a human is on it.
5. 🟢 **Policy routing wraps everything.** A LangGraph policy node resolves the learner's
   jurisdiction before any model call: **Korea** (AI Basic Act, in force 22 Jan 2026) and
   **Vietnam** (Law on AI, in force 1 Mar 2026, **education transition 1 Sep 2027**) are binding
   regimes; **Japan** and **Australia** route to voluntary-framework handling. 🔴 This is the one
   component with no open-source part and it is where the studio's margin is.

🟢 **What the client gets to own.** Apache-2.0 on the SIS gives an **express patent grant** and
permits a closed derivative; MIT on the three agent parts permits the same. 🟢 **So the AI layer can
be proprietary and the SIS can be modified in place** — which `P521` cannot offer in 🇧🇷.
🔴 **Attribution obligations still ship:** Apache-2.0 requires the `NOTICE` and licence text to
travel with the derivative, and the repo carries both `LICENSE` and `LICENSE.txt`.

🔴 **Honest sizing, stated rather than buried.** `schoolcms` is **292★/110 forks** on **ThinkPHP**
(PHP) — mature for its niche, not a modern framework; `eduagent-digital-workforce` is **3★** and
self-describes as *"a demonstrable MVP rather than a production system"*; `AI_Tutor_Release` is
**74★**. 🟢 **`OpenMAIC` is the only large part (41.7k★, 798 commits).** 🟢 **Read the recipe
accordingly: it is a credible reference architecture with one production-grade component, and the
studio's work is hardening the other four** — which is precisely the APAC engagement shape this
pass established.

### 🟢 `P523` — The licence-clearance gate: run this before any APAC architecture work

🔵 **Who it is for:** any engagement that will build on open-source parts found in a region whose
supply this base has measured as **two-thirds ungranted** (`intel/trends.md` `T517-1`).

🟢 **It is a script in this repo, not advice:**
[`ingest/probe-grant.sh`](../ingest/probe-grant.sh).

```bash
./ingest/probe-grant.sh owner/repo [owner/repo ...]
# TSV out: repo  live  default_branch  head_sha  grant_files  spdx_guess
```

🟢 **What it does that hand-checking did not**, and this base has the scar tissue to prove each one
matters:

| guarantee | the failure it prevents | the pass that paid for it |
|---|---|---|
| default branch via `git ls-remote --symref` | probing `main`/`master` on a repo whose default is `2.12` or `1.6` → **false "unlicensed"** | `p509`, repeated by `p516` |
| **53 grant filenames in 14 languages** | missing `LICENSE-CODIGO.md` / `LICENSE-DADOS.md` → **a split MIT + CC BY 4.0 repo read as unlicensed** | `p516` |
| emits **`UNRESOLVED`**, never *"unlicensed"* | publishing a verdict where only a measurement exists | `p516`, `p517` |

🟢 **The triage, which is the actual deliverable of the gate:**

1. 🟢 **Apache-2.0 / MIT / BSD → BUILD.** Closed derivative permitted; carry `NOTICE` and licence
   text. Apache-2.0 adds an express patent grant.
2. 🟡 **GPL / AGPL / LGPL → ISOLATE.** Keep the copyleft component at arm's length — separate
   process, network boundary, no linking. 🔴 **AGPL reaches across the network**, so an AGPL
   gradebook (`i-diario`) cannot sit inside a proprietary service.
3. 🟡 **Split grants (code vs data) → CARRY BOTH.** `bncc-pacotes` ships **MIT code and CC BY 4.0
   data in one wheel**; attribution must travel into the product, and its **name and visual
   identity are not licensed** — so a derivative may use the data and may not present itself as
   BNCC-branded.
4. 🔴 **`UNRESOLVED` → DO NOT SHIP.** Default copyright applies: no licence means no permission.
   🟢 **Next step is not a judgement, it is an email** — open an issue asking the maintainer to
   declare a licence. 🔵 Before concluding absence, check the README, `pyproject.toml` classifiers
   and `package.json` `license`, which this probe does not read (`Gap 517-E`).

🔴 **Do not use `curl -sI` as the liveness check** in this session class: it returns **403 on
every GitHub repo page**, including ones `git ls-remote` proves alive (17/17 this pass). A pass that
treated 403 as 404 would delete true rows. 🟢 `probe-grant.sh` establishes liveness on `git`, so
liveness is attested by construction.


## 🆕 `p516` — `2026-10-29` — **🟢 `P521` — the first recipe on these shelves built END-TO-END from LATAM-originated, licence-verified parts. 🔴 It exists because the premise that LATAM had no such parts was false.**

### 🟢 `P521` — Curriculum-anchored tutoring and reporting on a Brazilian municipal stack

🔵 **Who it is for:** a Brazilian municipal or state education secretariat (or a private network)
already running **`i-educar`**, that wants AI tutoring and curriculum-aligned reporting without
replacing its system of record. 🟢 **Every part is verified from bytes this pass and is
LATAM-originated except the tutoring runtime.**

**The parts, with the grants that govern them:**

| Layer | Part | Licence | Why this one |
|---|---|---|---|
| System of record | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) @ `2.12`, HEAD `435649b0474f` | **GPL-2.0** | 722★, already deployed in Brazilian municipalities via the federal *Portal do Software Público*; holds enrolment, grades, staff |
| Teacher surface | [`portabilis/i-diario`](https://github.com/portabilis/i-diario) @ `1.6`, HEAD `ef909f23755a` | 🔴 **AGPL-3.0** | attendance, lesson records, continuous assessment |
| Curriculum ground truth | [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | **MIT** | **1,721** BNCC learning objectives, JSON/SQLite/CSV, provenance per record |
| Agent access to curriculum | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 code **MIT** + data **CC BY 4.0** | ships an **MCP server** (`mcp-worker/src/`) — the tutor resolves objectives as tools, no custom integration |
| Factuality gate | [`bncc-dev/bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark) | 🟡 code **MIT** + data **CC BY 4.0** | curriculum-grounded hallucination benchmark — gates the model *before* it reaches students |
| Tutoring runtime | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp), HEAD `98463a0cb5fb`, **57★**, 🔴 **alpha** | **MIT** | MCP-native ITS that tracks learner state and holds no item bank — so BNCC objectives become the item spine |
| Evidence trail | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi), HEAD `fbf609142c3c` | **MIT** | writes every interaction to an xAPI LRS — the record a secretariat produces under audit |

**How to wire it:**

1. 🟢 **Stand up the curriculum as tools, not as a prompt.** Run `bncc-pacotes`' MCP worker; the
   tutor calls it to resolve BNCC codes to objectives. Pin the `bncc-dados` commit — `bncc-pacotes`
   syncs data from a pinned commit by design, so reproduce that discipline.
2. 🟢 **Gate the model before students see it.** Run `bncc-benchmark` against the candidate model.
   Its held-out item set is private to resist contamination, so the score means something. Record
   the figure as an acceptance criterion in the SOW.
3. 🟢 **Attach `tutor-mcp` as the runtime** and let BNCC objectives supply the item spine it lacks.
   🔴 **It is alpha at 57★** — treat it as a component to fork and own, not a dependency to trust.
4. 🟢 **Read, do not fork, the system of record.** Have the tutor read learner context from
   `i-educar` over its database/API from a **separate service**. 🔴 **This is the licence-critical
   step** (see below).
5. 🟢 **Emit every interaction to an LRS via `learnmcp-xapi`.** This is what answers the governance
   gap — IESALC puts **26%** of LATAM institutions with a formal AI strategy, UNESCO **<10%** with
   guidelines plus capacity, and Brazil's **PL 2.338/2023** names *"selection of students for
   access to education"* high-risk.
6. 🟢 **Report in BNCC terms.** Because objectives carry provenance, mastery reporting cites the
   curriculum record rather than a vendor's taxonomy — which is what survives a secretariat review.

🔴 **The licence trap, stated as the decisive design constraint.** `i-educar` is **GPL-2.0** and
`i-diario` is **AGPL-3.0**, and these are *not* the same obligation. 🟢 A **separate service** that
talks to `i-educar` keeps the AI work outside the GPL boundary. 🔴 **Modifying `i-diario` and
hosting it for a municipality triggers AGPL-3.0's network source-offer to users** — so put AI
features *beside* `i-diario`, not *inside* it, unless the client accepts publishing the modified
source. 🟡 And the two `bncc-*` package repos ship **code MIT + data CC BY 4.0 in the same npm
tarball and PyPI wheel**: carry the data attribution into the product, and note that `bncc-pacotes`
withholds **name and visual identity**, so the derivative may **not** present as BNCC-branded.

🔵 **Indicative shape:** 8–10 weeks. Weeks 1–2 curriculum MCP + pinned data; week 3 benchmark gate
and acceptance figure; weeks 4–6 tutor-mcp fork and `i-educar` read-path; weeks 7–8 xAPI evidence
trail and BNCC-term reporting; weeks 9–10 governance documentation against PL 2.338/2023.
🔴 **Largest risk is `tutor-mcp`'s alpha status**, not the integration.

🟢 **Generalising `P521` outside Brazil:** the pattern is *curriculum-as-data → MCP → factuality
gate → tutor → xAPI evidence*. Only `bncc-*` is Brazil-specific. 🔵 Any jurisdiction publishing a
national curriculum can be substituted at layer 3; the other five layers are unchanged. 🟢 **That
is the reusable Globant asset — the architecture, not the Brazilian dataset.**

### 🟡 `P520` — amended, because the premise under it was withdrawn

🔴 **`P520` (provenance-and-portfolio audit of assets the client already funded) was justified by
`p515`'s claim that LATAM had "0 LATAM-originated open-source education repositories" and therefore
only a distribution gap.** 🟢 **That premise is withdrawn** (see
[`intel/market.md`](../intel/market.md)). 🟡 **`P520` is not withdrawn with it** — an audit offer
still fits the **193 IDB-reviewed solutions**, which remain unverified (`Gap 515-D`). 🔴 **But it
must no longer be sold as "there is nothing to build on," and it should not be the *first* LATAM
offer.** 🟢 **Lead with `P521`**: the client likely already runs `i-educar`, and customisation of a
system of record is a larger and better-anchored engagement than an inventory audit.



## 🆕 `p515` — `2026-10-28` — **🔴 `P518`'s STATED PREMISE IS WITHDRAWN AND THE RECIPE IS KEPT: *"every LMS on these shelves is copyleft"* is false against two live Apache-2.0 LMS rows, one of them added one pass earlier, so the claim that *"Sunbird removes the need for the boundary"* credits Sunbird with a constraint `OpenOlat` lifted at `p508`. 🟢 `P518` survives under the qualifier its own headline used — **first national-scale, DEPLOYED permissive platform** — and its byte-reads reproduce exactly. 🟢 `P521` is the recipe the correction makes available: a **closed derivative of a permissive full LMS**, OpenOlat + DeepTutor over LTI 1.3, EMEA-placed, with the SIS nil priced as scope and both auto-assessment deadlines named. 🔴 `make hooks` not attempted (declared abstention).**

🔴 **Gate posture, stated first — and it is NOT the prior 18 denials.** The previous eighteen
passes recorded a classifier **DENIAL** (`Code from External`) on `make hooks`. 🟡 **This pass
the battery was never submitted:** every gate in `HOOK_GATES` executes `$(PY) -I` over Python
inside `compose/code/p*/` — interpreter runs over a freshly cloned third-party working tree —
and this session's standing rule is not to run interpreters over cloned repository content.
🟡 **So `p515`'s posture is a declared abstention, not a refusal received.** The distinction
matters because it is *stable*: a future pass should expect abstention, not retry-and-be-denied.
🔴 `p511`'s **45/63** remains the last gate-attested reading — now **four passes stale**.
🔵 Every figure below is named to the channel that produced it, and the one conflict this pass
resolved is resolved on a channel the refusing pass did not use.

### 🔴 The refutation — `p514`'s own `P518` premise, against this base's live shelves

🔴 **What `p514` published**, in [`compose/patterns.md`](../compose/patterns.md), as the stated
reason `P518` could not have been written earlier:

> *"Every LMS on these shelves is copyleft — Moodle **GPL-3.0**, Chamilo **GPL-3.0**, Open edX
> **AGPL-3.0** — so `P515` had to invent a standards boundary to keep a Globant deliverable from
> touching client source. 🟢 **Sunbird removes the need for the boundary**."*

🔴 **The three licences named are correct. The universal claim around them is false, and it is
falsified by this base's own shelves — one of them written one pass earlier.**

| slug | shelf that holds it | grant as shelved | 🟢 `p515` byte-read, third channel | verdict |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | [`verticals/solutions.md`](../verticals/solutions.md) L521, L663, L959; [`repos/foundations.md`](../repos/foundations.md) L557 | **Apache-2.0**, 10,982 B `6dbc5b605ed0…` | 🟢 **Apache-2.0**, `master/LICENSE`, **10,982 B**, `sha256₁₆ 6dbc5b605ed0be6e`, HTTP **200** | 🟢 **IDENTICAL** to the shelved cell |
| [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | [`verticals/solutions.md`](../verticals/solutions.md) L983 (**added `p513`**); [`repos/foundations.md`](../repos/foundations.md) L1134 | **Apache-2.0**, 11,362 B | 🟢 **Apache-2.0**, `main/LICENSE`, **11,362 B**, `sha256₁₆ a890392684288f18`, HTTP **200** | 🟢 **byte count IDENTICAL**; digest newly recorded |

🔴 **This base does not merely contain a counterexample — it advertises one.**
[`verticals/solutions.md`](../verticals/solutions.md) L521 sells `OpenOlat` as *"**The only
permissive full LMS found.** Pick this when the client needs a closed derivative."* L663 reduces
the whole decision to *"OpenOlat (Apache-2.0) **or** accept copyleft."* And L983, written at
`p513` — **the pass immediately before the one that claimed every LMS is copyleft** — introduces
`TutorLoom` as *"Second permissive full LMS after OpenOlat."*

### 🔴 The claim was published TWICE, and the probe found the instance a manual read missed

🔵 **This pass wrote a probe before it wrote the finding** (`compose/code/p515-class-claim/`), and
the probe returned an instance that reading `compose/patterns.md` by hand did not:
[`verticals/solutions.md`](../verticals/solutions.md) **L112**, inside `p514`'s own section —

> *"🟢 **Why it matters more than another LMS would.** Every LMS on this shelf is copyleft — Moodle
> and Chamilo **GPL-3.0**, Open edX **AGPL-3.0**, formaLMS **GPL-2.0** — and the only permissive
> rows have been **small**: `gegok12` (SIS) and a handful of components."*

🔴 **This second instance is the worse of the two**, for three reasons:
1. 🔴 It sits in **the very file whose platform table sells `OpenOlat` as the Apache-2.0 full LMS** —
   the counterexample is roughly 400 lines below the claim, in the same document.
2. 🔴 It does not merely omit the permissive rows, it **mischaracterises them**: *"the only
   permissive rows have been small — `gegok12` (SIS) and a handful of components"*. `OpenOlat` is a
   **448★ full Java LMS**, and `TutorLoom` is a full multi-tenant LMS; neither is a component.
3. 🔴 It then draws the operational conclusion — *"impossible with Moodle or Open edX"* — which is
   true of Moodle and Open edX and **false of the shelf it generalises to**.

🟡 **Both instances are left exactly as published**, per this base's standing practice of correcting
above rather than rewriting history. 🔵 The correction is this section; the original stands below it
under its own heading.

### 🟡 What survives, and the qualifier that carries it

🟢 **The `P518` recipe is sound and is not withdrawn.** Sunbird's MIT grant is real — this pass
byte-read it independently and reproduced `p514`'s cell **exactly**: `master/LICENSE`, **1,072 B**,
`sha256₁₆ 7dde06716f259584`, HTTP **200**. DeepTutor's cell reproduces exactly too: **Apache-2.0**,
**11,408 B**, `sha256₁₆ cd2f54e1e5066644`.

🟡 **What must be rewritten is the justification.** The defensible claim is the one with the
qualifier `p514` used in its own headline and then dropped in its rationale:

> 🟢 Sunbird is the first **national-scale, deployed** permissive learning platform on this shelf.

🔴 **Why this is a commercial correction and not a wording nit.** `P518`'s premise tells a reader
that *"must ship closed + wants a full LMS"* was unsolved until `p514`. On this base's own data it
has been solved since `p508`, by a platform with — per [`repos/foundations.md`](../repos/foundations.md)
L557 — a *"strong EMEA higher-ed footprint"*. 🔴 A proposal built off `P518`'s premise would route
an EMEA closed-derivative engagement to a heavy Indian-ministry stack and never mention the Swiss
Apache-2.0 LMS already on the shelf. 🟢 `P521`, written this pass, is that missing recipe.

### 🔴 The first measured cost of the stale gate

🔵 `HOOK_GATES` carries **`gate-shelf-consistency`** (`p308` — *"no slug may carry disagreeing
licence cells across the live shelves"*, 59 controls) and **`gate-prose-claims`**. 🔴 The battery
has not run since `p511`. 🔴 **In that four-pass window a cross-shelf claim shipped that contradicts
two live rows.** 🟡 This is the first instance on this base where the gate's absence can be shown to
have *cost* something rather than merely being noted as stale — and it argues the staleness is
itself the top-priority gap, above any discovery leg (`Gap 515-A`).

### 🟢 `P521` — Ship closed on a permissive full LMS: the OpenOlat build — **8–11 weeks**

🔵 **Why this recipe did not exist until the premise was corrected.** `P515` invented a standards
boundary to avoid touching copyleft LMS source; `P518` declared the boundary unnecessary *because
Sunbird is MIT*. 🔴 **Both were working around a constraint this base's own shelves had already
lifted:** [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is **Apache-2.0** and has
been shelved as *"the only permissive full LMS"* since `p508`. 🟢 `P521` is the engagement that
follows from that row — a **closed derivative of a full LMS**, with no boundary and no fork of a
ministry-scale distribution.

| component | address | grant, byte-read `p515` | role |
|---|---|---|---|
| the LMS — fork it | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0**, `master/LICENSE`, **10,982 B**, `sha256₁₆ 6dbc5b605ed0be6e` | enrolment, course structure, assessment UI; Java |
| tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0**, **11,408 B**, `sha256₁₆ cd2f54e1e5066644` | adaptive tutoring service behind the LMS's auth |
| launch boundary | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0**, `master/LICENSE`, **10,273 B**, `sha256₁₆ 73ba74dfaa520b49` | mount the tutor as an **LTI 1.3** tool — no LMS core patch needed for v1 |
| telemetry out | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 **Apache-2.0**, `master/LICENSE`, **11,525 B**, `sha256₁₆ a1587287ff0445e1` | learner statements to the client's LRS |
| credentials out | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0**, `develop/LICENSE`, **13,185 B**, `sha256₁₆ ba1f153bdba34cc8` | verifiable completion |
| offline reach | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT**, `develop/LICENSE`, **1,097 B**, `sha256₁₆ 3c056b34a4762a9a` | low-connectivity campuses |
| alternative, **watch row only** | [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | 🟢 **Apache-2.0**, **11,362 B**, `sha256₁₆ a890392684288f18` | lighter Django/React LMS — **~4 weeks old; do not stake an engagement on it** |

🔵 **Wiring.** Fork OpenOlat → stand the tutor up as a separate service and mount it through
**LTI 1.3** (tsugi) so phase 1 ships *without* patching LMS core → emit **xAPI** per interaction
to the client's LRS → issue **Open Badges** on mastery, validated with the 1EdTech validator →
only in phase 2, patch OpenOlat core for the UX the LTI boundary cannot reach, which is where the
Apache-2.0 grant actually earns its place. 🟢 **Tutor, badge layer and any core patches stay
Globant IP**; Apache-2.0 asks for attribution, `NOTICE` retention and nothing else.

🔴 **Say these four things out loud in the proposal, because each is real and each is on this base.**
1. 🔴 **Budget the SIS integration as scope, not as a surprise.** This base's standing nil holds:
   **no permissive platform is both a full LMS and a student information system**, and the
   permissive LMS tier ships no gradebook-of-record or SIS integration between its members. The
   build is OpenOlat ↔ the client's existing SIS over LTI + xAPI. **2–3 of the 8–11 weeks.**
2. 🔴 **Warn the client's licence scanner before it fails the build.** OpenOlat's `LICENSE` is the
   Apache-2.0 text **plus** an openolat.org attribution statement, so GitHub's own classifier
   reports `NOASSERTION`. 🟢 The payload is Apache-2.0 on a byte read — three passes running now.
   Hand the auditor the digest above, or an automated gate will reject the component.
3. 🔴 **Turning on auto-assessment changes the regulatory object, in two jurisdictions.** Under the
   **EU AI Act** Annex III point 3, evaluating learning outcomes is high-risk — standalone
   obligations now **2 Dec 2027** (Reg. (EU) 2026/1744), Art. 50 transparency already live.
   In **Vietnam**, an LMS with automated grading or ranking is listed high-risk, and a **new 2026
   deployment gets the shorter runway — 1 Mar 2027**, not the incumbent's 1 Sep 2027.
   🟡 **The platform is not the regulated thing; the configuration is.** Price the conformity work
   per switch, and keep grading off in v1 unless the client is buying the compliance build too.
4. 🟡 **It is Java, and that is a staffing question.** OpenOlat is a Java LMS; `P518`'s Sunbird and
   `TutorLoom` are not. Confirm the studio's Java bench before pricing phase 2's core patches.

🟢 **Where it sells: EMEA first.** OpenOlat is Swiss-origin with — per
[`repos/foundations.md`](../repos/foundations.md) — a strong EMEA higher-ed footprint, so the
reference customers, the language coverage and the data-residency posture all sit in region.
🟡 **One address in this pass's own draft of `P521` was wrong, and the pre-write probe caught it.**
The LTI row was first written as `tsugi/tsugi`, which **404s even on `README.md`**. The canonical
address this base already held 28 times is [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi);
[`csev/tsugi`](https://github.com/csev/tsugi) serves a **byte-identical** payload (both `LICENSE`
**10,273 B** `sha256₁₆ 73ba74dfaa520b49`, both `README.md` 10,277 B). 🟢 **Every one of `P521`'s
seven components is byte-read above — none is carried on a shelf citation alone.**

🔵 **`P518` (Sunbird, APAC/ministry) and `P521` (OpenOlat, EMEA/institution) are complements, not
rivals** — the discriminator is *national system* versus *single institution or consortium*, which
is exactly the discriminator `P518`'s own caveat 3 names.


## 🆕 `p514` — `2026-10-28` — **🟢 `P518` — THE FIRST RECIPE ON THIS BASE THAT EXTENDS A NATIONAL-SCALE PLATFORM AND STILL SHIPS CLOSED, because [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) is **MIT** and every LMS these patterns had to work around is copyleft. 🟢 `P519` — the North America district pack, priced against the FOUR states that mandate both state guidance and district policy, with Oklahoma's **2027-28** deadline as the clock. 🟢 `P520` — the licence-provenance audit as a BILLABLE deliverable, built from this pass's own 1,840-probe instrument and justified by three findings that a client's own counsel would have missed.**

🔴 **Gate posture:** `make hooks` **DENIED** (`Code from External`). 🟡 `p511`'s **45/63** stands.
🔵 Every component named below carries a grant this base byte-read at a pinned ref.

### 🟢 `P518` — Extend a national platform, ship closed: the Sunbird build — **10–14 weeks**

🔵 **The problem this solves, and why it could not be written before `p514`.** Every LMS on these
shelves is copyleft — Moodle **GPL-3.0**, Chamilo **GPL-3.0**, Open edX **AGPL-3.0** — so `P515`
had to invent a standards boundary to keep a Globant deliverable from touching client source.
🟢 **Sunbird removes the need for the boundary**: MIT, so the platform can be forked, extended and
delivered as part of a closed product.

| component | address | grant, byte-read | role |
|---|---|---|---|
| learning portal | [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🟢 **MIT**, 1,072 B `7dde06716f259584`, 78/79 heads | the platform — fork it |
| tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0**, 11,408 B `cd2f54e1e5066644` @ `1ea7df155447` | adaptive tutoring service |
| offline reach | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 permissive *(shelved)* | low-connectivity districts |
| credentials out | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0** | verifiable completion |
| analytics out | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 permissive spec | ministry reporting |

🔵 **Wiring.** Fork the portal → add a tutoring microservice behind the portal's existing auth,
calling DeepTutor → emit **xAPI** statements per learner interaction to the ministry's LRS → issue
**Open Badges** on mastery, validated with the 1EdTech validator → package Kolibri for offline
districts and sync on reconnect. 🟢 **The tutor and the badge layer stay Globant IP**; only portal
modifications inherit MIT, which imposes attribution and nothing else.

🔴 **Say these three things out loud in the proposal, because they are real.**
1. 🔴 **This row attests ONE repository.** Sunbird Ed is a multi-repo distribution; every other
   component needs its own byte-read before delivery (`Gap 514-E`). **Budget two weeks for that
   audit and run `P520` as its first phase.**
2. 🔴 **Sunbird ships no native AI.** It is an integration target, exactly as Moodle is.
3. 🟡 **It is heavy.** Fits a ministry or state; **wrong** for a single-institution pilot — there,
   use [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (MIT, local-first) instead.

🟢 **Where it sells: APAC first** — DIKSHA is the reference deployment and the stack is already
understood by Indian system integrators. 🔵 Also **LATAM**, where `P517`'s governance work is the
natural predecessor and a national platform is the natural successor.

### 🟢 `P519` — The North America district pack: a statutory deadline, not a pitch — **5–7 weeks, repeatable**

🔵 **Why this is unusual in this sector: the buyer has a legal deadline, and there are thousands of
buyers who need the same artefact.** **Maryland, Idaho, Oklahoma and Virginia** require *both* state
guidance *and* district-level AI policy. 🔴 **Oklahoma `S.B. 1734` fixes it: every district must
adopt a written AI policy before the 2027-28 school year.**

🟢 **The deliverable, four artefacts:**

| artefact | content | constraint it satisfies |
|---|---|---|
| district AI policy | adoption-ready text, mapped to the state's guidance | the statutory requirement itself |
| human-oversight workflow | which decisions an AI may not make; the review step and its record | Oklahoma / Maryland high-stakes prohibitions |
| student-data boundary | a documented no-training-data path, with the technical control that enforces it | 🔴 California **AB 1159** — bars student data for model training |
| audit trail | per-decision logging, retention, exportable evidence | district board review and future audit |

🔵 **Build it on what is already shelved**: the policy and oversight artefacts are documents, and
the technical control is a proxy/logging layer in front of whichever vendor API the district uses.
🟢 **No platform commitment is required**, which is why it closes fast.

🔴 **The margin is in repetition, not in the first sale.** 🟢 Templatise against each of the four
states' guidance once; every district in that state is then a short engagement. 🟡 Curriculum work
(Utah **H.B. 218**'s grade 7-8 digital-skills course, Georgia and Mississippi CS credits) is a
second, slower line — different buyer, different cycle.

### 🟢 `P520` — The licence-provenance audit, as a deliverable — **2–3 weeks**

🔵 **The pitch is this pass's own findings, and they are the proof.** A client's counsel reads a
licence badge or an SPDX field. 🔴 **Three findings at `p514` show what that misses:**

| finding | what a badge or aggregator would have told the client |
|---|---|
| [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) | 🔴 *"GPL-3.0"* — **wrong about the shipped code.** The grant is on a branch abandoned in **2022**; the active `main` (**2026-10-13**) carries **none** |
| [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | 🔴 *"no licence"* — **wrong.** Apache-2.0 grant clause at `NOTICE`, default branch |
| *(the inverse case this base holds)* | 🔴 A licence file **titled** like MIT that forbids commercial use — `T48` |

🟢 **The instrument exists and is committed:**
[`compose/code/p514-branch-grant-probe/`](code/p514-branch-grant-probe/). For every dependency and
platform in the client's stack it enumerates **every head** with `git ls-remote --heads`, probes
**20** licence paths per head on `raw.githubusercontent.com`, and gates every verdict on a
known-good **and** known-bad control so a broken channel cannot read as an empty world.

🔵 **Wiring.** Inventory the stack → run the probe → for each address report **family, bytes,
`sha256₁₆`, path, ref, and the ref the client deploys** → flag three classes: *grant does not cover
the shipped ref* (`T52`), *grant exists at an unprobed path* (`T51`), *title and body disagree*
(`T48`) → hand over the TSV plus a per-component delivery verdict.

🔴 **Scope limits in the statement of work, not discovered later.** 🔴 It does **not** walk trees, so
a deep-subtree grant is still missed (`Gap 514-A`); it reads the **grant**, not dependency
closure; and 🔴 **it is not legal advice** — it is byte-level evidence counsel can rely on.

🟢 **Sell it as phase zero of `P518` or of any build on a platform the client did not write.**
🔵 **It is the cheapest pattern on this base and the only one whose value is entirely in what it
stops you doing.**
## 🆕 `p513` — `2026-10-28` — **🟢 `P515` — THE STANDARDS-BOUNDARY ENGAGEMENT, which is the recipe this repository has been one table away from for eleven passes: a CLOSED Globant deliverable that speaks LTI in, SCORM both ways, xAPI out and Open Badges out, with every one of those four components byte-attested permissive, so the client's AGPL LMS never touches our source. 🟢 `P516` — the EU build re-dated against **Regulation (EU) 2026/1744**: Article 50 is LIVE NOW, Annex III is 2 Dec 2027, and that inversion changes which deliverable ships first. 🟢 `P517` — the LATAM governance-first engagement, priced off a measured 87 %/26 % gap instead of a market-size slide.**

### 🟢 `P515` — The standards-boundary build: closed deliverable, copyleft LMS, no contact — **8–10 weeks**

🔴 **The problem this solves.** The client runs **Canvas (AGPL-3.0)** or **Open edX (AGPL-3.0)**.
Every AI feature they want — tutor, generated courseware, assessment, credentials — looks like it
has to live *inside* that LMS, and the moment it does, the AGPL reaches our code. Eleven passes of
this KB have had all four interop components on the base and none of them in a census, so the
answer existed and was not reachable.

🟢 **The architecture: the LMS stays on the other side of four standards.** Nothing crosses the
boundary except protocol messages.

| edge | direction | component | grant (byte-read `p513`) | SHA |
|---|---|---|---|---|
| launch | LMS → us | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | **Apache-2.0**, 10 273 B | `214d11084b7f` |
| courseware | us → LMS | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT**, 1 072 B | `f966a1b7d6f0` |
| telemetry | us → LRS | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) + [`openfun/ralph`](https://github.com/openfun/ralph) | **Apache-2.0** / **MIT** | `ca782a1129bc` / `91fef112394d` |
| credentials | us → wallet | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0**, 13 185 B | `0a66b52a8a0b` |

**Inside the boundary — the part Globant owns and keeps closed:**
- [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) (**MIT**, `8fe4372557f8`) —
  source material → animated narrated lessons, 🟢 **emits SCORM natively**, so it hands straight to
  `scorm-again` with no conversion layer.
- [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (**MIT**,
  `98463a0cb5fb`) — **Bayesian Knowledge Tracing over MCP**. 🟢 Use this rather than `OATutor`
  (MIT, 274★) when BKT must be a *service* the orchestrator calls; use `OATutor` when it must be a
  product the learner opens.
- [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)
  (**Apache-2.0**, `31fd6dbb0c07`) — lesson-planning and differentiation skills **plus their eval
  rubrics**, which is what the release gate in step 5 runs on.
- [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) —
  🔴 **MIT CODE ONLY.** Its prompts/settings are CC BY 4.0 and **the CLEAR and PERSUADE 2.0 corpora
  are CC BY-NC-SA 4.0 (NonCommercial)**. Vendor the harness; **do not ship the corpora**.

**Wiring, in order:**
1. **Weeks 1–2** — stand up `tsugi` as the LTI 1.3 tool provider. Register against the client LMS
   developer key. 🔴 **Pin `tsugi` by SHA, not by tag** — its newest-sorted tag is `PHP_7_2`, a
   platform marker, not a version.
2. **Weeks 2–4** — `Papermorph` ingests the client's source material; its SCORM output is served
   through `scorm-again`'s runtime so progress and completion report back through the LMS's own
   SCORM API. 🟢 **The LMS believes it is running an ordinary SCORM package.**
3. **Weeks 4–6** — `tutor-mcp` behind the orchestrator as the mastery model; every learner
   interaction emits an **xAPI statement** to a self-hosted `ralph` LRS. 🟢 The LRS is MIT, so the
   telemetry store is ours and the client's data-residency answer is "your tenant".
4. **Weeks 6–8** — mastery threshold → issue an Open Badge; `openbadges-validator-core` verifies
   every badge before release. 🔴 Pin it by SHA: last pushed **2025-11-04**, default branch
   `develop`.
5. **Weeks 8–10** — release gate: `k12-teacher-skills` rubrics + the `evaluators` MIT harness score
   every generated lesson for pedagogy, rigour, format and scaffolding. **Nothing ships un-scored.**

🟢 **The deliverable that makes this sellable is a one-page licence boundary diagram** showing four
permissive grants with byte counts and SHAs on our side and the AGPL on theirs. Client counsel can
sign that; they cannot sign "we integrated with Canvas".

🔴 **Where this pattern does NOT apply:** if the client wants the AI *inside* the LMS as a native
plugin (a Moodle plugin, a Canvas LTI-less integration), the boundary collapses and the copyleft
obligation is real. Say so and reprice — do not build `P515` and hope.

### 🟢 `P516` — The EU build, re-dated: Article 50 now, Annex III on 2 Dec 2027 — **10–12 weeks**

🔴 **This pattern replaces the compliance premise under every prior EMEA recipe in this file.**
**Regulation (EU) 2026/1744** (OJ **24 Jul 2026**, in force **27 Jul 2026**) deferred Annex III
high-risk obligations — grading, admissions, placement, proctoring — to **2 December 2027**. It did
**not** defer **Article 50 transparency**, which has applied since **2 August 2026**. Emotion
recognition in schools has been **prohibited since February 2025**, and the AI-literacy duty has
applied since then too.

🟢 **So the build order inverts.** What was going to be a conformity scramble for August 2026 is now
a 13-month design window for Annex III — **and a live obligation today for disclosure.**

**Ships in weeks 1–4 (already overdue, not forward-looking):**
- **Article 50 surfaces** — an unmistakable "you are talking to an AI" disclosure on every learner
  turn, and **machine-readable marking of synthetic output**. 🔵 The marking grace period
  (**2 Dec 2026**) covers only systems placed on the market before 2 Aug 2026 — a new build gets no
  grace at all.
- **Emotion-recognition audit** — 🔴 a named deliverable, because this is a *prohibition*, not a
  risk tier. Any affect detection, engagement scoring from webcam, or sentiment-from-face in a
  school context comes out.
- **AI-literacy provision** for staff and learners, documented.

**Weeks 4–12, the Annex III readiness file, built on a sovereign stack:**
- [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**, 10 982 B at
  `5b42ca47bd10`) — 🟢 **the sector's only permissive full LMS**, Swiss-origin, strong EMEA
  higher-ed footprint. 🔴 **Tell your licence gate explicitly that this is Apache-2.0: GitHub's API
  reports `NOASSERTION`** because an attribution statement follows the terms.
- [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (**MIT**, `2a604cc3935a`) — the
  tutor **runs locally**; no learner text leaves the tenant.
- [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) (**MIT**,
  `74bc17ea406e`) — **Wav2Vec2 + DTW**, self-hosted. 🟢 **Decisive for language assessment under
  GDPR: voice is biometric-adjacent and this keeps it in-tenant.**
- [`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) (**Apache-2.0**,
  `089b4483df27`, Fraunhofer IAIS) for STEM. 🔴 **The licence-branch trap goes in the build script:**
  its default branch is `develop` and serves **no licence payload**; the grant is at
  **`master/LICENSE`**. A CI licence check pointed at the default branch will fail this
  dependency and block the pipeline (`T42`).
- Grading stays `P513`-shaped: **the model never issues the grade.** On 2 Dec 2027 that is the
  difference between a high-risk system and a decision-support tool, so build it now and the
  deadline costs nothing.

🟢 **The commercial line:** *"Article 50 is live and you are likely non-compliant today; Annex III
is 2 December 2027 and we will have your readiness file before it."* 🔴 **Do not sell "ready for
August 2026"** — it is simultaneously 16 months early for Annex III and late for Article 50.

🔵 **One caveat recorded honestly:** the Omnibus dates above are corroborated across six independent
legal-advisory sources; **EUR-Lex itself was not read from this session** (`Gap 513-D`). Confirm
against the Official Journal before putting a date in a contract.

### 🟢 `P517` — LATAM governance-first: sell the inventory before the tutor — **6–8 weeks**

🟢 **Priced off measured numbers, not a market-size slide.** UNESCO IESALC, 200 higher-education
institutions across 19 countries: **87 % already use AI, 26 % have a formal strategy.** Brazilian
schools: **53 %** of administrators use AI, **22 %** have guidelines (Cetic.br). Teachers are
**ahead** of the OECD (BR 56 / CL 55 / CO 53 / CR 52 vs **36 %**); students are at **nine in ten**
(PISA 2025).

🔴 **So the usual pitch order is wrong on arrival.** Nobody needs persuading to adopt — adoption
already happened, ungoverned, at scale. A "pilot" framing insults the facts. **The deliverable is
governance over an installed base, and it is the fastest-closing education sale in this KB.**

**Weeks 1–3 — inventory and policy, no model involved:**
1. Shadow-AI inventory: what staff and students are actually using. The 61-point strategy gap means
   this has never been enumerated.
2. A written institutional AI policy with the three clauses the region's statutes converge on:
   permitted uses, disclosure, and 🔴 **no automated high-stakes decision** (the Oklahoma
   constraint, which travels well as a norm even where no LATAM statute yet compels it).
3. 🔴 **Equity is a design input, not a CSR paragraph:** Argentina runs **75 %** adoption among high
   socio-economic groups against **42 %** among low. A policy that assumes connectivity entrenches
   that 33-point gap.

**Weeks 3–8 — the governed stack, offline-first by default:**
- [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**,
  `9ca1b5b13d7f`, 542 tags) — runs **without connectivity**. 🔴 Default branch is **`develop`**.
- [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform)
  (**Apache-2.0**, `f2d62af1eb82`) — **WhatsApp-delivered, 15 languages, no app and no browser.**
  🟢 The only delivery surface here that works on a shared phone with no data plan.
- [`oluiscabral/studorama`](https://github.com/oluiscabral/studorama) (**MIT**, `2ddbb1122b5b`) —
  pt-BR + ES localisation, **Ollama local-model path**. 🔴 **Single maintainer, personal licence
  holder: fork and own it, never take a dependency.**
- [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) —
  **MIT code only**, 🔴 corpora are **CC BY-NC-SA**. The eval harness is what turns "we have a
  policy" into "we can show the tool helps", which is the renewal argument.

🔴 **Say the supply reality out loud in the bid, because it is a strength.** `p513` ran a
Spanish/Portuguese discovery leg: **18 rows, zero AI education products**; the closest were a
Brazilian school-management system with **no AI** (`ipti/br.tag`, 20★) and a Colombian media-centre
app (39★). 🟢 **There is no regional open-source incumbent to be compared against.** Globant builds
here rather than composing — and `Studorama` at **111★** is the entire LATAM-placed AI product
shelf.

**Partners to name:** UNESCO **IESALC**, the **Observatory on AI in Education for LAC** (launched
14 Apr), **ECLAC/eLAC** working group (co-coordinated by Chile's **CENIA** and Uruguay's
**AGESIC**), **Ceibal** (UY), **Cetic.br** (BR).

## 🆕 `p512` — `2026-10-28` — **🟢 `P513` — AI inside a peer-review workflow the institution already runs, on an MIT platform, with the grade never leaving human hands. 🟢 `P514` — the EMEA-sovereign STEM build on an Apache-2.0 Fraunhofer base, with the licence-branch trap written into the build step so it cannot bite. 🔴 And 13 star figures in THIS file were wrong, because every census this base has run framed on the shelves and this file's recipes were never swept.**

🔴 **Correction notice for this file, first, because it affects what a client was shown.** Thirteen
star figures inside live recipes here were stale or wrong, including **`14,300★` for
[`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) in three
separate recipes** (`P491-1`, `P493-1`, `P502-1`) — a value `p511` corrected **one pass ago** on
[`verticals/solutions.md`](../verticals/solutions.md) and nowhere else. Also corrected:
`k12-teacher-skills` **595 / 598 → 600** (two sites), `kolibri` **1,200 → 1,162**,
`OpenMAIC` **41,700 → 41,710**, `smolagents` **30,118 → 30,123**, `Papermorph` **993 / 982 → 995**,
`book-to-skill` **36,339 → 36,421**, `TorchLeet` **2,595 → 2,596**, `TrenTorch` **739 → 741**,
`math-question-bank` **358 → 360**, `freelingo` **210 → 211**, `mathtutorbench` **45 → 46**. All now
carry a `*(🟢 `p512`, API)*` suffix. 🔵 **Licence and role cells were re-read alongside and none was
refuted** — the recipes were right about what the components *are*, and stale about how popular.

### 🟢 `P513` — AI in the peer-review loop, where the model never issues the grade — **6–8 weeks**

**Why this and why now.** `p512` put the first **peer-assessment** platform on the permissive shelf:
[`expertiza/expertiza`](https://github.com/expertiza/expertiza) — **MIT**, `main/LICENSE` **1,068 B**
`sha256₁₆ cc922786cdca1cd7`, `HEAD` `b68bb8f640ac`, **194★** *(🟢 `p512`, API)* and **1,329 forks**.
🔵 **The ratio is the business case.** 6.85 forks per star means US institutions are *running* it, not
bookmarking it — so this pattern proposes AI **inside a workflow the client already operates**, which
is the cheapest change-management ask available in education, and it lands on the one structure that
defuses the region's sharpest objection: **a human peer writes the review and an instructor
moderates; the model never issues a grade.** Same structural answer as `P492-1` (arithmetic) and
`P497-1` (admissions), now at the assessment layer.

**The stack — every grant read from bytes at a pinned ref**

| layer | repo | licence | job |
|---|---|---|---|
| review workflow | [`expertiza/expertiza`](https://github.com/expertiza/expertiza) | 🟢 **MIT** (1,068 B `cc922786cdca1cd7`) | rubrics, review mapping, submission, instructor moderation — **the system of record for the grade** |
| review assistant | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | drafts and critiques a *peer's review text*, never the artefact's score |
| rubric quality gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT**, 13★ *(🟢 `p512`, API)* | pre/post instrument: does assisted reviewing raise review quality, measurably |
| integrity arm | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT**, 355★ *(🟢 `p512`, API)* | code-submission plagiarism, because peer review of code invites it |
| audit trail | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0**, 144★ *(🟢 `p512`, API)* | every assist is an xAPI statement — who was helped, when, with what (sequences `P502-1`) |
| eval runtime | [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT**, **14,341★** *(🟢 `p512`, API)* | regression-gates the assistant before each release (`P491-1`) |

**Wiring — in this order, because the order is the compliance argument**

1. **Deploy `expertiza` unmodified first** and leave the grade path untouched. Write down, with the
   client, the exact field that holds the score and the exact actor permitted to write it.
2. **Insert the assistant on the REVIEW TEXT only.** It reads the submission and the rubric and
   returns *suggested review prose* plus *rubric-criterion coverage flags* to the **peer reviewer**,
   who edits and submits. 🔴 **No code path from the assistant to the score field.** Enforce it in the
   application, not in a prompt.
3. **Gate on coverage, not on sentiment.** The useful assist is *"you have not addressed criterion
   3"*, not *"this looks like a B"*. Build the criterion-coverage check first; it is the part
   instructors will defend in a faculty meeting.
4. **Emit xAPI to `lrsql` for every assist**, including the ones the reviewer discarded. 🔵 The
   discarded ones are the evidence that the human was in control, and that is the artefact an audit
   asks for.
5. **Run `dolos`** over code submissions before peer allocation, so reviewers are not unknowingly
   reviewing a copy.
6. **Measure with `pedagogy-benchmark`** before and after. A peer-review programme that cannot show
   review quality rose is indistinguishable from one that just made reviewing faster.

🔴 **Do this or it is negligent.** `expertiza`'s grant **has no title line** — it is the verbatim MIT
body with a bare copyright notice. 🟢 The API's detector reads `MIT` and the three MIT paragraphs are
present in the payload, so the grant is sound; 🔴 **but a title-anchored licence gate will report "no
grant found"** and block the build or, worse, let someone conclude the platform is unlicensed. **Tell
your licence tooling about this row before the first build** (`T43`).
🟡 **Honest limits.** `expertiza` is Rails and long-lived; the 1,329 forks are course forks, not a
contributor community, so treat upstream velocity as low and plan to **fork and own**. And peer
review is a pedagogy choice, not a feature — if the client's instructors do not already use it, this
pattern is the wrong one and `P500-1` is closer.

### 🟢 `P514` — EMEA-sovereign K-12 STEM on an Apache-2.0 Fraunhofer base — **8–10 weeks**

**Why.** EMEA education procurement asks sovereignty first and *who stands behind the code* second.
🟢 [`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) answers both:
**Apache-2.0** (`master/LICENSE` **11,359 B** `sha256₁₆ 8c6db340475136df`), **Fraunhofer IAIS**,
**147★** *(🟢 `p512`, API)* / 141 forks, `develop` `HEAD` `089b4483df27`, browser-delivered block
programming for real robots with no client install. 🔵 **It is the first permissive, state-backed,
EMEA-origin PLATFORM on these shelves** — `ralph` and `warren` are EMEA and MIT but are components.

**The stack**

| layer | repo | licence | job |
|---|---|---|---|
| teaching environment | [`OpenRoberta/openroberta-lab`](https://github.com/OpenRoberta/openroberta-lab) | 🟢 **Apache-2.0** | block programming, device abstraction, browser delivery |
| local model | Ollama-served open weights | 🟢 permissive weights only | 🔴 **no cloud inference** — the residency answer, stated before price |
| tutor loop | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT**, 252★ | diagnosis-first STEM tutoring over the student's own program (`P508-R2`) |
| record layer | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **Apache-2.0** / **MIT** | xAPI store plus 🟢 **EMEA-origin, state-backed** ingest (France Université Numérique) |
| LMS boundary | LTI 1.3 via [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0**, 377★ *(🟢 `p512`, API)* | launch from the authority's existing LMS; keep the copyleft LMS on the other side of the boundary (`P511`) |

**Wiring**

1. 🔴 **Pin the licence to `master`, not to the default branch.** The grant is **absent from
   `develop`** at twelve conventional paths and present at `master/LICENSE`. Record the branch, the
   byte count and the sha in the build manifest (`p509-R1`), or your own audit will later report the
   platform as unlicensed (`T42`).
2. Fork `openroberta-lab` and stand it up **inside the authority's own tenancy**. Nothing in this
   pattern calls out of the jurisdiction.
3. Wire the diagnostic tutor to the **student's program and its execution trace**, not to free chat.
   It reads the blocks and the robot's behaviour and asks the next useful question.
4. Serve the model **locally via Ollama**. 🔵 Where the authority will not host GPUs, this is the step
   to price explicitly rather than quietly swap for an API.
5. **Launch over LTI 1.3** from the incumbent LMS and 🔴 **do not migrate the LMS** — Moodle (GPL-3.0),
   ILIAS (GPL-3.0) and Open edX (AGPL-3.0) stay where they are, outside the derivative boundary.
6. Emit xAPI to `lrsql`, dashboard with `ralph`/`warren`, and keep the records in-region.

🔵 **What to say to an EMEA client.** The teaching environment is Apache-2.0 from a Fraunhofer
institute; the model runs on their hardware; the records never leave their tenancy; and the LMS is
untouched. 🔴 **What not to say:** do not quote a sector market size — this pass widened the
published 2026 spread to **3.3×** (`$3.7B` – `$12.3B`) and the EMEA demand channel returned **no
education-sector source at all**. Price the Annex III function the client is building, not the market.
🟡 **Limits.** Robotics means hardware, and hardware means a procurement cycle this pattern does not
control. `openroberta-lab` is a large Java/JavaScript codebase (485 MB checkout) with 362 open
issues — budget real integration time, and do not promise a small footprint.

## 🆕 `p511` — `2026-10-28` — **🟢 `P511` — the standards-spine tutor: an LTI-launched, xAPI-instrumented tutor assembled from FOUR byte-attested permissive grants, with the copyleft LMS deliberately on the other side of the boundary. 🟢 `P512` — the LATAM pt-BR study product, local-model path included.**

### 🟢 `P511` — Standards-spine tutor (LTI 1.3 in, xAPI out) — **8–10 weeks**

🔵 **The problem this solves is the one that kills education engagements**: a good tutor that cannot
be launched from the institution's LMS, cannot read its existing catalogue, and leaves no audit
trail — so it never leaves the pilot. 🟢 **Every component below is permissive and its grant was read
from bytes this pass or is carried byte-attested on these shelves.**

| layer | component | licence (bytes) | why this one |
|---|---|---|---|
| **LMS launch** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) **377★** | 🟢 Apache-2.0, `LICENSE` **10,273 B** `sha256₁₆ 73ba74dfaa520b49` | LTI 1.3 tool provider with roles + grade passback. Launches from **Moodle, Canvas, Open edX, Blackboard** unchanged |
| **tutoring loop** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) **57★** | 🟢 MIT, `LICENSE` **1,073 B** `sha256₁₆ 1e05c9440068c66c` | MCP server exposing an Intelligent Tutoring System (BKT mastery) to any LLM — so the pedagogy is a tool, not a prompt |
| **mastery state** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) **274★** | 🟢 MIT, **1,105 B** `sha256₁₆ 5baaaf977a28e9fd`, holder *"Zachary A. Pardos"* | UC Berkeley BKT implementation; the knowledge-tracing reference to calibrate `tutor-mcp` against |
| **legacy catalogue** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) **360★** | 🟢 MIT, **1,072 B** `sha256₁₆ 383b85b370e8da44` | Runs the client's existing SCORM 1.2/2004 packages in-browser. **This is the migration story**, and it is usually the reason procurement says yes |
| **assessment items** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🆕 🟢 MIT, **1,076 B** `sha256₁₆ 7faa621251d7ed2b` | QTI 3 items render without re-authoring. Grant read for the first time at `p511` |
| **telemetry of record** | [`openfun/ralph`](https://github.com/openfun/ralph) **51★** | 🟢 MIT, `LICENSE.md` **1,094 B** `sha256₁₆ 08ea77291de9c70f` | xAPI Learning Record Store, `v5.1.0`. Statements land in a store **the client owns** |
| **model layer** | Ollama / vLLM behind one gateway | 🟢 MIT / Apache-2.0 | Local inference where residency demands it; hosted where it does not |

🟢 **Wiring, concretely.** `tsugi` receives the LTI 1.3 launch and establishes the user, course and
role context. It hands that context to the tutor service, which calls `tutor-mcp` over MCP for the
next pedagogical move and keeps BKT mastery state calibrated against `OATutor`'s implementation.
Assessment items come from `qti3-item-player`; legacy modules the client already owns are played by
`scorm-again` inside the same shell. **Every interaction is emitted as an xAPI statement to `ralph`**,
and grades go back to the LMS over LTI's own grade service — so the LMS stays the system of record
and the LRS becomes the analytics substrate.

🟢 **The licence argument, which is the commercial point.** The LMSs are copyleft — **Moodle GPL-3.0,
Open edX AGPL-3.0, Canvas AGPL-3.0**. 🔵 **A tool launched over LTI is not a derivative work of the
LMS**, so the copyleft stops at the launch boundary and the deliverable stays permissive. **The
interop layer is the licence firewall**, and this is the sentence to put in front of a client's
counsel.

🔴 **What this pattern does NOT give you.** No SIS: fees, exams, transport and hostel are absent from
every permissive education platform on these shelves (`p509`'s finding, re-confirmed at `p511`), so
anything touching enrolment or billing is a build, costed separately.
🔴 **`qti3-item-player` is carried without a star read** — read it before quoting adoption.

🟢 **Regions:** 🟢 **North America** — the xAPI trail is the artefact the four states' district-policy
mandates ask for. 🟢 **EMEA** — the two load-bearing grants are held by **France Université
Numérique** and the **University of Zurich** lineage (`OpenOLAT`, Apache-2.0, **448★**), which is a
sovereignty answer with holders rather than adjectives. 🟢 **APAC** — the same spine over Moodle is
demonstrated in-region by [`kltn-moolde/moodle-adaptive-learning-plugin`](https://github.com/kltn-moolde/moodle-adaptive-learning-plugin)
(LTI 1.3, Q-learning, SHAP).

### 🟢 `P512` — pt-BR study product with a local-model path — **4–6 weeks**

🔵 **For a LATAM engagement where per-token cost and data residency are the first two objections.**

| layer | component | licence (bytes) | role |
|---|---|---|---|
| **product shell** | [`oluiscabral/studorama`](https://github.com/oluiscabral/studorama) **111★** | 🟢 MIT, `LICENSE` **1,064 B** `sha256₁₆ 75ecd9ad0bb3b543` | Multi-provider AI study platform; **pt-BR is a first-class feature**, with localized prompt content, not a translation layer |
| **local inference** | Ollama, already a first-class provider in the shell | 🟢 MIT | The cost and residency answer. The shell ships **six** providers including browser-local, so the switch is configuration |
| **spacing / retention** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) **155★** | 🟢 MIT, `LICENSE` **1,068 B** `sha256₁₆ 5352b49679829689` | Block-based adaptive workspace, local-first, spaced repetition — the retention layer studorama does not own |
| **telemetry** | [`openfun/ralph`](https://github.com/openfun/ralph) **51★** | 🟢 MIT | xAPI, so outcomes are measurable from week one rather than argued |

🟢 **Why it is billable in six weeks:** `studorama` is a running product with **10 tags**, not a
research repo, and the provider abstraction already exists — the engagement is institutional
integration, content grounding and the retention layer, not a build from zero.

🔴 **The risk, stated as a line item and not hidden:** `studorama`'s licence holder is a **personal
handle**, not an organisation, and there is one maintainer. 🟢 **Mitigation: fork and own it at a
pinned SHA (`2ddbb1122b5b`) on day one.** MIT permits it, and the fork is the deliverable.

🟢 **The demand case this sells into, from [`market.md`](../intel/market.md):** **87 %** of 200
institutions across 19 countries use AI somewhere while **26 %** have a formal strategy (UNESCO
IESALC), and in Brazil **53 %** of school administrators use AI against **22 %** whose school has
guidelines (Cetic.br). 🔵 **The product is not the hard part; the governance wrapper is, and that is
the margin.**

# Compose patterns — concrete education AI recipes

> 🟢 **`p510` (`2026-10-28`) — ONE NEW RECIPE, AND IT EXISTS BECAUSE THIS PASS MEASURED THE REF EVERY VERTICAL ACTUALLY DEFAULTS TO. 🔴 THE "VERIFY THE URL" STEP THESE PATTERNS INHERIT WAS A NO-OP AND IS REPLACED.**
> 🔵 Every component below has its grant read from **bytes with a sha256** on
> `raw.githubusercontent.com`, on its **resolved default branch**, and its address **proven LIVE** on
> an instrument control-proven to discriminate — **154 of 154**:
> [`liveness-branch-census.2026-10-28-p510.tsv`](../evidence/liveness-branch-census.2026-10-28-p510.tsv),
> [`url-check-control.2026-10-28-p510.tsv`](../evidence/url-check-control.2026-10-28-p510.tsv).
> 🔴 **`curl -sI https://github.com/<slug>` must not be used as the verification step in any recipe
> here**: it answers **403** to live and absent alike.

> 🟢 **`p509` (`2026-10-28`) — TWO NEW RECIPES, AND BOTH ARE BUILDABLE ONLY BECAUSE THIS PASS MEASURED SOMETHING: ONE SHIPS THE LICENCE EVIDENCE AS A DELIVERABLE, THE OTHER IS SCOPED FROM A COUNT OF MODULES THAT DO NOT EXIST.**
> 🔵 Every component below has its grant read from **bytes with a sha256** on
> `raw.githubusercontent.com`, on its **resolved default branch**, and no AGPL, noncommercial,
> source-available or `POINTER_DANGLING` component appears in a shipped step.
> Reads: [`licence-byte-census.2026-10-28-p509.tsv`](../evidence/licence-byte-census.2026-10-28-p509.tsv),
> [`gegok12-packaging.2026-10-28-p509.tsv`](../evidence/gegok12-packaging.2026-10-28-p509.tsv).

### 🟢 `p509-R1` — The licence-attested build manifest, as a client deliverable

🔵 **Why this one exists:** every recipe on this shelf names components and their licences, and on
an engagement that claim is re-litigated by someone else's legal team from scratch. 🟢 **This pass
produced the artefact that settles it once — a grant payload pinned by sha256 — so the recipe is to
ship that artefact alongside the code rather than to assert a licence in a slide.**
🔴 **It is also the only recipe here that defends against this base's own six defect classes**,
which is the point: the manifest is generated by a checker that cannot make them.

| step | component | grant (bytes / sha256) | role |
|---|---|---|---|
| 1 | resolve `HEAD` symref per dependency | — | 🔴 **`T36`** — 13.2% of real education repos are on neither `main` nor `master`; a manifest pinned to `main` is wrong for one dependency in eight |
| 2 | enumerate the tree, don't guess paths | — | 🔴 **`T34`** — `git clone --depth 1 --filter=blob:none --no-checkout` + `ls-tree -r`; catches lowercase `license`, installer-served grants, and vendored-only repos |
| 3 | fetch **every** licence-ish blob, not the first | — | 🔴 defect 1 — `microsoft/autogen` is `LICENSE` **CC-BY-4.0** *and* `LICENSE-CODE` **MIT 1,141 B `c2cfccb812fe4821`** |
| 4 | classify on the payload, excluding `NOTICE` | — | 🔴 **`T33`** + defect 4 — a `NOTICE` is Apache §4(d) attribution; a bare `spdx_id` is a detector's opinion |
| 5 | anchor on title block **with a condition-text fallback** | — | 🔴 defect 5 — **BSD-3-Clause has no title line**; `Open-TutorAi/open-tutor-ai-CE` (1,531 B) reads `CUSTOM` without it |
| 6 | emit `{slug, branch, path, bytes, sha256, family}` | — | 🟢 the deliverable; re-verifiable by the client with `curl` + `sha256sum` and nothing else |
| 7 | fail the build on `AGPL` / `*-NC` / `Elastic` / `POINTER_DANGLING` / `NOTICE_ONLY` | — | 🟢 the gate — refuses `edx-platform`, `TarrySingh`, `advisingapp`, `codeforlife-*`, both `fedena` mirrors |

🟢 **Worked output exists**: this pass's own census is the manifest for 137 addresses, **81 of them
permissive**. 🔵 **Effort: 2–3 days** for the checker; it replaces a licence review per engagement.
🔴 **Known limit, stated rather than discovered later: `curl -sI` is non-discriminating against
`github.com` in this session (`Gap 505-G`) and `ls-remote` is not concurrency-safe (`T35`) — the
checker must run its ref resolution serially and verify with a known-good *and* a known-bad control
before it reports a count.**

### 🟢 `p509-R2` — The permissive SIS, scoped from what `gegok12` does NOT ship

🔵 **Why this one exists:** `Gap 508-C` asked whether the one MIT education SIS is a real system or
an open-core shell. 🟢 **It is real — 107 models, 247 controllers, 108 migrations — and the four
modules it lacks are exactly the four a commercial suite charges for.** That turns a licence
question into a **build estimate**, which is the form an engagement can price.

| step | component | grant | role |
|---|---|---|---|
| 1 | [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT**, 1,150 B `b8694396d7dc6439`, `main` | the base: admissions, attendance, academic year, assignments + approvals, discipline, library circulation, messaging, documents, **4-model Payroll** |
| 2 | **build: fees / invoicing** | — | 🔴 **no model matches `fee`/`invoice`** — the single largest gap, and the one every school asks for first |
| 3 | **build: examinations / results** | — | 🔴 **no model matches `exam`/`result`** — pairs with step 5 |
| 4 | **build: transport / hostel** | — | 🔴 absent; scope out unless the client is residential |
| 5 | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT**, 1,105 B `5baaaf977a28e9fd` | mastery estimation (BKT) over the assessment data step 3 creates — 🔵 **the reason to build exams properly rather than as a CRUD screen** |
| 6 | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0**, 11,357 B `58d1e17ffe5109a7` | the teacher-facing surface on top of the SIS record |
| 7 | [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) | 🟢 **MIT**, 1,106 B `aad28612a5b76f86` | the auto-grader + MCP-tutor pattern to copy for step 3's grading path |
| 8 | human-review gate on every graded or placement decision | — | 🔴 **required, not optional**: OK **SB 1734** bars AI as the *primary basis* for grading, discipline or placement; 🇻🇳 Decision **33/2026** makes automated assessment high-risk |

🟡 **Measure definition (`T31`), because the estimate rests on it:** steps 2–4 are *"zero filenames
under `app/Models/` matching `fee`/`invoice`/`exam`/`result`/`transport`/`hostel`"*. A module under a different
name, or built without an Eloquent model, would not be counted — 🟢 **confirm against the vendor's
module list before pricing**, which is the half of `Gap 508-C` this session could not reach.
🔵 **Effort: 10–14 weeks** for steps 2–3 plus 5–8; steps 1 and 4 are inherit-or-skip.
🟢 **Regional fit: LATAM and APAC**, where this file's market section records high AI use against low
formal governance and where a permissive SIS base avoids both the AGPL of `edx-platform` and the
Elastic-2.0 of `advisingapp`.


> 🟢 **`p508` (`2026-10-28`) — TWO NEW RECIPES, AND BOTH ARE BUILT AROUND A LICENCE-ARCHITECTURE DECISION RATHER THAN A FEATURE LIST.**
> 🔵 Every component below was read on the API channel this pass (`license.spdx_id`, `archived`, stars)
> and every **payload-level** licence claim was read on `raw.githubusercontent.com` with bytes and
> sha256. 🔴 **No AGPL or `NOASSERTION`-without-payload component appears in a shipped step** — where
> an AGPL asset is unavoidable (`Anki`), the recipe keeps it **on the learner's own machine** and says
> so. Reads: [`licence-bytes.2026-10-28-p508.tsv`](../evidence/licence-bytes.2026-10-28-p508.tsv),
> [`api-shelf-read.2026-10-28-p508.tsv`](../evidence/api-shelf-read.2026-10-28-p508.tsv).

### 🟢 `p508-R1` — The retention loop, with the AGPL kept on the learner's device

🔵 **Why this one exists:** every tutoring recipe on this shelf ends at *explanation*. Retention is
where learning is actually measured, and the reference scheduler in this field (**Anki**, 32,300★) is
**AGPL-3.0** — which is why nobody builds it into a client product. 🟢 **The MIT MCP server in step 3
dissolves the problem: the agent writes cards into the learner's own Anki install, so the AGPL code
never enters the deliverable.**

| step | component | licence | ★ | role |
|---|---|---|---|---|
| 1. source → study package | [`SYuan03/Skill-Anything`](https://github.com/SYuan03/Skill-Anything) | 🟢 MIT | 344 | PDF / video / web / audio → quizzes, flashcards and a 12-section study guide in one command. |
| 2. scheduling policy | [`HumphreySun98/Smart-Study-Agent`](https://github.com/HumphreySun98/Smart-Study-Agent) | 🟢 MIT | 57 | **FSRS** for *when*, RL for *which action* — the part a chatbot has no opinion about. |
| 3. card delivery | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT | **537** | MCP server over the learner's **local** Anki. 🔴 Anki itself is AGPL-3.0 — it stays on the device, the MIT server is what you ship. |
| 4. institutional landing | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 MIT | 995 *(🟢 `p512`, API)* | **Emits SCORM** — the loop reports into Moodle / Canvas / ILIAS without an integration project. |
| 5. evidence of mastery | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | 274 | **BKT** mastery estimates, UC Berkeley — gives step 2 a target rather than a guess. |

🟢 **Shippable licence surface: MIT only.** 🔴 **What it is not:** a hosted SRS product — if the client
wants cards on a server, the Anki dependency has to be replaced, and FSRS (step 2) is the algorithm you
reimplement, not the app.

### 🟢 `p508-R2` — Diagnose-first STEM tutor over MCP, with an eval gate before release

🔵 **Why this one exists:** `p507-R1` built the teacher side because TALIS says preparation is where the
usage is. This is the student side done the way the evidence shelf demands — **a diagnosis before a
lesson, and a pedagogical-quality gate before anything reaches a classroom.**

| step | component | licence | ★ | role |
|---|---|---|---|---|
| 1. ITS runtime | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | 57 | MCP server that turns any LLM into an intelligent tutoring system — model-agnostic, so the client's procurement decides the model. |
| 2. pedagogy | [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 MIT | 252 | **Diagnosis first**, no mode menu. This is the behaviour teachers ask for and chat UIs never do. |
| 3. mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | 274 | BKT over a skill graph — the state that makes step 2's diagnosis persist between sessions. |
| 4. domain depth (CS/ML) | [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) · [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) | 🟢 MIT · 🟢 MIT | 299 · 2,595 | DSA mentoring and 65 ML problems **with an auto-grader** — a verifiable correctness signal, not an LLM opinion. |
| 5. release gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) run under [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT · 🟢 MIT | 13 · **14,338** | 1,143 teacher-exam questions as a **CI gate**: no prompt change ships without a pedagogy score. |
| 6. institutional layer *(only if a closed derivative is required)* | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0 by payload** (10,982 B, `sha256 6dbc5b605ed0…`) | 448 | The only permissive full LMS. 🔴 **Its API `license.spdx_id` reads `NOASSERTION`** — an automated licence gate in the client's pipeline will reject it unless you give it the payload reading. |

🟢 **Shippable licence surface: MIT throughout steps 1–5**, Apache-2.0 (with attribution) at step 6.
🔴 **What it is not:** a K-12 product — steps 4 and 5 are tertiary/professional in scope, and the
benchmark at step 5 is a **13★ corpus**: treat it as a gate you maintain, not a dependency you trust.

> 🟢 **`p507` (`2026-10-28`) — TWO NEW RECIPES, BOTH BUILT ONLY FROM MIT PARTS VERIFIED THIS PASS.**
> 🔵 Every repo named below was read on the API channel this pass: `license.spdx_id`, `archived`
> and star count are measured, not carried. 🔴 **No AGPL or `NOASSERTION` repo appears in any wiring
> step** — the two fastest-growing new education repos of this pass
> ([`Echo-Loop`](https://github.com/echo-loop/Echo-Loop), [`penecho`](https://github.com/penecho/penecho))
> are deliberately absent for that reason, and are cited only as design references.
> Reads: [`new-addresses.2026-10-28-p507.tsv`](../evidence/new-addresses.2026-10-28-p507.tsv),
> [`api-shelf-read.2026-10-28-p507.tsv`](../evidence/api-shelf-read.2026-10-28-p507.tsv).

### 🟢 `p507-R1` — Teacher-side preparation, because that is what the probability sample says sells

🔵 **Why this one exists:** TALIS 2024 reports that among AI-using teachers, **68%** use it to
learn or summarise a topic and **64%** to generate lesson plans — **both preparation**. Student-
facing tutoring is where the stars are; **preparation is where the usage is.** Build the one people
already do.

| step | component | licence | ★ | role |
|---|---|---|---|---|
| 1. source → knowledge | [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | 🟢 MIT | 36,421 *(🟢 `p512`, API)* | Turn the syllabus, textbook or curriculum PDF into agent-readable skill knowledge. |
| 2. pedagogy layer | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 permissive | **600** *(🟢 `p512`, API)* | Lesson-planning skills **plus eval rubrics** — the rubrics are the part that makes step 5 possible. |
| 3. generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 MIT | **387** | Emit lesson plans, question banks and activities as structured objects, not prose. |
| 4. delivery into the institution | [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 MIT | 995 *(🟢 `p512`, API)* | **Emits SCORM** — lands inside Moodle/Canvas/ILIAS without an integration project. |
| 5. quality gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) + [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🟢 permissive | 13 / 46 | Score the generated material for **pedagogical** quality before a teacher ever sees it. |

🟢 **Wiring:** `book-to-skill` writes a knowledge pack → `k12-teacher-skills` supplies the planning
skill and its rubric → `educhain` generates against that rubric → **`pedagogy-benchmark` scores the
output and anything below threshold regenerates rather than shipping** → `Papermorph` packages the
survivors as SCORM → import into the LMS.
🔴 **The non-obvious step is 5.** Every education generation demo skips it, and it is the only step
that distinguishes this from a prompt. 🟡 **Step 2's rubrics and step 5's benchmark must agree** —
wire the rubric into the benchmark's scoring config, or you are measuring a different thing than
you asked for.
🔵 **Regional fit:** 🇫🇷 France (**14%** use, **9%** training) is the sharpest case — the
deliverable is enablement, and this recipe produces material a teacher keeps.

### 🟢 `p507-R2` — Assessment with an auto-grader and an MCP tutor, end to end

🔵 **Why this one exists:** [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) (🟢 **MIT**,
**2,595★**, `archived: false`) is the rare repo that ships **an auto-grader and an MCP AI tutor
together**. The MCP surface is the point — it composes with any agent on this shelf instead of
being a closed app.

| step | component | licence | ★ | role |
|---|---|---|---|---|
| 1. problem bank + grader | [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) | 🟢 **MIT** | **2,596** *(🟢 `p512`, API)* | Problems with an auto-grader; **its MCP server is the tutor interface**. |
| 2. tutoring policy | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 permissive | **274** | **Bayesian Knowledge Tracing** — decides *what next* from the grader's pass/fail stream, instead of letting the LLM guess mastery. |
| 3. integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 permissive | **355** | Source-code plagiarism detection on submissions — the control an institution asks for before it will grade with AI. |
| 4. LMS surface | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 permissive | **309** | Canvas LMS over MCP — the same protocol as step 1, so roster, assignment and grade flow need no adapter. |
| 5. evidence | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 permissive | **144** | xAPI learning-record store: every attempt, hint and grade as a statement. |

🟢 **Wiring:** Canvas publishes the assignment via `canvas-mcp` → the learner works a `TorchLeet`
problem → the auto-grader returns pass/fail → **`OATutor`'s BKT updates mastery and selects the next
problem** → the `TorchLeet` MCP tutor explains **only** the failed step → `dolos` screens
submissions → every event lands in `lrsql` as xAPI.
🟢 **Steps 1 and 4 both speak MCP, so the tutor and the LMS compose without glue** — that is what
makes this a build rather than an integration.
🔴 **And step 5 is the compliance step, not a nicety.** 🇻🇳 **Decision 33/2026/QD-TTg** names AI
that *"automatically conducts examinations, assesses learning outcomes or ranks learners"* a
**high-risk** system — this recipe is squarely inside it. 🟡 **An xAPI record of every automated
decision, plus a human override on the grade, is the conformity evidence**, and a **new** Vietnamese
deployment must have it by **1 Mar 2027**, not the incumbents' 1 Sep 2027.

### 🟢 `p507-R3` — Embodied STEM, a category this base could not build before

🔵 [`PetoiCamp/OpenCat-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)
(🟢 **MIT**, **5,518★ / 650 forks**) is the first permissive repo on these shelves that produces a
**physical** learner artefact.

🟢 **Wiring:** `OpenCat` (or the ESP32 board,
[`OpenCatEsp32`](https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot), **521★**) supplies the
robot and its block-coding surface → `k12-teacher-skills` generates the lesson sequence and its
rubric → `educhain` emits the worksheets and assessment items → **the robot's own telemetry becomes
the evidence stream into `lrsql`**, so "did the learner's program make the robot walk" is a graded
xAPI statement rather than a teacher's impression → `Papermorph` packages the unit as SCORM for the
LMS.
🟡 **Use the ESP32 board for classroom fleets** — lower unit cost and the same framework.
🔵 **Regional fit:** this is the recipe for a 🇦🇪/🇸🇬-style high-adoption, well-funded STEM
programme, where the differentiator is no longer *whether* teachers use AI (**~75%** already do) but
what the programme produces.


**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it with **`P491-1`**, which supersedes `P490-6`. Pre-p490 sections remain in
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
| Tool surface | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | Canvas tools + 8 agent skills over MCP. 🔴 **Pin `v1.16.0` or later** (`p492`) — see the amended threat model below. Tool count is self-inconsistent upstream (102 vs 128): **do not quote one.** |
| Agent loop | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | code-writing agent runtime |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | quizzes, lesson plans, flashcards |

**Wiring:** run `canvas-mcp` against the institution's Canvas API token → expose as MCP tools to a
`smolagents` agent → `educhain` generates assessment items that the agent writes back through
`canvas-mcp`'s content tools.

**Do this or it is negligent:** start from `canvas-mcp`'s **read-only** tool subset
(`get_*`/`list_*`), enable write tools individually through its operator allowlist, and put a human
gate on anything that writes a grade. Its own source makes the point to honour: *a confirmation
token does not prove a human approved anything.*

🔴 **Amended `p492` — the threat model above was right and is no longer sufficient.** This pattern
previously named **one** advisory as the threat model. `v1.16.0` publishes **four**, and two of them
are not covered by tool scoping at all:

| advisory | subject | what it defeats |
|---|---|---|
| `GHSA-7mj9-4mcg-hvhv` | **Canvas token handling** | 🔴 **Read-only tool scoping does not protect the token.** This pattern hands the server an *institutional* Canvas API token — scoping tools limits what the agent may call, not what a token-handling defect exposes. |
| `GHSA-7pp5-29mw-9jq3` | **local code sandbox** | 🔴 Code execution reachable from an agent loop driven by **student-authored text**. |
| `GHSA-hmr8-mvr2-mvw5` | **file content fencing** | The advisory this pattern already carried. Upstream's words are *file content fencing*, not "prompt-injection path". |
| `GHSA-qf6c-jv93-38gv` | Windows download permissions | Low relevance on Linux hosting; still live. |

**Three additions to the build, not optional:**

1. **Treat the Canvas API token as the primary asset, not the tool scope.** Issue a **dedicated
   service token** scoped to the pilot faculty, hold it in a secret manager the agent process
   cannot read, inject at request time, and **rotate on a schedule set before go-live**. Never the
   institution's admin token.
2. **Isolate the runtime.** With a published sandbox advisory and `smolagents` *writing and running
   code* in this very pattern, the agent process runs in its own container with **no ambient cloud
   credentials** and egress restricted to the Canvas host and the model endpoint.
3. **Pin and watch.** Pin `canvas-mcp` to `v1.16.0`+ by tag, subscribe to its advisories, and
   re-read them at every engagement checkpoint. 🟢 It **has** a `SECURITY.md` and discloses — which
   is why four advisories is a sign of a project worth depending on, not one to avoid. **An
   education MCP server with zero advisories is unexamined, not safe.**

🔵 **Also `p492`:** this pattern's base **drifted** — HEAD moved from this KB's pinned
`32e5d1ca0175` to `830bc2ef8389`, with the licence **byte-identical at both SHAs** (MIT, 1 071 B),
so the change is **code-only**. Pin by release tag rather than tracking `main`.

🔴 **`p494` — and it drifted again, inside a single pass's own window.** `830bc2ef8389` →
**`47394125364b`**, observed ~30 minutes apart in the same pass and stable across three reads.
Licence **byte-identical at all three SHAs** (MIT, 1 071 B, `sha1 491fb891a4cf`), so every move so
far is code-only. 🔴 **Two moves in ~24 hours makes this the most volatile dependency in this KB,
and it is this pattern's base.** The instruction above is therefore not a preference but a
requirement: **pin `v1.16.0` or later by tag, never a branch HEAD** — a HEAD pin on this repo is
stale before the engagement's first sprint review, and `git ls-remote` will report drift that is
merely upstream's normal cadence. 🟡 **Advisory caveat:** the **four** advisories named below were
read by `p492` at `v1.16.0` and were **not** re-read at `47394125364b`. On a repo moving this fast
and carrying a **token-handling** advisory, **re-read the advisory list at the tag you actually pin,
before you deploy** — do not inherit this KB's count.

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

## P490-6 — Open education-AI evaluation harness (build, not compose) 🟡 **— superseded by `P491-1`**

🔵 **Superseded.** Its premise — that *no* education-AI evaluation instrument exists — was refuted
in `p491`: two real benchmarks exist, and they are **unlicensed**. Use **`P491-1`** below, which
keeps this pattern's scoring design but rebases the runtime on a permissive harness instead of
building one. Kept here because the component wiring below is still sound and the two patterns
differ only in their base.

**Why:** this is the sector's largest structural gap. Nobody can currently demonstrate that an AI
tutor improves outcomes. Buyers in all four regions are starting to ask, and EU high-risk
conformity will require evidence by **2 Dec 2027**.

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

## P491-1 — Tutoring-quality eval harness on a permissive base 🟢 *(supersedes `P490-6`)*

**Why:** `p491` established that the instruments for measuring tutoring quality **exist and carry
no license** — [`mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (46★ *(🟢 `p512`, API)*, EMNLP 2025 Oral)
and [`TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) (0★, KAIST) both ship **no grant
file**, and MathTutorBench's README contradicts itself (`CC BY 4.0` badge vs `CC BY-SA 4.0` text,
neither a software grant). So the research is public and the **code and data are not takeable**.
That is a licensing blocker, not a scarcity one, and it has a clean route around it.

| Component | Repo | License | Role |
|---|---|---|---|
| Harness runtime | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** (1,066 B @ `d6de81643928`) | task registry, model adapters, runners, reporting — 14,341★ *(🟢 `p512`, API)*, the de-facto standard |
| Ground-truth mastery | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT as the reference learner model |
| Item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | held-out item banks at volume |
| Curriculum authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | answer keys with provenance |
| Learner simulation | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | drive simulated learner trajectories |
| Subject under test | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | first candidate tutor |

**Wiring:** implement each pedagogical dimension as a **native `lm-evaluation-harness` task** —
that is the one decision that makes this reusable, because it inherits the harness's model
adapters, caching, reproducible task versioning and result format for free, and anything scored
this way is comparable against general-model baselines. Then: KSoR holds curriculum and answer
keys → `educhain` generates held-out item banks → `smolagents` drives simulated learner
trajectories against the candidate tutor → OATutor's BKT scores **per-skill mastery gain** against
the key → the harness emits the report. Score learning gain, never token overlap.

**The license line that makes this work — read it before writing any code:**

1. 🟢 **Every component above is MIT or Apache-2.0.** The output is a clean closed or open
   deliverable, your choice.
2. 🔴 **Do not vendor `mathtutorbench` or `TutorCaseBench` code or data.** No grant means no
   rights — not permissive-by-default. Cloning for private reading is one thing; shipping their
   code or redistributing their datasets in a client deliverable is another.
3. 🟢 **Reimplement the *task designs* from the papers** (arXiv 2502.18940 for MathTutorBench;
   TutorCaseBench's 5 challenge types). Benchmark methodology published in a paper is readable and
   reimplementable; that is what papers are for. Cite both.
4. 🟢 **Ask the authors to add a license.** Both are academic groups (ETH LRE, KAIST kixlab) and an
   MIT or Apache-2.0 grant is usually a five-minute decision nobody got around to. An upstream
   license would convert this whole pattern from a build into a compose — the highest-leverage
   email in this file.

**Why it is worth building anyway:** EU high-risk conformity needs **evidence of educational
efficacy** by **2 Dec 2027** (`P490-2`), and no buyer in any region can currently get it. A
published, permissively-licensed tutoring-eval harness is a credibility asset that also doubles as
the measurement layer under every other pattern here.

**Scope:** 8–12 weeks for v1 on one subject domain — shorter than `P490-6`'s 10–14, because the
runtime, model adapters and reporting are no longer yours to write.

---

## Patterns deliberately **not** offered

- **Nothing on Moodle or Open edX at the agent layer.** Neither has an MCP/tool surface at a
  usable star floor; the connector is unbudgeted build work. Use P490-1 (Canvas) where possible
  and price the connector explicitly otherwise.
- **No closed SaaS on an incumbent LMS fork.** Moodle is GPL-3.0; Open edX, Canvas, Frappe LMS,
  Tutor **and LearnHouse** (`p491`, 2,400★) are **AGPL-3.0** — hosting a modified copy owes source
  to users. Only OpenOlat, Kolibri, Oppia and mentingo support that shape.
- **Nothing on `frappe/education`** (`p491`, 682★) despite it being a genuine school-management
  base: its grant is a **19-byte stub** naming GPL v3 with no license text, so it is copyleft *and*
  its paperwork will not survive a client's legal review. Named so the omission is visible.
- **Nothing built on an unlicensed benchmark.** `mathtutorbench` and `TutorCaseBench` are the two
  best education-AI instruments in existence and **neither can be composed** — see `P491-1`.
- **No closed SIS or assessment product.** Every SIS found (`rosariosis` GPL-2.0, `GibbonEdu`
  GPL-3.0, `openeducat_erp` LGPL-3.0) and the only real assessment engine (`tao-core` GPL-2.0)
  are copyleft. There is no permissive base — it is a ground-up build.
- **Nothing using `ChatTutor` (AGPL-3.0) or `tutor-gpt` (GPL-3.0)** in a hosted commercial
  pattern, despite both being capable. Named here so the omission is visible rather than silent.


## 🆕 `P492-1` — Grading assistant whose arithmetic the model never touches 🟢

**Why:** every high-risk education regime now converging on the same functional trigger —
**automated assessment or ranking of learners** (EU Annex III; Vietnam Decision `33/2026/QD-TTg`,
3 education systems of 46) — demands demonstrable human oversight from the **provider**. And
[`intel/market.md`](../intel/market.md) establishes that **for a Globant-built education AI system,
Globant is the provider.** The cheapest way to fail a conformity assessment is to let an LLM
compute a grade total.

| Component | Repo | License | Role |
|---|---|---|---|
| Reference design | [vulinh1704/ai-tutor-agent](https://github.com/vulinh1704/ai-tutor-agent) | MIT | 🔵 **read, do not depend** (0★, 13 commits) — the rubric/leak-guard/thread architecture below |
| Agent runtime | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **MIT** (1 072 B, `sha1 73a6ebe3bd93` @ `eb8ec111b3e9`) | explicit per-session thread with checkpointed state |
| Rubric item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | generates the rubric criteria and assessment items |
| LMS write-back | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | **`v1.16.0`+**, write tools behind a human gate |
| Quality harness | [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 🔴 **no software grant** | 🔵 measure against it; **do not vendor it** — see [`agents/top.md`](../agents/top.md) |

**Wiring — the whole point is the split:**

1. `educhain` emits the **rubric** (criteria + weights + max points) as data, reviewed by a human
   **once per assignment**, then frozen and version-pinned.
2. The model is asked for **per-criterion structured output only** — a score and a feedback string
   per criterion, validated against the frozen rubric schema with Pydantic. **A response that does
   not validate is rejected and retried, never coerced.**
3. 🟢 **The total is computed in Python from the validated per-criterion scores.** The model is
   never asked for, and never shown, a total. This is the single load-bearing decision.
4. **Socratic mode gets the answer-leak guard:** a draft hint that reveals the answer is
   regenerated under a stricter instruction; if it still leaks, a safe canned hint replaces it.
   Hints escalate one level at a time.
5. Session state is an **explicit LangGraph thread** (SQLite for a pilot), so every grade carries a
   replayable trace — which is what an oversight duty actually asks for.
6. `canvas-mcp` writes the grade back **only after a human gate**, per `P490-1`'s amended rules
   (dedicated scoped token, isolated runtime, pinned release).

**What makes this conformant rather than merely careful:** the arithmetic is deterministic and
auditable, the rubric is human-approved before any student is graded, every score decomposes to a
criterion with a rationale, and the trace is replayable. 🟢 **An EU-conformant build of this
transfers to Vietnam with little rework** — the functional trigger is the same, which is why this
KB's standing advice is to build conformity **once, in EMEA shape, and reuse it**.

🔴 **Do not propose the reference repo as a dependency.** One author, 13 commits, zero stars, no
security process. Its value is that it is a **1 071-byte MIT grant over an architecture worth
copying** — the first open implementation of advice this KB has given for several passes without
being able to point at code.

🔵 **Honest gap:** `mathtutorbench` measures tutoring quality and **ships no software licence**
(its own README names two different Creative Commons variants, neither a software grant). Use it as
an **external yardstick you run against**, never as vendored code. There is still **no usable
open-source education-AI evaluation harness** — see `T11`.

**Scope:** 5–7 weeks to a governed pilot on one course, including the rubric-freeze workflow and
the oversight trace. Add 2–3 weeks if the conformity documentation is a deliverable.

---

## 🆕 `P493-1` — The first end-to-end **all-permissive** education stack 🟢

**Why:** every stack this KB has been able to propose crossed a copyleft boundary somewhere —
usually at the platform layer, which is why `T2` called that *the binding constraint*. `p493`
restored eight addresses that earlier passes had promoted and later rewrites deleted (see
[`agents/trending.md`](../agents/trending.md) `p493`), and with them **a complete stack exists in
which every component is MIT, Apache-2.0 or BSD-3-Clause.** For a client who cannot accept
copyleft — a commercial derivative, a hosted multi-tenant product, an OEM arrangement — this is the
difference between "we must talk about AGPL" and "we do not".

| Component | Repo | License | ★ | Role |
|---|---|---|---|---|
| Courseware / classroom | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,710 *(🟢 `p512`, API)* | Topic or document → multi-agent interactive lesson: slides, quizzes, project-based work |
| Teacher workflow | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** | 600 *(🟢 `p512`, API)* | Lesson planning + differentiation skills **with their eval rubrics** |
| Teacher workflow (twin) | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | **Apache-2.0** | 40 | Consortium-side payloads + `evals/` rubrics for pedagogy, rigour, format, scaffolding |
| Tutoring platform | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | Collaborative tutoring platform where ChatTutor (AGPL-3.0) was the only option |
| Quality gate | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 13 | 1,143 teacher-exam items (920 CDPK / 223 SEND), 100+ models |
| Eval runtime | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** | 14,341 *(🟢 `p512`, API)* | the harness `pedagogy-benchmark` runs on |
| Academic integrity | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | Source-code plagiarism detection; 3,865 commits |
| Delivery — offline | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,162 *(🟢 `p512`, API)* | runs without connectivity |
| Delivery — no app | [Orenda-Project/rumi-platform](https://github.com/Orenda-Project/rumi-platform) | **Apache-2.0** | 18 | WhatsApp, 15 languages |
| Institutional layer *(only if needed)* | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 448 | enrolment, roles, gradebook — **the only permissive full LMS** |

**Wiring:** `OpenMAIC` generates the courseware and runs the classroom experience → the two
teacher-skill packs drive lesson planning and differentiation at the teacher's desk (a skill pack
has **no runtime**, so nothing is hosted and no data-residency posture attaches to it) →
`open-tutor-ai-CE` carries the 1:1 tutoring surface → `dolos` sits on submitted code →
`pedagogy-benchmark` on `lm-evaluation-harness` runs as a **release gate in CI**, not as a one-off
report → `Kolibri` or `rumi-platform` carries delivery where connectivity is not assumable →
`OpenOLAT` underneath **only** where the engagement genuinely needs enrolment, roles and a
gradebook.

**Do this or it is negligent:**

1. 🔴 **`OpenMAIC` is not an LMS and must not be sold as one.** Nothing on its page claims
   enrolment, a gradebook, SIS integration or institutional roles. If the client needs those, the
   permissive answer is `OpenOLAT` beneath it — and if they need a **SIS** or a **QTI exam
   engine**, 🔴 **there is no permissive option at all** and the copyleft conversation is
   unavoidable. Say that in week one, not at UAT.
2. 🔴 **Pin every component by SHA or release tag and re-read the licence bytes at that pin.** This
   pattern's own evidence is why: `p493` found eight promoted rows deleted from this KB's shelves,
   and `p492` found `canvas-mcp` drifted with its licence byte-identical at both SHAs. Pins read at
   `2026-10-28`: `OpenMAIC` `70859b42e714` (MIT, 1 065 B), `k12-teacher-skills` `31fd6dbb0c07`
   (Apache-2.0, 11 357 B), `open-tutor-ai-CE` `196c547291da` (BSD-3-Clause, 1 531 B), `dolos`
   `74b101785bad` (MIT, 1 084 B), `pedagogy-benchmark` `21a43a395ab4` (MIT, 1 064 B),
   `agent-skills` `8b0599c24469` (Apache-2.0, 10 173 B), `rumi-platform` `f2d62af1eb82`
   (Apache-2.0, 11 287 B).
3. 🔴 **Honour BSD-3-Clause's third condition.** `open-tutor-ai-CE` forbids using the copyright
   holder's or contributors' names to endorse or promote a derivative without written permission.
   **Do not put "built on Open-TutorAI" in client-facing marketing** without that permission —
   attribution in the NOTICE file, yes; endorsement in a pitch deck, no. 🔵 This is the one
   obligation in the stack that bites *marketing* rather than *engineering*, which is exactly why
   it gets missed.
4. 🔴 **Three components are single-digit-to-low-double-digit★ and must be treated as corpora, not
   dependencies.** `pedagogy-benchmark` (13★, 5 commits), `rumi-platform` (18★),
   `Shiksha-Copilot` (9★) have no community and no security process. **Vendor the code into the
   engagement repository**, do not take a live dependency, and budget to maintain it yourself.
   `OpenMAIC` (781 commits), `dolos` (3,865 commits) and `Kolibri` are the three that can carry a
   real dependency.
5. 🟢 **Run `pedagogy-benchmark` before the pilot and keep the baseline.** It is the only licensed
   education-specific instrument available (see [`intel/trends.md`](../intel/trends.md) `T11`), and
   the **SEND** subset (223 items) is the only readable signal in this KB on special-educational-needs
   competence — the population where an unevaluated tutor does the most harm and where procurement
   asks the hardest questions.
6. 🟢 **Keep the human-oversight gate even though nothing here is formally high-risk yet.**
   `Shiksha-Copilot`'s shipped design — **every generated artefact routed to a teacher for review
   before classroom use** — is the pattern to copy, and `P492-1`'s rule stands: **the model never
   does the arithmetic on a grade.** This is what EU Annex III will require of a *provider* from
   **2 Dec 2027**, what Oklahoma S.B. 1734 appears to require of districts before the **2027-28**
   school year (see [`intel/market.md`](../intel/market.md) `p493`), and what Vietnam's decision
   keys its high-risk tier to.

**Licence note:** 🟢 **No copyleft anywhere in the stack**, including the optional LMS layer. The
one component to keep out is this KB's most-cited education skill pack,
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) —
**CC-BY-SA-4.0**, re-confirmed at 1 230 B this pass. 🔴 **ShareAlike on a content licence reaches
the derived curriculum, not just the code**, which would relicense the client's teaching materials.
Reference it; do not vendor it.

**Regional fit:** 🟢 **APAC strongest** — `OpenMAIC` (China), `Shiksha-Copilot` (India),
`rumi-platform` (Pakistan) are all regional in origin. 🟢 **LATAM** — pair with `Kolibri` and
`rumi-platform` against the **33-point Argentine socio-economic access gap** `p493` records, and note
there is still **no LATAM-origin component** at usable scale. 🟢 **EMEA** — `dolos` (Belgium) and
`open-tutor-ai-CE` (Morocco) are in-region, and the all-permissive property is what makes a
provider-grade conformity build sellable as product rather than as services. 🟡 **North America** —
the skill packs are NA-origin, but `P490-1` remains the faster route into US higher ed because
Canvas is the incumbent and has the only maintained agent surface.

**Scope:** 10–12 weeks to a governed pilot with an evaluation baseline. 🔵 Longer than `P490-1`
(4–6 weeks) because `OpenMAIC` is a courseware engine rather than an integration into an incumbent
LMS — **you are standing up a stack, not instrumenting one that exists.** Add 3–4 weeks if an
`OpenOLAT` institutional layer is in scope.

## 🆕 `P494-1` — APAC agentic education build with a Vietnam/Singapore jurisdiction fork 🟢

**Why:** `P490-4` offers a jurisdiction-routing provenance layer for APAC, and its premise is that
China's binding rules, India's labelling duty, Japan's promotion posture and Singapore's voluntary
assurance cannot be satisfied by one configuration. 🔴 **That premise had one of its four
jurisdictions deleted from this KB** — the Singapore posture was held at `p315` and removed by
`p315`'s own rewrite (see [`../intel/market.md`](../intel/market.md) `p494`). Restoring it, plus
`p494`'s reading of Vietnam's full education scope, changes what the APAC build actually has to
produce. 🟢 **Two of Vietnam's three high-risk education triggers do not transfer from an
EU-conformant design, and Singapore's agentic framework asks four questions no education regime
asks.** This pattern is `P493-1`'s all-permissive stack with those obligations built in.

**Base stack:** unchanged from [`P493-1`](#-p493-1--the-first-end-to-end-all-permissive-education-stack-) —
[`OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (MIT, `70859b42e714`) for courseware and the
classroom, [`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3-Clause,
`196c547291da`) for 1:1 tutoring, [`dolos`](https://github.com/dodona-edu/dolos) (MIT,
`74b101785bad`) on submitted code,
[`pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT, `21a43a395ab4`)
on [`lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) (MIT) as the CI
release gate, [`Kolibri`](https://github.com/learningequality/kolibri) (MIT) and
[`rumi-platform`](https://github.com/Orenda-Project/rumi-platform) (Apache-2.0, `f2d62af1eb82`) for
delivery. 🟢 **No copyleft anywhere**, which is what makes the conformity artefacts below sellable
as product rather than as services.

### 🔴 The three Vietnam triggers, and what each one costs to build

Decision `33/2026/QD-TTg` (issued **30 Jun 2026**, in force **15 Aug 2026**) names **three**
education system types. This KB recorded one until `p494`.

| trigger | transfers from an EU build? | artefact you must produce |
|---|---|---|
| automatic **assessment, grading or ranking** of students | 🟢 **yes** — same functional trigger as EU Annex III | `P490-2`'s conformity pack, reused as-is |
| self-learning content from **uncontrolled data sources** | 🔴 **no** | a **corpus provenance manifest** — see below |
| **biometric** monitoring of learner behaviour | 🔴 **no, opposite direction** | a **build-time fork** — see below |

**1. 🔴 The corpus trigger fires on retrieval design alone.** A RAG tutor over an unvetted corpus is
high-risk in Vietnam **with no grading feature anywhere in the product**. This is a
corpus-governance obligation and an EU-conformant build produces nothing that answers it. Concretely,
in `open-tutor-ai-CE`'s retrieval path and `OpenMAIC`'s document-ingest path:

- **Pin the corpus and hash it.** One manifest row per document: source URL or acquisition route,
  licence, retrieval date, SHA-256, and the human who approved it. Vendor the manifest into the
  engagement repository next to the index.
- **Gate retrieval to the manifest.** Reject at query time any chunk whose document id is not in the
  manifest, and fail closed. An index rebuilt from a crawl that was never approved is the exact
  failure the trigger describes.
- 🔵 **This is cheap if done at week one and near-impossible to retrofit**, because the provenance of
  documents already embedded is not recoverable from the vector store.

**2. 🔴 Biometrics is a build-time fork, never a runtime policy flag.** The EU **prohibits** emotion
recognition in education outright (live since **2 Feb 2025**, narrow medical/safety exception —
`T6`); Vietnam **permits biometric learner monitoring as a high-risk category**, i.e. allowed subject
to conformity duties. 🟢 **The feature must be *absent* in one jurisdiction and *documented and
governed* in the other.** A feature flag does not satisfy the EU prohibition — the capability's
presence in a shipped artefact is the problem, not its default state. **Two build targets, one
codebase, and the EU target must not compile the module.** 🔵 This is the sharpest regulatory
asymmetry in this KB and the one most likely to be mistaken for a configuration question.

**3. 🟡 Which deadline applies depends on when the system went live, and the new-build answer is
single-sourced.** Education, healthcare and finance systems **in operation before 15 Aug 2026** have
until **1 Sep 2027**; other listed sectors have until **1 Mar 2027**. `p492` reports that a system
first operated **within six months after** 15 Aug 2026 falls back to **1 Mar 2027** — 🔴 **that row
rests on a single vendor compliance tracker and is expressly unconfirmed against the official
text.** **Plan to 1 Mar 2027**, because the error direction is safe that way, but 🔴 **do not put
either date in a contract before someone reads Decision 33's official text** (`english.luatvietnam.vn`
is subscriber-gated and does not open from this session). **Name that read as a deliverable in week
one.**

### 🟢 Singapore: four questions, four artefacts, and a voluntary gate worth designing to

IMDA's **Model AI Governance Framework for Agentic AI** (launched **22 Jan 2026**, voluntary, with
**AI Verify** as the assurance side — `T15`) asks the four questions a multi-agent education system
actually has to answer. 🔵 **Because it is voluntary, it is demonstrable** — design to the rubric and
point at it, rather than arguing an obligation down. And per this KB's restored Singapore note,
vendors selling into government and banks **are expected to point to these frameworks**, which makes
it a **procurement gate**.

| framework axis | artefact in this stack |
|---|---|
| **how much autonomy the agent is granted** | A written capability inventory per agent role in `OpenMAIC`'s multi-agent classroom: what each may read, generate, and persist. 🔴 **No agent gets write access to a gradebook** — `P492-1`'s rule, and the one that survives every regime here |
| **how actions are bounded and logged** | Structured per-action log (agent id, tool, inputs, outputs, timestamp) retained for the engagement's audit window. 🔵 The same log discharges Vietnam's human-review evidence, so build it once |
| **how humans stay meaningfully in the loop** | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)'s shipped design (MIT, 9★): **every generated artefact routed to a teacher for review before classroom use.** Copy the shape; vendor the code, do not depend on it |
| **accountability when several agents interact** | A named owner per agent role and a single escalation path. 🔴 This is the axis most multi-agent demos have nothing to say about, and the one a Singapore procurement reviewer will ask about first |

🟢 **And the arithmetic rule is the one thing every regime in this file agrees on.**
[`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) (MIT, `5511bf6dc707`,
🔴 **0★, 13 commits — a reference design, not a dependency**) is the only implementation this KB can
hand an engineer: per-criterion structured output validated against the rubric, **totals computed in
Python, never by the model**, plus an answer-leak guard. **Copy both mechanisms into the engagement
repository.**

### Do this or it is negligent

1. 🔴 **Decide the biometric question before the first sprint, not at UAT.** It determines whether
   you have one build target or two, and retrofitting the EU target means removing a module from a
   shipped artefact and re-certifying it.
2. 🔴 **Produce the corpus provenance manifest from the first ingested document.** Provenance is not
   recoverable from a vector store after the fact.
3. 🔴 **Pin every component by SHA or release tag and re-read the licence bytes at that pin.**
   `p493` found eight promoted rows deleted from this KB's own shelves, and `canvas-mcp` has now
   drifted **twice in ~24 hours** — `32e5d1ca0175` → `830bc2ef8389` → `47394125364b`, the last move
   observed **inside a single pass's window**, licence byte-identical throughout. 🔵 **The rule that
   follows: pin a release tag wherever upstream publishes one, and treat a HEAD SHA as a dated
   observation rather than a pin.** Pins as read `2026-10-28` are listed in `P493-1`; the components
   in this pattern were all re-resolved at that date and only `canvas-mcp` moved.
4. 🔴 **Treat `pedagogy-benchmark` (13★), `rumi-platform` (18★), `Shiksha-Copilot` (9★) and
   `ai-tutor-agent` (0★) as corpora, not dependencies.** Vendor them; budget to maintain them.
5. 🟢 **Run `pedagogy-benchmark` before the pilot and keep the baseline**, including the **SEND**
   subset (223 items) — the population where an unevaluated tutor does most harm and where
   procurement asks hardest.
6. 🔴 **Do not claim an agent-identity requirement for Singapore.** An academic commentary
   (`arXiv:2608.15417`) asserts the framework requires verifiable per-agent digital identity and an
   audit trail; that conflicts with its voluntary standing and 🔴 **`arxiv.org` is
   `connect_rejected` by this session's proxy**, so it is unverified. Build the audit log because it
   is good practice and discharges Vietnam's evidence need — **not because Singapore mandates it.**
7. 🔴 **Honour BSD-3-Clause's third condition** on `open-tutor-ai-CE`: attribution in `NOTICE`, yes;
   **"built on Open-TutorAI" in a pitch deck, no**, absent written permission.

**Regional fit:** 🟢 **APAC-native** — `OpenMAIC` (China), `Shiksha-Copilot` (India),
`rumi-platform` (Pakistan) are in-region by origin. 🟡 **Do not carry an "APAC is permissive"
framing into Australia or New Zealand** — `p493` records ANZ showing *higher* support for banning AI
in schools than the seven APAC markets at 23–31%, an EMEA-like public mood. 🔵 **The corpus manifest
and the action log are jurisdiction-neutral and transfer to EMEA and LATAM engagements unchanged**,
which is the part of this pattern worth reusing even where Decision 33 does not apply.

**Scope:** 12–14 weeks to a governed pilot — `P493-1`'s 10–12 plus 2 weeks for the corpus manifest
and the action-log schema. 🔴 **Add 4–6 weeks if the biometric fork is in scope**, and resolve that
question in week one, because it is the only item here that cannot be parallelised.


## 🆕 `P495-1` — Hardened Canvas agent deployment 🟢 *(amends `P490-1`; supersedes its pin and its tool list)*

🔴 **Why this exists.** `P490-1` recommends [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
as the Canvas agent surface and that recommendation **stands** — it is still the only maintained
agent surface on an incumbent LMS this KB has found. 🔴 **But `p495`'s first-hand advisory read makes
the deployment details non-optional**: below `v1.16.0` the base ships **two High** advisories, and
`v1.16.0` itself is only patched **on Node.js ≥ 22.18** while its advisory states in writing that
**executed code can still reach the caller's Canvas token**.

### The stack

| role | component | licence | pin | note |
|---|---|---|---|---|
| LMS agent surface | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT *(`1 071 B`, `sha1 491fb891a4cf`)* | 🔴 **tag `v1.16.0` = `b3f06c76e43569f10f8f11833b4eb4ba2ee478ba`** | **never branch HEAD**; HEAD `47394125364b` is unreleased code above the newest tag |
| runtime | Node.js | — | 🔴 **≥ 22.18** | the sandbox fix *is* Node's permission model; older Node = unpatched |
| tutor / RAG core | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 *(see the licence caveat in [`../agents/top.md`](../agents/top.md))* | `a31d82624c27` | 🟢 5 passes byte-stable |
| quality gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | — | 1,143 teacher-exam items; 🔴 do not cite its arXiv abstract until a human opens it (`arxiv.org` is proxy-refused) |
| integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | `74b101785bad` | plagiarism detection, the most-maintained address on the permissive shelf |

### Wiring — the five hardening steps, in order

1. 🔴 **Pin the tag, not the branch.** `pip install canvas-mcp==1.16.0`, or check out
   `b3f06c76e43569f10f8f11833b4eb4ba2ee478ba`. **Record the tag in the client's SBOM**, because that
   is the only artefact that lets anyone later say which advisories were closed at ship time.
2. 🔴 **Assert the runtime, in CI, as a build failure.** `node -v` → must be **≥ 22.18**. A version
   check here is not hygiene: it is the difference between the sandbox being enforced and the
   version string merely claiming it is. **Do this before any functional test**, because every
   functional test passes either way.
3. 🔴 **Disable `execute_typescript` at the server's tool registry**, and assert its absence in the
   agent's tool list at startup. The `1.16.0` advisory states egress blocking is best-effort and
   **executed code can still access the caller's Canvas token** — so the only complete mitigation
   is that the capability is not exposed. 🔵 Nothing in `P490-1`'s use case (course Q&A, assignment
   lookup, submission summaries) needs code execution.
4. 🔴 **Scope and time-box the Canvas token.** `GHSA-7mj9-4mcg-hvhv` has the bearer token sent to a
   URL **chosen by the file-storage host** on upload confirmation. Use the narrowest Canvas
   developer-key scopes that satisfy the tool list, short expiry, rotation, and **never an
   admin-scoped token for an instructor-facing agent.**
5. 🔴 **Treat course content as hostile input.** `GHSA-hmr8-mvr2-mvw5` is a student editing course
   content to instruct the instructor's assistant, reaching **grade change**. `1.13.0` added a write
   allowlist and message previews; `1.16.0` marks `read_course_file` contents untrusted. 🔵 **Keep
   both**: no write tool reachable on a first call, and a human preview on any grade-affecting
   action. **Log every write with the prompt that produced it** — which is also what satisfies
   Singapore's agentic-AI framework (action logging, human-in-the-loop placement, accountability
   across agents) per [`../intel/market.md`](../intel/market.md), and is reusable as evidence rather
   than as overhead.

### What this pattern is worth saying out loud to a client

🔵 **The deployable posture here cost a release-tag read, four advisory reads, a CVSS read and a
runtime check** — none of which a university IT department will do before installing an MCP server
someone demoed to them. 🟢 **That gap is the engagement.** The sellable artefact is not the tutor:
it is **a pinned, hardened, logged integration with a written risk register**, on an MIT base the
client can keep.

🔴 **Say the residual risk plainly, because it does not go away with the patch:** an agent holding an
instructor's Canvas token and reading student-editable content is a real attack surface. The
mitigation is capability-removal and credential-scoping, and the **audit log is the control that
makes the remaining risk detectable** rather than deniable.

### 🟡 Honest limits of this recipe

- 🔴 **`v1.16.0` is the newest tag AND the minimum safe one.** There is no headroom: the next
  advisory has no released fix to point at. **Re-read the advisory page before each client ship** —
  do not inherit this pass's count of four.
- 🟡 **Advisory severities were read from the GitHub advisory pages, not from CVE records.** The
  CVSS vector is published for `GHSA-7pp5-29mw-9jq3` (7.8) and **not** for the other three.
- 🔴 **`DeepTutor`'s licence caveat and `pedagogy-benchmark`'s unread paper are unchanged** and both
  need a human (`arxiv.org` is **proxy-refused** from this session, permanently — `p494`/`p495`).



## 🆕 `P496-1` — IEP / accommodation drafting with a **monotonic statutory floor enforced in code** 🟢

**For:** a US district or state SELPA, or an Indian school group under the RPwD Act, that wants AI
help drafting IEPs and §504 plans without any possibility of the model weakening a legally required
accommodation.

🔵 **Where the idea comes from, and the attribution matters because the source is unusable.**
[`SudhanvaJ-bit/project-samarth`](https://github.com/SudhanvaJ-bit/project-samarth) has **no licence
at six filenames** (`d628b919449a`, `README.md → 200`), so **no line of it may be copied**. It is
read for one architectural decision, stated in its own README:

> a rule-based baseline of what the statute requires for each disability category is merged with the
> model's suggestions, and **the model can add to the list; it cannot remove from it.**

🟢 **That is the accommodation analogue of `P492-1`'s rule that the model never does the arithmetic**
— a legally binding floor held in code, not requested in a prompt. `P496-1` generalises it and
builds it from assets that are **actually licensed**.

### The stack — every component byte-verified this pass or already pinned here

| role | component | grant at SHA |
|---|---|---|
| **Statutory floor, US federal** | [`jscott5811/IEP-and-Section-504-Plans-Skill`](https://github.com/jscott5811/IEP-and-Section-504-Plans-Skill) | 🟢 **MIT**, 1 068 B, `sha1 e8b3ee2c48a2` (`cd3a9018681f`) — IDEA **34 CFR Part 300**, **§504**, ED/OCR/OSERS sources by date |
| **Statutory floor, state overlay** | [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) (CA) · [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) (AZ K-8) | 🟢 **MIT** (both, already pinned in this KB) |
| **Parent-facing navigation** | [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | 🟢 **MIT**, 1 068 B · `68657618a157` |
| **Deterministic output renderer** | [`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) | 🟢 **MIT**, 1 080 B, `sha1 fb30401f6782` (`264786ddb518`) — in-browser, no server, no AI service |
| **Agent runtime** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** (`96f33faaf028`) |
| **Orchestration + durable state** | LangGraph (MIT) · Temporal (MIT) | 🟢 permissive, both already on these shelves |
| **Pedagogical regression gate** | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) + [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT** both — `21a43a395ab4` stable this pass; **223 SEND items** are the relevant subset |
| **Reference design only — do not import** | `SudhanvaJ-bit/project-samarth` | 🔴 **no grant** |

🟢 **Every buildable component is MIT or Apache-2.0.** This is the second all-permissive stack in
this file after `P493-1`.

### Wiring — the floor is the whole point, so build it first

1. **Encode the floor as data, not prose.** From the MIT knowledge packs, build a table keyed by
   `(jurisdiction, disability category) → required accommodations/services`. Federal (IDEA/§504)
   rows from `jscott5811`; state rows overlaid from the California and Arizona packs. 🔴 **Hand-check
   this table against the cited regulation.** It is the only artefact in the system that must be
   right, and it is small enough to review.
2. **Let the model propose only additions.** The agent returns a *candidate set*. Merge is
   `final = floor ∪ model_suggestions`, computed in Python. 🔴 **The model never sees a delete
   path** — not a discouraged one, an absent one. Any suggestion that collides with a floor item is
   recorded as a comment on that item, never as a replacement.
3. **Make removal possible only for a named human.** A floor item can be removed **only** by an
   authenticated user with a role that the district maps to IEP-team membership, and the removal
   writes an audit row: who, when, which statute cite, what justification. 🟢 **This is what makes
   the system lawful rather than merely cautious** — IDEA contemplates team decisions, not immutable
   plans.
4. **Track authorship per field.** Store, for every field, whether its current value is AI- or
   human-authored, and preserve the original model output alongside edits. 🔵 Taken from
   `project-samarth`, which does this and is right to.
5. **Render deterministically, and keep the document off the network.** Fork `rtwergrfh-cmyk/iep`
   for the per-adult plain-language sheets. 🟢 **It uses no model and no server**, so the finished
   IEP never leaves the browser — which answers the egress objection architecturally (`T9`'s
   non-egress leg, `intel/trends.md` `p496`). 🔴 Honour its mixed grant: `pdf.js` **Apache-2.0**,
   Nunito **SIL OFL 1.1** — OFL restricts **renaming** the font, so a district rebrand must not
   rename it.
6. **Gate on the SEND subset before every release.** Run `pedagogy-benchmark`'s **223 SEND** items
   through `lm-evaluation-harness` and block deploys on regression. 🟢 This is the only
   education-specific, **licensed** instrument that touches special educational needs.

### 🔴 Calibrate the compliance gate, or you have rebuilt the bug

`project-samarth` reports **15 of 15** evaluation runs returning `Partial`, with its compliance agent
**never once** returning `compliant`. 🔴 **A gate that never passes is uncalibrated, not
conservative** — staff learn in a week that `Partial` means nothing and stop reading it.

🟢 **Do this instead:** make the gate **mechanical and binary** — *is every floor item present in the
output, yes or no* — because that is a set-containment check, computable exactly, with no model in
the loop. Anything requiring judgement (is this goal measurable? is this accommodation appropriate?)
goes to the human reviewer as a **flag with the statute cite**, never as a score. 🔵 **Separate what
code can decide from what a person must**, and the gate becomes trustworthy because it only ever
claims the first.

### What to say to the client, and what not to

- 🟢 **"The statutory floor cannot be weakened by the model — that is enforced in code, and here is
  the table and the merge function."** Reviewable in an afternoon; the strongest sentence in this
  recipe.
- 🟢 **"The finished IEP never leaves the browser."** True, because the renderer has no server.
- 🔴 **Do not say the output is compliant.** Nothing here certifies compliance; the floor check
  proves *presence of required items*, which is necessary and nowhere near sufficient.
- 🔴 **Do not claim bilingual delivery.** The renderer's classifier is English-only and its Spanish
  translation is a **~150-phrase** list; many items still need a human translator.
- 🔴 **Do not use real student data in a pilot until storage is encrypted at rest and the district's
  FERPA — and in Illinois **SOPPA** — obligations are contracted. 🔵 **This KB holds no permissive
  asset addressing SOPPA**; `avivkatz1/easy-iep` frames it and has **no licence**.

### 🟡 Honest limits of this recipe

- 🔴 **There is no special-education platform to build on** — open or permissive, none exists
  ([`../verticals/solutions.md`](../verticals/solutions.md) `p496`). This composes knowledge packs
  and a renderer beside the district's existing system of record; it does **not** replace it, and
  there is **no integration surface** to attach to the way Canvas or Moodle offer one.
- 🔴 **Jurisdiction coverage is three deep, not fifty.** Federal + California + Arizona, plus
  Missouri parent-facing content. Every other state is net-new work, and the state packs are
  **0–1★ single-author repositories** — fork them, do not depend on them.
- 🔴 **India needs the floor rebuilt from the statute.** The RPwD Act / NCTE route has **no licensed
  asset at all**; `project-samarth` is a read, and upstream itself says board- and state-specific
  rules are not implemented. 🔵 Scope that as statutory research, not as integration.
- 🟡 **Every MIT component here is tiny** — 1 to 55 commits, 0–13★, no release tags on most. 🟢 That
  is tolerable precisely because they are *knowledge packs and renderers* rather than runtimes: the
  value is the pinned regulatory content, which a fork freezes safely. 🔴 It would not be tolerable
  for the agent runtime, which is why that slot is `smolagents` (Apache-2.0, 30,100★).

## 🆕 `P497-1` — Admissions triage agent with the **decision** kept out of the model 🟢

**For:** a university or ministry that wants AI in admissions before **2 December 2027**, when EU AI
Act Annex III point 3 obligations bite — or a US district under a state AI-policy mandate (Ohio,
Tennessee, Maryland, Idaho, Oklahoma, Virginia).

**Why this pattern exists:** admissions is a **designated high-risk function in every regime this KB
tracks**, and until `p497` there was **no buildable admissions asset on these shelves** — 59 files of
regulatory prose, nothing to implement (`T18`). There is now exactly one, at 5★.

### The parts, each with its licence read from bytes at a pinned SHA

| role | repo | licence | pin | why this one |
|---|---|---|---|---|
| **Reference architecture** (read, re-implement — do not depend) | [`ASUCICREPO/Admissions-AI-Agent`](https://github.com/ASUCICREPO/Admissions-AI-Agent) | **MIT**, 1 123 B, `sha1 8a0aae668604` | `fcbbbb2fe19f` | 🟢 The only admissions agent on these shelves, authored by **Arizona State University's AI Cloud Innovation Centre**. Its adviser-handoff boundary is the part that carries the compliance story. 🔴 **5★ and AWS-Bedrock-AgentCore-bound** — the MIT grant covers orchestration, not a portable runtime |
| **Agent runtime** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | Apache-2.0 | `96f33faaf028` | Minimal code-writing loop; keeps the orchestration yours and portable off Bedrock |
| **System of record** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0**, 15 214 B, `sha1 58cb1cfbf839` | `fa5f4b66caf4` | Holds applicants, enrolments, grades. 🔴 **Default ref is `refs/heads/mobile`** — resolve the symref or you clone nothing |
| *(higher-ed alternative)* | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `46a5d7d40082`, **`refs/heads/19.0`** | Admissions + fees + timetable on Odoo |
| **Eval harness** | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | `21a43a395ab4` | The licensed evaluation instrument (`p493`) |

🔴 **Licence boundary, and it decides the architecture.** `rosariosis` is **GPL-2.0** and
`openeducat_erp` **LGPL-3.0**. The agent must sit **out of process** and talk over HTTP, never link
the SIS as a library. That is not a style preference — linking makes Globant's agent a derivative
work of a copyleft SIS. There is **no permissive education SIS or ERP** to avoid this with
([`repos/foundations.md`](../repos/foundations.md) `p497`, settled).

### Wiring

```
applicant submits
      │
      ▼
┌─────────────────────────────────────────────────────┐
│ smolagents orchestrator  (Apache-2.0, yours)        │
│                                                     │
│  1. EXTRACT    transcript/docs → structured fields   │
│  2. CHECK      eligibility rules in DETERMINISTIC    │
│                CODE — not the model  ◄──── P492-1    │
│  3. EXPLAIN    model drafts rationale TEXT ONLY      │
│  4. ROUTE      complete / incomplete / needs-human   │
└───────────────┬─────────────────────────┬───────────┘
                │ HTTP (never linked)     │
                ▼                         ▼
        rosariosis / openeducat     human adviser queue
        (GPL-2.0 / LGPL-3.0)        ← EVERY admit/deny
                                       decision lands here
```

### The four rules that make this conformant rather than merely working

1. 🔴 **The model never decides.** It extracts, explains and routes. Admit/deny/waitlist is produced
   by rule code or by a human. This is `P492-1`'s arithmetic rule generalised from grading to
   admissions: **the model touches no number and no outcome.**
2. 🔴 **Eligibility rules are code, versioned, and replayable.** Given an applicant record and a
   ruleset version, the outcome must be reproducible without an LLM call. That is what you show a
   regulator.
3. 🟢 **Every decision has a named human.** The ASU design's adviser-handoff is the part to copy. An
   Annex III high-risk system needs demonstrable human oversight, and "a human could have looked" is
   not demonstrable — log who did.
4. 🔴 **No emotion recognition, anywhere.** Banned outright in EU education since **February 2025**
   (`T6`), interview video included. Do not add sentiment scoring to an applicant interview.

### Transparency, which bites sooner than the high-risk rules

🔴 **Article 50 chatbot-transparency duties apply from 2 August 2026 — already in force.** If the
applicant-facing surface is conversational, it must disclose it is an AI. 🟢 **Build that in from day
one**; it is cheap now and it is a finding later. The **2 December 2027** Annex III date is the
runway for the rest.

### What to tell the client about the gaps

🔴 **Placement and proctoring have no permissive open-source supply at all** — nothing for placement
in any pass, and nothing permissive out of 145 `topic:proctoring` repositories (`T18`). If the
engagement scope creeps into either, **re-price it as a build.** Do not promise composition where
there are no parts.

🔵 **Both regulatory citations here are search-channel reads.** `eur-lex.europa.eu` is `ENOTFOUND`
from this session (`p495`), so Regulation (EU) 2026/1744 and the Annex III point 3 scoping are
upstream-asserted. 🔴 **Have counsel confirm the dates against the Official Journal before they go in
a statement of work.**

### Effort

**8–10 weeks** to a governed pilot: 2 weeks reading and re-implementing the ASU design off Bedrock,
2 weeks rule engine and replay harness, 2 weeks SIS integration over HTTP, 2 weeks oversight logging
and Article 50 surface, 2 weeks evaluation against `pedagogy-benchmark` plus counsel review.

---

## 🆕 `P498-1` — Kolibri as an AI **host**, not a content sink 🟢 *(amends the Kolibri row in `P490-3` and `P493-1`)*

**Why:** `P490-3` and `P493-1` both use [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
as a **delivery sink** — generate study packages centrally and online, ship them into Kolibri's
offline content channels. 🟢 `p498` read the code at HEAD `08e3ecace444` (ref `develop`, last commit
2026-10-27) and Kolibri is an **extension host with a documented plugin contract**. The difference is
the difference between shipping a client pre-baked content and shipping them an in-platform AI
surface they control — on the only **MIT** institutional platform that exists.

| Component | Repo | Licence | Role |
|---|---|---|---|
| Host platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1 097 B · blob `6506702f35f3`) | Offline-first platform; pin at `08e3ecace444`, ref **`develop`** |
| Your AI surface | *(the plugin you write)* | yours | A Django app with a `kolibri_plugin` module, mounting its own URLs + DRF API |
| Source → study assets | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | **MIT** | Curriculum source → quizzes, flashcards, SRS items |
| Source → agent knowledge | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **MIT** (blob `b000bdffeaa2`) | Long-form PDF → a structured skill the plugin's agent reads. Default ref 🔴 `master` |
| Learner model | [beltromatti/get-it](https://github.com/beltromatti/get-it) | 🟡 **Apache-2.0, §6 edited** (blob `29492aec7faa`) | Knowledge graph + prerequisite ordering + spaced repetition. **Read the §6 note below** |
| Lesson structure | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | Explorations with misconception handling. Default ref 🔴 `develop` |
| Quality gate | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 1 143 teacher-exam items, run in CI |
| Eval runtime | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** | The harness the benchmark runs on |

🟢 **Every component is MIT or Apache-2.0.** This is an all-permissive stack — no AGPL, no
GPL, no non-commercial content asset.

### Wiring — against the contract that is actually in the code

1. **Build the AI surface as a plugin, not a fork.** A Kolibri plugin is a Django app containing a
   `kolibri_plugin` module; enabling it adds its apps to `INSTALLED_APPS`. Subclass
   `KolibriPluginBase` and implement `url_module` and `api_url_module` — the plugin then serves **its
   own pages and its own DRF API** inside Kolibri. Copy the shape of `kolibri/plugins/learn/`
   (learner-facing) or `kolibri/plugins/coach/` (teacher-facing): each is itself a plugin with
   `kolibri_plugin.py`, `api_urls.py`, `views.py`, `viewsets/`, `frontend/`, `buildConfig.js` and
   `package.json`.
2. **Ship it out-of-tree as a Python package.** The repository carries four worked examples under
   `python_packages/`: `kolibri-oidc-provider-plugin`, `kolibri-sentry-plugin`,
   `kolibri-sync-extras-plugin`, `kolibri-context-translation-plugin`. 🟢 An **OIDC provider** shipped
   as a plugin is proof the extension surface reaches authentication, so an AI surface is not
   stretching it.
3. **Keep generation central and online; keep inference local or optional.** `Skill-Anything` and
   `book-to-skill` run against the ministry's approved curriculum **in your environment**, producing
   content channels and structured skills. The plugin consumes those offline. Only the
   conversational surface needs a model at the edge, and that is the piece the institution can turn
   off.
4. **Put the learner model in the plugin's own tables.** `get-it`'s graph gives prerequisite
   ordering and spaced-repetition scheduling; `oppia` explorations carry remediation. Both are
   permissive, so the model stays yours.
5. **Gate releases on `pedagogy-benchmark` via `lm-evaluation-harness` in CI** — not as a one-off
   report. This is `P491-1`'s rule and it does not change here.

### 🟢 The clause that makes this pattern sellable

🟢 **Kolibri plugins are enabled and disabled from the CLI or a UI, and through
`ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`.** Write this into
the SOW:

> *The AI surface is a separately-packaged plugin. The institution disables it with one environment
> variable, with no rebuild and no redeployment of the platform. With the plugin disabled, Kolibri
> runs exactly as it does today.*

🔵 **That is a materially different regulatory object from an AI feature compiled into a platform.**
For an EU engagement it is the cleanest answer available to *"can this be switched off"*; for a
ministry pilot it is the answer to *"what happens when the next administration disagrees"* — which
is the LATAM failure mode [`intel/market.md`](../intel/market.md) names this pass. 🟢 And **there is
no incumbent AI to unwind**: the code read found **zero** LLM integration across 3 071 Python/Vue/JS
files.

### 🔴 Do this or it will bite

1. 🔴 **Hooks are singletons.** `KolibriHook` uses metaclass `KolibriHookMeta(SingletonMeta)` and
   raises `HookSingleInstanceError`. **One registration per hook.** If the client may run a second
   vendor's plugin, agree the hook split before you build, not at integration.
2. 🔴 **Honour the project's own rule or you will fork by accident:** *"a plugin should **never**
   modify internals of Kolibri or other plugins without using the hooks API or normal conventional
   Django scenarios."* Every internal reach-around is an upstream merge you will own forever.
3. 🔴 **Pin `develop`, not `main` — `main` does not exist.** Kolibri's default ref is `develop`, as
   are `oppia`'s and `frappe/*`'s; `book-to-skill`'s is `master`. **15 of 76 rows on these shelves
   are on a non-default ref across 11 distinct names**, four of them version numbers. Resolve with
   `git ls-remote --symref <url> HEAD`, which returns the ref and the SHA in one call.
4. 🔴 **Re-read `get-it`'s `LICENSE` bytes at your pin and tell the client about §6.** Five words
   are deleted from the Apache trademark clause (see [`agents/top.md`](../agents/top.md) `p498`). It
   does not block use; it narrows a safe harbour your own marketing copy may rely on.
5. 🟡 **No release pin is offered here because none was read.** Kolibri's version is re-exported from
   `kolibri._version` and was not resolved, and no tag list was read (`Gap 498-G`). **Pin the commit
   SHA**, and resolve a release tag before a production engagement.
6. 🔴 **Do not reach for `cn-math-taxonomy` to seed the learner model.** It is the best
   curriculum-aligned knowledge graph found this pass — 1 644 nodes, 2 403 prerequisite edges, 6 723
   items — and it is **CC BY-NC 4.0**. Use its *scope* as your estimate; build the graph.

### Scope

🟡 **8–12 weeks** for a first plugin with one learner-facing surface, the content pipeline and the
CI gate — the pipeline is the long pole, as in `P490-3`. 🔴 **Uncalibrated.** `Gap 484-A` (nothing on
these shelves has been executed) and `Gap 484-V` (no range calibrated against a delivered
engagement) both bound this figure, and this pattern was composed from a code and licence read, not
from running the stack (`Gap 498-I`).

### 🆕 Registered

| gap | statement |
|---|---|
| 🔴 **`Gap 498-I`** | `P498-1` is composed from a **code read**, not an execution. No Kolibri plugin was scaffolded, built or loaded. The plugin contract is quoted from `kolibri/plugins/__init__.py`, `hooks.py` and `registry.py` at `08e3ecace444`; that it works as described for an *AI* surface specifically is inference. |
| 🟡 **`Gap 498-J`** | The `ENV_VAR_*` kill-switch claim is read from `ConfigDict` properties in `kolibri/plugins/__init__.py`. **Nobody has toggled one.** It is the load-bearing sentence of the SOW language above. |

---

## P499-1 — Closed AI tool inside an LMS you do not own, over LTI 🟢

**Why this is the most commercially useful pattern on this shelf.** Every other pattern here either
accepts the host LMS's copyleft or avoids the incumbents entirely. This one does neither. The
education platform layer is GPL/AGPL — Moodle, Canvas, Open edX all are — and a client who wants a
**hosted, closed, multi-tenant** AI product has been told by this KB to pick `OpenOlat` (448★) and
give up the installed base. 🟢 **`p499` read the layer above the LMS and both of its standards are
permissive**, which means the product can be closed and the host can still be Moodle.

🟢 **The licence boundary, stated precisely:** LTI is a **network protocol**, not linking. A tool
that speaks LTI to an AGPL-3.0 LMS is a **separate work communicating at arm's length** — it does
not become a derivative of the LMS, and AGPL §13's network clause binds *the LMS operator*, who is
the institution, not you. The tool you ship stays under whatever licence you choose.

| Component | Repo | License | Operative verdict | Role |
|---|---|---|---|---|
| **LTI tool framework** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** `214d11084b7f` | 🟡 −4 (§4 list enumerators only; conditions verbatim) | Speaks LTI 1.1/1.3 + IMS Global + Common Cartridge. This is the plug. |
| **Courseware runtime** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** `86ab328f0e5b` | 🟢 IDENTICAL | SCORM 1.2 / 2004 / CMI, cross-frame. Needed wherever the client's content is already SCORM-packaged. |
| **Tutor agent** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT** `68788b5e7d34` | 🟢 IDENTICAL | Adaptive tutoring loop. Swap for `zijinz456/OpenTutor` (MIT, runs locally) when data cannot leave the building. |
| **Credentials / competency** | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 **MIT** `18f76c220561` | 🟢 IDENTICAL | Emits the competency record and digital credential the institution actually wants back. |
| **Host LMS** (client's, unchanged) | Moodle / Canvas / Open edX | 🔴 GPL-3.0 / AGPL-3.0 | — | 🟢 **Not modified, not linked, not forked.** No plugin fork means no copyleft reach. |

**Wiring.** Register the Tsugi tool in the LMS as an **LTI 1.3 tool** (client id + deployment id +
JWKS). The LMS launch posts a signed OIDC id_token carrying `sub`, context and roles; Tsugi
validates it and establishes session identity — **so you never build auth, and you never hold the
roster.** The tutor agent runs behind Tsugi as a plain HTTP service. Grades go back over **LTI
Assignment & Grade Services (AGS)**, not by touching the LMS database. Where the client's existing
content is SCORM, serve it through `scorm-again` in the tool frame and keep CMI state on your side.
Attach `iblai/lms` to consume the AGS stream and issue credentials.

🔴 **The one place copyleft still reaches you:** if you fork a **Moodle plugin** or an **Open edX
XBlock** to get what you need, you are inside GPL/AGPL and the argument above is void. **Stay on
the LTI side of the boundary.** `P490-1` (Canvas MCP) is the alternative when the client wants
agent *tool-calling* against Canvas specifically rather than an embedded tool.

**Regional fit.** 🟢 **North America strongest** — LTI is near-universal in US higher ed, and this
is the pattern that reaches Canvas's installed base without the AGPL conversation. 🟢 **EMEA** — the
arm's-length boundary also keeps the **EU AI Act provider/deployer line clean**: the institution
deploys, Globant provides, and the Annex III high-risk duties land where `P490-2` already maps
them. 🟡 **APAC / LATAM** — LTI penetration is lower outside higher ed; prefer `P490-3` for
ministry-scale K-12.

**Effort.** 🔴 Bounded by `Gap 484-A` and `Gap 499-G`: **nothing in this stack has been executed.**
The LTI claims are the standard's definition and the projects' own; no launch was performed, no
grade was posted. Treat any estimate as unvalidated.

---

## P499-2 — Pronunciation assessment with a named model, self-hosted 🟢

**Why:** every "AI language tutor" pitch in this market is a prompt around a chat model. This one
is a **measurable** component: phoneme-level scoring from an acoustic model, which produces a
number a ministry procurement can evaluate — and `p497`'s Annex III framing says the sellable cut
is the **function**, not the sector.

| Component | Repo | License | Operative verdict | Role |
|---|---|---|---|---|
| **Pronunciation scorer** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** `74bc17ea406e` | 🟡 +2 (title words) | **Wav2Vec2 + DTW**, phoneme-level English scoring. Self-hosted alternative to the commercial speech APIs. |
| **Practice surface** | [`langx/langx`](https://github.com/langx/langx) | 🟢 **BSD-3-Clause** `8dd6541f1ce8` | 🟡 clause-3 name substitution (instructed) | Peer language-exchange client; where the learner actually speaks. |
| **Retention layer** | [`kirill-markin/flashcards-open-source-app`](https://github.com/kirill-markin/flashcards-open-source-app) | 🟢 **MIT** `98663982f0ae` | 🟢 IDENTICAL | **FSRS** scheduling over the phonemes the learner failed. |
| **Offline delivery** (optional) | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) **`v0.19.5`** | 🟢 **MIT** | 🟢 IDENTICAL | Ships the lesson where there is no connectivity. |

**Wiring.** `OpenPronounce` runs as a self-hosted inference service — audio in, per-phoneme score
out. The practice surface posts learner audio and renders the phoneme heatmap. Failed phonemes
become FSRS cards, so the next session drills exactly the sounds that scored badly. 🟢 **The whole
stack is permissive and runs without a hosted model vendor**, which is what makes it viable where
student audio cannot leave the jurisdiction — EU, and every LATAM ministry deployment.

🔴 **Caveats, stated:** `OpenPronounce` is **English-only** and last pushed **2026-08-15**. Nothing
here was executed (`Gap 499-G`), so "phoneme-level accuracy" is the project's claim. Student voice
is **biometric-adjacent**: under the EU AI Act, emotion recognition in education is banned outright
(`T6`) — scoring *pronunciation* is not emotion recognition, but the data handling sits close
enough that the DPIA is not optional.

---

## 🔧 `P498-1` amended — the pin becomes a release (`Gap 498-G` closed)

`P498-1` pins **a commit** because no Kolibri release cadence had ever been read, and `Gap 498-G`
recorded that as a defect. 🟢 Read this pass with `git ls-remote --tags`: **542 tags.**

| | |
|---|---|
| 🟢 **pin this** | **`v0.19.5`** — current stable |
| in flight | `v0.20.0-alpha0`, `v0.20.0-alpha1` |
| cadence | `v0.19.3` → `v0.19.4` → `v0.19.5`, each preceded by `alpha`/`beta`/`rc` pre-releases |

🟢 **`P498-1` and `P499-2` both pin `v0.19.5`.** The project ships release candidates before every
minor, so a client can track `v0.19.x` for production and validate `v0.20.0` pre-releases out of
band. 🔵 `Gap 498-J` is untouched — **nobody has toggled `ENV_VAR_ENABLED_PLUGINS`**, and that is
still the load-bearing sentence of `P498-1`'s SOW language.

---

## 🆕 `p500` — `2026-10-28` — three patterns, each keyed to a regulation or licence fact established this pass

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Every component below is a row verified from bytes at a pinned commit SHA — see
[`agents/top.md`](../agents/top.md) `p500`, [`repos/foundations.md`](../repos/foundations.md) `p500`
and [`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv).

---

## P500-1 — Student-success advising agent for US higher ed, without the Elastic trap 🟢

**Why:** advising and retention is one of the most-bought education-AI capabilities, and this pass
established that the leading open-ish implementation —
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) (340★) — is **Elastic License
2.0**, which forbids providing the software to third parties as a hosted service. A hosted advising
product **cannot** be a fork of it. This pattern reaches the same capability from permissive parts.

**Components**

| Role | Component | Licence |
|---|---|---|
| Way into the institution's LMS | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0, 10 273 B |
| Courseware/progress signal | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 MIT, 1 072 B |
| Competency + credential state | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 MIT, 1 063 B |
| Output QA against rubrics | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (**code only**) | 🟢 MIT, 1 615 B |

**Wiring**

1. Register a **Tsugi** LTI tool against the incumbent LMS (Canvas, Moodle, Open edX). Tsugi is the
   boundary that does not require owning the LMS — no fork, no migration.
2. Read progress through **scorm-again**'s CMI runtime and competency state from **iblai/lms**;
   these two give the agent a factual record instead of a chat history.
3. The advising agent proposes interventions. **Gate every student-facing message** behind the
   **evaluators** rubric families (Feedback, Text Complexity) so tone and reading level are checked
   before send.
4. 🔴 **Deploy the evaluators' MIT code with your own rubric data.** The shipped annotated **CLEAR**
   and **PERSUADE 2.0** corpora are **CC BY-NC-SA 4.0 — non-commercial** and must not ship in a paid
   engagement (`Gap 500-E`).
5. Enforce **human-in-the-loop** on anything touching grading or discipline — see `P500-2`.

**Licence posture:** 🟢 all four components permissive; a closed hosted derivative is lawful.
🔴 The corpus carve-out in step 4 is the one hard constraint.

**Estimate:** 8–10 weeks to a pilot against one LMS.

---

## P500-2 — District AI policy-conformance layer for US K-12 🟢

**Why:** `T14` and the North America read. **Oklahoma SB 1734** would require a written district AI
policy before AY 2027–28 and **bar AI as the primary basis for grading or discipline**; **NYC** runs
a moratorium on student-facing AI through grade 8; most US public schools have no formal policy
while teacher use is near **60%**. The gap between mandated use and governed use is the deliverable.

**Components**

| Role | Component | Licence |
|---|---|---|
| Teacher-side generation, local-first | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 MIT, 1 078 B `18f2e223cdd1` |
| LMS boundary | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 |
| Output QA / reading level | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (code) | 🟢 MIT |
| Sequencing policy, swappable | [`shigella520/MindTrain`](https://github.com/shigella520/MindTrain) | 🟢 MIT, 1 067 B `7115c484c77e` |

**Wiring**

1. **Claw-ED** runs **local-first** against the district's own curriculum and chosen model. This is
   the architectural reason to pick it: under a grade-8 moratorium or an under-13 ban, the defensible
   deployment is one where no student-facing inference leaves the district's control.
2. Put an **age/grade gate** in front of every student-facing path, configured per district. NYC's
   grade-8 line and the UAE's under-13 line are the same control with a different constant — build
   it as configuration, not a branch.
3. Route teacher-authored output through **evaluators** for reading-level and feedback-quality
   checks before it reaches students.
4. **MindTrain**'s pluggable schedulers hold the sequencing policy, so a district can swap the
   progression rule without a code change.
5. **The compliance artefact is the point:** emit an append-only audit record — which model, which
   prompt, which student artefact, which human approved it. **SB 1734**'s grading/discipline bar is
   satisfiable only if you can show a human decided.

**Licence posture:** 🟢 fully permissive.
**Estimate:** 6–8 weeks for the gate + audit layer over an existing LMS; add 4 weeks for Claw-ED
curriculum onboarding.

---

## P500-3 — Multi-jurisdiction APAC tutoring deployment, keyed to Vietnam's grace period 🟢

**Why:** **Vietnam's Law on Artificial Intelligence** (in force **1 March 2026**) gives education
systems **already operating before 15 August 2026** additional time to comply — a statutory
advantage for *integrating with the incumbent stack* rather than replacing it. South Korea's **AI
Basic Act** and China's targeted measures need separate policy nodes; Japan, Singapore, Hong Kong,
Australia and India run on existing law.

**Components**

| Role | Component | Licence |
|---|---|---|
| Permissive RAG tutor, APAC curriculum | [`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) (EduAgent) | 🟢 MIT, 1 068 B `2987df2be268` |
| Institutional LMS, closed derivative allowed | [OpenOlat](https://github.com/OpenOLAT/OpenOLAT) | 🟢 Apache-2.0, 10 982 B `cd91a957ea2e` |
| Live classroom response | [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 🟢 Apache-2.0, 11 357 B `c4c0cb0b30b5` |
| LMS boundary where the incumbent stays | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 |

**Wiring**

1. **In Vietnam, do not replace the incumbent LMS.** Attach via **Tsugi** LTI so the deployment is
   a continuation of a system operating before **15 Aug 2026** — that is what the carve-out
   attaches to. Replacement forfeits the grace period.
2. **EduAgent** supplies the RAG tutor, already built against a K-9 curriculum rather than
   retrofitted from a Western one. 🔴 Reconcile its grade range first: the repo description says
   grades 1–9 and its README says 1–12.
3. Where a greenfield institutional platform *is* wanted (and a closed derivative is required),
   **OpenOlat** is the permissive full LMS — Apache-2.0 re-verified from bytes this pass, its
   +99-word residual being attribution prose with no added condition.
4. **realtime-quiz-framework** carries synchronous whole-class response; pair it with the LMS for
   roster and gradebook, which it does not provide.
5. **One policy node per jurisdiction**, not one per region. Vietnam (carve-out + in-force duties),
   South Korea (AI Basic Act), China (recommendation-algorithm, deep-synthesis, generative-AI and
   AI-content-labelling measures), and a light-touch default for JP/SG/HK/AU/IN. 🔴 Do not carry an
   **ANZ** deployment on pan-APAC sentiment — Australia and New Zealand show *higher* support for
   banning AI in schools than the 23–31% band across the rest of the region.

**Licence posture:** 🟢 all components permissive; closed hosted derivative lawful in every
jurisdiction above.
**Estimate:** 10–12 weeks for two jurisdictions; +3 weeks per additional policy node.


## 🆕 `p501` — `2026-10-28` — two patterns: the layer this base had no recipe for, and the licence artefact every engagement now needs

## P501-1 — Social-emotional / soft-skills coach for a school district, with the decision kept human 🟢

**Why:** `T23` established this pass that **every tutoring row on these shelves is cognitive** —
knowledge tracing, content generation, lesson planning, classroom simulation — and that
*"social-emotional"* returned **0 hits across four live shelves** before `p501`. An engagement that
says *"AI tutor"* and means **conflict resolution, communication practice, interview prep or an SEL
curriculum** had no recipe here. It now has exactly one permissive component, so this pattern is
honest about resting on a single row.

🔴 **And it is the riskiest education pattern on this file.** A system coaching a child's emotional
conduct sits closer to the EU's Annex III *"evaluates learners"* line, and to New York City's **red
tier** (grading, discipline, promotion, graduation), than a maths tutor does — while being **less
measurable**. The architecture below exists to keep it on the assistive side of that line.

**Components**

| Role | Component | Licence (read at SHA) |
|---|---|---|
| SEL role-play + feedback engine | [`GeminiLight/SocialCoach`](https://github.com/GeminiLight/SocialCoach) | 🟢 **Apache-2.0**, 11 358 B, blob `d645695673…`, **`0/0` operative**, at `84f67257f5aa` |
| Way into the incumbent LMS | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0, 10 273 B |
| Rubric gate on every learner-facing message | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (**code only**) | 🟢 MIT, 1 615 B |
| Teacher-review routing shape | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot) | 🟢 MIT, 1 141 B |
| Offline / low-connectivity delivery | Kolibri (**pin `v0.19.5`**, not a commit) | 🟢 MIT |
| No-app delivery surface, 15 languages | [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform) | 🟢 Apache-2.0, 11 287 B |

**Wiring**

1. Register **Tsugi** as an LTI tool against the district's existing LMS. 🔵 No fork and no
   migration — `T2`'s re-scoping is what makes this reachable without inheriting a copyleft
   platform.
2. Run **SocialCoach** behind it as the scenario engine. 🔴 **Pin a commit, not a tag: it has
   239 commits on `main` and no release.** Vendor it into your own build; do not track `main` in a
   client deployment (`Gap 499-H`'s caveat, and the reason this is a watch row on
   [`agents/top.md`](../agents/top.md)).
3. **Gate every learner-facing utterance** through the **evaluators** rubric families before send —
   tone, reading level, and an escalation rule for any disclosure a role-play may surface. 🔴 Ship
   the **MIT code with your own rubric data**: the shipped annotated **CLEAR** and **PERSUADE 2.0**
   corpora are **CC BY-NC-SA 4.0 — non-commercial** and must not ship in a paid engagement
   (`Gap 500-E`).
4. **Keep the agent out of every decision of record.** Following **Shiksha-Copilot**'s shape, any
   observation about a pupil — a pattern, a concern, a flag — is routed to a **named educator who
   decides**, with the decision and its author logged. 🔵 This is the one architecture that satisfies
   Oklahoma S.B. 1734, NYC's red tier, and the EU's assist/decide split **at the same time**; see
   [`intel/market.md`](../intel/market.md) `p501`.
5. For LATAM and African deployments, deliver through **Kolibri** offline or **rumi-platform**'s
   **WhatsApp** surface. 🔵 Argentina's **75% high-SES vs 42% low-SES** usage split makes an
   offline path a *procurement criterion*, not a nicety.
6. 🔴 **Scope language capability before build** (`T15`): SEL coaching is conversational and
   culturally loaded, so a model that handles the language of instruction only passably will fail
   here in ways a maths tutor would survive.

**What this pattern cannot claim**

🔴 **Nothing below was built or run.** Every component is a licence-and-description read
(`Gap 499-G`, `Gap 484-A`), so **no effort range is given** — this base has produced none it can
defend. 🔴 **SocialCoach's 57 forks and 239 commits are its only evidence of use**; no deployment,
benchmark or learning outcome was found for it. 🔴 **There is no SEL evaluation instrument on these
shelves at all** — `evaluators`' rubric families are about text quality, not emotional-coaching
safety. 🔵 If the buyer asks *"how will we know it worked?"*, the honest answer today is **an
instrument has to be built**, and that should be scoped and priced as its own work.

## P501-2 — The licence-assurance artefact an engagement can hand to counsel 🟢

**Why:** every pattern on this file turns on a licence fact, and this pass found how fragile those
facts are: a **6-path probe that reported GPL-3.0 ERPNext as having no grant**; a grader that
labelled a **CERN-OHL-S-2.0** hardware licence `BSD-2-Clause`; **three instruments producing three
different operative-word counts for one payload**; a **search-sourced version number stale by
twenty minor releases**; and a **CC-BY-NC** row sitting in supply that looks permissive at a glance.
🟢 Each of those is now fixed or bounded, and the parts compose into something a client's counsel
can actually read.

**Components** — all in this repository, all permissively licensed or self-authored

| Role | Component |
|---|---|
| 12 canonical licence payloads, pinned with bytes + blob SHA-1 + SHA-256 | [`evidence/canonical/`](../evidence/canonical/) + `MANIFEST.tsv` |
| Retention **and** upstream-amendment check | [`p501-abstention-and-reresolve/reresolve_canonical.py`](code/p501-abstention-and-reresolve/reresolve_canonical.py) |
| Family grading **with abstention** | [`p501-abstention-and-reresolve/grade_abstain.py`](code/p501-abstention-and-reresolve/grade_abstain.py) |
| Payload resolution at a pinned SHA | [`p501-abstention-and-reresolve/fetch_lic.sh`](code/p501-abstention-and-reresolve/fetch_lic.sh) |
| Multi-form canonical comparison | [`p500-dual-canonical-grader/`](code/p500-dual-canonical-grader/) |

**Wiring**

1. **Freeze the dependency set at SHAs, not tags or branches.** Resolve each with
   `git ls-remote --symref`; `api.github.com` returns **403** for arbitrary repositories and
   `curl -sI` on `github.com` returns **403 for existent and non-existent alike** — it has **zero
   discriminating power** and must never be used as an existence check (`Gap 498-M`).
2. **Resolve each licence payload at its pinned SHA over `raw.githubusercontent.com`** (200 real /
   404 fake — the gate that does discriminate). 🔴 **Probe 22 path forms, not six**: vary case and
   extension *together*, or you will report GPL-3.0 code as unlicensed exactly as this base did to
   ERPNext.
3. **Grade each payload against every retained form of its family and keep the best match**
   (`p500`'s rule) — otherwise the two legitimate Apache-2.0 forms manufacture a phantom `−19` and
   a correctly-licensed dependency reads as `DEVIANT` to a lawyer.
4. **Let the grader abstain.** `rel = (ins + del) / canonical_words`; label at `rel ≤ 0.15`,
   otherwise **`ABSTAIN` naming the nearest family and the distance**. An `ABSTAIN` row is routed to
   a human, which is the correct outcome for CERN-OHL-S, CC-BY-NC and anything else outside the set.
5. **Run the retention + amendment check every build.** Check A proves the retained canonicals are
   unchanged; **check B re-reads the same paths at the publisher's moving ref** and is the only one
   that can catch an upstream amendment. 🔵 Today they agree because
   `spdx/license-list-data` HEAD **is** the pinned commit `f715b366…`.
6. **Every instrument gets a known-good and a known-bad input before its output is used**, and the
   run prints `rows_in`/`rows_out` with an explicit `ASSERT` (`Gap 498-L`, `Gap 498-M`). 🔵 This
   pass's own first run reported *"`www.apache.org` unreachable"* — a prose annotation in a URL
   column — and the direct probe answered **200 on 3/3**.

**What the artefact contains, and what it is worth**

A per-dependency row: repo, pinned SHA, licence path, bytes, blob SHA-1, family verdict or
`ABSTAIN`, and the operative residual. 🟢 **The residual is the part counsel cares about**: `0/0`
means the dependency ships the canonical text, and a non-zero residual is the exact word list to
read.

🔴 **Three limits to state to the client, not bury.** (a) **Operative-word counts are artefacts of
the cut** — 1 408 / 1 426 / 1 431 for the same Apache-2.0 payload across three instruments here —
so quote *residuals within one run*, never a count as a licence property (`Gap 501-C`). (b) **`BAND
= 0.15` is chosen, not derived**, and is untested between `rel=0.08` and `rel=1.02` (`Gap 501-B`).
(c) **A small positive residual on a multi-author repository is this base's bug**: the notice-line
cut is line-based and copyright notices wrap, which put 4 phantom words on a six-author academic
repo this pass (`Gap 501-E`). 🔵 **None of this is legal advice** — it is a reproducible reading of
bytes, which is precisely what makes it useful to someone who *can* give legal advice
(`Gap 499-M`).

🔴 **Not gate-attested:** `make hooks` has not run on this base for **25 passes** (`Gap 446-A`).


## 🆕 `p502` — `2026-10-28` — one pattern: the compliance evidence layer, which every regulation on these shelves requires and no recipe here has built

## 🆕 `P502-1` — **Auditable AI tutoring: the agent writes to a Learning Record Store, not to a log file** 🟢

**What it answers.** Every regime in [`intel/market.md`](../intel/market.md) converges on one demand:
*prove a human reviewed the AI's output, and produce the record on request.* EU AI Act **Art. 26**
deployer logging; **Oklahoma** barring AI as the primary basis for grading or discipline; **Vietnam**
listing automated assessment as high-risk; **UNESCO IESALC**'s 87%-adopting / **26%**-with-a-strategy
finding across 200 LATAM institutions. 🔴 **No pattern on this shelf produces that record.** `P490-2`
and `microsoft/Shiksha-Copilot` route output to a teacher for review; neither *persists the review as
evidence*.

**Every component permissive, every licence read from bytes at the SHA shown** —
[`channel-crosscheck.2026-10-28-p502.tsv`](../evidence/channel-crosscheck.2026-10-28-p502.tsv).

| # | Component | Repo | Licence (bytes at SHA) | Pin | Role |
|---|---|---|---|---|---|
| 1 | Record store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** 11,356 B `58853eb8199b` | `6159416` 🟢 2 d | The evidence database. SQLite for a pilot, Postgres for an institution |
| 2 | Agent↔LRS bridge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT *(carried)* | `fbf6091` 🔴 **425 d** | MCP server exposing xAPI write/read **as agent tools** |
| 3 | Profile validation | [`yetanalytics/project-persephone`](https://github.com/yetanalytics/project-persephone) | **Apache-2.0** 11,356 B `58853eb8199b` | `92a3f78` 🟢 | Rejects a Statement that does not conform to your declared profile — **at write time** |
| 4 | Conformance gate | [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** 1,045 B `f1083e4aa47d` | `5bc232d` | CI gate + the artefact you hand procurement |
| 5 | Dashboard | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** 1,093 B `14a2c9fcad08` | `839fcbb` 🔴 **708 d** | Analytics views over the LRS. 🔴 **Fork it — see below** |
| 6 | The tutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) **or** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | Apache-2.0 / **MIT** | `a31d8262` / `70859b42` | Whichever the engagement already chose — this pattern is **agent-agnostic by design** |
| 7 | Teacher-review surface | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot) | MIT 1,141 B `689ec068` | `cf2a2e24` | Already routes every artefact to a teacher before classroom use |

### How they wire together

```
 (6) tutor/content agent
        │  proposes an artefact (lesson, quiz, feedback, grade suggestion)
        ▼
 (7) teacher-review surface  ──── human decides: approve / edit / reject
        │
        │  emit ONE xAPI Statement per decision, not per generation:
        │    actor  = the teacher (the human, never the model)
        │    verb   = approved | edited | rejected
        │    object = the artefact, with the model + prompt hash as context
        ▼
 (2) learnmcp-xapi  ──MCP tool call──►  (3) persephone: profile-valid?
        │                                     │ no → reject, surface to the teacher
        ▼                                     ▼ yes
 (1) lrsql  ◄── the evidence of record ──────┘
        │
        ├──► (5) warren        — dashboards for the institution
        └──► (4) conformance suite — CI gate + procurement artefact
```

### 🔴 The four things that make this work, which a naive build gets wrong

1. **The `actor` is the teacher, not the model.** An xAPI Statement whose actor is the agent records
   that *a machine did something*; the regulations above require evidence that **a human decided**.
   🔵 This single field choice is the difference between a log and a compliance artefact.
2. **Emit on the decision, not on the generation.** One Statement per human decision. Emitting per
   model call produces volume with no evidentiary value and leaks prompt content into a store that
   institutional staff can query.
3. **🔴 Fork components 2 and 5 at the start of the engagement, not when they break.**
   `learnmcp-xapi` is **425 days** unmoved and is the *entire* open-source supply for its role;
   `warren`'s `main` is **708 days** unmoved. Both are MIT, so forking is free and permitted. 🟢
   Budget for ownership on day one and say so in the proposal — this is the sixth consecutive pass on
   which `learnmcp-xapi` has not moved.
4. **🔴 Do not judge any of these by the API's `pushed_at`.** It reports `warren` as pushed **today**
   against a 708-day-unmoved `main`, and `ADL_LRS` as pushed `2025-11-14` against a last commit of
   `2025-06-13` (`Gap 502-B`, `T25`). **Date with git.** This is why component 1 is `lrsql` and not
   the 2.3×-larger `ADL_LRS`, whose mainline is **502 days** dead.

### Licence posture

🟢 **Apache-2.0 / MIT throughout — the deliverable can be closed.** 🔵 This is the first pattern on
this shelf whose *entire* critical path avoids `T2`'s copyleft platform constraint, because it never
forks the LMS: it integrates over LTI/xAPI and owns only the record layer. 🟢 Where the client already
runs Moodle (GPL-3.0), Canvas or Open edX (AGPL-3.0), **nothing here inherits those terms** —
separate process, standards-defined wire protocol.

### Regional fit

| region | fit | note |
|---|---|---|
| **LATAM** | 🟢 **strongest** | The 87%/26% gap *is* an evidence gap. Needs Spanish/Portuguese localisation of components 5 and 7 — neither of which exists, so it is build-and-own, not integrate |
| **EMEA** | 🟢 strong | Annex III conformity assessment consumes exactly component 4's output. 🔵 Both EMEA-origin components are France Université Numérique and one is stale |
| **North America** | 🟢 strong | Oklahoma's written-policy deadline is the **2027–28 school year**; the record layer is how a district demonstrates compliance rather than asserting it |
| **APAC** | 🟡 viable, no local supply | 🔴 **No APAC record-layer repo was found** (`Gap 502-E`). The agent tier is APAC-dominant (`DeepTutor`, `OpenMAIC`), so component 6 is local and components 1–5 are imported |

### 🔴 What this pattern does **not** do

- It does not make the tutor's output correct. It records who approved it.
- It does not satisfy the EU **conformity assessment** on its own — that is a documentation exercise;
  component 4 supplies one input to it, not the file.
- 🔵 It assumes the institution *wants* the record. Where `T1`'s delivery gap is really a
  procurement-will gap, the dashboard in component 5 is the part that sells it, and that is the
  **most stale component in the stack**.

## 🆕 `p503` — `2026-10-28` — one pattern: the study companion that survives a licence audit, assembled only from rows read from bytes this pass

## 🆕 `P503-1` — **Source-grounded study companion for a paid engagement, with the non-commercial half of the supply designed out** 🟢

🔵 **The problem this solves is procurement, not pedagogy.** The obvious 2026 build — take the
fastest-growing education repositories and wire them together — produces an estate that **cannot be
billed**: of the six highest-traction unshelved rows this pass read from bytes, **three are
PolyForm Noncommercial or AGPL-3.0** (`T26`). This recipe is the same product assembled from the
three that are MIT, with the exclusions named so a reviewer can check the reasoning rather than
trust it.

| # | Component | Repo | Licence (bytes at pinned SHA) | ★ | Role |
|---|---|---|---|---|---|
| 1 | **Material ingestion** | [`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) | 🟢 **MIT** 1 122 B `f8849746d85c` (blob `361465fb8b78`) | 1 190 | PDF / book / paper → an interactive page where **every generated claim keeps a pointer to its source span**. This is the provenance leg |
| 2 | **Route planning** | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 **MIT** 1 064 B `d8114f383632` (blob `1b105b8e1b6b`) | 1 245 | Decides *what next*: a sequenced route, taught against, with a project at the end. Topics declare `learning-agents` |
| 3 | **Scheduler** | [`shigella520/MindTrain`](https://github.com/shigella520/MindTrain) | 🟢 **MIT** 1 067 B `7115c484c77e` *(carried, `p500`)* | 128 | **Pluggable schedulers** — swap FSRS for the client's own policy without touching the agent. Keeps the review policy out of the prompt |
| 4 | **Output QA** | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 **code MIT** 1 615 B `b9d47891c1b8` (blob `86eebd7ebc43`) 🔴 **corpora CC BY-NC-SA 4.0 — excluded** | 87 | Scores generated items against rubric families (Text Complexity, Feedback, Standards Alignment, Durable Skills). **Code only** |
| 5 | **Record layer** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** 11 356 B `58853eb8199b` *(carried, `p502`)* | 144 | One xAPI Statement per **human** decision, per `P502-1`. The audit trail NA districts and EU Annex III both require |
| 6 | **Practice surface** *(optional, engineering curricula)* | [`xevrion/breakscale`](https://github.com/xevrion/breakscale) | 🟢 **MIT** 1 080 B `c58de512f3ae` (blob `0c920ce1638e`) | 1 858 | The simulate-then-explain loop: the learner breaks a system and the simulator explains why. Subject-bound (distributed systems) but the loop is the reusable part |

### How they wire together

```
   client's own materials (PDFs, textbooks, standards documents)
        │
        ▼
 (1) learn-from-materials ── extracts spans ──►  page + item candidates
        │                                              │
        │                                              ▼
        │                                      (4) evaluators (MIT code,
        │                                          YOUR rubrics — see below)
        │                                              │ score < threshold → regenerate
        ▼                                              ▼ pass
 (2) Study-Mate  ── route: what next, and why ──►  learner session
        │                                              │
        ▼                                              │ (6) breakscale for lab work
 (3) MindTrain scheduler ◄── review outcomes ──────────┘
        │
        └── teacher/tutor approves, edits or rejects ──► (5) lrsql
                                                          actor = the human
                                                          verb  = approved | edited | rejected
                                                          object = artefact + source span IDs
```

🔵 **The join that makes this more than four repos in a `docker-compose`:** component 1 emits
**source-span IDs**, and those IDs travel into the xAPI Statement in component 5. The result is an
audit trail that answers *"on what basis did the system say this?"* with a pointer into the client's
own material — not *"the model said so"*. 🔴 Neither repository does this out of the box; it is the
integration work, and it is roughly **two of the engagement's weeks**.

### 🔴 Designed out, with the reason recorded

| Excluded | Why |
|---|---|
| [`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch) (**741★** *(🟢 `p512`, API)*, +92% in 14 days as read at `p504`) | 🔴 **PolyForm Noncommercial 1.0.0** read from bytes (4 635 B). Source-available, **not** open source. The API says `NOASSERTION`, which is why it keeps reappearing on candidate lists |
| [`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank) (360★ *(🟢 `p512`, API)*) | 🔴 **AGPL-3.0** (34 523 B). It is the only **OCR-capable item bank** on these shelves and it cannot be a component. 🟡 Viable only if the client hosts it themselves as a separate service and accepts §13 |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) (211★ *(🟢 `p512`, API)*) | 🔴 **AGPL-3.0** (34 514 B). A whole platform rather than a component; use as a reference for the Ollama-local posture, not as code |
| **The Learning Commons corpora** — annotated CLEAR and PERSUADE 2.0 | 🔴 **CC BY-NC-SA 4.0 — non-commercial.** The MIT code is in; the shipped corpora are out. 🟢 **The substitution is the client's own rubrics**, which is better pedagogy anyway and avoids a US-anchored reading-level corpus in a non-US deployment |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) datasets | 🟡 **Code MIT; data licensed per dataset** — Open / Open + Gated / Gated. *"Attribution travels with the data, not with Learning Commons."* Usable, but every dataset is its own procurement question |

### Shape of the engagement

| phase | weeks | what lands |
|---|---|---|
| 1 — licence + materials audit | **1** | Every component's grant read **from bytes at a pinned SHA** (not from a badge), plus the client's own content rights. 🔵 This is the week that prevents the rebuild |
| 2 — ingestion + provenance | 2–3 | Component 1 against real client material; span IDs stable and addressable |
| 3 — rubrics + QA loop | 2 | Component 4 with the **client's** rubrics; regeneration threshold tuned with teachers in the room |
| 4 — route + scheduler | 2 | Components 2 and 3; scheduler policy declared as configuration, not prompt text |
| 5 — record layer + review surface | 2 | Component 5 per `P502-1`: actor = the human, one Statement per decision |
| 6 — pilot | 2 | One cohort, teacher-in-the-loop, with the conformance/evidence artefact produced |
| **total** | **11–12** | |

### Licence posture

🟢 **MIT + Apache-2.0 on the entire critical path**, with one named exclusion (the NC corpora) that
is enforced by *not shipping them*, not by a policy document. 🔵 Nothing here forks an LMS, so
Moodle (GPL-3.0), Canvas or Open edX (AGPL-3.0) can sit alongside it without infecting the
deliverable — integrate over LTI/xAPI exactly as `P502-1` does.
🔴 **Three of the six components are young** (created within 180 days, single-maintainer). Budget
fork-and-own for components 1, 2 and 6 from day one, as `P502-1` budgets it for `learnmcp-xapi` and
`warren`. MIT permits it; the proposal should say it out loud.

### Regional fit

| region | fit | note |
|---|---|---|
| **APAC** | 🟢 **strongest supply fit** | Components 1 and 2 are Chinese-language artefacts with bilingual material in component 1. 🔴 Localisation of component 2's UI is real work, not a config flag |
| **North America** | 🟢 strong | Component 5 is what a district points at when its 2026 AI policy asks how AI use is supervised (Ohio's 1 July 2026 mandate; Oklahoma S.B. 1734's human-decision requirement) |
| **EMEA** | 🟢 strong | The span-ID provenance join is a direct input to Annex III human-oversight and transparency documentation ahead of the **2 December 2027** obligations |
| **LATAM** | 🟡 viable, build-heavy | 🔴 **No LATAM-origin component exists on these shelves**, and HolonIQ's 2026 reading says the buyer is the teacher's workflow — so weight phase 3 (rubrics, teacher-facing QA) and localise components 1–2 to pt-BR/es |

### 🔴 What this pattern does **not** do

- It does not supply an **item bank**. The only OCR-capable one found is AGPL-3.0, and that is a
  measured absence on the permissive shelf, not an oversight.
- It does not make the companion correct — component 4 scores against rubrics, and rubrics encode
  the client's judgement, not truth.
- 🔴 It assumes a hosted LLM. **None of components 1, 2 or 3 declares a model boundary**, so a
  data-residency clause forces a local-inference adaptation (the `freelingo` posture) that this
  recipe does not include and that is not a week's work.

## 🆕 `p504` — `2026-10-28` — one pattern: the artefact the best-evidenced region on these shelves is actually missing, which is a **policy**, not a product

🟢 Every recipe in this file so far builds something a student or teacher *uses*. The strongest
regional finding this base holds says the gap is elsewhere: in LATAM, **92 % of students and 79 % of
faculty already use AI** (Digital Education Council, 30,000+ respondents) while **only ~25 % of
institutions have a formal framework** and **~30 % have published an AI-use policy** (UNESCO IESALC,
200 institutions / 19 countries). 🔴 **Those universities do not need another tutor. They need a
policy they can publish, enforce and audit** — and that is a buildable deliverable, not a document
exercise. `P504-1` is that build.

## 🆕 `P504-1` — **The AI-use policy as an executable artefact: a published profile, enforced in code, auditable per statement** 🟢

**Why:** a published AI-use policy is normally a PDF nobody can check. The move in this pattern is
to express the policy as a **machine-readable xAPI Profile** and then validate every recorded
interaction against it. That turns three things a governance committee currently asserts into things
it can *demonstrate*: what AI use is permitted, that recorded use conformed, and what happened when
it did not. 🟢 Every component below is a row this base has read from bytes, and the licence traps
are designed out explicitly rather than discovered at contract.

| Component | Repo | Licence | ★ | Role |
|---|---|---|---|---|
| Policy schema | [`yetanalytics/project-persephone`](https://github.com/yetanalytics/project-persephone) | 🟢 **Apache-2.0** | **8** | **The keystone.** Validates xAPI Statements against a **Profile** — i.e. against the published policy |
| Audit record | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | **144** | SQL-backed LRS (Clojure, SQLite/Postgres); the permissive LRS to build on |
| Ingestion / analytics | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟡 **MIT** *(carried `p467`, not re-read from bytes)* | **51** | LRS + ingestion CLI; 🇫🇷 France Université Numérique |
| Rubric grading | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟡 **MIT code + CC BY 4.0 prompts** | **87** | Grades AI output against research-backed rubrics. 🔴 **See the licence fence below — do NOT ship its corpora** |
| Pre-deployment gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT**, 1 064 B | **13** | 1,143 teacher-exam items (920 CDPK / 223 SEND) |
| Eval runtime | [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT** | **14,341** *(🟢 `p512`, API)* | the harness the benchmark runs on |
| Agent loop | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | **30,123** *(🟢 `p512`, API)* | minimal code-writing agent; emits the statements |
| Academic integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** | **355** | plagiarism detection, 3,865 commits, Ghent University |
| Institutional layer *(if the client has none)* | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | **448** | enrolment, roles, gradebook — served off `master` |
| Integration target 🇧🇷 *(do not fork)* | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** | **720** | the municipal SIS a Brazilian public engagement lands on; branch **`2.12`** |

### Wiring — the policy becomes a schema, then a gate, then evidence

1. **Write the institution's AI-use policy as an xAPI Profile**, not prose. Each permitted use
   becomes a statement template: who may do what, to which object, with which result. This is the
   step that makes everything after it mechanical.
2. **Stand up `lrsql`** as the record. Postgres for an institution, SQLite for a pilot.
3. **Put `project-persephone` in front of the LRS** and validate every statement against the
   Profile from step 1. 🟢 **A statement that the policy does not describe is rejected at write
   time** — so "we complied" stops being a claim and becomes a property of the store.
4. **Run the agent on `smolagents`**, emitting one xAPI statement per interaction. The agent does
   not write logs; it writes to the record that the policy validates.
5. **Gate the model before deployment** with `pedagogy-benchmark` on `lm-evaluation-harness`, and
   gate its *outputs* continuously with `evaluators`' rubrics.
6. **Report to the governance committee from `ralph`** — adoption by faculty and department,
   rejected-statement counts, rubric scores over time. This is the artefact that closes the
   ~70 % no-published-policy gap, because it shows the policy operating.
7. **Add `dolos`** where the policy makes claims about student submissions, so the integrity rule is
   enforced by the same stack that publishes it.

### 🔴 The two licence fences in this recipe, both found this pass

- 🔴 **`evaluators` is NOT cleanly permissive, and `NOASSERTION` hid it.** Byte-read at
  `b9d47891c1b8` (`LICENSE.md`, 1 615 B, blob `86eebd7ebc43`): **code MIT**, **prompts and settings
  CC BY 4.0**, but the **Annotated CLEAR Corpus and Annotated PERSUADE 2.0 Corpus are
  CC BY-NC-SA 4.0** — **non-commercial and ShareAlike**. 🟢 **Use the code and the prompts, with
  attribution; bring the client's own corpus.** Shipping either annotated corpus in a paid
  engagement is a breach, and nothing on the repo's GitHub sidebar tells you so.
- 🔴 **Do not reach for `learning-commons-org/knowledge-graph`** (164★) to seed the rubrics without a
  per-dataset review. Its data is **Open / Open+Gated / Gated per download**, Gated content needs
  provider approval and is not redistributable, a compiled build inherits **every** included
  dataset's obligations, and the terms can change between releases. 🔴 **There is no repo-level
  answer to "can we use it".** See [`noassertion-bytes.2026-10-28-p504.tsv`](../evidence/noassertion-bytes.2026-10-28-p504.tsv).
- 🔴 **`i-educar` is GPL-2.0.** Integrate across a process boundary — API, xAPI statements, its
  database — and do not fork it into a closed deliverable.

### 🔵 Honest limits of this recipe

- 🔴 **`project-persephone` is 8★ with 1 fork.** It is the keystone and it is the smallest component
  here. Read it before committing: it is small enough to audit in an afternoon and small enough to
  be abandoned. Budget for owning a fork.
- 🔴 **`ralph`'s MIT grant is carried from `p467`, not re-read from bytes this pass.** Verify before
  contract; `lrsql` alone can carry the pattern if it fails.
- 🔴 **Writing a correct xAPI Profile is the hard part of this build**, and it is consulting work,
  not integration work. A wrong Profile produces a store that validates the wrong thing confidently.
- 🔵 **No component here is LATAM-origin** except the integration target. The pattern is placed in
  LATAM by the *demand* evidence, not by supply provenance — the permissive pieces are North American
  and European, which is itself the regional finding (`market.md` `p504`).
- 🔴 **Do not substitute [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework)**
  for the classroom-response layer if this pattern is extended that way: it reads **`archived: true`**
  as of `p504` and is frozen upstream (`T29`).

---

## 🆕 `p505` — `2026-10-28` — one pattern: the **dated** version of a pattern this file already had, because the clock is what makes it sellable

🔵 `P490-5` is this file's US-patchwork pattern and it is correct, but it is **undated** — it lists
Maryland `S.B. 720` as one policy toggle among six. 🟢 `p505` promoted the instrument's **operative
clock** onto [`intel/market.md`](../intel/market.md): **24 districts, 120 days** from state guidance
to an aligned district AI policy. 🔵 **A 120-day statutory clock across 24 named buyers is a
different commercial object from a policy toggle**, and it deserves its own recipe. Nothing in the
stack below is new or unverified — the novelty is the **sequencing**, which the clock dictates.

## 🆕 `P505-1` — **Maryland 120-day district conformance kit: one configuration, 24 buyers** 🟢 *(dates and sequences `P490-5`; does not supersede it)*

**Why this one:** the clock is **statutory, public, and shared by 24 districts simultaneously**. That
is the rarest shape in US K-12 AI procurement — every other state mandate on these shelves is either
undated (`S.B. 1227`), set years out (Oklahoma `S.B. 1734`, before the **2027–28** school year), or
district-discretionary. 🔴 **Do not sell 24 builds.** Sell **one configuration plus 24 policy
records**, which is exactly what `P490-5`'s tenancy model already supports.

### The stack — every row MIT, every row already verified on these shelves

| Component | Repo | License | Role in *this* pattern |
|---|---|---|---|
| Multi-tenant LMS base | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **One deployment, 24 tenants.** Postgres row-level security makes a district a tenant and its policy record non-leaking — enforced in the database, not application code |
| Policy artefact | `P504-1`'s executable AI-use profile | 🟢 — | The district's adopted policy as a **published, enforceable, per-statement-auditable** artefact — which is what the Act actually requires a district to *have* |
| Content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** | Lesson plans and assessments. 🔵 **387★** (`p490` read; the `~12,000★` figure this base carried for ~500 passes was a stale carry) |
| Mastery model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | BKT, **explainable** — the human-oversight gate needs a reason it can show |
| Canvas bridge | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | Only where the district runs Canvas; harden per `P495-1` before deploying it |

🟢 **All five permissive** — a hosted closed derivative is clean, which this must be, because the
commercial model is one SaaS tenant per district.

### Wiring — sequenced to the clock, which is the whole point

1. **Before guidance lands (now):** build the tenancy and the **policy-record schema**, not the
   policy. The 120 days start at *state guidance*, so the schema is the only thing that can be built
   early — and it is the long pole.
2. **Day 0–15:** ingest the state guidance into `P504-1`'s profile form, once, centrally. One
   reading, 24 consumers.
3. **Day 15–60:** per-district deltas only. Grade band restrictions, parent opt-out, approved-tool
   lists — each a **record**, never a fork.
4. **Day 60–100:** the human-oversight gate on anything high-stakes. 🔴 **Calibrate it per `P496-1`'s
   warning** — an uncalibrated compliance gate reproduces the bug it was built to prevent.
5. **Day 100–120:** produce the **audit artefact** per district: which statement of the adopted
   policy is enforced by which code path. This is the deliverable a board signs, not the chatbot.

### 🔴 Do this or it is negligent

- 🔴 **Read the enrolled text before citing the Act's requirements.** This base's own Maryland row
  carries an explicit unresolved flag — *"read the enrolled text before citing either"* — on the
  question of what `S.B. 720` mandates (state guidance + statewide collaborative vs. every local
  system designating an AI coordinator). 🔴 **The 24 / 120 figures are secondary-sourced**, like
  everything in this base's EU date work, and the clock is the pattern's premise. **Verify both at
  the Maryland General Assembly before quoting them to a buyer.**
- 🔴 **There is no federal law to plan around.** `H.R. 8747` advanced in committee only.
- 🔴 **Do not reuse this recipe in the EU.** It has no Annex III conformity work and no Article 50
  marking — and the EU's own near date is **2 Dec 2026**, five weeks out, not 2027. Use `P490-2`.

### 🟡 Honest limits

- 🟡 **The clock may already have started or may not start for a year** — it is keyed to state
  guidance whose date this pass did **not** verify. A buyer conversation must open by establishing
  where in the 120 days they are; the pattern is worthless if that is unknown.
- 🟡 **24 districts is a ceiling, not a pipeline.** Maryland's districts procure independently.
- 🔵 **No component here is Maryland-origin or even US-education-origin.** The pattern is placed in
  North America by the *instrument*, not by supply provenance — the same observation `P504-1` made
  about LATAM.

## 🆕 `P506-1` — **EMEA teacher-capability engagement: prove the training worked, because the adoption argument is already over** 🟢

🔵 **The premise is `p506`'s EMEA finding, and it inverts the usual pitch.** Four independent
instruments now measure European education-AI adoption, and they agree that **uptake is not the
problem**: **39.3 %** of EU 16–24-year-olds already use generative AI for formal education
(Eurostat, 2025) and **44 %** of English teachers use it for school work at least sometimes
(DfE, *Technology in Schools 2024–25*). 🔴 **What is missing is capability and governance:**
**29.7 %** of EU teachers have had any AI professional development (TALIS 2024 via the European
Commission) and only **~one-third** of education systems teach AI in the national curriculum
(Eurydice, *Digital education at school in Europe 2026*, 22 Sep 2026).

🔴 **So do not sell adoption enablement into EMEA.** The buyer is a ministry, a regional authority
or a university that must evidence **trained teachers** and **curriculum coverage** — and the thing
they cannot currently buy is *proof the training changed practice*. That is a measurement product,
and every component below is permissive.

### The wiring

| layer | repo | licence (`p506`, read) | job in this pattern |
|---|---|---|---|
| teacher skill content | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0**, 600★ *(🟢 `p512`, API)* | the CPD payload itself — pedagogy as portable text (`T28`), so it localises per curriculum without a licence negotiation |
| delivery platform | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **Apache-2.0**, 6,950★, branch `develop` | structured "explorations" host the training as *practice*, not slides. 🔵 The second rung of the permissive tier (`p506` correction) |
| offline / low-bandwidth arm | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT**, 1,162★, branch `develop` | rural and low-connectivity authorities; same content, no hosting assumption |
| capability measurement | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT**, 13★ | scores pedagogical quality — the pre/post instrument that turns "trained" into a number |
| evidence store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0**, 144★ | xAPI Learning Record Store: every training interaction is a statement, auditable per teacher (sequences `P502-1`) |
| analytics over the LRS | [`openfun/ralph`](https://github.com/openfun/ralph) + [`openfun/warren`](https://github.com/openfun/warren) | 🟢 **MIT** / **MIT**, 51★ / 17★ | 🟢 **EMEA-origin and state-backed** — France Université Numérique. `ralph` ingests learning-record streams, `warren` dashboards them |
| integrity arm | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT**, 355★ | 🟢 **EMEA-origin** (Ghent). Academic-integrity evidence, which is the objection that kills AI training programmes politically |
| SCORM bridge | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT**, 360★ | ministries' existing LMS estates are SCORM; this is the adapter that avoids a platform migration |

### The sequence

1. **Baseline with the benchmark, before any training.** `pedagogy-benchmark` scores a sample of
   teachers' actual lesson artefacts. 🔵 This is the step that makes the engagement defensible: the
   DfE's own task split (**35 %** planning, **5 %** marking, **7 %** live lessons) shows where
   practice already is, so baseline those three separately or the post-measure is meaningless.
2. **Deploy the skills payload on `oppia` (or `kolibri` offline), bridged into the incumbent LMS via
   `scorm-again`.** Localise `k12-teacher-skills` to the national curriculum — Apache-2.0 permits
   it and the Eurydice "~one-third have AI in the curriculum" figure tells you whether you are
   authoring *to* a curriculum or *ahead of* one.
3. **Emit xAPI for every interaction into `lrsql`**, ingest with `ralph`, dashboard with `warren`.
4. **Re-run the benchmark.** The deliverable is a **signed delta per teacher cohort**, with the
   record store as the audit trail.
5. **Hand the authority the dashboard and the LRS**, not a report. 🟢 All-permissive means they can
   keep running it after the engagement closes, which is what makes this renewable.

### Why it clears EMEA's own bar

🟢 **The AI Act arm is already satisfied by construction.** Annex III education obligations bite at
**2 Dec 2027** (stand-alone) and **2 Aug 2028** (embedded) — 🔵 **quote those dates and name the
reading as secondary** (`Gap 483-K`: the primary is unreadable from this session). A pattern whose
evidence layer is an auditable record store is *already* the conformity artefact, so the training
programme and the compliance programme are one project rather than two.

### 🔴 Do this or the pattern is negligent

- 🔴 **Verify the four EMEA figures at their primaries before quoting any of them to a buyer.** All
  four are **`SEARCH-ATTESTED, PRIMARY UNREAD`** — Eurostat, the DfE report, Eurydice and the
  Commission's TALIS summary are all on hosts refused at the CONNECT in this session. **Named in
  [`emea-adoption-instruments.2026-10-28-p506.tsv`](../evidence/emea-adoption-instruments.2026-10-28-p506.tsv)
  for exactly that.**
- 🔴 **Never put two of these teacher figures in one trend line.** `T31`: the four European teacher
  numbers met this pass use four different verbs — *uses at least sometimes* (DfE 44 %), *has ever
  used* (DfE 82 %/78 %, secondary-sourced), *expects to use for one task* (Sanoma 63 %) and *used
  for their job, lower secondary only* (OECD 37 %). **They are not a time series.**
- 🔴 **`learning-commons-org/evaluators` and `knowledge-graph` are deliberately excluded here**
  despite fitting the measurement layer: both return **`NOASSERTION`** on the licence field, and
  this base's rule is that the grant is the bytes. Promote them into this pattern only after a
  payload read.
- 🟡 **`ralph` (51★) and `warren` (17★) are low-star.** They are in because they are **MIT,
  EMEA-origin and state-backed** (France Université Numérique), not because they are popular —
  expect to own operational burden, and say so in the SOW.
- 🟡 **`oppia` runs on branch `develop` and `kolibri` on `develop`.** Pin a release, not `HEAD`
  (`Gap 498-G`'s rule, still binding).

## 🆕 `P510-1` — **The vendoring attestation a platform engagement hands to the client's security review** 🟢 *(operationalises `Gap 498-G`'s "pin a release, not `HEAD`"; does not supersede `P501-2`)*

🔵 **The gap this fills.** `P501-2` produces the **licence** artefact for counsel. `Gap 498-G` says
pin a release. 🔴 **Neither is checkable by the client**, because the step both inherit —
*"verify the URL"* — was being run as `curl -sI https://github.com/<slug>`, which on this channel
answers **403 to a live repository and to one that never existed alike**
([`url-check-control.2026-10-28-p510.tsv`](../evidence/url-check-control.2026-10-28-p510.tsv)).
🟢 **This recipe replaces that step with one that can fail, and emits the result as a signed-off
deliverable.**

**Components** — each address proven `LIVE` this pass, on its resolved default ref:

| role | component | grant | ref to pin from |
|---|---|---|---|
| LMS / offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** *(🟢 `p510`, API)* | **`develop`** — not `main` |
| interactive lessons | [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** *(🟢 `p510`, API)* | **`develop`** |
| assessment / QTI | [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | GPL-2.0 **`or-later`** *(`p455`; grant re-read independently by `p510` — 18,025 B `a01259a1b522`, matching `p509`'s census to the digit)* | **`develop`** |
| SCORM runtime | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** *(`p509` byte-census, 1,072 B `383b85b370e8da44`)* | **`master`** |
| record layer | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** *(`p509` byte-census, 11,357 B `c71d239df91726fc`)* | **`main`** |
| tutoring agent | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** *(🟢 `p510`, API)* | **`main`** @ `1ea7df155447` |
| agent loop | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** *(`p509` byte-census)* | **`main`** |

🔴 **Four of the seven do not default to `main`.** A build script that clones without `-b`, or a
probe that reads `main/…`, is reading a different tree than this table — and will often get a
**200 from a stale branch** rather than an honest 404.

**Wiring — four steps, each producing a file the client keeps**

1. **Resolve, do not assume.** Run
   [`compose/code/p510-liveness-gate/`](code/p510-liveness-gate/) over the component list.
   `sweep()` calls `run_controls()` first and **raises `ControlFailure` instead of returning a
   count** if the known-good does not read `LIVE` or the known-bad does. Output: one row per
   component — state, **true default branch**, `HEAD` SHA.
2. **Pin from the resolved ref, never from `HEAD`.** Take the newest release *reachable from the ref
   step 1 resolved* (`git ls-remote --tags`, version-sorted — **not lexicographic**, per
   `Gap 505-C`). Record `owner/repo@tag` **and** the commit SHA; the SHA is what survives a retag.
3. **Read each grant from bytes on the pinned ref** — `raw.githubusercontent.com/<slug>/<ref>/<path>`
   with byte count and sha256, case-insensitively and accepting an extensionless `license`
   (`p509`'s defect #3). 🔴 **A `NOTICE` is not a grant** (Apache §4(d)); 🔴 **a detector's
   abstention is not a verdict** (`T33`) — read the payload.
4. **Gate it in the client's CI.** Re-run steps 1–3 on every dependency bump and fail the build on:
   any component not `LIVE`; a default ref that moved; a grant whose sha256 changed; or any grant
   outside MIT / Apache-2.0 / BSD-3-Clause entering a **shipped** path.

**The deliverable.** One TSV plus a one-page summary: every component, its proven-live address, its
pinned `ref@sha`, its grant with bytes and sha256, and the two control rows showing the instrument
can fail. 🟢 **The control rows are the point** — they are what makes the other rows evidence rather
than assertion.

**Caveats, stated in the SOW**

- 🟡 **Liveness is positive-only on one channel.** An absent repository and a **private** one answer
  identically over the git protocol, so `UNREADABLE` must be resolved on a second channel before any
  component is declared gone (`Gap 510-B`).
- 🔴 **`tao-core` is GPL-2.0-or-later** — combinable forward, but it is **not** permissive; keep it
  behind a service boundary if the engagement ships proprietary code, per `P503-1`'s discipline.
- 🟡 **Licence payloads are branch-stable on this population** (7 of 7 identical across stale and
  true refs, [`stale-branch-byte-compare.2026-10-28-p510.tsv`](../evidence/stale-branch-byte-compare.2026-10-28-p510.tsv)),
  **but versioned content is not** — which is exactly what vendoring reads. Resolve the ref for
  code, not for the licence cell.
- 🔴 **Not gate-attested.** `make hooks` has been DENIED (`Code from External`) for sixteen of the
  last seventeen passes, so this recipe's own CI step is the only gate it can promise.
