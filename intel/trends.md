---
industry: education
region: Global
updated: 2026-10-12
---

# Education — current trends

**Pass 139, 2026-10-12.** 🟢 **`T17` was fired at and survived.** p138 added it one pass ago and
registered its own falsifier: *if the grants live in source-file headers rather than licence files,
7 of 21 is an overstatement.* 🔴 **`ACTION CH` read every shipped text file in all 21 payloads and
found 0 of the 9 carrying their own header grant** — so `T17` holds and is now **strengthened**
with the clause below. 🆕 **`T18` is added**, and it is the operational half of `T17`: per-file
notice is practised by **1 of 21** rows, which is what decides whether a grant survives a partial
copy. 🔵 **No trend is added from the search channel this pass, because it returned nothing** —
11 searches, 0 new rows, 0 corrections, which is `T10` holding again.

### 🟢 p139 strengthens `T17`: the grants are not hiding in the source, and one "grant" was Meta's

| | |
|---|---|
| **the claim** | 🔴 An SPDX identifier without the text it names is **a third of the published education-connector shelf** — and the text is not elsewhere in the payload either |
| **the measurement** | **21** packages, all **sha1-verified** against the registry's own `shasum`. **9** ship no licence file *(independently re-measured, agrees with p138 exactly)*. 🔴 **0 of those 9 carry their own grant in a source header.** In **8 of 9** there is no copyright line, no SPDX tag and no operative licence sentence in any shipped text file |
| 🔵 **the near-refutation** | **1 of the 9 did** report a notice: `@owen-x-tech/canvas-mcp` 1.1.0, carrying `@license React … Copyright (c) Meta Platforms, Inc. and affiliates` at byte **1197** of a **572 657-byte** minified `dist/ui/mcp-app.html`. 🔴 **A bundler hoisted a dependency's notice into the header window**, and it points at a `LICENSE file in the root directory` the package does not ship. 🔵 **Position cannot attribute a notice** — the new rule treats a notice in minified output (any line over 2 000 B) as the bundle's, never the package's. Without that clause this trend would read as refuted by a React licence |
| 🔴 **what would overturn it** | A grant living where the probe does not look: a sourcemap, an extensionless script, a `LICENSE` spelled so p138's path matcher misses it, or authored source whose notice sits below the first 4 096 bytes. 🔵 The window is what separates a package's own header from a bundled dependency's text, but it is the assumption most likely to be wrong |

### 🆕 `T18` — a licence cell describes a tree; only a per-file notice survives a partial copy, and 1 in 21 has one

| | |
|---|---|
| **the claim** | 🔴 **Per-file notice is not a practice in the education-connector tier: 1 of 21 rows — 5%.** On the other 20, a single file lifted out of the package names no holder and no grant |
| **why it is not a restatement of `T17`** | `T17` is about packages with **no grant at all** (9 of 21). `T18` is about the **11 that are clean at the root and still unattributable file-by-file**. 🔵 A root `LICENSE` discharges redistribution of the *whole* package; it discharges nothing about the file a developer pastes into a client's codebase |
| **the one row that has it** | 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) **3.13.10**: `Copyright (c) 2026 Rohan Muppa … Licensed under MIT — see LICENSE file for details` in **100 of 118** shipped text files, **and the `LICENSE` ships**, so the reference resolves. 🟢 **56★** — neither the largest (547 paths) nor the most-starred row on the shelf |
| **what it changes in a room** | 🔴 *"It's MIT, just keep the notice"* is not actionable on this shelf. In 9 payloads there is no notice to keep; in 11 more it exists only as one root file that any partial copy drops. 🟢 **The deliverable is a notice-injection step in the build**, not a licence column in a slide |
| 🔴 **what would overturn it** | The same census run over a tier that is **not** npm-published TypeScript — the Java and PHP rows on this KB's standards and platform pages are the obvious test, and header notice is conventional in both. 🔵 **So `T18` is scoped to this tier and must not be generalised to the shelf's institutional rows until that runs** (`ACTION CJ`) |

### 🔵 p139 on `T10`: the search channel returned nothing, and that is now the dominant cost finding

🔵 **11 searches — 4 global, 1 each for North America, EMEA, APAC and LATAM — produced 0 new rows
and 0 corrections** anywhere in this KB. Every repo, platform, figure and institution surfaced is
already carried, several with **better provenance here than the channel supplied**: the channel
offered UNESCO IESALC's 87%/26% as *2026* data, where [`market.md`](market.md) records that the
fieldwork ran **August–October 2025** and must be quoted as a baseline.

🔴 **One item was genuinely absent from this KB and could not be verified in this channel**: Texas
**HB 149 (TRAIGA)**, in force **2026-01-01**. `capitol.texas.gov` and `agora.eto.tech` both fail
DNS resolution here, so the statute could not be read and **nothing is published from the vendor
summaries that did return**. Registered as `ACTION CK` with the exact question. 🔵 **The secondary
sources agree that TRAIGA carries no curriculum or school-training mandate** — education appears in
its regulatory **sandbox** list and via a government-deployer disclosure duty — **so the likely
finding is a negative one**, which is precisely why it must not be asserted before it is read.

**Pass 138, 2026-10-12.** p137's sixteen trends retained. 🆕 **`T17` is added — the first trend this
KB has measured at the distribution layer rather than the repository layer, and it reframes every
licence cell on every page.** 🟢 **`T13` is narrowed for the third consecutive pass and is now one
interface wide rather than one standard version wide.** 🟢 **`T14` gains its first measurement in the
under-claiming direction**, which is the more dangerous one. 🆕 **`T16` gains a scope element the
English-language read had missed.** Each change states the measurement and what would overturn it.

### 🆕 `T17` — a licence identifier is not a licence, and a third of a published tier proves it

| claim | 🔴 **An open-source licence cell sourced from a repository describes the repository, not the artefact a client installs — and for a third of the published education-connector tier the artefact carries no licence text at all.** |
|---|---|
| measurement | **21** education-LMS connector packages (Canvas, Moodle, Brightspace, EduBase), every tarball **sha1-verified against the registry's own `shasum`**, 21 of 21 matching. 🔴 **7 (33%) declare an SPDX identifier and ship no licence file; 2 (10%) declare nothing and ship nothing; 12 (57%) are clean.** [`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md) |
| 🔴 the sharpest case | `moodle-mcp-server-aql` **0.1.7** declares **AGPL-3.0** across **141 shipped paths** with no licence text, while its repository carries a canonical **34 523-byte** grant |
| the mechanism | `canvas-mcp-server` **2.2.3**'s packed manifest **names `LICENSE` in `files`** and ships 8 paths containing none. npm silently omits a `files` entry absent from the tree |
| 🟢 direction | **all nine are the repository being better than the distribution**; not one package shipped a licence its repository lacked. So this is packaging discipline, not misrepresented licensing |
| what it changes | 🔵 **Every licence column in this KB is now a claim about a repository.** For any row a client will `npm install`, the payload is a separate question with a separate answer |
| 🔴 **what would overturn it** | A re-run finding the licence files present — which would mean the probe's path matcher is wrong, so the matcher is tested against real and near-miss filenames (7 tests, all passing). Or a licence-header read showing the grants live in source files rather than licence files, which would make **7 of 21 an overstatement of the defect and an understatement of the obligation**. 🔴 `ACTION CH` was registered for exactly this and has not run |
| 🔴 scope limit | npm only; four platform families; one registry search each. PyPI, Maven, crates unprobed. `moodler-mcp` **is not on PyPI (404)**, so part of the shelf has no payload layer to measure |

### 🟢 p138 narrows `T13` a third time: the residue is one interface, and it is a published extension point

| p137's clause | p138's measurement, in source |
|---|---|
| *"the 1.3 half of the gap"* — no RFC 8707-bound token for an MCP resource server | 🟢 **Present and named.** [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) `src/auth/oauth/authorization-server.ts` (**978 lines**) implements **RFC 8707 §7** canonical resource comparison as `normalizeResource()`, with **PKCE S256** and **dynamic client registration**; `resource-server.ts` (195 lines) publishes `/.well-known/oauth-protected-resource` and checks the **audience** |
| *"an adapter of about two weeks"* between three components | 🟢 **Still about two weeks, and no longer an estimate of unknown work.** `CanvasMCPServerConfig` accepts `oauthStore?: OAuthStore` — *"Embedders may supply their own implementation"* — and `OAuthStore` exposes `putClient`, `putGrant`, `putToken`, over a `Grant` carrying `CanvasConnection { refreshToken }` |
| 🔴 what still does not exist | 🔴 **An external verified subject cannot be injected.** The subject is established by `CanvasOAuthClient`, which redirects the user to Canvas. No code path accepts an LTI 1.3 assertion |

🟢 **So `T13` reduces to: the LTI→MCP seam is one store implementation, and it forks neither
library.** 🔴 **Overturned if** either library requires a patched release in practice — the
interface is published but the integration was **not executed** this pass, and `store.ts`'s
*"Update only, never create (QA S7, #356)"* comment on the Canvas-refresh path means the adapter
must `putGrant` before the first token call rather than relying on an upsert.

