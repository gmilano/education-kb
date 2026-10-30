---
industry: education
region: Global
updated: 2026-10-30
---

## 🆕 `p550` — `2026-10-30` — **two recipes: the accreditation substrate this base has never had a permissive platform for, and the prerequisite graph the knowledge-tracing stack has always been missing**

🔵 **Supporting measurements: [`../agents/top.md`](../agents/top.md#-p550--2026-10-30)
(velocity, `Gap 550-A`), [`../verticals/solutions.md`](../verticals/solutions.md#-p550--2026-10-30)
(`ilios`), [`../intel/trends.md`](../intel/trends.md) (`Trend 55`, `Trend 56`).**

### 🟢 `P7` — Accreditation-grade curriculum intelligence on a permissive platform (North America, 10–14 weeks)

🔴 **The problem this solves, stated as a buyer states it.** An accredited professional
programme must demonstrate, to a regulator, that every required competency is taught,
assessed and resourced across a multi-year curriculum — and must produce that evidence on
demand. 🟢 This is a **reporting and ontology** problem before it is an AI problem, and the
AI is only trustworthy if it sits on a real curriculum model.

**The stack, named concretely:**

| Layer | Artefact | Grant | Why this one |
|---|---|---|---|
| Curriculum system of record | [`ilios/ilios`](https://github.com/ilios/ilios) | 🟢 **MIT** | 🟢 **The only permissively granted institutional platform on this base.** Longitudinal curriculum, competency mapping, **instructional hours**, role transitions, documented API (`docs/ilios_api.md`), **560 releases**, maintained since 2012 |
| Delivery, where it already exists | Moodle / Canvas, left in place | GPL-3.0 / AGPL-3.0 | 🔵 Ilios's own README positions itself as the **backbone under** these, so the LMS is **not** migrated — which is what makes the engagement sellable |
| LMS bridge | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) **308★** · MIT, or [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) **104★** | MIT (the latter **by manifest**, shelf rule 16) | Reads live course/assessment state so the report reflects what was *delivered*, not what was *planned* |
| Competency → labour-market codes | [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | MIT | 🔴 **Optional and EMEA-specific** — ESCO is an EU taxonomy. For a US accreditor the competency framework is the accreditor's own; 🔴 **the adapter is studio work either way** (upstream is 1.4 years dead) |
| Agent layer | **Build it.** Ilios API + an agent that answers *"show every competency with no assessment in year 3"* | — | 🔴 **No AI exists in Ilios and none is implied.** This is the studio's deliverable |
| Evaluation | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) **605★** · Apache-2.0 | Apache-2.0 | 🔵 Its **eval rubrics**, not its skills — the only published yardstick in this sector for *"is this output pedagogically acceptable"* |

🟢 **Wiring.** Ilios stays the system of record; the MCP bridge supplies delivered state;
the agent is **read-only against both** and emits an accreditation narrative with every
claim linked to an Ilios competency ID and a Canvas assessment. 🔴 **The agent must not
write to the curriculum** — a regulator-facing record with an LLM write path is
unauditable, and `Trend 1`'s governance gap is the thing being sold against.

🟢 **Why `ilios` makes this pattern possible and no other platform does.** Every
alternative is copyleft (`Trend 56`): forking Moodle or Open edX to add a curriculum
ontology obliges the client to publish the fork. 🟢 **MIT means the extension is the
client's.** 🔴 **Scope limit, stated:** Ilios is built for the **health professions**; the
model generalises to any accredited professional programme and is **not** a K-12 system.

🔴 **What is unproven here.** No AI integration with Ilios has been built or tested by
this base. The grant, the releases, the API documentation and the liveness are
first-hand; **the pattern is an architecture, not a validated deployment**, and should be
costed with a 2-week discovery against a real Ilios instance.

### 🟢 `P8` — A declared prerequisite graph over a statistical mastery estimator (any region, 6–8 weeks)

🔴 **The gap this closes, and it is a real one in this base's own shelf.** The
knowledge-tracing stack here — [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) **291★**,
[`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) **453★**,
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) **274★**, all MIT — **infers mastery
over a skill set that someone else must declare.** 🔴 None of them ships the
**prerequisite relation**: *what must be known before this*.

| Layer | Artefact | Grant | Role |
|---|---|---|---|
| Prerequisite graph | [`miuuyy/Clew`](https://github.com/miuuyy/Clew) **212★** | 🟢 MIT | Topic/prerequisite graph: what a topic **requires** and what it **unlocks**; exports the graph and shares read-only learning context **over MCP** |
| Mastery estimator | [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | MIT | Bayesian Knowledge Tracing, C++ core — per-skill mastery probability from response streams |
| Model justification | [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | MIT | Benchmarks BKT against deep KT on standard datasets — 🔵 **what you show the client to defend the estimator choice** |
| Reference tutor integration | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT | BKT already in front of learners (ReactJS/Firebase) — the integration to copy |
| Retention | [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) **539★** | MIT | Spaced repetition over the mastered set; the learner keeps the deck |
| Activity record | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | Writes activity **back** to an xAPI LRS so tutoring is auditable. 🔴 **426 days dead** — read as architecture, own the adapter |

🟢 **Wiring.** Clew's graph supplies the **skill DAG**; `pyBKT` estimates mastery per node
from learner responses; the next node is the **unmastered node whose prerequisites are
all mastered** — a graph query, not a prompt. `pykt-toolkit` justifies the estimator;
`anki-mcp-server` schedules retention; `learnmcp-xapi` records it to the LRS. 🔵 **The
LLM's job shrinks to explanation and question generation** — the sequencing decision is
deterministic and inspectable, which is the property `Swon010191/Math_teacher` earned its
shelf row for.

🔴 **The blocker, stated before anyone costs it: `Gap 550-B`.** Clew's **desktop app
requires a ChatGPT Plus or Pro plan** (`Trend 55`). 🟢 **The code is MIT and the graph
model is the asset.** 🔴 **The dependency is not deployable into a school.** So this
pattern takes **Clew's graph schema and its MCP export contract** and reimplements the
host against a self-hostable path — the same **Ollama/local-first** posture
`Math_teacher` demonstrates. 🔵 **Budget it as "adopt the data model, rebuild the
runtime"**, roughly 3 of the 6–8 weeks, and say so in the proposal rather than
discovering it in week 4.

🟢 **Why this is worth building at all:** `Trend 3` says *pedagogy is becoming measurable
and almost nobody is measuring it*. A declared prerequisite DAG plus a calibrated mastery
estimator is **measurable pedagogy** — every sequencing decision has a reason that
survives a parent, a teacher and an auditor asking why.

### 🔴 What `p550` did NOT do on this page

- 🔴 **Neither pattern was built or run.** Both are architectures over artefacts whose
  grants, releases and liveness were verified first-hand this pass; neither has been
  deployed by this base.
- 🔴 **No week count is evidence-backed.** `10–14` and `6–8` are estimates, labelled as
  estimates, and the one decomposed claim (3 weeks to replace Clew's runtime) is the only
  figure with a stated reason.
- 🔴 **`frappe/flow_client` remains archived** (`2026-10-22`, AGPL-3.0), so the Frappe
  agent layer is still build-it-yourself over the REST API — unchanged this pass.

> 🟢 **`p546` adds `P596` and `P597`, taking the page to **51** recipes (`P547`…`P597`,
> contiguous).** 🔴 **The derivation could not be run:**
> [`../ingest/derive-counts.py`](../ingest/derive-counts.py) was **denied by name**
> (`Code from External`) for the thirteenth pass in fourteen, so **51** is this pass's own
> inline count of the `^## …P<n>` headings and the gate did **not** attest it. 🔵 Stated
> rather than implied, because the previous three count defects on this base were all
> prose figures that nobody could check.
>
> 🟢 **Both new recipes come from one measured finding and neither invents a component:**
> for four of five interoperability standards on this base the **maintained**
> implementation is not the one the standards body publishes
> ([`../repos/trending.md`](../repos/trending.md#-p546--2026-10-30)), and the interop
> standard is the **only** anchor class that survives a change of region
> ([`../intel/trends.md`](../intel/trends.md)). `P596` is the stack that follows from
> that. `P597` is the gate that stops a studio shipping the dead half of it.

> 🟢 **`p548` adds `P601` and closes `Gap 547-H`.** 🔴 **The derivation could not be run
> again:** every script in `ingest/` was **denied by name** (`Code from External`) for the
> **sixteenth** pass in seventeen, so the figures below are inline counts and the gate did
> **not** attest them.
>
> 🟢 **`Gap 547-H` is CLOSED, and `547-H` was right where `p548`'s first measurement was
> wrong.** The later `P565` — *"The disconnected classroom, served end to end"* — is now
> **`P600`**, the next free id, so this page is **contiguous `P547`…`P601`** *and* its ids
> are **unique**. 🔵 Three inbound references that unambiguously meant the disconnected
> classroom were repointed on [`../repos/foundations.md`](../repos/foundations.md),
> [`../intel/market.md`](../intel/market.md) and [`../intel/trends.md`](../intel/trends.md);
> 🔴 two in [`../agents/trending.md`](../agents/trending.md) were **left alone** — one is
> correctly about Brightspace, the other is ambiguous (keyed to Krayin, which appears
> nowhere on this page) — because that page is append-only and this base does not rewrite
> history to tidy a reference.
>
> 🔴 **A correction `p548` owes against itself.** Its first count of this page reported
> **six** duplicate ids (`P551`×4, `P558`, `P565`, `P590`, `P592`, `P593`) and briefly
> treated `547-H` as a sixfold understatement. 🔴 **The cause was a greedy regex:**
> `^## .*P[0-9]+` matches the **last** id in a heading, so any heading whose title cites
> another recipe was filed under the id it cited. 🟢 With the correct rule — **the first
> `P<n>` token in the heading**, and `^## ` headings with no leading id being pass sections
> rather than recipes — the page had 54 headings, 53 distinct ids and **exactly one**
> duplicate, reproducing `547-H` precisely. 🟢 The rule now ships in
> [`../evidence/pattern-id-uniqueness.2026-10-30-p548.tsv`](../evidence/pattern-id-uniqueness.2026-10-30-p548.tsv)
> so the next pass can disagree with it instead of recounting from scratch.
>
> 🟢 **`P601` comes from a retraction, not a discovery:** `openSIS-Classic` was filed ⛔
> *no grant* for nineteen passes and is **GPL-2.0**, read from the payload. The largest
> open-source SIS this base can name is buildable, and no recipe used it.


> 🟢 **`p547` adds `P598` and `P599`.** 🔴 **The derivation could not be run again:**
> [`../ingest/derive-counts.py`](../ingest/derive-counts.py) was **denied by name**
> (`Code from External`) for the fourteenth pass in fifteen — this pass's denial covered
> **every** script in `ingest/`, so the figures below are inline counts and the gate did
> **not** attest them.
>
> 🔴 **And counting it honestly found a defect four passes of "contiguous" prose had
> missed: this page has 54 `^## …P<n>` headings but only 53 DISTINCT ids.**
> 🔴 **`P565` is used twice** — *"Brightspace, the third LMS (North America first)"* at one
> place and *"The disconnected classroom, served end to end (LATAM rural, Africa)"* at
> another. 🔵 **So every cross-reference to `P565` on this base is ambiguous**, and the
> range `P547`…`P599` is contiguous while the ids are **not unique** — two different
> claims that `p546`'s *"51 recipes (`P547`…`P597`, contiguous)"* collapsed into one.
> Registered as **`Gap 547-H`**: renumber the later `P565` and fix inbound references.
> 🔵 This is the fourth time on this base that a derived count stated in prose was wrong
> in a way nobody could see (`Gap 544-E`, `Gap 546-B`, `Gap 547-F`), and the fix is the
> same one `546-B` got — [`../ingest/address-count.py`](../ingest/address-count.py) now
> reports `table_data_rows` per page, and an id-uniqueness check belongs beside it.
>
> 🟢 **`P598` is the first recipe on this page derived from a convergence rather than from a
> single artefact:** five independently-built education agents across three regions, citing
> none of each other, each put a **deterministic or human gate between the model and the
> artefact that reaches a student**
> ([`../agents/trending.md`](../agents/trending.md#-p547--2026-10-30)). That is also the
> mitigation the high-risk regimes this base holds actually ask for, so the recipe is a
> compliance argument and an architecture at the same time. 🔴 **`P599` is the negative
> recipe the pass could not avoid writing:** how to tell, before a client engagement
> commits, that an attractive artefact is unusable — and the two tests that catch what a
> licence check does not.

> 🟢 **`p549` adds `P602` and `P603`, taking the page to **57** recipes
> (`P547`…`P603`, contiguous).** 🔴 **The derivation could not be run:**
> [`../ingest/derive-counts.py`](../ingest/derive-counts.py) and every other script in
> `ingest/` were **denied by name** (`Code from External`) for the **seventeenth** pass in
> eighteen, so **57** is this pass's own inline count of the `^## …P<n>` headings and the
> gate did **not** attest it. 🟢 **What the gate could not stop was *reading* the scripts**,
> and that is where this pass's retraction came from
> ([`../repos/foundations.md`](../repos/foundations.md)).
>
> 🔵 **A false-duplicate warning for the next pass, measured so it is not re-discovered.**
> **60** `##` headings on this page carry a `P<n>` id while only **57** ids are distinct, and
> that is **not** `Gap 547-H` recurring: every id has exactly **one** defining heading, and
> the surplus is **cross-references inside other recipes' titles** (`P551` is named in five:
> `P556`, `P564`, `P568`, `P572`, `P597`) plus **pass-announcement headings** that list the
> ids they added (`p542`→`P589`/`P590`, `p543`→`P591`/`P592`, `p544`→`P593`). 🟢 **Counting
> headings finds duplicates that are not there; counting *definitions* does not.**
>
> 🟢 **Both new recipes come from measured findings and neither invents a component.**
> `P602` exists because the one new platform this pass found
> ([`PKulal/LMS`](https://github.com/PKulal/LMS), Apache-2.0, REUSE-compliant at file level)
> ships **deliberately no AI** — every AI feature is behind a paid edition or on a roadmap —
> so the AI layer is the studio's to own on a permissive base, which is the cleanest
> starting position this page has ever been able to offer. `P603` is the gate that would
> have found that platform earlier: it is the three-channel grant probe that
> `Gap 549-C` (`UNINDEXED-NOT-ABSENT`) and `Trend 51` require.

## 🆕 P602 — The Apache-2.0 multi-tenant LMS with the AI layer the vendor withheld (APAC-origin, portable; 6–9 weeks to a defensible pilot)

🔵 **Where this comes from.** One measurement, taken this pass:
[`PKulal/LMS`](https://github.com/PKulal/LMS) is a **multi-tenant LMS under Apache-2.0** whose
`README.md` splits the product into a free **Community** edition (this repository) and a paid
**Enterprise** edition — and **every AI feature sits on the paid side or on the roadmap**:

| Feature | Edition in the vendor's own table |
|---|---|
| Coding questions with **AI test cases**, **AI starter code**, AI-generated SQL practice schema | 💎 **Enterprise (paid)** |
| Chapter-scoped **AI tutor chat**, **AI feedback drafts for trainers**, plagiarism/similarity check | 🔵 *"Proposed (edition not yet decided)"* |
| **`SCORM / xAPI import`** | 🔵 *"Proposed"* — 🔴 **not shipped** |
| Assessments and certificates, SSO, audit logs, Super Admin console | 💎 **Enterprise (paid)** |

🟢 **So the open base is a clean LMS with a hole exactly where the differentiating work is**,
and the hole is permissively licensed. 🔴 **The same table is the warning:** assessment is
Enterprise-only, so this is a platform to build **on**, never a product to deliver.

### The recipe

1. 🟢 **Take the platform at a commit, not a tag.** `git clone --depth 1` →
   `HEAD 2abdade` (`2026-10-08`). 🔴 **`git ls-remote --tags` returns nothing**: no release
   has ever been cut, so there is no version to pin and no published upgrade path. Fork,
   pin the SHA, and own the rebase.
2. 🟢 **Run `reuse lint` in CI on day one — it will pass, and that is the point.**
   The repository already ships `REUSE.toml`, `.reuse/`, `LICENSES/` and `NOTICE` to **REUSE
   spec 3.3**, with **762 of 854** tracked files carrying in-header SPDX identifiers. 🟡 Two scoped
   exceptions are enumerated by path and must survive the fork: **BSD-3-Clause** on unmodified
   Flutter template icons, and **`LicenseRef-PaceWisdom-Trademark`** on **7 logo paths** —
   which, citing **Apache §6**, requires a modified redistribution to **replace those logos**.
   🔵 **Step one of any white-label is therefore a logo swap, and it is a licence obligation,
   not a design task.**
3. 🟢 **Mount the tutor as a separate service, not as a platform fork.** Put
   [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**, **51 247★**,
   `v1.7.0`, lifelong learner memory) behind the platform's DRF API and key its memory on the
   platform's `organizations` + `accounts` tenant ids. 🔵 Grant-compatible: Apache-2.0 both
   sides, so there is nothing to reconcile.
4. 🟢 **Build the course material into teachable units with**
   [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) (**Apache-2.0**,
   **464★**): it distils video, PDF, transcripts and notes into **source-backed** teacher
   skills. 🔵 It is the right component here because the platform's course builder already
   holds video and documents — so the input exists and the output is traceable to it, which
   is what an institution will ask about first.
5. 🟢 **Add retention with** [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server)
   (**MIT**, **539★**) as an MCP server. 🔵 The platform ships `gamification` and progress
   tracking but **no spaced repetition**; this is the missing half of the learning loop and
   the learner keeps the deck.
6. 🟢 **Own the record layer, because the platform does not.** `SCORM / xAPI import` is
   *Proposed*, so emit xAPI yourself with
   [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (**MIT**) into an
   LRS. 🔴 **Read that component as an architecture, not a dependency** — `p546` dated it at
   **426 days** without a commit. 🟢 **This is the step that makes the pilot defensible:** it
   is what turns tutoring from ephemeral chat into an auditable learner record, which is the
   `87 %`-adoption / `26 %`-governance gap on
   [`../intel/market.md`](../intel/market.md) answered in code.
7. 🟢 **Gate the AI with `P598`'s two decisions and**
   [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)
   (**Apache-2.0**, **605★**) **eval rubrics**. 🔵 Rubrics, not prompts, are what a
   procurement conversation can actually inspect.
8. 🔴 **Close the assessment hole explicitly, in writing, before the pilot.** Assessments and
   certificates are Enterprise-only. Either buy that edition, or build assessment as the
   studio's own module against the open `curriculum` app — and **say which**, in the
   statement of work. 🔵 Silence here is how an open-core pilot becomes a licence dispute.

### Why the regions line up

🟢 **APAC** is the natural first engagement: the platform is India-origin on in-repo evidence
(**DPDP** named in its roadmap, holder an Indian `Pvt. Ltd.`), so data-residency language is
already in the vendor's own vocabulary, and **Australia's TEQSA** per-provider action plans
make the audit trail of step 6 a procurement trigger rather than a nicety. 🟢 **LATAM** is the
second: the governance gap is measured (`Trend 53`) and multi-tenancy is how one ministry or
one university group serves many institutions from one installation. 🟡 **EMEA** needs the
Annex III conformity work layered on top — and has **more runway than the 2026 date implied**
(see the deadline move on [`../intel/market.md`](../intel/market.md)). 🔴 **North America** is
the hardest fit despite being the most regulated: NY `A 9190`'s grade-9 age gate and the
four-state mandate for district policy both have to be enforced in the platform, and
**nothing in this stack enforces them today.**

### 🔴 What this recipe does not give you

🔴 **No dependency-grant clearance.** Per `Gap 528-C` this base has no instrument that
enumerates dependency grants, and this stack ships `poetry.lock`,
`frontend/package-lock.json` and a Flutter `pubspec.lock`. 🟢 The repository-level grants are
Apache-2.0 / MIT throughout, and the engagement's own licence scan remains the control —
**but it is unusually cheap here**, because REUSE metadata already exists (step 2).

## 🆕 P603 — The three-channel grant probe: the gate that stops a shortlist from missing what search cannot see

🔵 **Where this comes from.** `Gap 549-C` and `Trend 51`, both measured this pass: the
best-granted artefact on this base is **absent from the GitHub search index** while three
other channels serve it. 🔴 **Every census on this base since `p529` asks an index what
exists**, and this is the error class no absence-check catches.

### The recipe — four probes, in cost order, and what each one may and may not conclude

1. 🟢 **Screen** — MCP `search_repositories` with `repo:` qualifiers **OR-ed in one call**
   (shelf rule 17). Returns existence, SPDX screen, **exact** star and fork counters,
   `pushed_at`, `archived`, default branch. 🔴 **May conclude: "indexed, and here are its
   counters."** 🔴 **May NOT conclude: "does not exist."** A null here is
   `UNINDEXED-NOT-ABSENT` until probe 2 or 3 says otherwise. 🔴 And per shelf rules 8–9, the
   SPDX field **screens; it never grades** — `NOASSERTION` has resolved to permissive,
   copyleft, non-OSI *and* no grant on this base.
2. 🟢 **Grade** — `raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`, reading the
   **licence file's own title block**, its **byte count** and its **`sha256`**. 🔴 Probe the
   **subtree**, not only the root: `Gap 548-A` (`ENUMERATED-NOT-READ`) was earned by 19
   passes of ⛔ on `openSIS-Classic`, whose GPL-2.0 sat at `docs/License.txt` the whole time.
   🔵 And check the **manifest** before recording an absence (shelf rule 16): `DESCRIPTION`,
   `package.json`, `pyproject.toml`, `Cargo.toml`.
3. 🟢 **Exist and date** — `git ls-remote <url> HEAD` and `git ls-remote --tags --refs`.
   🟢 **This is the probe that refutes probe 1's null**, and it is also a **release
   instrument** (shelf rule 19): the publisher's own tags, with **zero tags** a finding in
   its own right. 🔵 It needs no API token and no HTML page.
4. 🟢 **Census** — `git clone --depth 1` into an **empty directory**, then count
   `SPDX-License-Identifier` headers against tracked files and read `REUSE.toml` /
   `LICENSES/` if present. 🟢 **This is the only probe that distinguishes a repository-level
   grant from a file-level one**, and it is what graded `PKulal/LMS` at **762 / 854**. 🔴 It
   is also the only probe with a disk cost, so it runs **last and only on candidates that
   passed 2**.

### The gate, stated as a rule a later pass can enforce

🟢 **A verdict cell records the probes that were run**, in the form
`UNREAD(curl-403, mcp-untried)` or `UNMEASURABLE(mcp-unindexed, curl-403)` — `Gap 549-A`.
🔴 **An absence claim requires probes 1 **and** 3 to agree**; probe 1 alone may never produce
one. 🟢 **A grant claim cites a path, a byte count and a hash** — never a sidebar, never a
search field, never a secondary source. 🔵 **And every recorded blocker is re-probed on the
pass that depends on it**, which is `Trend 52`: the refutation that lifted two passes of
self-imposed ceiling cost exactly **one call**.

## 🆕 P598 — The gated teacher agent: deterministic core, human approval, official-source binding (all regions; the compliance argument comes free)

🔵 **Where this comes from.** Not from one repository — from **five**, built independently
in three regions, none citing another:

| Artefact | Region | Grant | The gate, in its own words |
|---|---|---|---|
| [`Swon010191/Math_teacher`](https://github.com/Swon010191/Math_teacher) | APAC (Vietnam) | 🟢 **MIT** | *"giáo viên duyệt trước khi lên bảng"*; equations solved exactly and **verified by substitution** |
| [`ceanjonnube-negra/docente-ia`](https://github.com/ceanjonnube-negra/docente-ia) | LATAM (Mexico) | 🔴 ungranted | *"el Tool Registry determinista … **nunca pasa por Claude**"*; sources restricted to **`.gob.mx`** |
| [`MaiQuangPhuoc/edu_agents`](https://github.com/MaiQuangPhuoc/edu_agents) | APAC (Vietnam) | 🔴 ungranted | **deterministic pipeline over ReAct**; LLM **bounded to the textbook** |
| [`jrsaguas/DocenteAgent`](https://github.com/jrsaguas/DocenteAgent) | 🟡 unplaced | 🔴 ungranted | *"Acciones externas sensibles requieren autorización humana **inicialmente**"* |
| `Ignacio-Ghub/asistente-docente-sin-conexion` | LATAM | 🔴 ungranted | local model; *"la IA solo propone borradores que el docente revisa y decide"* |

🔴 **Four of the five are unusable as code** (see
[`../intel/measured-unusable.md`](../intel/measured-unusable.md)). 🟢 **The convergence is
the asset, and it is not encumbered.**

### The recipe

1. 🟢 **Start from the one artefact you may actually build on.**
   [`Swon010191/Math_teacher`](https://github.com/Swon010191/Math_teacher) (**MIT**, grant
   read first-hand at `HEAD` `18bee0983b3b`, 42 commits). Take its two load-bearing
   decisions, not its UI: a **deterministic solver** that the LLM never answers for, and a
   **teacher-approval step** between suggestion and display.
2. 🟢 **Put the subject logic in a library, never in the model.** `Math_teacher` uses a
   symbolic solver and **checks its own answer by substitution**. 🔵 This is the single
   cheapest accuracy win in education AI: the class of error parents and inspectors
   actually escalate is **confidently wrong arithmetic**, and a symbolic core cannot
   produce it.
3. 🟢 **Bind retrieval to an authoritative domain, as `docente-ia` does.** Restrict the
   agent's sources to the ministry's own host — `.gob.mx` in Mexico — so every curriculum
   or calendar answer is attributable to the body that will be asked about it. 🔵 Where a
   permissive machine-readable curriculum exists, prefer it to scraping:
   `oaknational/oak-open-curriculum-ecosystem` (**MIT**, MCP server over England's national
   curriculum), `bncc-dev/bncc-dados` (**MIT** code / **CC BY 4.0** data, Brazil),
   `esco-skill-extractor` (**MIT**, EU ESCO) for outcome→skill mapping.
4. 🟢 **Make the human gate a hard boundary, not a setting.** 🔴 `DocenteAgent` states its
   gate holds *"inicialmente"* — **a provisional gate is not a control.** Implement it as
   the only write path to anything a student sees, and log the approving identity.
5. 🟢 **Keep it local-first.** `Math_teacher` runs with Ollama and **no API key required**.
   🔵 This is what moves a pilot from demonstrable to deployable wherever pupil data cannot
   leave the institution.
6. 🟢 **Record the activity to a standards-compliant store**, so tutoring is auditable
   rather than ephemeral: `DavidLMS/learnmcp-xapi` (**MIT**) is the architecture — 🔴 read
   it as a design, not a dependency (last commit `2025-08-29`), and prefer the maintained
   xAPI successors named on [`../repos/trending.md`](../repos/trending.md).
7. 🟢 **Wire the staleness gate `P597` and the provenance gate `P595` in front of all of
   it** — and under `Gap 547-C`, evaluate recency on the last **human** commit.

### 🟢 Why the compliance argument comes free

🔵 Steps 2, 4 and 5 are not best practice bolted on — they are **the mitigations the
regimes this base already holds ask for**: **EU AI Act Annex III point 3** (grading,
admission, proctoring) with Art. 50 transparency from `2026-08-02` and stand-alone
high-risk duties from `2027-12-02` (**Regulation (EU) 2026/1744**); **Vietnam's Decision
33/2026/QD-TTg**, which places education AI on its high-risk list; **Korea's AI Basic Act**
(in force `2026-01-22`); **TEQSA**'s institutional action plans in Australia. 🟢 **Five
teacher-built projects with no compliance budget converged on this independently**, which
is the most persuasive thing a studio can put in front of a ministry buyer.

🔴 **What this pattern does not give you.** None of the five implements assessment
*validity* — they gate what reaches a learner, not whether the pedagogy is sound
(`Trend 3`). 🔴 And `DocenteAgent`'s roadmap carries `biometría después`: **biometric
attendance is the one extension that would move an engagement from high-risk toward the
AI Act's prohibited tier** if it drifted into emotion inference. Do not inherit it.

## 🆕 P599 — The disqualification sweep: two tests that catch what a licence check cannot (all regions, run before scoping)

🔵 **Run this before an artefact enters a proposal.** `p547` measured six newly-found
systems and **five were unusable** — but only three of the five would fail a conventional
licence check ([`../intel/trends.md`](../intel/trends.md)).

### Test 1 — `declared` and `served` are two columns, never one (`Gap 547-A`)

```
# the grant the author ASSERTS
curl -s raw.githubusercontent.com/$SLUG/$REF/.claude-plugin/plugin.json | grep -i '"license"'
curl -s raw.githubusercontent.com/$SLUG/$REF/package.json              | grep -i '"license"'
curl -s raw.githubusercontent.com/$SLUG/$REF/README.md                 | grep -iE 'licen|lizenz|licencia'

# the grant the repository SERVES -- the whole tree, not the root
git clone --filter=blob:none --no-checkout -q https://github.com/$SLUG t   && git -C t ls-tree -r --name-only HEAD | grep -iE 'licen|lizenz|copying|notice'
```

🔴 **`declared ∧ ¬served` is its own verdict and it is the dangerous one.**
`lehrer-tools/lehrer-agent` declares MIT **twice** and serves nothing at any of 103 paths,
under holder `{"name": "anonym"}` — 🔵 so MIT's notice clause **cannot be satisfied even in
principle**, and a buyer reading the manifest concludes the opposite.
🟡 **And `¬declared ∧ ¬served` is not "permissive by default"** — it is all rights
reserved. Three of `p547`'s six were in that state.

### Test 2 — ask what the tooling does to third-party content (`Gap 547-B`)

🔵 **A clean licence does not make an artefact lawful to use.** Grep the tree's own
description of its adapters:

```
git -C t ls-tree -r --name-only HEAD | grep -iE '^bin/|extract|scrape|decrypt'
curl -s raw.githubusercontent.com/$SLUG/$REF/README.md   | grep -iEn 'decrypt|entschl|AES|DRM|licence key|offline (book|library)'
```

🔴 **`lehrer-agent` returns `AES-256-CTR` (BiBox/Westermann) and `AES-128-CBC`
(Cornelsen).** Decrypting an effective technological measure engages **UrhG § 95a** and
**InfoSoc 2001/29/EC Art. 6**, and no research or education exception reaches a commercial
engagement. 🟢 **Its `bin/klett` path decrypts nothing** — so the correct output of this
test is **not "reject the repository"** but *"one of three adapters is reusable; the other
two define a publisher negotiation"* (see
[`../verticals/solutions.md`](../verticals/solutions.md)).

### Test 3 — is a human writing this? (`Gap 547-C`)

```
git -C t log --format='%an' | sort | uniq -c | sort -rn
```

🔴 **All commits by `github-actions[bot]` means the freshness signal is void.**
`MarinaVeauvy/ia-educacion` showed 64 commits and a commit from the previous day, and is
**eleven near-duplicate keyword-slug articles** with no `README`. 🟢 Treat a wholly
bot-authored history as **`UNDATED`, not `FRESH`**, or a recency ranking will prefer it to
the one artefact worth promoting.

🔵 **Cost of the whole sweep: three commands and no API access** — which matters, because
`api.github.com` and `github.com` both return **403** under this session's policy
(`Gap 547-E`), while `raw.` and the git protocol do not.

## 🆕 P596 — The portable tutoring stack: anchor on the standard, load the curriculum as data (all regions)

**The problem it solves.** 73 % of the agents on this base's shelf are anchored to
**nothing** and the anchored minority is mostly anchored to **one country** — BNCC, the
National Curriculum for England, GDPT. 🔴 **An asset built on a curriculum anchor cannot
be resold into another region**, which for a global studio is the whole economics. 🟢
**This recipe inverts it:** the architecture anchors on **xAPI + LTI 1.3 + QTI**, and the
curriculum becomes a **data set loaded into** that architecture rather than structure
compiled into it.

**Components — every one dated at `p546`, and every date is why it is here rather than its
obvious alternative.**

| Layer | Component | Licence | Last commit | Why this one |
|---|---|---|---|---|
| **Learning record store** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Apache-2.0 | 🟢 **3 d** | 🔴 **not** [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (**1.4 y**) — the reference implementation is the dead one |
| **Record pipeline** | [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | Apache-2.0 | 🟢 **72 d** | moves statements between stores; what makes the record layer portable instead of captive |
| **LMS attachment** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) *(Node)* | Apache-2.0 | 🟢 **16 d** | 🔴 **not** [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (**3.9 y**) — LTI 1.3 is alive in Node and PHP and **dead in Python**, which is the binding an AI stack reaches for first |
| **LMS attachment** *(PHP estates)* | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 | 🟢 **13 d** | Moodle and Chamilo estates are PHP; same standard, live binding |
| **Assessment interchange** | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | Apache-2.0 | 🟢 **20 d** | 🔴 **not** [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (**1.4 y**) |
| **SCORM legacy** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | MIT | 🟢 **1 d** | the only live SCORM runtime here; needed for existing content estates |
| **Mastery estimator** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 🟢 **1 d** | Bayesian Knowledge Tracing as **one MCP server**, not an application |
| **Agent record bridge** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | MIT | 🔴 **426 d** | 🔴 **READ, DO NOT TAKE.** The only artefact that writes agent activity *back* to an LRS — and it has not moved in 1.2 years. **Port the ~32-commit pattern onto `lrsql` directly** |
| **Curriculum as data** | [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) | MIT | 🟢 **8 d** | the reference shape for the whole recipe: a *national* curriculum served through an **API + MCP server**, so the country is a data set |
| **Skills mapping** | [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | MIT | 🔴 **505 d** | 🔴 **READ, DO NOT TAKE.** ESCO itself is a maintained EU taxonomy; this binding is 1.4 y dead. Re-implement against the ESCO API |

**Wiring, in order.**

1. **Stand up the record layer first, not the agent.** `lrsql` behind `xapipe`. Every
   tutoring interaction becomes an xAPI statement from day one; this is what makes the
   engagement auditable under EMEA's Article 50 duties *and* saleable in North America.
2. **Attach to the LMS through `ltijs`** (or the PHP library for Moodle/Chamilo estates).
   🔵 The LMS stays the system of record for enrolment and grades — `p529`'s finding that
   *the unit of LMS integration is the institution, not the product* still governs.
3. **Mount `tutor-mcp` as the mastery estimator.** It speaks MCP, so any assistant can
   use it, and it ships real BKT rather than a prompt that claims to track mastery.
4. **Load the curriculum through an Oak-shaped adapter.** One adapter per country — Oak
   for England, a BNCC adapter for Brazil (see `P555`) — all emitting the same internal
   competency model. 🟢 **This is the step that makes the stack portable:** a new region
   is a new adapter, not a new product.
5. **Emit assessment as QTI 3** via `LongsightGroup/qti3`, so items survive a change of
   platform; keep `scorm-again` only where a legacy content estate requires it.
6. **Port, do not depend on, the two dead bindings.** `learnmcp-xapi`'s agent→LRS write
   pattern and `esco-skill-extractor`'s ESCO mapping are both small and both abandoned;
   re-implement each against the live layer underneath it.

🔴 **What this recipe does not give you.** No agent in it is *itself* standards-anchored —
the anchoring is the studio's work, which is precisely why it is billable. 🔴 And the
portability claim has a limit worth stating to a client: a standard can be profiled
per-jurisdiction, so "xAPI" in two countries is not automatically the same xAPI. 🟡 **Test
it with `xapipe` between two deployments before promising portability.**

**Effort.** 8–10 weeks for the record + LTI + mastery spine; **+2–3 weeks per additional
country adapter** thereafter, which is the number to quote.

## 🆕 P597 — The staleness gate: refuse a dependency by its commit date (run inside `P551`, after `P568`)

**Why it exists.** `p545` reported every address on this base's shelves as **`LIVE`** and
`p546` dated them: **28 of 175 foundations addresses have had no commit in over a year,
six in over six years, and the stalest is 11.9 years old.** 🔴 **Two of `p545`'s own four
new shelf promotions were over a year dead when they were promoted**, because the
promotion instrument takes stars, forks and grants and **does not take a date**. 🔵 **A
liveness check that only resolves the address cannot catch this. This gate is four lines
of git.**

**The instrument.** 🟢 Already written and published at
[`../scratchpad/p546/staleness.sh`](../scratchpad/p546/staleness.sh):

```bash
# one network op per dependency, no file contents fetched, no working tree kept
git clone --bare --depth 1 --filter=blob:none "https://github.com/$slug" "$d"
git --git-dir="$d" symbolic-ref --short HEAD     # the branch, RESOLVED not guessed
git --git-dir="$d" log -1 --format=%cI           # the date
rm -rf "$d"
```

🟢 **Cost, measured:** **273 addresses in 96 seconds, zero failures**, and **304 KB** of
transfer for a repository whose full shallow clone is **219 MB** — a **720×** saving on
[`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS), both
reporting the same commit date.

**The thresholds, and the three exceptions that stop it being a blunt instrument.**

| Verdict | Rule |
|---|---|
| 🟢 **PASS** | last commit ≤ 90 days |
| 🟡 **REVIEW** | 91–365 days — usable, name a maintenance owner in the proposal |
| 🔴 **FAIL** | > 365 days — do not take as a dependency; port the pattern instead |

- 🟡 **Exception 1 — ratified specifications.** [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec)
  at 1.3 y is *finished*, not abandoned. **Apply the rule to implementations, never to
  specs.**
- 🟡 **Exception 2 — teaching material.** A tutorial repository is not a dependency, though
  [`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial) at
  **8.7 y** is still *wrong*, not merely old.
- 🔴 **Exception 3 — release-branch projects, and this one has teeth.** A six-month default
  branch can be a project that commits on release branches, so **check every head before
  failing it**. 🟢 `p546` did exactly that for
  [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms): **377 heads,
  every one last committed `2026-04-30`**, including branches named for later releases. 🔵
  The exception was tested and did not rescue it.

**Wiring into `P551`.** Run this **after** the grant gates (`P556` grant-union, `P568`
split-grant) and **before** architecture is written, because its output changes component
choice rather than licence posture. 🟢 Its output is one row per dependency —
`slug · branch · head_sha · committed_iso · age_days` — which is the same shape as
[`../evidence/staleness-foundations.2026-10-30-p546.tsv`](../evidence/staleness-foundations.2026-10-30-p546.tsv)
and drops straight into a proposal appendix.

🔴 **The gate's honest limit:** a commit date measures *activity*, not *health*. A
well-factored library finished two years ago may be a better dependency than a churning
one, and this gate will fail the first and pass the second. 🔵 **So `FAIL` means
"justify in writing", not "forbidden"** — and the justification belongs in the proposal
where a client can see it.

# Compose Patterns — Education

**Pass `p546` · 2026-10-30.** 🟢 **recipes: **51**** — `P547`…`P597`, contiguous,
🔴 **counted inline this pass, NOT gate-attested:**
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) was denied by name
(`Code from External`) for the thirteenth pass in fourteen. The derivation below is the
one that *would* have run, and it still fails if this sentence and the headings disagree —
but nothing re-checked it this pass. 🔵 Previously `49` —
counted from the headings by
[`../ingest/derive-counts.py`](../ingest/derive-counts.py), which fails if this sentence
and the headings disagree.

🔴 **`p544`'s header said "Thirty-eight", and that was wrong by eleven.** This page held
**47** recipes (`P547`…`P593`) when that sentence was written. 🔵 **This is the third
instance of one defect class, found a third way:** `p543` caught it in `agents/top.md`'s
shelf heading, `p545` caught it in `repos/foundations.md` (*"seventy-two"* against a
derived **156**), and now here. 🟢 **A count written in prose beside the rows it counts
goes stale the moment a pass adds a row and forgets the sentence — so this one is no
longer written, it is derived, and a gate fails if the sentence and the headings
disagree.** Every component named below
was read from its repository page, and **every licence was read from the licence
file's own title block** over `raw.githubusercontent.com`. 🟢 **The parenthesis
this header carried — "`github.com` returns HTTP 403" — is corrected at `p534`:
the HTML is 403 to `curl` and **200 through WebFetch**, which is how every
component below now also carries an **archive-state** read.** 🔴 **That read
immediately invalidated a component this file would have recommended** — see
`P570`. No recipe uses a component this base has not verified.

**The licence rule that shapes all eight:** the mainstream LMS cores are copyleft
(Moodle GPL-3.0, Open edX / Canvas AGPL-3.0). Agents stay **permissive and
out-of-process**, talking over MCP, LTI 1.3, REST or xAPI. Where a recipe forks,
it forks a permissive core.

---

## 🆕 P594 — the device-statute classroom tutor, built inside Brazil's `Lei 15.100/2025` exception (LATAM)

**Brief.** A Brazilian state or municipal network must comply with **Lei nº 15.100 of
13 January 2025**, which bans personal devices in *educação básica* during class, break
and intervals — **excepting strictly pedagogical, teacher-mediated use.** The network does
not want phones out of the classroom; it wants them usable **only** inside that exception.
🟢 **The compliance artefact is therefore not a policy document — it is the teacher-opened
session**, and that is what this recipe builds.

| Role | Component | Licence, read as bytes |
|---|---|---|
| Reference architecture for the session model | 🆕 [maiatechdev/avit](https://github.com/maiatechdev/avit) | **MIT** — sidebar; 5 430 B README |
| LMS of record (not forked) | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 — integrate over REST/LTI 1.3 |
| Activity record, so the exception is auditable | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** · `LICENSE` @`main` |
| Learning Record Store | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** |
| Policy gate + audit trail on every tool call | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | **MIT** · `LICENSE` @`main` |
| BNCC competency anchoring for the lesson objective | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | **MIT** · `LICENSE` @`main` |

**Wiring.** The teacher opens a session against a **BNCC competency code** — `agente-bncc-professores`
turns the code into the objective and the item bank, so the session's pedagogical purpose is
*recorded before any device unlocks*. The session issues a code/QR; a learner's device is in
scope **only** while that session is open, which is the statute's "teacher-mediated" limb
made mechanical rather than promised. The tutor follows `avit`'s ladder — hints that
withhold the answer, then a worked explanation after three unsuccessful attempts, then a
similar exercise. Every turn is written as **xAPI** through `learnmcp-xapi` into Ralph, so
the network can later demonstrate *which* minutes were pedagogical. The
**agent-governance-toolkit** sits between the tutor and every tool call, giving the audit
record and the policy gate the statute's mental-health-strategy duty will eventually be
inspected against. 🔵 **The teacher dashboard shows class aggregates only; the learner sees
their own session** — `avit`'s own split, and the one that keeps this out of the
student-profiling conversation.

**🔴 Hard constraints, stated as build rules and not as caveats.**
1. 🔴 **`avit` is a prototype and its own README says so** — *"protótipo de demonstração.
   Não há uso com dados reais de alunos até que a análise jurídica seja concluída."*
   **Read it for the session model; do not take it as a dependency.** `0★ · 0 forks`.
2. 🔴 **Moodle is GPL-3.0.** The tutor stays out-of-process across REST/LTI 1.3. Nothing in
   this recipe forks an LMS core.
3. 🔴 **Lei 15.100/2025 is a *device* statute, not an *AI* statute.** It says nothing about
   models, automated assessment or profiling, and **Brazil's `PL 2338/2023` is still
   pending in the Câmara.** 🔵 **Build as though the AI rules are coming**, because this
   recipe's audit trail is cheap now and retrofitting one is not.
4. 🟡 **Scope: *educação básica*.** Higher education is outside the statute and this
   recipe's compliance argument does not transfer to it.

**Effort.** 6–8 weeks to a one-network pilot, assuming Moodle is already running.

---

## 🆕 P595 — the dependency-provenance gate a studio ships in week one (all regions)

**Brief.** Every engagement in this sector inherits open-source components whose licence
decides the architecture — and **the comparison articles the client has already read are
wrong about them.** `p545` measured a widely-cited 2026 LMS comparison calling
[`frappe/lms`](https://github.com/frappe/lms) *"MIT"* when its `license.txt` is **33 893 B
of AGPL-3.0**. 🟢 **This recipe is the gate that makes that discoverable on day one instead
of at legal review.** It is this base's own instrument, generalised for client delivery.

| Stage | How | Why this exact shape |
|---|---|---|
| 1. Resolve the default branch | `git ls-remote --symref <url> HEAD` | 🔴 **`p545` swept 162 shelf repos: only `94` default to `main` — `42 %` do not**, and eight serve values no candidate list would hold (`v4.0.x-develop`, `java11`, `2.12`, `19.0`). **Never enumerate branch candidates.** |
| 2. Walk a filename ladder | `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `LICENCE` (British), `LICENSE-CODE` + `LICENSE-TEXT` (split grants), each in case variants | 🔴 A single-filename probe misreads a fork as ungranted — [`oaknational/oak-open-curriculum-ecosystem`](https://github.com/oaknational/oak-open-curriculum-ecosystem) ships **`LICENCE`**, and `frappe/*` ships lowercase **`license.txt`** |
| 3. Read the **title block**, not the sidebar | first lines of the payload over `raw.githubusercontent.com` | 🔴 Sidebars round, mislabel and sometimes say nothing; the title block is the grant |
| 4. Record **bytes + `sha256`** | `wc -c` and `sha256sum` on the payload | 🟢 Content-addressed, so a **relicensing** is detectable later without re-reading prose. `frappe/frappe` **MIT 1 118 B `b03bbdca4e0a`** vs `frappe/lms` **AGPL-3.0 33 893 B `db1a87ba81e8`** |
| 5. Flag **stub grants** | any licence file under ~100 B | 🔴 [`frappe/education`](https://github.com/frappe/education)'s entire `license.txt` is **19 B** — `License: GNU GPL V3`. **A family name is not a grant**: no text, no holder, no permission language, nothing for counsel to review |
| 6. Flag **alias pairs** | identical HEAD sha across two addresses | 🟡 `p545` found [`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) ≡ [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET) at `4f96365d3108`. **Two addresses, one system** — a dependency list that counts both overstates the surface |
| 7. Check the grant **per app, not per vendor** | run 1–6 on every repo in the family | 🔴 **Frappe is the worked example:** framework **MIT**, LMS **AGPL-3.0**, ERP **GPL-3.0**, school admin **GPL-3.0 declared-only**. *"Frappe is MIT"* is true of one of four |

**🔴 What this gate cannot see, stated so it is not oversold.**
- 🔴 **Transitive grants.** The licence you ship is the **union of the grants you link** —
  this base already recorded an MIT repo landing in the network-copyleft band because it
  links AGPL-3.0 **PyMuPDF**. A repo-level probe is blind to it; you still need a
  dependency scan.
- 🔴 **Per-subtree grants.** [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp)
  is **MIT at root** and **GPL-3.0 under `legacy_reference/`**. A root-only read is wrong
  about it.
- 🔴 **Staleness.** `ls-remote` returns a HEAD sha and **no date**. Liveness is not
  currency, and this gate measures only the first.

**Effort.** 1–2 days to build, then it runs in CI. 🟢 **`p545` ran stages 1 and 6 over 162
addresses and got `162/162 LIVE`, zero dead** — the gate is cheap and the sweep finishes in
minutes.

---

## P547 — Canvas-attached teacher copilot (North America)

**Brief.** A district or university on Canvas wants lesson prep, feedback drafting
and routine answers, without touching grades and without forking an AGPL core.

| Role | Component | Licence |
|---|---|---|
| LMS (not forked) | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 · 6.9k★ |
| Integration seam | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ · v1.16.0 |
| Lesson authoring, source-backed | 🆕 [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** · 462★ |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Acceptability gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

**Wiring.** `canvas-mcp` runs as a separate process and is the *only* thing that
touches Canvas — this is what keeps AGPL-3.0 §13 away from your code. The copilot
calls it for roster, assignment and submission context. 🆕 **`lineage-skill` is the
authoring stage**: feed it the course's own videos, PDFs, transcripts and notes and
it emits lessons that **trace back to that source material** — so a teacher
challenged on "where did this come from" has an answer, and Educhain fills in
items underneath it. Output is emitted as **H5P** so it survives a future platform
migration; every interaction is written to Ralph as xAPI. The k12 rubrics run in CI
against a fixed set of teacher prompts, and a regression there fails the build.

**Hard constraint — build it in, not in the policy doc.** Oklahoma (S.B. 1734) bars
AI as the main basis for high-stakes decisions and requires a written district
policy before 2027-28; Maryland's districts have 120 days from MSDE guidance; Idaho
(S.B. 1227) adds data-privacy duties; Utah (H.B. 218) mandates AI literacy in grade
7/8. The grading path must be **structurally** human-decided: the agent may draft,
a human must commit, and the xAPI record must name who committed. "We have a
policy" is not the deliverable; "the model cannot do it" is.

**Effort.** 6-8 weeks. Weeks 1-2 MCP deployment and auth; 3-5 authoring +
H5P emission; 6 rubric CI; 7-8 audit trail and district pilot.

---

## P548 — EU AI Act conformity scaffolding for an education product (EMEA)

**Brief.** A European edtech vendor, university or ministry needs its grading /
admissions / proctoring AI ready, with the obligations that are already live
satisfied now.

| Role | Component | Licence |
|---|---|---|
| Permissive LMS core (forkable) | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · 449★ |
| Governance-provenance alternative | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 · 505★ |
| xAPI record store (the audit substrate) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |
| Integrity, explainable | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** · 355★ |
| Pedagogy evidence | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |

**Wiring.** Fork OpenOLAT (Apache-2.0 — proprietary extensions are fine). Ralph is
not analytics here, it is the **conformity artefact**: logging and traceability are
Annex IV obligations, and an xAPI store gives them in a standard shape rather than
a bespoke table nobody can audit. Dolos handles integrity *without* an LLM, because
a finding presented at an appeal must be explainable. The pedagogy benchmark
produces the accuracy-and-performance evidence the technical documentation needs.

🆕 **Sequence against the real dates — and establish which clock the client is on
before anything else.** Regulation (EU) 2026/1744 (Digital Omnibus, OJ 24 Jul 2026,
in force 27 Jul 2026):

1. **Now** — **Article 50 transparency has applied since 2 Aug 2026** and was *not*
   delayed: disclose AI interaction at every touchpoint. Confirm no
   emotion-recognition anywhere in the product (**banned in schools since Feb 2025**).
2. 🆕 **By 2 Dec 2026 (~5 weeks out)** — two new Article 5 prohibitions added by the
   Omnibus phase in. Check the product against them now, not in 2027.
3. **Now → 2027** — risk management, data governance, logging via Ralph,
   human-oversight design, technical documentation. 🆕 National **regulatory
   sandboxes** must exist by 2 Aug 2027: a sandbox slot is a de-risking vehicle,
   as in P550.
4. **By 2 Dec 2027** — conformity assessment for stand-alone Annex III high-risk
   functions (grading, admissions triage, programme assignment, proctoring, access
   to qualifications). 🆕 **2 Aug 2028** if the AI is a safety component of a
   regulated product (Annex I).
5. 🆕 **By 2 Aug 2030 — if, and only if, the client is a public authority** with the
   system *already in service*. State schools and public universities qualify
   across most of the EU.

🆕 **The two-clock rule is the commercial core of this pattern.** A private vendor
has ~25 months; a public institution running an existing system may have ~45. Ask
first, scope second — and never let a public client be told they have 13 months.

**Note.** Regulation (EU) 2026/1744 was cross-checked across multiple secondary
sources across two passes, **not read from the Official Journal**. The 2 Dec 2027,
2 Aug 2028 and Article 50 dates are corroborated by several sources; **the 2 Aug
2030 public-authority date rests on one**. Read the regulation before any of this
reaches a client deliverable, and that date before it reaches a public one.

**Effort.** 10-12 weeks for the scaffolding; the audit-and-remediate slice for the
already-live obligations (Article 50, emotion recognition, the 2 Dec 2026
prohibitions) is **2-3 weeks, needs no new technology, and sells on its own.**

---

## P549 — Multi-agent classroom on the APAC cores (Global, APAC-sourced)

**Brief.** Fastest credible tutoring prototype available. Use it for a pilot in any
region — the supply is APAC-academic, the deployment need not be.

| Role | Component | Licence |
|---|---|---|
| Lifelong tutor + learner memory | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 49.0k★ · v1.7.0 (2026-10-28) |
| Multi-agent classroom roles | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 41.8k★ · v1.3.0 (2026-10-29) |
| Mastery estimation, published | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** · 274★ |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) + [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** · 538★ / **MIT** · 4.1k★ |
| Records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

**Wiring.** DeepTutor owns the long-lived learner model (three-layer memory,
learning paths, mastery gates). OpenMAIC supplies the classroom *cast* — lecturer,
peer, assistant — when the pedagogy calls for social learning rather than 1:1.
**Replace any prompt-claimed mastery with OATutor's Bayesian Knowledge Tracing**:
it is the one published estimator on these shelves, and "the model says the student
has mastered it" is not a measurement. Mastered items are pushed into the learner's
**own** Anki deck via the MCP server, scheduled by FSRS — so the learning survives
the end of the engagement. Everything lands in Ralph as xAPI.

**Why both large repos.** DeepTutor is depth-over-time for one learner; OpenMAIC is
breadth-of-role in one session. They solve different halves and neither subsumes
the other.

**Regional adjustments.**
- **India / China** — AI-content labelling is mandatory (India from **20 Feb 2026**).
  Attach provenance metadata at authoring time, in the H5P package, not afterwards.
  🆕 Use `lineage-skill` (Apache-2.0) for the authoring leg: source-backed output
  means the labelling obligation is met structurally.
- 🆕 **Vietnam** — the risk-based AI law gives **education an 18-month transition**
  for systems already in service: the softest APAC landing for a product already
  running elsewhere, and the right first port.
- **ANZ** — public opinion leans toward *banning* AI in schools. Lead with Dolos
  integrity and the audit trail; demo the controls before the tutor.

**Effort.** 4-6 weeks to a defensible pilot; 2 weeks for a demo on DeepTutor alone.

---

## P550 — Teacher-first lesson preparation in PT/ES (LATAM)

**Brief.** The LATAM market has already moved to the teacher as buyer (Teachy's
position, and the 2026 EdTech 100 shows upskilling losing ground). Build for the
teacher, in Portuguese and Spanish, and integrate with the incumbent rather than
replacing it.

| Role | Component | Licence |
|---|---|---|
| Incumbent school management (integrate only) | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 · 722★ |
| Accessible LMS, thin IT | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 · 1.0k★ |
| Offline-first delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** · 1.2k★ |
| Authoring, source-backed | 🆕 [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** · 462★ |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** · 387★ |
| Single-teacher reference shape | 🆕 [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | **MIT** · 63★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Rubric gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** · 601★ |

**Wiring.** i-educar is **GPL-2.0 and must stay across a service boundary** — read
enrolment, attendance and performance signals over its API/DB into your own
permissive service; never link it. `lineage-skill` and Educhain generate plans and
items; H5P makes the output portable into Chamilo, Moodle or Kolibri. **Kolibri is
the connectivity answer**: a cloud-only tutor is undeployable in the municipalities
that run i-educar, so generate centrally and *ship* content packages offline.

🆕 **Read Claw-ED before designing the teacher UX.** It is MIT, 63★, local-first,
works from the teacher's own curriculum files, and is explicit that it is
**single-teacher-per-instance, not multi-tenant**, with student-facing features
labelled experimental. That boundary is exactly the gap a studio fills — and the
repo is an honest map of where the hard part starts.

**De-risking vehicle.** Run the pilot inside **Brazil's ANPD AI regulatory sandbox
(open through December 2026)**. That produces a compliance narrative that survives
**PL 2338/2023** becoming law. 🆕 **Peru** also has sandboxes and a phased rollout,
so the same play works there; **Colombia** has CONPES 4144 (Feb 2025) as the policy
hook; **Mexico's** risk-based bill is still only in the Senate, so there is no
compliance anchor to sell against there yet.

**Greenfield read.** CENIA finds **13 of 19 LAC countries studied** have not yet
introduced early AI adoption in schools — national AI-literacy programmes with no
incumbent to displace. Google.org's **$4.6M across nine countries, 1.25M students
by 2028** is the co-funding context.

**Effort.** 6-8 weeks. Add 2-3 weeks for i-educar integration per municipal variant.

---

## P551 — Licence due-diligence gate (run this first, every engagement)

**Brief.** Before any of the above. Education repositories mis-grade more often
than any other vertical this base has measured, and the failures are expensive
rather than cosmetic.

| Role | Component |
|---|---|
| Known-bad controls, mislabelled | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) 2.1k★ (bespoke non-commercial, grant at `LICENSE.md`), [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) 340★ (Elastic-2.0), [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) 5.1k★ (CC-BY-**NC**-4.0) |
| 🆕 Known-bad control, **self-contradicting** | [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) 91★ — sidebar `GPL-3.0`, **README badge `License: MIT`**, licence file `GNU GENERAL PUBLIC LICENSE Version 3` |
| Known-bad filename control | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) — 107.5k★, grant at `LICENSE.txt`, **no licence type named on the page**; read this pass as **Apache-2.0** |
| 🆕 Known-bad **ungranted** controls | [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) **64★** (no licence file; README says only *"open source and available for educational purposes"*), [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) 25★ (sidebar "License" link **anchors into the README**), [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) (search result claimed MIT; no licence file) |
| 🆕 Known-bad **per-app** control | [frappe/lms](https://github.com/frappe/lms) **AGPL-3.0** vs [frappe/education](https://github.com/frappe/education) **GPL-3.0** — same vendor, same framework, two regimes |
| Known-good controls | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (Apache-2.0), [learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT), [sakaiproject/sakai](https://github.com/sakaiproject/sakai) (ECL-2.0) |

**The seven rules, each earned from a real failure.**
1. **Grade from the title block, never a body sentence.** PageLM's licence *opens*
   with *"Permission is hereby granted, free of charge…"* and then prohibits
   redistribution outright and requires a **revenue-share agreement before any
   commercial deployment**. A body-matching probe calls that MIT.
2. **Try `LICENSE`, `LICENSE.txt`, `LICENSE.md` and `license.txt`.** One filename
   misfiles a **107.5k★** asset as ungranted; Frappe's grant is at `license.txt`,
   PageLM's at `LICENSE.md`. Try `main`, `master` *and* `develop`.
3. **Never drop a `NonCommercial` qualifier** when naming a family.
4. **Case-insensitive matching, or none.** A GPL-2.0 payload that happens to
   mention *"GNU Lesser General Public License"* in its preamble cross-reference
   will grade as LGPL under a case-sensitive matcher —
   [oat-sa/tao-core](https://github.com/oat-sa/tao-core) (GPL-2.0, 64★) is the live
   example.
5. 🆕 **When the README badge and the sidebar disagree, the licence file decides.**
   A badge is a claim; a licence file is the grant. (`lumen`.)
6. 🆕 **Record "no licence file" as a verdict, not a blank.** An absent grant is a
   *harder* blocker than a bad one — there is no counterparty to negotiate an
   exception with. Stars do not imply a grant: 64★ bought none.
7. 🆕 **Grade per app, not per vendor** (`frappe/*`), and **never** accept a search
   result or a blog roundup as the licence channel — three of the controls above
   were mis-described by one.

🆕 **Channel note, and it is reusable.** With `github.com` and `api.github.com`
returning HTTP 403 through the session proxy, **`raw.githubusercontent.com` is
still reachable** — so the gate should fetch the licence *file* directly rather
than scrape a sidebar badge. That is both the cheaper channel and the more
authoritative one, and it is what rules 1, 5 and 6 require. A ~20-line shell loop
over `{branch} × {filename}` printing the first four non-blank lines is the whole
implementation.

**Output.** A **four**-band verdict per repository — *permissive / copyleft-integrate
only / not usable / **ungranted*** — with the licence filename, the branch, the
title line read, and the byte size recorded. The last two bands never reach an
architecture diagram.

**Effort.** 1 week to stand up, then **seconds** per repository.

---

## P552 — Pedagogy evaluation harness (the differentiator)

**Brief.** Answer "does this actually teach?" with a number, before a client asks
and before a competitor can.

| Role | Component | Licence |
|---|---|---|
| Pedagogical knowledge benchmarks (CDPK, SEND) | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |
| Teacher-workflow eval rubrics | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** · 601★ |
| Mastery ground truth | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) (BKT) | **MIT** · 274★ |
| Longitudinal signal | [openfun/ralph](https://github.com/openfun/ralph) (xAPI) | **MIT** · 51★ |

**Wiring.** Run CDPK and SEND across the candidate models at model-selection time —
the result is a model choice you can defend in writing, which is a different
artefact from a preference. Run the k12 rubrics in CI over a fixed prompt set so a
model or prompt change that degrades teaching quality fails the build. Use OATutor
BKT as ground truth for mastery claims. Ralph supplies the longitudinal arm: did
mastery *hold* at 30 days, not just at the end of the session.

**Why this is worth its own pattern.** The pedagogy benchmark has **13 stars**
against DeepTutor's **49.0k**. Everyone is shipping tutors; almost nobody is
measuring teaching. 🆕 The **OECD 2026 Digital Education Outlook** reportedly tells
institutions to prefer **purpose-built educational AI over general-purpose tools** —
this harness is how you evidence that claim rather than assert it.

🆕 **Two regional angles the benchmark's own provenance opens up.**
- **LATAM / Spanish.** The repository credits **Chile's Agencia de la Calidad de la
  Educación and CPEIP** for the exams CDPK is built from. Running it in Spanish,
  against Chilean teacher-certification standards, answers *"does this model know
  how to teach **here**"* — and CENIA already co-chairs the ECLAC regional AI
  working group, so there is a named counterpart.
- **EMEA / SEND.** Special educational needs and disabilities is where European
  regulators and parents apply the most pressure and where essentially no vendor
  can show evidence. `SEND` is half of this benchmark and it is MIT.

**Effort.** 2-3 weeks standalone; it should be folded into every other pattern here
rather than sold alone.

---

## 🆕 P553 — The Moodle agent bridge (the build nobody has done)

> 🔴 **`p529`: superseded in scope by [`P558`](#-p558--the-moodle-bridge-generator-the-build-the-field-actually-needs).**
> The premise below — *"the entire Moodle-MCP field tops out at 27★"* — is wrong.
> The field is **222 addresses**; its ceiling is **52★ and ungranted**; its
> permissive leader is **45★ and eight months stale**. 🟢 **The conclusion
> survives and strengthens** — there is still no credible, shippable bridge — but
> *"nobody has done this"* becomes *"hundreds have each done it once, for one
> campus."* **P553 remains valid as a single-client build.** When the client is
> buying a capability rather than one integration, run **P558** instead.

**Brief.** Moodle has the sector's largest install base and plugin ecosystem and
**no credible agent bridge.** Canvas has one at 308★; the entire Moodle-MCP field
tops out at **27★**. This is the clearest build opportunity on this base, and it
is a *build*, not a fork.

| Role | Component | Licence |
|---|---|---|
| The platform (not forked) | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ |
| Nearest prior art — the lineage head | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** · **27★** |
| Secondary prior art | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) (claims ~230 tools, Moodle 4.5/5.x) | **MIT** · 2★ |
| ⛔ Do **not** start here | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | **AGPL-3.0** · 1★ |
| Reference architecture to copy | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |

⚠️ **Why the field is empty — corrected `p528`, and the correction changes the
recipe.** `p527` wrote that the field *"resolves to roughly three codebases."* It
does not. A thirteen-address census — **twelve probed first-hand this pass**, the
thirteenth a duplicate carried from `p527` — found **eleven independent codebases
plus two forks**, four languages, tool counts from **8 to ~230**, **37 stars across every
counter read**, and 🟢 **ten of the eleven under MIT.** The forks are real
(`thc1006` → `G36maid`; `triffon` → `falkenslab`, via its
`Copyright (c) 2026 Falkenslab` line) and `tosuki/moodle-mcp` is genuinely
ungranted — but they are two of thirteen, not the shape of the field. Full census:
[`../repos/foundations.md`](../repos/foundations.md).

🔵 **So this is a consolidation, not a greenfield build**, and that is cheaper and
more defensible. Four MIT pieces to take, each verified `p528`:

| Take | From | Why that one |
|---|---|---|
| Typed tool surface + tested version matrix (3.7 / 4.5 / 5.2) | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) · MIT · 27★ · Rust | The only one that names three live-tested Moodle versions |
| Two-flag write gate + `confirm=true` on destructive calls | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) · MIT · 3★ | Best-governed write model in the census (32 read / 8 write, writes off by default) |
| Course-whitelist boundary (`MOODLE_DEV_COURSE_WHITELIST`, prod writes off) | [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) · MIT · 2★ | The only one that separates dev from prod write scope |
| Zero-dependency posture (stdlib only, single file) | [Faixiang/moodle-mcp](https://github.com/Faixiang/moodle-mcp) · MIT · 2★ | Makes the institutional security review short |

🟢 **The asset worth owning is the vocabulary, not the server.** No two of the
eleven name the same operations the same way, and three contradict their own
READMEs on tool count (Faixiang 6 vs 8, leshamblin 70 vs 67, falkenslab 140 vs
~230). **Publish the tool schema as a spec and the server as its reference
implementation.** 🔴 Do not take `sonstellar969/open-moodle` as a starting point
despite its MIT grant: it links **AGPL-3.0 PyMuPDF**. See **P556**.

**Wiring.** Build the server **permissively (MIT/Apache-2.0) and out-of-process**,
speaking **Moodle Web Services** — never link Moodle's GPL-3.0 code, and never
vendor the AGPL-3.0 implementation into the deliverable. Start from
`G36maid/moodle-mcp` (MIT) for the tool surface and **copy `canvas-mcp`'s shape**
for everything else: it is the mature one, and it already answers the questions
this build will hit (auth scoping, student-vs-educator tool split, per-role skill
packaging, a security-release cadence). Two design commitments worth making up
front, both learned from the field above:

1. **Read-write, but gated.** `csmediapro` chose read-only to be safe; that is the
   right default and the wrong ceiling. Separate read tools from write tools and
   require an explicit human commit on anything that touches a grade — which is
   also what Oklahoma S.B. 1734 requires in P547.
2. **State a tool count that is true.** `falkenslab` says ~230 in the README and a
   search summary said 140; `canvas-mcp` says 102 in About and 128 in the README.
   The whole category has a credibility problem that costs nothing to avoid.

Emit **H5P** for generated content and write every interaction to **Ralph** as
xAPI, as in P547 — the bridge is only half the deliverable, the audit trail is the
other half.

**Why Globant specifically.** Moodle's plugin directory is distribution for free,
and a permissive MCP server is the one component in this sector that **every**
Moodle engagement afterwards reuses. It is the highest-leverage reusable asset on
this base, and today's bar to clear is 27 stars.

**Effort.** 8-10 weeks to a credible first release (4-5 for the tool surface on
Web Services, 2 for auth and role scoping, 2-3 for H5P/xAPI and docs). Publish it;
the field is empty.

---

## 🆕 P554 — Governance over the AI already in the building (LATAM-led, globally applicable)

**Brief.** UNESCO IESALC + UNU-IAS surveyed **200 LATAM higher-ed institutions in
19 countries: 87% already use AI, 26% have a formal AI strategy**, and adoption is
driven by **individual faculty and students, not institutional policy**. These
institutions do not need to be sold AI. They need control of the AI already
running, unmanaged, inside them. This is consulting-led with a software tail, and
it is the highest-probability LATAM opening on this base.

| Role | Component | Licence |
|---|---|---|
| Audit substrate (xAPI) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |
| Acceptability yardstick | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |
| Model-fitness evidence (ES, Chilean standards) | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |
| Integrity, explainable | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** · 355★ |
| Incumbent systems (integrate only) | [i-educar](https://github.com/portabilis/i-educar) GPL-2.0 · [chamilo](https://github.com/chamilo/chamilo-lms) GPL-3.0 · [moodle](https://github.com/moodle/moodle) GPL-3.0 | copyleft — service boundary |
| Mastery ground truth | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** · 274★ |

**Wiring — four stages, and the first two sell on their own.**

1. **Inventory (2-3 weeks).** Find the AI actually in use. Bottom-up adoption means
   it is in individual faculty's tools, not in procurement records, so this is
   interviews and traffic analysis, not a vendor list.
2. **Policy and classification (2-3 weeks).** Sort each use by whether it touches a
   high-stakes decision — grading, admissions, progression. That is the same
   classification Annex III forces in EMEA (P548) and Oklahoma forces in NA (P547),
   which is why this pattern ports.
3. **Enforcement in code (4-6 weeks).** Human-in-the-loop on every high-stakes path,
   enforced structurally rather than by policy; Dolos for integrity findings that
   survive an appeal; OATutor BKT wherever a mastery claim is being made.
4. **Audit trail (2-3 weeks).** Ralph as the xAPI store, so "is the AI helping, and
   who decided what" becomes answerable retrospectively instead of arguable.

**Why the benchmark belongs here.** CDPK is built on **Chile's own
teacher-certification exams** (Agencia de la Calidad de la Educación, CPEIP,
credited on the repo). Run in Spanish against Chilean standards, it turns stage 2
from a policy document into **evidence** — and **CENIA** co-chairs the ECLAC
regional AI working group alongside **Uruguay's AGESIC**, so there is a named
institutional counterpart rather than a cold call. UNESCO's **Observatory on AI in
Education for LAC** (launched Santiago, 14 April 2026) is the other door.

**Where it ports.** The 87/26 split is the sharpest *measured* instance of a
global pattern: 70% of higher-ed institutions in Europe and North America have
guidance "in place or in development" — the second half of that phrase is this
engagement. Lead with the UNESCO number in LATAM because it is regional and
primary; lead with the regulation in EMEA (P548) and with state statute in NA
(P547). **Same four stages, different opening sentence.**

**Caveat to carry into the pitch.** CENIA finds **13 of 19 LAC countries** have not
begun early AI adoption in schools, and adoption in urban schools concentrates in
better-resourced private institutions. **This pattern fits the 87%, not the
greenfield** — for the greenfield, run P550 with Kolibri.

**Effort.** 10-15 weeks end to end; stages 1-2 are a **4-6 week standalone
assessment** and the natural door-opener.

---

## 🆕 P555 — Portuguese-language curriculum and assessment stack (LATAM, Brazil)

**Brief.** Everything in this recipe is **Brazilian, MIT and verified**, which is
what makes it new: for seven passes this base held that LATAM contributed *data*
and not *code* to the agent legs. It does not. The recipe grounds a teacher-facing
agent in Brazil's own curriculum (**BNCC**) and marks student writing against
Brazil's own examination (**ENEM**) — no translation layer, no US rubric wearing a
Portuguese label.

| Role | Component | Licence | Verified |
|---|---|---|---|
| Essay marking, 5 ENEM competencies | [dsvi-b/corretor-enem](https://github.com/dsvi-b/corretor-enem) | **MIT** · 7★ | `p420`, re-read `p528` |
| Curriculum grounding (BNCC `EF01`–`EF04`, PCNs) | [ThallesYVasconcelos/Agente-Educacional](https://github.com/ThallesYVasconcelos/Agente-Educacional) | **MIT** · 0★ | `p528` |
| LMS seam | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) (or **P553**'s consolidation) | **MIT** · 27★ | `p528` |
| Pedagogical evaluation | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ | `p527` |
| Retention | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** · 4.1k★ | `p527` |
| Event records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ | `p527` |
| Local inference | Ollama (the EduRAG reference runs `llama3.2` / `qwen2.5` / `mistral` / `gemma2`) | — | `p528` |

**Wiring.**

1. **Take `corretor-enem` as a skill, not a service.** It is *agent-agnostic by
   design*: no API, no ML, no model weights — a methodology plus a local SQLite
   corpus of **11,147 examiner-marked essays**, which the agent reads to anchor
   its scores. 🟢 **That is why it belongs at the bottom of the stack:** the
   marking rationale is inspectable and the corpus is the citation. Methodology
   credited to **Silva & Araujo (UFPE, 2024)**; corpora to `rafaelanchieta/essay`
   and `lplnufpi/essay-br`.
2. **Copy EduRAG's grounding architecture, do not depend on it.** 0★ and a
   university course's final project — but it is the cleanest reference this base
   has for curriculum grounding: page-level citations into **MEC** documents,
   BNCC-code identification for an arbitrary activity, a **Self-RAG** check
   before answering, and **Giskard** for evaluation. Re-implement that shape on
   your own stack (LangGraph + ChromaDB + `bge-m3` embeddings is what it uses).
3. **Attach to the LMS over MCP**, never by forking Moodle (GPL-3.0).
4. **Evaluate with `pedagogy-benchmark` before and after.** It carries **CDPK**
   and **SEND**, and its ground truth comes from Chile's Agencia de la Calidad de
   la Educación and CPEIP — 🔵 **so the evaluation instrument is also LATAM**, and
   a procurement conversation can be held entirely in regional evidence.
5. **Write every marking event to Ralph (xAPI)** so the audit trail survives the
   agent.

🔴 **State the maturity honestly to the client.** The two Brazilian components
total **7 stars, 1 fork and zero releases**. They are *correct* and they are
*unproven at scale*. Price the engagement as "harden and operate verified
reference code", not "integrate a maintained dependency" — and expect to become
the de-facto maintainer of both. ⚠️ `corretor-enem`'s own page calls its output
**an estimate, not an official score**; that sentence belongs in the deliverable's
UI, not just in its README.

**Timeline.** 6–8 weeks to a marked-essay pilot in one school network. **Region:
LATAM.**

## 🆕 P556 — The grant-union gate (run inside P551)

**Brief.** `p551` reads the repository's licence file. `p528` found two ways that
is not enough, both in live education repos, and both would pass a repo-level
probe.

| Failure | Instance, verified `p528` | What the probe sees | What ships |
|---|---|---|---|
| 🔴 **Transitive copyleft** | [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) | **MIT** | Links **PyMuPDF (AGPL-3.0)** for PDF extraction — the page says so itself. Network copyleft reaches the hosted deliverable. |
| 🟡 **Non-code grant** | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) · **926★** | sidebar names **no licence**; README badge reads CC BY-SA 4.0 | **CC BY-SA 4.0** — a *content* licence. ShareAlike propagates to adaptations, no patent grant, and the code/content line is undrawn across a 157-tool MCP server and 165 prose skills. |

**The gate, four commands and two questions.**

1. `curl -s raw.githubusercontent.com/<repo>/<branch>/README.md` → **does the
   address resolve at all?** A 404 everywhere is *absent*, not *ungranted*.
   (`belentani7/aprende-brasil`: a search summary described 205 modules and a
   tutor named "Nilo"; the repository does not exist.)
2. Read the **licence file's title block** — not the badge, not the sidebar.
3. **Enumerate the dependency licences** (`requirements.txt`, `pyproject.toml`,
   `package.json`, `Cargo.toml`) and take the **union**. 🔵 *The grant you ship is
   the union of the grants you link.*
4. Ask **what the licence was written to cover.** CC BY-SA on an executable skill
   library and MIT on a corpus are both category errors; only the first is
   currently common, and it is on the largest education-skills repo in the field.

**Output.** One row per component: address resolves (y/n) · grant from title
block · dependency grants · union verdict · *written for code or for content*.
🟢 **Any `ShareAlike`, `NonCommercial` or `AGPL` in the union stops the fork
decision**, whatever the top-level badge says.

## 🆕 P557 — Mastery-tracked tutoring with real retention (Global)

**Brief.** Every "AI tutor" demo answers questions. Almost none **model what the
learner knows** or **schedule the review that makes it stick** — the two things
fifty years of cognitive science say decide the outcome. Both halves now exist
permissively and neither needs building.

| Role | Component | Grant | Verified `p529` |
|---|---|---|---|
| Tutoring + **mastery estimate** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | API + title block · **57★** · Go · pushed 28 Oct 2026 · topics name **`bkt`** |
| Retention **algorithm** | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | API + title block · **4,119★** · 165 forks |
| Retention **surface** the learner keeps | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** | API · **538★** |
| Independent mastery baseline | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** | API · **274★** · BKT, published |
| Does the model teach acceptably? | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | API · 13★ · CDPK + SEND |
| Event records in a standard shape | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | xAPI/LRS · 51★ |

**Wiring.** `tutor-mcp` mounts as an MCP server beside whatever assistant the
client already licenses — it is not an application, so there is no UI to
displace. It holds the learner model; every turn updates a **BKT** estimate per
skill. When a skill crosses mastery, the agent emits a card through
`anki-mcp-server` and **`fsrs4anki` owns the interval** — do not invent a review
schedule, the problem is solved and the solution is MIT. `ralph` receives xAPI
statements so the mastery trace lives in a standard store rather than a vendor
table. `OATutor` is the control: run the same cohort against a published BKT
implementation and compare, because *"our tutor tracks mastery"* is a claim an
institution will ask you to prove.

🟢 **Why this composition and not a bigger one.** Every component is **MIT**,
every one was verified twice this pass, and the whole stack is **out-of-process**
— so it drops beside a GPL Moodle or an AGPL Canvas without touching either.
**8–10 weeks.** 🔴 **Gate it with `P551` + `P556`:** all six rows are
*repository*-level verdicts, and `fsrs4anki` ships Python/Jupyter with a real
dependency tree.

## 🆕 P558 — The Moodle bridge **generator** (the build the field actually needs)

**Brief.** 🔴 **`P553` assumed a missing product. The measurement says otherwise:
the field has 222 addresses, 14 of the top 26 bridge exactly one named
university, and nobody has consolidated anything.** You cannot consolidate
repositories whose purpose is to be institution-specific. **What is missing is
not a bridge — it is the thing that produces a bridge**, with the safety and
audit properties an institution's legal and data-protection review will demand.

| Role | Component | Grant | Note |
|---|---|---|---|
| Tool-vocabulary reference | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** · 27★ | The only one naming three live-tested Moodle versions (**3.7, 4.5, 5.2**) |
| **Write-gating** reference | [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | **MIT** · 3★ | Writes off by default behind two flags; `confirm=true` on destructive calls — **the best governance model in the field** |
| Scope-boundary reference | [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) | **MIT** · 2★ | `MOODLE_DEV_COURSE_WHITELIST`, `MOODLE_PROD_ALLOW_WRITES=false` |
| Architecture to copy wholesale | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ | The field's one proven LMS bridge |
| The platform — **never forked** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 · 7.6k★ | Bridge stays out-of-process |
| Per-tenant worked examples | [`iDavi/usp-mcp`](https://github.com/iDavi/usp-mcp) (🔴 GPL-3.0), [`Equisdo/fich-mcp`](https://github.com/Equisdo/fich-mcp) (**MIT**), [`changazo/udesa-mcp`](https://github.com/changazo/udesa-mcp) (**Apache-2.0**) | mixed | **Read for requirements, do not vendor.** USP is GPL-3.0 — copying it into a permissive core relicenses the core |
| Audit trail | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ | Every tool call becomes an xAPI statement |

⛔ **Do not start from** [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp)
(52★, **no licence file** — the field's most-starred artefact is unshippable),
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)
(**AGPL-3.0**), `threos/mcp4lms` (**AGPL-3.0**), or
[`sonstellar969/open-moodle`](https://github.com/sonstellar969/open-moodle)
(MIT repo, **AGPL-3.0 PyMuPDF** in the artefact — `P556` catches this one).

**Wiring.** One permissive core (`MIT`/`Apache-2.0`) implementing a **named tool
vocabulary** taken from `G36maid`, with three properties the hand-built instances
almost never have: **read-only by default**, writes behind an explicit per-course
allowlist (`leshamblin`) plus confirmation on destructive calls
(`moodler-mcp`), and **token custody** that never puts a Moodle Web Services
token in a shared config. Per-institution output is **configuration plus a
capability manifest**, not a fork: endpoint, enabled tools, course scope, data
residency. `ralph` makes every call auditable, which is what converts this from
a student project into something a DPO signs off.

🔵 **Why it sells.** The per-campus bridges cluster in **LATAM and APAC**, where
institutions build because nobody sells them this; **North America builds none**,
because NA institutions buy integration. So the same artefact is a *cost
reduction* in LATAM/APAC — a day instead of a semester, with governance attached
— and a *product* in NA. **10–12 weeks for the core + 1 week per tenant.**
🔴 Gate with `P551` + `P556` before any row above enters a deliverable.

## 🆕 P562 — The computational course, served from inside the LMS (Global; EMEA/North America first)

**When.** The client teaches anything where the student writes code or runs a
notebook — data science, statistics, engineering, bioinformatics — and the ask is
"put AI in the course". 🔴 **The pedagogical part is not the hard part; serving
500 students a reproducible environment, authenticated out of the LMS, is.** This
pattern is entirely permissive and almost entirely assembly.

**The stack, bottom to top — every piece verified this pass.**

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Compute | [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | BSD-3-Clause · 611★ | One notebook pod per student, with per-student CPU/RAM limits as config |
| …or, on a cluster | [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | BSD-3-Clause · 207★ | Spawn into Slurm/PBS/LSF when the client's compute is a research queue |
| …or, for a pilot | [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | BSD-3-Clause · 543★ | One host, Docker, one afternoon |
| Identity | [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | BSD-3-Clause · 73★ | 🔴 **The load-bearing row.** LTI launch from Moodle/Canvas/Brightspace — no second login |
| …or SSO / directory | [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) · [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | BSD-3-Clause · 443★ / 214★ | OIDC where the tenant has SSO; LDAP/AD where it has a directory, which in EMEA public-sector estates it does |
| Assignment lifecycle | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause · 1 370★ | Release, collect, autograde, manual-grade, return |
| …or a full platform | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** · 823★ | Use instead of nbgrader when exercises span programming, modelling and text, and an exam mode is required |
| The agent | any shelf row from [`../agents/top.md`](../agents/top.md) | MIT/Apache-2.0 | Runs **inside the student's own kernel**, so it reads the code they wrote rather than a paraphrase of it |

**Wiring.**
1. Deploy the hub with `kubespawner` (or `batchspawner` on HPC). Pin the image.
2. Register the hub as an **LTI 1.3 tool** in the LMS and configure
   `ltiauthenticator`. 🟢 This is the step that makes it a course rather than a
   demo: the student clicks the assignment in Moodle and lands in their own
   server, already identified.
3. Install `nbgrader` for release/collect/autograde. Keep the autograder
   deterministic — the model never decides the mark.
4. Attach the agent in the kernel with a **read-only** view of the student's
   notebook and an explicit refusal to emit the solution cell. The agent's
   output is a hint and a next step; `nbgrader` produces the grade.
5. Emit xAPI statements to an LRS ([yetanalytics/lrsql](https://github.com/yetanalytics/lrsql),
   Apache-2.0) so engagement and hint-use are measurable rather than anecdotal.

🔴 **Two traps, both measured.** The official JupyterHub deployment tutorial
([`jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial),
202★) is **archived by its owner** — write your own runbook and do not cite it
to the client. And [`wrapspawner`](https://github.com/jupyterhub/wrapspawner)
(65★), which is what you reach for to let students choose a profile, was last
pushed **2025-08-16**: pin it.

**Why this is the pattern and not a shopping list.** Every row is
BSD-3-Clause or MIT, so the deliverable can be proprietary; the only copyleft in
the picture is the LMS you are *attaching to*, and LTI is a protocol boundary,
not a linkage. 🟢 **The licence question answers itself.**

---

## 🆕 P563 — Adaptive assessment a ministry would accept (LATAM-led, globally applicable)

**When.** The client wants "personalised testing" and the buyer is a ministry, a
board or a university registrar — i.e. somebody who will ask **how the score was
derived**. 🔴 An LLM choosing the next question is not an adaptive test; it is an
unaudited one.

**The stack.**

| Layer | Repo | Licence | Role |
|---|---|---|---|
| Psychometrics | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · 153★ | IRT item banks, item selection, ability estimation, stopping rules — **the audited core** |
| Item interchange | [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** · 6★ | QTI 3 items, so the bank outlives the vendor |
| Item *generation* | a shelf agent + the client's curriculum | MIT/Apache-2.0 | Drafts candidate items **into the bank**, never into the exam |
| Curriculum anchor | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) (Brazil, MIT) · the client's own standard elsewhere | MIT | Each item carries the objective it tests, with provenance |
| Retention | [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | **MIT** · 180★ | Schedules the *review*, which is a different job from scoring |
| Records | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 · 144★ | xAPI statements per response |

**Wiring.** The agent writes items; a human calibrates them; `catsim` selects and
scores; `fsrs.js` schedules the revisit. 🔴 **The line that makes it defensible:
the model is upstream of the item bank and nowhere near the score.** Every
delivered item has IRT parameters estimated from real responses, and the
ability estimate comes from `catsim`, which is 153★ of published method rather
than a prompt.

🟢 **Why LATAM-led.** `catsim`'s author is in Brazil and
[`Dramoscuello/simic`](https://github.com/Dramoscuello/simic) already does the
ICFES Saber 11 shape in Colombia; `bncc-dados` carries **1 721** BNCC objectives
with per-record provenance. 🔵 The region has the exam culture, the standards as
open data and now the psychometrics — which is a stronger starting position than
any other region holds for this pattern.

---

## 🆕 P564 — The transitive-grant answer, retrieved rather than built (run inside `P551`)

**When.** Always, before the deliverable ships — and specifically when `P551`'s
shelf-level licence check has passed and somebody asks the real question:
**what grant does this thing carry once its dependencies are counted?**

🔴 **`Gap 528-C` scoped a dependency-grant enumerator as a build for four
passes. It did not need building.**

| Tool | Licence | Use it when |
|---|---|---|
| [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | **Apache-2.0** (engine) · 🟡 **CC-BY-4.0** (licence datasets) | You need the **evidence**: it detects licences, copyrights, package manifests and **direct dependencies**, and processes manifest and lockfile formats to Package URLs. This is the artefact you hand a client's legal team. |
| [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | **Apache-2.0** · 2 109★ | You need a **gate in CI**: the *Analyzer* resolves dependencies across package managers, the *Evaluator* runs policy-as-code, and it emits SPDX/CycloneDX plus attribution documents. |
| [anchore/syft](https://github.com/anchore/syft) | **Apache-2.0** · 9 792★ | You need the **deployed artefact's** bill of materials, from the image rather than the source tree. |

**Wiring.** `ort analyze` → `ort evaluate` with a policy that fails on AGPL-3.0
reaching a shipped binary → `scancode` over the same tree for the evidence pack
→ `syft` over the built image, so the claim covers what actually runs.

🔴 **Read `scancode`'s dual grant before redistributing.** The engine is
Apache-2.0; the reference licence data is **CC-BY-4.0**, so shipping the rule set
inside a product carries attribution duties. 🔵 **That is exactly the
"granted, but not under a code licence" band this base opened at `p528`, and it
appears here in the tool you would use to check for it.**

---

## 🆕 P565 — Brightspace, the third LMS (North America first)

**When.** The client runs **D2L Brightspace** — which, in North American higher
education, a large share of them do, and which this base had no agent row for
until this pass.

**The stack.** [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(**MIT, 60★**, npm-published, works against any tenant) for grades, due dates,
assignments, announcements, rosters, syllabus and content · a shelf agent from
[`../agents/top.md`](../agents/top.md) as the reasoning half ·
[`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (**Apache-2.0, 373★**) if
the deliverable must also appear *inside* the LMS as a tool rather than only
beside it · [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) for the
record.

**Wiring.** MCP for the read path and the teacher-facing write path (grades,
comments); LTI 1.3 via `ltijs` for placement and launch; AGS for grade passback
when the tool owns the activity. 🔴 **Do not fork Brightspace** — it is not open
source at all, which makes the API and LTI the *only* boundaries, and therefore
makes this the cleanest of the three LMS patterns rather than the hardest.

🔵 **Parity note, stated because it is the reason this pattern exists:** the
shelf now carries Canvas ([`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp),
MIT, 308★; [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp),
MIT, for the **write** half) and Brightspace, and for Moodle still carries a
**build** (`P553`, `P558`) rather than a row. 🔴 **Moodle — the largest LMS in
the world — remains the one with no credible off-the-shelf bridge**, and that
has now been true across four passes.

---

## 🆕 P567 — The institutional assessment stack, permissive end to end (EMEA-first; North America with one substitution)

**Brief.** A university or ministry wants automated assessment *with* a tutor that
explains the result, and it must be self-hosted, auditable and extensible with
proprietary work. 🔴 **This base's previous answer was "fork Artemis and build the
feedback agent."** That build is unnecessary: TU München already ships it, under
**MIT**, as a separate repository. The pattern is now assembly, not construction.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Platform | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** · 823★ | Programming, modelling, text and quiz exercises, proctored exam mode, in production across European universities |
| Tutor | **Iris** in [ls1intum/edutelligence](https://github.com/ls1intum/edutelligence) | 🟢 **MIT** · 17★ | Explains a failing exercise from the **submitted code, the assessment feedback and the build logs** — not from the prompt alone. RAG over instructor material; FastAPI + Weaviate |
| Assessment | **Athena** (same repo) | 🟢 **MIT** | (Semi-)automated assessment for **text and programming** exercises, built for large-course scale |
| Competencies | **Atlas** (same repo) | 🟢 **MIT** | Generates the competency model, infers relationships, recommends activities. 🟢 **Its README states it is adaptable to other LMSs — so this layer is liftable on its own** |
| Sandbox | [judge0/judge0](https://github.com/judge0/judge0) | 🔴 **GPL-3.0** · 4,498★ | Only if Artemis's own container grading is insufficient. 🔵 **Deploy as a separate network service**: GPL-3.0 has no §13, so the deliverable does not inherit the grant |
| Evaluation | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** · 13★ | Answers *"does the model we routed to actually know how to teach"* (CDPK/SEND) before it faces students |
| Deployment | [ls1intum/artemis-ansible-collection](https://github.com/ls1intum/artemis-ansible-collection) | 🟢 **MIT** | The maintainers' own runbook |

**Wiring, concretely.** Artemis speaks to EduTelligence over its REST seam —
**pin the pair using the suite's 21-row compatibility matrix** (Artemis `10.2.x`
↔ EduTelligence `3.2.x`; never infer the pairing). Point Iris's model routing at
whatever the engagement's sovereignty rules allow (self-hosted via Ollama/vLLM,
or a hosted API) and Weaviate at the instructor corpus. Athena runs behind the
existing grading pipeline, so **the grade stays deterministic and only the
explanation is generated** — the single most defensible division of labour in
assessment, and the one that survives Oklahoma S.B. 1734-style rules barring AI
as the *primary basis* for a grade.

🔵 **North America substitution:** swap Artemis + Athena for
[autolab/Autolab](https://github.com/autolab/Autolab) (**Apache-2.0**, 808★,
Carnegie Mellon) and keep Atlas and the benchmark. Autolab is the same idea under
a permissive grant with CMU's deployment history, and
[uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal)
(**Apache-2.0**) is the natural student-facing shell in a US higher-ed estate.

**Effort.** 🟢 **4–6 weeks** to a running pilot on a real course, against the
**10–12** this base previously implied for the same outcome — the saving is the
tutor and assessment services that no longer need writing. Budget the time in
model routing, the instructor corpus, and the EU AI Act Art. 50 transparency
duties (in force since `2026-08-02`), **not** in agent code.

🔴 **What to check before promising it.** EduTelligence is **17★** — the
institution, the deployment at `artemis.cit.tum.de` and the release discipline
are the evidence, not the counter. Read the three services' own READMEs for
per-service Python versions (3.13 for Iris and Atlas, **3.11** for Athena) and
confirm the compatibility row for the Artemis version the client actually runs.

## 🆕 P568 — The split-grant gate (run inside `P551`, after `P556`)

**Brief.** `P551` reads the licence file; `P556` takes the **union** of linked
dependency grants. 🔴 **Neither handles a repository whose own licence file names
two grants scoped to different directories** — and that is the normal shape for a
corpus, an item bank or a benchmark, which is where this sector's value is
moving (trend 19).

| Failure | Instance, verified `p533` | What a repo-level probe sees | What is actually granted |
|---|---|---|---|
| 🔴 **Split grant, scoped by path** | [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) · 12★ | `NOASSERTION` (API); a title line reading only `# Licenças`, naming no licence family | **MIT** for `harness/`, `test/` and config · **CC BY 4.0** for `itens/`, `resultados/`, `METODOLOGIA.md` and docs |
| 🟡 **Third-party output inside a granted repo** | same repo, `resultados/` | one grant for the whole tree | Model responses generated by **third-party models**, whose own reuse conditions the repo explicitly pushes to `resultados/README.md` |

**The gate, three steps.**

1. **If the licence file's title line names no licence family, do not grade the
   repository — read the body.** Look for `##`-level headings that name a scope
   (a directory, "código", "dados", "datasets", "models", "content"). 🔵 Every
   rule on [`../agents/top.md`](../agents/top.md) reads the *title line*; this is
   the case that defeats all of them.
2. **Record the grant per path**, as `grant | grant@path` — e.g.
   `MIT | CC-BY-4.0@itens/,resultados/`. A single cell cannot carry it, and
   flattening it to either grant is wrong in a different direction each way.
3. **Ask which half you are actually shipping.** 🔴 **`CC BY 4.0` is not a
   software licence**: it grants no patent terms and no sublicensing, and
   attribution must travel with the data. Shipping an item bank inside a
   proprietary deliverable is therefore a *different legal act* from shipping the
   harness, even though one `git clone` produced both. If the corpus is
   `NonCommercial` (as with `xiaoyang111222/cn-math-taxonomy`, **CC-BY-NC-4.0**),
   the data half stops the engagement while the code half is fine.

**Output.** One row per component: grant on the title line (or `names-none`) ·
per-path grants · *which paths this deliverable actually ships* · verdict.
🟢 **A benchmark you only ever *run* is a much easier case than a corpus you
*redistribute*** — and separating those two uses is usually what unblocks the
deal.

## 🆕 `p534` — two patterns added, one grant corrected by a gate

🟢 **`P569`** assembles a university AI service from **MIT Open Learning's own
production code** — the find that closed `Gap 533-A`. 🟢 **`P570`** replaces the
Frappe recipe this file would otherwise have recommended, because its agent
layer was **archived seven days before this pass**. 🔴 **And `P570`'s first draft
graded `frappe/frappe` as AGPL-3.0; `make gate-shelf-consistency` caught it
against [`../repos/foundations.md`](../repos/foundations.md) before commit and
the licence file settles it as MIT.** 🔵 Each pattern below also now carries a
**security precondition** where its components have published advisories — see
`P569`, whose Canvas bridge published **four advisories on 2026-10-25**, two of
them **High**.

## P569 — The university AI service, started from a peer university's production code (North America first; Global)

**Brief.** A university wants a student-facing AI service — tutor, syllabus
answers, video Q&A, resource recommendation — self-hosted, auditable, and
extensible by its own staff after the studio leaves. 🔴 **This base's previous
answer was to assemble a tutor from a pedagogical engine plus a framework and
write the service layer.** That service layer already exists, under **MIT**,
written by MIT Open Learning and running at `learn.mit.edu` — and `p534` found
it at **0★**.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Service | 🆕 [mitodl/learn-ai](https://github.com/mitodl/learn-ai) | 🟢 **MIT** · 🔴 0★ · **816 commits** | **Four education agents already wired**: resource recommender, syllabus bot, **VideoGPT**, **TutorBot** — LangGraph graphs served over **Django Channels** (streaming, not request/response) |
| Pedagogy | [mitodl/open-learning-ai-tutor](https://github.com/mitodl/open-learning-ai-tutor) | 🟢 **MIT** · 1★ | The tutoring engine `learn-ai` serves. Keep them as a pair — they are one system split across two release cadences |
| Agent toolchain | 🆕 [mitodl/agent-kit](https://github.com/mitodl/agent-kit) | 🟢 **BSD-3-Clause** · 5★ | `witan-core` (shared memory), `witan-council` (work coordination), `witan-code` (code graph), `agent-config-kit` CLI, MCP install helpers, Claude Code + Copilot agent definitions |
| Observability | **Opik** + LangSmith + PostHog, as `learn-ai` already integrates them | per-vendor | 🟢 **Already wired, which is the rare part.** MIT runs Opik self-hosted at `opik.ol.mit.edu` — take that deployment shape when the client cannot send traces off-premises |
| Eval | `learn-ai`'s own **RAG evaluation** harness + [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | Retrieval quality from the repo, *pedagogical* quality from the benchmark. 🔵 They measure different failures and a client will ask about both |
| LMS seam | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (read) + [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) (write) | 🟢 **MIT** · 308★ / 10★ | Canvas dominates US higher ed. 🔴 Do not fork Canvas itself — attach over LTI 1.3 + MCP |

🔴 **Security precondition, added after reading the bridge's own advisories this
pass — do not skip it.**
[`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
published **four advisories on 2026-10-25**, two of them **High**. Pin
**≥ 1.16.0** *and* **Node.js ≥ 22.18** (below that floor the patched release
refuses to run `execute_typescript` at all, so upgrading the package alone leaves
the deployment unpatched), or set `EXECUTE_TYPESCRIPT_ENABLED=false` and lose
nothing this pattern needs. 🔴 **Even patched, code executed in local sandbox
mode can still reach the caller's Canvas token**, and outbound network blocking
there is best-effort (issue #157). 🔴 **And `GHSA-hmr8-mvr2-mvw5` is the one that
bites *this* pattern specifically:** *"prompt-injected assistant could disclose
course data or change grades through first-call write tools"* — which is exactly
the write mount below. 🟢 **So the write server is not merely flag-gated, it is
gated on a human confirmation for grade and enrolment calls**, and the tutor
graph must never pass retrieved course text into a write tool's arguments
without a confirmation step. That is the trend-12 thesis in operational form:
the integration layer inherits the authority of the system it attaches to.

**Wiring, concretely.** Stand up `learn-ai` as the service and `agent-kit` as the
developer environment around it; keep `open-learning-ai-tutor` as a pinned
dependency rather than vendoring it, because the two move on different cadences
(this is trend 18 applied at the dependency level). Point the LangGraph model
routing at whatever the engagement's sovereignty rules allow. Mount the Canvas
MCP servers as tools on the TutorBot graph — **read server by default, write
server behind an explicit flag and a course allow-list**, which is the governance
pattern `leshamblin/MoodleMCP` demonstrates and this stack does not ship. Run the
RAG eval harness in CI from day one; it is the artefact that makes the
"is it working?" conversation answerable.

**Effort.** 🟢 **4–6 weeks** to a pilot on one faculty's courses — the service,
the four agents, the tracing and the eval harness are all inherited. Budget in
the **corpus** (syllabi, lecture video, library holdings), the Canvas tenant
negotiation, and institutional review. 🔴 **Not** in agent code.

🔴 **What to check before promising it.** `learn-ai` has **0 stars and no
forks**: the evidence is the **816 commits**, the named RC deployment
(`rc.learn.mit.edu`, `api.rc.learn.mit.edu`) and the fact that a peer
institution runs it — not the counter. Read the per-service setup in its README
(the backend expects port 8005, the sandbox frontend 8003) and confirm the
LangGraph and Django Channels versions against the client's Python estate.
🔵 **And say out loud what this pattern really is:** adopting another
university's internal service, which means inheriting its assumptions about
identity, course structure and content licensing. That is a governance
conversation, not a technical risk, and it is cheaper than the alternative.

## 🆕 P570 — The Frappe-stack education engagement, after Flow was archived (Global; LATAM and APAC SMB-first)

**Brief.** A school group or training provider already runs the **Frappe /
ERPNext** stack for administration and wants agents on top of it. 🔴 **The
obvious component is gone:** [`frappe/flow_client`](https://github.com/frappe/flow_client)
— *"native AI agents, tools and triggers for Frappe"*, **89★** — was marked
**`Public archive` on 2026-10-22**, seven days before this pass. 🔵 **This
pattern exists because the archive flag is only readable on a channel this base
believed was closed** (see `p534`'s channel correction), and without it this file
would have recommended a retired dependency.

| Layer | Component | Grant | Note |
|---|---|---|---|
| ERP / SIS | [frappe/education](https://github.com/frappe/education) | 🔴 **GPL-3.0** | School management on the Frappe stack. 🔴 **Not the same grant as Frappe LMS** |
| LMS | [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · 3.4k★ | Network copyleft — decisive for a hosted deliverable |
| Framework | [frappe/frappe](https://github.com/frappe/frappe) | 🟢 **MIT** — `The MIT License · Copyright (c) 2016-2021 Frappe Technologies Pvt. Ltd.`, read at **`develop/LICENSE`** (1 118 B, `bc6001a54ffc`) | 🔴 **This cell said `AGPL-3.0` when this pattern was first written, and `make gate-shelf-consistency` caught it against [`../repos/foundations.md`](../repos/foundations.md) *before commit*.** The framework is **permissive**; the *apps* on it are not (`education` GPL-3.0, `lms` AGPL-3.0). 🔵 Also note the default branch is **`develop`**, not `master` as the foundations row cites — rule 11 |
| 🔴 Agent layer | ~~[frappe/flow_client](https://github.com/frappe/flow_client)~~ | 🔴 **AGPL-3.0 · ARCHIVED 2026-10-22** | ⛔ **Do not build on it.** No upstream, no security fixes, and AGPL anyway |
| 🟢 Agent layer, instead | **Your own service against the Frappe REST API**, orchestrated with [mitodl/agent-kit](https://github.com/mitodl/agent-kit) (**BSD-3**) or plain LangGraph | 🟢 permissive | 🟢 **The REST boundary is also the licence boundary** — an external service calling Frappe's API does not inherit AGPL the way a vendored app does |
| Retention | [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | 🟢 **MIT** | Scheduling is solved; do not invent intervals |
| Tutor | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · 57★ | Mastery estimation (BKT) as one MCP server, mountable from outside the Frappe process |

**Wiring, concretely.** Run the agents as a **separate service** that
authenticates to Frappe over REST with a scoped API key — never as a Frappe app
in the same process, which is both the licence boundary and the upgrade
boundary. Model the student, course and enrolment reads as MCP tools over that
API so the same tool surface works against ERPNext and, later, against a
different SIS. Write-backs (attendance, grades, fee notes) go behind an explicit
allow-list per site, exactly as the Moodle census's best-governed bridges do.

**Effort.** 🟡 **6–8 weeks**, which is **2–3 weeks more** than the same
engagement would have cost with Flow alive. 🟢 State that honestly in the
estimate: the saving from a maintained upstream was real and it is gone.

🟢 **One grant correction, found by a gate rather than by a reader.** The first
draft of this pattern graded `frappe/frappe` as **AGPL-3.0** from the
surrounding prose. `make gate-shelf-consistency` — which `p534` is the first
pass in eleven to run — flagged it against the **MIT** cell on
[`../repos/foundations.md`](../repos/foundations.md), and the licence file
settles it: **`The MIT License`**, read at `develop/LICENSE`. 🔵 **The
architectural consequence is the opposite of what the draft implied:** the
*framework* is permissive and only the *apps* are copyleft, so a service built
against Frappe's framework and API has more room than the AGPL cell suggested.

🔴 **What to check before promising it.** Confirm whether Frappe has published a
successor to Flow — this pass found none, and an archive without a named
replacement is the signal that the vendor's own AI strategy has moved. 🔴 **And
re-read the grants per app:** `education` is **GPL-3.0** and `lms` is
**AGPL-3.0**, two different copyleft regimes on one stack, so a deliverable
spanning both inherits both.

## 🆕 P572 — The access-type-aware content pipeline (North America first; run inside `P551`)

**When the brief is:** *"ground our teacher copilot in real instructional content and
real rubrics, not in a prompt"* — the US K-12 and higher-ed shape, against a buyer who
will ask who vouches for the content.

**Why this pattern exists.** `p536` filed the three repositories Anthropic's
`k12-teacher-skills` is built *"with"*, and the two that matter most here do **not have a
repository-level grant**. Vendoring them the way a studio vendors a library is not a
licensing risk to be managed later — it is **incorrect**, and the payload says so.

**Components, all measured at `p536`:**

| Role | Component | Grant | Note |
|---|---|---|---|
| Instructional content | [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🔵 **MIT code; data Open / Open + Gated / Gated, per download** | 164★. The grant is **per row and time-varying** |
| Rubrics + scoring | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🔵 **code MIT · rubrics CC BY 4.0 · corpora CC BY-NC-SA** | 87★. Ship the first two; **do not ship the third** |
| Teacher skills | [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) | 🟢 **Apache-2.0** | 40★ — the only part of the stack permissive end to end |
| Teacher workflows + eval rubrics | [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 Apache-2.0 | 601★, already on the agent shelf |
| Permissive calibration set | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | 13★ — the fallback when the NC corpora are out of bounds |
| SBOM / dependency grants | [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) | 🟢 Apache-2.0 | 552★ — `P556`'s instrument, now named |

**Wiring, in order. The first step is the pattern; the rest is ordinary work.**

1. 🔴 **Build the manifest before the pipeline.** For every dataset and **every
   download** you intend to use, record: dataset id, download id, **access type**
   (`Open` / `Open+Gated` / `Gated`), licence (`CC BY 4.0` / `CC0` / per-agreement),
   upstream source for attribution, and the date read. This is a table in your repo, not
   a comment — the payload states terms *"can change between releases"*, so the manifest
   carries a read date or it is worthless.
2. 🔴 **Make `Gated` un-compilable, mechanically.** The ingest step refuses any row whose
   access type is not `Open`, unless an explicit access-agreement id is present in the
   manifest. A build that *can* include a Gated row eventually will.
3. 🟢 **Carry attribution to the original source, not to the distributor.** The payload
   is explicit: attribution *"travels with the data"*. A CC BY 4.0 build owes each
   upstream publisher. Emit the attribution file from the manifest, so it cannot drift.
4. 🟢 **Calibrate behind a boundary; ship thresholds, not corpora.** Run `evaluators`
   against the annotated CLEAR / PERSUADE corpora **in a non-shipped evaluation
   environment**, record rubric version + resulting thresholds, and ship the thresholds.
   Where the client needs the calibration itself to be redistributable, calibrate against
   `pedagogy-benchmark` instead and say which you did.
5. 🟢 **Mount the skills.** `agent-skills` + `k12-teacher-skills` over the content
   resolved in step 2; the rubrics from step 4 gate the output.
6. 🟢 **Run `P556` with a real instrument.** `cyclonedx-cli` produces the dependency
   SBOM; the grant union is computed from it rather than asserted. This is `Gap 528-C`'s
   remedy, finally holding a tool.

**Timeline:** 5–7 weeks. The manifest and the ingest gate are ~1.5 weeks of that and are
the part a client cannot do themselves, because it requires re-reading the catalogue each
release.

🔴 **What this pattern does not do.** It does not get you the Gated content. If the
engagement needs the instructional or assessment materials behind the gate, that is a
**commercial conversation with the data provider**, and it should happen in week 1, not
week 6. Say so in the proposal.

---

## 🆕 P573 — The ministry-data advisory agent, two countries from one pattern (LATAM; APAC with one substitution)

**When the brief is:** *"an agent that answers questions about our education system using
our own published data"* — a ministry, a regional secretariat, a university consortium or
an NGO that must cite official figures rather than a model's recollection.

**Why this pattern exists, and why now.** `p536` placed the two halves in two different
countries, both **MIT**, and neither had ever been filed: the **agent** shape in Colombia
and the **data** shape in Chile. 🟢 Separately they are 0★ and 136★ curiosities; together
they are a repeatable engagement, and a third country (India) has just published the
*government-shipped* version of the same thing, which is the precedent to quote.

**Components:**

| Role | Component | Grant | Region |
|---|---|---|---|
| Agent over national open education data | [`startin-lab/brujula-educativa`](https://github.com/startin-lab/brujula-educativa) | 🟢 **MIT** | 🟢 LATAM (Colombia) |
| Curated, normalised national public data | [`cortega26/chile-hub`](https://github.com/cortega26/chile-hub) | 🟢 **MIT**, 136★ | 🟢 LATAM (Chile) |
| 🟢 **The precedent**: a ministry shipping its own MCP | [`nso-india/esankhyiki-mcp`](https://github.com/nso-india/esankhyiki-mcp) | 🟢 **MIT**, 147★, copyright **MoSPI** | 🟢 APAC (India) |
| Orchestration + policy nodes | `LangGraph` | 🟢 MIT | — |
| Rural / low-connectivity delivery | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | 🟢 **MIT** | 🟢 LATAM |
| Offline-first distribution | `Crosstalk-Solutions/Project-NOMAD` | 🟢 Apache-2.0 | — (`p532`) |
| Citation-grounded retrieval reference | [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | 🟢 MIT | — |

**Wiring:**

1. 🟢 **Normalise before you retrieve.** `chile-hub`'s contribution is not data, it is
   *validated, normalised* data — which is the step a ministry's own portal has usually
   not done. Replicate its schema for the target country rather than importing its rows.
2. 🟢 **Expose the data as an MCP server, not as a RAG index.** This is the
   `esankhyiki-mcp` lesson: official figures are **queried**, not *recalled*, so the
   agent asks for a number and gets that number with its series and vintage attached. A
   vector index over statistical tables invents plausible figures, which is the one
   failure mode this buyer cannot tolerate.
3. 🟢 **Make every answer carry its citation.** `brujula-educativa` is the shape;
   `adaptive-knowledge-graph` is the reference implementation of *cited* answers over an
   openly-licensed corpus.
4. 🟡 **Add the rural path only if the brief has one.** `TutorIA` (rural higher ed) and
   Project-NOMAD (offline-first) make the same agent reachable where connectivity is not
   assumed — §6 of [`../verticals/solutions.md`](../verticals/solutions.md).
5. 🔵 **Lead the proposal with the precedent, not the architecture.** India's Ministry of
   Statistics and Programme Implementation publishes its own MCP server under **MIT**.
   For a ministry deciding whether to expose data this way, that is worth more than any
   diagram.

**Timeline:** 6–8 weeks per country; the second country is ~3, because steps 2–3 carry
over and only step 1 is country-specific.

🔴 **Stated limits.** `brujula-educativa` and `TutorIA` are **0★, pre-release, single-lab
artefacts** — read the architecture, do not take the dependency. And this pattern is
**only as good as the portal**: where a ministry publishes nothing machine-readable,
step 1 is a data-engineering engagement in its own right and should be priced as one.

---


## 🆕 P574 — The Gulf engagement, where there is nothing to fork (EMEA — Saudi Arabia, UAE)

**The problem this solves.** `Gap 536-D` and `Trend 25`: the Gulf has the highest
teacher-adoption figure on this base (**UAE ~75 %**) and, across its two leading AI
institutions, **one permissively licensed repository in nine**. Every other recipe here
starts by forking a platform. 🔴 **In the Gulf there is no platform to fork**, so a
recipe that assumes one produces a proposal the client cannot accept.

**Components, each grant read first-hand at the resolved default branch:**

| Role | Component | Grant | How it is used — and the constraint |
|---|---|---|---|
| Capability model | [`mbzuai-oryx/groundingLMM`](https://github.com/mbzuai-oryx/groundingLMM) | 🟢 **Apache-2.0** (11 356 B) | **The only buildable Gulf-origin asset.** GLaMM grounds language to *regions of an image*, so it is the layer for marking diagrams, geometry and handwritten working — build on it freely, including commercially |
| Curriculum | [`KAUST-Academy/Artificial-Intelligence-Courses`](https://github.com/KAUST-Academy/Artificial-Intelligence-Courses) · [`2026_Introduction_To_AI`](https://github.com/KAUST-Academy/2026_Introduction_To_AI) · [`2026_Advanced_AI`](https://github.com/KAUST-Academy/2026_Advanced_AI) | 🔴 **GPL-3.0** (35 128 B each) | 🔴 **Integrate and attribute; never fork into a client-branded product.** A derivative of GPL-3.0 courseware distributed to a client's learners is a GPL-3.0 distribution. Two lawful routes: deliver it **unmodified with attribution** alongside your own materials, or **negotiate a separate licence with KAUST Academy** |
| Tutor runtime | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, 59★ | BKT mastery model over MCP — the pedagogy layer, carried in from outside the region because the region ships none |
| Local inference | [`avps82/mentar`](https://github.com/avps82/mentar) — **pattern only** | 🔴 **AGPL-3.0** | 🔴 **Read its Ollama / llama.cpp wiring as a reference and write your own.** AGPL-3.0 §13 makes a hosted product owe source to its users; do not vendor it |
| Compliance record | [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli) | 🟢 **Apache-2.0**, 552★ | Emit an SBOM per delivery. **Mandatory here**, because the copyleft and the permissive components sit in one tree and the boundary is the deliverable |

**Wiring, in order:**

1. **Draw the licence boundary before writing code.** Two artefacts, two grants:
   `product/` (your code + `groundingLMM` + `tutor-mcp`, all permissive) and
   `curriculum/` (KAUST material, GPL-3.0, unmodified, attributed). 🔴 They ship
   as separate deliverables with separate notices — the moment GPL-3.0 content is
   *built into* the product tree, the product is GPL-3.0.
2. **Stand up the tutor loop** with `tutor-mcp` as the MCP server and the client's own
   model provider; mastery state stays on the client's infrastructure.
3. **Add visual marking** by serving `groundingLMM` behind one internal endpoint for
   diagram and worked-answer feedback. Apache-2.0, so this is the only layer you may
   freely modify and re-licence.
4. **Mount the curriculum read-only** and have the agent *cite* it rather than
   reproduce it — citation is not derivation, and it keeps step 1's boundary intact.
5. **Emit the SBOM** with `cyclonedx-cli` and attach the GPL-3.0 notice set.
6. **Bill the licence review as a line item.** 🟢 Four of the nine Gulf
   repositories measured serve **no grant at any of 21 probed paths**, two of them
   pushed within ten weeks of this read. An institution that wants its work adopted and
   has not noticed this is a conversation — and offering to fix it upstream is the
   cheapest goodwill available in the region.

🔵 **What this recipe deliberately does not do:** promise a forkable Gulf
platform, or treat `groundingLMM` as an education product. 🔴 **And it does not
pretend the curriculum problem is technical.** It is a licensing negotiation, and it
should be opened in week one, not discovered at delivery.

## 🆕 P575 — The adapter fleet: one agent, thirteen systems of record it does not control (LATAM, EMEA, North America)

**The problem this solves.** `Trend 41` established the adapter inversion — against a
closed national system, the engagement is *adapter plus agent layer*, not platform
customisation. `p537` filed **thirteen** such adapters, each permissive, each reaching a
named system of record. 🔴 **Every one of them is also a single-author maintenance
liability**, and a recipe that mounts them without saying so hands the client a fleet of
silent dependencies.

**The fleet, as filed on [`../intel/market.md`](../intel/market.md):**

| Region | System of record | Adapter | Grant | Risk to price in |
|---|---|---|---|---|
| **LATAM** (Brazil) | 70 Brazilian public-sector APIs | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟢 MIT, **1 840★ / 287 forks** | 🟢 **Low** — the only adapter here with a real contributor base |
| **LATAM** (Brazil) | BNCC national curriculum | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟡 **Split grant** — code and dataset licensed separately | 🔴 Read **both** notices; `Gap 536-B`'s fourth instance |
| **LATAM** (Brazil) | SUAP (IFRN) | [`django-by-kelsoncm/django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) | 🟢 MIT | 🔴 Single author, 0★, 0 forks |
| **LATAM** (Mexico) | SIASE (UANL) · SAES (IPN) | [`ramomar/siase-schedule-scraper`](https://github.com/ramomar/siase-schedule-scraper) · [`roncuevas/ipn_saes_utils`](https://github.com/roncuevas/ipn_saes_utils) | 🟢 MIT | 🔴 Scrapers — they break when the portal's markup moves |
| **LATAM** (Colombia) | SIA (U. Nacional) | [`gabotachak/sia-unal-bridge`](https://github.com/gabotachak/sia-unal-bridge) | 🟢 MIT | 🟡 Live, 1★ — wraps Oracle ADF as JSON |
| **LATAM** (Chile) | U. de Concepción courses | [`Open-Source-eUdeC/UdeCursos-bot`](https://github.com/Open-Source-eUdeC/UdeCursos-bot) | 🟢 MIT | 🟡 Quiet since 2025-08 |
| **EMEA** (DE/AT/CH) | WebUntis | [`Keule0010/WebUntisAPI`](https://github.com/Keule0010/WebUntisAPI) (Java) · [`Suiram1701/WebUntisAPI.Client`](https://github.com/Suiram1701/WebUntisAPI.Client) (.NET) | 🟢 MIT | 🔴 Both **unofficial**; the vendor rate limit is real (≤1 800/h, permanent blocking as the penalty) |
| **EMEA** (Germany) | Schulmanager Online | [`egore4606/schulmanager-calendar-sync`](https://github.com/egore4606/schulmanager-calendar-sync) | 🟢 MIT | 🟡 Live, self-hosted, 1★ |
| **North America** | PowerSchool · Ed-Fi | [`IronCountySchoolDistrict/powerschool-alchemy`](https://github.com/IronCountySchoolDistrict/powerschool-alchemy) · [`xmarcosx/edfi-via-kubernetes`](https://github.com/xmarcosx/edfi-via-kubernetes) · [`Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-AdminApp) | 🟢 MIT · Apache-2.0 · Apache-2.0 | 🔴 The first two are **stale** (2024-02, 2022-05); `Ed-Fi-AdminApp` is vendor-maintained and current |

**Wiring:**

1. **One MCP boundary, many adapters behind it.** Expose a single tool surface to the
   agent — `list_courses`, `get_timetable`, `get_grades` — and implement it per region.
   🔵 The agent must not know whether it is talking to SIASE or WebUntis; that is
   what makes the fleet a fleet rather than thirteen integrations.
2. **Pin and vendor every adapter at a read commit**, because eight of the thirteen have
   a single author and three have zero forks. 🔴 Treat each as **code you now
   maintain**, not a dependency you track.
3. **Put a contract test per adapter in CI** that runs against a recorded fixture, so a
   portal markup change surfaces as a red test and not as a silent wrong answer in front
   of a learner.
4. **Honour the documented rate limits** — WebUntis is the measured case (≤1 800/h,
   hard ceiling 3 600/h, **permanent blocking** as the penalty), so throttle centrally at
   the MCP boundary, never per adapter.
5. **Emit the SBOM** ([`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli),
   Apache-2.0) and read `bncc-pacotes`' **two** notices separately.
6. **Price the maintenance, not the integration.** 🟢 The build is days per
   adapter; the liability is years. This is the honest shape of the quote, and the reason
   `Mcp-Brasil/mcp-brasil` (287 forks) is worth more than its star count suggests — it
   is the one adapter the client will not be maintaining alone.

## Pattern selection

| If the brief is… | Run |
|---|---|
| Any engagement, before anything else | **P551** licence gate |
| Canvas-based district or university (NA) | **P547** |
| EU vendor, university or ministry with grading/admissions/proctoring AI | **P548** — *establish public vs private clock first* |
| Fastest credible tutoring pilot, any region | **P549** |
| Teacher-facing, PT/ES, public sector (LATAM) | **P550** |
| 🆕 Moodle client, or a reusable asset worth owning | **P553** |
| 🆕 Institution already using AI without a strategy (the 87%) | **P554** |
| 🆕 Brazilian school network, PT-BR curriculum or ENEM marking (LATAM) | **P555** |
| 🆕 Any fork decision — run **after** P551's title-block read | **P556** grant-union gate |
| A claim about learning outcomes needs defending | **P552**, folded into the above |
| 🆕 Ground a teacher copilot in audited instructional content + rubrics (NA) | **P572** — build the per-download manifest **first** |
| 🆕 Ministry, secretariat or consortium wants an agent over its own official data | **P573** (LATAM; APAC with one substitution) |
| 🆕 The client demands an **effect estimate**, not a pilot | **P571** + [`terracotta`](https://github.com/terracotta-education/terracotta) for assignment and consent |

**Components not used, and why:** `advisingapp` (Elastic-2.0 — forbids the hosted
shape), `PageLM` (non-commercial, revenue-share), `cn-math-taxonomy`
(CC-BY-NC-4.0), 🆕 `lumen` (**GPL-3.0**, despite its own README badge saying MIT),
🆕 `csmediapro/moodle-mcp-server` (AGPL-3.0 — see P553), 🆕
`A-R007/Multi-Agent-Study-Assistant`, `idoforgod/Vibe-learning-AgenticWorkflow`
and `tosuki/moodle-mcp` (**ungranted — no licence file at all**), 🆕
`sonstellar969/open-moodle` (MIT, but links **AGPL-3.0** PyMuPDF — see **P556**),
🆕 `GarethManning/education-agent-skills` (**CC BY-SA 4.0**, 926★ — a real grant
with a ShareAlike condition, usable only where the derivative can be published),
🆕 `henriquebotelhogomes/educacao` and `Fatima0923/AssessmentAI` (**ungranted**),
🆕 `JustinoLM/STI-matematicas` (**ungranted — no licence at 10 probed paths**, and the
best-evaluated artefact on this base: UTP Panama, 74 pupils, SUS 70.1 — see `Gap 536-C`),
🆕 `Schlaflied/Plot-Ark` and `avps82/mentar` (**AGPL-3.0**), 🆕 `brownplt/LTLTutor`
(**GPL-3.0**) — the last three usable behind a service boundary, never vendored, and
🆕 the annotated **CLEAR** and **PERSUADE 2.0** corpora inside
`learning-commons-org/evaluators` (**CC BY-NC-SA 4.0** — the code and rubrics beside them
*are* usable; see **P572** step 4).
All of them look usable to a careless probe. See **P551** and **P556**.

---

## 🆕 P559 — The SIS agent, permissive end to end (the greenfield `p530` found)

**Why this is the pass's best build.** Every bridge field this base has censused
is crowded: Moodle has **222** addresses, Canvas has dozens. Crossing
`topic:student-information-system` with MCP returns **nothing** — and as of
`p530` there is a **permissive** SIS to build it against, so the whole stack can
ship under MIT.

**Components, all verified at `p530`.**

| Role | Component | Grant |
|---|---|---|
| Records core | [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 MIT · 409★ · Laravel + Filament |
| Agent surface | an MCP server over Academico's Eloquent models | 🟢 yours |
| Standards bridge | [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 · LTI launch into the LMS |
| Mastery model | [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🟢 MIT · BKT |
| Event sink | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · xAPI LRS |

**Wiring.**

1. Stand up Academico. Because it is **MIT**, the agent goes **in-process** — a
   Filament panel plus an `artisan` command — instead of the out-of-process
   sidecar every copyleft core forces. This is the step no other records platform
   in this sector permits.
2. Expose a read/write MCP server over the Eloquent models: enrolment, attendance,
   grades, fees. **Scope writes to an explicit allow-list**; advising agents that
   can silently change a grade are the reason institutions refuse them.
3. Launch it inside the institution's existing LMS over **Tsugi** (LTI 1.3), so
   staff meet it where they already work rather than in a second system.
4. Emit every interaction as **xAPI** into `lrsql`. This is the audit trail that
   answers "what did the agent do", and it is the artefact a procurement review
   asks for.
5. Fit **pyBKT** on the attendance + grade history so "this student is at risk"
   is a mastery estimate with a literature behind it, not a model's opinion.

**Grant check (run P556 before quoting).** Academico MIT · Tsugi Apache-2.0 ·
pyBKT MIT · lrsql Apache-2.0 → 🟢 **the union is permissive; the artefact is
shippable.** 🔴 Verify Academico's own `composer.json` tree — Filament is MIT but
the direct-dependency scan is still the engagement's control, not this base's
(`Gap 528-C`).

**Shape:** 8–10 weeks. **Region:** Global; strongest where small and medium
private institutions buy directly rather than through a ministry — **LATAM and
EMEA**.

---

## 🆕 P560 — Grounding a tutor in the institution's own lectures and standards

**The failure this avoids.** A tutor grounded in a general corpus answers
plausibly and off-syllabus, which is precisely the objection faculty raise. The
components to ground it in the institution's *own* material are permissive and
have been in this base's history for twenty passes unused.

| Role | Component | Grant |
|---|---|---|
| Source material | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 · lecture capture, 509★ |
| Source → teachable unit | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | 🟢 Apache-2.0 · 462★ · source-backed skills |
| Legacy content bridge | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 MIT · 361★ · SCORM 1.2/2004 runtime |
| Maths marking | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 Apache-2.0 · CAS-backed e-assessment |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT · spaced repetition |
| Event sink | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 |

**Wiring.**

1. Opencast already holds the lectures — most universities running it have years
   of recordings. Pull transcripts from its existing pipeline; **do not build a
   capture system**.
2. Feed transcripts plus the course PDFs through **lineage-skill**, whose output
   is *source-backed*: each generated lesson traces to the material it came from.
   That traceability is the faculty-acceptance argument, so do not substitute a
   generic summariser.
3. Mount the institution's existing SCORM packages through **scorm-again** so the
   tutor can reference and sequence content the institution already licensed.
4. For quantitative subjects, mark with **Numbas** rather than the model.
   Numbas's CAS judges mathematical *equivalence*; an LLM asked to mark algebra
   grades the string. 🔵 This is the single highest-value substitution in the
   recipe.
5. Push mastery events to **lrsql**; schedule review through
   **anki-mcp-server** so the learner keeps the deck when the engagement ends.

**Grant check.** ECL-2.0 (Apache-like, narrowed patent clause) · Apache-2.0 ·
MIT · Apache-2.0 · MIT → 🟢 permissive union. 🟡 ECL-2.0's patent clause is
narrower than Apache-2.0's — flag it in the engagement's legal review; it is not
a trap, but it is not Apache-2.0 either.

**Shape:** 10–12 weeks. **Region:** EMEA first — Opencast and Numbas are both
European-consortium/university projects with existing installed bases there.

---

## 🆕 P561 — The ledger as a billable artefact (productising `Gap 529-A`)

**The insight is `p530`'s own failure.** This base spent ~400 passes
rediscovering addresses it already held, and a **one-file index** surfaced 97
unused permissive components in a single run. A client's engineering
organisation has the same pathology in its own repos, wikis and ADRs.

| Role | Component | Grant |
|---|---|---|
| The compaction | [`../ingest/address-ledger.py`](../ingest/address-ledger.py) | 🟢 this base's |
| Grant resolution | [`../ingest/probe-grant.sh`](../ingest/probe-grant.sh) | 🟢 this base's · 159 filename variants, branch resolved |
| Knowledge tracing of *components*, not learners | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT |

**Wiring.**

1. Point the ledger at the client's own corpus. One row per artefact:
   `address · first_seen · last_verdict · filed_on · last_measured`.
2. Run `probe-grant.sh` over every address for a **grant census**. Expect what
   `p530` found: a minority permissive, a long ungranted tail, and at least one
   licence asserted in a wiki that the repository does not carry.
3. Rank by **distinct mentions without adoption**. That number is the cost of
   rediscovery, and it is the number that justifies the engagement.
4. Put the index **in front of** the process that keeps losing things, not after
   it. 🔴 `p528` named a rewrite as the cause and repaired the symptom; the debt
   recurred one pass later because the control sat downstream.

**Three defects to carry in, each of which cost this base a pass.**
🔴 Case-sensitivity: `LICENSE.txt` ≠ `LICENSE.TXT` — generate variants, never
list them. 🔴 Default branches: **15% of addresses** are not `main`/`master`
(`develop`, `dev`, `mobile`). 🔴 Search excludes forks unless the query says
`fork:true`, and forks are not lesser objects — one was an **IMS-certified**
library.

**Shape:** 3–4 weeks for a first census; the instrument is already written.
**Region:** Global. 🔵 Best sold to organisations with long-lived internal
platform estates — which in this sector means ministries and university systems.

---

## 🆕 P600 — The disconnected classroom, served end to end (LATAM rural, Africa; Global wherever connectivity is assumed away)

> 🟢 **Renumbered from `P565` to `P600` at `p548`, closing `Gap 547-H`.** This recipe
> carried the same id as *"Brightspace, the third LMS"* (above) from `p532` to `p547`, so
> every cross-reference to `P565` on this base was ambiguous. `P600` was the next free id,
> so the range stays **contiguous** (`P547`…`P600`) and the ids are now **unique**.

🔵 **The engagement this answers.** A ministry or NGO programme where the
deliverable has to work in schools with intermittent power and no reliable
uplink. Every other recipe on this page assumes a reachable model endpoint. This
one does not, and `p532` is the first pass that can name a **permissive server
side** for it.

**Components, all read first-hand this pass:**

| Component | Repo | Grant (title block) | Stars | Role in the recipe |
|---|---|---|---|---|
| Offline server + local assistant | [Crosstalk-Solutions/Project-NOMAD](https://github.com/Crosstalk-Solutions/Project-NOMAD) | 🟢 **Apache-2.0** | **41.3k** | The box. Self-contained offline knowledge/education server, ≈5 GB disk and <1 GB RAM for the server itself, terminal install on Ubuntu 26.04 / 24.04 / Debian 12, **local AI assistant included**. |
| Curriculum + learner model | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1.2k | The learner-facing half: curriculum structure, progress and offline sync — the part NOMAD does not model. |
| Content studio | [learningequality/studio](https://github.com/learningequality/studio) | 🟢 **MIT** | — | Authoring and channel packaging for the Kolibri side, so a ministry curates its own corpus rather than shipping someone else's. |
| Mastery assessment | [beltromatti/get-it](https://github.com/beltromatti/get-it) | 🟢 **Apache-2.0** | 1.1k | Turns the PDFs a school already has into concept-level mastery maps. 🟡 24-hour hackathon origin — take the architecture, rewrite the shell. |
| Spaced repetition | [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | 🟢 **MIT** | 180 | Scheduling that survives a device being offline for a week. |

**Wiring.**
1. **NOMAD is the deployment unit**, one per school: it already bundles content
   serving plus a local model, so the AI tier has no egress dependency.
2. **Kolibri runs beside it on the same box** and owns the learner model and
   curriculum tree; NOMAD owns the corpus, the tooling and the assistant. Neither
   project duplicates the other's half, which is why the pairing is clean.
3. **`get-it`'s mastery decomposition runs against the school's own PDFs**, with
   the local model as its engine instead of an account-based CLI.
4. **`fsrs.js` schedules review** entirely on-device; nothing in the loop needs a
   round trip.
5. **Sync is Kolibri's**, opportunistic — when an uplink appears, progress leaves
   and curated channels arrive. Treat connectivity as an event, never a
   precondition.

🔴 **The licence reading that makes this shippable.** Apache-2.0 + MIT
throughout, so a studio can ship proprietary extensions on top. 🔵 Contrast the
LMS cores in [`../verticals/solutions.md`](../verticals/solutions.md), which are
almost entirely AGPL/GPL — **the permissive surface in this sector is the
integration and delivery layer, not the platforms**, and that is exactly the
surface this recipe is built on.

**Shape:** 8–10 weeks to a pilot on real hardware; the long pole is **content
curation and teacher training**, not code. 🔴 Budget hardware per school and say
so in the proposal — this is the one recipe on this page with a unit cost.
**Region:** LATAM rural and Africa first; applicable anywhere a client's
connectivity assumption is weaker than the demo's.

---

## 🆕 P566 — One agent, four LMS platforms (Global; North America and EMEA first)

🔵 **The engagement this answers.** A university system or district running
**more than one** LMS — which is the normal case after any merger, federation or
decade of procurement — that wants one assistant across all of them rather than
four integrations.

🟢 **`p532` is the first pass where this recipe is possible**, because the
Blackboard bridge was the missing fourth and it had been sitting in this base's
own history, MIT-licensed, described in eight passes and filed in none.

| Platform | Bridge | Grant (title block) | Stars |
|---|---|---|---|
| **Canvas** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | 308 |
| **Blackboard Learn** | 🆕 [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 **MIT** | 2 |
| **Brightspace (D2L)** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **MIT** | 60 |
| **Moodle** | 🆕 [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **MIT** | 1 |

**Wiring.**
1. **Normalise at the tool boundary, not in the agent.** The four servers do not
   share a tool vocabulary — `p528` measured that across the Moodle field alone —
   so define one internal verb set (`list_courses`, `get_roster`,
   `post_announcement`, `read_submissions`, `write_grade`) and adapt each bridge
   to it. This is the actual deliverable; the bridges are upstream.
2. **Run each bridge as its own process** behind that façade, so a platform
   outage degrades one tenant rather than the assistant.
3. **Keep writes behind an approval step.** Grades and placement are exactly what
   NYC's red tier and the EU AI Act's high-risk list cover — see **P548** and the
   `p532` regional table in [`../intel/market.md`](../intel/market.md). Reads can
   be direct; writes are proposals a human confirms.
4. **Adopt `bb-mcp`'s own argument deliberately:** *"the integration logic lives
   here, not in the client."* One façade, many clients.

🔴 **State the maturity honestly in the proposal.** Two of the four bridges are
**1★ and 2★**. These are *correct starting points with a permissive grant*, not
adopted dependencies — the studio **forks and owns** them, and prices that in.
🟢 What the permissive grant buys is the right to do exactly that: `p529`'s
census found the Moodle MCP field's most-visible option is **AGPL-3.0** and its
**52★ ceiling is ungranted**, so forking an MIT 1★ server beats depending on a
copyleft 52★ one.

**Shape:** 6–8 weeks for two platforms, +2 per additional platform once the
façade exists. **Region:** Global; North America and EMEA first, where
multi-LMS estates and Blackboard/Brightspace share are concentrated.

---

## 🆕 P571 — The efficacy trial, as a shippable component (North America first; EMEA, LATAM)

**Brief.** A client has, or wants, an AI tutor, and the question that will decide renewal
is no longer "does it work?" but **"can you show it caused learning?"** This pattern
produces a defensible effect estimate as a **deliverable of the build**, not a study
bolted on afterwards.

🔵 **Why it is separate from [`P552`](#p552--pedagogy-evaluation-harness-the-differentiator),
which it depends on.** P552 answers *does this model know how to teach* — construct
validity, model selection, a CI gate on teaching quality. **P571 answers a different
question**: *did this deployment change outcomes for these students, against a
counterfactual.* A buyer can accept P552's benchmark scores and still have nothing to
show a ministry, a school board or a funder. Run P552 at model-selection time; run P571
around the deployment.

**The demand signal this is built for.** A coalition reported as **140+ organisations**
asked US federal funders on **2026-10-15** to fund exactly this kind of research, on the
back of a review reported to find only ~**20 of 800+** K-12 AI studies carrying strong
causal evidence ([`../intel/trends.md`](../intel/trends.md) Trend 21). 🔴 Single-channel
claim — but the *direction* is corroborated by HolonIQ (systems expecting evidence of
improved learning) and 1EdTech (institutions standing up evaluation processes).

| Role | Component | Licence |
|---|---|---|
| LMS of record (**not forked**) — cohorts, sections, gradebook | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 · 6.9k★ |
| Assignment + roster seam | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** · 308★ |
| The intervention (tutor under test) | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) · v1.7.0 (2026.10.28) | **Apache-2.0** · 49.7k★ |
| Mastery ground truth (BKT) | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** · 274★ |
| Retention outcome, principled | [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** · 519★ |
| Longitudinal event capture (xAPI LRS) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** · 51★ |
| Agent-version provenance for every event | 🆕 [comet-ml/opik](https://github.com/comet-ml/opik) | **Apache-2.0** · 23.0k★ |
| Causal assumptions, stated and refuted | 🆕 [py-why/dowhy](https://github.com/py-why/dowhy) | **MIT** · 8.4k★ |
| Heterogeneous effects — *who* it helped | 🆕 [py-why/EconML](https://github.com/py-why/EconML) | **MIT** · 4.8k★ |
| Teaching-quality gate, upstream | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** · 13★ |

**Wiring, in the order it has to happen.**

1. **Pre-register the primary outcome before any code ships.** One outcome, named, with
   its measurement window — e.g. *mastery on the OATutor BKT skill model at 30 days*,
   not "engagement". 🔴 Everything after this step is cheap; this step is what separates
   the 20 credible studies from the 780.
2. **Assign at the level the institution already groups by** — Canvas **sections**, read
   through `canvas-mcp`. Cluster assignment by section, not by student, because students
   talk to each other and contaminate a student-level control arm. The control arm is
   business-as-usual teaching, **not** a degraded tutor.
3. **Stamp every event with the agent version.** `opik` traces model, prompt and
   retrieval version; that id travels into each xAPI statement written to `ralph`. 🔵
   Without this, a mid-trial prompt change silently makes the two arms three arms, and
   the estimate is unrecoverable.
4. **Capture outcomes through `ralph`** for both arms, from the LMS and the tutor alike,
   so the control arm is measured by the same instrument as the treatment arm.
5. **Estimate with `dowhy` first, not last.** State the graph — assignment, prior
   attainment, teacher, section size — and run its **refutation tests** (placebo
   treatment, random common cause). A model that fails them is reported as failing them.
6. **Then `EconML` for the heterogeneous effect**, pre-specifying the subgroup that
   matters: prior-attainment quartile. 🟢 **This is usually where the finding is.** A
   null average with a real gain in the bottom quartile is the result that renews a
   contract, and an average-only analysis throws it away.
7. **Hand over the estimation code with the model.** Both libraries are MIT, so the
   client can re-run and audit the claim themselves — which is the difference between
   evidence and a vendor assertion.

🔴 **The licence boundary is unchanged and still decides the architecture.** Canvas stays
AGPL-3.0 and **unforked**; the tutor, the LRS and the whole estimation stack are
permissive and out-of-process, talking over MCP, LTI 1.3 and xAPI. Nothing in this
pattern links copyleft code in-process.

🔴 **State the honest limits in the proposal, because a buyer who asks for causal
evidence will ask these.** A single-institution cluster trial has few clusters and wide
intervals; it will rarely produce a statistically significant average effect in one term.
🟢 **Sell it as what it is**: a pre-registered design, an auditable pipeline and an
honest interval — which is already more than the field's 780 non-credible studies offer,
and it compounds across terms.

**Regional fit.**
- **North America** — the live demand. Federal research funding is being actively lobbied
  for, **134 AI-education bills across 31 states**, and four states now mandate
  district-level AI policy; a district that must adopt a written policy needs evidence to
  write it against.
- **EMEA** — the compliance fit. The EU AI Act makes education **assessment** high-risk,
  and an effect estimate with stated assumptions is the natural evidence artefact for
  that file. 🔵 And the opening is teacher-side: **29.7%** of EU teachers have had any AI
  CPD and **53%** have had none and report no strong need for it, so the trial's control
  arm is genuinely business-as-usual.
- **LATAM** — the governance gap as the sale. UNESCO IESALC: **87%** of surveyed
  institutions use AI, **26%** have a formal strategy. An institution with no strategy
  and a deployment in flight is one that can be sold the measurement *first*.

**Shape:** 3–4 weeks to stand up the pipeline if P552 already exists, then one academic
term for the trial window. **Region:** North America first; EMEA where the AI Act file
needs an evidence artefact; LATAM where the governance gap is the opening.

## 🆕 P576 — The Moodle bridge, built by consolidating three **MIT** servers and *reading* the ungranted leader (Global; supersedes the sizing in `P553`/`P558`)

**Who this is for.** Any engagement on Moodle — the sector's largest install
base — that needs an agent to do more than read.

🔴 **Why this supersedes the earlier sizing.** `P553` and `P558` were scoped
against a census that said the Moodle MCP field *"sums to under 40 stars"* with
*"nobody above 27★"*. `p538` re-read the field first-hand and those figures are
wrong; [`../repos/foundations.md`](../repos/foundations.md) had already said so
at `p529`. The field is larger, and **its leader is unusable**, which changes
what you consolidate.

**The three components, all MIT, so they compose with no licence question:**

| Take from | Address | Stars | Take exactly this |
|---|---|---|---|
| **Widest surface** | [`GhaithAlHallak8/moodler-mcp`](https://github.com/GhaithAlHallak8/moodler-mcp) | 3 · 1 fork | The **40-tool** vocabulary (32 read / 8 write) and its two-flag write gate — writes off by default behind `MOODLER_ALLOW_STUDENT_WRITES` and a second flag, with `confirm=true` |
| **The write loop** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **45** · 14 forks | The **teacher-side grading path** — `get_student_submissions` → `provide_assignment_feedback`, and `get_quiz_attempts` → `provide_quiz_feedback`. This is the only one of the four that ships the feedback write as a first-class tool |
| **Runtime discipline** | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | 27 · 1 fork | **Rust on the official MCP SDK**, 20 typed tools plus 2 opt-in escape hatches gated by `MOODLE_ENABLE_WS_FUNCTION`, and its tested Moodle version matrix |

🔴 **Read, do not copy:**
[`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) — **52★, 14 forks,
24 tools in four documented groups (courses & content · assignments & deadlines
· grades & progress · aggregated overviews)**. It is the **most-starred bridge
in the field and has the best-organised tool taxonomy**, and it carries **no
grant at all** — no licence entry in its sidebar, none in its title block.
⛔ **Default copyright applies. Do not vendor it, do not copy its code, do not
lift its source.** 🟢 **What you may take is the *design*: the four-group
grouping is the clearest read of what a Moodle agent surface needs, and a
taxonomy is not copyrightable expression.** Re-derive the tools from Moodle's
own Web Services API against that grouping.

**Wiring.**

1. Start from `moodler-mcp` (MIT). It has the widest surface and the safest write posture already.
2. Re-group its 40 tools into `loyaniu`'s four categories. Taxonomy only — no code.
3. Port `peancor`'s two feedback writes as first-class tools inside `moodler-mcp`'s existing gate. They are the two the other three lack.
4. Adopt `G36maid`'s version matrix as the test matrix. It is the only one in the field that publishes which Moodle releases it is tested against.
5. Put the whole thing behind [`oas114/EduShield`](https://github.com/oas114/EduShield) (MIT) when student free text crosses to a model — see **P577**.
6. Grade it with the rubrics in [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (**87★**; 🔵 code MIT, rubrics CC BY 4.0 — attribute, do not relicense).

**Effort.** 5–7 weeks to a write-capable bridge on the merged vocabulary, versus
the 8–10 weeks `P553` assumed for a greenfield build — the saving is entirely
`moodler-mcp`'s existing 40 tools and gate.

⚠️ **Scope honesty:** four of eleven codebases in the census were re-read this
pass. Seven carry figures no pass has re-attested (`Gap 538-B`), and **every tool
count in this field is the repository's own claim** — three of them contradict
themselves on it. Treat tool counts as marketing.

## 🆕 P577 — The zero-infrastructure PII shield, for a school with no IT department (Global; APAC and LATAM first)

**Who this is for.** Any K-12 engagement where the customer has no server, no
IT staff, and student free text that must reach a model anyway. This is the
common case in LATAM *secretarias* and across APAC, and this base's
data-protection patterns have all assumed a service to deploy.

**The component.** [`oas114/EduShield`](https://github.com/oas114/EduShield) —
教育隱私保護系統, **MIT**, 11★, Taiwan. De-identifies text **before** it reaches
a model, replacing personal data with placeholder codes, then restores the
original values in the output. 🟢 **It is 單一靜態 HTML 檔案 — one static HTML
file, no backend, no install** — with an optional local scan through **Ollama**
for anything the pattern rules miss.

**Why this is a pattern and not just a dependency.** 🔵 **The deployment story
is the product.** Every other anonymisation option on this base
([`microsoft/presidio`](https://github.com/microsoft/presidio) and the vault
contracts in `P572`) requires something to run and someone to run it. **A single
HTML file is deployable by emailing it.** That removes the one blocker that kills
these engagements before procurement: there is nobody on the customer's side to
operate a service.

**Wiring.**

1. Fork `EduShield` (MIT — clean). Replace its pattern rules with the jurisdiction's categories: **FERPA's 7 / COPPA's 10** from [`pii-student-vault-contract-profile`](https://github.com/mizcausevic-dev/pii-student-vault-contract-profile) for the US, **LGPD** categories for Brazil, **PDPA** for Taiwan and Singapore.
2. Keep the Ollama path and ship a model with it for the offline case. This is what makes it defensible rather than regex theatre.
3. For an institution that *does* have infrastructure, run the same category list through `presidio` server-side and keep the HTML file as the fallback — one category definition, two deployments.
4. Log every model read through [`student-data-access-audit-stream`](https://github.com/mizcausevic-dev/student-data-access-audit-stream) (MIT) when the jurisdiction is the US: its hash-chained schema enforces tokenised student IDs and **FERPA §99.32** consistency.

**Effort.** 2–3 weeks per jurisdiction for the category rules and the offline
model, on top of a 1-week fork.

⚠️ **What this is not.** `EduShield` is 11★ and `student-data-access-audit-stream`
is 0★ at v0.1; both state they are scaffolding rather than certification.
🔵 **The engagement's deliverable is the category mapping and the evidence
trail, which is billable work; the repositories are the starting shape.**

## 🆕 P578 — Curriculum-grounded tutoring where the national corpus is downloadable (APAC first — China; the method is portable)

**Who this is for.** A ministry or publisher engagement in a jurisdiction that
publishes its curriculum on a national platform. China's compulsory AI-from-age-six
policy makes this concrete now; India's Class 3 target and Brazil's BNCC make the
method portable.

**The gap this closes.** Every tutoring pattern on this base says "ground it in
the curriculum" and none says **how you get the curriculum**. 🟢 `p538` filed the
answer for one jurisdiction.

| Layer | Component | Grant | Role |
|---|---|---|---|
| **Corpus acquisition** | [`alterem/knowledge-grab`](https://github.com/alterem/knowledge-grab) | 🟢 **MIT**, **567★** · 52 forks | Pulls e-textbooks, course video and courseware from 国家中小学智慧教育平台 (`basic.smartedu.cn`) — the PRC national K-12 platform. Decrypts video, merges to MP4 via ffmpeg. Tauri + Vue 3 |
| **Video → text** | [`LeoLiu363/ai-video-understanding`](https://github.com/LeoLiu363/ai-video-understanding) | ⛔ **Ungranted** — read for method only | Local transcription + courseware OCR with timestamped Q&A. The *approach* is what you take |
| **Curriculum-code grounding** | [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional) | 🟢 **MIT**, 0★ | The cleanest reference on this base for grounding an agent in a *national* curriculum: BNCC code identification, page-level citations, **Self-RAG** hallucination check, LangGraph + ChromaDB + `bge-m3` + Ollama, **Giskard** evaluation |
| **Citation + policy architecture** | [`upstream1119/Traceable-Ideological-Education-RAG`](https://github.com/upstream1119/Traceable-Ideological-Education-RAG) | ⛔ **Ungranted** — read for architecture only | The only artefact here treating **citation grounding and a policy check as first-class components** rather than as prompt text. Essential shape where curriculum content is itself regulated |
| **Tutor runtime** | [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) | 🟢 **MIT**, 41★ | A local-first adaptive-tutoring **foundation** that already ships a worked vertical (civil-service exam: practice, grading, review, planning) |
| **Mastery scheduling** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, **59★** · 9 forks | **Bayesian Knowledge Tracing + FSRS** as an MCP server, so the "what next" decision is a tool call rather than prompt logic |

**Wiring.** `knowledge-grab` fills a corpus store → transcribe and OCR locally
(method from `ai-video-understanding`, **implemented fresh — it is ungranted**)
→ index with `Agente-Educacional`'s BNCC-style scheme, swapping BNCC codes for
the target jurisdiction's curriculum codes → serve retrieval with its
page-level citations and Self-RAG check → architect citation and policy checks
as separate components per `Traceable-Ideological-Education-RAG`'s shape,
**written from scratch** → run the tutor on `civil-ai`'s foundation → delegate
mastery to `tutor-mcp` over MCP → evaluate with Giskard, as
`Agente-Educacional` already does.

🔴 **The licence line that decides this build.** Two of the six components are
**ungranted** and are present as *architecture*, not code. The four you may
build on — `knowledge-grab`, `Agente-Educacional`, `civil-ai`, `tutor-mcp` — are
all **MIT**, so the buildable path is clean end to end.

⚠️ **The unresolved question, and it is legal rather than technical.**
`knowledge-grab`'s MIT grant covers **the tool**. The **content** on
`basic.smartedu.cn` carries the platform's own terms, which this base **has not
read**. 🔴 **For a commercial deployment that is the whole question, and it must
be answered by counsel in-jurisdiction before the corpus is built** — not by a
star count or a repository licence. Stated plainly because the technical path is
easy enough to make the legal one easy to skip.

**Effort.** 4–6 weeks to a grounded tutor over one subject and one grade band,
assuming the corpus question is already answered. **Indefinite if it is not.**

## P579 — The auditable tutor: an AI tutor whose every interaction lands in a standards-compliant learner record (EMEA first; Global)

**Brief.** An institution wants a tutor it can put in front of a regulator. The
pedagogy is the easy half — this base has had a tutoring shelf for hundreds of
passes. 🔴 **The half that has been missing on every live shelf until this pass
is the record:** an interaction that exists only in a chat log is not evidence,
and EU **Annex III** attaches to systems influencing access to qualifications.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Record layer | 🆕 [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** · 16★ · 4 forks | *"Enables AI agents to **record and retrieve** learning activities through xAPI-compliant Learning Record Stores."* 🟢 **The only artefact on this base that writes learner activity back to a standards store** rather than only reading from one. Python, MCP server |
| The store | **Ralph LRS**, named in `learnmcp-xapi`'s own README | per-project | 🟢 **Self-hostable and EMEA-domiciled** — by **France Université Numérique**. Processing stays in the institution, which moves the hardest conformity question off the table |
| Mastery estimate | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** · 57★ | Bayesian Knowledge Tracing over MCP — a **numeric, inspectable** mastery state, not a model's opinion. Go |
| Tutor surface | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · 50.0k★ · 6.2k forks | The shelf's most-starred tutor; re-read this pass |
| Policy gate | 🆕 [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** · 6.5k★ · 1.1k forks | Every tool call checked against policy before it runs, plus agent identity, sandboxed execution and **audit records**. Covers the OWASP Agentic Top 10. 🔴 **Public preview, and education is nowhere on its page** — it is general infrastructure used here for a specific purpose |
| Pedagogical eval | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | Conformity asks whether the system is *accurate*, not only whether it is logged |

**Wiring, concretely.** Mount `learnmcp-xapi` and `tutor-mcp` as two MCP servers
behind the governance toolkit's policy engine — the toolkit sits between the
tutor and both servers, so no statement reaches the LRS and no mastery write
happens without passing policy first. The tutor graph's turn loop becomes:
read mastery from `tutor-mcp` → generate → **emit an xAPI statement through
`learnmcp-xapi` before replying** → update mastery. 🔵 **Emit before replying,
not after**, or a crash loses exactly the interaction a regulator would ask
about. Point `learnmcp-xapi` at a self-hosted Ralph instance inside the
institution's boundary; the toolkit's audit log is the second, independent
record and the two should be reconcilable by statement id.

🔴 **The honest weaknesses.** `learnmcp-xapi` is **16★ with 32 commits** — this
is a thin component carrying a load-bearing role, so budget to own it. The
governance toolkit is a **public preview**. And xAPI statement *design* is the
real work: a badly modelled verb vocabulary produces an audit trail nobody can
query. 🟢 **Pair with 1EdTech's Caliper vocabulary** rather than inventing verbs.

**Shape of the engagement.** 8–10 weeks: 2 for statement/verb modelling against
the institution's own assessment language, 2 for the Ralph deployment and policy
rules, 3 for the tutor and mastery integration, 2 for the conformity pack
(Annex III documentation, audit queries, eval results). 🟢 **The deliverable a
client actually buys is the conformity pack** — the tutor is the demo.

## P580 — The national-curriculum engagement: start from the state's own ontology, not from a scrape (EMEA — England; the shape is portable)

**Brief.** A ministry, academy trust or publisher wants AI lesson preparation and
assessment aligned to the national curriculum. The default build scrapes
curriculum text into a vector store and hopes. 🟢 **In England that is now
unnecessary and strictly worse:** the curriculum is published as data, with an
API, an SDK **and an MCP server**, by a state-funded body.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Curriculum ontology + MCP | 🆕 [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT** (`LICENCE` at `main`) · 8★ · **6 835 commits** | *"Tools for working with the Oak Open Curriculum Data, via API, SDK and MCP app."* **Oak National Academy** + **Education Endowment Foundation**, against the **National Curriculum for England (2014)**. Topics include `mcp-server`, `openapi`, `elasticsearch` |
| Curriculum graph | [oaknational/oak-curriculum-ontology](https://github.com/oaknational/oak-curriculum-ontology) | 🟢 **MIT** (`LICENSE.md` at `main`) | The ontology behind the data. 🔴 **Grant attested by bulk gate this pass; stars not read** |
| Lesson drafting | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** · 63★ | Local-first, works from the teacher's own curriculum files — point it at Oak data instead of a scrape. 🔴 Explicitly **single-teacher, not multi-tenant** |
| Provenance-bearing skills | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | 🟢 **Apache-2.0** · 462★ | Emits **source-backed** teacher skills — the citation back to the curriculum unit is the audit trail an inspector wants |
| Assessment | [inducer/relate](https://github.com/inducer/relate) | 🟡 **MIT by README text only** — sidebar names no grant | Course content as **YAML + Markdown under git**, so a curriculum change is a reviewable commit and a diff. 437★ · 125 forks |
| Agent conventions | 🆕 [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | 🟢 **MIT** · 27★ · **19 739 commits** | 🔵 **Read, do not deploy.** It ships `AGENTS.md`, `CLAUDE.md` and *"Guidance for AI coding agents"* — this is how the **Department for Education** expects agents to behave in its codebases, which is what a public-sector review will measure you against |

**Wiring, concretely.** Mount Oak's MCP server as the single source of
curriculum truth; forbid the drafting agent from retrieving curriculum text from
anywhere else, so every generated lesson carries an Oak unit identifier. Run
`lineage-skill` over the institution's own materials to produce skills whose
claims cite those identifiers. Hold the resulting lesson and assessment content
in `relate`'s git-backed YAML, which gives the trust a reviewable history per
curriculum change. 🟢 **The Oak identifier is the join key across the whole
pattern** — drafting, assessment and reporting all key on it, which is what makes
the output checkable by a person who never saw the model.

🔴 **Weaknesses.** Oak's ecosystem repo is **8★** — mature by commits, tiny by
community, so it is a dependency to watch. `Claw-ED` is single-tenant by design,
so a trust-wide rollout needs an orchestration layer the pattern does not supply.
`relate`'s grant is **README text with no sidebar licence** — get written
confirmation before a commercial deployment. 🟡 **And the portability claim is
untested:** the shape (national curriculum published as queryable data) is
replicable in principle, but England is the only region where this base has found
it shipped.

**Shape of the engagement.** 6–8 weeks for a single-subject pilot; 12–14 for
trust-wide, where most of the added time is multi-tenancy and SSO rather than AI.

## P581 — Course outcome to labour-market credential: the skills layer every 2026 trend list asks for (EMEA/EU first)

**Brief.** An institution or ministry wants to show that what it teaches maps to
what employers hire for, and to issue a credential a third party can verify.
🟢 **Both halves now exist permissively and this base had neither on a shelf
before this pass.**

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Skills extraction | 🆕 [KonstantinosPetrakis/esco-skill-extractor](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 **MIT** · 32★ · 13 forks | *"Extract **ESCO** skills and **ISCO** occupations from texts such as job descriptions or CVs."* Embeddings + sentence-transformer + cosine similarity. Built in the **SKILLAB EU Horizon** project |
| The taxonomy | **ESCO** — European Skills, Competences, Qualifications and Occupations | EU-published | 🟢 **The external referent.** A skill code is checkable by an employer, a ministry and a regulator independently |
| Credential wallet | [digitalcredentials/learner-credential-wallet](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 **MIT** (`LICENSE` at `main`) | Verifiable credentials in a learner-held wallet. 🔴 Grant attested by bulk gate; stars not read this pass |
| Standards validator | [1EdTech/digital-credentials-public-validator](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** | Validate before you issue. 🔴 Grant attested by bulk gate; stars not read |
| Records substrate | [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) (NA) or the LRS from **P579** (EMEA) | 🟢 Apache-2.0 / MIT | Where the achievement actually lives before it becomes a credential |

**Wiring, concretely.** Run the extractor over two corpora, not one: the
institution's **course and module descriptions**, and a sample of **live job
postings** in its region. The intersection is the alignment report; the
difference in both directions is the finding a client pays for — taught skills no
employer asks for, and demanded skills nobody teaches. Then, for a completed
learner outcome, issue a verifiable credential carrying the ESCO codes, validate
it against 1EdTech's validator **before** issuance, and hold the underlying
achievement in Ed-Fi or the LRS.

🔵 **Why the two-corpus design matters.** A one-corpus run produces a taxonomy
mapping, which is a deliverable nobody can act on. The two-corpus run produces a
*gap list* with a curriculum change attached to each row.

🔴 **Weaknesses, plainly.** The extractor is **32★** and its README does not even
define ESCO — budget to read its embedding approach properly before trusting a
match. ESCO is **European**: the pattern does not transfer to North America
without swapping in O*NET, which this base has not filed. And two of the five
components are **gate-attested only**, so read their pages before committing.

**Shape of the engagement.** 4 weeks for the alignment report alone (the sellable
first slice), 10–12 for issuance end to end.

## P582 — Classroom capture to courseware: the APAC seam, using the largest permissive education codebase on this base (APAC first)

**Brief.** An institution runs live online classes and wants them to become
reusable, searchable courseware rather than a folder of recordings.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Classroom + capture | 🆕 [netless-io/flat](https://github.com/netless-io/flat) | 🟢 **MIT** · **6 400★** · 876 forks | Agora Flat's open-source classroom: interactive whiteboard, Electron desktop clients, and 🟢 **cloud recording** — the capture step most patterns assume and none supplied |
| Video → courseware | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | 🟢 **Apache-2.0** · 462★ | *"Distill videos, PDFs, transcripts and notes into **source-backed** teacher Agent Skills"* — built for exactly this input |
| Ingest fallback | [LeoLiu363/ai-video-understanding](https://github.com/LeoLiu363/ai-video-understanding) | ⛔ **Ungranted** | Local transcription + courseware OCR with timestamped Q&A. 🔴 **No licence file — read it, do not ship it** |
| Tutor over the result | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** · 50.0k★ | Serves the distilled material back as lifelong personalised tutoring |
| Record | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** · 16★ | So the replay is attributable per learner, per **P579** |

**Wiring, concretely.** Flat's cloud-recording artefact plus its whiteboard
stream are the ingest payload: pass both to `lineage-skill`, which emits skills
whose claims cite the timestamp they came from. That citation is the whole value —
a student asking "where did this come from?" gets a minute marker in the lesson
they attended.

🔴 **The commercial dependency is the thing to price first.** Flat's MIT grant
covers the **client**; the real-time transport is **Agora's commercial SDK**. So
this pattern has a per-minute cost that none of the others do, and it must be in
the first conversation, not the last. 🔴 **And China's framework imposes
mandatory registration and content-labelling obligations** on a deployed system —
a generated lesson is generated content.

**Shape of the engagement.** 6–8 weeks, of which 2 are Agora commercials and
regional compliance rather than engineering.


## P583 — The efficacy audit: prove the AI a LATAM institution already bought actually worked (LATAM first; the shape is global)

**Brief.** UNESCO IESALC surveyed 200 higher-education institutions across 19
countries in Latin America and the Caribbean: **87 %** use AI somewhere, **74 %**
in teaching and learning, **26 %** hold a formal AI strategy, and 🔴 **9 %
evaluate what their AI use delivers.** 🔵 **Ninety-one percent of institutions
that already spent the money cannot say whether it worked** — and unlike an
adoption pitch, that buyer has a budget line to defend to a rector, a ministry
or an accreditor. This recipe does not deploy AI. It **measures AI that is
already deployed**, which is the engagement the region's numbers actually
describe.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| Learner-record feed | [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | 🟢 Apache-2.0 | Forwards and filters xAPI statements **governed by a declared xAPI Profile**, so the measurement has a schema an auditor can read rather than ad-hoc ETL. 17★ · 9 forks — small, and the Profile governance is why it is here |
| Statement source | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT | Already on this base's agent shelf. It is the piece that makes an agent's tutoring **write back** to a Learning Record Store instead of evaporating into a chat log — without it there is nothing to audit |
| LMS extraction | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 MIT | Grades, enrolments and course structure out of Canvas across the API boundary. Canvas is AGPL-3.0; **do not fork it**. 🟡 Default branch is `develop` — pin it, not `main` |
| Experiment harness | [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 BSD-3-Clause | Configuration-driven ML experiments from **Educational Testing Service** — the organisation behind TOEFL and the GRE. The provenance is the point: a rector will accept a method from ETS that they will not accept from a consultancy's notebook |
| Causal estimator | the causal-inference layer filed at `p535` | 🟢 permissive | Adoption is self-selected, so a raw before/after comparison measures who opted in. This is the layer that makes the answer a finding rather than a correlation |
| Institutional corpus | [`dspace/dspace`](https://github.com/dspace/dspace) | 🟢 BSD-3-Clause | Where theses, datasets and OER already live. **1.1k★ · 1.5k forks — f/★ 1.364**, the strongest institutional-deployment signal this base has measured, which means the client very likely already runs one |

**How it wires together.** `canvasapi` pulls the pre-period and post-period
gradebook and enrolment data; `learnmcp-xapi` supplies interaction-level
statements for whatever agent is already in use; `xapipe` normalises both into
one Profile-governed stream; `skll` runs the specification as a configuration
file so the whole analysis is a reviewable artefact rather than a notebook; the
`p535` estimator corrects for self-selection into AI use. Output is one
document: *what changed, for whom, by how much, and with what confidence.*

**Why it is sellable here specifically.** 🟢 Counterparts now have names. The
**Observatory on Artificial Intelligence in Education for Latin America and the
Caribbean** launched **14 April 2026**, UNESCO-led with **CAF**, **CENIA**
(Chile), **Cetic.br** (Brazil), **ECLAC**, **Fundación Ceibal** (Uruguay),
**Fundación Santillana**, **Tecnológico de Monterrey**, **ProFuturo**,
**Universidad del Desarrollo** and **IRCAI**. An efficacy method published
through that network is worth more than the same method sold institution by
institution.

🔴 **Where it breaks.** If the institution has no LRS and no interaction
logging, there is no pre-period and the first engagement is instrumentation,
not measurement — say so in week one rather than discovering it in week four.
🔴 And `xapipe` is a 17-star project: read it before depending on it, and be
ready to carry it.

**Shape of the engagement.** 8–10 weeks. Weeks 1–2 instrumentation audit,
3–5 extraction and normalisation, 6–8 estimation, 9–10 the document and its
defence. 🔵 It converts a sunk cost into a renewal argument, which is why it
sells to a buyer who will not fund another pilot.

## P584 — Policy conformance over an existing LMS: proving a district's AI rules are being followed (North America first)

**Brief.** The 2026 US state legislative session produced **134 AI-in-education
bills across 31 states**. Maryland gives all 24 districts **120 days from MSDE
guidance** to adopt aligned policies; Oklahoma requires a written district AI
policy before the 2027-28 school year and — 🟡 per a secondary source this pass
could not confirm against the enrolled text — bars AI from being **the primary
basis for grading, discipline, placement or other high-stakes decisions**. 🔵
**Districts now have policies and no way to demonstrate compliance with them.**
That is the product: not a tutor, an evidence trail.

| Layer | Component | Grant | Why this one |
|---|---|---|---|
| LMS reader | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 MIT | Reads gradebook changes, enrolment and course structure across the API boundary — no AGPL inheritance from the Canvas core |
| LTI attachment | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT | 138★ · 84 forks. The LTI 1.3 Advantage route into an LMS the district will not let you fork. 🟡 A same-named `ucfopen/pylti1.3` exists at 3★ with an identical description and **neither declares a fork** — pin the owner, not the name |
| Event stream | [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) | 🟢 Apache-2.0 | Profile-governed forwarding, so "an AI touched this grade" is a typed statement rather than a log line |
| Agent loop | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 Apache-2.0 | 30.1k★ · 3.2k forks, **f/★ 0.106 — a dependency, not a fork**. Reach for it rather than a full framework when the task is one classification per event |
| Compute substrate | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause | 8.4k★ · 2.1k forks, **f/★ 0.250 — run your own copy, budget the fork.** The standard way a district gives staff isolated, resourced analysis environments |

**How it wires together.** The LTI 1.3 tool registers once per district tenant;
`canvasapi` polls grade and enrolment changes; each change becomes an xAPI
statement through `xapipe` tagged with whether an AI system contributed and in
what role; a `smolagents` loop classifies each statement against the district's
written policy clauses; the output is a per-course, per-term conformance report
an administrator can hand to a board. 🔵 **The deliverable is the report, and
the report is what the statute created demand for.**

🔵 **Reuse the second surface while you are there.** The **ADA
web-accessibility update** landed for large public institutions in April 2026
and is the compliance surface AI demonstrably helps with — captioning, alt
text, reading-level adjustment — over the same content inventory this pipeline
already enumerates. Scoping both together roughly halves the second one.

🔴 **Where it breaks.** The policy clauses are prose, and a classifier over
prose will disagree with a human reader at the margin. **Ship it as evidence
for a human decision, never as the decision** — which is also what Oklahoma's
provision requires, so the architectural constraint and the legal one point the
same way. 🔴 And verify the Oklahoma status against the legislature's own
record before putting it in a proposal; this base has a conflict on it between
two secondary sources.

**Shape of the engagement.** 6–8 weeks for one district tenant, of which week 1
is reading the district's actual policy text. 🔴 **It does not generalise across
districts for free** — the clause set is local, so build the classifier's rule
set as configuration from day one.

## P585 — The accessible-courseware retrofit: make an existing LMS's material usable by disabled students (LATAM first; the shape is global)

🔵 **Why this pattern and not another.** Every delivery pattern on this base
assumes a student who can read the screen. `p541` filed the first artefact
that does not —
[`UFPA-LAMIC/EduAcess`](https://github.com/UFPA-LAMIC/EduAcess), **MIT**
(1,144 B, read first-hand), from a Brazilian federal university lab — and
accessibility is a **procurement requirement** in most public education
systems rather than a nice-to-have, which makes it a funded engagement rather
than a pilot.

**The stack, with grants read first-hand:**

| Role | Component | Grant | Why this one |
|---|---|---|---|
| Material adapter | [`UFPA-LAMIC/EduAcess`](https://github.com/UFPA-LAMIC/EduAcess) | 🟢 **MIT** (1,144 B) | Converts course PDFs to **narrated audio** and text optimised for visual impairment, ADHD, autism and dyslexia. **AI plus regex heuristics**, so it degrades predictably rather than hallucinating |
| Course system of record | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | The LMS the material already lives in. Adapter runs **beside** it over web services, never vendored in — the GPL boundary is the integration seam |
| Delivery of adapted assets | [`openedx/XBlock`](https://github.com/openedx/XBlock) *or* Moodle's own file API | 🟢 Apache-2.0 / 🔴 GPL-3.0 | Serve the adapted artefact next to the original so the student picks |
| Local inference | `ollama` | 🟢 MIT | The adaptation runs on institution hardware: student material with disability metadata is the most sensitive data in the building |

**How to wire it, in the order that de-risks fastest:**

1. **Start from one course, not the catalogue.** Export its PDFs via Moodle web
   services. Run `EduAcess` over them. Put the audio and optimised text beside
   the originals as additional resources.
2. **Measure adaptation quality by hand on 20 documents before automating
   anything.** The regex half is deterministic and auditable; the model half is
   not. Separate the two in reporting so the institution can see which is which.
3. **Only then add the agent layer.** A tutoring agent over adapted material is
   a second phase, and `P579`'s learner-record wiring is where it belongs.

🔴 **What will go wrong.** `EduAcess` carries **0 stars and 14 commits** — it
is a working university prototype, not a maintained product. Treat it as **the
reference implementation to harden**, budget for taking over maintenance, and
read [`../agents/top.md`](../agents/top.md#-p541--four-agents-off-the-spanish-and-portuguese-legs-and-what-the-language-of-a-query-costs)
before quoting it to a client.

🟢 **Why it is still the right starting point:** nothing else on this base
does this job at all, the grant is clean MIT, and the accessibility
requirement it addresses is already written into the buyer's procurement rules.

## P586 — The teacher skill pack on an LMS the institution already runs (EMEA first)

🔵 **The unit of packaging in this sector is becoming the *skill*** — trend 9
on [`../intel/trends.md`](../intel/trends.md) — and `p541` filed the first
artefact on this base that ships one **with an LMS exchange format** rather
than as a chat prompt:
[`cjescudero/asistente-docente`](https://github.com/cjescudero/asistente-docente),
**MIT** (1,075 B, titled, read first-hand).

| Role | Component | Grant | Why this one |
|---|---|---|---|
| Teacher-facing skills | [`cjescudero/asistente-docente`](https://github.com/cjescudero/asistente-docente) | 🟢 **MIT** (1,075 B) | **Twelve skills**: organise sources, build materials, assess, return feedback. One source tree, packaged for **ChatGPT Work and Claude Cowork** |
| The LMS seam | Moodle **GIFT** question-bank import/export | 🔴 GPL-3.0 (Moodle) | 🟢 **This is the part that matters.** GIFT is a text format Moodle imports natively, so generated items land in the real question bank with no plugin and no database access |
| Assessment delivery | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (2,058 B) | When the institution needs **QTI 2.1** rather than GIFT, this is the permissive engine `p541` filed |
| Record of what happened | `yetanalytics/xapipe` | 🟢 Apache-2.0 | Feedback and attempts into an LRS, per `P579` |

**The wiring:**

1. **Fork the skill pack and cut it to three skills**, not twelve — the ones
   the department actually asks for. Twelve skills is a demo; three that match
   a real marking workflow is a deployment.
2. **Generate into GIFT, import into a staging Moodle course, and have two
   teachers mark the output against their own rubric.** The import path is the
   whole technical risk and it is cheap to prove.
3. **Export feedback back through the same seam.** The pack already does this;
   do not rebuild it.
4. **Add QTI via `qtiworks` only if the institution's assessment policy
   requires standards-compliant items.** GIFT is enough for formative work.

🔵 **Estimating aid, not a branch:** p540's forks-per-star ranking put
import-as-dependency components at **≤ 0.182** and
deploy-per-institution at **≥ 0.250**. A skill pack is the former; Moodle and
`qtiworks` are the latter. 🔴 Per `Gap 540-C` the boundary is fitted to n = 14,
so no step above branches on it.

🔴 **The provenance clause to put in the statement of work.** The pack carries
a `.zenodo.json`, so the author intends an archival DOI — good for citation,
and it means **the upstream may be versioned academically rather than
semantically**. Pin a commit.

## P587 — The public-sector integration engagement: build against the state's own schemas (EMEA — Finland; the shape is portable across the EU)

🟢 **`p541` filed seven national registries** Finland's National Agency for
Education publishes in the open. For a ministry or agency buyer this replaces
the most expensive part of a data-platform engagement — agreeing the model —
with reading someone else's working one.

| Layer | Component | Grant | Role in the build |
|---|---|---|---|
| Curriculum | [`opetushallitus/eperusteet`](https://github.com/opetushallitus/eperusteet) | 🟡 **EUPL-1.1+** by reference | The machine-readable national curriculum: the outcome vocabulary everything else keys to |
| Learner identity | [`opetushallitus/oppijanumerorekisteri`](https://github.com/opetushallitus/oppijanumerorekisteri) | 🟡 **EUPL-1.1+** | The national learner identifier — the join key |
| Records | [`opetushallitus/koski`](https://github.com/opetushallitus/koski) | 🟡 **EUPL-1.1+** | Study rights and completed studies |
| Admissions | [`opetushallitus/ataru`](https://github.com/opetushallitus/ataru) | 🟡 **EUPL-1.2** | Applications and admissions |
| Analytics over it | [`Apereo…/LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | 🟢 **ECL-2.0** (9,919 B) | 🟢 **The permissive half of the stack.** Risk models over the registry data |
| Extractor pattern | [`Apereo…/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 🟢 **ECL-2.0** (11,087 B) | The template to copy when writing the extractor for *this* client's LMS |

**The wiring, and the licence boundary that defines it:**

1. **Read the schemas; do not vendor the services.** 🔴 EUPL is **reciprocal**
   with an EU-law jurisdiction clause. The registries are **integration targets
   and reference models**. Everything the studio writes sits on the
   **ECL-2.0 / Apache side** of the boundary.
2. **Build the extractor first**, modelled on `lap-sakai-extractor`, mapping the
   client's LMS into the LAP schema.
3. **Run `LearningAnalyticsProcessor` over it** for the risk model, and serve
   results through `OpenDashboard-api` (**ECL-2.0**).
4. **Check the version of every EUPL notice you rely on.** 🔴 Six of the seven
   say **1.1** and one says **1.2**; the obligations differ and the notice is
   the only place the version appears, because the text is **not reproduced in
   the repository**.

🔴 **Do not reuse `Apereo…/OpenLRS`**: its own description reads
**"Deprecated"**. 🔴 And `KualiCo/rice` (**ECL-2.0**, 11,106 B) is available
for the administrative workflow layer, but it is a large institutional
middleware — take the workflow engine, not the suite.

## P588 — Licence triage as a billable intake step, before any architecture (Global; APAC and LATAM first)

🔵 **This pattern exists because `p541` measured the failure rate of not doing
it.** Of 37 education repositories whose grants an automated pass could not
resolve, **13 are not usable in client work** and **six of those read as
permissive to a body-matching tool** — a `SATA`-titled MIT, a *Research*-titled
MIT, a *License Agreement*-titled MIT, a *Proprietary*-titled body a classifier
calls AGPL-3.0, `open-webui`'s clause-4 BSD, and a scoped *"most of the files"*
AGPL. 🔴 **A studio that skips this step discovers it at integration, after the
estimate.**

**The instruments, all on this base and all offline:**

| Step | Instrument | What it decides |
|---|---|---|
| 1. Is this actually new? | [`compose/code/p541-restated-presence/`](code/p541-restated-presence/) | Grades each candidate address against the committed tree: `FILED`/`PROSE` (already held), `HISTORY` (known, unfiled — **promote, don't re-discover**), `ARCHIVE` (recover), `BACKLOG`, `ABSENT`. Reads a **git ref**, so work in progress cannot self-match |
| 2. Does the title agree with the body? | [`compose/code/p541-grant-residue/`](code/p541-grant-residue/) — `bespoke_guard()` | 🔴 **Runs before any recall widening.** A stock body under a non-stock title is **not** that family |
| 3. Is the grant reproduced or referenced? | same — `by_reference()` | A short notice naming an authority plus a URL is a **real grant whose terms are not in the repository**, and whose **version** must be read off the notice |
| 4. Did the ladder read a fill-in? | same — `stub_payload()` | A 45 B `YEAR: / COPYRIGHT HOLDER:` file is a template stub; the grant is one rung on, at `LICENSE.md` |
| 5. What family is it? | [`ingest/backlog-gate.py`](../ingest/backlog-gate.py) · [`compose/code/p228-shelf-gate/classify_grant.py`](code/p228-shelf-gate/classify_grant.py) | 🔴 **Run both.** `p541` found they disagree, and that one already handles Portuguese while the other does not → `Gap 541-C` |

**The sequence, and the reason it is this order:**

1. **Run step 1 on the whole candidate list before reading anything.** `p541`
   ran it on 20 mandated-leg candidates and **20 were already held**; the
   reading budget it saved is the pattern's entire return.
2. **Fetch grants as bytes, not as pages.** `raw.githubusercontent.com`
   answered **200** for every address this pass probed while `github.com` HTML
   answered **403** through the session proxy. Record the byte count — it is
   the cheapest re-measurement a successor can make.
3. **Steps 2–4 before step 5.** Every one of them can **overturn** a family
   verdict, and running them after is how a false permissive grant reaches an
   estimate.
4. **Deliver the triage table itself.** Address, title block, byte count,
   family, and the verdict — buildable, reference-only, or excluded. 🟢 For an
   APAC or LATAM engagement, run the supply search **in the client's language
   first**: `p541` measured **8 new addresses of 10** in Spanish and
   Portuguese against **0 of 5** in English.

## 🆕 `p544` — one recipe added (`P593`), and **a licence contradiction corrected inside this very file**

🔴 **The defect first, because it is the more useful finding.** `P592`'s component
table called [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) **MIT**, and
annotated the cell *"(carried; re-read at `p541`)"*. 🔴 **It is Apache-2.0**, read
first-hand this pass at `main` · `1ea7df155447`: title block **`Apache License`**,
**`11 408` B**, **`sha256₁₂ cd2f54e1e506`** — byte-identical to the figure this
base has carried since `p543`.

🔴 **Four other cells in this same file already said Apache-2.0** (`P556`,
`P573`, `P583`, `P584`), as do
[`../agents/top.md`](../agents/top.md)'s shelf row,
[`../verticals/solutions.md`](../verticals/solutions.md),
[`../intel/trends.md`](../intel/trends.md) and
[`../intel/market.md`](../intel/market.md). 🔵 **So the base was right in nine
places and wrong in one, and the wrong one is the one that claimed to have been
re-read.** 🟢 **The lesson is narrow and worth keeping: a provenance note is not a
provenance.** *"(carried; re-read at `pN`)"* is prose a successor can type without
re-reading anything; a byte count and a digest are not. 🔴 **This matters here
more than on a shelf** — a recipe's licence column is what a studio acts on, and
MIT and Apache-2.0 impose different attribution and patent terms on a
deliverable.

🔴 **A second defect measured and left open rather than papered over:** this file
carries **four different star figures for DeepTutor** — `49.0k`, `49.7k`, `50.0k`,
`50.0k` — because each was rounded at a different pass. 🟢 GitHub's sidebar now
reads **`50.5k`**, and this base's one *precise* figure is `p537`'s **49 850**.
🔵 **A rounded number restated across passes becomes four numbers.** Registered as
`Gap 544-G`: a component's volatile metrics belong in **one** place, and a recipe
should cite it, not copy it.

## P593 — The mandatory-form generator that is forbidden to invent its own identifiers (EMEA — Russia/Türkiye shape; portable to any national funder or regulator)

**Brief.** 🟢 **The demand shape is evidenced by four artefacts across two
unrelated regions, and `p544` is the pass that noticed they are all the same
thing.** Every domestic, non-English education agent this base has found
automates **a document the state obliges someone to produce** — a **TÜBİTAK
2209-A** research proposal, a Russian **ДПО** professional-development programme,
a **BTK 514** course record — and **none of them automates a curriculum**. 🔴
**And every one of them is unlicensed**
([`../intel/measured-unusable.md`](../intel/measured-unusable.md)), so the
engagement is *build*, not *adopt*.

🟢 **The architectural requirement they all converge on, and it is unusual enough
to be the whole pattern:** the artefact's value is that certain fields are
**NOT generated**. `fairyofmiracle/edu_course_agent` refuses to invent the order
number (`наказ`) and the labour-function code; `captainmgc/tubitak-skills`
verifies every DOI across three MCP servers rather than emitting a plausible one.
🔵 **A hallucinated identifier on a legally load-bearing form is worse than a
blank one**, because a blank is visible and a plausible fake is not.

| Role | Component | Licence, read from the title block |
|---|---|---|
| 🔴 **Requirement evidence — READ, DO NOT FORK** | [fairyofmiracle/edu_course_agent](https://github.com/fairyofmiracle/edu_course_agent) (RU, ДПО) · [MaiQuangPhuoc/edu_agents](https://github.com/MaiQuangPhuoc/edu_agents) (VN, GDPT 2018) | 🔴 **NO GRANT** — `UNRESOLVED`, 10 filenames at the resolved ref, `p544` |
| Funder-form skills + **verified** citation lookup | [captainmgc/tubitak-skills](https://github.com/captainmgc/tubitak-skills) | 🟢 **MIT** — `LICENSE` @`main`, `1 067` B *(`p543`)* |
| Authoritative identifier source — **the gate that makes this safe** | the funder's / ministry's own registry, via MCP. Reference implementation: [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT** — `LICENCE` @`main` *(`p543`)* |
| Deterministic orchestration, fixed edges | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **MIT** *(carried)* |
| Skill / occupation codes where the form demands them | [KonstantinosPetrakis/esco-skill-extractor](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 **MIT** — `LICENSE` @`master` *(`p543`)* |
| Launch inside the institution's LMS | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 **Apache-2.0** — `LICENSE.md` @`master`, **`11 343` B · `sha256₁₂ 78b49eeaddbf`**, v6.4.4 (2026-09-23), re-read `p544` |
| Audit trail of what was generated and by whom | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 **MIT** — `LICENSE` @`main` *(`p543`)* |
| Licence gate | [`P551`](#p551--licence-due-diligence-gate-run-this-first-every-engagement) | — |
| Grant + archive precondition | [`P588`](#p588--licence-triage-as-a-billable-intake-step-before-any-architecture) + `p544`'s archive field | — |

**Wiring.**

1. **Model the form, not the subject.** Encode the target document as a schema
   with every field typed, and mark each field **`GENERATED`** or
   **`AUTHORITATIVE`**. 🔴 The `AUTHORITATIVE` set — order numbers, funder scheme
   codes, labour-function codes, DOIs, curriculum identifiers — is the whole risk
   surface.
2. **Make `AUTHORITATIVE` fields unreachable by the model.** They are filled by a
   **lookup against the issuing registry over MCP**, or they are left blank and
   flagged. 🔵 **Never by generation, and never by a retrieval the model can
   paraphrase.** `tubitak-skills`' DOI verification across three servers is the
   shape; `oak-open-curriculum-ecosystem` is the reference for what a state body's
   own registry-over-MCP looks like.
3. **Orchestrate with fixed edges.** **LangGraph** with a deterministic graph, not
   an autonomous loop — the same conclusion `edu_agents` reached independently for
   a prescribed curriculum (`P592`). A form has a fixed shape; an agent that can
   decide to skip a step is a liability.
4. **Emit in the funder's own template.** DOCX/PPTX/PDF from the real template
   file, not a lookalike. 🔴 **A regulator rejects on format before it reads
   content**, which is why both evidence artefacts ship template-faithful export.
5. **Log every field's provenance to an LRS.** `learnmcp-xapi` writes back over
   xAPI, so each `AUTHORITATIVE` value carries *where it came from*. 🟢 This is
   what converts the deliverable from a document into an **auditable** document —
   and under the EU AI Act's Article 50 transparency duties, **already in force
   since `2026-08-02`**, that audit trail is a compliance artefact, not a nicety.
6. **Gate the components before step 1.** Run `P551`/`P588`, plus `p544`'s
   **archive-state** read — `p543` shelved a platform archived two months earlier
   and `p534` an agent layer archived seven days earlier, so archive state is a
   precondition, not a detail.

🔴 **Where this pattern must not be sold.** If the client's form is **not**
state-mandated, the `AUTHORITATIVE`/`GENERATED` split costs more than it returns
and `P589`'s course factory is the better shape. 🔵 **The whole justification for
this architecture is that a wrong identifier has a legal consequence.**

🟡 **Stated as a limit, not hidden:** the demand evidence is **n = 4** and all
four artefacts were found by non-English search legs, which is a discovery method
with a known bias (`Gap 544-B` names the test that would confirm or kill the
form-not-curriculum reading). 🟢 **Every component above, by contrast, is granted
and was read first-hand** — so the recipe is buildable today even if the market
claim narrows.

## 🆕 `p543` — two recipes added (`P591`, `P592`), and the second one exists because its components are **unusable**

🔵 Every component named below had its **grant read as bytes on `2026-10-30`**
with the probe this pass repaired (`Gap 542-A`, `542-H`). 🔴 **`P592` is the
first recipe on this page whose central finding is that you may not use the
assets that prove the requirement** — three Vietnamese education agents carrying
no licence on any channel. A pattern that pretends otherwise would be a
liability, so the recipe is built as a **clean-room re-implementation against
measured requirements**, which is a different engagement with a different price.

## P591 — The national research-funding workflow, which no other asset on this base addresses (EMEA; Türkiye, portable to any national funder)

**Brief.** A university research office — or a national funder itself — wants
to raise the volume *and* the floor of quality of proposals submitted to a
state grant programme. The work is not writing prose: it is **conforming to a
funder's template, verifying every citation, and producing the exact artefact
the form demands**, repeatedly, under a deadline. 🟢 **This base held 71 agents
and none of them did this**, which is why `p543` shelved a 0★ repository.

| Role | Component | Licence (read as bytes, `2026-10-30`) |
|---|---|---|
| 🆕 Proposal workflow (the core) | [captainmgc/tubitak-skills](https://github.com/captainmgc/tubitak-skills) | **MIT** · `LICENSE`@`main` **1 067 B** · 🔴 **0★, 4 commits** |
| 🆕 Domain curriculum for upskilling the office | [kmkarakaya/btk_rag_bot_egitimi](https://github.com/kmkarakaya/btk_rag_bot_egitimi) | **MIT** · `LICENSE`@`main` **1 071 B** · 20★, 43 commits |
| 🆕 Localisation precedent | [komunite/ai-engineering](https://github.com/komunite/ai-engineering) | **MIT** **1 070 B**, holder `Rohit Ghumare` — a declared fork of [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) |
| Citation verification | `paper-search-mcp`, `arxiv-mcp-server`, `semantic-scholar-mcp` (named by the skill pack) | 🟡 **not read this pass — probe before use** |
| Agent substrate | [Intelligent-Internet/ii-agent](https://github.com/Intelligent-Internet/ii-agent) | **Apache-2.0** · 3.4k★ *(carried from `p542`'s read)* |
| Licence gate | [`P551`](#p551--licence-due-diligence-gate-run-this-first-every-engagement) | — |

**Wiring.** Treat `tubitak-skills` as a **specification, not a dependency** —
at 4 commits it is a worked example of the shape, and the shape is the value:
a skill that knows *this* funder's call rules, *this* funder's form template,
and emits `docx`/`pdf` the form accepts. Lift that structure onto `ii-agent` so
the substrate is maintained by someone else, and keep **one skill per funder
programme** rather than one general "grant writer" — the rules differ per call
and they change annually, which is exactly the knowledge the office already
has and cannot encode. 🟢 **Wire the three MCP citation servers as a hard gate,
not a helper:** a proposal with a hallucinated DOI is worse than a late one,
so an unverifiable reference fails the build. Use `btk_rag_bot_egitimi` as the
**internal upskilling track** — it is a state authority's own 55-lesson RAG
course, so the office learns the technology from a nationally-recognised
curriculum rather than a vendor deck.

**Hard constraint — the call rules are dated, and the asset says so.**
`tubitak-skills` states its rules are *"2026 çağrısına göre"* and tells the
user to check the current call announcement. 🔴 **Build that in: every
generated proposal carries the call-document version it was written against,
and the pipeline refuses to run against an expired call.** This is the same
dated-premise failure `Gap 543`/`Gap 523` record for legal claims, and it bites
harder here because a funder rejects on form.

**Effort.** 5-7 weeks. Week 1 `P551` over every component including the three
MCP servers; 2-3 re-implement the skill structure per target programme on
`ii-agent`; 4 template-fidelity testing against accepted historical proposals
the office supplies; 5 citation-verification gate; 6-7 pilot on one call, with
the office's own reviewers scoring blind against unaided submissions.

---

## P592 — Capturing a requirement when the proof-of-requirement is unlicensed (APAC; Vietnam)

**Brief.** `p543`'s Vietnamese leg found three domestic education agents that
between them describe a market this base's 72 shelved agents do not serve:
**scarce hardware**, **a prescribed national curriculum**, and **a messaging
app rather than an LMS as the teacher's interface**. 🔴 **None of the three
carries a licence** — `UNRESOLVED` across 180 filenames at the resolved
default branch, a silent sidebar, and silent README prose. **So the engagement
is not "adopt these"; it is "build this, having learned from these".**

| Role | Component | Licence |
|---|---|---|
| 🔴 **Requirement evidence — READ, DO NOT FORK** | [MaiQuangPhuoc/edu_agents](https://github.com/MaiQuangPhuoc/edu_agents) · [dungptt-dng/smart-ict-classroom](https://github.com/dungptt-dng/smart-ict-classroom) · [minhdevtry/AI-Teacher-Assistant-Agent](https://github.com/minhdevtry/AI-Teacher-Assistant-Agent) | 🔴 **NO GRANT on three channels** |
| Curriculum-bounded tutoring core | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** — 🔴 **corrected at `p544`; this cell read "MIT (carried; re-read at `p541`)" and was the only curated cell on the base that said so.** Title block `Apache License`, `11 408` B, `sha256₁₂ cd2f54e1e506`, read at `main` · `1ea7df155447` |
| Deterministic orchestration | [LangGraph](https://github.com/langchain-ai/langgraph) | **MIT** *(carried)* |
| Retrieval over the prescribed textbook | Qdrant + the client's own licensed corpus | Apache-2.0 *(carried)* |
| Offline / low-spec delivery | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** *(carried)* |
| Licence gate | [`P551`](#p551--licence-due-diligence-gate-run-this-first-every-engagement) | — |

**Wiring.** The three unlicensed projects converge on one architectural
decision worth copying: **`edu_agents` chooses a deterministic pipeline over
ReAct for the education domain and bounds the LLM to the textbook to suppress
invention.** 🟢 **That is the right default for a prescribed national
curriculum and it is the opposite of what a general tutor does** — so build on
**LangGraph** with fixed edges, not an autonomous loop, and make "cite the
textbook section or refuse" a structural property of retrieval rather than a
prompt instruction. Take `smart-ict-classroom`'s constraint seriously:
**scheduling under hardware scarcity is the product** in a lab with fewer
machines than groups, and it is plain software — fair turn rotation and
in-group role rotation, no model required. Deliver through **Kolibri** where
connectivity is the binding constraint. And take the interface finding
literally: if teachers run the class from a messaging app, the LMS is the
system of record and **the chat surface is the UI**.

**Hard constraint — the licence boundary is the deliverable's main risk.**
🔴 **Do not vendor, fork, copy or paste from the three evidence repositories,
and do not let a coding agent read them into a working tree.** An absent
licence is not permission; it is reserved copyright. 🟢 **Capture the
requirement as a written specification with the repositories cited as prior
art, have the client sign that specification, and build clean.** Where a
specific project is genuinely the right starting point, the honest route is
commercial: **approach the authors for a grant or a contribution agreement** —
all three are live and actively developed, and `edu_agents`' author is
reachable through the repository. **That conversation is cheaper than the
rewrite and it is the first thing to try.**

**Regulatory driver, already on this base.** Vietnam's **Decision
33/2026/QD-TTg** names education among six high-risk sectors and puts automated
assessment in scope. 🟢 **So the audit trail is not optional polish** — every
assessment decision needs its retrieval sources and its human approver on
record, which is the one thing none of the three prototypes does.

**Effort.** 10-12 weeks, and the first two are legal, not technical. Weeks 1-2
specification and prior-art citation, plus the authorship approach above;
3-4 `P551` over every component actually to be used; 5-7 deterministic
LangGraph core bounded to the client's licensed textbook corpus; 8 scheduling
module; 9 messaging-surface adapter; 10 Kolibri offline packaging; 11-12
assessment audit trail and a one-school pilot.

---

## 🆕 `p542` — two recipes added (`P589`, `P590`), both built on components read first-hand this pass

🔵 Every component named in the two recipes below had its **grant read as
bytes** on `2026-10-30`, and the two new grant shapes this pass found
(`LICENSE-CODE`/`LICENSE-TEXT`, and a grant on `master`) are written into the
tables rather than normalised away — because a due-diligence gate that probes
`LICENSE` at `main` will report both as ungranted (`Gap 542-A`, `542-B`).
🔴 **Run [`P551`](#p551--licence-due-diligence-gate-run-this-first-every-engagement)
first, as always — and patch its probe surface before you trust it on
courseware.**

## P589 — The course factory: attack faculty workload, not learner response (Global; North-America-funded)

**Brief.** A university or a publisher wants to cut the cost of *producing* a
course — syllabus, slides, scripts, assessments — rather than add another
student-facing tutor. This is the half of the market that the US `$169 M`-class
higher-ed funding actually buys, and until `p542` this base had **no permissive
asset pointed at it**.

| Role | Component | Licence (read as bytes, `2026-10-30`) |
|---|---|---|
| 🆕 Course generation (the core) | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** · `LICENSE`@`main` **1 067 B** · 490★ · EACL 2026 Main |
| 🆕 Licensed content body | [ocademy-ai/machine-learning](https://github.com/ocademy-ai/machine-learning) | **MIT** (`LICENSE-CODE`) **+ CC-BY-4.0** (`LICENSE-TEXT`) · 231★ · 3 049 commits |
| 🆕 Agent substrate | [Intelligent-Internet/ii-agent](https://github.com/Intelligent-Internet/ii-agent) | **Apache-2.0** · `LICENSE`@`main` **11 357 B** · 3.4k★ |
| Delivery target | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 |
| Portable output | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 · 152★ |
| Learner record | [DavidLMS/learnmcp-xapi](https://github.com/DavidLMS/learnmcp-xapi) → [openfun/ralph](https://github.com/openfun/ralph) | **MIT** / **MIT** |
| Acceptability gate | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) rubrics | **Apache-2.0** · 601★ |

**Wiring.** `instructional_agents` is the pipeline, and the reason to start
there rather than from a prompt chain is that it already implements **ADDIE**
(Analyse, Design, Develop, Implement, Evaluate) as distinct agent stages, which
is the model the client's own instructional designers are trained on — you are
automating a process they recognise, not proposing a new one. Drive it through
its **REST API**, not its CLI, so the factory is a service the LMS calls; its
web UI becomes the designer's review console. **`ii-agent` sits underneath as
the substrate** so that swapping model providers or adding tools does not mean
re-writing the ADDIE stages — the education semantics stay in
`instructional_agents`, the plumbing stays in `ii-agent`. 🟢 **`ocademy` is the
seed corpus and the licence story**: its content is **CC-BY-4.0**, so generated
courses derived from it can be shipped and attributed, which is the question
that normally kills a course-factory pilot at legal review. Emit **H5P** so the
artefacts outlive the platform; write every generation and review event to
**Ralph** as xAPI through `learnmcp-xapi`, so "who approved this course" has an
answer. The **k12 rubrics** run in CI over a fixed prompt set and a regression
fails the build.

**Hard constraint — build it in, not in the policy doc.** Course content is a
*publication*, so the binding risk is provenance, not safety. Two rules,
structural: (1) **every generated artefact carries the licence and attribution
of its sources** — CC-BY-4.0 requires attribution, and a factory that loses it
produces unshippable output at scale; (2) **a human commits, the agent drafts**,
and the xAPI record names the committer — the same rule as `P547`, for the same
reason. ⚠️ **And `instructional_agents` is a research artefact**: 95 commits, an
EACL paper, no release cadence. Vendor the version you validate and expect to
maintain your fork.

**Effort.** 8-10 weeks. Weeks 1-2 REST deployment and `ii-agent` substrate;
3-5 ADDIE stage tuning against the client's own course corpus; 6 `ocademy`
seeding and attribution plumbing; 7 H5P emission; 8 xAPI and approval trail;
9-10 rubric CI and a single-department pilot.

---

## P590 — The PII-stripped on-premise classroom, because APAC procurement asks for it in writing (APAC)

**Brief.** Singapore MOE requires that for commercial off-the-shelf tools,
schools **check that input data contains no personally identifiable information**
and complies with data-management guidelines; China MOE's 2026 priorities put
**data security and personal-information protection** beside the pedagogy. Both
are ingress-path architecture requirements, and a hosted-API tutor cannot
satisfy either cheaply. This recipe answers them in hardware.

| Role | Component | Licence (read as bytes, `2026-10-30`) |
|---|---|---|
| 🆕 On-premise classroom analytics | [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) — `smart-classroom`, `ai-teaching-assistant` | **Apache-2.0** · `LICENSE`@`main` **11 351 B** · 2★ / **14 forks** · 481 commits |
| Classroom delivery | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 41.8k★ · 6.5k forks · 805 commits |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) · [vllm-project/vllm](https://github.com/vllm-project/vllm) | **MIT** / **Apache-2.0** |
| 🆕 Agent-loop reference (for the PII gate) | [minmaxflow/mini-kode](https://github.com/minmaxflow/mini-kode) | **MIT** · `LICENSE`@**`master`** **1 066 B** · 305★ |
| LMS of record | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 |
| Learner record | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** |

**Wiring.** The **Intel suite is the ingress**, and it is chosen for one
property: its audio and video pipelines are *"accelerated with the OpenVINO™
toolkit"* against Intel **CPUs, integrated GPUs and NPUs**, so classroom
session processing — `smart-classroom`'s statistics, re-identification and
session summaries — **runs on the school's own hardware and the raw media never
leaves the building.** That is the PII requirement satisfied structurally
rather than contractually. 🟢 **The PII gate is a separate process in front of
everything else**, and `mini-kode` is on this table as the **reference
implementation to copy, not a dependency to ship**: it is an explicitly
educational agent loop with **permission approval** already modelled, which is
exactly the shape the gate needs — every tool call pauses, is inspected, and is
either stripped or refused. **`OpenMAIC` is the delivery surface** (lecturer,
peer and assistant roles, slides, quizzes, whiteboard) and talks only to
**local** inference via Ollama or vLLM. Moodle stays the system of record;
Ralph takes the xAPI stream. 🔴 **Nothing in this stack calls a hosted model
API**, which is the whole point — and it is why the pattern is `P590` and not a
variant of `P549`.

**Hard constraint — build it in, not in the policy doc.** (1) **Re-identification
is the risk, not the feature.** `smart-classroom` offers student
re-identification; in a jurisdiction that requires PII-free input this must be
**off by default and separately authorised**, with the authorisation in the
xAPI record. (2) **Selectivity is a stated procurement rule**, not a
preference: Singapore MOE says AI should be used only where it contributes
meaningfully to learning outcomes, so the deliverable needs a *named learning
outcome per agent surface* — a feature with no outcome attached is a
procurement liability. (3) ⚠️ **The Intel suite's own disclaimer, carried
verbatim: the applications are *"intended for reference and demonstration, not
production."*** Treat it as a benchmark harness and a starting point; the
hardening is yours, and it is most of the work. 🔵 **Its 2-stars-to-14-forks
ratio is the encouraging signal** — more parties are deriving from it than
bookmarking it.

**Effort.** 10-14 weeks. Weeks 1-2 hardware sizing and OpenVINO benchmarking on
the client's actual devices; 3-4 PII gate (modelled on `mini-kode`'s approval
loop) and the authorisation record; 5-7 `smart-classroom` hardening with
re-identification off; 8-10 `OpenMAIC` against local inference; 11-12 Moodle and
Ralph integration; 13-14 one-school pilot and the jurisdiction's
data-management sign-off. 🔴 **The long pole is weeks 1-2** — if the hardware
cannot carry the pipelines, the pattern does not apply and you need `P549`
instead. **Benchmark before you promise.**

---


## 🆕 P601 — The SIS this base had written off (North America on-prem; LATAM public sector; APAC data-residency)

🟢 **Why this recipe exists at all:** `p548` read
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)'s licence **payload**
and found the complete **GNU GPL v2** at `docs/License.txt` (**17 286 B**,
`sha256 224ac3d403e3…b8ba`, declared in `README.md` **L49–51**), after nineteen passes of
this base publishing ⛔ *no grant* from **root-scoped** probes. 🔵 So the largest
open-source SIS this base can name is buildable, and nothing on this page used it.

**When.** The client needs a **student information system of record** — enrolments,
scheduling, grades, attendance, transcripts — and one of the following is true: the data
cannot leave their premises (district/state contract language in North America; APAC
high-risk regimes), or the deliverable must itself be publishable (LATAM ministry and NGO
programmes). 🔴 **Do not use this recipe for a hosted multi-tenant product**: GPL-2.0 is
copyleft and the SIS is the core, not a leaf.

### Components, each with the grant this base read first-hand

| Layer | Repo | Grant | Role |
|---|---|---|---|
| **SIS of record** | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟡 **GPL-2.0** (`docs/License.txt`, 17 286 B — *read `p548`*) | PHP/MySQL. 347★, 288 forks, human commit **2026-10-26**. Enrolment, scheduling, gradebook, attendance, transcripts |
| **LMS beside it** | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Course delivery. Already copyleft, so it adds no new constraint this stack does not have |
| **LMS tool surface** | [`leshamblin/MoodleMCP`](https://github.com/leshamblin/MoodleMCP) | 🟢 **MIT** | 67 counted tools, **read-only by default** with writes behind an explicit flag — the safety posture an SIS-adjacent agent needs |
| **Orchestration** | [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) | 🟢 **MIT** (`main/LICENSE`) | 14 372★. Horizontal, nothing education-specific — which is why it carries no sector licence risk into the stack |
| **Tutoring surface** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** | Student-facing tutoring tools, shelf-attested |
| **Assessment feedback** | [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 **Apache-2.0** | Automated submission feedback with an API the agents can call |
| **Offline tier (optional)** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | Only if connectivity is a constraint — then compose with **`P600`** instead of extending this one |

### How it wires together, and where the licence boundary runs

```
          ┌──────────────────────── the copyleft core (GPL) ────────────────────────┐
          │  openSIS-Classic  (GPL-2.0)        moodle  (GPL-3.0)                    │
          │  enrolment · scheduling · grades   course delivery · activity logs      │
          └───────────▲───────────────────────────────▲─────────────────────────────┘
                      │ MySQL views, read-only user   │ MoodleMCP (MIT) — 67 tools,
                      │ + openSIS's own PHP endpoints │ writes OFF by default
          ┌───────────┴───────────────────────────────┴─────────────────────────────┐
          │   MCP boundary — a process boundary, NOT a linking boundary             │
          └───────────▲─────────────────────────────────────────────────────────────┘
                      │ stdio / HTTP
          ┌───────────┴─────────────────────────────────────────────────────────────┐
          │  agent-framework (MIT)  —  orchestration, owned by the client           │
          │    ├── registrar agent   → reads openSIS, drafts, never auto-commits    │
          │    ├── tutoring agent    → tutor-mcp (MIT)                              │
          │    └── feedback agent    → feedbacksystem (Apache-2.0) API              │
          └─────────────────────────────────────────────────────────────────────────┘
```

🟢 **The licence boundary is the load-bearing design decision, and it is why this recipe is
shaped this way.** The GPL core is reached **only** across a **process** boundary — MCP over
stdio or HTTP, plus a read-only MySQL user and openSIS's own PHP endpoints. 🟢 The agent
layer is a **separate program** that communicates with the SIS at arm's length, so the
client's own orchestration code and prompts are **not** derivative of openSIS. 🔴 **What
would break that:** compiling agent code into openSIS as a PHP module, or shipping a patched
openSIS as part of a closed product. 🔵 Both are avoidable and neither is needed here.

🟡 **Stated plainly for the engagement letter:** modifications *to openSIS or Moodle
themselves* must be published under their licences. 🟢 In a ministry, district or NGO
programme that is usually already a requirement rather than a cost. 🔴 **This is not legal
advice** and the client's counsel decides; the point of the recipe is that the architecture
keeps the question **small and locatable** instead of diffuse.

### Build order

1. **Verify the grant yourself before anything else.** `P551`'s rule 1, and this recipe is
   the reason it exists: fetch `docs/License.txt` at `HEAD`, confirm **17 286 B** and the
   GPL-2 title block. 🔴 Do **not** accept a root-scoped scanner's *"unlicensed"* — that
   verdict is what cost this base nineteen passes (Trend 49).
2. **Stand up openSIS + Moodle on the client's infrastructure**, with a read-only MySQL
   user for everything the agent layer reads.
3. **Put `MoodleMCP` in front of Moodle with writes off.** Turn individual writes on only
   where a human approves the action downstream.
4. **Wrap openSIS behind a thin MCP server of your own** — it has no published MCP surface,
   so this is the one component you build. 🟢 Scope it to the read paths in step 2 first;
   add writes last and gate them.
5. **Orchestrate in `agent-framework`**, one agent per role, and keep the registrar agent
   **draft-only**: it proposes an enrolment or grade change, a human commits it.
6. **Attach `tutor-mcp` and `feedbacksystem`** for the student-facing and assessment paths.
7. **Gate with `P597`** before shipping, and re-run the staleness read — openSIS's human
   commit cadence is the thing to watch, not its star count.

🔵 **Regional notes.** 🟢 **LATAM:** openSIS joins `i-educar` (GPL-2.0, 722★) and
`RosarioSIS` (GPL-2.0, 648★) — the copyleft SIS tier is four platforms deep and three of
them are built for the region's languages and public sector; pick by localisation, not by
stars. 🟢 **North America:** this is the open-source answer to the proprietary SIS
incumbents for a client whose contract forbids hosted data. 🟢 **APAC:** compose with
**`P590`** (PII-stripped on-premise classroom) — the constraint is the same one and the
recipes share a deployment shape.

