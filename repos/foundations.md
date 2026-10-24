---
industry: education
region: Global
updated: 2026-10-24
---

## 🆕 `p420` · 2026-10-24 — **The three Frappe platforms this base recommends were one lowercase filename away from being graded ungranted. 🟢 All three grant at `license.txt`: ERPNext GPL-3.0, Frappe LMS AGPL-3.0-or-later, Frappe Education. 🔴 And five Moodle AI plugins carry their GPL grant ONLY in source headers — one of them on no other channel at all.**

🔵 Every read below is first-hand on **2026-10-24**, at a SHA or a ref resolved by `git ls-remote`.

### 🟢 The grant-channel audit over the recommendation shelves — four channels, and the root path is the weakest

🔴 **19 addresses on these shelves return no grant at any of 15 root paths.** Run through the deep
ladder (25 paths), the manifest channel (7 manifests), the README channel (`p288`) and the
file-header channel, **13 of the 19 are granted and the root path was simply the wrong place to look.**

| address | where the grant actually is | licence, as measured |
|---|---|---|
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **`license.txt`** — lowercase, root; `LICENSE` → `404` | 🟢 **GPL-3.0** (`package.json` agrees: `"license": "GPL-3.0"`) |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`license.txt`** | 🟢 **AGPL-3.0-or-later** (`package.json` agrees) |
| [`frappe/education`](https://github.com/frappe/education) | 🔴 **`license.txt`** | 🟢 **GPL-family payload present**; no manifest field |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟡 **README + `index.php` header** — no root licence file | 🟡 **GPL** — *"openSIS is an Open Source Project licensed under the GNU General Public License"*, and `index.php` carries *"This program is released under the terms of the GNU General Public License"* |
| [`marcusgreen/moodle-qtype_aitext`](https://github.com/marcusgreen/moodle-qtype_aitext) | 🟡 README + `version.php` | 🟡 **GPL-3.0-or-later** |
| [`marcusgreen/moodle-tool_aiconnect`](https://github.com/marcusgreen/moodle-tool_aiconnect) | 🔴 **`version.php` ONLY** — its `readme.md` contains no licence word | 🟡 **GPL-3.0-or-later**, on a single channel |
| [`lmscloud-io/moodle-aiprovider_openaicompatible`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) | 🟡 README (*"GNU GPL v3 or later"*) + `version.php` | 🟡 **GPL-3.0-or-later** |
| [`bycs-lp/moodle-block_ai_chat`](https://github.com/bycs-lp/moodle-block_ai_chat) | 🟡 `version.php` | 🟡 **GPL-3.0-or-later** |
| [`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) | 🟡 `version.php`; 🔴 its README's `## License` section is **empty** | 🟡 **GPL-3.0-or-later** — 🟢 **this shelf already says exactly this**, and the audit confirms it |
| [`TecFancy/dsh-deeptutor`](https://github.com/TecFancy/dsh-deeptutor) | 🟡 `package.json` only | 🟡 **MIT, manifest-only** — carried verdict confirmed |
| [`nanobpm/nano-ide`](https://github.com/nanobpm/nano-ide) | 🟡 `package.json` only | 🟡 **Apache-2.0, manifest-only** — carried verdict confirmed |
| [`patriciamar/ShinyItemAnalysis`](https://github.com/patriciamar/ShinyItemAnalysis) | 🟡 **`DESCRIPTION`** — the R convention, no root licence file | 🟡 **GPL-3** |
| [`philchalmers/mirt`](https://github.com/philchalmers/mirt) | 🟡 **`DESCRIPTION`** | 🟡 **GPL (>= 3)** |

🔴 **The Moodle plugin ecosystem is the load-bearing case, and it is systematic rather than sloppy.**
Moodle plugins **never** ship a root licence file; the grant lives in the GPL boilerplate at the top
of `version.php`. 🔴 **A root-path auditor marks the entire Moodle plugin ecosystem ungranted** — and
the correct verdict, **GPL-3.0-or-later**, is a *copyleft* obligation, so the error is not merely a
false negative: it would also let a studio mistake a plugin for permissive-ready if it ever flipped
to a badge read. 🟢 **`Gap 298` / `Gap 405-A` are untouched by all of this**: nothing here is
permissive, and the scarcity of a permissively-licensed SIS or LMS is confirmed on a **seventh**
independent channel this pass.

### 🔴 Six that survive all four channels — and the base already graded every one of them

`1EdTech/openbadges-specification` (`develop`) · `Daniel-ux1026/Tutor-Inteligente` ·
`Nutlope/llamatutor` · `gradescope/autograder_samples` · `savinoo/ai-grading-system` ·
`x-cookie/agent`.

🟢 **Not one is a new finding.** `agents/top.md` already carries `gradescope/autograder_samples` as
*"UNGRANTED AT ROOT"* with its two **vendored** `jh61b/LICENSE.txt` copies named; `llamatutor` (46
files) and `Tutor-Inteligente` (145) as ungranted **by full tree enumeration** — a stronger channel
than this pass's ladder; `x-cookie/agent` as *"ungranted on every arm"*; and `savinoo/ai-grading-system`
as `p417`'s `T98` specimen, badge over no payload. 🔴 **`gate-absence` exists precisely to stop an absence being republished as a discovery**, and it fired
on `p419`'s prose while `p419` was live (`Gap 420-A`), and this table is the honest
version: a **confirmation sweep**, not supply.

🟢 **One methodological upgrade worth adopting here.** Every grant above was re-read **at the commit
SHA**, not at a ref — a bogus 40-hex SHA returns `404`, so no alias can satisfy the channel
(`T106`). 🔵 That is strictly stronger than `ACTION p419-B`'s prescribed `ls-remote` remedy and needs
no second request.

## 🆕 `p419` · 2026-10-24 — **`p418` answered "what is this repository's licence?" with *a SET over subtrees*. 🔴 `p419` widens the question again: the set is over `(ref × path)`, because a repository can ship licensed and unlicensed applications on different BRANCHES. 🟢 And the ref layer of this file was swept against an authoritative channel — every claim holds.**

🔴 **Gates did not run** — `make hooks` executes code from this cloned repository and the host's
auto-mode classifier refused it (`[Code from External]`). Contracts honoured by hand;
`Gap 419-D` registers the un-run suite. **No claim below rests on a green gate.**

### 🔴 A foundational grant is resolved at a `(ref, path)` pair — and the default ref is not the repository

🟢 **`p418`'s Amendment 8 made the probe enumerate every licence-shaped path in one tree.** That is
necessary and it is **not sufficient**. [`piyushdhoka/GradeU`](https://github.com/piyushdhoka/GradeU)
is one product in three applications, **one per branch**, published as such in its own
`README.md:50-54`:

| ref | app | tracked paths | licence-shaped paths | manifest `license` |
|---|---|---|---|---|
| `main` *(default)* | Student site | 199 | 🟢 `LICENSE` — MIT `1 065` B `10e6b9c80b1b` | 🔴 absent (`"private": true`) |
| `teacher` | Teacher studio | 55 | 🔴 **NONE at any depth** | 🔴 absent (`"private": true`) |
| `admin` | Admin portal | 43 | 🔴 **NONE at any depth** | 🔴 absent (`"private": true`) |

🔴 **Amendment 8 run perfectly on `main` returns *"MIT, one grant, enumerated"* — and it is wrong
about two thirds of the product.** 🟢 **The correction is cheap and it is a one-line addition to
every probe this base runs:** `git ls-remote --heads` before the path enumeration, then enumerate
**per ref**. It needs no new channel, no API and no HTML.

🔵 **Why this is a foundations question and not a trivia question.** A foundation is chosen to be
built on. If the component a client engagement needs is the **teacher studio** or the **admin
portal**, the project's MIT badge — accurate on `main`, accurate on GitHub's sidebar — **grants
nothing for the code that would actually be used.**

### 🔴 The channel that keeps this invisible, measured with its controls

🟢 **`raw.githubusercontent.com` serves `master` and `HEAD` as ALIASES for the default branch even
when no such ref exists.** Three repositories, each with an authoritative `git ls-remote` beside it,
all read **2026-10-24**:

| repository | real `refs/heads` | `main/LICENSE` | `master/LICENSE` | `trunk/` · `develop/` · bogus ref |
|---|---|---|---|---|
| `piyushdhoka/GradeU` | `main`, `admin`, `teacher` — 🔴 no `master` | `200` `1 065` B `10e6b9c80b1b` | 🔴 **`200`, byte-identical** | `404` · `404` · `404` |
| `THU-MAIC/OpenMAIC` | `main` + 280 others — 🔴 no `master` | `200` `1 065` B `ba2525637432` | 🔴 **`200`, byte-identical** | `404` · `404` · `404` |
| `Gchism94/ai-tutor` | `main` only — 🔴 no `master` | `200` `1 070` B `3d5a24e51479` | 🔴 **`200`, byte-identical** | `404` · `404` · `404` |

🔴 **`p354`'s `gate-grant-path` asserts *"a BRANCH and a FILE, and both must resolve"* — and on this
channel the branch half cannot be falsified for `master` or `HEAD`.** 🟢 The authoritative channel
is `git ls-remote`, which this base already uses for identity (`gate-identity-online`) and which no
alias satisfies.

### 🟢 This file's own ref claims — swept, and they hold

🟢 **`repos/foundations.md` publishes ``ref `master` `` for [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp)
(lines 62 and 1786) and ``ref `develop` `` for [`luisricar-do/portugol-ai-tutor`](https://github.com/luisricar-do/portugol-ai-tutor).
Both verified on `git ls-remote` 2026-10-24: `aureuserp` has a real `refs/heads/master` at HEAD
`8f6e107`; `portugol-ai-tutor` has a real `refs/heads/develop` at HEAD `84ae17c`.** 🔵 Across all
six live shelves the sweep is **18 claims, 18 correct** — so the alias hazard is **latent on this
base, not live**, which is itself the result worth publishing: only an authoritative channel could
establish it, and no amount of `200`s could.

### 🟢 Two foundational MIT payloads at exactly `1 065` B — and the identity test that separates them

🟢 `GradeU`'s `10e6b9c80b1b` and `OpenMAIC`'s `ba2525637432` are **both exactly `1 065` B**; `cmp`
separates them at char 1, line 1. Four deltas sum to zero: **+3** B extra blank lines, **−1** B
missing terminal newline, **−2** B shorter holder name. 🔴 **`T101` therefore holds for a nameable
reason** — whitespace presentation and holder-name length trade byte for byte — and `p312`'s *a
length is not a template* with it.

🔴 **`T102`:** a line-based read of `GradeU`'s payload returns **`1 066`** B, because line-oriented
tools re-add the terminal newline the file lacks — the same off-by-one `p418` corrected on
`OpenMAIC`'s root. **Byte counts come from `wc -c` on raw bytes.**

### 🔴 The foundations scarcity, confirmed on a SIXTH channel

🟢 The `open source platform education SIS LMS … MIT Apache 2026` leg returned Forma LMS
(Apache-2.0), OpenOLAT (Apache-2.0), Open edX (AGPL-3.0), Sakai (ECL-2.0), Moodle (GPL), Canvas
(AGPL), RosarioSIS (GPL), OpenEduCat, openSIS and SchoolTool — **every one already carried**.
🔴 **Sixth independent channel to confirm that no major education SIS or LMS carries a permissive
grant** (`Gap 298` / `Gap 405-A`). 🔵 The permissive layer remains what these shelves already say it
is: integration clients, emitters and tutors, never the system of record.

## 🆕 `p418` · 2026-10-24 — **The foundational question this pass answers is "what is this repository's licence?" — and for a workspace monorepo the honest answer is a SET. 🔴 `OpenMAIC`: eight MIT grants and one `LGPL-3.0-or-later`.**

🟢 **Gates on arrival: 50 / 51**, the lone red `gate-census-union` control 24 (`Gap 400-B`,
deliberately red since `p398`). 🔵 One gate **added** this pass, so the standing check is now
**52 controls wide**: `gate-register-currency`.

### 🔴 A foundational repository can carry more than one grant, and the probe must enumerate

🟢 **The rule, stated for the foundations layer because this is where it costs the most:** a
repository's licence is **one cell per licence-shaped path**, never one cell per repository. Measured
this pass on [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC):

| grant | bytes | `sha256₁₂` | family |
|---|---|---|---|
| root + 7 × `packages/@openmaic/*` | `1 065` | `ba2525637432` | 🟢 **MIT** (identical in all eight) |
| `packages/mathml2omml/` | `7 652` | `e3a994d82e64` | 🔴 **LGPL-3.0** (manifest: `LGPL-3.0-or-later`) |

🔵 **Why the foundations shelf and not only the agents shelf:** the LGPL package is **vendored
third-party** (`mathml2omml` `0.5.0`, Johannes Wilm, upstream `fiduswriter/mathml2omml`), and
vendoring is a *foundation* decision. A consumer who forks `OpenMAIC` inherits the vendoring, the
build order (`build:packages` builds `mathml2omml` **first**) and the obligation — **35** tracked
paths of it. 🔴 **No root `THIRD-PARTY-NOTICES`**, so nothing in the repository announces it.

🟢 **The one-command enumeration, which is cheaper than being wrong:**

```sh
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/<slug> /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -E '(^|/)(LICEN[CS]E|COPYING)'
for p in <each path>; do git -C /tmp/x cat-file -p "HEAD:$p" | sha256sum; done
```

🔵 Then re-read each path on `raw.githubusercontent.com` with a calibrated control pair — this pass
did, and both channels agreed on every one of the nine payloads (controls: `package.json` → `200`,
`NO_SUCH_FILE_p418` → `404`).

### 🔴 A shared byte LENGTH is not identity — demonstrated on this base's own cells

🟢 `p312` settled that a byte length does not identify a **template**. This pass settles the adjacent
case: it does not identify a **payload** either. The `1 077` B MIT band on these shelves now holds
**four distinct digests**:

| address | bytes | `sha256₁₂` |
|---|---|---|
| [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) | `1 077` | `0eeb9d32caed` |
| [`jarmolkowicz/knowledge-base-modrn-mind`](https://github.com/jarmolkowicz/knowledge-base-modrn-mind) | `1 077` | `5e2f8f0fa782` |
| [`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) | `1 077` | `d150aadcccd2` |
| 🆕 [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) | `1 077` | `c6dca3b0db5b` |

🔴 **And `P564` asserted byte-identity across the band from a length alone**, pairing `aureuserp`
with [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) — which is **`1 078`** B,
`a76aa4a4405c`. `cmp` separates them; the delta is `aureuserp`'s **missing terminal newline**.
🟢 **`T101`: a `cmp`-identity claim carries BOTH digests or it is not recorded.**

### 🟢 `Gap 417-E` closed, and `Gap 298` confirmed from a fifth channel

🟢 [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) **resolves** — ref `master`
*(not `main`, which is what `p417` probed)*, HEAD `8f6e107` **2026-10-23**, `LICENSE` **MIT**
`1 077` B. 🔴 `p417` recorded the address as unresolvable under the slug `aureus-erp/aureus`;
**the correct slug was already on `agents/top.md:2330`** and `agents/trending.md:26550`.
🟢 **It is admitted as real permissive ERP supply** — with the standing caveat that it is a
*generic* ERP (`verticals/`), carries **no academic data model**, and is the same vendor as Krayin.

🔴 **`Gap 298` / `Gap 405-A` confirmed again, from the ERP/CRM leg:** OpenEduCat **LGPL-3.0**,
openSIS **GPL-2.0**, RosarioSIS **GPL-2.0**, Fedena **Apache-2.0**, Gibbon **GPL-3.0**, SchoolTool
**GPL-2.0**, OpenOlat **Apache-2.0**, GegoK12 **MIT but open-core and 120 d stale**. 🟢 **Five
independent channels now agree: no major education SIS is MIT.** The standing answer is unchanged —
**graft a permissive general CRM onto admissions rather than fork a copyleft SIS**.

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

### 🟢 One genuinely new foundational address — state-backed, AGPL-3.0, and at `p413`'s canonical digest

🟢 [`exelearning/exelearning`](https://github.com/exelearning/exelearning) is **unshelved**: *"eXe
Learning"*, *"exelearning"*, *"eXeLearning"* and *"iteexe"* each return **0 hits** across all eight
shelves and every `.tsv`. (*"eXe"* returns 340, all substring noise.)

| field | measured today |
|---|---|
| grant | 🟢 **AGPL-3.0** — `main/LICENSE`, **`34 523` B**, **`661`** lines, **`3` × `https://`**, `sha256:0d96a4ff68ad`, served `200` from `raw.githubusercontent.com` |
| stars | **150** |
| scale | **1 413** commits |
| what | Free/libre authoring tool for open educational resources: iDevice-composed interactive content, hierarchical index, **real-time collaborative editing**, export for Moodle and other platforms, offline installers for Linux/Windows/macOS |
| stack | Bun, Elysia, Kysely |
| governance | 🟢 **Spain's Ministry of Education, Vocational Training and Sports (MEFPD)**, through **Cedec-INTEF**, with regional administrations participating; originated in the eXeLearning.org project in **New Zealand**, state-led since **2010** |
| region | 🟢 **EMEA** |

🟢 **The digest is the load-bearing part, and it is a confirmation of `p413` from an eleventh
address.** `p413` measured the AGPL-3.0 revision family as two forms: **`34 523` B / 661 lines /
`3 × https://` / `sha256:0d96a4ff68ad`** and **`34 501` B / 662 lines / `3 × http://` /
`sha256:884b434957ba`**, over **10** addresses. 🟢 `exelearning` lands on the **first** form,
byte-identical and digest-identical, measured independently. 🔵 `p413`'s lattice now stands on
**11** addresses and has not needed an amendment.

### 🔴 A licence claim refuted — and the refutation is a FORK PAIR, with both payloads read

🔴 The authoring leg reported eXe Learning as **"GPL v2"**. 🟢 **That is right about the legacy
repository and wrong about the live one**, and both halves were read byte-level:

| address | grant payload, measured | verdict |
|---|---|---|
| [`exelearning/exelearning`](https://github.com/exelearning/exelearning) *(live)* | `main/LICENSE` — **`34 523` B**, 661 lines, `sha256:0d96a4ff68ad`, title *"GNU AFFERO GENERAL PUBLIC LICENSE"* | 🟢 **AGPL-3.0** |
| [`exelearning/iteexe`](https://github.com/exelearning/iteexe) *(legacy)* | `master/COPYING` — **`17 992` B**, **340** lines, `sha256:32b1062f7da8`, title *"GNU GENERAL PUBLIC LICENSE"*, **`Version 2, June 1991`** | 🟢 **GPL-2.0** |

🔵 **So the source was not wrong, it was stale by one repository** — the same shape `p404`'s
fork-direction work exists for, except that here the two halves carry **different licence families**,
not byte-identical ones. 🟢 **`T99` (new): on a project with a legacy and a live repository, a
licence family is a property of the ADDRESS, not the project name.** A proposal citing *"eXe
Learning, GPL-2.0"* is citing a repository that has been superseded, and copyleft **escalated**
GPL-2.0 → AGPL-3.0 across the move — which is the direction that matters, because AGPL's network
clause reaches a hosted authoring service where GPL-2.0 does not.

🔴 **Bound, stated plainly:** the GitHub page for `exelearning/exelearning` says content exports *"to
various formats"* and names Moodle; **it does not mention SCORM or xAPI.** One secondary source
claimed SCORM 1.2 + 2004 export. 🔴 **Unverified, and therefore not recorded as a SCORM emitter** —
`p416` closed the permissive-SCORM-producer scarcity with `Papermorph`, and this address is **not**
offered as a second instance. 🟡 `ACTION p417-B`: read `exelearning`'s export modules in-tree before
any SCORM claim is made for it.

### 🔵 The five-repo floor, and why it is not re-padded this pass

🟢 This file carries well above the five-repo minimum and `p417` adds **one** verified address rather
than padding. 🔴 **The prescribed ERP/CRM leg returned nothing new in-domain** and independently
confirmed `Gap 298` / `Gap 405-A`: it surfaced `OpenEduCat` (LGPL-3.0), `OpenSIS` (GPL-2.0),
`Fedena` (Apache-2.0), `RosarioSIS` (GPL), `Gibbon` (GPL-3.0), `SchoolTool` (GPL-2.0) and
`OpenOlat` (Apache-2.0) — **every one already carried**, and the leg's own conclusion is this base's:
**no major open-source education SIS is MIT-licensed.** 🟢 Fourth independent channel to agree; the
recommendation is unchanged — *integrate against the system of record, do not fork it*.


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

### 🟢 The interoperability layer finally has a PRODUCER, not only consumers

🔵 These shelves have carried the SCORM/LTI interoperability tier for many passes as a **read-side**
tier: libraries that *play* standards-conformant content inside or outside an LMS. Re-read
first-hand today, that tier is intact and permissive:

| Repo | Licence (sidebar, read today) | Stars | Role | Direction |
|---|---|---|---|---|
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **357** | JavaScript SCORM runtime: SCORM 1.2 and 2004, including Simple-Sequencing-based 2004 sequencing. Runs with any LMS or none | 🔵 **consumes** |
| [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** | **376** | Multi-tenant LTI tool-hosting environment and developer console; implements the IMS ContentItem app store. Apereo Incubating | 🔵 **hosts** |
| [`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 **MIT** | *(carried)* | Wraps H5P content so a SCORM-only LMS can run it | 🔵 **adapts** |
| [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4.1k** | FSRS scheduler for Anki plus an optimiser that fits parameters to a real review history | 🔵 **schedules** |
| 🆕 [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 **MIT** — `1 069` B, `sha256:41857092247a` | **849** | Textbook → narrated interactive lesson; **packages as SCORM 1.2 / 2004** (`scripts/scorm.py`); also exports video | 🟢 **PRODUCES** |

🟢 **The asymmetry this closes was declared on these shelves, not invented here.**
`agents/top.md:1815` records SCORM support as *"genuinely scarce in permissive open source"* while
pointing at a **source-closed** package; `agents/trending.md:5080` records a leg that named SCORM
explicitly and returned **"No SCORM result at all."** As of today the tier is complete in both
directions, under MIT at both ends.

🔵 **Why a producer is worth more than another runtime to a studio.** A runtime is something you ship
*to* the client's LMS and then support. A producer is something that leaves your build as a **file
the client's existing LMS already installs** — no integration project, no plugin review, no
procurement of a new system. That is the difference between an engagement that ends at a handover
and one that ends at an upload.

### 🟢 The research tier, re-read and unchanged

| Repo | Licence (sidebar, read today) | Stars | What it is |
|---|---|---|---|
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **451** | PyTorch library for training and benchmarking deep knowledge-tracing models on standardised preprocessing |
| [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | 🟢 **MIT** | **82** | Unified experimental pipeline across knowledge tracing, cognitive diagnosis, exercise recommendation and learning-path recommendation; `v1.0.0` in its own release table |
| [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) | 🟢 **MIT** | **79** | PyTorch library for student cognitive modelling (cognitive diagnosis + knowledge tracing), tied to a *Frontiers of Computer Science* 2025 paper. 🔵 Hefei University of Technology by organisation name; the page does not spell it out |
| [`bigdata-ustc/EduData`](https://github.com/bigdata-ustc/EduData) | *(carried)* | **314** | Education datasets with download and preprocessing tooling. 🔴 Last updated **2023-09-26** |

🔴 **One honest note on this tier: it is APAC-concentrated and ageing at the edges.** `pykt-toolkit`,
`pyedmine` and `EduStudio` are all China-origin and all live; `EduData` has not moved in three years.
A knowledge-tracing engagement composes entirely from in-region Chinese academic code — which is
fine under MIT, and worth saying out loud before a client discovers it in a dependency tree.

## 🆕 `p415` · 2026-10-23 — **The agent tier re-measured FIRST-HAND against the live GitHub sidebars, and three figures this base carried are refuted — one of them by a factor of 31.** 🟢 Fifteen agent addresses and nine foundations read today, every licence taken from the repository's own sidebar. 🔴 AND the read channel matters: `curl` and `api.github.com` are REFUSED for every repository not attached to this session, so a pass that reports "unreachable" from `curl` alone is reporting a fact about the CHANNEL.

🔵 **Dating note.** Every search leg and every licence read below was executed on **2026-10-23**, and the
commit lands **2026-10-23**. This is the twenty-first pass dated today, after `p395`–`p414`.

🔵 **Channel note, measured this pass.** `curl -sI https://github.com/CAHLR/OATutor` → **403**, and
`curl -s https://api.github.com/repos/HKUDS/DeepTutor` returns the session's own refusal body
(*"GitHub access to this repository is not enabled for this session"*), **not** GitHub's. The same
addresses read cleanly through `WebFetch`. Both instruments were run side by side before any address
below was written down. Every licence, star count and date in this pass came through `WebFetch`.

### 🟢 The foundation tier — nine addresses, every licence read from the sidebar on 2026-10-23

| Repo | Licence (sidebar, read today) | Stars | What it is | Build-on? |
|---|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | **8.2k** | The Open edX LMS + Studio: MOOC-scale delivery, cohorts, certificates, `XBlock` extension model | 🔴 **Integrate, do not fork.** AGPL reaches hosted services; extend through `XBlock` and the APIs |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** | **7.5k** | The most-deployed LMS in education worldwide; plugin architecture, AI-provider plugins live out of tree | 🔴 **Plugin boundary only.** GPL triggers on distribution, not on hosting |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | **6.9k** | Interactive tutor-style *explorations* that give learners feedback as they work — the pedagogy engine, not a gradebook | 🟢 **Yes — the largest permissive education platform on these shelves** |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** | **1.4k** | Assigning, collecting, autograding and returning Jupyter notebooks | 🟢 Yes — the default autograding substrate for anything CS/data |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1.2k** | **Offline-first** teaching and learning platform: full delivery with no internet requirement | 🟢 **Yes — and it is the single most important address for connectivity-constrained deployments** |
| [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 **BSD-3-Clause** | **451** | Rust implementation of **FSRS** — scheduler plus optimiser — the modern spaced-repetition algorithm | 🟢 Yes. Already the de-facto review scheduler across this field |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | **448** | Web-based LMS for teaching, assessment and communication; descends from OLAT at the University of Zurich, maintained by frentix | 🟢 **Yes — the only permissively-licensed full LMS here, and it is European** |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** | **152** | Framework-independent PHP library for H5P interactive content; plugs into LMS and CMS hosts | 🔴 Integrate through the host's plugin interface |
| [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🟢 **MIT** | **41** | Web portal for the **Sunbird** education stack — India's digital public infrastructure for learning | 🟢 Yes. 🔵 **Do not read 41★ as insignificance** — it is one module of a DPI stack deployed at national scale, and stars measure developer attention, not deployment |

### 🟢 The build-on set, stated plainly

**Permissive and therefore safe to fork into client work:** `oppia` (Apache-2.0), `kolibri` (MIT),
`OpenOLAT` (Apache-2.0), `nbgrader` (BSD-3), `fsrs-rs` (BSD-3), `SunbirdEd-portal` (MIT).

**Copyleft and therefore integration-only:** `edx-platform` (AGPL-3.0), `moodle` (GPL-3.0),
`h5p-php-library` (GPL-3.0). 🔵 The distinction that keeps getting lost: **GPL triggers on
distribution, AGPL triggers on network use.** Hosting a stock Moodle for a client is not a
distribution; shipping them a modified Moodle is. Hosting a *modified* Open edX is already the
trigger.

### 🔴 The gap this tier still has

🔴 **There is no permissively-licensed Student Information System.** The SIS field is
`RosarioSIS`, `Gibbon` and `Academico` — GPL or unstated — and the one MIT-licensed SIS a previous
pass found (`coderzaman/Student-Information-System`) is a teaching demo last touched in 2024.
**Any SIS work in an engagement is build-from-scratch or integrate-over-API; it is not fork-and-go.**
This gap has now survived every pass that looked for it.

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

### 🔴 `34 501` is not a revision — it is `acanas/swad-core`'s de-indented title line, and this base put its only `http` instance in the reference slot

🔵 `p413` closed `Gap 412-B` with a two-form model and this file still carries it: *"`https` **34 523**
B / 661 lines / 5 of 10"* against *"`http` **34 501** B / 662 lines / **1 of 10** (`acanas/swad-core`)"*.
🔴 **A reference derived from a single instance is a sample, and this one is the outlier.** 🟢 Seven
AGPL-3.0 payloads were read first-hand at a ref this pass, and the measurement that settles it is the
**leading indentation of line 1**:

| slug | bytes | lines | `https://` | title indent | sha256 |
|---|---|---|---|---|---|
| [`acanas/swad-core`](https://github.com/acanas/swad-core) | **34 501** | 662 | 0 | 🔴 **0 sp** | `884b434957ba` |
| [`mastodon/mastodon`](https://github.com/mastodon/mastodon) | **34 520** | 661 | 0 | 🟢 **20 sp** | `57c8ff33c9c0` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) *(rider stripped)* | **34 521** | 662 | 0 | 🟢 **20 sp** | `432d251a78db` |
| [`grafana/grafana`](https://github.com/grafana/grafana) | **34 523** | 661 | 3 | 🟢 **20 sp** | `0d96a4ff68ad` |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | **34 524** | 662 | 3 | 🟢 **20 sp** | `8d56b405468a` |
| [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) | **34 524** | 662 | 3 | 🟢 **20 sp** | `8d56b405468a` |

🔴 **`swad-core` is the only de-indented payload — 1 of 7.** Its `diff` against `edx-platform`'s base
is **two hunks and 20 bytes**: line 1 loses its 20 leading spaces, and the §"How to Apply" reflow at
lines 636–637 moves a word across a line break at **zero** byte cost. 🟢 So the `http` revision
**does** carry the canonical 20-space title indentation — `mastodon` and `edx-platform` both prove it
— and `34 501` is a **transcription artifact of one repository**, not a form of the licence.

🔴 **And this file's own closing arithmetic is numerically right and causally wrong.** It reads
**`34 501 + 20 + 3 − 1 = 34 523`** ✔ and attributes the `+20` to *"the title line's leading
indentation"* — correct as a mechanism — but then books it as a property of the **`http` form**.
🟢 It is a property of **`swad-core`**. 🔴 The `−1` fails the same way: this file calls it *"a trailing
blank line present in the `http` form and absent in the `https` one"*, yet `grafana` is `https` at
**661** lines and `blend-ed` is `https` at **662**. **The line count varies inside both schemes**, so
it is an independent axis, not a scheme property. 🟢 The identity balanced because two unrelated
terms happened to cancel.

🟢 **What replaces it: two independent axes over one base, and all four cells are measured.**

| cell | scheme | lines | bytes | instance read this pass |
|---|---|---|---|---|
| 1 | `http://` | 661 | **34 520** | `mastodon/mastodon` |
| 2 | `http://` | 662 | **34 521** | `openedx/edx-platform` *(under its rider)* |
| 3 | `https://` | 661 | **34 523** | `grafana/grafana` + the 5 this file already carries |
| 4 | `https://` | 662 | **34 524** | `blend-ed/openedx-mcp`, `blend-ed/tutor-contrib-openedxmcp` |

> **`bytes = 34 520 + 3·(scheme == https) + 1·(line 662 present)`**, and `swad-core` is that minus
> **20** for its de-indented title.

🔵 **`Pattern AI`'s `~34 522 B` still matches no cell, and this pass does not rehabilitate it.**
`intel/open-gaps.md` records it as matching neither form; against the lattice it matches none of the
**four**. 🟢 What changes is the bracket: it sits **inside** the span `34 520`–`34 524`, between cells
2 and 3. 🔴 The gap stays **OPEN** — a figure one byte from a real cell is still unprovenanced, and
`p413` was right that it reads as a subtraction.

🔵 **`openedx/edx-platform`'s rider, re-measured so the lattice can be checked against it.** Total
**35 136** B / **671** lines; strip the appended block and the base is **34 521** / **662** /
`432d251a78db` — **lattice cell 2, exactly**. 🟢 The rider is therefore a **pure append** of
**615 B / 9 lines**, which confirms `p413`'s own count of *"nine operative lines"* and refutes this
base's older cell at `repos/trending.md` reading *"`10` APPENDED lines"* — corrected on that shelf
this pass. 🔵 What the rider **says**, and the `NARROWED-OPERATIVE` consequence for a separate
RPC-speaking service beside Open edX, is `p413`'s finding and is **not** restated here.

🟢 Full table, with the off-lattice arithmetic, in
[`evidence/agpl-presentation-lattice.2026-10-23-p414.tsv`](../evidence/agpl-presentation-lattice.2026-10-23-p414.tsv).
🔵 The runnable selector that replaces Amendment 6 is **Amendment 7** on the patterns shelf.

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

### 🟢 `Gap 412-B` CLOSED — AGPL-3.0 measured first-hand on TEN addresses, and the answer is sharper than the question

🔵 **Every row below is a `GET` of `<branch>/LICENSE` on `raw.githubusercontent.com`, the one
allowlisted code channel, with a `404`-shaped negative control run in the same loop** (a
non-existent path returns a **14-byte** `404: Not Found` body, so a short read is never mistaken for
a grant).

| address | grant path | bytes | lines | `https://` | `http://` | sha256 (12) | `p378` text |
|---|---|---|---|---|---|---|---|
| [`sourcegrade/jagr`](https://github.com/sourcegrade/jagr) | `master/LICENSE` | **34 523** | 661 | 3 | 0 | `0d96a4ff68ad` | `2097961c7782` |
| [`ai-lingnan/econai-agent-platform`](https://github.com/ai-lingnan/econai-agent-platform) | `master/LICENSE` | **34 523** | 661 | 3 | 0 | `0d96a4ff68ad` | `2097961c7782` |
| [`wwyw4842-dot/OpenMAIC`](https://github.com/wwyw4842-dot/OpenMAIC) | `main/LICENSE` | **34 523** | 661 | 3 | 0 | `0d96a4ff68ad` | `2097961c7782` |
| [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) | `main/LICENSE` | **34 523** | 661 | 3 | 0 | `0d96a4ff68ad` | `2097961c7782` |
| [`chipmates/agoracosmica`](https://github.com/chipmates/agoracosmica) | `main/LICENSE` | **34 523** | 661 | 3 | 0 | 🔴 `8486a10c4393` | `2097961c7782` |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | `master/LICENSE` | **34 524** | 662 | 3 | 0 | `8d56b405468a` | `2097961c7782` |
| [`blend-ed/tutor-contrib-openedxmcp`](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master/LICENSE` | **34 524** | 662 | 3 | 0 | `8d56b405468a` | `2097961c7782` |
| [`idurar/idurar-erp-crm`](https://github.com/idurar/idurar-erp-crm) | `master/LICENSE` | 🔴 **34 230** | 661 | 3 | 0 | `7800536d5087` | `2097961c7782` |
| [`acanas/swad-core`](https://github.com/acanas/swad-core) | `master/LICENSE` | **34 501** | 662 | 0 | 3 | `884b434957ba` | 🟡 `d3d83b9336df` |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master/LICENSE` | 🔴 **35 136** | 671 | 0 | 3 | `e12d78569742` | 🔴 `0563ef8a5f99` |

🟢 **The headline, in one sentence, derived with this base's own instruments:** **`p312` sees SIX
templates over these ten payloads; `p378`'s presentation fold collapses them to THREE texts** — and
only **two** of the three are the FSF text at all.

🔵 **The two FSF forms, and the arithmetic closes EXACTLY.**

| form | bytes | lines | scheme | instances |
|---|---|---|---|---|
| `https` | **34 523** | 661 | 3 × `https://` | 5 of 10, byte-identical |
| `http` | **34 501** | 662 | 3 × `http://` | 1 of 10 (`acanas/swad-core`) |

🔴 **And `p412`'s GPL-3.0 arithmetic does NOT transfer.** The GPL-3.0 spread closed on the URL
scheme alone; the AGPL-3.0 spread of **22 B** closes on **three** mechanisms, of which the scheme is
the smallest:

> **+20** the title line's leading indentation · **+3** the three `http:`→`https:` upgrades ·
> **−1** a trailing blank line present in the `http` form and absent in the `https` one.
> **34 501 + 20 + 3 − 1 = 34 523** ✔

🟢 **What DOES transfer is `p412`'s discriminator, unchanged**: `grep -c 'https://'` returns **3** on
one form and **0** on the other, so **Amendment 5's in-tree selection works on AGPL-3.0 as written** —
`Pattern AJ` **Amendment 6** below records it. 🔵 **The `http` form has `n = 1` here**, so its
unindented title is a property of the one instance measured, not an established FSF property; the
discriminator does not depend on that and the arithmetic is stated per-instance.

### 🔴 `Pattern AI` step 4's AGPL reference is a SUBTRACTION, and its provenance is now identified

🔵 `Gap 412-B` predicted that the `~34 522 B` AGPL constant carried the same unrecorded-provenance
defect as the GPL-3.0 one. 🟢 **It does, and the source is on this base's own shelves.**
`repos/trending.md:14872` records `openedx/edx-platform`'s `35 136 B` with a **`614 B`** appended
edX block — and **`35 136 − 614 = 34 522`**. 🔴 **So the AGPL reference was never a measured FSF
payload: it is edx-platform's LICENSE minus a block.** It lands **1 B below** the `https` form and
**21 B above** the `http` one, matching neither.

🔴 **And the subtraction could not have been right**, because `edx-platform`'s base text combines
`http://` URLs with an **indented** title — a combination **neither** measured form has. 🟢 Subtracting
a block from a payload that is itself a fourth presentation cannot recover a canonical value. 🔵 The
repair is Amendment 6: **select the AGPL denominator in-tree by the same grep, never by subtraction.**

### 🔴 A byte band says "same", a digest says "different", and both answer the wrong question

🔵 `p196` recorded that *"three AGPL-3.0 texts here are `34 523` B exactly with different digests"*
and left identity at `(FILE, digest)`. 🟢 **The mechanism is now measured.**
[`chipmates/agoracosmica`](https://github.com/chipmates/agoracosmica) against
[`sourcegrade/jagr`](https://github.com/sourcegrade/jagr): **identical `34 523` B, identical 661
lines, different sha256** — and `diff` returns **exactly one hunk of two lines**, the hard-wrap of
the *How to Apply* appendix (`as published` / `by the Free Software Foundation` versus `as published
by` / `the Free Software Foundation`). 🔵 The wrap moves three bytes from one line to the next, so
the byte count cannot move. **Zero operative words differ.** 🟢 `p378` folds them to one text, which
is the correct answer and the reason that gate exists.

🟢 **`idurar/idurar-erp-crm` is the same class at ten times the amplitude.** `34 230` B is **293 B
short** of canonical at the **same 661 lines**, and `diff` returns **318 changed lines** — every one
of them a stripped leading indent or a collapsed double space after a full stop. 🔴 **A digest check
calls it not-AGPL; a byte band calls it not-AGPL; the header read calls it AGPL-3.0 — and the header
read is right.** 🟢 `p378` folds it onto the canonical text, so **the fold now spans `34 230` /
`34 523` / `34 524` B: a 294-byte spread on ONE text**, which ends any byte-band reading of this
family outright.

### 🔴 `openedx/edx-platform`'s grant is NARROWED, and this base carried the bytes without the consequence

🔵 `repos/trending.md:14851` already records *"`35 136 B` with `10` APPENDED lines from EdX Inc."* —
the bytes, the line count and the block size. 🔴 **What was never recorded is what the block SAYS**,
and it is the most commercially consequential licence sentence on this industry's vertical layer:

> EdX Inc. wishes to state, in clarification of the above license terms, that any public,
> independently available web service offered over the network and communicating with edX's
> copyrighted works by any form of inter-service communication, including but not limited to Remote
> Procedure Call (RPC) interfaces, is not a work based on our copyrighted work within the meaning of
> the license. "Corresponding Source" of this work, or works based on this work, as defined by the
> terms of this license do not include source code files for programs used solely to provide those
> public, independently available web services.

🟢 **That is `gate-subtree-grant`'s `NARROWED-OPERATIVE` class on the Open edX flagship**, and it is
the clause that makes a **separate** AI service beside Open edX, speaking to it over RPC, safe from
AGPL §13's network copyleft **on that service**. 🔴 A reader who grades this address `AGPL-3.0` by
header, by digest or by byte band never sees it — and that reader then refuses an engagement shape
the licence actually permits. 🟢 **`p378` correctly declines to fold `edx-platform` onto the stock
text**: nine operative lines are not presentation, and the gate's *"must never do"* control holds on
a family it was never built for.

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

### 🟢 A foundation-layer measurement that closes `p411`'s open finding 5

🔵 **Two of this base's foundation repositories settled a question `p411` left open as
unresolvable.** `p411` read GPL-3.0 at three sizes and concluded that, with `gnu.org` refused,
*“no authoritative denominator exists on this channel at all.”* 🟢 **It does not need one.**

| source | path | bytes | lines | CR bytes | `http://` | `https://` | revision |
|---|---|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | `COPYING.txt` | **35 147** | 674 | 0 | **4** | 0 | FSF text, **`http` scheme**, `philosophy/why-not-lgpl.html` |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `license.txt` | **35 149** | 674 | 0 | 0 | **4** | FSF text, **`https` scheme**, `licenses/why-not-lgpl.html` |
| `Pattern AI` step 4 | quoted constant | **~35 141** | unrecorded | unrecorded | unrecorded | unrecorded | 🔴 **matches NEITHER** — 6 B below the `http` revision, provenance unrecorded |

🟢 **The two revisions differ on exactly four lines and the arithmetic closes exactly:** three
lines gain **+1 B** each (`http:`→`https:`), and the fourth gains +1 while losing 2
(`philosophy/why-not-lgpl.html` → `licenses/why-not-lgpl.html`) ⇒ **35 147 + 3 − 1 = 35 149** ✔.
🔵 **Both files are 674 lines with zero CR bytes**, so line count and line endings are *not* the
discriminator — **the URL scheme is**, and `grep -c 'https://'` reads it in one command.

🔴 **Consequence for this shelf.** GPL-3.0 on these shelves is a **revision family of two**, not a
constant, and the base's own gate has been quoting a third number. 🟢 The repair is
`Pattern AJ` **Amendment 5** in [`compose/patterns.md`](../compose/patterns.md) — select the
denominator by the scheme grep rather than averaging or leaving it unsourced.

🔵 **What this does NOT change.** `frappe/education`'s 19-byte `license.txt` is **0.054 %** of
either revision, so `p411`'s finding 1 is robust to the whole spread — which is precisely why the
2-byte difference is *fatal to three significant figures and harmless to a 50 % floor*.
🔴 **Not verified this pass:** `Pattern AI` step 4's AGPL-3.0 reference (`~34 522 B`) was not
re-measured, so it may carry the same unrecorded-provenance defect. Registered as `Gap 412-B`.

### 🔴 `Gap 298`'s authorship axis, CORRECTED in place

🔴 **The `Gego-K12/gegok12` authorship cell on this file read “5 distinct authors” and is now
keyed to `%ae`, where it is 3.** Full history re-derived this pass: **123 commits**, **3 distinct
`%ae`**, **5 distinct `%an`**. 🔵 `p411` published all five *names with their counts*, so the
collapse needed no new probe — `Karthick` (34) + `GegoSoft` (4) + `karthick` (1) are **one email**,
`karthick@gegosoft.com`, totalling **39**, exact. 🔴 `devteam@gegok12.com` is a **shared role
account with 83 of 123 commits (67.5 %)**.

🟢 **The grant, the 7 623 tracked paths, the Laravel 12 / PHP 8.4 stack and the full container
chain are unaffected and remain first-hand.** 🔴 **What fails is the authorship inference**, and
`Gap 298` therefore does **not** close on the axis `p410` moved it to.

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

### 🟢 `Gap 298` — the permissive SIS has a BUILD now, and the remaining caveat is neither licence nor authorship

🔴 **Where `p410` left it.** `p409` measured the gap as currency (*“permissive grants on dead code,
live code copyleft”*). `p410` refuted that with [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement)
(MIT, 1 077 B, 19 d) and restated the absence as **authorship** — *“one author and no build file is
a bus factor of one.”*

🟢 **Probed this pass with a different wording, and the authorship restatement does not survive it.**

| | [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) — “GegoK12 School ERP” |
|---|---|
| licence | 🟢 **MIT**, root `LICENSE`, payload **1 150 B**, `Copyright (c) 2025 GegoSoft Technologies and GegoK12 Contributors` |
| default ref · HEAD | `main` · `99da145` **2026-06-25 — 🔴 120 d** |
| size | 🔴 **7 623 tracked paths** — far above `p176`'s 200-file enumeration threshold, so this is a **path-list** claim and is labelled as one |
| stack | PHP **8.4** / Laravel **12**, Livewire; MySQL; `docs/`, `api.md`, `lang/` |
| build + deploy chain | 🟢 **Complete and byte-counted**: `composer.json` 4 644 B · `package.json` 3 131 B · `Dockerfile` 1 108 B · `docker-compose.yml` 1 609 B · `.env.example` 1 402 B · `artisan` 1 686 B · `phpunit.xml` 961 B |
| authorship | 🔴 **123 commits across 3 distinct `%ae`, not 5** — `devteam@gegok12.com` 83 (shared ROLE account, 67.5 %), `karthick@gegosoft.com` 39, `abinaya@gegosoft.com` 1. 🔵 The **5** figure is `%an`, and `p411` published the list that refutes it: (`Devteam` 83, `Karthick` 34, `GegoSoft` 4, `karthick` 1, `AbinayaVelaMothilal` 1) — `Karthick` + `karthick` + `GegoSoft` are **one email**, 34+4+1 = 39. Still a **company**, not a person — but one role account and one human with more than a single commit *(`p412`: corrected in place, history not edited elsewhere)* |
| registrar depth | `app/` carries `Schoolplus`, `Calendar`, `Conference`, `Exports`, `Imports`, `Livewire`, `Observers`, `Policies`, `Presenters`, `Rules` |
| 🔴 what it is not | 🔴 **120 days stale** · 🔴 **open-core** — the vendor states the public repo is the free core and premium modules (online quiz, private chat, bus management) sit outside it · 🔴 **17 licence-shaped paths, 16 of them vendored** |

🟢 **So `Gap 298` moves a third time, and the wording that is left is the honest one.** A permissive
SIS exists; it has a real framework, a real build, a container and a company behind it. 🔴 **What
it does not have is currency and completeness**: a 120-day-old HEAD, and a feature set deliberately
partial because the paid modules are the business model.

🔵 **Consequence for a proposal, and it has changed AGAIN.** `p409` said *don't fork, integrate* —
reason: dead code. `p410` kept the advice on a new reason: bus factor. 🟢 **Neither reason applies
here.** For `gegok12` the question is **open-core scope**: fork-and-own is viable (MIT, real build),
but a studio must first enumerate **which modules the client needs and which of those are premium**,
because the gap between the demo and the repository is the vendor's revenue. **That is a
scoping exercise, not a licence or maintenance risk, and it belongs in the SOW rather than the
risk register.**

### 🔴 The vendored-grant trap at scale — `p410`'s `School-CRM` finding, one order of magnitude up

🔴 `p410` flagged `addex12/School-CRM` for carrying **five** licence-shaped paths of which **four**
were dependency grants. 🔴 **`gegok12` carries 17, and 16 are vendored** —
`custompackages/brozot/laravel-fcm/LICENSE` plus **fifteen webpack-emitted
`public/js/<chunk>.js.LICENSE.txt` banners**.

🔵 **The new part is the shape, not the count.** `Pattern AI` step 2 discards grants under
`vendor/`, `node_modules/`, `third_party/` and `native/*/packages/`. 🔴 **None of those prefixes
matches `public/js/` or `custompackages/`** — the first is a **build artefact** directory and the
second is a project-specific vendor directory. **A first-hit reader of a recursive listing here
lands on a minified bundle's banner.** `Pattern AJ` below fixes the rule.

### 🔴 The Frappe family — four sibling repositories, four grant shapes, and the education one is the broken one

🟢 **Read first-hand this pass, same org, same channel, one command each:**

| repository | grant path | payload | named | manifest channel | 
|---|---|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | `LICENSE` | **1 118 B** | MIT | 🟢 `package.json` `"MIT"` |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `license.txt` | **35 149 B** | GPL-3.0 | 🟢 `package.json` `"GPL-3.0"` |
| [`frappe/lms`](https://github.com/frappe/lms) | `license.txt` | **33 893 B** | AGPL-3.0 | 🟢 `package.json` `"AGPL-3.0-or-later"` |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | `license.txt` | 🔴 **19 B** | “GNU GPL V3” | 🔴 **none — no `license` field anywhere** |

🟢 **`frappe/lms` at 33 893 B reproduces this base's own `p209` read to the byte** — an
independent re-measurement 202 passes later, and the *MIT* claim `p209` killed stays killed.

🔴 **The finding is the contrast, and it resolves finding 1 rather than just restating it.** Three
siblings ship full payloads with agreeing manifests. **The same organisation demonstrably knows how
to ship a grant** — so `frappe/education`'s 19 bytes are a **shortcut, not a different intent**.

🟢 **And that separates two things `Pattern AI` step 4 currently conflates.** The ratio test returns
`NOTICE-OR-STUB` for both `addex12/School-CRM` (874 B of Apache notice, manifest says MIT, three
channels three answers) and `frappe/education` (19 B, no manifest, siblings agree). 🔴 **They are
not the same risk.** The first **conceals** a conflict; the second merely **under-documents** a
grant that three sibling repositories corroborate — and in a direction that costs a studio nothing,
because GPL-3.0 is the *more* restrictive reading and adopting it is the safe error.

🔵 **Rule, cheap and new:** when a grant payload fails the ratio test, **read the organisation's
sibling repositories before reporting it as a defect.** Thinness and deception are different
findings with different answers, and the sibling read is one `ls-tree` per repo.

### 🔴 The census, carried forward and marked NOT re-derived

🔴 Unchanged from `p409`'s figures — **2 695 addresses / 3 529 over both channels** — and `STALE`
for a third consecutive pass. **`p411` shelves 15; `p410` shelved 8; expect +23.** `make
address-shape-census` is code in this clone and this session will not execute it.

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

### 🟢 `Gap 298` — the permissive SIS exists, and the restated absence is *authorship*, not code

🔴 **`p409` measured the gap as a currency problem:** *“the permissive SIS grants sit on dead code,
and the live SIS code is copyleft,”* on the evidence of [`coderzaman/Student-Information-System`](https://github.com/coderzaman/Student-Information-System)
(MIT, 1,069 B, **726 d** stale, a teaching demo). The register's own note was franker still: *“Not
probed this pass: whether a permissive SIS exists at all.”*

🟢 **Probed this pass. It exists.**

| | [`shrikrishna-lab/StudentManagement`](https://github.com/shrikrishna-lab/StudentManagement) — “EduTrack ERP” |
|---|---|
| licence | 🟢 **MIT**, payload **1,077 B**, root `LICENSE`, title line `MIT License` |
| default ref · HEAD | `main` · `e75afa5` **2026-10-04 — 19 d** |
| size | **156 tracked paths**, enumerated (below `p176`'s 200-file enumeration threshold, so this is not a path-list claim) |
| tiers | `frontend/` React 18/19 + Vite 6 · `server/` Express 4.21 + WebSocket · `backend/` Java 21 DAO layer |
| deployable? | 🟢 `database/student_management.sql`, `frontend/package.json`, `server/package.json`, `.env.example`, `DESIGN.md`, `CONTRIBUTING.md` |
| registrar depth | 🟢 `SemesterTranscriptDAO`, `StudentClearanceDAO`, `CertificateRequestDAO`, `ExamScheduleDAO`, `AttendanceDAO`, `MarksDAO`, `TeacherDAO`, `UserCredential` |
| 🔴 what it is not | **single author** (`com.krrish`) · a vendored `mysql-connector-j-8.4.0.jar` compiled from a hand-written `backend/sources.txt` with **no `pom.xml` or `build.gradle`** · `data/students.txt` as a flat file · a README trading in *“Apple-grade frosted glassmorphic”* and *“sub-millisecond”* |

🟡 **So the gap moves rather than closes, and the new wording is the useful part.** Transcripts,
clearance and certificate requests are **registrar** functions, not CRUD — this is somebody who has
seen a real academic office. 🔴 But one author and no build file is a **bus factor of one**, and
that is a different risk from a licence risk and has a different answer.

🟢 **Consequence for a proposal, and it has CHANGED.** `p409`'s advice — *“don't fork the SIS,
integrate against it”* — was right for the reason it gave (dead code) and that reason no longer
holds. 🔵 The advice **survives on a new reason**: fork-and-own on a single-author tree makes the
studio the maintainer of a student-records system on day one. **Read it for the schema** — the
`.sql` and the DAO layer are the reusable asset — and integrate against the institution's system of
record, per `Pattern AH`.

### 🔴 `addex12/School-CRM` — why it is NOT a foundation, stated with the measurement

🔴 **Default ref `develop`** (not `main`, not `master` — a third shape, and a probe hardcoding
either misses this tree entirely). HEAD `011a98c` **2025-05-10 · 531 d**.

🔴 **Five licence-shaped paths in the tree, and FOUR are vendored dependencies**: `LICENSE`,
`PhpSpreadsheet/LICENSE`, `vendor/cboden/ratchet/LICENSE`, `vendor/composer/LICENSE`,
`vendor/composer/pcre/LICENSE`. 🔵 A reader who takes the first hit from a recursive listing can
land on **Composer's** grant and attribute it to the project.

🔴 **And the root payload is 874 B against Apache-2.0's 11,358 B.** It is a notice, the manifest
says MIT, and the tree is 531 days stale. **Not a foundation on any of the three counts.**

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

### 🔴 `Gap 298` re-tested — still **no permissive SIS**, and the one new MIT candidate shows why the gap is structural

🟢 **The gap was declared, not inherited: `intel/open-gaps.md:18062` — "no SIS platform with a
permissive grant, and the SIS is where the records live."** This pass ran the leg again
(`open source student information system SIS MIT Apache license github 2026`) and the answer has
not changed in the direction that matters.

| candidate | grant | state | why it does not close `Gap 298` |
|---|---|---|---|
| 🆕 [coderzaman/Student-Information-System](https://github.com/coderzaman/Student-Information-System) | 🟢 **MIT** *(1,069 B, payload-read)* | 🔴 HEAD `9714b11` **2024-10-27 — 726 d** | **The only MIT SIS the leg returned.** A PHP/MySQL university-operations demo with admin/teacher/student panels. 🔴 Permissive and *abandoned by two years* — a grant with nothing live under it. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 | 🟢 live (already shelved) | Copyleft. The leg returned it as *"updated Oct 17, 2026"* — liveness confirms the shelf, licence does not move. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | already shelved | The most complete free option on the leg's own reading — and still not permissive. |
| [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | already shelved | — | Returned again via the GitHub `student-information-system` topic. |
| `foradian/fedena` / `projectfedena/fedena` | Apache-2.0 *(per the leg; already shelved)* | 🔴 no 2026 activity shown | The one **Apache** SIS lineage, and the leg itself could not date it. |
| openSIS | 🔴 GPL-2.0 | — | Already carried, **with its own licence trap** (grant one directory down). |

🔴 **So the shape of `Gap 298` is now measured rather than asserted: the permissive SIS grants that
exist sit on dead or toy code, and the live SIS code is copyleft.** 🔵 That is a different problem
from scarcity, and it has a different answer — for a client that cannot take AGPL/GPL into its own
SIS extension, the move is not "find a permissive SIS" but **leave the SIS where it is and integrate
against it**, which is what `compose/patterns.md` Pattern AH does.

🔵 **Re-dated, not re-asserted.** `Gap 298` is now **checkable**: the next pass can re-run this one
leg and compare six rows, rather than re-deciding the question from scratch.

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

### 🆕 `p406` — the foundation tier swept for decay, and one carried row is a REPAIR not a deletion

🟢 **Five of this shelf's addresses do not resolve** (`ale-alejandro/beadkit`, `apereo/opencast`,
`superbuilders/timeback-dev-python`, `thanh01pmt/interactive-quiz-kit`, and the base's own
dead-address control). 🟢 **All five are already carried AS dead or AS unreadable on this shelf** —
`apereo/opencast` has had its live successor and a redirect row since `p230` — so **no foundation row
recommends an address that answers nothing.**

🟢 **`opencast/opencast` re-verified first-hand this pass**, and it is the strongest state any carried
row is in: `EXISTS-PUBLIC` at **`153d1b1`**, last commit **2026-10-22**, licence title line
**`Educational Community License, Version 2.0 (ECL-2.0)`** read from a shallow clone. 🟡 ECL-2.0 is an
Apache-2.0 derivative with a **patent-grant clause narrowed to the licensor's own contributions** —
permissive enough to build on, and it is **not** on the MIT/Apache shortlist a Globant engagement
usually prices against, so it is named here rather than silently folded in.

| foundation row | address | licence | state, 2026-10-23 |
|---|---|---|---|
| Lecture capture + video pipeline | [opencast/opencast](https://github.com/opencast/opencast) | 🟡 **ECL-2.0** | 🟢 `EXISTS-PUBLIC` `153d1b1`, commit **2026-10-22** |
| 🔴 *(superseded)* | `apereo/opencast` | — | 🔴 `ABSENT-OR-PRIVATE` — **MOVED**, not dead; redirect row at line ~747 |

🔵 **The MOVED state is not a verdict this channel can return.** `p293`'s bound names two inseparable
cases — absent and private — and this is a **third**: the address refuses, the artefact is alive at
another address. Control `C7c` forbids inventing a `MOVED` token from a sweep, because a move is only
establishable by probing a **guessed successor**, which is evidence about the guess. 🟢 Guessed
successors were probed for the other 11 dead build-on-tier addresses: **11 of 11 refused.**

### 🟢 One new foundation-adjacent address, licence read at a pin

| repo | licence | pin · recency | why it is a CENSUS row and not a foundation row |
|---|---|---|---|
| [StudentTraineeCenter/edu-agent](https://github.com/StudentTraineeCenter/edu-agent) | **MIT** *(title line, `(c) 2025 Student Trainee Center`)* | `77c9ee5` · **2025-12-30** · 511 tracked files | 🟢 The most substantial new address this pass — LangGraph + RAG over course documents, with `alembic`, `uv.lock`, `docker-compose`, `deploy/` and `docs/`, i.e. a **deployable** shape rather than a demo. 🔴 **Ten months without a commit.** Per the `Continue` rule a dormant artefact stays a census address and is **not** promoted to a build-on tier |

🔵 **The `Continue` rule is doing real work here**, and it is worth restating because the temptation
runs the other way: 511 tracked files and a lockfile look like production, and dormancy is the signal
that survives a demo's polish. A foundation row is a thing an engagement **depends** on.

🟡 **And a decay channel is not a payload channel.** Two carried addresses answer `EXISTS-NO-REFS` —
[`cdweaver1992/edfi-mcp-server`](https://github.com/cdweaver1992/edfi-mcp-server) and
[`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback)
— **empty repositories, which EXIST**. A row keyed on either passes a 404 check and still ships no
code. 🔵 Named so a successor does not read `EXISTS-PUBLIC` as *"there is something to build on."*

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
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 🔴 `master` | 🟢 **MIT** *(`LICENSE`, 1,072 B, "Copyright (c) 2018 Project Sunbird")* | 🟢 **The counter-example to this file's opening thesis, and the largest one available: a permissive grant at NATIONAL-PLATFORM scale.** Sunbird ED is the building block **DIKSHA**, India's national school platform, is built on — so unlike every other permissive row here it comes with a ministry adopter rather than a pilot. 🔴 **The cost is maintenance, and it is large:** HEAD `9efc8b5` **2025-12-16 — 311 d**. Fork at a pinned SHA, run the client's CVE sweep before week 1 ends, and price a maintenance line; this is a fork-and-maintain base, not an integrate-and-extend one. 🔵 The exact inverse of Moodle's trade (current code, hostile grant) — see `Pattern AG`. 🔴 Sibling `Sunbird-Ed/sunbird-learning-platform` **resolves no ref** and must not be named in a deliverable; a failed resolve cannot distinguish private from deleted. |
| 🆕 `p408` [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | `main` | 🟢 **MIT** *(`LICENSE`, 1,078 B)* | The handset client for the row above, and the surface that matters wherever the learner's only device is a phone. 🔴 HEAD `9de5e08` **2025-09-19 — 399 d**, staler than the portal, so the mobile path carries the heavier maintenance share. 🔵 Pairs with [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT) rather than competing with it: Kolibri owns the offline-first runtime, this owns the DPI-aligned content contract. |

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