### 🟢 p138 extends `T14`: capability metadata drifts in BOTH directions, and under-claiming is worse

🔵 **`T14` has been measured only on over-claiming — connectors whose descriptions promised more
tools than they had. The first source-read of this pass drifts the other way.**

| repo | source | documented | 🔴 undocumented |
|---|---|---|---|
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (**MIT**, Go) | **19** tools (`mcp.NewTool`) | **14** | `download_resource`, `get_journal_entry`, `list_resources`, 🔴 **`submit_journal`**, 🔴 **`update_assignment`** |

🔴 **Two of the five are writes.** A client reading this README concludes the server is read-only;
it is not. 🔵 **For an education deployment that is a governance fact, not a documentation nit** — the
write surface is precisely what a data-protection review covers, and here it is larger than the
document the reviewer is handed. 🟢 **The clause `T14` gains:** *a tool count in a description is not
a measurement — and neither is its absence.*

🟢 **And one of `T14`'s recorded conflicts resolves in source, in the reassuring direction.**
`canvas-mcp-server@2.2.3`'s `build/index.js` registers **exactly 54** tools, all `canvas_`-prefixed,
against a HEAD README claiming **"50+ Tools"** — agreement. The surviving *"102 vs 126"* conflict
belongs to [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) and is
unchanged. 🔴 **`ACTION CI` therefore remains PARTIALLY discharged** — two repositories, not the tier.

### 🆕 p138 adds a scope element to `T16`: psychological assessment is in Vietnam's education list

🟢 **`T16` — that the first binding education-AI conformity regime in force is Vietnam's, not the
EU's — is unchanged and firms up.** Decision **33/2026/QĐ-TTg** was signed **2026-06-30** by Deputy
PM **Hồ Quốc Dũng**, in force **2026-08-15**, under 🆕 **Nghị định 142/2026/NĐ-CP**.

🆕 **The education entries include `đánh giá tâm lý` — psychological assessment** — which p137's
English-language read did not record alongside uncontrolled-source self-study content, automated
grading and behaviour monitoring. 🔵 **This catches a product class a vendor would not self-file as
high-risk**: wellbeing screening, engagement scoring and at-risk prediction are none of them
"grading" and none of them "biometrics".

🔴 **The transition date remains contradictory in Vietnamese sources too** — **2027-09-01** for
health/education/finance with **2027-03-01** for other listed sectors in one, a general
**2027-03-01** in another whose visible scope list omits education. 🔵 **Plan against 2027-03-01**:
a client ready for March is ready for September, not the reverse. 🔴 **The gazette
(`congbao.chinhphu.vn`) does not resolve in this channel** — primary source, secondary transport,
third pass running.

**Pass 137, 2026-10-11.** p136's fifteen trends retained. 🔴 **`T13` is rewritten for the second
consecutive pass, and this time by source code rather than by a better query**: the mapping it
called absent is library code owned by a US university. 🟢 **`T14` extends from licence metadata to
CAPABILITY metadata** — four of four connectors in one fork family contradict themselves about their
own tool count. 🟢 **`T15` survives its own falsifier by a factor of ten** (50% against a 5%
threshold) and gains the clause that makes it usable. 🆕 **`T16` is added: the first binding
education-AI conformity regime in force is Vietnam's, not the EU's.** Each change states the
measurement and the condition that would overturn it.

### 🔴 p137 rewrites `T13`: the LTI→OAuth-subject mapping exists, and the residue is one standard version wide

| p136's clause | p137's measurement, in source |
|---|---|
| *"Nothing maps a verified LTI 1.3 launch onto a broker's subject and audience"* | 🔴 [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) (**LGPL-3.0**, Kansas State University, HEAD 2026-09-30) maps a verified launch onto a **per-user** OAuth grant: `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → `/login/oauth2/auth` for that user → Canvas **as** that user |
| *"the whole remaining bespoke surface of the sanctioned path"* | 🟡 **Narrower**: the mapping is anchored on **LTI 1.1** (OAuth 1.0a consumer signing) and returns a platform API token, **not** an RFC 8707-bound token for an MCP resource server |
| *"none of the six brokers terminates an LTI launch"* | 🟢 **Still true**, and now accompanied by its mirror image: a 9★ education-native row, [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (**MIT**), *is* an OAuth 2.1 authorization **and** resource server with RFC 9728 metadata and audience checks |
| *(unstated — assumed from READMEs)* | 🔴 **`ltijs` v7.0.7 confirms the gap in code**: its only outbound token is `client_credentials` with `{sub: platform.clientId, iss: platform.clientId, aud: platform.authorizationServer}`. **The tool is the subject by design**, and the launch user's `sub` is stored and never leaves |

🔵 **The trend statement that survives**: *the credential blocker was solved, the
identity-assertion blocker was solved twice in parts, and what remains is an adapter between two
standard versions.* 🔴 **Falsifier for the next pass**: if `ltijs` v7's `LaunchContext` cannot hand a
verified `sub` to `canvas-lms-mcp`'s authorization server without forking either library, the
adapter is bigger than two weeks and this clause is wrong (`ACTION CE`).

### 🟢 `T14` extended — from licence metadata to CAPABILITY metadata

`T14` says declared metadata is systematically wrong in the direction of institutional code. 🔴 **The
same defect now has a second, cheaper-to-measure form**: a connector's declared **tool count**.

| repo | About | README / manifest |
|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) **289★** | *up to 102 tools* | *up to 126 tools* |
| [`abr-Projects/canvas-mcp`](https://github.com/abr-Projects/canvas-mcp) (fork) | *80+ tools, 5 skills* | *101 tools, 8 skills* |
| [`lindsay-cheng/canvas-mcp`](https://github.com/lindsay-cheng/canvas-mcp) (fork) | *102 tools* | *103 tools* |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) **103★** | *Version 2.2 · 54 tools* | README **v2.3.0**, `package.json` **2.3.1** |

🔵 **Four of four, including the upstream.** A KB row that quotes a tool count inherits the drift, so
this KB now counts from source: **136** for `EduBase/MCP` (57 get / 41 post / 24 delete / 10 patch /
3 put), **36** for `brightspace-mcp-server`, all read-only. 🔴 **And the same class covers standards
names used as product names**: `canvas-lms-mcp`'s *"New Quizzes (LTI)"* is Canvas's feature name —
the code reads `is_quiz_lti_assignment` and implements no LTI, so a topic- or keyword-level LTI probe
false-positives on it.

### 🟢 `T15` survives its falsifier by a factor of ten, and gains the clause that makes it usable

🔴 **`ACTION BY`: 10 of the 20 largest rows (50%) carry a licence file whose holder is not the
repository's own.** The refutation threshold was 5%. **224 591** tree paths, **316** non-root
licence-shaped files, **242** real grants (`compose/code/p137-foreign-holder-tree`, 12 tests).

🔵 **The new clause comes from reading it against
[`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md), which measured the
root licence **family** as complete **92%** of the time:**

> 🟢 **A root licence cell predicts what you may DO. It does not predict whom you OWE.**
> Family: 92% root-complete. Ownership: 50% root-incomplete, in the largest rows.

🔴 **Two instances that change a decision rather than a caution**: `instructure/canvas-lms` is
AGPL-3.0 at the root and ships **MIT** LTI Advantage code held by a named individual four levels
down; `classroomio/classroomio` is AGPL-3.0 and vendors **ten MIT agent-skills packs** held by
outsiders. 🟡 **And 50% is a floor**: the instrument reads licence *files*, so a grant inside a
source header — the `pipwerks` case — is invisible to it (`ACTION CH`).

## 🆕 `T16` — The first binding education-AI conformity regime in force is Vietnam's, not the EU's *(new, p137)*

