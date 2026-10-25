---
industry: education
region: Global
updated: 2026-10-25
---

## 🆕 `p425` · 2026-10-25 — **The platform tier gains a row and loses a candidate: `frappe/lms` circulated this week as "100% MIT" and is AGPL-3.0 at its own SHA. 🟢 The procurement rule this forces is a boundary rule — a grant belongs to a REPOSITORY, never to a vendor or to the framework underneath it.**

🔴 **Gates could NOT run on this host.** `make commit-gates` and `make hooks` were both refused by
this host's auto-mode classifier (`[Code from External]`) — reproducing `p422`'s condition exactly
and **not** `p423`'s. 🟢 Per `p423`'s own rule — *a declared-un-run suite must never be read as
un-runnable* — this is recorded as a property of **this host**, not of the suite. The file
contracts below are honoured **by hand**, and that is stated rather than implied (`Gap 425-B`).
🔵 **No date straddle:** every leg, `ls-remote`, SHA read and payload digest happened
**2026-10-25**; the commit lands **2026-10-25**, so `updated:` carries one date.

### 🟢 The platform tier, re-graded where this pass read a payload

| platform | grant | payload read at SHA | customisable with AI on top? |
|---|---|---|---|
| **OpenOLAT** | 🟢 **Apache-2.0** | `LICENSE` `10 982` B `6dbc5b605ed0` @ `d073ad444fe5` *(`p424`)* | 🟢 **Fork and ship.** The one permissive full LMS on these shelves |
| **Sakai** | 🟡 **ECL-2.0** | `LICENSE` **`11 120` B `0688f62d04f1`** @ **`4debc94780cc`** 🆕 re-read this pass | 🟢 Yes — permissive, Apache-derived, education-specific, narrowed `§3` patent scope. 🔴 **Not Apache-2.0** |
| **Frappe LMS** | 🔴 **AGPL-3.0** | `license.txt` **`33 893` B `db1a87ba81e8`** @ **`5d6df8e3ed8e`** 🆕 this pass | 🔴 **Network copyleft.** A hosted AI layer over it is a *conveyance* — price the obligation before the engagement, do not discover it after |
| **Moodle** | 🔴 GPL-3.0 | `COPYING.txt` `35 147` B *(in-tree, `p411`/`p418`)* | 🟡 Plugin-tier work is normal; a forked distribution is a licence event |
| **Open edX** | 🔴 AGPL-3.0 *(platform)* | carried | 🟡 **But `openedx/XBlock` and `openedx/xblock-sdk` are Apache-2.0** (`11 358` B `cfc7749b96f6`) — the **component** boundary is the permissive one |
| **Canvas LMS** | 🔴 AGPL-3.0 | carried | 🟡 As Open edX. 🔴 **`Gap 423-D` still open:** an MCP-census row keyed `canvas` reads **MIT** beside the platform's `canvas lms` → **AGPL-3.0**, and the shorter key matches a platform-worded question first |
| **OpenEduCat** | 🔴 LGPL-3.0 | carried | 🟢 The only one integrating LMS + SIS + fees on one database |
| **forma LMS** | 🔴 GPL-2.0 | `html/license.txt` `18 346` B `4e63feff285d` *(`p424`, after a root-only read published a false absence)* | 🔴 — |
| **RosarioSIS / Gibbon / openSIS / Fedena** | 🔴 GPL family | carried | 🔵 **Seventh channel confirming no education SIS is MIT** |

### 🔴 The boundary rule, written for a client

🔴 This week's claim — *"Frappe LMS is a 100% MIT-licensed LMS by Frappe Technologies, **built on
the Frappe/ERPNext framework**"* — is **true of the framework and false of the product**:

