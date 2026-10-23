---
industry: education
region: Global
updated: 2026-10-23
---


**🆕 Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **`p396` ranked
re-running the xAPI 2.0 bake-off second, on the grounds that *"three claimants at 1 star between them
will move fast or die; either outcome changes the recommendation."* They moved — and they did not
move together.** One new pattern, and `Pattern AE` amended rather than restated. Evidence:
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) ·
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

## 🟢 `Pattern AE` AMENDED — the xAPI 2.0 bake-off now has an activity ranking

🔵 `Pattern AE` told a studio to adjudicate three zero-star LRS claimants itself, because *"reputation
cannot decide this."* That still stands. 🟢 **What `p397` adds is the one signal that was missing:
which of them is actually being built.** Dated on the git channel, never on the HTML "Updated" column
(`396-G`):

| candidate | stack | `p396` | `p397` HEAD | days | reading |
|---|---|---|---|---|---|
| [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | ASP.NET Core | "under 75 d" | `0d47d65` 2026-10-21 | 🟢 **1** | 🟢 **under active daily development** |
| [`codetakt/kiva`](https://github.com/codetakt/kiva) | Rust, F\* proofs | "under 75 d" | `addf100` 2026-10-21 | 🟢 **2** | 🟢 **also moving**; 🔵 still the only one whose README *withdraws its own conformance claim* |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | TypeScript/Hono/Postgres | "under 75 d" | `4d18e0c` 2026-08-08 | 🔴 **75** | 🔴 **has not moved at all** since `p396` measured it |

🟢 **So the "all three are under 75 days" sentence has split into two live projects and one
stalled one**, and the bake-off order changes accordingly: 🟢 **run `xapi-dotnet` and `kiva` first**,
and treat `xapi-lrs` as the control rather than a contender until it commits again.

🔴 **The tooling half of `Pattern AE` is the part that has aged, and it matters more than the
candidates.** [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
is 🟢 MIT, 78 ★ — and **`5bc232d`, 2025-09-04, 413 d**, unchanged. 🔵 **You are asked to certify
2.0 conformance with a suite that has not been touched in fourteen months**, while the implementations
it judges change weekly. 🟢 [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner)
(Apache-2.0, **6 d**) and [`yetanalytics/xapi-schema`](https://github.com/yetanalytics/xapi-schema)
(**6 d**) are both live, so the **CI harness around the suite is maintained even though the suite is
not.** 🔴 **Quote that asymmetry to a client before you quote a pass rate.**

## 🆕 `Pattern AF` — prove provenance BEFORE you prove the licence, in two commands

**When.** Any engagement that is about to adopt, fork or warrant an open-source education component
— and especially when the candidate came out of a search result rather than a standards document.

🔴 **Why it goes first.** A licence read **cannot** tell a fork from its upstream: the payload is
usually byte-identical, so the grant channel is blind by construction (`395-A`). A star read cannot
tell a rename from a fork either: GitHub answers on the old organisation path indefinitely and shows
the same stars. 🔴 **On these shelves, 8 of 15 shared-root pairs were renames and 7 were real
forks** — and nothing short of comparing commits separates them.

**The recipe, and it needs no API, no HTML and no credentials.**

1. **Root commit** — shared root means shared ancestry:
   `git clone --filter=blob:none --no-checkout -q https://github.com/OWNER/REPO d && git -C d rev-list --max-parents=0 HEAD`
2. **HEAD** on the same clone: `git -C d rev-parse --short=12 HEAD`
3. **Adjudicate**: same root + same HEAD → **one artefact, two addresses** (fold them, cite the
   current path); same root + different HEAD → **a real fork** (now decide which side to carry);
   distinct roots → **unrelated** despite the shared name; either side unresolvable → **inconclusive**,
   never "independent".
4. 🟢 **Then date both sides**, because step 3 tells you the fork is real and nothing about whether
   anyone maintains it. `T40` is the cautionary case: `ucfopen/pylti1.3` is a genuine institutional
   fork of `dmitry-viskov/pylti1.3`, and **both are over 1 370 days dead.**
5. **Only now read the grant**, and read it by enumerating the tree
   (`git ls-files | grep -iE '(licen[cs]e|copying)'`) rather than guessing filenames — that is how
   this pass found [`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples)
   ungranted at root with vendored third-party MIT two directories down.

🟢 **Wired and runnable:** `bash compose/code/p397-shelf-fork-audit/lineage.sh OWNER_A/REPO OWNER_B/REPO`,
with `make shelf-fork-candidates` deriving the candidate pairs from the shelves themselves and
`make gate-shelf-fork` holding 11 controls. 🔴 **Stated limit:** a squashed or re-rooted fork reads as
independent — no false positives, possible false negatives.

🔵 **Cost: two blobless clones per pair, a few seconds each.** `p397` ran 21 pairs inside one pass.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** Two patterns, both built on grants and dates
read first-hand this pass:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

## 🆕 `Pattern AD` — the agent that writes to the institution's record, not just its own memory

**When.** The client needs to show *someone else* — an accreditor, a regulator, a district board, a
parent — what the AI did and what the learner actually demonstrated. This is every North America K-12
engagement under Oklahoma-style teacher-review and opt-out rules, every EU deployer under Article 26
logging, and the governance sale that `intel/market.md` identifies as the LATAM entry point.

🔴 **Why you cannot just use the agent's memory.** `DeepTutor`, `inno-agent` and every other tutoring
agent on this shelf keep private, vendor-shaped memory designed for conversational continuity. It is
not an evidence record, it does not survive replacing the agent, and no registrar will read it
(`T37`).

**Components, all dated this pass.**

| Role | Component | Licence | Age | Note |
|---|---|---|---|---|
| Record store (Python shop) | [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT | 🟢 10 d | France Université Numérique; Open edX Aspects' own LRS |
| Record store (JVM shop) | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 | 🟢 21 d | 144 ★; SQLite/Postgres/MariaDB/MySQL |
| Record store (.NET shop) | [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | 🟢 Apache-2.0 | 🟢 1 d | 🔴 0.x, 1 ★ — gate on a conformance run |
| Platform emitter (Moodle) | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 GPL-3.0 | 🟢 2 d | 82 ★; GPL because every Moodle plugin is |
| Agent ↔ LRS bridge | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 🟢 MIT | 🔴 **419 d** | **the weak link — see below** |
| Launch into the LMS | `packbackbooks/lti-1-3-php-library` / `ltijs` / `lti-tool` (`p395`) | 🟢 permissive | 🟢 1–9 d | pick by runtime |

**Wiring.** Agent → MCP (`learnmcp-xapi`) → LRS (`ralph` or `lrsql`); LMS → emitter
(`moodle-logstore_xapi`) → *the same* LRS; agent launched from the LMS over LTI 1.3 so the learner
identity on both paths is the same subject. 🔵 **The single design decision that makes this worth
building:** the agent's statements and the platform's statements land in **one** store against **one**
identity, so "what did the AI do for this student" and "what did this student do" are one query.

🔴 **Scope this honestly at estimate time.** `learnmcp-xapi` is 15 ★ and has not moved in fourteen
months. 🟢 It is MIT, it is small, and the xAPI statement shapes it needs are specified — so treat it
as **a reference to fork and own, budgeted as build, not as a dependency**. Anyone quoting it as
maintained third-party infrastructure will be wrong by about a year.

**Effort.** 6–8 weeks for a single-LMS, single-agent deployment on an existing Moodle or Open edX;
add 3–4 weeks to own the MCP bridge properly rather than vendoring it.

## 🆕 `Pattern AE` — choosing an xAPI 2.0 LRS when every candidate has zero stars

**When.** The client specified xAPI 2.0 / IEEE 9274.1.1 — increasingly common in defence, aviation,
regulated corporate training and any procurement written against the current standard.

🔴 **The situation, measured.** No adopted open-source LRS implements 2.0. `lrsql` (144 ★) and Ralph
(51 ★) are both 1.0.3. The three claimants hold **one star between them**: `pelotech/xapi-lrs` (0 ★,
TypeScript/Hono/Postgres), `codetakt/kiva` (0 ★, Rust, F* proofs) and `nurullahturkoglu/xapi-dotnet`
(1 ★, ASP.NET Core). 🔴 **Reputation cannot decide this**, and each project's own conformance claim
is self-reported — `kiva`'s README goes so far as to withdraw its own repository blurb, saying
equivalence with the 2025 edition *"has not been established"* and that source traceability *"does
not establish implementation conformance."*

🟢 **So adjudicate it yourself, with permissive tooling that already exists.**

1. Stand up each candidate against a **throwaway** Postgres — the suite persists data and its README
   warns it *"should not run against a production LRS endpoint."*
2. Run [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite)
   (🟢 MIT, 78 ★, Node) with `--xapiVersion 2.0.0`, then again with `1.0.3` — a conformant 2.0 LRS
   must still accept 1.0.x statements.
3. On the JVM, drive the same suite from CI with
   [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) (🟢 Apache-2.0,
   6 d) so the result is a build artefact rather than a screenshot.
4. 🟡 Read failures with judgement: a .NET implementer reports the suite *"sometimes expects more
   than the standard requires"* *(secondary)*, and the suite is **413 days old** while all three
   candidates are under 75 days. A failure is a conversation, not a disqualification.

🟢 **Hedge the choice structurally.** `pelotech/xapi-lrs` states its schema matches `lrsql` v0.9.5's
Postgres shape, so an `lrsql` database can be taken over. 🔵 This pass's fork arm confirms the two are
**independent codebases, not a fork** (distinct root commits `b1bfc0f67292` vs `f9e81c891b9a`) — so
this is genuine schema compatibility between rivals, which is the rare case where a client can start
on the 144 ★ 1.0.3 store and migrate to the 0 ★ 2.0 store without a data conversion.

**Effort.** 2–3 weeks for the bake-off and a reproducible CI conformance job; the result is reusable
across every later engagement on this layer, which is the main reason to do it once properly.


# Compose patterns — education

**🆕 Pass `p395` · reads and commit both 2026-10-23.** Two patterns, both built on grants and **dates**
read first-hand this pass: [`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv) ·
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).

## 🆕 `Pattern AC` — the JVM-or-Go client's LTI edge (the one this base could not quote before)

**When.** The client's platform team owns **Java** or **Go**, and an agent has to launch from their
Moodle, Canvas, Blackboard or D2L. This is most enterprise work and much of European public sector.

🔴 **Why the obvious route is closed.** The only permissive **Java** LTI 1.3 core is
[`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) (MIT) — **1,193 days dead**. The
Go options are [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti)
(Apache-2.0, **679 d**, pre-1.0 API) and [`macewan-cs/lti`](https://github.com/macewan-cs/lti) (MIT,
**1,918 d**, self-declared unstable, **deep linking unimplemented**). 🔴 An unmaintained library doing
**OAuth 2 / JWT signing and key rotation** is a *security* dependency — the same argument that
demoted `1EdTech/lti-1-3-php-library`. Do not put a client's identity flow on any of the three.

**Wire it like this.**

1. **LTI edge — [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool)** (🟢 MIT, HEAD **1 d**,
   `@lti-tool/core` v1.3.2). Serverless-native: Lambda, Workers, Hono, with OIDC, **Assignment and
   Grade Services**, Names and Role Provisioning, Deep Linking and Dynamic Registration all
   implemented, and the session store chosen at deploy time. 🟡 Prefer
   [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 Apache-2.0, **9 d**, 207 npm releases)
   instead when the client wants a long-running Node process and already runs Mongo.
2. **The hop.** The edge validates the launch, then forwards a **signed, short-lived internal token**
   carrying only `sub`, context, roles and the resource link to the JVM/Go service. 🔵 The agent never
   parses an LTI message, which is the whole point: the standards surface stays in the runtime where
   it is maintained.
3. **The agent** stays in Java or Go — the client's own service, unchanged.
4. **Grades back** through the edge's AGS client, never direct from the agent. One component holds the
   platform credentials.

🟢 **Why this beats forking a dead library:** `lti-tool` is 1 day old and `ltijs` 9, so key rotation
and spec drift are somebody's job. 🔴 **Cost to state in the proposal:** one extra deployable and one
extra network hop — *and* `lti-tool` is **8 ★ with no production claim** (its README's
*"Production-ready security features"* heading is about the security section, not the project), so
pilot it; `ltijs` is the safer default for a ministry. 🔵 Note this is the architecture `p391`
recommended for Python and `p392` correctly withdrew when `django-lti` turned up live at 2 days. **It
stands for Java and Go because the dating says so, not because it is the usual advice.**

## 🆕 `Pattern AD` — a learner-facing agent shell with a curriculum you are actually allowed to ship

**When.** The client wants a personal tutor that remembers a learner across months, and the
deliverable must survive a legal review.

1. **Shell — [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent)** (🟢 MIT, **1.3k ★**, HEAD
   **10 d**). You get the parts that are expensive to build: **L1** learner profile, **L2** a native
   wiki knowledge base, **L3** session records with cross-conversation retrieval, a **cron scheduler**
   for proactive check-ins, and a workspace-scoped **Practice Lab** with an in-browser terminal.
   🔵 It sits on the Pi coding-agent SDK (MIT) *without modifying its kernel*, so the upgrade path is
   npm, not a fork.
2. 🔴 **Do NOT ship its skill library.** The companion
   [`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) — skills and
   workspace presets — is **ungranted on every arm** (no licence file, no manifest field, no README
   grant, all three enumerated). Read it for shape; author your own.
3. **Curriculum — granted sources only.** [`oppia/oppia`](https://github.com/oppia/oppia)
   (🟢 Apache-2.0) for misconception-aware lesson structure, and
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) when the
   deployment is offline-first. 🔴 **Avoid grounding the tutor on
   [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) without legal sign-off**
   — `ODbL-1.0 AND CC-BY-SA-4.0`, and the **CC-BY-SA half reaches generated content**, so a curriculum
   document produced from it can inherit share-alike. That is `Pattern H`'s warning, and it is the
   trap this pattern is most likely to fall into.
4. **Launch from the LMS** with `Pattern AC`'s edge, so the tutor is reachable where students already
   are.
5. 🔴 **Regulatory stop, before any design work.** The moment this agent **grades**, **assigns a
   learner to a programme**, **assesses their appropriate level**, or **monitors behaviour during a
   test**, it is **Annex III ¶3 high-risk** in the EU and needs the human-in-the-loop and
   documentation posture. 🔴 And **no emotion inference, ever, in an EU educational setting** — that is
   prohibited outright, not assessable. Keep the memory layers descriptive (what was practised, what
   was missed) and never affective.

🟡 **Honest limits.** `inno-agent` is a **single-learner companion** — there is no cohort, roster or
teacher dashboard in it, so an institutional pilot needs that built. Its IM channels ship as **Feishu
and WeChat**, so a non-APAC deployment replaces the messaging layer. And at **10 days old with a June
2026 technical report**, it is a strong pilot base, **not** a ministry platform this quarter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** Two new patterns, both built on grants
read at the payload this pass. 🟢 **`Pattern AB`** — the **R statistics course graded automatically**,
closing the hole `p393` named when it pointed out that this base's most-adopted *maintained*
autograder grades R
while the shelves held no R components; its delivery layer is permissive (`gradethis` MIT, `learnr`
Apache-2.0, `ottr` BSD-3) and its measurement layer is GPL behind a process boundary, and its last
step is **the only offline assessment loop in this base** (`cran/exams` NOPS: printed, scanned, marked
automatically, paper audit trail). 🟢 **`Pattern AC`** — **give teachers an assistant builder instead
of building their assistants**, on **LAMB** (GPL-3, UPC Barcelona + UPV/EHU, peer-reviewed), which
publishes each teacher-authored assistant into Moodle as an **LTI external tool** so the LMS is never
forked. 🔴 Both patterns carry a hard stop at grading: under the EU AI Act, systems that grade
learners or influence access to qualifications are **high-risk and require conformity assessment
before deployment**, so the grading step is scoped as a separate assessed workstream rather than sold
in the same phase.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/compose-patterns.md`](../archive/2026-10-22-p383-pre-rewrite/compose-patterns.md).

Every repo named here was verified first-hand on 2026-10-22 —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv). Licences are read from the
payload at the repository's **real default ref**, which for 13 of 58 live addresses is not `main`.

**The governing constraint for all of these:** the platform tier is copyleft, the agent tier is
permissive. Every pattern below therefore puts a **documented interop boundary** — LTI 1.3, MCP, or
web services — between client-owned code and the platform. None of them forks an LMS.

🆕 **`p389`** adds **`Pattern Q`** (the generated classroom, the greenfield answer when there is no
LMS to bolt onto), gives **`Pattern B`** a maintained mastery model, and gives **`Pattern D`** two
components that remove its server. Every repository named in those changes was **dated** this pass —
last commit at the real default ref:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). 🔵 **Read a date as a cost line:**
a permissive repository nobody has touched in eight months is something you *vendor and maintain*, not
something you *integrate* — which is why `Pattern B` vendors `pybryt` and why `Pattern Q` pins a ref.

---

## Pattern A — Tutor over the client's existing LMS (no fork, no copyleft exposure)

**For:** a client who already runs Moodle or Canvas and wants a tutor that knows the actual course.

**Wiring:**
1. **Expose the LMS.**
   - *Moodle:* install **`webservice_mcp`** from Moodle's own plugin directory (Moodle 4.5–5.2,
     latest release 23 Jul 2026). It serves Moodle's external functions as **MCP tools over
     JSON-RPC 2.0**, gated on the `webservice/mcp:use` capability. Configured inside Moodle — no
     patch to core, so **no GPL obligation reaches your agent**.
   - *Canvas:* [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for courses,
     assignments, submissions, grading, rubrics, students; or the fork
     [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (**MIT**) which adds office-hour
     appointment groups, syllabus read/write, student groups and course-content copy.
   - 🆕 `p390` *Open edX:* skip the MCP hop and run **inside** the platform as an **XBlock** — and the licence maths
     works out better than it looks. The platform is **AGPL-3.0**, but the component API your plugin imports,
     [`openedx/XBlock`](https://github.com/openedx/XBlock), and the [`xblock-sdk`](https://github.com/openedx/xblock-sdk)
     you develop against are both **Apache-2.0** (`LICENSE.TXT`, both dated 2026-10-22). **So the XBlock you write can stay
     MIT or proprietary while running in an AGPL host** — no fork, no LTI hop, and full access to course state.
     [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia) is the working proof.
     🔴 **Check the boundary per package, not per org:** [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning)
     and the `frontend-app-*` MFEs are **AGPL-3.0**, so an import from those pulls network copyleft straight back in.
     Keep the plugin's dependency list to `XBlock` plus your own code and audit it in CI.
   - 🟡 **Grant status, corrected:** the plugin repo
     [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has **no
     root licence file**, but `version.php` carries the full **GPL-3.0-or-later** header Moodle
     requires of every plugin — so it is granted, and GPL is survivable because you reach it over
     JSON-RPC rather than linking to it.
     [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) is
     **manifest-only MIT** (`package.json` declares it; the file it names is absent from the tree).
     🔴 **Do not use** [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp): no licence file
     **and** no `license` field in `pyproject.toml` — genuinely no grant to redistribute.
2. **Ground it in the course material.** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
   (**Apache-2.0**) over the course files, with
   [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
   (**Apache-2.0**) for the PDF/DOCX/PPTX/scan reality. If the client has lecture video,
   [opencast/opencast](https://github.com/opencast/opencast) transcripts are the richest corpus
   available and nobody is using them.
3. **Give it pedagogy and memory.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (**Apache-2.0**) for persistent learner memory plus material-grounded tutoring. If the client
   wants explanation *pitched* to the learner's state rather than merely retrieved, look at
   [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) — but it is **GPL-3.0**, so
   run it as a separate service, not as a library inside the deliverable.
4. **Front it.** [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) — SSO,
   per-user quota, provider routing and the **audit log** that gets the build past a data-protection
   officer. (Not `open-webui`: its `LICENSE` is 2,819 B of BSD-3 text **plus** a branding
   restriction and a CLA.)
5. **Prove it.** [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   (**MIT**) with [MMLU](https://github.com/hendrycks/test) (**MIT**) and
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**), scored on the client's own
   subject mix, before and after.

**Licence posture:** client-owned code is MIT/Apache/BSD throughout. The only copyleft component is
the LMS itself, reached over a published protocol. **Deliverable stays closed if the client wants it
closed.**

---

## Pattern B — Autograding that assesses the approach, not just the output

**For:** CS, data-science and engineering programmes drowning in submissions.

**Wiring:** [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) (**BSD-3**) for
identical per-cohort compute → [jupyter/nbgrader](https://github.com/jupyter/nbgrader)
(**BSD-3**) for the release/collect/autograde/return lifecycle →
[ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) (**BSD-3**, default ref
`master`) for container-isolated grading at cohort scale →
[microsoft/pybryt](https://github.com/microsoft/pybryt) (**MIT**) to check **how** the student got
there, not only whether the answer matched →
[jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) (**BSD-3**) so the LLM explains
*why* the approach was wrong, inside the notebook the student is already in.

**Why this combination:** pybryt is the piece everyone misses. An LLM that reviews output rewards
the student who guessed; pybryt's annotations let you detect the *intended method* and then have the
model give feedback on the method. **Fully permissive — BSD-3 and MIT only, zero copyleft.**

🔴 🆕 `p387` **Vendor pybryt; do not install it.** PyPI `pybryt` has shipped nothing since
**v0.7.0, 2022-04-28** — four and a half years — so a client support contract cannot rest on it as a
dependency. The pattern does not change: copy the annotation approach (and, licence permitting under
its MIT grant, the code) into the deliverable and maintain it there, with the maintained BSD-3
halves of this stack (`nbgrader`, `otter-grader`) carrying the running infrastructure. Dates:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

🟢 🆕 `p388` **And the notebook-tutor half now has a maintained component, which changes what you
vendor.** [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) (**BSD-3**,
`main` · `139bb11`, **v0.3.2, 7 releases, → 2026-09-25**, from a known Jupyter-ecosystem maintainer)
replaces the ad-hoc "wire `jupyter-ai` into the grading loop" step with a component built for exactly
this job:

- A per-cell **Explain Code** button sends the cell source, the kernel language, **the error
  traceback**, and the preceding cells up to the last markdown cell **as the exercise statement** —
  so the model sees the task, not just the broken line.
- 🟢 **The tutor persona lives in a `TUTOR.md`, discovered by walking up from the notebook's
  directory to the server root.** Each course, module or folder carries its own pedagogy **in version
  control**. This is the single most useful thing on this shelf for a client engagement: *"AI must
  not give the answer"* stops being a prompt someone pasted and becomes a reviewable file in the
  course repository, diffable and auditable per cohort.
- 🟢 **`reference_solution` and `evaluation_criteria` ride in cell metadata, ROT13-encoded** so they
  are not casually readable by a student holding the notebook — the same instinct as `pybryt`'s
  annotations, shipped in a maintained package.

**Revised wiring:** `jupyterhub` → `nbgrader` → `otter-grader` for the lifecycle and
container-isolated grading (all BSD-3, all maintained) → **`jupyter-ai-tutor`** for the in-notebook
explanation layer, configured by a per-course `TUTOR.md` → **vendored `pybryt` annotations** for
approach assessment, maintained inside the deliverable as `p387` requires. 🔵 Note the division of
labour this produces, and it is the one the guardrail below wants anyway: `jupyter-ai-tutor` **explains
and never grades**, `nbgrader`/`otter-grader` grade and never explain. 🟡 It requires
`jupyter-ai-jupyternaut` (<0.1) for the agent, so pin that bound.

🟢 🆕 `p389` **And the missing third component: the mastery model.** Everything above assesses a
*submission*. Nothing in it answers the question a programme director actually asks — **which skills
has this student mastered, and what should come next** — and this base has carried that gap while
recommending a dependency that stopped shipping in 2022. The maintained answer is
[**CAHLR/pyBKT**](https://github.com/CAHLR/pyBKT) (**MIT**, real ref `master`, **last commit
2026-10-21 — 1 day**), from UC Berkeley's CAHLR, who also maintain
[**OATutor**](https://github.com/CAHLR/OATutor) (**MIT**, `main`, **1 day**) as the tutoring front end
built on it.

- **What it adds to this wiring:** fit **Bayesian Knowledge Tracing** on the client's *own*
  `nbgrader`/`otter-grader` outcome logs — one row per (student, skill, attempt, correct) — and you get
  per-skill **learn, guess, slip and forget** parameters plus a running mastery probability per student.
- 🟢 **Why it is the defensible choice and not just the available one:** those four parameters are
  **inspectable numbers a client can argue with**, re-estimated on their own cohort. "The model thinks
  Ana has not mastered partial fractions, with these parameters fitted on this data" survives a
  procurement review; "the LLM judged her weak" does not. North American and Maryland-style rules that
  bar AI from high-stakes decisions about students are satisfiable here precisely *because* the
  decision rule is a published model rather than a generation.
- **Revised wiring, end to end:** `jupyterhub` → `nbgrader` → `otter-grader` (lifecycle + isolated
  grading) → **`pyBKT`** fitted on the outcome log (mastery per skill) → **`jupyter-ai-tutor`** with a
  per-course `TUTOR.md` for in-notebook explanation → **vendored `pybryt` annotations** for approach
  assessment. 🟢 **Still fully permissive: BSD-3 and MIT only, zero copyleft.** 🔵 The sequencing
  matters: `pyBKT` decides *what to work on*, the tutor explains *why the attempt failed*, and the
  graders remain the only components that produce a grade.
- 🟡 **Cold start is the real constraint**, not the licence: BKT needs interaction history. For a new
  cohort, serve `OATutor`'s scaffolds with default parameters, log, and re-fit at the end of the first
  module — and say so in the estimate rather than discovering it in week three.

**Guardrail:** where DC-style rules apply, AI must not be the grader of record. Configure the LLM as
a **feedback generator with a human grade-of-record** and keep the audit trail; that configuration is
the deliverable, not a disclaimer. 🆕 `p389` The same rule governs the mastery model: a BKT mastery
probability is **advisory input to a human decision**, and the moment it auto-finalises anything
consequential it is the "sole basis for a decision without meaningful human review" that Vietnam's
Decision 33/2026 and EU Annex III both reach.

---

## Pattern C — Citation-grounded academic assistant (and the EU compliance story that comes free)

**For:** higher-ed research support, library services, graduate programmes.

**Wiring:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa) (**Apache-2.0**) as
the answer engine → [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar)
(**Apache-2.0**) or [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib)
(**Apache-2.0**) for multi-paper synthesis →
[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) (**Apache-2.0**)
for ingest → [LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**) as the campus gateway.
For guided-inquiry assignments, [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
(**Apache-2.0**) as the student-facing research scaffold.

**The compliance argument:** paper-qa **declines to answer** without retrieved evidence. Under
**EU AI Act Art. 50** (transparency, live from **2 Aug 2026** — *not* delayed by Regulation (EU)
2026/1744) a system that cites its sources and refuses otherwise is dramatically easier to document
than one that generates fluently. Build the refusal behaviour in, then point at it in the
conformity file. **Fully Apache-2.0/MIT.**

---

## Pattern D — Offline-first deployment for connectivity-constrained regions

**For:** LATAM, African and rural APAC deployments — including the nine countries in the Google.org
AI-literacy rollout (Argentina, Brazil, Chile, Colombia, Dominican Republic, El Salvador, Mexico,
Peru, Uruguay).

**Wiring:** [learningequality/kolibri](https://github.com/learningequality/kolibri) (**MIT**,
default ref 🔴 `develop`) as the edge runtime — offline-first by design, not a degraded mode →
a small local model on the same device for the tutoring loop →
[FSRS](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for scheduling review, because
retention is the one outcome measurable without a network →
content authored in [H5P](https://github.com/h5p/h5p-php-library) — 🟡 **GPL-3.0, keep it as
runtime content, not linked code** → periodic sync to the central LMS over
[LTI 1.3](https://github.com/Cvmcosta/ltijs) (**Apache-2.0**) when a link is available. 🆕 `p392` **Use a maintained implementation, and pick it by language — all three majors have one.** **Python:** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT, PyPI v0.10.1, HEAD 2026-10-20) **in-process** for a Django agent, or [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 BSD-3) for a JupyterHub. **Node:** `ltijs` (Apache-2.0, npm v7.0.7, 2026-10-06), or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT, npm `@lti-tool/core` v1.3.2) when the target is **Lambda or Cloudflare Workers**. **PHP:** `packbackbooks/lti-1p3-tool` (Apache-2.0, packagist v6.4.4). 🔴 **Not** the standards-body copy `p390` cited (2,333 days stale) and **not** `pylti1.3` (1,431 days) — but `p391`'s conclusion from that second fact, *"a Python agent sits behind a Node or PHP edge rather than speaking LTI itself"*, is **withdrawn**: `Gap 391-A` is closed and the extra service comes out of the budget.

**Why FSRS matters here:** it has published parameters, so "the student is retaining more" is a
number you can defend to a ministry, offline, without telemetry.

🟢 🆕 `p389` **Two components that remove a server from this pattern, which is the cost line that
actually kills offline deployments.**

1. **Lesson delivery with no application server at all.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT**, committed **0 d**) exports a
   finished classroom as **one self-contained offline HTML file that plays the lesson** (or as a PPTX
   that keeps every scene). 🔵 **So the authoring server and the delivery target separate cleanly:**
   generate lessons once where there is power and bandwidth — a ministry office, a regional hub, a
   studio — and ship HTML files to the edge, where they need nothing but a browser. That is a
   fundamentally cheaper edge than "a Kolibri server per school", and the two compose: Kolibri remains
   the catalogue, progress store and sync layer; the exported HTML is the content it serves. 🟡 The
   export is a *playback* artefact — the agentic mid-lesson chat needs the server — so scope it as
   narrated, interactive courseware, not as a tutor that answers back offline.
2. **Notebook exercises with no per-student compute.**
   [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) (**BSD-3**, 6 d) runs the
   kernel **in the browser via WebAssembly**: no container, no install, no server, and it works offline
   once the page is cached. For a CS or data-science module this deletes the single largest
   infrastructure line in `Pattern B` at the edge. 🟡 No server also means no server-side autograding —
   collect the notebook and grade it with `nbgrader` when a link is available.

🔵 **What this pattern now says to a ministry.** The old answer was "a server per school, syncing when
it can." The 2026 answer is **generate centrally, deliver as files, compute in the browser, sync
progress when a link exists** — and every component in it is MIT or BSD-3, so the ministry owns the
deliverable outright. 🔴 One licence caution unchanged: H5P content stays **runtime content** under
GPL-3.0, never linked code.

---

## Pattern E — Sovereign EMEA public-sector stack

**For:** European public-sector clients demanding both data sovereignty and code ownership.

**Wiring:** **[OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, default ref `master`)**
as the platform — **the only major open-source LMS a studio can extend with closed code** →
[serlo/serlo.org](https://github.com/serlo/serlo.org) (**Apache-2.0**) or
[oppia/oppia](https://github.com/oppia/oppia) (**Apache-2.0**, default ref `develop`) for structured
content → [openfun/richie](https://github.com/openfun/richie) (**MIT**, default ref `master`) as the
public catalogue → permissive agents over LTI 1.3 → all EU-hosted.

**The alternative, when the client insists on the openDesk lineage:** **ILIAS (GPL-3.0, default ref
`release_11`) + OpenProject behind a single SSO** — the ZenDiS pattern, and ZenDiS co-develops with
France's DINUM (LaSuite). 🔴 **But do not quote "8,600 schools":** that figure traces to a single
news item, and this pass found **no school deployment of openDesk in any source**. Named users are
administrative bodies. Sell the architecture, not the number.

**Dated compliance roadmap to attach to the bid** — this is the part competitors get wrong:
| obligation | when | status |
|---|---|---|
| Art. 4 AI literacy (every organisation using AI) | **since 2 Feb 2025** | 🔴 already binding |
| Emotion recognition in education | **prohibited since 2 Feb 2025** | 🔴 design it out |
| Art. 50 transparency | **from 2 Aug 2026** | 🔴 **not delayed** |
| Stand-alone high-risk education systems (admissions, assessment, proctoring, AI-detection in assessment, path-steering personalisation) | **2 Aug 2026 → 2 Dec 2027** per **Regulation (EU) 2026/1744** (OJ 24 Jul 2026) | 🟢 14 months of runway |

---

## Pattern F — Teacher-facing instructional assistant (the pattern the market and the regulator agree on)

**For:** LATAM and ANZ especially, where student-facing generative AI is either commercially
unproven or politically restricted.

**Wiring:** [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) for lesson plans,
quizzes and question banks → [openedx/edx-ora2](https://github.com/openedx/edx-ora2)
(**AGPL-3.0**, run as the platform's own service) for rubric-based open-response assessment with
the human grade-of-record → [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (**MIT**) so the
prompt pipeline has a metric attached instead of being hand-tuned →
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) (**LGPL-3.0**, default ref
🔴 `19.0`) where the administrative record has to move too.

**Why it sells:** HolonIQ's 2026 LATAM EdTech 100 finds regional AI concentrated in **teacher-facing
instructional tools rather than consumer tutoring**; Brazil's PL 2.338/2023 reportedly targets
**student selection**; DC bans AI in grading, discipline, IEP and teacher evaluation; ANZ shows the
highest ban support in the Ipsos 2026 data. **Teacher-facing-only must be an architectural switch,
not a retrofit.**

---

## Pattern G — Provenance and labelling in the generation path (APAC, overdue)

**For:** anything shipped into **India** (amended IT Rules: prominent labels **and provenance
markers** on AI-generated content from **20 Feb 2026**) or **China** (AI-content labelling measures
applicable from **1 Sep 2025**; 988 services filed by 30 Jun 2026).

**Wiring:** label and sign **at generation**, not at display — every artefact an education agent
emits (generated question, feedback text, summary, image) carries a label and a provenance record
from the moment it is created; the LMS stores the record alongside the artefact (Moodle web services
/ MCP, Canvas API) so an audit can reconstruct what was machine-made months later; the student-facing
surface renders the label rather than deriving it.

**Why it is a build, not a memo:** if labelling happens in the UI, every export, API call and
copy-paste strips it. The requirement is on the content, so the marker belongs in the content
record. Most tutoring products shipped into IN/CN today do not do this and are already out of time.

---

## Pattern H — 🆕 `p384` Prerequisite-aware tutoring, grounded on a curriculum graph you must **not** fork

**For:** the adaptive-learning engagement everyone pitches and nobody can substantiate — "the tutor
knows what the learner is missing". The missing ingredient was never the model; it was a
machine-readable map of what must be mastered **before** the next topic. One now exists.

🔴 **Read this first.** [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
is licensed **ODbL** (`main/LICENSE`, 25,289 B), a **share-alike database licence**, and it has
**no code grant**. The whole pattern is built around keeping it on the right side of §4.4:

| what you do | ODbL clause | obligation |
|---|---|---|
| Tutor **output** grounded in the graph — next-topic choice, lesson plan, explanation, diagnosis | **§4.3** *Produced Work* | 🟢 **Attribution notice only.** Nothing to release. ODbL supplies the wording: *"Contains information from DATABASE NAME, which is made available here under the Open Database License (ODbL)."* |
| Shipping the graph **extended or merged** — client topics added, standards remapped, graph re-cut | **§4.4** *Derivative Database* | 🔴 **Share-alike.** Must be publicly used only under ODbL / a later ODbL / a compatible licence. §4.4(b): extracting *"the whole or a Substantial part of the Contents into a new database"* **is** a Derivative Database. |

🟢 **So the architectural rule is one sentence: join, never merge.** The client's curriculum data
stays in the client's own store; the taxonomy stays a read-only input resolved at query time. Break
that rule and the client's curriculum map becomes an ODbL obligation.

**Wiring:**
1. **Load the graph read-only, in its own store.** `data/topics.json` (1,930 micro-topics, each with
   a plain-language description, mastery **evidence** criteria, a type — conceptual / procedural /
   representational / language / meta — subject, domain and an approximate age range) and
   `data/dependencies.json` (4,102 edges, `topicId` → `prerequisiteId`, each tagged `hard`/`soft`
   with a one-line reason). 🔵 Keep it in a **separate schema or database** from anything client-
   specific, and never write client rows into it — that separation *is* the §4.4 firewall, and it
   should be visible in the deployment diagram so counsel can see it.
2. **Map the client's own curriculum to it by reference, not by insertion.** A join table
   `client_objective_id → topicId` in the **client's** store. The taxonomy's standards alignments
   (**NGSS, Common Core, UK National Curriculum**, Australian curriculum — Mathematics 442
   alignments across 325 topics, English 630/267, Science 245/131, HASS 210/124) usually give you
   the hook. 🟡 Unmapped client objectives are a **finding to report**, not a gap to paper over.
3. **Diagnose with the graph, not with the model's intuition.** Walk the DAG backwards from the
   failed topic over `hard` edges to find unmet prerequisites. This is a **graph traversal, not a
   generation** — deterministic, inspectable, and the reason the pattern can survive an audit that
   a pure-LLM "diagnosis" cannot. Treat `soft` edges as ranking hints only.
4. **Attach the tutor.** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (**Apache-2.0**) for
   persistent learner memory plus RAG over the learner's materials, with the traversal result from
   step 3 injected as the lesson objective. Teacher-facing variant: feed the same unmet-prerequisite
   list to [satvik314/educhain](https://github.com/satvik314/educhain) (**MIT**) to draft the
   remediation worksheet — which is the side of the market that is actually growing (Trend 5).
5. **Schedule the retention.** [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki)
   (**MIT**) over the mastered topics. The graph says *what* to review next; FSRS says *when*, with
   published parameters. 🟢 Together they make "personalisation" two measurable quantities instead
   of a claim.
6. **Deliver it through the client's existing LMS**, per **Pattern A** — `webservice_mcp` for
   Moodle, [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (**MIT**) for Canvas. For
   K-12 student records, [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (**GPL-2.0**,
   ref `master`) over its API — never linked.
7. **Prove it on the prerequisite claim specifically.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   [GSM8K](https://github.com/openai/grade-school-math) (**MIT**) for the multi-step maths chain.
   🟢 The honest measurement here is not a headline score: it is **whether remediating the
   prerequisite the graph identified improves the dependent topic**. That is an A/B the client has
   never been offered, and it is the whole value of the pattern.
8. **Ship the attribution notice.** §4.3 costs one line in the product's about page and the
   documentation. Put it in at step one; retrofitting a notice after a client review is avoidable
   embarrassment.

🟡 **Scope the research claim honestly.** The taxonomy's teaching-research payload
(`data/teaching-research.json`, ~24 MB) covers **1,049** topics — Science and Mathematics — and the
maintainers state that **881 topics have no research in this release**. "Research-backed guidance"
is true for roughly half the graph. Check which half a client's subject mix lands in **before** the
claim reaches a deck.

🔵 **Coverage note:** `v1` is primary/elementary and strongest on the Australian and US/UK
standards. Secondary and vocational curricula are not covered — for those, this pattern is the
*shape* to build, with the client's own map in place of the taxonomy.

**Licence posture:** client-owned code is MIT/Apache throughout. Two non-permissive components, both
held at arm's length: the **taxonomy** (ODbL, read-only input, joined never merged — §4.3 notice
only) and the **LMS/SIS** (GPL, reached over a published protocol). **Deliverable stays closed.**

---

## Pattern M — 🆕 `p385` The agent-native classroom (when the client has **no** LMS to bolt onto)

**Pattern A inverts the usual build: an agent over the client's existing LMS. Pattern M is for the
engagement where there is no LMS worth integrating** — corporate L&D, a bootcamp, a professional body,
a ministry pilot — and the deliverable is the learning loop itself, not a Moodle plugin.

**The shape.** The classroom is an **MCP server**; the agent is bring-your-own and replaceable. That
inversion is what makes it worth a pattern: the client is not buying a model, so a model swap (or a
provider outage, or a procurement decision two years out) does not invalidate the asset.

| layer | component | licence | why this one |
|---|---|---|---|
| Classroom / state | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 AGPL-3.0 (`main`) · 🟢 MIT at `v0.1.0` | ~50 MCP tools over courses, lessons, graded exercises and a persistent learner memory. Read **Pattern L step 10 before you pick a ref** — this decision is the whole procurement question |
| Retention scheduling | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 MIT | learn-shell schedules flashcards with FSRS already; use the upstream parameters so retention is a published model, not a vendor claim |
| Course material ingest | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | 🟢 Apache-2.0 | the client's PDFs, DOCX and slide decks are the corpus |
| Grounding | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 🟢 Apache-2.0 | document-aware retrieval over that corpus |
| Measurement | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 MIT | the before/after on the client's own subject mix, which `intel/trends.md` Trend 2 makes a procurement precondition |
| Gateway / audit | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | per-user quota and an audit log, which is what gets it past a DPO |

**Wiring.** The agent reaches learn-shell over MCP (JSON-RPC), exactly the boundary Pattern A uses to
stay clear of Moodle's GPL — so the agent code and the prompt/curriculum assets stay the client's.
`unstructured` → `ragflow` builds the grounding index; the agent writes lessons, exercises and
flashcards **into learn-shell** so the evidence of teaching outlives the context window; FSRS decides
what comes back and when; `lm-evaluation-harness` runs the before/after.

🔴 **Three things to say out loud in the pitch, because they are real:**
1. **AGPL reaches hosted use.** If you deploy `main` for the client as a service, the AGPL obligations
   attach to the deployment. The MIT `v0.1.0` tag avoids that and costs you every fix since
   2026-08-16. There is no third option, and this is the decision, not a detail.
2. **v1 is single-machine and unauthenticated by the maintainer's own description.** It is a pilot
   substrate. Multi-tenant auth, isolation and backup are *your* scope — budget them, do not discover them.
3. **It is one maintainer's project.** Weigh that against what it replaces: the alternative is building
   course/lesson/exercise/memory state from scratch, which is the part of this pattern nobody costs correctly.

🔵 **When NOT to use this.** If the client already runs Moodle, Canvas or Open edX, **Pattern A is
strictly better** — the learner records, rostering and gradebook already exist and integration beats
migration. Pattern M is for a greenfield loop, and its honest competitor is not an LMS but a spreadsheet.

## Pattern N — 🆕 `p386` Harden a student-side LMS MCP server into one an institution can deploy

**When to use it.** The client runs **Blackboard, D2L/Brightspace, Canvas or Moodle** and wants an
agent over it. As of `p386` there is a granted community MCP server for **every** one of those
platforms (see [`agents/top.md`](../agents/top.md#the-blackboard-and-d2l-supply-measured)) — so this
is never a greenfield build. 🔴 But **11 of the 12 granted Blackboard/D2L servers authenticate as the
signed-in student**: they ride the user's own browser SSO session, hold whatever rights that user
holds, and have no audit trail. **Licence-clean and still undeliverable.** This pattern is the gap
between the two.

**The parts.**

| role | pick | licence | why this one |
|---|---|---|---|
| Blackboard, institution-grade start | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 MIT | The only server on these shelves that targets the **official Blackboard Learn REST API** and claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrub and a JSON audit log. 🟡 Self-claims — **verify by execution before you quote them** |
| D2L start | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | 🟢 MIT | Multi-strategy auth (TOTP/OAuth/browser), retry + circuit-breaker + cache, **opt-in** writes. The nearest thing to a hardening base on D2L |
| Canvas start | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | 🟢 MIT | The clean default; [mdweaver](https://github.com/mdweaver/canvas-mcp) fork adds office hours and syllabus write |
| Moodle start | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 🟡 GPL-3.0-or-later, header-granted | First-party route: it is in **Moodle's own plugin directory**, and the agent reaches it over JSON-RPC so GPL never reaches the agent — **Pattern A**'s boundary |
| Identity / gateway | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | SSO, per-user quota and the audit log that gets a deployment past a DPO |
| Jurisdiction gate | [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) | — | A granted licence does not make **grade write-back** lawful where you are deploying it |

**The work, in order — this is the whole deliverable.**

1. **Replace the session with a service identity.** Swap browser-session auth for the platform's
   own OAuth2 / API-key flow against a **service account scoped to the courses in scope**. If the
   chosen server cannot do this (most cannot), this step is a fork, and it is the reason the
   engagement exists.
2. **Scope by role, server-side.** Student / instructor / admin tool sets, enforced in the server,
   never in the prompt. A model that *can* call `update_grade` and is *asked not to* is not a
   control.
3. **Split read from write, and default write off.** Ship read-only first; put every mutation behind
   an explicit per-deployment flag. `JhostinAleck/brightspace-mcp`'s opt-in-writes design is the
   shape to copy.
4. **Gate grade write-back on the jurisdiction, before any code.** Several jurisdictions in the
   policy matrix gate or prohibit automated grading outright — Oklahoma and Maryland bar AI from
   high-stakes student decisions, the EU AI Act puts assessment in Annex III high-risk, Vietnam
   names automated assessment explicitly, and Illinois SB 2909 reaches *teacher* evaluation. 🔴 This
   gate decides the product's tool list, so run it in week one, not at security review.
5. **Add an audit trail that answers a DPO's actual question**: who (service identity + end user),
   which tool, which course, which record, when, and what the platform returned. Structured JSON to
   the client's existing log sink.
6. **Pin the contract, not the login page.** Pin the vendor API version and put contract tests
   around the tools you use; a student-side server breaks silently when the vendor restyles SSO.
7. **Carry the attribution the payload actually requires** — per **Pattern L step 11**. If you
   started from a fork-family server, the NOTICE file may owe **two** credits.
8. **Prove it before handover.** Execute the maintainer's claims rather than quoting them: run the
   role gate against an under-privileged token, confirm the audit record exists for every mutation,
   and confirm the PII scrub on a real transcript.

🟢 **Why this sells.** It is small, bounded, and the client can show the output to their
data-protection officer — and it is available on every major LMS today, because the licences are
already clear. 🔴 **Say the honest part too:** on D2L all six granted servers are student-side, so
step 1 there is a genuine build and should be costed as one, not as a configuration.

## Pattern O — 🆕 `p387` The LATAM engagement, built on what the region already shipped

**For:** a Brazilian or Spanish-speaking LATAM client — ministry, municipality, university or
school network — where the deliverable has to be in the local language, aligned to the *national*
curriculum, and deployable by an institution rather than demoed to one.

**The premise this pattern corrects:** the LATAM supply is not empty. Every component below is a
real address with a grant read first-hand on 2026-10-22.

**Wiring, Brazil (the fully-specified case):**

1. **Start from the national curriculum, not from a prompt.**
   [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores)
   (**MIT**, `main`) already anchors generation to **BNCC** skill codes and **discards an invented
   code before the teacher sees it**. Keep that gate and extend it: the gate *is* the trust story,
   and it is the same mechanism `Pattern H` specifies against a curriculum graph.
2. **Deliver through the LMS the client runs, never a new portal.** On **Moodle**, the
   `webservice_mcp` plugin per **Pattern A**; on **Open edX**, start from
   [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (**MIT**, `main`), which is already an
   XBlock/plugin with a teacher statistics panel, TTS and cross-session context.
   🔴 **Licence boundary, non-negotiable:** TutorIA's MIT grant covers *the plugin*. Open edX is
   **AGPL-3.0** and hosting it is hosting AGPL software. Keep the agent a **separate service** the
   plugin calls over HTTP, keep the plugin thin, and the client's AGPL obligations stay exactly
   where they were before you arrived.
3. **Integrate the student-record system over its API.**
   [portabilis/i-educar](https://github.com/portabilis/i-educar) (**GPL-2.0-or-later**, real default
   ref **`2.12`**) is what a Brazilian municipality is running. Read rosters and write results
   through its API; **do not fork it** — the fork pulls GPL into the deliverable and buys nothing.
   (Its sibling `i-diario` is AGPL-3.0; check per repository, not per organisation.)
4. **Make it multi-tenant before anyone calls it a pilot.** A school network is many tenants. On
   Moodle, [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
   (**GPL-3.0-or-later**, in `version.php`) supplies exactly this — per-role provider routing, rate
   limits, per-tenant enable/disable, usage monitoring — and it reaches the agent over its own API,
   so the copyleft stays on the Moodle side. On Open edX, build the tenant boundary per
   **Pattern N** steps 1–5.
5. **Run it where connectivity is the constraint**, which is the actual deployment profile for
   TutorIA's own users (rural Risaralda) and for most of the nine Google.org rollout countries:
   [Kolibri](https://github.com/learningequality/kolibri) (**MIT**, default ref `develop`) per
   **Pattern D**, with a local open-weight model behind the AI manager's **Ollama** tool rather than
   a metered API.
6. **Schedule retention, in the local language.**
   [fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) (**MIT**) for the scheduler; the
   content language is a data property, not a code property, so this layer ports unchanged.
7. **Measure in the language of instruction, and publish the baseline.**
   [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (**MIT**) with
   Portuguese/Spanish task sets built from the client's own past assessments. 🔴 Do **not** ship an
   English benchmark number as evidence for a Portuguese deployment.
8. **Say out loud what you are adding.** The agents exist and are MIT; **tenancy, support,
   governance and curriculum QA are the deliverable.** That is a defensible studio pitch and an
   honest one — and it is cheaper for the client than the rebuild a "no LATAM supply" story implies.

**Spanish-speaking variant:** swap step 1's BNCC grounding for the client's national curriculum
standard, keep TutorIA (Spanish-first) at step 2, and use
[academico-sis/academico](https://github.com/academico-sis/academico) (**MIT**, Spanish built in) or
[Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) where no SIS/LMS is in place.

🟡 **Two addresses this pattern deliberately does not use, and why.**
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru) is the
offline-first PWA tutor with explainable difficulty selection that step 5 would otherwise want — it
has **no grant at any of eight probed paths**, so it cannot enter a deliverable, and asking its
author to add a licence is the cheapest possible contribution to the region's supply.
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref `master`) is ungranted for the same reason.

---

## Pattern P — 🆕 `p388` The parent and guardian surface (and the FERPA line that splits it in two)

**For:** a K-12 district, school group or education provider that is being asked — by statute, by
families, or by its own board — to make a student's progress legible to parents, and an engagement
that wants a real deliverable rather than another policy PDF.

🔴 **Read this first: this is two different products, and conflating them is how the engagement
fails.** The code is the same; the obligations are not.

| | **P-1 · parent-side** | **P-2 · district-side** |
|---|---|---|
| Who holds the credential | the **parent**, for their own child | the **institution** |
| What a read is | a parent exercising their own access | a **FERPA-governed disclosure of an education record** |
| Tenancy | none needed — single user, single family | **full multi-tenant**, per-district, per-role |
| Who buys | a provider bundling it, or nobody (it is a tool, not a sale) | the district, through procurement |
| Build cost | days | the real engagement |

**Components (all verified first-hand 2026-10-22 — [`verified-repos`](../evidence/verified-repos.2026-10-22-p388.tsv)):**

- **Infinite Campus (SIS):** [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp)
  — `main` · `971d58f`, 🟢 **MIT** (1,067 B), **47 npm releases → 2026-10-19**. 20 tools over **Campus
  Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent window, **attendance
  events with codes and comments**, behavior, food service, documents, standardized **assessment
  scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via
  **CUPS SSO**; `FeatureDisabled`-aware, so a district with a module switched off degrades instead of
  erroring — which is what makes it deployable across a group of districts rather than one.
- **Canvas (LMS):** [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
  — `main` · `428b78b`, 🟢 **MIT** (1,067 B), **43 releases → 2026-10-16**. 18 `canvas_*` tools held
  to the **read-only observer scope** (`canvas_list_observees` is the hinge), plus student
  self-access. Four auth modes in priority order. 🟢 Copy its download hardening rather than
  re-inventing it: host-pinned to the Canvas origin, confined to a download directory, never writes
  through a symlink, new files `0600`.

### Wiring P-1 (parent-side) — days, not weeks

1. Parent installs the MCP server locally against **their own** portal credential (token, OAuth, or
   session). Nothing is hosted; no institutional agreement is needed because no institutional
   credential is used.
2. Keep it **read-only**. Both servers are already scoped that way; do not add write tools. A parent
   agent that can submit work on a child's behalf is an academic-integrity incident waiting to be
   filed.
3. Add a **digest** rather than a chat surface: *"what changed this week, what is missing, what is
   due."* 🔵 The persona's actual job is **noticing**, not conversing — the portal already answers
   questions, badly, and nobody logs in.

### Wiring P-2 (district-side) — the real engagement

1. 🔴 **Do not host the parent-side tool for the district.** The moment the credential is
   institutional, every read is a FERPA disclosure. Build the institutional path deliberately:
2. **Put the district's own identity in front of it.** Parent identity comes from the district IdP,
   and **the parent↔student relationship is authoritative from the SIS** — never from a claim the
   agent accepts. `ic_list_students` / `canvas_list_observees` define the blast radius of the whole
   system, so that relationship check is the security boundary, not a feature.
3. **Borrow the tenancy layer that already exists.** This is the same problem `p386` identified for
   student-side LMS servers, and `Pattern A`'s answer applies unchanged: per-tenant configuration,
   per-role rate limits and usage monitoring — on Moodle,
   [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) is the
   worked example to copy the *shape* of.
4. **Log every read as a disclosure, not as a request.** Who asked, for which student, which fields,
   under which relationship, at what time. 🔵 This log is the deliverable a district's counsel signs
   off on, and it is cheap to build on day one and near-impossible to retrofit.
5. **Keep the model away from the record where you can.** Fetch and render deterministically;
   use the model for **summary and prioritisation over data already authorised**, not as the thing
   that decides what to fetch. Smaller surface, smaller disclosure, cheaper review.
6. **Ship the translation layer — it is the actual product.** Gradebook rows are not an answer to
   *"is my kid okay?"* Convert to plain language, in the family's language, at a reading level the
   district specifies, with **no inference about the child beyond what the record states**. A tool
   that volunteers *"your child seems disengaged"* has invented an education record.

**Guardrails:**
- 🔴 **No predictions, no risk scores, no labels.** A parent-facing risk score about a student is
  the high-stakes automated decision Oklahoma and Maryland's frameworks are written to restrain, and
  under the EU AI Act Annex III it is squarely high-risk. Report the record; do not score the child.
- 🔴 **Attendance, behavior, food-service and fee data are the sensitive tail.** `infinitecampus-mcp`
  exposes all four. Free-lunch status and behavior records are the fields a district will refuse last
  and worry about most — scope them out explicitly unless the district asks for them in writing.
- 🟡 **Both servers authenticate as a person.** Treat credential custody as the top risk in the
  design review; a stored parent credential in a studio-hosted service is the worst of both worlds.
- 🔵 **Multiple children, multiple districts.** `ic_list_districts` + CUPS SSO exist because families
  span districts. Test the two-children-two-districts case before a demo; it is the common case and
  the one that breaks naive implementations.

**Why this pattern is worth having at all:** it is the only education surface this base has found
with **granted, maintained components and no incumbent vendor** — the parent portal is a feature of
the SIS, not a market. And **family transparency is already in the statutes** (Oklahoma SB 1734
names it; Maryland's Chapter 634 is built on guidance districts hand down), so the buyer has an
obligation and no product. 🔵 See `Trend 10` in [`intel/trends.md`](../intel/trends.md).

---

## Pattern Q — 🆕 `p389` The generated classroom, governed (and what it supersedes in `Pattern M`)

**For:** a client with **no usable LMS** — a corporate academy, a ministry training programme, a
vocational provider, a new institution — who needs **teachable lessons in weeks, not a platform in
quarters**. Also the fastest credible answer to the EMEA teacher-training demand recorded in
[`intel/market.md`](../intel/market.md): the UAE has **22,000 teachers and education professionals**
to train on a curriculum that became compulsory by Cabinet decision.

**The base:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT** (read from the
payload at `main` @ `269fde2d991f`; `package.json` agrees), Tsinghua University, **committed
2026-10-22**, ~41.3k ★, **JCST 2026** paper, grown out of the internal **MAIC** system and validated
on **700+ students**. 🔴 **Pin `v1.2.1` (2026-10-18), not head.** Head is `v1.3.0-rc.1`, and the
project states breaking upgrade conditions with **no rollback below that release** — a pilot does not
want to be the first to find that out.

### Wiring

1. **Stand up the authoring server.** Node ≥ 22.19, pnpm ≥ 10, **PostgreSQL 16**, a long-running
   server (🔴 **not Vercel** — Vercel deployments are capped at the 1.1.x line, so "we'll host it
   serverless" is a downgrade). Generation is **server-first** from v1.2.0: it survives closed tabs and
   restarts, which is what makes it usable by teachers rather than by engineers.
2. **Write the governance file first, before any content.** `openmaic.yml` declares **providers** and
   assigns every AI use — a named **slot** (`llm`, `course.outline`, slide content, TTS, web search,
   `video`) — to one of them, with keys referenced as `${VAR}` from `.env.local`. 🟢 **Three settings
   are the compliance deliverable, not configuration:** pin each slot to the provider under the
   client's own contract; set the server to **forbid user-supplied keys**, so no teacher can route
   student work through an unvetted account; and set unused capabilities to `null` rather than leaving
   them available. 🔵 **This file is the artefact that answers a district's or ministry's AI policy
   question** — *which model saw student input, under whose contract* — in one reviewable, diffable
   page. Almost nothing else in this base can answer it at all.
3. **Ground the content in the client's curriculum, not in the model.** Feed the jurisdiction's own
   material through the **knowledge base** (v1.3.0 line) or as per-course uploads — parsed once and
   reused — and where a standards graph exists, drive the lesson plan from it rather than from a
   prompt: [`os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) (🔴 **ODbL-1.0 — a database
   licence; reach it over a service, do not fork it into the deliverable**, per `Pattern H`), or
   [`bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) (**MIT**) for a
   North American engagement — 🟡 whose crawl is **209 days** old, so budget the re-crawl its MIT grant
   permits.
4. **Keep the record of record outside it.** 🔴 OpenMAIC has **no enrolment, no gradebook of record,
   no transcripts and no stated LTI story**. Pair it with the administration base the client already
   runs or should: [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) (GPL-2.0, over its API),
   [academico](https://github.com/academico-sis/academico) (**MIT**) at SME scale,
   [i-educar](https://github.com/portabilis/i-educar) (ref `2.12`) for Brazilian municipal work, or
   [OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0) where an ERP is wanted.
   **Completion and scores flow out of OpenMAIC into that system; identity and enrolment flow in.**
5. **Add the mastery model it does not have.** Quiz results are events, not a mastery estimate. Fit
   [`pyBKT`](https://github.com/CAHLR/pyBKT) (**MIT**, 1 d) on the quiz log per skill, as in the
   revised `Pattern B`, and use it to choose the next lesson. 🟢 This is also what keeps the
   high-risk-assessment line on the right side: the progression decision becomes **a published model
   plus a human review step**, not a generation.
6. **Deliver to the edge as files.** Export each finished classroom as **one offline HTML file** (or
   PPTX). See `Pattern D` — authoring stays central, delivery needs only a browser.
7. **Run the models where the data has to stay.** **Lemonade** for local inference and **FunASR** for
   local ASR are supported paths, not forks — so a deployment that may not send audio or text
   off-premises is a configuration change.

### Why this supersedes `Pattern M` for institutional delivery

`Pattern M` is built on [learn-shell](https://github.com/sf-shenfeng/learn-shell), whose v1 is
explicitly **single-machine and unauthenticated**, and whose grant is **AGPL-3.0 at `main`** (MIT only
at tag `v0.1.0`). That is a fine shape for an individual learner and an impossible one for an
institution. OpenMAIC is **MIT at head**, server-first, multi-user, with central model governance and
a published security practice — five releases since September 2026 carrying SSRF, DNS-rebinding,
token-expiry and provider-redirect fixes under **GHSAs**. 🔵 **Keep `Pattern M` for the
bring-your-own-agent, one-learner case; use `Pattern Q` whenever a client is the buyer.**

### Guardrails

- 🔴 **Auto-graded quizzes are the regulated surface.** Assessment is **Annex III high-risk** in the
  EU and named explicitly in **Vietnam's Decision 33/2026/QD-TTg**. The trigger in both is a decision
  taken on the system's output **without meaningful human review**, so ship the human review step for
  anything consequential and keep its audit trail. A practice score is not consequential; a module
  pass that gates progression is.
- 🔴 **Simulated classmates must be labelled.** An AI teacher with a voice and AI peers in a classroom
  is exactly the surface **EU AI Act Art. 50** transparency and China's labelling rules address, and
  `Pattern G` already covers the mechanics. Label in the UI, not in the terms of service.
- 🟡 **Generated content is a draft until a teacher signs it.** The 2026 procurement trend is evidence
  of instructional benefit; a lesson nobody reviewed cannot be put in front of a class at a client's
  reputational risk. Make teacher review a workflow state, and bill it — it is the part of the
  engagement that is actually about teaching.
- 🟡 **Language and regional fit:** interface is **EN + zh-CN** and the provider catalogue is built for
  a market that includes DeepSeek and Kimi. For a Gulf or LATAM engagement, **localisation of the
  teaching surface is a line item**, and there is no Arabic-first alternative in the open-source supply
  (see `intel/market.md`, EMEA).

---

## Pattern V — 🆕 `p390` The spoken tutor, and the two things that make or break it

**For:** learners who cannot or will not type their way through a lesson — early grades, low typing
fluency, shared-device households, visually impaired learners, and language learning where
*pronunciation is the skill being assessed*. This is also the pattern that reaches the LATAM and
APAC households `Trend 10` describes, where the phone is the only device.

**Why it is a separate pattern:** a voice tutor is not a text tutor with TTS bolted on. Two
properties decide whether a child keeps talking to it, and neither is in the LLM:

1. **Turn-taking.** The tutor must know when the learner has stopped speaking, tolerate a
   four-second pause while a 9-year-old thinks, and **stop talking the moment it is interrupted**.
2. **Latency budget.** Past roughly a second of silence the learner starts talking over it, and the
   session degrades into collision recovery.

**Wiring:**

1. **Do not write the voice loop.** [`livekit/agents`](https://github.com/livekit/agents)
   (🟢 **Apache-2.0**, dated 2026-10-22) is the substrate: full-duplex WebRTC transport, pluggable
   STT/LLM/TTS, **turn detection, interruption and barge-in handling**. All three legs are
   provider-swappable, which is what makes step 4 possible.
2. **Start from the working reference.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent)
   ("Manu", 🟢 **MIT**, dated 2026-10-07) is a pt-BR maths tutor on exactly that substrate, scaling
   its explanation from 1st grade to university. 🔴 Its README says **"in development" with no public
   deployment** — take the pipeline and the prompt-scaffolding, not a production claim.
3. 🔴 **Put a symbolic checker behind any arithmetic.** Manu's correctness layer is the LLM itself.
   For a maths tutor that is the one unacceptable gap: route every numeric or algebraic claim through
   SymPy (or the client's own CAS) and have the agent *read back* the verified result. A spoken wrong
   answer is harder for a learner to catch than a written one — there is no transcript to re-read.
4. **Localise the ASR, not just the prompt.** Accent and dialect coverage is where regional voice
   tutors fail. [`mozilla/common-voice`](https://github.com/mozilla/common-voice) ships **CC0-1.0**
   corpora across ~130 language variants (pt-BR, es-419 variants, Hindi, Bengali, Kiswahili) — use
   them to *evaluate* candidate ASR models on the client's actual learner population before picking
   one, and to fine-tune where the gap is real. 🟢 CC0 means no attribution and no share-alike, so
   this is safe in a commercial deliverable. 🟡 MPL-2.0 covers the **platform code**, not the corpora.
5. **Keep the mastery model outside the voice path.** Voice is an I/O channel, not a pedagogy.
   [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (🟢 MIT, dated 2026-10-22) holds the Bayesian
   Knowledge Tracing state so "what comes next" survives a dropped call and stays inspectable — which
   is also what makes the decision auditable under step 6.
6. 🔴 **Voice raises the compliance stakes, so settle three things before the pilot.**
   - **Biometrics.** A voice recording is biometric data under GDPR Art. 9 and most LATAM regimes
     (Brazil's LGPD included). Default to **transcribe-and-discard**, keep no audio unless the client
     has a lawful basis and a retention policy, and write that down.
   - **Emotion inference is prohibited in EU education** (AI Act, in force since 2 Feb 2025) — and
     voice is the modality vendors are most tempted to infer affect from. Do not ship it in EMEA,
     and strip it from any upstream SDK feature you enable.
   - **Disclosure.** AI Act Art. 50 applies from **2 Aug 2026**: a synthetic voice must be
     disclosed as synthetic. Say it in the first turn, in the learner's language, every session.
7. **Measure it as a tutor, not as a demo.** Score the *transcripts* with
   [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
   (🟢 MIT) on the client's own item bank, and track interruption rate and mean response latency
   alongside learning gain — a tutor that is pedagogically right and 1.5 s slow will still be
   abandoned.

**Licence position:** Apache-2.0 substrate + MIT reference + CC0 data + MIT mastery model — the whole
chain is permissive, so this pattern can ship as a closed client deliverable with attribution only.

**What this pattern does not solve:** there is **no granted, maintained open-source voice tutor for
an African or South Asian language** on these shelves. See `Gap 390-A`.

## Pattern W — 🆕 `p391` Qualify the district *before* the pitch (North America)

**For:** a North America K-12 engagement, at the stage before anyone has written code — choosing
which districts to approach, and pricing a pilot against a budget that actually exists. Every other
pattern here answers *what to build*; this one answers *for whom, and with whose money*.

**Why it is a pattern and not a sales note:** US school AI spending is not discretionary in the way
enterprise AI spending is. It comes from identifiable federal, state and local lines, and the
largest flexible federal line — **Title I** — is allocated on **Census child-poverty counts**, not
on enrolment. A pilot proposed without that number is priced blind, and a district with a high
poverty count and a low per-pupil spend is a different conversation from the inverse.

**Wiring:**

1. **Pull the universe.** [`pipeworx-io/mcp-education-data`](https://github.com/pipeworx-io/mcp-education-data)
   (🟢 **MIT**, HEAD 2026-10-21) — `education_find_districts` for a state returns every local
   education agency with its **LEA id**, school count, enrolment and teacher counts. The `leaid` is
   the join key for everything below.
2. **Add the budget.** `education_district_finance` on that `leaid` returns revenue split
   **federal / state / local** and expenditure by function, with **per-pupil spending computed**.
   🔴 **The survey lags the directory by 1–2 years** — quote it as "FY-whatever per-pupil", never as
   current-year, or the first CFO in the room ends the meeting.
3. **Add the federal lever.** `education_child_poverty` returns Census **SAIPE** counts and rates of
   children 5–17 in poverty by district — the figures Title I formulas run on. High poverty rate plus
   low per-pupil spend identifies districts with *federal* money and *no* incumbent vendor: the
   cheapest pilot to land and the hardest to displace later.
4. **Add the surface.** `education_find_schools` carries **charter/magnet status, grade range and
   free/reduced-price lunch counts** per school, so the pilot can be scoped to named schools rather
   than to a district abstraction.
5. **Then pick the build.** Hand the shortlist to whichever pattern fits the client's platform —
   `Pattern F` (teacher-facing, the one the market and the regulator agree on) is the usual answer at
   this budget, `Pattern N` if they run an LMS already.

🔴 **Three things to decide before the first call, not after.** The integration is **unofficial** and
not affiliated with the upstream provider — fine for your own targeting, not something to resell as a
data product. The default path is a **hosted gateway** (`gateway.pipeworx.io`): the underlying data is
public federal data, but the **query pattern is not** — which districts a studio is sizing up is
commercially sensitive, so self-host before running this against a named client list. And a scoped
endpoint lists roughly **30 shared gateway meta-tools** alongside the four that matter, so budget the
context or connect once to the full gateway rather than to several pack endpoints.

🔵 **Regional honesty.** This is a **North America–only** instrument: it is NCES/Census data and has
no EMEA, APAC or LATAM analogue on these shelves. The equivalent question in those regions is still
answered by hand — recorded as `Gap 391-B` rather than left to look like coverage.

## Pattern X — 🆕 `p391` Keep the client's pedagogy as a separate, reviewable artefact

**For:** any tutoring engagement that will be audited, handed over, or argued about — which, under
EU AI Act high-risk obligations and most North American district procurement, is all of them. Also
the pattern for a studio that wants the *teaching* it built to outlive the *runtime* it shipped on.

**Why it is a separate pattern:** in nearly every tutor on these shelves, the pedagogy is diffused
through the application — prompt fragments, conditional branches, UI copy. That makes two things
expensive that clients ask for routinely: *show me the teaching policy* and *change the teaching
policy without a release*. [`SenmuuuuW/dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor)
(🟢 **MIT**, HEAD 2026-10-21) is the first row here built the other way round, and it is worth copying
even where the repository itself is not used.

**The split, which is the whole point:**

| | owns | where it lives |
|---|---|---|
| [`universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, → 2026-09-24) | **what to teach next**: diagnosis, teaching moves, pacing, when a check is passed, what the next step is | its own repository, versioned independently |
| [`dsh-diagnostic-tutor`](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) (🟢 **MIT**) | **where it is kept**: learner state, the diagnosis map, structured lessons, the UI | the runtime, which contains **no teaching logic at all** |

**Wiring:**

1. **Put the pedagogy in a versioned repository of its own**, as prose and rules rather than code:
   diagnosis strategy, teaching moves, mastery criteria, escalation. This is the artefact a client
   reviews, a subject expert edits without a developer, and an auditor reads **without reading the
   application**. It is also the thing a studio can hand over at the end of an engagement.
2. **Make the runtime record decisions, never make them.** The runtime stores what the teaching layer
   decided and renders it; every pedagogical choice arrives from the policy artefact. Test this by
   grepping the runtime for teaching rules — if `if blocked, explain the prerequisite` lives in the
   application, the separation has already leaked.
3. **Put the assessment behind a pure function.** [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)
   (🟢 **MIT**, HEAD 2026-10-18) — `@intellectif/lk-core` gives schemas, a **pure scoring engine**,
   **rubric and deferred grading**, attempt plans and redaction, with no runtime dependency beyond
   Zod. Scoring that is a pure function is unit-testable by the client and readable by a regulator;
   **deferred grading keeps a human marker in the loop by construction**, which is what high-risk
   assessment obligations ask for rather than something to retrofit.
4. **Emit evidence, do not hoard it.** `lk-core`'s **xAPI builder** sends statements to the client's
   own LRS — [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) where one is needed — so the learning
   record stays the client's property and the tutor stays replaceable.
5. **Launch it from the LMS over a maintained LTI edge — in the agent's own language.** 🆕 `p392`
   For a **Django** agent, [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
   (🟢 **MIT**, PyPI `django-lti` v0.10.1, HEAD **2026-10-20**): one installed app, one middleware,
   one migration, **no second service**. For a **JupyterHub**,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**).
   For **Node**, [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) (🟢 **Apache-2.0**, npm v7.0.7)
   or [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 **MIT**) if the deployment is
   serverless. 🔴 `p391`'s *"the edge is Node or PHP regardless of what the agent is written in"* is
   **withdrawn** — `Gap 391-A` is closed. The constraint that remains is a **licence** one: the
   best-maintained Python implementation, `openedx/xblock-lti-consumer`, is **AGPL-3.0**.

🔴 **What this pattern does not give you.** `dsh-diagnostic-tutor` is **v0.1.1 and early by its own
account**: no PDF or document ingestion, no RAG, no flashcards, no analytics, and **a route never
marks knowledge as mastered**. It also **requires DeepSeek Harness** — it is a harness extension, not
a standalone application, so an engagement that cannot adopt that harness should copy the *structure*
(steps 1–2) onto a tutor it can deploy, not adopt the repository. 🟢 Take the separation; shop for the
runtime.

## Pattern L — Clear a repository for reuse by **subtree**, not by its licence badge

**The one durable result of the `p3xx` apparatus**, kept as a procurement gate rather than a
narrative. Run it before any repo enters a client deliverable.

1. **Resolve the real default ref first.** `git ls-remote --symref https://github.com/<slug> HEAD`.
   **13 of 58 live addresses verified in `p383` are not on `main`** — `master`, `develop`, `dev`,
   `release`, `development`, `release_11`, and OpenEduCat's `19.0`; `p384` adds **openSIS-Classic
   → `master`**. A `main`-assuming read reports "no licence" for every one of them, and that false
   negative looks exactly like a real one.
2. **Probe more than one path — eight, not seven.** In order: `LICENSE`, `LICENSE.md`,
   `LICENSE.txt`, `LICENCE`, `COPYING`, `LICENSE-MIT`, `license`, and 🆕 **`docs/License.txt`**
   (with `doc/LICENSE` as its variant). Verified instances where the grant is *not* at `LICENSE`:
   **Moodle → `COPYING.txt`**, **Frappe LMS → `license.txt`** (lowercase),
   **ai-shifu → `LICENSE.txt`**, **lm-evaluation-harness → `LICENSE.md`**,
   **H5P → `LICENSE.txt`**, and 🆕 **openSIS-Classic → `docs/License.txt`** (17,286 B, stock
   GPL-2.0, *"Version 2, June 1991"*, corroborated by `"version 2 of the License"` headers in
   `index.php` and `Modules.php`). 🔵 `p384` added the eighth path because the seven-path read
   returned "ungranted" for **the most widely deployed open-source SIS in K-12** — a repository with
   a perfectly ordinary grant sitting one directory down.
3. **Check for a split grant.** **[microsoft/autogen](https://github.com/microsoft/autogen)**: root
   `LICENSE` is **CC-BY-4.0** (18,649 B, "Attribution 4.0 International"); the **code** grant is a
   separate file, `LICENSE-CODE` = **MIT**. One file read gives you the wrong answer either way.
   Conversely, confirm a split grant is **absent** before assuming one:
   [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) has **no** code grant —
   `LICENSE-CODE`, `LICENSE.code`, `CODE_LICENSE` and `licenses/LICENSE` all **404** — so its ODbL
   is the only grant on offer, for the tooling as well as the data.
4. **Compare byte length against the stock text.** A licence whose length is off is a licence that
   was edited. **[open-webui/open-webui](https://github.com/open-webui/open-webui)**: `LICENSE` is
   **2,819 B** against stock BSD-3's ~1,500 B — BSD-3 text **plus** a branding restriction and a
   CLA, self-titled "Open WebUI License". Not an OSI-standard grant.
5. **Read the manifest and the source headers before you call anything ungranted.** 🔴 **`p383`'s
   own first draft failed this step and `gate-enumeration` refused it.** Five repositories had no
   licence file at any of the seven paths; only **two** turned out to be ungranted.
   `DMontgomery40/mcp-canvas-lms` and `general-mudkip/d2l-mcp-server` declare
   `"license": "MIT"` in `package.json` (**manifest-only** — reusable, but record the line and ask
   for the file). `onbirdev/moodle-webservice_mcp` carries the full **GPL-3.0-or-later** header in
   `version.php`, as Moodle requires of every plugin — **granted, with no licence file at all.**
   Probe `package.json`, `pyproject.toml`, `composer.json`, the `README`'s licence section and the
   main source file's header before rejecting a repository;
   🆕 `p385` — **but read what that section *says*, not that it *exists*.** Two failure modes, both on
   these shelves: [moarshy/mcp-tutor](https://github.com/moarshy/mcp-tutor) has a `## License` heading whose
   entire body is *"This project is experimental and intended for educational and research purposes"* —
   which grants **nothing**, while satisfying any check that asks "is there a licence section?";
   [h9-tect/AI-Roadmaps](https://github.com/h9-tect/AI-Roadmaps) states *"provided under the
   [MIT License](LICENSE)"* and **that `LICENSE` link 404s**. A prose assertion is weaker evidence than a
   manifest field, which is weaker than the text itself — grade them separately and never as "MIT"; a file-only read would have wrongly
   rejected three of five, including the plugin Moodle's own directory distributes.
6. **Only now treat "no licence" as a hard stop — and it is a hard stop.** Two live, functional,
   actively advertised repositories survive every check above with no grant anywhere:
   `loyaniu/moodle-mcp` (no `license` field in `pyproject.toml` either) and
   `Seechange-edu/act-ai-tutor-backend` (no manifest at all). 🔵 Both were **re-probed at the new
   eighth path in `p384` and remain ungranted.** No grant means no right to redistribute, whatever
   the README invites you to do.
7. **Ask what the grant covers, not just what it is.** A valid, unmodified, correctly-recognised
   licence can still leave the part you are shipping ungranted — stock **ODbL** governs a database's
   *rights*, by its own preamble **not the contents of the database individually**. If you ship
   derivatives of the *contents* on the strength of "licence: ODbL-1.0", you have no grant for the
   part you shipped. Record the answer **per subtree** (`data/`, `docs/`, `scripts/`), and record
   "not stated" as distinct from "not granted".
   🟢 🆕 **This step was written abstractly in `p383`. `p384` gave it its first real instance** —
   `os-taxonomy`, ODbL, no code grant — and the concrete reading is now **Pattern H** below. The
   step was right in advance, which is reason to trust it on the next data artefact: education runs
   on standards, item banks and curriculum maps, so this will not be the last one.
8. **Re-check dead addresses.** Four in common circulation do not resolve: `apereo/opencast`,
   `edx/openassessment`, `openedx/openassessment`, `OpenEduCat/OpenEduCat`. Live replacements in
   [`repos/foundations.md`](../repos/foundations.md).
9. 🆕 **Confirm there is a *tree*, not just a *ref*.** `git ls-remote` on
   [projectfedena/fedena](https://github.com/projectfedena/fedena) returns two heads — and every
   content path at `master` (`README`, `README.md`, `LICENSE`, `Gemfile`, `app`) returns **404**.
   **`ls-remote` proves a ref, not a payload**, so step 1 can pass on a repository that has nothing
   in it to licence. A vendor article lists this slug as an Apache-2.0 SIS; the correct record is
   **"nothing read"** — neither granted nor ungranted. Any address census built on resolution alone
   over-counts the supply.

10. 🆕 **Read the grant at the ref you are shipping — the licence is a property of the *ref*, not of the
    repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is **AGPL-3.0** at
    `main` (`LICENSE`, 34,523 B, stock) and **MIT** at tag **`v0.1.0`** (`LICENSE`, 1,081 B,
    *"Copyright (c) 2026 Learn Shell contributors"*). Both were read first-hand in `p385`; the project
    relicensed on **2026-08-16**. 🔵 This base already knew relicensing happens —
    `snflwr-ai/snflwr.ai` went AGPL-3.0 → proprietary (`p241`), `AIHawk` went MIT for releases after a date.
    What `p385` adds is the **direction that favours the buyer**: permissive → copyleft, with the permissive
    grant **still retrievable at a tag**. 🔴 The trap in both directions is a cached audit. "We cleared that
    repo as MIT last quarter" is a statement about a ref that has moved. Record **slug + ref + licence +
    date-read**, never slug + licence — and re-read before each release, not once per engagement.
    🟡 And when you pin a tag to keep a permissive grant, say out loud what it costs: a frozen tree, no
    upstream fixes, and a maintainer who has signalled they do not want that code used on those terms.

11. 🆕 `p386` **Classify a byte-length anomaly before you judge it — "longer than stock" has two
    opposite meanings.** Step 4 says a non-stock length means the text was edited. True, and `p386`
    found the benign half of that read, which a length check alone cannot distinguish from the
    hostile one:

    | repo | bytes | the excess is | what you do |
    |---|---|---|---|
    | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 2,819 (BSD-3 ≈1,500) | 🔴 **added restriction** — branding clause + CLA | walk away, or get written permission |
    | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1,200 (MIT ≈1,065) | 🟢 **added attribution** — inline notice, *"Portions … derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License"* | ship it, carry the extra notice |
    | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | 2,181 | 🟢 **two complete MIT grants concatenated** — its own plus `d2l-cli`, © 2026 Aaryan Kapoor | ship it, carry **both** notices |
    | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 11,906 (Apache-2.0 ≈11,358) | 🟢 **ASF's appended notice text** | ship it, keep `NOTICE` |

    🔵 **So the test is not "is the length stock?" but "does the delta add a condition or a
    credit?"** Added conditions are procurement stops. Added credits are NOTICE-file entries — and
    they are *obligations you inherit silently*: ship `D2L-MCP` and you owe attribution to a project
    you never chose, which no SBOM built from a licence **identifier** will tell you.
    🟡 Record the delta's content, not just the byte count.

12. 🆕 `p386` **Count grants, not addresses — and never let a count of zero reads print as
    "ungranted".** For four passes [`agents/top.md`](../agents/top.md) said *"Blackboard has nine
    servers and not one verified grant; D2L has six and the only one checked is ungranted"*, and
    concluded both platforms needed a permissive server built. `p386` probed all fifteen: **6 MIT on
    Blackboard, 6 MIT on D2L**. 🔴 The grants existed; the reads did not. A harvest column headed
    *"distinct slugs"* answers **how many addresses exist**; `LIVE-GRANTED` / `LIVE-NOGRANT` answers
    **how many were read**. When the second number is zero the honest word is **unread**, and the
    cost of the wrong word here was a false build recommendation on two platforms.
    🔵 Before any shelf states a supply gap, state which census it is quoting.

13. 🆕 `p387` **Date the artefact you are about to ship, in the registry.** A grant tells you whether
    you *may* use it; a publish date tells you whether anyone is still there. Read the package name
    from the manifest at the real default ref, then:
    `curl -s https://registry.npmjs.org/<name>` → `dist-tags.latest`, `time.created`,
    `time.<latest>`, `versions.<latest>.license`, `.repository`; or
    `curl -s https://pypi.org/pypi/<name>/json` → `info.version`, `info.license`,
    `releases[*].upload_time`. 🟢 Three usable outputs: a **second, independently published grant**
    (a manifest-only MIT becomes an MIT published to a registry); a **maintenance date** that
    survives `api.github.com` being 403; and the discovery that an address ships **no artefact at
    all**, which is a different conversation with a client than "it is old". 🔴 `p387` found a
    four-and-a-half-year-stale dependency inside a pattern on this page, a 16-month-stale server
    recommended for its tool count, and an "institution-grade" server with no release.

14. 🆕 `p387` **A manifest's package name is not proof of a publication — match the registry back to
    the slug.** [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
    declares the npm name **`class`**, and npm's `class` is an unrelated **2013** package by
    `deadlyicon`. Keyed on the name alone, a recency sweep would have printed *"MIT, published
    2013-08-15"* onto a Google Classroom row. 🟢 **The check:** accept a registry row only when its
    `repository` field — or the links in its description — point back at the same slug; otherwise
    record `NOT PUBLISHED` and say so. The same check collapses fork families for free: four
    Blackboard addresses declare `blackboard-mcp` and **one** publication exists, its `repository`
    naming `felipedias-ie`; `mdweaver/canvas-mcp` carries upstream's scoped name
    `@r-huijts/canvas-mcp`. **Count the artefact, not the slug.**

11. 🆕 `p388` **If the repository is unreadable, read the *artefact*. The manifest is a claim; the
    tarball is the evidence.** `git ls-remote` distinguishes two states a 404 conflates: a
    **credentials prompt means the repository exists and is closed**, not absent. For such a package
    — and **6 of 32 addresses probed in `p388` are in this state while publishing to npm
    normally** — the published tarball is still readable and is **the licence that actually ships**:
    ```
    curl -s https://registry.npmjs.org/<pkg> | jq -r '.versions[.["dist-tags"].latest].dist.tarball'
    curl -s <tarball> | tar -tz | grep -i -E 'license|copying'      # is a grant shipped at all?
    ```
    🔴 **This is how `p388` established that a major publisher's tutoring SDK is ungranted.**
    `@santillana-ai/typescript-tutor-sdk` — **115 published versions** — has **no `license` field in
    `package.json`**, **no licence file anywhere in its 896,006-byte tarball**, and **no `repository`
    field at all**; its sibling scaffolder claims `"license": "MIT"` in the manifest while shipping
    **no licence file either**. Neither the repo (private) nor the badge (absent) could have settled
    it; the artefact did.
    🔵 **Three sub-rules:**
    **(a)** A manifest reading **`"SEE LICENSE IN LICENSE"` that points into an unreadable
    repository is not a grant** — it is a circular reference
    — [ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) is the worked example, and 🆕 `p390` re-confirmed its repository is **still unreadable**, so the circle is still closed.
    **(b)** Steps 1–10 clear a repository **by subtree**; when there is no readable subtree, *this*
    step is the only one available, and it can only ever yield 🟡 manifest-only or 🔴 ungranted —
    **never a clean clearance**.
    **(c)** 🔴 Check **which** package in a scope carries the grant. Here the MIT claim sits on the
    *scaffolder* and the **dependency a client's code would actually import carries nothing**. Read
    the licence of the package you will `import`, not of the one you will `npx` once.

**Channel note, so this is reproducible:** `curl -sI https://github.com/...` returns **403** through
this sandbox's agent proxy and `api.github.com` returns **403**. `git ls-remote --symref` and
`raw.githubusercontent.com` both work, and together they are a stronger check than a HEAD request —
one proves the address and its real ref, the other reads the grant itself.

🟢 🆕 `p389` **Step 11, and it makes steps 1–10 one command.** A **blobless shallow clone** does the
whole gate in ~1.2 s, from the payload, with no API and no credentials:

```bash
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the real default ref (step 1)
git -C r ls-tree --name-only HEAD     # is there a LICENSE at all, and where (steps 2-3)
git -C r show HEAD:LICENSE            # the grant text itself (step 4)
git -C r show HEAD:package.json       # the manifest that must agree with it (step 5)
git -C r log -1 --format='%H %cI'     # ← NEW: who still works on this, and when
```

🔵 **Why the last line belongs in a procurement gate and not just in a research note.** The gate has
only ever answered *may we use this*. It now also answers *will we be alone on it* — and the two
produce different estimates. **A permissive grant plus an eight-month-old HEAD is a vendoring
decision with a maintenance line**, which is precisely the call this base made for `pybryt` after
reading a *registry* date; the clone reads it for any repository, published package or not. 🟡 Read
the date against the artefact: a release branch can trail a default ref
([instructure/canvas-lms](https://github.com/instructure/canvas-lms), `master` **175 days** behind its
moving `stable/*` branches), and a finished specification is not decaying. 🔴 And the limit, **re-measured at `p392` and narrower than it was**: the `git` channel itself gives no
stars, forks or releases — but `github.com/{owner}/{repo}` answers **200 via WebFetch** (403 via
curl), so **stars, forks, commit counts and release tags are readable again**, and `api.github.com`
answers **200** while refusing **by scope** rather than outright (`/search/*` is closed by design).
**Discovery** remains web search and package registries; **verification** is first-hand; and
**popularity** is back, per tool. See [`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

## Pattern Y — 🆕 `p392` Exam integrity the client can defend, without becoming a high-risk deployer

**For:** a client — a university, a certification body, a bootcamp — who asks for proctoring, and
whose actual requirement is *"we must be able to defend a result if it is challenged"*.

🔴 **Read this first, because it is the whole pattern.** For four passes these shelves said proctoring
had *"no credible permissive open-source option"*. That was wrong (`Gap 391-C`, closed this pass). But
the granted supply covers **deterministic lockdown and event telemetry**, while the **inference**
layer — identity matching, gaze, multi-face, behavioural scoring — is absent, roadmapped, or the
proprietary service an AGPL workflow brokers (`Trend 20`). 🟢 **That asymmetry is a gift, not a
shortfall:** the half you can build permissively is the half that is explainable in an appeal, and the
half you cannot is the half that makes the client a **deployer of an Annex III high-risk system** with
standalone obligations from **2 Dec 2027**.

**Wiring:**
1. **Signals in the browser, permissively.**
   [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
   manifest agrees, HEAD **2026-09-28**, npm v0.5.1): tab-switch, right-click, DevTools shortcuts,
   clipboard events, camera state, **faces**, audio loudness, and **virtual-camera / loopback /
   screen-share detection**. Face detection is `@vladmandic/face-api` 1.7.15 on TF.js, **in the
   browser**. 🔴 **Two things to change before a pilot:** self-host the model weights (it loads
   face-api **and** its weights from jsDelivr by default — a supply-chain and data-residency defect in
   any EU or public-sector deployment, and the README documents the self-hosted path), and read all
   46 commits — this is **1 ★ and one maintainer**, so vendor it and own it.
   🟡 *Alternative when you need lockdown rather than detection:*
   [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) — 398 commits,
   HEAD **2026-10-13** — blocks copy/paste/cut, right-click, selection and shortcuts and reports eight
   named violation types. 🔴 Its grant is a **CONFLICT** (Apache-2.0 in the payload, `ISC` in
   `package.json` and on npm): both readings are permissive, so it is usable, but get the two files
   reconciled before a client depends on it. 🔴 And its AI features are marked *"(To be Done)"* — do
   not quote them.
2. **Keep the record, not the video.** Both components POST to an endpoint **you** build. Store the
   **event trail** (what happened, when, on which element) and resist storing webcam frames: snapshots
   are off by default in `proctoring.js`, and leaving them off is a defensible default, not a
   limitation. Audio is analysed in memory and discarded — say so in the privacy notice.
3. **Put the decision in a human's hands, in the workflow.** The attempt/review state machine already
   exists: [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) (🔴 **AGPL-3.0**,
   253 releases, `master` HEAD **2026-10-22** — re-read first-hand this pass) if the client runs Open edX — brokered over the platform boundary, not forked — or
   [`intellectif/learning-kit`](https://github.com/intellectif/learning-kit)'s (🟢 **MIT**)
   **deferred grading** when you are building the assessment surface yourself. **No automatic
   flagging decides anything**; a flagged attempt opens a review task.
4. **Launch and report over LTI 1.3, in the agent's own language.**
   [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 MIT) for a
   Django service, [`lti-tool/lti-tool`](https://github.com/lti-tool/lti-tool) (🟢 MIT) for a
   serverless one — so the integrity result lands in the gradebook of record as an **LTI AGS score**
   with a reviewable note attached, rather than in a side system nobody audits.
5. **Write the Art. 50 and Annex III position down before you build.** Students are told, in advance,
   which signals are collected and what a flag does; the review path and the appeal path are named; the
   retention period is set. 🟢 This is cheap here **because** step 1 does no inference — the honest
   disclosure is short.

**Effort:** 4–6 weeks for steps 1–4 on an existing assessment surface; step 5 is a day of writing and
the thing that gets the deployment approved.

🔴 **What this pattern refuses to build, and tell the client why:** automated cheating *verdicts*,
identity verification from a webcam, and gaze or emotion scoring. The permissive supply does not have
them, the obligations land on the client rather than on us, and a flag that cannot be explained in an
appeal is a liability dressed as a feature.

## Pattern Z — 🆕 `p392` Size and price a Brazilian education engagement before the first meeting

**For:** a LATAM pitch — a municipal or state network, a private group — where the honest answer to
*"how big is this?"* has until now been *"we will need to scope it."* `Pattern W` does this for a US
district; this is the Brazilian instrument, and it is the closure of `Gap 391-B` for one country.

**Wiring:**
1. **Install the access layer.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil)
   (🟡 **MIT — code only**, 1,072 B; PyPI **`mcp-brasil` v0.14.0**, 18 releases; HEAD **2026-08-18**):
   an MCP server over **70 Brazilian public sources**, 533 tools, **66 of them keyless**, with large
   datasets cached locally and queried through embedded **DuckDB**. No procurement, no API key, no
   vendor.
2. **Query the school census.** `censo_escolar` (INEP) is the per-school base: network, enrolment,
   infrastructure. Build the target list — how many schools, which bands, which municipalities — and
   put a **per-school number** in the proposal instead of a range. `enem` adds outcome context where
   the engagement is secondary-level.
3. **Match it to the platform the client already runs.**
   [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🔴 GPL-2.0-or-later, real default
   ref **`2.12`**) is the municipal SIS a Brazilian engagement actually meets;
   [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) (GPL-3.0) for Portuguese/Spanish
   course delivery. Integrate **over the boundary** — web services or LTI 1.3 — so the copyleft stays
   on their side of it (`Pattern A`).
4. **Put the agent in Portuguese, from the shelf.** Tier 4 of [`agents/top.md`](../agents/top.md)
   holds the LATAM-native, Portuguese-first granted agents; `Pattern O` is the full regional build.
5. 🔴 **State the three limits in the proposal, in writing.** The bundled INEP data is a **2023
   snapshot** — currency is the risk, not the licence; the project's own `SOURCES.md` asks you to
   **validate a sample to confirm anonymisation**; and `mcp-brasil` is **not an official government
   service**, so a ministry-facing document cites **INEP** as the source and this as the access path.
   🟢 Its LGPD handling is genuinely documented: education is graded *RISCO ALTO*, the 2022 withdrawal
   and 2024 anonymised resumption are recorded, and `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate
   columns only — no `NU_INSCRICAO`, name or CPF.

**Effort:** 2–3 days to a priced, school-level proposal; the integration in step 3 is the engagement.

🔴 **And know what you are walking into.** `Trend 21`: five live 2026 LATAM tenders, **none asking for
open source** — they buy subscriptions and licences. This pattern makes the *total-cost* argument
possible; it does not make the procurement ask for it.

## Pattern AA — 🆕 `p393` The LATAM SME delivery stack, entirely permissive, with billing already in it

**When to reach for this.** A LATAM client — a training provider, a professional body, a private
school group, a corporate academy — needs to **deliver and sell courses in Spanish** and wants to own
closed extensions. Every incumbent regional base is copyleft: **Chamilo** GPL-3.0, **i-educar**
GPL-2.0-or-later, **Moodle** GPL-3.0, **frappe/lms** AGPL-3.0. Until `p393` this shelf had to answer
either *"take the GPL"* or *"build a platform."*

🟢 **The base, and it is new to these shelves:**
[`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) — **Apache-2.0**, payload read
first-hand (10,915 B, `sha256`₁₆ `a9c4042d767d`, © 2021–2024 BMO Moreno Berroteran Ortiz Soluciones,
**S.A., Nicaragua**), `main` · `53dcb60`, HEAD **2026-08-31 — 52 d**, **676 files, 505 commits, 57
releases**, PyPI `now-lms` v2.0.4. Flask/Python; courses, delivery, certificates and **monetisation**
in the box.

### The stack

| layer | component | grant | why this one |
|---|---|---|---|
| **Platform** | [`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | The only Spanish-language LMS on these shelves you can fork, extend and **ship closed**. Flask — a studio reads the whole thing in a day. |
| **Tutor / agent** | the LATAM-native agent tier on [`agents/top.md`](../agents/top.md) | 🟢 MIT | Three granted regional options; one ships as an Open edX plugin, so prefer the standalone ones here. |
| **Interop edge** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) 🟢 MIT, + [`…/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) 🟢 MIT | 🟢 MIT | 🔴 **Django, and `now-lms` is Flask** — see the honest caveat below. Needed only when the client must appear **inside someone else's LMS**. |
| **Autograding** (technical courses) | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) 🟢 BSD-3 (**161 ★**, 197 releases) + [`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) 🟢 MIT | 🟢 permissive | Grading and submission halves respectively. Both Python, both beside the platform's own runtime. |
| **Assessment import** | [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) | 🟡 **LGPL-3.0** | Ingest existing question banks as QTI. 🟡 **Link it, do not fork it** — LGPL permits the first and not the second. |
| **Public-data sizing** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | 🟡 MIT (code only) | For a **Brazilian** engagement, size the market from INEP `censo_escolar` before the first meeting — `Pattern Z`. |

### Wiring it

1. **Fork `now-lms`, pin the Apache-2.0 payload into the delivery record.** Record bytes and
   `sha256`, per `Pattern L` step 1. The appendix is **filled in**, not narrowed — that is the benign
   non-stock case, and worth noting in the record so a later reviewer does not re-raise it.
2. **Keep the agent out of the platform process.** The tutor talks to `now-lms` over HTTP and holds
   its own store. 🔵 This is `Pattern A`'s rule and it survives here for a different reason: not
   copyleft containment, but so the platform fork stays rebaseable onto a 57-release upstream.
3. **Add autograding only for the courses that need it.** `otter-grader` runs containerised; invoke
   it as a job, not in the request path.
4. **Decide the interop edge explicitly, and this is where the caveat bites** (below).
5. **Bill through the platform's own monetisation**, which is the reason to pick this base over
   `academico`. Verify it against the client's local payment rails before promising it — Nicaraguan
   defaults are not Brazilian or Mexican ones.

### 🔴 The caveats, because this base's own history says to write them next to the recipe

- 🔴 **21 ★, and that is the real risk, not the licence.** One company, 505 commits, no multi-tenancy
  claim. **Fork it and plan to own it** — budget maintenance as if upstream may stop. Do not put a
  ministry on it; `Pattern O` and Chamilo remain the public-sector answer.
- 🔴 **The LTI edge is Django and `now-lms` is Flask.** All five Python LTI implementations
  (`p393`, refuting `Gap 391-A` a second time) are **Django** apps or JupyterHub authenticators. If
  the client must launch from a third-party LMS, the edge is a **separate Django service** beside the
  Flask app. 🔵 Note what this is and is not: `p391` published *"the interop edge must be a separate
  runtime"* as a **language** claim and was wrong; here it is a **framework** claim about one specific
  pairing, and it is a deployment line to cost, not an architecture verdict.
- 🟡 **Three of the four non-platform components are copyleft or weak-copyleft** once assessment import
  enters. Keep QTI conversion (`Citolab`, GPL-3.0) and packaging (LGPL-3.0) as **arm's-length tools**
  invoked by a pipeline; nothing copyleft links into the delivered fork.
- 🔴 **Do not reach for the `timeback-*` OneRoster/QTI clients**, however well they fit on paper:
  147 releases, MIT **declared**, and a **source repository that does not resolve** (`Gap 393-B`,
  `Trend 23`). You cannot warrant a grant you cannot read.

🟢 **What the client gets that they cannot buy:** a Spanish-language delivery platform they own
outright, with billing, autograding and an AI tutor — assembled from **four permissive grants read at
the payload**, on a base whose entire source a studio can audit in an afternoon.

## Pattern AB — 🆕 `p394` The statistics and data-science course, graded automatically, including where the network is not

**When to reach for this.** The client teaches **R** — statistics, biostatistics, econometrics,
data science, any quantitative methods course — and wants automated feedback at cohort scale.
🔵 `p393` flagged that this base's most-adopted *maintained* autograder **grades R** while the shelves held no R
components at all; this pattern is the hole closed. 🟢 **And its last step is the only offline
assessment loop in this entire base**, which is what makes it worth reaching for in LATAM and APAC
rather than only in a well-connected university.

**The components, and the licence boundary runs between steps 3 and 5.**

| # | step | component | grant |
|---|---|---|---|
| 1 | Serve identical compute to the cohort | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause |
| 2 | Author the tutorial the student works inside | [`rstudio/learnr`](https://github.com/rstudio/learnr) | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* |
| 3 | Grade the exercise and answer back | [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | 🟢 **MIT** *(1,078 B, `48c18e68ffed`)* |
| 4 | Batch-autograde submitted scripts and notebooks | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) + [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🟢 BSD-3-Clause both |
| 5 | **Generate the exam** in the LMS's own format | [`cran/exams`](https://github.com/cran/exams) | 🔴 **GPL-2 \| GPL-3 — service boundary** |
| 6 | Calibrate the items after the fact | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) · [`cran/catR`](https://github.com/cran/catR) · [`ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) | 🔴 **GPL — service boundary** |
| 7 | Carry the generated exam into the LMS | QTI 2.1 / Moodle XML, per `p393`'s **Tier 8** standards layer | per that tier |

**Wiring it.**

1. **Steps 1–4 are your product and they are permissive.** `learnr` renders the tutorial, `gradethis`
   supplies the per-exercise predicate (`grade_this_code()` against a model solution for mechanical
   exercises; `grade_this()` where you must inspect the student's actual object), `ottr` handles
   batch submission. 🟢 A closed-source product may embed all four.
2. **Steps 5–6 run as a separate service, invoked over a process boundary.** 🔴 `cran/exams`, `mirt`,
   `catR` and `ShinyItemAnalysis` are **GPL**; call them as a job — stdin/stdout, a queue, an HTTP
   worker — and never link them into the product. 🔵 Same discipline `Pattern A` and `Pattern O` apply
   to Moodle and Open edX, applied here for the same reason.
3. **Record the disjunctive choice once, in writing.** `cran/exams` is **GPL-2 *or* GPL-3 at the
   licensee's election**. Pick a rung, write down which and why, and keep it with the engagement's
   licence register — downstream compatibility differs between the two, and "GPL" alone is not an
   answer a client's counsel will accept.
4. **Step 5's output is the integration point, and it is wide.** `exams2qti21()`, `exams2moodle()`,
   `exams2canvas()`, `exams2blackboard()`, `exams2ilias()`, `exams2openolat()` — verified from the
   `R/` source filenames in the clone. 🟢 So one authored item bank feeds **whichever** LMS the client
   already runs, which is the opposite of the usual per-platform rewrite.
5. 🟢 **Then NOPS, which is the step nothing else here can do.** `cran/exams` emits a standardised PDF
   that is **printed, sat on paper, scanned, and marked automatically**. 🔵 Use it where the network
   is unreliable, where invigilation must be physical, or where the institution needs a **paper audit
   trail** it can produce years later. 🔴 It is also the honest answer to the finding on
   [`intel/market.md`](../intel/market.md) that **assessment is the lowest-adoption AI use case among
   LATAM faculty**: if the reluctance is about connectivity, invigilation and auditability rather than
   about AI, NOPS addresses the actual objection instead of arguing with it.

🔴 **Two things this pattern does not claim.** **(1)** `ottr` has **3 ★** — the adoption sits on the
Python parent, so you are deploying a lightly-used component and should budget to read its source.
**(2)** `learnr`'s HEAD is **343 days** old. That reads as stable rather than abandoned — the movement
is in `gradethis` (**126 d**) — but it is a dependency whose maintenance a studio should check before
year three, not a vendor commitment.

🔴 **And a provenance warning that will bite at review.** `cran/exams`, `mirt`, `catR`, `TAM` and
`ShinyItemAnalysis` carry **no licence file at any path** — their grant is the `License:` field in
`DESCRIPTION`, which is what CRAN enforces. 🔵 **GitHub's sidebar therefore shows no licence for any of
them**, so a reviewer checking the UI will report five granted GPL packages as unlicensed. Put the
`DESCRIPTION` line in the licence register, not a screenshot of the repository page (`Gap 394-B`).

## Pattern AC — 🆕 `p394` Give teachers an assistant builder instead of building their assistants (EMEA, Moodle)

**When to reach for this.** The client is a **university or school group already running Moodle**,
their teachers keep asking for subject-specific AI assistants, and a studio cannot profitably build
one assistant per course. 🟢 **LAMB inverts the unit of delivery**: the studio delivers the *builder*
and governs it; teachers author the assistants themselves, with no code.

**The components.**

| # | step | component | grant |
|---|---|---|---|
| 1 | The assistant builder and manager | [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb) | 🔴 **GPL-3.0** *(35,349 B, `17fe6d0ffa96`)* |
| 2 | Publish each assistant into the LMS | **LTI external tool** — LAMB's own publishing path | 1EdTech LTI |
| 3 | Graded assignments against an assistant | [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) | 🔴 **GPL** |
| 4 | The LMS itself | Moodle | 🔴 GPL-3 |
| 5 | Models, where sovereignty is required | open-weights served locally — LAMB states it shares no user information with model providers and can run on *"open source and open weights models running on your compute"* | per model |

**Wiring it.**

1. **The whole stack is copyleft and that is fine here**, because nothing in it is a product a studio
   resells. 🟢 Moodle is GPL-3, LAMB is GPL-3, LAMBA is GPL — the engagement is **deployment,
   integration, governance and training**, not licensing. 🔵 This is the one shape where the copyleft
   frontier on [`repos/foundations.md`](../repos/foundations.md) costs nothing.
2. **Step 2 is why this is a pattern and not a tool.** Assistants arrive in Moodle as **LTI external
   tools**, so the LMS stays untouched: no plugin to maintain against Moodle's upgrade cycle, no
   fork, and the assistant can be withdrawn without a migration. 🟢 Same architecture `Pattern A`
   prescribes for every agent going into a copyleft LMS, except here the upstream project already
   did it.
3. **Read the tree before you read the badge.** 🔴 LAMB carries **three grants**: root GPL-3,
   `lamb-kb-server-stable/` with its own stock GPL payload, and a **vendored `open-webui/` under
   verbatim BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). `Pattern L` is the procedure; this repository is
   why `Pattern L` exists. 🔵 Check the vendored Open WebUI copy's licence **at the pin you deploy** —
   upstream Open WebUI added branding restrictions in later releases, and the copy vendored here is
   the plain BSD-3 one.
4. **Sovereignty is a configuration, not a port.** Step 5 is the reason to shortlist LAMB for an
   EMEA engagement at all: it is designed to run against locally-served open-weights models and
   states that no user information reaches a model provider. 🟢 That answers the EU AI Act data
   questions in the architecture rather than in a DPA annex.
5. 🔴 **Size it as a high-risk deployment the moment it touches grading.** `lamba` grades assignments.
   Under the EU AI Act, systems that **grade learners, assign them to programmes or influence access
   to qualifications** are **high-risk and need a conformity assessment before deployment** (see
   *EMEA* on [`intel/market.md`](../intel/market.md)). 🟢 So: ship step 2 (assistants that tutor and
   explain) first and get it in front of teachers; treat step 3 (assistants that grade) as a
   **separate, later, assessed workstream**. Selling them as one phase is how an integration project
   becomes a compliance project mid-delivery.

🔴 **The maturity caveat, stated here and not only in the evidence file.** LAMB's own Moodle.org thread
(Feb 2026) describes it as *"at a very beta stage"* with *"a few universities running pilots"*, and the
repository is **one squashed commit** with HEAD **2 d**. 🟢 It is university-authored, peer-reviewed in
*Computer Standards & Interfaces*, and visibly active — **a strong pilot base**. 🔴 It is **not** a
ministry-scale platform, there is no multi-tenancy claim this base has verified, and an engagement
that needs one should read `Pattern O`'s tenancy discussion first. 🔵 Propose it as a pilot with a
named exit, and say so to the client in the first meeting rather than the third.