🔴 **Vietnam:** AI Law **No. 134/2025/QH15** in force **2026-03-01**; Decision **No.
33/2026/QD-TTg** (issued 2026-06-30) **effective 2026-08-15** lists **46 high-risk AI systems** over
six sectors, **three of them education** — generating self-study content from uncontrolled data
sources, **testing/grading/ranking learners**, and monitoring learner behaviour with biometric data.
Duties: conformity assessment (third-party or self-assessment per the decision's pathway),
registration in the **National AI Database**, human oversight, incident reporting.

🔴 **The EU moved the other way on the same obligation class.** The Digital Omnibus on AI —
**Regulation (EU) 2026/1744**, in force **2026-07-27** — defers **Annex III** high-risk duties, which
is where education sits, from **2026-08-02** to **2027-12-02** (Annex I embedded: **2028-08-02**).
🟢 **Article 50 transparency was not deferred and applied from 2026-08-02**, with a grace period to
**2026-12-02** for systems already on the market.

🔵 **Why this is a trend and not a news item.** For three passes this KB has sold the EU's clock as
*the* compliance driver and recorded APAC as *"mandates and no market"*. 🟢 **Both halves flip**: the
jurisdiction with live education-AI conformity duties is in APAC, and the EU's live duty is the
*transparency* one — narrower, cheaper, and already late. A single engagement therefore splits into
two differently-shaped pieces (`compose/patterns.md` → `P15` for the EU, `P16` for Vietnam).

🔴 **Falsifiers, stated:** `T16` fails if Vietnam's decree text (read in Vietnamese, `ACTION CG`)
grants education systems a transition that runs past **2027-12-02**, since the EU's deferred date
would then arrive first after all; and it weakens if another jurisdiction is found whose education-AI
conformity duties were already in force before **2026-08-15**. 🔴 **Both sources for the Vietnamese
dates are law-firm briefings, and they contradict each other on the transition**, which is recorded
as a conflict rather than resolved.

---

**Pass 135, 2026-10-11.** p134's trends retained; 🔴 **`T12` is qualified by the measurement that
finished its own register — the sanctioned layer is not uniformly mature, and the variable is the
standard's AGE** — **`T10`'s probe rule is generalised from a fact about one word into a rule about
institutions** (`ACTION BM`), and **`T13` and `T14` are added**. Each trend states its evidence and,
where it matters, what would falsify it.

**Pass 132, 2026-10-11.** p131's trends retained; 🔴 **T8 and T9 are substantially corrected — both
had declared an absence that this pass filled** — **T4 and T10 are qualified**, and **T11 is added**
(see `README.md` → Pass 132). Each trend is stated with the evidence that supports it and, where it
matters, what would falsify it.

## T1 — The governance gap is the market

Student and teacher adoption has outrun institutional policy by an order of magnitude: **88%** of
students worldwide (95% of UK undergraduates) use generative AI, **60%** of US K-12 teachers used it
in 2024-25, and **18%** of US teachers have a written policy telling them how. This is the defining
condition of education AI in 2026. It means the buyer's problem is not capability — the tools are
already in the building — but control, evidence and defensibility.

**Consequence for engagements:** lead with inventory, data-flow proof, human-in-the-loop gates and
audit logs. A tutoring demo does not address the thing keeping the client awake.

## T2 — Mandates with hard dates replaced guidance

2026 is the year education AI rules acquired deadlines:

- **Ohio:** every K-12 district must adopt a formal AI use policy **by 1 July 2026**.
- **South Korea:** AI Basic Act in force **22 January 2026**.
- **India:** AI and computational thinking mandatory **from Class 3, 2026-27 academic year**.
- **China:** AI compulsory from age six since September 2025; Cybersecurity Law AI amendments
  effective January 2026.
- **Vietnam:** Decision 33/2026/QD-TTg names education — including automated assessment and
  behavioural monitoring — as high-risk.
- **EU:** AI literacy duties in force since February 2025; emotion recognition in education
  **prohibited** since 2 February 2025.
- **US states:** 134 bills across 31 states in 2026; 30+ states with guidance.

**The trend is not "regulation is coming" — it is "obligations are already in force and capacity is
missing."**

## T3 — The EU's high-risk clock slipped to December 2027, and that is a sales window

Annex III education obligations (admissions, grading, proctoring) were postponed to **2 December
2027** via the Digital Omnibus on AI. 🟢 **p131 closes p130's open question: the Council HAS adopted.**
A final Council green light is reported for **29 June 2026**, and this KB's own append-only pages
have carried the instrument as **Regulation (EU) 2026/1744 of 8 July 2026** for several passes.
p130's *"Council adoption was still outstanding"* was a regression against this KB's own record,
and an independent channel now corroborates the adoption. **The deferral is law, not a political
agreement.** Annex I embedded systems follow at **2 August 2028**.

Meanwhile what binds *now* is unmoved: Article 4 AI-literacy duties and the emotion-recognition
prohibition (both since February 2025), and **Art. 50 transparency, live since 2 August 2026**.

**Read it as:** ~14 months to build conformity in by design rather than retrofit it, not 14 months
of nothing to do. 🔴 **The old falsifier ("if the Council fails to adopt") is spent.** The live
falsifier is narrower: a further omnibus reopening Annex III, or a national regulator applying the
pre-deferral dates anyway.

## T4 — Supply is extraordinarily concentrated, and one repo is the whole mid-market

`HKUDS/DeepTutor` (Apache-2.0) stands at **41 136 stars**. The next education-specific agent found
this pass is `GarethManning/education-agent-skills` at 847 (and its licence does not resolve to an
OSI identifier), then `satvik314/educhain` at 388 and `vishalsachdev/canvas-mcp` at 288. There is
**no middle of this market** — one large permissive agent and a long tail of sub-1k projects.

**Consequence:** a client wanting "the open-source tutoring stack" gets DeepTutor plus bespoke
integration. Budget for the integration, not the engine.

🟡 **Qualified by p132 in two ways.** First, there is now a **second** repo at that scale:
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0, 39 444★**) — so the shape is two large permissive projects, not one, and the second
one is an *offline composition layer* rather than an engine. Second, the "long tail of sub-1k
projects" is **much longer and much better placed than this KB knew**: **36** SIS/portal rows at
0–40 stars (21 from p132, **15 added by p133**), ~90% region-placed. 🔴 **Licence mix corrected by
p133: p132's "~80% MIT" was measured before the LATAM and ANZ probes ran** — the 12 LATAM rows are
**42% MIT**, and the tier's new top row, `BetterSEQTA-Plus`, is **MIT at 40★**, which also retires
the "nothing above 10 stars" ceiling. 🔵 **The concentration finding holds for *engines* and is
misleading about *connectors*** — the connector layer is not concentrated at all, it is atomised
across national platforms, which is a different procurement problem and a different opportunity.

**Correction to this KB's own record:** earlier passes recorded DeepTutor at "~22k★" and then
"~24k★", and `educhain` at "~9k★" then "~12k★". Verified today: DeepTutor **41 136**, educhain
**388**. The educhain figure was overstated by roughly 30×. Star counts in this KB predating pass
130 should not be trusted without re-verification.

## T5 — Connector effort has pooled on Canvas, and fork swarms inflate the apparent supply

Five-plus Canvas MCP servers exist; eight of the fifteen platforms in `verticals/solutions.md` have
**no** AI-on-top project at all.

🔴 **Correction to p130's version of this trend.** It said Moodle *"has no permissively licensed MCP
route"*. Moodle has **eight standalone MCP servers, five of them MIT** — the tier p130's queries
missed because it looked only for in-tree plugins. The concentration claim survives; the Moodle
exception does not. 🟡 **But note what the permissive tier looks like:** the largest MIT one
(`peancor/moodle-mcp-server`, 43★) has not been pushed since February 2026, and the most-starred
Moodle connector overall (`loyaniu/moodle-mcp`, 40★) carries **no licence at all**. The permissive
rows and the active rows are different rows.

Worse, the apparent supply is padded by **fork swarms**: at least five repositories carry a
byte-identical `canvas-mcp` description under different owners, and `tutor-mcp` appears under two.
A fork-excluding search resolves each to a single canonical upstream
(`vishalsachdev/canvas-mcp`, `ArnaudGuiovanna/tutor-mcp`); one fork still advertises an older
tool count as current. Counting repos overstates the field substantially.

## T6 — Licence risk is concentrated exactly where the traction is

The most-starred education agent-skills collection (847★) reads as **NOASSERTION**. A 103-star
Canvas MCP server has **no licence file at all**. The cleanest Moodle→MCP route is **unlicensed**.
Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to OSI identifiers.

Meanwhile the platforms are mostly **AGPL-3.0** (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse,
ClassroomIO), which network-copyleft binds any client offering a hosted service. The permissive
shortlist is small and worth memorising: **Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT),
Academico (MIT), Richie (MIT), H5P (MIT), XBlock (Apache-2.0), codejail (Apache-2.0)**.

**Consequence:** licence review belongs at the start of an education engagement, not at hardening.
The highest-traction components are the riskiest ones.

## T7 — The measurement layer exists and cannot be shipped *(corrected by p131)*

🔴 **p130 stated this trend as "nobody measures learning" and called it the largest hole on the
shelf. That was false, and this KB's own pages refuted it.** Two real benchmarks exist:

- [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) — 43★, **ETH Zurich**,
  **EMNLP 2025 oral**, held in this KB **since pass 4**. Measures open-ended *pedagogical* capability
  (scaffolding, hint quality), not answer accuracy.
- [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) — 57★,
  **Khan Academy**, with its licence read in full by an earlier pass.

🔴 **The real constraint is the grant, and it is worse than a missing repo.** `mathtutorbench` has
**no licence field** and a README that names **two different licences in one file** (CC-BY-4.0 badge
vs CC-BY-SA-4.0 body); Khan's carries a **bespoke 2 690-byte "Evaluation Dataset License"**, not an
OSI one, and has been dormant since August 2024. **Both can be run and cited; neither can be shipped
inside a client deliverable without counsel.**

🟢 **The genuine gap, stated so it cannot regress again:** nothing open source measures **learning
outcomes** — durable gains in what a student knows. Both benchmarks measure *tutor behaviour*. The
OECD's 2026 Digital Education Outlook asks precisely for durable learning gains, and that standard
is still unmet.

