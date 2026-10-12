---
industry: education
region: Global
updated: 2026-10-12
---

# Education — compose patterns

**Pass 140, 2026-10-12.** 🆕 **`P19` is added, and it is the first pattern on this page sourced
from a row that already SHIPS the control rather than needing one wrapped around it.** 🔁 **`P18`
is amended at step 5**: enumerate per *deployment configuration*, not per package — because
`ACTION CP` established that a connector's tool surface is a property of its flags.

## 🔁 `P18` amended again at step 5 — a static tool count is a BOUND only on the npm connector tier *(p141 — Global)*

p140 amended step 5 to enumerate per **configuration**, because `tutor-mcp`'s surface moves with
`deps.Institution` and `REGULATION_GOAL`. 🔴 **`ACTION CZ` shows the amendment was both too
narrow and too broad.**

| | npm connector tier | 🔴 agent-server tier |
|---|---|---|
| rows measured | 8 *(p140)* | 4 *(p141)* |
| 🔴 **dynamic registration** — name from an expression | 1 — **12%** | 🔴 **2 — 50%** |
| flag-gated registration | 0 | 🔴 **0** |

🔵 **So gating is one row's maturity, not a tier property — and the thing that actually defeats a
static enumeration is DYNAMIC registration, which is the majority shape one tier up.**

### The amended step 5

> 5. **Enumerate the tool surface with the method the tier requires, and say which you used.**
>
>    a. **Grep for name literals** at registration sites. 🟢 On the npm connector tier this is
>       sufficient and *provably* so: a single server instance + literal names + no gate forces
>       the live `tools/list` to equal the static count, for 7 of 8 measured rows.
>
>    b. 🔴 **Then count registration sites whose name comes from an EXPRESSION** —
>       `for (const t of TOOLS) server.registerTool(t.name, …)`,
>       `@mcp.tool(name=name)` inside a walk over a spec table. **If that count is non-zero,
>       step (a)'s number is meaningless and must not be reported.** Resolve the collection
>       instead: `ahmedEid1/lumen` serves **10** tools from 10 `ToolSpec(` entries where a
>       literal count returns **1**; `nirholas/ai-tutor-mcp` serves **2** where it returns **0**.
>
>    c. 🔴 **Then look for gating ONE INDIRECTION UP, not at the registration site.**
>       `tutor-mcp` gates in `tools/tools.go`, where `registerGetNextActivity(server, deps)` is
>       called inside `if deps != nil && deps.Institution` — while the name literal sits in an
>       `addTool(…)` helper two frames away. 🔵 **No lexical test at the name site can see this**,
>       which is why `p141-agent-surface-gate`'s Go lane fails its own control and publishes no
>       Go verdict. Read the central register function by hand.
>
>    d. **Report the method, the tier and the residual uncertainty**, in the delivery document.
>       🔴 **"62 tools" with no method attached is the number that produced p140's 61-tool blind
>       spot.**

🟢 **Tooling**: [`p140-live-surface-bound`](code/p140-live-surface-bound/README.md) for
TypeScript/JavaScript, [`p141-agent-surface-gate`](code/p141-agent-surface-gate/README.md) for
Python `FastMCP`, JavaScript and hand-rolled PHP. 🔴 **Neither covers Go**; that one is manual.

---

## 🆕 `P20` — The three-layer due-diligence gate: run it before the first sprint, in under an hour *(new, p141 — Global)*

🔵 **This pass measured four numbers a buyer would want before signing, none of which appears in
any market report on `intel/market.md`, all four from published artefacts in under an hour.**
`P20` is that hour, written down as a gate with named components.

### What it answers, and why each question has burned this KB

| layer | the question | what goes wrong if you skip it |
|---|---|---|
| **1. Grant** | Where is the licence, really? | 🔴 **5 of 9 Maven coordinates declare nothing in their own POM.** `org.verapdf:verapdf-library` — the PDF/UA accessibility validator — is **dual GPL-3.0 / MPL-2.0** two levels up, and a scanner reading the named coordinate reports *"no licence"* |
| **2. Payload** | Does the grant travel with the code you will copy? | 🔴 **`openedx-core` 1.9.1: 0 licence files, 0 SPDX headers, 0 copyright lines in 237 files across six packages**, under an **AGPL-3.0-only** distribution. Lift `openedx_tagging/` and the obligation travels silently |
| **3. Data** | What does it actually store about a learner? | 🔴 **96 of 118 tables in `tutor-mcp` are declared only in Go source.** A DPIA that enumerates `db/*.sql` finds `learners.email` and misses `pedagogical_decisions`, `assessment_attempts` and `audit_events` |

### The stack

| role | component | licence |
|---|---|---|
| grant resolution, Maven | [`p140-pom-parent-chain`](code/p140-pom-parent-chain/README.md) — walks `<parent>` upward, XML-parsed, `<licenses>` only as a direct child of `<project>` | KB-internal |
| grant resolution, npm/PyPI | [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) + [`p141-package-grant-layer`](code/p141-package-grant-layer/README.md) | KB-internal |
| notice injection | `P17`'s build step — the remedy for layer 2 | — |
| schema enumeration | [`p141-schema-location`](code/p141-schema-location/README.md) — `CREATE TABLE` across `.sql` **and** embedded migration bodies, comments stripped | KB-internal |
| tool-surface enumeration | `P18` as amended above | — |
| origin / accountability | [`p141-repo-origin-layer`](code/p141-repo-origin-layer/README.md) — compiled-in hosts, Maven `groupId`, commit offsets, with ambiguous offsets refused | KB-internal |

### How it wires together

1. **Resolve every coordinate's grant to a file, not a field.** For Maven, run the parent-chain
   walk and record the **depth** at which the grant appears. 🔴 **Continue past a silent
   ancestor** — `org.sonatype.oss:oss-parent:7` is the shared grandparent of two chains on this
   shelf and declares nothing. For an artefact that is `<packaging>pom` or `war`
   (`verapdf-library`, `org.jasig.ssp:ssp`), 🔴 **there is no jar to inspect**; resolve the
   modules consumers actually pull.
2. **For every dual or multi-licence grant, ELECT in writing.** veraPDF offers MPL-2.0 beside
   GPL-3.0; the election is free and is irrecoverable later if nobody made it.
3. **Decide what will be COPIED rather than depended on**, and run `P17`'s notice injection on
   exactly that subtree. 🔵 **This is the step that pays for the whole gate**: `openedx_tagging/`
   is 56 files that today carry no grant at all.
4. **Enumerate the schema from source, not from `.sql`.** Then diff the result against the DPIA's
   table list. 🔴 **On the one subject measured, that diff is 96 tables wide.**
5. **Enumerate the tool surface per `P18` (a)–(d)**, and treat any non-zero dynamic-registration
   count as a hard stop on reporting a tool number.
6. **Record accountability, or record that you cannot.** 🔴 **5 of 8 npm connector rows on these
   shelves declare no repository in any published version**, and one declares an unreadable one —
   so for those rows the honest entry in a vendor register is *"no accountable publisher
   identified"*, not a guess from the package name.

### Shape of the engagement

**1 day**, run by one engineer before the first sprint, on a laptop. No vendor contact, no NDA,
no running of third-party code — 🟢 **every measurement above was taken from published
registry artefacts and `git clone`**, which is why it fits in a day and why it can be re-run on
every dependency bump.

### Why it wins the room

🔵 **Because every one of its findings is a sentence a procurement officer can act on, and none
of them requires trusting the vendor's description.** *"Your accessibility validator is
GPL-3.0-or-MPL-2.0 and nobody has elected"*; *"the 56 files you are about to copy carry an AGPL
obligation and no notice"*; *"your DPIA lists 22 tables and the system has 118"*. 🟢 **And the
gate's own instruments are committed with tests, controls and their failures recorded** — three
of them corrected themselves this pass, one withheld a verdict because its control failed. 🔵
**A due-diligence tool that publishes its own limits is the only kind a client should accept.**

---

## 🔁 `P19` STRENGTHENED — the oversight primitive is enforced by the DATABASE, not by the agent *(p141 — EMEA)*

p140 adopted `tutor-mcp`'s one-way `mark_domain_high_stakes` as `P19`, on the strength of a
missing inverse tool and a typed evidence policy. 🟢 **`ACTION CX` found the layer underneath it,
and it is stronger than p140 could claim.**

`pedagogical_decisions` — declared in `db/pedagogical_contract_schema.go`, not in any `.sql` file
([`p141-schema-location`](code/p141-schema-location/README.md)):

| guarantee | mechanism | enforced by |
|---|---|---|
| append-only | `pedagogical_decisions_no_update BEFORE UPDATE … RAISE(ABORT, 'pedagogical decisions are immutable')`; Postgres `tutor_immutable_pedagogical_decision()` `FOR EACH ROW` | 🟢 **the engine** |
| tenant isolation the table owner cannot bypass | `ENABLE` **and** `FORCE ROW LEVEL SECURITY` + policy on `current_setting('app.current_tenant')` | 🟢 **the engine** |
| one decision per graded attempt | `assessment_attempts.decision_id REFERENCES pedagogical_decisions(id)` + `CREATE UNIQUE INDEX idx_assessment_decision_once … WHERE decision_id IS NOT NULL` | 🟢 **the engine** |
| 🟢 **the recommendation and the assessment cannot drift apart** | `assessment_decision_scope` refuses the insert unless `json_extract(p.snapshot_json, '$.contract.target_concept') = NEW.concept_id` **and** the recommended activity type matches, at the pinned `curriculum_version` | 🟢 **the engine** |

### What to steal, concretely

🔵 **Not the code — the shape.** Three rules, portable to any stack and cheap to add:

1. **Make the decision log append-only in the database**, with a trigger that raises. 🔴 **An
   application-level "we never update this" is not an audit trail**; it is a convention that
   survives until the next migration script.
2. **Bind the decision to the artefact it produced, with a unique index and an immutability
   trigger on the identity columns.** 🟢 This is what lets you answer *"was this learner graded
   against the thing the system recommended?"* with a query instead of an investigation.
3. **Type the evidence that can clear a safety gate.** `tutor-mcp`'s own policy string:
   `"trusted human_review evidence is required; host_llm and external_service evaluations do not
   satisfy this gate"`. 🔵 **The model cannot certify itself** — and `FORCE ROW LEVEL SECURITY`
   is what stops a privileged service account from editing the record of that refusal.

🟡 **The caveats are unchanged and still belong in the room**: alpha, one maintainer, 🔴 its
institutional tier is undocumented, and 🔴 **three undocumented writes in that tier —
`draft_formation`, `publish_formation`, `add_formation_concepts` — author the curriculum a cohort
is assessed against.** 🟢 **Adopt the three rules; do not adopt the dependency without `P20`
step 4.**

---

## 🔁 `P18` amended at step 5 — enumerate per CONFIGURATION, because the surface moves with the flags *(p140 — Global)*

p139 wrote `P18` step 5 as *"call `tools/list` on the running server and diff again — because
registration is not behaviour"*, and pre-registered `ACTION CP` to test whether that step was
needed at all. 🔴 **It is needed, and for a different reason than p139 gave.**

🟢 **On the npm connector shelf, registration IS behaviour.** All eight downloadable rows are a
single server instance registering literal tool names with no gate, so the live `tools/list` is
*forced* to equal the static build count — provable from the payload, without running anything
([`p140-live-surface-bound`](../compose/code/p140-live-surface-bound/README.md)). For those rows,
a static count is sound.

🔴 **The step survives because of the rows that are not shaped like that**, and this pass found
both failing shapes:

| shape | instance | what breaks |
|---|---|---|
| 🔴 **deployment-flag gating** | `ArnaudGuiovanna/tutor-mcp`: `deps.Institution`, `REGULATION_GOAL`, `deps.OAuthGranularScopes` | **55** names in the build; its own CI test asserts a live list of **46**. 🔵 No payload read can tell you which flags a client sets |
| 🔴 **dynamic registration** | `@owen-x-tech/canvas-mcp`: `for (const tool of tools) httpMcp.registerTool(tool.name, …)` | **1** name literal on the HTTP path; **62** tools served |
| 🔴 **two server instances** | same package, `--http` vs stdio | two surfaces under one version number |

### The amended step 5

> 5. Call `tools/list` **against each configuration the engagement will actually run** —
>    every transport the client will connect on, and every feature flag the contract enables —
>    and diff each result against the documentation *and against the other configurations.*
>    🔴 **Record the flag set beside the count.** A tool count with no configuration attached is
>    not a measurement.

🔵 **The practical consequence for a delivery team is a line item, not a philosophy**: if the
contract turns on an institutional tier, the tier's tools are the ones least likely to be
documented. On `tutor-mcp` that is exactly where the three undocumented writes are.

## 🆕 `P19` — Adopt the one-way high-stakes gate as the engagement's oversight primitive *(new, p140 — Global)*

🔵 **Every high-risk control this page has specified until now was something Globant builds AROUND
a component.** `P15` ships an Article 50 obligation, `P16` assembles a Decision 33 dossier, `P18`
gates a connector whose writes nobody enumerated. 🟢 **`ACTION CT` found a row that ships the
control itself, in MIT-licensed source, and it is better than what this page has been
specifying.**

