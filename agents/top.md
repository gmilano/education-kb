---
industry: education
region: Global
updated: 2026-10-25
---

## 🆕 `p429` · 2026-10-25 — **A row this base published as MIT three times is now PROPRIETARY, and the change is dated to a single commit two days old. 🟢 The MIT lane is not lost — it survives at a different address, and this pass found that address by DIGEST EQUALITY rather than by looking for it. 🔴 And p428's `Trend 53` is refuted by the cohort it did not read.**

🟢 **Gates RAN on this host**, against `79362ca`: a baseline run **before this pass wrote a
line** exited `0` over 🟢 **56 blocking gates green**, and after these writes `make commit-gates`
exits `0` over the same 🟢 **56** — this pass built no new gate, and says so rather than
implying one. 🔵 **No date straddle:** every leg, `ls-remote`, clone, `ls-tree`, payload fetch
and digest happened **2026-10-25**; the commit lands **2026-10-25**.

🔵 **The legs.** Two GitHub repository searches, sorted by `updated` desc:
`google classroom mcp` → `total_count` **37**, **all 37 read**; `blackboard learn mcp` →
`total_count` **10**, **all 10 read**. 🟢 **47 of 47 resolve** under `git ls-remote` — no
credential prompt, no gone address, which is the first clean resolution sweep on these shelves.
🔴 **The four prescribed web legs returned ZERO addresses again — the third consecutive pass**
(`Gap 426-C`); they are recorded in `agents/trending.md` with what each actually returned.

### 🔴 A LICENCE REGRESSION on a row this base published three times — the first one here measured on both sides

🔵 **What this base said.** `pengusto/google-classroom-mcp` was read as **MIT** by **pase 74**
(2026-10-03, `LICENSE` recorded at **`1 145` B**, "concurring with `package.json`"), by **p340**
(2026-10-20, *"MIT"*, listed among nine permissive Google Classroom lanes), and by **p353**
(2026-10-21). p340's platform table names it as one of the two recommended Google Classroom
lanes: *"Teacher-side (`pengusto`) and student-side (`OmarNiazi`) lanes both MIT"*.

🟢 **Those readings were CORRECT WHEN TAKEN. The grant changed underneath them.** Read from the
file's own history this pass, with `git log --follow -- LICENSE`:

| commit | date | `LICENSE` payload | family |
|---|---|---|---|
| `8a548eb` | **2026-09-08** | **`1 145` B `sha256₁₂ a01639b20880`** | 🟢 **MIT**, dual copyright — *"Adrià Santacreu i Giménez and contributors"* **and** *"Pengusto (modifications)"*. 🔵 **`1 145` B is pase 74's figure exactly**, and the dual copyright is p268's note on this row exactly. Two passes' readings reproduced from history |
| `3609bf6` | **2026-10-23** — *"chore: commercially license maintainer extensions (#5)"* | **`3 053` B `sha256₁₂ d84e558a5033`** | 🔴 **PROPRIETARY — "Pengusto Commercial License 1.0"**, *"Effective for distributions carrying this notice from 2026-10-24"* |

🔴 **The clauses that decide an engagement, quoted from the payload at `3609bf6`:** §2 grants
**source inspection only**; §3 is titled **"Paid commercial agreement required"** and reaches
*"an educational institution or training provider, **whether nonprofit or commercial**"* **by
name** — which is precisely the buyer these shelves exist to serve. `package.json`'s `license`
field moved from **`"MIT"`** to **`"SEE LICENSE IN LICENSE"`**, and GitHub's own licence field
now reads **`NOASSERTION`**, so the API agrees the family changed.

🟢 **This is a regression, not an error by a predecessor, and the distinction is the point.**
No instrument on this base was wrong; the world moved. 🔵 What it demonstrates is that **a
permissive grade has a shelf life**, and that nothing here measures it: the shelves carry
a family read once and no re-read date. See `Gap 429-A`.

### 🟢 The MIT lane SURVIVES at another address, and a digest found it

🔴 **The obvious conclusion — "the teacher-side MIT Google Classroom lane is gone" — is wrong.**
🟢 One address in this pass's cohort carries `LICENSE` at **`1 145` B `sha256₁₂ a01639b20880`**:
**the same bytes pengusto abandoned**, confirmed with `cmp` and carrying the same dual copyright.

| address | grant, read at the SHA | heads | capability — band stated per cell | region |
|---|---|---|---|---|
| [`vTanco/google-classroom-mcp`](https://github.com/vTanco/google-classroom-mcp) | 🟢 **MIT** — `LICENSE` **`1 145` B `sha256₁₂ a01639b20880`** @ HEAD `9ba0070eff2f`, **byte-identical** to pengusto's pre-relicensing payload. 🟢 Tree **ENUMERATED**: one licence-shaped path 🟢 **`authoritative`** | **1** ref; pushed **2026-10-22**; ref set exactly `refs/heads/main` | 🟢 **The teacher-side authoring lane**, and it writes: creates coursework in bulk from one instruction, attaching a Drive file as **a copy per student**, with points, per-session due dates, and **`En borrador`** — created as DRAFT. 🔵 That draft-by-default behaviour is the human-in-the-loop step three jurisdictions ask for, already in the code | **EMEA** |

🟢 **Why that row is placed in EMEA on PAYLOAD evidence and not on its language.** A Spanish
README is evidence of a language, not of a country — Spanish is the language of both Spain and
most of LATAM, and this base has a standing rule against turning an anthroponym or a language
into a region (`gate-region-place`). 🟢 The placing evidence is a **curriculum token**: the
README's worked example is *"ESO 2º Tecnología"*, and **ESO — Educación Secundaria Obligatoria —
is the statutory secondary stage of the SPANISH school system**, not of any LATAM system.
🔵 **That is a named standard in the payload, which is exactly what `gate-region-place` accepts.**

🟢 **The practical rule, and it is one line.** An engagement needing the MIT teacher-side Google
Classroom lane should pin **`vTanco` at `9ba0070eff2f`**, not pengusto. Full chain, both sides of
the regression and the upstream check:
[`evidence/p429-licence-regression.2026-10-25-p429.tsv`](../evidence/p429-licence-regression.2026-10-25-p429.tsv).

### 🔴 And the grant pengusto left behind is readable ONLY inside pengusto

🟢 pengusto preserves the upstream notice at `LICENSES/MIT-upstream.txt` — **`1 101` B
`sha256₁₂ dd5ae846ce41`**, the **single-copyright** MIT, correctly stripped of its own
modification line. 🔵 **That is correct attribution hygiene and is recorded as such.**

🔴 **The upstream it names grants nothing at source.**
[`adriasantacreu/google-classroom-mcp`](https://github.com/adriasantacreu/google-classroom-mcp)
at HEAD `29c2c2a07670` has **ZERO licence-shaped paths across its whole tree** — established by
`git ls-tree -r HEAD` over all **15** paths, not by probing a filename — and **no `license`
field** in `package.json`. So pengusto's commercial licence asserts *"It remains available under
MIT"* about a repository whose own payload says nothing at all, and **the only extant copy of
that MIT grant is held by the party that relicensed away from it.**

🔵 **This is `Gap 428-B`'s shape, arriving through a different door.** p428 found a licence file
asserting twelve third parties' families inside an **attribution block**; here a **commercial**
licence asserts one third party's family, and it is equally unconfirmable. 🟢 `Gap 428-B` wanted
a second specimen before it could be a rate — it now has one, from a different channel.

🔴 **A correction this pass owes its own record:** the first probe for `LICENSES/MIT-upstream.txt`
returned **404** and this pass nearly published that absence. It was a **malformed URL** — the
SHA field had been read from the wrong column — and the tree enumeration caught it. 🔵 The
absence that *is* real (adriasantacreu) is the one established from a whole tree. **That is the
whole argument for `gate-subtree-grant`'s instrument over a path probe**, demonstrated at this
base's own expense.

### 🟢 Promoted to this shelf — eleven further new addresses, every grant read first-hand at the SHA

🔵 All eleven are absent from this base's **5 674** previously-cited slugs, checked against every
`.md` in the repository including both append-only logs.

| address | grant, read at the SHA | heads | capability — band stated per cell | region |
|---|---|---|---|---|
| [`BxnIceLemon/minerva-mcp`](https://github.com/BxnIceLemon/minerva-mcp) | 🟢 **ISC** — `LICENSE` **`741` B `sha256₁₂ 5d3787deebf3`** @ HEAD `534b7dc7b78e`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **0** refs; pushed **2026-10-21** | 🟢 **Blackboard Learn Ultra *and* Gradescope** in one server — the only address on these shelves spanning an LMS and a separate grading product. 🟢 Rides **the session the human already signed in with**, in a real browser window. 🔵 **Its README names its template:** *"follows the approach of [`campus-cli`](https://github.com/alejooroncoy/campus-cli)"* — a **LATAM** address already on these shelves | **EMEA** |
| [`UKplus8HRS/bb-mcp`](https://github.com/UKplus8HRS/bb-mcp) | 🟢 **MIT** — `LICENSE` **`1 067` B `sha256₁₂ 02049138f239`** @ HEAD `d639765bc267`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **0** refs; pushed **2026-10-21** | 🟢 Blackboard Learn via **Playwright** against *"your own institution's Blackboard site"* — **configurable, not institution-pinned**, which is the reusable shape of the cohort. 🔵 It drives a browser **because the REST path needs a key the institution must register**; see `Trend 54` | Global |
| [`AnonymousOnyx22/google-classroom-student-mcp`](https://github.com/AnonymousOnyx22/google-classroom-student-mcp) | 🟢 **MIT** — `LICENSE` **`1 072` B `sha256₁₂ ed912ca72d9e`** @ HEAD `f3c1bd8e6a11`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **0** refs; pushed **2026-10-24** — the freshest in this leg | 🟢 Read-only student lane: classes, due dates, **missing work**, grades on returned work. 🔵 **The fourth LMS from one owner** — this base already shelves the same owner's Canvas, Moodle and Brightspace student servers. One architecture, four platforms, by the only author here doing it deliberately | Global |
| [`Mattlo0546/classroom-mcp`](https://github.com/Mattlo0546/classroom-mcp) | 🟢 **MIT** — `LICENSE` **`1 067` B `sha256₁₂ 13c8ad755224`** @ HEAD `46e4ff4195b6` 🟢 **`authoritative`** | **0** refs; pushed **2026-10-20** | 🟢 Courses, assignments, announcements, materials — **and it downloads class slides**, saving Google Slides and Docs as PDF, one folder per course. 🔵 **Its licence digest is byte-identical to the same owner's `blackboard-mcp`** — see `Trend 56` | Global |
| [`Mugen-Ibi/Classroom-MCP`](https://github.com/Mugen-Ibi/Classroom-MCP) | 🟢 **MIT** — `LICENSE` **`1 081` B `sha256₁₂ b77185922cd4`** @ HEAD `5f746bdae197`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **0** refs, **1** fork; pushed **2026-10-14** | 🟢 Google Classroom over **Cloudflare Workers**, with a Japanese-language design and verification record under `docs/`. 🔴 **Its README states the cohort's governing constraint outright** — 「このリポジトリを自分のCloudflareアカウントへデプロイし、自分のGoogleアカウントで使うためのプロジェクトです。**共有サービスの接続先は提供しません**」: *deploy this to your own account; no shared endpoint is offered.* 🔵 That is `Trend 54` in an author's own words | **APAC** |
| [`supachai-j/google-classroom-mcp-project`](https://github.com/supachai-j/google-classroom-mcp-project) | 🟢 **MIT** — `LICENSE` **`1 090` B `sha256₁₂ 125a8bf7ce31`** @ HEAD `9490c0fc068b` 🟢 **`authoritative`** | **0** refs; pushed **2026-05-24** | 🟢 The most complete **assessment** surface in this cohort: rosters, student submissions **and their Drive attachments**, **computes weighted final grades**, exports CSV. 🔴 **Weighted grade computation is an Annex III high-risk function under the EU AI Act** — capable, and the one row here that cannot be dropped into an EMEA engagement without an oversight step around it | Global |
| [`charlie2233/coursebinder-ai-ready-google-classroom-exporter`](https://github.com/charlie2233/coursebinder-ai-ready-google-classroom-exporter) | 🟢 **MIT** — `LICENSE` **`1 068` B `sha256₁₂ 7f208bdb3cc4`** @ HEAD `54e1eccaf943` 🟢 **`authoritative`** | **0** refs; pushed **2026-06-21** | 🟢 Exports the Classroom content **a logged-in Chromium tab can already see** into a local AI-readable archive. 🔵 Its README draws the distinction this pass measures: *"a browser-visible-content exporter, **not a Google API downloader**"* — built to avoid the credential gate, not to hold a credential | Global |
| [`sinh-x/personal-google-mcp`](https://github.com/sinh-x/personal-google-mcp) | 🟢 **MIT** — `LICENSE` **`1 068` B `sha256₁₂ 5ed26262319d`** @ HEAD `6e6a98d957e0` 🟢 **`authoritative`** | **0** refs; pushed **2026-04-26**; 🟢 **4 branches** — the widest ref set in this cohort | 🟢 **Rust** — the only non-TypeScript, non-Python server in either cohort, and the only one with a memory-safe compiled runtime to offer an institution. 🔴 **Its ref set is itself evidence:** one branch is named `fix/oauth-token-refresh-hang` | Global |
| [`praisethefacts/dsh-plugin-google-classroom`](https://github.com/praisethefacts/dsh-plugin-google-classroom) | 🟢 **MIT** — `LICENSE` **`1 064` B `sha256₁₂ c35e96e7d382`** @ HEAD `4115d38621e4` 🟢 **`authoritative`** | **0** refs; pushed **2026-10-06** | 🟢 A **packaged bundle** of the owner's own Google Classroom server for a third-party agent harness — read-only course and assignment tools. 🔵 Shelved for the **distribution shape**: the server and its packaging-for-a-host are separate addresses, which is how a studio ships one connector to several clients | Global |
| [`PrahanG/Google-Classroom-MCP`](https://github.com/PrahanG/Google-Classroom-MCP) | 🟢 **MIT** — `LICENSE` **`1 060` B `sha256₁₂ f06ff8fa5a6c`** @ HEAD `5c675c96b901` 🟢 **`authoritative`** | **0** refs; pushed **2025-11-25** — 🔴 the oldest HEAD in this leg, eleven months stale | 🟢 Ships **both a JavaScript and a Python implementation** of the same server surface. 🔵 Shelved as a **parity reference** for a studio choosing a runtime, not as a dependency | Global |
| [`Shiv-D-Coder/google-mcp-agent`](https://github.com/Shiv-D-Coder/google-mcp-agent) | 🟢 **MIT** — `LICENSE` **`1 069` B `sha256₁₂ 2deff4ab7dff`** @ HEAD `206bff862a0e` 🟢 **`authoritative`** | **1** ref; pushed **2025-07-27** — 🔴 fifteen months stale | 🟢 **FastMCP** agent spanning Gmail, Drive **and** Classroom in one tool surface. 🔵 Shelved because the **multi-surface** shape is the one an institutional assistant actually needs; the code is a pattern, not a pin | Global |

🔴 **Graded honestly: ten of these twelve have ZERO or ONE ref.** They are pattern exemplars, not
dependencies — pin a SHA and expect to own the code. 🟢 **The exception is the one that matters:**
`vTanco` is load-bearing not because it is popular but because it holds a **specific grant** that
a row this base recommended no longer holds.

### 🔴 Declined this pass — read first-hand, no grant to read

| address | what was read at the SHA | why it is not on the shelf |
|---|---|---|
| [`tirbofish/google-classroom-mcp`](https://github.com/tirbofish/google-classroom-mcp) | HEAD read 2026-10-25. 🔴 **Zero licence-shaped paths**, no manifest field, no README claim | 🔴 **All rights reserved by default.** 🔵 **A real loss, and the most instructive payload in either cohort:** it is a browser-driving read-only server *"for Google Classroom accounts that **cannot grant OAuth access** to the official Classroom API … specifically students under **DETNSW**"* — the New South Wales Department of Education. **APAC**, institutionally placed, and `Trend 54`'s mechanism stated by an author who hit it |
| [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | HEAD read 2026-10-25, **2026-10-14**. 🔴 Zero licence-shaped paths | 🔴 **All rights reserved by default.** 🔵 README names **Universidad de Navarra, San Sebastián, Spain** and notes the Blackboard API is standard enough to retarget — an **EMEA** institutional address one `LICENSE` file away from being shelvable |
| [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) | HEAD read 2026-10-25, **2026-07-28**. 🔴 Zero licence-shaped paths | 🔴 **All rights reserved by default.** 🔵 README names the **University of Queensland** and **Okta SSO** — the **APAC** institutional shape, and the clearest SSO-brokered Blackboard lane found |
| [`JuancitoCozzeti24/santa-rita-escolar`](https://github.com/JuancitoCozzeti24/santa-rita-escolar) | HEAD read 2026-10-25, **2026-10-18**. 🔴 Zero licence-shaped paths | 🔴 **All rights reserved by default.** 🔵 Bridges Classroom **and SIEWeb**, a school-administration system used in Perú, with *matrícula* and *registro de notas* flows — the **LATAM** administrative shape this base has repeatedly recorded as missing |
| [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) | HEAD `3609bf6`, **2026-10-23**. 🟢 Grant payload present and read in full | 🔴 **Proprietary — "Pengusto Commercial License 1.0".** Source inspection only; §3 requires a paid agreement **naming educational institutions**. 🔵 **Not a defect in the repository and not hidden** — the relicensing commit says what it does, and the upstream notice is preserved. It is simply no longer a lane Globant can build on |

🔵 **Declared so the silence does not read as coverage: 21 of the 47 addresses read this pass
(45 %) carry NO grant payload at all** — and the four most useful of them are the four regionally
placed ones above. 🔴 **Grant absence, not copyleft, is still the binding constraint in this
sector**, now measured on two further cohorts. Full census:
[`evidence/p429-lms-cohort-census.2026-10-25-p429.tsv`](../evidence/p429-lms-cohort-census.2026-10-25-p429.tsv).

## 🆕 `p428` · 2026-10-25 — **A THIRD address channel, and it was sitting inside a licence file. 🟢 `semyonfox/canvas-mcp`'s MIT `LICENSE` names TWELVE upstream addresses with their families; six were unshelved, and the channel carries the OBLIGATION along with the address — which no other channel does. 🔴 Two of the twelve asserted grants do not hold up when read at source.**

🟢 **Gates RAN on this host**, against `b46290a`: the baseline run was 🟢 **55 blocking gates
green** before this pass wrote a line, and after these writes `make commit-gates` exits `0` over
🟢 **56 blocking gates green** — the new one is `gate-branch-alias`, built and wired on this
pass. 🔵 **No date straddle:** every leg, `ls-remote`, shallow clone, tree enumeration, registry
query and payload digest happened **2026-10-25**; the commit lands **2026-10-25**.

🟢 **`Gap 425-A` is REFUTED in its general form, and this pass measured the replacement.**
`p425`–`p427` recorded *"DNS is GitHub-only"* and concluded that **no** cell sourced outside
GitHub could ever be `authoritative`. On this host `registry.npmjs.org` and `pypi.org` both
return **`200`** with full JSON, `files.pythonhosted.org` and `crates.io` are reached, and
**`gitlab.com`** resolves — while `unesco.org`, `oecd.org`, `moodle.org`, `openedx.org`,
`huggingface.co`, `europa.eu` and `wikipedia.org` are all **`000`**. 🔵 The egress is a
**forge-and-package-registry allowlist**, not a GitHub-only DNS. 🟢 **A registry response is a
payload** — it can be digested and pinned (npm ships a `sha512` in `dist.integrity`) — so a
**registry cell CAN be `authoritative`**. 🔴 **Every policy and market cell on this base stays
`reported`:** not one standards-body or vendor domain resolves. Full probe:
[`evidence/p428-egress-allowlist.2026-10-25-p428.tsv`](../evidence/p428-egress-allowlist.2026-10-25-p428.tsv).

### 🟢 Promoted to this shelf — ten new addresses, plus one carried row re-graded on a second channel. Every grant read first-hand at the SHA

| address | grant, read at the SHA | heads | capability — band stated per cell | region |
|---|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) *(carried, re-graded)* | 🟢 **MIT** — and for the first time on this base the grant is confirmed on a **second, digestible channel**: PyPI `canvas-mcp` **`1.16.0`** declares the full MIT text and back-links to this exact repository 🟢 **`authoritative`** | 🟢 **308** refs, **99** forks; HEAD `c9274b74325f` **2026-10-25** | 🟢 Canvas LMS, **102 tools and 8 agent skills**, for students *and* educators; states compatibility with Claude, Cursor, Codex "and 40+ agents". 🔵 **This is the hub the Moodle cohort does not have** — ~14× the refs of the largest Moodle address on these shelves (`kad-xyz/spbstu-mcp`, 22) | Global |
| [`semyonfox/canvas-mcp`](https://github.com/semyonfox/canvas-mcp) | 🟢 **MIT** — `LICENSE` **`1 881` B `sha256₁₂ fea4cd7cb04d`** @ HEAD `e317c4b7bf10`. 🔴 **The size is the finding:** stock MIT runs ~`1 070` B; the extra `811` B is an **attribution block naming twelve upstream projects and their families inside the licence body**. 🟢 Tree **ENUMERATED**: one licence-shaped path 🟢 **`authoritative`** | **6** refs; last **2026-10-24** | 🟢 TypeScript Canvas server, **129 tested tools**, built against the **MCP `2026-07-28`** core revision, with **documented permission boundaries** | Global |
| [`Teci-AI/moodle-mcp-connector`](https://github.com/Teci-AI/moodle-mcp-connector) | 🟢 **MIT** — `LICENSE` **`1 103` B `sha256₁₂ c8bcb50d415c`** @ HEAD `2318b9927da5`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **1** ref; last **2026-10-23** | 🟢 External REST client for Moodle — reads *and authors* course content. 🔵 Its value here is as **half of a natural experiment**: the same owner publishes the in-LMS half separately, and the two grants differ. See `repos/foundations.md` | Global |
| [`The-Morrow-Project/Morrow-Bridge`](https://github.com/The-Morrow-Project/Morrow-Bridge) | 🟢 **MIT** — `LICENSE` **`1 071` B `sha256₁₂ f37f80963047`** @ HEAD `b5e9993c5d53`. 🟢 Tree **ENUMERATED**: **two** licence-shaped paths (`LICENSE`, `desktop/LICENSE`) carrying the **same digest**, so `gate-subtree-grant` is satisfied on both 🟢 **`authoritative`** | **31** refs — the highest in this leg; last **2026-10-20** | 🟢 **Cross-LMS**: Canvas first, Moodle in progress, Blackboard named. Ships as a Chrome extension **and** an Electron desktop app. 🔵 Its README states the thesis plainly — *"you should not have to wait for your institution to buy and roll out a separate course assistant"* — which is the **shadow-IT** procurement shape, not a campus rollout | Global |
| [`Jacob-Met/canvaspilot`](https://github.com/Jacob-Met/canvaspilot) | 🟢 **MIT** — `LICENSE` **`1 075` B `sha256₁₂ 85144488dcaf`** @ HEAD `e75196e94c6c`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **23** refs; last **2026-10-22**; 🔴 **63 open issues** | 🟢 MCP **+ CLI** with a **stay-open SSO session broker**: it uses the browser session the user already has rather than a Personal Access Token. 🔵 **That is a procurement fact, not a feature**: its README's reason is that *many schools disable* token issuance — so the token-holding architecture every other row here assumes is **unavailable at some institutions** | Global |
| [`arthurcuri/mcp-instructure-canvas`](https://github.com/arthurcuri/mcp-instructure-canvas) | 🟢 **MIT** — `LICENSE` **`1 074` B `sha256₁₂ 161c1c8666c3`** @ HEAD `fc3c813e76d0`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **1** ref; last **2026-10-23** | 🟢 Canvas read **and write**, Telegram reminders, a local Codex/Claude agent, and GitHub Actions automation. 🟢 **Region is placed on evidence in the payload, not on the author's name**: `timezone: str = "America/Sao_Paulo"` is the **default in code** (17 occurrences) and the README is pt-BR | **LATAM** |
| [`angelonrevelo/bettercanvasmcp`](https://github.com/angelonrevelo/bettercanvasmcp) | 🟢 **MIT** — `LICENSE` **`1 070` B `sha256₁₂ fe401a64566c`** @ HEAD `1f5a5969e502`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | 🔴 **1** ref; last **2026-10-12** | 🟢 Read-only, and its stated purpose is **the edges the popular Canvas servers skip**: due-date *overrides*, New Quizzes, group work and file text. 🔵 Useful as a **conformance checklist** against any Canvas server a studio picks, whatever it ends up shipping | Global |
| [`sweeden-ttu/canvas-lms-mcp`](https://github.com/sweeden-ttu/canvas-lms-mcp) | 🟢 **MIT** — `LICENSE` **`1 056` B `sha256₁₂ 06dcddbb6908`** @ HEAD `13f357361fe8`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **4** refs; last **2026-03-09** | 🟢 Canvas server scoped to one institution. 🟢 **The only North American institutional address on these shelves** — README names **Texas Tech University** explicitly, which is payload evidence, not a name inference | **North America** |
| [`a-ariff/canvas-mcp`](https://github.com/a-ariff/canvas-mcp) | 🟢 **MIT** — `LICENSE` **`1 064` B `sha256₁₂ 040d00e3cf79`** @ HEAD `28496f9ca414`. 🟢 Tree **ENUMERATED**: one path 🟢 **`authoritative`** | **2** refs; last **2026-02-16** | 🟢 TypeScript Canvas server with **CI wired** (a build badge against its own `ci.yml`) — one of the few in this cohort with a test gate of its own | Global |
| [`Kuria-Mbatia/Canvas-MCP-server`](https://github.com/Kuria-Mbatia/Canvas-MCP-server) | 🟢 **MIT** — `LICENSE` **`1 063` B `sha256₁₂ fd34175ea8f9`** @ HEAD `c2fee6cb2fc0` 🟢 **`authoritative`** | **4** refs; last **2025-10-08** — 🔴 the oldest HEAD in this leg, over a year stale | 🟢 "Notioc" Canvas server with **composite-intelligence tools** layered over the raw API. 🔵 Shelved for the **layering pattern**, not as a dependency | Global |
| [`Shashwatpog/poke-canvas-mcp`](https://github.com/Shashwatpog/poke-canvas-mcp) | 🟢 **MIT** — `LICENSE` **`1 072` B `sha256₁₂ b60d2cd596b7`** @ HEAD `4917cf253ef7` 🟢 **`authoritative`** | 🔴 **1** ref; last **2026-02-02** | 🟢 Canvas context for **Poke**, a third-party personal assistant. 🔵 The only row here whose consumer is **neither an IDE nor a chat client** — evidence the LMS-MCP surface is being consumed by general assistants too | Global |

🔴 **Graded honestly, and the honesty cuts two ways.** Nine of these eleven have **6 refs or
fewer**; they are pattern exemplars, not dependencies, and an engagement should pin a SHA and
expect to own the code. 🟢 **But `vishalsachdev/canvas-mcp` is not in that class** — 308 refs, 99
forks, a published PyPI distribution and a HEAD from today. It is the first address on these
shelves that a studio could plausibly **depend on** rather than read.

### 🔴 The twelve attributions, read at source — and two of them do not hold

🔵 **What the channel is.** `semyonfox/canvas-mcp`'s `LICENSE` does not merely say MIT. Below the
copyright line it lists twelve upstream projects *with their licence families*:
`vishalsachdev/canvas-mcp` (MIT), `DMontgomery40/mcp-canvas-lms` (MIT), `r-huijts/canvas-mcp`
(MIT), `mtgibbs/canvas-lms-mcp` (MIT), `ahnopologetic/canvas-lms-mcp` (MIT),
`aryankeluskar/canvas-mcp` (**ISC**), `a-ariff/canvas-mcp` (MIT), `sweeden-ttu/canvas-lms-mcp`
(MIT), `Jon-Vii/canvas-student-mcp` (MIT), `Kuria-Mbatia/Canvas-MCP-server` (MIT),
`enkhbold470/mcp-server-canvas` (MIT), `Shashwatpog/poke-canvas-mcp` (MIT).

🟢 **Why that is a channel and not a curiosity.** Every other address channel this base reads —
the name search, the bare backticked slug (`gate-bare-slug-channel`), the census union
(`gate-census-union`) — yields an address and nothing else. **This one yields the address, the
asserted family and the reason the obligation exists, in the same sentence.** Six of the twelve
were unshelved; four are promoted above.

🔴 **And it is an UNVERIFIED third-party claim, which this pass established by reading all
twelve at source:**

| the assertion | what the payload says | grade |
|---|---|---|
| `enkhbold470/mcp-server-canvas` is **MIT** | 🔴 **No licence file at all.** `git ls-tree -r` at HEAD `386f198241ee` returns **zero** licence-shaped paths, and `package.json` has **no `license` field**. The only claim anywhere is a README heading reading *"## License / MIT"* | 🔴 **README-only** (`gate-readme-channel`, p288) — not a payload, and absent one the default is all-rights-reserved |
| `Jon-Vii/canvas-student-mcp` is **MIT** | 🔴 **The address does not resolve.** `ls-remote` answers with a **credential prompt** while the control `moodle/moodle` resolves anonymously | 🔴 **UNVERIFIABLE** (p293: a credential prompt is a measurement — private or gone) |
| the other ten | 🟢 Each resolves, and the four read first-hand this pass carry a licence payload whose family matches the assertion | 🟢 `authoritative` for the four read; `reported` for the six not read this pass |

🔴 **So the notice obligation on `semyonfox/canvas-mcp` is THIRTEEN copyright lines, not one** —
and two of the thirteen name a project whose grant cannot be confirmed from its own payload.
🔵 **This is `gate-restatement`'s subject (p289) arriving through a door it does not watch**: that
gate grades a restatement of an unreachable authority in a **README**. Here the restatement is
**inside the licence file**, where every instrument on this base reads the family and stops.

🟢 **The practical rule, and it is cheap.** When a licence file names upstreams, resolve each one
before shipping: the obligation you owe is to the project as it is, not as the file you inherited
says it was. Full table:
[`evidence/p428-address-verification.2026-10-25-p428.tsv`](../evidence/p428-address-verification.2026-10-25-p428.tsv).

### 🔴 Declined this pass — read first-hand, no grant to read

| address | what was read at the SHA | why it is not on the shelf |
|---|---|---|
| [`CarvalhoJeo/moodle-unisinos-mcp`](https://github.com/CarvalhoJeo/moodle-unisinos-mcp) | HEAD `05799bc9ee99`, **2026-10-23**. 🔴 Zero licence-shaped paths; no `license` field in `package.json`; no README claim | 🔴 **All rights reserved by default.** 🔵 A pity: a Brazilian-university Moodle connector is exactly the LATAM shape this base is short of, and one `LICENSE` file would change that |
| [`jtuttas/moodle-agent-mcp`](https://github.com/jtuttas/moodle-agent-mcp) | HEAD `f96bbe8cd7c9`, **2026-10-23**, **3** refs. 🔴 Zero licence-shaped paths, no manifest field, no README claim | 🔴 **All rights reserved by default** — despite reading submissions and **writing grades**, which is the highest-consequence surface in this cohort |
| [`enkhbold470/mcp-server-canvas`](https://github.com/enkhbold470/mcp-server-canvas) | HEAD `386f198241ee`, **2025-03-26**. 🔴 README says MIT; nothing in the payload does | 🔴 **README-only claim.** Asserted MIT by a third party's licence file, which is where it was found |

🔵 **Stated so the absence cannot read as an oversight:** three of the fourteen addresses read
first-hand this pass carry **no grant payload**. That is **21 %** of what one day's legs returned,
and it is the single commonest reason a usable-looking address is unusable.
## 🆕 `p427` · 2026-10-25 — **SIXTEEN unshelved addresses from ONE two-word leg, after `p426` recorded eleven consecutive passes of zero. 🟢 `Gap 426-C` is CONFIRMED and its MECHANISM is named: this cohort is named after the INSTITUTION, not the platform, so `p426`'s name-keyed census catches exactly 1 of the 16. 🔴 And one of the sixteen carries a grant shape nine instruments on this base read wrong.**

🟢 **Gates RAN on this host**, against `13ecffc`: the baseline run was 🟢 **54 blocking gates
green** before this pass wrote a line, and after these writes `make commit-gates` exits `0` over
🟢 **55 blocking gates green** — the new one is `gate-conjunctive-grant`, built and wired on this
pass. 🔵 **No date straddle:** every leg, `ls-remote`, shallow clone, tree enumeration and payload
digest happened **2026-10-25**; the commit lands **2026-10-25**, so `updated:` carries one date.

🔴 **`Gap 425-A` reproduces, and this pass measured it on a SECOND channel.** `p426` recorded
`curl` at `HTTP 000` for every non-GitHub domain. On this host **both** fetch channels fail:
`curl` returns `000` for `unesco.org`, `oecd.org`, `iesalc.unesco.org`,
`education.ec.europa.eu`, `multistate.us`, `en.wikipedia.org` and
`digital-strategy.ec.europa.eu`, and the tool-side fetcher fails **DNS resolution**
(`ENOTFOUND`) on the same domains while resolving `github.com` normally. 🟢 So the gap is
narrower and harder than "this host cannot reach": **DNS is GitHub-only, and server-side search
summaries are the one non-GitHub channel** — summaries cannot be digested, so **no policy or
market cell on a host of this class can ever be `authoritative`.** Every licence cell below is
`authoritative`; every policy and market cell is `reported`.

### 🟢 Promoted to this shelf — six addresses, every grant read first-hand at the SHA

| address | grant, read at the SHA | heads | capability — band stated per cell | region |
|---|---|---|---|---|
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | 🟢 **MIT** — `LICENSE` **`1 078` B `sha256₁₂ d0a329112827`** @ HEAD `a0c831a7d1af`. 🟢 Tree **ENUMERATED**: `git ls-tree -r` returns **exactly one** licence-shaped path. 🟢 `package.json` declares `"license": "MIT"` — two channels **agree** | **13** refs; last **2026-10-24**; 19 open issues | 🟢 Teacher-side Moodle agent, **es-ES throughout** (`"Te ayuda a preparar tu asignatura"`). Grades against **the teacher's own rubric**, works the forum, builds topics and quizzes, and reports how the class is going. Built on the **Claude Agent SDK** with **Playwright** browser automation — so it drives Moodle's *web UI* where no web-service token exists. 🟢 **`authoritative`** — read from the payload at the SHA | EMEA |
| [`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) | 🟢 **ISC** — `LICENSE` **`748` B `sha256₁₂ 2ad14eb14513`** @ HEAD `bdafc6ae0932`. 🟢 Tree **ENUMERATED**: one licence-shaped path. 🟢 `package.json` declares `"license": "ISC"` — two channels **agree** | **12** refs; last **2026-10-24** | 🟢 Moodle **+ SIU Guaraní** (the student-records system used across Argentine public universities) behind one agent. 🔵 The SIU Guaraní limb is the part that matters: it is a **records** system, not an LMS, and no prior row on these shelves reaches one. Authenticates on the institutional mail form `<legajo>@<especialidad>.frc.utn.edu.ar` 🟢 **`authoritative`** | LATAM |
| [`HyNuwa/UniMCP`](https://github.com/HyNuwa/UniMCP) | 🟢 **MIT *and* ISC** — root `LICENSE` **`1 980` B `sha256₁₂ 727b864af003`** @ HEAD `2916cce7a726`. 🔴 **This cell is TWO families and nine instruments on this base said one** — see the finding below. 🟢 Tree **ENUMERATED**: **four** licence-shaped paths, so a root-only read is wrong twice over (`gate-subtree-grant`) | **10** refs; last **2026-10-24**; carries `evals/` and `mcpb/` packaging | 🟢 Generalises `utn-mcp` from one university to **many**: UTN, **UNJu** (`virtual.unju.edu.ar`), **UNSa** (`exavirtual.unsa.edu.ar`) — Moodle *and* SIU Guaraní per institution. 🔵 A **multi-tenant** institutional connector is the shape a regional engagement actually needs 🟢 **`authoritative`** | LATAM |
| [`jamestesting0/tum-mcp`](https://github.com/jamestesting0/tum-mcp) | 🟢 **MIT** — `LICENSE` **`1 092` B `sha256₁₂ ce90dfa77bef`** @ HEAD `ef7cb0a8dc59`. 🟢 Tree **ENUMERATED**: one licence-shaped path. 🟢 **Three** channels agree: `package.json` `"license": "MIT"` **and** `pyproject.toml` `license = "MIT"` | **4** refs; last **2026-10-25** | 🟢 **36 tools** over **TU München** Moodle **+ Artemis** (the interactive-exercise/assessment platform) **+ Zulip**. 🔵 The Artemis limb is the first **assessment-platform** reach on these shelves that is not an LMS gradebook. Published to npm as `@jamestesting888/tum-mcp` — 🔴 note the npm scope (`…888`) differs from the GitHub owner (`…0`); pin the repository, not the package name. 🔴 README states it is **unofficial and independent of TUM** 🟢 **`authoritative`** | EMEA |
| [`kad-xyz/spbstu-mcp`](https://github.com/kad-xyz/spbstu-mcp) | 🟢 **MIT** — `LICENSE` **`1 064` B `sha256₁₂ 0dc1ec808f28`** @ HEAD `f142752372ac`. 🟢 Tree **ENUMERATED**: one licence-shaped path. 🟢 **`clean` under `Amendment 13`** — holder `kad-xyz` equals the owner segment, the **only** one of thirteen payloads this pass read where that is true | **20** refs; last **2026-10-24** | 🟢 **Go** implementation over SPbPU: `dl.spbstu.ru` Moodle, university mail, **and `openedu.ru`** (the Russian national MOOC platform). 🔵 Highest ref count among the granted addresses in this leg, and the only **compiled-language** member — relevant where a client will not run a Node or Python toolchain inside the campus network 🟢 **`authoritative`** | EMEA |
| [`simonseifert/merlin-mcp`](https://github.com/simonseifert/merlin-mcp) | 🟢 **MIT** — `LICENSE` **`1 070` B `sha256₁₂ c458af6b099b`** @ HEAD `a2633e3e1cda`. 🟢 Tree **ENUMERATED**: one licence-shaped path. 🟢 `package.json` declares `"license": "MIT"` — two channels **agree** | 🔴 **2** refs — the thinnest in the set; last **2026-10-24** | 🟢 **SRCE Merlin** (the Moodle 5.2 service shared across Croatian universities). 🟢 **Read-only by construction, with "phone-approved sends"** — a write is gated on an out-of-band human confirmation. 🔵 **That is the oversight artefact `Trend 48` is about, arrived at independently**: this is the second address on these shelves where human-in-the-loop is the default rather than studio-added, and the first where the approval leaves the machine 🟢 **`authoritative`** | EMEA |

🔴 **Graded honestly: these are small.** Ref counts run **2**–**20**; `merlin-mcp` and
`moodlia-portable` have **2**. 🔴 **They are pattern exemplars and connectors, not
dependencies** — an engagement should read the architecture, pin a SHA, and expect to own the
code. 🔵 Their value is that each one has already solved an **institution-specific
authentication and data-shape problem** that a studio would otherwise discover in week 3.

### 🔴 `T427` — `HyNuwa/UniMCP`'s grant is TWO FAMILIES, and nine instruments on this base read ONE

🟢 **The payload, read at the SHA.** Below a separator rule, `LICENSE` continues past its MIT
body:

> `Portions of this software are derived from utn-mcp and remain under its original license:`
> `ISC License` · `Copyright (c) 2026 Joaquín Peñalva`

🟢 **Both grants are live and simultaneous.** Nothing is chosen: **MIT** (© *MaxiFG*) governs the
work, **ISC** (© *Joaquín Peñalva*) governs the derived portions, and a distributor owes **both**
notices. 🟢 **And this pass verified the named parent independently in the same leg** —
`nialvape/utn-mcp`, **ISC**, `748` B `sha256₁₂ 2ad14eb14513`, **© Joaquín Peñalva**: the same
holder the ISC segment names. 🔵 This is the **correctly-attributed** form of what `p426`'s
`T129` caught undeclared — the lineage is stated **inside the grant**.

🔴 **Nine instruments, one answer, and it is incomplete:**

| instrument | its declared subject | on this payload |
|---|---|---|
| `p198` `p306` `p228` `p211` `p191` `p419` *(6 family classifiers)* | the licence **family** | 🔴 all six → **`MIT`**; none reports ISC |
| `p228.dual_grant` | a **CHOICE** — *"available under either MIT or GPLv2"* | 🔴 **`None`** — the payload offers no choice |
| `p202.scope_reader` | a **PATH** — `skills/` AGPL-3.0, `app/` AGPL-only | 🔴 **`split_scope=False`**, and it emits the `-----` separator as a spurious scope row |
| `p419.menciones_cruzadas` | copyleft parentage (needles `affero`, `lesser general public`) | 🔴 **`[]`** — a permissive-to-permissive cross-grant is outside its vocabulary |

🟢 **Not one of those is a bug; each is correct inside its scope.** The gap is that **no scope
covered this payload**, so the taxonomy is **three** shapes and this base had instruments for
two: **DISJUNCTIVE** (`p228`), **PATH-SCOPED** (`p202`), and **DERIVATION-SCOPED** — which had
none.

🔴 **The cost passes every tier check, which is why nothing caught it.** Both families are
permissive, so `commercial_use` is unaffected and no licence gate goes red. The defect is an
**understated notice obligation**: the `MIT` cell owes **one** notice; the payload owes **two**,
and the second is a **named third party's copyright**. A studio shipping one notice here drops an
attribution it actually holds.

🟢 **Built and wired on this pass**, so it is standing rather than a one-off:
[`gate-conjunctive-grant`](../compose/code/p427-conjunctive-grant/) — **24 controls**,
blocking, no network, in `HOOK_GATES` and `COMMIT_GATES`.
🔵 **Its two guards were calibrated against a real payload, not an imagined one.** Stock
**GPL-3.0** (`35 149` B, carried by `EduardoKrausME/moodle-local_mcp`) names
`13. Use with the GNU Affero General Public License.` in its own §13 **and** contains
`at your option` twice — so the naive form of *both* detectors fires on it. Guard 1 requires a
**standalone title line**; guard 2 requires a **scope sentence** above the second title, and
stock GPL-3.0 has none. `C7`–`C10` hold it out.
🔵 **Population, derived after the writes:** **265** licence payloads committed to this base,
**1** conjunctive, **2** disjunctive, **262** single. 🔴 One in 265 is not a trend — but it was
found in the **first ten addresses this pass read**, and those two rates are not the same claim.

### 🔴 `T428` — `Amendment 13` MEASURED: it fires on 12 of 13 payloads and NONE of the 12 is a fork

🟢 `p426` registered `Amendment 13` — *compare the copyright **holder** against the **owner**
segment* — on **one** specimen, and explicitly made it *"a signal rather than a verdict."* 🟢
**That caution is now vindicated with a number.** Across the **13** payloads this pass read
first-hand, the raw comparison fires **12** times (**92 %**) and **zero** of those twelve is a
fork. Full rows in
[`evidence/p427-amendment13-measurement.2026-10-25-p427.tsv`](../evidence/p427-amendment13-measurement.2026-10-25-p427.tsv).

| class | n | why it fires |
|---|---|---|
| 🟢 **CLEAN** | **1** | `kad-xyz/spbstu-mcp` — holder equals owner |
| 🟡 **NORMALISATION** | **4** | one identity in two spellings: `Simon Seifert`/`simonseifert`, `Carlos André Ferreira`/`CarlosAndreFerreira` *(accent fold)*, `Matt Lo`/`Mattlo0546` *(digit strip)*, `Alexander Leschinskiy`/`av-leschinskiy` *(surname substring)* |
| ⚪ **STOCK-TEXT — the question is UNDEFINED** | **2** | both GPL-3.0 rows: a stock copyleft text carries the **Free Software Foundation's** notice and **never** names the project's holder, so no named party exists to compare against |
| 🟡 **COLLECTIVE** | **2** | `TUM Moodle integration contributors`, `Lakshman Reddy and contributors` — a project body, not a named party |
| 🔴 **PERSON-VS-HANDLE — irreducible** | **4** | a real person whose handle or org simply differs: `falkenslab`/*Francisco Vargas Ruiz*, `nialvape`/*Joaquín Peñalva*, `OmarAli-prod`/*Omar Ismail*, `HyNuwa`/*MaxiFG* |

🔴 **The obvious refinement is REFUTED by `p426`'s own specimen, and this pass tested it rather
than assuming it.** Adding *"holder equals the HEAD commit author"* as a third channel resolves
`HyNuwa/UniMCP` cleanly — holder `MaxiFG`, HEAD author `MaxiFG`. 🔴 **But on `thc1006/moodle-mcp`
the HEAD commit author is ALSO `G36maid`**, because a fork **carries the upstream's commits**, so
the upstream's author is the fork's HEAD author **by construction**. The channel is satisfied in
the fork case **and** the legitimate case: it cannot discriminate, and wiring it would turn this
base's **only** true positive into a **miss**. 🔵 Recorded as a refutation, not an improvement.

🟢 **What did separate the two specimens: the licence payload DIGEST, shared across OWNERS.**
`thc1006/moodle-mcp` and `G36maid/moodle-mcp` both carry `LICENSE` at **`1 064` B
`sha256₁₂ 5da1fff0a1db`** — byte-identical, two owners, and the holder names *the other owner*.
`UniMCP`'s payload (`1 980` B `727b864af003`) collides with nothing, because it is **not a copy**:
it is a declared derivative that states its lineage in the grant text. 🔵 That is
`gate-payload-digest`'s existing subject, so the discriminating form of `Amendment 13` is a
**join onto an instrument this base already has**. 🔴 **Not claimed as a rate:** two specimens, one
positive and one negative, is a hypothesis.

### 🔴 Three of sixteen carry NO grant at any depth, and the largest is the worst case

| address | refs | tree enumeration | consequence |
|---|---|---|---|
| [`JaipuriaAILabs/Moodle-MCP`](https://github.com/JaipuriaAILabs/Moodle-MCP) | 🔴 **93** — the **highest ref count in the whole leg** | 🔴 **zero** licence-shaped paths | 🔴 **Not shelvable at any capability.** Serves Jaipuria institutions (India) and gates on a Google account. The activity signal is the strongest in the set and the grant is absent — which is exactly the pair a studio misreads as maturity |
| [`JeabtiE/iep-gen-assistant`](https://github.com/JeabtiE/iep-gen-assistant) | 59 | 🔴 **zero** licence-shaped paths | 🔴 Not shelvable. **Thai special-education IEP** generation, built for the **JUMP THAILAND Hackathon 2026** — see the declared capability gap below |
| [`hd659/moodle-ed-autopilot-patch`](https://github.com/hd659/moodle-ed-autopilot-patch) | 2 | 🔴 **zero** licence-shaped paths | 🔴 Not shelvable. A **MYT (Malaysia)** deadline normaliser and short-extension guard; `README.md` is **empty** |

### 🔵 Declared, so silence cannot read as coverage

- 🔴 **ZERO North American addresses in sixteen.** Checked rather than assumed: every `.edu`
  string in the set resolves to **`.edu.ar`** (`unju`, `unsa`, `utn`), **`.edu.eg`**
  (`zewailcity`), or the placeholder `lms.university.edu`. 🟡 `Gap 427-B`: the institutional-agent
  supply in this cohort is **entirely non-US**, while the LMS whose agents dominate these shelves
  (Canvas) is **US-market**. Nothing has measured whether that is a discovery artefact or a real
  asymmetry.
- 🔴 **A real capability gap, now with a specimen and no grant.** **Special-education IEP**
  generation appears twice in this pass's capability legs (`JeabtiE/iep-gen-assistant`, and
  `100205ivan/EyeEP` which is **already shelved**) and the unshelved one carries **no licence**.
  🟡 `Gap 427-C`: there is demand-side evidence for IEP tooling and **no permissively-granted
  implementation** this base can offer.
- 🔵 **`ISC` is NOT new to this base.** Checked before claiming it: `ISC` already appears in cells
  across `agents/top.md`, `repos/foundations.md` and four other shelves, so `utn-mcp` extends an
  existing family rather than opening one.
- 🔴 **`24kchengYe/human-skill-tree` is NOT a `p427` finding.** This pass's census flagged its
  split notice as disjunctive; checking first showed `p200`/`p202` **already** registered it,
  with `ACTION OJ`/`ACTION OR` and a built scope reader. Recorded so the sweep's output is not
  mistaken for a discovery.

## 🆕 `p426` · 2026-10-25 — **One unshelved address in eight legs — and it is the first grading agent on these shelves whose DEFAULT behaviour is the artefact three jurisdictions demand. 🔴 And this pass COMMITTED `T127` before catching it: a slug census run without a boundary terminator reported four live addresses as dead, because `owner/moodle-mcp-server` folds into `owner/moodle-mcp` under an unanchored pattern.**

🟢 **Gates RAN on this host**, against `49585c4`: the first run went **red at `gate-union-currency`** on `p425`'s inherited census, and the final run is 🟢 **54 blocking gates green** (`gate-census-union` is the one declared, non-blocking red). 🔵 Three gates fired on this pass's own first drafts and all three were right — `gate-union-currency`, `gate-identity`, `gate-case-collision`. 🔵 This **contradicts `Gap 425-B`**, which recorded `make commit-gates` and `make hooks`
as refused by the host's auto-mode classifier. Per `p423`'s rule — *a declared-un-run suite must
never be read as un-runnable* — `p425` scoped that refusal to **its** host rather than to the
suite, and the scoping is now **vindicated**: the suite is runnable and it was the **host** that
varied. 🔵 **No date straddle:** every leg, `ls-remote`, clone, tree enumeration and payload digest
happened **2026-10-25**; the commit lands **2026-10-25**, so `updated:` carries one date.

### 🟢 The one unshelved address in eight legs — promoted to this shelf

| address | grant, read at the SHA | heads | capability — band stated per cell |
|---|---|---|---|
| [`kaushikgunasekaren/canvas-grader-mcp`](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | 🟢 **MIT** — `LICENSE` **`1 076` B `sha256₁₂ 2bcdae923d26`** @ HEAD `c47e8b3ac2ae`. 🟢 Tree **ENUMERATED**, not laddered (`gate-subtree-grant`): `git ls-tree -r` returns **exactly one** licence-shaped path. 🟢 `pyproject.toml` declares `license = "MIT"` — the two channels **agree**, so this is not a `T117` metadata conflict | **2** refs (`HEAD`, `main`); **1** commit; last **2026-10-20**; CI present (`.github/workflows/test.yml`) and `tests/test_server.py` | 🟢 Canvas LMS grading for **teachers and TAs**. Reads rubric criteria and ratings, **per-student** due dates including overrides and extensions, and the course's automatic late policy; ingests submissions as **PDF, `.docx`, Jupyter, Scratch `.sb3`, zip, source**; classifies every submitted link so a photo album is not accepted as the required video; flags students who submitted **identical files**. 🟢 **`authoritative`** — read from the payload at the SHA |

🟢 **Why it earns a row rather than a mention.** `p421` established the boundary regulators are
drawing — *a tutor is generally outside EU Annex III; a grader is inside it* — and `p425`'s Global
block states that **one** deliverable serves EMEA's Annex III (**2027-12-02**), Vietnam's Decision
33 (**in force 2026-08-15**) and the US state statutes barring AI from replacing a licensed
educator: **a reviewable human-in-the-loop evidence trail.** 🟢 This address is the first on these
shelves where that trail is the **default construction** rather than an integration the studio
adds: grades, rubric scores and comments are **staged locally, previewed, and posted only on
explicit confirmation**, and the staged breakdown — per-category scores, late penalty, extra
credit — is written into the student's comment, which is the audit artefact itself.

🔴 **Graded honestly, because the row is five days old.** **1** commit, **2** refs, a star count in
the single digits. 🔴 **It is a pattern exemplar, not a dependency** — an engagement should read
the architecture and expect to own the code, not pin the package. 🔴 **And its own `README.md`
states the exposure plainly**: the server runs locally, but *the student work it reads is sent to
whichever AI model you use*. 🔵 Under **CA `AB 1159`** (student data barred from training AI models
unless the school directly benefits) and under Annex III, **that sentence is the procurement
question**, not a footnote — and it is to the repository's credit that it is in the README rather
than discovered at legal review.

### 🔴 `T127` — THIS PASS REPORTED FOUR LIVE ADDRESSES AS DEAD, AND THE CAUSE WAS A MISSING BOUNDARY TERMINATOR

🔴 **Committed, then caught, inside this pass.** Testing whether the discovery channel's
`moodle-mcp` was shelved, this pass ran a slug census over the live shelves with the pattern
`[A-Za-z0-9_.-]+/moodle-mcp` — **unanchored at the right-hand end**. It returned **18** owners. Five
of them answered `git ls-remote` with **0 refs** and `raw.githubusercontent.com` with **404**,
which this pass briefly recorded as *five dead addresses on the live shelves*, two of them
(`peancor` at 73 hits, `csmediapro` at 65) the base's most-cited of the name.

🟢 **The finding was false, and the re-run with a boundary terminator shows why:**

| census | pattern | distinct slugs | unresolvable |
|---|---|---|---|
| 🔴 first run | `[A-Za-z0-9_.-]+/moodle-mcp` *(unanchored)* | **18** | 🔴 **5** |
| 🟢 re-run | `github\.com/[A-Za-z0-9_.-]+/moodle-mcp[A-Za-z0-9_.-]*` *(boundary-terminated, captures the full slug)* | **16** — **12** `moodle-mcp` + **4** `moodle-mcp-server` | 🟢 **1** |

🟢 **Four of the five "dead" addresses are alive, and they are a DIFFERENT REPOSITORY** — the base
never carried `owner/moodle-mcp` for any of them, it carried `owner/moodle-mcp-**server**`, and the
unanchored pattern truncated the slug at its own last literal character:

| carried slug | refs, read this pass | `raw` README |
|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **5** | 🟢 `200` |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🟢 **9** | 🟢 `200` |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟢 **23** | 🟢 `200` |
| [`lmscloud-io/moodle-mcp-server`](https://github.com/lmscloud-io/moodle-mcp-server) | 🟢 **6** | 🟢 `200` |

🟢 **And the fifth is not new either.** `nahuelalbornoz/moodle-mcp` is genuinely unresolvable — **0**
refs, `raw` `404` — and [`intel/open-gaps.md`](../intel/open-gaps.md) **already names it**, in the
`5 of 47 addresses do not resolve` row, flagged `🆕` at the time it was found. 🟢 **So the corrected
yield of the whole exercise is ZERO new dead addresses.**

🔴 **Why this class is worth a `T`-number rather than a correction note.** A truncating census does
not fail loudly — it **manufactures a 404** by probing an address nobody ever published, and the
404 then reads as hard first-hand evidence of decay. 🔵 It is the mirror image of `gate-bare-slug`'s
concern: that gate asks whether a slug has an owner, and this failure invents a slug that *has* an
owner and does not exist. 🟢 **The control is one character**: a slug census must capture to a
**boundary**, never to the pattern's last literal. 🔵 Recorded with the wrong figure shown beside
the right one on purpose, because the wrong one looked exactly like a finding.

### 🔴 `T128` — THE CASE COLLISION IS REAL, IT IS INVISIBLE TO THE GATE BY DESIGN, AND THIS PASS PROVED BOTH BY BREAKING THE GATE

🟢 **The repository.** [`marcosnahuel/moodle-mcp`](https://github.com/marcosnahuel/moodle-mcp) is
also cited, in this base's append-only logs, under the owner spelling `MarcosNahuel`. 🟢 **Probed
separately this pass, both spellings `ls-remote` to the same HEAD
`d5ca68e8cd1b0ebc861a3f35916cfe9fb5ff7fdd`** — one repository. GitHub owner names are
**case-insensitive for resolution and case-preserving for display**, so both serve and neither
`404`s: every existence and currency probe this base runs passes on **both**.

🔴 **This pass's first draft was WRONG about where the collision lives, and the correction is the
more useful result:**

| population | `MarcosNahuel` | `marcosnahuel` | collision visible to `gate-case-collision`? |
|---|---|---|---|
| the **six curated shelves** the gate scans — `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md`, `intel/market.md`, `intel/trends.md`, `compose/patterns.md` | 🟢 **0** before this pass | **7** | 🟢 **No collision existed.** Run against pristine `49585c4`: **368** distinct slugs, **0 findings** |
| the **two append-only logs** — `agents/trending.md`, `repos/trending.md` | 🔴 **32** | **3** | 🔴 **Collision — and the gate does not scan these files** |

🟢 **The exclusion is deliberate and documented in the gate's own module:** *"The append-only files
are NOT scanned. History records the spelling that was published, and editing it would be the error
this KB forbids elsewhere."* 🔵 **So this is not a gate defect — it is the stated cost of the
append-only convention.** A repository may stand under two spellings **permanently** in the
history, and the detector is right to ignore it, because the only repair available is the
retro-edit `p352` forbids.

🔴 **And the demonstration was accidental.** This pass's first draft quoted both spellings as
`github.com/…` links into `agents/top.md` and `intel/open-gaps.md` — **importing a historical
collision onto a curated shelf** — and `gate-case-collision` went red at once, naming
`agents/top.md:89`. 🟢 **The gate was right and the write-up was wrong: documenting a collision is
not a licence to create one.** 🟢 The row above therefore links **one** canonical spelling — the
one the live shelves already used — and names the variant **as a string**.

🔵 **`p423` found this class on the repository segment**, via an instrument that had been in no
`make` target; this is the **owner** segment, and the reason it survived that wiring is that it
never reached a scanned file. 🟡 **`Gap 426-B` is therefore about a POPULATION, not a repair:** no
census has asked how many other repositories are dual-spelled inside the append-only logs, where
nothing is looking.

### 🔴 `T129` — THE DISCOVERY CHANNEL SERVED A FORK AS THE CANONICAL ADDRESS. SECOND SPECIMEN, AND THIS ONE IS CHEAP TO CATCH

🔴 Leg 9 returned [`thc1006/moodle-mcp`](https://github.com/thc1006/moodle-mcp) as *the* Moodle MCP
server — *"MCP server that lets AI agents operate Moodle: courses, assignments, forums, grades and
files-as-markdown"* — with no indication it is downstream of anything.

🟢 **Measured first-hand, both repositories, at their SHAs:**

| repository | `LICENSE` | `sha256₁₂` | copyright line **inside that repository** | HEAD | last commit |
|---|---|---|---|---|---|
| [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | **`1 064` B** | **`5da1fff0a1db`** | *"Copyright (c) 2026 **G36maid**"* | `18bd1777eb0b` | **2026-10-20** |
| [`thc1006/moodle-mcp`](https://github.com/thc1006/moodle-mcp) | **`1 064` B** | **`5da1fff0a1db`** | *"Copyright (c) 2026 **G36maid**"* | `cac60b6b37a8` | 🔴 **2026-10-15** |

🟢 **Byte-identical grant payloads, identical README banner, and the downstream copy is FIVE DAYS
STALE.** 🟢 `G36maid/moodle-mcp` is **already carried** on these shelves (13 mentions), so the
channel offered a fork of a shelved address as new supply.

🔵 **`p422` found this exact shape** — *"the discovery leg served a 683-commit-stale FORK as the
canonical address, with the upstream's copyright line intact so a licence-only check cannot see
it."* 🟢 **This specimen sharpens the control rather than repeating it.** `p422`'s was 683 commits
stale and therefore visible on any activity axis; this one is **five days** stale, which no
freshness heuristic would flag. 🟢 **What does catch it is free and deterministic: the copyright
holder inside `thc1006`'s own payload is `G36maid`, not `thc1006`.** 🔴 A licence *grade* cannot
see this — both repositories grade `🟢 MIT`, correctly. 🟢 **The holder string, compared against the
owner segment, is a one-field fork oracle**, and it is the field a licence read already has in
hand. 🔵 `gate-fork-direction` exists in this Makefile; this pass records the specimen and the
oracle rather than claiming the gate covers it.

## 🆕 `p425` · 2026-10-25 — **`T100`'s TENTH confirmation, and the cleanest one: three addresses the discovery channel presented as NEW, three payload reads, three carried cells reproduced EXACTLY — zero unshelved. 🔴 And the pass's real find is on this shelf itself: `agents/top.md` carries Canada's only provincial education-AI asset and, before this pass wrote into it, contained the string `canad` ZERO times — which is the mechanism by which `Gap 422-B` published an absence this base refutes.**

🔴 **Gates could NOT run on this host.** `make commit-gates` and `make hooks` were both refused by
this host's auto-mode classifier (`[Code from External]`) — reproducing `p422`'s condition exactly
and **not** `p423`'s. 🟢 Per `p423`'s own rule — *a declared-un-run suite must never be read as
un-runnable* — this is recorded as a property of **this host**, not of the suite. The file
contracts below are honoured **by hand**, and that is stated rather than implied (`Gap 425-B`).
🔵 **No date straddle:** every leg, `ls-remote`, SHA read and payload digest happened
**2026-10-25**; the commit lands **2026-10-25**, so `updated:` carries one date.

### 🔴 `T124` — this shelf refutes `Gap 422-B`, and it does so without ever using the word

🔴 `intel/market.md` publishes, as an informed gap: *"`Gap 422-B`: **no Canadian federal or
provincial education-AI instrument is on these shelves**, and the gap is now explicit rather than
assumed"* — re-published unchanged by `p424`.

🟢 **This shelf has carried a provincial one since `p388`.**
[`pdg6/bc-curriculum-mcp-server`](https://github.com/pdg6/bc-curriculum-mcp-server) is an MCP
server over the **entire British Columbia Ministry of Education K–12 curriculum** — a Canadian
province's statutory curriculum, including the **First Peoples Principles of Learning**. Re-read
first-hand this pass: **MIT**, `LICENSE` **`1 070` B `sha256₁₂ e14de82d46bf`** @ `687c55b7ed3c`,
holder *"Copyright (c) 2026 Paul de Groot"*, `package.json` declaring `"license": "MIT"` — the two
channels **agree**, so this is not a `T117` metadata conflict. **4** refs; `package.json` version
**`1.1.1`**, which also updates `p388`'s *"2 releases, both 2026-03-27"*.

🔴 **The mechanism, measured.** The slug appears **15** times across these shelves and **0** of
those lines contain `canad` in any case or inflection. *"British Columbia"* appears **4** times,
**3** of which do name Canada — but never on a line with the slug. 🔴 **And `agents/top.md`, the
file holding the full row, contained `canad` ZERO times** — measured **before this section was
written**, which is the only state in which the figure is true, since this very paragraph changes
it. `canad*` had **113** hits across the shelves, in six files, of which this file and
`verticals/solutions.md` were not two. 🔵 Pinned to its measurement time on purpose: `p424`'s
`gate-census-currency` red was exactly a figure derived before that pass's own writes and then
published as current.

🔵 So the absence was keyed on a **string** while the refutation sits under a **jurisdiction name
one level down**. That is `gate-capability-absence`'s predicate verbatim — *an absence whose
refutation is in the base's own harvest log under different words* — and it is the **third
consecutive pass** in which the corpus held the answer and the pass republished the absence
(`p423` formalms, `p424` `Gap 298`, `p425` here). 🟢 `T120`'s shape, now with a measured blind
spot rather than an anecdote.

### 🟢 `T100`, tenth confirmation — and every candidate died on a payload read, not on a grade

🔵 Eight legs (four global, four regional). The discovery channel offered **three** addresses as
new supply. **All three reproduce cells this base already carries, to the byte.**

| address | this pass, read first-hand | carried | verdict |
|---|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0**, `LICENSE` **`11 120` B `0688f62d04f1`** @ HEAD `4debc94780cc`, title line *"Educational Community License, Version 2.0 (ECL-2.0)"*; **15 512** refs | `11 120` B `0688f62d04f1`, read at SHA `c35e7a2` | 🟢 **CARRIED — and a currency confirmation at a NEW SHA.** The grant holds at today's HEAD, not merely at the SHA the row was written against |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | 🟢 **ODbL** *(Open Data Commons Open Database License)*, `LICENSE` **`25 289` B `77d2692c3d64`** @ HEAD `7bd8b6794cb7`; **102** refs, one branch `curriculum/australia-cleanup-ontario-2026-10-23` — **two days old** | *"ODbL-1.0 + CC BY-SA 4.0 … 25,289 bytes"* | 🟢 **CARRIED, byte-exact.** 🔴 **Not MIT**, against a trending roundup that lists it among education repos without a grant |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0**, `license.txt` **`33 893` B `db1a87ba81e8`** @ HEAD `5d6df8e3ed8e`; **2 472** refs | `AGPL-3.0-or-later` | 🟢 **CARRIED** — and the *claim* against it is new, below |

🟢 **The disposal is the finding.** `p424` closed on *"the pass's only significant find came from
spending a carried ACTION on a payload read, not from a discovery leg"*. 🔵 This pass has **no**
carried ACTION to spend and **no** significant supply find — and the three reads it did spend all
came back `CARRIED`. **Tenth consecutive pass in which the supply layer returns nothing unshelved.**

### 🔴 `T125` — the "MIT LMS" claim is a FRAMEWORK/APP CONFLATION, and the claim's own sentence carries the mechanism

🔴 The vertical-platform leg returned, as its single permissive-platform hit: *"**Frappe LMS** is a
100% MIT-licensed LMS by Frappe Technologies (India), **built on the Frappe/ERPNext framework**."*

🟢 **Measured first-hand, both repositories, this pass:**

| repository | role | grant, read at SHA |
|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | the **framework** | 🟢 **MIT** — `LICENSE` **`1 118` B `bc6001a54ffc`** @ `360bcc23bc81`, *"Copyright (c) 2016-2021 Frappe Technologies Pvt. Ltd."* |
| [`frappe/lms`](https://github.com/frappe/lms) | the **application** | 🔴 **AGPL-3.0** — `license.txt` **`33 893` B `db1a87ba81e8`** @ `5d6df8e3ed8e` |

🟢 **And the app's tree was ENUMERATED, not laddered** (`gate-subtree-grant`, `p382`): `git
ls-tree -r` over `frappe/lms` HEAD returns **exactly ONE** licence-shaped path — `license.txt`.
🔴 **There is therefore no MIT component anywhere in the LMS repository**, at any depth, so the
claim cannot be rescued as a statement about a subtree.

🔵 **The claim is true of the framework and false of the application, and its own subordinate
clause is the transmission path.** 🟢 **Sharper than `p424`'s `forma LMS` specimen**, where the
circulating *"Apache-2.0"* traced to an unrelated web-server line in a requirements list: here the
false sentence contains a **correct** statement about a **different repository** and inherits its
licence across a dependency boundary. 🔴 **Procurement rule, extended:** a grant is a property of
**a repository at a SHA**, never of a vendor, a product family, or the framework underneath. Two
addresses from one house, one permissive and one copyleft, is the normal case.

### 🔴 `T126` — A COMMIT SHA IS PUBLISHED IN A PAYLOAD-DIGEST COLUMN, AND THIS PASS REPRODUCED THE ERROR BEFORE CATCHING IT

🔴 **Found by this pass's own hand-check**, re-reading the three carried digests it had cited
rather than read (`p289`: a restatement is not an authority). Two of three matched
(`OpenOLAT/OpenOLAT` `10 982` B `6dbc5b605ed0` @ `d073ad444fe5`; `duck-5/moodle-mcp` `1 072` B
`64dc9680d3bb` @ `dd9682ca97e3`). **The third did not.**

[`dodona-edu/dolos`](https://github.com/dodona-edu/dolos), read first-hand at **two** refs:

| ref | `LICENSE` | `sha256₁₂` |
|---|---|---|
| HEAD `2b82821c29d7` *(today)* | **`1 084` B** | **`881163366572`** |
| `44925b867ce7` *(the value the shelves carry)* | **`1 084` B** | **`881163366572`** |

🟢 **Byte-identical at both refs, so this is NOT drift** — the payload has not changed, and two
carried cells were simply wrong when written.

🔴 **Two distinct defects in the carried rows:**

1. **`44925b867ce7` is a COMMIT SHA, published in a payload-digest column.** `agents/trending.md`
   and `repos/trending.md` both render it as the digest beside a byte count. 🟢 **The base's own
   files prove it is a commit:** `intel/open-gaps.md` cites *"`HEAD` `44925b867ce7`"* and
   *"at `44925b867ce7`"*, and `repos/trending.md`'s third row correctly renders it as
   **`main` · `44925b8`**. 🔴 A commit SHA and a payload digest are **not interchangeable**: the
   digest identifies the grant text, the commit identifies the tree. Publishing one as the other
   makes a licence cell unverifiable while *looking* verified.
2. **An off-by-one byte count.** Two rows carry **`1 083`** B; one carries **`1 084`**; the payload
   is **`1 084`**. 🟢 **The correct row existed on the same shelf as a wrong one** — so
   `gate-shelf-consistency`'s question (*no slug may carry disagreeing licence cells across the
   live shelves*) had a standing answer here and nothing asked it.

🔴 **And this pass published the wrong pair first.** `Pattern AW` was drafted citing
*"`1 083` B `44925b867ce7`"*, copied straight from the carried cell — **the precise error class
`T125` and `T124` are about, committed while writing them up**, and caught only because the
hand-check re-read a payload it had already cited. 🟢 Corrected before the commit. 🔵 **Fourth
consecutive pass in which the corpus held what the pass got wrong** (`p423`, `p424`, `T124`, now
`T126`) — and the first in which the pass caught *itself* rather than being caught by a gate, which
is the only reason it is in this section rather than in a successor's.

🟢 **The rule this earns:** a licence cell needs **byte count + digest + the SHA the payload was
read at**, in three separate columns, and a bare hex string in a digest column must be
**re-read, never copied**. 🔴 `Gap 425-E` registers the remaining exposure: these shelves hold
**unknown** numbers of hex values in digest columns that are commit SHAs, and this one was found by
accident while checking something else.

## 🆕 `p424` · 2026-10-24 — **`Gap 298` IS REFUTED, AND IT WAS NEVER A SUPPLY FACT. 🟢 `OpenOLAT/OpenOLAT` — a university-grade LMS these shelves have carried as a MENTION for nine passes — is **Apache-2.0** in its own payload at its own SHA. 🔴 The gap stood on an UNREAD PAYLOAD, not on an absent one, and `ACTION p422-A` had already named the exact read that would close it. 🟢 Plus `T121`: three slugs, one root commit, one byte-identical licence digest — and OPPOSITE statuses.**

🟢 **Gates ran FIRST** (`p412`'s standing rule), against `p423`'s commit `3009a89`, **before** this
pass's first capability leg: **`make hooks` 54 / 55 green**, the single red being the declared
`gate-census-union` (`Gap 400-B`), and **`make commit-gates` exits `0`** over its 54 blocking
gates. 🔵 So `p423`'s closing claim reproduces exactly on this host, and this pass started from a
measured baseline rather than an assumed one.
🔵 **No date straddle:** every leg, `ls-remote`, SHA read, payload digest and gate run happened
**2026-10-24**; the commit lands **2026-10-24**.
🟡 **Declared, because the rule is worth more than the appearance of keeping it:** two orientation
legs (the generic ranking leg and the trending leg) ran **before** the gate suite finished. They
produced **no graded cell** — every address written below was read after the gates were green —
but `p412`'s rule says *first*, and "first for the legs that matter" is not what it says.
`Gap 424-A`.

**What this pass established, first-hand:**

- 🟢 **`T122` — `Gap 298` IS REFUTED. There IS a permissive education platform, and it is a
  serious one.** [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) carries **Apache-2.0**
  at `LICENSE` @ `d073ad444fe5`, **`10 982` B `6dbc5b605ed0`**. The body is the canonical Apache
  2.0 text — diffed against `apache.org/licenses/LICENSE-2.0.txt` (`11 358` B) and agreeing on
  every term — with the **`APPENDIX: How to apply` boilerplate absent** (`grep -c APPENDIX` → `0`,
  which is the whole `376`-byte difference) and two **attribution** statements appended for the
  `olat.org` and `openolat.org` code bases. 🔵 Attribution, not restriction: neither statement
  adds a condition, and the grant is unmodified.
- 🟢 **Corroborated on two further channels, in the order `p289` requires — payload first, then
  corroboration.** `NOTICE.TXT` @ the same SHA (**`14 712` B `572140fc1b71`**) opens
  *"Licensed under the Apache License, Version 2.0"*; the `README.md` carries an Apache-2.0 badge
  and a `## Licensing` section pointing at both files. 🔵 **31** heads, tags through
  `OpenOlat_20.0.pre2`.
- 🔴 **And THAT is the finding, not the licence.** `Gap 298` has been published as a supply
  absence — *"no permissive education platform anywhere on these shelves"* — and was confirmed on
  a **ninth** channel as recently as `p423`. 🔴 **Every one of those confirmations was a
  restatement, and the refutation was one `curl` away the whole time.** `p422` saw it exactly:
  it refused the blog's Apache-2.0 claim under `p289` (correctly — a blog is not a grade) and
  registered **`ACTION p422-A`** to read the payload. The action was carried, not spent, and the
  gap outlived it by two passes. 🟡 `Gap 424-B`: this base has an instrument for an absence its
  own index refutes (`gate-absence`) and none for an absence **an unread payload would refute**.
- 🟢 **`ACTION p422-A` is discharged, both halves.** [`formalms/formalms`](https://github.com/formalms/formalms)
  @ `446a77a9b9cb` is 🔴 **GPL-2.0**, payload at **`html/license.txt`**, **`18 346` B
  `4e63feff285d`**. 🟢 So `p422` was right to refuse the Apache-2.0 claim, and the serving
  channel's own disclosure — *"other sources grade it `GPL` or `LGPL`"* — resolves to **GPL-2.0**
  on the payload.
- 🔴 **`T123` — AND THIS PASS GOT IT WRONG FIRST, which is the half worth publishing.** `p424`
  ran the **root** ladder — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENSE.TXT`, `COPYING`,
  `COPYING.txt`, `LICENSE.GPL`, `license.txt`, `LICENSE.rst`, `docs/LICENSE`, `lib/LICENSE`,
  `gpl.txt`, `GPL.txt`, `COPYRIGHT`, **14 paths, 14 × `404`** — and wrote *"no grant payload at
  any ladder path"* into four files. 🔴 **`gate-enumeration` reddened on the post-write run and
  named the refutation: `html/license.txt`.** 🟢 This is `p382`'s `gate-subtree-grant` class
  exactly — *a grant has SUBTREES, and a root-only read is wrong about the repository* — and this
  base **already had the instrument**. 🔵 `T120`'s shape, turned on this pass: the corpus held
  the rule, the pass did not apply it, and only a gate stopped it reaching the shelves.
- 🟡 **The Apache string in that README is still only a web-server requirement**, and still the
  most plausible origin of the circulating claim: the **only** occurrence of `Apache` in
  `README.md` is line 21, **`- Apache (recommended) with mod_rewrite enabled`**. 🔴 But that is
  now an **inference about how a false claim spread**, not a finding about an absent grant — the
  grant exists and is GPL-2.0. `Gap 424-C` records the downgrade.
- 🔴 **`Gap 298` is NOT weakened by this.** `formalms` joins the copyleft side of the tier, which
  makes the permissive count **1 of 10**, not 1 of 9.
- 🟢 **`T121` — one root commit, one licence digest, OPPOSITE statuses.** Three `canvas-mcp`
  slugs all carry `LICENSE` **`1 071` B `5385a26e2fac`** — byte-identical to the digest `p422`
  recorded for `vishalsachdev/canvas-mcp` — and all three share the **same root commit**
  `afe32c3e1721` (2025-02-27). 🔴 **A shared digest and a shared root say "one family"; they say
  nothing about whether an address is worth citing**, and measured against upstream `main` the two
  new slugs are opposites: `Harikeshav-R/canvas-mcp` is **0 ahead / 63 behind** — a stale mirror
  with no original commit — while `KKazuhaK/canvas-mcp` is **283 ahead / 96 behind**, of which
  **257** are its own non-merge commits under a **single** author key (`%ae`). 🔵 Neither is
  shelved: a mirror adds nothing, and a 257-commit single-author divergence from a live upstream
  is a **maintenance liability**, not a foundation. The upstream keeps the row.
- 🟢 **The Moodle tier gets its first graded address, and it is four days old.**
  [`duck-5/moodle-mcp`](https://github.com/duck-5/moodle-mcp) is 🟢 **MIT**, `LICENSE` **`1 072` B
  `64dc9680d3bb`** @ `dd9682ca97e3` — a **distinct** payload from the Canvas line's
  `5385a26e2fac`, so this is not that family under another name. **17** commits, **2026-10-20 →
  2026-10-21**, **2** author keys (`%ae`), 2 heads.
- 🔵 **`T114` extends from Canvas to Moodle on first evidence.** `p422` measured the MCP-over-LMS
  agent layer at **9 of 10 MIT** across the **Canvas** line; the first **Moodle**-line address
  read at a SHA here is also MIT. 🟡 One address is not a tier — this is a **second data point on
  `T114`**, exactly as `p423`'s single BSL-1.1 SIS address was a boundary rather than a
  refutation.
- 🔴 **One refusal, stated rather than padded.** `ArbaazAli1209/eduadapt-aiml-project` is 🟢
  genuinely **MIT** (`1 074` B `53264a4cc83f` @ `b5b9eb626ad7`) and on-topic — BKT in NumPy with
  an open-weights quiz generator — but it is **4 commits, 2026-10-11 → 2026-10-15, 2 author keys (`%ae`)
  resolving to one person**. 🔴 `p423`'s `ckz/edu_data_mcp_server` class exactly. Below this
  shelf's bar; recorded so the refusal is visible.
- 🔵 **Tier 8 is unchanged in membership.** Ten legs returned **4** unshelved addresses and
  **1** shelf-worthy grant (`duck-5/moodle-mcp`, recorded on the trending shelf rather than
  promoted here on four days of history) — `T100`'s **eighth** confirmation that the ranking and
  trending vocabularies have stopped producing supply this base does not already hold.

### 🟢 The two addresses this pass promotes to the platform tier's permissive row

🔵 Read first-hand at their own SHAs on **2026-10-24**. The second row is the one that moves
`Gap 298`; the first is recorded because an engagement that can use one can usually use both.

| address | grant, read at the SHA | why it is citable |
|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** — `LICENSE` `10 982` B `6dbc5b605ed0` @ `d073ad444fe5`; `NOTICE.TXT` `14 712` B `572140fc1b71` agrees | 🟢 **The first permissive education PLATFORM on these shelves.** A full LMS — assessment, course management, portfolio, video — under a grant that permits a commercial fork with no distribution trigger. 🔵 Swiss-origin (frentix GmbH, from the University of Zurich's OLAT), **EMEA**, 31 heads, tags through `OpenOlat_20.0.pre2` |
| [`duck-5/moodle-mcp`](https://github.com/duck-5/moodle-mcp) | 🟢 **MIT** — `LICENSE` `1 072` B `64dc9680d3bb` @ `dd9682ca97e3` | 🟢 **The Moodle line's first graded MCP address**, extending `T114` off the Canvas family. 🔴 **17 commits over two days** — cite as a reference architecture, never as a dependency |

🔴 **What this table is not.** `OpenOLAT` is promoted on its **grant**, read today. Its *depth* is
long-established and its *currency* is visible in its tag set, but this pass did not re-measure
its commit history, so no claim is made here about release cadence. 🟡 `ACTION p424-A` carries
that measurement.

## 🆕 `p423` · 2026-10-24 — **This pass adds NO row to this shelf, and that is the finding: the single new SIS-tier agent the capability leg returned is published as MIT by its npm registry entry, by a third-party MCP directory AND by its own in-repo manifest, and its only grant payload is Business Source License 1.1. 🔴 The conflict ships INSIDE the npm tarball, byte-identical to the repo payload. 🟢 And `p422`'s correct casing is vindicated against the gate that reddened it — then the fix turned out to exist already, in an instrument this base has kept in no `make` target since `p439`, which on being wired immediately found one repository cited under two spellings on THIS shelf.**

🟢 **Gates ran FIRST, and this time against a commit nobody had measured.** `make hooks`
completed against `p422`'s commit `82235af` **before** this pass's first research leg, which is
`p412`'s standing rule: **47 / 53 green, 6 red.** 🔵 `p422` declared its own suite un-run — the
host's auto-mode classifier refused to execute code from the clone — and honoured every file
contract **by hand**. 🟢 **On this host the suite ran with no refusal at all**, so "declared
un-run" must never be read as "un-runnable": that refusal is a property of a session, not of this
repository. 🔴 **The hand-honoured contract held on 47 gates and failed on five.** Evidence:
[`p423-gate-cost.2026-10-24-p423.tsv`](../evidence/p423-gate-cost.2026-10-24-p423.tsv).
🔵 **No date straddle:** every leg, `ls-remote`, SHA read, digest and gate run happened
**2026-10-24**; the commit lands **2026-10-24**.

**What this pass established, first-hand:**

- 🔴 **`T117` — a package can declare MIT on every metadata channel and ship a non-open-source
  grant, and the conflict travels in the artifact.** `tixuz/openemis-mcp` — an MCP server over
  **OpenEMIS**, UNESCO/KORDIT's school MIS — is listed as MIT by its npm registry metadata, by the
  MCP directory that surfaced it, and by **its own `package.json` in the same tree at the same
  SHA**. Its only grant payload is **Business Source License 1.1**, `647` B `4dead97d8aaf`, at
  `LICENSE.md` @ `f88a80fc1d5b`. The whole ladder — `LICENSE`, `LICENSE.txt`, `LICENSE.TXT`,
  `LICENSE-MIT`, `LICENSE-APACHE`, `COPYING` — is `404` at that SHA. **There is no MIT payload in
  the tree.** 🔴 And `npm openemis-mcp@1.2.0` ships `package/LICENSE.md` at the **same 647 B /
  `4dead97d8aaf`** beside a `package.json` reading `"license": "MIT"`, so `npm i` installs the
  contradiction. **Not recommendable, and not on this shelf.**
- 🔴 **The BSL names a DIFFERENT WORK than the repository it sits in.** `Licensed Work:
  openemis-mcp-pro`, where the repo and the package are both `openemis-mcp`. Additional Use Grant:
  *non-production evaluation and internal testing only*. `Change Date: 2029-01-01`,
  `Change License: MIT`. 🔵 So even read charitably — a "pro" edition's licence left at the root of
  the free edition — the address cannot be graded permissive by any channel this base trusts, and
  read literally it forbids exactly the commercial embedding an engagement would do.
- 🟢 **It is not a late re-licensing.** `LICENSE.md` entered in the **first commit**
  (`148c0bc`, 2026-04-19, *"Initial release: openemis-mcp v1.0.0 — free read-only MCP for
  OpenEMIS"*) and has never been modified. **32** commits, **4** authors (`%ae`), 2026-04-19 →
  2026-06-16, every commit at **`+0300`** (🟢 EMEA; `+0300` carries no DST in the Moscow/Istanbul
  band, so the placement does not rest on a DST assumption — `gate-offset-region`).
- 🟢 **`T118` — `p422`'s permissive-agent-layer thesis does NOT extend to the SIS tier on this
  evidence, and the one address that tested it is the counter-example.** `p422` measured 9 of 10
  MCP-over-**LMS** addresses MIT. The first MCP-over-**SIS** address read at its SHA is BSL-1.1.
  🔵 One address is not a tier, which is why this is registered as a boundary on `T114` rather
  than a refutation of it.
- 🟢 **`T116` re-tested: `p419`'s branch-grant hazard still does not fire.** `openemis-mcp` ref
  `openemis-core-5.10.0-update` (`e14c514598d4`) carries the **same** `647` B `4dead97d8aaf`
  payload as `main`. Counter advances **32 → 34** `(slug, ref)` pairs, **0** hits.
- 🟢 **`T106` re-calibrated on this host before anything was graded.**
  `Mattlo0546/canvas-mcp` `LICENSE` at SHA `b6c26ba` reproduced **`1 067` B `13c8ad755224`**
  exactly — the figure `p422` published — so the measurement channel is sound and the gradings
  below are not resting on an unverified instrument.
- 🔴 **`T119` — PRECEDENCE IS NOT AUTHORITY, and `gate-fold-identity` had only precedence.** The
  gate reddened on `Mattlo0546/canvas-mcp` across three shelves as a "new casing" against
  `p370`'s lower-case row. 🟢 **Resolved first-hand: GitHub's canonical display form is
  `Mattlo0546`** — title and breadcrumb — the lower-case form appearing only inside URLs, which
  are case-insensitive. **So `p422` wrote the correct casing and the gate was pointing at the
  wrong row.** A precedence-only gate does not merely miss that: it **demands every later pass
  reproduce the error**. 🟢 Fixed by an authority register, not by reverting the correct row
  (`Gap 423-C`, and the register is
  [`p423-canonical-casing.tsv`](../evidence/p423-canonical-casing.tsv)).
- 🔴 **`T120` — AND THIS PASS BUILT SOMETHING THE CORPUS ALREADY HELD, which is `T109`'s class
  turned on the pass itself.** `p439-case-collision-gate` had already written the
  canonical-resolution channel order down — **registry homepage, then the repository's own
  self-link, then a recorded majority decision** — and has been in **no `make` target since
  `p439`**. `p423` built its casing arm without it and found it only afterwards, while
  discharging `ACTION p421-A`. 🔴 **So `Gap 421-A` is not untidiness: an instrument in no target
  is invisible, and the invisibility CAUSED the duplication.** 🟢 `p421`'s
  `gate-action-answered` was built to stop a pass *delivering an action* the corpus answers; it
  does not grade a pass *building* what the corpus holds, and that is the hole this instance
  exposes.
- 🟢 **`p439` is WIRED as of this pass — and on its first run inside a target it found a live
  defect on this very shelf.** `RohanMuppa/brightspace-mcp-server` was cited **both ways**:
  upper case at `agents/top.md` ×3 and `repos/foundations.md`, lower case at `agents/top.md` ×3
  and `verticals/solutions.md` — **one repository under two spellings on the recommendation
  shelves**, which `gate-identity` exists to prevent and does not catch on casing. 🟢 Resolved by
  `p439`'s **own channel 2** at SHA `4b3bc9bf3838` — the README self-links
  `github.com/RohanMuppa/brightspace-mcp-server` **×3** and `package.json` agrees — and the four
  lower-case citations are normalised. `p439` now reports **0 findings over 365** distinct
  case-insensitive slugs.
- 🟢 **`ACTION p421-A` DISCHARGED, with a sharper number than it asked for.** `compose/code/`
  holds **431** directories; **328** are named nowhere in the `Makefile`; **175** of those carry
  a `test_*.py` nothing runs; and 🔴 **15 of those describe themselves as a gate.**
  `gate-region-headings` (`p338`) and `action-gap-crosscheck` (`p421`) were instances 1 and 2 of
  that shape — this is the first time it has a **population**. 🟡 "Self-describes as a gate" is a
  text match, so those 15 are **candidates, not verdicts**; this pass claims the denominator and
  `ACTION p423-A` asks for the adjudication. Evidence:
  [`unwired-instruments.2026-10-24-p423.tsv`](../evidence/unwired-instruments.2026-10-24-p423.tsv).
- 🟡 **The leg's other unshelved address is real, permissive and below bar.**
  [`ckz/edu_data_mcp_server`](https://github.com/ckz/edu_data_mcp_server) — 🟢 **MIT** `LICENSE`
  `1 060` B `a21e3d63806c` @ `a3eb7e8f2e70`, 1 ref, **4** commits, 1 author (`%ae`), 2025-03-21 →
  2025-03-22. It wraps the Urban Institute education-data API: enrollment **statistics**, not
  student records, so it answers an SIS-worded leg without being an SIS agent.
  🔴 **REFUSED-BELOW-BAR** on age and surface, recorded so the refusal is explicit.
- 🔴 **`T100` confirmed a SEVENTH time, and `T113` again.** All four ranking- and trend-worded
  legs plus all four regional legs returned **0 unshelved**; the capability-worded legs returned
  **2 unshelved, 0 supply**. 🔵 This is the first pass where the entire unshelved set is disposed
  of by refusal on **two different grounds** — a licence conflict and a below-bar grade. Evidence:
  [`discovery-legs.2026-10-24-p423.tsv`](../evidence/discovery-legs.2026-10-24-p423.tsv).

### 🔴 The three channels that disagree about one address, stated as a table

| channel | what it says about `tixuz/openemis-mcp` | authority |
|---|---|---|
| grant payload at the SHA (`LICENSE.md` @ `f88a80fc1d5b`) | 🔴 **BSL-1.1**, `647` B `4dead97d8aaf`, `Licensed Work: openemis-mcp-pro` | 🟢 **this base's authority** (`p289`) |
| in-repo manifest at the same SHA (`package.json`) | 🟢 `"license": "MIT"` | 🔴 wrong, and it is the channel `gate-provenance` reads |
| npm registry metadata + the MCP directory that surfaced it | 🟢 MIT | 🔴 wrong, and it is the channel a client reads first |

🔴 **The ordering is the lesson.** This base already knew a *search result* can say MIT over a
copyleft payload (`p409`). `p423`'s instance is worse in the direction that matters: the
**manifest inside the repository** is the thing that is wrong, and `gate-provenance` (`p280`)
identifies a manifest by what it **declares**. On this address, obeyed literally, it would grade
BSL-1.1 code as MIT. `Gap 423-A`.

## 🆕 `p422` · 2026-10-24 — **The permissive arm of education open source EXISTS — and it is not the platform, it is the AGENT-FACING LAYER ON TOP of the platform. 🟢 Ten LMS MCP servers read at their own commit SHAs: NINE are MIT, one is ungranted. 🔴 And the discovery leg served a 683-commit-stale FORK as the canonical address, with the upstream's copyright line intact so a licence-only check cannot see it.**

🔴 **Gates did NOT run this pass** — `make hooks` executes code from this cloned repository and the
host's auto-mode classifier refused it (`[Code from External]`), the same refusal `p419` recorded.
🟢 `p412`'s standing rule is therefore **unmet and declared**, not skipped silently; every file
contract below was honoured by hand. `Gap 422-A` registers the un-run suite, second instance.
🔵 **No date straddle:** every leg, `ls-remote`, SHA read and digest ran **2026-10-24**; the commit
lands **2026-10-24**, so `updated:` carries one date.

**What this pass established, first-hand:**

- 🟢 **`T114` — a whole capability class whose grant profile is uniformly permissive, which this
  base has never recorded.** Ten MCP-over-LMS addresses, every grant read at its own commit SHA:
  **9 GRANTED, all MIT**, 1 ungranted. 🔴 **`Gap 298` is not refuted — it is QUALIFIED, and the
  qualification is the commercially useful part** (below).
- 🔴 **`T115` — the leg served a FORK as the canonical address.** `NelsonSpencer/canvas-mcp` and
  `vishalsachdev/canvas-mcp` share root commit `afe32c3e1721` and **414** commits; the served one
  holds **2** own commits against the upstream's **683**, and is a week staler. 🟢 Their `LICENSE`
  payloads are **byte-identical** (`1 071` B `5385a26e2fac`) **with the upstream's copyright line
  retained** — correct MIT behaviour, and exactly what makes the substitution invisible to a
  grant-only check.
- 🟢 **`T116` — `p419`'s branch-grant hazard tested on a new class and it does NOT fire.** **32**
  `(slug, ref)` pairs across the three multi-head repositories (10 + 16 + 6 heads); **every head
  carries `LICENSE`, byte-identical within each repository**. The hazard stays rare.
- 🔴 **`T117` — this pass's improvised ladder was wrong by ONE BYTE, and caught itself.**
  `$(curl …)` strips the trailing newline: the same payload reads **1 068** B `453575e61c43`
  through command substitution and **1 069** B `72380798af61` through `curl -o file`. 🟢 **The
  canonical instruments are clean** — `p230`'s and `p211`'s ladders use the file channel, so no
  shelved digest is contaminated. `T108`'s class, sixth instance.
- 🟢 **`T100` holds a SEVENTH time and SHARPENS.** Both ranking legs and the two capability legs
  worded at capabilities this register has already exhausted (tutoring, essay grading) returned
  **zero** unshelved of ~40 addresses. The only productive leg was worded at a capability class
  the register had never enumerated: **3 unshelved of 15**. 🔵 **The discriminator is not
  "capability vocabulary" — it is an UN-ENUMERATED capability class.**

### 🆕 Tier 8 — the MCP-over-LMS class, every grant read at its own commit SHA on 2026-10-24

🔵 **Channel:** `git ls-remote --heads` for refs, `raw.githubusercontent.com/<slug>/<sha>/<path>`
for payloads. `api.github.com` and `github.com` HTML are **403** on this egress allowlist, so
**no star count was readable this pass** and none is written below — `p415`'s channel finding
holding a fifth time. 🟢 Bytes and digests are file-channel, per `T117`.

| address | grant, read at the SHA | heads | history | capability — band stated per cell |
|---|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** `LICENSE` `1 071` B `5385a26e2fac` @ `f4f0780` | 4 | **1 097** commits, 2025-02-27 → **2026-10-23** | 🟢 **The canonical upstream of the Canvas MCP line.** Student + educator tools with anonymisation tiers. 🔵 Already on these shelves (197 mentions) — `p422` establishes its position, not its existence |
| [`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp) | 🟢 **MIT** `LICENSE` `1 071` B `5385a26e2fac` @ `92b7fbc` — 🔴 **byte-identical to the row above, copyright line `2025 Vishal Sachdev` retained** | 16 | **416** commits, same root, **2 own / 683 behind**, last **2026-10-16** | 🔴 **A lagging fork the discovery leg served as the canonical address.** Do not pin it: the upstream carries 683 commits it does not have |
| [`javohir73/mcp-server-canvas-lms`](https://github.com/javohir73/mcp-server-canvas-lms) | 🟢 **MIT** `LICENSE` `1 069` B `72380798af61` @ `2472593` | 10 | **23** commits, 2026-08-14 → **2026-10-21** | 🆕 **Unshelved before this pass.** 🟢 **Strictly read-only** — stated in its own `README.md` read at the SHA, not from a snippet. Courses, grades, submissions, files |
| [`AnonymousOnyx22/canvas-lms-student-mcp`](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp) | 🟢 **MIT** `LICENSE` `1 072` B `ed912ca72d9e` @ `29c6baa` | 1 | **41** commits, 2026-10-14 → **2026-10-23** | 🟡 Read-only Canvas: due dates, grades, missing work, announcements. Band `reported` — the read-only claim is the repository's own description, not read from code |
| [`AnonymousOnyx22/moodle-student-mcp`](https://github.com/AnonymousOnyx22/moodle-student-mcp) | 🟢 **MIT** `LICENSE` `1 072` B `ed912ca72d9e` @ `23cdf92` — 🔵 **byte-identical to the row above; same author, two repositories** | 1 | **49** commits, 2026-10-14 → **2026-10-23** | 🟡 Read-only Moodle through the **mobile web service**, which is the deployment precondition. Band `reported` |
| [`JohannsenLum/canvas-api-mcp`](https://github.com/JohannsenLum/canvas-api-mcp) | 🟢 **MIT** `LICENSE` `1 070` B `f01d2f81a436` @ `bd7ec03` | 1 | **79** commits, 2026-08-07 → **2026-08-15** | 🟡 16 curated student tools plus a gateway over the wider Canvas API. 🔴 **No commit in ~10 weeks** — the widest surface in the tier is also among the stalest |
| [`Mattlo0546/canvas-mcp`](https://github.com/Mattlo0546/canvas-mcp) | 🟢 **MIT** `LICENSE` `1 067` B `13c8ad755224` @ `b6c26ba` | 1 | **5** commits, 2026-10-19 → **2026-10-20** | 🟢 **The only one that avoids API tokens entirely — university SSO sign-in.** 🔴 **5 commits over two days**: an architecture to copy, not a dependency to take |
| [`mtgibbs/canvas-lms-mcp`](https://github.com/mtgibbs/canvas-lms-mcp) | 🟢 **MIT** `LICENSE` `1 064` B `6923a6b4bf1c` @ `9b7efdc` | 6 | **70** commits, 2026-01-13 → **2026-02-13** | 🟡 Grades, assignments, academic data. 🔴 **Dormant ~8 months** |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | 🟢 **MIT** `LICENSE` `1 063` B `2cf91ec5272f` @ `a65aefa` | 1 | **13** commits, 2026-03-16 → **2026-04-04** | 🔴 **NOT read-only** — its `README.md` at the SHA names `submit_assignment`, read first-hand. 🟢 Go, not Python, which is the only non-Python runtime in the tier. 🔴 Dormant ~6 months |
| [`DA0806/canvas-student-mcp`](https://github.com/DA0806/canvas-student-mcp) | 🔴 **UNGRANTED** @ `5d8ace9` — no payload at **10** licence paths, and **neither `package.json` nor `pyproject.toml` declares a licence** | 1 | **12** commits, 2026-09-15 → **2026-10-03** | 🆕 Unshelved before this pass, and 🔴 **unusable as-is**: FastMCP Canvas student server with no grant on any channel checked |

🔴 **Ten rows, ten real addresses, every one probed.** No row below is carried from a snippet
without a first-hand read of its grant.

### 🟢 What `Gap 298` actually says after this pass

🔴 **`Gap 298` — "education open source is overwhelmingly copyleft" — was measured on the PLATFORM
tier and is true there**: Moodle `GPL-3.0`, Open edX `AGPL-3.0`, Canvas `AGPL-3.0`, Sakai
`ECL-2.0`, OpenEduCat `LGPL-3.0`, `frappe/lms` `AGPL-3.0-or-later`. 🟢 **The INTEGRATION tier over
those same platforms is uniformly MIT — 9 of 9 granted addresses.**

🟢 **The studio consequence is concrete and it is a sell:** *you cannot ship a permissive fork of
the LMS, but you can ship the agent layer over it permissively, and that is the layer the client
is actually buying.* 🔵 The copyleft obligation attaches to the platform the client already runs;
the new code sits beside it, over a network API, under MIT.

### 🔴 Searched and NOT found — recorded so a successor does not re-spend the leg

🟢 **Five legs returned zero unshelved addresses**, which is why this is written down rather than
omitted: `top open source AI agents education 2026 github MIT`; `github trending education AI 2026
repositories`; `open source AI tutor agent github 2026 adaptive learning LLM`; `open source essay
grading agent rubric LLM github 2026 MIT license classroom`; `open source platform education LMS
SIS MIT Apache self-hosted 2026`. 🔵 Between them they served `OpenOLAT`, `formalms`, `frappe/lms`,
`OpenEduCat`, `RosarioSIS`, `Gibbon`, `autorubric`, `researchrubrics`, `inside-the-scorer`,
`essay-grader-llm`, `AssessmentAI`, `bandup`, `freelingo`, `OpenTutor`, `Learning-Agent-System`,
`adaptive-knowledge-graph` and `ai-agent-to-learn-faster-and-better` — **every one already on these
shelves.**

## 🆕 `p421` · 2026-10-24 — **The instrument for *"is this action already answered?"* has existed since pase 59, passes 16/16, and is in NO `make` target — and wiring it as-is would have bought NOTHING, because it reads a notation this register retired. 🔴 `ACTION p420-E` is the live specimen: both halves were already on these shelves. 🟢 `gate-action-answered` is BUILT, AMENDED THREE TIMES on measured false rates, and WIRED — 268 findings cut to 2, both of them the specimen.**

🟢 **Gates ran FIRST this pass, which `p412`'s standing rule asks and `p420` admitted breaking.**
`make hooks` completed against `p420`'s commit `d93ad76` **before** any research leg: **51 / 52
green**, the single red being `gate-census-union` control 24 — `Gap 400-B`, deliberately red since
`p398`. 🔵 **No date straddle:** every leg, `ls-remote`, SHA read, payload digest and gate run
happened **2026-10-24**; the commit lands **2026-10-24**, so `updated:` carries one date.

| # | finding |
|---|---|
| 1 | 🔴 **`compose/code/action-gap-crosscheck` is in no `make` target at all.** `grep -n action-gap-crosscheck Makefile` → **nothing**, for ~360 passes since pase 59. Its stated purpose is this base's exact blind spot — *«que ninguna acción entregada esté ya contestada por el propio corpus»* — and its own suite still passes **16 / 16**. 🟢 This is `gate-region-headings`' class (`p338`/`ACTION ZP`: *"the gate existed with a passing suite … and was in no target, so `make hooks` never judged this file at all"*), and it is the **second** instance on this base |
| 2 | 🔴 **And wiring it as-is would have bought NOTHING, which is the harder half.** Run over the live corpus it reports `gap citations inside action blocks : 0`. It is calibrated to the **retired** Spanish-era ledger notation and the register has moved on all three channels it reads: the action-block heading (`^## … acciones que el pase N deja escritas` vs `### 🟢 Actions`), the gap-citation shape (`gap 51` vs `Gap 420-C`), and the closure vocabulary (`CERRADO` vs `### 🟢 Closed this pass`). 🔴 **A gate whose denominator is zero is green for the same reason a correct one is green** — `gate-backlog-denominator`'s class |
| 3 | 🟢 **`T109` — the specimen, and it is `ACTION p420-E` itself.** It asked a successor to *"resolve first-hand whether any Open edX component or Sakai is Apache-2.0"*, citing `p289`. 🔴 **Both halves were already on these shelves when it was written:** `verticals/solutions.md` carries `\| **Sakai** \| 🟡 **ECL-2.0**` and `\| **Open edX** \| AGPL-3.0`, and `compose/patterns.md` has carried the Apache-2.0 Open edX component since **`p390`**. 🔵 This is the third consecutive pass to find a prescribed action mis-specified rather than open — `p420` amended `ACTION p419-A`, `p421` answers `p420-E` from the base's own files |
| 4 | 🟢 **Re-read first-hand anyway at the commit SHA (`T106`), because `p289` is right even when the answer is already shelved.** [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) → **ECL-2.0**, `11 120` B, `sha256₁₂ 0688f62d04f1`, `LICENSE` at SHA `c35e7a2` on `master`. 🔴 **NOT Apache-2.0:** the sources calling it *"Apache-derived"* describe **lineage**, not the grant. 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) and [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) → **Apache-2.0**, `11 358` B, `cfc7749b96f6`, at `c73c4bb` and `e61f9d2` — **byte-identical to each other**, so this is a digest identity and not a `T101` length collision |
| 5 | 🔴 **`T110` — the grant was reachable only at an UPPERCASE extension, and the repository's own README cites a path that 404s.** `openedx/XBlock`'s grant is at **`LICENSE.TXT`**; `LICENSE.txt`, `LICENSE.Txt`, `license.TXT` and `LICENSE` **all `404`** at the same SHA, and the README links `LICENSE.txt` by name. 🟢 Only `pyproject.toml` names the real path — `license = "Apache-2.0"`, `license-files = ["LICENSE.TXT"]`. 🔴 **`p401-C` recorded *"one live repository was lost to a lowercase letter"*; this is the same defect inverted**, and this pass's improvised ladder reproduced it — `T108`'s **fifth** instance. 🟢 The base's OWN ladder vocabulary has carried `LICENSE.TXT` since `p211`/`p256` |
| 6 | 🟢 **`gate-action-answered` BUILT, AMENDED THREE TIMES AND WIRED into `HOOK_GATES` — in-pass, not registered.** 29 controls, 29 pass. 🔴 **The first draft reported 268 findings over 103 action blocks** — the 99 %-false shape `p420` refused to ship for `ACTION p419-A`. Three measured defects: a bare `owner/repo` regex admitted **this base's own shelf paths** as addresses (see 7); a clause citing a *second* action was graded as if that action had been delivered; and a licence **token** fired on the word *"granted"* inside a fixture list. 🟢 **268 → 13 → 12 → 2**, and the two survivors are both `ACTION p420-E`, over a denominator of **551** delivered actions. Zero false positives corpus-wide, pinned as the **RATCHET** |
| 7 | 🟡 **`T111` — `p351`'s shape rule calls four of this base's five shelf paths candidate addresses, and the fifth is rejected by coincidence.** `classify()` returns `None` (*may be an address*) for `agents/top.md`, `intel/open-gaps.md`, `compose/patterns.md` and `verticals/solutions.md`; `repos/foundations.md` is rejected **only because GitHub happens to use `repos` as one of its own namespaces**. 🟢 **LATENT on both live channels, measured rather than assumed:** `p348`'s `slugs_in` anchors on `github.com/` so the census never feeds it a shelf path (`make address-shape-census` → zero shelf filenames), and `p367`'s channel B, which *does* harvest backticked tokens, returns 2 survivors and admits **zero**. 🔴 **It went live the moment `p421` fed `classify` a third channel** — a register clause — which is how it was found |
| 8 | 🔴 **`ACTION p420-C` is ANSWERED BY REFUSAL, and the action was mis-specified.** It asked to run `gate-slug-oracle` against the 8 `Gap 420-C` addresses *"and record each as absent or private."* 🟢 **Run — calibrated control pair green (`moodle/moodle` → `EXISTS-PUBLIC`, a bogus org → the refusal signature) — all 8 return `ABSENT-OR-PRIVATE`.** 🔴 **The instrument's own header says the distinction the action asked for does not exist on this channel:** *"this channel cannot separate a missing repository from a private one."* 🟢 **The gain is real but smaller than prescribed:** an un-calibrated exit `128` becomes a calibrated verdict with transport confirmed. 🟢 **And the consequence is clean:** all 8 are carried **as unreadable or dead**, none recommended, so `gate-dead-citation` holds |
| 9 | 🟢 **`ACTION p420-D` executed with this base's own instrument, and the result inverts its framing.** `forkdir.sh` (`p404`) over full clones: [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) **continues** [`Pranjulcr7/OpenTutor`](https://github.com/Pranjulcr7/OpenTutor) — `SUPERSET`, direction `b`, **193** shared commits, **189** shared trees, `b_contains_a_head` **True**. 🔴 **`T112`: the continuation holds FOUR FEWER commits than the side it continues** — 206 against 210 across all refs — so a commit **count** names the wrong side while ancestry names the right one. One family, one citable unit (`p405`) |
| 10 | 🔴 **Supply this pass is ZERO, and it is a measured zero rather than a thin leg.** The capability leg returned **5** unshelved in-domain addresses; **all 5 are UNGRANTED** on a 15-path ladder at their own SHAs, with **no `license` field in any manifest** (`requirements.txt` ×4, `pyproject.toml` ×1). An ungranted repository cannot be evaluated, let alone built on (`p289`, `gate-payload-pin`). 🟢 **`T113`: an unshelved COUNT is not a supply count** |
| 11 | 🟢 **And the five are NOT one artefact, which refutes this pass's own first hypothesis.** They share an example topic (*"Intro to RAG"*), so `p421` predicted a fork or content-copy class and graded three pairs by full history: **all three `INDEPENDENT` — 0 shared commits AND 0 shared trees.** 🔴 **So the duplication is convergent, at the level of PROSE and TOPIC, and no history instrument on this base can see it.** 2–5 commits each |
| 12 | 🟢 **`T100` holds a SIXTH consecutive time.** The two ranking-worded legs returned **zero** unshelved in-domain addresses — all seven addresses they produced (`HKUDS/DeepTutor`, `Open-TutorAi/open-tutor-ai-CE`, `samrathreddy/Tutor-multi-ai-agent`, `TovTechOrg/Tov-learn`, `HugeCatLab/ChatTutor`, `ashishpatel26/500-AI-Agents-Projects`, `GarethManning/education-agent-skills`) are already carried. 🟢 **Including DeepTutor at `v1.6.15`, released 2026-10-19 — the figure `p415` already recorded first-hand, at `42.3k★`** |
| 13 | 🔵 **Regional legs: four for four returned material, none a nil — and two carry DATE CONFLICTS this pass refuses to resolve by preference.** 🟢 **`ACTION SH` did not fire for EMEA:** this pass's sources carry the AI Act education deferral to **2027-12-02** explicitly, so the counter advances to **nine** and `Gap 417-A` stays open. 🔴 **But APAC and LATAM each produced a conflict** — Vietnam's education grace period (`2027-03-01` + pre-`2026-08-15` grandfathering **vs** this base's carried `2027-09-01`) and Brazil's `PL 2338/2023` (Senate-approved **vs** ministries still consulting). Both registered, neither picked |

🟢 **Every figure above is reproducible from this pass's evidence store**, written the same day:
[`grant-at-sha.2026-10-24-p421.tsv`](../evidence/grant-at-sha.2026-10-24-p421.tsv) (10 addresses at
their SHAs) · [`p293-slug-oracle.2026-10-24-p421.tsv`](../evidence/p293-slug-oracle.2026-10-24-p421.tsv)
(the 8 `Gap 420-C` addresses with the calibration pair) ·
[`fork-lineage.2026-10-24-p421.tsv`](../evidence/fork-lineage.2026-10-24-p421.tsv) (4 pairs by full
history) · [`action-answered.2026-10-24-p421.tsv`](../evidence/action-answered.2026-10-24-p421.tsv)
(the gate's 2 findings) ·
[`crosscheck-blindness.2026-10-24-p421.tsv`](../evidence/crosscheck-blindness.2026-10-24-p421.tsv)
(why the pase-59 instrument reads nothing, channel by channel).

### 🔴 No new agent row this pass, and the zero is the finding

🔵 **Five unshelved addresses, zero rows.** Stated plainly because `p420`'s standing instruction is
that **fewer real rows always beat padding**, and an ungranted repository is not a row this base
may offer.

| address | read at SHA | why it is not a row |
|---|---|---|
| [`ShanmukaAlapati/Lesson-Writer-Agent`](https://github.com/ShanmukaAlapati/Lesson-Writer-Agent) | 🔴 **UNGRANTED** — 15 licence-shaped paths at `600f257` | Self-evaluating lesson generator, rubric-gated regeneration, multi-provider. 🔴 **5 commits, no grant, no `license` in `requirements.txt`** |
| [`Avinashhmavi/Self-Evaluating-Lesson-Content-Generator`](https://github.com/Avinashhmavi/Self-Evaluating-Lesson-Content-Generator) | 🔴 **UNGRANTED** at `4a43490` | Cross-family LLM grader over 12 hard pass/fail checks — the most interesting **design** of the five. 🔴 **3 commits, ungranted** |
| [`Subhradyuti/Lesson-Content-Generator`](https://github.com/Subhradyuti/Lesson-Content-Generator) | 🔴 **UNGRANTED** at `ef4bf9e` | 🔴 5 commits. `pyproject.toml` present and carries **no `license` field** |
| [`Shaik-Sam/rag-lesson-agent`](https://github.com/Shaik-Sam/rag-lesson-agent) | 🔴 **UNGRANTED** at `149c513` | 🔴 3 commits |
| [`rohan-9506/lesson-agent`](https://github.com/rohan-9506/lesson-agent) | 🔴 **UNGRANTED** at `fc0db44` | 🔴 **2 commits** |

🔴 **All five on default ref `main`**, all five with the same worked example, and **`INDEPENDENT`
from one another by full history**. 🟢 **What this base searched and did not find:** a permissive,
adopted, self-hostable **grading** agent beyond the two already shelved (`dsvi-b/corretor-enem`,
MIT, `p420`; `piyushdhoka/GradeU`, MIT on `main` only, `p419`). The capability vocabulary that
found those two returned no third this pass.

## 🆕 `p420` · 2026-10-24 — **The ref axis is POPULATION-WIDE and the hazard on it is RARE. 🟢 239 of 327 shelved addresses are multi-ref and 668 `(slug, ref)` pairs were probed first-hand; exactly ONE address is a genuine branch-grant hazard — the specimen `p419` already found. 🔴 `ACTION p419-A`'s gate, built as prescribed, would have fired 114 times to catch 2 real pairs. 🟢 AND the grant's PATH is a function of the REF: Moodle's grant is root `COPYING.txt` on `main` and `lang/en/docs/licence.html` on `MOODLE_13/14/15_STABLE`.**

🟢 **Gates RAN this pass, and that is the first thing a successor needs to know** — `p419` could not
execute them at all (`Gap 419-D`). `make hooks` completed: **48 / 52 green** against `p419`'s commit
`65afae9`. 🔴 **So `Gap 419-D` CLOSES, and `p419` is graded retrospectively** — see
`intel/open-gaps.md`. 🟢 **And this pass's own commit grades 51 / 52, the single red being `Gap 400-B`,
deliberately red since `p398`; all six census cells read MATCH after re-derivation.** 🔵 **Honest ordering note, against `p412`'s standing rule:** the four global
research legs ran **before** the gate suite this pass, not after. The rule was broken; it is recorded
rather than hidden, and nothing below depends on the ordering.
🔵 **No date straddle:** every leg, `ls-remote`, probe, payload read and digest ran **2026-10-24**;
the commit lands **2026-10-24**, so `updated:` carries one date.

| # | finding |
|---|---|
| 1 | 🟢 **The ref-axis population `Gap 419-A` left unmeasured is now MEASURED.** **338** addresses harvested fold-deduped from the four recommendation shelves; **327** resolve on `git ls-remote`; **239 of 327 (73.1 %) carry more than one branch**, 86 carry exactly one. 🔵 Default refs resolved first-hand for all 239: **`main` 156 · `master` 55 · `develop` 11 · `dev` 4 · `trunk` 2**, plus eleven singletons (`v4.0.x-develop`, `tcd`, `release_11`, `release`, `mobile`, `gh-pages`, `development`, `claude/eager-newton-boy1g0`, `2.2`, `2.12`, `#34282-…`) |
| 2 | 🔴 **And the hazard is rare, which is the opposite of what the population suggests.** **668** `(slug, ref)` pairs probed across **189** addresses (bounded at five non-default refs each, `master` and `HEAD` excluded because `Gap 419-B` makes a `200` there unfalsifiable). The base's own nine-path ladder returns **554 GRANTED / 114 UNGRANTED**. 🟢 **After calibration, ladder-deepening and mechanism adjudication, exactly 2 pairs on 1 address are genuine: `piyushdhoka/GradeU` `teacher` and `admin` — `p419`'s own specimen.** 🔴 **112 of 114 flags are false: 98.2 %** |
| 3 | 🔴 **`ACTION p419-A` is therefore AMENDED, not executed.** It prescribes extending `gate-subtree-grant`'s unit from `path` to `(ref, path)`. 🔴 **Built exactly as written, that gate is a 98 %-false-alarm instrument** and would bury the one real finding it exists to catch. 🟢 **The unit is `(ref, TREE)`, not `(ref, path)`** — and it needs the three admissions below before it is worth running |
| 4 | 🟢 **`T104` — a grant's PATH is a function of the REF, measured on one project across its own history.** [`moodle/moodle`](https://github.com/moodle/moodle) grants at root **`COPYING.txt`** on `main` (`200`; `LICENSE`, `license.txt`, `COPYING` all `404`) and at **`lang/en/docs/licence.html`** on `MOODLE_13_STABLE`, `MOODLE_14_STABLE` and `MOODLE_15_STABLE` — **`200` on all three** — with **no GPL boilerplate in `version.php`** on `1.5`, so the file-header channel is empty there too. 🔴 **A root-path read calls the three LTS refs of a GPL project ungranted.** 🔵 This is strictly past `p418` (*a grant has subtrees*) and `p419` (*a grant has branches*): **the path itself migrates** |
| 5 | 🔴 **`T105` — an `UNGRANTED` verdict on a ref is void without a POSITIVE CONTROL on that same ref.** **5 of the 114** are refs `git ls-remote` lists and `raw.githubusercontent.com` serves **nothing** at any of nine common paths: `aureuserp/aureuserp` `gh-pages`, `OS4ED/openSIS-Classic` `Version_8.0`, `projectfedena/fedena` `projectfedena-patch-1`, `Seechange-edu/act-ai-tutor-backend` `TNS-1616-…`, and `frappe/erpnext` **`#34282-Record-advance-payment-as-a-liability`**. 🟢 **The last one has a mechanism: a ref whose name begins with `#` cannot be probed over HTTP at all** — the fragment is stripped before the request leaves. 🔵 The other four are `Gap 420-B` |
| 6 | 🔴 **Two filenames account for most of the false alarm, and the base already learned one of them.** `COPYING.md` rescued **9** pairs (`jupyterhub/jupyterhub` `0.9.x`–`4.x`, `jupyter/nbgrader` `0.2.x`–`0.5.x`); lowercase **`license.txt`** rescued **5** (`frappe/erpnext`, `frappe/lms`, `frappe/education` on their defaults, `chamilo/chamilo-lms` `1.9.x` and `1.10.x`); `LICENSE.html` rescued **2** (`rstudio/learnr`, `jhudsl/ottrpal` `gh-pages`). 🔴 **`p401-C` already recorded that *"one live repository was lost to a lowercase letter"*** — and this pass's improvised ladder lost five more to the same letter |
| 7 | 🟢 **`T106` — probe the grant at the COMMIT SHA, the one channel no alias can satisfy.** Calibrated: a bogus 40-hex SHA → **`404`**; `GradeU` `main` `LICENSE` at `4ab0011…` → **`200`**. 🟢 **This is strictly stronger than `ACTION p419-B`'s remedy** (resolve the branch half on `ls-remote`): a SHA read needs no second channel and no trust in a ref name. 🔵 Every new grant below was read at its SHA, not at a ref |
| 8 | 🟢 **`T107` — a `gh-pages` ref is BUILT OUTPUT, not source, and its grant absence is not a licensing finding.** **6** of the 21 surviving pairs are `gh-pages`. Control on two of them: `index.html` → **`200`**, `package.json` → **`404`** (`rstudio/learnr`, `netless-io/flat`). 🔵 Also adjudicated out: **8** stale feature/asset branches (`inducer/relate` ×4 — `setup.py` declares `license="MIT"`; `tutors-sdk/tutors` ×3; `huggingface/agents-course` `UpdateDocTree`) and **3** Moodle LTS refs per `T104` |
| 9 | 🟡 **Two pairs survive as a real but low-consequence gap, and they are NOT GradeU's class.** [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) `release-2.6.0` and `release-2.7.0`: **no grant at 25 root paths**, and `package.json` resolves (`200`) with **no `license` field at all**. 🔵 The project is MIT on `main`; these are **release branches cut without the grant**, which matters only to an engagement that pins an old Sunbird release — and India/APAC engagements do |
| 10 | 🔴 **The default-ref arm of this audit found NOTHING the base did not already hold — and that is the pass's hardest lesson.** 19 addresses whose default ref returns no grant on a 15-path ladder were run through the deep ladder, the manifest channel, the README channel and the file-header channel. **Every single one this base carries was already graded correctly, several on BETTER channels than this pass's root ladder** — `gradescope/autograder_samples` (*"UNGRANTED AT ROOT"* with its two vendored copies named), `Nutlope/llamatutor` and `Daniel-ux1026/Tutor-Inteligente` (ungranted **by full tree enumeration**, 46 and 145 files), `x-cookie/agent` (*"ungranted on every arm"*), `bycs-lp/moodle-local_ai_manager` (*"GPL-3.0-or-later — granted in the source headers (`version.php`), no root licence file"*), `TecFancy/dsh-deeptutor` + `nanobpm/nano-ide` (*"manifest-only grants, `Pattern L` class 3"*), `marcusgreen/moodle-tool_aiconnect` (`401-C`). 🟢 **`gate-absence` exists for exactly this, and it fired on `p419`'s prose while `p419` was live** (`Gap 420-A`; 🟡 green again now that `p420` is the live section, which is a moved subject rather than a fix) |
| 11 | 🟢 **`T108` — an improvised instrument reproduces a defect the base already has a gate for. FOUR times in one pass.** The path ladder (`p283`/`p401-C`'s lowercase lesson) · the absence attribution (`gate-absence`/`T103`) · the address shape — **`OWNER/REPO`, `repos/CaviraOSS` and `repos/HKUDS` entered this pass's harvest**, the first a bare placeholder and the other two sliced out of an `api.github.com/repos/…` path, all three of which `gate-address-shape` (`p351`) rejects by construction · and slug existence (`p293`'s calibrated oracle, not run against the 8 addresses that returned exit `128` below). 🔴 **The pass's real lesson is to RUN this base's instruments, not to re-improvise them** |
| 12 | 🟡 **8 carried addresses did not resolve, and this run CANNOT call them dead.** `thanh01pmt/interactive-quiz-kit`, `AI-Matrix-Engine/aidream`, `Mckaroff/GraphLMS`, `santillana-ai/tutor-sdk`, `ale-alejandro/beadkit`, `yokowasis/autograder`, `e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp` — all **exit `128`** on `ls-remote` twice, without credentials. 🔴 **Un-credentialled `128` does not separate *absent* from *private***, which is precisely what `gate-slug-oracle` (`p293`) was built to do and this pass did not run against them — `Gap 420-C`. 🟢 **Separately CONFIRMED:** the two `EXISTS-NO-REFS` addresses `repos/foundations.md` names — `cdweaver1992/edfi-mcp-server` and `openfresno/edgenuity-aeries-grade-passback` — return **0 heads**, first-hand |
| 13 | 🟢 **Supply: 1 unshelved address worth a row, from 4 capability legs — and `T100` holds a FIFTH time.** The two ranking-worded legs (*"top open source AI agents education 2026"*, *"github trending education AI 2026"*) returned **zero** unshelved in-domain addresses for the fifth consecutive pass. The capability-worded legs returned **five** unshelved, of which one is supply. 🟢 **The discriminator is capability vocabulary, not recency vocabulary** |
| 14 | 🔵 **Regional legs: four for four RETURNED MATERIAL, none a nil.** 🟢 **`ACTION SH` did not fire** — this pass's EMEA sources carry the AI Act education deferral to **2027-12-02** explicitly; the counter holds at **eight** and `Gap 417-A` stays open. 🟢 **And an APAC source independently CONFIRMS `p417`'s correction of `p411`:** Vietnam's Law on AI **No. 134/2025/QH15** in force **2026-03-01**, with **education, health and finance extended to 2027-09-01**. 🔵 `T45` (school-level APAC rules) remains the informed gap: the leg returned national instruments and one cross-country survey, no school-level rules |

🟢 **Every figure above is reproducible from this pass's evidence store**, written the same day:
[`refaxis-census.2026-10-24-p420.tsv`](../evidence/refaxis-census.2026-10-24-p420.tsv) (338 addresses,
head counts and ref lists) · [`default-refs.2026-10-24-p420.tsv`](../evidence/default-refs.2026-10-24-p420.tsv)
(239 defaults) · [`grant-probe-9path.2026-10-24-p420.tsv`](../evidence/grant-probe-9path.2026-10-24-p420.tsv)
(668 pairs, the uncalibrated run **kept deliberately** so the 98.2 % false rate can be re-derived) ·
[`grant-calibrated.2026-10-24-p420.tsv`](../evidence/grant-calibrated.2026-10-24-p420.tsv) (the 114
negatives with their positive controls) ·
[`branchgrant-class-deep.2026-10-24-p420.tsv`](../evidence/branchgrant-class-deep.2026-10-24-p420.tsv) ·
[`defaultref-deep.2026-10-24-p420.tsv`](../evidence/defaultref-deep.2026-10-24-p420.tsv).

### 🆕 Tier 7 — the agent-agnostic grader, and it is LATAM

🟢 **One new row this pass, and it is a composition primitive this base has never shelved: a grading
methodology with no model, no API and no service.**

| agent | address | licence *(read at SHA `e3807a6`)* | ★ | what it is, and the boundary |
|---|---|---|---|---|
| **corretor-enem** | [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) | 🟢 **MIT** — `1 078` B, `sha256₁₂ 4e4fd8d68768`, *"Copyright (c) 2026 Davi Azevedo Pessanha"* | 6 | ENEM essay grader over the **five official competencies** (0–200 each, 0–1000 total), *"calibrado em 11.147 redações reais"* from the **Essay-BR** corpus, shipped as a local **SQLite `corpus.db`** with full-text search. 🟢 **`Sem API/ML`: it calls no model and vendors no SDK** — the methodology is markdown plus thin per-agent shims, and it *"roda dentro de qualquer coding agent (Claude Code, Codex, Cursor, Gemini, Aider…)"*. **Python 3.10+, stdlib `sqlite3` only.** 🟡 **Its own stated limits are the boundary:** the corpus is pre-2025, so competencies **C2, C4 and C5 drift**; it documents interrater variance and repertoire gaming, and calls its output an estimate, not an official grade. 🔵 **11 commits, single ref `master`** — young, and shelved for its shape, not its maturity. 🟢 **LATAM — Brazil** |

🔵 **Why it earns a row at 6 ★ when `p419` admitted `GradeU` at 3 ★ for a boundary.** A studio that
already runs coding agents can mount this **without deploying anything** — no inference cost, no
data egress, no model contract — and it is the first **LATAM-placed permissive** grading asset on
these shelves. 🔴 **It is not a foundation and not a service;** it is a rubric engine for an agent
the engagement already has.

### 🟡 Three capability sightings promoted to NOTHING, deliberately

🔵 Same disposition as `p417`'s two graders, and for the same reason: real code, no adoption.

| address | grant *(at SHA)* | why it is not supply |
|---|---|---|
| [`M0hamed0mar/adaptive-learning-agent`](https://github.com/M0hamed0mar/adaptive-learning-agent) | 🟢 MIT `1 069` B `d4f5fc21f1e1`, *"Copyright (c) 2026 Mohamed Omar"* | 🔴 **0 ★ and 2 commits.** LangGraph + FastAPI over Groq `qwen/qwen3.8-27b`, **eight** declared roles including critic→refiner loops; documents its own AWS ECS running cost at *"~$20/month"*. 🔵 Architecture worth reading, adoption worth nothing |
| [`VaishnaviSingh-Analyst/Learning-Agent-System`](https://github.com/VaishnaviSingh-Analyst/Learning-Agent-System) | 🟢 MIT `1 086` B `b29adecda524` | 🔴 **0 ★**, 37 commits. LangGraph + local Ollama `llama3.1`, **5-3-2** tiered checkpoints (5 MCQ / 3 short / 2 long), `THRESHOLD` 0.7, Feynman re-teach, Streamlit, HF `zephyr-7b-beta` fallback. 🟡 **The grant's holder is `springboardmentor123455-maker`, not the repository owner** — a holder line is a **provenance claim**, and a mentorship-programme origin is the obvious reading but **the README says nothing of the kind**, so the string is recorded and the inference refused |
| [`Shahzar07/Lesson-Planner-Ai`](https://github.com/Shahzar07/Lesson-Planner-Ai) | 🔴 **NONE** — 12 licence-shaped paths at SHA `69dc697`, and `package.json` carries **no `license` field** | 🔴 **Ungranted, so it cannot be evaluated, let alone built on.** 🟡 Its default ref is **`claude/dazzling-tesla-o8gpe6`** — an agent-generated session branch standing as the repository's default, the first such specimen on these shelves |

🟡 **One unshelved FORK CANDIDATE, recorded and not graded.**
[`Pranjulcr7/OpenTutor`](https://github.com/Pranjulcr7/OpenTutor) (12 heads, HEAD `a890519`) is a
second address for the project this base already carries as `zijinz456/OpenTutor` (11 heads, HEAD
`2d2c003`). 🔴 **Direction is NOT established** — `p404` requires full history for that and this pass
read ref sets only, the exact test `p404` recorded as insufficient. 🔵 Registered so a successor
grades it rather than re-finding it.

## 🆕 `p419` · 2026-10-24 — **A grant has BRANCHES, not only subtrees. 🔴 The one new agent address this pass ships three applications on three branches and the MIT payload exists on ONE of them. 🟢 And every ref this base publishes survives an authoritative sweep — 18 for 18 — which is what makes the channel finding latent rather than live.**

🔴 **Gates did NOT run this pass.** `p412`'s standing rule is *gates before the first research leg*;
`make hooks` executes code from this cloned repository and the host's auto-mode classifier refused
it (`[Code from External]`). 🟢 **Every gate contract below was honoured by hand** — `gate-tables`
(no row renders as a header), `gate-dates`, `gate-enumeration`, `gate-register-currency`
(`intel/open-gaps.md` written in **this** pass). 🔵 `Gap 419-D` registers the un-run suite:
**nothing on this page's `p419` section rests on a green gate.**
🔵 **No date straddle:** every leg, clone, probe and digest ran **2026-10-24**; the commit lands
**2026-10-24**.

| # | finding |
|---|---|
| 1 | 🟢 **One unshelved in-domain address — the first supply increment in four passes.** [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU): MIT on `main`, `1 065` B, `sha256₁₂ 10e6b9c80b1b`, HEAD `4ab0011` **2026-10-23 · 1 d**, 3 ★, 86 commits, root `d7b19e6` 2026-02-02, **not** a fork by `p395-A`'s root-commit arm |
| 2 | 🔴 **Its grant covers one third of its product.** The project is **one application per BRANCH** by its own `README.md:50-54`. `main` (Student site, 199 paths) carries `LICENSE`; **`teacher`** (Teacher studio, 55 paths) and **`admin`** (Admin portal, 43 paths) carry **no licence-shaped path at any depth** and **no `license` field in any manifest** — all three set `"private": true`. All three heads were committed **within eight minutes** on 2026-10-23 |
| 3 | 🔴 **`p382`'s `gate-subtree-grant` has the right subject and the wrong axis.** Its unit is a path inside one tree; here the ungranted code is on a **different ref**. The enumeration axis is `(ref × path)` and every instrument this base owns reads one ref — `Gap 419-A` |
| 4 | 🔴 **`raw.githubusercontent.com` ALIASES `master` and `HEAD` to the default branch even when no such ref exists.** Measured on `GradeU` (heads `main`/`admin`/`teacher`), `THU-MAIC/OpenMAIC` (`main` + 280) and `Gchism94/ai-tutor` (`main` only): all three return a **byte-identical `200`** at `master/LICENSE`. 🟢 Negative controls hold — `trunk` → `404`, `develop` → `404`, bogus ref → `404` (14 B, `d5558cd419c8`). 🟢 **The decisive control is a fourth repository whose default is NEITHER name:** `learningequality/kolibri` defaults to `develop`, and `master/LICENSE` → **`200`, `1 097` B `3c056b34a476`, byte-identical to `develop/LICENSE`**, while `main/LICENSE` → **`404`**. **The alias target is the default branch whatever it is called; the alias names are `master` and `HEAD` only** |
| 5 | 🔴 **So `p354`'s contract is unfalsifiable on that channel for the two most-assumed ref names.** *"A published grant path asserts a BRANCH and a FILE, and both must resolve"* — a `200` at `master/…` proves the file and says **nothing** about the branch. 🔴 **The asymmetry is directional:** `p418` closed `Gap 417-E` on a `main` → `404`, which is a **true** negative because `main` does not alias |
| 6 | 🔴 **And on `GradeU` the alias hides exactly this pass's finding.** `master/LICENSE` → MIT `200`, `admin/LICENSE` → `404`, `teacher/LICENSE` → `404`. An auditor asserting ref `master` reads one MIT grant and never reaches the two ungranted branches |
| 7 | 🟢 **The hazard is LATENT here, and that is measured.** All **18** `(slug, ref)` claims on the six live shelves were re-verified with `git ls-remote`, which no alias satisfies: **18 of 18 are real branches standing at `HEAD`** — nine at `master` (`henriquebotelhogomes/educacao`, `aureuserp/aureuserp`, `idurar/idurar-erp-crm`, `Loganxgreaves/blackboard-mcp`, `AI4Bharat/Anudesh-Backend`, `CAHLR/pyBKT`, `OpenOLAT/OpenOLAT`, `openfun/richie`, `OS4ED/openSIS-Classic`), five at `develop`, plus `tcd`, `2.2`, `2.12` |
| 8 | 🔴 **A refutation this pass BUILT and then WITHDREW, recorded rather than dropped.** A first extractor paired each ``ref `master` `` claim with the nearest slug in a ±6-line window and produced *six* apparent falsehoods. **All six were artefacts of the window.** These rows are single lines thousands of characters wide carrying many addresses: `agents/top.md:701`'s ``ref `master` `` belongs to `henriquebotelhogomes/educacao`, not to `portugol-ai-tutor` three addresses earlier on the same line. 🟢 **`T103`: a claim on these shelves is attributed by its SENTENCE, never by its line number** |
| 9 | 🟢 **`T101` gets its mechanism one pass after `T101`.** `GradeU` and `OpenMAIC` are **both exactly `1 065` B** with different digests, and `cmp` separates them at char 1. The equality is four deltas summing to zero: **+3** B extra blank lines, **−1** B missing terminal newline, **−2** B shorter holder (`GradeU` vs `THU-MAIC`). 🔴 **The collision is reachable by construction**, not coincidental |
| 10 | 🟢 **`T102`, and it explains a number `p418` corrected.** A line-based read of `GradeU`'s payload returns **`1 066`** B because line tools **re-add the terminal newline it lacks**. `p418` corrected a carried `1,066` to `1 065` on `OpenMAIC`. **Byte counts come from `wc -c` on raw bytes, never a line pipeline** |
| 11 | 🔴 **A manifest-only audit would call `GradeU` AI-free.** Inference is reached by raw `fetch` — `src/app/api/student/ai-tutor/route.ts:47` → `https://api.groq.com/openai/v1/chat/completions`, model `openai/gpt-oss-120b` — and **no AI SDK appears in `package.json`** (no `openai`, no `groq-sdk`, no `@ai-sdk/*`, no `ai`). 🟢 **A vendored-SDK absence is not a capability absence** |
| 12 | 🔵 **Supply legs: 1 unshelved of 8 on the capability leg, 0 of 11 on the two ranking legs.** `T100` confirmed a **fourth** time and sharpened — the discriminator is **capability vocabulary** (`tutor`, `grading`, `lesson planning`), not recency vocabulary (`top`, `trending`) |
| 13 | 🔵 **Regional legs: four for four CARRIED**, each stated as a placed nil, with every item grep-confirmed against `intel/market.md` / `intel/policy-matrix.tsv`. 🟢 **`ACTION SH` did not fire**; the counter holds at **eight** and `Gap 417-A` stays open |
| 14 | 🟢 **`p418`'s Africa / Middle East nil MOVES.** South Africa's draft National AI Policy (DCDT, **2026-04-10**) was **withdrawn 2026-04-26** by Minister Solly Malatsi because **≥10 % of its academic references were fictitious**, gazetted **2026-06-12** in its entirety. 🟡 Band `reported` — strongest channel reached is `sanews.gov.za`; the gazette text was **not** read because `en.wikipedia.org` is **off this environment's egress allowlist**, `p413`'s finding holding a fourth time |

### 🆕 Tier 6 — the branch-grant specimen

| agent | address | licence *(as measured, per branch)* | ★ | HEAD | what it is, and the boundary |
|---|---|---|---|---|---|
| **GradeU** | [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU) | 🟢 **MIT** on `main` only — `1 065` B `10e6b9c80b1b`. 🔴 **`teacher` and `admin`: UNGRANTED** (no payload, no manifest field) | 3 | `4ab0011` 2026-10-23 · 1 d | Learning platform in three branch-shipped apps: AI tutor (Groq `openai/gpt-oss-120b` over raw `fetch`), teacher-side course generation from a syllabus outline, in-browser proctoring (`@tensorflow-models/blazeface`, `ProctoringEngine.tsx`, `ProctoringLog.ts`), security/NLP labs, certificates. 🔴 **Only the student app is licensed.** 🟡 Four humans + 1 bot (`p412` rule), `"version": "0.0.0"`, and MongoDB (`mongoose`) still live beside Supabase mid-migration (`migrateLabsToSupabase.ts`) |

🔵 **Why it is admitted at all, with 3 ★.** It is the only new in-domain address in four passes; its
AI-tutor and proctoring capabilities are **real code**, not README claims; and it is this base's
**first specimen of the branch-grant class** — the reason it earns a row is the boundary, not the
star count. 🔴 **It is not a foundation and is not recommended as one.**

## 🆕 `p418` · 2026-10-24 — **This base's most-detailed agent row says `🟢 MIT` and the repository ships an `LGPL-3.0-or-later` subtree under exactly the capability the row recommends. 🟢 `THU-MAIC/OpenMAIC` has NINE grants, not one; eight are stock MIT and the ninth is the FSF's lesser licence. 🔴 AND `P564`'s byte-identity claim is refuted by a figure `p417` itself corrected and nobody connected back.**

🟢 **Gates ran before the first research leg** (`p412`'s standing rule): **50 / 51 green on arrival**,
the lone red `gate-census-union` control 24 — **`Gap 400-B`**, deliberately red since `p398`.
🔵 **No date straddle this pass:** every leg, probe, payload read and digest below was executed on
**2026-10-24** and the commit lands **2026-10-24**, so `updated:` is a single date rather than
`p417`'s split.

| # | finding |
|---|---|
| 1 | 🔴 **A root-only licence read is wrong about [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC), and this shelf's own row is the one that is wrong.** The repository carries **nine** `LICENSE` paths. **Eight** are byte-identical stock MIT — `1 065` B, `sha256₁₂ ba2525637432`, *"Copyright (c) 2026 THU-MAIC"* — at the root and in seven `packages/@openmaic/*` subtrees. 🔴 **The ninth, `packages/mathml2omml/LICENSE`, is `7 652` B, `sha256₁₂ e3a994d82e64`, titled *"GNU LESSER GENERAL PUBLIC LICENSE / Version 3, 29 June 2007"*, holder *"Copyright (C) 2007 Free Software Foundation, Inc."*** — **LGPL-3.0**, inside the repository this base presents as its flagship permissive APAC agent |
| 2 | 🟢 **The manifest AGREES with the subtree grant, which is what makes it a fact rather than a stray file.** `packages/mathml2omml/package.json` declares `"license": "LGPL-3.0-or-later"`, `"name": "mathml2omml"`, `"version": "0.5.0"`, `"author": "Johannes Wilm"`, upstream `git+https://github.com/fiduswriter/mathml2omml.git`. 🔵 So it is **vendored third-party code**, not THU-MAIC's own — and `-or-later` is the **wider** grant, which matters: the obligation is LGPL-3.0's, not a bare reference |
| 3 | 🔴 **And it is a DIRECT dependency of the shipped application, not an optional extra.** Root `package.json:118` declares `"mathml2omml": "workspace:*"`, and the root `build:packages` script builds it **first in the chain** (`cd packages/mathml2omml && npm run build && cd ../pptxgenjs && …`). **35** tracked paths sit under the LGPL subtree. 🔵 `packages/pptxgenjs/package.json` is the second vendored third-party and is **MIT** — so the monorepo is MIT + MIT + **LGPL-3.0-or-later**, three grants over two vendors |
| 4 | 🔴 **The LGPL subtree sits under the exact capability this shelf recommends the project FOR.** `mathml2omml` converts MathML to OMML — Office math — and the row below praises *"a PPTX that keeps every scene"* and *"export of a finished classroom as one offline HTML file"* as the reasons to reach for OpenMAIC over the larger `DeepTutor`. 🟢 **The recommendation survives; the licence cell behind it does not.** A studio pricing *"OpenMAIC, MIT, PPTX export"* is pricing a copyleft component as permissive, and it is the export path that carries it |
| 5 | 🟢 **`p382`'s gate is the one that names this, and it was never run against this address.** `gate-subtree-grant`'s subject is *"a grant has SUBTREES, and a root-only read is wrong about the repository"*; `p414` applied it to `education-agent-skills` and found a POINTER on both subtrees. 🔵 **Nothing applied it to the row this base cites most.** The instrument existed; the address it most needed was not in its input |
| 6 | 🔴 **The carried root figure is refuted by one byte, on two independent channels.** This shelf's row reads `1,066 B`; the payload is **`1 065` B** by blobless clone (`git cat-file -p HEAD:LICENSE`) **and** by `raw.githubusercontent.com`, both returning `sha256₁₂ ba2525637432`, against a calibrated control pair (`package.json` → `200`, `NO_SUCH_FILE_p418` → `404`) |
| 7 | 🔴 **`P564` is refuted — and the figure that refutes it was published by `p417`, on this same base, unconnected.** `P564` (`agents/trending.md:26534`) states `krayin/laravel-crm` and `aureuserp/aureuserp` ship a *"**byte-identical** 1 077 B MIT payload"*. Read first-hand today: **krayin `1 078` B `sha256₁₂ a76aa4a4405c`** (ref `2.2`, HEAD `5eecae0`, 2026-10-21) against **aureuserp `1 077` B `sha256₁₂ c6dca3b0db5b`** (ref `master`, HEAD `8f6e107`, 2026-10-23). 🔴 `cmp` → **they differ**, by exactly `aureuserp`'s missing terminal newline |
| 8 | 🟢 **`P564`'s CONCLUSION survives; its EVIDENCE does not — and the distinction is the finding.** *"One vendor, not two options"* is right, and the holder line is what establishes it: both read *"Copyright 2010-2025, Webkul Software"*. 🔴 But `p417` recorded krayin at **`1 078` B / `a76aa4a4405c`** (`README.md`, finding 11) — the correct figure — **in the very pass that declared `aureuserp` unresolvable**, so the base held the number that breaks `P564`'s identity claim and never compared them. 🟢 `T101`: **a `cmp`-identity claim is recorded with BOTH digests or it is not recorded** — a shared byte LENGTH is not identity, and `p312` already settled the adjacent case that a length is not a TEMPLATE |
| 9 | 🔵 **The one-byte class is live TWICE in one pass, which is why it earns a rule rather than a note.** The Webkul pair differs by a terminal newline (`1 077` vs `1 078`); this shelf's OpenMAIC cell differs from the payload by the same magnitude (`1,066` vs `1 065`). 🟢 **And the `1 077` B MIT band is crowded**: these shelves already carry four *different* digests at that exact length — `0eeb9d32caed` (`oak-curriculum-api`), `5e2f8f0fa782` (`knowledge-base-modrn-mind`), `d150aadcccd2` (`oak-ai-lesson-assistant`) and now `c6dca3b0db5b` (`aureuserp`). **A length cannot identify a payload on this base, demonstrably** |
| 10 | 🟢 **`Gap 417-E` CLOSED — and it closed from this file, 1 880 lines below the section that opened it.** `p417` recorded `aureus-erp/aureus` `main/LICENSE` → `404` and prescribed `ACTION p417-C` to *"resolve the real address or drop the row"*. 🔴 **The resolvable address was already on `agents/top.md:2330`** — `aureuserp/aureuserp` (MIT) — and again at `agents/trending.md:26550`. 🔴 `p417`'s row had **two** errors in one cell: the wrong slug **and** the wrong ref (it probed `main`; the real default is **`master`**). 🔵 `p416`'s standing suggestion is *"`grep -rF` the band a pass claims is empty"*, and `p417` prescribed a probe for a question its own base answered |
| 11 | 🟢 **`Gap 417-D` CLOSED, and the two halves of the claim have OPPOSITE answers.** `ACTION p417-B` asked for `exelearning/exelearning`'s export modules in-tree before any SCORM/xAPI claim. Read at HEAD `c848eca` (2026-10-23), **9 756** tracked paths: **774** match `/scorm/i`. SCORM 1.2 runtime (`public/app/common/scorm/scorm12/exe-scorm12-adapter.js`, `SCORM_API_wrapper.js`, `SCOFunctions.js`), a **SCORM 2004** contract suite (`scorm2004-contract.test.js`), the manifest generator `src/shared/export/generators/ImsManifest.ts`, and export fixtures carrying **`imscp_rootv1p1p2.xsd`** (SCORM 1.2 CP) beside **`imscp_v1p1.xsd`** (plain IMS CP). 🟢 **The secondary source was RIGHT and the repository PAGE was incomplete** — the inverse of this base's usual failure |
| 12 | 🔴 **But xAPI is RETIRED, by the project's own decision record.** `doc/architecture/adr/ADR-2302-02-xapi-retirement.md`. 🟢 `p417` bundled *"SCORM/xAPI"* as one capability claim; **SCORM is shipped and xAPI was removed on purpose**, so the bundle could only ever have been half-true. 🔵 **And it does NOT give a second *permissive* SCORM emitter** — `exelearning` is **AGPL-3.0**, so `p416`'s closure of the permissive-SCORM scarcity still rests on `Papermorph` alone |
| 13 | 🟢 **`ACTION p417-D` BUILT this pass rather than deferred.** [`compose/code/p418-register-currency-gate`](../compose/code/p418-register-currency-gate/) — **16 controls**, wired into `make hooks` as `gate-register-currency`. 🟢 **Validated against the real commits**: red at `4a53447` (`p414`, *stale by 1*), `1d3f173` (`p415`, *by 2*), `ea583bf` (`p416`, *by 3*), green at `20aa033` (`p417`). 🔵 It would have fired on **`p414`, the pass the drift began** — three passes before anyone noticed. `p412` answered the same failure with a warning and the warning did not hold (`P237`) |
| 14 | 🔵 **Eight prescribed legs run; the supply layer returned NIL unshelved.** `OpenMAIC` (41.3k★ MIT), `os-taxonomy`, `frappe/education`, `Gego-K12/gegok12`, `nanochat`, `developer-roadmap`, `Ebimsv/AITutorAgent`, `Gchism94/ai-tutor`, `mitodl/open-learning-ai-tutor`, `500-AI-Agents-Projects`, `OpenEduCat`, `RosarioSIS`, `openSIS`, `Fedena`, `ERPNext` — **every one already shelved, with hit counts**. 🟢 `T100` held: **the pass's value came from re-reading a verdict, not from another leg** |


## 🆕 `p417` · 2026-10-24 (reads 2026-10-23) — **`p411` graded a CORRECT source as carrying "the wrong Vietnamese date" — and the row's OWN QUOTED TEXT contains the clause that makes the source right. 🟢 Plus the first genuinely new state-backed EMEA supply in several passes: `exelearning/exelearning`, AGPL-3.0 at `p413`'s canonical digest, led by Spain's Ministry of Education. 🔴 AND the gap register is THREE passes stale.**

🔵 **Dating note, and this pass is the first in the run that has to SPLIT it.** Every search leg,
licence read, payload read, digest and gate run below was executed on **2026-10-23**; **the commit
lands 2026-10-24**, because the work crossed **00:00 UTC** before it was written out. 🟢 **The two
dates are therefore recorded separately rather than collapsed to one**, and the frontmatter
`updated:` field carries the **commit** date while every `evidence/*.tsv` filename carries the
**read** date — which is why they disagree by one day, deliberately. 🔵 `p395`–`p416` were all
dated **2026-10-23**, twenty-two passes; **this is the first pass dated 2026-10-24**, and the first
whose reads and commit fall on different days. 🔴 `p223`'s date gate is satisfied by the split, not
by rounding either date toward the other.

🟢 **Gates ran BEFORE the first research leg — `p412`'s standing rule, which `p416` admitted
breaking: 50 / 51 green on arrival**, equal to `p413`–`p416`. 🔵 The lone red is
`gate-census-union` control 24 — **`Gap 400-B`**, carried deliberately red since `p398`. `p387-G`
forbids closing it by weakening a control and this pass did not try.

🔵 **Channel note, in agreement with `p414`–`p416`.** `raw.githubusercontent.com` serves **`200`**
and is how every byte-level grant read below was taken; `github.com` HTML reads cleanly through
`WebFetch`. `p414`'s `AUTHZ-REFUSED` class holds a fourth consecutive pass.

### 🔴 Two unshelved education grading agents, both REAL, both UNGRANTED — and one carries an MIT badge over no payload

🟢 Ten discovery legs today returned **two** in-domain addresses this base had never recorded
(`savinoo`, `ai-grading-system`, `AssessmentAI`, `Fatima0923` — **0 hits each** across all eight
shelves and every `.tsv`). 🔴 **Neither can be built on.** Both exist; neither has a grant.

| Address | Grant, probed byte-level | Stars | What it is | Region |
|---|---|---|---|---|
| [`savinoo/ai-grading-system`](https://github.com/savinoo/ai-grading-system) | 🔴 **NONE.** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` on **both** `main` and `master` → **8 × `404`**. No sidebar licence entry. 🔴 **README badge claims `License-MIT-green`; README text says *"MIT — ver arquivo `LICENSE`"* — pointing at a file that does not exist** | **2** | Multi-agent grader for discursive exams: LangGraph + LangChain, FastAPI, PostgreSQL, ChromaDB, RAG, **conditional divergence arbitration**, Alembic, Docker Compose, Python 3.12+ | 🟢 **LATAM** — Instituto Federal Fluminense, Campos dos Goytacazes-RJ, **Brazil**; TCC capstone, April 2026 |
| [`Fatima0923/AssessmentAI`](https://github.com/Fatima0923/AssessmentAI) | 🔴 **NONE.** Same 8 paths → **8 × `404`**, no sidebar entry. 🔴 README's License section says only *"This project is for academic research purposes"* — **not an OSI grant and not a licence at all** | **0** | 7-node LangGraph essay-evaluation pipeline, configurable assessor persona, FAISS RAG, human-in-the-loop, AI-only vs AI-against-human-marks modes; Gradio, PyMuPDF, DeepSeek API | 🔵 **not placed** — no country stated |

🔴 **The `ai-grading-system` row is the one worth a lesson, and it is the inverse of `p411`'s.**
`p411` recorded *"a manifest that **agrees** with the grant and proves nothing."* 🔴 **Here the
manifest DISAGREES with the absence**: a green MIT badge and a prose pointer, over **zero** bytes of
grant on eight paths. 🟢 **`T98` (new): a badge and a prose pointer are both claims about a payload,
and neither is one.** The base already holds the un-badged version of this —
`aaryansamanta/ai-ethos` at **498★** with no sidebar entry (`p416`) — and the badged version is
*more* dangerous, because it survives a casual look.

🟡 **Both are promoted to NOTHING, deliberately.** They are a **capability** sighting, not supply:
they demonstrate that the discursive-grading pattern is being built independently in at least two
places on LangGraph, which is a market signal. 🔴 **Neither belongs in a client document** — an
ungranted repository is all-rights-reserved by default, and the Brazilian one would have to be asked
for a real `LICENSE` commit before it could even be evaluated. 🟢 That ask is cheap and is recorded as
`ACTION p417-A`.

### 🟢 Confirmations — a confirmation is a measurement, and one of these is a digest match

- [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — 🟢 **`LICENSE` read
  first-hand: `25 289` B, `540` lines, `sha256:77d2692c3d64`, title line *"Open Data Commons Open
  Database License (ODbL)"*, served `200`.** This **confirms this base's own carried cell** —
  *"ODbL-1.0 + CC BY-SA 4.0 (`LICENSE` read first-hand, 25,289 bytes of genuine ODbL text)"* — to the
  byte. 🔴 **And it matters for the reason `p416` gave about `cn-math-taxonomy`:** the two best
  curriculum knowledge graphs this base knows are **both** outside the permissive shortlist — one
  `CC BY-NC 4.0`, one `ODbL-1.0 + CC BY-SA 4.0`. 🟢 ODbL is *not* non-commercial, so `os-taxonomy`
  **is** usable in paid work, under share-alike on the database. That distinction is the whole
  difference between the two rows and it should never be collapsed to "both non-permissive".
- 🔵 **A search claim refuted on the payload, in this file's own idiom:** one leg reported `H5P` as
  *"MIT-licensed"* and SCORM export as going through a separate desktop tool. The licence family is
  carried here already; **the split-tool structure is the part a proposal gets wrong**, and it is
  recorded on `verticals/solutions.md` this pass rather than here.

### 🔵 The agent field, measured against `p416`'s standing suggestion

🟢 `p416` closed with a rule for successors: *"before any pass asserts a shape of the field — a hub,
a gap, a missing tier — `grep -rF` the band it claims is empty."* 🟢 **This pass followed it and
therefore asserts no shape.** What it can say is bounded and checked: of **13** candidate addresses
named across ten legs, **11** were already shelved (`scorm-engine` 53 hits, `bandup` 50,
`BaijayantaRoy` 28, `Autonomous-Exam-Proctoring` 84, `biswal-prem` 90, `SCORM-to-xAPI-Wrapper` 100,
`Adapt` 123, `H5P` 192, `Lumi` 95, `os-taxonomy` 142, `Papermorph` 28) and **2** were new, both
ungranted. 🔵 **A 2-in-13 novelty rate on a 417-pass shelf is the expected number**, and recording it
is how a successor can tell whether the channel is drying up or the shelf is saturated.


## 🆕 `p416` · 2026-10-23 — **Sixty-eight addresses read across four discovery legs returned exactly ONE unshelved in-domain repository — and it closes a scarcity this base declared BY NAME. `DozenTwelve/Papermorph` is MIT, readable and emits SCORM 1.2/2004, where the shelf's only prior SCORM emitter is source-CLOSED. 🔴 AND `p415`'s headline — "the agent field has one hub and no middle" — is refuted by four middle-tier addresses already recorded in `agents/top.md` itself.**

🔵 **Dating note.** Every search leg, licence read, payload read and gate run below was executed on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twenty-second pass dated
today**, after `p395`–`p415`.

🟢 **Gates ran three times, and the middle run is the one worth recording: 50 / 51 → 48 / 51 →
50 / 51.** Green on arrival, equal to `p413`–`p415`. 🔴 **Then this pass's own shelf writes turned
`gate-census-currency` and `gate-union-currency` red** — the published census triple no longer
matched the live shelves. 🟢 Re-derived with `make address-shape-census` / `make union-currency` as
the last act before the commit and **restated rather than back-dated**, per `p352` and `p376`; back
to 50 / 51. 🔵 The lone remaining red is `gate-census-union` control 24, **`Gap 400-B`**, carried
deliberately red since `p398`; `p387-G` forbids closing it by weakening a control and this pass did
not try. 🔴 **Honest deviation from `p412`'s standing rule:** the first gate run was started *in
parallel with* the first research leg, not strictly before it. Nothing below depends on a gate
result — but the rule says *first*, and this pass did not obey it to the letter.

🔵 **Channel note, re-measured and in agreement with `p414`–`p415`.**
`curl -sS https://github.com/GeminiLight/gen-mentor` → **`http=403`, 378 B**, and the body is the
*session's own* refusal (*"GitHub access to this repository is not enabled for this session. Use
`add_repo`…"*), **not** GitHub's; `https://api.github.com/repos/CaviraOSS/PageLM` returns the
**identical 378-byte body**. The same addresses read cleanly through `WebFetch`, and
`raw.githubusercontent.com` serves **`200`** — which is how the byte-level grant read below was
taken. 🟢 `p414`'s `AUTHZ-REFUSED` class, confirmed a third consecutive pass, on a third pair of
addresses.

### 🔴 `p415`'s headline is refuted by `p415`'s own file — four middle-tier addresses it omitted are recorded in `agents/top.md`

`p415` concluded, in its title line, that **"the agent field has one hub and no middle."** Four
addresses read first-hand today sit in exactly that middle, and **every one of them was already on
these shelves before `p415` wrote** — three of the four on `agents/top.md`, the file carrying the
claim.

| Address | stars, read today | Grant | already recorded at | in `p415`'s fifteen-row table? |
|---|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | **2.0k** | 🔴 **dual**: stock MIT at `LICENSE.md` **plus** a non-OSI "Community License" (`8 563` B, non-commercial, §4 revenue-share) | `agents/top.md:1289`, `agents/trending.md:4463`, `:5592`, `:5632` | 🔴 **no** |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | **1.7k** | 🔴 **AGPL-3.0** | 266 hits across these shelves | 🔴 **no** |
| [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) | **326** | 🟢 **Apache-2.0** *(grant at `LICENSE.txt`, not `LICENSE`)* | `agents/top.md:1597`, `:1845`, `:2187` | 🔴 **no** |
| [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | **133** | 🟡 **CC0-1.0** | `agents/trending.md:3907`, `:8129`, `:8639`, and the gate fixture `cc0-1.0-gen-mentor` | 🔴 **no** |

🔴 **And no threshold explains the omission.** `p415`'s table includes `mentingo` at **96★**,
`tutor-mcp` at **53★** and `papayaykware/agente-educativo-psicocognitivo` at **0★**, so it was not
filtering by scale. Nor by copyleft: it included `freelingo` at **AGPL-3.0**. 🟢 **The strongest
single case is `ai-shifu`** — permissive, squarely in-domain (agent-led course delivery, Research
Center of Intelligent Software Engineering, Harbin Institute of Technology), **326★**, and written
onto `agents/top.md` three times before `p415` ran.

🔵 **The lesson is about the instrument, not the author.** "No middle" was a property of a
fifteen-row hand-picked table, and it was published as a property of the field. A shelf that
re-measures addresses but not its own *selection* will keep producing confident claims about
absences it created. 🟢 **Standing suggestion for a successor:** before any pass asserts a shape of
the field — a hub, a gap, a missing tier — `grep -rF` the band it claims is empty.

### 🟢 The one unshelved in-domain address of sixty-eight read today

| Repo | Grant, read byte-level | Stars | What it is | Region |
|---|---|---|---|---|
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 **MIT** — `main/LICENSE`, **`1 069` B**, `sha256:41857092247a`, served `http=200` from `raw.githubusercontent.com` | **849** | Claude Code skill: a textbook becomes narrated, interactive web lessons; a story becomes a paper-puppet film. Static pages on a shared player, video export, and **SCORM 1.2 / 2004 packaging via `scripts/scorm.py`**. Engine versioned by tag, latest `engine-v2.1` | 🔵 **not placed** — English README, owner `DozenTwelve`, no country stated |

🟢 **Why this one matters, and it is not the star count.** `agents/top.md:1815` already records that
SCORM support **"is genuinely scarce in permissive open source"** — and the address it records there,
[`thanh01pmt/interactive-quiz-kit`](https://github.com/thanh01pmt/interactive-quiz-kit), is
**manifest-MIT with the source closed**. `agents/trending.md:5080` records **"No SCORM result at
all, from a leg that named SCORM explicitly."** These shelves therefore hold SCORM *consumers* —
[`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT, **357★**, SCORM 1.2 + 2004
with IMS Simple Sequencing), [`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper)
(MIT), `scormflow/scorm-engine-client` (MIT) — and, until today, **no readable permissive
producer**. 🟢 **`Papermorph` is one.** The declared scarcity is closed, not re-declared.

🔵 **Second grant, declared rather than discovered.** The README's own licence section reads:
*"[MIT](LICENSE). The bundled MathJax (`engine/vendor/mathjax`) is under the Apache License 2.0."*
🟢 That is `p414`'s *second-grant-on-a-subtree* shape — and unlike `education-agent-skills`, this one
is **announced in the README with its path and its family**, which is the behaviour this base should
be rewarding. `LICENSE.md`, `LICENCE` and `COPYING` all return `404`: one grant file, one vendored
exception, no pointer.

🔴 **Provenance caveat, and it is the reason to read a holder line and not just a family.** The MIT
payload's copyright line reads **`Copyright (c) 2026 TedKaczynski`** — a handle, not a legal entity,
and not the repository owner's name either. `p129-transcription-audit` exists because the **holder**
is a different question from the **family**. The grant is stock MIT and the text is clean; **the
assignor is unattributable**, and that is a procurement question, not a licence question. Flag it
before this address reaches a client document.

### 🔴 Four carried star figures re-measured — and one of them went DOWN

| Address | carried on these shelves | read today | delta |
|---|---|---|---|
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | `1 704` (`agents/trending.md:5630`), `780` (`:7865`) | **2.8k** | 🔴 **+64%** on the newer figure; the older has more than **tripled** |
| [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | `338` (`:5597`), `317` (`:7838`), `127` (`:14591`) | **403** | +19% on the newest carried figure |
| [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) | `356` (`:5595`), `342` (`:6051`) | **391** | +10% |
| [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | `135` (`:3907`, `:8129`) | **133** | 🔵 **−2 — it went down** |

🔵 **The `gen-mentor` row is the useful one.** Stars are **not monotonic**, and a base that only ever
revises a count upward is not measuring, it is extrapolating. `p415` refuted three figures and all
three moves were large; this pass records a two-star decrease because the alternative is a shelf that
can only detect growth.

🔴 **`cn-math-taxonomy` is the row to watch and the row NOT to build on.** It is the best Chinese K-12
curriculum knowledge graph these shelves know, it is growing fastest of anything measured today — and
it is **CC BY-NC 4.0**, barred from paid work, and its own README states the content is an
**unreviewed AI-generated draft**. Both facts travel together or neither should be quoted.

### 🟢 Confirmations — recorded because a confirmation is a measurement too

- [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) — **498★**, and the sidebar
  has **no licence entry at all**. Confirms `agents/trending.md:7876` and `repos/trending.md:7302`
  (carried `499`/`501`). A 498-star nonprofit education repository with **no grant** is
  all-rights-reserved by default; the 501(c)(3) framing does not change that.
- [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) — **Apache-2.0, 582★, Portuguese
  README, archived by the owner on `2024-12-12`, read-only.** Confirms `agents/trending.md:14606`.
- [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) — **Elastic License 2.0**,
  **340★**, source-available, built by Canyon GBS with Gates Foundation support. Confirms
  `agents/trending.md:5629`.
- 🔵 **One increment on `PageLM`:** the non-OSI document is named **two different ways on the same
  page** — the README body calls it the **"CaviraOSS Community License"**, the badge immediately
  above it the **"PageLM Community License"**. `agents/trending.md:4463` records only the second
  name. A grant that cannot name itself consistently is a grant to read in full before relying on it.
- Permissive rows re-read clean and unchanged: `pykt-toolkit` MIT **451**, `tsugi` Apache-2.0 **376**
  (Apereo, LTI), `scorm-again` MIT **357**, `pyedmine` MIT **82**, `EduStudio` MIT **79**,
  `fsrs4anki` MIT **4.1k**.

### 🔴 Searched and NOT found — recorded so a successor does not re-spend the leg

- 🔴 **There is still no permissive education ERP.** The literal ERP/CRM leg returns exactly one
  education ERP, **OpenEduCat**, and it is **LGPL-3.0** — not MIT, not Apache. Every other result on
  that leg was the same vendor's own comparison pages in eight languages.
- 🔴 **Fifth consecutive nil on the LATAM leg — but the gap has changed shape.** The Spanish leg
  naming Brazilian, Mexican and Chilean universities returned no repository: a Panamanian LinkedIn
  announcement with no licence and no code, and `1111philo/learn` whose licence reads *"other"*.
  🟢 **What is new is that the nearest thing to a LATAM-origin platform already exists and is
  frozen** — `menthorlabs/menthor`, Apache-2.0, 582★, Portuguese, archived since `2024-12-12`.
  The gap is **not** "none was built"; it is "the one that was built is unowned".
- 🔴 **EMEA still has no education agent at scale.** The only EMEA-origin agent the legs surfaced is
  [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) — **Apache-2.0, 24★**,
  Technische Hochschule Mittelhessen, automatic checking of student submissions with immediate
  corrective feedback and aggregation of common errors for the lecturer. 🔵 Already shelved (92 hits).
  Good provenance, real pedagogy, **no scale** — the EMEA finding of `p415` stands.
- 🔴 **No authoritative 2026 ranking of education-specific agents exists**, for the second pass
  running. The global leg returns general-purpose agent lists in which education is a use-case
  column, plus self-published blog rankings.

## 🆕 `p415` · 2026-10-23 — **The agent tier re-measured FIRST-HAND against the live GitHub sidebars, and three figures this base carried are refuted — one of them by a factor of 31.** 🟢 Fifteen agent addresses and nine foundations read today, every licence taken from the repository's own sidebar. 🔴 AND the read channel matters: `curl` and `api.github.com` are REFUSED for every repository not attached to this session, so a pass that reports "unreachable" from `curl` alone is reporting a fact about the CHANNEL.

🔵 **Dating note.** Every search leg and every licence read below was executed on **2026-10-23**, and the
commit lands **2026-10-23**. This is the twenty-first pass dated today, after `p395`–`p414`.

🔵 **Channel note, measured this pass.** `curl -sI https://github.com/CAHLR/OATutor` → **403**, and
`curl -s https://api.github.com/repos/HKUDS/DeepTutor` returns the session's own refusal body
(*"GitHub access to this repository is not enabled for this session"*), **not** GitHub's. The same
addresses read cleanly through `WebFetch`. Both instruments were run side by side before any address
below was written down. Every licence, star count and date in this pass came through `WebFetch`.

### 🔴 Three carried figures REFUTED by a first-hand read — and the direction is not uniform

| Address | carried as | read today (sidebar) | Verdict |
|---|---|---|---|
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | `~12k★` (`education_cycle3`) | 🔴 **387★**, MIT | **Refuted — carried figure is ~31× the real one.** Never sourced first-hand; it entered from a secondary list |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `~24k★` (`education_cycle3`) | 🟢 **42.3k★**, Apache-2.0, `v1.6.15` **2026-10-19** | **Refuted upward.** The project nearly doubled; the stale figure under-sold the one address on these shelves with real scale |
| [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | `Apache-2.0`, `~200★` | 🟢 **MIT**, **488★** | **Licence cell refuted.** MIT is *more* permissive than the shelf claimed — the error was conservative, but it was still an error |

🔵 **Why this matters more than the numbers.** All three carried values came from secondary lists, and
all three were wrong in different directions. A star count is cheap to re-read and worthless when
guessed; an inherited one should be treated as unmeasured until a sidebar says otherwise.

### 🟢 The agent tier — fifteen addresses, every licence read from the repository sidebar on 2026-10-23

| Repo | Licence (sidebar, read today) | Stars | What it is | Region |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | **42.3k** | Agent-native learning workspace: tutoring, problem solving, quizzes, research, visualisation and mastery practice in one extensible system. `v1.6.15`, **2026-10-19** | **APAC** — HKU Data Intelligence Lab |
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 **MIT** | **1.2k** | AI study partner for maths and CS: plans a learning route, explains concepts, walks projects. Updated **2026-10-21** | **APAC** — Simplified-Chinese README, English version linked |
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** | **530** | MCP server over Anki — read, create and manage cards and decks from an assistant. Updated **2026-10-22** | Global |
| [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | 🟢 **MIT** | **488** | Multi-agent system on the **ADDIE** instructional-design model: syllabi, slides, scripts, assessments, plus evaluation tooling | Global |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **451** | PyTorch library for training and benchmarking deep **knowledge-tracing** models with standardised preprocessing | **APAC** — China |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** | **387** | Python package that generates educational content — MCQs, lesson plans — with generative models | **APAC** — India |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** | **307** | MCP server for **Canvas LMS**: student- and educator-side tools exposed to Claude, Cursor and similar clients | **North America** |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT** | **292** | Socratic tutor built on Bloom's 2-sigma framing. Ships **both** as a Claude Code skill and as a self-hostable web app. Updated **2026-10-20** | **APAC** — Chinese-first |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | **269** | Open-source adaptive tutoring system; skill mastery estimated with **Bayesian Knowledge Tracing**. React, optional Firebase logging | **North America** — CAHLR, UC Berkeley |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🔴 **AGPL-3.0** | **203** | Self-hosted language-learning platform: CEFR study plans, AI tutor, voice conversation, flashcards, spaced repetition, local or cloud LLMs. Updated **2026-10-21** | **EMEA** — author Arturo Carretero Calvo |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | **149** | Local-first learning workspace: uploaded course material becomes notes, quizzes, flashcards and an adaptive tutor. Updated **2026-10-22** | Global — English original, Chinese translation |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** | **112** | Community Edition of a personalised-tutoring platform. 🟡 **CE/EE split** — the Enterprise Edition is proprietary, so read the boundary before building on it | **EMEA** — founded by Mohamed El Hajji; page states no country |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **96** | Self-hosted LMS with an **AI mentor for role-play training**, aimed at corporate L&D and compliance. Updated **2026-10-23** | 🔵 **not placed** — maintained by Selleo, a product-engineering company; the page states no country |
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT** | **53** | MCP server that gives any assistant adaptive tutoring: **BKT + FSRS** sequencing, durable learner state. 🟡 Self-declared **alpha**; profiles need `v0.6.0+`, `v0.6.1` is the recommended patch | 🔵 not placed |
| [`papayaykware/agente-educativo-psicocognitivo`](https://github.com/papayaykware/agente-educativo-psicocognitivo) | 🟢 **MIT** | **0** | Adaptive tutor: **Deep Knowledge Tracing**, emergent psycho-cognitive profile, affect detection, dynamic planning. Spanish README. 🔴 **Roadmap-stage, zero stars** — publish only as a reference design | **LATAM** — Spanish-language |

🟢 **Twelve of the fifteen are MIT, one BSD-3-Clause, one Apache-2.0 — thirteen are build-on grants.**
🔴 **One, `freelingo`, is AGPL-3.0:** hosting it unmodified is fine; shipping modified code to a client
is the trigger. It is on the shelf because its CEFR + FSRS design is the most complete
language-learning reference here, not because it can be forked into client work.

### 🔴 Searched and NOT found — recorded so a successor does not re-spend the leg

- 🔴 **No mature LATAM-origin open-source education agent.** Two Spanish-language legs
  (`proyecto código abierto agente IA educativo github 2026 tutor español universidad latinoamérica`
  and the regional LATAM leg) returned exactly one on-brief address,
  `papayaykware/agente-educativo-psicocognitivo` — **MIT, 0 stars, roadmap-stage**. This is the fourth
  consecutive pass to find no LATAM-origin agent with traction. **The gap is structural, not a miss.**
- 🔴 **No EMEA-origin education agent with scale.** `freelingo` (AGPL-3.0, 203★) and
  `open-tutor-ai-CE` (BSD-3, 112★) are the whole EMEA agent supply on these shelves. Europe's public
  money is going into *models* (OpenEuroLLM, Teuken, Apertus) and *regulation*, not into agents.
- 🔴 **No authoritative 2026 ranking of education-specific agents exists.** The global leg
  (`top open source AI agents education 2026 github MIT`) returns general-purpose agent lists —
  OpenClaw, OpenHands, CrewAI, SWE-agent — with education appearing only as a use-case column.
  Any "top education agents 2026" list a successor finds is almost certainly a general list re-tagged.

## 🆕 `p414` · 2026-10-23 — **`34 501` is NOT the AGPL-3.0 `http` form — it is ONE repository's de-indented title line, and the spread is a 2×2 lattice over `34 520` whose four cells are all now measured. 🔴 `education-agent-skills`' grant is a POINTER on BOTH its subtrees and its operative text is unreachable here. 🔴 AND the egress refusal has TWO classes these shelves record as one.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the twentieth pass
dated today**, after `p395`–`p413`.

🟢 **Gates FIRST, per the standing rule `p412` set and `p413` kept.** `make hooks` ran **before** any
research: **50 of 51 gates green on the FIRST run** — equal to `p413`'s best-ever first-run state and
again against `47` for both `p409` and `p412`. 🔵 The lone red is `gate-census-union` control 24,
**`Gap 400-B`**, carried deliberately red since `p398`; `p387-G` forbids closing it by weakening a
control and this pass did not try. 🟢 **`p413` left the base clean** — the currency gates were green
on arrival for the second consecutive pass.

🔵 **Channel note, and it CORRECTS `p413`'s largest finding rather than repeating it.** `p413`
concluded the egress channel is an **allowlist** and recorded its evidence as *"`http=000` —
connection never established, **not a `403`**, not a `404`"*. 🔴 **There is a `403`, and it is at the
`CONNECT` layer**: `curl` prints `CONNECT tunnel failed, response 403` and the proxy names
`connect_rejected` — *"the host is not allowed for this session"*. 🟢 **`p413`'s conclusion was right
and its evidence was under-read**, and reading it properly splits what these shelves record as one
refusal into **two classes with different remedies**:

| class | http | body | what it means | remedy here |
|---|---|---|---|---|
| 🟢 **SERVED** | `200` | yes | `pypi.org`, `raw.githubusercontent.com`, `registry.npmjs.org` | — |
| 🟢 **SEMANTIC-404** | `404` | yes (21 B) | the registry **answered**; the absence is a fact | — |
| 🔴 **AUTHZ-REFUSED** | `403` | **yes, 378 B** | tunnel opens; the body names the **session's repository scope** (`api.github.com`, `codeload.github.com`) | a scope grant — **not** a host problem |
| 🔴 **TUNNEL-REFUSED** | `000` | **no** | `CONNECT` 403 + `connect_rejected`; host **not on the session allowlist** | 🔴 **none on this environment** |

🔵 Fifteen URLs, control pair first, in
[`evidence/refusal-taxonomy.2026-10-23-p414.tsv`](../evidence/refusal-taxonomy.2026-10-23-p414.tsv);
the probe is [`compose/code/p414-refusal-taxonomy/refusal.sh`](../compose/code/p414-refusal-taxonomy/refusal.sh).
🟢 **Why the split pays:** an `AUTHZ-REFUSED` host is reachable and merely unauthorised, so a figure
behind it is *obtainable in principle*; a `TUNNEL-REFUSED` host is not, so a figure behind it is
**unverifiable on this channel, permanently**, and `p413`'s standing register rule applies. 🔴 This
base's own [`p798-proxy-refusal-ledger`](../compose/code/p798-proxy-refusal-ledger/README.md) records
refusals **without** this class split — successor item 1.

### 🔴 `education-agent-skills`' grant is a POINTER on BOTH subtrees, and the subtree that holds the CODE is the one with no scope

🔵 This base carries [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
across every shelf — **`CC-BY-SA-4.0`**, `1 230` B, `f952182df4eb`, `main` `6bbbce4`, `165` `SKILL.md`
— and `agents/trending.md` grades it *"**cesión**, no identificador"*: a **grant**, not a mere
identifier. 🔴 **First-hand, it is a `POINTER` on `p307`'s three-valued classifier, and so is its
second grant.** `repos/trending.md:13531` already notes *"second grant at `mcp-server/LICENSE`"* —
🔴 **and no pass has read it.** It is a **different payload**:

| # | finding |
|---|---|
| 1 | 🔴 **Neither in-tree payload contains CC BY-SA 4.0's operative legalcode, and each says so of itself.** The root `LICENSE` closes *"**This is a human-readable notice.** The full legal terms are available at: `creativecommons.org/licenses/by-sa/4.0/legalcode`"*; `mcp-server/LICENSE` closes *"Full licence text: `…/legalcode`"*. 🟢 That is `p307`'s `POINTER` class and `p254-scoped-grant-reference`'s subject verbatim — *a POINTER to a licence is not a GRANT* — and the gate exists for exactly this shape |
| 2 | 🔴 **The two payloads are not the same text.** Root **`1 230` B / 33 lines / `f952182df4eb`**; `mcp-server/LICENSE` **`978` B / 28 lines / `f8366f5391f4`**. Delta **252 B**, and `diff` shows the four deleted lines **are the scope sentence** |
| 3 | 🔴 **And the scope is deleted from the half that is software.** The root grant names its subject — *"the educational skills, documentation, examples, and curriculum materials in this repository"*. `mcp-server/` names **nothing at all**, and `mcp-server/` is the **MCP server**: the one subtree that is code rather than curriculum is the one whose content licence declines to limit itself. 🟢 `gate-grant-scope`'s subject — *a grant has a SCOPE and a PROVENANCE* — and the direction is **against** the consumer, not for them |
| 4 | 🔵 **A provenance signal in the spelling.** The root is en-GB throughout (*"licence"*); `mcp-server/LICENSE` is en-US in its body (*"license"*) and en-GB in its final line. 🟢 Two authoring events, not one template copied twice — which is why a successor should expect a **third** payload if a third subtree appears |
| 5 | 🔴 **The operative text is `TUNNEL-REFUSED` on this environment.** `creativecommons.org/.../legalcode` answers `http=000`, `CONNECT` 403, against a control pair that served `200` twice. 🟢 **So 100 % of this address's operative licence is by reference and 0 % of it is readable here** — the first address on these shelves in that state, and a sharper thing to record than "CC BY-SA 4.0" |

🟢 **What does NOT change:** the ShareAlike reading these shelves already publish, and the
*reference-don't-vendor* posture, both stand — `p85`'s cost analysis is untouched. 🔴 **What changes
is the class and the compliance step**: a reviewer who grades this address from the in-tree file is
grading a notice, and the terms they would be held to are on a host this environment cannot open.
🔵 Both payloads, digested, in
[`evidence/pointer-grant-subtrees.2026-10-23-p414.tsv`](../evidence/pointer-grant-subtrees.2026-10-23-p414.tsv).

### 🟢 The agent tier — nil new supply for a sixth pass, and five currency re-reads that all held

🔴 **The English legs returned five agent-layer addresses and every one was already shelved.** 🟢 The
budget was spent re-reading their grants first-hand at a ref rather than re-asserting carried cells:

| slug | `LICENSE` read at a ref | bytes · sha256 | shelf |
|---|---|---|---|
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | `main/LICENSE` | `1 069` · `7d574cf3632e` | 🟢 **MIT**, agrees |
| [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | `main/LICENSE` | `1 078` · `4d5d987f4f89` | 🟢 **MIT**, agrees |
| [`TovTechOrg/Tov-learn`](https://github.com/TovTechOrg/Tov-learn) | `master/LICENSE` | `1 064` · `092d389ac156` | 🟢 **MIT**, agrees |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `main/LICENSE` | `11 408` · `cd2f54e1e506` | 🟢 **Apache-2.0**, agrees |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `main/LICENSE` | `1 230` · `f952182df4eb` | 🟡 bytes and digest agree; **class does not** — above |

🔴 **No star figure is recorded this pass, and that is deliberate.** The relay offered `DeepTutor` at
*"~41.6k"* and *"~41k"* from two sources against the `22`–`24k` these shelves carry from August.
🟢 **Stars are unverifiable on this environment**: `api.github.com` is `AUTHZ-REFUSED`, and a relayed
figure cannot be pinned to a ref or digested. 🔵 Recording the movement as fact would put an
unverifiable number in a cell that currently holds a dated one — see
[`evidence/agent-licence-reread.2026-10-23-p414.tsv`](../evidence/agent-licence-reread.2026-10-23-p414.tsv).

### 🔵 One channel claim this pass nearly published, and did not

🟡 **`registry.npmjs.org` is not a new channel.** It answered `200` on a real package and a semantic
`404` on an invented one, which looked like a third surface beside `p413`'s two. 🔴 **This base opened
it at pass 49** — [`compose/code/npm-surface-probe`](../compose/code/npm-surface-probe/README.md) —
and `intel/trends.md` already calls it *"an independent second channel"*. 🟢 Checked before writing,
and recorded here so a successor does not spend a leg rediscovering it. 🔵 `p413`'s *"two surfaces
remain"* should read **three**: PyPI JSON, `raw.githubusercontent.com`, and the npm registry.

## 🆕 `p413` · 2026-10-23 — **AGPL-3.0 IS a revision family, and `Pattern AI`'s AGPL reference is a SUBTRACTION rather than a measurement. 🟢 `openedx/edx-platform`'s grant is NARROWED and this base carried the bytes without the consequence. 🔴 AND THE EGRESS CHANNEL IS AN ALLOWLIST — every "proxy-refused" note on these shelves is a fact about the CHANNEL, not the host.**

🔵 **Dating note.** Every search leg, licence read, registry probe, channel probe and gate run below
was executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the nineteenth pass
dated today**, after `p395`–`p412`.

🟢 **Gates FIRST, per `p412`'s successor item 1.** `make hooks` ran **before** any research:
**50 of 51 gates green on the FIRST run** under `p300`'s no-masking runner — **the best first-run
state this base has recorded**, against `47` for both `p409` and `p412`. 🔵 The lone red is
`gate-census-union` control 24, **`Gap 400-B`**, carried deliberately red since `p398`; `p387-G`
forbids closing it by weakening a control and this pass did not try. 🟢 **`p412` left the base
clean** — `gate-census-currency` and `gate-union-currency` were **green on arrival**, the first time
a pass has inherited a current census rather than a stale one.

🔵 **Channel note, and it is this pass's largest finding.** The egress channel was probed with
`p293`'s control pair FIRST: `pypi.org` **200**, `raw.githubusercontent.com` **200**. Then **10 of
10** other hosts answered `http=000` — *connection never established*, not a `403`, not a `404`:
`moodle.org`, `openeducat.org`, `education.ec.europa.eu`, `gov.uk`, `tum.de`, `uni-siegen.de`,
`kimadu.de`, `lernen-digital.nrw`, `bildungsserver.de`, `diariodarepublica.pt`. 🔴 **Two of those
are this industry's own flagship project domains.** 🟢 So the refusal is a property of the
**channel**, not of any host, and it is an **allowlist** rather than a geography filter — a
conclusion no single-host observation could reach.

### 🟢 What this pass did on the agent layer

| # | finding |
|---|---|
| 1 | 🟢 **`Gap 412-B` is CLOSED, and the AGPL side of the agent layer is byte-identical across the Open edX MCP pair.** [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) `master/LICENSE` and [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) `master/LICENSE` both read **`34 524` B, `662` lines, sha256 `8d56b405468a`** — the same payload to the byte. 🔵 That is the canonical `https` AGPL form (`34 523` B) **plus one trailing newline**, so the pair's shared `34 524` is a presentation, not a third licence |
| 2 | 🔴 **`Gap 297-R` HARDENS on a second distribution, and it will not close by waiting.** `tutor-contrib-openedxmcp` on PyPI is **`v0.2.2`, 9 releases, last upload `2026-10-22`**, `license` field **`AGPL-3.0`** — carried here at `v0.2.0`. 🔵 It pairs *exactly* with `p412`'s reading of `openedx-mcp` at **`v0.1.9`, 9 releases, `2026-10-22`**: **both halves of the Open edX MCP side-car — the library and the Tutor plugin that deploys it — are AGPL, at the same release count, shipped the same day.** 🔴 The absence `Gap 297-R` names is a *permissive* side-car, and two actively-maintained distributions have now declined to become one |
| 3 | 🔴 **`tutor-contrib-openedxmcp` publishes NO `project_urls` and NO `home_page` on PyPI** — `p280`'s unattributable class, **third instance, second on PyPI**. 🟢 **And the attribution sharpens: both PyPI instances are the same publisher's packages** (`blend-ed`'s library and its Tutor plugin), so the cause is the **publisher's metadata habit**, not a registry defect. 🔵 This base already carries the `0.1.7` reading as *"ninguno declarado"*; what is new is that it is a **house pattern across the family**, which is a predictor for the next package they ship |
| 4 | 🔴 **`p312`'s template registry has no AGPL-3.0 entry at all.** `identify()` returns **`UNKNOWN-TEMPLATE`** on **all ten** AGPL payloads this pass read first-hand, including both agent-layer addresses above. 🟢 So on this family the only instruments that answer identity are **`p378`'s presentation fold** and the header read — and `gate-bespoke-title`'s rule that *`UNKNOWN-TEMPLATE` must never be read as bespoke* is doing more work here than its own docstring claims, because it is covering an **entire licence family**, not an edge case |
| 5 | 🟢 **A new EMEA agent instrument, and it is a SHAPE this base has not carried: permissively-licensed supply with no repository.** **KIMADU** (Universität Siegen with NRW's Ministerium für Schule und Bildung, state-funded **above €1 M**, running **2025-02-01 → 2027-07-31** across **25** schools) publishes **eleven didactic German-subject agents** whose system prompts / megaprompts are **OER under `CC BY-SA 4.0`** — downloadable, adaptable, and explicitly transferable into one's own environment. 🔴 **But it is distributed as HTML and PDF from `lernen-digital.nrw` and `kimadu.de` for pasting into ChatGPT or fobizz: no repository, no package, no version, no digest.** 🔵 Every other permissive agent on these shelves is citable by `(FILE, digest)`; this one is not, and the gap is in the *distribution*, not the grant |
| 6 | 🔴 **The KIMADU grant is SCOPED, and the scope excludes the part that carries the pedagogy.** The `KIM — Lehrpartner für Schreibaufgaben` document states the licence covers *"ausschließlich den Prompt und unsere Informationen zur Nutzung des KI-Agenten"* — **only the prompt and the usage notes.** 🔴 The agent is designed to run with **three knowledge-base libraries supplied as Wissensdateien**, and those sit **outside** the `CC BY-SA 4.0` grant. 🟢 `gate-grant-scope`'s subject exactly — *a grant has a SCOPE and a PROVENANCE* — on a prompt asset rather than a source tree, which is a first here |
| 7 | 🔴 **`Gap 411-A`'s class recurs, and this time the MECHANISM is readable in the source URL.** The German leg returned *"KIMADU has released a fully functional, data-protection-compliant platform, available as open-source software for all universities."* 🔴 **It has not.** The sentence comes from a newsletter issue whose own title concatenates **"NRW startet Projekt KIMADU"** and **"KI für alle Hochschulen in BW"** — **two separate items in one issue, fused by the summariser.** 🔵 `p411`'s instance was an invented *fork*; this is an invented *release*. 🟢 What is actually open is prompts under `CC BY-SA 4.0`, which is finding 5 — the real fact was adjacent to the invented one, which is why the invention is hard to see |
| 8 | 🔴 **And this base cannot verify finding 5 or 6 first-hand, now or ever on this environment.** `kimadu.de`, `lernen-digital.nrw`, `uni-siegen.de` and `bildungsserver.de` are all `http=000` against a control pair that returned `200` twice. 🟡 **So both rows are published SEARCH-CHANNEL ONLY and labelled so** per `gate-restatement`, and the honest register entry is *"unverifiable on this channel"* rather than *"re-try the host"* — see the trends shelf for why that distinction is now a standing rule |

🔵 **What the English regional legs returned on the agent layer: nothing.** `p412`'s successor item 3
said not to re-ask them; this pass re-asked them anyway and **the advice was right** — **17** named
regional facts checked against these shelves, **15 already carried**, and the 2 unshelved are a
vendor ranking whose own figures its publisher does not source and a Microsoft-attributed adoption
figure this base already holds under UNESCO IESALC and TALIS attribution. 🟢 **The cost is recorded
here so a sixth pass does not pay it again.** 🟢 **The in-language legs paid for the third time in
four passes** — German and Portuguese returned seven unshelved items, and findings 5–7 are what
survived verification.

## 🆕 `p412` · 2026-10-23 — **`make hooks` RUNS**, the pass that declared it unrunnable is the pass that **broke a gate**, **“5 authors” is `%an` and collapses to 3**, and the GPL-3.0 denominator spread is **two FSF revisions, not noise**

🔵 **Dating note.** Every search leg, clone, licence read, registry probe and gate run below was
executed on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the eighteenth pass
dated today**, after `p395`–`p411`.

🟢 **Channel note — and the headline is a channel REFUTATION.** `make hooks` **RAN TO COMPLETION
this pass: 47 of 51 gates green** under `p300`'s no-masking runner. 🔴 **`Gap 410-C` (“`make hooks`
unrunnable”) is therefore REFUTED, not closed** — and this is the **second** time this base has had
to refute it: `p397` already disposed of the identical belief as `Gap 396-C`, recording that *“the
repository's python runs here, `make hooks` runs here, and three gates had drifted red with nobody
looking.”* 🔴 **`p410` and `p411` re-acquired a belief this base had already disproved**, and the
cost was **three consecutive passes of gate blindness**. Measured this pass:

| channel | `p411` reading | `p412` reading | note |
|---|---|---|---|
| `make hooks` | 🔴 declared unrunnable | 🟢 **47/51 green on the first run, 50/51 after repair** | 🔴 **the central claim of the last two passes, refuted by running it.** The lone remaining red is `gate-census-union` control 24 = **`Gap 400-B`**, carried deliberately red since `p398` |
| `api.github.com` | `403` | 🔴 `403` | unchanged for a third pass |
| `github.com` HTML | `403` | 🔴 `403` | reproduces `p411` |
| `git` smart-HTTP | works | 🟢 works | `ls-remote moodle/moodle HEAD` = `46c042e7da65f8cb2ec7dc19f46566ce61a393e1`; every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second registry channel |
| **PyPI** | `200`, recorded as **unused** | 🟢 **`200`, and USED this pass** | 🆕 `p411` noted the channel and did not spend it; this pass does — see the PyPI rows |
| `gnu.org` | `000` — `connect_rejected` | 🔴 `000` | 🆕 **mechanism refined:** `curl (56) CONNECT tunnel failed, response 403` — the **proxy** refuses the tunnel; the host never answers |
| `oecd.org`, `eur-lex.europa.eu` | `000` | 🔴 `000` | same proxy mechanism; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | **third** consecutive pass reproducing the exact byte count |

🔴 **This is a GATE-AND-CORRECTION pass, and the supply brief is exhausted on BOTH halves.** Eight
legs ran — four global, four regional. 🔴 **The four global supply legs returned seven addresses and
this base already carries every one of them** (`withmarbleapp/os-taxonomy`, `karpathy/nanochat`,
`frappe/education`, `Gego-K12/gegok12`, `ashishpatel26/500-AI-Agents-Projects`,
`luongnv89/claude-howto`, Nous Research's `hermes-agent`); the only unshelved shape was
`HuggerHustle/ai-radar`, a general AI-trend issue tracker and **not education supply**. 🔴 **The four
regional legs returned ZERO unshelved facts for a FOURTH consecutive pass.** 🔵 So `p409`–`p411`'s
regional reading now holds four passes deep, and `p411`'s *“supply is exhausted only in the wording
`p408` used”* does **not** reproduce: the ERP/CRM/SIS wording that paid at `p410` and `p411` returned
nothing new this pass.

**Evidence:** [`gate-suite-result`](../evidence/gate-suite-result.2026-10-23-p412.tsv) (5 rows) ·
[`author-key-rederivation`](../evidence/author-key-rederivation.2026-10-23-p412.tsv) (3 rows) ·
[`gpl3-revision-pair`](../evidence/gpl3-revision-pair.2026-10-23-p412.tsv) (4 rows) ·
[`pypi-channel-probe`](../evidence/pypi-channel-probe.2026-10-23-p412.tsv) (8 rows) ·
[`channel-reachability`](../evidence/channel-reachability.2026-10-23-p412.tsv) (10 rows) ·
[`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p412.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **`make hooks` runs, and the two passes that said otherwise left a gate RED behind them.** 47/51 green. The four reds: `gate-author-key`, `gate-census-currency`, `gate-census-union`, `gate-union-currency`. 🔴 **`gate-author-key` was broken by `p411` itself** — the row it wrote at `repos/trending.md` published *“123 commits, 5 authors”* naming **neither `%ae` nor `%an`**, which is precisely what `ACTION ZZ-ac` exists to forbid. 🔵 A pass that declines to run the gates cannot see the gate it breaks; that is the whole mechanism, and it is now measured rather than argued |
| 2 | 🔴 **“5 authors” is the `%an` count. By `%ae` it is 3 — and `p411` published the list that refutes it.** `Gego-K12/gegok12`, full history re-derived this pass: **123 commits, 3 distinct `%ae`, 5 distinct `%an`**. `karthick@gegosoft.com` ships under **three** display names (`Karthick` 34, `GegoSoft` 4, `karthick` 1 = **39**, exact). 🔴 `devteam@gegok12.com` is a **shared ROLE account carrying 83 of 123 commits (67.5 %)**. 🔵 **No new probe was needed:** `repos/foundations.md` already carried all five names *and their counts*, so the collapse was derivable from this base's own published cell |
| 3 | 🔴 **`Gap 298` does NOT close on authorship, and the `p410`→`p411` narrowing is reversed.** `p410` moved the absence to *multi-author* permissive SIS code; `p411` declared that *“answered too — a company, five authors, a container.”* 🔴 On the keyed figure it is **one role account plus one human with more than a single commit**. 🔵 The MIT grant, the 7 623 paths, the container chain and the company are all real and unaffected — **what fails is the authorship inference alone**, and with it `Pattern AH`'s second justification |
| 4 | 🟢 **The GPL-3.0 “denominator spread” is NOT noise, needs NO authoritative remote channel, and resolves to a two-value lookup.** `p411` measured 35 141 / 35 147 / 35 149 B and concluded that with `gnu.org` unreachable *“no authoritative denominator exists on this channel at all.”* 🟢 **Measured in-tree this pass: `moodle/moodle` `COPYING.txt` = 35 147 B and `frappe/erpnext` `license.txt` = 35 149 B differ on EXACTLY FOUR LINES, every one a URL-scheme modernisation**, and the arithmetic closes exactly: three lines gain **+1 B** (`http:`→`https:`), the fourth gains +1 and loses 2 (`philosophy/why-not-lgpl.html` → `licenses/why-not-lgpl.html`) ⇒ **35 147 + 2 = 35 149** ✔. Both are **674 lines** with **zero CR bytes**, so neither line count nor line endings discriminate — **the URL scheme does, and one grep reads it** |
| 5 | 🔴 **`Pattern AI` step 4's own `~35 141 B` reference matches NEITHER measured revision.** It sits **6 B below** the `http` revision, and its provenance is unrecorded. 🔵 So the gate's denominator was never the FSF text at either revision; it is a third value this base has been quoting as canonical. 🟢 Repaired as **`Pattern AJ` Amendment 5** — which *sharpens* `p411`'s Amendment 3 rather than replacing it: two significant figures is the right floor, but the denominator is now **selectable in-tree** instead of unsourced |
| 6 | 🟢 **PyPI worked, and it re-dates `Gap 297-R` through a channel that answers while GitHub is `403`.** `blend-ed/openedx-mcp` on PyPI: **v0.1.9, 9 releases, last upload 2026-10-22 · 1 d**, **AGPL-3.0** on *both* PyPI sub-channels (`license` field and OSI classifier). 🔴 This base reads it at **v0.1.5, 5 releases**, from `p190` evidence dated **2026-10-14**. 🟢 **`Gap 297-R` STAYS OPEN — the licence has not moved** — but **`ACTION NL`'s scope (`0.1.1`–`0.1.5`) is stale by four releases** |
| 7 | 🔴 **A PyPI record that names NO repository at all — `p280`'s unattributable class, second instance, now on a second registry.** `openedx-mcp` publishes **no `project_urls` and no `home_page`**, so PyPI alone cannot link the package to `blend-ed/openedx-mcp`; that linkage comes entirely from another channel. 🔵 `p411` recorded the same class on npm (`repos/trending.md` — *“no `repository` field … live, recent and unauditable”*). 🟢 `canvas-mcp` is the well-formed control in the same probe: MIT on both sub-channels **and four URLs naming its repository** |
| 8 | 🔵 **A third channel agreeing with an absence — recorded as a corroboration, not a discovery.** `loyaniu/moodle-mcp` on PyPI (**v0.2.1, 3 releases, last upload 2026-06-29**) has an **empty `license` field and zero License classifiers**. 🟢 This base already carries it `UNGRANTED` by full-tree enumeration (13 files) *and* by an absent `pyproject.toml` licence field; PyPI is now the **third** independent silent channel. 🔵 Marked as corroboration because `gate-absence` exists to stop exactly this being re-published as a find |
| 9 | 🔵 **`gate-census-union` control 24 is red, and it is NOT a new gap — this pass’s first draft nearly re-registered it.** The control wants both rejection arms to fire on the live shelves; `NAME-REF-OR-PATH` fires and `NAME-DOT-RUN` does not. 🟢 **That is `Gap 400-B`, diagnosed at `p398`** (`p382` duplicated `p375`’s rule upstream and made the audited arm unreachable) and **carried deliberately red ever since** — `p409` recorded it as *“a sixth pass”*. 🔴 Writing it up as `Gap 412-A` would have been exactly the restated-absence defect `gate-absence` exists to catch; caught here before the commit, and recorded because the near-miss is the useful part |
| 10 | 🔴 **`p411` left NO entry in the gap register.** `intel/open-gaps.md`'s newest pass section is **`p410`**, so the register has been one pass stale all day while three of this base's own gates were red. 🟢 Repaired below: `p412` registers its own gaps **and** `p411`'s |

### 🔴 The agent tier — nil new supply, and the one agent-side address that MOVED

🔴 **No new agent addresses this pass.** The four global supply legs returned seven, all carried
(listed in the channel note above). 🔵 `p411`'s `ArnaudGuiovanna/tutor-mcp` remains the newest
agent-tier upstream on these shelves, and nothing this pass displaces it.

🟢 **What DID move is read through PyPI, not GitHub** — the channel `p411` noted and did not spend.

| address | channel | reading this pass | base's reading | verdict |
|---|---|---|---|---|
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | PyPI `openedx-mcp` | 🔴 **AGPL-3.0**, `v0.1.9`, **9 releases**, last upload **2026-10-22 · 1 d** | `v0.1.5`, 5 releases, `p190` evidence **2026-10-14** | 🔴 **`Gap 297-R` STAYS OPEN** — the licence has not moved in four releases. 🔴 **`ACTION NL` is under-scoped: it reads `admin.py` across `0.1.1`–`0.1.5`; there are now nine releases** |
| [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) | PyPI `moodle-mcp` | 🔴 **empty `license` field, zero License classifiers**, `v0.2.1`, 3 releases, last upload **2026-06-29** | already `UNGRANTED` by tree enumeration (13 files) + absent `pyproject.toml` field | 🔵 **CORROBORATION, not a discovery** — third independent silent channel on the same absence |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | PyPI `canvas-mcp` | 🟢 **MIT** on both sub-channels, `v1.14.0`, **23 releases**, last upload **2026-10-08** | already carried | 🟢 **The well-formed control** — and the only one of the three naming its repository (four `project_urls`) |

🔴 **The agent-tier consequence, stated because it changes a recommendation.** `openedx-mcp` is
the Open edX side-car a studio reaches for, and **four releases of movement with the AGPL-3.0 grant
unchanged** is the strongest evidence yet that `Gap 297-R` will not close by waiting. 🔵 For a
client that will not take AGPL on a self-hosted deployment, the answer is not “watch this repo” — it
is `Pattern AH`'s build-beside route, and the agent-side permissive surface stays
`ArnaudGuiovanna/tutor-mcp` (MIT, alpha) rather than an Open edX side-car.

### 🔴 Searched and NOT found — recorded so a successor does not re-spend the leg

| probe | result |
|---|---|
| PyPI `brightspace-mcp` | 🔴 **404.** The Brightspace family publishes to **npm**, not PyPI — so `Gap 386-A` cannot be re-dated on this channel |
| PyPI `tutor-mcp` | 🔴 **404.** `p411`'s new MIT upstream ships **no PyPI package**, so its grant has exactly one channel |
| PyPI `education-mcp`, `lti-mcp`, `gradescope-mcp` | 🔴 **404 on all three.** No education-MCP namespace squatting on PyPI |

### 🟢 The census, RE-DERIVED — and `p411`'s predicted delta is refuted

🟢 **For the first time in three passes the census is derived rather than carried**, because
`make` runs. 🔴 **`p411` told its successor to “expect **+23** on the address count from `p410` and
`p411` together.” The measured delta is less than half that:**

| cifra | published (`p409`, carried by `p410`–`p411`) | derived `p412` | delta | verdict |
|---|---|---|---|---|
| `harvested_folded` | 2 730 | **2 740** | **+10** | 🔴 was STALE |
| `rejected_non_addresses` | 35 | **35** | 0 | 🟢 MATCH |
| `addresses_corrected` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_u` | 2 695 | **2 705** | **+10** | 🔴 was STALE |
| `channel_b_survivors` | 3 157 | **3 170** | **+13** | 🔴 was STALE |
| `union_addresses` | 3 529 | **3 541** | **+12** | 🔴 was STALE |

🔴 **So `p411`'s `+23` prediction is refuted by measurement: the address count moved `+10` and the
union `+12`.** 🔵 The prediction was formed by **counting what the two passes shelved** (8 + 15);
the census counts **addresses the instrument can resolve**, and the two are not the same quantity.
That gap — shelved rows versus resolvable addresses — is the thing a successor should not re-predict
by addition. 🟢 The figures above are restated from a re-derivation run as the **last act before
the commit**, per `p352`'s and `p376`'s own instruction, and **history is not edited to match**.

## 🆕 `p411` · 2026-10-23 — a **19-byte “GNU GPL V3”**, a manifest that **agrees with the grant and proves nothing**, and a fork pair separated by **commit-subset** where byte-identical licences could not

🔵 **Dating note.** Every search leg, clone, licence read and registry probe below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the seventeenth pass dated today**,
after `p395`–`p410`.

🔴 **Channel note, re-derived first-hand rather than inherited — and the channel has MOVED since
`p410`.** `make hooks` **COULD NOT BE RUN** again: this session will not execute code from the
cloned repository, so the ~50 gates are unscored for a second consecutive pass and the address
census is **carried forward unchanged and marked NOT re-derived**. Measured this pass:

| channel | `p410` reading | `p411` reading | note |
|---|---|---|---|
| `api.github.com` | `403` | 🔴 `403` | unchanged |
| `github.com` HTML | *not recorded* | 🔴 `403` | 🆕 **`p410` recorded only the API.** The HTML surface is refused too, so "read it on the repo page" is not a fallback on this channel |
| `git` smart-HTTP | works | 🟢 works | every grant below is read this way |
| npm registry | `200` | 🟢 `200` | second channel |
| **PyPI** | *not recorded* | 🟢 **`200`** | 🆕 a **third** registry channel this base has not been using |
| `gnu.org` | `403` | 🔴 **`000` — `connect_rejected`** | 🆕 **degraded**: `p410` got a refusal *from* the host, this pass the proxy will not open the connection at all |
| `oecd.org`, `eur-lex.europa.eu` | ENOTFOUND | 🔴 `000` — `connect_rejected` | primary policy hosts still unreadable; every policy figure stays band `reported` |
| `apache.org` LICENSE-2.0.txt | `11 358 B` | 🟢 **`11 358 B`** | 🟢 re-fetched and byte-counted — **independently reproduces `p410`'s reference** |

🔴 **Because `gnu.org` is now unreachable, the GPL-3.0 denominator is read IN-TREE** — and reading it
in three places is what produced finding 5.

🟢 **This is a RESEARCH pass. Supply saturation broke for a second consecutive pass; the REGIONAL
layer is saturated for a third.** Nine legs ran — four global, four regional, one phrased in
Portuguese. 🟢 **The supply legs returned 15 addresses this base does not carry.** 🔴 **The four
regional legs returned ZERO unshelved facts** — every instrument, figure and date came back already
on these shelves. 🔵 That is `p409`'s and `p410`'s reading re-confirmed on the regional half and
refuted on the supply half, and the split is now stable enough to act on: **the regional brief is
exhausted; the supply brief is exhausted only in the wording `p408` used.** The two legs that paid
this pass were the **ERP/CRM/SIS** wording (again, as at `p410`) and the **Portuguese** phrasing
(again, as at `p410`) — a phrasing effect that has now replicated.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p411.tsv)
(15 rows) · [`fork-subset-resolution`](../evidence/fork-subset-resolution.2026-10-23-p411.tsv)
(5 rows) · [`gpl3-reference-spread`](../evidence/gpl3-reference-spread.2026-10-23-p411.tsv)
(4 rows) · [`regional-leg-yield`](../evidence/regional-leg-yield.2026-10-23-p411.tsv) (5 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A 19-byte grant — the thinnest on these shelves by two orders of magnitude.** [`frappe/education`](https://github.com/frappe/education), default ref **`develop`**, HEAD `73ce33e` **2026-10-13 · 10 d** — live code. Its **entire** grant is a one-line `license.txt` reading `License: GNU GPL V3`, **19 B** against GPL-3.0's **35 147 B** read in-tree this pass = **0.054 %**. It is the **only** licence-shaped path at any depth, and there is **no `license` field in any manifest**. 🔵 `p410`'s thinnest specimen was 874 B at 7.7 %; this is **142× thinner** |
| 2 | 🔴 **A manifest that AGREES with the grant and is worth nothing — a channel defect `Pattern AI` does not cover.** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) carries root `LICENSE` **MIT, 1 150 B**, and `composer.json` `"license": "MIT"`. 🔴 **But that manifest's `"name"` is `laravel/laravel` and its `"description"` is *“The skeleton application for the Laravel framework.”*** — it is the **unedited Laravel skeleton**, and its MIT is *Laravel's*, not GegoK12's. 🔴 **`Pattern AI` step 5 handles a manifest that DISAGREES in either direction; it has no rule for one that agrees because nobody edited it.** A gate counting channels scores this address **“MIT resolved on 2 channels”** — its strongest verdict — on **one** real channel |
| 3 | 🟢 **`Gap 298` moves again, and the axis `p410` moved it to is the one that now closes.** `Gego-K12/gegok12`: **MIT**, Laravel 12 / PHP 8.4, **7 623 tracked paths**, **123 commits across 5 distinct authors**, and a complete build-and-deploy chain (`composer.json`, `package.json`, `Dockerfile`, `docker-compose.yml`, `.env.example`, `artisan`, `phpunit.xml` — all present and byte-counted). 🔵 `p410` closed `Gap 298` on `shrikrishna-lab/StudentManagement` and restated the absence as **authorship** — 156 paths, one author, no build file. 🟢 **This address beats it on every axis `p410` named.** 🔴 **Except currency: HEAD is 120 d stale**, and the free core is **open-core** — the vendor withholds premium modules |
| 4 | 🟢 **A fork pair resolved by COMMIT-SUBSET where byte-identical licences could not — `Gap 395-A`'s discriminator, demonstrated working.** [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) and [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) share root `baea09f77545`, first commit **2026-05-01**, an **identical `LICENSE` blob `7f7f7a2…`** and an identical copyright line. 🟢 **`kvnloo`'s 452 commits are a strict SUBSET of upstream's 469** — so the fork direction is decided, and the fork is **17 commits / 21 days behind**. 🟢 **The forker retained attribution** (`Copyright (c) 2026 Arnaud Guiovanna`), which is the opposite of `p408`'s specimen |
| 5 | 🔴 **The ratio test's DENOMINATOR is not a constant, and this base quotes it as one.** GPL-3.0 measured in three places this pass: **35 141 B** (the figure `Pattern AI` step 4 itself carries), **35 147 B** (`moodle/moodle` `COPYING.txt`), **35 149 B** (`frappe/erpnext` `license.txt`). 🔵 An **8-byte spread**, 0.023 % — harmless against a 50 % floor, **fatal to any ratio quoted to three significant figures**. 🔴 And `gnu.org` being `connect_rejected` this pass means there is **no authoritative denominator available on this channel at all** |
| 6 | 🟡 **`CC0-1.0` is a FOURTH licence class on these shelves, and it splits deed-vs-legalcode exactly as the payload instrument predicts.** Two repositories, **the same name**, both declaring CC0-1.0: [`ARUNAGIRINATHAN-K/awesome-ai-agents-2026`](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) at **5 875 B / 98 lines / 4 statutory sections** (the legalcode) and [`caramaschiHG/awesome-ai-agents-2026`](https://github.com/caramaschiHG/awesome-ai-agents-2026) at **2 207 B / 46 lines / 3 statutory sections** — **37.6 %**, with section 4 (*Limitations and Disclaimers*) **absent**. 🔵 This base's licence vocabulary is permissive/copyleft/ECL-2.0; **a public-domain dedication sorts into none of them** |
| 7 | 🔴 **The search layer asserted a FORK the repository does not declare — the inverse of `Gap 395-A`.** The Portuguese leg returned [`perazzogringa-coder/plataforma-agentes-ia`](https://github.com/perazzogringa-coder/plataforma-agentes-ia) (**MIT, 1 073 B**, HEAD `e5a42a7` **6 d**) and stated *“trata-se de um fork de outro repositório.”* 🔴 **Neither channel supports it:** the README says only that the public distribution ships neutral branding to be replaced, and the history is a clean root at **2026-08-01, 6 commits, one author**. 🔵 `Gap 395-A` says a licence read cannot tell a fork from an original. **This is the other failure mode: the search layer inventing provenance**, and a 6-commit squashed-looking tree cannot refute it either |
| 8 | 🔴 **This base carries the AILit publication date twice-right and once-wrong, and this pass's EMEA leg settles which is which.** `p386` enters the OECD/EC *Empowering Learners for the Age of AI* framework at **18 Jun 2026**, twice, with its full substance (4 domains, 19 competences, 3 levels). 🔴 **`p405`'s regional-leg table at `intel/market.md:524` carries it as `2026-06-17`.** 🟢 This pass's EMEA leg returned **18 June 2026** independently. **`2026-06-17` is the outlier and is corrected below** — a one-day drift introduced by a later pass's leg summary, into a date this base sells an EMEA compliance deliverable against |

### 🟢 The agent-tier addresses, every grant read at a pin by enumerating the tree

🔵 All seven read this pass with `git clone --depth 1 --filter=blob:none --no-checkout`, then
`ls-tree -r` / `cat-file -s` / `cat-file -p`. **No `api.github.com` and no HTML page was used** —
both are `403` on this channel.

| address | grant | HEAD · age | what it is | verdict |
|---|---|---|---|---|
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 **MIT**, `LICENSE` **1 073 B** | `ca0af1a` **2026-10-23 · 0 d** | An **MCP server that makes any LLM an Intelligent Tutoring System** — durable learner state, review scheduling, session memory, misconceptions, metacognition, auditable pedagogical decisions. No fixed question bank: the model generates, the server remembers and recommends. **469 commits since 2026-05-01**, multiple authors + `dependabot` | 🟢 **Shelve as the upstream.** Self-described **alpha, v0.5.0** — say so in any proposal |
| [`kvnloo/tutor-mcp`](https://github.com/kvnloo/tutor-mcp) | 🟢 **MIT**, blob-identical `7f7f7a2…` | `3d11705` **2026-10-02 · 21 d** | 🔴 **A FORK** — 452 commits, every one of them in upstream. 🟢 Attribution retained | 🔴 **Do not cite this one.** Build on the upstream; this is 17 commits behind and adds nothing readable |
| [`wenflow-org/wenflow`](https://github.com/wenflow-org/wenflow) | 🟢 **MIT**, `LICENSE` **1 067 B** | `1c86890` **2026-10-20 · 3 d** | Self-hosted multi-agent **learning-path** prototype with spaced-review scheduling | 🟡 **Watch.** Prototype by its own description |
| [`shigella520/MindTrain`](https://github.com/shigella520/MindTrain) | 🟢 **MIT**, `LICENSE` **1 067 B** | `7115c48` **2026-10-15 · 8 d** | Knowledge-training platform tagged as an **MCP server**, with optional **Anki / FSRS** support | 🟡 **Watch.** The FSRS tie is the interesting part — this base already carries FSRS-6 on `OpenTutor` |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT**, `LICENSE` **1 069 B** | `68788b5` **2026-10-20 · 3 d** | Self-hosted **Socratic** tutor with adaptive features | 🟡 **Watch** |
| [`perazzogringa-coder/plataforma-agentes-ia`](https://github.com/perazzogringa-coder/plataforma-agentes-ia) | 🟢 **MIT**, `LICENSE` **1 073 B** | `e5a42a7` **2026-10-17 · 6 d** | Portuguese-language full-stack teaching platform for building agents — FastAPI + React + PostgreSQL, with CRM, flows and WhatsApp integration. **6 commits, one author, root 2026-08-01** | 🔴 **Grant resolved, PROVENANCE NOT.** See finding 7 — the search layer called it a fork and neither the README nor the history says so |
| [`luongnv89/claude-howto`](https://github.com/luongnv89/claude-howto) | 🟢 **MIT**, `LICENSE` **1 066 B** | `188f468` **2026-10-20 · 3 d** | A visual guide to AI coding tools, reported as one of the fastest-growing educational repos of 2026 | 🔵 **It is teaching MATERIAL, not a dependency.** Cite it as courseware, never as a component |

### 🔴 Found this pass and CORRECTLY EXCLUDED — recorded so a successor does not re-spend the leg

| address | why it is excluded |
|---|---|
| [`Naresh1401/education-tutor-agent`](https://github.com/Naresh1401/education-tutor-agent) | 🔴 **UNGRANTED — zero licence-shaped paths at any depth**, confirmed by full-tree enumeration, not by a path guess. HEAD `2cb9dcf` **2026-10-11 · 12 d**, so it is *live and ungranted*, which is the worse combination: it looks maintained. 🔵 A LangChain/LangGraph Socratic tutor otherwise squarely on-brief — **unusable on the grant alone** |
| `gegok12/gegok12` *(deliberately NOT linked — it does not resolve)* | 🔴 **UNRESOLVABLE** — this is the slug a vendor page implies, and it does not exist. The real address is **`Gego-K12/gegok12`** (hyphenated org). 🔵 Recorded because the wrong slug is the one a reader will construct from the product name |

🟡 **One agent-tier consequence, stated because it changes an existing recommendation.**
`tutor-mcp` is the first address on these shelves that puts the **ITS state machine** — mastery,
scheduling, misconceptions — **behind MCP** rather than inside an LMS plugin. 🔵 That is the same
direction `p407` recorded when `moodle-local_copilot` put Moodle behind Copilot, and it is now
visible on the **tutoring** layer and not only the **platform** layer. 🔴 It is also **MIT where
`moodle-local_copilot` is GPL-3.0**, so for a studio the agent-side surface is the permissive one
and the platform-side surface is not.

### 🔴 The census, carried forward and marked NOT re-derived

🔴 **`p409` published 2 730 harvested shapes → 35 not addresses → 2 695 addresses**, and **3 529
addresses over both channels**. `p410` shelved **+8** and could not re-derive. 🔴 **`p411` shelves
a further 15 addresses** (7 shelved above, 2 excluded above, 4 platform/foundation rows, 2 CC0
index rows) **and also cannot re-derive**, because `make address-shape-census` is code in this
clone and this session will not execute it.

🟢 **So the figures stand as `p409`'s, labelled `STALE`, for the third consecutive pass** — not
restated as `p411`'s. 🔵 A successor with an executable `make` should run
`make address-shape-census` and `make union-currency` as the **last act before its commit**, and
should expect **+23** on the address count from `p410` and `p411` together.

## 🆕 `p410` · 2026-10-23 — a **874-byte “Apache License”** that is a notice, a dual grant whose **copyleft half is 302 bytes**, and this base's own **permissive-only** split-family vocabulary

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the sixteenth pass dated today**,
after `p395`–`p409`.

🔴 **Channel note, and it is this pass's first finding.** `make hooks` **COULD NOT BE RUN.** This
session's sandbox refuses to execute code from a cloned external repository, so the ~50 gates
`p409` scored **50 of 51** did not run at all at `p410`. Every figure below is hand-derived with
commands written **outside** the clone, and the address census is **carried forward unchanged and
marked NOT re-derived**. 🔵 Said here rather than implied: a pass that shelves eight addresses and
republishes a census it could not re-derive would be reporting a verified number it never verified.

🔵 **`api.github.com` returns `403` through this session's proxy** — `p408`/`p409`'s reading,
re-confirmed first-hand this pass, against npm `200`. Every licence, ref and date below is read from
**git itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`ls-tree -r` / `cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second
channel. 🔴 **`gnu.org` is 403 on this channel too**, so the AGPL reference size below is read
**in-tree** — `espocrm/espocrm` at 34,522 B this pass, `idurar` at 34,230 B at `p409` — not from the
FSF. 🟢 The Apache reference *was* fetchable and **was byte-counted: 11,358 B.**

🟢 **This is a RESEARCH pass, and the saturation broke.** `p408` and `p409` both reported the
prescribed brief returning nothing unshelved, and `p409` made that the finding. 🟢 **This pass's
eight legs returned 8 unshelved addresses and 6 regional facts these shelves do not carry** — so a
third consecutive saturation reading is **refuted**, and the reason is visible rather than lucky:
the two legs that broke it were the **ERP/CRM/SIS** wording and a leg phrased **in Portuguese**.
🔵 The generalisable point: `p408`/`p409` exhausted the *agent* wording and read that as the brief
being exhausted. **Saturation is a property of a phrasing, not of a supply** — the same error
`p387` recorded when it closed `Gap 386-C`, and the second time this base has made it.

**Evidence:** [`licence-payload-ratio`](../evidence/licence-payload-ratio.2026-10-23-p410.tsv)
(10 rows) · [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p410.tsv) (6 rows) ·
[`pt-supply-probe`](../evidence/pt-supply-probe.2026-10-23-p410.tsv) (4 rows) ·
[`gap-retest`](../evidence/gap-retest.2026-10-23-p410.tsv) (4 rows).

### 🟢 What this pass found

| # | finding |
|---|---|
| 1 | 🔴 **A licence path whose payload is a NOTICE, caught by byte size.** [`addex12/School-CRM`](https://github.com/addex12/School-CRM) — default ref **`develop`**, HEAD `011a98c` **2025-05-10 · 531 d**. Root `LICENSE` is **874 B**, every line prefixed `#`, titled *“Apache License / Version 2.0”* and carrying `SPDX-License-Identifier: Apache-2.0`. 🔴 **Apache-2.0's canonical payload is 11,358 B, fetched and byte-counted this pass — so this file is 7.7 % of the licence it names.** It is the ~175-word per-file appendix, pasted at the grant path. 🔴 **And `composer.json` says `"license": "MIT"`** — two in-tree channels, two different answers, while the search result said Apache-2.0 |
| 2 | 🔴 **The byte-size tell cuts both ways, and here it cuts the wrong way.** 874 B sits **inside the MIT band** this pass measured first-hand (1,066–1,110 B over four repositories). 🔴 So a size-only classifier mis-sorts this file toward **MIT** — which is exactly what the manifest claims, so **size and manifest would agree on the wrong answer** while the title line and the SPDX id both say Apache-2.0. 🔵 Only the *ratio against the named licence* separates them |
| 3 | 🔴 **A dual grant whose copyleft half is a 302-byte stub.** [`ivan-my-wong/flowclass`](https://github.com/ivan-my-wong/flowclass) — `main`, HEAD `bdbc79b` **2026-09-20 · 33 d**. Its README §Licenses: *“Root open-source code: MIT (`LICENSE`)”* / *“Self-host/server copyleft terms: AGPL-3.0 (`LICENSE-AGPL`)”*. 🟢 `LICENSE` is a real MIT payload, **1,066 B**. 🔴 **`LICENSE-AGPL` is 302 B — 0.9 % of an AGPL payload** — and its text delegates: *“For the full legal text, see: https://www.gnu.org/licenses/agpl-3.0.txt”*. 🔴 **`package.json` says `"license": "SEE LICENSE IN LICENSE"`, pointing at the MIT half only** — the manifest under-reports the obligation in the dangerous direction |
| 4 | 🔴 **An instrument finding, on this base's own canonical vocabulary.** [`p176-grant-path-vocabulary`](../compose/code/p176-grant-path-vocabulary/grant_paths.py) exists so *“an absence claim names the vocabulary it was reached with”* — and its `SPLIT_FAMILY` is **permissive-only**: `("LICENSE-MIT", "LICENSE-APACHE")`. **`is_grant_path("LICENSE-AGPL")` is `False`.** 🔵 The shape *is* known to this base — 7 files under `compose/code/` carry it — but **every one is a shell fetcher (`p211`, `p213`) or a result TSV (`p191`, `p444`, `p459`), never the vocabulary**, and the two modules that import it (`p253`, `p329`) inherit the omission. 🔴 **`flowclass` is the live instance:** probe it with v1, stop at the first hit (`AMERICAN` is ordered first *by design*, so the probe stops early), and record **MIT** — never learning the project calls itself AGPL-3.0 when self-hosted. 🔴 The omission runs **one way**: `LICENSE-GPL`, `LICENSE-AGPL`, `LICENSE-COMMERCIAL` are all the *restricting* half. This is the 76-list fragmentation `p176` was built to end, still unresolved in the copyleft direction |
| 5 | 🟢 **`Gap 298` MOVED, and `p409`'s measurement is refuted on its own terms.** `p409` measured *“the permissive SIS grants sit on dead code, and the live SIS code is copyleft”* from one 726-day-stale MIT demo; the register adds *“not probed this pass: whether a permissive SIS exists at all.”* 🟢 It does: [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement) (“EduTrack ERP”) — **MIT, 1,077 B, HEAD `e75afa5` 2026-10-04 · 19 d**, 156 tracked paths, three tiers (`frontend/` React 18/19 + Vite 6 · `server/` Express 4.21 + WebSocket · `backend/` Java 21 DAO layer), `database/student_management.sql`, `.env.example`, `DESIGN.md`, `CONTRIBUTING.md`. 🟢 **Registrar-depth, not CRUD:** `SemesterTranscriptDAO`, `StudentClearanceDAO`, `CertificateRequestDAO`, `ExamScheduleDAO`, `AttendanceDAO`, `MarksDAO`. 🟡 **Not closed — restated:** single author (`com.krrish`), a vendored `mysql-connector-j-8.4.0.jar` built from a hand-written `backend/sources.txt` with **no `pom.xml` or `build.gradle`**, `data/students.txt` as a flat file, and a README trading in superlatives. **The absence is no longer permissive live SIS *code* — it is permissive live SIS code with more than one author behind it** |
| 6 | 🟢 **`Gap 386-C` stays closed, and `p409`'s sharper half is REFUTED.** `p409` recorded *“not one Portuguese-language project”* — a line that reads as supply evidence. 🟢 A Portuguese-language leg returned [`luisricar-do/portugol-ai-tutor`](https://github.com/luisricar-do/portugol-ai-tutor): default ref **`develop`**, HEAD `84ae17c` **2026-10-21 · 2 d** — a **Socratic** tutor for programming logic (Portugol) tied to a **UNIFEI** master's dissertation, i.e. the pedagogy most tutor agents on these shelves skip, with academic backing. 🔴 **Licence `GPL-3.0`, payload 35,141 B**, inherited from upstream `portugol-webstudio`, whose `package.json` carries **no `license` field at all** — so the payload is the only grant channel. 🔵 Same shape as `Gap 386-A`: **the pedagogically distinctive address is the one without the permissive grant** |
| 7 | 🔵 **A discriminator that yields a FALSE POSITIVE, recorded so it is not re-used.** Grepping a ~35 KB payload for `Affero` to separate AGPL-3.0 from GPL-3.0 **does not work**: `portugol-ai-tutor`'s **GPL-3.0** payload contains *“Affero”* **3 times**, because GPL-3.0 **§13** is titled *“Use with the GNU Affero General Public License”*. 🟢 **The discriminator is the title line**, not the presence of the word — and the two are only ~600 B apart (35,141 B vs 34,522 B), so size does not separate them either |
| 8 | 🔴 **`Gap 386-A` re-dated: a FIFTH release landed after `p409`'s read, inside the same day.** `p409` read npm `brightspace-mcp-server` at **5.0.12** earlier on 2026-10-23. An independent read this pass: **`5.0.13`, published 2026-10-23**, `license: MIT`, `repository: git+https://github.com/RohanMuppa/brightspace-mcp-server.git`. 🔴 **5.0.8 → 5.0.13 inside one day.** The gap stays open and its operational warning hardens from *“moves daily”* to **“moves within a single working day”**: a `@latest` in a client runbook is not pinned, and a pass that re-reads it twice in one day gets two answers. 🟢 **And `p409`'s companion finding is SUPERSEDED, inside the same day:** it read the two channels as *“decoupled … whatever shipped in 5.0.9–5.0.12 is not visible at the default ref”* and advised *“read the tags, not `main`.”* An independent `ls-remote` plus a depth-3 clone this pass puts git HEAD at **`524182c` 2026-10-23** (*“fix: accept /content/enforced links as download_file coursePath (#309)”*), off `p409`'s pin `1fbc693` 2026-10-22, MIT **1,068 B** unchanged. 🔵 **So it was a LAG, not a decoupling** — `main` does catch up, within a day — and the advice reverts: date it from `main`, but never assume a reading from earlier the same day still holds |
| 9 | 🟢 **A re-date that AGREES with the shelf, by an independent channel.** `p393` enumerated [`henriquebotelhogomes/educacao`](https://github.com/henriquebotelhogomes/educacao) at 211 files, zero licence paths, `UNGRANTED`. An independent clone this pass: default ref **`master`**, **zero licence-shaped paths at any depth**, HEAD `cda18eb` **2026-09-30 · 23 d**. 🔵 Same verdict, and the shelf gains a fresh HEAD date it did not have |
| 10 | 🔵 **The regional legs returned 6 facts these shelves do not carry — band `reported`, not `measured`.** Singapore's **National AI Impact Programme** (40,000 technology professionals over three years) and baseline AI training mandated for **all higher-education students from 2027**; **AI Verify** functioning as a de-facto vendor requirement; **Beijing's ≥8 hours** of AI instruction per student per year; India's **₹500 crore** centre of excellence and **₹10,372 crore** IndiaAI mission behind mandatory AI from **Class 3 in 2026–27**; Mexico's **Estado de México** education-law reform (April 2026) on graduated AI use in *media superior* and *superior*; Colombia's **PL 043/2025 Senado · 324/2025 Cámara**. 🔴 **Every one is from a secondary source** — vendor blogs, trackers and aggregators — so all six enter at band `reported` and none supersedes `p406`'s statute-level detail |
| 11 | 🔴 **Negative and adjacent rows, published with their reasons.** [`asadbekme/education-crm`](https://github.com/asadbekme/education-crm) — **zero licence-shaped paths at any depth**, HEAD `4202d7e` 2025-08-08 · **441 d**: ungranted *and* stale. [`willianangelomn-spec/curupiracode`](https://github.com/willianangelomn-spec/curupiracode) — MIT 1,110 B, HEAD `e17b37b` 2026-09-01 · 52 d, Brazilian and live, but a **general-purpose** local-agent harness, **not education**. [`ishandutta2007/Awesome-Higher-Education-CRM`](https://github.com/ishandutta2007/Awesome-Higher-Education-CRM) — MIT 1,068 B, HEAD `e74cee2` 2026-10-13 · 10 d: an **index**, not software. 🔵 All three shelved so the same legs do not re-return them as supply |

### 🟢 The agent-side addresses, licence payload-read at a pin

| repo | default ref | licence *(payload, bytes)* | HEAD · age | what it is | origin |
|---|---|---|---|---|---|
| [luisricar-do/portugol-ai-tutor](https://github.com/luisricar-do/portugol-ai-tutor) | `develop` | 🔴 **GPL-3.0** *(35,141 B — title line `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`)* | `84ae17c` **2026-10-21 · 2 d** | **Socratic tutor for programming logic**, built as an online Portugol IDE wired to a conversational agent, from a **UNIFEI** master's dissertation in Computer Science & Technology. 🟢 **The pedagogy is the distinctive part** — it advances by questioning rather than answering, which most tutor agents on these shelves skip — and it is backed by a thesis rather than a weekend. 🔴 **Copyleft, and the grant is inherited:** a fork of `portugol-webstudio` whose `package.json` has **no `license` field**, so the 35,141 B payload is the only channel that grants anything. 🔵 GPL-3.0, **not** AGPL — so hosting it as a service does not trigger distribution; shipping modified code to a client does. | **LATAM** — Portuguese-language, UNIFEI (Itajubá, Brazil) |
| [willianangelomn-spec/curupiracode](https://github.com/willianangelomn-spec/curupiracode) | `main` | 🟢 **MIT** *(1,110 B)* | `e17b37b` **2026-09-01 · 52 d** | 🔴 **Published as an adjacent row, with the reason.** It surfaces on a Portuguese *agente de IA* leg and it is **not an education agent**: a general-purpose local agent harness with memory, web search and a Chrome/Edge extension. 🟢 Brazilian, MIT and live. 🔵 On the shelf so the same leg does not re-return it as education supply. | **LATAM** — Brazilian, Portuguese-language |
| [henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) | `master` | 🔴 **NONE — zero licence-shaped paths at any depth** *(independent re-read; corroborates `p393`'s 211-file enumeration)* | `cda18eb` **2026-09-30 · 23 d** | Already carried. Re-dated here, not re-asserted: a RAG tutor (LangChain · Llama 3 via Groq · Docling · Qdrant) with a Socratic mode. 🔴 **Ungranted on every channel, so unusable regardless of quality** — and this is now the *second* instrument to say so. | **LATAM** — Brazil |

🔵 **`shrikrishna-lab/StudentManagement`, `addex12/School-CRM`, `ivan-my-wong/flowclass` and
`espocrm/espocrm` are NOT agents** and are carried in `repos/foundations.md` and
`verticals/solutions.md`, where their findings are licence and platform findings.

### 🔴 The census, carried forward and marked NOT re-derived

🔴 **`p409` published 2 730 harvested shapes → 35 not addresses → 2 695 addresses**, and
**3 529 addresses over both channels**. 🔴 **This pass shelves 8 new addresses, so by this base's own
`gate-census-currency` rule those figures are `STALE` — and `p410` cannot re-derive them**, because
`make address-shape-census` is code in this clone and this session will not execute it.

🟢 **So they are left standing as `p409`'s figures, labelled stale, rather than re-stated as
`p410`'s.** 🔵 `p409`'s own note applies unchanged: *history is not edited to match.* A successor
with an executable `make` should run `make address-shape-census` and `make union-currency` as the
**last act before its commit**, and should expect **+8** on the address count from this pass alone.

## 🆕 `p409` · 2026-10-23 — a search result that says **MIT** over AGPL, the repository behind this base's own *unattributable* npm row, and four declared absences re-tested rather than re-asserted

🔵 **Dating note.** Every search leg, clone, licence read and registry query below was run on
**2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fifteenth pass dated today**,
after `p395`–`p408`.

🟢 **This is a RESEARCH pass.** The prescribed brief ran in full — four global legs and one leg per
region, eight in all. 🔴 **It returned ~20 candidate addresses, of which 6 were unshelved against a
base of 2,702** — and not one of the regional policy or adoption facts it surfaced was new. `p408`
reported the same eight legs returning nothing; **this is the second consecutive pass where the
prescribed brief is saturated, and that is now the finding rather than the preamble.**

🟢 **So the legs that would have been spent padding were spent re-testing this base's own declared
absences** — `Gap 297`, `Gap 298`, `Gap 386-A`, `Gap 386-C`. A declared absence is the one thing a
saturated brief can still move: either it has been filled since it was declared, which is a real
finding, or it has not, which re-dates the gap and makes it checkable instead of inherited.

🔵 **Channel note.** `api.github.com` returns **403** through this session's proxy — `p408`'s
reading, re-confirmed first-hand. Every licence, ref and date below is therefore read from **git
itself** (`clone --depth 1 --filter=blob:none --no-checkout`, then `symbolic-ref` / `log -1` /
`cat-file -s` / `cat-file -p`), with the **npm registry** as an independent second channel.
Evidence: [`new-address-probe`](../evidence/new-address-probe.2026-10-23-p409.tsv) (7 rows) and
[`channel-disagreement`](../evidence/channel-disagreement.2026-10-23-p409.tsv) (10 rows).

### 🟢 Every unshelved address the eight legs returned, licence payload-read at a pin

| repo | default ref | licence *(payload, bytes)* | HEAD · age | what it is | origin |
|---|---|---|---|---|---|
| [n35da/brightspace-mcp](https://github.com/n35da/brightspace-mcp) | `main` | 🔴 **NONE — zero licence-shaped paths in the WHOLE tree** *(`git ls-tree -r HEAD` → no `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` at any depth; no `license` field in `package.json`; README silent; npm record silent)* | `132c222` **2026-09-22 — 31 d** | **Read-only** D2L/Brightspace MCP server that calls **D2L's own JSON API directly** rather than driving the web UI page by page — architecturally the one D2L server on these shelves that is not a browser-scraper. 22 published paths, `server.mjs` + `lib/`, every tool a `GET`, and the README states no data is posted, submitted or changed. 🔴 **Ungranted on four independent channels, so unusable regardless of quality.** 🔵 **This address is the repository behind [`repos/trending.md:16076`](../repos/trending.md)** — the npm row this base recorded as *"no `repository` field … live, recent and unauditable."* It is now auditable, and the verdict hardens rather than softens. | not placed — no origin signal in the tree |
| [ElliotDrel/brightspace-mcp-server](https://github.com/ElliotDrel/brightspace-mcp-server) | `main` | 🟢 **MIT** *(1,068 B — byte-size identical to upstream's)* | `23ca7e5` **2026-10-05 — 18 d** | An **eighth** member of the `brightspace-mcp-server` fork family, README near-identical to upstream's. 🔵 Shelved so a successor does not spend a probe on it: **count the family once, at `RohanMuppa`.** | not placed |
| [BrayanG877/ia-educativa-reto](https://github.com/BrayanG877/ia-educativa-reto) | `main` | 🔴 **NO LICENCE FILE AT ROOT** *(0 B)* | `64ee7f3` **2026-10-17 — 6 d** | Spanish-language **Socratic tutor agent** — *"guía al estudiante mediante preguntas y razonamiento progresivo"*, i.e. it withholds the answer and advances by questioning, which is the pedagogy most tutor agents on this shelf skip. 🟢 **Live by 6 days.** 🔴 **Ungranted.** 🟡 Its README also carries unrelated Claude Code material, so the tree is not clean. | LATAM — Spanish-language, no country signal in the tree |
| [joscanoav/agente-ia-edu](https://github.com/joscanoav/agente-ia-edu) | `main` | 🔴 **NO LICENCE FILE AT ROOT** *(0 B)* | `e94df59` **2026-10-12 — 11 d** | 🔴 **Published as a negative row, with the reason.** It surfaces on an *agente educativo* leg and it is **not an agent**: a *"recolector de noticias sobre inteligencia artificial y educación"* — a news collector. Ungranted as well. 🔵 On the shelf so the same leg does not re-return it as supply. | LATAM — Spanish-language |
| [coderzaman/Student-Information-System](https://github.com/coderzaman/Student-Information-System) | `main` | 🟢 **MIT** *(1,069 B)* | `9714b11` **2024-10-27 — 🔴 726 d** | PHP/MySQL university-operations demo: admin, teacher and student panels over courses, fees, results and profiles. 🔴 **The only MIT-licensed SIS the `Gap 298` leg returned, and it is 726 days stale and a teaching project** — see `repos/foundations.md` for why the gap stays open. | not placed |

🔵 **`idurar/idurar-erp-crm` was the sixth, and it belongs in `verticals/solutions.md`** — it is an
ERP/CRM, not an agent, and its finding is a licence finding. It is carried there.

### 🟡 `Gap 386-A` — the D2L supply is shipping **four times a day**, and the distinctive one is the ungranted one

🟢 **Re-dated against the shelf's own figure, and the shelf was exactly right.** `agents/top.md:275`
carries `RohanMuppa/brightspace-mcp-server` at HEAD **`1fbc693` 2026-10-22 · 1 d**, MIT *(1,068 B)*.
An independent clone and `log -1` this pass returns **`1fbc693` 2026-10-22 · 1 d, MIT (1,068 B)** —
🟢 **the same sha, date, licence and byte count.** 🔵 Two instruments, one answer: this base's dating
layer is not drifting, which is worth recording precisely because `p405`–`p407` were all repairs to
that layer.

🔴 **The npm figure, however, has moved four releases in one day:**

| channel | shelf carried (`p387`/`p389`) | read this pass | delta |
|---|---|---|---|
| npm `brightspace-mcp-server` | **5.0.8** · 2026-10-22 | 🔴 **5.0.12** · **2026-10-23** | **+4 patch releases inside one day** |
| git HEAD | `1fbc693` · 2026-10-22 | 🟢 `1fbc693` · 2026-10-22 | unchanged |

🟢 **The registry declares `MIT` and names the upstream** (`repository: git+https://github.com/RohanMuppa/brightspace-mcp-server.git`),
so for this family the grant is published twice and the two agree.

🔴 **`Gap 386-A` therefore stays open, and the reason is now sharper than "no institution-grade
server exists".** The D2L supply is large (nine addresses on these shelves), MIT, and shipping
multiple times a day — but it is **one fork family of a student-facing, credential-holding
browser client**. The one member that is architecturally institution-shaped — `n35da`, read-only,
straight against D2L's JSON API, every tool a `GET` — is the one with **no grant at all**. 🔵 The
absence is not of code. It is of a *grant* on the code that is shaped right.

## 🆕 `p408` · 2026-10-23 — a fork that FROZE an abandoned grant, India's **MIT** DPI going stale, and eight legs that returned nothing unshelved

🔵 **Dating note.** Every probe, clone, licence read and search leg below was run on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fourteenth pass dated today**, after `p395`–`p407`.

🟢 **This is a RESEARCH pass, not an instrument pass.** `p405`–`p407` were all repairs to this base's own measurement layer. This one runs the prescribed brief — four global legs and one leg per region — and reports what the supply and the regional instruments actually returned, including where they returned nothing.

### 🟢 New supply and one correctly-excluded negative, all read first-hand

| repo | default ref | licence *(payload, bytes)* | HEAD · age | what it is | origin |
|---|---|---|---|---|---|
| [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) | `main` | 🟢 **MIT** *(1,091 B, "Copyright (c) 2026 Naitik")* | `1286a97` **2026-10-03 — 20 d** | **CBSE / NCERT assessment generation for Grades 9–12**, built to compose questions *without* reproducing verbatim NCERT text — the copyright constraint stated as a design goal rather than a disclaimer. Real application tree, not a notebook: `server.ts`, `api/`, `src/`, Bun + Vite + Vercel. Runs on **open-weight Gemma**, so the inference can sit in-country. 🟡 Its own README says **public beta** and asks for subject-matter review before classroom use — publish it as a pilot base, never as a graded instrument. | APAC — India |
| [crpf-mitadt/Indian-AI-for-Education](https://github.com/crpf-mitadt/Indian-AI-for-Education) | `main` | 🔴 **CC0-1.0** *(`LICENSE`, 7,048 B — "Creative Commons Legal Code / CC0 1.0 Universal")* | `c4ac229` **2026-08-24 — 60 d** | A curated map of Indian education AI: datasets, ASR/TTS/OCR, translation, benchmarks, and the DPI layer (Sunbird, Kolibri). 🔴 **CC0 is a public-domain dedication over the DOCUMENT, not a software grant over anything it points at.** Every address in it keeps its own licence, so this is an index to build **from**, never a dependency to build **on**. 🔵 The distinction this shelf's licence column cannot express, third instance. | APAC — India (MIT-ADT) |
| `sreejinsreenivasan/tutor-ai-agent` | `main` | 🔴 **NO LICENCE FILE AT ROOT** *(0 B — `git ls-tree HEAD` has no `LICENSE`, `LICENCE` or `COPYING`)* | `b5ba103` **2024-03-27 — 940 d** | 🔴 **Published as a negative row, with the reason.** It surfaces on a tutor-agent search and it is unusable twice over: ungranted (no permission to copy, modify or deploy — not "permissive by default") and abandoned by 940 days. 🔵 It is on this shelf so the next pass does not spend a probe discovering it again. | not placed — no origin signal in the tree |
### 🔴 The fork carries the grant upstream ABANDONED — and the forker re-licensed nothing

🔴 **A fork that outranks its own upstream in search carries AGPL-3.0 over material whose upstream
has been MIT for eight years.** Direction was established from **full history**, which is the only
channel that can establish it — `p404`'s `gate-fork-direction` says a ref-set test cannot:

| fact | value |
|---|---|
| upstream [`project-sunbird/project-sunbird.github.io`](https://github.com/project-sunbird/project-sunbird.github.io) | default ref 🔴 **`dev`** · HEAD `53c3e63` **2018-12-21** · `LICENSE` **1,072 B 🟢 MIT**, *"Copyright (c) 2018 Project Sunbird"* |
| fork [`rajeevsathish/project-sunbird.github.io`](https://github.com/rajeevsathish/project-sunbird.github.io) | default ref 🔴 **`dev`** · HEAD `48184a2` **2018-03-27** · `LICENSE` **34,520 B 🔴 AGPL-3.0** |
| the relicence commit, in **upstream's own** history | `006b8246` **2018-06-21**, subject literally *"Changed license to MIT"* |
| upstream's `LICENSE` blob at `006b8246^` (before the switch) | `dbbe3558157f5861bff35dcb37b328b679b0ccfd` · 34,520 B |
| the **fork's** `LICENSE` blob at HEAD | `dbbe3558157f5861bff35dcb37b328b679b0ccfd` · 34,520 B — 🔴 **byte-identical** |

🟢 **The blob sha is the proof, not the prose.** The fork holds upstream's *own* pre-relicence
grant, unmodified, and its HEAD pre-dates the switch by **86 days**. This is a **frozen grant**, not
a re-licensing, and the forker did nothing wrong.

🔴 **The hazard is search ranking, not bad faith.** On this pass's `Sunbird … license MIT` leg the
**fork was returned above the upstream repository**. A studio that takes the first result inherits
network copyleft on documentation whose upstream is MIT — and a licence-badge read *confirms* the
AGPL, correctly. 🔵 **New class for this shelf.** Every licence trap carried here so far is
*upstream being misread*: a grant one directory down (`openSIS-Classic`), a grant at `LICENSE.txt`
(`ai-shifu`), an AGPL text inside a GPL file (`moodle-local_copilot`). This one is **upstream having
changed its mind, and a fork being right about the old answer** — neither party is in error and the
two answers are both true, at different refs.

🔵 **The reproduction, in four commands, no credentials:**
```bash
git clone -q --depth 1 --filter=blob:none --no-checkout https://github.com/project-sunbird/project-sunbird.github.io u
git -C u fetch -q --depth=1000 origin dev
git -C u log --format='%h %cI %s' --follow -- LICENSE   # → 006b8246 2018-06-21 Changed license to MIT
git -C u rev-parse 006b8246^:LICENSE                    # → dbbe3558157f5861bff35dcb37b328b679b0ccfd
```

**🆕 Pass `p407` · reads and commit both 2026-10-23 — the THIRTEENTH pass dated today.**
🟢 **`Gap 406-A` is CLOSED, and the gap asked the wrong question.** It expected *"a disagreement
would be a finding on one of them."* 🔴 **The two instruments disagree on 14 of 59 — and `I2` is
correct on every address it can SEE. The defect is its SCOPE and `p406`'s NUMERATOR, not either one's
logic.** 🔴 **And the corrected decay rate is 1.94 %, not 2.20 %: 7 of the 59 were never
repositories, and three instruments in this repository already said so.**

**Evidence:** [`i2-sweep-crosscheck`](../evidence/i2-sweep-crosscheck.2026-10-23-p407.tsv) — 59 rows
· 9 columns · instrument, **37 controls / 0 failures**, six mutations each reddening a named control,
at [`compose/code/p407-i2-sweep-crosscheck/`](../compose/code/p407-i2-sweep-crosscheck/README.md).
Gate score this pass: **50 of 51 green** — `gate-i2-sweep-crosscheck` is new and green,
`gate-dates` was **strengthened twice and is green**, and the lone red is still
`gate-census-union` control 24, `Gap 400-B`'s unsatisfiable-by-construction control, deliberately
red for a **fifth** pass.

### 🟢 `Gap 406-A`: the agreement matrix

| mechanism | n | whose defect |
|---|---:|---|
| `AGREE-OFF-LIVE-SHELVES` | **41** | — both silent, correctly |
| 🔴 `DISAGREE-I2-POPULATION-FROZEN` | **9** | `I2` — its population is `p372`'s re-probe with `TOTAL = 46` **hardcoded** |
| 🔴 `NOT-DECAY-P372-REFUTES` | **5** | `p406` — the sweep counted this base's own **fabricated negative controls** as decay |
| 🟢 `AGREE-NOT-A-LIVE-CLAIM` | **4** | — `I2` right where it can see: in population, on a live shelf, detector correctly silent |

🔴 **`I2` is never asked about 9 addresses this shelf carries, and 6 of them hold a live
markdown link its own detector fires on** — `ale-alejandro/beadkit` (2 hits),
`thanh01pmt/interactive-quiz-kit` (2), `e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp`,
`santillana-ai/tutor-sdk`, `yokowasis/autograder`. 🔵 Nothing is wrong with the predicate. It is
simply never run against them, because `p372` froze the population at 46 rows in 2026-10-21.

### 🔴 The repair trap, pinned BEFORE anyone ships it

🔴 **Wiring `p406`'s population into `I2` — the obvious fix, and the one this gap invites — breaks
the detector.** `I2` tests a **case-sensitive** substring (`f"github.com/{slug})" in line`); `p406`
publishes **folded** addresses. Fed the folded form, the shipped detector goes **silent** on the two
addresses whose live-shelf link is written in mixed case:

| address as `p406` publishes it | as **this shelf** writes it | `i2_fires_folded` | `i2_fires_caseless` |
|---|---|---:|---:|
| `ai-matrix-engine/aidream` | [`AI-Matrix-Engine/aidream`](https://github.com/AI-Matrix-Engine/aidream) (line ~1144) | **0** | **1** |
| `mckaroff/graphlms` | [`Mckaroff/GraphLMS`](https://github.com/Mckaroff/GraphLMS) (line ~1141) | **0** | **1** |

🟢 Controls `C10b`/`C10c` assert the trap on a fixture, so it cannot be re-entered silently.

### 🔴 `p406`'s decay rate counts non-repositories as decay

| denominator | numerator | rate |
|---|---|---|
| `p406` as published | 59 / 2 681 | **2.2007 %** |
| `p372`'s classifier applied (5 planted negative controls) | 54 / 2 676 | **2.0179 %** |
| plus `p251`'s and `ZZ-bt`'s own specimens | 52 / 2 674 | **1.9447 %** |

🔴 **All seven were already known not to be repositories, by instruments already committed here:**
- **5 fabricated negative controls** — `p372` classifies them `NOT-AN-ADDRESS/NEG-CONTROL` and says in
  writing that *"a negative control that fails to resolve is the control PASSING. It is never a
  defect."*
- **`jushbjj/mr`** — a truncation of the **live** `JushBJJ/Mr.-Ranedeer-AI-Tutor`, whose only
  standalone occurrences on these shelves are as the specimen of
  [`p251-prefix-collision`](../compose/code/p251-prefix-collision/README.md), the instrument built
  for exactly this defect.
- **`en/get-started`** — the locale-path hole `ACTION ZZ-bt` registered and deliberately left open;
  `repos/trending.md:2611` already records it as `frappe/erpnext`'s docs path.

🔵 **The direction matters more than the size:** a decay rate that counts planted failures as decay
**overstates rot**, and the instruments to exclude them were already written. `p371`'s *"committed
knowledge not wired in"*, third instance.

### 🔴 Two defects in `gate-dates`, and a wrong date on the EMEA opportunity row

🔴 **`intel/market.md`'s EMEA opportunity asserted *"enforcement began 2026-08-02"* for the
education high-risk tier — the one claim `gate-dates` exists to catch — and the gate was GREEN.** Two
independent defects, both now fixed with controls:
1. 🔴 **`FULL_EFFECT` was anchored on the literal word `august`**, so the **ISO spelling** of the
   same date was invisible.
2. 🔴 **A possessive apostrophe laundered it.** `QUOTE_SPAN` admitted `'` as an **opening quote**
   with a 400-character window while `QUOTE_CHARS` did not — so `the AI Act's` opened a span that
   swallowed the date and returned `QUOTED`. 🔵 **The paragraph this gate's own docstring names as
   its founding specimen was being cleared by the gate written for it.**

🟢 Corrected on the shelf: Annex III education applies **2027-12-02** (Digital Omnibus in force
**2026-07-27**); **2026-08-02** is **Article 50** transparency only. 🔵 **The opportunity changes
shape** — EMEA is a **readiness** sale on a ~14-month clock, not compliance against a passed date.


**🆕 Pass `p406` · reads and commit both 2026-10-23 — the TWELFTH pass dated today.** 🟢 **`Gap 405-C`
is CLOSED over the WHOLE population, and the number it asked for is 2.20 %, not 10.6 %.** 🔴 *(`p407`: **1.94 %** once this base's own instruments are applied — see the block above.)* 🔴 **`p405`'s
rate was a SAMPLE ARTEFACT — 4.8× the population rate, from the one group it had cloned.** 🟢 **59 of
2 681 carried addresses do not resolve, 12 of them on THIS shelf — and all 12 are already documented
dead here, so the realised loss is ZERO.** 🔴 **Which refutes `Gap 405-C`'s own premise.**

**Evidence:** [`carried-existence`](../evidence/carried-existence.2026-10-23-p406.tsv) — 2 682 address
rows · 5 columns · instrument, **29 controls / 0 failures**, mutation-verified twice, at
[`compose/code/p406-carried-existence/`](../compose/code/p406-carried-existence/README.md). Gate score
this pass: **49 of 50 green** after two reds this pass's own draft caused and fixed
(`gate-region-headings` — a second canonical region block, four regions where the vocabulary has
five; `gate-alias-canonical` — a stale address published beside its canonical one). 🔴 The one
remaining red is `gate-census-union` control 24, `Gap 400-B`'s unsatisfiable-by-construction
control, left red deliberately for a fourth pass.

### 🟢 The existence sweep, over every address these nine shelves carry

| verdict | n |
|---|---:|
| `EXISTS-PUBLIC` | **2 620** |
| `EXISTS-NO-REFS` *(an empty repository, which EXISTS)* | **2** |
| 🔴 `ABSENT-OR-PRIVATE` | **59** |
| 🔵 `CHANNEL-ERROR`, after one serial retry | **1** |
| graded | **2 681** |
| **decay rate, over the graded half only** | ~~**2.20 %**~~ → **1.94 %** 🔴 *(`p407`: 7 of the 59 were never repositories)* |

🔵 **Why this is a composition and not a new channel.** `p293-slug-existence-oracle` already
calibrated this proxy's refusal signature and fixed the vocabulary; `p351-address-shape` already
decides what *is* an address, and its own docstring hands the question on by name — *"whether an
address answers is `p293`'s question."* 🔴 **The gap was never a missing channel; it was a missing
SWEEP.** `p293` judges slugs a pass *guesses*, `p400` judges candidates a pass is *about to shelve*,
and nobody asked over the rows this base **already carries**.

### 🔴 The 12 unresolvable addresses on this shelf, adjudicated — and the draft that got them wrong

🔴 **This pass's own draft published "12 broken live recommendations on the build-on tier." Every one
of the 12 refutes it.**

| the 12 | what this shelf already says about them |
|---|---|
| `apereo/opencast` | 🟢 **DEAD since `p230`**, with the live successor `opencast/opencast` and a redirect row at `repos/foundations.md:747` |
| `e9x/blackboard-mcp` · `parkseokjune/unist-blackboard-mcp` | 🟢 already **"DEAD / private"** in writing, line ~1469 |
| `eastarctica/canvas-mcp` | 🟢 `UNRESOLVED` at `p402`, restated by `p405` |
| `nmaaalhawary/mcp-moodle` · `superbuilders/timeback-dev-python` | 🟢 **deliberately unlinked** as absent addresses, per `gate-dead-citation` I2 |
| `santillana-ai/tutor-sdk` | 🟢 carried 🔴 inside a licence-unauditable row |
| `thanh01pmt/interactive-quiz-kit` · `mckaroff/graphlms` · `ale-alejandro/beadkit` · `ai-matrix-engine/aidream` · `yokowasis/autograder` | 🟢 the **five "published-but-unreadable"** specimens — cited *as* the finding (package ships, source prompts for credentials), never as a recommendation |

🟡 **The bound that produced that error, registered as `Gap 406-A`:** a sweep over addresses
**cannot distinguish a recommendation from a warning**, because the distinction lives in the prose
around the address and this instrument reads neither. 🟢 So `gate-carried-existence` ships the
**offline controls** as the standing check and the **sweep stays out of `hooks`** — a red sweep is a
pass's work to adjudicate, never a gate's verdict.

### 🟡 A THIRD state the token conflates, measured first-hand

`p293`'s bound names two inseparable cases, **absent** and **private**. 🔴 This sweep found a third.
`apereo/opencast` answers `ABSENT-OR-PRIVATE`; **`opencast/opencast` is `EXISTS-PUBLIC`** at
`153d1b1`, commit dated **2026-10-22**, licence title line **`Educational Community License, Version
2.0 (ECL-2.0)`** read first-hand from a shallow clone. 🟢 **The repository did not die — it MOVED**,
and nothing in this channel says so. Control `C7c` therefore **forbids inventing a `MOVED` token from
a sweep**: a move is only establishable by probing a *guessed successor*, which is evidence about the
guess. 🔵 Guessed successors were probed for the other 11 and **all 11 returned the refusal** — weak
evidence, recorded as weak.

### 🟢 Three NEW addresses, licences payload-read at a pin

🟢 The supply tail `…github repository license` — `p400`'s remedy — returned **9 candidates, 3 of them
unshelved**, graded by instrument rather than by grep.

| agent | repo | licence | read at | description |
|---|---|---|---|---|
| EduAgent | [StudentTraineeCenter/edu-agent](https://github.com/StudentTraineeCenter/edu-agent) | **MIT** *(title line, `(c) 2025 Student Trainee Center`)* | `77c9ee5` · last commit **2025-12-30** · 511 files | LangGraph agents + RAG turning static course documents into tutoring environments: active-recall study plans, quizzes, flashcards, semantic mind maps. Python, `pyproject` + `uv.lock` + `alembic` + `docker-compose`, `deploy/` and `docs/` — 🟢 the most substantial of the three, and 🔴 **ten months without a commit**, so a census address, not a build-on row |
| Syllabus-RAG-AI-Agent | [R0HITHRAO/Syllabus-RAG-AI-Agent](https://github.com/R0HITHRAO/Syllabus-RAG-AI-Agent) | **MIT** *(title line, `(c) 2026 Rohith Rao`)* | `9eceb19` · last commit **2026-09-24** · 44 files | Zero-hallucination syllabus RAG with verifiable citations, auto-graded quizzes, revision flashcards. Flask (`app.py`, `core/`, `gunicorn.conf.py`), `Dockerfile` + compose + `Procfile`, `sample_data/` |
| ai4education | [5th-legionnaire/ai4education](https://github.com/5th-legionnaire/ai4education) | **Apache-2.0** *(title line)* | `70e8726` · last commit **2026-10-16** · 9 files | 🟡 **Not a platform — a SKILLS collection** for educators (`skills/` + README only). Freshest of the three, and the one whose shape a *"top agents"* table would misrepresent |

🔴 **`StudentTraineeCenter/edu-agent` graded `NAME-SUBSTRING-ONLY`, not `UNSHELVED`** — the hit is
`edu-agent-lab`, a different repository. 🟢 **That is `p400`'s defect class caught live for the FOURTH
time:** a bare `grep edu-agent` would have read it as already shelved and dropped a real MIT address.

### 🔴 `p400`'s own instrument had the same defect one layer down, and this pass paid for it

🔴 **Run from its own directory, `membership.py` graded nine already-shelved addresses `UNSHELVED` —
`HKUDS/DeepTutor` among them.** The mechanism: `shelf_paths` filters by existence, so from the module
directory the only `SHELVES` entry that resolves is **its own `README.md`**, and the population is
**6 addresses**. 🔴 **So a guard on EMPTINESS does not fire** — this pass's first draft wrote exactly
that guard and it changed nothing. 🟢 **The right guard is on COMPLETENESS of the shelf set**: a
misresolved root is detectable at the file layer and invisible at the address layer. Fixed, with two
controls (`15`, `16`) and mutation-verified; `p400`'s suite is **16 → 18 controls**. Registered as
`Gap 406-B`.

### 🟢 By-product: 40 HEAD collisions, `p283`'s question answered at scale

`--symref` carries the HEAD sha, so a sweep adjudicates *"two names, one tree"* for free. **40
collision groups**, among them `1edtech/*` ↔ `imsglobal/*` (**six** pairs — the standards body's
rename), `edx/ease` ↔ `openedx-unsupported/ease` ↔ `openedx/ease` (a three-name group),
`kantord/librelingo` ↔ `librelingo/librelingo`, `iterative/dvc` ↔ `treeverse/dvc`. 🔵 Not adjudicated
here — a collision is a **finding** and `p283` owns the verdict. Every group is recoverable from the
evidence TSV's `head_sha` column.

---

**🆕 Pass `p405` · reads and commit both 2026-10-23 — the ELEVENTH pass dated today.** 🔴 **The LMS-MCP
crowding this base has been citing as "real supply" is 42 addresses and only 27 PROJECTS — and the
inflation is NOT uniform: `canvas-mcp` absorbs 11 addresses into one family while `moodle-mcp` absorbs
none.** 🟢 **`intel/open-gaps.md` item 3's lineage half is CLOSED for all four groups it names.**

🔵 **Why `p402`'s channel could not see this, stated as a property and not as a fault.** `p402` probed
**ref sets** and got **20 distinct HEADs, 20 distinct fingerprints, 0 aliases** on `canvas-mcp` — and
wrote its own limit: *"a distinct HEAD rules out an alias and a non-divergent fork, and does **not** rule
out a **divergent** fork."* 🟢 **Every one of the 11 `canvas-mcp` family members has a distinct HEAD and
they all share the same root commit.** The ref-set answer was correct and the question it answers is a
different one.

🟢 **Measured 2026-10-23 from full clones — 42 addresses, 269 pairs, every pair graded.**

| group | addresses | resolved | pairs | 🟢 **projects** | related pairs | families |
|---|---|---|---|---|---|---|
| `canvas-mcp` | 23 | **20** | 190 | 🔴 **9** | **56** | **11** + **2** |
| `moodle-mcp` | 11 | **10** | 45 | 🟢 **10** | 🟢 **0** | 🟢 **none** |
| `blackboard-mcp` | 9 | **8** | 28 | **6** | **2** | 2 + 2 |
| `brightspace-mcp-server` | 4 | **4** | 6 | 🔴 **2** | **3** | **3** |
| 🟢 **total** | **47** | **42** | **269** | 🟢 **27** | **61** | 5 families, **15** addresses absorbed |

🟢 **Evidence:** [`group-lineage`](../evidence/group-lineage.2026-10-23-p405.tsv) — 47 address rows ·
269 pair rows · 21 columns · instrument, **12 controls / 0 failures**, and a facts cache that re-grades
without re-cloning, at [`compose/code/p405-group-lineage/`](../compose/code/p405-group-lineage/README.md).

### 🔴 Which address to build on, per family — four of the five were not the one this base cites most

🟢 **The origin is named by the ROOT COMMIT's author, first-hand, not inferred from currency or from
star count.**

| family | 🟢 **build on this** | measured | the rest of the family |
|---|---|---|---|
| `canvas-mcp` **FAMILY-1 (11)** | 🟢 [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **1,089 commits · 23 tags · HEAD `ebab8d6969cc` 2026-10-22 · 1 d** · MIT *(1,071 B)* · root `afe32c3e1721` **2025-02-27**, root-commit author identity (`%an <%ae>`) `vishalsachdev <svishal2001@gmail.com>` — 🟢 **and that same root commit, by that same author, is the root of all eleven** | `bartmassey-upstream` (1,001 · 23 tags · 12 d) · `sirdanielm` (972 · 3 d) · `lindsay-cheng` (928 · 26 d) · `yeetingwaterbottle` (873 · 20 d) · `harrywang` (709 · 42 d) · `abr-projects` (672 · 10 d) · `amirf194` (671 · 64 d) · `jsrodr` (555 · 66 d) · `nelsonspencer` (472 · 7 d) · `fdis111` (301 · 21 d) |
| `canvas-mcp` **FAMILY-2 (2)** | 🟡 **keep** [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | 61 commits · **3 tags** · HEAD `711549f163ef` 2026-09-21 · 32 d · MIT *(1,065 B)* · root `731aa116052b` **2024-12-12**, root-commit author identity (`%an <%ae>`) `R.Huijts <r.huijts@fontys.nl>` *(Fontys, NL)* | 🔴 [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) is a **`SUPERSET`** — 64 commits, r-huijts's HEAD is an ancestor — **22 d**, and **0 tags**. 🟡 **Three commits ahead is not canonical**: the published artefact and the institutional provenance are both on `r-huijts` |
| `brightspace-mcp-server` **(3)** | 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | 🟢 **472 commits · 6 tags · HEAD `1fbc693bf9e1` 2026-10-22 · 1 d** · MIT *(1,068 B)* · root `fb3d6c0a57bf` **2026-02-07**, root-commit author identity (`%an <%ae>`) `RohanMuppa <rohanmuppawork@gmail.com>` — 🟢 **root of all three** | `lmgveerhoek` (308 · 0 tags · 26 d) and `matthewliu10` (251 · 5 tags · 41 d), both `DIVERGED-FORK` |
| `blackboard-mcp` **FAMILY-1 (2)** | 🟢 [`alanwtom/blackboard-mcp`](https://github.com/alanwtom/blackboard-mcp) | 26 commits · 1 tag · HEAD `5c7462019957` **2026-10-22 · 1 d** · MIT *(1,065 B)* · root `881f50968ac3` 2026-08-29, root-commit author identity (`%an <%ae>`) `alanwtom <alanwtom@users.noreply.github.com>` | `lukecarroll15` (20 · 39 d), `DIVERGED-FORK` |
| `blackboard-mcp` **FAMILY-2 (2)** | 🟢 [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) | 21 commits · 3 tags · HEAD `fb057928ae20` 2026-10-14 · **9 d** · MIT *(1,084 B)* · root `946d69b33dfa` 2026-09-10, root-commit author identity (`%an <%ae>`) `felipedias-ie <231931438+felipedias-ie@users.noreply.github.com>` | 🔵 `bibo242` carries **28** commits over all refs and is the **ANCESTOR** — see the trap below |

🔴 **The trap in that last row, and it is the one a commit count walks straight into.**
`bibo242/blackboard-mcp` has **28** commits to `felipedias-ie`'s **21**, and `felipedias-ie` is
nonetheless the **descendant**: `git merge-base --is-ancestor` puts `bibo242`'s HEAD inside
`felipedias-ie`'s history. 🟢 **The extra commits sit on refs that are not reachable from `bibo242`'s
own HEAD.** 🔵 So ancestry must be asked against **`rev-list HEAD`**, never against `rev-list --all`,
and this instrument's load-bearing control is exactly that case.

### 🔴 `bartmassey-upstream/canvas-mcp` — the slug says upstream and the history says fork

🔴 **It is not upstream.** Its root commit is `afe32c3e1721`, authored by **`vishalsachdev`**, and it is a
`DIVERGED-FORK` of `vishalsachdev/canvas-mcp` at **1,001 commits against 1,089**. 🟢 Same class as
`p402`'s `*-unsupported` finding, with the sign reversed: there an owner name **was** the stewardship
fact, here an owner name **asserts** a provenance the history denies. 🔵 **The rule for a licence or
provenance cell:** an owner or slug containing `upstream`, `canonical`, `official` or `main` is a
**claim**, and the root commit is the measurement.

### 🟢 What this does NOT change

| | |
|---|---|
| 🟢 **`moodle-mcp` is genuinely 10 projects** | **45 pairs, 45 `INDEPENDENT`, 0 shared commits and 0 shared trees anywhere in the group.** 🔵 The crowding reading was right for this group and wrong for the other three, which is why a per-group measurement was needed rather than one verdict about "LMS MCP supply" |
| 🟡 **7 of `canvas-mcp`'s 20 are real sole projects** | `caleb-media-studio`, `admin978`, `aryankeluskar` *(🔵 **ISC**, 746 B — still the only non-MIT/Apache/BSD permissive grant these shelves carry)*, `mattlo0546`, `lucanardinocchi` *(🔴 **no grant**)*, `plyght` *(🔴 **no grant**, 2 commits, 358 d)* and `zhenghh04` |
| 🔴 **It does not grade quality** | A shared commit proves a relation. **Nothing here says the family head is good software** — only that the other ten addresses are not independent evidence of ecosystem breadth |
| 🔴 **5 of 47 addresses do not resolve** | `eastarctica/canvas-mcp` *(already known `UNRESOLVED` at `p402`)*, 🆕 `owen-x-tech/canvas-mcp`, 🆕 `owentaylor/canvas-mcp`, 🆕 `nahuelalbornoz/moodle-mcp`, 🆕 `e9x/blackboard-mcp`. 🟡 **Four of the five are new**, and they are named so they are not re-probed |

🔵 **One more shape, recorded so it is not mistaken for an address.** `io.github.vishalsachdev/canvas-mcp`
appears on [`agents/trending.md`](trending.md) and is the **MCP registry identifier**, not a GitHub
address — it is the registry name of `vishalsachdev/canvas-mcp`, the family head above. 🔴 **It is also
NOT the dot-run specimen `gate-census-union`'s control 24 wants**: that rule tests the repository **NAME**
position for `^\.{3,}$`, and this dot run is in the **OWNER** position. Checked, so a successor does not
read it as the fix for that red gate.

---


**🆕 Pass `p404` · reads and commit both 2026-10-23 — the TENTH pass dated today.** 🟢 **`p402`'s
three open-direction pairs are CLOSED, in one channel nobody here had used: a FULL-history clone.
Three pairs, three different verdicts.** 🔴 **One of the three REFUTES `p402`'s own note, and the
refuted pair is cited on all four build-on tiers while its 1,125-day-fresher superset is cited once.**

🔵 **Why this pass did not run a sixth language leg.** `p403` spent the Hindi leg and recorded the
prescribed legs as saturated; `p403` also left three items *"named so it cannot look worked"*. 🟢 This
pass takes the one that was **narrowed to a single measurable question** — `p401`'s
`aiprovider_openaicompatible` pair — and finds the measurement generalises, so it closes the other two
open pairs in the same run.

🔴 **`p402` wrote, in its own instrument's *"What it did NOT establish"*: for
`moodle-aiprovider_openaicompatible`, `pylti1.3`, `lti` and `moodle-mcp-server` "the HEADs differ …
and the fork direction stays unestablished."** 🟢 **It is establishable — but not by a better ref-set
test.** A ref set is derived from *current* refs, and direction is a fact about *history*: a
**squash-republish shares ZERO commit SHAs with its origin**, so a ref-set test grades a copy and two
unrelated namesakes **identically**. The signal is absent from the channel, not faint in it.

| pair | commits *(all refs)* | shared commits | shared trees | ancestry | 🟢 **verdict, first-hand 2026-10-23** |
|---|---|---|---|---|---|
| [`ADORSYS-GIS`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible) ↔ [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) `moodle-aiprovider_openaicompatible` | **35** ↔ **17** | 🔴 **0** | 🟢 **1** | none | 🟢 **`CONTENT-COPY` · direction `lmscloud-io` → `ADORSYS-GIS`** |
| [`astiusa/lti`](https://github.com/astiusa/lti) ↔ [`macewan-cs/lti`](https://github.com/macewan-cs/lti) | **91** ↔ **89** | 🟢 **89** | 🟢 **89** | 🟢 **`macewan-cs` HEAD IS an ancestor of `astiusa` HEAD** | 🟢 **`SUPERSET` · `macewan-cs` → `astiusa`** |
| [`lmscloud-io`](https://github.com/lmscloud-io/moodle-mcp-server) ↔ [`peancor`](https://github.com/peancor/moodle-mcp-server) `moodle-mcp-server` | **10** ↔ **11** | 🔴 **0** | 🔴 **0** | none | 🟢 **`INDEPENDENT` — measured, not assumed** |

🟢 **Evidence:** [`fork-direction`](../evidence/fork-direction.2026-10-23-p404.tsv) — 6 addresses · 21
columns · instrument, **9 controls / 0 failures** and all three pairs **reproduced end-to-end from
clean clones**, at [`compose/code/p404-fork-direction/`](../compose/code/p404-fork-direction/README.md).

### 🟢 `p401`'s pair, CLOSED — and the direction is the opposite of what currency suggests

🟢 **Three independent measurements agree.** (1) The **only** shared tree, `85d9a99e3c96`, is
`ADORSYS-GIS`'s **root** tree — and it is `lmscloud-io`'s working tree at commit `c8b6f9fe`,
**2026-06-09**, seven weeks before `ADORSYS-GIS`'s root commit of **2026-07-27**. A root commit cannot
hold content that did not already exist. (2) Both root commits carry the **same author identity**,
`Leghadjeu-Christian <legochristianarthur@gmail.com>` — so this is a hand-off, not an unattributed
lift. (3) 🟢 **The version counter is inherited.** `lmscloud-io` sets `$plugin->version = 2026060200`
on **2026-06-02**; `ADORSYS-GIS`'s root commit **starts at that same `2026060200`** and only later
bumps to `2026101500`. A counter cannot be inherited backwards.

🔴 **And the useful half, which no shelf here said.** The **origin is the stale one.**
`lmscloud-io` is **93 d** (HEAD `040b74d5b13e`, 2026-07-22, branch `moodle405`); `ADORSYS-GIS` is
🟢 **8 d** (HEAD `371278b0ebd6`, 2026-10-15), carries a `moodle-plugin-ci` pipeline with a **Moodle
5.0+ matrix**, an open `chore/bump-plugin-version` branch, and a commit whose message links the
**Moodle Plugins directory listing**. 🟢 **So `ADORSYS-GIS` is the one to build on and `lmscloud-io` is
the provenance** — the reverse of the reading "the older address is upstream, therefore canonical".
🟡 **One regression in the copy, worth a config note:** `lmscloud-io` declares
`$plugin->supported = [500, 502]`; `ADORSYS-GIS` **dropped** that line while keeping
`$plugin->requires = 2025041400`, so the copy ships **no declared Moodle upper bound**.

🟡 **Grant unchanged, and `LADDER_BLIND` reproduced.** Neither repository has a licence-shaped file in
its root tree — `ADORSYS-GIS` is `[.github .gitignore README.md UPGRADING.md amd classes db lang tests
version.php]`, `lmscloud-io` the same without `.gitignore` — and the grant exists only in **PHP file
headers** (*"version 3 of the License, or (at your option) any later version"*), i.e.
**`GPL-3.0-or-later`**. 🔵 That is `p401`'s pattern again, measured rather than inherited.

### 🔴 The `lti` pair — `p402`'s note is REFUTED, and a live recommendation is 1,125 days stale

🔴 **`p402` recorded `astiusa/lti` ↔ `macewan-cs/lti` as *"two unrelated repositories sharing a very
short name"*.** 🟢 **They share a root commit** — `228556c`, **2021-05-07**, *"Create LICENSE"*, by
Nicholas Boers — and **89 of `macewan-cs`'s 89 commits are reachable from `astiusa`'s HEAD**, which
`git merge-base --is-ancestor` confirms. They are not a name collision; they are one lineage.

🟢 **`astiusa/lti` is a strict superset at 794 d against `macewan-cs`'s 1,919 d** — a **1,125-day**
correction on this shelf's freshest permissive **Go** LTI 1.3 option. The two extra commits are both
by `hussein.vastani@asti-usa.com`: **2023-05-22** (import paths, plus `target_link_uri` taken from the
**login request** instead of from registration, plus a `TargetLinkURI` helper on the connector) and
**2024-08-20** (*"Added support for PKCS8 files"*) — **11 files, +49 / −26**. 🟢 The MIT grant file is
**byte-identical** across both, 1,108 B, `sha256`₁₆ `6e58273960b0`, still **© 2021 MacEwan University —
Department of Computer Science**, so the fork kept the attribution.

🔴 **The shelf defect this exposes.** `macewan-cs/lti` is cited on **all four build-on tiers**
([`repos/foundations.md`](../repos/foundations.md) ×2, [`verticals/solutions.md`](../verticals/solutions.md),
[`compose/patterns.md`](../compose/patterns.md)); `astiusa/lti` appears **once**, in a star-count table
on this file. 🟡 **The recommendation itself survives** — `p391`/`p392`'s *"front a Go or JVM platform
with `ltijs` or `lti-tool` over HTTP"* stands, because 794 d is still dead and **both repositories
carry 0 tags**, so there is no published artefact either way. 🔴 **What does not survive is the
dating**, and [`repos/foundations.md`](../repos/foundations.md) now carries the corrected row.

🔴 **The switching cost, which identical licence bytes hide.** The 2023-05-22 commit **changed the Go
module path**. So a strict superset by history is **not** a drop-in dependency by import path: a
consumer must edit its imports to move. 🔵 Recorded as an amendment on
[`intel/trends.md`](../intel/trends.md) — *same grant, same code, different package identity*.

### 🟢 The `moodle-mcp-server` pair — independence MEASURED, and the two are not interchangeable

🟢 **0 shared commits AND 0 shared trees**, no ancestry either way: two genuinely independent
implementations that share a plugin name. 🔵 `p402` had graded them `DISTINCT` from differing HEADs,
which is the right verdict from the wrong evidence — a differing HEAD is also what a copy looks like.

🔴 **And they differ in exactly the two cells a build decision turns on**, which is itself positive
evidence of independence:

| address | language | 🟢 **grant *(root `LICENSE`, payload-read)*** | HEAD · age | tags | what it means for a build |
|---|---|---|---|---|---|
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **TypeScript / Node** *(`package.json`, `tsconfig.json`)* | 🟢 **MIT** *(1,064 B, `845ac6ac9e57`, © 2025 peancor)* | `666f12222ed6` · 🟡 **243 d** | 🔴 **0** | 🟢 **The build-on one.** Permissive, and it sits in the same runtime as `ltijs` / `lti-tool` |
| [`lmscloud-io/moodle-mcp-server`](https://github.com/lmscloud-io/moodle-mcp-server) | **Python** *(`pyproject.toml`, `src/`, `fastmcp`)* | 🔴 **`GPL-3.0`** *(35,148 B full text, `8b1ba204bb69`)* | `4b11494d6522` · 🟡 **168 d** | 🟢 **3** — `v1.0.0`…`v1.0.2` | 🟡 **Fresher, versioned, and copyleft.** Root commit authored by **Marina Glancy** — Moodle core provenance — so read it even where the grant rules it out of a proprietary path |

🔴 **A shelf that says "use `moodle-mcp-server`" without naming the owner spans an MIT/GPL-3.0
boundary**, and the fresher of the two is the copyleft one. 🟢 Both rows are now disambiguated here and
on [`repos/trending.md`](../repos/trending.md).

### 🔴 Saturation, measured rather than asserted — 20 candidate addresses, 20 already shelved

🟢 **All five prescribed legs were run, plus two extra probes** (a university-/LMS-MCP-server probe,
because this base records that class as its most reliably-growing one, and a non-GitHub-forge probe for
GitLab and Codeberg). 🔴 **They produced 20 distinct candidate addresses and every one of them is
already on these shelves** — `vishalsachdev/canvas-mcp`, `DMontgomery40/mcp-canvas-lms`,
`JohannsenLum/canvas-api-mcp`, `AnonymousOnyx22/canvas-lms-student-mcp`, `Mattlo0546/canvas-mcp`,
`peancor/moodle-mcp-server`, `loyaniu/moodle-mcp`, `saylordotorg/moodle-local_ai_course_assistant`,
`Open-TutorAi/open-tutor-ai-CE`, `098765d/AI_Tutor`, `Selleo/mentingo`, `OpenOLAT/OpenOLAT`,
`Miaotofu01/Study-Mate`, `SenmuuuuW/universal-diagnostic-tutor-skill`, `lowwwbank/anything-to-course`,
`SirhanMacx/Claw-ED`, `A-R007/Multi-Agent-Study-Assistant`, `HugeCatLab/ChatTutor` and both
`lti` addresses above.

🟢 **Matched by `p400`'s rule — exact slug, never substring** — against an index of **3,479** distinct
`owner/repo` slugs harvested from every `.md`, `.tsv` and `.py` on these shelves. 🔵 **20 / 20 is a
denominator**, which is what separates this from a pass that searched and found nothing: the legs are
not failing, the shelf is ahead of them.

---

**🆕 Pass `p403` · reads and commit both 2026-10-23 — the NINTH pass dated today.** 🟢 **A
**Hindi-language** leg returns the first **Indic-language** education addresses this base has ever
held, and it is the THIRD independent confirmation of `p401-T1` — this time *predictively*.** 🔴 **No
row is promoted to a build-on tier: of three addresses, one is UNGRANTED and two are not agents.**

🔵 **Why this pass ran a Hindi leg at all.** `T35` records the four prescribed English global legs as
spent, and `p401-T1` states that national-language supply appears roughly a year behind national
mandates — evidenced on the Gulf, and already proved once from the other direction when `p387` broke a
four-pass LATAM null with Spanish and Portuguese. 🟢 [`intel/market.md`](../intel/market.md) already
carries India's mandate: **AI and computational thinking compulsory from Class 3 from the 2026–27
academic year**. `p401-T1` therefore *predicts* Indic-language supply appearing around now — and a
Hindi leg was the cheapest available test of this base's own trend.

🟢 **The prediction holds. Every grant below was read from the payload on 2026-10-23**, via
`git ls-remote --symref` for the real default ref and a `--depth 1` clone for the tree, because
🔴 **`github.com` HTML is `403` on this session** — established against a known-good control
([`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) returns `403` too), so the block is the
channel and not the addresses.

| address | ref | grant *(payload, first-hand)* | HEAD · refs | what it actually is | region |
|---|---|---|---|---|---|
| [AI4Bharat/Anudesh-Backend](https://github.com/AI4Bharat/Anudesh-Backend) | 🔴 **`master`** | 🟢 **MIT** *(1,067 B, `sha256`₁₆ `e2cd4cec54f7`, "Copyright (c) 2023 AI4Bhārat")* | **2026-09-01** · 754 refs · 🔴 **0 tags** | 🟡 **NOT an agent — a multi-annotator task-and-review workflow backend.** Django, with `projects` → `tasks` → `users` / `organizations` / `workspaces` / `notifications` / `dataset` / `filters` apps, Docker-composed with Elasticsearch and Celery. 🟢 Its education value is the **workflow substrate**: the projects-to-reviewers machinery an assessment or marking pipeline needs, and the collection harness for Indic-language instruction data a curriculum-grounded tutor would train or evaluate on. 🔴 **0 tags means no published artefact** — vendor a commit, do not "install" it. | APAC — AI4Bhārat, India |
| [AI4Bharat/IndicIFEval](https://github.com/AI4Bharat/IndicIFEval) | `main` | 🟡 **MIT on the CODE** *(1,074 B, `sha256`₁₆ `1bff713bf26a`, "Copyright (c) 2026 Thanmay Jayakumar")* **· `CC-BY-4.0` on the DATASET** | **2026-09-16** · 6 refs | 🟢 **The evaluation gate for any Indic-language tutor — verifiable, rule-based instruction-following across 14 Indic languages plus English** (Assamese, Bengali, Gujarati, Hindi, Nepali, Odia, Punjabi … ), with `indicifeval-ground`, `indicifeval-trans` and a bundled `lm-evaluation-harness`. arXiv `2602.22125`; dataset also on Hugging Face. 🔵 Rule-based and verifiable is the point: it scores constraint compliance deterministically, so it is usable as a **CI gate** rather than an LLM-judge. | APAC — AI4Bhārat, India |
| [matsuolab/lecture-ai-engineering-2026-hi](https://github.com/matsuolab/lecture-ai-engineering-2026-hi) | `main` | 🔴 **NO GRANT** — no licence-shaped file in the root tree, no licence field in `pyproject.toml` | **2026-10-19 — 4 d** · 2 refs | 🟡 **Courseware, and the single most interesting *shape* this pass.** The **Hindi localisation** of the University of Tokyo **Matsuo Lab**'s *AI Engineering Pilot Course* (`AIE2026`): across the course students **progressively build an agent that helps them learn AI engineering**. README, and even the `pyproject.toml` comments, are **Hindi-first**. Browser-only via Codespaces; deps pinned (`google-genai==2.31.0`, `pydantic-ai-slim[google,mcp]==2.57.0`), with **MCP server and client in Lecture 05**. 🔴 Ungranted, so it is a **reference, not a reusable asset**. | APAC — Matsuo Lab (JP) **localised for India** |

🟢 **The `NO GRANT` verdict on the third row is MEASURED, not inferred from a blank sidebar** — in
`p293`'s shape: `README.md` is present at the same ref, so the tree read demonstrably works and the
absence of `LICENSE` is real.

🔴 **`IndicIFEval` is the FOURTH instance of `T36` on these shelves, and the cleanest.** The repository
is MIT and the dataset is `CC-BY-4.0`, stated in its own §License — so *"IndicIFEval is MIT"* is true
and misleading at once. 🟢 Both grants are commercially usable, which the earlier `T36` instances were
not, so the consequence here is **attribution obligations attaching to the data**, not exclusion.
Recorded on [`intel/trends.md`](../intel/trends.md).

🔴 **All five prescribed legs are SATURATED for a fifth-plus consecutive pass, named so silence cannot
read as coverage.** The global agent, GitHub-trending, vertical-platform and industry-news legs
returned **zero** unshelved granted education-native addresses; every vertical candidate they produced
(`frappe/education`, `openeducat`, `ERPNext`, `openSIS`, `Fedena`, `GegoK12`) is **already shelved**,
and the four regional legs returned **zero new facts** — see
[`intel/market.md`](../intel/market.md) for that result, which is itself the pass's second finding.

🟢 **Two table defects of the class this base keeps warning about were found and FIXED, in the append-only files where they had been invisible.** 🔴 `repos/trending.md`'s `ACTION XN` verdict table had **five data rows missing their leading `|`** — real content (`WARN 145`, `DOCUMENTED 47`, `IGNORED-PATH-FRAGMENT 37`, `REFUSE-ANNOTATED 6`, `REFUSE 0`) that markdown rendered as prose, so a row-reading compiler saw **zero rows**. 🔴 `agents/trending.md`'s Article 6(3) citation sat **in the header row** with an empty body — same outcome, opposite cause. 🔵 **Neither was a placeholder**, which is why no placeholder sweep had caught them: the defect is a table that *parses to nothing while reading correctly to a human*. 🟢 Both now carry a real header and real rows; a whole-file check across all eight shelves is otherwise clean.

🔴 **Also carried, so it cannot look worked:** `p402`'s **296 of 324** backlog addresses remain
unadjudicated; `p370`'s **1,152**-slug promotion backlog is untouched for a **seventh** pass; and
`p401`'s `moodle-aiprovider_openaicompatible` pair is still **narrowed, not closed**.

**🆕 Pass `p402` · reads and commit both 2026-10-23 — the EIGHTH pass dated today.** 🟢 **`p397`'s
fork backlog is worked for the first time in five passes — the item `p400` ranked and `p401`
recorded itself as declining.** 🔴 **No row on this shelf gains or loses a grant.** What changed is
**which address** three groups are cited by, and one of them had been open since `p350`.

| | |
|---|---|
| 🟢 **`ACTION ZZ-al` CLOSED after ~52 passes** | The register asked which of `edx/ease` or `openedx/ease` is canonical. 🔴 **Both are STALE.** The canonical address is [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease) — **zero** prior mentions in this base — on the **HTML header after the redirect**, the channel `p351` correctly said the clone arm *"does not have"*, corroborated by a ref-set fingerprint identical across all **three** addresses (**173 refs**, fp `e3793cd329e4`). 🔵 **AGPL-3.0 and archived since 2024-02-28**, so nothing moves commercially — but a live recommendation on [`verticals/solutions.md`](../verticals/solutions.md) pointed at an alias, and is corrected. |
| 🟢 **Both register-absent pairs `p397` flagged "YES" adjudicated, with direction** | `1EdTech/lti-1-3-php-library` **CANONICAL** ↔ `IMSGlobal/…` **STALE** (61 refs both, fp `08d380600a05`); `meta-pytorch/opacus` **CANONICAL** ↔ `pytorch/opacus` **STALE** (562 refs both, fp `aeb05358835f`). 🔵 `packbackbooks`' parent is now named **first-hand** by the HTML `forked from` line — a provenance confirmation, **not** a shelf defect: `p391` recommends that fork deliberately. |
| 🔴 **This pass's own draft reproduced `p400`'s substring defect** | The draft claimed *"stale aliases in live use on the build-on tiers"* off **2** `pytorch/opacus` citations. 🔴 **One is the substring inside `meta-pytorch/opacus`**, the other is the register row discussing the alias — 🟢 **true independent citations: 0**, and the claim was withdrawn before publication. `p400`'s guard earns its keep against the pass two later. |
| 🔴 **The 324-address sweep was REFUSED** | `Exfil Scouting`, in a parallel **and** a plain sequential form. Individually named addresses are permitted, so the backlog is worked in **bounded, named batches — 28 addresses**. 🔵 `T82`: a refusal licenses exactly one conclusion, *this invocation was refused*. 🟢 It improved the scoping — batches were chosen by whether a build-on tier actually **cites** the group. |
| 🔴 **Carried, and named so it cannot look worked** | **296 of 324** backlog addresses unadjudicated; `p370`'s **1 152**-slug promotion backlog untouched for a **sixth** pass; `p401`'s `moodle-aiprovider_openaicompatible` pair **narrowed, not closed** (HEADs differ → two repositories, direction still unestablished). |

🔴 **All five prescribed global legs are SATURATED, including the supply tail that paid for `p401`** —
every address it returned is **exact-shelved**. 🟢 Two first-hand reads came out of it anyway:
`Ebimsv/AITutorAgent` is **MIT** by payload (`LICENSE`, 1 072 B, title `MIT License`, on **both**
`main` and `master`), and `Naresh1401/education-tutor-agent` carries **no grant at either branch**
with `README.md` → 200 as the branch control — 🟢 **independently reproducing this base's `NO GRANT`
verdict and refuting the search engine's "MIT-licensed" claim.**

**Evidence:** [`alias-direction`](../evidence/alias-direction.2026-10-23-p402.tsv) — 28 addresses ·
[`regional-legs`](../evidence/regional-legs.2026-10-23-p402.tsv) — 9 legs · instrument and **4
reproduced `p370` controls** at [`compose/code/p402-alias-direction/`](../compose/code/p402-alias-direction/README.md).



**🆕 Pass `p401` · reads and commit both 2026-10-23 — the SEVENTH pass dated today.** 🟢 **The
Arabic-language leg that `p389` named as *"the next step"* and that five passes did not run has
been run, and it refutes this base's absolute supply null.** 🔴 **What it found is six weeks old
and tops out at 4 ★, so none of it is promoted to a build-on tier — the rows below carry their
real counts so nobody mistakes a seedbed for a starting point.**

🔴 **The claim that is refuted, quoted exactly.** [`intel/market.md`](../intel/market.md) has
carried, as a 🔴 supply gap, *"**No** Gulf-origin and **no** Arabic-first open-source education
agent or platform was found — **not one address**, against the strongest statutory demand in the
world"* — with the honest rider *"the leg was English-language; an Arabic-language search is the
next step."* 🟢 **The rider was right.** An Arabic-language query returns education-native
addresses on the first page, and `p387` had already proved this exact fix on the four-pass LATAM
null with Spanish and Portuguese legs.

## Tier 7 — 🆕 `p401` The Arabic-first watch tier · **NOT a build-on tier**

🔵 **Why this is a tier and not a promotion.** Every grant below was read by **payload** on
2026-10-23 and every count comes from the **authenticated API** the same day. 🔴 **The ceiling is
four stars.** All three permissive addresses were created between **2026-09-14** and
**2026-10-13**, none is a platform, and a studio cannot stand an engagement on a six-week-old
repository with no adopters. 🟢 **They are shelved because the ABSENCE was load-bearing** — this
base was telling itself the Arabic supply was empty, and it is not.

| agent | repo | ref | licence | ★ · created | what it actually does | region |
|---|---|---|---|---|---|---|
| **Taqyeed-AI** | [okba-boubakeur/Taqyeed-AI](https://github.com/okba-boubakeur/Taqyeed-AI) | `main` | 🟢 **MIT** *(1,373 B, payload-read)* | **4 ★** · 2026-09-14 | 🟢 **The only STUDENT-FACING Arabic-first tool found with a verified permissive grant.** *"قَيِّدْ عِلْمَكَ"* — smart lecture and lesson recording, note-taking, and custom AI actions, addressed in its own description to *طلبة العلم*. TypeScript. 🔵 Arabic-first in the **interface and the framing**, not a translation layer bolted onto an English product. | EMEA |
| **build-your-own-agent-ar** | [kazoya/build-your-own-agent-ar](https://github.com/kazoya/build-your-own-agent-ar) | `main` | 🟢 **MIT** *(1,070 B, payload-read)* | **0 ★** · 2026-10-12 | 🟡 **Teaching MATERIAL, not a runnable platform** — an Arabic step-by-step path to building a working agent. 🟢 **It lands on the one surface the Gulf demand actually names:** the UAE's decision attaches **22,000 teachers** to be trained, and teacher-facing AI-literacy material *in Arabic* is the scarcest input in that programme. HTML. | EMEA |
| **Arab-Artificial-Intelligence** | [openaziz00-sudo/Arab-Artificial-Intelligence](https://github.com/openaziz00-sudo/Arab-Artificial-Intelligence) | `main` | 🟢 **MIT** *(1,609 B, payload-read)* | **0 ★** · 2026-10-13 | 🟡 **Curriculum-grounding raw material, not an agent.** An Arabic AI library of **1,650 prompts across 17 categories**, audience explicitly including **students** (*والطلاب*). Python. 🔵 Useful as seed content for Arabic prompt scaffolds; it carries no model, no retrieval and no runtime. | EMEA |

🔴 **Four further Arabic addresses carry NO grant at the ladder, each with a PASSING branch
control** — a measured absence in `p293`'s shape, not an inference from a blank sidebar:
[`ehtsmulhq/ArabicTutorRAG`](https://github.com/ehtsmulhq/ArabicTutorRAG) (a Madinah-grammar RAG
tutor whose **README claims MIT for code** with content held non-commercial — `p288`: a
README-only claim is a **POINTER**, never a verified grant),
[`sartaj1995/arabic-tutor`](https://github.com/sartaj1995/arabic-tutor) (**100 curriculum levels,
1,367 exercises** as structured JSON — the richest *content* asset found, and unlicensed),
[`wajhullah/arabic-literature-ai`](https://github.com/wajhullah/arabic-literature-ai) and
[`jibrilsettles-dot/Arabic-Tutor`](https://github.com/jibrilsettles-dot/Arabic-Tutor).
🔴 [`michaelsboost/ArabEngo`](https://github.com/michaelsboost/ArabEngo) is **CC-BY-NC-4.0**
*(17,766 B)* and is **excluded outright** — NonCommercial is not an OSI grant and forbids the
commercial derivative a studio engagement produces.

🟡 **One new address from the global supply tail, promotion also refused.**
[`braiinz94/braiinz-education`](https://github.com/braiinz94/braiinz-education) —
*"Socratic tutoring, spaced repetition, PISA-aligned diagnostics … aligned with French
curriculum"*, 🟢 **Apache-2.0 read by payload at 11,356 B on BOTH `main` and `master`**, Python,
pushed **2026-10-20**, not archived. 🔴 **0 ★, 1 fork.** 🟢 It is the first
**EMEA-curriculum-aligned** permissive agent on these shelves and the only one found anywhere
that names a **PISA** alignment — worth watching for that alone. 🔵 Its fork
`sbkriz/braiinz-education` reports licence `NOASSERTION` against the source's Apache-2.0;
flagged, not adjudicated.

🔴 **The four prescribed global tails are saturated for a FOURTH pass.** `OpenClaw`, `Hermes`,
`OpenHands`, `CrewAI`, `LangGraph`, `500-AI-Agents-Projects`, `withmarbleapp/os-taxonomy`,
`luongnv89/claude-howto`, `plastic-labs/tutor-gpt`, `microsoft/moodle-ai-assistant`,
`openedx/openedx-ai-extensions`, `saylordotorg/moodle-local_ai_course_assistant`,
`yedidiaklein/moodle-local_aiquestions`, `X5GON/x5moodle` — **9 of 13 graded `SHELVED-EXACT` by
exact address**, the remainder forks of shelved upstreams
([`raccoongang/openedx-ai-extensions`](https://github.com/raccoongang/openedx-ai-extensions) under
shelved `openedx`) or unlicensed. 🟢 **Checked with `p400`'s exact-address test, not a grep.**

**🆕 Pass `p400` · reads and commit both 2026-10-23 — the SIXTH pass dated today.** 🔴 **No row
added, for the third consecutive pass — but this time the reason is a measured property of the
ADMISSION TEST, not of the supply.** 🟢 **The test that decides what reaches this shelf now has
an instrument, 16 controls and a live specimen.**

🔴 **`400-C`: the acceptance check this shelf has relied on is a SUBSTRING match.** `p398` and
`p399` each certified their declines with *"every one already carried on these shelves, **each
checked by grep** rather than by memory"* — and a grep for a bare repository **name** matches any
shelf text that *contains* it. 🔴 **`p400`'s own first check produced a false *"already
shelved"* on a real address**: a bare `grep ai-grader` returns hits, every one of them from
[`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) — a different owner, a
different repository and a **different name** that merely contains the candidate's.

🔵 **The nearest owner, named so this is not re-sold as new:** `p332-delivery-audit` already
reports this *shape* as `PREFIX PAIRS` — the **stump**
`eecs-autograder/autograder`, a **truncated** form of
`eecs-autograder/autograder.io`. 🔴 **But it looks INSIDE the harvested corpus**, and an
incoming candidate is not in the corpus yet — which is why the shape survived there and was
never caught at the door. Same family as `T80`, one layer out.

🟢 **Re-graded by exact address, and the prior passes are VINDICATED rather than impugned.**
[`candidate-membership`](../evidence/candidate-membership.2026-10-23-p400.tsv) — **24 candidates:
23 `SHELVED-EXACT`, 1 `NAME-SUBSTRING-ONLY`.** 🟢 **`p398`'s and `p399`'s declines survive the
re-grade 14-for-14**, so the defect is a real mechanism that had not yet cost this base an
address — it cost `p400` one, and was caught because the instrument existed by then.

🔴 **The one genuinely unshelved address is NOT promoted to this shelf, and the reason is the
grant.** [`andres-tovar-purdue/ai-grader`](https://github.com/andres-tovar-purdue/ai-grader) —
*"Modular AI grading agent for engineering programming projects"*, **2 ★**, **0 forks**, **39
commits**, no archive banner. 🔴 **No grant, established by PAYLOAD and not by a missing sidebar
entry:** `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` all **404** on **both** `main` and
`master` — **eight probes** — while `main/README.md` answers **200** (so the branch exists and
the channel works for this repository), and `moocupv/lti-ai-grader`'s `main/LICENSE` returns a
real **Apache-2.0** payload through the same channel in the same minute. 🟢 **A calibrated pair,
`p293`'s shape: the absence is measured, not inferred.** It is a census address on
[`trending.md`](trending.md) only — an unlicensed repository is not something a studio builds on,
and **fewer real rows beat padding**.

**🆕 Pass `p399` · reads and commit both 2026-10-23 — the FIFTH pass dated today.** 🔴 **No row
was added to this shelf, for the second consecutive pass, and the candidate list was measured before
being declined.** Four global supply legs plus one extended supply leg returned
`agents-from-scratch`, `ai-engineering-from-scratch`, `AI-Roadmaps`, `ai-agents-for-beginners`,
`500-AI-Agents`, `awesome-llm-apps`, Hermes, OpenClaw, `BlackyDrum/ai-tutor`, `Gchism94/ai-tutor`,
`zijinz456/OpenTutor`, `artcc/freelingo`, `KeWang0622/kaogong-skill` and `Zenglian990/AI_Tutor_Release`
— 🔴 **every one already carried on these shelves**, each checked by grep rather than by memory.

🔴 **One address was genuinely unshelved and is still not promoted:**
[`the-open-agent/openagent`](https://github.com/the-open-agent/openagent) — a general personal
assistant with computer-use and browser-use loops. 🔵 **It is not education-native**, and this shelf
does not carry general agents that merely *could* be pointed at a classroom; that rule is what keeps
the tier readable. Recorded here as a declined candidate so the next pass does not re-litigate it.

🟢 **The autograder tier gains a first-hand grant read rather than a row.**
[`arthtyagi/judge`](https://github.com/arthtyagi/judge) — 🟢 **MIT**, **32 ★**, 3 forks — is
🔴 **archived since 2022-08-11**, so `Gap 398-D` closes with the licence established and the
artefact still excluded. 🔵 The `okpy/ok` correction from `397-A` stands unchanged and was not
re-derived this pass. `Gap 399-A`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — the FOURTH pass dated today.** 🔴 **No row was
added to this shelf, and that is the finding rather than a shortfall.** Four global supply legs
returned `Ebimsv/AITutorAgent`, `maxew6/ai-tutor-project`, `Zenglian990/AI_Tutor_Release`,
`os-taxonomy` and the standard LMS set — 🔴 **every one already carried here**, and
`maxew6/ai-tutor-project` is held under `P150-B`/`T79` with a sharper reading than the channel gave.
🟢 **The autograder tier is now positively CORROBORATED rather than merely unrefuted:** `p397`'s
`topic:autograder` lead was spent this pass, and sorting those 124 results by stars returns
[`okpy/ok`](https://github.com/okpy/ok) at **#1, 370 ★** — 🟢 **`397-A`'s correction reproduced blind
through a channel that ranks by the disputed field, without re-reading the repository.** 🔴 Nine of
that page's ten rows were already shelved and the tenth is archived, so this tier should be treated
as **covered**, not under-harvested. `Gap 398-C` · `Gap 398-D`.

**Pass `p397` · reads and commit both 2026-10-23 — the THIRD pass dated today, after `p395` and
`p396`.** 🟢 **`p396` ranked running its fork arm over the existing shelf FIRST. It is done: 551
candidate pairs derived with no network, 21 adjudicated — and the arm's own verdict label turned out
to be wrong.** 🔴 **And a superlative this base has published in five places across three passes is
refuted by a row this base already held.** Evidence:
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv) — 21 pairs ·
[`shelf-fork-candidates`](../evidence/shelf-fork-candidates.2026-10-23-p397.tsv) — 121 groups ·
[`record-layer-redating`](../evidence/record-layer-redating.2026-10-23-p397.tsv) — 22 addresses ·
[`verified-repos`](../evidence/verified-repos.2026-10-23-p397.tsv) · instrument and controls at
[`p397-shelf-fork-audit`](../compose/code/p397-shelf-fork-audit/README.md).

### 🔴 The correction first: `okpy/ok` is the most-starred autograder on these shelves, and it is not close

`p394` published — and `p395`, `p396` carried — *"`gradethis` at 164 ★ edges `otter-grader` at
161 ★, so the most-starred autograder on these shelves was never the Python one, and it is MIT."*

🔴 **That is false, and the refuting row was already on these shelves when it was written.**
[`okpy/ok`](https://github.com/okpy/ok) — **Apache-2.0**, **370 ★**, **UC Berkeley** — has been
carried here since `pass 85`, and [`agents/trending.md`](trending.md) names it **in the same
comparison group as `otter-grader`**, one line apart. Re-read first-hand this pass: **370 ★**,
Apache-2.0, 88 forks, 🟢 **no archived banner**, HEAD `f5610a7` **2025-05-07 — 532 d**.

| autograder | licence | ★ | HEAD | days |
|---|---|---|---|---|
| [`okpy/ok`](https://github.com/okpy/ok) | 🟢 Apache-2.0 | **370** | `f5610a7` | 🔴 **532** |
| [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | 🟢 MIT | 164 | — | 🟡 126 |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 BSD-3-Clause | 161 | — | 🟢 21 |

🔵 **The claim holds only under a qualifier nobody wrote down: *"excluding the stale ones."*** That
qualifier is defensible — 532 days is not a base a studio should start on — but it is a **judgement
that belongs in the sentence**, and leaving it out turned a reasonable preference into a false fact.
🔴 **The failure mode is not the arithmetic, it is the denominator**: a superlative was derived over
the rows the author was looking at rather than over the shelf, and three passes re-published it
without re-deriving it. 🟢 **Corrected at all EIGHT live-shelf sites** that carried it — four on this shelf, two on
[`repos/foundations.md`](../repos/foundations.md), two in [`compose/patterns.md`](../compose/patterns.md) —
rather than only here. 🔵 **The two mentions in `agents/trending.md` and `repos/trending.md` are left
exactly as written**: those shelves are append-only history, and a correction belongs in a new dated
entry, not in a rewrite of the entry that got it wrong. 🔵 **This paragraph's own first draft said
"five places" before the sites were counted** — the same not-deriving-the-denominator error, one
screen above its own diagnosis. `Gap 397-A`.

### 🟢 `396-F`'s arm, run over the shelf — and the label it returns is wrong

🟢 **`396-F` stated the blocker honestly:** *"it needs a suspected upstream to compare against —
discovery of the pair is still WebSearch's job."* 🟢 **So the pairs were derived from the shelves
instead, with no network at all:** two addresses sharing a repository **name** under different
**owners** are a candidate. **2 694 harvested → 34 rejected → 2 660 addresses → 121 collision
groups → 551 candidate pairs.** The denominator is **p351's, imported rather than re-implemented**,
so it agrees with the published channel-U census to the address.

🔴 **21 pairs adjudicated, and the headline is that `SHARED-ROOT -> FORK LINEAGE` over-claims.** A
shared root commit is shared **ancestry** — equally implied by a fork, an organisation **rename**, a
repository **transfer** and a re-push. 🔵 **This is the `Trend 25` error inside the instrument built
to fix `Trend 25`**, which is worth stating plainly rather than quietly patching.

🟢 **The discriminator is one extra field off the same clone:** compare HEAD as well as root.

| verdict | n | what it means | examples |
|---|---|---|---|
| 🔴 `SAME-REPO-ALIAS` (shared root, **same HEAD**) — 🔵 **`p402`: `ease`'s canonical is a THIRD address, `openedx-unsupported/ease`; `ACTION ZZ-al` CLOSED** | **8** | **ONE artefact, TWO shelf addresses** — a census duplicate, not a fork | `1EdTech`↔`IMSGlobal` ×3 (the standards-body rename), `edx`↔`openedx` `ease`, `pytorch`↔`meta-pytorch` `opacus`, `kantord`↔`LibreLingo`, `digitalcredentials`↔`openwallet-foundation-labs` |
| 🟢 `DIVERGENT-FORK` (shared root, **different HEAD**) | **7** | two artefacts, one ancestry — a real choice to adjudicate | `DavidLMS`↔`ashleycribb` `learnmcp-xapi` (`p396`'s catch, reproduced blind), `dmitry-viskov`↔`ucfopen` `pylti1.3`, `EleutherAI`↔`latam-gpt` `lm-evaluation-harness` |
| 🟢 `INDEPENDENT` (distinct roots) | **4** | same name, unrelated code | `OpenLRS`, `qti-convert`, `ims-lti`, `lrs` |
| 🔵 `INCONCLUSIVE-UNRESOLVABLE` | **2** | 🔵 never called INDEPENDENT from a failed read | `apereo/opencast` (404 — 🔵 **already known dead since `p230`**, see below), and the base's own dead-address control |

🟢 **The control that matters most:** `agent0ai/agent-zero` ↔ `frdel/agent-zero` returns
`SAME-REPO-ALIAS`, and the committed alias register — built `p349` by a **completely different
method** (the search index's `full_name`) — already records exactly that relation. 🔵 **Two
independent methods, one answer.**

### 🔵 A near-miss worth publishing: the arm's one `404` is a CORROBORATION, not a discovery

🔴 **This pass's draft announced `apereo/opencast` as "a dead
address that fell out of the audit." It is nothing of the kind, and checking the tree before
publishing is what stopped it.** This base **proved** that address dead at **`p230` on 2026-10-15**,
carries the successor mapping on [`repos/foundations.md`](../repos/foundations.md) *(twice)* and in
[`repos/trending.md`](trending.md), and holds it in a **`dead-successor-register`** built for exactly
this row. `opencast/opencast`'s **ECL-2.0** grant and its 🔴 **`develop`** default ref are both
already shelved too — so the *"a ref-guessing probe would miss this"* line the draft reached for was
also already owned.

🟢 **What is genuinely worth recording is the arm's behaviour:** handed a pair where one side does not
resolve, it returned **`INCONCLUSIVE-UNRESOLVABLE`** and 🟢 **declined to call the other side
`INDEPENDENT`** — which is the control `C10` exists for, and the `p393` false-`UNGRANTED` class
avoided by construction. 🔵 **A third method agreeing with a register built by two others is a real
result; it is just not a new address.** 🔴 **`p393`'s warning — *"a new discovery channel's first
temptation is to re-sell what you already own"* — has now fired on three consecutive passes, and
`p397` is the one where it fired twice** (here, and on the `topic:education` candidates below).

🔴 **Stated as a backlog, not a result: 551 pairs derived, 21 adjudicated, 530 unexamined.**

### 🟢 Three new addresses, every grant read by enumerating the tree

🔵 Found through `396-A`'s reopened enumeration channel using **curated topics** rather than free
tokens — `topic:autograder` returns **124** results where the free-token query returned general
agent infrastructure (`393-A`, confirmed again).

| Address | Licence — read first-hand | ★ | HEAD | Note |
|---|---|---|---|---|
| 🆕 [`gradescope/gradescope-utils`](https://github.com/gradescope/gradescope-utils) | 🟢 **MIT** · `LICENSE`, 1,070 B, `sha256`₁₆ `1fa57a15a75b` · © 2022 **Turnitin, LLC** | **38** | `5689b27` · **69 d** | Python package for building **Gradescope** autograders. 🔵 The grant is **Turnitin's** — Gradescope's owner — so this is a commercial vendor's permissive client library, not a university project. The cheapest path to an autograder a US institution **already licenses**. |
| 🆕 [`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples) | 🔴 **UNGRANTED AT ROOT** — no licence file anywhere in the tree except two **vendored** copies at `java/src/main/java/com/gradescope/jh61b/LICENSE.txt` and `java_template/src/com/gradescope/jh61b/LICENSE.txt` (both 1,075 B, `8a6114b1d4ae`, MIT © 2016 Josh Hug) | **91** | `6832253` · **69 d** | 🔴 **`p382`'s subtree axis, in its purest form: 91 ★ and the only MIT in the tree belongs to somebody else's library.** 🟢 **GitHub shows no licence either**, so this base's verdict and GitHub's agree — unlike `p394`'s README-ONLY class where both were wrong. **Read the samples, do not vendor the repository.** |
| 🆕 [`TricksterGuy/complx`](https://github.com/TricksterGuy/complx) | 🟡 **GPL-3.0** · `LICENSE`, 32,422 B, `963392e038d7`; plus vendored Scintilla at `lc3edit/wxScintilla/src/scintilla/License.txt` (868 B, `94a798c912d4`) | 68 | `73ce7ab` · 🔴 **1 392 d** | LC-3 teaching simulator. 🔴 Copyleft **and** four years dead — shelved so a successor does not re-find it. 🔵 Its Scintilla payload carries *"All Rights Reserved"*, the exact phrase `P459` had to stop treating as a non-grant. |

### 🔴 Found this pass and DECLINED — because this base already holds every one of them

🟢 `topic:education topic:ai stars:>30` on the reopened channel returned **48 results**, and the top
of that list looks like a haul: `learnhouse/learnhouse` (**2.4k ★**, HEAD **0 d**),
`CaviraOSS/PageLM` (**2k ★**), `echo-loop/Echo-Loop` (**4.2k ★**), `penecho/penecho` (**2.5k ★**).

🔴 **All four are already on these shelves** — `learnhouse` appears in **129** files here, `PageLM`
in **56**. 🔵 **Checked before writing, not after**, which is the only reason this section says
"declined" instead of "discovered". 🟢 The genuinely new supply from the same channel is the **three
rows above**, and it came from `topic:autograder`, not from the education topic at all.

🔵 **The lesson is about the channel, not the pass:** a topic query sorted by stars returns a
region's **most adopted** repositories, which is precisely the set a mature base has already
harvested. 🟢 **The new supply sits further down the adoption curve**, which is where
`topic:autograder`'s 124 results had it.

### 🟡 `396-H` re-dated, as `p396` asked — the bridge has not moved

| Address | `p396` | `p397` | verdict |
|---|---|---|---|
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | 419 d, HEAD `fbf6091` | 🔴 **419 d, HEAD `fbf6091` — byte-identical** | 🔴 **Unmoved.** The entire open-source agent↔LRS supply is one 15 ★ repo, fourteen months dead, under every logging duty this base has recorded. 🟢 `396-H`'s *"fork and own it"* only gets stronger. |

**🆕 Pass `p396` · reads and commit both 2026-10-23.** 🔴 **No new education-native agent cleared
this pass, and the honest headline is that the one the search channel offered was a fork of a dead
project.** The supply finding is stated here rather than padded over:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv) — 28 addresses.

### 🟡 The one agent address worth shelving, with its defect on the same line

[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) — 🟢 **MIT** (1,069 B,
`sha256`₁₆ `4aa758cb51b2`, read first-hand), **15 ★**, 4 forks, HEAD `fbf6091` — 🔴 **2025-08-29,
419 days** — is an **MCP server that lets an agent read and write a learner's xAPI record** in a
conformant Learning Record Store. Backends named in its README: `lrsql`, Ralph LRS and Veracity.

🔵 **Why a 15 ★ repo is worth a row at all.** It is the *only* address found in this pass that joins
an agent to the record layer. Every tutoring agent on this shelf keeps its own memory — `DeepTutor`'s
lifelong memory, `inno-agent`'s L1/L2/L3 layers — and **none of them writes to the institution's
LRS**, which is where a registrar, a regulator or a credential actually looks. 🔴 **So the integration
every enterprise engagement needs is served by one MIT repo that has not moved in fourteen months.**
That is a gap in the open-source supply, and it is also the clearest build opportunity this base has
surfaced for Globant — see `Pattern AD`.

🔴 **Do not take the address search returns for it.** The first result is
[`ashleycribb/learnmcp-xapi`](https://github.com/ashleycribb/learnmcp-xapi) — **0 ★**, a fork — whose
licence payload is byte-identical to upstream's, so the grant channel cannot tell. It was caught by
this pass's new arm (`396-F`), which reproduces `p395`'s catch blind:
[`p396-fork-provenance-arm`](../compose/code/p396-fork-provenance-arm/README.md).

### 🔴 Rejected this pass, and why — so a successor does not re-spend a leg on them

| Address | Found by | Rejected because |
|---|---|---|
| [`ashleycribb/learnmcp-xapi`](https://github.com/ashleycribb/learnmcp-xapi) | WebSearch, first result | 🔴 **fork** of `DavidLMS/learnmcp-xapi`; shared root commit `95ba79652b92` |
| [`jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada`](https://github.com/jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada) | Spanish leg | 🔴 **not open source.** Grant read first-hand: 1,262 B, `33a3bb8713ec`, *"Licencia Comunitaria de Uso Profesional"* — a bespoke licence. 1 d old, active, genuinely a teacher-agent environment — and **unusable by a studio** |
| [`lbhubedu/lbedu.me`](https://github.com/lbhubedu/lbedu.me) | Portuguese leg | 🟡 MIT (2,118 B, `18272c548223`), 4 d — but it is a **recipe collection** (prompts, MCPs) in pt-BR, not an agent. Out of class, recorded so it is not re-found |
| `DannyAvilaL/agente_clases`, `BrayanG877/ia-educativa-reto` | Spanish leg | 🟡 personal course projects; no grant surfaced, no adoption |

🔵 **The Spanish and Portuguese legs are still the right change** — `p395` broke a six-pass dry spell
on one, and this pass's only *active* education-native agent (`Aula`) came from the same leg. 🔴 **But
`387-D` should now be amended rather than simply repeated: the non-English legs find live projects
with non-OSI licences.** Two passes, two Spanish-language finds, and the licence was the blocker
once. Add *the grant read* to the leg, not just the search.


# Top education AI agents

**🆕 Pass `p395` · reads and commit both 2026-10-23.** 🟢 **The first education-native agent this
base has added in six passes, and `Gap 387-D` is finally specific about why the dry spell happened.**
[`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) — 🟢 **MIT** (1,080 B, `sha256`₁₆
`f92c6c6a1cc8`, read first-hand), **1.3k ★**, 231 forks, HEAD **2026-10-13 — 10 d** — is an
*"open-source personal learning agent"* with three explicit memory layers (**L1** learner profile,
**L2** a native wiki knowledge base, **L3** session records with cross-conversation retrieval), a cron
scheduler, personal IM channels and a workspace-scoped **Practice Lab** with an in-browser terminal.
Technical report *"Inno Agent: An Open-Source Personal Learning Agent with Layered Memory, Educational
Post-Training, and Local Deployment"* (arXiv, June 2026), authors **Hao Hao, Ye Lu, Ruotong Yang,
Yongheng Guo, Aimin Zhou**, with preliminary post-training results on **Qwen3.6 35B**.

🟢 **Its region is placed on a functional signal, not on author names.** The shipped IM channels are
**Feishu and WeChat** — the two China-market messengers — so this is **APAC** supply by what it
integrates with, which is the kind of evidence this base can defend at a client meeting. No institution
is stated anywhere in the README or on the repository page, so the *holder* stays **unplaced**.

🔴 **And the caveat is the part that changes a proposal.** The agent is MIT; its companion
[`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) — the **skill library
and workspace presets**, which is the content a studio would actually want to reuse — is
**UNGRANTED on every arm**: no licence-shaped file, no manifest field, no README grant, all three
enumerated this pass. 🔵 This is `Gap 549`'s shape again (a code grant and a content grant in one
project), and it means *"inno-agent is MIT"* is true and misleading at the same time: the kernel is
granted, the curriculum around it is not.

🟡 **Architecture note worth a line in any pitch:** it is built on the **Pi coding-agent SDK**
(`@earendil-works/pi-coding-agent`, MIT) *"without modifying its kernel"* — a coding agent repurposed
into a learning agent. That is a reusable move, and it is cheaper than the tutoring frameworks on this
shelf that own their whole runtime.

### 🔴 `Gap 395-A` — WebSearch returns FORKS, and a licence read cannot tell

**Three of the four addresses this pass's search legs handed over were forks, and the licence payloads
were byte-identical to their upstreams, so nothing in the grant channel could reveal it.**

| Address returned by search | Stars | Canonical | Stars |
|---|---|---|---|
| [`Poki-cbq/inno-agent`](https://github.com/Poki-cbq/inno-agent) | **0** | [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) | **1.3k** |
| [`astiusa/lti`](https://github.com/astiusa/lti) | **0** | [`macewan-cs/lti`](https://github.com/macewan-cs/lti) | **8** |
| [`drop-project-edu/java-lti-1.3-core-for-dp`](https://github.com/drop-project-edu/java-lti-1.3-core-for-dp) | **0** | [`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) | — |

🔴 **The existing alias gate does not catch this.** `gate-alias-canonical` keys on an **identical HEAD
sha**, which is what an *org rename* produces. A fork has a **different** HEAD sha, an **identical**
licence payload and a **different** star count — so it passes the alias check and fails the
provenance question. 🔵 **Only the HTML channel shows it**, in a `forked from` line that neither
`raw.githubusercontent.com` nor the git dating channel carries. Had this pass shelved what search
returned, it would have published a **0 ★ row for a 1.3k ★ project** — and `drop-project-edu`'s own
README says the plainest version of it: *"a fork of the LTI 1.3 shared library, with no source code
modification, just for convenience"*.

🟢 **Cheap remedy, and it is one read per new address:** before shelving, fetch the repository page and
reject any address carrying `forked from`, then re-probe the upstream. This pass did that by hand for
four addresses; it should be an arm, because every address this base acquires now arrives through the
one channel that returns forks preferentially.

### 🟡 Found and declined this pass, with the reason

Stated rather than dropped, so a successor does not spend the same legs again:

- [`naorpeled/aitutor`](https://github.com/naorpeled/aitutor) — 🟢 MIT, HEAD **2026-09-05 — 47 d**, Go.
  🔴 **A course, not an agent**: a terminal tutorial *about* AI tooling (context windows, MCP,
  subagents). Declined under `p394`'s own rule that a course is not supply.
- [`Priyamakeshwari/TeachGPT`](https://github.com/Priyamakeshwari/TeachGPT) — 🟢 MIT, 🔴 HEAD
  **2023-11-30 — 1,057 d dead**.
- [`x-cookie/agent`](https://github.com/x-cookie/agent) — 🔴 a 14-lesson agent-building course, and
  **ungranted** on every arm.

🔵 **Dating note — this pass straddles midnight UTC, and the two dates are not interchangeable.**
Every clone, tree enumeration, licence payload read, star read, archived-banner read, registry probe
and search leg below was run on **2026-10-22**; the commit lands **2026-10-23**. Evidence filenames
carry **2026-10-22** because that is the measurement date, and the frontmatter carries **2026-10-23**
because that is when the shelf was written. Stated rather than smoothed, because `gate-dates` exists
to stop this base asserting a date it has already refuted, and a silent redating of 15 first-hand
reads is exactly that.

**Pass `p394` · reads 2026-10-22, committed 2026-10-23.** 🟢 **`Gap 393-F` is discharged, and its
answer is the opposite of its prediction.** `p393` ranked one audit first: re-read every `UNGRANTED` row with `git ls-files`,
because `p393` had just manufactured a false absence from a closed filename list. That audit ran here
over **all 11 re-readable condemned addresses**, with the whole tree enumerated, plus three arms no
prior pass ran on those rows — SPDX identifiers, manifest fields, and the README. 🟢 **On the predicted
class it is 11 for 11 clean: not one licence-shaped file at any path in any of the eleven trees**, so
`p393`'s `LICENSE.LGPL-3.0` miss was a **singleton, not a symptom**, and a successor need not go
hunting the filename space again. 🔴 **But two of the eleven are refuted anyway, by the README** —
[`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) and
[`jarodise/Language-Transfer`](https://github.com/jarodise/Language-Transfer) both carry a plain MIT
grant in their README, and `p288` made the README a standing grant channel **roughly a hundred passes
before `p386` condemned them**. 🔵 **The gap named the right rows and the wrong defect.**

🔴 **And `bbmcps` is wrong twice.** It is **not a Blackboard Learn integration at all**: zero
occurrences of `blackboard.com`, no Learn REST call, no OAuth, dependencies `mcp` and `sqlite3`, and
a `blackboard://` scheme that is the **blackboard architectural pattern** — shared memory and a
knowledge graph, credited in its own README to `dx-corp/shared-memory-mcp`. The Blackboard family on
this shelf drops from **nine addresses to eight**, and the one "ungranted Blackboard server" leaves
the family entirely. 🔵 **This is `Gap 393-A` found on this base's own shelf rather than in a new
channel: a token was read as a capability, and it has been sitting in the census for eight passes.**

🟢 **`Gap 393-G` is half closed, and the half that failed is worth more than the half that worked.**
`p393` asked for a CRAN channel. **CRAN is refused on BOTH tools** (`curl` 000, `WebFetch` ENOTFOUND),
and so is r-universe — so unlike `Gap 532`'s asymmetry this is a real absence, not a tool artefact.
🟢 **But `github.com/cran/<pkg>` read-only-mirrors every CRAN package including its `DESCRIPTION`**, so
an R grant is verifiable first-hand without CRAN, with a calibrated oracle behind it (`catR`, `TAM`,
`learnr` present; `gradethis`, `qti` and a nonsense control absent). 🔴 **It verifies and cannot
discover** — name to package, never capability to names. 🔵 **And the irony is load-bearing:
`cran/gradethis` is ABSENT, because the one permissive autograder this pass found is not on CRAN. The
index `Gap 393-G` asked for would have missed the best row it produced.**

🔴 **The pass's most expensive finding is in this base's own licence gate, and it produces false
absences of GRANTS.** `licence-grant-gate` returned **`granted: False` on verbatim, unmodified
BSD-3-Clause**. The trigger is the literal phrase **"all rights reserved"** — carried in the gate's
non-grant marker list since `P455`, and **line 2 of the canonical BSD-3 and BSD-2 templates**. The
mechanism was isolated by experiment, not inferred: adding a title line changed nothing, removing the
phrase flipped the verdict. 🟢 **`P455`'s own specimen does not contain the phrase at all** — re-read
200 today, 869 B, `sha256`₁₆ `c341a936e405b61d`, its refusal resting on four other markers — so the
marker was never load-bearing for the defect it was added for. It was pure false-positive surface.
🟢 **Fixed, with twelve controls including two negative ones that keep the old defect reproducible**
(`P459`; the gate's suite went 47 → 59, and `make hooks` holds at its inherited **44/46**). 🟡 **The
realised damage on these shelves is NIL and that is stated rather than inflated**: no published row
was ever graded from an untitled BSD payload. The exposure was prospective, over **297 BSD-3-Clause
and 201 BSD-UNVERSIONED cells**, and it fired for the first time on this pass's own candidate.

🔵 **Three instances, one root cause, and `p393`'s ranked item 5 should now be read as ranked item 1.**
`Gap 392-A` over-refutes on a runtime key. `Gap 393-A` over-discovers on a name. `P459` strips a grant
from a payload that plainly makes one. **All three are a string matched as though it were a meaning**,
and the gate already holds the right concept one screen away — `AMBIGUOUS_WORDS = ("apache", "nginx",
"mit", "bsd")`, with a comment saying each is simultaneously a licence name and something else. The
base applied that insight to licence **names** and never to licence **clause text**.

**Pass `p393` · 2026-10-22.** 🟢 **`Gap 392-C` is closed by an artefact that costs 1.4 seconds.** `p392`
registered *"there is no Python package DISCOVERY channel, and that is why `Gap 391-A` was invisible"*,
and asked a successor to look for *"a mirror, an index dump, or accept that Python supply is found
through GitHub and papers only."* **The index dump exists:** PEP 691 serves the whole simple index as
JSON at `pypi.org/simple/` — **45,189,043 B, 920,784 project names, HTTP 200, unauthenticated**. The
first sweep over 24 token-exact education keys returned **507 name hits → 15 distinct addresses**, of
which **13 are live and verified first-hand** here. 🔴 **Against ZERO granted addresses from all four
prescribed English legs**, run the same hour. 🔴 And it refutes `Gap 391-A` a second time: not three
Python LTI implementations but **five**.

**Pass `p392` · 2026-10-22.** The shelves below are the deliverable: real repositories, licences read
from the payload, and a **last-commit date on every row**. This pass **builds the instrument `p391`
ranked first** — an absence check keyed on *capability* rather than on string identity — and its first
run refutes **all three gaps `p391` opened eight hours earlier**, every refutation already sitting in
this base's own harvest log. It also **reopens the popularity channel** eleven passes after this base
declared it closed, and the first thing the stars do is overturn a superlative on this very shelf.

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p392.tsv) — 15 addresses, every
licence read from the payload at the **real default ref** ·
[`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv) — 24 channels measured **per tool** ·
[`capability-absence-census`](../evidence/capability-absence-census.2026-10-22-p392.txt) — 364 absence
sentences adjudicated · the instrument and its 11 controls at
[`compose/code/p392-capability-absence/`](../compose/code/p392-capability-absence/README.md).

## What `p394` changes

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p394.tsv) — 17 rows ·
[`ungranted-reread`](../evidence/ungranted-reread.2026-10-22-p394.tsv) — `Gap 393-F`'s audit, all 12
condemned addresses with four arms each ·
[`channel-state`](../evidence/channel-state.2026-10-22-p394.tsv) — 14 channels **per tool** ·
[`regional-legs`](../evidence/regional-legs.2026-10-22-p394.tsv) — 11 legs · the gate fix and its 12
new controls in [`compose/code/licence-grant-gate/`](../compose/code/licence-grant-gate/grant_gate.py).

| # | finding | where it bites |
|---|---|---|
| 1 | 🟢 **`Gap 393-F` DISCHARGED — 11 of 11 clean on the predicted class.** Every re-readable `UNGRANTED` address re-read by **tree enumeration**, not by a path list: `loyaniu/moodle-mcp` (13 files), `Seechange-edu/act-ai-tutor-backend` (3), `Nutlope/llamatutor` (46), `Daniel-ux1026/Tutor-Inteligente` (145), `FXArth/Tutor-Programacao` (12), `henriquebotelhogomes/educacao` (211), `anastasasenov/bbmcps` (9), `jarodise/Language-Transfer` (42), `DMontgomery40/mcp-canvas-lms` (36), `general-mudkip/d2l-mcp-server` (54), `onbirdev/moodle-webservice_mcp` (20). **Zero licence-shaped files at any path in any tree**, and **zero SPDX identifiers** — an arm no prior pass ran. 🟢 So `p393`'s false absence was a singleton. | 🟢 **A negative result that buys something: the filename space is NOT the leak**, and the next pass can stop widening path ladders. `santillana-ai/tutor-sdk` is excluded and said so — a tree that cannot be cloned cannot be enumerated. |
| 2 | 🔴 **Two condemned rows REFUTED — by the README, which `p288` made a standing channel ~100 passes before `p386` condemned them.** [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps): *"This project is open-source and available under the MIT License."* (`readme.md:84`). [`jarodise/Language-Transfer`](https://github.com/jarodise/Language-Transfer): `## License` → `MIT` (`README.md:167`, **31 ★**). Both carry **no** licence file and **no** manifest, and 🔴 **GitHub's own sidebar shows no licence for either**, so the base's verdict and GitHub's agree — and both are wrong. | Rows corrected below and in the provenance table. New class: **README-ONLY** — one rung weaker than `p383`'s MANIFEST-ONLY, because nothing machine-readable asserts it. 🔵 **The lesson is not "add the README to the probe": the gate for it already existed. The verdict pipeline did not call it.** |
| 3 | 🔴 **`bbmcps` is not a Blackboard integration, and the census has carried it as one for eight passes.** No `blackboard.com`, no Learn REST, no OAuth; dependencies `mcp` + `sqlite3`; `blackboard://` is the **blackboard architectural pattern** (shared memory, knowledge graph), credited in its own README to `dx-corp/shared-memory-mcp`. **Blackboard: 9 → 8 addresses**, and the family's only ungranted row leaves it: **8 probed = 6 MIT + 2 dead, 0 ungranted.** | Census and the measured-supply table corrected below. 🔵 **This is `Gap 393-A` on this base's own shelf**, not in a new channel — and it is the strongest argument for `p393`'s ranked item 5, because it shows the defect does not only mis-discover, it mis-*files* what it already owns. |
| 4 | 🔴 **`licence-grant-gate` read `granted: False` on verbatim BSD-3-Clause — a false absence of a GRANT, the most expensive error class this base has.** Specimen: `open-webui/LICENSE` vendored inside `Lamb-Project/lamb`, 1,510 B, `sha256`₁₆ `6c4b8d8034b9`, stock BSD-3 and **untitled**. Cause isolated by experiment: the phrase **"all rights reserved"**, in the gate's `NON_GRANT_MARKERS` since `P455` and **line 2 of the canonical BSD-3/BSD-2 templates**. Title made no difference; removing the phrase flipped the verdict. 🟢 `P455`'s own specimen (`murderszn/open-tutor`, 869 B, `c341a936e405b61d`, re-read **200** today) **contains the phrase nowhere** — four other markers carry its refusal. | 🟢 **Fixed as `P459`**, the marker made conditional on the absence of an operative grant sentence; **12 new controls, 2 of them negative** so the old defect stays reproducible; suite **47 → 59**; `make hooks` unchanged at its inherited **44/46**. 🟡 **Realised damage: NIL** — no published row was graded from an untitled BSD payload. Exposure was prospective across **297 BSD-3-Clause + 201 BSD-UNVERSIONED** cells. |
| 5 | 🟢 **`Gap 393-G` half closed: an R supply tier exists, and three of its rows are PERMISSIVE.** 🟢 [`rstudio/gradethis`](https://github.com/rstudio/gradethis) — **MIT**, `sha256`₁₆ `48c18e68ffed`, **164 ★**, 41 forks, HEAD **126 d**, Posit Software PBC. 🟢 [`rstudio/learnr`](https://github.com/rstudio/learnr) — **Apache-2.0**, `60a581bccd57`, **738 ★**, 241 forks. 🟢 [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) — **BSD-3-Clause**, `1677c5307530`, the R extension **for `otter-grader`**, this base's most-adopted autograder. Plus GPL psychometrics: [`philchalmers/mirt`](https://github.com/philchalmers/mirt) (**235 ★**, HEAD **1 DAY**), [`patriciamar/ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) (**47 ★**), `cran/catR` (**computerized adaptive testing**), `cran/TAM`. | New **Tier 6** below; rows on [`repos/foundations.md`](../repos/foundations.md); **`Trend 24`**; new **`Pattern AB`**. 🔵 **`gradethis` at 164 ★ edges `otter-grader` at 161 ★** — so the most-starred autograder on these shelves was never the Python one, and it is MIT. 🔴 **`p397` correction: refuted as written.** `okpy/ok` (Apache-2.0, **370 ★**, Berkeley) was already on these shelves when this was published; the claim holds only for *maintained* rows — see `Gap 397-A`. |
| 6 | 🟢 **`cran/exams` is the broadest assessment exporter on these shelves, and it lands directly on `p393`'s new Tier 8.** R/exams v2.4-5 (Achim Zeileis, R-project) emits **QTI 1.2, QTI 2.1, Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS, TestVision, Particify, ARSnova, Kahoot!, Grasple, TCExam** — read from the `R/` source filenames in the clone, not from prose — plus **NOPS**: printed, scanned, automatically marked PDF. 🟡 **GPL-2 \| GPL-3, disjunctive** — the licensee picks the rung. | 🔵 Compare `p393`'s [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker): LGPL-3.0, **4 ★**, Canvas and Blackboard only. **The QTI story on this shelf changes shape**: the generator with the widest reach is GPL and ten years old, not the new LGPL one. 🟢 **NOPS is the paper-assessment path** — the one thing in this whole base that works where connectivity does not. |
| 7 | 🟢 **A no-code LLM-assistant builder that publishes into Moodle over LTI, and it is EMEA-authored and peer-reviewed.** [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb) — **GPL-3.0** (35,349 B, `17fe6d0ffa96`, stock GPL-3 under a four-line project header), Marc Alier (**UPC Barcelona**) and Juanan Pereira (**UPV/EHU**), 7,087 files, HEAD **2 d**, published in *Computer Standards & Interfaces*. Companion [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) is the **LTI activity module for assignments graded by a LAMB assistant**. 🔴 A Moodle.org thread (Feb 2026) calls it *"at a very beta stage"* with *"a few universities running pilots"* — carried on every LAMB row, because a 2-day HEAD reads as momentum and the forum reads as pilot-stage. | New row below and on [`verticals/solutions.md`](../verticals/solutions.md); **`Pattern AC`**. 🔴 **Three grants in one tree** (`p382`'s subtree axis): root GPL-3, `lamb-kb-server-stable/` stock GPL, and the vendored `open-webui/` BSD-3 — the last being the specimen that exposed `P459`. 🔴 **Fold recorded:** `Lamb-Project/LAMBA` is the same repository as `lamba` (identical head `87e203a`, identical payload `sha256`), published once per `p348`. |
| 8 | 🔴 **`Gap 393-G`'s channel question answered precisely, and the answer is a per-tool absence.** CRAN: **`curl` 000 proxy-refused, `WebFetch` ENOTFOUND** — closed on **both** tools, so unlike `Gap 532` this is a real absence rather than a tool artefact. r-universe, the obvious substitute: **also refused**. 🟢 The substitute that works is **`github.com/cran/<pkg>`**, a read-only mirror of every CRAN package's `DESCRIPTION`, with a calibrated oracle: `catR`/`TAM`/`learnr` present, `gradethis`/`qti`/nonsense-control absent. 🔴 **It verifies; it cannot discover.** | [`channel-state`](../evidence/channel-state.2026-10-22-p394.tsv). **`Gap 394-C`** asks for the one missing piece: an org listing for `cran` (≈22,000 packages) would turn the lookup mirror into an index. 🔵 **Also localised: `api.github.com` 403 is SESSION REPOSITORY SCOPING, not a proxy block** — earlier cycles recorded it as "github-api-proxy-blocked", which pointed at the wrong remedy. |
| 9 | 🔴 **Three R grants live ONLY in `DESCRIPTION`, and GitHub's sidebar shows no licence for any of them.** `cran/exams`, `mirt` and `ShinyItemAnalysis` carry **no licence-shaped file at any path**. 🟢 **This base already knew the rule** — `p1052` holds `DESCRIPTION` in its manifest list with a test asserting *"CRAN: the grant lives in DESCRIPTION and must be read verbatim"*, and `p122` has a `STUB-SEE-DESCRIPTION` verdict — so this pass does **not** publish it as a discovery. 🔴 **But `licence-grant-gate` does not know it**: `DESCRIPTION` is in neither its path ladder nor its `EXISTENCE_PATHS`. | **`Gap 394-B`**: the knowledge is in the base and not in the instrument that produces the verdicts. 🔵 **And a second ordering defect beside it:** the ladder is **first-hit-wins** with `LICENSE` at position 0 and `LICENSE.md` at position 1, and R's convention puts a **49-byte year/holder stub** at `LICENSE` with the real text at `LICENSE.md`. On `rstudio/gradethis` the gate therefore returns `NON-GRANT` from the stub while extracting the holder correctly — **`Gap 394-A`**. 🔴 Neither a wider path list nor tree enumeration can fix that one, so `Gap 393-F`'s remedy would never have caught it. |
| 10 | 🔵 **`Gap 387-D`, fifth confirmation — with the failure mode newly specific.** Four English global legs: **0 granted addresses**, and every education-adjacent name they returned is already carried here as a course or a list. 🟢 **The EMEA leg reversed `p393`'s nil** and returned the EU AI Act's education trigger directly. 🟢 **The one leg that returned an address was the SPANISH one** — LAMB. | [`regional-legs`](../evidence/regional-legs.2026-10-22-p394.tsv). 🔵 `p393` showed an index beats the legs. **`p394` adds the other half: when the legs do return supply, it is the non-English leg that returns it.** Two passes, two distinct ways the prescribed English legs under-return. |
| 11 | 🟢 **`Gap 393-E`'s archived column, delivered rather than deferred.** [`Ed-Fi-Exchange-OSS/LMS-Toolkit`](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit): *"This repository was archived by the owner on Mar 10, 2025. It is now read-only."* — **591 days**, 11 ★, Apache-2.0. Seven further addresses read this pass carry a verified **not-archived**. | 🟢 `p393` was right that the cost is near zero: the `WebFetch` star read returns the banner in the **same** read. Column added to [`verified-repos`](../evidence/verified-repos.2026-10-22-p394.tsv) and to the dated tables below. |

## What `p393` changes

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p393.tsv) — 15 addresses ·
[`pypi-index-channel`](../evidence/pypi-index-channel.2026-10-22-p393.tsv) — the sweep, key by key, with
the **shelvable** count stated per key ·
[`channel-state`](../evidence/channel-state.2026-10-22-p393.tsv) — 14 channels **per tool** ·
[`regional-legs`](../evidence/regional-legs.2026-10-22-p393.tsv) — 10 legs ·
the instrument at [`compose/code/p393-pypi-index-channel/`](../compose/code/p393-pypi-index-channel/README.md),
wired as `make pypi-index-sweep`.

| # | finding | where it bites |
|---|---|---|
| 1 | 🟢 **The Python discovery channel exists and `Gap 392-C` is CLOSED.** `pypi.org/simple/` under `Accept: application/vnd.pypi.simple.v1+json` returns **920,784 project names in 45 MB in 1.4 s**, unauthenticated and unchallenged — while `pypi.org/search`, the channel `p392` probed, is still a bot-challenge page. 🔵 **The asymmetry `p392` feared was real and it was costly:** every registry sweep this base has run went through npm, so *"no maintained Python X"* meant *"npm search does not index PyPI"*. All thirteen live addresses below are **PyPI distributions with no npm package**, so an npm-only registry sweep cannot return any of them **by construction** — which is the asymmetry, stated as something checkable rather than as a count. | New instrument + `make pypi-index-sweep` / `make pypi-index-verify`. Rows below and on [`repos/foundations.md`](../repos/foundations.md), [`verticals/solutions.md`](../verticals/solutions.md). 🔵 **Two of the fifteen are corroborations, not discoveries**, and are marked as such: `otter-grader` and `loyaniu/moodle-mcp` were already carried here, and the channel re-derived both independently. |
| 2 | 🔴 **`Gap 391-A` is refuted a SECOND time, and `p392`'s own count of three was low.** Two further Python LTI 1.3 addresses, both 🟢 **MIT**, both read from the payload today: [`openfun/django-lti-toolbox`](https://github.com/openfun/django-lti-toolbox) (1,078 B, `sha256`₁₆ `504c17f9869b`; **France Université Numérique**, the French state's higher-education platform operator; HEAD `22c6f2f` **2024-11-14 — 707 days**; PyPI v2.0.0; **14 ★**) and [`Harvard-University-iCommons/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) (1,100 B, `1ade29a33914`; HEAD `2873d2f` **2025-09-15 — 402 days**; **3 ★**), which implements **LTI Dynamic Registration** — the one Advantage flow `p392`'s three rows left uncovered. 🔵 **Five Python implementations, from Michigan, Jupyter, Open edX, France and Harvard.** 🔴 Both new rows are **cold** (707 and 402 days), so `p392`'s *licence-shaped* generalisation gains a maintenance clause: the permissive Python LTI supply is **real, plural, and largely unmaintained**; the only one committed this month is AGPL. | `Gap 391-A` **stays closed, with its count corrected from three to five.** `Pattern B`'s pick is unchanged (`django-lti`, 2 days) and now has two named fallbacks and a Dynamic-Registration add-on. |
| 3 | 🟢 **A NEW SUPPLY CLASS: live releases, dead source — and the licence claim is unauditable.** `superbuilders/timeback-dev-python` (🔴 unlinked deliberately: an absent address, `gate-dead-citation` I2) is the declared `Repository` of **three** PyPI packages — `timeback-qti`, `timeback-oneroster`, `timeback-caliper`, **147 releases between them**, last **2026-07-18**, each declaring **MIT** and together forming a complete **1EdTech client family** (QTI, OneRoster v1.2, Caliper). 🔴 **The repository does not resolve for an unauthenticated clone**, so there is no payload to read: the MIT claim is **metadata-only and unverifiable in principle**, not merely unread. Second instance the same hour: `moodle-mcp-bridge` (v1.7.0, *"88 typed AI tools"*) → `NmaaAlhawary/MCP-Moodle`, also unresolvable. 🔵 **And this base already knew the first address was dead:** `p371`'s tree run and `p372`'s successor probe both recorded `superbuilders/timeback-dev-python` as `NO-REMOTE`, and `p372` searched for a shorter-name sibling (`superbuilders/timeback`) and found none. What `p393` adds is the *other* side of it — that this dead address is the declared source of **147 live MIT releases** — which is what makes it a supply class rather than one more dead link. | 🔵 **This is not `p388`'s "published but unreadable"** (a payload that exists and says nothing). It is a payload that **cannot be fetched at all** while the artefact ships. Registered as **`Gap 393-B`** and written into the ladder discussion on [`repos/foundations.md`](../repos/foundations.md). A studio may still *install* these; it may not *warrant* them. |
| 4 | 🔴 **A name is not a capability, and this channel's precision cost is measured, not estimated.** The dump carries **names only** — no summary, no classifier, no licence — so discovery is by token, and two of fifteen candidates were pure collisions: **`proctor-ai`** is a structured **prompt-engineering** library, and **`xapi-python`** is the **xStation5 broker API**, not Experience API. Whole keys failed the same way: **`canvas`** returns 146 names that are overwhelmingly HTML-canvas and AWS Nova Canvas, **`d2l`** is Dive-into-Deep-Learning, **`blackboard`** is mostly the drawing metaphor. | Both collisions are fixtures in [`test_fixtures.tsv`](../compose/code/p393-pypi-index-channel/test_fixtures.tsv) so the class is not re-learned. Registered as **`Gap 393-A`** — and it is `Gap 392-A`'s defect **arriving from the opposite direction**: that one over-refutes on a runtime key, this one over-discovers on a name. |
| 5 | 🔴 **This pass published an UNGRANTED verdict against a real grant, caught it, and the cause is a closed filename list.** [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) (QTI packages for Canvas and Blackboard, 381 commits, HEAD **2026-10-12 — 10 days**) was first read as having no licence, from a six-name probe (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.LESSER`, `LICENCE`). The grant is **LGPL-3.0** and sits at **`LICENSE.LGPL-3.0`** — 7,652 B, `sha256`₁₆ `e3a994d82e64`. 🟢 **Corrected by enumerating the tree** (`git ls-files | grep -i licen`) instead of guessing names. | **Enumerate; do not guess.** The method note on this shelf and in the instrument's README now says so. 🔵 A false *absence* of a grant is the same error class as a false absence of a repository — `Gap 392-A`'s family — and it was produced by the cheaper half of this base's own method. |
| 6 | 🟢 **The thing the channel actually found is a LAYER, not a repository: Python is where the LMS-to-agent bridge and the standards clients live.** Two new granted Moodle MCP servers ([`Dathis/swiss-moodle-mcp`](https://github.com/Dathis/swiss-moodle-mcp) 🟢 MIT, **EMEA/Switzerland**; [`Snaw80/moodle-mcp`](https://github.com/Snaw80/moodle-mcp) 🟢 MIT), a new **autograding** client ([`edulinq/autograder-py`](https://github.com/edulinq/autograder-py) 🟢 MIT, 49 releases) beside the already-carried [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader), **measured for the first time at 161 ★ / 197 releases**, the **Ed-Fi K-12 data path** for North America ([`edanalytics/edfi_api_client`](https://github.com/edanalytics/edfi_api_client) 🟢 Apache-2.0, HEAD **16 days**), **QTI conversion** ([`Citolab/qti-convert-python`](https://github.com/Citolab/qti-convert-python) 🔴 GPL-3.0, **Cito, the Dutch national assessment institute**), H5P inside Open edX ([`edly-io/h5pxblock`](https://github.com/edly-io/h5pxblock) 🟢 MIT, HEAD **6 days**), and 🟢 **a full permissive Python LMS from Nicaragua** ([`bmosoluciones/now-lms`](https://github.com/bmosoluciones/now-lms) 🟢 Apache-2.0, 676 files, 505 commits). | New rows below, on [`repos/foundations.md`](../repos/foundations.md) and [`verticals/solutions.md`](../verticals/solutions.md); `Trend 22` and `Trend 23` on [`intel/trends.md`](../intel/trends.md); new **`Pattern AA`** on [`compose/patterns.md`](../compose/patterns.md). 🔵 `now-lms` is the **LATAM-native platform row** this base's own LATAM section has been asking for since `p387`. |
| 7 | 🔴 **An archived repository and an ungranted one, both published as such rather than as "Apache" and "MIT".** [`Ed-Fi-Exchange-OSS/LMS-Toolkit`](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit) (Canvas / Google Classroom / Schoology extractors, 763 files) is 🟢 Apache-2.0 **and 🔴 ARCHIVED BY ITS OWNER on 2025-03-10 — read-only**, which the licence column alone would never show. [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) has **no licence-shaped file at any path in its tree and no licence field in `pyproject.toml`** — 🟢 **independently re-confirming this shelf's existing `UNGRANTED` row from a second channel**. | 🔵 **An archived-state column is missing from these shelves**, registered as **`Gap 393-E`**. The `WebFetch` star channel reads the archive banner for free, so the cost of adding it is near zero. |
| 8 | 🔵 **The prescribed legs, stated plainly, for a FOURTH consecutive confirmation of `Gap 387-D`.** All four English global legs: **0 granted addresses.** The four prescribed regional legs: **0 granted addresses**, 14 facts. 🔴 **The EMEA leg returned no education-sector content at all** — enterprise AI adoption only, one source dated 2023 — and that is written down rather than left silent. 🔴 And `p392`'s procurement-shaped replacement **does not generalise out of es/pt**: ported to French and German it returned **no ministry tender** for AI in education in France or Germany (it did return Aalborg University's *call for AI pilot projects 2026* and a Brazilian **MEC regulatory-sandbox** call). | [`regional-legs`](../evidence/regional-legs.2026-10-22-p393.tsv). 🔵 The comparison is the finding: **four prescribed English legs returned 0 addresses; one 1.4-second index fetch returned 15.** The brief's search legs are a **market-intelligence** instrument, not a supply instrument, and this base should stop asking them for supply. |
| 9 | 🔴 **A correction to a claim the North America leg carried as its headline.** *"Boston Public Schools became the first major US district to mandate AI fluency as a graduation requirement, starting September 2026"* is **not what the primary coverage says.** Boston runs a **$1M-funded district AI-literacy programme** with a curriculum built with UMass Boston; the **graduation requirement** is a **Massachusetts DESE proposal still in development**, recommended in June by the Statewide Graduation Council. 🔵 Two different bodies, two different instruments, one conflated sentence. | Corrected on [`intel/market.md`](../intel/market.md) under North America. Registered as **`Gap 393-C`**: this base holds **no** primary-source US state education-AI rule, and the secondary summaries it does hold have now been caught overstating one. |

## What `p392` changes

| # | finding | where it bites |
|---|---|---|
| 1 | 🔴 **`Gap 391-A` is wrong, and it is the fourth instance of the error `p391` diagnosed in the same breath.** `p391` published *"there is no maintained Python LTI 1.3 library… the interop edge must be a separate Node or PHP service in front of the agent"* across three shelves and two patterns. 🟢 **There are three Python LTI 1.3 implementations**, read first-hand today: [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) (🟢 **MIT**, 1,098 B, © The Regents of the **University of Michigan**; HEAD `1ac0b56` **2026-10-20 — 2 days**; PyPI `django-lti` **v0.10.1**, 17 releases, 2026-08-07; 264 commits, **26 ★**) — *"LTI Advantage support for Django"*, installed as one app plus one middleware, **in-process**; [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (🟢 **BSD-3-Clause**, 1,528 B; HEAD `c0c3bf3` **2026-07-01**; PyPI v1.6.3; 523 commits, **73 ★**) — **LTI 1.1 *and* 1.3** into JupyterHub; and [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) (🔴 **AGPL-3.0**, 34,520 B; HEAD **2026-10-22 — committed today**) — the best-maintained of the three and the one off the permissive shelf. 🔵 **Both halves of `p391`'s claim were in this base's harvest log already**, dated and licence-read, under tokens the absence never names. | **The second runtime comes out of the budget.** Corrected on [`repos/foundations.md`](../repos/foundations.md), [`verticals/solutions.md`](../verticals/solutions.md), [`intel/market.md`](../intel/market.md) (the EMEA engagement-cost line) and in `Pattern A` / `Pattern B` / `Pattern N`. `Gap 391-A` **CLOSED**. |
| 2 | 🟢 **`Gap 391-D`'s remedy is built, and it found findings 1, 3 and 4 rather than a human noticing them.** `p391` registered *"an absence check keyed on **capability** rather than on string identity"* as the top-ranked instrument for this pass, with the predicate it had itself corrected. [`p392-capability-absence`](../compose/code/p392-capability-absence/README.md) projects **both** sides into one capability space, so an absence written as *"no Python LTI 1.3"* meets a harvest row written as *"django-lti · LTI Advantage · PyPI"* although **the two share no token**. **15 controls green**, five of them false-positive classes the draft had — and 🔴 **two of those five were found by pointing the gate at `p392`'s own draft, where it failed**: a quoted absence spanning a colon stopped looking quoted, and a **struck-through retraction** was being read as a fresh claim, which would have punished the correction. Measured: **1,116** evidence-complete harvest rows over **17** capabilities, **356** absence sentences, **46** `REFUTED-CANDIDATE` (36 in historical gap-log sections, 8 in this pass's own closure table, **2** on the live shelves). The first run — before those bugs were fixed — returned **8 live candidates of which 7 were true**, and those seven are findings 1, 3 and 4 above. The 2 that remain are **known-false, registered as `Gap 392-A` and `Gap 392-G`, and written into an [adjudication ledger](../compose/code/p392-capability-absence/adjudicated.2026-10-22-p392.tsv) with a reason** — because a gate that fails on an adjudicated candidate gets switched off, and one that filters it silently hides the measurement. | Wired as `gate-capability-absence` in `make hooks`, which now runs **46** gates (44 green; the two red are `Gap 391-F`'s, red at `HEAD` before this pass wrote anything). |
| 3 | 🟢 **`Gap 391-C` is refuted: there are two granted proctoring components, and the clean one has a privacy posture worth selling.** [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) — 🟢 **MIT** (1,069 B, manifest agrees), HEAD **2026-09-28**, npm v0.5.1 — tab-switch, camera, **face** (face-api on TF.js, in-browser), audio, and **virtual-camera / loopback / screen-share** detection, with *"no hidden network calls… nothing leaves the page unless you set `backend.endpoint`"*, audio discarded, clipboard never read, screenshots off by default. [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) is the bigger codebase (398 commits, HEAD **2026-10-13**, **3 ★**) and the weaker record: 🔴 **grant CONFLICT — Apache-2.0 in the 11,356 B payload, `ISC` in `package.json` *and* on npm** — and its README marks the AI half (object detection, multi-face, eye tracking) *"(To be Done)"*, so what ships is **lockdown and telemetry**. 🔵 [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) is the **same HEAD sha `d1193a6`** — one project, two addresses, counted once. | 🔴 **The liability half of the old sentence survives and is the part to say out loud:** either component makes the client a **deployer** of an Annex III high-risk system. Rows on [`repos/foundations.md`](../repos/foundations.md); the old absence withdrawn on [`verticals/solutions.md`](../verticals/solutions.md); new `Pattern Y`. |
| 4 | 🟢 **`Gap 391-B` is closed for LATAM — 24 hours after it was opened — by a row this base has carried since before `p391`.** [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (🟡 **MIT, code only**, 1,072 B; PyPI `mcp-brasil` **v0.14.0**, 18 releases) serves **INEP `censo_escolar`** — Brazil's national school census — and **INEP `enem`** microdata among **70 public sources / 533 tools, 66 of them keyless**, cached locally and queried through DuckDB. That is the Brazilian analogue of the US district-targeting instrument `p391` said had none. 🟢 Its **LGPD** handling is documented in `SOURCES.md` (education graded *RISCO ALTO*; the 2022 withdrawal and 2024 anonymised resumption recorded; a code safeguard that whitelists aggregate columns and excludes `NU_INSCRICAO`, name and CPF). 🔴 Data is a **2023 snapshot**; HEAD is **2026-08-18 — 65 days**, which **disagrees with this base's own harvest row** (*"pushed 2026-10-20"*) because `pushed_at` and a HEAD commit date are different signals. 🔴 Still open for **EMEA, APAC and Mexico**. | [`intel/market.md`](../intel/market.md) LATAM, [`repos/foundations.md`](../repos/foundations.md), new `Pattern Z`. 🔵 Also `Gap 549` in the flesh: **one repository, a code grant and 70 data grants.** |
| 5 | 🟢 **The popularity channel is OPEN, and `p391`'s *"no row here carries a star count"* was a curl-only reading.** `github.com/{owner}/{repo}` answers **200 via WebFetch** and **403 via curl** — the same URL, two tools — which is `Gap 532`'s asymmetry replicated a seventh time. 🔴 And `api.github.com` is **not 403** either, as four passes recorded: it answers **200** with an authenticated **15,000/h** allowance and refuses **by scope**, naming `add_repo` as the remedy, while `/search` is closed by design. 🔵 So the limitation this shelf has carried since `p374` was a statement about one tool. | Stars restored on the rows below. **Measure a channel per tool, and record the tool** — `channel-state` now does. |
| 6 | 🔴 **And the first thing the stars do is overturn this shelf's own superlative.** The OpenMAIC row calls it *"the largest education-native repository in the open-source supply (~41.3k ★)"*. Read today through the one open channel: **OpenMAIC 41.3k ★** (confirming `p389`'s figure) and **[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) 42.2k ★** — **DeepTutor is larger**, and it was already on this shelf, two rows down, with no star count against it. | Superlative **retired** on both rows below. 🔵 The lesson is `p381`'s `openDesk` lesson again: **a superlative needs the comparison that would refute it**, and a shelf with one measured row and twelve unmeasured ones cannot carry one. |
| 7 | 🔵 **The discovery channels, measured rather than asserted — and one of them is new.** `packagist.org/search.json` is **open, keyless, and the only popularity channel here that is not GitHub** (it returns `downloads` and `favers`): 2 education/LTI queries, **7 results, 0 shelvable** — recorded so the next pass does not re-run it expecting a yield. `pypi.org/search` is a **JavaScript bot-challenge page**, so despite finding 1 there is **no Python discovery channel** in this sandbox. 🟢 `raw.githubusercontent.com` answers **200**, which reads a README or a manifest **without a clone**. | [`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv). The three new rows this pass shelved came from **npm** and from **this base's own harvest log**, not from a new forge. |
| 8 | 🔵 **The prescribed regional legs were replaced rather than re-run, as `Gap 387-D` asked — and the replacement yielded.** A **public-procurement-shaped** leg in Spanish and Portuguese returned four live LATAM education-AI tenders (Santa Fe province, Argentina; OEI-Chile; UNOPS Argentina; the CIEDEPAR consortium, Paraná) — **none of which specifies open source**, which is itself the finding. 🔴 The four stars-sorted, English-language legs returned, for a third consecutive pass, material this base already holds more precisely. | [`intel/market.md`](../intel/market.md) → LATAM; [`intel/trends.md`](../intel/trends.md) gains the procurement trend. 🔵 `Gap 548`'s point, now with a counter-example: a leg sorted by a dimension the live supply cannot compete on returns nothing, and a leg shaped like a **buyer** returns buyers. |

🔵 **`p391`'s table is preserved verbatim** at
[`archive/2026-10-22-p392-pre-rewrite/agents-top-p391-findings.md`](../archive/2026-10-22-p392-pre-rewrite/agents-top-p391-findings.md),
including the five findings of it this pass does not touch.

## How these rows were verified

🟢 🆕 `p392` **The popularity channel is readable again, and the sentence this paragraph carried for
eleven passes was true of one tool only.** `github.com/{owner}/{repo}` answers **200 via WebFetch**
and **403 via curl**; `api.github.com` answers **200** with an authenticated 15,000/h allowance and
refuses **by scope** (attached repositories only, `add_repo` named as the remedy) rather than
outright, while `/search` is closed by design. Star counts below are therefore marked
**`★ · github.com HTML · WebFetch · 2026-10-22`**, and rows read before this pass still carry none —
an unmeasured row is left unmeasured rather than back-filled from a roundup. Ranking is by what a studio can act
on: licence permissiveness, maintenance date and fit. Dating and licence reads come from `git` read
access, which **is** open to every public repository:

```bash
# ~1.2 s per repository, no credentials, no API
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the REAL default ref — not always main/master
git -C r log -1 --format='%H %cI'     # HEAD sha + last commit date  ← the maintenance signal
git -C r ls-tree --name-only HEAD     # root tree: is there a LICENSE at all?
git -C r show HEAD:LICENSE            # the GRANT, from the payload at that ref
git -C r show HEAD:package.json       # the manifest, which must agree with it
```

Two limits of that method, stated because they shape the rows: a **last-commit date under-reports
tag-shipping projects** (finding 9), and a **failed clone cannot distinguish private from deleted**
(the non-finding above).


## Tier 1 — Tutoring and instruction agents

| agent | repo | default ref | licence | what it actually does | origin |
|---|---|---|---|---|---|
| **OpenMAIC** 🆕 `p389` | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | `main` | 🔴 🆕 `p418` **MIT AT THE ROOT, AND THE REPOSITORY IS NOT MIT-ONLY.** Root grant re-read first-hand: **`1 065` B** *(not the `1,066` this row carried)*, `sha256₁₂ ba2525637432`, *"Copyright (c) 2026 THU-MAIC"*, root `package.json` `"license": "MIT"` — and the **same payload byte-identically in seven `packages/@openmaic/*` subtrees**. 🔴 **The ninth grant, `packages/mathml2omml/LICENSE`, is `LGPL-3.0` (`7 652` B, `sha256₁₂ e3a994d82e64`, FSF 2007)**, its manifest declaring `"license": "LGPL-3.0-or-later"` — vendored third-party code (`mathml2omml` `0.5.0`, Johannes Wilm, upstream `fiduswriter/mathml2omml`), a **direct root dependency** (`"mathml2omml": "workspace:*"`), built **first** by `build:packages`, **35** paths. 🔴 **It sits under the PPTX/Office-math export path this row recommends the project for.** 🔵 `packages/pptxgenjs` is the second vendored third-party and is MIT. 🟢 Build on it, but price the export path as **LGPL-3.0-or-later** | **The whole classroom, generated.** 🔴 🆕 `p392` *(This row said "and the largest education-native repository in the open-source supply (~41.3k ★)". **Retired.** Read today through the one open channel: OpenMAIC **41.3k ★** — `p389`'s figure confirmed — against [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) at **42.2k ★**, which was already two rows below with no star count against it. The superlative was published because the comparison was unmeasured, not because it had been made.)* A topic or an uploaded document becomes a multi-agent lesson: an AI teacher with a voice, teaching assistants, simulated classmates, narrated slides, auto-graded quizzes, HTML interactives and a shared whiteboard, with **agentic mid-lesson chat about any slide element**. Grew out of **MAIC**, deployed inside Tsinghua and validated on **700+ real students**; paper in **JCST 2026**. 🟢 Three properties that decide a school deployment and that almost nothing else on this shelf has: **server-first** generation (v1.2.0) that survives closed tabs and restarts on PostgreSQL; **central model governance** — every AI use is a named *slot* in `openmaic.yml`, each slot pinned to a provider, with an option to **forbid user-supplied keys** outright and `video: null` to switch a capability off; and **export of a finished classroom as one offline HTML file** (or a PPTX that keeps every scene). 🟢 Local-model path is real: **Lemonade** for local inference, **FunASR** for local ASR. 🟢 **24 built-in skills** plus per-owner authored skills; the course agent works through validated tools (patch one scene atomically, reorder pages, import `.pptx` with layout) rather than rewriting opaque blobs. 🟢 Security is handled like a product, not an afterthought — five releases since September carry SSRF, DNS-rebinding and provider-redirect fixes under published GHSAs. 🔴 Current head is **v1.3.0-rc.1** (knowledge base, 2026-10-22) with **breaking upgrade conditions and no rollback below it**; pin **v1.2.1** (2026-10-18) for a pilot. 🔴 Needs Node ≥ 22.19, pnpm ≥ 10, PostgreSQL 16 and a long-running server — Vercel deployments are capped at the 1.1.x line. 🔵 🆕 `p392` **Measured: `41.3k ★` · 6.4k forks · 750 commits** *(github.com HTML · WebFetch · 2026-10-22)*. | APAC — Tsinghua University, China (EN + zh-CN) |
| **OATutor** 🆕 `p389` | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | `main` | 🟢 **MIT** | **The adaptive tutor with the mastery model in the open, and the one with an academic maintainer behind it** — UC Berkeley's CAHLR. Intelligent-tutoring scaffolds over an open problem bank, with **Bayesian Knowledge Tracing** driving what comes next, so "adaptive" is a parameterised model a client can inspect and re-estimate rather than a prompt. Pairs with [`pyBKT`](https://github.com/CAHLR/pyBKT) (MIT) on [`repos/foundations.md`](../repos/foundations.md), which fits the model from the client's own interaction logs. 🟢 Dated **2026-10-21** — this is a live project, not a paper artefact. 🟡 Content-first: the win is the scaffold-and-mastery machinery, not an LLM. | North America — UC Berkeley CAHLR |
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main` | 🟢 **Apache-2.0** | Lifelong personalised tutoring: persistent learner memory plus RAG grounded in the learner's own uploaded materials. The most substantial permissive tutor in the open-source supply. 🟢 🆕 `p392` **And the largest education-native repository on these shelves, measured: `42.2k ★` · 5.3k forks · 2,935 commits · release `v1.6.15`, 2026-10-19** *(github.com HTML · WebFetch · 2026-10-22)* — ahead of OpenMAIC's 41.3k, which this shelf had called the largest. Apache-2.0 **and** bigger **and** actively released is an unusually easy recommendation; the reason to still reach for OpenMAIC is the governance surface (named model slots, forbid-user-keys, offline HTML export), not the size. | APAC — HKU Data Intelligence Lab, Hong Kong |
| **ai-shifu** | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | `main` | 🟢 **Apache-2.0** *(grant at `LICENSE.txt`, not `LICENSE`)* | AI-led chat-based course delivery — the agent drives the lesson script rather than waiting to be asked. | APAC — China |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | `main` | 🟢 **MIT** | Content generation for instructors: quizzes, lesson plans, question banks, YouTube-to-course. Teacher-facing, which is where the fastest-growing region's market actually is. | APAC — India |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main` | 🟢 **MIT** | AI-native LMS with an AI Mentor and role-play scenarios built in rather than bolted on. | EMEA — Selleo, Poland |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main` | 🟢 **BSD-3-Clause** | Self-hostable tutoring platform with local RAG over textbooks and notes — the data-residency option. | not verified this pass |
| **tutor-gpt** | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main` | 🟡 **GPL-3.0** | Theory-of-Mind tutoring: models the learner's mental state to pitch the explanation, rather than retrieving a better paragraph. Pedagogically the most interesting approach here. 🔴 🆕 `p389` **Dated: last commit `2025-11-13` — 343 days.** Keep it on the shelf as the clearest *statement* of learner-state modelling, but it is no longer a maintained dependency, and GPL-3.0 was always the harder sell. | North America |
| **ChatTutor** | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | `main` | 🔴 **AGPL-3.0** | Visual, interactive tutor. Network copyleft — hosting it as a service triggers source obligations. | APAC |
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **`dev`** | 🔴 **AGPL-3.0** | AI-native course platform. Note the default ref is `dev`: a `main`-assuming clone or licence read fails silently. | EMEA |
| **Learn Shell** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | `main` | 🔴 **AGPL-3.0** at `main` — 🟢 **MIT at tag `v0.1.0`** | 🆕 `p385`. **Agent-native teaching OS: the classroom is the server and the agent is bring-your-own.** Courses, lessons, FSRS-scheduled flashcards, graded exercises, mindmap, document reader, and a memory layer the agent reads back (`get_context` / `get_learner_brief`) instead of re-deriving the learner each session. ~50 tools over MCP, self-describing via a `manifest://capabilities` resource. 🔴 v1 is explicitly **single-machine and unauthenticated** — not multi-tenant as it stands. | APAC — China (MCP tool descriptions and prep-report are Chinese-first; docs English-first) |
| **OpenTutor** | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main` | 🟢 **MIT** *(1,068 B, © 2026 Zijin Zhang)* | 🆕 `p386`. **Block-based adaptive workspace that runs entirely on the client's own machine.** Course material in (PDF), structured notes, flashcards, quizzes and an adapting tutor out; **FSRS** spaced repetition, a knowledge graph and cognitive-load detection are in the product rather than on the roadmap. Next.js 16 + Python 3.11, Docker, **runs on local open-weight models with no API key and no data leaving the host**. 🟢 The data-residency tutor with a *permissive* grant — which [Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3) was the only other candidate for. 🟡 One maintainer; bilingual EN / zh-CN. | APAC — China |
| **Aha Tutor** (开窍) | [BaronCyrus/dsh-aha-tutor](https://github.com/BaronCyrus/dsh-aha-tutor) | `main` | 🟢 **MIT** *(1,067 B)* | 🆕 `p388`. **The most complete statement of adaptive-tutoring design on these shelves.** Builds a course from one sentence or an uploaded textbook, establishing the learner's baseline, goal, time budget and desired course size *before* writing a unit → chapter → lesson blueprint. Delivery is a **narrated handwriting blackboard** (formula-driven curves computed point-by-point, draggable parameters). 🟢 Mid-lesson checks **record confidence**, so a lucky guess, a hesitant answer and a confident wrong answer are three different events; weak points earn an automatic consolidation lesson. 🟢 A **"this step is wrong?"** button re-checks, corrects the blackboard, and **re-grades past attempts and the mastery estimate**. FSRS review, printable cheat sheets, video/PDF export. Built as a **DeepSeek Harness** extension; npm `dsh-aha-tutor` v1.7.0, published **2026-10-22**. 🟡 Single maintainer. | APAC — China (Chinese-first) |
| **Diagnostic Tutor** 🆕 `p391` | [SenmuuuuW/dsh-diagnostic-tutor](https://github.com/SenmuuuuW/dsh-diagnostic-tutor) | `main` | 🟢 **MIT** *(1,089 B)* | **The cleanest separation of pedagogy from runtime on these shelves — the teaching logic is in a different repository.** Diagnosis-first: the learner states a goal in their own words, a diagnosis map grows one node at a time, the tutor writes a lesson, a check is answered in the chat, evidence is recorded, and the tutor chooses the next step. 🟢 **The architectural claim is the row's value.** The runtime here holds *no teaching logic* — no "if blocked, explain the prerequisite" rule anywhere in it; those live in [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) (🟢 **MIT**, v2.1, → 2026-09-24). The runtime stores what the tutor decided, shows it, and never decides it. For a studio that means **the client's pedagogy is a separable, reviewable, swappable artefact** — and an auditor can read the teaching policy without reading the application, which is the cheapest Art. 50 / high-risk documentation posture on this shelf. 🟢 Docked learning surface: map, lesson and chat on screen at once, so answering a check never leaves the lesson. npm `dsh-diagnostic-tutor` **v0.1.1**, → 2026-10-17; HEAD **2026-10-21**. 🔴 **Early, and it says so rather than leaving it to be discovered:** no PDF or document ingestion, no RAG, no flashcards, no analytics, and a route **never marks knowledge as mastered**. 🔴 Requires DeepSeek Harness — it is a harness extension, not a standalone app. | APAC — China (EN + zh-CN interface switch on `main`, unpublished) |

## Tier 2 — Research and literature agents (higher education)

| agent | repo | default ref | licence | what it actually does |
|---|---|---|---|---|
| **paper-qa** | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main` | 🟢 **Apache-2.0** | Citation-grounded Q&A over a paper corpus that **declines to answer** without retrieved evidence. The refusal behaviour is the compliance story under EU AI Act Art. 50. |
| **OpenScholar** | [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main` | 🟢 **Apache-2.0** | Retrieval-augmented synthesis across scientific literature. |
| **ai2-scholarqa-lib** | [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main` | 🟢 **Apache-2.0** | The library behind AI2's Scholar QA — a production reference, not a demo. |
| **gpt-researcher** | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main` | 🟢 **Apache-2.0** | Autonomous multi-source research agent; the generic backbone for a guided-inquiry assignment. |

## Tier 3 — Assessment and classroom-infrastructure agents

| agent | repo | default ref | licence | what it actually does |
|---|---|---|---|---|
| **jupyter-ai** | [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main` | 🟢 **BSD-3-Clause** | LLM assistance inside JupyterLab — the surface where most CS and data-science teaching already happens. |
| **pybryt** | [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Assesses the **approach** a student's code takes, not only its output. Pairs with an LLM that explains *why* the approach was wrong. 🔴 🆕 `p387` **No PyPI release since `v0.7.0`, 2022-04-28 — four and a half years.** The idea is still the best available statement of approach-assessment and `Pattern B` still stands on it, but treat it as **a reference implementation to vendor and maintain, not a dependency to install**. Repository commit activity is unreadable here (`github.com` 403), so this is a statement about the *published artefact*, which is what a client would install. |
| **canvas-mcp** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | MCP server over Canvas LMS: courses, assignments, submissions, grading, rubrics, students. Fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT) adds office-hours, syllabus read/write and course-content copy. |
| 🆕 `p393` **autograder-py** | [edulinq/autograder-py](https://github.com/edulinq/autograder-py) | `main` | 🟢 **MIT** *(1,071 B, `7eb48830c022`)* | Python client for the **edulinq autograding server** — the submission/feedback half rather than the grading half, so it **pairs with** rather than competes against `otter-grader`. **49 releases**, 494 commits, HEAD `7984bd2` **2026-10-02 — 20 d**, **16 ★**. 🔵 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) is **not** a `p393` discovery — this base has carried it on [`repos/foundations.md`](../repos/foundations.md) Tier 3 and in `Pattern E` for several passes. What `p393` adds to it is its **first measurement**: 🟢 **161 ★**, **197 releases**, 3,825 commits, HEAD `190c1a4` **2026-10-01 — 21 d**, which makes it the most-adopted *maintained* autograder on these shelves (🔴 `okpy/ok`, Apache-2.0, **370 ★**, leads on adoption but is **532 d** stale — `Gap 397-A`). |
| **Flat** | [netless-io/flat](https://github.com/netless-io/flat) | `main` | 🟢 **MIT** | Open-source online classroom (interactive whiteboard, recording) — the live-session substrate an agent can sit in. |
| **jupyter-ai-tutor** | [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` | 🟢 **BSD-3-Clause** *(1,532 B)* | 🆕 `p388`. **The maintained notebook-tutor layer, and the replacement for `Pattern B`'s stale dependency.** Per-cell **Explain Code** button sends the cell source, kernel language, **the error traceback**, and the preceding cells up to the last markdown cell *as the exercise statement*. 🟢 Two pedagogically serious details: the tutor persona lives in a **`TUTOR.md` discovered by walking up from the notebook's directory**, so each course or folder carries its own in version control; and an optional **`reference_solution` + `evaluation_criteria` in cell metadata, ROT13-encoded** to keep it out of the student's view. From **QuantStack**, a known Jupyter-ecosystem maintainer. Requires `jupyter-ai-jupyternaut` (<0.1). v0.3.2, 7 releases, → 2026-09-25. |
| **BC Curriculum MCP** | [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p388`. **The North American curriculum-grounding instance** — the third region to get one, after Brazil's BNCC agent (`p387`) and `os-taxonomy` (`p384`). 12 MCP tools over the **entire BC Ministry of Education K–12 curriculum**, crawled into SQLite: Big Ideas / Curricular Competencies / Content in the real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search — and the **First Peoples Principles of Learning**, a jurisdictional requirement no generic tutor carries. Hosted HTTP endpoint or local stdio via `npx`. 🟡 2 releases, both **2026-03-27**; the data is a crawl, so currency is the risk, not the licence. |
| **tudelft-mcp** | [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p388`. **The EMEA institution-specific pattern, and the best-governed write path read so far.** One server over **four** systems a real university runs — Brightspace, **OSIRIS** (official records), MyTimetable and the public Study Guide — behind a single browser sign-in **including MFA**, with a self-renewing session. 🟢 **Every write (submitting an assignment, joining a group, replying in a discussion, registering for a course or exam) shows a preview and requires confirmation** — the human-in-the-loop control EU high-risk obligations ask for, shipped as the default. v0.1.4, → 2026-10-07. |
| **Canvas Toolchain** | [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` | 🟢 **MIT** *(1,063 B)* | 🆕 `p388`. **Teacher-facing semester refresh** — `Trend 5`'s shape exactly. Reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, and emits Canvas-safe HTML. 🟢 The **no-token "generate the HTML and paste it in"** path is first-class, so it delivers value without an API token or admin approval — which is how a pilot actually starts. 🟡 Installer is not code-signed; `npx canvas-toolchain` avoids it. → 2026-08-29. |
| 🆕 `p408` **CurriculumCraft AI** | [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) | `main` | 🟢 **MIT** *(1,091 B, "Copyright (c) 2026 Naitik")* | **Curriculum-bound item generation for a named jurisdiction — CBSE / NCERT, Grades 9–12.** 🟢 The row's value is the constraint, not the generator: it is built to compose questions **without reproducing verbatim NCERT text**, which is the copyright exposure a client's counsel asks about first and which almost no tutor on these shelves addresses at all. Real application tree (`server.ts`, `api/`, `src/`, Bun + Vite + Vercel), and it targets **open-weight Gemma**, so inference can be served in-country — the APAC data-residency posture without a sovereign-cloud contract. HEAD `1286a97` **2026-10-03 — 20 d**. 🔴 **Public beta by its own README**, which asks for subject-matter review before classroom use: wire it behind human review and never as the graded instrument. 🟡 Single maintainer. Origin: **APAC — India**. |

## Tier 4 — 🆕 `p387` LATAM-native agents (the tier `Gap 386-C` said did not exist)

Every row re-read first-hand on 2026-10-22 at the repository's **real default ref**, resolved with
`git ls-remote --symref`. These are **not** English-language agents with Spanish strings bolted on:
each is built by a LATAM institution or developer against a LATAM curriculum, platform or
constraint, and the prose in the repository is Spanish or Portuguese first.

| agent | repo | ref | licence | what it actually does | origin |
|---|---|---|---|---|---|
| **TutorIA** | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main` | 🟢 **MIT** *(1,069 B, © 2026 Grupo Sirius)* | 🟢 **The one LATAM-native agent built as an LMS plugin rather than a standalone app.** Conversational tutor delivered **inside Open edX as an XBlock/plugin**, FastAPI backend, Claude API, TTS audio replies, animated avatar, **teacher statistics panel**, context persistence across sessions. Shipped for **rural higher education in Risaralda, Colombia**; first subjects Programación I (Python) and Introducción a la Matemática. Docker + Azure, GitHub Actions. 🟡 Read the licence boundary below before quoting it. | LATAM — Universidad Tecnológica de Pereira, Colombia |
| **Agente BNCC para professores** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main` | 🟢 **MIT** *(1,074 B; `package.json` also declares MIT)* | 🟢 **Curriculum-grounded generation with the hallucination gate in the product, not the roadmap.** Lesson plans and exams-with-answer-keys anchored to official **BNCC** skill codes (Brazil's national curriculum): the model writes the prose, but every code and skill description comes from the official base and **an invented code is discarded before it reaches the teacher**. 1st year of Fundamental → 3rd year of Ensino Médio, cross-term skill selection, student/teacher PDF pairs, keyed **API v1** so a school's own systems call the same agent, Gemini or DeepSeek per request. Next.js 16 + TypeScript. | LATAM — Brazil |
| **TechLead AI Tutor** | [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main` | 🟢 **MIT** *(1,069 B, © 2026 Thiago Silva)* | Programming and software-engineering tutor built to **refuse to hand over the code**: spec-driven planning before any line is written, and **the agent that teaches is not the agent that verifies** — mechanical sensors grade the build. The clearest open statement of anti-dependency tutoring design on these shelves. | LATAM — Universidade Federal do Agreste de Pernambuco (UFAPE), Brazil |
| **Manu** 🆕 `p390` | [Jeanikt/tutor-ai-agent](https://github.com/Jeanikt/tutor-ai-agent) | `main` | 🟢 **MIT** | 🟢 **The first voice-first row on these shelves, and it is LATAM-native.** A spoken maths tutor in **Brazilian Portuguese** that re-pitches the same concept from 1st grade to university, built on **[LiveKit Agents](https://github.com/livekit/agents)** (Apache-2.0) in TypeScript — so the realtime STT → LLM → TTS pipeline, turn detection and interruption handling are an upstream dependency rather than this project's own code. 🟢 Voice matters more here than in English-first markets: it reaches learners with low typing fluency and the shared-device households that `Trend 10` describes, and it sidesteps the written-Portuguese barrier for early grades. 🔴 **Early — the README states "in development" with no public deployment**, and the maths-correctness layer is the LLM itself, with no symbolic checker. Dated **2026-10-07 (15 days)**. Take it as a **working reference for the voice pipeline**, not a deployable tutor; see 🆕 `Pattern V`. | LATAM — Brazil (pt-BR) |

🟡 **The licence boundary on TutorIA, stated because a studio will hit it on day one.** The plugin's
own grant is MIT and a studio can keep its changes closed. **Open edX itself is AGPL-3.0**, and
TutorIA is delivered as an XBlock inside it — so the *platform* obligations are untouched by the
plugin's MIT grant. Deliver it the way `Pattern A` and `Pattern O` deliver every agent into a
copyleft LMS: **the agent is a separate service the plugin calls**, and the plugin stays thin.

🔴 **Ungranted, and recorded so nobody re-finds them as candidates** (no licence file at any of the
eight probed paths, no `license` field in any manifest):
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru —
offline-first PWA, 1.°–5.° de secundaria, explainable decision-tree difficulty selection; **this is
the one that hurts**, because `Pattern D` wants exactly this and cannot use it),
[FXArth/Tutor-Programacao](https://github.com/FXArth/Tutor-Programacao) (Brazil),
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref **`master`**).

## Tier 5 — 🆕 `p388` Parent and guardian agents (the persona no shelf here had)

These shelves have carried the learner, the teacher and the institution since they were built. **The
parent was absent** — the word "observer" appeared in exactly one file before this pass. The registry
discovery channel surfaced three granted servers for that persona, two by one maintainer working the
problem deliberately across two different platforms.

🔵 **Why it is a market fact, not a curiosity.** Every North American instrument this base tracks puts
**family transparency** in the statute — Oklahoma SB 1734 names it outright, and Maryland's act is
built around guidance districts must hand down. A parent-facing read surface is the one place where
"transparency" becomes a *product* instead of a policy document. It is also the only education
persona with **no incumbent vendor lock**, because the parent portal is a feature of the SIS rather
than a market of its own.

| agent | repo | ref | licence | what it actually does | platform |
|---|---|---|---|---|---|
| **infinitecampus-mcp** | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | 🟢 **The first SIS-side parent portal on these shelves.** 20 tools over **Campus Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent-grades window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via **CUPS SSO**, and it is `FeatureDisabled`-aware, so it degrades per district instead of erroring. **47 npm releases**, → 2026-10-19. | Infinite Campus |
| **canvas-parent-mcp** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | The same scope against Canvas: 18 `canvas_*` tools held deliberately to **the read-only parent-observer surface** (`canvas_list_observees` is the hinge), plus student self-access. Four auth modes tried in priority order. 🟢 The download tool is properly hardened — host-pinned to your Canvas origin, writes only inside a download directory, never through a symlink, new files `0600`. **43 npm releases**, → 2026-10-16. | Canvas |
| **mtgibbs/canvas-lms-mcp** | [mtgibbs/canvas-lms-mcp](https://github.com/mtgibbs/canvas-lms-mcp) | `main` | 🟢 **MIT** *(1,064 B)* | Canvas read access framed first at *"parents monitoring their child's academic progress"*: due-this-week, missing work across all classes, grade questions in natural language. 🟡 **Last published 2026-02-13** — eight months. Shelved for the framing; take the row above as the dependency. | Canvas |

🔴 **The compliance edge, stated before anyone builds on these.** All three are **personal-credential**
tools — a parent's own token, OAuth, or a scraped session. That is fine for a parent acting for their
own child. **The moment a studio hosts one on behalf of a district, the credential becomes
institutional and the read becomes a FERPA-governed disclosure of an education record.** The persona
is new; the obligation is not. `Pattern P` is built around that boundary.

## Tier 6 — 🆕 `p394` The R teaching, autograding and psychometrics stack

🔵 **Why this tier did not exist until now.** `p393` ranked a CRAN channel second and gave the reason:
`otter-grader`, the most-adopted *maintained* autograder on these shelves (🔴 `okpy/ok` at **370 ★**
leads on adoption and is **532 d** stale — `Gap 397-A`), **grades R**, and the statistics-teaching
stack is R-shaped — so one whole teaching discipline sat in a blind spot. The channel it asked for is
**closed on both tools** (CRAN `curl` 000 / `WebFetch` ENOTFOUND; r-universe refused), but the supply
is reachable by clone, and `github.com/cran/<pkg>` mirrors every CRAN `DESCRIPTION`. Every row below
was read from a cloned tree on 2026-10-22.

🔴 **Read the licence column carefully: this tier splits cleanly, and the split is commercial.** The
three **delivery** components are permissive and the four **measurement** components are GPL.

| repo | ref · HEAD | licence | ★ | what it is |
|---|---|---|---|---|
| [rstudio/gradethis](https://github.com/rstudio/gradethis) | `main` · **126 d** | 🟢 **MIT** *(1,078 B, `sha256`₁₆ `48c18e68ffed`; `DESCRIPTION`: `MIT + file LICENSE`)* | **164** | 🆕 `p394`. **Automated feedback for student exercises**, from **Posit Software, PBC**. Two grading modes: compare against a model solution (`grade_this_code()`), or write the predicate yourself (`grade_this()`). 41 forks. 🟢 **The most-starred *maintained* autograder on these shelves and the most permissive** — it edges
`otter-grader` (161 ★). 🔴 **Not the most-starred outright:** `okpy/ok` holds **370 ★** at 532 d (`Gap 397-A`). 🔴 **Not on CRAN** (`cran/gradethis` ABSENT), so a CRAN index would have missed it. |
| [rstudio/learnr](https://github.com/rstudio/learnr) | `main` · **343 d** | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`; `DESCRIPTION`: `Apache License (>= 2.0)`)* | **738** | 🆕 `p394`. **Interactive tutorials in R Markdown** — the runtime `gradethis` grades inside. 241 forks. 🟡 HEAD is 343 days: this is a **stable substrate**, not an abandoned one; the movement is in `gradethis`. |
| [ucbds-infra/ottr](https://github.com/ucbds-infra/ottr) | `master` · **108 d** | 🟢 **BSD-3-Clause** *(1,555 B, `1677c5307530`; `DESCRIPTION`: `BSD_3_clause + file LICENSE`)* | 3 | 🆕 `p394`. **The R autograding extension for `otter-grader`** — UC Berkeley Data Science Education Program. Grades R scripts, Rmd documents and Jupyter notebooks with R kernels. 🟢 So `otter-grader`'s R half is permissive. 🔴 **3 ★: the adoption is on the Python parent**, and this is the component you would actually deploy for an R course. |
| [philchalmers/mirt](https://github.com/philchalmers/mirt) | `main` · **1 DAY** | 🟡 **GPL (>= 3)** — 🔴 **grant lives only in `DESCRIPTION`; no licence file at any tree path** | **235** | 🆕 `p394`. **Multidimensional item response theory** — the canonical IRT engine, v1.48.2, 88 forks, committed **yesterday**. 🔵 This base has carried `adaptive-knowledge-graph` (IRT + BKT, ~350 ★) and `OATutor` (BKT) as its adaptive layer; `mirt` is the thing those are approximating. |
| [patriciamar/ShinyItemAnalysis](https://github.com/patriciamar/ShinyItemAnalysis) | `master` · **136 d** | 🟡 **GPL-3** — 🔴 **`DESCRIPTION` only** | 47 | 🆕 `p394`. **Test and item analysis via Shiny**, v1.6.0, 27 forks. The psychometric-review front end a ministry or exam board would hand to a non-programmer. |
| [`cran/exams`](https://github.com/cran/exams) | `master` · **14 d** | 🟡 **GPL-2 \| GPL-3** *(disjunctive — the licensee picks)* — 🔴 **`DESCRIPTION` only** | n/a *(mirror)* | 🆕 `p394`. **R/exams v2.4-5**, Achim Zeileis (R-project). 🟢 **The broadest assessment exporter on these shelves**: QTI 1.2, QTI 2.1, Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS, TestVision, Particify, ARSnova, Kahoot!, Grasple, TCExam — verified from the `R/` source filenames in the clone (`exams2qti12.R`, `exams2qti21.R`, `exams2moodle.R`, `exams2canvas.R`, `exams2blackboard.R`, `exams2ilias.R`, `exams2openolat.R`, …). 🟢 **Plus NOPS**: a standardised PDF that is printed, scanned and marked automatically. |
| [`cran/catR`](https://github.com/cran/catR) | `master` | 🟡 **GPL (>= 3)** — 🔴 **`DESCRIPTION` only** | n/a *(mirror)* | 🆕 `p394`. v3.17. Response-pattern generation under **computerized adaptive testing** — the CAT engine behind every "adaptive tutor" claim on this shelf. Sibling [`cran/TAM`](https://github.com/cran/TAM) (GPL >= 2, v4.3-25) carries the test-analysis modules. |

🟢 **The NOPS path deserves naming separately, because nothing else in this base does what it does.**
R/exams can emit a printed exam, take a **scan** of the completed paper, and mark it automatically. Every
other assessment component on these shelves assumes a browser, a session and a network. 🔵 **For the
LATAM and APAC engagements this base keeps describing as connectivity-constrained, an offline
assessment loop with an auditable paper trail is not a downgrade — it is the requirement**, and the
LATAM survey fact on [`intel/market.md`](../intel/market.md) sharpens it: **assessment is the
*lowest*-adoption AI use case among LATAM faculty**, which is precisely where this supply sits.

🔴 **Two licence boundaries a studio will hit in week one, stated now rather than discovered later.**
**(1)** The **delivery** layer is permissive (`gradethis` MIT, `learnr` Apache-2.0, `ottr` BSD-3) and the
**measurement** layer is GPL (`exams`, `mirt`, `ShinyItemAnalysis`, `catR`, `TAM`). So a closed-source
product can embed the tutoring and grading loop and must reach the psychometrics **over a process
boundary** — the same discipline `Pattern A` and `Pattern O` already apply to copyleft LMSs. **(2)**
`cran/exams` is **GPL-2 or GPL-3 at the licensee's choice**; a disjunctive grant is a decision the
studio must record once, not a footnote, because the downstream compatibility differs.

🔴 **And a provenance warning specific to this tier.** `mirt`, `ShinyItemAnalysis`, `cran/exams`,
`cran/catR` and `cran/TAM` all have **no licence file at any path**: GitHub's sidebar shows **no
licence** for them, and a reviewer who checks the sidebar will report five granted GPL packages as
unlicensed. The authoritative grant is the `License:` field in `DESCRIPTION`, which is what CRAN
itself enforces. 🔵 **That is `Gap 394-B`**, and it is the reason this tier is published with its
grant-location column visible.

🔴 **One name collision, recorded as a fixture rather than offered as a component.**
[`jhudsl/ottrpal`](https://github.com/jhudsl/ottrpal) (GPL-3, v2.0.0, HEAD **569 d**) is **not** related
to `ottr`: "OTTR" there is **Open-source Tools for Training Resources** (Johns Hopkins / Fred Hutch), a
course-publishing toolchain. 🔵 Two unrelated projects, one token, found in the same hour in a brand-new
channel — `Gap 393-A` reproducing itself on first contact.

## Courseware, not agents — but the fastest way to staff a team

| repo | default ref | licence | note |
|---|---|---|---|
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main` | 🟢 **MIT** | 12-lesson agent curriculum. Frequently mis-listed as an agent in roundups; it is a course. |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | `main` | 🟢 **Apache-2.0** | Hugging Face's agents course. |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | 🔴 **`development`** | 🟢 **MIT** | Open courseware delivery components. Default ref is `development`. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | `main` | 🟢 **MIT** *(1,070 B stock, © 2026)* | 🆕 `p384`. Model foundations → LLM systems → agents, with a retrieval-evaluation lab and local graders. A **staffing** asset for the studio, not a deliverable component. |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | `main` | 🟢 **MIT** *(1,070 B stock)* | 🆕 `p384`. Curated use-case index with an education section. 🟡 It is a **list** — roundups file it as an agent; it is not one. |

## 🔴 No licence file — and "ungranted" is three different things

Five repositories on these shelves have **no licence file at any of seven probed paths**. 🔵 **That
is where this pass's own first draft stopped, and it was wrong to.** This base's `gate-enumeration`
refused the draft, so the manifests and source headers were read too — and the five split into
three classes that call for three different decisions:

| repo | no licence file at 7 paths | but the manifest / headers say | verdict |
|---|---|---|---|
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | ✔ (`LICENSE` `LICENSE.md` `LICENSE.txt` `LICENCE` `COPYING` `LICENSE-MIT` `license`) | `pyproject.toml` present, **no `license` field** | 🔴 **UNGRANTED — do not ship** |
| [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | ✔ | no manifest found | 🔴 **UNGRANTED — do not ship** |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ✔ | `package.json` → **`"license": "MIT"`**, and its `files` array even **names a `LICENSE` that is not in the tree** | 🟡 **MANIFEST-ONLY MIT.** A published npm-style grant with the file missing. Reusable in practice, but ask the maintainer to commit the file — and record the manifest line you relied on |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | ✔ | `package.json` → **`"license": "MIT"`** | 🟡 **MANIFEST-ONLY MIT** |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | ✔ | **`version.php` carries the full GPL-3.0-or-later header** — *"either version 3 of the License, or (at your option) any later version"* | 🟢 **GPL-3.0-or-later, granted in the source headers.** Standard and required practice for a Moodle plugin; the missing root file is a packaging habit, not a missing grant |

🆕 `p386` — **three more ungranted addresses, and one of them matters more than the others.**

| repo | result | why it is recorded |
|---|---|---|
| [Nutlope/llamatutor](https://github.com/Nutlope/llamatutor) | 🔴 **UNGRANTED** — nothing at 9 paths, no manifest licence field | 🔴 **It circulates widely as "an open-source AI personal tutor"** and is still returned by the prescribed global search leg. It is not reusable as it stands. The most-cited tutor on the open web and the most-cited *granted* tutor are not the same repository. |
| [jarodise/Language-Transfer](https://github.com/jarodise/Language-Transfer) | 🔴 ~~UNGRANTED~~ → 🟡 **README-ONLY MIT** *(corrected `p394`)* | 🔴 **`p386`'s verdict is withdrawn.** `README.md:167` carries `## License` → `MIT`. No licence file at any of 42 tree paths, no manifest, no SPDX, and GitHub's sidebar shows nothing — but `p288` made a README grant claim a standing channel, and this row never consulted it. **31 ★**, 4 forks, HEAD 2026-02-28 (**236 d**), single commit, markdown-only. 🟢 `p386`'s *other* reading survives intact: it teaches **Spanish to non-speakers** inside an agent CLI, so it is still not the Spanish-language tutor for Spanish-speaking learners that the LATAM supply gap is about. |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | 🔴 ~~UNGRANTED~~ → 🟡 **README-ONLY MIT** *(corrected `p394`)* | 🔴 **Wrong twice, and the second error is worse.** `readme.md:84`: *"This project is open-source and available under the MIT License."* **And it is not a Blackboard Learn integration**: no `blackboard.com`, no Learn REST, no OAuth, dependencies `mcp` + `sqlite3`, and `blackboard://` is the **blackboard architectural pattern** — shared memory and a knowledge graph, credited in its own README to `dx-corp/shared-memory-mcp`. **0 ★**, HEAD 2026-10-16 (**6 d**), single commit, 9 files. 🔵 It therefore **leaves the Blackboard family**, which this shelf has counted at nine for eight passes. |

🔵 **The lesson is now `Pattern L` step 8** in [`compose/patterns.md`](../compose/patterns.md):
*a missing `LICENSE` file is a reason to read the manifest and the source headers, not a verdict.*
Three of these five would have been wrongly rejected by a file-only read — including the one
plugin Moodle's own directory distributes.

For Moodle, use the **`webservice_mcp` plugin from Moodle's own plugin directory** instead
(Moodle 4.5–5.2, latest release 23 Jul 2026) — see [`compose/patterns.md`](../compose/patterns.md).

### 🆕 `p388` — a fourth class: **the licence can be missing from the payload while the manifest claims it, and the repository can be closed while the artefact is readable**

The discovery sweep turned up a case that none of the three classes above describes, and it involves
the largest organisation to appear on these shelves: **Santillana**, one of the biggest education
publishers in Spain and Latin America. It is the first time a major regional publisher's own AI
tutoring code has surfaced here. **It does not survive procurement.**

| package | npm history | declared licence | licence file **in the published tarball** | repository |
|---|---|---|---|---|
| `@santillana-ai/create-tutor-app` | **v5.9.0, 63 versions**, 2025-08-28 → 2025-10-21 | 🟡 **`"license": "MIT"`** in `package.json` | 🔴 **NONE** — tarball read first-hand (38,447 B): `README.md` and templates only | 🔴 [santillana-ai/tutor-sdk](https://github.com/santillana-ai/tutor-sdk) — `git ls-remote` **prompts for credentials** |
| `@santillana-ai/typescript-tutor-sdk` | **v5.9.0, 115 versions**, 2025-08-27 → 2025-10-21 | 🔴 **`license` field absent entirely** | 🔴 **NONE** — tarball read first-hand (896,006 B): `README.md` only | 🔴 no `repository` field at all |

🔴 **Verdict: UNGRANTED — do not ship.** Note *which* package fails. The MIT claim sits on the
**scaffolder**, a one-command project generator. The package a client's codebase would actually
depend on — **`typescript-tutor-sdk`, 115 published versions** — declares **no licence at all**,
ships no licence text, and names no repository. Both are in any case **clients for a proprietary
keyed API**, so even a clean grant would buy an SDK, not a tutoring engine.

🔵 **Three method points that generalise past this case:**
1. **`git ls-remote` separates *private* from *absent*.** A credentials prompt is not a 404 — the
   repository exists and is closed. This base can now write "closed" instead of "dead".
2. **The tarball is the artefact, and npm serves it even when the repo is closed.** The licence that
   *ships* is a different question from the licence the repository *states*. Here the tarball settles
   it; `raw.githubusercontent.com` could not have.
3. 🔴 **A scoped npm org is not a corporate attestation.** `@santillana-ai` is consistent with
   Santillana and the sole maintainer is a plausible individual account, but **nothing read this pass
   ties the scope to the company** — recorded as `Gap 388-E`. The licence verdict does not depend on
   resolving it.

🔴 **And the same sweep found five more repositories in the published-but-unreadable state** — the
package ships, the source prompts for credentials. The one that costs the most:
**[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)**,
`@thanh01.pmt/interactive-quiz-kit` **v1.4.10 across 103 published versions** (2025-06-12 →
2026-09-23), manifest MIT, source closed — interactive quizzes with AI generation **and SCORM
support**, which is genuinely scarce in permissive open source. Also
[Mckaroff/GraphLMS](https://github.com/Mckaroff/GraphLMS) (`rhizome-lms-mcp`, manifest MIT),
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) — whose manifest reads
🔴 **`"SEE LICENSE IN LICENSE"`, pointing at a file in a repository nobody can read**, a perfectly
circular grant — [AI-Matrix-Engine/aidream](https://github.com/AI-Matrix-Engine/aidream) and
[yokowasis/autograder](https://github.com/yokowasis/autograder). Full table in
[`agents/trending.md`](trending.md).

🔵 **The procurement rule this yields, and it is `Pattern L`'s new step:** for an npm-only
dependency, **the manifest is a claim and the tarball is the evidence**. A grant that points into an
unreadable repository is not a grant — and it is the one case where re-reading the payload cannot
save it.

🟡 **Two more manifest-only grants found this pass** (`Pattern L` class 3, reusable with the caveat
recorded): [TecFancy/dsh-deeptutor](https://github.com/TecFancy/dsh-deeptutor) — no licence file at
10 probed paths, npm `dsh-deeptutor` declares **MIT**; a DeepSeek Harness learning extension — and
[nanobpm/nano-ide](https://github.com/nanobpm/nano-ide) — no licence file, `@nanobpm/agentic`
declares **Apache-2.0**.

## Build-on-this tier

The permissive shortlist: every agent on these shelves a studio can build on and still hand a
client closed, client-owned code. 🆕 `p387`: **23 permissive rows** (19 at `p386`, **+4: three LATAM-native agents and `d2l-cli`**) — MIT, Apache-2.0 or BSD-3 only, no
copyleft, no bespoke clause, every grant read first-hand at the repository's real default ref.

| repo | ref | licence | use it for |
|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main` | Apache-2.0 | tutoring with learner memory |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main` | MIT | 🆕 `p386` — local-first adaptive workspace; tutoring with **no data leaving the host** |
| [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | `main` | Apache-2.0 | agent-led course delivery |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `main` | MIT | teacher-facing content generation |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main` | MIT | AI-native LMS starting point |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main` | BSD-3-Clause | self-hosted tutoring, data residency |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main` | Apache-2.0 | citation-grounded answers that refuse without evidence |
| [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main` | Apache-2.0 | literature synthesis |
| [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main` | Apache-2.0 | production scholar-QA reference |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main` | Apache-2.0 | guided-inquiry research scaffold |
| [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main` | BSD-3-Clause | LLM help inside the teaching notebook |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | MIT | assess the approach, not the output |
| [netless-io/flat](https://github.com/netless-io/flat) | `main` | MIT | live online classroom substrate |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | MIT | governed campus LLM gateway |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | MIT | give the prompt pipeline a metric |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | Apache-2.0 | document-aware RAG over course material |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | MIT | the before/after measurement |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | MIT | retention scheduling with published parameters |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | `development` | MIT | courseware delivery components |
| [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main` | MIT | 🆕 `p387` — Spanish-language tutor **inside Open edX**; the LATAM reference deployment |
| [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main` | MIT | 🆕 `p387` — BNCC-anchored teacher generation with a curriculum-code gate |
| [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main` | MIT | 🆕 `p387` — tutoring that withholds the answer; author ≠ verifier |
| [Jeanikt/tutor-ai-agent](https://github.com/Jeanikt/tutor-ai-agent) | `main` | MIT | 🆕 `p390` — **voice-first pt-BR maths tutor**; the reference for a spoken tutor |
| [livekit/agents](https://github.com/livekit/agents) | `main` | Apache-2.0 | 🆕 `p390` — the **realtime voice substrate** (STT→LLM→TTS, turn detection) under any spoken tutor |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | `master` | MIT | 🆕 `p390` — **permissive courseware engine** (CMU OLI) with adaptive activities + analytics |
| [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli) | `main` | MIT | 🆕 `p387` — read-only Brightspace client written **for agents** (PyPI `d2l-cli` 0.3.0) |
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` | MIT | 🆕 `p388` — **187-tool teacher/admin Canvas surface with a FERPA mode**; 87 releases, published 2026-10-22 |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) | `main` | MIT | 🆕 `p388` — 209-tool **student-side** Canvas surface, opens no port |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` | MIT | 🆕 `p388` — **the parent/guardian persona, SIS-side**; 47 releases |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` | MIT | 🆕 `p388` — parent-observer scope over Canvas, hardened downloads |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` | BSD-3-Clause | 🆕 `p388` — notebook tutor with a version-controlled `TUTOR.md` persona; **replaces `pybryt` as the live dependency** |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | MIT | 🆕 `p388` — **North American** curriculum grounding (BC K–12, incl. First Peoples Principles of Learning) |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` | MIT | 🆕 `p388` — **EMEA**; four university systems, one MFA sign-in, **every write preview-confirmed** |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` | MIT | 🆕 `p388` — teacher-facing semester refresh with **topic-currency scoring**; works with no API token |
| [BaronCyrus/dsh-aha-tutor](https://github.com/BaronCyrus/dsh-aha-tutor) | `main` | MIT | 🆕 `p388` — adaptive tutoring that **records answer confidence** and re-grades on correction |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` | MIT | 🆕 `p388` — RAG over the **Moodle codebase**; cuts `Pattern A`'s build cost |

🔴 Deliberately **not** here, and why: `plastic-labs/tutor-gpt` (GPL-3.0) and
`HugeCatLab/ChatTutor`, `learnhouse/learnhouse` (AGPL-3.0) are run as **separate services**, never
linked. `microsoft/autogen`'s code grant is MIT but lives in `LICENSE-CODE`, so it needs the
per-file check below before it enters a deliverable.
🆕 `p385` **[sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is not here either, and it is the
interesting case:** `main` is **AGPL-3.0**, but the project was **MIT until it relicensed on 2026-08-16**, and that
MIT grant is still readable at tag **`v0.1.0`** (1,081 B, read first-hand this pass). A studio that needs permissive
*can* pin `v0.1.0` — but it inherits a frozen tree with **no upstream path**, because every commit since is AGPL.
🔵 Pinning a tag to dodge a relicence buys the licence and gives up the project. See **Pattern L step 10**.

## MCP servers by LMS platform

MCP reached the LMS in 2026 and this is the integration path that did not exist a year ago.
🆕 `p386`: **6 platforms** are reachable through the servers below — LMS platforms, counting Anki's
spaced-repetition loop separately because it is not an LMS. Blackboard joined the table at `p386`,
with a verified grant for the first time.

### Agents over the systems

🆕 `p387`: **25 distinct MCP server slugs appear in this section's table** — **23 platform rows**,
every one resolved and licence-read first-hand on 2026-10-22 (12 at `p383`–`p385`, 11 added at
`p386`), **plus two fork addresses named inside a row's note** (`lmgveerhoek/brightspace-mcp-server`
and `matthewliu10/brightspace-mcp-server`, both byte-identical to their upstream).
🔵 **The count and the scope are stated together on purpose.** `p278` registered this claim as
*"MCP server slugs in the MCP section's table"* but anchored it to a sentence about **rows**, so
the instrument measured 25 while the shelf said 23 and the gate read STALE with nothing actually
wrong. `p387` re-points the anchor at the quantity the instrument measures — slugs — and keeps the
row count in the same sentence, because a reader wants rows and the gate wants slugs.

| platform | server | ref | licence | note |
|---|---|---|---|---|
| **Moodle** | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | `main` | 🟡 **GPL-3.0-or-later, in the source headers** (no root licence file) | 🟢 **The first-party path.** The GitHub home of the `webservice_mcp` plugin listed in **Moodle's own plugin directory** (Moodle 4.5–5.2, latest release 23 Jul 2026, gated on `webservice/mcp:use`). No root `LICENSE`, but `version.php` carries the full GPL-3.0-or-later header, as Moodle requires of every plugin. Granted — and GPL is survivable here, because the agent reaches it over JSON-RPC rather than linking to it. |
| **Moodle** | [lmscloud-io/moodle-mcp-server](https://github.com/lmscloud-io/moodle-mcp-server) | `main` | 🟡 GPL-3.0 | Vendor-maintained. GPL is survivable here: the agent talks to it over JSON-RPC, it is not linked. |
| **Moodle** | [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | `main` | 🔴 **UNGRANTED** | Course, announcement and assignment tools. No licence file **and** no `license` field in `pyproject.toml`. Do not ship. |
| **Moodle** | 🆕 `p393` [Dathis/swiss-moodle-mcp](https://github.com/Dathis/swiss-moodle-mcp) | `main` | 🟢 **MIT** *(1,063 B, `84e5d85f30e9`)* | 🟢 **The EMEA/Switzerland row, found through the new PyPI index channel.** Courses, materials, downloads, deadlines, announcements over **ZHAW, FHNW, ETH, EPFL and any Moodle 4**. 🟢 **Privacy posture worth repeating to a client:** the user authenticates themselves, typically via **SWITCH edu-ID**, and the README states passwords are never seen or stored. HEAD `cdb11c0` **2026-09-29 — 23 d**, PyPI `swiss-moodle-mcp` v0.5.0. 🔴 **0 ★, 21 commits, and self-described as an unofficial student project not affiliated with any university — pilot it, do not put a university on it this quarter.** |
| **Moodle** | 🆕 `p393` [Snaw80/moodle-mcp](https://github.com/Snaw80/moodle-mcp) | `main` | 🟢 **MIT** *(1,072 B, `b2bb31ce9d90`)* | Exposes Moodle **Web Services** to an MCP client. HEAD `4fc83d0` **2026-06-13 — 131 d**, PyPI `mcp-moodle` v0.1.2, 13 commits, **4 ★**. 🔵 Smallest of the granted Moodle servers; useful mainly as a second opinion on tool shape against the two GPL vendor servers above. |
| **Moodle** | 🔴 `p393` `NmaaAlhawary/MCP-Moodle` *(unlinked: absent address)* | — | 🔴 **UNAUDITABLE — MIT declared on PyPI, source does not resolve** | PyPI `moodle-mcp-bridge` **v1.7.0** (2026-07-24) advertises *"a Moodle site as 88 typed AI tools"* and a docs site; the declared repository does not resolve unauthenticated, so **there is no payload to read**. `Gap 393-B`'s class. Listed so it is not re-found and mistaken for granted supply. |
| **Canvas** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | 🟢 **The clean default.** Courses, assignments, submissions, grading, rubrics, students. |
| **Canvas** | [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) | `main` | 🟢 **MIT** | Fork of the above: adds office-hour appointment groups, announcement editing, syllabus read/write, student groups, course-content copy. |
| **Canvas** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main` | 🟢 **MIT** | Independent implementation — useful as a second opinion on tool shape. |
| **Canvas** | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | 🟡 **MANIFEST-ONLY MIT** — 🆕 `p387` **also published to npm as MIT**, a second independent grant publication | 🔴 🆕 `p387`: npm `canvas-mcp-server` **v2.2.3, last published 2025-06-27 — ~16 months stale**, while [r-huijts](https://github.com/r-huijts/canvas-mcp) published 2026-09-21. Its tool count is the largest on the Canvas shelf and its release is the oldest; prefer the maintained one unless you need those tools. Advertises 54 tools and Streamable HTTP. No licence **file**, but `package.json` declares `"license": "MIT"` — and its `files` array names a `LICENSE` that is absent from the tree. Usable; get the file committed. |
| **Open edX** | [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | `master` | 🔴 AGPL-3.0 | Matches the platform's own licence, which is the reason it can exist. |
| **Open edX** | [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master` | 🔴 AGPL-3.0 | The `tutor` plugin that installs it — the realistic deployment route. |
| **Google Classroom** | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | `main` | 🟢 **MIT** | Classroom is not an LMS a studio can fork, so MCP is the *only* integration surface. |
| **Brightspace / D2L** | [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | `main` | 🟡 **MANIFEST-ONLY MIT** — 🆕 `p387` the npm record declares `MIT` too, so the grant is published twice | 🔴 🆕 `p387`: npm `d2l-mcp-server` **v1.0.1, published 2025-11-28 and never again — ~11 months stale.** The only D2L server verified this pass. No licence file; `package.json` declares `"license": "MIT"`. **D2L remains thin — one server, and its grant is a manifest line.** |
| **Blackboard** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | `main` | 🟢 **MIT** *(1,063 B)* | 🔴 🆕 `p387`: **it has never shipped a release.** Its `package.json` claims the npm name `blackboard-learn-mcp`, which is **404 on the registry**; the unrelated npm package `bb-mcp` (v1.0.0, 2026-06-19) carries **no licence field and no repository field** and must not be attributed to it. So the one institution-grade claim on this shelf is **unexecuted (`Gap 386-B`) *and* unpublished** — build from it, do not install it. 🆕 `p386`. 🟢 **The only institution-grade LMS MCP server on this shelf.** Wraps the **official Blackboard Learn REST API**; README claims OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log, Prometheus `/metrics`, 40 tools incl. **grade write-back** and webhooks (self-claimed, read not executed). 🔴 Grade write-back is gated or prohibited in several jurisdictions — check [`policy-matrix`](../intel/policy-matrix.tsv) before enabling it. |
| **Blackboard** | [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | 🆕 `p386`. Blackboard **Ultra**, student-side: signs in through the user's own university SSO/MFA in a real browser, **no API key**, read-only. Courses, deadlines, announcements, lecture-slide download. Same author ships Canvas and Moodle siblings. 🟡 A personal tool, not a tenant deployment. |
| **Blackboard** | [alanwtom/blackboard-mcp](https://github.com/alanwtom/blackboard-mcp) | `main` | 🟢 **MIT** *(1,065 B)* | 🆕 `p386`. Local-first, read-only, reads the signed-in student's own Ultra data through their normal browser session. Upstream of the fork below. |
| **Blackboard** | [lukecarroll15/blackboard-mcp](https://github.com/lukecarroll15/blackboard-mcp) | 🔴 **`tcd`** | 🟢 **MIT** *(1,065 B)* | 🆕 `p386`. 🔵 **Two lessons in one row.** The default ref is **`tcd`**, not `main` — a `main`-assuming read returns "no licence". And the payload is **byte-identical to upstream with the holder still `alanwtom`**, so the fork lineage is readable from the grant alone. |
| **Blackboard** | [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | `main` | 🟢 **MIT** *(1,084 B, © "blackboard-mcp contributors")* | 🆕 `p386`. Ultra: courses, content, files, grades, deadlines over the user's own browser session. Collective copyright holder rather than a named individual. |
| **Blackboard** | [Loganxgreaves/blackboard-mcp](https://github.com/Loganxgreaves/blackboard-mcp) | 🔴 **`master`** | 🟢 **MIT** *(1,070 B)* | 🆕 `p386`. Read-only, defaulted to one university (Sheffield Hallam) — re-point via config. Non-`main` default ref. |
| 🔴 ~~**Blackboard**~~ **NOT A BLACKBOARD SERVER** | [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | `main` | 🔴 ~~UNGRANTED~~ → 🟡 **README-ONLY MIT** | 🔴 **`p394` strikes this row from the Blackboard family.** Tree enumerated (9 files): no licence file, no manifest, no SPDX — but `readme.md:84` grants MIT, so the `UNGRANTED` verdict falls. **And it was never a Blackboard integration**: deps `mcp` + `sqlite3`, zero Learn API surface, `blackboard://` = the blackboard *architectural pattern*. Kept here, struck, so the correction is visible where the error was. |
| **Brightspace / D2L** | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p386`. 🟢 **The most substantial D2L server found.** Multi-strategy auth (TOTP, OAuth, browser), retry / circuit-breaker / cache tiers, and **opt-in write operations**. The closest available base for an institution-grade D2L server. |
| **Brightspace / D2L** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | `main` | 🟢 **MIT** *(1,068 B)* | 🆕 `p386`. 🔵 **Upstream of a fork family — count it once.** [`lmgveerhoek`](https://github.com/lmgveerhoek/brightspace-mcp-server) and [`matthewliu10`](https://github.com/matthewliu10/brightspace-mcp-server) publish **byte-identical** payloads still holding `© 2026 Rohan Muppa`; several more forks share the npm name. Grades, due dates, assignments, announcements, rosters, syllabus. Automated login is wired per school. |
| **Brightspace / D2L** | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | `main` | 🟢 **MIT** *(🔵 **1,200 B** — non-stock)* | 🆕 `p386`. The extra bytes are **attribution, not restriction**: an inline notice *"Portions of this software are derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License."* See **Pattern L step 11**. |
| **Brightspace / D2L** | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | `main` | 🟢 **MIT** *(🔵 **2,181 B** — **two stacked grants**)* | 🆕 `p386`. The payload is **two complete MIT licences**: its own (© 2026 Robert McCrary) **plus** *"Portions of this project are derived from d2l-cli: Copyright (c) 2026 Aaryan Kapoor."* 🟡 Shipping it means carrying **both** notices. Go, read-only, pre-1.0. |
| **Anki** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | `main` | 🟢 **MIT** | Not an LMS — the spaced-repetition loop, which pairs with FSRS above. |

### 🆕 `p387` — Dated: which of these servers actually ships a release

Stars are unreadable here and always were a poor proxy. **A publish date is the signal a studio can
act on**: it dates the artefact the client would install. Method and every raw row:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

| server | package | latest | last published | read it as |
|---|---|---|---|---|
| [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | npm `brightspace-mcp-server` | **5.0.8** | **2026-10-22** (today) | 🟢 the most actively published LMS MCP server on this shelf — and a **v5** line, not a weekend project |
| [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | npm `brightspace-d2l-mcp` | 1.4.3 | 2026-10-21 | 🟢 active |
| [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | npm `brightspace-mcp` | 1.3.1 | 2026-09-28 | 🟢 active — corroborates `p386`'s pick as the most substantial D2L base |
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | npm `@r-huijts/canvas-mcp` | 1.5.1 | 2026-09-21 | 🟢 active — the Canvas default, now dated |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | npm `@ankimcp/anki-mcp-server` | 0.27.0 | 2026-10-04 | 🟢 active |
| [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | npm `blackboard-mcp` | 0.1.2 | 2026-09-10 | 🟡 one release, pre-1.0 — **and it is the only publication in its fork family** |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | npm `d2l-mcp-server` | 1.0.1 | 2025-11-28 | 🔴 ~11 months stale |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | npm `canvas-mcp-server` | 2.2.3 | 2025-06-27 | 🔴 ~16 months stale |
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | npm `blackboard-learn-mcp` | — | **never** | 🔴 no published release (see its row above) |
| [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) · [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | PyPI `blackboard-mcp` · npm `canvas-mcp-code-api` | — | **never** | 🟡 clone-and-run tools, not installable packages — fine, but say so to a client |

🔵 **The fork families collapse mechanically, and now there is a second way to see it.** `p386`
collapsed them by **licence bytes** (byte-identical payloads, upstream's copyright holder). The
registry collapses them by **publication**: four Blackboard addresses
([alanwtom](https://github.com/alanwtom/blackboard-mcp),
[lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp),
[Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp),
[felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp)) all declare the package name
`blackboard-mcp`, and **exactly one publication exists** — its `repository` field points at
`felipedias-ie`. Same for [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp), whose fork
kept upstream's scoped name `@r-huijts/canvas-mcp`. **Four addresses, one artefact.** Two
independent instruments, same answer: count the project, not the slug.

🔴 **And this pass's own instrument error, published rather than tidied.**
[faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
declares the package name **`class`** — and npm's `class` is an unrelated **2013** package by
`deadlyicon` (MIT, v0.1.4). A registry lookup keyed on the manifest name alone would have printed
*"MIT, published 2013-08-15"* onto this shelf for a Google Classroom server. **A manifest name is
not a publication.** The gate is now `Pattern L` **step 14**: accept a registry row only when its
`repository` field — or its description links — point back at the same slug.

### 🔵 Supply census: how crowded each platform already is

Counts carried from this base's own cumulative harvest across `agents/top.md` and
[`agents/trending.md`](trending.md) (distinct slugs, not all individually re-verified this pass —
the twelve rows above are the verified subset):

| platform | distinct MCP server slugs harvested |
|---|---|
| Canvas | 35 |
| Moodle | 20 |
| Google Classroom / Workspace for Education | 12 |
| Blackboard | 🔴 ~~9~~ **8** *(`p394`: `anastasasenov/bbmcps` is not a Blackboard integration — see the correction above)* |
| Brightspace / D2L | 6 |
| Open edX | 2 |
| Anki | 1 |

🆕 `p386` — **and the two rows that were only counts are now measured.** 🔴 **Re-stated by `p394`:** of
the **eight** Blackboard slugs harvested — `bbmcps` was never one, and is struck above — eight were
probed first-hand: **6 MIT, 0 ungranted, 2 dead**. Of the six
D2L slugs, **6 MIT** — three of them one upstream and two byte-identical forks. The census column
above counts *addresses*; it never counted *grants*, and for four passes the difference read as an
absence of supply.

🔵 **Read the shape, not the totals.** Canvas and Moodle are saturated with near-duplicate
community servers, of which a minority carry a usable licence — so the work there is **selection**,
not building. Open edX has two, both AGPL and both from one vendor.

## The Blackboard and D2L supply, measured

🆕 `p386`. Until this pass this shelf said **"Blackboard has nine servers and not one verified grant;
D2L has six and the only one checked is ungranted"**, and concluded that both were places where
*"a permissively-licensed server would be a genuine contribution."* 🔴 **That conclusion was wrong,
and it was wrong because nobody had read the grants — not because the grants were absent.**

🔴 **`p394` corrects the sentence a second time, in the other direction.** The nine was never nine:
`anastasasenov/bbmcps` is a shared-memory MCP server that happens to use the word *blackboard* as an
architectural metaphor, so **eight addresses, 6 MIT and 2 dead, and not one ungranted Blackboard
server exists.** 🔵 The original claim was wrong because nobody read the grants; the correction was
wrong because nobody read the *repository*. Both errors are the same error — **a cell inherited as a
count rather than derived from an artefact** — and the second survived four passes of scrutiny that
were all looking at the licence column.

| platform | probed this pass | 🟢 MIT, payload read | 🔴 ungranted | 🔴 address dead |
|---|---|---|---|---|
| **Blackboard** | 🔴 ~~9~~ **8** *(`p394`)* | **6** | 🔴 ~~1 (`anastasasenov/bbmcps`)~~ → **0** | 2 (`e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp`) |
| **Brightspace / D2L** | 6 | **6** | 0 | 0 |

🔵 **The gap moved, it did not close — and the new shape is the actionable part.** Eleven of the
twelve granted servers authenticate as **the signed-in student**: the user's own browser SSO/MFA
session or session cookies, no admin API key, read-only by design and by necessity. Those are
**personal tools**, and a studio cannot deliver one to an institution — it has no tenant identity,
no role boundary, no audit trail, and it breaks whenever the vendor changes a login page.

🟢 **Exactly one reads as institution-grade: [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
(MIT, 1,063 B).** It wraps the **official Blackboard Learn REST API** and its README's architecture
block claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrubbing, a structured JSON
audit log, Prometheus `/metrics`, and 40 tools including **grade write-back** and webhook
subscriptions. 🟡 **Those are maintainer self-claims — read, not executed, this pass**; and the
grade-write-back surface is precisely what [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv)
gates or prohibits by jurisdiction, so the licence clearing it is the *first* gate, not the last.

🔵 **So the restated recommendation:** on Blackboard and D2L the work is **selection plus hardening**
— take a granted server and add tenant auth, role scoping and an audit trail — not greenfield
building. The genuine remaining contribution is **an institution-grade D2L server**: all six granted
Brightspace servers are student-side, and `JhostinAleck/brightspace-mcp` (opt-in writes,
TOTP/OAuth/browser auth strategies) is the closest thing to a base for one.

## 🟡 Two licence traps that a badge-read would miss

🆕 `p389` — **and a third kind: the trap is not in the repository at all, it is in the write-up.**

- [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — a 2026 third-party review of this
  project states it is "**AGPL-3.0**, with commercial licensing available by contact." **It is not.**
  Read first-hand at the real default ref (`main` @ `269fde2d991f`, 2026-10-22): `LICENSE` is **1,066 B
  of stock MIT text**, "MIT License / Copyright (c) 2026 THU-MAIC", and the root `package.json`
  independently declares `"license": "MIT"`. Two sources inside the payload agree; the review is
  simply wrong. 🔴 🆕 `p418` **Two amendments, and the second is larger than the first.**
  (a) The root payload is **`1 065` B**, `sha256₁₂ ba2525637432`, on two channels — the `1,066`
  above is one byte over. (b) 🔴 **"It is not AGPL" was right; "it is MIT" is incomplete** — the
  repository ships **nine** grants, and `packages/mathml2omml/LICENSE` is **LGPL-3.0**
  (`7 652` B, `sha256₁₂ e3a994d82e64`). 🟢 **A root-only read refuted the review and still
  mis-stated the repository**, which is `p382`'s subject exactly: the review was wrong about the
  family, and this base was wrong about the SCOPE. 🔵 **Why this one matters more than a badge mismatch.** A badge mismatch is caught by
  the probe on this page. A *licence claim in a review* is caught by nothing — it is read by a studio
  lead doing exactly the sort of search that produced this pass, and "AGPL + commercial licence"
  reads as *do not propose this to a client*. The largest education-native repository in the supply
  was one secondary source away from being ruled out of every engagement. 🟢 **Procurement rule:
  never let a third-party write-up decide a licence. `Pattern L` is the gate, and it reads the
  payload.**


- [microsoft/autogen](https://github.com/microsoft/autogen) — root `LICENSE` is **CC-BY-4.0**
  (18,649 B, "Attribution 4.0 International"). The **code** grant is a *different file*,
  `LICENSE-CODE` = **MIT**. A tool that reads one file and reports "CC-BY" is wrong about the code,
  and a tool that reports "MIT" is wrong about the docs.
- [open-webui/open-webui](https://github.com/open-webui/open-webui) — `LICENSE` is **2,819 B**
  against stock BSD-3's ~1,500 B. It is BSD-3 text **plus a branding restriction and a Contributor
  License Agreement**, self-titled "Open WebUI License". Not an OSI-standard BSD grant. Prefer
  [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**, 1,065 B) as a campus
  LLM gateway where the licence has to be clean.

## 🆕 `p387` — The institution-grade Brightspace tooling exists, and it is not an MCP server

`Gap 386-A` is *"no institution-grade D2L MCP server exists"*, and that still holds. But the
adjacent question a studio actually asks — *has anyone automated Brightspace against the official
API at institutional scale?* — has an answer this base did not hold:

| tool | channel it was found and read on | licence | what it is |
|---|---|---|---|
| **`bscli`** — Brightspace Command Line Interface | **PyPI** `bscli` (`pypi.org/pypi/bscli/json`) — v**0.3.13**, published **2026-09-04** | 🟢 **MIT** — the *full payload* is carried in the PyPI `info.license` field, © 2024 Ciske Harsema, read first-hand | Grading **operations** at university scale: bulk-download submissions, process them, **distribute them to graders**, collect grades and **upload them back to Brightspace**. Author e-mails are `@ru.nl` — **Radboud University**, EMEA — and the README states it is designed for educational institutions and adaptable to any Brightspace instance. |
| **`d2l-cli`** | **PyPI** `d2l-cli` v0.3.0, published **2026-09-24**, `Homepage` → [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli); grant then read at `main/LICENSE` (MIT, 1,070 B, © 2026 Aaryan Kapoor) | 🟢 **MIT** | *"Read-only CLI client for D2L Brightspace student APIs, built for AI agents."* 🟢 **This closes `Gap 386-E`:** it is the address named in [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP)'s stacked grant, so anyone shipping that server now knows exactly what they are carrying attribution for. |

🔵 **Why these were invisible for four passes, stated as a method lesson.** Both were found by
**package-registry name**, not by a repository search. `bscli`'s own home,
`bscli.science.ru.nl`, is **DNS-unreachable** from this sandbox and no git address for it was
resolvable — so the *grant* is read, the *code* is installable, and the **source address remains
unresolved** (`Gap 387-B`). For `d2l-cli` the registry handed over the address that a repository
search for the string in a licence notice could not: `p386` was right not to guess a slug, and the
registry is where the slug actually lives.

## 🆕 `p389` — Dated: every address on these shelves, in days since last commit

The instrument is the blobless shallow clone described above. **60 addresses, 58 live, 2 dead**, each
dated at its **real default ref** on 2026-10-22. Full table:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). What the dates change:

### 🔴 Stale — and four of them carry a recommendation on these shelves

| address | real ref | days since last commit | licence (payload) | what the date changes |
|---|---|---|---|---|
| [apache/ofbiz](https://github.com/apache/ofbiz) | `trunk` | 🔴 **3,539** *(2017-02-12)* | Apache-2.0 | **A lookalike at the obvious address.** This is the retired monolith. The ERP base recommended on [`verticals/solutions.md`](../verticals/solutions.md) is [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) — **dated 0 days, committed today**. 🟢 The shelf had the right address; a client's engineer typing the obvious one lands on a nine-year-dead tree. Name the `-framework` suffix in the proposal. |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main` | 🔴 **343** *(2025-11-13)* | 🟡 GPL-3.0 | Demoted in *Tier 1* above: a reference for learner-state modelling, not a dependency. |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | `main` | 🔴 **242** *(2026-02-22)* | 🟢 MIT | The Moodle MCP supply is **thinner than its address count** — see the *Supply census*. MIT and 8 months idle is a **vendoring candidate**, not an integration to depend on. |
| [allenai/olmocr](https://github.com/allenai/olmocr) | `main` | 🔴 **211** *(2026-03-25)* | 🟢 Apache-2.0 | 🆕 Not previously on these shelves and **not added as a dependency** because of this date. For parsing scanned course material prefer [docling-project/docling](https://github.com/docling-project/docling) (**MIT, 0 days**) — see [`repos/foundations.md`](../repos/foundations.md). |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | 🔴 **209** *(2026-03-27)* | 🟢 MIT | Confirms `p388`'s own caveat quantitatively: the risk is **currency**, not licence. A curriculum crawl 7 months old is a crawl to re-run, and the MIT grant means you may. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | 🔴 **144** *(2026-05-31)* | 🔴 **NO LICENCE FILE** | Both failure modes at once. It is cited in round-ups as "another open-source option" for Canvas; it is **ungranted and idle**. Not a Canvas option. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | `master` | 🔴 **175** *(2026-04-30)* | 🔴 AGPL-3.0 | 🔵 **The one that should change how the Canvas shelf is pitched.** Eleven Canvas integrations are catalogued on this page, and **the platform's own default ref has not moved in ~6 months** while its `stable/*` branches have. Nothing is wrong with Canvas — this is how Instructure ships — but *anyone cloning `master` to reason about the API surface is reading an April tree*. State the ref you integrated against. |

### 🟢 Live — dated, so the claim is now checkable rather than asserted

**Committed on 2026-10-22, the day of this pass:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
(MIT) · [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) (MIT) ·
[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0) ·
[apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) · [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (MIT) ·
[learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT) · [oppia/oppia](https://github.com/oppia/oppia) (Apache-2.0) ·
[OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0) · [docling-project/docling](https://github.com/docling-project/docling) (MIT) ·
[chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) · [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) ·
[openedx/edx-platform](https://github.com/openedx/edx-platform) · [opencast/opencast](https://github.com/opencast/opencast) ·
[frappe/erpnext](https://github.com/frappe/erpnext) · [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) ·
[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI).

**Within a week:** `HKUDS/DeepTutor` (3 d) · `chrischall/infinitecampus-mcp` (3 d) ·
`learningequality/ricecooker` (3 d) · `CAHLR/OATutor` (1 d) · `CAHLR/pyBKT` (1 d) ·
`vishalsachdev/canvas-mcp` (1 d) · `academico-sis/academico` (1 d) · `moodle/moodle` (1 d) ·
`jupyter/nbgrader` (1 d) · `krayin/laravel-crm` (1 d) · `langchain-ai/langgraph` (1 d) ·
`chroma-core/chroma` (1 d) · `ankitects/anki` (1 d) · `Mattlo0546/canvas-mcp` (2 d) ·
`mem0ai/mem0` (2 d) · `h5p/h5p-php-library` (2 d) · `overhangio/tutor` (2 d) ·
`francoisjacquet/rosariosis` (5 d) · `jupyterlite/jupyterlite` (6 d) · `microsoft/autogen` (6 d).

### 🔴 Two addresses that do not resolve

| address | correction |
|---|---|
| `openedx/tutor` | The Open edX deployment tool is **[overhangio/tutor](https://github.com/overhangio/tutor)** (AGPL-3.0, `release`, 2 d). The `openedx/` org does not carry it. |
| `edx/openedx-app-android` | The `edx/` org is not where the mobile apps live; the Open edX work is under `openedx/`. No mobile client is recommended on these shelves on the strength of a guessed address. |

🟡 **One limit of the instrument, stated.** A date tells you **someone pushed**, not that the project
is healthy, nor that the push was to the branch a release is cut from — `instructure/canvas-lms` is
the whole argument for that caveat. And the reverse: a repository that is *finished* (a
specification, a dataset) is not unhealthy for being quiet. Read the date against what the thing is.

## Verification method

`curl -sI https://github.com/...` returns **403** through this sandbox's agent proxy, and
`api.github.com` returns **403** with an `add_repo` message, so the method prescribed in the run
brief was unavailable. Two stronger channels were used instead and are reproducible:

1. `git ls-remote --symref https://github.com/<slug> HEAD` — proves the address resolves **and**
   returns the **real default ref**. A renamed, deleted or private repository fails here; a HEAD
   request against GitHub's HTML would not have distinguished those.
2. `raw.githubusercontent.com/<slug>/<real-ref>/<path>` — the licence **text**, read first-hand and
   recorded with its byte length, so a hand-edited or non-stock grant shows up as a length anomaly.
3. 🆕 `p389` — **`git clone --depth 1 --filter=blob:none --no-checkout`**, which subsumes both of the
   above and adds the signal they could not reach. One ~1.2 s call yields the real default ref, the
   **HEAD SHA**, the **last commit date**, the **whole root tree** (so "is there a `LICENSE` at all"
   is answered by listing, not by guessing eight paths), and any blob on demand via
   `git show HEAD:<path>` — the grant *and* the manifest that should agree with it. 🟢 It also fixes
   `p384`'s "resolves but has no tree" failure mode by construction: a clone that produces no `HEAD`
   is reported `EMPTY`, distinct from `DEAD`. 🔴 It does **not** give stars, forks, watchers, release
   metadata or an enumeration of the supply — `api.github.com/search/*` stays **403**, so *discovery*
   is still web-search and package registries, and only *verification* is first-hand.

🔵 **`p384` extended the probe set from seven paths to eight.**
[OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) carries a standard GPL-2.0 grant
at **`docs/License.txt`** — absent from all seven root paths, so the old read would have returned
"ungranted" for the most widely deployed open-source SIS in K-12. The probe now also checks
**`docs/License.txt`** and **`doc/LICENSE`** before any ungranted verdict is recorded. 🟡 **No
`p383` verdict is overturned:** the two repositories ruled UNGRANTED
([loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp),
[Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend)) were
re-probed at the new paths this pass and remain ungranted.

🔵 **And a second failure mode `p384` found: an address that resolves with no tree behind it.**
[projectfedena/fedena](https://github.com/projectfedena/fedena) returns refs from
`git ls-remote --heads` but 404s on every content path probed. **`ls-remote` proves a ref, not a
payload** — which is why channel 1 is never sufficient on its own, and why a census built on
resolution alone over-counts the supply.

### Grant read at — provenance for every agent-tier address

The exact ref-and-path each grant above was read from, so any reader can repeat the read.
`<ref>/<path>` resolves as `raw.githubusercontent.com/<slug>/<ref>/<path>`.

| repo | grant read at | licence |
|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main/LICENSE` | Apache-2.0 |
| [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | `main/LICENSE.txt` | Apache-2.0 |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `main/LICENSE` | MIT |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main/LICENSE` | MIT |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main/LICENSE` | BSD-3-Clause |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main/LICENSE` | GPL-3.0 |
| [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | `main/LICENSE` | AGPL-3.0 |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | `dev/LICENSE` | AGPL-3.0 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main/LICENSE` | Apache-2.0 |
| [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main/LICENSE` | Apache-2.0 |
| [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main/LICENSE` | Apache-2.0 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main/LICENSE` | Apache-2.0 |
| [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main/LICENSE` | BSD-3-Clause |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main/LICENSE` | MIT |
| [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main/LICENSE` | MIT — 1,069 B, © 2026 Grupo Sirius *(`p387`)* |
| [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main/LICENSE` | MIT — 1,074 B *(`p387`)* |
| [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main/LICENSE` | MIT — 1,069 B, © 2026 Thiago Silva *(`p387`)* |
| [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli) | `main/LICENSE` | MIT — 1,070 B, © 2026 Aaryan Kapoor *(`p387`)* |
| `bscli` *(no git address resolved)* | PyPI `info.license` payload | MIT — © 2024 Ciske Harsema *(`p387`)* |
| [netless-io/flat](https://github.com/netless-io/flat) | `main/LICENSE` | MIT |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main/LICENSE` | MIT |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | `development/LICENSE` | MIT |
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main/LICENSE` | MIT |
| [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) | `main/LICENSE` | MIT |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main/LICENSE` | MIT |
| [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | `master/LICENSE` | AGPL-3.0 |
| [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master/LICENSE` | AGPL-3.0 |
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | `main/LICENSE` | MIT |
| [lmscloud-io/moodle-mcp-server](https://github.com/lmscloud-io/moodle-mcp-server) | `main/LICENSE` | GPL-3.0 |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | `main/LICENSE` | MIT |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main/LICENSE` | MIT |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | `main/LICENSE` | Apache-2.0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | `main/LICENSE-CODE` | MIT (code); `main/LICENSE` is CC-BY-4.0 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | `main/LICENSE` | not stock BSD-3 — branding clause + CLA |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | — none at 7 paths; no `license` in `pyproject.toml` | UNGRANTED |
| [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | — none at 7 paths; no manifest | UNGRANTED |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main/package.json` (`"license": "MIT"`) | MIT, manifest-only — file absent |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | `main/package.json` (`"license": "MIT"`) | MIT, manifest-only — file absent |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | `main/version.php` (GPL header) | GPL-3.0-or-later, header-granted |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | `main/LICENSE` | MIT *(`p384`)* |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | `main/LICENSE` | MIT *(`p384`)* |
| [inducer/relate](https://github.com/inducer/relate) | `main/LICENSE` | MIT *(`p384`)* |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main/LICENSE` | **ODbL** — share-alike database licence, no code grant *(`p384`)* |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | `master/docs/License.txt` | GPL-2.0 — 🔵 **8th probe path**, absent from all seven root paths *(`p384`)* |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | — `master` resolves; `README`/`README.md`/`LICENSE`/`Gemfile`/`app` all 404 | **nothing read** — no tree to licence *(`p384`)* |
| [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | `main/LICENSE` **and** `v0.1.0/LICENSE` | 🔴 **AGPL-3.0** at `main` (34,523 B stock) · 🟢 **MIT** at tag `v0.1.0` (1,081 B, *"Copyright (c) 2026 Learn Shell contributors"*) — 🔵 **one repository, two refs, two grants**, both read first-hand; relicensed 2026-08-16 *(`p385`)* |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main/LICENSE` | MIT — 1,068 B, © 2026 Zijin Zhang *(`p386`)* |
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | `main/LICENSE` | MIT — 1,063 B *(`p386`)* |
| [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) | `main/LICENSE` | MIT — 1,067 B *(`p386`)* |
| [alanwtom/blackboard-mcp](https://github.com/alanwtom/blackboard-mcp) | `main/LICENSE` | MIT — 1,065 B *(`p386`)* |
| [lukecarroll15/blackboard-mcp](https://github.com/lukecarroll15/blackboard-mcp) | 🔴 **`tcd`**`/LICENSE` | MIT — 1,065 B, holder still `alanwtom` *(`p386`)* |
| [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | `main/LICENSE` | MIT — 1,084 B, © "blackboard-mcp contributors" *(`p386`)* |
| [Loganxgreaves/blackboard-mcp](https://github.com/Loganxgreaves/blackboard-mcp) | 🔴 **`master`**`/LICENSE` | MIT — 1,070 B *(`p386`)* |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | 🟢 **whole tree enumerated** (9 files): no licence file, no SPDX, no manifest — grant at **`readme.md:84`** | 🔴 ~~UNGRANTED~~ → 🟡 **README-ONLY MIT** *(`p394`)* |
| [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | `main/LICENSE` | MIT — 1,070 B *(`p386`)* |
| [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | `main/LICENSE` | MIT — 1,068 B; `lmgveerhoek` and `matthewliu10` byte-identical *(`p386`)* |
| [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | `main/LICENSE` | MIT — 1,200 B, inline derivation notice *(`p386`)* |
| [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | `main/LICENSE` | MIT — 2,181 B, **two stacked MIT grants** (own + `d2l-cli`) *(`p386`)* |
| [Nutlope/llamatutor](https://github.com/Nutlope/llamatutor) | — none at 9 paths; no manifest licence field | UNGRANTED *(`p386`)* |
| [jarodise/Language-Transfer](https://github.com/jarodise/Language-Transfer) | 🟢 **whole tree enumerated** (42 files): no licence file, no SPDX, no manifest — grant at **`README.md:167`** | 🔴 ~~UNGRANTED~~ → 🟡 **README-ONLY MIT** *(`p394`)* |
| [e9x/blackboard-mcp](https://github.com/e9x/blackboard-mcp) · [parkseokjune/unist-blackboard-mcp](https://github.com/parkseokjune/unist-blackboard-mcp) | — `ls-remote` returns nothing | **DEAD / private** — both listed by search results as live MIT servers *(`p386`)* |
**13 of the 58 live addresses are not on `main`** (`master`, `develop`, `dev`, `release`,
`development`, `release_11`, `19.0`) — 🆕 `p386` adds **four more refs** to that list from 22 new
probes: **`tcd`** (`lukecarroll15/blackboard-mcp`), **`master`** (`Loganxgreaves/blackboard-mcp`,
`aureuserp/aureuserp`), **`2.2`** (`krayin/laravel-crm`, a version branch with no `main`) and
**`trunk`** (`apache/ofbiz-framework`). Resolving the ref **before** reading the licence is not
optional; a `main`-assuming read returns "no licence" for every one of them.