**Still the most commercially valuable gap in the KB**, and now a cheaper build than p130 implied:
start from `mathtutorbench`'s task structure rather than a blank page, and anchor the quantitative
side on `OATutor` and `tutor-mcp`, which already expose Bayesian Knowledge Tracing mastery estimates
that an LLM's self-report cannot substitute for. See `compose/patterns.md` → P6.

## T8 — Offline and low-bandwidth stopped being an edge case

Kolibri (MIT, offline-first, content sync by LAN or USB) is the clearest instance of a trend driven
by where growth actually is: APAC at ~35.3% CAGR, India mandating AI from Class 3 across government
schools, LATAM adopting ahead of infrastructure, Google.org targeting 1.25M LATAM students by 2028.
Small local models make an offline tutor technically possible for the first time, and the data never
leaving the device resolves most of the privacy problem in T1 and T2 by construction.

~~**Nobody has built it:** no AI agent on top of Kolibri was found. MIT licence, offline design,
regulatory tailwind, no incumbent.~~

🔴 **CORRECTED BY p132 — somebody built it, at 39 444 stars.**
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0**) is an offline-first knowledge and education server that orchestrates containerised
tools: **Kiwix** for the library, **Kolibri** for the education platform, **Ollama** for the AI
assistant. It is the **second-largest repository in this entire KB**, behind only DeepTutor. There
is also a macOS port ([`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos),
20★) and an Indian Class-10 offline LMS claiming Kolibri integration
([`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI), 2★).

🔵 **Why the probe missed it, which matters more than the miss.** p131's `kolibri stars:>2` query
was valid: 86 repos, 3 in the Learning Equality family, 0 with AI. **NOMAD composes Kolibri as a
Docker container and never names it in its description.** A dependency is not always visible in the
metadata of the thing that depends on it — so "no project builds on X" cannot be concluded from
searching for X's name.

🟢 **The trend is intact and stronger; only the opportunity changed shape.** Offline is real, the
drivers above are unchanged, and the engagement is now *"deploy and extend a permissive 39k-star
stack"* rather than *"build it"* — faster and far easier to defend in procurement.
🔴 **The surviving gaps are narrower and genuinely open: nothing builds AI *inside* Kolibri**
(NOMAD attaches from outside; the Learning Equality repos carry none), **and nothing offline
targets LATAM** — the one curriculum-specific offline project is Indian, in the region this KB
argues needs offline most. **What would falsify the trend:** NOMAD stalling, or local-model quality
on commodity hardware failing to reach tutoring grade.

## T9 — Administrative automation is the most-cited driver and the least-served

Intelligent tutoring, personalised learning, administrative automation, AI-driven assessment and
virtual assistants are the standard trend list; administration is where institutions report the
clearest return.

🔴 ~~**There is still no open-source *agent* for a student information system** — no enrolment,
records or timetabling agent. That half of the trend holds, and it is now the largest genuine hole
in this KB.~~ **REFUTED BY p132, one pass after being promoted to "the largest genuine hole".**
There are **21 rows** (`agents/top.md`), including a **NEP 2020 timetable optimiser** (MIT), a
**FERPA-logging student-records server** (Apache-2.0, org-owned), an **Okta/SCIM** identity demo,
and a **standalone 42-tool classroom-management server** (MIT) — plus national portal connectors for
Librus, EduPage, Pronote, IServ, Sisu, uSaint, VTOP, QLDT, VSB and NYCU.

🔵 **The cause of the false absence was vocabulary, not supply.** Every probe asked for *"student
information system"*, *"school management"*, *"SIS"*. The builders name repos after the platform
they connect to. The query that worked was `timetable timetabling MCP` — **timetable access is the
one capability all of them implement.**

🟢 **The trend's core claim survives in a sharper form, and it is better for an engagement.**
Administration is still underserved, but not for want of software: **(a) nothing in the tier exceeds
10 stars**, so there is no production-grade row; **(b) the credential model is unsanctioned portal
scraping with a stored pupil password**, which no client security team will accept; and
**(c) all 21 connect to proprietary or institution-hosted portals — the open-source systems of
record have exactly zero agent coverage.** 🔴 **That last point is the useful inversion: connector
effort has gone to the platforms a studio cannot fork and avoided the ones it can.**

🔴 **The other half was wrong.** p130 said the only candidates are `openeducat_erp` *"(licence
unclear)"* and `academico`. The **platform** tier is at least six systems deep —
`frappe/education` (662★), `openeducat_erp` (**LGPL-3.0**, payload-read, not "unclear"),
`academico` (MIT, 404★), RosarioSIS (GPL-2.0), Gibbon (GPL-3.0), openSIS, Fedena — all restored in
`repos/foundations.md`. 🟢 **The constraint is licensing, not supply: exactly one of them
(`academico`, MIT) can become a closed derivative.** "No software exists" and "the software is
copyleft" lead to opposite engagement plans.

## T10 — The demand-side channel is a dating channel, not a fact channel *(corrected by p132)*

🔴 **Fourth consecutive pass in which the prescribed regional battery returned nothing this KB did
not already hold.** All four regional queries plus the four global ones were run this pass. **Zero
new tokens in all four regions.** Everything they returned was already on a live page here: the
Digital Omnibus deferral (2027-12-02 / 2028-08-02), Ohio's 1 July 2026 district duty, H.R. 8747,
California AB 1159, Idaho SB 1227, Vietnam's high-risk education listing, Korea's AI Basic Act
(22 January 2026), UNESCO IESALC's **87% adoption / 26% with a strategy**, the Digital Education
Council's LATAM faculty figures, the UNESCO LAC Observatory (14 April 2026), the UK's £4M
lesson-planning programme, the OECD *2026 Digital Education Outlook*, **134 bills across 31 US
states**, and the EMEA market at ~$2.64B.

🟢 **One thing the channel did add, and it is worth the battery on its own:** independent
corroboration that the **Council adopted** the Digital Omnibus (29 June 2026), which closes a
question p130 left open and repairs `intel/policy-matrix.tsv`. A saturated channel is not a useless
channel — it is a *confirmation* channel, and should be budgeted as one.

🟢 **The supply side moved, as it has every pass.** p131's new addresses all came from
layer-specific repo queries aimed at this KB's own declared gaps, not from the generic battery:
three MIT proctoring projects, and the restoration of two tiers p130 had declared absent.

**Consequence for how these passes are run:** spend the regional battery on *confirmation and
dating*, and spend the pass's real effort on gap-directed supply queries and on **auditing this
KB's own claims against its own pages.** Pass 131 found more by grepping this repository than by
searching the web.

### 🟢 p132: the streak broke in 4 of 4 regions — and the reason refines the trend

p131 counted a **fourth consecutive pass** of zero new tokens and recommended budgeting the battery
as a confirmation channel. Run again unchanged, it produced **new tokens in all four regions**.
🔵 **But not one of them is a new fact.** Every one is a **date, a denominator or a delivery
structure**:

| region | the new token | its type |
|---|---|---|
| LATAM | IESALC fieldwork ran **August–October 2025** | 🟢 **a date that re-ages a held figure** — the *87% / 26%* numbers describe late 2025, not now |
| LATAM | **200** institutions, **19** countries; **ILIA 2025 (CEPAL)** carries country-level regulation detail | a denominator and a named instrument |
| EMEA | UK **AI Adoption Summit, £200m+**; delivered by **Cisco/IBM/BT/Rolls-Royce**, curriculum by **Skills England**, *few education providers involved* | 🟢 **a delivery structure** |
| North America | **10%** of institutions have AI guidelines; **71%** of teachers untrained; **CMU + Gates $55M** on *gateway courses* | denominators and a capital target |
| APAC | **Australia/New Zealand** tightening governance; OpenAI appoints an ANZ policy lead | a jurisdiction this KB had never covered |

🔴 **So the trend as p131 stated it was half right and the half it got wrong is the operative
half.** The battery is not saturated — it is **saturated for facts and productive for provenance**.
Four passes called it dead because they only ever asked *"what is new?"*. Asking **"when was this
measured, who was counted, and who is being paid to deliver it?"** of the *same* results is still
productive, and the answers change how a figure may be quoted to a client.

🔴 **One stale claim is still circulating and a client may arrive holding it:** that the EU AI Act
puts education AI in high-risk *"with full effect in August 2026"*. The schools-facing Annex III
date is **2027-12-02** (T3). This KB has flagged it for three consecutive passes.

### 🟢 p135 generalises the probe rule: it is about institutions, not about words

p133 found that *"EMEA"* returns enterprise IT because it is **a vendor sales-region word no ministry
uses** (`P133-E`), and p134's `ACTION BK` confirmed it by re-probing EMEA country by country.
`ACTION BM` tested the other two regions this pass:

| bare probe | result |
|---|---|
| **"EMEA"** | 🔴 **Fails.** Enterprise IT outlooks, a 2023 enterprise-AI trust study, enterprise compliance commentary. One education source, and its event sat in **October 2024** |
| **"APAC"** | 🔴 **Fails identically.** Enterprise tech priorities, sovereign-cloud analysis, and vendor press releases. The run recorded finding **no** education-specific regulation, ministry rule or edtech market data |
| **"LATAM"** | 🟢 **Succeeds.** UNESCO **IESALC** (200 institutions, 19 countries, 87% using AI, 26% with a framework), the **Digital Education Council** LATAM survey 2026 (30 000+ responses), the **IDB** readiness index, and country-level regulatory posture for Chile, Brazil, Colombia and Mexico |
| **"North America"** | 🟡 **Partly.** Market-research geography segments dominate, but real findings surface (state-legislature activity, a $169M government commitment, a $55M CMU/Gates courseware investment) |

🔴 **So `P134-H` is not a fact about the word "EMEA", and stating it that way was too narrow.**
🟢 **The rule:** *a bare regional probe returns education material exactly when a region-scoped
education body publishes under that label.* Latin America has two — **UNESCO IESALC**, the
institute for higher education in Latin America and the Caribbean, and the **IDB**. "EMEA" and
"APAC" have no counterpart; no ministry, university network or multilateral addresses research to
them. "North America" sits in between because market-research firms use it as a reporting segment.

🔵 **Why this is worth more than the three results.** It is **decidable before searching.** Ask
whether a region-scoped education institution exists; if not, probe by country from the start.
🟢 **That is a standing method rule, and it predicted this pass's APAC result correctly** — the
country probe returned India's Class-3 mandate, Singapore's literacy framework and South Korea's
2026 work plan, none of which the regional probe could see.

### 🔴 p136 adds the missing clause: the INSTRUMENT'S LANGUAGE is part of the probe

p135's rule — *a bare regional probe works when a region-scoped education body publishes under that
label* — is right and **incomplete**, and `ACTION BT` found the hole. 🔴 **Japan has a body that
publishes prolifically, a dated national instrument, and a ministerial circular number — and p135
recorded Japan as MEASURED ABSENT**, because the probe ran in English while the instrument is
Japanese.

