---
industry: education
region: Global
updated: 2026-10-18
---

## 🟢 Pass 300 — three new patterns (`P66`-`P68`), each built from rows promoted THIS pass, and every component licence PAYLOAD-verified

⏱️ `2026-10-18`. Evidence:
[`p300-promotion-gap.2026-10-18-p300.tsv`](../evidence/p300-promotion-gap.2026-10-18-p300.tsv) ·
[`p300-payload-grade.2026-10-18-p300.tsv`](../evidence/p300-payload-grade.2026-10-18-p300.tsv).

🔴 **Numbered `P66`-`P68`: `P63`-`P65` are taken by `p299`, `P60`-`P62` by `p298`, `P56`-`P59` by
`p297`** — the shelf was enumerated before numbering, because a duplicate pattern ID compiles into
two entities with one name.

🟢 **Every component named below carries a sha256-pinned licence payload.** `p299` could offer five
payload reads of fifteen and flagged the rest; 🟢 **`p300` read 20 of 20**, so for the first time a
pattern on this file can be quoted with **no sidebar-grade dependency in it.**

## P66 — Credentials the institution owns, on a copyleft LMS it does not fork (global; EU variant noted)

**The engagement.** A university or ministry issues certificates through a hosted vendor. The
credential — the thing the learner carries for forty years — lives in that vendor's database, and
leaving means re-issuing everything. The LMS is Moodle (GPL-3.0), Canvas (AGPL-3.0) or Open edX
(AGPL), so forking is off the table.

**The build — all permissive, all payload-read `2026-10-18`:**