### The primitive, as [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) implements it

`mark_domain_high_stakes` applies a **one-way** classification to a learning domain. Once set:

| property | implementation |
|---|---|
| 🟢 **irreversible from the agent tier** | **no inverse tool exists** — this pass searched for `unmark_*`, `clear_*`, `unset_*`, `reset_*` and found none |
| 🟢 **rationale recorded in code** | `db/store.go`: *"Downgrading safety classification requires an operator-controlled process that is outside the learner-facing MCP trust boundary."* |
| 🟢 **evidence provenance is typed** | returns `"policy": "trusted human_review evidence is required; host_llm and external_service evaluations do not satisfy this gate"` |
| 🟢 **capabilities withdrawn, not warned about** | returns `demonstrated_claims_allowed: false`, `intrusive_notifications_allowed: false` |
| 🟢 **degradation is explicit** | returns `degraded_components: ["human_review_evidence_readback"]` rather than failing silently |

🔵 **The design idea worth stealing is that the model cannot certify itself.** A `host_llm`
evaluation is *typed as insufficient*, so "the AI reviewed it" is not a path through the gate.
🔴 **That is the one property every regulator in this KB's matrix is reaching for and almost no
implementation expresses** — EU AI Act **Article 14** human oversight, **Annex III** grading and
ranking, Vietnam's **Decision 33/2026/QĐ-TTg**, and the Oklahoma and Maryland statutes requiring
human oversight and barring AI from high-stakes decisions about students.

### Why this row is inside the regime at all

🔴 Not a judgement — its schema
([`p140-agent-tier-pii`](../compose/code/p140-agent-tier-pii/README.md)):

- `learners.email` — `TEXT UNIQUE NOT NULL`, a **direct identifier**
- `affect_states` — a **per-session psychological profile** keyed `UNIQUE(learner_id, session_id)`:
  `energy`, `subject_confidence`, `satisfaction`, `perceived_difficulty`, `next_session_intent`,
  `autonomy_score`
- **27 of its 55 tools are writes**, including `submit_assessment_attempt`,
  `publish_curriculum_revision`, `update_learner_profile`, `record_affect`

🔵 **p138 established that Vietnam's Decision 33 names psychological assessment in its education
high-risk list.** `affect_states` is that, persisted, per session. A deployment of this row is
inside Annex III *and* Decision 33 on the strength of its schema alone.

### The stack

| layer | component | licence | why |
|---|---|---|---|
| oversight primitive | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) `mark_domain_high_stakes` | 🟢 **MIT** | the gate, and MIT means it can be lifted into client code |
| adaptive core *(same row)* | its `algorithms/` — BKT, FSRS, IRT, KST | 🟢 **MIT** | 286 test files against 279 source files |
| LMS attachment | the sanctioned-integration stack of `P11` (LTI AGS, OneRoster, xAPI/LRS) | permissive | `P19` governs decisions; `P11` moves them |
| connector gate | `P18` as amended above | — | the LMS write surface still needs enumerating per configuration |
| dossier | `P16` (Decision 33) / `P15` (Article 50) | — | `P19` produces the oversight *evidence* those dossiers assert |

### How it wires together

1. **Lift the gate, not the product.** The engagement adopts the *contract* —
   one-way classification, typed evidence provenance, no self-certification, explicit
   degradation — into whatever system of record the client already runs. 🟢 **MIT permits
   copying the source outright**, which is why this is `P19` and not a build-from-scratch.
2. **Bind the classification to the client's high-stakes definition.** For an EMEA client that is
   Annex III (admission, evaluation, exam scoring, proctoring); for a Vietnamese deployment it is
   Decision 33's list *including psychological assessment*; for Oklahoma or Maryland it is the
   statute's "high-stakes decisions about students".
3. **Make the inverse operator-only.** 🔴 **Reproduce the absence of the inverse tool.** If a
   downgrade path exists in the agent tier, the gate is advisory and the dossier claim is false.
4. **Type the evidence, do not merely log it.** `human_review` must be a distinct, trusted kind
   that `host_llm` and `external_service` cannot satisfy. 🔵 **Most "human in the loop" builds
   fail precisely here** — they record who clicked, not what class of evaluator it was.
5. **Enumerate the surface per configuration** (amended `P18` step 5). On this row, enabling the
   institution tier turns on `draft_formation`, `publish_formation` and `add_formation_concepts` —
   🔴 **three undocumented writes that author the curriculum a cohort is assessed against.**
6. **Carry the degradation signal into the dossier.** `degraded_components` is the field an
   auditor needs and the one hand-rolled implementations omit.

### Shape of the engagement

**6–8 weeks.** Weeks 1–2: map the client's high-stakes definition onto the classification and
confirm the statutory list that applies. Weeks 3–5: lift and bind the gate, with the
operator-only downgrade path built outside the agent trust boundary. Week 6: enumerate every
configuration's tool surface and document the tier the vendor did not. Weeks 7–8: assemble the
`P15`/`P16` dossier around the oversight evidence the gate now produces.

### Why it wins the room

🔵 **It inverts the usual conversation.** The standing pitch has been *"your AI tutor needs
governance we will build"*. This one is *"a working implementation of the oversight duty exists
under MIT, we have read its schema and its gate, and here is what it does that your current build
does not — the model cannot sign off on itself."* 🔴 **And the honest caveat is part of the
pitch**: the row is **alpha**, single-maintainer, and its own institutional tier is undocumented.
🟢 **Globant is adopting a contract, not a dependency** — which is the version of this argument
that survives procurement.

**Pass 139, 2026-10-12.** 🟢 **`P13` is revised a fifth time — and this time from an EXECUTION
rather than a reading.** `ACTION CL` ran the adapter against a live server: the protocol half is
cheaper than p138 estimated and the integration half is dearer, in a specific and fixable way.
🆕 **`P18` is added** because 62 undocumented write tools across nine connectors is not a caveat on
`P17`, it is its own gate.

## 🔁 `P13` rewritten — the grant goes in the store, and the server runs as a process *(fifth revision, p139)*

🟢 **Executed, not estimated.** p138's fourth revision rested on reading
[`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp)'s `OAuthStore` interface.
`ACTION CL` seeded a fixture grant and drove the real server over HTTP. Full transcript and harness:
[`p139-oauthstore-adapter`](../compose/code/p139-oauthstore-adapter/README.md).

**What the run proves:**

| step | result |
|---|---|
| `POST /oauth/token`, `grant_type=refresh_token`, grant pre-seeded | 🟢 **HTTP 200** |
| token issued | 🟢 `mcpat_…`, `Bearer`, `expires_in: 3600` |
| scopes from the seeded grant | 🟢 `canvas:read canvas:write` |
| refresh rotation (single-use, OAuth 2.1 §6.1) | 🟢 **rotated** |
| 🟢 **Canvas contacts during the entire flow** | 🟢 **0**, measured by a sentinel listener |
| grant store at rest | 🟢 **`scrypt` + AES-GCM, no plaintext** |

🔵 **So an institution that already holds Canvas refresh tokens — from an LTI launch, a prior
consent, or a service account — can mint MCP tokens for its own clients with no user redirect and no
Canvas call.** That is the whole premise of `P13`, and it is now demonstrated rather than inferred.

🔴 **The cost moved, it did not vanish.** `dist/http.js` calls `main()` at module top level with no
`import.meta.main` guard, so `import { createHttpHandler } from 'canvas-lms-mcp/http'` parses the
**importer's** `process.argv` and calls `process.exit(1)`. 🔴 **The `oauthStore` config seam is
therefore unreachable by import**, and the per-module `.d.ts` tree describes the source rather than
the bundled payload (`AuthorizationServer`, `ClientResolver`, `CanvasOAuthClient` are **not**
exported; only five symbols are).

### The build, as it actually has to be done

```text
1.  Seed:   FileOAuthStore.open(path, keySecret)
              → putClient({ clientId, clientSecretHash: sha256(secret),
                            grantTypes: ['authorization_code','refresh_token'],
                            source: 'preregistered' })
              → putGrant({ id, clientId, scopes, resource,
                           canvasUserId, canvas: { accessToken, refreshToken, expiresAt } })
              → putToken({ hash: sha256(refresh), kind: 'refresh', grantId, … })
              → flush()
2.  Run:    CANVAS_AUTH_PROFILE=oauth_brokered \
            CANVAS_MCP_ISSUER=https://… CANVAS_BASE_URL=https://canvas.inst.edu \
            CANVAS_OAUTH_CLIENT_ID=… CANVAS_OAUTH_CLIENT_SECRET=… \
            CANVAS_MCP_OAUTH_STORE=/var/lib/…/store.json \
            CANVAS_MCP_OAUTH_STORE_KEY=… \
            node dist/http.js serve --port 8097
3.  Verify: GET /.well-known/oauth-authorization-server   ← take endpoint paths from HERE
            POST /oauth/token  (NOT /token — that is a 404)
```

🔵 **Take the endpoint paths from the metadata document.** This pass lost a run posting to `/token`;
the issuer mounts OAuth under `/oauth`, and `authorization_endpoint`, `token_endpoint`,
`registration_endpoint` and `revocation_endpoint` are all advertised.

| element | estimate |
|---|---|
| 🟢 brokered token flow against a pre-seeded grant | 🟢 **hours — it works as shipped** |
| the LTI→grant seeding job (`kstateome/lti-launch` → `putGrant`) | **3–5 days** |
| 🔴 process supervision, store key management, rotation/backup of the encrypted store | 🔴 **3–5 days — this is the new line item** |
| 🟡 *optional* fork or one-line patch adding a `main` guard, if an in-process embed is required | 🟡 **1 day + a maintenance burden** |
| **total** | 🟢 **~1.5–2 weeks, and the risk has moved from protocol to plumbing** |

🔴 **Two licence conditions to settle before this ships.** `canvas-lms-mcp` is **MIT and ships its
`LICENSE` in the payload** (🟢 clean, verified p138). But `edu.ksu.ome.lti:lti-launch` **1.4.7** is
**LGPL-3.0 and ships NO licence text in its jar** — so step 1's dependency obliges a notice the
artefact does not provide, and the text must be taken from
[the repository](https://github.com/kstateome/lti-launch) and shipped deliberately. 🔵 **Run `P17`
over both before writing any of this.**

## 🆕 `P18` — The tool-surface gate: enumerate what the connector can DO before anyone connects it *(new, p139 — Global)*

🔴 **Why this is a gate and not a checklist item.** Across the nine published LMS connectors
measured this pass: **411 tools registered, 249 documented, 162 undocumented — and 62 of those
mutate the LMS.** One package registers **227** tools and documents **96**, with **61 undocumented
writes** including `bulk_update_grades`, `grade_submission`, `create_user`, `update_user_login` and
🔴 **`update_sso_settings`**. 🔵 **"Grading or ranking learners" is named high-risk by EU AI Act
Annex III and Vietnam's Decision 33/2026/QĐ-TTg. A duty cannot be discharged against a capability
nobody enumerated — and the README is what procurement reads.**

**The recipe**

| step | what you do | tool |
|---|---|---|
| 1 | Pull the **payload**, not the repo. Verify the registry's own digest (sha1 on npm, sha256 on PyPI, `.sha1` on Maven) | `p138-npm-payload-licence`, `p139-pypi-maven-payload` |
| 2 | Count **registered** tools in the shipped build across all three idioms — `registerTool(…)`, `{ name, …, inputSchema }`, and a module exporting `name` + `inputSchema` | [`p139-tool-count-drift`](../compose/code/p139-tool-count-drift/README.md) |
| 3 | Diff against the package's own documentation → the **undocumented** set | same |
| 4 | Partition the undocumented set by **write verb** → the **governance** set | `count_tools.is_write_tool` |
| 5 | Call `tools/list` on the **running** server and diff against step 2 — registration is not behaviour, and a stub is not a capability | your MCP client |
| 6 | For every write tool reaching grades, identity or enrolment: either **disable it at the gateway** or **file it in the conformity dossier** (`P16`) / Annex III technical documentation (`P15`) | `mcp-allowlist-gateway` |
| 7 | Re-run at **every dependency bump**. `@imazhar101/mcp-canvas-server` went 2.1.3 on 2026-10-01; the tier publishes weekly | CI |

🔵 **Step 6 is where this pattern pays for itself**: this KB already carries
[`mcp-allowlist-gateway`](code/mcp-allowlist-gateway/README.md), so the remediation is configuration
of something that exists, not a build.

🔴 **Two preconditions this gate also catches, both found this pass:**

- 🔴 **A package may contain no server at all.** `@exhabition/brightspace-mcp` is an **82-line
  loader** that downloads a Rust binary from GitHub Releases, `chmod 0o700`s it and `spawn`s it with
  **no checksum or signature**. Steps 2–4 correctly return **0** and tell you nothing; step 1 and a
  read of `bin/` are what catch it.
- 🔴 **A package may contain no code at all.** `openedx-learning` **0.33.0** and **0.33.1** are
  **1 479-byte** wheels holding only `dist-info` metadata, down from **257 553 B** at 0.32.0. 🔵 **Pin
  `0.32.0`** and make "artefact is non-empty" an assertion in step 1.

**Effort:** 🟢 **2–3 days to stand up for one connector family, then minutes per bump in CI.**
**Deliverable:** a signed tool inventory, a diff against vendor documentation, and a gateway
allowlist — 🔵 **which is exactly the artefact an Annex III or Decision 33 reviewer asks for and
that no vendor currently supplies.**


---

**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🔁 **`P17` is rewritten one pass after it was added, and the change makes
it shippable.** p138 created it as a gate that proves what you are about to redistribute; `ACTION
CH` then measured that **0 of 9** licence-file-less packages carry a grant in their source either,
and that **only 1 of 21** rows on the whole shelf practises per-file notice. 🔴 **So a gate that
only checks for a root licence file passes 11 packages whose grant any partial copy silently
drops.** `P17` now gates both layers and ships a notice-injection step. 🆕 **`P18` is added** for
the AGPL row, because it is the one finding on this shelf that should stop a delivery rather than
annotate it. 🔵 **No pattern is added from the search channel: 11 searches returned 0 new rows.**

## 🔁 `P17` rewritten — the two-layer licence gate, plus the notice the build must inject *(second revision, p139 — Global)*

**The problem p138's version missed.** A gate that asks *"does the payload contain a licence
file?"* splits this shelf 12 / 9 and calls the 12 clean. 🔴 **But a root licence file discharges
redistribution of the whole package and nothing about a single file.** A developer who copies one
module out of a clean MIT connector into a client's codebase carries **no holder and no grant** on
20 of 21 rows — and that copy, not the tarball, is what ends up in the client's repository.

### The stack

| component | licence *(payload-verified this pass)* | role |
|---|---|---|
| [`p139-source-header-grant`](code/p139-source-header-grant/README.md) | this KB | reads every shipped text file; reports own-grant vs `VENDORED` vs none. **24 tests** |
| [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) | this KB | the root-file layer, sha1-verified against the registry's `shasum`. **7 tests** |
| 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **MIT** (`LICENSE` ships; notice in **100 of 118** files) | 🟢 **the reference implementation of the output** — copy its header convention verbatim |

### How it wires together

1. **Gate A — the root layer.** For each dependency, download the published tarball, **sha1-verify
   it against the registry's own `shasum`**, and enumerate paths. No licence file and no SPDX id →
   🔴 **block**. SPDX id without text → 🔴 **block** and fetch the grant from the repository.
2. **Gate B — the file layer *(new)*.** Read every shipped text file. 🔵 **Report own-grant,
   `VENDORED` and none as three separate counts, never two** — a notice in minified output is a
   bundled dependency's and must not be credited to the package. A dependency at **0%** own-notice
   is not blocked; it is **flagged for step 3**.
3. **Inject on copy.** Any file lifted out of a flagged dependency and into the client's tree gets
   a header naming **that dependency's** holder and grant, applied by a build step, not by hand.
   This is the deliverable that makes Gate B worth running.
4. **Resolve the dangling references.** 🔴 A vendored notice pointing at a `LICENSE file in the
   root directory` that does not ship is an **unresolved** reference, not a satisfied one — fetch
   the named text and vendor it alongside.
5. **Pin and re-run per release.** Both gates read a *version*, and 5 of the 21 rows published
   inside eleven days.

### Why it wins the room

🔵 **It converts a licence column into a build step.** The client's question is never *"what does
the table say?"* but *"what is in our repository and can we ship it?"* — and on this shelf the
honest answer requires reading the bytes twice, at two layers.

## 🆕 `P18` — Stop-ship gate for the one copyleft row on this shelf *(new, p139 — Global)*

🔴 **`moodle-mcp-server-aql` 0.1.7 declares AGPL-3.0, ships 141 paths and 71 text files, and
carries no grant at either the file layer or the header layer.** Its repository
([`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)) carries the
canonical text, re-verified this pass at **34 523 B**, first line `GNU AFFERO GENERAL PUBLIC
LICENSE`. 🔵 **The grant exists; the distribution drops it.**