| probe form | result |
|---|---|
| English, country-level (`"AI education Japan policy"` family, p135's APAC sweep) | 🔴 **Nothing.** Japan was the one country in a five-country sweep that returned no instrument |
| 🟢 Japanese, by ministry (`文部科学省 生成AI 教育 ガイドライン`) | 🟢 **First attempt**: MEXT's own PDFs, the guideline Ver.2.0 of **2024-12-26**, circular **6文科初第1895号**, and the 2026-06-30 committee papers opening the Ver.2.1 revision |

🟢 **So the method rule now has three clauses, and all three are decidable before searching:**

1. **Does a region-scoped education body publish under that label?** If not, probe by country
   (p133/p134/p135).
2. 🆕 **In what language does that country's education ministry publish?** Probe in it. The
   ministry's own name is the highest-yield token — `文部科学省`, not "Japan".
3. **Name the instrument class, not the topic.** "Guideline", "circular", "curriculum" and their
   local words; a topic word returns commentary, an instrument word returns the instrument.

🔴 **The uncomfortable corollary, written down rather than left implicit.** This KB's **China**,
**Korea** and **Brazil** policy cells were all built from English-language sources about
non-English instruments. `ACTION BT` proved that shape can miss an entire national policy, so those
three cells are provisional until re-probed in 中文, 한국어 and português.

## T11 — The connector layer is being built bottom-up by students, not by vendors *(new, p132)*

🟢 **The strongest structural finding of this pass, and it reframes where supply comes from.** The
21 SIS/student-portal agents found this pass share a profile so consistent it is clearly a
phenomenon rather than a coincidence:

| property | value | what it implies |
|---|---|---|
| **author** | ~~one person, almost always a student~~ → 🔴 **not in LATAM or Australia** | p133: **4 rows serve a teacher**, one is **org-owned with a product homepage** (`expeditto`), and `BetterSEQTA` is a two-product org with 25 forks |
| **licence** | ~~**~80% MIT**~~ → 🔴 **tier-wide this is wrong; see p133** | 🟡 measured on 21 EMEA/APAC/NA rows. The **12 LATAM rows** p133 added are **42% MIT** (3 unlicensed, 2 GPL-3.0, 1 AGPL-3.0), and the one row p132 left unread reads **AGPL-3.0** |
| **stars** | **0–10**, none higher | no production-grade row anywhere in the tier |
| **created** | mostly within the last 6 months; three within 10 days of this pass | 🟢 the tier is *forming now* |
| **region** | **~90% placed** on hard evidence (named institution, national platform, country-coded host) | the best regional evidence in this KB |
| **target** | **proprietary** national platforms and university portals | 🔴 zero coverage of open-source systems of record |
| **auth** | the author's own portal password; unofficial; 2FA unsupported | 🔴 undeployable as published |

🔵 **Why this is happening, and why it will continue.** MCP made it a weekend's work to wrap a
portal an author already logs into daily, and the itch — *"when is my next class, what is my
attendance, am I on track to graduate"* — is universal. Nothing about that requires a vendor,
a budget, or permission.

**Consequences for a studio, in order of usefulness:**

1. 🟢 **The expensive part of a national-platform integration is already published under MIT.**
   Mapping Librus's or Pronote's undocumented surface is weeks of work; it is done and readable.
   **Keep the surface map, discard the auth layer, rebuild it sanctioned.**
2. 🟢 **These repos are a demand signal with a region attached** — and the only such signal this KB
   has. Two independent EduPage implementations is a better indicator of Slovak demand than any
   market report on this page.
3. 🔴 **None of it is adoptable.** A 1-star repo with a stored pupil password is a reference
   document, not a dependency. Say so to a client before they find it themselves.
4. ~~🔵 **Where it is NOT happening is the finding for LATAM:** zero of the 21 are LATAM-origin…~~
   🔴 **REFUTED BY p133, and this was a claim about a query.** Probing `sigaa`, `suap` and
   `siu-guarani` returns **12 LATAM rows**. The bottom-up wave had reached LATAM; the probe had not.
   🟢 **And it arrived in a different shape: LATAM's wave is partly *staff-side*** — `expeditto`
   (AGPL-3.0, org-owned, drafts a lecturer's RIT workload report), `auto-sigaa` and
   `Auto_Grade_Guarani` (both move grades into the national SIS for a teacher). See `T9`.
5. 🔴 **The structural risk of the whole tier now has a measured instance, not just a worry.**
   `st22209/Parent-Portal` (MIT, New Zealand, **KAMAR**) is **archived**, and its README gives the
   cause: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. **An unsanctioned connector does not degrade when
   the vendor changes an endpoint — it ends.** That is the argument for pattern `P8` as an observed
   outcome.

**What would falsify this:** a vendor (Librus, EduPage, Instructure, Moodle HQ) shipping an official
agent or MCP surface, which would make the student connectors redundant overnight — and which is
exactly the engagement to propose to such a vendor.

## T12 — The sanctioned-integration layer is mature, permissive and agent-less *(new, p134)*

🔴 **This is the trend that reframes `T5`, `T6` and `T11` at once, and it took four passes of
connector-counting to see.** `T11` says the connector layer is being built bottom-up by students
rather than vendors, and `agents/top.md` says the resulting credential model makes nearly all of it
undeployable. 🟢 **Both are true of the *portal* layer and false of the layer beside it.**

**The interoperability standards layer — LTI 1.3 Advantage, OneRoster 1.2, Ed-Fi, xAPI — is built,
permissive, and owned by exactly the institutions this KB keeps saying are absent:**

| the claim this KB has been making | what the standards layer shows |
|---|---|
| *"supply is extraordinarily concentrated and student-built"* (`T4`, `T11`) | 🟢 **`Cvmcosta/ltijs` — Apache-2.0, 373★, pushed 2026-10-06.** Larger and more active than the LTI row this KB already had |
| *"licence risk is concentrated where the traction is"* (`T6`) | 🔴 **Inverted here.** The platforms are AGPL/GPL/LGPL; **the standards layer is Apache-2.0, MIT and 0BSD** — the most permissive set of rows in this entire KB |
| *"no institutional or vendor owners"* | 🟢 **Ed-Fi Alliance, Google, the US DoD's ADL Initiative, the Minnesota Department of Education, France Université Numérique, UNIwise ApS, Blackboard, Open Assessment Technologies** |
| *"the credential model is a tier-wide blocker"* | 🟢 **A tool launched over LTI holds no user password at all** — it runs on a client ID the institution issues and can revoke |

🔴 **And here is the trend, in one sentence: the standards are finished and the agents have not
arrived.** The bridge from an AI agent to any sanctioned learning standard is **one repository** —
[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, 15★, last push
2025-08-29) — and **the only Ed-Fi MCP server in existence is an empty repository**
(`cdweaver1992/edfi-mcp-server`: `size: 0`, HTTP 404 on 15 probes across 3 branch refs, created and pushed in
the same second).

🟢 **Why this is a trend and not a single finding.** The direction of travel across every other
trend on this page points at it. `T9` (administrative automation is the most-cited driver and least
served) needs a system of record, and OneRoster/Ed-Fi *is* the sanctioned route into one. `T3` and
the 2027 compliance clocks reward auditable access over scraped access. The market's
fastest-growing segment — **assessment and feedback agents at 44.36% CAGR** — is precisely what
**LTI AGS grade passback** was designed to carry. 🔵 **Four independent pressures all terminate at
the same missing component, which is usually what a build opportunity looks like before anyone
builds it.**

🟡 **What would falsify this trend.** If an MCP-over-LTI/OneRoster server appears with real
traction in the next few passes, this stops being an opportunity and becomes a dependency — and
**that is the thing to watch for, because it would also be the fastest-moving row in this KB.**
🔴 **Equally, if the standards layer turns out to be shallower than its metadata suggests — the
Python LTI library is already ~2 years dormant and the xAPI bridge ~14 months — then "mature" is
too strong, and this pass will have over-read activity from stars and a single `pushed_at`.** No
repository in this tier has been code-audited by this KB.

🔵 **The regional asymmetry is part of the trend, not an aside.** LTI, OneRoster and Ed-Fi are
**North-American and European procurement standards**. The LATAM national systems (SIGAA, SUAP,
SIU-Guaraní, SAES, Q-Acadêmico) publish no equivalent, and APAC's only standards-tier rows are an
AGPL-3.0 project and a spec translation. 🔴 **So the sanctioned path is available where the
standards are, and the scraping is a symptom of their absence — not of a different builder
culture.** That is a materially different explanation from `T11`'s, and it is testable: it predicts
that LATAM supply stays unsanctioned until a national system publishes an API, regardless of who
builds it.

### 🔴 p135 qualifies `T12`: maturity tracks the standard's AGE, not its design

p134 stated `T12` as *"the sanctioned-integration layer is mature, permissive and agent-less."*
🟢 **The second and third clauses hold.** 🔴 **The first is true only on average, and the average
hides the thing a studio needs to know.** Finishing the register (`ACTION BN`) measured all six
remaining standards:

| standard | first published | largest repo | ★ | supply verdict |
|---|---|---|---|---|
| **SCORM** | **1999** | `adaptlearning/adapt_framework` | **630** | 🟢 **Deep.** Four repos above 350★; a permissive modern runtime; authoring tools |
| **LTI** | 2010 (1.3 in 2019) | `Cvmcosta/ltijs` | **373** | 🟢 **Strong and current** (pushed 2026-10-06) |
| **QTI** | 2000s (QTI 3 in 2022) | `amp-up-io/qti3-item-player` | **30** | 🟡 **Thin but real** — 15 repos, mostly MIT, several vendor-owned |
| **Open Badges** | 2011 (3.0 in 2022) | `1EdTech/digital-credentials-public-validator` | **17** | 🟡 **Thin, converging on W3C Verifiable Credentials** |
| **Comprehensive Learner Record** | 2010s | *the same validator* | **17** | 🔴 **One real row in existence** |
| **Caliper Analytics** | 2015 | `lsloan/udp-notebooks` | 🔴 **0** | 🔴 **No usable supply at all.** One repo, unlicensed, untouched since 2023 |

🔵 **The pattern is monotonic in age and has nothing to do with the standards' quality.** SCORM is
technically the crudest of the six and has the most code; Caliper is the most modern event model and
has none. 🟢 **The mechanism is deployment, not merit: SCORM and LTI are what institutions have
*bought* for twenty years, so there is installed base to write against.** Caliper and CLR are
procured rarely, so nobody has written a client.

🔴 **What this changes in a pitch.** *"We build on the sanctioned standards"* is credible for content
and launch (SCORM, LTI), **defensible** for assessment and credentials (QTI, Open Badges), and
🔴 **not currently true for analytics** (Caliper). A proposal that promises standards-based learning
analytics is promising a standard with **no open-source client**, which is a build the client should
be told about rather than a dependency.

🔵 **Falsifier.** If a Caliper or CLR client library appears above ~50★ with a permissive licence,
this reframing weakens and `T12`'s original wording is closer to right.

## 🔴 `T13` — The credential blocker was solved and replaced by an identity-assertion blocker *(new, p135)*

**This is the most consequential thing p135 found, and it only became visible by reading source.**

For four passes this KB has said the portal-connector tier is undeployable because every row holds a
student's password, and that the sanctioned path fixes it. 🟢 **The second half is confirmed:** of
the three bridges read this pass, **`ltijs` holds no user credential at all**, and the two MCP
servers hold an institution-issued *service* credential, never a student's password.

🔴 **But the sanctioned standard carries a cryptographically verified identity, and both agent
bridges to it discard that verification:**

| bridge | how the user's identity is established |
|---|---|
| `Cvmcosta/ltijs` | 🟢 **A platform-signed JWT, signature verified** against the platform's keys, with nonce tracking |
| `DavidLMS/learnmcp-xapi` | 🔴 **An environment variable** (`ACTOR_UUID`). 🔴 And its own docstrings claim *"Actor UUID from JWT"* while **the project has no JWT dependency at all** |
| `nitsuah/bb-mcp` | 🔴 **The caller's own assertion** (`caller_identity`), documented as *"trusted at face value"*. `role: "admin"` bypasses the course-entitlement gate; the app token is **org-wide** |

🔵 **Why this is a trend and not three bugs.** It is structural. MCP has no end-user identity model —
`bb-mcp`'s source says so in its first paragraph — so **every MCP server that fronts an institutional
system of record must either invent an identity model or accept one on trust, and the shipped
examples accept it on trust.** As agent-mediated access spreads from reading a portal to writing a
system of record, that choice stops being acceptable: a grade write attributed to an unverified
subject is an audit finding.

🟢 **The commercial consequence, and it is a component rather than a caveat.** The missing piece is
an **identity broker**: something that terminates a verified identity (an LTI launch, OIDC, or the
institution's IdP) and only then calls the MCP server with a subject it has itself established.
🔴 **No repository in this KB does this, in any region.** That is the clearest unbuilt component on
the shelf, it sits between two mature layers, and it is required by every engagement on the
sanctioned path. See `compose/patterns.md` → **P13**.

🔵 **Falsifier.** If an MCP server appears that verifies an LTI or OIDC assertion itself before
acting — rather than accepting `caller_identity` — this trend has been answered by the ecosystem and
becomes a build-versus-buy question instead of a gap.

### 🔴 p136: THE FALSIFIER FIRED, and `T13` is rewritten rather than restated

`ACTION BS` queried the **professional** register — `mcp oauth resource server`,
`mcp authorization server`, `token exchange rfc 8693` — because an authorization component is built
by people who do not say "education". 🔴 **Six repositories do exactly what the falsifier
describes**, and the best is Apache-2.0:
[`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) verifies the upstream OIDC
`id_token` against the provider's **JWKS**, binds and checks the nonce, **refuses to issue when the
provider returns no subject claim** (*"provider did not supply a subject claim"*, in its own error
path), and implements the MCP authorization spec of **2025-11-25** — RFC 9728 protected-resource
metadata, RFC 8707 resource binding, RFC 9068 JWT access tokens with published JWKS, PKCE, DPoP and
token exchange, with **56 test files** under `server/`.
[`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (Apache-2.0, 60★) puts
the same thing in front of **any** MCP server *"without code modification"*. Register and licences:
`agents/top.md`.

🟢 **So the trend's mechanism stands and its conclusion inverts.** MCP still has no end-user
identity model — that is why these six exist. 🔴 **What was wrong was the sentence "no repository
does this, in any region"**: it was true of *this KB's rows*, which is the weak kind of absence
claim, and p135 said so when it registered `ACTION BS` against its own finding.

🟡 **What survives, and it is now sharp enough to quote in a proposal.** None of the six terminates
an **LTI 1.3 launch**. The missing piece is no longer a component but an **adapter**: `ltijs`
already verifies the launch correctly, and nothing maps that verified launch — its `deployment_id`,
AGS scopes and roster context — onto a broker's subject and audience. 🔵 **Measured, not assumed:**
`topic:lti` + `topic:mcp` across all of GitHub returns **two** repositories, and **neither
implements LTI**.

🔵 **New falsifier for the rewritten trend.** If a repository appears that terminates an **LTI 1.3
launch** and then issues a broker token bound to that subject, `T13` closes entirely and `P13`
becomes a procurement decision with no bespoke code at all.

## 🟡 `T14` — Licence metadata is systematically wrong in the direction of institutional code *(new, p135)*

🔴 **Measured, twice, with a reason.** `P134-F` found that GitHub's `NOASSERTION` is *"biased toward
unusual, not toward fine."* p135 measured why, by hash-matching 26 licence payloads against
canonical SPDX texts (`compose/code/p135-licence-sha-identity`):

- 🔴 **A licence payload never matches its canonical text naively.** Real `LICENSE` files wrap at ~72
  columns; SPDX wraps at ~105. **Zero of 26 payloads were whitespace variants** — refuting the
  premise `ACTION BP` was written on.
- 🔴 **Matchers are defeated by punctuation.** SPDX's canonical GPL-3.0 uses curly quotes; the
  `COPYING` shipped in real repositories uses ASCII. That alone accounted for five payloads.
- 🔴 **And by the licence steward editing its own text.** Two such edits are known for GNU: the
  `http`→`https` change, and the FSF moving `why-not-lgpl.html` from `/licenses/` to `/philosophy/`.
- 🔴 **The bias has a cause: appended institutional attribution.** `OpenOLAT` is Apache-2.0 to the
  character and then carries two attribution statements for the University of Zurich's original OLAT
  base and frentix GmbH. `Citolab/qti-convert` fills GNU's appendix with its real holder —
  **Stichting Cito Instituut voor Toetsontwikkeling** — which is correct practice and makes the text
  non-canonical. 🟢 **Well-governed, institution-derived projects are the most likely to append
  attribution, so they are the most likely to be mislabelled.**

🔴 **The practical edge, because this is a procurement risk and not a curiosity.** In this corpus a
badge would have mislabelled an LMS a studio can use (`OpenOLAT`, permissive) and said nothing about
two it cannot: `pipwerks/scorm-api-wrapper` (**391★, 130 forks, no licence file at all**) and
`cybercussion/SCOBot` (**164★, and the licence file is the CC-BY-SA-4.0 human-readable deed, not the
legal code** — a ShareAlike content licence on software). 🟢 **Rule: on anything a client will ship,
read the payload and hash it. A badge is a lead.**

### 🔴 p136 extends `T14` from licences to DECLARED METADATA, and corrects its own example

🔴 **The `pipwerks` example above is wrong in the direction this trend warns about.** "No licence
file at all" is a statement about **filenames**; the repository declares an MIT-style grant in
`package.json` and in its source header. 🔵 **A trend about metadata being unreliable published an
unreliable metadata reading** — which is the most useful way to learn that *absence of a file* and
*absence of a grant* are different measurements. Corrected in full on `repos/foundations.md` and
`agents/top.md`.

🟢 **And the same defect exists one field over, in topics.** `topic:lti` + `topic:mcp` across all of
GitHub is **two** repositories:

| repo | what the topic claims | what the source does |
|---|---|---|
| [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | `lti` | 🔴 Logs in with `ICTEXAM_EMAIL` + `ICTEXAM_PASSWORD` and rides the web app's session cookie + CSRF. LTI 1.3 belongs to a **separate Moodle activity module** |
| [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) | `lti`, `scorm`, `xapi` | 🔴 None implemented. In the SDK, `scorm` and `xapi` are **lesson-type enum values** |

🔵 **Why topics behave like licence badges.** Both are **author-declared strings with no verifier**,
and both are read by tooling as facts. 🟢 **Rule, generalised: every author-declared field — licence
badge, topic, description, docstring (p135's `learnmcp-xapi` *"Actor UUID from JWT"*) — is a claim.
Source and payload are measurements. This KB's auth and standards cells must say which they are**,
and after two source reads that each overturned a published cell, the base rate for the connector
tier is **2 for 2**.

## 🔴 `T15` — A licence verdict belongs to a LINEAGE, not to a slug *(new, p136)*

Three of this pass's findings are the same finding seen from three sides, and together they break an
assumption every page of this KB rests on: **that a repository URL identifies the thing whose
licence you read.**

| what was measured | why the slug is the wrong key |
|---|---|
| 🔴 **A grant declared outside the LICENSE file.** `pipwerks/scorm-api-wrapper`: `package.json` + source header, body at an off-repository URL (`ACTION BR`) | The licence is in the **artefact**, not at the path a filename probe looks at |
| 🔴 **A copy that DROPPED the grant.** [`0awei0/kt`](https://github.com/0awei0/kt) re-uploads [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) in **one commit**, README byte-identical, **upstream's MIT `LICENSE` absent** | The row reads unlicensed; **the code is MIT**. The grant lives with the **upstream**, not with this slug |
| 🔴 **Eleven slug pairs that are ONE repository.** Identical ref sets after a rename or transfer — `jdolny`/`theopenem` `OneRoster.NET`, `KI-Campus/LRS`/`openHPI/openLRS` (`ACTION BU`) | Two rows, one licence, and this KB has already **reasoned about which owner to pin** |
| 🔴 **A grant that travels INSIDE a vendored file.** `numbas/Numbas` is Apache-2.0 at the root and carries `pipwerks`' MIT-style header four levels down, at a version **four years** behind upstream | A root licence is not the licence of the tree |

🔵 **Two earlier passes each found one face of this, and neither generalised it.**
`p742-grant-body-vs-reference` (p58) fixed the licence **file** that points elsewhere while carrying
the grant; `p969-root-only-licence-reach` (p93) found that a root probe cannot see a **per-directory**
licence. 🟢 **`T15` is the third instance and the one that names the common cause**: the grant's
location is not a property of the slug, and neither is the code's provenance.

🔵 **Why it is a trend rather than four incidents.** The sector's code moves by **copying**, not by
dependency resolution: `SCORM_API_wrapper.js` appears in **293 files** on GitHub, the ENEM dataset
API exists as one project and **three history-rewritten copies**, and this KB's own corpus holds
**71** byte-identical README clusters. 🟢 **In a copy-propagated ecosystem, provenance is the
licence question.** Where a dependency manifest would carry a version and a licence, a vendored file
carries a header and a copy carries nothing at all.

🟢 **The operational rule.** Resolve the slug to a **repository** (ref-set identity), then to a
**lineage** (shared commits / root tree), then read the grant **wherever the artefact declares it**
— file, manifest, header or reference — and record **which** of those it was. Instrument with six
verdicts and 10 tests: `compose/code/p136-lineage-verdict/`; the grant-location classes are on
`agents/top.md`.

🔵 **Falsifier.** If a corpus-wide tree-level probe finds that vendored third-party code is rare —
say under 5% of rows carrying a foreign licence header — then slug-level licence verdicts are good
enough and this trend is an artefact of four unlucky examples.

## Watch list for the next pass

**Resolved this pass:**

- ~~Whether a **student-information-system agent** appears — now the largest genuine hole (T9).~~
  🟢 **RESOLVED: 21 exist** (T9, T11). Watch instead for the *first one to exceed 10 stars*, and
  for any connector that authenticates through institutional SSO rather than a pupil password.
- ~~Whether any **Kolibri-based AI project** appears (T8).~~ 🟢 **RESOLVED: `project-nomad`,
  Apache-2.0, 39 444★**, orchestrating Kolibri + Kiwix + Ollama (T8).
- ~~**Africa and the Middle East:** no regional evidence for a second pass.~~ 🟡 **PARTLY
  RESOLVED:** one 63★ Egyptian-targeted row, unlicensed by declaration. Still no African or Gulf
  market sizing, no national instrument, no Sub-Saharan row.

**Carried forward, unchanged this pass:**

- Whether `mathtutorbench` **resolves its own licence** (T7). Re-checked: still no `LICENSE`, badge
  **CC-BY-4.0** vs body **CC-BY-SA-4.0**. Still the single highest-leverage upstream change
  available to this KB.
- ~~Whether `instructure/canvas-lms` resumes activity; `pushed_at` **2026-04-30**…~~ 🔴 **RETIRED
  BY p133 AS A MIS-MEASUREMENT.** `canvas-lms` declares the topic **`gerrit-mirror`**, and
  `instructure/analytics` shares its `pushed_at` **one second later** (14:52:10 / 14:52:11) — two
  repos cannot be hand-pushed a second apart. **This is a stopped mirror export, not four passes of
  developer silence.** 🟡 **Watch the right thing instead: whether the GitHub mirror resumes at all**
  — because while it is frozen, GitHub is not an activity signal for Canvas and anyone diffing the
  mirror to track upstream is reading a five-month-old tree. See `repos/foundations.md`.
- 🔴 **New standing rule from that correction: never read `pushed_at` as activity without checking
  for a mirror.** Flag a recency reading as unreliable when *"mirror"* appears in topics, when two
  repos in one org share `pushed_at` to the second, or when the README names an upstream elsewhere
  (Gerrit, GitLab, SVN). This KB's `git-recency-channel` and `p109-freshness` lanes currently
  mis-rank every mirror in the direction of looking abandoned; `gerrit` appeared **zero** times
  across 1 733 addresses before this pass.
- Whether **Open edX MCP** moves past experimental; `blend-ed/openedx-mcp` still **2 stars**.
- Whether any **proctoring project acquires an institutional owner** — tier still permissive and
  capped at 18★.
- Whether a national regulator applies the **pre-deferral AI Act dates**, or a further omnibus
  reopens Annex III.

**New for the next pass:**

- ~~🔴 **Probe ANZ directly.**~~ 🟢 **DONE p133 (`ACTION BF`) — and ANZ is not a blank.**
  `BetterSEQTA/BetterSEQTA-Plus` (**MIT, 40★**, org-owned, 25 forks, Chrome Web Store, pushed
  2026-10-06) and `BetterSEQTA/DesQTA` (**MIT, 16★**) over **SEQTA**, Australia. New Zealand:
  one MIT **KAMAR** row, archived. 🟡 **Watch next: whether `BetterSEQTA` adds an AI/MCP surface** —
  it is the only product-shaped org in the portal tier and has not yet shipped an agent.
- ~~🔴 **Probe LATAM with platform proper nouns, not category terms.**~~ 🟢 **DONE p133
  (`ACTION BE`) — REFUTED: 12 LATAM rows.** `sigaa` (5), `suap` (3), `siu-guarani` (4). 🔴 **Probes
  that returned nothing are recorded with their probe in `intel/market.md` → LATAM**: SIAGIE (Peru)
  and Q-Acadêmico (Brazil) have real installed bases and **no agent layer at all** — the two
  cleanest unclaimed LATAM slots this KB can name. **Chile's `ucampus` probe collided with a Chinese
  homograph and the qualified re-probe returned 0.** 🟡 **Not reached: `simat` (Colombia), `saes`
  (Mexico)** — carried as `ACTION BJ`.
- 🟡 Read **ILIA 2025 (CEPAL)** directly for LATAM country-level regulation, instead of re-running
  regional news queries that return commentary.
- ~~🟡 Licence-measure the three rows left `UNREAD`…~~ 🟢 **DONE p133, all three read:**
  `edwyj/ddl-killer` = 🔴 **AGPL-3.0** (holder is the FSF only — a `DOCUMENT-TEXT` case),
  `karissafuller/project-nomad-macos` = 🟢 **MIT** (*"Copyright (c) 2026 Karissa Fuller"*),
  `Tushar-cy/Offline-AI` = 🔴 **no payload at `/main/` or `/master/`** → measured-absent.
  🔴 **Instrument note for the next pass: the GitHub contents API is scope-blocked in this session**
  (it returns *"repository is not configured for this session"*, which is an authorisation refusal,
  **not** a 404 and **not** evidence about the repo). **The working lane is
  `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE`.**
- 🔵 Check whether `Tushar-cy/Offline-AI` and `Tushar-cy/Ai-edge-learning-hub` are a rename pair,
  and retire the dead one from this KB before it is ever counted twice.

### 🆕 Added to the watch list by p134

- 🟢 **An MCP server over LTI AGS, OneRoster or Ed-Fi gaining traction.** Today the whole category is
  one 15-star repo and one empty one. This is the highest-signal thing to re-measure next pass.
- 🔴 **`cdweaver1992/edfi-mcp-server` — watch for it to acquire code.** A named, described, empty
  repo in a high-demand slot is the kind of thing that gets filled, and if it is filled by someone
  else it stops being an opportunity.
- 🟡 **`dmitry-viskov/pylti1.3` (MIT, 138★, last push 2024-08-18).** The Python LTI binding is the
  weak link for any agent build. Watch for a fork gaining activity, or for the upstream to wake.
- 🟡 **`DavidLMS/learnmcp-xapi` last push (2025-08-29).** If it stays still, the bridge has to be
  built rather than adopted.
- 🟢 **France's fuller AI-in-education plan**, expected spring 2026 per the June 2025 *cadre
  d'usage*; and whether a **national monitoring body** is created, since its absence is the
  assurance opening.
- 🟢 **Jisc's AI marking and feedback pilots (38 UK institutions).** Findings from a 38-institution
  programme would be the best outcome evidence available in this market.
- 🔴 **Colorado's reported AI Act repeal (May 2026) and the FERPA-covered-institution exemption** —
  unconfirmed by any second source this pass. **Either confirm it against the state legislature or
  strike it; it must not reach a client either way until then.**
- 🟡 **Whether "APAC" and "LATAM" are mis-queried the way "EMEA" was.** `ACTION BK` proved the
  sales-region word reaches enterprise IT rather than ministries. The same test has not been run on
  the other two region words — see `ACTION BM`.

### 🆕 Added to the watch list by p135

- 🔴 **Whether an identity broker appears** — an MCP server, or a component in front of one, that
  verifies an LTI launch or an OIDC assertion itself rather than accepting `caller_identity` on
  trust. **This is the single most consequential thing to watch on this shelf** (`T13`). It would
  turn the sanctioned path from a build into an assembly.
- 🔴 **Whether anything at all appears for Caliper Analytics.** One repository, 0★, unlicensed,
  untouched since 2023. A permissive client above ~50★ would reframe `T12` and partially unblock the
  measurement layer of `T7`.
- ~~🟡 **Whether `pipwerks/scorm-api-wrapper` gains a licence.**~~ 🔴 **ANSWERED BY p136, and the
  question was wrong.** It has declared one all along — `package.json` and the source header, *"MIT-style
  license"* at an off-repository URL. The propagation question is answered too: **one** row on this
  KB's pages (`numbas/Numbas`, by **vendoring**), and **293 files** sector-wide carrying the header.
  🟡 **Watch instead** whether it ever ships an SPDX-identifiable text, since *"MIT-style"* names no
  standard body, and note its **HEAD commit is 2018-09-06**.
- 🟡 **Whether `learnmcp-xapi` is maintained or forked.** Last push **2025-08-29**, and it is still
  the only agent↔xAPI bridge in existence. Its docstrings describe a JWT trust anchor it does not
  implement, so a maintained fork would be a natural place for the identity work above to land.
- 🟡 **Whether `Selleo/mentingo` keeps its pace.** MIT, 92★, pushed 2026-10-10, and the only row
  where the AI *is* the platform rather than a connector onto someone else's. If it sustains, it is
  a fork base; if it stalls, it is a reference architecture.
- ~~🔴 **Japan's national AI-education policy, which this pass measured ABSENT.**~~ 🟢 **RESOLVED BY
  p136 (`ACTION BT`): Ver.2.0 of 2024-12-26, circular 6文科初第1895号, Ver.1.0 in July 2023.**
  🟡 **Watch instead** for the **Ver.2.1** text, whose draft direction names agentic AI, cognitive
  offloading and assessment — the first national instrument this KB has seen address **agentic** AI
  in schools directly, and therefore the most quotable document in the region when it lands.
- 🟡 **Whether Colorado's enforcement stay is lifted** (`X. AI LLC v. Weiser`) and whether the AG's
  rulemaking lands by its **2027-01-01** deadline. The compliance dates are not stayed; the cure
  period ends 2030.
- 🟡 **Whether ELM (European Learner Model) supply grows beyond three repositories**, and whether any
  of it appears in a language other than Rust. It is the EU's cross-border credential model and the
  only permissive implementation is a language mismatch for most AI work.

### 🆕 Added to the watch list by p136

- 🔴 **Whether anyone writes the LTI→broker adapter.** Six identity brokers exist and none
  terminates an LTI 1.3 launch; `topic:lti` + `topic:mcp` is **two** repositories, neither
  implementing LTI. 🟢 **This is now the single most consequential thing on this shelf** (`T13`
  rewritten): the first repository that verifies an LTI launch and issues a broker token bound to
  that subject closes `T13` and turns `P13` into procurement.
- 🟡 **Whether `giantswarm/mcp-oauth` stays alive and gains adopters.** Apache-2.0, **14★**, pushed
  the day of this pass, 56 test files, MCP spec 2025-11-25. 🔴 **Its star count is small enough that
  bus-factor is a real question for a component a client's security team must trust** — compare
  `atrawog/mcp-oauth-gateway` (60★) and `NapthaAI/http-oauth-mcp-server` (108★), and watch whether
  one of the three becomes the obvious default.
- 🔴 **Japan's Ver.2.1 guideline**, expected within FY2026 — agentic AI, cognitive offloading,
  assessment (see `T10`'s third clause and `intel/market.md` → APAC).
- 🔴 **Whether South Korea's reversal spreads.** The National Assembly stripped AI textbooks of
  official status in August after sub-30% adoption. 🟡 Watch whether any other APAC mandate slips on
  **readiness** grounds — the stated reason — because that is the teacher-capacity engagement
  (`compose/patterns.md` → **P5**) arriving as a procurement, not a pilot.
- 🟡 **Whether Ohio enforces.** Its district AI-policy deadline of **2026-07-01** has elapsed. Watch
  for the first compliance review, audit finding or state report naming districts without a policy —
  the moment the North American conversation moves from drafting to evidence.
- 🟡 **Whether a tree-level licence probe changes `T15`.** The falsifier is explicit: if vendored
  third-party code turns out to be rare across this corpus, slug-level licence verdicts are good
  enough and `T15` is four unlucky examples rather than a trend.
- 🟡 **Whether `GarethManning/education-agent-skills`' ShareAlike obligation becomes visible in
  practice.** 847★, 122 forks, CC-BY-SA-4.0 by deed. Watch whether any fork publishes adaptations
  under the same licence — the first test of whether a content licence on an agent-skills pack is
  honoured or ignored.
