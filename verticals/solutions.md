---
industry: education
region: Global
updated: 2026-11-12
---

## 🆕 `p796` — **the brand layer is a separate licence question, and on three platforms in this file the answer is more restrictive than the code. `metabase`'s carve-out is now SIZED; `DSpace`'s third-party anthology is opened and turns out to be a deliverable.**

### 🔴 `T914` — the licence that lets you ship the platform is not the licence that lets you put the client's name on it

🔴 **Every engagement in this file ends in a white-labelled deployment. `p796` counted root licence FILES across `174` addresses and found that on three platforms recommended here, the brand assets are carved out of the permissive grant:**

| Platform | Code licence | 🔴 Brand / embed layer | 🟢 What to do about it |
|---|---|---|---|
| 🔴 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10,982 B` | 🔴 **`NOTICE.TXT` (`14,412 B`): *"The OpenOlat logo and icons … are released under the Creative Commons Attribution-NoDerivs 2.5 license."*** | 🟢 **REPLACE the logo and icon set outright.** 🔵 `NoDerivs` forbids modifying them; it does not forbid shipping your own. 🟢 The code stays Apache-2.0 and the row stays the permissive EMEA choice |
| 🔴 [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🔴 **BSD-3-Clause + a fourth clause** · `2,819 B` | 🔴 **Clause `4`: altering, removing or replacing *"Open WebUI" branding* is a material breach** (`T900`) | 🔴 **Cannot be delivered white-labelled at all.** 🟢 Use it as an internal tool or negotiate a licence; do not plan a rebranded delivery on it |
| 🔴 [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 **AGPL-3.0** · `37,265 B` | 🔴 **`4` root licence files, `1` OSI grant.** `LICENSE-EMBEDDING.txt` is **`8,877 B` of terms containing NO recognised grant**, plus `LICENSE-MCL.txt` (`425 B`) and `LICENSE.txt` (`855 B`) | 🔴 **Embedding analytics into a client portal is the exact act the `8,877 B` governs.** 🟢 Read it, or choose a dashboard without a per-file carve-out |

🔵 **The general rule, and it is cheap to apply: list the root tree, not just the root `LICENSE`.** 🟢 **A vendor's carve-out is always on the piece they most want to control — the embed, the client, the brand.** 🔴 **Three for three, on rows this file already recommended.**

### 🟢 `DSpace` — the third-party anthology is a procurement asset (`T920`)

🟢 **[`DSpace/DSpace`](https://github.com/DSpace/DSpace) ships `LICENSES_THIRD_PARTY` (`91,354 B`): `721` dependency entries grouped by licence, with the project's policy stated in its own preamble — *"DSpace actually does NOT allow for any dependencies that are solely released under GPL terms."*** 🟢 **Verified: the single `GPL-3.0` entry (`juniversalchardet:2.5.0`) is dual-listed under `LGPL`.** 🟡 **~`13` `LGPL`-named entries** (`openpdf`, `jna` `LGPL-2.1-or-later`, `JHighlight`, `8` × `java-json-tools`) — 🟢 low risk for a server-side repository, and the first thing legal asks for. 🟢 **Hand this file over rather than generating one.**

### 🔴 `odoo`'s licence file carries the GPL verbatim as well as the LGPL

🔴 **[`odoo/odoo`](https://github.com/odoo/odoo)'s single `43,529 B` `LICENSE` holds TWO grants: `LGPL-3.0` at line `15` and the FULL `GPL-3.0` text at line `183`.** 🔵 **This base spent four passes (`p222`–`p225`) resolving `openeducat`'s LGPL bound against Odoo's manifest grammar. `p796` adds the structural fact underneath it: the file those readings rest on is not one licence.** 🟢 **For a deployment that only *uses* Odoo the practical answer is unchanged; for one that redistributes a modified Odoo, both texts are in scope.**

### 🟢 Platform licence-file counts — the census row every platform here now has

| Platform | Root licence files | Grants | Note |
|---|---|---|---|
| `metabase/metabase` | 🔴 **`4`** | `1` OSI | 🔴 `8,877 B` embedding carve-out with no grant |
| `DSpace/DSpace` | `4` | `1` | 🟢 `91,354 B` third-party disclosure — an asset |
| `open-webui/open-webui` | 🔴 **`3`** | 🔴 `3` | 🔴 branding rider + MIT/BSD relicensing record |
| `OpenOLAT/OpenOLAT` | `2` | `1` | 🔴 `CC BY-ND 2.5` brand assets in `NOTICE.TXT` |
| `oppia/oppia` | `2` | `1` | 🟢 Apache-2.0 + a `146 B` NOTICE — clean |
| `chamilo/chamilo-lms` | `2` | `1` | 🟢 one `GPL-3.0` grant; the second file is a `1,614 B` notice |
| `sakaiproject/sakai` | `2` | `1` | 🟢 `ECL-2.0` |
| `moodle/moodle` · `odoo/odoo` · `instructure/canvas-lms` · `openedx/edx-platform` | `1` | `1` · 🔴 **`2`** · `1` · `1` | 🟢 `odoo` is the outlier — see above |

🔵 **`19` rows in this base serve no root licence file at all and `12` serve one this pass could not grade.** 🟢 Both numbers are published; neither is folded into the other.


## 🆕 `p795` — **The BI layer this file recommends forbids the embed it was recommended for, and the strongest new platform row is a Moodle plugin — AI on top of the incumbent, not a replacement for it.**

### 🔴 `T912` — `metabase` cannot be embedded white-labelled, and this file's analytics advice assumed it could

🔴 **`metabase/metabase` carries `4` root licence files, and the one no pass had opened governs a single FILE.** `LICENSE-EMBEDDING.txt` (`8,877 B`) applies to `app-embed.js`, lifts it out of AGPL-3.0 (*"free and clear of any Affero GPL License requirements"*), and then:

| Clause | 🔴 What it forbids |
|---|---|
| `§2` | Modifying `app-embed.js`, or *"blocking, overlaying, or otherwise obstructing the contents of the embedded element"* |
| 🔴 **`§3`** | 🔴 ***"the removal of the Metabase's name or logo in the iframe that is embedded in your application"*** |
| `§2(b)` | Transferring, sublicensing, leasing or distributing the Software to any third party |

🟢 **Corrected rule for this file.** 🔴 **Do NOT embed `app-embed.js` into a client-branded learning-analytics surface** — the Metabase mark must remain visible, so the surface cannot carry only the institution's identity. 🟢 **Do run metabase as its own AGPL-3.0 application behind SSO and link to it from the client surface**; that uses the AGPL grant, needs no embedding licence, and keeps the institution's deployment intact. 🔵 **Identical in shape to `T900` (Open WebUI's branding rider), which this file corrected last pass — two of this file's recommended surfaces now turn out to be un-white-labellable, and that is a pattern worth stating to delivery leads before the design review, not after.**

### 🟢 `T909` — platform rows now carry a CONSEQUENCE beside `UNGRADED`

🔴 **`UNGRADED` is a verdict about which licence FAMILY applies; this file was reading it as a verdict about whether a platform can ship.** 🟢 **For `CaviraOSS/PageLM` the two answers are opposite:** the family is genuinely unclassifiable **and** the licence is non-commercial with a section headed *"Prohibition on Redistribution"* — 🔴 **so it cannot be in a client deliverable in any form**, which `UNGRADED` alone never said. 🟢 Carried as a consequence field, not a re-grade.

### 🟢 The platform row added this pass — and it is the "AI on top of the incumbent" path

| Platform | Repo | Grant, on the bytes | Deps | Region | Note |
|---|---|---|---|---|---|
| **Moodle AI Skill Navigator** | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | 🟡 **GPL-3.0** · `35,153 B` · `a0ca524c0129` | 🔵 unmeasured (`p795-C`) | Global | 🟢 **AI tutoring, quizzes, mind maps and RAG over course materials, delivered as a Moodle plugin** (★`281`, pushed `2026-11-07`). 🟢 **GPL-3.0 is correct and unavoidable** — a Moodle plugin inherits Moodle's licence. 🔵 **This is the shape most institutional clients actually want: the LMS of record stays, the AI arrives as a plugin inside it** |
| **AI Shifu** | [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) | 🟢 **Apache-2.0** · `11,342 B` · `0150fcb2599f` | 🔵 unmeasured (`p795-C`) | APAC 🇨🇳 | 🟢 Permissive conversational teaching platform, pushed `2026-11-12`. 🟢 The deployable alternative when a client will not accept AGPL |
| **DeepTutor-AILearning** | [`3yangyang9/DeepTutor-AILearning`](https://github.com/3yangyang9/DeepTutor-AILearning) | 🟢 **Apache-2.0** · `11,408 B` · `ae1dbfc5e74c` | 🔵 unmeasured (`p795-C`) | APAC 🇨🇳 | 🟢 **Multi-tenant by construction**: platform → institution → campus → teacher/student. 🔵 **The only row in this file with a tenancy model already built**, which is what a training-provider client buys rather than builds |

🔵 **The strategic point, and it cuts against this file's historical bias.** 🟢 This file has catalogued **replacement** platforms — Moodle, Canvas, Open edX, Sakai, Chamilo, ILIAS — and graded their licences. 🔴 **An institution with a working LMS of record is not buying a replacement.** 🟢 **The `moodle-ai-skill-navigator` row is the first catalogued artefact of the other engagement shape: leave the system of record alone and deliver AI as a plugin inside it.** 🟡 **The licence consequence is the trade: that path is GPL-3.0 by inheritance, permanently, and no permissive option exists inside Moodle's plugin boundary.**

### 🔴 The maintenance field this file never had (`ACTION p794-A`)

🟢 **Archived platform rows: still exactly `3`, confirmed across `167` addresses.** 🔴 **But `Kosudo/nextSIS` — an SIS in this file's Student Information section — has not been pushed since `2018-07-16`, `88` months.** 🔴 **For a system that holds student records that is not staleness, it is an unowned CVE surface**, and the correct advice is a deliberate fork with a named maintainer, or a different SIS. 🟡 `jkbrzt/rrule` (`28` mo) corrected in place above with its consequence graded as near-harmless.

### 🟢 `ACTION p794-C` — one `Deps` cell closed, the rest named

🟢 **`oppia/oppia` CONFIRMED on the second instrument** (PyPI version-scoped JSON: `mutagen==1.47.0` → `GPL-2.0-or-later`); the hosted-deployment rule in this file is unchanged. 🔴 **Every other `Deps` cell in this file remains a claim about a version nobody has identified.** 🟢 **`DSpace/DSpace` is next and the target is already located: a `91,354 B` `LICENSES_THIRD_PARTY` anthology in its root tree.**

## 🆕 `p794` — **The delivery surface this file recommends cannot carry a client's name, and the ePortfolio it recommends is archived.**

🟢 **All platform rows re-measured on the byte channel plus GitHub's own classifier: `118/118` licence agreement, `0` clone failures, `1` correction — and the correction is on the row a client sees first.**

### 🔴 `T900` — Open WebUI cannot be white-labelled, and this file told clients to use it as the front end

🔴 This file published [`open-webui/open-webui`](https://github.com/open-webui/open-webui) (`★158,480`) as 🟢 `BSD-3-Clause`, *"the fastest data-resident front end"*. 🔴 **Canonical BSD-3-Clause has three numbered clauses; the served `LICENSE` (`2,819 B`) has four.** Clause `4` bars *"altering, removing, obscuring, or replacing any 'Open WebUI' branding"* and makes alteration a **material breach**.

🔵 **For this file specifically, that is the difference between a usable row and a trap**, because a delivery surface is the one component a client expects to carry its own name. 🟢 **Two ways to keep it:** ship it **with Open WebUI branding intact** where that is acceptable, or 🟢 **put the tutor in the LMS the client already owns** — which is what `P794-1` does and why that pattern needs no chat surface at all.

🔴 **And the trap is laid three files deep:** `LICENSE` (`2,819 B`, ridered) · **`LICENSE_HISTORY` (`2,872 B`, grades as clean BSD-3-Clause)** · `LICENSE_NOTICE` (`721 B`, a title line only). 🟢 GitHub's classifier says `NOASSERTION` — **more honest than this file's grade.**

### 🔴 `T901` — platform rows have no maintenance field, and three are archived

🔴 **Mahara** — the ePortfolio recommendation — is 🔴 **ARCHIVED, last push `2023-11-16`**. 🔴 **MyScriptJS** — the maths-input primitive — is 🔴 **ARCHIVED, last push `2021-01-04`**. 🟡 **European Learning Model** — the EMEA credential vocabulary — is 🟡 **ARCHIVED, last push `2024-02-14`**. 🔴 **All three return `rc=0` with refs and a valid `HEAD`, so every existence instrument this base has ever run called them healthy.** 🟢 All three are now labelled in place with their last-push dates.

🔵 **What this changes in a proposal:** an archived platform is not disqualified — it is a **fork you own from day one**, with the maintenance cost priced in. 🔴 **Saying so is the deliverable; discovering it in month three is the failure.**

### 🟢 `ECL-2.0` — why Sakai and Opencast stay recommended, with one sentence added for counsel

🟢 **Both remain the permissive answer in a copyleft sector**, and both are `ECL-2.0` — verified on the bytes (`11,120 B` and `11,340 B`) and confirmed by GitHub's classifier. 🔵 **The sentence to add:** ECL-2.0's §3 narrows Apache-2.0's patent grant so that, for institution-employed contributors, it reaches only claims where the author is also the inventor **and** the institution may grant under its research-funding agreements. 🟡 **Copyright permissions are identical to Apache-2.0; patent coverage is thinner, and these are university-contributed codebases.** 🟢 Ship them — and do not describe them as Apache-equivalent in a procurement response.

### 🔴 Corrected in this file

| Row | Was | 🟢 Now |
|---|---|---|
| **Open WebUI** | 🟢 `BSD-3-Clause` | 🔴 **`BSD-3-Clause + branding rider`, non-OSI — not white-labellable** |
| **nextSIS** | 🔴 `PROPRIETARY`, *"named here only so it is not mistaken for an option"* | 🟢 **`GPL-3.0` — it IS an option**; deploy separately, integrate at the boundary (stale since `p790`) |
| **Mahara** · **MyScriptJS** · **European Learning Model** | no maintenance field | 🔴 **ARCHIVED**, with last-push dates |

### 🟢 Platform licence reality, re-measured — the rule this file exists to state is unchanged

🔴 **The platform layer is still copyleft and the agent layer is still permissive.** Measured this pass: `moodle/moodle` GPL-3.0 (`★7,607`) · `openedx/edx-platform` AGPL-3.0 · `chamilo/chamilo-lms` GPL-3.0 (`35,147 B`, affero×`3` — 🟢 the `T894` discriminator reproduced) · `frappe/erpnext` GPL-3.0 (`★41,231`) · `odoo/odoo` **LGPL-3.0** · `openeducat/openeducat_erp` **LGPL-3.0** · `ankitects/anki` **AGPL-3.0** · `metabase/metabase` **AGPL-3.0** (`★50,301`) · `bigbluebutton/bigbluebutton` LGPL-3.0 (`★9,274`) · 🟢 **permissive: `sakaiproject/sakai` and `opencast/opencast` ECL-2.0, `getodk/collect` Apache-2.0, `Gego-K12/gegok12` MIT, `learningequality/kolibri` MIT, `jupyter/notebook` BSD-3-Clause.** 🟢 **`Gego-K12/gegok12` remains the only permissive school ERP/SIS in this file and the only place an agent can live *inside* the system of record.**

## 🆕 `p793` — **The MCP edge was read, not assumed: the canonical Canvas server has real data-governance engineering and its hardened settings are self-declared placeholders.**

`p792` added MCP as "the Odoo pattern's edge — permissive even when the platform is not". 🔴 **`ACTION p792-D` required that claim be measured before any security offer was written, starting with the auth model.** Measured.

### 🟢 [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — MIT, `1,071 B`, `3c7307584ae4`, `529`-file tree

🟢 **This is not an unconsidered server, and the base's working assumption that community MCP servers hold institutional tokens with no governance thought does NOT survive contact with the canonical one:**

| Control it actually ships | Evidence in the tree |
|---|---|
| 🟢 Structured audit trail | `src/canvas_mcp/core/audit.py` — `6,420 B`, `215` lines: `log_data_access` · `log_code_execution` · `log_access_change` |
| 🟢 **Identifier masking in the log** | `_sanitize_endpoint`: `/courses/12345/users/678` → `/courses/***/users/***` |
| 🟢 Executed code recorded as a **hash**, never raw | `log_code_execution(code_hash=…)` — SHA-256 prefix |
| 🟢 **Three deployment tiers** | `config/overlays/baseline.env` · `public.env` · `enterprise.env` |
| 🟢 Sandbox, outbound network blocked by default in all three | `TS_SANDBOX_BLOCK_OUTBOUND_NETWORK=true`; enterprise adds `TS_SANDBOX_ALLOWLIST_HOSTS` |
| 🟢 Token rotation · security CI · its own prior reviews | `scripts/rotate-canvas-token.mjs` · `.github/workflows/security-testing.yml` · `docs/audits/2026-09-23-codex-review.md` · `security/student-feature-review-2026-10-08.md` |
| 🟢 Entra / Azure auth path | `deploy/azure/authsettingsv2.example.json` |

### 🔴 And the two things an institution must not misread

**1. The hardened flags are labelled unfinished by the project itself.** `enterprise.env` declares `MCP_CLIENT_AUTH_MODE=api_key_or_mtls`, `MCP_CLIENT_API_KEY_REQUIRED=true` and `MCP_CLIENT_CERT_AUTHORITY` under the comment **"(pending feature wiring)"**. `public.env` declares `TOKEN_STORAGE_BACKEND=keyring` under the same comment and `LOG_REDACT_PII=true` under **"Logging hygiene (some flags are placeholders)"**. 🔴 **A procurement reviewer who treats `enterprise.env` as a control inventory will believe mTLS client authentication and PII redaction are in force.** The project is honest in its comments; the hazard is entirely in how the file gets read.

**2. The token layer protects the server, not the Canvas account.** `src/canvas_mcp/core/access/tokens.py` is `50` lines of HMAC-signed claims (`oid`, `jti`, `exp`) — authentication **of clients to this MCP server**. The Canvas credential underneath is untouched, and `SECURITY.md` says so without hedging: 🔴 **"Your Canvas API token has full access to your Canvas account."** No per-tool scoping exists, because Canvas offers none; the documented mitigation is `chmod 600 .env`.

🔴 **And the tool surface includes `bulk_grade_submissions`** — writing grades, i.e. EU AI Act **Annex III point 3** (*evaluation of learning outcomes*), reached by a tool call holding an account-scoped credential, from **`2027-12-02`**.

### 🟢 The rule this file carries forward, amended

🟢 **The LTI/MCP edge is still the right architecture** — a permissive process on one side of a boundary, a copyleft platform on the other (`csev/tsugi`, Apache-2.0, remains the most useful licensing component in the sector). 🔵 **What `p793` adds: the edge component's governance must be read from its code and its comments, not from its settings file.** A config key is a claim; a wired control is a control. Recipe: [`compose/patterns.md`](../compose/patterns.md) → `P793-1`. Mechanism: [`intel/trends.md`](../intel/trends.md) → `T897`.

## 🆕 `p792` — **The Odoo pattern gets its missing piece: a permissive, tool-scoped way INTO a copyleft platform. Plus the one row this file told clients to avoid is cleared.**

🔵 **This file's governing pattern, carried:** take a mature, deployed platform that already holds the institution's data and add agents **at its edge** — nobody replaces a Student Information System in an engagement. 🔴 **The problem has always been that the edge was an LTI tool or a REST client, which is a lot of integration work per deliverable.** 🟢 **`p792` records a better edge.**

### 🟢 MCP is the Odoo pattern's edge, and it is permissive even when the platform is not

| Platform | The permissive way in | Grant, on the bytes | ★ | Verdict for an AI layer |
|---|---|---|---|---|
| 🟢 **Canvas LMS** (AGPL core) | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · `1,071 B` · `3c7307584ae4` | **`323`** | 🟢 **The most useful row added to this file in four passes.** Canvas is what a North American higher-ed client is running, and its core is **AGPL** — which is exactly why every AI deliverable has had to sit outside it. 🟢 **An MIT MCP server is a clean boundary**: courses, assignments, submissions, grading and announcements become agent tools, the agent code stays MIT/proprietary as the client prefers, and **Canvas's AGPL is never linked, only called**. `529` files, **one** licence path. Pushed `2026-11-12` |
| 🟢 **Gradescope** (proprietary SaaS) | [`Yuanpeng-Li/gradescope-mcp`](https://github.com/Yuanpeng-Li/gradescope-mcp) | 🟢 **MIT** · `1,068 B` · `0e01db542a01` | `8` | 🟡 Rubrics and submissions as tools. 🔴 `★8` — read it for the auth and rubric shape; do not depend on it |
| 🟡 **Open edX** (AGPL) | reported MCP integration | 🔵 **not byte-verified this pass** | — | 🔵 Named because a secondary source reports it and this base will want it. **Unverified — do not cite to a client until read** |

🔴 **Canonicity matters here more than anywhere else in this base (`T887`).** The first Canvas MCP a query returns is [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) — MIT, `1,070 B`, `501` files, **`★10`**: granted, real, and a derivative. Canonical is `★323`. 🔴 `DMontgomery40/mcp-canvas-lms` at `★104` is **ungranted**. 🟢 **Sweep the name; the top hit is ranked by query match.**

🔴 **The governance caveat is the commercial opportunity, and it must be said in the same breath.** 🔴 **No LMS vendor ships an official MCP server** — Instructure documents the REST/GraphQL APIs and LTI 1.3 / LTI Advantage. Hosted commercial alternatives exist (Atomic Jolt's Atomic MCP for Canvas; ibl.ai connectors). 🔴 **And no independent security or data-governance evaluation of any education MCP server has been published.** An MCP server holding an institutional Canvas token can reach **student records**, which in North America means **FERPA** and in EMEA **GDPR** plus the EU AI Act's high-risk regime from **`2027-12-02`**. 🟢 **Token scoping, audit logging and a data-protection review around an education MCP deployment is work nobody is currently doing, on a component everybody is about to deploy.**

### ✏️ `oppia/oppia` — this file's dependency warning is withdrawn

🔴 **What this file said:** `oppia/oppia` is Apache-2.0 and **depends on an AGPL-3.0 library**, cited as the lead example of why *"a permissive host is a necessary condition for direct embedding, not a sufficient one."*

🟢 **Measured on the lockfile (`T884`): `oppia` resolves `angular-shepherd` to `11.0.0`, which is MIT.** The AGPL-3.0 relicence happened at **`v22.0.0`**, and `^11.0.0` cannot reach it. `shepherd.js` resolves to `8.3.1`, also MIT.

🟢 **The RULE this file states is still correct and still worth its place** — a host's dependencies must be read. 🔴 **The EXAMPLE was wrong, and `kolibri`'s two LGPL packages now have to carry the argument instead.** 🟡 **`oppia` moves from "do not embed" to "embeddable, with Shepherd pinned and its major bump gated"** — and it gains a separate, smaller note: `mutagen==1.47.0` (**GPL-2.0-or-later**) is a direct Python dependency, which matters only if the service is **distributed** rather than hosted.

### 🟢 Carried, unchanged

🟢 **`Gego-K12/gegok12`** (MIT, `1,150 B`, `★56`) remains the only permissive school ERP/SIS in this file and the only place an agent can live **inside** the system of record. 🔴 **`frappe/education`** remains **intent-to-GPL-3.0** on a `19`-byte licence file — boundary only, no embedding, confirm upstream before a derivative ships. 🔵 Both verdicts were re-read this pass and neither changed.


## 🆕 `p791` — a vendor licence claim that HOLDS, and a `19`-byte grant on a platform this file recommends

🔵 **`p790`'s block on education ERP ended with three vendor licence claims failing on the bytes.** `p791` ran the same test on two more and got one of each — which is the useful outcome, because it shows the probe is not simply biased against vendors.

| Platform | Address | Grant, on the bytes | ★ | Deps | Verdict for an AI layer |
|---|---|---|---|---|---|
| **GegoK12** 🆕 | [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** · `1,150 B` · `f86101816893` | `56` | 🟢 `laravel-fcm` **MIT** (`1/1` audited) | 🟢 **The vendor claim HOLDS, and it is the only permissive school ERP in this file.** Laravel K-12 ERP/SIS — students, attendance, timetables, fees, multi-role portals. 🟢 **Direct embedding is clean (`T861` satisfied to the first layer)**, so an agent can be an in-process module rather than an LTI tool or an API client. 🔴 **But `★56`**: pick it for greenfield K-12 or as a schema reference, not to replace a running SIS. 🔵 Vendor pages also market a cloud/paid tier — the open-core split is real, so read what the free tier contains |
| **Frappe Education** ✏️ | [`frappe/education`](https://github.com/frappe/education) | 🔴 **`19 B` reference, NO grant text** · `beca17940a71` | `706` | — | ✏️ **Corrected, and this file recommended it.** The ERPNext-based education module is a genuine fit for the Odoo pattern — mature ERP underneath, education modules on top. 🔴 **Its licence file says `License: GNU GPL V3` in `19` bytes and stops**, while `frappe/lms` (`33,893 B`) and `frappe/erpnext` (`35,149 B`) carry full texts. 🟡 **Build at the boundary and treat it as intent-to-GPL-3.0** until upstream confirms; the ERPNext layer beneath it is properly granted, so a Frappe-stack engagement is not blocked — only this module's own derivative status is unsettled |

🟢 **The Odoo-pattern conclusion is unchanged and slightly strengthened.** Nobody replaces a Student Information System in an engagement, so the AI layer sits at the platform's edge. `p791` adds the one exception worth knowing: **when the platform is `gegok12`, the edge and the inside are the same place**, because the grant permits it.


# Vertical platforms — real systems an AI layer can sit on top of — `p790`

The pattern that works in education is the Odoo pattern: **take a mature, deployed, customisable
platform that already holds the institution's data, and add agents at its edge.** Nobody replaces a
Student Information System in an engagement. The grants below decide *where* the AI code can live.

🔴 **New rule this pass, and it changes the last section of this file.** A permissive host is a
necessary condition for direct embedding, **not a sufficient one**: the host's **dependencies** must
be read too. `oppia/oppia` is Apache-2.0 and depends on an **AGPL-3.0** library; `learningequality/kolibri`
is MIT and depends on two LGPL ones (`T861`). **`Deps` below records the first-layer audit where one
was run; a blank cell means not audited, not clean.**


## 🆕 `p790` — Education ERP / SIS, probed on the bytes, and **three vendor licence claims fail**

🔵 **Why this block exists.** The brief for this base asks for *real systems an AI layer can sit on
top of* — Odoo for ERP, OpenMRS for health, Moodle for learning. The education-ERP market answers
that question mostly through **vendor comparison tables**, and vendor tables are a claim channel.
Each row below was read on the byte channel instead.

| Platform | Address | Grant, on the bytes | ★ | Verdict for an AI layer |
|---|---|---|---|---|
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL** · `8,241 B` · `46a5d7d40082` | `911` | 🟡 **The vendor claim HOLDS — the only one here that does.** Education ERP built on Odoo's ORM, with `openeducat_core` as the SIS. 🟢 **LGPL tolerates dynamic linking**, so an AI layer calling it as a service or an Odoo module is clean; keep the LGPL components replaceable and their source available |
| **Odoo** (the ERP underneath) | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **`ANTHOLOGY[LGPL, GPL-3.0]`** · `43,529 B` · `3ce3a7dc8ecb` | `55,739` | 🔴 **`T875` lands on the most-cited vertical platform in the sector on its first application.** Odoo's single `LICENSE` carries **two** copyleft families; reporting it as "LGPL" — as the education-ERP tables do — states one of the two. 🟡 Build **modules**, not a fork, and read which family governs the part you touch |
| **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0 — BY REFERENCE, in `19` bytes** · `1fcecf395312` · `61408d3da518` | `705` | 🔴 **The shortest grant this base has ever measured, and it is a real one.** The entire file reads `License: GNU GPL V3` — no operative text. 🟢 `T845` at its extreme: **`19` bytes is a grant and `39,890` was not proprietary.** 🔴 Copyleft; and note it is **GPL-3.0**, *not* the AGPL-3.0 this base records for its sibling `frappe/lms` — the two Frappe education products differ in family |
| **openSIS Classic** | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 **NO GRANT SERVED** · `8348cd069aa2` | `351` | 🔴 **Re-confirmed, and it reproduced an unplanned 11th control** — this base already records this address at this exact sha as grant-less. 🔵 The vendor tables list it `GPL-2.0`; the repository serves nothing |
| **Fedena** | [`foradian/fedena`](https://github.com/foradian/fedena) | 🔴 **NO GRANT SERVED** · `333477b06f1d` | — | 🔴 **CLAIM REFUTED.** OpenEduCat's own comparison table lists Fedena as **Apache-2.0**. The repository serves **no licence on `10` paths**. 🔵 A competitor's table is not a licence |
| **GegoK12** | `gegok12/gegok12` | 🔴 **ADDRESS DOES NOT EXIST** (`git ls-remote` `rc=128`) | — | 🔴 **CLAIM REFUTED, and this is the sharpest one.** The vendor site states an **MIT** licence and that *"modification, rebranding, and resale are permitted"* — the most permissive claim in the entire education-ERP market. 🔴 **A GitHub-wide search for `gegok12` returns `13` results and none is this product.** There is no locatable source. 🟢 **An MIT claim with no repository is not a finding** |

🟢 **The sentence to carry into an engagement.** In education ERP/SIS the permissive layer is not
narrow — **it is empty**. `0` of `6` platforms probed carry MIT, Apache-2.0 or BSD: four are
copyleft (`LGPL`, `LGPL+GPL-3.0`, `GPL-3.0`, and `nextSIS`'s corrected `GPL-3.0`), and the two that
were *claimed* permissive are a refuted table entry and a non-existent address. 🔴 **So the AI layer
in this sector is always an integration, never an embed** — which is the same conclusion
`repos/foundations.md` reaches for LMSs, now measured on the administrative side too.

🔵 **And the pattern that follows from it:** the attachment points this base already holds —
`brightspace-d2l-mcp` (MIT), `classcharts-agent` (MIT, read-only), `teams-facultad-mcp` (MIT),
`LearningLocker/xapi-service` (MIT) — are **more valuable than they look**, because every system
they attach to is copyleft. 🟢 **An MIT MCP server in front of a GPL platform is the whole
architecture**, not a convenience.

## Learning Management — the delivery layer

| Platform | Address | Grant, on the bytes | Deps | Region | Where an AI layer attaches |
|---|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 · `35,147 B` · `afbcc55fa1bd` | — | Global | The sector default — if a client has an LMS, assume this. 🔴 A plugin is a derivative work and must be GPL-3.0. 🟢 **Attach through LTI via Tsugi, or Moodle's web services API, and your code stays yours** |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · `35,136 B` · `d3a86602dcf7` | — | Global | MOOC-scale delivery; deploy with `overhangio/tutor`. 🔴 AGPL network clause — attach as an **XBlock across a service boundary**, never by linking |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 · `34,520 B` · `1c9f0bb8013e` | — | North America | Dominant in US higher ed. 🟢 Strong LTI 1.3 support — the sanctioned attachment point |
| **D2L Brightspace** | proprietary SaaS — [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 **New this pass.** The third major North American LMS, and until now the only one with no attachment point in this base. The platform is proprietary; **the MCP server over it is MIT**, which is the whole point — attach, never replace |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | — | North America | 🟢 **Permissive and mature.** When a client wants a customised LMS they can own outright, this is the one that does not force disclosure |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10,982 B` · `322e90dd5507` | — | EMEA | 🟢 The permissive choice for a European university, already trusted in Swiss and German HE. 🔴 **`p796` (`T914`): `NOTICE.TXT` (`14,412 B`) licenses the logo and icons `CC BY-ND 2.5` — `NoDerivs`. Replace the brand assets; do not modify them** |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 · `35,147 B` · `e137bded10b5` | — | EMEA | 🟢 **The strongest Spanish-language LMS footprint; widely deployed across LATAM ministries and universities** — the incumbent to integrate with, not displace |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 · `35,147 B` · `87a79b237fcc` | — | EMEA | German public-sector and university installs; SCORM-heavy |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 AGPL-3.0 · `33,893 B` · `45edbff87486` | — | APAC | Modern Indian-origin LMS; pairs with ERPNext and `frappe/education` for a full institution stack |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1,097 B` · `fe298f54494c` | 🟡 **2 LGPL of 32** | Global | 🟢 **Still the platform for low-connectivity deployments** — offline-first, syncs when a link appears, runs on legacy hardware. First choice for rural LATAM, African and remote-APAC programmes. ⚠️ **Two LGPL dependencies**: dynamic linking is permitted so this remains usable, but the components must stay replaceable with source available |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 · `11,358 B` · `bbda308fd5db` | 🔴 **1 AGPL-3.0 of 171** | Global | Interactive lessons that behave like one-to-one tutoring, `7.0k★`. 🔴 **DO NOT ship as-is: `angular-shepherd` is AGPL-3.0 and a browser bundle is network delivery.** Replace or remove it, then embed freely |

## Student Information / School Management — where the institution's data actually lives

| Platform | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL · `8,241 B` · `46a5d7d40082` | Global | 🟢 **The closest thing to "Odoo for education"** — SIS + LMS + finance in one, on Odoo. LGPL permits dynamic linking, so a separate AI module is clean |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 LGPL-3.0 · `43,529 B` · `3ce3a7dc8ecb` | Global | The ERP base underneath. ⚠️ `T847`: the grant sits on line 3 behind a deferral |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 · `15,214 B` · `e4cd20a48bf1` | Global | 🟢 Mature SIS with strong **Spanish and French** localisation — the SIS that fits a LATAM or Francophone-African engagement |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 GPL-3.0 · `35,121 B` · `59334a28613f` | Global | School management and teaching in one system; common in international K-12 |
| **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0** · **`19 B`** · `61408d3da518` | APAC | Frappe's school-management module: admissions, programmes, fees, assessment. 🔵 **The shortest grant in this base and a real one** — the whole `license.txt` reads `License: GNU GPL V3` |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 GPL-3.0 · `34,916 B` · `447313109fdd` | APAC | Finance, HR and procurement for school groups |
| ✏️ **nextSIS** | [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | 🟢 **GPL-3.0** · `39,890 B` · 🟢 `01fa8c8c4c6e` | Global | ✏️ **`p794` removes the stale `PROPRIETARY` row that survived `p790`'s correction.** 🟢 **It IS usable** — copyleft, so deploy separately and integrate at the boundary. Previously filed in this base as merely "ungranted" |

## Assessment, content and classroom

| Platform | Address | Grant, on the bytes | Deps | Region | Note |
|---|---|---|---|---|---|
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | 🟢 **0 of 18** | Global | 🟢 **The permissive autograding core, and the cleanest audit in this file.** Release → collect → autograde → feedback, with a human-review step already in the model — exactly what EU Annex III, Korea's AI Basic Act and US state grading rules require |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause · `1,475 B` · `41fffb935326` | — | Global | Cohort-scale serving under nbgrader |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · `1,105 B` · `fae8cc474484` | 🟢 **0 of 43** | North America | UC Berkeley Bayesian Knowledge Tracing — the mastery model. 🟢 Clean to the first layer |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | 🟢 **MIT** · `1,052 B` · `e722e959afd0` | — | North America | Khan Academy's exercise/question renderer — the content primitive for interactive items |
| **xAPI service** | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **New to this file, and it closes a real hole: a Learning Record Store under MIT.** Every "audit trail" claim in this base previously had to hand-roll its storage. Pair with [`xapi-validation`](https://github.com/LearningLocker/xapi-validation) (MIT, `1,070 B`) |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 · `35,146 B` · `2d7f937a03c9` | — | EMEA | Interactive content types already embedded in Moodle and Canvas — generate *H5P content*, which is data, not derivative code |
| **edx-ora2** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 · `35,135 B` · `0d60a779e29d` | — | Global | Open-response, peer and staff assessment — the rubric model to mirror |
| 🔴 **INGInious** | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · `34,764 B` · `98d56ade0351` | — | EMEA | Automated grading from UCLouvain — a real, mature European platform in the **regulated** surface. 🔴 AGPL **and** ⚠️ **SCOPE-LIMITED**: its licence covers *"most of the files"* and defers the rest to per-file notices. **Study it; do not vendor it** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** · `11,340 B` · `94aecba33ed9` | — | EMEA | 🟢 Permissive lecture capture — transcription, chaptering and summarisation attach naturally |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL · `7,652 B` · `13b55d45c046` | — | Global | Virtual classroom designed for teaching; LGPL allows dynamic linking |
| **MyScriptJS** 🔴 **ARCHIVED** | [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | 🟢 **Apache-2.0 (by reference)** · `570 B` · `968021fcc1f4` | — | EMEA | 🔴 **ARCHIVED UPSTREAM, last push `2021-01-04` (`T901`)** — `★357`. Handwriting and **maths** input recognition, French origin, the input primitive for a maths tutor on a tablet — 🔴 **but unmaintained for nearly six years.** Rescued from this base's unusable class this pass |
| **Mahara** 🔴 **ARCHIVED** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 GPL-3.0 · `35,148 B` | — | Global | 🔴 **ARCHIVED UPSTREAM, last push `2023-11-16` (`T901`)** — read-only, `★120`. ePortfolio, still the natural home for skills-based credentialing, 🔴 **but the engagement owns the fork from day one** |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | 🟢 BSD-3-Clause · `1,504 B` · `2d991b4832bb` | — | Global | Institutional repository for OER, theses and research output |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 AGPL-3.0 · `1,930 B` · `a5461e33e3db` 🔴 **(`p796` `T919`: the `1,930 B` is a POINTER, not a grant — it DECLARES `AGPL-3.0-or-later` plus BSD-3 contributed portions, and neither text ships at root)** | — | Global | The reference spaced-repetition scheduler. 🟡 For a permissive recurrence primitive instead, use [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) (BSD-3, `3,493 B`) — 🔴 **but it is STALE: last push `2024-06-27`, `28` months, not archived (`p795`).** 🟢 Recurrence rules are frozen mathematics, so the staleness is near-harmless here; pin the version and own the fork knowingly |
| **ODK Collect** | [`getodk/collect`](https://github.com/getodk/collect) | 🟢 **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | 🟢 Offline mobile data collection — the field instrument for a readiness diagnostic or a baseline survey where connectivity fails |
| 🔴 **Metabase** | [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 **SPLIT BY DIRECTORY** · `855 B` · `6006cc9c65dd` | — | Global | Frequently the BI layer a client already runs over learning data. 🔴 **AGPL-3.0 outside `enterprise/`, Metabase Commercial License inside it.** Deploy it; do not vendor code out of it without deciding which side of the boundary you are on |

## 🟢 School operations — timetabling, substitution and behaviour (`p789`)

🟢 **New category this pass, and it is the one with the clearest architecture.** The permissive
supply here is **solvers plus approval gates**, not conversational agents — which means the AI layer
sits at the *edges* of a deterministic core, reading intent and explaining outcomes, never deciding
the schedule itself.

| Platform / component | Address | Grant | What an AI layer attaches to |
|---|---|---|---|
| 🟢 **Timefold** (via case study) | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | A **constraint solver** on Quarkus. The LLM turns plain-English policy into constraints and explains rejections; the solver produces the timetable |
| 🟢 **OR-Tools** (via Timable) | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | Clash-free, priority-aware scheduling with a Streamlit surface — the second independent solver |
| 🟢 **schoolflow-agent** | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) | 🟢 MIT · `1,081 B` · `1b7481d92d0f` | **Disruption handling** — absences and substitutions — with a **human approval step** before any schedule is written |
| 🟢 **ClassCharts** (via agent) | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | 🇬🇧 A live UK homework/behaviour MIS, attached **read-only** on a parent account |
| 🟢 **D2L Brightspace** (via MCP) | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 MIT · `1,200 B` · `a873478a6b4e` | The third major North American LMS, over MCP |
| 🔴 **School ERP** (via MCP) | [`NSK-394/schoolbridge-mcp`](https://github.com/NSK-394/schoolbridge-mcp) | 🔴 **ungranted** | **Role-based** agent access to attendance, fees and student records. 🔵 The right control surface, no grant — an upstream licence request |

🔴 **The caution this section exists to state.** Timetabling, attendance and safeguarding touch
children's personal data and, in the EU, sit close to the high-risk boundary when they feed
decisions about individuals. 🟢 The read-only attachment (`classcharts-agent`) and the approval gate
(`schoolflow-agent`) are not conveniences — **they are the two design choices that keep this
category deployable**, and both already exist in permissive code.

## Interop — the layer that makes all of the above composable

| Component | Address | Grant, on the bytes | Region | Why it matters |
|---|---|---|---|---|
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 **Apache-2.0** · `10,273 B` · `f54555227df1` | Global | 🟢 **The single most useful licensing tool in this file.** Hosts LTI tools that any LMS can launch *across a process boundary* — so permissive or proprietary AI code serves Moodle, Canvas or Sakai **without becoming a derivative work of them** |
| **OOAPI** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 EUPL-1.2 · `13,827 B` · `d9c5b0a1a68d` | EMEA | 🟢 A **live** open education interop standard — courses, offerings, enrolments, results |
| **European Learning Model** 🟡 **ARCHIVED** | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 EUPL-1.2 · `13,865 B` | EMEA | 🟡 **ARCHIVED UPSTREAM, last push `2024-02-14` (`T901`)**, `★54`. 🟢 **The European Commission's own** learning and credential data model — the vocabulary an EU public-sector client is most likely to be asked to speak. Rescued from the ungranted class this pass |
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 EUPL-1.2 · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms, `1,697★` |
| **Open WebUI** ✏️ | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🔴 **`BSD-3-Clause + BRANDING RIDER` (non-OSI)** · `2,819 B` · 🟢 `99f39e7feff2` | Global | 🔴 **CORRECTED at `p794` (`T900`).** Self-hosted chat surface over a school-controlled model — still the fastest data-resident front end, 🔴 **but clause `4` makes removing or replacing the "Open WebUI" branding a material breach, so it cannot be delivered white-labelled.** 🔵 Two of its three root licence files read clean; `LICENSE` is the one that governs |

## The rule this file exists to state — amended this pass

🟢 **An engagement's licensing posture is decided by where the AI code sits, not by which LMS the
client runs.** Three safe attachment points, in order of preference:

1. **LTI across a process boundary** (`csev/tsugi`, Apache-2.0) — works with Moodle, Canvas, Sakai,
   Open edX; your code never links to theirs. For D2L Brightspace, the equivalent is
   `brightspace-d2l-mcp` (MIT).
2. **The platform's web API / web services** — same boundary, no LTI ceremony.
3. **Generated content rather than generated code** — producing H5P or QTI items is authoring data,
   which carries none of the host platform's copyleft.

🔴 **Only embed directly when the host itself is permissive — AND its dependencies have been read.**
That second clause is new, and it is the whole point of `T861`:

| Host | Repo grant | First-layer deps | Embed directly? |
|---|---|---|---|
| `jupyter/nbgrader` | BSD-3 | 🟢 `0` of `18` copyleft | 🟢 **Yes** |
| `CAHLR/OATutor` | MIT | 🟢 `0` of `43` copyleft | 🟢 **Yes** |
| `learningequality/kolibri` | MIT | 🟡 `2` LGPL of `32` | 🟡 **Yes, with the LGPL components kept replaceable and their source available** |
| `oppia/oppia` | Apache-2.0 | 🔴 `1` **AGPL-3.0** of `171` | 🔴 **Not until `angular-shepherd` is removed or replaced** |
| `sakaiproject/sakai` · `OpenOLAT` · `opencast` | ECL-2.0 / Apache-2.0 | ⚪ not audited | 🟡 **Permissive at the root; audit before shipping.** 🔴 **`p796`: `OpenOLAT` audited and the root was not the whole answer — brand assets `CC BY-ND 2.5` in `NOTICE.TXT` (`T914`)** |
| 🟢 **`Kosudo/nextSIS`** `CORRECTED p790` | 🔴 **GPL-3.0** (served in an anthology) | ⚪ not audited | 🔴 **No — separate deployment, integrate at the boundary.** 🟢 **But it is now *usable*, which is the change:** this base barred it as proprietary for two passes. **The only open Student Information System it holds** |
| 🟢 **`MrEug3n1o/spanish-tutor-ai`** `NEW p790` | 🟢 MIT | ⚪ not audited | 🟡 **Permissive at the root — and the only row here with no external model call in its default loop.** That removes the cross-border data question instead of governing it, which is why `P788-4` now has a reference implementation |
| 🟡 **`jinlize-tech/*`** `NEW p790` | 🟢 Apache-2.0 (`100/100` sampled) | ⚪ not audited | 🟡 **Grant clean, code `0/130` platform-validated by its own README.** Take the `8`-centre back-office taxonomy now; take the packages only after your own tests |

🟢 **`p790` gives that rule a denominator.** The `5` new permissive rows placed this pass were each
probed for a scope carve-out and **`0` of `5` carry one** — their grants are unqualified at the
repository level. 🔴 **That is not the same as the curriculum being cleared.**
`bncc-lesson-generator` generates against Brazil's **BNCC**, `mi_icfes` against Colombia's
**Saber 11**, `StudyLah` against Malaysia's **SPM** — three state or ministry instruments, and
**none of the three repositories makes any claim about them in either direction.** 🔵 **The absence
of a scope clause is the absence of a *statement*, not a grant of the content.** `paes-mcp`, which
does state it (and names **DEMRE** as the rights-holder of Chile's PAES items), is the row that
taught this base to look — and it remains the only row in the base that answers the question
out loud.

🔵 **And one more rule, from `T864`.** In education the **content** has a rights-holder and the
repository is the cheap part. Exam items, textbooks and curricula belong to ministries, universities
and publishers — `paes-mcp`'s MIT grant covers its code and explicitly not Chile's PAES papers, which
belong to DEMRE. **Read the scope clause. Ask who owns the content.**