### Why this is a pattern and not a footnote

AGPL-3.0 is the strongest obligation on this shelf, and §13 reaches **network use** — which is
exactly how an MCP server is deployed. 🔴 **A client who installs this package into a hosted
tutoring or administration service takes on a source-provision duty over a network boundary, and
the artefact that arrived tells them nothing about it.** Two of three signals a reviewer would
check are silent: no licence file, no header. Only the manifest's `"license": "AGPL-3.0"` says so.

### Shape of the engagement

1. **Detect before install.** Gate A of `P17` catches it: SPDX `AGPL-3.0`, licence file absent.
2. **Decide at the network boundary, not the repository boundary.** If the service is reachable by
   users, §13 is live. 🔵 This is a **hosting-architecture** question, and it belongs with the
   client's counsel before an estimate, not after one.
3. **If the answer is no, the alternative is on the same shelf and is permissive.** The Moodle
   connector tier carries MIT rows with licence files present —
   [`verticals/solutions.md`](../verticals/solutions.md) and
   [`agents/top.md`](../agents/top.md) place them. 🔵 **`P7` already describes the permissive route
   onto Moodle**; this pattern is the gate that routes a client into it.
4. **If the answer is yes, vendor the grant the distribution dropped** — fetch the 34 523-byte text
   from the repository and ship it with the deployment, per `P17` step 4.

### Why it wins the room

🔴 **It is the only finding in this KB that can stop a delivery**, and it is three facts long: a
declared copyleft licence, a network-deployed server, and no notice in the artefact. 🟢 **Raising
it before the build is a credibility event; discovering it at a client's security review is the
opposite.**

**Pass 137, 2026-10-11.** p136's fourteen recipes retained. 🔴 **`P13` is rewritten again and
shrinks again** — from p136's three-to-four-week buy-and-adapt to **an adapter of about two weeks**,
because `ACTION BX` found the per-user mapping already implemented in a university-owned library and
the MCP half already implemented in an MIT one. 🆕 **`P15` is added because the EU deferral changed
which obligation is late**: Annex III high-risk moved to 2027-12-02 and **Article 50 did not move**.
🆕 **`P16` is added because Vietnam's education conformity duties are in force as of 2026-08-15** —
the first such regime anywhere, and this KB had no recipe for it.

🔵 **Every component named below was read this pass or in a prior pass with the licence established
from the payload.** Where a component was **not** read in source, the row says so.

## 🔁 `P13` rewritten — the adapter is an `OAuthStore` implementation *(fourth revision, p138)*

🟢 **`ACTION CE` discharged in source, and the one unknown in the third revision is now a published
interface.** p137 left the adapter as *"about two weeks"* of work whose shape was inferred. This pass
read `bruchris/canvas-lms-mcp`'s OAuth module and the shape is no longer inferred:

| p137's open question | p138's measurement |
|---|---|
| Does the broker implement the **RFC 8707** binding the LTI seam lacks? | 🟢 **Yes, by name.** `src/auth/oauth/authorization-server.ts` (**978 lines**) carries `normalizeResource()` — *"Canonical comparison for RFC 8707 `resource` values (§7)"* — plus **PKCE `S256`**, `registration_endpoint` with **dynamic client registration**, `/.well-known/oauth-authorization-server`, and a `canvas:write` scope. `resource-server.ts` (195 lines) publishes `/.well-known/oauth-protected-resource` (**RFC 9728**) and performs the **audience** check |
| Does wiring it require forking either library? | 🟢 **No.** `CanvasMCPServerConfig` takes `oauthStore?: OAuthStore`, documented *"Embedders may supply their own implementation"*. `OAuthStore` exposes `putClient`, `putGrant`, `putToken`, `putPendingAuthorization`, over a `Grant` carrying `CanvasConnection { refreshToken }` |
| Can a verified LTI `sub` be injected directly? | 🔴 **No — and this is the adapter's entire reason to exist.** The subject is established by `CanvasOAuthClient`, which redirects the user to Canvas. No path accepts an external assertion |

🔵 **So `P13` step 2 and step 3 collapse into one deliverable with a known signature**: implement
`OAuthStore`, seed it from the launch, hand it to the server constructor.

**Shape of the work (≈2 weeks, one engineer) — revised steps 2–3.**
1. Stand up `ltijs` v7 as the tool; take `sub`, `deployment_id` and the course context from the
   verified launch (the `LaunchContext` v7 hands the handler). *Unchanged.*
2. 🔁 **Implement `OAuthStore`** against the institution's own session store, keyed by the launch
   `sub`. Obtain the per-user Canvas refresh token in the shape `kstateome/lti-launch` proves
   (`/beginOauth` for that user → `storeToken(userId, refreshToken)`) and `putGrant` a `Grant`
   carrying it as `CanvasConnection { refreshToken }`.
   🔴 **Create the grant up front.** `store.ts` carries *"Update only, never create (QA S7, #356)"*
   on the Canvas-refresh path — a lazy upsert on first token call will not work.
3. 🔁 **Construct the server with `{ oauthStore, authProfile: 'oauth_brokered' }`.** The brokered flow
   then issues an audience-bound MCP token for the launching user **without the Canvas redirect**,
   because the grant is already present. 🟢 **No fork of `ltijs`, no fork of `canvas-lms-mcp`.**
4. Pseudonymise before anything leaves the boundary: `canvas-lms-mcp` ships
   `src/pseudonym/pseudonymizer.ts`. 🟢 **And it fails closed** — when `sharedAcrossCallers` is
   undeclared the factory treats the deployment as shared and **throws** rather than guess if the
   environment asks for reverse lookup. *Build on that default; do not switch it off.*
