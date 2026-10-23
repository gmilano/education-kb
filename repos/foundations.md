---
industry: education
region: Global
updated: 2026-10-23
---

### 🆕 `p405` — two MIT Moodle MCP rows with PUBLISHED artefacts, and they refute a live recommendation

🟢 **Both read first-hand on 2026-10-23 from FULL clones** — grant from the payload at `HEAD`, tag list
from the clone's own refs, provenance from the root commit and from named files in the tree.
🔴 **Promoted from `p370`'s backlog**, where both have sat on
[`repos/trending.md`](trending.md) and [`agents/trending.md`](../agents/trending.md) without ever
reaching a build-on tier. 🔵 That backlog has been *"carried unmoved"* for eight passes; this moves
**two** rows off it, which is not clearing it.

| repo | layer | licence *(payload, first-hand)* | HEAD · age | tags | published artefact | why it earns a row |
|---|---|---|---|---|---|---|
| [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | **Tier 7 — Integration / MCP** | 🟢 **MIT** *(1,067 B, title line `MIT License`)*, and `package.json` declares `"license": "MIT"` — 🟢 **two channels agreeing** | `7da66c1a...` · 🟢 **1 d** *(2026-10-22)* | 🟢 **6** — `v0.1.0 … v0.5.0` | 🟢 **npm `@falkenslab/moodle-mcp`** | 🟢 **~230 Moodle tools, and it needs NOTHING installed in Moodle** — no web-service token, no admin, no plugin. It drives a **real browser session** (Playwright) logged in as the teacher, so it works on any Moodle 4.5 / 5.x site the user can already log into, SSO and 2FA included. 🟢 **Students are pseudonymised to the model** (`A-7KQ2XM` aliases, de-aliased only on the operator's machine) — `pseudonymization` is a declared `package.json` keyword, not a README adjective. 🟡 Write tools confirm before acting. **194 commits** |
| [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | **Tier 7 — Integration / MCP** | 🟢 **MIT** *(1,064 B)*, and `Cargo.toml` declares `license = "MIT"` — 🟢 **two channels agreeing** | `18bd1777...` · 🟢 **3 d** *(2026-10-20)* | 🟢 **7** — `v0.1.0 … v0.2.1` | 🟢 **crates.io `moodle-mcp`** | 🟢 **A Rust MCP server over Moodle's own Web Services** *(`rmcp` 3.5, Rust 1.88, edition 2024)* — a single static binary, which is the deployment shape a school IT department will accept where a Node runtime will not. Moodle **3.7 → 5.x** via the mobile-app web service. CI + Codecov. **163 commits**, docs as mdBook, README in **8 languages** |

🟢 **Region, for the filter — and one of the two is settled first-hand.**

| repo | region | 🟢 **what the payload says**, not what the name suggests |
|---|---|---|
| `G36maid/moodle-mcp` | 🟢 **APAC** | 🟢 **Established from the tree:** `src/sso/ntust.rs` is a dedicated SSO driver for **NTUST** *(National Taiwan University of Science and Technology)*, and the docs name the two verified deployments as *"NTNU by the credentials mode, NTUST by the SSO driver"*. `Cargo.toml` `homepage = "https://moodle.ntnu.cc"`, and **繁體中文** is the first of the seven translations. 🔵 **Taiwan.** The bare string `NTNU` is ambiguous *(it also names a Norwegian university)* — the **`ntust.rs` driver is what settles it**, because no Norwegian institution is NTUST |
| `falkenslab/moodle-mcp` | 🟡 **Global** | 🔴 **Jurisdiction NOT established, and recorded that way rather than guessed.** The signals are Spanish-language: the only translated docs tree is `/es/`, and the root commit's author is `Francisco Vargas Ruiz`. 🔴 **All 194 commits are authored from `users.noreply.github.com`**, so there is no domain, no institution and no country in the payload — Spain and Spanish-speaking LATAM are both consistent with everything measurable here. 🔵 `T82`: that licenses *"the payload does not name a jurisdiction"*, never *"the project is European"* |

🔴 **What these two refute, and it is a LIVE recommendation on two other shelves.** `p404` wrote, in
[`compose/patterns.md`](../compose/patterns.md)'s layer-2 decision tree: *"`peancor` is the only
permissive option measured here, and its **0 tags** means the pattern vendors a pinned commit rather
than tracking a release."* 🟢 **Both rows above are MIT, both carry tags, and both publish to a package
registry** — so the *"vendor a pinned commit because there is no release"* instruction is no longer the
only option for a studio that cannot ship GPL. 🔵 The correction is made where it bites, on
[`compose/patterns.md`](../compose/patterns.md).

🟡 **The slug that made this invisible, named as a method note.** `p404` measured the group
**`moodle-mcp-server`** and these two are **`moodle-mcp`** — a different slug, so no amount of work on
the first group reaches the second. 🔴 **Both groups answer the same engagement question** *("which
Moodle MCP server do we deploy?")*, and this base's name-collision backlog is keyed on the **slug**,
which is exactly the wrong key for that question. 🔵 Registered on
[`intel/open-gaps.md`](../intel/open-gaps.md).

---


### 🆕 `p404` — the Go LTI 1.3 row is 1,125 days out of date, and a new foundation row replaces it

🟢 **Read first-hand on 2026-10-23 from a FULL-history clone**, not from a rendered page
(🔴 `github.com` HTML is `403` on this session, reproduced against `HKUDS/DeepTutor`) and not from
`--depth 1`, which discards the objects this finding rests on.

| repo | layer | licence *(payload, first-hand)* | HEAD · age | tags | why it earns a row |
|---|---|---|---|---|---|
| [`astiusa/lti`](https://github.com/astiusa/lti) | **Tier 7 — Integration / LTI 1.3** | 🟢 **MIT** *(1,108 B, `sha256`₁₆ `6e58273960b0`, © 2021 MacEwan University — Dept. of Computer Science)* | `6f980746162b` · 🔴 **794 d** | 🔴 **0** | 🟢 **A strict superset of [`macewan-cs/lti`](https://github.com/macewan-cs/lti), which this file already recommends at 1,919 d** — **89 / 89** of `macewan-cs`'s commits are reachable from this HEAD, confirmed by `git merge-base --is-ancestor`. It adds **PKCS8 key support** (2024-08-20) and takes `target_link_uri` from the **login request** rather than from registration, plus a `TargetLinkURI` connector helper (2023-05-22): **11 files, +49 / −26** |

🔴 **`p402` had this pair recorded as *"two unrelated repositories sharing a very short name"*. It is
refuted.** Both share the root commit `228556c`, **2021-05-07**, *"Create LICENSE"*, by Nicholas Boers
— one lineage, not a name collision. 🟢 Direction `macewan-cs` → `astiusa`, verdict `SUPERSET`;
instrument and controls at
[`compose/code/p404-fork-direction/`](../compose/code/p404-fork-direction/README.md), rows in
[`fork-direction.2026-10-23-p404.tsv`](../evidence/fork-direction.2026-10-23-p404.tsv).

🟡 **What this changes, and what it does not.** 🟢 **Changed:** the freshest **permissive Go** LTI 1.3
code on these shelves moves from **1,919 d** to **794 d** — a **1,125-day** correction — and the Go
option is no longer the single worst-dated row in the LTI family. 🔴 **Unchanged:** `p391`/`p392`'s
recommendation stands. 794 d is still dead, **both addresses carry 0 tags** so there is no published
artefact either way, and `macewan-cs`'s own warning (*"the functionality is not stable and we will
almost certainly introduce breaking changes"*, deep linking unimplemented) travels **into** the
superset — `astiusa`'s two commits do not touch it. 🔵 For a Go or JVM platform team the answer is
still **front the agent with `ltijs` or `lti-tool` over HTTP** and keep the Go service behind it.

🔴 **The switching cost that identical licence bytes hide.** The 2023-05-22 commit **changes the Go
module path**. So `astiusa/lti` is a superset by *history* and **not** a drop-in replacement by
*import path*: moving costs an import edit in every consumer. 🟡 **Same grant, same code, different
package identity** — amended onto [`intel/trends.md`](../intel/trends.md), because this base's licence
and alias reasoning had no cell for it.

🟡 **Region, for the filter.** Both addresses are **North America**: `macewan-cs` is MacEwan University
(Edmonton, Canada), and the two superset commits are authored from `asti-usa.com`. 🔵 The institutional
provenance this file already recorded for `macewan-cs` is intact in the fork — the MIT file still reads
**© MacEwan University** byte-for-byte.

---

### 🆕 `p403` — two Indic-language foundation rows, and the licence frontier inside one repository

🟢 **Both grants read from the payload on 2026-10-23**, via `git ls-remote --symref` for the real
default ref and a `--depth 1` clone for the root tree. 🔴 **`github.com` HTML is `403` on this
session**, proved against a known-good control ([`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
also `403`), so the channel is blocked and the addresses are not in doubt.

| repo | layer | licence *(payload, first-hand)* | HEAD · refs | why it earns a row |
|---|---|---|---|---|
| [AI4Bharat/IndicIFEval](https://github.com/AI4Bharat/IndicIFEval) | **Tier 4 — Measurement** | 🟡 **MIT** on the code *(1,074 B, `sha256`₁₆ `1bff713bf26a`, © 2026 Thanmay Jayakumar)* · 🟡 **`CC-BY-4.0`** on the dataset *(its own §License)* | **2026-09-16** · 6 refs | 🟢 **The only Indic-language evaluation asset on these shelves, and the first eval here that can run as a deterministic CI gate.** Verifiable, **rule-based** instruction-following constraints across **14 Indic languages + English** (Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Nepali, Odia, Punjabi, Sanskrit, Tamil, Telugu, Urdu — all 14 enumerated first-hand from the README), with `indicifeval-ground`, `indicifeval-trans` and a bundled `lm-evaluation-harness`. arXiv `2602.22125`; dataset mirrored on Hugging Face. 🔵 Rule-based scoring means **no LLM judge in the loop** — the property that lets it gate a build rather than advise one. |
| [AI4Bharat/Anudesh-Backend](https://github.com/AI4Bharat/Anudesh-Backend) | **Tier 7 — Integration / workflow** | 🟢 **MIT** *(1,067 B, `sha256`₁₆ `e2cd4cec54f7`, © 2023 AI4Bhārat)* | **2026-09-01** · 754 refs · 🔴 **0 tags** | 🟡 **Not education software; a workflow substrate education software keeps needing.** Django, apps `projects` / `tasks` / `users` / `organizations` / `workspaces` / `notifications` / `dataset` / `filters`, composed with Elasticsearch and Celery. 🟢 That is the **assign → attempt → review → report** shape an assessment or marking pipeline needs, plus the collection harness for the Indic instruction data a curriculum-grounded tutor would train or evaluate against. 🔴 **Default ref is `master`** and there are **0 tags** — vendor a pinned commit; there is no published artefact to install. |

🔴 **The licence frontier now runs *inside* a repository, not just between them.** `IndicIFEval` is the
**fourth** `T36` instance on these shelves and the first where **both** halves are commercially usable:
the consequence is **attribution obligations attaching to the data**, not exclusion. 🟢 A SOW that says
*"IndicIFEval is MIT"* is true about the harness and wrong about the benchmark it exists to carry.


**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🔴 **The licence ladder this shelf grades
every candidate with is structurally blind to the largest family on this base — and the family it
cannot see is uniformly copyleft, which is the direction that costs money.**

🔴 **`401-A`, measured over every Moodle plugin address these shelves hold — 60 slugs.** A Moodle
plugin declares its grant in the **header of every PHP file**, because the plugin is the
distribution unit and `version.php` is mandatory. A repository can therefore be unambiguously
licensed and carry **no licence file at all**:

| channel | what it reads | grants found |
|---|---|---|
| **L** — the ladder every prior pass probed | `LICENSE` · `LICENSE.md` · `LICENSE.txt` · `COPYING` | **24** |
| **P** — the family's actual convention | a GNU GPL notice in the **PHP file header** | **51** |

🔴 **27 of 51 readable grants (53%) are invisible to channel L.** 🟢 Where both channels answer
they **agree in all 24** — `CHANNEL_CONFLICT` is **0**, so this is a *coverage* defect and not a
contradiction. Census:
[`moodle-plugin-grant-channel`](../evidence/moodle-plugin-grant-channel.2026-10-23-p401.tsv);
instrument and 20 controls at
[`p401-plugin-grant-channel`](../compose/code/p401-plugin-grant-channel/README.md).

🔴 **Why it is a foundations problem and not a bookkeeping one.** A ladder-blind plugin grades
*"no grant"* or *"unknown"*, and on this shelf an unknown reads as **unencumbered** — the exact
opposite of `GPL-3.0-or-later`. 🟢 **All 51 grants in the family are `GPL-3.0-or-later`. Not one
MIT, Apache-2.0 or BSD in 51 reads.** 🔵 So the single most active integration surface in
education AI is the one a studio can least build a closed product on, and the ladder was quietly
reporting it as the opposite.

🔵 **Lineage, so this is not re-sold as new.** `p275` found this class for **manifests** and
`docs/License.txt` and wrote the rule — *"the LADDER, not the slug, is the defect."* `p394` found
it for **CRAN `DESCRIPTION`**, and [`philchalmers/mirt`](https://github.com/philchalmers/mirt) is
**already on this shelf** labelled *"grant lives only in `DESCRIPTION`; no licence file at any
tree path."* 🟢 **`p401` is that same class in the one large family nobody had tested.** The
general rule, now stated for whichever pass meets the next ecosystem: **read the grant where the
ECOSYSTEM puts it** — `DESCRIPTION` for CRAN, `version.php` for Moodle, `*.csproj`/`nuspec` for
.NET, `pubspec.yaml` for Dart — and treat a four-path licence ladder as a *default*, never as a
denominator.

🔴 **Two address-hygiene findings fall out of the same census.** **7 of the 60 are PHANTOM** —
404 on `version.php` at `main` and `master` **and** 0 results from the authenticated API **with
`fork:true`** (the flag matters: forks are excluded from search by default, so without it a fork
reads as absent): `catalyst/moodle-tool_aiconnect`,
`industria-elearning/moodle-local_forum_ai`, `jmolpea/moodle-block_openaiagent`,
`moodlehq/moodle-local_oneroster`, `moodlehq/moodle-enrol_lti`, `moodle/moodle-enrol_oneroster`,
`Moodle-An-Hochschulen/moodle-local_ai_manager`. 🔵 **Two of those owners — `catalyst` and
`Moodle-An-Hochschulen` — are real Moodle houses whose other plugins exist**, which is exactly how
a plausible wrong address gets written down and never questioned. 🟡 And one
`EXISTS_EMPTY_TREE`: `bycs-lp/moodle-report_ai_analysis` exists per the API (created 2025-10-23,
default `master`) with **no file resolving at `master`**.

🔴 **`401-C`: one live repository was lost to a lowercase letter.**
[`marcusgreen/moodle-tool_aiconnect`](https://github.com/marcusgreen/moodle-tool_aiconnect) —
**10 ★**, default `main`, not archived, `GPL-3.0-or-later` in `version.php` — graded
`ADDRESS_UNRESOLVED` by this pass's first census because it carries **`readme.md`** and
`raw.githubusercontent.com` is **case-sensitive**. 🟢 Rescued. 🔵 `p283`'s `gate-ladder-case`
asks the case-fold question of **licence** ladders; the **branch-control** ladder was never asked.
🔴 **A branch control that is one file makes "no README under that exact name" indistinguishable
from "this branch does not exist", and the damage is quiet: it does not produce a wrong licence,
it produces a smaller shelf.**

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🔴 **No
foundational repo added.** 🟢 **What changed for this shelf is that its GRANT CHANNEL was
re-measured and is OPEN, which is the opposite of what a reader would infer from the policy
channel's state.**

🟢 **Measured this pass, not assumed:** `raw.githubusercontent.com` answers **301** and serves
real licence payloads (`moocupv/lti-ai-grader` `main/LICENSE` → verbatim *"Apache License /
Version 2.0, January 2004"*, corroborating this shelf's recorded Apache-2.0). 🔴 **Every primary
policy host answers `000`**, and `moe.gov.cn`, `beijing.gov.cn`, `cbseacademic.nic.in` and
`algoritmos.uniandes.edu.co` all returned `ENOTFOUND`/`000` to `WebFetch` and `curl` alike.
🔵 **So this session has a first-hand channel for the LICENCE axis and none for the JURISDICTION
axis** — which is worth stating on this page precisely because both axes gate every row here,
and only one of them can be settled first-hand today.

🔴 **The one candidate address of this pass is excluded on the grant, by payload:**
[`andres-tovar-purdue/ai-grader`](https://github.com/andres-tovar-purdue/ai-grader) — four grant
filenames × two branches = **eight 404s**, against a **200** on `main/README.md` as the branch
control. 🟢 No grant, so no promotion, and the exclusion is measured rather than read off an
absent sidebar entry.

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No
foundational repo was added.** 🟢 **`Gap 398-D` is closed, and it closes in the direction that keeps
the shelf as it is.**

[`arthtyagi/judge`](https://github.com/arthtyagi/judge), which `p398` declined while recording
🔴 *"its grant was not read first-hand — stated, not assumed"*, has now been read:
🟢 **MIT** — verbatim *"MIT license"* — **32 ★**, **3 forks**, Python/Django, **56 commits**, and
🔴 **"This repository was archived by the owner on Aug 11, 2022. It is now read-only."**

🔵 **So the grant is permissive and the decision is unchanged.** Four years archived is not a base a
studio starts on, and `p398` declined it on the archive banner alone — 🟢 **the licence read
confirms the call without having driven it**, which is the right order. It stays a census address on
[`trending.md`](trending.md) and off this shelf, per the `Continue` rule.

🔵 **Worth naming plainly:** had the read returned a non-commercial grant, `p398`'s guess would
have been wrong in a way nobody would have caught, because the row was already excluded for a
different reason. 🟢 **An exclusion is not a licence check**, and this base should not let one stand
in for the other.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No foundational
repo was added, and one candidate was deliberately declined.**
[`arthtyagi/judge`](https://github.com/arthtyagi/judge) (**32 ★**, Python) is the single address from
`topic:autograder`'s first page this base did not already hold — 🔴 **and it is labelled "Public
archive"**, so it is recorded as a census address on [`repos/trending.md`](trending.md) and **kept off
this shelf**, because this base does not offer an archived tree as a starting point (the `Continue`
rule). 🔴 **Its grant was not read first-hand** — stated, not assumed: `Gap 398-D`. 🔵 The other nine
rows on that page were already here, which makes the curated-topic channel a corroboration
instrument for this tier rather than a discovery one.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🔴 **Eight addresses on
these shelves are not eight repositories.** `396-F`'s arm, run over the whole shelf for the first
time, found **eight pairs that share a root commit AND a HEAD** — one artefact answering at two
addresses — and three of those pairs sit on the **standards tier this shelf added at `p393`.**
Evidence: [`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv) ·
[`shelf-fork-candidates`](../evidence/shelf-fork-candidates.2026-10-23-p397.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-23-p397.tsv).

### 🔴 The standards tier carries the same artefacts twice, under a rename this shelf never folded

🟢 **`IMSGlobal` became `1EdTech`** in 2022, GitHub keeps the old organisation path answering, and
**this shelf harvested both.** Proven by root **and** HEAD, not by the name:

| folded pair | root (12) | HEAD (12) | verdict |
|---|---|---|---|
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) ↔ `IMSGlobal/caliper-spec` | `563b4accbb4a` | `1849e118b47a` | 🔴 **SAME REPO** |
| [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) ↔ `IMSGlobal/openbadges-specification` | `21cbb1d20fcc` | `04c4bc2ee16d` | 🔴 **SAME REPO** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) ↔ `IMSGlobal/lti-1-3-php-library` | `db5856f2f782` | `3a192de99f37` | 🔴 **SAME REPO** |
| `1EdTech/lti-1-3-php-library` ↔ [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | `db5856f2f782` | 🟢 `66d8e4e4b9bd` **differs** | 🟢 **genuine divergent fork** |

🔵 **The fourth row is why the HEAD field had to be added.** `packbackbooks` shares the ancestry and
has moved independently — so of four same-name pairs on one tier, **three are a bookkeeping artefact
and one is a real engineering choice**, and `396-F`'s single `FORK LINEAGE` verdict called all four
the same thing. 🟢 **Use the `1EdTech` path**: it is where the standards body publishes now.

### 🔴 And the correction this pass owes its own audit: SIX of the eight folds were ALREADY REGISTERED

🔴 **`p397`'s draft presented all eight `SAME-REPO-ALIAS` pairs as findings, and claimed this base
had no gate for them. Both halves are wrong, and `gate-alias-canonical` is what caught it** — the
gate went red on this very shelf while the draft sat in the tree.

🟢 **The register and the gate both already exist**, built at `p349`/`p350` from the **search
index's `full_name` and repository `id`** — a channel entirely independent of this pass's clone
arm. Against [`alias-register`](../evidence/alias-register.2026-10-21-p370.tsv):

| pair | register state | new to the register? |
|---|---|---|
| `1EdTech/caliper-spec` + its STALE sibling | 🟢 `CANONICAL-SELF` / `SAME-REF-SET` | 🔴 **no — `p349`** |
| `1EdTech/openbadges-specification` + its STALE sibling | 🟢 `CANONICAL-SELF` / `SAME-REF-SET` | 🔴 **no — `p349`** |
| `kantord/LibreLingo` + its STALE sibling | 🟢 `CANONICAL-SELF` / `SAME-REF-SET` | 🔴 **no — `p349`** |
| `agent0ai/agent-zero` + its STALE sibling | 🟢 `CANONICAL-SELF` / `SAME-REF-SET` | 🔴 **no — `p349`** |
| [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease) + `openedx/ease` **and** `edx/ease`, **both STALE** | 🟢 **`CANONICAL-SELF` / `SAME-REF-SET` ×3 — `ACTION ZZ-al` CLOSED by `p402`** | 🟢 **YES — the canonical address is NEW to this base** |
| [`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet) + `digitalcredentials/learner-credential-wallet`, its STALE sibling | 🟢 `CANONICAL-SELF` / `SAME-REF-SET` — 🔵 **`p350` already applied the canonical to this shelf and `verticals/solutions.md`** | 🔴 **no** |
| `1EdTech/lti-1-3-php-library` + `IMSGlobal/lti-1-3-php-library` | 🆕 absent → 🟢 **adjudicated `p402`: `1EdTech` CANONICAL, `IMSGlobal` STALE** — 61 refs both, fp `08d380600a05` | 🟢 **YES** |
| `pytorch/opacus` + `meta-pytorch/opacus` | 🆕 absent → 🟢 **adjudicated `p402`: `meta-pytorch` CANONICAL, `pytorch` STALE** — 562 refs both, fp `aeb05358835f` | 🟢 **YES** |

🔴 **So the honest arithmetic is 2 new alias pairs, not 8** — and the draft's *"a census-integrity
defect this base has no gate for"* was describing a gate that has been standing for ~48 passes.
🔵 **`p393`'s warning fired for the third time in this one pass.**

🟢 **What the clone arm genuinely adds, and it is not nothing.** The register's channel is the
**search index**, and for `ease` that channel is **blind**: both rows read `index-returns-ZERO`,
`NO-CANONICAL`, *"the index answers neither address"* — which is why `ACTION ZZ-al` has sat
unresolved since `p350`. 🟢 **The clone arm answers from git alone: shared root `79dd16652a23`,
identical HEAD `056da0adc6f3`, so the two addresses are provably ONE repository** even though the
index cannot see either. 🔴 **It still cannot say WHICH is canonical** — that is `p349`'s rule and
`ZZ-al`'s actual question — so `ZZ-al` was **narrowed, not closed**: the *identity* half proven,
the *direction* half still needing a channel the arm does not have.

### 🟢 `p402` — `ACTION ZZ-al` CLOSED, and the canonical address is one NEITHER candidate named

🟢 **The channel the arm did not have is the HTML header *after* the redirect.** GitHub serves a
rename or transfer as a redirect; the fetcher follows it silently, so reading the
header/breadcrumb of the page you **land on** names the canonical address first-hand.

🔴 **The answer is `openedx-unsupported/ease` — a THIRD address, with zero prior mentions anywhere
in this base.** `ZZ-al` had been framed for ~52 passes as *"which of `edx` or `openedx`?"*, and the
answer is **neither**: both are STALE aliases of an address in an owner literally named
`unsupported`. Confirmed on two channels — the HTML header, and a ref-set fingerprint **identical
across all three addresses** (**173 refs**, fp `e3793cd329e4`, HEAD `056da0adc6f3`, matching the
HEAD this base already published).

🔴 **And it refutes this base's own standing recommendation.** `verticals/solutions.md` advised
🔵 *"Prefer the `openedx` path for anything written today, on the stewardship argument rather than
on the register."* 🔴 **`openedx/ease` is itself stale**, so the advice pointed at an alias — and
the stewardship argument, read correctly, says the opposite of what it was used for: Open edX moved
this code to an **explicitly unsupported** org and **archived** it (read-only since **2024-02-28**,
a status this base already held for `edx/ease`). 🟢 Its **AGPL-3.0** grant was already read at
`master/LICENSE.txt`, 35 136 B. 🔵 So nothing changes commercially — `ease` was already off the
permissive shelf — but the *address* a reader is sent to, and the *reason*, were both wrong.

🔵 **The signature worth keeping**, because it is how this was found: two stale addresses both
report *"NOT A FORK"* with **identical star counts**, which reads exactly like two independent
repositories. *Same stars · no fork line · two owners* is the thing to key on.

🔴 **What the same instrument did NOT settle.** A distinct ref set says *"two repositories"*, never
*"who forked whom"*. `p401`'s carried `moodle-aiprovider_openaicompatible` pair is **narrowed, not
closed**: `ADORSYS-GIS` `371278b0ebd6` and `lmscloud-io` `040b74d5b13e` — **HEADs differ**, so they
are genuinely two repositories and the byte-identical `classes/provider.php` at 3 963 B stays a
lineage signal with **no direction**. Same for `pylti1.3`, `lti` and `moodle-mcp-server`.

### 🟢 One new permissive row, grant read by enumerating the tree

| Repo | Ref · HEAD | Licence — first-hand | ★ | Why it is here |
|---|---|---|---|---|
| 🆕 [`gradescope/gradescope-utils`](https://github.com/gradescope/gradescope-utils) | `master` · `5689b27` · **69 d** | 🟢 **MIT** *(`LICENSE`, 1,070 B, `sha256`₁₆ `1fa57a15a75b`, © 2022 **Turnitin, LLC**)* | **38** | Python harness for **Gradescope** autograders: result JSON, visibility, per-test weighting. 🔵 **The grant is the platform vendor's own** — Gradescope belongs to Turnitin — so an institution that already pays for Gradescope can have a permissive autograder on top of what it licenses, with no new procurement. 🟢 Pairs with `otter-grader` and `edulinq/autograder-py` rather than competing. |

🔴 **And one 91 ★ address that must NOT be vendored:**
[`gradescope/autograder_samples`](https://github.com/gradescope/autograder_samples) has **no licence
at its root** — the only grants in the tree are two **vendored** `jh61b` MIT files (1,075 B,
`8a6114b1d4ae`, © 2016 Josh Hug). 🟢 GitHub shows no licence either, so for once this base's verdict
and GitHub's classifier agree. 🔵 **`p382`'s subtree axis at its sharpest: the MIT in the tree belongs
to a third party's teaching library, and it does not travel to the samples.** Read it; do not fork it.

**🆕 Pass `p396` · reads and commit both 2026-10-23 — second pass of the day, after `p395`.**
🟢 **`p395` dated the LAUNCH layer (LTI 1.3) end to end. This pass does the matching RECORD layer
(xAPI / Learning Record Store) — 28 addresses, one sitting — and the two tables together answer a
question neither could answer alone: *which runtime can a client actually build both halves in?***
Evidence: [`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv) ·
[`channel-state`](../evidence/channel-state.2026-10-23-p396.tsv).

### 🔴 The cross-layer result, and it is a procurement answer rather than a shelf note

| Runtime | Launch layer (LTI 1.3, `p395`) | Record layer (xAPI LRS, `p396`) | Verdict |
|---|---|---|---|
| **Python** | 🟢 `lti-tool` 1 d · `django-lti` 2 d · `ltiauthenticator` 113 d | 🟢 [`openfun/ralph`](https://github.com/openfun/ralph) **MIT**, 10 d, 51 ★ | 🟢 **BOTH LIVE AND PERMISSIVE — the only one** |
| **Node / TS** | 🟢 `ltijs` 9 d | 🟡 [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) Apache-2.0, 75 d, **0 ★** | 🟡 both permissive, record side **unproven** |
| **PHP** | 🟢 `packbackbooks/lti-1-3-php-library` 6 d | 🔴 nothing — `TinCanPHP` is a *client*, 1,450 d | 🔴 launch only |
| **JVM** | 🔴 `UOC/java-lti-1.3-core` 1,193 d | 🟢 [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) Apache-2.0, 21 d, 144 ★ | 🔴 record only — **the mirror image of PHP** |
| **Go** | 🔴 679 d / 1,918 d | 🔴 `GO_LRS` **4,676 d**, self-described *not production ready* | 🔴 **neither layer** |

🔵 **Read it as the second question to ask at procurement, after `p395`'s.** `Pattern AC` already
tells a Java shop it cannot take an in-process LTI dependency from this base. This table says the
same shop *can* take its LRS in-process — `lrsql` is the best-adopted permissive LRS found, on the
JVM — and that a **PHP** shop is in the exactly opposite position. 🔴 **A Go shop should be quoted an
HTTP edge on both layers**, which is a materially different estimate from a Python shop, where both
halves are live, permissive and in-process.

### 🟢 The record layer, dated first-hand — new permissive addresses

| Repo | Runtime | Licence | Bytes / `sha256`₁₆ | HEAD | Age | ★ |
|---|---|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | Clojure/JVM | 🟢 **Apache-2.0** | 11,357 B · `c71d239df917` | `cb794e4` | 🟢 **21 d** | **144** |
| [`openfun/ralph`](https://github.com/openfun/ralph) | Python | 🟢 **MIT** | 1,094 B · `08ea77291de9` | `91fef11` | 🟢 **10 d** | 51 |
| [`yetanalytics/lrs`](https://github.com/yetanalytics/lrs) | Clojure | 🟢 **Apache-2.0** | 11,357 B · `c71d239df917` | `d75e2de` | 🟢 **6 d** | 7 |
| [`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) | Clojure/JVM | 🟢 **Apache-2.0** | 11,357 B · `c71d239df917` | `830a4b2` | 🟢 **6 d** | 0 |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | Node | 🟢 **MIT** | 1,046 B · `c0fc02a86ae2` | `5bc232d` | 🔴 **413 d** | 78 |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | TypeScript | 🟢 **Apache-2.0** | 11,357 B · `c71d239df917` | `4d18e0c` | 🟡 **75 d** | **0** |
| [`nurullahturkoglu/xapi-dotnet`](https://github.com/nurullahturkoglu/xapi-dotnet) | C#/.NET | 🟢 **Apache-2.0** | 11,358 B · `c95bae1d1ce0` | `0d47d65` | 🟢 **1 d** | 1 |
| [`codetakt/kiva`](https://github.com/codetakt/kiva) | Rust | 🟢 **Apache-2.0** | 11,357 B · `c71d239df917` | `addf100` | 🟢 **2 d** | **0** |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | TypeScript | 🟢 **MIT** | 1,080 B · `df57b343c1a3` | `3596bb5` | 🟢 **37 d** | 2 |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | Python/Django | 🟢 **Apache-2.0** | 11,357 B · `58d1e17ffe51` | `efa045e` | 🔴 **496 d** | 334 |
| [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | PHP | 🔴 **GPL-3.0** | 35,121 B · `e1c0ad728983` | `df5c665` | 🟢 **2 d** | 82 |

🔴 **Three corrections to what this base would otherwise have published**, each from the search
channel and each caught by a first-hand read:

- **`LearningLocker/learninglocker` is dead, and it is still the first result for every LRS query.**
  Search reported it *"updated May 2024"*; the git channel puts HEAD at **`5fec948`, 2021-11-16 —
  1,801 days**. It is **GPL-3.0** (35,141 B, `589ed823e9a8`), 585 ★, and carries **no archived banner
  and no deprecation notice**, so nothing on the page warns a reader. 🔵 Anyone who names "the open
  source LRS" from memory names this one. It has not moved in five years.
- **`openfun/ralph` is MIT, not Apache-2.0** — read at the payload, 1,094 B, *"Copyright (c)
  2020-present France Université Numérique"*. The Apache attribution came from a search summary.
- **`adlnet/ADL_LRS` is not a product.** Its own README: *"This version is stable, but only intended
  to support a small amount of users as a proof of concept."* 334 ★ and 155 forks make it look like
  one; it is 496 days old and self-disclaimed.

### 🔴 `xAPI 2.0` has no adopted implementation, and the three claimants total **1 star**

🟢 xAPI 2.0 is **IEEE 9274.1.1-2023**. Three permissive LRSs claim it, all found and dated this pass:
`pelotech/xapi-lrs` (**0 ★**, claims CI against the ADL suite), `nurullahturkoglu/xapi-dotnet`
(**1 ★**, 0.x, claims a passing run on SQLite and Postgres), `codetakt/kiva` (**0 ★**, Rust + F*
proofs). 🔴 **The two best-adopted LRSs do not implement it**: `lrsql` is 1.0.3-era, and Ralph's own
docs say 2.0 *"is not currently supported."*

🟢 **And there is exactly one way to tell these apart, which is the useful half of this finding.**
[`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) — 🟢
**MIT**, 78 ★, Node, `--xapiVersion` selects 1.0.3 or 2.0 — is the referee, and
[`yetanalytics/lrs-test-runner`](https://github.com/yetanalytics/lrs-test-runner) (Apache-2.0, 6 d)
drives it from the JVM. 🔴 **Caveat that belongs on the same line:** the referee is **413 days old**
while all three claimants were written in the last 75, and its README warns it *"should not run
against a production LRS endpoint"* because it persists data. 🔵 So the honest instruction is *stand
up a throwaway endpoint and run the suite yourself* — not *trust the badge*, and not *trust this
table*.

### 🟡 One new licence family this base's own instrument cannot name

[`yetanalytics/xapi-schema`](https://github.com/yetanalytics/xapi-schema) (6 d) is **Eclipse Public
License** — 11,218 B, `a5cb01efb664`, title region *"THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE
TERMS OF THIS ECLIPSE PUBLIC LICENSE."* 🔴 **`EPL` is not in `grant_gate.py`'s `FAMILIES` tuple**, so
the instrument reads a real, permissive, weak-copyleft grant and returns *no family*. See `396-E`.
🔵 Procurement note on the same vendor: `lrsql` the deployable is **Apache-2.0**; `xapi-schema`, the
library underneath it, is **EPL**. One vendor, two grants, different obligations.


# Foundational repos for education

**🆕 Pass `p395` · reads and commit both 2026-10-23.** 🟢 **The LTI layer is now dated end to end — all
13 addresses, one channel, one sitting — and the result is an architecture constraint this base has
never stated: there is NO maintained permissive LTI 1.3 implementation in Go or in Java.** Evidence:
[`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-23-p395.tsv).

🟢 **Three new permissive addresses, two new languages**, none of them previously on any shelf here:

| Repo | Lang | Licence | HEAD | Age | Read |
|---|---|---|---|---|---|
| [`StevenWeathers/peregrine-lti`](https://github.com/StevenWeathers/peregrine-lti) | **Go** | 🟢 **Apache-2.0** | `a442a55` | 🟡 **679 d** | 11,357 B, `sha256`₁₆ `c71d239df917` |
| [`UOC/java-lti-1.3-core`](https://github.com/UOC/java-lti-1.3-core) | **Java** | 🟢 **MIT** | `6db9889` | 🔴 **1,193 d** | 1,060 B, `b6b29f11f74e` |
| [`macewan-cs/lti`](https://github.com/macewan-cs/lti) | **Go** | 🟢 **MIT** | `9ab95e5` | 🔴 **1,918 d** | 1,108 B, `6e58273960b0`  🆕 🔴 **`p404`: SUPERSEDED — [`astiusa/lti`](https://github.com/astiusa/lti) is a strict superset of this address at 794 d (89/89 commits reachable, same MIT bytes). Read the row at the top of this file before citing this one.** |

🔴 **What this means, and it is a budget line rather than a shelf note.** `p391` and `p392` settled
the maintained set as **PHP, Node and Python** — `packbackbooks` (6 d), `ltijs` (9 d), `lti-tool`
(1 d), `django-lti` (2 d), `ltiauthenticator` (113 d), all re-confirmed blind this pass through the
git dating channel rather than inherited. 🔴 **The JVM and Go shelves have nothing live.** The only
permissive Java LTI 1.3 core found anywhere is **1,193 days dead**; the freshest permissive Go one is
**679 days** and pre-1.0. 🔵 So for a client whose platform team is Java or Go — which is most
enterprise and much of European public sector — the honest recommendation is **not** an in-process
library: front the agent with `ltijs` or `lti-tool` over HTTP and keep the JVM service behind it.
That is the same shape `p391` recommended for Python and `p392` then withdrew when `django-lti`
turned up live. 🟡 **It stands for Java and Go, and the dating is why it stands rather than a guess.**

🟡 **`peregrine-lti` is the one of the three worth piloting.** Its own README: *"Technically the launch
flow is feature complete"* and *"this library is in active use so it has been tested and is not just a
proof of concept"* — but *"the public API of the library could still change before the `v1.0.0`
release"*. 🔴 **`macewan-cs/lti` should be read and not installed**: *"the functionality is not stable
and we will almost certainly introduce breaking changes"*, it *partially* implements 1.3, and **deep
linking is unimplemented**. It is MacEwan University (Canada) work, funded by its Faculty of Arts and
Science — 🔵 institutional provenance in **North America**, which is where the LMS integration budget
is, and it has still been untouched for 5 years.

🟢 **Two addresses already cited in patterns are dated here for the first time:**
[`openfun/django-lti-toolbox`](https://github.com/openfun/django-lti-toolbox) **707 d** and
[`Harvard-University-iCommons/django-lti-dynamic-registration`](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration)
**402 d** — both 🟡 **stale**, neither dead. They were carried without dates while the rows beside
them had them.

🟢 **And `394-B` is discharged, so six R rows stop reading as unlicensed.** `cran/exams`
(`GPL-2 | GPL-3`), `philchalmers/mirt` (`GPL (>= 3)`), `patriciamar/ShinyItemAnalysis` (`GPL-3`),
`cran/catR` (`GPL (>= 3)`), `cran/TAM` (`GPL (>= 2)`) and `cran/learnr` (`Apache License (>= 2.0)`)
now carry a **`MANIFEST-ONLY`** grant read verbatim from the `License:` field in `DESCRIPTION`,
which CRAN itself enforces. 🔴 **GitHub's sidebar still shows no licence for any of them**, so the
caveat `394-B` asked for stays on every row: *a reviewer checking the UI will report five granted GPL
packages as unlicensed.* Instrument and controls:
[`compose/code/p395-grant-ladder-fallthrough/`](../compose/code/p395-grant-ladder-fallthrough/README.md).

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** **Tier 3 gains the R half of the
CS-teaching stack**, and the surprise is in the licence column rather than the tier: the three
components that run the teaching loop are **permissive** (`gradethis` 🟢 MIT **164 ★**, `learnr`
🟢 Apache-2.0 **738 ★**, `ottr` 🟢 BSD-3-Clause), and every component that **measures the learner** is
GPL (`exams`, `mirt`, `catR`, `TAM`, `ShinyItemAnalysis`). 🟢 **`gradethis` at 164 ★ edges
`otter-grader` at 161 ★**, so the most-adopted *maintained* autograder on this shelf was never the
Python one. 🔴 **`Gap 397-A`:** outright, `okpy/ok` leads at **370 ★** — Apache-2.0, Berkeley, **532 d** stale.
🟢 **And `cran/exams` is the broadest assessment exporter this base carries** — QTI 1.2 and 2.1,
Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS and six more, **plus NOPS**, a printed exam that is
scanned and marked automatically, which is the only offline assessment loop here. 🔴 Five of those
rows have **no licence file at any tree path**: the grant lives only in `DESCRIPTION`, GitHub's sidebar
shows nothing, and that is **`Gap 394-B`**.

🔴 **`Gap 393-G` is only half closed and the open half is named.** CRAN is refused on **both** tools
(`curl` 000, `WebFetch` ENOTFOUND) and so is r-universe; `github.com/cran/<pkg>` mirrors every CRAN
`DESCRIPTION` and **verifies without discovering**. 🔵 **`cran/gradethis` is ABSENT** — the best row
this pass produced is not a CRAN package at all, so the index `p393` asked for would have missed it.

**🆕 Pass `p393` · 2026-10-22.** This shelf gains **a new Tier 8**, because the thing the new PyPI
index-dump channel found is a *layer* rather than a repository: the **1EdTech standards clients and the
LMS-to-agent bridge live in Python**, where every registry sweep this base had run (all of them npm)
was structurally unable to see them. Channel, limits and the two name collisions it cost:
[`compose/code/p393-pypi-index-channel/`](../compose/code/p393-pypi-index-channel/README.md) ·
[`pypi-index-channel`](../evidence/pypi-index-channel.2026-10-22-p393.tsv) ·
[`verified-repos`](../evidence/verified-repos.2026-10-22-p393.tsv).

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/repos-foundations.md`](../archive/2026-10-22-p383-pre-rewrite/repos-foundations.md).
Every address verified first-hand on this date — method and channel notes in
[`agents/top.md`](../agents/top.md#verification-method), raw results in
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

🆕 **Pass `p389` · 2026-10-22 — increment.** Every address on this shelf is now **dated**: a blobless
shallow clone (`git clone --depth 1 --filter=blob:none --no-checkout`, ~1.2 s, no API, no credentials)
returns the real default ref, the HEAD SHA and the **last commit date**, and `git show HEAD:LICENSE`
returns the grant from the payload at that ref. Method in
[`agents/top.md`](../agents/top.md#verification-method); **60 rows** in
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). **This changes the headline claim
of this file — see the paragraph after the table below** — and it adds three repos to *Tier 4*.

🆕 **Pass `p392` · 2026-10-22 — increment, and it is a CORRECTION of yesterday's increment.**
`p391`'s `Gap 391-A` — *"there is no maintained in-process Python LTI option"* — is **wrong**, and the
refutation was in this base's own harvest log, dated and licence-read, before `p391` wrote it. **There
are three Python LTI 1.3 implementations**, two of them permissive, re-read first-hand today: rows
below. 🟢 This shelf also gains the **serverless** Node LTI route, **two granted proctoring
components** (the gap `p391` opened as `Gap 391-C`), and the **LATAM analogue of the US
district-targeting instrument** (`Gap 391-B`) — INEP Censo Escolar and ENEM, MIT code, keyless.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p392.tsv) — 15 addresses ·
[`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv) — 24 channels, and **the star
channel is open again**.

## 🔴 Read this before choosing a base: the licence frontier in education runs the wrong way

**The platform tier is copyleft. The agent tier is permissive.** That is the single most
consequential structural fact in this industry for a studio that needs to ship client-owned code:

| tier | licences actually found | what it means |
|---|---|---|
| **LMS / platform** | GPL-3.0 (Moodle, Chamilo, ILIAS, H5P), AGPL-3.0 (Open edX, Canvas, Tutor, Frappe LMS), ECL-2.0 (Sakai, Opencast), LGPL-3.0 (OpenEduCat) | Forking the platform pulls copyleft into the deliverable. AGPL additionally reaches **hosted** use. |
| **the one exception** | 🟢 **Apache-2.0 — [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | The only major open-source LMS a studio can extend with closed code. Underweighted by every roundup we read. |
| **agents / tooling** | MIT, Apache-2.0, BSD-3 almost throughout | Permissive. |

🆕 `p389` — **the "one exception" row is wrong, and the dating is what shows it.** There are **four**
permissive platform-tier bases on this shelf, not one, and the reason the claim survived this long is
that the other three were each filed as something narrower than a platform:

| permissive platform base | licence | last commit | the role it actually fills |
|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for an **institution**. Swiss, mature, full LMS. |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | 🔴 `master` | 🟢 **MIT** *(`LICENSE.md`)* | 🆕 `p390`. 🟢 **The permissive courseware engine, and the gap it fills is a licence gap rather than a feature gap.** **Torus** is the authoring-and-delivery platform behind **Carnegie Mellon's Open Learning Initiative** — the group whose course-effectiveness studies are the most-cited evidence base in the field. Pages, structured activities, adaptive **scripted "advanced authoring"** activities, mastery/proficiency reporting per learning objective, LTI 1.3 delivery into a host LMS, and a research-grade analytics surface. 🟢 **Everything else at this scale is copyleft** (Open edX AGPL-3, Canvas AGPL-3, Moodle GPL-3) — so when a client needs to *ship a modified platform* rather than host one, this is the only row on this shelf that lets them. Elixir/Phoenix + PostgreSQL. Dated **2026-10-22** — committed today. 🔴 **Mind the slug:** `CMU-OpenLearning/oli-torus` does not resolve; the canonical owner is `Simon-Initiative`. 🟡 Elixir is a real staffing constraint for most studio teams — cost it before proposing it. |
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for **pedagogy**: misconception-aware branching lessons. Filed in *Tier 2* as content, but it is a platform. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **2026-10-22 (0 d)** | The permissive base for **low-connectivity delivery**, and the only MIT one. Filed as a runtime; it is the platform in any engagement where bandwidth is the constraint. |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🟢 **2026-10-21 (1 d)** | The permissive base for a **course**. |

🔵 **What to say instead of "the platform tier is copyleft."** *The platform tier is copyleft wherever
the install base is* — Moodle, Canvas, Open edX, Chamilo, ILIAS are where the clients already are, and
those are GPL/AGPL/ECL. **Permissive platform bases exist, are all actively maintained, and all cost you
the install base.** That is a trade a client can be walked through; "there is one exception" was not.
The design consequence below is unchanged and is still the default — it is the *greenfield* branch of
the decision that just got three more options.

🆕 `p385` **And a third axis the table above cannot show: the grant can differ by *ref* within one
repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) reads **AGPL-3.0** at
`main` (34,523 B) and **MIT** at tag **`v0.1.0`** (1,081 B) — both read first-hand this pass. It relicensed on
**2026-08-16**. 🔵 So "what is this repository licensed as?" is not a well-formed question; **"what is it
licensed as at the ref I am shipping?"** is. That is now **Pattern L step 10**, and it cuts both ways: a
permissive grant can be *retrievable at a tag* after the project has moved away from it, and a repository
a prior audit cleared as MIT can be AGPL at `main` today.

**The design consequence**, not a preference: compose permissive agents **over** a copyleft platform
across a documented interop boundary — **LTI 1.3**, **MCP**, or the platform's web-services API —
rather than forking the platform. Recipes in [`compose/patterns.md`](../compose/patterns.md).

## Tier 1 — Learning platforms

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** — 🔴 grant is in **`COPYING.txt`**, there is **no root `LICENSE`** | The install base. Moodle Pty Ltd reports 400M+ users and ~150,000 registered sites. Originates in Australia (APAC). Huge plugin catalogue, and now a first-party MCP path. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 `master` | 🔴 **AGPL-3.0** | The MOOC-scale platform: LTI 1.3, XBlocks, deep data control. Deploy via `tutor` below, not by hand. |
| 🆕 `p393` [bmosoluciones/now-lms](https://github.com/bmosoluciones/now-lms) | `main` · `53dcb60` | 🟢 **Apache-2.0** *(10,915 B, `sha256`₁₆ `a9c4042d767d`)* | 🟢 **The permissive LMS this shelf did not have, and it is LATAM-native.** © 2021–2024 **BMO Moreno Berroteran Ortiz Soluciones, S.A. (Nicaragua)**. A complete Flask/Python LMS — courses, delivery, certificates, **monetisation** — at **676 files, 505 commits, 57 releases**, HEAD **2026-08-31 — 52 d**, PyPI `now-lms` v2.0.4, **21 ★**. 🔵 **Why it matters out of proportion to its stars:** every other platform on this tier is GPL (Moodle), AGPL (Open edX, Canvas) or LGPL, so `now-lms` is the **only Tier 1 row a studio can fork, extend and ship closed** — the licence frontier this file opens by describing, crossed at last. 🔴 The trade is scale: 21 ★ against Moodle's install base, and no multi-tenancy claim. Pilot and SME delivery, not a ministry. 🔵 Its non-stock Apache byte count is the **appendix FILLED IN**, not narrowed — `Pattern L` step 4's benign case, distinct from `Ed-Fi`'s absent appendix below. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 `master` | 🔴 **AGPL-3.0** | Dominant in North American higher ed. Open-**core**: the published tree is not the commercial ecosystem, so scope assumptions break on integration. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** | Swiss, mature, permissive. The default recommendation whenever a client needs to own closed extensions to the LMS itself. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** | The LATAM/EMEA public-sector base. Strongest Spanish/Portuguese-language footing of any platform here. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🔴 `master` | 🟡 **ECL-2.0** | Apache-2.0-derived **Educational Community License** — permissive-shaped with an education-specific patent/attribution twist. Read it; do not assume Apache. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** | German public-sector LMS and the learning component of the openDesk sovereign stack. Default ref is a release branch. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 🔴 **AGPL-3.0** *(`LICENSE.txt`)* | The Docker distribution for Open edX and the de-facto deployment path. Nobody should be installing `edx-platform` without it. |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT** *(`LICENSE`, 1,145 B — "MIT/X Consortium license")* | 🆕 `p384`. Django courseware with autograding, flexible access rules, per-student statistics and multi-course support. 🟢 **Permissive at the platform level**, which almost nothing else in this tier is. 🟡 Courseware-scale: the permissive base for a **course**, where OpenOLAT is the permissive base for an **institution**. Do not pitch it as a Moodle replacement. |
| [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | `main` | 🔴 **AGPL-3.0-only** *(`LICENSE`, 34,523 B; `pyproject.toml` → `AGPL-3.0-only`)* | 🆕 `p387`. 🟢 **The platform's own AI extension point — read this before anyone proposes forking Open edX to add AI.** First-party `openedx` org, so the extension surface is maintained with the platform rather than against it; the grant matches the platform's, which is why it can exist inside it. 🟡 Marked **experimental, not for production** in its own docs, so treat it as the contract to build against, not the thing to ship. Compare [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) (`main`, AGPL-3.0, Aulasneo — Argentina) for the LATAM-maintained customisation route. |

## Tier 2 — Content, courseware and assessment

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 **Apache-2.0** | Structured interactive lessons with a real pedagogy engine (misconception-aware branching). Permissive, which is rare at this level of pedagogical depth. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🟢 **MIT** | Offline-first learning runtime for low-connectivity deployment. The single most important repo on this shelf for LATAM and African engagements. |
| [serlo/serlo.org](https://github.com/serlo/serlo.org) | `main` | 🟢 **Apache-2.0** | German open learning platform — permissive, EMEA-native, curriculum-aligned content model. 🔴 🆕 `p390` **Dated: last commit `2023-02-09` — 1,351 days.** Serlo the *service* is very much alive (`serlo.org` serves German schools daily); this *repository* is not where it is developed any more. Keep it as the **content-model reference** — the permissive, curriculum-aligned data shape is still the most useful thing here — but do not plan a fork or a dependency on it, and ask Serlo where the current code lives before quoting an EMEA-native platform base. |
| [openfun/richie](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** | Course catalogue and portal front-end from France Université Numérique. Pairs with Open edX as the public face. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 `master` | 🟡 **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in nearly every LMS. 🔴 **Routinely described as MIT; it is not.** Keep H5P as *content* loaded at runtime, not as linked code. |
| [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 `master` | 🔴 **AGPL-3.0** | Open-response and peer assessment. 🔴 `edx/openassessment` and `openedx/openassessment` are both **DEAD** — this is the live address. |
| [opencast/opencast](https://github.com/opencast/opencast) | 🔴 `develop` | 🟡 **ECL-2.0** | Lecture capture and video pipeline. 🔴 `apereo/opencast` is **DEAD**; use this org. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(`LICENSE.md`, 11,342 B; `composer.json` declares `"license": "Apache-2.0"`)* | 🟢 **THE LTI 1.3 DEPENDENCY TO INSTALL — and it corrects `p390`'s finding #1, which told three shelves there was none.** LTI 1.3 is *the* standards surface for putting an agent inside Moodle, Canvas, Blackboard or D2L, and this is a **live** implementation of it: HEAD `66d8e4e`, **2026-10-16 — 6 days**, shipping as packagist **`packbackbooks/lti-1p3-tool` v6.4.4, 68 versions, published 2026-09-23**. Same Apache-2.0 grant as the 1EdTech copy (byte-identical 11,342 B licence), under active maintenance. 🟢 It keeps the **copyleft-firewall** role intact: permissive code talks to a GPL/AGPL platform over the LTI boundary without linking to it. 🔵 Note the ref is **`master`**, not `main` — a `main`-assuming licence read fails silently. |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(11,360 B; `package.json` agrees)* | 🟢 **The Node LTI 1.3 route, and the better default for an agent stack.** HEAD `41f150c`, **2026-10-13 — 9 days**; npm **`ltijs` v7.0.7, 207 published versions, 2026-10-06** — the most actively released LTI implementation this base has read. A standalone LTI *tool* provider rather than a platform plugin, which is the shape an agent engagement actually needs: the agent is its own service, and the LMS launches into it. 🟢 Prefer this over the PHP line unless the client's platform work is already PHP (a Moodle plugin, an Open edX fork). |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🔴 `master` | 🟢 **Apache-2.0** | 🔴 **DEMOTED to a spec citation — do not install it.** Last commit `2020-06-03` — **2,333 days**, and `composer.json` carries no licence field. An unmaintained PHP library handling OAuth 2 / JWT signing and key rotation is a **security** dependency, not merely a compatibility one. 🟢 The architectural role it was shelved for is not lost: it moves to `packbackbooks/lti-1-3-php-library` (above), which is the maintained line. 🔴 🆕 `p391` **It also has an alias:** [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) returns the **identical HEAD sha `3a192de`** — an org rename, one project at two addresses. Counted **once**. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) 🆕 `p391` | `master` | 🟡 **MIT** | 🔴 **The Python LTI route, and it is genuinely dead — which is an architecture constraint, not a shelf note.** Last commit `2022-11-21` — **1,431 days**; PyPI **`PyLTI1p3` 2.0.0, published 2022-11-20**, 29 releases, none since. 🔴 🆕 `p392` **And `p391`'s conclusion from this row is withdrawn.** It read *"so there is no maintained in-process Python LTI option: the edge must be `ltijs` (Node) or `packbackbooks` (PHP) fronting the Python agent over HTTP"*. `pylti1.3` is dead — that part is right — but **it is not the Python route**; it is one dead address on a road with three live ones (next three rows). `Gap 391-A` is **CLOSED**. |
| [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) 🆕 `p392` | `main` | 🟢 **MIT** *(1,098 B, "Copyright (c) 2022 The Regents of the University of Michigan"; PyPI classifier agrees)* | 🟢 **THE IN-PROCESS PYTHON LTI 1.3 ROUTE, AND IT IS THE ONE `Gap 391-A` SAID DID NOT EXIST.** A Django reusable app providing **LTI Advantage** — `pip install django-lti`, add `lti_tool` to `INSTALLED_APPS`, add `LtiLaunchMiddleware` after `SessionMiddleware`, migrate. That is the whole integration: **no second runtime, no sidecar, no HTTP hop**, which is the deployment component `p391` told three shelves and two patterns to budget for. HEAD `1ac0b56`, **2026-10-20 — 2 days**; PyPI **`django-lti` v0.10.1, 17 releases, 2026-08-07**; 264 commits, **26 ★**. 🟢 Maintained by the **University of Michigan Center for Academic Innovation** — an institutional maintainer in the region that buys the most LMS integration work. 🔴 Django-shaped: a FastAPI or Flask agent still needs the launch handled elsewhere, and there is **no release tagged on GitHub** (read PyPI for the version, not the Releases tab). |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) 🆕 `p392` | `main` | 🟢 **BSD-3-Clause** *(1,528 B, "Copyright (c) 2016, Project Jupyter Contributors")* | 🟢 **The Python LTI route for the one surface where most CS and data-science teaching already happens.** Implements **both LTI 1.1 and LTI 1.3** authenticators for JupyterHub, so an LMS launch lands the student directly in a running notebook with their identity attached. HEAD `c0c3bf3`, **2026-07-01 — 113 days**; PyPI **`jupyterhub-ltiauthenticator` v1.6.3, 15 releases, 2026-03-26**; 523 commits, **73 ★**. 🟢 **This is what makes `Pattern B` whole** — `jupyterhub`, `nbgrader` and [jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) are already on these shelves, and this is the missing launch edge between them and the client's Moodle or Canvas. 🟡 113 days is slower than `django-lti`; for a Jupyter stack that is a feature, not a risk — but read it as a stable component, not an active one. |
| [openedx/xblock-lti-consumer](https://github.com/openedx/xblock-lti-consumer) 🆕 `p392` | 🔴 `master` | 🔴 **AGPL-3.0** *(34,520 B)* | 🔴 **The best-maintained Python LTI 1.3 implementation in any language — and it is off the permissive shelf.** HEAD `5ba9d16`, **2026-10-22 — committed today**; PyPI `lti-consumer-xblock` **v11.4.2**. Recorded as a **boundary, not a pick**: it is the *platform* side (Open edX consuming an external tool), and AGPL-3.0 reaches hosted use. 🔵 Its existence is why `Gap 391-A` should never have been written as a supply claim — the Python LTI supply was not thin, it was **licence-filtered**, and nobody had split those two readings. |
| [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) 🆕 `p392` | `main` | 🟢 **MIT** *(1,076 B)* | 🟢 **The serverless Node LTI 1.3 route — the shape `ltijs` cannot take.** *"Serverless-native LTI 1.3 toolkit for Node.js (Lambda, Workers, Hono)"*: a seven-package monorepo (`@lti-tool/core`, `hono`, `memory`, `dynamodb`, `postgresql`, `mysql`, `d1`) with **OIDC, Assignment and Grade Services, Names and Role Provisioning, Deep Linking and Dynamic Registration** all implemented, and the session store chosen at deploy time rather than assumed. HEAD `1fa0148`, **2026-10-20 — 2 days**; npm **`@lti-tool/core` v1.3.2, 2026-10-21**; 353 commits, **8 ★**. 🟢 Prefer it over `ltijs` when the deliverable is **Cloudflare Workers or Lambda**: `ltijs` assumes a long-running Node process with Mongo. 🔴 **8 ★ and no stated production claim** — the README's only such wording is a *"Production-ready security features"* heading, which is about the security section, not the project. Pilot it; do not put a ministry on it this quarter. |
| [mdestafadilah/proctoring.js](https://github.com/mdestafadilah/proctoring.js) 🆕 `p392` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **THE GRANTED PROCTORING COMPONENT `Gap 391-C` SAID DID NOT EXIST — and its privacy posture is the reason to shelve it rather than merely record it.** *"Zero-dependency browser proctoring toolkit: tab-switch, camera, face and audio monitoring with a single event API."* Detects tab switching, right-click, DevTools/view-source shortcuts, clipboard copy/cut/paste, camera state, **faces**, audio loudness, and **third-party capture software — virtual cameras, loopback audio, screen shares**. Face detection is `@vladmandic/face-api` 1.7.15 on TensorFlow.js/WebGL, **in the browser**. HEAD `c49b41c`, **2026-09-28 — 24 days**; npm **`proctoring.js` v0.5.1, 2026-09-24**; 46 commits, **1 ★**. 🟢 The README's claims are the sellable part, and they are unusually specific: *"No hidden network calls. Nothing leaves the page unless you set `backend.endpoint`"*; audio is analysed in memory and **discarded, never recorded**; the clipboard is **never read** (the event, the element and a character count only); screenshots are **off by default** and held in memory. 🔴 **1 ★, 46 commits, one maintainer** — vendor it, read it, own it; do not sell it as a maintained dependency. 🔴 By default it loads face-api **and its weights from jsDelivr at runtime** — a supply-chain and data-residency defect in any EU or public-sector deployment. **Self-host the weights**; the README says you can. 🔴 And the EU obligation does not transfer with the licence: *you* become the deployer of a high-risk Annex III system the moment this drives an exam decision. |
| [Scaler-Opensource/exam-guard](https://github.com/Scaler-Opensource/exam-guard) 🆕 `p392` | `main` | 🔴 **CONFLICT — Apache-2.0 in the payload, ISC in the manifest** *(`LICENSE` 11,356 B is the stock Apache-2.0 text; `package.json` at the same ref declares `"license": "ISC"`, and npm `@exam_guard/core` v10.1.0 declares ISC too)* | 🟡 **The bigger proctoring codebase, the weaker grant record, and the AI half is explicitly unbuilt.** *"AI Proctoring tool developed by Scaler"* — 398 commits, HEAD `d1193a6`, **2026-10-13 — 9 days**, npm **`@exam_guard/core` v10.1.0, 2026-10-13**, **3 ★**. What it actually ships is **browser lockdown and event telemetry**: blocks copy/paste/cut, right-click, text selection and keyboard shortcuts; detects `tabSwitch`, `browserBlur`, `rightClick`, `exitTab`, `copyPasteCut`, `restrictedKeyEvent`, `textSelection`, `fullScreen`; takes periodic page and webcam snapshots and POSTs events to an `eventsUrl` **you must build**. 🔴 **The README marks object detection, multiple-face detection and eye tracking *"(To be Done)"*** — so the "AI" in the name is a roadmap, not a dependency. 🔵 **Which is good news for a regulated deployment:** lockdown and event telemetry do no biometric inference, so this component is *not* the Annex III surface — the inference you add on top is. 🔴 Both readings of the grant are permissive and OSI-approved, so this is **publishable but ambiguous**; get the maintainer to reconcile the two files before a client depends on it (`gate-conflict`'s class). 🔵 [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) returns the **identical HEAD sha `d1193a6`** — one project at two addresses, counted **once**. |
| [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) 🆕 `p392` | `main` | 🟡 **MIT — CODE ONLY** *(1,069→1,072 B, "Copyright (c) 2025-2026 MCP Brasil"; `pyproject.toml` and the PyPI classifier agree — **and the README states the grant covers the code alone: each of the 70 data sources carries its own licence in `SOURCES.md`, under an `ACCEPTABLE_USE.md` policy**)* | 🟢 **THE LATAM ANALOGUE OF THE US DISTRICT-TARGETING INSTRUMENT — `Gap 391-B` closed for Brazil, 24 hours after it was opened.** An MCP server over **70 Brazilian public data sources**, 533 tools, **66 of them needing no API key**, with large datasets cached locally and queried through embedded DuckDB. The education ones are the point: **INEP `censo_escolar`** (the national school census — the per-school enrolment and infrastructure base a Brazilian pilot is scoped against) and **INEP `enem`** (the national exam microdata). HEAD `2efb258`, **2026-08-18 — 65 days**; PyPI **`mcp-brasil` v0.14.0, 18 releases, 2026-04-24**. 🟢 **Its LGPD handling is why this is shelvable and not merely findable.** `SOURCES.md` grades *Educação* **RISCO ALTO**, records that INEP withdrew microdata in 2022 under LGPD and resumed anonymised publication in 2024, states that the bundled snapshot is **2023, post-LGPD**, and documents a **code safeguard**: `COLUNAS_DISTINCT_PERMITIDAS` whitelists aggregate categories only (UF, sex, age band, race, school) and **does not expose** `NU_INSCRICAO`, name or CPF. 🔴 **Three limits to state in a proposal:** the data is a **2023 snapshot**, so currency is the risk and not the licence; the project's own note is to *validate a sample to confirm anonymisation*; and it is **explicitly not an official government service**. 🔴 A dating disagreement, published rather than resolved: this base's harvest row reads *"pushed 2026-10-20"* while `main`'s HEAD commit is **2026-08-18**. Two different signals — `pushed_at` spans every ref, a HEAD date does not. 🔵 This row is also `Gap 549` in the flesh: **a code grant and a data grant in one repository**, and this shelf's licence column was built for the first. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main` | 🟡 **`(ODbL-1.0 AND CC-BY-SA-4.0)`** 🆕 `p390` *(exact SPDX expression, read from `package.json`; the tree carries **two** files — `LICENSE` (ODbL, 25,289 B) and `LICENSE-CONTENT`. There is still no separate permissive code grant.)* | 🆕 `p384`. **The curriculum prerequisite graph**: `v1` ships **1,930 micro-topics** and **4,102 prerequisite edges** as a DAG (`hard`/`soft`, each edge carrying a reason) over **9 subjects**, aligned to NGSS, Common Core, the UK National Curriculum and the Australian curriculum. Data at `data/topics.json`, `data/dependencies.json`, `data/teaching-research.json` (~24 MB). 🔴 **A share-alike *database* licence, not a code licence** — grounding a tutor on it is a §4.3 *Produced Work* (attribution notice only); shipping an extended taxonomy is a §4.4 *Derivative Database* (share-alike). See **Pattern H**. 🟡 Maintainer-stated gap: teaching research covers **1,049** topics, **881 have none**. 🔴 🆕 `p390` **The `CC-BY-SA-4.0` half is the one that reaches the client deliverable**: the *content* (topic prose, teaching research) is share-alike independently of the ODbL database right, so a curriculum document generated from it can inherit SA even where the DAG itself is only a Produced Work. Clear this with the client's legal team **before** it is a deliverable, not after. Dated `2026-10-22` — actively maintained. |
| [intellectif/learning-kit](https://github.com/intellectif/learning-kit) 🆕 `p391` | `main` | 🟢 **MIT** *(1,071 B; `package.json` agrees)* | 🟢 **A permissive, headless alternative to H5P — and the assessment component this shelf was thin on.** TypeScript-first SDK for interactive educational activities, described by its own README as *"a lightweight, composable, bring-your-own-backend alternative to H5P"*, for React 19. `@intellectif/lk-core` is the part that matters to a studio: **schemas, a pure scoring engine, rubric and deferred grading, assessment composition, attempt plans, redaction, and an xAPI statement builder — with zero runtime dependencies beyond Zod**. `@intellectif/lk-react` adds components and a resumable exam/review pager. 🟢 **Three properties that decide an engagement:** scoring is a *pure function* a client can unit-test and an auditor can read; **deferred grading** means a human marker stays in the loop by construction, which is the posture EU high-risk assessment obligations ask for; and **redaction** is in the core rather than bolted on. 🟢 Pairs directly with the xAPI/LRS rows on this shelf — it emits statements, it does not store them. HEAD `1e39e9e`, **2026-10-18 — 4 days**. 🔴 **It is deliberately not a CMS:** authoring UI, content storage, delivery, auth and the learner database are the consuming application's job. 🟡 The two packages' version numbers moved apart at 1.0, so a `lk-react` major is not by itself a breaking React API change — read its changelog. |

## Tier 3 — Grading, notebooks and the CS-teaching stack

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | `main` | 🟢 **BSD-3-Clause** | Multi-user notebook serving — the standard way a cohort gets identical compute. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** | Release / collect / autograde / return. The assignment lifecycle, already solved. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🔴 `master` | 🟢 **BSD-3-Clause** | Autograding at Berkeley cohort scale; container-isolated execution. |
| 🆕 `p393` [edulinq/autograder-py](https://github.com/edulinq/autograder-py) | `main` · `7984bd2` | 🟢 **MIT** *(1,071 B, `7eb48830c022`)* | The **submission and feedback** client for the edulinq autograding server — the half `nbgrader` and `otter-grader` leave to the institution. **49 releases**, 494 commits, HEAD **2026-10-02 — 20 d**, **16 ★**. 🔵 Pairs with `otter-grader` (grading) rather than competing with it. |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Pedagogical assessment of *how* code was written. The missing half of autograding. 🔴 🆕 `p387`: **PyPI `pybryt` has had no release since v0.7.0 on 2022-04-28.** Keep it as the design it states, vendor the code, and do not sell a client a dependency that has not shipped in four and a half years. The maintained halves of this tier (`nbgrader`, `otter-grader`) are where the running infrastructure should sit. |
| 🆕 `p394` [rstudio/gradethis](https://github.com/rstudio/gradethis) | `main` · `48aaf89` | 🟢 **MIT** *(1,078 B, `48c18e68ffed`; `DESCRIPTION`: `MIT + file LICENSE`)* | **Automated feedback for student exercises**, from **Posit Software, PBC**. `grade_this_code()` compares against a model solution; `grade_this()` takes a predicate you write. HEAD **2026-06-18 — 126 d**, **164 ★**, 41 forks. 🟢 **The most-starred *maintained* autograder on this shelf and the most permissively licensed** — it edges `otter-grader` at 161 ★. 🔴 `okpy/ok` leads outright at **370 ★**, 532 d stale (`Gap 397-A`). 🔴 **Not a CRAN package** (`cran/gradethis` ABSENT), so install from GitHub or r-universe, not from CRAN. |
| 🆕 `p394` [rstudio/learnr](https://github.com/rstudio/learnr) | `main` · `e7164a8` | 🟢 **Apache-2.0** *(10,472 B, `60a581bccd57`)* | **Interactive tutorials in R Markdown** — the runtime `gradethis` grades inside; the two are a pair, not alternatives. **738 ★**, 241 forks. 🟡 HEAD **2025-11-13 — 343 d**: a stable substrate rather than an abandoned one, and the movement is in `gradethis`. |
| 🆕 `p394` [ucbds-infra/ottr](https://github.com/ucbds-infra/ottr) | 🔴 `master` · `693b3df` | 🟢 **BSD-3-Clause** *(1,555 B, `1677c5307530`; `DESCRIPTION`: `BSD_3_clause + file LICENSE`)* | **The R autograding extension for `otter-grader`** (row above), UC Berkeley Data Science Education Program — grades R scripts, Rmd documents and Jupyter notebooks with R kernels. HEAD **2026-07-06 — 108 d**. 🟢 So this tier's flagship autograder is permissive in **both** languages. 🔴 **3 ★**: the adoption sits on the Python parent, but this is the component an R course actually deploys. |
| 🆕 `p394` [cran/exams](https://github.com/cran/exams) | `master` · `baa3e28` | 🟡 **GPL-2 \| GPL-3** — 🔴 **disjunctive**, and 🔴 **no licence file at any tree path**: the grant is the `License:` field in `DESCRIPTION` | **R/exams v2.4-5**, Achim Zeileis (R-project). HEAD **2026-10-08 — 14 d**. 🟢 **The broadest assessment exporter on these shelves**: QTI 1.2, QTI 2.1, Moodle XML, Blackboard, Canvas, OpenOlat, ILIAS, TestVision, Particify, ARSnova, Kahoot!, Grasple, TCExam — read from the `R/` source filenames in the clone (`exams2qti21.R`, `exams2moodle.R`, `exams2canvas.R`, …), not from its prose. 🟢 **Plus NOPS**: a standardised PDF printed, scanned and marked automatically — the only offline assessment loop in this base. 🔵 Belongs with **Tier 8** as much as here; it is the generator the standards layer consumes. |
| 🆕 `p394` [philchalmers/mirt](https://github.com/philchalmers/mirt) | `main` · `e37f14c` | 🟡 **GPL (>= 3)** — 🔴 **`DESCRIPTION` only; GitHub's sidebar shows no licence** | **Multidimensional item response theory** — the canonical IRT engine, v1.48.2. HEAD **2026-10-21 — 1 DAY**, **235 ★**, 88 forks. 🔵 This shelf's Tier 4 carries `adaptive-knowledge-graph` (IRT + BKT, ~350 ★) and `OATutor` (BKT) as the adaptive layer; **`mirt` is the thing those approximate**, and it is committed daily. Sibling [`cran/catR`](https://github.com/cran/catR) (🟡 GPL >= 3, v3.17) is the **computerized adaptive testing** engine, [`cran/TAM`](https://github.com/cran/TAM) (🟡 GPL >= 2, v4.3-25) the test-analysis modules, and [`patriciamar/ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) (🟡 GPL-3, **47 ★**) the non-programmer front end. |

🔴 **The licence line through this tier runs between DELIVERY and MEASUREMENT, and `p394` found it by
accident.** The three components that *run the teaching loop* are permissive — `gradethis` MIT,
`learnr` Apache-2.0, `ottr` BSD-3-Clause — and every component that *measures the learner* is GPL:
`exams`, `mirt`, `catR`, `TAM`, `ShinyItemAnalysis`. 🟢 **That is a workable boundary rather than a
blocker**, because it falls exactly where a studio's product boundary falls anyway: embed the tutoring
and grading loop, reach the psychometrics **over a process boundary**, the same discipline `Pattern A`
and `Pattern O` already apply to copyleft LMSs. 🔴 **But `cran/exams`'s grant is disjunctive — GPL-2
*or* GPL-3 at the licensee's choice — and that choice must be recorded once, deliberately**, because
downstream compatibility differs between the two rungs.

🔴 **A provenance warning this tier needs and the others do not.** `cran/exams`, `mirt`,
`ShinyItemAnalysis`, `cran/catR` and `cran/TAM` have **no licence-shaped file at any path in their
trees** — enumerated, not guessed. GitHub's sidebar therefore shows **no licence** for all five, and a
reviewer who checks the sidebar will report five granted GPL packages as unlicensed. The authoritative
grant is the `License:` field in `DESCRIPTION`, which is what CRAN itself enforces. 🔵 Registered as
**`Gap 394-B`**, because this base already knows the rule — `p1052` carries `DESCRIPTION` in its
manifest list with a test asserting *"CRAN: the grant lives in DESCRIPTION and must be read
verbatim"* — and `licence-grant-gate`, the instrument that produces the verdicts, does not.

## Tier 4 — Measurement, memory and retrieval (what makes the agents honest)

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | 🟢 **MIT** *(`LICENSE.md`)* | The eval runner. Nothing in this industry should ship without a before/after on the client's own subject mix. |
| [hendrycks/test](https://github.com/hendrycks/test) | 🔴 `master` | 🟢 **MIT** | **MMLU** — 57 academic subjects. The subject-level breakdown is the useful part, not the headline score. |
| [openai/grade-school-math](https://github.com/openai/grade-school-math) | 🔴 `master` | 🟢 **MIT** | **GSM8K** — multi-step arithmetic reasoning; the canonical K-12 maths probe. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | 🟢 **MIT** | **FSRS** scheduler. A retention model with published parameters — the part of "personalisation" that is actually measurable. Note [ankitects/anki](https://github.com/ankitects/anki) itself is **AGPL-3.0**; the scheduler is the reusable piece. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | 🟢 **Apache-2.0** | Document-aware RAG — handles the textbook/worksheet/PDF reality of course material. |
| [livekit/agents](https://github.com/livekit/agents) | `main` | 🟢 **Apache-2.0** | 🆕 `p390`. 🟢 **The realtime voice substrate — the piece a spoken tutor should never write itself.** Full-duplex STT → LLM → TTS pipelines with **turn detection, interruption handling and barge-in**, the three things that separate a tutor a child will talk to from a demo. Provider-agnostic on all three legs, so the ASR can be swapped for a local model where data residency demands it. This is what `Manu` (Tier 4, [`agents/top.md`](../agents/top.md)) is built on, and why that project is ~15 days old and already has a working voice loop. Dated **2026-10-22**. See 🆕 `Pattern V`. |
| [mozilla/common-voice](https://github.com/mozilla/common-voice) | `main` | 🟡 **MPL-2.0** *(code; the **corpora** are **CC0-1.0**)* | 🆕 `p390`. 🟢 **The licence answer to regional-language speech.** Crowd-sourced, CC0 speech corpora across ~130 language variants — including **pt-BR, es-419 variants, Kiswahili, Hindi and Bengali** — which is the fine-tuning and ASR-evaluation data a voice tutor needs outside English. 🟢 **CC0 on the data is the strongest possible position**: no attribution, no share-alike, usable in a commercial deliverable. 🟡 MPL-2.0 is weak file-level copyleft and applies to the **platform code**, not the corpora — do not conflate the two when quoting. Dated **2026-10-21**. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | `main` | 🟢 **Apache-2.0** *(`LICENSE.md`)* | Ingest for the formats education actually runs on: PDF, DOCX, PPTX, scans. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | 🟢 **MIT** | Programmatic prompt optimisation — turns "we tuned the tutor prompt" into something with a metric attached. |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | 🟢 **MIT** | The campus LLM gateway universities actually deploy: multi-provider, SSO, per-user quota, audit. MIT where the obvious alternative is not (see [`agents/top.md`](../agents/top.md)). |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🔴 `master` | 🟢 **MIT** | 🆕 `p389`. **Bayesian Knowledge Tracing, fitted from the client's own interaction logs** — and the maintained answer to a gap this base has carried for two passes. `Pattern B` stands on [microsoft/pybryt](https://github.com/microsoft/pybryt), whose published artefact has had **no release since 2022-04**; this is a *different* job (mastery estimation, not approach assessment) but it is the piece that makes "adaptive" a number instead of an adjective. 🟢 **Last commit 2026-10-21 (1 d)**, from UC Berkeley's CAHLR, who also maintain [`OATutor`](https://github.com/CAHLR/OATutor) (MIT) on [`agents/top.md`](../agents/top.md). 🟢 Per-skill learn/guess/slip/forget parameters are inspectable and defensible — which is what a district's procurement rubric asks for when it asks how the system decides a student is behind. |
| [docling-project/docling](https://github.com/docling-project/docling) | `main` | 🟢 **MIT** | 🆕 `p389`. **Course-material ingest, MIT, and committed today (0 d).** Layout-aware parsing of PDF, DOCX, PPTX, XLSX, HTML and images into a structured document model, with table structure and reading order preserved — which is the difference between a tutor that can cite page 7's table and one that cannot. 🟢 Chosen over [allenai/olmocr](https://github.com/allenai/olmocr) (Apache-2.0) **on the date**: olmocr's last commit is **2026-03-25, 211 days**. 🟢 Complements, not replaces, [`unstructured`](https://github.com/Unstructured-IO/unstructured) — docling is the stronger reader for textbook-shaped PDFs, `unstructured` has the wider connector set. |
| [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) | `main` | 🟢 **BSD-3-Clause** | 🆕 `p389`. **Jupyter with no server: the kernel runs in the browser via WebAssembly.** Last commit 2026-10-16 (6 d). 🟢 Two education problems it solves outright: a CS or data-science exercise that needs **no per-student compute, no container and no install** (the cost line that kills notebook teaching at scale), and a **lab that works offline once the page is cached** — the `Pattern D` constraint, met without shipping a server. 🟡 No server means no server-side autograding: pair it with [`nbgrader`](https://github.com/jupyter/nbgrader) on a submitted notebook rather than expecting it to assess in place. |
| [pipeworx-io/mcp-education-data](https://github.com/pipeworx-io/mcp-education-data) 🆕 `p391` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **The first row on these shelves that answers *which district*, rather than *what to build* — engagement targeting and funding data, not a classroom capability.** Four MCP tools over **keyless US federal data**: `education_find_schools` (NCES Common Core of Data via the Urban Institute — enrolment, charter/magnet status, grade range, free/reduced-price lunch counts), `education_find_districts` (LEA id, schools, enrolment, teacher counts), **`education_district_finance`** (revenue split **federal / state / local** and expenditure by function, with computed **per-pupil spending**) and **`education_child_poverty`** (Census SAIPE estimates of 5–17-year-olds in poverty — **the figures that drive federal Title I funding**). 🟢 **Why a studio cares:** a North America pitch can be priced against a named district's actual per-pupil budget and Title I eligibility before the first call. 🔴 **Three caveats that belong in the row:** it is an **unofficial** integration, not affiliated with the upstream provider; the default path is a **hosted gateway** (`gateway.pipeworx.io`), so a district deployment means self-hosting or accepting a third party in the data path — the data is public, but the *query pattern* may not be something a client wants off-premises; and a scoped endpoint also lists **~30 shared gateway meta-tools**, so the real context cost is far above four tools. 🟡 The finance survey **lags the directory data by 1–2 years** — never quote per-pupil spend as current-year. HEAD `060371b`, **2026-10-21 — 1 day**. |

## Tier 5 — Student information / administration

| repo | default ref | licence | note |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** | Odoo-based education ERP/SIS. Default ref is a **version branch**, `19.0` — there is no `main`. 🔴 `OpenEduCat/OpenEduCat` is **DEAD**; this is the live address. Its Brazil and Mexico country pages are vendor marketing — treat feature claims as unverified. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 **MIT** | Laravel school-management platform with **Spanish and French built in**. SME-scale, not university-scale. The only permissive, Spanish-native administration platform found in this pass — relevant to the LATAM supply gap recorded in [`intel/market.md`](../intel/market.md). |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`master`** | 🟡 **GPL-2.0** — 🔴 grant is at **`docs/License.txt`** (17,286 B), **not** at any root path; `index.php` and `Modules.php` headers pin *"version 2 of the License"* | 🆕 `p384`. The most widely deployed open-source SIS in the K-12 tier. GPL-2.0 is survivable the same way Moodle is — reach it over its API, do not link to it. 🔵 **This repo is why the licence probe set grew from seven paths to eight**: a root-only read returns "ungranted" for a repository with a perfectly standard grant one directory down. |
| 🆕 `p393` [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) | `main` · `6b13cb9` | 🟢 **Apache-2.0** *(11,357 B, `c71d239df917` — 🔵 **STOCK**, this pass's reference byte count)* | 🟢 **The North American K-12 data path, and the first Ed-Fi row on these shelves.** Ed-Fi is the dominant US K-12 **data standard** (state longitudinal systems, district warehouses); this is a maintained Python client for its API — paging, auth, swagger introspection, async pulls. HEAD **2026-10-06 — 16 d**, 79 commits, PyPI v0.4.1, **15 ★**. 🔵 For a North America engagement this is the **roster-and-outcomes join** that `Gap 391-B`'s district instrument needs, and it is Apache-2.0. |
| 🆕 `p393` [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit) | `main` · `b1266b7` | 🟢 **Apache-2.0** *(10,141 B, `cc4d4de0920b` — 🔴 non-stock: the **APPENDIX IS ABSENT**)* | 🔴 **ARCHIVED BY ITS OWNER ON 2025-03-10 — READ-ONLY.** Extractors for **Canvas, Google Classroom and Schoology** into Ed-Fi, plus a harmonizer: 763 files, 451 commits, PyPI `edfi-lms-harmonizer` v1.2.2. 🔵 Published **because** it is archived: it is the best available map of the LMS→Ed-Fi field mappings, and a studio should **read it and port it**, never depend on it. An archived upstream takes no security patch. 🔴 This is the state the licence column cannot show — `Gap 393-E`. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 **AGPL-3.0** — grant is in lowercase **`license.txt`** | Frappe/ERPNext-ecosystem LMS; attractive where the client already runs ERPNext. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 **GPL-2.0-or-later** *(`2.12/LICENSE`, 18,092 B; `composer.json` → `GPL-2.0-or-later`)* | 🆕 `p387`. 🟢 **Brazil's largest free education software, and the SIS a LATAM public-sector engagement will actually meet** — *"o maior software livre educacional do Brasil"*, municipal-scale student records, enrolment, grades. 🔴 **Its real default ref is `2.12`** — a version branch, neither `main` nor `master`: resolved with `git ls-remote --symref` (HEAD `7903a3e`). A `main`-assuming clone or licence read fails or reads the wrong tree, and a `master`-assuming one reads a branch that is not HEAD. 🟡 GPL-2.0 at the platform, so reach it over its API and keep the agent a separate service (`Pattern O`). Sibling `portabilis/i-diario` is AGPL-3.0 — the grant is a per-repository fact, not an organisation-wide one. |

## 🆕 `p387` — Tier 6: the multi-tenant AI layer, which is the thing `p386`'s tenancy gap was asking for

`p386` replaced a licensing gap with a **tenancy** gap: every granted LMS MCP server authenticates
as the signed-in student, so *"a studio cannot deliver one of those to an institution."* On Moodle
the tenancy layer already exists, it is maintained by a state education authority, and this base
has never shelved it.

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) | `main` | 🟡 **GPL-3.0-or-later — granted in the source headers** (`version.php`), no root licence file | 🟢 **A multi-tenant AI backend for Moodle, explicitly offered as the alternative to Moodle 4.5's own single-tenant AI subsystem.** Two subplugin types — `aitool` (connect ChatGPT, Gemini, Dall-E, **Ollama**…) and `aipurpose` (bind a *purpose* to a tool **per role**) — plus per-role rate limits, per-tenant user enable/disable, usage monitoring, teacher visibility of student prompts (capability-gated), and tenant-handling hooks. Release **5.1.1**, version code **2026102305**. 🟢 This is the component that turns "an agent talks to the LMS" into "an institution can deploy it": the **sovereign EMEA option in `Pattern E`**, from Bavaria's state school platform, with a local-model path via the Ollama tool. 🔵 **Cite this address.** The `mebis-lp` organisation serves the same repository at `mebis-lp/moodle-local_ai_manager`, which this base's alias register already records as **STALE** (canonical: `bycs-lp/moodle-local_ai_manager`, resolved `p350`, confirmed `p370`) — 🆕 `p387` re-confirms it mechanically: `git ls-remote --symref` returns the **identical HEAD sha `4ff5a87`** at both, and `version.php` the identical component, release **5.1.1** and version code **2026102305**, which upgrades `p226`'s sibling-set inference from *weak* to an identity read. One repository, one row. |
| [bycs-lp/moodle-block_ai_chat](https://github.com/bycs-lp/moodle-block_ai_chat) | `main` | 🟡 **GPL-3.0-or-later** in `version.php` | The chat frontend that consumes the manager's API. 🔵 Cited at the canonical org, as above; the manager's own README links the sibling set under `mebis-lp` — `tiny_ai`, `block_ai_control` — and both orgs answer, so resolve the ref before you pin one. The family also includes [marcusgreen/moodle-qtype_aitext](https://github.com/marcusgreen/moodle-qtype_aitext) (AI-marked question type, `main`, resolved this pass). **Deploy the manager first, then pick frontends** — not the other way round. |

🔵 **Second instance of `Pattern L` step 8, and it is now a Moodle-wide rule, not an anecdote.**
`p386` found [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp)
granted **only** in `version.php`. Both plugins above are the same: **no root licence file, a full
GPL-3.0-or-later header in `version.php`.** For a Moodle plugin that is the convention Moodle
requires, so *"no `LICENSE` file"* on a Moodle plugin means **read `version.php`**, never
"ungranted".

## 🆕 `p388` — Tier 7: the integration layer, reordered by maintenance rather than by tool count

`p387` dated this shelf and found its richest LMS integration was also its stalest. **This pass found
the replacements**, via a channel nobody here had asked: `registry.npmjs.org/-/v1/search` is open and
**indexes by relevance while reporting publish history**, so "does this exist?" and "is it
maintained?" are answered in one call. 29 education queries → 383 addresses absent from this base →
**22 granted**. Full method in [`repos/trending.md`](trending.md).

| repo | default ref · HEAD | licence | why it is foundational |
|---|---|---|---|
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` · `34e6156` | 🟢 **MIT** (1,070 B) | 🟢 **The maintained teacher/admin Canvas surface, and the new default for an institutional engagement.** 187 tools: grade, comment, rubrics, New Quizzes (LTI), gradebook *history*, enrollments, accounts, analytics, outcomes, grading standards, content exports/migrations, quiz **accommodations**, appointment groups — plus **link audit**, **accessibility audit** and **grade projection**, three deployment modes (stdio, HTTP, library import) and a one-click `.mcpb`. 🟢 **It ships a FERPA mode** — the first time compliance appears as a *product feature* on these shelves rather than a caveat in this base's prose. `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22 (today)**: the most actively published LMS integration here. |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) · [`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server) | `main` · `c7e5725` / `8e424f1` | 🟢 **MIT** (1,091 B, both) | The **student-side** Canvas surface, 209 tools, shipped as a deliberate pair: **Local Edition** (stdio, *no port opened, nothing exposed*) and **Remote Edition** (ngrok, OAuth 2.1, multi-computer failover). Distinctive part is grade *intelligence* rather than grade retrieval: `what_if_grade`, `compute_needed_score`, `grade_impact_ranking`, `study_priority_ranking`, `semester_snapshot`, plus full `.imscc` export. 🔴 Remote Edition opens a **public HTTPS address** — a school's decision, never a default. |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS-side integration on this shelf, and it opens the parent/guardian persona.** 20 tools over **Campus Parent** — schedule, assignments, grades, attendance *events with codes*, behavior, food service, documents, standardized assessment scores, fees, messaging from three sources — with linked districts auto-discovered via **CUPS SSO** and `FeatureDisabled`-awareness so it degrades per district. **47 releases**, → 2026-10-19. 🔵 Every SIS on this shelf until now was a *platform to deploy* (openSIS, i-educar); this is a *surface to read*. |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | The parent-observer scope over Canvas: 18 tools, `canvas_list_observees` as the hinge. 🟢 Download path is hardened in a way worth copying — host-pinned to the Canvas origin, confined to a download directory, never writes through a symlink, new files `0600`. **43 releases**, → 2026-10-16. |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` · `139bb11` | 🟢 **BSD-3-Clause** (1,532 B) | 🟢 **The live replacement for this shelf's most-depended-on stale artefact.** `Pattern B` rested on `pybryt`, last published **2022-04-28**. This is maintained (**v0.3.2, 7 releases, → 2026-09-25**) and from **QuantStack**, a known Jupyter-ecosystem maintainer. Per-cell **Explain Code** sends source, kernel language, **the traceback**, and preceding cells as the exercise statement; the tutor persona lives in a **`TUTOR.md` found by walking up from the notebook**, so it is per-course and version-controlled; `reference_solution` and `evaluation_criteria` ride in cell metadata, **ROT13-encoded** to keep them from the student. |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` · `687c55b` | 🟢 **MIT** (1,070 B) | 🟢 **The North American curriculum-data layer** — the third region to acquire one. 12 tools over the whole **BC Ministry of Education K–12 curriculum** in its real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search, and the **First Peoples Principles of Learning**. Hosted HTTP *or* local stdio. 🟡 2 releases, both **2026-03-27**, and the data is a crawl of `curriculum.gov.bc.ca` — **currency is the risk here, not the licence**. |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` · `3c680e0` | 🟢 **MIT** (1,070 B) | 🟢 **The EMEA institution-shaped integration, and the governance reference on this shelf.** One server spanning **Brightspace + OSIRIS (official records) + MyTimetable + the public Study Guide** behind a single browser sign-in **including MFA**, session self-renewing. 🟢 **Every write action shows a preview and requires confirmation** — the human-oversight control EU high-risk obligations ask for, implemented as the default rather than documented as advice. |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` · `ac0c75f` | 🟢 **MIT** (1,063 B) | Teacher-facing **semester refresh**: reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, emits Canvas-safe HTML. 🟢 The **no-token path is first-class** — generate the HTML, paste it in — so it delivers before anyone grants API access, which is how a pilot actually begins. |
| [gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) | `main` · `7962e49` | 🟡 **GPL-3.0** (284 B short notice) | Node client and CLI for Moodle Core web services **plus the MoodlIA plugin — a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser path. 🔵 A far wider surface than `webservice_mcp`, and GPL is survivable the same way: reached over REST/JSON-RPC, never linked. |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` · `a333415` | 🟢 **MIT** (1,094 B) | 🔵 **Not a teaching tool — a build-cost tool, which is why it is on a foundations shelf.** RAG over a **Moodle codebase** for developers: semantic code search, 7 agents, 9 slash commands, all local. `Pattern A`'s real cost is Moodle plugin work; this is aimed at exactly that. 🟡 v1.0.0, single publish 2025-10-12. |

🔵 **How to read this tier against Tier 1–6.** Those tiers are **systems to deploy**; this one is
**surfaces to read and write**. A studio picks one platform base from Tier 1 and then one integration
row here *per persona* — and the personas are no longer two. Teacher/admin (`bruchris`), student
(`Fireiscoolsolo`), parent/guardian (`chrischall`) are three distinct tool surfaces over the *same*
institutional data, and **the tool counts are scope, not quality**: 187 vs 209 vs 20 reflects who is
being served, not which is better built.

🔴 **The maintenance rule this tier is sorted by, stated so it survives the next pass.** `p387`
established that **recency replaces popularity** here, because no star channel is open. `p388` adds
the corollary: **where two integrations cover the same surface, prefer the one still publishing** —
`canvas-mcp-server` (54 tools, last shipped 2025-06-27) is now dominated on both axes by a 187-tool
server that published today. Tool count and maintenance pointed in opposite directions for one pass;
they no longer do.

🔴 **And a supply category this shelf could not previously name: published-but-unreadable.** Six
addresses from the same sweep **publish to npm from a repository that prompts for credentials** —
the dependency is installable, its provenance is not auditable. The costliest is
[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit) (**103
published versions**, manifest MIT, SCORM support), and the most instructive is
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest reads
**`"SEE LICENSE IN LICENSE"`** — pointing at a file in a repository nobody can read. 🔵 `Pattern L`
clears a repository by reading its subtree; **there is no subtree here to read**, so these cannot be
cleared that way. For an npm-only dependency the rule is: **the manifest is a claim, the tarball is
the evidence** — and `registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves that tarball even when the
repository is closed. Full table and the Santillana case in
[`agents/top.md`](../agents/top.md#-no-licence-file--and-ungranted-is-three-different-things).

## 🆕 `p393` — Tier 8: the 1EdTech standards layer, which is where Python's education supply actually is

`p388` opened Tier 7 with a channel nobody had asked (npm search). This tier exists because `p393`
opened the **other** channel — `pypi.org/simple/`, PEP 691, **920,784 names in 45 MB in 1.4 s** — and
what came back was not more MCP servers but the **interoperability plumbing**: LTI, QTI, OneRoster,
Caliper, Ed-Fi. 🔵 **Read that as a sourcing rule, not a curiosity:** the integration layer is written
in Python and the agent layer is written in TypeScript, so a sweep of one registry answers only half
the question — and this base answered it with npm alone for eleven passes.

| repo | default ref · HEAD | licence (payload) | why it is foundational |
|---|---|---|---|
| 🆕 `p393` [openfun/django-lti-toolbox](https://github.com/openfun/django-lti-toolbox) | 🔴 `master` · `22c6f2f` | 🟢 **MIT** *(1,078 B, `504c17f9869b`)* | **The fourth Python LTI 1.3 implementation**, from **Open FUN — France Université Numérique**, the French state's higher-education platform operator. A Django app for building LTI **Tool Providers**. PyPI v2.0.0, 7 releases, 53 files, **14 ★**. 🔴 **HEAD 2024-11-14 — 707 days.** Granted and architecturally useful; **cold**. Read it for its shape, pick `django-lti` to ship. |
| 🆕 `p393` [Harvard-University-iCommons/django-lti-dynamic-registration](https://github.com/Harvard-University-iCommons/django-lti-dynamic-registration) | `main` · `2873d2f` | 🟢 **MIT** *(1,100 B, `1ade29a33914`)* | **The fifth**, and the only one covering **LTI Dynamic Registration** — the flow that lets a tool be installed in an LMS without a human exchanging keys. An explicit add-on to `academic-innovation/django-lti`, so it **composes with** `Pattern B`'s pick rather than replacing it. 🔴 HEAD **2025-09-15 — 402 days**, 19 commits, **3 ★**: a small, single-purpose, cold component — vendor it and own it. |
| 🆕 `p393` [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) | `main` · `e22fc04` | 🟡 **LGPL-3.0** *(7,652 B, `e3a994d82e64`, at **`LICENSE.LGPL-3.0`**)* | **Writes QTI** assessment packages for **Canvas and Blackboard** from plain question banks — the export half of an assessment pipeline. 381 commits, HEAD **2026-10-12 — 10 d**, PyPI `qti-package-maker` v26.7.14, **4 ★**. 🔴 **This base first published this row as UNGRANTED and was wrong**: a six-name licence-filename probe missed `LICENSE.LGPL-3.0`. Corrected by enumerating the tree. 🟡 **LGPL, so library-linking is fine and modification is not**: use it as a dependency, do not fork it into a product. |
| 🆕 `p393` [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) | `main` · `7a7ec60` | 🔴 **GPL-3.0** *(35,196 B, `f93eb1d94904`)* | **Converts QTI 2.x → 3.0 and 3.0 → 2.1** — items, tests, stimuli and content packages — from **Citolab**, the lab of **Cito, the Dutch national assessment institute**. The migration nobody else here supplies, and QTI 3.0 is the version procurement is starting to demand in EMEA. 🔴 **GPL-3.0: off the permissive shelf.** Run it as a **batch tool at arm's length** (a container invoked by a pipeline), never linked into delivered code. 🔵 Its TypeScript sibling [`Citolab/qti-convert`](https://github.com/Citolab/qti-convert) serves the **byte-identical** payload — so here the grant is **org-shaped, not language-shaped**, the exact complement of `Gap 391-A`'s lesson. |
| 🆕 `p393` `superbuilders/timeback-dev-python` *(🔴 unlinked deliberately — an absent address may not be linked from a live shelf: `gate-dead-citation` I2)* | 🔴 **does not resolve** — 🔵 and `p371`/`p372` already recorded it `NO-REMOTE`; what is new is that it is the declared source of **147 live releases** | 🔴 **UNAUDITABLE — MIT declared on PyPI, no payload obtainable** | The declared source of **three** live PyPI packages — `timeback-qti`, `timeback-oneroster` (OneRoster **v1.2**), `timeback-caliper` — **147 releases** between them, last **2026-07-18**: on paper the most complete 1EdTech client family in Python. 🔴 **The repository does not resolve for an unauthenticated clone, so the MIT claim cannot be checked even in principle.** `Gap 393-B`. 🔵 **The procurement line to say out loud:** a studio may evaluate these in a sandbox; it may not **warrant** them to a client, because warranting a licence means having read it. If the roster/QTI client is needed and granted, build on `oneroster`-shaped code you can read, or ask the publisher to open the repository. |

🔵 **What this tier changes about how this base searches.** `Gap 392-C` was right that the language
bias of a discovery channel becomes a supply claim — and the correction is not "also sweep PyPI once".
It is that **a supply question needs one channel per ecosystem**, and this base can now name its set:
`registry.npmjs.org/-/v1/search` (npm, relevance + publish history), `pypi.org/simple/` (PyPI, the
whole name space), `packagist.org/search.json` (PHP — open, measured by `p392`, **0 shelvable**), and
`raw.githubusercontent.com` + `git ls-remote` for first-hand verification of whatever any of them
returns. 🔴 **Still missing: Maven, NuGet, RubyGems and CRAN** — and `R` matters here, because
`otter-grader` grades R and the statistics-teaching stack is CRAN-shaped.

## 🔴 Dead addresses corrected this pass

Four addresses in common circulation do not resolve. Each has a live replacement:

| dead address | live replacement |
|---|---|
| `apereo/opencast` | [opencast/opencast](https://github.com/opencast/opencast) |
| `edx/openassessment` **and** `openedx/openassessment` | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) |
| `OpenEduCat/OpenEduCat` | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) |

## 🔴 `p384` — an address that resolves but has no tree

[`projectfedena/fedena`](https://github.com/projectfedena/fedena) is listed by a vendor comparison
article as an **Apache-2.0** student information system. It is neither confirmed nor refutable from
a resolution check alone, which is the point:

| check | result |
|---|---|
| `git ls-remote --heads` | 🟢 **resolves** — two refs: `master`, `projectfedena-patch-1` |
| `master/README`, `README.md`, `LICENSE`, `Gemfile`, `app` | 🔴 **404, all five** |

🔵 **`ls-remote` proves a ref, not a tree.** The base's verification method pairs resolution with a
first-hand payload read precisely so this case is caught: there is no readable tree here to carry a
licence, so the Apache-2.0 claim is recorded as **unsubstantiated — nothing read**, not as a
licence of any kind. Any address census built on resolution alone over-counts the supply.

**Still absent from the supply, and it did not change this pass:** no platform is both an **LMS and
a SIS** under a permissive licence. The shape is permissive *courseware*
([`inducer/relate`](https://github.com/inducer/relate),
[`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors)), one permissive *major LMS*
([OpenOLAT](https://github.com/OpenOLAT/OpenOLAT), Apache-2.0), and copyleft everywhere else —
Moodle GPL-3, Open edX AGPL-3, Canvas CE AGPL-3, openSIS GPL-2.0, OpenEduCat LGPL-3. **Pairing two
bases is the only route**; the single permissive LMS+SIS does not exist to be found, and a pitch
that assumes it will be found is a pitch with a hole in it.

🆕 `p386` **— the claim survives a search aimed straight at it, and gains a third route.** The
prescribed ERP/CRM leg (`open source platform education ERP CRM MIT Apache 2026`) returned **no
permissive education platform**, which is this shelf's claim holding up under test rather than for
want of looking. What it did return is three **permissive general ERP/CRM bases**, licence payloads
read first-hand: [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (🟢 **MIT**, 1,077 B,
default ref **`master`**, Laravel 13 + FilamentPHP 5 **with a plugin system**),
[krayin/laravel-crm](https://github.com/krayin/laravel-crm) (🟢 **MIT**, 1,078 B, default ref
**`2.2`**) and [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) (🟢 **Apache-2.0**,
11,906 B, default ref **`trunk`**). 🔵 So the pairing routes are now three, not two: copyleft
LMS + copyleft SIS, copyleft LMS + permissive courseware, or **copyleft LMS + a permissive ERP base
whose education modules you build**. The trade is written out on
[`verticals/solutions.md`](../verticals/solutions.md) — and none of the three bases ships an
education module, so the third route is a **build**, costed as one.