- [`frappe/frappe`](https://github.com/frappe/frappe), the framework → 🟢 **MIT**, `LICENSE`
  **`1 118` B `bc6001a54ffc`** @ `360bcc23bc81`.
- [`frappe/lms`](https://github.com/frappe/lms), the application → 🔴 **AGPL-3.0**, `license.txt`
  **`33 893` B `db1a87ba81e8`** @ `5d6df8e3ed8e`.
- 🟢 **Tree enumerated, not laddered** (`gate-subtree-grant`): **exactly one** licence-shaped path
  in the whole LMS repository, so no MIT subtree exists to rescue the claim.

🟢 **Three rules, and each one has now been paid for on these shelves:**

1. **A grant belongs to a repository at a SHA** — not to a vendor, a product family, or the
   framework underneath. *(This pass: Frappe.)*
2. **Read the payload, over the whole tree.** A root-only ladder is wrong about the repository
   (`p382`); `p424` published a false absence on 14 root `404`s that a path one directory down
   refuted. *(forma LMS.)*
3. **Metadata is a claim, not a grant.** `p423`'s `openemis-mcp` declared MIT on npm, in the MCP
   directory **and in its own `package.json`** while shipping **BSL-1.1** in the installed tarball.

🔵 Taken together these are three *distinct* failure modes — vendor inheritance, incomplete
enumeration, and a lying manifest — and a client's procurement check has to survive all three.

## 🆕 `p424` · 2026-10-24 — **The platform tier's "no permissive grant anywhere" row is WRONG as of this pass, and this file has carried it longest. 🟢 `OpenOLAT` is Apache-2.0 at its own SHA — a full LMS a studio may fork and ship. 🔴 And the Apache-2.0 claim about `forma LMS` turns out to have been read off a WEB-SERVER REQUIREMENT.**

🟢 Gates first against `p423`'s `3009a89`: **54 / 55**, one declared red, `commit-gates` → `0`.
🔵 Every read **2026-10-24**. 🟡 `Gap 424-A` declares two pre-suite orientation legs.

### 🟢 The tier picture, with the row that has been wrong since `Gap 298` was opened

| tier | what these shelves graded it | `p424` |
|---|---|---|
| education **platforms** (LMS / SIS / MIS) | 🔴 *"no permissive grant anywhere"* — `Gap 298`, re-confirmed on a ninth channel by `p423` | 🟢 **REFUTED.** `OpenOLAT/OpenOLAT` is **Apache-2.0**, `10 982` B `6dbc5b605ed0` @ `d073ad444fe5`. 🔵 The distributional claim survives: **8 of 9** graded platforms remain copyleft |
| platform **extension points** | 🟢 permissive — `openedx/XBlock` + `openedx/xblock-sdk`, Apache-2.0, `11 358` B `cfc7749b96f6` | 🔵 unchanged — and no longer the *only* permissive thing on this file |
| **LMS** agent layer (MCP over the LMS) | 🟢 9 of 10 MIT at their own SHAs (`p422`, `T114`) | 🟢 extended off the Canvas family: `duck-5/moodle-mcp`, MIT, `1 072` B `64dc9680d3bb` |
| **SIS / MIS** agent layer | 🔴 first address read at a SHA is `BSL-1.1` (`p423`, `T118`) | 🔵 unchanged — no new SIS address this pass |

### 🟢 `OpenOLAT`, graded — what a studio may actually do with it

🔵 **What it is:** a full university LMS — course management, assessment, portfolio, video — that
began as **OLAT** at the **University of Zurich** and is maintained by **frentix GmbH**
(Switzerland, 🟢 **EMEA**). **31** heads, tags through `OpenOlat_20.0.pre2`.

🟢 **What the grant permits that no other platform on this file permits:** fork it, modify it,
host it, and ship the result commercially **with no distribution obligation and no network-use
trigger**. 🔴 On Moodle or Open edX the same work is a release trigger — which is the entire
reason `Pattern AT` exists (*do not fork the LMS — talk to it*). 🟢 **`OpenOLAT` is the one
platform where forking is an available strategy rather than a licence event**, and
[`compose/patterns.md`](../compose/patterns.md) carries that as `Pattern AV` this pass.

🟡 **The honest caveat.** This pass graded the **grant** and did not re-measure release cadence or
community size, so nothing here says `OpenOLAT` is the *best* platform for a given client — only
that it is the one whose licence does not constrain the commercial shape of the engagement.
`ACTION p424-A`.

### 🔴 `forma LMS` — the claim `p422` refused, now explained rather than merely refused

🟢 `p422` declined to write *"forma LMS is Apache-2.0"* because the serving channel disclosed its
own conflict. 🟢 **Resolved first-hand this pass: it is `GPL-2.0`**, payload at
**`html/license.txt`**, **`18 346` B `4e63feff285d`** @ `446a77a9b9cb`. The channel's own
hedge — *"other sources grade it `GPL` or `LGPL`"* — lands on `GPL`.

🔴 **And this pass got there the wrong way first, which is worth more than the grade.** `p424`
ran a **root-only** ladder (14 paths, 14 × `404`) and wrote *"no grant payload"* into four files.
`gate-enumeration` refuted it on the post-write run by naming `html/license.txt`. 🟢 That is
`p382`'s `gate-subtree-grant` rule — *a root-only read is wrong about the repository* — which
this base **already held**. 🔵 `T123`; `Gap 424-C`.

🟡 **The Apache string in that README is still only this:**

> `- Apache (recommended) with mod_rewrite enabled`

🔵 A web-server requirement, and the most plausible origin of the circulating claim — but an
**inference about transmission**, not a finding about the grant. 🟢 The operational rule stands
either way: a licence claim supported only by a string match on a licence *name* is worth
nothing, because `Apache`, `MIT` and `BSD` are also the names of servers, universities and
operating systems. **Grade the payload — at every path, not just the root.**

## 🆕 `p423` · 2026-10-24 — **The SIS tier gets its first MCP address and it is NOT permissive: `tixuz/openemis-mcp` over UNESCO's OpenEMIS is Business Source License 1.1 at its own SHA, under an MIT manifest and an MIT npm entry. 🔵 So `p422`'s "the agent layer is the permissive arm" holds for LMS and is UNTESTED-TO-FALSE for SIS, on one address.**

🟢 Gates first against `p422`'s `82235af`: **47 / 53**, 1 deliberate red, 5 new, all five fixed
this pass. 🔵 Every read **2026-10-24**. 🔵 **No platform row is added or changed** — the vertical
leg returned **8 platforms, 8 already shelved, 0 unshelved**, a third consecutive pass of zero
unshelved platforms.

### 🔴 The tier picture, corrected where this pass could correct it

| tier | what these shelves grade it | p423 |
|---|---|---|
| education **platforms** (LMS / SIS / MIS) | 🔴 **no permissive grant anywhere** — `Gap 298`, confirmed on an eighth channel by `p421` | 🔵 unchanged; the leg returned Moodle, Open edX, Canvas LMS, Sakai, OpenEduCat, Chamilo, ILIAS and OpenEduCat again, all carried |
| platform **extension points** | 🟢 **permissive** — `openedx/XBlock` + `openedx/xblock-sdk`, Apache-2.0, `11 358` B `cfc7749b96f6` | 🔵 unchanged, and still the most useful boundary this base has on `Gap 298` |
| **LMS** agent layer (MCP over the LMS) | 🟢 **9 of 10 MIT** at their own SHAs (`p422`, `T114`) | 🔵 unchanged |
| **SIS / MIS** agent layer | 🆕 **first address read at a SHA, and it is `BSL-1.1`** | 🔴 `T118` — one address, so a **boundary on `T114`**, not a refutation of it |

🔴 **`OpenEMIS` is now graded on both tiers and neither is permissive.** The platform,
[`OpenEMIS/core`](https://github.com/OpenEMIS/core), these shelves already carry as
**GPL-2.0** — the payload that proved `P572`. The agent above it,
[`tixuz/openemis-mcp`](https://github.com/tixuz/openemis-mcp), is **BSL-1.1** (`647` B
`4dead97d8aaf` at `LICENSE.md` @ `f88a80fc1d5b`), with `Licensed Work: openemis-mcp-pro`, an
Additional Use Grant of *non-production evaluation and internal testing only*, and
`Change Date: 2029-01-01`. 🔵 OpenEMIS is UNESCO/KORDIT's school MIS and is deployed by
ministries, which makes it exactly the platform a public-sector education engagement meets — and
the only agent surface over it that this base can find is unusable commercially for three years.

🔴 **What a studio must not do with it:** take the MIT badge from the npm page or the MCP
directory. Both say MIT. So does `package.json`, in the same tree at the same SHA. The only
licence payload in the repository is the BSL, the rest of the ladder is `404`, and the **published
npm tarball ships that same 647-byte BSL file** beside the MIT manifest. `Gap 423-A`.

🟢 **What a studio CAN do:** build the SIS agent surface itself, against `OpenEMIS/core`'s
GPL-2.0 boundary, copying the **architecture** rather than the code — see `Pattern AU` in
[`compose/patterns.md`](../compose/patterns.md), which uses the LMS tier's MIT exemplars as the
design to clone and keeps the copyleft platform behind a process boundary.

🟢 **One repair on this file this pass, unrelated to the SIS tier.** `RohanMuppa/brightspace-mcp-server`
was cited here in lower case while `agents/top.md` and `repos/foundations.md` carried it in upper
case — one repository, two spellings, three shelves. Found by `p439-case-collision-gate` on the
pass that **wired** it (it had been in no `make` target since `p439`), resolved by that gate's own
channel 2 at SHA `4b3bc9bf3838`, and normalised. `T120`.

## 🆕 `p422` · 2026-10-24 — **The vertical leg returned ZERO unshelved platforms for a second consecutive pass — and it also returned two Apache-2.0 claims this file must NOT accept, because both conflict with grades already on these shelves. 🟢 The real vertical movement is one layer up: the agent-facing tier over these platforms is MIT, 9 of 9.**

🔴 **Gates did NOT run this pass** — `make hooks` executes code from this cloned repository and the
host's auto-mode classifier refused it (`[Code from External]`), the same refusal `p419` recorded.
🟢 `p412`'s standing rule is therefore **unmet and declared**, not skipped silently; every file
contract below was honoured by hand. `Gap 422-A` registers the un-run suite, second instance.
🔵 **No date straddle:** every leg, `ls-remote`, SHA read and digest ran **2026-10-24**; the commit
lands **2026-10-24**, so `updated:` carries one date.

### 🔴 Two licence claims from the vertical leg, REFUSED rather than written

🟢 **`p289`'s rule is the operative one: a licence claim from a comparison blog is not a grade.**
The leg `open source platform education LMS SIS MIT Apache self-hosted 2026` served two
permissive claims, and **neither is written into a cell this pass:**

| claim served | why it is refused | what this file already holds |
|---|---|---|
| 🟡 **OpenOlat is Apache-2.0** | 🔵 Plausible and **consistent with a mention this base already carries** in `compose/patterns.md` — but **no payload was read at a SHA this pass**, and `p289` forbids promoting an unread grade into a graded cell | Carried as a mention, not as a graded row. 🟢 Left exactly as it was |
| 🔴 **forma LMS is Apache-2.0** | 🔴 **The serving channel itself reported that other sources grade it `GPL` or `LGPL`** — a conflict disclosed at the point of service. Writing either value would be picking a side unread | No graded row. 🟢 Registered as conflicted, resolved by neither |

🔵 **`ACTION p422-A`** — resolve `OpenOLAT/OpenOLAT`'s grant first-hand at its SHA with `p230`'s
ladder, and grade `formalms/formalms` or record it as unreachable. 🟢 Both are one `ls-remote` and
one `raw.githubusercontent.com` read away on the channel `p422` used all pass; neither was spent
here because the pass's measurement budget went to the MCP tier.

### 🟢 The platform tier, re-stated — because the contrast with the new tier is the finding

🔵 Carried from these shelves, each graded at a SHA by an earlier pass. **Nothing below is new**,
and it is restated only so the two-tier contrast reads in one place:

| platform | grant | note |
|---|---|---|
| **Moodle** | 🔴 `GPL-3.0` | 🔵 Grant path varies by ref — root `COPYING.txt` on `main`, `lang/en/docs/licence.html` on the `MOODLE_*_STABLE` refs (`p420`) |
| **Open edX** (`openedx/edx-platform`) | 🔴 `AGPL-3.0`, narrowed (`p413`) | 🟢 But its component `openedx/XBlock` is **Apache-2.0**, `11 358` B `cfc7749b96f6` @ `c73c4bb` (`p421`) — **the extension point is permissive even though the host is not** |
| **Canvas LMS** | 🔴 `AGPL-3.0` | 🟢 The platform with the deepest MCP tier above it, by a wide margin |
| **Sakai** | 🔴 `ECL-2.0`, `11 120` B `0688f62d04f1` @ `c35e7a2` (`p421`) | 🔵 Apache-derived but **not** Apache-2.0 |
| **OpenEduCat** | 🔴 `LGPL-3.0` | 🔵 The Odoo-based education ERP; the closest thing in this sector to the "Odoo for ERP" shape |
| **`frappe/lms`** | 🔴 `AGPL-3.0-or-later`, grant at lowercase `license.txt` | 🔵 `package.json` agrees (`p420`) |
| **RosarioSIS · Gibbon · Chamilo · ILIAS** | 🔴 `GPL` family | 🔵 All carried; none moved this pass |

🔴 **Not one permissive grant in the platform tier.** 🟢 **Nine of nine in the tier directly above
it.** That is the whole commercial shape of this sector's licensing, and `p422` is the first pass
that can state both halves from measurement.

### 🟢 What this changes about how a vertical engagement is scoped

- 🟢 **The customisation surface a client buys is the MCP/agent layer, and it is MIT.** Scope it as
  deliverable IP; it is not a derivative work of the AGPL host it talks to.
- 🔴 **The platform itself stays the client's.** Fork it and the engagement acquires a
  distribution obligation — network use included, under AGPL. 🔵 Open edX is the one place where a
  permissive *extension point* exists inside a copyleft host (`openedx/XBlock`, Apache-2.0).
- 🟡 **The SIS tier is GPL across the board and has no measured agent layer at all.** 🔵 Stated as
  an informed gap, not as coverage: this pass found **no** MCP or agent surface over RosarioSIS,
  Gibbon or openSIS, where Canvas alone has at least seven.

## 🆕 `p421` · 2026-10-24 — **`ACTION p420-E` resolved first-hand: Sakai is `ECL-2.0` and NOT Apache-2.0, and the Apache-2.0 Open edX component is real — `openedx/XBlock`. 🔴 Both answers were already on these shelves when the action was written. 🟡 And this file grades Sakai on a row that carries no address, which refuted the obvious fix for `p421`'s new gate.**

🔵 **No date straddle:** every payload read, SHA resolution and digest ran **2026-10-24**; the
commit lands **2026-10-24**. 🟢 **Gates ran FIRST** (`p412`): **51 / 52**, single red `Gap 400-B`.

### 🟢 The platform licence question, resolved at the commit SHA

| platform | address | licence *(read at SHA `T106`, 2026-10-24)* | what changes for an engagement |
|---|---|---|---|
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** — `LICENSE`, `11 120` B, `sha256₁₂ 0688f62d04f1`, SHA `c35e7a2`, ref `master` | 🔴 **Not Apache-2.0.** ECL-2.0 is an Apache-2.0 **derivative** drafted for academic redistribution; the text names *"Apache 2.0 license"* in lower case and contains **zero** occurrences of `Apache License`, which is why `compose/code/p1040-ecl-corpus-census` exists at all. 🟢 Permissive in practice, **its own licence** in a compliance review |
| **Open edX** *(platform)* | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0**, narrowed — as `p413` established | Unchanged |
| **Open edX** *(component API)* | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** — `LICENSE.TXT`, `11 358` B, `cfc7749b96f6`, SHA `c73c4bb` | 🟢 **This is the answer `ACTION p420-E` wanted.** The API a plugin imports is permissive even though the host is not |
| **Open edX** *(dev harness)* | [`openedx/xblock-sdk`](https://github.com/openedx/xblock-sdk) | 🟢 **Apache-2.0** — `LICENSE.TXT`, `11 358` B, **`cfc7749b96f6`**, SHA `e61f9d2` | 🟢 Build and run an XBlock **without** standing up `edx-platform`. Byte-identical grant |
| **Open edX** *(deployment)* | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** — `LICENSE.txt`, `34 523` B, `0d96a4ff68ad`, SHA `279f774`, ref **`release`** | 🔵 The official installer is **copyleft**, and its default ref is `release` — neither `main` nor `master`, which a root-and-default read gets wrong |
| **Open edX** *(MFE)* | [`openedx/frontend-app-learning`](https://github.com/openedx/frontend-app-learning) | 🔴 **AGPL-3.0** — `LICENSE`, `34 523` B, `8486a10c4393`, SHA `50faa45` | 🔵 Same byte count as Tutor's grant, **different digest** — a new `T101` band |

🔴 **The consequence for a studio, stated plainly and bounded.** The permissive cell is the
**component API**, not the platform, not the installer and not the front end. 🟢 A plugin built
against `XBlock` + `xblock-sdk` imports Apache-2.0 code. 🔴 **What a deployment alongside an
AGPL-3.0 host obliges is a question for counsel, not for this base** — `p421` measured grants, and
says so rather than implying more.

### 🟡 This shelf grades Sakai with no address, and that refuted a fix

🔵 Measured while closing a hole in `p421`'s new `gate-action-answered`: the platform vocabulary it
derives from **this file** was going to be closed on *"a platform this base recommends has an
address."* 🔴 **That closure drops `sakai` — the specimen's own subject** — because the row grading
it `ECL-2.0` carries **no `github.com/…` slug at all**; the address lives on
`repos/foundations.md` instead. 🟢 **A cross-shelf split, not a missing address**, and a closure
that deletes the specimen is worse than the hole it closes, so the hole is pinned OPEN as a fixture
(`p364`'s disposition) rather than guessed at.

### 🟢 `Gap 298` / `Gap 405-A` confirmed on an EIGHTH channel — and qualified

🔵 This pass's vertical leg returned Moodle, Open edX, Canvas, Sakai, OpenOLAT, Chamilo, ILIAS,
Forma LMS, OpenEduCat, RosarioSIS, Gibbon and Open LMS. 🟢 **No permissive platform that was not
already carried** — OpenOLAT (Apache-2.0) is the only one, shelved since earlier passes, and the
leg's own sources disagree about Open edX's licence (one lists Apache-2.0 against the AGPL
majority, which is what produced `ACTION p420-E`). 🔴 **RosarioSIS and Gibbon are GPL; the leg found
no MIT or Apache SIS**, an eighth independent confirmation.

🟢 **The qualification this gap has been missing:** *the platform* is copyleft and *the extension
point* is permissive, and reading only the platform cell gives an engagement the opposite answer.

## 🆕 `p420` · 2026-10-24 — **Moodle's grant MOVES with its ref: root `COPYING.txt` on `main`, `lang/en/docs/licence.html` on `MOODLE_13/14/15_STABLE`. 🔴 An engagement that pins a Moodle LTS ref and reads the root path concludes the world's most-deployed LMS is unlicensed.**

🔵 Every probe below is first-hand on **2026-10-24** against a ref `git ls-remote` resolved.

### 🔴 `T104` — the grant's PATH is a function of the REF, measured on one platform across its own history

| platform | ref | root licence path | verdict |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | 🟢 **`COPYING.txt` → `200`** (`LICENSE`, `license.txt`, `COPYING` all `404`) | 🟢 **GPL-3.0, granted at root** |
| `moodle/moodle` | `MOODLE_13_STABLE` | 🔴 **nothing at 25 root paths** | 🟢 **GPL — grant at `lang/en/docs/licence.html` → `200`** |
| `moodle/moodle` | `MOODLE_14_STABLE` | 🔴 **nothing at 25 root paths** | 🟢 **GPL — `lang/en/docs/licence.html` → `200`** |
| `moodle/moodle` | `MOODLE_15_STABLE` | 🔴 **nothing at 25 root paths**, and **no GPL boilerplate in `version.php`** | 🟢 **GPL — `lang/en/docs/licence.html` → `200`** |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `1.9.x` / `1.10.x` | 🔴 `LICENSE` → `404` | 🟢 **GPL-3.0 at lowercase `license.txt`**; `1.10.x` `composer.json` agrees, and `index.php` carries the pointer *"For licensing terms, see /license.txt"* |

🔴 **This is strictly past `p418` and `p419`.** `p418` established that a grant has **subtrees**;
`p419` that it has **branches**; this pass measures that **the path itself migrates across a
project's history**. 🟢 **So the enumeration unit is `(ref, TREE)` — not `(ref, path)`, which is what
`ACTION p419-A` prescribes** and which would have graded three LTS refs of a GPL project ungranted.

🟡 **The procurement consequence is concrete and it is not abstract pedantry.** Education engagements
pin LTS refs — that is the whole point of a Moodle `_STABLE` branch. 🟢 **The grant is there on every
one of them;** a studio must read the tree, not a root ladder, before telling a client what it owes.

### 🟢 The vertical shelf, re-confirmed rather than re-bought

🔵 This pass's vertical leg (*"open source platform education LMS SIS ERP MIT Apache 2026"*) returned
**Moodle** (GPL-3.0), **Open edX** (AGPL-3.0, with sources disagreeing about Apache-2.0 for some
components), **Canvas LMS** (AGPL-3.0 community edition), **Sakai** (ECL-2.0 per most sources,
Apache-2.0 per one), **OpenOLAT** (Apache-2.0), **Chamilo** (GPL-3.0), **OpenEduCat** (LGPL-3.0),
**RosarioSIS** (GPL), **openSIS** (GPL), **Open LMS** (a managed Moodle service, not a separate
project). 🔴 **Every one already carried.** 🟢 **`Gap 298` / `Gap 405-A` confirmed on a seventh
independent channel: no major education SIS or LMS carries a permissive grant**, and the one
Apache-2.0 LMS on the list — **OpenOLAT** — is the exception this base already shelves.

🔴 **A licence claim this pass refused to carry forward.** Two sources in the vertical leg assert
**Apache-2.0** for Open edX components and **Apache-2.0** for Sakai, against **AGPL-3.0** and
**ECL-2.0** in the majority. 🟡 **Neither was resolved first-hand this pass** and neither is written
into a cell: band `reported`, and `p289`'s rule applies — a restatement of an unreachable authority
is not a verified grant. 🔵 Registered as the cheapest vertical probe available to a successor.

## 🆕 `p419` · 2026-10-24 — **A self-hostable platform can be MIT and still leave the two components a deployment needs UNGRANTED, because the grant sits on one branch of three. 🔴 `piyushdhoka/GradeU` is the specimen, and the teacher studio and admin portal are the ungranted two.**

🔴 **Gates did not run** — `make hooks` runs code from this cloned repository and the host's
auto-mode classifier refused it (`[Code from External]`). Contracts honoured by hand;
`Gap 419-D` registers the un-run suite.

### 🔴 `piyushdhoka/GradeU` — admitted with its boundary priced, not with its badge

| field | measured 2026-10-24 |
|---|---|
| address | [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU) |
| default ref | **`main`** — 🔴 **there is no `master` branch**, and `raw…/master/LICENSE` nonetheless returns `200` (see below) |
| HEAD | `4ab0011` **2026-10-23T19:34:19+05:30 · 1 d** |
| licence | 🟢 **MIT on `main`** — `1 065` B, `sha256₁₂ 10e6b9c80b1b`, *"Copyright (c) 2026 GradeU"*. 🔴 **`teacher` and `admin`: no licence-shaped path at any depth, no manifest `license` field** |
| stack | Next.js 16 · React 19 · Supabase (Postgres / Auth / Storage) · Upstash Redis · MongoDB via `mongoose` *(mid-migration)* · `@tensorflow-models/blazeface` |
| inference | Groq, model `openai/gpt-oss-120b`, raw `fetch` to `https://api.groq.com/openai/v1/chat/completions`, key `GROQ_API_KEY` — 🔴 **no AI SDK in `package.json`** |
| scale signals | 3 ★ · 1 fork · 86 commits · root `d7b19e6` 2026-02-02 · **four humans + one bot** (`p412` identity rule) · `"version": "0.0.0"` |

🔴 **What a deployment actually gets, per branch.** The project ships **one application per branch**,
stated in its own `README.md:50-54`:

| branch | app | who it serves | tracked paths | grant |
|---|---|---|---|---|
| `main` | Student site — Next.js 16 / React 19 | learners | 199 | 🟢 **MIT** |
| `teacher` | Teacher studio — Next.js 16 + BullMQ worker | teachers | 55 | 🔴 **UNGRANTED** |
| `admin` | Admin portal — Vite + React 18 | platform admins | 43 | 🔴 **UNGRANTED** |

🟢 **All three heads were committed within eight minutes** on 2026-10-23, so none is dormant, and
the three manifests carry **different project names** (`grade-u`, `course-app-next`,
`vois-admin-portal`) with `"private": true` and no `license` field on any of them. 🔴 **So the MIT
payload on `main` is the only grant channel in the repository, and it reaches one app of three.**

🔴 **The practical consequence for a studio engagement.** A platform is chosen for the *tenant-admin
and author-side* workflows at least as often as for the learner view. Here those two are the
ungranted ones: **a teacher-studio or admin-portal deployment has no licence at all**, while the
badge, the sidebar and a default-branch licence read all say MIT. 🟢 **The remedy is a question, not
a workaround:** ask the maintainers to extend `LICENSE` to `teacher` and `admin` — four humans, an
active week, and a repository that already chose MIT once.

🔵 **Where it sits against this file's existing rows.** It is **not** a Moodle / Open edX / Kolibri
substitute and is not offered as one: 3 ★, `"version": "0.0.0"`, one semester of history. 🟢 **What
it genuinely supplies that the copyleft platforms do not** is a *permissively granted, readable*
reference for in-browser proctoring and syllabus-to-course generation — on `main`, which is the
licensed branch.

### 🔴 The channel note this file needs, because it publishes `(ref, path)` grant cells

🟢 **`raw.githubusercontent.com` serves `master` and `HEAD` as ALIASES for the default branch even
when no such ref exists.** Measured on three repositories today, with negative controls: `trunk`
and `develop` → `404`, a bogus ref → `404`. 🔴 **A `200` at `…/master/LICENSE` therefore proves the
file and says NOTHING about the branch** — `p354`'s `gate-grant-path` contract is unfalsifiable
there for the two most-assumed ref names.

🟢 **This file's own ref claims were swept against `git ls-remote` and they hold:**
[`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) ``master`` ✓ (HEAD `e935dec`),
[`Loganxgreaves/blackboard-mcp`](https://github.com/Loganxgreaves/blackboard-mcp) ``master`` ✓
(`c2629ae`), [`lukecarroll15/blackboard-mcp`](https://github.com/lukecarroll15/blackboard-mcp)
``tcd`` ✓ (`1aeb80b`), [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic)
``master`` ✓ (`5d546f2`), [`learningequality/kolibri`](https://github.com/learningequality/kolibri)
``develop`` ✓ (`44a4e68` — and 🟢 **it has neither `master` nor `main`**, so this file's `develop`
cell is the only correct way to cite it). 🔵 **18 of 18 across all six shelves.**

### 🔴 The vertical-platform leg — a SIXTH channel on the same scarcity

🟢 Returned Forma LMS (Apache-2.0), OpenOLAT (Apache-2.0), Open edX (AGPL-3.0), Sakai (ECL-2.0),
Moodle (GPL), Canvas (AGPL), RosarioSIS (GPL), OpenEduCat, openSIS, SchoolTool — **every one
carried**. 🔴 **Sixth independent confirmation that no major education system of record is
permissively granted** (`Gap 298` / `Gap 405-A`). 🔵 The honest shape of this file is unchanged:
**the system of record is copyleft, the permissive layer is what you bolt onto it.**

## 🆕 `p418` · 2026-10-24 — **The permissive ERP row `p417` refused is REAL — it was the slug and the ref that were wrong, and the right ones were already on this base. 🔴 Plus: the Webkul pair is one vendor, but it is NOT one payload.**

### 🟢 `aureuserp/aureuserp` admitted — `Gap 417-E` closed, `ACTION p417-C` discharged

| field | measured 2026-10-24 |
|---|---|
| address | [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) 🔴 **not** `aureus-erp/aureus` |
| default ref | **`master`** 🔴 `p417` probed `main` → `404` |
| HEAD | `8f6e107`, **2026-10-23T18:06+05:30** — live, one day old |
| grant | 🟢 **MIT**, `LICENSE`, `1 077` B, `sha256₁₂ c6dca3b0db5b`, *"Copyright 2010-2025, Webkul Software"* |
| shape | Laravel: `composer.json`, `package.json`, `artisan`, `phpunit.xml`, `Dockerfile`/`docker-compose.yml`, `plugins/`, `database/`, `lang/`, `.scribe` (API docs) |

🔴 **`p417` registered `Gap 417-E` and prescribed a probe for a question this base had already
answered** — `agents/top.md:2330` carries the correct slug with its MIT grant, and
`agents/trending.md:26550` carries it again. 🔵 `p416`'s standing suggestion is *"`grep -rF` the band
a pass claims is empty"*; two `grep` calls would have closed this without a network probe.

### 🔴 One vendor, two payloads — the Webkul pair re-measured

| address | ref · HEAD | bytes | `sha256₁₂` |
|---|---|---|---|
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | `2.2` · `5eecae0` (2026-10-21) | `1 078` | `a76aa4a4405c` |
| [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) | `master` · `8f6e107` (2026-10-23) | `1 077` | `c6dca3b0db5b` |

🟢 **Same holder, same text, different bytes** — `aureuserp` has no terminal newline.
🟢 **The procurement conclusion is unchanged and still load-bearing:** these are **one vendor**
(Webkul Software), so choosing both is not diversification. 🔴 **`P564`'s stated basis —
*"byte-identical 1 077 B"* — is refuted**, and `p417` itself published krayin's correct `1 078` B.

### 🟢 `exelearning` placed on this shelf properly: a SCORM-emitting authoring tool, AGPL-3.0

🟢 `ACTION p417-B` discharged in-tree (HEAD `c848eca`, **9 756** paths, **774** matching `/scorm/i`):
**SCORM 1.2 runtime** (`exe-scorm12-adapter.js`, `SCORM_API_wrapper.js`), a **SCORM 2004** contract
suite, the generator `src/shared/export/generators/ImsManifest.ts`, and export fixtures in **two**
packaging profiles — `imscp_rootv1p1p2.xsd` (SCORM 1.2 CP) and `imscp_v1p1.xsd` (plain IMS CP).
🔴 **xAPI is retired by decision record** (`ADR-2302-02-xapi-retirement.md`), so a proposal must not
offer xAPI from this component.
🔴 **AGPL-3.0 decides the commercial model**, and that is the whole caveat: a *hosted* service built
on `exelearning` triggers §13 network copyleft. 🟢 For a **desktop/offline authoring** deployment, or
one where the studio publishes its modifications, it is the strongest state-backed authoring tool on
this shelf (Spain's MEFPD via Cedec-INTEF).

### 🔵 The vertical platform table, re-stated with what each one is for

| platform | grant | layer | AI-on-top verdict |
|---|---|---|---|
| [Moodle](https://github.com/moodle/moodle) | GPL-3.0 | LMS | 🟢 the default LMS target; MCP servers carried on `agents/top.md` |
| [Open edX](https://github.com/openedx/edx-platform) | AGPL-3.0 🔴 **narrowed grant** (`p413`) | LMS / MOOC | 🟡 read the narrowing before a hosted build |
| [`exelearning/exelearning`](https://github.com/exelearning/exelearning) | AGPL-3.0 | **authoring → SCORM** | 🟢 strongest OER authoring; 🔴 §13 on hosting |
| [Kolibri](https://github.com/learningequality/kolibri) | MIT | offline-first learning | 🟢 the permissive choice for low-connectivity LATAM / Africa deployments |
| [OpenEduCat](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | education ERP | 🟡 copyleft, Odoo-based |
| [RosarioSIS](https://gitlab.com/francoisjacquet/rosariosis) | GPL-2.0 | K-12 SIS | 🟡 copyleft |
| [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 *(grant at `docs/License.txt`)* | K-12 SIS | 🟡 copyleft; 🔵 the path that broke a root-only probe at `p384` |
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | MIT | school management | 🔴 **open-core** (premium modules withheld), HEAD 120 d stale, manifest is the unedited Laravel skeleton |
| 🆕 [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) | 🟢 **MIT** | generic ERP | 🟢 permissive admissions/finance substrate; 🔴 **no academic model**, same vendor as Krayin |
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🟢 **MIT** | generic CRM | 🟢 permissive admissions CRM; 🔴 0 education terms in its README |
| [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | virtual classroom | 🟡 copyleft, library-scoped |
| [H5P](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** | interactive content | 🔴 **SCORM export runs through the separate `Lumi` DESKTOP app** (`p417`) — not a server-side pipeline. 🔴 🆕 `p418` **This row said MIT in its first draft and `gate-shelf-consistency` refused it** — four cells on these shelves said GPL-3.0 and they are right: `LICENSE.txt` read first-hand today = **`35 146` B, `sha256₁₂ c53a65c2fd56`, *"GNU GENERAL PUBLIC LICENSE, Version 3"***. 🔵 **And it carries a SECOND grant** — `fonts/inter/LICENSE.txt` (`4 380` B, `262481e84452`, Inter Project Authors), a third live instance of `Pattern AJ` Amendment 8 |

🟢 **The standing recommendation for an admissions build is unchanged**: no major education SIS is
permissive (`Gap 298`, now confirmed from a **fifth** channel), so graft **`aureuserp` or `krayin`
(MIT)** onto the academic model rather than forking a GPL/AGPL SIS — and remember they are the
**same vendor**.

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

### 🟢 A state-backed authoring platform joins the vertical stack — and it is AGPL, which changes where it sits

🟢 [`exelearning/exelearning`](https://github.com/exelearning/exelearning) is the first **publicly
governed** authoring platform on this shelf: **AGPL-3.0**, **150★**, **1 413 commits**, maintained by
**Spain's Ministry of Education, Vocational Training and Sports (MEFPD)** through **Cedec-INTEF** with
regional administrations participating, after originating in New Zealand and going state-led in
**2010**.

| layer | platform | grant | where it sits |
|---|---|---|---|
| **LMS / system of record** | Moodle | GPL-3.0 | 🟢 carried — the 0%-decay tier (`T83`) |
| | Open edX | AGPL-3.0 | 🟢 carried — grant **NARROWED**, see `Gap 413-B` |
| | OpenOlat | Apache-2.0 | 🟢 carried — the permissive LMS option |
| | Kolibri | MIT | 🟢 carried — permissive, offline-first |
| **SIS / ERP** | OpenEduCat · OpenSIS · Fedena · RosarioSIS · Gibbon · SchoolTool | LGPL-3.0 · GPL-2.0 · Apache-2.0 · GPL · GPL-3.0 · GPL-2.0 | 🔴 `Gap 298` — **no major education SIS is MIT**; integrate, do not fork |
| 🆕 **authoring / OER** | **`exelearning/exelearning`** | 🟡 **AGPL-3.0** | 🟢 **new** — state-backed, collaborative editing, Moodle export |
| | Adapt | GPL-3.0 | 🟢 carried — emits SCORM 1.2 + 2004 |
| | H5P | MIT | 🟢 carried — 🔴 **but see the split below** |
| **SCORM runtime** | `scormflow/scorm-engine` | MIT | 🟢 carried — LRS, xAPI, cmi5; **runtime, not authoring** |

🔴 **Why the AGPL cell is a placement decision, not a footnote.** An authoring tool is normally
offered to a client **as a hosted service**, and that is exactly the deployment AGPL's network clause
reaches. 🟢 **`exelearning` is therefore fine to deploy for a client on the client's own
infrastructure, and a trap to wrap into a studio-hosted multi-tenant product** without counsel.
🔵 Where a client refuses copyleft at this layer, the permissive answer on this shelf is still
**H5P (MIT)** plus a separate emitter — with the caveat below.

### 🔴 The H5P / Lumi split — a real integration defect this shelf had not stated

🔴 The authoring leg reported `H5P` as *"MIT, fully free for self-hosted use"* and, in the same
breath, that **SCORM export goes through a separate desktop tool, `Lumi` Desktop**. 🟢 Both halves are
carried on these shelves (192 and 95 hits) — 🔴 **but never as a dependency.** A proposal that prices
"H5P, MIT, SCORM export" is pricing **two** products, one of which is a **desktop application** and
therefore not part of a server-side pipeline at all.

🟢 **The correction for a studio:** H5P is an **in-LMS interactive content** layer, not a SCORM
packaging step. For SCORM packaging, the readable permissive producer on these shelves is `Papermorph`
(MIT, `p416`), and the runtime is `scorm-engine` (MIT). 🔵 `exelearning`'s own SCORM capability is
**unverified** — the repository page names Moodle export and *"various formats"* and does **not**
mention SCORM (`ACTION p417-B`).

### 🟢 Permissive general ERP/CRM as the admissions-and-enrolment path, with payloads read

🔵 `Gap 298` says no education SIS is MIT. 🟢 **The prescribed ERP/CRM leg returned the other half of
that answer** — permissive *general* platforms that can carry admissions, enrolment and student-CRM
workflows without forking a copyleft SIS. Grants read byte-level this pass:

| platform | grant, measured | note |
|---|---|---|
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🟢 **MIT** — `master/LICENSE`, **`1 078` B**, `sha256:a76aa4a4405c`, *"Copyright 2010-2025, Webkul Software"* | 🟢 carried (65 files). Laravel; a candidate admissions CRM. 🔵 One leg calls its UI *"clunky"* |
| [`marmelab/atomic-crm`](https://github.com/marmelab/atomic-crm) | 🟢 **MIT** — `main/LICENSE.md`, **`1 105` B**, `sha256:1774c14a7b97`, *"Copyright (c) 2024-present, Francois Zaninotto, Marmelab"* | 🟡 **near-unshelved** — *"Atomic CRM"* 2 files, *"atomic-crm"* **0**. React-admin + Supabase |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** — `trunk/LICENSE`, **`11 906` B** | 🟢 carried (124 files). Accounting → CRM → MRP; 🔴 Java, heavy implementation cost |
| `Corteza` | Apache-2.0 *(as reported)* | 🟢 carried (82 files) |
| `Huly` | Apache-2.0 *(as reported)* | 🟢 carried (24 files) |
| 🔴 `Aureus ERP` | 🔴 **not verified** — `aureus-erp/aureus` `main/LICENSE` → **`404`** | 🔴 Reported MIT by one leg. **Address unconfirmed; do not cite** (`ACTION p417-C`) |
| 🔴 `ERPNext` | GPL-3.0-only | 🔴 **lists Education as a module** but fails the permissive shortlist |

🟢 **`atomic-crm` is the one worth adding**: stock-shape MIT at 1 105 B, React-admin + Supabase, which
is a far cheaper graft onto an existing student data store than OFBiz. 🔴 **`Aureus ERP` is explicitly
NOT recorded as supply** — a reported licence with a 404 at the probed path is not a finding.


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

### 🟢 A new attach point, and it is the cheapest one on this file: the package format

🔵 Every row already on this file attaches AI to a platform through an **extension mechanism** —
`XBlock` for Open edX, a plugin for Moodle, LTI for anything Apereo, MCP for the agent layer. Each
of those is an integration project: code the client has to review, install, host and keep working
across upgrades. 🟢 **There is a cheaper boundary, and as of today these shelves hold a permissive
tool that emits it.**

| Platform | Licence | SCORM ingest | What that means for a `Papermorph`-produced course |
|---|---|---|---|
| [Moodle](https://moodle.org) | 🔴 GPL-3.0 | 🟢 **core SCORM activity** | Upload the package, add the activity, done — no plugin review |
| [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 | 🟢 **imports SCORM packages** | Course-level import; grade passback through the standard |
| [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **SCORM supported** | 🟢 The permissive-platform path: no copyleft anywhere in the stack |
| [Open edX](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | 🟡 **via a community `scormxblock`** | Needs the XBlock installed first — so this one *is* an integration project |
| [Kolibri](https://github.com/learningequality/kolibri) | 🟢 MIT | 🔴 **not claimed** | Kolibri uses its own channel/content pipeline; 🔴 **do not assume SCORM** |

🟡 **Verification status, stated rather than implied.** The `Papermorph` side was read first-hand
today — MIT, `scripts/scorm.py`, SCORM 1.2 and 2004, `849★`. 🟡 **The ingest column was NOT re-read
first-hand this pass**; it is carried from platform documentation knowledge and should be confirmed
against the client's *actual version* before it reaches a statement of work. SCORM support is
notoriously version-sensitive, and "supports SCORM" has meant three different things on Moodle alone.

🟢 **Why this belongs on `verticals/solutions.md` and not only on `repos/`.** The question this file
exists to answer is *"the client already runs X — where does AI attach?"*. For content generation,
the answer has just changed from *"write an XBlock / a Moodle plugin / an LTI tool"* to **"emit a
SCORM package"** — which attaches to four of the five platforms above through a door that is already
open, already reviewed, and already in the LMS administrator's muscle memory.

### 🔴 The ERP question, re-run and re-answered: there is no permissive education ERP

The literal `open source platform education ERP CRM MIT Apache` leg returned **one** education ERP —
**[OpenEduCat](https://github.com/openeducat/openeducat_erp)** — and both the project's own site and
its Odoo app listing give the licence as **LGPL-3.0**, not MIT and not Apache. Everything else the
leg returned was the same vendor's comparison pages in eight languages.

| Claim on the vendor's pages | Status |
|---|---|
| Built on Odoo; students, courses, attendance, fees, timetables, exams, parent portal, plus native CRM/HR/payroll/accounting | 🟢 consistent across the listing and the site |
| "30,000+ institutions in 130+ countries" / "3 million users across 1,000+ institutions in 90+ countries" | 🔴 **the vendor's own pages contradict each other**; quote neither |
| Founded 2012 / founded 2014 | 🔴 contradictory on the same vendor's pages |
| Modules from $69/yr, user packs $299/yr, unlimited $4,369/yr | 🟡 vendor pricing, uncontested but unverified |

🔵 **The consequence for a build.** An education ERP engagement inherits **LGPL-3.0 plus Odoo's own
licensing**, which is a materially different conversation from the MIT/Apache agent layer above it.
🟢 The composition rule still works — **the LGPL stays in the platform, the permissive code stays in
the agents, and the boundary is a process boundary (MCP or a REST call), not a link.**

## 🆕 `p415` · 2026-10-23 — **The agent tier re-measured FIRST-HAND against the live GitHub sidebars, and three figures this base carried are refuted — one of them by a factor of 31.** 🟢 Fifteen agent addresses and nine foundations read today, every licence taken from the repository's own sidebar. 🔴 AND the read channel matters: `curl` and `api.github.com` are REFUSED for every repository not attached to this session, so a pass that reports "unreachable" from `curl` alone is reporting a fact about the CHANNEL.

🔵 **Dating note.** Every search leg and every licence read below was executed on **2026-10-23**, and the
commit lands **2026-10-23**. This is the twenty-first pass dated today, after `p395`–`p414`.

🔵 **Channel note, measured this pass.** `curl -sI https://github.com/CAHLR/OATutor` → **403**, and
`curl -s https://api.github.com/repos/HKUDS/DeepTutor` returns the session's own refusal body
(*"GitHub access to this repository is not enabled for this session"*), **not** GitHub's. The same
addresses read cleanly through `WebFetch`. Both instruments were run side by side before any address
below was written down. Every licence, star count and date in this pass came through `WebFetch`.

### 🟢 The platform layer — what a client already runs, and where AI attaches

| Platform | Licence | Verified | What it is | Where AI attaches |
|---|---|---|---|---|
| [Open edX](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 | 🟢 sidebar, today, **8.2k★** | MOOC-scale LMS + Studio authoring | **`XBlock`** components and the course/enrolment APIs. 🔴 AGPL reaches a hosted modification |
| [Moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 🟢 sidebar, today, **7.5k★** | The most-deployed LMS in education | Out-of-tree **AI provider plugins** (the `aiprovider_*` family) and the web-services API |
| [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 sidebar, today, **448★** | Full LMS: teaching, assessment, communication. Swiss lineage (OLAT / University of Zurich, maintained by frentix) | 🟢 **Anywhere — the grant does not constrain you.** This is the LMS to pick when the client needs modification rather than configuration |
| [Kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 sidebar, today, **1.2k★** | Offline-first learning platform; content packs sync when a link appears | 🟢 Local inference beside it. The pairing that makes AI tutoring work without bandwidth |
| [Oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 🟢 sidebar, today, **6.9k★** | Interactive *explorations* with feedback — closer to a tutoring engine than to an LMS | 🟢 Generate and grade explorations; keep Oppia's feedback loop as the pedagogy spine |
| [Sunbird](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🟢 **MIT** | 🟢 sidebar, today, **41★** | India's education digital public infrastructure | 🟢 National-scale reference for a public-sector engagement in APAC |
| [Mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 🟢 sidebar, today, **96★** | Self-hosted LMS **with an AI role-play mentor built in**, aimed at corporate L&D and compliance | 🟢 Already there — this is the one platform on the shelf that is AI-native rather than AI-extended |
| Canvas LMS | 🔴 AGPL-3.0 *(carried, not re-read this pass)* | 🟡 carried | Dominant LMS in North American higher education | An MCP server over the Canvas HTTP API — the AI side stays permissive even though the platform is not. 🔵 The server and its grant are named in the paragraph below this table, deliberately kept out of this row so the platform's copyleft cell cannot be read as the connector's |
| Sakai | 🟡 **ECL-2.0 or Apache-2.0 — sources disagree, NOT resolved** | 🔴 **unresolved** | Apereo Foundation LMS, higher education | 🔴 **Do not cite the licence until someone reads it.** Two secondary sources give two answers |

🟢 **The Canvas connector, named outside the table above.** [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — **MIT**, **307★**, licence read from the sidebar on **2026-10-23** — exposes Canvas courses, assignments and submissions to an assistant over the Canvas HTTP API.

🔵 **The architectural point this table is really making.** Every dominant LMS in education is
copyleft, and almost every useful AI component is permissive. **The MCP server is what keeps the two
apart**: `canvas-mcp` talks to Canvas over its HTTP API and carries MIT, so a client gets AI
capability over an AGPL platform without any licence question reaching their code. Build the agent
layer as a separate permissive service that speaks the platform's API. Never as a fork of the
platform.

### 🔴 The MCP layer over LMSs is where the licence risk actually is

Previous passes read this layer first-hand and the results do not improve: `openedx-mcp` is
**AGPL-3.0**; `moodle-mcp` (PyPI) ships an **empty `license` field and zero licence classifiers**;
`n35da/brightspace-mcp` has **no licence-shaped file anywhere in its tree**, on four independent
channels. 🟢 `vishalsachdev/canvas-mcp` (MIT, re-read today at 307★) remains the one well-formed
member of this family. **If an engagement needs Moodle or Brightspace through MCP, that connector is
something to write, not something to adopt.**

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

### 🟢 What the lattice changes for a vertical licence read, and the one row it corrects

🔵 This shelf's job is to say whether a platform can be **built on**, and on the copyleft verticals
that turns on reading one payload correctly. 🟢 **Two readings on this shelf's own flagships are
re-derived first-hand this pass:**

| platform | grant, read at a ref | what the lattice adds |
|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0**, `35 136` B / `671` lines / `e12d78569742` | 🟢 base is **`34 521`** = **lattice cell 2** (`http`, 662) + a **pure append** of `615` B / `9` lines. 🔵 The append's `NARROWED-OPERATIVE` consequence for a separate RPC service is `p413`'s finding and stands unchanged |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) · [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) | **AGPL-3.0**, `34 524` B / `662` / `8d56b405468a`, byte-identical | 🟢 **lattice cell 4** (`https`, 662). 🔴 `Gap 297-R` is untouched: both halves of the Open edX MCP side-car remain copyleft, and a **permissive** side-car still does not exist |

🔴 **The practical consequence, stated plainly:** a vertical licence read that grades by **byte band**
will see `34 520`, `34 521`, `34 523` and `34 524` as four different instruments and `34 501` as a
fifth. 🟢 They are **one licence in four presentations plus one de-indented transcription**, and the
in-tree discriminator that resolves them — Amendment 7 — is on the patterns shelf. 🔵 On this shelf
nothing is reclassified: every AGPL vertical row keeps its family, its posture and its gate.

### 🟡 An EMEA procurement signal this shelf should hold, labelled for what it is

🟡 **France's ministry prefers libre, in writing.** The *cadre d'usage de l'IA en éducation* instructs
readers to *"privilégiez les solutions libres qui permettent un contrôle des corpus utilisés ainsi
que des procédures de traitement"*, and the surrounding **feuille de route IA 2026–2027** names **La
Forge des communs numériques éducatifs** as the state's channel for libre educational resources, plus
an **AI tutor in pilot classes from Q3 2026** reviewed in **2027**. 🟢 For a shelf whose whole thesis
is *customise an open platform rather than buy a closed one*, that is demand stated in the
customer's own policy language. 🔴 **And it cannot be verified here**: `education.gouv.fr`,
`eduscol.education.fr`, **`forge.apps.education.fr`**, `conseil-ia-numerique.fr` and `pix.fr` are
**all five** `TUNNEL-REFUSED`, so this row is **search-channel only** per `gate-restatement`. 🔵 The
forge being unreachable is the expensive part: it is a **supply** host, not a policy one, so whatever
libre education assets it carries cannot be enumerated, licence-read or shelved from this
environment at all. 🔴 Declared as a channel gap, not as an absence of supply.

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

### 🔴 The most consequential licence fact on this shelf was sitting in a byte count

🔵 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) is carried here as `AGPL-3.0`,
`35 136` B, digest `e12d78569742` — read and re-read without drift since `p140`. 🔴 **What no pass
recorded is that those bytes include a nine-line clarification from EdX Inc. that NARROWS the
grant**, and the narrowing is the one every AI engagement on Open edX turns on:

> …any public, independently available web service offered over the network and communicating with
> edX's copyrighted works by any form of inter-service communication, including but not limited to
> Remote Procedure Call (RPC) interfaces, **is not a work based on our copyrighted work** within the
> meaning of the license. "Corresponding Source" … **do not include source code files for programs
> used solely to provide those public, independently available web services.**

🟢 **Read against AGPL §13, that is permission to put an AI service BESIDE Open edX rather than
inside it.** A tutor, a grading assistant or an MCP side-car that talks to the platform over RPC is
**not** a derivative work under this grant, and its own source is **not** Corresponding Source. 🔴 **The
architectural consequence is the opposite of what a bare `AGPL-3.0` cell implies**: the copyleft
risk is not in building alongside Open edX, it is in **modifying `edx-platform` itself** — and that
is a boundary a client can be held to in design review.

🔴 **The caveat, stated with the fact.** The clarification is **EdX Inc.'s statement of intent
appended to the licence file**, not a term of AGPL-3.0, and this base measured it in the payload
`openedx/edx-platform` serves at `master` on **2026-10-23**. 🟡 It is strong enough to design
against and **not** a substitute for counsel on a specific deployment; a client engagement cites the
payload, the ref and the date, which is why all three are recorded.

🟢 **And it is measurable, which is why it belongs on a shelf rather than in a memo.** `p378`'s
presentation fold collapses eight of ten AGPL-3.0 payloads this pass read to one text and **refuses
to fold `edx-platform`** — nine operative lines are not presentation. 🔵 So the base's own instrument
separates *the stock grant* from *the narrowed grant* without being told to, and the vertical layer
now carries the distinction rather than the byte count alone.

### 🔵 The vertical supply question, re-asked and unmoved

🔴 **The ERP/CRM/SIS leg returned eight platforms and not one unshelved**: `OpenEduCat` (LGPL-3.0),
`OpenSIS` (GPL-2.0), `Fedena` (Apache-2.0), `RosarioSIS` (GPL), `Gibbon` (GPL-3.0), `SchoolTool`
(GPL-2.0), `OpenOlat` (Apache-2.0, Java, higher-ed and corporate training rather than SIS), and
[`coderzaman/Student-Information-System`](https://github.com/coderzaman/Student-Information-System),
which `p409` already measured as a **726-day-stale teaching demo**. 🟢 **The leg's own conclusion
matches this base's**: *no major open-source SIS is MIT-licensed; the mature options are GPL, LGPL or
Apache*. 🔴 **`Gap 405-A` and `Gap 298` therefore stand, now corroborated from an independent
channel** — and the recommendation they imply is unchanged: **integrate against the system of
record, do not fork it.**

🔴 **A channel limit that bears directly on this shelf, and it is new.** `moodle.org` and
`openeducat.org` both answer **`http=000`** from this environment — *connection never established* —
against a control pair (`pypi.org`, `raw.githubusercontent.com`) that returned `200` in the same
loop. 🟢 **The two flagship vertical platforms on this shelf cannot be read at their own
domains here.** 🔵 Their *code* remains readable on the allowlisted code channel, so licence and
payload claims stay verifiable; **release notes, roadmaps and pricing do not.** A successor should
plan vertical-layer verification around the code channel and label anything sourced from a vendor
domain as search-channel — see the trends shelf for the standing rule.

🟡 **EMEA, with its boundary stated.** Portugal's **IAedu** (FCT/FCCN) offers institution-grounded
virtual agents with API access, and Portugal's higher-education diagnostic (**CNIPES**, April 2026)
proposes a shared *Plataforma de Práticas Pedagógicas de IA*. 🔴 **IAedu is restricted to RCTS-network
institutions**, which makes it a national service rather than deployable supply — the useful read is
that **the demand signal is institutional and the delivery vehicle is already chosen**, so an EMEA
engagement there sells integration and practice design, not a platform. 🟡 Both rows are
**search-channel only**: every Portuguese government and university host probed is `http=000`.

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

### 🔴 The platform layer — one gap re-dated, one gap re-opened

🔴 **`Gap 297-R` re-dated first-hand, and it is not closing.** The Open edX MCP side-car
[`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) has moved **`v0.1.5` → `v0.1.9`**
(**9 releases**, last upload **2026-10-22 · 1 d**) since this base last read it at `p190`
(**2026-10-14**), and it is still **AGPL-3.0** — on *both* PyPI sub-channels, the `license` field and
the OSI classifier. 🟢 Read through **PyPI**, because `api.github.com` and the GitHub HTML surface
are both `403` on this channel.

🔴 **So the gap stays open on the axis that matters to a studio: there is still no *permissive*,
production-graded Open edX MCP side-car, and four releases of active maintenance did not change
that.** 🔵 A client who will not accept AGPL-3.0 on a self-hosted deployment should not be told to
wait for this repository.

🔴 **`Gap 298` re-opens on authorship — the vertical platform that looked like it closed it does
not.** [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12), the MIT school ERP/SIS `p411`
shelved, re-measured over full history: **123 commits, 3 distinct `%ae`** (not the 5 `%an` published),
of which `devteam@gegok12.com` is a **shared role account with 83 commits — 67.5 %**.

| axis | `p411`'s reading | `p412`'s reading | state |
|---|---|---|---|
| grant | MIT, `LICENSE` 1 150 B | 🟢 unchanged, first-hand | 🟢 **holds** |
| build chain | `composer.json`, `Dockerfile`, `docker-compose.yml`, `artisan`, `phpunit.xml`, `.env.example` | 🟢 unchanged | 🟢 **holds** |
| scale | 7 623 tracked paths, Laravel 12 / PHP 8.4 | 🟢 unchanged | 🟢 **holds** |
| **authorship** | 🟢 “5 distinct authors — a company” | 🔴 **3 `%ae`**; 1 role account (67.5 %), 1 human >1 commit, 1 single-commit | 🔴 **REFUTED** |
| currency | HEAD 2026-06-25 · 120 d | 🔴 unchanged — **120 d** | 🔴 **stale** |
| scope | open-core, premium modules withheld | 🔴 unchanged | 🔴 **SOW item** |

🔵 **Read as a platform recommendation:** `gegok12` is still the only maintained company-backed
**MIT** school ERP/SIS on these shelves, and that is a real and useful fact. 🔴 **What cannot be
said about it any more is that its contributor base de-risks the dependency** — two thirds of its
history is one shared account, which is a bus-factor statement, and it belongs in a risk register
rather than in a column that reads “5 authors” — an unkeyed `%an` figure.

🟢 **`Gap 405-A` unchanged and named so it cannot look worked:** still no permissive vertical
platform with institutional backing. Nothing this pass moved it.

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

### 🟢 Two platform addresses read first-hand this pass, with the grant that governs each

| platform | grant | HEAD · age | scope | where it sits on the ladder |
|---|---|---|---|---|
| [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) | 🟢 **MIT**, 1 150 B | `99da145` **2026-06-25 · 120 d** | School ERP / SIS — Laravel 12, PHP 8.4, **7 623 paths**, Docker-shipped. Admissions, attendance, gradebook, exams, timetable, fees, parent portal | 🟢 **The permissive rung this ladder has never had a real occupant on.** 🔴 **Open-core** — premium modules are outside the repo |
| [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0, declared in 19 B** | `73ce33e` **2026-10-13 · 10 d** | Frappe/ERPNext education module — the live, maintained option | 🔴 **Copyleft rung.** The grant is thin but corroborated by three sibling repos |

🔴 **The two together are the decision, and it is a real one for the first time.** Until this pass
the SIS/ERP layer of this shelf offered copyleft-or-nothing: `frappe` family under GPL/AGPL,
`rosariosis` GPL-2.0, `openeducat` LGPL-3.0, `espocrm` AGPL-3.0. 🟢 **`gegok12` is a genuine MIT
occupant with a container and a company behind it** — but it is **120 days stale and deliberately
incomplete**, against `frappe/education` at **10 days and complete**.

🟢 **So the vertical choice is now a straight trade and a studio can state it in one line:**
**permissive-but-partial-and-slow (`gegok12`)** against **copyleft-but-whole-and-current
(`frappe/education`)**. 🔵 Which one wins is decided by the **deployment mode**, exactly as the
`p401` plugin-boundary rule says: a client self-hosting their own estate loses nothing to GPL-3.0,
so `frappe/education` is the better engineering answer. A studio building a **multi-tenant hosted
product** it intends to keep closed needs the MIT rung, and then **`gegok12`'s open-core scope is
the thing to price**, not its licence.

### 🔴 The licence ladder, re-confirmed on a channel that did not exist last pass

🟢 The Portuguese leg independently returned this shelf's own ladder: **Moodle and Chamilo
GPL-3.0; Open edX and Canvas AGPL-3.0.** 🔵 Nothing new — but it is the **first corroboration of
the ladder from a non-English source**, and it closes the possibility that the ladder is an
artefact of English-language sourcing. **The ladder is a property of the market, not of the leg.**

### 🔴 `gegok12` carries 16 vendored grants — and 15 of them are BUILD ARTEFACTS

🔴 Seventeen licence-shaped paths; one is the project's. The other sixteen are
`custompackages/brozot/laravel-fcm/LICENSE` and **fifteen webpack banner files** at
`public/js/<chunk>.js.LICENSE.txt`.

🔵 **Why this belongs on the platform shelf and not only in the gate:** a compiled platform ships
its dependency notices **inside its own public web root**. `Pattern AI` step 2's prefix list
(`vendor/`, `node_modules/`, `third_party/`, `native/*/packages/`) **does not catch `public/js/`**,
and a platform is precisely the kind of repository that has one. **Any grant audit of a built
PHP/JS platform must exclude build output by extension (`*.js.LICENSE.txt`) as well as by
directory.**

### 🔴 The census, carried forward and marked NOT re-derived

🔴 `p409`'s **2 695 addresses / 3 529 over both channels**, `STALE` for a third consecutive pass.
**`p411` shelves 15, `p410` shelved 8 — expect +23.**

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

### 🟢 Four platform addresses this pass read first-hand, with the grant that governs each

🔵 These are **systems to customise**, not agents — the Odoo/Moodle/OpenMRS layer of this shelf. The
grant is the deciding column, because a studio's deliverable is usually *modified code shipped to a
client*, and that is the act copyleft governs.

| platform | grant *(payload-read)* | HEAD · age | what a studio can actually do with it |
|---|---|---|---|
| [shrikrishna-lab/StudentManagement](https://github.com/shrikrishna-lab/StudentManagement) — “EduTrack ERP” | 🟢 **MIT** *(1,077 B)* | `e75afa5` **2026-10-04 · 19 d** | 🟢 **The only permissive, live SIS these shelves can name.** Three tiers, `database/student_management.sql`, registrar-depth DAOs (transcripts, clearance, certificate requests). 🟢 **MIT means fork, modify and ship, with attribution only.** 🔴 **Bus factor one** and no build file — so take the **schema and the domain model** as the asset and expect to own the Java tier if you adopt it whole. |
| [espocrm/espocrm](https://github.com/espocrm/espocrm) | 🔴 **AGPL-3.0** *(34,522 B)* | `167dbcb` **2026-10-23 · 0 d** | 🟢 Mature, general CRM, **committed today** — a real admissions/advancement CRM base. 🔴 **AGPL-3.0 reaches users over a network**: offer a modified EspoCRM as a hosted service to a university and the modified source is owed to its users. 🔵 Viable as **the client's own self-hosted system**, hard as a studio-hosted multi-tenant product. Say which, in the SOW. |
| [ivan-my-wong/flowclass](https://github.com/ivan-my-wong/flowclass) | 🟡 **DUAL, and the copyleft half is a 302 B stub** | `bdbc79b` **2026-09-20 · 33 d** | 🔴 **Do not adopt on the manifest.** `package.json` says `"SEE LICENSE IN LICENSE"` and `LICENSE` is MIT — but the README puts **self-hosted server distributions under AGPL-3.0** via a `LICENSE-AGPL` that is **0.9 % of the licence it names** and delegates to a URL. 🔴 Self-hosting is the *only* way a studio would deploy this, i.e. **the deployment mode a client wants is the one the copyleft half governs**. Ask the maintainer for a written grant before it is in a proposal. |
| [addex12/School-CRM](https://github.com/addex12/School-CRM) | 🔴 **UNRESOLVED — three channels, three answers** | `011a98c` **2025-05-10 · 531 d** | 🔴 **Not adoptable.** `LICENSE` is **874 B** of Apache-2.0 *notice* (7.7 % of 11,358 B), `composer.json` says `MIT`, the search result said Apache-2.0, and four of its five licence-shaped paths are **vendored dependency grants**. 🔴 Plus 531 d stale. 🔵 Carried so a successor spends no probe on it. |

🔴 **`Gap 405-A` and `Gap 298` both touch this file, and this pass moves one of them.** The permissive
*SIS* absence is now an **authorship** absence, not a code absence — see `repos/foundations.md`. The
permissive, production-graded *platform with institutional backing* absence is untouched: of the four
above, the permissive one has one author, and the mature ones are copyleft.

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

### 🔴 NEW licence-trap class: **three channels, three different answers, in one repository**

🔴 **[`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) — default ref `master` (not
`main`), HEAD `e935dec` 2026-08-15 · 69 d.** An actively-developed open-source ERP/CRM
(`backend/` + `frontend/`, Node + React), returned by this pass's ERP/CRM leg as a permissive
platform to build on. 🔴 **It is not one.**

| channel | what it says | authoritative |
|---|---|---|
| the web search result, read **2026-10-23** | 🔴 *"iDURAR is fully open-source under the **MIT** license"* | 🔴 **NO** |
| `backend/package.json` → `"license"` | 🔴 **`"Fair-code License"`** | 🔴 **NO** — not an OSI licence and **not an SPDX identifier**; it is the source-available marketing term of the n8n family |
| `README.md` → `## License` | 🟢 *"Released under the GNU Affero General Public License v3.0"* | 🟡 agrees with the payload |
| **`LICENSE` payload at root** | 🟢 **34,230 B**, first line `GNU AFFERO GENERAL PUBLIC LICENSE`, `Version 3, 19 November 2007` | 🟢 **YES** |

🟢 **Verdict: AGPL-3.0. Network copyleft.** Deploying a modified iDURAR as a hosted service for a
client triggers §13 — the client's modifications must be offered to its own users. 🔴 **Not a
build-on base for a client SaaS**, whatever the search result or the manifest says.

🔵 **Why this is a NEW class, and not one of the five this shelf already carries.** The existing
traps are all *upstream being misread at one channel*: a grant one directory down
(`openSIS-Classic`), a grant at `LICENSE.txt` (`ai-shifu`), AGPL text inside a GPL-named file
(`moodle-local_copilot`), a manifest claiming a grant whose payload is absent (`p388`), a fork
freezing its upstream's pre-relicence grant (`p408`'s `project-sunbird`). 🔴 **This one has three
channels returning three distinct answers simultaneously, and the two wrong ones err in OPPOSITE
directions** — the search says *more* permissive than the truth, the manifest says something
*outside the licence vocabulary altogether*. A reader who checks one extra channel and stops at the
manifest ends up **worse off than one who checked none**, because `"Fair-code License"` reads like a
deliberate, specific answer.

🟢 **The gate that catches it is cheap and it is the same one every time:** read the **payload at the
root of the default ref**, and read the **default ref** too — `master` here, which a `main`-only
probe would have missed entirely.

### 🟡 `Gap 297` restated — the Open edX MCP side-car EXISTS, and the gap should never have said otherwise

🔵 **`intel/open-gaps.md:18053` declares `Gap 297` — "Open edX has no MCP side-car, and it is the
second-largest open LMS" — and the ledger at `:18120` still carries it as 🔴 open.** 🔴 **That row is
stale, and this base's own shelves refute it:** `agents/top.md:1378` carries
[`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) (`master`, **AGPL-3.0**,
34,524 B payload-read, `v0.1.5`, 2★) together with its deployment half,
[`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp).

🟢 **This pass's Open edX leg corroborates the shelf from an independent channel**: run fresh on
2026-10-23, it returned `blend-ed/openedx-mcp` as **the only** Open edX MCP server in existence —
the same singleton the shelf recorded, found by a different route. It exposes staff/superuser admin
operations (course, user, role, enrolment, certificate, report, authoring) over **native
`openedx-platform` APIs only**, with access resting on the platform's own staff and superuser flags
re-checked live per request, and it is reached over streamable HTTP with a bearer key.

🟢 **So the honest restatement, which is narrower and more useful than the original:**

> 🔴 **`Gap 297-R`** — Open edX has an MCP side-car, but **no permissive one**. The only
> implementation is **AGPL-3.0**, matching the platform's own grant, and it is **2★ and
> `v0.1.5`** — experimental by its own versioning. The absence is of a *permissive, production-graded*
> Open edX side-car, not of a side-car.

🔵 **That distinction decides an engagement.** A client extending Open edX is already inside AGPL, so
`blend-ed` costs nothing extra in licence terms — it is the **maturity**, not the grant, that is the
risk there. A client wanting an MCP side-car *beside* a non-AGPL estate has no option on this shelf
at all. 🔴 The original gap wording would have sent both clients to the wrong answer.

### 🔴 The SIS layer, re-tested: permissive grants on dead code, live code under copyleft

🟢 Full six-row table in `repos/foundations.md`. The one-line consequence for a vertical build:
**there is no permissive SIS to fork**, so the SIS stays where it is and the AI layer integrates
against it. `coderzaman/Student-Information-System` is the only MIT SIS the leg returned and it is
**726 days stale**; `rosariosis` (GPL-2.0) is the live one; `openeducat_erp` (LGPL-3.0) is the
complete one; `fedena` (Apache-2.0) is the one permissive lineage and it could not be dated.

## 🆕 `p408` · 2026-10-23 — a fork that FROZE an abandoned grant, India's **MIT** DPI going stale, and eight legs that returned nothing unshelved

🔵 **Dating note.** Every probe, clone, licence read and search leg below was run on **2026-10-23**, and the commit lands **2026-10-23**. 🔵 **This is the fourteenth pass dated today**, after `p395`–`p407`.

🟢 **This is a RESEARCH pass, not an instrument pass.** `p405`–`p407` were all repairs to this base's own measurement layer. This one runs the prescribed brief — four global legs and one leg per region — and reports what the supply and the regional instruments actually returned, including where they returned nothing.

### 🔴 India's education DPI is MIT — and its reference implementation is going stale

🟢 **Sunbird ED is the grant this shelf's own licence thesis says should not exist at this scale.**
[`repos/foundations.md`](../repos/foundations.md) opens by stating that *the licence frontier in
education runs the wrong way*: Moodle GPL, Open edX AGPL, Canvas AGPL, OpenEduCat LGPL. Sunbird ED
is **MIT**, and it is the platform **DIKSHA** — India's national school platform — is built on.
🔴 **And its published implementation has not taken a commit in almost a year:**

| repo | default ref | licence *(payload, bytes)* | HEAD | days since |
|---|---|---|---|---:|
| [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🔴 `master` | 🟢 **MIT** *(`LICENSE`, 1,072 B)* | `9efc8b5` **2025-12-16** | 🔴 **311 d** |
| [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | `main` | 🟢 **MIT** *(`LICENSE`, 1,078 B)* | `9de5e08` **2025-09-19** | 🔴 **399 d** |
| `Sunbird-Ed/sunbird-learning-platform` | — | — | 🔴 **no ref resolves** | — |

🔴 **The third row is the one to read carefully.** `git ls-remote --symref` returns no HEAD for it,
and this base already states the limit that makes that verdict partial: **a failed resolve cannot
distinguish private from deleted.** What it does establish is that the address is not clonable from
here today, so it must not be named in a recipe.

🟡 **What this changes for an APAC engagement.** The grant is the easy part and it is already won —
MIT, at national scale, with a ministry adopter. The cost is **maintenance**: a studio taking
Sunbird inherits a reference implementation ~10–13 months behind, which is a fork-and-maintain
engagement, not an integrate-and-extend one. 🔵 That is the opposite trade from Moodle, where the
code is current and the **grant** is the obstacle.

## 🆕 `p407` — Microsoft ships a GPL-3.0 Moodle plugin that puts Moodle INSIDE Copilot

🟢 **New to this shelf, read first-hand at a pinned SHA.** The vertical-platform leg has been
`SATURATED` since `p403`, and this is the first addition in four passes — found not by a repo search
but by following a **plugin directory** entry to its source.

| plugin | repo | licence | release | Moodle | what it does |
|---|---|---|---|---|---|
| `local_copilot` | [microsoft/moodle-local_copilot](https://github.com/microsoft/moodle-local_copilot) | 🟡 **GPL-3.0** | **5.1.0**, `MATURITY_STABLE` | **5.1 only** (`supported = [501, 501]`) | Ships **two declarative M365 Copilot agents** — teacher and student — so Moodle is driven from **inside Word, PowerPoint and BizChat**. Teacher agent lists courses, creates assignments and forums, posts announcements; student agent self-enrols and reads grades and overdue work |

🔵 **Read, not inferred.** `HEAD` = `404ab2b6296c61f9d246605afe98d91b4f12d56c`;
`version.php` (1 342 B, HTTP 200) gives the release ladder; `LICENSE` (35 148 B, HTTP 200) is the
canonical GPL-3.0 text. 🔴 **And it re-confirms `p401`'s §13 trap on a fresh payload:** that file
says **"GNU Affero"** three times, so a naive grep publishes `AGPL-3.0` — the exact mechanism that
produced seven false verdicts at `p401`. The **title block** is what decides, and it reads
*"GNU GENERAL PUBLIC LICENSE Version 3"*.

### 🔴 Why it matters commercially, and why it is NOT a sovereign option

🟢 **The direction is new on this shelf.** Every Moodle AI row here so far puts a model *behind*
Moodle (the `aiprovider_*` family, `p404`). This one puts **Moodle behind Microsoft's agent surface**:
the teacher never opens the LMS. 🔵 For a client already on M365 that is the shortest path to
"agentic LMS" in existence, and it is **first-party**, not a studio integration to maintain.

🔴 **Two hard limits, stated so a proposal does not overreach.**
- 🔴 **GPL-3.0 and Moodle-5.1-only.** `supported = [501, 501]` is a *single* release — a client on
  4.5 LTS **cannot install it**, and `p401`'s plugin-boundary rule governs what studio code may sit
  beside it.
- 🔴 **It requires M365 Copilot licensing and an Entra app registration.** There is **no
  sovereign or local-model path** through this plugin, so it is the opposite of the Ollama-provider
  route this shelf recommends for EMEA sovereignty and LATAM cost. 🔵 **Both can be true on one
  estate, and a proposal should say which surface it is buying.**

🔴 **An informed gap, not a silence.** The plugin directory lists **5.0.0** and **4.5.2** as its
published versions while `HEAD` is **5.1.0** — `p977`'s lesson exactly (*a version ladder read from
the wrong channel reports a stale release without failing*). 🔵 `moodle.org` is
**`EGRESS_BLOCKED`** through this proxy, so which of the three a client's directory actually offers
could **not** be read first-hand; the repository ladder is what is pinned above.

## 🆕 `p406` — the vertical platforms are the ONE tier with zero decay, and the licence ladder is why

🟢 **`verticals/solutions.md` carries 104 addresses and NOT ONE of them failed to resolve** — **0 %
decay**, against a base rate of ~~2.20 %~~ **1.94 %** 🔴 *(`p407` — `p406`'s figure counted 7 non-repositories as decay)* and against `agents/top.md`'s 12 dead addresses. 🔵 Measured
per shelf, two of the nine are clean: this one at **0 / 104** and `intel/market.md` at **0 / 74**.
The other seven run `agents/trending.md` **53** · `repos/trending.md` **46** ·
`intel/open-gaps.md` **28** · `agents/top.md` **12** · `repos/foundations.md` **5** ·
`intel/trends.md` **4** · `compose/patterns.md` **2**.

🔵 **That is not luck, and the mechanism is worth naming because it is a procurement argument.** This
shelf's rows are **institutional platforms** — Moodle, Open edX, Canvas, Sakai, Kolibri, OpenOlat,
BigBlueButton, H5P, OpenEduCat, Frappe LMS, Opencast — each with a foundation, a consortium or a
company behind the namespace. The decay on this base concentrates in **single-maintainer MCP servers
and npm-published demos**, which is exactly the population `agents/top.md` is made of. 🟢 **So the
layer a client's system of record sits on is the layer least likely to vanish**, and the layer
Globant composes *on top* is the volatile one. Pattern consequence in
[`compose/patterns.md`](../compose/patterns.md).

### 🟡 The licence shape of this tier, restated against this pass's reads

| platform | licence | 🟢 permissive enough to build on and redistribute? |
|---|---|---|
| **Moodle** | GPL-3.0 | 🔴 copyleft — a plugin inherits it |
| **Open edX** | AGPL-3.0 | 🔴 copyleft, **network clause** |
| **Canvas LMS** *(community edition)* | AGPL-3.0 | 🔴 copyleft, network clause |
| **Sakai** | 🟡 **ECL-2.0** | 🟡 permissive, Apache-derived, **narrowed patent grant** |
| **Opencast** | 🟡 **ECL-2.0** — 🟢 title line read first-hand this pass at `153d1b1` | 🟡 same |
| **Kolibri** | MIT | 🟢 yes |
| **OpenOlat** | Apache-2.0 | 🟢 yes |
| **H5P** | MIT *(core libraries)* | 🟢 yes |
| **OpenEduCat** | LGPL-3.0 | 🟡 weak copyleft |

🟡 **ECL-2.0 now appears TWICE on this tier** (Sakai, Opencast) and it is **neither MIT/Apache nor
copyleft** — an Apache-2.0 derivative whose patent grant is narrowed to the licensor's own
contributions. 🔵 A Globant engagement that prices *"MIT / Apache 2.0 / BSD only"* will mis-sort both,
and the error runs **toward over-caution** on this tier: ECL-2.0 is permissive and both platforms are
redistributable. 🟢 Stated here so the shortlist is not applied as a filter that silently drops the
two Apereo platforms.

### 🔴 The LMS-MCP layer's supply is the volatile half, per platform

🔴 Of the carried MCP addresses that **do not resolve**, every one is on the agent tier and none on
this one: `eastarctica/canvas-mcp`, `e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp`,
`nmaaalhawary/mcp-moodle`, `owen-x-tech/canvas-mcp`, `owentaylor/canvas-mcp`,
`nahuelalbornoz/moodle-mcp`. 🟢 **Blackboard's permissive MCP supply is now 0 of 2 resolvable** — both
addresses this base carries for it are dead, which `agents/top.md` already recorded and this sweep
confirms independently through a different channel.

🟢 **Moodle is the exception and the two MIT servers `Gap 405-A` named both resolve:**
[`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) and
[`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) — 🟢 `EXISTS-PUBLIC`, probed this pass.
🔵 So the layer-2 recommendation `p405` corrected is also **alive**, which is the half a lineage
question cannot answer.

---

## 🆕 `p405` — the LMS-MCP layer, per platform: how much supply each LMS actually has

🔴 **This file, and `agents/top.md`, have cited LMS MCP servers by bare slug while this base's own
[`intel/open-gaps.md`](../intel/open-gaps.md) item 3 recorded that nothing here knew whether the
crowding was *"many projects or a few forked many times."*** 🟢 **Measured 2026-10-23 from full clones
— 42 addresses, 269 pairs, every pair graded** — and the answer differs **per platform**, which is the
grain an engagement actually asks at.

| the LMS a client runs | addresses | 🟢 **independent projects** | 🟢 **clone this** | what a studio should conclude |
|---|---|---|---|---|
| **Moodle** | 10 *(`moodle-mcp`)* + the `moodle-mcp-server` pair | 🟢 **10 + 2** | 🟢 [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) *(MIT, npm, 6 tags, **1 d**)* or [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) *(MIT, crates.io, 7 tags, **3 d**)* | 🟢 **The deepest and the only genuinely uncollapsed supply: 45 pairs, 45 `INDEPENDENT`, zero shared commits and zero shared trees anywhere.** Ten real implementations means a real **choice** — by runtime (Node vs. a Rust static binary) and by integration channel (browser session vs. Web Services) |
| **Canvas** | 20 resolvable | 🔴 **9** | 🟢 [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) *(MIT, 1,089 commits, 23 tags, **1 d**)* | 🔴 **The most overstated: 11 of the 20 are one family on root commit `afe32c3e1721`, authored by `vishalsachdev`.** A market map that counted addresses would show Canvas with twice Moodle's supply; by projects it has **fewer** |
| **Blackboard** | 8 resolvable | **6** | 🟢 [`alanwtom/blackboard-mcp`](https://github.com/alanwtom/blackboard-mcp) *(MIT, **1 d**)* or [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) *(MIT, 3 tags, **9 d**)* | 🟡 **Thin everywhere.** The largest of the eight is **28** commits. 🔴 No address here is a dependency; they are reference implementations to read before writing your own |
| **Brightspace / D2L** | 4 | 🔴 **2** | 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) *(MIT, 472 commits, 6 tags, **1 d**)* | 🔴 **Effectively ONE maintained project.** Three of the four share root `fb3d6c0a57bf` by `RohanMuppa`; the only independent address, `pranav-vijayananth`, is **7 commits, Apache-2.0, 374 d**. 🟡 Sell this as a single-vendor dependency with the risk stated |

🔴 **Why this correction belongs on THIS file and not only on a repo shelf.** A platform-coverage claim
is what a client hears as *"the ecosystem supports our LMS."* 🟢 **Canvas and Brightspace coverage is
narrower than their address counts**, and Brightspace in particular rests on **one maintainer**. 🔵 A
pitch that says *"there are twenty open-source Canvas MCP servers"* is true about addresses and wrong
about the thing the client is buying.

🟢 **The deployment seam is unchanged**, and is the reason the choice is free: the MCP server sits at
layer 2, so it can be MIT or GPL without reaching a studio's layer-3 — see
[`compose/patterns.md`](../compose/patterns.md). 🟢 **What changes is that the Moodle side now has an
MIT option with a published release**, where `p404` could only offer *"vendor a pinned commit."*

🟡 **One grant note with an engagement consequence, measured on a fifth address.**
[`marcosnahuel/moodle-mcp`](https://github.com/marcosnahuel/moodle-mcp) *(MIT, 1,065 B, 10 tags, npm
`@nahuelalbornoz/moodle-mcp`, **173 d**)* **ships a real Moodle plugin inside the MIT repository** —
`local_italiciamcp`, with `db/services.php`, `db/access.php` and 13 `classes/external/` web-service
functions. 🔴 **18 PHP files, ZERO GPL mentions, and no licence file anywhere inside the plugin
directory**, so the only grant reaching a Moodle plugin here is the repository's **MIT**. 🔴 **Read this
as a diligence flag, not a shortcut:** a plugin calling Moodle's GPL APIs is normally held to GPL
distribution terms, so the most likely reading is a defect on the author's side. 🟢 **`p401`'s boundary
rule is unchanged** — a studio's permissive code still belongs **outside** the plugin boundary. Rows:
[`plugin-inherited-grant.2026-10-23-p405.tsv`](../evidence/plugin-inherited-grant.2026-10-23-p405.tsv).

🔵 **The platform leg itself stayed saturated**, as `p403` predicted: `open source platform education
ERP CRM MIT Apache` returned `openeducat.org` vendor glossary pages in six languages plus **ERPNext**
(GPL-3.0), **Twenty** (BSL-1.1) and a **2010** CK-ERP mailing-list post. 🔴 Every licence claim it
produced came from a vendor page — a **POINTER, never a grant** (`p288`).

---


## 🆕 `p404` — the `aiprovider_openaicompatible` pair is NOT two independent vendors, and this file said it was

🟢 **Measured first-hand on 2026-10-23 from full-history clones.** 🔴 **This file's own text read
*"two independent vendors … ship an OpenAI-compatible provider under the same plugin name"*. That is
refuted**: it is **one author's content copy**, and the copy is the live address.

| | measured |
|---|---|
| 🟢 **Verdict** | **`CONTENT-COPY`**, direction [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) → [`ADORSYS-GIS`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible) |
| 🔵 **Why a ref-set test could not see it** | **0 shared commit SHAs.** A squash-republish shares none, so `p402`'s ref-set instrument grades a copy exactly like two unrelated namesakes |
| 🟢 **What proves the direction** | The **single** shared tree `85d9a99e3c96` is `ADORSYS-GIS`'s **root** tree, and is `lmscloud-io`'s working tree at `c8b6f9fe`, **2026-06-09** — seven weeks before the copy's root commit of 2026-07-27. A root commit cannot hold content that did not already exist |
| 🟢 **Corroboration ×2** | Both root commits carry the **same author identity** `Leghadjeu-Christian <legochristianarthur@gmail.com>` — a hand-off, not a lift · the copy **inherits** `$plugin->version = 2026060200` and only then bumps to `2026101500` |
| 🟢 **Which to deploy** | 🟢 **`ADORSYS-GIS` — 8 d** (HEAD `371278b0ebd6`, 2026-10-15), `moodle-plugin-ci` with a **Moodle 5.0+ matrix**, a commit linking the **Moodle Plugins directory listing**. 🟡 `lmscloud-io` is **93 d** (`040b74d5b13e`, branch `moodle405`) — the provenance, not the product |
| 🟡 **One regression in the copy** | `lmscloud-io` declares `$plugin->supported = [500, 502]`; **`ADORSYS-GIS` dropped it** while keeping `$plugin->requires = 2025041400`, so the live plugin ships **no declared Moodle upper bound**. Pin the Moodle version in the engagement's own config |
| 🟡 **Grant** | **Unchanged and `LADDER_BLIND` reproduced** — no licence-shaped file in either root tree; `GPL-3.0-or-later` lives only in the PHP headers |

🟢 **The seam itself is unaffected.** *Implement the provider interface, point it at your own gateway,
keep the IP behind the gateway* stands exactly as this file states it — what changes is **which address
a studio clones** and that the "two vendors" framing overstated the ecosystem's breadth: there is **one**
OpenAI-compatible `core_ai` provider lineage here, maintained by one author, now at its second address.

🔴 **Also corrected on this file:** the LTI row at **`macewan-cs/lti`**. It has a strict superset at
[`astiusa/lti`](https://github.com/astiusa/lti) — **89 / 89** commits reachable, same MIT bytes
(1,108 B, `6e58273960b0`), **794 d** against **1,919 d**. 🟡 The *recommendation* is unchanged (both
are dead, both carry **0 tags**); the **dating** was 1,125 days out.

🔵 Instrument, 9 controls and three end-to-end reproductions:
[`compose/code/p404-fork-direction/`](../compose/code/p404-fork-direction/README.md) · rows:
[`fork-direction.2026-10-23-p404.tsv`](../evidence/fork-direction.2026-10-23-p404.tsv).

---

## 🆕 `p403` — the vertical-platform leg is SATURATED, and the candidates are named

🔴 **The prescribed vertical leg (`open source platform education ERP CRM MIT Apache`) returned
`0` unshelved platforms on 2026-10-23.** 🟢 **Named rather than summarised, so a successor does not
re-spend the leg:** `frappe/education` + **ERPNext**, **OpenEduCat**, **openSIS**, **Fedena** and
**GegoK12** were all returned, and **every one is already carried on these shelves** — most of them on
this file. 🔵 **An informed gap, not a silence:** the open-source education platform layer (LMS, SIS and
ERP) is the **most mature** layer in this industry's supply, and a leg phrased as a platform search now
reliably returns this base's own contents.

🟡 **One quality note on the leg's own sources.** Every licence claim it produced came from **vendor
pages or vendor-written comparisons** — including the Apache-2.0 claim for **Fedena** and the MIT claim
for **GegoK12**. 🔴 This base grades those as **POINTERS, never grants** (`p288`): a licence belongs to
the payload at a ref, and a vendor comparison table is neither.

🔵 **Where new platform-layer supply has actually come from** is the record and standards layers
(`p393`'s 1EdTech tier, `p388`'s integration tier) and from **national-language legs** — not from the
platform-category search. See [`intel/trends.md`](../intel/trends.md) `T35` and `p401-T1`.


**🆕 Pass `p401` · reads and commit both 2026-10-23.** 🔴 **The Moodle plugin layer — the most
active AI integration surface in education — is uniformly `GPL-3.0-or-later`, and half of those
grants are invisible to a licence-file check. This is the file where that costs an engagement
money, so the rule is written here.**

## 🆕 `p401` — the plugin boundary rule: where a studio's permissive code may and may not sit

🟢 **The measurement first.** Every Moodle plugin address on these shelves — **60 slugs**, read
2026-10-23 through two channels — yields **51 grants, every one `GPL-3.0-or-later`**. 🔴 **Not one
MIT, Apache-2.0 or BSD in 51 reads.** And **27 of the 51 carry no licence file at any of
`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`** — the grant lives in the header of
`version.php` and every other PHP file, because the plugin is the distribution unit. Census:
[`moodle-plugin-grant-channel`](../evidence/moodle-plugin-grant-channel.2026-10-23-p401.tsv).

🔴 **The failure mode this prevents, stated as a sentence a studio lead can act on.** A plugin
with no licence file looks unlicensed, and an unlicensed-looking component gets treated as
*unencumbered*. It is the opposite: it is **strong copyleft with a "or-later" clause**. 🔵 A
pre-flight that asks *"does this repo have a LICENSE file?"* returns **a wrong answer in the
dangerous direction for 53% of this family.**

### 🟢 What the rule actually permits

| where the code sits | licence consequence | verdict for a studio |
|---|---|---|
| **Inside** a Moodle plugin (`local_*`, `block_*`, `mod_*`, `aiprovider_*`, `tiny_*`, `qtype_*`) | The plugin is a derivative work of Moodle and is distributed under **GPL-3.0-or-later**. Moodle's own plugin directory requires it. | 🔴 **Never the home for proprietary logic.** Fork, extend and **contribute back** — a perfectly good engagement, but it is services, not a product. |
| **Outside** the plugin, called over a network boundary — an **MCP server**, a REST service, a queue worker | GPL-3.0 is **not** a network-copyleft licence. Code the plugin merely *calls* across a process/network boundary is not a derivative work of it. | 🟢 **This is where a studio's permissive or proprietary IP goes.** The plugin becomes a thin GPL adapter; the model routing, retrieval, grounding corpus and evaluation harness stay outside it. |
| Inside a plugin, but linked to an **AGPL** component | AGPL's §13 reaches users interacting **over a network** — a hosted LMS is exactly that. | 🔴 **Check before hosting.** 🟢 This census found **zero** AGPL in the plugin family, so the risk here is theoretical for Moodle today — but `bycs-lp/moodle-tiny_ai`, `limekiller/moodle-block_openai_chat`, `cgrevisse/moodle-qbank_genai`, `danielcregg/moodle-local_aitutor`, `adamjenkins/moodle-local_nomoreai`, `yedidiaklein/moodle-local_aiquestions` and `saylordotorg/moodle-local_ai_course_assistant` all ship a **full 35,149 B GPL-3.0 text whose §13 names the AGPL**, and a substring check reads that as AGPL. 🔵 Do not let a tool tell you these are AGPL. They are not. |

🔵 **The `aiprovider_*` shim is the tell, and it is where the ecosystem is heading.** Moodle's
`core_ai` subsystem now has provider plugins, and 🆕 🔴 **ONE author's lineage at two
addresses** — 🟢 [`ADORSYS-GIS`](https://github.com/ADORSYS-GIS/moodle-aiprovider_openaicompatible)
*(live, 8 d)* and [`lmscloud-io`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible)
*(origin, 93 d)* — ship an OpenAI-compatible provider under the **same plugin name** with a
**byte-identical `classes/provider.php` at 3,963 B**. 🆕 🔴 **`p404` refutes the
"two independent vendors" reading that stood here**: `CONTENT-COPY`, direction `lmscloud-io` →
`ADORSYS-GIS`, measured from full history — see the top of this file. 🟢 **Both are `LADDER_BLIND` `GPL-3.0-or-later`.** 🔵 For a
studio this is the cheapest supported seam in the whole platform: implement the provider
interface, point it at your own gateway, and keep everything behind the gateway. 🆕 🟢 **Direction
IS established as of `p404`** — `lmscloud-io` → `ADORSYS-GIS`, from the root-tree position in full
history, not from the equal bytes. **Clone `ADORSYS-GIS`.**

🟡 **The permissive exception, named so the table above is not read as "Moodle is closed to
permissive work".** [`microsoft/moodle-ai-assistant`](https://github.com/microsoft/moodle-ai-assistant)
is **MIT** *(1,084 B, payload-read 2026-10-23)* — an accelerator for deploying an AI agent against
Moodle rather than a plugin living inside it, which is the boundary rule above demonstrated by its
author. 🔴 It is **alpha (0.1.0)**; this shelf already carries it and `p401` does not re-promote it.

**🆕 Pass `p400` · reads and commit both 2026-10-23 — sixth pass of the day.** 🔴 **No platform
was added**, and the vertical-platform leg returned the standing result again: **no
education-specific MIT or Apache platform exists**; the capable systems are GPL, AGPL or
LGPL — **Moodle** (GPL-3.0, ~1 800 plugins, still the most-deployed LMS), **Open edX** (AGPL-3.0,
stewarded by Axim Collaborative), **OpenEduCat** (LGPL-3.0 ERP on PostgreSQL), with Sakai, ILIAS,
Chamilo and Canvas (open core) behind them — 🔴 all already carried or already excluded here.

🟢 **What changed for this shelf is upstream of it, and it changes an APAC pre-flight.** Every
platform here is deployed into a jurisdiction, and
[`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) — the file a deployment pre-flight
actually reads — 🔴 **carried exactly ONE APAC teaching-mandate row, and it said
`NOT_ESTABLISHED`.** 🟢 It now carries **seven**.

🔵 **Concretely for this shelf:**

- 🟢 **A Moodle or Open edX engagement in Beijing** now reads a binding curricular floor —
  **no fewer than 8 class-hours per academic year, all primary and secondary schools, from the
  autumn 2025 semester** (`CN-BJ`, `MANDATED`). That is a **reporting and timetabling
  requirement on the platform**, not a content nice-to-have.
- 🟡 **The same engagement elsewhere in the PRC reads `ADVISORY_NONBINDING`** — a *guide* with
  two sanctioned delivery modes (standalone course **or** cross-disciplinary integration), which
  is a **configuration** decision the platform must support both ways rather than a mandate to
  implement once.
- 🟡 **An India engagement reads `IN-CBSE | MANDATED` but `IN | NOT_ESTABLISHED`** — so a
  CBSE-affiliated deployment has a dated curriculum to build to (Classes III–VIII from 2026-27,
  **integrated into Mathematics/EVS at Classes 3–5**, no board exam), and a non-CBSE deployment
  has no national instrument behind it. 🔴 **Pitching the two as one addressable market is the
  error `400-F` corrected.**
- 🔴 **A Korea engagement reads `NONE_IN_FORCE`** — ministry-mandated AI courseware **existed and
  was withdrawn to optional status within a year**. Lead with platform optionality there, not
  with mandated content.

**🆕 Pass `p399` · reads and commit both 2026-10-23 — fifth pass of the day.** 🔴 **No platform
was added.** The vertical-platform leg returned **OpenEduCat**, **ERPNext** (GPL-3.0), **Twenty CRM**
(BSL-1.1, not OSI-permissive) and **Odoo** — 🔴 all already carried or already excluded here, and the
leg's own summary again volunteered this shelf's standing result: *"no education-specific MIT or
Apache platform"*, the capable ones being AGPL, GPL or source-available.

🟢 **What changed for this shelf is upstream of it.** Every platform here is deployed into a
jurisdiction, and [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv) — the file a deployment
pre-flight actually reads — 🔴 **carried no LATAM teaching-mandate row at all** until this pass.
🟢 It now carries **six**, headed by **Colombia's `Ley 2626 de 2026`** (binding, official schools,
curricular guidelines due **Feb 2027**).

🔵 **Concretely for this shelf:** a Moodle, Open edX or Chamilo engagement in **CO** is no longer a
greenfield curriculum question — there is a statute naming the competencies the deliverable must
carry, and a **Feb 2027** date it must land before. 🔵 That is a scoping input, not a licence one,
which is why it is recorded here as a pointer rather than as a new row. `Gap 398-C`.

**🆕 Pass `p398` · reads and commit both 2026-10-23 — fourth pass of the day.** 🔴 **No platform was
added.** The open-source-LMS leg returned **Open edX, Chamilo, ILIAS, Frappe LMS and Sakai** — 🔴 **all
already carried here**, and the leg's own summary volunteered what this shelf has recorded for many
passes: *"no strong option under MIT or Apache"*, the capable ones being AGPL or GPL. 🟢 **One tracked
signal did move.** [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) re-read first-hand —
**MIT**, **41.3k ★**, corroborating this base's `41 208` and the `p389` finding that a third-party
review's *"AGPL-3.0 with commercial licensing"* claim is simply wrong. 🆕 **`v1.3.0-rc.1` is dated
2026-10-22**, while [`repos/trending.md`](../repos/trending.md) tracked `v1.2.0-rc.1` (2026-10-04) as
*"still a pre-release, 11 days on"* — 🔴 **a second RC series opened without the first reaching
stable.** 🔵 For a platform recommendation that matters: the grant is clean and the adoption is real,
but **this project has not shipped a stable release in two RC cycles**, so pin a commit rather than a
tag. `Gap 398-C`.

**Pass `p397` · reads and commit both 2026-10-23 — third pass of the day.** 🟢 **A platform's
address and a platform's *project* are not the same thing, and this pass can finally tell the
difference without reading prose.** `396-F`'s root-commit arm, extended with a HEAD comparison and
run over the shelf, folded **eight** address pairs into single artefacts — and one of those folds is
a **governance** change a studio should quote to a client. Evidence:
[`shelf-lineage`](../evidence/shelf-lineage.2026-10-23-p397.tsv).

### 🔴 The fold this pass thought it had found, and the register that already held it

🔴 **`p397`'s draft announced the credential wallet's move to a Linux Foundation umbrella as a
governance finding. This shelf already carries it, and `p350` put it there.**
[`openwallet-foundation-labs/learner-credential-wallet`](https://github.com/openwallet-foundation-labs/learner-credential-wallet)
is recorded `CANONICAL` in [`alias-register`](../evidence/alias-register.2026-10-21-p370.tsv), with
`digitalcredentials/learner-credential-wallet` as its **STALE** sibling, proven at `p349` from the
search index's `full_name` and repository `id` — and `p350`'s note says in so many words that the
canonical was **already applied to this shelf**. 🟢 Caught by `gate-alias-canonical`, which went red
on the draft.

🟢 **The substance stands and is worth restating once, because it is what a client actually asks:**
the MIT Digital Credentials Consortium wallet is maintained under **OpenWallet Foundation Labs**, a
**Linux Foundation** project — a materially better answer to *"who maintains this after the grant
ends"* than *"a university lab"*. 🔵 **What `p397` adds is corroboration from an independent
channel**, not the fact: shared root `af51e5505cbf`, identical HEAD `1c46a82ba384`, read from git
with no index and no API.

🟡 **And one register row this pass can genuinely move.** For `ease`, the register's index channel is
**blind** — both rows read `index-returns-ZERO` / `NO-CANONICAL`, which is why **`ACTION ZZ-al`** has
been unresolved since `p350`. 🟢 The clone arm proves [`openedx/ease`](https://github.com/openedx/ease)
and `edx/ease`, its **STALE** sibling, are **one repository** (shared root `79dd16652a23`, identical
HEAD `056da0adc6f3`) without the index at all. 🔴 **It cannot say which address is canonical**, which
is `ZZ-al`'s real question — so the identity half is proven and the direction half is still open.

> 🔴 **`p402` CORRECTION — the advice that stood here is REFUTED.** This paragraph used to end
> 🔵 *"Prefer the `openedx` path for anything written today, on the stewardship argument rather than
> on the register."* 🔴 **`openedx/ease` is itself STALE.** The canonical address is
> [`openedx-unsupported/ease`](https://github.com/openedx-unsupported/ease) — a third owner with
> **zero** prior mentions in this base — established from the **HTML header after the redirect** and
> corroborated by a ref-set fingerprint identical across all three addresses (**173 refs**, fp
> `e3793cd329e4`). 🟢 **`ACTION ZZ-al` is CLOSED**, ~52 passes after `p350` opened it.
> 🔵 **And the stewardship argument inverts:** Open edX moved this code to an owner named
> `unsupported` and archived it read-only on **2024-02-28**. It is **AGPL-3.0** either way, so it was
> never on the permissive shelf — but **cite the canonical address, and cite it as archived.**

### 🔵 The standards layer, de-duplicated

🟢 **`IMSGlobal` → `1EdTech`** is a rename GitHub keeps answering on both paths, and this base
harvested both for `caliper-spec`, `openbadges-specification` and `lti-1-3-php-library` — three
"pairs" that are three repositories, not six. 🟢 **Cite the `1EdTech` path** when writing a conformance
clause into a statement of work; it is the one the standards body publishes from.

🔵 **What did NOT fold, and that is the useful half:** `OpenLRS`
(`Apereo-Learning-Analytics-Initiative` vs `openHPI`), `qti-convert` (`citolab` vs `rolfis`),
`ims-lti` (`instructure` vs `omsmith`) and `lrs` (`yetanalytics` vs `escolalms`) all have **distinct
root commits** — same name, unrelated code. 🔴 **Four same-name pairs on this shelf that a
name-matching de-duplication would have wrongly merged**, which is the error the arm was built not to
commit.

**🆕 Pass `p396` · reads and commit both 2026-10-23.** 🟢 **The platform question this shelf could not
answer until now: once a platform is customised, where does the learning data go, and can the client
own it?** `p395` settled how an agent *launches* from Moodle, Canvas, Blackboard or D2L (LTI 1.3).
This pass settles how it *records*. Evidence:
[`record-layer-dating`](../evidence/record-layer-dating.2026-10-23-p396.tsv).

### 🟢 The emitter shelf — getting data out of the platform

| Platform | Emitter | Licence | HEAD | Age | Note |
|---|---|---|---|---|---|
| **Moodle** | [`davidpesce/moodle-logstore_xapi`](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 **GPL-3.0** | `df5c665` | 🟢 **2 d** | 82 ★, 95 forks — the live, maintained route out of Moodle |
| **Open edX** | Aspects → [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** | `91fef11` | 🟢 **10 d** | Open edX's own analytics stack **already ships Ralph as its LRS** |

🔵 **The Moodle row is a licence note, not a licence problem.** `moodle-logstore_xapi` is GPL-3.0
because every Moodle plugin is — Moodle itself is GPL, and a plugin inherits the obligation. A studio
deploying it into a client's Moodle is *using* it, not redistributing a derived product, which is the
ordinary posture for the whole Moodle plugin estate already on this shelf. 🔴 It is a problem only if
a client wants the emitter embedded in a proprietary product they ship.

🟢 **The Open edX row is the strongest platform+AI story on this shelf**, and it needs no
integration work invented here: Open edX Aspects already selected Ralph as its LRS with ClickHouse
underneath. A studio customising Open edX gets an **MIT, 10-day-fresh, French-public-sector-maintained
LRS** in the architecture by default.

### 🔴 What is NOT on this shelf, stated because the absence is the finding

🔴 **No permissive LRS ships inside any of the big platforms.** Moodle, Canvas, Blackboard and D2L
all expect you to bring one. 🔴 **And `LearningLocker` — the LRS almost everyone names — has not had
a commit since 2021-11-16 (1,801 days), is GPL-3.0, and carries no archived banner or deprecation
notice on its page.** 585 ★ and 294 forks make it look maintained. 🔵 **This is the single most
likely wrong decision a studio could make on this layer**, and nothing on GitHub warns against it.

🟢 **The replacement depends on the client's runtime**, which is the cross-layer table in
[`repos/foundations.md`](../repos/foundations.md): Python → Ralph, JVM → `lrsql`, .NET →
`xapi-dotnet`, Node/TS → `pelotech/xapi-lrs` **only after you run the conformance suite yourself**.

### 🟡 A conformance toolkit worth watching, not yet worth quoting

[`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) — 🟢 **MIT** (1,080 B,
`df57b343c1a3`), HEAD `3596bb5`, **37 d**, 🔴 **2 ★** — is a TypeScript monorepo offering typed
contracts, a headless QTI runtime and conformance runners across **xAPI, cmi5, LTI 1.3, QTI 2.x/3.0,
Caliper, Common Cartridge, CLR 2.0, Open Badges 3.0, OneRoster 1.2, CASE, h5p and W3C VC 2.0**. Its
`package.json` wires `lrsql` as its xAPI backend through podman-compose, so the pairing is real code
rather than a claim.

🔴 **Two stars.** 🔵 Recorded here because it is the only address found that covers the standards
surface this shelf cares about in one place, and because its own README is unusually honest — it
states plainly that it is *"not affiliated with, endorsed by, or certified by 1EdTech, ADL/ADLNet,
W3C"* and that it produces *"conformance assessments, not official certification."* 🟡 **Do not quote
it to a client as a conformance guarantee.** Watch it; re-date it next pass.


# Education vertical platforms — real systems to customise with AI on top

**🆕 Pass `p395` · reads and commit both 2026-10-23.** 🔴 **A constraint that lands directly on this
shelf's headline pattern.** `p394` shelved **LAMB** on the strength of its publishing into **Moodle as
an LTI external tool** — so the LTI layer is load-bearing for the platform story here, and this pass
dated all 13 known LTI 1.3 addresses: [`lti-layer-dating`](../evidence/lti-layer-dating.2026-10-23-p395.tsv).
🟢 The maintained permissive set is **PHP, Node and Python** (`packbackbooks` 6 d, `ltijs` 9 d,
`lti-tool` 1 d, `django-lti` 2 d, `ltiauthenticator` 113 d). 🔴 **There is nothing live in Go or
Java** — `StevenWeathers/peregrine-lti` 679 d, `UOC/java-lti-1.3-core` 1,193 d, `macewan-cs/lti`
1,918 d. 🔵 **At procurement this is the question to ask before the licence question:** *what runtime
does the client's platform team own?* A Java shop cannot take an in-process LTI dependency from this
base at all, and should be quoted an HTTP edge instead (see `Pattern AC`).

🟢 **Re-confirmed independently, not inherited:**
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp)'s grant was re-read at the
payload this pass — **8,241 B at `master/LICENSE`**, *"OpenEduCat is published under the GNU LESSER
GENERAL PUBLIC…"* — which **agrees with this shelf's existing LGPL-3.0 row**. 🔵 Recorded because a
re-read that agrees is the only thing that makes a re-read that disagrees meaningful, and this shelf
has had several of the latter.

**🆕 Pass `p394` · reads 2026-10-22, committed 2026-10-23.** 🟢 **One addition, and it is the
EMEA-authored platform layer this shelf has been short of.** [`Lamb-Project/lamb`](https://github.com/Lamb-Project/lamb)
— **LAMB, Learning Assistants Manager and Builder** — 🟡 **GPL-3.0** (35,349 B, `sha256`₁₆
`17fe6d0ffa96`, read first-hand), **7,087 files**, HEAD **2026-10-20 — 2 d**. Teachers build LLM
learning assistants **with no code** and publish each one into **Moodle as an LTI external tool**; its
companion [`Lamb-Project/lamba`](https://github.com/Lamb-Project/lamba) is the **LTI activity module
for assignments graded by a LAMB assistant**. Authored by **Marc Alier (UPC Barcelona)** and **Juanan
Pereira (UPV/EHU)** and published in *Computer Standards & Interfaces*. 🔴 **Maturity caveat carried on
every LAMB row:** its own Moodle.org thread (Feb 2026) calls it *"at a very beta stage"* with *"a few
universities running pilots"*, so this is a **pilot base, not a ministry platform** — said here and in
the pattern, not only in the evidence file.

🔴 **Three grants in one tree, which is `p382`'s subtree axis and it matters at procurement.** Root
**GPL-3.0**; `lamb-kb-server-stable/` carries its own stock **GPL** payload; and `open-webui/` is a
**vendored third party** under verbatim **BSD-3-Clause** (1,510 B, `6c4b8d8034b9`). A root-only licence
read is wrong about this repository in both directions. 🔵 That vendored BSD payload is also the
specimen that exposed **`P459`**: this base's own grant gate was reading verbatim BSD-3 as
`granted: False`, because *"All rights reserved."* is line 2 of the BSD template.

🔴 **Also corrected on this shelf's neighbours:** `anastasasenov/bbmcps`, carried across these shelves
as one of nine Blackboard servers, is **not a Blackboard Learn integration at all** (deps `mcp` +
`sqlite3`, no Learn API surface; `blackboard://` is the *architectural pattern*). Blackboard goes
**9 → 8 addresses, 6 MIT + 2 dead + 0 ungranted**. See [`agents/top.md`](../agents/top.md).

**🆕 Pass `p393` · 2026-10-22.** Three additions, all from the new `pypi.org/simple/` index-dump
channel ([`compose/code/p393-pypi-index-channel/`](../compose/code/p393-pypi-index-channel/README.md)):
🟢 a **permissive LATAM-native LMS** (`now-lms`, Apache-2.0, Nicaragua) on the four-way decision, the
🟢 **Ed-Fi** K-12 data path for North America, and the 🔴 copyleft **QTI exchange** layer for EMEA
assessment migration. Region placements updated under *Regional fit*.

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md`](../archive/2026-10-22-p383-pre-rewrite/verticals-solutions.md).
All addresses and licences verified first-hand on this date —
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).
🆕 **`p386` adds the permissive-base row this shelf has been missing**, and corrects the MCP section
below: Blackboard and D2L both have verified MIT servers now.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p386.tsv).

🆕 **Pass `p392` · 2026-10-22.** Two of this shelf's sentences are **withdrawn and replaced**, both
of them absences this base held the refutation for in its own harvest log: the **interop boundary**
row (Python LTI 1.3 is in-process after all — `django-lti`, MIT, 2 days) and the **proctoring**
bullet at the end (two granted components, one clean). Both were found by the instrument built this
pass — [`gate-capability-absence`](../compose/code/p392-capability-absence/README.md) — rather than by
accident, which is the first time that is true of this error class.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p392.tsv) ·
[`channel-state`](../evidence/channel-state.2026-10-22-p392.tsv).

This shelf answers one question: **what existing system does the client already run (or could run),
and what can be bolted onto it?** Same role Odoo plays for ERP or OpenMRS for healthcare.

🆕 **`p389` adds a fifth answer to that question, and it is a different kind of answer: what if the
client runs nothing, and the *classroom itself* is the platform?** See
*[The generated classroom as a platform](#-p389--the-generated-classroom-as-a-platform-openmaic)*.
`p389` also **dates every base on this shelf** — 60 addresses, last-commit date read from the payload
at the real default ref — and the dates change two things below: a decade-dead lookalike sits at the
obvious ERP address, and the Canvas row needs a sentence it did not have.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv).

## Choosing the base: the four-way decision

| if the client needs… | base | licence | the catch |
|---|---|---|---|
| **To own closed extensions to the platform itself** | [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | Smaller plugin ecosystem than Moodle; more build, less assemble. **The only permissive major LMS.** |
| **The widest plugin ecosystem and the largest talent pool** | [Moodle](https://github.com/moodle/moodle) | 🟡 GPL-3.0 (`COPYING.txt`) | Copyleft on anything linked. Extend through web services / the MCP plugin, not by patching core. |
| **MOOC scale, cohort analytics, deep data control** | [Open edX](https://github.com/openedx/edx-platform) + [tutor](https://github.com/overhangio/tutor) | 🔴 AGPL-3.0 | AGPL reaches **hosted** use. Build XBlocks and LTI tools; keep proprietary logic the other side of the boundary. |
| **🆕 `p389` No incumbent platform at all, and lessons needed now** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** | Not an LMS: no enrolment, no gradebook of record, no SIS. You get the *teaching surface* and you still owe the system of record. See the section below. |
| **🆕 `p390` To *ship* a modified platform, not host one** | [OLI Torus](https://github.com/Simon-Initiative/oli-torus) | 🟢 **MIT** | **The only permissive answer on this shelf, and the catch is staffing, not licensing.** Carnegie Mellon Open Learning Initiative's courseware engine: authoring + delivery, adaptive scripted activities, per-objective mastery reporting, LTI 1.3 delivery into a host LMS. Every other base of comparable scope here is GPL/AGPL, so this is the row to reach for when the deliverable is **software the client redistributes or embeds in a product**. 🔴 **Elixir/Phoenix + PostgreSQL** — a genuine staffing constraint; cost the hiring before proposing it. 🔴 Slug trap: `CMU-OpenLearning/oli-torus` does not resolve. Dated **2026-10-22**. |
| **🆕 `p393` To ship a small permissive LMS, in Spanish, with billing already in it** | [now-lms](https://github.com/bmosoluciones/now-lms) | 🟢 **Apache-2.0** | **21 ★** and no multi-tenancy claim. A Flask application a studio can read in a day — which is the point — but not a ministry platform. |
| **North American higher-ed integration reality** | [Canvas LMS](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0, open-**core** | The published tree ≠ the commercial ecosystem. Scope integrations against the real tenant, not the repo. 🆕 `p389` **And the published tree is also *older than it looks*: `master` last moved 2026-04-30 — 175 days — while the `stable/*` branches move.** Read the API surface off the tenant, and if you must read it off the repo, say which ref. 🟡 🆕 `p390` **Dating caveat, so nobody demotes Canvas off a bad read:** its `master` last moved **2026-04-30 — 175 days**, but Canvas **ships from tags** (`v5.14.2` current), not from the default ref. For any tag-releasing project, a last-commit-on-default-ref date under-reports maintenance; check `git ls-remote --tags` before calling it stale. |

### Regional fit
- **LATAM / Iberia:** 🆕 `p393` **the permissive option now exists and it is regional:**
  [now-lms](https://github.com/bmosoluciones/now-lms) (🟢 **Apache-2.0**, © BMO … S.A., **Nicaragua**;
  676 files, 505 commits, HEAD **2026-08-31**) is the only Spanish-language LMS on this shelf a studio
  can fork and ship **closed**. Use it for SME and pilot delivery; keep Chamilo for public-sector scale.
  [Chamilo](https://github.com/chamilo/chamilo-lms) (GPL-3.0) — strongest
  Spanish/Portuguese public-sector base. [academico-sis/academico](https://github.com/academico-sis/academico)
  (MIT) for SME-scale administration with Spanish built in.
  🆕 `p387` For **Brazil specifically**, the base a municipal engagement will already be running is
  [portabilis/i-educar](https://github.com/portabilis/i-educar) (GPL-2.0-or-later, **real default
  ref `2.12`**) — see the administration table below — and the agent tier now has three granted
  LATAM-native options on [`agents/top.md`](../agents/top.md),
  including one that ships **as an Open edX plugin** rather than as a separate app.
- **EMEA public sector:** [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) (GPL-3.0, default ref
  `release_11`) and [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0, Switzerland).
  🆕 `p393` For **assessment migration**, which EMEA procurement is beginning to specify as QTI 3.0:
  [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0** — run it
  as a batch tool at arm's length, never linked), from the lab of **Cito, the Dutch national assessment
  institute**. For a **Swiss university** engagement,
  [Dathis/swiss-moodle-mcp](https://github.com/Dathis/swiss-moodle-mcp) (🟢 MIT) already speaks ZHAW,
  FHNW, ETH and EPFL Moodle with **SWITCH edu-ID** user-held authentication — 🔴 but at **0 ★** and
  self-described as an unofficial student project, so it is a pilot reference, not a dependency.
  [Serlo](https://github.com/serlo/serlo.org) (Apache-2.0, Germany) and
  [Richie](https://github.com/openfun/richie) (MIT, France) for content and catalogue.
- **APAC:** Moodle itself is Australian in origin; [netless-io/flat](https://github.com/netless-io/flat)
  (MIT) for live online classrooms.
- **Low-connectivity anywhere:** [Kolibri](https://github.com/learningequality/kolibri) (MIT,
  default ref `develop`) — offline-first by design, not as a degraded mode.
- **K-12 administration anywhere:** [openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
  (GPL-2.0, default ref `master`) — the student-record half that no permissive base supplies.
- 🆕 `p393` **North America K-12 data integration:** the standard is **Ed-Fi**, and the granted client
  is [edanalytics/edfi_api_client](https://github.com/edanalytics/edfi_api_client) (🟢 **Apache-2.0**,
  stock 11,357 B, HEAD **2026-10-06 — 16 d**). The **Canvas / Google Classroom / Schoology → Ed-Fi**
  extractors exist at [Ed-Fi-Exchange-OSS/LMS-Toolkit](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit)
  (🟢 Apache-2.0) 🔴 **but that repository was ARCHIVED by its owner on 2025-03-10 and is read-only** —
  port its field mappings, never depend on it.

## 🔴 The sovereign-stack story in EMEA, corrected

The previous pass carried a headline that **openDesk Edu** was deployed in **8,600 German schools**
and then downgraded it to "traces to a single news item with no official confirmation". **This pass
re-ran the search and the downgrade stands — in fact it goes further:**

- What is **confirmed**: openDesk is a free and open-source productivity suite from **ZenDiS** (the
  German Center for Digital Sovereignty in Public Administration); **v1.0 released 20 Oct 2024**.
  ZenDiS works with France's **DINUM** on the French equivalent **LaSuite**, and the two agencies
  added videotelephony, note-taking and SSO to both suites in **100 workdays**.
- What is **not confirmed**: **no school deployment of openDesk appears in any source found this
  pass.** Named users are public-administration bodies (BWI GmbH for the Bundeswehr, the ÖGD public
  health service). Germany's **DigitalPakt Schule** (€6.5bn school infrastructure) is a separate
  programme and is not evidence of openDesk in schools.
- **How to use it anyway:** the *pattern* is real and sellable even if the school number is not —
  **ILIAS (learning) + OpenProject (collaboration) behind a single SSO**, all open source, all
  EU-hosted. That is the sovereign education stack an EMEA public-sector client will ask for. Sell
  the architecture; do not quote the 8,600.

## Student information and administration

| platform | repo | default ref | licence | fit |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 `19.0` | 🟡 LGPL-3.0 | Odoo-based SIS/ERP: admissions, curriculum, fees, library, hostel. The Odoo ecosystem is the reason to pick it — AI modules can be ordinary Odoo addons. |
| **Academico** | [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 MIT | Laravel, Spanish + French built in, SME-scale: courses, enrolments, scheduling, reports. |
| **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 `master` | 🟡 GPL-2.0 — 🔴 grant at **`docs/License.txt`**, not at any root path | 🆕 `p384`. The K-12 default: enrolment, attendance, grades, scheduling, parent/student portals. GPL-2.0 is survivable the Moodle way — reach it over its API, never link. 🔵 A root-only licence read reports this repo as ungranted; it is not. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 AGPL-3.0 (`license.txt`) | Only where the client already runs ERPNext — then the student record and the finance record are one system. |
| **i-Educar** 🆕 `p387` | [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 GPL-2.0-or-later (`2.12/LICENSE`, 18,092 B) | 🟢 **The LATAM row this table was missing.** Brazil's largest free education software — municipal student records, enrolment, grades — deployed by Brazilian municipalities at scale and maintained by Portabilis plus a community. 🔴 Its default ref is the version branch **`2.12`**: clone and read the grant there, not at `main` or `master`. Reach it over its API; keep AI alongside it, never inside it. Sibling `i-diario` (classroom diary) is **AGPL-3.0** — different grant, same organisation. |

### 🆕 `p386` — the permissive ERP **base**, since the permissive education ERP does not exist

Every row in the table above is copyleft except `academico` (MIT, SME-scale). The prescribed ERP/CRM
research leg was run directly at that gap. **It does not close it** — no education-specific
permissive ERP was found, which *confirms* the structural claim on
[`repos/foundations.md`](../repos/foundations.md) — but it returns three permissive bases, all three
licence payloads read first-hand this pass:

| base | real default ref | licence | what you get, and what you build |
|---|---|---|---|
| [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) | 🔴 **`master`** | 🟢 **MIT** *(1,077 B, "Copyright 2010-2025, Webkul Software"; `composer.json` also declares `"license": "MIT"`)* | Laravel 13 + FilamentPHP 5 modular ERP **with a plugin system**: accounting, inventory, HR, CRM, projects, and a Filament admin panel a client's staff can actually use. 🔴 **No education module** — admissions, curriculum, fees, attendance and transcripts are **your build**. |
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** *(version branch; no `main`)* | 🟢 **MIT** *(1,078 B, same Webkul holder)* | The **admissions funnel** as a CRM: lead → applicant → enrolment, with the pipeline, activity log and email already built. The piece an SIS always lacks and a school always asks for. |
| [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | 🔴 **`trunk`** | 🟢 **Apache-2.0** *(11,906 B; `NOTICE` 166 B, "Copyright 2001-2026 The Apache Software Foundation")* | The ASF alternative: accounting, CRM, manufacturing, order management. 🔴 Developer-facing and heavy — pick it for ASF governance and longevity, not for time-to-first-demo. 🆕 `p389` **Dated: `trunk` committed 2026-10-22 — 0 days. The ASF-longevity argument holds up.** 🔴 **But write the `-framework` suffix into the proposal.** [apache/ofbiz](https://github.com/apache/ofbiz) — the address anyone guesses — resolves, carries a valid Apache-2.0 grant, and its `trunk` **last moved 2017-02-12, 3,539 days ago**. It is the retired monolith. A client engineer who checks the obvious address finds a nine-year-dead tree and concludes the recommendation was careless. |

🔵 **What this changes in a pitch.** [OpenEduCat](https://github.com/openeducat/openeducat_erp)'s
**LGPL-3.0** used to be the only road to an open-source education ERP, so it was not a decision. It
is now a **trade against a named alternative**:

- **Take OpenEduCat (LGPL-3.0)** → admissions, curriculum, fees, library and hostel exist today, on
  the Odoo ecosystem, and AI features can be ordinary Odoo addons. You accept LGPL on the modules
  and the Odoo version-branch cadence (`19.0`).
- **Take Aureus (MIT) + Krayin (MIT)** → the client owns every line, including the education
  modules you write. You are costing **admissions, curriculum, fees, attendance and transcripts as
  a build**, on a base whose plugin system is designed for exactly that.

🔴 **Do not sell the second option as "an open-source education ERP."** It is a permissive ERP plus
a scoped education build, and the honest version of that sentence is the one that survives the
client's own technical review.

🟡 **Still not found, and still the clearest build-vs-buy opening in the rotation:** no open-source
Brazilian or Mexican academic-management system. Aureus + Krayin is now the most *defensible*
starting point for one — Laravel, MIT, and `academico` (MIT, Spanish-native) already proves that
stack fits the region's SME school market.

## Content, assessment and media layers

| layer | platform | licence | note |
|---|---|---|---|
| Interactive content | [H5P](https://github.com/h5p/h5p-php-library) | 🟡 **GPL-3.0** | Embeds in Moodle, Open edX, Canvas, Drupal, WordPress. 🔴 Widely mislabelled MIT. Treat as runtime content, not linked code. |
| 🆕 `p393` H5P **inside Open edX** | [edly-io/h5pxblock](https://github.com/edly-io/h5pxblock) | 🟢 **MIT** *(1,064 B)* | 🟢 **The permissive way to get H5P content into an AGPL platform.** Self-hosted H5P player as an XBlock — HEAD **2026-10-16 — 6 d**, 82 commits, 23 releases, **19 ★**. 🔵 Note the licence shape, which is `p390`'s firewall again: the **content library** above is GPL-3.0 and the **platform** is AGPL-3.0, but this bridge is MIT, so the part a studio writes against stays permissive. |
| 🆕 `p393` QTI assessment exchange | [vosslab/qti_package_maker](https://github.com/vosslab/qti_package_maker) (🟡 **LGPL-3.0**) · [Citolab/qti-convert-python](https://github.com/Citolab/qti-convert-python) (🔴 **GPL-3.0**) | 🟡 / 🔴 copyleft | **Write** QTI packages for Canvas/Blackboard, and **convert** QTI 2.x ↔ 3.0. The assessment-portability layer this shelf had no row for. 🔴 Neither is permissive: use the LGPL one as a **linked dependency** and the GPL one as an **arm's-length batch tool**. 🔴 A third family — PyPI's `timeback-qti` / `-oneroster` / `-caliper`, 147 releases, MIT **declared** — has an **unresolvable source repository**, so it is listed here only as a warning, not an option (`Gap 393-B`). |
| Structured pedagogy | [Oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | Misconception-aware lesson branching. Permissive and pedagogically serious — unusual combination. |
| Open-response assessment | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 | Peer + self + staff assessment rubrics. The place an LLM grader must plug in to stay auditable. |
| Lecture capture | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 ECL-2.0 | Video pipeline → the transcript corpus every education RAG build needs. |
| 🆕 `p390` Self-hosted video delivery | [Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube) | 🔴 **AGPL-3.0** | Federated (ActivityPub) video hosting — the option when lecture video must stay off YouTube and off a hyperscaler, which is a recurring EMEA public-sector requirement. 🔴 **Network copyleft: hosting it as a service for the client triggers source obligations** — fine for a public institution, usually not for a commercial product. Dated **2026-10-16**. 🔴 **A wrong-slug trap worth naming, because it inverts the licence:** [`PeerTube/PeerTube`](https://github.com/PeerTube/PeerTube) also resolves, is **3,660 days stale**, and reads **GPL-3.0** — so a careless licence read off that slug gets the *wrong grant* for the project, not merely a stale one. The canonical owner is `Chocobozzz`. |
| Live classroom | [netless-io/flat](https://github.com/netless-io/flat) | 🟢 MIT | Whiteboard, recording, real-time session. |
| Interop boundary | 🆕 `p392` [academic-innovation/django-lti](https://github.com/academic-innovation/django-lti) (**Python**) · [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (Node) · [lti-tool/lti-tool](https://github.com/lti-tool/lti-tool) (Node, **serverless**) · [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) (PHP) | 🟢 **MIT / Apache-2.0 / MIT / Apache-2.0** | **The copyleft firewall, and as of `p392` it is maintained in THREE languages including Python.** 🆕 `p392` `django-lti` (🟢 MIT, 1,098 B, HEAD **2026-10-20**, PyPI v0.10.1) puts LTI Advantage **inside** a Django agent — one middleware, no second runtime — so `p391`'s *"the edge must be Node or PHP in front of the agent"* is withdrawn; `lti-tool/lti-tool` (🟢 MIT, HEAD **2026-10-20**, npm `@lti-tool/core` v1.3.2) is the **serverless** Node option for Lambda / Cloudflare Workers, where `ltijs` assumes a long-running process with Mongo. 🔴 `p390` dated the standards-body reference copy at 2,332 days and concluded the boundary had no installable implementation; that was wrong. **`ltijs`** — npm v7.0.7, **207 versions, published 2026-10-06**, HEAD 2026-10-13 — and **`packbackbooks/lti-1p3-tool`** — packagist v6.4.4, **68 versions, published 2026-09-23**, HEAD 2026-10-16 — are both live, both Apache-2.0, and either one keeps permissive code the right side of a GPL/AGPL platform boundary without linking to it. Prefer **`ltijs`** unless the client's platform work is already PHP. 🔴 Cite [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) as the **spec reference only** — 2,333 days, and `IMSGlobal/lti-1-3-php-library` is the same project at a renamed org (identical HEAD `3a192de`). 🔴 There is **no maintained Python LTI library**, so the edge is Node or PHP in front of a Python agent. Full note in [`repos/foundations.md`](../repos/foundations.md). |
| Local-first tutoring workspace | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** | 🆕 `p386`. Self-hosted, block-based adaptive workspace: PDF in → notes, flashcards, quizzes and an adapting tutor out, with **FSRS** scheduling, a knowledge graph and cognitive-load detection. Runs on local open-weight models — **no API key, no data leaving the host**, which is the answer to a DPO who will not approve an external model call at all. |
| Campus LLM gateway | [LibreChat](https://github.com/danny-avila/LibreChat) | 🟢 MIT | Multi-provider, SSO, quota, audit log. The audit log is what gets a deployment past a university's data-protection officer. |
| Courseware platform | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🆕 `p384`. Django courseware with autograding, flexible access rules and per-student statistics. Course-scale and permissive — the base when the client must own the platform code but does not need an institutional LMS. |
| **Agent-native teaching OS** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | 🔴 **AGPL-3.0** (`main`) · 🟢 MIT at tag `v0.1.0` | 🆕 `p385`. The **inverse** of every other row here: instead of bolting an agent onto an LMS, the classroom itself is an MCP server (~50 tools) and the agent is bring-your-own. Courses, lessons, FSRS flashcards, graded exercises, and a persistent learner-memory layer (`get_context` / `get_learner_brief`) that survives a change of model or session. 🔴 **v1 is single-machine and unauthenticated** — a pilot substrate, not a tenant-ready platform. AGPL reaches hosted use, so a client deployment must either accept that or pin the MIT `v0.1.0` tag and forgo upstream. |
| **Curriculum prerequisite graph** | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 **ODbL** | 🆕 `p384`. 1,930 micro-topics, 4,102 prerequisite edges, 9 subjects; aligned to NGSS, Common Core, UK National Curriculum, Australian curriculum. 🔴 **Share-alike database licence, not a code licence** — ground a tutor on it (§4.3 *Produced Work*, attribution only); do **not** ship an extended taxonomy (§4.4 *Derivative Database*, share-alike). See **Pattern H**. |

## 🟡 MCP has reached the LMS — and this is new as of 2026

This did not exist a year ago and it changes the integration story:

- 🆕 `p387` **Moodle, the tenancy layer — and this is the part a client-ready deployment needs
  before any MCP server:** [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager)
  (GPL-3.0-or-later, granted in `version.php`, release **5.1.1**) is a **multi-tenant AI backend**
  offered as the alternative to Moodle 4.5's own single-tenant AI subsystem: `aitool` subplugins
  connect providers (ChatGPT, Gemini, Dall-E, **Ollama** for on-premises), `aipurpose` subplugins
  bind a purpose to a provider **per role**, with per-role rate limits, per-tenant enable/disable,
  usage monitoring and capability-gated teacher visibility of student prompts. 🔵 The same project
  is also published at `mebis-lp/moodle-local_ai_manager` — **identical HEAD sha, one project, two
  addresses.** 🔴 Its own README warns it is **not compatible with core-AI-subsystem plugins and
  vice versa**: choosing it is an architectural fork in the road, taken once, early.
- 🆕 `p387` **Open edX, first-party AI extension point:**
  [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) (AGPL-3.0-only)
  is the platform org's own AI extensibility framework — **experimental**, but it is the contract to
  build against instead of forking `edx-platform`. Pair it with
  [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) for the agent-facing surface.

- **Moodle, first-party path:** the **`webservice_mcp`** plugin in **Moodle's own plugin directory**
  (and the Moodle Marketplace) exposes Moodle's external functions as **MCP tools over JSON-RPC
  2.0**. Supports **Moodle 4.5–5.2**, latest release **23 Jul 2026**, gated on the
  `webservice/mcp:use` capability. Configured inside Moodle — no fork, no patch, **no GPL exposure
  for the agent on the other side of it.**
- **Canvas, community path:** [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) (MIT)
  and its fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT, adds office
  hours, syllabus read/write, student groups, course-content copy).
  [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) advertises 54
  tools and Streamable HTTP; it has **no licence file**, but `package.json` declares
  `"license": "MIT"` — 🟡 **manifest-only MIT**, usable if you record the manifest line and ask for
  the file.
- 🆕 `p386` **Blackboard, community path — and it is no longer empty.** Nine addresses probed,
  **6 MIT grants read first-hand**, 1 ungranted, 2 dead. 🟢 **[nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
  (MIT) is the only institution-grade LMS MCP server on any of these shelves**: official Blackboard
  Learn REST API, OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log,
  Prometheus `/metrics`, 40 tools including **grade write-back** (maintainer self-claims, read not
  executed). The other five —
  [Mattlo0546](https://github.com/Mattlo0546/blackboard-mcp),
  [alanwtom](https://github.com/alanwtom/blackboard-mcp),
  [lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp) (ref **`tcd`**),
  [felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp),
  [Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp) (ref **`master`**) — are
  **student-side**: they ride the signed-in user's own browser SSO session. 🔴 Granted, useful, and
  **not deliverable to an institution**.
- 🆕 `p386` **Brightspace / D2L — six addresses, six MIT grants.**
  [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) is the fullest
  (TOTP/OAuth/browser auth strategies, retry + circuit-breaker + cache, **opt-in writes**);
  [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) is the
  upstream of a fork family whose copies publish **byte-identical** licence payloads, so count it
  once. 🔵 **All six are student-side** — an institution-grade D2L server is the one genuine
  greenfield contribution left on this platform.
- **No official server** from Instructure, Moodle HQ, Anthology/Blackboard or D2L. 🟡 Verified gap —
  every server named on this shelf is community-built.
- 🔴 [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) is **UNGRANTED** — no licence file
  *and* no `license` field in its `pyproject.toml`. Use the plugin-directory route for Moodle:
  [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) has no root
  licence file either, but its `version.php` carries the full **GPL-3.0-or-later** header that
  Moodle requires of every plugin, so it *is* granted.

## 🆕 `p388` — The parent portal is a platform surface, and it was missing from this shelf

This shelf asks *"what does the client already run, and what can be bolted onto it?"* For every
platform below it answered that for **the learner, the teacher and the administrator**. It never
answered it for **the parent** — yet in K-12 the parent portal is a shipped feature of every SIS and
the one surface families actually log into.

| platform | server | ref · HEAD | licence | what it bolts on |
|---|---|---|---|---|
| **Infinite Campus** (Campus Parent) | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS parent portal on this shelf.** 20 tools: schedule, assignments (`missingOnly`), grades + 14-day recent window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, messaging from three sources. Linked districts auto-discovered via **CUPS SSO**; `FeatureDisabled`-aware, so a district that has switched a module off degrades instead of erroring. **47 npm releases**, → 2026-10-19. |
| **Canvas** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | 18 `canvas_*` tools held to **the read-only observer surface** (`canvas_list_observees` is the hinge) plus student self-access; four auth modes in priority order; hardened file download (host-pinned, directory-confined, no symlink writes, `0600`). **43 releases**, → 2026-10-16. |

🔵 **Why it belongs on the *verticals* shelf and not only on the agents shelf.** Infinite Campus is a
**major North American K-12 SIS** that this base has only ever been able to name as a proprietary
system with nothing attachable. It now has a granted, maintained, MIT integration surface — so the
"what can be bolted on" answer for a US K-12 district changes from *nothing* to *the parent portal*.

🔴 **The boundary that decides the engagement, and it is not a licence boundary.** Both servers
authenticate as **a person** — a parent's own token, OAuth, or a scraped session. Deployed by a family
for their own child, that is the parent exercising their own access. **Hosted by a studio on behalf of
a district, the same call becomes an institutional disclosure of an education record and FERPA
governs it.** The code is identical; the obligation is not. 🆕 `Pattern P` in
[`compose/patterns.md`](../compose/patterns.md) is built around that line, and it is the same
tenancy problem `p386` found for student-side LMS servers — **the parent surface inherits it
unchanged**, which is worth knowing before a district pilot is scoped.

## 🆕 `p388` — Canvas: the integration surface reordered, and a FERPA mode shipped as a feature

`p387` recorded that the richest Canvas server (`canvas-mcp-server`, 54 tools) had not shipped since
**2025-06-27**. For a client engagement that mattered and there was nothing better to recommend.
There is now:

- 🟢 **[bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp)** — `main` · `34e6156`,
  🟢 **MIT** (1,070 B), `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22
  (today)**. **187 tools on the teacher/admin surface**, including the ones an institution asks about
  and demos usually lack: gradebook *history*, quiz **accommodations**, grading standards, content
  exports and migrations, outcomes, analytics, appointment groups, plus **link audit**,
  **accessibility audit** and **grade projection**. Three deployment modes (stdio, HTTP, library
  import). 🟢 **It ships a FERPA mode.** That is the first time on these shelves that an education
  compliance regime appears as a *product feature* of an open-source component rather than as a
  caveat this base has to supply — and in a procurement conversation it is worth more than the tool
  count.
- 🟢 **[Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local)**
  (`c7e5725`) and its remote twin
  **[`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server)** (`8e424f1`) — 🟢 **MIT**
  (1,091 B each), **209 tools on the student surface**, split deliberately into a **Local Edition**
  that opens no port and a **Remote Edition** on ngrok with OAuth 2.1 and multi-computer failover.
  🔴 The Remote Edition exposes a **public HTTPS address**: a school's decision, never a default, and
  not a thing to leave switched on in a pilot.

🔵 **Pick by persona, not by tool count.** 187 (teacher/admin) vs 209 (student) vs 20 (parent) is
**scope**, not quality: three different people reading the same institutional data. An engagement
usually needs one, occasionally two, and should deploy them separately — the FERPA posture differs
per surface, and a single server covering all three personas would be the hardest version of this to
get approved.

🟢 **And a wider Moodle surface than `webservice_mcp`:**
[gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) — `main` · `7962e49`, 🟡 **GPL-3.0**
(284 B short-form notice) — a Node client and CLI against Moodle Core web services **plus the MoodlIA
plugin, a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser
path. GPL survives here for the same reason it does for `webservice_mcp`: the agent reaches it over
REST, it is not linked.

## 🆕 `p389` — The generated classroom as a platform (OpenMAIC)

[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 🟢 **MIT**, Tsinghua University, real
default ref `main` @ `269fde2d991f`, **committed 2026-10-22 (0 d)**, ~41.3k ★. Grant read from the
payload: `LICENSE` is stock MIT text, `package.json` declares `"license": "MIT"`.
🔴 **A 2026 third-party review of this project reports it as AGPL-3.0 with paid commercial licensing.
That is false** — see [`agents/top.md`](../agents/top.md#-two-licence-traps-that-a-badge-read-would-miss).

**Why it belongs on *this* shelf and not only the agent shelf.** Every other row here is a system of
record that AI gets bolted onto. OpenMAIC inverts it: the artefact is a **classroom** — narrated
slides, an AI teacher with a voice, teaching assistants, simulated classmates, auto-graded quizzes,
HTML interactives, a shared whiteboard — generated from a topic or an uploaded document, and then
*taught*. It is a Next.js 16 / React 19 / TypeScript application on **PostgreSQL 16**, self-hosted
with Docker, and it has the three properties that separate a platform from a demo:

| property | what it is | why an institution needs it |
|---|---|---|
| **Server-first generation** (v1.2.0) | Generation runs on the server, survives closed tabs and restarts; the web app and the API share one pipeline | A teacher who closes a laptop does not lose a lesson. The demo-grade alternative generates in the tab. |
| **Central model governance** | Every AI use is a named **slot** in `openmaic.yml` (outline, slide content, TTS, web search, …), each pinned to a declared provider, keys referenced as `${VAR}` from `.env.local`; a capability is switched off with `video: null`, and the server can be configured to **forbid user-supplied keys** | This is the artefact a district's AI policy is actually written against: *which model saw student input, under whose contract*. Almost nothing else in this base can answer that in one file. |
| **Export to one offline HTML file** | A finished classroom exports as a single self-contained HTML that plays the lesson, or as a PPTX that keeps every scene | The low-connectivity story (`Pattern D`) **and** the procurement story: a reviewer can be sent the lesson without being given access to the system. |

🟢 **Local inference is a supported path, not a fork:** **Lemonade** for local models and **FunASR**
for local ASR, so a deployment that may not send audio or text off-premises has a configuration
rather than a rewrite. 🟢 **Provenance:** grew out of **MAIC**, run inside Tsinghua and validated on
**700+ students**; paper in **JCST 2026**. 🟢 **Security handled as product work** — five releases
since September 2026 carry SSRF, DNS-rebinding, access-token-expiry and provider-redirect fixes under
published GHSAs, which is a maturity signal almost nothing else on the agent shelf has.

🔴 **What you still owe, and it is the whole administrative half.** No enrolment, no gradebook of
record, no transcripts, no SIS, no LTI story stated. It is a **teaching surface**, so in an engagement
with an incumbent LMS it sits *beside* Moodle/Canvas/Open edX as a content and delivery tool, and the
system of record stays where it is. 🔴 **Pin the ref.** Head is **v1.3.0-rc.1** (knowledge base,
2026-10-22) and the project states **breaking upgrade conditions with no rollback below that
release**; a pilot pins **v1.2.1** (2026-10-18). 🔴 **Operational floor:** Node ≥ 22.19, pnpm ≥ 10,
PostgreSQL 16, a long-running server — Vercel is capped at the 1.1.x line, so "we'll put it on Vercel"
is a downgrade, not a deployment.

🔵 **Where it lands by region.** Origin is **APAC** (China), the interface is EN + zh-CN, and the
provider catalogue is built for a market that includes DeepSeek and Kimi alongside OpenAI, Anthropic
and Gemini. For an engagement under **EU AI Act** or **FERPA** constraints the slot-pinning and
forbid-user-keys controls are an asset, and the *data-residency* question is answered by the local
Lemonade/FunASR path — but the assessment features (auto-graded quizzes, mastery signals) are exactly
what Annex III and Vietnam's Decision 33/2026 treat as high-risk, so human review of any consequential
score is a build item, not a setting. See [`intel/trends.md`](../intel/trends.md).

## What is *not* available as open source, and matters

An informed gap, recorded so silence is not mistaken for coverage:

- **No open-source equivalent of Khanmigo or LearnLM.** The pedagogically-tuned model layer is
  closed across the board; the open supply is agents and scaffolding over general models.
- **No open-source Brazilian or Mexican academic-management system was found.** A targeted search
  for SIGAA source and for Portuguese/Spanish-language academic management on GitHub returned
  nothing usable. `academico` (MIT) and Chamilo are the closest fits, neither region-native at
  university scale. See [`intel/market.md`](../intel/market.md) — this is the clearest
  build-vs-buy opening in the current rotation.
- **No official Instructure or Moodle-HQ MCP server** (community only, as above).
- 🔴 🆕 `p392` **~~Proctoring and AI-detection have no credible permissive open-source option~~ —
  WITHDRAWN. There are two granted components, and one of them is clean.**
  [`mdestafadilah/proctoring.js`](https://github.com/mdestafadilah/proctoring.js) (🟢 **MIT**, 1,069 B,
  manifest agrees, HEAD **2026-09-28**, npm v0.5.1) does tab-switch, camera, **face** (face-api on
  TF.js, in-browser), audio and **virtual-camera / loopback / screen-share** detection, and states
  *"nothing leaves the page unless you set `backend.endpoint`"*.
  [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) (🔴 **grant
  CONFLICT** — Apache-2.0 payload, ISC manifest and npm; HEAD **2026-10-13**, 398 commits) is the
  bigger codebase but ships **lockdown and event telemetry only** — its README marks object
  detection, multi-face and eye tracking *"(To be Done)"*.
  🔵 **What survives of the old sentence, and it is the half worth saying to a client:** the
  *liability* boundary is real and unchanged — an exam decision driven by either component makes the
  client a **deployer of an Annex III high-risk system** (standalone obligations from **2 Dec 2027**).
  The absence of code was never what made proctoring expensive; the obligations are. 🟢 So the honest
  advice flips from *"we cannot build this"* to **"we can build this, and here is what it commits you
  to"** — see [`compose/patterns.md`](../compose/patterns.md) `Pattern Y`. Full rows on
  [`repos/foundations.md`](../repos/foundations.md).