5. 🔴 **Acceptance tests that make the pattern honest** — three now, not one:
   - a valid MCP token for a *different* audience must be refused (*"Access token was not issued for
     this resource"*);
   - a token without the `canvas:write` scope must leave write tools **blocked**, which `http.ts`
     decides at `outcome.scopes.includes('canvas:write')`;
   - a pasted `X-Canvas-Token` must get a **`400`** under the brokered profile.
6. 🔴 **Pin the dependency by payload, not by identifier.** `canvas-lms-mcp` **2.2.0** on npm is
   clean (378 paths, `package/LICENSE` present, published **2026-10-10**) — but 9 of 21 packages on
   this shelf ship no licence text, so verify the one you pin. See `P17`.

🔴 **What still kills this build is unchanged:** an institution whose LMS is **not** Canvas. The
broker and the launch mapping are both Canvas-specific, and the Brightspace and Moodle connectors
hold credentials instead of brokering them. 🟡 **For Brightspace, `D2L_PASSWORDLESS=true` plus a
token-paste path is the stopgap** — a stopgap, not the pattern.

## 🆕 `P17` — The licence-payload gate: prove what you are about to redistribute *(new, p138 — Global)*

**The engagement.** Any engagement that ships open-source components to a client — so, effectively,
all of them. 🔴 **`T17` measured that 9 of 21 published education-connector packages carry no licence
text, 7 of them while declaring an SPDX identifier.** A studio that reads licences from repositories
and ships artefacts from registries is checking a different object from the one it delivers.

**Why this is a pattern and not a checklist item.** 🔵 **The defect is invisible to every tool a
studio normally uses.** `npm ls --json` reports the identifier from the manifest; so do licence
scanners that read `package.json`. Both report `MIT` for a package whose tarball contains no licence
file at all. The only way to see it is to enumerate the payload.

**The stack.**

| piece | component | licence | role |
|---|---|---|---|
| the probe | [`p138-npm-payload-licence`](code/p138-npm-payload-licence/README.md) — in this KB | — | 🟢 **Runs as-is.** Takes package names, emits one TSV row each: version, publish time, SPDX id, `files` field, path count, licence file. **sha1-verifies every tarball against the registry's own `shasum`** and refuses to report a row whose bytes do not match |
| licence family classification | `compose/code/lib/license_family.sh` — in this KB | — | classifies the grant text once found, so a payload licence can be checked against the declared identifier rather than merely counted |
| the gate | the probe's exit path, wired into CI | — | fail the build when a dependency the client will receive ships an identifier with no text |

**How it wires together.**
1. Resolve the dependency set you will actually ship (not the dev tree) to exact versions.
2. Run `scan_npm_payload.sh` over those names; keep the TSV as a **build artefact**, because it is
   the evidence, and it is dated and reproducible.
3. 🔴 **Fail on `spdx_id != ABSENT && licence_file == NONE`** — the declared-but-absent class. That is
   the one where the client is told an obligation exists and handed nothing to satisfy it.
4. 🟡 **Warn, do not fail, on `spdx_id == ABSENT && licence_file == NONE`.** Two live packages on this
   shelf are in that state with no `repository` field either (`@imazhar101/mcp-canvas-server`,
   `@n35da/brightspace-mcp`). 🔵 **Nothing to read, nobody to ask — the correct action is not to ship
   them, which is a sourcing decision rather than a build failure.**
5. 🟢 **Escalate copyleft rows to a block.** `moodle-mcp-server-aql` declares **AGPL-3.0** over 141
   paths with no text. A permissive row missing its notice is an attribution defect; a copyleft row
   missing its text is a conveyance defect, and for an AGPL component attached to a GPL platform
   (this KB's `P7` route) it is the one that reaches the client's own obligations.
6. 🟢 **When a row fails, the ask upstream is small and specific**: all nine defects measured are the
   repository being *better* than the distribution, so the fix is one `files` entry in `package.json`,
   not a licensing negotiation. Open that PR; it is a two-line change and it fixes it for everyone.

**Shape of the engagement.** 🔵 **Two days to wire, then free forever.** It is not a billable
workstream; it is the thing that keeps a licence column from being wrong in the one place it matters.

🔴 **What this pattern does NOT cover, stated so nobody over-trusts it.** It reads licence **files**
only, so a grant in a source-file header reads as `NONE` — p137's `pipwerks` correction proved that
case is real, which means the gate **over-reports** and every failure needs a header read before
anyone writes to an upstream. It covers **npm** only: PyPI, Maven and crates need the same probe
against their own payload formats, and some rows have no payload layer at all (`moodler-mcp` is not
on PyPI). 🔵 **Use it as a gate on what you ship, never as a licence verdict on a project.**

## 🔁 `P13` rewritten — sanctioned MCP access to an LMS with no new credential *(third revision, p137)*

**The engagement.** An institution wants agents to act inside its LMS *as the person who launched
them*, with no personal access token pasted anywhere and no password held by the tooling. 🔴 **p135
called this a 4–6-week build. p136 called it a 3–4-week buy-and-adapt. p137 measures it as an
adapter**, because three of the four pieces exist.

| piece | component | licence | status after this pass |
|---|---|---|---|
| terminate the launch | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) **v7.0.7** | 🟢 Apache-2.0 | 🟢 Verifies an LTI 1.3 launch correctly. 🔴 **v7 is a TypeScript rewrite: Node 24+, no session cookies (`localStorage` + postMessage storage), `Provider` constructed not `setup()`** — budget the migration if the client is on v5 |
| map launch subject → per-user grant | [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🔴 **LGPL-3.0**, Java/Spring | 🆕 **The pattern, proven in production code**: `ensureApiTokenPresent()` → `getRefreshToken(eid)` → `/beginOauth` for that user → `storeToken(userId, refreshToken)`. 🔴 **Port the pattern, not the file**: LGPL + Java against a Python/TS agent stack |
| issue the agent's own audience-bound token | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) `--auth-profile oauth_brokered` | 🟢 MIT | 🆕 **Already an OAuth 2.1 authorization + resource server**: RFC 9728 protected-resource metadata, audience check, `canvas:read` scope, revocation, Canvas refresh, **`400` to a pasted `X-Canvas-Token`** |
| generic IdP instead of Canvas | [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) | 🟢 Apache-2.0 | carried from p136: JWKS-verified `id_token`, refuses to issue with no subject claim, RFC 8707 resource binding |
| 🔴 **the bespoke part** | the LTI 1.3 → broker adapter | — | 🔴 **Still nothing maps a verified 1.3 `id_token` onto an RFC 8707-bound MCP token.** Proven in code, not assumed: `ltijs` v7 mints only `client_credentials` with the **tool's** client id as `sub` |

**Shape of the work (≈2 weeks, one engineer).**
1. Stand up `ltijs` v7 as the tool; take `sub`, `deployment_id` and the course context from the
   verified launch (the `LaunchContext` v7 hands the handler).
2. Persist a per-user upstream grant in the `OauthTokenService` shape — `get` / `store` / `update`
   keyed by the launch subject. 🔵 **This is the piece `lti-launch` proves is sufficient.**
3. Point `canvas-lms-mcp`'s `oauth_brokered` profile at that store, so the MCP access token it issues
   is bound to the same subject and carries its own audience.
4. Pseudonymise before anything leaves the boundary: `canvas-lms-mcp` ships
   `src/pseudonym/pseudonymizer.ts`.
5. 🔴 **Acceptance test that makes the pattern honest**: a request bearing a *valid* MCP token for a
   *different* audience must be refused. That string exists in the implementation — *"Access token
   was not issued for this resource"*.

🔴 **What still kills this build:** an institution whose LMS is **not** Canvas. `canvas-lms-mcp`'s
broker is Canvas-specific, `lti-launch` is Canvas-specific, and the Brightspace and Moodle
connectors on the shelf hold credentials instead of brokering them. 🟡 **For Brightspace,
`D2L_PASSWORDLESS=true` plus a token-paste path is the stopgap** — and it is a stopgap, not the
pattern.

## 🆕 `P15` — Ship the Article 50 obligation that did NOT move, while the high-risk clock runs *(new, p137 — EMEA)*

**The engagement.** A European institution or edtech vendor was told to be conformity-ready by
**2026-08-02**. 🔴 **That date moved to 2027-12-02 for Annex III** (education) under **Regulation
(EU) 2026/1744** (in force 2026-07-27). 🟢 **Article 50 transparency did not move: it applied from
2026-08-02**, with a grace period to **2026-12-02** for systems already on the market. So the
client's *late* obligation is the marking one, and the expensive one has fourteen months.

| step | component | licence | what it does |
|---|---|---|---|
| mark synthetic output | `compose/code/aiact-50-2-marking` | this KB | Article 50(2) marking surface, with tests |
| package the provenance | `compose/code/aiact-50-2-pack` | this KB | an XSD-validated marking pack |
| find what is already exposed | `compose/code/aiact-50-2-exposure`, `-spans` | this KB | which outputs and spans fall under the duty |
| disclose at the interaction boundary | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) v7 launch handler | 🟢 Apache-2.0 | the launch is where a learner meets the system, so it is where the disclosure belongs |
| keep the conformity file open | `intel/policy-matrix.tsv` | this KB | 🟡 Annex III duties by **2027-12-02**: a tracked file, not a sprint |

🔵 **Why this sells in October 2026 and not in 2027:** the deferral was granted because harmonised
standards and national authorities were not ready, so **the control set a client will be audited
against does not exist yet** — while the marking duty is already enforceable. 🟢 **Do the enforceable
half now and keep a dated register for the deferred half.** 🔴 **One conflict to disclose to a
client rather than hide**: one source dates the already-on-market grace to **2027-02-02** rather than
2026-12-02; treat 2026-12-02 as the planning date and say why.

## 🆕 `P16` — Conformity dossier for an education AI system under Vietnam's Decision 33 *(new, p137 — APAC)*

**The engagement.** A platform operating in Vietnam runs one of the **three education classes** that
Decision **33/2026/QD-TTg** made high-risk, **effective 2026-08-15**: self-study content generated
from uncontrolled sources; **testing, grading or ranking learners**; behaviour monitoring using
biometric data. Duties: conformity assessment, **registration in the National AI Database**, human
oversight, incident reporting.

| duty | how this KB's shelf discharges it | component | licence |
|---|---|---|---|
| **human oversight** on grading | 🟢 **Never let the agent be the grader**: draft-only, human commit | `compose/code/grading-draft-gate` + [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) read tools | this KB / 🟢 MIT |
| **bounded write surface** | 🟢 `EDUBASE_READONLY` + per-toolset selection + `destructiveHint` is the pattern to copy: a connector that can be *configured* to be unable to write | [`EduBase/MCP`](https://github.com/EduBase/MCP) | 🟢 MIT |
| 🔴 **no uncontrolled-source self-study content** | serve retrieval from an institution-controlled corpus only; offline-first stacks make the boundary physical | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (🟢 MIT) + [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) (🟢 Apache-2.0) | 🟢 permissive |
| **no biometric monitoring** | state it as a *design exclusion* in the dossier; the cheapest conformity argument is the capability you do not ship | — | — |
| **identity, so the oversight claim is auditable** | `P13`'s broker chain: a token bound to the launching person, not a shared key | `ltijs` v7 + `canvas-lms-mcp` + `lti-launch` pattern | 🟢/🟢/🔴 LGPL |
| **incident reporting** | one append-only log per tool call with the subject the broker established, not the one the caller claimed | this KB's `mcp-allowlist-gateway` notes | this KB |

🔴 **What this pattern cannot yet do, said plainly.** The decree's **transition date for systems
already running is contradictory across the two briefings this KB could reach** (2027-09-01 vs an
unspecified additional period from 2026-08-15), and **no Vietnamese-language read of the decree has
been done** (`ACTION CG`). 🔴 **There is also no Vietnamese-owned repository anywhere on this KB's
pages**, so every component above is foreign-owned — which is itself a procurement risk in a
jurisdiction that registers systems nationally. 🟡 **Scope a dossier, not a certification.**

---

**Pass 135, 2026-10-11.** p134's twelve recipes retained; 🔴 **`P13` is added and it is a
prerequisite for `P11`, not an alternative** — p135 read the source of all three agent bridges and
found that two accept the user's identity on trust, so the pattern this KB has been recommending as
its new default **ships an agent that will act on whatever subject the caller claims**. 🟢 **`P14`
is added** from the content and assessment layer the standards register finished this pass. Fourteen
recipes. Each names the actual repos, the licence posture of the result, how the pieces wire
together, and what it does not solve.

🔵 **Every licence stated in `P13` and `P14` was established by sha256 identity against canonical
SPDX texts** (`compose/code/p135-licence-sha-identity`), not from a GitHub badge — and two popular
components are flagged out of `P14` for exactly that reason.

**Pass 132, 2026-10-11.** p131's seven recipes retained; 🔴 **P2 is re-based on a real 39 444-star
stack instead of a greenfield build** and **P8 and P9 are added** from the SIS/portal tier found
this pass (see `README.md` → Pass 132). Nine recipes. Each names the actual repos, the licence
posture of the result, how the pieces wire together, and what it does not solve. Repos cited are
verified in `evidence/verified-repos.2026-10-11.tsv` and
`evidence/verified-repos.2026-10-11-p132.tsv`.

---

## P1 — Auditable AI tutor on an existing LMS *(the default engagement)*

**For:** an institution whose students already use AI and whose board now wants control.
**Timeline:** 8–10 weeks to pilot.

**Stack**

| layer | component | licence |
|---|---|---|
| tutoring engine | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 |
| mastery + decision audit | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| LMS connector | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (Canvas) | MIT |
| launch into LMS | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) (LTI 1.3) | MIT |
| mastery reference model | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT |

**Wiring.** The agent runs *outside* the LMS and is launched via LTI 1.3, so no platform source is
touched and **no AGPL reciprocity is triggered** — this is the point of the pattern. `canvas-mcp`
gives the agent tools over courses, assignments, submissions and rubrics. `tutor-mcp` holds the
state DeepTutor lacks: per-learner BKT mastery, review scheduling, misconception records, and an
append-only log of *why* each pedagogical decision was made. Grades return to the LMS through LTI
grade passback, never by the agent writing directly to the gradebook.

**Why the audit log is the deliverable.** T1/T2 in `intel/trends.md`: the client's problem is
defensibility. "The agent recommended this exercise because mastery of skill S was estimated at
0.42" is reviewable by a human; "the model suggested it" is not.

**Result licence:** fully permissive (Apache-2.0 + MIT). Shippable as a closed derivative.

**Does not solve:** whether learning improves (see P6). Canvas-specific — for Moodle, swap the
connector for a GPL-3.0 plugin or `onbirdev/moodle-webservice_mcp` (**unlicensed — clear first**).

---

## P2 — Offline-first tutor for low-connectivity deployments *(re-based by p132: the slot is occupied, and that is good news)*

**For:** rural LATAM, Sub-Saharan Africa, South Asia; ministries and NGOs.
**Timeline:** 10–12 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| 🆕 **orchestration (start here)** | [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | **Apache-2.0** |
| education platform | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) *(NOMAD's education container)* | MIT |
| reference library | **Kiwix** *(NOMAD's Information Library — offline Wikipedia and books)* | GPL-3.0 family |
| local inference | **Ollama** *(NOMAD's AI Assistant; external OpenAI-compatible endpoint also supported)* | MIT |
| content pipeline | [`learningequality/studio`](https://github.com/learningequality/studio) | MIT |
| mastery state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| interactive content | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT |
| single-machine pilot | [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 UNREAD |

🔴 **Re-based by p132. Do not build this stack from parts — it exists.** Earlier versions of this
pattern called the slot unclaimed and specified an integration of Kolibri + a local model from
scratch. [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0, 39 444★**, 850 commits) already orchestrates exactly those pieces as Docker
containers: Kiwix for the library, **Kolibri for the education platform**, Ollama for the AI
assistant. It is the second-largest repo in this KB.

**Wiring, revised.** Stand up NOMAD first and confirm the three containers on the client's target
hardware — that is now a deployment task, not an integration project. Then add the two things NOMAD
does not do: **`tutor-mcp` for durable learner state** (BKT mastery, review scheduling,
misconceptions) persisted locally and reconciled on next sync, and **H5P activities** authored
through Kolibri Studio so the same content survives a later move to Moodle or Open edX. Pilot on a
single machine with the macOS port before committing to the Docker estate.

**Why this remains the strategically strongest pattern in the KB — more so now.** Permissive top to
bottom (Apache-2.0 orchestration over MIT components; **check Kiwix's GPL-3.0 terms if you intend to
modify it rather than run it**), and **data never leaves the device**, which discharges most of the
privacy obligation in US state law, the EU AI Act and Brazil's pending PL 2338 by construction
rather than by policy. 🟢 **The difference from the old version is commercial: the client is buying
weeks of deployment and curriculum work on a proven stack, not months of integration risk.** That
is an easier sale and a defensible one.

**Timeline, revised:** **5–7 weeks** (was 10–12), because the integration layer is no longer yours
to build.

**Result licence:** Apache-2.0 orchestration over MIT components; audit Kiwix if modified.

**Does not solve:** small-model quality is still the binding constraint — scope to one subject and
validate before widening. Still requires device-management capability the client may not have.
🔴 **And the opportunity gap is now geographic, not technical: nothing offline targets LATAM.**
The one curriculum-specific offline project found is Indian
([`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI)), so a Spanish- or
Portuguese-curriculum NOMAD deployment is unclaimed, permissively licensed, and now cheap.

---

## P3 — Policy-to-implementation compliance layer *(North America, hard deadlines)*

**For:** a US district or university facing a mandate — e.g. **Ohio's 1 July 2026 policy
requirement**, California AB 1159's ban on training with student data, Oklahoma/Maryland human-
oversight rules.
**Timeline:** 6–8 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| tool inventory | LMS connectors as discovery instruments: [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp), [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | MIT |
| decision log | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| sandboxing | [`openedx/codejail`](https://github.com/openedx/codejail) | Apache-2.0 |
| no-source-touch integration | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | MIT |

**Wiring.** Three artefacts, in order. **(1) Inventory:** enumerate via the LMS API every external
tool, LTI registration and integration touching student data — most institutions cannot currently
produce this list. **(2) Routing with proof:** put every model call behind one gateway that records
destination, payload class and retention terms, so "no student data reached a training endpoint" is
a query result, not an assurance. **(3) Gates:** any high-stakes output — grades, placement,
discipline, admissions — is advisory only and requires recorded human approval, satisfying
Oklahoma/Maryland-style rules and aligning with the EU's eventual Annex III duties.

`codejail` sandboxes learner- or model-generated code if the engagement includes auto-grading for
programming courses.

**Result licence:** permissive.

**Does not solve:** the policy text itself (that is counsel's work). This builds the technical means
to comply with it and the evidence of compliance.

---

## P4 — EMEA conformity-by-design build *(before December 2027)*

**For:** an EU institution that will fall under Annex III when high-risk duties apply.
**Timeline:** 10–12 weeks.

**Stack**

| layer | component | licence |
|---|---|---|
| platform | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) or [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) or Moodle | GPL-3.0 |
| public portal | [`openfun/richie`](https://github.com/openfun/richie) | MIT |
| step-level feedback | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | Apache-2.0 |
| mastery audit | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| integration | LTI 1.3 via [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | MIT |

**Wiring.** Build to the obligations **already in force**, not the postponed ones: Article 4 AI
literacy (since February 2025) and the **prohibition on emotion recognition in education** (since
2 February 2025). Architecturally: no affect/emotion inference anywhere in the system — products
built for other markets ship it and it is illegal here; grading and admissions remain human
decisions with the agent advisory only, which keeps the deployment out of the heaviest Annex III
duties by design; `ideas-edu/ideas` provides deterministic, domain-reasoned step-level feedback for
maths and logic, which is defensible to a regulator in a way LLM free-text is not; Richie (MIT,
proven at French national scale) fronts it.

**Why ILIAS/Chamilo rather than Canvas.** EMEA procurement runs on these, scores standards and
accessibility compliance in tenders, and neither has any AI-on-top — an open field.

**Watch:** Council adoption of the Digital Omnibus. If it fails, the original high-risk dates snap
back and this timeline compresses hard.

**Does not solve:** no open-source proctoring or academic-integrity system exists, and proctoring is
squarely Annex III. Do not promise it.

---

## P5 — Teacher-capacity tooling at national scale *(APAC mandates)*

**For:** ministries and large private networks facing curriculum mandates — **India from Class 3 in
2026-27**, China from age six.
**Timeline:** 8–10 weeks to a usable generator; longer to scale.

**Stack**

| layer | component | licence |
|---|---|---|
| content generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | MIT |
| pedagogy/skill library | [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION — review first** |
| interactive output | [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | MIT |
| platform | [`frappe/lms`](https://github.com/frappe/lms) or Moodle | AGPL-3.0 / GPL-3.0 |
| delivery at scale | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) where connectivity is poor | MIT |

**Wiring.** The bottleneck in a national mandate is teachers, not students: curriculum, lesson
plans, question banks and assessments in volume, in local languages. `educhain` generates the
artefacts; the skills library supplies pedagogical structure; output is authored as **H5P** so it
renders on whatever platform each state or network runs. Human review stays in the loop per
artefact — content entering a national curriculum needs a named approver, and India's AI-content
labelling rules apply to generated material.

**Licence caution, twice.** `educhain` publishes **no GitHub releases** and its README's version
history stops at **v0.3.13 (October 2024)** — pin a commit and expect to maintain it.
`education-agent-skills` reads as **NOASSERTION**: read the terms before any client reuse.

**Does not solve:** teacher training itself. ~a quarter to a third of the APAC public wants AI out
of classrooms (Ipsos 2026), so adoption is a change-management problem, not a software one.

---

## P6 — Learning-outcome evaluation harness *(the instrument exists; it is unshippable)*

**For:** any client who will be asked "did it work?" — and the differentiator none of them can
currently buy.
**Timeline:** 4–6 weeks, runs alongside P1–P5.

**Stack**

| layer | component | licence |
|---|---|---|
| mastery ground truth | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (BKT) | MIT |
| decision + mastery log | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT |
| structured lesson model | [`oppia/oppia`](https://github.com/oppia/oppia) | Apache-2.0 |
| interaction telemetry | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (xAPI) | MIT |
| multi-agent baseline | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 |
| **pedagogical benchmark** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (ETH Zurich, EMNLP 2025 oral) | 🔴 **none declared** — run/cite only |
| **failure-mode dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) (Khan Academy) | 🔴 **bespoke eval-dataset licence** — run/cite only |

**Wiring.** 🔴 **p130 built this pattern on the claim that no benchmark exists. Two do** (T7), and
starting from them removes weeks of design — so this pattern is now *two layers*, and the licence
boundary between them is the whole point.

**Layer 1 — borrow the published task structure (do not ship it).** Run `mathtutorbench` against
the candidate tutor for open-ended *pedagogical* capability (scaffolding, hint quality, when to
withhold the answer), and use `Khan/tutoring-accuracy-dataset` as the known-failure-mode set for
maths tutoring. 🔴 **Neither may be redistributed inside a client deliverable**: `mathtutorbench`
declares no licence and its README names two different ones, Khan's is a bespoke 2 690-byte
"Evaluation Dataset License". **Run them in your own environment, report the scores, ship neither
the data nor a derived fixture set.** If the client needs a shippable suite, re-author the task
*shapes* against their own curriculum — the ideas are not the asset, the labelled data is.

**Layer 2 — build the outcome half, which genuinely does not exist.** Both benchmarks measure tutor
behaviour, not whether a student learned. BKT parameters from `OATutor` give a quantitative,
inspectable mastery estimate independent of the tutor's self-assessment; `tutor-mcp` logs every
decision with the mastery state that produced it; xAPI via `scorm-again` captures interaction
telemetry from existing courseware so a pre-intervention baseline exists; Oppia's lesson model
encodes misconceptions explicitly, giving labelled targets to measure against. Run a holdout: same
content, tutor on and off, compare mastery trajectories and retention at a fixed interval.

**Why it closes every other pattern.** The OECD's 2026 Outlook asks for **durable learning gains**;
US state mandates ask for evidence that high-stakes decisions were sound; EU Annex III will ask for
documented performance. One harness answers the pedagogical question and three regulatory ones.

**Does not solve:** it measures, it does not teach. It needs a holdout design the institution must
agree to — negotiate that at contract time, not at delivery. 🔴 **And the two borrowed benchmarks
are maths-only**: for any other subject, Layer 1 has no published instrument and the shapes must be
authored from scratch.

---

## P7 — Moodle agent on the permissive side of the GPL boundary *(the route p130 said did not exist)*

**For:** any client on Moodle — the most deployed LMS in the world — that wants an AI layer it can
own, without taking on GPL-3.0 reciprocity on its own code.
**Timeline:** 5–7 weeks.

**Stack**

| layer | component | licence | why this one |
|---|---|---|---|
| platform (untouched) | [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | Left entirely alone. **Nothing is forked and no plugin is written**, so no reciprocity is triggered. |
| connector | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | Standalone MCP server against Moodle's **web-service API**. Verified MIT by two independent instruments. 🔴 **Quiet since 2026-02-22 and publishes no tags — pin a commit.** |
| assessment + gradebook | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | Exams, gradebooks, item analysis, with **writes off by default** — the right default for anything touching grades. Corporate holder, LTI path. |
| durable learner state | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | BKT mastery, review scheduling, misconception tracking, auditable pedagogical decisions. LMS-agnostic. |
| launch surface | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | LTI 1.3 launch with signed identity and grade passback, so the UX lives inside Moodle while the code lives outside it. |
| build velocity | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) + [`claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | Live moodledev.io docs, Hooks API, XMLDB and Jira as agent tools; plus plugin-building skills if a plugin ever does become necessary. |

**Wiring.** Moodle's web-service API is the whole trick: enable the web-service functions the use
case needs, issue a scoped token per service, and point the MIT MCP servers at it. The agent gets
courses, assignments, submissions and grades as tools; `tutor-mcp` holds the mastery state between
turns so the tutor is not re-deriving the learner from the transcript each time; `ictexam-mcp`
handles anything assessment-shaped with writes explicitly enabled only where a human approves.
Learner-facing UX enters through **LTI 1.3**, not a plugin. **Every line Globant writes stays MIT or
client-proprietary**; the only GPL-3.0 artefact in the deployment is Moodle itself, unmodified.

**Why this pattern exists.** p130's pages told a reader that Moodle had *no permissively licensed
MCP route* and that the options were a GPL-3.0 in-tree plugin or an unlicensed web-service plugin.
That was false in both directions, and the cost of the error is the whole engagement shape: it
pushes a client toward writing a GPL plugin when a clean-room MIT side-car was available.

**Checks before proposing it.** Confirm the client's Moodle has web services enabled and tokens
issuable — some managed hosts disable them. Pin commits (`peancor` has no tags). Keep grade writes
behind human approval: automated grading is **Annex III high-risk** in the EU from 2027-12-02 and is
restricted by several US state rules now (`intel/policy-matrix.tsv`).

**Does not solve:** deep in-page Moodle UX. If the client insists the AI live inside a Moodle
activity rather than an LTI launch, a GPL-3.0 plugin becomes unavoidable — and the reciprocity is on
the plugin, not the client's other code.

---

## P8 — Sanctioned connector for a national school platform *(new, p132 — EMEA's clearest unmet need)*

**For:** the vendor or ministry behind a national K-12 platform — **Librus** (Poland), **EduPage**
(Slovakia/Czechia), **Pronote** (France), **IServ** (Germany) — or a large school group running one.
**Timeline:** 8–10 weeks.

🔵 **Why this pattern exists.** p132 found that all four platforms already have open-source MCP
connectors, mostly MIT, written by pupils and parents — and **every one is an unofficial
password-scraper with no DPA, no audit trail, and (for `librus-mcp`) no 2FA support**. The vendors
have no agent story at all. So the work is not *"can an agent reach this platform"* — that is proven
and published — it is *"make it legitimate"*.

**Stack**

| layer | component | licence | role |
|---|---|---|---|
| API surface map | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) · [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) · [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) · [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | MIT *(🔴 `librus-mcp`: MIT 2.x only — `legacy_reference/` is **GPL-3.0-only**)* | 🟢 **read as documentation**; keep the endpoint map, discard the auth |
| identity | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) as the reference shape — Okta OIDC/SAML, OAuth 2.0, **SCIM** | 🔴 unlicensed — **pattern only, do not vendor the code** | replaces the stored pupil password |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) FERPA-logging approach | **Apache-2.0** (payload-read) | per-access logging a regulator can read |
| policy gate | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) for auditable pedagogical decisions | MIT | keeps inference out of high-stakes calls |
| launch surface | [`instructure/ims-lti`](https://github.com/instructure/ims-lti) where the platform speaks LTI | MIT | avoids touching platform source |

**Wiring.** Lift the endpoint map from the existing MIT connectors — that is the weeks of
undocumented-API archaeology you do not repeat. Replace the credential model wholesale: the agent
authenticates through the platform's own SSO with scoped, revocable tokens provisioned by SCIM, and
**never holds a pupil credential**. Every read is logged with actor, subject, field and purpose.
Write operations stay off by default; grade and attendance writes require a human confirmation step.
Ship it as a vendor-sanctioned integration, not a scraper.

🔴 **The compliance work is the deliverable, not overhead.** For all four platforms the subjects are
children, so: a **DPA with the vendor**, a lawful-basis analysis, a **DPIA**, data-minimised scopes
(a timetable agent does not need disciplinary records), and retention limits. Annex III of the AI
Act is not triggered by reading a timetable — but it *is* triggered the moment the same connector
feeds grading or admissions, which is the second phase every client will ask for. **Architect the
boundary now** (`P4`).

**Result licence:** your own code; MIT inputs read as reference only. 🔴 **Do not vendor
`sis-demo`** (unlicensed) or `librus-mcp`'s `legacy_reference/` (GPL-3.0-only).

**Does not solve:** it needs the platform vendor at the table. Without their cooperation this is
still a scraper, and should not be built. 🟢 **The pitch to the vendor is that pupils are already
scraping them with stored passwords and no 2FA** — a sanctioned surface is a security improvement
for the vendor, not just a feature.

---

## P9 — Administrative automation on an open-source system of record *(new, p132 — the real hole)*

**For:** institutions running, or willing to adopt, an open-source SIS/ERP — mid-size universities,
school groups, ministries. **Timeline:** 10–12 weeks.

🔵 **Why this is the sharpest opportunity in the KB after p132.** The SIS *agent* gap is closed —
there are 21 connectors — but **every single one targets a proprietary or institution-hosted
portal.** The open-source systems of record have **zero** agent coverage between them, while
administrative automation remains the most-cited adoption driver. **The connector effort has gone to
the platforms a studio cannot fork and avoided the ones it can.**

**Stack**

| layer | component | licence | note |
|---|---|---|---|
| system of record | [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 🟢 **the only permissive SIS** — the one base a client can own as a closed derivative |
| — or — | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (payload-read) | broadest functional coverage; **linking is fine**, modifying the module carries reciprocity |
| — or — | [`frappe/education`](https://github.com/frappe/education) | 🔴 **read `LICENSE` first** (API says `NOASSERTION`) | pick when the client already runs ERPNext |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | 🟢 standalone, ~42 tools, teaching-agent roles — **the reference design to read** (1★; do not depend on it) |
| optimiser | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | conflict-free timetabling under India's NEP 2020 — the only real optimiser found |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | **Apache-2.0** | FERPA-style per-access logging |
| identity | SCIM/OIDC per [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) | 🔴 unlicensed — pattern only | institutional SSO, scoped tokens |

**Wiring.** Pick the system of record on the licence question first, because it is irreversible:
**`academico` (MIT)** if the client wants to own a closed product, **`openeducat_erp` (LGPL-3.0)** if
they want coverage and will call it from outside without modifying it. Put an MCP server in front of
it modelled on `classroom-mcp`'s tool taxonomy — students, enrolment, assignments, courseware,
progress — reading through the platform's own permission model rather than around it. Attach the
timetable optimiser as a *tool the agent calls*, not as something the model does: scheduling is a
constraint-satisfaction problem and an LLM is the wrong instrument for it. Wrap everything in
per-access logging and SCIM-provisioned scoped tokens from day one.

🟢 **The commercial shape is better than the tutoring engagements.** Timetabling, enrolment and fee
chasing have a measurable baseline (hours of registrar time, scheduling conflicts per term, days to
produce a timetable), so the business case writes itself — unlike tutoring, where the client is
buying an unproven learning-outcome claim (`P6`). And the regulatory exposure is far lower: **a
timetable is not Annex III.**

**Result licence:** MIT throughout if built on `academico`; LGPL-3.0 linking obligations if on
`openeducat_erp` and the module is modified.

**Does not solve:** 🔴 **the client has to be willing to run an open-source SIS**, and most
institutions of record run a proprietary one — which is why the 21 connectors target those instead.
Realistically this lands at mid-size institutions, new campuses and ministry programmes rather than
at a university replacing Banner or SITS. 🔴 **Both scaffold rows are 1★** — read them as reference
designs and expect to own the code.

---

## P10 — Grade and workload passback for a LATAM national academic system *(new, p133 — the first pattern this KB can ground in LATAM rows)*

**For:** Brazilian federal universities (**SIGAA**) and federal institutes (**SUAP**), Argentine
universities on the **SIU-Guaraní** consortium stack. **Timeline:** 6–8 weeks for the first faculty,
plus 3–4 weeks per additional campus. 🟢 **The shortest, lowest-risk engagement in this file.**

🔵 **Why this pattern exists now and could not be written before.** For four passes this KB reported
"no LATAM-origin supply" and recommended LATAM work on market share alone. `ACTION BE` refuted that
with **12 addresses** — and three of them are doing the *same unglamorous job in two countries*:
**moving grades and workload into a national system of record that a human is currently retyping.**
🟢 **That is not a guess about demand; it is three independent people having already built it.**

🔴 **And the demand number is on the same page.** IESALC's 200-institution survey puts
**administration at 34.1%** adoption — second-lowest of four areas — while the Digital Education
Council's LATAM 2026 survey finds **50% of students want AI-assisted feedback and only 19% of faculty
give it** (`intel/market.md` → LATAM). **The bottleneck is the teacher's data-entry time, and that is
exactly what this pattern removes.**

**Stack**

| layer | component | licence | note |
|---|---|---|---|
| reference: grade passback | [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) | **MIT** | 🟢 **start here.** Pushes a spreadsheet of grades into SIGAA. MIT, 9★ — the one forkable staff-facing row |
| reference: workload report | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🔴 **AGPL-3.0** | **Read, do not fork.** Org-owned, drafts a lecturer's **RIT** from SUAP via CLI **and** MCP — the closest thing to a product in this tier. Its *architecture* is the deliverable here, not its code |
| reference: Argentina | [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) | 🔴 **unlicensed** | Pattern only. Proves the identical need on SIU-Guaraní |
| API surface: SUAP | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) (**MIT**) + [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) (🔴 unlicensed) | mixed | 🟢 **Two independent MCP implementations of the same SUAP surface** — cross-read them to separate the real API from one author's assumptions |
| API surface: SIGAA | [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) (🟡 GPL-3.0), [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) (**MIT**), [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) (**MIT**) | mixed | The published map of SIGAA's undocumented screens. 🔴 Read `sigaa-calendar` for its *surface*, not its code — GPL-3.0 |
| agent scaffold | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | tool taxonomy for courses/assignments/scores (1★ — reference design) |
| audit | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | **Apache-2.0** | per-access logging; the LGPD analogue of its FERPA model |
| the counterparty | [`SIU-Toba`](https://github.com/SIU-Toba) (Argentina) | 🔴 unlicensed, dormant since 2017 | 🟢 **The SIS consortium is itself on GitHub** — the only named sanctioned-integration counterparty in this KB (`P8`) |

**Wiring.** Three steps, in this order, and the order is the whole point.

1. **Build the importer, not the agent.** A deterministic job that takes an instructor's grade
   spreadsheet, validates it against the course roster pulled from SUAP/SIGAA, and writes it back
   through the institution's own authenticated session. **No model in this path.** `auto-sigaa` is
   the worked example; fork it. 🔵 **Grade entry is a correctness problem, not a language problem —
   an LLM in the write path converts a 2-hour chore into an unauditable liability.**
2. **Put the LLM only where the text is.** Two jobs, both safe: (a) *reconciliation* — explain in
   Portuguese or Spanish why 3 of 180 rows failed validation, which name matched no enrolment, which
   grade is out of range; (b) *narrative drafting* — the prose sections of a workload report
   (`expeditto`'s RIT), always **as a draft the lecturer edits and submits.** 🔴 **Never
   auto-submit:** a drafted report a human signs is administrative support; an auto-filed one is an
   automated decision about staff performance.
3. **Then, and only then, add the MCP surface.** Once the importer is correct and logged, expose it
   as MCP tools modelled on `academic-tracker-mcp` so the instructor can ask *"how many of my
   students are missing a grade for unit 2"*. 🟢 **This ordering is what makes the engagement
   financeable: step 1 has a measurable baseline (hours per term per lecturer, error rate,
   days-late on grade submission) before any AI spend is defended.**

**Credentials — the one blocker, and LATAM has a better answer than EMEA.** Every reference row above
logs in as its author. 🔴 **Do not ship that.** But unlike Librus or Pronote, **the counterparty here
is reachable**: SIGAA and SUAP are *public-sector* systems (SIG/UFRN-derived and IFRN-derived
respectively, both federal), and SIU-Guaraní is published by a **university consortium that already
has a GitHub org**. 🟢 **A federal institute can authorise its own integration — which is precisely
what pattern `P8` cannot get from a private EMEA vendor.** Get an institutional service account and
a DPA under **LGPD** (Brazil) or **Ley 25.326** (Argentina) before the first write.

**Result licence:** MIT throughout, if built from `auto-sigaa` + `academic-tracker-mcp` +
`classroom-mcp` and `expeditto`/`sigaa-calendar` are read rather than copied. 🔴 **Track that
boundary in the repo:** the two most useful references are **AGPL-3.0** and **GPL-3.0**, and this
pattern's whole commercial value depends on not importing them.

**Does not solve:** 🔴 **this is administrative plumbing, not pedagogy** — it will not satisfy a
client who came for a tutor (`P1`). 🔴 **It is per-platform**, so a Brazilian federal university
(SIGAA) and a federal institute (SUAP) are two integrations, not one. 🟡 **And every reference row is
0–20★ with a bus factor of one** — budget to own the code, and read `P8` before promising the
institution a sanctioned path.

---

## P11 — The sanctioned-integration agent: MCP over LTI AGS, OneRoster and an LRS *(new, p134 — and it is the pattern the other ten have been working around)*

🔴 **Every connector-based pattern in this file carries the same unpriced risk**, and `P8` names it:
the open-source connectors authenticate as a student with a stored portal password against a
platform that never sanctioned it. 🟢 **p134 found that the sanctioned path is not a research
project — it is a mature, permissive, institution-owned standards stack — and that the one missing
piece is the agent binding.** This pattern is that binding, and every dependency in it is already
chosen and licence-verified.

**Use it when:** the client runs **Canvas, Moodle, Blackboard, Open edX, Sakai, D2L or ILIAS** (i.e.
anything LTI-compliant), AND the engagement has to survive a security review, a procurement process,
or a data-protection assessment. 🟢 **Which is to say: almost every real engagement, as opposed to
every demo.**

### The stack, with licences this pass verified by payload read

| layer | component | licence | why this one |
|---|---|---|---|
| **launch + identity** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (11 361 B, holder named) | 373★, pushed 2026-10-06. OIDC launch, JWKS, Deep Linking, **AGS**, NRPS. The tool is **invited in** by a client ID the institution issues and can revoke — no stored password anywhere in the design |
| *(Python alternative)* | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (1 070 B) | 138★. 🔴 **Dormant since 2024-08-18 — budget maintenance for it, or put the LTI edge in Node and the agent in Python** |
| **PoC scaffold** | [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) | **MIT** | A template *over* `ltijs` with Dynamic Registration and PostgreSQL — days, not weeks, to a first launch |
| **grade write-back** | **LTI AGS**, via `ltijs` | — | Writes to the LMS gradebook **through the platform's own service**, which is the sanctioned equivalent of what the LATAM teacher-facing rows do by scraping (`P10`) |
| **rostering** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (711 B) | TypeScript OneRoster 1.2 SDK. **0BSD drops even attribution** — the least encumbered dependency in this KB |
| **rostering (US K-12)** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (10 173 B) | Serves OneRoster 1.2 from an **Ed-Fi ODS** — the standards body's own bridge, pushed 2026-10-09 |
| 🟢 **conformance proof** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** | **Run these and hand the client the output.** The only test suite in this KB that proves an integration correct rather than asserting it |
| **learner state / audit** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 🔴 **The load-bearing and least-maintained link: 15★, last push 2025-08-29.** An MCP server that records and retrieves learning activity via an **xAPI LRS**. **Expect to fork and own it** |
| **analytics surface** | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | xAPI learning-analytics dashboards from **France Université Numérique**, pushed 2026-10-11 |
| **enterprise auth** | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) (pattern only) | 🔴 **no licence — read, do not fork** | The worked example of **Okta OIDC/SAML + SCIM** provisioning. 🟢 Second instance now exists against a real institution: [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) (UQ, Okta SSO, 🔴 unlicensed) |
| **access logging** | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) (pattern only) | 🟢 Apache-2.0 (notice-block form) | **FERPA access logging as a first-class feature** — the audit-trail design to copy |
| **pedagogical state** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | BKT mastery, review scheduling, auditable pedagogical decisions, LMS-agnostic — so it sits behind the LTI edge rather than inside the LMS |

### How it wires together

1. **The LMS launches the tool over LTI 1.3.** `ltijs` validates the OIDC handshake and the platform
   JWT. 🟢 **The agent now knows who the learner is, in which course, with what role — signed by the
   platform, with no credential of the learner's held anywhere.**
2. **Roster context comes from OneRoster**, not from scraping a class list: `oneroster-ts` against
   the institution's rostering endpoint, or `edfi-oneroster` over an Ed-Fi ODS in US K-12.
3. **The agent runs** — any framework; `tutor-mcp` supplies mastery and scheduling state so the
   pedagogy is auditable rather than an LLM's opinion.
4. **Learner activity is written to an LRS as xAPI statements** through `learnmcp-xapi`. 🟢 **This is
   the step that makes the whole thing defensible:** every interaction lands in a store the
   institution owns, in a standard format, queryable for an audit or an impact study.
5. **Grades go back over AGS**, into the LMS gradebook, through the platform's own service.
6. **`warren` renders the analytics** over the same xAPI data — so the evaluation harness (`P6`) and
   the product read from one store.
7. **Access is governed by the institution's IdP** (Okta OIDC/SAML + SCIM per `sis-demo`) and
   **every record access is logged** (per `mcp-student-records`).

### Shape of the engagement

**8–12 weeks to a defensible pilot in one course**, on the assumption that the client's LMS admin
can register an LTI tool — 🔴 **confirm that in week one; it is the only hard external dependency,
and in a large institution it is a ticket, not a conversation.**

- **Weeks 1–2** — LTI registration; `ltijs` launch working end to end; rostering endpoint identified
  and the **Google conformance tests run against it**.
- **Weeks 3–5** — LRS stood up; fork and harden `learnmcp-xapi` (🔴 **assume this is real work: 15
  stars, 14 months quiet**); xAPI statement vocabulary agreed with the client's institutional
  research team.
- **Weeks 6–8** — the agent itself, with `tutor-mcp` for mastery state; AGS grade passback;
  human-in-the-loop review on every write.
- **Weeks 9–12** — IdP integration and SCIM; FERPA/GDPR access logging; `warren` dashboards; the
  conformance and audit artefacts packaged as deliverables.

### Why it wins the room

🟢 **The security review is the deliverable, not the obstacle.** Against any of the 43 portal
connectors, the honest answer to *"where does the student's password live?"* is "in our config".
Here the answer is **"we never have one"** — and there is a conformance-test output, an audit log and
a standards-based record store to hand over with it. 🟢 **And it is the only pattern in this file
whose dependencies are owned by the Ed-Fi Alliance, Google, the US DoD and a French public
operator**, which is a different procurement conversation from one about student projects.

🔴 **What to tell the client honestly.** The standards layer is mature; **the agent binding is one
unmaintained 15-star repository and you are adopting it.** `learnmcp-xapi` and `pylti1.3` are the
two components to price as *owned*, not *consumed*. 🔴 **And no repository in this stack has been
code-audited by this KB** — the licences are payload-verified and the activity is metadata-verified,
but *"uses the public REST API"* is read from descriptions, not source. **Read the code in week one.**

🔴 **Where this pattern does not apply, and say so early.** The LATAM national systems
(SIGAA, SUAP, SIU-Guaraní, SAES, Q-Acadêmico) and the EMEA K-12 platforms (Librus, EduPage, Pronote,
IServ) **publish no LTI, no OneRoster and no Ed-Fi.** There is no sanctioned door to walk through,
which is why that supply is scrapers. For those clients the route is **`P8`** (negotiate with the
vendor) or **`P10`** (work inside the institution's own mandate), not this.

## P12 — Assessment and feedback agent built for the 2027 clocks *(new, p134)*

🟢 **Why this pattern exists separately from `P1`:** assessment and feedback is the **fastest-growing
segment of this market (44.36% CAGR,** `intel/market.md`**)** and simultaneously **the most regulated
activity in every region this KB covers.** Those two facts are usually treated as a tension. 🟢
**They are the offer:** build the fast-growing thing in the way the compliance clocks will require,
and the compliance work becomes the differentiator instead of the tax.

**The three clocks, which are closer than they look:**

| jurisdiction | obligation | date |
|---|---|---|
| **EU** | education uses in **Annex III high-risk**; 🔴 **emotion inference in education prohibited outright since 2025-02-02** | 🔴 **2027-12-02** |
| **Oklahoma** | every district to adopt a written AI policy | 🔴 **before the 2027-28 school year** |
| **Maryland** | an **AI coordinator** per school system; AI literacy in state standards | 🔴 **by June 2027** |

**The build:** `P11`'s stack, with the agent specialised to **grading open-ended responses and
generating feedback**, plus:

- 🔴 **No affect, emotion or behavioural inference, at all.** Prohibited in EU education settings
  since 2025-02-02 and the single fastest way to make the deliverable unshippable. This rules out
  three of the four permissive proctoring rows in `agents/top.md` by construction.
- 🟢 **Human-in-the-loop on every grade that reaches a student**, logged, with the model's rationale
  retained. AGS write-back happens **after** review, not instead of it.
- 🟢 **Every decision written to the LRS as xAPI** — which is what turns "we had oversight" into
  evidence that oversight happened.
- 🟢 **Evaluate against a real benchmark and say which:** [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench)
  for pedagogical quality, [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset)
  for known maths-tutoring failure modes. 🔴 **Both are ungranted — run them, cite them, ship
  neither** (`P6`, `T7`).
- 🟢 **Exam/item plumbing, if the client needs it:** [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp)
  (MIT, corporate holder, **writes off by default**, LTI path) is the most procurement-friendly
  assessment connector on the shelf.

**The counterparties p134 adds, which make this sellable rather than speculative:**

- 🟢 **UNIwise ApS (Denmark)** — a Nordic/UK digital-assessment vendor publishing its **own MIT
  integration packages** covering **assessor allocation and grade passback**
  ([`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages),
  licence payload-read, holder *"UNIwise ApS"*). **A vendor that already ships a permissive
  integration path is the shortest route to a sanctioned assessment engagement in EMEA.**
- 🟢 **Jisc's AI marking and feedback pilots across 38 UK colleges and universities** — a named
  sector programme already running, and the obvious place to look for outcome evidence rather than
  vendor claims.
- 🟡 **Open Assessment Technologies (Luxembourg)**, vendor of **TAO**, publishing
  [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) — 🟡 GPL-2.0, so read
  before forking.

🔵 **The demand signal to open the conversation with:** UK university student AI use went from
**66% to 92% in one year**, and in LATAM **87% of universities use AI while 26% have a strategy and
9% evaluate it.** 🟢 **Nobody is arguing about whether students use AI. The unanswered question is
whether the institution can show what its own AI did** — and that is this pattern.

## 🟢 P13 — The identity broker in front of a standards MCP server *(new, p135; **rewritten by p136 from BUILD to BUY-AND-ADAPT**)*

### 🆕 p136 — the broker is a product now, and only the adapter is yours

**Pass 136.** p135 wrote this pattern around **"your ~300 lines"** because no row in this KB
terminated a verified identity before calling an MCP server. 🔴 **`ACTION BS` probed the
professional register and found six repositories that do**, so the middle row of the stack table
below is **no longer bespoke**:

| layer | p135 said | 🆕 p136 says |
|---|---|---|
| Identity termination (LTI) | `Cvmcosta/ltijs`, Apache-2.0 | 🟢 unchanged |
| **Broker** | 🔴 **"your ~300 lines"** | 🟢 **BUY**: [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (**Apache-2.0**, Go, MCP auth spec **2025-11-25**, RFC 9728 + 8707 + 9068, JWKS-verified upstream OIDC, PKCE, DPoP, token exchange, **56 test files**) — or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (**Apache-2.0**, 60★) to front an existing MCP server *"without code modification"* |
| **LTI→broker adapter** | *(not separated out)* | 🔴 **BUILD — and this is the only bespoke code on the path.** Map the verified launch's `sub`, roles, `deployment_id`, course context and AGS endpoints onto the broker's subject, audience and scopes |
| Agent surface | `bb-mcp` / `learnmcp-xapi`, MIT | 🟢 unchanged — and behind the gateway they need no edits |

🔵 **Why the broker existed where nobody looked.** It was built by the **cloud-infrastructure**
community for MCP generally, not by edtech: querying `mcp oauth resource server` finds it,
`ai education identity` does not. 🟢 **That is clause 5 of `agents/top.md`'s vocabulary rule paying
for itself**, and it is the reason this pattern's price drops by weeks.

🔴 **What is NOT bought, stated precisely.** None of the six terminates an **LTI 1.3 launch**; they
terminate OIDC, OAuth and managed IdPs. LTI's launch is OIDC-shaped and `ltijs` already verifies it
correctly, so the adapter is a mapping rather than a protocol implementation — but it is **yours**,
it is where the security review will look, and `topic:lti` + `topic:mcp` across all of GitHub is
**two repositories, neither implementing LTI**.

🟢 **Revised engagement shape: 3–4 weeks, not 4–6.** Week 1: LTI developer key and a verified
launch (unchanged). Week 2: stand up `mcp-oauth` or the gateway against the institution's IdP —
configuration, not code. Week 3: the adapter, with the same two tests p135 specified (an unasserted
subject is refused; `role:admin` cannot be self-granted) **plus one the bought component makes
cheap** — that a token minted for course A cannot be replayed against course B, which is RFC 8707
resource binding and already implemented. Week 4: the security review.

🔵 **One caution that comes with buying.** `giantswarm/mcp-oauth` is **14★**. The capability is
excellent and the bus factor is not; `atrawog/mcp-oauth-gateway` (60★) and
[`NapthaAI/http-oauth-mcp-server`](https://github.com/NapthaAI/http-oauth-mcp-server) (108★, MIT)
are the alternates, and a client's security team will ask about exactly this. **Vendor-in the
component, pin the version, and read the 56 tests — they are the strongest evidence any of the three
offers.**

---

**Why this pattern exists** *(p135's original, kept because the mechanism is unchanged)*. p134 established that the sanctioned path (P11) removes the credential
blocker, and that is correct: a tool launched over LTI holds no user credential. 🔴 **p135 read the
source of all three agent bridges and found that two of them accept the user's identity on trust**
(`intel/trends.md` → `T13`, `agents/top.md` → `ACTION BL`). **P11 as written ships an MCP server
that will act on whatever subject the caller claims.** This pattern is the missing component, and it
is small.

### The problem, in one table

| component | what it proves about the user |
|---|---|
| `Cvmcosta/ltijs` (Apache-2.0, 373★) | 🟢 **Verified.** Platform-signed JWT, signature checked against platform keys, nonce tracked |
| `nitsuah/bb-mcp` (MIT) | 🔴 **Nothing.** `caller_identity` is a tool argument the client fills in; the README states it is *"trusted at face value"*, and `role: "admin"` bypasses the course-entitlement gate |
| `DavidLMS/learnmcp-xapi` (MIT) | 🔴 **Nothing.** The actor is `ACTOR_UUID` from the environment — one process per student |

🔵 **So the verification exists at the LMS boundary and is thrown away before the agent acts.** The
broker's whole job is to carry it across.

### The stack

| role | component | licence |
|---|---|---|
| Identity termination | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — LTI 1.3 launch, OIDC, signature verification, nonce replay protection | 🟢 Apache-2.0 *(hash-verified, p135)* |
| Broker | ~~**your ~300 lines.**~~ 🆕 **p136: BUY IT.** [`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) (Apache-2.0) or [`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (Apache-2.0). What stays yours is the **LTI→broker adapter**: map the launch's verified claims onto the broker's subject, audience and scopes | 🟢 **Apache-2.0** *(payload-read, p136)* |
| Agent surface | [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) or [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi), called **only** by the broker | 🟢 MIT *(both hash-verified)* |
| Record | the institution's LRS (xAPI) or the platform's own API | — |
| Audit | `bb-mcp`'s structured access log, SHA-256-hashed subjects, kept | 🟢 MIT |

### How it wires together

1. The user launches the tool from the LMS. `ltijs` validates the `id_token` signature against the
   platform's JWKS, checks the nonce, and yields **claims the institution signed**: subject, roles,
   context (course), and the AGS/NRPS endpoints available for this launch.
2. The broker mints a **short-lived token** carrying only those claims, scoped to that course.
3. Every MCP call goes through the broker, which fills `caller_identity` **from the verified claims,
   never from the agent**. The MCP server's own RBAC, FERPA gate and course-entitlement check then
   operate on a subject that was actually proven.
4. 🔴 **Network-close the MCP server.** `bb-mcp` fails closed without `MCP_API_KEY` and TLS on a
   non-loopback host — keep that, and additionally make the broker the only route to it. Its
   `MCP_API_KEY` authenticates *the client*, not the user; the broker supplies the user.
5. Writes (grade passback) go over **LTI AGS** where available, so the write is authorised by the
   same launch that authenticated the user.

### Why it wins the room

🟢 **It is the answer to the only question that stops these projects in security review:** *"what
stops the agent claiming to be someone else?"* With P11 alone the honest answer is "nothing, we
trust the client application" — which is `bb-mcp`'s documented design and a finding in any audit.
With P13 the answer is **"the LMS signed it, we verified the signature, and the agent never supplies
the subject."**

🔴 **State the FERPA/GDPR consequence plainly to the buyer.** `bb-mcp` gates its restricted tools on
a `ferpa_authorized: true` flag that **the calling application asserts**. Unbrokered, that flag is
the agent asserting its own authorisation to see protected education records. Brokered, it is
derived from a verified role. **That is the difference between a control and a comment.**

### Shape of the engagement

**4–6 weeks.** Week 1: LTI developer key in the client's LMS and a working verified launch.
Weeks 2–3: the broker, with tests that prove an unasserted subject is refused and that `role:admin`
cannot be self-granted. Weeks 4–5: wire one MCP server behind it, one read tool and one write tool.
Week 6: the security review the client was always going to run.

🔵 **What it does not solve.** It does not make `learnmcp-xapi` multi-tenant — that repo is one
process per `ACTOR_UUID` and last saw a commit on **2025-08-29**, so budget a fork. It does not give
you Caliper analytics, which have **no open-source client at all**. And it does not remove the need
for P6: brokered identity makes the audit trail trustworthy, not the pedagogy effective.

## 🟢 P14 — Standards-native content and assessment pipeline *(new, p135)*

**For the client that asks for AI-generated course content or assessment items and needs them to
work in the LMS it already owns.** p135's register found that the content and assessment standards
carry far more code than this KB had recorded, and all the pieces below are permissive **except
where flagged**.

| role | component | licence |
|---|---|---|
| Item authoring | [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) — Markdown → QTI 3.0 XML; 🟢 carries the topic `agent-tool` | 🟢 MIT |
| Item rendering/preview | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (30★) or [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) (TypeScript, pushed 2026-10-09) | 🟢 MIT |
| Assessment engine | [`numbas/Numbas`](https://github.com/numbas/Numbas) — **Newcastle University**, strongest for mathematics, SCORM-packageable | 🟢 Apache-2.0 |
| Course packaging | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) (630★) — responsive, accessible, multi-language, emits SCORM **and** xAPI | 🔴 **GPL-3.0 — run it, do not link it** |
| Runtime/tracking | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (354★) — SCORM 1.2/2004, **offline-first** | 🟢 MIT |
| Legacy migration | [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) — QTI 2 → QTI 3 | 🔴 **GPL-3.0** (holder: **Stichting Cito**) |
| Conformance | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) for badges/CLR; `googleworkspace/oneroster-integration-conformance-tests` for rostering | 🟢 Apache-2.0 |

**How it wires together.** The agent generates items as **Markdown**, not as XML — `markdown-to-qti`
owns the schema so the model never has to. Items render in the QTI player for human review before
anything ships. Reviewed items go into Adapt (run as a tool; the client owns the output) or Numbas
for maths, and export as a **SCORM package** the client's existing LMS already knows how to ingest.
`scorm-again` carries the runtime client-side, so completion tracking survives a lost connection and
reconciles later.

🟢 **Why this shape and not an LMS plugin.** Nothing in it touches platform source, so it is
licence-neutral with respect to the client's LMS — it works against Moodle (GPL), Canvas (AGPL),
Open edX (AGPL) and OpenOlat (Apache) identically, because **a SCORM package is a SCORM package.**
That is the same argument P11 makes for launch and rostering, applied to content.

🔴 **Two licence traps on this path, both measured this pass.** Do **not** reach for
`pipwerks/scorm-api-wrapper` (**391★ and no licence file of any kind** — use `scorm-again`), and do
**not** reach for `cybercussion/SCOBot` (**164★, CC-BY-SA-4.0, and the file is only the
human-readable deed** — a ShareAlike content licence on code, with no patent grant). Both are
popular, which is exactly why they get picked by default.

🔵 **What it does not solve.** Accessibility still needs human review — Adapt is built for it, which
helps, but generated content is not conformant because the framework is. And there is **no
conformance suite for QTI**, so "the item is valid QTI 3" rests on the player accepting it.

## Pattern selection, one line each

| if the client… | run |
|---|---|
| already runs Canvas/Moodle and wants control | **P1** |
| serves low-connectivity learners | **P2** |
| faces a US state mandate with a date | **P3** |
| is an EU institution touching admissions/grading | **P4** |
| is a ministry facing a curriculum mandate | **P5** |
| is a Brazilian or Argentine institution on SIGAA / SUAP / SIU-Guaraní | **P10** |
| wants a teacher's admin time back, with a measurable baseline | **P10**, then **P9** |
| will be asked whether it worked | **P6** — always, alongside the others |
| runs **Moodle** and wants to own its AI layer | **P7** |
| is the **vendor** of a national K-12 platform, or runs one at scale | 🆕 **P8** |
| wants **administrative** automation and will run open-source as its record | 🆕 **P9** |
| 🆕 runs **any LTI-compliant LMS** and the build must pass a security review or DPIA | 🟢 **P11** — *the new default where P1 was the old one* |
| 🆕 wants **AI grading or feedback**, in the EU, Oklahoma or Maryland | 🟢 **P12**, on **P11**'s stack |
| 🆕 is a **US K-12 district or state agency** with an Ed-Fi ODS | 🟢 **P11**, via `edfi-oneroster` |
| 🆕 is an **assessment platform vendor** rather than an institution | 🟢 **P12** — and see UNIwise as the precedent |
| 🆕 will put an agent in front of a **system of record**, or faces a security review or DPIA | 🔴 **P13 — mandatory, and before P11 ships, not after** |
| 🆕 asks for **AI-generated course content or assessment items** for an LMS it already owns | 🟢 **P14** |
| 🆕 needs tracked content delivery to work **offline** | 🟢 **P14** (`scorm-again` is offline-first), with **P2** |
| 🆕 is a **German-speaking-Europe** institution wanting off Moodle's GPL | 🟢 **OpenOlat** as the base (Apache-2.0 + attribution), then **P11** |
| 🆕 runs **Brightspace / D2L** | 🟢 **P11** shape with [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) (MIT) as the read surface — 🔴 **behind P13**, and audit its write surface first: it was not source-read |
| 🆕 asks *"can we buy the identity layer rather than build it?"* | 🟢 **P13 as rewritten by p136** — buy `giantswarm/mcp-oauth` or `atrawog/mcp-oauth-gateway` (both Apache-2.0), build only the LTI adapter |
| 🆕 **ships any open-source component to a client** — so, every engagement | 🟢 **P17** — two days to wire, and it catches the defect `npm ls` and manifest-reading licence scanners both report as `MIT` |
| 🆕 will attach an **AGPL-3.0 connector to a GPL platform** (the **P7** route) | 🔴 **P17 first, as a blocking gate** — `moodle-mcp-server-aql` declares AGPL-3.0 over 141 shipped paths and ships no licence text |
| 🆕 runs **Canvas** and wants the broker wired without forking anything | 🟢 **P13 fourth revision** — implement `OAuthStore`, `putGrant` the per-user Canvas refresh token, pass it to the server constructor |
| 🆕 runs **Moodle** and wants a permissive connector with its own test discipline | 🟢 [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (**MIT**, Go, committed `go vet`/`staticcheck`/`-race`/coverage) — 🔴 **but audit its write surface: 19 tools in source, 14 documented, and `submit_journal` and `update_assignment` appear in neither** |
| 🆕 wants to **reuse an open skills/prompt library** in a client deliverable | 🔴 Read the licence first: `GarethManning/education-agent-skills` is **CC-BY-SA-4.0 by deed** (847★) — **ShareAlike propagates into the client's adaptations** |

**Cross-cutting constraints.** Prefer **LTI 1.3** over forking any AGPL platform. Never ship
emotion recognition into an EU deployment. Treat unlicensed components as unusable
until counsel clears them, however many stars they have — and treat **`NOASSERTION` as "unread",
not "unusable"**: GitHub reports it whenever its matcher does not recognise a `LICENSE` file, and
this KB has now resolved **both** such rows by reading the payload (`openeducat_erp` → **LGPL-3.0**,
8 241 B; `OpenOLAT` → **Apache-2.0 with two attribution statements**, p135). 🔴 **And `NOASSERTION`
is biased towards institution-derived projects**, because appending institutional attribution is
exactly what defeats a licence matcher — so the rows it mislabels are disproportionately the ones an
education engagement most wants to use (`intel/trends.md` → `T14`).

🆕 **p136 splits `NOASSERTION` once more, because two of its causes have opposite remedies.**
**(a) GRANTED, BODY ELSEWHERE** — the grant is declared in a manifest, a source header or a URL
rather than in a `LICENSE` file. `pipwerks/scorm-api-wrapper` declares *"MIT-style license"* in
`package.json` **and** in `src/JavaScript/SCORM_API_wrapper.js`; `GarethManning/education-agent-skills`
and `cybercussion/SCOBot` ship the **Creative Commons deed** with the legal code off-repository.
🟢 **Remedy: read the manifest and the file headers before concluding anything, and fetch the named
standard text from the SPDX mirror on GitHub** — which works even when the publisher's own host is
unreachable. 🔴 **But a *bespoke* referenced text (`pipwerks`' personalised "MIT-style") stays
genuinely unknown: that one needs a question to the author.**
**(b) THE GRANT WAS DROPPED BY A COPY** — [`0awei0/kt`](https://github.com/0awei0/kt) re-uploads an
**MIT** project in one commit without its `LICENSE` file. 🟢 **Remedy: resolve the lineage and read
the UPSTREAM's grant** (`compose/code/p136-lineage-verdict/`, `intel/trends.md` → `T15`).
🔵 **One line to carry both: ask where the grant IS, not whether a file is.**

Pin commits for repos with no releases. **Benchmarks and datasets need the same licence
screen as code** — the two education benchmarks that exist are both ungranted.

🆕 **Three cross-cutting rules added by p132:**

1. 🔴 **Distinguish three licence states, never conflate them.** **Granted-but-unmatched**
   (`NOASSERTION` over a real grant — `mcp-student-records` is **Apache-2.0** carried as a
   ~745-byte notice block; `openeducat_erp` is **LGPL-3.0** at 8 241 bytes), **silent** (no licence
   file — `sisu-mcp`, `sis-demo`, `DAU-buddy`), and **deliberately withheld**
   (`graduation-project-advisor`: *"Private / TBD"*). Only the first is buildable.
2. 🔴 **Check for mixed licences inside a single repo.** `krzysztofbury/librus-mcp` is **MIT at
   2.x** over a `legacy_reference/` directory that remains **GPL-3.0-only**. A whole-repo fork
   inherits the stricter term; exclude the directory or do not fork.
3. 🔴 **Never adopt a student-built portal connector as a dependency.** They authenticate as the
   pupil with a stored password against an unsanctioned platform, and the ones that work are the
   ones with 2FA disabled. 🟢 **Read them for the API surface map, then rebuild the auth layer**
   (`P8`).

🆕 **Three cross-cutting rules added by p134:**

4. 🟢 **Reach for the standard before the connector.** If the client's platform speaks **LTI 1.3**,
   **OneRoster** or **Ed-Fi**, that is the integration — and it is permissively licensed, vendor- or
   government-owned, and holds no user credential. **Scraping is for platforms that publish no door**
   (the LATAM national systems, the EMEA K-12 platforms), not a general technique.
5. 🔴 **`NOASSERTION` is not biased toward "actually fine" — it is biased toward "unusual".** This
   KB has corrected several `NOASSERTION` rows *upward* (`openeducat_erp` → LGPL-3.0,
   `mcp-student-records` → Apache-2.0) and that run created an expectation p134 broke:
   [`tha-guy-nate/tha-edfi-runner`](https://github.com/tha-guy-nate/tha-edfi-runner) is **MIT plus an
   added clause requiring a visible link to the repo or PyPI page in any publicly available
   application** — a **user-visible obligation inside the client's product**, not a notice in a
   THIRD-PARTY file. **GitHub's matcher was right to flag it.** Read the payload to find out *which*
   way it is unusual, and never to confirm that it is fine.
6. 🟢 **Ask for a conformance test and hand over its output.** `googleworkspace/oneroster-integration-conformance-tests`
   is currently the only one this KB has found, for any standard in this industry. **Where a
   conformance suite exists, running it is the cheapest credibility in the engagement; where none
   exists — LTI AGS, Ed-Fi, and all 43 portal connectors — "it works" is a developer's assertion,
   and that is worth stating in the proposal rather than leaving a client to discover.**

🆕 **Two cross-cutting rules added by p136:**

7. 🔴 **Resolve the repository before you cost the component.** Two rows can be one repository: p136
   measured **11** slug pairs on this KB's own pages with **identical git ref sets** — a rename or a
   transfer that GitHub still answers — plus **37** more that differ only in capitalisation. 🟢 **In
   a proposal this matters twice**: a "two independent implementations" claim can be one, and a
   "well-forked, actively maintained" claim can be one repository counted twice. **Check the ref set
   (`git ls-remote`), then the shared commits, then the dates** — `compose/code/p136-lineage-verdict/`.
8. 🔴 **A declared field is a claim; source and payload are measurements — say which you used.**
   Two source reads have each overturned a cell this KB had published: `learnmcp-xapi`'s docstrings
   name a **JWT** trust anchor the project has no dependency on (p135), and `ictexam-mcp`'s `lti`
   **topic** describes a separate Moodle module while the MCP server itself logs in with an admin
   **password** (p136). 🟢 **Before any auth or standards claim reaches a client deliverable, clone
   the repository and read the three files that matter** — the config loader, the HTTP client and the
   tool definitions. It took under ten minutes per repository in this environment.