| step | component | licence (pinned) |
|---|---|---|
| 1. reach the LMS **without forking it** | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) · [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) · [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | Apache-2.0 / Apache-2.0 / MIT *(`p298`)* |
| 2. **issue and revoke** | [`digitalcredentials/issuer-coordinator`](https://github.com/digitalcredentials/issuer-coordinator) | 🟢 MIT · 1 087 B · `ca28a7ae5c7e` |
| 3. **sign** over W3C VC | [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) | 🟡 BSD-3-Clause · 1 525 B · `4f0d287e80be` *(holder Digital Bazaar; a declared fork — read the row)* |
| 4. put it in the **learner's hands** | [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 MIT · 1 092 B · `1032f65dd2f6` |
| 5. let **anyone verify** | [`digitalcredentials/verifier-core`](https://github.com/digitalcredentials/verifier-core) *(engine)* + [`verifier-plus`](https://github.com/digitalcredentials/verifier-plus) *(app)* | 🟢 MIT · `6e7a616c4d70` / `85569d7ed8fc` |
| 6. **prove conformance** before go-live | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 Apache-2.0 · 11 357 B · `c71d239df917` |
| 7. **CI gate** on every issued batch | [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) — `credlens`, JSON output, offline | 🟢 MIT · 1 080 B · `f65f32330671` |

🇪🇺 **EU variant:** insert [`impierce/credential-converter`](https://github.com/impierce/credential-converter)
(Apache-2.0, Rust, `efd09e39cb61`) between steps 3 and 4 to emit **ELM** for Europass alongside OBv3,
with [`impierce/digital-credential-data-models`](https://github.com/impierce/digital-credential-data-models)
(Apache-2.0, **branch `dev`**) as the typed model. For skills vocabulary, bind to **ESCO** using
[`BeBadges/escobadges`](https://github.com/BeBadges/escobadges) (MIT) as the worked reference —
🔴 **18 commits: read it, do not depend on it.**

⚠️ **Boundaries that belong in the proposal, not in discovery:** `verifier-plus` supports **VC v1/v2
and OBv3 but NOT OBv2**, so a client on OBv2 needs the converter from day one; `credential-lens` is
**3 commits** and validates **structure only** — *no signature verification, no status-list fetch, no
DID resolution*; and the chain is **standards-conformant, not accredited** — OBv3 conformance is not
a statement about what a registrar will legally accept.

🔴 **What NOT to use, and it is the cheapest finding in this pattern:**
[`issuebadge/mcp-server`](https://github.com/issuebadge/mcp-server) is MIT and looks like a shortcut
through steps 2-4. **Its certificates are minted by a hosted commercial issuer behind an
`ISSUEBADGE_API_KEY`** — it reproduces the exact lock-in the engagement exists to remove.

**Sequencing, 10-12 weeks.** Weeks 1-2: LTI launch against the client's own LMS instance. 3-5: issuer
and signing, **revocation included** *(the half vendors skip and registrars ask about)*. 6-8: wallet
and verification page. 9-10: validator in CI, conformance evidence pack. 11-12: migration of existing
credentials, with the converter if the source is OBv2 or ELM.

## P67 — An agent that drafts credentials and cannot invent one (global; runs air-gapped)

**The engagement.** Writing credential metadata — title, criteria, skills, description — for hundreds
of courses is the work that stalls a credentialing programme after procurement. An LLM is the obvious
tool and the obvious risk: free-text output nobody can validate, on a hosted model the institution
may not send student or curriculum data to.

**The build.** 🟢 **The agent and its validator are both permissive and both read this pass:**

1. **Draft** with [`oneorigin-2-0/dcc-credential-co-writer-monorep`](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep)
   — 🟢 **MIT**, 1 087 B, `7f62d1bf385d`, holder **DCC**, 440 commits: a Next.js 15 UI, a
   **FastAPI + Ollama** service running a **fine-tuned `phi-4-mini`**, and a Pillow badge renderer.
   **23 languages**, streaming, **human-in-the-loop editor.**
2. 🔵 **Pin it on-premises.** The model is served by **Ollama** — no egress, no student or curriculum
   data leaving the institution. **That is what makes this sellable to a ministry**, and why the row
   sits on [`agents/top.md`](../agents/top.md) at 0 stars.
3. **Constrain the output to a standard, not to a prompt.** It emits **OBv3**, so `credential-lens`
   (MIT, offline) gates structure in CI and `1EdTech/digital-credentials-public-validator`
   (Apache-2.0) proves conformance. 🟢 **An agent whose output is checkable by an instrument the same
   engagement already owns is a different proposition from an agent that emits prose.**
4. **Align skills to a controlled vocabulary:** **CASE** via
   [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) (Apache-2.0, `ccf5a4564e72`) so
   *"curriculum-aligned"* becomes machine-checkable — or **ESCO** in the EU.
5. **Record the drafting events** as xAPI (see `P68`) so the human-in-the-loop edits are auditable.

⚠️ **State this boundary first, in writing: 0 stars, 1 fork — nobody has adopted it**; its three
services were standalone repositories until recently and those predecessors are **unread**; and the
page nowhere claims an official DCC release. 🔵 **Quote it as the strongest available reference
implementation and budget for reading its code, not for depending on it.**

**6-8 weeks** on top of `P66`: 1-2 stand up Ollama and the SLM service on client hardware; 3-4 wire
the authoring UI to the course catalogue; 5-6 CASE/ESCO binding; 7-8 the CI validation gate and the
human-review workflow.

## P68 — Move the learning-record estate to xAPI 2.0 without a migration project

**The engagement.** A client has a Learning Record Store and wants *"standards-shaped analytics."*
🔴 **Two traps this base has now measured, both of which a studio walks into by default:**

| trap | what was measured |
|---|---|
| 🔴 **Caliper is not an option** | `p299`: **all five** reference client libraries `404`; the standards body took the upstream private; the only permissive remnant is a **20-commit playground** |
| 🔴 **xAPI's headline repository is the OLD version** | `p300`: [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) — **955★ / 402 forks** — says in its own README that it holds **1.0.3**, that the current version is **xAPI 2.0**, that the spec moved to **IEEE**, and that *"the next version has not been planned"* |

**The build.** 🟢 **One row on this base implements 2.0, and it was promoted this pass:**

1. **Run** [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) — 🟢 Apache-2.0, 11 357 B,
   `c71d239df917`; **xAPI 1.0.3 AND 2.0**; Hono with **PostgreSQL or PGlite** (embedded, so the same
   build runs offline on a laptop and in a datacentre); statement validation, attachments, **SSE**
   streaming, JWT/Basic auth, admin UI, OpenTelemetry.
2. 🟢 **Migrate without a migration.** It **takes over an existing
   [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) database in place** — so a client on
   this base's `p298`/`p299` 1.0.3 stack reaches 2.0 **without a data-migration workstream**, which
   is normally the line item that kills the project.
3. **Prove the claim instead of repeating it** with
   [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) — MIT,
   78★, 1 039 commits, from **ADL, who author the spec**. ⚠️ **Its own README: basic auth only, and
   never run it against a production endpoint** — stand up a conformance instance.
4. **Shape the statements** with [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles)
   (Apache-2.0) and filter or forward with
   [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) (Apache-2.0), which filters by
   Profile templates.
5. **In PHP estates** (Moodle, Tsugi) reach the boundary in-runtime with
   [`php-xapi/client`](https://github.com/php-xapi/client) + [`php-xapi/model`](https://github.com/php-xapi/model)
   (MIT) — 🔴 **and cite the branch**, since neither exposes a default branch on its page.
6. **For a Laravel application** needing `cmi5`, [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS)
   (MIT) serves `/api/cmi5/**` — 🔴 **pinned to 1.0.3**, so pair it with `xapi-lrs` where 2.0 is
   required.

🔵 **The sentence for the proposal:** *"your analytics layer will emit xAPI 2.0, verified by the
specification author's own conformance suite, on an Apache-2.0 store that can adopt your existing LRS
database in place."* 🔴 **Never write "Caliper-compatible", and never cite `xAPI-Spec`'s star count
as evidence of currency.**

**4-6 weeks:** 1-2 stand up `xapi-lrs` beside the existing store; 3 take over the `lrsql` database in
a staging copy and diff; 4 conformance suite green; 5-6 profiles, forwarding, and the dashboards the
client actually asked for.


## 🟢 Pass 299 — three new patterns (`P63`-`P65`), each built from rows promoted THIS pass

⏱️ `2026-10-18`. Evidence:
[`p299-promotion-gap.2026-10-18-p299.tsv`](../evidence/p299-promotion-gap.2026-10-18-p299.tsv) ·
[`p299-caliper-layer.2026-10-18-p299.tsv`](../evidence/p299-caliper-layer.2026-10-18-p299.tsv).
🔴 **Numbered `P63`-`P65`: `P60`-`P62` are taken by `p298`, `P56`-`P59` by `p297`, `P52`-`P55` by
`p296` and `P51` by `p294`** — the shelf was enumerated before numbering, because a duplicate pattern
ID compiles into two entities with one name.

🔵 **All three are built on the fifteen substrates promoted this pass.** `p298` armed the integration
boundary at **launch** (LTI) and at **item playback**; `p299` arms it at **authoring, conversion,
delivery and measurement** — so for the first time an assessment engagement can be quoted end to end
without a copyleft dependency. 🟢 **Five of this pass's licence reads are PAYLOAD-grade**
(`raccoongang/edx_xblock_scorm` → Apache-2.0, `OpenOLAT/qtiworks` → BSD-3-Clause,
`1EdTech/caliper-js-example` → LGPL-3.0, `1EdTech/caliper-spec` → no file, plus the control reads),
which is a higher grade than `p297`-`p298` could offer. ⚠️ **The remaining ten are sidebar-grade — see
the caveat at the end.**

## P63 — An assessment migration off a vendor LMS, permissive end to end (global, runtime-agnostic)

**Who it is for.** Any engagement that must get **assessment content out of Canvas / Blackboard /
Moodle** and into something the client owns — a migration, a consolidation after a merger, or an exit
from a per-seat licence. 🔵 **This pattern exists because `p298` could only offer playback and
packaging; the steps a real migration actually starts and ends with were missing from these shelves
until this pass.**

**The wiring, in the order the work happens:**

1. **Get the items out of the incumbent.** [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert)
   (**Apache-2.0**, 22★, 42 commits, Python) converts a **Canvas QTI export package** to **JSON** or
   **Word (.docx)**. 🟢 **This is the only row in this base that reads a vendor's export format** —
   and an export package is what the client will hand you on day one.
2. **Normalise and re-package.** [`examplary/qti`](https://github.com/examplary/qti) (**MIT**,
   TypeScript) builds *and* parses **QTI 3.0 and 2.1** packages, manifests, items, tests and stimuli,
   with automatic version detection. For PHP estates use
   [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) (**MIT**, shelved `p298`).
   🔴 **Cite `examplary/qti` by owner: [`instructure/qti`](https://github.com/instructure/qti) is a
   different thing entirely** — a Ruby gem that *parses* QTI **1.2 / 2.1**. Use that one when the
   legacy corpus predates QTI 3, which on a migration it usually does.
3. **Author the new items in a format humans will maintain.**
   [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) (**MIT**, TypeScript
   CLI, npm) turns **Markdown + a manifest** — ordering, IDs, points — into QTI 3.0. 🟢 **This is what
   makes an LLM a usable item author: generate Markdown, not XML**, then compile it deterministically.
4. **Let a human see it before it ships.** [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground)
   (**MIT**) gives a split-pane editor with live QTI 3.0 preview — the review step for step 3.
5. **Deliver it.** Choose by stakes, and this is the decision that matters:
   - 🟢 **Exam-shaped, server-authoritative** → [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks)
     (**BSD-3-Clause**, **2 087 commits**, Java): QTI 2.1 delivery engine + **JQTI+** library +
     **MathAssess** extensions for mathematical assessment. 🔴 **Take this fork, not the 68★
     `davemckain/qtiworks`, which announces its own closure in its description.**
   - 🟡 **Browser-side, low-stakes practice** →
     [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (**MIT**, shelved
     `p298`), with [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer)
     (**MIT**) for scoring/report/explanation HTML.
   - 🔴 **Do NOT use [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player)
     as a general player** — its own README says **`choice-interaction` only, no scoring, no test
     structure, partial expressions, host must supply MathJax.**
   - 🔴 **Do NOT ship [`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti) as the
     delivery engine** — its own README says pre-1.0, *"not fully conformant or certified"*, and not
     for untrusted or high-stakes delivery without a backend-authoritative integration. 🟢 **Use it for
     what it is: the QTI ↔ PIE transform (794 commits), i.e. step 2 for PIE-shaped corpora.**
6. **If the content is SCORM rather than QTI** — which on a corporate or older K-12 estate it will be:
   [`S4-NetQuest/react-scorm-provider`](https://github.com/S4-NetQuest/react-scorm-provider)
   (**MIT**, 67★) for a React front end, or
   [`raccoongang/edx_xblock_scorm`](https://github.com/raccoongang/edx_xblock_scorm)
   (**Apache-2.0**, payload-read) to run SCORM 1.2/2004 **inside Open edX**. ⚠️ **The XBlock is
   archived (2023-11-27) — read it as a pattern, vendor the code, and own the fork knowingly.** Its
   **65 forks against 32 stars** say the rest of the market made the same decision.
7. **Measure the result, and make the measurement provable** — `P64`.

**Why it wins.** 🟢 **Every step is MIT / Apache-2.0 / BSD-3-Clause, and the two steps that look
cheapest to hand-roll (export parsing and item authoring) are the two that are shelved.** 🔵 **And
three of the six components carry a disqualifying limit in their own README** — a pitch that names
those limits before the client's own engineer finds them is the differentiator, not the component list.

**Rough shape.** 6-9 weeks for a single-course pilot through step 5; the corpus size drives step 1-2,
the stakes drive step 5.

## P64 — Prove the learning-record trail instead of asserting it, permissively (global — and the ONLY standards-shaped option after this pass)

**Who it is for.** Any engagement where an AI system touches a student outcome and someone will later
ask *what happened* — the North America governance gap (**~10% of institutions have formal AI
guidelines**), the LATAM one (**92% of students engaged, ~30% of institutions with a published
policy**), or any regulator-facing deployment.

**The wiring:**

1. 🔴 **Choose xAPI, not Caliper, and this is now a finding rather than a preference.** All five
   Caliper reference client libraries return **`404`**; 1EdTech made the upstream **private**; the only
   permissive remnant is a **20-commit playground** whose README says its auth flow *"must not be used
   in production"*; the spec repository's own grant reads **`Other`** with **no `LICENSE` file at
   `master`**. See [`p299-caliper-layer.2026-10-18-p299.tsv`](../evidence/p299-caliper-layer.2026-10-18-p299.tsv).
2. **Fix the vocabulary first.** [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles)
   (**Apache-2.0**, 60★) — the Profiles specification from **ADL**, who author xAPI itself. 🟢 **Write
   the profile before the first statement**, or you will be migrating verbs in month four.
3. **Store the statements, in the runtime you already have:**
   - **JVM / standalone** → [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (**Apache-2.0**).
   - **PHP / Laravel** → [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) (**MIT**) — 🟢 **the only
     `cmi5` row in this base**, serving `/api/cmi5/**` at `x-experience-api-version: 1.0.3`. Use this
     when the estate is Moodle-adjacent and standing up a JVM service is the thing that kills the
     pilot.
   - **Emit from PHP** → [`php-xapi/client`](https://github.com/php-xapi/client) +
     [`php-xapi/model`](https://github.com/php-xapi/model) (**MIT**). 🔴 **Pin the branch you read —
     neither repo exposes a default branch on its page** (`0.7` and `3.x` respectively).
4. 🟢 **Now the step that makes this a pattern rather than a stack:**
   [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (**MIT**, 78★, **1 039 commits**) tests the **`MUST` requirements of the xAPI spec** against your
   endpoint. ⚠️ **Its own README: basic auth only, and never run it against a production LRS** — so run
   it in CI against staging, and **ship the output as the deliverable.**
5. **Move only what the downstream is entitled to.**
   [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) (**Apache-2.0**, shelved `p298`)
   forwards statements **filtered by Profile templates and patterns**, resumably. 🔵 **This is the
   data-minimisation control in code** — the thing a privacy reviewer asks for and usually receives as
   a paragraph.

**Why it wins.** 🟢 **"Our audit trail is standards-conformant" stops being a claim and becomes a test
report, produced by the spec's own authors' suite, in CI.** 🔴 **And it inverts the Caliper problem into
a selling point:** the studio arrives knowing that the competitor's "Caliper-ready" slide is backed by
LGPL/GPL code or by libraries that no longer exist publicly.

**Rough shape.** 3-5 weeks to a conformance report on a staging LRS; step 2 is the long pole and it is
a workshop, not an engineering task.

## P65 — Capability, not rooms: converting a national hardware rollout into measured learning (🇵🇱 Poland first · 🇵🇰 Pakistan variant · transferable to any state lab programme)

**Who it is for.** A ministry or regional authority that has **already bought the hardware** and now
owns the gap between *installed* and *used*. 🟢 **Poland is the live instance:** ~**1.9 bn złoty** for
AI labs in **~12 000 schools** (~8 000 primary + ~4 000 secondary), inside a **> 5 bn złoty** digital
programme, **~EUR 500M mostly EU funds** — against an **IBE PIB 2025 baseline of 1% of schools with an
AI lab and 27% with no Wi-Fi**, and a corpus that notes **teacher-training and data-privacy guidance
were still missing in 2025/26**.

**The wiring:**

1. **Do not touch the ministry's stack.** Reach it at the **LTI 1.3 boundary** per `P60`, in the
   studio's own runtime. 🔵 **A hardware programme is procured by one directorate and the curriculum by
   another; a tool that requires an LMS migration dies between them.**
2. **Attack the teacher-time constraint, because that is what "unused lab" actually means.**
   [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents)
   (**Apache-2.0**, EACL 2026) generates syllabus → slides → assessments under an **ADDIE** multi-agent
   loop with a **Full Co-Pilot** mode. 🟢 **Run it in co-pilot mode, never autonomously, in a
   programme whose own documents admit teacher training is missing.**
3. **Make the output land in the national assessment format, not in a PDF.** `P63` steps 3-5:
   Markdown → **QTI 3.0** ([`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti)),
   reviewed in [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground), delivered by
   [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) (**BSD-3-Clause**) if it is graded.
4. **Instrument it from day one** — `P64`. 🔴 **A state programme measured only by labs installed cannot
   be renewed on evidence.** An xAPI profile plus a conformance report is the renewal argument.
5. **Attach the governance artefact before the first classroom**, as `p298` concluded for Morocco: an
   AI-use policy, a human-decision boundary, and an audit trail. 🟢 **In the EU this is also the AI Act
   answer**, and the corpus says the ministry has not written it yet.

**🇵🇰 The Pakistan variant — same pattern, inverted constraint.** Pakistan's **National AI Policy
(July 2025)** plus **up to USD 1 bn by 2030**, **1 000 AI PhD scholarships** and
**Train-the-Trainer for 10 000 educators by 2027** sit against an **IT ministry diagnosis (Oct 2026)**
naming **rural connectivity, instructor supply, training facilities and awareness** as what blocks it.
🔴 **So steps 2-4 must run offline-first** — `P62`'s shape — with **WhatsApp-class delivery**, for which
[`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform) (**Apache-2.0**,
Taleemabad, national curriculum, 15 languages) is the shelved reference. 🔴 **And qualify the
counterparty first, per `p298`'s Mozambique/Angola finding: the AI money sits with the IT ministry and
the curriculum mandate sits with education.**

**Why it wins.** 🔵 **Both countries have published the gap themselves** — Poland in a 1%-baseline
study and a missing-guidance note, Pakistan in a ministry statement of why its training "isn't
working." 🟢 **A proposal that quotes the client's own diagnosis back to them, with permissive
components named per step, is a different document from a capability deck.**

**Rough shape.** 10-14 weeks for a regional pilot (one voivodeship / one province) through step 5;
**verify the Poland rollout status with the Ministry of Education before quoting the 12 000 figure** —
this base has recorded the announcement, not the delivery.

### ⚠️ Grade caveat for `P63`-`P65`

🟢 **Five of `p299`'s licence reads are payload-grade** — `raccoongang/edx_xblock_scorm`
(`Apache-2.0`, 11.1 KB), `OpenOLAT/qtiworks` (`BSD-3-Clause`, `LICENSE.txt`, 2.01 KB),
`1EdTech/caliper-js-example` (`LGPL-3.0`, 7.43 KB), `1EdTech/caliper-spec` (**no file — `404`**) and
the `404` control set. 🔴 **The other ten admissions are SIDEBAR-grade: GitHub's label, not the
file.** `p298` proved that label is not a property of the payload, and `p299` found **four distinct
causes** for a bare sidebar pointing at **opposite** decisions (`T-p299d`).

🔴 **Before any of these patterns ships to a client, read the `LICENSE` file of every component you
actually ship, and check `LICENSE.txt` as well as `LICENSE`** — `OpenOLAT/qtiworks` would have been
graded unlicensed by a `LICENSE`-only scanner, and it is BSD-3-Clause. ⚠️ **Also re-read the three
README-stated limits named in `P63`** (`pie-qti` not exam-grade, `qti-3-player` single-interaction,
`edx_xblock_scorm` archived) **and the two in `P64`** (conformance suite not for production, `php-xapi`
branches unpinned) **at the version you pin** — this base records them as read on `2026-10-18`.


## 🟢 Pass 298 — three new patterns (`P60`-`P62`), each built from rows promoted THIS pass

⏱️ `2026-10-18`. Evidence:
[`p298-promotion-gap.2026-10-18-p298.tsv`](../evidence/p298-promotion-gap.2026-10-18-p298.tsv).
🔴 **Numbered `P60`-`P62`: `P56`-`P59` are taken by `p297`, `P52`-`P55` by `p296` and `P51` by
`p294`** — the shelf was enumerated before numbering, because a duplicate pattern ID compiles into
two entities with one name.

🔵 **All three are built on the thirteen substrates promoted this pass**, and that is deliberate:
`T-p298a` measured that this base has told clients *"integrate, do not fork"* for 297 passes while
carrying **one** integration-boundary row, in **one** language. Every component below was
licence-read on `2026-10-18` and is shelved on [`repos/foundations.md`](../repos/foundations.md) or
[`verticals/solutions.md`](../verticals/solutions.md).
⚠️ **Read the grade caveat at the end before any of these ships** — all fourteen `p298` reads are
**sidebar-grade, not payload-grade.**

## P60 — Put your own tool inside their copyleft LMS, in the language you already use (global, runtime-agnostic)

**Who it is for.** Any engagement whose incumbent estate is **Moodle** (GPL-3.0), **Canvas**
(AGPL-3.0) or **Open edX** (AGPL) and whose deliverable must stay permissive. 🔵 **This is `P60`'s
whole reason to exist: the advice existed, the implementation did not, and the studio's runtime
decided whether the advice was usable.**

**The wiring, bottom to top:**

1. **Pick the LTI 1.3 library by YOUR runtime, not by their LMS** — LTI is the contract, so all four
   reach all three platforms:
   - **Node / TypeScript** → [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**,
     373★, 575 commits). Launches, **Deep Linking**, **AGS**, **NRPS**, **Dynamic Registration**.
   - **PHP** → [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library)
     (**Apache-2.0**, 124★, **107 forks**) for the protocol, or
     [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) (**Apache-2.0**) for a whole tool
     framework.
   - **Python** → [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (**MIT**,
     138★) with its Django or Flask adapter. 🔴 **Cite this owner — `ucfopen/pylti1.3` is a 3★
     re-publication carrying this author's own copyright line.**
   - **Notebooks** → [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
     (**BSD-3-Clause**, 523 commits): the LMS launches JupyterHub directly, and `nbgrader` or
     `otter-grader` (both BSD-3) grade underneath. **The whole lane is permissive.**
2. **Agent surface, if the deliverable is conversational:** the MCP row for the platform —
   [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT) for Canvas,
   or `aryankeluskar/canvas-mcp` (ISC) **only** when Gradescope must be reached.
3. **Keep the data boundary where the licence boundary is:** write learner evidence to
   [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (**Apache-2.0**) and forward a
   filtered subset with 🆕 [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe)
   (**Apache-2.0**) — **never into the LMS database.**

🔴 **What this pattern refuses to do:** fork the LMS, patch its templates, or ship a plugin that
inherits its grant. **The AGPL network clause reaches a hosted deployment; an LTI tool launched
*from* it does not cross it.** 🟢 **And the vendor agrees: Instructure publishes
[`instructure/qti`](https://github.com/instructure/qti) under MIT while
[`canvas-lms`](https://github.com/instructure/canvas-lms) is AGPL-3.0.** Quote that in procurement.

**Effort.** 3-5 weeks for a launched, graded, rostered tool against one platform; **add ~1 week per
further platform**, not per further tenant.

## P61 — A dropout early-warning deployment with the governance artefact already attached (EMEA · 🇲🇦 Morocco first, LATAM transferable)

**Who it is for.** A ministry or academy that **already has a dropout-detection pilot and a
governance complaint about it.** 🟢 **This is not a hypothetical: `p298`'s Maghreb leg found an AI
school-support system operating in Morocco's Draâ-Tafilalet academy to identify students at risk of
dropping out, with positive results and a stated path to national extension — while a parliamentary
report finds the governance framework unclear and demands a legal one.** 🔵 **The instrument and the
objection arrived in the same leg, which is why they belong in one pattern.**

**The wiring:**

1. **The model layer, and it is already permissive:**
   [`cedanl/student-signal`](https://github.com/cedanl/student-signal) (**MIT**) — `prepare()`,
   `rank()`, `evaluate()` reporting **precision/recall at multiple invitation thresholds** on the
   **Eegdeman invitation-rule methodology**. 🟢 It deliberately does **not** choose your estimator, so
   a ministry's existing model drops in. Beside it,
   [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) (**MIT**,
   **3 015 commits**, a named deployment outcome) when the client wants a worked precedent.
2. **The data layer:** rostering via 🆕 [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster)
   (**MIT**) or 🆕 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
   (**Apache-2.0**) where an Ed-Fi ODS exists; event stream via `lrsql` + 🆕 `xapipe`.
3. 🟢 **The governance artefact — the half that wins the procurement:**
   [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) (**MIT**, 8 033
   commits) as the harness, [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (**MIT**) as the task set, and [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit)
   (**MIT**) for tamper-evident audit. 🔵 **A government-maintained harness is materially easier to
   defend to a parliament than a bespoke test script** — see `P56`, which `P61` consumes rather than
   repeats.
4. **Delivery language:** French **and** Arabic for Morocco; the same stack ships to LATAM in Spanish
   or Portuguese, where this base's standing architecture already assumes a Moodle incumbent — reach
   it with `P60`.

🔴 **Three prices to quote honestly.** (1) **A ranking that decides about a student is EU AI Act
Annex III high-risk** (`T-p296a`, due `2027-12-02`) — Morocco is not EU-bound, but a Moroccan
deployment reused in Europe is, so build to the stricter rule once. (2) **The evaluation layer is
not optional and is not free**: it is the artefact the parliamentary report is asking for.
(3) ⚠️ **Everything known about the Moroccan pilot is `ATTRIBUTED` press, not primary text** — a
ministry-site leg is the first billable hour, not an assumption.

**Effort.** 6-8 weeks to a ranked cohort with a documented eval; **the eval harness is ~2 of those
weeks and should be sold separately, because it is what survives a change of government.**

## P62 — Offline-first delivery where connectivity is the binding constraint (🇦🇴 Angola · 🇲🇿 Mozambique · transferable to any low-connectivity estate)

**Who it is for.** An estate where **the constraint is not the model, it is the network.** 🟢 **Named
domestically rather than inferred here:** FNIA 2026 co-founder **Estevão Zinga** on Angola —
*"ainda temos algumas zonas cinzentas, províncias que não têm conexão à internet"* — and Mozambique's
**UEM** naming unequal access to technology as a standing constraint.

**The wiring:**

1. **The platform decides itself:** **Kolibri** (**MIT**) — the offline-first row this base's
   platform shelf has carried throughout. 🔵 **In this pattern the licence and the architecture agree
   for once: the only offline-capable platform here is also the only permissive one.**
2. **Content exchange, so the material is not trapped in one deployment:** 🆕
   [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) (**MIT**) to build and validate
   **QTI 3 packages** server-side, 🆕 [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player)
   (**MIT**) to play them **in the browser, on the device**, and
   [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (**MIT**) for the SCORM material
   a ministry already owns. 🟢 **Items authored once, synced as packages, scored locally.**
3. **Sync, not streaming:** 🆕 [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe)
   (**Apache-2.0**) is the component that makes this work — **it resumes an interrupted job from the
   file system or Redis**, which is precisely the failure mode of a province with intermittent
   connectivity. Local `lrsql` at the school, forward when the link returns.
4. **Inference on-premises or on-device:**
   [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite)
   (**Apache-2.0**) rather than a hosted API.
5. **Language:** Portuguese plus local languages. 🔴 ⚠️ **If any of this becomes voice-led, read
   [`AI-for-Education/voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework)
   (**MIT**) first: it is the only instrument in this base that measures CHILD speech recognition**,
   which every literacy deliverable silently assumes works.

🔴 **The procurement warning that is specific to these two countries, from `T-p298c`: qualify WHICH
ministry holds the mandate.** In **Mozambique** the AI regulator is being created by the **Minister
of Planning and Development** and the schools robotics-and-AI programme is run by the **Ministry of
Communications and Digital Transformation** — **the education ministry appears nowhere in the leg.**
A deck addressed to Education may reach the wrong department. ⚠️ **Mozambique's STEMMOZ target
(~5 000 pupils, *"todas escolas públicas"*) was dated end-2025: verify delivery before citing it.**

**Effort.** 4-6 weeks for a syncing Kolibri estate with locally-scored QTI content at pilot scale;
🔴 **the cost driver is device logistics and teacher training, not software** — price those or the
engagement will be mispriced.

### ⚠️ Grade caveat for `P60`-`P62`

All fourteen `p298` reads are **`WebFetch` over rendered `github.com` HTML — sidebar/About licence
label plus README body.** That is **sidebar-grade, not payload-grade**: only
`ucfopen/pylti1.3`'s root `LICENSE` was opened at payload (1.04 KB), and it is the one row `p298`
**rejected**. 🔴 `curl` is unavailable as a channel this pass — **`curl -sI` returned the proxy's
`HTTP/1.1 200 Connection Established` for an invented hostname as readily as for a real repository,
and a full `GET` returned a `403` whose 378-byte body is byte-identical for both.** 🟢 Before any of
these patterns ships, **re-read the grant of every component at its payload and pin the commit** —
`p295` also showed rendered star counts are **not monotonic**, so treat every figure above as a
reading taken on `2026-10-18` and not as a property of the repository.

## 🟢 Pass 297 — four new patterns (`P56`-`P59`), each built from rows promoted THIS pass

⏱️ `2026-10-18`. Evidence:
[`p297-promotion-gap.2026-10-18-p297.tsv`](../evidence/p297-promotion-gap.2026-10-18-p297.tsv).
🔴 **Numbered `P56`-`P59`: `P52`-`P55` are taken by `p296` and `P51` by `p294`** — the shelf was
enumerated before numbering, because a duplicate pattern ID compiles into two entities with one name.

🔵 **All four are built on the nine substrates promoted this pass**, and that is deliberate: `T-p297b`
measured that this base had **42 agent rows** over an **institutional layer that was nearly empty**,
so the patterns that were *missing* were never tutor patterns. Every component below was
licence-read on `2026-10-18` and is shelved on [`agents/top.md`](../agents/top.md),
[`repos/foundations.md`](../repos/foundations.md) or [`verticals/solutions.md`](../verticals/solutions.md).
⚠️ **Read the grade caveat at the end before any of these ships** — all twelve `p297` reads are
**sidebar-grade, not payload-grade.**

## P56 — An evaluation harness a regulator will accept (EMEA, portable)

**Who it is for.** A university or ministry deploying anything that touches **admissions ranking,
student evaluation or exam scoring** — the three uses the EU AI Act keeps in **Annex III high-risk**,
now due **`2027-12-02`** (`T-p296a`). 🔵 **`P52` covers the deployment; `P56` is the evidence
artefact** — the thing you hand an auditor.

**The wiring, bottom to top:**

1. **Harness:** [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai)
   (**MIT**, 3.0k★, **8 033 commits**). Scaffolding for LLM evals, maintained by the **UK AI Security
   Institute**. 🟢 *A government-maintained harness is a materially easier artefact to defend to a
   regulator than a bespoke test script* — that is the whole reason it is in this slot.
   🔴 **Its README names no education use: you supply every education task.**
2. **Task set:** [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (**MIT**, shelved `p296`) — teacher-exam items including a **Chilean MINEDUC** question bank
   (arXiv:2506.18710). This is what turns the empty harness into a *pedagogical* eval.
3. **Content scoring:** [`AI-for-Education/edu-qurating`](https://github.com/AI-for-Education/edu-qurating)
   (**MIT**, 277 commits) — scores generated teaching material on **factual accuracy, pedagogical
   quality and lesson engagement**, keeping the top 50th percentile. Run it on **your system's
   output**, not on training data.
4. **Alignment assertion:** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE)
   (**Apache-2.0**, CASE 1.0/1.1) — bind each eval item to a **named curriculum standard**, so
   *"curriculum-aligned"* becomes **machine-checkable instead of asserted in a slide**.
5. **Run log:** [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit)
   (**MIT**, 6.4k★) — **tamper-evident audit records** of every eval run, with actions bound to a
   specific agent identity.

**What you hand over.** An eval suite versioned next to the model config; a per-release report scored
on the three named pedagogical axes; a standards-alignment map; and a signed, tamper-evident log of
every run. **~6-8 weeks.**

🔴 **What to check before quoting.** `edu-qurating`'s trained models live on **`huggingface.co`, which
is unreachable at this environment's resolver** (`p295`) — the **code** is usable, the **published
weights are unread**. And `inspect_ai` + `agent-governance-toolkit` are **not education software**;
the education judgement is entirely yours.

## P57 — The evidence pack that unlocks a state pilot's scale gate (EMEA / Central Asia)

**Who it is for.** A government that has **already bought the platform** and set a scale gate by
decree. The live instance: **Kazakhstan** — **165 000 ChatGPT Edu licences**, AI in schools from
**`2026-09-01`**, pilot in **10 rural schools** (Pavlodar, Kyzylorda), **500 institutions by January
2027**. 🔵 **`P55` is a LATAM governance retrofit over tools already in casual use; `P57` is
different** — here the procurement is done, the deadline is a **decree**, and the deliverable is the
**evidence that justifies going from 10 schools to 500.**

**The wiring:**

1. **Policy enforcement at the call site:** [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit)
   (**MIT**) — decides whether a tool call is **allowed before it runs**, binds it to an agent
   identity, and writes a tamper-evident record. This is what makes *"AI is used responsibly in our
   schools"* a **query against a log** rather than a claim.
2. **Pre-deployment and periodic evals:** [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai)
   (**MIT**) — see `P56`; the gate report needs a *measured* answer, not a satisfaction survey.
3. **The surface teachers actually touch:** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (**MIT**, 295★, 1 026 commits) or [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp)
   (**MIT**) — reach the incumbent LMS **without forking it**. ⚠️ `moodle-mcp`'s writes are
   **ungated** (this base's `T4`): put it behind the policy layer in step 1, not beside it.
4. **The outcome number the ministry will ask for:** [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool)
   (**MIT**, 3 015 commits, shelved `p296`) for retention, **or**
   [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis)'s *Insights*, which derives topic
   understanding from **submission and test-result timestamps** — 🟢 **an outcome signal that needs no
   extra instrumentation and no new student data collection**, which matters where data rules bite.
5. **If sovereignty is raised** (Forrester expects it to shape infrastructure for ~half of APAC firms,
   and Kazakhstan runs a sovereign **KazLLM**): [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite)
   (**Apache-2.0**, Intel/OpenVINO, shelved `p296`) for on-prem inference.

**What you hand over.** A policy pack enforced in code; an audit trail per school; an eval report at
the gate; and one retention or understanding metric with a stated baseline. **~8-10 weeks**, sized to
land **before** the January 2027 gate.

🔴 **The honest risk.** The platform is **proprietary and already chosen** — you are not replacing it
and should not propose to. ⚠️ **KazLLM's parameter sizes (8B/70B) are commentary-attributed and
unread**; do not design a sovereign fallback around them without reading the grant.

## P58 — A Hausa teacher coach built on state-published weights (EMEA, Nigeria)

**Who it is for.** A Nigerian state, NGO or donor programme that needs a **teacher-facing** coach in
**Hausa**. 🔴 **The gap this answers is measured, not assumed:** the most deployed Hausa teacher tool,
**`aprendIA`** (IRC), reaches **5 800 teachers today with a projection of 137 000 by 2028** — and it
is **proprietary**. Every *open* Hausa instrument this base found is a **model or a paper**; the
**deployed product is closed.**

**The wiring:**

1. **Language layer — published by the state:** **N-ATLAS**, Nigeria's government-released open
   multilingual model (Sept 2025: **Hausa, Yoruba, Igbo, Nigerian-accented English**), now being
   scaled as a **template** across the continent by **GSMA + five African governments** as
   **ATLAS Umoja AI**. Fallback/complement: **InkubaLM** (open, five African languages incl. Hausa).
   🔴 **BLOCKING CHECK: no repository slug was recovered for N-ATLAS this pass and its licence terms
   are UNREAD.** *"Open-sourced"* is **press-attributed**. **Read the grant before a SOW names it.**
2. **Delivery shape — already proven in a comparable system:** [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform)
   (**Apache-2.0**, 847 commits, shelved `p296`) — Pakistan/Taleemabad national curriculum over
   **WhatsApp**, **15 languages**. 🟢 Same constraint set as northern Nigeria: low bandwidth, teacher
   on a phone, many languages. **Do not rebuild this; fork it.**
3. **Curriculum-bound lesson planning:** [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)
   (**MIT**, MSR India + Sikshana Foundation, shelved `p296`) — the capability is *lesson planning
   bound to a specific curriculum*, which is the task, not open-ended chat.
4. **The measurement nobody runs and everybody assumes:** [`AI-for-Education/voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework)
   (**MIT**) — **EGRA child-speech ASR evaluation**, built for **Kiswahili** and the right shape to
   re-point at Hausa. 🔴 **Adult-speech WER does not predict performance on a six-year-old in a noisy
   classroom.** If the programme has a reading component, this is the gate, not a nice-to-have.
5. **Human checkpoint:** the shape in [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent)
   (**MIT**, shelved `p296`) — **approve/reject before export, auto-grading deliberately frozen.**
   `T-p288a` records that regulators in all four regions now require exactly this.

**What you hand over.** A WhatsApp Hausa teacher coach on state-published weights, with a **measured
ASR floor on child speech** and a human approval step before anything reaches a learner.
**~10-12 weeks.**

## P59 — A verifiable skills credential for the APAC corporate-learning buyer (APAC, portable)

**Who it is for.** The buyer APAC's channel actually surfaces. 🔴 **`T-p297d`: four passes running,
every non-nil APAC education hit was CORPORATE learning** — **TCS + Pearson**'s AI learning alliance
on employer skills gaps, **Alteryx**'s Academy relaunch *with credentials*, **LearnUpon**'s Sydney
APAC HQ, **NIIT MTS**'s sixteenth year on a corporate-content list. 🔵 **For this buyer the
deliverable is not a tutor; it is a credential a third party can verify.**

**The wiring:**

1. **Assessment engine:** [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) (**MIT**, 382★,
   **1 638 commits**, NYU Tandon) — a repo per assignment, **push-triggered tests** as objective
   evidence of competence, **timestamps** as evidence of effort. 🟢 Newly the **first permissively
   licensed LMS** on [`verticals/solutions.md`](../verticals/solutions.md), so it can be **forked**,
   unlike every other platform row there. ⚠️ Scoped to **computing-science** courses, and running it
   means running **Kubernetes** — price the operations.
2. **Competency binding:** [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE)
   (**Apache-2.0**, CASE 1.0/1.1) — bind each credential to a **named competency** rather than a
   course title, which is the difference between a certificate and something an employer can filter
   on.
3. **Verification:** [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator)
   (**Apache-2.0**, **628 commits**, from the standards body) — validate issued **Open Badges 3.0**
   (2.0 also accepted). 🔴 **Two boundaries, both read rather than assumed:** its sidebar mentions
   *Comprehensive Learner Record* but **its README describes Open Badges only — do not promise CLR**;
   and **a validator validates, it does not issue.** You still build or buy the issuer.
4. **If the cohort is Indian:** [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2)
   (**MIT**, 482★) — **22 scheduled Indic languages**. ⚠️ Substrate only; it mentions no education use.
5. **If an LLM grades anything:** add `P56`'s harness. An employer-facing credential whose grading is
   unevaluated is a liability dressed as a product.

**What you hand over.** An assessment engine, a competency map, issued badges and an independent
validator — i.e. **a credential whose claims can be checked by someone who does not trust you**.
**~6-8 weeks.**

### 🔴 The grade caveat that applies to all four patterns

**Every one of the twelve repositories read this pass was read on ONE path: the rendered
`github.com` sidebar/About licence label plus README body.** `curl -sI` was **403 on 4/4** probes
(including an invented hostname, so a 403 licenses no existence claim), and there is **no
`api.github.com` channel** and **no raw payload channel** from this environment. 🔴 **No `LICENSE`
file was read at payload for any `p297` row.** This base has been bitten twice by single-path licence
reads (`p295`: `Submitty` served `BSD-3-Clause` at `LICENSE.md` with plain `LICENSE` at **404**).
**Request the payload before any of these components ships in a deliverable** — the patterns are
sound, the grants are **sidebar-grade**.

## 🟢 Pass 296 — four new patterns (`P52`-`P55`), built only from rows promoted this pass

⏱️ `2026-10-18`. Evidence:
[`p296-promotion-gap.2026-10-18-p296.tsv`](../evidence/p296-promotion-gap.2026-10-18-p296.tsv).
🔴 **Numbered `P52`-`P55`: `P29`-`P32` are taken by passes 277-278, and this pass caught itself
about to re-issue them — a duplicate pattern ID compiles into two entities with one name.**
Every component below was licence-read on `2026-10-18` and is now shelved on
[`agents/top.md`](../agents/top.md) or [`repos/foundations.md`](../repos/foundations.md).

## P52 — Defensible student evaluation for the EU's December 2027 window (EMEA)

**Who it is for.** A European university or exam board whose assessment system falls in **Annex III**
(student evaluation, exam scoring, admissions ranking). `T-p296a`: the deadline moved to
**2 December 2027**, the **classification did not change**, and the **Art. 4 literacy duty binds
now**. So this is a build-time pattern, not a relief pattern.

**Wiring.**

| layer | component | licence | why this one |
|---|---|---|---|
| submission + autograding platform | [`autolab/Autolab`](https://github.com/autolab/Autolab) | 🟡 Apache-2.0 **README-ONLY** | 808★ / 2 179 commits; runs the assignment and the automatic grade. ⚠️ **get the LICENSE payload in writing before this is a dependency** |
| integrity evidence | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 MIT | 3 838 commits, Ghent University; detects modified copies. **This is the artefact that survives an appeal** — use it as the JS library so results land in your own record, not a separate tool's UI |
| feedback suggestion (advisory) | [`ls1intum/Athena`](https://github.com/ls1intum/Athena) | 🟡 MIT *(metadata, 12/14 manifests)* | per-module Poetry packages; `module_programming_llm` for code, `module_text_llm` for prose |
| human checkpoint | — | — | 🔴 **the AI output is advisory; a human sets the grade.** `T-p288a`: in all four regions this is the regulatory interface, not a UX nicety |
| pedagogical eval | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | the measurement to put **in the conformance file** |

**Sequence.** Autolab runs the submission → Dolos produces an integrity score as structured evidence →
Athena proposes feedback → **a human issues the grade, with both machine outputs attached as
rationale**. Log every step: Annex III wants traceability, and the log *is* the conformance artefact.

⚠️ **Two licence prices in one stack.** Autolab is `README-ONLY` grade; Athena is `metadata` grade
(no licence file, 12 of 14 manifests declare MIT). **Both are usable and neither is payload-verified
— write that in the SOW rather than discovering it at legal review.** Timeline: **10-12 weeks** to a
conformance-shaped pilot on one faculty.

## P53 — Teacher-facing pilot that ships inside a US district AI moratorium (North America)

**Who it is for.** A district like **NYC**, which bans **student-facing** AI through grade 8, in a
state like **California (AB 1159)**, which bars training on student data. `p296`'s North America
block: 134 bills, 31 states. **The pilot that survives is teacher-facing and trains on nothing.**

**Wiring.**

| layer | component | licence | role |
|---|---|---|---|
| teacher skills | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 Apache-2.0 | lesson planning, differentiation, prep, formative checks — **plus the eval framework**, which is what answers the district AI committee |
| curriculum binding | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot) | 🟢 MIT | grade/subject/chapter binding and **export to Word/PowerPoint/handouts** — the teacher edits a file they already own |
| advisor-side early warning | [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool) | 🟢 MIT | 3 015 commits; surfaces students needing contact. ⚠️ branch **`develop`**. **Advisor-facing, never student-facing** |
| retrieval, not training | corpus RAG over district material | — | 🔴 **AB 1159 makes fine-tuning on student data illegal.** RAG is the compliant architecture, not merely the cheap one |

**Why it clears the committee.** Nothing is student-facing; nothing trains on student data; every
output is a document a teacher reviews and edits; and the eval framework ships with the skills, so the
pilot arrives with its own measurement. Timeline: **6-8 weeks**.

## P54 — WhatsApp teacher coach for a low-bandwidth, many-language system (APAC, portable)

**Who it is for.** A ministry or NGO where teachers have phones and intermittent data, not laptops.

**Wiring.** [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform)
(🟢 **Apache-2.0**, 847 commits) is the base: WhatsApp-delivered classroom coaching, **reading
assessment from a voice note**, lesson plans and teacher PD, with a **national-curriculum content
library** (Taleemabad, Pakistan). Add [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)
(🟢 MIT) to re-bind generation to the **host country's** curriculum, and
[`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite)
(🟢 Apache-2.0) if the speech pipeline must run **on-premise** — it ships the audio pipelines **and the
benchmarking tools to size the hardware**.

🔵 **The transferable asset is the channel, not the country.** WhatsApp delivery plus voice-note
assessment removes the device, bandwidth and literacy barriers that kill web-app pilots — which is why
this pattern also fits **LATAM** and African deployments, where `P9` previously had no permissive base.

⚠️ **Quote the README's 15 languages, not the sidebar's 9** — the repo contradicts itself.
⚠️ **The bundled curriculum is Pakistan's**; replacing it is the bulk of the work, and `T-p287a` warns
the host country's curriculum **licence** may not permit shipping it at all. **Check that before
estimating.** Timeline: **8-10 weeks** per country.

## P55 — Governance retrofit over AI that is already in use (LATAM)

**Who it is for.** The **74%**. UNESCO IESALC: **87%** of 200 institutions across 19 countries use AI;
**26%** have a strategy; adoption is driven by individuals. 🔵 **Do not sell adoption into this — the
adoption already happened, unowned.**

**Sequence, and note that steps 1-3 ship no model at all.**

1. **Inventory.** Enumerate the AI already in use by faculty and students. This is interviews and
   log analysis, not engineering, and it is the step that produces the shock that funds the rest.
2. **Boundaries.** Data-minimisation at the tool boundary (`P24`), aligned to the **risk-based
   taxonomies** the region's lawmakers are converging on — which are EU-shaped, so EU-conformant
   design is reusable here.
3. **Measurement.** [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
   (🟢 MIT) — and in this region it is the **locally sourced** instrument: its question bank is
   **Chile's Ministry of Education** teacher-certification exams (*Agencia de la Calidad* + CPEIP).
4. **Only then, a sanctioned system.** [`datakind/student-success-tool`](https://github.com/datakind/student-success-tool)
   (🟢 MIT, 3 015 commits) for retention, which is the outcome a LATAM university is actually measured
   on, with a named deployment behind it (John Jay College, funded by Google.org).

**Who to involve.** The **UNESCO Observatory on AI in Education for LAC** (launched **14 April 2026**,
Santiago) runs policy and teacher-training pilots — including **Mexico with CONALEP and DGETI**.
**Uruguay** is the one country with a binding external commitment (Council of Europe Framework
Convention, 2025); **Colombia** has **CONPES 4144**.

⚠️ **Scope to higher education.** The UNESCO instrument is HE-only; **K-12 is not covered**, and ILIA
2025 finds school-level AI education remains an exception. Do not quote 87% at a ministry about
schools. Timeline: **6 weeks** (steps 1-3) **+ 8 weeks** (step 4).

## 🟢 Pass 295 — `P52`, and it exists because A MINISTRY WROTE DOWN THE REQUIREMENT THIS BASE ALREADY HELD THE ANSWER TO

⏱️ **Seventeenth pass of `2026-10-18`.** Evidence:
[`p295-websearch.2026-10-18-p295.tsv`](../evidence/p295-websearch.2026-10-18-p295.tsv) ·
[`p295-star-channel.2026-10-18-p295.tsv`](../evidence/p295-star-channel.2026-10-18-p295.tsv).

🔵 Most patterns here start from a capability looking for a buyer. 🟢 **`P52` starts from a
procurement document.** Ethiopia's Ministry of Education launched an AI teacher assistant **into the
national curriculum** on **`2026-05-14`** for Grades **9–12**, **prioritised to function OFFLINE**
because of rural infrastructure gaps — and is separately drafting a higher-education AI framework
whose stated focus is **assessment integrity**. Those are two requirements, written by the customer,
that this base can already answer with **permissive, first-hand-verified rows**.

### `P52` — Offline-first, curriculum-aligned teacher assistant with an integrity half

**When to reach for it:** a ministry, state or district engagement where (a) connectivity cannot be
assumed, (b) the deliverable must map to a **national curriculum**, and (c) the buyer has named
**academic integrity** as a condition rather than a feature. Ethiopia is the live instance; the
pattern holds for rural LATAM, low-bandwidth APAC and Francophone West Africa, where **IFEF** has
stated the matching constraint — *« nos données ne sont pas sur Internet »*.

| layer | repo | licence | verified | what it does here |
|---|---|---|---|---|
| **Delivery substrate** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 🟢 **re-read `p295`**: 1.2k★ / **1.0k forks** / 39,803 commits | Runs **fully offline**, syncs opportunistically. The forks-to-stars ratio (**83 %**) is the deployment signature — this is software institutions *run* |
| **Curriculum authoring** | [`learningequality/studio`](https://github.com/learningequality/studio) | **MIT** | 🟡 **carried** (193★, 15,493 commits) — *not re-read this pass* | Authors the curriculum **channels** Kolibri ships. This is where Grades 9–12 mapping lives |
| **Tutor / assistant** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | 🟢 **re-read `p295`**: 41.6k★ / 5.3k forks / `v1.6.14` (`2026.10.8`) | Model-agnostic across **Ollama, LM Studio, llama.cpp, vLLM** — which is the whole reason it can run with no egress |
| **Local inference** | `llama.cpp` / Ollama / vLLM *(via DeepTutor's own adapters)* | — | 🔵 substrate, not an education row | Keeps inference **on the device or on a school server**. No student utterance leaves the building |
| **Integrity half** | [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | **BSD-3-Clause** ⚠️ payload at **`LICENSE.md`**, plain `LICENSE` is `404` | 🟢 **re-read `p295`**: 802★ / 1.1k forks / 9,321 commits | Submission, autograding **and** the TA grading workflow — the artefact an assessment-integrity framework actually asks for |

**How it wires together.**

1. **Author the curriculum in Studio, not in the tutor.** Grades 9–12 content becomes Kolibri
   channels. 🔵 This is the step that makes the deliverable *national-curriculum-aligned* rather
   than *generically pedagogical*, and it is the step vendors skip.
2. **Ship Kolibri to the school as the only networked component**, syncing opportunistically. It
   already does this; nothing is built here.
3. **Run DeepTutor against a local model** through its existing `llama.cpp`/Ollama adapters, scoped
   to the Kolibri channel as its RAG corpus. 🟢 **The offline requirement is then met structurally,
   not contractually** — the same argument `Numbas` makes for in-browser assessment.
4. **Attach Submitty for anything graded**, so the integrity position is a running system rather
   than a policy PDF.
5. **Sync artefacts, not transcripts.** When connectivity appears, push *aggregates* — mastery,
   completion, item difficulty — and leave student utterances on the device. That is what makes the
   data-residency answer survive a procurement review.

**🔴 Price these before the SOW — all four are real and all four are recorded elsewhere in this base:**

- 🔴 **DeepTutor is not a stable dependency.** `125` open PRs / `129` open issues at `p234`,
  `v1.6.14` eight days before this pass. **Pin a tag; do not track `main`.**
- 🔴 **Submitty's licence path is a trap** — a probe that tries only `LICENSE` reads it as
  unlicensed. Verified **BSD-3-Clause** at `LICENSE.md`, `1 542 B`, sha256₁₂ `c123708cb4ef`.
- 🔴 **`learningequality/studio` was NOT re-read this pass.** Its figures are carried. Re-read before
  quoting them — `p295` refuted two carried cells out of eleven.
- 🔴 **"Offline" must be verified per component, not per stack.** Kolibri's offline operation is
  first-hand on these shelves; DeepTutor's is an **inference from its adapter list**, not a measured
  property. 🔵 **Measure it in the pilot before it appears in a proposal.**

**🔵 What to say to the buyer.** Every layer is **MIT, Apache-2.0 or BSD-3-Clause** — no copyleft
reaches the deliverable, and no network clause reaches a hosted deployment. 🟢 The Ethiopian
requirement, the Francophone West African constraint and the LATAM data-residency objection are the
**same engineering problem**, and this stack answers all three by keeping inference and student data
local.

## 🟢 Pass 294 — a new recipe, and it exists because THIS BASE CARRIED A STALE FIGURE FOR EIGHTEEN PASSES ON A CHANNEL THAT WAS NEVER CLOSED

⏱️ **Sixteenth pass of `2026-10-18`.** Evidence:
[`p294-star-channel.2026-10-18-p294.tsv`](../evidence/p294-star-channel.2026-10-18-p294.tsv) ·
[`p294-proxy-existence-control.2026-10-18-p294.tsv`](../evidence/p294-proxy-existence-control.2026-10-18-p294.tsv).

🔴 **`p293` declared the star channel closed** after `api.github.com` answered `403` to repository
metadata, and published *"none is first-hand and none is published"*. 🟢 `WebFetch` over the
rendered `github.com` page — **the channel `P349` was built on at `p110`** — answered on the first
try. Reading it refuted **three cells this base had published**, including a description
(*"12-lesson course"*) carried in its own prose since `p275`.

🔵 **The deliverable lesson is not "re-read your numbers".** It is that a figure in a client
artefact has **four** parts, and this base was shipping one of them: the **value**, its **channel**,
that channel's **resolution bound**, and the **date it was read**. A value alone cannot be checked,
cannot be aged, and cannot be defended when a client's own analyst pulls a different number.

### 🔵 The one error class behind all three refuted cells

🔴 **Measuring channel A and concluding about subject B.** `p293` measured `api.github.com` and
concluded about *stars*. `p292` probed two guessed slug spellings and concluded about a *project*.
`p294` ran `make carried` on a **guessed** slug (`NousResearch/Hermes`), got `NEW`, and nearly
opened a row for a repository `CARRIED` since `p275` — the real spelling,
`NousResearch/hermes-agent`, was in the index the whole time. 🟢 Three passes, one class, and the
standing answer is `p293`'s: **ask, calibrate, then believe.**

## P51 — Every figure in the deliverable carries its channel, its bound and its read-date *(new in pass 294)*

**Target:** any education engagement whose output contains numbers a client will act on — a market
sizing, a build-versus-buy comparison, an adoption baseline, a shortlist with popularity or
maturity signals. 🔵 In this sector the numbers come almost entirely from **vendor market research
and social posts**, and this base has now measured the same repository at **47.3k**, **67.2k** and
**77.4k** stars in two passes. A deck that states one of those is wrong 2 times in 3.

🔴 **Why this is a recipe and not a disclaimer.** The failure is not *imprecision*, it is
**unfalsifiability**. A cell reading `41.5k` cannot be checked by the client, cannot be aged by the
studio, and gets re-quoted for eighteen passes. A cell reading
`41.6k · WebFetch github.com page · ±50 (K-3CIFRAS) · 2026-10-18` is checkable in thirty seconds by
anyone, including the client's procurement analyst — which is what makes it a procurement artefact.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| the figure's channel, declared | [`compose/code/p798-proxy-refusal-ledger`](code/p798-proxy-refusal-ledger/README.md) | 🟢 **this base's** | **22 offline controls.** Separates the **channel** verdict from the **existence** verdict, so *"we could not fetch it"* can never be written up as *"the source is not there"* — `p294` proved an **invented** hostname earns the identical refusal |
| the resolution bound on a rendered count | [`compose/code/p349-star-resolution-band`](code/p349-star-resolution-band/README.md) + [`p351-star-digit-sweep`](code/p351-star-digit-sweep/README.md) | 🟢 **this base's** | the bound is a **step function**, not "3 significant figures": **exact** below 1 000, **±50** in the `41.6k` band, **±500** above 100k. 🔴 Quote `41.6k ±50`, never `41,600` |
| is the figure a positive-class artefact | [`compose/code/p415-positive-class-stars`](code/p415-positive-class-stars/README.md) | 🟢 **this base's** | a shortlist ranked on stars inherits the sampling of whatever list surfaced the candidates |
| monotonic sanity | the read-date column itself | — | 🟢 **The cheapest check in the set, and it caught a claim this pass.** Stars never fall: *"32 741"* dated after a first-hand **40.8k** is refuted by arithmetic, with no second fetch |
| derived quantities re-derived from rows | `make recount` → [`compose/code/p274-quantity-recount`](code/p274-quantity-recount/README.md) | 🟢 **this base's** | any total, count or "N of M" in the deck is recomputed from the rows instead of being retyped |
| currency of a pinned payload | [`compose/code/p987-census-sha-currency`](code/p987-census-sha-currency/README.md) | 🟢 **this base's** | the same discipline for grants: **bytes + sha256₁₂ at a pin**, so "unchanged" is a measurement — `HKUDS/DeepTutor`'s `11 408 B` / `cd2f54e1e506` reproduced at a **new** pin this pass |
| the grant beside the figure | [`p228-shelf-gate/classify_grant.py`](code/p228-shelf-gate/classify_grant.py) over `raw.githubusercontent.com/<slug>/<sha>/<path>` | 🟢 **this base's** | 🔴 `github.com` answers **`403`** in a restricted-egress environment while `raw` answers `200`. **Never let one host's refusal stand for the repository** |

### What you hand over

1. **A figure table with four columns, not one:** value · channel · bound · read-date. Any cell
   missing a channel is marked **`UNSOURCED`** and does not go in the deck.
2. **A channel appendix** naming, per host, what answered and what refused — with the refusal
   attributed to the **layer that logged it**, and an explicit
   `EXISTENCE-UNMEASURED (channel refused)` wherever the environment, not the source, was the limit.
3. **The monotonic column.** Any quantity that can only increase (stars, forks, enrolled cohorts,
   cumulative spend) is checked against the previous read before publication. 🔵 This is the one
   control that needs no network.
4. **A re-read cadence, with the cadence stated.** 🔴 The defect this recipe exists for was not a
   wrong number: it was a **right** number that nothing re-read. Eighteen passes.

### 🔴 What to check before quoting

- 🔴 **A vendor market size is not a measurement.** This pass alone: **$6.4 B**, **$7.52 B**,
  **$10.6 B** for overlapping windows, endpoints **$10.6 B (2026)** to **$79.6 B (2034)**, CAGRs
  **28 %** to **36 %**. 🟢 **Quote the spread and name the publishers**, or quote nothing.
- 🔴 **Two-decimal shares are a tell, not precision.** *"K-12 = 45.62 % of adoption"* comes with no
  method. Carry it as a **ranking** (K-12 leads, language learning grows fastest), never as a value.
- 🔴 **A secondary figure the source itself flags as secondary** — *"student AI usage 66 % → 92 %"* —
  does not enter a deliverable until the original report is read.
- 🔴 **`EGRESS_DENIED` is not `404`, and `curl -sI` cannot tell them apart here.** Real and invented
  hosts both return `000`. 🟢 Any claim of the form *"the source is gone"* needs a channel that
  answered.

## 🟢 Pass 293 — a new recipe, and it exists because ONE ORGANISATION SHIPPED TWO GRANTS IN ONE WEEK AND ONLY ONE OF THEM IS REAL

⏱️ **Fifteenth pass of `2026-10-18`.** Evidence:
[`p293-websearch.2026-10-18-p293.tsv`](../evidence/p293-websearch.2026-10-18-p293.tsv) ·
[`p293-slug-oracle.2026-10-18-p293.tsv`](../evidence/p293-slug-oracle.2026-10-18-p293.tsv) ·
[`channel-conflict.2026-10-18-p293.tsv`](../evidence/channel-conflict.2026-10-18-p293.tsv).

| finding | verdict |
|---|---|
| `p292`'s ranked item 1 — recover `tokenaii`'s slug, read the grant at a pin | 🟢 **DISCHARGED.** [`tokenaii/Horus-Taleeq-0.2B-Base`](https://github.com/tokenaii/Horus-Taleeq-0.2B-Base), pin `f7a7700289791a9c114ab038af73b4d45c17c7e7`, `LICENSE` **MIT**, 1 080 B, sha256₁₂ `96c22722c817` |
| `p292`'s ranked item 2 — the README channel as a column *(carried FIVE passes)* | 🟢 **DISCHARGED.** Three appended columns in `p278`'s `sweep.sh`; ladder read from `p288`, one copy |
| `p292`'s *"credential prompt = INCONCLUSIVE"* | 🔴 **REFUTED.** Calibrated against a known-real and a known-fake control, the prompt **discriminates**. `p292` threw away three real negatives |
| `p292`'s *"OpenEduCat's default branch is `master`"* | 🔴 **WRONG — it is `19.0`.** The lesson (*"the 404 is about the branch name"*) stands; the name was guessed instead of read from the symref |
| the candidate's place on an education shelf | 🔴 **REFUTED by its own README** — zero education claims; filed as a substrate, not an agent |

### 🔵 The one error class behind three of those rows

🔴 **Guessing a name the channel will tell you.** The slug (four guesses, thrown away as
inconclusive), the branch (`master` inferred from a `404`), and the refusal signature itself
(read as noise when it was a measurement). Three findings, one root cause, all inside one hour of
`p292`. 🟢 `p293`'s oracle is the standing answer: **ask, calibrate, then believe**.

---

## P50 — The grant bill of materials, pinned, as the first deliverable of any education AI build *(new in pass 293)*

**Target:** any education or vocational client who will **redistribute, host for others, or
procure** an AI layer — i.e. all of them. 🔵 Public-sector education procurement in every region
this base maps asks the same question before it asks about pedagogy: *what is in it, and are we
allowed to ship it?*

🔴 **Why this is a recipe and not hygiene.** `p293` measured **one organisation, one week, two
grades**: `Horus-Taleeq-0.2B-Base` is MIT with its payload and README in agreement, and its
sibling `Horus-Lens-1.0` asserts Apache-2.0 in a README while **four licence paths `404` at the
pin**. 🔵 A bill of materials built from organisation names, press coverage or GitHub's licence
badge would have carried both as permissive. The unit of licence risk is **the repository, at a
commit** — never the org, never the model family.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| does this slug exist at all | [`compose/code/p293-slug-existence-oracle`](code/p293-slug-existence-oracle/README.md) | 🟢 **this base's** | **45 offline controls**; a **calibration pair gates every verdict**, so a channel that changed its refusal wording cannot silently invert the answer |
| the grant body, at a commit | `git ls-remote --symref` for the branch and HEAD, then `raw.githubusercontent.com/<slug>/<sha>/<path>` | — | 🔴 **Read the branch, never guess it** — `openeducat/openeducat_erp` is `19.0`, not `master` or `main`. 🔵 `raw` answers at an **arbitrary SHA**, which is what makes the read reproducible |
| the family, from the body | [`compose/code/p228-shelf-gate/classify_grant.py`](code/p228-shelf-gate/classify_grant.py) | 🟢 **this base's** | positional: the **earliest licence title in document order** wins, because every unsafe channel failed on a substring later in the body than the real title |
| the README channel | [`compose/code/p288-readme-channel`](code/p288-readme-channel/README.md), now a **column** of [`p278`'s sweep](code/p278-channel-conflict/sweep.sh) | 🟢 **this base's** | turns `AGREE` / `DANGLING-CLAIM` / `NO-CHANNEL` into a per-row verdict instead of a hand-run |
| the manifest channel | the same sweep's per-package walk | 🟢 **this base's** | catches **subpackage disagreement** — a studio vendoring one directory of a monorepo gets *that* directory's grant |
| one repo, two names | `head_sha()` collision report (`p283`'s rule) | 🟢 **this base's** | `Horus-Taleeq-0.2B-Base` and `Horus-Taleeq-0.2B` share a HEAD: **one** row, not two |
| the platform underneath | **Moodle** (GPL-3.0) · **Open edX** (Apache-2.0) · **OpenEduCat Community** (LGPL-3.0) | copyleft | 🔴 Keep them as the **system of record behind an HTTP/LTI boundary**; the AI layer stays separate and permissive. 🔴 OpenEduCat **Enterprise is proprietary and agreement-gated** |

### What you hand over

1. **One row per dependency**, each carrying: slug · default branch **as read from the symref** ·
   pin · licence path · **bytes** · **sha256₁₂** · family · README verdict · manifest verdict.
2. **A verdict vocabulary that cannot overclaim.** `ABSENT-OR-PRIVATE` is one token, because this
   channel cannot separate a missing repository from a private one — control `C9` forbids a bare
   `ABSENT` from entering the set at all.
3. **The `DANGLING-CLAIM` list, with its posture.** Each one is an **`ASK`**: a grant is claimed
   and never served, so the vendor is asked for a licence payload *before* the build depends on it.
4. **The re-run.** Every figure above is reproducible from the pin by a third party with network
   access and no credentials — which is the property that makes it a procurement artefact rather
   than an assertion.

### 🔴 What to check before quoting

- 🔴 **`ABSENT-OR-PRIVATE` is not "does not exist".** A private repository answers identically.
  Do not write a non-existence finding into a client deliverable on this channel's word alone.
- 🔴 **A README claim is a reference, not a grant.** `p742`'s distinction: `AGREE` means two
  channels concur, `DANGLING-CLAIM` means one channel asserts and none serves. Only a **body**
  read at a pin is a grant.
- 🔴 **The oracle must be calibrated where it runs.** The refusal signature is a property of the
  *channel*, not of git or of github.com. `--online` runs the control pair first and reports
  nothing if either control fails — 🔵 an uncalibrated read is exactly what produced `p292`'s row.
- 🔴 **Byte counts and digests must be taken from a FILE, not a shell variable.** `$(...)` strips
  trailing newlines, so the same blob measures **8 240 B / `8f4ce028f93d`** through command
  substitution and **8 241 B / `528f84036800`** as a file. 🟡 Caught this pass only because `p292`
  had published the digest. A one-byte difference is a completely different sha.
- 🟡 **Model weights are usually NOT in the repository.** Taleeq's repo carries training code,
  stages, data policy and a compute profile; the weights live on a host that is unreachable from
  here. 🔴 A grant read on the code says nothing about the weights' licence — ask separately.

### 🟢 The Arabic-medium variant, since this pass is where the substrate came from

For an Arabic-medium tutoring or assessment build — the MENA engagements `P39` and `P40` open and
this base could never supply a substrate for — the stack is:
**`tokenaii/Horus-Taleeq-0.2B-Base` (MIT, at its pin)** for the Arabic language layer ·
**Moodle or Open edX** as the system of record · **`P49`**'s decision store for the oversight
record · **`P50`** (this recipe) as the procurement artefact that makes the first item defensible.

🔴 **State the substrate's boundary in the SOW, because the repository states it:** this is a
**base-model development release**, *"not a finished production chat model"*, with **no
instruction tuning and no safety alignment**, and it **does not claim full corpus
reproducibility**. Instruction tuning, alignment and evaluation are the studio's work, and they
are the majority of it. 🟢 That is a feature of the quote, not a caveat buried in it.

## 🟢 Pass 292 — the evidence store, BUILT; and the backlog entry that asked for it was wrong about its own size

⏱️ **Fourteenth pass of `2026-10-18`.** Evidence:
[`decision-store-worked.2026-10-18-p292.jsonl`](../evidence/decision-store-worked.2026-10-18-p292.jsonl) ·
[`p292-websearch.2026-10-18-p292.tsv`](../evidence/p292-websearch.2026-10-18-p292.tsv).

🟢 **`p291`'s ranked item 1 is done.** The component `P45`-`P48` terminate in — *"an append-only
record of who decided what, shown what, under which rubric version"* — exists, with **90
offline controls** in `make hooks`:
[`compose/code/p292-decision-evidence-store`](code/p292-decision-evidence-store/README.md).
It needs no network, no server and no dependency outside the standard library.

🔴 **And building it refuted the entry that asked for it.** `p290` wrote *"three recipes … and
one evidence store"*; `p291` wrote *"now **four** recipes, one build"*. Measured against the
shelves, **two** recipes terminate in the decision record:

| recipe | what the shelf actually says it needs | is it this component? |
|---|---|---|
| `P45` admissions | *"the evidence store — you build it"*; *"the append-only decision record"* | 🟢 **yes** |
| `P48` vocational | *"Terminate in the evidence store — the same append-only record"* | 🟢 **yes** |
| `P46` retention | *"the **intervention log** — date, method, response, outcome"* | 🔴 **adjacent** — an outcome log over time |
| `P47` grading | *"a built **deadline-and-evidence** layer"*, *"statutory, calendar-bound"* | 🔴 **adjacent** — a calendar |

🔵 **Why that is not a wording quibble.** *"One build"* sounds like one thing, so it was costed
as one thing — and deferred as one thing, for **four passes**. Stated correctly it is **one
substrate, four schemas**: all four surfaces write into the same chain, each with its own
closed act vocabulary, and `P46` and `P47` each additionally need a component this store does
**not** supply. 🟢 Said that way it was buildable in a single pass. 🔴 Arm `S2` makes the
overclaim standing — no line mentioning the store may assert more store-bearing recipes than
the shelves carry — and it fails `p291`'s own sentence.

### 🔴 The boundary, because this product category's standard overclaim is exactly here

The chain is **tamper-EVIDENT, not tamper-proof.** It catches an edit, a deletion or a reorder
*in place*; it does **not** catch a writer who rewrites the whole file, because that writer
recomputes every link and the result verifies clean. 🟢 **Control `C18` asserts that failure as
a control**, so no reader of the suite can mistake the guarantee, and `anchor_statement()`
prints the sentence beside the real head value. What closes the gap is publishing `head()`
where the writer cannot reach it — **the anchor is the client's**.

### 🟢 The one place where the obvious control was the wrong one

The tempting rule is to reject a decision identical to the agent's recommendation as a rubber
stamp. 🔴 That is wrong twice over: a human who agrees with a correct recommendation **has still
decided**, and a store that rejects agreement teaches its users to stop recording the
recommendation — destroying the only evidence the question can be answered from. 🟢 So
concurrence is **derived, sealed into the digest, and never refused**, and `concurrence_rate()`
returns `(concurred, comparable, rate)`. **A rate near 1.0 over a large denominator is the
rubber-stamp finding** an oversight audit is actually looking for, and it is measurable only
because the record was kept. The worked example reports `2/6 = 0.33`.

## P49 — The oversight record sold as the deliverable, because the agent layer is now free and the record never was *(new in pass 292)*

**Target:** any client whose education or vocational AI output reaches a human who then decides
— EU **Annex III(3)** high-risk oversight, the **Oklahoma / Maryland** bar on AI in high-stakes
student decisions, **Vietnam**'s sole-basis test. 🔵 All three regimes ask the *same* question —
*can you show a human decided, and what they were shown?* — so one implementation answers all
of them, in all four regions.

🔵 **Why this is the billable half.** `P45`-`P48` establish that the agent layer is MIT and
free: `iblai`'s segment configs are `GRANTED-AT-PIN` MIT, `cedanl/student-signal` is MIT. 🔴 What
no repository on these shelves supplies, after 292 passes of looking, is **the record**. A
client cannot buy it, cannot defend an audit without it, and the four regimes above all
terminate in it.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| the record | [`compose/code/p292-decision-evidence-store`](code/p292-decision-evidence-store/README.md) | 🟢 **this base's** — reference implementation, adapt freely | 106 offline controls; JSON-Lines + sha256 chain; no server, no dependency outside the standard library. An auditor reads it with `jq` |
| the acts | `SURFACES` — admissions · retention · grading · credential · vocational | — | 🔵 A **closed** vocabulary per surface, so *"scored"* can never be written in the slot that means *"decided"* |
| the agent layer | `iblai/*-agents` at their pins · [`cedanl/student-signal`](https://github.com/cedanl/student-signal) | 🟢 **MIT** | already verified at the pin (`p291`); the store records them as `role: "advisory"` and refuses any other role |
| the anchor | 🔴 **the client's** — publish `head()` daily outside the writer's reach | the client's | 🔴 Without it the chain is tamper-evident only. **Say so in the SOW**; `anchor_statement()` prints the sentence |
| the read model | 🔴 **beside the chain, never in it** | the client's | Deliberate non-feature: a store that also serves queries stops being append-only the first time someone needs an index rebuilt |

### What you hand over

1. **The chain** — one JSON line per decision, `fsync`ed, linked by sha256 over canonical bytes.
2. **Ten refusals that are controls, not validation** — the agent cannot be recorded as the
   decider (`R1`); no decision without the digest-bound observations the human saw (`R2`); no
   decision without the rubric version in force (`R3`); distress routes to a **named human**,
   not a queue (`R10`); the subject reference must be pseudonymous (`R9`).
3. **`verify()`** — a chain walk that catches edit-in-place, deletion and reorder, with the
   file-and-line of every finding.
4. **`concurrence_rate()`** — the rubber-stamp measurement, per surface.
5. **`limb_census()`** — every Annex III limb exercised, `NONE-DECLARED` included, which is
   `P48` step 2's recorded exclusion and the first thing an auditor probes.

### 🔴 What to check before quoting

- 🔴 **Retention is out of scope and jurisdiction-specific.** `R9` keeps the long-lived record
  pseudonymous so retention stays a client decision; the schedule itself is counsel's.
- 🔴 **`R1` fixes attribution, not authorisation.** It ensures the *record* cannot misattribute
  the decision. It cannot stop a badly-scoped agent from writing elsewhere — that is
  `auth-profiles.json` and the host sandbox policy, as `P45` already says.
- 🟡 **The Annex III limb tokens are `ATTRIBUTED`**, keyed to a conference reproduction plus
  commentary; EUR-Lex has been unreachable since `p289`. The code does not depend on the
  wording — `ANNEX_LIMBS` is a closed token set. Check the Official Journal before a client
  relies on the mapping.
- 🟢 **Licence surface is clean**: standard library only, so there is no third-party grant to
  audit in the deliverable itself.

## 🟢 Pass 291 — the licence boundary, corrected and completed; and one recipe for the part of the AI Act that the segment labels hide

⏱️ **Thirteenth pass of `2026-10-18`.** Evidence:
[`submodule-pin-grant.2026-10-18-p291.tsv`](../evidence/submodule-pin-grant.2026-10-18-p291.tsv) ·
[`segment-education-surface.2026-10-18-p291.tsv`](../evidence/segment-education-surface.2026-10-18-p291.tsv) ·
[`guard-vocabulary.2026-10-18-p291.tsv`](../evidence/guard-vocabulary.2026-10-18-p291.tsv).

### 🟢 The licence boundary for every recipe that vendors `iblai` configurations — now all seven, read at the pin

🔵 **Supersedes the `p290` table below.** That table asked *"HEAD read = gitlink pinned?"* and
could answer for two segments. The question was the wrong one: `raw.githubusercontent.com`
serves a payload **at any commit**, so the grant can be read **at the pin itself** and `HEAD`
never enters. All seven, read that way this pass:

| what you clone | pinned gitlink | grant read **at that commit** |
|---|---|---|
| [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) | `1a2d898bbd04` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | `54ee9d91eecd` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/enterprise-agents`](https://github.com/iblai/enterprise-agents) | `7f00879a9f57` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/government-agents`](https://github.com/iblai/government-agents) | `fbf903250c96` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/legal-agents`](https://github.com/iblai/legal-agents) | `b059cd452bf3` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/financial-services-agents`](https://github.com/iblai/financial-services-agents) | `6ea18f015b1e` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |
| [`iblai/medical-healthcare-agents`](https://github.com/iblai/medical-healthcare-agents) | `cd0d9fcfa523` | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` |

🔴 **Quote the submodule, never the superproject** — that still holds, and it is now a gate
([`gate-pin-grant`](code/p291-submodule-pin-grant/README.md), 31 controls in `make hooks`).
🟢 **But the verification recipe changes**, and it is two lines:

```sh
# the grant a `git clone --recurse-submodules` ACTUALLY lands on:
PIN=$(git ls-tree HEAD <segment> | awk '{print $3}')        # the 160000 gitlink
curl -fsS "https://raw.githubusercontent.com/<owner>/<repo>/$PIN/LICENSE"
```

🔵 Do **not** read the submodule at `HEAD` and then check `HEAD == pin`. If `HEAD` has moved,
that check reports *"cannot verify"* for a grant that is sitting there readable — and the next
reader re-probes at `HEAD` and ships the licence at `HEAD`, which is not the one pinned.

## P48 — The vocational-training guard retrofit: the Annex III work that nobody labels "education" *(new in pass 291)*

**Who it is for.** Any client running corporate L&D, professional certification or
continuing-education systems in the EU — law firms (CLE), financial services (FINRA CE),
healthcare (HIPAA/credentialing), government workforce development. 🔴 **None of them calls
itself an education buyer**, and all of them are inside the Act's education limb.

**The premise, measured rather than assumed.** EU AI Act **Annex III(3)** limb (a) covers
access, admission or assignment to educational **and vocational** training institutions; limb
(b) the evaluation of learning outcomes including where they steer a learner's path. **One
limb suffices.** 🟡 ATTRIBUTED — a conference reproduction plus commentary; EUR-Lex is
unreachable from here (`p289`). Verify against the Official Journal before a client relies on it.

🔴 **The measured gap, from the one MIT corpus this base has read end to end:**

| | education-labelled segments | the five "non-education" segments |
|---|---|---|
| agents | 30 | 65 |
| with a human-decision guard | 7 (**23 %**) | 5 (**8 %**) |
| L&D agents | — | **6**, of which **1** guarded |

### The build

1. **Inventory the learning surface, not the org chart.** Walk every agent, workflow and model
   and keep the ones that *recommend a learning path, score a learner, track a credential or
   gate a certification*. Precedent: in `iblai`'s set those live in `enterprise/training-agent`,
   `government/employee-training-agent`, `legal/training-agent` (CLE),
   `financial-services/employee-training-agent` (FINRA CE),
   `medical-healthcare/compliance-training-agent`. **The segment label will not find them.**
2. **Map each to an Annex III(3) limb**, and record the ones that match none — the exclusions
   are what an auditor will probe first.
3. **Retrofit the guard clause**, copying the language that is already MIT and already written:
   *"Never issue a final … decision unilaterally; always present findings as input for the
   human reader"* (`higher-education/application-reader-agent`) ·
   *"Treat every risk flag as a hypothesis to be confirmed, not a verdict"*
   (`higher-education/retention-agent`) · *"decisions are made by the full team … not by any
   single professional or AI tool"* (`k-12/special-education-agent`). 🟢 All three are
   `GRANTED-AT-PIN` MIT: copy them, do not draft them.
4. **Build the translation table.** 🔴 The corpus contains the regulator's phrase *"sole basis"*
   **once in 95 agents**, and that occurrence is a CPT-coding note, not a guard. A keyword
   audit scores one hit and it is a false positive, while 12 real guards go unseen. Ship a
   mapping from payload language → Annex III limb so the engineer's words and the auditor's
   list meet. **This is the deliverable nothing on these shelves supplies.**
5. **Terminate in the evidence store** — the same append-only record of *who decided what,
   shown what, under which rubric version* that [`P45`](#p45--the-admissions-reader-that-is-structurally-incapable-of-admitting-anyone-new-in-pass-290)
   terminates in. 🟢 **BUILT in `p292`:**
   [`compose/code/p292-decision-evidence-store`](code/p292-decision-evidence-store/README.md),
   106 offline controls, in `make hooks`. Write this surface's acts through the `vocational`
   vocabulary and record the limb — `NONE-DECLARED` included, which is step 2's exclusion.
   🔴 **CORRECTED in `p292`:** this step used to read *"that `P45`, `P46` and `P47` all terminate
   in … `P48` makes **four** recipes that need the identical component."* Measured against the
   shelves it is **two** — `P46` needs an **intervention log** and `P47` a
   **deadline-and-evidence layer**, which are adjacent components, not this one. 🔵 *"One
   build"* sounded like one thing, so it was costed as one thing and deferred for four passes;
   stated as **one substrate, four schemas** it took a single pass. Arm `S2` now fails the old
   sentence.

**Shape.** 🔵 Steps 1-2 are a 2-3 week audit that is sellable on its own and produces the
inventory the rest depends on. Steps 3-4 are ~4 weeks. Step 5 is the build, and it is the same
build in all four regions. 🔴 **Scope boundary:** step 3 changes what an agent *says* it will
not do. That is a prompt-level control, not an enforced one — do not sell it as enforcement.
Enforcement is step 5's store plus the client's own workflow gate.

## 🟢 Pass 290 — three recipes whose compliance layer is a DEPENDENCY instead of a deliverable, and one evidence store that is neither

⏱️ **Twelfth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`submodule-grant-boundary.2026-10-18-p290.tsv`](../evidence/submodule-grant-boundary.2026-10-18-p290.tsv).

🔵 **The licence boundary shared by all three recipes below, because it is unusual and it is
NOT where a reader will look for it.** The MIT grant that matters is **not** the one on
[`iblai/iblai-claw-agents`](https://github.com/iblai/iblai-claw-agents). That repository is a
13-file shell whose segment directories are **`160000 commit` gitlinks**. The payload that
covers the configurations you vendor is each **submodule's own** `LICENSE`:

| what you clone | grant read first-hand | HEAD read = gitlink pinned? |
|---|---|---|
| [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` | 🟢 **yes** — `1a2d898bbd04` |
| [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | 🟢 **MIT**, 1 063 B, sha256₁₂ `f1269b7b2313` | 🟢 **yes** — `54ee9d91eecd` |
| [`iblai/iblai-claw-setup`](https://github.com/iblai/iblai-claw-setup) (the host) | 🟢 **MIT**, 1 063 B | tree **not enumerated** — stated, not assumed |

🔴 **Quote the submodule, never the superproject.** If a later HEAD moves past the pinned
commit, the pin is an **unread commit** and the correct posture is `UNVERIFIED-AT-PIN`: re-read
the payload at the pin before shipping. 🔴 **Five of seven segments are unprobed** — enterprise,
government, legal, financial-services, medical-healthcare. A non-education engagement **must
probe its own segment**; the superproject's single MIT badge is not an answer for it.

🔴 **And the honest shape of what these configs are**: `SOUL.md` / `IDENTITY.md` / `MEMORY.md` /
`TOOLS.md` / `auth-profiles.json` per agent, plus `openclaw.json`, `.config-hash`, `skills/` and
`.env.example`. **No application code, no build, no tests** — the README says so itself. They
are a **prompt-and-wiring layer**, which is why every recipe below puts the billable work
somewhere else.

## P45 — The admissions reader that is STRUCTURALLY INCAPABLE of admitting anyone *(new in pass 290)*

**Target:** any institution whose admissions output reaches an EU-located applicant (EU AI Act
**Annex III**: admission decisions and evaluation of learners are **high-risk**), plus US
institutions under the **Oklahoma / Maryland** bar on AI in high-stakes student decisions, plus
Vietnamese institutions under the **sole-basis** test.

🔵 **Why this is a pattern and not a product.** Every commercial application-scoring tool sells
*the score*. The regulated act is **not scoring** — it is **deciding**. A recipe that cannot
decide is cheaper to build, cheaper to defend, and is the only shape that is unambiguously
permitted in all three regimes today.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| reader agent | [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) → `agents/application-reader-agent` | 🟢 **MIT** at pinned `1a2d898bbd04` | 🟢 **Its `SOUL.md` already refuses the regulated act**: *"Never issue a final admit or deny decision unilaterally; always present findings as input for the human reader"*, and *"flag anomalies — grade inflation, unexplained gaps, inconsistent self-reported data — as observations, not conclusions"* |
| funnel siblings | same repo → `enrollment-agent`, `yield-agent`, `prospective-student-agent` | 🟢 MIT | the same rubric and the same refusal across the whole funnel, so one evidence schema covers all of it |
| host runtime | [`iblai/iblai-claw-setup`](https://github.com/iblai/iblai-claw-setup) (OpenClaw) or **NVIDIA NemoClaw** | 🟢 MIT / per vendor | the configs are drop-in: copy `openclaw.json`, `.config-hash`, `agents/`, `skills/`, `workspace/` into `/sandbox/.openclaw/`, recompute the hash, reload the gateway |
| systems of record | `skills/slate` (admissions), `skills/banner` (SIS), `skills/salesforce-education-cloud`, `skills/workday` | 🟢 MIT **adapters** | 🔴 the adapter is MIT; **Slate, Banner, Salesforce and Workday are proprietary** — contract, credentials and API terms per system. This is the schedule risk, not the licence |
| 🟢 **the evidence store** | [`compose/code/p292-decision-evidence-store`](code/p292-decision-evidence-store/README.md) — **built in `p292`**, adapt it | 🔴 the **anchor** is the client's | 🔴 **Nothing else in the stack records anything**, and that is still the deliverable. 🟢 Now a reference implementation rather than a line item: 106 offline controls, `admissions` act vocabulary, `R1` refuses the agent as decider, `R10` routes distress to a named human. 🔴 It is tamper-**evident**, not tamper-proof — publish `head()` outside the writer's reach |

### The flow

1. An application lands in **Slate**; the adapter pulls it with the institution's **published
   rubric** as the only scoring authority.
2. `application-reader-agent` returns **observations**: academic indicators, contextual factors,
   anomalies flagged as observations, and an explicit statement of *what the score does and does
   not capture*.
3. 🔴 **Nothing is written to the applicant record.** Output goes to a **human reader's queue**.
4. The human reader decides. 🟢 **The decision, the reader's identity, the timestamp, the
   observations shown to them, and the rubric version in force are written to an append-only
   store.**
5. Distress flag: the config instructs *"flag any application that contains information
   suggesting the applicant is in distress for immediate human follow-up"* — route it to a named
   human, not to a queue.

### What the deliverable is

🟢 **Steps 3–4: the review queue and the append-only decision record.** The agent layer is a
free MIT dependency now; the thing a regulator, an auditor or a rejected applicant's lawyer
asks for is **the record that a human decided and what they were shown**. 🔵 Build it once and
it answers the EU high-risk oversight requirement, the Oklahoma/Maryland bar and Vietnam's
sole-basis clause from one implementation.

### What to check before quoting

- 🔴 **The prompt is not a control.** *"Never issue a final decision"* is an instruction to a
  model. The **enforcement** is that the agent has no write path to the applicant record —
  verify that in `auth-profiles.json` and in the host sandbox policy, not in the prose.
- 🟡 **Rubric versioning is in scope and is not in the repo.** "Apply the rubric consistently"
  is only auditable if the rubric in force at decision time is recorded with the decision.
- 🟢 **Licence surface is clean**: MIT at the pinned commit, verified per repository.

## P46 — The retention loop with a DEFENSIBLE number, where the model is permissive and the threshold is the client's *(new in pass 290)*

**Target:** institutions with an SIS and a student-success team; strongest fit in 🇳🇱/EMEA higher
education (where the library originates) and 🇺🇸 state/district systems (where the reference
design originates).

🔵 **Why the measurement layer comes first.** `p288`'s regulatory finding was that a risk score
which drives an intervention without human review is the regulated act. The usual failure is
upstream of that: nobody can say **how wrong the score is**. This recipe starts from the one
component that answers that question in its own API.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| risk measurement | [`cedanl/student-signal`](https://github.com/cedanl/student-signal) — `prepare()` → `rank()` → `evaluate()` | 🟢 **MIT**, 1 078 B, HEAD `4463e8d17cfb` | 🟢 It **ranks** rather than labels, and `evaluate()` reports **precision/recall at multiple invitation thresholds** with a traffic-light status. **Invitation-rule methodology (Eegdeman, 2022)** |
| the model | **the client's choice** — any sklearn-compatible estimator | 🟢 **the client's** | 🔵 `student-signal` deliberately does **not** pick one. The client's model and thresholds stay the client's IP beside an MIT library |
| reference design | [`jknowles/EWStools`](https://github.com/jknowles/EWStools) | 🟡 **GPL-3.0 only** | 🟢 ROC testing, model search and post-prediction adjustment as a **US state education agency** shipped them (Wisconsin DEWS). 🔴 **Last commit `2016-02-03` — port the method, never the package.** Linking it in an R deliverable makes that deliverable a derivative work |
| intervention agent | [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) → `agents/retention-agent` | 🟢 **MIT** at pinned `1a2d898bbd04` | 🟢 Its `SOUL.md` carries the posture the regime requires: *"Treat every risk flag as a hypothesis to be confirmed, not a verdict"*, *"use the risk score to triage, not to rank human worth"*, and *"know the difference between academic struggle and a mental health or safety concern"* |
| data in | `skills/banner` or `skills/powerschool` (SIS), `skills/canvas` (engagement), `skills/eab-navigate` / `skills/civitas-learning` | 🟢 MIT adapters over 🔴 proprietary systems | one adapter set for both the measurement feed and the outreach surface |
| 🔴 **the intervention log** | **you build it** | **the client's** | 🔴 *"Log every intervention — date, method, response, outcome"* is a sentence in a prompt. The **store** is the deliverable |

### The flow

1. Nightly SIS + LMS extract → `prepare(train_df, pred_df, target_col=..., id_col=...)`.
2. The client's estimator trains; `rank()` produces a **ranked list**, not a flag.
3. 🟢 `evaluate()` publishes **precision and recall at the invitation threshold the institution
   actually intends to use**, before anyone is contacted. **This is the number that makes the
   programme defensible** — it states how many invited students will be false positives.
4. The success team sets the threshold. 🔴 **Not the model, not the studio, not the agent.**
5. `retention-agent` drafts **non-stigmatising** outreach and coordinates across advisor /
   instructor / counsellor / financial aid — and treats each flag as a hypothesis requiring a
   confirming conversation.
6. Every intervention — date, method, response, outcome — is appended to the log. Safety and
   mental-health concerns escalate to counselling **immediately, outside the queue**.

### What the deliverable is

🟢 **Step 3 and step 6: the threshold report and the intervention log.** 🔵 The threshold report
is also the sales artefact — it is the only thing in this market that tells a provost *"at this
threshold you will contact 400 students and roughly 120 of them were never at risk"*, in
advance. 🔴 The log is what makes every later intervention auditable.

### What to check before quoting

- 🔴 **`student-signal` requires Python 3.13+** and `uv`; parts of its docs are **in Dutch**
  (`docs/aan-de-slag.md`). Budget a translation/readthrough, not a rewrite.
- 🔴 **Do not take `EWStools` as a dependency.** GPL-3.0 **only** (no "or later" bound — the
  *"any later version"* strings in its payload are How-to-Apply boilerplate), and dormant for a
  decade.
- 🟡 **The demo data is synthetic.** `data/01-raw/demo/synth_data_*.csv` proves the pipeline
  runs; it proves nothing about the client's base rates.

## P47 — The special-education documentation assistant, where the STATUTORY LAYER is now a free dependency *(new in pass 290)*

**Target:** 🇺🇸 US districts and charter networks under **IDEA 2004** and **Section 504**.
🔵 **This recipe did not exist two passes ago, and this base said so in print.**

🔴 **What `T-p288b` published at `p288`:** of the entire open source answer to IEP/504
administration — *"One copyleft, two unusable. Zero permissive. A studio taking an IEP
engagement **writes it**."* 🟢 **`p290` corrects the "zero permissive" half.**
🟡 **The "writes the application" half still stands**, and that is exactly why this is a
pattern: the dependency covers the reasoning, the deliverable is the workflow.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| statutory reasoning | [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) → `agents/special-education-agent` | 🟢 **MIT** at pinned `54ee9d91eecd` | 🟢 Its `MEMORY.md` is a **seeded statutory corpus**: IDEA 2004, **the 13 IDEA disability categories**, §504 as civil-rights law *(not special-education law)*, **FAPE/LRE**, **prior written notice**, annual review + **triennial re-evaluation**, **RTI/MTSS**, **ESY** recoupment, **age-16 transition planning**, and FERPA treatment of disability records |
| the refusal | same config, `SOUL.md` | 🟢 MIT | 🟢 *"Never make eligibility determinations — eligibility requires a qualified multidisciplinary team evaluation and legal decision"*, *"IEP decisions are made by the full team, including parents and guardians, not by any single professional or AI tool"*, and *"do not generate legal advice"* |
| drafting scope | same config | 🟢 MIT | **SMART IEP goals** (measurable, observable, standards-aligned), evidence-based accommodations by disability category, meeting agendas, **present-levels** summaries, goal-progress narratives, and a flag when a related-services evaluation (OT/PT/speech/counselling) may be needed |
| SIS + assessment | `skills/powerschool`, `skills/nwea-map`, `skills/i-ready` | 🟢 MIT adapters over 🔴 proprietary systems | present-levels and progress narratives need the assessment record, not a chat history |
| family comms | same repo → `agents/family-communication-agent` | 🟢 MIT | 🟡 The `p288` row this replaces (`hdronamraju/sped-agent`, **all rights reserved**) was valued for **bilingual EN/es parent notices**; check that requirement against this config rather than assuming it |
| 🔴 **deadline calendar + record** | **you build it** | **the client's** | 🔴 **The hard part, and it is absent** — see below |

### What the deliverable is

🔴 **The deadline engine and the documentation record.** `p288` measured this category as
*"statutory, calendar-bound and evidence-producing"*, and **the calendar is the half no MIT
component supplies.** Annual review dates, triennial re-evaluation windows, evaluation
timelines, PWN-before-change gates, ESY determinations and age-16 transition triggers are
**day-counting rules per state**. 🟢 The MIT config now knows *what the rules are*; 🔴 nothing
in it knows *what day it is for this student*, and nothing records that the team met, that the
parent was noticed, or that the notice was in the parent's language.

🔵 **So the engagement is: free statutory reasoning + a built deadline-and-evidence
system** — which is a far better quote than `p288`'s *"write all of it"*, and a far more
honest one than *"there is an open source IEP agent."*

### What to check before quoting

- 🔴 **FERPA data class.** Disability records are among the most sensitive FERPA categories, and
  the config says so itself. The host sandbox policy, the `.env` credential surface and the
  model's retention terms are **in scope before any pilot** — and a hosted model endpoint is a
  disclosure question, not an infrastructure question.
- 🔴 **State rules are not in the corpus.** `MEMORY.md` is federal. The `p288` rows that carried
  **state** rules were Colorado and California, and both were unusable
  (`AaronGrace978/EduHelp` is **AGPL-3.0**; `hdronamraju/sped-agent` is **all rights
  reserved**). State day-counting is **net new** in every engagement.
- 🟡 **It is 5 files.** Read `SOUL.md`, `IDENTITY.md`, `MEMORY.md`, `TOOLS.md` and
  `auth-profiles.json` end to end before quoting — it is a short read and it is the entire
  dependency.
- 🟢 **Person-first language is the default** in the config, with an explicit note to follow a
  student's or family's stated preference for identity-first language. Keep that behaviour;
  do not "normalise" it in a rewrite.

# Compose patterns — Education

> Concrete recipes: named repos, named licences, named wiring. Every component below was
> licence-verified from payload on 2026-10-17
> ([evidence: pass 264](../evidence/verified-repos.2026-10-17-p264.tsv),
> [pass 265](../evidence/verified-repos.2026-10-17-p265.tsv)). **P8–P10 are new in pass 265.**
> Each pattern states the licence boundary — the line the client's proprietary code must stay
> on to keep a copyleft platform from colouring the deliverable.

## 🟢 Pass 289 — the first recipe in this file whose alignment claim is CHECKABLE, and a gate that stops a restated licence shipping as a verified one

⏱️ **Eleventh pass of `2026-10-18`.** Evidence:
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv) ·
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../evidence/curriculum-authority-egress.2026-10-18-p289.tsv).

### `P43` — the curriculum-aligned tutor whose alignment is VALIDATED, not asserted

🔵 **Why this recipe did not exist before pass 289.** This base has published
*"curriculum-aligned"* for roughly 200 passes with **no alignment target in it**. An agent said
*"this lesson covers fractions at year 5"* and nothing could contradict it. Pass 289 found a
target that can.

**The licence boundary first, because it is unusual and it is split by directory:**

| component | address | grant (payload, first-hand) | boundary |
|---|---|---|---|
| curriculum graph | [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) `ontology/` `data/` `docs/` | 🔵 **OGL v3.0** — `DATA-LICENSE.md`, 2 408 B, `c117e319f357`. **`RESTATEMENT`** | commercial use **explicit**; 🔴 exemption for third-party rights is **not closable from the payload** |
| graph tooling | same repo, `scripts/` + `.github/workflows/` | 🟢 **MIT** — `CODE-LICENSE.md`, 1 491 B, `427f1d8b0cc1` | clean |
| curriculum service | [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) | 🟢 **MIT**, 1 077 B, `0eeb9d32caed` | 🔴 **code only** — *"lesson materials, videos, worksheets and quizzes are not covered"* |
| agent edge | [`oaknational/oak-ai-plugins`](https://github.com/oaknational/oak-ai-plugins) | 🟢 **MIT**, 1 085 B, `e90b3e1c8e94` | clean |
| SDK + MCP | [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT**, 1 086 B, `02c5a8e84229` | ⚠️ **API key required** (free, on request); **no external PRs accepted** |
| the agent | client code | proprietary | stays proprietary — nothing above is copyleft |

**The wiring, in the order it must be built:**

1. **Pull the graph, not the media.** Clone `oak-curriculum-ontology` and load
   `data/` + `ontology/` — Turtle, JSON-LD, RDF/XML, N-Triples, SQLite or property-graph
   JSONL. 🔵 **Take the SQLite build for a pilot**: 50 948 key learning points, 11 207
   misconceptions, 7 432 prerequisite edges, 160 progression threads, 12 subjects, queryable
   with no triplestore to operate.
2. **Make "aligned" a validation, not a claim.** The repo ships **38 SHACL shapes**. The agent
   emits a *proposed* lesson plan carrying the key-learning-point IRIs it claims to cover;
   the pipeline validates that against the shapes. **A plan that does not validate does not
   reach a teacher.** This is the step that distinguishes `P43` from every prior tutor recipe
   in this file.
3. **Use the prerequisite edges as the tutor's actual policy.** 7 432 prerequisite relations
   and 160 progression threads are a ready-made curriculum ordering. Remediation becomes a
   **graph walk backwards** from the failed objective, not a prompt asking the model what
   comes first.
4. **Mine the misconceptions as assessment distractors.** 11 207 recorded misconceptions are
   the highest-value and least-replicable asset in the corpus: generating *plausible wrong
   answers* is exactly what a model does badly and what this graph already contains.
5. **Reach live content through MCP**, not by vendoring: `mcp.thenational.academy/mcp` (public
   beta) plus the TypeScript/Zod SDK. Own the client; do not fork the platform — the repo takes
   no external PRs.
6. 🔴 **Emit BOTH attribution strings** (see `P44`; the payload prescribes two and says which
   discharges it nowhere).
7. 🟡 **Clear the media per engagement.** Ship the **graph**; treat lesson videos, worksheets
   and quizzes as out of scope until cleared — the API's own `LICENSE` excludes them and OGL
   exempts third-party rights Oak cannot license.

**Where this is sellable:** 🇬🇧 **England first** — the only jurisdiction in this base whose
curriculum is ceded with commercial use explicit. 🔵 The *pattern* ports anywhere a ministry
publishes curriculum as data; the *corpus* does not port, because the grant is national.

---

### `P44` — the licence-provenance gate: stop a RESTATED grant from shipping as a VERIFIED one

🔴 **The failure this prevents, and it is one line in a deliverable.** A build pulls a
curriculum corpus, a scanner reports *"OGL-3.0 — permissive, commercial use allowed"*, and the
compliance file says the grant was verified. **It was not.** The payload was the licensee's
**paraphrase**; the authoritative text lives on a third-party host, and in this environment
**12 of 12** licensing authorities are unreachable. `p742` grades that payload `GRANTED`, and
so does every off-the-shelf licence scanner.

**The wiring:**

1. Vendor [`compose/code/p289-restatement-authority/`](code/p289-restatement-authority/README.md)
   into the client's CI (**40 controls**, no network needed for the suite).
2. On every dependency carrying a licence payload, run `classify_payload()`:
   **`AUTHORITATIVE-BODY`** → the body travels with the clone, nothing more owed.
   **`RESTATEMENT`** → the real text is elsewhere; record the authority host.
   **`BARE-REFERENCE`** / **`NO-GRANT`** → **stop the build**.
3. For each `RESTATEMENT`, probe its authority host and pass the **measured** result to
   `posture()`. Reachable → `VERIFY` (diff the restatement against the authority and keep the
   diff). Unreachable → `USE-WITH-RECORDED-BOUND`. Nobody probed → `UNPROBED`.
   🔵 **The posture is a property of the environment, not of the repository** — the same payload
   grades differently behind a different egress policy, which is exactly the fact a compliance
   file should carry and normally loses.
4. Run `attribution_verdict()`. **`DISAGREEMENT` means the payload prescribes two different
   obligations**, and the build emits **both**:

   ```
   Contains public sector information licensed under the Open Government Licence v3.0.
   Oak National Academy
   ```

   🔴 Both Oak OGL payloads do this. Crediting *"Oak National Academy"* alone — the form the
   friendly summary asks for — **does not meet the condition the same file states 35 lines
   above it**.
5. Run `body_vs_summary_attribution()`. **3 of 3** Oak licence files with a summary block state
   the obligation differently there than in their terms. 🔵 **Gate the summary, because the
   summary is what a human reads.**
6. Run `self_description_verdict()`. `LICENSE.md` advertises `DATA-LICENSE.md` as the
   *"Full OGL 3.0 License"*; it is a restatement → **`OVERSTATED`**. A file's claim about itself
   is not evidence about itself.

**What the client gets:** a compliance file that distinguishes *"we read this grant"* from
*"we read someone's description of this grant and here is the host we could not reach"* —
and the attribution strings, emitted by the build rather than remembered by a developer.

## 🟢 Pass 288 — two recipes for the shape this pass actually found: a platform you can REACH but not VENDOR, and a compliance design that exists only in unusable code

⏱️ **Tenth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p288.tsv`](../evidence/verified-repos.2026-10-18-p288.tsv) ·
[`p288-readme-channel.2026-10-18-p288.tsv`](../evidence/p288-readme-channel.2026-10-18-p288.tsv).

### `P41` — Blackboard Learn agent reach, where every community server is a dead end

🔴 **The licence boundary first, because it is the whole reason this recipe differs from
`P12`'s Moodle/Canvas shape.** All three community Blackboard MCP servers are unusable as
dependencies:

| component | verified grant | may the studio ship it? |
|---|---|---|
| [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) | 🔴 **NONE_IN_TREE** across 9 files, 55 paths × 2 refs → 404. `readme.md` **claims MIT** | 🔴 **No.** The claim is an **ASK** — request a licence payload from the author before any use |
| [`yoyoconnor/BlackboardMCP`](https://github.com/yoyoconnor/BlackboardMCP) | 🔴 **NONE_IN_TREE** across 9 files; `pyproject.toml` has no `license` key | 🔴 **No.** Read as a **design reference** only |
| [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) *(already carried)* | see its carried row | 🟡 Check its row before use; RBAC middleware is its distinguishing feature |

🟢 **So the wiring owns the server and borrows nothing:**

1. **Surface** — the **Blackboard Learn REST API**. This is the stable, documented, vendor-owned
   contract and the only part of this stack that is not a 9-file community wrapper.
2. **Server** — write a **thin MCP server** the studio owns outright. Scope it read-only first,
   exactly as `yoyoconnor/BlackboardMCP` does by design (*"it never submits, posts or changes
   anything"*): courses, class times, assignments, grades, course materials.
3. **Authorization** — copy the posture from Open edX's plugin
   ([`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp), 🟡 **AGPL-3.0**, carried):
   **re-check the platform's own staff/superuser flags live on every request; never cache a
   role.** 🔵 Reading that plugin for its *posture* is fine; linking its AGPL-3.0 code into a
   proprietary deliverable is not.
4. **RBAC** — role-based access control at the tool boundary, per `nitsuah/bb-mcp`'s approach,
   so a student-scoped session cannot reach instructor-scoped tools.
5. **Audit** — log *who asked what*, because under `T-p288a` that log is half the human-oversight
   evidence an EMEA high-risk deployment has to produce.

🔴 **The trap this recipe exists to prevent:** `bbmcps` is discoverable, small, reads as
finished, and a secondary listicle reports it as **"MIT License"**. The MIT exists **only in its
`readme.md` sentence and in that listicle — never in a payload.** 🔵 And it is served at
**lower-case `readme.md`**, 404 at the upper-case spelling on every ref, which is how this pass
nearly recorded it as having no README at all.

### `P42` — a grader that is shippable in all four regions, assembled from a design this pass could not license

🔵 **The requirement comes from [`intel/trends.md`](../intel/trends.md) `T-p288a`:** a recorded
human decision point plus provenance marking clears Vietnam's sole-basis clause, Korea's marking
duty, the EMEA high-risk tier and the Oklahoma/Maryland oversight rules **in one build**.

🔴 **Licence boundary:** the reference implementation,
[`arijit8972/agentic-automated-assignment-grading`](https://github.com/arijit8972/agentic-automated-assignment-grading),
serves **no grant** — **1 531 files**, and its **66** licence-like paths are **all vendored
`ui/node_modules/**`**, which is `p280`'s class, not a grant. 🟢 **Read it, do not vendor it.**
For the parts that must be real dependencies, use rows this base has already payload-verified
(`asu2304/auto-assessment-agent`, `laurauguc/grading_assistant` — both carried, both MIT per
their carried rows; re-read the row before shipping).

🟢 **Wiring:**

1. **Intake** — accept PDF, image, plain text and DOCX; batch a whole class against one rubric.
2. **Criterion-level scoring** — score **per rubric criterion**, with the evidence span that
   produced each score attached. An aggregate grade with no per-criterion evidence cannot be
   defended to a parent or an auditor.
3. **Confidence + disagreement flags** — raise a flag on evaluation errors, low confidence, and
   disagreement between evaluators. 🔵 Copied from the reference implementation's design.
4. 🟢 **The `needs_review` terminal state — THE compliance artefact.** A flagged submission
   still produces a report, and **its feedback is marked `draft`**. The grade is *not* released
   on the model's say-so. **This is the sole-basis clause satisfied in code**, not in a policy
   document.
5. **Provenance marking** — mark every generated artefact as AI-generated (Korea's Framework Act
   makes this an explicit duty; nothing else in this stack is harder to retrofit later).
6. **Audit record** — persist who reviewed, when, and what they changed, so the human decision
   point is *evidenceable* and not merely *present*.

🔴 **Do not skip step 4 to ship faster.** It is the single step that distinguishes a grader that
is legal in Vietnam, Korea and the EU from one that is not, and it costs a state field and a
release gate.

## 🟢 Pass 287 — the binding constraint in a tutoring deliverable is the CURRICULUM'S licence, and no recipe below had a row for it

⏱️ `2026-10-18`, ninth pass. Evidence:
[`verified-repos.2026-10-18-p287.tsv`](../evidence/verified-repos.2026-10-18-p287.tsv) ·
[`p287-websearch.2026-10-18-p287.tsv`](../evidence/p287-websearch.2026-10-18-p287.tsv).

🟢 **New pattern `P40` — the two-corpus tutor.** Every recipe in this file prices the **code**
licence of its components, which is what 287 passes of instrument work have been for.
🔴 **`p287` read a working project's own content audit and found the constraint that actually
decides a paid tutoring deliverable, and it is not a code licence at all:**
[`avps82/mentar`](https://github.com/avps82/mentar)'s `docs/CONTENT_LICENSES.md` clears its
Khan Academy grounding corpus (`CC BY-NC-SA`) for *"the **non-commercial** local pilot"* and
states it 🔴 ***"does NOT clear the Phase-3 paid hosted tier."***

🔵 **A Globant deliverable is paid by construction**, so the pilot corpus and the shippable
corpus are **different corpora** — and the platform's own licence does not change between those
two phases while the content's obligations do all the work. `P40` makes that split a
configuration boundary instead of a discovery.

🟢 **The second half of the same finding**: `mentar`'s country strategy
(`AU = ACARA (CC BY)`, `IN/SG/US = GENERIC packs (no claimed alignment)`) shows that
**"curriculum-aligned" is claimable only where the curriculum itself is openly licensed.**
🔴 This base has read **one** national curriculum licence first-hand. `P40` step 4 therefore
scopes a **research task** per engagement rather than a lookup, and
[`intel/trends.md`](../intel/trends.md) `T-p287a` ranks reading five ministry licences for
`p288`.

🔵 **Why this belongs in `compose/` and not only in `intel/`:** the remedy is a *wiring*
decision with a deadline. Keep `libzim` (GPL-3.0-or-later) an **optional** extra with lazy
imports and the core stays permissive; make it core and the combined distribution must go
copyleft. 🟢 **`mentar` documents making exactly that change, with dates** — one dependency's
placement decided the licence of the whole deliverable, and it is the cheapest high-stakes
decision in the build.

## 🟢 Pass 283 — every component address in every recipe below is now PROVEN distinct

⏱️ `2026-10-18`, fifth pass. Evidence: [`p283-websearch.2026-10-18-p283.tsv`](../evidence/p283-websearch.2026-10-18-p283.tsv) · [`repo-identity.2026-10-18-p283.tsv`](../evidence/repo-identity.2026-10-18-p283.tsv).

🔴 `p282` found **six recipes in this file** wiring together `ls1intum/Iris` and `ls1intum/Pyris` —
**one repository under two names**. A delivery team following any of those six would have scoped an
integration between a component and itself. All six were corrected by hand.

🟢 **`p283` turns that hand-check into a standing one.** `make gate-identity` is in `make hooks`,
and its online half resolved **138 live addresses across the three component shelves to 138 distinct
HEADs, 0 collisions, 0 unreachable**. 🔵 **Every repo named in P1–P10 below is a distinct
repository**, and a later pass cannot reintroduce the defect without the gate going red.

🔴 **One caveat a recipe author must keep.** The gate proves *distinctness of address*, not
*independence of component*. `ls1intum/Artemis` and `ls1intum/Pyris` are genuinely two repositories
and Pyris is still the AI layer *inside* Artemis; composing them is one deployment, not two
integrations. **Distinct HEAD is a floor, not an architecture.**

## P1 — Teacher co-pilot for a national AI-literacy mandate
**Target:** India (Class 3 mandate, AY 2026-27), Mexico (SEP teacher formation), Brazil (MEC basic-education guidance)
**Timeline:** 8–10 weeks to a measurable pilot

```
[instructional_agents  MIT]   multi-agent ADDIE: syllabus -> LaTeX slides -> assessments
        |                      roles: Teaching Faculty / Instructional Designer / TA / Coordinator
        v
[Claw-ED  MIT]                teacher edits and approves before anything reaches a student
        |                      (local-first: curriculum never leaves the institution)
        v
[lineage-skill  Apache-2.0]   every generated artefact stays tied to its source document
        |
        v
[Moodle  GPL-3.0]  <--LTI--  [tsugi  Apache-2.0]      delivery into the installed base
        |
        v
[pykt-toolkit  MIT]           did the teacher formation move learner outcomes?
```

**Wiring:** run `instructional_agents` in its Feedback-Guided mode so a human is in the loop
by construction, not by policy. Deliver through `tsugi` as an LTI 1.3 tool — the agent code
stays MIT/Apache-2.0 and never links against Moodle's GPL.
**Licence boundary:** LTI launch. Everything studio-built sits on the permissive side.
**Why it sells:** three governments are funding exactly this, and
[`intel/market.md`](../intel/market.md) shows Mexico's gap quantified at 76%-vs-36%.

## P2 — Compliant tutoring for the EU AI Act window
**Target:** EMEA higher education and vocational training
**Timeline:** 10–12 weeks; must land before **2027-12-02**

```
[DeepTutor  Apache-2.0]              persistent student model, multi-agent tutoring
        |
        +-- served by --> [Ollama / vLLM, self-hosted]   no prompt leaves the member state
        |
        v
[OpenOLAT  Apache-2.0]  or  [Artemis  MIT]   EMEA-origin, permissive platform
        |
        v
[lrsql  Apache-2.0]  +  [xAPI-Spec  Apache-2.0]   auditable record of every AI interaction
        |
        v
[Moodle 5.1 per-course/per-activity AI toggles]   where Moodle is the installed base
```

**Wiring:** two obligations, two mechanisms. **Transparency (live since 2026-08-02):** an
explicit AI-disclosure interstitial on every `DeepTutor` session entry, logged as an xAPI
statement into `lrsql` so disclosure is provable, not asserted. **High-risk (from
2027-12-02):** any function that determines access, assesses outcomes or influences an
educational path routes through a human-decision step — `DeepTutor` proposes, a named
educator disposes, and `lrsql` holds both records.
**Licence boundary:** the whole stack is Apache-2.0/MIT. Deliberate: an AI Act technical
file is easier to assemble when no component carries network copyleft.
**Why it sells:** the delay created a 14-month window and most clients will read it as a reprieve.

## P3 — Dropout early-warning for a LATAM public university
**Target:** Brazil, Mexico, Colombia, Argentina — Moodle/Chamilo installed base
**Timeline:** 6–8 weeks

```
[Moodle  GPL-3.0]  /  [Chamilo  GPL-3.0]        activity logs, grades, submissions
[academico  MIT]  /  [GibbonEdu  GPL-3.0]       enrolment, attendance, demographics
        |
        v
[lrsql  Apache-2.0]                             one event stream, xAPI vocabulary
        |
        v
[pyedmine  MIT]  or  [pykt-toolkit  MIT]        knowledge tracing + cognitive diagnosis
        |                                        [EduData  Apache-2.0] for baselining
        v
[risk scores + next-best-action]
        |
        v
[Moodle block via tsugi  Apache-2.0]            advisor dashboard, inside the LMS they use
```

**Wiring:** pull through Moodle's REST API into `lrsql` — never read the LMS database
directly, or the integration dies at the next platform upgrade. Train with `pykt-toolkit`'s
standard splits so the accuracy claim is comparable to published baselines instead of
self-graded. Use `pyedmine` when the client wants a recommendation, not just a prediction.
**Licence boundary:** REST + LTI. No studio code links to GPL internals.
**Why it sells:** Brazil's digital-sovereignty framing makes self-hosted inference the
policy-preferred architecture, not the budget option.

## P4 — Education skill pack for a client's existing assistant
**Target:** any region; clients who already run an AI assistant
**Timeline:** 3–4 weeks

```
[Bloom  MIT]                             adaptive tutoring skill
[universal-diagnostic-tutor-skill  MIT]  diagnose the misconception first
[universal-examprep-skill  MIT]          teach from the client's own slides, page-cited
[anki-mcp-server  MIT]                   spaced repetition behind MCP
[tutor-mcp  MIT]                         tutoring loop behind MCP
        |
        v
[client's assistant]  -- MCP -->  [institutional content + Anki decks]
```

**Wiring:** ship skills, not an application. The MCP servers expose the institution's
content and the learner's review schedule; the skills carry the pedagogy. `fsrs4anki` (MIT)
or `fsrs-rs` (BSD-3-Clause) supplies the scheduler so retention is managed by a real
algorithm rather than a prompt.
**Licence boundary:** every component MIT or BSD-3. Nothing to negotiate.
**Why it sells:** this is **T2** in [`intel/trends.md`](../intel/trends.md) — the fastest-moving
shape in education open source, and the cheapest engagement to start.
**Avoid:** `education-agent-skills` (873 stars) is **CC-BY-SA-4.0**. Superb reference,
ShareAlike on derivatives — read it, do not vendor it into a proprietary pack.

## P5 — Integrity-first assessment where student-facing AI is restricted
**Target:** US states barring AI from high-stakes decisions (OK, MD), NYC K-8 moratorium districts
**Timeline:** 6–8 weeks

```
[Artemis  MIT]              programming/modelling/text exercises, automated FEEDBACK
        |                    (feedback, explicitly not autonomous grading)
        v
[dolos  MIT]                source-code plagiarism detection across submissions
        |
        v
[Numbas  Apache-2.0]        randomised maths assessment; SCORM-packaged output
        |
        v
[scorm-again  MIT]          runs that SCORM inside the institution's existing LMS
        |
        v
[teacher sign-off]  ------>  grade of record
```

**Wiring:** the architecture encodes the regulation. No AI output becomes a grade without a
named educator's action; `Artemis` produces feedback and evidence, the teacher produces the
grade. `Numbas` randomisation means per-student variants, which is integrity by design
rather than detection after the fact.
**Licence boundary:** fully permissive, and `scorm-again` keeps legacy content in place —
no content migration in the SOW.
**Why it sells:** in restricted jurisdictions this is the AI story that is unambiguously
permitted (see **T8**).

## P6 — AI-native corporate L&D, no LMS legacy
**Target:** enterprise L&D, North America and EMEA
**Timeline:** 5–7 weeks

```
[mentingo  MIT]                      AI-native LMS: AI mentor w/ voice role-play + auto-scoring,
        |                             AI course builder (policy docs -> structured courses),
        |                             open-ended answer grading, bring-your-own-key
        +-- traces --> [Langfuse]     cost, latency and mentor output, per call
        +-- exposes --> [MCP]         the client's assistant can drive the LMS
        |
        v
[fsrs4anki  MIT]                     spaced repetition for compliance-knowledge retention
        |
        v
[lrsql  Apache-2.0]  + [xAPI-Spec]   completion and competency evidence for audit
```

**Wiring:** feed existing policy and knowledge-base documents into the AI course builder,
then use role-play scenarios for compliance and sales enablement with auto-scoring as
formative — never summative — signal. Langfuse tracing gives the client per-call cost
visibility from day one, which is usually the first question procurement asks in month two.
**Licence boundary:** MIT throughout.
**Why it sells:** retrofitting Moodle for corporate L&D costs more than starting on a base
that already has the agent, the tracing and the MCP endpoint.

## P7 — Sovereign tutoring deployment, air-gapped
**Target:** Brazil (MEC digital sovereignty), EMEA public sector, defence/government training
**Timeline:** 8–10 weeks

```
[Open TutorAI CE  BSD-3-Clause]      multimodal tutoring: voice, video, 3D avatars, Docker-first
        |
        +-- inference --> [Ollama / vLLM on-premise]    no external API
        v
[OpenOLAT  Apache-2.0]               Apache-2.0 LMS: no copyleft anywhere in the stack
        |
        v
[lrsql  Apache-2.0]                  all records on-premise
```

**Wiring:** every component runs inside the perimeter and the entire stack is
permissive — which matters when a government client wants to audit, modify and redistribute
internally without GPL obligations following the artefact. Open TutorAI's avatar and voice
layer is the differentiator where face-to-face interaction is culturally expected.
**Licence boundary:** none to manage. That is the point of this pattern.
**Why it sells:** Brazil's MEC *Referencial* asks for national solutions reducing dependence
on global platforms. This is that, literally.

## P8 — Sovereign agentic layer over Brazil's municipal school stack
**Target:** Brazilian municipal and state education networks (SME/SEDUC)
**Timeline:** 8–10 weeks to a pilot in one network
**Why it exists:** this is the pattern pass 264 could not write, because it had not found a
LATAM-origin base.

```
[i-educar  GPL-2.0]        enrolment, attendance, grades, the municipal system of record
   (portabilis, BR)        origin: prefeitura de Itajai-SC -> Portal do Software Publico, 2008
        |  \                last commit 2026-10-14, 34,948 commits
        |   \__ teachers __> [i-diario  AGPL-3.0]   portal do professor (payload is pt-BR AGPL)
        |
        |  === LICENCE BOUNDARY: HTTP / LTI 1.3. Nothing below links against the above. ===
        v
[tsugi  Apache-2.0]        LTI 1.3 tool; the studio's deliverable starts here
        |
        v
[DeepTutor  Apache-2.0]    tutoring, persistent student model
[instructional_agents MIT] teacher materials, ADDIE pipeline
        |
        +-- served by --> [Ollama / vLLM, on-premise]   no student prompt leaves the municipality
        |
        v
[pyedmine  MIT]            dropout / at-risk modelling on i-Educar's attendance + grade history
        |
        v
[lrsql  Apache-2.0] + [xAPI-Spec  Apache-2.0]   audit trail for PL 2338 high-risk classification
```

**Wiring:** read i-Educar through its API/database views, never by patching it — GPL-2.0 is a
distribution licence and an unmodified upstream keeps the municipality's upgrade path intact.
Teacher-facing output surfaces in i-Diário, which teachers already open daily; student-facing
output goes through an LTI launch. Attendance plus grade history in i-Educar is exactly the
feature set `pyedmine` needs, so the dropout model has training data on day one instead of
after a year of instrumentation.
**Licence boundary:** the HTTP/LTI line. i-Educar stays GPL-2.0 and unmodified, i-Diário stays
AGPL-3.0 and unmodified, everything studio-built is MIT/Apache-2.0.
**Legal note:** i-Diário's licence payload is a **Portuguese translation** of AGPL-3.0; FSF
translations are unofficial. Cite the English AGPL-3.0 in the SOW.
**Why it sells:** MEC's *Referencial* (March 2026) asks for national solutions that reduce
dependence on global platforms. A Brazilian-maintained base with federal software-public
provenance, local inference and an auditable record is not an interpretation of that policy —
it is the policy, implemented. And `PL 2338` would classify education-related **selection** as
high-risk, so the xAPI trail is built before the law needs it, not after.

## P9 — Offline-first tutoring where there is no network
**Target:** rural LATAM, low-bandwidth APAC, anywhere power and connectivity are intermittent
**Timeline:** 6–8 weeks to a device-level pilot

```
[Kolibri  MIT]                     complete learning platform that runs with NO network
  (learningequality)               content channels sync opportunistically when a link appears
        |                          39,803 commits; MIT - no copyleft anywhere in this stack
        v
[local quantised model via Ollama]  tutoring and explanation on-device
        |                           (DeepTutor's prompting patterns, Apache-2.0, as the design
        |                            reference - its orchestration assumes a server; do not
        |                            port it wholesale onto a classroom device)
        v
[fsrs-rs  BSD-3]  /  [fsrs4anki  MIT]   retention scheduling that needs no server at all
        |
        v
[xAPI statements buffered locally] --sync-on-contact--> [lrsql  Apache-2.0]  central reporting
```

**Wiring:** every component assumes absence of network as the default state, not as an error.
Kolibri handles content distribution and sync; FSRS schedules review entirely locally (it is
an algorithm, not a service); xAPI statements queue on device and drain when a link appears.
The model is the only part that needs sizing care — budget the device class first and choose
the quantisation to fit it, because this is the one pattern where the hardware is the
constraint rather than the licence.
**Licence boundary:** none. MIT, BSD-3 and Apache-2.0 end to end.
**Why it sells:** it is simultaneously the answer to *"our schools lose connectivity"* and to
*"no student data may leave the premises"* — and nothing leaves the device, so the
data-protection conversation (LGPD, GDPR, state privacy statutes) is short. Note what it is
**not**: a frontier-model experience. Say that up front.

## P10 — Permissive autograding where AI is barred from the grade
**Target:** US states barring AI from high-stakes decisions (Idaho, Oklahoma, NYC K-8), EU
institutions under Annex III, Brazilian institutions ahead of `PL 2338`
**Timeline:** 4–6 weeks

```
[Autolab  Apache-2.0]        auto-graded programming assignments + course management (CMU)
   or
[nbgrader  BSD-3-Clause]     assign and grade notebooks (the data-science department's default)
   or
[Artemis  MIT]               automated FEEDBACK with an auditable exercise runner (TUM)
        |
        |   the grade is produced DETERMINISTICALLY, by a test suite, not by a model
        v
[teacher sign-off step]      explicit, logged, reversible
        |
        +--- optional, on the feedback side only ---> [LLM explains WHY a test failed]
        |                                              never proposes or alters the mark
        v
[dolos  MIT]                 integrity check on submissions
        |
        v
[lrsql  Apache-2.0]          who decided what, when - the record a regulator asks for
```

**Wiring:** the architectural claim is the separation. Marks come from a deterministic runner;
the model only ever produces explanation text attached to an already-computed result, and the
human sign-off is a logged state transition rather than a UI affordance. That makes "AI did not
make a decision about a student" demonstrable from the audit log instead of asserted in a
policy document.
**Licence boundary:** none to manage — Apache-2.0, BSD-3 and MIT throughout. `INGInious`
(AGPL-3.0) is the substitute where UCLouvain's feature set is wanted and AGPL is acceptable.
**Why it sells:** it is the one AI story that is unambiguously permitted in the jurisdictions
tightening fastest, it is cheaper than an LLM grader, and it gets *more* defensible as
regulation increases rather than less.

🔴 **`p284` — the scope limit this pattern did not state: a test suite cannot grade prose.**
Everything above is for programming, notebook and modelling work; it has **nothing to offer essay
marking**, which is the workload a secondary teacher actually carries. 🟢 And the conservatism here —
*"the model only ever produces explanation text … never proposes or alters the mark"* — is now
**stricter than at least one regulator requires**: Brazil's MEC, amending `Parecer CNE/CP nº 15/2026`
before homologation, **permits AI as a `primeiro filtro` that proposes** in essay correction and
forbids only the **assignment of the mark** and the approval/failure decision. 🔵 Use this pattern
where the grade can be **computed**; use **`P37`** where it cannot. The boundary between the two is
**not** regulatory — it is whether the artefact being assessed is executable.

## P11 — Agent layer over India's national stack (MIT end-to-end, no copyleft anywhere)

**When:** an APAC public-sector engagement — a state education department or ministry — that
already runs **DIKSHA** or a Sunbird-derived platform. **Do not propose a migration.**

**Why it wins:** the platform, the content pipeline and the political precedent exist. The
engagement is the agent layer on top, and every component is permissive, so there is **no
copyleft obligation anywhere in the stack** — the only pattern in this file with that property.

```
Sunbird-Ed/SunbirdEd-portal        MIT    national platform (38,046 commits)
project-sunbird/knowledge-platform MIT    content/knowledge backend  <-- integrate HERE
Sunbird-Ed/SunbirdEd-mobile-app    MIT    mobile client
  |
  +-- ls1intum/Pyris               MIT    LLM microservice (REST, swappable pipelines)
  |     +-- ls1intum/Pyris         MIT    tutor: hints and leading questions, not answers
  |              ("Iris" is the tutor's USER-FACING name; the repo is Pyris — p282)
  +-- numbas/Numbas                Apache-2.0  assessment, executes in-browser
  +-- pykt-team/pykt-toolkit       MIT    learner model over Sunbird telemetry
  +-- yetanalytics/lrsql           Apache-2.0  xAPI Learning Record Store
```

**Wiring, concretely:**
1. Integrate at the **`knowledge-platform` API**, not in the portal UI. The portal is the piece
   a ministry has customised and will keep customising; the backend API is stable.
2. Stand up **Pyris** as a separate service and point it at the content store. Pyris already
   exposes swappable LLM pipelines and RAG over instructor material, so bring-your-own-model
   (including a locally hosted one) is configuration, not code.
3. Emit **xAPI** statements to **lrsql** for every tutor interaction. This is what makes the
   learner model trainable later and the deployment auditable now.
4. Attach **Numbas** for assessment. Browser-side execution means submissions need not leave the
   device — carry that into the data-protection annex explicitly.
5. Fit **pykt-toolkit** on the accumulated telemetry only once there is enough of it. Do not
   promise a learner model in phase 1; promise the instrumentation that makes one possible.

**Licence posture to put in the SOW:** MIT / MIT / MIT / MIT / Apache-2.0 / MIT / Apache-2.0.
Nothing here triggers source disclosure, including on a hosted deployment.

**Slug caution:** `Sunbird-Ed/sunbird-ed-portal` **does not resolve**. The live slugs are
camel-case (`SunbirdEd-portal`, `SunbirdEd-mobile-app`).

---

## P12 — Declassify-by-design assessment for Vietnam's 2027 deadline

**When:** an APAC engagement touching **automated assessment** or any form of student
**behavioural monitoring**, in Vietnam or any jurisdiction converging on the same test (see T17).

**The governing fact** ⚠️ *(secondary-source grade)*: Vietnam's July 2026 decision makes these
uses high-risk **only where the AI output is the sole basis for a decision without meaningful
human review.** Compliance **2027-03-01**; **+6 months** if the system was live before
**2026-08-15** — so an education system already running on that date has until **2027-09-01**
*(Law `134/2025/QH15`'s 18-month transition for pre-existing healthcare, education and finance
systems; adjudicated across four publishers in [`intel/open-gaps.md`](../intel/open-gaps.md), and
restated by `p281`'s APAC leg as a third independent source)*.

🔴 **The counter-intuitive consequence, and it decides sequencing:** a **later-launched** education
system has the **earlier** deadline. Replacing a legacy Vietnamese system therefore moves a client
from the **September 2027** rung to the **March 2027** rung — so a migration that looks like
modernisation buys six months *less* runway, not more.

**So the deliverable is not a compliance document — it is an architecture that stays out of the
high-risk class.**

```
ls1intum/Artemis            MIT   assessment platform, human-in-the-loop by construction
  +-- ls1intum/Athena       (!!)  feedback SUGGESTED to instructor, never applied to student
  +-- ls1intum/Pyris        MIT   tutor ("Iris") : hints only, no grading authority
  +-- ls1intum/Pyris        MIT   LLM microservice; swap to a local model for data residency
  +-- config gate           ----  every AI subsystem independently switchable OFF
  |
  +-- yetanalytics/lrsql    Apache-2.0  immutable xAPI record of who decided what, and when
```

**The four build rules that do the legal work:**
1. **Athena suggests; an instructor disposes.** No code path applies a model-generated grade to
   a student record. This is the single requirement that keeps the system out of the high-risk
   class under Vietnam's carve-out, Oklahoma's `SB 1734` and Maryland's rule alike.
2. **Config-gate every AI subsystem.** Artemis already does this. It means "AI was off for this
   cohort" is a verifiable configuration claim, not a promise.
3. **Log the human decision, not just the model output.** `lrsql` holds an xAPI record showing a
   named human reviewer and a timestamp per decision. "Meaningful human review" is an evidentiary
   claim; without a log it is unprovable.
4. **Keep the model swappable** via Pyris, so a data-residency or sovereign-hosting requirement
   is a configuration change rather than a re-platforming.

⚠️ **Two cautions, stated plainly.** (a) **`ls1intum/Athena` serves no licence payload** — marked
`(!!)` above. Artemis's MIT grant does **not** automatically extend to it. Resolve the licence in
writing with TUM before Athena ships in a deliverable, or implement the feedback-suggestion step
yourself against Pyris. (b) The Vietnam dates **conflicted across sources** this pass and could
not be confirmed against the primary decision text; confirm before contracting to a deadline.

---

## P13 — Governance retrofit for a LATAM university that already adopted AI

**When:** the 87%-adopting / 26%-governed institution ⚠️ described in T16 — which is most of
LATAM higher education. The client has AI in use across faculties and **no strategy, inventory
or review process.** No platform displacement is required, which is why this sells.

**This pattern is deliberately mostly not software.** Writing code first is the standard mistake
here; the deliverable is governance *with* instrumentation, in that order.

```
Phase 1  Inventory        what models, in whose hands, on whose data
         +-- dodona-edu/dolos        MIT   integrity baseline on existing submissions
Phase 2  Policy           AI-use policy, human-review rules, assessment-integrity standard
         +-- aligned to: UNESCO IESALC guidance; Brazil MEC referencial; PL 2338 (high-risk
             education-related selection) if the client is Brazilian
Phase 3  Instrumentation  make the policy observable instead of aspirational
         +-- yetanalytics/lrsql     Apache-2.0  xAPI record store
         +-- adlnet/xAPI-Spec       Apache-2.0  the vocabulary
Phase 4  Controlled pilot one faculty, one use case, measured
         +-- ls1intum/Artemis       MIT   if assessment; config-gated AI
         +-- ls1intum/Pyris         MIT   if tutoring; local model where data cannot leave
Phase 5  Learner model    only once phases 1-4 produce trustworthy data
         +-- pykt-team/pykt-toolkit MIT
```

**Why this order and not the reverse:** a learner model built on ungoverned data inherits every
consent and integrity defect in the institution. Phase 5 is where the client *wants* to start
and where the engagement should finish.

**Entry points that are real convening bodies, not citations:** UNESCO's **Observatory on AI in
Education for LAC** (launched 2026-04-14, Santiago, at ECLAC), **UNESCO IESALC**, **Ceibal**
(Uruguay), and the **ILIA** index. The public/private split ⚠️ (**68%** public vs **84%** private
non-profit) says the public sector is the larger gap and the slower sale — staff accordingly.

**Do not** brief [`guedesindev/ai_tutor_forge`](https://github.com/guedesindev/ai_tutor_forge)
as regional capability. It is GPL-3.0, 18★, 21 commits — a personal project, and the only
Portuguese-language education agent this base has verified.

---

## P14 — An agent inside the Canvas the client already runs, with an MIT-only deliverable *(new in pass 267)*

**When:** the client runs **Canvas** — the dominant LMS in North American higher education — and
wants an AI layer over *their* courses, rosters, assignments and grades. The most common NA
situation in this KB, and until pass 267 it had no pattern, because this base believed Canvas was
closed SaaS. It is **AGPL-3.0 with 78,765 commits**.

```
Client's existing system  instructure/canvas-lms         AGPL-3.0   DO NOT FORK. Do not link.
         |                                                          78,765 commits; the network
         |                                                          clause is the only reason you
         |                                                          stay out -- not access.
         | Canvas REST API  (process boundary = licence boundary)
         v
Doorway   vishalsachdev/canvas-mcp      MIT   295*, 1,026 commits, v1.14.0 (Oct 2026)
          +-- 102-126 tools + 8 agent skills; courses, assignments, grades, roster
          +-- speaks MCP to Claude / Cursor / Codex / 40+ clients
         |
         v
Pedagogy  ls1intum/Pyris                MIT   LLM microservice: exercise feedback, RAG over
          |                                   instructor-supplied course material
          +-- ArnaudGuiovanna/tutor-mcp  MIT   when a constrained tutoring loop is enough
          +-- ls1intum/Pyris             MIT   hints and leading questions, not answers
         |
         v
Grading   Submitty/Submitty             BSD-3  submission + autograde + TA workflow
          +-- ucbds-infra/otter-grader  BSD-3  Python AND R; ships a CANVAS AUTOGRADER ADAPTER
          +-- jupyter/nbgrader          BSD-3  notebook courses
         |
         v
Audit     yetanalytics/lrsql            Apache-2.0  xAPI record of every AI interaction
          adlnet/xAPI-Spec              Apache-2.0  the vocabulary
```

**The licence argument, which is the point of the pattern:** every component you deliver is **MIT,
BSD-3 or Apache-2.0**. The only copyleft artefact in the system is **Canvas itself, which the
client already owns and operates**. You call its REST API across a process boundary and never link
its code, so nothing in the deliverable derives from an AGPL work — a sentence the client's legal
team can verify in an afternoon. **AGPL platform, MIT doorway.**

**Sequence that avoids the usual failure:** stand up `canvas-mcp` read-only against a sandbox
course first and prove the tool surface, *then* enable writes. Count the tools you actually
register — the project publishes **102 in its About blurb and 126 in its README**, and the default
profile registers fewer than either. Quote the range to the client, never a single number.

**Where the client runs Moodle instead:** the doorway is
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) — **AGPL-3.0,
open-core (premium tools sold separately), 10 free tools, 1★, 57 commits** — or a direct build
against Moodle Web Services. **Price the Moodle variant as engineering, not integration:** its MCP
surface is roughly 1/300th as adopted as Canvas's, and the AGPL network clause now sits in *your*
deliverable rather than only in the client's platform.

---

## P15 — Defensible autograding with zero copyleft, end to end *(new in pass 267)*

**When:** state or institutional rules bar AI from *determining* a grade (Oklahoma `SB 1734`,
Ohio `HB 96`, California `AB 1159`, Idaho `SB 1227`, and the "meaningful human review" test in
T17), but the client still needs assessment at scale. The grade must be **deterministic,
reproducible and explainable on appeal**; the AI may explain, suggest and tutor around it.

```
Substrate   jupyterhub/jupyterhub        BSD-3   8.4k*, 8,913 commits; per-student environments
           |
Grading    Submitty/Submitty            BSD-3   802*, 9,316 commits, 1.1k forks (RPI/RCOS)
           |                                    submission + autograding + TA grading workflow
           +-- ucbds-infra/otter-grader  BSD-3   UC Berkeley; Python AND R; Canvas/Gradescope
           |                                    adapters + student-side public checks
           +-- jupyter/nbgrader          BSD-3   notebook assign/release/collect/grade
           +-- autolab/Autolab           Apache-2.0  CMU; course-management shell
           +-- numbas/Numbas             Apache-2.0  maths; executes ENTIRELY IN THE BROWSER
           |                                        -> submission never leaves the device
           v
AI layer   ls1intum/Pyris               MIT     feedback SUGGESTIONS to the instructor
           (never writes a grade)               + RAG over the course's own material
           v
Record     yetanalytics/lrsql           Apache-2.0  who saw what, who approved, when
```

**Six permissive grading options, three licences (BSD-3 / Apache-2.0 / MIT), zero copyleft.**
This is the pattern's whole commercial content: **autograding is a solved, free problem.** Proposing
to build one is proposing to rebuild five mature university systems. The billable work is
(a) wiring a grader into the client's LMS — `otter-grader`'s Canvas adapter does half of it,
(b) the pedagogy of the feedback, and (c) **defensibility**: the appeal path, the human sign-off
record, the disclosure artefact.

**The regulatory test this satisfies by construction:** the deterministic grader produces the mark;
the model never touches it; `lrsql` holds the evidence that a human disposed of every AI
suggestion. That is **declassification by architecture** (T17), not by policy document — and it
reuses P10's posture with five permissive components instead of three.

**Do not** substitute `PrairieLearn` into this stack without legal review: it is strong software,
but the grant is **partitioned four ways** (AGPL-3.0 Community Edition, a separate-terms Enterprise
Edition directory, AGPL client-side JavaScript, MIT contributor portions) and the GitHub sidebar
shows no label at all. Likewise `RunestoneInteractive/rs`, whose MIT headline excepts a
**commercial** Handsontable dependency.

---

## P16 — Delivering India's Class 3-8 AI curriculum on India's own MIT stack *(new in pass 267)*

**When:** an APAC public-sector or education-group engagement in India. **The mandate is dated and
the platform is permissive** — the only region in this KB where both are verified (T22, and the
APAC section of [`intel/market.md`](../intel/market.md)).

- **Demand:** AI and computational thinking compulsory from **Class 3**; CT&AI curriculum for
  Classes 3-8 **launched 2026-04-01**; implementation from the **2026-27 session**; Classes 9-10 in
  **2027-28**; teacher training through **NISHTHA**; **₹500 crore** Centre of Excellence announced
  in the 2025-26 budget. ⚠️ Secondary-source — dates decision-usable, figures directional.
- **Supply:** the national stack is **MIT, end to end.**

```
Platform   Sunbird-Ed/SunbirdEd-portal            MIT   38,046 commits, 317 forks (41*)
           project-sunbird/knowledge-platform     MIT   content/knowledge services
           Sunbird-Ed/SunbirdEd-mobile-app        MIT   mobile client -- the real access path
           ^ the codebase under DIKSHA (NCERT / Ministry of Education)
           |
Curriculum DaRL-GenAI/instructional_agents        MIT   488*, EACL'26: ADDIE pipeline
           |                                            syllabus -> slides -> assessments,
           |                                            with Instructional Designer / TA roles
           +-- JuneYaooo/lineage-skill        Apache-2.0  turns NCERT material into agent skills
           |                                              that stay TIED TO THEIR SOURCES
           v
Teacher    SirhanMacx/Claw-ED                     MIT   local-first, teacher-reviewed lesson drafts
enablement ls1intum/Pyris                         MIT   tutor microservice, RAG over the
           |                                            ministry's own curriculum documents
           v
Offline    learningequality/kolibri                MIT  offline delivery where bandwidth fails
           learningequality/studio                 MIT  authoring + REMIX AGAINST NATIONAL CURRICULA
           Tangerine-Community/Tangerine        GPL-3.0  offline ASSESSMENT -- keep behind an API
           v
Measure    bigdata-ustc/EduData              Apache-2.0  datasets/preprocessing
           pykt-team/pykt-toolkit                  MIT   knowledge tracing, once data is trustworthy
```

**Why this is an unusually clean pattern:** no platform displacement is proposed, no copyleft
enters the deliverable (Tangerine is the one exception and sits behind an API boundary), and the
client's own ministry already maintains the base. **The scarce thing is not the platform — it is
Classes 3-8 content and teacher capability at national scale**, which is exactly what
`instructional_agents` (peer-reviewed, MIT) and `lineage-skill` (provenance-preserving) address.

**The failure mode to design against, from the region's own recent history:** South Korea mandated
AI digital textbooks, saw **under 30% adoption**, and in **August 2025 its National Assembly
stripped them of official textbook status** after teachers' unions said the pace had outrun
preparation. **Lead with NISHTHA-aligned teacher enablement and measurable classroom readiness,
not content volume.** A mandate engagement is cancelled by unprepared teachers, not by missing
content.

⚠️ **Sunbird slug trap:** the live slugs are camel-case (`Sunbird-Ed/SunbirdEd-portal`);
`Sunbird-Ed/sunbird-ed-portal` does not resolve. And do not read Sunbird's **41 stars** as
adoption — 38,046 commits and 317 forks are the signal, re-measured and reproduced in pass 267.

---

## P17 — Delivering a primary-school AI-literacy mandate when the curriculum cannot be licensed *(new in pass 268)*

> 🟢 **EXTENDED pass 285 — a second, independent instance of this pattern's premise, and this one
> states the remedy in its own words.** [`Angel-builds/edubot-africa`](https://github.com/Angel-builds/edubot-africa)
> records, first-hand in its README, that **Ghana's NaCCA curriculum PDFs are free to download but
> marked *all rights reserved*, and that WAEC past questions carry *no public licence*.** Its
> architecture is this pattern's remedy, independently arrived at: **use the curriculum as
> taxonomy, not as content** — NaCCA's `B7.1.1.1` annotation scheme becomes a **skill graph**, and
> explanatory prose is grounded on **openly licensed sources** instead.
>
> 🔵 **Why this is worth carrying as a design rule rather than a Ghana footnote.** The two assets
> every education engagement wants to ground on are the **national curriculum** and the
> **examination board's past papers**, and across this region **both are closed**. So the
> constraint is **architectural, not a legal-review item**: *a design that stores curriculum TEXT
> cannot ship; a design that stores curriculum STRUCTURE can.* Structure — codes, strands,
> outcomes, progressions — is the part a tutor actually needs to sequence and assess against.


**The engagement.** A ministry or large district must deliver AI instruction to primary pupils
against a dated mandate — China (≥8 h/year from age six, since Sep 2025), Singapore MoE (Mar 2026),
India CBSE Classes 3-8 (session 2026-27), or the EU AI Act Art. 4 staff-literacy duty.

**Why this pattern exists and `P91-G`/`P16` do not cover it.** `Gap 367` has carried *"no permissive
AI curriculum for primary"* for ~175 passes as *"the largest named, dated, deadline-bearing demand on
this shelf with no supply"*, naming **Code.org** and **MIT Day of AI** as alternatives. Pass 268 read
the licences. **The gap is not under-searched — it is correctly empty**, and that changes the
proposal rather than delaying it.

| what | component | licence | role |
|-------|-----------|---------|------|
| Delivery engine | [`code-dot-org/code-dot-org`](https://github.com/code-dot-org/code-dot-org) | **Apache-2.0** *(source and assets only — see the carve-out)* | Lesson delivery, progress tracking, classroom management, block-based programming environment. **215,796 commits** of it. |
| Offline delivery, where connectivity is the constraint | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Ships the originated content to schools with no network |
| Content authoring + national-curriculum remix | [`learningequality/studio`](https://github.com/learningequality/studio) | **MIT** | The pipeline that organises originated lessons into channels and aligns them to the national curriculum |
| Teacher-facing generation, human-in-the-loop | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** (EACL'26) | ADDIE multi-agent: syllabus → slides → assessments, for *teacher review* |
| Local-first lesson drafting | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | **MIT** | Draft editable lessons where pupil data cannot leave the building |
| Pupil-facing tutoring, if in scope at all | [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) *(the tutor is called **Iris**; `ls1intum/Iris` is an alias of this same repo — `p282`)* | **MIT** | Pedagogically constrained by design (hints, not answers) — the posture a high-risk classification wants |

**Wiring.**
1. **Fork the Code.org platform, strip the content.** Deploy the Apache-2.0 engine. Delete, do not
   adapt, every Proprietary Material: artwork, graphics, sounds, lectures, videos, logos, characters
   and fonts. The payload confines them to *"Code.org's own web site, mobile applications, or social
   media channels ... without modification or embedding in another format."*
2. **Originate the lessons against AI4K12's Five Big Ideas** — the framework Code.org and MIT Day of
   AI both organise on — but **write your own text**, because
   [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12) **serves no licence payload**
   (`Gap 354`). An unlicensed framework can be *conformed to*; it cannot be *redistributed*.
3. **Author and package in Kolibri Studio**, align to the national curriculum there, publish as
   channels, and deliver through Kolibri where bandwidth is the real constraint.
4. **Put `instructional_agents` behind the teachers, not the pupils.** Generation for teacher review
   keeps the system out of the EU AI Act's high-risk band via the `P2`/`T17` meaningful-human-review
   route, and keeps a staff-literacy duty satisfiable by the same deployment.
5. **Add `Iris`/`Pyris` only if pupil-facing tutoring is genuinely in scope.** For primary pupils in
   a mandate engagement it usually is not, and the config-gated design means the platform runs
   identically with AI off — which is the demonstration a regulator wants.

🔴 **The three things that must be said in the first meeting.**
- **The curriculum is the deliverable; the engine is the freebie.** Budget belongs in instructional
  design and localisation, not platform build.
- **You cannot reuse Code.org's Minecraft, Star Wars, Frozen, Angry Birds or Plants vs. Zombies
  activities.** The `NOTICE` lists them as third-party licensed IP — Code.org cannot sublicense
  them, so no contract with Code.org would help either. Also excluded: **Font Awesome Pro**.
- **A client who has seen Code.org assumes the lessons come with the code.** Correcting that
  assumption before signature is the single highest-value sentence in this pattern.

🟢 **Estimate shape:** 10-14 weeks. Platform deployment and content stripping is ~2 weeks of it;
the rest is curriculum origination, translation and teacher enablement. **Do not quote this as a
platform project.**

## P18 — An agent over the system of record a US district already runs *(new in pass 268)*

**The engagement.** A US district, state education agency, or a vendor selling into them, wants
AI-assisted early warning, reporting or an agent surface — with no copyleft boundary in the
deliverable.

**Why this pattern exists.** `verticals/solutions.md` published, in pass 267, that no North American
public-sector base existed. It does: **Ed-Fi**, Apache-2.0, and this base's own gap register has
carried it as *the only permissive system of record* for roughly 200 passes. Every layer below is
permissive, which is what Canvas (AGPL-3.0) and Open edX (AGPL-3.0) deny.

| layer | component | licence |
|-------|-----------|---------|
| Student data model | [`Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** |
| System of record (existing deployments) | [`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) + [`Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** |
| System of record (new builds) | [`Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** |
| Learner event stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** |
| Risk model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) or [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | **MIT** |
| Agent surface over the LMS beside it | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** |
| Human review surface | [`uPortal-Project/uPortal`](https://github.com/uPortal-Project/uPortal) | **Apache-2.0** |

**Wiring.**
1. **Read from Ed-Fi, do not re-model.** The agency's students are already in the Ed-Fi model, so
   the integration is *conformance*, not mapping — and it ports to the next district unchanged.
2. **Write AI output to the LRS, never to the system of record.** This is the load-bearing decision.
   `Gap 314` establishes that **DMS provisioning is create-only**: an AI-generated risk flag, an
   AI-assisted grade or generated evidence is a **data-model extension and a re-provision of the
   database**, not an insert. Writing to `lrsql` as xAPI statements keeps the system of record
   untouched and keeps the AI output auditable and separable — which is also what a
   meaningful-human-review posture (`T17`) requires.
3. **Train the risk model on Ed-Fi reads plus xAPI events**, with `pykt-toolkit` for prediction or
   `pyedmine` where the deliverable is a recommender.
4. **Surface it to staff through uPortal** (Apache-2.0, campus single-pane) and reach the LMS via
   `canvas-mcp` (MIT) — never by forking `instructure/canvas-lms` (AGPL-3.0).

🔴 **Three prices to quote from the register, not the README.**
- **DMS adoption is a re-platforming with a data migration**, stated normatively in
  `docs/PRD-v8.0.md` (`Gap 303`). **Never price it as an in-place cutover.**
- **DMS provisioning is create-only** (`Gap 314`) — hence step 2.
- **OneRoster is absent from DMS v8.0** (`Gap 309`), while native **OneRoster 1.2** shipped in the
  **ODS/API 7.3.2** line (search-summary grade). **Say which line you are quoting**, because the
  rostering story differs between them. Also note the platform moved to **.NET 10** ahead of .NET 8
  end-of-support in **November 2026** — a client on an older ODS has a dated upgrade of its own.

⚠️ **Do not brief a state adoption count.** Neither Ed-Fi README names a state or an agency; the
14-state list is third-party, and **`ed.sc.gov` did not resolve from this environment**, so the one
primary government page that would settle it was not read. Quote the **licence** — payload-verified
2026-10-17 — and let the client's procurement confirm their own state's status.

🟢 **Estimate shape:** 8-10 weeks for the Ed-Fi read + LRS write + risk model + staff surface, on an
existing ODS deployment. **Add a separate migration line item if the client is moving ODS → DMS**;
that is not part of this pattern and it is not small.

## Component quick reference

| Need | Component | Licence |
|------|-----------|---------|
| Tutoring agent | `HKUDS/DeepTutor` | Apache-2.0 |
| Course material generation | `DaRL-GenAI/instructional_agents` | MIT |
| Human-reviewed lesson drafting | `SirhanMacx/Claw-ED` | MIT |
| Source provenance for generated content | `JuneYaooo/lineage-skill` | Apache-2.0 |
| Automated assessment + feedback | `ls1intum/Artemis` | MIT |
| Maths e-assessment | `numbas/Numbas` | Apache-2.0 |
| Code plagiarism detection | `dodona-edu/dolos` | MIT |
| Knowledge tracing | `pykt-team/pykt-toolkit` | MIT |
| Tracing + diagnosis + recommendation | `ZhijieXiong/pyedmine` | MIT |
| Education datasets | `bigdata-ustc/EduData` | Apache-2.0 |
| Spaced repetition scheduler | `open-spaced-repetition/fsrs4anki` · `fsrs-rs` | MIT · BSD-3 |
| LTI tool framework | `tsugiproject/tsugi` · `pylti1.3` | Apache-2.0 · MIT |
| Learning record store | `yetanalytics/lrsql` + `adlnet/xAPI-Spec` | Apache-2.0 |
| SCORM runtime | `jcputney/scorm-again` | MIT |
| Permissive LMS — institutional | `OpenOLAT/OpenOLAT` | Apache-2.0 |
| Permissive platform — lesson delivery | `oppia/oppia` | Apache-2.0 |
| Permissive platform — offline-first | `learningequality/kolibri` | MIT |
| Autograding — programming + course mgmt | `autolab/Autolab` | Apache-2.0 |
| Autograding — notebooks | `jupyter/nbgrader` | BSD-3-Clause |
| Brazilian municipal SIS + teacher portal | `portabilis/i-educar` · `portabilis/i-diario` | GPL-2.0 · AGPL-3.0 |
| AI-native LMS | `Selleo/mentingo` | MIT |
| Multimodal tutoring platform | `Open-TutorAi/open-tutor-ai-CE` | BSD-3-Clause |
| MCP: spaced repetition · tutoring | `ankimcp/anki-mcp-server` · `tutor-mcp` | MIT |

**Do not compose:** `formalms/formalms` (**GPL-2.0**, despite a 2026 review publishing it as
Apache-2.0), Fedena (`foradian/fedena`, `projectfedena/fedena` — **abandoned since 2012/2016,
no licence payload**, still recommended by vendor comparisons as *the* Apache-2.0 education
ERP), `h5p/h5p-php-library` (**GPL-3.0**, widely miscited as MIT — including in earlier Globant
KB cycles), `os4ed/openSIS-Classic` (🟢 **GPL-2.0 at payload since p275** — `docs/License.txt`, 17 286 B; copyleft on distribution, so scope it on the licence's REACH, not on a missing grant),
`CaviraOSS/PageLM` (non-commercial, redistribution prohibited),
`GarethManning/education-agent-skills` (CC-BY-SA-4.0 ShareAlike),
`GeminiLight/awesome-ai-llm4education` (no licence served),
`human-skill-tree` / `freelingo` / `lumen` (AGPL/GPL — network copyleft on hosted delivery).

## Declared gaps

- **Still no pattern for autonomous grading, and now it is a design choice rather than a
  shortage.** P10 exists precisely because the regulated markets (US states, EU Annex III,
  Brazil's `PL 2338`) are converging on human decision-makers. Deterministic autograding plus a
  logged human sign-off is the architecture; an LLM that assigns marks is not a pattern this KB
  will publish.
- **Retracted: "no APAC-origin component appears in any pattern above."** `HKUDS/DeepTutor`
  (P2, P8) is from the **Data Intelligence Lab at the University of Hong Kong**, and
  `bigdata-ustc/EduData` (USTC) and `HFUT-LEC/EduStudio` (Hefei University of Technology) are
  in the quick reference. The APAC-origin components were in the patterns the whole time; the
  gap statement was not re-tested against them. What remains true: **no APAC-origin
  *platform*** anchors any pattern.
- **No LATAM-origin agent in any pattern.** P8 is anchored on LATAM-origin *platforms*
  (`i-educar`, `i-diario`) with non-LATAM agents on top. That is the honest state of the shelf:
  the region publishes systems of record, not agents.
- **P9's model layer is deliberately unspecified.** Device class drives quantisation, and this
  KB has not benchmarked tutoring quality for small local models on classroom hardware. Naming
  a model here would be a guess dressed as a recommendation.

### Added in pass 267

- **P14 is the pattern this file most needed and did not have.** The single most common North
  American situation — *"the client runs Canvas"* — had no recipe for 266 passes, because
  [`verticals/solutions.md`](../verticals/solutions.md) carried Canvas as closed SaaS. Its source
  is **AGPL-3.0, 78,765 commits**, and the engagement shape is an **MIT doorway**
  (`vishalsachdev/canvas-mcp`) over a platform the client already operates. 🔵 **The general rule
  this suggests:** before writing a pattern that routes *around* an incumbent, read the
  incumbent's licence payload. "Commercial" and "closed" are different claims.
- **P15 supersedes nothing but strengthens P10 materially** — five permissive graders plus a
  permissive substrate (`jupyterhub`, BSD-3, 8.4k★) instead of three graders and no substrate.
- **P16 is the only pattern in this file where mandate, platform and licence all line up**, and it
  is deliberately weighted toward teacher enablement because the region supplies a **documented
  failure case** (Korea's withdrawn textbook mandate) rather than only a success story.
- **Still no pattern for:** a North American *public-sector platform* engagement (none exists —
  the NA public-sector code located is a service layer, not a platform), and a LATAM engagement
  outside Brazil on open code (**Uruguay's Ceibal publishes no repositories at all**, verified this
  pass).


## P19 — Delivering an African or Middle Eastern ministry mandate when the regional supply serves no grant *(new in pass 269)*

> 🟢 **EXTENDED pass 285 (`2026-10-18`) — the evidence base for this pattern's central claim went
> from two rows to five, and the claim held.** `p284` left the instruction to search African
> education **code** by **exam-board and language names** rather than by the word *"Africa"*. It
> worked on the first attempt, and every repository it found was tree-enumerated:
>
> | repository | what it is | tree | grant |
> |---|---|---|---|
> | [`Angel-builds/edubot-africa`](https://github.com/Angel-builds/edubot-africa) | 🇬🇭 Maths tutor on the **Ghanaian JHS NaCCA Common Core (B7–B9)**; withholds solutions by construction, routes arithmetic through **SymPy**, gates retrieval quality **in CI** | 40 files | 🔴 **NONE_IN_TREE**; `pyproject.toml` declares **no licence key** |
> | [`Onyeocha-Keside/naija-learn`](https://github.com/Onyeocha-Keside/naija-learn) | 🇳🇬 **Voice-first** study Q&A in **Yoruba, Hausa, Igbo, Nigerian English** (N-ATLaS ASR + YarnGPT2) | 35 files | 🔴 **NONE_IN_TREE**; no licence line in `README` |
> | [`meduoyeomoyenia-cyber/Education-AI-TUTOR`](https://github.com/meduoyeomoyenia-cyber/Education-AI-TUTOR) | 🇳🇬 **WAEC / NECO / JAMB** SS1–SS3 tutor, Nigerian Pidgin | 138 files | 🔴 **NONE_IN_TREE**; `web/package.json` has **no `license` key**, `"private": true` |
>
> 🔴 **Five African education code rows are now known to this base. All five serve no grant** —
> the two this pattern already named plus these three. 🟢 **That is no longer a thin sample, and it
> upgrades this pattern's premise from an observation to a measured regional property:** the
> constraint in MEA is **not** that nobody is building. It is that **nothing being built is
> licensed**. For a studio the practical consequence is unchanged but now firmly evidenced — these
> repositories are **readable prior art and unusable dependencies**, and the two lawful routes are
> a **written grant request to the author** or a **clean reimplementation** against the same
> curriculum structure.
>
> 🔴 **One lure to carry:** `studyield/studyield`, returned by the same leg as a self-described
> open-source learning platform, **does not resolve**. Fourth channel for the dead-address class.
> Evidence: [`tree-enumeration.2026-10-18-p285.tsv`](../evidence/tree-enumeration.2026-10-18-p285.tsv).


**The engagement.** A ministry of education — or a development funder working through one — has a
**funded, dated AI mandate** and no licensed software to execute it. Kenya (**10,382** junior
secondary schools under **KDEAP**, **62,000+** teachers ICT-trained), Nigeria (AI + programming +
robotics in secondary curriculum since **September 2025**), Egypt (**UNESCO** national **AI
competency framework for teachers**, **2026-06-03**; **236,000+** general-secondary enrolments from
2025/26), South Africa (**no national policy in force** — the 2026 draft was **abrogated 2026-04-27**
— but **DBE Coding and Robotics for Grades R–9** in development).

**Why this pattern exists and why it is not `P17` or `P16`.** `P16` delivers India's mandate **on
India's own MIT stack** (Sunbird/DIKSHA) — there is a national permissive platform to stand on.
`P17` handles a mandate whose **curriculum** cannot be licensed. **MEA is the harder case: neither
exists.** Pass 269 located the first two African-context education agents in this base and **both
serve no grant** — [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa)
(South Africa, Grades 8–12, **pre-licence**, placeholder still in the README) and
[`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria, **no grant on either
channel**). **Nigeria's Naija Teacher AI states no licence; Kenya's Kytabu SOMANASI is
proprietary.** So the stack has to be assembled from permissive software built elsewhere, with the
*local* contribution being curriculum alignment and language — which is exactly what a studio sells.

| layer | component | licence | why this one |
|-------|-----------|---------|--------------|
| Teacher-facing authoring | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | Peer-reviewed (EACL'26) ADDIE pipeline: syllabus → slides → assessments. **The deliverable Egypt's teacher framework implies.** |
| Local-first lesson drafting | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | **MIT** | Runs without sending student or curriculum data out of the building — the posture for a ministry pilot. |
| Provenance of generated material | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** | Generated material stays tied to its source. A ministry asks *"where did this come from"* before it asks anything else. |
| Offline delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | Connectivity is the binding constraint in every one of the four countries. `P9` is the offline half. |
| Offline assessment at national scale | [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | GPL-3.0 ⚠️ | README claims **5M+ assessments across 65 countries** — the only regionally-proven assessment option. **Copyleft: keep it as a deployed system beside the deliverable, never linked into it.** |
| Lesson-plan structuring precedent | [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | **MIT** | **Sierra Leone MBSSE national lesson plans → structured JSON**, corpus shipped. The one piece of Africa-engaged permissive code in this base, and a working template for doing the same to a Kenyan or Nigerian curriculum. ⚠️ Research-grade (1–12★), so read it as a method, not a dependency. |
| Tutor layer, if the pilot is student-facing | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | Default tutoring row; persistent student model. |

**Wiring.**
1. **Attach to the national instrument, and pick the right one per country.** Egypt → the **teacher
   competency framework** (teacher-facing workflow, which is where permissive supply actually
   exists). Kenya → the **KDEAP rollout** (devices and connectivity already funded; the gap is
   content and teacher capability). Nigeria → the **secondary curriculum lines** (Python, JS,
   HTML/CSS are named, so the scope is bounded). **South Africa → enter at INSTITUTION level**, not
   ministry: **NWU has a policy** and USAf keeps a register, while the national policy was withdrawn.
2. **Parse the national curriculum into structure before generating anything**, using
   `lesson-plan-parse-mbsse` as the worked precedent. **This is the step that makes the deliverable
   defensible and the step that cannot be imported** — it is per-country, and it is billable.
3. **Generate with `instructional_agents`, draft locally with `Claw-ED`, and keep lineage with
   `lineage-skill`.** Every one permissive, so the deliverable carries no copyleft.
4. **Ship offline through Kolibri (MIT).** Deploy `Tangerine` **as a system** if national assessment
   is in scope, and keep its GPL-3.0 boundary at the process edge.
5. **Originate the curriculum content; do not ship a found one.** `P17`'s rule applies with a new
   instance: `datawhalechina/ai-edu-for-kids`, the most-adopted primary-band curriculum artefact
   this base has found, is **CC-BY-NC-SA-4.0** (and only in README prose). Read it to establish
   *what a primary AI course must cover*; write the text yourself.

🔴 **Four prices to quote honestly.**
- **There is no MEA market sizing in this base** — no spend figure, no vendor share, no CAGR for any
  of the four countries. **Scope from the programme counts above (schools, teachers, enrolments),
  not from a market number**, because this base does not have one and will say so.
- **Every regional figure here is secondary-source grade.** `p268` established the non-GitHub DNS
  failure as environmental; no ministry document was read. **Make confirmation against the ministry's
  own circular an explicit first-phase task**, not an assumption.
- ⚠️ **Do not name Egypt's delivery platform.** Reporting splits across **QUREO**, the Japanese
  **Kiryo**, and a **Sprix** contract approved January 2026. **Brief the framework, not the vendor.**
- 🔴 **Do not cite the `EduNaija AI Tutor` paper and `Valexxy/edunaija-os` as the same thing.** The
  paper (ACL AfricaNLP 2026, DOI `10.18653/v1/2026.africanlp-main.11`) is a five-agent LangChain +
  FAISS tutor with **English / Yoruba / Hausa / Igbo** support **whose code this base could not
  locate**; the similarly-named repository is an unlicensed starter codebase.

🟢 **The one cheap upstream move.** `EduTwin-Africa`'s README says *"Add the project's chosen license
here before publishing."* **That author knows the grant is missing** — so unlike this base's other
ungranted rows, a licence request there has a plausible answer, and a South African engagement would
start from existing SA-curriculum-aware code rather than from zero. **Ask before you rebuild.**

🟢 **Estimate shape:** **6–8 weeks** for curriculum parsing + teacher-facing generation + offline
delivery against **one** country's instrument, assuming the device and connectivity layer is already
funded (true in Kenya, not assumed elsewhere). **Each additional country is a new curriculum parse
and a new language pass — price it as a new engagement, not a rollout**, because the permissive
layer ports and the national layer does not.

## P20 — The Spanish/LOMLOE teacher-workflow engagement, and how to ship against a ShareAlike curriculum framework *(new in pass 270)*

**Target:** Spain (LOMLOE + CCAA autonomous-community curricula). Transfers to any jurisdiction
whose curriculum publishes **official criteria** a deliverable must demonstrably cover.
**Why now:** the **Sanoma Learning 2026 European Teacher Survey** (>20,000 teachers, 14 countries)
measured **63% of European teachers using AI** and **only 16% believing general-purpose AI improves
learning outcomes** (`T28`). The client already has an AI tool, already has evidence it is not
working, and the reason is that it does not know their curriculum. **This pattern is the answer to
that specific objection, and nothing else on these shelves answers it as directly.**
**Timeline:** 6–8 weeks to a measurable teacher-facing pilot.

```
[OpenDidactia  CC BY-SA 4.0]  <- READ as a specification, NOT shipped as content
  nmarafo/OpenDidactia         OKF: curricular schemas for Programaciones Didacticas
  2,123 B licence payload      and Situaciones de Aprendizaje (LOMLOE / CCAA)
  50 commits / 0 stars         ** NOT runnable code — prompts + schemas **
        |
        |  (the licence boundary lives on THIS arrow — see below)
        v
[instructional_agents  MIT]    multi-agent ADDIE: syllabus -> slides -> assessments
  DaRL-GenAI/instructional_agents    roles: Teaching Faculty / Instructional Designer / TA
        |
        v
[Claw-ED  MIT]                 teacher approves before anything reaches a student;
  SirhanMacx/Claw-ED           
                               local-first, curriculum never leaves the institution
        |
        v
[Numbas  Apache-2.0]           assessment execution ENTIRELY CLIENT-SIDE —
  numbas/Numbas                answers a Spanish data-residency objection structurally
        |
        v
[Moodle  GPL-3.0]              the LMS Spanish public education already runs;
                               keep it at the process edge, integrate over its API
```

🔴 **The licence boundary, which is the whole engineering content of this pattern.**
`OpenDidactia` is **CC BY-SA 4.0** — verified first-hand at `main/LICENSE.md`, 2,123 B, pass 270.
**ShareAlike, and critically NOT NonCommercial**, which makes it *commercially usable* and puts it
in a different category from `datawhalechina/ai-edu-for-kids` (**NC *and* SA**, unusable in a
deliverable at all — `P17`, `p269`). **"CC with a hyphenated suffix" is not a verdict; read which
suffixes.**

What ShareAlike colours here is **adapted content**, not the client's code:
1. 🟢 **Read OpenDidactia's OKF schemas to learn the SHAPE of a LOMLOE programación** — the
   mandatory prior inventory of every official criterion, the 100%-coverage audit line, the
   analytic rubric per instrument. **Shape and method are not copyrightable; the text is.**
2. 🔴 **Do not ship its prompt text, its schemas or an edit of them** inside a proprietary
   deliverable. That is the derivative that triggers SA.
3. 🟢 **Write your own schemas against the official curriculum** — which is the authoritative source
   anyway, and which `OpenDidactia` is itself a reading of. **Then the generated programaciones are
   the client's, under whatever terms the client wants.**
4. 🟢 **If the client is a public body and SA is acceptable** (common in Spanish public education —
   CC BY-SA is the default in much of the sector), **adopt OpenDidactia directly and contribute
   back**. This is the cheaper path and it is available more often than a reflex "no copyleft" rule
   admits. **Ask which one the client wants in week one; do not decide it for them.**

🟡 **What to verify in week one, because this base cannot.**
- 🔴 **`OpenDidactia` is 0 stars at 50 commits, GitHub detects no language, and it is a
  prompt/knowledge framework rather than software.** **There is no community, no release and no
  maintenance signal.** Treat it as **one practitioner's written-down method** — valuable as that,
  and **not** as a dependency. Nothing in the chain above calls it at runtime, by design.
- ⚠️ **CCAA divergence is the real scope risk.** LOMLOE sets the frame; each autonomous community
  publishes its own criteria. **Price one community, then price each additional one as a new
  curriculum parse** — the same rule `P19` applies to additional countries.
- ⚠️ **Every regulatory and market figure behind this pattern is secondary-source grade** and the
  EMEA market number is now a **two-publisher range ($2.1–2.6B, 2026 — `T30`)**, not a point.
  **Quote the range and say it is a range.** Scope from teacher and school counts instead.

🟢 **Why this pattern beats the obvious alternative.** The obvious alternative is Estonia's: buy a
proprietary platform at national scale (`~half of 20,000` upper-secondary students, Minister
**Kristina Kallas** to *Politico*, May 2026). It works, and it is the thing a sovereignty-conscious
European procurement will be asked about afterwards. 🔵 **Every component above except Moodle's
GPL-3.0 edge is MIT or Apache-2.0, and every one of them is EMEA-origin or EMEA-hosted** — which
this base's EMEA section already establishes as the regional differentiator. **The permissive,
regionally-governed stack exists; this pattern is the assembly instructions.**

## P21 — Shipping against a DATED future mandate: the Netherlands `kerndoelen`, 2027-08-01 *(new in pass 271)*

**Target:** Netherlands — `primair onderwijs`, `onderbouw vo` and `(voortgezet) speciaal onderwijs`.
Transfers to any jurisdiction whose AI-literacy duty is **enacted with a named future commencement**
rather than already binding.
**Why now, and why this is a better engagement than the claim it replaces:** pass 270 retracted the
Netherlands as `NOT_ESTABLISHED`; pass 271's Dutch-language leg found the instrument
(`T35`). The **`kerndoelen digitale geletterdheid`** include **`AI-geletterdheid` explicitly**, are
**concept today**, become **legally official on 2027-08-01**, and are **fully introduced with
`Inspectie` oversight in 2031**.
🔵 **A present-tense "market leader" is a market already lost. A dated commencement is a procurement
runway with a deadline on it** — roughly 9 months of buying time before the duty attaches, and a
further inspection horizon that makes evidence-of-coverage the renewable part of the deliverable.
**Timeline:** 10–12 weeks to an inspectable pilot across two bands.

```
[kerndoelen digitale geletterdheid]   <- READ as the specification. A government instrument,
  SLO / OCW, concept (Jul+Nov 2025)      NOT a repo and NOT a licence question.
  official 2027-08-01                    3 domains; practical domain = AI exploration:
  Inspectie oversight from 2031          recognise AI around you / how it works /
        |                                social + ethical consequences
        |  map each kerndoel -> one competency id, ONCE, as data
        v
[competency map: your own artefact]   the deliverable the client actually owns.
  TSV/JSON, no upstream licence         po | onderbouw-vo | (v)so  x  3 domains
        |
        +-------------------------------+
        |                               |
        v                               v
[DeepTutor  Apache-2.0]          [instructional_agents  MIT]
  HKUDS/DeepTutor                  DaRL-GenAI/instructional_agents
  student-facing tutoring,         teacher-facing: syllabus -> slides ->
  bound to the competency id       assessments against the same ids
        |                               |
        +-------------------------------+
        |
        v
[H5P content generated, played through MIT]   <- THE LICENCE BOUNDARY OF THIS PATTERN
  generate interactive items, then play them with
  tunapanda/h5p-standalone  MIT  (1,077 B)
  package with sr258/scorm-h5p-wrapper  MIT  (1,073 B)
  ** NEVER fork h5p/h5p-php-library — GPL-3.0, 35,146 B, master/LICENSE.txt **
        |
        v
[Moodle  GPL-3.0]                the LMS Dutch schools run; integrate over its API and its
  moodle/moodle                    provider-pluggable AI subsystem (4.5+), never by forking
        |
        v
[Koha  GPL-3.0]  (optional, HE/vo+ only)   catalogue as the curated retrieval authority
  Koha-Community/Koha                      librarian-maintained metadata, not scraped text
```

🟢 **Why the competency map is the first deliverable and not the tutor.** The mandate is a
**coverage** obligation inspected from 2031, so what the client must be able to produce is *evidence
that every kerndoel is addressed*, per band. Build that as **data you own** — one row per kerndoel,
mapped to one competency id — and both the student-facing and teacher-facing agents become consumers
of it. 🔵 **This also makes the 2027→2031 gap billable in the right order:** map and pilot before
commencement, then widen coverage and produce inspection evidence after it.

🔴 **The H5P arrow is where this pattern is won or lost.** H5P is already inside most Dutch Moodle
estates, so generating interactive content is the path of least resistance — and the **authoring core
is GPL-3.0 with no permissive alternative** (`ACTION PW`, pass 271). **Generate content, play it
through the MIT runtime, package with the MIT wrapper.** A fork of the authoring core puts the
client's whole content pipeline inside GPL-3.0; the MIT playback path does not.

🟢 **The sovereignty argument is supplied by the ministry itself, which is rare and should be quoted.**
OCW's **Kamerbrief on `digitale autonomie` (2026-07-02)** states that Dutch education is
*"in grote mate afhankelijk van niet-Europese techbedrijven"* — **largely dependent on non-European
tech companies** — while naming responsible AI use as part of public digital provision. Pair it with
`p270`'s Estonia finding (≈half of 20,000 upper-secondary students on an **OpenAI-partnered
proprietary** platform) and the **Sanoma** numbers (**63%** of European teachers using AI, **16%**
believing general-purpose AI improves outcomes — `T28`). 🔵 **Every component above is open source and
curriculum-bindable, which is precisely what the general-purpose assistant cannot be.**

🟡 **What this pattern does NOT claim, stated so a proposal does not overreach:**
- 🔴 **The Netherlands is not a current K-12 AI leader.** That aggregator claim is still unsupported
  (`T33` — it is the same sentence as the `$2.64B` EMEA figure). **No Dutch deployment at Estonia's
  measured scale was located.** Sell the runway, not a race already run.
- 🔴 **The kerndoelen are CONCEPT.** Final wording can still change before 2027-08-01. Build the map
  as data precisely so a wording change is a data migration, not a re-architecture.
- 🟡 **`Gap 367` is not closed by this.** There is still **no permissively licensed primary-band
  AI-literacy curriculum artefact** in any of the four languages searched (`p269`–`p271`). This
  pattern works *because* it treats the government instrument as the specification and keeps the
  generated artefact as the client's own — the same move as `P17` and `P20`, now with a date attached.
- ⚠️ **All Dutch policy datums here are secondary-source grade.** The primary channel
  (`open.overheid.nl`, `rijksoverheid.nl`) is unreachable from this environment — re-tested pass 271,
  both transports. Verify the commencement date against the primary text before contracting on it.

## P22 — The zero-copyleft engagement: a full education stack where procurement excludes GPL/AGPL *(new in pass 272)*

**Target:** US state university systems and public agencies whose procurement or redistribution rules
exclude copyleft — the lane **SUNY's systemwide AI policy across 64 campuses** (new on `market.md` this
pass) and **Utah's statewide vendor deal** both sit in; also EMEA public bodies that must redistribute
derivative work without a network-copyleft obligation.
**Timeline:** 10–14 weeks to a production pilot.

**Why this pattern exists.** Every default answer in education is copyleft: **Moodle GPL-3.0**,
**Open edX AGPL-3.0**, **Canvas AGPL-3.0**, **OpenEduCat LGPL-3.0**, **Koha GPL-3.0**, **H5P GPL-3.0**.
When a client's procurement excludes copyleft, the usual advice is "use the API and don't fork" — which is
a constraint, not a stack. 🟢 **Pass 272 established there is a complete, genuinely permissive path**, every
component read at payload this pass and **rider-cleared**, not merely licence-labelled.

```
                     ALL COMPONENTS Apache-2.0 / MIT — NO copyleft anywhere in the tree
                     every grant read at payload on 2026-10-17 (see evidence TSV)

  [OpenOLAT          Apache-2.0  10,982 B]   LMS of record: courses, enrolment, assessment, groups
         |                                    rider-cleared: terms section byte-identical to upstream
         |  LTI 1.3
  [tsugi             Apache-2.0  10,273 B]   the sanctioned tool-integration boundary — your agent
         |                                    ships as an LTI tool, so core is NEVER forked
         +---> [Numbas        Apache-2.0  11,357 B]  randomised maths/science assessment, SCORM out
         +---> [Autolab       Apache-2.0  11,324 B]  autograding with per-submission containers
         +---> [scorm-again   MIT          1,072 B]  runtime for the client's existing SCORM estate
         |
  [xAPI-Spec         Apache-2.0  11,525 B]   the telemetry vocabulary
         |
  [lrsql             Apache-2.0  11,357 B]   Learning Record Store — SQL-backed, self-hosted
         |                                    every learner event lands here, on the client's infra
         +---> [pykt-toolkit  MIT          1,066 B]  learner model / knowledge tracing over the LRS
         |
  [academico         MIT          1,094 B]   SIS: enrolment, attendance, results
         |                                    (byte column filled in by p272; vendor page said
         |                                     "licence not named" — the payload says MIT)
         |
  [DeepTutor         Apache-2.0  11,408 B]   the tutor agent, pointed at a self-hosted model
```

### Wiring

1. **Stand up `OpenOLAT`** as the LMS of record. Java/Spring; it behaves like an institutional LMS
   (that is the reason to pick it over Oppia or Kolibri, which are not institutional).
2. **Put every agent behind `tsugi` as an LTI 1.3 tool.** This is the architectural commitment that makes
   the pattern hold: the agent is a *tool*, never a patch. A client can swap `OpenOLAT` for Moodle later
   without touching your code — and if they do, **the copyleft stays on their side of the LTI boundary.**
3. **Emit `xAPI` statements for every learner interaction into `lrsql`.** Do this from day one. The LRS
   is what makes the engagement extensible rather than a one-off tutor, and it is the client's data on
   the client's infrastructure.
4. **Train the learner model with `pykt-toolkit` against the LRS**, not against the LMS database. The
   model then survives a platform migration.
5. **`DeepTutor` as the tutor surface**, pointed at a self-hosted model. ⚠️ Apache-2.0 covers the
   *code*; it says nothing about the *weights* you point it at — that is a separate licence question and
   the one most likely to be missed in a procurement review.
6. **`academico` for SIS data** feeding dropout-risk work; `Numbas`/`Autolab` for assessment;
   `scorm-again` to keep the client's existing SCORM content playable.

### The licence boundary — the point of the pattern

🟢 **There isn't one inside the stack.** Apache-2.0 and MIT both permit proprietary derivative work with
attribution, so **the client's own code can sit anywhere in this tree**, including inside a fork of any
component. Apache-2.0 additionally carries an **express patent grant**, which is usually what a
public-sector legal review is actually asking about.

⚠️ **Three things still to get in writing:**
- **Model weights are not covered** by any grant above (step 5).
- **`xAPI-Spec` is a specification**, Apache-2.0 — implementing it is unencumbered, but conformance
  claims and the ADL trademark are not the same thing.
- **If the client insists on Moodle or Canvas** after all, the pattern degrades gracefully *only* through
  the LTI boundary in step 2. Keep it even if you think you won't need it.

### What this pattern is NOT

🔴 **It is not an ERP.** **No education ERP under MIT or Apache-2.0 has been located**, tested from two
independent channels (`p271`, `p272`). If the engagement needs admissions/fees/library as one system,
`OpenEduCat` is **LGPL-3.0** and that is a different conversation. 🔴 **And it is not a reason to quote a
market size** — see `T36`: the regional AI-in-education figures all trace to one publisher, and LATAM's
span roughly 6×. Size this engagement from the **adoption** datums on `intel/market.md`, not the forecasts.

## P23 — An agent inside the Moodle the client already runs, without the AGPL and without forking

*(new in pass 273)*

**When to reach for it.** The client runs **Moodle** — the default LMS of public education worldwide —
and wants an agent that does real work in it: publishing lesson content, building quizzes, enrolling
cohorts, reading the gradebook. `P14` is the same shape for Canvas. **This is its Moodle counterpart, and
until pass 273 this KB could not offer one without an AGPL-3.0 open-core dependency.**

### The stack

| layer | component | licence | why this one |
|---|---|---|---|
| LMS (incumbent) | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Already installed. **You are not forking it** |
| Agent doorway — **writes** | [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** *(payload, 1,065 B)* | 40 facades + `ws_raw`, upsert-by-`idnumber`, any Moodle 4.x/5.x with Web Services on |
| WS surface for writes | `local_italiciamcp` *(ships in `plugin-companion/`)* | covered by the root MIT; **no grant of its own** | Supplies the `type=write` WS functions Moodle core does not expose |
| Agent doorway — **student side** | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** *(payload, 1,063 B)* | Go; grades, deadlines, notifications, `submit_assignment` |
| Tutor behaviour | [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | MIT | Swappable LLM pipelines, RAG over instructor material. Pedagogically constrained by design |
| Assessment that never leaves the device | [`numbas/Numbas`](https://github.com/numbas/Numbas) | Apache-2.0 | Browser-executed marking — answers a residency objection structurally |
| Integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | Source-code plagiarism detection |

### How to wire it

1. **Enable Moodle Web Services** and mint a token scoped to a dedicated service account — *not* a
   teacher's account. The capability the write functions demand is `moodle/course:manageactivities`; grant
   that and nothing wider.
2. **Install `local_italiciamcp`** as a *Complemento local* and expose only the WS functions you intend to
   use. 🔵 **Enumerate them explicitly** — `db/services.php` declares write functions including
   `upsert_page`, `upsert_quiz`, `update_course_summary` and **`delete_module_by_idnumber`**. A deletion
   endpoint does not belong in a pilot's token.
3. **Run the wrapper over stdio** against your MCP client. Start with the **read-only facades**
   (`listar_alumnos`, `obtener_calificaciones`, `obtener_info_sitio`) and `ws_raw`, which work **without**
   the plugin at all — so phase 1 of the engagement needs no Moodle code installed and no licence
   conversation.
4. **Put a confirmation gate in front of every write.** 🔴 **Non-optional, and it is this base's own
   finding, not a precaution:** `T4` records that this wrapper's writes execute **with no confirmation and
   no disclosure**. Wrap `calificar_manualmente`, `matricular_csv`, `reset_password` and
   `delete_module_by_idnumber` in a human-approval step before a pilot touches a live course. **A grade
   written by an unattended agent is an EU AI Act Annex III problem, not a UX problem.**
5. **Lean on `upsert`-by-`idnumber`.** Every write is idempotent on a stable key, so the content pipeline
   can be re-run from source. **That is what makes the agent output reviewable** — regenerate, diff,
   re-publish.
6. **Keep the tutor out of the LMS.** Pyris behind the agent, Numbas for marking. Moodle stays the system
   of record; nothing pedagogical is forked into it.

### The licence boundary, stated once and precisely

🟢 **The wrapper is MIT and stays MIT** — it links nothing, it speaks REST.
🔵 **The deployed combination (Moodle + the `local_` plugin) is a GPL-3.0 work.** Hosting it for the
client triggers **nothing**, because GPL-3.0 has **no network clause**. Handing the client a *distributed*
image containing the plugin ships that image under **GPL-3.0**.
🟢 **Against the alternative this KB used to offer** —
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server), **AGPL-3.0 *and*
open-core — this is strictly cheaper on both axes**: no network clause, and no tools held behind a paid
tier. See `T41`.

⚠️ **What you are buying, honestly.** `1★ / 1 fork / 59 commits`, and a *burst-and-silence* release
pattern (`CHANGELOG` last moves `2026-05-03`). **Treat it as a reference implementation you adopt and
maintain, not as an upstream that will maintain itself.** The 40-facade surface and the `idnumber` upsert
discipline are the valuable parts, and they are worth more than the maintenance risk precisely because
you can read all of it.

**Rough shape:** 4-6 weeks to a governed pilot on one faculty — week 1 read-only against a Moodle staging
clone with no plugin installed, weeks 2-3 plugin plus gated writes on a single course, weeks 4-6
content-pipeline regeneration and the Annex III human-review record.

## P24 — The agent pilot that survives the district's AI committee: data minimisation at the tool boundary

*(new in pass 274)*

**When to reach for it.** Any engagement where the deliverable is *"an agent over the system the client
already runs"* — which is `P14` (Canvas), `P18` (Ed-Fi), `P23` (Moodle) and, after pass 274, Brightspace,
Blackboard and Open edX as well. 🔴 **Reach for it BEFORE the pilot is scoped, because the objection this
pattern answers is the one that kills these pilots and it is not technical.**

### The objection, in the market's own words

| source | the blocker |
|---|---|
| **GovTech**, reporting **Bridges 2026** | Few districts and colleges have agents in day-to-day operations; leaders *"remain cautious about granting the tools access to sensitive systems and data"* |
| **EdTech Hub** (2026-03-30), Southeast Asia | Education-AI initiatives *"remain short-term and project-based"* |
| This base's own `T24` | *"The OAuth consent a pilot asks a school for is much wider than the feature being piloted … in EMEA that is a GDPR conversation before an engineering one; in the US, FERPA/COPPA"* |

🔵 **Supply-side and demand-side evidence have converged on the same sentence.** The pilots are not
stalling on model quality, licence cost or integration difficulty. **They stall at the consent form.**

### The stack

| layer | component | licence | why this one |
|---|---|---|---|
| Doorway, **with pseudonymisation built in** | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | 🟢 **MIT** *(payload, `1 070` B, `p274`)* | **Opt-in FERPA mode: student names and contact details are replaced with pseudonyms before tool output reaches the model.** The boundary is in the server, not in a prompt |
| Doorway, breadth | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT | 102–126 tools when breadth matters more than minimisation. ⚠️ Cite the tool count as a range |
| Same shape, other platforms | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) · [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) · [`NiccoloSalvini/mcp-blackboard-ucsc`](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) · [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) · [`Kimmahone/edu-workspace-mcp`](https://github.com/Kimmahone/edu-workspace-mcp) | 🟢 all **MIT** *(all payload-read `p274`)* | **Six platforms, five under MIT.** The pattern is portable; only the API differs |
| Audit trail of what the model actually read | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | xAPI statements per tool call: the artefact a committee asks for and nobody has |
| Human sign-off on anything consequential | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) + Iris | MIT | Config-gated AI — *"AI off"* is a deployment setting, which is what `T17`'s five jurisdictions converge on |
| Local inference where residency binds | Ollama / vLLM behind the platform's provider setting | permissive | No prompt leaves the member state (`T6`) |

### How to wire it

1. **Enable the pseudonymisation mode first, then the tools** — not the other way round. The default
   posture of every other server on this shelf is *the model sees real names*.
2. **Scope the OAuth consent to the tools you actually enabled**, and put the enabled list in the SOW as
   a schedule that changes by change-order. ⚠️ `edu-workspace-mcp` reaches **Docs, Sheets, Slides,
   Forms, Drive and Classroom** — an entire tenant — so a Classroom pilot on it is a tenant-wide consent.
3. **Write every tool call to the LRS**, including the ones that returned nothing. A committee's real
   question is *"what did it look at"*, and an empty answer is only credible if the log is complete.
4. **Put a human in front of every write.** Reads can be pseudonymised; a write cannot be anonymous.
5. **Demonstrate the boundary in the pilot review** by showing the model's transcript with pseudonyms in
   it. 🟢 **This is the deliverable that converts a pilot into an operation** — which, per EdTech Hub, is
   the transition the whole category is failing to make.

### What this is worth, said plainly

🟢 **It reframes the sale.** *"Will you let an AI see your student records?"* is a question a district
AI committee answers **no** to by default. *"The model never receives a student's name — here is the
pseudonymisation boundary, here is the log of every field it read, and here is the switch you hold"* is a
different question, and it is answerable in a single meeting.

⚠️ **The counter-example is in the same category and must be read first.**
[`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) carries its own
security disclosure of a **broken access control that exposed other students' personal information** —
same category, same description in a search result, opposite risk posture. 🔵 **Read the disclosure
history, not only the grant** (`T45`).

## P25 — The incumbent you were told to replace already has an MIT doorway

*(new in pass 274)*

**When to reach for it.** A North American higher-education engagement where the client runs
**Blackboard / Anthology** or **Brightspace / D2L**, and the brief — including, until this pass, **this
KB's own market shelf** — says the pitch is to replace it.

🔴 **Do not pitch the replacement.** [`intel/market.md`](../intel/market.md) carried
*"Blackboard / Anthology … replacement engagements; the incumbent's lock-in is the pitch"* while this
base's own trending shelf held **two MIT MCP servers for Blackboard Ultra**. 🔵 **`p267` found exactly
this shape for Canvas and named it — *"the opening is the opposite of migration"* — and the correction
was applied to Canvas alone.** `P25` is that correction generalised to the class.

### The platform ladder, after pass 274's re-count

| platform | doorway | licence *(payload, `p274`)* | platform's own licence | engagement shape |
|---|---|---|---|---|
| **Canvas** | `vishalsachdev/canvas-mcp` · `bruchris/canvas-lms-mcp` | 🟢 **MIT** | AGPL-3.0 | `P14` — extend, never migrate |
| **Moodle** | `MarcosNahuel/moodle-mcp` · `Jawadh-Salih/moodle-mcp-server` | 🟢 **MIT** | GPL-3.0 | `P23` — writes via a `local_` plugin; combination is GPL-3.0, **no network clause** |
| **Google Classroom / Workspace** | `Kimmahone/edu-workspace-mcp` | 🟢 **MIT** | proprietary | ⚠️ Tenant-wide consent — scope it (`P24`) |
| 🆕 **Brightspace / D2L** | `RohanMuppa/brightspace-mcp-server` | 🟢 **MIT** | proprietary | **Extend. No platform decision asked of the client** |
| 🆕 **Blackboard Ultra** | `felipedias-ie/blackboard-mcp` · `NiccoloSalvini/mcp-blackboard-ucsc` | 🟢 **MIT** | proprietary | **Extend** — and the UCSC server works over the **public REST API**, so the cheapest pilot on this ladder needs **no institutional plugin approval** |
| 🆕 **Open edX** | `blend-ed/tutor-contrib-openedxmcp` | 🔴 **AGPL-3.0** | AGPL-3.0 | Already priced on the verticals shelf. ⚠️ `/health` is unauthenticated — fix before any pilot |

### Why this is the stronger pitch, in one paragraph

🟢 **A replacement engagement asks the client to make a platform decision, re-train every user and
migrate years of course content before any AI value appears.** An MIT doorway asks for an API token.
🔵 **And the deliverable stays the studio's and the client's**: the platform's copyleft — where there is
any — never reaches code that talks to it over HTTP. 🔴 **For a proprietary incumbent like Blackboard or
Brightspace there is not even a licence question to answer** — the only question was whether a doorway
existed, and the answer has been yes, on this base's own shelves, for several passes.

⚠️ **Two honest caveats.** The Blackboard and Brightspace servers are **small** (0–59★): they are
**reference implementations, not dependencies** — read them, fork them, own them, and budget for
maintaining what you fork. And every one of these reaches **real student data**, so `P24` is not an
optional companion to this pattern; it is the half that gets it approved.

## P26 — The open automated-grading engagement: the whole TUM stack is permissively graded, and this base said otherwise for three passes *(new in pass 275)*

**When a client asks for it:** *"We want automated feedback on programming and written assignments —
and we want to own it."* Until `p275` this base answered that the tutor was available (Iris, MIT) but the
**feedback/grading engine was all-rights-reserved**, and steered engagements to build that half from
scratch. 🔴 **That advice was wrong.** `ls1intum/Athena` declares `license = "MIT"` in **12 of its 14
manifests**, and the reusable modules are precisely the ones that declare it.

### The stack — four repos, one institution, one licence family

| role | repo | grant | grade |
|---|---|---|---|
| Platform, exercises, CI runner | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | **MIT** | payload (root `LICENSE`) |
| Tutor (**Iris**) *and* the LLM microservice behind it — REST, swappable pipelines, RAG | [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | **MIT** | payload |
| 🔴 ~~`ls1intum/Iris` as a second component~~ | **withdrawn by `p282`** — a name alias of `ls1intum/Pyris`, identical tree `4e2f096df767` | — | [`alias-identity`](../evidence/alias-identity.2026-10-18-p282.tsv) |
| 🟢 **Feedback / grading suggestions — NEW to this pattern** | [`ls1intum/Athena`](https://github.com/ls1intum/Athena) | **MIT** | ⚠️ **metadata** — 12 of 14 manifests; **no licence FILE** (tree enumerated, 691 paths) |

🔵 **Why TU Munich specifically:** this is one institution's stack, so the four pieces are *designed* to
compose — Artemis config-gates Iris, Athena and Hyperion as subsystems rather than bolting them on. You
are not integrating four strangers.

### Wiring it

1. **Deploy Artemis** (Java/Spring + Angular) as the platform of record; it owns exercises, submissions,
   the gradebook and the build/test runner. Keep its AI subsystems **config-gated off** at first — that
   is Artemis's own deployment model, and it is what lets you stage the rollout.
2. **Stand up Pyris** as the only component holding model credentials. Point it at whatever the client's
   data-residency rules allow — a hosted API, or **Ollama/vLLM on their own tenancy** for an EMEA
   sovereignty constraint (`P4`-shaped; see `intel/market.md`'s EMEA section).
3. **Enable Iris** against Pyris for the tutor surface. Iris is *pedagogically constrained by design* —
   hints and leading questions, not answers — which is the single easiest thing to defend to an academic
   integrity committee.
4. 🟢 **Enable Athena for feedback suggestions, installing only the modules the client needs**, because
   each is an independently installable Poetry package: `module_text_llm` (written work),
   `module_programming_llm` (code), `module_modeling_llm` (diagrams/models). `module_programming_apted`
   and `module_programming_winnowing` are **non-LLM** structural/similarity engines — cheaper, offline,
   and worth enabling first as a baseline you can measure the LLM against.
5. **Keep the human in the loop at the boundary Athena already draws:** it emits *feedback suggestions*
   for an instructor to accept, edit or reject. **Do not re-plumb it into autonomous grading** — the
   suggestion boundary is the compliance story, and `intel/market.md`'s LATAM and NA sections both show
   governance, not capability, is what stalls these deployments.

### The two prices, written down

- ⚠️ **Athena's grant is metadata grade.** There is no licence file, and that absence is now
  *definitive* (enumerated, not sampled). Twelve unanimous manifest declarations is the strongest
  metadata channel on this base — `kolibri-design-system` rests on one — but a client's legal team may
  still want a payload. 🟢 **Ask TUM for a `LICENSE` file in the repository root, not for permission:**
  they have already granted MIT twelve times, so this is a request to *document* a grant, which is a far
  easier conversation than requesting one. The earlier *"ask TUM whether there is a licence"* is withdrawn.
- ⚠️ **Artemis is a platform, not a library.** Java/Spring + Angular, 12 437 commits, self-hosted by
  universities. If the client only wants a feedback *service*, **take Pyris + Athena and leave Artemis
  out** — Pyris is explicitly *"the reusable piece: it will serve a stack that is not Artemis."*

### Why this beats the alternative this base used to recommend

🔴 The prior advice — build the grading half yourself — meant writing an LLM feedback pipeline, a
rubric model, and an instructor review UI from zero. The entire reason that advice existed was **a
licence verdict produced by probing one 632-byte file.** 🔵 **Before costing a from-scratch build
because a component is unlicensed, enumerate the tree** (`T46`) **and read every manifest, not just the
root one** (`T47`).

## P27 — Adaptive assessment with a permissive psychometrics core: the layer this base kept recommending and had no licence for

**When a client asks for it:** *"We want adaptive testing — item difficulty, ability estimation, and
scores that stay comparable across forms and across years."* Until `p276` this base could offer a
**learner model** (`OATutor`'s BKT) but had **no permissive answer for the psychometrics** underneath it,
and in particular none for **equating** — the thing that makes this year's score mean what last year's
score meant. 🔴 **The answer was on the shelves the whole time, carried as `no payload`.**

### The stack — three repos, all permissive, all payload- or manifest-read

| role | repo | grant | grade |
|---|---|---|---|
| 🟢 **Item/ability estimation, linking, equating — NEW** | [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | **Apache-2.0** | `pom.xml` `<licenses>`, read `p276` |
| Tutoring + mastery (BKT) front end | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | payload |
| 🟢 **Review scheduling (FSRS) — NEW** | [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | **MIT** | payload, `1 079` B, read `p276` |
| LMS doorway (grades in, roster out) | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) *or* [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **MIT** | payload / manifest+registry |

🔵 **Why these three compose rather than overlap:** they answer three different questions that teams
routinely conflate. `psychometrics` answers *"how hard is this item and how able is this student, on a
scale that survives a change of form"* (IRT: Rasch/2PL/3PL/GPCM, plus **Mean-Mean, Mean-Sigma and
Stocking-Lord linking** and score equating). `OATutor` answers *"has this student mastered this skill
yet"* (BKT, per-skill, within one course). `fsrs4anki-helper` answers *"when should this come back"*.
**Mastery is not difficulty and neither is retention.**

### Wiring it

1. **Calibrate the item bank offline with `psychometrics`** (JVM; modules `-irt`, `-ctt`, `-factor`,
   `-fmm`). Fit IRT parameters on historical response data before any agent touches a learner. Treat this
   as a batch job with a reviewed output, not a service — calibration is a measurement decision, and it
   wants a psychometrician's signature on it.
2. **Expose calibrated parameters as read-only reference data** (a table keyed by item id: `a`, `b`, `c`,
   plus the form and the calibration date). Everything downstream reads this; nothing downstream writes it.
3. **Select the next item in the agent layer**, using ability estimate + target information, and keep the
   selection rule **declarative and logged**. 🔵 This is the single most audited line of an adaptive test —
   write it so it can be replayed from the log alone.
4. **Keep `OATutor`'s BKT for mastery and hint sequencing**, driven by the same response stream. Do not try
   to make IRT do mastery or BKT do scaling.
5. **Hand long-term retention to `fsrs4anki-helper`**, scheduling review of items the learner has passed
   rather than re-testing them adaptively. Its load-balancing matters once a cohort shares a calendar.
6. **Write scores back through the MCP doorway**, never by direct DB write into the LMS.
7. 🔴 **Re-equate when the form changes, and say so in the report.** `psychometrics`' linking methods are
   the reason this stack can promise year-over-year comparability — a promise an engagement should only
   make if step 7 is actually scheduled.

**Licence boundary:** everything above is **MIT / Apache-2.0**, so the client's proprietary item bank,
selection policy and reporting stay proprietary. ⚠️ **The one trap is data, not code:** calibration needs
historical response data, which is student data — see `P24`'s pseudonymisation boundary, and note the EU
position in `P29` if the cohort is in the EEA.

**Timeline:** 6–8 weeks to a calibrated bank and a replayable selection rule on one subject; equating
across two forms adds ~3 weeks and needs an anchor-item design agreed up front.

## P28 — Two MIT doorways into Canvas, and the one this base told you not to use is the more capable

**When a client asks for it:** *"Our LMS is Canvas and we want an agent inside it — not another portal."*

🔴 **This pattern exists because of a correction.** This base published
[`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) as *"NONE — no licence
statement … Do not use. No licence = all rights reserved."* `p276` read `package.json` l.66
(`"license": "MIT"`) and the npm registry (`canvas-mcp-server`, **MIT across 19 published versions**).
**Withdrawn.** Canvas now has **two** MIT doorways on this base.

| doorway | grant grade | pick it when |
|---|---|---|
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT**, payload read (`1 070` B) | 🟢 **Compliance is the gating concern** — it ships **opt-in FERPA pseudonymisation** |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **MIT**, **manifest grade** + registry (**no payload in tree**) | 🟢 **Coverage is the gating concern** — 54 tools, `v2.3.1`, student *and* account management, vitest suite |

### Wiring it

1. **Choose by gate, not by star count.** If the client's blocker is *"we will not give an agent access to
   student records"* — which `p274` recorded as the market's own stated reason for not deploying agents —
   start with `bruchris` and turn pseudonymisation **on** before the first demo.
2. **Run the MCP server as the only component holding the Canvas API token**, scoped to the narrowest
   Canvas role that satisfies the use case. Agents get tools, never credentials.
3. **Compose, don't fork.** Where `bruchris` has the compliance posture and `DMontgomery40` has the tool
   you need, run **both** servers and let the agent hold two tool namespaces. That is what MCP is for, and
   it keeps each upstream updatable.
4. 🔴 **Pin `DMontgomery40` by version and vendor the grant.** Its `files` array names a `LICENSE` that is
   **not in the git tree**; the grant lives in the manifest and the registry. **Record the npm version,
   the `package.json` licence line and the registry metadata in the engagement's licence file** — a
   manifest grade is real but thinner than a payload, and a future maintainer must not have to re-derive it.
5. **Write back through the LMS's own gradebook semantics** (assignment, submission, grade), so the
   institution's existing audit trail stays the system of record.

**Licence boundary:** both doorways are **MIT** — no copyleft reaches the client's agent code. The
constraint is **data**, not licence: FERPA in the US, and Annex III in the EEA (`P29`).

**Timeline:** 2–3 weeks to a working tool surface against a Canvas sandbox; add 2–3 weeks for a
pseudonymisation review if student records leave the institution's tenancy.

## P29 — The EMEA education build that is Annex III-ready before Annex III bites

**When a client asks for it:** *"We are an EEA institution (or we sell to them) and we want AI in
admissions, assessment or tutoring without betting the roadmap on the AI Act."*

🟢 **The date moved and the architecture did not.** The **Digital Omnibus — Regulation (EU) 2026/1744**
(in force `2026-07-27`) **deferred Annex III high-risk obligations from `2026-08-02` to `2027-12-02`**.
⚠️ **Grade: secondary-convergent, four independent legal publishers; the Official Journal text is UNREAD
from this environment (`eur-lex.europa.eu` CONNECT 403) — verify before quoting a date to a client.**

🔴 **What is already in force, and catches education first:**

| in force now | what it means for the build |
|---|---|
| **Ban on inferring emotions in education settings** (since Feb 2025) | **Not a deferred duty — a prohibition.** No engagement-detection, no affect-based proctoring. Design it out; do not plan to switch it off later |
| **Article 4 AI-literacy duty** | The institution owes staff and student literacy — a deliverable a studio can actually supply |
| **Article 50 transparency** (from `2026-08-02`, marking grace to `2026-12-02`) | Disclose AI interaction and mark synthetic output **now** |

🔵 **And who you are in the regulation:** a studio *building* the system is the **provider** — risk
management, data governance, technical documentation, conformity assessment, EU-database registration.
The institution *deploying* it owes instructions-compliance, **human oversight** and incident logging, and
a **public** institution owes a **Fundamental Rights Impact Assessment before first use**. **The heavy
half is the studio's.**

### Wiring it

1. **Start from a permissive stack you can document end to end** — `P26`'s TUM four (`Artemis`, `Iris`,
   `Pyris`, `Athena`, all MIT) is the strongest option here precisely because one institution's stack
   leaves one coherent paper trail.
2. **Keep the model boundary sovereign:** `Pyris` as the only credential holder, pointed at **Ollama or
   vLLM in the client's own tenancy** where residency is a constraint.
3. 🔴 **Classify every feature against Annex III on day one**, not at audit. **Admissions, assessing
   learning outcomes and determining level of education are high-risk**; automated grading, adaptive
   learning and proctoring are commonly read as high-risk; scheduling is low-risk; a tutoring chatbot
   mainly owes **transparency**. Write the classification into the backlog as a field on each epic.
4. **Keep the human-decision boundary where `Athena` already draws it** — *suggestions* an instructor
   accepts, edits or rejects. This is simultaneously the pedagogy argument, the Annex III oversight
   argument and the academic-integrity argument. 🔵 **One architectural choice answers three committees.**
5. **Build the FRIA with the deployer, as a deliverable** — it is the institution's duty, it needs facts
   only the builder has, and an engagement that produces it is far harder to displace.
6. **Treat `2027-12-02` as the audit date, not the start date.** 16 months is less than the life of a
   platform built in 2026; a system that reaches that date un-classified is re-architected under
   deadline.

⚠️ **One EMEA supply warning from `p276`'s enumeration:** the European Commission's own **European Digital
Credentials** reference implementation
([`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials))
carries **no licence grant across `2 970` enumerated paths** and no `license` element in its `pom.xml`.
**Do not plan a credential-issuance deliverable on it as open source** — read its terms with the client's
counsel, or build issuance on a granted stack.

**Timeline:** 10–12 weeks to a classified, documented, FRIA-supported pilot on one high-risk use case;
the classification and documentation are roughly a third of it and are the part that cannot be compressed.

## P30 — The APAC engagement briefed per jurisdiction, because there is no APAC requirement to build against *(new in pass 277)*

**When a client asks for it:** *"We operate schools (or sell edtech) across Asia-Pacific and we want one
AI roadmap for the region."*

🔴 **Refuse the premise in the first meeting, politely and with the table.** There is no APAC education
AI requirement. There are five large, incompatible national ones, and they disagree on the two things
that drive architecture: **who the AI may face, and who must be trained.** `p277` established the cells
first-hand-by-query; see [`intel/market.md`](../intel/market.md#apac).

| jurisdiction | the binding thing | what it forces into the build |
|---|---|---|
| **China** | *AI Plus Education* plan (Apr 2026 → 2030) + May 2025 guides | **Curriculum delivery at hour floors** (Gr 1–4 ≥6 h/yr, 5–9 ≥10 h/yr, 10–11 ≥1 h/fortnight) and a **teacher AI-literacy standard tied to qualification exams** → the deliverable is *courseware plus teacher certification tracking*, not a tutor |
| **India** | CBSE Circular Acad-15/2026, session 2026-27 | **Classes III–VIII, no board exam, project-based** → assessment must be **formative and portfolio-shaped**; a summative scoring engine is the wrong product. Scope is **CBSE only** |
| **Japan** | MEXT Ver. 2.0 ("human-centred use") | **A person must make the final judgment and own the deliverable** → human-in-the-loop is a *written requirement*; and the funded majority is **teacher-administrative**, not in-class |
| **Singapore** | Teacher AI Literacy Roadmap (Module 1 due end-2026) | **Time-bound compulsory teacher training** → the near-term buy is *training and workload relief*; and **lower primary is deliberately excluded** from AI tools |
| **South Korea** | AI digital textbooks, status revoked | **Adoption is voluntary and the regulator is active** → nothing ships without a pilot and a DPIA. See `P31` |

### Wiring it

1. **Pick the jurisdiction first, then the stack** — in that order, because the jurisdiction decides
   whether you are building courseware, a teacher tool, or a tutor.
2. **For China and India (curriculum delivery, scale, often offline/low-connectivity):** start from
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (**MIT**, offline-first) with
   [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
   (**MIT**, metadata grade) for the UI; generate and version the curriculum artefacts with
   [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) (**MIT**,
   ADDIE pipeline: syllabus → slides → assessments). **India's "no board exam" rule means you wire the
   assessment output to a portfolio, not a gradebook.**
3. **For Japan and Singapore (teacher-facing, workload-first):** put the agent behind the LMS the client
   already runs — [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (**MIT**) or
   [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) (**MIT**, ⚠️ its write half
   needs a GPL-3.0 companion plugin — see `P23`) — and keep **every** write behind an explicit teacher
   confirmation. **That confirmation is not UX polish in Japan; it is the policy.**
4. **Where tutoring is in scope, use a pedagogically-constrained tutor, not a general assistant:**
   [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) *(one repository — `Iris` is its tutor's name, not a second clone)*
   (**MIT**) give hints and leading questions rather than answers, and `Pyris` is the reusable half —
   a REST API over swappable pipelines that will serve a stack that is not Artemis.
5. **If procurement excludes copyleft**, the platform is
   [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (**Apache-2.0**, payload-verified `p272`,
   `master/LICENSE` 10,982 B) — still the only permissive full LMS on this base's shelf.
6. **Never present one APAC compliance slide.** Produce one per jurisdiction in scope; the cost of the
   extra slides is hours, and the cost of the single slide is the Korea outcome.

**Timeline:** 2–3 weeks per jurisdiction for the compliance brief and the stack decision, run in
parallel; 8–10 weeks to a first deliverable in the **one** jurisdiction you start with. **Do not start
in all of them.**

## P31 — The pilot-gated rollout that survives a privacy regulator, built backwards from Korea's reversal *(new in pass 277)*

**When a client asks for it:** *"We have ministry or district backing and we want to roll out to every
school next term."* 🔴 **That sentence is the Korea precondition.** South Korea had the mandate, the
budget and national coverage, and the programme was **unwound in four months**: status revoked, adoption
**37% → 19%**, **two data-protection violations** found, and a **state auditor finding that it was
brought into schools without a pilot**. The causes were factual errors, privacy, screen time and teacher
workload — **all four a delivery failure, none a model failure**.

### Wiring it — the four failures, each with a concrete counter-measure

| the Korean failure | what you build instead |
|---|---|
| **No pilot** | A gate, not a phase: **one district, one subject, one term**, with the success criteria written and signed *before* the build. The auditor's finding is that this step was skipped — so it is the deliverable that protects the programme |
| **Privacy violations** | 🟢 **No real pupil data in the pilot at all.** Generate the test corpus with [`sdv-dev/SDV`](https://github.com/sdv-dev/SDV) — ⚠️ **Business Source License 1.1, NOT open source** (`LICENSE`, 4,818 B, read first-hand `p277`; Licensor DataCebo, Inc.). **Its Additional Use Grant permits use and derivatives EXCEPT to offer a "Synthetic Data Service"** — a commercial offering letting third parties access the functionality. 🔵 **So: generating synthetic student records inside a client deliverable is permitted; reselling that generation as a service is not.** Record that distinction in the SOW. Then enforce minimisation at the tool boundary per `P24` |
| **Factual errors in generated content** | Ground every learner-facing claim in the institution's own material and cite it: [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**) keeps generated artefacts tied to their sources, and [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) (**MIT**) teaches from the institution's slides with **page-level citations**. 🔵 **A wrong answer with a citation is a correctable content bug; a wrong answer without one is a programme risk** |
| **Teacher workload went UP** | Measure it as a success metric, not a side effect. Ship the teacher-facing half first — grading suggestions via [`ls1intum/Athena`](https://github.com/ls1intum/Athena) (**MIT**, metadata grade, 12 of 14 manifests) whose `module_text_llm` / `module_programming_llm` / `module_modeling_llm` are independently installable Poetry packages, so you can deploy **one** module and show the hours back. **Japan funded 100 municipalities on teacher administration and 10 in class — follow the money, not the demo** |

🔵 **Where adaptive assessment is in scope**, keep the psychometrics honest with
[`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) (**Apache-2.0**, `pom.xml`
`<licenses>`) for IRT linking and score equating, and
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (**MIT**) as the reference ITS with Bayesian
Knowledge Tracing. **An adaptive claim you cannot equate across forms is the next factual-errors
finding, one layer down.**

🔴 **The one thing to put in writing before anything is built:** *a mandate is not adoption.* Korea's
decline from 37% to 19% happened **while the mandate was still in force**. Price the change management,
or the rollout number is the number that falls.

**Timeline:** 3–4 weeks to the signed pilot gate and the synthetic-data corpus; one term for the pilot
itself, which **cannot be compressed** — compressing it is the finding the auditor made.

## P32 — The licence intake gate, sold as a deliverable, because the client's own CI structurally cannot do it *(new in pass 278)*

**When a client asks for it:** *"Our security team already scans dependencies — we're covered on open
source licensing."* 🔴 **They are covered on what the manifest SAYS.** Every licence gate in a normal
CI pipeline reads the **declared field**: `npm ls --json`, `pip-licenses`, most SBOM generators and most
SCA scanners. 🔴 **On this base's own education shelf, five addresses declare a permissive licence in a
manifest while committing something else entirely** — and the client's gate returns *"permissive,
pass"* on all five:

| address | its manifest declares | what it actually commits | what ships undetected |
|---|---|---|---|
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | **MIT** | **AGPL-3.0** (`LICENSE`, 34,523 B) | a **network-copyleft** obligation on a hosted deliverable |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | **MIT** | **AGPL-3.0** (`LICENSE.md`, 34,143 B) | same |
| [`tadreeb-lms/tadreeblms`](https://github.com/tadreeb-lms/tadreeblms) | **MIT** | **AGPL-3.0** (`LICENSE`, 34,523 B) | same |
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | **MIT** | **"Fair Code License" v1.0** (10,830 B) | 🔴 **€100,000 past 1,000 users, plus 5%** |
| [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | **MIT** | 🔴 **`CC-BY-NC-SA-4.0`** (1,891 B) | a **non-commercial** bar on a client deliverable |

🟢 **The rule the gate enforces, in one sentence:** *a manifest licence field is a **HINT**; the
committed licence file, on the **default branch**, at a **pinned SHA**, is the **GRANT**.*

### Wiring it

| step | what you build | why that exact shape |
|---|---|---|
| **1. Resolve the ref** | `git ls-remote --symref <repo> HEAD` → the **default branch**, then pin the **SHA** | 🔴 Guessing `main` is a measured failure on this base: `kolibri` is **MIT on `develop` and 404 on `main`** (`p269`). A grant read on the wrong ref is not this repository's grant |
| **2. Read the payload** | Fetch the licence file from `raw.githubusercontent.com` at the pinned SHA; classify on the **title block**, never the body | 🔴 GPL-3.0 **section 13 is titled** *"Use with the GNU Affero General Public License"*, so a body grep labels every GPL-3.0 payload AGPL-3.0 (`P171`). Reuse one hardened classifier — this base has `compose/code/lib/license_family.sh` and rewrote it from scratch once, reintroducing the defect |
| **3. Read the manifest** | `package.json` · `pyproject.toml` · `composer.json` · `Cargo.toml` · `pom.xml` — **per package, not only at the root** | 🔴 `ls1intum/Athena` declares **MIT in 12 of 14 manifests**, all in subdirectories, while its **root** `pyproject.toml` is a 632-byte workspace stub with the string `license` **absent**. A root-only reader calls a permissive monorepo unlicensed |
| **4. Read a registry** | npm / PyPI / Packagist for the published artefact | 🟢 This is the channel that settled `mcp-canvas-lms`: **MIT across 19 published versions** when the tree carried no licence **FILE**. 🔵 Note the wording — `make gate-enumeration` rejected an earlier draft of this cell that said *"no grant at all"*, because the manifest declares one. **A gate catching the pattern that teaches the two-channel rule for forgetting it is the strongest argument for the gate** |
| **5. Compare on a TIER, not for equality** | `direction(manifest, payload)` → the manifest **overstates** (🔴 bills), **understates** (🟡 over-blocks) or is **same-tier, wrong name** (🟡 attribution changes) | 🔵 The two directions do not cost the same. Measured: **7 of 10** contradictions overstate. Equality cannot express *which way* the error leans |
| **6. Prove an absence, never ladder it** | `git clone --depth 1 --filter=blob:none --no-checkout` + `git ls-tree -r`, and **publish the path count** | 🔴 A path ladder was measured at a **~1-in-4 error rate** over 43 rows (`p275`/`p276`). *"No licence in 15 paths"* and *"no licence in 15,448 paths"* are the same sentence and different claims |
| **7. Ask WHOSE grant a path carries** | Exclude vendored, asset, icon, translation and source paths before treating a licence-like path as the grant | 🔴 `LearnPress/learnpress`: **1,985 paths**, and **both** licence-like paths belong to a **vendored dependency** and a **`.php` source file**. An SCA scanner reports *"GPL-3.0 found"* and attributes a dependency's grant to the parent |

🔵 **Make it a STEP, not a document.** This base's own experience is the argument: it published a
*"manifest is a hint"* rule in `p121` and then spent a later pass rebuilding the class, because the
rule lived in prose. The runnable version — `make gate-conflict` plus
[`compose/code/p278-channel-conflict/`](code/p278-channel-conflict/) — re-derives every verdict on
every run. **A rule that has to be remembered is not a control.**

⚠️ **Price it honestly.** Steps 1–5 are a few days of work on a repository list the client already has;
step 6 needs egress and time proportional to tree size. **The deliverable that sells it is step 5's
report**, because it names, per dependency, what the client's existing gate waved through.

## P33 — The compliance-deadline engagement, scoped to a JURISDICTION rather than a region *(new in pass 278)*

**When a client asks for it:** *"What do we need to do about AI in education policy?"* 🔴 **There is no
regional answer to that question, and three passes of this base's own blanks are the evidence** — EMEA
looked quiet until `p275` queried the **instrument**, APAC looked quiet for ten passes until `p277`
queried the **ministries**, and LATAM looked like *"intention rather than policy"* until `p278` queried
the **five countries separately** and found a statute. **Ask which jurisdiction, then build against the
instrument that binds there.**

### The three engagement shapes, and how to tell which one you are in

| shape | where it is live now | the deliverable |
|---|---|---|
| 🔴 **A statute ahead of its guidance** | **Colombia — Ley 2626 de 2026** (sanctioned **Aug 2026**): computational thinking, programming, **AI**, data science and digital citizenship phased into basic and secondary education; **binding on official public schools**, an optional model for private ones; **MEN must act jointly with MinTIC and MinCiencias, so the implementing *lineamientos* do not exist yet** | 🟢 **Curriculum mapping against the statute, before the guidance lands.** The client's question is *"how do we comply before MEN publishes"*, which is an implementation engagement **with a deadline and no spec** — so the deliverable is a defensible mapping plus the evidence trail that justifies it |
| 🔴 **A deadline already in the past** | **Ohio** — every district had to **adopt an AI-use policy by 1 Jul 2026**. **Maryland SB 720 (Ch. 634)** and **Idaho SB 1227** oblige **AI literacy and teacher training** | 🟢 **Policy remediation, then the training programme.** Teacher PD is staffable work with a statutory hook. 🔵 Build the teacher-facing half first: Japan funded **100 municipalities on teacher administration against 10 in class** — follow the money, not the demo |
| 🟡 **No rule at all, and the buyer is lower down** | **Canada** — no binding provincial rule in **Ontario, Alberta or BC**; education is **provincial jurisdiction**; the Alberta Teachers' Association's own summary is that there is *"not a lot of policy at the jurisdictional level"* | 🟢 **Sell the policy itself to the board or district.** BC's 2023 ministry framework (**seven areas of consideration**) and the **ASBA**'s Sept 2024 guidance are the scaffolding to adapt, not competitors |

### What you build on, in every one of the three

🟢 **The permissive stack does not change with the jurisdiction** — only the obligation does:
[`moodle/moodle`](https://github.com/moodle/moodle) or [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)
(**Apache-2.0**) as the platform; [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) (**MIT**
core — ⚠️ **26 of 38 modules free, 12 sold separately: scope the modules in the SOW**) where the need is
administrative rather than instructional; [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (**MIT**)
as the reference ITS; [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents)
(**MIT**) for the syllabus → slides → assessment pipeline a curriculum mandate actually asks for; and
[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) + [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris)
(**MIT**) where automated feedback is in scope.

🔵 **Two framings that travel across all three shapes.** **(1)** Teach *about* AI before teaching
*with* it: Brazil's MEC document sets **7 diretrizes and 12 aprendizagens** for teaching about AI with
the **BNCC** as the starting point, and China, India and Colombia all legislate the curriculum side
first — so an *AI-literacy* curriculum is the lowest-risk opening deliverable almost everywhere.
**(2)** The data-protection floor is usually statutory even where the pedagogy is only guidance:
Brazil's **LGPD (Lei 13.709/2018)** and **ECA Digital (Lei 15.211/2025)** are transversal and
**mandatory** inside an otherwise non-binding orientation. **Build to the floor, not to the guidance.**

⚠️ **Evidence grade, stated because it changes what you may put in a proposal.** Every policy
instrument above is **SECONDARY-CONVERGENT, PRIMARY UNREAD**: the primary addresses were located and
**none is reachable from this environment**
([map](../evidence/egress-map.2026-10-17-p278.tsv)). 🔴 **Before a statute goes into a client-facing
document, read the official text** — above all **Ley 2626**'s scope, where *"binding on public,
optional for private"* decides whether a private-school client has an obligation at all. 🔴 And two
figures that circulate widely are **not** usable: **"27 states"** counts **active bills**, not enacted
laws, and the **"$2.5B K-12 AI grant program"** traces to a single weakly-sourced blog.

---

## P34 — The monorepo grant audit, because what a client vendors is a DIRECTORY and not a repository *(new in pass 279)*

**When a client asks for it:** *"We're reusing this open-source LMS — legal says it's MIT, are we
clear?"* 🔴 **A monorepo does not have "a licence". It has one per package, and your client is copying
a folder.**

### The evidence this pattern is built on, measured on this base's own shelves

`p279` rebuilt the channel sweep to walk manifests **per package** across 14 carried rows. Three carry
**more than one distinct declaration among their own manifests**:

| repository | what its own manifests declare | what a studio must notice |
|---|---|---|
| 🔴 [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) | root `composer.json` **GPL-3.0-or-later** · root `package.json` **ISC** · `packages/dependecy-extraction-webpack-plugin/` **MIT** | 🔴 **Three grants in one repository — and the two ROOT manifests disagree with each other.** Which applies depends on what you took |
| 🔴 [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | root **MIT** · `apps/api/` **ISC** *(`@classroomio/api`)* | 🟢 Both permissive, so nothing you may *do* changes — 🔴 **but the attribution obligation differs per directory** |
| 🔴 [`ls1intum/Athena`](https://github.com/ls1intum/Athena) | **12 of 14** manifests **MIT**; root `pyproject.toml` **silent** | 🟢 Unanimous where it speaks — 🔴 **and a root-only reader sees NOTHING**, which is how this row spent a pass ungraded |

### The procedure

```bash
# 1. ENUMERATE the tree -- never guess a path (p275)
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> /tmp/t
git -C /tmp/t ls-tree -r --name-only HEAD > /tmp/paths.txt

# 2. walk EVERY manifest, not the root one           (12 of Athena's 14 are subpackages)
# 3. reject vendored paths with the SHARED predicate (is_bundled -- and see warning 1)
# 4. read the ROOT manifest's `name` against the slug (T229-M2 -- and see warning 2)
make conflict-sweep SLUGS=/tmp/slugs.txt    # all four, with the accounting columns
```

### 🔴 Two warnings that each cost a pass, so put them in the SOW

1. 🔴 **A vendored dependency's manifest is not a per-package declaration, and a path list will not
   reliably separate them.** `tadreeblms` vendors `moment`, `swiper`, `tailwindcss`, `prismjs` and
   three CKEditor builds under **two different directory spellings in the same repository**
   (`public/assets/libs/` and `resources/views/backend/assetslib/libs/`). Excluding the first still
   left a false *"the subpackages disagree"* from the second. 🔵 **A vendored-path exclusion is a
   floor; read the package names of anything surprising.**
2. 🔴 **A root manifest may not be the project's own.** `tadreeb-lms/tadreeblms`'s root
   `composer.json` declares `"name": "rappasoft/laravel-boilerplate-upgraded"` — **a Laravel
   boilerplate fork serving upstream's file**, so its `MIT` describes `rappasoft`, not the LMS your
   client is adopting. 🟡 **But a name that merely DIFFERS is innocent:** `mcp-canvas-lms` names its
   package `canvas-mcp-server`, `Studivexa` names its `student-management-backend`, and both are
   plainly their own. **The name is a flag for a human, never an automatic rejection.**

### What you sell

🟢 **A per-directory grant map of everything the client intends to vendor** — committed payload beside
declared manifest for each, plus an explicit list of directories whose obligation differs from the
root's. 🔵 **Two to three days across a handful of repositories, run on `make conflict-sweep` plus
judgement.** It prevents the one outcome legal cannot remediate afterwards: **shipping an AGPL or
non-commercial obligation that a manifest-reading check called MIT.** 🔴 `leemonade/leemons` has **114
manifests** — nobody does this by eye.

---

## P35 — The "already refuted" intake check, sold as the research function a client cannot staff *(new in pass 279)*

**When a client asks for it:** *"Our people keep bringing us contradictory answers on AI regulation —
can you just tell us what's true?"* 🟢 **Yes — and the durable deliverable is not the answer. It is the
mechanism that stops the wrong answer arriving again.**

### The evidence, and it is this base's own worst recurring error

🔴 **The claim that the EU AI Act's education high-risk obligations took effect in August 2026 has
arrived from an inbound source in FIVE separate passes**, each from a source these shelves do not
cite, each caught by a careful reader. It is wrong by **fifteen months in the direction that tells a
client they are bound now.** Correct: **Annex III point 3 applies `2027-12-02`**; **`2026-08-02` is
Article 50 transparency**, which *is* live.

🔵 **Note what did NOT work.** This base had settled the question on `2026-10-15`, published the
instrument number, and flagged the stale claim four times. **None of it stopped the fifth arrival**,
because a settled fact on a shelf does not inspect what the next search returns.

### The build, in two halves — a client needs both

| half | what it checks | result here |
|---|---|---|
| 🟢 **Outbound** | does OUR OWN prose assert a claim we refuted? | 🟢 clean — **0 ASSERTED** across 10 shelves, 28,000+ lines |
| 🔴 **Inbound** | does a source we JUST READ assert it? | 🔴 **2 hits in one pass's research file** |

One classifier, one table of refuted claims, checked in both directions — so the claim is defined
once. Four verdicts, so a report is not a rejection: `ASSERTED` *(the source states it — stop)*,
`ATTRIBUTED` *(reporting verb, no verdict — warn)*, `QUOTED` *(quoting someone else — clean outbound,
**not** clean inbound)*, `CORRECTED` *(states it **and** refutes it — clean)*.

### 🔴 The two vocabulary gaps, because a client's table will have the same ones

1. 🔴 **Know the AMENDING instrument, not just the Act.** The table knew `AI Act` and not **`Digital
   Omnibus`** — which is what every source writing about the *delay* actually names. **A table that
   knows an Act and not its amending instrument has a hole the size of the whole conversation about
   the change.**
2. 🔴 **A claim can be asserted by DENYING its correction.** *"Until a formal legislative extension is
   enacted, the obligation **remains** August 2, 2026"* carries no *effective* or *full effect* token
   at all. 🔵 And the first fix spelled the date `august 2026`, missing **`August 2, 2026`** — the one
   spelling a reader actually meets.

### What you sell

🟢 **A refuted-claims register for the client's own domain, plus the two-directional gate that reads
it**, wired into whatever their analysts already use. **The register is the asset:** every
expensively-wrong claim their team has re-adjudicated, written down once with its refutation and its
instrument number. 🔵 **Price it as research infrastructure, not a report** — a report answers this
quarter's question; this stops the question being re-asked every hour by whoever searched last.
🔴 **And wire it in rather than document it:** this base's own gate for this exact class existed,
passed its controls, and **had never been run by `make hooks` in 56 passes.**

## P36 — Teacher-mediated K-12 tutoring for the three jurisdictions that prohibit unsupervised use

**Where it is live now:** 🟢 **China** (MOE's *Guide to Using Generative AI in Primary and Secondary
Schools*, 2025 Edition — primary pupils barred from autonomous open-ended generative tools) ·
🟢 **Singapore** (teacher roadmap — **P1–P3 print-first, no chatbots**, MOE's own SLS tools from
**P4**) · 🟢 **Brazil** (`Parecer CNE/CP nº 15/2026` — **autonomous use prohibited up to the 5th
year**; *pending homologation, reported imminent with amendments, **12-month adequacy window from
publication***). See [`../intel/trends.md`](../intel/trends.md) `T67`.

**Why it is a pattern and not a filter:** the constraint is on **who makes the request**, not on what
comes back. A content filter in front of a pupil-initiated chat turn satisfies none of the three.

### The wiring

| layer | what to use | licence | why this one |
|---|---|---|---|
| tutoring engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) — **Socratic** and **Quiz** modes | **Apache-2.0**, held by **Data Intelligence Lab, The University of Hong Kong** *(payload-verified `p280`)* | 🟢 the holder is an **institution**, so the grant does not rest on one maintainer — the strongest provenance on this shelf |
| knowledge state | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | the pupil model must live **outside** the chat surface, because the pupil may not drive the chat surface |
| request routing | the **LMS role model** — Moodle *(GPL-3.0)* capabilities or Open edX *(AGPL-3.0)* roles | copyleft **at the platform**, permissive at the extension point | 🔵 the teacher is the authenticated requester; the pupil's client never holds a prompt. `p273`: the Moodle plugin door is permissive, so the extension you write is yours |
| transport | an **MCP server** per data source, behind the LMS's own auth | per server | `T3`: MCP is the integration layer; keep the pupil-facing surface with **no tool of its own** |

### The flow, which is the whole pattern

1. The **teacher** selects a class, an objective and a pupil or group inside the LMS.
2. The platform — **not the model** — resolves the pupil's knowledge state from `pykt`.
3. `DeepTutor` runs in **Socratic** mode against *that* state and returns **candidate prompts,
   hints and a next step**, to the **teacher's** screen.
4. The teacher releases a step to the pupil. 🔴 **The pupil's surface renders released content and
   accepts bounded replies only** — no free-text prompt reaches a model.
5. Every release and every pupil reply is written to the LMS's own log, **per pupil, per objective**.

### What the deliverable is

🟢 **A release gate and an audit trail, not a chatbot.** The sellable artefact is step 3→5: the
teacher-facing review queue, the release control, and the per-pupil record of what was released and
by whom. 🔵 **That record is also what answers `T68`** — Maryland `SB 720` bars AI as the primary
basis for grading or discipline, and Brazil's amendment bars AI from determining approval or failure,
so a system that already records *human released this, human adjudicated that* has the evidence both
regimes ask for. 🔴 **Build the teacher-facing half first**: in all three jurisdictions it is the only
half that is unambiguously permitted today.

### What to check before quoting

- 🔴 **Brazil: the binding text is not the text that was approved.** Homologation is reported
  imminent **with amendments**; re-check `pcp015_26.pdf` against the DOU homologating act, and start
  the **12-month** clock from that publication, not from `2026-09-01`.
- 🟡 **China: brief the two 2025 guidelines and Beijing's ≥ 8 class hours per pupil per year.** The
  *"required in all schools from 2026–27"* claim is **secondary-only** and should not appear in a
  proposal.
- 🟢 **Licence surface:** `DeepTutor` Apache-2.0 and `pykt` MIT are both **payload-verified**. The
  platform is copyleft; your extension is not, provided it stays on the documented extension point.

## P37 — Assistive essay grading where the regulator PERMITS the suggestion and FORBIDS the mark *(new in pass 284)*
**Target:** Brazilian institutions under `Parecer CNE/CP nº 15/2026`; Vietnamese institutions under
`Decision 33/2026/QD-TTg`; EU institutions building ahead of Annex III pt 3 (`2027-12-02`)
**Timeline:** 5–7 weeks

🔵 **Why this is not `P10`.** `P10` produces the mark **deterministically, from a test suite**, and
the model is confined to explaining an already-computed result. That is the right architecture for
programming and notebook work and it has **nothing to offer an essay** — a test runner cannot grade
prose. 🟢 **`p284` found that Brazil's MEC, amending the CNE text before homologation, explicitly
PERMITS AI as a `primeiro filtro` in essay and dissertation correction** while forbidding an
automated system from assigning the final mark or deciding approval/failure. **That is a larger
permitted scope than `P10` assumes**, and this pattern is the one that uses it.

```
[Artemis  MIT]                      the platform: text exercises, submissions, auditable runner
        |
[Athena  MIT (metadata, 12/14)]     deploy ONE module: module_text_llm
        |                           -> a RUBRIC-ANCHORED feedback SUGGESTION per criterion,
        |                              each with the span of text it is about
        v
[suggestion record]                 status = PROPOSED.  Carries: rubric criterion, span,
        |                           suggested band, model+prompt version, timestamp.
        |                           🔴 It is NOT a grade and is never written to a grade field.
        v
[teacher review surface]            accept / edit / reject, per criterion, with the span shown
        |                           🔴 No "accept all".  The mark field is writable ONLY here.
        v
[mark assignment]                   the teacher's value is the ONLY value recorded as the mark
        |
        +--> [lrsql  Apache-2.0]     xAPI record of BOTH values and who moved the state
        |                            -> this is the artefact that proves compliance
        v
[bruchris/canvas-lms-mcp  MIT]      optional: write the mark back to the Canvas the client runs,
                                    with its opt-in FERPA pseudonymisation on the way in
```

**Wiring.** Three properties do the regulatory work, and each is a build decision rather than a
policy sentence:

1. **Two fields, not one.** `suggested_band` and `mark` are separate columns with separate write
   permissions. The model's credential can write the first and **cannot** write the second. *"AI did
   not assign the grade"* is then a schema property, demonstrable from the grant table.
2. **No bulk accept.** The prohibition is on the automated system *deciding*. An "accept all 180
   essays" button reintroduces the decision at the UI layer with the audit log still looking clean —
   it is the single highest-risk affordance in this pattern and it must not exist.
3. **The span is mandatory.** Each suggestion cites the text it is about. This is what makes a
   teacher's review a review rather than a rubber stamp, and it is what makes the `primeiro filtro`
   framing defensible: the teacher is reading evidence, not a verdict.

**Licence boundary.** `Artemis` MIT, `lrsql` Apache-2.0, `canvas-lms-mcp` MIT. ⚠️ **`Athena` is MIT
at *metadata* grade** — 12 of 14 manifests declare it, **no licence file exists** (tree enumerated,
691 paths). Write the grade into the SOW and request a payload from TUM; do not brief it as
payload-verified. 🔴 **Do not substitute `ECNU-ICALK/EduChat` for the essay-assessment half without
reading its three-way split** — Apache-2.0 code, **AGPL-3.0 model**, **CC-BY-NC-4.0 data**.

🔴 **Two scheduling constraints, and both are easy to get wrong.**
- **Brazil: the adequacy window does not defer the bans.** Institutions get **one year to adapt**,
  but the **prohibitions apply from publication of the parecer**. Ship the two-field schema and the
  human mark gate in the **first** increment, not the last.
- **Brazil: `educação infantil` is a hard exclusion.** AI use is **totally forbidden** at the
  early-childhood stage. Scope the deployment to the stages with progressive rules and say so in
  writing; a platform-wide rollout crosses a prohibition.
- ⚠️ **The parecer is NOT homologated** in any source found as of `2026-10-18`. Under **art. 2 of
  Lei nº 9.131/1995 it has no normative force until the homologating act is published** — so this
  pattern is **build-ahead**, and the binding text differs from the September one. Re-read on
  publication. Secondary-source, two outlets; `T61` blocks the primary.

🔴 **The honest gap.** This base shelves `dodona-edu/dolos` (MIT) for **source-code** similarity and
has **no permissive text-similarity or AI-text-detection component** on any shelf. An integrity
claim about *essays* cannot be assembled from these rows — say so in the proposal rather than
implying the integrity layer transfers from `P10`.

**Why it sells.** It is the only pattern here aimed at the workload a secondary teacher actually
carries — marking prose — and it is aimed at it in the **one form a regulator that just considered
banning it has said yes to**. 🟢 And the argument that moved MEC is the argument that sells it:
*"impedia um recurso que facilita a rotina docente sem substituir o professor"* — a resource that
eases the teaching routine without replacing the teacher.

## P38 — The agentic layer over Moodle a client can install rather than commission *(new in pass 285)*

**The engagement.** A university, ministry or public-sector training body already runs **Moodle**
— the default LMS of public education worldwide — and wants an AI tutor, AI-assisted content
preparation and an MCP surface over it, under procurement rules that require **data residency**
and, in the EU, **transparency about AI-generated content**.

**Why this pattern exists.** Every prior Moodle recipe in this file wires a **third-party** MCP
server to Moodle across a companion `local_` plugin. Pass 285 found a **vendor-shipped suite that
already is that layer**, in-tree and payload-verified, which changes the proposal from *build* to
*install, configure and extend*.

| what | component | licence | role |
|---|---|---|---|
| LMS of record | [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | The system the client already runs |
| Tutor in the course | `blocks/elediaai_tutor` | **GPL-3.0-or-later** | Chat in course and dashboard |
| Chat engine | `local/elediaai_chatengine` | **GPL-3.0-or-later** | Threads, streaming, shared UI |
| Core | `local/elediaai_core` | **GPL-3.0-or-later** | Feature registry, **quota**, **audit** |
| Content → knowledge base | `local/elediaai_sources` | **GPL-3.0-or-later** | **17 extractor subplugins** (assign, book, data, feedback, folder, glossary, h5pactivity, imscp, label, lesson, page, …) |
| 🟢 Data residency | `local/literag` | **GPL-3.0-or-later** | **Local RAG over Moodle's own full-text search — no external service** |
| 🟢 AI Act Art. 50(2) | `local/aitransparency` | **GPL-3.0-or-later** | **Marking of AI-generated content** |
| 🟢 Agent surface | `webservice/elediamcp` | **GPL-3.0-or-later** | **MCP connector: Moodle tools for AI assistants** |

All seven ship from one repository:
[`eledia/moodle-elediaai-suite-free`](https://github.com/eledia/moodle-elediaai-suite-free)
(880 files, root `LICENSE` = full GPL-3.0 text, 35 149 B; each plugin carries its own
*"either version 3"* grant — all payload-read `2026-10-18`).

**How to wire it.** Install in the suite's own documented dependency order —
`local_elediaai_core` → `local_elediaai_chatengine` → `webservice_elediamcp` →
`block_elediaai_tutor` — then add `local_elediaai_sources` for the knowledge base, `local_literag`
where no external inference endpoint is permitted, and `local_aitransparency` wherever the AI Act
marking duty applies. The client's own agent talks to `webservice_elediamcp` over MCP; **the
studio's differentiating work sits in that agent, on the far side of the MCP boundary.**

**The licence boundary — and the reason this is sellable.** GPL-3.0-or-later with **no network
clause**: hosting a modified Moodle triggers nothing, while a **distributed** Moodle image carrying
these plugins ships as GPL-3.0-or-later. 🔵 **That is the licence the engagement already had** —
Moodle itself is GPL-3.0 — **so adopting the suite does not change the deliverable's licence
position at all.** Proprietary studio code stays in the agent across the MCP boundary, exactly as
in `P23`.

⚠️ **Two cautions.** The GitHub repository is a **mirror of eLeDia's GitLab**, so upstream patches
go through their issue tracker, not pull requests; and it is the **free** subset of a commercial
suite, so scope which components are in the SOW (`T20`, failure mode 3). 🔴 **EMEA-placed (DE)** —
the deployment evidence is German-speaking higher education, and nothing here establishes
references in other regions.

## P39 — The WhatsApp teacher assistant for an East African ministry, on a stack that is already MIT *(new in pass 286)*

**The engagement.** A ministry, examinations council, teacher-training college or education NGO in
**Tanzania or the wider East African Community** wants AI support for **teachers** — lesson
preparation, curriculum-aligned question generation, marking help — under three constraints that
rule out every pattern above it in this file: teachers reach the internet **on a phone, through
WhatsApp**, the language of instruction is **Swahili as well as English**, and the curriculum
authority is **TIE**, not a European or North American framework.

**Why this pattern exists.** Every prior pattern in this file assumes a browser, an LMS of record
and a Western curriculum body. Pass 286 found a repository that already makes the opposite
assumptions, **MIT-licensed and production-shaped**, which turns this from a build into an
extension. 🔴 It also retires this base's own 17-pass claim that no such thing existed.

| what | component | licence (payload-read `2026-10-18`) | role |
|---|---|---|---|
| 🟢 Teacher-facing agent | [`Tanzania-AI-Community/twiga`](https://github.com/Tanzania-AI-Community/twiga) | 🟢 **MIT** — `development/LICENSE`, 1 073 B | WhatsApp assistant for Tanzanian teachers. **230 files**: `app/` (101) with `clients/whatsapp_client.py` and `clients/agent_client.py`, `database/` with 12 migrations, **30 tests**, 15 docs, `monitoring/`, `docker/`, CI |
| 🟢 Curriculum knowledge | TIE curriculum + textbooks, via `twiga`'s own RAG path | — | Already wired in-tree; the retrieval corpus is the ministry's own material |
| 🟢 National results channel | [`vincent-laizer/NECTA-API`](https://github.com/vincent-laizer/NECTA-API) | 🟢 **MIT** — root `LICENSE`, 1 092 B | **NECTA** examination results. The cohort-outcome signal the agent otherwise has no access to |
| 🟡 Learner model, if the scope reaches analytics | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **MIT** | Knowledge tracing over whatever interaction log the deployment accumulates |
| 🟡 Offline-capable tutoring, if the scope reaches pupils | [`nguyenbaophuc27129-web/VIETPOET`](https://github.com/nguyenbaophuc27129-web/VIETPOET) as a **design reference only** | 🔴 **no grant — do not import** | Its Socratic-prompting + compressed-model-on-CPU design is the right answer to intermittent connectivity. **Reimplement; do not vendor** |

**How to wire it.** `twiga` is already the spine: WhatsApp Business API → `whatsapp_client` →
`agent_client` → retrieval over the TIE corpus, with its own quota and persistence behind it. The
studio's work is (1) **operate it** — the repo ships `docker/`, `migrations/` and `monitoring/`, so
the deployment is a configuration and SRE exercise, not a rewrite; (2) **widen the corpus** to the
syllabus years and subjects in scope; (3) **join `NECTA-API` results to cohorts** so the ministry
gets outcome reporting the agent can be measured against; (4) **add Swahili evaluation** — the one
thing no component supplies, and the thing a local engagement is uniquely able to staff.

**The licence boundary.** 🟢 **MIT throughout** — `twiga` and `NECTA-API` both. Studio
modifications may stay proprietary, the deliverable carries no copyleft obligation, and nothing here
needs a network boundary to keep it clean. 🔵 **This is the only African-deployment pattern in this
file with that property**, and it is why the sub-region matters: the 🇬🇭/🇳🇬 prior art is
**unlicensed** (ask first — `P32`, `P35`) and 🇰🇪 `shule-ai` is **CC BY-NC-ND**, which forbids both
billing and modification.

⚠️ **Four cautions.** `twiga`'s default ref is **`development`**, not `main` — pin a commit, and
expect the branch to move under you. `NECTA-API` is **unofficial and self-described as in
development**, so treat the results channel as a scraper with an SLA of zero and cache
aggressively. Star counts are **frozen at `2026-10-17`** base-wide (`api.github.com/repos` is
refused by session policy), so **adoption is unmeasured here** — assess it from commit and issue
activity directly before committing a client. And the copyright holder of `twiga`'s MIT grant is an
**individual** (*Victor Oldensand*, 2024) while the repository sits under a **community
organisation** — fine for MIT, but confirm the contribution history if the client's procurement
asks who owns the upstream. 🔴 **APAC-placed components, APAC-placed evidence:** `sekolahyuk-app`
and `rapkumer` are 🇮🇩; nothing in this pattern establishes East African references for them.

## P40 — The TWO-CORPUS tutor: a pilot that proves it and a deliverable that can actually ship *(new in pass 287)*

**The engagement.** Any paid tutoring deliverable, in any region. The client wants a pilot that
demonstrates quality fast, then a product. 🔴 **The trap this pattern exists for is that the
fastest pilot corpus is usually one the product may not use**, and the discovery is normally made
after the pilot has set expectations.

**Why this pattern exists.** `p287` read
[`avps82/mentar`](https://github.com/avps82/mentar)'s own `docs/CONTENT_LICENSES.md` — an
unusually rigorous audit by a working project, not a vendor claim — and it states the boundary
in its own verdict column: its live grounding source, **Khan Academy (ZIM) under
`CC BY-NC-SA`**, is ✅ *"cleared for the **non-commercial** local pilot"* and 🔴 ***"does NOT
clear the Phase-3 paid hosted tier."*** 🟢 **A Globant deliverable is paid by construction**, so
for this base that is the default case, not an edge case. See [`intel/trends.md`](../intel/trends.md)
`T-p287a`.

| what | component | licence (payload-read `2026-10-18`) | role |
|---|---|---|---|
| 🟡 Reference agent to read before building | [`avps82/mentar`](https://github.com/avps82/mentar) | 🟡 **AGPL-3.0** — root `LICENSE`, 34 523 B, HEAD `9d9d43c` | **839 files.** Local-first multi-curriculum tutor, deterministic answer checker, `CLA.md`. 🔴 **AGPL: import only behind a network boundary, or read it and reimplement** |
| 🟢 **Pilot corpus** (tier 1) | Khan Academy ZIM, Vikidia, Simple English Wikipedia | 🔴 KA **`CC BY-NC-SA`** · 🟢 Vikidia **`CC BY-SA 3.0`** · 🟢 Simple-WP **`CC BY-SA 4.0`** | Grounding passages for RAG. 🟢 **Vikidia and Simple-WP carry NO NC clause — they survive into tier 2; KA does not** |
| 🟢 **Shippable corpus** (tier 2) | the NC-free subset only, plus any openly licensed national curriculum | 🟢 **ACARA (AU) is `CC BY`** — alignment claimable | The corpus the paid deliverable is actually built on |
| 🟢 Offline reader | `libzim` / `python-libzim` | 🔴 **GPL-3.0-or-later** | ZIM access. 🔴 **See the boundary note — this single dependency decided `mentar`'s whole licence** |
| 🟢 Deterministic maths | `sympy` (BSD), `pint` (BSD), `num2words` (**LGPL**) | 🟢 permissive / weak copyleft | Route arithmetic through a CAS instead of the model — `mentar` and 🇬🇭 `edubot-africa` arrived at this independently |
| 🟡 Learner model | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | Knowledge tracing over accumulated interaction logs |
| 🟡 Smallest readable tutor loop | [`bunnywaffle/Open-Education`](https://github.com/bunnywaffle/Open-Education) | 🟢 **Apache-2.0**, 11 357 B | 🔴 **3 files** (`app.py` is the whole thing). Read it in ten minutes as the minimum viable answer-a-learner loop; **not a dependency** |

**How to wire it.**

1. 🟢 **Declare the two corpora on day one, in the SOW.** Tier 1 (pilot, local, non-commercial)
   may use NC content. Tier 2 (the paid deliverable) may use **only** the NC-free subset. Write
   the tier boundary into the retrieval configuration, not into a document — one corpus
   directory per tier, selected by environment, so the shippable build **cannot** read the NC
   corpus even by mistake.
2. 🟢 **Keep `libzim` an OPTIONAL extra with lazy imports.** This is `mentar`'s own dated
   self-correction and the single most portable lesson in its audit: while `libzim`
   (GPL-3.0-or-later) was a **core** dependency, *"a permissive licence for the combined
   distribution was NOT viable"*; moving it to an optional `[grounding]` extra — imports lazy,
   grounding degrading to `""` without it — returned the core to *"every dependency permissive
   or weak copyleft"*. 🔵 **One dependency's placement decided the licence of the whole
   deliverable**, which is the cheapest high-stakes decision in the build.
3. 🟢 **Route every computable answer through a CAS**, not the model. `sympy` for algebra,
   `pint` for units. Both BSD.
4. 🟢 **Decide the alignment claim from the curriculum's licence, never from the market plan.**
   Openly licensed curriculum (🇦🇺 ACARA, `CC BY`) → claim alignment and cite it. Anything else →
   ship generic packs and **withhold the claim**. 🔴 This base has **not** read the licences for
   NCERT, FBISE, NaCCA, TIE, NCTB or NCDC — see the caution below.
5. 🟡 **Attribution is a build task, not a licence task.** `mentar`'s audit notes that **no
   attribution UI exists for any source today** — grounding passages reach the system prompt and
   never a learner-visible credit string, while `CC BY`/`BY-SA` require credit. 🟢 **Build the
   attribution surface in tier 1**, where it is cheap, rather than discovering it in tier 2.

**The licence boundary.** 🔴 **`mentar` is AGPL-3.0: do not vendor it into a proprietary
deliverable.** Two clean uses: (a) **read it** — the audits are the deliverable here, and reading
is unrestricted; (b) **run it behind a network boundary** as a separate service, with the
client's proprietary code on the other side. 🟢 **The corpus components are the real boundary in
this pattern**, and they are CC, not code: `BY-SA` obliges **attribution and share-alike on
adaptations**; `BY-NC-SA` adds **NC**, and 🔴 **`SA` COMPOUNDS it** — a redistributed adaptation
of NC content inherits `CC BY-NC-SA`, carrying NC forward into everything downstream. Vikidia and
Simple-WP are `BY-SA` **without** NC, which is exactly why they survive into the paid tier and
Khan Academy does not.

⚠️ **Five cautions.** 🔴 **`mentar`'s audit is not counsel** — its own front matter says *"⚠️ Not
legal advice"*, its identifications are *"as of 2026-06-14"*, and the repository was **private**
when it was written (*"no one has yet received the code under AGPL"*), so its AGPL framing
describes an intent, not a distribution history. 🔴 **The KA ZIM's CC version is unspecified on
the ZIM itself** — the audit treats it as 3.0/4.0-equivalent *"pending exact confirmation"*;
confirm before relying on either. 🔴 **This base has read exactly ONE national curriculum licence
first-hand (ACARA, via this audit)** — the other six markets it names are unverified, so step 4
is a research task on every new engagement, not a lookup. 🟡 **Star counts are frozen base-wide**
(`api.github.com/repos` refused by session policy), so judge `mentar`'s 839-file maturity from
its commit and issue activity directly. 🔴 **And do not import 🇵🇰 `PrepifyAI`'s textbook JSON as
a shortcut to a corpus** — it redistributes FBISE and Punjab board textbooks with no grant of any
kind, and that is the one failure in this pattern that a licence-intake ask **cannot** repair
(`T-p287c`).
